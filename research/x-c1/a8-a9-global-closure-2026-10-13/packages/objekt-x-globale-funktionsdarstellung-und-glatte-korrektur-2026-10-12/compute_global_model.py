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
endpointZ=[];carrierZ=[];globalZ=[];cellZ=[];profileZ=[]
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
 endpointZ.append(trace_endpoint(action,sh));carrierZ.append(carrier(action,sh));globalZ.append(action);cellZ.append(sh);profileZ.append(f)
say('four physical z endpoint finite parts and carrier integrals completed')


# Build a complete finite FUNCTION model, then apply the exterior operator.
# This is not a global Gram or an operator-error certificate.
from cauchy_transform import cauchy_moments, row_pair, integer_powers
label=args.parity.upper()
reference_paths={
 'common':ROOT/'work/direct-rest84-2026-10-11/REFINED_COMMON96.json',
 'input':ROOT/'work/direct-rest84-2026-10-11/REFINED_INPUT.json',
 'response':ROOT/f'work/new-responses84-2026-10-11/RESPONSES_{label}.json',
 'inner':ROOT/'work/inner-log-2026-10-12/INNER_LOG_1536.json',
 'traces':ROOT/f'work/inner-log-2026-10-12/TRACES_{label}_3072.json',
 'composed':ROOT/f'work/inner-log-2026-10-12/COMPOSED_{label}_3072.json',
 'shell':INHERITED/'work/gamma-low-2026-10-09/SHELL_GAMMA_4096.json'}
bindings.update({k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in reference_paths.items()})
new=read(reference_paths['common'])['cases'][p]
inp=read(reference_paths['input'])['cases'][p]
resp=read(reference_paths['response']);inner=read(reference_paths['inner'])['cases'][p]
ep=read(reference_paths['traces']);comp=read(reference_paths['composed'])

def freeze(v):
    if isinstance(v,list):return af((F(v[0])+F(v[1]))/2)
    return af(v)
def frozen_matrix(v):return arb_mat([[freeze(x) for x in rr] for rr in v])
def polycols(pp,n=None):
    n=max(map(len,pp)) if n is None else n
    return arb_mat([[f[k] for f in pp] for k in range(n)])
def cols_to_polys(mm):
    return [arb_poly([mm[k,j] for k in range(mm.nrows())]) for j in range(mm.ncols())]
def submat(v,ii,jj):return arb_mat([[v[i,j] for j in jj] for i in ii])
def row(v):return arb_mat([v])

delta=af(resp['delta']);eta=af(resp['eta']);rho=af(resp['rho'])
AC=arb_mat([[af(F(int(z),int(new['inverse_congruence_denominator']))) for z in rr] for rr in new['inverse_congruence_integer_matrix']])
X=ratmat(resp['X84x203_rational'])
lowF=frozen_matrix(inner['new_low_F_model'])
qcoeff=AC*arb_mat([[int(i==j) if j<191 else -lowF[i,j-191]/(1-rho) for j in range(203)] for i in range(191)])
# Source order: 84 J, eight Y, four physical z.
sourcecoeff=arb_mat([[X[i,j]/delta if i<84 else -int(j==195+i-84)/delta if i<92 else -int(j==191+i-92)/delta for j in range(203)] for i in range(96)])
source_global=globalF+globalZ;source_cell=cellF+cellZ
source_cJ=frozen_matrix(inp['galerkin']['old_low_c_model'])
source_cF=frozen_matrix(inp['old_certificate']['source_c_model'])
csource=arb_mat([[source_cJ[i,j] if j<84 else source_cF[i,j-80] if j<92 else source_cF[i,j-92] for j in range(96)] for i in range(191)])
# New exact analytic carrier integrals are kept, not dropped.
cars=carrierJY+carrierZ
rawsource=arb_mat([[cars[j] if i==0 else csource[i-1,j]+cn[i-1]*cars[j] for j in range(96)] for i in range(192)])
rawbasis=polycols([pol[n]*arb(2*n+1).sqrt() for n in range(p,384,2)],384)
proj_source=cols_to_polys(rawbasis*rawsource)
source_high=[add_function(f,{None:pr},-1) for f,pr in zip(source_global,proj_source)]

# Complete old Q_a Phi model; all logarithms remain functions.
rawA=old['parities'][args.parity]['A']
A=arb_mat([[af(F(int(v[0])+int(v[1]),2*10**100)) for v in rr] for rr in rawA])
oldcars=[freeze(v) for v in ep['old_Qphi_carrier']]
rawold=arb_mat([[oldcars[j] if i==0 else A[i-1,j]+cn[i-1]*oldcars[j] for j in range(191)] for i in range(192)])
proj_old=cols_to_polys(rawbasis*rawold)
phi_matrix=polycols(phi,384)
old_smooth=[]
hp=sum((arb(1)/k for k in range(1,p+1)),arb(0))
for j,n in enumerate(range(p+2,384,2)):
    ls=[arb(0)]*(n+1);ls[n]=arb(2*n+1).sqrt();ls[p]=-cn[j]*arb(2*p+1).sqrt()
    dh=pol[n]*(ls[n]*sum((arb(1)/k for k in range(1,n+1)),arb(0)))+pol[p]*(ls[p]*hp)
    action=dh+phi[j]*(-(2*arb.pi()*a).log()-arb.const_euler())-kernel(phi[j],ls,a,gammaOld,p)
    old_smooth.append(phi[j]-(action-proj_old[j])*(1/delta))
    if j%32==0:say(f'full old action model {j}/191')
low_global=[{None:f,'one':ph*(1/(2*delta)),'minus_one':ph*(1/(2*delta))} for f,ph in zip(old_smooth,phi)]
source_tags=list(source_high[0])
source_matrices={tag:polycols([f.get(tag,arb_poly([])) for f in source_high]) for tag in source_tags}
low_matrices={tag:polycols([f[tag] for f in low_global]) for tag in [None,'one','minus_one']}
source_cell_matrices=[polycols([v[ci] for v in source_cell]) for ci in range(len(cells))]
old_shifts=[]
for primepower,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
    weight=arb(prime).log()/arb(primepower).sqrt()/delta
    shift=arb(primepower).log()/a
    for sign in [-1,1]:
        sh=sign*shift;lo=max(arb(0),-1-sh);hi=min(arb(1),1-sh)
        if lo<hi:old_shifts.append((sh,lo,hi,weight))
say('complete core model assembled: 203 columns, five log roots, all prime cells')

def matrix_value(mm,t):return row(integer_powers(t,mm.nrows()-1))*mm
def eval_global(matrices,t):
    answer=arb_mat(1,next(iter(matrices.values())).ncols())
    for tag,mm in matrices.items():
        value=matrix_value(mm,t)
        if tag is not None:value*=abs(t-roots[tag]).log()
        answer+=value
    return answer
def core_value(t):
    sign=1
    if t<0:t=-t;sign=(-1)**p
    assert t>0 and t<1
    aa=eval_global(source_matrices,t)
    matches=[i for i,(lo,hi) in enumerate(cells) if roots[lo]<t and t<roots[hi]]
    assert len(matches)==1
    aa+=matrix_value(source_cell_matrices[matches[0]],t)
    bb=eval_global(low_matrices,t)
    for sh,lo,hi,weight in old_shifts:
        if lo<t and t<hi:bb+=matrix_value(phi_matrix,t+sh)*weight
    return (aa*sourcecoeff+bb*qcoeff)*sign

def cauchy_global(matrices,s):
    answer=arb_mat(1,next(iter(matrices.values())).ncols())
    for tag,mm in matrices.items():
        seq=cauchy_moments(s,roots['zero'],roots['one'],mm.nrows()-1,None if tag is None else roots[tag])
        answer+=row_pair(seq,mm,arb_mat)
    return answer
def core_cauchy(s):
    aa=cauchy_global(source_matrices,s)
    for ci,(lo,hi) in enumerate(cells):
        mm=source_cell_matrices[ci]
        aa+=row_pair(cauchy_moments(s,roots[lo],roots[hi],mm.nrows()-1),mm,arb_mat)
    bb=cauchy_global(low_matrices,s)
    for sh,lo,hi,weight in old_shifts:
        bb+=row_pair(cauchy_moments(s+sh,lo+sh,hi+sh,383),phi_matrix,arb_mat)*weight
    return aa*sourcecoeff+bb*qcoeff

# Full monomial moments, solely for the polynomial regular kernel.
# They are integrated over all core cells, not cut off Legendre coefficients.
source_mom=[]
for f,shifts in zip(source_high,source_cell):
    mm=function_moments(f,mom,'zero','one',224)
    for ci,(lo,hi) in enumerate(cells):
        cc=mom.polynomial_moments(shifts[ci],lo,hi,224)
        mm=[v+w for v,w in zip(mm,cc)]
    source_mom.append(mm)
low_mom=[]
for j,f in enumerate(low_global):
    mm=function_moments(f,mom,'zero','one',224)
    for sh,lo,hi,weight in old_shifts:
        ph=phi[j](arb_poly([sh,1]))*weight
        pp=ph.integral()
        # Polynomial convolution integrates every power exactly.
        seq=[(hi**(k+1)-lo**(k+1))/(k+1) for k in range(len(ph)+224)]
        conv=arb_poly(list(reversed(ph.coeffs())))*arb_poly(seq)
        dd=len(ph)-1
        mm=[v+conv[dd+k] for k,v in enumerate(mm)]
    low_mom.append(mm)
core_mom=arb_mat(source_mom).transpose()*sourcecoeff+arb_mat(low_mom).transpose()*qcoeff
say('complete core moments through 224 integrated for the regular kernel')

def regular_weights(x):
    weights=[arb(0)]*225
    for k,ck in enumerate(gamma):
        if not ck:continue
        for l in range(k+1):weights[l]+=af(ck)*comb(k,l)*x**(k-l)*a**l*((-1)**l+(-1)**p)/(2**k)
    return row(weights)
def exterior_core(x):
    s=x/a
    singular=-(core_cauchy(s)-((-1)**p)*core_cauchy(-s))/(2*(2*a).sqrt())
    regular=-(2*a).sqrt()/2*regular_weights(x)*core_mom
    shifts=arb_mat(1,203)
    for primepower,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
        shifts-=core_value((x-arb(primepower).log())/a)*(arb(prime).log()/arb(primepower).sqrt()/(2*a).sqrt())
    return singular+regular+shifts

# Direct shell Q action on Lambda J, Lambda Y and the four physical z.
shell_data=read(reference_paths['shell']);cs32=list(map(F,shell_data['self_coefficients']))
shell_smooth=[];mmirror=[]
harm=[sum((arb(1)/k for k in range(1,n+1)),arb(0)) for n in range(96)]
for j in range(92):
    sf=sum((pol[n]*(Ymid[n,j]*((2*n+1)/(2*h)).sqrt())*(harm[n]-(arb.pi()*h).log()-arb.const_euler()) for n in range(96)),arb_poly([]))
    for pl in [0,1]:
        ls=[Ymid[n,j]*((2*n+1)/(2*h)).sqrt() if n%2==pl else arb(0) for n in range(96)]
        rp=sum((pol[n]*ls[n] for n in range(96)),arb_poly([]))
        sf-=kernel(rp,ls,h/2,cs32,pl)
    shell_smooth.append(sf)
for j in range(32):
    rate=af(F(4*j+1,2))
    mmirror.append([h*((2*n+1)/(2*h)).sqrt()*(-rate*c).exp()*((-1)**n)*mellin(n,rate*h) for n in range(96)])
mirror_model=arb_mat(mmirror)*Ymid
shell_matrix=polycols(shell_smooth)
ylocal_matrix=polycols(Ylocal)

def core_polynomial_exterior(f,x):
    """Physical polynomial supported on the core, with prescribed parity."""
    fm=[pint(f*arb_poly([0]*k+[1])) for k in range(225)]
    sing=-(sum((f[k]*v for k,v in enumerate(cauchy_moments(x/a,arb(0),arb(1),len(f)-1))),arb(0))-((-1)**p)*sum((f[k]*v for k,v in enumerate(cauchy_moments(-x/a,arb(0),arb(1),len(f)-1))),arb(0)))/2
    reg=-a*(regular_weights(x)*arb_mat([[v] for v in fm]))[0,0]
    sh=-sum((arb(prime).log()/arb(q).sqrt()*f((x-arb(q).log())/a) for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]),arb(0))
    return sing+reg+sh
def direct_shell(x):
    t=(x-c)/d
    yy=matrix_value(shell_matrix,t)-matrix_value(ylocal_matrix,t)*(1-t*t).log()/2
    yy-=((-1)**p)*row([(-af(F(4*j+1,2))*x).exp() for j in range(32)])*mirror_model
    qms=core_polynomial_exterior(mcore,x)
    yy-=row(lam)*(qms/mu)
    zz=[]
    for f,prof in zip(globalZ,profileZ):
        v=eval_global({tag:polycols([po]) for tag,po in f.items()},x/a)[0,0]/(2*a).sqrt()
        v-=sum((arb(prime).log()/arb(q).sqrt()*prof((x-arb(q).log())/a) for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]),arb(0))
        zz.append(v)
    finite=row(zz+[yy[0,j] for j in range(84,92)])
    out=arb_mat([[arb(0)]*191+[finite[0,j] for j in range(12)]])
    return out-(1-eta)*submat(yy,[0],range(84))*X

# This extension omits only the smooth moment-adjoint term and the canonical
# T projection. Neither omission is silently counted as a certified error.
# Their exact algebraic form and the missing error charge are in PROOF.txt.
def raw_residual_model(x):return direct_shell(x)+exterior_core(x)

# Compare the independently assembled core finite part with earlier traces.
def endpoint_parts(matrices):
    al=matrix_value(matrices.get('one',arb_mat(1,next(iter(matrices.values())).ncols())),arb(1))
    fi=matrix_value(matrices[None],arb(1))+al*(h/a).log()
    for tag,mm in matrices.items():
        if tag not in (None,'one'):fi+=matrix_value(mm,arb(1))*abs(1-roots[tag]).log()
    return al,fi
sa,sf=endpoint_parts(source_matrices);sf+=matrix_value(source_cell_matrices[-1],arb(1))
ba,bf=endpoint_parts(low_matrices)
for sh,lo,hi,weight in old_shifts:
    if hi==arb(1):bf+=matrix_value(phi_matrix,1+sh)*weight
alog=(sa*sourcecoeff+ba*qcoeff)/(2*a).sqrt()
afin=(sf*sourcecoeff+bf*qcoeff)/(2*a).sqrt()
endpoint_diff=[alog-mat(comp['A_log_model']),afin-mat(comp['A_fin_model'])]
for v in endpoint_diff:assert norm_bound(v)<af('1e-45'),norm_bound(v)
say('406 independently assembled core endpoint coefficients agree within 1e-45')
inner_jumps=row([Ylocal[j](arb(-1))+lam[j]*mcore(arb(1))/mu for j in range(92)])
gjump=arb_mat([[arb(0)]*195+[inner_jumps[0,j] for j in range(84,92)]])-(1-eta)*submat(inner_jumps,[0],range(84))*X
c1=-gjump/2+afin/2-((-1)**p)*arb(2).log()/arb(8).sqrt()*alog
c2=alog/4
outer_f=row([prof(r) for prof in profileZ]+[Ylocal[j](arb(1)) for j in range(84,92)])
c3=((1-eta)*row([Ylocal[j](arb(1)) for j in range(84)])*X-arb_mat([[arb(0)]*191+[outer_f[0,j] for j in range(12)]]))/2
cc=arb_mat([[v[0,j] for j in range(203)] for v in [c1,c2,c3]])
log_diff=norm_bound(cc-mat(comp['C_three_log_rows_model']))
assert log_diff<af('1e-45')
say('all 609 leading logarithmic coefficients agree with the previous certified model')
points=[]
for uq in ['1/4','1/2','3/4']:
    u=af(uq);xx=a+h*u
    rr=raw_residual_model(xx)
    assert all(rr[0,j].is_finite() for j in range(203)),('non-finite model',uq)
    points.append({'u':uq,'raw_residual_model_1x203':rr})
    say('complete function model evaluated at u='+uq)
out={'status':'COMPLETE_RAW_FUNCTION_MODEL_IMPLEMENTED_CANONICAL_AND_ERROR_CERTIFICATES_OPEN',
 'parity':args.parity,'bits':args.bits,'source_columns':96,'old_columns':191,'residual_columns':203,
 'definition':'raw Q(Fv-(1-eta)Lambda JX)+Q(core W), restricted to shell; not yet canonical R_X',
 'endpoint_A_log_difference_norm':norm_bound(endpoint_diff[0]),'endpoint_A_fin_difference_norm':norm_bound(endpoint_diff[1]),
 'three_log_rows_difference_norm':log_diff,
 'points':points,'bindings':bindings,'seconds':time.monotonic()-start,
 'global_raw_function_formula_implemented':True,'canonical_R_X_model_completed':False,
 'global_model_Gram_computed':False,'global_model_error_certified':False,'full_remainder_certified':False}
args.out.write_text(json.dumps(serial(out,80),indent=2)+'\n',encoding='utf-8')
say('DONE raw global function model; canonical correction, global Gram and complete error are open')
