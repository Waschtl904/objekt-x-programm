"""Exact REAL symmetric conditional gates. Does not verify operator enclosures."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json


class Inconclusive(Exception):
    pass


def q(x):
    if isinstance(x, bool) or not isinstance(x, (int, str, F)):
        raise ValueError('Rational input must be an integer or fraction string; floats are forbidden')
    return F(x)


def mat(rows):
    if not isinstance(rows, list) or not rows or not isinstance(rows[0], list) or not rows[0]:
        raise ValueError('Nonempty matrix required')
    n = len(rows[0])
    if any(not isinstance(row, list) or len(row) != n for row in rows):
        raise ValueError('Ragged matrix')
    return [[q(x) for x in row] for row in rows]


def tr(a):
    return [list(row) for row in zip(*a)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def scale(a, c):
    return [[c*x for x in row] for row in a]


def add(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError('Shape mismatch')
    return [[x+y for x, y in zip(row, other)] for row, other in zip(a, b)]


def sub(a, b):
    return add(a, scale(b, F(-1)))


def mul(a, b):
    if len(a[0]) != len(b):
        raise ValueError('Product shape mismatch')
    return [[sum(x*y for x, y in zip(row, col)) for col in tr(b)] for row in a]


def gram(a, metric=None):
    return mul(tr(a), a if metric is None else mul(metric, a))


def inverse(a):
    n = len(a)
    if len(a[0]) != n:
        raise ValueError('Inverse requires a square matrix')
    x = [row[:] + eye(n)[i] for i, row in enumerate(a)]
    for j in range(n):
        candidates = [i for i in range(j, n) if x[i][j]]
        if not candidates:
            raise ValueError('Singular matrix')
        p = candidates[0]
        x[j], x[p] = x[p], x[j]
        pivot = x[j][j]
        x[j] = [v/pivot for v in x[j]]
        for i in range(n):
            if i != j:
                c = x[i][j]
                x[i] = [v-c*w for v, w in zip(x[i], x[j])]
    return [row[n:] for row in x]


def positive(a, strict=False):
    """Exact Schur pivots, including correct handling of zero PSD pivots."""
    n = len(a)
    if len(a[0]) != n or a != tr(a):
        raise ValueError('Real symmetric square matrix required')
    s = [row[:] for row in a]
    for k in range(n):
        pivot = s[k][k]
        if pivot < 0 or (strict and pivot == 0):
            return False
        if pivot == 0:
            if any(s[k][j] != 0 for j in range(k+1, n)):
                return False
            continue
        for i in range(k+1, n):
            for j in range(i, n):
                value = s[i][j]-s[i][k]*s[k][j]/pivot
                s[i][j] = s[j][i] = value
    return True


def need(condition, message):
    if not condition:
        raise Inconclusive(message)


def certify(data):
    if data.get('schema') != 'objekt-x-coverage/1':
        raise ValueError('Unsupported schema')
    alpha = q(data['alpha'])
    if alpha != F(1, 10):
        raise ValueError('This protocol is bound to alpha=1/10')
    epsilon = q(data['leakage_budget'])
    need(0 <= epsilon <= F(1, 20), 'LEAKAGE_BUDGET_EXCEEDS_PROTOCOL')
    wm, wp = mat(data['basis_gram_lower']), mat(data['basis_gram_upper'])
    need(positive(wm, strict=True), 'BASIS_GRAM_NOT_CERTIFIED')
    need(positive(sub(wp, wm)), 'BASIS_GRAM_BOUNDS_INCONSISTENT')
    ue = mat(data['leakage_gram_upper'])
    need(positive(ue), 'LEAKAGE_UPPER_NOT_PSD')
    need(positive(sub(scale(eye(len(ue)), epsilon), ue)), 'COVERAGE_BOUND_INCONCLUSIVE')
    delta = alpha-epsilon
    out = {
        'status': 'PASS_CONDITIONAL_COVERAGE',
        'basis_dimension': len(wm), 'functional_rows': len(ue),
        'alpha': str(alpha), 'leakage_budget': str(epsilon),
        'conditional_tail_floor': str(delta),
        'assumptions': 'True full operator enclosures and domain/membership claims must be proved separately.',
        'operator_input_verified': False, 'full_remainder_certified': False,
        'synthetic_input': data.get('kind') == 'SYNTHETIC_ONLY',
    }
    if 'schur' not in data:
        return out
    s = data['schur']
    kl, gr = mat(s['K_lower']), mat(s['residual_gram_upper'])
    need(positive(gr), 'RESIDUAL_GRAM_UPPER_NOT_PSD')
    eta = q(s['eta'])
    need(eta > 0, 'POSITIVE_ETA_REQUIRED')
    lower = sub(kl, scale(gr, 1/delta))
    need(positive(sub(lower, scale(wp, eta))), 'FINITE_SCHUR_INCONCLUSIVE')
    out.update(status='PASS_CONDITIONAL_SCHUR', eta=str(eta), residual_charge_factor=str(1/delta))
    if 'normalization' in s:
        n = s['normalization']
        yu = mat(n['response_gram_upper'])
        y, r = q(n['response_norm_bound']), q(n['residual_norm_bound'])
        need(y >= 0 and r >= 0, 'NEGATIVE_NORM_BOUND')
        need(positive(yu), 'RESPONSE_GRAM_UPPER_NOT_PSD')
        need(positive(sub(scale(wm, y*y), yu)), 'RESPONSE_NORM_NOT_CERTIFIED')
        need(positive(sub(scale(wm, r*r), gr)), 'RESIDUAL_NORM_NOT_CERTIFIED')
        shear = y+r/delta
        beta = min(eta, delta)/(1+shear)**2
        out.update(conditional_R12_floor=str(beta), shear_bound=str(shear),
                   physical_A9_floor_asserted=False)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    args = parser.parse_args()
    try:
        result = certify(json.loads(args.certificate.read_bytes()))
    except Inconclusive as exc:
        print(json.dumps({'status': 'INCONCLUSIVE', 'failed_gate': str(exc),
                          'actual_operator_counterexample': False}, indent=2))
        raise SystemExit(2)
    except (ValueError, KeyError, TypeError, ZeroDivisionError) as exc:
        print(json.dumps({'status': 'INVALID_CERTIFICATE_INPUT', 'detail': str(exc)}, indent=2))
        raise SystemExit(1)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
