#!/usr/bin/env python3
"""Exact rational support checks for X-C1 three-cell factorization.

No A1 data, repository imports, large matrix, floating acceptance, or CI.
The companion note proves the infinite-dimensional operator statements.
This script verifies only elementary enclosures and scalar comparison budgets.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial, isqrt
import json
from pathlib import Path

COUNT = 0

def check(condition: bool, label: str) -> None:
    global COUNT
    if not condition:
        raise ArithmeticError('FAIL: ' + label)
    COUNT += 1
    print('PASS: ' + label)


def atan_partial(x: F, terms: int) -> F:
    return sum(((-1)**k * x**(2*k+1) / (2*k+1) for k in range(terms)), F(0))


def log_near_one(x: F, terms: int = 48) -> tuple[F, F]:
    if not F(1) <= x <= F(2):
        raise ValueError('Range reduction required')
    z = (x-1)/(x+1)
    partial = 2*sum((z**(2*k+1)/(2*k+1) for k in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return partial, partial+tail


def log_bounds(x: F) -> tuple[F, F]:
    if x <= 0:
        raise ValueError('logarithm requires positive input')
    if x < 1:
        lo, hi = log_bounds(1/x)
        return -hi, -lo
    n = 0
    while x > 2:
        x /= 2
        n += 1
    lo2, hi2 = log_near_one(F(2))
    lo, hi = log_near_one(x)
    return lo+n*lo2, hi+n*hi2


def exp_lower(x: F, terms: int) -> F:
    return sum((x**k/factorial(k) for k in range(terms)), F(0))


def sqrt_bounds(n: int, denominator: int = 10**14) -> tuple[F, F]:
    k = isqrt(n*denominator*denominator)
    return F(k, denominator), F(k+1, denominator)


def encode(x: F) -> dict[str, str]:
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}


def main() -> None:
    pi_lo = 16*atan_partial(F(1,5), 12)-4*atan_partial(F(1,239), 13)
    pi_hi = 16*atan_partial(F(1,5), 13)-4*atan_partial(F(1,239), 12)
    check(F(157,50) < pi_lo < pi_hi < F(22,7), 'Machin enclosure: 3.14 < pi < 22/7')
    ln2lo, ln2hi = log_bounds(F(2))
    ln3lo, ln3hi = log_bounds(F(3))
    ln32lo, _ = log_bounds(F(3,2))
    ln43lo, _ = log_bounds(F(4,3))
    check(F(2,3) < ln2lo < ln2hi < F(7,10), '2/3 < log 2 < 7/10')
    check(F(1) < ln3lo < ln3hi < F(11,10), '1 < log 3 < 11/10')
    check(ln32lo > F(2,5), 'log(3/2) > 2/5')
    check(ln43lo > F(2,7), 'log(4/3) > 2/7')
    check(exp_lower(F(11,10), 6) > 3, 'independent positive-series check: exp(11/10)>3')
    check(F(7,5)**2 < 2 and F(17,10)**2 < 3, 'rational square-root lower bounds')

    eps, delta = F(1,100), F(1,50)
    check(-F(7,20)-eps > -1 and F(11,10)-F(1,3)+eps < 1,
          'all three fixed cells lie strictly inside (-1,1)')
    check(F(2,5)-delta > delta, 'all three support gaps exceed the small-delay cutoff')
    check(F(2,7) > delta and F(2,5) > delta,
          'log 4/log 3 and log 3/log 2 separation excludes accidental prime channels')
    check(2*delta < F(2,3), 'within-cell and touching two-cell distances have no prime delay')

    # gamma lies strictly between H_20-log21 and H_20-log20.
    H20 = sum((F(1,k) for k in range(1,21)), F(0))
    ln20lo, ln20hi = log_bounds(F(20))
    ln21lo, ln21hi = log_bounds(F(21))
    gam_lo, gam_hi = H20-ln21hi, H20-ln20lo
    check(F(11,20) < gam_lo < gam_hi < F(61,100), 'elementary harmonic/log enclosure for Euler gamma')
    # coth(z)>1/z; atan(tanh z)<z; pi<22/7, z=1/200.
    # c > log(1750/11)-H20-1/100.
    lnratlo, _ = log_bounds(F(1750,11))
    c_lower_expression = lnratlo-H20-F(1,100)
    c0 = F(29,20)
    check(c_lower_expression > c0, 'strengthened analytic floor c_delta > 29/20')
    # coth(z)<1/z+z; 200+1/200 < 64*pi; gamma>11/20.
    check(200+F(1,200) < 64*pi_lo, 'coth(1/200)/(8*pi) < 8')
    check(3*ln2hi-gam_lo < F(31,20), 'analytic ceiling c_delta < 31/20')
    check(F(31,20) < pi_lo/2, 'at delta=1/50: c_delta < pi/2')
    merged_lo, _ = log_bounds(F(875,11))
    check(merged_lo-H20-F(1,50) > F(3,4),
          'after retaining the Gamma interface, merged-cell floor c_(2delta) > 3/4')

    g12 = delta*(1+1/(2*(F(2,3)-delta)))
    g13 = delta*(1+1/(2*(F(1)-delta)))
    g23 = delta*(1+1/(2*(F(2,5)-delta)))
    a,b,g = F(27,50), F(17,25), F(1,20)
    check(g12 == F(86,2425), 'Gamma 1--2 Schur bound')
    check(g13 == F(37,1225), 'Gamma 1--3 Schur bound')
    check(g23 == F(22,475), 'Gamma 2--3 Schur bound')
    check(F(1,2)+g12 < a, '||A|| < 27/50, with complete Gamma kernel')
    check(F(11,17)+g13 < b, '||B|| < 17/25, with complete Gamma kernel')
    check(g23 < g, '||C|| < 1/20, no prime 3/2 channel')
    check(a*a+b*b < F(87,100)**2, 'simultaneous star norm < 87/100')
    check(F(87,100)+g == F(92,100), 'complete block coupling norm < 92/100')
    check(c0-F(92,100) == F(53,100), 'whole bounded residual floor > 53/100')

    d2 = c0-a*a/c0
    eta = g+a*b/c0
    d3 = c0-b*b/c0-eta*eta/d2
    check(d2 == F(18109,14500) and d2 > F(6,5), 'second Schur pivot > 18109/14500 > 6/5')
    check(eta == F(4397,14500), 'induced leaf coupling bound includes B A*/c')
    check(d3 == F(95749,90545) and d3 > F(21,20), 'third Schur pivot > 95749/90545 > 21/20')
    m2 = a*a/c0**2
    m3 = b*b/c0**2+eta*eta/(c0*d2)
    check(m2 < F(7,50), 'Neumann/binomial operator parameter M2 < 7/50')
    check(m3 < F(7,25), 'binomial operator parameter M3 < 7/25')

    # A symbolic 3x3 comparator is not the actual operator: this is only a
    # scalar algebra regression for orientation and no double use of reserve.
    x,y,z = F(3,7), F(-2,5), F(4,9)
    value = c0*(x*x+y*y+z*z)-2*a*x*y-2*b*x*z-2*g*y*z
    squared = c0*(x-a*y/c0-b*z/c0)**2+d2*(y-eta*z/d2)**2+d3*z*z
    check(value == squared, 'correct upper-triangular completion of squares (scalar regression)')
    check(c0*d2*d3 == c0**3-c0*(a*a+b*b+g*g)-2*a*b*g,
          'Schur determinant ledger, including the three-way mixed term')
    check(value != c0*x*x+d2*(y+a*x/c0)**2+d3*(z+b*x/c0+eta*y/d2)**2,
          'the proposed reversed/sign-changed triangular readout does not reproduce the form')

    # Proper von Mangoldt weight on 4: log 2 / 2, not log 4 / 2.
    total_lo, total_hi = F(0), F(0)
    for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7)):
        lo,hi = log_bounds(F(p)); sl,sh = sqrt_bounds(n)
        total_lo += lo/sh; total_hi += hi/sl
    check(F(292623,100000) < total_lo < total_hi < F(292624,100000),
          'correct prime-power weight sum is in (2.92623,2.92624)')

    report = {
        'status': 'PASS', 'checks': COUNT,
        'delta': encode(delta), 'c_lower': encode(c0),
        'coupling_cap': encode(F(92,100)),
        'full_residual_floor': encode(F(53,100)),
        'second_pivot_floor': encode(d2), 'third_pivot_floor': encode(d3),
        'third_contraction_cap': encode(m3),
        'prime_weight_sum_lower': encode(total_lo),
        'prime_weight_sum_upper': encode(total_hi),
        'scope': 'Scalar budgets only. Infinite-dimensional factorization, domains, and Carleman interface statements require the companion analytic proofs.',
        'nonclaims': 'No A1 replay, no independent external review, no full-window Weil positivity, no RH or novelty claim.'
    }
    Path('triple_rational_results.json').write_text(json.dumps(report,indent=2)+'\n', encoding='utf-8')
    print(f'TOTAL: {COUNT} exact checks PASS')
    print(report['scope'])
    print(report['nonclaims'])

if __name__ == '__main__':
    main()
