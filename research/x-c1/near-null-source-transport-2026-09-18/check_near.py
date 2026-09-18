#!/usr/bin/env python3
"""Exact near-null source reconstruction and finite-channel transport audit.

All proof decisions and displayed enclosures use integer/Fraction arithmetic.
The analytic domain and the meaning of the interval covers are in PROOF.md.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

SCALE = 10**220
TERMS = 384


def down(x):
    x = F(x)
    return F((x.numerator * SCALE) // x.denominator, SCALE)


def up(x):
    return -down(-F(x))


class I:
    """Directed intervals stored as integer multiples of 1/SCALE."""
    def __init__(self,lo,hi=None):
        low=F(lo);high=low if hi is None else F(hi)
        self._lo=(low.numerator*SCALE)//low.denominator
        self._hi=-((-high.numerator*SCALE)//high.denominator)
        assert self._lo<=self._hi
    @classmethod
    def raw(cls,lo,hi):
        obj=cls.__new__(cls);obj._lo=lo;obj._hi=hi
        assert lo<=hi
        return obj
    @property
    def lo(self):return F(self._lo,SCALE)
    @property
    def hi(self):return F(self._hi,SCALE)
    @staticmethod
    def of(x):return x if isinstance(x,I) else I(x)
    def __add__(self,other):
        o=I.of(other);return I.raw(self._lo+o._lo,self._hi+o._hi)
    __radd__=__add__
    def __neg__(self):return I.raw(-self._hi,-self._lo)
    def __sub__(self,other):return self+(-I.of(other))
    def __rsub__(self,other):return I.of(other)+(-self)
    def __mul__(self,other):
        o=I.of(other)
        v=[self._lo*o._lo,self._lo*o._hi,self._hi*o._lo,self._hi*o._hi]
        return I.raw(min(v)//SCALE,-((-max(v))//SCALE))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=I.of(other);assert o._lo>0 or o._hi<0
        inv=I.raw(SCALE*SCALE//o._hi,-((-SCALE*SCALE)//o._lo))
        return self*inv
    def __rtruediv__(self,other):return I.of(other)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        v=I(1)
        for _ in range(n):v=v*self
        return v


def exp_pos(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= 4
    term = total = I(1)
    for k in range(1, TERMS+1):
        term = term*x/k
        total = total+term
    following = term*x/(TERMS+1)
    tail = following/(1-x/(TERMS+2))
    return total + I(0, tail.hi)


def atanh(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= F(1, 2)
    term = x
    total = I(0)
    for k in range(TERMS):
        total = total + term/(2*k+1)
        term = term*x*x
    tail = term/((2*TERMS+1)*(1-x*x))
    return total + I(0, tail.hi)


LOG2 = 2*atanh(I(F(1, 3)))


def log_point(x):
    assert x > 0
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1
    return 2*atanh(I((x-1)/(x+1))) + k*LOG2


def log(x):
    x = I.of(x)
    return I(log_point(x.lo).lo, log_point(x.hi).hi)


def atan(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= F(1, 2)
    term = x
    total = I(0)
    for k in range(TERMS):
        total = total + ((-1)**k)*term/(2*k+1)
        term = term*x*x
    # 256 terms end negative; the next positive term bounds the remainder.
    return total + I(0, (term/(2*TERMS+1)).hi)


PI = 16*atan(I(F(1, 5))) - 4*atan(I(F(1, 239)))


def gamma():
    # Euler-Maclaurin through B16; bound the periodic polynomial by
    # its coefficient l1 norm on [0,1]. Integral remainder C/(16 N^16).
    from math import comb
    bs=[F(1)]
    for n in range(1,17):
        bs.append(-sum((F(comb(n+1,k))*bs[k] for k in range(n)),F(0))/(n+1))
    n=10000
    harmonic=sum((I(F(1,k)) for k in range(1,n+1)),I(0))
    center=harmonic-log(I(n))-F(1,2*n)
    for k in range(1,9):center+=bs[2*k]/(2*k*n**(2*k))
    radius=sum((abs(comb(16,k)*bs[k]) for k in range(17)),F(0))/(16*n**16)
    return center+I(-radius,radius)


from math import factorial, comb, isqrt
from functools import lru_cache

def polyadd(p,q):
    return [(p[k] if k<len(p) else F(0))+(q[k] if k<len(q) else F(0)) for k in range(max(len(p),len(q)))]

def polymul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return r

def polyval(p,x):
    v=I(0)
    for c in reversed(p):v=v*x+c
    return v

def integral(p):return sum((p[k]/(k+1) for k in range(0,len(p),2)),F(0))

@lru_cache(None)
def leg(n):
    if n==0:return [F(1)]
    if n==1:return [F(0),F(1)]
    return polyadd([F(0)]+[(2*n-1)*x/n for x in leg(n-1)],[-(n-1)*x/n for x in leg(n-2)])

@lru_cache(None)
def prod(i,j):return polymul(leg(i),leg(j))

@lru_cache(None)
def shiftedleg(n):return [F((-1)**(n+l)*factorial(n+l),factorial(l)**2*factorial(n-l)) for l in range(n+1)]

@lru_cache(None)
def tpoly(i,j):
    r=[F(0)]*(i+j+2)
    for k in range(i+1):
        ai=F((-1)**(i+k)*factorial(i+k),2**k*factorial(k)**2*factorial(i-k))
        for l in range(j+1):
            aj=F((-1)**(j+l)*factorial(j+l),2**l*factorial(l)**2*factorial(j-l))
            r[k+l+1]+=(-1)**j*ai*aj*F(factorial(k)*factorial(l),factorial(k+l+1))
    return r

def inverse_series(p,n):
    r=[1/p[0]]
    for k in range(1,n+1):r.append(-sum((p[j]*r[k-j] for j in range(1,min(k,len(p)-1)+1)),F(0))/p[0])
    return r


SOURCE_DEGREES=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
SOURCE_COEFFICIENTS=['164018480112512163411979847045033354860286814396683571030069/500000000000000000000000000000000000000000000000000000000000', '-1', '483647885202406740629948493077253062150776995857013408880713/500000000000000000000000000000000000000000000000000000000000', '-26107878020040960771035029521234819454942408337488457038099/62500000000000000000000000000000000000000000000000000000000', '1200146538027145237853602806278925692737086876457656656819/40000000000000000000000000000000000000000000000000000000000', '54451666587616638371252134384391227349503966055463274551163/1000000000000000000000000000000000000000000000000000000000000', '-27933660232256949517408667493257416460682633840646113853311/1000000000000000000000000000000000000000000000000000000000000', '7253951579823722772363534332496791038806429839633926883563/1000000000000000000000000000000000000000000000000000000000000', '-856033529096393606964648887857482732443835846149468364909/500000000000000000000000000000000000000000000000000000000000', '948766261365282768354510432398796146811737431644392282989/1000000000000000000000000000000000000000000000000000000000000', '-114091330063973619547350301797559739256881101501643655513/250000000000000000000000000000000000000000000000000000000000', '310381190296545427874088182477397498416619510472895005829/1000000000000000000000000000000000000000000000000000000000000', '-6110097597538170265620485592436444254415861249937787351/100000000000000000000000000000000000000000000000000000000000', '97048029534789993152315339159250614447933389525159752927/1000000000000000000000000000000000000000000000000000000000000', '32220209683147168323130467853006707854904493378988952129/1000000000000000000000000000000000000000000000000000000000000', '1597592088764216018220055649283195016071373053956887/40000000000000000000000000000000000000000000000000000000', '21382578895933618998735734752627754039879942188408796483/500000000000000000000000000000000000000000000000000000000000', '15259048523448307947148744919302652362140044235493961287/500000000000000000000000000000000000000000000000000000000000', '3072781379694026659371547112576289369350310254254236563/100000000000000000000000000000000000000000000000000000000000', '12089961954395756906421414618014571268763692049766647521/500000000000000000000000000000000000000000000000000000000000', '22629544316980650983279720967953012921252561912284128383/1000000000000000000000000000000000000000000000000000000000000', '17976626812008601603944457119937992234635241842566037787/1000000000000000000000000000000000000000000000000000000000000', '13152161772272608956679417018769341558684230807519105499/1000000000000000000000000000000000000000000000000000000000000', '625958632509596836929583928084603925972792687443653959/50000000000000000000000000000000000000000000000000000000000', '7110385001593621318454820668257240186211666445686370139/1000000000000000000000000000000000000000000000000000000000000', '3005897384659188744014473587617533368381495835521767047/500000000000000000000000000000000000000000000000000000000000', '3277021036733145295481378101076976931642017981343133263/1000000000000000000000000000000000000000000000000000000000000', '790977345390041694250534368449591912753260370400406441/500000000000000000000000000000000000000000000000000000000000', '632716858028324087992261016497617625738353272624495539/1000000000000000000000000000000000000000000000000000000000000', '-1029891693616951021396187429853808369428346496295199853/1000000000000000000000000000000000000000000000000000000000000']
SOURCE_JSON_SHA256='b37e0e8ed3da94722652fbea40117246a9f180cae3b7d9ac0578368109bb44ed'
SOURCE_OLD_RAYLEIGH={'hi': '329629119641678396715614642284203289594975043263146221495670279121308617458008960690532639869911066782010656318170847272175058906709454996836111704365930258925302796110072550114443409839601/100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'lo': '164814522840761248995619815807364924101674927763366358637886619578932704991870488192147930862884576446538346059244703233836651710700688259637808914350377221301870980636666555323964944665639/50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'outward_decimal': ['0.000000000003296290456815', '0.000000000003296291196417']}

def configure(digits):
    global SCALE,TERMS,LOG2,PI,GAMMA
    SCALE=10**digits;TERMS=384 if digits<=220 else 512
    LOG2=2*atanh(I(F(1,3)))
    PI=16*atan(I(F(1,5)))-4*atan(I(F(1,239)))
    GAMMA=gamma()

def show(x):
    x=I.of(x);d=30
    def dec(v,hi=False):
        n=-((-v.numerator*10**d)//v.denominator) if hi else (v.numerator*10**d)//v.denominator
        return ('-' if n<0 else '')+str(abs(n)//10**d)+'.'+str(abs(n)%10**d).zfill(d)
    return [dec(x.lo),dec(x.hi,True)]

def pack(x):
    x=I.of(x);return {'lo':str(x.lo),'hi':str(x.hi),'decimal':show(x)}

def exact_hn(n):return polyadd(leg(n),[F(0),F(0)]+[-x for x in leg(n)])
PHI=[F(1),F(0),F(-1)]
SOURCE=[F(0)]*(max(SOURCE_DEGREES)+3)
for n,c in zip(SOURCE_DEGREES,SOURCE_COEFFICIENTS):
    SOURCE=polyadd(SOURCE,[F(c)*x for x in exact_hn(n)])
assert sum(SOURCE,F(0))==0 and all(x==0 for k,x in enumerate(SOURCE) if k%2)
BASIS=[SOURCE,PHI]

@lru_cache(None)
def mon_leg(r,n):
    if r<n or (r-n)%2:return F(0)
    def dfac(k):
        a=1
        for j in range(k,0,-2):a*=j
        return a
    return F(factorial(r),dfac(r-n)*dfac(r+n+1))

LEG_COEFF=[[sum((v*mon_leg(r,n) for r,v in enumerate(p)),F(0))*(2*n+1) for n in range(len(SOURCE))] for p in BASIS]
NORMS=[[integral(polymul(p,q)) for q in BASIS] for p in BASIS]
HARM=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(len(SOURCE))]
DIAGS=[[sum((HARM[n]*LEG_COEFF[i][n]*LEG_COEFF[j][n]/(2*n+1) for n in range(len(SOURCE))),F(0)) for j in range(2)] for i in range(2)]

def log_moment_coeff(p):
    return sum((v*sum((F(1,2*j+1) for j in range(k//2+1)),F(0))/(k+1) for k,v in enumerate(p) if not k%2),F(0))
VCON=[[log_moment_coeff(polymul(p,q)) for q in BASIS] for p in BASIS]

@lru_cache(None)
def moment_coeff(which,last=160):
    p=BASIS[which]
    return [sum((v/F(r+k+1) for r,v in enumerate(p)),F(0))/factorial(k) if k%2==0 else F(0) for k in range(last+1)]

def moment(which,a):
    c=a/2;last=160
    val=polyval(moment_coeff(which),c)
    norm=sum(abs(v) for v in BASIS[which])
    rem=norm*c**(last+2)/factorial(last+2)/(1-c**2/((last+3)*(last+4)))
    return val+I(-rem.hi,rem.hi)

def ratio(a):return moment(0,a)/moment(1,a)
def combine(mat,r):return I.of(mat[0][0])-2*r*mat[0][1]+r*r*mat[1][1]

def translate_exact(p,c):
    return [sum((v*comb(n,k)*c**(n-k) for n,v in enumerate(p) if n>=k),F(0)) for k in range(len(p))]

EDGES=[translate_exact(p,F(-1)) for p in BASIS]
@lru_cache(None)
def shift_poly(i,j):
    p,q=EDGES[i],EDGES[j];out=[F(0)]*(len(p)+len(q))
    for k,x in enumerate(p):
        if not x:continue
        for l,y in enumerate(q):
            if y:out[k+l+1]+=x*y*F(factorial(k)*factorial(l),factorial(k+l+1))
    return out

@lru_cache(None)
def shifted_unit(which):
    p=BASIS[which]
    return [sum((v*comb(n,k)*2**k*(-1)**(n-k) for n,v in enumerate(p) if n>=k),F(0)) for k in range(len(p))]

@lru_cache(None)
def kernel_energy(i,j,k):
    # Independent integration of BOTH triangles on [0,1]^2.
    p,q=shifted_unit(i),shifted_unit(j)
    beta=[F(factorial(r)*factorial(k),factorial(r+k+1)) for r in range(max(len(p),len(q)))]
    return 2**k*sum((x*y*(beta[r]+beta[s])/F(r+s+k+2) for r,x in enumerate(p) if x for s,y in enumerate(q) if y),F(0))

@lru_cache(None)
def gamma_model(M):
    degree=max(192,M+4)
    if degree%2:degree+=1
    cs=[F(1,factorial(k)) if not k%2 else F(0) for k in range(degree+1)]
    sn=[F(1,factorial(k+1)) if not k%2 else F(0) for k in range(degree+1)]
    ic=inverse_series(cs,M);ins=inverse_series(sn,M+1)
    pg=[(ic[k]+ins[k+1])/4 for k in range(M+1)]
    error=F(0)
    for p,d,fac in [(ic,cs,degree+2),(ins,sn,degree+3)]:
        residual=polymul(p,d);residual[0]-=1
        assert all(x==0 for x in residual[:len(p)])
        # Uniform x<=1. Denominators >=1, and the omitted factorial
        # series has successive ratio <=1/((degree+3)(degree+4)).
        error+=(sum(abs(x) for x in residual)+sum(abs(x) for x in p)/F(factorial(fac))/(1-F(1,(degree+3)*(degree+4))))/4
    return pg,error

@lru_cache(None)
def gamma_energy_poly(i,j,M):
    pg,_=gamma_model(M)
    return [F(0)]+[2*pg[k]*kernel_energy(i,j,k)/2**k for k in range(M+1)]

def sqrt_i(n):
    k=isqrt(n*SCALE*SCALE);return I(F(k,SCALE),F(k+1,SCALE)) if k*k!=n*SCALE*SCALE else I(F(k,SCALE))

def evaluate(a,M,active):
    a=I.of(a);r=ratio(a);norm=combine(NORMS,r)
    assert norm.lo>0
    diag=combine(DIAGS,r);v=combine([[VCON[i][j]-LOG2*NORMS[i][j] for j in range(2)] for i in range(2)],r)
    q0=(-log(2*PI*a)-GAMMA)*norm
    kmat=[[polyval(gamma_energy_poly(min(i,j),max(i,j),M),a) for j in range(2)] for i in range(2)]
    kg=combine(kmat,r)
    pieces={'harmonic':diag/norm,'log_potential':v/norm,'scalar':q0/norm,'regular_Gamma':-kg/norm}
    total=diag+v+q0-kg
    for q in active:
        prime=2 if q==4 else q;w=log(I(prime))/sqrt_i(q);u=2-log(I(q))/a
        assert u.lo>0
        smat=[[polyval(shift_poly(min(i,j),max(i,j)),u) for j in range(2)] for i in range(2)]
        contribution=-w*combine(smat,r)
        pieces['prime_'+str(q)]=contribution/norm;total+=contribution
    _,error=gamma_model(M)
    ray=total/norm+I(-(2*a*error).hi,(2*a*error).hi)
    return {'a':pack(a),'moment_ratio':pack(r),'norm':pack(norm),'pieces':{k:pack(v) for k,v in pieces.items()},
        'Rayleigh':pack(ray),'Gamma_uniform_error':pack(error),'Mellin_residual':pack(moment(0,a)-r*moment(1,a))}

class Jet:
    def __init__(self,v,d=0,dd=0):self.v=I.of(v);self.d=I.of(d);self.dd=I.of(dd)
    @staticmethod
    def of(x):return x if isinstance(x,Jet) else Jet(x)
    def __add__(self,o):
        o=Jet.of(o);return Jet(self.v+o.v,self.d+o.d,self.dd+o.dd)
    __radd__=__add__
    def __neg__(self):return Jet(-self.v,-self.d,-self.dd)
    def __sub__(self,o):return self+-Jet.of(o)
    def __rsub__(self,o):return Jet.of(o)+-self
    def __mul__(self,o):
        o=Jet.of(o);return Jet(self.v*o.v,self.d*o.v+self.v*o.d,self.dd*o.v+2*self.d*o.d+self.v*o.dd)
    __rmul__=__mul__
    def inv(self):
        v=1/self.v;return Jet(v,-self.d*v*v,2*self.d*self.d*v*v*v-self.dd*v*v)
    def __truediv__(self,o):return self*Jet.of(o).inv()
    def __rtruediv__(self,o):return Jet.of(o)*self.inv()

def jetpoly(p,x):
    v=Jet(0)
    for c in reversed(p):v=v*x+c
    return v

def jetlog(x):return Jet(log(x.v),x.d/x.v,x.dd/x.v-(x.d/x.v)**2)

def jetmoment(which,a):
    assert 0<a.v.lo<=a.v.hi<=1
    val=jetpoly(moment_coeff(which),a/2);norm=sum(abs(x) for x in BASIS[which]);tails=[]
    for d in range(3):
        k=162
        tails.append(norm*F(1,2**d)*F(1,2)**(k-d)/factorial(k-d)/(1-F(1,4*(k-d+1)*(k-d+2))))
    return Jet(val.v+I(-tails[0],tails[0]),val.d+I(-tails[1],tails[1]),val.dd+I(-tails[2],tails[2]))

@lru_cache(None)
def centered_shift(i,j,center):return translate_exact(shift_poly(i,j),center)

def jetcombine(mat,r):return Jet.of(mat[0][0])-2*r*mat[0][1]+r*r*mat[1][1]

def jetenergy(ai,M,centers=None,target=F(0)):
    a=Jet(ai,1);r=jetmoment(0,a)/jetmoment(1,a);norm=jetcombine(NORMS,r)
    diag=jetcombine(DIAGS,r);v=jetcombine([[VCON[i][j]-LOG2*NORMS[i][j] for j in range(2)] for i in range(2)],r)
    q0=(-jetlog(a)-log(2*PI)-GAMMA)*norm
    kg=jetcombine([[jetpoly(gamma_energy_poly(min(i,j),max(i,j),M),a) for j in range(2)] for i in range(2)],r)
    total=diag+v+q0-kg
    if centers is None:centers={2:F(6,5),3:F(3,4),4:F(2,5),5:F(1,6)}
    for q in (2,3,4,5):
        w=log(I(2 if q==4 else q))/sqrt_i(q);u=2-Jet(log(I(q)))/a;center=centers[q]
        mat=[[jetpoly(centered_shift(min(i,j),max(i,j),center),u-center) for j in range(2)] for i in range(2)]
        total-=jetcombine(mat,r)*w
    _,eps=gamma_model(M)
    return total-(target+2*a*eps)*norm

@lru_cache(None)
def centered_channel5(i,j,center):
    p=shift_poly(i,j);assert p[:3]==[0,0,0]
    return translate_exact(p[3:],center)

def jet_channel5(ai,M,centers=None,target=F(0)):
    a=Jet(ai,1);r=jetmoment(0,a)/jetmoment(1,a);u=2-Jet(log(I(5)))/a
    center=F(1,6) if centers is None else centers[5]
    mat=[[jetpoly(centered_channel5(min(i,j),max(i,j),center),u-center) for j in range(2)] for i in range(2)]
    return jetcombine(mat,r)

def transport_cover(M,target=F(1,10**12),mode='energy'):
    B=log(I(5))/2;C=log(I(7))/2
    # Rational t in [0,1], a(t)=B+(C-B)t. Hence channel 5 is
    # active (or exactly zero at t=0), with no extrapolated entrance.
    evaluator=jetenergy if mode=='energy' else jet_channel5
    globaljet=evaluator(I(B.lo,C.hi),M,target=target)
    print('global second derivative bound',show(globaljet.dd),flush=True)
    stack=[(F(0),F(1),0)];accepted=[];fail=[];calls=0
    while stack:
        lo,hi,depth=stack.pop();tmid=(lo+hi)/2;mid=B+(C-B)*tmid;rad=(C-B).hi*(hi-lo)/2
        cell=I((B+(C-B)*lo).lo,(B+(C-B)*hi).hi)
        centers={q:F(((2-log(I(q))/mid).lo*1000).__floor__(),1000) for q in (2,3,4,5)}
        box=evaluator(cell,M,centers,target);point=evaluator(mid,M,centers,target)
        second=max(abs(box.dd.lo),abs(box.dd.hi));first=max(abs(point.d.lo),abs(point.d.hi))
        lower=point.v.lo-first*rad-second*rad*rad/2
        calls+=1
        if lower>0:
            accepted.append({'lo':str(lo),'hi':str(hi),'lower':str(lower),'second_abs_upper':str(second)})
        elif depth<45 and calls<10000:
            stack.append((tmid,hi,depth+1));stack.append((lo,tmid,depth+1))
        else:fail.append({'lo':str(lo),'hi':str(hi),'depth':depth,'lower':str(lower)})
        if calls%10==0:print('cover',calls,'accepted',len(accepted),'pending',len(stack),'fail',len(fail),flush=True)
    return {'mode':mode,'target':str(target),'parameter':'a=B+(C-B)t, 0<=t<=1','cells':accepted,'failures':fail,'calls':calls}
@lru_cache(None)
def kernel_images(which,M):
    p=BASIS[which];b=shifted_unit(which);cols=[[integral(p)]]
    for k in range(1,M+1):
        source=p if k==1 else [k*(k-1)*v for v in cols[k-2]]
        out=[F(0),F(0)]+[v/F((n+1)*(n+2)) for n,v in enumerate(source)]
        value=2**k*sum((v*F(factorial(n)*factorial(k),factorial(n+k+1)) for n,v in enumerate(b)),F(0))
        deriv=k*2**(k-1)*sum((v*F(factorial(n)*factorial(k-1),factorial(n+k)) for n,v in enumerate(b)),F(0))
        alpha=deriv-sum((n*v for n,v in enumerate(out)),F(0));beta=value-sum(out,F(0))-alpha
        out[1]+=alpha;out[0]+=beta
        assert all(v==0 for n,v in enumerate(out) if n%2)
        cols.append(out)
    return cols

def primitive_v(x,nmax):
    negative=x.hi<0
    if negative:x=-x
    assert 0<=x.lo<=x.hi<=1
    endpoint=x.lo==x.hi==1
    lm=I(0) if endpoint else log(1-x);lp=log(1+x)
    powers=I(1);simple=I(0);alternating=I(0);out=[]
    for n in range(nmax+1):
        m=n+1;powers*=x;simple+=powers/m;alternating=-alternating+powers/m
        minus=((powers-1)*lm-simple)/m
        plus=((powers-(-1)**m)*lp-alternating)/m
        val=-(minus+plus)/2
        out.append(val*((-1)**m if negative else 1))
    return out

def poly_integral(p,lo,hi):
    lp=hp=I(1);out=I(0)
    for n,v in enumerate(p):
        lp*=lo;hp*=hi;out+=v*(hp-lp)/(n+1)
    return out

def v_integral(p,lo,hi):
    l=primitive_v(lo,len(p)-1);h=primitive_v(hi,len(p)-1)
    return sum((v*(h[n]-l[n]) for n,v in enumerate(p)),I(0))

def translate_interval(p,s):
    # Horner translation, separate from the source energy beta formula.
    out=[I(0)]
    for v in reversed(p):
        out=[s*out[0]+v]+[out[k-1]+s*(out[k] if k<len(out) else 0) for k in range(1,len(out)+1)]
    return out[:-1]

@lru_cache(None)
def projection_shift(n,which):
    p=translate_exact(leg(n),F(-1));q=EDGES[which];out=[F(0)]*(len(p)+len(q))
    for k,x in enumerate(p):
        for l,y in enumerate(q):
            if x and y:out[k+l+1]+=x*y*F(factorial(k)*factorial(l),factorial(k+l+1))
    return out

def audit_tail(a,M,cutoffs=(63,79,95)):
    r=ratio(a);p=[I(v)-r*(PHI[k] if k<len(PHI) else 0) for k,v in enumerate(SOURCE)]
    norm=combine(NORMS,r);v0=LEG_COEFF[0][0]-r*LEG_COEFF[1][0];xnorm=norm-v0*v0
    pg,eps=gamma_model(M);images=[kernel_images(i,M) for i in range(2)]
    kp=[I(0)]*(len(SOURCE)+M+1)
    for k in range(M+1):
        # All degree-k kernel energies are compared with the independent
        # two-triangle beta integration before using the image.
        for i,j in ((0,0),(0,1),(1,1)):
            assert integral(polymul(BASIS[i],images[j][k]))==kernel_energy(i,j,k)
        if not pg[k]:continue
        factor=2*a*pg[k]*(a/2)**k
        for n in range(len(images[0][k])):
            coeff=images[0][k][n]-r*(images[1][k][n] if n<len(images[1][k]) else 0)
            kp[n]+=factor*coeff
    zero=I(0);one=I(1)
    kk=poly_integral(polymul(kp,kp),zero,one)
    vk=v_integral(polymul(p,kp),zero,one)
    vv=I(0)
    for n,v in enumerate(polymul(p,p)):
        if n%2:continue
        rr=n//2;odd=sum((F(1,2*j+1) for j in range(rr+1)),F(0));odd2=sum((F(1,(2*j+1)**2) for j in range(rr+1)),F(0))
        vv+=v*((odd-LOG2)**2+odd2-PI**2/12)/(n+1)
    ch=[]
    for q in (2,3,4):
        d=log(I(q))/a;w=log(I(2 if q==4 else q))/sqrt_i(q);acts=[]
        for sign in (-1,1):
            s=sign*d;lo=I(-1) if sign==1 else -1+d;hi=1-d if sign==1 else I(1)
            acts.append((lo,hi,translate_interval(p,s)))
        ch.append((q,w,acts))
    pair={};vs=I(0);ks=I(0);ss=I(0)
    for q,w,acts in ch:
        for lo,hi,ap in acts:
            vs+=w*v_integral(polymul(p,ap),lo,hi)/2
            ks+=w*poly_integral(polymul(kp,ap),lo,hi)/2
        for q2,w2,acts2 in ch:
            value=I(0)
            for lo,hi,ap in acts:
                for lo2,hi2,bp in acts2:
                    # Endpoints are tiny point intervals with certified order.
                    assert (lo.lo==lo2.lo and lo.hi==lo2.hi) or lo.hi<lo2.lo or lo2.hi<lo.lo
                    assert (hi.lo==hi2.lo and hi.hi==hi2.hi) or hi.hi<hi2.lo or hi2.hi<hi.lo
                    l=lo if lo.lo+lo.hi>=lo2.lo+lo2.hi else lo2
                    h=hi if hi.lo+hi.hi<=hi2.lo+hi2.hi else hi2
                    if l.lo>=h.hi:continue
                    assert l.hi<h.lo
                    value+=poly_integral(polymul(ap,bp),l,h)/2
            pair[str(q)+'_'+str(q2)]=pack(value/norm);ss+=w*w2*value
    full=vv+kk+ss-2*vk-2*vs+2*ks
    print('full joint residual norm',show(full/norm),flush=True)
    prefix=I(0);data={};source=evaluate(a,M,[2,3,4]);modelray=sum((I(F(v['lo']),F(v['hi'])) for v in source['pieces'].values()),I(0))
    for n in range(0,max(cutoffs)+1,2):
        vh=[]
        for which in (0,1):
            pol=polymul(BASIS[which],leg(n));vh.append(log_moment_coeff(pol)-LOG2*integral(pol))
        vp=vh[0]-r*vh[1]
        kproj=sum((v*mon_leg(k,n) for k,v in enumerate(kp)),I(0))
        sp=I(0)
        for q,w,_ in ch:
            u=2-log(I(q))/a
            sp+=w*(polyval(projection_shift(n,0),u)-r*polyval(projection_shift(n,1),u))
        proj=vp-kproj-sp;prefix+=(2*n+1)*proj*proj
        if n+1 in cutoffs:
            cutoff=n+1;tail=n+2;gram=full-prefix
            harmonic=sum((F(1,k) for k in range(1,tail+1)),F(0))
            L=2*a;gL=(1/exp_pos(L/2))/(1-1/exp_pos(2*L))-1/(2*L)
            snorm=LOG2+log(I(3))/sqrt_i(3)+LOG2/2
            q0=-log(2*PI*a)-GAMMA
            beta=((a/2)**2/(2*(1-(a/2)**2/12)))**2
            assert max(abs(q0.lo),abs(q0.hi))<4
            assert ((1-LOG2)**2+1-PI**2/12).hi<4
            assert (L*(F(1,4)+eps)).hi<1 and snorm.hi<2 and beta.hi<1
            assert 0<gL.lo<=gL.hi<F(1,4) and L.hi<2
            rem=(a/2)**tail/factorial(tail)/(1-(a/2)**2/((tail+1)*(tail+2)))
            err=2*L*eps+80*rem
            delta=harmonic-log(2*PI*a)-GAMMA-L*(F(1,4)-gL+eps)-snorm-err
            ga=F(1001,1000)*gram+1001*err*err*xnorm
            deduction=ga/delta/norm;lower=modelray-err*xnorm/norm-deduction
            assert gram.lo>0 and delta.lo>0 and lower.lo>0
            data[str(cutoff)]={'full_tail_Gram_over_source_norm':pack(gram/norm),'tail_floor':pack(delta),
                'directional_Schur_deduction':pack(deduction),'directional_comparison_lower':pack(lower)}
            print('tail cutoff',cutoff,'Gram',show(gram/norm),'deduction',show(deduction),'lower',show(lower),flush=True)
    return {'cutoffs':data,'mixed_shift_Gram':pair,'joint_residual_norm_over_source_norm':pack(full/norm),
            'squared_norm_components':{k:pack(v/norm) for k,v in {'VV':vv,'KK':kk,'SS':ss,'VK':vk,'VS':vs,'KS':ks}.items()},
            'exact_kernel_identity_comparisons':3*(M+1)}
def run():
    report={'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN','checks':[],
            'scope':'one explicit even source, its whole directional tail, and its exact-Mellin transport; not a new all-source endpoint theorem',
            'source_commit':'6a16d90b551588572c87e622c21c2df7f7b1adc2','source_json_sha256':SOURCE_JSON_SHA256,
            'source_degrees':SOURCE_DEGREES,'source_coefficients':SOURCE_COEFFICIENTS,
            'source_definition':'H=sum c_n (1-x^2)P_n; phi=1-x^2; v_a=H-<H,cosh(ax/2)>/<phi,cosh(ax/2)> phi',
            'source_monomial_H':[str(x) for x in SOURCE]}
    lines=[]
    def check(name,ok):
        assert ok,name
        report['checks'].append(name);lines.append('PASS '+name)
    def interval(v):return I(F(v['lo']),F(v['hi']))
    def cover_check(name,r):
        check(name+' all cells positive',not r['failures'] and all(F(v['lower'])>0 for v in r['cells']))
        cells=sorted(r['cells'],key=lambda v:F(v['lo']))
        check(name+' exact continuum cover',F(cells[0]['lo'])==0 and F(cells[-1]['hi'])==1 and all(F(a['hi'])==F(b['lo']) for a,b in zip(cells,cells[1:])))
    check('source degree 62, even parity and exact zero endpoint traces',len(SOURCE)==63 and sum(SOURCE,F(0))==0 and all(x==0 for n,x in enumerate(SOURCE) if n%2))
    configure(220);M=112;B=log(I(5))/2;C=log(I(7))/2
    check('transport interval and exact active-set thresholds',0<B.lo<B.hi<C.lo<C.hi<1)
    points=[('B',B,[2,3,4]),('17/20',I(F(17,20)),[2,3,4,5]),('9/10',I(F(9,10)),[2,3,4,5]),('19/20',I(F(19,20)),[2,3,4,5]),('C',C,[2,3,4,5])]
    report['points']={}
    for name,a,active in points:
        print('direct point '+name,flush=True);v=evaluate(a,M,active);report['points'][name]=v
        mr=interval(v['Mellin_residual'])
        check(name+' numerical moment enclosure consistent with exact cancellation',mr.lo<=0<=mr.hi and mr.hi-mr.lo<F(1,10**150))
        check(name+' direct positive Rayleigh enclosure',F(v['Rayleigh']['lo'])>0)
        lines.append(name+' Rayleigh '+str(v['Rayleigh']['decimal']))
    oldlo=F(SOURCE_OLD_RAYLEIGH['lo']);oldhi=F(SOURCE_OLD_RAYLEIGH['hi']);base=interval(report['points']['B']['Rayleigh'])
    check('reconstructs the pinned original source Rayleigh enclosure',oldlo<base.lo<base.hi<oldhi)
    rB=ratio(B);rbox=ratio(I(B.lo,C.hi));normB=combine(NORMS,rB);normbox=combine(NORMS,rbox)
    diff=rbox-rB;det=NORMS[0][0]*NORMS[1][1]-NORMS[0][1]**2
    sinupper=max(abs(diff.lo),abs(diff.hi))**2*det/(normB.lo*normbox.lo)
    check('whole-family normalized overlap squared > 0.99998',det>0 and normbox.lo>0 and 1-sinupper>F(99998,100000))
    report['overlap_squared_lower']=pack(1-sinupper)
    report['source_Legendre_at_B']=[pack(LEG_COEFF[0][n]-rB*LEG_COEFF[1][n]) for n in range(len(SOURCE))]
    print('continuum source-energy cover',flush=True)
    report['energy_cover']=transport_cover(M);cover_check('energy',report['energy_cover'])
    print('continuum channel-5 sign cover',flush=True)
    report['channel5_cover']=transport_cover(M,target=F(0),mode='channel5');cover_check('channel5',report['channel5_cover'])
    configure(300);M=144;B=log(I(5))/2;C=log(I(7))/2
    report['precision_recheck']={'digits':300,'Gamma_degree':M}
    for name,a,active in [('B',B,[2,3,4]),('C',C,[2,3,4,5])]:
        v=evaluate(a,M,active);report['precision_recheck'][name]=v
        old=report['points'][name]['Rayleigh'];new=v['Rayleigh']
        check(name+' higher precision and Gamma degree strictly narrow the enclosure',F(old['lo'])<F(new['lo'])<F(new['hi'])<F(old['hi']))
        lines.append(name+' higher precision Rayleigh '+str(new['decimal']))
    print('whole infinite directional tail',flush=True)
    tail=audit_tail(B,M);report['tail_audit']=tail
    check('435 exact Gamma image versus triangle-integral comparisons',tail['exact_kernel_identity_comparisons']==435)
    for q in (2,3,4):
        for r in (2,3,4):
            a=tail['mixed_shift_Gram'][str(q)+'_'+str(r)];b=tail['mixed_shift_Gram'][str(r)+'_'+str(q)]
            assert max(F(a['lo']),F(b['lo']))<=min(F(a['hi']),F(b['hi']))
    check('all nine ordered mixed shift Gram entries and their symmetry',len(tail['mixed_shift_Gram'])==9)
    previous=None
    for n in (63,79,95):
        row=tail['cutoffs'][str(n)]
        check('cutoff '+str(n)+' full tail and directional Schur lower bound positive',all(F(row[k]['lo'])>0 for k in ['full_tail_Gram_over_source_norm','tail_floor','directional_comparison_lower']))
        if previous:
            check('cutoff '+str(n)+' tail subtraction decreases',F(row['directional_Schur_deduction']['hi'])<F(previous['directional_Schur_deduction']['lo']))
        previous=row
        lines.append('cutoff '+str(n)+' Schur deduction '+str(row['directional_Schur_deduction']['decimal']))
    report.update({'verdict':'SOURCE-AND-TRANSPORT-POSITIVE','transport_Rayleigh_lower':'1/1000000000000',
        'channel5_sign':'strictly negative contribution for B<a<=C; exactly zero at B',
        'mellin_conditions':2,'external_audit_completed':False,'new_all_source_endpoint_theorem':False,
        'check_count':len(report['checks'])})
    lines.append('TOTAL '+str(len(report['checks']))+' checks PASS')
    lines.append('ONLY THIS TRANSPORTED FAMILY: Rayleigh > 1/10^12 for B<=a<=C')
    lines.append('NO ALL-SOURCE COERCIVITY CLAIM AT C; EXTERNAL REVIEW OPEN')
    return report,'\n'.join(lines)+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__);mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--write',action='store_true');mode.add_argument('--verify',action='store_true')
    args=parser.parse_args();root=Path(__file__).resolve().parent
    report,logtext=run();jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
    files={'near_results.json':jsontext,'near_checks.log':logtext}
    payload=['PROOF.md','README.md','check_near.py','near_checks.log','near_results.json']
    if args.write:
        for name,content in files.items():(root/name).write_text(content,encoding='utf-8',newline='\n')
        (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in payload),encoding='ascii',newline='\n')
    if args.verify:
        for name,content in files.items():assert (root/name).read_bytes()==content.encode('utf-8'),name+' replay mismatch'
        entries=(root/'SHA256SUMS').read_text(encoding='ascii').splitlines();assert len(entries)==5
        for entry in entries:
            digest,name=entry.split('  ',1);assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name+' hash mismatch'
        print('REPLAY and all five SHA256 payload hashes PASS',flush=True)
    print(logtext,end='')

if __name__=='__main__':main()
