"""Outward fixed-grid rational LDL checks; no numerical runtime required."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse,hashlib
HERE=Path(__file__).resolve().parent
SCALE=10**45

def ceildiv(a,b):return -((-a)//b)
def point(q):
    q=F(q);v=q.numerator*SCALE
    return (v//q.denominator,ceildiv(v,q.denominator))
def interval(v):return (point(v[0])[0],point(v[1])[1])
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    z=[a*b for a in x for b in y]
    return (min(z)//SCALE,ceildiv(max(z),SCALE))
def div(x,y):
    assert y[0]>0
    z=[(a*SCALE,b) for a in x for b in y]
    return (min(a//b for a,b in z),max(ceildiv(a,b) for a,b in z))
ZERO=(0,0);ONE=(SCALE,SCALE)

def positive(A):
    n=len(A);L=[[ZERO]*n for _ in range(n)];D=[]
    for j in range(n):
        d=A[j][j]
        for k in range(j):d=sub(d,mul(mul(L[j][k],D[k]),L[j][k]))
        assert d[0]>0,('unproved positive pivot',j,d)
        D.append(d);L[j][j]=ONE
        for i in range(j+1,n):
            q=A[i][j]
            for k in range(j):q=sub(q,mul(mul(L[i][k],D[k]),L[j][k]))
            L[i][j]=div(q,d)
    return {'positive_pivots':n,'smallest_pivot_lower':str(F(min(d[0] for d in D),SCALE))}

def read(p):return json.loads(p.read_bytes())
def imat(a):return [[interval(v) for v in row] for row in a]
def test_matrix(A,B=None,scalar=ONE,error=ZERO):
    return [[sub(sub(mul(scalar,A[i][j]),B[i][j] if B else ZERO),error if i==j else ZERO)
             for j in range(len(A))] for i in range(len(A))]

def audit(label):
    d=read(HERE/f'GALERKIN_{label}_3072.json');B=imat(d['B84_model']);R=imat(d['R84_model'])
    eb=interval(d['B84_operator_error_scalar']);er=interval(d['R84_operator_error_scalar'])
    lo=point(d['B84_certified_lower_scalar']);hi=point(d['B84_certified_upper_scalar'])
    checks={'B84_lower':positive(test_matrix(B,error=add(eb,lo))),
            'B84_upper':positive([[sub(sub(hi if i==j else ZERO,B[i][j]),eb if i==j else ZERO)
                                 for j in range(84)] for i in range(84)])}
    if d['finite_R84_le_B84_certified_by_directed_LDL']:
        checks['original_finite_gate']=positive(test_matrix(B,R,error=add(eb,er)))
    opt=d['optional_positive_potential_comparison'];V=imat(opt['potential84_model'])
    eta=point(F(9999999999,10**10))
    BP=[[add(B[i][j],mul(eta,V[i][j])) for j in range(84)] for i in range(84)]
    ep=interval(opt['Bplus_operator_error_scalar']);ell=point(opt['finite_generalized_eigenvalue_upper_rational'])
    checks['potential_finite_eigenvalue_upper']=positive(test_matrix(BP,R,ell,add(mul(ell,ep),er)))
    if opt['finite_R84_le_Bplus84_certified']:
        checks['potential_finite_gate']=positive(test_matrix(BP,R,error=add(ep,er)))
    diagnostic=read(HERE/'BRIDGE_DIAGNOSTIC.json')
    proposal=next(c for c in diagnostic['cases'] if c['parity']==label.lower())
    assert proposal['galerkin_sha256']==hashlib.sha256((HERE/f'GALERKIN_{label}_3072.json').read_bytes()).hexdigest()
    assert proposal['stronger_bridge_proved'] is False
    if proposal['status']=='CONDITIONAL_FINITE_GATE_PASSES_WITH_STRONGER_Q8':
        nr=imat(proposal['conditional_R84_model']);nell=point(proposal['finite_generalized_eigenvalue_upper'])
        checks['conditional_stronger_Q8_gate']=positive(test_matrix(BP,nr,error=add(ep,er)))
        checks['conditional_stronger_Q8_eigenvalue_upper']=positive(test_matrix(BP,nr,nell,add(mul(nell,ep),er)))
    assert len(d['X_rational'])==84 and all(len(row)==203 for row in d['X_rational'])
    assert len(opt['Xplus_rational'])==84 and all(len(row)==203 for row in opt['Xplus_rational'])
    return {'parity':label.lower(),'checks':checks,'full_remainder_certified':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--parity',choices=['even','odd']);args=ap.parse_args()
    labels=[args.parity.upper()] if args.parity else ['EVEN','ODD']
    out={'status':'PASS_RATIONAL_POSITIVE_BLOCKS','decimal_grid_digits':45,
         'cases':[audit(label) for label in labels],'full_remainder_certified':False}
    dest=HERE/('POSITIVE_BLOCK_AUDIT_'+args.parity.upper()+'.json' if args.parity else 'POSITIVE_BLOCK_AUDIT.json')
    dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2),flush=True)
