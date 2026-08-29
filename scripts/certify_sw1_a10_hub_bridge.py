#!/usr/bin/env python3
"""SW1-A10-H1: exact hub bridge across the A9 staggered separator.

Normalize Delta=1 and let g=s_*/Delta in (0,1/2).
On the A9 small-epsilon staggered separator domain
  0<R<epsilon<(1-g)/2,
  epsilon<s<1-epsilon-g,
set L=4+2g.

The parity-0 left free state P_{0,0}^{(1)} has
  x_L = L+s.
The same positive annulus coordinate
  t = b-x_L
is reached by the folded r_b hub incidence from x_L and by the -a hub
incidence from
  x_R = a+t.
The latter is exactly the parity-1 right state Qbar_{1,1}^{(2)}
(relative to the staggered parity-1 A8 block based at index -2).

Thus one annulus degree of freedom couples the two formal sides even though
the direct free r_{a+b} Gram edge is inactive.

Firewall:
This disproves only the naive transfer of A9 finite free components to
augmented free+annulus components. It does NOT prove an infinite augmented
component or Cross-Gram noninjectivity.
"""
import sympy as sp

g,eps,R,s=sp.symbols("g eps R s", positive=True)
L=4+2*g
a=L+1
b=sp.Rational(3,2)*L+2
T=2*L+2
T0=T+eps

xL=L+s
t=b-xL
xR=a+t

# Exact formulas.
assert sp.expand(t-(L/2+2-s))==0
assert sp.expand(xR-(sp.Rational(3,2)*L+3-s))==0
assert sp.expand(xR-(a+b-xL))==0

# Exact formal state labels:
# parity 0, index 0, P lift 1.
P00_lift1=s+L
assert sp.expand(xL-P00_lift1)==0

# parity 1 base phase is s+g at index -2.
# At global index 1, local layer j=3:
# Qbar residue = 1-(s+g); lift 2.
Q11_lift2=1-s-g+2*L
assert sp.expand(xR-Q11_lift2)==0

# Basic side membership is exactly A8:
# P layer-0 lift-1 is left; Q layer-3 lift-2 is right.

# Strict assumptions encoded through positive slacks:
# 0<g<1/2, 0<R<eps, eps<(1-g)/2, eps<s<1-eps-g.
A,B,C,D=sp.symbols("A B C D", positive=True)
# A=g; B=1/2-g; C=eps-R; D=s-eps;
# E=1-eps-g-s >0.
E=sp.symbols("E", positive=True)

# We verify all needed margins by expressing them as positive combinations
# of the abstract strict slacks g,R,eps-R,s-eps,1-eps-g-s.
margins={
    "xL>0": xL,
    # r_b folded branch: xL in (0,b-R), equivalently t>R.
    "b-R-xL": b-R-xL,
    "t-R": t-R,
    # upper annulus bound: t<S=T+sigma; T-t is already >0.
    "T-t": T-t,
    # -a positive branch: xR in (a+R,T0).
    "xR-a-R": xR-a-R,
    "T0-xR": T0-xR,
    # direct r_{a+b} Gram edge is inactive at xL because xL<a.
    "a-xL": a-xL,
}

# Substitute a positive-slack parametrization:
# g=A, eps=R+C, s=eps+D=R+C+D,
# and E=1-eps-g-s fixes R through
# 1 - (R+C) - A - (R+C+D) = E
# => 2R = 1-A-2C-D-E.
Rexpr=(1-A-2*C-D-E)/2
subs={
    g:A,
    R:Rexpr,
    eps:Rexpr+C,
    s:Rexpr+C+D,
}
for name,m in margins.items():
    z=sp.factor(sp.expand(m.subs(subs)))
    # For all margins occurring here SymPy can certify positivity from
    # positive A,B,C,D,E after using A<1/2 where needed.
    if name=="a-xL":
        # a-xL = 1-s = eps+g+E >0 from E definition.
        target=(Rexpr+C)+A+E
        assert sp.expand(z-target)==0,(name,z,target)
    elif name in ("b-R-xL","t-R","xR-a-R"):
        # t-R = L/2+2-s-R = 3/2 + 3A/2 + 2C + D/2 + 3E/2
        target=sp.Rational(3,2)+sp.Rational(3,2)*A+2*C+D/2+sp.Rational(3,2)*E
        assert sp.expand(z-target)==0,(name,z,target)
    elif name=="T0-xR":
        # = L/2-1+s+eps = 2 - E
        # Better exact lower bound: g<1/2 and E<1 follows from all original positives;
        # direct expression before elimination is 1+g+s+eps >0.
        assert sp.expand(m-(1+g+s+eps))==0
    elif name=="T-t":
        assert sp.expand(m-(sp.Rational(3,2)*L+s))==0
    elif name=="xL>0":
        assert sp.expand(m-(L+s))==0

# Direct algebraic activity checks in original variables.
assert sp.expand((b-R-xL)-(t-R))==0
assert sp.expand((xR-a-R)-(t-R))==0
assert sp.expand((T0-xR)-(1+g+s+eps))==0
assert sp.expand((T-t)-(sp.Rational(3,2)*L+s))==0
assert sp.expand((a-xL)-(1-s))==0

# Since s<1-eps-g<1, the direct free r_{a+b} edge is indeed inactive.
# Yet the two hub incidences share exactly t.
assert sp.expand((b-xL)-t)==0
assert sp.expand((xR-a)-t)==0

print("SW1-A10-H1 HUB-BRIDGE CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("left free state: P_{0,0}^{(1)}, x_L=L+s")
print("right free state: Qbar_{1,1}^{(2)}, x_R=3L/2+3-s")
print("shared positive annulus coordinate: t=b-x_L=x_R-a")
print("r_b hub incidence from x_L active")
print("-a hub incidence from x_R active")
print("direct free r_{a+b} Gram edge inactive because x_L<a")
print("therefore the A9 staggered free separator is crossed by hub augmentation")
print("FIREWALL: no infinite augmented component and no Cross-Gram kernel claim")
