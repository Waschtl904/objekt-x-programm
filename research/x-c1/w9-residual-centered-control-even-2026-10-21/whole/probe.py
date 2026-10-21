"""Exploratory coupled-rest diagnostics. No certificate or full-energy claim."""
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import ModuleType
from flint import arb, arb_mat, ctx

ROOT = Path(__file__).resolve().parents[1] / 'objekt-x-integration-20261019'
OUT = Path(__file__).resolve().parent
PKG = ROOT / 'research/x-c1/w9-new-k-schur-underform-even-2026-10-20'
ctx.prec = 1024

def module(name, path):
    raw = path.read_bytes()
    m = ModuleType(name)
    m.__file__ = str(path)
    sys.modules[name] = m
    exec(compile(raw, str(path), 'exec'), m.__dict__)
    return m

manifest = json.loads((PKG/'MANIFEST.json').read_bytes())
for name in ('engine.py', 'INPUT_BINDINGS.json', 'CANDIDATE.json', 'RESULT.json'):
    assert hashlib.sha256((PKG/name).read_bytes()).hexdigest() == manifest[name]
eng = module('new_k_probe_engine', PKG/'engine.py')
spec, data = eng.snapshot(ROOT, (PKG/'INPUT_BINDINGS.json').read_bytes())
env = eng.load(ROOT, spec, data)
c = env['common']
q, mat, quad = c.q, c.mat, eng.quad
w = arb_mat([[q(v)] for v in json.loads((PKG/'CANDIDATE.json').read_bytes())['raw_coefficients']])
e = env['energy']
case = env['inp'].json('common')['cases'][0]
raw = env['inp'].json('old_sources')['cases'][0]
UJ = arb_mat([[env['U'][i,j] for j in range(12,96)] for i in range(12,96)])
EJ = 2*(c.box(case['tail_feature_error_scalar']) + c.box(raw['galerkin']['high_source_error_norm'])**2/e.w['delta'])
ew = EJ*(w.transpose()*w)[0,0]
uw = quad(UJ,w)
directional_u = 2*(uw*ew).sqrt()+ew
DL, DU = mat(case['D96_lower_model']), mat(case['D96_upper_model'])
Ddiff = arb_mat([[(DU[i,j]-DL[i,j])/2 for j in range(12,96)] for i in range(12,96)])
directional_d = quad(Ddiff,w)
old = json.loads((PKG/'RESULT.json').read_bytes())
rest = json.loads((ROOT/'research/x-c1/w9-rest-feasibility-even-2026-10-20/RESULT.json').read_bytes())
new_price = directional_u+directional_d
old_price = c.box(old['form_common_D_U_error'])
new_Fup = q(rest['F_interval'][1])-old_price+new_price
new_Flo = q(rest['F_interval'][0])+old_price-new_price
budget = c.box(rest['budget_interval'])
result = {'status':'EXPLORATORY_NOT_A_CERTIFICATE', 'source_main':'639d25e38b453f2e10b859553ca49a7a0e4fafdb',
    'old_common_price':c.enc(old_price), 'directional_U_price':c.enc(directional_u),
    'directional_D_price':c.enc(directional_d), 'proposed_F_interval':[c.enc(new_Flo)[0],c.enc(new_Fup)[1]],
    'proposed_margin':c.enc(budget-new_Fup), 'full_residual_computed':False,
    'new_physical_witness':False, 'milestone_4_closed':False}
def approx(x):
    return float(Q(str(x.mid().fmpq())))
print('FORM', json.dumps({k:[float(Q(s)) for s in v] if isinstance(v,list) else v for k,v in result.items()}), flush=True)

# Residual-centered use of the existing inverse theorem. Unlike #247 this
# applies the majorant to r=nu-HJw, not to nu itself.
Pup=e.w['P']; Ki=e.w['Ki']; a=e.w['a']; GF=e.w['GF']; GJ=e.w['GJ']
tr=c.trace
UF=arb_mat([[env['U'][i,j] for j in range(12)] for i in range(12)])
EF=2*(mat(case['finite_feature_error_gram'])+mat(raw['old_certificate']['joint_high_source_error_gram'])/e.w['delta'])
dd=e.bounds['direct_energy_relative_error_upper']
rcoef=Ki*a*w
gr=quad(GF,rcoef); ur=quad(UF,rcoef); er=quad(EF,rcoef)
gw=quad(GJ,w)
tpG=tr(Pup*GJ); tpU=tr(Pup*UJ); tpE=EJ*tr(Pup)
tkG=tr(Ki*GF); tkU=tr(Ki*UF); tkE=tr(Ki*EF)
root=lambda x: eng.norm_upper(x)
ea_direction=dd*root(tkG*gw)+root(tkU*ew)+root(tkE*uw)+root(tkE*ew)
delta_a_left=dd*root(gr*tpG)+root(tpU*er)+root(tpE*ur)+root(tpE*er)
delta_a_HS=dd*root(tkG*tpG)+root(tkU*tpE)+root(tkE*tpU)+root(tkE*tpE)
a0_HS=root(tr(Pup*a.transpose()*Ki*a))
err_square=delta_a_left+(a0_HS+delta_a_HS)*ea_direction
err_U=root(tpU*ew)+root(tpE*uw)+root(tpE*ew)
err_D=root(tr(Pup*Ddiff)*directional_d)
eta=q('1e-10')
DJ=arb_mat([[(DU[i,j]+DL[i,j])/2 for j in range(12,96)] for i in range(12,96)])
nmodel=env['nu']-env['H0']*w+eta*DJ*w
prior=json.loads(data['pilot_result'])
pweight=q(prior['P_weight'])
err_nu=c.box(prior['feature_error_norms']['P_upper_J_star_nu'])/pweight.sqrt()
err_nu+=c.box(prior['residual_model_error_norm'])/pweight.sqrt()
zr=root(quad(Pup,nmodel))+err_nu+(1+eta)*err_D+err_U+err_square
margin=q(rest['budget_interval'][0])-new_Fup
cap=q(rest['c']); beta=q(rest['beta'])
target=None
if (1-cap)*margin > zr**2:
    target=beta*(((1-cap)*(margin-zr**2)).sqrt()-cap.sqrt()*zr)**2
pieces={'nu_error_P_norm':err_nu,'D_action_error_P_norm':err_D,
        'U_action_error_P_norm':err_U,'a_square_action_error_P_norm':err_square,
        'a_direction_Ki_error':ea_direction,'a_left_error_P_norm':delta_a_left,
        'a0_HS_P_Ki':a0_HS,'residual_P_norm_upper':zr,
        'remaining_energy_allowance':margin}
result['residual_centered_finite_diagnostic']=c.encode(pieces)
result['sufficient_full_residual_Ldual_energy_upper']=None if target is None else c.enc(target)
print('RESIDUAL',json.dumps({k:approx(v) for k,v in pieces.items()}),flush=True)
print('FULL_RESIDUAL_TARGET',None if target is None else c.enc(target),flush=True)

# Midpoint-only trade-off in the stored response Gram. This does not bound
# the whole residual: the extra terms in nu-Ht must still be controlled.
fin = json.loads((ROOT/'research/x-c1/w9-rest-feasibility-even-2026-10-20/FINITE.json').read_bytes())
P = c.ratmat(fin['P_lower_rational'])
for i,d in enumerate(fin['P_lower_to_upper_diagonal']): P[i,i] += q(d)/2
P = arb_mat([[P[i,j].mid() for j in range(84)] for i in range(84)])
H = arb_mat([[env['H0'][i,j].mid() for j in range(84)] for i in range(84)])
nu = arb_mat([[env['nu'][i,0].mid()] for i in range(84)])
base = sum((quad(e.components[k],env['c']) for k in ('high_U8','finite_U8','K_inverse_v')),arb(0))
base = base.mid()
I = arb_mat([[int(i==j) for j in range(84)] for i in range(84)])
beta = q(rest['beta']); cap=q(rest['c'])
rows=[]
for power in [0,-2,-4,-6,-8,-10,-12,-16,-20,-24,-32,-40]:
    lam=q(str(Q(10)**power))
    y=(H*P+lam*I).solve(nu)
    trial=P*y
    cost=quad(P,y)
    gain=2*(nu.transpose()*trial)[0,0]-quad(H,trial)
    deficit=quad(H,trial-w)
    row={'lambda':str(Q(10)**power),'model_F':approx(base+gain),'model_variational_loss':approx(deficit),
         'model_E_cost':approx(cost),'model_Ru_Ldual_bound_expression':approx(cap*beta*cost),
         'coefficient_norm':approx(eng.norm_upper((trial.transpose()*trial)[0,0]))}
    rows.append(row); print('TRADEOFF',json.dumps(row),flush=True)
result['regularization_model_tradeoff']=rows
(OUT/'probe-result.json').write_bytes((json.dumps(result,indent=2)+'\n').encode())
