from fractions import Fraction as F
import json
from pathlib import Path

def Q(s): return F(s)
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
tL=F(791438,1000000); tU=F(791439,1000000)

def G_lower(v,t):
    Cl,Ch=v['C']; Ml,Mh=v['M']; Pl,Ph=v['P']; ll,lh=v['lam']; dl,dh=v['del']; bl,bh=v['be']
    mul,muh=t*Ml,t*Mh
    Slo=ll+mul*Pl-(muh*muh)*Ph/dl
    eta=min(Slo,dl)/(1+muh/dl)**2
    pen=(bh/(1+bh))*(Ch+t/(1-t)*Mh)
    return eta-pen

def G_upper(v,tlo,thi):
    Cl,Ch=v['C']; Ml,Mh=v['M']; Pl,Ph=v['P']; ll,lh=v['lam']; dl,dh=v['del']; bl,bh=v['be']
    mul,muh=tlo*Ml,thi*Mh
    Sup=lh+muh*Ph-(mul*mul)*Pl/dh
    eta=min(Sup,dh)/(1+mul/dh)**2
    pen=(bl/(1+bl))*(Cl+tlo/(1-tlo)*Ml)
    return eta-pen

def Gp(v,t):
    Ml,Mh=v['M']; Pl,Ph=v['P']; ll,lh=v['lam']; dl,dh=v['del']; bl,bh=v['be']
    Al,Ah=Ml*Pl,Mh*Ph; ql,qh=Ml/dh,Mh/dl
    nlo=Al-2*lh*ql-3*Ah*qh*t
    nhi=Ah-2*ll*qh-3*Al*ql*t
    ep_l=nlo/(1+qh*t)**3; ep_h=nhi/(1+ql*t)**3
    return ep_l-(bh/(1+bh))*Mh/(1-t)**2, ep_h-(bl/(1+bl))*Ml/(1-t)**2

def odd_lower(v):
    ll,lh=v['lam']; bl,bh=v['bo']
    return (ll+F(1,3)-(F(1,2)-ll)*bh)/(1+bh)

checks=[]
def ok(name,cond,val):
    if not cond: raise AssertionError((name,val))
    checks.append(name)

glo=G_lower(L,tL); ok('Gnode positive at a=0.3930108',glo>0,glo)
dL=Gp(U,tL); dU=Gp(U,tU)
ok('Gtheta positive at left bracket',dL[0]>0,dL)
ok('Gtheta negative at right bracket',dU[1]<0,dU)
gup=G_upper(U,tL,tU); ok('Gnode negative at a=0.3930110',gup<0,gup)
Ml,Mh=U['M']; Pl,Ph=U['P']; ll,lh=U['lam']; dl,dh=U['del']
Al,Ah=Ml*Pl,Mh*Ph; ql,qh=Ml/dh,Mh/dl
conc=Ah*qh-Al+lh*ql; ok('eta concave',conc<0,conc)
odd=odd_lower(U); ok('odd gap >1/4',odd>F(1,4),odd)
res={'a_lower':'3930108/10000000','a_upper':'3930110/10000000','theta_bracket':[str(tL),str(tU)],'G_lower':str(glo),'G_upper':str(gup),'odd_lower':str(odd),'checks':len(checks)}
Path('node_schur_results.json').write_text(json.dumps(res,indent=2)+'\n')
for c in checks: print('PASS',c)
print('TOTAL',len(checks))
