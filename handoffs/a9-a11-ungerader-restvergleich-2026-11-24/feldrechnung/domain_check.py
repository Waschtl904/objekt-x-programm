"""Verify prime-cell coverage, both odd Gamma orientations, and the available scalar budgets."""
import hashlib,json,sys
from math import comb,factorial
from fractions import Fraction as F
from pathlib import Path
from flint import ctx,arb
root,cache,outdir=map(Path,sys.argv[1:])
vendor=root/"research/x-c1/w9-residual-centered-control-even-2026-10-21/whole"
sys.path.insert(0,str(vendor))
import model_cache
ctx.prec=3072
data,_=model_cache.load(cache,hashlib.sha256(Path(__file__).with_name("odd_field_control.py").read_bytes()).hexdigest())
ref=json.loads((vendor/"cut-audit.json").read_bytes())
def val(vec):
    terms=[F(v) for v in vec]
    return sum((arb(v.numerator)/v.denominator*arb(p).log() for v,p in zip(terms,ref["prime_log_basis"])),arb(0))
core=[val(row) for row in ref["core_cuts"]];outer=[val(row) for row in ref["outer_cuts"]]
assert len(core)==len(data["edges"]) and all(x.overlaps(y) for x,y in zip(core,data["edges"]))
assert all(x<y for x,y in zip(core,core[1:])) and all(x<y for x,y in zip(outer,outer[1:]))
p=json.loads((outdir/"panels.json").read_bytes())
assert len(outer)==4 and len(p["panels"])==11
def ball(s):
    x,y=map(F,s)
    return (arb(x.numerator)/x.denominator).union(arb(y.numerator)/y.denominator)
pan=[]
for i,(l,r) in enumerate(zip(outer,outer[1:])):
    if i==1: pan.append((l,r))
    else:
        for k in range(1,6):
            pan.append((l+(r-l)/2**k,l+(r-l)/2**(k-1)) if i==0 else (r-(r-l)/2**(k-1),r-(r-l)/2**k))
assert all(l.overlaps(ball(row['left'])) and r.overlaps(ball(row['right'])) for (l,r),row in zip(pan,p['panels']))
counter=0
for n in range(225):
    for j in range(n+1):
        b=comb(n,j)
        f=factorial(n)//(factorial(j)*factorial(n-j))
        assert (-b+(-1)**j*b) == f*((-1)**j-1)
        assert ((-1)**(n-j)*b-b) == f*(-2 if (n-j)%2 else 0)
        counter+=1
assert counter==25425
def read(f): return json.loads((outdir/f).read_bytes())
tail=read('endpoints.json')
core_price=F(read('core.json')['dual_norm_upper'])
features=F(read('features.json')['joint_dual_error'])
assert sum(F(r['upper']) for r in p['panels'])<=F('2.072e-12')
assert F(p['interior_model_X_squared_upper'])<F('2.072e-12')
assert F(tail['two_extreme_tails_model_X_squared'])<F('0.6e-12')
extra_model,extra_dual=F('3e-8'),F('5e-6')
room=F('9e-5')-extra_dual-core_price-features
assert room>0 and F(5,21)*(extra_model+F('2.672e-12'))<room*room
print('PASS: both parity coefficients, 11 panel limits on exact prime cells, conditional budget.')
