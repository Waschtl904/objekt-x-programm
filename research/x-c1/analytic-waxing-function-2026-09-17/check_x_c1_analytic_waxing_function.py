#!/usr/bin/env python3
from fractions import Fraction as F
import json
from pathlib import Path

checks=[]
def ok(name, cond, value=None):
    if not cond:
        raise AssertionError(f"{name}: {value!r}")
    checks.append(name)

def exp_neg_iv(x,N=40):
    s=F(0); term=F(1); sums=[]
    for k in range(N+1):
        if k==0: term=F(1)
        else: term*=x/F(k)
        s += term if k%2==0 else -term
        sums.append(s)
    return (sums[N-1],sums[N]) if N%2==0 else (sums[N],sums[N-1])

def atanh_iv(t,N=40):
    s=F(0)
    for n in range(N):
        s += t**(2*n+1)/F(2*n+1)
    tail=t**(2*N+1)/F(2*N+1)/(1-t*t)
    return s,s+tail

def log2_iv(N=40):
    lo,hi=atanh_iv(F(1,3),N)
    return 2*lo,2*hi

def log_iv(x,N=40):
    assert x>0
    k=0; y=x
    while y>=2:
        y/=2; k+=1
    while y<1:
        y*=2; k-=1
    q=(y-1)/(y+1)
    alo,ahi=atanh_iv(q,N)
    lylo,lyhi=2*alo,2*ahi
    l2lo,l2hi=log2_iv(N)
    if k>=0:
        return lylo+k*l2lo,lyhi+k*l2hi
    return lylo+k*l2hi,lyhi+k*l2lo

def atan_iv(x,N=20):
    s=F(0); sums=[]
    for n in range(N):
        s += (-1)**n*x**(2*n+1)/F(2*n+1)
        sums.append(s)
    return min(sums[-1],sums[-2]),max(sums[-1],sums[-2])

def pi_iv():
    a1lo,a1hi=atan_iv(F(1,5),20)
    a2lo,a2hi=atan_iv(F(1,239),10)
    return 16*a1lo-4*a2hi,16*a1hi-4*a2lo

def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))

def gamma_iv(n=100):
    lnlo,lnhi=log_iv(F(n))
    base_lo=harmonic(n)-lnhi-F(1,2*n)+F(1,12*n*n)-F(1,120*n**4)
    base_hi=harmonic(n)-lnlo-F(1,2*n)+F(1,12*n*n)-F(1,120*n**4)+F(1,252*n**6)
    return base_lo,base_hi

def H_iv(s):
    qlo,qhi=exp_neg_iv(s/2)
    ratio_lo=(1+qlo)/(1-qlo); ratio_hi=(1+qhi)/(1-qhi)
    llo,_=log_iv(ratio_lo); _,lhi=log_iv(ratio_hi)
    pilo,pihi=pi_iv()
    rlo=(1-qhi)/(1+qhi); rhi=(1-qlo)/(1+qlo)
    arlo,_=atan_iv(rlo,16); _,arhi=atan_iv(rhi,16)
    return llo/2+pilo/4-arhi, lhi/2+pihi/4-arlo

def h_iv(t):
    qlo,qhi=exp_neg_iv(t/2)
    rlo,rhi=exp_neg_iv(2*t)
    return qlo/(1-rlo), qhi/(1-rhi)

def kappa_iv():
    pilo,pihi=pi_iv(); glo,ghi=gamma_iv(100)
    loglo,_=log_iv(8*pilo); _,loghi=log_iv(8*pihi)
    return loglo+glo+pilo/2, loghi+ghi+pihi/2

def Lambda2_iv(a):
    hlo,hhi=h_iv(2*a)
    Hlo,Hhi=H_iv(a)
    klo,khi=kappa_iv()
    return F(1)+2*a*hlo+2*Hlo-khi, F(1)+2*a*hhi+2*Hhi-klo

b=F(10,57)
coef=2*b+b*b
ok("sinh-square coefficient = 1240/3249", coef==F(1240,3249), coef)
ok("sinh-square coefficient < 1/2", coef<F(1,2), coef)

a_lo=F(3916683,10_000_000)
a_hi=F(3916684,10_000_000)
Llo_lo,Llo_hi=Lambda2_iv(a_lo)
Lhi_lo,Lhi_hi=Lambda2_iv(a_hi)
ok("Lambda2(a_lo) > 0", Llo_lo>0, Llo_lo)
ok("Lambda2(a_hi) < 0", Lhi_hi<0, Lhi_hi)

L387_lo,L387_hi=Lambda2_iv(F(387,1000))
ok("optimal constant-floor Lambda2(0.387) > 0", L387_lo>0, L387_lo)

L392_lo,L392_hi=Lambda2_iv(F(49,125))
ok("optimal constant-floor Lambda2(0.392) < 0", L392_hi<0, L392_hi)

results={
    "a_root_lower": str(a_lo),
    "a_root_upper": str(a_hi),
    "Lambda2_lower_endpoint_lower_decimal": f"{float(Llo_lo):.18g}",
    "Lambda2_upper_endpoint_upper_decimal": f"{float(Lhi_hi):.18g}",
    "Lambda2_at_0.387_lower_decimal": f"{float(L387_lo):.18g}",
    "Lambda2_at_0.392_upper_decimal": f"{float(L392_hi):.18g}",
    "checks": len(checks),
}
Path("analytic_waxing_results.json").write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
for name in checks:
    print("PASS",name)
print("TOTAL",len(checks))
