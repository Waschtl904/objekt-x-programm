#!/usr/bin/env python3
"""SW1-A8 midpoint degeneracy correction certificate.

Scope:
- exact collision analysis of the 20 middle P/Qbar lift states used by A8;
- prove that among the exact 20 A8 middle-block labels the only cross-sheet
  physical collision phase in 0<s<Delta is s=Delta/2;
- prove 4 Delta < L < 5 Delta exactly;
- certify that removing s=Delta/2 leaves two nonempty open separator intervals.

Firewall:
This supplements the existing A8 raw-edge gate certificate. It does not alter
the A8 finite-component conclusion; it corrects the pointwise separator scope.
"""
from fractions import Fraction as F

# Work in exact coordinates relative to Delta: r=L/Delta with 4<r<5.
# Completeness scope: A8 has exactly four middle layers because the A7 edge
# range is <=3, and A8.8-A8.9 give exactly 20 labels on those layers.
# Same-sheet equality within these layers is impossible for distinct labels:
# |j-m|<=3 while 4Delta<L, so a nonzero lift difference cannot be cancelled.
# Cross-sheet equality P_j^k = Q_m^ell implies
# 2 s/Delta = (4-m-j) + (ell-k) r.

states = {
    0:[("P",0),("P",1),("P",2),("Q",0),("Q",1)],
    1:[("P",0),("P",1),("P",2),("Q",0),("Q",1)],
    2:[("P",0),("P",1),("Q",0),("Q",1),("Q",2)],
    3:[("P",0),("P",1),("Q",0),("Q",1),("Q",2)],
}

# Exhaust same-sheet pairs in the finite middle ledger.
flat=[]
for j in range(4):
    for sh,k in states[j]:
        flat.append((j,sh,k))
assert len(flat)==20
for idx,(j,sh,k) in enumerate(flat):
    for m,th,ell in flat[idx+1:]:
        if sh!=th:
            continue
        assert abs(j-m)<=3
        if k!=ell:
            assert 4*abs(k-ell) > abs(j-m)
        else:
            assert j!=m

candidates=[]
for j in range(4):
    for sh,k in states[j]:
        if sh!="P":
            continue
        for m in range(4):
            for th,ell in states[m]:
                if th!="Q":
                    continue
                A=4-m-j
                B=ell-k
                # r in (4,5), so A+B r ranges strictly between endpoint values.
                v4=F(A)+F(4)*F(B)
                v5=F(A)+F(5)*F(B)
                lo=min(v4,v5)/2
                hi=max(v4,v5)/2
                # Could s/Delta intersect (0,1)?
                if hi>0 and lo<1:
                    candidates.append((j,k,m,ell,A,B,lo,hi))

assert len(candidates)==10
assert all((A,B)==(1,0) for _,_,_,_,A,B,_,_ in candidates)
assert all(lo==F(1,2) and hi==F(1,2) for *_,lo,hi in candidates)

# Hence all ten possible middle cross-sheet coincidences occur at s=Delta/2
# and there are no others in 0<s<Delta.
expected_pairs = {
    (0,0,3,0),(0,1,3,1),(0,2,3,2),
    (0,0,3,0), # set will deduplicate; kept visually grouped below
}
collision_pairs={(j,k,m,ell) for j,k,m,ell,*_ in candidates}
assert len(collision_pairs)==10

# Exact fixed inequalities:
# L-4Delta = log(256/243) > 0.
assert 256>243
# 5Delta-L = (1/2) log(3^12/2^19) > 0.
assert 3**12 > 2**19

# For 0<epsilon<Delta/2, both corrected separator components
# (epsilon,Delta/2) and (Delta/2,Delta-epsilon) are nonempty.
# Pure order consequence; no sampling required.
print("SW1-A8 MIDPOINT DEGENERACY FIX CERTIFICATE: PASS")
print("exact arithmetic: Python fractions.Fraction")
print("4 Delta < L < 5 Delta certified by integer inequalities")
print("all 20 A8 middle-block labels exhaustively covered; same-sheet collisions excluded")
print("the unique collision phase in 0<s<Delta is s=Delta/2")
print("exactly 10 cross-sheet state-pair coincidences occur there")
print("corrected separator set: (epsilon,Delta/2) U (Delta/2,Delta-epsilon)")
print("both components are open and nonempty for 0<epsilon<Delta/2")
print("GLOBAL FIREWALL: collisions outside the middle block require the separate sheet-quotient lemma")
print("FIREWALL: supplements A8; no KNF/A9 or Schur claim")
