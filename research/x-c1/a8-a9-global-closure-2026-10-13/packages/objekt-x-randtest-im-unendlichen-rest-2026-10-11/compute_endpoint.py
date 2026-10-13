"""Complete nonpolynomial endpoint-step source and direct-form integrals.

The complete degree<104 projection is removed from a normalized step.
All old high-source moments are integrated, including new prime cuts.
This is data for a necessary tail test, not a full tail upper enclosure.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, comb
import argparse, sys, json, gzip, hashlib, time

HERE=Path(__file__).resolve().parent
ROOT=Path(sys.argv[sys.argv.index('--root')+1]).resolve()
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
ap.add_argument('--root',type=Path,required=True)
ap.add_argument('--cut-power',type=int,default=14)
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
NC=93
NLOC=104
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
ewidth=h/2**args.cut_power
bumpedge=a+ewidth
amplitude=1/(2*ewidth).sqrt()
cutlocal=-1+2*ewidth/h
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
frozenpath=ROOT/f'work/galerkin84-2026-10-10/MODEL_RAY_{args.parity.upper()}_3072.json'
bindings['frozen_J']=hashlib.sha256(frozenpath.read_bytes()).hexdigest()
frozen=read(frozenpath)['working_basis_midpoints_rational']
Rmid=ratmat(frozen)
rounding=norm_bound(YL-Rmid)
savedY=ratmat(data['centres']['Y_local_rational_midpoints'])
Yrounding=norm_bound(Yfull-savedY)
assert rounding<af('1e-60') and Yrounding<af('1e-60')
stepcoeff=[h*amplitude*((2*n+1)/(2*h)).sqrt()*pint(pol[n],arb(-1),cutlocal) for n in range(NLOC)]
# Keep one fixed dyadic polynomial centre; all 104 projection errors are paid.
stepmid=[x.mid() for x in stepcoeff]
stepround=sum((abs(x-y).upper()**2 for x,y in zip(stepcoeff,stepmid)),arb(0)).sqrt()
assert stepround<af('1e-200')
Ymid=arb_mat([[Rmid[i,j] if i<96 and j<84 else savedY[i,j-84] if i<96 and j<92 and j>=84 else -stepmid[i] if j==92 else arb(0) for j in range(NC)] for i in range(NLOC)])
definition='J84,Y8, then normalized endpoint step minus its full degree<104 projection; exact W_X projection is enclosed separately'
actual_coefficients=serial(YL,70)
Ylocal=[];Ycore=[];Yphysical=[]
for j in range(NC):
    f=sum((pol[k]*(Ymid[k,j]*((2*k+1)/(2*h)).sqrt())
           for k in range(NLOC)),arb_poly([]))
    Ylocal.append(f)
    Yphysical.append(f(arb_poly([-c/d,1/d])))
    Ycore.append(f(arb_poly([-c/d,a/d])))
Ynorm=norm_bound(Ymid)
assert Ynorm<14 and rounding<af('1e-50')
shell_m=arb_poly([(d/2)**k/factorial(k)*
                  ((c/2).cosh() if (k+p)%2==0 else (c/2).sinh())
                 for k in range(161)])
lam=[d*pint(f*shell_m,arb(-1),arb(1)) for f in Ylocal]
lam[92]+=amplitude*2*((bumpedge/2).sinh()-(a/2).sinh()) if p==0 else amplitude*2*((bumpedge/2).cosh()-(a/2).cosh())
shell_m_tail=(c/2).exp()*(d/2)**161/factorial(161)/(1-d/(2*162))
lam_error=(h/2).sqrt()*Ynorm*shell_m_tail
assert lam_error<af('1e-300')
say('fixed centres reconstructed; local-coordinate rounding bounded')

gamma,epsGamma=sc.gamma_polynomial(224)
epsGamma=af(epsGamma)
gammaOld=list(map(F,old['Gamma_polynomial_coefficients']))
# Positive-core cells include every new shell-shift and old/core-shift break.
roots,cells,cut_vectors=core_partition(a,b)
roots['bumpouter']=bumpedge/a;roots['minus_bumpouter']=-bumpedge/a
# Add all new prime-shift discontinuities of the narrow step. Old endpoints
# remain named exactly, so no numerical equality is used for old cuts.
ends=['zero']+[lo for lo,hi in cells if lo!='zero']+['one']
for q in [2,3,4,5,7,8]:
    for sign in [-1,1]:
        for endsign in [-1,1]:
            x=(endsign*bumpedge-sign*arb(q).log())/a
            if x>0 and x<1:
                name=f'bumpcut{q}_{sign}_{endsign}';roots[name]=x;ends.append(name)
ends.sort(key=lambda key:float(roots[key].mid()))
assert all(roots[x]<roots[y] for x,y in zip(ends[:-1],ends[1:]))
cells=list(zip(ends[:-1],ends[1:]));mom=Moments(roots,2000)
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
    ym=[pint(f*arb_poly([0]*k+[1]),a,b)+(amplitude*(bumpedge**(k+1)-a**(k+1))/(k+1) if j==92 else 0) for k in range(225)]
    regular=[arb(0)]*225
    for k,ck in enumerate(gamma):
        if not ck:continue
        weight=af(ck)/(2**k)
        for l in range(k+1):
            regular[l]+=weight*comb(k,l)*((-1)**l+(-1)**p)*a**l*ym[k-l]
    sing[None]-=arb_poly(regular)
    if j==92:
        for key,weight in [('bumpouter',-1),('one',1),('minus_bumpouter',-((-1)**p)),('minus_one',(-1)**p)]:
            sing[key]=sing.get(key,arb_poly([]))+arb_poly([amplitude*weight/2])
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
        if j==92:
            for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
                sh=arb(q).log();w=arb(prime).log()/arb(q).sqrt()
                for sign in [-1,1]:
                    at=mid+sign*sh
                    if at>a and at<bumpedge:primepart-=arb_poly([amplitude*w])
                    elif at>-bumpedge and at<-a:primepart-=arb_poly([amplitude*w*((-1)**p)])
        shifts.append((primepart-qmshift[ci]*(lam[j]/mu))*(2*a).sqrt())
    cellF.append(shifts)
say(f'{NC} complete core source model(s) formed, including singular Gamma and moments')



def columns(vectors):return arb_mat([[v[i] for v in vectors] for i in range(len(vectors[0]))])
def sub(A,rows,cols):return arb_mat([[A[i,j] for j in cols] for i in rows])
def polycols(polys,n):return arb_mat([[v[k] for v in polys] for k in range(n)])
def complete_mom(fun,shifts,n,logs=()):
    v=function_moments(fun,mom,'zero','one',n,logs)
    for (lo,hi),part in zip(cells,shifts):
        w=mom.polynomial_moments(part,lo,hi,n,logs);v=[x+y for x,y in zip(v,w)]
    return v
def complete_pair(fun1,sh1,fun2,sh2):
    v=function_product(fun1,fun2,mom,'zero','one')
    for ci,(lo,hi) in enumerate(cells):
        a1={None:sh1[ci]};a2={None:sh2[ci]}
        v+=function_product(fun1,a2,mom,lo,hi)+function_product(a1,fun2,mom,lo,hi)+function_product(a1,a2,mom,lo,hi)
    return v

rawdegrees=list(range(p,544,2))
vm=complete_mom(globalF[92],cellF[92],543)
rawmat=arb_mat([[sum((pol[n][k]*vm[k] for k in range(n+1)),arb(0))*arb(2*n+1).sqrt()] for n in rawdegrees])
rawlow=sub(rawmat,range(192),[0])
cforce=arb_mat([[rawlow[k+1,0]-cn[k]*rawlow[0,0]] for k in range(191)])
projection=sum((pol[n]*(rawlow[i,0]*arb(2*n+1).sqrt()) for i,n in enumerate(range(p,384,2))),arb_poly([]))
hf=add_function(globalF[92],{None:projection},-1)
zero=complete_mom(hf,cellF[92],383)
assert all(abs(sum((pol[n][k]*zero[k] for k in range(n+1)),arb(0)))<af('1e-100') for n in range(p,384,2))
say('full endpoint source and its complete high projection formed')

# Full high cross: hf is orthogonal to every low old polynomial, so it
# may be paired directly with the unprojected 92 bound source functions.
cross=arb_mat(92,1)
for tag in globalF[0]:
    size=max(len(f[tag]) for f in globalF[:92])
    vec=complete_mom(hf,cellF[92],size-1,() if tag is None else (tag,))
    coeff=polycols([f[tag] for f in globalF[:92]],size)
    cross+=coeff.transpose()*columns([vec])
for ci,(lo,hi) in enumerate(cells):
    size=max(len(sh[ci]) for sh in cellF[:92]);fun=add_function(hf,{None:cellF[92][ci]})
    vec=function_moments(fun,mom,lo,hi,size-1)
    cross+=polycols([sh[ci] for sh in cellF[:92]],size).transpose()*columns([vec])
hff=complete_pair(hf,cellF[92],hf,cellF[92])
assert hff>0
say('complete endpoint high Gram and all 92 source crosses integrated')

mixed=arb_mat(191,1);vv=[arb(0)]*384
for tag in ['one','minus_one']:
    vec=complete_mom(hf,cellF[92],383,(tag,));vv=[x-y/2 for x,y in zip(vv,vec)]
mixed+=polycols(phi,384).transpose()*columns([vv])
shiftcache={}
for ci,(lo,hi) in enumerate(cells):
    middle=(roots[lo]+roots[hi])/2
    cm=columns([function_moments(add_function(hf,{None:cellF[92][ci]}),mom,lo,hi,383)])
    operator=arb_mat(191,384)
    for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
        shiftby=arb(q).log()/a;w=arb(prime).log()/arb(q).sqrt()
        for sign in [-1,1]:
            if abs(middle+sign*shiftby)<1:
                key=(q,sign)
                if key not in shiftcache:
                    sp=legendre(383,sign*shiftby)
                    ps=[sp[n]*arb(2*n+1).sqrt()-sp[p]*(cn[k]*arb(2*p+1).sqrt()) for k,n in enumerate(range(p+2,384,2))]
                    shiftcache[key]=polycols(ps,384).transpose()*w
                operator-=shiftcache[key]
    mixed+=operator*cm
up=[1/(arb(2*n+1)*arb(2*n+3)).sqrt() for n in range(550)]
weights={k:2*a*af(gammaOld[k])*(a/2)**k*factorial(k) for k in range(1,161,2)}
gammaMixed=arb_mat(191,len(rawdegrees))
for row,n in enumerate(range(p+2,384,2)):
    if n+160<384+p:continue
    power={n:arb(1)}
    for order in range(1,161):
        nxt={}
        for k,v in power.items():
            nxt[k+1]=nxt.get(k+1,arb(0))+v*up[k]
            nxt[k-1]=nxt.get(k-1,arb(0))-v*up[k-1]
        power=nxt
        if order%2==0:
            for k,v in power.items():
                if k>=384+p:gammaMixed[row,(k-p)//2]-=weights[order-1]*v
mixed+=gammaMixed*rawmat
say('all 191 complete mixed forces integrated')

from eight_source_refined import make_sources
zbase,zsh,zprofiles,zW,ztail,zeps=make_sources(p,[(roots[l],roots[u]) for l,u in cells],pol)
HFK=arb_mat(12,1)
for j in range(4):
    HFK[j,0]=complete_pair({None:zbase[j]},[r[j] for r in zsh],hf,cellF[92])
for j in range(8):HFK[j+4,0]=cross[j+84,0]
say('all twelve complete physical-source crosses integrated')

# Direct physical z/f pairs. The endpoint step is integrated in addition
# to the degree-103 polynomial; there is no Legendre cutoff of the step.
def core_shifts(f,terminal):
    result=[]
    for lo,hi in cells:
        mid=(roots[lo]+roots[hi])/2;out=arb_poly([])
        for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
            shift=arb(q).log()/a;weight=arb(prime).log()/arb(q).sqrt()
            for sign in [-1,1]:
                if abs(mid+sign*shift)<terminal:out-=f(arb_poly([sign*shift,1]))*weight
        result.append(out)
    return result
def core_pair_m(fun,shifts,measure=2*a):
    val=function_product(fun,{None:mcore},mom,'zero','one')
    for (lo,hi),shift in zip(cells,shifts):val+=mom.integral(shift*mcore,lo,hi)
    return measure*val
DFK=arb_mat(12,1)
for j,n in enumerate(range(p+2,p+10,2)):
    cz=arb(2*n+1).sqrt()/arb(2*p+1).sqrt()*mellin(n,b)/mellin(p,b)
    ls=[arb(0)]*(n+1);ls[n]=((2*n+1)/(2*b)).sqrt();ls[p]=-cz*((2*p+1)/(2*b)).sqrt()
    f=sum((pol[k]*ls[k] for k in range(n+1)),arb_poly([]))
    dh=sum((pol[k]*(ls[k]*sum((arb(1)/v for v in range(1,k+1)),arb(0))) for k in range(n+1)),arb_poly([]))
    smooth=dh+f*(-(2*arb.pi()*b).log()-arb.const_euler())-kernel(f,ls,b,gamma,p)
    f=f(arb_poly([0,1/r]));smooth=smooth(arb_poly([0,1/r]))
    action={None:smooth+f*r.log(),'outer':f*(-arb(1)/2),'minus_outer':f*(-arb(1)/2)}
    Mz=core_pair_m(action,core_shifts(f,r));shell=dict(action)
    for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
        shell[None]-=f(arb_poly([-arb(q).log()/a,1]))*(arb(prime).log()/arb(q).sqrt())
    val=function_product(shell,{None:Ycore[92]},mom,'one','outer')
    val+=amplitude*function_moments(shell,mom,'one','bumpouter',0)[0]
    DFK[j,0]=2*a*val-lam[92]*Mz/mu

shellpath=INHERITED/'work/gamma-low-2026-10-09/SHELL_GAMMA_4096.json';shell_data=read(shellpath)
cs32=list(map(F,shell_data['self_coefficients']));kernels=[]
for j in range(92):
    ks=arb_poly([])
    for parity_local in [0,1]:
        ls=[Ymid[n,j]*((2*n+1)/(2*h)).sqrt() if n%2==parity_local else arb(0) for n in range(96)]
        rp=sum((pol[n]*ls[n] for n in range(96)),arb_poly([]));ks+=kernel(rp,ls,h/2,cs32,parity_local)
    kernels.append(ks)
localmom=Moments({'left':arb(-1),'right':arb(1),'cut':cutlocal},500)
def test_poly(poly,logs=()):
    return localmom.integral(poly*Ylocal[92],'left','right',logs)+amplitude*localmom.integral(poly,'left','cut',logs)
Mtest=[];Mknown=[]
for j in range(32):
    rate=af(F(4*j+1,2))
    coefficients=[h*((2*n+1)/(2*h)).sqrt()*(-rate*c).exp()*((-1)**n)*mellin(n,rate*h) for n in range(NLOC)]
    v=sum((coefficients[n]*Ymid[n,92] for n in range(NLOC)),arb(0))+amplitude*((-rate*a).exp()-(-rate*bumpedge).exp())/rate
    Mtest.append(v)
    Mknown.append([sum((coefficients[n]*Ymid[n,k] for n in range(96)),arb(0)) for k in range(92)])
Msource_test=core_pair_m(globalF[92],cellF[92],(2*a).sqrt())
Msource_known=[core_pair_m(globalF[j],cellF[j],(2*a).sqrt()) for j in range(92)]
Qmm=core_pair_m(qm,qmshift)
harm=[arb(0)]
for n in range(1,NLOC):harm.append(harm[-1]+arb(1)/n)
c_direct=-(arb.pi()*h).log()-arb.const_euler();DJK=arb_mat(84,1)
direct92=[]
for j in range(92):
    diag=sum(((harm[n]+c_direct)*Ymid[n,j]*(stepcoeff[n]+Ymid[n,92]) for n in range(96)),arb(0))
    potential=-h*(test_poly(Ylocal[j],('left',))+test_poly(Ylocal[j],('right',)))/2
    selfpair=h*test_poly(kernels[j])
    mirrorpair=2*sum((Mknown[k][j]*Mtest[k] for k in range(32)),arb(0))
    correction=-(lam[j]*Msource_test+Msource_known[j]*lam[92])/mu-lam[j]*lam[92]*Qmm/mu**2
    val=diag+potential-selfpair-((-1)**p)*mirrorpair+correction
    direct92.append(val)
    if j<84:DJK[j,0]=val
    else:DFK[j-80,0]=val
say('all direct endpoint pairs include the complete step and moment correction')

# Exact infinite weighted Legendre energy of the normalized step.
# The harmonic operator has kernel (f(x)-f(y))/(2|x-y|).
entropy=h*h.log()-ewidth*ewidth.log()-(h-ewidth)*(h-ewidth).log()
Lstep=af('1.1')+entropy/(2*ewidth)
Loutside=Lstep-sum(((harm[n]+af('1.1'))*stepcoeff[n]**2 for n in range(NLOC)),arb(0))
massoutside=1-sum((v*v for v in stepcoeff),arb(0));assert Loutside>0 and massoutside>0
nu=(b.sinh()-a.sinh()+(h if p==0 else -h))/2
qcore_norm=box(half['core_form_absolute_bound'])/(2*mu).sqrt()
global_source_norm=af('3.2')+(nu/2).sqrt()*qcore_norm/mu
epsilon_f=2*b*epsGamma*(2+abs(lam[92])*(2*mu).sqrt()/mu)+af('1e-190')+global_source_norm*stepround
gamma_a=af('2.1')*af(old['Gamma_kernel_error_exact'])
em=(af('0.525')**(384+p)/factorial(384+p)/(1-af('0.525')**2/((385+p)*(386+p))))*(4 if p else 1)
eB=2*gamma_a+24*em;epsilon_h=(1+em**2).sqrt()*epsilon_f+em*abs(rawlow[0,0])
assert epsGamma<af('1e-34') and stepround<af('1e-200')
out={'status':'COMPLETE_ENDPOINT_STEP_TEST_DATA','parity':args.parity,'bits':args.bits,'cut_power':args.cut_power,
 'definition':definition,'outside_degrees_from':104,'step_projection_coefficients':stepcoeff,
 'mass_outside':massoutside,'L_step_exact_model':Lstep,'L_outside_exact_model':Loutside,
 'source_c_model':cforce,'source_Bh_model':mixed,'H_J_test_model':sub(cross,range(84),[0]),'H_F_test_model':HFK,
 'H_test_model':hff,'direct_J_test_model':DJK,'direct_F_test_model':DFK,
 'source_error_norm':epsilon_f,'high_source_error_norm':epsilon_h,'old_coupling_error_norm':eB,
 'moment_basis_coefficients':cn,'direct_entry_error':'1e-20','working_step_projection_rounding':stepround,
 'full_geometric_test_correction_norm_upper':'1e-350','bindings':bindings,'seconds':time.monotonic()-start,
 'full_remainder_certified':False,'negative_actual_Schur_witness':False}
args.out.write_text(json.dumps(serial(out,80),indent=2)+'\n')
say('DONE full endpoint test; no infinite upper bound is asserted')
