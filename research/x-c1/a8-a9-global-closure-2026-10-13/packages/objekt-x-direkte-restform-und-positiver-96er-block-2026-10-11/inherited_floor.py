"""Rational constants for a full old-high Gamma derivative bound."""
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path

def prove():
 r=F(26,25);N=384;eps=F(1,10**6)
 terms=[r**(2*k)/factorial(2*k) for k in range(21)]
 tail=r**42/F(factorial(42))/(1-r*r/F(43*44))
 cosh_upper=sum(terms)+tail;assert cosh_upper<2
 # On 0<z<=r, S=sinh(z)/z satisfies S>=1, S<=cosh(z)<2,
 # cosh(z)-1<=z^2 cosh(r)/2<z^2 and S-1<=z^2 cosh(r)/6<z^2/3.
 # Hence |cosh(z)-S^2|<=2 z^2, and |k_reg'(2z)|<=3/8.
 derivative=F(3,8)
 hs_squared=(2*r*r*derivative)**2*F(2,3)
 gamma_high_squared=hs_squared/F(N*(N+1))
 gamma_high_upper=F(1,500)
 assert gamma_high_squared<gamma_high_upper**2
 def log_upper(n,N=120):
  z=F(n-1,n+1)
  return 2*sum(z**(2*k+1)/F(2*k+1) for k in range(N))+2*z**(2*N+1)/F((2*N+1))/(1-z*z)
 assert F(3,2)*log_upper(2)<r
 assert sum(F(1,k) for k in range(1,385))>F(6529,1000)
 assert log_upper(F(2)*F(22,7)*r)+F(5773,10000)<F(491,200)
 assert 3**2>2**3
 weights={2:F(491,1000),3:F(635,1000),4:F(347,1000),5:F(720,1000),7:F(736,1000)}
 for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:assert log_upper(prime)**2<weights[q]**2*q
 # q=7 only acts for |x|>0.87; q=2 has two directions only for |x|<1/3.
 assert 7**200>2**561
 z=F(7,5)
 exp_upper=sum(z**k/factorial(k) for k in range(31))+z**31/F(factorial(31))/(1-z/32)
 assert exp_upper<F(10000,2431)
 losses=[2*weights[2]+weights[3],sum(weights[q] for q in [2,3,4,5]),sum(weights.values())-F(7,10)]
 prime_potential_loss=F(9,4)
 assert all(x<prime_potential_loss for x in losses)
 raw=F(6529,1000)-F(491,200)-prime_potential_loss-gamma_high_upper
 corrected=raw-16*eps-12*eps**2
 delta=F(91,50)
 assert corrected>delta*(1+eps**2)
 return {'status':'RATIONAL_CONSTANTS_PASS_FOR_COMBINED_HIGH_FLOOR',
  'r':str(r),'cosh_r_upper':str(cosh_upper),'regular_kernel_derivative_upper':str(derivative),
  'weighted_derivative_HS_squared_upper':str(hs_squared),
  'high_Gamma_norm_squared_upper':str(gamma_high_squared),
  'high_Gamma_norm_simple_upper':str(gamma_high_upper),
  'prime_weight_upper':{str(k):str(v) for k,v in weights.items()},
  'potential_threshold_exp_upper':str(exp_upper),'row_loss_upper_bounds':list(map(str,losses)),
  'joint_potential_prime_loss':str(prime_potential_loss),
  'raw_high_floor':str(raw),'moment_corrected_floor_over_raw_norm':str(corrected),
  'physical_high_floor':str(delta),'previous_physical_high_floor':'2/3',
  'scope':'Full high space, conditional on inherited old form decomposition and scalar q0/prime/moment bounds; analytic derivative/Legendre argument in accompanying proof.'}

if __name__=='__main__':
 assert __debug__
 data=prove();p=Path(__file__).resolve().parent/'FLOOR_CHECK.json'
 p.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
