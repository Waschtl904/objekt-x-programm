"""Rational replay of the global reduction scalars and new 9D certificates.

Full function integration is a separate optional workflow described in README.
This replay verifies stored integration enclosures, not their analytic premises.
"""
from pathlib import Path
from fractions import Fraction as F
from math import prod,isqrt
import json,hashlib,sys
import rational_interval_ldl as ld
HERE=Path(__file__).resolve().parent
def read(name):return json.loads((HERE/name).read_bytes())
def upper(v):return F(v[1])
def lower(v):return F(v[0])
def sqrt_up(x):
 x=F(x);assert x>=0;scale=10**100
 n=isqrt(x.numerator*scale*scale//x.denominator)
 while F(n*n,scale*scale)<x:n+=1
 return F(n,scale)
def audit():
 assert sys.flags.optimize==0,'Run without -O'
 manifest=read('MANIFEST.json')
 for name,digest in manifest['files'].items():
  path=(HERE/name).resolve();assert path.is_relative_to(HERE)
  assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,name
 a=read('data/INFINITE_REDUCTION.json')
 ds=[sum((F(1,k) for k in range(1,n+1)),F(11,10)) for n in range(97)]
 assert ds[95]==F(a['local_L_weight_95'])<7 and ds[96]==F(a['local_L_weight_96'])>6
 tail=F(3*193,8*64**192*prod(range(1,194,2))**2)
 assert tail==F(a['moment_tail_squared_rational_upper'])<F(1,10**704)
 t=F(1,10**352)
 price=(40*t+400*t*t)/6+1000*t*t*(1+20*t)**2/36
 assert price==F(a['projection_correction_per_full_residual_norm_squared'])<F(1,10**350)
 assert price*10**100<F(1,10**250)
 # Explicit conservative bookkeeping for the conditional X-residual norm.
 Ubound=2000**2+10**30*(3*10**8)**2
 assert Ubound<10**48
 Alow=2*10**30*(3*10**8)**2
 Across=2*10**24+2*10**20*10**48
 Aweighted=Alow+Across*10**26
 assert Aweighted<10**95
 assert 2*Aweighted+8*10**90<10**100
 cases=[]
 fields=['Hgram','source_c_model','source_Bh_model','source_high_cross_model','direct_F_cross_model','direct_probe_model','exact_local_coefficient_intervals']
 for p,label in enumerate(['EVEN','ODD']):
  c=a['cases'][p]
  mu=lower(c['mu']);nu=upper(c['nu'])
  assert mu>F(9,100) and nu<F(1,10)
  cb=(2/mu)**2*ds[95]*nu/2
  assert cb<1000 and cb/ds[0]<400
  assert lower(c['c'])>0 and upper(c['c'])<1000 and upper(c['v_X_norm_squared'])<400
  assert len(c['L_orthogonality_enclosures'])==84
  assert all(lower(row[0])<=0<=upper(row[0]) for row in c['L_orthogonality_enclosures'])
  s=c['source_bound_checks']
  for key,cap in [('inverse_trace',10**30),('HB_trace',10**10),('Kold_inverse_trace',10**20),('rho',F(1,2)),('finite_U_trace_upper',10**20),('g_X_operator_bound',1000),('old_low_moment_gram_bound',2),('high_J84_model_trace',1000)]:
   assert upper(s[key])<cap,(label,key)
  lo=read(f'data/PROBE_{label}_3072.json');hi=read(f'data/PROBE_{label}_4096.json')
  overlaps=0
  for key in fields:
   assert len(lo[key])==len(hi[key])
   for row,row2 in zip(lo[key],hi[key]):
    assert len(row)==len(row2)
    for x,y in zip(row,row2):
     assert max(lower(x),lower(y))<=min(upper(x),upper(y)),(label,key,overlaps)
     overlaps+=1
  assert overlaps==4752
  r=read(f'data/RESULT_{label}_3072.json')
  trace=upper(r['restricted9_model_energy_trace']);err=upper(r['restricted9_feature_error_trace'])
  charge=2*sqrt_up(trace*err)+err
  fsum=sum(abs(F(v)) for v in r['fixed_F_coefficients'])
  direct=F(1,10**20)*(2*fsum*9+9)
  reserve=F(r['restricted9_reserve'])
  matrix=[[ld.interval(v) for v in row] for row in r['restricted9_lower_model']]
  for i in range(9):matrix[i][i]=ld.sub(matrix[i][i],ld.point(charge+direct+reserve))
  pivots=ld.positive(matrix)
  assert r['restricted9_positive'] is True and reserve>0
  cases.append({'parity':label.lower(),'precision_interval_comparisons':overlaps,'restricted9_reserve':str(reserve),'rational_LDL':pivots})
  print(label,'PASS',overlaps,'interval comparisons; 9 positive rational pivots; reserve',reserve,flush=True)
 result={'status':'PASS_GLOBAL_GEOMETRY_REDUCTION_AND_RESTRICTED9','files_bound':len(manifest['files']),
  'moment_tail_squared_upper':'1e-704','conditional_geometry_price':'1e-250 D203_new',
  'new_answer_admissibility_conditions_checked':False,'cases':cases,
  'full_residual_tail_computed':False,'tail_coercivity_certified':False,'full_remainder_certified':False}
 print(json.dumps(result,indent=2))
 return result
if __name__=='__main__':audit()
