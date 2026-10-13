"""Complete old force centres on the fixed eight half-inverse polynomials.

This is a centre computation, not a bound on the half-inverse error Delta.
Logarithmic kernels and their complete high-mode moments are integrated
analytically. All numbers are directed Arb enclosures.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, comb
import argparse, sys, json, gzip, hashlib, time

HERE=Path(__file__).resolve().parent
ROOT=Path(sys.argv[sys.argv.index('--root')+1]).resolve() if '--root' in sys.argv else HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/compute-deps'),str(ROOT/'work/galerkin84-2026-10-10'), str(ROOT/'work/tail-probe-2026-10-10/vendor'),str(ROOT/'work/tail-probe-2026-10-10'),
             str(ROOT/'work/remainder-integration-check-v2/originals/eight-source/code'),
             str(ROOT/'work/inverse-energy-repo-replay/original/vendor')]
from flint import arb, arb_poly, arb_mat, ctx
from compute_inverse_energy_gate import af, box, serial, loewner_bounds, ldl
from compute_source_mixed import legendre
from eight_source_refined import kernel
from log_integrals import Moments, function_moments, function_product, add_function
from prime_geometry import core_partition
from bounded_moments import Moments
import gc
from safe_serial import serial
import source_core as sc

ap=argparse.ArgumentParser()
ap.add_argument('--root',type=Path)
ap.add_argument('--bits',type=int,required=True)
ap.add_argument('--out',type=Path,required=True)
ap.add_argument('--parity',choices=['even','odd'],required=True)
ap.add_argument('--degree',type=int,default=12)
ap.add_argument('--calibration',action='store_true')
args=ap.parse_args()
assert not args.out.exists()
ctx.prec=args.bits
start=time.monotonic()
NJ=84
NC=92
def say(x):print(time.strftime('%H:%M:%S')+' '+args.parity+': '+x,flush=True)
def read(p):
    raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def sym(x):return (x+x.transpose())/2
def mat(x):return arb_mat([[box(v) for v in r] for r in x])
def ratmat(x):return arb_mat([[af(v) for v in r] for r in x])
def upper(x):return loewner_bounds(sym(x))[1]
def trace(x):return sum((x[i,i] for i in range(x.nrows())),arb(0))
def norm_bound(x):
    return sum((abs(x[i,j]).upper()**2 for i in range(x.nrows())
                for j in range(x.ncols())),arb(0)).sqrt()
def pint(poly,l=arb(0),h=arb(1)):
    pp=poly.integral()
    return pp(h)-pp(l)
def pair(poly,mom):return sum((poly[k]*mom[k] for k in range(len(poly))),arb(0))
def coeffs(pol):return [pol[k] for k in range(len(pol))]
def mirror(pol):return arb_poly([(-1)**k*pol[k] for k in range(len(pol))])
def multiply_fun(f,s):return {r:p*s for r,p in f.items()}
def fname(tag):return HERE/tag

INHERITED=ROOT/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09'
base=INHERITED/'work/remainder-integration-check-v2/originals'
paths={'half':base/'half-inverse/expected/1536.json',
       'old':base/'weighted-response/inputs/a8_model.json.gz',
       'eight':base/'eight-source/expected/4096/RESULT.json',
       'basis':ROOT/f'work/basis-coverage-2026-10-10/BASIS_{args.parity.upper()}.json',
       'centres':INHERITED/f'work/u00-2026-10-07/CENTRES_{args.parity.upper()}_4096.json',
       'frozen_J':ROOT/f'work/galerkin84-2026-10-10/MODEL_RAY_{args.parity.upper()}_3072.json',
       'inverse':INHERITED/f'work/gamma-low-2026-10-09/CERTIFICATE_{args.parity.upper()}_gamma224_tight_4096.json'}
bindings={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in paths.items()}
data={k:read(p) for k,p in paths.items()}
p=0 if args.parity=='even' else 1
half=data['half']['blocks'][p]
old=data['old'];eight=data['eight']['blocks'][p]
assert old and half['P_R_lower_integer']>=20
a=3*arb(2).log()/2;b=arb(3).log();h=b-a;c=(a+b)/2;d=h/2;r=b/a
mu=(a.sinh()+(a if p==0 else -a))/2
pol=legendre(544)
cn=[]
def mellin(n,t):
    z=t/2;lead=arb(1)
    for k in range(1,n+1):lead*=z/(2*k+1)
    val=term=arb(1)
    for k in range(256):
        term*=z*z/(2*(k+1)*(2*n+2*k+3));val+=term
    nxt=term*z*z/(2*257*(2*n+515))
    ratio=z*z/(2*258*(2*n+517))
    return lead*(val+arb(0,(nxt/(1-ratio)).upper()))
for n in range(p+2,384,2):
    cn.append(arb(2*n+1).sqrt()/arb(2*p+1).sqrt()*mellin(n,a)/mellin(p,a))
phi=[pol[n]*arb(2*n+1).sqrt()-pol[p]*(cn[k]*arb(2*p+1).sqrt())
     for k,n in enumerate(range(p+2,384,2))]
say('recomputed old moment-kernel basis')

# Replace the stored interval coordinates only in the working centre model.
# The bound on this change is recorded in the orthonormal local basis, before
# converting polynomials to monomials. It is not amplified by monomial norms.
Q=mat(half['basis_Q_local_coefficients'])
S=ratmat(half['half_inverse_centre_rational_Q_coefficients'])
Yfull=Q*S
J=arb_mat([[box(row[j]) for j in range(4)] for row in half['basis_Z_local_coefficients']])
lam_local=arb_mat([[(h*(2*n+1)/2).sqrt()*((c/2).cosh() if (n+p)%2==0 else (c/2).sinh())*mellin(n,h/2) for n in range(96)]])
assert args.bits>=3072 and not args.calibration
D=ratmat(data['basis']['D_rational'])
Z=arb_mat([[D[i,j] if i<8 else int(i-8==j) for j in range(NJ)] for i in range(92)])
YL=Q*Z
assert norm_bound(S.transpose()*Z)<af('1e-800')
Rmid=ratmat(data['frozen_J']['working_basis_midpoints_rational'])
rounding=norm_bound(YL-Rmid)
savedY=ratmat(data['centres']['Y_local_rational_midpoints'])
Yrounding=norm_bound(Yfull-savedY)
assert rounding<af('1e-60') and Yrounding<af('1e-60')
Ymid=arb_mat([[Rmid[i,j] if j<NJ else savedY[i,j-NJ] for j in range(NC)] for i in range(96)])
definition='J=Q[D;I84], D=-(S_top^T)^-1 S_bottom^T; plus eight fixed source models for calibration'
actual_coefficients=serial(YL,70)
Ylocal=[];Ycore=[];Yphysical=[]
for j in range(NC):
    f=sum((pol[k]*(Ymid[k,j]*((2*k+1)/(2*h)).sqrt())
           for k in range(96)),arb_poly([]))
    Ylocal.append(f)
    Yphysical.append(f(arb_poly([-c/d,1/d])))
    Ycore.append(f(arb_poly([-c/d,a/d])))
Ynorm=norm_bound(Ymid)
assert Ynorm<12 and rounding<af('1e-50')
shell_m=arb_poly([(d/2)**k/factorial(k)*
                  ((c/2).cosh() if (k+p)%2==0 else (c/2).sinh())
                 for k in range(161)])
lam=[d*pint(f*shell_m,arb(-1),arb(1)) for f in Ylocal]
shell_m_tail=(c/2).exp()*(d/2)**161/factorial(161)/(1-d/(2*162))
lam_error=(h/2).sqrt()*Ynorm*shell_m_tail
assert lam_error<af('1e-300')
say('fixed centres reconstructed; local-coordinate rounding bounded')

gamma,epsGamma=sc.gamma_polynomial(224)
epsGamma=af(epsGamma)
gammaOld=list(map(F,old['Gamma_polynomial_coefficients']))
# Positive-core cells include every new shell-shift and old/core-shift break.
roots,cells,cut_vectors=core_partition(a,b)
mom=Moments(roots,1100)
say(f'complete core partition: {len(cells)} cells')

# Q_a^np m_core, as polynomial + exact logarithm + prime shifts.
# m is approximated by its degree-160 Taylor polynomial. The uniform error,
# derivative error and resulting complete operator error are charged below.
mcore=arb_poly([(a/2)**k/factorial(k) if k%2==p else arb(0)
                for k in range(161)])
mls=[arb(0)]*161;mdh=arb_poly([])
Hn=arb(0)
for n in range(161):
    if n:Hn+=arb(1)/n
    if n%2==p:
        mls[n]=(2*n+1)*pint(mcore*pol[n])
        mdh+=pol[n]*(mls[n]*Hn)
qma=mdh+mcore*(-(2*arb.pi()*a).log()-arb.const_euler())-kernel(mcore,mls,a,gamma,p)
qm={None:qma,'one':mcore*(-af('0.5')),'minus_one':mcore*(-af('0.5'))}
qmshift=[]
for lo,hi in cells:
    mid=(roots[lo]+roots[hi])/2;shift=arb_poly([])
    for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
        shiftby=arb(q).log()/a;w=arb(prime).log()/arb(q).sqrt()
        for sign in [-1,1]:
            if abs(mid+sign*shiftby)<1:
                shift-=mcore(arb_poly([sign*shiftby,1]))*w
    qmshift.append(shift)

# Singular Carleman action and complete regular Gamma action on the shell.
globalF=[];cellF=[]
for j,f in enumerate(Yphysical):
    if j%8==0:say(f'forming full core sources {j}/{NC}')
    div=arb_poly([])
    for k in range(1,len(f)):
        div+=arb_poly([f[k]*(b**(k-l)-a**(k-l))/(k-l) for l in range(k)])
    divcore=div(arb_poly([0,a]))
    sing={None:(divcore+mirror(divcore)*((-1)**p))*(-af('0.5')),
          'outer':Ycore[j]*(-af('0.5')),'one':Ycore[j]*af('0.5'),
          'minus_outer':mirror(Ycore[j])*(-af('0.5')*((-1)**p)),
          'minus_one':mirror(Ycore[j])*(af('0.5')*((-1)**p))}
    # k_reg(t)=sum gamma[k]*(t/2)^k. Integrate in y before evaluating x.
    ym=[pint(f*arb_poly([0]*k+[1]),a,b) for k in range(225)]
    regular=[arb(0)]*225
    for k,ck in enumerate(gamma):
        if not ck:continue
        weight=af(ck)/(2**k)
        for l in range(k+1):
            regular[l]+=weight*comb(k,l)*((-1)**l+(-1)**p)*a**l*ym[k-l]
    sing[None]-=arb_poly(regular)
    total=add_function(sing,qm,-lam[j]/mu)
    globalF.append(multiply_fun(total,(2*a).sqrt()))
    shifts=[]
    for ci,(lo,hi) in enumerate(cells):
        mid=a*(roots[lo]+roots[hi])/2;primepart=arb_poly([])
        for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
            shiftby=arb(q).log();w=arb(prime).log()/arb(q).sqrt()
            for sign in [-1,1]:
                at=mid+sign*shiftby
                if at>a and at<b:
                    primepart-=f(arb_poly([sign*shiftby,a]))*w
                elif at>-b and at<-a:
                    primepart-=f(arb_poly([-sign*shiftby,-a]))*(w*((-1)**p))
        shifts.append((primepart-qmshift[ci]*(lam[j]/mu))*(2*a).sqrt())
    cellF.append(shifts)
say(f'{NC} complete core source model(s) formed, including singular Gamma and moments')



# Full one-sided finite parts and exact carrier integrals, without sampling.
def trace_endpoint(fun,shifts):
 al=fun.get('one',arb_poly([]))(arb(1))
 fin=fun.get(None,arb_poly([]))(arb(1))+al*(h/a).log()+shifts[-1](arb(1))
 for tag,poly in fun.items():
  if tag is not None and tag!='one':fin+=poly(arb(1))*abs(1-roots[tag]).log()
 return al,fin

def carrier(fun,shifts):
 mm=function_moments(fun,mom,'zero','one',p)
 for ci,(lo,hi) in enumerate(cells):
  add=mom.polynomial_moments(shifts[ci],lo,hi,p)
  mm=[v+w for v,w in zip(mm,add)]
 return pair(pol[p],mm)*arb(2*p+1).sqrt()

endpointJY=[trace_endpoint(fun,sh) for fun,sh in zip(globalF,cellF)]
carrierJY=[carrier(fun,sh) for fun,sh in zip(globalF,cellF)]
say('92 full endpoint finite parts and carrier integrals completed')

# The four physical z functions are smooth across a. Their exact logarithms
# at +/-b are retained here, rather than Taylor-expanded.
endpointZ=[];carrierZ=[]
for n in range(p+2,p+10,2):
 cnz=arb(2*n+1).sqrt()/arb(2*p+1).sqrt()*mellin(n,b)/mellin(p,b)
 ls=[arb(0)]*(n+1);ls[n]=((2*n+1)/(2*b)).sqrt();ls[p]=-cnz*((2*p+1)/(2*b)).sqrt()
 f=sum((pol[k]*ls[k] for k in range(n+1)),arb_poly([]))
 dh=sum((pol[k]*(ls[k]*sum((arb(1)/v for v in range(1,k+1)),arb(0))) for k in range(n+1)),arb_poly([]))
 smooth=dh+f*(-(2*arb.pi()*b).log()-arb.const_euler())-kernel(f,ls,b,gamma,p)
 f=f(arb_poly([0,1/r]));smooth=smooth(arb_poly([0,1/r]))
 action=multiply_fun({None:smooth+f*r.log(),'outer':f*(-arb(1)/2),'minus_outer':f*(-arb(1)/2)},(2*a).sqrt())
 sh=[]
 for lo,hi in cells:
  mid=(roots[lo]+roots[hi])/2;z=arb_poly([])
  for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
   shift=arb(q).log()/a;weight=arb(prime).log()/arb(q).sqrt()
   for sign in [-1,1]:
    if abs(mid+sign*shift)<r:z-=f(arb_poly([sign*shift,1]))*weight
  sh.append(z*(2*a).sqrt())
 endpointZ.append(trace_endpoint(action,sh));carrierZ.append(carrier(action,sh))
say('four physical z endpoint finite parts and carrier integrals completed')

# Q_a ell_p: one complete source gives every carrier of Q_a Phi_i by
# symmetry. This uses precisely the old degree-160 Gamma model of A.
fp=pol[p]*arb(2*p+1).sqrt();ls=[arb(0)]*(p+1);ls[p]=arb(2*p+1).sqrt()
hp=sum((arb(1)/k for k in range(1,p+1)),arb(0))
q0={None:fp*(hp-(2*arb.pi()*a).log()-arb.const_euler())-kernel(fp,ls,a,gammaOld,p), 'one':fp*(-arb(1)/2),'minus_one':fp*(-arb(1)/2)}
q0sh=[]
for lo,hi in cells:
 mid=(roots[lo]+roots[hi])/2;v=arb_poly([])
 for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
  shift=arb(q).log()/a;weight=arb(prime).log()/arb(q).sqrt()
  for sign in [-1,1]:
   if abs(mid+sign*shift)<1:v-=fp(arb_poly([sign*shift,1]))*weight
 q0sh.append(v)
mm=function_moments(q0,mom,'zero','one',383)
for ci,(lo,hi) in enumerate(cells):
 add=mom.polynomial_moments(q0sh[ci],lo,hi,383)
 mm=[v+w for v,w in zip(mm,add)]
carrierPhi=[pair(f,mm) for f in phi]

# The finite part at t=1 is evaluated from endpoint moments, avoiding a
# degree-543 monomial action for each of the 191 old basis functions.
endpointPhi=[];shiftvals={q:[f(1-arb(q).log()/a) for f in phi] for q in [2,3,4,5,7]}
for j,n in enumerate(range(p+2,384,2)):
 ls={n:arb(2*n+1).sqrt(),p:-cn[j]*arb(2*p+1).sqrt()}
 fv=sum(ls.values(),arb(0));dh=sum((v*sum((arb(1)/i for i in range(1,k+1)),arb(0)) for k,v in ls.items()),arb(0))
 kv=arb(0)
 for k,ck in enumerate(gammaOld):
  if not ck:continue
  mk=sum((v*af(F((-1)**l*2**(k+1)*factorial(k)**2,factorial(k-l)*factorial(k+l+1))) for l,v in ls.items() if l<=k),arb(0))
  kv+=a*af(ck)*(a/2)**k*mk
 fin=dh+fv*(-(2*arb.pi()*a).log()-arb.const_euler())-kv-fv*(2*h/a).log()/2
 for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:fin-=shiftvals[q][j]*arb(prime).log()/arb(q).sqrt()
 endpointPhi.append([-fv/2,fin])

# Direct independent finite-part check on several old basis functions.
checks=[]
for j in [0,17,90,190]:
 n=p+2+2*j;ls=[arb(0)]*(n+1);ls[n]=arb(2*n+1).sqrt();ls[p]=-cn[j]*arb(2*p+1).sqrt()
 dh=pol[n]*(ls[n]*sum((arb(1)/i for i in range(1,n+1)),arb(0)))+pol[p]*(ls[p]*hp)
 smooth=dh+phi[j]*(-(2*arb.pi()*a).log()-arb.const_euler())-kernel(phi[j],ls,a,gammaOld,p)
 fin=smooth(arb(1))-phi[j](arb(1))*(2*h/a).log()/2
 for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:fin-=shiftvals[q][j]*arb(prime).log()/arb(q).sqrt()
 diff=fin-endpointPhi[j][1];assert diff.contains(0) and abs(diff)<af('1e-60')
 checks.append({'column':j,'difference':diff})
say('191 old action traces and carriers completed, with four independent action checks')
result={'parity':args.parity,'bits':args.bits,'normalization':'normalized core t=x/a, multiply physical values by sqrt(2a); finite parts use log(s/h)',
 'source_JY_endpoint_log_and_finite':endpointJY,'source_JY_carrier':carrierJY,
 'source_Z_endpoint_log_and_finite':endpointZ,'source_Z_carrier':carrierZ,
 'old_Qphi_endpoint_log_and_finite':endpointPhi,'old_Qphi_carrier':carrierPhi,
 'old_moment_coefficients_cn':cn,'old_endpoint_raw_low_weights':[arb(2*n+1).sqrt() for n in range(p+2,384,2)],
 'old_endpoint_carrier_weight':arb(2*p+1).sqrt()+sum((arb(2*n+1).sqrt()*cn[j] for j,n in enumerate(range(p+2,384,2))),arb(0)),
 'independent_action_checks':checks,'gamma224_error':epsGamma,'J_rounding':rounding,'Y_rounding':Yrounding,
 'bindings':bindings,'seconds':time.monotonic()-start,'full_remainder_certified':False}
args.out.write_text(json.dumps(serial(result,80),indent=2)+'\n',encoding='utf-8')
say('DONE complete endpoint models; operator error and final residual composition are separate')
