#!/usr/bin/env python3
"""Check publication bytes only. No mathematical replay or network writes."""
import sys
if sys.flags.optimize or not __debug__:
    raise SystemExit('OPTIMIZED_PYTHON_REJECTED: no publication was checked')
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import subprocess
import zipfile

HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
V1_COMMIT = '20a4c6392fa17f6b1dc5527ae223b32415244190'

def need(value, message):
    if not value:
        raise ValueError(message)

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def path_ok(name):
    need(isinstance(name, str) and name and '\\' not in name and ':' not in name,
         'Invalid relative path')
    p = PurePosixPath(name)
    need(not p.is_absolute() and all(x not in ('', '.', '..') for x in name.split('/')),
         'Unsafe path: ' + name)
    return p

def read_local(name):
    p = PACKAGE
    for part in path_ok(name).parts:
        p = p / part
        need(not p.is_symlink(), 'Symlink: ' + name)
    need(p.is_file(), 'Missing regular file: ' + name)
    return p.read_bytes()

def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args])

def check_zip(path, expected):
    need(path.is_file() and path.stat().st_size == expected['bytes'], 'Archive size')
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(2**20), b''):
            h.update(block)
    need(h.hexdigest() == expected['sha256'], 'Archive SHA-256: ' + path.name)
    z = zipfile.ZipFile(path)
    need(len(z.namelist()) == len(set(z.namelist())), 'Duplicate ZIP members')
    return z

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('v1', 'v2', 'gpt1'):
        ap.add_argument('--' + name, type=Path)
    ap.add_argument('--git-ref')
    args = ap.parse_args()
    manifest = json.loads((HERE / 'PUBLICATION_MANIFEST.json').read_bytes())
    archives = json.loads((HERE / 'ARCHIVES.json').read_bytes())['archives']
    rows = manifest['files']
    need(len(rows) == len({r['path'] for r in rows}), 'Duplicate publication paths')
    need(manifest['v1_publication_commit'] == V1_COMMIT, 'V1 anchor changed')
    for row in rows:
        raw = read_local(row['path'])
        need(len(raw) == row['bytes'] and digest(raw) == row['sha256'],
             'Publication byte mismatch: ' + row['path'])
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        need(blob == row['git_blob'], 'Git blob identity: ' + row['path'])
    root = Path(git(PACKAGE, 'rev-parse', '--show-toplevel').decode().strip())
    prefix = PACKAGE.relative_to(root).as_posix() + '/'
    old = git(root, 'ls-tree', '-r', '--name-only', V1_COMMIT, '--', prefix).decode().splitlines()
    need(len(old) == 48, 'Unexpected v1 publication scope')
    for name in old:
        need(read_local(name[len(prefix):]) == git(root, 'show', V1_COMMIT + ':' + name),
             'V1 publication changed: ' + name)
    if args.git_ref:
        for name in old + [prefix + r['path'] for r in rows] + [prefix + 'revision-v2/PUBLICATION_MANIFEST.json']:
            need(read_local(name[len(prefix):]) == git(root, 'show', args.git_ref + ':' + name),
                 'Exact Git ref mismatch: ' + name)
    checked_archives = []
    archive_copies = 0
    opened = {}
    try:
        for key in ('v1', 'v2', 'gpt1'):
            path = getattr(args, key)
            if path is not None:
                opened[key] = check_zip(path, archives[key])
                checked_archives.append(key)
        for row in rows:
            src = row.get('source')
            if not src or src['archive'] not in opened:
                continue
            z = opened[src['archive']]
            nested = []
            try:
                for member in src['nested_members']:
                    path_ok(member)
                    z = zipfile.ZipFile(io.BytesIO(z.read(member)))
                    nested.append(z)
                path_ok(src['member'])
                need(z.read(src['member']) == read_local(row['path']),
                     'Original copy changed: ' + row['path'])
                archive_copies += 1
            finally:
                for nz in nested:
                    nz.close()
        if 'v1' in opened:
            reading = json.loads(read_local('READING_MANIFEST.json'))
            for row in reading['files']:
                if row.get('archive_member'):
                    need(opened['v1'].read(row['archive_member']) == read_local(row['path']),
                         'V1 reading copy mismatch: ' + row['path'])
    finally:
        for z in opened.values():
            z.close()
    print(json.dumps({'status': 'PUBLICATION_BYTES_PASS', 'publication_files': len(rows),
        'unchanged_v1_files': len(old), 'archives_checked': checked_archives,
        'new_original_copies_checked_against_archives': archive_copies,
        'git_ref': args.git_ref, 'mathematical_replay': False,
        'external_author_v2_receipt_checked': False}, indent=2))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError, zipfile.BadZipFile) as e:
        print('PUBLICATION_REJECTED: ' + str(e), file=sys.stderr)
        raise SystemExit(1)
