"""Physical odd shell field for the new common core and fixed rational shell response."""
import argparse
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import sys

from bindungen import PAIRS, checked_pkg
from flint import ctx, arb, arb_mat, fmpq_mat, fmpq
parse=argparse.ArgumentParser()
for name in ("root","parent","finite","cache","output"):
    parse.add_argument(name,type=Path)
parse.add_argument("direction",choices=("e","s"))
args=parse.parse_args()
pkg=checked_pkg(args.root)
field=args.root.resolve()/"research/x-c1/w9-residual-centered-control-even-2026-10-21/whole"
parent=args.parent.resolve()
sys.path[:0]=[str(parent),str(pkg),str(field),str(field/"vendor")]
import common as c, model_cache
from common import q, mat, norm, box, trace
from assemble import Inputs, Energy,load_pairs,quad
from weights import sub
ctx.prec=3072
inputs=Inputs()
pairs=load_pairs(pkg/"expected/PAIRS_odd.json.gz")
assert pairs["_source_sha256"]==PAIRS
e=Energy(inputs,pairs)
with gzip.open(args.cache,"rt") as fp:
    hdr=json.load(fp)
cache_source=hdr["source_sha256"]
current=hashlib.sha256(Path(__file__).with_name("feldprobe.py").read_bytes()).hexdigest()
if cache_source!=current:
    assert cache_source=="f064f04219239aa69458a0a6045e331c8a9d61364f2f39fcb66c65d0ec02aaff"
    assert hdr["payload_sha256"]=="0ac3905a5fac91b704d1e7f2e7cf96c0d20794d979f7ab4158b3e5073b28c68d"
model,bindings=model_cache.load(args.cache,cache_source)
assert bindings=={k:hashlib.sha256(v).hexdigest() for k,v in inputs.data.items()}
source_script=parent/"source_bridge.py"
assert hashlib.sha256(source_script.read_bytes()).hexdigest()=="cff740fcd2f1e1dc191669d2c0f9a4c9b4fc2c88e625702025d0ffdf55c6fad4"
args.transport=parent/"transport.json"
assert hashlib.sha256(args.transport.read_bytes()).hexdigest()=="44a9e5e8d19ca5eac9b534088230b79a96eadef9064f4381c253ea8d646dab65"
frozen=json.loads(args.finite.read_bytes())["trial_"+args.direction]
def vec(values):
    return c.ratmat([[str(v)] for v in values])
coef=vec(frozen["raw"])
coef/=quad(e.G,coef).sqrt()
coef0=arb_mat([[v] for v in model["cc"]])
assert norm(coef-coef0)<q("1e-50")
eps_h=e.eResidual+norm(coef-coef0)*(trace(mat(pairs["H9_Gram"])).sqrt()+e.eResidual)
case=inputs.json("common")["cases"][1]
raw=inputs.json("old_sources")["cases"][1]
W=e.w
delta=model["delta"]
assert delta.overlaps(q("1.84298"))
gamma,C,rho,old_delta=(W[k] for k in ("gamma","C","rho","delta"))
T=C.transpose()/(1-rho).sqrt()
p,ff,low,w=(model[k] for k in ("pv","ff","low","w"))
finite={"w_rational":frozen["test"][12:]}
exactV=vec(frozen["test"])
roundV=arb_mat([[-p[i,0]] if i<12 else [w[i-12,0]] for i in range(96)])
dv=exactV-roundV
assert norm(dv)<q("1e-240")
round_price=5*quad(mat(case["D96_upper_model"]),dv).abs_upper().sqrt()
S,J=raw["old_certificate"],raw["galerkin"]
def scaled(key):
    return c.ratmat(case[key+"_integer_matrix"])/q(case[key+"_denominator"])
al=T*(scaled("F")+scaled("HB")/old_delta)*T.transpose()
g=T*(mat(raw["old_raw_coupling_gram"])/q(10**100))*T.transpose()
tau=q("1e-16")
spread=(2*tau*g+2/tau*box(S["old_coupling_error_norm"])**2*(T*T.transpose()))/delta
weighted=e.wj*w-e.wh*coef-e.wf*p
bare=mat(J["old_low_c_model"])*w-e.ell*coef-mat(S["source_c_model"])*p
alpha=old_delta/delta
u=alpha*weighted+(1-alpha)*T*bare
eta_model=T.transpose().solve(ff)
es=e.certificate(frozen["raw"],"10","bridge")["feature_error_norms"]["finite_U8"]
es+=e.bounds["U8_norm_upper"].sqrt()*eps_h+quad(e.EF,p).abs_upper().sqrt()+e.eJ*norm(w)
raw_error=gamma.sqrt()*eps_h+quad(e.ELF,p).abs_upper().sqrt()+e.eLJ*norm(w)
# Measured equation defect for the cached low coefficient, before pricing it
# against the true Schur inverse (bounded by I in these normalized coordinates).
eta_err=norm(u-(al-g/delta)*eta_model)+alpha*es+(1-alpha)*norm(T)*raw_error
eta_err+=(trace(spread)*quad(spread,eta_model)).abs_upper().sqrt()
assert eta_err.is_finite()
program=source_script.read_text(encoding="utf8")
program=program[program.index("from residuals import Residuals"):]
# Treat the rounded shell inputs as one form perturbation via the bound
# S_shell<=D on the old shell. This covers both the 12 and the 84 entries.
program=program.replace('w_round_dual = oldq*(H95+q("1.1")).sqrt()*jn*dw',
                        'w_round_dual = round_price')
program=program.replace('result={k:upper_decimal(v) for k,v in observed.items()}',
                        'observed.update(low_solution_dual=5*eta_err); result={k:upper_decimal(v) for k,v in observed.items()}')
exec(compile(program,str(source_script),"exec"))
