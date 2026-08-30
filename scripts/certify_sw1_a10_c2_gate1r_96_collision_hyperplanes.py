#!/usr/bin/env python3
"""SW1-A10-C2-GATE1R collision geometry for the corrected 96-wall alphabet.

The final operator convention uses the corrected C2-GATE0R alphabet
B96=B92 plus four pure matrix-selector walls:
  eta*L/2+k*Delta, eta in {0,1}, k in {5,6}.

This certificate recomputes the parameter collision geometry exactly and proves:
- 96 choose 2 = 4560 pairs -> 503 raw difference signatures;
- the same uniform |q|>=4 cutoff applies on 3<r<4;
- after cutoff there are 2539 canonical equations at r0=7/2:
  18 strict + 18 closure-only + 2503 outside;
- the strict and closure sets are EXACTLY equal as sets to the old B92 sets;
- no non-identical simplex-vertex critical ratio lies in (3,4).

Therefore the corrected 96-wall matrix alphabet still has exactly the old
18-hyperplane / 64-open-chamber parameter arrangement.

Firewall: parameter hyperplanes only. 96-label pair multiplicities on
hyperplanes/randstrata are not recomputed here.
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
Bf={
    zero,V(E=1),sub(a,V(E=1)),add(a,V(E=1)),sub(twod,V(E=1)),sub(T,V(E=1)),
    V(S=1),add(e,V(S=1)),add(a,V(S=1)),sub(a,V(R=1)),add(a,V(R=1)),
    sub(b,V(R=1)),add(b,V(R=1)),sub(T,V(R=1)),add(T,V(R=1)),a,b,T,T0,
}
Bw={
    V(R=1),V(E=1),add(e,V(E=1)),d,add(d,V(R=1)),a,add(a,V(R=1)),
    add(a,V(E=1)),b,sub(T,V(R=1)),T,Sann,
}

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
            for wall in Bf:
                Braw.add(sub(wall,cc))
    else:
        for wall in Bf:
            Braw.add(sub(cc0,wall))
for orient,twolam,k in sig:
    cc=cv(F(twolam,2),k)
    for wall in Bf:
        z=sub(wall,cc)
        if orient==-1:
            z=neg(z)
        Braw.add(z)

B92={modL(x) for x in Braw}
assert len(B92)==92
NEW={
    V(D=5),V(L=F(1,2),D=5),
    V(D=6),V(L=F(1,2),D=6),
}
B96=B92|NEW
assert len(B96)==96

# Fixed-circle normalization for transfer across varying circumference L(r).
# Since L(r)=4+10r is positive on 3<r<4, division by L(r) identifies
# R/L(r)Z orientation-preservingly with the fixed circle R/Z.
def wall_lift(sig,r,s,R,e):
    l,k,rho,mu,nu=sig
    Lr=4+10*r
    Dr=1+2*r
    return l*Lr+k*Dr+rho*R+mu*e+nu*s

def wall_mod(sig,r,s,R,e):
    Lr=4+10*r
    z=wall_lift(sig,r,s,R,e)
    n=F(floorf(z/Lr))
    return z-n*Lr

def wall_norm(sig,r,s,R,e):
    Lr=4+10*r
    assert Lr > 0
    return wall_mod(sig,r,s,R,e)/Lr

# Exact endpoint/monotonicity certificate for L(r)>0 throughout (3,4).
assert 10 > 0 and 4+10*F(3) > 0 and 4+10*F(4) > 0

# Mechanical normalization check on a certified generic reference chamber point:
# theta/L in [0,1), injectivity is preserved, and the increasing order is identical.
probe_r=F(7,2)
probe_s,probe_R,probe_e=F(1,7),F(2,7),F(3,7)
probe_sigs=sorted(B96)
probe_mod_vals=[wall_mod(sig,probe_r,probe_s,probe_R,probe_e) for sig in probe_sigs]
probe_norm_vals=[wall_norm(sig,probe_r,probe_s,probe_R,probe_e) for sig in probe_sigs]
probe_L=4+10*probe_r
assert all(F(0) <= u < F(1) for u in probe_norm_vals)
assert all(probe_norm_vals[i]*probe_L == probe_mod_vals[i] for i in range(96))
assert len(set(probe_mod_vals)) == len(set(probe_norm_vals)) == 96
assert tuple(sorted(range(96),key=lambda i:probe_mod_vals[i])) == tuple(sorted(range(96),key=lambda i:probe_norm_vals[i]))

raw92={sub(x,y) for x,y in combinations(sorted(B92),2)}
raw96={sub(x,y) for x,y in combinations(sorted(B96),2)}
assert len(raw92)==463
assert len(raw96)==503
assert 96*95//2==4560

# Uniform exact cutoff, as in the previous larger-alphabet audit:
# L/chi>34, Delta/chi<9, eps_*/chi<5/2, |k|<=10,
# |rho|,|mu|,|nu|<=2.
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
E96=equations(raw96)
assert len(E96)==2539

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

S92={eq for eq in E92 if status(eq,r0)=="strict"}
C92={eq for eq in E92 if status(eq,r0)=="closure"}
S96={eq for eq in E96 if status(eq,r0)=="strict"}
C96={eq for eq in E96 if status(eq,r0)=="closure"}
counts=Counter(status(eq,r0) for eq in E96)

assert len(S92)==18 and len(C92)==18
assert counts==Counter({"outside":2503,"strict":18,"closure":18})

# Strong set identity, not merely equal cardinality.
assert S96==S92
assert C96==C92
assert S96-S92==set() and S92-S96==set()
assert C96-C92==set() and C92-C96==set()

critical=set()
identical=0
for eq in E96:
    q,k,rho,mu,nu=eq
    A=4*q+k
    B=10*q+2*k
    for c in {F(0),mu,rho+mu,rho+mu+nu}:
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

print("SW1-A10-C2-GATE1R 96-WALL COLLISION-HYPERPLANE CERTIFICATE: PASS")
print("96 boundary labels -> 4560 pairs -> 503 raw differences")
print("fixed-circle normalization theta/L(r) -> R/Z: PASS; L(r)>0 on 3<r<4")
print("reference normalization preserves all 96 labels and their increasing/cyclic order")
print("after exact |q|<4 cutoff: 2539 canonical equations = 18 strict + 18 closure + 2503 outside")
print("STRONG IDENTITY: S96 == S92 as sets of canonical equations")
print("STRONG IDENTITY: C96 == C92 as sets of canonical equations")
print("no non-identical simplex-vertex critical r lies in (3,4)")
print("parameter arrangement remains the same 18 hyperplanes / 64 open chambers")
print("SUPERSEDES: earlier 100-wall collision audit for the non-operator-oriented selector alphabet")
print("FIREWALL: parameter geometry only; 96-label hyperplane multiplicities remain separate")
