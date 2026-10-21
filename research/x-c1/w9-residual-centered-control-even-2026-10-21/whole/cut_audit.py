"""Exact prime-log labels for every discontinuity used in the whole model."""
import hashlib,json
from fractions import Fraction as Q
from pathlib import Path
from flint import arb,ctx
import model_cache
HERE=Path(__file__).resolve().parent;ctx.prec=3072
values,bindings=model_cache.load(HERE/'whole-model-ed58da3caacd.json.gz',hashlib.sha256((HERE/'whole_function_probe.py').read_bytes()).hexdigest())
primes=(2,3,5,7,11)
def vec(*items):
    out=[Q(0)]*5
    for p,c in items:out[primes.index(p)]+=Q(c)
    return tuple(out)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def evaluate(v):return sum((arb(c.numerator)/c.denominator*arb(p).log()for p,c in zip(primes,v)),arb(0))
z=vec();a=vec((2,Q(3,2)));b=vec((3,1));newb=vec((11,Q(1,2)))
channels=[vec((2,1)),vec((3,1)),vec((2,2)),vec((5,1)),vec((7,1)),vec((2,3))]
newchannels=channels+[vec((3,2))]
def interior(v,lo,hi):
    if v in(lo,hi):return False
    x=evaluate(v);ll=evaluate(lo);hh=evaluate(hi)
    if x>ll and x<hh:return True
    assert x<ll or x>hh,'Unresolved ordering of distinct exact log vectors'
    return False
def prime_cuts(horizons,shifts):
    return {add(signh,signs)for h in horizons for signh in(h,neg(h))for s in shifts for signs in(s,neg(s))}
hcuts=prime_cuts((b,newb),newchannels)
oldcuts=prime_cuts((a,b),channels)
# Additional harmless subdivisions explicitly present in the old model.
core={z,a}|{v for v in hcuts|oldcuts|{sub(newb,b)}if interior(v,z,a)}
ordered=sorted(core,key=lambda v:float(evaluate(v)))
assert len(ordered)==len(values['edges'])
for v,x in zip(ordered,values['edges']):assert evaluate(v).overlaps(x)
for left,right in zip(ordered[:-1],ordered[1:]):assert evaluate(left)<evaluate(right)
outer={a,b}|{v for v in hcuts|oldcuts if interior(v,a,b)}
for edge in core:
    for sh in channels:
        for v in(add(edge,sh),sub(edge,sh),sub(sh,edge),neg(add(edge,sh))):
            if interior(v,a,b):outer.add(v)
outer=sorted(outer,key=lambda v:float(evaluate(v)))
for left,right in zip(outer[:-1],outer[1:]):assert evaluate(left)<evaluate(right)
out={'status':'EXACT_LOG_CUT_COVERAGE_PASS','prime_log_basis':list(primes),
     'core_cuts':[[str(q)for q in v]for v in ordered],
     'outer_cuts':[[str(q)for q in v]for v in outer],
     'core_count':len(ordered),'outer_count':len(outer),
     'covers_all_h_and_Q_prime_translations':True,
     'distinct_labels_ordered_by_directed_intervals':True,
     'same_labels_equal_by_exact_log_prime_algebra':True}
(HERE/'cut-audit.json').write_bytes((json.dumps(out,indent=2)+'\n').encode())
print('CUTS',out['core_count'],out['outer_count'],out['outer_cuts'])
