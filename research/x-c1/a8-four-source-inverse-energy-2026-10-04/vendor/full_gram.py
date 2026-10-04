"""Complete L2 residual Gram on A8, retaining the logarithmic endpoint weight.
Source q identity and old/new physical profiles are inherited. No target inverse
or target positivity is used. All enclosures use integer interval arithmetic.
"""
from source_core import I,F,S,DIGITS,ceildiv,log2,log_point,log,pi,euler,mellin,leg,H,padd,pscale,pmul,pint,gamma_polynomial
from pathlib import Path
from functools import lru_cache
from math import factorial,comb
import json,gzip,hashlib,argparse,time

def logmsg(s):print(time.strftime('%H:%M:%S'),s,flush=True)
def zero(x):return x.lo==x.hi==0

def trim(p):
    while len(p)>1 and zero(p[-1]):p.pop()
    return p

def pm_direct(a,b):
    """Convolve interval coefficients, accumulating integer products before rounding."""
    lo=[0]*(len(a)+len(b)-1);hi=lo.copy()
    aa=[(i,x.lo,x.hi) for i,x in enumerate(a) if not zero(x)]
    bb=[(i,x.lo,x.hi) for i,x in enumerate(b) if not zero(x)]
    for i,al,ah in aa:
        for j,bl,bh in bb:
            if al>=0:
                if bl>=0:l,h=al*bl,ah*bh
                elif bh<=0:l,h=ah*bl,al*bh
                else:l,h=ah*bl,ah*bh
            elif ah<=0:
                if bl>=0:l,h=al*bh,ah*bl
                elif bh<=0:l,h=ah*bh,al*bl
                else:l,h=al*bh,al*bl
            else:
                if bl>=0:l,h=al*bh,ah*bh
                elif bh<=0:l,h=ah*bl,al*bl
                else:l,h=min(al*bh,ah*bl),max(al*bl,ah*bh)
            lo[i+j]+=l;hi[i+j]+=h
    return trim([I.raw(l//S,ceildiv(h,S)) for l,h in zip(lo,hi)])

def unsigned_convolution(a,b):
    # Exact Kronecker substitution. Each base digit exceeds every coefficient.
    n=len(a)+len(b)-1;ma=max(a);mb=max(b)
    if not ma or not mb:return [0]*n
    width=(ma.bit_length()+mb.bit_length()+min(len(a),len(b)).bit_length()+7)//8
    aa=int.from_bytes(b''.join(x.to_bytes(width,'little') for x in a),'little')
    bb=int.from_bytes(b''.join(x.to_bytes(width,'little') for x in b),'little')
    raw=(aa*bb).to_bytes(width*(n+1),'little')
    return [int.from_bytes(raw[k*width:(k+1)*width],'little') for k in range(n)]

def signed_convolution(a,b):
    ma=max(0,-min(a));mb=max(0,-min(b))
    v=unsigned_convolution([x+ma for x in a],[x+mb for x in b])
    pa=[0];pb=[0]
    for x in a:pa.append(pa[-1]+x)
    for x in b:pb.append(pb[-1]+x)
    for k in range(len(v)):
        al=max(0,k-len(b)+1);ah=min(len(a)-1,k)
        bl=max(0,k-len(a)+1);bh=min(len(b)-1,k)
        count=max(0,ah-al+1)
        v[k]-=mb*(pa[ah+1]-pa[al])+ma*(pb[bh+1]-pb[bl])+ma*mb*count
    return v

def pm(a,b):
    # One exact signed convolution; a conservative integer radius encloses
    # every coefficient error, including all products of coefficient radii.
    ma=[(x.lo+x.hi)//2 for x in a];mb=[(x.lo+x.hi)//2 for x in b]
    ra=[max(x.hi-m,m-x.lo) for x,m in zip(a,ma)]
    rb=[max(x.hi-m,m-x.lo) for x,m in zip(b,mb)]
    rad=sum(abs(x) for x in ma)*sum(rb)+sum(ra)*sum(abs(x) for x in mb)+sum(ra)*sum(rb)
    conv=signed_convolution(ma,mb)
    sa={i%2 for i,x in enumerate(a) if not zero(x)};sb={i%2 for i,x in enumerate(b) if not zero(x)}
    allowed={(i+j)%2 for i in sa for j in sb}
    return trim([I.raw((v-rad)//S,ceildiv(v+rad,S)) if k%2 in allowed else I(0) for k,v in enumerate(conv)])

def shifted(p,t):
    """Horner composition p(x+t)."""
    v=[I(0)]
    for c in reversed(p):
        w=[I(0)]*(len(v)+1)
        for i,x in enumerate(v):w[i]+=t*x;w[i+1]+=x
        w[0]+=c;v=w
    return trim(v)

def scale_arg(p,t):
    out=[];pw=I(1)
    for x in p:out.append(x*pw);pw*=t
    return out

def linear_combine_leg(ls):
    out=[I(0)]*len(ls)
    for n,w in enumerate(ls):
        if zero(w):continue
        for k,v in enumerate(leg(n)):
            if v:out[k]+=w*I(v)
    return trim(out)

def parity_poly(p,par):
    for i in range(1-par,len(p),2):
        assert p[i].contains_zero()
        p[i]=I(0) # enforced exact parity of the source and even kernel
    return trim(p)

def peval1(p):return sum(p,I(0))
def pder1(p):return sum((i*c for i,c in enumerate(p)),I(0))
def int2(p):return [I(0),I(0)]+[v/((k+1)*(k+2)) for k,v in enumerate(p)]

def kernel_action(poly,ls,t,coeff,par):
    """A_k=integral[-1,1] |x-y|^k p(y)dy.
    A_1''=2p and A_k''=k(k-1)A_(k-2), with exact endpoint moments.
    Uses the unnormalised dy integral; K_t=t*integral k_reg dy.
    """
    moments=[]
    for k in range(len(coeff)):
        v=I(0)
        for n in range(par,min(k,len(ls)-1)+1,2):
            weight=F((-1)**n*2**(k+1)*factorial(k)**2,
                     factorial(k-n)*factorial(k+n+1))
            v+=ls[n]*I(weight)
        moments.append(v)
    previous=[];out=[I(0)];pw=I(1)
    for k,w in enumerate(coeff):
        if k==0:ak=[moments[0]]
        else:
            rhs=pscale(poly,2) if k==1 else pscale(previous[k-2],k*(k-1))
            ak=int2(rhs)
            if par==0:
                ak[0]=moments[k]-peval1(ak)
                assert (pder1(ak)-k*moments[k-1]).contains_zero()
            else:
                ak[1]=k*moments[k-1]-pder1(ak)
                assert (peval1(ak)-moments[k]).contains_zero()
        ak=parity_poly(ak,par);previous.append(ak)
        if w:out=padd(out,pscale(ak,t*I(w)*pw))
        pw*=t/2
    return parity_poly(out,par)

class Moments:
    def __init__(self,edges,max_degree):
        self.max=max_degree;self.m={};self.w={};self.v2=[]
        l2=log2();p2=pi()**2
        oh=oh2=I(0)
        for k in range(max_degree+1):
            if k%2==0:
                oh+=I(1)/(k+1);oh2+=I(1)/((k+1)**2)
                self.v2.append(((oh-l2)**2+oh2-p2/12)/(k+1))
            else:self.v2.append(I(0)) # used only with same-parity products
        for edge in edges:
            key=(edge.lo,edge.hi);power=[I(1)]
            for k in range(max_degree+1):power.append(power[-1]*edge)
            self.m[key]=[power[k+1]/(k+1) for k in range(max_degree+1)]
            v=[]
            if edge.lo==edge.hi==0:v=[I(0)]*(max_degree+1)
            elif edge.lo==edge.hi==S:
                odds=I(0);ha=I(0)
                for k in range(max_degree+1):
                    if k%2==0:odds+=I(1)/(k+1);v.append((odds-l2)/(k+1))
                    else:ha+=I(1)/((k+1)//2);v.append(ha/(2*(k+1)))
            else:
                assert 0<edge.lo and edge.hi<S
                lg=log(1-edge*edge);atanh=(log(1+edge)-log(1-edge))/2
                se=so=I(0)
                for k in range(max_degree+1):
                    if k%2==0:
                        se+=power[k+1]/(k+1)
                        v.append(-(power[k+1]*lg+2*(atanh-se))/(2*(k+1)))
                    else:
                        so+=power[k+1]/(k+1)
                        v.append(((1-power[k+1])*lg/2+so)/(k+1))
            self.w[key]=v
    def integrate(self,p,l=I(0),h=I(1),weight=0):
        if weight==2:
            assert l.lo==l.hi==0 and h.lo==h.hi==S
            assert all(zero(p[k]) for k in range(1,len(p),2))
            vals=self.v2
        else:
            d=self.w if weight==1 else self.m
            a=d[(l.lo,l.hi)];b=d[(h.lo,h.hi)]
            vals=[b[k]-a[k] for k in range(len(p))]
        return sum((v*vals[k] for k,v in enumerate(p) if not zero(v)),I(0))

def serial(x,digits=60):
    if isinstance(x,I):
        ss=10**digits;fac=S//ss
        return [str(F(x.lo//fac,ss)),str(F(ceildiv(x.hi,fac),ss))]
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serial(v,digits) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v,digits) for v in x]
    return x

def show(x):return x.display()
def upper(x):return I.raw(x.hi,x.hi)
def loadI(v):return I.hull(F(v[0]),F(v[1]))

def compute(model_path,sol_path,out,potential_degree=640):
    assert __debug__ and not out.exists()
    raw=model_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='5f8935d53f8518540ef25e6f2d511955bad688cf5905cb63e8d89f03aae2474b'
    model=json.loads(gzip.decompress(raw));solraw=sol_path.read_bytes();sol=json.loads(solraw)
    a=3*log2()/2;b=log_point(3);r=a/b;sr=r.sqrt()
    qa=-log(2*pi()*a)-euler();qb=-log(2*pi()*b)-euler()
    logmsg('constants ready')
    oldcoeff=list(map(F,model['Gamma_polynomial_coefficients']));epso=F(model['Gamma_kernel_error_exact'])
    newcoeff,epsn=gamma_polynomial(128)
    channels=[(2,2),(3,3),(4,2),(5,5),(7,7)]
    specs=[]
    for is_old,chs,t in [(True,channels,a),(False,channels+[(8,2)],b)]:
        for q,prime in chs:
            if is_old and q in (2,4):d=I(F(2 if q==2 else 4,3))
            elif not is_old and q==3:d=I(1)
            else:d=log_point(q)/t
            w=log_point(prime)/I(q).sqrt()
            scale=I(1) if is_old else r
            for sign in (-1,1):
                shift=sign*d
                ll=(-1-shift)/scale;hh=(1-shift)/scale
                if ll.hi<=0:l=I(0)
                elif ll.lo>=S:continue
                else:l=ll
                if hh.lo>=S:h=I(1)
                elif hh.hi<=0:continue
                else:h=hh
                if h.hi<=l.lo:continue
                assert l.hi<h.lo
                specs.append((is_old,q,shift,w,l,h))
    edges=[I(0),I(1)]
    for _,_,_,_,l,h in specs:edges.extend([l,h])
    edges.sort(key=lambda x:x.lo);uniq=[]
    for x in edges:
        if uniq and x.intersects(uniq[-1]):
            # The only nontrivial coincident old edges are ±2/3, ±4/3.
            assert x.lo==uniq[-1].lo and x.hi==uniq[-1].hi,(x,uniq[-1])
        else:uniq.append(x)
    edges=uniq
    logmsg('positive-half cells '+str(len(edges)-1))
    # Smooth new log potential expansion, the original singular old potential remains exact.
    vp=[I(0)]*(2*potential_degree+1);pw=I(1);r2=r*r
    for k in range(1,potential_degree+1):pw*=r2;vp[2*k]=pw/(2*k)
    vtail=pw*r2/(2*(potential_degree+1)*(1-r2))
    logmsg('new potential uniform tail '+str(show(vtail)))
    maxdeg=2*(2*potential_degree+7)+4
    moments=Moments(edges,maxdeg)
    logmsg('analytic log and squared-log moments ready')
    records=[];function_records=[]
    for par,label in enumerate(['even','odd']):
        P=[[F(v) for v in row] for row in sol['blocks'][par]['proposal']]
        assert len(P)==191
        oldmom=[mellin(n,a) for n in range(384)]
        news=[2+par,4+par]
        base=[];bb=[];oldp=[];oldq=[];oldls=[];newg=[];p_norm=[];z_norm=[];kernelo=[];kerneln=[]
        for col,m in enumerate(news):
            ls=[I(0)]*384
            for i,n in enumerate(range(2+par,384,2)):ls[n]=I(P[i][col])*I(2*n+1).sqrt()
            ls[par]=-sum((ls[n]*oldmom[n]/oldmom[par] for n in range(2+par,384,2)),I(0))
            pp=linear_combine_leg(ls);dh=linear_combine_leg([v*I(H(n)) for n,v in enumerate(ls)])
            ko=kernel_action(pp,ls,a,oldcoeff,par)
            oq=padd(padd(dh,pscale(pp,qa)),pscale(ko,-1))
            lsn=[I(0)]*(m+1);lsn[m]=I(2*m+1).sqrt();lsn[par]=-lsn[m]*mellin(m,b)/mellin(par,b)
            gg=linear_combine_leg(lsn);ndh=linear_combine_leg([v*I(H(n)) for n,v in enumerate(lsn)])
            kn=kernel_action(gg,lsn,b,newcoeff,par)
            ng=padd(padd(ndh,pscale(gg,qb)),pscale(kn,-1))
            ng=pscale(scale_arg(ng,r),sr)
            ng=padd(ng,pm(pscale(scale_arg(gg,r),sr),vp))
            ba=padd(ng,pscale(oq,-1));bo=pscale(pp,-1)
            pn=(sum((I(x[col]*x[col]) for x in P),I(0))+ls[par]**2/(2*par+1)).sqrt()
            zn=(I(1)+lsn[par]**2/(2*par+1)).sqrt()
            base.append(ba);bb.append(bo);oldp.append(pp);oldq.append(oq);newg.append(gg)
            oldls.append(ls);p_norm.append(pn);z_norm.append(zn);kernelo.append(ko);kerneln.append(kn)
            logmsg(label+' column '+str(col)+' action built; pnorm '+str(show(pn)))
        cells=[]
        # Prebuild the shifted polynomials; 22 endpoint/shift representations only.
        shiftpolys=[]
        for isold,q,t,w,l,h in specs:
            shiftpolys.append([pscale(shifted(oldp[j] if isold else newg[j],t),w if isold else -sr*w) if isold else
                               pscale(scale_arg(shifted(newg[j],t),r),-sr*w) for j in range(2)])
        for l,h in zip(edges,edges[1:]):
            mid=I.raw((l.hi+h.lo)//2,(l.hi+h.lo)//2)
            sh=[[I(0)],[I(0)]];oldsh=[[I(0)],[I(0)]];newsh=[[I(0)],[I(0)]]
            for sp,pols in zip(specs,shiftpolys):
                isold,q,t,w,sl,shigh=sp
                active=sl.hi<mid.lo and mid.hi<shigh.lo
                if active:
                    for j in range(2):
                        sh[j]=padd(sh[j],pols[j])
                        if isold:oldsh[j]=padd(oldsh[j],pscale(pols[j],-1)) # old Q includes -S_a
                        else:newsh[j]=padd(newsh[j],pols[j])
            cells.append((l,h,sh,oldsh,newsh))
        logmsg(label+' shift polynomials ready')
        G=[[I(0) for _ in range(2)] for _ in range(2)]
        oldG=[[I(0) for _ in range(2)] for _ in range(2)]
        for i in range(2):
            for j in range(i,2):
                value=moments.integrate(pm(base[i],base[j]))
                value+=moments.integrate(padd(pm(base[i],bb[j]),pm(bb[i],base[j])),weight=1)
                value+=moments.integrate(pm(bb[i],bb[j]),weight=2)
                # Old model Q^P p norm, separately usable against complete_model_raw_high_Gram.
                ov=moments.integrate(pm(oldq[i],oldq[j]))
                ov+=moments.integrate(padd(pm(oldq[i],oldp[j]),pm(oldp[i],oldq[j])),weight=1)
                ov+=moments.integrate(pm(oldp[i],oldp[j]),weight=2)
                for l,h,sh,osh,nsh in cells:
                    value+=moments.integrate(padd(padd(pm(base[i],sh[j]),pm(sh[i],base[j])),pm(sh[i],sh[j])),l,h)
                    value+=moments.integrate(padd(pm(bb[i],sh[j]),pm(sh[i],bb[j])),l,h,1)
                    ov+=moments.integrate(padd(padd(pm(oldq[i],osh[j]),pm(osh[i],oldq[j])),pm(osh[i],osh[j])),l,h)
                    ov+=moments.integrate(padd(pm(oldp[i],osh[j]),pm(osh[i],oldp[j])),l,h,1)
                G[i][j]=G[j][i]=value;oldG[i][j]=oldG[j][i]=ov
                logmsg(label+' raw Gram '+str((i,j))+' '+str(show(value)))
        # Exact parity means full L2(dx/2) pairings equal integrals on [0,1].
        mp=[I(0)]*201;pw=I(1)
        for k in range(201):
            if k%2==par:mp[k]=pw/I(factorial(k))
            pw*=a/2
        mtail=pw/I(factorial(201))/(1-a/(2*202))
        mun=moments.integrate(pm(mp,mp));munorm=upper(mun).sqrt()
        mu=mun.inflate(2*munorm*mtail+mtail**2)
        assert mu.lo>0
        beta=[]
        for i in range(2):
            v=moments.integrate(pm(base[i],mp))+moments.integrate(pm(bb[i],mp),weight=1)
            for l,h,sh,_,_ in cells:v+=moments.integrate(pm(sh[i],mp),l,h)
            v=v.inflate(upper(G[i][i]).sqrt()*mtail);beta.append(v)
        projected=[[G[i][j]-beta[i]*beta[j]/mu for j in range(2)] for i in range(2)]
        assert projected[0][0].lo>0 and projected[1][1].lo>0,projected
        err=[2*a*I(epso)*p_norm[i]+2*b*I(epsn)*z_norm[i]+vtail*z_norm[i] for i in range(2)]
        gram=[];rnorm=[upper(projected[i][i]).sqrt() for i in range(2)]
        for i in range(2):
            row=[]
            for j in range(2):
                er=rnorm[i]*err[j]+rnorm[j]*err[i]+err[i]*err[j]
                row.append(projected[i][j].inflate(er))
            gram.append(row)
        logmsg(label+' PROJECTED TRUE GRAM '+str([[show(x) for x in row] for row in gram]))
        records.append({'parity':label,'unprojected_model_gram':G,'mellin_projection_pairings':beta,
                        'mellin_function_norm_squared':mu,'mellin_polynomial_tail':mtail,
                        'projected_model_gram':projected,'complete_true_residual_gram':gram,
                        'old_source_norms':p_norm,'new_source_norms':z_norm,
                        'model_to_true_function_error_norms':err,'old_model_action_gram':oldG})
        function_records.append({'parity':label,'smooth_base':base,'old_log_coefficient':bb,
                     'positive_cells':[{'lo':l,'hi':h,'shift_polynomials':sh} for l,h,sh,_,_ in cells],
                     'mellin_pairings':beta,'mellin_norm_squared':mu,'projection_function_parity':par,
                     'old_legendre_coefficients':oldls,'old_smooth_action':oldq,'old_polynomial':oldp,
                     'old_shift_cells':[{'lo':l,'hi':h,'shift_polynomials':osh} for l,h,_,osh,_ in cells]})
    result={'status':'COMPLETE_L2_RESIDUAL_GRAM_ENCLOSED','model_sha256':hashlib.sha256(raw).hexdigest(),
            'solutions_sha256':hashlib.sha256(solraw).hexdigest(),'interval_decimal_digits':DIGITS,
            'old_gamma_degree':160,'new_gamma_degree':128,'new_potential_series_terms':potential_degree,
            'new_potential_uniform_tail':vtail,'old_kernel_error':epso,'new_kernel_error':epsn,
            'blocks':records,'full_variational_inverse_energy_computed':False,'forward_reserve_proved':False,
            'target_positivity_used':False,'github_changed':False}
    out.mkdir(parents=True)
    (out/'FULL_GRAM.json').write_text(json.dumps(serial(result),indent=2)+'\n',encoding='utf8',newline='\n')
    # Coefficient boxes are computational enclosures and not independent freely variable inputs.
    fun={'description':'g_model(x)=base(x)+B(x)*(-log(1-x*x)/2)+cell_shift(x); exact parity continuation. r_model=Pi_a g_model.',
         'input_coordinate':'L2((-1,1),dx/2), physical via U_a^{-1}',
         'a':a,'b':b,'blocks':function_records}
    (out/'FUNCTIONS.json').write_bytes((json.dumps(serial(fun,700),separators=(',',':'))+'\n').encode('utf8'))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--model',type=Path,required=True);p.add_argument('--solutions',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--potential-terms',type=int,default=640)
    ar=p.parse_args();compute(ar.model,ar.solutions,ar.out,ar.potential_terms)
