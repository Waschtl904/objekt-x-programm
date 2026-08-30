#!/usr/bin/env python3
"""SW1-A10-C2-GATE1 enlarged 100-wall collision-hyperplane certificate.

Starting from the certified C1B0 92-wall set plus the eight C2-GATE0 pure
wrap walls, this certificate proves that the parameter collision geometry in
the normalized project interval 3<r=s*/chi<4 does NOT acquire any new
hyperplanes.

All calculations use exact Fraction arithmetic after
  Delta/chi = 1+2r, L/chi = 4+10r, epsilon_*/chi=(r+1)/2.

Results:
- 100 choose 2 = 4950 pairs -> 527 raw difference signatures;
- |q|>=4 is uniformly impossible in 3<r<4;
- after that exact wrap cutoff there are 2659 canonical equations at r0=7/2:
  18 strict-interior, 18 closure-only, 2623 outside;
- the strict and closure sets are exactly the old 92-wall sets;
- no non-identical simplex-vertex touch ratio lies in (3,4), so this
  classification is constant throughout the whole project interval;
- hence the 18-hyperplane / 64-open-chamber parameter arrangement is unchanged.

Firewall: label-pair multiplicities/collision-class sizes on the hyperplanes
are not recomputed here; only the parameter hyperplane arrangement is certified.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter

def V(L=0,D=0,R=0,E=0,S=0):
    return (F(L),F(D),F(R),F(E),F(S))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def floorf(q): return q.numerator//q.denominator
def modL(x):
    n=F(floorf(x[0]))
    return (x[0]-n,)+x[1:]
def canon(eq):
    for z in eq:
        if z:
            return tuple(-x for x in eq) if z<0 else eq
    return eq

zero=V(); e=V(F(1,2),0); d=V(F(1,2),1); a=V(1,1); b=V(F(3,2),2); T=V(2,2); twod=V(1,2)
T0=add(T,V(E=1)); Sann=add(T,V(S=1))
Bf={zero,V(E=1),sub(a,V(E=1)),add(a,V(E=1)),sub(twod,V(E=1)),sub(T,V(E=1)),
    V(S=1),add(e,V(S=1)),add(a,V(S=1)),sub(a,V(R=1)),add(a,V(R=1)),
    sub(b,V(R=1)),add(b,V(R=1)),sub(T,V(R=1)),add(T,V(R=1)),a,b,T,T0}
Bw={V(R=1),V(E=1),add(e,V(E=1)),d,add(d,V(R=1)),a,add(a,V(R=1)),add(a,V(E=1)),
    b,sub(T,V(R=1)),T,Sann}

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
sig={q for cell in C for q in cell}
def rel(x,y):
    s,l,k=x; t,m,j=y
    if s==t:
        lam=F(m-l,2); dk=j-k
        if lam<0 or (lam==0 and dk<0):
            lam=-lam; dk=-dk
        return ("T",lam,dk)
    return ("R",F(l+m,2),k+j)
master={rel(x,y) for cell in C for x,y in combinations(cell,2)}
def cv(lam,k): return V(L=lam,D=k)

Braw=set(Bf|Bw)
for typ,lam,k in master:
    cc0=cv(lam,k)
    if typ=="T":
        for dr in (-1,1):
            cc=tuple(dr*z for z in cc0)
            for wall in Bf: Braw.add(sub(wall,cc))
    else:
        for wall in Bf: Braw.add(sub(cc0,wall))
for orient,twolam,k in sig:
    cc=cv(F(twolam,2),k)
    for wall in Bf:
        z=sub(wall,cc)
        if orient==-1: z=neg(z)
        Braw.add(z)

B92={modL(x) for x in Braw}
assert len(B92)==92
NEW={
    V(D=-3),V(L=F(1,2),D=-3),
    V(D=5),V(L=F(1,2),D=5),
    V(D=6),V(L=F(1,2),D=6),
    V(D=7),V(L=F(1,2),D=7),
}
B100=B92|NEW
assert len(B100)==100

raw92={sub(x,y) for x,y in combinations(sorted(B92),2)}
raw100={sub(x,y) for x,y in combinations(sorted(B100),2)}
assert len(raw92)==463
assert len(raw100)==527
assert 100*99//2==4950

# Uniform wrap cutoff on 3<r<4 after scaling chi=1:
# L=4+10r>34, Delta=1+2r<9, epsilon_*=(r+1)/2<5/2.
# For B100 differences: |k|<=10 and |rho|,|mu|,|nu|<=2.
# Thus |k Delta + parameter term| < 10*9+6*(5/2)=105.
# If |q|>=4, |q|L>136, impossible.
assert 4*34 > 10*9 + 6*F(5,2)

def equations(raw):
    out=set()
    for dL,dD,dR,dE,dS in raw:
        for n in range(-4,5):
            q=dL-F(n)
            if abs(q)>=4:
                continue
            out.add(canon((q,dD,dR,dE,dS)))
    return out

E92=equations(raw92)
E100=equations(raw100)
assert len(E100)==2659

r0=F(7,2)

def status(eq,r):
    q,k,rho,mu,nu=eq
    Lr=4+10*r
    Dr=1+2*r
    Emax=(r+1)/2
    target=-(q*Lr+k*Dr)
    vals=[F(0),mu,rho+mu,rho+mu+nu]
    lo=min(vals)*Emax
    hi=max(vals)*Emax
    if lo < target < hi:
        return "strict"
    if lo <= target <= hi:
        return "closure"
    return "outside"

S92={e for e in E92 if status(e,r0)=="strict"}
C92={e for e in E92 if status(e,r0)=="closure"}
S100={e for e in E100 if status(e,r0)=="strict"}
C100={e for e in E100 if status(e,r0)=="closure"}
counts=Counter(status(e,r0) for e in E100)

assert len(S92)==18 and len(C92)==18
assert counts==Counter({"outside":2623,"strict":18,"closure":18})
assert S100==S92
assert C100==C92

# A change of closed-simplex status requires target to equal one of the four
# simplex-vertex values. Every non-identical such equality has a rational root.
critical=set()
identical=0
for eq in E100:
    q,k,rho,mu,nu=eq
    A=4*q+k
    B=10*q+2*k
    for c in {F(0),mu,rho+mu,rho+mu+nu}:
        # -(A+B r)=c(r+1)/2
        aa=-A-c/F(2)
        bb=-B-c/F(2)
        if aa==0 and bb==0:
            identical+=1
            continue
        if bb!=0:
            root=-aa/bb
            if F(3)<root<F(4):
                critical.add(root)

assert critical==set()
assert identical==18

print("SW1-A10-C2-GATE1 100-WALL COLLISION-HYPERPLANE CERTIFICATE: PASS")
print("100 boundary labels -> 4950 pairs -> 527 raw differences")
print("uniform exact bound excludes |q|>=4 throughout 3<r<4")
print("after cutoff: 2659 canonical equations at r0=7/2 = 18 strict + 18 closure-only + 2623 outside")
print("strict-interior collision set is exactly unchanged from the old 92-wall alphabet")
print("closure-only collision set is exactly unchanged from the old 92-wall alphabet")
print("no non-identical simplex-vertex critical r lies in (3,4)")
print("therefore the parameter arrangement remains the same 18 hyperplanes and 64 open chambers")
print("FIREWALL: 100-label collision-class multiplicities on hyperplanes/randstrata remain to be recomputed")
