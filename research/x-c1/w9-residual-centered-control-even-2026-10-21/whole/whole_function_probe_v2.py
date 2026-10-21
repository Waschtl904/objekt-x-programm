"""Exploratory complete residual function. All decisions remain uncertified."""
import argparse,json,sys,time,hashlib
from pathlib import Path
from math import factorial
from flint import arb,acb,arb_poly,arb_mat,ctx
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'objekt-x-integration-20261019'
ap=argparse.ArgumentParser();ap.add_argument('--nodes',type=int,default=64);ap.add_argument('--outer-nodes',type=int,default=32);args=ap.parse_args()
start=time.monotonic()
program_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
exec(compile((HERE/'probe.py').read_text().split('# Midpoint-only trade-off')[0],str(HERE/'probe.py'),'exec'))
ctx.prec=3072
src=ROOT/'research/x-c1/w9-partial-energy-2026-10-18'
resmod=module('residuals',src/'residuals.py');of=module('old_fields',src/'old_fields.py')
logmod=module('log_integrals',Path('C:/Users/sebas/Documents/Codex/2026-10-09/github-plugin-github-openai-curated-remote/work/tail-probe-2026-10-10/vendor/log_integrals.py'))
res=resmod.Residuals(env['inp'],'even');a,b,hs=res.a8,res.a,res.hs
mid=(a+b)/2;half=hs/2;mu=res.mu8;leg=res.legs
midmat=lambda A:arb_mat([[A[i,j].mid() for j in range(A.ncols())] for i in range(A.nrows())])
coeff=midmat(env['c']);w=midmat(w);cc=[coeff[i,0] for i in range(12)]
ki=midmat(e.w['Ki']);aa=midmat(e.w['a']);pv=midmat(ki*(aa*w-e.v*coeff))
raw=env['inp'].json('old_sources')['cases'][0]
cF=midmat(mat(raw['old_certificate']['source_c_model']));cJ=midmat(mat(raw['galerkin']['old_low_c_model']))
byF=midmat(mat(raw['old_certificate']['source_Bh_model']));byJ=midmat(mat(raw['galerkin']['old_low_Bh_model']))
cs=cJ*w-midmat(e.ell)*coeff-cF*pv
bys=byJ*w-midmat(e.By)*coeff-byF*pv
C=e.w['C'];delta=e.w['delta'];rho=e.w['rho']
ff=midmat(C*C.transpose()*(cs-bys/delta)/(1-rho))
old=env['inp'].json('a8_model')
Am=arb_mat([[q(v[0]).union(q(v[1]))/10**100 for v in row]for row in old['parities']['even']['A']])
low=midmat(cs-midmat(Am)*ff)
Y=midmat(c.ratmat(env['inp'].json('frozen_Y_even')['Y_local_rational_midpoints']))
J=midmat(c.ratmat(env['inp'].json('frozen_J_even')['working_basis_midpoints_rational']))
gamma=of.gamma_coefficients(224);gamma_old=list(map(q,old['Gamma_polynomial_coefficients']))
mc=arb_poly([(a/2)**k/factorial(k) if k%2==0 else arb(0) for k in range(161)])
mls=[arb(0)]*161;mdh=arb_poly([])
harm=[arb(0)]
for k in range(1,550):harm.append(harm[-1]+arb(1)/k)
for n in range(0,161,2):
    mls[n]=(2*n+1)*c.pint(mc*leg[n]);mdh+=leg[n]*(mls[n]*harm[n])
qm={None:mdh+mc*(-(2*arb.pi()*a).log()-arb.const_euler())-of.kernel(mc,mls,a,gamma,0),
    'one':mc*(-arb(1)/2),'minus_one':mc*(-arb(1)/2)}
rootvalues={'one':arb(1),'minus_one':arb(-1),'outer':b/a,'minus_outer':-b/a}
channels=[(arb(n).log(),arb(p).log()/arb(n).sqrt())for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2))]
fac=[arb(factorial(k))for k in range(600)]
convker=arb_poly([gamma[k]/2**k*fac[k]for k in range(224,-1,-1)])
def mirror(p):return arb_poly([(-1)**k*v for k,v in enumerate(p)])
def add(dst,src,factor=1):
    for tag,p in src.items():dst[tag]=dst.get(tag,arb_poly([]))+p*factor
def source_poly(n,length):
    base=c.mellin(0,length)
    ls=[arb(0)]*(n+1);ls[n]=(arb(2*n+1)/(2*length)).sqrt()
    ls[0]=-arb(2*n+1).sqrt()*c.mellin(n,length)/base/(2*length).sqrt()
    return leg[n]*ls[n]+leg[0]*ls[0],ls
phi=[]
for n in range(2,384,2):phi.append(source_poly(n,a)[0])
zp=[source_poly(n,b)for n in range(2,10,2)]
def regular_out(moments):
    v=[(2*moments[k] if k%2==0 else arb(0))/fac[k]for k in range(225)]
    co=convker*arb_poly(v)
    return arb_poly([co[224-k]/fac[k]for k in range(225)])
def build_core(qphi,qF,qJ):
    """Q of the combined old function, with exact logs and prime cells."""
    g={};ph=arb_poly([]);z=arb_poly([]);ls=[arb(0)]*384
    for i,n in enumerate(range(2,384,2)):
        ph+=phi[i]*qphi[i,0]
        ls[n]+=qphi[i,0]*(arb(2*n+1)/(2*a)).sqrt()
    ls[0]=ph[0]-sum((ls[n]*leg[n][0]for n in range(2,384,2)),arb(0))
    dh=sum((leg[n]*(ls[n]*harm[n])for n in range(384)),arb_poly([]))
    add(g,{None:dh+ph*(-(2*arb.pi()*a).log()-arb.const_euler())-of.kernel(ph,ls,a,gamma_old,0),
           'one':ph*(-arb(1)/2),'minus_one':ph*(-arb(1)/2)})
    for i,(pol,zls) in enumerate(zp):
        zz=pol(arb_poly([0,a/b]));z+=zz*qF[i,0]
        smooth=sum((leg[n]*(zls[n]*harm[n])for n in range(len(zls))),arb_poly([]))
        smooth+=pol*(-(2*arb.pi()*b).log()-arb.const_euler())-of.kernel(pol,zls,b,gamma,0)
        add(g,{None:smooth(arb_poly([0,a/b]))+zz*(b/a).log(),'outer':zz*(-arb(1)/2),'minus_outer':zz*(-arb(1)/2)},qF[i,0])
    slocal=Y*arb_mat([[qF[i,0]]for i in range(4,12)])+J*qJ
    sp=sum((leg[k]*(slocal[k,0]*(arb(2*k+1)/(2*hs)).sqrt())for k in range(96)),arb_poly([]))
    spx=sp(arb_poly([-mid/half,1/half]));yc=spx(arb_poly([0,a]))
    lm=sum((slocal[k,0]*(hs*(2*k+1)/2).sqrt()*c.mellin(k,hs/2)*((mid/2).cosh()if k%2==0 else(mid/2).sinh())for k in range(96)),arb(0))
    div=arb_poly([sum((spx[k]*(b**(k-l)-a**(k-l))/(k-l)for k in range(l+1,len(spx))),arb(0))for l in range(len(spx)-1)])(arb_poly([0,a]))
    ym=[c.pint(spx*arb_poly([0]*k+[1]),a,b)for k in range(225)]
    add(g,{None:(div+mirror(div))*(-arb(1)/2)-regular_out(ym)(arb_poly([0,a])),
           'outer':yc*(-arb(1)/2),'one':yc*(arb(1)/2),
           'minus_outer':mirror(yc)*(-arb(1)/2),'minus_one':mirror(yc)*(arb(1)/2)})
    add(g,qm,-lm/mu)
    core=ph+z-mc*(lm/mu)
    shell=z(arb_poly([0,1/a]))+spx
    def prime(lo,hi):
        at=(lo+hi)/2;out=arb_poly([])
        for sh,wt in channels:
            for sign in (-1,1):
                y=at+sign*sh
                if abs(y)<a:out-=core(arb_poly([sign*sh/a,1]))*wt
                elif a<abs(y)<b:out-=shell(arb_poly([sign*sh,a])if y>0 else arb_poly([-sign*sh,-a]))*wt
        return out
    return g,prime,sp,spx,lm,slocal

g,prime,*_=build_core(-ff,-pv,w)
eta=q('1e-10');zero=arb_mat(191,1)
gpsi,primepsi,sp,spx,lm,slocal=build_core(zero,pv,-(1-eta)*w)
phif=sum((phi[i]*ff[i,0]for i in range(191)),arb_poly([]))
plow=sum((leg[n]*(low[i,0]*(arb(2*n+1)/(2*a)).sqrt())for i,n in enumerate(range(2,384,2))),arb_poly([]))
cuts=list(res.cuts)
for sh,wt in channels:cuts.extend([sh-a,a-sh,sh-b,b-sh])
cuts=[x for x in cuts if 0<x<a];cuts.sort(key=float);edges=[arb(0)]
for x in cuts:
    if not x.overlaps(edges[-1]):edges.append(x)
edges.append(a)
endpoint_names=['zero']+[f'c{i}'for i in range(1,len(edges)-1)]+['one']
roots={**rootvalues,**{name:v/a for name,v in zip(endpoint_names,edges)}}
roots['one']=arb(1)
mom=logmod.Moments(roots,1100)
cells=list(zip(endpoint_names[:-1],endpoint_names[1:]))
def integrate_static(parts,primes,n=0):
    result=logmod.function_moments(parts,mom,'zero','one',n)
    for (lo,hi),pp in zip(cells,primes):
        row=mom.polynomial_moments(pp,lo,hi,n)
        result=[v+x for v,x in zip(result,row)]
    return result
pp=[prime(lo,hi)for lo,hi in zip(edges[:-1],edges[1:])]
pps=[primepsi(lo,hi)for lo,hi in zip(edges[:-1],edges[1:])]
def hfun(fun,x):return sum((z*v for z,v in zip(cc,fun(x))),arb(0))
nodes={}
def gauss(n):
    if n not in nodes:nodes[n]=[arb.legendre_p_root(n,k,weight=True)for k in range(n)]
    return nodes[n]
panels=[(lo,hi,args.nodes)for lo,hi in zip(edges[:-2],edges[1:-1])]
width=a-edges[-2]
for k in range(48):panels.append((a-width*arb(2)**(-k),a-width*arb(2)**(-k-1),max(24,args.nodes//2)))
hpoints=[];hmom=[arb(0)]*225;hm=arb(0);hq=arb(0)
def evaluate(parts,t):
    v=parts.get(None,arb_poly([]))(t)
    for tag,p in parts.items():
        if tag is not None:v+=p(t)*abs(t-rootvalues[tag]).log()
    return v
def qmprime(lo,hi):
    at=(lo+hi)/2;out=arb_poly([])
    for sh,wt in channels:
        for sign in (-1,1):
            if abs(at+sign*sh)<a:out-=mc(arb_poly([sign*sh/a,1]))*wt
    return out
qmp=[qmprime(lo,hi)for lo,hi in zip(edges[:-1],edges[1:])]
print('Core function expressions ready',round(time.monotonic()-start,1),flush=True)
for k,(lo,hi,n) in enumerate(panels):
    fun=res.cell(lo,hi);qp=qmprime(lo,hi)
    rv=[];powers=[]
    for z,wt in gauss(n):
        x=(lo+hi)/2+(hi-lo)*z/2;ww=(hi-lo)*wt/2;hh=hfun(fun,x);t=x/a
        hpoints.append((x,ww*hh));hm+=ww*hh*res.m(x)
        hq+=ww*hh*(evaluate(qm,t)+qp(t))
        row=[arb(1)]
        for j in range(224):row.append(row[-1]*x)
        powers.append(row);rv.append([ww*hh])
    v=arb_mat(powers).transpose()*arb_mat(rv)
    hmom=[h+v[i,0]for i,h in enumerate(hmom)]
    if k%16==0:print('core h quadrature',k,len(panels),round(time.monotonic()-start,1),flush=True)
me=(2*a).sqrt()*c.mellin(0,a);scale=(2/a).sqrt()
intg=a*integrate_static(g,pp)[0]
alpha=(intg-hmom[0])*scale/me
ustatic={tag:p*(1/delta) for tag,p in g.items()}
ustatic[None]=ustatic.get(None,arb_poly([]))+phif-(plow+alpha*mc)*(1/delta)
upp=[p*(1/delta) for p in pp]
# On the outside, include the moment lift's core part in this same integral.
outerstatic=dict(ustatic);outerstatic[None]=outerstatic[None]-mc*(lm/mu)
um=integrate_static(outerstatic,upp,224)
physical_mom=[a**(k+1)*v-hmom[k]/delta for k,v in enumerate(um)]
outerreg=regular_out(physical_mom)
# The core moment correction is integrated analytically for all large old terms.
mqpsi=logmod.function_product(gpsi,{None:mc},mom,'zero','one')
uq=logmod.function_product(ustatic,qm,mom,'zero','one')
for (lo,hi),up,qp,gp in zip(cells,upp,qmp,pps):
    mqpsi+=mom.integral(gp*mc,lo,hi)
    uq+=logmod.function_product(ustatic,{None:qp},mom,lo,hi)
    uq+=logmod.function_product({None:up},qm,mom,lo,hi)+mom.integral(up*qp,lo,hi)
momentR=hm+a*mqpsi+a*uq-hq/delta
assert all(v.is_finite()for v in physical_mom) and momentR.is_finite()
print('Complete core moment and regular convolution ready',round(time.monotonic()-start,1),flush=True)
import model_cache
cache_names='a b hs mid half mu cc delta rootvalues roots cells edges ustatic outerstatic upp hpoints outerreg momentR sp spx slocal gamma convker fac harm zp pv lm channels J Y w ff low'.split()
cache_path=HERE/('whole-model-'+program_sha[:12]+'-n'+str(args.nodes)+'.json.gz')
model_cache.save(cache_path,{name:globals()[name]for name in cache_names},program_sha,
                 {name:hashlib.sha256(raw).hexdigest()for name,raw in env['inp'].data.items()})
print('Exact model cache saved',cache_path.name,flush=True)
# Cauchy integrals of polynomial/log expressions; no high-mode truncation.
logseq={tag:of.log_moments(root,600)for tag,root in rootvalues.items()}
def divide(p,s):
    if len(p)<2:return arb_poly([]),p[0]if len(p)else arb(0)
    out=[arb(0)]*(len(p)-1);out[-1]=p[len(p)-1]
    for k in range(len(p)-2,0,-1):out[k-1]=p[k]+s*out[k]
    return arb_poly(out),p[0]+s*out[0]
def ilog(s,r):
    d=r-s
    if d.contains(0):raise RuntimeError('Cauchy log diagonal needs separate formula')
    def real_dilog(z):
        if z>1:return arb.pi()**2/6-z.log()*(z-1).log()-acb(1-z).polylog(2).real
        return acb(z).polylog(2).real
    def primitive(v,at_root=False):
        li=arb.pi()**2/6 if at_root else real_dilog(-v/d)
        return abs(d).log()*abs(v).log()-li
    return primitive(s)-primitive(s-1,r==1)
def cauchy_static(s):
    total=arb(0)
    for tag,p in outerstatic.items():
        qq,ps=divide(p,s)
        if tag is None:total+=ps*abs(s/(s-1)).log()-c.pint(qq)
        else:total+=ps*ilog(s,rootvalues[tag])-sum((v*logseq[tag][k]for k,v in enumerate(qq)),arb(0))
    for pp,(lo,hi)in zip(upp,cells):
        qq,ps=divide(pp,s);ll,hh=roots[lo],roots[hi]
        total+=ps*abs((s-ll)/(s-hh)).log()-c.pint(qq,ll,hh)
    return total
# Local same-interval regular Gamma operator, including both parities of s.
sp_mom=[c.pint(sp*arb_poly([1,1])**k,arb(-1),arb(1))for k in range(225)]
ck=[];selfreg=arb_poly([])
for k in range(225):
    if k==0:pol=arb_poly([sp_mom[0]])
    else:
        rhs=sp*2 if k==1 else ck[k-2]*(k*(k-1))
        pol=rhs.integral().integral()
        slope=-k*sp_mom[k-1]-pol.derivative()(-1)
        pol+=arb_poly([sp_mom[k]-pol(-1)+slope,slope])
    ck.append(pol);selfreg+=pol*(half*gamma[k]*(half/2)**k)
shellmom=[c.pint(spx*arb_poly([0]*k+[1]),a,b)for k in range(225)]
co=convker*arb_poly([v/fac[k]for k,v in enumerate(shellmom)])
reflectreg=arb_poly([co[224-k]/fac[k]for k in range(225)])
dh=sum((leg[k]*(slocal[k,0]*(arb(2*k+1)/(2*hs)).sqrt()*harm[k])for k in range(96)),arb_poly([]))
def shell_cauchy(x):
    qq,rem=divide(spx,-x)
    return c.pint(qq,a,b)+rem*((x+b)/(x+a)).log()
zglobal=[]
for i,(pol,ls)in enumerate(zp):
    smooth=sum((leg[k]*(ls[k]*harm[k])for k in range(len(ls))),arb_poly([]))
    smooth+=pol*(-(2*arb.pi()*b).log()-arb.const_euler())-of.kernel(pol,ls,b,gamma,0)
    zglobal.append((pol,smooth,pv[i,0]))
def residual_core(x):
    idx=next(i for i in range(len(edges)-1)if edges[i]<=x<edges[i+1])
    t=x/a
    return evaluate(ustatic,t)+upp[idx](t)-hfun(res.cell(edges[idx],edges[idx+1]),x)/delta
def outer_value(x):
    u=(x-mid)/half;s=x/a
    base=hfun(res.cell(x-q('1e-50'),x+q('1e-50')),x)
    val=base+dh(u)+spx(x)*(-(2*arb.pi()).log()-arb.const_euler()-((x-a)*(b-x)).log()/2)
    val-=shell_cauchy(x)/2+selfreg(u)+reflectreg(x)
    # Complete outer action of the combined core source.
    singular=(cauchy_static(s)-cauchy_static(-s))/2
    for y,weighted_h in hpoints:singular-=weighted_h*(1/(x-y)+1/(x+y))/(2*delta)
    val-=singular+outerreg(x)
    for pol,smooth,factor in zglobal:
        zz=pol(x/b)
        value=smooth(x/b)-zz*((1-x/b)*(1+x/b)).log()/2
        for sh,wt in channels:
            for sign in (-1,1):
                y=x+sign*sh
                if abs(y)<b:value-=pol(y/b)*wt
        val+=factor*value
    for sh,wt in channels:
        for sign in (-1,1):
            y=x+sign*sh;ay=abs(y)
            if ay<a:val-=wt*(residual_core(ay)-lm/mu*res.m(ay))
            elif a<ay<b:val-=wt*spx(ay)
    return val-res.m(x)*momentR/mu
print('Whole function ready',round(time.monotonic()-start,1),flush=True)
samples=[]
for f in ('0.01','0.1','0.3','0.5','0.7','0.9','0.99'):
    x=a+hs*q(f);v=outer_value(x)
    assert v.is_finite()
    samples.append([f,c.enc(v)])
    print('POINT',f,v.str(16),flush=True)
(HERE/('whole-function-points-'+program_sha[:12]+'.json')).write_text(json.dumps({'status':'EXPLORATORY_NO_DIRECTED_REMAINDERS','samples':samples,'seconds':time.monotonic()-start},indent=2)+'\n')
