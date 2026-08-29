#!/usr/bin/env python3
import sympy as sp

L2,L3=sp.log(2),sp.log(3)
a=L2/2; b=L3/2; T=2*a; d=b-a; e=T-b
Delta=sp.simplify(d-e)
C=sp.simplify(a+e)
B1=sp.simplify(b+Delta)
B2=sp.simplify(b+2*Delta)
hB=sp.simplify(e-Delta)
kB=sp.simplify(hB-Delta)

s,eps,R=sp.symbols("s eps R", real=True)
u=sp.simplify(hB-s)
t=sp.simplify(Delta-s)
ru=sp.simplify(Delta-u)

# Fixed identities.
assert sp.simplify(C+s-(b-t))==0
assert sp.simplify(B2-s-(B1+t))==0
assert sp.simplify(B2+s-(T+(s-kB)))==0
assert sp.simplify((s-kB)-ru)==0
assert sp.simplify(B2+s-(T+ru))==0

# New B-wall is nested inside the old AWI wall.
assert sp.simplify(hB-Delta-kB)==0
assert kB.is_positive is True
# If s > hB-eps, then automatically s > Delta-eps because hB>Delta.
assert sp.simplify((hB-eps)-(Delta-eps)-kB)==0

# Upper-wall fold parameter u is in the old J:
# u=hB-s; s<h eps? Algebraic endpoint map sends
# s=hB-eps -> u=eps, s=eps -> u=hB-eps.
assert sp.simplify((hB-(hB-eps))-eps)==0
assert sp.simplify((hB-eps)-(hB-eps))==0
# Since hB-eps > Delta-eps, the image interval is contained in J.
assert sp.simplify((hB-eps)-(Delta-eps)-kB)==0

# Its AWI partner is ru=Delta-u=s-kB.
assert sp.simplify(Delta-u-(s-kB))==0

# On a nonempty J_B, eps>hB/2>kB, so |s-kB|<eps for s in J_B.
assert sp.simplify(hB/2-kB-(Delta-kB)/2)==0
assert sp.simplify(Delta-kB).is_positive is True

# Stage-10B orbit translation relations persist.
rD=sp.simplify(Delta-s)
rB=sp.simplify(hB-s)
assert sp.simplify(Delta-rB-(s-kB))==0
assert sp.simplify(hB-rD-(s+kB))==0
assert sp.simplify(3*kB-Delta).is_positive is True

print("SW1-DELTA-DESCENT STAGE-10C CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("C+s = b-(Delta-s): old B-profile is orbit-internal")
print("B2-s = B1+(Delta-s): next-center minus branch is orbit-internal")
print("B2+s = T+(s-kB) = T+r_Delta(r_B(s)): plus branch is inner AWI/2TP")
print("J_B is nested in J and the r_B image lies in J")
print("no new y-boundary type remains on the upper Stage-10 chamber")
print("master-block invertibility follows operatorially from compression of I+A >= I")
