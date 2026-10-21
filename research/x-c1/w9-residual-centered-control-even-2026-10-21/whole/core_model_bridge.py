"""Directed full-function bound between the two finite core quadrature models."""
import contextlib,hashlib,io,json
from pathlib import Path
from flint import arb,arb_mat,arb_poly,ctx
import model_cache
HERE=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile((HERE/'probe.py').read_text().split('# Midpoint-only trade-off')[0],str(HERE/'probe.py'),'exec'))
ctx.prec=3072
def read(name,source):return model_cache.load(HERE/name,hashlib.sha256((HERE/source).read_bytes()).hexdigest())
old,ib=read('whole-model-ed58da3caacd.json.gz','whole_function_probe.py')
new,nb=read('whole-model-36d3f3fcb6cb-n128.json.gz','whole_function_probe_v2.py')
assert ib==nb
for key in old:
    if key not in ('hpoints','ustatic','outerstatic','outerreg','momentR'):
        assert model_cache.pack(old[key])==model_cache.pack(new[key]),key
for field in('ustatic','outerstatic'):
    for key in old[field]:
        if key is not None:assert model_cache.pack(old[field][key])==model_cache.pack(new[field][key])
a,b,hs,mu,delta=(old[k]for k in('a','b','hs','mu','delta'))
edges=old['edges'];width=a-edges[-2]
panels=[(lo,hi,64,128)for lo,hi in zip(edges[:-2],edges[1:-1])]
panels +=[(a-width*arb(2)**(-k),a-width*arb(2)**(-k-1),32,64)for k in range(48)]
indices=[0,0];points=[old['hpoints'],new['hpoints']]
bound=arb(0);rows=[];dmean=arb(0)
for i,(lo,hi,n0,n1)in enumerate(panels):
    mid=(lo+hi)/2;half=(hi-lo)/2;distance=a-mid;ratio=half/distance
    assert 0<ratio<1
    moments=arb_mat(128,1);tv=arb(0)
    for which,n in enumerate((n0,n1)):
        pp=[];ww=[]
        block=points[which][indices[which]:indices[which]+n];indices[which]+=n
        for x,weight in block:
            assert lo<x<hi
            z=(x-mid)/half;row=[arb(1)]
            for k in range(127):row.append(row[-1]*z)
            pp.append(row);ww.append([weight if which==0 else-weight]);tv+=abs(weight).upper()
        moments+=arb_mat(pp).transpose()*arb_mat(ww)
    dmean+=moments[0,0]
    total=sum((abs(moments[k,0]).upper()*ratio**k/arb(2*k+1).sqrt()for k in range(128)),arb(0))
    total+=tv*ratio**128/(1-ratio)
    total*=(2/distance).sqrt()
    bound+=total
    rows.append(c.enc(total))
assert indices==[len(points[0]),len(points[1])]
regdiff=old['outerreg']-new['outerreg']
regsup=sum((abs(v).upper()*b**k for k,v in enumerate(regdiff)),arb(0))
regular=regsup*(2*hs).sqrt()
moment=abs(old['momentR']-new['momentR']).upper()/mu*2*(2*hs).sqrt()
alpha=100*(2*mu).sqrt()*abs(dmean).upper()/(a*delta)
full=bound/delta+regular+moment+alpha
out={'status':'DIRECTED_STORED_MODEL_DIFFERENCE_BOUND',
     'same_mathematical_source_inputs':True,'core_measure_singular_X_bound':c.enc(bound),
     'regular_X_bound':c.enc(regular),'moment_X_bound':c.enc(moment),
     'mean_difference':c.enc(dmean),'mean_lift_X_bound':c.enc(alpha),
     'full_X_difference_bound':c.enc(full),
     'requires_whole_moment_coupling_cap':100,
     'whole_operator_model_error_paid':False,'full_comparison_pass':False,
     'per_cell_Cauchy_bounds':rows}
(HERE/'core-model-bridge.json').write_bytes((json.dumps(out,indent=2)+'\n').encode())
print({k:[float(q(x))for x in v]for k,v in out.items()if isinstance(v,list)and len(v)==2 and isinstance(v[0],str)},flush=True)
