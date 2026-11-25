"""Whole-interval weighted Schur bound for the seven raw prime translations."""
import math
from flint import arb, fmpq


def row_bound(cells=512):
    a=arb(11).log()/2
    channels=[(arb(q).log()/a,arb(p).log()/arb(q).sqrt()) for q,p in
              [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]]
    edges=[arb(i)/cells for i in range(cells+1)]
    potential=[-(1-x*x).log()/2 for x in edges[:-1]]
    stencils=[]
    for i,(l,r) in enumerate(zip(edges,edges[1:])):
        row=[]
        for d,w in channels:
            for s in (-1,1):
                x=l+s*d
                z=r+s*d
                if x>1 or z< -1:
                    continue
                if x>=0:
                    lo,hi=x,z
                elif z<=0:
                    lo,hi=-z,-x
                else:
                    assert x<0 and z>0
                    lo=arb(0)
                    hi=max((-x).upper(),z.upper())
                lo=int((lo*cells).lower().floor().unique_fmpz())
                hi=int((hi*cells).upper().floor().unique_fmpz())
                ix=list(range(max(0,lo),min(cells-1,hi)+1))
                assert ix
                row.append((ix[0],ix[-1],w))
        stencils.append(row)
    # Only the final positive rational test enters the proof.
    float_rows=[[(j,k,float(w)) for j,k,w in row] for row in stencils]
    diag=[8-float(v) for v in potential]
    weights=[1.0]*cells
    for _ in range(220):
        new=[diag[i]*weights[i]+sum(w*max(weights[j:k+1]) for j,k,w in row) for i,row in enumerate(float_rows)]
        scale=max(new)
        weights=[x/scale for x in new]
    weights=[max(1,round(x*10**9)) for x in weights]
    caps=[sum((w*max(weights[j:k+1]) for j,k,w in row),arb(0))/weights[i]-potential[i]
          for i,row in enumerate(stencils)]
    cap=max(v.upper() for v in caps)
    assert all(v < arb(fmpq(295,100)) for v in caps)
    return cap


if __name__=="__main__":
    print(row_bound())
