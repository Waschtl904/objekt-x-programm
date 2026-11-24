"""Bounded odd coupled comparison; input: project checkout, output: JSON path."""
import hashlib
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path

from flint import arb, arb_mat, ctx, fmpq, fmpq_mat

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def sha(b):
    return hashlib.sha256(b).hexdigest()

root = Path(sys.argv[1]).resolve()
pkg = root / "research/x-c1/w9-partial-energy-2026-10-18"
pins = {
    "INPUT_BINDINGS.json":"a57030f51a827598cc41b923b8cfd23410cfd0b2",
    "common.py":"1a88b1d72daa3fe6aeccee0449ecc6998c466a6f",
    "weights.py":"adc250e1a3cf0d842fea94806fdb6bfa5e3a6f95",
    "assemble.py":"aeadc048c4928bf739c70a1cbf49b8651cf73544",
    "expected/K_P_odd.json":"76783a37e42c933701c2118dbb3d88a3de10b922",
    "expected/CANDIDATE_odd.json":"4e21fad9f0569fe1738e328e620f4da4075b7e76",
    "expected/COMPARISON_odd.json":"f1b97ac47f4be56f527d90b64e41836b45a25c71",
}
for name, code in pins.items():
    raw = (pkg/name).read_bytes()
    require(hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest() == code, name)

sys.path.insert(0, str(pkg))
from common import Inputs, box, enc, mat, norm, q, ratmat, trace
from weights import sub
from assemble import Energy, load_pairs, quad

ctx.prec = 1024
inp = Inputs()
rawp = inp.json("old_sources")["cases"][1]
case = inp.json("common")["cases"][1]
require(case["parity"] == "odd", "wrong common case")
pairs = load_pairs(pkg/"expected/PAIRS_odd.json.gz")
frozen = json.loads((pkg/"expected/CANDIDATE_odd.json").read_bytes())
kp = json.loads((pkg/"expected/K_P_odd.json").read_bytes())
historical = json.loads((pkg/"expected/COMPARISON_odd.json").read_bytes())
require(pairs["_source_sha256"] == frozen["pairs_sha256"] == historical["pairs_sha256"],"pairings")
require(sha((pkg/"expected/CANDIDATE_odd.json").read_bytes()) == kp["candidate_sha256"] == historical["candidate_sha256"], "candidate")
require(sha((pkg/"expected/K_P_odd.json").read_bytes()) == historical["K_P_certificate_sha256"],"budget")
lo, hi = range(12), range(12,96)
U, DL, DU = [mat(case[k]) for k in ("U96_model","D96_lower_model","D96_upper_model")]
EF0 = mat(case["finite_feature_error_gram"])
UF = sub(U,lo,lo)
GF = ratmat([row[:12] for row in case["G96_rational"][:12]])
def nearest(v, grid):
    u = F(str(v.mid().fmpq()))*grid + F(1,2)
    return F(u.numerator//u.denominator,grid)
def strings(A):
    return [[str(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def exact(rows):
    return fmpq_mat([[fmpq(x) for x in row] for row in rows])
def positive(A):
    require(A == A.transpose(), "exact symmetry")
    # Sylvester criterion, exact rational leading principal determinants.
    dets = [fmpq_mat([[A[i,j] for j in range(n)] for i in range(n)]).det() for n in range(1,A.nrows()+1)]
    require(all(v>0 for v in dets), "strict positive order")
    return len(dets)
def lower(A):
    n = A.nrows()
    centers, radii = [], []
    for i in range(n):
        row, rad = [], F(0)
        for j in range(n):
            l,u = map(F,enc((A[i,j]+A[j,i])/2))
            row.append((u+l)/2)
            rad += (u-l)/2
        centers.append(row)
        radii.append(rad)
    for i,rad in enumerate(radii):
        centers[i][i] -= rad + F(1,10**60)
    return exact([[str(v) for v in row] for row in centers])

ep = nearest((trace(GF.inv()*EF0)/trace(GF.inv()*UF)).sqrt(),10**40)
require(ep>0,"positive parity-specific epsilon")
K = lower(sub(DL,lo,lo)-(1+q(ep))*UF-q(1+1/ep)*EF0)
co = inp.json("coherent")["parities"]["odd"]
old = exact(co["K_rational"])
pivots = positive(K-old)
Ki_rows, K_rows = strings(K.inv()), strings(K)
BJJ = sub((DL+DU)/2-U,hi,hi)
class View:
    def __init__(self, P=None):
        self.P = P
    def json(self, name):
        data = inp.json(name)
        if name == "coherent":
            data["parities"]["odd"].update(K_rational=K_rows,K_inverse_rational=Ki_rows)
        if name == "inverse_odd" and self.P is not None:
            data["P_upper_rational"] = self.P
        return data

seed = Energy(View(), pairs)
coeff = arb_mat([[q(x)] for x in frozen["raw_coefficients"]])
coeff /= quad(seed.G,coeff).sqrt()
nu = seed.nu*coeff
H0 = BJJ-seed.w["a"].transpose()*seed.w["Ki"]*seed.w["a"]
def mid(A):
    return arb_mat([[A[i,j].mid() for j in range(A.ncols())] for i in range(A.nrows())])
solution = mid((H0+H0.transpose())/2).solve(mid(nu))
wlist = [nearest(solution[i,0],10**50) for i in range(84)]
w = arb_mat([[q(v)] for v in wlist])
# A rank-one positive semidefinite output weight evaluates precisely this dual pairing.
Pww = [[str(x*y) for y in wlist] for x in wlist]
e = Energy(View(Pww),pairs)
cert = e.certificate(frozen["raw_coefficients"], kp["K_P_interval"], "fixed_odd_coupled")
W = e.w
def up(x): return q(enc(x)[1])
def sq(x): return x.sqrt()
def nn(x): return max(arb(0),x.lower())
def hull(l,u): return [enc(l)[0],enc(u)[1]]
base0 = sum((cert["component_model_energies"][k] for k in ("high_U8","finite_U8","K_inverse_v")),arb(0))
base_err = (cert["feature_error_norms"]["finite_U8"]**2+cert["feature_error_norms"]["K_inverse_v"]**2).sqrt()
base_err += (e.bounds["U8_norm_upper"]+e.bounds["v_feature_operator_norm_upper"]**2).sqrt()*e.eResidual
base = hull(nn(base0.lower().sqrt()-up(base_err))**2,(base0.upper().sqrt()+up(base_err))**2)
pairmodel=(w.transpose()*e.nu*coeff)[0,0]
pairerr=(cert["feature_error_norms"]["P_upper_J_star_nu"]+cert["residual_model_error_norm"])/q("11/10").sqrt()
pair=hull(pairmodel-up(pairerr),pairmodel+up(pairerr))
# Directional D and U discrepancy and off-diagonal error for ||Ki^(1/2) a w||^2.
Ki, a0, GJ = W["Ki"], W["a"], W["GJ"]
fvec = Ki*a0*w
EF = 2*(EF0+mat(rawp["old_certificate"]["joint_high_source_error_gram"])/W["delta"])
EJ = 2*(box(case["tail_feature_error_scalar"])+box(rawp["galerkin"]["high_source_error_norm"])**2/W["delta"])
DD = (DU-DL)/2
dw,uw = quad(sub(DD,hi,hi),w),quad(sub(U,hi,hi),w)
ew = EJ*(w.transpose()*w)[0,0]
direct_err = quad(sub(DD,lo,lo),fvec)
ur,er=quad(UF,fvec),quad(EF,fvec)
require(all(x>=0 for x in (dw,uw,ew,direct_err,ur,er)),"directional certificates")
bprice = dw+2*sq(uw*ew)+ew
crossprice = 2*(sq(direct_err*dw)+sq(ur*ew)+sq(er*uw)+sq(er*ew))
sqmodel=quad(Ki,a0*w)
extra_sq = W["da"]**2*trace(Ki*GF)*quad(GJ,w)
floor_sq = nn(sqmodel-up(crossprice))
ceil_sq = sqmodel+up(crossprice+extra_sq)
bmodel=quad(BJJ,w)
eta=q("1e-10")
eta_hi=eta*quad(sub(DU,hi,hi),w)
require(eta_hi>=0,"positive direct upper cap")
F_interval = hull(q(base[0])+2*q(pair[0])-bmodel-up(bprice)+floor_sq,
                  q(base[1])+2*q(pair[1])-bmodel+up(bprice)+ceil_sq+up(eta_hi))
def sci(x):
    v=F(x)
    with localcontext() as ctxd:
        ctxd.prec=18
        return str(Decimal(v.numerator)/Decimal(v.denominator))
P = seed.w["P"]
pcert = seed.certificate(frozen["raw_coefficients"], kp["K_P_interval"], "original_odd_P_metric")
UJ = sub(U,hi,hi)
gr,gw = quad(GF,fvec),quad(GJ,w)
tpG,tpU,tpE = trace(P*GJ),trace(P*UJ),EJ*trace(P)
tkG,tkU,tkE = trace(Ki*GF),trace(Ki*UF),trace(Ki*EF)
tpD = trace(P*sub(DD,hi,hi))
dd = e.bounds["direct_energy_relative_error_upper"]
ea = dd*sq(tkG*gw)+sq(tkU*ew)+sq(tkE*uw)+sq(tkE*ew)
left = dd*sq(gr*tpG)+sq(tpU*er)+sq(tpE*ur)+sq(tpE*er)
hs = dd*sq(tkG*tpG)+sq(tkU*tpE)+sq(tkE*tpU)+sq(tkE*tpE)
square_error = left+(sq(trace(P*a0.transpose()*Ki*a0))+hs)*ea
u_action = sq(tpU*ew)+sq(tpE*uw)+sq(tpE*ew)
d_action = sq(tpD*dw)
DJ = sub((DU+DL)/2,hi,hi)
nmodel = nu-H0*w+eta*DJ*w
nu_error = (pcert["feature_error_norms"]["P_upper_J_star_nu"]+
            pcert["residual_model_error_norm"])/sq(q("11/10"))
z = sq(quad(P,nmodel))+nu_error+(1+eta)*d_action+u_action+square_error
budget=list(map(F,kp["K_P_interval"]))
fl,fu=map(F,F_interval)
require(q(enc(quad(sub(DL,hi,hi),w))[0])>=0, "eta*q[Jw] lower endpoint")
preflight = (pkg.parent/"w9-majorant-preflight-2026-10-18/EXPECTED.json").read_bytes()
require(hashlib.sha1(b"blob "+str(len(preflight)).encode()+b"\x00"+preflight).hexdigest()
        =="f33aa356795b9280387aa00a80dacacefdaff29a","majorant source")
pre = json.loads(preflight)["parities"]["odd"]
cap,beta = map(F,(pre["full_residual_cap"],pre["beta"]))
require(cap==F(6967,10**6) and beta==F(20209999981781,182190000000000),"odd contraction")
margin = budget[0]-fu
zup = F(enc(z)[1])
require(margin>zup*zup/(1-cap), "finite correction exceeds margin")
dstar = q(beta)*(sq(q((1-cap)*(margin-zup*zup)))-q(zup)*sq(q(cap)))**2
# Settle on a transferable cap rounded down to an exact multiple of 1e-10.
dcap = F((F(enc(dstar)[0])*10**10)//1,10**10)
x2 = q(dcap/beta)
conditional = q(fu)+(x2+q(zup*zup)+2*q(zup)*sq(q(cap)*x2))/(1-q(cap))
require(dcap>0 and F(enc(conditional)[1])<budget[0], "strict conditional comparison")
print("z upper",sci(zup),"d threshold",list(map(sci,enc(dstar))),"d cap",sci(dcap),
      "conditional upper",sci(enc(conditional)[1]),"conditional margin",sci(budget[0]-F(enc(conditional)[1])),flush=True)
print("epsilon",ep,"pivots",pivots, "F interval",list(map(sci,F_interval)), "budget",list(map(sci,budget)),flush=True)
print("base",list(map(sci,base)),"pair",list(map(sci,pair)),"directional model",enc(base0+2*pairmodel-quad(H0,w))[0][:70],"gap (budget lower-F upper)",sci(budget[0]-fu),flush=True)
result=dict(commit="18dd92f89f889c1f506673fefee33e4544b22038",parity="odd",bits=ctx.prec,epsilon=str(ep),
    positive_K_minus_old=pivots,K_rational=K_rows,old_witness_sha256=kp["candidate_sha256"],
    pairing_file_sha256=pairs["_source_sha256"],w_rational=list(map(str,wlist)),base=base,pairing=pair,
    F=F_interval,K_P=kp["K_P_interval"],K_lower_minus_F_upper=str(budget[0]-fu),F_lower_minus_K_upper=str(fl-budget[1]),
    D_U_diagonal_error=enc(bprice),a_cross_error=enc(crossprice),a_square_positive_error=enc(extra_sq),eta_upper=enc(eta_hi))
result.update(c=str(cap), beta=str(beta), residual_P_norm_upper=str(zup),
    finite_residual_error_terms={k:enc(v) for k,v in dict(model=sq(quad(P,nmodel)),nu=nu_error,
        D=(1+eta)*d_action,U=u_action,square=square_error).items()},
    d_boundary=enc(dstar),sufficient_d=str(dcap),conditional_full_upper=enc(conditional)[1],
    conditional_margin=str(budget[0]-F(enc(conditional)[1])),
    actual_whole_residual_certified=False,odd_witness_pass=None,
    point4_closed=False, status="AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN")
# b = v - a_fin Jw is formed before the final application of the inverse.
# The physical outer-source error, a-action error and rationalization all
# enter in the same old 12-dimensional K-inverse norm.
force_model = seed.v*coeff-a0*w
force_rows = [nearest(force_model[i,0],10**60) for i in range(12)]
force_diff = force_model-arb_mat([[q(x)] for x in force_rows])
# trace(Ki) bounds its spectral norm, also valid for interval rounding errors.
force_rounding = sq(trace(Ki))*norm(force_diff)
force_error = (pcert["feature_error_norms"]["K_inverse_v"]+
               seed.bounds["v_feature_operator_norm_upper"]*seed.eResidual+ea+force_rounding)
result["grouped_force_before_K_inverse"] = list(map(str,force_rows))
result["grouped_force_error_K_inverse_upper"] = enc(force_error)[1]
print("grouped force error",sci(enc(force_error)[1]),flush=True)
Path(sys.argv[2]).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
