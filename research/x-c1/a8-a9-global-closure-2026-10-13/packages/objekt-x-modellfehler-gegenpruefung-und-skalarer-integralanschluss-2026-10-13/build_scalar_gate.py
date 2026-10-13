"""Build rational proposals for a scalar sufficient global Gram test.

No integration or global remainder certificate is produced here.
The floating/Arb construction is separately checked by audit_scalar_gate.py.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys,time
from flint import arb,arb_mat,ctx,fmpq
ctx.prec=768
def read(p):return json.loads(p.read_bytes())
def af(v):
 q=F(v);return arb(fmpq(q.numerator,q.denominator))
def mat(v):return arb_mat([[af(x) for x in r] for r in v])
def fix(v):
 q=F(v.mid().str(120,radius=False));scale=10**60
 return str(F((q*scale).numerator//(q*scale).denominator,scale))
def freeze(m):return [[fix(m[i,j]) for j in range(m.ncols())] for i in range(m.nrows())]
def chol(m):
 n=m.nrows();l=[[arb(0) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for j in range(i+1):
   z=m[i,j]-sum((l[i][k]*l[j][k] for k in range(j)),arb(0))
   l[i][j]=z.sqrt() if i==j else z/l[j][j]
 return arb_mat(l)
def main():
 ap=argparse.ArgumentParser()
 for k in ['inputs','direction','polynomials','out']:ap.add_argument('--'+k,type=Path,required=True)
 a=ap.parse_args();src=read(a.inputs);direction=read(a.direction);pol=read(a.polynomials)
 G=mat(direction['full_log_tail_Gram_rational_upper_3x3']);cases=[]
 aa=3*arb(2).log()/2;bb=arb(3).log();hh=bb-aa
 for idx,r in enumerate(src['cases']):
  start=time.monotonic();d=direction['cases'][idx];K=mat(r['K12_new_rational']);rho=af(r['rho'])
  D=arb_mat([[1-rho if i==j and i<191 else K[i-191,j-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
  T=af(r['beta'])*(D-mat(r['M_upper_rational']));C0=mat(d['coefficient_midpoints_3x203'])
  H=(af(d['derivative_target_coefficient_T'])*T-af(d['derivative_target_subtracted_coefficient_D'])*D-af(d['derivative_target_subtracted_coefficient_CtGC'])*C0.transpose()*G*C0)/10920
  C=chol(H).inv()*af(F(10001,10000))
  cr=[[fix(C[i,j]) if j<=i else '0' for j in range(203)] for i in range(203)]
  cf=mat(cr);check=cf*H*cf.transpose()
  for i in range(203):
   radius=sum((abs(check[i,j]).upper() for j in range(203) if j!=i),arb(0))
   assert check[i,i]-radius>1 and check[i,i]+radius<af(F(1001,1000))
  # Convert the old fixed proposal to physical ordinary Legendre coefficients.
  # W^{-1}=diag(sqrt(1-rho) I, L12^T), where D=L_D L_D^T.
  coeff=mat(pol['cases'][idx]['whitened_normalized_Legendre_coefficients'])
  LK=chol(K);last=arb_mat([[coeff[i,j] for j in range(191,203)] for i in range(104)])*LK.transpose()
  physical=arb_mat([[ (coeff[i,j]*(1-rho).sqrt() if j<191 else last[i,j-191])*(arb(2*i+1)/(2*hh)).sqrt() for j in range(203)] for i in range(104)])
  pr=freeze(physical)
  cases.append({'parity':r['parity'],'C_lower_triangular_rational':cr,'p_ordinary_shifted_Legendre_coefficients_rational':pr,
   'p_definition':'p(a+h*u)=sum(n=0..103) P_n(2*u-1) p_n, in physical force coordinates',
   'C_definition':'I < C H C^T < (1001/1000) I; H=E_dir/10920',
   'sufficient_scalar_integral_upper':'999/1000','global_scalar_integral_certified':False})
  print(r['parity'],'built rational scalar metric and fixed polynomial',round(time.monotonic()-start,2),'seconds',flush=True)
 a.out.write_text(json.dumps({'status':'RATIONAL_PROPOSALS_REQUIRE_SEPARATE_AUDIT','cases':cases,
  'scalar_integral_definition':'2*h integral_0^1 ||(Rhat0(a+h*u)-B(u) C0-p(a+h*u)) C^T||_2^2 du',
  'full_remainder_certified':False},indent=2)+'\n')
if __name__=='__main__':main()
