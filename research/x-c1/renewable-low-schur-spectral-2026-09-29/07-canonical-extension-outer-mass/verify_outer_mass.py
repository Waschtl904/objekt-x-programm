"""Exact-rational audit of directed outer-mass data and canonical E bounds.

Standard library only. Recomputes all small-matrix, angle, mass and coupling
conclusions; polynomial integral enclosures remain the separate Arb input.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,io,json,shutil,subprocess,zipfile

PIN='d16ba43ebb20f2c61f43379fc65d7a9b9dba76de'
TRANSPORT_SHA='b5c8f81630711dbde81c3a2622507aa56ee835f19cae4691b3547dbb58db8cc4'
def sha(x):return hashlib.sha256(x).hexdigest()
def root(x,up=True,digits=18):
    assert x>=0;s=10**digits;k=isqrt(x.numerator*s*s//x.denominator)
    assert F(k*k,s*s)<=x<F((k+1)*(k+1),s*s)
    if up and F(k*k,s*s)<x:k+=1
    out=F(k,s);assert out*out>=x if up else out*out<=x
    return out
def archive(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        assert z.testzip() is None
        files={Path(n).name:z.read(n) for n in z.namelist() if not n.endswith('/')}
    for line in files['SHA256SUMS'].decode().splitlines():
        h,n=line.split('  ',1);assert sha(files[n])==h
    return files
def pair(x):
    l,h=map(F,x);assert l<=h;return l,h
def hull(x,y):
    a,b=pair(x),pair(y);assert max(a[0],b[0])<=min(a[1],b[1])
    return min(a[0],b[0]),max(a[1],b[1])
def matrix_hull(x,y):
    assert len(x)==len(y) and all(len(a)==len(b) for a,b in zip(x,y))
    return [[hull(a,b) for a,b in zip(u,v)] for u,v in zip(x,y)]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    z=[x*y for x in a for y in b];return min(z),max(z)
def isum(seq):
    v=(F(0),F(0))
    for x in seq:v=add(v,x)
    return v
def absup(x):return max(abs(x[0]),abs(x[1]))
def gram(m):return [[isum(mul(m[i][k],m[j][k]) for k in range(len(m[0]))) for j in range(len(m))] for i in range(len(m))]
def gupper(m):return max(m[i][i][1]+sum(absup(m[i][j]) for j in range(len(m)) if j!=i) for i in range(len(m)))
def glower(m):return min(m[i][i][0]-sum(absup(m[i][j]) for j in range(len(m)) if j!=i) for i in range(len(m)))
def small_spectrum(m):
    n=len(m);assert n in (1,2)
    c=[[(m[i][j][0]+m[i][j][1]+m[j][i][0]+m[j][i][1])/4 for j in range(n)] for i in range(n)]
    err=max(sum(max(abs(m[i][j][0]-c[i][j]),abs(m[i][j][1]-c[i][j])) for j in range(n)) for i in range(n))
    if n==1:return [(c[0][0]-err,c[0][0]+err)]
    center=(c[0][0]+c[1][1])/2;rad=((c[0][0]-c[1][1])/2)**2+c[0][1]**2
    lo,hi=root(rad,False,80),root(rad,True,80)
    return [(center-hi-err,center-lo+err),(center+lo-err,center+hi+err)]
def serial_matrix(m):return [[[str(l),str(h)] for l,h in row] for row in m]

def main():
    p=argparse.ArgumentParser()
    for k in ('repo','primary','crosscheck','transport-reference','a8-gap','a8-proposal','out'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();git=shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe'
    assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==PIN
    traw=a.transport_reference.read_bytes();assert sha(traw)==TRANSPORT_SHA
    tf=archive(traw);rf=archive(tf['rank_reference.zip']);archive(rf['A11_reference.zip'])
    transport=json.loads(tf['verification.json']);a8=json.loads(a.a8_gap.read_bytes())
    pdat=json.loads(a.primary.read_bytes());cdat=json.loads(a.crosscheck.read_bytes())
    assert {pdat['precision_bits'],cdat['precision_bits']}=={1024,1280}
    assert pdat['extra_quadrature_nodes']==0 and cdat['extra_quadrature_nodes']==8
    assert a8['status']=='CERTIFIED_A8_FULL_COMPLEMENT_GAPS'
    assert a8['proposal_sha256']==sha(a.a8_proposal.read_bytes())
    for data in (pdat,cdat):
        assert data['status']=='CERTIFIED_CANONICAL_EXTENSION_OUTER_MASS_ENCLOSURES'
        assert data['source_commit']==PIN
        assert data['transport_receipt_sha256']==sha(tf['verification.json'])
        assert data['a8_gap_receipt_sha256']==sha(a.a8_gap.read_bytes())
        assert data['vectors_sha256']==sha(rf['fixed_vectors.json'])
    assert pdat['source_sha256']==cdat['source_sha256']
    sources=pdat['source_sha256']|transport['bound_source_sha256']|a8['bound_source_sha256']
    for rel,h in sources.items():
        raw=(a.repo/rel).read_bytes();assert sha(raw)==h
        assert raw==subprocess.check_output([git,'show',PIN+':'+rel],cwd=a.repo)
    trials={}
    for key,pt in pdat['trials'].items():
        ct=cdat['trials'][key];s=matrix_hull(pt['physical_Ritz_matrix'],ct['physical_Ritz_matrix'])
        matrix_hull(pt['orthogonalizer'],ct['orthogonalizer'])
        theta=gupper(s);gap=F((a8 if key.startswith('A8-') else transport)['gaps'][key]['physical_complement_lower_exact'])
        eta=root(theta/gap);assert 0<theta<gap and eta<1
        assert pt['rank']==ct['rank']=={'A8':5,'A9':6,'A11':8}[key.split('-')[0]]
        trials[key]={'rank':pt['rank'],'theta_upper_exact':str(theta),'gap_lower_exact':str(gap),
                     'projector_norm_error_upper_exact':str(eta),'method':'energy and complete physical gap'}
    results={}
    for key,pr in pdat['results'].items():
        cr=cdat['results'][key];transition,parity=key.rsplit('-',1);first,last=transition.split('->')
        d=pr['dimension'];assert d==cr['dimension']==(1 if first=='A8' else 2)
        assert cr['quadrature_nodes']==pr['quadrature_nodes']+8
        m=matrix_hull(pr['trial_overlap'],cr['trial_overlap']);s2=glower(gram(m));assert 0<s2<1
        matrix_hull(pr['auxiliary_kernel_basis_in_new_trial'],cr['auxiliary_kernel_basis_in_new_trial'])
        mass=matrix_hull(pr['auxiliary_outer_mass_matrix'],cr['auxiliary_outer_mass_matrix'])
        ev=small_spectrum(mass);assert 0<ev[0][0]<=ev[-1][1]<1
        ta,tb=trials[first+'-'+parity],trials[last+'-'+parity]
        ea,eb=F(ta['projector_norm_error_upper_exact']),F(tb['projector_norm_error_upper_exact'])
        th_a,th_b=F(ta['theta_upper_exact']),F(tb['theta_upper_exact'])
        zeta=root(th_a*th_b)/17
        error2=eb*eb+(ea+zeta+root(1-s2)*eb)**2/s2;assert error2<1
        distance=root(2*error2/(1+root(1-error2,False)))
        mfroot=root(ev[0][0],False);assert mfroot>distance
        lc=(1-distance/mfroot)**2;uc=(1+distance/mfroot)**2
        eig=[]
        for lo,hi in ev:
            low=(root(lo,False)-distance)**2;high=min(F(1),(root(hi)+distance)**2)
            assert 0<low<high<=1
            eig.append({'lower_exact':str(low),'upper_exact':str(high)})
        perturb=2*root(ev[-1][1])*distance+distance*distance
        actual=[[(l-perturb,h+perturb) for l,h in row] for row in mass]
        minmass=F(eig[0]['lower_exact']);maxminmass=F(eig[0]['upper_exact'])
        geometric=root(1-minmass,True,12)
        alpha_a=th_a/(th_a+17);alpha_b=th_b/(th_b+17)
        energy_c=root(alpha_a*alpha_b,True,18)
        sigma=F(transport['transports'][key]['projected_transport_min_singular_lower_exact'])
        results[key]={'dimension':d,'auxiliary_outer_mass_matrix':serial_matrix(mass),
            'auxiliary_outer_mass_eigenvalues':[[str(x),str(y)] for x,y in ev],
            'overlap_singular_squared_lower_exact':str(s2),'L2_overlap_defect_upper_exact':str(zeta),
            'E_projector_error_squared_upper_exact':str(error2),'polar_basis_distance_upper_exact':str(distance),
            'canonical_E_basis':'L2 polar projection of the certified auxiliary kernel basis onto canonical E',
            'canonical_E_outer_mass_matrix_entry_intervals':serial_matrix(actual),
            'matrix_error_norm_upper_exact':str(perturb),
            'loewner_lower_factor_exact':str(lc),'loewner_upper_factor_exact':str(uc),
            'canonical_E_outer_mass_eigenvalues':eig,
            'm_out_lower_exact':str(minmass),'m_out_upper_exact':str(maxminmass),
            'geometric_pulled_back_b_coupling_upper_exact':str(geometric),
            'geometric_L2_coupling_upper_exact':str(17*geometric),
            'geometric_coupling_on_transported_b_space_upper_exact':str(geometric/sigma),
            'known_positive_terminal_energy_CS_pulled_back_b_coupling_upper_exact':str(energy_c)}
        print(key,'CERTIFIED m_out in',[float(minmass),float(maxminmass)],
              'C geometric b <=',float(geometric),'known q-CS <=',float(energy_c),flush=True)
    out={'status':'RATIONAL_CANONICAL_OUTER_MASS_AND_COUPLING_CHECKS_PASS','source_commit':PIN,
        'source_sha256':sources,'primary_sha256':sha(a.primary.read_bytes()),'crosscheck_sha256':sha(a.crosscheck.read_bytes()),
        'transport_reference_sha256':sha(traw),'a8_gap_sha256':sha(a.a8_gap.read_bytes()),
        'a8_gap_proposal_sha256':sha(a.a8_proposal.read_bytes()),
        'scope':'Canonical E enclosures derived from auxiliary polynomial spaces by full physical spectral gap estimates. Analytic assumptions and directed integral data remain inputs.',
        'trials':trials,'results':results,'relative_kappa_computed':False}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('ALL RATIONAL OUTER MASS AND COUPLING CHECKS PASS',flush=True)

if __name__=='__main__':main()
