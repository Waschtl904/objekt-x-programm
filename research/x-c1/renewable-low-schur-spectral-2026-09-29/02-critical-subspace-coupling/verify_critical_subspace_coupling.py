"""Independent exact-rational checks of block identities and saved bounds.

This does not rebuild the terminal models or replace the Arb computation.
Only Python's standard library is used.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, shutil, subprocess

def mat(rows): return [[F(x) for x in row] for row in rows]
def eye(n): return mat([[int(i == j) for j in range(n)] for i in range(n)])
def tr(a): return [list(row) for row in zip(*a)]
def add(a, b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(c,a): return [[c*x for x in row] for row in a]
def sub(a,b): return add(a,scale(-1,b))
def mul(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in tr(b)] for row in a]
def trace(a): return sum(a[i][i] for i in range(len(a)))
def inv(a):
    n=len(a); aug=[row[:]+e for row,e in zip(a,eye(n))]
    for j in range(n):
        k=next(k for k in range(j,n) if aug[k][j]); aug[j],aug[k]=aug[k],aug[j]
        c=aug[j][j]; aug[j]=[v/c for v in aug[j]]
        for k in range(n):
            if k != j:
                c=aug[k][j]; aug[k]=[v-c*w for v,w in zip(aug[k],aug[j])]
    return [row[n:] for row in aug]
def null(a):
    a=[row[:] for row in a]; n=len(a[0]); piv=[]; i=0
    for j in range(n):
        ks=[k for k in range(i,len(a)) if a[k][j]]
        if not ks: continue
        k=ks[0]; a[i],a[k]=a[k],a[i]; c=a[i][j]; a[i]=[v/c for v in a[i]]
        for k in range(len(a)):
            if k != i:
                c=a[k][j]; a[k]=[v-c*w for v,w in zip(a[k],a[i])]
        piv.append(j); i+=1
        if i == len(a): break
    cols=[]
    for j in range(n):
        if j not in piv:
            v=[F(0)]*n; v[j]=F(1)
            for i,k in enumerate(piv): v[k]=-a[i][j]
            cols.append(v)
    return tr(cols)
def positive(a):
    assert a == tr(a)
    a=[row[:] for row in a]; piv=[]
    for k in range(len(a)):
        p=a[k][k]; assert p>0; piv.append(str(p))
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)): a[i][j]-=a[i][k]*a[k][j]/p
    return piv

def exact_tests():
    tests=[]
    q=mat([[6,1,1,0],[1,5,0,1],[1,0,4,1],[0,1,1,3]])
    positive(q); qi=inv(q)
    for rho in [F(0),F(1,2),F(17)]:
        b=add(q,scale(rho,eye(4)))
        for rank in (1,2):
            w=[row[:rank] for row in mat([[1,1],[2,0],[0,1],[1,-1]])]
            wt=tr(w); bg=mul(mul(wt,b),w); s=mul(mul(wt,q),w)
            g=mul(wt,w); t=mul(mul(wt,qi),w)
            n=null(mul(wt,b)); nt=tr(n)
            assert mul(mul(wt,b),n)==scale(0,mul(wt,n))
            c=mul(mul(wt,q),n); d=mul(mul(nt,q),n)
            assert c==scale(-rho,mul(wt,n))
            z=sub(s,mul(mul(c,inv(d)),tr(c))); positive(z)
            rr=add(add(s,scale(2*rho,g)),scale(rho*rho,t))
            assert rr==mul(mul(mul(mul(wt,b),qi),b),w)
            assert z==mul(mul(bg,inv(rr)),bg)
            direct_graph=sub(w,mul(mul(n,inv(d)),tr(c)))
            resolvent_graph=mul(mul(mul(add(eye(4),scale(rho,qi)),w),inv(rr)),bg)
            assert direct_graph==resolvent_graph
            assert mul(mul(nt,q),direct_graph)==scale(0,mul(nt,w))
            assert mul(mul(wt,b),direct_graph)==bg
            # Exact inverse identity underlying the reciprocal eigenvalue formula.
            assert inv(z)==mul(mul(inv(bg),rr),inv(bg))
            tests.append({'test':'nonorthogonal_source_schur_and_graph','rho':str(rho),'rank':rank})

    # Mellin-null finite model: the same complete dual Gram identity as in L2.
    m=mat([[1],[2],[3],[4]]); e=mat([[1],[0],[0],[0]])
    w=mat([[-2,-3],[1,0],[0,1],[0,0]])
    assert mul(tr(m),w)==mat([[0,0]])
    embedding=mat([[0,0,0],[1,0,0],[0,1,0],[0,0,1]])
    mellin=mul(sub(eye(4),mul(e,tr(m))),embedding)
    dual=mul(tr(mellin),w); beta=mul(tr(e),w); g=mul(tr(w),w)
    rhs=add(g,scale(mul(tr(m),m)[0][0],mul(tr(beta),beta)))
    assert mul(tr(dual),dual)==rhs
    low=[dual[0]]; high=dual[1:]
    assert mul(tr(high),high)==sub(rhs,mul(tr(low),low))
    tests.append({'test':'complete_mellin_dual_gram_with_high_tail'})

    # Exact model with a genuinely coupled three-dimensional high block.
    coupling=mat([[F(1,3),F(1,4),0],[0,F(1,5),F(1,6)]])
    low=mat([[3,F(1,7)],[F(1,7),4]])
    delta=F(2,3); high=add(scale(delta,eye(3)),mat([[1,0,0],[0,2,1],[0,1,2]]))
    qq=[low[i]+coupling[i] for i in range(2)]+[tr(coupling)[i]+high[i] for i in range(3)]
    positive(qq)
    gram=mul(coupling,tr(coupling)); ff=sub(low,scale(1/delta,gram)); positive(ff)
    rhs=mat([[1,2],[3,1],[F(1,2),1],[1,F(1,3)],[2,-1]])
    aa=rhs[:2]; hh=rhs[2:]; exact=mul(mul(tr(rhs),inv(qq)),rhs)
    lower=mul(mul(tr(aa),inv(low)),aa)
    chi=2*trace(mul(inv(ff),gram))/(delta*delta)+1/delta
    upper=add(scale(2,mul(mul(tr(aa),inv(ff)),aa)),scale(chi,mul(tr(hh),hh)))
    positive(sub(exact,lower)); positive(sub(upper,exact))
    tests.append({'test':'full_resolvent_lower_and_upper_bounds'})
    return tests

def main():
    p=argparse.ArgumentParser()
    for name in ('primary','crosscheck','vectors','out'): p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--repo',type=Path); args=p.parse_args()
    first=json.loads(args.primary.read_bytes()); second=json.loads(args.crosscheck.read_bytes())
    vector_hash=hashlib.sha256(args.vectors.read_bytes()).hexdigest()
    assert first['source_commit']==second['source_commit']
    assert first['source_sha256']==second['source_sha256']
    assert len(first['source_sha256'])==11
    assert first['old_vector_file_sha256']==second['old_vector_file_sha256']==vector_hash
    assert first['precision_bits']==1024 and second['precision_bits']==1280
    assert set(first['results'])==set(second['results'])=={
        'A8->A9-even','A8->A9-odd','A9->A11-even','A9->A11-odd'}
    comparisons=[]
    for key,left in first['results'].items():
        right=second['results'][key]
        assert right['quadrature_nodes']==left['quadrature_nodes']+8
        assert not left['old_space_uses_new_terminal_eigenvectors']
        assert left['D_floor_depends_on_existing_new_terminal_certificate']
        c=F(1,10**(35 if left['new']=='A9' else 50))
        assert F(left['new_D_b_metric_floor_exact'])==c/(c+17)
        for pivot in left['old_S_positive_interval_pivots']: assert F(pivot['lower'])>0
        assert [v['rank'] for v in left['ranks']]==[1,2,3]
        for x,y in zip(left['ranks'],right['ranks']):
            a,b=[F(x['one_minus_kappa_'+end+'_exact']) for end in ('lower','upper')]
            c,d=[F(y['one_minus_kappa_'+end+'_exact']) for end in ('lower','upper')]
            assert 0<a<=b<1 and 0<c<=d<1 and max(a,c)<=min(b,d)
            relative=max(abs(a-c)/a,abs(b-d)/b)
            assert relative<F(1,10**12)
            comparisons.append({'case':key,'rank':x['rank'],'intervals_overlap':True,
                                'relative_endpoint_change':float(relative)})
    sources=[]
    if args.repo:
        git=shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe'
        pin=first['source_commit']
        assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=args.repo).decode().strip()==pin
        for path,digest in first['source_sha256'].items():
            raw=(args.repo/path).read_bytes()
            assert hashlib.sha256(raw).hexdigest()==digest
            assert raw==subprocess.check_output([git,'show',pin+':'+path],cwd=args.repo)
            sources.append(path)
    result={'status':'PASS','scope':'Exact finite rational identities, recorded bound consistency, optional input bindings; not terminal-model rebuild',
            'exact_rational_tests':exact_tests(),'comparison_cases':comparisons,
            'repository_sources_rechecked':sources,'source_commit':first['source_commit'],
            'old_vectors_sha256':vector_hash}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS:',len(result['exact_rational_tests']),'exact identities;',len(comparisons),
          'interval comparisons;',len(sources),'pinned source bindings.')

if __name__=='__main__': main()
