"""Standard-library integer interval replay of projected complement witnesses.

Starts from saved outward Gram intervals. It does not rebuild those intervals
from terminal integrals; their construction is the separate Arb computation.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess

SCALE=10**220
def updiv(a,b): return -((-a)//b)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    vals=[x*y for x in a for y in b]
    return (min(vals)//SCALE,updiv(max(vals),SCALE))
def div(a,b):
    assert b[0]*b[1]>0
    lo=[x*SCALE//y for x in a for y in b]
    hi=[updiv(x*SCALE,y) for x in a for y in b]
    return (min(lo),max(hi))
ZERO=(0,0);ONE=(SCALE,SCALE)
def isum(xs):
    s=ZERO
    for x in xs:s=add(s,x)
    return s
def load_matrix(rows,den):
    assert SCALE%den==0;factor=SCALE//den
    return [[(int(x[0])*factor,int(x[1])*factor) for x in row] for row in rows]
def ldl(a):
    n=len(a);L=[[ZERO]*n for _ in range(n)];d=[]
    for i in range(n):
        di=sub(a[i][i],isum(mul(mul(L[i][k],L[i][k]),d[k]) for k in range(i)))
        assert di[0]>0,('pivot',i,di);d.append(di);L[i][i]=ONE
        for j in range(i+1,n):
            L[j][i]=div(sub(a[j][i],isum(mul(mul(L[j][k],L[i][k]),d[k]) for k in range(i))),di)
    return L,d
def solve(L,d,h):
    n=len(h);z=[]
    for i in range(n):z.append(sub(h[i],isum(mul(L[i][j],z[j]) for j in range(i))))
    z=[div(z[i],d[i]) for i in range(n)];x=[ZERO]*n
    for i in reversed(range(n)):x[i]=sub(z[i],isum(mul(L[j][i],x[j]) for j in range(i+1,n)))
    return x
def rational_tests():
    eps=F(1,10**30);tilt=F(1,10**15)
    # q=diag(eps,1), k=(1,tilt), n=(tilt,-eps).
    assert eps*tilt+tilt*(-eps)==0
    mu=(eps*tilt**2+eps**2)/(tilt**2+eps**2)
    assert mu==2*eps/(1+eps)
    tau=mu/(mu+17)
    assert 0<tau<2*eps/17
    # A separate exact Schur projection example in a nonorthogonal source basis.
    Q=[[F(3),F(1)],[F(1),F(2)]];k=[F(1),F(2)];v=[F(2),F(-1)]
    def q(a,b):return sum(a[i]*Q[i][j]*b[j] for i in range(2) for j in range(2))
    s=q(k,k);h=q(k,v);alpha=h/s;w=[v[i]-alpha*k[i] for i in range(2)]
    assert q(k,w)==0 and q(w,w)==q(v,v)-h*h/s
    return {'q_orthogonality_and_schur_projection':'PASS','near_eigenvector_counterexample':'PASS',
            'counterexample_epsilon':str(eps),'counterexample_tau':str(tau)}

def main():
    p=argparse.ArgumentParser()
    for key in ('primary','crosscheck','vectors','old-vectors','out'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--repo',type=Path);a=p.parse_args()
    one=json.loads(a.primary.read_bytes());two=json.loads(a.crosscheck.read_bytes())
    vectors=json.loads(a.vectors.read_bytes());old=json.loads(a.old_vectors.read_bytes())
    assert one['source_commit']==two['source_commit'] and one['source_sha256']==two['source_sha256']
    assert one['old_vectors_sha256']==two['old_vectors_sha256']==hashlib.sha256(a.old_vectors.read_bytes()).hexdigest()
    assert one['fixed_vectors_sha256']==two['fixed_vectors_sha256']==hashlib.sha256(a.vectors.read_bytes()).hexdigest()
    assert len(one['results'])==len(two['results'])==6
    results={};max_difference=F(0)
    for case,item in two['results'].items():
        for j in (1,2,3):assert vectors[case+'-'+str(j)]['coefficients']==old[case+'-'+str(j)]['coefficients']
        form=load_matrix(item['projected_form_gram'],int(item['projected_gram_denominator']))
        gram=load_matrix(item['projected_L2_gram'],int(item['projected_gram_denominator']))
        L,d=ldl(form);ldl(gram)
        rows=[]
        for rank in range(1,21):
            arow=one['results'][case]['ranks'][rank-1];brow=item['ranks'][rank-1]
            assert arow['rank']==brow['rank']==rank
            lower=F(brow['tau_lower_exact']);assert lower==F(arow['tau_lower_exact'])
            old_c=F(item['old_physical_floor_exact']);assert lower==old_c/(old_c+17)
            au=F(arow['tau_upper_exact']);bu=F(brow['tau_upper_exact'])
            assert 0<lower<=min(au,bu)<1
            difference=abs(au-bu)/max(au,bu);max_difference=max(max_difference,difference)
            assert difference<F(1,10**5)
            h=[form[i][rank] for i in range(rank)]
            correction=solve(L,d,h)
            energy=sub(form[rank][rank],isum(mul(h[i],correction[i]) for i in range(rank)))
            coeff=[neg(x) for x in correction]+[ONE]
            norm=isum(mul(mul(coeff[i],gram[i][j]),coeff[j]) for i in range(rank+1) for j in range(rank+1))
            assert energy[0]>0 and norm[0]>0,(case,rank,'inconclusive integer witness')
            upper=F(energy[1],energy[1]+17*norm[0])
            assert lower<=upper<1
            rows.append({'rank':rank,'tau_lower_exact':str(lower),
                         'integer_replay_raw_upper_exact':str(upper),
                         'witness_energy_upper_exact':str(F(energy[1],SCALE)),
                         'witness_norm_squared_lower_exact':str(F(norm[0],SCALE)),
                         'relative_L2_distance_to_K_squared_upper_exact':str(min(F(1),F(gram[rank][rank][1],norm[0]))),
                         'arb_raw_upper_exact':str(max(au,bu)),
                         'combined_raw_upper_exact':str(max(upper,au,bu))})
        # A witness in R_j also lies in R_r whenever j >= r.
        for i,row in enumerate(rows):
            chosen=min(range(i,20),key=lambda j:F(rows[j]['combined_raw_upper_exact']))
            row['monotone_upper_exact']=rows[chosen]['combined_raw_upper_exact']
            row['upper_witness_rank']=chosen+1
        assert all(F(rows[i]['monotone_upper_exact'])<=F(rows[i+1]['monotone_upper_exact']) for i in range(19))
        results[case]={'positive_form_pivots':len(d),'ranks':rows}
        print(case,'20 integer witness replays PASS',flush=True)
    bindings=[]
    if a.repo:
        git=shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe';pin=one['source_commit']
        assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==pin
        for path,digest in one['source_sha256'].items():
            raw=(a.repo/path).read_bytes();assert hashlib.sha256(raw).hexdigest()==digest
            assert raw==subprocess.check_output([git,'show',pin+':'+path],cwd=a.repo)
            bindings.append(path)
    result={'status':'PASS','source_commit':one['source_commit'],
            'scope':'Independent integer replay from Arb-produced Gram intervals; terminal model construction not repeated',
            'integer_decimal_places':220,'witness_count':120,'results':results,
            'maximum_relative_Arb_upper_change':float(max_difference),
            'rational_tests':rational_tests(),'verified_repository_sources':bindings,
            'fixed_vectors_sha256':hashlib.sha256(a.vectors.read_bytes()).hexdigest()}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS: 120 witnesses, 126 positive source-form pivots,',len(bindings),'source bindings.')

if __name__=='__main__':main()
