#!/usr/bin/env python3
"""SW1-A10-H2 complete KNF-pulled-back hub incidence/bridge certificate.

Scope: B_R = J_R^* H E_A on the positive odd-annulus coordinate t in (R,S),
S=T+sigma, in the small lower chamber used by A9.

The t-axis has 11 exact cells. Direct hub incidence has nine geometric branch
types, split where the reconstructed A_- window is hit. On exactly three
t-windows (d,d+R), (a,a+R), (T-R,T), the physical row is A_-=a-u and J_R^*
redistributes that hub row to the five free KNF branches.

The certificate aggregates coincident (free x, annulus t) channels BEFORE any
graph verdict, proves all aggregate coefficients nonzero, and classifies every
two-step free--t--free bridge.

Firewall: incidence/bridge graph only. No claim that augmented components are
finite/infinite and no Cross-Gram injectivity claim.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations
import sympy as sp

# Exact phase coordinates: a constant is lam*L + k*Delta; normalize Delta=1.
# Channel x(t) = slope*t + lam*L + k.
def X(slope,lam,k):
    return (F(slope),F(lam),F(k))

# Small lower chamber ordering inputs:
# 0<sigma<=R<epsilon<epsilon_*<1/2 and 0<g<1/2, L=4+2g.
# The exact t-cell endpoint order is:
cells=[
 ("R","eps"),
 ("eps","e+eps"),
 ("e+eps","d"),
 ("d","d+R"),
 ("d+R","a"),
 ("a","a+R"),
 ("a+R","a+eps"),
 ("a+eps","b"),
 ("b","T-R"),
 ("T-R","T"),
 ("T","S"),
]
assert len(cells)==11

# Positivity/order proof uses only:
# e=L/2>2, d=e+1, a=L+1, b-a=d, T-b=e, R<eps<1/2.
# Hence e+eps<d, d+R<a, a+eps<b, b<T-R.
assert F(2)>F(1,2)

p,r,q=sp.symbols("p r q", positive=True)

# A channel generator: name, x-affine tuple, coefficient, active cell indices.
raw=[]

def add(name,x,coeff,idxs):
    raw.append((name,x,sp.simplify(coeff),tuple(idxs)))

# Direct folded hub channels after removing the three reconstructed A_- pieces.
add("A_L", X(-1,1,1), -p, range(0,5))
add("A_R", X(+1,1,1), +p, range(0,7))
add("A_O_left", X(+1,-1,-1), -p, range(5,9))
add("A_O_tail", X(+1,-1,-1), -p, [10])

add("B_L_left", X(-1,F(3,2),2), -r, range(0,3))
add("B_L_right",X(-1,F(3,2),2), -r, range(4,8))
add("B_R", X(+1,F(3,2),2), +r, range(0,2))
add("B_O", X(+1,F(-3,2),-2), -r, range(8,11))

add("T_L_left", X(-1,2,2), -q, range(0,5))
add("T_L_right",X(-1,2,2), -q, range(6,10))
add("T_R", X(+1,2,2), +q, [0])
add("T_O", X(+1,-2,-2), -q, [10])

# Reconstruction coefficients for A_-=A+ -(r/p)B- +(r/p)B+ -(q/p)T- +(q/p)T+.
c={"A+":1,"B-":-r/p,"B+":r/p,"T-":-q/p,"T+":q/p}

# B_L hits A_- for t in (d,d+R), cell 3. Physical hub coefficient = -r.
BLpos={
 "A+":X(+1,F(1,2),0),
 "B-":X(-1,2,3),
 "B+":X(+1,1,1),
 "T-":X(-1,F(5,2),3),
 "T+":X(+1,F(3,2),1),
}
for z,x in BLpos.items():
    add("BL_rec_"+z,x,-r*c[z],[3])

# T_L hits A_- for t in (a,a+R), cell 5. Physical hub coefficient = -q.
TLpos={
 "A+":X(+1,0,0),
 "B-":X(-1,F(5,2),3),
 "B+":X(+1,F(1,2),1),
 "T-":X(-1,3,3),
 "T+":X(+1,1,1),
}
for z,x in TLpos.items():
    add("TL_rec_"+z,x,-q*c[z],[5])

# A_O hits A_- for t in (T-R,T), cell 9. Physical hub coefficient = -p.
AOpos={
 "A+":X(-1,3,3),
 "B-":X(+1,F(-1,2),0),
 "B+":X(-1,F(7,2),4),
 "T-":X(+1,0,0),
 "T+":X(-1,4,4),
}
for z,x in AOpos.items():
    add("AO_rec_"+z,x,-p*c[z],[9])

assert len(raw)==27

# Aggregate identical (x,t) channels cell by cell.
aggregated=[]
cell_channels=[]
for ci in range(len(cells)):
    groups=defaultdict(list)
    for name,x,coeff,idxs in raw:
        if ci in idxs:
            groups[x].append((name,coeff))
    out=[]
    for x,terms in groups.items():
        coeff=sp.simplify(sum(v for _,v in terms))
        out.append((x,coeff,tuple(name for name,_ in terms)))
        aggregated.append((ci,x,coeff,tuple(name for name,_ in terms)))
    cell_channels.append(out)

counts=[len(x) for x in cell_channels]
assert counts==[6,5,4,7,4,7,4,3,3,7,3]
assert sum(counts)==53

# The only two actual coefficient aggregations.
multi=[z for z in aggregated if len(z[3])>1]
assert len(multi)==2
coeffs={z[3]:sp.factor(z[2]) for z in multi}
assert set(coeffs)=={
    ("A_R","BL_rec_B+"),
    ("A_R","TL_rec_T+"),
}
assert sp.simplify(coeffs[("A_R","BL_rec_B+")]-(p**2-r**2)/p)==0
assert sp.simplify(coeffs[("A_R","TL_rec_T+")]-(p**2-q**2)/p)==0

# Exact canonical weights and strict positivity of both cancellation-sensitive terms.
P=sp.sqrt(sp.log(2))*2**sp.Rational(-3,4)
Rv=sp.sqrt(sp.log(3))*3**sp.Rational(-3,4)
Q=sp.sqrt(sp.log(2))*2**sp.Rational(-3,2)

assert sp.simplify(P**2-Q**2).is_positive is True

# Elementary strict brackets, also recognized exactly by SymPy:
# log 2 > 2/3 from log x = 2*atanh((x-1)/(x+1));
# log 3 < 10/9 by bounding the atanh(1/2) tail.
assert (sp.log(2)-sp.Rational(2,3)).is_positive is True
assert (sp.Rational(10,9)-sp.log(3)).is_positive is True
p_lower=1/(3*sp.sqrt(2))
r_upper=sp.Rational(10,27)/sp.sqrt(3)
assert (p_lower-r_upper).is_positive is True
assert sp.Integer(243)>sp.Integer(200)
assert sp.simplify(P**2-Rv**2).is_positive is True

# Hence every aggregate cell-channel is nonzero after canonical substitution.
for ci,x,coeff,names in aggregated:
    cv=sp.simplify(coeff.subs({p:P,r:Rv,q:Q}))
    assert cv!=0
    assert cv.is_zero is not True

# Every w(t) node connects all aggregated free channels active on its t-cell.
pair_occurrences=0
relation_cells=defaultdict(set)

def relation(x1,x2):
    s1,l1,k1=x1
    s2,l2,k2=x2
    if s1==s2:
        # translation, canonical up to inverse
        l=l2-l1; k=k2-k1
        if l<0 or (l==0 and k<0):
            l=-l; k=-k
        return ("T",l,k)
    assert s1==-s2
    return ("R",l1+l2,k1+k2)

for ci,out in enumerate(cell_channels):
    for A,B in combinations(out,2):
        pair_occurrences+=1
        relation_cells[relation(A[0],B[0])].add(ci)

assert pair_occurrences==115
assert len(relation_cells)==22

expected_trans={
 ("T",F(0),F(1)),             # Delta
 ("T",F(1,2),F(0)),           # e
 ("T",F(1,2),F(1)),           # d
 ("T",F(1),F(1)),             # a
 ("T",F(1),F(2)),             # L+2Delta
 ("T",F(3,2),F(1)),           # b-Delta
 ("T",F(3,2),F(2)),           # b
 ("T",F(2),F(2)),             # T
}
expected_ref={
 ("R",F(1,2),F(0)),           # r_e
 ("R",F(1,2),F(1)),           # r_d
 ("R",F(1),F(1)),             # r_a
 ("R",F(3,2),F(1)),           # r_{b-Delta}
 ("R",F(3,2),F(2)),           # r_b
 ("R",F(2),F(2)),             # r_T
 ("R",F(2),F(3)),             # r_{T+Delta}
 ("R",F(5,2),F(2)),           # r_{a+b-Delta}
 ("R",F(5,2),F(3)),           # r_{a+b}
 ("R",F(3),F(3)),             # r_{3a}
 ("R",F(3),F(4)),             # r_{2b}
 ("R",F(7,2),F(3)),           # r_{T+b-Delta}
 ("R",F(7,2),F(4)),           # r_{T+b}
 ("R",F(4),F(4)),             # r_{4a}
}
assert set(relation_cells)==expected_trans|expected_ref
assert len(expected_trans)==8 and len(expected_ref)==14

# Finite-state range over the same Delta rotation.
# Translation lam*L+kDelta has |P-index jump|=|k|.
trans_range=max(abs(k) for _,lam,k in expected_trans)
# For reflection c=lam L+kDelta, relative to 2b=3L+4Delta,
# P_n -> Qbar_{n+(4-k)} up to finite parity.
ref_range=max(abs(4-k) for _,lam,k in expected_ref)
assert trans_range==2
assert ref_range==4
assert max(trans_range,ref_range)==4
assert all(l.denominator in (1,2) for _,l,k in relation_cells)

print("SW1-A10-H2 COMPLETE HUB-INCIDENCE CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("exact t-cell count: 11")
print("raw channel generators: 27 = 12 direct-split + 15 reconstructed-row pullbacks")
print("aggregated nonzero channel/cell occurrences: 53")
print("only two coefficient aggregations: (p^2-r^2)/p and (p^2-q^2)/p; both >0")
print("two-step free--annulus--free pair occurrences across cells: 115")
print("unique affine bridge types: 22 = 8 translation magnitudes + 14 reflections")
print("same irrational Delta base retained; half-L parity only")
print("maximal bridge index range: 4")
print("FIREWALL: complete incidence/bridge algebra only; no component or kernel verdict")
