"""Exact checks of saved geometry enclosures; no operator certification."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib

def lower(m):
    n=len(m);assert all(len(row)==n for row in m)
    out=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        radius=F(0)
        for j in range(n):
            a,b=map(F,m[i][j]);assert a<=b
            assert m[i][j]==m[j][i]
            out[i][j]=(a+b)/2;radius+=(b-a)/2
        out[i][i]-=radius
    return out

def pivots(m):
    a=[row[:] for row in m];ds=[]
    for k in range(len(a)):
        d=a[k][k];assert d>0,(k,d)
        ds.append(str(d))
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                a[i][j]-=a[i][k]*a[k][j]/d
    return ds

def pairs(x,y,path=''):
    count=0
    if isinstance(x,list):
        assert isinstance(y,list) and len(x)==len(y),path
        if len(x)==2 and all(isinstance(z,str) for z in x):
            a,b=map(F,x);c,d=map(F,y)
            assert a<=b and c<=d and max(a,c)<=min(b,d),path
            return 1
        for i,(a,b) in enumerate(zip(x,y)):count+=pairs(a,b,path+'/'+str(i))
    elif isinstance(x,dict):
        assert x.keys()==y.keys()
        for k in x:
            if k!='bits':count+=pairs(x[k],y[k],path+'/'+k)
    else:assert x==y,path
    return count

def run():
    root=Path(__file__).resolve().parent
    protocol=root/'PROTOCOL.json'
    ps=json.loads(protocol.read_bytes())
    assert ps['right_shell_legendre_seed_degrees']==list(range(4,12))
    digest=hashlib.sha256(protocol.read_bytes()).hexdigest()
    docs=[json.loads((root/f'GEOMETRY_{bits}.json').read_bytes()) for bits in (768,1024)]
    count=pairs(docs[0],docs[1])
    checked=[]
    for d in docs:
        assert d['status']=='PASS_FIXED_PILOT_GEOMETRY_ONLY'
        assert d['protocol_sha256']==digest
        assert d['program_sha256']==hashlib.sha256((root/'geometry.py').read_bytes()).hexdigest()
        assert d['source_quotient_sha256']==hashlib.sha256((root/'inputs/QUOTIENT_NORM.json').read_bytes()).hexdigest()
        assert [r['parity'] for r in d['blocks']]==['even','odd']
        for r in d['blocks']:
            lo,hi=map(F,r['first_four_test_coefficients_determinant'])
            assert lo>0 or hi<0
            test=pivots(lower(r['tested_quotient_gram']))
            pilot=pivots(lower(r['raw_pilot_WX_gram']))
            checked.append({'bits':d['bits'],'parity':r['parity'],
                            'test_gram_pivots':test,'pilot_gram_pivots':pilot})
        assert not d['B00_computed'] and not d['cross_gram_computed'] and not d['tail_norm_computed']
    print(json.dumps({'status':'PASS_EXACT_GEOMETRY_ONLY','interval_pairs_compared':count,
                      'checks':checked,'full_remainder_certified':False},indent=2))

if __name__=='__main__':
    assert __debug__
    run()
