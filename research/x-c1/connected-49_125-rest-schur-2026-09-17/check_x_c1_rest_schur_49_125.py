#!/usr/bin/env python3
from fractions import Fraction as F
import json
from pathlib import Path

checks=[]
def ok(name, cond, value=None):
    if not cond:
        raise AssertionError(f"{name}: {value!r}")
    checks.append(name)

def exp_neg_iv(x,N=24):
    s=F(0); term=F(1); sums=[]
    for k in range(N+1):
        if k==0: term=F(1)
        else: term*=x/F(k)
        s += term if k%2==0 else -term
        sums.append(s)
    return (sums[N-1],sums[N]) if N%2==0 else (sums[N],sums[N-1])

def atanh_iv(t,N=24):
    s=F(0)
    for n in range(N):
        s += t**(2*n+1)/F(2*n+1)
    tail=t**(2*N+1)/F(2*N+1)/(1-t*t)
    return s,s+tail

def log2_iv(N=24):
    lo,hi=atanh_iv(F(1,3),N)
    return 2*lo,2*hi

def log_iv(x,N=24):
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

def atan_iv(x,N=14):
    s=F(0); vals=[]
    for n in range(N):
        s += (-1)**n*x**(2*n+1)/F(2*n+1)
        vals.append(s)
    return min(vals[-1],vals[-2]),max(vals[-1],vals[-2])

def pi_iv():
    a1lo,a1hi=atan_iv(F(1,5),16)
    a2lo,a2hi=atan_iv(F(1,239),8)
    return 16*a1lo-4*a2hi,16*a1hi-4*a2lo

def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))

def gamma_iv(n=50):
    lnlo,lnhi=log_iv(F(n))
    lo=harmonic(n)-lnhi-F(1,2*n)+F(1,12*n*n)-F(1,120*n**4)
    hi=harmonic(n)-lnlo-F(1,2*n)+F(1,12*n*n)-F(1,120*n**4)+F(1,252*n**6)
    return lo,hi

def H_iv(s):
    qlo,qhi=exp_neg_iv(s/2)
    ratio_lo=(1+qlo)/(1-qlo); ratio_hi=(1+qhi)/(1-qhi)
    llo,_=log_iv(ratio_lo); _,lhi=log_iv(ratio_hi)
    pilo,pihi=pi_iv()
    rlo=(1-qhi)/(1+qhi); rhi=(1-qlo)/(1+qlo)
    arlo,_=atan_iv(rlo,12); _,arhi=atan_iv(rhi,12)
    return llo/2+pilo/4-arhi, lhi/2+pihi/4-arlo

def h_iv(t):
    qlo,qhi=exp_neg_iv(t/2)
    rlo,rhi=exp_neg_iv(2*t)
    return qlo/(1-rlo),qhi/(1-rhi)

def kappa_iv():
    pilo,pihi=pi_iv(); glo,ghi=gamma_iv(50)
    loglo,_=log_iv(8*pilo); _,loghi=log_iv(8*pihi)
    return loglo+glo+pilo/2,loghi+ghi+pihi/2

def H_arg_iv(slo,shi):
    # H is strictly decreasing.
    lo,_=H_iv(shi)
    _,hi=H_iv(slo)
    return lo,hi

a=F(49,125)
L=2*a
ell_lo,ell_hi=log2_iv()

# Tight rational enclosure of sqrt(2), checked algebraically.
sq_lo=F(1414213,10**6)
sq_hi=F(1414214,10**6)
ok("sqrt2 lower square < 2", sq_lo*sq_lo<2)
ok("sqrt2 upper square > 2", sq_hi*sq_hi>2)
w_lo=ell_lo/sq_hi
w_hi=ell_hi/sq_lo

d_lo=L-ell_hi
d_hi=L-ell_lo
Hd_lo,Hd_hi=H_arg_iv(d_lo,d_hi)
Hell_lo,Hell_hi=H_arg_iv(ell_lo,ell_hi)
kappa_lo,kappa_hi=kappa_iv()

# Exact global node floor on this window:
# C = kappa_* + w_2 - H(L-log2) - H(log2).
C_lo=kappa_lo+w_lo-Hd_hi-Hell_hi
C_hi=kappa_hi+w_hi-Hd_lo-Hell_lo
ok("C < 1711/1000", C_hi<F(1711,1000), C_hi)

# Check that the active-endband floor is indeed no larger than the center floor.
Ha_lo,Ha_hi=H_iv(a)
center_minus_end_lo=2*Ha_lo-Hd_hi-Hell_hi+w_lo
ok("center node level above endband floor", center_minus_end_lo>0, center_minus_end_lo)

# On the outer halves of the active endbands, |x|>=log2/2.
# V(x)=rho(x)+C is increasing there; its minimum is at x=log2/2.
s1_lo=(L+ell_lo)/2; s1_hi=(L+ell_hi)/2
s2_lo=(L-ell_hi)/2; s2_hi=(L-ell_lo)/2
H1_lo,H1_hi=H_arg_iv(s1_lo,s1_hi)
H2_lo,H2_hi=H_arg_iv(s2_lo,s2_hi)
Vmid_lo=H1_lo+H2_lo-Hd_hi-Hell_hi
ok("outer-half node surplus > 3/10", Vmid_lo>F(3,10), Vmid_lo)

# Maximal constant gamma floor c(a)=g(L) gives lambda_2=1+L*h(L)-C.
hL_lo,hL_hi=h_iv(L)
lambda2_lo=F(1)+L*hL_lo-C_hi
lambda2_hi=F(1)+L*hL_hi-C_lo
ok("lambda2 > -21/500", lambda2_lo>-F(21,500), lambda2_lo)
# lambda_4-lambda_2=1/3+1/4=7/12.
ok("even tail floor > 27/50", lambda2_lo+F(7,12)>F(27,50), lambda2_lo+F(7,12))
# lambda_3-lambda_2=1/3.
ok("odd tail floor > 437/1500", lambda2_lo+F(1,3)>F(437,1500), lambda2_lo+F(1,3))
# lambda_1=lambda_2-1/2, so its negative magnitude is <271/500.
ok("odd low-mode magnitude < 271/500", -(lambda2_lo-F(1,2))<F(271,500), -(lambda2_lo-F(1,2)))

# Outer-slab mass of normalized e_2.  With z0=log2/L,
# p=5 int_{z0}^1 P_2(z)^2 dz.
z_hi=ell_hi/L
p_lo=F(1)-F(9,4)*z_hi**5+F(5,2)*z_hi**3-F(5,4)*z_hi
ok("outer-slab P2 mass > 2/5", p_lo>F(2,5), p_lo)

# Moment reconstruction bounds inherited in form, rechecked at a=49/125.
z=a/2
cosh_rel=z*z/(2*(1-z*z/F(12)))
sinh_rel=z*z/(6*(1-z*z/F(20)))
ok("even moment ratio < 1/50", cosh_rel<F(1,50), cosh_rel)
ok("odd moment ratio < 1/150", sinh_rel<F(1,150), sinh_rel)

# Pure rational Schur budget.
m=F(3,10)
mu=m/2
delta=F(27,50)
lam2_floor=-F(21,500)
p_floor=F(2,5)
# D>=delta I and ||P_tail P_J e2||^2 <= p imply
# Schur >= lambda2 + mu*p*(1-mu/delta).
s0=lam2_floor+mu*p_floor*(1-mu/delta)
ok("even Schur scalar = 1/750", s0==F(1,750), s0)
# The LDL shear has norm <=1+k with k<=mu/delta=5/18.
k=mu/delta
ok("Schur shear = 5/18", k==F(5,18), k)
eta=s0/(1+k)**2
ok("pre-moment even gap = 54/66125", eta==F(54,66125), eta)

# The node inequality costs an extra m|u0|^2; C<1711/1000.
moment_penalty=(F(1711,1000)+m)*F(1,2500)
even_high_gap=eta-moment_penalty
ok("even high gap positive", even_high_gap>0, even_high_gap)
even_source_gap=even_high_gap/(1+F(1,2500))
ok("even source gap > 1/100000", even_source_gap>F(1,100000), even_source_gap)

# Odd sector does not need the node rescue.
odd_tail=F(437,1500)
odd_penalty=F(271,500)*F(1,22500)
odd_source_gap=(odd_tail-odd_penalty)/(1+F(1,22500))
ok("odd source gap > 1/4", odd_source_gap>F(1,4), odd_source_gap)

results={
    "a": str(a),
    "C_upper_decimal": f"{float(C_hi):.15f}",
    "center_minus_end_lower_decimal": f"{float(center_minus_end_lo):.15f}",
    "outer_node_surplus_lower_decimal": f"{float(Vmid_lo):.15f}",
    "lambda2_lower_decimal": f"{float(lambda2_lo):.15f}",
    "outer_P2_mass_lower_decimal": f"{float(p_lo):.15f}",
    "even_gap": str(even_source_gap),
    "odd_gap": str(odd_source_gap),
    "published_gap": "1/100000",
    "checks": len(checks),
}
Path("rest_schur_49_125_results.json").write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
for name in checks:
    print("PASS",name)
print("TOTAL",len(checks))
