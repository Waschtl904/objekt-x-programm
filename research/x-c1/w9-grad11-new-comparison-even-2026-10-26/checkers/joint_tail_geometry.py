"""Exact frame and inverse finite-gap weights for all residual cross terms."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,time
H=Path(__file__).resolve().parent;start=time.monotonic();columns=[];receipts=[]
def dyadic(m,e):return Q(m*2**e)if e>=0 else Q(m,2**(-e))
for i in range(12):
    label='T'+str(i).zfill(2);binding=json.loads((H/(label+'_MODEL_BINDING.json')).read_bytes())
    name='whole-model-'+binding['expanded_builder_sha256'][:12]+'-n'+('128'if i==0 else'64')+'.json.gz'
    raw=(H/name).read_bytes();body=json.loads(gzip.decompress(raw));payload=body['payload'].encode()
    assert hashlib.sha256(payload).hexdigest()==body['payload_sha256']
    assert body['source_sha256']==binding['expanded_builder_sha256']
    entries=dict(json.loads(payload)['mapping']);cc=[]
    for ball in entries['cc']:
        m,e,r,s=ball['ball'];mid=dyadic(m,e);rad=dyadic(r,s)
        exact=Q(round(mid*10**100),10**100)
        assert rad<Q('1e-150')and mid-rad<=exact<=mid+rad
        cc.append(exact)
    assert len(cc)==12;columns.append(cc)
    receipts.append({'label':label,'cache':name,'sha256':hashlib.sha256(raw).hexdigest()})
N=12;B=[[columns[j][i]for j in range(N)]for i in range(N)]
raw=(H/'SOURCE_ARITHMETIC_CLOSURE.json').read_bytes();boxes=json.loads(raw)['remaining_gap']
mid=[[(Q(x[0])+Q(x[1]))/2 for x in row]for row in boxes]
rad=[sum(((Q(x[1])-Q(x[0]))/2 for x in row),Q())for row in boxes]
G=[[mid[i][j]-(rad[i]if i==j else 0)for j in range(N)]for i in range(N)]
def trans(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum((a[i][k]*b[k][j]for k in range(len(b))),Q())for j in range(len(b[0]))]for i in range(len(a))]
C=mul(mul(trans(B),G),B)
L=[[Q(int(i==j))for j in range(N)]for i in range(N)];D=[]
for j in range(N):
    p=C[j][j]-sum((L[j][k]**2*D[k]for k in range(j)),Q());assert p>0;D.append(p)
    for i in range(j+1,N):L[i][j]=(C[i][j]-sum((L[i][k]*L[j][k]*D[k]for k in range(j)),Q()))/p
A=[]
for j in range(N):
    forward=[]
    for i in range(N):forward.append(Q(int(i==j))-sum((L[i][k]*forward[k]for k in range(i)),Q()))
    x=[Q()]*N
    for i in reversed(range(N)):x[i]=forward[i]/D[i]-sum((L[k][i]*x[k]for k in range(i+1,N)),Q())
    A.append(x)
A=trans(A)
assert mul(C,A)==[[Q(int(i==j))for j in range(N)]for i in range(N)]
out={'status':'EXACT_COMMON_FRAME_FINITE_GAP_INVERSE','basis':[[str(x)for x in r]for r in B],
 'finite_gap_lower_in_basis':[[str(x)for x in r]for r in C],
 'inverse':[[str(x)for x in r]for r in A],'positive_exact_pivots':12,
 'source_closure_sha256':hashlib.sha256(raw).hexdigest(),'caches':receipts,
 'whole_residual_bound_rule':'theta = sum_ij abs(A_ij) n_i n_j; all mixed residual Gram terms are paid by Cauchy-Schwarz. Positivity needs theta<1 and every n_i closed.',
 'whole_residual_closed':False,'seconds':time.monotonic()-start}
(H/'JOINT_TAIL_GEOMETRY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('Exact positive frame pivots',12,'seconds',round(out['seconds'],1))
print('Inverse diagonal weights',[float(A[i][i])for i in range(N)])
