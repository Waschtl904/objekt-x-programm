"""Exact reduction checks and inherited bounds for the true canonical kappa.

Standard library only. Does not compute new spectral projectors or the true
inverse-energy moments on E, and does not replay the original terminal models.
The analytic proof in RELATIVE_KAPPA.md is part of this conditional result.
"""
from fractions import Fraction as F
from pathlib import Path
from decimal import Decimal, localcontext
import argparse
import hashlib
import json
import shutil
import subprocess

PIN = '8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b'
FAMILY = 'research/x-c1/renewable-low-schur-spectral-2026-09-29/'
OUTER = FAMILY + '07-canonical-extension-outer-mass/'


def mat(a): return [[F(x) for x in row] for row in a]
def eye(n): return mat([[int(i == j) for j in range(n)] for i in range(n)])
def transpose(a): return [list(row) for row in zip(*a)]
def scale(c, a): return [[c*x for x in row] for row in a]
def add(a, b): return [[x+y for x, y in zip(u, v)] for u, v in zip(a, b)]
def sub(a, b): return add(a, scale(-1, b))
def mul(a, b): return [[sum(x*y for x, y in zip(u, v)) for v in transpose(b)] for u in a]
def trace(a): return sum(a[i][i] for i in range(len(a)))


def inverse(a):
    n = len(a)
    rows = [u[:] + v for u, v in zip(a, eye(n))]
    for j in range(n):
        k = next(k for k in range(j, n) if rows[k][j])
        rows[j], rows[k] = rows[k], rows[j]
        rows[j] = [v/rows[j][j] for v in rows[j]]
        for k in range(n):
            if k != j:
                c = rows[k][j]
                rows[k] = [v-c*w for v, w in zip(rows[k], rows[j])]
    return [u[n:] for u in rows]


def nullspace(a):
    rows = [u[:] for u in a]
    n, i, piv = len(rows[0]), 0, []
    for j in range(n):
        ks = [k for k in range(i, len(rows)) if rows[k][j]]
        if not ks:
            continue
        k = ks[0]
        rows[i], rows[k] = rows[k], rows[i]
        rows[i] = [v/rows[i][j] for v in rows[i]]
        for k in range(len(rows)):
            if k != i:
                c = rows[k][j]
                rows[k] = [v-c*w for v, w in zip(rows[k], rows[i])]
        piv.append(j)
        i += 1
        if i == len(rows):
            break
    columns = []
    for j in range(n):
        if j not in piv:
            v = [F(0)]*n
            v[j] = F(1)
            for i, k in enumerate(piv):
                v[k] = -rows[i][j]
            columns.append(v)
    return transpose(columns)


def positive(a):
    assert a == transpose(a)
    a = [u[:] for u in a]
    for k in range(len(a)):
        p = a[k][k]
        assert p > 0
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                a[i][j] -= a[i][k]*a[k][j]/p


def compression(w, a): return mul(mul(transpose(w), a), w)


def formula_checks():
    tests = []
    q = mat([[6, 1, 1, 0, 0, 0], [1, 5, 0, 1, 0, 0],
             [1, 0, 4, 1, 0, 0], [0, 1, 1, 4, 1, 0],
             [0, 0, 0, 1, 5, 1], [0, 0, 0, 0, 1, 6]])
    positive(q)
    qi = inverse(q)
    for shift in (F(1, 2), F(17), F(23)):
        b = add(q, scale(shift, eye(6)))
        for dim in (1, 2):
            e = [row[:dim] for row in mat([[1, 1], [2, 0], [0, 1],
                                          [1, -1], [-1, 2], [1, 0]])]
            n = nullspace(mul(transpose(e), b))
            assert mul(mul(transpose(e), b), n) == scale(0, mul(transpose(e), n))
            l, g, t = compression(e, q), mul(transpose(e), e), compression(e, qi)
            be = add(l, scale(shift, g))
            r = add(add(l, scale(2*shift, g)), scale(shift**2, t))
            assert r == compression(e, mul(mul(b, qi), b))
            s = compression(n, q)
            c = mul(mul(transpose(n), q), e)
            z = sub(l, mul(mul(transpose(c), inverse(s)), c))
            positive(z)
            assert z == mul(mul(be, inverse(r)), be)
            # The reciprocal matrix is similar to a symmetric positive matrix.
            v = mul(mul(mul(r, inverse(be)), l), inverse(be))
            reciprocal = mul(inverse(l), z)
            assert trace(inverse(v)) == trace(reciprocal)
            if dim == 2:
                det = lambda x: x[0][0]*x[1][1]-x[0][1]*x[1][0]
                assert det(inverse(v)) == det(reciprocal)
            # Nonzero coupling eigenvalues agree on old and extension sides.
            old_c = mul(mul(mul(inverse(s), c), inverse(l)), transpose(c))
            new_c = mul(mul(mul(inverse(l), transpose(c)), inverse(s)), c)
            for power in (1, 2, 3):
                op, np = eye(len(old_c)), eye(dim)
                for _ in range(power):
                    op, np = mul(op, old_c), mul(np, new_c)
                assert trace(op) == trace(np)
            # Known exact Gershgorin bounds: I <= Q <= 8 I.
            m, upper = 1/(1+shift), 8/(8+shift)
            constant = (m+upper)**2/(4*m*upper)
            positive(sub(scale(constant, mul(mul(be, inverse(l)), be)), r))
            tests.append({'test': 'nonorthogonal_E_inverse_compression_and_coupling',
                          'dimension': dim, 'shift': str(shift)})
    # Sharp scalar spectral-band example, and the dispersion identity.
    for m, upper in ((F(1, 1000), F(1, 10)), (F(1, 10**50), F(1, 10000))):
        d, h = (m+upper)/2, (1/m+1/upper)/2
        k = 1-1/(d*h)
        assert k == ((upper-m)/(upper+m))**2
        assert d*h-1 == (upper-m)**2/(4*m*upper)
        tests.append({'test': 'sharp_band_and_scalar_dispersion', 'm': str(m)})
    # A small ordinary angle alone need not give a relative energy margin.
    t, eps = F(1, 200), F(1, 10**40)
    s, c = 2*t/(1+t*t), (1-t*t)/(1+t*t)
    assert s*s+c*c == 1 and 0 < s < F(1, 100)
    d, h = eps*s*s+c*c, s*s/eps+c*c
    survival = 1/(d*h)
    assert survival == eps/(eps+(1-eps)**2*s*s*c*c)
    assert F(1, 10**36) < survival < F(1001, 10**39)
    tests.append({'test': 'small_angle_large_relative_coupling',
                  'projector_distance_exact': str(s),
                  'one_minus_kappa_exact': str(survival)})
    return tests


def interval_upper(matrix):
    return max(F(row[i][1])+sum(max(abs(F(x[0])), abs(F(x[1])))
                               for j, x in enumerate(row) if j != i)
               for i, row in enumerate(matrix))


def scientific_lower(x, digits=6):
    with localcontext() as ctx:
        ctx.prec = 160
        approx = Decimal(x.numerator)/Decimal(x.denominator)
        exponent = approx.adjusted()-digits+1
    unit = F(10**exponent) if exponent >= 0 else F(1, 10**(-exponent))
    k = (x/unit).numerator//(x/unit).denominator
    lower = k*unit
    assert 0 < lower <= x < lower+unit
    return f'{k/(10**(digits-1)):.{digits-1}f}e{exponent+digits-1:+d}', str(lower)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    git = shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe'
    def git_bytes(*words):
        return subprocess.check_output([git, *words], cwd=args.repo)
    assert git_bytes('rev-parse', 'HEAD').decode().strip() == PIN
    bindings = {}
    def read(path):
        raw = (args.repo/path).read_bytes()
        assert raw == git_bytes('show', PIN+':'+path), path
        bindings[path] = hashlib.sha256(raw).hexdigest()
        return json.loads(raw) if path.endswith('.json') else raw
    report = read(OUTER+'verification.json')
    primary, cross = read(OUTER+'primary.json'), read(OUTER+'crosscheck.json')
    assert bindings[OUTER+'primary.json'] == report['primary_sha256']
    assert bindings[OUTER+'crosscheck.json'] == report['crosscheck_sha256']
    for path, digest in report['source_sha256'].items():
        read(path)
        assert bindings[path] == digest, path
    for path in (FAMILY+'06-critical-spectral-transport/PROOF.md',
                 FAMILY+'05-canonical-spectral-ranks/verification.json',
                 OUTER+'PROOF.md'):
        read(path)
    results = {}
    for old, new in (('A8', 'A9'), ('A9', 'A11')):
        folder = f'research/x-c1/chambers-through-a11-2026-09-28/{new.lower()}/'
        reserve = read(folder+'common_reserve.json')
        c = F(reserve['common_physical_floor_exact'])
        assert c == (F(1, 10**35) if new == 'A9' else F(1, 10**50))
        m = c/(c+17)
        for parity in ('even', 'odd'):
            key = f'{old}->{new}-{parity}'
            trial = f'{new}-{parity}'
            x, y = primary['trials'][trial]['physical_Ritz_matrix'], cross['trials'][trial]['physical_Ritz_matrix']
            hull = []
            for row_x, row_y in zip(x, y):
                row = []
                for ix, iy in zip(row_x, row_y):
                    a, b, c0, d = map(F, ix+iy)
                    assert max(a, c0) <= min(b, d)
                    row.append([str(min(a, c0)), str(max(b, d))])
                hull.append(row)
            theta = interval_upper(hull)
            assert theta == F(report['trials'][trial]['theta_upper_exact'])
            upper = theta/(theta+17)
            assert 0 < m < upper < F(1, 10000)
            survival = 4*m*upper/(m+upper)**2
            kappa = ((upper-m)/(upper+m))**2
            assert survival+kappa == 1 and 0 < survival < 1
            display, rounded = scientific_lower(survival)
            dim = report['results'][key]['dimension']
            assert dim == (1 if old == 'A8' else 2)
            results[key] = {
                'dimension_E': dim,
                'physical_terminal_floor_exact': str(c),
                'b_spectral_lower_exact': str(m),
                'physical_Ritz_upper_exact': str(theta),
                'b_spectral_upper_exact': str(upper),
                'kappa_lower_exact': '0', 'kappa_upper_exact': str(kappa),
                'one_minus_kappa_lower_exact': str(survival),
                'one_minus_kappa_upper_exact': '1',
                'one_minus_kappa_display_lower': display,
                'display_lower_exact': rounded,
                'uses_existing_new_terminal_positivity': True,
                'true_E_inverse_moment_computed': False}
            print(key, '1-kappa >=', display, '(inherited spectral-band bound)')
    checks = formula_checks()
    output = {
        'status': 'EXACT_CANONICAL_REDUCTION_AND_INHERITED_BOUNDS_PASS',
        'source_commit': PIN, 'source_sha256': bindings,
        'bound_file_count': len(bindings),
        'formula_check_count': len(checks), 'formula_checks': checks,
        'results': results,
        'arithmetic': 'Python standard library Fraction; no binary float in proof arithmetic',
        'terminal_models_replayed': False,
        'canonical_inverse_moments_enclosed': False,
        'sharp_transition_specific_kappa_enclosure': False,
        'forward_renewal_proved': False,
        'scope': 'Conditional on the published analytic results and terminal certificates. '
                 'Finite examples check formulas; the general proof is in RELATIVE_KAPPA.md.'}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(len(bindings), 'commit-bound files;', len(checks), 'exact formula checks; PASS')


if __name__ == '__main__':
    main()
