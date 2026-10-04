"""Exact final 2x2 certificates and independent polynomial identity controls.

Standard library only. This checks the rational conclusion of the supplied
directed energy calculation, not every analytic assumption of its inputs.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path


def rational_bound(matrix, sign):
    n = len(matrix)
    assert n == 2 and all(len(row) == n for row in matrix)
    mid = [[F(0) for _ in range(n)] for _ in range(n)]
    rad = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            lo, hi = map(F, matrix[i][j])
            assert lo <= hi and matrix[i][j] == matrix[j][i]
            mid[i][j] = (lo + hi) / 2
            rad[i][j] = (hi - lo) / 2
    for i in range(n):
        mid[i][i] += sign * sum(rad[i])
    return mid


def minors(a):
    assert a[0][1] == a[1][0]
    return a[0][0], a[1][1], a[0][0]*a[1][1]-a[0][1]**2


def add(a, b):
    return [(a[i] if i < len(a) else F(0)) +
            (b[i] if i < len(b) else F(0)) for i in range(max(len(a), len(b)))]


def scaled(a, c):
    return [c*x for x in a]


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def primitive_controls():
    # Unnormalized Legendre polynomials, built directly over the rationals.
    leg = [[F(1)], [F(0), F(1)]]
    for n in range(2, 28):
        leg.append(scaled(add(scaled([F(0)]+leg[-1], 2*n-1),
                              scaled(leg[-2], -(n-1))), F(1, n)))
    controls = []
    for n in range(10, 19):
        for k in [1, 3, 5, 7]:
            expansion = {n: F(1)}
            for _ in range(k+1):
                nxt = {}
                for degree, value in expansion.items():
                    assert degree >= 1
                    nxt[degree+1] = nxt.get(degree+1, F(0)) + value/(2*degree+1)
                    nxt[degree-1] = nxt.get(degree-1, F(0)) - value/(2*degree+1)
                expansion = nxt
            recurrence = []
            for degree, value in expansion.items():
                recurrence = add(recurrence, scaled(leg[degree], 2*factorial(k)*value))
            direct = [F(0)]*(n+k+2)
            # Integrate y^j |x-y|^k on [-1,x] and [x,1], after y=x+t.
            for j, coefficient in enumerate(leg[n]):
                for m in range(j+1):
                    for ell in range(k+m+2):
                        direct[j-m+ell] += (coefficient * comb(j,m) *
                            F(comb(k+m+1,ell), k+m+1) *
                            ((-1)**m + (-1)**ell))
            assert trim(recurrence) == trim(direct), (n,k)
            controls.append({'legendre_degree': n, 'odd_kernel_power': k,
                             'exact_polynomial_identity': True})
    return controls


def serial(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: serial(v) for k,v in x.items()}
    if isinstance(x, list) or isinstance(x, tuple):
        return [serial(v) for v in x]
    return x


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gate', type=Path, required=True)
    ap.add_argument('--mixed', type=Path, required=True)
    ap.add_argument('--second-mixed', type=Path)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    assert __debug__ and not args.out.exists()
    raw = args.gate.read_bytes()
    gate = json.loads(raw)
    mixed_raw = args.mixed.read_bytes()
    mixed = json.loads(mixed_raw)
    assert gate['status'] == 'COMPLETED_DIRECTED_GATE'
    assert gate['uses_target_positivity'] is False
    assert gate['full_old_low_high_coupling_retained'] is True
    assert gate['full_quotient_coverage_proved'] is False
    assert gate['github_changed'] is False
    assert mixed['high_mode_truncation_of_log_or_shift'] is False
    assert gate['bindings']['mixed']['sha256'] == hashlib.sha256(mixed_raw).hexdigest()
    assert [b['parity'] for b in gate['blocks']] == ['even', 'odd']
    checks = []
    for block, floor in zip(gate['blocks'], [F(1,100000), F(33,1000000)]):
        assert block['old_schur_positive_pivots'] == 191
        trial = next(t for t in block['mixed_trials'] if t['young_parameter'] == '1/10000000')
        klo = rational_bound(block['K_loewner_lower'], -1)
        wup = rational_bound(trial['fixed_proposal_residual_inverse_energy_upper'], +1)
        lower = [[klo[i][j]-wup[i][j] for j in range(2)] for i in range(2)]
        surplus = [[lower[i][j] - (floor if i==j else 0) for j in range(2)] for i in range(2)]
        principal = minors(surplus)
        assert all(v > 0 for v in principal)
        assert all(v > 0 for v in minors(wup))
        margin = minors(lower)[2] / (lower[0][0]+lower[1][1])
        assert margin > floor
        checks.append({'parity': block['parity'], 'coefficient_norm_floor': floor,
                       'K_rational_lower': klo, 'W_rational_upper': wup,
                       'schur_rational_lower': lower, 'surplus_principal_minors': principal,
                       'surplus_strictly_positive': True,
                       'det_over_trace_lower': margin})
    assert sum(b['low_pairing_checks'] for b in mixed['blocks']) == 764
    assert sum(b['independent_complete_contractions_checked'] for b in mixed['blocks']) == 8
    precision = None
    if args.second_mixed:
        raw2 = args.second_mixed.read_bytes()
        second = json.loads(raw2)
        assert second['bits'] > mixed['bits']
        assert mixed['bindings'] == second['bindings']
        assert mixed['blocks'] == second['blocks']
        precision = {'bits': [mixed['bits'], second['bits']],
                     'all_serialized_numerical_blocks_identical': True,
                     'second_file_sha256': hashlib.sha256(raw2).hexdigest()}
    controls = primitive_controls()
    result = {'status': 'PASS', 'arithmetic': 'exact rational; Python standard library',
              'gate_sha256': hashlib.sha256(raw).hexdigest(),
              'mixed_sha256': hashlib.sha256(mixed_raw).hexdigest(),
              'blocks': checks, 'precision_comparison': precision,
              'exact_gamma_primitive_controls': controls,
              'scope': 'Final rational energy certificates and 36 polynomial controls; inherited analytic bounds remain source-bound, external review open.',
              'full_new_quotient_covered': False, 'object_x_constructed': False,
              'github_changed': False}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(serial(result), indent=2)+'\n', encoding='utf-8', newline='\n')
    print('PASS: exact even floor 1/100000; odd floor 33/1000000; 36 Gamma controls.')


if __name__ == '__main__':
    main()
