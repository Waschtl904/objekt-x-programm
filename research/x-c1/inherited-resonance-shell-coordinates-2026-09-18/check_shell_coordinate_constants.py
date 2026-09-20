#!/usr/bin/env python3
"""Directed constant checks for the shell-coordinate lemmas.

The functional-analytic density, trace, surjectivity and direct-sum proofs are
in PROOF.md. This script only checks the closed-form constants and the stated
uniform numerical margins; it is not a substitute for those proofs.
"""
from fractions import Fraction as F
from math import isqrt
import hashlib, json
from pathlib import Path

SCALE=10**100

def down(x):
    x=F(x); return F((x.numerator*SCALE)//x.denominator,SCALE)
def up(x):
    x=F(x); return -down(-x)

class I:
    def __init__(self,lo,hi=None):
        self.lo=down(lo); self.hi=up(lo if hi is None else hi); assert self.lo<=self.hi
    @staticmethod
    def of(x): return x if isinstance(x,I) else I(x)
    def __add__(self,o):
        o=I.of(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-I.of(o))
    def __rsub__(self,o): return I.of(o)+(-self)
    def __mul__(self,o):
        o=I.of(o); v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]; return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=I.of(o); assert o.lo>0 or o.hi<0; return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return I.of(o)/self
    def __pow__(self,n):
        r=I(1)
        for _ in range(n): r=r*self
        return r

def atanh(x):
    x=I.of(x); term=x; total=I(0)
    for k in range(180):
        total += term/(2*k+1); term=term*x*x
    return total+I(0,(term/(361*(1-x*x))).hi)
LOG2=2*atanh(I(F(1,3)))

def log_point(x):
    k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    return 2*atanh(I((x-1)/(x+1)))+k*LOG2

def log(x):
    x=I.of(x); return I(log_point(x.lo).lo,log_point(x.hi).hi)

def exp_pos(x):
    x=I.of(x); term=total=I(1)
    for k in range(1,180):
        term=term*x/k; total+=term
    following=term*x/180
    return total+I(0,(following/(1-x/181)).hi)

def sinh(x):
    x=I.of(x); ep=exp_pos(x); em=1/ep; return (ep-em)/2

def cosh(x):
    x=I.of(x); ep=exp_pos(x); em=1/ep; return (ep+em)/2

def atan(x):
    x=I.of(x); term=x; total=I(0)
    for k in range(180):
        total += ((-1)**k)*term/(2*k+1); term=term*x*x
    return total+I(0,(term/361).hi)
PI=16*atan(I(F(1,5)))-4*atan(I(F(1,239)))

def show(x):
    x=I.of(x)
    return [float(x.lo),float(x.hi)]

checks=[]
def ok(name,cond):
    assert cond,name; checks.append(name)

B=log(I(5))/2
h0=1-B
HB=cosh(B/2)
A0=(B+sinh(B))/2
MB=4*(HB-1)/B
AT=A0/HB
Hmax=cosh(I(F(1,2)))
Calpha=Hmax/(PI*A0)
CT2=(3*B+5*sinh(B))/(8*HB*HB)
CM2=B/3+1/B
Cgamma=(AT+Hmax*h0/I.of(2)**0) # placeholder overwritten below
# sqrt(2) directed
k=isqrt(2*SCALE*SCALE); sqrt2=I(F(k,SCALE),F(k+1,SCALE))
Cgamma=(AT+Hmax*h0/sqrt2)/MB

ok('B lies strictly between 4/5 and 81/100',F(4,5)<B.lo<B.hi<F(81,100))
ok('unit endpoint leaves positive shell width',h0.lo>0)
ok('H(B)>1',HB.lo>1)
ok('A_B positive and > 4/5',A0.lo>F(4,5))
ok('M_B positive and > 2/5',MB.lo>F(2,5))
ok('A_T positive',AT.lo>0)
ok('orthogonal alpha constant < 43/100',Calpha.hi<F(43,100))
ok('phi_T H1 norm squared positive',CT2.lo>0)
ok('phi_M H1 norm squared positive',CM2.lo>0)
ok('uniform gamma coefficient < 231/100',Cgamma.hi<F(231,100))

# Closed-form identity for M_B is independently checked by evaluating the
# antiderivatives: int H = 2 sinh(B/2), int xH = 2B sinh(B/2)-4H_B+4.
M_direct=2*sinh(B/2)-(2*B*sinh(B/2)-4*HB+4)/B
ok('closed-form Mellin corrector mass identity',
   M_direct.lo<=MB.lo<=MB.hi<=M_direct.hi)

res={
  'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
  'checks':len(checks),
  'B':show(B),'h_max_to_unit_window':show(h0),'H_B':show(HB),
  'A_B':show(A0),'M_B':show(MB),'A_T':show(AT),
  'C_alpha_upper':show(Calpha),'C_gamma_upper':show(Cgamma),
  'note':'Numeric directed checks support only the closed-form constants; analytic source-space lemmas are proved in PROOF.md.'
}
log='\n'.join('PASS '+x for x in checks)+'\nTOTAL '+str(len(checks))+'\n'
root=Path(__file__).resolve().parent
jsontext=json.dumps(res,indent=2,sort_keys=True)+'\n'
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(); m=p.add_mutually_exclusive_group(); m.add_argument('--write',action='store_true'); m.add_argument('--verify',action='store_true'); args=p.parse_args()
    if args.write:
        (root/'shell_coordinate_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
        (root/'shell_coordinate_checks.log').write_text(log,encoding='utf-8',newline='\n')
        payload=['PROOF.md','README.md','check_shell_coordinate_constants.py','shell_coordinate_checks.log','shell_coordinate_results.json']
        manifest=''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in payload)
        (root/'SHA256SUMS').write_text(manifest,encoding='ascii',newline='\n')
    if args.verify:
        assert (root/'shell_coordinate_results.json').read_bytes()==jsontext.encode()
        assert (root/'shell_coordinate_checks.log').read_bytes()==log.encode()
        for line in (root/'SHA256SUMS').read_text().splitlines():
            d,n=line.split('  ',1); assert hashlib.sha256((root/n).read_bytes()).hexdigest()==d,n
        print('REPLAY and all payload SHA256 hashes PASS')
    print(log,end='')
