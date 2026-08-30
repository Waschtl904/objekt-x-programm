#!/usr/bin/env python3
"""SW1-A10-H3 exact H2-only rotation-cover certificate.

Finite/algebraic scope only.

Use the A10-H2 certified t-cell ledger. For fixed small-lower-chamber
parameters define the free blind band J=(0,L). The certificate verifies four
H2-only words which realize the circle rotation x -> x+Delta (mod L):

  low branch 0<x<L-Delta:
    P1 on (0,e-R), P2 on (e-R,e), P3 on (e,L-R), each x->x+Delta;

  wrap branch L-Delta<x<L:
    W on the whole interval, x->x+Delta-L.

Since R<Delta, the three low domains cover (0,L-Delta) except the two open
cell boundaries e-R,e. The only finite exceptional physical points are thus
cell/switch boundaries. The infinite-orbit conclusion additionally uses the
separate analytic input Delta/L irrational.

Firewall: this certifies the H2 word cover and physical free-band legality.
It does not certify any Cross-Gram kernel vector or noninjectivity.
"""
import sympy as sp

R,B,C,G=sp.symbols("R B C G", positive=True)
eps=R+B
Delta=2*(R+B+C)
L=4*Delta+2*G
e=L/2
d=e+Delta
a=L+Delta
b=sp.Rational(3,2)*L+2*Delta
T=2*L+2*Delta
T0=T+eps

assert sp.simplify(Delta/2-eps-C)==0
assert sp.simplify(L/2-2*Delta-G)==0
assert sp.simplify(a-R-L-(Delta-R))==0
assert (Delta-R).is_positive is True

def ch(s,twolam,k,t):
    return s*t+sp.Rational(twolam,2)*L+k*Delta

t=sp.symbols("t", real=True)
x=sp.symbols("x", real=True)

def amap(src,tgt):
    ts=sp.solve(sp.Eq(x,ch(*src,t)),t)[0]
    return sp.expand(ch(*tgt,t).subs(t,ts))

P1a=((+1,-3,-2),(-1,4,2))
P1b=((-1,3,2),(+1,-2,-1))
P2a=((+1,-3,-2),(-1,7,4))
P2b=((+1,1,1),(-1,3,2))
P3a=((-1,4,2),(-1,3,2))
P3b=((-1,2,1),(-1,3,2))
W2 =((-1,4,2),(+1,-3,-2))
W3 =((-1,3,2),(-1,4,2))
W4 =((+1,-2,-1),(-1,3,2))

maps={
 "P1a":amap(*P1a), "P1b":amap(*P1b),
 "P2a":amap(*P2a), "P2b":amap(*P2b),
 "P3a":amap(*P3a), "P3b":amap(*P3b),
 "W2":amap(*W2), "W3":amap(*W3), "W4":amap(*W4),
}
assert sp.simplify(maps["P1a"]-(e-x))==0
assert sp.simplify(maps["P1b"]-(d-x))==0
assert sp.simplify(maps["P2a"]-(T-x))==0
assert sp.simplify(maps["P2b"]-(2*L+3*Delta-x))==0
assert sp.simplify(maps["P3a"]-(x-e))==0
assert sp.simplify(maps["P3b"]-(x+d))==0
assert sp.simplify(maps["W2"]-(e-x))==0
assert sp.simplify(maps["W3"]-(x+e))==0
assert sp.simplify(maps["W4"]-(d-x))==0

def comp(expr, names):
    y=expr
    for n in names:
        y=sp.expand(maps[n].subs(x,y))
    return sp.expand(y)

assert sp.simplify(comp(x,["P1a","P1b"])-(x+Delta))==0
assert sp.simplify(comp(x,["P2a","P2b"])-(x+Delta))==0
assert sp.simplify(comp(x,["P3a","P3b"])-(x+Delta))==0
assert sp.simplify(comp(x,["P3a","W2","W3","W4"])-(x+Delta-L))==0

assert sp.simplify((d-eps)-e-(Delta-eps))==0
assert (Delta-eps).is_positive is True
assert sp.simplify((T-e)-b)==0

assert sp.simplify((e+(e-R))-(L-R))==0
assert sp.simplify((a-eps)-(L-R)-(Delta-eps+R))==0
assert (Delta-eps+R).is_positive is True

assert sp.simplify((L-R)-(L-Delta)-(Delta-R))==0
assert (Delta-R).is_positive is True

assert sp.simplify((L-Delta)-e-(e-Delta))==0
assert sp.simplify(e-Delta-(Delta+G))==0
assert (Delta+G).is_positive is True
assert sp.simplify((a-eps)-L-(Delta-eps))==0
assert sp.simplify((e-Delta)-R-(Delta+G-R))==0
assert (Delta+G-R).is_positive is True
assert sp.simplify((d-eps)-Delta-(e-eps))==0
assert (e-eps).is_positive is True

assert sp.simplify(L-Delta-(3*Delta+2*G))==0
assert (3*Delta+2*G).is_positive is True
assert sp.simplify((a-R)-L-(Delta-R))==0

print("SW1-A10-H3 H2-ONLY ROTATION-COVER CERTIFICATE: PASS")
print("exact symbolic arithmetic: SymPy")
print("free invariant band candidate: J=(0,L) subset (0,a-R)")
print("low words: P1 on (0,e-R), P2 on (e-R,e), P3 on (e,L-R)")
print("all low words implement x -> x+Delta")
print("wrap word is legal on all (L-Delta,L) and implements x -> x+Delta-L")
print("therefore the H2 incidence graph realizes Delta-rotation on J away from finitely many open-cell boundaries")
print("ANALYTIC INPUT FOR INFINITE ORBIT: Delta/L irrational (separate A4/A5 result)")
print("FIREWALL: rotation-cover algebra only; no Cross-Gram kernel/noninjectivity claim")
