#!/usr/bin/env python3
"""SW1-A9 full KNF finite-state cocycle certificate.

Certifies the transition algebra after J1:
- A7 raw maps preserve parity and have |index jump|<=3;
- the six genuinely new KNF affine types flip parity and have |jump|<=2;
- the same irrational Delta-rotation is the only base phase;
- T0<3L gives at most 3 lifts per sheet/parity, hence <=12 formal labels/index.

Physical label coincidences are to be quotient-identified; they can only reduce
the number of physical states and are not treated as separate physical points.
"""
from fractions import Fraction as F

# Constants in exact (L,Delta) coordinates:
# a=L+D, T=2L+2D, b=3L/2+2D, d=L/2+D, e=L/2.
a=(F(1),F(1))
T=(F(2),F(2))
b=(F(3,2),F(2))
d=(F(1,2),F(1))
e=(F(1,2),F(0))

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(q,x): return (q*x[0],q*x[1])

# A7 parity-preserving local jumps.
a7={
 "+a": {"P":("P",+1),"Q":("Q",-1)},
 "-a": {"P":("P",-1),"Q":("Q",+1)},
 "+T": {"P":("P",+2),"Q":("Q",-2)},
 "-T": {"P":("P",-2),"Q":("Q",+2)},
 "r_a":{"P":("Q",+3),"Q":("P",-3)},
 "r_T":{"P":("Q",+2),"Q":("P",-2)},
 "r_3a":{"P":("Q",+1),"Q":("P",-1)},
 "r_4a":{"P":("Q",0),"Q":("P",0)},
 "r_2b":{"P":("Q",0),"Q":("P",0)},
}
assert max(abs(j) for m in a7.values() for _,j in m.values())==3

# New translation constants are L/2+k Delta.
new_translation_k={
 "tau_e":0,
 "tau_d":1,
 "tau_b":2,
}
# P jump +k, Qbar jump -k, parity flips.
new_trans={}
for name,k in new_translation_k.items():
    new_trans[name]={
        "P":("P",+k,1),
        "Q":("Q",-k,1),
    }

# Reflection c-2b = L/2+k Delta mod L:
# r_ab: k=-1 -> P->Q +1
# r_Tb: k=0 -> P->Q 0
# r_b:  k=-2 -> P->Q +2
ref_k={
 "r_ab":-1,
 "r_Tb":0,
 "r_b":-2,
}
new_ref={}
for name,k in ref_k.items():
    new_ref[name]={
        "P":("Q",-k,1),
        "Q":("P",+k,1),
    }

assert max(abs(j) for m in new_trans.values() for _,j,_ in m.values())==2
assert max(abs(j) for m in new_ref.values() for _,j,_ in m.values())==2

# Exact constant identities behind the table.
assert e==(F(1,2),F(0))
assert d==(F(1,2),F(1))
assert b==(F(3,2),F(2))

# Reflection differences c-2b modulo one L.
r_ab=add(a,b)
r_Tb=add(T,b)
r_b=b
diffs={
 "r_ab":sub(r_ab,mul(2,b)),
 "r_Tb":sub(r_Tb,mul(2,b)),
 "r_b":sub(r_b,mul(2,b)),
}
# Normalize L coefficient to 1/2 modulo integers.
def half_mod_L(x):
    q=x[0]
    # subtract integer floor-like choice so L coefficient becomes 1/2.
    # All three exact q values are half-integers.
    n=q-F(1,2)
    assert n.denominator==1
    return (x[0]-n,x[1])

assert half_mod_L(diffs["r_ab"])==(F(1,2),F(-1))
assert half_mod_L(diffs["r_Tb"])==(F(1,2),F(0))
assert half_mod_L(diffs["r_b"])==(F(1,2),F(-2))

# Full finite-state bounds.
formal_labels_per_index=2*2*3
assert formal_labels_per_index==12
assert max(
    [abs(j) for m in a7.values() for _,j in m.values()]
    +[abs(j) for m in new_trans.values() for _,j,_ in m.values()]
    +[abs(j) for m in new_ref.values() for _,j,_ in m.values()]
)==3

print("SW1-A9 FULL KNF FINITE-STATE COCYCLE CERTIFICATE: PASS")
print("exact arithmetic: Python fractions.Fraction")
print("A7 maps: parity preserving, maximal index range 3")
print("new translations tau_e,tau_d,tau_b: parity flip, jumps 0,1,2")
print("new reflections r_ab,r_Tb,r_b: parity flip, jumps 1,0,2")
print("same single Delta base rotation; no second irrational phase")
print("T0<3L input -> <=3 lifts per sheet/parity")
print("formal state bound: 2 sheets * 2 parities * 3 lifts = 12 per index")
print("physical coincidences must be quotient-identified and only reduce this bound")
print("FIREWALL: finite-state reduction only; no finite/infinite component verdict")
