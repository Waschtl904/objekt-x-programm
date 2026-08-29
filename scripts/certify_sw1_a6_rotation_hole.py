#!/usr/bin/env python3
import sympy as sp

L2,L3=sp.log(2),sp.log(3)
a=L2/2; b=L3/2; T=2*a; d=b-a; e=T-b; Delta=sp.simplify(d-e)
L=sp.simplify(a-Delta)
eps=sp.symbols('eps', positive=True)

A=sp.simplify(2*d-eps)
B=sp.simplify(T-eps)
D=sp.simplify(B-Delta)
C=sp.simplify(T+eps-Delta)

assert sp.simplify(B-A-L)==0
assert sp.simplify(C-D-2*eps)==0
assert sp.simplify(B-C-(Delta-2*eps))==0
assert sp.simplify(D-A-(L-Delta))==0

# Lower branch composition.
x=sp.symbols('x', real=True)
low=sp.simplify(2*b-(3*a-x))
assert sp.simplify(low-(x+Delta))==0

# Wrap composition.
wrap=sp.simplify(2*b-(4*a-(2*b-(3*a-x))))
assert sp.simplify(wrap-(x+Delta-L))==0

# Hole image under r_3a is exactly R4I=(a+eps,2d-eps).
hole_im_lo=sp.simplify(3*a-B)
hole_im_hi=sp.simplify(3*a-C)
assert sp.simplify(hole_im_lo-(a+eps))==0
assert sp.simplify(hole_im_hi-(2*d-eps))==0

# Formal next rotation value is beyond T0 throughout the open hole.
T0=T+eps
assert sp.simplify((C+Delta)-T0)==0
assert sp.simplify((B+Delta)-T0-(Delta-2*eps))==0

# Chamber boundary: hole length collapses exactly at eps=Delta/2.
assert sp.simplify((Delta-2*eps).subs(eps,Delta/2))==0

print('SW1-A6 ROTATION-HOLE AFFINE CERTIFICATE: PASS')
print(f'sympy={sp.__version__}')
print('I_epsilon has length L=a-Delta')
print('lower branch x->x+Delta certified')
print('wrap branch x->x+Delta-L certified')
print('hole maps exactly into A1-R4I where the word-11 return is absent')
print('hole length Delta-2eps and collapse at eps=Delta/2 certified')
print('finite-component conclusion uses irrational-rotation minimality in the audit')
print('scope: contracted A4 rotation subgraph only; bypass edges remain open')
