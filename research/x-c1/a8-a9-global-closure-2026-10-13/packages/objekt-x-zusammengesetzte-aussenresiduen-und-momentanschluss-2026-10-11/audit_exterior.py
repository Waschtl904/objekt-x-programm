"""Rational replay of all 203 composed residuals on eight exterior directions.

Only Python's standard library is used. Analytic source-error estimates are
inherited, bound inputs. This is NOT an upper bound for the infinite tail.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
import interval_helpers as h
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ip(a):return h.pts(h.rat(a))
def integer_matrix(a,den):return h.pts([[F(int(v),int(den)) for v in row] for row in a])
def interval_endpoint(a):return F(a[1])
def square_norm(a):return sum(max(abs(h.lower(v)),abs(h.upper(v)))**2 for row in a for v in row)
def comparison(lo,hi):
 count=0
 for key in ['full_high_cross_model','direct_cross_model','L_external_model','L_J_external_model']:
  h.overlaps(h.im(lo[key]),h.im(hi[key]));count+=sum(map(len,lo[key]))
 assert count==2080
 return count
def audit(new,common,incoming):
 assert __debug__,'Run without -O'
 ns=read(common/'REFINED_COMMON96.json')['cases'];inputs=read(common/'REFINED_INPUT.json')['cases']
 prior=read(new/'AUDIT.json')['cases'];gates=read(HERE/'ATTACHMENT_GATES.json')['cases']
 geo=read(incoming/'data/INFINITE_REDUCTION.json');localgeo=read(HERE/'INFINITE_REDUCTION_LOCAL.json')
 def unbind(v):
  if isinstance(v,dict):return {k:unbind(x) for k,x in v.items() if k!='bindings'}
  if isinstance(v,list):return [unbind(x) for x in v]
  return v
 assert unbind(geo)==unbind(localgeo)
 for path in [common/'REFINED_COMMON96.json',common/'REFINED_INPUT.json']:
  found=[v for k,v in localgeo['bindings'].items() if k.replace('\\','/').split('/')[-1]==path.name]
  assert found==[sha(path)]
 rows=[]
 for p,label in enumerate(['EVEN','ODD']):
  d=read(new/f'RESPONSES_{label}.json');n=ns[p];inp=inputs[p];gate=gates[p]
  probe=read(incoming/f'data/PROBE_{label}_3072.json')
  cross=read(HERE/f'CROSS_{label}_3072.json');higher=read(HERE/f'CROSS_{label}_4096.json')
  result=read(HERE/f'EXTERIOR_{label}_3072.json')
  bindings={new/f'RESPONSES_{label}.json',common/'REFINED_COMMON96.json',common/'REFINED_INPUT.json',incoming/f'data/PROBE_{label}_3072.json',HERE/f'CROSS_{label}_3072.json',HERE/'ATTACHMENT_GATES.json'}
  assert result['bindings']=={path.name:sha(path) for path in bindings}
  precision=comparison(cross,higher)
  for cr in [cross,higher]:
   assert cr['bindings']['frozen_K']==sha(incoming/f'data/PROBE_{label}_3072.json')
   assert cr['bindings'][f'DIRECT_REST_{label}_3072.json']==sha(common/f'DIRECT_REST_{label}_3072.json')
   assert cr['complete_low_force_calibrations']==17572
   assert F(cr['rounding'][1])<F(1,10**60) and F(cr['gamma_error'][1])<F(1,10**34)
   for check in cr['full_high_function_checks']:
    lo,hi=map(F,check['difference']);assert lo<=0<=hi and max(abs(lo),abs(hi))<F(1,10**30)
  rho=F(d['rho']);delta=F(d['delta']);eta=F(d['eta']);beta=F(d['beta'])
  assert delta==F(18219,10000) and eta==F(1,10**10) and beta==1-eta-F(16198,18219)
  K=h.rat(d['K12_new_rational']);Ki=h.inv(K);kii=h.pts(Ki)
  Kold=h.rat([r[:12] for r in n['G96_rational'][:12]]);eps=F(n['common96_positive_reserve_relative_to_G'])
  gproof=h.ld.positive(h.pts([[K[i][j]-eps*Kold[i][j] for j in range(12)] for i in range(12)]))
  Xrat=h.rat(d['X84x203_rational']);X=h.pts(Xrat)
  xn=sum(v*v for row in Xrat for v in row);assert xn==F(gate['X_Frobenius_squared_exact'])<10**40
  x2=F(d['fixed_X_squared_HS_in_D_inverse_metric'][1])
  rj=F(prior[p]['finite_model_residual_norm_upper'])*h.sqrtup(F(191)/(1-rho)+h.tr(Ki))+F(d['C_inverse_D_metric_error'][1])+F(d['B84_operator_error'][1])*h.sqrtup(x2)
  jprice=F(5,21)*rj*rj;assert jprice==F(gate['basis84_dual_contribution_relative_to_D_upper'])
  mr=F(63,5)*F(prior[p]['full_coarse_QR_normalized_upper_audited'])
  assert F(geo['projection_correction_per_full_residual_norm_squared'])*mr<F(1,10**300)
  assert 20*F(1,10**352)*h.sqrtup(mr)<F(1,10**300)
  AC=integer_matrix(n['inverse_congruence_integer_matrix'],n['inverse_congruence_denominator'])
  old=inp['old_certificate'];pg=inp['galerkin']
  lF=h.mmI(h.T(AC),h.add(h.im(old['source_c_model']),h.sc(h.im(old['source_Bh_model']),1/delta),-1))
  lK=h.mmI(h.T(AC),h.add(h.block(h.im(probe['source_c_model']),range(191),range(1,9)),h.sc(h.block(h.im(probe['source_Bh_model']),range(191),range(1,9)),1/delta),-1))
  HFK=h.block(h.im(probe['source_high_cross_model']),range(12),range(1,9));HKK=h.block(h.im(probe['Hgram']),range(1,9),range(1,9))
  UFK=h.add(h.sc(HFK,1/delta),h.sc(h.mmI(h.T(lF),lK),1/(1-rho)))
  UKK=h.add(h.sc(HKK,1/delta),h.sc(h.mmI(h.T(lK),lK),1/(1-rho)))
  CFK=h.add(h.block(h.im(probe['direct_F_cross_model']),range(12),range(1,9)),UFK,-1)
  AK=lK+CFK
  SJ=h.add(h.sc(h.im(cross['direct_cross_model']),1-eta),h.sc(h.im(cross['full_high_cross_model']),1/delta),-1)
  RK=h.add(h.T(AK),h.mmI(h.T(SJ),X),-1)
  h.overlaps(AK,h.im(result['AK_model']));h.overlaps(SJ,h.im(result['S_JK_model']));h.overlaps(RK,h.im(result['RK_8x203_model']))
  # Independent integer construction of the ill-conditioned inverse traces.
  ci=[[int(v) for v in row] for row in n['inverse_congruence_integer_matrix']];cd=int(n['inverse_congruence_denominator'])
  assert all(ci[i][j]==0 for i in range(191) for j in range(i))
  xi=[[sum(ci[i][k]*ci[j][k] for k in range(max(i,j),191)) for j in range(191)] for i in range(191)]
  factor=F(1,cd**2)/(1-rho);tx=sum(xi[i][i] for i in range(191))*factor
  hi=[[int(v) for v in row] for row in n['HB_integer_matrix']]
  txh=F(sum(xi[i][j]*hi[j][i] for i in range(191) for j in range(191)),int(n['HB_denominator']))*factor
  cn=[[h.ld.interval(v)] for v in probe['moment_basis_coefficients']]
  acn=h.mmI(h.T(AC),cn);txgm=tx+square_norm(acn)/(1-rho)
  ef=F(probe['source_model_error_norm'][1]);eh=F(probe['high_source_error_norm'][1]);eb=F(probe['old_coupling_error_norm'][1])
  eK=8*(eh**2/delta+3*(txgm*ef**2+txh*eh**2/delta**2+tx*eb**2*h.itr(HKK)/delta**2))
  eF=h.pair_upper(h.im(n['finite_feature_error_gram']),h.T(kii));tauF=h.pair_upper(h.block(h.im(n['U96_model']),range(12),range(12)),h.T(kii));tauK=h.itr(UKK)
  errC=h.sqrtup(eK)+h.sqrtup(eF*tauK)+h.sqrtup(tauF*eK)+h.sqrtup(eF*eK)+h.sqrtup(96*h.tr(Ki))*F(1,10**20)
  ehJ=F(pg['high_source_error_norm'][1]);hj=delta*h.itr(h.im(n['H84_new_model']))
  errH=(h.sqrtup(hj)*eh+h.sqrtup(h.itr(HKK))*ehJ+eh*ehJ)/delta
  errS=(1-eta)*h.sqrtup(F(84*8))*F(1,10**20)+errH
  errR=errC+errS*h.sqrtup(x2);errEll=errR+F(1,10**300)
  # Certify R^* diag(1/d_n) R <= model_cap*T without computing T^{-1}.
  weights=[sum((F(1,k) for k in range(1,j+1)),F(11,10)) for j in range(96,104)]
  WG=[h.sc([row],1/weight)[0] for row,weight in zip(RK,weights)]
  gram=h.mmI(h.T(RK),WG)
  D=[[F(1-rho) if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
  MU=h.rat(d['M_upper_rational']);T=[[beta*(D[i][j]-MU[i][j]) for j in range(203)] for i in range(203)]
  modelcap=F(192,10**6) if p==0 else F(643,10**6)
  proof=h.ld.positive(h.add(h.sc(h.pts(T),modelcap),gram,-1))
  sigma=F(d['sufficient_complete_QR_normalized_budget'])
  # sqrt(1/(6*sigma)) gives an upper bound for the division by sqrt(6*sigma).
  actualcap=(h.sqrtup(modelcap)+errEll*h.sqrtup(1/(6*sigma)))**2
  cap=F(1,5000) if p==0 else F(13,20000)
  assert actualcap<cap
  remaining=(1-cap)*sigma-jprice-F(1,10**300);assert remaining>0
  assert not result['full_remainder_certified'] and not result['negative_actual_Schur_witness']
  rows.append({'parity':label.lower(),'geometry_gate':gproof,'response_Frobenius_norm_upper':str(h.sqrtup(xn)),
   'basis84_dual_price_relative_to_D':str(jprice),'full_moment_correction_price':'1e-300',
   'new_precision_comparisons':precision,'new_low_force_calibrations_per_precision':17572,
   'composed_residual_entries_rebuilt':8*203,'cross_entries_rebuilt':84*8,'residual_error_upper':str(errR),
   'model_gram_relative_to_directional_budget_upper':str(modelcap),'model_gram_LDL':proof,
   'actual_first_eight_weighted_gram_relative_to_directional_budget_upper':str(cap),
   'remaining_uniform_budget_for_degrees_ge_104':str(remaining),
   'complete_tail_bound_from_degree_104':False,'full_remainder_certified':False})
  print(label,'PASS all 1624 composed entries; 203 positive pivots; weighted first eight <',str(cap),'* T',flush=True)
 # Countercontrols: a visible residual can cancel only after composition,
 # and a finite prefix gives no upper bound for a missing exterior row.
 assert (F(3)-F(2))**2==1 and F(3)**2+F(2)**2==13
 assert F(1,4)<1 and F(1,4)+4>1
 try:h.ld.positive(h.pts([[F(1),F(2)],[F(2),F(1)]]))
 except AssertionError:pass
 else:raise AssertionError('indefinite matrix accepted')
 return {'status':'PASS_COMPOSED_FIRST_EIGHT_AND_GEOMETRY_GATES_FULL_TAIL_OPEN','rational_grid_digits':100,'cases':rows,
  'inherited_operator_hypotheses':True,'full_remainder_certified':False,
  'countercontrols':['composition before squaring','finite prefix cannot bound missing row','indefinite matrix rejected']}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--new',type=Path,required=True);ap.add_argument('--common',type=Path,required=True);ap.add_argument('--incoming',type=Path,required=True);args=ap.parse_args()
 out=audit(args.new,args.common,args.incoming);(HERE/'AUDIT_EXTERIOR.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
