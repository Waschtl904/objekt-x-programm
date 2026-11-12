"""Verify publication bytes and stated boundaries, not physical mathematics."""
from pathlib import Path, PurePosixPath
from fractions import Fraction as F
import argparse, hashlib, json, subprocess, sys, tempfile, zipfile

ROOT = Path(__file__).resolve().parent
ARCHIVES = {
    'gpt2-run-2026-11-05': '501ed63430ad88dae24006791ea1eaf55936d387061600dd9c1927395e79b90e',
    'gpt1-start-review-2026-11-05': 'cec71cb0f581bc3326230106f3209e74bbc69fa34cfd1f09814bb54a2e9be5bd',
    'gpt1-bridge-2026-11-09': 'bb969c4a364d8c44d1d5ac4d931636e1ca74c4da1fa4a93d198c8a7806424c90',
    'budget-review-2026-11-10': '19769a8e1e66aa6fa80116022f813c3dde1965e5c54b18d374580ef7fb5bb056',
    'gpt1-first-column-2026-11-11': '36a20575ba76a32c744f826b7603468b9de1b5ec5ddd6331f57adc8a3b3cfe54',
    'gpt2-first-column-2026-11-11': 'd8c0edc6c92f38d78e72d814165c29426bb7e6f8417d5978d9a61822182c1641',
    'gpt2-second-column-2026-11-11': '34b6dfb12bc759b7971c5bed296914e1b72a407879e6e57d210fadf208a5610c',
    'gpt2-data-map-2026-11-10': '49dbdfb08418a66fa7d3815a2f26cd96f4694bf3ef131fe97630ecb3d8337e8c',
}

def need(ok, message):
    if not ok:
        raise ValueError(message)

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for data in iter(lambda: f.read(1024 * 1024), b''):
            h.update(data)
    return h.hexdigest()

def safe(path):
    p = PurePosixPath(path)
    need(not p.is_absolute() and '\\' not in path and ':' not in path
         and all(part not in ('', '.', '..') for part in path.split('/')), 'Unsafe path')
    return path

def identity(path, record):
    need(path.is_file() and not path.is_symlink(), 'Missing regular file: ' + str(path))
    need(path.stat().st_size == record['bytes'] and digest(path) == record['sha256'],
         'Byte identity failed: ' + str(path))

def validate_scope(s):
    need(s['kernel_run']['result'] == 'EINSCHLIESSUNG_UNENTSCHIEDEN', 'Kernel result promotion')
    need(s['kernel_run']['start_review_original_available'] is True
         and s['kernel_run']['result_review_original_available'] is False, 'Start/result review conflated')
    need(s['bridge']['full_physical_remainder_proved'] is False, 'Bridge overclaimed')
    need(s['first_column']['status'] == 'PROJECT_INTERNAL_TARGETED_ACCEPTANCE'
         and s['first_column']['independent_exact_matches'] == 14, 'First-column scope changed')
    need(s['first_column']['original_python_flint_checker_executed_by_GPT2'] is False,
         'Unperformed author replay claimed')
    need(F(s['first_column']['whole_energy_strict_upper']) == F('0.000003522682288001101'),
         'First-column bound changed')
    need(s['second_column']['status'] == 'CONDITIONAL_SCALAR_SUFFICIENCY_ONLY'
         and s['second_column']['Qq_bound_achieved'] is False
         and s['second_column']['Qq_reachability_proved'] is False, 'Second-column promotion')
    need(s['second_column']['native_X12_contract_conditional'] is True
         and s['budget']['native_X12_ancestry_unresolved'] is True
         and s['native_bindings']['resolved'] is False, 'Native ancestry silently closed')
    o = s['overall']
    need(o['status'] == 'RESTMACHBARKEIT_OFFEN' and o['external_review'] == 'OPEN'
         and o['object_x'] == 'NOT_CONSTRUCTED', 'Overall promotion')
    need(all(o[k] is False for k in ('two_space_closed', 'point4_closed',
         'new_physical_main_run_justified', 'historical_A11_positivity_used_as_input')),
         'Unjustified closure, computation or circular input')

def verify(root=ROOT, asset_dir=None, replay=True):
    need(not sys.flags.optimize, 'Optimized Python is not an accepted verification mode')
    root = Path(root)
    manifest = json.loads((root / 'MANIFEST.json').read_bytes())['files']
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    need(actual == set(manifest) | {'MANIFEST.json'}, 'Manifest does not cover exact file set')
    for name, record in manifest.items():
        identity(root / safe(name), record)
    index = json.loads((root / 'SOURCE_INDEX.json').read_bytes())
    archives = {a['id']: a for a in index['archives']}
    need(set(archives) == set(ARCHIVES), 'Source archive set changed')
    need(len(index['readable_originals']) == 34, 'Readable original set changed')
    available = {}
    for key, a in archives.items():
        need(a['sha256'] == ARCHIVES[key], 'Original source hash changed')
        if a['target_kind'] == 'GITHUB_RELEASE_ASSET':
            need(key == 'gpt2-run-2026-11-05', 'Unexpected release asset')
            if asset_dir is None:
                continue
            path = Path(asset_dir) / safe(a['filename'])
        else:
            need(a['target_kind'] == 'GIT_FILE', 'Unknown publication target')
            path = root / safe(a['target'])
        identity(path, a)
        available[key] = path
    for copy in index['readable_originals']:
        path = root / safe(copy['target'])
        identity(path, copy)
        if copy['archive_id'] in available:
            with zipfile.ZipFile(available[copy['archive_id']]) as z:
                need(z.read(safe(copy['member'])) == path.read_bytes(), 'Original member altered')
    need(index['missing_originals'][0]['reported_sha256'] ==
         '52fd67cdaf5586b421fc32230b6f03f445e51705d492cba9b91ec788cedd59e7', 'Missing original hidden')
    validate_scope(json.loads((root / 'SCOPE.json').read_bytes()))
    if replay:
        archive = available['gpt2-second-column-2026-11-11']
        prefix = archives['gpt2-second-column-2026-11-11']['original_root']
        with tempfile.TemporaryDirectory(prefix='objx-november-') as temporary:
            target = Path(temporary)
            with zipfile.ZipFile(archive) as z:
                for item in z.infolist():
                    safe(item.filename)
                z.extractall(target)
            package = target / prefix
            result = target / 'SECOND_REPLAY.json'
            p = subprocess.run([sys.executable, '-B', '-X', 'utf8',
                str(package / 'check_second_scalar.py'), '--abnahme', str(package / 'inputs'),
                '--output', str(result)], capture_output=True, text=True, encoding='utf-8')
            need(p.returncode == 0, 'Bounded scalar replay failed: ' + p.stderr)
            need(json.loads(result.read_bytes()) == json.loads((package / 'SECOND_SCALAR_RESULT.json').read_bytes()),
                 'Bounded scalar result changed')
    return {'status': 'INTEGRATION_BINDINGS_PASS', 'git_archives_verified': 7,
            'release_asset_bytes_verified': asset_dir is not None, 'readable_originals': 34,
            'scalar_replay': replay, 'first_column_replayed': False,
            'new_q_evaluations': 0, 'new_integrations': 0,
            'native_original_bindings_resolved': False, 'second_energy_proved': False}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--asset-dir', type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(asset_dir=args.asset_dir), indent=2))
