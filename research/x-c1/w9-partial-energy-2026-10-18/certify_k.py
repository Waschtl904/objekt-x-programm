"""Directed full K_P for a separately frozen candidate; no direction search."""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from flint import arb,acb,arb_poly,acb_poly,arb_mat,ctx
from common import Inputs,q,box,mat,ratmat,pint,pad,encode,legs,need
from assemble import load_pairs


def certify(inp,data,coefficients,nodes_count=128):
    par=data['parity'];eps=1 if par=='even' else -1
    a=arb(3).log();b=arb(11).log()/2;h=b-a;mu=(eps*a+a.sinh())/2
    leg=legs(12);c=arb_mat([[q(v)]for v in coefficients]);G=mat(data['G_W'])
    normalization=(c.transpose()*G*c)[0,0].sqrt();c/=normalization
    P=sum((c[j,0]*(arb(2*j+1)/(2*h)).sqrt()*leg[j](arb_poly([-1-2*a/h,2/h]))for j in range(12)),arb_poly([]))
    m=lambda x:(x/2).cosh()if eps==1 else(x/2).sinh()
    # The exact moment can also be recovered from the norm-one shell polynomial.
    M=arb_poly([((a/2).cosh()if ((eps==1)==(j%2==0))else(a/2).sinh())*(a/2)**j/arb.fac_ui(j)for j in range(121)])
    s=b/a-1;pu=P(arb_poly([a,a]));em=(b/2).exp()*(a*s/2)**121/arb.fac_ui(121)
    pnorm=sum((abs(v).upper()*s**j for j,v in enumerate(pu)),arb(0))
    lam=a*pad(pint(pu*M,arb(0),s),s*pnorm*em);Ac=-lam/mu
    derivative=P.derivative()
    A=2*pint(derivative*derivative,a,b)+2*Ac**2*(-eps*a+a.sinh())/8
    J=2*((P(a)-Ac*m(a))**2+P(b)**2)
    ends=[(-b,-a),(-a,a),(a,b)];polys=[P(arb_poly([0,-1]))*eps,None,P]
    def exponential_primitive(p,sign):
        ans=p*(arb(2)*sign);d=p
        for k in range(1,len(p)):
            d=d.derivative();ans+=d*((-1)**k*(arb(2)*sign)**(k+1))
        return ans
    def correlation_formula(selector):
        pairs=[]
        for i,(ai,bi)in enumerate(ends):
            for j,(aj,bj)in enumerate(ends):
                ld=aj-selector-ai;ud=bj-selector-bi
                need(ld>0 or ld<0,'Autocorrelation lower branch')
                need(ud>0 or ud<0,'Autocorrelation upper branch')
                lj=ld>0;hj=ud<0
                lo=aj-selector if lj else ai;hi=bj-selector if hj else bi
                need(hi>lo or hi<lo,'Autocorrelation overlap branch')
                if hi>lo:pairs.append((i,j,lj,hj))
        def value(r):
            iscomplex=isinstance(r,acb);Poly=acb_poly if iscomplex else arb_poly
            total=acb(0)if iscomplex else arb(0)
            for i,j,lj,hj in pairs:
                lo=ends[j][0]-r if lj else ends[i][0];hi=ends[j][1]-r if hj else ends[i][1]
                if i==j==1:
                    total+=Ac**2*((hi+r/2).sinh()-(lo+r/2).sinh()+eps*(hi-lo)*(r/2).cosh())/2
                elif i!=1 and j!=1:
                    pol=Poly(polys[i])*Poly(polys[j])(Poly([r,1]));Q=pol.integral();total+=Q(hi)-Q(lo)
                else:
                    pol=Poly(polys[j])(Poly([r,1]))if i==1 else Poly(polys[i])
                    shift=arb(0)if i==1 else r
                    for sign in (1,-1):
                        Q=exponential_primitive(pol,sign)
                        v=(hi*sign/2).exp()*Q(hi)-(lo*sign/2).exp()*Q(lo)
                        total+=Ac/2*(1 if sign==1 else eps)*(shift*sign/2).exp()*v
            return total
        return value
    C0=correlation_formula(h/2)(arb(0));need(C0.contains(1),'Unit autocorrelation')
    kernel=lambda r:(-r/2).exp()/(1-(-2*r).exp())
    theta=lambda r:(-r/2).exp().atanh()+(-r/2).exp().atan()
    depth=48;cut=h*arb(2)**(-depth)
    near=A*(cut**3/3+cut**2/4)+2*(A*J).sqrt()*(2*cut**2*cut.sqrt()/5+cut*cut.sqrt()/3)+J*(cut**2/2+cut/2)
    panels=[(h*arb(2)**(-k),h*arb(2)**(-k+1))for k in range(depth,0,-1)]
    for left,right in ((h,2*a),(2*a,a+b),(a+b,2*b)):
        lo=left
        while 2*lo<right:panels.append((lo,2*lo));lo=2*lo
        panels.append((lo,right))
    nodes=[arb.legendre_p_root(nodes_count,k,weight=True)for k in range(nodes_count)]
    integrated=arb(0);quad_error=arb(0)
    for idx,(lo,hi)in enumerate(panels):
        mid=(lo+hi)/2;half=(hi-lo)/2;corr=correlation_formula(mid)
        value=sum((half*w*2*kernel(mid+half*x)*(1-corr(mid+half*x))for x,w in nodes),arb(0))
        zz=acb(arb(mid,half.upper()*5/4),arb(0,half.upper()*3/4));need(zz.real>0,'Gamma ellipse pole')
        M=abs(2*kernel(zz)*(1-corr(zz))).upper()
        need(M.is_finite() and value.is_finite(),'Nonfinite K_P cell enclosure')
        error=8*(hi-lo)*M*arb(2)**(-2*nodes_count)
        integrated+=pad(value,error);quad_error+=error
        if idx%16==0:print(par,'K_P cell',idx,'/',len(panels),flush=True)
    tail=2*theta(2*b);E=integrated+arb(0).union(near.upper())+tail
    prime=arb(0);prime_values={}
    for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)):
        r=2*a if n==9 else arb(n).log()
        if n!=9:
            need(all(abs(r-edge)>q('1e-8')for edge in (0,h,2*a,a+b,2*b)),
                 'Prime correlation selector crosses a breakpoint')
        value=correlation_formula(r+q('1e-10'))(r)
        prime_values[str(n)]=value;prime+=2*arb(p).log()/arb(n).sqrt()*value
    direct=E-(8*arb.pi()).log()-arb.const_euler()-arb.pi()/2-prime
    AQ=[[Fraction(v)for v in row]for row in inp.json('fresh_A12')['parities'][par]['midpoint']]
    XQ=[[Fraction(v)for v in row]for row in inp.json('frozen_response')['parities'][par]['X']]
    SQ=[[XQ[i][j]+XQ[j][i]-sum((XQ[k][i]*AQ[k][l]*XQ[l][j]for k in range(12)for l in range(12)),Fraction(0))for j in range(12)]for i in range(12)]
    S=ratmat(SQ);F=mat(data['Fhat'])*c;correction=(F.transpose()*S*F)[0,0]
    err=q(inp.json('response')['parities'][par]['fixed_X']['direct_K_error_upper'])
    KP=pad(direct-correction,err)
    return {'status':'AUTHOR_DERIVED_CONDITIONAL_DIRECTED_K_P_EXTERNAL_REVIEW_OPEN','parity':par,
            'raw_coefficients':coefficients,'normalization':normalization,'unit_autocorrelation':C0,
            'derivative_square':A,'jump_square':J,'near_zero_bound':near,'quadrature_remainder':quad_error,
            'outer_tail':tail,'translation_energy':E,'prime_correlations':prime_values,
            'direct_form':direct,'response_correction':correction,'K_model_error':err,'K_P_interval':KP,
            'candidate_selected_here':False,'N12_closed':False}


def baseline(inp,data):
    par=data['parity']
    coeff=inp.json('old_candidate_'+par)['raw_exact_rational_coefficients']
    result=certify(inp,data,coeff)
    reference=box(inp.json('kp_'+par)['actual_K_P_interval'])
    need(result['K_P_interval'].overlaps(reference),'Independent previous K_P certificate comparison')
    result['previous_K_P_interval']=reference
    result['previous_interval_overlap']=True
    result['role']='NEW_IMPLEMENTATION_CONTROL_ON_PREVIOUS_FROZEN_DIRECTION'
    return result


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('pairs',type=Path);ap.add_argument('candidate',type=Path);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();ctx.prec=800
    candidate_raw=args.candidate.read_bytes()
    frozen=json.loads(candidate_raw);data=load_pairs(args.pairs)
    need(frozen['parity']==data['parity'],'Candidate parity')
    need(frozen['pairs_sha256']==data['_source_sha256'],'Candidate pair binding')
    result=certify(Inputs(),data,frozen['raw_coefficients'])
    result['candidate_sha256']=hashlib.sha256(candidate_raw).hexdigest()
    args.output.write_text(json.dumps(encode(result),indent=2)+'\n')
    print(data['parity'],'K_P',result['K_P_interval'],flush=True)
