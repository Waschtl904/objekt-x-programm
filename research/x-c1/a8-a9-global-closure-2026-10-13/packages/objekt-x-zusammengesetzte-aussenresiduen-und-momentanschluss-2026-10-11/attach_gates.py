"""Bind the new responses to the full infinite L-dual reduction."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import interval_helpers as h
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
NEW=ROOT/'work/new-responses84-2026-10-11'
REF=ROOT/'work/direct-rest84-2026-10-11'
REVIEW=ROOT/'work/infinite-dual-review-input-2026-10-11/Objekt-X-Unendlicher-Dualrest-und-Aussenrichtungen-2026-10-11'
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 assert __debug__
 ref=read(REF/'REFINED_COMMON96.json')['cases'];audit=read(NEW/'AUDIT.json')['cases'];geo=read(REVIEW/'data/INFINITE_REDUCTION.json')
 rows=[]
 for p,label in enumerate(['EVEN','ODD']):
  path=NEW/f'RESPONSES_{label}.json';d=read(path);n=ref[p];rho=F(d['rho'])
  K=h.rat(d['K12_new_rational']);Kold=h.rat([row[:12] for row in n['G96_rational'][:12]])
  eps=F(n['common96_positive_reserve_relative_to_G'])
  proof=h.ld.positive(h.pts([[K[i][j]-eps*Kold[i][j] for j in range(12)] for i in range(12)]))
  den=10**60;xi=[[int(F(v)*den) for v in row] for row in d['X84x203_rational']]
  xnorm2=F(sum(v*v for row in xi for v in row),den**2);assert xnorm2<10**40
  Ki=h.inv(K);dinvtrace=F(191)/(1-rho)+h.tr(Ki)
  model_norm=F(audit[p]['finite_model_residual_norm_upper'])
  model_weighted=model_norm*h.sqrtup(dinvtrace)
  ce=F(d['C_inverse_D_metric_error'][1]);be=F(d['B84_operator_error'][1]);x2=F(d['fixed_X_squared_HS_in_D_inverse_metric'][1])
  rj=model_weighted+ce+be*h.sqrtup(x2)
  jprice=F(5,21)*rj*rj
  # W<= (19/9)I <3I. The earlier full WX-dual norm estimate, not a
  # finite projected residual, therefore controls the canonical X norm.
  oldcap=F(audit[p]['full_coarse_QR_normalized_upper_audited'])
  mr_x2=F(63,5)*oldcap
  geometry=F(geo['projection_correction_per_full_residual_norm_squared'])*mr_x2
  assert mr_x2<10**100 and geometry<F(1,10**300)
  gprice=F(1,10**300)
  budget=F(d['sufficient_complete_QR_normalized_budget'])-jprice-gprice
  assert budget>0
  rows.append({'parity':label.lower(),'Knew_ge_epsilon_Kold':proof,'epsilon':str(eps),
   'X_Frobenius_squared_exact':str(xnorm2),'X_Frobenius_bound_1e20_checked':True,
   'actual_RJ_D_inverse_metric_norm_upper':str(rj),'basis84_dual_contribution_relative_to_D_upper':str(jprice),
   'full_canonical_X_residual_squared_norm_upper':str(mr_x2),
   'geometric_correction_computed_upper':str(geometry),'geometric_correction_charged':'1e-300',
   'remaining_scalar_budget_for_weighted_exterior_sum':str(budget),
   'remaining_matrix_budget_definition':'beta*(D203-M_upper) - (basis84_price + 1e-300)*D203',
   'full_exterior_sum_certified':False,'full_remainder_certified':False,
   'bindings':{path.name:sha(path),'previous_response_AUDIT.json':sha(NEW/'AUDIT.json'),'REFINED_COMMON96.json':sha(REF/'REFINED_COMMON96.json'),'INFINITE_REDUCTION.json':sha(REVIEW/'data/INFINITE_REDUCTION.json')}})
  print(label,'PASS both geometry gates; X norm <',float(h.sqrtup(xnorm2)),'RJ price <',float(jprice),'outside budget',float(budget),flush=True)
 out={'status':'PASS_ACTUAL_RESPONSE_GATES_BASIS_RESIDUAL_AND_FULL_MOMENT_PRICE','cases':rows,'full_remainder_certified':False}
 (HERE/'ATTACHMENT_GATES.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
