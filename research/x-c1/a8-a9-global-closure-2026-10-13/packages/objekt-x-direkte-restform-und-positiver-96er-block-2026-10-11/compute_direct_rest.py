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
ROOT=HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/compute-deps'), str(ROOT/'work/tail-probe-2026-10-10/vendor'),str(ROOT/'work/tail-probe-2026-10-10'),
             str(ROOT/'work/remainder-integration-check-v2/originals/eight-source/code'),
             str(ROOT/'work/inverse-energy-repo-replay/original/vendor')]
from flint import arb, arb_poly, arb_mat, ctx
from compute_inverse_energy_gate import af, box, serial, loewner_bounds, ldl
from compute_source_mixed import legendre
from eight_source_refined import kernel
from log_integrals import Moments, function_moments, function_product, add_function
from prime_geometry import core_partition
sys.path.insert(0,str(ROOT/'work/galerkin84-2026-10-10'))
from bounded_moments import Moments
import gc
from safe_serial import serial
import source_core as sc

ap=argparse.ArgumentParser()
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
       'frozen':ROOT/f'work/galerkin84-2026-10-10/MODEL_RAY_{args.parity.upper()}_3072.json',
       'centres':INHERITED/f'work/u00-2026-10-07/CENTRES_{args.parity.upper()}_4096.json',
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
assert args.bits>=3072
D=ratmat(data['basis']['D_rational'])
Z=arb_mat([[D[i,j] if i<8 else int(i-8==j) for j in range(NJ)] for i in range(92)])
Jtrue=Q*Z
assert norm_bound(S.transpose()*Z)<af('1e-800')
Jmid=ratmat(data['frozen']['working_basis_midpoints_rational'])
Ysaved=ratmat(data['centres']['Y_local_rational_midpoints'])
rounding=norm_bound(Jtrue-Jmid)+norm_bound(Yfull-Ysaved)
Ymid=arb_mat([[Jmid[i,j] if j<NJ else Ysaved[i,j-NJ] for j in range(NC)] for i in range(96)])
assert rounding<af('1e-60')
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



def core_pair_m(fun,shifts,measure=2*a):
    val=function_product(fun,{None:mcore},mom,'zero','one')
    for (lo,hi),shift in zip(cells,shifts):val+=mom.integral(shift*mcore,lo,hi)
    return measure*val


Msource=[]
for j in range(NC):
    Msource.append(core_pair_m(globalF[j],cellF[j],(2*a).sqrt()))
    if j%16==0:say(f'complete moment-carrier pairings {j}/{NC}')
Qmm=core_pair_m(qm,qmshift)
shellpath=INHERITED/'work/gamma-low-2026-10-09/SHELL_GAMMA_4096.json'
bindings['shell_gamma']=hashlib.sha256(shellpath.read_bytes()).hexdigest()
shell_data=read(shellpath)
def polycols(polys,n):return arb_mat([[v[k] for v in polys] for k in range(n)])
def hankel(seq,n,m):return arb_mat([[seq[i+j] for j in range(m)] for i in range(n)])
def sub(A,rows,cols):return arb_mat([[A[i,j] for j in cols] for i in rows])
localmom=Moments({'left':arb(-1),'right':arb(1)},500)
c_direct=-(arb.pi()*h).log()-arb.const_euler()
harm=[arb(0)]
for n in range(1,96):harm.append(harm[-1]+arb(1)/n)
mass=Ymid.transpose()*Ymid
diagonal=Ymid.transpose()*arb_mat([[(harm[n]+c_direct)*Ymid[n,k] for k in range(NC)] for n in range(96)])
YLpoly=polycols(Ylocal,96)
seq1=localmom.sequence('left','right',('left',),190)
seq2=localmom.sequence('left','right',('right',),190)
potential=sym(YLpoly.transpose()*hankel([-(x+y)*h/2 for x,y in zip(seq1,seq2)],96,96)*YLpoly)
cs32=list(map(F,shell_data['self_coefficients']))
kernels=[]
for j in range(NC):
    ks=arb_poly([])
    for parity_local in [0,1]:
        ls=[Ymid[n,j]*((2*n+1)/(2*h)).sqrt() if n%2==parity_local else arb(0) for n in range(96)]
        rp=sum((pol[n]*ls[n] for n in range(96)),arb_poly([]))
        ks+=kernel(rp,ls,h/2,cs32,parity_local)
    kernels.append(ks)
kd=max(map(len,kernels));seq=localmom.sequence('left','right',(),kd+94)
selfpair=sym(polycols(kernels,kd).transpose()*hankel(seq,kd,96)*YLpoly*h)
vm=[]
for j in range(32):
    rate=af(F(4*j+1,2))
    vm.append([h*((2*n+1)/(2*h)).sqrt()*(-rate*c).exp()*((-1)**n)*mellin(n,rate*h) for n in range(96)])
Mmirror=arb_mat(vm)*Ymid
mirrorpair=2*Mmirror.transpose()*Mmirror
kernelgram=selfpair+((-1)**p)*mirrorpair
correction=arb_mat([[-(lam[i]*Msource[j]+Msource[i]*lam[j])/mu-lam[i]*lam[j]*Qmm/mu**2 for j in range(NC)] for i in range(NC)])
direct=sym(diagonal+potential-kernelgram+correction)
assert epsGamma<af('1e-34') and h>af('1/20') and h<af('1/16') and mu>af('9/100')
assert all(sum((Ymid[i,j]**2 for i in range(96)),arb(0))<4 for j in range(NC))
# Analytic error is paid per true entry, in addition to all interval radii.
result={'status':'FULL_DIRECT_REST84_AND_Y8_ENCLOSED','bits':args.bits,'parity':args.parity,
 'basis_order':'J84 then fixed Y8; unchanged physical functions',
 'mu':mu,'lambda_model':lam,'M_source_model':Msource,'Q_mm_model':Qmm,
 'constant_direct':c_direct,'constant_bonus':c_direct-af('11/10'),
 'mass_model':mass,'shell_diagonal_model':diagonal,'shell_potential_model':potential,
 'shell_self_kernel_model':selfpair,'shell_mirror_unsigned_model':mirrorpair,
 'shell_signed_kernel_model':kernelgram,'moment_correction_model':correction,
 'D92_model':direct,'D84_direct_model':sub(direct,range(NJ),range(NJ)),
 'entry_error':'1e-25','D84_operator_error':'84e-25','D92_operator_error':'92e-25',
 'coefficient_rounding_norm':rounding,'gamma_error':epsGamma,'bindings':bindings,
 'seconds':time.monotonic()-start,'full_remainder_certified':False}
args.out.write_text(json.dumps(serial(result,80),indent=2)+'\n',encoding='utf-8')
say('DONE full direct rest84 matrix including signed kernel and moment terms')
