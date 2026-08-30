#!/usr/bin/env python3
"""SW1-A10-C1C0 formal ambient-cover certificate.

Scope:
- distinguishes partition boundaries, operator channel types and formal orbit-cover states;
- certifies the 12-slot free/physical orbit cover from sheet x parity x lift;
- certifies at most 3 positive annulus lifts;
- certifies every one of the 19 H2 channel signatures lands in the same
  four sheet/parity species modulo L and has direct H2 base-index jump <=3;
- therefore gives the formal fixed cover sizes 15 input slots
  (12 free + 3 annulus) and 12 physical-output slots.

Firewall:
These are formal orbit-cover slots, not yet independent Hilbert fiber
coordinates. The unitary/isometric fiberization map, its image constraints,
and the direct (I+A)J_R free-to-physical matrix ledger remain open.
"""
from fractions import Fraction as F

# Normalized constants chi=1, r=s*/chi with project inequality 3<r<4.
# Delta=1+2r, L=4+10r, epsilon_*=(r+1)/2.
# T=2L+2Delta. For any epsilon<epsilon_* and sigma<=R<epsilon:
# S=T+sigma<T+epsilon=T0<T+epsilon_*<3L.
# Exact margin:
# 3L-(T+epsilon_*)=(3+11r)/2 > 0.
# It suffices to verify the coefficient identity.
# vectors below are affine coefficients (constant, r)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(q,a): return (q*a[0],q*a[1])
L=(F(4),F(10))
D=(F(1),F(2))
eps_star=(F(1,2),F(1,2))
T=add(mul(2,L),mul(2,D))
margin=add(mul(3,L),mul(-1,add(T,eps_star)))
assert margin==(F(3,2),F(11,2))
# r>3 makes this strictly positive; already stronger than positivity.
assert margin[0]+3*margin[1] > 0

# A9 formal orbit-cover states.
sheets=("P","Q")
parities=(0,1)
lifts=(0,1,2)
FREE_STATES={(sh,eta,k) for sh in sheets for eta in parities for k in lifts}
assert len(FREE_STATES)==12

# Positive odd-folded annulus lies in (R,S) subset (0,T0) with T0<3L,
# hence a residue mod L has at most three physical lifts.
W_STATES={0,1,2}
assert len(W_STATES)==3

# Complete H2 aggregated channel signatures:
# (slope, 2*lambda, k) for x(t)=slope*t+(lambda)L+k Delta.
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
sig=sorted({q for cell in C for q in cell})
assert len(sig)==19

mapped=[]
for slope,twolam,k in sig:
    eta=twolam % 2
    integer_L=(twolam-eta)//2
    assert twolam == 2*integer_L + eta
    if slope==1:
        # P_j,eta has phase t+j Delta+eta L/2, hence j=k.
        sheet="P"; j=k
    else:
        # Qbar_j,eta has phase -t+(4-j)Delta+eta L/2, hence j=4-k.
        sheet="Q"; j=4-k
    assert sheet in sheets and eta in parities
    mapped.append((slope,twolam,k,sheet,eta,integer_L,j))

# Direct W->physical H2 channels need no fifth sheet/parity species.
assert {(x[3],x[4]) for x in mapped} == {
    ("P",0),("P",1),("Q",0),("Q",1)
}
# Their direct base-index range is only 3. (The H2 free-t-free bridge
# composition can reach 4, but that is not the inverse-free C_R channel range.)
assert max(abs(x[6]) for x in mapped)==3
assert {x[6] for x in mapped}=={-2,-1,0,1,2,3}

FORMAL_INPUT_SLOTS=len(FREE_STATES)+len(W_STATES)
FORMAL_OUTPUT_SLOTS=len(FREE_STATES)
assert (FORMAL_INPUT_SLOTS,FORMAL_OUTPUT_SLOTS)==(15,12)

print("SW1-A10-C1C0 FORMAL AMBIENT-COVER CERTIFICATE: PASS")
print("12 formal free/physical orbit-cover slots = 2 sheets * 2 parities * 3 lifts")
print("3 positive annulus lift slots because S<T0<3L")
print("19 H2 channel signatures close on the same four sheet/parity species")
print("direct H2 W->physical base-index jump range: -2..3 (max abs 3)")
print("formal fixed cover shape: input 15 = 12 free + 3 annulus; output 12")
print("FIREWALL: cover slots are not yet independent Hilbert-fiber coordinates")
print("FIREWALL: unitary fiberization/image constraints and direct (I+A)J_R ledger remain open")
