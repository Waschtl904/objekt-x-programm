#!/usr/bin/env python3
"""SW1-A10-C1B common boundary-alphabet certificate.

Builds an over-refined but exhaustive symbolic boundary alphabet for a common
circle partition on which all currently known A7/A9 free gates and H2 annulus
incidences can be made simultaneously constant.

Inputs:
- 19 free-coordinate/gate walls from A0/A1/A7/A9;
- 12 H2 annulus t-cell walls;
- the complete 22-type H2 master affine alphabet (which contains A7+A9);
- the 19 distinct H2 affine channel signatures.

For every free boundary we include its preimages under every directed master
translation/reflection and under every H2 channel map. After reduction modulo L
there are 92 distinct symbolic boundary signatures.

Firewall: this certifies finite boundary-alphabet closure only. It does not
order those 92 forms for all parameter values, resolve coincidences, determine
atoms, or determine the final physical fiber dimension N.
"""
from fractions import Fraction as F
from itertools import combinations

def V(L=0,D=0,R=0,E=0,S=0):
    return (F(L),F(D),F(R),F(E),F(S))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)

zero=V()
e=V(F(1,2),0)
d=V(F(1,2),1)
a=V(1,1)
b=V(F(3,2),2)
T=V(2,2)
twod=V(1,2)

Bf={
 zero,
 V(E=1),
 sub(a,V(E=1)), add(a,V(E=1)), sub(twod,V(E=1)), sub(T,V(E=1)),
 V(S=1), add(e,V(S=1)), add(a,V(S=1)),
 sub(a,V(R=1)), add(a,V(R=1)),
 sub(b,V(R=1)), add(b,V(R=1)),
 sub(T,V(R=1)), add(T,V(R=1)),
 a,b,T,add(T,V(E=1)),
}
assert len(Bf)==19

Bw={
 V(R=1),V(E=1),add(e,V(E=1)),d,add(d,V(R=1)),
 a,add(a,V(R=1)),add(a,V(E=1)),
 b,sub(T,V(R=1)),T,add(T,V(S=1)),
}
assert len(Bw)==12
assert len(Bf|Bw)==24

C=[
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1),(1,3,2),(1,4,2)],
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1),(1,3,2)],
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1)],
[(-1,2,1),(-1,4,2),(-1,4,3),(-1,5,3),(1,1,0),(1,2,1),(1,3,1)],
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1)],
[(-1,3,2),(-1,5,3),(-1,6,3),(1,-2,-1),(1,0,0),(1,1,1),(1,2,1)],
[(-1,3,2),(-1,4,2),(1,-2,-1),(1,2,1)],
[(-1,3,2),(-1,4,2),(1,-2,-1)],
[(-1,4,2),(1,-3,-2),(1,-2,-1)],
[(-1,4,2),(-1,6,3),(-1,7,4),(-1,8,4),(1,-3,-2),(1,-1,0),(1,0,0)],
[(1,-4,-2),(1,-3,-2),(1,-2,-1)]]
sig=set(q for cell in C for q in cell)
assert len(sig)==19

def rel(x,y):
    s,l,k=x; t,m,j=y
    if s==t:
        lam=F(m-l,2); dk=j-k
        if lam<0 or (lam==0 and dk<0):
            lam=-lam; dk=-dk
        return ("T",lam,dk)
    return ("R",F(l+m,2),k+j)

master={rel(x,y) for cell in C for x,y in combinations(cell,2)}
assert len(master)==22

def cv(lam,k): return V(L=lam,D=k)

Braw=set(Bf|Bw)

for typ,lam,k in master:
    c=cv(lam,k)
    if typ=="T":
        for direction in (-1,1):
            cc=tuple(direction*z for z in c)
            for wall in Bf:
                Braw.add(sub(wall,cc))
    else:
        for wall in Bf:
            Braw.add(sub(c,wall))

for s,twolam,k in sig:
    c=cv(F(twolam,2),k)
    for wall in Bf:
        z=sub(wall,c)
        if s==-1:
            z=neg(z)
        Braw.add(z)

assert len(Braw)==195

def floor_fraction(q):
    return q.numerator//q.denominator

def modL(x):
    n=F(floor_fraction(x[0]))
    return (x[0]-n,)+x[1:]

Bmod={modL(x) for x in Braw}
assert len(Bmod)==92

assert {x[0] for x in Bmod}=={F(0),F(1,2)}
assert max(abs(x[1]) for x in Bmod)==4
assert max(abs(x[2]) for x in Bmod)==1
assert max(abs(x[3]) for x in Bmod)==1
assert max(abs(x[4]) for x in Bmod)==1

print("SW1-A10-C1B COMMON BOUNDARY-ALPHABET CERTIFICATE: PASS")
print("free/source walls: 19; H2 t-cell walls: 12; direct union: 24")
print("master affine types: 22; H2 channel signatures: 19")
print("unique symbolic pullback walls before mod L: 195")
print("unique symbolic circle-boundary signatures mod L: 92")
print("every boundary has L-parity 0 or 1/2, |Delta coefficient|<=4")
print("R/epsilon/sigma coefficients are each in {-1,0,1}")
print("FIREWALL: finite boundary alphabet only; ordering/coincidences/atoms/final N remain open")
