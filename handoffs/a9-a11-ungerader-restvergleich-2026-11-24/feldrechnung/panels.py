"""Directed Taylor enclosures of specified compact subintervals of the stored odd model."""
import argparse, hashlib, json, sys, time
from pathlib import Path
from types import ModuleType
from flint import acb, arb, arb_mat, arb_poly, arb_series, ctx

def checked_module(path, changes):
    raw=path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=="8b7a7234698878fc9aa1c0ef03b8e20de9f29361d151ebe0f3517b0ae74d26e6"
    src=raw.decode().replace("\r\n","\n")
    for before,after in changes:
        assert before in src,before
        src=src.replace(before,after)
    mod=ModuleType("odd_taylor")
    exec(compile(src,str(path), "exec"),mod.__dict__)
    return mod

ap=argparse.ArgumentParser()
ap.add_argument("root",type=Path)
ap.add_argument("cache",type=Path)
ap.add_argument("output",type=Path)
ap.add_argument("depth",type=int)
args=ap.parse_args()
start=time.monotonic()
src=args.root/"research/x-c1/w9-partial-energy-2026-10-18"
vendor=args.root/"research/x-c1/w9-residual-centered-control-even-2026-10-21/whole"
sys.path[:0]=[str(src),str(vendor)]
import common as c, residuals as resmod, old_fields as of, model_cache, fast_evaluation
from common import q
ctx.prec=3072
inps=c.Inputs()
res=resmod.Residuals(inps,"odd")
leg=res.legs
source=Path(__file__).with_name("odd_field_control.py")
values,bindings=model_cache.load(args.cache,hashlib.sha256(source.read_bytes()).hexdigest())
assert bindings=={k:hashlib.sha256(v).hexdigest() for k,v in inps.data.items()}
globals().update(values)
code=source.read_text(encoding="utf8")
exec(code[code.index("def evaluate("):code.index("def qmprime(")])
exec(code[code.index("# Cauchy integrals of polynomial"):code.index("print('Whole function ready'")])
_fast=fast_evaluation.install(globals())

def poly_sup(p,lo,hi):
    if not len(p): return arb(0)
    rounded=p(arb_poly([(lo+hi)/2,(hi-lo)/2]))
    integ=c.pint(rounded*rounded,arb(-1),arb(1))/2
    assert integ.upper()>=0
    return len(p)*integ.upper().sqrt()
# The four permitted real logarithms each have absolute integral below 10.
cauchy_l1=sum(((1 if tag is None else 10)*poly_sup(p,arb(0),arb(1))
               for tag,p in outerstatic.items()),arb(0))
for p,(ll,hh) in zip(upp,cells):
    cauchy_l1+=(roots[hh]-roots[ll])*poly_sup(p,roots[ll],roots[hh])
shell_l1=hs*poly_sup(sp,arb(-1),arb(1))
tm=checked_module(vendor/"taylor_model.py",[
    ("(ep+1/ep)/2","(ep-1/ep)/2"),("+1/ep*(jm(a-x)+jp(a+x))","-1/ep*(jm(a-x)+jp(a+x))"),
    ("+peval(model['ell'],-x)*logp+peval(model['quot'],-x)","-peval(model['ell'],-x)*logp-peval(model['quot'],-x)"),
    ("else peval(model['ell'],-x-sh)","else -peval(model['ell'],-x-sh)"),
    ("        return ans\n","        gap=z.b.real.lower()-1 if z.b.real>1 else -z.b.real.upper()\n        assert gap>0\n        ans.b=acb(arb(0,(ns['cauchy_l1']/gap).upper()),arb(0,(ns['cauchy_l1']/gap).upper()))\n        return ans\n"),
    ("    val-=shellc/2+peval(ns['selfreg'],u)+peval(ns['reflectreg'],x)",
     "    shellmax=(ns['shell_l1']/(a+x.b.real.lower())).upper()\n    shellc.b=acb(arb(0,shellmax),arb(0,shellmax))\n    val+=shellc/2-peval(ns['selfreg'],u)+peval(ns['reflectreg'],x)"),
    ("cauchy(s)-cauchy(-s)","cauchy(s)+cauchy(-s)"),
    ("for shift in(-y,y):","for shift,weight in ((-y,wh),(y,-wh)):"),
    ("term=wh/den","term=weight/den"),("measure_ball+=wh/(x.b+shift)","measure_ball+=weight/(x.b+shift)"),
    ("if ay.s[0]<a:val-=wt*(core(ay)-ns['lm']/mu*moment(ay))","sign_y=1 if yy.s[0]>=0 else -1\n            if ay.s[0]<a:val-=sign_y*wt*(core(ay)-ns['lm']/mu*moment(ay))"),
    ("val-=wt*peval(ns['spx'],ay)","val-=sign_y*wt*peval(ns['spx'],ay)")
])
cuts=list(res.cuts)
for edge in edges:
    for sh,_ in channels: cuts.extend([edge+sh,edge-sh,sh-edge,-edge-sh])
outer_edges=[a]
for x in sorted((v for v in cuts if a<v<b),key=float):
    if not x.overlaps(outer_edges[-1]): outer_edges.append(x)
outer_edges.append(b)
panels=[]
for i,(l,r) in enumerate(zip(outer_edges[:-1],outer_edges[1:])):
    if i in (0,len(outer_edges)-2):
        for k in range(1,args.depth+1):
            if i==0: panels.append((l+(r-l)/2**k,l+(r-l)/2**(k-1)))
            else: panels.append((r-(r-l)/2**(k-1),r-(r-l)/2**k))
    else: panels.append((l,r))
result={"cache_sha256":hashlib.sha256(args.cache.read_bytes()).hexdigest(),"panels":[],
        "truncated_at_both_endpoints":True,"whole_model_certified":False,"physical_residual_certified":False}
total=arb(0);length=arb(0)
for i,(left,right) in enumerate(panels):
    preview=tm.build(globals(),left,right,4)
    # Allocate 1e-7 in X-norm to each interior Taylor remainder.
    M=preview['contour_bound']; eps=q('1e-7')/((right-left)*2).sqrt()
    import math
    N=max(32,math.ceil(float((M/eps).log()/arb(2).log()))+12)
    N=((N+15)//16)*16
    assert N<=1536
    v=tm.build(globals(),left,right,N)
    control=abs(v['polynomial'](0)-outer_value((left+right)/2)).upper()
    assert control<q("1e-15") and ((right-left)*2).sqrt()*v["taylor_error"]<q("1e-7")
    total+=v["model_Xnorm_squared_upper"];length+=right-left
    result["panels"].append(dict(left=c.enc(left),right=c.enc(right),order=v["order"],
        upper=c.enc(v['model_Xnorm_squared_upper'])[1],midpoint_control=c.enc(control)[1]))
    result["interior_model_X_squared_upper"]=c.enc(total)[1]
    result["fraction_covered"]=c.enc(length/hs)
    args.output.write_text(json.dumps(result,indent=2),encoding="utf8")
    print("CERTIFIED MODEL PANEL",i+1,len(panels),N,float(total.upper()),round(time.monotonic()-start,1),flush=True)
