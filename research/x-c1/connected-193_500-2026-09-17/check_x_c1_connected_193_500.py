#!/usr/bin/env python3
from fractions import Fraction as F
import sys
sys.set_int_max_str_digits(1000000)
import json
from pathlib import Path

checks=[]

def ok(name, cond, value=None):
    if not cond:
        raise AssertionError(f"{name}: {value!r}")
    checks.append(name)

def exp_neg_iv(x, N=24):
    s=F(0); term=F(1); sums=[]
    for k in range(N+1):
        if k==0: term=F(1)
        elif k>0: term *= x/F(k)
        s += term if k%2==0 else -term
        sums.append(s)
    if N%2==0: return sums[N-1], sums[N]
    return sums[N], sums[N-1]

def atanh_series_iv(t,N=24):
    s=F(0)
    for n in range(N):
        s += t**(2*n+1)/F(2*n+1)
    tail=t**(2*N+1)/F(2*N+1)/(1-t*t)
    return s,s+tail

def log2_iv(N=24):
    lo,hi=atanh_series_iv(F(1,3),N)
    return 2*lo,2*hi

def log_iv(x,N=24):
    assert x>0
    k=0; y=x
    while y>=2:
        y/=2; k+=1
    while y<1:
        y*=2; k-=1
    t=(y-1)/(y+1)
    alo,ahi=atanh_series_iv(t,N)
    lylo,lyhi=2*alo,2*ahi
    l2lo,l2hi=log2_iv(N)
    if k>=0:
        return lylo+k*l2lo, lyhi+k*l2hi
    return lylo+k*l2hi, lyhi+k*l2lo

def atan_small_iv(x,N=12):
    sums=[]; s=F(0)
    for n in range(N):
        s += ((-1)**n)*x**(2*n+1)/F(2*n+1)
        sums.append(s)
    a,b=sums[-1],sums[-2]
    return min(a,b),max(a,b)

def pi_iv():
    a1lo,a1hi=atan_small_iv(F(1,5),15)
    a2lo,a2hi=atan_small_iv(F(1,239),8)
    return 16*a1lo-4*a2hi,16*a1hi-4*a2lo

def H_iv(s):
    qlo,qhi=exp_neg_iv(s/2,24)
    ratio_lo=(1+qlo)/(1-qlo)
    ratio_hi=(1+qhi)/(1-qhi)
    llo,_=log_iv(ratio_lo,24)
    _,lhi=log_iv(ratio_hi,24)
    ahlo,ahhi=llo/2,lhi/2
    pilo,pihi=pi_iv()
    rhi=(1-qlo)/(1+qlo)
    rlo=(1-qhi)/(1+qhi)
    _,ar_hi=atan_small_iv(rhi,10)
    ar_lo,_=atan_small_iv(rlo,10)
    return ahlo+pilo/4-ar_hi, ahhi+pihi/4-ar_lo

def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))

a=F(193,500)
C=F(3307,2000)
ell0=F(693,1000)

l2lo,l2hi=log2_iv()
ok("log2 > 693/1000", l2lo>ell0, l2lo)
ok("log2 < 7/10", l2hi<F(7,10), l2hi)
ok("sqrt2 > 7/5", F(2) > F(49,25))

H200=harmonic(200)
log200lo,_=log_iv(F(200))
gamma_up=H200-log200lo-F(1,401)
ok("gamma upper < 57722/100000", gamma_up<F(57722,100000), gamma_up)

pilo,pihi=pi_iv()
_,log8pi_hi=log_iv(8*pihi)
kappa_hi=log8pi_hi+gamma_up+pihi/2
Halo,Hahi=H_iv(a)
center_lo=2*Halo-kappa_hi
ok("center rho > -3307/2000", center_lo>-C, center_lo)

d0=2*a-ell0
Hdlo,_=H_iv(d0)
Hello,_=H_iv(ell0)
endband_lo=Hdlo+Hello-2*Hahi
ok("endband extra leakage > 1/2", endband_lo>F(1,2), endband_lo)

lam1=F(1)+F(2,5)*a-C
lam2=F(3,2)+F(2,5)*a-C
ok("lambda1 exact", lam1==-F(4991,10000), lam1)
ok("lambda2 exact", lam2==F(9,10000), lam2)
ok("lambda2 positive", lam2>0, lam2)

z=a/2
cosh_bound=z*z/(2*(1-z*z/F(12)))
sinh_bound=z*z/(6*(1-z*z/F(20)))
ok("cosh relative remainder <1/50", cosh_bound<F(1,50), cosh_bound)
ok("sinh relative remainder <1/150", sinh_bound<F(1,150), sinh_bound)

B_even=C/lam2*F(1,2500)
B_odd=(-lam1)/lam2*F(1,22500)
B2=max(B_even,B_odd)
ok("B_even = 3307/4500", B_even==F(3307,4500), B_even)
ok("B2 < 1", B2<1, B2)
gap=(1-B2)*lam2/(1+F(1,2500))
ok("gap exact", gap==F(1193,5002000), gap)
ok("gap >1/5000", gap>F(1,5000), gap)

results={
    "a": str(a),
    "center_lower_decimal": f"{float(center_lo):.15f}",
    "endband_lower_decimal": f"{float(endband_lo):.15f}",
    "lambda1": str(lam1),
    "lambda2": str(lam2),
    "B2_upper": str(B2),
    "gap": str(gap),
    "checks": len(checks),
}
Path("connected_193_500_results.json").write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
for name in checks:
    print(f"PASS {name}")
print(f"TOTAL {len(checks)}")
