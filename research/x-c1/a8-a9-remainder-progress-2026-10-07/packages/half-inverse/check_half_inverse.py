"""Small exact audit of bindings, error sums and the partial 19I upper matrices.
Does not replace the analytic operator derivation or the Arb integrations.
"""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib, argparse

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ldl(a):
    n=len(a);L=[[F(int(i==j)) for j in range(n)] for i in range(n)];ds=[]
    for j in range(n):
        d=a[j][j]-sum((L[j][k]**2*ds[k] for k in range(j)),F(0))
        assert d>0,('LDL',j)
        ds.append(d)
        for i in range(j+1,n):
            L[i][j]=(a[i][j]-sum((L[i][k]*L[j][k]*ds[k] for k in range(j)),F(0)))/d
    return ds
def fracmat(a): return [[F(v) for v in row] for row in a]
def overlap(a,b,path=''):
    if isinstance(a,list) and len(a)==2 and all(isinstance(v,str) for v in a):
        lo,hi=map(F,a);l2,h2=map(F,b);assert max(lo,l2)<=min(hi,h2),path
        return 1
    if isinstance(a,list):
        assert len(a)==len(b)
        return sum(overlap(v,w,path+'/'+str(i)) for i,(v,w) in enumerate(zip(a,b)))
    return 0
def check(root):
    manifest=root/'SHA256SUMS'
    if manifest.exists():
        for line in manifest.read_text().splitlines():
            expected,name=line.split('  ',1)
            p=(root/name).resolve();assert p.is_relative_to(root.resolve())
            assert digest(p)==expected,name
    bindings=json.loads((root/'SOURCE_BINDINGS.json').read_text())
    for name,s in bindings['included_files'].items():assert digest(root/name)==s,name
    proto=json.loads((root/'inputs/PROTOCOL.json').read_text())
    assert digest(root/'inputs/PROTOCOL.json')=='7572ce23726101c4c82c06a5381f2544d2c84c882b564046ff20b10c4b30407a'
    assert proto['right_shell_legendre_seed_degrees']==list(range(4,12))
    records=[];runs=[]
    for bits in (1024,1536):
        data=json.loads((root/f'expected/{bits}.json').read_text());runs.append(data)
        assert data['bits']==bits and data['size']==96 and data['resolvent_panels']==1024
        assert data['program_sha256']==digest(root/'half_inverse.py')
        assert data['geometry_sha256']==digest(root/'inputs/GEOMETRY_1024.json')
        assert data['protocol_sha256']==digest(root/'inputs/PROTOCOL.json')
        assert data['full_remainder_certified'] is False and data['target_positivity_used'] is False
        for b in data['blocks']:
            assert all(b[k] is None for k in ('U00','G01','gamma01','beta_tail','eta','alpha'))
            assert b['P_R_lower_integer']==20 and F(b['P_R_lower_bound'][0])>20
            assert b['finite_A_spectrum']==[20,30]
            for key in ('lambda_on_R_norm_squared','integral_on_R_norm_squared'):
                assert 0<F(b[key][0])<=F(b[key][1])
            e=F(b['joint_half_inverse_error_upper_rational'])
            assert F(b['joint_half_inverse_error_norm_upper'][1])<=e<F(1,3000)
            terms=[v for k,v in b['error_budget'].items() if k!='regular_gamma_current_bound_floor']
            assert all(F(v[0])>=0 for v in terms)
            assert sum((F(v[1]) for v in terms),F(0))<=e
            S=fracmat(b['half_inverse_centre_rational_Q_coefficients'])
            assert len(S)==92 and all(len(row)==8 for row in S)
            gram=[[sum((row[i]*row[j] for row in S),F(0)) for j in range(8)] for i in range(8)]
            ldl(gram)
            t=F(b['shift19_young_parameter']);assert t>0
            U=[[19*((1+t)*gram[i][j]+((1+1/t)*e**2 if i==j else 0)) for j in range(8)] for i in range(8)]
            assert U==fracmat(b['shift19_B00_Loewner_upper'])
            pivots=ldl([[F(int(i==j))-U[i][j] for j in range(8)] for i in range(8)])
            norm=max(sum(map(abs,row),F(0)) for row in U)
            assert norm==F(b['shift19_B00_operator_norm_upper']) and norm<1
            # Certified image norms and a conservative uniform whole-family band.
            assert all(F(v[0])>F(1,5) and F(v[1])<F(211,1000) for v in b['column_centre_norms'])
            records.append({'bits':bits,'parity':b['parity'],'P_R_lower':20,
                'joint_half_inverse_error_upper':str(e),
                'partial_19I_upper_norm_below':'0.866',
                'partial_19I_upper_norm_exact':str(norm),
                'minimum_pivot_I_minus_partial_upper_positive':min(pivots)>0})
            assert norm<F(866,1000)
    pairs=0
    for a,b in zip(runs[0]['blocks'],runs[1]['blocks']):
        for key in ('basis_Q_local_coefficients','basis_Z_local_coefficients','WX_gram','finite_model_A',
                    'finite_model_action_coefficients','complete_log_residual_gram','P_R_lower_bound',
                    'lambda_on_R_norm_squared','integral_on_R_norm_squared'):
            pairs+=overlap(a[key],b[key],a['parity']+'/'+key)
        for key in ('half_inverse_centre_rational_Q_coefficients','shift19_B00_Loewner_upper','joint_half_inverse_error_upper_rational'):
            assert a[key]==b[key],key
    return {'status':'PASS_BOUNDED_HALF_INVERSE_AUDIT',
        'scope':'Source hashes, rational error sums and partial 19I matrices; analytic derivation and Arb kernels remain separate inputs.',
        'precision_runs':2,'interval_pairs_overlap':pairs,'half_inverse_images':16,
        'full_B00_computed':False,'full_remainder_certified':False,'external_review':'OPEN','blocks':records}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--out',type=Path);args=ap.parse_args();answer=check(args.root)
    content=json.dumps(answer,indent=2)+'\n'
    if args.out:args.out.write_text(content,encoding='utf-8')
    print(content)
