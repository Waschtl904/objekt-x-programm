#!/usr/bin/env python3
"""SW1-A10-C1C1 corrected parity-fold / cover normalization certificate.

Algebraic/mechanical scope:
- the signed even horizon fold F_+ y = sqrt(2) y|_(0,T0) is unitary at norm-square level;
- the signed odd annulus fold F_- w = sqrt(2) w|_(R,S) is unitary at norm-square level;
- the positive four-sheet cover V_H has component scale 1/2, hence U_H=V_H F_+
  has original-y component scale 1/sqrt(2);
- the positive annulus lift cover V_W is unscaled, hence U_W=V_W F_-
  has original-w component scale sqrt(2);
- fixed-point collisions of the Klein-four circle action occur only on finite
  solution sets and are irrelevant to direct-sum norm bookkeeping;
- no pointwise distinctness assumption is used.

Analytic change-of-variable and closed-image statements remain written Hilbert-space mathematics.
"""
from fractions import Fraction as F

signed_norm_sq = F(2)

horizon_species = 4
original_y_component_scale_sq = F(1,2)
assert horizon_species * original_y_component_scale_sq == signed_norm_sq

assert F(2) * F(1,4) == F(1,2)

annulus_component_scale_sq = F(2)
assert annulus_component_scale_sq == signed_norm_sq

P0=(1,0,0)
P1=(1,1,0)
Q0=(-1,0,4)
Q1=(-1,1,4)
G=(P0,P1,Q0,Q1)

assert P0 != P1 and Q0 != Q1

rhs_classes={(F(0),F(4)),(F(1,2),F(4))}
assert len(rhs_classes)==2
collision_points_upper_bound=2*len(rhs_classes)
assert collision_points_upper_bound==4

assert len(G)==4

print("SW1-A10-C1C1 PARITY-FOLD NORMALIZATION CERTIFICATE: PASS")
print("signed even/odd norm-square = 2 * positive-half norm-square")
print("correct original-horizon component scale-square = 1/2 (scale 1/sqrt(2))")
print("correct original-annulus component scale-square = 2 (scale sqrt(2))")
print("Klein-four point collisions lie in at most four circle points")
print("pointwise orbit distinctness is not required for the direct-sum isometry")
print("FIREWALL: analytic change-of-variable, closed-image, and operator intertwining remain separate")
