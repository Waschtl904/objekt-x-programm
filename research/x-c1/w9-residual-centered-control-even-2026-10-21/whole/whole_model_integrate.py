"""Joint exploratory WX residual norm and independent coordinate checks."""
import argparse,hashlib,json,sys,time
from pathlib import Path
from flint import arb,acb,arb_poly,arb_mat,ctx
import model_cache
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent/'objekt-x-integration-20261019'
ap=argparse.ArgumentParser();ap.add_argument('--cache',type=Path,required=True);ap.add_argument('--nodes',type=int,default=32);ap.add_argument('--panels',type=int,default=30);ap.add_argument('--fast',action='store_true');ap.add_argument('--tail-nodes',type=int,default=0);ap.add_argument('--source',type=Path,default=HERE/'whole_function_probe.py');ap.add_argument('--suffix',default='');args=ap.parse_args()
start=time.monotonic()
exec(compile((HERE/'probe.py').read_text().split('# Midpoint-only trade-off')[0],str(HERE/'probe.py'),'exec'))
ctx.prec=3072
src=ROOT/'research/x-c1/w9-partial-energy-2026-10-18'
resmod=module('residuals',src/'residuals.py');of=module('old_fields',src/'old_fields.py')
res=resmod.Residuals(env['inp'],'even');leg=res.legs
code=args.source.read_bytes()
values,bindings=model_cache.load(args.cache,hashlib.sha256(code).hexdigest())
assert bindings=={name:hashlib.sha256(raw).hexdigest()for name,raw in env['inp'].data.items()}
globals().update(values)
def hfun(fun,x):return sum((z*v for z,v in zip(cc,fun(x))),arb(0))
def evaluate(parts,t):
    v=parts.get(None,arb_poly([]))(t)
    for tag,p in parts.items():
        if tag is not None:v+=p(t)*abs(t-rootvalues[tag]).log()
    return v
text=code.decode()
tail=text[text.index('# Cauchy integrals'):text.index("print('Whole function ready'")]
exec(compile(tail,'bound_whole_model_evaluation','exec'))
if args.fast:
    import fast_evaluation
    fast_evaluation.install(globals())
cuts=[]
for edge in edges:
    for sh,wt in channels:
        for x in (edge+sh,edge-sh,sh-edge,-edge-sh):
            if a<x<b:cuts.append(x)
for x in res.cuts:
    if a<x<b:cuts.append(x)
cuts.sort(key=float);outeredges=[a]
for x in cuts:
    if not x.overlaps(outeredges[-1]):outeredges.append(x)
outeredges.append(b)
pan=[]
for i,(lo,hi)in enumerate(zip(outeredges[:-1],outeredges[1:])):
    if i==0:
        for k in range(args.panels):pan.append((lo+(hi-lo)*arb(2)**(-k-1),lo+(hi-lo)*arb(2)**(-k)))
    elif i==len(outeredges)-2:
        for k in range(args.panels):pan.append((hi-(hi-lo)*arb(2)**(-k),hi-(hi-lo)*arb(2)**(-k-1)))
    else:pan.append((lo,hi))
nodesets={}
mr=arb(0);r2=arb(0);moments=arb_mat(104,1);maxr=arb(0)
for i,(lo,hi)in enumerate(pan):
    n=args.nodes
    if args.tail_nodes and hi-lo<hs/64:n=args.tail_nodes
    if n not in nodesets:nodesets[n]=[arb.legendre_p_root(n,k,weight=True)for k in range(n)]
    nodes=nodesets[n]
    for z,wt in nodes:
        x=(lo+hi)/2+(hi-lo)*z/2;ww=(hi-lo)*wt/2
        rr=outer_value(x)
        assert rr.is_finite()
        u=(x-mid)/half
        pol=[arb(1),u]
        for n in range(1,103):pol.append(((2*n+1)*u*pol[-1]-n*pol[-2])/(n+1))
        r2+=2*ww*rr**2;mr+=2*ww*rr*res.m(x)
        maxr=max(maxr,abs(rr).upper())
        for n in range(104):moments[n,0]+=2*ww*rr*pol[n]*(arb(2*n+1)/(2*hs)).sqrt()
    if i%4==0:print('Whole model panels',i,len(pan),'seconds',round(time.monotonic()-start,1),flush=True)
# Riesz projection onto the complete T: subtract exactly the twelve constraints,
# not 96 modes. The local W metric carries its rank-one moment correction.
S=arb_mat(96,12)
for j,(pol,ls)in enumerate(zp):
    localpol=pol(arb_poly([mid/b,half/b]))
    for n in range(9):S[n,j]=(hs*(2*n+1)/2).sqrt()*c.pint(localpol*leg[n],arb(-1),arb(1))
for n in range(96):
    for j in range(8):S[n,j+4]=Y[n,j]
lv=arb_mat([[(hs*(2*n+1)/2).sqrt()*c.mellin(n,hs/2)*((mid/2).cosh()if n%2==0 else(mid/2).sinh())]for n in range(96)])
lamS=S.transpose()*lv
GS=S.transpose()*S+2/mu*lamS*lamS.transpose()
m96=arb_mat([[moments[n,0]]for n in range(96)])
rs=S.transpose()*m96
wx=r2-mr**2/(2*res.mu)-(rs.transpose()*GS.inv()*rs)[0,0]
rJ=J.transpose()*m96
Jdifference=rJ-nmodel
P=e.w['P']
jd2=(Jdifference.transpose()*P*Jdifference)[0,0]
outside_path=Path('C:/Users/sebas/Documents/Codex/2026-10-09/github-plugin-github-openai-curated-remote/work/infinite-dual-review-input-2026-10-11/Objekt-X-Unendlicher-Dualrest-und-Aussenrichtungen-2026-10-11/data/PROBE_EVEN_3072.json')
external=json.loads(outside_path.read_bytes())
Klocal=arb_mat([[q(external['working_local_coefficients_rational'][i][j])for j in range(1,9)]for i in range(104)])
rK=Klocal.transpose()*moments
independent=json.loads((HERE/'exterior-96.json').read_bytes())
rkdiff=rK-c.mat(independent['r_K_model'])
out={'status':'EXPLORATORY_WHOLE_FUNCTION_QUADRATURE_WITHOUT_DIRECTED_REMAINDERS',
     'cache_sha256':hashlib.sha256(args.cache.read_bytes()).hexdigest(),'nodes':args.nodes,'panels':args.panels,'tail_nodes':args.tail_nodes,'fast':args.fast,
     'raw_X_norm_squared':c.enc(r2),'whole_T_W_dual_norm_squared_model':c.enc(wx),
     'whole_L_dual_upper_expression_model':c.enc(wx*5/21),
     'finite_J_P_difference_squared':c.enc(jd2),'outside8_independent_pair_difference':c.enc(c.norm(rkdiff)),
     'rJ_model':c.encode(rJ),'rK_model':c.encode(rK),'maximum_sampled_absolute_raw_function':c.enc(maxr),
     'quadrature_remainder_paid':False,'whole_model_error_paid':False,'comparison_pass':False,
     'seconds':time.monotonic()-start}
path=HERE/f'whole-norm-{args.nodes}-{args.panels}{"-fast"if args.fast else ""}{args.suffix}.json';assert not path.exists()
path.write_text(json.dumps(out,indent=2)+'\n')
print('WHOLE MODEL',float(wx.mid()),'L price expression',float((wx*5/21).mid()),'J check',float(jd2.mid()),'K check',c.norm(rkdiff).str(12),flush=True)
