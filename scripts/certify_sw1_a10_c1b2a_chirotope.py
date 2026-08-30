#!/usr/bin/env python3
"""SW1-A10-C1B2A exact chirotope-constancy certificate on 3<r<4.

The 18 collision hyperplanes and 4 simplex facets are represented by the
oriented augmented rows (a1,a2,a3,-b(r)) of a.x=b(r).  Since r occurs only in
the last column, every 4x4 minor is affine-linear in r.  The certificate
enumerates all C(22,4)=7315 minors exactly, classifies identically-zero,
constant, and genuinely linear minors, and proves that no nonzero minor has a
root in the open interval (3,4).  Hence the rank-4 chirotope is constant there.

Scope:
- exact finite chirotope/oriented-matroid constancy for the 22-object affine
  arrangement, including all simplex-facet interactions;
- this is the finite algebraic premise for the standard arrangement-isotopy
  transfer; the topological isotopy lemma is a separate mathematical step;
- no Cross-Gram injectivity claim.
"""
from itertools import combinations
import hashlib
import sympy as sp

r=sp.symbols('r')
H=[]
def hp(name,a,b0=0,b1=0):
    H.append((name,sp.Matrix([sp.Rational(x) for x in a]),
              sp.Rational(b0)+sp.Rational(b1)*r))

# 18 collision planes.
hp('A_2R',[0,2,0],0,1); hp('A_R+e',[0,1,1],0,1); hp('A_R+s',[1,1,0],0,1)
hp('A_2e',[0,0,2],0,1); hp('A_e+s',[1,0,1],0,1); hp('A_2s',[2,0,0],0,1)
hp('B_e-R',[0,-1,1],1,0); hp('B_s',[1,0,0],1,0); hp('B_2s',[2,0,0],1,0)
hp('B_e-s',[-1,0,1],1,0); hp('B_e',[0,0,1],1,0); hp('B_e+s',[1,0,1],1,0)
hp('B_2e',[0,0,2],1,0); hp('B_R-s',[-1,1,0],1,0); hp('B_R',[0,1,0],1,0)
hp('B_R+s',[1,1,0],1,0); hp('B_R+e',[0,1,1],1,0); hp('B_2R',[0,2,0],1,0)

# 4 oriented simplex facets for 0<sigma<R<epsilon<(r+1)/2.
hp('D_s0',[1,0,0],0,0)
hp('D_R=s',[-1,1,0],0,0)
hp('D_e=R',[0,-1,1],0,0)
hp('D_e=E',[0,0,1],sp.Rational(1,2),sp.Rational(1,2))
assert len(H)==22

rows=[sp.Matrix([[a[0],a[1],a[2],-b]]) for _,a,b in H]
r0=sp.Rational(7,2)
records=[]
roots=[]
zero_count=constant_count=linear_count=0
neg_count=pos_count=0

for inds in combinations(range(22),4):
    M=sp.Matrix.vstack(*[rows[i] for i in inds])
    det=sp.factor(sp.expand(M.det()))
    if det==0:
        zero_count+=1
        kind='Z'; root=''; sign=0
    else:
        p=sp.Poly(det,r)
        assert p.degree()<=1
        sign=int(sp.sign(det.subs(r,r0)))
        assert sign in (-1,1)
        if sign<0: neg_count+=1
        else: pos_count+=1
        if p.degree()==0:
            constant_count+=1
            kind='C'; root=''
        else:
            linear_count+=1
            aa,bb=p.all_coeffs()
            rr=sp.factor(-bb/aa)
            assert rr.is_Rational
            assert not (sp.Rational(3)<rr<sp.Rational(4))
            roots.append(rr)
            root=str(rr)
        # Independent exact sign samples inside the interval.
        assert int(sp.sign(det.subs(r,sp.Rational(31,10))))==sign
        assert int(sp.sign(det.subs(r,sp.Rational(39,10))))==sign
    names=tuple(H[i][0] for i in inds)
    records.append((inds,names,str(det),kind,root,sign))

assert len(records)==sp.binomial(22,4)==7315
assert (zero_count,constant_count,linear_count)==(1652,2012,3651)
assert (neg_count,pos_count)==(2907,2756)

critical=sorted(set(roots))
EXPECTED_CRITICAL=[
    sp.Rational(-3),sp.Rational(-2),sp.Rational(-1),sp.Rational(-1,2),
    sp.Rational(0),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(2,3),
    sp.Rational(1),sp.Rational(4,3),sp.Rational(3,2),sp.Rational(2),
    sp.Rational(5,2),sp.Rational(3),sp.Rational(4),sp.Rational(5),sp.Rational(6)
]
assert critical==EXPECTED_CRITICAL
assert not any(sp.Rational(3)<x<sp.Rational(4) for x in critical)

# The chosen simplex side stays nonempty throughout 3<r<4: this fixed point
# lies strictly inside 0<sigma<R<epsilon<(r+1)/2 for the whole interval.
sigma0,R0,eps0=sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4)
assert 0<sigma0<R0<eps0<sp.Rational(2)  # (r+1)/2 > 2 when r>3.

payload='\n'.join('|'.join(map(str,rec)) for rec in records).encode()
sign_payload=''.join('+' if rec[-1]==1 else '-' if rec[-1]==-1 else '0' for rec in records).encode()
root_payload='\n'.join(map(str,critical)).encode()
ledger_digest=hashlib.sha256(payload).hexdigest()
sign_digest=hashlib.sha256(sign_payload).hexdigest()
root_digest=hashlib.sha256(root_payload).hexdigest()
assert ledger_digest=='55a082bc5079dcca74fadf8cd8d4be875bd99f5ff3d2e9dac568e7ab82a5bded'
assert sign_digest=='a442d13d7a368d931ac890098131bdbdbd7b5a4e02a2c7372c6c3b1cc1ddc1ac'
assert root_digest=='27267468d5d217db17e6123b6a95254ffa885057e5f6bee9a79fca2b4f1c398b'

print('SW1-A10-C1B2A CHIROTOPE CONSTANCY CERTIFICATE: PASS')
print('22 objects; 4x4 minors:',len(records))
print('minor classes: 1652 identically zero, 2012 constant nonzero, 3651 affine-linear')
print('nonzero signs at r0=7/2: 2907 negative, 2756 positive')
print('exact critical-root set:',','.join(str(x) for x in critical))
print('no nonzero 4x4 minor has a root in the open interval (3,4)')
print('rank-4 chirotope is constant on 3<r<4, including simplex-facet interactions')
print('ledger SHA256:',ledger_digest)
print('sign-vector SHA256:',sign_digest)
print('critical-root SHA256:',root_digest)
print('FIREWALL: finite chirotope premise only; topological isotopy lemma and Cross-Gram injectivity are separate')
