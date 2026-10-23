#!/usr/bin/env python3
"""Publication checks and bounded replays; L1 and external review stay open."""
import sys
if not __debug__:
    raise SystemExit('Python -O/-OO is rejected')
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import tempfile
from fractions import Fraction

HERE = Path(__file__).resolve().parent
BASE = 'beb38c9d1cba666bb3b7ddab9577873e59d854c4'

def need(ok, message):
    if not ok:
        raise ValueError(message)

def read(path):
    return json.loads(path.read_bytes())

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def bound_path(root, name):
    p = PurePosixPath(name)
    need(not p.is_absolute() and '..' not in p.parts and '\\' not in name, 'Invalid bound path')
    out = root.joinpath(*p.parts)
    need(out.resolve().is_relative_to(root.resolve()) and not out.is_symlink(), 'Escaping bound path')
    return out

def check_bytes(raw, expected, name):
    need(digest(raw) == expected, 'Bound bytes differ: ' + name)

def check_manifest(root):
    manifest = read(root / 'MANIFEST.json')
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    need(actual == set(manifest) | {'MANIFEST.json'}, 'Manifest coverage: ' + str(root))
    for name, sha in manifest.items():
        check_bytes(bound_path(root, name).read_bytes(), sha, name)
    return len(manifest)

def check_scope(scope):
    need(scope['L1']['status'] == 'OPEN', 'L1 must remain OPEN')
    need(scope['mathematical_status'] == 'AUTHOR_DERIVED', 'No status promotion')
    need(scope['review_status'] == 'EXTERNAL_REVIEW_OPEN', 'External review remains open')
    need(scope['second_direction_started'] is False, 'No second direction')
    need(set(scope['L1']['includes']) == {'LOW-HIGH-SOURCES', 'H-SOURCE', 'REST-CATALOGUE'}, 'Incomplete L1 mapping')

NUMBER_SPECS = [
    ('residual_energy', 'finite-audit/evidence/rational-cross-audit.json', ['repaired_Ldual_energy_upper'], False, '4.632e-11', 'L-dual energy'),
    ('continuous_corrected_u_norm', 'finite-audit/evidence/source-caps.json', ['values', 'continuous_corrected_u_norm'], True, '3.240e17', 'X norm'),
    ('moment_chain_factor', 'finite-audit/evidence/source-caps.json', ['values', 'explicit_moment_chain_factor'], True, '2.021e22', 'amplification factor'),
    ('moment_chain_X', 'finite-audit/evidence/source-caps.json', ['values', 'explicit_moment_chain_X'], True, '8.570e-257', 'X norm'),
    ('whole_source_transport', 'finite-audit/evidence/finite-RESULT.json', ['whole_force_transport', 'values', 'full_force_operator_upper'], True, '6.051', 'D-weighted transport to L-dual norm'),
    ('raw_operator', 'finite-audit/evidence/raw-operator-result.json', ['bounds_with_half', 'raw_g_and_density_adjoint'], True, '11.439', 'operator norm'),
    ('cache_difference_X', 'finite-audit/evidence/cache-price.json', ['complete_difference_X_upper'], False, '5.989e-888', 'X norm'),
    ('tiny_rest_budget', 'finite-audit/evidence/cache-price.json', ['new_joint_raw_equivalent_upper'], False, '7.729e-239', 'source budget equivalent; not inverse norm inference'),
]

def canonical_numbers(root=HERE):
    result = {}
    for name, path, keys, interval, cap, units in NUMBER_SPECS:
        raw = (root / path).read_bytes()
        value = json.loads(raw)
        for key in keys:
            value = value[key]
        upper = Fraction(value[1] if interval else value)
        need(upper >= 0 and upper < Fraction(cap), 'Numeric cap failed: ' + name)
        result[name] = {'source': path, 'source_sha256': digest(raw), 'keys': keys,
                        'exact_upper': str(upper), 'strict_display_cap': cap, 'units': units}
    return result

def check_package(root=HERE):
    count = check_manifest(root)
    for sub in ('finite-audit', 'model-connection', 'joint-audit'):
        check_manifest(root / sub)
    check_scope(read(root / 'STATUS.json'))
    need(read(root / 'NUMBERS.json') == canonical_numbers(root), 'Canonical number record differs')
    sources = read(root / 'finite-audit/SOURCE_BINDINGS.json')
    model = read(root / 'model-connection/SOURCE_FILES.json')
    need(sources['base_commit'] == model['commit'] == BASE, 'Source commit differs')
    need(len(sources['repository_files']) == 668, 'Expected 668 pinned source files')
    need({n: v['sha256'] for n, v in sources['repository_files'].items()} == model['files'], 'Source inventories differ')
    return count

def export_sources(repo, out):
    bindings = read(HERE / 'finite-audit/SOURCE_BINDINGS.json')['repository_files']
    tree = subprocess.check_output(['git', '-C', str(repo), 'ls-tree', '-rz', BASE])
    blobs = {}
    for row in tree.split(b'\0'):
        if row:
            meta, name = row.split(b'\t')
            blobs[name.decode()] = meta.decode().split()[2]
    need(all(blobs.get(n) == v['git_blob_sha1'] for n, v in bindings.items()), 'Pinned tree differs')
    out.mkdir(parents=True)
    # Stream the exact Git blobs. Working-tree files (including PR A) are not inputs.
    proc = subprocess.Popen(['git', '-C', str(repo), 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        for name, item in bindings.items():
            proc.stdin.write((item['git_blob_sha1'] + '\n').encode()); proc.stdin.flush()
            header = proc.stdout.readline().decode().split()
            need(len(header) == 3 and header[1] == 'blob', 'Missing source blob: ' + name)
            raw = proc.stdout.read(int(header[2])); need(proc.stdout.read(1) == b'\n', 'Invalid blob framing')
            check_bytes(raw, item['sha256'], name)
            target = bound_path(out, name); target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(raw)
    finally:
        proc.stdin.close(); proc.stdout.close(); need(proc.wait() == 0, 'Git source export failed')
    return len(bindings)

def replay(repo, work):
    import flint
    need(flint.__version__ == '0.9.0', 'Use python-flint 0.9.0')
    source = work / 'snapshot'
    count = export_sources(repo, source)
    env = os.environ.copy(); env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1')
    def run(*args, seed='0'):
        env['PYTHONHASHSEED'] = seed
        subprocess.run([sys.executable, '-u', '-B', *map(str, args)], check=True, env=env)
    for seed in ('0', '1'):
        run(HERE / 'model-connection/reproduce.py', '--snapshot', source,
            '--run-dir', work / ('model-seed-' + seed), seed=seed)
    run(HERE / 'joint-audit/reproduce.py', '--snapshot', source, '--run-dir', work / 'joint')
    run(HERE / 'finite-audit/scripts/source_cap_audit.py', '--repo', source, '--out', work / 'caps')
    fresh = read(work / 'caps/source-caps.json'); old = read(HERE / 'finite-audit/evidence/source-caps.json')
    fresh.pop('seconds', None); old.pop('seconds', None)
    need(fresh == old, 'Source cap deterministic fields differ')
    return {'pinned_sources': count, 'model_hash_seeds': [0, 1], 'joint_review_reproduced': True,
            'source_caps_reproduced': True, 'historic_panels_reintegrated': False,
            'cache_recomputed_in_this_replay': False,
            'cache_evidence': 'finite-audit/evidence/PORTABLE_REPLAY.json'}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=HERE.parents[2])
    ap.add_argument('--replay', action='store_true')
    ap.add_argument('--report', type=Path)
    args = ap.parse_args()
    report = {'status': 'BOUNDED_PUBLICATION_CHECK_PASS_CONDITIONAL', 'manifest_entries': check_package(),
              'base': BASE, 'L1': 'OPEN', 'external_review': 'EXTERNAL_REVIEW_OPEN'}
    if args.replay:
        with tempfile.TemporaryDirectory(prefix='objekt-x-model-publication-') as temp:
            report['replay'] = replay(args.repo.resolve(), Path(temp))
    if args.report:
        need(not args.report.resolve().is_relative_to(HERE), 'Write reports outside the package')
        args.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
