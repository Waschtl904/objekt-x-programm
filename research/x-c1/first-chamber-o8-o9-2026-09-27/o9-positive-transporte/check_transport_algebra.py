"""Exact finite algebra checks for the O9 construction; not an operator proof.

Standard library only. The infinite-dimensional proof and dependency scope
are stated in PROOF.md. No repository state is modified.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json


def matrix(rows):return [[F(x) for x in row] for row in rows]
def identity(n):return matrix([[int(i==j) for j in range(n)] for i in range(n)])
def transpose(a):return [list(row) for row in zip(*a)]
def multiply(a,b):
    assert len(a[0])==len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def difference(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def inverse(a):
    n=len(a);rows=[r[:] + s for r,s in zip(a,identity(n))]
    for j in range(n):
        pivot=next(k for k in range(j,n) if rows[k][j])
        rows[j],rows[pivot]=rows[pivot],rows[j]
        divisor=rows[j][j];rows[j]=[x/divisor for x in rows[j]]
        for k in range(n):
            if k==j:continue
            factor=rows[k][j]
            rows[k]=[x-factor*y for x,y in zip(rows[k],rows[j])]
    assert [r[:n] for r in rows]==identity(n)
    return [r[n:] for r in rows]
def positive(a):
    assert a==transpose(a)
    remaining=[row[:] for row in a]
    while remaining:
        pivot=remaining[0][0]
        if pivot<=0:return False
        remaining=[[remaining[i][j]-remaining[i][0]*remaining[0][j]/pivot for j in range(1,len(remaining))] for i in range(1,len(remaining))]
    return True


def main():
    checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    roots={
        1:matrix([['3/8']]),
        2:matrix([['3/8',0],[0,'1/2']]),
        3:matrix([['9/40',0,'3/10'],[0,'1/2',0],['3/10',0,'9/20']])
    }
    raw={}
    for a in (1,2,3):
        for b in range(a,4):raw[a,b]=matrix([[int(i==j) for j in range(a)] for i in range(b)])
    G3=multiply(roots[3],roots[3])
    grams={a:multiply(multiply(transpose(raw[a,3]),G3),raw[a,3]) for a in (1,2,3)}
    corrected={}
    for a in (1,2,3):
        check(str(a)+' positive root',positive(roots[a]))
        check(str(a)+' root below identity',positive(difference(identity(a),roots[a])))
        check(str(a)+' root square equals the compressed terminal Gram',multiply(roots[a],roots[a])==grams[a])
        for b in range(a,4):
            corrected[a,b]=multiply(multiply(roots[b],raw[a,b]),inverse(roots[a]))
            check(str((a,b))+' raw isometry',multiply(transpose(raw[a,b]),raw[a,b])==identity(a))
            check(str((a,b))+' Gram compression',multiply(multiply(transpose(raw[a,b]),grams[b]),raw[a,b])==grams[a])
            check(str((a,b))+' corrected isometry',multiply(transpose(corrected[a,b]),corrected[a,b])==identity(a))
            check(str((a,b))+' corrected source intertwining',multiply(corrected[a,b],roots[a])==multiply(roots[b],raw[a,b]))
        check(str(a)+' corrected identity',corrected[a,a]==identity(a))
    check('raw cocycle',multiply(raw[2,3],raw[1,2])==raw[1,3])
    check('corrected cocycle',multiply(corrected[2,3],corrected[1,2])==corrected[1,3])
    check('nontrivial corrected transport has expected columns',corrected[2,3]==matrix([['3/5',0],[0,1],['4/5',0]]))
    discrepancy=difference(multiply(roots[3],raw[2,3]),multiply(raw[2,3],roots[2]))
    discrepancy_sq=sum((x*x for row in discrepancy for x in row),F(0))
    check('raw square-root intertwining demonstrably fails',discrepancy_sq==F(9,80))
    range_projection=multiply(corrected[2,3],transpose(corrected[2,3]))
    check('corrected range projection is proper and idempotent',range_projection!=identity(3) and multiply(range_projection,range_projection)==range_projection)
    fixed={a:multiply(roots[3],raw[a,3]) for a in (1,2,3)}
    check('fixed terminal readout naturality',multiply(fixed[2],raw[1,2])==fixed[1])
    check('local and fixed terminal realizations agree',all(multiply(corrected[a,3],roots[a])==fixed[a] for a in (1,2,3)))
    check('unitary identifications respect the corrected cocycle',multiply(corrected[2,3],corrected[1,2])==corrected[1,3])
    check('change of terminal is compatible with corrected readout',multiply(corrected[2,3],multiply(roots[2],raw[1,2]))==fixed[1])
    c=F(12,10**30);eta=c/(c+F(23,2))
    check('inherited exact O8 reserve',eta==F(24,23*10**30+24))
    check('uniform inverse-root bound below 10^15',eta>F(1,10**30))
    result={
        'status':'EXACT_O9_ALGEBRA_CHECKS_PASS',
        'scope':'Finite rational 1->2->3 model, including a counterexample to raw square-root intertwining; scalar consequence of the inherited O8 reserve.',
        'infinite_dimensional_proof':'PROOF.md',
        'independent_O8_matrix_reproduction_performed':False,
        'raw_square_root_intertwining_discrepancy_squared':str(discrepancy_sq),
        'common_O8_defect_floor_exact':str(eta),
        'inverse_square_root_norm_upper_strict':'10^15',
        'checks_passed':len(checks),'checks':checks,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'repository_status_promotion':False,'github_writes':False
    }
    Path(__file__).with_name('transport_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(str(len(checks))+' exact algebra checks PASS')
    print('Raw square-root intertwining fails in the model; corrected transport is isometric and obeys the cocycle.')


if __name__=='__main__':main()
