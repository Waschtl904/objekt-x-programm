"""Actual terminal low matrices and complete infinite coupling Grams; python-flint 0.9.0."""
import sys,time,json,argparse
from pathlib import Path
from flint import arb,arb_mat,arb_poly,fmpq,fmpq_poly,ctx
from math import factorial
from functools import lru_cache

def progress(text):print(time.strftime('%H:%M:%S'),text,flush=True)
def ball(q):return arb(q)
def aminus_radius(value, radius):return value+arb(0,radius)
def matrix(rows):return arb_mat(rows)
def zeros(n,m):return arb_mat(n,m)
def rational(x):
    m,e=x.man_exp();m=int(m);e=int(e)
    return fmpq(m*2**e) if e>=0 else fmpq(m,2**(-e))
def interval(x,digits=55):
    scale=10**digits
    lo=int((x.lower()*scale).floor().unique_fmpz())
    hi=int((x.upper()*scale).ceil().unique_fmpz())
    return [str(lo),str(hi)]
def bounds_summary(x):return x.str(20)

def leg_polynomials(n):
    x=fmpq_poly([0,1]);out=[fmpq_poly([1])]
    if n:out.append(x)
    for k in range(2,n+1):out.append(((2*k-1)*x*out[-1]-(k-1)*out[-2])/k)
    return out
def leg_values(x,n):
    out=[arb(1)]
    if n:out.append(x)
    for k in range(2,n+1):out.append(((2*k-1)*x*out[-1]-(k-1)*out[-2])/k)
    return out
def translated_polys(s,n):
    x=arb_poly([s,1]);out=[arb_poly([1])]
    if n:out.append(x)
    for k in range(2,n+1):out.append(((2*k-1)*x*out[-1]-(k-1)*out[-2])*(arb(1)/k))
    return out

def gamma_polynomial(M):
    # Exact reciprocal series; finite residual plus explicit factorial tail.
    D=max(256,M+20)
    if D%2:D+=1
    cs=[fmpq(1,factorial(k)) if k%2==0 else fmpq(0) for k in range(D+1)]
    sn=[fmpq(1,factorial(k+1)) if k%2==0 else fmpq(0) for k in range(D+1)]
    def inverse(p,n):
        out=[fmpq(1)]
        for k in range(1,n+1):out.append(-sum((p[j]*out[k-j] for j in range(1,min(k,D)+1)),fmpq(0)))
        return out
    ic=inverse(cs,M);ins=inverse(sn,M+1)
    pg=[(ic[k]+ins[k+1])/4 for k in range(M+1)]
    err=fmpq(0)
    for polynomial,denom,tail_start in [(ic,cs,D+2),(ins,sn,D+3)]:
        residual=fmpq_poly(polynomial)*fmpq_poly(denom)-1
        assert all(residual[k]==0 for k in range(len(polynomial)))
        finite=sum((abs(c) for c in residual.coeffs()),fmpq(0))
        tail=fmpq(1,factorial(tail_start))/(1-fmpq(1,(tail_start+1)*(tail_start+2)))
        err+=(finite+sum((abs(c) for c in polynomial),fmpq(0))*tail)/4
    return pg,err

def leg_integrate_sparse(p):
    out={}
    for n,v in p.items():
        term=v/(2*n+1)
        out[n+1]=out.get(n+1,fmpq(0))+term
        if n:out[n-1]=out.get(n-1,fmpq(0))-term
    return {n:v for n,v in out.items() if v}

def gamma_columns(N,M,pg):
    # The coefficient of P_n in K_poly P_j, exact rational at a=1.
    out=[]
    for j in range(N+1):
        previous=[{0:fmpq(1)} if j==0 else {}]
        column={}
        if j==0:column[0]=2*pg[0]
        for k in range(1,M+1):
            p={j:fmpq(1)} if k==1 else {n:k*(k-1)*v for n,v in previous[k-2].items()}
            r=leg_integrate_sparse(leg_integrate_sparse(p))
            val=fmpq(2**k*(-1)**j*factorial(k)**2,factorial(k-j)*factorial(k+j+1)) if k>=j else fmpq(0)
            der=fmpq(k*2**(k-1)*(-1)**j*factorial(k-1)**2,factorial(k-1-j)*factorial(k+j)) if k-1>=j else fmpq(0)
            alpha=der-sum((v*fmpq(n*(n+1),2) for n,v in r.items()),fmpq(0))
            beta=val-sum(r.values(),fmpq(0))-alpha
            r[1]=r.get(1,fmpq(0))+alpha;r[0]=r.get(0,fmpq(0))+beta
            r={n:v for n,v in r.items() if v}
            assert all(n%2==j%2 for n in r)
            previous.append(r)
            if pg[k]:
                weight=fmpq(2,2**k)*pg[k]
                for n,v in r.items():column[n]=column.get(n,fmpq(0))+weight*v
        out.append(column)
        if j%32==0:progress('Gamma column '+str(j)+'/'+str(N))
    return out

def ldl(a):
    n=a.nrows();low=[[arb(0) for _ in range(n)] for _ in range(n)];piv=[]
    for i in range(n):
        d=a[i,i]-sum((low[i][k]**2*piv[k] for k in range(i)),arb(0))
        if not d>0:return low,piv,d
        piv.append(d);low[i][i]=arb(1)
        for j in range(i+1,n):
            low[j][i]=(a[j,i]-sum((low[j][k]*low[i][k]*piv[k] for k in range(i)),arb(0)))/d
    return low,piv,None

def compute(N=383,M=128,precision=2048,output=None):
    ctx.prec=precision;start=time.time();size=N+1
    progress(f'Terminal a=1, raw degrees 0..{N}, Gamma degree {M}, {precision} bits')
    channels=[(q,arb(p).log()/arb(q).sqrt(),arb(q).log()) for q,p in [(2,2),(3,3),(4,2),(5,5),(7,7)]]
    assert channels[-1][2]<2<arb(8).log()
    q0=-(2*arb.pi()).log()-arb.const_euler()
    log2=arb(2).log();pi=arb.pi()
    polys=leg_polynomials(N)
    coefficients=matrix([[arb(polys[i][j]) for j in range(size)] for i in range(size)])
    harm=[arb(0)]
    for k in range(1,2*N+2):harm.append(harm[-1]+arb(1)/k)
    def potential(i,j):
        if (i+j)%2:return arb(0)
        if i!=j:return arb(1)/(abs(i-j)*(i+j+1))
        return (arb(1)/(2*i+1)+2*(harm[2*i]-harm[i])-log2)/(2*i+1)
    P=matrix([[potential(i,j) for j in range(size)] for i in range(size)])
    pg,epsq=gamma_polynomial(M);eps=arb(epsq)
    progress('Gamma uniform kernel error '+bounds_summary(eps))
    kcols=gamma_columns(N,M,pg)
    def gamma_entry(i,j):
        if i<=N:return arb(kcols[i].get(j,fmpq(0)))/(2*j+1)
        return arb(kcols[j].get(i,fmpq(0)))/(2*i+1)
    Gamma=matrix([[gamma_entry(i,j) for j in range(size)] for i in range(size)])
    assert (Gamma-Gamma.transpose()).contains(zeros(size,size))
    progress('Gamma matrix ready; exact polynomial Gauss rules')
    nodes=[arb.legendre_p_root(size,k,weight=True) for k in range(size)]
    S=zeros(size,size)
    for q,w,d in channels:
        length=2-d
        left=[];right=[]
        for node,weight in nodes:
            x=-1+length*(node+1)/2
            left.append(leg_values(x,N));right.append([v*weight*length/2*w for v in leg_values(x+d,N)])
        block=matrix(left).transpose()*matrix(right)
        S+=(block+block.transpose())/2
        progress('Prime matrix channel '+str(q))
    for i in range(size):
        for j in range(size):
            if (i+j)%2:S[i,j]=0
    # Exact V^2 moments, so the singular boundary potential is never sampled.
    lm2=[];odd=arb(0);odd2=arb(0)
    for r in range(N+1):
        odd+=arb(1)/(2*r+1);odd2+=arb(1)/(2*r+1)**2
        lm2.append(((odd-log2)**2+odd2-pi*pi/12)/(2*r+1))
    H2=matrix([[lm2[(i+j)//2] if (i+j)%2==0 else arb(0) for j in range(size)] for i in range(size)])
    P2=coefficients*H2*coefficients.transpose()
    progress('Complete V squared matrix ready')
    actions=[];breaks=[arb(0),arb(1)]
    for q,w,d in channels:
        for sign in (-1,1):
            shift=sign*d;actions.append((shift,w,translated_polys(shift,N)))
            for edge in (-1,1):
                b=edge-shift
                if b>0 and b<1:breaks.append(b)
                else:assert b<=0 or b>=1
    breaks.sort(key=lambda x:float(x.mid())) # ordering subsequently proved with balls
    assert all(breaks[i]<breaks[i+1] for i in range(len(breaks)-1))
    def v_moments(b):
        if b==1:return [arb(0)]*(2*N+1)
        lm=(1-b).log();lp=(1+b).log();hp=arb(0);ps=arb(0);ao=arb(0);az=arb(0);power=arb(1);out=[]
        for m in range(1,2*N+2):
            power*=b;hp+=arb(1)/m;ps+=power/m;ao=-ao+arb(1)/m;az=-az+power/m
            minus=(hp-ps-(1-power)*lm)/m
            plus=((1-(-1)**m)*log2-ao-(power-(-1)**m)*lp+az)/m
            out.append((minus-plus)/2)
        return out
    Sq=zeros(size,size);VS=zeros(size,size)
    for cell,(l,r) in enumerate(zip(breaks,breaks[1:])):
        mid=(l+r)/2;active=[]
        for shift,w,pol in actions:
            if mid+shift>-1 and mid+shift<1:active.append((shift,w,pol))
            else:assert mid+shift<=-1 or mid+shift>=1
        actpol=[sum((w*pol[i] for _,w,pol in active),arb_poly([])) for i in range(size)]
        Acoef=matrix([[actpol[i][j] for j in range(size)] for i in range(size)])
        vals=[];weighted=[]
        for node,weight in nodes:
            x=l+(r-l)*(node+1)/2
            v=[arb(0)]*size
            for shift,w,_ in active:
                seq=leg_values(x+shift,N)
                v=[a+w*b for a,b in zip(v,seq)]
            vals.append(v);weighted.append([a*weight*(r-l)/2 for a in v])
        Sq+=matrix(vals).transpose()*matrix(weighted)
        vl=v_moments(l);vr=v_moments(r);mom=[a-b for a,b in zip(vl,vr)]
        VH=matrix([[mom[i+j] for j in range(size)] for i in range(size)])
        VS+=coefficients*VH*Acoef.transpose()
        progress('Complete shift/cross Gram cell '+str(cell+1)+'/'+str(len(breaks)-1))
    for i in range(size):
        for j in range(size):
            if (i+j)%2:Sq[i,j]=0;VS[i,j]=0
    Dnorm=matrix([[arb(2*i+1) if i==j else arb(0) for j in range(size)] for i in range(size)])
    VminusS=P-S
    Cgram=P2+Sq-VS-VS.transpose()-VminusS*Dnorm*VminusS.transpose()
    high=list(range(N+1,N+M+2))
    GK=matrix([[gamma_entry(i,k) for k in high] for i in range(size)])
    # The polynomial Gamma image has finite Legendre support. For the mixed
    # high term, P(i,k)-S(i,k) is still needed up to this exact support.
    # Compute all additional shift entries with a larger exact Gauss rule.
    extN=N+M+1;extquad=(N+extN+2)//2
    extnodes=[arb.legendre_p_root(extquad,k,weight=True) for k in range(extquad)]
    SH=zeros(size,len(high))
    for q,w,d in channels:
        length=2-d;left=[];right=[]
        for node,weight in extnodes:
            x=-1+length*(node+1)/2
            left.append(leg_values(x,N))
            seq=leg_values(x+d,extN)
            right.append([seq[k]*weight*length/2*w for k in high])
        SH+=matrix(left).transpose()*matrix(right)
        progress('Exact Gamma-support cross terms channel '+str(q))
    for i in range(size):
        for kk,k in enumerate(high):
            if (i+k)%2:SH[i,kk]=0
    PH=matrix([[potential(i,k) for k in high] for i in range(size)])
    WH=matrix([[arb(2*k+1) if j==i else arb(0) for j in range(len(high))] for i,k in enumerate(high)])
    Cgram+=GK*WH*GK.transpose()-(PH-SH)*WH*GK.transpose()-GK*WH*(PH-SH).transpose()
    Q=P-Gamma-S
    for i in range(size):Q[i,i]+=(harm[i]+q0)/(2*i+1)
    # Positive Taylor series for each exact Mellin moment, with full remainder.
    def moment(n):
        lead=arb(1)
        for j in range(1,n+1):lead/=2*(2*j+1)
        term=total=arb(1)
        for k in range(128):
            term/=8*(k+1)*(2*n+2*k+3);total+=term
        nxt=term/(8*129*(2*n+259))
        tail=nxt/(1-arb(1)/(8*130*(2*n+261)))
        return lead*(total+arb(0,tail.upper()))
    require_terminal = N == 383 and M == 128 and precision == 2048
    if not require_terminal:
        raise ValueError('Published model fixes N=383, M=128, precision=2048')
    moment_error=arb(5)/2**384/arb(factorial(384))/(1-arb(1)/(4*385*386))
    err=4*eps+80*moment_error
    result={'endpoint':1,'cutoff':N,'Gamma_degree':M,'precision_bits':precision,
      'arithmetic':'python-flint 0.9.0 Arb balls','scale_digits':55,
      'Gamma_kernel_error':interval(eps),'form_error':interval(err),'parities':{}}
    for parity in (0,1):
        label='even' if parity==0 else 'odd';ix=list(range(parity+2,N+1,2));n=len(ix)
        change=zeros(size,n)
        for j,k in enumerate(ix):
            scale=arb(2*k+1).sqrt();change[k,j]=scale;change[parity,j]=-scale*moment(k)/moment(parity)
        A=change.transpose()*Q*change;G=change.transpose()*Cgram*change
        A=(A+A.transpose())/2;G=(G+G.transpose())/2
        result['parities'][label]={'dimension':n,
          'A':[[interval(A[i,j]) for j in range(n)] for i in range(n)],
          'complete_coupling_Gram':[[interval(G[i,j]) for j in range(n)] for i in range(n)]}
        progress(label+' actual low matrix and complete infinite coupling Gram enclosed')
    if output:Path(output).write_text(json.dumps(result,separators=(',',':'))+'\n',encoding='utf-8')
    progress('Finished in '+str(time.time()-start)+' seconds')
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--degree',type=int,default=383);ap.add_argument('--gamma',type=int,default=128);ap.add_argument('--precision',type=int,default=2048);ap.add_argument('--output',default='terminal_model_recomputed.json');a=ap.parse_args()
    compute(a.degree,a.gamma,a.precision,a.output)
