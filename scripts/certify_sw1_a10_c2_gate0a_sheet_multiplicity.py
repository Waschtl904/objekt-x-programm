#!/usr/bin/env python3
"""SW1-A10-C2-GATE0A physical-sheet image multiplicity certificate.

Audits the 19 physical A1 boundary walls under the four Sheet/Parity pullbacks
P0,P1,Q0,Q1. There are 19*4=76 labeled occurrences before deduplication.

Result:
- exactly 46 distinct circle images;
- multiplicity distribution among those 46 images:
  32 singleton, 4 double, 4 triple, 6 quadruple;
- hence duplicate excess is exactly 76-46=30.

Firewall: this is only the internal multiplicity ledger for the physical
Sheet/Parity images. Containment in B92 is certified separately by C2-GATE0.
"""
from fractions import Fraction as F
from collections import Counter, defaultdict

def V(L=0,D=0,R=0,E=0,S=0):
    return (F(L),F(D),F(R),F(E),F(S))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def floorf(q): return q.numerator//q.denominator
def modL(x):
    n=F(floorf(x[0]))
    return (x[0]-n,)+x[1:]

zero=V()
e=V(F(1,2),0)
a=V(1,1)
b=V(F(3,2),2)
T=V(2,2)
twod=V(1,2)
T0=add(T,V(E=1))

Bf={
    zero,
    V(E=1),
    sub(a,V(E=1)), add(a,V(E=1)), sub(twod,V(E=1)), sub(T,V(E=1)),
    V(S=1), add(e,V(S=1)), add(a,V(S=1)),
    sub(a,V(R=1)), add(a,V(R=1)),
    sub(b,V(R=1)), add(b,V(R=1)),
    sub(T,V(R=1)), add(T,V(R=1)),
    a,b,T,T0,
}
assert len(Bf)==19

G=[
    ("P0",+1,V()),
    ("P1",+1,V(L=F(1,2))),
    ("Q0",-1,V(D=4)),
    ("Q1",-1,V(L=F(1,2),D=4)),
]
assert len(G)==4

def preim(w,g):
    _,s,c=g
    z=sub(w,c)
    if s==-1:
        z=neg(z)
    return modL(z)

occurrences=[(w,g[0],preim(w,g)) for w in sorted(Bf) for g in G]
assert len(occurrences)==19*4==76

groups=defaultdict(list)
for w,g,img in occurrences:
    groups[img].append((w,g))

assert len(groups)==46

mult=Counter(len(v) for v in groups.values())
assert mult==Counter({1:32,2:4,3:4,4:6})
assert sum(m*n for m,n in mult.items())==76
assert sum((m-1)*n for m,n in mult.items())==30
assert max(mult)==4

print("SW1-A10-C2-GATE0A PHYSICAL-SHEET IMAGE MULTIPLICITY CERTIFICATE: PASS")
print("raw labeled occurrences: 19*4 = 76")
print("distinct circle images after exact symbolic mod-L deduplication: 46")
print("image multiplicities: 32x1, 4x2, 4x3, 6x4")
print("duplicate excess: 30")
print("FIREWALL: multiplicity ledger only; B92 containment remains C2-GATE0")
