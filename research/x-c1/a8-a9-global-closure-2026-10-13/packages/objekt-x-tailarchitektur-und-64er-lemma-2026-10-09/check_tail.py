"""Exact scalar arithmetic and synthetic algebra checks; no operator integration."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def matrix(rows):
    return [[F(x) for x in row] for row in rows]


def adj(a):
    return list(map(list, zip(*a)))


def mul(a, b):
    require(len(a[0]) == len(b), 'Matrix shape mismatch')
    return [[sum(x*y for x, y in zip(row, col)) for col in adj(b)] for row in a]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(row, other)] for row, other in zip(a, b)]


def inv(a):
    n = len(a)
    x = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        p = next(i for i in range(j, n) if x[i][j])
        x[j], x[p] = x[p], x[j]
        pivot = x[j][j]
        x[j] = [v/pivot for v in x[j]]
        for i in range(n):
            if i != j:
                factor = x[i][j]
                x[i] = [v-factor*w for v, w in zip(x[i], x[j])]
    return [row[n:] for row in x]


def gram(a, metric):
    return mul(adj(a), mul(metric, a))


def positive(a):
    a = [row[:] for row in a]
    require(a == adj(a), 'Nonsymmetric test matrix')
    for j in range(len(a)):
        if a[j][j] <= 0:
            return False
        for i in range(j+1, len(a)):
            for k in range(j+1, len(a)):
                a[i][k] -= a[i][j]*a[j][k]/a[j][j]
    return True


def block(a, b, d):
    return [x+y for x, y in zip(a, b)] + [x+y for x, y in zip(adj(b), d)]


def synthetic_case(negative_tail):
    # Entirely synthetic rational data, independent of the research certificates.
    a = matrix([[3, 1], [1, 2]])
    gf = matrix([[1, 2], [0, 1]])
    gt = matrix([[2, -1], [1, 3]])
    sf = matrix([[2, 1], [1, 3]])
    c = matrix([[1, -2], [2, 1]])
    wanted = matrix([[-1 if negative_tail else 1, F(1, 3)], [F(1, 3), 2]])
    p = matrix([[F(1, 3), F(-1, 2)], [F(2, 5), F(1, 4)]])
    ai, si = inv(a), inv(sf)
    t = add(wanted, gram(c, si))
    dff = add(sf, gram(gf, ai))
    dft = add(c, mul(adj(gf), mul(ai, gt)))
    dtt = add(t, gram(gt, ai))
    old_plus_finite = block(a, gf, dff)
    require(positive(old_plus_finite), 'Synthetic old-plus-finite block is not positive')
    one_step = add(dtt, gram(gt+dft, inv(old_plus_finite)), -1)
    require(one_step == wanted, 'One-step elimination failed')
    sequential = add(t, gram(c, si), -1)
    require(sequential == wanted, 'Sequential elimination failed')
    residual = add(c, mul(sf, p), -1)
    k = add(add(add(t, mul(adj(c), p), -1), mul(adj(p), c), -1), gram(p, sf))
    require(add(k, gram(residual, si), -1) == wanted, 'Residual identity failed')
    gcorrected = add(gt, mul(gf, p), -1)
    dcorrected = add(add(add(dtt, mul(adj(dft), p), -1), mul(adj(p), dft), -1), gram(p, dff))
    require(add(dcorrected, gram(gcorrected, ai), -1) == k, 'Correlated force identity failed')
    mixed = add(t, gram(dft, si), -1)  # Delete only the old cross-energy: forbidden mixing.
    require(mixed != wanted, 'Negative control did not detect deleted cross-energy')
    require(positive(wanted) == (not negative_tail), 'Tail-sign control failed')
    return {'negative_actual_tail': negative_tail, 'old_and_finite_positive': True,
            'one_step_equals_sequential': True, 'residual_identity_exact': True,
            'common_corrected_old_force_exact': True,
            'deleted_cross_energy_detected': True, 'synthetic_only': True}


def calculate():
    delta = F(91, 50)
    high_lift_square = 1+F(1, 10**12)
    loss = F(16, 5)**2 * high_lift_square / delta
    require(loss == F(512, 91)*high_lift_square, 'Loss simplification failed')
    harmonic = F(0)
    margins = []
    for n in range(65):
        if n:
            harmonic += F(1, n)
        margins.append(harmonic+1-loss)
    require(margins[64] > F(1175, 10000) > F(1, 10), 'N=64 tail inequality failed')
    require(margins[63] > F(1, 10) >= margins[62], 'Within-majorant threshold check failed')
    old_margin = harmonic+1-F(16, 5)**2*high_lift_square/F(2, 3)
    require(old_margin < 0, 'Old-floor negative control failed')
    leak_safe_margin = harmonic+1-F(1001, 1000)*loss-F(1, 1000)
    require(leak_safe_margin > F(1, 10), 'Leakage-aware high constant failed')
    return {
        'status': 'PASS_EXACT_SCALAR_AND_SYNTHETIC_ALGEBRA',
        'conditional_analytic_claim': 'tau >= W_X/10 on Z_64 as defined in HERLEITUNG.txt',
        'delta_old_high': str(delta), 'N': 64,
        'harmonic_H64_exact': str(harmonic), 'loss_exact': str(loss),
        'margin_N64_exact': str(margins[64]), 'certified_floor': '1/10',
        'margin_N64_gt_1175_over_10000': True,
        'first_N_passing_one_tenth_with_this_scalar_majorant': 63,
        'old_floor_N64_margin_exact': str(old_margin),
        'leakage_aware_high_margin_exact': str(leak_safe_margin),
        'leakage_aware_high_margin_gt_one_tenth': True,
        'codimension_full_shell_upper': 276,
        'codimension_R12_upper': 264,
        'codimension_is_actual_computed_rank': False,
        'synthetic_checks': [synthetic_case(False), synthetic_case(True)],
        'operator_domains_machine_proved': False,
        'actual_functional_kernels_numerically_constructed': False,
        'new_operator_integrations': False,
        'full_remainder_certified': False,
        'object_X_constructed': False,
        'review_status': 'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-checks', action='store_true', help='Authoring only: write the deterministic scalar receipt')
    args = parser.parse_args()
    result = calculate()
    checks = ROOT/'CHECKS.json'
    if args.write_checks:
        checks.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
        print('Wrote exact scalar receipt; no operator integrals computed.')
        return
    require(result == json.loads(checks.read_bytes()), 'Stored scalar receipt mismatch')
    manifest = json.loads((ROOT/'MANIFEST.json').read_bytes())
    expected = manifest['files']
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
              if p.is_file() and p.name != 'MANIFEST.json' and '__pycache__' not in p.parts}
    require(set(expected) == actual, 'Manifest member coverage mismatch')
    for name, digest in expected.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, 'Binding mismatch: '+name)
    print(json.dumps({'status': 'PASS_BOUND_PACKAGE', 'files': len(expected),
                      'arithmetic_and_synthetic_checks': result,
                      'manifest_is_external_authentication': False}, indent=2))


if __name__ == '__main__':
    main()
