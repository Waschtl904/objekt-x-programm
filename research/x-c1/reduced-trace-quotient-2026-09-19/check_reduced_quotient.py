#!/usr/bin/env python3
"""Exact algebra regressions for the trace-quotient coordinate theorem.

The Hilbert/form-domain theorem is in PROOF.md.  This checker verifies the
finite algebra of the gauge map and the published scalar constant conversion.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json

checks=[]
def ok(name, cond):
    assert cond, name
    checks.append(name)

# A rational finite-dimensional model of the quotient algebra.
psi=(F(1),F(2),F(1))
psi2=sum(x*x for x in psi)
e=(F(1),F(0),F(0))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def smul(c,a): return tuple(c*x for x in a)
def sub(a,b): return add(a,smul(-1,b))

def reduce_pair(w,z):
    c=dot(w,psi)/psi2
    w0=sub(w,smul(c,psi))
    z0=add(z,smul(c,e))
    return w0,z0,c

vectors=[
    ((F(3),F(-1),F(4)),(F(2),F(5),F(-3))),
    ((F(-7),F(2),F(1)),(F(0),F(3),F(9))),
    ((F(1,3),F(5,7),F(-2,5)),(F(4,9),F(-1,2),F(8,11))),
]

for idx,(w,z) in enumerate(vectors):
    w0,z0,c=reduce_pair(w,z)
    ok(f'reduced core orthogonal {idx}', dot(w0,psi)==0)
    # Gauge reconstruction: (w,z) - (w0,z0) = c*(psi,-e).
    ok(f'gauge core identity {idx}', sub(w,w0)==smul(c,psi))
    ok(f'gauge shell identity {idx}', sub(z,z0)==smul(-c,e))
    # Reduction is idempotent on the slice.
    ww,zz,cc=reduce_pair(w0,z0)
    ok(f'reduction idempotent core {idx}', ww==w0 and cc==0)
    ok(f'reduction idempotent shell {idx}', zz==z0)
    # Adding any gauge vector does not change the reduced representative.
    lam=F(idx+2,idx+3)
    wg=add(w,smul(-lam,psi)); zg=add(z,smul(lam,e))
    wg0,zg0,_=reduce_pair(wg,zg)
    ok(f'gauge invariance {idx}', wg0==w0 and zg0==z0)

# Kernel generator reduces to zero.
w0,z0,c=reduce_pair(smul(-1,psi),e)
ok('kernel generator reduces to zero', w0==(F(0),)*3 and z0==(F(0),)*3)

# Published continuation constant.
epsilon=F(1,10**13)
delta=F(1,32*10**13)
ok('shell delta below inherited epsilon', delta<epsilon)
ok('conditioning denominator exact', 65*32==2080)
base_gap=delta/F(65)
ok('reduced base gap exact', base_gap==F(1,2080*10**13))

# Exact scalar form of the inverse-free inequality with r=sqrt(theta) in [0,1].
# For rational nonnegative a,d,r, the difference is r*(sqrt(a)-sqrt(d))^2;
# use perfect-square regression cases so the identity is exact over Q.
for i,(aa,dd,rr) in enumerate([(4,9,F(1,2)),(25,1,F(3,4)),(16,16,F(7,8))]):
    sa=F(int(aa**0.5)); sd=F(int(dd**0.5))
    lhs=F(aa+dd)-2*rr*sa*sd
    rhs=(1-rr)*F(aa+dd)
    ok(f'inverse-free scalar inequality {i}', lhs-rhs==rr*(sa-sd)**2 and lhs>=rhs)

res={
  'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
  'checks':len(checks),
  'gauge_kernel':'span{(-psi,e)}',
  'reduced_core':'L2-orthogonal complement of psi',
  'epsilon':str(epsilon),
  'delta':str(delta),
  'base_gap_before_(1-sqrt(theta))':str(base_gap),
  'note':'Exact finite algebra regressions only; the quotient/form-domain theorem is analytic in PROOF.md.'
}
log='\n'.join('PASS '+x for x in checks)+'\nTOTAL '+str(len(checks))+'\n'
jsontext=json.dumps(res,indent=2,sort_keys=True)+'\n'
root=Path(__file__).resolve().parent

if __name__=='__main__':
    p=argparse.ArgumentParser(); g=p.add_mutually_exclusive_group(); g.add_argument('--write',action='store_true'); g.add_argument('--verify',action='store_true'); args=p.parse_args()
    if args.write:
        (root/'reduced_quotient_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
        (root/'reduced_quotient_checks.log').write_text(log,encoding='utf-8',newline='\n')
        payload=['PROOF.md','README.md','check_reduced_quotient.py','reduced_quotient_checks.log','reduced_quotient_results.json']
        manifest=''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in payload)
        (root/'SHA256SUMS').write_text(manifest,encoding='ascii',newline='\n')
    if args.verify:
        assert (root/'reduced_quotient_results.json').read_bytes()==jsontext.encode()
        assert (root/'reduced_quotient_checks.log').read_bytes()==log.encode()
        for line in (root/'SHA256SUMS').read_text().splitlines():
            d,n=line.split('  ',1); assert hashlib.sha256((root/n).read_bytes()).hexdigest()==d,n
        print('REPLAY and all payload SHA256 hashes PASS')
    print(log,end='')
