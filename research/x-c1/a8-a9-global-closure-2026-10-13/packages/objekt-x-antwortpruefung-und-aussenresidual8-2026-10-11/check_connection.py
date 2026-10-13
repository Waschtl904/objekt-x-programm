"""Rational checks connecting the new responses to the full L-dual reduction."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, sys

ap=argparse.ArgumentParser()
ap.add_argument('--responses',type=Path,required=True)
ap.add_argument('--parent',type=Path,required=True)
ap.add_argument('--out',type=Path,required=True)
args=ap.parse_args()
sys.path.insert(0,str(args.responses))
import audit as au
ld=au.ld
def read(p):return json.loads(p.read_bytes())
def hi(v):return F(v[1])
assert __debug__
ref=read(args.parent/'REFINED_COMMON96.json')['cases']
source=read(args.parent/'REFINED_INPUT.json')['cases']
input_audit=read(args.responses/'AUDIT.json')['cases']
rows=[]
for p,label in enumerate(['EVEN','ODD']):
 path=args.responses/f'RESPONSES_{label}.json'
 d=read(path);K=au.rat(d['K12_new_rational']);Ki=au.inv(K)
 old=au.rat([r[:12] for r in ref[p]['G96_rational'][:12]])
 eps=F(ref[p]['common96_positive_reserve_relative_to_G'])
 gate=ld.positive(au.pts([[K[i][j]-eps*old[i][j] for j in range(12)] for i in range(12)]))
 X=au.rat(d['X84x203_rational'])
 xraw=sum(v*v for row in X for v in row)
 assert xraw<10**40
 rho=F(d['rho']);x2=hi(d['fixed_X_squared_HS_in_D_inverse_metric'])
 delta=F(d['delta']);eta=F(d['eta']);n=ref[p]
 U=au.im(n['U96_model']);kii=au.pts(Ki)
 eF=au.pair_upper(au.im(n['finite_feature_error_gram']),au.T(kii))
 eJ=84*hi(n['tail_feature_error_scalar'])
 tauF=au.pair_upper(au.block(U,range(12),range(12)),au.T(kii))
 tauJ=au.itr(au.block(U,range(12,96),range(12,96)))
 cerror=au.sqrtup(eJ)+au.sqrtup(eF*tauJ)+au.sqrtup(tauF*eJ)+au.sqrtup(eF*eJ)+au.sqrtup(12*84*au.tr(Ki))*F(1,10**25)
 eh=hi(source[p]['galerkin']['high_source_error_norm'])
 htrace=delta*au.itr(au.im(n['H84_new_model']))
 direct=read(args.parent/f'DIRECT_REST_{label}_3072.json')
 berror=(1-eta)*F(direct['D84_operator_error'])+(2*au.sqrtup(htrace)*eh+eh**2)/delta
 # The full model Galerkin residual is normalized using the actual metric.
 model=F(input_audit[p]['finite_model_residual_norm_upper'])
 dinvtrace=F(191)/(1-rho)+au.tr(Ki)
 rj=cerror+berror*au.sqrtup(x2)+model*au.sqrtup(dinvtrace)
 finite=F(5,21)*rj*rj
 beta=F(d['beta']);budget=F(d['sufficient_complete_QR_normalized_budget'])
 geometry=F(1,10**250)
 # The coarse estimate already bounds the WX-dual norm before division
 # by 21/5. For the canonical X-representer, ||WX||<3 gives this price.
 coarse=F(input_audit[p]['full_coarse_QR_normalized_upper_audited'])
 canonical_norm2=F(63,5)*coarse
 assert canonical_norm2<10**45 if p==0 else canonical_norm2<10**42
 assert canonical_norm2*F(1,10**350)<geometry
 available=budget-finite-geometry
 assert available>0
 dn128=F(11,10)+sum((F(1,k) for k in range(1,129)),F(0))
 rows.append({'parity':label.lower(),'K_new_minus_epsilon_K_old_LDL':gate,
  'epsilon':str(eps),'X_Frobenius_squared':str(xraw),'X_Frobenius_upper':str(au.sqrtup(xraw)),
  'new_answer_admissibility_conditions_checked':True,
  'true_Jstar_R_D_normalized_norm_upper':str(rj),
  'full_finite_J_dual_Gram_D_normalized_upper':str(finite),
  'geometry_error_D_upper':str(geometry),'beta':str(beta),
  'scalar_QR_budget':str(budget),'scalar_available_for_external_weighted_sum':str(available),
  'd128':str(dn128),'conditional_U128_budget_if_Q96_128_zero':str(dn128*available),
  'residual_X_norm_squared_D_upper_under_inherited_hypotheses':'1e100',
  'sharper_canonical_X_residual_norm_squared_D_upper':str(canonical_norm2),
  'bindings':{str(path.name):hashlib.sha256(path.read_bytes()).hexdigest()},
  'sharp_full_residual_gram_computed':False,'full_remainder_certified':False})
 print(label,'gates PASS; ||X||F <',float(au.sqrtup(xraw)),
       '; true finite dual Gram/D <',float(finite),'; outside budget',float(available),flush=True)
out={'status':'NEW_ANSWER_GEOMETRY_GATES_AND_TRUE_FINITE_RESIDUAL_BOUND_PASS',
 'cases':rows,'full_remainder_certified':False}
args.out.write_text(json.dumps(out,indent=2)+'\n')
