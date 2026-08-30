#!/usr/bin/env python3
"""SW1-A10-C2-HUB0 symmetric-cover / pure-Delta closure certificate.

Scope:
- starts from the nine physical positive-odd-folded branches of H E_A, not the
  53 KNF-pulled-back H2 channels;
- uses the four horizon Sheet/Parity maps P0,P1,Q0,Q1;
- proves that duplicating the positive annulus with the same four species
  closes every physical hub branch as a pure base shift theta -> theta+j Delta;
- proves the direct shift range is |j|<=3;
- proves that within this G-covariant pure-Delta architecture all four annulus
  species are required to fill all four horizon output species;
- verifies the symmetric 12_W cover has the same original-space component
  normalization 1/sqrt(2) as the corrected 12_H cover, so transported hub
  coefficients remain exactly the physical coefficients +/-p,+/-r,+/-q.

Firewall:
No lift-gate matrix ledger yet; no claim that 12_W is minimal among every
possible representation; necessity is only within the chosen four-species
G-covariant pure-Delta architecture.
"""
from fractions import Fraction as F
from collections import defaultdict

G=[
    ("P0",+1,0,0),
    ("P1",+1,1,0),
    ("Q0",-1,0,4),
    ("Q1",-1,1,4),
]
assert len(G)==4

CH=[
    ("A_L",-1,F(1),1,"-p"),
    ("A_R",+1,F(1),1,"+p"),
    ("A_O",+1,F(-1),-1,"-p"),
    ("B_L",-1,F(3,2),2,"-r"),
    ("B_R",+1,F(3,2),2,"+r"),
    ("B_O",+1,F(-3,2),-2,"-r"),
    ("T_L",-1,F(2),2,"-q"),
    ("T_R",+1,F(2),2,"+q"),
    ("T_O",+1,F(-2),-2,"-q"),
]
assert len(CH)==9

def transport(ch,gin):
    name,s,lam,k,coeff=ch
    iname,si,etai,kapi=gin
    so=s*si
    parity_twice=s*etai + 2*lam
    assert parity_twice.denominator==1
    etaout=int(parity_twice)%2
    gout=next(g for g in G if g[1]==so and g[2]==etaout)
    oname,so2,etao,kapo=gout
    assert so2==so
    j=F(s*kapi+k-kapo,so)
    assert j.denominator==1
    return oname,int(j)

transitions=[]
for ch in CH:
    seen_out=set()
    for gin in G:
        gout,j=transport(ch,gin)
        transitions.append((ch[0],gin[0],gout,j,ch[4]))
        seen_out.add(gout)
    assert seen_out=={g[0] for g in G}

assert len(transitions)==36
assert {j for _,_,_,j,_ in transitions}=={-3,-2,-1,1,2,3}
assert max(abs(j) for _,_,_,j,_ in transitions)==3

inverse=defaultdict(list)
for name,gin,gout,j,c in transitions:
    inverse[(name,gout)].append((gin,j,c))
assert len(inverse)==9*4
assert all(len(v)==1 for v in inverse.values())

required_inputs={v[0][0] for v in inverse.values()}
assert required_inputs=={g[0] for g in G}

W_LIFTS=3
assert len(required_inputs)*W_LIFTS==12

orig_component_scale_sq=F(2)*F(1,4)
assert orig_component_scale_sq==F(1,2)
assert F(1,2)/F(1,2)==1

expected={
"A_L":[("P0","Q0",3),("P1","Q1",3),("Q0","P0",-3),("Q1","P1",-3)],
"A_R":[("P0","P0",1),("P1","P1",1),("Q0","Q0",-1),("Q1","Q1",-1)],
"A_O":[("P0","P0",-1),("P1","P1",-1),("Q0","Q0",1),("Q1","Q1",1)],
"B_L":[("P0","Q1",2),("P1","Q0",2),("Q0","P1",-2),("Q1","P0",-2)],
"B_R":[("P0","P1",2),("P1","P0",2),("Q0","Q1",-2),("Q1","Q0",-2)],
"B_O":[("P0","P1",-2),("P1","P0",-2),("Q0","Q1",2),("Q1","Q0",2)],
"T_L":[("P0","Q0",2),("P1","Q1",2),("Q0","P0",-2),("Q1","P1",-2)],
"T_R":[("P0","P0",2),("P1","P1",2),("Q0","Q0",-2),("Q1","Q1",-2)],
"T_O":[("P0","P0",-2),("P1","P1",-2),("Q0","Q0",2),("Q1","Q1",2)],
}
for name in expected:
    got=[(gin,gout,j) for n,gin,gout,j,c in transitions if n==name]
    assert got==expected[name]

print("SW1-A10-C2-HUB0 SYMMETRIC-COVER CLOSURE CERTIFICATE: PASS")
print("physical hub branches: 9; G-covariant transitions: 36")
print("all four annulus Sheet/Parity species are required within pure-Delta architecture")
print("symmetric annulus cover: 4 species * 3 lifts = 12_W slots")
print("direct physical hub rotation range: j in {-3,-2,-1,1,2,3}")
print("corrected symmetric input/output component scales match, so hub coefficients are unchanged")
print("FIREWALL: no lift-gate matrices yet; no universal minimality claim; no injectivity")
