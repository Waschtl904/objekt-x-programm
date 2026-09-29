"""Old-only bounds on q-orthogonal complement gaps for fixed low sources.

Upper bounds use exact q-orthogonalized low test sources, not a truncation claim
about the full complement. Lower bounds come from the same old certificate.
The first three source vectors are preserved byte-for-byte as decimal rationals.
Additional diagnostic vectors do not purport to be spectral projectors.
"""
from pathlib import Path
from fractions import Fraction
import argparse,gzip,hashlib,json,subprocess,sys,time
import flint
from flint import arb,arb_mat,fmpq,ctx

sys.set_int_max_str_digits(100000)
p=argparse.ArgumentParser()
p.add_argument('--repo',type=Path,required=True);p.add_argument('--old-vectors',type=Path,required=True)
p.add_argument('--out',type=Path,required=True);p.add_argument('--bits',type=int,default=1024)
p.add_argument('--max-rank',type=int,default=20);p.add_argument('--iterations',type=int,default=32)
p.add_argument('--fixed-vectors',type=Path);p.add_argument('--only',nargs='*')
a=p.parse_args();ctx.prec=a.bits;assert flint.__version__=='0.9.0'
PIN='d16ba43ebb20f2c61f43379fc65d7a9b9dba76de';DEN=10**100
git=r'C:\Program Files\Git\cmd\git.exe'
assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==PIN
a.out.mkdir(parents=True,exist_ok=True)
old=json.loads(a.old_vectors.read_bytes());fixed=json.loads(a.fixed_vectors.read_bytes()) if a.fixed_vectors else None
sources={};results={};outvec={}

def read(path,zipped=False):
    raw=path.read_bytes();rel=path.relative_to(a.repo).as_posix()
    assert raw==subprocess.check_output([git,'show',PIN+':'+rel],cwd=a.repo)
    sources[rel]=hashlib.sha256(raw).hexdigest()
    return json.loads(gzip.decompress(raw) if zipped else raw)
def rational(value):
    v=Fraction(value);return arb(fmpq(v.numerator,v.denominator))
def ball(x):
    lo,hi=map(int,x);assert lo<=hi
    return arb(fmpq(lo+hi,2*DEN))+arb(0,arb(fmpq(hi-lo,2*DEN)))
def matrix(rows):return arb_mat([[ball(v) for v in row] for row in rows])
def dot(x,y):return (x.transpose()*y)[0,0]
def norm(x):return dot(x,x).sqrt()
def col(x,j):return arb_mat([[x[i,j]] for i in range(x.nrows())])
def columns(cols):return arb_mat([[v[i,0] for v in cols] for i in range(cols[0].nrows())])
def cut(x,n):return arb_mat([[x[i,j] for j in range(n)] for i in range(n)])
def exact(x,lower=True):
    v=x.lower() if lower else x.upper();s=10**140
    n=int(((v*s).floor() if lower else (v*s).ceil()).unique_fmpz())
    return str(Fraction(n,s))
def desc(x):return {'display':x.str(18),'lower_exact':exact(x),'upper_exact':exact(x,False)}
def integer_pair(x):
    s=10**140
    return [str(int((x.lower()*s).floor().unique_fmpz())),
            str(int((x.upper()*s).ceil().unique_fmpz()))]
def ldl_positive(x):
    n=x.nrows();L=[[arb(0)]*n for _ in range(n)];d=[]
    for i in range(n):
        di=x[i,i]-sum((L[i][k]*L[i][k]*d[k] for k in range(i)),arb(0))
        assert di>0,('uncertified source Gram',i,di);d.append(di);L[i][i]=arb(1)
        for j in range(i+1,n):L[j][i]=(x[j,i]-sum((L[j][k]*L[i][k]*d[k] for k in range(i)),arb(0)))/di
    return [desc(v) for v in d]
def orthogonal(v,cols):
    for _ in range(2):
        for w in cols:v=(v-w*(dot(w,v)/dot(w,w))).mid()
    return (v/norm(v)).mid()

root=a.repo/'research/x-c1'
cases=[('A8',root/'first-chamber-o8-o9-2026-09-27/o8-rechenstand','reserve_refined'),
       ('A9',root/'chambers-through-a11-2026-09-28/a9','reserve_results'),
       ('A11',root/'chambers-through-a11-2026-09-28/a11','reserve_results')]
for name,folder,stem in cases:
    model=read(folder/(name.lower()+'_model.json.gz'),True)
    lower=read(folder/(stem+'_lower_matrices.json.gz'),True)
    receipt=read(folder/(stem+'.json'))
    physical=read(folder/'preconditioned_results.json') if name=='A11' else receipt
    for parity in ('even','odd'):
        key=name+'-'+parity
        if a.only and key not in a.only:continue
        started=time.time();n=model['parities'][parity]['dimension'];m=a.max_rank+1
        print(key,'source construction',flush=True)
        fm=matrix(lower['parities'][parity]['lower_matrix']).mid()
        if fixed:
            seq=[fixed[key+'-'+str(j+1)]['coefficients'] for j in range(m)]
        else:
            finv=fm.inv().mid()
            locked=[arb_mat([[rational(x)] for x in old[key+'-'+str(j+1)]['coefficients']]) for j in range(3)]
            vecs=locked[:]
            for j in range(3,m):
                v=arb_mat([[int(i==j)] for i in range(n)])
                vecs.append(orthogonal(v,vecs))
            for it in range(a.iterations):
                trial=finv*columns(vecs[3:]);updated=locked[:]
                for j in range(m-3):updated.append(orthogonal(col(trial,j),updated))
                vecs=updated
                if (it+1)%8==0:print(key,'diagnostic extension iteration',it+1,flush=True)
            seq=[old[key+'-'+str(j+1)]['coefficients'] if j<3 else
                 [vecs[j][i,0].str(90,radius=False) for i in range(n)] for j in range(m)]
        assert all(seq[j]==old[key+'-'+str(j+1)]['coefficients'] for j in range(3))
        for j,coeff in enumerate(seq):outvec[key+'-'+str(j+1)]={'coefficients':coeff,'parity':parity,'terminal':name}
        V=arb_mat([[rational(seq[j][i]) for j in range(m)] for i in range(n)])
        VG=V.transpose()*V;ldl_positive(VG)
        L=matrix(model['parities'][parity]['A']);eL=rational(receipt['low_form_error_exact'])
        S=V.transpose()*L*V
        for i in range(m):
            for j in range(m):S[i,j]+=arb(0,(eL*(VG[i,i]*VG[j,j]).sqrt()).upper())
        pivots=ldl_positive(S)
        pi=int(parity=='odd');degrees=list(range(pi+2,model['cutoff']+1,2))
        carrier=[]
        for j in range(m):carrier.append(-sum((V[i,j]*arb(2*k+1).sqrt()*ball(model['raw_low_moments'][k]) for i,k in enumerate(degrees)),arb(0))/(arb(2*pi+1).sqrt()*ball(model['raw_low_moments'][pi])))
        G=VG+arb_mat([[carrier[i]*carrier[j] for j in range(m)] for i in range(m)])
        # Extract the actually certified parity floor from the old package.
        pp=physical['parities'][parity]
        c=Fraction(int(pp['full_physical_reserve'][0]),DEN)
        tau_lower=c/(c+17);assert c>0
        rows=[]
        for rank in range(1,a.max_rank+1):
            sr=cut(S,rank);h=arb_mat([[S[i,rank]] for i in range(rank)])
            correction=sr.solve(h,algorithm='precond')
            energy=S[rank,rank]-dot(h,correction)
            coeff=arb_mat([[-correction[i,0]] for i in range(rank)]+[[1]])
            norm2=dot(coeff,cut(G,rank+1)*coeff)
            assert energy>0 and norm2>0,(key,rank,energy,norm2)
            upper=energy.upper()/(energy.upper()+17*norm2.lower())
            assert upper>0 and upper<1
            upper_exact=exact(upper,False)
            assert Fraction(upper_exact)>=tau_lower
            # S*correction=h defines the exact q-orthogonal witness for actual L.
            rows.append({'rank':rank,'tau_lower_exact':str(tau_lower),
                         'tau_upper_exact':upper_exact,'tau_upper_display':float(upper),
                         'witness':'v_(r+1) - V_r (V_r* L V_r)^-1 V_r* L v_(r+1)',
                         'witness_energy':desc(energy),'witness_L2_norm_squared':desc(norm2)})
            print(key,'r',rank,'tau <=',float(upper),flush=True)
        results[key]={'old_only':True,'new_terminal_used':False,'first_three_vectors_preserved':True,
                      'old_physical_floor_exact':str(c),'ranks':rows,'source_gram_positive_pivots':pivots,
                      'projected_gram_denominator':str(10**140),
                      'projected_form_gram':[[integer_pair(S[i,j]) for j in range(m)] for i in range(m)],
                      'projected_L2_gram':[[integer_pair(G[i,j]) for j in range(m)] for i in range(m)],
                      'seconds':time.time()-started}
        (a.out/'fixed_vectors.json').write_text(json.dumps(outvec,indent=2)+'\n',encoding='utf-8')
        report={'status':'OLD_ONLY_COMPLEMENT_GAP_BOUNDS','source_commit':PIN,'precision_bits':a.bits,
                'source_sha256':sources,'old_vectors_sha256':hashlib.sha256(a.old_vectors.read_bytes()).hexdigest(),
                'fixed_vectors_sha256':hashlib.sha256((a.out/'fixed_vectors.json').read_bytes()).hexdigest(),
                'lower_bound_method':'same-terminal certified physical floor c/(c+17)',
                'upper_bound_method':'exact q-orthogonalized finite polynomial witness in full complement',
                'space_choice':'old F-diagnostic low vectors, first 3 fixed; not certified spectral subspace',
                'results':results}
        (a.out/'gap_bounds.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(key,'complete',round(time.time()-started,1),'seconds',flush=True)
print('COMPLETE',flush=True)
