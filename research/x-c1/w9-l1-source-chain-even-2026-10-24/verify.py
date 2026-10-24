"""Bind the unchanged L1 author archive and optionally replay its finite checker.

Standard library only. No quadrature, source regeneration or network access.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import io
import json
import stat
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
ARCHIVE = 'author/Objekt-X-L1-Anwendungskette-2026-10-24.zip'
ARCHIVE_SHA = '6a4a713e931f5db5d43931ed730caaa97ac6fbe83fd646a89e4cac2115cb4d8b'
ARCHIVE_SIZE = 47074898


def need(test, message):
    if not test:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def unique(items):
    result = {}
    for key, value in items:
        need(key not in result, 'Duplicate JSON key: ' + key)
        result[key] = value
    return result


def parse(raw):
    return json.loads(raw, object_pairs_hook=unique)


def safe_name(name):
    p = PurePosixPath(name)
    need(bool(name) and not p.is_absolute() and p.as_posix() == name
         and '..' not in p.parts and '\\' not in name and ':' not in name,
         'Unsafe path: ' + name)
    return p


def check_package(root):
    root = Path(root)
    manifest = parse((root / 'MANIFEST.json').read_bytes())
    files = {}
    for path in root.rglob('*'):
        need(not path.is_symlink(), 'Symlink in package')
        if path.is_file():
            files[path.relative_to(root).as_posix()] = path
    need(set(files) - {'MANIFEST.json'} == set(manifest), 'Package inventory mismatch')
    for name, expected in manifest.items():
        safe_name(name)
        need(digest(files[name].read_bytes()) == expected, 'Package hash mismatch: ' + name)
    return len(manifest)


def archive_bytes(path, expected_sha=ARCHIVE_SHA, expected_size=ARCHIVE_SIZE):
    path = Path(path)
    if path.exists():
        raw = path.read_bytes()
    else:
        root = path.parent.parent
        spec = parse((root / 'AUTHOR_ARCHIVE_CHUNKS.json').read_bytes())
        need(spec['original_path'] == ARCHIVE and spec['bytes'] == expected_size
             and spec['sha256'] == expected_sha, 'Chunk archive identity mismatch')
        pieces = []
        for entry in spec['chunks']:
            safe_name(entry['path'])
            piece = (root / entry['path']).read_bytes()
            need(len(piece) == entry['bytes'] and digest(piece) == entry['sha256'],
                 'Archive chunk mismatch: ' + entry['path'])
            pieces.append(piece)
        raw = b''.join(pieces)
    need(len(raw) == expected_size, 'Original archive size mismatch')
    need(digest(raw) == expected_sha, 'Original archive SHA-256 mismatch')
    return raw


def read_archive(path, expected_sha=ARCHIVE_SHA, expected_size=ARCHIVE_SIZE):
    raw = archive_bytes(path, expected_sha, expected_size)
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        names = z.namelist()
        need(len(set(names)) == len(names), 'Duplicate archive member')
        for info in z.infolist():
            safe_name(info.filename)
            need(not info.is_dir() and not stat.S_ISLNK(info.external_attr >> 16),
                 'Unexpected archive directory or symlink')
        members = {name: z.read(name) for name in names}
    manifest = parse(members['MANIFEST.json'])
    need(set(members) - {'MANIFEST.json'} == set(manifest), 'Author inventory mismatch')
    for name, expected in manifest.items():
        need(digest(members[name]) == expected, 'Author hash mismatch: ' + name)
    return members


def check_copies(root, members):
    copies = list((root / 'author-text').iterdir())
    need(bool(copies), 'Missing readable author copies')
    for path in copies:
        need(path.is_file() and path.name in members, 'Unknown author copy')
        need(path.read_bytes() == members[path.name], 'Author copy differs: ' + path.name)
    need(parse((root / 'evidence/FRESH-RESULT.json').read_bytes()) == parse(members['RESULT.json']),
         'Recorded fresh result differs')


def compare_result(actual, expected):
    need(actual == expected, 'Finite replay result differs from original')


def output_path(report, root):
    p = Path(report).resolve()
    need(not p.is_relative_to(Path(root).resolve()), 'Report must be outside the package')
    need(not p.exists(), 'Refusing to overwrite an existing report')
    return p


def verify(root=ROOT, replay=False):
    need(sys.flags.optimize == 0, 'Optimized Python is not a supported audit mode')
    root = Path(root).resolve()
    count = check_package(root)
    members = read_archive(root / ARCHIVE)
    check_copies(root, members)
    bindings = parse(members['SOURCE_BINDINGS.json'])
    need(len(bindings['files']) == 30, 'Expected 30 author inputs')
    for alias, entry in bindings['files'].items():
        safe_name(entry['path'])
        need(digest(members[entry['path']]) == entry['sha256'], 'Input hash mismatch: ' + alias)
    status = parse((root / 'STATUS.json').read_bytes())
    need(status['L1_application'] == 'CLOSED_LOCALLY_UNDER_H1_H4'
         and status['external_review'] == 'EXTERNAL_REVIEW_OPEN'
         and status['second_direction_certified'] is False, 'Unexpected claim promotion')
    replay_result = None
    if replay:
        with tempfile.TemporaryDirectory(prefix='objekt-x-l1-replay-') as temp:
            work = Path(temp)
            for name, raw in members.items():
                path = work / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
            report = work / 'NEW-REPLAY.json'
            run = subprocess.run([sys.executable, '-B', str(work / 'verify_chain.py'),
                                  '--bindings', str(work / 'SOURCE_BINDINGS.json'),
                                  '--output', str(report)], cwd=work, text=True,
                                 capture_output=True, timeout=600)
            need(run.returncode == 0, 'Author finite replay failed: ' + run.stdout + run.stderr)
            replay_result = parse(report.read_bytes())
            compare_result(replay_result, parse(members['RESULT.json']))
    return {'status': 'PASS_BOUNDED_L1_PACKAGE_CHECKS',
            'author_archive_sha256': ARCHIVE_SHA, 'author_archive_bytes': ARCHIVE_SIZE,
            'package_manifest_entries': count, 'author_manifest_entries': len(members)-1,
            'bound_author_inputs': len(bindings['files']),
            'finite_replay_performed': replay,
            'all_result_fields_identical': True if replay else None,
            'finite_result': replay_result,
            'historical_analytic_lemmas_reproved': False,
            'new_quadrature': False, 'second_direction_certified': False,
            'external_review': 'EXTERNAL_REVIEW_OPEN'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    target = output_path(args.report, ROOT) if args.report else None
    result = verify(replay=args.replay)
    if target:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('x', encoding='utf-8', newline='\n') as handle:
            json.dump(result, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'finite_result'}, indent=2))


if __name__ == '__main__':
    main()
