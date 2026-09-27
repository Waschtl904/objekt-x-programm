"""Replay the bound O8/O9 certificates in a fresh output directory."""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def canonical(value, omitted=()):
    if isinstance(value, dict):
        return {k: canonical(v, omitted) for k, v in value.items() if k not in omitted}
    if isinstance(value, list):
        return [canonical(v, omitted) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    require(not output.exists(), 'Output must be a new directory')
    require(not output.is_relative_to(HERE), 'Output must be outside the bound package')
    output.mkdir(parents=True)
    for line in (HERE / 'SHA256SUMS').read_text(encoding='ascii').splitlines():
        expected, name = line.split('  ', 1)
        path = (HERE / name).resolve()
        require(path.is_relative_to(HERE) and path.is_file(), 'Invalid manifest path: ' + name)
        require(sha(path) == expected, 'Manifest mismatch: ' + name)
    bindings = read(HERE / 'SOURCE_BINDINGS.json')
    for ref in bindings['repository_inputs']:
        raw = subprocess.run(['git', 'show', ref['commit'] + ':' + ref['path']],
                             cwd=ROOT, capture_output=True, check=True).stdout
        require(hashlib.sha256(raw).hexdigest() == ref['sha256'], 'Pinned input mismatch: ' + ref['path'])
        require(sha(ROOT / ref['path']) == ref['sha256'], 'Current input changed: ' + ref['path'])
    for page in HERE.rglob('*.md'):
        for link in re.findall(r'\]\(([^\s)]+)\)', page.read_text(encoding='utf-8')):
            if '://' not in link and not link.startswith('#'):
                require((page.parent / unquote(link.split('#')[0])).exists(), 'Broken link: ' + str(page.relative_to(HERE)) + ' -> ' + link)
    copy = output / 'package'
    shutil.copytree(HERE, copy, ignore=shutil.ignore_patterns('__pycache__'))
    steps = []

    def run(name, script, *arguments):
        print('RUN ' + name, flush=True)
        p = subprocess.run([sys.executable, str(copy / script), *map(str, arguments)],
                           capture_output=True, text=True, encoding='utf-8')
        (output / (name + '.log')).write_text(p.stdout + p.stderr, encoding='utf-8', newline='\n')
        require(p.returncode == 0, name + ' failed; see its log')
        steps.append({'name': name, 'returncode': p.returncode})
        print('PASS ' + name, flush=True)

    def same(actual, expected, omitted=()):
        require(canonical(read(actual), omitted) == canonical(read(expected), omitted),
                'Reproduction differs: ' + str(actual.name))

    calc = copy / 'o8-rechenstand'
    run('tail-original', 'o8-vorbereitung/check_constants.py')
    same(copy / 'o8-vorbereitung/constants.json', HERE / 'o8-vorbereitung/constants.json')
    run('tail-refined', 'o8-rechenstand/refine_tail.py')
    same(calc / 'refined_tail.json', HERE / 'o8-rechenstand/refined_tail.json')
    run('arb-certificate', 'o8-rechenstand/check_a8.py', '--high-floor', '2/3', '--output', output / 'arb.json')
    require(read(output / 'arb.json')['both_parities_strictly_certified'] is True, 'Arb positivity failed')
    same(output / 'arb.json', calc / 'reserve_refined.json', ('check_seconds',))
    require(sha(output / 'arb_lower_matrices.json.gz') == sha(calc / 'reserve_refined_lower_matrices.json.gz'), 'Recomputed lower matrices changed')
    run('common-reserve', 'o8-rechenstand/check_common_reserve.py')
    same(calc / 'common_reserve.json', HERE / 'o8-rechenstand/common_reserve.json')
    run('integer-certificate', 'o8-reproduktion/verify_integer_intervals.py', '--package', calc, '--output', output / 'integer.json')
    integer = read(output / 'integer.json')
    require(integer['both_parities_certified'] is True, 'Independent positivity failed')
    require(all(v == sha(calc / k) for k, v in integer['input_hashes'].items()), 'Independent input binding failed')
    same(output / 'integer.json', HERE / 'o8-reproduktion/integer_results.json', ('seconds', 'input_hashes'))
    run('graph-schur', 'o8-schur-abgleich/check_graph_schur.py')
    same(copy / 'o8-schur-abgleich/graph_check_results.json', HERE / 'o8-schur-abgleich/graph_check_results.json', ('elapsed_seconds',))
    require(sha(copy / 'o8-schur-abgleich/graph_lower_matrices.json.gz') == sha(HERE / 'o8-schur-abgleich/graph_lower_matrices.json.gz'), 'Graph matrices changed')
    run('normalization', 'o8-rechenstand/check_normalization_a8.py', '--model', calc / 'normalization_model.json.gz', '--output', output / 'normalization.json')
    same(output / 'normalization.json', calc / 'normalization_results.json')
    run('o9-algebra', 'o9-positive-transporte/check_transport_algebra.py')
    same(copy / 'o9-positive-transporte/transport_checks.json', HERE / 'o9-positive-transporte/transport_checks.json')
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    result = {'status': 'PASS', 'source_commit': commit, 'python': platform.python_version(),
              'manifest_sha256': sha(HERE / 'SHA256SUMS'), 'steps': steps,
              'positive_pivots_each_parity': 191, 'external_review': 'OPEN',
              'full_integral_model_recomputed': False}
    (output / 'result.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
