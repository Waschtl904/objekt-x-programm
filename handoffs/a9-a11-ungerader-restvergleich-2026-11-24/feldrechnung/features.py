"""Directed source errors in the 191 and 12 force coordinates of the stored odd model."""
import argparse, hashlib, json, sys
from pathlib import Path
from flint import arb, arb_mat, ctx
from fractions import Fraction

ap=argparse.ArgumentParser()
for key in ('root','finite','cache','transport','output'): ap.add_argument(key,type=Path)
args=ap.parse_args()
src=args.root/"research/x-c1/w9-partial-energy-2026-10-18"
vendor=args.root/"research/x-c1/w9-residual-centered-control-even-2026-10-21/whole"
sys.path[:0]=[str(src),str(vendor)]
import common as c, model_cache
from common import q, mat, norm, box, trace
from assemble import quad, Energy, load_pairs
from flint import fmpq_mat,fmpq

ctx.prec=3072
raw=args.finite.read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='0cd7325cfed36fb357d6c44c0f2b7e14eeb491be'
finite=json.loads(raw)
inputs=c.Inputs()
k=fmpq_mat([[fmpq(v) for v in row] for row in finite['K_rational']])
inv=k.inv()
class View:
    def json(self,name):
        x=inputs.json(name)
        if name=='coherent':
            x['parities']['odd'].update(K_rational=finite['K_rational'],K_inverse_rational=[[str(inv[i,j]) for j in range(12)] for i in range(12)])
        return x
e=Energy(View(),load_pairs(src/'expected/PAIRS_odd.json.gz'))
source=Path(__file__).with_name('odd_field_control.py')
model,bindings=model_cache.load(args.cache,hashlib.sha256(source.read_bytes()).hexdigest())
assert bindings=={k:hashlib.sha256(v).hexdigest() for k,v in inputs.data.items()}
p,ff,low,w=(model[k] for k in ('pv','ff','low','w'))
case=inputs.json('common')['cases'][1]
raw=inputs.json('old_sources')['cases'][1]
W=e.w
Ki,C,delta,rho,gamma=(W[k] for k in ('Ki','C','delta','rho','gamma'))
frozen=json.loads((src/'expected/CANDIDATE_odd.json').read_bytes())
coef=c.ratmat([[v] for v in frozen['raw_coefficients']])
coef/=quad(e.G,coef).sqrt()
coef0=arb_mat([[v] for v in model['cc']])
eps_h=e.eResidual+norm(coef-coef0)*(trace(mat(e.data['H9_Gram'])).sqrt()+e.eResidual)
bh=c.ratmat([[v] for v in finite['grouped_force_before_K_inverse']])
p_switch=quad(W['K'],p+Ki*bh).abs_upper().sqrt()
p_err=q(finite['grouped_force_error_K_inverse_upper'])+p_switch
hn=quad(e.H,coef).abs_upper().sqrt(); eh=abs((e.eh*coef)[0,0]).upper()
en=norm(e.ell*coef)
eBy=e.eRawA*(hn+gamma*eh)+e.eLowA*en
eWh=norm(C)*eBy/(delta*(1-rho).sqrt())
EF=2*(mat(case['finite_feature_error_gram'])+mat(raw['old_certificate']['joint_high_source_error_gram'])/delta)
EJ=2*(box(case['tail_feature_error_scalar'])+box(raw['galerkin']['high_source_error_norm'])**2/delta)
eta_model=e.wj*w-e.wh*coef-e.wf*p
eta_round=norm(eta_model-C.solve(ff)*(1-rho).sqrt())
eta_err=eta_round+EJ.sqrt()*norm(w)+quad(EF,p).abs_upper().sqrt()+eWh+e.bounds['U8_norm_upper'].sqrt()*eps_h
cap=q(json.loads(args.transport.read_bytes())['force_cap'])
joint=cap*(p_err**2+eta_err**2).sqrt()
out={}
for k,v in dict(b_representative_switch=p_switch,physical_source=eps_h,pW=p_err,eta_round=eta_round,etaW=eta_err,joint_dual_error=joint).items():
    assert v.is_finite() and v>=0
    out[k]=str(Fraction(str(v.upper().fmpq())))
print({k:float(Fraction(v)) for k,v in out.items()},flush=True)
out.update(whole_residual_certified=False)
args.output.write_text(json.dumps(out,indent=2),encoding='utf8')
