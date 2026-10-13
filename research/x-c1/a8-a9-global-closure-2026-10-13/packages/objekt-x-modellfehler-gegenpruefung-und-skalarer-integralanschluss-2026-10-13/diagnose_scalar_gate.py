"""Reuse earlier point samples to diagnose the NEW fixed scalar objective.

No new function integration, quadrature remainder, or global upper bound.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
import numpy as np
from flint import arb,arb_mat,ctx,fmpq
ctx.prec=768
def af(x):
 q=F(x);return arb(fmpq(q.numerator,q.denominator))
def mat(a):return arb_mat([[af(x) for x in r] for r in a])
def floating(a):return np.array([[float(a[i,j].mid()) for j in range(a.ncols())] for i in range(a.nrows())])
def main():
 ap=argparse.ArgumentParser()
 for k in ['inputs','weights','samples','out']:ap.add_argument('--'+k,type=Path,required=True)
 a=ap.parse_args();src=json.loads(a.inputs.read_bytes());weights=json.loads(a.weights.read_bytes());cases=[]
 hh=arb(3).log()-3*arb(2).log()/2
 for idx,r in enumerate(src['cases']):
  p=r['parity'];C=mat(weights['cases'][idx]['C_lower_triangular_rational']);P=mat(weights['cases'][idx]['p_ordinary_shifted_Legendre_coefficients_rational'])
  K=mat(r['K12_new_rational']);rho=af(r['rho']);ll=[[arb(0) for _ in range(12)] for _ in range(12)]
  for i in range(12):
   for j in range(i+1):
    v=K[i,j]-sum((ll[i][k]*ll[j][k] for k in range(j)),arb(0));ll[i][j]=v.sqrt() if i==j else v/ll[j][j]
  L=arb_mat(ll);Winv=arb_mat([[(1-rho).sqrt() if i==j and i<191 else L[j-191,i-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
  transform=floating(Winv*C.transpose());poly=floating(P*C.transpose()*(2*hh).sqrt())
  values=[]
  for n in [128,256]:
   samples=np.load(a.samples/f'EXPLORATORY_{p.upper()}_{n}.npz');u=samples['nodes'];v=samples['values'];wg=samples['weights']
   basis=np.polynomial.legendre.legvander(2*u-1,103)
   residual=v@transform-basis@poly
   estimate=float(np.sum(wg[:,None]*residual**2))
   values.append({'old_quadrature_order':n,'fixed_new_scalar_integral_estimate':estimate,'certified_upper_bound':False})
  cases.append({'parity':p,'diagnostics':values,'same_fixed_polynomial_in_both_orders':True})
 out={'status':'EXPLORATORY_REUSE_OF_PREVIOUS_POINT_SAMPLES_ONLY','cases':cases,'new_function_points_computed':0,'quadrature_error_bounded':False,'global_scalar_integral_certified':False,'full_remainder_certified':False}
 a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
