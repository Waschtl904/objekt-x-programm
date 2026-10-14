"""Independent rational checks; infinite-dimensional arguments are in HERLEITUNG_GPT2.txt.

Standard library only. Original archives and their programs are never modified.
"""
from fractions import Fraction as F
from pathlib import Path, PurePosixPath
from itertools import combinations
from math import factorial
import argparse
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
INPUT_NAME = 'Objekt-X-Tailboden-1-20-durch-Komplementwechsel-2026-10-14.zip'
INPUT_SHA = 'aaa21cb4cbab92f10c128b7709b011ca51b68cb0b53f2738b2eb64597701d818'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def member(archive, suffix):
    names = [n for n in archive.namelist() if n == suffix or n.endswith('/' + suffix)]
    assert len(names) == 1, (suffix, names)
    return archive.read(names[0])


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in transpose(b)] for row in a]


def sub(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def inv(a):
    n = len(a)
    m = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if m[k][j])
        m[j], m[k] = m[k], m[j]
        d = m[j][j]
        m[j] = [v/d for v in m[j]]
        for i in range(n):
            if i != j:
                d = m[i][j]
                m[i] = [x-d*y for x, y in zip(m[i], m[j])]
    return [row[n:] for row in m]


def det(a):
    if len(a) == 1:
        return a[0][0]
    return sum(((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]])
                for j in range(len(a))), F(0))


def block(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def diagonal(values):
    return [[F(x if i == j else 0) for j in range(len(values))]
            for i, x in enumerate(values)]


def inverse_compression_control():
    # Five-dimensional independent test: two eliminated and three retained
    # coordinates, nonidentity metric, nonorthogonal basis within K, full coupling.
    w = diagonal([2, 3, 5, 7, 11])
    u = [[1, 1, 2, 0, 1], [0, 1, -1, 1, 2], [0, 0, 1, 2, 0],
         [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]
    t = mm(mm(transpose(u), diagonal([1, 2, 3, 4, 5])), u)
    j = [[2, 1], [0, 3], [0, 0], [0, 0], [0, 0]]
    assert mm(mm(transpose(j), w), j) == [[8, 4], [4, 29]]
    assert mm(w, t) != mm(t, w)
    k, z = range(2), range(2, 5)
    tzz, wz = block(t, z, z), block(w, z, z)
    schur = sub(tzz, mm(mm(block(t, z, k), inv(block(t, k, k))), block(t, k, z)))
    compressed_inverse = block(inv(t), z, z)
    assert compressed_inverse == inv(schur)
    assert compressed_inverse != inv(tzz)
    # These are quadratic-form matrices for inverse operators in the W metric.
    restriction_inverse_energy = mm(mm(wz, inv(tzz)), wz)
    compressed_inverse_energy = mm(mm(wz, compressed_inverse), wz)
    gap = sub(compressed_inverse_energy, restriction_inverse_energy)
    minors = [det(block(gap, c, c)) for n in range(1, 4)
              for c in combinations(range(3), n)]
    assert all(x >= 0 for x in minors) and any(x > 0 for x in minors)
    assert restriction_inverse_energy != inv(tzz)  # catches loss of the metric
    return {'dimension': 5, 'eliminated_dimension': 2,
            'noncommuting_metric_and_form': True,
            'inverse_compression_equals_inverse_Schur': True,
            'inverse_restriction_strictly_smaller_in_some_directions': True,
            'gap_principal_minors': [str(x) for x in minors],
            'finite_control_is_not_an_infinite_dimensional_proof': True}


def independent_math(inverse_archive):
    domain = json.loads(member(inverse_archive, 'sources/DOMAIN_BOUND_INPUTS.json'))
    beta = F(20209999981781, 182190000000000)
    moment = F(3, 100)*(4*F(3, 200)**96/F(factorial(96)))**2
    d96 = F(11, 10) + sum((F(1, n) for n in range(1, 97)), F(0))
    assert moment < F(1, 10**600) and d96 > F(31, 5)
    cases = []
    for parity, c in [('even', F(1, 250)), ('odd', F(71, 10000))]:
        source = next(x for x in domain['cases'] if x['parity'] == parity)
        rec = json.loads(member(inverse_archive, f'INVERSE_{parity.upper()}.json'))
        assert F(source['beta']) == F(rec['beta']) == beta
        assert F(source['whole_residual_simple_cap']) == F(rec['residual_cap']) == c
        a = (1-c)*beta
        floor = F(21, 5)*a
        assert floor > F(231, 500) > F(1, 20)
        assert a*d96/(1+3000*moment) > F(671, 1000) > F(2, 3)
        assert F(3, 2) < 20
        cases.append({'parity': parity, 'a=(1-c)beta': str(a),
                      'weighted_inverse_coefficient_1_over_a': str(1/a),
                      'generic_floor': str(floor), 'generic_floor_gt_231_over_500': True,
                      'geometric_floor_gt_671_over_1000': True,
                      'conditional_transferred_floor': '2/3',
                      'conditional_restriction_inverse_norm_upper': '3/2'})
    return {'cases': cases, 'moment_mass_lt_1e_minus_600': True,
            'inverse_compression_control': inverse_compression_control()}


def response_basis_chain(schur_path, supplied, bindings):
    raw = schur_path.read_bytes()
    assert sha(raw) == bindings['original_schur_package']['sha256']
    with zipfile.ZipFile(io.BytesIO(raw)) as sz:
        refs = json.loads(member(sz, 'INPUT_BINDINGS.json'))
        archives = {}
        for key in ['responses', 'common']:
            data = member(sz, refs[key]['filename'])
            assert sha(data) == refs[key]['sha256']
            archives[key] = zipfile.ZipFile(io.BytesIO(data))
        result = []
        try:
            for parity in ['EVEN', 'ODD']:
                response = json.loads(member(archives['responses'], f'RESPONSES_{parity}.json'))
                for name, expected in response['bindings'].items():
                    assert sha(member(archives['common'], name)) == expected, name
                direct_name = f'DIRECT_REST_{parity}_3072.json'
                direct = json.loads(member(archives['common'], direct_name))
                basis = member(supplied, f'sources/BASIS_{parity}.json')
                assert direct['bindings']['basis'] == sha(basis)
                assert direct['bindings']['half'] == json.loads(basis)['bindings']['half']
                result.append({'parity': parity.lower(), 'basis_sha256': sha(basis),
                               'response_to_Common96_all_bindings_verified': len(response['bindings']),
                               'Common96_direct_to_original_basis_verified': True})
        finally:
            for archive in archives.values():
                archive.close()
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--schur-package', type=Path)
    ap.add_argument('--basis-package', type=Path)
    ap.add_argument('--full-source-replay', action='store_true')
    ap.add_argument('--output', type=Path, default=HERE/'REPLAY.json')
    args = ap.parse_args()
    if args.full_source_replay:
        assert args.schur_package and args.basis_package, 'Full replay needs both original archives.'
    if (HERE/'MANIFEST.json').exists():
        for name, entry in json.loads((HERE/'MANIFEST.json').read_text(encoding='utf-8'))['files'].items():
            path = (HERE/name).resolve()
            assert path.is_relative_to(HERE)
            data = path.read_bytes()
            assert sha(data) == entry['sha256'] and len(data) == entry['bytes'], name
    source = HERE/'inputs'/INPUT_NAME
    assert sha(source.read_bytes()) == INPUT_SHA
    full_receipt = json.loads((HERE/'reports/FULL_SOURCE_REPLAY.json').read_text(encoding='utf-8'))
    with zipfile.ZipFile(source) as supplied:
        assert full_receipt == json.loads(member(supplied, 'reports/ACCEPTANCE.json'))
        assert full_receipt['fresh_inverse_replay']['new_complete_positive_LDL_pivots'] == 574
        assert sum(x['exact_basis_null_relations'] for x in full_receipt['cases']) == 1344
        bindings = json.loads(member(supplied, 'SOURCE_BINDINGS.json'))
        inverse_bytes = member(supplied, 'Objekt-X-A9-Inverserneuerung-und-Hoher-Schurrest-2026-10-13.zip')
        with zipfile.ZipFile(io.BytesIO(inverse_bytes)) as iz:
            math = independent_math(iz)
        chain = response_basis_chain(args.schur_package, supplied, bindings) if args.schur_package else None
        with tempfile.TemporaryDirectory(prefix='objekt-x-tail-review-') as tmp:
            for info in supplied.infolist():
                p = PurePosixPath(info.filename)
                assert not p.is_absolute() and '..' not in p.parts
                assert ':' not in info.filename and '\\' not in info.filename
                assert (info.external_attr >> 16) & 0o170000 != 0o120000
            supplied.extractall(tmp)
            root = Path(tmp)/INPUT_NAME[:-4]
            outpath = Path(tmp)/'source-replay.json'
            command = [sys.executable, '-B', '-X', 'utf8', str(root/'check.py'), '--output', str(outpath)]
            if args.full_source_replay:
                command += ['--replay-inverse']
            for option, path in [('--schur-package', args.schur_package), ('--basis-package', args.basis_package)]:
                if path:
                    command += [option, str(path.resolve())]
            run = subprocess.run(command, cwd=root, text=True, encoding='utf-8', capture_output=True)
            assert run.returncode == 0, run.stdout + run.stderr
            current = json.loads(outpath.read_text(encoding='utf-8'))
            for key, value in full_receipt.items():
                if key == 'fresh_inverse_replay' and not args.full_source_replay:
                    assert current[key] is None
                elif key == 'original_Schur_data_binding' and not args.schur_package:
                    assert current[key] is None
                elif key == 'original_basis_archive_byte_comparison' and not args.basis_package:
                    assert current[key] is False
                else:
                    assert current[key] == value, key
    result = {'status': 'PASS_CONDITIONAL_TAIL_COUNTERCHECK',
              'input_sha256': INPUT_SHA, 'mathematical_checks': math,
              'original_full_receipt_equals_all_supplied_acceptance_fields': True,
              'current_original_checker': current,
              'current_response_to_original_basis_chain': chain,
              'analytic_proof': 'HERLEITUNG_GPT2.txt',
              'large_integrations_rerun': False, 'external_mathematical_review_open': True,
              'github_modified_in_this_review': False}
    if (HERE/'reports/INDEPENDENT_AUDIT.json').exists():
        old = json.loads((HERE/'reports/INDEPENDENT_AUDIT.json').read_text(encoding='utf-8'))
        assert math == old['mathematical_checks']
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'independent_parities': 2,
                      'source_replay': 'full' if args.full_source_replay else 'fast',
                      'source_chain_checked_now': chain is not None,
                      'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
