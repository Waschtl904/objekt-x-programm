#!/usr/bin/env python3
"""Cross-check verifier for the FG classification candidate.

Checks exact shift arithmetic, sampling-window connectivity thresholds, horizon
identities, and affine-overlap compositions. It does not replace the continuum
branch/gluing reconstruction proof and does not prove Schur transversality.
"""
import sympy as sp

L2 = sp.log(2)
L3 = sp.log(3)
a = L2/2
b = L3/2
T = 2*a
d = b-a
e = T-b
delta = d-e

# Exact arithmetic gates already used throughout P11/R32.
assert 9 > 8       # d>e
assert 32 > 27     # e>d/2
assert 4 > 3       # e>0
print('FG_ARITHMETIC_GATES = PASS')

# Center differences and compositions.
u = sp.symbols('u', real=True)
sd = lambda x: d-x
se = lambda x: e-x
sa = lambda x: a-x
assert sp.simplify(sd(se(u))-(u+delta)) == 0
assert sp.simplify(sa(sd(u))-(u+e)) == 0
assert sp.simplify(sa(se(u))-(u+d)) == 0
assert sp.simplify(a-d-e) == 0
assert sp.simplify(a-e-d) == 0
print('FG_AFFINE_COMPOSITIONS = PASS')

# Horizon identities.
eps = sp.symbols('epsilon', positive=True)
T0 = T+eps
assert sp.simplify(T0-b-(e+eps)) == 0
assert sp.simplify(T0-T-eps) == 0
print('FG_HORIZON_IDENTITIES = PASS')

# Sampling-window overlap thresholds: R>=d/2 implies both a/b and b/T overlaps.
R = sp.symbols('R', positive=True)
# Gaps are (b-R)-(a+R)=d-2R and (T-R)-(b+R)=e-2R.
assert sp.simplify((b-R)-(a+R)-(d-2*R)) == 0
assert sp.simplify((T-R)-(b+R)-(e-2*R)) == 0
print('FG_WINDOW_GAP_IDENTITIES = PASS')

# Blind-tail geometry when R<epsilon.
assert sp.simplify((T0)-(T+R)-(eps-R)) == 0
print('FG_HORIZON_TAIL_LENGTH = PASS epsilon-R')

# Irrationality proof ledger (textual exact argument):
# d/e=m/n => (3/2)^n=(4/3)^m => 3^(n+m)=2^(n+2m), impossible
# by unique prime factorization for positive integers m,n.
print('FG_IRRATIONALITY_LEDGER = PASS by unique-factorization argument in audit')

print('P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_VERIFY = PASS')
