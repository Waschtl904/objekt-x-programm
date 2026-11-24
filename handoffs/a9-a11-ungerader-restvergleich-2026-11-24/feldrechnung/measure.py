"""Integrate the joint odd field at fixed nodes and compare its independent 84 coordinates."""
import json
from flint import arb, arb_mat, arb_poly


def measure(ns, edges, order, rescaled_parts):
    a,b,hs,mid,half=(ns[k] for k in ("a","b","hs","mid","half"))
    c,res,leg,J,Y=(ns[k] for k in ("c","res","leg","J","Y"))
    e,w,coeff=ns["e"],ns["w"],ns["coeff"]
    q=c.q
    direct_lo=c.mat(ns["case"]["D96_lower_model"]); direct_up=c.mat(ns["case"]["D96_upper_model"])
    gram=c.mat(ns["case"]["U96_model"])
    inds=range(12,96)
    dj=arb_mat([[(direct_lo[i,j]+direct_up[i,j])/2 for j in inds] for i in inds])
    uj=arb_mat([[gram[i,j] for j in inds] for i in inds])
    nref=e.nu*coeff-(dj-uj-e.w["a"].transpose()*e.w["Ki"]*e.w["a"])*w+q("1e-10")*dj*w
    span=arb_mat(96,12)
    for j,(p,_) in enumerate(ns["zp"]):
        loc=p(arb_poly([mid/b,half/b]))
        for n in range(len(loc)):
            span[n,j]=(hs*(2*n+1)/2).sqrt()*c.pint(loc*leg[n],arb(-1),arb(1))
    for n in range(96):
        for j in range(8): span[n,j+4]=Y[n,j]
    lam=arb_mat([[(hs*(2*n+1)/2).sqrt()*c.mellin(n,hs/2)*((mid/2).sinh() if n%2==0 else (mid/2).cosh())] for n in range(96)])
    lm=span.transpose()*lam
    gramS=span.transpose()*span+2/ns["mu"]*lm*lm.transpose()
    panels=[]
    for i,(left,right) in enumerate(zip(edges[:-1],edges[1:])):
        if i in (0,len(edges)-2):
            pts=[left+(right-left)/2**k if i==0 else right-(right-left)/2**k for k in range(1,rescaled_parts+1)]
            pts=[left]+(pts[::-1] if i==0 else pts)+[right]
            panels.extend(zip(pts[:-1],pts[1:]))
        else: panels.append((left,right))
    moments=arb_mat(96,1); raw=arb(0); mr=arb(0)
    scales=[(arb(2*n+1)/(2*hs)).sqrt() for n in range(96)]
    for i,(left,right) in enumerate(panels):
        for t,wt in ns["gauss"](order):
            x=(right+left+(right-left)*t)/2
            rr=ns["outer_value"](x)
            assert rr.is_finite()
            fac=(right-left)*wt*rr
            raw+=fac*rr; mr+=fac*res.m(x)
            s=(x-mid)/half
            p=[arb(1),s]
            for n in range(1,95): p.append(((2*n+1)*s*p[-1]-n*p[-2])/(n+1))
            for n in range(96): moments[n,0]+=fac*scales[n]*p[n]
    rspan=span.transpose()*moments
    projected=raw-mr**2/(2*res.mu)-(rspan.transpose()*gramS.solve(rspan))[0,0]
    rj=J.transpose()*moments
    discrepancy=rj-nref
    return dict(nodes=order,panels=len(panels),raw_model_X_squared=float(raw.mid()),
                projected_model_Wdual_squared=float(projected.mid()),
                projected_model_RL_upper_expression=float((projected*5/21).mid()),
                norm_P_feature_mismatch=float(ns["quad"](e.w["P"],discrepancy).sqrt().mid()),
                full_84_mismatch=float(c.norm(discrepancy).mid()))
