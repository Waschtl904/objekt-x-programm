"""Certify the unchanged sufficient A11 matrix by an exact rational congruence.

Midpoints propose a unit triangular preconditioner only. The final proof
uses the original full intervals, directed products, Gershgorin, and LDL.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json,gzip,hashlib,time
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(100000)
from flint import arb,arb_mat,fmpq,ctx
from check_a11 import ball,af
from generate_a11 import interval

def ldl(a):
    """Use interval multiplication for squares, including zero-midpoint balls."""
    n=a.nrows();low=[[arb(0) for _ in range(n)] for _ in range(n)];piv=[]
    for i in range(n):
        d=a[i,i]-sum((low[i][k]*low[i][k]*piv[k] for k in range(i)),arb(0))
        if not d>0:return low,piv,d
        piv.append(d);low[i][i]=arb(1)
        for j in range(i+1,n):
            low[j][i]=(a[j,i]-sum((low[j][k]*low[i][k]*piv[k] for k in range(i)),arb(0)))/d
    return low,piv,None

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ctx.prec=3072;p=Path(__file__).resolve().parent
    original=json.loads((p/'reserve_results.json').read_bytes())
    raw=json.loads(gzip.decompress((p/'reserve_results_lower_matrices.json.gz').read_bytes()))
    model=json.loads(gzip.decompress((p/'a11_model.json.gz').read_bytes()))
    tail=json.loads((p/'CHECK_RESULTS.json').read_bytes())
    checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    zero_ball=arb(0,arb('1e-100'))
    check('zero-midpoint interval product is finite and contains zero',(zero_ball*zero_ball).is_finite() and (zero_ball*zero_ball).contains(0))
    check('original model bound',sha(p/'a11_model.json.gz')==original['model_sha256'])
    check('original sufficient-matrix checker bound',sha(p/'check_a11.py')==original['checker_sha256'])
    check('original tail receipt unchanged',sha(p/'CHECK_RESULTS.json')==original['refined_tail_binding_sha256'])
    check('all tail source files unchanged',all(sha(p/name)==value for name,value in tail['file_sha256'].items()))
    scale=10**100;transformed={'scale_digits':100,'preconditioner_scale_digits':100,'parities':{}}
    report=dict(original);report['checks']=checks;report['parities']={}
    report.update(status='RATIONAL_CONGRUENCE_CERTIFICATE_ANALYTIC_REVIEW_OPEN',
                  checker_sha256=sha(Path(__file__)),original_raw_check_sha256=sha(p/'reserve_results.json'),
                  original_checker_sha256=original['checker_sha256'],
                  raw_lower_matrix_sha256=sha(p/'reserve_results_lower_matrices.json.gz'),
                  proof_sha256=sha(p/'PRECONDITIONING.md'),
                  pivot_basis='exact rational unit-upper-triangular congruence of the unchanged sufficient matrix')
    for label in ['even','odd']:
        start=time.time();source=raw['parities'][label]['lower_matrix'];n=len(source)
        check(label+' dimension 285',n==285)
        midpoint=arb_mat([[arb(fmpq(int(x[0])+int(x[1]),2*scale)) for x in row] for row in source])
        low,piv,fail=ldl(midpoint)
        check(label+' midpoint provides preconditioner candidate only',fail is None and len(piv)==n)
        integers=[[0]*n for _ in range(n)]
        for k in range(n):
            col=[arb(0)]*n
            for i in range(k,n):
                col[i]=(arb(1) if i==k else arb(0))-sum((low[i][j]*col[j] for j in range(k,i)),arb(0))
                integers[k][i]=scale if i==k else int((col[i].mid()*scale).lower().floor().unique_fmpz())
        check(label+' exact unit upper triangular preconditioner',all(integers[i][i]==scale and all(integers[i][j]==0 for j in range(i)) for i in range(n)))
        P=arb_mat([[arb(fmpq(v,scale)) for v in row] for row in integers])
        full=arb_mat([[ball(x,scale) for x in row] for row in source])
        changed=P.transpose()*full*P
        changed=(changed+changed.transpose())/2
        print(label+': exact rational congruence applied to full interval matrix',flush=True)
        margins=[changed[i,i].lower()-sum((abs(changed[i,j]).upper() for j in range(n) if j!=i),arb(0)) for i in range(n)]
        print(label+': Gershgorin positive rows '+str(sum(bool(x>0) for x in margins))+'/'+str(n),flush=True)
        mu_exact=min(F(int(interval(x)[0]),scale) for x in margins)
        print(label+': minimum exact Gershgorin margin '+str(float(mu_exact)),flush=True)
        check(label+' directed Gershgorin lower bound strictly positive',all(x>0 for x in margins) and mu_exact>0)
        norm_squared=F(sum(v*v for row in integers for v in row),scale*scale)
        sigma_exact=mu_exact/norm_squared
        check(label+' exact original-coordinate spectral floor',mu_exact>0 and norm_squared>=n and sigma_exact>0)
        _,certified_pivots,failed=ldl(changed)
        print(label+': transformed LDL '+str(len(certified_pivots))+'; failure '+str(failed),flush=True)
        check(label+' all 285 full-interval congruence pivots positive',failed is None and len(certified_pivots)==n)
        eB=F(original['parities'][label]['coupling_operator_error_exact'])
        gram=model['parities'][label]['complete_model_raw_high_Gram']
        b2=F(1001,1000)*sum((F(int(gram[i][i][1]),scale) for i in range(n)),F(0))+n*1001*eB*eB
        check(label+' original coupling bound positive',b2>0)
        gap=min(af(sigma_exact),arb(1))/(4*(1+af(b2).sqrt())**2)
        eta=gap/(gap+13)
        check(label+' full physical and defect floors positive',gap>0 and eta>0)
        row=dict(original['parities'][label])
        for key in ['first_unproved_pivot','first_unproved_pivot_display','pivot_strictly_negative','meaning']:
            row.pop(key,None)
        row.update(verdict='STRICT_POSITIVE_SUFFICIENT_MATRIX_BY_RATIONAL_CONGRUENCE',
                   positive_directed_pivots=len(certified_pivots),
                   gershgorin_lower_exact=str(mu_exact),preconditioner_frobenius_squared_exact=str(norm_squared),
                   original_coordinate_schur_floor_exact=str(sigma_exact),
                   full_physical_reserve=interval(gap),full_physical_reserve_display=gap.str(40),
                   full_defect_reserve=interval(eta),full_defect_reserve_display=eta.str(40),
                   all_positive_pivot_intervals=[interval(x) for x in certified_pivots],
                   check_seconds=time.time()-start)
        report['parities'][label]=row
        transformed['parities'][label]={'dimension':n,'preconditioner_integer_grid':[[str(v) for v in row] for row in integers],
                                      'transformed_matrix':[[interval(changed[i,j]) for j in range(n)] for i in range(n)]}
        print(label+': 285 positive pivots; physical '+gap.str(24)+'; defect '+eta.str(24),flush=True)
    path=p/'preconditioned_matrices.json.gz'
    path.write_bytes(gzip.compress((json.dumps(transformed,separators=(',',':'))+'\n').encode(),mtime=0))
    report['preconditioned_matrices_sha256']=sha(path)
    report['both_parities_strictly_certified']=True;report['check_count']=len(checks)
    (p/'preconditioned_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(str(len(checks))+' congruence certificate groups PASS',flush=True)

if __name__=='__main__':main()
