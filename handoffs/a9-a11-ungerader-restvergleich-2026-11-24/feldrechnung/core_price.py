"""Enclose the model change from continuous h to the 64/32-node inner Gauss measure."""
from pathlib import Path
import sys
# Share the parity-checked, source-bound field and signed analytic h evaluator.
code=Path(__file__).with_name('panels.py').read_text(encoding='utf8')
exec(compile(code[:code.index('cuts=list(res.cuts)')],str(Path(__file__).with_name('panels.py')),'exec'))
from math import factorial

mc=arb_poly([(a/2)**k/factorial(k) if k%2==1 else arb(0) for k in range(161)])
mls=[arb(0)]*161;mdh=arb_poly([])
for n in range(1,161,2):
    mls[n]=(2*n+1)*c.pint(mc*leg[n])
    mdh+=leg[n]*(mls[n]*harm[n])
qms=mdh+mc*(-(2*arb.pi()*a).log()-arb.const_euler())-of.kernel(mc,mls,a,gamma,1)
def coeff_abs(p,rad):
    return sum((abs(v).upper()*rad**k for k,v in enumerate(p)),arb(0))
qr=q('1.2')
assert coeff_abs(qms,qr)<100 and coeff_abs(mc,qr)<3
assert coeff_abs(arb_poly(gamma),q('1.1'))<2
prime=sum((2*w for _,w in channels),arb(0))
assert prime<12
# At most two real reflected logs in qm on the core. On the ellipse
# |y/a|<=1.2 and Re(y)>-a/2, |Log(1+-y/a)|<=5+|log(gap)|.
# Every active shifted polynomial may be extended a little beyond the cut.
max_shifted_ratio=q(3)
assert coeff_abs(mc,max_shifted_ratio)<4
def refined_h_bound(left,right):
    mid=(left+right)/2
    half=(right-left)/2
    # The selected cell defines an analytic expression across its prime cuts.
    # Keep the larger rectangle before the first outer logarithmic endpoint.
    radius=min(q(4),(res.a-mid)/(half*2))
    assert radius>2
    def peval(p,x):
        x=tm.jet(x)
        pol=p(arb_poly([x.s[0],x.s[1]]))
        bound=coeff_abs(pol,radius)
        return tm.Jet(arb_series(list(pol)[:tm.Jet.N],prec=tm.Jet.N),
                      acb(arb(0,bound),arb(0,bound)))
    tm.peval=peval
    tm.Jet.N=128;ctx.cap=128
    xx=tm.Jet(arb_series([mid,half],prec=128),acb(arb(mid,radius*half.upper()),arb(0,radius*half.upper())))
    hh=tm.hjet(globals(),xx)
    assert hh.s.prec>=127
    ratio=2/radius
    return coeff_abs(hh.s,arb(2))+abs(hh.b).upper()*ratio**hh.s.prec/(1-ratio)

pan=[(l,r,64) for l,r in zip(edges[:-2],edges[1:-1])]
width=a-edges[-2]
pan += [(a-width*arb(2)**(-k),a-width*arb(2)**(-k-1),32) for k in range(48)]
Eh=arb(0);Ec=arb(0);Ehm=arb(0);Ehq=arb(0);Ealpha=arb(0)
index=0;Gauss={}
for left,right,n in pan:
    mid=(left+right)/2;half=(right-left)/2
    M=refined_h_bound(left,right)
    gap=a-mid-2*half
    assert gap>0
    yy=acb(arb(mid,2*half.upper()),arb(0,2*half.upper()))
    assert abs(yy).upper()<qr*a and yy.real.lower()>-a/2
    assert (b+abs(yy).upper())/2<q("1.1")
    assert all((abs(yy).upper()+abs(sh))<max_shifted_ratio*a for sh,_ in channels)
    # The numerator bounds refer to the radius-two disk; Bernstein ellipse
    # rho=2 is contained in that disk. The analytic Gauss error is then
    # bounded by 8*length*sup*2^(-2n).
    error=8*(right-left)*M*arb(2)**(-2*n)
    Eh+=error; Ec+=error*(2/gap).sqrt(); Ehm+=2*error
    Ehq+=error*1000*(1+abs(gap.log()).upper())
    Ealpha+=qr*error
    if n not in Gauss: Gauss[n]=[arb.legendre_p_root(n,j,weight=True) for j in range(n)]
    fn=res.cell(left,right)
    for t,wt in Gauss[n]:
        y,hwt=hpoints[index];index+=1
        actual=mid+half*t
        assert y.overlaps(actual) and hwt.overlaps(half*wt*hfun(fn,actual))
assert index==len(hpoints)
dtail=width*arb(2)**(-48)
Mt=refined_h_bound(a-dtail,a)
Ec+=arb.pi()/2*Mt*(2*dtail).sqrt()+Mt*dtail/a*(2*hs).sqrt()/2
Eh+=Mt*dtail; Ehm+=2*Mt*dtail; Ealpha+=Mt*dtail
Ehq+=1000*Mt*dtail*(2-dtail.log())
alpha=Ealpha*(6/a).sqrt()/((6*a).sqrt()*c.mellin(1,a))
outer_m=((b.sinh()-a.sinh()-hs)).sqrt()
# A bound for the coefficient of the alpha correction in the finite
# Gamma224 model. Its direct cross operator costs <12 and the physical
# moment correction uses integral of m160*qm, where ||qm||<100 as below.
cross=arb.pi()/2+(hs/a).sqrt()/2+4*(hs*a).sqrt()+prime
m_sup=coeff_abs(mc,arb(1))
assert m_sup<1 and cross<15
# For log(1-t) and log(1+t) on [0,1], use sqrt(2) and log(2).
qmL2=(2*a).sqrt()*(coeff_abs(qms,arb(1))+m_sup*(arb(2).sqrt()+arb(2).log())/2+prime*m_sup)
assert qmL2<100
mnorm=(2*a).sqrt()*m_sup
alpha_cost=(cross+outer_m*qmL2/(2*mu))*mnorm*alpha
regular=4*Eh*(2*hs).sqrt()
cost=(Ec+regular+alpha_cost)/delta+outer_m/mu*(Ehm+Ehq/delta)
result={"core_atoms":index,"whole_outer_X_upper":c.enc(cost)[1],"dual_norm_upper":c.enc((q('5/21')).sqrt()*cost)[1],
        "core_tail_sup":c.enc(Mt)[1],"whole_residual_certified":False}
args.output.write_text(json.dumps(result,indent=2),encoding="utf8")
print("CORE PRICE",float(cost.upper()),"dual",float(((q('5/21')).sqrt()*cost).upper()),"tail sup",float(Mt.upper()),flush=True)
