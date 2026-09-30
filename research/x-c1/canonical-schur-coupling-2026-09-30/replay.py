"""Verify preserved packages and replay their small certificate checks."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import io
import json
import os
import subprocess
import sys
import time
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PIN = '8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def manifest(raw, fetch, names):
    listed = set()
    for line in raw.decode('utf-8').splitlines():
        expected, name = line.split('  ', 1)
        path = PurePosixPath(name)
        require(not path.is_absolute() and '..' not in path.parts and '\\' not in name,
                'Unsafe manifest path: ' + name)
        require(name not in listed and name in names, 'Missing or duplicate manifest entry: ' + name)
        require(digest(fetch(name)) == expected, 'Hash mismatch: ' + name)
        listed.add(name)
    return listed


def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', '-c', 'safe.directory=' + cwd.as_posix(),
                                    '-c', 'core.longpaths=true', *args], cwd=cwd)


def verify():
    bindings = read(HERE / 'SOURCE_BINDINGS.json')
    require(bindings['source_commit'] == bindings['publication_base'] == PIN, 'Unexpected source commit')
    files = {p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()}
    listed = manifest((HERE / 'SHA256SUMS').read_bytes(), lambda n: (HERE / n).read_bytes(), files)
    require(listed | {'SHA256SUMS'} == files, 'Unbound family files')
    count = len(listed)
    originals = {entry['path']: entry['sha256'] for entry in bindings['original_files']}
    for path, h in originals.items():
        require(digest((HERE / path).read_bytes()) == h, 'Original changed: ' + path)
    for pkg in bindings['packages']:
        folder = HERE / pkg['folder']
        names = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()}
        package_files = manifest((folder / 'SHA256SUMS').read_bytes(), lambda n: (folder / n).read_bytes(), names)
        count += len(package_files)
        require(package_files | {'SHA256SUMS', 'PROOF.md', 'META.yaml'} == names, 'Unbound package file')
        require((folder / 'PROOF.md').read_bytes() == (folder / pkg['original_proof']).read_bytes(), 'Proof differs from original')
        raw = (HERE / pkg['archive']).read_bytes()
        require(digest(raw) == pkg['archive_sha256'], 'Archive changed')
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            members = [n for n in archive.namelist() if not n.endswith('/')]
            require(len(members) == len(set(members)), 'Duplicate archive member')
            manifests = [n for n in members if n == 'SHA256SUMS' or n.endswith('/SHA256SUMS')]
            require(len(manifests) == 1, 'Expected one archive manifest')
            prefix = manifests[0][:-len('SHA256SUMS')]
            require(set(members) == {prefix + n for n in package_files | {'SHA256SUMS'}}, 'Archive members differ')
            for name in package_files | {'SHA256SUMS'}:
                require(archive.read(prefix + name) == (folder / name).read_bytes(), 'Archive differs: ' + name)
            count += len(manifest(archive.read(prefix + 'SHA256SUMS'), lambda n: archive.read(prefix + n), package_files))
    for entry in bindings['repository_inputs']:
        path, h = entry['path'], entry['sha256']
        for revision in (PIN, 'HEAD'):
            require(digest(git('show', revision + ':' + path)) == h, 'Git source changed: ' + path)
        require(digest((ROOT / path).read_bytes()) == h, 'Working source changed: ' + path)
    return {'manifest_entries': count, 'original_files': len(originals),
            'archives': len(bindings['packages']), 'repository_inputs': len(bindings['repository_inputs'])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    checks = verify()
    print('PASS preserved inputs ' + json.dumps(checks), flush=True)
    if args.verify_only:
        return
    require(args.output is not None, 'Missing --output')
    out = args.output.resolve()
    require(not out.exists() and not out.is_relative_to(ROOT), 'Use a new output directory outside the repository')
    out.mkdir(parents=True)
    source = out / 'pinned-source'
    # Originals require HEAD at their proof commit. A private clone satisfies
    # that invariant without rewriting any original checker or current branch.
    git('-c', 'core.autocrlf=false', 'clone', '--quiet', '--shared', '--no-checkout', str(ROOT), str(source))
    git('-c', 'core.autocrlf=false', 'checkout', '--quiet', '--detach', PIN, cwd=source)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1')
    # Trust only this private clone in child processes. No global Git changes.
    index = int(env.get('GIT_CONFIG_COUNT', '0'))
    env.update({'GIT_CONFIG_COUNT': str(index + 2), 'GIT_CONFIG_KEY_' + str(index): 'safe.directory',
                'GIT_CONFIG_VALUE_' + str(index): source.as_posix(),
                'GIT_CONFIG_KEY_' + str(index + 1): 'core.longpaths',
                'GIT_CONFIG_VALUE_' + str(index + 1): 'true'})
    steps, receipts = [], []

    def run(label, script, *arguments, expected=None):
        print('RUN ' + label, flush=True)
        start = time.monotonic()
        with (out / (label + '.log')).open('w', encoding='utf-8') as log:
            completed = subprocess.run([sys.executable, '-B', str(script), *map(str, arguments)],
                                       stdout=log, stderr=subprocess.STDOUT, env=env)
        require(completed.returncode == 0, label + ' failed; inspect ' + str(out / (label + '.log')))
        if expected is not None:
            result = out / (label + '.json')
            require(read(result) == read(expected), label + ': receipt content changed')
            require(result.read_bytes().replace(b'\r\n', b'\n') == expected.read_bytes().replace(b'\r\n', b'\n'),
                    label + ': receipt differs beyond platform line endings')
            receipts.append({'name': label, 'path': result.name, 'sha256': digest(result.read_bytes()),
                             'matches_original_except_line_endings': True})
        steps.append({'name': label, 'returncode': 0, 'seconds': time.monotonic() - start})
        print('PASS ' + label, flush=True)

    p1, p2, p3, p4 = [HERE / p['folder'] for p in read(HERE / 'SOURCE_BINDINGS.json')['packages']]
    run('relative-kappa', p1 / 'verify_relative_kappa.py', '--repo', source,
        '--out', out / 'relative-kappa.json', expected=p1 / 'verification.json')
    run('resolvent-moments', p2 / 'verify_resolvent_moments.py', '--repo', source,
        '--primary', p2 / 'primary.json', '--crosscheck', p2 / 'crosscheck.json',
        '--out', out / 'resolvent-moments.json', expected=p2 / 'verification.json')
    run('interval-guards', p2 / 'check_interval_guards.py')
    run('schur-mechanism', p3 / 'verify_mechanism.py', '--repo', source,
        '--out', out / 'schur-mechanism.json', expected=p3 / 'verification.json')
    run('extremal-gate', p4 / 'verify_extremal_gate.py', '--out', out / 'extremal-gate.json',
        expected=p4 / 'verification.json')
    require(not read(out / 'extremal-gate.json')['true_maximizer_isolated'], 'Unexpected isolation claim')
    require(not git('status', '--porcelain', cwd=source).strip(), 'Pinned source changed')
    require(verify() == checks, 'Inputs changed during replay')
    receipt = {'status': 'PASS', 'integration_commit': git('rev-parse', 'HEAD').decode().strip(),
               'source_commit': PIN, 'input_checks': checks, 'steps': steps, 'receipts': receipts,
               'large_resolvent_solves_rerun': False, 'true_maximizer_isolated': False}
    (out / 'REPLAY.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8', newline='\n')
    print('ALL FOUR CANONICAL CERTIFICATE REPLAYS PASS', flush=True)


if __name__ == '__main__':
    main()
