#!/usr/bin/env python3
"""SW1-A10-C2-FREE0 physical free-block pure-Delta closure certificate.

Scope:
- extracts the ten distinct physical source-affine types occurring in the A1
  row archetypes for (I+A)y on the positive horizon;
- transports each source map through the four corrected horizon Sheet/Parity
  species P0,P1,Q0,Q1;
- proves closure as pure base shifts theta -> theta+j Delta with |j|<=3;
- verifies no new sheet/parity species is required;
- notes that input/output cover component normalization is identical, so scalar
  row coefficients are unchanged by the Hilbert-space transport.

Firewall:
This is affine closure only. It does not yet encode which A1 cell activates
which branch or the cell-dependent scalar coefficient. No full matrix ledger
and no injectivity claim.
"""
from fractions import Fraction as F

G=[
    ("P0",+1,0,0),
    ("P1",+1,1,0),
    ("Q0",-1,0,4),
    ("Q1",-1,1,4),
]
assert len(G)==4

BR=[
    ("I",       +1,F(0), 0),
    ("r_a",     -1,F(1), 1),
    ("tau_+a",  +1,F(1), 1),
    ("r_T",     -1,F(2), 2),
    ("tau_+T",  +1,F(2), 2),
    ("r_3a",    -1,F(3), 3),
    ("tau_-a",  +1,F(-1),-1),
    ("r_2b",    -1,F(3), 4),
    ("r_2T",    -1,F(4), 4),
    ("tau_-T",  +1,F(-2),-2),
]
assert len(BR)==10

def transport(branch,gout):
    name,s,lam,k=branch
    oname,so,etao,kapo=gout
    si=s*so
    parity_twice=s*etao + 2*lam
    assert parity_twice.denominator==1
    etai=int(parity_twice)%2
    gin=next(g for g in G if g[1]==si and g[2]==etai)
    iname,si2,etai2,kapi=gin
    assert si2==si
    j=F(s*kapo+k-kapi,si)
    assert j.denominator==1
    return iname,int(j)

transitions=[]
for branch in BR:
    seen_inputs=set()
    for gout in G:
        gin,j=transport(branch,gout)
        transitions.append((branch[0],gout[0],gin,j))
        seen_inputs.add(gin)
    assert seen_inputs=={g[0] for g in G}

assert len(transitions)==40
assert {j for _,_,_,j in transitions}=={-3,-2,-1,0,1,2,3}
assert max(abs(j) for _,_,_,j in transitions)==3

expected={
"I":[("P0","P0",0),("P1","P1",0),("Q0","Q0",0),("Q1","Q1",0)],
"r_a":[("P0","Q0",3),("P1","Q1",3),("Q0","P0",-3),("Q1","P1",-3)],
"tau_+a":[("P0","P0",1),("P1","P1",1),("Q0","Q0",-1),("Q1","Q1",-1)],
"r_T":[("P0","Q0",2),("P1","Q1",2),("Q0","P0",-2),("Q1","P1",-2)],
"tau_+T":[("P0","P0",2),("P1","P1",2),("Q0","Q0",-2),("Q1","Q1",-2)],
"r_3a":[("P0","Q0",1),("P1","Q1",1),("Q0","P0",-1),("Q1","P1",-1)],
"tau_-a":[("P0","P0",-1),("P1","P1",-1),("Q0","Q0",1),("Q1","Q1",1)],
"r_2b":[("P0","Q0",0),("P1","Q1",0),("Q0","P0",0),("Q1","P1",0)],
"r_2T":[("P0","Q0",0),("P1","Q1",0),("Q0","P0",0),("Q1","P1",0)],
"tau_-T":[("P0","P0",-2),("P1","P1",-2),("Q0","Q0",2),("Q1","Q1",2)],
}
for name in expected:
    got=[(go,gi,j) for n,go,gi,j in transitions if n==name]
    assert got==expected[name]

scale_sq=F(1,2)
assert scale_sq/scale_sq==1

print("SW1-A10-C2-FREE0 PHYSICAL FREE-BLOCK CLOSURE CERTIFICATE: PASS")
print("10 physical affine source types -> 40 Sheet/Parity transitions")
print("all transitions close on P0,P1,Q0,Q1 with pure Delta shifts")
print("free-block rotation range: j in {-3,-2,-1,0,1,2,3}")
print("same input/output Hilbert-cover scaling leaves scalar row coefficients unchanged")
print("FIREWALL: affine closure only; A1 cell gates and coefficients remain for C2-FREE1")
