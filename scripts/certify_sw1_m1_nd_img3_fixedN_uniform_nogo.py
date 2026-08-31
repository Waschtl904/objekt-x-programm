#!/usr/bin/env python3
"""SW1 M1-ND IMG3 fixed-order Neumann truncation uniform no-go.

For the truncation
  A_N = C_K sum_{n=0}^N (-K_R)^n D_R^{-1} H_R,
K_R=D_R^{-1}R_R,
count raw affine sampling paths only.

Facts:
- C_K has at most 6 sample branches.
- each off-diagonal FREE row of R_R has at most 5 source branches.
- H_R has at most 6 annulus source branches.
- D_R^{-1} changes coefficients/gates but creates no new sample map.

Hence order n has at most 36*5^n affine annulus sample maps and the full
0..N truncation has at most
  M_N = 36 sum_{n=0}^N 5^n = 9(5^(N+1)-1)
maps.

Each map sends u in (0,R) by an affine isometry t=+-u+c, so it can see an
annulus interval of length at most R.  Therefore the visible annulus measure
is <= M_N R.

For every fixed N we exhibit an admissible SW1 parameter point with
M_N R < |(R,S)|, so the truncation has a positive-measure blind set and an
infinite-dimensional kernel.  Thus no fixed N can yield a uniform bounded-
below proof over the entire open SW1 scope.
"""

import sympy as sp

print("SW1 M1-ND IMG3 FIXED-ORDER TRUNCATION UNIFORM NO-GO")

N=sp.symbols("N", integer=True, nonnegative=True)
M=9*(5**(N+1)-1)

L2,L3=sp.log(2),sp.log(3)
a=L2/2
T=2*a
d=L3/2-a
e=T-L3/2
Delta=sp.simplify(d-e)

assert T.is_positive is True
assert Delta.is_positive is True

# Universal explicit witness in terms of abstract positive T,Delta and
# a positive path-count M.  This isolates the inequality proof from CAS
# recognition of the logarithmic constants; the physical T,Delta above were
# already proved positive separately.
m=sp.symbols("m", positive=True)
Tw,Dw=sp.symbols("Tw Dw", positive=True)
Rw=sp.simplify(Dw*Tw/(10*(m+1)*(Tw+Dw)))
epsw=2*Rw
sigmaw=Rw/2
Sw=Tw+sigmaw

# Exact admissibility margins.
assert Rw.is_positive is True
assert sp.simplify(Rw-sigmaw).is_positive is True
assert sp.simplify(epsw-Rw).is_positive is True
assert sp.factor(Dw-(Rw+epsw)).is_positive is True

# Visible-measure versus annulus-length margin.
# It suffices that m*R < T-R, since S-R = T-R/2 > T-R.
margin=sp.factor((Tw-Rw)-m*Rw)
assert margin.is_positive is True
assert sp.factor((Sw-Rw)-(Tw-Rw)).is_positive is True

# Concrete sanity instances; these are not the universal proof.
for n in range(8):
    mn=9*(5**(n+1)-1)
    rv=sp.simplify(Rw.subs({m:mn,Tw:T,Dw:Delta}))
    assert sp.N(mn*rv) < sp.N((T+rv/2)-rv)

print("raw branch bounds: C_K<=6, R_R<=5 per step, H_R<=6")
print("M_N = 9*(5^(N+1)-1)")
print("explicit witness R_N = Delta*T/[10*(M_N+1)*(T+Delta)]")
print("choose sigma_N=R_N/2, eps_N=2R_N")
print("SW1 admissibility for every fixed N: PASS")
print("M_N*R_N < annulus length S_N-R_N: PASS")
print("CONCLUSION: every fixed finite truncation fails uniform injectivity on full SW1")
print("FIREWALL: N may still depend on parameters; full infinite Neumann operator unaffected")
print("SW1 M1-ND IMG3 FIXED-ORDER TRUNCATION UNIFORM NO-GO: PASS")
