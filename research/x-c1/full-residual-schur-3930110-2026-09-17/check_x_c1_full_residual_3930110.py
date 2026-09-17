from fractions import Fraction as F
import json
from pathlib import Path

def Q(s): return F(s)
U={
'C':(Q('1.721783015631312581283784160551'),Q('1.721783015631312581283784160552')),
'M':(Q('0.315465625080952843258919237594'),Q('0.315465625080952843258919237595')),
'P':(Q('0.412222201868127728071463858814'),Q('0.412222201868127728071463858815')),
'lam':(Q('-0.052177701129694902683268810644'),Q('-0.052177701129694902683268810643')),
'del':(Q('0.531155632203638430650064522689'),Q('0.531155632203638430650064522690')),
'be':(Q('0.000375178861428239119741300041'),Q('0.000375178861428239119741300042')),
'bo':(Q('0.000041579088482741342782943617'),Q('0.000041579088482741342782943618')),
}
a=F(393011,1000000)
L=2*a

def exp_neg_iv(x,N=22):
    s=F(0); term=F(1); vals=[]
    for k in range(N+1):
        if k: term*=x/F(k)
        s += term if k%2==0 else -term
        vals.append(s)
    # alternating, x<2 here
    return (vals[N-1],vals[N]) if N%2==0 else (vals[N],vals[N-1])

def h_iv(t):
    qlo,qhi=exp_neg_iv(t/2)
    rlo,rhi=exp_neg_iv(2*t)
    return qlo/(1-rlo),qhi/(1-rhi)

def g_iv(t):
    lo,hi=h_iv(t)
    return lo-F(1,2*t), hi-F(1,2*t)

checks=[]
def ok(name,c,v=None):
    if not c: raise AssertionError((name,v))
    checks.append(name)

Cl,Ch=U['C']; Ml,Mh=U['M']; Pl,Ph=U['P']; ll,lh=U['lam']; dl,dh=U['del']; bel,beh=U['be']; bol,boh=U['bo']

# Recover h(L) and g(L) directly from certified lambda2,C intervals:
# lambda2 = 1 + L h(L) - C.
hL_lo=(ll+Cl-1)/L
hL_hi=(lh+Ch-1)/L
gL_lo=hL_lo-F(1,2*L)
gL_hi=hL_hi-F(1,2*L)

# One new elementary interval evaluation: g(L/2).
gH_lo,gH_hi=g_iv(L/2)
rhalf_lo=gH_lo-gL_hi
qgamma_lo=F(21,32)*L*rhalf_lo
ok('Gamma residual e2 floor > 1/100',qgamma_lo>F(1,100),qgamma_lo)

# Since g decreases on (0,2] and g(0+)=1/4:
# 0<=r(t)<=1/4-g(L). The graph Laplacian norm is <=2 L sup r.
Mgamma_hi=2*L*(F(1,4)-gL_lo)
ok('Gamma residual norm < 27/500',Mgamma_hi<F(27,500),Mgamma_hi)

# Allocate s=2/5 of the Gamma residual to the low mode.
s=F(2,5)
deltaG_lo=dl-s/(1-s)*Mgamma_hi
ok('Gamma-reduced tail > 99/200',deltaG_lo>F(99,200),deltaG_lo)

# Node split: rational theta=18/25 (not optimized; robust full-residual certificate).
theta=F(18,25)
mu_lo=theta*Ml; mu_hi=theta*Mh
ok('mu < deltaG/2',mu_hi<deltaG_lo/2,(mu_hi,deltaG_lo))

# Full residual Schur pivot. f(mu)=mu(1-mu/d) is increasing for mu<d/2.
node_lo=mu_lo*Pl*(1-mu_lo/deltaG_lo)
sigma_lo=ll+s*qgamma_lo+node_lo
ok('full residual Schur pivot > 1/500',sigma_lo>F(1,500),sigma_lo)

# Square completion / shear.
k_hi=mu_hi/deltaG_lo
eta_lo=sigma_lo/(1+k_hi)**2
ok('pre-moment full residual gap > 1/800',eta_lo>F(1,800),eta_lo)

# Gamma difference energy annihilates e0. Only the node theta-split pays moment penalty.
K_hi=Ch+theta/(1-theta)*Mh
num_lo=eta_lo-beh*K_hi
ok('post-moment numerator > 3/10000',num_lo>F(3,10000),num_lo)
G_lo=num_lo/(1+beh)
ok('full even source gap > 1/4000',G_lo>F(1,4000),G_lo)

# Odd remains strongly positive from imported scalar tail.
odd_lo=(ll+F(1,3)-(F(1,2)-ll)*boh)/(1+boh)
ok('odd source gap > 1/4',odd_lo>F(1,4),odd_lo)

res={
'a':'393011/1000000',
'gamma_e2_floor_decimal':f'{float(qgamma_lo):.15f}',
'gamma_norm_upper_decimal':f'{float(Mgamma_hi):.15f}',
'delta_gamma_lower_decimal':f'{float(deltaG_lo):.15f}',
'theta_node':'18/25',
'gamma_split':'2/5',
'full_schur_lower_decimal':f'{float(sigma_lo):.15f}',
'pre_moment_gap_lower_decimal':f'{float(eta_lo):.15f}',
'even_gap_lower_decimal':f'{float(G_lo):.15f}',
'odd_gap_lower_decimal':f'{float(odd_lo):.15f}',
'published_gap':'1/4000',
'checks':len(checks),
}
Path('full_residual_results.json').write_text(json.dumps(res,indent=2)+'\n')
for c in checks: print('PASS',c)
print('TOTAL',len(checks))
