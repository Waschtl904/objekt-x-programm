"""Directed core quadrature error inventory for the frozen whole model.

The coarse Q8m contour bound is an explicit analytic obligation in the proof.
This file alone does not assert a complete residual comparison.
"""
import contextlib,io,json,time
from pathlib import Path
from flint import arb,acb,arb_poly,arb_series,ctx
HERE=Path(__file__).resolve().parent
code=(HERE/'whole_model_integrate.py').read_text()
with contextlib.redirect_stdout(io.StringIO()):exec(compile(code.split('cuts=[]')[0],str(HERE/'whole_model_integrate.py'),'exec'))
import fast_evaluation,taylor_model as tm
_fast=fast_evaluation.install(globals())
RADIUS=arb(2)
def peval_R(p,x):
    x=tm.jet(x);assert x.s.length()<=2
    co=p(arb_poly([x.s[0],x.s[1]]))
    bound=arb_poly([abs(v).upper()for v in co])(RADIUS).upper()
    return tm.Jet(arb_series(list(co)[:tm.Jet.N],prec=tm.Jet.N),acb(arb(0,bound),arb(0,bound)))
tm.peval=peval_R
corepan=[(lo,hi,128)for lo,hi in zip(edges[:-2],edges[1:-1])]
width=a-edges[-2]
corepan +=[(a-width*arb(2)**(-k),a-width*arb(2)**(-k-1),64)for k in range(48)]
nodesets={};position=0;Ec=arb(0);Eh=arb(0);Ehm=arb(0);Ehq=arb(0);rows=[]
for i,(lo,hi,n)in enumerate(corepan):
    mid=(lo+hi)/2;half=(hi-lo)/2
    tm.Jet.N=4;ctx.cap=4;RADIUS=arb(2)
    xx=tm.Jet(arb_series([mid,half],prec=4),acb(arb(mid,2*half.upper()),arb(0,2*half.upper())))
    # These n-point Gauss rules are controlled on the smaller rho=2 ellipse;
    # the radius-two circle rectangle used here is a conservative superset.
    hh=tm.hjet(globals(),xx);M=abs(hh.b).upper()
    gap=a-xx.b.real.upper();assert gap>0
    assert (b+abs(xx.b).upper())/2<q('11/10')
    error=8*(hi-lo)*M*arb(2)**(-2*n)
    # Complete X norm in the exterior for the singular and reflected kernels.
    # Integral_0^hs (u+gap)^-2 du <=1/gap; reflection is smaller.
    Ec+=error*(2/gap).sqrt()
    Eh+=error;Ehm+=2*error
    qmbound=1000000*(1+abs(gap.log()).upper())
    Ehq+=error*qmbound
    if n not in nodesets:nodesets[n]=[arb.legendre_p_root(n,k,weight=True)for k in range(n)]
    for z,wt in nodesets[n]:
        savedx,savedwh=hpoints[position];position+=1
        node=mid+half*z
        assert savedx.overlaps(node),'Cache does not use these core quadrature nodes'
        value=half*wt*hfun(res.cell(lo,hi),node)
        assert savedwh.overlaps(value),'Cached core quadrature value differs'
    rows.append({'index':i,'M':c.enc(M),'gap':c.enc(gap),'integral_error':c.enc(error)})
assert position==len(hpoints)
# The omitted core interval is smooth: the logarithmic h endpoint is at b>a.
d=width*arb(2)**(-48);half=d/2;mid=a-half
tm.Jet.N=8;ctx.cap=8;RADIUS=q('0.001')/half
xx=tm.Jet(arb_series([mid,half],prec=8),acb(arb(mid,q('0.001')),arb(0,q('0.001'))))
hh=tm.hjet(globals(),xx)
remainder=abs(hh.b).upper()*RADIUS**(-8)/(1-1/RADIUS)
htail=sum((abs(v).upper()for v in hh.s),arb(0))+remainder
tailnorm=htail*(2*d).sqrt()
Ec+=arb.pi()/2*tailnorm+htail*d/a*(2*hs).sqrt()/2
Eh+=htail*d;Ehm+=2*htail*d
# Real endpoint envelope |Q8m(a-v)|<=1000(1+|log v|), a deliberately
# separate obligation from the complex contour bound above.
Ehq+=1000*htail*d*(2-d.log())
regular=4*Eh*(2*hs).sqrt()
alpha=Eh/a
# Whole q-coupling of the moment direction, including the moment correction.
alpha_force=100*(2*mu).sqrt()*alpha
moment=((2*hs)**q('1/2'))*2/mu*(Ehm+Ehq/delta)
whole_X=(Ec+regular+alpha_force)/delta+moment
result={'status':'CORE_QUADRATURE_CONTROL_PENDING_QM_ENVELOPE_AUDIT',
        'bound_core_values_checked':position,'singular_X_error':c.enc(Ec),
        'regular_X_error':c.enc(regular),'mean_error':c.enc(Eh),
        'moment_h_error':c.enc(Ehm),'moment_Qm_h_error':c.enc(Ehq),
        'omitted_core_h_sup':c.enc(htail),'omitted_core_width':c.enc(d),
        'total_outer_X_error_upper_expression':c.enc(whole_X),
        'qm_contour_envelope':1000000,'qm_endpoint_envelope':1000,
        'whole_comparison_pass':False,'cells':rows}
(HERE/'core-quadrature-control-128.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:[float(q(x))for x in v]for k,v in result.items()if isinstance(v,list)and len(v)==2 and isinstance(v[0],str)},flush=True)
