from fractions import Fraction as F
import json
from pathlib import Path

def Q(s): return F(s)

# Directed outer intervals imported from the 80-digit evaluation step.
L={
'C':(Q('1.721780763071941330812018087086'),Q('1.721780763071941330812018087087')),
'M':(Q('0.315465754699270793738346419061'),Q('0.315465754699270793738346419062')),
'P':(Q('0.412221205211700601850984257149'),Q('0.412221205211700601850984257150')),
'lam':(Q('-0.052175515045093205960567162120'),Q('-0.052175515045093205960567162119')),
'del':(Q('0.531157818288240127372766171213'),Q('0.531157818288240127372766171214')),
'be':(Q('0.000375178095261906739617847774'),Q('0.000375178095261906739617847775')),
'bo':(Q('0.000041579003682082929495764460'),Q('0.000041579003682082929495764461')),
}
U={
'C':(Q('1.721783015631312581283784160551'),Q('1.721783015631312581283784160552')),
'M':(Q('0.315465625080952843258919237594'),Q('0.315465625080952843258919237595')),
'P':(Q('0.412222201868127728071463858814'),Q('0.412222201868127728071463858815')),
'lam':(Q('-0.052177701129694902683268810644'),Q('-0.052177701129694902683268810643')),
'del':(Q('0.531155632203638430650064522689'),Q('0.531155632203638430650064522690')),
'be':(Q('0.000375178861428239119741300041'),Q('0.000375178861428239119741300042')),
'bo':(Q('0.000041579088482741342782943617'),Q('0.000041579088482741342782943618')),
}

theta_test_lower=F(791438,1000000)
theta_bracket_lo=F(791428,1000000)
theta_bracket_hi=F(791429,1000000)

def eta_lower(v,t):
    Ml,Mh=v['M']; Pl,Ph=v['P']; ll,lh=v['lam']; dl,dh=v['del']
    mul,muh=t*Ml,t*Mh
    Slo=ll+mul*Pl-(muh*muh)*Ph/dl
    return min(Slo,dl)/(1+muh/dl)**2

def eta_upper(v,tlo,thi):
    Ml,Mh=v['M']; Pl,Ph=v['P']; ll,lh=v['lam']; dl,dh=v['del']
    mul,muh=tlo*Ml,thi*Mh
    Sup=lh+muh*Ph-(mul*mul)*Pl/dh
    return min(Sup,dh)/(1+mul/dh)**2

def G_lower(v,t):
    # Correct normalization:
    # G = (eta - beta*K)/(1+beta), K=C+theta/(1-theta)M.
    Cl,Ch=v['C']; Ml,Mh=v['M']; bl,bh=v['be']
    eta=eta_lower(v,t)
    Kup=Ch+t/(1-t)*Mh
    num=eta-bh*Kup
    return num/(1+bh) if num>=0 else num/(1+bl)

def G_upper(v,tlo,thi):
    Cl,Ch=v['C']; Ml,Mh=v['M']; bl,bh=v['be']
    eta=eta_upper(v,tlo,thi)
    Klo=Cl+tlo/(1-tlo)*Ml
    num=eta-bl*Klo
    return num/(1+bh) if num<0 else num/(1+bl)

def eta_prime_iv(v,t):
    Ml,Mh=v['M']; Pl,Ph=v['P']; ll,lh=v['lam']; dl,dh=v['del']
    Al,Ah=Ml*Pl,Mh*Ph; ql,qh=Ml/dh,Mh/dl
    nlo=Al-2*lh*ql-3*Ah*qh*t
    nhi=Ah-2*ll*qh-3*Al*ql*t
    return nlo/(1+qh*t)**3, nhi/(1+ql*t)**3

def Gp(v,t):
    # G_theta = (eta_theta - beta*M/(1-theta)^2)/(1+beta).
    Ml,Mh=v['M']; bl,bh=v['be']
    ep_l,ep_h=eta_prime_iv(v,t)
    nlo=ep_l-bh*Mh/(1-t)**2
    nhi=ep_h-bl*Ml/(1-t)**2
    vals=[nlo/(1+bl),nlo/(1+bh),nhi/(1+bl),nhi/(1+bh)]
    return min(vals),max(vals)

def odd_lower(v):
    ll,lh=v['lam']; bl,bh=v['bo']
    return (ll+F(1,3)-(F(1,2)-ll)*bh)/(1+bh)

checks=[]
def ok(name,cond,val):
    if not cond: raise AssertionError((name,val))
    checks.append(name)

glo=G_lower(L,theta_test_lower)
ok('corrected Gnode positive at a=0.3930108',glo>0,glo)

dL=Gp(U,theta_bracket_lo)
dU=Gp(U,theta_bracket_hi)
ok('corrected Gtheta positive at left bracket',dL[0]>0,dL)
ok('corrected Gtheta negative at right bracket',dU[1]<0,dU)

gup=G_upper(U,theta_bracket_lo,theta_bracket_hi)
ok('corrected Gnode negative at a=0.3930110',gup<0,gup)

Ml,Mh=U['M']; Pl,Ph=U['P']; ll,lh=U['lam']; dl,dh=U['del']
Al,Ah=Ml*Pl,Mh*Ph; ql,qh=Ml/dh,Mh/dl
conc=Ah*qh-Al+lh*ql
ok('eta concave',conc<0,conc)

odd=odd_lower(U)
ok('odd gap >1/4',odd>F(1,4),odd)

res={
    'a_lower':'3930108/10000000',
    'a_upper':'3930110/10000000',
    'lower_test_theta':str(theta_test_lower),
    'theta_bracket':[str(theta_bracket_lo),str(theta_bracket_hi)],
    'G_lower':str(glo),
    'G_upper':str(gup),
    'G_lower_decimal':f'{float(glo):.16g}',
    'G_upper_decimal':f'{float(gup):.16g}',
    'odd_lower':str(odd),
    'checks':len(checks),
    'normalization':'G=(eta-beta*K)/(1+beta)',
}
Path('node_schur_results.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
for c in checks: print('PASS',c)
print('TOTAL',len(checks))
