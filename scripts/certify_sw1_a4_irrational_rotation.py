#!/usr/bin/env python3
import sympy as sp

L2,L3=sp.log(2),sp.log(3)
a=L2/2; b=L3/2; T=2*a; d=b-a; e=T-b; Delta=sp.simplify(d-e)
x,eps=sp.symbols('x eps', real=True)

c2=L2*2**sp.Rational(-9,4)
c11=2*L3/(3*sp.sqrt(3))
beta_m=-2*c2
beta_b=-c11
beta_T=-sp.Rational(5,8)*L2

# Fixed arithmetic.
assert sp.simplify(2*b-3*a-Delta)==0
assert sp.simplify(a-Delta-2*e)==0
assert sp.simplify(a-3*Delta).is_positive is True
assert sp.simplify(a-2*Delta).is_positive is True
assert beta_m.is_negative is True
assert beta_b.is_negative is True
assert beta_T.is_negative is True

A=sp.simplify(2*d-eps)
B=sp.simplify(T-eps)
L=sp.simplify(B-A)
C=sp.simplify(B-Delta)
theta=sp.simplify(C-A)

assert sp.simplify(A-(a+Delta-eps))==0
assert sp.simplify(L-(a-Delta))==0
assert sp.simplify(L-2*e)==0
assert sp.simplify(theta-(a-2*Delta))==0
assert sp.simplify(B-C-Delta)==0
assert sp.simplify(theta+Delta-L)==0

# Chamber-II positive slacks.
u=sp.simplify(2*eps-Delta)   # >0
v=sp.simplify(Delta-eps)     # >0
assert sp.simplify(u+2*v-Delta)==0

# I lies in (a,T).
assert sp.simplify(A-a-v)==0
assert sp.simplify(T-B-eps)==0

# High branch I_+=(C,B) is wholly in R5: C>a+eps.
assert sp.simplify((C-(a+eps))-((a-3*Delta)+2*v))==0

# Low branch x1=r_3a(x), x in (A,C):
# x1 in (a+eps+Delta, T-Delta+eps).
low_y1_lo=sp.simplify(3*a-C)
low_y1_hi=sp.simplify(3*a-A)
assert sp.simplify(low_y1_lo-(a+eps+Delta))==0
assert sp.simplify(low_y1_hi-(T-Delta+eps))==0
assert sp.simplify(T-low_y1_hi-v)==0

# Low composition r_2b o r_3a is +Delta.
low_comp=sp.simplify(2*b-(3*a-x))
assert sp.simplify(low_comp-(x+Delta))==0
assert sp.simplify((B-(C+Delta)))==0
assert sp.simplify((A+Delta)-A-Delta)==0

# High branch first image stays in R5.
high_y1_lo=sp.simplify(3*a-B)
high_y1_hi=sp.simplify(3*a-C)
assert sp.simplify(high_y1_lo-(a+eps))==0
assert sp.simplify(high_y1_hi-(a+eps+Delta))==0
assert sp.simplify((T-eps)-high_y1_hi-((a-3*Delta)+2*v))==0

# Second image x+Delta lies in the extended T-tail and below T0 exactly because u>0.
high_y2_lo=sp.simplify(B)
high_y2_hi=sp.simplify(B+Delta)
T0=T+eps
assert sp.simplify(T0-high_y2_hi-u)==0

# Third image r_4a(x+Delta) lies in R6/R7; lower gap above T-eps is u.
high_y3_lo=sp.simplify(4*a-high_y2_hi)
high_y3_hi=sp.simplify(4*a-high_y2_lo)
assert sp.simplify(high_y3_lo-(T+eps-Delta))==0
assert sp.simplify(high_y3_hi-(T+eps))==0
assert sp.simplify(high_y3_lo-(T-eps)-u)==0

# Four-step composition.
high_comp=sp.simplify(2*b-(4*a-(2*b-(3*a-x))))
assert sp.simplify(high_comp-(x+2*Delta-a))==0
assert sp.simplify(high_comp-(x+Delta-L))==0

# Endpoint transport of high branch: C -> A and B -> A+Delta.
assert sp.simplify((C+Delta-L)-A)==0
assert sp.simplify((B+Delta-L)-(A+Delta))==0
assert sp.simplify(B-(A+Delta)-(a-2*Delta))==0

# Circle coordinate t=x-A: cut is L-Delta, both branches are +Delta mod L.
assert sp.simplify((C-A)-(L-Delta))==0

print('SW1-A4 IRRATIONAL-ROTATION AFFINE CERTIFICATE: PASS')
print(f'sympy={sp.__version__}')
print('I_eps=(2d-eps,T-eps) has constant length a-Delta=2e')
print('all chamber-II support gaps reduce to 2eps-Delta>0 and Delta-eps>0 plus fixed positive constants')
print('lower active echo path r_2b o r_3a = x+Delta certified')
print('upper active echo path r_2b o r_4a o r_2b o r_3a = x+Delta-(a-Delta) certified')
print('beta_-, beta_b, beta_T are strictly nonzero')
print('piecewise map is rotation by Delta modulo a-Delta')
print('irrationality Delta/(a-Delta) uses the UFD proof in the audit, not CAS')
print('certificate scope: point-orbit strategy no-go mechanism only; no Schur-kernel verdict')
