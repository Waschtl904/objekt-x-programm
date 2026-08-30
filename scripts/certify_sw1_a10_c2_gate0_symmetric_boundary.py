#!/usr/bin/env python3
"""SW1-A10-C2-GATE0 symmetric-cover boundary-closure certificate.

Reconstructs the certified C1B0 92-boundary alphabet, then audits every new
boundary source introduced by the symmetric 12_H+12_W pure-Delta cover.

Key separation:
- physical A1 row/support gates transformed through all four output
  Sheet/Parity species are already contained in the old 92 alphabet;
- physical source-domain endpoint gates need no independent coefficient wall:
  A1/HUB0-COMP already encode them as output branch activation walls, while
  invalid cover input slots vanish on the closed image subspace;
- the only genuinely new coefficient-selector walls are canonical-residue
  wrap switches needed to select the correct input lift after theta -> theta+jDelta.

Result: exactly eight new pure-phase walls, so 92 -> 100.

Firewall: boundary alphabet only. Collision/order stratification of the enlarged
100-wall alphabet is NOT certified here.
"""
from fractions import Fraction as F
from itertools import combinations

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
d=V(F(1,2),1)
a=V(1,1)
b=V(F(3,2),2)
T=V(2,2)
twod=V(1,2)
T0=add(T,V(E=1))
Sann=add(T,V(S=1))

# ------------------------------------------------------------------
# Rebuild the exact C1B0 92-boundary alphabet.
# ------------------------------------------------------------------
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

Bw={
 V(R=1),V(E=1),add(e,V(E=1)),d,add(d,V(R=1)),
 a,add(a,V(R=1)),add(a,V(E=1)),
 b,sub(T,V(R=1)),T,Sann,
}
assert len(Bw)==12

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

assert len(Braw)==195
B92={modL(x) for x in Braw}
assert len(B92)==92

# ------------------------------------------------------------------
# Four Sheet/Parity species and preimage helper.
# phi_g(theta)=s theta + c_g mod L.
# ------------------------------------------------------------------
G=[
    ("P0",+1,V()),
    ("P1",+1,V(L=F(1,2))),
    ("Q0",-1,V(D=4)),
    ("Q1",-1,V(L=F(1,2),D=4)),
]
Gdict={x[0]:x for x in G}

def preim(w,g):
    _,s,c=g
    z=sub(w,c)
    if s==-1:
        z=neg(z)
    return modL(z)

def shift_minus_jD(w,j):
    return modL(sub(w,V(D=j)))

# Every physical output row/support wall under every species is old.
out_physical={preim(w,g) for w in Bf for g in G}
assert len(out_physical)==46
assert out_physical <= B92

# The nine direct physical hub support walls are a subset of Bf.
hub_support={
 V(S=1),add(e,V(S=1)),add(a,V(S=1)),
 sub(a,V(R=1)),add(a,V(R=1)),
 sub(b,V(R=1)),add(b,V(R=1)),
 sub(T,V(R=1)),add(T,V(R=1)),
}
assert hub_support <= Bf
assert {preim(w,g) for w in hub_support for g in G} <= B92

# ------------------------------------------------------------------
# Rebuild C2-HUB0 and C2-FREE0 species/rotation transitions.
# Only canonical-residue input-wrap switches can create new selector walls.
# ------------------------------------------------------------------
Gsimple=[
    ("P0",+1,0,0),
    ("P1",+1,1,0),
    ("Q0",-1,0,4),
    ("Q1",-1,1,4),
]

HUB=[
    ("A_L",-1,F(1),1),
    ("A_R",+1,F(1),1),
    ("A_O",+1,F(-1),-1),
    ("B_L",-1,F(3,2),2),
    ("B_R",+1,F(3,2),2),
    ("B_O",+1,F(-3,2),-2),
    ("T_L",-1,F(2),2),
    ("T_R",+1,F(2),2),
    ("T_O",+1,F(-2),-2),
]

def hub_transport(ch,gin):
    name,s,lam,k=ch
    iname,si,etai,kapi=gin
    so=s*si
    parity_twice=s*etai+2*lam
    etaout=int(parity_twice)%2
    gout=next(g for g in Gsimple if g[1]==so and g[2]==etaout)
    j=F(s*kapi+k-gout[3],so)
    assert j.denominator==1
    return gout[0],int(j)

hubtrans=[]
for ch in HUB:
    for gin in Gsimple:
        gout,j=hub_transport(ch,gin)
        hubtrans.append((ch[0],gin[0],gout,j))
assert len(hubtrans)==36

FREE=[
    ("I",+1,F(0),0),
    ("r_a",-1,F(1),1),
    ("tau_+a",+1,F(1),1),
    ("r_T",-1,F(2),2),
    ("tau_+T",+1,F(2),2),
    ("r_3a",-1,F(3),3),
    ("tau_-a",+1,F(-1),-1),
    ("r_2b",-1,F(3),4),
    ("r_2T",-1,F(4),4),
    ("tau_-T",+1,F(-2),-2),
]

def free_transport(br,gout):
    name,s,lam,k=br
    oname,so,etao,kapo=gout
    si=s*so
    parity_twice=s*etao+2*lam
    etai=int(parity_twice)%2
    gin=next(g for g in Gsimple if g[1]==si and g[2]==etai)
    j=F(s*kapo+k-gin[3],si)
    assert j.denominator==1
    return gin[0],int(j)

freetrans=[]
for br in FREE:
    for gout in Gsimple:
        gin,j=free_transport(br,gout)
        freetrans.append((br[0],gout[0],gin,j))
assert len(freetrans)==40

# Canonical-residue wrap of an input species occurs at phi_g(theta+jD)=0 mod L.
Hwrap={
    shift_minus_jD(preim(zero,Gdict[gin]),j)
    for _,gout,gin,j in freetrans
}
Wwrap={
    shift_minus_jD(preim(zero,Gdict[gin]),j)
    for _,gin,gout,j in hubtrans
}
assert len(Hwrap)==18
assert len(Wwrap)==18

newH=Hwrap-B92
newW=Wwrap-B92
assert len(newH)==4
assert len(newW)==8
assert newH <= newW

NEW={
    V(D=-3),V(L=F(1,2),D=-3),
    V(D=5), V(L=F(1,2),D=5),
    V(D=6), V(L=F(1,2),D=6),
    V(D=7), V(L=F(1,2),D=7),
}
assert newW==NEW

B100=B92|Hwrap|Wwrap
assert len(B100)==100
assert B100-B92==NEW

# The old pure-phase portion was exactly eta=0,1 and k=-2..4.
pure_old={x for x in B92 if x[2:]==(F(0),F(0),F(0))}
assert pure_old=={
    V(L=eta,D=k)
    for eta in (F(0),F(1,2))
    for k in range(-2,5)
}
assert len(pure_old)==14

print("SW1-A10-C2-GATE0 SYMMETRIC-COVER BOUNDARY CERTIFICATE: PASS")
print("old C1B0 circle-boundary alphabet: 92")
print("all 46 four-species images of the 19 physical A1 walls are already in the old 92")
print("free-input canonical-wrap selectors add 4 new walls; hub-input selectors add 8, with the former contained in the latter")
print("new walls are exactly eta*L/2+k*Delta with eta in {0,1}, k in {-3,5,6,7}")
print("enlarged C2 gate alphabet: 100")
print("IMPORTANT: C1B1/B2 collision/order stratification is not automatically valid for the enlarged 100-wall alphabet")
print("FIREWALL: boundary closure only; next step must reclassify collisions/order for the 8 added walls")
