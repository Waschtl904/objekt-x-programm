#!/usr/bin/env python3
"""Exact scalar/algebra checks for X-C1-CONNECTED-3/8.

Standard library only. This is NOT a full-form discretization, A1 replay,
external review, or proof of all-window positivity. The companion note proves
all kernel, domain, infinite-series and operator statements analytically.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path

CHECKS: list[dict[str, str]] = []


def require(ok: bool, name: str) -> None:
    if not ok:
        raise AssertionError(name)
    CHECKS.append({'name': name, 'status': 'PASS'})
    print('PASS:', name)


def exp_bounds(x: F, n: int = 40) -> tuple[F, F]:
    if x < 0:
        lo, hi = exp_bounds(-x, n)
        return 1 / hi, 1 / lo
    if x >= n + 2:
        raise ValueError('Taylor tail ratio must be less than one')
    p = sum((x**k / factorial(k) for k in range(n + 1)), F(0))
    tail = (x ** (n + 1) / factorial(n + 1)) / (1 - x / (n + 2))
    return p, p + tail


def log_unit(x: F, n: int = 48) -> tuple[F, F]:
    if not F(1) <= x <= F(2):
        raise ValueError('log_unit requires 1 <= x <= 2')
    q = (x - 1) / (x + 1)
    p = 2 * sum((q ** (2*k + 1) / (2*k + 1) for k in range(n)), F(0))
    tail = 2*q ** (2*n + 1) / ((2*n + 1)*(1-q*q))
    return p, p + tail


def log_bounds(x: F) -> tuple[F, F]:
    if x <= 0:
        raise ValueError('positive logarithm argument required')
    if x < 1:
        lo, hi = log_bounds(1/x)
        return -hi, -lo
    k = 0
    while x > 2:
        x /= 2
        k += 1
    lo, hi = log_unit(x)
    l2, u2 = log_unit(F(2))
    return lo + k*l2, hi + k*u2


# Polynomials are coefficient lists in increasing degree.
def trim(p: list[F]) -> list[F]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p: list[F], q: list[F]) -> list[F]:
    out = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p): out[i] += x
    for i, x in enumerate(q): out[i] += x
    return trim(out)


def scale(p: list[F], c: F) -> list[F]:
    return trim([c*x for x in p])


def harmonic(n: int) -> F:
    return sum((F(1,k) for k in range(1,n+1)), F(0))


def regional_operator(p: list[F]) -> list[F]:
    """A x^m = H_m x^m - sum_{k odd, 1<=k<m} x^(m-1-k)/(k+1)."""
    out = [F(0)]*len(p)
    for m, c in enumerate(p):
        out[m] += c*harmonic(m)
        for k in range(1,m,2):
            out[m-1-k] -= c/F(k+1)
    return trim(out)


def main() -> None:
    a, length, z = F(3,8), F(3,4), F(3,16)
    l2,u2 = log_bounds(F(2))
    l3,u3 = log_bounds(F(3))
    require(F(69,100)<l2 and u2<F(7,10), '69/100 < log 2 < 7/10')
    require(l3>1, 'log 3 > 1: only Prime 2 is active on length 3/4')
    require(u2<length and 2*l2>length, 'one active shift, with disjoint endpoint bands')
    require(u2/2+F(1,100)<a, 'the original fixed Prime-2 pair lies inside the new interval')
    require(F(7,5)**2<2 and F(7,10)/F(7,5)==F(1,2), 'w2 < 1/2')

    # Uniform lower kernel comparison on 0 < t <= 3/4.
    b = F(1,6)/(1-length**2/20)
    margin = F(1,10)-(b-F(1,8))*length-F(2,5)*b*length**2
    require(b==F(160,933), 'geometric sinh(t)/t majorant coefficient')
    require(margin==F(1321,49760) and margin>0,
            'uniform polynomial margin for h(t) > 1/(2t) + 1/5')
    require(exp_bounds(F(3,8))[1]<F(3,2),
            'convex exponential bound for h(t) < 1/(2t) + 1/3')

    # Exterior reserve: gamma < 579/1000 from a harmonic/log enclosure.
    gamma_upper=harmonic(400)-log_bounds(F(400))[0]
    require(gamma_upper<F(579,1000), 'gamma < H400-log400 < 579/1000')
    require(log_bounds(F(33,14))[1]<F(429,500), 'log(33/14) < 429/500')
    reserve_cost=F(429,500)+F(579,1000)+F(3,16)
    require(reserve_cost==F(3249,2000) and reserve_cost<F(13,8),
            'central exterior reserve > -3249/2000 > -13/8')
    require(F(4)/(3*F(22,7))==F(14,33), 'pi < 22/7 gives the correct logarithmic ratio')

    # Actual shift can be charged to enhanced exterior leakage at the ends.
    require(length-F(69,100)==F(3,50), 'L-log2 < 3/50')
    require(a*a/(F(3,50)*F(7,10))==F(375,112), 'endpoint leakage logarithmic ratio')
    require(exp_bounds(F(6,5))[1]<F(375,112), 'log(375/112) > 6/5')
    edge_gain=F(3,5)-F(2,15)*F(13,40)
    require(edge_gain==F(167,300) and edge_gain>F(1,2),
            'endpoint leakage gain > 167/300 > w2')
    require(F(13,8)-reserve_cost==F(1,2000), 'positive vertex weight V > 1/2000')

    # Two global moment vectors, not per-cell constraints.
    cosh_err=z*z/(2*(1-z*z/12))
    sinh_rel=z*z/(6*(1-z*z/20))
    require(cosh_err<F(1,50), 'cosh(x/2)-1 < 1/50 on the full interval')
    require(sinh_rel<F(1,150), 'sinh(x/2)/(x/2)-1 < 1/150')
    require(F(1,5)*length==F(3,20), 'constant-kernel complete-graph energy coefficient')
    require(F(13,8)-1-F(3,20)==F(19,40), 'exact negative first-mode coefficient')
    require(F(13,8)-F(3,20)==F(59,40), 'high-mode weights H_n-59/40')
    require(harmonic(2)-F(59,40)==F(1,40), 'smallest high-mode weight is 1/40')
    be2=F(13,8)*40/F(50)**2
    bo2=F(19,40)*40/F(150)**2
    require(be2==F(13,500), 'even moment row norm squared < 13/500')
    require(bo2==F(19,22500) and bo2<be2, 'odd moment row is smaller; parities are orthogonal')
    require(be2<F(1,36), 'rank-two contraction has norm < 1/6')
    floor=(1-be2)*F(1,40)/(1+F(1,2500))
    require(floor==F(487,20008) and floor>F(1,50), 'full connected NULLPOL lower bound > 1/50')

    # Finite algebra regressions only. The all-degree proof is in the note.
    polys=[[F(1)],[F(0),F(1)]]
    for n in range(1,12):
        polys.append(scale(add(scale([F(0)]+polys[-1], F(2*n+1)),
                               scale(polys[-2], F(-n))), F(1,n+1)))
    for n,p in enumerate(polys):
        require(regional_operator(p)==scale(p,harmonic(n)),
                f'polynomial regression A P_{n} = H_{n} P_{n}')

    result={
        'status':'EXACT_SCALAR_AND_POLYNOMIAL_CHECKS_ONLY',
        'check_count':len(CHECKS),
        'interval_half_width':str(a),
        'length':str(length),
        'central_reserve_lower':str(-reserve_cost),
        'vertex_lower':str(F(1,2000)),
        'B_norm_squared_upper':str(be2),
        'Q_lower':str(floor),
        'coarse_claim':str(F(1,50)),
        'gamma_upper_rational':str(gamma_upper),
        'checks':CHECKS,
        'not_tested':['external mathematical review','full unit window','all-window X',
                      'A1','pointwise or arbitrary-source numerical positivity']}
    Path('connected_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'TOTAL: {len(CHECKS)} exact scalar/algebra checks PASS')
    print('The analytic infinite-dimensional proof is in X_C1_CONNECTED_MOMENT_FACTORIZATION.md.')
    print('No A1 replay, no CI claim, no independent review, no full-unit-window claim.')


if __name__=='__main__':
    main()
