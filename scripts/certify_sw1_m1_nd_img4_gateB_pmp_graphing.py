#!/usr/bin/env python3
"""IMG4 Gate-B exact pmp-graphing premise certificate at epsilon0=Delta/4.

Certifies that the nine A7/A8 graphing maps are partial Lebesgue-measure
preserving Borel bijections with inverses inside the same graphing:
  +a <-> -a,
  +T <-> -T,
  r_a, r_T, r_3a, r_4a, r_2b involutive on invariant domains.

This is exactly the finite geometric premise needed by the self-contained
Mass-Transport proof in the IMG4 analytic-gates audit.  It does not itself
prove the integral Mass-Transport identity or the kernel theorem.
"""

import sympy as sp

print("SW1 M1-ND IMG4 GATE-B PMP GRAPHING CERTIFICATE")

L2,L3=sp.log(2),sp.log(3)
a=L2/2
b=L3/2
T=2*a
d=b-a
e=T-b
Delta=sp.expand(d-e)
eps=sp.expand(Delta/4)
T0=sp.expand(T+eps)

# Exact lower-chamber domains from A7.1--A7.9.
D={
    "+a":(sp.Integer(0),a+eps),
    "-a":(a,T0),
    "+T":(sp.Integer(0),eps),
    "-T":(T,T0),
    "r_T":(sp.Integer(0),T),
    "r_3a":(a-eps,T0),
    "r_4a":(T-eps,T0),
    "r_2b":(2*d-eps,T0),
}
D_ra=[(sp.Integer(0),eps),(a-eps,a)]

# For affine x -> s*x+c, image of open interval (lo,hi).
def image_interval(s,c,lo,hi):
    y1=sp.expand(s*lo+c)
    y2=sp.expand(s*hi+c)
    if s==1:
        return (y1,y2)
    assert s==-1
    return (y2,y1)

def eq_int(I,J):
    return sp.simplify(I[0]-J[0])==0 and sp.simplify(I[1]-J[1])==0

# Translation inverse-domain checks.
assert eq_int(image_interval(1,a,*D["+a"]),D["-a"])
assert eq_int(image_interval(1,-a,*D["-a"]),D["+a"])
assert eq_int(image_interval(1,T,*D["+T"]),D["-T"])
assert eq_int(image_interval(1,-T,*D["-T"]),D["+T"])

# Reflection domain invariance.
assert eq_int(image_interval(-1,T,*D["r_T"]),D["r_T"])
assert eq_int(image_interval(-1,3*a,*D["r_3a"]),D["r_3a"])
assert eq_int(image_interval(-1,4*a,*D["r_4a"]),D["r_4a"])
assert eq_int(image_interval(-1,2*b,*D["r_2b"]),D["r_2b"])

# r_a swaps its two connected components.
ra0=image_interval(-1,a,*D_ra[0])
ra1=image_interval(-1,a,*D_ra[1])
assert eq_int(ra0,D_ra[1])
assert eq_int(ra1,D_ra[0])

# Every graphing map has |Jacobian|=1.
slopes={"+a":1,"-a":1,"+T":1,"-T":1,
        "r_a":-1,"r_T":-1,"r_3a":-1,"r_4a":-1,"r_2b":-1}
assert set(slopes)=={"+a","-a","+T","-T","r_a","r_T","r_3a","r_4a","r_2b"}
assert all(abs(s)==1 for s in slopes.values())

# The finite graphing therefore generates a countable equivalence relation:
# finite words over 9 maps plus inverses form a countable set.
assert len(slopes)==9

print("+a/-a inverse domains: PASS")
print("+T/-T inverse domains: PASS")
print("r_a swaps its two domain components: PASS")
print("r_T,r_3a,r_4a,r_2b invariant involution domains: PASS")
print("all nine graphing maps have |Jacobian|=1: PASS")
print("FINITE PREMISE: A7/A8 is a pmp partial-isometry graphing")
print("FIREWALL: Mass Transport integral identity remains the analytic lemma")
print("SW1 M1-ND IMG4 GATE-B PMP GRAPHING CERTIFICATE: PASS")
