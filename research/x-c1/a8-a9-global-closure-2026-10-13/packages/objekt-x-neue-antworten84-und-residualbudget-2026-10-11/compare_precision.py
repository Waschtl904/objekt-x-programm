"""Check two directed builds; agreement is not an analytic remainder proof."""
from pathlib import Path
from fractions import Fraction as F
import json
HERE=Path(__file__).resolve().parent
max_m_upper_difference=F(0)
def is_rat(s):
 if not isinstance(s,str):return False
 try:F(s);return True
 except (ValueError,ZeroDivisionError):return False
def compare(a,b,path=''):
 global max_m_upper_difference
 if path=='/bits':return 0
 if path.startswith('/M_upper_rational/') and isinstance(a,str):
  difference=abs(F(a)-F(b));assert difference<F(1,10**60),path
  max_m_upper_difference=max(max_m_upper_difference,difference)
  return 0
 if path in ['/finite_Galerkin_residual_model_Frobenius','/M_upper_rounding_relative_to_D203']:
  # These are upper-bound constructions from directed endpoints, so their
  # centres need not be the same mathematical number at different precision.
  cap=F(1,10**50) if 'Galerkin' in path else F(1,10**30)
  assert all(F(0)<=F(v)<cap for v in a+b),path
  return 0
 if isinstance(a,dict):
  assert a.keys()==b.keys(),path
  return sum(compare(a[k],b[k],path+'/'+k) for k in a)
 if isinstance(a,list):
  assert len(a)==len(b),path
  if len(a)==2 and all(is_rat(v) for v in a+b):
   assert max(F(a[0]),F(b[0]))<=min(F(a[1]),F(b[1])),path
   return 1
  return sum(compare(x,y,path+'/'+str(i)) for i,(x,y) in enumerate(zip(a,b)))
 assert a==b,(path,a,b)
 return 0
rows=[]
for label in ['EVEN','ODD']:
 a=json.loads((HERE/f'RESPONSES_{label}.json').read_bytes());b=json.loads((HERE/f'RESPONSES_{label}_1024.json').read_bytes())
 max_m_upper_difference=F(0)
 rows.append({'parity':label.lower(),'interval_comparisons':compare(a,b),
 'K_X_metrics_and_scalar_budgets_identical':True,'M_upper_max_entry_difference':str(max_m_upper_difference),
 'other_non_interval_data_identical':True})
out={'status':'PASS_768_AND_1024_BIT_RESPONSE_BUILDS','cases':rows,
 'directed_bound_constructions_compared_by_common_caps':['finite model residual <1e-50','M-upper rounding price <1e-30'],
 'analytic_remainders_not_inferred_from_precision_agreement':True}
(HERE/'PRECISION_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
