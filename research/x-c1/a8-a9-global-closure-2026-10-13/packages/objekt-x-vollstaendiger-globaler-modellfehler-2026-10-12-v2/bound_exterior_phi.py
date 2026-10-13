"""Complete shell L2 bound for K Phi AC, including the logarithmic endpoint.

Every interior panel uses a Taylor polynomial and an integral-geometric
remainder for the complete Cauchy transform. No sampling inference.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import sys,json,time,argparse,hashlib
HERE=Path(__file__).resolve().parent; ROOT=Path(sys.argv[sys.argv.index('--root')+1]).resolve() if '--root' in sys.argv else HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/compute-deps'),str(ROOT/'work/galerkin84-2026-10-10'),str(ROOT/'work/tail-probe-2026-10-10/vendor')]
from flint import arb,arb_poly,arb_mat,ctx,fmpq
from safe_serial import serial
def af(v):
 q=F(v);return arb(fmpq(q.numerator,q.denominator))
def norm(mm):return sum((abs(mm[i,j]).upper()**2 for i in range(mm.nrows()) for j in range(mm.ncols())),arb(0)).sqrt()
from compute_source_mixed import legendre
import source_core
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path);ap.add_argument('--parity',choices=['even','odd'],required=True);ap.add_argument('--bits',type=int,default=3072);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--panels',type=int,default=64);args=ap.parse_args()
assert not args.out.exists();ctx.prec=args.bits;start=time.monotonic();p=int(args.parity=='odd')
def say(s):print(time.strftime('%H:%M:%S'),args.parity,s,flush=True)
def read(s):return json.loads(s.read_bytes())
def polys(mm):return [arb_poly([mm[i,j] for i in range(mm.nrows())]) for j in range(mm.ncols())]
def matrix(pp,n):return arb_mat([[f[i] for f in pp] for i in range(n)])
def cnorm(rr):return sum((abs(v).upper()**2 for v in rr),arb(0)).sqrt()
def coeffnorms(pp,n):return [cnorm([f[i] for f in pp]) for i in range(n)]
def mellin(n,t):
 z=t/2;lead=arb(1)
 for k in range(1,n+1):lead*=z/(2*k+1)
 v=term=arb(1)
 for k in range(256):term*=z*z/(2*(k+1)*(2*n+2*k+3));v+=term
 nxt=term*z*z/(2*257*(2*n+515));rr=z*z/(2*258*(2*n+517))
 return lead*(v+arb(0,(nxt/(1-rr)).upper()))
a=3*arb(2).log()/2;b=arb(3).log();h=b-a;vmax=h/a
commonpath=ROOT/'work/direct-rest84-2026-10-11/REFINED_COMMON96.json'
data=read(commonpath)['cases'][p]
AC=arb_mat([[af(F(int(v),int(data['inverse_congruence_denominator']))) for v in rr] for rr in data['inverse_congruence_integer_matrix']])
lp=legendre(384);cn=[arb(2*n+1).sqrt()/arb(2*p+1).sqrt()*mellin(n,a)/mellin(p,a) for n in range(p+2,384,2)]
base=[lp[n]*arb(2*n+1).sqrt()-lp[p]*(cn[j]*arb(2*p+1).sqrt()) for j,n in enumerate(range(p+2,384,2))]
phi=polys(matrix(base,384)*AC)
# Exact full [-1,1] polynomial division of the Cauchy kernel.
quot=[]
for f in phi:
 quot.append(arb_poly([sum((2*f[n]/(n-k) for n in range(k+1,len(f)) if (n-k)%2),arb(0)) for k in range(len(f)-1)]))
gamma,eps=source_core.gamma_polynomial(224);eps=af(eps)
# Positive-core moments; parity is included explicitly in the kernel.
pm=arb_mat([[sum((f[k]/(k+l+1) for k in range(len(f))),arb(0)) for f in phi] for l in range(225)])
gm=arb_mat([[af(gamma[k+l])*comb(k+l,l)*a**(k+l)*(((-1)**l)+((-1)**p))/(2**(k+l)) if k+l<=224 else 0 for l in range(225)] for k in range(225)])
reg=polys(-(2*a).sqrt()/2*gm*pm)
polyterm=reg
for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
 shift=arb(q).log()/a;weight=-arb(prime).log()/arb(q).sqrt()/(2*a).sqrt()
 polyterm=[g+f(arb_poly([-shift,1]))*weight for g,f in zip(polyterm,phi)]
say('complete Cauchy and polynomial exterior model assembled')
# ||Phi AC|| on normalized positive core; Phi*Phi=I+cn cn*.
cnrow=arb_mat([cn])*AC
inputnorm=(norm(AC)**2+norm(cnrow)**2).sqrt()
fac=1/(2*(2*a).sqrt());N=80
rows=[];energy=arb(0)
# The entire endpoint interval, including its infinite logarithmic energy.
q0=F(1,2**20);width=vmax*af(q0);shift=arb_poly([1,width])
ph=[f(shift) for f in phi];qq=[f(shift) for f in quot];bb=[f(shift) for f in polyterm]
logplus=arb_poly([arb(2).log()]+[(-1)**(k+1)*(width/2)**k/k for k in range(1,N)])
analytic=[g+fac*(v+f*width.log()-f*logplus) for f,v,g in zip(ph,qq,bb)]
logcoef=[f*fac for f in ph]
acap=sum(coeffnorms(analytic,max(map(len,analytic))),arb(0))
lcap=sum(coeffnorms(logcoef,384),arb(0))
rem=fac*sum(coeffnorms(ph,384),arb(0))*(width/2)**N/(N*(1-width/2))
endpointcap=(acap+arb(2).sqrt()*lcap+rem)
endpointenergy=2*h*af(q0)*endpointcap**2;energy+=endpointenergy
rows.append({'kind':'whole_logarithmic_endpoint','u_lo':'0','u_hi':str(q0),'scaled_analytic_coefficient_sum':acap,'scaled_log_coefficient_sum':lcap,'analytic_log_remainder':rem,'energy_upper':endpointenergy})
say('full endpoint energy < '+endpointenergy.str(12))
# Dyadic panels followed by a uniform partition; all endpoints are rational.
ends=[q0]
while ends[-1]<F(1,args.panels):ends.append(min(2*ends[-1],F(1,args.panels)))
ends+=list(F(k,args.panels) for k in range(2,args.panels+1))
for ii,(lo,hi) in enumerate(zip(ends[:-1],ends[1:])):
 centre=1+vmax*af((lo+hi)/2);radius=vmax*af((hi-lo)/2);dist=centre-1
 sh=arb_poly([centre,radius]);ph=[f(sh) for f in phi];qq=[f(sh) for f in quot];bb=[f(sh) for f in polyterm]
 logseq=[((centre+1)/(centre-1)).log()]+[af(F((-1)**(k+1),k))*((radius/(centre+1))**k-(radius/(centre-1))**k) for k in range(1,N)]
 logp=arb_poly(logseq)
 total=[]
 for f,v,g in zip(ph,qq,bb):
  product=f*logp
  total.append(arb_poly([g[k]+fac*(v[k]-product[k]) if k<N else g[k] for k in range(max(N,len(g)))]))
 terms=coeffnorms(total,max(map(len,total)))
 tcap=sum(terms,arb(0))
 # Cauchy geometric tail integrated on the full core, for all 191 columns.
 tail=2*fac*inputnorm*(radius/dist)**N/(dist-radius)
 cap=tcap+tail;en=2*h*af(hi-lo)*cap**2;energy+=en
 rows.append({'kind':'interior_taylor_with_complete_integral_remainder','u_lo':str(lo),'u_hi':str(hi),'coefficient_sum':tcap,'complete_cauchy_remainder':tail,'energy_upper':en})
 if ii%8==0:say(f'panel {ii}/{len(ends)-1}, norm cap {cap.str(12)}; cumulative L2 {energy.sqrt().str(12)}')
 # Check coefficients at the exact centre against the original formula.
 direct=[-fac*(f(centre)*logseq[0]-v(centre))+g(centre) for f,v,g in zip(phi,quot,polyterm)]
 assert all((total[j][0]-direct[j]).contains(0) for j in range(191))
modelnorm=energy.sqrt()
# Independent Legendre-Q recurrence for the entire singular cross action.
# These controls test the formula; the proof of the global bound is above.
controls=[]
for u0 in [F(1,1000),F(1,3),F(9,10)]:
 s=1+vmax*af(u0);qqn=[((s+1)/(s-1)).log()/2]
 qqn.append(s*qqn[0]-1)
 for n in range(1,383):qqn.append(((2*n+1)*s*qqn[n]-n*qqn[n-1])/(n+1))
 legrow=arb_mat([[2*(arb(2*n+1).sqrt()*qqn[n]-cn[j]*arb(2*p+1).sqrt()*qqn[p]) for j,n in enumerate(range(p+2,384,2))]])*AC
 closed=arb_mat([[f(s)*((s+1)/(s-1)).log()-v(s) for f,v in zip(phi,quot)]])
 err=norm(closed-legrow);assert err<af('1e-100')
 controls.append({'u':str(u0),'complete_singular_row_difference':err})
# Actual external Gamma kernel differs uniformly by eps; safe complete HS bound.
gammaerror=4*eps*inputnorm
bound=modelnorm+gammaerror
out={'status':'COMPLETE_GLOBAL_EXTERIOR_BOUND','parity':args.parity,'bits':args.bits,'taylor_terms':N,'panels':rows,'normalized_core_input_HS_norm':inputnorm,'full_model_exterior_L2_HS_norm':modelnorm,'full_external_Gamma_error':gammaerror,'actual_K_Phi_AC_L2_HS_norm_upper':bound,'independent_Legendre_Q_controls':controls,'common_sha256':hashlib.sha256(commonpath.read_bytes()).hexdigest(),'seconds':time.monotonic()-start,'global_residual_Gram_certified':False,'full_remainder_certified':False}
args.out.write_text(json.dumps(serial(out,80),indent=2)+'\n');say('DONE complete exterior bound '+bound.str(16))
