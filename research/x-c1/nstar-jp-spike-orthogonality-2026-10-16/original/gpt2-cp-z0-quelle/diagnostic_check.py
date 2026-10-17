"""Independent floating-point integration checks, NOT directed certificates."""
import math,json
from pathlib import Path
from fractions import Fraction as F
import cp_z0 as c

def mid(x):return float(F(x.lo+x.hi,2*c.sc.S))
def gauss(n):
    nodes=[]
    for i in range(1,n+1):
        x=math.cos(math.pi*(i-.25)/(n+.5))
        for _ in range(30):
            p0,p1=1.,x
            for k in range(2,n+1):p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
            dp=n*(x*p1-p0)/(x*x-1);step=p1/dp;x-=step
            if abs(step)<2e-16:break
        p0,p1=1.,x
        for k in range(2,n+1):p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
        dp=n*(x*p1-p0)/(x*x-1)
        nodes.append((x,2/((1-x*x)*dp*dp)))
    assert abs(sum(w for x,w in nodes)-2)<1e-13
    return nodes
RULES={n:gauss(n) for n in (64,128)}
def integral(fun,l,r,n):
    return (r-l)/2*math.fsum(w*fun((l+r)/2+(r-l)*x/2) for x,w in RULES[n])
def direct(x,sigma,n):
    a=math.log(3);b=math.log(11)/2;eps=(-1)**sigma
    m=(lambda y:math.cosh(y/2)) if sigma==0 else (lambda y:math.sinh(y/2))
    mu=(math.sinh(a)+eps*a)/2
    L=2*((math.sinh(b/2)-math.sinh(a/2)) if sigma==0 else (math.cosh(b/2)-math.cosh(a/2)))
    B=1/math.sqrt(2*(b-a+L*L/mu));A=-B*L/mu
    def u(y):
        if abs(y)<a:return A*m(y)
        if abs(y)<b:return B*(1 if y>=0 else eps)
        return 0.
    ux=u(x)
    def kernel(r):return math.exp(-r/2)/(-math.expm1(-2*r))
    def integrand(r):
        diff=-4*A*m(x)*math.sinh(r/4)**2 if r<a-x else 2*ux-u(x+r)-u(x-r)
        return kernel(r)*diff
    cuts=sorted(set([0.,a-x,a+x,b-x,b+x]));value=0.
    for l,r in zip(cuts,cuts[1:]):
        # Geometric subdivision resolves small distances to a support jump.
        pieces=[l]
        if l>0:
            while pieces[-1]*2<r:pieces.append(pieces[-1]*2)
        pieces.append(r)
        value+=math.fsum(integral(integrand,ll,rr,n) for ll,rr in zip(pieces,pieces[1:]))
    last=cuts[-1]
    value+=integral(lambda t:2*ux*kernel(last+t/(1-t))/(1-t)**2,0.,1.,n)
    shifts=math.fsum(math.log(pr)/math.sqrt(q)*(u(x+math.log(q))+u(x-math.log(q))) for q,pr in c.CHANNELS)
    return value-shifts
def main():
    cuts=[c.I(0)]+[v for _,v in c.interior_cuts()]+[c.geometry(0)['a']]
    rows=[]
    for sigma in (0,1):
        for j,(l,r) in enumerate(zip(cuts,cuts[1:])):
            x=(l+r)/2;formula=mid(c.raw_source(x,sigma));xfloat=mid(x)
            d64=direct(xfloat,sigma,64);d128=direct(xfloat,sigma,128)
            assert abs(d128-formula)<1e-9,(sigma,j,d128,formula)
            assert abs(d128-d64)<1e-9,(sigma,j,d128,d64)
            rows.append({'parity':sigma,'cell':j,'x':xfloat,'formula':formula,
                'direct_128_minus_formula':d128-formula,'direct_128_minus_64':d128-d64})
    out={'status':'PASS_NUMERICAL_DIAGNOSTIC_ONLY','direct_integral_comparisons':len(rows),
        'maximum_absolute_difference':max(abs(r['direct_128_minus_formula']) for r in rows),
        'directed_quadrature_remainder_proved':False,'rows':rows}
    (Path(__file__).parent/'DIAGNOSTIC_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(out['status'],out['direct_integral_comparisons'],out['maximum_absolute_difference'])
if __name__=='__main__':main()
