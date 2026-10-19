"""Common cell integration of all twelve residuals and 287 old source fields.

Gauss errors use an analytic rho=2 ellipse, not mesh differences. Logarithmic
endpoint tails are retained. Regular-kernel and old finite-model errors are
separate from these integration enclosures.
"""
import argparse
import json
import time
from pathlib import Path
from flint import arb, acb, arb_poly, arb_mat, ctx
from common import Inputs, Poly, columns, encode, need, pad, q, mat
from residuals import Residuals
from old_fields import OldFields
from source_bounds import SourceBounds
from checkpoint import Checkpoint


def ellipse(lo,hi):
    c=(lo+hi)/2;d=(hi-lo)/2
    return acb(arb(c,d.upper()*5/4),arb(0,d.upper()*3/4))


def cheb_error(lo,hi,n):
    # Polynomial exactness through 2n-1 and the Chebyshev series tail.
    return 8*(hi-lo)*arb(2)**(-2*n)


def outer(a,b):
    return arb_mat([[x*y for y in b] for x in a])


def powers(x,n):
    out=[arb(1)]
    for _ in range(1,n):out.append(out[-1]*x)
    return out


def absolute_poly(f,radius):
    return sum((abs(v).upper()*radius**k for k,v in enumerate(f)),arb(0)).upper()


def endpoint_residual_bounds(res):
    """|r_j(a-u)| <= A_j |log u| + B_j, 0<u<min(h,1/100)."""
    a,b=res.a,res.b
    em=(b/2).exp();A=[];B=[]
    for j in range(12):
        en=absolute_poly(res.ell[j].p,b)
        dv=absolute_poly(res.Dv[j].p,arb(1))
        dp=absolute_poly(res.Dpoly[j],arb(1))
        for i,fj in enumerate(res.funcs):
            for term in fj['D']['shift_terms']:
                dp+=abs(res.T[i,j]).upper()*absolute_poly(arb_poly(list(map(q,term['polynomial']))),arb(1))
        prim=sum((2*arb(prime).log()/arb(n).sqrt()*(abs(res.Ac[j]).upper()*em+en)
                  for n,prime in res.channels),arb(0))
        A.append((en+abs(res.Ac[j]).upper()*em+dv/(2*a).sqrt())/2)
        # jp/jm regular parts at u=0 are bounded by 3, the far arguments by 4;
        # hence the moment-source regular part is bounded by 20 exp(b/2).
        B.append(20*em*abs(res.Ac[j]).upper()+en*(abs(res.h.log()).upper()+4)+
                 absolute_poly(res.quot[j].p,b)+absolute_poly(res.gamma[j].p,b)+prim+
                 (dp+2*dv+abs(res.Dm[j]).upper()*em)/(2*a).sqrt())
    return A,B


def run(parity,output,ncore=64,ntail=16,panels=200,work=None,stop_after=None):
    need(parity in ('even','odd'),'Unknown parity')
    need(type(panels)is int and panels>=200,'At least 200 endpoint panels are required')
    need(all(type(n)is int and 1<=n<=2048 for n in (ncore,ntail)),
         'Starting quadrature orders must be integers in [1,2048]')
    ctx.prec=3072
    checkpoint=Checkpoint(work or output.with_suffix('.work'),
                          {'parity':parity,'ncore':ncore,'ntail':ntail,'panels':panels,'bits':ctx.prec})
    completed_this_call=0
    start=time.monotonic();inp=Inputs();res=Residuals(inp,parity);old=OldFields(inp,res)
    source_bounds=SourceBounds(old,inp)
    a8,a=res.a8,res.a
    print(parity,'all function models ready',round(time.monotonic()-start,1),flush=True)
    # Reject interval-dependence blow-up before any large integration.
    for fraction in (q('1/7'),q('1/2'),q('9/10')):
        at=res.a8*fraction
        cell=next((lo,hi)for lo,hi in zip(old.edges[:-1],old.edges[1:])if lo<at and at<hi)
        pp=old.prime_polys(*cell)
        for j,field in enumerate(old.global_fields):
            value=field[None](fraction)+pp[j](fraction)
            for tag,f in field.items():
                if tag is not None:value+=f(fraction)*abs(fraction-old.roots[tag]).log()
            need(abs(value).upper()<q('1e10'),'Old field point control: bad representation or interval blow-up')
    print(parity,'861 old field point controls PASS',flush=True)
    tags=list(old.roots)
    moments={tag:arb_mat(m.nrows(),14) for tag,m in old.global_matrices.items()}
    prime_pairs=arb_mat(287,14);pair_error=arb_mat(287,14)
    mr=arb_mat(1,12);mc=arb_mat(1,12);epair=arb_mat(1,12)
    H=arb_mat(12,12);HC=arb_mat(12,12);Phi=arb_mat(191,12)
    bare=arb_mat(96,12)
    hm_error=arb_mat(1,12);hc_error=arb_mat(12,12);h_error=arb_mat(12,12)
    mc_error=arb_mat(1,12);e_error=arb_mat(1,12);phi_error=arb_mat(191,12);bare_error=arb_mat(96,12)
    nodes={}
    def quadrature(n):
        if n not in nodes:nodes[n]=[arb.legendre_p_root(n,k,weight=True) for k in range(n)]
        return nodes[n]
    # Around the logarithmic endpoint, shift polynomials BEFORE taking bounds.
    # This prevents a monomial coefficient norm from destroying cancellation.
    shifted_global={tag:[Poly(f.get(tag,arb_poly([]))(arb_poly([1,1]))) for f in old.global_fields] for tag in tags}
    original_global={tag:[Poly(f.get(tag,arb_poly([])))for f in old.global_fields[:195]]for tag in tags}
    shifted_phi=[Poly(f(arb_poly([1,1]))) for f in old.phi]
    original_phi=[Poly(f)for f in old.phi]
    all_core=list(zip(old.edges[:-2],old.edges[1:-1]))
    width=a8-old.edges[-2]
    all_core += [(a8-width*arb(2)**(-k),a8-width*arb(2)**(-k-1)) for k in range(panels)]
    previous_prime=None;prime_mom=None;prime_polys=None;prime_matrix=None
    next_core=0
    saved=checkpoint.load('core')
    if saved:
        moments=saved['moments'];prime_pairs=saved['prime_pairs'];pair_error=saved['pair_error']
        mc=saved['mc'];epair=saved['epair'];HC=saved['HC'];mc_error=saved['mc_error']
        e_error=saved['e_error'];hc_error=saved['hc_error'];phi_error=saved['phi_error'];bare_error=saved['bare_error']
        prime_mom=saved['prime_mom'];previous_prime=saved['previous_prime'];next_core=saved['next_index']
        prime_polys=old.prime_polys(old.edges[previous_prime],old.edges[previous_prime+1])
        prime_matrix=columns(prime_polys)
        shifted_prime=[Poly(f(arb_poly([1,1]))) for f in prime_polys]
        original_prime=[Poly(f)for f in prime_polys[:195]]
        print(parity,'resuming after',next_core,'core cells',flush=True)
    def finish_prime():
        nonlocal prime_pairs
        if prime_matrix is not None:prime_pairs+=prime_matrix.transpose()*prime_mom
    for index,(lo,hi) in enumerate(all_core):
        if index<next_core:continue
        last=index>=len(old.edges)-2
        original_index=len(old.edges)-2 if last else index
        if original_index!=previous_prime:
            finish_prime()
            prime_polys=old.prime_polys(lo,hi);prime_matrix=columns(prime_polys)
            prime_mom=arb_mat(prime_matrix.nrows(),14)
            shifted_prime=[Poly(f(arb_poly([1,1]))) for f in prime_polys]
            original_prime=[Poly(f)for f in prime_polys[:195]]
            previous_prime=original_index
        fun=res.cell(lo,hi);xx=ellipse(lo,hi)
        need(xx.real>-a and xx.real<a,'Core residual ellipse domain')
        tt=xx/a8;shifted=tt-1
        log_factors={}
        for tag in tags[1:]:
            root=old.roots[tag]
            arg=(root-tt) if root>(lo+hi)/(2*a8) else (tt-root)
            need(arg.real>0,'Log ellipse crosses a root')
            log_factors[tag]=arg.log()
        bounds=[]
        for j in range(195):
            v=shifted_global[None][j](shifted)+shifted_prime[j](shifted)
            v0=original_global[None][j](tt)+original_prime[j](tt)
            for tag in tags[1:]:
                v+=shifted_global[tag][j](shifted)*log_factors[tag]
                v0+=original_global[tag][j](tt)*log_factors[tag]
            bounds.append(min(abs(v).upper(),abs(v0).upper()))
        bounds+=source_bounds.ellipse(xx,[abs(f(shifted)).upper()for f in shifted_prime[195:]])
        rb=[abs(v).upper() for v in fun(xx)]
        mb=abs(res.m(xx)).upper();eb=abs(Poly(res.legs[res.sigma])(tt)).upper()
        allb=rb+[mb,eb]
        need(all(v.is_finite() for v in bounds+allb),'Nonfinite core analytic enclosure')
        n=ntail if last else ncore
        while cheb_error(lo,hi,n)*max(bounds)*max(allb)>q('1e-32'):
            n*=2
            need(n<=2048,'Core quadrature remainder needs more than 2048 nodes')
        rows=[];weights=[];ts=[];mvals=[];evals=[];rvals=[]
        for z,w in quadrature(n):
            x=(lo+hi)/2+(hi-lo)*z/2;ww=(hi-lo)*w/2
            rr=fun(x);mm=res.m(x);ee=res.legs[res.sigma](x/a8)
            rows.append(rr+[mm,ee]);weights.append(ww);ts.append(x/a8)
            rvals.append(rr);mvals.append(ww*mm);evals.append(ww*ee)
        R=arb_mat(rvals);WR=arb_mat([[w*v for v in row]for w,row in zip(weights,rvals)])
        mc+=arb_mat([mvals])*R;epair+=arb_mat([evals])*R
        hc=R.transpose()*WR;HC+=hc
        for tag,glob in old.global_matrices.items():
            d=glob.nrows()
            P=arb_mat([powers(t,d) for t in ts])
            if tag is None:wv=weights
            else:wv=[w*abs(t-old.roots[tag]).log() for t,w in zip(ts,weights)]
            M=P.transpose()*arb_mat([[w*v for v in row] for w,row in zip(wv,rows)])
            moments[tag]+=M
            if tag is None:
                prime_mom+=arb_mat([[M[i,j]for j in range(14)]for i in range(prime_matrix.nrows())])
        e=cheb_error(lo,hi,n)
        pair_error+=outer(bounds,allb)*e
        mc_error+=arb_mat([[e*mb*v for v in rb]])
        e_error+=arb_mat([[e*eb*v for v in rb]])
        hc_error+=outer(rb,rb)*e
        phib=[min(abs(f(shifted)).upper(),abs(g(tt)).upper())for f,g in zip(shifted_phi,original_phi)]
        phi_error+=outer(phib,rb)*(2*e)
        zb=[abs(Poly(f)(xx/a)).upper() for f in old.z]
        for i in range(4):
            for j in range(12):bare_error[i,j]+=2*e*zb[i]*rb[j]
        if index%10==0:print(parity,'core',index,'/',len(all_core),'n',n,'seconds',round(time.monotonic()-start,1),flush=True)
        completed_this_call+=1
        if (index+1)%10==0 or index+1==len(all_core):
            checkpoint.save('core',{'moments':moments,'prime_pairs':prime_pairs,'pair_error':pair_error,
                'mc':mc,'epair':epair,'HC':HC,'mc_error':mc_error,'e_error':e_error,'hc_error':hc_error,
                'phi_error':phi_error,'bare_error':bare_error,'prime_mom':prime_mom,
                'previous_prime':previous_prime,'next_index':index+1})
            if stop_after is not None and completed_this_call>=stop_after:
                print(parity,'CHECKPOINT_ONLY: core cells saved through',index+1,flush=True)
                return None
    finish_prime()
    rawpairs=prime_pairs
    for tag,glob in old.global_matrices.items():rawpairs+=glob.transpose()*moments[tag]
    common_mom=arb_mat([[moments[None][i,j]for j in range(12)]for i in range(moments[None].nrows())])
    Phi=2*columns(old.phi,common_mom.nrows()).transpose()*common_mom
    zpoly=[f(arb_poly([0,a8/a])) for f in old.z]
    zz=2*columns(zpoly,common_mom.nrows()).transpose()*common_mom
    for i in range(4):
        for j in range(12):bare[i,j]+=zz[i,j]
    # Complete logarithmic core tail. Coefficients are bounded after shifting
    # to the endpoint; the log moment is integrated in closed form.
    d=width*arb(2)**(-panels);xx=arb(a8-d/2,d.upper()/2);tt=xx/a8;shifted=tt-1
    rb=[abs(v).upper() for v in res.cell(a8-d,a8)(xx)]
    mb=abs(res.m(xx)).upper();eb=abs(Poly(res.legs[res.sigma])(tt)).upper();allb=rb+[mb,eb]
    tail_source=[]
    for j in range(195):
        G=abs(shifted_global['one'][j](shifted)).upper()
        v=shifted_global[None][j](shifted)+shifted_prime[j](shifted)-shifted_global['one'][j](shifted)*a8.log()
        for tag in ('minus_one','outer','minus_outer'):
            v+=shifted_global[tag][j](shifted)*abs(tt-old.roots[tag]).log()
        tail_source.append(d*(G*(1-d.log())+abs(v).upper()))
    tail_source+=source_bounds.tail_integrals(d,[abs(f(shifted)).upper()for f in shifted_prime[195:]])
    pair_error+=outer(tail_source,allb)
    mc_error+=arb_mat([[d*mb*v for v in rb]]);e_error+=arb_mat([[d*eb*v for v in rb]])
    hc_error+=outer(rb,rb)*d
    phi_error+=outer([abs(f(shifted)).upper() for f in shifted_phi],rb)*(2*d)
    for i,f in enumerate(old.z):
        for j in range(12):bare_error[i,j]+=2*d*abs(f(xx/a)).upper()*rb[j]
    mr=arb_mat(mc);H=arb_mat(HC);hm_error=arb_mat(mc_error);h_error=arb_mat(hc_error)
    # Old shell: all 84 basis pairings and eight Y pairings share the same nodes.
    local=[Poly(f) for f in old.local]
    shifted_local=[Poly(f(arb_poly([1,1]))) for f in old.local]
    shell_mom=arb_mat(96,12)
    shell_z=[f(arb_poly([(a8+a)/(2*a),res.hs/(2*a)]))for f in old.z]
    shell_columns=columns(shell_z+old.local,96)
    next_shell=0;saved=checkpoint.load('shell')
    if saved:
        shell_mom=saved['shell_mom'];mr=saved['mr'];H=saved['H'];hm_error=saved['hm_error'];h_error=saved['h_error']
        bare_error=saved['bare_error'];next_shell=saved['next_index']
        print(parity,'resuming after',next_shell,'shell cells',flush=True)
    for k in range(panels):
        if k<next_shell:continue
        lo=a-res.hs*arb(2)**(-k);hi=a-res.hs*arb(2)**(-k-1)
        fun=res.cell(lo,hi);xx=ellipse(lo,hi);uu=(2*xx-a8-a)/res.hs
        need(xx.real<a and xx.real>-a,'Shell ellipse domain')
        rb=[abs(v).upper() for v in fun(xx)];mb=abs(res.m(xx)).upper()
        yb=[min(abs(f(uu-1)).upper(),abs(g(uu)).upper())for f,g in zip(shifted_local,local)]
        zb=[abs(Poly(f)(xx/a)).upper() for f in old.z]
        need(all(v.is_finite() for v in rb+yb+zb+[mb]),'Nonfinite shell analytic enclosure')
        n=ntail
        while cheb_error(lo,hi,n)*max(rb)*max(rb+yb+zb+[mb])>q('1e-32'):
            n*=2;need(n<=2048,'Shell quadrature bound')
        rv=[];wv=[];mv=[];uv=[]
        for z,w in quadrature(n):
            x=(lo+hi)/2+(hi-lo)*z/2;ww=(hi-lo)*w/2;rr=fun(x)
            rv.append(rr);wv.append([ww*v for v in rr]);mv.append(ww*res.m(x))
            u=(2*x-a8-a)/res.hs
            uv.append(powers(u,96))
        R=arb_mat(rv);WR=arb_mat(wv)
        mr+=arb_mat([mv])*R;H+=R.transpose()*WR
        shell_mom+=arb_mat(uv).transpose()*WR
        e=cheb_error(lo,hi,n)
        hm_error+=arb_mat([[e*mb*v for v in rb]]);h_error+=outer(rb,rb)*e
        for i,v in enumerate(zb+yb):
            for j in range(12):bare_error[i,j]+=2*e*v*rb[j]
        if k%20==0:print(parity,'shell',k,'/',panels,'n',n,'seconds',round(time.monotonic()-start,1),flush=True)
        completed_this_call+=1
        if (k+1)%20==0 or k+1==panels:
            checkpoint.save('shell',{'shell_mom':shell_mom,'mr':mr,'H':H,'hm_error':hm_error,
                'h_error':h_error,'bare_error':bare_error,'next_index':k+1})
            if stop_after is not None and completed_this_call>=stop_after:
                print(parity,'CHECKPOINT_ONLY: shell cells saved through',k+1,flush=True)
                return None
    bare+=2*shell_columns.transpose()*shell_mom
    d=res.hs*arb(2)**(-panels);A,B=endpoint_residual_bounds(res)
    L1=[d*(aa*(1-d.log())+bb) for aa,bb in zip(A,B)]
    L2=arb_mat([[d*(A[i]*A[j]*(d.log()**2-2*d.log()+2)+(A[i]*B[j]+B[i]*A[j])*(1-d.log())+B[i]*B[j])for j in range(12)]for i in range(12)])
    xx=arb(a-d/2,d.upper()/2);uu=(2*xx-a8-a)/res.hs
    for j in range(12):hm_error[0,j]+=res.m(xx).abs_upper()*L1[j]
    h_error+=L2
    for i,f in enumerate([Poly(f)for f in old.z]):
        for j in range(12):bare_error[i,j]+=2*abs(f(xx/a)).upper()*L1[j]
    for i,f in enumerate(shifted_local):
        for j in range(12):bare_error[i+4,j]+=2*abs(f(uu-1)).upper()*L1[j]
    def padded(v,e):
        return arb_mat([[pad(v[i,j],e[i,j])for j in range(v.ncols())]for i in range(v.nrows())])
    rawpairs=padded(rawpairs,pair_error);mc=padded(mc,mc_error);mr=padded(mr,hm_error)
    epair=padded(epair,e_error);Phi=padded(Phi,phi_error);bare=padded(bare,bare_error)
    HC=padded(HC,hc_error);H=padded(H,h_error)
    for i in range(92):
        for j in range(12):bare[i+4,j]-=2*old.lam[i]*mc[0,j]/res.mu8
    H8=2*(HC-mc.transpose()*mc/res.mu8)
    H9=2*(H-mr.transpose()*mr/res.mu)
    scale=(2*(2*res.sigma+1)/a8).sqrt()
    me=(2*a8*(2*res.sigma+1)).sqrt()*__import__('common').mellin(res.sigma,a8)
    eh=epair*scale-mc*(me/res.mu8)
    gamma=2*res.mu8/(me*me)
    YH=H8+eh.transpose()*eh*gamma-Phi.transpose()*Phi
    eg=arb_mat([[scale*rawpairs[i,13]-rawpairs[i,12]*me/res.mu8]for i in range(287)])
    inner=arb_mat([[2*(rawpairs[i,j]-rawpairs[i,12]*mc[0,j]/res.mu8)for j in range(12)]for i in range(287)])
    high=inner+eg*eh*gamma-old.low.transpose()*Phi
    result={'status':'DIRECTED_QUADRATURE_OF_ANALYTIC_MODELS_ONLY','parity':parity,
            'precision_bits':ctx.prec,'tail_panels':panels,'core_nodes':ncore,'tail_nodes':ntail,
            'Phi_star_h':Phi,'high_Gram':YH,'H8_Gram':H8,'H9_Gram':H9,'e_h':eh,
            'raw_old_pairs':rawpairs,'high_cross_models':high,'bare_F_J_pairs':bare,
            'Fhat':res.Fhat,'T':res.T,'T_enclosure':res.T_enclosure,'G_W':res.GW,'gamma_M':gamma,
            'old_Y_coordinate_rounding_norm':old.round_Y,'old_J_coordinate_rounding_norm':old.round_J,
            'regular_kernel_errors_included':False,'old_low_model_errors_included':False,
            'maximum_raw_pair_quadrature_radius':max(rawpairs[i,j].rad()for i in range(287)for j in range(14))}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(encode(result),indent=2)+'\n')
    print(parity,'common pairings written',output,'seconds',round(time.monotonic()-start,1),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('parity',choices=['even','odd']);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--panels',type=int,default=200);ap.add_argument('--core-nodes',type=int,default=64)
    ap.add_argument('--tail-nodes',type=int,default=16)
    ap.add_argument('--work',type=Path);ap.add_argument('--stop-after',type=int)
    a=ap.parse_args();run(a.parity,a.output,a.core_nodes,a.tail_nodes,a.panels,a.work,a.stop_after)
