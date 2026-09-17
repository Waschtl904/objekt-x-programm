#!/usr/bin/env python3
from fractions import Fraction as F
import sys, json
from pathlib import Path
sys.set_int_max_str_digits(1000000)

checks=[]

def ok(name, cond, value=None):
    if not cond:
        raise AssertionError(f"{name}: {value!r}")
    checks.append(name)

def exp_neg_iv(x, N=26):
    s=F(0); term=F(1); sums=[]
    for k in range(N+1):
        if k==0: term=F(1)
        else: term *= x/F(k)
        s += term if k%2==0 else -term
        sums.append(s)
    return (sums[N-1], sums[N]) if N%2==0 else (sums[N], sums[N-1])

def atanh_series_iv(t,N=28):
    s=F(0)
    for n in range(N):
        s += t**(2*n+1)/F(2*n+1)
    tail=t**(2*N+1)/F(2*N+1)/(1-t*t)
    return s,s+tail

def log2_iv(N=28):
    lo,hi=atanh_series_iv(F(1,3),N)
    return 2*lo,2*hi

def log_iv(x,N=28):
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

def atan_small_iv(x,N=14):
    sums=[]; s=F(0)
    for n in range(N):
        s += ((-1)**n)*x**(2*n+1)/F(2*n+1)
        sums.append(s)
    a,b=sums[-1],sums[-2]
    return min(a,b),max(a,b)

def pi_iv():
    a1lo,a1hi=atan_small_iv(F(1,5),17)
    a2lo,a2hi=atan_small_iv(F(1,239),9)
    return 16*a1lo-4*a2hi,16*a1hi-4*a2lo

def H_iv(s):
    qlo,qhi=exp_neg_iv(s/2,26)
    ratio_lo=(1+qlo)/(1-qlo)
    ratio_hi=(1+qhi)/(1-qhi)
    llo,_=log_iv(ratio_lo,28)
    _,lhi=log_iv(ratio_hi,28)
    ahlo,ahhi=llo/2,lhi/2
    pilo,pihi=pi_iv()
    rhi=(1-qlo)/(1+qlo)
    rlo=(1-qhi)/(1+qhi)
    _,ar_hi=atan_small_iv(rhi,12)
    ar_lo,_=atan_small_iv(rlo,12)
    return ahlo+pilo/4-ar_hi, ahhi+pihi/4-ar_lo

def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))

a=F(387,1000)
L=2*a
C=F(331,200)
c=F(43,200)

l2lo,l2hi=log2_iv()
ok("log2 > 693/1000", l2lo>F(693,1000), l2lo)
ok("log2 < 694/1000", l2hi<F(694,1000), l2hi)
ok("sqrt2 > 707/500", F(2)>F(707,500)**2)
w2_upper=F(491,1000)
ok("w2 < 491/1000", F(347,707)<w2_upper, F(347,707))

H300=harmonic(300)
log300lo,_=log_iv(F(300))
gamma_up=H300-log300lo-F(1,601)
ok("gamma upper < 578/1000", gamma_up<F(578,1000), gamma_up)

pilo,pihi=pi_iv()
_,log8pi_hi=log_iv(8*pihi)
kappa_hi=log8pi_hi+gamma_up+pihi/2
Halo,Hahi=H_iv(a)
center_lo=2*Halo-kappa_hi
ok("center rho > -331/200", center_lo>-C, center_lo)

d_hi=2*a-l2lo
Hdlo,_=H_iv(d_hi)
Helllo,_=H_iv(l2hi)
endband_lo=Hdlo+Helllo-2*Hahi
ok("endband extra leakage > 99/200", endband_lo>F(99,200), endband_lo)
ok("endband extra leakage > w2", F(99,200)>w2_upper, (F(99,200),w2_upper))

b=F(1,6)/(1-L*L/F(20))
A=F(1,2)-2*c
B=F(1,8)-b
D=F(1,48)-2*c*b
qL=A+B*L+D*L*L
ok("kernel lower polynomial coefficients B,D negative", B<0 and D<0, (B,D))
ok("kernel lower endpoint margin positive", qL>0, qL)

old_lam2=F(3,2)+L*F(1,5)-C
ok("old scalarized lambda2 crosses negative", old_lam2==-F(1,5000), old_lam2)

lam0=-C
lam1=F(1)+L*c-C
lam2=F(3,2)+L*c-C
lam3=F(11,6)+L*c-C
ok("new lambda1 exact", lam1==-F(48859,100000), lam1)
ok("new lambda2 exact", lam2==F(1141,100000), lam2)
ok("new lambda2 positive", lam2>0, lam2)
ok("new lambda3-lambda2=1/3", lam3-lam2==F(1,3), lam3-lam2)

z=a/2
cosh_bound=z*z/(2*(1-z*z/F(12)))
sinh_bound=z*z/(6*(1-z*z/F(20)))
ok("cosh relative remainder <1/50", cosh_bound<F(1,50), cosh_bound)
ok("sinh relative remainder <1/150", sinh_bound<F(1,150), sinh_bound)

B_even=C/lam2*F(1,2500)
B_odd=(-lam1)/lam2*F(1,22500)
B2=max(B_even,B_odd)
ok("B_even exact", B_even==F(331,5705), B_even)
ok("B_odd exact", B_odd==F(48859,25672500), B_odd)
ok("B2 < 3/50", B2<F(3,50), B2)

gap=(1-B2)*lam2/(1+F(1,2500))
ok("gap exact", gap==F(2687,250100), gap)
ok("gap > 1/100", gap>F(1,100), gap)

results={
    "a": str(a),
    "L": str(L),
    "center_lower_decimal": f"{float(center_lo):.15f}",
    "endband_lower_decimal": f"{float(endband_lo):.15f}",
    "old_lambda2": str(old_lam2),
    "strengthened_constant": str(c),
    "lambda1": str(lam1),
    "lambda2": str(lam2),
    "B2_upper": str(B2),
    "gap": str(gap),
    "checks": len(checks),
}
Path("connected_387_1000_results.json").write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
for name in checks:
    print(f"PASS {name}")
print(f"TOTAL {len(checks)}")
