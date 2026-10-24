"""Publication binding and bounded replay of the unchanged reviewed revision."""
import sys
if sys.flags.optimize:
    sys.stderr.write('OBJEKT_X_PUBLICATION_OPTIMIZED_PYTHON_REJECTED\n')
    raise SystemExit(78)
sys.dont_write_bytecode = True

from pathlib import Path, PurePosixPath
import argparse
import hashlib
import io
import json
import os
import stat
import subprocess
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
REVISION = '8d364fd430d68ce6ec9da29d33fb23aac3d480e489515e1aaa959ae8f93c02f8'
ORIGINAL = 'e1911ce244aa51062f6b06bb767f945922199112380022b59846de4ec7f0e89d'
L1_HEAD = '898711c85fc188b38d7fb1129800d7f5a282ad4c'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'Duplicate JSON key: ' + key)
        result[key] = value
    return result


def parse(raw):
    return json.loads(raw, object_pairs_hook=unique)


def safe(name):
    p = PurePosixPath(name)
    need(bool(name) and not p.is_absolute() and p.as_posix() == name
         and '..' not in p.parts and '\\' not in name and ':' not in name,
         'Unsafe path: ' + name)
    return p


def manifest(root):
    expected = parse((root / 'MANIFEST.json').read_bytes())
    actual = {}
    for p in root.rglob('*'):
        need(not p.is_symlink(), 'Package symlink')
        if p.is_file():
            actual[p.relative_to(root).as_posix()] = p
    need(set(actual) == set(expected) | {'MANIFEST.json'}, 'Package inventory')
    for name, digest in expected.items():
        safe(name)
        need(sha(actual[name].read_bytes()) == digest, 'Package hash: ' + name)
    return len(expected)


def archive_bytes(root, entry):
    safe(entry['path'])
    path = root / entry['path']
    if path.exists():
        raw = path.read_bytes()
    else:
        spec = parse((root / 'ARCHIVE_CHUNKS.json').read_bytes())[entry['path']]
        need(spec['sha256'] == entry['sha256'] and spec['bytes'] == entry['bytes'],
             'Chunk archive identity')
        pieces = []
        for part in spec['chunks']:
            safe(part['path'])
            data = (root / part['path']).read_bytes()
            need(len(data) == part['bytes'] and sha(data) == part['sha256'],
                 'Chunk hash: ' + part['path'])
            pieces.append(data)
        raw = b''.join(pieces)
    need(len(raw) == entry['bytes'] and sha(raw) == entry['sha256'], 'Archive identity')
    return raw


def members(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        names = z.namelist()
        need(len(names) == len(set(names)), 'Duplicate ZIP member')
        for info in z.infolist():
            safe(info.filename)
            need(not info.is_dir() and not stat.S_ISLNK(info.external_attr >> 16),
                 'Unexpected ZIP member type')
        return {name: z.read(name) for name in names}


def bound_members(raw, manifest_name):
    data = members(raw)
    inventory = parse(data[manifest_name])
    need(set(data) == set(inventory) | {manifest_name}, 'ZIP inventory')
    for name, digest in inventory.items():
        need(sha(data[name]) == digest, 'ZIP binding: ' + name)
    return data


def l1_dependency(root, repo):
    dep = parse((root / 'L1_REFERENCE.json').read_bytes())
    need(dep['publication_head'] == L1_HEAD, 'L1 head changed')
    safe(dep['repository_package'])
    path = repo / dep['repository_package'] / 'MANIFEST.json'
    need(sha(path.read_bytes()) == dep['publication_manifest_sha256'], 'L1 manifest mismatch')
    pinned = subprocess.check_output(['git', '-C', str(repo), 'show',
                                     L1_HEAD + ':' + dep['repository_package'] + '/MANIFEST.json'])
    need(pinned == path.read_bytes(), 'L1 pinned bytes differ')
    subprocess.run(['git', '-C', str(repo), 'merge-base', '--is-ancestor', L1_HEAD, 'HEAD'], check=True)
    need((repo / dep['repository_package'] / 'author-text/L1-BEWEIS.txt').read_bytes()
         == (root / 'premises/L1-BEWEIS.txt').read_bytes(), 'Frozen H1-H4 differs')
    return dep['publication_head']


def verify(root=HERE, repo=None, replay=False):
    root = Path(root).resolve()
    repo = Path(repo).resolve() if repo else root.parents[2]
    count = manifest(root)
    head = l1_dependency(root, repo)
    info = parse((root / 'ARCHIVES.json').read_bytes())
    archives = {e['sha256']: archive_bytes(root, e) for e in info['archives']}
    need(REVISION in archives and len(archives[REVISION]) == 11442481, 'Wrong protected revision')
    revision = bound_members(archives[REVISION], 'FULL-MANIFEST.json')
    original_info = info['historical_original_nested_in_revision']
    original = revision[original_info['member']]
    need(len(original) == 11129155 and sha(original) == ORIGINAL, 'Original archive changed')
    views = {digest: members(raw) for digest, raw in archives.items()}
    views[ORIGINAL] = bound_members(original, 'MANIFEST.json')
    for row in parse((root / 'READABLE_COPIES.json').read_bytes()):
        safe(row['path'])
        raw = (root / row['path']).read_bytes()
        need(sha(raw) == row['sha256'] and raw == views[row['archive_sha256']][row['member']],
             'Readable copy differs: ' + row['path'])
    state = parse((root / 'STATUS.json').read_bytes())
    need(state['review_status'] == 'EXTERNAL_REVIEW_OPEN' and state['point4_closed'] is False
         and state['full_degree11_closed'] is False and state['odd_parity_closed'] is False,
         'Claim boundary changed')
    result = {'status': 'PASS_BOUNDED_TWO_SPACE_PUBLICATION', 'L1_head': head,
              'package_bindings': count, 'revision_archive_sha256': REVISION,
              'original_archive_sha256': ORIGINAL, 'replay_performed': replay,
              'fresh_integrated_panels': 0, 'fresh_numerical_generators': False,
              'external_review': 'EXTERNAL_REVIEW_OPEN'}
    if replay:
        with tempfile.TemporaryDirectory(prefix='objekt-x-two-space-publication-') as t:
            work = Path(t)
            for name, raw in revision.items():
                dest = work / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(raw)
            base = work / 'zweiraum-protection-v1'
            archive = work / original_info['member']
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1', PYTHONOPTIMIZE='0')
            run = subprocess.run([sys.executable, '-B', str(base / 'test_revision.py'),
                                  '--archive', str(archive), '--out', str(work / 'fresh-test.json')],
                                 env=env, capture_output=True, text=True, timeout=600)
            need(run.returncode == 0, 'Protected suite failed: ' + run.stdout + run.stderr)
            fresh = parse((work / 'fresh-test.json').read_bytes())
            need(fresh['optimization_cases'] == 258 and fresh['guarded_python_files'] == 43
                 and len(fresh['normal_replays']) == 11 and len(fresh['normal_failure_controls']) == 3
                 and fresh['original_bytes_unchanged'] is True, 'Incomplete protected suite')
            result['technical_suite'] = fresh
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path)
    ap.add_argument('--replay', action='store_true')
    ap.add_argument('--report', type=Path)
    args = ap.parse_args()
    if args.report:
        need(not args.report.exists() and not args.report.resolve().is_relative_to(HERE),
             'Report must be new and outside package')
    result = verify(repo=args.repo, replay=args.replay)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open('x', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'technical_suite'}, indent=2))


if __name__ == '__main__':
    main()
