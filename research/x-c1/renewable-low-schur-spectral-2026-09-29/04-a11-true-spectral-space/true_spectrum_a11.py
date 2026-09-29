"""Certified physical spectral bounds using complete old-terminal inequalities.

F eigenvalues remain comparison data; they are not called eigenvalues of Q.
Physical lower bounds use a whole-space Schur comparison, upper bounds use
physical Rayleigh-Ritz with the full Mellin mass Gram. No high truncation.
"""
from pathlib import Path
from fractions import Fraction
import argparse,gzip,hashlib,json,subprocess,sys,time
from flint import arb,arb_mat,fmpq,ctx
import flint

sys.set_int_max_str_digits(100000)
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
p.add_argument('--old-projection',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
p.add_argument('--bits',type=int,default=512);p.add_argument('--only',nargs='*');a=p.parse_args()
ctx.prec=a.bits;assert flint.__version__=='0.9.0';a.out.mkdir(parents=True,exist_ok=True)
PIN='d16ba43ebb20f2c61f43379fc65d7a9b9dba76de';DEN=10**100
git=r'C:\Program Files\Git\cmd\git.exe'
assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==PIN
sources={};results={};root=a.repo/'research/x-c1/chambers-through-a11-2026-09-28/a11'
def read(path,zipped=False):
    raw=path.read_bytes();rel=path.relative_to(a.repo).as_posix()
    assert raw==subprocess.check_output([git,'show',PIN+':'+rel],cwd=a.repo)
    sources[rel]=hashlib.sha256(raw).hexdigest()
    return json.loads(gzip.decompress(raw) if zipped else raw)
def rational(x):
    f=Fraction(x);return arb(fmpq(f.numerator,f.denominator))
def ball(x,den=DEN):
    lo,hi=map(int,x);assert lo<=hi
    return arb(fmpq(lo+hi,2*den))+arb(0,arb(fmpq(hi-lo,2*den)))
def matrix(rows,den=DEN):return arb_mat([[ball(x,den) for x in row] for row in rows])
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def exact(x,lower=True):
    v=x.lower() if lower else x.upper();s=10**110
    n=int(((v*s).floor() if lower else (v*s).ceil()).unique_fmpz())
    return str(Fraction(n,s))
def data(x):return {'lower_exact':exact(x),'upper_exact':exact(x,False),'display':x.str(20)}
def eig_real(x):
    values=x.eig()
    assert all(v.is_finite() and v.imag.contains(0) for v in values)
    values=sorted([v.real for v in values],key=lambda x:float(x.mid()))
    assert all(values[i].upper()<values[i+1].lower() for i in range(len(values)-1))
    return values

model=read(root/'a11_model.json.gz',True)
lower=read(root/'reserve_results_lower_matrices.json.gz',True)
receipt=read(root/'reserve_results.json')
projection=json.loads(a.old_projection.read_bytes())
assert projection['source_commit']==PIN
for parity in ('even','odd'):
    if a.only and parity not in a.only:continue
    start=time.time();n=model['parities'][parity]['dimension'];pi=int(parity=='odd')
    F=matrix(lower['parities'][parity]['lower_matrix'])
    Hup=matrix(model['parities'][parity]['complete_model_raw_high_Gram'])*rational('1001/1000')
    eB=rational(receipt['parities'][parity]['coupling_operator_error_exact'])
    Hup+=eye(n)*(1001*eB*eB)
    print(parity,'whole-high relative coupling trace',flush=True)
    gamma=(F.solve(eye(n),algorithm='precond')*Hup).trace().upper();assert gamma>0
    endpoint=ball(model['endpoint_interval'])
    mnorm=(endpoint.sinh()/endpoint+(1 if pi==0 else -1))/2
    me=arb(2*pi+1).sqrt()*ball(model['raw_low_moments'][pi])
    rho=(mnorm/(me*me)).upper();assert rho>=1
    print(parity,'full interval comparison spectrum, dimension',n,flush=True)
    fs=eig_real(F);assert fs[0]>0
    print(parity,'comparison spectrum isolated',len(fs),'elapsed',round(time.time()-start,1),flush=True)
    pg=projection['results']['A11-'+parity];scale=int(pg['projected_gram_denominator'])
    S=matrix(pg['projected_form_gram'],scale);G=matrix(pg['projected_L2_gram'],scale)
    (a.out/(parity+'_comparison_eigenvalues.json')).write_text(json.dumps(
        {'precision_bits':a.bits,'F_sha256':sources['research/x-c1/chambers-through-a11-2026-09-28/a11/reserve_results_lower_matrices.json.gz'],
         'eigenvalues':[data(v) for v in fs]},indent=2)+'\n',encoding='utf-8')
    print(parity,'physical trial-space upper bounds with mass Gram',flush=True)
    upper=[];ritz_details=[]
    for rank in range(1,S.nrows()+1):
        smax=max(S[i,i].upper()+sum((abs(S[i,j]).upper() for j in range(rank) if j!=i),arb(0)) for i in range(rank))
        gmin=min(G[i,i].lower()-sum((abs(G[i,j]).upper() for j in range(rank) if j!=i),arb(0)) for i in range(rank))
        assert gmin>0 and smax>0
        upper.append((smax/gmin).upper())
        ritz_details.append({'form_Gershgorin_upper':data(smax),'mass_Gershgorin_lower':data(gmin)})
    rows=[]
    for j in range(len(upper)):
        f=fs[j].lower()
        bb=1+(1+gamma)*f
        t=2*f/(bb+(bb*bb-4*f).sqrt())
        lo=(t/rho).lower();hi=upper[j].upper()
        assert lo>0 and hi>=lo
        rows.append({'index':j+1,'physical_mu_lower_exact':exact(lo),
                     'physical_mu_upper_exact':exact(hi,False),
                     'physical_mu_display':[float(lo),float(hi)],
                     'optimal_tau_lower_exact':exact(lo/(lo+17)),
                     'optimal_tau_upper_exact':exact(hi/(hi+17),False),
                     'comparison_F_eigenvalue':data(fs[j]),'physical_trial_space_upper':data(upper[j]),
                     'trial_space_details':ritz_details[j]})
        print(parity,'mu',j+1,'in',float(lo),float(hi),flush=True)
    results[parity]={'dimension':n,'gamma_upper':data(gamma),'mass_norm_squared_upper':data(rho),
                     'all_comparison_eigenvalues':[data(x) for x in fs],
                     'physical_bounds':rows,'seconds':time.time()-start}
    output={'status':'CERTIFIED_PHYSICAL_SPECTRAL_BOUNDS_BY_FULL_HIGH_COMPARISON',
            'source_commit':PIN,'precision_bits':a.bits,'source_sha256':sources,
            'old_projection_sha256':hashlib.sha256(a.old_projection.read_bytes()).hexdigest(),
            'method':'whole-space lower Schur comparison and physical generalized Rayleigh-Ritz upper bounds',
            'high_response_truncated':False,'results':results}
    (a.out/'spectral_bounds.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print('COMPLETE',flush=True)
