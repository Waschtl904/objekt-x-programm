"""Read-only exploratory comparison, not a positivity certificate or status update.

High precision is used on the rational midpoint matrices. Original input
intervals are retained for Rayleigh-direction bounds. Physical cross-horizon
transport is NOT represented by padding Legendre coefficient vectors.
"""
from pathlib import Path
from fractions import Fraction
import argparse,gzip,hashlib,json,subprocess,sys,time
from flint import arb,arb_mat,fmpq,ctx
sys.set_int_max_str_digits(100000)
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
p.add_argument('--bits',type=int,default=768);p.add_argument('--modes',type=int,default=3)
p.add_argument('--only',nargs='*');args=p.parse_args();ctx.prec=args.bits
PIN='d16ba43ebb20f2c61f43379fc65d7a9b9dba76de'
git=r'C:\Program Files\Git\cmd\git.exe'
assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=args.repo).decode().strip()==PIN
args.out.mkdir(parents=True,exist_ok=True)
root=args.repo/'research/x-c1';scale=10**100
inputs={};summaries={};vectors={};matrices={};bases={}
def read(path,zipped=False):
    raw=path.read_bytes();rel=path.relative_to(args.repo).as_posix()
    committed=subprocess.check_output([git,'show',PIN+':'+rel],cwd=args.repo)
    assert raw==committed,rel
    inputs[rel]=hashlib.sha256(raw).hexdigest()
    return json.loads(gzip.decompress(raw) if zipped else raw)
def mid(pair):return arb(fmpq(int(pair[0])+int(pair[1]),2*scale))
def ball(pair):return mid(pair)+arb(0,arb(fmpq(int(pair[1])-int(pair[0]),2*scale)))
def rat(value):return arb(fmpq(str(value)))
def midpoint_matrix(rows):
    a=arb_mat([[mid(x) for x in row] for row in rows]);return ((a+a.transpose())/2).mid()
def point(a):return a.str(70,radius=False)
def dot(a,b):return (a.transpose()*b)[0,0]
def norm(a):return dot(a,a).sqrt()
def normalize(a):return (a/norm(a)).mid()
def column(a,j):return arb_mat([[a[i,j]] for i in range(a.nrows())])
def orthogonalize(a):
    cols=[]
    for j in range(a.ncols()):
        x=column(a,j)
        for _ in range(2):
            for y in cols:x=(x-y*dot(y,x)).mid()
        cols.append(normalize(x))
    return arb_mat([[col[i,0] for col in cols] for i in range(a.nrows())])
def ldl_basis(a):
    n=a.nrows();L=[[arb(0)]*n for _ in range(n)];d=[]
    for i in range(n):
        di=(a[i,i]-sum((L[i][k]*L[i][k]*d[k] for k in range(i)),arb(0))).mid()
        assert di>0,('midpoint LDL',i,di);d.append(di);L[i][i]=arb(1)
        for j in range(i+1,n):
            L[j][i]=((a[j,i]-sum((L[j][k]*L[i][k]*d[k] for k in range(i)),arb(0)))/di).mid()
    P=arb_mat(L).inv().transpose().mid()
    return P,d
cases=[('A8',root/'first-chamber-o8-o9-2026-09-27/o8-rechenstand','reserve_refined'),
       ('A9',root/'chambers-through-a11-2026-09-28/a9','reserve_results'),
       ('A11',root/'chambers-through-a11-2026-09-28/a11','reserve_results')]
for name,folder,stem in cases:
    model=read(folder/(name.lower()+'_model.json.gz'),True)
    raw=read(folder/(stem+'_lower_matrices.json.gz'),True)
    receipt=read(folder/(('preconditioned_results' if name=='A11' else stem)+'.json'))
    original=read(folder/(stem+'.json')) if name=='A11' else receipt
    for parity in ('even','odd'):
        key=name+'-'+parity
        if args.only and key not in args.only:continue
        started=time.time();print(key,'loading and inverting midpoint',flush=True)
        source=raw['parities'][parity]['lower_matrix'];n=len(source);m=args.modes
        fm=midpoint_matrix(source);full=arb_mat([[ball(x) for x in row] for row in source])
        inv=fm.inv().mid();matrices[key]=source
        x=arb_mat([[int(i==j) for j in range(m)] for i in range(n)])
        for iteration in range(1,81):
            x=orthogonalize(inv*x)
            if iteration>=8 and iteration%4==0:
                errors=[]
                for j in range(m):
                    v=column(x,j);lam=dot(v,fm*v);errors.append(norm(fm*v-v*lam)/abs(lam))
                if all(e<arb('1e-25') for e in errors):break
        print(key,'inverse iteration',iteration,'relative residuals',[float(e) for e in errors],flush=True)
        L=midpoint_matrix(model['parities'][parity]['A'])
        G=midpoint_matrix(model['parities'][parity]['complete_model_raw_high_Gram'])
        delta=rat(receipt['full_high_physical_floor']);eL=rat(receipt['low_form_error_exact'])
        eB=rat(receipt['parities'][parity]['coupling_operator_error_exact'])
        rows=[];pidx=int(parity=='odd');degrees=list(range(2+pidx,2*n+1+pidx,2))
        for j in range(m):
            v=column(x,j);lam=dot(v,fm*v);energy=[float(v[i,0])**2 for i in range(n)]
            cumulative=0;quantiles={}
            for i,value in enumerate(energy):
                cumulative+=value
                for threshold in (.5,.9,.99,.999):
                    if cumulative>=threshold and str(threshold) not in quantiles:quantiles[str(threshold)]=degrees[i]
            lq=dot(v,L*v);gq=dot(v,G*v);hc=(rat('1001/1000')*gq+1001*eB*eB)/delta
            residual=norm(fm*v-v*lam)/abs(lam)
            # Interval evaluation along a fixed dyadic point vector: this is a
            # Rayleigh-direction enclosure, not an enclosed eigenvector.
            fixed=v.mid();rayleigh=dot(fixed,full*fixed)/dot(fixed,fixed)
            carrier=-sum((v[i,0]*arb(2*k+1).sqrt()*mid(model['raw_low_moments'][k])
                         for i,k in enumerate(degrees)),arb(0))/(arb(2*pidx+1).sqrt()*mid(model['raw_low_moments'][pidx]))
            row={'mode':j+1,'midpoint_eigenvalue_approx':point(lam),'relative_residual':float(residual),
                 'rayleigh_interval':rayleigh.str(30),'low_model_rayleigh':point(lq),
                 'coupling_penalty_rayleigh':point(hc),'low_model_error':point(eL),
                 'coupling_penalty_over_low_model':float(hc/lq),'degree_energy_quantiles':quantiles,
                 'top_degrees':[{'degree':degrees[i],'coefficient':float(v[i,0])}
                                for i in sorted(range(n),key=lambda i:energy[i],reverse=True)[:10]],
                 'physical_norm_squared_reference':point(1+carrier*carrier)}
            rows.append(row)
            vectors[key+f'-{j+1}']={'endpoint':float(mid(model['endpoint_interval'])),'parity':parity,
                'degrees':degrees,'coefficients':[point(v[i,0]) for i in range(n)],'carrier_coefficient':point(carrier)}
        print(key,'midpoint LDL basis',flush=True)
        P,d=ldl_basis(fm);bases[key]=P
        colnorm=[sum((P[i,j]*P[i,j] for i in range(n)),arb(0)) for j in range(n)]
        summ={'dimension':n,'endpoint':model['endpoint'],'gamma_degree':model['Gamma_degree'],
              'active_prime_powers':model['active_prime_powers'],'high_floor':receipt['full_high_physical_floor'],
              'published_physical_reserve':receipt['parities'][parity]['full_physical_reserve_display'],
              'midpoint_inverse_trace_floor':point(1/inv.trace()),'modes':rows,
              'basis':{'kind':'midpoint L^-T, diagnostic only','frobenius_squared':point(sum(colnorm,arb(0))),
                       'minimum_pivot':point(min(d)),'maximum_pivot':point(max(d)),
                       'max_column_norm_squared':point(max(colnorm)),
                       'max_column_degree':degrees[max(range(n),key=lambda j:float(colnorm[j]))]},
              'seconds':time.time()-started}
        summaries[key]=summ
        print(key,'lambda1',rows[0]['midpoint_eigenvalue_approx'][:30],'done',round(summ['seconds'],1),flush=True)
        (args.out/'diagnostics.json').write_text(json.dumps({'status':'EXPLORATORY_NOT_A_GENERAL_PROOF','source_commit':PIN,
           'precision_bits':args.bits,'input_sha256':inputs,'cases':summaries},indent=2)+'\n',encoding='utf-8')
        (args.out/'critical_vectors.json').write_text(json.dumps(vectors,indent=2)+'\n',encoding='utf-8')
comparison={}
for left,right in [('A8','A9'),('A9','A11'),('A8','A11')]:
    for parity in ('even','odd'):
        lk,rk=left+'-'+parity,right+'-'+parity
        if lk not in matrices or rk not in matrices:continue
        a,b=matrices[lk],matrices[rk];n=min(len(a),len(b));diff=[]
        for i in range(n):
            lo=int(b[i][i][0])-int(a[i][i][1]);hi=int(b[i][i][1])-int(a[i][i][0])
            diff.append((lo,hi))
        cmp={'common_reference_coefficient_dimension':n,'not_physical_zero_extension':True,
             'strict_negative_diagonal_count':sum(hi<0 for lo,hi in diff),
             'strict_positive_diagonal_count':sum(lo>0 for lo,hi in diff),'diagonal_witnesses':[],'basis_cosines':[]}
        for label,which in [('minimum',min(range(n),key=lambda i:diff[i][1])),('maximum',max(range(n),key=lambda i:diff[i][0]))]:
            cmp['diagonal_witnesses'].append({'type':label,'degree':2+int(parity=='odd')+2*which,
              'interval_numerators':list(map(str,diff[which])),'denominator':str(scale),
              'display':[float(Fraction(v,scale)) for v in diff[which]]})
        for j in (15,31,63,95,127,159,190):
            if j>=n:continue
            v=[bases[lk][i,j] for i in range(j+1)];w=[bases[rk][i,j] for i in range(j+1)]
            cosine=abs(sum((x*y for x,y in zip(v,w)),arb(0)))/(
              sum((x*x for x in v),arb(0))*sum((x*x for x in w),arb(0))).sqrt()
            cmp['basis_cosines'].append({'column_degree':2+int(parity=='odd')+2*j,'absolute_cosine':float(cosine)})
        comparison[lk+'->'+rk]=cmp
data=json.loads((args.out/'diagnostics.json').read_bytes());data['reference_comparisons']=comparison
(args.out/'diagnostics.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('COMPARISON COMPLETE',flush=True)
