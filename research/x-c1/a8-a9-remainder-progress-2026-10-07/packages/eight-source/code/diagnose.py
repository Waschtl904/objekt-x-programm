"""Floating-point direction search followed by exact rational directional bounds."""
from pathlib import Path
from fractions import Fraction as F
import json, math, argparse
from audit_eight import bound, quadratic, serialize

def tr(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def chol(a):
    n=len(a);l=[[0.]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            v=a[i][j]-sum(l[i][k]*l[j][k] for k in range(j))
            l[i][j]=math.sqrt(v) if i==j else v/l[j][j]
    return l
def invlow(a):
    n=len(a);b=[[0.]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):b[i][j]=((1. if i==j else 0.)-sum(a[i][k]*b[k][j] for k in range(i)))/a[i][i]
    return b
def eigen(a):
    a=[r[:] for r in a];n=len(a);v=[[float(i==j) for j in range(n)] for i in range(n)]
    for _ in range(100):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1e-28:break
        theta=.5*math.atan2(2*a[p][q],a[q][q]-a[p][p]);c=math.cos(theta);s=math.sin(theta)
        R=[[float(i==j) for j in range(n)] for i in range(n)]
        R[p][p]=R[q][q]=c;R[p][q]=s;R[q][p]=-s
        a=mul(mul(tr(R),a),R);v=mul(v,R)
    order=sorted(range(n),key=lambda i:a[i][i])
    return [(a[k][k],[v[i][k] for i in range(n)]) for k in order]
def mids(a):return [[float(sum(map(F,v))/2) for v in row] for row in a]
def direction(a,w):
    li=invlow(chol(w));ee=eigen(mul(mul(li,a),tr(li)));d=[]
    for val,vec in ee:d.append((val,[sum(li[j][i]*vec[j] for j in range(len(li))) for i in range(len(li))]))
    return d
def directional(a,y):return [quadratic(bound(a,-1),y),quadratic(bound(a,1),y)]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--result',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();r=json.loads(args.result.read_bytes());records=r['blocks'] if 'blocks' in r else [r];res=[]
    for r in records:
        w=mids(r['reference_gram']);e=direction(mids(r['S_lower']),w)
        proposals=[]
        for val,v in e:
            y=[F(round(x*10**12),10**12) for x in v]
            ds={key:directional(r[key],y) for key in ['reference_gram','S_lower','K_model','K_lower','K_upper','D_model','D_lower','D_upper','Gamma_upper','old_source_inverse_energy_upper','corrected_source_energy_upper','force_error_gram_upper','true_high_gram_upper']}
            ds['full_residual_norm_squared']=directional(r['full_residual']['complete_true_residual_gram'],y)
            proposals.append({'search_ritz_value_approx':val,'rational_direction':y,'exact_directional_intervals':ds,
                'negative_actual_form_witness':ds['K_upper'][1]<0,'negative_lower_bound_only':ds['S_lower'][1]<0 and ds['K_upper'][0]>0})
        res.append({'parity':r['parity'],'approximate_generalized_lower_eigenvalues':[x[0] for x in e],
                    'approximate_generalized_K_model_eigenvalues':[x[0] for x in direction(mids(r['K_model']),w)],'directions':proposals})
    out={'status':'DIRECTION_SEARCH_WITH_EXACT_DIRECTIONAL_EVALUATION','blocks':res,'eigenvectors_certified':False,'scope':'Directions are diagnostics; negative lower enclosures are not negative actual-form witnesses.'}
    args.out.write_text(json.dumps(serialize(out),indent=2)+'\n',encoding='utf-8')
    for r in res:
        d=r['directions'][0]['exact_directional_intervals']
        print(r['parity'], 'S lower spectrum',r['approximate_generalized_lower_eigenvalues'],'K model spectrum',r['approximate_generalized_K_model_eigenvalues'])
        print('weak direction budgets', {k:[float(v) for v in x] for k,x in d.items()})
if __name__=='__main__':main()
