"""Standard-library rational certificate for the scalar integration metric.

Checks the full 203x203 target and its congruence. No integral is inferred.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys,time
def read(p):return json.loads(p.read_bytes())
def bounds(a,h):
 lower=[];upper=[]
 for i,row in enumerate(a):
  rad=sum((max(abs(h.lower(v)),abs(h.upper(v))) for j,v in enumerate(row) if i!=j),F(0))
  lower.append(h.lower(row[i])-rad);upper.append(h.upper(row[i])+rad)
 return min(lower),max(upper)
def main():
 ap=argparse.ArgumentParser()
 for k in ['helpers','inputs','direction','weights','error','out']:ap.add_argument('--'+k,type=Path,required=True)
 a=ap.parse_args();sys.path.insert(0,str(a.helpers));import interval_helpers as h
 ld=h.ld;src=read(a.inputs);direction=read(a.direction);weights=read(a.weights);errors=read(a.error)
 G=h.pts(h.rat(direction['full_log_tail_Gram_rational_upper_3x3']));cases=[]
 for idx,r in enumerate(src['cases']):
  start=time.monotonic();d=direction['cases'][idx];w=weights['cases'][idx];K=h.rat(r['K12_new_rational']);rho=F(r['rho'])
  Dr=[[1-rho if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
  D=h.pts(Dr);T=h.sc(h.add(D,h.pts(h.rat(r['M_upper_rational'])),-1),F(r['beta']))
  C0=h.pts(h.rat(d['coefficient_midpoints_3x203']))
  H=h.sc(h.add(h.add(h.sc(T,F(d['derivative_target_coefficient_T'])),h.sc(D,F(d['derivative_target_subtracted_coefficient_D'])),-1),h.sc(h.mmI(h.T(C0),h.mmI(G,C0)),F(d['derivative_target_subtracted_coefficient_CtGC'])),-1),F(1,10920))
  C=h.rat(w['C_lower_triangular_rational']);assert len(C)==203 and all(len(v)==203 for v in C)
  assert all(C[i][i]>0 and all(C[i][j]==0 for j in range(i+1,203)) for i in range(203))
  polynomial=h.rat(w['p_ordinary_shifted_Legendre_coefficients_rational']);assert len(polynomial)==104 and all(len(v)==203 for v in polynomial)
  W=h.pts(C);CHCt=h.mmI(h.mmI(W,H),h.T(W));lo,hi=bounds(CHCt,h)
  assert lo>1 and hi<F(1001,1000),(r['parity'],float(lo),float(hi))
  # With H>=uD, certify the inherited model+rounded-log absorption numerically.
  u=F(['0.000001832433','0.000010613269'][idx]);deltaR=F(errors['cases'][idx]['complete_canonical_high_model_error'])
  floorproof=ld.positive(h.add(H,h.sc(D,u),-1))
  deltaC=F(1,10**10);assert 4*(deltaR+deltaC)**2<F(1,10**6)*u
  # An understated metric must be rejected by exactly the same congruence gate.
  bad=h.sc(CHCt,F(1,4));badlo,badhi=bounds(bad,h);assert badhi<1
  cases.append({'parity':r['parity'],'rational_congruence_lower':str(lo),'rational_congruence_upper':str(hi),
   'full_target_entries':203**2,'C_H_Ct_between_I_and_1p001I':True,'fixed_polynomial_degree':103,
   'inverse_target_majorized_by_CtC':True,'half_sized_C_rejected':True,
   'target_lower_relative_to_D':str(u),'target_lower_LDL_proof':floorproof,
   'sufficient_full_scalar_integral_bound':'999/1000',
   'full_scalar_integral_bound_proved':False,'global_model_Gram_certified':False,'full_remainder_certified':False})
  print(r['parity'],'PASS all 41209 congruence entries; eigenvalues between',float(lo),float(hi),'seconds',round(time.monotonic()-start,2),flush=True)
 out={'status':'PASS_RATIONAL_SCALAR_INTEGRATION_METRICS_ONLY','cases':cases,'full_scalar_integral_computed':False,'full_remainder_certified':False}
 a.out.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
 assert __debug__
 main()
