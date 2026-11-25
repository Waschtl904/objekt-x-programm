import json
from fractions import Fraction as Q
from pathlib import Path
from flint import arb, arb_poly, ctx


def value(x):
    f=Q(str(x))
    return arb(f.numerator)/f.denominator


def reflected_tail(raw, norm_lo, N):
    # The direct recurrence is outward-rounded at 8192 bits, including the cutoff.
    a=arb(3).log()
    b=arb(11).log()/2
    xi=(arb(10).log()-b-a)/(b-a)
    eta=2*xi-1
    pol=[arb_poly([1]),arb_poly([0,1])]
    for j in range(1,len(raw)-1):
        pol.append(((2*j+1)*arb_poly([0,1])*pol[-1]-j*pol[-2])*(arb(1)/(j+1)))
    src=sum((value(c)*arb(2*j+1).sqrt()*pol[j] for j,c in enumerate(raw)),arb_poly([]))
    target=src(arb_poly([2*xi,-1]))
    total_primitive=(src*src).integral()
    total=(total_primitive(1)-total_primitive(eta))/2
    max_n=N+len(raw)
    P=[arb(1),eta]
    for n in range(1,max_n+1):
        P.append(((2*n+1)*eta*P[-1]-n*P[-2])/(n+1))
    base=[1-xi]+[(P[n-1]-P[n+1])/(2*(2*n+1)) for n in range(1,max_n+1)]
    weights=list(target)
    moments=[weights[-1]*v for v in base]
    for coefficient in reversed(weights[:-1]):
        old=moments
        moments=[old[1]+coefficient*base[0]]
        for n in range(1,len(old)-1):
            moments.append((n*old[n-1]+(n+1)*old[n+1])/(2*n+1)+coefficient*base[n])
    tail_sq=total-sum((2*n+1)*moments[n]**2 for n in range(N))
    assert tail_sq>0
    return tail_sq.sqrt()/value(norm_lo)

if __name__=='__main__':
    import sys
    ctx.prec=8192
    energy=json.loads(Path(sys.argv[1]).read_bytes())
    norm={'e':'1', 's':'9999.871371863025338'}
    for key in ('e','s'):
        result=reflected_tail(energy['trial_'+key]['raw'],norm[key],4096)
        scale=2*arb(2).log()*arb(5).log()/(arb(10).sqrt()*value('1.84298'))
        print(key,result.str(17), (scale*result).str(17),flush=True)

