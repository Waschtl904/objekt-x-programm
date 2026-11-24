"""Rational endpoint audit for the fixed odd witness. Run in the field directory."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument("results",type=Path)
parser.add_argument("finite",type=Path)
parser.add_argument("output",type=Path)
args=parser.parse_args()
def read(name): return json.loads((args.results/name).read_bytes())
def sqrt_up(x):
    assert x>=0
    scale=10**55
    scaled=x*scale**2
    root=isqrt(scaled.numerator//scaled.denominator)
    bound=F(root+1,scale)
    assert bound*bound>=x
    return bound
def upper(x,places):
    m=10**places
    return F(-((-x.numerator*m)//x.denominator),m)
def dec(x,places):
    value=x*10**places
    assert value.denominator==1 and x>=0
    s=str(value.numerator).zfill(places+1)
    return s[:-places]+'.'+s[-places:]
def interval(row):
    lo,hi=map(F,row)
    assert lo<=hi
    return lo,hi

fbytes=args.finite.read_bytes()
assert hashlib.sha1(b'blob '+str(len(fbytes)).encode()+b'\0'+fbytes).hexdigest()=='0cd7325cfed36fb357d6c44c0f2b7e14eeb491be'
finite=json.loads(fbytes)
right,left,inside=read('right-edge.json'),read('left-edge.json'),read('panels.json')
assert right['cache_sha256']==left['cache_sha256']==inside['cache_sha256']
assert right['includes_endpoint'] and left['includes_endpoint']
assert len(inside['panels'])==11
for sy, idx in ((left,0),(right,6)):
    first=inside['panels'][idx]
    ll,lh=interval(first['left']); rl,rh=interval(first['right'])
    wl,wh=interval(sy['width'])
    assert 0<wl and (rl-lh)/16<=wh and wl<=(rh-ll)/16
assert len(left['dyadic_upper'])==left['extra_dyads'] and left['extra_dyads']>0
assert sum(F(p['upper']) for p in inside['panels']) < F('2.072e-12')
assert sum(map(F,left['dyadic_upper']))+F(left['endpoint_X_squared_upper']) < F('7e-14')
Il=F(left['X_squared_upper']); Ir=F(right['X_squared_upper']); I0=F(inside['interior_model_X_squared_upper'])
field=I0+Il+Ir
bridge=F(read('moment-bridge.json')['combined_dual'])
core=F(read('core.json')['dual_norm_upper']); force=F(read('features.json')['joint_dual_error'])
dual=sqrt_up(F(5,21)*field)+core+force+bridge
d=upper(dual**2,20)
c,beta,z=map(F,(finite['c'],finite['beta'],finite['residual_P_norm_upper']))
assert 0<c<1 and z>=0 and beta>0 and d<F('8.1e-9')
F_hi=interval(finite['F'])[1]; K_lo=interval(finite['K_P'])[0]
cost=upper(F_hi+(d/beta+z*z+2*z*sqrt_up(c*d/beta))/(1-c),18)
margin=-upper(cost-K_lo,18)
assert margin>F('7.4034e-8')
result=dict(scope='FIXED_ODD_WITNESS_UNDER_INHERITED_FORM_AND_SOURCE_CONTRACTS',
    model_X_squared_upper=dec(upper(field,20),20),
    remaining_physical_dual_upper=dec(upper(bridge,20),20),
    whole_dual_norm_upper=dec(upper(dual,15),15),whole_RL_energy_upper=dec(d,20),
    full_inverse_energy_upper=dec(cost,18),positive_margin_lower=dec(margin,18),
    external_review='OPEN',whole_quotient_certified=False,U11_constructed=False)
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,indent=2))
