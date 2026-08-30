#!/usr/bin/env python3
"""SW1-A10-C1B2A affine chirotope certificate with hyperplane at infinity.

The 22 oriented affine hyperplanes are homogenized as rows
(a1,a2,a3,-b(r)).  To distinguish the affine chart from the underlying
projective arrangement, add the fixed distinguished infinity element
  g_inf=(0,0,0,1).
The script enumerates all C(23,4)=8855 rank-4 minors exactly.

Because the spatial normals are r-independent, every new minor containing
INF is r-independent.  Hence the affine oriented-matroid data has the same
critical r-set as the 22-object projective configuration.

Scope: exact finite affine-chirotope constancy premise only.  The transfer from
constant affine oriented-matroid data to the concrete M1 chamber/circle-order
case list remains a separate mathematical step.  No injectivity claim.
"""
from itertools import combinations
import hashlib
import sympy as sp

r=sp.symbols('r')
H=[]
def hp(name,a,b0=0,b1=0):
    H.append((name,sp.Matrix([sp.Rational(x) for x in a]),
              sp.Rational(b0)+sp.Rational(b1)*r))

hp('A_2R',[0,2,0],0,1); hp('A_R+e',[0,1,1],0,1); hp('A_R+s',[1,1,0],0,1)
hp('A_2e',[0,0,2],0,1); hp('A_e+s',[1,0,1],0,1); hp('A_2s',[2,0,0],0,1)
hp('B_e-R',[0,-1,1],1,0); hp('B_s',[1,0,0],1,0); hp('B_2s',[2,0,0],1,0)
hp('B_e-s',[-1,0,1],1,0); hp('B_e',[0,0,1],1,0); hp('B_e+s',[1,0,1],1,0)
hp('B_2e',[0,0,2],1,0); hp('B_R-s',[-1,1,0],1,0); hp('B_R',[0,1,0],1,0)
hp('B_R+s',[1,1,0],1,0); hp('B_R+e',[0,1,1],1,0); hp('B_2R',[0,2,0],1,0)
hp('D_s0',[1,0,0],0,0); hp('D_R=s',[-1,1,0],0,0); hp('D_e=R',[0,-1,1],0,0)
hp('D_e=E',[0,0,1],sp.Rational(1,2),sp.Rational(1,2))
assert len(H)==22

rows=[sp.Matrix([[a[0],a[1],a[2],-b]]) for _,a,b in H]
rows.append(sp.Matrix([[0,0,0,1]]))
names=[x[0] for x in H]+['INF']
r0=sp.Rational(7,2)
records=[]; roots=[]
zero_count=constant_count=linear_count=0
neg_count=pos_count=0
inf_zero=inf_constant=inf_linear=0

for inds in combinations(range(23),4):
    det=sp.factor(sp.Matrix.vstack(*[rows[i] for i in inds]).det())
    has_inf=22 in inds
    if det==0:
        kind='Z'; root=''; sign=0; zero_count+=1
        if has_inf: inf_zero+=1
    else:
        p=sp.Poly(det,r)
        assert p.degree()<=1
        sign=int(sp.sign(det.subs(r,r0))); assert sign in (-1,1)
        if sign<0: neg_count+=1
        else: pos_count+=1
        if p.degree()==0:
            kind='C'; root=''; constant_count+=1
            if has_inf: inf_constant+=1
        else:
            kind='L'; linear_count+=1
            if has_inf: inf_linear+=1
            aa,bb=p.all_coeffs(); rr=sp.factor(-bb/aa)
            assert rr.is_Rational
            assert not (sp.Rational(3)<rr<sp.Rational(4))
            roots.append(rr); root=str(rr)
    records.append((inds,tuple(names[i] for i in inds),str(det),kind,root,sign))

assert len(records)==sp.binomial(23,4)==8855
assert (zero_count,constant_count,linear_count)==(2274,2930,3651)
assert (neg_count,pos_count)==(3400,3181)
assert (inf_zero,inf_constant,inf_linear)==(622,918,0)
assert inf_zero+inf_constant+inf_linear==sp.binomial(22,3)==1540

critical=sorted(set(roots))
EXPECTED=[sp.Rational(-3),sp.Rational(-2),sp.Rational(-1),sp.Rational(-1,2),
          sp.Rational(0),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(2,3),
          sp.Rational(1),sp.Rational(4,3),sp.Rational(3,2),sp.Rational(2),
          sp.Rational(5,2),sp.Rational(3),sp.Rational(4),sp.Rational(5),sp.Rational(6)]
assert critical==EXPECTED
assert not any(sp.Rational(3)<x<sp.Rational(4) for x in critical)

payload='\n'.join('|'.join(map(str,x)) for x in records).encode()
sign_payload=''.join('+' if x[-1]==1 else '-' if x[-1]==-1 else '0' for x in records).encode()
ledger_digest=hashlib.sha256(payload).hexdigest()
sign_digest=hashlib.sha256(sign_payload).hexdigest()
assert ledger_digest=='90e6fa2f00c35435f5821ff94020725c13b1252c7c91194eb198dc95903d1583'
assert sign_digest=='8b9e06f0e2bd3c77549d6d801098d7076391f545bc07f3cc06444bab58b6f987'

print('SW1-A10-C1B2A AFFINE CHIROTOPE CERTIFICATE: PASS')
print('23 elements including INF; 4x4 minors:',len(records))
print('minor classes: 2274 identically zero, 2930 constant nonzero, 3651 affine-linear')
print('INF-containing minors: 622 zero, 918 constant nonzero, 0 r-dependent')
print('exact critical-root set:',','.join(str(x) for x in critical))
print('no affine-chirotope degeneration occurs for 3<r<4')
print('ledger SHA256:',ledger_digest)
print('sign-vector SHA256:',sign_digest)
print('FIREWALL: affine oriented-matroid premise only; concrete transfer and injectivity remain separate')
