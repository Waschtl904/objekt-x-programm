"""Rational GLOBAL target budgets after all three logarithmic components.

No value for the remaining global integral is computed or inferred here.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json,zipfile
import interval_helpers as h
HERE=Path(__file__).resolve().parent
HASHES={
 'responses':'5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3',
 'log':'96b8367c5f49ab8b99f63aade251942221a3fcad50ba09c6acb3a662e0dd8016',
 'review':'869a8b518825ed73a440cc82f0dfaba7f8f70c330931c2f4571ee6e880d684a0'}
def readzip(path,relative):
 with zipfile.ZipFile(path) as z:
  root=path.stem+'/'
  return json.loads(z.read(root+relative))
def floor_grid(v):return F((v*10**12).numerator//(v*10**12).denominator,10**12)
def rootiv(v,digits=70):
 den=10**digits;n=isqrt(v.numerator*den**2//v.denominator)
 return F(n,den),F(n+1,den)
def main(args):
 assert __debug__
 for key,want in HASHES.items():
  path=getattr(args,key+'_zip');assert hashlib.sha256(path.read_bytes()).hexdigest()==want,key
 logaudit=readzip(args.log_zip,'AUDIT.json');oldscope=readzip(args.review_zip,'data/INDEPENDENT_GEOMETRY.json')
 assert logaudit['status']=='PASS_COMPLETE_THREE_LOG_COMPONENT_TAIL'
 # Bound inherited geometric gates from the immutable nested input.
 with zipfile.ZipFile(args.log_zip) as zz:
  from io import BytesIO
  name='Objekt-X-Aussenresidualpruefung-und-Logarithmischer-Randtail-2026-10-11'
  with zipfile.ZipFile(BytesIO(zz.read(args.log_zip.stem+'/inputs/'+name+'.zip'))) as z:
   prior='Objekt-X-Zusammengesetzte-Aussenresiduen-und-Momentanschluss-2026-10-11'
   with zipfile.ZipFile(BytesIO(z.read(name+'/inputs/'+prior+'.zip'))) as q:
    gates=json.loads(q.read(prior+'/ATTACHMENT_GATES.json'))['cases']
 dN=F(11,10)+sum((F(1,k) for k in range(1,105)),F(0));rows=[]
 for p,label in enumerate(['EVEN','ODD']):
  r=readzip(args.responses_zip,'RESPONSES_'+label+'.json');case=logaudit['cases'][p]
  K=h.rat(r['K12_new_rational']);rho=F(r['rho']);beta=F(r['beta']);sigma=F(r['sufficient_complete_QR_normalized_budget']);M=h.rat(r['M_upper_rational'])
  D=[[1-rho if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
  T=[[beta*(D[i][j]-M[i][j]) for j in range(203)] for i in range(203)]
  c8=F(1,5000) if p==0 else F(13,20000);clog=F(case['three_log_full_weighted_tail_relative_to_T_upper'])
  assert clog==(F(1,500) if p==0 else F(1,250))
  j=F(gates[p]['basis84_dual_contribution_relative_to_D_upper']);eps=j+F(1,10**300)
  theta=F(427,20) if p==0 else F(74,5)
  factor=theta/(1+theta)*(1-c8-(1+theta)*clog);dfactor=theta/(1+theta)*eps
  allowed=[[dN*(factor*T[i][j]-dfactor*D[i][j]) for j in range(203)] for i in range(203)]
  scalar=floor_grid(dN*(factor*sigma-dfactor));energy=floor_grid(10920*dN*(factor*sigma-dfactor))
  assert scalar>0 and energy>0
  proof=h.ld.positive(h.pts([[allowed[i][j]-scalar*D[i][j] for j in range(203)] for i in range(203)]))
  energyproof=h.ld.positive(h.pts([[10920*allowed[i][j]-energy*D[i][j] for j in range(203)] for i in range(203)]))
  oldenergy=F(case['sufficient_E_g_tail_scalar_relative_to_D']);improvement=energy/oldenergy
  effective=1-c8-eps/sigma
  sl,su=rootiv(effective/clog);ol,ou=rootiv(effective*clog)
  optimal_lo=effective+clog-2*ou;optimal_hi=effective+clog-2*ol
  achieved=factor-dfactor/sigma
  assert achieved<=optimal_hi and optimal_lo-achieved<F(1,10**7)
  # Reject the exact rational matrix at a value above the analytic optimum.
  assert (F(1)+clog)>optimal_hi
  rows.append({'parity':label.lower(),'N':104,'d104':str(dN),'Young_parameter':str(theta),
   'remaining_Ug_target_T_coefficient_before_d104':str(factor),'remaining_Ug_target_D_subtraction_before_d104':str(dfactor),
   'sufficient_global_Ug_upper_relative_to_D':str(scalar),'sufficient_global_Eg_tail_upper_relative_to_D':str(energy),
   'global_integral_budget_positive':proof,'derivative_budget_positive':energyproof,
   'previous_derivative_target':str(oldenergy),'derivative_target_increase_factor':str(improvement),
   'optimal_Young_parameter_enclosure':[str(sl-1),str(su-1)],
   'scalar_normalized_target_optimality_gap_upper':str(optimal_hi-achieved),
   'integral_Ug_computed':False,'derivative_Gram_computed':False,'full_remainder_certified':False})
  print(label,'conditional Ug/D <=',float(scalar),'or Eg_tail/D <=',float(energy),'target increase',float(improvement),flush=True)
 # An exact cumulative function can vanish at every sampled point while
 # its derivative integral is positive and can be scaled arbitrarily.
 coeff=[F(0),F(1,2),F(-3,2),F(1)];der=[(k+1)*coeff[k+1] for k in range(3)]
 assert all(sum(coeff[k]*q**k for k in range(4))==0 for q in [F(0),F(1,2),F(1)])
 hidden=sum(der[i]*der[j]/F(i+j+1) for i in range(3) for j in range(3))
 assert hidden==F(1,20)>0
 result={'status':'PASS_OPTIMIZED_CONDITIONAL_GLOBAL_BUDGETS','cases':rows,'input_SHA256':HASHES,
  'countercontrol_zero_sample_values_positive_global_integral':'1/20',
  'logarithmic_coefficients_already_computed_in_bound_log_package':True,'new_global_residual_integral_computed':False,
  'full_remainder_certified':False,'tail_floor_1_over_20_certified':False}
 args.out.write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':
 ap=argparse.ArgumentParser()
 for key in HASHES:ap.add_argument('--'+key+'-zip',type=Path,required=True)
 ap.add_argument('--out',type=Path,required=True);main(ap.parse_args())
