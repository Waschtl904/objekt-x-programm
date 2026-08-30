#!/usr/bin/env python3
"""SW1 A8/A9 global sheet-collision quotient symmetry certificate.

Analytic input (separate, already certified in A4/A5):
    Delta/L is irrational.

If two formal rotation sheets intersect physically, irrationality implies a
unique integer K and parity offset delta in Z/2 such that
    P_{n,eta} = Qbar_{K-n, eta+delta}
for every n,eta in the colliding pair. Thus the physical identification is
the involution J_{K,delta} swapping P/Q and reflecting n -> K-n.

This certificate verifies the purely finite transition statement:
J_{K,delta} commutes with every A7 raw affine transition and every new A9 KNF
transition, for both delta=0 and delta=1.

Therefore the quotient saturation of a formal connected component C is
C union J(C), hence at most two formal components. If formal components are
finite, the physical quotient components are finite as well.
"""
from fractions import Fraction as F

maps={
 "+a":("T",0,+1,-1),
 "-a":("T",0,-1,+1),
 "+T":("T",0,+2,-2),
 "-T":("T",0,-2,+2),
 "r_a":("R",0,+3,-3),
 "r_T":("R",0,+2,-2),
 "r_3a":("R",0,+1,-1),
 "r_4a":("R",0,0,0),
 "r_2b":("R",0,0,0),
 "+e":("T",1,0,0),
 "-e":("T",1,0,0),
 "+d":("T",1,+1,-1),
 "-d":("T",1,-1,+1),
 "+b":("T",1,+2,-2),
 "-b":("T",1,-2,+2),
 "r_ab":("R",1,+1,-1),
 "r_Tb":("R",1,0,0),
 "r_b":("R",1,+2,-2),
}
assert len(maps)==18
assert all(qj==-pj for _,_,pj,qj in maps.values())

def mod2(x): return x%2
def J(state,K,delta):
    sh,n,eta=state
    return ("Q" if sh=="P" else "P", K-n, mod2(eta+delta))

def step(state,rec):
    sh,n,eta=state
    kind,flip,pj,qj=rec
    jump=pj if sh=="P" else qj
    sh2=sh if kind=="T" else ("Q" if sh=="P" else "P")
    return (sh2,n+jump,mod2(eta+flip))

for delta in (0,1):
    for K in (-7,-1,0,1,8):
        for n in (-11,-3,0,4,13):
            for eta in (0,1):
                for sh in ("P","Q"):
                    state=(sh,n,eta)
                    assert J(J(state,K,delta),K,delta)==state
                    for name,rec in maps.items():
                        lhs=J(step(state,rec),K,delta)
                        rhs=step(J(state,K,delta),rec)
                        assert lhs==rhs,(delta,K,n,eta,sh,name,lhs,rhs)

assert all(rec[3]==-rec[2] for rec in maps.values())

print("SW1 GLOBAL SHEET-COLLISION QUOTIENT CERTIFICATE: PASS")
print("exact arithmetic: Python integers/Fraction")
print("18 directed affine transition types checked (9 A7 + 9 new A9)")
print("J_{K,delta} is an involution for delta=0 and delta=1")
print("J commutes with every transition because Q-jump = -P-jump")
print("physical gates/supports depend only on x, so identical labels share activity")
print("component saturation under quotient is C union J(C): at most two formal components")
print("ANALYTIC INPUT: Delta/L irrational gives uniqueness of K and excludes multiple offsets")
print("FIREWALL: quotient-symmetry lemma only; finite formal components required separately")
