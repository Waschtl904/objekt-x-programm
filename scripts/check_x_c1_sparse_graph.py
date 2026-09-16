#!/usr/bin/env python3
"""Exact support-budget and finite-analogue tests for X-C1-SPARSE-GRAPH.

Python standard library only; no floats, quadrature, A1/C0 replay, or large
matrix. The finite graph tests check algebra and all inclusion patterns of
six cells. They do not replace the continuous-domain proofs in the note.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

counts: dict[str, int] = {}


def require(group: str, condition: bool, detail: str) -> None:
    if not condition:
        raise AssertionError(f'{group}: {detail}')
    counts[group] = counts.get(group, 0) + 1


def log_lower(x: F, terms: int) -> F:
    if x <= 1 or terms < 1:
        raise ValueError('Use x>1 and at least one term.')
    t = (x-1)/(x+1)
    return 2*sum((t**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))


# All inequalities below use positive-term log series and rational arithmetic.
delta = F(1, 50)
log2_low = log_lower(F(2), 5)
require('constant budgets', log2_low > F(2, 3), 'log 2 lower bound')
gamma_upper = sum((F(1, k) for k in range(1, 33)), F(0))-5*log2_low
require('constant budgets', gamma_upper < F(3, 5), 'H32-5 log 2 < 3/5')
require('constant budgets', log_lower(F(175, 11), 15) > F(11, 4), 'log(175/11)>11/4')
require('constant budgets', 1+F(7,10)+F(7,10)**2/2+F(7,10)**3/6 > 2, 'log 2 < 7/10')
require('constant budgets', F(7,5)**2 < 2, 'sqrt(2)>7/5')
for k in range(1, 6):
    require('integer isolation', F(1, 2**k+1) > delta, f'upper neighbor at 2^{k}')
    require('integer isolation', F(1, 2**k) > delta, f'lower neighbor at 2^{k}')

prime_upper = {1:F(1,2), 2:F(7,20), 3:F(1,4), 4:F(7,40), 5:F(1,8)}
gamma_upper_by_gap = {k:delta*(1+1/(2*(F(2*k,3)-delta))) for k in range(1,6)}
V = frozenset(range(6))
sets = [frozenset(i for i in V if mask & (1 << i)) for mask in range(1,64)]
max_prime, max_gamma = F(0), F(0)
for S in sets:
    for i in S:
        p = sum((prime_upper[abs(i-j)] for j in S if j != i), F(0))
        g = sum((gamma_upper_by_gap[abs(i-j)] for j in S if j != i), F(0))
        require('all cell rows', p <= F(39,20), f'prime row {S}, {i}')
        require('all cell rows', g <= F(1430258,9458955), f'Gamma row {S}, {i}')
        max_prime, max_gamma = max(max_prime,p), max(max_gamma,g)
require('exact margins', max_prime == F(39,20), 'maximal prime degree')
require('exact margins', max_gamma == F(1430258,9458955), 'maximal Gamma loss')
margin = F(11,4)-F(3,5)-F(1,200)-max_prime-max_gamma
require('exact margins', margin == F(16569529,378358200), 'exact slack bound')
require('exact margins', margin-F(1,25) == F(1435201,378358200), 'positive surplus beyond 1/25')
require('exact margins', margin > F(1,25), 'strict slack')
require('exact margins', sum(prime_upper.values(),F(0)) == F(7,5), 'bounded readout upper budget')
require('exact margins', F(592,45) < 16, 'C0-to-readout norm is below 4')

# Exact complex arithmetic over Q(i).
Z = tuple[F, F]
ZERO: Z = (F(0),F(0))

def sub(a: Z, b: Z) -> Z:
    return a[0]-b[0], a[1]-b[1]

def neg(a: Z) -> Z:
    return -a[0],-a[1]

def norm2(a: Z) -> F:
    return a[0]**2+a[1]**2

def real_pair(a: Z, b: Z) -> F:
    return a[0]*b[0]+a[1]*b[1]

# Finite analogue: two positive edge measures on the same oriented pairs.
# Its rational weights are not presented as numerical values of h or log(2).
Edge = tuple[str,int,int]
weights: dict[Edge,F] = {}
for lo, hi in combinations(range(6),2):
    weights[('gamma',hi,lo)] = F(1,1+hi-lo)
    weights[('prime',hi,lo)] = F(1,2+hi-lo)
external = {i:F(12)+F(i,7) for i in V}
kappa = F(1)

def edges(S: frozenset[int]) -> list[Edge]:
    return [e for e in weights if e[1] in S and e[2] in S]

def rho(S: frozenset[int], i: int) -> F:
    gamma_out = sum((weights[('gamma',max(i,j),min(i,j))] for j in V-S),F(0))
    prime_in = sum((weights[('prime',max(i,j),min(i,j))] for j in S if j != i),F(0))
    return external[i]+gamma_out-kappa-prime_in

Output = tuple[dict[Edge,Z],dict[int,Z]]

def readout(S: frozenset[int], u: dict[int,Z]) -> Output:
    return {e:sub(u[e[1]],u[e[2]]) for e in edges(S)}, dict(u)

def outnorm(S: frozenset[int], out: Output) -> F:
    e,z = out
    return sum((weights[k]*norm2(value) for k,value in e.items()),F(0)) + sum((rho(S,i)*norm2(z[i]) for i in S),F(0))

def primitive(S: frozenset[int], u: dict[int,Z]) -> F:
    v = {i:u.get(i,ZERO) for i in V}
    ans = sum(((external[i]-kappa)*norm2(v[i]) for i in V),F(0))
    for e,w in weights.items():
        kind, hi, lo = e
        ans += w*norm2(sub(v[hi],v[lo])) if kind == 'gamma' else -2*w*real_pair(v[hi],v[lo])
    return ans

def inclusion(S: frozenset[int], T: frozenset[int], out: Output) -> Output:
    if not S <= T:
        raise ValueError('Non-nested supports')
    old,z = out
    new: dict[Edge,Z] = {}
    for e in edges(T):
        _,hi,lo = e
        if hi in S and lo in S:
            new[e] = old[e]
        elif hi in S:
            new[e] = z[hi]
        elif lo in S:
            new[e] = neg(z[lo])
        else:
            new[e] = ZERO
    return new,{i:z.get(i,ZERO) for i in T}

sample_u: dict[frozenset[int],dict[int,Z]] = {}
sample_out: dict[frozenset[int],Output] = {}
for S in sets:
    u = {i:(F(i+1,3),F(2-i,5)) for i in S}
    # Edge values independent of vertex values: checks the WHOLE target map.
    es = {e:(F(1+e[1]+e[2],7),F(e[1]-2*e[2]+(e[0]=='prime'),11)) for e in edges(S)}
    out = es,{i:(F(i+2,4),F(1-i,6)) for i in S}
    sample_u[S],sample_out[S] = u,out
    require('finite energy identities', primitive(S,u) == outnorm(S,readout(S,u)), f'energy split {S}')
    require('finite energy identities', all(rho(S,i)>0 for i in S), f'positive model slack {S}')

for S in sets:
    for T in sets:
        if not S <= T:
            continue
        out = sample_out[S]
        require('inclusion isometries', outnorm(S,out) == outnorm(T,inclusion(S,T,out)), f'{S}->{T}')
        u = sample_u[S]
        extended = {i:u.get(i,ZERO) for i in T}
        require('readout intertwinings', inclusion(S,T,readout(S,u)) == readout(T,extended), f'{S}->{T}')
        for U in sets:
            if T <= U:
                require('inclusion cocycles', inclusion(T,U,inclusion(S,T,out)) == inclusion(S,U,out), f'{S}->{T}->{U}')

if __name__ == '__main__':
    for name,total in counts.items():
        print(f'PASS  {name}: {total}')
    print(f'TOTAL: {sum(counts.values())} exact checks PASS')
    print(f'Exact slack lower comparison: {margin}')
    print(f'Surplus beyond 1/25: {margin-F(1,25)}')
    print('Finite graph weights are an algebraic analogue, not a quadrature of the continuum.')
    print('Analytic convergence/domain proofs and the six-interval scope remain essential.')
    print('No independent external review, full C1-GEOM, Object X, or RH claim.')
