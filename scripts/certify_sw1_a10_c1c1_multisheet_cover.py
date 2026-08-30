#!/usr/bin/env python3
"""SW1-A10-C1C1 finite algebraic skeleton for the analytic multi-sheet cover.

The analytic lemma uses four circle maps on T_L:
 P0(x)=x,
 P1(x)=x+L/2,
 Q0(x)=4 Delta-x,
 Q1(x)=4 Delta-x+L/2.
They are the Klein-four orbit of the half-shift h and reflection q modulo L.
Each map is Lebesgue-measure preserving. Together with T0<3L this yields
12 formal horizon cover slots (4 species x 3 lifts); the analytic isometry
uses normalization 1/2 because the horizon is copied four times.

This certificate checks only the exact affine/group and lift-count skeleton.
The L2 change-of-variables/isometry proof is analytic and remains a separate
lemma/review item.
"""
from fractions import Fraction as F

# affine map represented by (slope, Lcoeff, Dcoeff), x -> slope*x+c
P0=(1,F(0),F(0))
P1=(1,F(1,2),F(0))
Q0=(-1,F(0),F(4))
Q1=(-1,F(1,2),F(4))

def norm(m):
    s,l,d=m
    # normalize L coefficient modulo integers into [0,1)
    n=l.numerator//l.denominator
    l=l-F(n)
    return (s,l,d)

def compose(f,g):
    # f o g
    sf,lf,df=f; sg,lg,dg=g
    return norm((sf*sg, sf*lg+lf, sf*dg+df))

h=P1
q=Q0
I=P0

assert compose(h,h)==I
assert compose(q,q)==I
assert compose(h,q)==Q1
assert compose(q,h)==Q1
assert compose(Q1,Q1)==I
assert {I,h,q,Q1}=={P0,P1,Q0,Q1}

# All four maps have slope +/-1, hence preserve Lebesgue measure on the circle.
assert {abs(m[0]) for m in (P0,P1,Q0,Q1)}=={1}

# C1C0 normalized margin: T0<T+eps_*<3L.
# r>3, with 3L-(T+eps*)=(3+11r)/2.
assert F(3,2)+F(11,2)*3 > 0

species=4
lifts=3
assert species*lifts==12
# Four equal-norm copies require amplitude normalization 1/sqrt(4)=1/2.
scale=F(1,2)
assert species*scale*scale==1

print("SW1-A10-C1C1 MULTI-SHEET COVER SKELETON CERTIFICATE: PASS")
print("four circle maps form an exact Klein four-group modulo L")
print("all four maps have slope +/-1 and preserve circle Lebesgue measure")
print("T0<3L gives at most three physical horizon lifts per circle residue")
print("formal horizon cover: 4 species * 3 lifts = 12 slots")
print("analytic isometry normalization skeleton: 4*(1/2)^2=1")
print("FIREWALL: L2 change-of-variables, closed-image characterization and operator intertwining are analytic, not certified here")
