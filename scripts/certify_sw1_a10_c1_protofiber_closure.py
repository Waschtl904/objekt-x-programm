#!/usr/bin/env python3
"""SW1-A10-C1 proto-fiber closure certificate.

Finite/algebraic scope:
- derive the complete H2 affine bridge alphabet from the certified 11-cell ledger;
- show all A7 raw and A9 KNF affine relation types are contained in that H2 alphabet;
- classify all 53 H2 channel/cell occurrences into a finite set of affine channel signatures;
- verify every signature has only orientation +/-1, half-L parity, integer L-lift shift,
  and integer Delta shift.

This is a proto-fiber closure result only. It does NOT determine the final fiber
dimension N because physical wrap/lift identifications and the common finest gate
partition of T_L still have to be imposed.
"""
from fractions import Fraction as F
from itertools import combinations

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
assert len(C)==11
assert [len(x) for x in C]==[6,5,4,7,4,7,4,3,3,7,3]
assert sum(map(len,C))==53

sig=set(q for cell in C for q in cell)
assert len(sig)==19

def fiber_signature(q):
    s,twolam,k=q
    assert s in (-1,1)
    eta=twolam % 2
    m=(twolam-eta)//2
    assert twolam==2*m+eta
    assert eta in (0,1)
    return (s,eta,m,k)

fib={fiber_signature(q) for q in sig}
assert len(fib)==19
assert max(abs(m) for _,_,m,_ in fib)==4
assert max(abs(k) for *_,k in fib)==4

def rel(a,b):
    s,l,k=a; t,m,j=b
    if s==t:
        lam=F(m-l,2); dk=j-k
        if lam<0 or (lam==0 and dk<0):
            lam=-lam; dk=-dk
        return ("T",lam,dk)
    return ("R",F(l+m,2),k+j)

H2=set()
pair_occ=0
for cell in C:
    for a,b in combinations(cell,2):
        pair_occ+=1
        H2.add(rel(a,b))
assert pair_occ==115
assert len(H2)==22
assert sum(1 for x in H2 if x[0]=="T")==8
assert sum(1 for x in H2 if x[0]=="R")==14

expected_H2={
 ("T",F(0),1),
 ("T",F(1,2),0),
 ("T",F(1,2),1),
 ("T",F(1),1),
 ("T",F(1),2),
 ("T",F(3,2),1),
 ("T",F(3,2),2),
 ("T",F(2),2),
 ("R",F(1,2),0),
 ("R",F(1,2),1),
 ("R",F(1),1),
 ("R",F(3,2),1),
 ("R",F(3,2),2),
 ("R",F(2),2),
 ("R",F(2),3),
 ("R",F(5,2),2),
 ("R",F(5,2),3),
 ("R",F(3),3),
 ("R",F(3),4),
 ("R",F(7,2),3),
 ("R",F(7,2),4),
 ("R",F(4),4),
}
assert H2==expected_H2

A7={
 ("T",F(1),1),
 ("T",F(2),2),
 ("R",F(1),1),
 ("R",F(2),2),
 ("R",F(3),3),
 ("R",F(4),4),
 ("R",F(3),4),
}
assert A7 <= H2

A9new={
 ("T",F(1,2),0),
 ("T",F(1,2),1),
 ("T",F(3,2),2),
 ("R",F(5,2),3),
 ("R",F(7,2),4),
 ("R",F(3,2),2),
}
assert A9new <= H2
assert len(A7|A9new)==13
assert (A7|A9new) <= H2

extra=H2-(A7|A9new)
assert len(extra)==9
assert all((2*x[1]).denominator==1 and F(x[2]).denominator==1 for x in H2)

print("SW1-A10-C1 PROTO-FIBER CLOSURE CERTIFICATE: PASS")
print("11 annulus t-cells; 53 channel/cell occurrences; 19 distinct affine channel signatures")
print("each channel signature = (orientation, half-L parity, integer L-lift shift, integer Delta shift)")
print("H2 free-free bridge alphabet: 22 types = 8 translations + 14 reflections")
print("all A7 raw affine types are contained in H2")
print("all genuine A9 KNF affine additions are contained in H2")
print("H2 adds exactly 9 affine types beyond A7+A9")
print("same single Delta base phase; only finite half-L parity/lift data")
print("FIREWALL: proto-fiber alphabet closure only; final physical fiber dimension N not yet determined")
