"""Directed scalar integration under the bound operator/source hypotheses.

Arb enclosures, exact polynomial/log moments for the frozen physical F_hat,
and Gauss-Legendre with an explicit Chebyshev-tail remainder on each cell.
"""
import json, gzip, os, sys, time, hashlib
from pathlib import Path
from fractions import Fraction
from flint import arb, acb, arb_poly, acb_poly, ctx

ctx.prec = 800
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PACKAGE = HERE.parent/'nstar-jp-spike-orthogonality-2026-10-16'
INPUTS = Path(os.environ['OBJEKT_X_STAGE5_INPUTS'])
OUT = Path(os.environ['OBJEKT_X_L00_OUTPUT'])
OUT.mkdir(parents=True, exist_ok=True)


def q(s):
    f=Fraction(s);return arb(f.numerator)/f.denominator
def box(v):return q(v[0]).union(q(v[1]))
def ub(x):return abs(x).upper()
def pad(x,e):return x+arb(0,ub(e))
def enc(x):return [str(x.lower().fmpq()),str(x.upper().fmpq())]
def dot(x,y):return sum((a*b for a,b in zip(x,y)),arb(0))
def norm(x):return dot(x,x).sqrt()
def load(p):return json.loads(p.read_bytes())
def abs_poly(p,s):return sum((ub(c)*s**k for k,c in enumerate(p)),arb(0))
def pint(p,s):return sum((c*s**(k+1)/(k+1) for k,c in enumerate(p)),arb(0))
def plogint(p,s):return sum((c*s**(k+1)*(s.log()/(k+1)-arb(1)/(k+1)**2) for k,c in enumerate(p)),arb(0))
def poly(p):return arb_poly(p)


class Poly:
    def __init__(self,p):self.r=arb_poly(p);self.c=acb_poly(self.r)
    def __call__(self,x):return self.c(x) if isinstance(x,acb) else self.r(x)


def legpolys(n):
    p=[poly([1]),poly([0,1])]
    for k in range(1,n-1):p.append(((2*k+1)*poly([0,1])*p[k]-k*p[k-1])*(arb(1)/(k+1)))
    return p[:n]


def main(par):
    assert par in ('even','odd')
    manifest=load(HERE/'INPUT_BINDINGS.json')
    for rel,digest in manifest['repository_files'].items():
        assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest,rel
    for rel,digest in manifest['prepared_inputs'].items():
        assert hashlib.sha256((INPUTS/rel).read_bytes()).hexdigest()==digest,rel
    sigma=0 if par=='even' else 1;eps=(-1)**sigma
    a8=3*arb(2).log()/2;a=arb(3).log();b=arb(11).log()/2;hs=a-a8
    mu8=(a8*eps+a8.sinh())/2;mu=(a*eps+arb(4)/3)/2
    def m(x):return (x/2).cosh() if sigma==0 else (x/2).sinh()
    L=2*((b/2).sinh()-(a/2).sinh()) if sigma==0 else 2*((b/2).cosh()-(a/2).cosh())
    B=1/(2*(b-a+L*L/mu)).sqrt();Ac=-B*L/mu
    funcs=load(INPUTS/'FUNCTIONS12.json')['parities'][par]['functions']
    fr=load(INPUTS/'FROZEN_RESPONSE12.json')['parities'][par]
    X=[[q(v) for v in row] for row in fr['X']]
    # Certified physical F_hat z0. Expand only smooth log and hyperbolic factors.
    s=b/a-1;order=120
    lp=poly([arb(0)]+[arb((-1)**(k+1))/(k*2**k) for k in range(1,order+1)])
    elog=(s/2)**(order+1)/((order+1)*(1-s/2))
    mc=[];fac=arb(1)
    for k in range(order+1):
        if k:fac*=a/(2*k)
        mk=(a/2).cosh() if (sigma+k)%2==0 else (a/2).sinh()
        mc.append(mk*fac)
    M=poly(mc)
    em=(b/2).exp()*(a*s/2)**(order+1)/arb.fac_ui(order+1)
    W=poly([1])+L/mu*M;ew=ub(L/mu)*em
    Wmax=1+ub(L/mu)*m(b)
    F=[]
    for fj in funcs:
        spec=fj['F'];P=poly(list(map(q,spec['polynomial'])))(poly([1,1]))
        Q=poly(list(map(q,spec['log_ratio_multiplier'])))(poly([1,1]))
        cm=q(spec['physical_W_moment_multiplier'])
        A=P+Q*(poly([arb(2).log()])+lp)+cm*M
        er=abs_poly(Q,s)*elog+ub(cm)*em
        approx=pint(A*W,s)-plogint(Q*W,s)
        err=s*er*Wmax+ew*s*(abs_poly(A,s)+abs_poly(Q,s)*(1-s.log()))
        F.append(2*B*a/(2*a).sqrt()*pad(approx,err))
    T=[dot(row,F) for row in X]
    print(par,'F/T certified',float(max(v.rad() for v in T)),flush=True)
    # Common fixed-coordinate data.
    fa=load(PACKAGE/'original/gpt2-stufe3-endliche-u8-antwort/expected/FINITE_ACTION.json')[par]['directions']['lower_Pv']
    c=[box(v) for v in fa['c_model']]
    psi=load(PACKAGE/'original/gpt1-stufe1-zertifikat/expected/PSI_CORRECTED.json')['data'][par]['directions']['lower_Pv']
    psiP=Poly([box(v) for v in psi['core_polynomial_scaled_x_over_a8_interval']])
    psiM=box(psi['core_m_multiplier_model_interval'])
    psish=[box(v) for v in psi['shell_model_coefficients_interval']]
    legs=legpolys(384)
    psiS=Poly(sum((v*((arb(2*n+1)/(2*hs)).sqrt())*legs[n] for n,v in enumerate(psish)),poly([])))
    # Mellin moments: positive spherical-Bessel series with a geometric tail.
    def moment(n):
        z=a8/2;t=z**n*2**n*arb.fac_ui(n)/arb.fac_ui(2*n+1);total=t
        for k in range(1,160):
            t*=z*z/(2*k*(2*n+2*k+1));total+=t
        ratio=z*z/(2*160*(2*n+321))
        return pad(total,ub(t)*ratio/(1-ratio))*arb(2*n+1).sqrt()
    base=moment(sigma);degs=list(range(sigma+2,sigma+383,2))
    betas=[moment(n)/base for n in degs]
    # The 12 physical F sources controlling the psi error.
    hb=load(INPUTS/'HALF_INVERSE_1536.json')
    directions=load(INPUTS/'DIRECTIONS.json')[par]['directions']['upper_v']
    Zt=list(map(q,directions['Zt_exact_rational']))
    jref=[box(x) for x in directions['Jt_local_orthonormal_Legendre_coefficients_interval']]
    blocks=[]
    for cand in hb['blocks']:
        Qm=[[box(v) for v in row] for row in cand['basis_Q_local_coefficients']]
        if all(dot(row,Zt).overlaps(ref) for row,ref in zip(Qm,jref)):blocks.append((cand,Qm))
    assert len(blocks)==1
    blk,Qm=blocks[0];Sm=[[q(v) for v in row] for row in blk['half_inverse_centre_rational_Q_coefficients']]
    Y=[]
    for j in range(8):
        coef=[sum((Qm[n][k]*Sm[k][j] for k in range(92)),arb(0)) for n in range(96)]
        Y.append(Poly(sum((v*(arb(2*n+1)/(2*hs)).sqrt()*legs[n] for n,v in enumerate(coef)),poly([]))))
    zdata=load(PACKAGE/'stufe1/PSI_DEFINITION.json')[par]
    # z sources are exact moment-null Legendre differences, using certified moments on a9.
    def mellin_a(n):
        z=a/2;t=z**n*2**n*arb.fac_ui(n)/arb.fac_ui(2*n+1);total=t
        for k in range(1,160):t*=z*z/(2*k*(2*n+2*k+1));total+=t
        ratio=z*z/(2*160*(2*n+321))
        return pad(total,ub(t)*ratio/(1-ratio))*arb(2*n+1).sqrt()
    bz=mellin_a(sigma)
    Z=[Poly((arb(2*n+1)/(2*a)).sqrt()*legs[n]-(mellin_a(n)/bz)*(arb(2*sigma+1)/(2*a)).sqrt()*legs[sigma]) for n in zdata['core_z_degrees']]
    logs={n:arb(n).log() for n in (2,3,4,5,7,8,9)}
    channels=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
    cuts=[a-logs[2],b-logs[2],b-a]+[logs[k]-a for k in (4,5,7,8)]+[logs[k]-b for k in (4,5,7,8)]+[2*a-b]
    cuts=sorted(cuts,key=float)
    edges=[arb(0)]+cuts+[a8]
    assert all(hi>lo for lo,hi in zip(edges[:-1],edges[1:]))
    Dpoly=sum((T[i]*poly(list(map(q,fj['D']['polynomial']))) for i,fj in enumerate(funcs)),poly([]))
    Dv=Poly(sum((T[i]*poly(list(map(q,fj['D']['V_multiplier']))) for i,fj in enumerate(funcs)),poly([])))
    Dm=sum((T[i]*q(fj['D']['moment_multiplier']) for i,fj in enumerate(funcs)),arb(0))
    def theta(r):
        v=(-r/2).exp();return v.atanh()+v.atan()
    def jp(r):return 3*arb(2).log()/2+arb.pi()/4-r-(1-(-2*r).exp()).log()/2
    def jm(r):
        v=(-r).exp();return arb(2).log()/2+arb.pi()/4-((1-v)/(1+v)).log()/2
    # All branches are selected on a cell; their analytic continuations define the ellipse bound.
    def cell_data(lo,hi):
        mid=(lo+hi)/2;terms=[];dp=arb_poly(Dpoly)
        for i,fj in enumerate(funcs):
            for t in fj['D']['shift_terms']:
                sh=logs[int(t['channel'])]/a
                dl,dh=(arb(0),1-sh) if int(t['translation_sign'])==1 else (max(arb(0),sh-1),arb(1))
                if dl<mid/a<dh:dp+=T[i]*poly(list(map(q,t['polynomial'])))
        for n,prime in channels:
            for sign in (-1,1):
                shift=sign*logs[n];y=mid+shift;weight=arb(prime).log()/arb(n).sqrt()
                if -a<y<a:terms.append((weight,shift,'core'))
                elif a<y<b:terms.append((weight,shift,'plus'))
                elif -b<y<-a:terms.append((weight,shift,'minus'))
        dp=Poly(dp)
        def primes(x):
            return sum((w*(Ac*m(x+sh) if kind=='core' else B*(1 if kind=='plus' else eps)) for w,sh,kind in terms),arb(0))
        def residual(x):
            ep=(x/2).exp()
            ms=(ep*(jp(a-x)+jm(a+x))+eps/ep*(jm(a-x)+jp(a+x)))/2
            ts=theta(a-x)-theta(b-x)+eps*(theta(a+x)-theta(b+x))
            ct=Ac*ms-B*ts-primes(x)
            dv=(dp(x/a)-Dv(x/a)*(1-(x/a)**2).log()/2+Dm*m(x))/(2*a).sqrt()
            return ct-dv
        return residual,dp,primes
    # rho=2 ellipse rectangle, semiaxes 5/4 and 3/4.
    def ellipse(lo,hi):
        d=(hi-lo)/2;center=(hi+lo)/2
        xx=acb(arb(center,ub(d)*5/4),arb(0,ub(d)*3/4))
        assert xx.real > -a and xx.real < a
        return xx
    # Chebyshev tail after degree 2n-1: error <= 8*d*M*rho^-2n/(1-rho^-1).
    def remainder(lo,hi,n,M):return 8*((hi-lo)/2)*M*arb(2)**(-2*n)/(1-arb(1)/2)
    nodes={n:[arb.legendre_p_root(n,k,weight=True) for k in range(n)] for n in (128,512)}
    accum=[arb(0)]* (5+191+4+8+8)
    # entries: int r*m, int r^2, int psi*r, int psi*m, int core r*m; then phi, z*r, Y*r, Y*m.
    core_r2=arb(0)
    for region,panels,n in [('core',list(zip(edges[:-1],edges[1:])),512),('shell',[(a-hs*arb(2)**(-k),a-hs*arb(2)**(-k-1)) for k in range(160)],128)]:
        for ix,(lo,hi) in enumerate(panels):
            r,_,_=cell_data(lo,hi);center=(lo+hi)/2;half=(hi-lo)/2
            def vals(x):
                rr=r(x);mm=m(x)
                pp=psiP(x/a8)+psiM*mm if region=='core' else psiS((2*x-a8-a)/hs)
                v=[rr*mm,rr*rr,pp*rr,pp*mm,rr*mm if region=='core' else arb(0)]
                if region=='core':
                    ps=[arb(1),x/a8]
                    for k in range(1,383):ps.append(((2*k+1)*(x/a8)*ps[k]-k*ps[k-1])/(k+1))
                    v.extend([rr*((arb(2*k+1)/(2*a8)).sqrt()*ps[k]-beta*(arb(2*sigma+1)/(2*a8)).sqrt()*ps[sigma]) for k,beta in zip(degs,betas)])
                else:v.extend([arb(0)]*191)
                v.extend([zz(x/a)*rr for zz in Z])
                y=[yy((2*x-a8-a)/hs) for yy in Y] if region=='shell' else [arb(0)]*8
                v.extend([yy*rr for yy in y]);v.extend([yy*mm for yy in y])
                return v
            total=[arb(0)]*len(accum)
            for z,w in nodes[n]:
                vv=vals(center+half*z)
                for i,value in enumerate(vv):total[i]+=half*w*value
            xx=ellipse(lo,hi);rr=r(xx);mm=m(xx)
            pp=psiP(xx/a8)+psiM*mm if region=='core' else psiS((2*xx-a8-a)/hs)
            bounds=[ub(rr*mm),ub(rr*rr),ub(pp*rr),ub(pp*mm),ub(rr*mm) if region=='core' else arb(0)]
            # Bounding polynomial values in the same ellipse rectangle is conservative.
            if region=='core':
                ps=[acb(1),xx/a8]
                for k in range(1,383):ps.append(((2*k+1)*(xx/a8)*ps[k]-k*ps[k-1])/(k+1))
                bounds.extend([ub(rr*((arb(2*k+1)/(2*a8)).sqrt()*ps[k]-beta*(arb(2*sigma+1)/(2*a8)).sqrt()*ps[sigma])) for k,beta in zip(degs,betas)])
            else:bounds.extend([arb(0)]*191)
            bounds.extend([ub(zz(xx/a)*rr) for zz in Z])
            yy=[yy((2*xx-a8-a)/hs) for yy in Y] if region=='shell' else [arb(0)]*8
            bounds.extend([ub(y*rr) for y in yy]);bounds.extend([ub(y*mm) for y in yy])
            total=[pad(v,remainder(lo,hi,n,M)) for v,M in zip(total,bounds)]
            assert all(v.is_finite() for v in total),(region,ix)
            accum=[x+y for x,y in zip(accum,total)]
            if region=='core':core_r2+=total[1]
            if ix%20==0:print(par,region,ix,'I-part radius',float(accum[2].rad()),flush=True)
    # Entire omitted endpoint: r=G(x) log(a-x)+H(x), 0<a-x<d.
    d=hs*arb(2)**(-160);xx=(a-d).union(a);tt=arb(0).union(d)
    _,dp,primes=cell_data(a-d,a)
    expx=(xx/2).exp()
    q2=(2*(-2*d).exp()).union(arb(2));q1=(-d).exp().union(arb(1));qh=((-d/2).exp()/2).union(arb(1)/2)
    jpr=3*arb(2).log()/2+arb.pi()/4-tt-q2.log()/2
    jmr=arb(2).log()/2+arb.pi()/4-q1.log()/2+(1+(-tt).exp()).log()/2
    thr=(1+(-tt/2).exp()).log()/2-qh.log()/2+(-tt/2).exp().atan()
    msreg=(expx*(jpr+jm(a+xx))+eps/expx*(jmr+jp(a+xx)))/2
    tsreg=thr-theta(b-xx)+eps*(theta(a+xx)-theta(b+xx))
    H=Ac*msreg-B*tsreg-primes(xx)-(dp(xx/a)-Dv(xx/a)*((a+xx).log()-2*a.log())/2+Dm*m(xx))/(2*a).sqrt()
    G=(B-Ac*m(xx))/2+Dv(xx/a)/(2*(2*a).sqrt())
    l1=d*(ub(H)+ub(G)*(1-d.log()))
    l2=2*d*(ub(H)**2+ub(G)**2*(d.log()**2-2*d.log()+2))
    pmax=ub(psiS((2*xx-a8-a)/hs));mmax=ub(m(xx))
    tail=[mmax*l1,l2,pmax*l1,pmax*mmax*d,arb(0)]+[arb(0)]*191
    tail.extend([ub(zz(xx/a))*l1 for zz in Z])
    yy=[ub(y((2*xx-a8-a)/hs)) for y in Y]
    tail.extend([y*l1 for y in yy]);tail.extend([y*mmax*d for y in yy])
    assert all(v.is_finite() for v in tail)
    accum=[pad(x,e) for x,e in zip(accum,tail)]
    mr,nr,pr,pm,mc=accum[:5]
    phih=[2*v for v in accum[5:196]]
    nh2=2*(nr-mr*mr/mu);nh82=2*(core_r2-mc*mc/mu8)
    assert nh2>0 and nh82>0
    nh,nh8=nh2.sqrt(),nh82.sqrt()
    I0=2*(pr-mr*pm/mu)-dot(c,phih)
    bf=[2*v for v in accum[196:200]]+[2*(v-lam*mc/mu8) for v,lam in zip(accum[200:208],accum[208:216])]
    common=json.loads(gzip.decompress((INPUTS/'stage3/inputs/REFINED_COMMON96.json.gz').read_bytes()))['cases'][sigma]
    C=[[arb(int(v))/int(common['inverse_congruence_denominator']) for v in row] for row in common['inverse_congruence_integer_matrix']]
    Cph=[dot(col,phih) for col in zip(*C)]
    cphnorm=norm(Cph)
    data=load(PACKAGE/'original/gpt2-stufe4-hochantwort/expected/COMPLETE_HIGH_RESPONSE.json')[par]['directions']['lower_Pv']
    coh=load(PACKAGE/'original/gpt2-kp-und-kohaerenter-transport/expected/COHERENT_TRANSPORT_INPUTS.json')['parities'][par]['directions']['p']
    assert psi['k_model_exact']==coh['fixed_k0_rational']
    assert 'psi_actual-psi_model=-F*(k_actual-k_model)' in psi['analytic_function_error_structure']
    metric=[[q(v) for v in row] for row in coh['metric_G_equals_eta_squared_K_inverse']]
    kpsi=dot(bf,[dot(row,bf) for row in metric]).sqrt()
    feat=q(data['finite_pairing_feature_error_multiplier'][1])/(1-q(common['rho'])).sqrt()*cphnorm
    feature_factor=cphnorm/(1-q(common['rho'])).sqrt()
    feat_fixed=q(fa['fixed_k_feature_error_bound'][1])*feature_factor
    feat_k=q(fa['k_change_feature_error_bound'][1])*feature_factor
    assert ub(feat_fixed+feat_k) <= ub(feat)+arb('1e-100')
    high=q(data['whole_physical_high_U8_part_norm_upper'][1])*nh8
    radius=ub(kpsi)+ub(feat)+ub(high)
    enclosure=pad(I0,radius)
    out={'status':'PASS_DIRECTED_UNDER_BOUND_OPERATOR_DOMAIN_AND_SOURCE_HYPOTHESES',
         'review_status':'AUTHOR_DERIVED_EXTERNAL_REVIEW_OPEN',
         'model_scope':'h=(C_p-Dhat X_fix Fhat)z0; actual k; no N12 energy conclusion',
         'parity':par,'I0':enc(I0),'L00':enc(enclosure),'norm_h':enc(nh),'norm_h8':enc(nh8),
         'Cstar_Phi_star_h8_norm':enc(cphnorm),'psi_k_coherent_error':enc(kpsi),'finite_response_feature_error':enc(feat),
         'finite_response_fixed_k_error':enc(feat_fixed),'finite_response_k_change_error':enc(feat_k),
         'I0_all_coefficient_roundoff_and_integration_radius':enc(I0.rad()),
         'high_remainder_bound_using_h8':enc(high),'radius_without_I0_width':enc(radius),
         'Fhat_z0':[enc(v) for v in F],'Tz0':[enc(v) for v in T],'b_F':[enc(v) for v in bf],
         'Phi_star_h8':[enc(v) for v in phih], 'core_moment':enc(mc),'whole_moment':enc(mr),
         'tail_integral_abs_r':enc(l1),'tail_integral_r_squared':enc(l2),
         'precision_bits':ctx.prec,'core_gauss_nodes':512,'shell_gauss_nodes':128,'shell_dyadic_panels':160}
    simple=('-407.736','401.497') if par=='even' else ('-2.646','11.832')
    threshold=q('980.113997' if par=='even' else '398.766496')
    assert enclosure > q(simple[0]) and enclosure < q(simple[1])
    assert max(abs(q(simple[0])),abs(q(simple[1])))<threshold
    assert I0.rad()<q('1e-12')
    out['outward_decimal_L00']=list(simple)
    out['exclusion_threshold']=str(threshold.mid().fmpq())
    out['scalar_test_outcome']='NO_EXCLUSION_BY_Z0_WITH_THE_BOUND_SCALAR_CRITERION'
    (OUT/f'L00_CERTIFICATE_{par}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(par,'I0',I0,'budget',kpsi,feat,high,'L00',enclosure,flush=True)


if __name__=='__main__':main(sys.argv[1])
