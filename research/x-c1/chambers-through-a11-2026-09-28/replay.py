"""Reproduce the unchanged O10 -> A9 -> general wall -> A11 chain."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def canonical(value, omitted=()):
    if isinstance(value, dict):
        return {k: canonical(v, omitted) for k, v in value.items() if k not in omitted}
    if isinstance(value, list):
        return [canonical(v, omitted) for v in value]
    return value


def same(actual, expected, omitted=()):
    require(canonical(read(actual), omitted) == canonical(read(expected), omitted),
            'Reproduction differs: ' + str(actual))


def matrix_same(actual, expected):
    require(json.loads(gzip.decompress(actual.read_bytes())) ==
            json.loads(gzip.decompress(expected.read_bytes())),
            'Recomputed interval matrix differs: ' + str(actual))


def verify_inputs():
    count = 0
    manifests = [HERE / 'SHA256SUMS'] + [HERE / p / 'SHA256SUMS' for p in ('o10', 'a9', 'wall', 'a11')]
    for manifest in manifests:
        for line in manifest.read_text(encoding='ascii').splitlines():
            expected, name = line.split('  ', 1)
            path = (manifest.parent / name).resolve()
            require(path.is_relative_to(manifest.parent) and path.is_file(), 'Unsafe manifest path: ' + name)
            require(sha(path) == expected, 'Manifest mismatch: ' + str(path))
            count += 1
    bindings = read(HERE / 'SOURCE_BINDINGS.json')
    for row in bindings['original_files']:
        require(sha(HERE / row['path']) == row['sha256'], 'Original source changed: ' + row['path'])
    for row in bindings['repository_inputs']:
        for commit in (row['commit'], 'HEAD'):
            content = subprocess.check_output(['git', 'show', commit + ':' + row['path']], cwd=ROOT)
            require(hashlib.sha256(content).hexdigest() == row['sha256'], 'Repository input changed: ' + row['path'])
    require(sha(HERE / 'high-tail/PROOF.md') == sha(HERE / 'a11/GENERAL_TAIL_PRINCIPLE.md') ==
            bindings['high_tail_copy_sha256'], 'General high-tail source changed')
    # Only the new publication navigation is asserted here. Preserved historical
    # inputs retain their old link context as explained in the publication README.
    for page in [HERE / 'README.md', HERE / 'high-tail/README.md']:
        for target in re.findall(r'\]\(([^\s)]+)\)', page.read_text(encoding='utf-8')):
            if '://' not in target and not target.startswith('#'):
                require((page.parent / unquote(target.split('#')[0])).exists(), 'Broken publication link: ' + target)
    return {'manifest_entries': count, 'original_files': len(bindings['original_files']),
            'repository_input_bindings': len(bindings['repository_inputs'])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    verification = verify_inputs()
    print('PASS input verification: ' + json.dumps(verification), flush=True)
    if args.verify_only:
        return
    require(args.output is not None, '--output is required for certificate replay')
    output = args.output.resolve()
    require(not output.exists(), 'Output must be a new directory')
    require(not output.is_relative_to(ROOT), 'Replay output must be outside the repository')
    output.mkdir(parents=True)
    copy = output / 'package'
    shutil.copytree(HERE, copy, ignore=shutil.ignore_patterns('__pycache__'))
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1')
    steps = []

    def run(name, script, *arguments):
        print('RUN ' + name, flush=True)
        p = subprocess.run([sys.executable, str(copy / script), *map(str, arguments)],
                           capture_output=True, text=True, encoding='utf-8', env=env)
        (output / (name + '.log')).write_text(p.stdout + p.stderr, encoding='utf-8', newline='\n')
        require(p.returncode == 0, name + ' failed; see its log')
        steps.append({'name': name, 'returncode': p.returncode})
        print('PASS ' + name, flush=True)

    def algebra(name, folder, script, expected_count):
        fresh = output / (name + '.json')
        run(name, folder + '/' + script, '--repository', ROOT, '--output', fresh)
        same(fresh, HERE / folder / 'CHECK_RESULTS.json')
        require(read(fresh)['checks_passed'] == expected_count, name + ' count mismatch')

    def common(folder):
        fresh = output / (folder + '-common.json')
        run(folder + '-common', folder + '/common_reserve.py', '--output', fresh)
        same(fresh, HERE / folder / 'common_reserve.json')

    def integer(folder, degree, count):
        fresh = output / (folder + '-integer.json')
        run(folder + '-integer', folder + '/verify_integer_' + folder + '.py', '--output', fresh)
        same(fresh, HERE / folder / 'integer_results.json', ('seconds',))
        result = read(fresh)
        require(result['both_parities_certified'] is True and result['checks_passed'] == count,
                folder + ' independent certification failed')
        require(all(row['positive_directed_pivots'] == degree for row in result['parities'].values()),
                folder + ' independent pivot count mismatch')

    def normalization(folder, count):
        fresh = output / (folder + '-normalization.json')
        run(folder + '-normalization', folder + '/check_normalization_' + folder + '.py',
            '--model', copy / folder / 'normalization_model.json.gz', '--output', fresh)
        same(fresh, HERE / folder / 'normalization_results.json')
        require(read(fresh)['status'] == 'PASS' and read(fresh)['check_count'] == count,
                folder + ' normalization mismatch')

    algebra('o10', 'o10', 'verify_o10.py', 68)
    algebra('a9-tail', 'a9', 'check_tail.py', 72)
    arb9 = output / 'a9-arb.json'
    run('a9-arb', 'a9/check_a9.py', '--output', arb9)
    same(arb9, HERE / 'a9/reserve_results.json', ('check_seconds',))
    matrix_same(output / 'a9-arb_lower_matrices.json.gz', HERE / 'a9/reserve_results_lower_matrices.json.gz')
    require(read(arb9)['both_parities_strictly_certified'] is True and
            all(row['positive_directed_pivots'] == 296 for row in read(arb9)['parities'].values()),
            'A9 Arb positivity failed')
    common('a9')
    integer('a9', 296, 37)
    normalization('a9', 239)
    algebra('general-wall-q9', 'wall', 'verify_wall.py', 109)
    algebra('a11-tail', 'a11', 'check_tail.py', 187)

    # The direct attempt is a preserved inconclusive diagnostic. Reproduce its
    # complete receipt, but never treat it as a positive certificate.
    raw11 = output / 'a11-direct-diagnostic.json'
    run('a11-direct-diagnostic', 'a11/check_a11.py', '--output', raw11)
    same(raw11, HERE / 'a11/reserve_results.json', ('check_seconds',))
    matrix_same(output / 'a11-direct-diagnostic_lower_matrices.json.gz',
                HERE / 'a11/reserve_results_lower_matrices.json.gz')
    require(read(raw11)['both_parities_strictly_certified'] is False,
            'A11 direct diagnostic changed; inspect rather than silently reclassify')

    run('a11-congruence', 'a11/certify_preconditioned.py')
    fresh11 = copy / 'a11/preconditioned_results.json'
    same(fresh11, HERE / 'a11/preconditioned_results.json', ('check_seconds',))
    matrix_same(copy / 'a11/preconditioned_matrices.json.gz', HERE / 'a11/preconditioned_matrices.json.gz')
    require(read(fresh11)['both_parities_strictly_certified'] is True and
            all(row['positive_directed_pivots'] == 285 for row in read(fresh11)['parities'].values()),
            'A11 congruence certification failed')
    # Store every fresh receipt before restoring proven-identical canonical
    # bytes needed by the downstream SHA bindings. Only timings may differ.
    shutil.copyfile(fresh11, output / 'a11-congruence.json')
    shutil.copyfile(copy / 'a11/preconditioned_matrices.json.gz', output / 'a11-congruence-matrices.json.gz')
    for name in ('preconditioned_results.json', 'preconditioned_matrices.json.gz'):
        shutil.copyfile(HERE / 'a11' / name, copy / 'a11' / name)
    common('a11')
    integer('a11', 285, 47)
    normalization('a11', 245)

    require(verify_inputs() == verification, 'Published inputs changed during replay')
    result = {'status': 'PASS', 'source_commit': subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'python': platform.python_version(), 'manifest_sha256': sha(HERE / 'SHA256SUMS'),
        'input_verification': verification, 'steps': steps, 'step_count': len(steps),
        'a9_pivots_each_parity': 296, 'a11_pivots_each_parity': 285,
        'a9_physical_floor': '1e-35', 'a11_physical_floor': '1e-50',
        'full_integral_models_recomputed': False, 'external_analytic_review': 'OPEN'}
    (output / 'result.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
