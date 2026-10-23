"""Fresh source rebuild using bound old quadrature; no new integration grid."""
import sys
if not __debug__:raise SystemExit('Assertions required; no -O/-OO.')
sys.dont_write_bytecode=True
from pathlib import Path
from math import factorial
import ast,contextlib,hashlib,importlib.util,io,json,time
from flint import arb,arb_poly,arb_mat,acb,ctx
W=Path(__file__).resolve().parent
ROOT=W.parent/'pr254-review'
P=ROOT/'research/x-c1/w9-gamma-repair-even-2026-10-22'
WHOLE=ROOT/'research/x-c1/w9-residual-centered-control-even-2026-10-21/whole'
sys.path.insert(0,str(WHOLE));sys.path.insert(0,str(P))
import model_cache,corrected_builder
import exact_cache
ctx.prec=3072
tick=time.monotonic()
def status(s):print(s,round(time.monotonic()-tick,2),flush=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((P/'MANIFEST.json').read_bytes())
assert sha(P/'MANIFEST.json')=='ce44e7b00cef7c77a19c732ce0eb58b7e137bcb45a9afd85c82e02349f5f3edf'
for name,h in manifest.items():assert sha(P/name)==h,name
inputs=json.loads((P/'INPUT_BINDINGS.json').read_bytes())['repository_files']
extra='research/x-c1/w9-residual-centered-control-even-2026-10-21/MANIFEST.json'
inputs[extra]='cc1aa64855995f96d0127ea09cec94c59b826fb62a6ce601f0373b2cd5d0b151'
for name,h in inputs.items():assert sha(ROOT/name)==h,name
source=(WHOLE/'whole_function_probe.py').read_text(encoding='utf-8')
cached,binding=exact_cache.load(WHOLE/'whole-model-ed58da3caacd.json.gz',corrected_builder.EXPECTED)
ownpath=P/'norm/inputs/own-correction.json.gz'
import gzip
ownmeta=json.loads(gzip.decompress(ownpath.read_bytes()))
correction,_=exact_cache.load(ownpath,ownmeta['source_sha256'])

code=(WHOLE/'probe.py').read_text(encoding='utf-8').split('# Midpoint-only trade-off')[0]
oldroot="ROOT = Path(__file__).resolve().parents[1] / 'objekt-x-integration-20261019'"
assert code.count(oldroot)==1
code=code.replace(oldroot,'ROOT=Path('+repr(str(ROOT))+')')
base={'__file__':str(WHOLE/'probe.py'),'__name__':'bound_model_identification'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(code,str(WHOLE/'probe.py'),'exec'),base)
assert binding=={k:hashlib.sha256(v).hexdigest()for k,v in base['env']['inp'].data.items()}
base.update(arb_poly=arb_poly,acb=acb,factorial=factorial,Path=Path)
status('REFERENCE_BOUND')
pathneedle="Path('C:/Users/sebas/Documents/Codex/2026-10-09/github-plugin-github-openai-curated-remote/work/tail-probe-2026-10-10/vendor/log_integrals.py')"
def initialize(text,shared=None):
    ns=dict(base if shared is None else shared)
    prefix=text[text.index('ctx.prec=3072'):text.index('nodes={}')]
    assert prefix.count(pathneedle)==1
    prefix=prefix.replace(pathneedle,'Path('+repr(str(WHOLE/'vendor/log_integrals.py'))+')')
    if shared is None:
        exec(compile(prefix,'bound_builder_before_quadrature','exec'),ns)
    else:
        # Both source versions use the identical setup and frozen coefficients.
        # Rebind function globals, then execute the changed build_core calls.
        functions=[n for n in ast.parse(prefix).body if isinstance(n,ast.FunctionDef)]
        exec(compile(ast.Module(body=functions,type_ignores=[]),'shared_setup_functions','exec'),ns)
        exec(compile(prefix[prefix.index('g,prime,*_=build_core'):],'corrected_core_from_shared_setup','exec'),ns)
    funcs=[n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef)and n.name in ('evaluate','qmprime')]
    assert len(funcs)==2
    exec(compile(ast.Module(body=funcs,type_ignores=[]),'bound_evaluation_helpers','exec'),ns)
    ns['qmp']=[ns['qmprime'](lo,hi)for lo,hi in zip(ns['edges'][:-1],ns['edges'][1:])]
    return ns
old=initialize(source);status('OLD_SOURCE_BUILT')
new=initialize(corrected_builder.corrected_source(ROOT),old);status('CORRECTED_SOURCE_BUILT')
c=old['c'];q=c.q
enc=lambda v:[str(v.lower().fmpq()),str(v.upper().fmpq())]
def upper(x):return abs(x).upper()
def polsup(p):return sum((upper(v)for v in p),arb(0)).upper()
def matdiff(a,b):return sum((upper(a[i,j]-b[i,j])**2 for i in range(a.nrows())for j in range(a.ncols())),arb(0)).sqrt().upper()
def partnorm(parts,ns):
    a=ns['a'];ans=arb(0)
    for tag,p in parts.items():
        if tag is None:factor=(2*a).sqrt()
        elif tag=='one':factor=(4*a).sqrt()
        else:
            root=ns['rootvalues'][tag]
            factor=(2*a).sqrt()*max(upper(abs(root).log()),upper(abs(1-root).log()))
        ans+=polsup(p)*factor
    return ans.upper()
def diffparts(a,b):return {k:a.get(k,arb_poly([]))-b.get(k,arb_poly([]))for k in sorted(set(a)|set(b),key=lambda k:(k is not None,''if k is None else k))}
controls={}
fixed_fields=['a','b','hs','mid','half','mu','delta','rootvalues','roots','cells','edges',
              'sp','spx','slocal','channels','J','Y','w','pv','lm','zp','cc','gamma','harm','fac','convker']
exact_common={key:bool(model_cache.pack(old[key])==model_cache.pack(new[key]))for key in fixed_fields}
cache_common={key:bool(model_cache.pack(old[key])==model_cache.pack(cached[key]))for key in fixed_fields}
assert all(exact_common.values()),[key for key,ok in exact_common.items()if not ok]
for key in ['J','Y','w','pv','ff','low','slocal']:
    controls['unchanged_'+key]=matdiff(old[key],new[key])
    controls['cached_'+key]=matdiff(old[key],cached[key])
    assert controls['unchanged_'+key]<q('1e-150')
    assert controls['cached_'+key]<q('1e-150')
for key in ['g','gpsi']:
    d=diffparts(new[key],old[key]);d[None]-=correction['dG'if key=='g'else'dPsi']
    controls['source_'+key+'_correction_X']=partnorm(d,old)
    assert controls['source_'+key+'_correction_X']<q('1e-150')
status('FIXED_INPUTS_AND_SOURCE_CORRECTIONS_CHECKED')

# Reconstruct all finite Gauss sums from the original stored atoms, grouping
# exactly as the original 64-node builder. The original cells and atoms remain fixed.
hpoints=cached['hpoints'];old['hpoints']=new['hpoints']=hpoints
edges=old['edges'];a=old['a'];delta=old['delta']
panels=[(lo,hi,64)for lo,hi in zip(edges[:-2],edges[1:-1])]
width=a-edges[-2]
panels += [(a-width*arb(2)**(-k),a-width*arb(2)**(-k-1),32)for k in range(48)]
assert sum(n for lo,hi,n in panels)==len(hpoints)
hmom=[arb(0)]*225;hm=arb(0);hq=arb(0);pos=0
for index,(lo,hi,n)in enumerate(panels):
    block=hpoints[pos:pos+n];pos+=n;pp=old['qmprime'](lo,hi)
    powers=[];weights=[]
    for x,weighted in block:
        assert lo<x<hi
        hm+=weighted*old['res'].m(x)
        hq+=weighted*(old['evaluate'](old['qm'],x/a)+pp(x/a))
        row=[arb(1)]
        for k in range(224):row.append(row[-1]*x)
        powers.append(row);weights.append([weighted])
    v=arb_mat(powers).transpose()*arb_mat(weights)
    hmom=[v[i,0]+hmom[i]for i in range(225)]
    if index%20==0:status('BOUND_GAUSS_SUMS_'+str(index)+'/'+str(len(panels)))
for label,ns in [('old',old),('corrected',new)]:
    status('POST_QUADRATURE_'+label)
    if label=='corrected':ns['mom']=old['mom']
    ns.update(hmom=hmom,hm=hm,hq=hq)
    section=source[source.index('me=(2*a).sqrt()'):source.index("print('Complete core moment")]
    exec(compile(section,'bound_post_quadrature_construction','exec'),ns)
status('WHOLE_MODEL_COMPONENTS_REBUILT')
cache_reproduction={key:bool(model_cache.pack(old[key])==model_cache.pack(cached[key]))for key in ['ustatic','outerstatic','upp','outerreg','momentR']}
status('CACHE_REPRODUCTION_'+str(cache_reproduction))

# Propagate the actual source difference before applying large common affine
# terms. The shared h quadrature, low projection, Phi*f0 and direct shell data
# cancel by the displayed source identities, rather than by subtracting two
# independent copies of their already rounded interval enclosures.
dg=diffparts(new['g'],old['g']);dpsi=diffparts(new['gpsi'],old['gpsi'])
zero_primes=[arb_poly([])for _ in old['upp']]
moment0=old['integrate_static'](dg,zero_primes)[0]
alpha_delta=moment0/c.mellin(0,a)
du_parts={k:v*(1/delta) for k,v in dg.items()}
du_parts[None]-=old['mc']*(alpha_delta/delta)
du_error=dict(du_parts);du_error[None]-=correction['du']
controls['shared_du_minus_correction_X']=partnorm(du_error,old)
mom_delta=old['integrate_static'](du_parts,zero_primes,224)
physical_delta=[a**(k+1)*v for k,v in enumerate(mom_delta)]
reg_delta=old['regular_out'](physical_delta)
dmoment=a*old['logmod'].function_product(dpsi,{None:old['mc']},old['mom'],'zero','one')
dmoment+=a*old['logmod'].function_product(du_parts,old['qm'],old['mom'],'zero','one')
for (lo,hi),qp in zip(old['cells'],old['qmp']):
    dmoment+=a*old['logmod'].function_product(du_parts,{None:qp},old['mom'],lo,hi)
status('SHARED_SOURCE_DIFFERENCE_PROPAGATED')

for key in ['ustatic','outerstatic']:
    controls['old_cache_'+key+'_X']=partnorm(diffparts(old[key],cached[key]),old)
    delta_parts=diffparts(new[key],old[key]);delta_parts[None]-=correction['du']
    controls['new_old_'+key+'_minus_du_X']=partnorm(delta_parts,old)
controls['old_cache_upp_X']=max(polsup(a-b)for a,b in zip(old['upp'],cached['upp']))*(2*old['a']).sqrt()
controls['new_old_upp_X']=max(polsup(a-b)for a,b in zip(new['upp'],old['upp']))*(2*old['a']).sqrt()
x=arb_poly([old['a'],old['hs']])
controls['old_cache_outerreg_X']=polsup((old['outerreg']-cached['outerreg'])(x))*(2*old['hs']).sqrt()
controls['new_old_outerreg_minus_correction_X']=polsup((new['outerreg']-old['outerreg']-correction['outerreg_change'])(x))*(2*old['hs']).sqrt()
momentfactor=(old['hs']+old['b'].sinh()-old['a'].sinh()).sqrt()/old['mu']
controls['old_cache_momentlift_X']=upper(old['momentR']-cached['momentR'])*momentfactor
controls['new_old_momentlift_minus_correction_X']=upper(new['momentR']-old['momentR']-correction['dR'])*momentfactor

# Whole outer-function difference: cross Cauchy + reflected Cauchy and all
# prime translates of the core discrepancy, regular convolution and moment
# discrepancies separately. Common h atoms and common direct shell fields cancel.
crosscap=arb.pi()/2+(old['hs']/old['a']).sqrt()/2+2*sum((wt for sh,wt in old['channels']),arb(0))
old_core=controls['old_cache_outerstatic_X']+controls['old_cache_upp_X']
old_prime=controls['old_cache_ustatic_X']+controls['old_cache_upp_X']
old_full=(crosscap*max(old_core,old_prime)+controls['old_cache_outerreg_X']+controls['old_cache_momentlift_X']).upper()
new_core=controls['new_old_outerstatic_minus_du_X']+controls['new_old_upp_X']
new_prime=controls['new_old_ustatic_minus_du_X']+controls['new_old_upp_X']
new_full=(crosscap*max(new_core,new_prime)+controls['new_old_outerreg_minus_correction_X']+controls['new_old_momentlift_minus_correction_X']).upper()
controls['whole_old_builder_to_cache_X']=old_full
controls['whole_corrected_builder_to_cache_plus_correction_X']=(old_full+new_full).upper()
controls['shared_outerreg_minus_correction_X']=polsup((reg_delta-correction['outerreg_change'])(x))*(2*old['hs']).sqrt()
controls['shared_momentlift_minus_correction_X']=upper(dmoment-correction['dR'])*momentfactor
shared_full=(crosscap*controls['shared_du_minus_correction_X']+controls['shared_outerreg_minus_correction_X']+controls['shared_momentlift_minus_correction_X']).upper()
controls['shared_whole_correction_identification_X']=shared_full

# The exact high projection is followed by M. Its extra constant is governed
# by the degree >=384 tail of cosh(a*t/2), not by a degree-95 norm argument.
assert 0<old['a']/2<1
high_m_tail=q(2)/arb(factorial(384))
postMprice=high_m_tail*q('1e21')
moment160_price=q('2e6')/arb(factorial(160))*q('1e40')
controls['missing_post_M_core_cap_if_high_vector_norm_below_1e21']=postMprice
controls['inherited_moment_series_bound_rebuilt']=moment160_price
controls['sum_projection_moment_and_rebuild_allowances']=(100*postMprice+100*moment160_price+shared_full).upper()

# Quantify the moment of the modeled high component; it is not silently assumed
# to be in H8. The exact high-vector bound above is a separate analytical condition.
for label,ns in [('old',old),('corrected',new)]:
    parts=dict(ns['ustatic']);parts[None]-=ns['phif']
    moment=ns['logmod'].function_product(parts,{None:ns['mc']},ns['mom'],'zero','one')*ns['a']
    for (lo,hi),pp in zip(ns['cells'],ns['upp']):moment+=ns['a']*ns['mom'].integral(pp*ns['mc'],lo,hi)
    moment-=hm/delta
    controls[label+'_modeled_high_moment']=moment

result={'status':'DIAGNOSTIC_COMPONENT_REBUILD','base_commit':'beb38c9d1cba666bb3b7ddab9577873e59d854c4',
        'inputs':inputs,'package_manifest_sha256':sha(P/'MANIFEST.json'),
        'bound_gauss_atoms':len(hpoints),'new_quadrature':False,'fixed_fields_byte_identical':exact_common,
        'old_builder_components_byte_identical_to_cache':cache_reproduction,
        'cache_fixed_field_equality_diagnostic':cache_common,
        'bounds':{k:enc(v)for k,v in controls.items()},
        'naive_independent_interval_difference_meets_1e_150':bool(old_full+new_full<q('1e-150')),
        'shared_correction_bridge_below_1e_150':bool(shared_full<q('1e-150')),
        'old_cache_exact_reproduction_pass':bool(all(cache_reproduction.values())and all(cache_common.values())),
        'allowances_below_1e_150':bool(controls['sum_projection_moment_and_rebuild_allowances']<q('1e-150')),
        'full_analytic_identification_closed':False,'external_acceptance':False,
        'seconds':time.monotonic()-tick}
(W/'component-rebuild.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:float(upper(v))for k,v in controls.items()},indent=2),flush=True)
assert result['shared_correction_bridge_below_1e_150']and result['allowances_below_1e_150']
status('SHARED_CORRECTION_BRIDGE_PASS_CONDITIONAL')
if not result['old_cache_exact_reproduction_pass']:
    print('FULL ORIGINAL-CACHE IDENTIFICATION REMAINS OPEN: unequal arithmetic enclosures.',flush=True)
