"""Bound full source-space coupling across two ALREADY certified terminals.

This measures a retrospective construction. New-terminal positivity and the
existing full-high certificates are input assumptions, not conclusions derived
from old data alone. No new-terminal eigenvectors are used to choose K_A.
"""
from pathlib import Path
from fractions import Fraction
import argparse,gzip,hashlib,json,subprocess,sys,time
import flint
from flint import arb,arb_mat,fmpq,ctx
assert flint.__version__=='0.9.0'
sys.set_int_max_str_digits(100000)
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
p.add_argument('--vectors',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
p.add_argument('--bits',type=int,default=1024);p.add_argument('--quadrature-extra',type=int,default=0)
p.add_argument('--only',nargs='*');a=p.parse_args();ctx.prec=a.bits
PIN='d16ba43ebb20f2c61f43379fc65d7a9b9dba76de';scale=10**100
git=r'C:\Program Files\Git\cmd\git.exe'
assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==PIN
a.out.mkdir(parents=True,exist_ok=True);inputs={};cache={};results={}
vectors=json.loads(a.vectors.read_bytes())
def read(path,zipped=False):
    if str(path) in cache:return cache[str(path)]
    raw=path.read_bytes();rel=path.relative_to(a.repo).as_posix()
    assert raw==subprocess.check_output([git,'show',PIN+':'+rel],cwd=a.repo),rel
    inputs[rel]=hashlib.sha256(raw).hexdigest()
    value=json.loads(gzip.decompress(raw) if zipped else raw);cache[str(path)]=value;return value
def ball(pair):
    lo,hi=map(int,pair);assert lo<=hi
    return arb(fmpq(lo+hi,2*scale))+arb(0,arb(fmpq(hi-lo,2*scale)))
def rational(value):
    f=Fraction(value);return arb(fmpq(f.numerator,f.denominator))
def matrix(rows):return arb_mat([[ball(x) for x in row] for row in rows])
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def prefix(x,n):return arb_mat([[x[i,j] for j in range(n)] for i in range(n)])
def enclose(x):return {'display':x.str(22),'lower':x.lower().str(60,radius=False),'upper':x.upper().str(60,radius=False)}
def exact_outward(x,lower=True,digits=110):
    s=10**digits;v=x.lower() if lower else x.upper()
    n=int(((v*s).floor() if lower else (v*s).ceil()).unique_fmpz())
    return str(Fraction(n,s))
def interval_ldl(x):
    n=x.nrows();L=[[arb(0)]*n for _ in range(n)];piv=[]
    for i in range(n):
        d=x[i,i]-sum((L[i][k]*L[i][k]*piv[k] for k in range(i)),arb(0))
        assert d>0,('small Gram not certified',i,d);piv.append(d);L[i][i]=arb(1)
        for j in range(i+1,n):
            L[j][i]=(x[j,i]-sum((L[j][k]*L[i][k]*piv[k] for k in range(i)),arb(0)))/d
    return [enclose(x) for x in piv]
def legendre(x,n):
    # Evaluate at the exact dyadic midpoint to avoid exponential dependency
    # widening of the three-term recurrence on an uncertain argument. On [-1,1],
    # |P_k'| <= k(k+1)/2 follows from P_k' = sum (2j+1)P_j and |P_j|<=1.
    assert x>=-1 and x<=1
    radius=x.rad();x=x.mid()
    seq=[arb(1)]
    if n:seq.append(x)
    for j in range(2,n+1):seq.append(((2*j-1)*x*seq[-1]-(j-1)*seq[-2])/j)
    return [v+arb(0,(radius*k*(k+1)/2).upper()) for k,v in enumerate(seq)]
root=a.repo/'research/x-c1'
folders={'A8':root/'first-chamber-o8-o9-2026-09-27/o8-rechenstand',
         'A9':root/'chambers-through-a11-2026-09-28/a9',
         'A11':root/'chambers-through-a11-2026-09-28/a11'}
def data(name):
    folder=folders[name];stem='reserve_refined' if name=='A8' else 'reserve_results'
    return (read(folder/(name.lower()+'_model.json.gz'),True),read(folder/(stem+'.json')),
            read(folder/(stem+'_lower_matrices.json.gz'),True))
for old,new in [('A8','A9'),('A9','A11')]:
    mo,ro,fo=data(old);mn,rn,fn=data(new)
    certificate=read(folders[new]/'common_reserve.json');c=rational(certificate['common_physical_floor_exact'])
    assert c>0;alpha=c/(c+17)
    for parity in ('even','odd'):
        key=old+'->'+new+'-'+parity
        if a.only and key not in a.only:continue
        started=time.time();print(key,'old source space',flush=True)
        pi=int(parity=='odd');nold=mo['parities'][parity]['dimension'];nnew=mn['parities'][parity]['dimension'];r=3
        degrees=list(range(pi+2,mo['cutoff']+1,2))
        V=arb_mat([[rational(vectors[f'{old}-{parity}-{j+1}']['coefficients'][i]) for j in range(r)] for i in range(nold)])
        VG=V.transpose()*V;interval_ldl(VG)
        carrier=[]
        for j in range(r):
            carrier.append(-sum((V[i,j]*arb(2*k+1).sqrt()*ball(mo['raw_low_moments'][k])
                                 for i,k in enumerate(degrees)),arb(0))/(arb(2*pi+1).sqrt()*ball(mo['raw_low_moments'][pi])))
        G=VG+arb_mat([[carrier[i]*carrier[j] for j in range(r)] for i in range(r)])
        S=V.transpose()*matrix(mo['parities'][parity]['A'])*V
        old_error=rational(ro['low_form_error_exact'])
        for i in range(r):
            for j in range(r):S[i,j]+=arb(0,(old_error*(VG[i,i]*VG[j,j]).sqrt()).upper())
        old_pivots=interval_ldl(S);B=S+17*G
        Aold=ball(mo['endpoint_interval']);Anew=ball(mn['endpoint_interval']);rho=Aold/Anew
        assert rho>0 and rho<1
        m_e=arb(2*pi+1).sqrt()*ball(mn['raw_low_moments'][pi])
        moments_norm=(Anew.sinh()/Anew+(1 if pi==0 else -1))/2
        factor=moments_norm/(m_e*m_e)
        count=(mo['cutoff']+mn['cutoff']+2)//2+a.quadrature_extra
        print(key,'physical zero extension, Gauss nodes',count,flush=True)
        overlap=arb_mat(nnew+1,r) # first row is the normalized moment carrier e_p
        newdegrees=[pi]+list(range(pi+2,mn['cutoff']+1,2))
        for k in range(count):
            x,w=arb.legendre_p_root(count,k,weight=True)
            oldpol=legendre(x,mo['cutoff']);newpol=legendre(rho*x,mn['cutoff'])
            vals=[sum((V[i,j]*arb(2*d+1).sqrt()*oldpol[d] for i,d in enumerate(degrees)),
                      carrier[j]*arb(2*pi+1).sqrt()*oldpol[pi]) for j in range(r)]
            weight=rho.sqrt()*w/2
            for i,d in enumerate(newdegrees):
                base=weight*arb(2*d+1).sqrt()*newpol[d]
                for j in range(r):overlap[i,j]+=base*vals[j]
        beta=[overlap[0,j] for j in range(r)]
        aa=arb_mat([[overlap[i+1,j]-beta[j]*arb(2*d+1).sqrt()*ball(mn['raw_low_moments'][d])/m_e
                     for j in range(r)] for i,d in enumerate(newdegrees[1:])])
        Hdual=G+arb_mat([[factor*beta[i]*beta[j] for j in range(r)] for i in range(r)])-aa.transpose()*aa
        assert Hdual.trace()>0,('high dual tail unresolved',Hdual.trace())
        print(key,'full resolvent bounds',flush=True)
        F=matrix(fn['parities'][parity]['lower_matrix'])
        Finv=F.solve(eye(nnew),algorithm='precond')
        assert all(x.is_finite() for x in Finv.entries())
        Lupper=matrix(mn['parities'][parity]['A'])+eye(nnew)*rational(rn['low_form_error_exact'])
        Lupperinv=Lupper.solve(eye(nnew),algorithm='precond')
        assert all(x.is_finite() for x in Lupperinv.entries())
        Hup=matrix(mn['parities'][parity]['complete_model_raw_high_Gram'])*rational('1001/1000')
        eB=rational(rn['parities'][parity]['coupling_operator_error_exact'])
        Hup+=eye(nnew)*(1001*eB*eB)
        tr=(Finv*Hup).trace();assert tr>0
        delta=rational(rn['full_high_physical_floor'])
        Tlo=aa.transpose()*Lupperinv*aa
        chi=2*tr.upper()/(delta*delta)+1/delta
        Thi=2*(aa.transpose()*Finv*aa)+Hdual*chi
        Rlo=S+34*G+289*Tlo;Rhi=S+34*G+289*Thi
        ranks=[]
        for rank in (1,2,3):
            sr=prefix(S,rank);br=prefix(B,rank);gr=prefix(G,rank)
            bi=br.inv();weight=bi*sr*bi
            tlo=(prefix(Rlo,rank)*weight).trace();thi=(prefix(Rhi,rank)*weight).trace()
            assert tlo>0 and thi>0
            survival_lower=1/thi.upper();survival_upper=rank/tlo.lower()
            assert survival_lower>0 and survival_upper<1
            ranks.append({'rank':rank,'one_minus_kappa_lower_exact':exact_outward(survival_lower,True),
              'one_minus_kappa_upper_exact':exact_outward(survival_upper,False),
              'one_minus_kappa_display':[float(survival_lower),float(survival_upper)],
              'weighted_resolvent_trace_lower':enclose(tlo),'weighted_resolvent_trace_upper':enclose(thi),
              'source_form_gram':[[enclose(sr[i,j]) for j in range(rank)] for i in range(rank)]})
            print(key,'r',rank,'1-kappa in',[float(survival_lower),float(survival_upper)],flush=True)
        results[key]={'status':'CONDITIONAL_FULL_SOURCE_SPACE_COUPLING_BOUNDS','old':old,'new':new,'parity':parity,
           'old_space_uses_new_terminal_eigenvectors':False,'K_definition':'first r fixed old rational coefficient vectors, exact old Mellin correction, physical zero extension',
           'old_S_positive_interval_pivots':old_pivots,'new_D_b_metric_floor_exact':str(Fraction(certificate['common_physical_floor_exact'])/(Fraction(certificate['common_physical_floor_exact'])+17)),
           'D_floor_depends_on_existing_new_terminal_certificate':True,
           'quadrature_nodes':count,'high_dual_gram_trace':enclose(Hdual.trace()),
           'complete_coupling_trace_bound':enclose(tr),'ranks':ranks,'seconds':time.time()-started}
        report={'status':'RETROSPECTIVE_COUPLING_BOUNDS_NOT_A_FORWARD_RENEWAL_PROOF','source_commit':PIN,
          'arithmetic':'python-flint 0.9.0 Arb directed intervals','precision_bits':a.bits,
          'old_vector_file_sha256':hashlib.sha256(a.vectors.read_bytes()).hexdigest(),'source_sha256':inputs,
          'scope':'Both known transitions, both parities, nested ranks 1/2/3; complete high response bounded, not truncated',
          'results':results}
        (a.out/'coupling_bounds.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(key,'complete',round(time.time()-started,1),'seconds',flush=True)
print('ALL REQUESTED CASES COMPLETE',flush=True)
