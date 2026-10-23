"""Fresh source rebuild using bound old quadrature; no new integration grid."""
import sys
if not __debug__:raise SystemExit('Assertions required; no -O/-OO.')
sys.dont_write_bytecode=True
from pathlib import Path
from math import factorial
import ast,contextlib,hashlib,importlib.util,io,json,time
from flint import arb,arb_poly,arb_mat,acb,ctx
W=Path(__file__).resolve().parent
import argparse
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
ROOT=args.repo.resolve()
P=ROOT/'research/x-c1/w9-gamma-repair-even-2026-10-22'
WHOLE=ROOT/'research/x-c1/w9-residual-centered-control-even-2026-10-21/whole'
sys.path.insert(0,str(WHOLE));sys.path.insert(0,str(P))
import model_cache,corrected_builder
sys.path.insert(0,'joint-final-audit/prior/unpacked/Vorbereitete-Revision/scripts')
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
source=(WHOLE/'whole_function_probe_v2.py').read_text(encoding='utf-8')
cached,binding=exact_cache.load(WHOLE/'whole-model-36d3f3fcb6cb-n128.json.gz',sha(WHOLE/'whole_function_probe_v2.py'))
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

OUTPUT=args.out.resolve();OUTPUT.parent.mkdir(exist_ok=True,parents=True)
old=initialize(source);status('N128_SOURCE_BUILT')
hpoints=cached['hpoints'];old['hpoints']=hpoints
edges=old['edges'];a=old['a'];width=a-edges[-2]
panels=[(lo,hi,128)for lo,hi in zip(edges[:-2],edges[1:-1])]+[(a-width*arb(2)**(-k),a-width*arb(2)**(-k-1),64)for k in range(48)]
hmom=[arb(0)]*225;hm=arb(0);hq=arb(0);pos=0
for index,(lo,hi,n)in enumerate(panels):
    block=hpoints[pos:pos+n];pos+=n;pp=old['qmprime'](lo,hi);powers=[];weights=[]
    for x,weighted in block:
        assert lo<x<hi
        hm+=weighted*old['res'].m(x)
        hq+=weighted*(old['evaluate'](old['qm'],x/a)+pp(x/a))
        row=[arb(1)]
        for k in range(224):row.append(row[-1]*x)
        powers.append(row);weights.append([weighted])
    v=arb_mat(powers).transpose()*arb_mat(weights)
    hmom=[v[i,0]+hmom[i]for i in range(225)]
    if index%16==0:status('N128_BOUND_ATOMS_'+str(index))
assert pos==len(hpoints)==5120
old.update(hmom=hmom,hm=hm,hq=hq)
section=source[source.index('me=(2*a).sqrt()'):source.index("print('Complete core moment")]
exec(compile(section,'bound_n128_post_quadrature_construction','exec'),old)
fields=['ustatic','outerstatic','upp','outerreg','momentR']
exact={k:bool(model_cache.pack(old[k])==model_cache.pack(cached[k]))for k in fields}
result={'scope':'fresh algebraic reconstruction of n128 cache from its 5120 stored atoms','components_exact':exact,'all_exact':all(exact.values()),'seconds':time.monotonic()-tick}
print(result,flush=True)
OUTPUT.write_text(json.dumps(result,indent=2)+'\n')
assert all(exact.values())
