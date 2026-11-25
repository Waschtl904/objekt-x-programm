"""Cross-check raw arithmetic using one-dimensional polynomial correlations."""
import gzip
import json
import sys
from math import comb, factorial
from pathlib import Path
from flint import arb,arb_poly,ctx,fmpq


def compare(data):
    ctx.prec=1536
    b=arb(11).log()/2
    monomial=arb_poly([0,1])
    one_minus=arb_poly([1,-1])
    leg=[arb_poly([1]),monomial]
    for n in range(1,10):
        leg.append(((2*n+1)*monomial*leg[-1]-n*leg[-2])*(arb(1)/(n+1)))
    def moment(p,parity):
        ans=arb(0)
        for k in range(parity,246,2):
            ans+=(b/2)**k/factorial(k)*sum((v/(j+k+1) for j,v in enumerate(p) if (j+k)%2==0),arb(0))
        return ans+arb(0,arb("1e-440"))
    def source(n):
        p=n%2
        multiplier=-arb(2*n+1).sqrt()*moment(leg[n],p)/moment(leg[p],p)
        return arb(2*n+1).sqrt()*leg[n]+multiplier*leg[p],multiplier
    def corr(A,B):
        out=arb_poly([])
        for i,v in enumerate(A):
            for j,w in enumerate(B):
                for k in range(j+1):
                    m=i+k+1
                    out+=v*w*comb(j,k)*monomial**(j-k)*(one_minus**m-(-1)**m)*(arb(1)/m)
        return out
    kernel=arb_poly([arb(fmpq(v))*(b/2)**i for i,v in enumerate(data["Gamma_polynomial_coefficients"])])
    q0=-(2*arb.pi()*b).log()-arb.const_euler()
    results=[]
    for n,m in [(2,2),(2,6),(6,8),(3,3),(3,7),(7,9)]:
        A,c=source(n)
        B,d=source(m)
        p=n%2
        AB=A*B
        val=arb(0)
        for j,v in enumerate(AB):
            if not j%2:
                val+=v*(q0+sum((arb(1)/(2*k+1) for k in range(j//2+1)),arb(0))-arb(2).log())/(j+1)
        val+=c*d*p/(2*p+1)
        if n==m:
            val+=sum((arb(1)/j for j in range(1,n+1)),arb(0))
        form=corr(A,B)+corr(B,A)
        val-=b/2*(form*kernel).integral()(2)
        for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]:
            val-=arb(prime).log()/arb(q).sqrt()*form(arb(q).log()/b)/2
        lo,hi=map(int,data["parities"][("even","odd")[p]]["A"][(n-p-2)//2][(m-p-2)//2])
        den=10**data["scale_digits"]
        assert val>arb(fmpq(lo,den)) and val<arb(fmpq(hi,den)),(n,m,val.str(25))
        results.append([n,m])
    return results

if __name__=="__main__":
    print(compare(json.loads(gzip.decompress(Path(sys.argv[1]).read_bytes()))))
