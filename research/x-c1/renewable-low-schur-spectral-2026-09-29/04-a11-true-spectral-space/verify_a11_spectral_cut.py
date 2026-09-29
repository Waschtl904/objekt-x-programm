"""Integer rank certificate and exact rational physical spectral implications.

The rank proof reconstructs F-sI+VV* and -V*(F-sI)V from pinned original F
intervals and fixed rational vectors. It does not use computed F eigenvalues.
The complete-high gamma and mass bounds are separately supplied Arb results.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,gzip,hashlib,json,subprocess,time

SCALE=10**200;ZERO=(0,0);ONE=(SCALE,SCALE)
def ceildiv(a,b):return -((-a)//b)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    values=[x*y for x in a for y in b]
    return (min(values)//SCALE,ceildiv(max(values),SCALE))
def div(a,b):
    assert b[0]*b[1]>0
    return (min(x*SCALE//y for x in a for y in b),max(ceildiv(x*SCALE,y) for x in a for y in b))
def isum(values):
    out=ZERO
    for v in values:out=add(out,v)
    return out
def interval_rational(value):
    x=Q(value)*SCALE
    return (x.numerator//x.denominator,ceildiv(x.numerator,x.denominator))
def positive_pivots(a):
    n=len(a);L=[[ZERO]*n for _ in range(n)];d=[]
    for i in range(n):
        pivot=sub(a[i][i],isum(mul(mul(L[i][k],L[i][k]),d[k]) for k in range(i)))
        assert pivot[0]>0,(i,'uncertified pivot');d.append(pivot);L[i][i]=ONE
        for j in range(i+1,n):
            L[j][i]=div(sub(a[j][i],isum(mul(mul(L[j][k],L[i][k]),d[k]) for k in range(i))),pivot)
    return [str(Q(x[0],SCALE)) for x in d]
def gram_bounds(case,rank):
    den=int(case['projected_gram_denominator']);s=case['projected_form_gram'];g=case['projected_L2_gram']
    su=max(Q(int(s[i][i][1])+sum(max(abs(int(s[i][j][0])),abs(int(s[i][j][1]))) for j in range(rank) if j!=i),den) for i in range(rank))
    gl=min(Q(int(g[i][i][0])-sum(max(abs(int(g[i][j][0])),abs(int(g[i][j][1]))) for j in range(rank) if j!=i),den) for i in range(rank))
    assert gl>0 and su>0;return su/gl

def exact_pencil_test():
    ll,bb,hh=Q(3),Q(1,4),Q(2)
    gll,glh,ghh=Q(5,4),Q(1,10),Q(6,5);mu=Q(1,3)
    bmu=bb-mu*glh;hmu=hh-mu*ghh
    schur=ll-mu*gll-bmu*bmu/hmu
    determinant=(ll-mu*gll)*hmu-bmu*bmu
    assert determinant==hmu*schur
    derivative=-gll+2*glh*bmu/hmu-ghh*bmu*bmu/(hmu*hmu)
    y=-bmu/hmu
    assert derivative==-(gll+2*glh*y+ghh*y*y)<0
    assert schur!=ll-mu-bb*bb/(hh-mu)
    return {'generalized_determinant_identity':'PASS','mass_pencil_derivative':'PASS',
            'nonorthogonal_mass_changes_schur':'PASS'}

def main():
    p=argparse.ArgumentParser()
    for k in ('repo','vectors','proposal','primary','crosscheck','projection','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();pin='d16ba43ebb20f2c61f43379fc65d7a9b9dba76de'
    git=r'C:\Program Files\Git\cmd\git.exe'
    assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==pin
    rel='research/x-c1/chambers-through-a11-2026-09-28/a11/reserve_results_lower_matrices.json.gz'
    raw=(a.repo/rel).read_bytes();assert raw==subprocess.check_output([git,'show',pin+':'+rel],cwd=a.repo)
    fdata=json.loads(gzip.decompress(raw));proposal=json.loads(gzip.decompress(a.proposal.read_bytes()))
    assert hashlib.sha256(raw).hexdigest()==proposal['source_F_sha256']
    assert hashlib.sha256(a.vectors.read_bytes()).hexdigest()==proposal['source_vectors_sha256']
    vectors=json.loads(a.vectors.read_bytes());primary=json.loads(a.primary.read_bytes());cross=json.loads(a.crosscheck.read_bytes())
    projection=json.loads(a.projection.read_bytes());assert projection['source_commit']==pin
    ph=hashlib.sha256(a.projection.read_bytes()).hexdigest()
    assert primary['old_projection_sha256']==cross['old_projection_sha256']==ph
    assert primary['source_sha256']==cross['source_sha256']
    bindings={}
    for name,digest in primary['source_sha256'].items():
        blob=(a.repo/name).read_bytes();assert hashlib.sha256(blob).hexdigest()==digest
        assert blob==subprocess.check_output([git,'show',pin+':'+name],cwd=a.repo);bindings[name]=digest
    for name in ['PROOF.md','GENERAL_TAIL_PRINCIPLE.md']:
        path='research/x-c1/chambers-through-a11-2026-09-28/a11/'+name
        blob=(a.repo/path).read_bytes();assert blob==subprocess.check_output([git,'show',pin+':'+path],cwd=a.repo)
        bindings[path]=hashlib.sha256(blob).hexdigest()
    results={};s=Q(proposal['cut_exact']);assert s==Q(1,500) and proposal['rank']==8
    for parity in ('even','odd'):
        start=time.time();rows=fdata['parities'][parity]['lower_matrix'];n=len(rows)
        assert n==285
        fi=[[(int(x[0])*10**100,int(x[1])*10**100) for x in row] for row in rows]
        v=[[interval_rational(vectors['A11-'+parity+'-'+str(j+1)]['coefficients'][i]) for j in range(8)] for i in range(n)]
        shifted=[[sub(fi[i][j],interval_rational(s)) if i==j else fi[i][j] for j in range(n)] for i in range(n)]
        r=[[int(x) for x in row] for row in proposal['parities'][parity]['R_upper_grid']]
        t=[[int(x) for x in row] for row in proposal['parities'][parity]['T_upper_grid']]
        grid=int(proposal['factor_scale']);grid2=grid*grid;assert SCALE%grid2==0
        assert all(r[i][i]>0 and t[i][i]>0 and all(r[i][j]==t[i][j]==0 for j in range(i)) for i in range(n))
        print(parity,'integer reconstruction of repaired matrix',flush=True)
        error_rows=[]
        for i in range(n):
            row_error=0
            for j in range(n):
                repaired=add(shifted[i][j],isum(mul(v[i][k],v[j][k]) for k in range(8)))
                rr=sum(r[k][i]*r[k][j] for k in range(min(i,j)+1))*(SCALE//grid2)
                row_error+=max(abs(repaired[0]-rr),abs(repaired[1]-rr))
            error_rows.append(row_error)
        epsilon=Q(max(error_rows),SCALE)
        rt_rows=[0]*n;rt_cols=[0]*n
        for i in range(n):
            for j in range(i,n):
                error=abs((grid2 if i==j else 0)-sum(r[i][k]*t[k][j] for k in range(i,j+1)))
                rt_rows[i]+=error;rt_cols[j]+=error
        eta=Q(max(rt_rows+rt_cols),grid2);tnorm=Q(sum(x*x for row in t for x in row),grid2)
        assert eta<1
        repaired_floor=(1-eta)**2/tnorm-epsilon;assert repaired_floor>0
        print(parity,'positive repair certified; negative compression',flush=True)
        fv=[[isum(mul(shifted[i][k],v[k][j]) for k in range(n)) for j in range(8)] for i in range(n)]
        compression=[[neg(isum(mul(v[k][i],fv[k][j]) for k in range(n))) for j in range(8)] for i in range(8)]
        pivots=positive_pivots(compression)
        # Independent F inertia count: exactly eight negative, zero null pivots.
        pr=primary['results'][parity];cr=cross['results'][parity]
        assert Q(pr['gamma_upper']['upper_exact'])<60 and Q(cr['gamma_upper']['upper_exact'])<60
        assert Q(pr['mass_norm_squared_upper']['upper_exact'])<Q(1003,1000)
        assert Q(cr['mass_norm_squared_upper']['upper_exact'])<Q(1003,1000)
        physical_cut=Q(17,9999);tt=Q(1003,1000)*physical_cut;aa=1-60*tt/(1-tt)
        assert 0<tt<1 and aa*s-tt>0
        u8=gram_bounds(projection['results']['A11-'+parity],8);assert u8<physical_cut
        eigen=[]
        for j,(pbound,cbound) in enumerate(zip(pr['physical_bounds'],cr['physical_bounds'])):
            lower=min(Q(pbound['physical_mu_lower_exact']),Q(cbound['physical_mu_lower_exact']))*Q(999999999999,1000000000000)
            f=min(Q(pbound['comparison_F_eigenvalue']['lower_exact']),Q(cbound['comparison_F_eigenvalue']['lower_exact']))
            gamma=max(Q(pr['gamma_upper']['upper_exact']),Q(cr['gamma_upper']['upper_exact']))
            rho=max(Q(pr['mass_norm_squared_upper']['upper_exact']),Q(cr['mass_norm_squared_upper']['upper_exact']))
            tlo=rho*lower;alo=1-gamma*tlo/(1-tlo)
            assert 0<tlo<1 and alo>0 and alo*f>=tlo
            upper=max(Q(pbound['physical_mu_upper_exact']),Q(cbound['physical_mu_upper_exact']),gram_bounds(projection['results']['A11-'+parity],j+1))
            assert 0<lower<=upper
            eigen.append({'index':j+1,'physical_mu_lower_exact':str(lower),'physical_mu_upper_exact':str(upper),
                          'optimal_tau_lower_exact':str(lower/(lower+17)),
                          'optimal_tau_upper_exact':str(upper/(upper+17))})
        assert all(Q(eigen[j]['physical_mu_upper_exact'])<Q(eigen[j+1]['physical_mu_lower_exact']) for j in range(8))
        mu9=Q(eigen[8]['physical_mu_lower_exact']);leakage=u8/mu9;assert leakage<1
        results[parity]={'comparison_cut_exact':str(s),'negative_count':8,'zero_count':0,
                         'repair_floor_exact':str(repaired_floor),'repair_residual_norm_upper_exact':str(epsilon),
                         'approximate_inverse_residual_upper_exact':str(eta),'inverse_factor_frobenius_squared_exact':str(tnorm),
                         'negative_compression_positive_pivots':pivots,'physical_cut_exact':str(physical_cut),
                         'b_spectral_cut_exact':'1/10000','true_spectral_projector_rank':8,
                         'minimal_rank_for_b_gap_at_least_cut':8,
                         'trial8_energy_upper_exact':str(u8),'trial_to_true_projector_leakage_squared_upper_exact':str(leakage),
                         'physical_eigenvalue_bounds':eigen,'seconds':time.time()-start}
        print(parity,'PASS: true spectral rank 8 below b-gap 1e-4',flush=True)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    out={'status':'CERTIFIED_TRUE_A11_LOW_SPECTRAL_PROJECTOR_RANK_AND_GAP','source_commit':pin,
         'scope':'Rank certified independently of computed F eigenvalues; high trace/mass bounds remain Arb input. Exact spectral projection defined; no numerical true eigenvectors or transported kappa computed.',
         'integer_decimal_places':200,'bound_source_sha256':bindings,'results':results,
         'full_two_parity_projector_rank':16,
         'exact_rational_pencil_tests':exact_pencil_test(),
         'proposal_sha256':hashlib.sha256(a.proposal.read_bytes()).hexdigest(),
         'projection_sha256':ph,'vectors_sha256':hashlib.sha256(a.vectors.read_bytes()).hexdigest()}
    a.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('ALL SPECTRAL CUT CHECKS PASS',flush=True)

if __name__=='__main__':main()
