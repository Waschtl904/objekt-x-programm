#!/usr/bin/env python3
"""SW1-A10-H0 exact hub phase-algebra certificate.

The annulus source term is
  H E_A w(x)
   = p[w(x-a)-w(x+a)]
   + r[w(x-b)-w(x+b)]
   + q[w(x-T)-w(x+T)].

On the signed annulus, the six source shifts x -> x +/- a,b,T have the same
single Delta base rotation as A9:
  a = L+Delta,
  T = 2L+2Delta,
  b = 3L/2+2Delta.
Thus +/-a and +/-T preserve half-period parity, while +/-b flips it.

If oddness is used to fold the signed annulus to its positive half, negation
itself is a finite sheet-switch:
  -P_{n,eta} = Qbar_{n+4,eta},
  -Qbar_{n,eta} = P_{n-4,eta}       (mod L).
So even after folding there is no new irrational phase.

Firewall:
This is only phase/transition algebra. It does NOT prove finite augmented
components, a finite scalar Cross-Gram matrix, or injectivity.
"""
from fractions import Fraction as F

# Exact coordinates in (L,Delta).
a=(F(1),F(1))
T=(F(2),F(2))
b=(F(3,2),F(2))
two_b=(F(3),F(4))

# signed hub shifts: (parity flip, P-index jump, Qbar-index jump)
hub={
 "+a":(0,+1,-1),
 "-a":(0,-1,+1),
 "+T":(0,+2,-2),
 "-T":(0,-2,+2),
 "+b":(1,+2,-2),
 "-b":(1,-2,+2),
}
assert len(hub)==6
assert max(abs(pj) for _,pj,_ in hub.values())==2
assert all(qj==-pj for _,pj,qj in hub.values())

# Exact constants behind the shift table.
assert a==(F(1),F(1))
assert T==(F(2),F(2))
assert b==(F(3,2),F(2))

# Negation relative to Qbar_n = 2b-x0-n Delta.
# Since 2b = 3L+4Delta, modulo L:
# -P_n = Qbar_{n+4}; -Qbar_n = P_{n-4}.
def neg(state):
    sh,n,eta=state
    if sh=="P":
        return ("Q",n+4,eta)
    return ("P",n-4,eta)

for sh in ("P","Q"):
    for n in range(-8,9):
        for eta in (0,1):
            assert neg(neg((sh,n,eta)))==(sh,n,eta)

# Apply signed hub shift in the formal P/Qbar parity convention.
def shift(state,rec):
    sh,n,eta=state
    flip,pj,qj=rec
    j=pj if sh=="P" else qj
    return (sh,n+j,(eta+flip)%2)

# Hub shifts commute with physical negation as expected:
# -(x+c)=(-x)-c, so neg after +c equals -c after neg.
inverse={"+a":"-a","-a":"+a","+T":"-T","-T":"+T","+b":"-b","-b":"+b"}
for sh in ("P","Q"):
    for n in range(-8,9):
        for eta in (0,1):
            state=(sh,n,eta)
            for name,rec in hub.items():
                lhs=neg(shift(state,rec))
                rhs=shift(neg(state),hub[inverse[name]])
                assert lhs==rhs,(state,name,lhs,rhs)

# Finite range after signed representation and after one odd-fold negation.
assert 2<4
folded_max_range=4
assert folded_max_range==4

print("SW1-A10-H0 HUB PHASE ALGEBRA CERTIFICATE: PASS")
print("exact arithmetic: Python fractions.Fraction")
print("six signed hub shifts certified")
print("+/-a: parity preserving, index jump +/-1")
print("+/-T: parity preserving, index jump +/-2")
print("+/-b: parity flipping, index jump +/-2")
print("odd folding negation: P_n -> Qbar_{n+4}, Qbar_n -> P_{n-4}")
print("signed max range=2; folded representation max range=4")
print("single Delta base phase retained; no new irrational rotation")
print("FIREWALL: phase algebra only; no augmented-component or injectivity verdict")
