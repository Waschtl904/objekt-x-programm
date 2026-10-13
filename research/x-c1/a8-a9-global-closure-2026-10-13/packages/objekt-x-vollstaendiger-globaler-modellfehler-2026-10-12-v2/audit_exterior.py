"""Independent rational assembly over the WHOLE shell, including u=0.

Stored directed coefficient sums are inputs; the geometric Cauchy remainder,
coverage, energy sum, Gamma error and norm are recomputed independently.
"""
from pathlib import Path
from fractions import Fraction as F
import json,sys,argparse
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE));sys.path.insert(1,str(HERE.parents[1]/'work/global-model-2026-10-12'))
import interval_helpers as h
def read(p):return json.loads(p.read_bytes())
def up(x):
 assert isinstance(x,list) and len(x)==2
 a,b=map(F,x);assert a<=b
 return b
def ceilgrid(v):
 scale=10**80
 return F((v.numerator*scale+v.denominator-1)//v.denominator,scale)
def audit(d):
 assert d['status']=='COMPLETE_GLOBAL_EXTERIOR_BOUND';N=d['taylor_terms'];assert N>=64
 inp=up(d['normalized_core_input_HS_norm']);en=F(0);last=F(0);count=0
 for i,row in enumerate(d['panels']):
  lo,hi=F(row['u_lo']),F(row['u_hi']);assert lo==last and lo<hi<=1
  if i==0:
   assert lo==0 and row['kind']=='whole_logarithmic_endpoint'
   cap=up(row['scaled_analytic_coefficient_sum'])+h.sqrtup(F(2))*up(row['scaled_log_coefficient_sum'])+up(row['analytic_log_remainder'])
  else:
   assert lo>0 and row['kind']=='interior_taylor_with_complete_integral_remainder'
   ratio=(hi-lo)/(hi+lo);assert 0<ratio<1
   # a<21/20, h>1/20 => sqrt(a/2)/h<15.
   rem=15*inp/lo*ratio**N
   cap=up(row['coefficient_sum'])+rem
  assert cap>=0
  cap=ceilgrid(cap)
  # 2h<3/25, deliberately independent of the stored Arb energy values.
  en+=F(3,25)*(hi-lo)*cap*cap
  count+=1;last=hi
 assert last==1
 gamma=4*F(1,10**34)*inp
 bound=h.sqrtup(en)+gamma
 assert bound<1000
 return {'complete_panels':count,'independent_rational_energy_upper':str(en),'complete_exterior_HS_norm_upper':str(bound),'simple_exterior_HS_norm_cap':'1000'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 d=read(a.input);out=audit(d)
 import copy
 bad=copy.deepcopy(d);bad['panels']=bad['panels'][1:]
 try:audit(bad)
 except AssertionError:out['missing_endpoint_rejected']=True
 else:raise AssertionError('omitted endpoint not rejected')
 bad=copy.deepcopy(d);bad['panels'].pop(len(bad['panels'])//2)
 try:audit(bad)
 except AssertionError:out['missing_interior_interval_rejected']=True
 else:raise AssertionError('missing interval not rejected')
 out.update(status='PASS_COMPLETE_GLOBAL_EXTERIOR_BOUND',parity=d['parity'])
 a.out.write_text(json.dumps(out,indent=2)+'\n');print(d['parity'],float(F(out['complete_exterior_HS_norm_upper'])),flush=True)
if __name__=='__main__':main()
