"""Read-only pinned context for the bounded PR252 connection audit."""
import hashlib, importlib.util, json, sys, time
from pathlib import Path
from flint import arb, arb_mat, arb_poly, ctx

BASE=Path(__file__).resolve().parent
ROOT=BASE/'repo'
PKG=ROOT/'research/x-c1/w9-residual-centered-control-even-2026-10-21'
WHOLE=PKG/'whole'
def sha(raw):return hashlib.sha256(raw).hexdigest()
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

start=time.monotonic()
manifest=json.loads((PKG/'MANIFEST.json').read_bytes())
for name,want in manifest.items():
    assert sha((PKG/name).read_bytes())==want, name
replay=json.loads((PKG/'REPLAY_BINDINGS.json').read_bytes())['repository_files']
package_prefix=str(PKG.relative_to(ROOT))+'/'
external_replay={name:want for name,want in replay.items() if not name.startswith(package_prefix)}
for name,want in external_replay.items():
    assert sha((ROOT/name).read_bytes())==want, name
# Same two binding scopes as the published whole_verify.py: current package
# through MANIFEST, external inputs through REPLAY_BINDINGS. Historical
# self-entries in REPLAY_BINDINGS are not current-package verification claims.
print('Bound package and external input hashes verified',len(manifest),len(external_replay),flush=True)
SCHUR=ROOT/'research/x-c1/w9-new-k-schur-underform-even-2026-10-20'
eng=module('connection_schur_engine',SCHUR/'engine.py')
spec,data=eng.snapshot(ROOT,(SCHUR/'INPUT_BINDINGS.json').read_bytes())
env=eng.load(ROOT,spec,data)
c=env['common'];e=env['energy'];q=c.q;mat=c.mat;quad=eng.quad
w=arb_mat([[q(x)]for x in json.loads((SCHUR/'CANDIDATE.json').read_bytes())['raw_coefficients']])
mcmod=module('connection_model_cache',WHOLE/'model_cache.py')
ctx.prec=3072
values,bindings=mcmod.load(WHOLE/'whole-model-ed58da3caacd.json.gz',sha((WHOLE/'whole_function_probe.py').read_bytes()))
assert bindings=={k:sha(v)for k,v in env['inp'].data.items()}
for i in range(84):assert values['w'][i,0].overlaps(w[i,0])
print('Context ready',round(time.monotonic()-start,3),'seconds',flush=True)
