"""Certify improved whole-space gaps and spectral transport bounds.

Analytical input: positive terminal forms, exact q/L2 naturality, spectral ranks.
New calculation: full-high Schur comparison at a positive parameter, certified
using integer intervals. No computed eigenvectors or truncated high response.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import argparse,gzip,hashlib,io,json,shutil,subprocess,time,zipfile
from transport_integer_arithmetic import SCALE,ZERO,add,sub,neg,mul,isum,irat,decode,positive_pivots

PIN='d16ba43ebb20f2c61f43379fc65d7a9b9dba76de'
REFERENCE_SHA='02dd77fef1df201918d5effdd9cd08500a1c319ce6c2b82661e93332804ec792'

def digest(raw):return hashlib.sha256(raw).hexdigest()
def archive_files(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        assert z.testzip() is None
        files={Path(n).name:z.read(n) for n in z.namelist() if not n.endswith('/')}
    for line in files['SHA256SUMS'].decode().splitlines():
        h,n=line.split('  ',1);assert digest(files[n])==h
    return files
def sqrt_bound(x,upper=True,digits=6):
    s=10**digits;assert x>=0
    k=isqrt((x.numerator*s*s)//x.denominator)
    assert Q(k*k,s*s)<=x<Q((k+1)*(k+1),s*s)
    if upper and Q(k*k,s*s)<x:k+=1
    return Q(k,s)

def main():
    p=argparse.ArgumentParser()
    for k in ('repo','reference','proposal','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();git=shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe'
    assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==PIN
    refraw=a.reference.read_bytes();assert digest(refraw)==REFERENCE_SHA
    ref=archive_files(refraw);a11=archive_files(ref['A11_reference.zip'])
    ranks=json.loads(ref['verification.json']);old=json.loads(a11['verification.json'])
    assert ranks['source_commit']==old['source_commit']==PIN
    assert ranks['two_parity_projector_ranks']=={'A8':10,'A9':12}
    assert old['full_two_parity_projector_rank']==16
    vraw=ref['fixed_vectors.json'];vectors=json.loads(vraw)
    propraw=a.proposal.read_bytes();prop=json.loads(gzip.decompress(propraw))
    assert prop['vectors_sha256']==digest(vraw)
    sources=ranks['bound_source_sha256']|old['bound_source_sha256']
    for n,h in prop['source_sha256'].items():
        if n in sources:assert sources[n]==h
        sources[n]=h
    base='research/x-c1/chambers-through-a11-2026-09-28/'
    for rel in ('wall/PROOF.md','wall/Q9.md','o10/PROOF.md'):
        path=base+rel;sources[path]=digest((a.repo/path).read_bytes())
    for rel,h in sources.items():
        raw=(a.repo/rel).read_bytes();assert digest(raw)==h
        assert raw==subprocess.check_output([git,'show',PIN+':'+rel],cwd=a.repo)
    mass={}
    for name in ('inputs512.json','inputs768.json'):
        data=json.loads(ref[name]);assert data['source_commit']==PIN
        for parity in ('even','odd'):
            key='A9-'+parity
            mass.setdefault(key,[]).append(Q(data['results'][key]['mass_norm_squared_interval'][1]))
    for name in ('spectral_bounds.json','spectral_bounds_crosscheck.json'):
        data=json.loads(a11[name]);assert data['source_commit']==PIN
        for parity in ('even','odd'):
            key='A11-'+parity
            mass.setdefault(key,[]).append(Q(data['results'][parity]['mass_norm_squared_upper']['upper_exact']))
    gaps={}
    for terminal,rank,delta in [('A9',6,Q(2,3)),('A11',8,Q(1))]:
        folder=a.repo/base/terminal.lower()
        model=json.loads(gzip.decompress((folder/(terminal.lower()+'_model.json.gz')).read_bytes()))
        fdata=json.loads(gzip.decompress((folder/'reserve_results_lower_matrices.json.gz').read_bytes()))
        receipt=json.loads((folder/'reserve_results.json').read_bytes())
        assert Q(receipt['full_high_physical_floor'])==delta
        for parity in ('even','odd'):
            start=time.time();key=terminal+'-'+parity;pr=prop['results'][key]
            assert pr['rank']==rank and Q(pr['delta_exact'])==delta
            rho=Q(pr['rho_exact']);assert rho==Q(1003,1000) and all(1<x<rho for x in mass[key])
            mu=Q(pr['physical_gap_cut_exact']);tt=rho*mu
            assert Q(17,9999)<mu and 0<tt<delta
            kappa=tt/(delta*(delta-tt))
            fi=[[decode(x) for x in row] for row in fdata['parities'][parity]['lower_matrix']]
            n=len(fi);assert n==(296 if terminal=='A9' else 285)
            gram=model['parities'][parity]['complete_model_raw_high_Gram']
            low=model['parities'][parity]['A']
            eb=irat(receipt['parities'][parity]['coupling_operator_error_exact'])
            el=irat(receipt['low_form_error_exact'])
            cm=[]
            for i in range(n):
                row=[]
                for j in range(n):
                    h=mul(irat('1001/1000'),decode(gram[i][j]))
                    if i==j:h=add(h,mul(irat(1001),mul(eb,eb)))
                    f=sub(decode(low[i][j]),mul(irat(1/delta),h))
                    if i==j:f=sub(f,el)
                    assert fi[i][j][0]<=f[0]<=f[1]<=fi[i][j][1],(key,i,j,'F enclosure')
                    c=sub(fi[i][j],mul(irat(kappa),h))
                    if i==j:c=sub(c,irat(tt))
                    row.append(c)
                cm.append(row)
            v=[[irat(vectors[key+'-'+str(j+1)]['coefficients'][i]) for j in range(rank)] for i in range(n)]
            r=[[int(x) for x in row] for row in pr['R_upper_grid']]
            t=[[int(x) for x in row] for row in pr['T_upper_grid']]
            grid=int(prop['factor_scale']);grid2=grid*grid;assert SCALE%grid2==0
            assert len(r)==len(t)==n and all(len(row)==n for row in r+t)
            assert all(r[i][i]>0 and t[i][i]>0 and all(r[i][j]==t[i][j]==0 for j in range(i)) for i in range(n))
            print(key,'integer reconstruction of full Schur comparison at mu',str(mu),flush=True)
            errs=[]
            for i in range(n):
                error=0
                for j in range(n):
                    repaired=add(cm[i][j],isum(mul(v[i][k],v[j][k]) for k in range(rank)))
                    rr=sum(r[k][i]*r[k][j] for k in range(min(i,j)+1))*(SCALE//grid2)
                    error+=max(abs(repaired[0]-rr),abs(repaired[1]-rr))
                errs.append(error)
            epsilon=Q(max(errs),SCALE)
            er,ec=[0]*n,[0]*n
            for i in range(n):
                for j in range(i,n):
                    e=abs((grid2 if i==j else 0)-sum(r[i][k]*t[k][j] for k in range(i,j+1)))
                    er[i]+=e;ec[j]+=e
            eta=Q(max(er+ec),grid2);nu=Q(sum(x*x for row in t for x in row),grid2)
            assert eta<1
            floor=(1-eta)**2/nu-epsilon;assert floor>0
            cv=[[isum(mul(cm[i][k],v[k][j]) for k in range(n)) for j in range(rank)] for i in range(n)]
            negative=[[neg(isum(mul(v[k][i],cv[k][j]) for k in range(n))) for j in range(rank)] for i in range(rank)]
            pivots=positive_pivots(negative)
            # New physical gap: <=rank nonpositive directions at mu.
            # Previous exact rank says rank actual eigenvalues are below 17/9999<mu.
            prior=ranks['results'][key] if terminal=='A9' else old['results'][parity]
            assert prior['true_spectral_projector_rank']==rank
            assert prior['b_spectral_cut_exact']=='1/10000'
            beta=mu/(mu+17)
            gaps[key]={'rank_below_fixed_cut':rank,'full_high_floor_exact':str(delta),
                'physical_complement_lower_exact':str(mu),'b_complement_lower_exact':str(beta),
                'rho_used_exact':str(rho),'reference_parameter_exact':str(tt),'coupling_coefficient_exact':str(kappa),
                'repair_floor_exact':str(floor),'repair_error_upper_exact':str(epsilon),
                'inverse_factor_residual_upper_exact':str(eta),'inverse_factor_frobenius_squared_exact':str(nu),
                'comparison_negative_pivots':pivots,'comparison_nonpositive_count':rank,
                'gap_endpoint_is_not_eigenvalue':True,'seconds':time.time()-start}
            print(key,'PASS: full physical complement above',float(mu),'b gap above',float(beta),flush=True)
    transports={}
    for first,last in [('A8','A9'),('A9','A11')]:
        for parity in ('even','odd'):
            key=first+'->'+last+'-'+parity
            src=ranks['results'][first+'-'+parity];dst=gaps[last+'-'+parity]
            alpha=Q(src['physical_trial_b_quotient_upper_exact']);beta=Q(dst['b_complement_lower_exact'])
            assert 0<alpha<Q(1,10000)<beta
            ratio=alpha/beta;eps=sqrt_bound(ratio);lower=sqrt_bound(1-ratio,False)
            coarse=sqrt_bound(alpha/Q(1,10000))
            assert eps*eps>=ratio and lower*lower<=1-ratio and 0<lower<1 and eps<coarse<1
            ra=src['true_spectral_projector_rank'];rb=dst['rank_below_fixed_cut'];assert rb>ra
            transports[key]={'norm':'b_A to b_B','old_critical_rank':ra,'new_critical_rank':rb,
                'canonical_extension_rank':rb-ra,'old_alpha_upper_exact':str(alpha),
                'new_beta_lower_exact':str(beta),'leakage_squared_upper_exact':str(ratio),
                'leakage_norm_upper_exact':str(eps),'projected_transport_min_singular_lower_exact':str(lower),
                'coarse_fixed_cut_leakage_norm_upper_exact':str(coarse),
                'projection_is_injective':True,
                'extension_has_no_nonzero_vector_supported_in_old_interval':True}
            print(key,'leakage <=',float(eps),'projected norm >=',float(lower),'new dimensions',rb-ra,flush=True)
    out={'status':'CERTIFIED_CRITICAL_SPECTRAL_TRANSPORT_BOUNDS','source_commit':PIN,
        'analytical_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN','integer_decimal_places':200,
        'fixed_b_cut_exact':'1/10000','fixed_physical_cut_exact':'17/9999',
        'scope':'Positive already-certified terminals and exact q/L2 naturality; improved complete-high comparison. Not a forward proof of new terminal positivity.',
        'reference_archive_sha256':digest(refraw),'proposal_sha256':digest(propraw),'vectors_sha256':digest(vraw),
        'bound_source_sha256':sources,'gaps':gaps,'transports':transports,
        'new_eigenvectors_computed':False,'high_response_truncated':False,
        'spatial_mass_distribution_computed':False,'new_kappa_test_computed':False}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('ALL TRANSPORT AND GAP CHECKS PASS',flush=True)

if __name__=='__main__':main()
