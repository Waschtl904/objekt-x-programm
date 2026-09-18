#!/usr/bin/env python3
from fractions import Fraction as F
import sys, json
from pathlib import Path
from functools import lru_cache
sys.set_int_max_str_digits(1000000)
checks=[]
def ok(name,cond,val=None):
    if not cond: raise AssertionError(f'{name}: {val!r}')
    checks.append(name)

@lru_cache(maxsize=None)
def exp_neg_iv(x,N=24):
    s=F(0); term=F(1); vals=[]
    for k in range(N+1):
        if k==0: term=F(1)
        else: term*=x/F(k)
        s += term if k%2==0 else -term
        vals.append(s)
    return (vals[N-1],vals[N]) if N%2==0 else (vals[N],vals[N-1])

@lru_cache(maxsize=None)
def atanh_iv(t,N=24):
    s=F(0)
    for n in range(N): s += t**(2*n+1)/F(2*n+1)
    tail=t**(2*N+1)/F(2*N+1)/(1-t*t)
    return s,s+tail

@lru_cache(maxsize=None)
def log2_iv(N=24):
    a,b=atanh_iv(F(1,3),N); return 2*a,2*b

@lru_cache(maxsize=None)
def log_iv(x,N=24):
    assert x>0
    k=0;y=x
    while y>=2: y/=2;k+=1
    while y<1: y*=2;k-=1
    q=(y-1)/(y+1);a,b=atanh_iv(q,N); lylo,lyhi=2*a,2*b; l2lo,l2hi=log2_iv(N)
    if k>=0: return lylo+k*l2lo,lyhi+k*l2hi
    return lylo+k*l2hi,lyhi+k*l2lo

@lru_cache(maxsize=None)
def atan_iv(x,N=14):
    s=F(0); vals=[]
    for n in range(N):
        s += (-1)**n*x**(2*n+1)/F(2*n+1); vals.append(s)
    return min(vals[-1],vals[-2]),max(vals[-1],vals[-2])

@lru_cache(maxsize=None)
def pi_iv():
    a1,b1=atan_iv(F(1,5),18); a2,b2=atan_iv(F(1,239),8)
    return 16*a1-4*b2,16*b1-4*a2

@lru_cache(maxsize=None)
def harmonic(n): return sum((F(1,k) for k in range(1,n+1)),F(0))
@lru_cache(maxsize=None)
def gamma_iv(n=50):
    lnlo,lnhi=log_iv(F(n));
    lo=harmonic(n)-lnhi-F(1,2*n)+F(1,12*n*n)-F(1,120*n**4)
    hi=harmonic(n)-lnlo-F(1,2*n)+F(1,12*n*n)-F(1,120*n**4)+F(1,252*n**6)
    return lo,hi

@lru_cache(maxsize=None)
def H_iv(s):
    qlo,qhi=exp_neg_iv(s/2)
    rlo=(1+qlo)/(1-qlo); rhi=(1+qhi)/(1-qhi)
    llo,_=log_iv(rlo); _,lhi=log_iv(rhi)
    pilo,pihi=pi_iv()
    tlo=(1-qhi)/(1+qhi); thi=(1-qlo)/(1+qlo)
    alo,_=atan_iv(tlo,14); _,ahi=atan_iv(thi,14)
    return llo/2+pilo/4-ahi,lhi/2+pihi/4-alo

@lru_cache(maxsize=None)
def H_arg_iv(slo,shi):
    lo,_=H_iv(shi); _,hi=H_iv(slo); return lo,hi

@lru_cache(maxsize=None)
def h_iv(t):
    qlo,qhi=exp_neg_iv(t/2); rlo,rhi=exp_neg_iv(2*t)
    return qlo/(1-rlo), qhi/(1-rhi)

@lru_cache(maxsize=None)
def kappa_iv():
    pilo,pihi=pi_iv(); glo,ghi=gamma_iv()
    llo,_=log_iv(8*pilo); _,lhi=log_iv(8*pihi)
    return llo+glo+pilo/2,lhi+ghi+pihi/2

ELL_LO,ELL_HI=log2_iv(); KLO,KHI=kappa_iv()
SQ_LO=F(1414213562373095,10**15); SQ_HI=F(1414213562373096,10**15)
assert SQ_LO*SQ_LO<2<SQ_HI*SQ_HI
W_LO=ELL_LO/SQ_HI; W_HI=ELL_HI/SQ_LO
HELL_LO,HELL_HI=H_arg_iv(ELL_LO,ELL_HI)

def ppoly(z): return F(1)-F(9,4)*z**5+F(5,2)*z**3-F(5,4)*z

def beta_e(a):
    z=a/2; r=z*z/(2*(1-z*z/F(12))); return r*r

def beta_o(a):
    z=a/2; r=z*z/(6*(1-z*z/F(20))); return r*r

@lru_cache(maxsize=None)
def pars(a):
    d_lo=2*a-ELL_HI; d_hi=2*a-ELL_LO
    Hd_lo,Hd_hi=H_arg_iv(d_lo,d_hi)
    C_lo=KLO+W_LO-Hd_hi-HELL_HI
    C_hi=KHI+W_HI-Hd_lo-HELL_LO
    s1lo=a+ELL_LO/2; s1hi=a+ELL_HI/2
    s2lo=a-ELL_HI/2; s2hi=a-ELL_LO/2
    H1lo,H1hi=H_arg_iv(s1lo,s1hi); H2lo,H2hi=H_arg_iv(s2lo,s2hi)
    m_lo=H1lo+H2lo-Hd_hi-HELL_HI
    m_hi=H1hi+H2hi-Hd_lo-HELL_LO
    zlo=ELL_LO/(2*a); zhi=ELL_HI/(2*a)
    p_lo=ppoly(zhi); p_hi=ppoly(zlo)
    hlo,hhi=h_iv(2*a)
    lam_lo=F(1)+2*a*hlo-C_hi; lam_hi=F(1)+2*a*hhi-C_lo
    dl_lo=lam_lo+F(7,12); dl_hi=lam_hi+F(7,12)
    return {'C':(C_lo,C_hi),'m':(m_lo,m_hi),'p':(p_lo,p_hi),'lam':(lam_lo,lam_hi),'d':(dl_lo,dl_hi),'be':beta_e(a),'bo':beta_o(a)}

# --- compact rigorous interval layer ---
DROUND=10**28
def floorq(x): return F(x.numerator*DROUND//x.denominator,DROUND)
def ceilq(x): return F(-((-x.numerator*DROUND)//x.denominator),DROUND)
def compact_pars(q):
    out={}
    for k in ('C','m','p','lam','d'):
        out[k]=(floorq(q[k][0]),ceilq(q[k][1]))
    out['be']=ceilq(q['be']); out['bo']=ceilq(q['bo'])
    return out

def iadd(x,y): return (x[0]+y[0],x[1]+y[1])
def ineg(x): return (-x[1],-x[0])
def isub(x,y): return iadd(x,ineg(y))
def imul(x,y):
    v=(x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1]); return min(v),max(v)
def iinv(x):
    assert x[0]>0 or x[1]<0
    v=(1/x[0],1/x[1]); return min(v),max(v)
def idiv(x,y): return imul(x,iinv(y))
def isq(x):
    if x[0]>=0: return x[0]*x[0],x[1]*x[1]
    if x[1]<=0: return x[1]*x[1],x[0]*x[0]
    return F(0),max(x[0]*x[0],x[1]*x[1])
def icube(x): return imul(isq(x),x)
def isc(c,x): return imul((c,c),x)

def h_arg_iv(tlo,thi):
    lo,_=h_iv(thi); _,hi=h_iv(tlo); return floorq(lo),ceilq(hi)
def hprime_arg_iv(tlo,thi):
    # h'(t)=-q(1+3r)/(2(1-r)^2), q=e^-t/2, r=e^-2t
    qlo,_=exp_neg_iv(thi/2); _,qhi=exp_neg_iv(tlo/2)
    rlo,_=exp_neg_iv(2*thi); _,rhi=exp_neg_iv(2*tlo)
    q=(floorq(qlo),ceilq(qhi)); r=(floorq(rlo),ceilq(rhi))
    return ineg(idiv(imul(q,iadd((F(1),F(1)),isc(F(3),r))),isc(F(2),isq(isub((F(1),F(1)),r)))))

def fixed_gap_lower(q,t):
    Clo,Chi=q['C'];mlo,mhi=q['m'];plo,phi=q['p'];llo,lhi=q['lam'];dlo,dhi=q['d'];b=q['be']
    mulo=t*mlo;muhi=t*mhi
    Slo=llo+mulo*plo*(1-muhi/dlo)
    eta=Slo/(1+muhi/dlo)**2
    loss=Chi+t/(1-t)*mhi
    return (eta-loss*b)/(1+b)

def concavity_lower(q):
    mlo,mhi=q['m'];plo,phi=q['p'];llo,lhi=q['lam'];dlo,dhi=q['d']
    return plo-phi*mhi/dlo+(-lhi)/dhi

def deriv_theta_iv(q,t):
    mlo,mhi=q['m'];plo,phi=q['p'];llo,lhi=q['lam'];dlo,dhi=q['d'];b=q['be']
    mulo=t*mlo;muhi=t*mhi
    Nlo=plo-3*phi*muhi/dlo+(-2*lhi)/dhi
    Nhi=phi-3*plo*mulo/dhi+(-2*llo)/dlo
    qlo=1+mulo/dhi;qhi=1+muhi/dlo
    # dPhi/dmu; sign is same as d/dtheta since m>0
    pen=b/(1-t)**2
    return Nlo/qhi**3-pen,Nhi/qlo**3-pen

def optimized_gap_upper_bracket(q,t0,t1):
    Clo,Chi=q['C'];mlo,mhi=q['m'];plo,phi=q['p'];llo,lhi=q['lam'];dlo,dhi=q['d'];b=q['be']
    mulo=t0*mlo;muhi=t1*mhi
    Shi=lhi+phi*muhi-plo*mulo*mulo/dhi
    eta=Shi/(1+mulo/dhi)**2
    loss=Clo+t0/(1-t0)*mlo
    return (eta-loss*b)/(1+b)

def odd_gap_lower(q):
    llo,lhi=q['lam']; b=q['bo']
    return ((llo+F(1,3))-(F(1,2)-llo)*b)/(1+b)

# Whole-interval derivative of the fixed-theta even gap.
def fixed_gap_derivative_interval(a0,a1,t,q0,q1):
    # Proven monotonic component ranges on this narrow interval:
    # C increases; m decreases; p increases; lambda and delta decrease; beta_e increases.
    C=(floorq(q0['C'][0]),ceilq(q1['C'][1]))
    m=(floorq(q1['m'][0]),ceilq(q0['m'][1]))
    p=(floorq(q0['p'][0]),ceilq(q1['p'][1]))
    lam=(floorq(q1['lam'][0]),ceilq(q0['lam'][1]))
    d=(floorq(q1['d'][0]),ceilq(q0['d'][1]))
    b=(floorq(beta_e(a0)),ceilq(beta_e(a1)))
    # C'=2h(2a-ell)
    darg=(2*a0-ELL_HI,2*a1-ELL_LO)
    Cp=isc(F(2),h_arg_iv(*darg))
    # m'=-h(a+ell/2)-h(a-ell/2)+2h(2a-ell)
    s1=(a0+ELL_LO/2,a1+ELL_HI/2); s2=(a0-ELL_HI/2,a1-ELL_LO/2)
    mp=iadd(iadd(ineg(h_arg_iv(*s1)),ineg(h_arg_iv(*s2))),isc(F(2),h_arg_iv(*darg)))
    # p'=(5/4)(3z^2-1)^2 z/a, z=ell/(2a)
    z=(floorq(ELL_LO/(2*a1)),ceilq(ELL_HI/(2*a0)))
    pp=isc(F(5,4),imul(isq(isub(isc(F(3),isq(z)),(F(1),F(1)))),idiv(z,(a0,a1))))
    # lambda'=2h(2a)+4a h'(2a)-C'
    lp=isub(iadd(isc(F(2),h_arg_iv(2*a0,2*a1)),isc(F(4),imul((a0,a1),hprime_arg_iv(2*a0,2*a1)))),Cp)
    # beta_e'=q*z/(1-z^2/12)^2, z=a/2, q=z^2/[2(1-z^2/12)]
    za=(a0/2,a1/2); den=isub((F(1),F(1)),isc(F(1,12),isq(za)))
    qq=idiv(isq(za),isc(F(2),den)); bp=idiv(imul(qq,za),isq(den))
    # Verify the monotonicities used above directly on this interval.
    ok('m decreases on [0.392,a_lo]',mp[1]<0,mp)
    ok('lambda/delta decrease on [0.392,a_lo]',lp[1]<0,lp)
    mu=isc(t,m); mup=isc(t,mp); one=(F(1),F(1)); mud=idiv(mu,d)
    S=iadd(lam,imul(imul(p,mu),isub(one,mud)))
    Sp=lp
    Sp=iadd(Sp,imul(imul(pp,mu),isub(one,mud)))
    Sp=iadd(Sp,imul(imul(p,mup),isub(one,isc(F(2),mud))))
    Sp=iadd(Sp,idiv(imul(imul(p,isq(mu)),lp),isq(d)))
    rr=iadd(one,mud); rp=isub(idiv(mup,d),idiv(imul(mu,lp),isq(d)))
    E=idiv(S,isq(rr)); Ep=isub(idiv(Sp,isq(rr)),idiv(isc(F(2),imul(S,rp)),icube(rr)))
    k=t/(1-t); M=iadd(C,isc(k,m)); Mp=iadd(Cp,isc(k,mp))
    N=isub(E,imul(b,M)); Np=isub(isub(Ep,imul(bp,M)),imul(b,Mp))
    return idiv(isub(imul(Np,iadd(one,b)),imul(N,bp)),isq(iadd(one,b)))

a0=F(49,125)
a_lo=F(3930108,10_000_000)
a_hi=F(3930109,10_000_000)
tfix=F(79142,100000)
t0=F(791425,1_000_000); t1=F(791426,1_000_000)

# Raw rigorous transcendental intervals are immediately rounded OUTWARD to denominator 1e28.
q0raw=pars(a0); qloraw=pars(a_lo); qhiraw=pars(a_hi)
q0=compact_pars(q0raw); qlo=compact_pars(qloraw); qhi=compact_pars(qhiraw)

lo_gap=fixed_gap_lower(qlo,tfix)
ok('fixed theta gap positive at a_lo',lo_gap>0,lo_gap)
Sfixed_hi=q0['lam'][1] + qlo['p'][1]*(tfix*q0['m'][1])
ok('fixed-theta Schur scalar stays below delta on interval',Sfixed_hi<qlo['d'][0],Sfixed_hi)
Gp=fixed_gap_derivative_interval(a0,a_lo,tfix,q0raw,qloraw)
ok('fixed theta gap strictly decreases on [0.392,a_lo]',Gp[1]<0,Gp)

# Therefore G_node >= G_theta >0 throughout [0.392,a_lo].
qconc=concavity_lower(qhi)
ok('upper-end optimizer objective strictly concave',qconc>0,qconc)
ok('upper-end even tail delta >1/2',qhi['d'][0]>F(1,2),qhi['d'])
# S(mu)<delta for all 0<=mu<=m: S<=lambda+p*delta/4.
Smax=qhi['lam'][1]+qhi['p'][1]*qhi['d'][1]/4
ok('upper-end Schur scalar stays below delta',Smax<qhi['d'][0],Smax)
d0=deriv_theta_iv(qhi,t0); d1=deriv_theta_iv(qhi,t1)
ok('optimizer derivative positive at theta lower bracket',d0[0]>0,d0)
ok('optimizer derivative negative at theta upper bracket',d1[1]<0,d1)
up_gap=optimized_gap_upper_bracket(qhi,t0,t1)
ok('global optimized even gap negative at a_hi',up_gap<0,up_gap)
odd=odd_gap_lower(qhi)
ok('odd gap at a_hi remains >1/4',odd>F(1,4),odd)

# Prime 3 is still inactive: 2*a_hi<4/5<1<log 3 (e<3).
ok('2a_hi < 4/5',2*a_hi<F(4,5),2*a_hi)

results={
 'architecture_domain_start':str(a0),
 'first_failure_lower':str(a_lo),
 'first_failure_upper':str(a_hi),
 'fixed_theta':str(tfix),
 'fixed_theta_gap_at_lower_decimal':f'{float(lo_gap):.18g}',
 'fixed_theta_derivative_lower_decimal':f'{float(Gp[0]):.18g}',
 'fixed_theta_derivative_upper_decimal':f'{float(Gp[1]):.18g}',
 'theta_optimizer_lower':str(t0),
 'theta_optimizer_upper':str(t1),
 'optimizer_derivative_at_lower_lower_decimal':f'{float(d0[0]):.18g}',
 'optimizer_derivative_at_lower_upper_decimal':f'{float(d0[1]):.18g}',
 'optimizer_derivative_at_upper_lower_decimal':f'{float(d1[0]):.18g}',
 'optimizer_derivative_at_upper_upper_decimal':f'{float(d1[1]):.18g}',
 'concavity_margin_decimal':f'{float(qconc):.18g}',
 'optimized_gap_upper_decimal':f'{float(up_gap):.18g}',
 'odd_gap_lower_decimal':f'{float(odd):.18g}',
 'checks':len(checks),
}
Path('node_schur_waxing_results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
for name in checks: print('PASS',name)
print('TOTAL',len(checks))
