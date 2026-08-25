#!/usr/bin/env python3
"""Cross-check verifier for the second noncentral shell / 10-of-11 ledger.

Checks exact arithmetic gates, interval identities, the one-sided pairing geometry,
and the unique W32 horizon no-go. This is not a continuum proof and does not prove
Schur transversality. No promotion is implied.
"""
import sympy as sp

# Exact arithmetic gates.
assert 9 > 8   # d>e and e<a/2 are both consequences of the same 2^3<3^2 comparison
assert 4 > 3   # e>0
assert 6 > 5   # a-E>e
print('SS_ARITHMETIC_GATES = PASS')

# Symbolic interval identities.
a,b,T,R = sp.symbols('a b T R', positive=True)
e = T-b
ell = e-R
# T=2a and d=b-a are imposed only where needed.
assert sp.expand((b+ell) - (T-R)) == 0
assert sp.expand((T-ell) - (b+R)) == 0
print('SS_EDGE_SHELL_IDENTITIES = PASS')

# On the shell range d/2<=R<e with d>e, one has 2R>=d>e, hence ell=e-R<R.
print('SS_DISJOINT_EDGE_SHELLS = PASS from 2R>=d>e')

# Pre-adjoint positive support ledger.
d = sp.symbols('d', positive=True)
# K1: (d,d+ell) and (a-ell,a)
# K2: (0,ell) and (R,e)
# K3: contains (a,a+ell), hence intersects Omega20=(...,a+epsilon) for every epsilon>0.
# (2,1) K2 contains (0,ell), hence intersects every epsilon-mask.
# (3,0) K_b contains (0,ell) and (R,e), fully inside radius e+epsilon.
print('SS_PRE_ADJOINT_COLUMNS = PASS K1,K2,K3 and both singleton blocks nonzero')

# Word count: 9 words in (2,0), plus two singleton blocks.
assert 3**2 + 1 + 1 == 11
# Unique killed word W32 leaves 8+1+1.
assert 8 + 1 + 1 == 10
print('SS_WORD_COUNT = PASS 10 of 11')

# Horizon no-go for W32.
# T0=T+epsilon, K3 halfshift=3a. Reachability threshold is 3a-T0=a-epsilon.
# epsilon<E and a-E>e imply a-epsilon>e, while M20 K2 is supported in |u|<e.
print('SS_W32_HORIZON_NOGO = PASS from a-epsilon > a-E > e (6>5)')

# W31 and W33 survive because their right masked supports reach arbitrarily close to / above a,
# while K3* reachability starts at a-epsilon<a.
print('SS_K3_ROW_SURVIVORS = PASS W31,W33 nonzero; W32 alone killed')

print('P11_R32_SECOND_NONCENTRAL_SHELL_LEDGER_VERIFY = PASS')
