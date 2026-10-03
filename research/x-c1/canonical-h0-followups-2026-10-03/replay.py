"""Replay the unchanged, nested H0 packages at the current integration commit."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import fnmatch
import json
import os
import subprocess
import sys
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_path(root, name):
    p = PurePosixPath(name)
    assert name and '\\' not in name and ':' not in name and not p.is_absolute(), name
    assert all(x not in ('', '.', '..') for x in name.split('/')), name
    target = root.joinpath(*p.parts)
    assert target.resolve().is_relative_to(root.resolve()) and not target.is_symlink(), name
    return target


def extract(archive, target, binding):
    assert digest(archive.read_bytes()) == binding['archive_sha256'], 'archive hash'
    prefix = binding['folder'] + '/'
    with zipfile.ZipFile(archive) as z:
        expected = {prefix + name for name in binding['files']}
        assert len(z.namelist()) == len(expected) and set(z.namelist()) == expected, 'archive members'
        assert z.testzip() is None, 'archive CRC'
        for name, expected_hash in binding['files'].items():
            p = safe_path(target, name)
            info = z.getinfo(prefix + name)
            assert (info.external_attr >> 16) & 0o170000 != 0o120000, 'archive symlink'
            raw = z.read(prefix + name)
            assert digest(raw) == expected_hash, 'file hash: ' + name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw)
    manifest = json.loads((target / 'MANIFEST.json').read_bytes())['sha256']
    assert set(binding['files']) == set(manifest) | {'MANIFEST.json'}, 'closed source manifest'
    for name, expected_hash in manifest.items():
        assert digest(safe_path(target, name).read_bytes()) == expected_hash, name


def controls():
    """Exercise failures at the publication boundary, not certificate arithmetic."""
    rejected = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name in ('../escape', '/absolute', 'x/../escape', 'x\\escape', 'C:escape'):
            try:
                safe_path(root, name)
            except AssertionError:
                rejected.append(name)
            else:
                raise AssertionError('unsafe path accepted: ' + name)
        archive = root / 'tiny.zip'
        raw = b'unchanged bytes\n'
        manifest = json.dumps({'sha256': {'data.txt': digest(raw)}}).encode()
        with zipfile.ZipFile(archive, 'w') as z:
            z.writestr('original/data.txt', raw)
            z.writestr('original/MANIFEST.json', manifest)
        binding = {'folder': 'original', 'archive_sha256': digest(archive.read_bytes()),
                   'files': {'data.txt': digest(raw), 'MANIFEST.json': digest(manifest)}}
        extract(archive, root / 'valid', binding)
        for kind in ('archive_hash', 'file_hash', 'members'):
            bad = json.loads(json.dumps(binding))
            if kind == 'archive_hash':
                bad['archive_sha256'] = '0' * 64
            elif kind == 'file_hash':
                bad['files']['data.txt'] = '0' * 64
            else:
                bad['files']['missing.txt'] = '0' * 64
            try:
                extract(archive, root / kind, bad)
            except AssertionError:
                rejected.append(kind)
            else:
                raise AssertionError('damaged binding accepted: ' + kind)
    assert len(rejected) == 8
    workflow = (REPO / '.github/workflows/canonical-h0-followups.yml').read_text(encoding='utf-8')
    filters = [line.strip()[3:-1] for line in workflow.splitlines() if line.strip().startswith('- "')]
    expected = ['research/x-c1/canonical-h0-followups-2026-10-03/**',
                'research/x-c1/canonical-y-kernel-second-order-2026-10-03/**',
                '.github/workflows/canonical-h0-followups.yml']
    assert filters == expected + expected
    routed = lambda path: any(fnmatch.fnmatchcase(path, p) for p in expected)
    assert routed('research/x-c1/canonical-h0-followups-2026-10-03/replay.py')
    assert routed('research/x-c1/canonical-y-kernel-second-order-2026-10-03/SOURCE_BINDINGS.json')
    assert routed('.github/workflows/canonical-h0-followups.yml')
    assert not routed('README.md') and not routed('00-uebersicht/RESEARCH_STATE.yaml')
    assert 'pull_request:' in workflow and 'branches: [main]' in workflow
    assert 'github.event.pull_request.head.sha || github.sha' in workflow
    assert workflow.index('core.autocrlf false') < workflow.index('actions/checkout@')
    return {'valid_archive_accepted': True, 'rejected_controls': rejected, 'CI_routing': 'PASS'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--controls-only', action='store_true')
    args = parser.parse_args()
    tested = controls()
    if args.controls_only:
        print(json.dumps(tested))
        return
    assert args.output, '--output is required'
    out = args.output.resolve()
    assert not out.exists() and not out.is_relative_to(REPO.resolve()), 'new output outside repository required'
    binding = json.loads((HERE / 'SOURCE_BINDINGS.json').read_bytes())
    out.mkdir(parents=True)
    packages = {}
    for spec in binding['packages']:
        if spec['key'] == 'three_cut':
            archive = safe_path(HERE, spec['archive'])
        else:
            parent, name = spec['archive'].split('/', 1)
            archive = safe_path(packages[parent], name)
        target = out / 'originals' / spec['folder']
        extract(archive, target, spec)
        packages[spec['key']] = target
    for name, row in binding['visible_copies'].items():
        raw = safe_path(HERE, name).read_bytes()
        assert digest(raw) == row['sha256']
        assert raw == safe_path(packages[row['package']], row['path']).read_bytes(), name
    # The old source embedded in the pullback must equal PR206's canonical archive.
    kernel = REPO / 'research/x-c1/canonical-y-kernel-second-order-2026-10-03'
    kernel_binding = json.loads((kernel / 'SOURCE_BINDINGS.json').read_bytes())
    pull = packages['pullback']
    source = pull / 'inputs/PR206_SOURCE.zip'
    assert source.read_bytes() == safe_path(kernel, kernel_binding['archive']).read_bytes()
    steps, receipts = [], []

    def run(label, script, arguments):
        with (out / (label + '.log')).open('wb') as log:
            proc = subprocess.run([sys.executable, '-B', str(script), *map(str, arguments)],
                                  stdout=log, stderr=subprocess.STDOUT,
                                  env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8'))
        assert proc.returncode == 0, label + ' failed; inspect log'
        steps.append(label)
        print(label + ': PASS', flush=True)

    def compare(generated, expected):
        assert generated.read_bytes() == expected.read_bytes(), str(expected)
        receipts.append({'file': generated.relative_to(out).as_posix(),
                         'sha256': digest(generated.read_bytes()), 'byte_identical': True})

    run('pullback', pull / 'verify_pullback.py', ['--source-archive', source,
        '--prior-diagnosis', pull / 'inputs/ROOT_DIAGNOSIS_GPT1.json', '--out', out / 'pullback'])
    for name in ('PULLBACK.json', 'FACTOR_COMPARISON.json'):
        compare(out / 'pullback' / name, pull / name)
    run('pullback_audit', pull / 'audit_pullback.py', ['--source-archive', source,
        '--receipt', out / 'pullback/PULLBACK.json', '--out', out / 'PULLBACK_AUDIT.json'])
    compare(out / 'PULLBACK_AUDIT.json', pull / 'PULLBACK_AUDIT.json')
    run('factor_audit', pull / 'audit_factors.py', ['--source-archive', source,
        '--receipt', out / 'pullback/FACTOR_COMPARISON.json', '--out', out / 'FACTOR_AUDIT.json'])
    compare(out / 'FACTOR_AUDIT.json', pull / 'FACTOR_AUDIT.json')
    run('endpoint_and_783', packages['root'] / 'reproduce.py', ['--out', out / 'root'])
    root_receipt = json.loads((out / 'root/REPRODUCTION.json').read_bytes())
    assert root_receipt['status'] == 'PASS' and root_receipt['stored_multipliers_exactly_audited']
    assert not root_receipt['numeric_search_repeated']
    run('three_cut', packages['three_cut'] / 'reproduce.py', ['--out', out / 'three_cut'])
    cut_receipt = json.loads((out / 'three_cut/REPRODUCTION.json').read_bytes())
    assert cut_receipt['status'] == 'PASS' and len(cut_receipt['receipts']) == 8
    run('strategy_algebra', HERE / 'check_strategy_algebra.py', [])
    head = subprocess.check_output(['git', '-c', 'safe.directory=' + REPO.as_posix(),
                                    '-C', str(REPO), 'rev-parse', 'HEAD']).decode().strip()
    record = {'status': 'PASS', 'integration_commit': head, 'source_head': binding['source_head'],
              'binding_sha256': digest((HERE / 'SOURCE_BINDINGS.json').read_bytes()),
              'source_archives': {p['key']: p['archive_sha256'] for p in binding['packages']},
              'source_file_count': sum(len(p['files']) for p in binding['packages']),
              'steps': steps, 'publication_controls': tested, 'pullback_receipts': receipts,
              'endpoint_and_783': root_receipt, 'three_cut': cut_receipt,
              'reported_block45_numeric_replay': False, 'root_status': 'UNRESOLVED',
              'scope': 'Finite source-bound replay; original operator reconstruction and external review not performed.'}
    (out / 'REPLAY.json').write_text(json.dumps(record, indent=2, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    print('H0 FOLLOWUP PUBLICATION REPLAY PASS', flush=True)


if __name__ == '__main__':
    main()
