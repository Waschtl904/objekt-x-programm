"""Exploratory analytic Taylor integration, with separate contour bounds.

This controls the stored quadrature MODEL only. Core quadrature and mathematical
source errors must additionally be paid before any complete comparison claim.
"""
from flint import arb,acb,arb_poly,acb_poly,arb_series,ctx
import math,time

class Jet:
    N=1024
    def __init__(self,s,b=None):
        self.s=s if isinstance(s,arb_series)else arb_series([s],prec=self.N)
        self.b=acb(s)if b is None else b
    def __add__(self,o):
        o=jet(o);return Jet(self.s+o.s,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Jet(-self.s,-self.b)
    def __sub__(self,o):return self+-jet(o)
    def __rsub__(self,o):return jet(o)+-self
    def __mul__(self,o):
        o=jet(o);return Jet(self.s*o.s,self.b*o.b)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=jet(o);assert not o.b.contains(0),'Contour denominator'
        return Jet(self.s/o.s,self.b/o.b)
    def __rtruediv__(self,o):return jet(o)/self
    def exp(self):return Jet(self.s.exp(),self.b.exp())
    def log(self):
        assert self.b.real>0,'Log contour must be in right half plane'
        return Jet(self.s.log(),self.b.log())

def jet(x):return x if isinstance(x,Jet)else Jet(x)
def lg(x):
    x=jet(x)
    return x.log()if x.s[0]>0 else(-x).log()

def peval(p,x):
    x=jet(x);assert x.s.length()<=2,'Affine polynomial argument required'
    co=p(arb_poly([x.s[0],x.s[1]]))
    # Recenter before taking a rectangle enclosure, preserving the polynomial.
    bound=arb_poly([abs(v).upper()for v in co])(2).upper()
    return Jet(arb_series(list(co)[:Jet.N],prec=Jet.N),acb(arb(0,bound),arb(0,bound)))

def dilog_real(z):
    c=z[0]
    val=arb.pi()**2/6-c.log()*(c-1).log()-acb(1-c).polylog(2).real if c>1 else acb(c).polylog(2).real
    one=1-z
    assert not c.contains(0)and not one[0].contains(0)
    sign=1 if one[0]>0 else-1
    ds=-(one*sign).log()*z.derivative()/z
    return ds.integral()+val

def ilog(s,r):
    ss=s.s
    lratio=lg(s).s-lg(s-1).s
    if r==1:
        derivative=lratio/(ss-1)
    else:
        lr=abs(r).log();l1r=abs(1-r).log()
        derivative=-l1r/(ss-1)+lr/ss+(l1r-lr+lratio)/(ss-r)
    out=(derivative*ss[1]).integral()+BASE_ILOG(ss[0],r)
    gap=s.b.real.lower()-1 if s.b.real>1 else -s.b.real.upper()
    assert gap>0,'Cauchy contour intersects core'
    # Each of the four fixed roots is +/-1 or +/-a9/a8; the integral of
    # |log|u-root|| on [0,1] is below 10. This bounds the analytic Cauchy integral.
    M=10/gap
    return Jet(out,acb(arb(0,M.upper()),arb(0,M.upper())))

def hjet(ns,x):
    res=ns['res'];model=ns['_scalar_model']
    fun=res.cell(x.s[0],x.s[0]);cell=model['records'][fun]
    a,b=res.a,res.b
    def moment(t):
        ep=(t/2).exp();return(ep+1/ep)/2
    def jp(t):return 3*arb(2).log()/2+arb.pi()/4-t-(1-(-2*t).exp()).log()/2
    def jm(t):
        v=(-t).exp();return arb(2).log()/2+arb.pi()/4-((1-v).log()-(1+v).log())/2
    ep=(x/2).exp();ms=(ep*(jp(a-x)+jm(a+x))+1/ep*(jm(a-x)+jp(a+x)))/2
    logm=(b-x).log()-(a-x).log();logp=(b+x).log()-(a+x).log()
    vlog=-((a-x).log()+(a+x).log()-2*a.log())/2
    shell=(peval(model['ell'],x)*logm+peval(model['quot'],x)+peval(model['ell'],-x)*logp+peval(model['quot'],-x))/2+peval(model['gamma'],x)
    prime=jet(0)
    for wt,sh,kind in cell['terms']:
        v=model['ac']*moment(x+sh)if kind=='core'else peval(model['ell'],x+sh)if kind=='plus'else peval(model['ell'],-x-sh)
        prime+=wt*v
    return model['ac']*ms-shell-prime-(peval(cell['dp'],x/a)+peval(model['dv'],x/a)*vlog+model['dm']*moment(x))/(2*a).sqrt()

def build(ns,lo,hi,N=1024):
    global BASE_ILOG
    BASE_ILOG=ns['ilog']
    Jet.N=N;ctx.cap=N
    mid=(lo+hi)/2;half=(hi-lo)/2
    # Circle radius two, enclosed by this square. All expressions are bounds
    # for the analytic continuation of the selected fixed prime cell.
    x=Jet(arb_series([mid,half],prec=N),acb(arb(mid,2*half.upper()),arb(0,2*half.upper())))
    a,b=ns['a'],ns['b'];s=x/a;u=(x-ns['mid'])/ns['half']
    c=ns['c'];delta=ns['delta'];mu=ns['mu'];roots=ns['roots']
    def cauchy(z):
        ans=-peval(ns['_fast']['cauchy_correction'],z)
        for tag,p in ns['outerstatic'].items():
            ans+=peval(p,z)*((lg(z)-lg(z-1))if tag is None else ilog(z,ns['rootvalues'][tag]))
        for p,(ll,hh)in zip(ns['upp'],ns['cells']):ans+=peval(p,z)*(lg(z-roots[ll])-lg(z-roots[hh]))
        return ans
    val=hjet(ns,x)+peval(ns['dh'],u)+peval(ns['spx'],x)*(-(2*arb.pi()).log()-arb.const_euler()-((x-a).log()+(b-x).log())/2)
    shellc=peval(ns['_fast']['shell_cauchy_correction'],-x)+peval(ns['spx'],-x)*((x+b).log()-(x+a).log())
    val-=shellc/2+peval(ns['selfreg'],u)+peval(ns['reflectreg'],x)
    singular=(cauchy(s)-cauchy(-s))/2
    # Taylor-expand the finite core Gauss measure to just the order needed
    # for 1e-35 uniform error. Its omitted series is paid separately.
    series=[arb(0)]*N;measure_ball=acb(0);measure_error=arb(0)
    for y,wh in ns['hpoints']:
        for shift in(-y,y):
            den=mid+shift;ratio=abs(half/den).upper();assert ratio<1
            bound=abs(wh/den).upper()
            nn=min(N,max(1,math.ceil(float((arb('1e-40')*(1-ratio)/(bound+arb('1e-100'))).log()/ratio.log()))))
            term=wh/den
            for k in range(nn):series[k]+=term;term*=-half/den
            measure_error+=bound*ratio**nn/(1-ratio)
            measure_ball+=wh/(x.b+shift)
    measure=Jet(arb_series(series,prec=N),measure_ball)
    singular-=measure/(2*delta)
    val-=singular+peval(ns['outerreg'],x)
    for pol,smooth,factor in ns['zglobal']:
        zz=peval(pol,x/b)
        vv=peval(smooth,x/b)-zz*((1-x/b).log()+(1+x/b).log())/2
        for sh,wt in ns['channels']:
            for sign in(-1,1):
                if abs(mid+sign*sh)<b:vv-=peval(pol,(x+sign*sh)/b)*wt
        val+=factor*vv
    def core(xx):
        idx=next(i for i in range(len(ns['edges'])-1)if ns['edges'][i]<=xx.s[0]<ns['edges'][i+1])
        t=xx/a
        vv=peval(ns['ustatic'][None],t)+peval(ns['upp'][idx],t)
        for tag,p in ns['ustatic'].items():
            if tag is not None:vv+=peval(p,t)*lg(t-ns['rootvalues'][tag])
        return vv-hjet(ns,xx)/delta
    def moment(xx):
        ep=(xx/2).exp();return(ep+1/ep)/2
    for sh,wt in ns['channels']:
        for sign in(-1,1):
            yy=x+sign*sh;ay=yy if yy.s[0]>=0 else-yy
            if ay.s[0]<a:val-=wt*(core(ay)-ns['lm']/mu*moment(ay))
            elif a<ay.s[0]<b:val-=wt*peval(ns['spx'],ay)
    val-=moment(x)*ns['momentR']/mu
    assert val.b.is_finite()and val.s.prec>=N-1
    # Derivatives in dilog cost at most one coefficient; retain that actual order.
    n=val.s.prec
    M=abs(val.b).upper()
    remainder=M*arb(2)**(1-n)+measure_error/(2*delta)
    polynomial=arb_poly(list(val.s))
    integral=2*half*c.pint(polynomial*polynomial,arb(-1),arb(1))
    assert integral.upper()>=0
    upper_norm=integral.upper().sqrt()+(4*half).sqrt()*remainder
    return dict(polynomial=polynomial,contour_bound=M,taylor_error=remainder,
                model_Xnorm_squared_upper=upper_norm**2,series_integral=integral,order=n)
