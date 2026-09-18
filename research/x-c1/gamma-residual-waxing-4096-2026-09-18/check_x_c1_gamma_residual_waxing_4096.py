from fractions import Fraction as F

class IV:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=I(o); return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-I(o))
    def __rsub__(self,o): return I(o)-self
    def __mul__(self,o):
        o=I(o); v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return IV(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=I(o); assert not(o.lo<=0<=o.hi),(self,o)
        r=IV(min(F(1,o.lo),F(1,o.hi)),max(F(1,o.lo),F(1,o.hi)))
        return self*r
    def __rtruediv__(self,o): return I(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return IV(1)
        vals=[self.lo**n,self.hi**n]
        if self.lo<=0<=self.hi and n%2==0: vals.append(F(0))
        return IV(min(vals),max(vals))
    def __repr__(self): return f'IV({float(self.lo):.17g},{float(self.hi):.17g})'

def I(x): return x if isinstance(x,IV) else IV(x)
def Q(s): return F(s)
def V(lo,hi): return IV(Q(lo),Q(hi))
def maxabs(x): return max(abs(x.lo),abs(x.hi))

LOW={
'C':V('1.72654328889094193071858175195110154700017979343345704194828978346282270301','1.72654328889094193071858175195110154700017979343345704194828978346282330068'),
'm':V('0.315190590626732609430171211118178887037703442688184733896226032527774062822','0.315190590626732609430171211118178887037703442688184733896226032527774877833'),
'p':V('0.414327349890677255957350999638546642307296949254426580279463780839409602816','0.414327349890677255957350999638546642307296949254426580279463780839409965043'),
'lam':V('-0.0567969382597063248052499187490562068136126307073611395343736736985646120852','-0.0567969382597063248052499187490562068136126307073611395343736736985639781876'),
'd':V('0.52653639507362700852808341458427712651972070262597219379895965963476871823','0.526536395073627008528083414584277126519720702625972193798959659634769361183'),
'be':V('0.000376807704395315098733790881667764256041187534375031444530544694280817802756','0.000376807704395315098733790881667764256041187534375031444530544694280817829286'),
'bo':V('0.0000417593709753854398479256283180349429203156477820859772944089770629535957297','0.000041759370975385439847925628318034942920315647782085977294408977062953599046'),
'Q':V('0.0182733958633881039013846578959942104453388087348774098414132557352214556661','0.0182733958633881039013846578959942104453388087348774098414132557352221956849'),
'M':V('0.0449944300085997741250982118123989031657122403982152264469055146679739582558','0.0449944300085997741250982118123989031657122403982152264469055146679742163426'),
}
UP={
'C':V('1.72654887145926766457337442145817650014942051583127853744500294537239506074','1.72654887145926766457337442145817650014942051583127853744500294537239558597'),
'm':V('0.315190266770421226123695336788021828355393374132005360404243401265564667223','0.315190266770421226123695336788021828355393374132005360404243401265565482234'),
'p':V('0.414329817403246135801861183910594387989955658226063330602609472303288424276','0.414329817403246135801861183910594387989955658226063330602609472303288804615'),
'lam':V('-0.0568023547744245123058479475692426022382082406640920020687986260399777023274','-0.056802354774424512305847947569242602238208240664092002068798626039977122764'),
'd':V('0.526530978558908821027485385764090731095125092669241331264534707293355627987','0.526530978558908821027485385764090731095125092669241331264534707293356216606'),
'be':V('0.000376809626069892209767926614973727048385851334599535632976891341751913940206','0.000376809626069892209767926614973727048385851334599535632976891341751913953472'),
'bo':V('0.0000417595836679748474188208809371087186444850970223996074755847506117818302746','0.0000417595836679748474188208809371087186444850970223996074755847506117818330382'),
'Q':V('0.0182796427694371468682660311301989935540853388091756595298302210791229700498','0.0182796427694371468682660311301989935540853388091756595298302210791237004469'),
'M':V('0.0449945720610338497631486725566441301997254080885502423503034606216550976363','0.0449945720610338497631486725566441301997254080885502423503034606216553738345'),
}

# Current-head global-floor branch check on the whole a-bracket.
# This encloses C2-C0 = 2H(a)-H(2a-log2)-H(log2)+log2/sqrt2.
FLOOR_MARGIN=V('0.0520436221650845972134545268096180780386717667471842855160638480556220139273',
               '0.0520507126687685428925538047723673426588625534891447228457736313525217458215')

checks=[]
def ok(name,cond,val=None):
    if not cond: raise AssertionError((name,val))
    checks.append((name,val))

ok('current-head C2 node-floor branch active on full a-bracket',FLOOR_MARGIN.lo>0,FLOOR_MARGIN)

def core(v,s,th):
    s=I(s); th=I(th)
    D=v['d']-s/(1-s)*v['M']
    mu=th*v['m']
    N=v['lam']+s*v['Q']+mu*v['p']*(1-mu/D)
    R=1+mu/D
    eta=N/(R**2)
    K=v['C']+th/(1-th)*v['m']
    G=(eta-v['be']*K)/(1+v['be'])
    return D,mu,N,R,eta,K,G

def derivs(v,s,th):
    s=I(s); th=I(th)
    D,mu,N,R,eta,K,G=core(v,s,th)
    D1=-v['M']/(1-s)**2
    D2=-2*v['M']/(1-s)**3
    Ns=v['Q']+v['p']*(mu**2)*D1/(D**2)
    Nss=v['p']*(mu**2)*(D2/(D**2)-2*(D1**2)/(D**3))
    Nt=v['p']*v['m']*(1-2*mu/D)
    Ntt=-2*v['p']*(v['m']**2)/D
    Nst=2*v['p']*mu*v['m']*D1/(D**2)
    Rs=-mu*D1/(D**2)
    Rss=-mu*(D2/(D**2)-2*(D1**2)/(D**3))
    Rt=v['m']/D
    Rtt=I(0)
    Rst=-v['m']*D1/(D**2)
    def eta2(Nij,Ni,Nj,Ri,Rj,Rij):
        return Nij/(R**2)-2*Ni*Rj/(R**3)-2*Nj*Ri/(R**3)+6*N*Ri*Rj/(R**4)-2*N*Rij/(R**3)
    etas=Ns/(R**2)-2*N*Rs/(R**3)
    etat=Nt/(R**2)-2*N*Rt/(R**3)
    etass=eta2(Nss,Ns,Ns,Rs,Rs,Rss)
    etast=eta2(Nst,Ns,Nt,Rs,Rt,Rst)
    etatt=eta2(Ntt,Nt,Nt,Rt,Rt,Rtt)
    Gs=etas/(1+v['be'])
    Gt=(etat-v['be']*v['m']/(1-th)**2)/(1+v['be'])
    Gss=etass/(1+v['be'])
    Gst=etast/(1+v['be'])
    Gtt=(etatt-2*v['be']*v['m']/(1-th)**3)/(1+v['be'])
    return G,Gs,Gt,Gss,Gst,Gtt,N,D

def odd_gap(v):
    return (v['lam']+F(1,3)-(F(1,2)-v['lam'])*v['bo'])/(1+v['bo'])

# Lower endpoint: explicit positive split.
sL=F(63597,125000)       # 0.508776
thL=F(1459223,2000000)  # 0.7296115
Dlow,mulow,Nlow,Rlow,etalow,Klow,GL=core(LOW,sL,thL)
ok('lower reduced tail D > 0',Dlow.lo>0,Dlow)
ok('lower Schur pivot > 0',Nlow.lo>0,Nlow)
ok('lower Schur pivot < D', (Nlow-Dlow).hi<0,Nlow-Dlow)
ok('lower endpoint fixed split G > 1/1,500,000',GL.lo>F(1,1_500_000),GL)
ok('lower endpoint odd gap > 1/4',odd_gap(LOW).lo>F(1,4),odd_gap(LOW))

# Upper endpoint: first exclude s outside [0.15,0.7] using sigma <= L+pD/4.
def Fmax(v,s):
    s=I(s); D=v['d']-s/(1-s)*v['M']
    return v['lam']+s*v['Q']+v['p']*D/4

def Fprime(v,s):
    s=I(s); return v['Q']-v['p']*v['M']/(4*(1-s)**2)

slo=F(3,20); shi=F(7,10)
ok('Fmax increasing on s<=0.15',Fprime(UP,slo).lo>0,Fprime(UP,slo))
ok('Fmax(0.15)<0',Fmax(UP,slo).hi<0,Fmax(UP,slo))
ok('Fmax decreasing on s>=0.7',Fprime(UP,shi).hi<0,Fprime(UP,shi))
ok('Fmax(0.7)<0',Fmax(UP,shi).hi<0,Fmax(UP,shi))

max_fminusd=F(-10**9)
for i in range(80):
    a=slo+(shi-slo)*F(i,80); b=slo+(shi-slo)*F(i+1,80)
    S=IV(a,b); D=UP['d']-S/(1-S)*UP['M']
    max_fminusd=max(max_fminusd,(Fmax(UP,S)-D).hi)
ok('sigma<D for all theta on central s-strip',max_fminusd<0,max_fminusd)

# On central s-strip, low theta <=0.55: D >= 2*(0.55)m, hence sigma increases in theta;
# certify sigma(s,0.55)<0 by exact interval cells.
thlow=F(11,20)
D_at_hi=(UP['d']-I(shi)/(1-I(shi))*UP['M'])
ok('central strip D >= 1.1m',D_at_hi.lo>(F(11,10)*UP['m']).hi,(D_at_hi,UP['m']))
lowtheta_max=F(-10**9)
Ncells=40
for i in range(Ncells):
    a=slo+(shi-slo)*F(i,Ncells); b=slo+(shi-slo)*F(i+1,Ncells)
    N=core(UP,IV(a,b),thlow)[2]
    if N.hi>lowtheta_max: lowtheta_max=N.hi
ok('sigma<0 for theta<=0.55 on central strip',lowtheta_max<0,lowtheta_max)

# Central rectangle R=[0.15,0.7]x[0.55,0.95]: exact interval Hessian certificate.
thhi=F(19,20)
worst_gss=F(-10**9); worst_det=F(10**9); worst_NminusD=F(-10**9)
NS=40; NT=40
for i in range(NS):
    sa=slo+(shi-slo)*F(i,NS); sb=slo+(shi-slo)*F(i+1,NS)
    for j in range(NT):
        ta=thlow+(thhi-thlow)*F(j,NT); tb=thlow+(thhi-thlow)*F(j+1,NT)
        G,Gs,Gt,Gss,Gst,Gtt,N,D=derivs(UP,IV(sa,sb),IV(ta,tb))
        det=Gss*Gtt-Gst**2
        worst_gss=max(worst_gss,Gss.hi)
        worst_det=min(worst_det,det.lo)
        worst_NminusD=max(worst_NminusD,(N-D).hi)
ok('sigma<D throughout central rectangle',worst_NminusD<0,worst_NminusD)
ok('G_ss<0 throughout central rectangle',worst_gss<0,worst_gss)
ok('Hessian determinant >0 throughout central rectangle',worst_det>0,worst_det)

# Concavity tangent at near-maximizer.
s0=F(5088559,10_000_000)    # 0.5088559
th0=F(7295959,10_000_000)   # 0.7295959
G0,Gs0,Gt0,*_=derivs(UP,s0,th0)
ds=max(abs(s0-slo),abs(shi-s0)); dt=max(abs(th0-thlow),abs(thhi-th0))
tangent_upper=G0.hi+maxabs(Gs0)*ds+maxabs(Gt0)*dt
ok('concavity tangent upper < -1/4,000,000',tangent_upper < -F(1,4_000_000),tangent_upper)

# For theta>=0.95: show G_theta(0.95)<0 on s-strip and G_theta is strictly decreasing.
max_Gt95=F(-10**9); max_cond=F(-10**9)
for i in range(40):
    sa=slo+(shi-slo)*F(i,40); sb=slo+(shi-slo)*F(i+1,40)
    S=IV(sa,sb)
    G,Gs,Gt,Gss,Gst,Gtt,N,D=derivs(UP,S,thhi)
    max_Gt95=max(max_Gt95,Gt.hi)
    # eta_tt sign condition at theta=1: A q - A + L q <0
    q=UP['m']/D; A=UP['m']*UP['p']; L0=UP['lam']+S*UP['Q']
    cond=A*q-A+L0*q
    max_cond=max(max_cond,cond.hi)
ok('G_theta(s,0.95)<0',max_Gt95<0,max_Gt95)
ok('eta_theta_theta<0 for theta>=0.95',max_cond<0,max_cond)

# Odd remains nonlimiting at upper endpoint.
ok('upper endpoint odd gap >1/4',odd_gap(UP).lo>F(1,4),odd_gap(UP))

import json
from pathlib import Path

def fnum(x):
    if isinstance(x,IV): return {'lo':f'{float(x.lo):.18g}','hi':f'{float(x.hi):.18g}'}
    return f'{float(x):.18g}'

results={
  'N':4096,
  'node_floor_C2_minus_C0':fnum(FLOOR_MARGIN),
  'a_lower':'3934355/10000000',
  'a_upper':'3934360/10000000',
  'lower_split_s':str(sL),
  'lower_split_theta':str(thL),
  'lower_even_gap':fnum(GL),
  'published_lower_gap':'1/1500000',
  'upper_tangent_point_s':str(s0),
  'upper_tangent_point_theta':str(th0),
  'upper_tangent_bound':f'{float(tangent_upper):.18g}',
  'upper_q_riemann':'left-endpoint upper sum q_4096_plus',
  'lower_q_riemann':'right-endpoint lower sum q_4096_minus',
  'worst_Gss_upper':f'{float(worst_gss):.18g}',
  'worst_Hessian_det_lower':f'{float(worst_det):.18g}',
  'max_Gtheta_at_095_upper':f'{float(max_Gt95):.18g}',
  'odd_lower':fnum(odd_gap(LOW)),
  'odd_upper':fnum(odd_gap(UP)),
  'checks':len(checks),
}
Path('gamma_residual_waxing_4096_results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
for name,val in checks:
    if isinstance(val,IV): out=(float(val.lo),float(val.hi))
    else:
        try: out=float(val)
        except: out=val
    print('PASS',name,out)
print('TOTAL',len(checks))
print('LOW_G',float(GL.lo),float(GL.hi))
print('UP_TANGENT',float(tangent_upper))
print('WORST_GSS',float(worst_gss),'WORST_DET',float(worst_det))
print('MAX_Gt95',float(max_Gt95),'MAX_COND',float(max_cond))
