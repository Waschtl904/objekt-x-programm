"""Exact independent geometry check for all core contours and saved nodes."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
H=Path(__file__).resolve().parent
frame=json.loads((H/'JOINT_TAIL_GEOMETRY.json').read_bytes());baseline=None;rows=[]
def dyadic(m,e):return Q(m*2**e)if e>=0 else Q(m,2**(-e))
def ball(obj):
    m,e,r,s=obj['ball'];m=dyadic(m,e);r=dyadic(r,s);return m-r,m+r
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def scale(x,t):return (x[0]*t,x[1]*t)if t>=0 else(x[1]*t,x[0]*t)
def abshi(x):return max(abs(x[0]),abs(x[1]))
def abslo(x):return Q()if x[0]<=0<=x[1]else min(abs(x[0]),abs(x[1]))
for i,item in enumerate(frame['caches']):
    raw=(H/item['cache']).read_bytes();assert hashlib.sha256(raw).hexdigest()==item['sha256']
    body=json.loads(gzip.decompress(raw));payload=body['payload'].encode();assert hashlib.sha256(payload).hexdigest()==body['payload_sha256']
    v=dict(json.loads(payload)['mapping'])
    geometry={name:v[name]for name in ['a','b','edges','channels']}
    if baseline is None:baseline=geometry
    else:assert geometry==baseline
    a,b=ball(v['a']),ball(v['b']);edges=list(map(ball,v['edges']));order=128 if i==0 else 64
    panels=[(lo,hi,order,Q(2))for lo,hi in zip(edges[:-2],edges[1:-1])]
    width=sub(a,edges[-2]);R=Q(2)if i==0 else Q(23,8)
    panels +=[(sub(a,scale(width,Q(1,2**k))),sub(a,scale(width,Q(1,2**(k+1)))),max(24,order//2),R)for k in range(48)]
    pos=0;active=0;minimum=None
    for lo,hi,n,R in panels:
        center=scale(add(lo,hi),Q(1,2));radius=scale(sub(hi,lo),Q(1,2))[1]
        re=add(center,(-R*radius,R*radius));imag=R*radius
        gap=a[0]-abshi(re);assert gap>0
        minimum=gap if minimum is None else min(minimum,gap)
        square=abshi(re)**2+imag**2
        assert square<(Q(6,5)*a[0])**2
        assert square<(Q(11,5)-b[1])**2
        for sh,_ in v['channels']:
            for sign in (-1,1):
                shifted=add(center,scale(ball(sh),sign))
                if abshi(shifted)<a[0]:
                    active+=1;sr=add(shifted,(-R*radius,R*radius))
                    assert abshi(sr)**2+imag**2<(Q(6,5)*a[0])**2
                else:assert abslo(shifted)>a[1]
        for _ in range(n):
            node=ball(v['hpoints'][pos][0]);pos+=1
            assert lo[1]<node[0]<=node[1]<hi[0]
    assert pos==len(v['hpoints'])
    rows.append({'label':item['label'],'panels':len(panels),'saved_nodes_strictly_inside_cells':pos,
                 'active_prime_contours_checked':active,'minimum_endpoint_distance':str(minimum),
                 'model_sha256':item['sha256']})
    print(item['label'],'exact contour and node geometry PASS',flush=True)
out={'status':'EXACT_NEW_CORE_CONTOURS_AND_ATOM_MEMBERSHIP_PASS','directions':rows,
     'same_geometry_in_all_models':True,'scope':'New radius 23/8 product contours remain in the inherited Qm and Gamma domains; analytic kernel inequalities themselves are inherited.'}
(H/'CORE_GEOMETRY_EXACT_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
