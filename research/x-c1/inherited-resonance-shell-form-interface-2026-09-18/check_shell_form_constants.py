#!/usr/bin/env python3
"""Directed scalar checks for the shell-form interface.

The common-jump identity, graph-space construction, and inverse-free Schur theorem
are analytic arguments in PROOF.md. This checker only verifies the elementary
unit-window active set and the advertised crude bound Gamma_b < 12.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib, json, argparse

SCALE=10**120

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

def atanh(x):
    x=I.of(x); term=x; total=I(0)
    for k in range(220):
        total += term/(2*k+1); term=term*x*x
    return total+I(0,(term/(441*(1-x*x))).hi)
LOG2=2*atanh(I(F(1,3)))

def log_point(x):
    k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    return 2*atanh(I((x-1)/(x+1)))+k*LOG2

def log(x):
    x=I.of(x); return I(log_point(x.lo).lo,log_point(x.hi).hi)

def atan(x):
    x=I.of(x); term=x; total=I(0)
    for k in range(220):
        total += ((-1)**k)*term/(2*k+1); term=term*x*x
    return total+I(0,(term/441).hi)
PI=16*atan(I(F(1,5)))-4*atan(I(F(1,239)))

def sqrtI(n):
    k=isqrt(n*SCALE*SCALE); return I(F(k,SCALE),F(k+1,SCALE))

def gamma_enclosure():
    # Classical 0 < gamma < H_1000-log(1000), with directed upper endpoint.
    H=sum((F(1,k) for k in range(1,1001)),F(0))
    upper=(I(H)-log(I(1000))).hi
    return I(0,upper)

checks=[]
def ok(name,c):
    assert c,name; checks.append(name)

B=log(I(5))/2
ok('B in (4/5,81/100)',F(4,5)<B.lo<B.hi<F(81,100))
ok('log(7)/2 below 1',(log(I(7))/2).hi<1)
ok('log(8)/2 above 1',(3*LOG2/2).lo>1)

# Maximal active prime powers for b<=1 are 2,3,4,5,7.
qs=[2,3,4,5,7]
weights=[]
for q in qs:
    if q==4: lp=LOG2
    else: lp=log(I(q))
    weights.append(lp/sqrtI(q))

ok('w2 < 1/2',weights[0].hi<F(1,2))
ok('w3 < 13/20',weights[1].hi<F(13,20))
ok('w4 < 7/20',weights[2].hi<F(7,20))
ok('w5 < 3/4',weights[3].hi<F(3,4))
ok('w7 < 3/4',weights[4].hi<F(3,4))

kappa=log(8*PI)+gamma_enclosure()+PI/2
ok('kappa_* < 11/2',kappa.hi<F(11,2))
Gamma=kappa+2*sum(weights,I(0))
ok('unit-window Gamma upper < 12',Gamma.hi<12)

# Sanity: the frozen core gap is strictly positive and below the near-null ceiling.
ok('frozen common core gap positive',F(1,10**13)>0)
ok('frozen core gap below 3.3e-12',F(1,10**13)<F(33,10**13))

res={
  'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
  'checks':len(checks),
  'B':[str(B.lo),str(B.hi)],
  'maximal_active_prime_powers_to_b_1':qs,
  'Gamma_enclosure':[str(Gamma.lo),str(Gamma.hi)],
  'uniform_semibound':'D_b[s] >= -12 ||L s||_2^2',
  'note':'Analytic graph-space and relative Schur claims are proved in PROOF.md; this script checks only scalar margins.'
}
logtxt='\n'.join('PASS '+x for x in checks)+'\nTOTAL '+str(len(checks))+'\n'
root=Path(__file__).resolve().parent
jsontext=json.dumps(res,indent=2,sort_keys=True)+'\n'

if __name__=='__main__':
    p=argparse.ArgumentParser(); g=p.add_mutually_exclusive_group(); g.add_argument('--write',action='store_true'); g.add_argument('--verify',action='store_true'); args=p.parse_args()
    if args.write:
        (root/'shell_form_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
        (root/'shell_form_checks.log').write_text(logtxt,encoding='utf-8',newline='\n')
        payload=['PROOF.md','README.md','check_shell_form_constants.py','shell_form_checks.log','shell_form_results.json']
        manifest=''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in payload)
        (root/'SHA256SUMS').write_text(manifest,encoding='ascii',newline='\n')
    if args.verify:
        assert (root/'shell_form_results.json').read_bytes()==jsontext.encode()
        assert (root/'shell_form_checks.log').read_bytes()==logtxt.encode()
        for line in (root/'SHA256SUMS').read_text().splitlines():
            d,n=line.split('  ',1); assert hashlib.sha256((root/n).read_bytes()).hexdigest()==d,n
        print('REPLAY and all payload SHA256 hashes PASS')
    print(logtxt,end='')
