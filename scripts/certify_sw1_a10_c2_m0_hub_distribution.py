#!/usr/bin/env python3
"""SW1-A10-C2-M0-HUB-DIST direct physical branch-shift distribution certificate.

Purpose:
Verify that the operator-oriented species count
  j=-3:2, -2:12, -1:4, +1:4, +2:12, +3:2
comes directly from the nine physical H E_A branches after solving for the
input variable, not from a relabeling artifact.

Branch-level result:
- A_L alone gives |j|=3: two +3 and two -3;
- A_R and A_O give |j|=1: together four +1 and four -1;
- all six B/T branches give |j|=2: together twelve +2 and twelve -2.

Thus the distribution is sign-symmetric; it is only non-uniform across
the magnitudes |j|=1,2,3.

Firewall: species/shift multiplicities only; lift selectors and matrices are
handled separately.
"""
from fractions import Fraction as F
from collections import Counter

G=[
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

def op_shift(ch,gout):
    name,s,lam,k=ch
    # physical input variable:
    # t = s*x - s*lam*L - s*k*Delta
    lamsrc=-s*lam
    ksrc=-s*k

    _,so,etao,kapo=gout
    si=s*so
    etai=int(s*etao+2*lamsrc)%2
    gin=next(g for g in G if g[1]==si and g[2]==etai)
    _,_,_,kapi=gin
    j=F(s*kapo+ksrc-kapi,si)
    assert j.denominator==1
    return int(j)

per_branch={}
for ch in HUB:
    js=[op_shift(ch,g) for g in G]
    per_branch[ch[0]]=Counter(js)

expected={
    "A_L":Counter({3:2,-3:2}),
    "A_R":Counter({-1:2,1:2}),
    "A_O":Counter({1:2,-1:2}),
    "B_L":Counter({2:2,-2:2}),
    "B_R":Counter({-2:2,2:2}),
    "B_O":Counter({2:2,-2:2}),
    "T_L":Counter({2:2,-2:2}),
    "T_R":Counter({-2:2,2:2}),
    "T_O":Counter({2:2,-2:2}),
}
assert per_branch==expected

total=Counter()
for c in per_branch.values():
    total.update(c)
assert total==Counter({-3:2,-2:12,-1:4,1:4,2:12,3:2})

# Strong decomposition by physical branch families.
AL=per_branch["A_L"]
A1=per_branch["A_R"]+per_branch["A_O"]
BT=Counter()
for name in ("B_L","B_R","B_O","T_L","T_R","T_O"):
    BT.update(per_branch[name])

assert AL==Counter({-3:2,3:2})
assert A1==Counter({-1:4,1:4})
assert BT==Counter({-2:12,2:12})

# Sign symmetry is exact.
for k in (1,2,3):
    assert total[k]==total[-k]

print("SW1-A10-C2-M0-HUB-DIST DIRECT PHYSICAL DISTRIBUTION CERTIFICATE: PASS")
print("A_L -> j=+3 x2, -3 x2")
print("A_R+A_O -> j=+1 x4, -1 x4")
print("all B/T branches -> j=+2 x12, -2 x12")
print("total: -3:2, -2:12, -1:4, +1:4, +2:12, +3:2")
print("distribution is sign-symmetric and follows directly from the physical branches")
print("FIREWALL: shift multiplicity only; no lift/matrix/injectivity claim")
