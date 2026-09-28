"""Independent small-degree integral assembly at the exact new endpoint.

Compares full-function integration followed by Parseval subtraction with the
generator's separate V/S/Gamma Gram assembly. This is not a tail certificate.
"""
from pathlib import Path
from math import factorial
import argparse,gzip,json
from flint import arb,arb_mat,arb_poly,fmpq,ctx
import generate_a9 as t
from check_a9 import ball


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--model',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    ctx.prec=512;checks=[]
    def check(name,condition):
        if not condition:raise RuntimeError(name)
        checks.append(name)
    data=json.loads(gzip.decompress(args.model.read_bytes()))
    N=data['cutoff'];M=data['Gamma_degree'];a=arb(3).log()
    assert N==15 and M==16
    scale=10**data['scale_digits'];log2=arb(2).log()
    pg,_=t.gamma_polynomial(M);columns=t.gamma_columns(N,M,pg,a)
    ext=N+M+1;polys=t.leg_polynomials(ext);pol=[arb_poly(p) for p in polys]
    def correlation(i,j):
        out=[fmpq(0)]*(i+j+2)
        for k in range(i+1):
            ai=fmpq((-1)**(i+k)*factorial(i+k),2**k*factorial(k)**2*factorial(i-k))
            for ell in range(j+1):
                aj=fmpq((-1)**(j+ell)*factorial(j+ell),2**ell*factorial(ell)**2*factorial(j-ell))
                out[k+ell+1]+=(-1)**j*ai*aj*fmpq(factorial(k)*factorial(ell),factorial(k+ell+1))
        return arb_poly(out)
    def intpoly(p,l,r):
        return sum((p[k]*(r**(k+1)-l**(k+1))/(k+1) for k in range(len(p))),arb(0))
    channels=[(q,arb(p).log()/arb(q).sqrt(),arb(1) if q==3 else arb(q).log()/a) for q,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]]
    nodes=[arb.legendre_p_root(20,k,weight=True) for k in range(20)]
    for q,w,d in channels:
        for i,j in [(0,0),(0,2),(1,1),(1,5),(4,6),(7,9)]:
            length=2-d
            rule=sum((weight*pol[i](-1+length*(x+1)/2)*pol[j](-1+length*(x+1)/2+d)*length/2 for x,weight in nodes),arb(0))
            check('shift integral '+str((q,i,j)),rule.overlaps(correlation(i,j)(length)))
    kernel=arb_poly([arb(pg[k])*(a/2)**k for k in range(M+1)])
    for i,j in [(0,0),(0,2),(1,1),(1,5),(4,6),(7,9)]:
        direct=a*intpoly(kernel*correlation(i,j)(arb_poly([2,-1])),arb(0),arb(2))
        check('scaled Gamma integral '+str((i,j)),direct.overlaps(arb(columns[i].get(j,0))/(2*j+1)))
    # Independent logarithmic primitives, including exact endpoint limits.
    def log_minus_primitive(n,x):
        m=n+1
        part=-sum((x**k/k for k in range(1,m+1)),arb(0))/m
        return part if x==1 else part+(x**m-1)*(1-x).log()/m
    def log_plus_primitive(n,x):
        m=n+1
        return ((x**m-(-1)**m)*(1+x).log()-sum(((-1)**k*x**(n-k+1)/(n-k+1) for k in range(n+1)),arb(0)))/m
    def vint(p,l,r):
        return -sum((p[k]*(log_minus_primitive(k,r)-log_minus_primitive(k,l)+log_plus_primitive(k,r)-log_plus_primitive(k,l))/2 for k in range(len(p))),arb(0))
    def v2int(p):
        value=arb(0)
        for k in range(0,len(p),2):
            rr=k//2
            odd=sum((arb(1)/(2*j+1) for j in range(rr+1)),arb(0))
            odd2=sum((arb(1)/(2*j+1)**2 for j in range(rr+1)),arb(0))
            value+=p[k]*((odd-log2)**2+odd2-arb.pi()**2/12)/(2*rr+1)
        return value
    kapp=[sum((arb(v)*pol[k] for k,v in col.items()),arb_poly([])) for col in columns]
    breaks=[arb(0),channels[2][2]-1,1-channels[0][2],channels[3][2]-1,channels[4][2]-1,channels[5][2]-1,arb(1)]
    check('exact six-cell A9 geometry ordered',all(x<y for x,y in zip(breaks,breaks[1:])))
    size=N+1;C=arb_mat(size,size);full=arb_mat(size,size)
    for i in range(size):
        for j in range(size):
            if (i+j)%2==0:
                C[i,j]=vint(pol[i]*pol[j],arb(0),arb(1))
                full[i,j]=v2int(pol[i]*pol[j])
    for l,r in zip(breaks,breaks[1:]):
        mid=(l+r)/2
        f=[]
        for i in range(size):
            v=-kapp[i]
            for q,w,d in channels:
                for sign in (-1,1):
                    sh=sign*d
                    if -1<mid+sh<1:v-=w*pol[i](arb_poly([sh,1]))
            f.append(v)
        for i in range(size):
            for j in range(size):
                if (i+j)%2==0:
                    C[i,j]+=intpoly(pol[i]*f[j],l,r)
                    full[i,j]+=vint(pol[i]*f[j]+pol[j]*f[i],l,r)+intpoly(f[i]*f[j],l,r)
    D=arb_mat([[arb(2*i+1) if i==j else arb(0) for j in range(size)] for i in range(size)])
    rawG=full-C*D*C.transpose()
    Q=arb_mat(C);q0=-(2*arb.pi()*a).log()-arb.const_euler()
    for i in range(size):Q[i,i]+=(sum((arb(1)/k for k in range(1,i+1)),arb(0))+q0)/(2*i+1)
    moments=[ball(x,scale) for x in data['raw_low_moments']]
    for parity,label in enumerate(('even','odd')):
        ix=list(range(parity+2,size,2));change=arb_mat(size,len(ix))
        for j,k in enumerate(ix):
            change[k,j]=arb(2*k+1).sqrt();change[parity,j]=-arb(2*k+1).sqrt()*moments[k]/moments[parity]
        L=change.transpose()*Q*change;G=change.transpose()*rawG*change
        for i in range(len(ix)):
            for j in range(len(ix)):
                check(label+' independently assembled low '+str((i,j)),L[i,j].overlaps(ball(data['parities'][label]['A'][i][j],scale)))
                check(label+' independently assembled full Gram '+str((i,j)),G[i,j].overlaps(ball(data['parities'][label]['complete_model_raw_high_Gram'][i][j],scale)))
    result={'status':'PASS','scope':'small degree N=15, Gamma M=16; normalization and independent complete-function Gram assembly only',
            'check_count':len(checks),'checks':checks,'full_terminal_positivity_claimed':False}
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(str(len(checks))+' new-endpoint normalization and independent assembly checks PASS')


if __name__=='__main__':main()
