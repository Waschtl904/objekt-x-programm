"""Independent exact rational audit of the proposed finite error ledger."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,time
H=Path(__file__).resolve().parent;start=time.monotonic()
def bound(A,upper):
    n=len(A);mid=[[(Q(a)+Q(b))/2 for a,b in row]for row in A]
    for i in range(n):
        radius=sum((max(abs(Q(a)-mid[i][j]),abs(Q(b)-mid[i][j]))for j,(a,b)in enumerate(A[i])),Q())
        mid[i][i]+=radius if upper else-radius
    return mid
def ldl(A):
    n=len(A);L=[[Q(int(i==j))for j in range(n)]for i in range(n)];d=[]
    for j in range(n):
        v=A[j][j]-sum((L[j][k]**2*d[k]for k in range(j)),Q())
        assert v>0,('nonpositive exact pivot',j);d.append(v)
        for i in range(j+1,n):L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*d[k]for k in range(j)),Q()))/v
    return d
source=H/'SOURCE_BLOCK_LEDGER_RESERVE.json';raw=source.read_bytes();data=json.loads(raw)
model=H.parent/'fo-response-reach-2026-10-25/frozen/MODEL.json';mg=json.loads(model.read_bytes())['matrices']['G_W']
L=bound(data['matrices']['remaining_gap'],False);G=bound(mg,True);floor=Q('4e-19')
A=[[L[i][j]-floor*G[i][j]for j in range(12)]for i in range(12)];p=ldl(A)
out={'status':'EXACT_ARITHMETIC_PASS_FOR_CANDIDATE_FINITE_LEDGER',
 'positive_rational_pivots':len(p),'proved_W_floor_for_stored_ledger':str(floor),
 'ledger_sha256':hashlib.sha256(raw).hexdigest(),'physical_metric_sha256':hashlib.sha256(model.read_bytes()).hexdigest(),
 'analytical_source_interfaces_audited_here':False,'infinite_remainder_included':False,
 'rational_pivots':[str(v)for v in p],'seconds':time.monotonic()-start}
(H/'SOURCE_GAP_EXACT_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items()if k!='rational_pivots'},indent=2))
