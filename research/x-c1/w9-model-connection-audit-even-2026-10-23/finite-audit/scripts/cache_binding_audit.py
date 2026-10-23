"""Targeted frozen Gauss-atom audit; no new quadrature rule or direction."""
import sys
if not __debug__: raise SystemExit('Optimized Python is rejected')
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,time
from flint import arb,arb_mat,ctx
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a0=ap.parse_args()
R=a0.repo.resolve();O=a0.out.resolve();O.mkdir(parents=True,exist_ok=True);start=time.monotonic()
def mod(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
S=R/'research/x-c1/w9-new-k-schur-underform-even-2026-10-20'
eng=mod('cache_audit_schur',S/'engine.py');ctx.prec=1024;spec,data=eng.snapshot(R,(S/'INPUT_BINDINGS.json').read_bytes());env=eng.load(R,spec,data)
ctx.prec=3072
W=R/'research/x-c1/w9-residual-centered-control-even-2026-10-21/whole'
cache=mod('cache_audit_loader',W/'model_cache.py')
resmod=mod('cache_audit_residuals',R/'research/x-c1/w9-partial-energy-2026-10-18/residuals.py');res=resmod.Residuals(env['inp'],'even')
v,bindings=cache.load(W/'whole-model-36d3f3fcb6cb-n128.json.gz',hashlib.sha256((W/'whole_function_probe_v2.py').read_bytes()).hexdigest())
assert bindings=={n:hashlib.sha256(d).hexdigest() for n,d in env['inp'].data.items()}
cc=v['cc'];a=v['a'];b=v['b'];edges=v['edges'];width=a-edges[-2]
panels=[(lo,hi,128)for lo,hi in zip(edges[:-2],edges[1:-1])]+[(a-width*arb(2)**(-k),a-width*arb(2)**(-k-1),64)for k in range(48)]
nodes={};pos=0;rows=[];total_dx=arb(0);total_dw=arb(0);mismatch=[];cn=cw=0;mx=arb(0);mw=arb(0)
enc=lambda x:[str(x.lower().fmpq()),str(x.upper().fmpq())]
for i,(lo,hi,n) in enumerate(panels):
 if n not in nodes:nodes[n]=[arb.legendre_p_root(n,k,weight=True)for k in range(n)]
 fun=res.cell(lo,hi);sumdx=arb(0);sumdw=arb(0)
 for z,wt in nodes[n]:
  x=(lo+hi)/2+(hi-lo)*z/2;ww=(hi-lo)*wt/2;hh=sum((c*t for c,t in zip(cc,fun(x))),arb(0));weight=ww*hh
  sx,sw=v['hpoints'][pos];dx=abs(sx-x).upper();dw=abs(sw-weight).upper()
  xc=sx.contains(x);wc=sw.contains(weight);cn+=int(xc);cw+=int(wc)
  if not(xc and wc):mismatch.append({'atom':pos,'node_contains':bool(xc),'weight_contains':bool(wc)})
  assert sx.overlaps(x) and sw.overlaps(weight)
  sumdx+=dx;sumdw+=dw;mx=max(mx,dx);mw=max(mw,dw);pos+=1
 total_dx+=sumdx;total_dw+=sumdw
 rows.append({'panel':i,'nodes':n,'node_difference_sum':enc(sumdx),'weight_difference_sum':enc(sumdw),'distance_to_outer_shell':enc(a-hi)})
 if i%8==0:print('PANELS',i,'ATOMS',pos,'SECONDS',round(time.monotonic()-start,1),flush=True)
assert pos==len(v['hpoints'])==5120
out={'scope':'fixed 128/64 Gauss atoms; complete differences, not only overlap','atoms':pos,'node_enclosures_contain_recomputation':cn,'weight_enclosures_contain_recomputation':cw,
 'all_nodes_overlap':True,'all_weights_overlap':True,'sum_node_differences':enc(total_dx),'sum_weight_differences':enc(total_dw),'max_node_difference':enc(mx),'max_weight_difference':enc(mw),'noncontainment':mismatch,'panels':rows,'seconds':time.monotonic()-start}
(O/'cache-atom-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('RESULT',pos,cn,cw,'DX',total_dx.str(12),'DW',total_dw.str(12),flush=True)
