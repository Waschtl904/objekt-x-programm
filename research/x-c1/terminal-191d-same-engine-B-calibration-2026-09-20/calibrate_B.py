#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, sys
from math import factorial
from pathlib import Path

from flint import arb, arb_mat, arb_poly, fmpq, ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
TERM=ROOT/'research/x-c1/terminal-191d-schur-enclosure-2026-09-20'
spec=importlib.util.spec_from_file_location('term_engine',TERM/'generate_terminal_matrices.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)

def gamma_columns_at(N,M,pg,a):
    out=[]
    for j in range(N+1):
        previous=[{0:fmpq(1)} if j==0 else {}]
        column={}
        if j==0:column[0]=2*a*arb(pg[0])
        for k in range(1,M+1):
            p={j:fmpq(1)} if k==1 else {n:k*(k-1)*v for n,v in previous[k-2].items()}
            r=t.leg_integrate_sparse(t.leg_integrate_sparse(p))
            val=fmpq(2**k*(-1)**j*factorial(k)**2,factorial(k-j)*factorial(k+j+1)) if k>=j else fmpq(0)
            der=fmpq(k*2**(k-1)*(-1)**j*factorial(k-1)**2,factorial(k-1-j)*factorial(k+j)) if k-1>=j else fmpq(0)
            alpha=der-sum((v*fmpq(n*(n+1),2) for n,v in r.items()),fmpq(0))
            beta=val-sum(r.values(),fmpq(0))-alpha
            r[1]=r.get(1,fmpq(0))+alpha;r[0]=r.get(0,fmpq(0))+beta
            r={n:v for n,v in r.items() if v}
            previous.append(r)
            if pg[k]:
                weight=2*a*(a/2)**k*arb(pg[k])
                for n,v in r.items():column[n]=column.get(n,arb(0))+weight*arb(v)
        out.append(column)
    return out

def compute_parities(precision=2048):
    ctx.prec=precision
    N=63;M=64;size=N+1
    a=arb(5).log()/2
    channels=[(q,arb(p).log()/arb(q).sqrt(),arb(q).log()/a) for q,p in [(2,2),(3,3),(4,2)]]
    assert channels[-1][2]<2 and (arb(5).log()/a).contains(2)
    q0=-(2*arb.pi()*a).log()-arb.const_euler()
    log2=arb(2).log();pi=arb.pi()
    polys=t.leg_polynomials(N)
    coefficients=t.matrix([[arb(polys[i][j]) for j in range(size)] for i in range(size)])
    harm=[arb(0)]
    for k in range(1,2*N+M+4):harm.append(harm[-1]+arb(1)/k)
    def potential(i,j):
        if (i+j)%2:return arb(0)
        if i!=j:return arb(1)/(abs(i-j)*(i+j+1))
        return (arb(1)/(2*i+1)+2*(harm[2*i]-harm[i])-log2)/(2*i+1)
    P=t.matrix([[potential(i,j) for j in range(size)] for i in range(size)])
    pg,epsq=t.gamma_polynomial(M);eps=arb(epsq)
    kcols=gamma_columns_at(N,M,pg,a)
    def gamma_entry(i,j):
        if i<=N:return kcols[i].get(j,arb(0))/(2*j+1)
        return kcols[j].get(i,arb(0))/(2*i+1)
    Gamma=t.matrix([[gamma_entry(i,j) for j in range(size)] for i in range(size)])
    assert (Gamma-Gamma.transpose()).contains(t.zeros(size,size))

    nodes=[arb.legendre_p_root(size,k,weight=True) for k in range(size)]
    S=t.zeros(size,size)
    for q,w,d in channels:
        length=2-d;left=[];right=[]
        for node,weight in nodes:
            x=-1+length*(node+1)/2
            left.append(t.leg_values(x,N))
            right.append([v*weight*length/2*w for v in t.leg_values(x+d,N)])
        block=t.matrix(left).transpose()*t.matrix(right)
        S+=(block+block.transpose())/2
    for i in range(size):
        for j in range(size):
            if (i+j)%2:S[i,j]=0

    lm2=[];odd=arb(0);odd2=arb(0)
    for r in range(N+1):
        odd+=arb(1)/(2*r+1);odd2+=arb(1)/(2*r+1)**2
        lm2.append(((odd-log2)**2+odd2-pi*pi/12)/(2*r+1))
    H2=t.matrix([[lm2[(i+j)//2] if (i+j)%2==0 else arb(0) for j in range(size)] for i in range(size)])
    P2=coefficients*H2*coefficients.transpose()

    actions=[];breaks=[arb(0),arb(1)]
    for q,w,d in channels:
        for sign in (-1,1):
            shift=sign*d;actions.append((shift,w,t.translated_polys(shift,N)))
            for edge in (-1,1):
                b=edge-shift
                if b>0 and b<1:breaks.append(b)
                else:assert b<=0 or b>=1
    breaks.sort(key=lambda x:float(x.mid()))
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
    Sq=t.zeros(size,size);VS=t.zeros(size,size)
    for l,r in zip(breaks,breaks[1:]):
        mid=(l+r)/2;active=[]
        for shift,w,pol in actions:
            if mid+shift>-1 and mid+shift<1:active.append((shift,w,pol))
            else:assert mid+shift<=-1 or mid+shift>=1
        actpol=[sum((w*pol[i] for _,w,pol in active),arb_poly([])) for i in range(size)]
        Acoef=t.matrix([[actpol[i][j] for j in range(size)] for i in range(size)])
        vals=[];weighted=[]
        for node,weight in nodes:
            x=l+(r-l)*(node+1)/2;v=[arb(0)]*size
            for shift,w,_ in active:
                seq=t.leg_values(x+shift,N);v=[aa+w*bb for aa,bb in zip(v,seq)]
            vals.append(v);weighted.append([aa*weight*(r-l)/2 for aa in v])
        Sq+=t.matrix(vals).transpose()*t.matrix(weighted)
        vl=v_moments(l);vr=v_moments(r);mom=[aa-bb for aa,bb in zip(vl,vr)]
        VH=t.matrix([[mom[i+j] for j in range(size)] for i in range(size)])
        VS+=coefficients*VH*Acoef.transpose()
    for i in range(size):
        for j in range(size):
            if (i+j)%2:Sq[i,j]=0;VS[i,j]=0
    Dnorm=t.matrix([[arb(2*i+1) if i==j else arb(0) for j in range(size)] for i in range(size)])
    VminusS=P-S
    Cgram=P2+Sq-VS-VS.transpose()-VminusS*Dnorm*VminusS.transpose()

    high=list(range(N+1,N+M+2))
    GK=t.matrix([[gamma_entry(i,k) for k in high] for i in range(size)])
    extN=N+M+1;extquad=(N+extN+2)//2
    extnodes=[arb.legendre_p_root(extquad,k,weight=True) for k in range(extquad)]
    SH=t.zeros(size,len(high))
    for q,w,d in channels:
        length=2-d;left=[];right=[]
        for node,weight in extnodes:
            x=-1+length*(node+1)/2;left.append(t.leg_values(x,N))
            seq=t.leg_values(x+d,extN);right.append([seq[k]*weight*length/2*w for k in high])
        SH+=t.matrix(left).transpose()*t.matrix(right)
    for i in range(size):
        for kk,k in enumerate(high):
            if (i+k)%2:SH[i,kk]=0
    PH=t.matrix([[potential(i,k) for k in high] for i in range(size)])
    WH=t.matrix([[arb(2*k+1) if j==i else arb(0) for j in range(len(high))] for i,k in enumerate(high)])
    Cgram+=GK*WH*GK.transpose()-(PH-SH)*WH*GK.transpose()-GK*WH*(PH-SH).transpose()

    Q=P-Gamma-S
    for i in range(size):Q[i,i]+=(harm[i]+q0)/(2*i+1)

    def moment(n):
        z=a/2
        lead=arb(1)
        for j in range(1,n+1):lead*=z/(2*j+1)
        term=total=arb(1)
        for k in range(128):
            term*=z*z/(2*(k+1)*(2*n+2*k+3));total+=term
        nxt=term*z*z/(2*129*(2*n+259))
        tail=nxt/(1-z*z/(2*130*(2*n+261)))
        return lead*(total+arb(0,tail.upper()))

    snorm=arb(2).log()+arb(3).log()/arb(3).sqrt()+arb(2).log()/2
    gend=(-a).exp()/(1-(-4*a).exp())-1/(4*a)
    out={}
    for parity in (0,1):
        label='even' if parity==0 else 'odd'
        ix=list(range(parity+2,N+1,2));n=len(ix);tail=N+1+parity
        change=t.zeros(size,n)
        for j,k in enumerate(ix):
            scale=arb(2*k+1).sqrt();change[k,j]=scale;change[parity,j]=-scale*moment(k)/moment(parity)
        A=(change.transpose()*Q*change);A=(A+A.transpose())/2
        G=(change.transpose()*Cgram*change);G=(G+G.transpose())/2
        rem=(a/2)**tail/arb(factorial(tail))/(1-(a/2)**2/((tail+1)*(tail+2)))
        epsmoment=rem if parity==0 else 4*rem/a
        err=4*a*eps+80*epsmoment
        delta=harm[tail]+q0-2*a*(arb(1)/4-gend+eps)-snorm-80*epsmoment
        lower=A-G*(arb(1001)/1000)/delta
        for i in range(n):lower[i,i]-=err+1001*err**2/delta
        low,piv,fail=t.ldl(lower)
        if fail is not None:raise RuntimeError(label+' directed LDL failed: '+str(fail))
        trace_inv=arb(0)
        for k in range(n):
            col=[arb(0)]*n
            for i in range(k,n):col[i]=(arb(1) if i==k else arb(0))-sum((low[i][j]*col[j] for j in range(k,i)),arb(0))
            trace_inv+=sum((col[i]**2/piv[i] for i in range(k,n)),arb(0))
        sigma=1/trace_inv
        coupling=(arb(1001)/1000)*G.trace()+n*1001*err**2
        shear=coupling/delta**2
        inverse=(1+shear.sqrt())**2
        z=a/2
        beta=((z*z)/(2*(1-z*z/3)))**2 if parity==0 else ((z*z)/(6*(1-z*z/5)))**2
        gap=min(sigma.lower(),delta.lower())/(inverse.upper()*(1+beta).upper())
        out[label]={
          'dimension':n,'delta':delta.str(30),'sigma':sigma.str(30),'shear':shear.str(30),
          'moment_beta':beta.str(30),'physical_gap_lower':str(gap),
          'positive_pivots':len(piv),'min_pivot':min(piv).str(30)}
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='calibration_results.json');args=ap.parse_args()
    out=compute_parities()
    target=fmpq(1,10**13)
    for parity in ('even','odd'):
        if out[parity]['positive_pivots']!=31:raise RuntimeError(parity+' wrong pivot count')
        if fmpq(out[parity]['physical_gap_lower'])<=target:
            raise RuntimeError(parity+' physical gap does not reproduce >1e-13: '+out[parity]['physical_gap_lower'])
    report={'status':'SAME_ENGINE_B_CALIBRATION_PASS','endpoint':'log(5)/2','target_gap':'1/10^13',
            'parities':out,'terminal_gate_promoted':False,'meaning':'audit calibration only'}
    Path(args.output).write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2,sort_keys=True))
if __name__=='__main__':main()
