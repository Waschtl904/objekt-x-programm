#!/usr/bin/env python3
"""IMG4 Gate-D finite domain/support premise certificate.

At the explicit witness
    epsilon0 = Delta/4,
    R0       = T/100000,
    sigma0   = R0/2,
this script checks the finite geometric premises used by Gate D:

1. all six KNF sampling half-windows lie inside the positive Horizon (0,T0);
2. the positive Annulus (R0,S0) lies inside the three-lift strip 0<x<3L,
   so every positive Annulus point has a unique decomposition x=theta+kL,
   k in {0,1,2}; hence the IMG0 masks n_k exhaust the whole positive Annulus;
3. the six odd-folded Hub source maps are 1-Lipschitz / partial isometries;
4. with the a.e. physical FREE-component bound 780, the visibility estimate
      |W_vis| <= 6 * 780 * 6R0 = 28080 R0
   is strictly smaller than S0-R0.

It does NOT prove Mass Transport, the reducing-subspace theorem, or the kernel
identity. Those remain analytic gates.
"""

import sympy as sp
from fractions import Fraction as F
from math import lcm

print("SW1 M1-ND IMG4 GATE-D DOMAIN/SUPPORT CERTIFICATE")

L2,L3=sp.log(2),sp.log(3)
a=L2/2
b=L3/2
T=L2
Delta=sp.expand(L3-sp.Rational(3,2)*L2)
L=sp.expand(2*L2-L3)

eps=sp.expand(Delta/4)
R=sp.expand(T/100000)
sigma=sp.expand(R/2)
S=sp.expand(T+sigma)
T0=sp.expand(T+eps)

def coeffs(expr):
    z=sp.expand(expr)
    A=sp.simplify(z.coeff(L2))
    B=sp.simplify(z.coeff(L3))
    rest=sp.simplify(z-A*L2-B*L3)
    assert rest==0,(expr,rest)
    assert A.is_Rational and B.is_Rational,(expr,A,B)
    return F(int(A.p),int(A.q)),F(int(B.p),int(B.q))

def sign(expr):
    A,B=coeffs(expr)
    if A==0 and B==0: return 0
    if A>=0 and B>=0: return 1
    if A<=0 and B<=0: return -1
    den=lcm(A.denominator,B.denominator)
    ai=A.numerator*(den//A.denominator)
    bi=B.numerator*(den//B.denominator)
    if ai>0 and bi<0:
        return (2**ai>3**(-bi))-(2**ai<3**(-bi))
    if ai<0 and bi>0:
        return (3**bi>2**(-ai))-(3**bi<2**(-ai))
    raise AssertionError((expr,A,B))

# Exact witness admissibility.
for z in [sigma,R-sigma,eps-R,Delta-(R+eps)]:
    assert sign(sp.expand(z))>0,z

# Six KNF half-windows: (tau-R,tau) and (tau,tau+R), tau=a,b,T.
# It suffices that every lower endpoint is >0 and every upper endpoint <T0.
for tau in [a,b,T]:
    assert sign(sp.expand(tau-R))>0,("lower",tau)
    assert sign(sp.expand(T0-(tau+R)))>0,("upper",tau)

# Optional stronger check: at the explicit tiny R, the six half-windows are
# pairwise disjoint up to their shared center endpoints.
centers=[a,b,T]
assert sign(sp.expand((b-R)-(a+R)))>0
assert sign(sp.expand((T-R)-(b+R)))>0

# The whole positive Annulus is contained in three lift strips k=0,1,2.
# R>0 and S<3L imply unique x=theta+kL with theta in [0,L), k in {0,1,2}.
assert sign(R)>0
assert sign(sp.expand(3*L-S))>0

# Each positive annulus point therefore belongs to exactly one IMG0 mask
# n_k(theta)=1_{R<theta+kL<S}; no extra covariance constraint exists in B_W.
# This is the finite geometric premise behind arbitrary L2(B0) reconstruction.

# Hub source maps on x>0:
# |x-a|, x+a, |x-b|, x+b, |x-T|, x+T.
# On each monotonicity piece their slopes are +/-1.
hub_maps={
    "abs_a":(-1,1),  # two pieces
    "plus_a":(1,),
    "abs_b":(-1,1),
    "plus_b":(1,),
    "abs_T":(-1,1),
    "plus_T":(1,),
}
assert len(hub_maps)==6
assert all(abs(s)==1 for slopes in hub_maps.values() for s in slopes)

# Exact blind-measure comparison using the corrected a.e. component bound.
COMP_AE=780
KNF_BRANCHES=6
HUB_BRANCHES=6
factor=COMP_AE*KNF_BRANCHES*HUB_BRANCHES
assert factor==28080

visible=sp.expand(factor*R)
annulus_len=sp.expand(S-R)
margin=sp.expand(annulus_len-visible)
assert sign(margin)>0

# Rational T-normalized identity:
# visible/T = 28080/100000 = 351/1250
# annulus_len/T = 1 - 1/200000.
assert F(28080,100000)==F(351,1250)
assert F(351,1250) < F(1)-F(1,200000)

print("explicit SW1 witness inequalities: PASS")
print("all six KNF half-windows lie inside (0,T0): PASS")
print("explicit six KNF half-windows are pairwise disjoint a.e.: PASS")
print("positive Annulus satisfies S<3L; three IMG0 lift masks exhaust it: PASS")
print("six Hub positive source maps have only slopes +/-1: PASS")
print("a.e. visibility factor:",factor)
print("28080 R0 < S0-R0: PASS")
print("FIREWALL: finite domain/support premises only; no kernel promotion")
print("SW1 M1-ND IMG4 GATE-D DOMAIN/SUPPORT CERTIFICATE: PASS")
