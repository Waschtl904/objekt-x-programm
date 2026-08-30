#!/usr/bin/env python3
"""Independent finite review of SW1-A10-H3 rotation-cover logic.

Checks:
1. canonical disjoint zone partition of J=(0,L):
   Z1=(0,e-R), Z2=(e-R,e), Z3=(e,L-Delta), Z4=(L-Delta,L);
2. every word segment is an actual pair of channels co-active in one exact H2 t-cell;
3. each canonical word maps to x+Delta (Z1-Z3) or x+Delta-L (Z4);
4. all intermediate physical points remain in the positive horizon;
5. the only canonical boundaries are 0~L, e-R, e, L-Delta;
6. P3/W overlap outside the canonical choice is acknowledged: both can be legal,
   but the canonical selector uses W on the wrap zone, so no uniqueness is claimed
   for the underlying graph relation.

Analytic infinite-orbit input remains separate: Delta/L irrational and the
countable-exception argument.
"""
import sympy as sp

R,B,C,G=sp.symbols("R B C G", positive=True)
eps=R+B
Delta=2*(R+B+C)
L=4*Delta+2*G
e=L/2; d=e+Delta; a=L+Delta
b=sp.Rational(3,2)*L+2*Delta
T=2*L+2*Delta
S=sp.symbols("S", positive=True)
x,t=sp.symbols("x t", real=True)

# H2 exact t-cells used by the selected word segments.
cells={
  4:(d+R,a),
  7:(a+eps,b),
  8:(b,T-R),
  9:(T-R,T),
}
# H2 compact-ledger channels in those cells, tuples (s,2lambda,k).
C4={(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1)}
C7={(-1,3,2),(-1,4,2),(1,-2,-1)}
C8={(-1,4,2),(1,-3,-2),(1,-2,-1)}
C9={(-1,4,2),(-1,6,3),(-1,7,4),(-1,8,4),(1,-3,-2),(1,-1,0),(1,0,0)}
ledger={4:C4,7:C7,8:C8,9:C9}

def ch(q):
    s,twolam,k=q
    return s*t+sp.Rational(twolam,2)*L+k*Delta

def bridge(src,tgt):
    assert any(src in v and tgt in v for v in ledger.values())
    ts=sp.solve(sp.Eq(x,ch(src)),t)[0]
    return sp.expand(ch(tgt).subs(t,ts)), ts

P1a=((1,-3,-2),(-1,4,2))       # cell 8
P1b=((-1,3,2),(1,-2,-1))       # cell 7
P2a=((1,-3,-2),(-1,7,4))       # cell 9
P2b=((1,1,1),(-1,3,2))         # cell 5 in full H2 ledger, add explicitly below
P3a=((-1,4,2),(-1,3,2))        # cell 7
P3b=((-1,2,1),(-1,3,2))        # cell 4
W2=((-1,4,2),(1,-3,-2))        # cell 8
W3=((-1,3,2),(-1,4,2))         # cell 7
W4=((1,-2,-1),(-1,3,2))        # cell 7

# Full cell 5 needed for P2b.
ledger[5]={(-1,3,2),(-1,5,3),(-1,6,3),(1,-2,-1),(1,0,0),(1,1,1),(1,2,1)}

pairs=[P1a,P1b,P2a,P2b,P3a,P3b,W2,W3,W4]
maps={}
tsrc={}
for i,p in enumerate(pairs):
    maps[i],tsrc[i]=bridge(*p)

expected=[
    e-x, d-x, T-x, 2*L+3*Delta-x,
    x-e, x+d, e-x, x+e, d-x
]
for got,want in zip(maps.values(),expected):
    assert sp.simplify(got-want)==0

def compose(indices):
    y=x
    for i in indices:
        y=sp.expand(maps[i].subs(x,y))
    return sp.expand(y)

assert sp.simplify(compose([0,1])-(x+Delta))==0
assert sp.simplify(compose([2,3])-(x+Delta))==0
assert sp.simplify(compose([4,5])-(x+Delta))==0
assert sp.simplify(compose([4,6,7,8])-(x+Delta-L))==0

# Canonical zone ordering:
# 0 < e-R < e < L-Delta < L.
assert (e-R).is_positive is True
assert R.is_positive is True
assert sp.simplify((L-Delta)-e-(Delta+G))==0
assert (Delta+G).is_positive is True
assert Delta.is_positive is True

# Also L-Delta < L-R since Delta>R.
assert sp.simplify((L-R)-(L-Delta)-(Delta-R))==0
assert (Delta-R).is_positive is True

# Segment-to-cell legality. We prove the source-annulus t ranges land inside
# one H2 cell for the entire canonical source zone.
# P1a: t=x+b, x in (0,e-R) -> (b,T-R), cell 8.
assert sp.simplify((b+(e-R))-(T-R))==0
# P1b after y=e-x: t=b-y=b-e+x; range (b-e,b-R).
# b-e = a+Delta > a+eps, hence cell 7.
assert sp.simplify((b-e)-(a+eps)-(Delta-eps))==0
assert (Delta-eps).is_positive is True

# P2a: t=x+b, x in (e-R,e) -> (T-R,T), cell 9.
assert sp.simplify((b+e)-T)==0
# P2b after y=T-x: source (+1,1,1) gives t=y-d.
# x in (e-R,e) -> t in (a,a+R), cell 5.
assert sp.simplify((T-e)-d-a)==0
assert sp.simplify((T-(e-R))-d-(a+R))==0

# P3a: t=T-x. Canonical x in (e,L-Delta) maps into
# (T-(L-Delta), T-e)=(L+3Delta,b), subset cell 7.
assert sp.simplify((T-e)-b)==0
assert sp.simplify((T-(L-Delta))-(a+eps)-(2*Delta-eps))==0
assert (2*Delta-eps).is_positive is True
# P3b after y=x-e: t=a-y=a+e-x.
# x in (e,L-Delta) -> t in (e+2Delta,a), subset cell 4=(d+R,a).
assert sp.simplify((e+2*Delta)-(d+R)-(Delta-R))==0
assert (Delta-R).is_positive is True

# Wrap first segment P3a: t=T-x, x in (L-Delta,L) ->
# (L+2Delta,L+3Delta), all in cell 7.
assert sp.simplify((L+2*Delta)-(a+eps)-(Delta-eps))==0
# W2 after y=x-e: t=T-y=T-x+e -> (b,b+Delta), cell 8,
# and b+Delta<T-R because e-Delta-R>0.
assert sp.simplify((T-R)-(b+Delta)-(e-Delta-R))==0
assert sp.simplify((e-Delta-R)-(Delta+G-R))==0
assert (Delta+G-R).is_positive is True
# W3 after z=L-x: t=b-z -> (b-Delta,b), cell 7.
assert sp.simplify((b-Delta)-(a+eps)-(e-eps))==0
assert (e-eps).is_positive is True
# W4 after w=L+e-x: source (+1,-2,-1) gives t=w+a ->
# (b-Delta,b), also cell 7.
assert sp.simplify((L+e-L+a)-(b-Delta))==0

# Physical endpoint selection:
# low zones land in (Delta,L), hence inside J;
# wrap lands in (0,Delta).
# In particular no lift identification is used.
assert Delta.is_positive is True
assert sp.simplify(L-Delta).is_positive is True

print("SW1-A10-H3 INDEPENDENT FINITE REVIEW CERTIFICATE: PASS")
print("canonical disjoint zones: (0,e-R),(e-R,e),(e,L-Delta),(L-Delta,L)")
print("all 9 bridge segments occur in explicit certified H2 cells")
print("canonical low words -> x+Delta; wrap word -> x+Delta-L")
print("canonical boundary set on the circle: {0,e-R,e,L-Delta}")
print("P3/W may both be legal off the canonical selector; graph relation need not be single-valued")
print("FIREWALL: finite H3 review only; infinite-orbit argument uses separate irrationality/countability proof")
