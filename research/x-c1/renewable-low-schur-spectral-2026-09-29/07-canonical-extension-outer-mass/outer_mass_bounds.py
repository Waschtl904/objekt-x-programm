"""Certified outer-mass enclosures for canonical extension spaces.

Polynomial subspaces are auxiliary. Their full physical spectral residuals
enclose the true spectral subspaces; no test vector is called an eigenvector.
The final E matrix uses the exact polar projection from an auxiliary kernel.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,gzip,hashlib,json,shutil,subprocess,time
import flint
from flint import arb,arb_mat,fmpq,ctx

PIN='d16ba43ebb20f2c61f43379fc65d7a9b9dba76de'
DEN=10**100
CASES={'A8':('research/x-c1/first-chamber-o8-o9-2026-09-27/o8-rechenstand','reserve_refined',5),
 'A9':('research/x-c1/chambers-through-a11-2026-09-28/a9','reserve_results',6),
 'A11':('research/x-c1/chambers-through-a11-2026-09-28/a11','reserve_results',8)}
def rat(x):
    f=Q(x);return arb(fmpq(f.numerator,f.denominator))
def ball(x):
    l,h=map(int,x);assert l<=h
    return arb(fmpq(l+h,2*DEN))+arb(0,arb(fmpq(h-l,2*DEN)))
def mat(rows):return arb_mat([[ball(x) for x in row] for row in rows])
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def exact(x,lower=True):
    s=10**120;v=x.lower() if lower else x.upper()
    mantissa,exponent=v.man_exp();mantissa=int(mantissa);exponent=int(exponent)
    dyadic=Q(mantissa*2**exponent) if exponent>=0 else Q(mantissa,2**(-exponent))
    scaled=dyadic*s
    z=scaled.numerator//scaled.denominator if lower else -((-scaled.numerator)//scaled.denominator)
    return str(Q(z,s))
def iv(x):return [exact(x),exact(x,False)]
def matrix_iv(x):return [[iv(x[i,j]) for j in range(x.ncols())] for i in range(x.nrows())]
def frob(x):return sum((x[i,j]*x[i,j] for i in range(x.nrows()) for j in range(x.ncols())),arb(0)).sqrt()
def gupper(x):return max(x[i,i].upper()+sum((abs(x[i,j]).upper() for j in range(x.ncols()) if j!=i),arb(0)) for i in range(x.nrows()))
def glower(x):return min(x[i,i].lower()-sum((abs(x[i,j]).upper() for j in range(x.ncols()) if j!=i),arb(0)) for i in range(x.nrows()))
def orthogonalizer(g):
    n=g.nrows();l=arb_mat(n,n)
    for i in range(n):
        v=g[i,i]-sum((l[i,k]*l[i,k] for k in range(i)),arb(0));assert v>0
        l[i,i]=v.sqrt()
        for j in range(i+1,n):
            l[j,i]=(g[j,i]-sum((l[j,k]*l[i,k] for k in range(i)),arb(0)))/l[i,i]
    return l.transpose().inv()
def legendre(x,n):
    assert x>=-1 and x<=1
    radius=x.rad();mid=x.mid();seq=[arb(1)]
    if n:seq.append(mid)
    for j in range(2,n+1):seq.append(((2*j-1)*mid*seq[-1]-(j-1)*seq[-2])/j)
    return [v+arb(0,(radius*k*(k+1)/2).upper()) for k,v in enumerate(seq)]
def spectrum_small(x):
    assert x.nrows()==x.ncols() and x.nrows() in (1,2)
    if x.nrows()==1:return [x[0,0]]
    mid=(x[0,0]+x[1,1])/2
    radius=(((x[0,0]-x[1,1])/2)**2+x[0,1]*x[1,0]).sqrt()
    return [mid-radius,mid+radius]

def main():
    p=argparse.ArgumentParser()
    for k in ('repo','vectors','transport','a8-gap','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--bits',type=int,default=1024)
    p.add_argument('--extra-nodes',type=int,default=0)
    a=p.parse_args();ctx.prec=a.bits;assert flint.__version__=='0.9.0'
    git=shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe'
    assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==PIN
    vec=json.loads(a.vectors.read_bytes());transport=json.loads(a.transport.read_bytes())
    a8gap=json.loads(a.a8_gap.read_bytes())
    assert transport['source_commit']==PIN
    assert transport['vectors_sha256']==hashlib.sha256(a.vectors.read_bytes()).hexdigest()
    assert a8gap['source_commit']==PIN and a8gap['status']=='CERTIFIED_A8_FULL_COMPLEMENT_GAPS'
    assert a8gap['vectors_sha256']==transport['vectors_sha256']
    assert a8gap['reference_archive_sha256']==transport['reference_archive_sha256']
    for rel,h in (transport['bound_source_sha256']|a8gap['bound_source_sha256']).items():
        raw=(a.repo/rel).read_bytes();assert hashlib.sha256(raw).hexdigest()==h
        assert raw==subprocess.check_output([git,'show',PIN+':'+rel],cwd=a.repo)
    sources={};trials={};cache={};results={}
    def read(path,zipped=False):
        raw=path.read_bytes();rel=path.relative_to(a.repo).as_posix()
        assert raw==subprocess.check_output([git,'show',PIN+':'+rel],cwd=a.repo)
        sources[rel]=hashlib.sha256(raw).hexdigest()
        return json.loads(gzip.decompress(raw) if zipped else raw)
    for name,(rel,stem,r) in CASES.items():
        folder=a.repo/rel;model=read(folder/(name.lower()+'_model.json.gz'),True)
        receipt=read(folder/(stem+'.json'))
        for parity in ('even','odd'):
            start=time.time();key=name+'-'+parity;pi=int(parity=='odd')
            degrees=list(range(pi+2,model['cutoff']+1,2));n=len(degrees)
            print(key,'physical trial space and complete spectral residual',flush=True)
            v=arb_mat([[rat(vec[key+'-'+str(j+1)]['coefficients'][i]) for j in range(r)] for i in range(n)])
            endpoint=ball(model['endpoint_interval'])
            me=arb(2*pi+1).sqrt()*ball(model['raw_low_moments'][pi])
            tl=arb_mat([[arb(2*d+1).sqrt()*ball(model['raw_low_moments'][d])/me] for d in degrees])
            carrier=-tl.transpose()*v
            gram=v.transpose()*v+carrier.transpose()*carrier
            z=orthogonalizer(gram);v=v*z;carrier=carrier*z
            # Exact physical U=M V is now L2 orthonormal by definition.
            check=v.transpose()*v+carrier.transpose()*carrier
            assert all(check[i,j].contains(int(i==j)) for i in range(r) for j in range(r))
            low=mat(model['parities'][parity]['A']);el=rat(receipt['low_form_error_exact'])
            s=v.transpose()*low*v;vg=v.transpose()*v
            for i in range(r):
                for j in range(r):s[i,j]+=arb(0,(el*(vg[i,i]*vg[j,j]).sqrt()).upper())
            theta=gupper(s);assert theta>0
            rho=((endpoint.sinh()/endpoint+(1 if pi==0 else -1))/2)/(me*me)
            tail2=(rho-1-(tl.transpose()*tl)[0,0]).upper();assert tail2>=0
            eb=rat(receipt['parities'][parity]['coupling_operator_error_exact'])
            hup=mat(model['parities'][parity]['complete_model_raw_high_Gram'])*rat('1001/1000')+eye(n)*(1001*eb*eb)
            # Pullback residual: M*(QU-US)=(Qhat-GS)V. ||M^{-*}||<=1.
            gv=v+tl*(tl.transpose()*v)
            dl=low*v-gv*s
            low_res=frob(dl)+el*frob(v)
            high_res=(v.transpose()*hup*v).trace().sqrt()+tail2.sqrt()*frob(tl.transpose()*v*s)
            residual=(low_res*low_res+high_res*high_res).sqrt().upper()
            receipt_gap=a8gap if name=='A8' else transport
            gap=rat(receipt_gap['gaps'][key]['physical_complement_lower_exact'])
            assert theta<gap
            energy=(theta/gap).sqrt().upper()
            sylvester=(residual/(gap-theta)).upper()
            eta=min(energy,sylvester);assert eta<1
            trials[key]={'rank':r,'physical_trial_max_Rayleigh_upper_exact':exact(theta,False),
                'physical_complement_gap_lower_exact':exact(gap),
                'full_residual_frobenius_upper_exact':exact(residual,False),
                'low_residual_upper_exact':exact(low_res,False),'high_residual_upper_exact':exact(high_res,False),
                'high_mass_tail_squared_upper_exact':exact(tail2,False),
                'projector_error_energy_upper_exact':exact(energy,False),
                'projector_error_residual_upper_exact':exact(sylvester,False),
                'projector_error_used_upper_exact':exact(eta,False),
                'physical_Ritz_matrix':matrix_iv(s),'orthogonalizer':matrix_iv(z),
                'seconds':time.time()-start}
            cache[key]={'A':endpoint,'degrees':degrees,'pi':pi,'v':v,'carrier':carrier,'N':model['cutoff'],
                        'r':r,'eta':eta,'theta':theta}
            print(key,'eta <=',float(eta),'energy',float(energy),'residual',float(sylvester),flush=True)
    nodes={}
    def values(c,points):
        ds=[c['pi']]+c['degrees']
        pol=arb_mat([[seq[d]*arb(2*d+1).sqrt() for d in ds] for seq in (legendre(x,c['N']) for x in points)])
        coeff=arb_mat([[c['carrier'][0,j] for j in range(c['r'])]]+
                      [[c['v'][i,j] for j in range(c['r'])] for i in range(c['v'].nrows())])
        return pol*coeff
    def weighted(x,w):return arb_mat([[x[i,j]*w[i] for j in range(x.ncols())] for i in range(x.nrows())])
    for first,last in [('A8','A9'),('A9','A11')]:
        for parity in ('even','odd'):
            start=time.time();key=first+'->'+last+'-'+parity;aa=cache[first+'-'+parity];bb=cache[last+'-'+parity]
            ratio=aa['A']/bb['A'];r=aa['r'];rn=bb['r'];d=rn-r
            count=max(aa['N'],bb['N'])+1+a.extra_nodes
            if count not in nodes:
                print(key,'Gauss nodes',count,flush=True)
                nodes[count]=[arb.legendre_p_root(count,k,weight=True) for k in range(count)]
            x=[q[0] for q in nodes[count]];w=[q[1] for q in nodes[count]]
            ua=values(aa,x);ub=values(bb,[ratio*t for t in x])
            m=ua.transpose()*weighted(ub,[ratio.sqrt()*wi/2 for wi in w])
            s2=glower(m*m.transpose());assert 0<s2<=1,(key,'overlap lower bound unresolved',s2)
            # Exact kernel basis of overlap with existing old trial space.
            left=arb_mat([[m[i,j] for j in range(r)] for i in range(r)])
            right=arb_mat([[m[i,j] for j in range(r,rn)] for i in range(r)])
            top=-left.solve(right,algorithm='precond')
            f=arb_mat([[top[i,j] for j in range(d)] for i in range(r)]+
                      [[int(i==j) for j in range(d)] for i in range(d)])
            f=f*orthogonalizer(f.transpose()*f)
            assert all((m*f)[i,j].contains(0) for i in range(r) for j in range(d))
            fg=f.transpose()*f;assert all(fg[i,j].contains(int(i==j)) for i in range(d) for j in range(d))
            print(key,'outer-mass polynomial integration',flush=True)
            ubout=values(bb,[(1+ratio)/2+(1-ratio)*t/2 for t in x])
            outer=ubout.transpose()*weighted(ubout,[(1-ratio)*wi/2 for wi in w])
            mass=f.transpose()*outer*f
            vals=spectrum_small(mass);assert vals[0]>0 and vals[-1]<1
            # Exact E b-orthogonality implies approximate L2 overlap <=zeta.
            zeta=(aa['theta']*bb['theta']).sqrt()/17
            error2=bb['eta']**2+(aa['eta']+zeta+(1-s2).sqrt()*bb['eta'])**2/s2
            assert error2<1
            distance=(2*error2/(1+(1-error2).sqrt())).sqrt().upper()
            assert vals[0].sqrt()>distance,(key,'positive mass not yet enclosed',vals[0],distance)
            loewner_lower=(1-distance/vals[0].sqrt())**2
            loewner_upper=(1+distance/vals[0].sqrt())**2
            eig=[]
            for val in vals:
                lo=(val.sqrt()-distance)**2;hi=(val.sqrt()+distance)**2
                assert lo>0
                eig.append({'lower_exact':exact(lo),'upper_exact':str(min(Q(1),Q(exact(hi,False))))})
            perturb=(2*vals[-1].sqrt()*distance+distance**2).upper()
            true_matrix=arb_mat([[mass[i,j]+arb(0,perturb) for j in range(d)] for i in range(d)])
            mlo=rat(eig[0]['lower_exact']);mhi=rat(eig[0]['upper_exact'])
            geom=(1-mlo).sqrt().upper()
            qcs=(aa['theta']/(aa['theta']+17)*bb['theta']/(bb['theta']+17)).sqrt().upper()
            results[key]={'dimension':d,'quadrature_nodes':count,'ratio_A_over_B':iv(ratio),
                'trial_overlap':matrix_iv(m),'overlap_singular_squared_lower_exact':exact(s2),
                'auxiliary_kernel_basis_in_new_trial':matrix_iv(f),'auxiliary_outer_mass_matrix':matrix_iv(mass),
                'auxiliary_outer_mass_eigenvalues':[iv(x) for x in vals],
                'old_projector_error_upper_exact':exact(aa['eta'],False),'new_projector_error_upper_exact':exact(bb['eta'],False),
                'exact_E_L2_overlap_defect_upper_exact':exact(zeta,False),
                'E_to_auxiliary_projector_error_squared_upper_exact':exact(error2,False),
                'polar_basis_distance_upper_exact':exact(distance,False),
                'canonical_E_matrix_basis':'L2 polar projection of the defined auxiliary kernel basis onto canonical E',
                'canonical_E_outer_mass_matrix_entry_intervals':matrix_iv(true_matrix),
                'matrix_perturbation_norm_upper_exact':exact(perturb,False),
                'loewner_lower_factor_exact':exact(loewner_lower),'loewner_upper_factor_exact':exact(loewner_upper,False),
                'canonical_E_outer_mass_eigenvalues':eig,
                'm_out_lower_exact':eig[0]['lower_exact'],'m_out_upper_exact':eig[0]['upper_exact'],
                'geometric_pulled_back_b_coupling_upper_exact':exact(geom,False),
                'known_positive_terminal_q_CS_pulled_back_b_coupling_upper_exact':exact(qcs,False),
                'seconds':time.time()-start}
            print(key,'m_out in',[float(mlo),float(mhi)],'E distance <=',float(distance),flush=True)
    out={'status':'CERTIFIED_CANONICAL_EXTENSION_OUTER_MASS_ENCLOSURES',
         'source_commit':PIN,'precision_bits':a.bits,'extra_quadrature_nodes':a.extra_nodes,
         'source_sha256':sources,'transport_receipt_sha256':hashlib.sha256(a.transport.read_bytes()).hexdigest(),
         'a8_gap_receipt_sha256':hashlib.sha256(a.a8_gap.read_bytes()).hexdigest(),
         'vectors_sha256':hashlib.sha256(a.vectors.read_bytes()).hexdigest(),
         'trials':trials,'results':results,'new_true_eigenvectors_computed':False,
         'full_high_response_paid':True,'relative_kappa_computed':False}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('ALL CANONICAL OUTER MASS ENCLOSURES COMPLETE',flush=True)

if __name__=='__main__':main()
