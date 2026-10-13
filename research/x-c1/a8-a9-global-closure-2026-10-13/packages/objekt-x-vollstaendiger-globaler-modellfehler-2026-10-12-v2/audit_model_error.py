"""Outward rational assembly of the complete physical model error.

Analytic hypotheses and binding to the implemented raw function are stated
in PROOF.txt. This does not certify the still uncomputed global model Gram.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json,gzip,argparse,hashlib
HERE=Path(__file__).resolve().parent;DEFAULT_ROOT=HERE.parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=DEFAULT_ROOT);ap.add_argument('--exterior',type=Path,default=HERE);ap.add_argument('--exterior-bits',type=int,choices=[3072,4096],default=3072);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();ROOT=args.root
sys.path.insert(0,str(HERE));sys.path.insert(1,str(DEFAULT_ROOT/'work/global-model-2026-10-12'))
import interval_helpers as h
from audit_exterior import audit as audit_exterior
def read(p):
 b=p.read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)
def up(v):return F(v[1])
def trace(v):return sum((v[i][i] for i in range(len(v))),F(0))
def weighted_trace(Ki,ei):
 return h.itr(h.mmI(h.pts(Ki),h.im(ei)))
oldpath=ROOT/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/remainder-integration-check-v2/originals/weighted-response/inputs/a8_model.json.gz'
old=read(oldpath);epsold=F(old['Gamma_kernel_error_exact'])
source=read(ROOT/'work/direct-rest84-2026-10-11/REFINED_INPUT.json')['cases']
rows=[]
for p,label in enumerate(['EVEN','ODD']):
 rpath=ROOT/f'work/new-responses84-2026-10-11/RESPONSES_{label}.json';r=read(rpath)
 c=read(ROOT/f'work/inner-log-2026-10-12/COMPOSED_{label}_3072.json')
 extpath=args.exterior/f'EXTERIOR_{label}_{args.exterior_bits}.json';ext=read(extpath)
 assert ext['status']=='COMPLETE_GLOBAL_EXTERIOR_BOUND'
 delta=F(r['delta']);rho=F(r['rho']);co=r['full_coarse_inputs']
 Ki=h.inv(h.rat(r['K12_new_rational']));tk=trace(Ki)
 xd=h.sqrtup(up(r['fixed_X_squared_HS_in_D_inverse_metric']))
 lowmodel=read(ROOT/'work/inner-log-2026-10-12/INNER_LOG_1536.json')['cases'][p]['new_low_F_model']
 radius2=sum(((F(v[1])-F(v[0]))**2/4 for rr in lowmodel for v in rr),F(0))
 low_round=h.sqrtup(radius2*tk)
 assert low_round<F(1,10**40)
 epslow=h.sqrtup(up(r['finite_feature_error_metric_trace']))+F(1,10**40)
 # Inherited full cross-operator norm <16/5, enlarged to 4.
 kop=F(4)
 exterior=F(audit_exterior(ext)['complete_exterior_HS_norm_upper'])
 hb=h.sqrtup(up(co['inverse_HB_trace']))
 # ||T_h||<2 and BB*<=HB. The first term is the NEW full exterior bound.
 KV=exterior+2*kop*hb/delta
 lowprice=KV*epslow/(1-rho)
 qnorm=up(c['old_q_polynomial_D_HS_norm'])+F(1,10**40)
 oldprice=8*epsold*qnorm/delta
 # Full source-function error per J/Y/z column, not just endpoint error.
 sourceweight=h.sqrtup(F(84))*xd+h.sqrtup(12*tk)
 assert qnorm<10**16 and sourceweight<10**8
 directprice=F(1,10**28)*sourceweight
 ecF=h.sqrtup(weighted_trace(Ki,source[p]['old_certificate']['joint_low_source_error_gram']))
 ecJ=up(source[p]['galerkin']['source_model_error_norm'])*xd
 sourceprice=(5*directprice+2*(ecF+ecJ))/delta
 # Raw-carrier/frozen-coordinate arithmetic and moment-projection correction.
 projectionprice=F(1,10**40)
 fixedWprice=oldprice+sourceprice+projectionprice
 tau=up(co['actual_finite_response_metric_trace']);mv=up(co['low_feature_HS_squared_WX'])
 Wcap=h.sqrtup(mv)/1000*(1+h.sqrtup(tau))+2/delta*(2000*h.sqrtup(F(2))*xd+h.sqrtup(delta*tau))
 Vcore=h.sqrtup(2*up(co['inverse_trace']))+2*hb/delta
 coreDifference=Vcore*epslow/(1-rho)+fixedWprice
 assert coreDifference<Wcap
 # Complete uniform degree-224 kernel error <1e-34, including both parities.
 outerprice=8*F(1,10**34)*Wcap
 physical=directprice+lowprice+kop*fixedWprice+outerprice
 smooth=F(1,10**300);total=physical+smooth
 target=F('0.000000676796364171' if p==0 else '0.000001628860045447')
 assert total<target
 simplecap=F(('1.2e-11' if p==0 else '2.3e-13') if args.exterior_bits==3072 else ('2e-11' if p==0 else '4e-13'))
 assert total<simplecap
 u=F('0.000001832433' if p==0 else '0.000010613269')
 logerror=F(1,10**10);epsilon=F(1,1000)
 assert 4*(total+logerror)**2<epsilon**2*u
 print(label,'PASS full physical error',float(physical),'target',float(target),flush=True)
 rows.append({'parity':label.lower(),'complete_cross_operator_norm_cap':str(kop),
  'complete_K_Vstar_HS_bound':str(KV),'low_feature_error_price':str(lowprice),
  'low_F_midpoint_D_dual_radius_upper':str(low_round),'low_F_midpoint_radius_price':'1e-40',
  'fixed_q_Gamma160_W_error':str(oldprice),'complete_source_projection_W_error':str(sourceprice),
  'carrier_rounding_and_high_projection_W_price':str(projectionprice),
  'direct_shell_function_error':str(directprice),'complete_external_kernel_error':str(outerprice),
  'complete_raw_physical_model_error':str(physical),'omitted_smooth_correction_norm_price':str(smooth),
  'complete_canonical_high_model_error':str(total),'simple_complete_model_error_cap':str(simplecap),
  'full_L2_error_budget_with_rounded_log_passes':True,
  'available_L2_model_error_budget':str(target),'budget_fraction':str(total/target),
  'core_W_actual_norm_cap':str(Wcap),'core_W_difference_bound':str(coreDifference),
  'response_sha256':hashlib.sha256(rpath.read_bytes()).hexdigest(),'exterior_sha256':hashlib.sha256(extpath.read_bytes()).hexdigest()})
out={'status':'PASS_COMPLETE_GLOBAL_MODEL_ERROR_CONDITIONAL_ON_INHERITED_OPERATORS',
 'cases':rows,'complete_global_model_error_certified':True,'global_model_Gram_computed':False,
 'tail_floor_1_over_20_certified':False,'full_remainder_certified':False}
args.out.write_text(json.dumps(out,indent=2)+'\n')
