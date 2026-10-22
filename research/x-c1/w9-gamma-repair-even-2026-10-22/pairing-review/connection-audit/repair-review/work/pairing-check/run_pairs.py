"""Read-only 84-coordinate diagnostic. No quadrature remainder is assumed zero."""
from pathlib import Path
import sys,json,time,hashlib,contextlib,io
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE/'deps'))
from flint import arb,arb_mat,arb_poly,acb,ctx
ROOT=(BASE/'snapshot').resolve()
ORIGINAL=BASE.parent/'repo/research/x-c1/w9-residual-centered-control-even-2026-10-21'
WHOLE=ORIGINAL/'whole'
sys.path.insert(0,str(WHOLE))
start=time.monotonic()
code=(WHOLE/'probe.py').read_text(encoding='utf-8').split('# Midpoint-only trade-off')[0]
old="ROOT = Path(__file__).resolve().parents[1] / 'objekt-x-integration-20261019'"
assert code.count(old)==1
code=code.replace(old,'ROOT = Path('+repr(str(ROOT))+')')
ns={'__file__':str(WHOLE/'probe.py'),'__name__':'bound_reference'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(code,str(WHOLE/'probe.py'),'exec'),ns)
c=ns['c'];enc=c.enc
reference=ns['nmodel']
data={'status':'DIAGNOSTIC_ONLY','reference':[enc(reference[i,0]) for i in range(84)],'reference_definition':'nu-H0*w+eta*DJ*w','eta':'1/10000000000','elapsed':time.monotonic()-start}
(BASE/'reference.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('REFERENCE_READY',round(time.monotonic()-start,2),flush=True)
ctx.prec=3072
src=ROOT/'research/x-c1/w9-partial-energy-2026-10-18'
resmod=ns['module']('residuals',src/'residuals.py');of=ns['module']('old_fields',src/'old_fields.py')
res=resmod.Residuals(ns['env']['inp'],'even')
import model_cache
values,bindings=model_cache.load(BASE.parent/'research-review/data/whole-model-ed58da3caacd.json.gz',hashlib.sha256((WHOLE/'whole_function_probe.py').read_bytes()).hexdigest())
assert bindings=={name:hashlib.sha256(raw).hexdigest() for name,raw in ns['env']['inp'].data.items()}
ns.update(values);ns.update(res=res,leg=res.legs,of=of,arb_poly=arb_poly,acb=acb)
ns['hfun']=lambda fun,x:sum((z*v for z,v in zip(values['cc'],fun(x))),arb(0))
def evaluate(parts,t):
    ans=parts.get(None,arb_poly([]))(t)
    for tag,p in parts.items():
        if tag is not None:ans+=p(t)*abs(t-ns['rootvalues'][tag]).log()
    return ans
ns['evaluate']=evaluate
source=(WHOLE/'whole_function_probe.py').read_text(encoding='utf-8')
tail=source[source.index('# Cauchy integrals'):source.index("print('Whole function ready'")]
exec(compile(tail,'published_function_evaluation','exec'),ns)
import fast_evaluation
ns['_fast']=fast_evaluation.install(ns)
print('FUNCTION_READY',round(time.monotonic()-start,2),flush=True)
a,b,hs,mid,half,J=(ns[x] for x in ('a','b','hs','mid','half','J'))
# Coarse signed quadrature for diagnosis only. All cells respect prime cuts.
cuts=[]
for edge in ns['edges']:
    for sh,wt in ns['channels']:
        cuts.extend(x for x in (edge+sh,edge-sh,sh-edge,-edge-sh) if a<x<b)
cuts.extend(x for x in res.cuts if a<x<b);cuts.sort(key=float)
oe=[a]
for x in cuts:
    if not x.overlaps(oe[-1]):oe.append(x)
oe.append(b)
pan=[]
for i,(lo,hi) in enumerate(zip(oe[:-1],oe[1:])):
    if i==0:
        pan.extend((lo+(hi-lo)*arb(2)**(-k-1),lo+(hi-lo)*arb(2)**(-k)) for k in range(20))
    elif i==len(oe)-2:
        pan.extend((hi-(hi-lo)*arb(2)**(-k),hi-(hi-lo)*arb(2)**(-k-1)) for k in range(20))
    else:pan.append((lo,hi))
mom=arb_mat(96,1);nodes={};npoints=0
for i,(lo,hi) in enumerate(pan):
    if time.monotonic()-start>900:raise RuntimeError('Bounded diagnostic time limit reached')
    n=24 if hi-lo>=hs/64 else 12
    if n not in nodes:nodes[n]=[arb.legendre_p_root(n,k,weight=True) for k in range(n)]
    for z,wt in nodes[n]:
        x=(lo+hi)/2+(hi-lo)*z/2;ww=(hi-lo)*wt/2
        rr=ns['outer_value'](x);assert rr.is_finite()
        u=(x-mid)/half;pol=[arb(1),u]
        for k in range(1,95):pol.append(((2*k+1)*u*pol[-1]-k*pol[-2])/(k+1))
        for k in range(96):mom[k,0]+=2*ww*rr*pol[k]*(arb(2*k+1)/(2*hs)).sqrt()
        npoints+=1
    if i%5==0:print('DIAGNOSTIC_PANEL',i+1,len(pan),'seconds',round(time.monotonic()-start,2),flush=True)
reconstructed=J.transpose()*mom
rows=[]
for i in range(84):
    d=reconstructed[i,0]-reference[i,0]
    rows.append({'coordinate':i+1,'reference_arithmetic_interval':enc(reference[i,0]),'reconstructed_quadrature_arithmetic_interval':enc(reconstructed[i,0]),'diagnostic_difference_arithmetic_interval':enc(d),'quadrature_remainder_certified':False,'status':'UNRESOLVED_PENDING_DIRECTED_PAIRING_REMAINDER'})
out={'status':'UNRESOLVED','reason':'Signed quadrature is independent of the stored finite pairing matrices but its discretization and omitted endpoint remainders are not certified here. Arithmetic balls alone are not integral enclosures.','rows':rows,'points':npoints,'panels':len(pan),'elapsed_seconds':time.monotonic()-start,'maximum_absolute_diagnostic_difference':max(float(abs(reconstructed[i,0]-reference[i,0]).upper()) for i in range(84))}
(BASE/'diagnostic.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
# Save sufficient models for componentwise error attribution without reloading.
model_cache.save(BASE/'pairing-model.json.gz',{k:ns[k] for k in ('nmodel','Pup','DJ','ea_direction','err_nu','err_D','err_U','err_square','Ki','a','w')}|{'J':J,'GJ':ns['GJ'],'reconstructed':reconstructed},hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),bindings)
print('DIAGNOSTIC_DONE',out['maximum_absolute_diagnostic_difference'],'seconds',round(out['elapsed_seconds'],2),flush=True)
