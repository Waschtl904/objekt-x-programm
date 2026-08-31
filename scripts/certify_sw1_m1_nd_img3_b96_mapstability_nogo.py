#!/usr/bin/env python3
"""Exact no-go certificate for naive B96 atom-to-atom pullback stability.

Witness from the failed IMG3 column-Schur probe:
- first C1B2A reference chamber,
- B96 atom index 3,
- P0 output lift 2 (active row R5),
- FREE branch r_3a.

The effective affine pullback is (-1,0,3), and the image of the atom midpoint
is exactly a B96 wall while the atom has positive half-width 2/7. Therefore
that output atom image crosses an input B96 wall in its interior.

Conclusion: the original B96 partition is NOT invariant atom-by-atom under
all effective pullbacks.  A column Schur ledger may still be built on a
refinement, but not by silently identifying each B96 output atom with one
B96 input atom.
"""

from fractions import Fraction as F
import certify_sw1_a10_c2_m1_full_b96 as m1

print("SW1 M1-ND IMG3 B96 MAP-STABILITY NO-GO CERTIFICATE")

rep=m1.reps[0]
sigma,R,eps=rep
vals=sorted(m1.bvalue(sig,rep) for sig in m1.B96)
assert len(vals)==96 and len(set(vals))==96

ai=3
lo=vals[ai]
hi=vals[ai+1]
theta=(lo+hi)/2
half=(hi-lo)/2
assert half==F(2,7)

lout=2
xout=theta+lout*m1.L
rows=m1.active_rows(xout,eps)
assert rows==["R5"]

gin,j,_,_=m1.free_sr[("r_3a","P0")]
_,s,eta,kappa=m1.gdict[gin]
amap=(s,F(eta,2),s*j+kappa)
assert amap==(-1,F(0),3)

image_mid=(amap[0]*theta+amap[1]*m1.L+amap[2]*m1.D)%m1.L
hits=[(idx,w) for idx,w in enumerate(vals) if w==image_mid]
assert len(hits)==1
wall_index,wall_value=hits[0]

# Since the affine map has slope -1, it is an isometry.  The source atom has
# positive radius half about theta; hence its image is an open arc of the
# same radius half about image_mid.  A wall at the image midpoint is strictly
# interior to that image arc.
assert half>0

print("reference chamber index: 0")
print("output atom index:",ai)
print("output lift:",lout)
print("active row:",rows[0])
print("FREE branch: r_3a")
print("effective map:",amap)
print("source atom half-width:",half)
print("image midpoint equals B96 wall index:",wall_index)
print("image midpoint/wall value:",wall_value)
print("NO-GO: B96 is not atom-to-atom stable under all effective pullbacks")
print("FIREWALL: this kills only the naive unrefined column-ledger shortcut")
print("SW1 M1-ND IMG3 B96 MAP-STABILITY NO-GO CERTIFICATE: PASS")
