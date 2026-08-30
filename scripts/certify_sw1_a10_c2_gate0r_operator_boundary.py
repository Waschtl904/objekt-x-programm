#!/usr/bin/env python3
"""SW1-A10-C2-GATE0R operator-oriented symmetric boundary certificate.

This supersedes the earlier C2-GATE0 wrap count, which used HUB0's
input->output displacement in a selector formula intended for the final
operator convention F(theta+j Delta). FREE0 was already operator-oriented;
the hub selector must use the inverse relation.

Results in the actual operator convention:
- all four-species images of the 19 physical A1 walls are old B92 walls;
- FREE input-wrap selectors give 18 pure-phase walls and add exactly
  eta*L/2+k*Delta with eta in {0,1}, k in {5,6};
- operator-oriented HUB input-wrap selectors give 14 walls and are a subset
  of the FREE selector walls;
- therefore the correct C2 matrix boundary alphabet is 92+4=96, not 100.

Firewall: boundary closure only. Parameter collision geometry is re-audited
separately in C2-GATE1R.
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

zero=V(); e=V(F(1,2),0); d=V(F(1,2),1); a=V(1,1); b=V(F(3,2),2); T=V(2,2); twod=V(1,2)
T0=add(T,V(E=1)); Sann=add(T,V(S=1))

Bf={
    zero,V(E=1),sub(a,V(E=1)),add(a,V(E=1)),sub(twod,V(E=1)),sub(T,V(E=1)),
    V(S=1),add(e,V(S=1)),add(a,V(S=1)),
    sub(a,V(R=1)),add(a,V(R=1)),sub(b,V(R=1)),add(b,V(R=1)),
    sub(T,V(R=1)),add(T,V(R=1)),a,b,T,T0,
}
Bw={
    V(R=1),V(E=1),add(e,V(E=1)),d,add(d,V(R=1)),a,add(a,V(R=1)),
    add(a,V(E=1)),b,sub(T,V(R=1)),T,Sann,
}
assert len(Bf)==19 and len(Bw)==12

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

G=[
    ("P0",+1,0,0,V()),
    ("P1",+1,1,0,V(L=F(1,2))),
    ("Q0",-1,0,4,V(D=4)),
    ("Q1",-1,1,4,V(L=F(1,2),D=4)),
]
Gdict={g[0]:g for g in G}

def preim(w,g):
    _,s,eta,kappa,c=g
    z=sub(w,c)
    if s==-1:
        z=neg(z)
    return modL(z)

# Physical output walls: 76 occurrences -> 46 unique, all old.
physical_occ=[preim(w,g) for w in Bf for g in G]
assert len(physical_occ)==76
assert len(set(physical_occ))==46
assert set(physical_occ)<=B92

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

def free_op(br,gout):
    name,s,lam,k=br
    _,so,etao,kapo,_=gout
    si=s*so
    etai=int(s*etao+2*lam)%2
    gin=next(g for g in G if g[1]==si and g[2]==etai)
    _,_,_,kapi,_=gin
    j=F(s*kapo+k-kapi,si)
    assert j.denominator==1
    return gin[0],int(j)

free_rules=[]
for br in FREE:
    for gout in G:
        gin,j=free_op(br,gout)
        free_rules.append((br[0],gout[0],gin,j))
assert len(free_rules)==40

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

def hub_op(ch,gout):
    name,s,lam,k=ch
    # source t=s*x-s*lam L-s*k Delta
    lamsrc=-s*lam
    ksrc=-s*k
    _,so,etao,kapo,_=gout
    si=s*so
    etai=int(s*etao+2*lamsrc)%2
    gin=next(g for g in G if g[1]==si and g[2]==etai)
    _,_,_,kapi,_=gin
    j=F(s*kapo+ksrc-kapi,si)
    assert j.denominator==1
    return gin[0],int(j)

hub_rules=[]
for ch in HUB:
    for gout in G:
        gin,j=hub_op(ch,gout)
        hub_rules.append((ch[0],gout[0],gin,j))
assert len(hub_rules)==36

def wrap_wall(gin_name,j):
    g=Gdict[gin_name]
    _,s,eta,kappa,_=g
    # phi_g(theta+jD)=0 mod L:
    # theta = -jD - s*eta*L/2 - s*kappa*D mod L.
    return modL(V(L=-F(s*eta,2),D=-(j+s*kappa)))

Hwrap={wrap_wall(gin,j) for _,gout,gin,j in free_rules}
Wwrap={wrap_wall(gin,j) for _,gout,gin,j in hub_rules}
assert len(Hwrap)==18
assert len(Wwrap)==14
assert Wwrap<=Hwrap

NEW={
    V(D=5),V(L=F(1,2),D=5),
    V(D=6),V(L=F(1,2),D=6),
}
assert Hwrap-B92==NEW
assert Wwrap-B92==NEW

B96=B92|Hwrap|Wwrap
assert len(B96)==96
assert B96-B92==NEW

print("SW1-A10-C2-GATE0R OPERATOR-ORIENTED BOUNDARY CERTIFICATE: PASS")
print("physical wall images: 76 labeled occurrences -> 46 unique, all contained in B92")
print("FREE operator input-wrap selector walls: 18")
print("HUB operator input-wrap selector walls: 14, all contained in FREE selector set")
print("new matrix-selector walls are exactly eta*L/2+k*Delta for eta in {0,1}, k in {5,6}")
print("correct operator-oriented C2 boundary alphabet: 92 -> 96")
print("SUPERSEDES: earlier 92->100 count used HUB0 input->output displacement in an operator selector")
print("FIREWALL: boundary closure only; collision geometry belongs to C2-GATE1R")
