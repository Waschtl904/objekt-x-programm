"""Independent rational checks of saved K metrics and scalar budget bounds.

No historical integration, S0 reconstruction, full archive replay or L0.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib, json, time

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'source'

def need(ok,label):
    if not ok: raise AssertionError(label)

def matrix(a): return [[F(x) for x in row] for row in a]
def mm(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]

def ldl(a):
    n=len(a)
    need(all(len(r)==n for r in a),'square')
    need(all(a[i][j]==a[j][i] for i in range(n) for j in range(n)),'symmetry')
    L=[[F(int(i==j)) for j in range(n)] for i in range(n)];D=[]
    for j in range(n):
        d=a[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),F(0))
        need(d>0,('positive pivot',j));D.append(d)
        for i in range(j+1,n):
            L[i][j]=(a[i][j]-sum((L[i][k]*D[k]*L[j][k] for k in range(j)),F(0)))/d
    return D

def upper_sqrt(x):
    need(x>=0,'radicand')
    S=10**70;n=isqrt(x.numerator*S*S//x.denominator)
    if F(n*n,S*S)<x:n+=1
    ans=F(n,S);need(ans*ans>=x,'upper square root');return ans

def upper_log(x):
    need(x>=1,'log argument');k=0
    while x>2:x/=2;k+=1
    def atanh_series(y):
        z=(y-1)/(y+1);power=z;ans=F(0)
        for j in range(128):
            ans+=power/F(2*j+1);power*=z*z
        return 2*(ans+power/(257*(1-z*z)))
    return atanh_series(x)+k*atanh_series(F(2))

def direct(A,end2,t):
    e=upper_sqrt(F(end2));J=2*((e+F(7,10))**2+end2)
    small=A*(t**3/3+t*t/4)+2*upper_sqrt(A*J*t)*(2*t*t/5+t/3)+J*(t*t/2+t/2)
    return small+4*(1-t+upper_log(1/t)/2+F(35,24))+3

def ceil6(x):return F(-((-x.numerator*10**6)//x.denominator),10**6)

def main():
    started=time.monotonic()
    bindings=json.loads((SRC/'SOURCE_BINDINGS.json').read_bytes())
    hashes={}
    for f in sorted(SRC.rglob('*')):
        if not f.is_file():continue
        rel=str(f.relative_to(SRC))
        if rel not in bindings['files']:continue
        raw=f.read_bytes();h=hashlib.sha256(raw).hexdigest()
        need(h==bindings['files'][rel]['sha256'],('source hash',rel))
        need(len(raw)==bindings['files'][rel]['bytes'],('source bytes',rel));hashes[rel]=h
    budget=json.loads((SRC/'original/gpt2-kp-budgets/expected/BUDGET_BOUNDS.json').read_bytes())
    data=json.loads((SRC/'original/gpt2-kp-und-kohaerenter-transport/expected/COHERENT_TRANSPORT_INPUTS.json').read_bytes())
    need(data['rule_id']==budget['rule_id']=='A9_A11_N12_MIDPOINT_INVERSE_60_V1','fixed rule')
    direct_bounds=[direct(F(1+200*(2*n+1)*n*(n+1)),F(5*(2*n+1)),F(1,10*(n+1)**2)) for n in range(12)]
    whole=direct(F(1+100*12**2*(12**2-1)),F(5*12**2),F(1,1440))
    result={
      'head':'92a274b247c1511ef0fe2402273df54887e2fe20',
      'scope':'Exact algebra and scalar budgets from stored inputs; historical operator/source integrations and eta bounds inherited. No S0 reconstruction or full six archive replays.',
      'source_hashes_checked':hashes,'parities':{}}
    identity=[[F(int(i==j)) for j in range(12)] for i in range(12)]
    for par in ('even','odd'):
        d=data['parities'][par];b=budget['parities'][par]
        K=matrix(d['K_rational']);Ki=matrix(d['K_inverse_rational'])
        need(len(K)==len(Ki)==12,'dimension')
        need(ldl(K)==list(map(F,d['K_positive_pivots'])),'exact positive pivots')
        need(mm(K,Ki)==identity and mm(Ki,K)==identity,'both inverse products')
        for t in ('v','p'):
            ds=d['directions'][t];eta=F(ds['eta_K_norm_upper']);need(eta>0,'eta')
            G=matrix(ds['metric_G_equals_eta_squared_K_inverse'])
            need(G==[[eta*eta*x for x in row] for row in Ki],('metric scaling',par,t))
            fallback=F(ds['Euclidean_fallback_multiplier_upper'])
            need(fallback**2>=sum((G[i][i] for i in range(12)),F(0)),'fallback trace')
        q=F(b['q']);err=F(b['two_sided_K_model_error_upper']);eps=F(b['D_model_scalar_error_upper'])
        need(q==F(d['q']) and q>0 and err>=0 and eps>=0,'positive budget inputs')
        need(all(F(x[0])>0 for x in b['S_model_positive_pivots']),'stored S0 pivot intervals positive (not reconstructed)')
        for n,row in enumerate(b['individual_directions']):
            B=F(row['K_P_upper_for_W_unit_direction']);threshold=F(row['exclusion_if_model_pairing_distance_exceeds'])
            need(B==ceil6(direct_bounds[n]+err),('independent direct upper',par,n))
            need(threshold==ceil6(upper_sqrt(F(10,11)*q*B)+eps),('independent threshold',par,n))
            need(threshold>eps and (threshold-eps)**2>F(10,11)*q*B,('strict sufficient threshold',par,n))
        need(F(b['all_degree_at_most_11_K_P_upper_per_W_norm_squared'])==ceil6(whole+err)==F('29.603644'),'whole-space bound')
        need(d['z0_budget']==b['individual_directions'][0],'same exact z0 budget record')
        need(F(d['safe_sufficient_distance_for_z0'])==F(b['individual_directions'][0]['exclusion_if_model_pairing_distance_exceeds']),'same z0 threshold')
        result['parities'][par]={'positive_K_pivots':12,'inverse_product_entries_checked':288,'metric_entries_checked':288,'budgets_checked':13,'thresholds_checked':12,'z0':b['individual_directions'][0]}
        print(par,'PASS: exact K algebra, G_v/G_p and scalar budget thresholds',flush=True)
    need(data['L0_computed'] is False and data['pairings_H_star_h_integrated'] is False,'no false pairing completion')
    result['status']='PASS_SCOPED_INDEPENDENT_ALGEBRA_AND_BUDGET_CHECKS'
    result['L0_computed']=False
    (ROOT/'CHECK_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('PASS; elapsed seconds:',round(time.monotonic()-started,2),'source hashes:',len(hashes),flush=True)

if __name__=='__main__':main()
