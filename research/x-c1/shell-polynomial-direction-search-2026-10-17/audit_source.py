"""Independent numerical quadrature check of the polynomial Gamma convolution.

This audit is not used as an error bound by the directed certifier.
"""
import os,json,hashlib
from pathlib import Path
from fractions import Fraction
import mpmath as mp
from flint import arb,arb_poly,arb_series,ctx
HERE=Path(__file__).resolve().parent
DATA=Path(os.environ.get('OBJEKT_X_SEARCH_OUTPUT',str(HERE/'data')))
ctx.prec=600;ctx.cap=362;mp.mp.dps=100
def q(v):
 f=Fraction(v);return arb(f.numerator)/f.denominator
def mf(x):
 f=Fraction(str(x.mid().fmpq()));return mp.mpf(f.numerator)/f.denominator
def audit(par):
 d=json.loads((DATA/f'FROZEN_{par}.json').read_text());eps=1 if par=='even' else -1
 a=arb(3).log();b=arb(11).log()/2;h=b-a
 p=[arb_poly([1]),arb_poly([0,1])]
 for j in range(1,11):p.append(((2*j+1)*arb_poly([0,1])*p[j]-j*p[j-1])*(arb(1)/(j+1)))
 raw=list(map(q,d['raw_exact_rational_coefficients']))
 S=sum((raw[j]*(arb(2*j+1)/(2*h)).sqrt()*p[j](arb_poly([-1-2*a/h,2/h])) for j in range(12)),arb_poly([]))
 nodes=[arb.legendre_p_root(64,k,weight=True) for k in range(64)]
 m=lambda x:(x/2).cosh() if par=='even' else (x/2).sinh()
 lam=sum((h*w/2*S((a+b)/2+h*z/2)*m((a+b)/2+h*z/2) for z,w in nodes),arb(0));mu=(eps*a+a.sinh())/2
 S*=1/(sum((r*r for r in raw),arb(0))+2*lam*lam/mu).sqrt()
 degree=360;fac=[arb.fac_ui(j) for j in range(degree+14)]
 reg=arb_series([1/(2**j*fac[j])for j in range(degree+2)],prec=degree+2)/arb_series([1/fac[j+1] if j%2==0 else arb(0)for j in range(degree+2)],prec=degree+2)/2
 assert reg.prec==362
 moments=[(b**(j+1)-a**(j+1))/(j+1) for j in range(degree+12)]
 sm=[sum((c*moments[j+k]for k,c in enumerate(S)),arb(0)) for j in range(degree+1)]
 conv=arb_poly([reg[j+1]*fac[j]for j in range(degree,-1,-1)])*arb_poly([v/fac[j] for j,v in enumerate(sm)])
 gam=arb_poly([conv[degree-k]/fac[k]*((-1)**k+eps)for k in range(degree+1)])
 Q=arb_poly([sum((S[j]*moments[j-k-1]for j in range(k+1,len(S))),arb(0))for k in range(len(S)-1)])
 aa=mp.log(3);bb=mp.log(11)/2;coeff=list(map(mf,S));rows=[]
 fun=lambda x:mp.polyval(coeff[::-1],x)
 kernel=lambda r:mp.exp(-r/2)/(1-mp.exp(-2*r))
 for factor in ('1/7','1/2','6/7'):
  x=a*q(factor);xx=aa*mf(q(factor))
  analytic=(S(x)*((b-x)/(a-x)).log()+Q(x)+eps*(S(-x)*((b+x)/(a+x)).log()+Q(-x)))/2+gam(x)
  direct=mp.quad(lambda y:fun(y)*(kernel(y-xx)+eps*kernel(y+xx)),[aa,bb])
  difference=abs(mf(analytic)-direct);assert difference<mp.mpf('1e-38')
  rows.append({'x_over_a':factor,'analytic_midpoint':mp.nstr(mf(analytic),70),'independent_mpmath_quad':mp.nstr(direct,70),'absolute_difference':mp.nstr(difference,12)})
 return {'candidate_sha256':hashlib.sha256((DATA/f'FROZEN_{par}.json').read_bytes()).hexdigest(),'checks':rows}
if __name__=='__main__':
 out={'status':'NUMERICAL_AUDIT_ONLY_NOT_A_DIRECTED_BOUND','mpmath_dps':100,'parities':{p:audit(p)for p in ('even','odd')}}
 (DATA/'SOURCE_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
 print('PASS: six independent Gamma integral point checks')
