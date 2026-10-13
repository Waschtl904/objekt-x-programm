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
