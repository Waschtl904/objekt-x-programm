"""Checkpointed analytic MODEL norm with explicitly provisional endpoint lemma."""
import contextlib,io,json,time,hashlib,math,os
from pathlib import Path
HERE=Path(__file__).resolve().parent
code=(HERE/'whole_model_integrate.py').read_text()
with contextlib.redirect_stdout(io.StringIO()):exec(compile(code.split('cuts=[]')[0],str(HERE/'whole_model_integrate.py'),'exec'))
import fast_evaluation,taylor_model
assert not args.fast
_fast=fast_evaluation.install(globals())
cuts=[]
for edge in edges:
    for sh,wt in channels:
        for x in(edge+sh,edge-sh,sh-edge,-edge-sh):
            if a<x<b:cuts.append(x)
for x in res.cuts:
    if a<x<b:cuts.append(x)
cuts.sort(key=float);oe=[a]
for x in cuts:
    if not x.overlaps(oe[-1]):oe.append(x)
oe.append(b)
pan=[]
for i,(lo,hi)in enumerate(zip(oe[:-1],oe[1:])):
    if i==0:
        for k in range(args.panels):pan.append((lo+(hi-lo)*arb(2)**(-k-1),lo+(hi-lo)*arb(2)**(-k)))
    elif i==len(oe)-2:
        for k in range(args.panels):pan.append((hi-(hi-lo)*arb(2)**(-k),hi-(hi-lo)*arb(2)**(-k-1)))
    else:pan.append((lo,hi))
destination=HERE/('taylor-model-panels'+args.suffix);destination.mkdir(exist_ok=True)
binding={'source':hashlib.sha256(args.source.read_bytes()).hexdigest(),
         'cache':hashlib.sha256(args.cache.read_bytes()).hexdigest(),
         'evaluator':hashlib.sha256((HERE/'taylor_model.py').read_bytes()).hexdigest(),
         'fast_evaluator':hashlib.sha256((HERE/'fast_evaluation.py').read_bytes()).hexdigest(),
         'panels':args.panels,'outer_edges':[c.enc(x)for x in oe]}
bindpath=destination/'BINDING.json'
rawbind=(json.dumps(binding,indent=2)+'\n').encode()
if bindpath.exists():assert bindpath.read_bytes()==rawbind
else:bindpath.write_bytes(rawbind)
total=arb(0)
first=int(os.environ.get('W9_PANEL_FIRST','0'))
last=int(os.environ.get('W9_PANEL_LAST',str(len(pan)-1)))
for i,(lo,hi)in enumerate(pan):
    if not first<=i<=last:continue
    path=destination/f'{i:04d}.json'
    if path.exists():
        value=json.loads(path.read_bytes());total+=q(value['model_Xnorm_squared_upper'][1]);continue
    preview=taylor_model.build(globals(),lo,hi,4)
    # Allocate a norm remainder below 1e-10 to each model panel.
    M=preview['contour_bound'];eps=q('1e-10')/(4*((hi-lo)*2).sqrt())
    n=max(128,math.ceil(float((M/eps).log()/arb(2).log()))+12)
    n=((n+31)//32)*32
    assert n<=1536,'Model Taylor order exceeds bounded protocol'
    tick=time.monotonic();value=taylor_model.build(globals(),lo,hi,n)
    assert (2*(hi-lo)).sqrt()*value['taylor_error']<q('1e-10')
    poly=value.pop('polynomial')
    control=abs(poly(0)-outer_value((lo+hi)/2)).upper()
    assert control<q('1e-15'),'Independent point check'
    record={k:(v if isinstance(v,int)else c.enc(v))for k,v in value.items()}
    record.update(index=i,lo=c.enc(lo),hi=c.enc(hi),midpoint_control=c.enc(control),seconds=time.monotonic()-tick,
                  status='DIRECTED_STORED_MODEL_PANEL_ONLY')
    with path.open('x',encoding='utf-8',newline='\n')as stream:
        stream.write(json.dumps(record,indent=2)+'\n')
    total+=q(record['model_Xnorm_squared_upper'][1])
    print('MODEL PANEL',i+1,len(pan),'order',n,'seconds',round(record['seconds'],1),'sum',float(total.mid()),flush=True)
if not all((destination/f'{i:04d}.json').exists()for i in range(len(pan))):
    print('ASSIGNED PANEL RANGE COMPLETE',first,last,flush=True)
    raise SystemExit(0)
total=sum((q(json.loads((destination/f'{i:04d}.json').read_bytes())['model_Xnorm_squared_upper'][1])for i in range(len(pan))),arb(0))
# Endpoint envelope is a separate analytical obligation, intentionally not
# silently promoted by successful finite panel arithmetic.
dl=(oe[1]-a)*arb(2)**(-args.panels);dr=(b-oe[-2])*arb(2)**(-args.panels)
def tail_bound(d):
    t=-d.log()
    # Integral of (1+log(v)^2)^2: 29+28t+14t²+4t³+t⁴.
    return 2*q('1e40')*d*(29+28*t+14*t*t+4*t**3+t**4)
tails=tail_bound(dl)+tail_bound(dr)
result={'status':'MODEL_NORM_CONDITIONAL_ON_ENDPOINT_ENVELOPE',
        'interior_upper':c.enc(total),'endpoint_upper_conditional':c.enc(tails),
        'model_Xnorm_squared_conditional_upper':c.enc(total+tails),
        'endpoint_assumption':'|r_model(a+v)|,|r_model(b-v)| <= 1e20 (1+log(v)^2)',
        'endpoint_lemma_checked':False,'whole_operator_model_errors_paid':False,
        'whole_comparison_pass':False,'panels':len(pan)}
(destination/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
print('MODEL SUMMARY',float(total.mid()),float(tails.mid()),flush=True)
