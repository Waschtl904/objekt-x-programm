"""Independent integer/Fraction proof of the old inverse majorant.

No flint dependency. Integer congruences prove both large positivity claims;
rational residuals then certify a usable six-force upper factorization.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,isqrt
import argparse,json,gzip,hashlib,sys,time
sys.set_int_max_str_digits(0)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ceilq(q,scale=10**40):
    q*=scale;return F(-((-q.numerator)//q.denominator),scale)
def sqrtlo(q,scale=10**40):return F(isqrt((q.numerator*scale*scale)//q.denominator),scale)
def sqrtup(q,scale=10**40):
    l=sqrtlo(q,scale);return l if l*l==q else l+F(1,scale)
def ldl(a):
    n=len(a);ls=[[F(int(i==j)) for j in range(n)] for i in range(n)];ds=[]
    for j in range(n):
        d=a[j][j]-sum((ls[j][k]**2*ds[k] for k in range(j)),F(0));assert d>0
        ds.append(d)
        for i in range(j+1,n):ls[i][j]=(a[i][j]-sum((ls[i][k]*ls[j][k]*ds[k] for k in range(j)),F(0)))/d
    return ds
def inverse(a):
    n=len(a);x=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        pivot=x[k][k];assert pivot
        x[k]=[v/pivot for v in x[k]]
        for i in range(n):
            if i!=k:
                t=x[i][k];x[i]=[v-t*w for v,w in zip(x[i],x[k])]
    return [row[n:] for row in x]
def prove_positive(a,den,cert):
    n=len(a);assert n==cert['dimension'] and str(den)==cert['matrix_denominator']
    scale=10**cert['preconditioner_scale_digits']
    x=[[int(v) for v in row] for row in cert['lower_triangular_preconditioner_integers']]
    assert len(x)==n and all(len(row)==n for row in x)
    assert all(x[i][j]==0 for i in range(n) for j in range(i+1,n))
    cols=list(zip(*a))
    xa=[[sum(u*v for u,v in zip(x[i][:i+1],col[:i+1])) for col in cols] for i in range(n)]
    off=[0]*n;diag=[0]*n
    for i in range(n):
        for j in range(i+1):
            g=sum(u*v for u,v in zip(xa[i][:j+1],x[j][:j+1]))
            if i==j:diag[i]=g
            else:off[i]+=abs(g);off[j]+=abs(g)
    margin=min(v-w for v,w in zip(diag,off))
    assert margin*1000>999*den*scale*scale
    # X A X* > 0 itself proves rank(X)=n and hence A > 0.
    print(time.strftime('%H:%M:%S'),cert['parity'],cert['matrix'],'exact integer positivity passed',flush=True)
    return {'dimension':n,'congruence_gershgorin_lower':'999/1000','positive':True}
def compare_intervals(a,b):
    if isinstance(a,list) and len(a)==2 and all(isinstance(v,str) for v in a):
        assert max(F(a[0]),F(b[0]))<=min(F(a[1]),F(b[1]));return 1
    if isinstance(a,list):return sum(compare_intervals(v,w) for v,w in zip(a,b))
    return 0
def check(root):
    root=root.resolve();manifest=root/'SHA256SUMS'
    if manifest.exists():
        for line in manifest.read_text().splitlines():
            h,name=line.split('  ',1);p=(root/name).resolve()
            assert p.is_relative_to(root) and sha(p)==h,name
    modelpath=root/'inputs/a8_model.json.gz';halfpath=root/'inputs/HALF_1536.json'
    assert sha(modelpath)=='5f8935d53f8518540ef25e6f2d511955bad688cf5905cb63e8d89f03aae2474b'
    source=json.loads(gzip.decompress(modelpath.read_bytes()));half=json.loads(halfpath.read_bytes())
    runs=[json.loads((root/f'expected/FACTOR_{bits}.json').read_bytes()) for bits in (1024,1536)]
    for data in runs:
        assert data['source_a8_sha256']==sha(modelpath) and data['source_half_inverse_sha256']==sha(halfpath)
        assert data['program_sha256']==sha(root/'factor_old_response.py')
        assert data['full_remainder_certified'] is False
    certs=json.loads((root/'POSITIVE_CERTIFICATES.json').read_bytes())['certificates']
    certmap={(c['parity'],c['matrix']):c for c in certs}
    records=[];majorants=[];paircount=0;fd=10**90;den=2*10**110
    gamma=F(21,10)*F(source['Gamma_kernel_error_exact'])
    for p,(b,b2) in enumerate(zip(runs[0]['blocks'],runs[1]['blocks'])):
        label=b['parity'];assert b['retained_rank']==b2['retained_rank']==6;r=6;n=191;tail=n-r
        assert b['rational_Fbar_integer_matrix']==b2['rational_Fbar_integer_matrix']
        assert b['tail_energy_kappa']==b2['tail_energy_kappa']
        for key in ('corrected_force_transform_T','small_schur_matrix','small_schur_inverse','tail_inverse_trace',
                    'joint_high_weighted_error_gram_scalar_upper','joint_complement_weighted_error_gram_scalar_upper'):
            paircount+=compare_intervals(b[key],b2[key])
        ints=[[int(v) for v in row] for row in b['rational_Fbar_integer_matrix']]
        assert all(ints[i][j]==ints[j][i] for i in range(n) for j in range(n))
        old=source['parities'][label]
        em=F(21,40)**(384+p)/factorial(384+p)/(1-F(21,40)**2/((385+p)*(386+p)))*(4 if p else 1)
        eb=2*gamma+24*em;shift=4*gamma+F(3,2)*1001*eb**2
        z=shift*den;down=z.numerator//z.denominator;up=-((-z.numerator)//z.denominator)
        gaps=[]
        for i in range(n):
            off=0;diagonal=None
            for j in range(n):
                al,au=map(int,old['A'][i][j]);gl,gu=map(int,old['complete_model_raw_high_Gram'][i][j])
                lo=al*(2*10**10)-gu*(3003*10**7)-ints[i][j]*(2*10**20)
                hi=au*(2*10**10)-gl*(3003*10**7)-ints[i][j]*(2*10**20)
                if i==j:diagonal=lo-up
                else:off+=max(abs(lo),abs(hi))
            gaps.append(diagonal-off)
        assert min(gaps)>=0
        fullcert=prove_positive(ints,fd,certmap[label,'Fbar'])
        kappa=F(b['tail_energy_kappa'])
        shifted=[[ints[i][j]*kappa.numerator-(fd*kappa.denominator if i==j else 0) for j in range(r,n)] for i in range(r,n)]
        gapcert=prove_positive(shifted,fd*kappa.numerator,certmap[label,'tail_gap'])
        # Exact rational transform centre, certified via its solve residual.
        td=2*10**70
        tm=[]
        for i in range(r):
            row=[]
            for j in range(n):
                v=(F(b['corrected_force_transform_T'][i][j][0])+F(b['corrected_force_transform_T'][i][j][1]))*10**70
                assert v.denominator==1
                row.append(v.numerator)
            assert row[:r]==[td*int(i==j) for j in range(r)]
            tm.append(row)
        tails=[row[r:] for row in tm]
        D=[[ints[i][j] for j in range(r,n)] for i in range(r,n)];dc=list(zip(*D))
        residual=[[sum(u*v for u,v in zip(tails[i],col))+td*ints[i][r+j] for j,col in enumerate(dc)] for i in range(r)]
        solve_l1=F(sum(abs(v) for row in residual for v in row),fd*td)
        transform_error=kappa*solve_l1
        knorm=F(sum(abs(ints[i][j]) for i in range(r) for j in range(r,n)),fd)
        s_error=transform_error*knorm
        sraw=[[F(ints[i][j],fd)+F(sum(tails[i][k]*ints[j][r+k] for k in range(tail)),fd*td) for j in range(r)] for i in range(r)]
        slo=[[(sraw[i][j]+sraw[j][i])/2-(s_error if i==j else 0) for j in range(r)] for i in range(r)]
        spiv=ldl(slo);hinv=inverse(slo);theta=F(1,10**20)
        hupper=[[(1+theta)*v for v in row] for row in hinv]
        trh=sum(hinv[i][i] for i in range(r))
        tail_charge=(1+1/theta)*transform_error**2*trh
        final_kappa=ceilq(kappa+tail_charge,10**6)
        # Rebuild the harmless weighted Delta bounds from the source data.
        hh=half['blocks'][p];eps=F(hh['joint_half_inverse_error_upper_rational'])
        mu=F(hh['mu'][0]);lr=sqrtup(F(hh['lambda_on_R_norm_squared'][1]))
        qnorm=F(hh['core_form_absolute_bound'][1])/sqrtlo(2*mu)
        gnorm=ceilq(F(16,5)+lr*qnorm/mu)
        hnorm=ceilq(gnorm*sqrtup(1+em*em))
        mo=source['raw_low_moments'];mp=min(map(F,mo[p]));assert mp>0
        gold=F(1)
        for degree in range(p+2+2*r,p+384,2):
            mn=max(abs(F(v)) for v in mo[degree])
            gold+=F(2*degree+1,2*p+1)*(mn/mp)**2
        gold=ceilq(gold)
        hdiag=1001*eb*eb
        htrace=sum(F(int(old['complete_model_raw_high_Gram'][i][i][1]),10**100)*F(1001,1000) for i in range(r,n))+tail*hdiag
        hrows=[]
        for i in range(r,n):
            hrows.append(sum(max(abs(F(v)) for v in old['complete_model_raw_high_Gram'][i][j])*F(1001,1000*10**100) for j in range(r,n))+hdiag)
        bnorm2=ceilq(min(htrace,max(hrows)))
        vnorm=ceilq(sqrtup(gold)*gnorm+F(3,2)*sqrtup(bnorm2)*hnorm)
        ehigh=ceilq(F(3,2)*hnorm**2*eps**2,10**12)
        etail=ceilq(final_kappa*vnorm**2*eps**2,10**12)
        total=ehigh+etail
        assert total<(F(1039,10**6) if p==0 else F(266,10**6))
        majorants.append({'parity':label,'retained_rank':r,
            'formula':'F_inherited^(-1) <= T0* H T0 + kappa_final P_J',
            'T0_rational':[[str(F(v,td)) for v in row] for row in tm],
            'H_rational':[[str(v) for v in row] for row in hupper],
            'kappa_final':str(final_kappa),'transform_operator_error_upper':str(transform_error),
            'schur_matrix_error_upper':str(s_error),'young_parameter':str(theta),
            'transform_rounding_tail_charge_upper':str(tail_charge),
            'joint_high_weighted_error_gram_scalar':str(ehigh),
            'joint_complement_weighted_error_gram_scalar':str(etail),
            'joint_high_plus_complement_error_gram_scalar':str(total),
            'six_sensitive_force_error_gram':None,'four_C_coupling_error_gram':None})
        records.append({'parity':label,'source_Loewner_lower_verified':True,
            'full_positive_certificate':fullcert,'tail_gap_certificate':gapcert,
            'retained_rank':r,'complement_dimension':tail,'kappa_final':str(final_kappa),
            'small_schur_exact_positive_pivots':len(spiv),
            'joint_high_error_gram_scalar':str(ehigh),'joint_complement_error_gram_scalar':str(etail),
            'joint_high_plus_complement_error_gram_scalar':str(total)})
    answer={'status':'PASS_EXACT_OLD_METRIC_REDUCTION_AND_PARTIAL_WEIGHTED_ERROR_GRAMS',
        'arithmetic':'Python integer and Fraction; no numerical library used by this checker',
        'scope':'Inherited finite Schur metric and two harmless error contributions. No new sensitive force values, no full B00.',
        'precision_interval_pairs_overlap':paircount,'blocks':records,'full_remainder_certified':False,
        'U00':None,'G01':None,'gamma01':None,'beta_tail':None,'external_review':'OPEN','github_changed':False}
    return answer,{'status':answer['status'],'blocks':majorants,'full_remainder_certified':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--out',type=Path);ap.add_argument('--majorant-out',type=Path);args=ap.parse_args()
    answer,majorants=check(args.root)
    if args.out:args.out.write_text(json.dumps(answer,indent=2)+'\n',encoding='utf-8')
    if args.majorant_out:args.majorant_out.write_text(json.dumps(majorants,indent=2)+'\n',encoding='utf-8')
    if (args.root/'EXACT_CHECK.json').exists():assert answer==json.loads((args.root/'EXACT_CHECK.json').read_bytes())
    if (args.root/'RATIONAL_MAJORANT.json').exists():assert majorants==json.loads((args.root/'RATIONAL_MAJORANT.json').read_bytes())
    print(json.dumps(answer,indent=2))
