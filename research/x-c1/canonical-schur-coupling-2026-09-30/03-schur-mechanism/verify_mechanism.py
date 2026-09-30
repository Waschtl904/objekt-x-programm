"""Exact rational audit of directional Schur and spectral-mixture witnesses.

No large solve is performed. Prior directed intervals and their analytic
certificates are inputs. See MECHANISM.md for all general arguments.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse, hashlib, json, subprocess

PIN = '8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b'
OUTER = 'research/x-c1/renewable-low-schur-spectral-2026-09-29/07-canonical-extension-outer-mass/primary.json'

def pt(x): return F(x), F(x)
def iv(x):
    a,b=map(F,x); assert a<=b; return a,b
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[1],-x[0]
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    z=[a*b for a in x for b in y]; return min(z),max(z)
def div(x,y):
    assert y[0]*y[1]>0
    return mul(x,(1/y[1],1/y[0]))
def ab(x): return max(abs(x[0]),abs(x[1]))
def sq(x):
    return (F(0) if x[0]<=0<=x[1] else min(abs(x[0]),abs(x[1]))**2, ab(x)**2)
def total(xs):
    s=pt(0)
    for x in xs: s=add(s,x)
    return s
def root(x,up=False):
    assert x>=0
    den=10**100; n=isqrt(x.numerator*den**2//x.denominator)
    if up and F(n*n,den**2)<x: n+=1
    y=F(n,den)
    assert y*y>=x if up else y*y<=x
    return y
def mat(a): return [[iv(x) for x in row] for row in a]
def tr(a): return list(map(list,zip(*a)))
def mm(a,b): return [[total(mul(x,y) for x,y in zip(u,v)) for v in tr(b)] for u in a]
def quad(a,x): return mm(mm(tr(x),a),x)[0][0]
def frob(a): return total(sq(x) for row in a for x in row)
def inv(a):
    if len(a)==1:
        assert a[0][0][0]>0
        return [[div(pt(1),a[0][0])]]
    assert len(a)==2 and a[0][0][0]>0
    det=sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0])); assert det[0]>0
    return [[div(a[1][1],det),div(neg(a[0][1]),det)],
            [div(neg(a[1][0]),det),div(a[0][0],det)]]
def gmin(a): return min(a[i][i][0]-sum(ab(x) for j,x in enumerate(row) if i!=j) for i,row in enumerate(a))
def gmax(a): return max(a[i][i][1]+sum(ab(x) for j,x in enumerate(row) if i!=j) for i,row in enumerate(a))

def rounded(x,up=False,digits=6):
    assert x>0
    e=0;y=x
    while y<1: y*=10;e-=1
    while y>=10: y/=10;e+=1
    s=10**(digits-1);z=y*s;k=z.numerator//z.denominator
    if up and F(k)<z:k+=1
    r=F(k,s)*F(10)**e
    assert r>=x if up else r<=x
    return f'{k//s}.{k%s:0{digits-1}d}e{e:+d}',r
def bound(x,up=False):
    display,r=rounded(x,up)
    return {'exact':str(x),'outward':display,'outward_exact':str(r),'side':'upper' if up else 'lower'}

def audit_case(r,source,key,prior):
    dim=r['dimension']; j=1 if key=='A8->A9-odd' else 0
    old,new=key.rsplit('-',1)[0].split('->');par=key.rsplit('-',1)[1]
    a,b=source['trials'][old+'-'+par],source['trials'][new+'-'+par]
    n=mat(r['canonical_N']);g=mat(r['canonical_basis_L2_Gram'])
    lm=mat(r['energy_Loewner_lower_in_raw_basis']);lp=mat(r['energy_Loewner_upper_in_raw_basis'])
    en=mat(r['trial_energy_on_N']);lmi=inv(lm);lpi=inv(lp)
    assert gmin(g)>0 and gmin(lm)>0
    nu=F(b['physical_complement_gap_lower_exact']);nua=F(a['physical_complement_gap_lower_exact'])
    theta=F(b['physical_trial_max_Rayleigh_upper_exact'])
    q=F(b['physical_Ritz_matrix'][j][j][1]);qa=F(a['physical_Ritz_matrix'][j][j][1])
    assert q>0 and qa>0
    x=[[pt(int(i==0))] for i in range(dim)]
    norm=quad(g,x);ll=quad(lm,x)[0];lh=quad(lp,x)[1]
    energy_lo=ll/norm[1];energy_hi=lh/norm[0]
    projection_error=root(q*en[0][0][1],True)/nu
    overlap=sub(n[j][0],(-projection_error,projection_error))
    assert overlap[0]*overlap[1]>0,('probe overlap crosses zero',key,j)
    raw_alpha=min(abs(overlap[0]),abs(overlap[1]))
    alpha2=raw_alpha**2/norm[1]
    alpha=root(alpha2)
    assert alpha>0 and alpha2<=1
    zprobe=alpha2/q
    gx=mm(g,x)
    denhi=lh+34*norm[1]+289*quad(lmi,gx)[1]
    beta_probe=(ll+34*norm[0]+289*raw_alpha**2/q)/denhi
    assert beta_probe>1
    flo=mm(mat(r['trial_resolvent_lower_factor']),n)
    fhi=mm(mat(r['trial_resolvent_upper_factor']),n)
    directional=[]
    for k in range(dim):
        y=[[pt(int(i==k))] for i in range(dim)]
        gy=mm(g,y);gn=quad(g,y);l=quad(lm,y)[0];u=quad(lp,y)[1]
        zl=max(gn[0]/theta,frob(mm(flo,y))[0]-quad(en,y)[1]/nu**2)
        zh=frob(mm(fhi,y))[1]
        dh=u+34*gn[1]+289*quad(lmi,gy)[1]
        dl=l+34*gn[0]+289*quad(lpi,gy)[0]
        assert 0<dl<=dh and 0<zl<=zh
        directional.append({'beta_lower':(l+34*gn[0]+289*zl)/dh,
                            'beta_upper':(u+34*gn[1]+289*zh)/dl})
    deep=4*q/alpha2;high=energy_lo/2
    assert 0<deep<high<theta
    old_overlap=root(qa*energy_hi,True)/17+root(qa/nua,True)
    matched=iv(source['results'][key]['trial_overlap'][j][j])
    assert matched[0]>0
    old_separation=max(F(0),alpha-old_overlap)
    # True maximizing inverse-response vector, irrespective of its coordinates.
    ell=gmin(lm)/gmax(g);theta_e=min(theta,gmax(lp)/gmin(g))
    beta_prior=1/F(prior['display_outward'][1])
    zstar=beta_prior/theta_e
    max_deep=2/zstar;max_high=ell/2
    assert max_deep<max_high
    return {
      'dimension':dim,'probe_index_one_based':j+1,
      'energy_lower':energy_lo,'energy_upper':energy_hi,
      'probe_energy_upper':q,'old_probe_energy_upper':qa,
      'probe_overlap_lower':alpha,'probe_overlap_squared_lower':alpha2,
      'overlap_projection_error_upper':projection_error,
      'inverse_moment_forced_lower':zprobe,'beta_probe_lower':beta_probe,
      'deep_band_cutoff_upper':deep,'deep_band_L2_mass_lower':alpha2/4,
      'high_band_cutoff_lower':high,'high_band_L2_mass_lower':energy_lo/(2*theta-energy_lo),
      'band_separation_lower':high/deep,
      'old_transported_trial_overlap_upper':old_overlap,
      'new_minus_old_overlap_lower':old_separation,
      'matched_trial_overlap_lower':matched[0],
      'maximizer_inverse_moment_lower':zstar,
      'maximizer_deep_cutoff_upper':max_deep,
      'maximizer_high_cutoff_lower':max_high,
      'maximizer_band_separation_lower':max_high/max_deep,
      'directional_axes':directional}

def formula_checks():
    # An invariant two-dimensional E: beta=1, but a mixed scalar direction
    # has a large arithmetic/harmonic product. This catches a false shortcut.
    eps=F(1,10**12);avg=(1+eps)/2;harm=(1+1/eps)/2
    assert avg*harm>10**11
    for l in [eps,F(1)]:
        z=1/l;assert (l+34+289*z)/(l+17)**2*l==1
    # Noncommuting positive moments, exact trace and determinant equivalence
    # between R B^-1 L B^-1 and (B L^-1 B)^-1 R.
    for shift in [F(3),F(17),F(23)]:
        l=[[pt(2),pt(F(1,3))],[pt(F(1,3)),pt(1)]]
        z=[[pt(7),pt(F(-2,3))],[pt(F(-2,3)),pt(5)]]
        b=[[add(l[i][j],pt(shift if i==j else 0)) for j in range(2)] for i in range(2)]
        r=[[add(add(l[i][j],pt(2*shift if i==j else 0)),mul(pt(shift**2),z[i][j])) for j in range(2)] for i in range(2)]
        m=mm(mm(b,inv(l)),b);x=mm(inv(m),r);y=mm(mm(mm(r,inv(b)),l),inv(b))
        assert add(x[0][0],x[1][1])==add(y[0][0],y[1][1])
        assert sub(mul(x[0][0],x[1][1]),mul(x[0][1],x[1][0]))==sub(mul(y[0][0],y[1][1]),mul(y[0][1],y[1][0]))
    return {'invariant_E_counterexample':True,'noncommuting_exact_pencil_checks':3}

def entry_relaxations(primary,cross,prior):
    cases={}
    for par,ls,z1,zlow,zhigh in [
        ('even',[F('6.6e-10'),F('3.2e-6')],F('1e22'),F('1e9'),F('1e21')),
        ('odd',[F('4.5e-8'),F('1.55e-4')],F('1e20'),F('1e7'),F('1e20'))]:
        key='A9->A11-'+par;items=[]
        for z2 in [zlow,zhigh]:
            zs=[z1,z2]
            for run in [primary,cross]:
                r=run['results'][key]
                for field,diag in [('physical_energy_entries',ls),('physical_inverse_energy_entries',zs)]:
                    m=mat(r[field])
                    for i in range(2):
                        for j in range(2):
                            value=diag[i] if i==j else F(0)
                            assert m[i][j][0]<=value<=m[i][j][1]
                assert min(ls)>=F(r['physical_energy_uniform_lower_exact'])
                assert max(ls)<=F(r['physical_energy_uniform_upper_exact'])
                assert min(zs)>=F(r['physical_inverse_energy_uniform_lower_exact'])
                assert max(zs)<=F(r['physical_inverse_energy_uniform_upper_exact'])
            for i in range(2):
                lo,hi=map(F,prior['results'][key]['physical_inverse_energy_diagonal_intervals'][i])
                assert lo<=zs[i]<=hi and zs[i]>=1/ls[i]
            betas=[l*(l+34+289*z)/(l+17)**2 for l,z in zip(ls,zs)]
            priorlo,priorhi=map(F,prior['results'][key]['display_outward'])
            assert priorlo<=1/max(betas)<=priorhi
            items.append({'L_diagonal':list(map(str,ls)),'Z_diagonal':list(map(str,zs)),
                          'beta_diagonal':list(map(str,betas)),
                          'maximizing_axis_one_based':1+int(betas[1]>betas[0])})
        assert [v['maximizing_axis_one_based'] for v in items]==[1,2]
        cases[key]=items
    return {'scope':'ENTRYWISE_RELAXATION_ONLY; not a realization of the full canonical source constraints',
            'cases':cases}

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
    p.add_argument('--repo',type=Path);a=p.parse_args();base=Path(__file__).resolve().parent
    bindings=json.loads((base/'input_bindings.json').read_bytes())
    data={}
    for name,h in bindings['sha256'].items():
        raw=(base/'inputs'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==h
        data[name]=json.loads(raw)
    primary=data['primary.json'];cross=data['crosscheck.json'];prior=data['prior_verification.json'];source=data['outer_primary.json']
    assert primary['source_commit']==cross['source_commit']==prior['source_commit']==PIN
    assert primary['precision_bits']==1024 and cross['precision_bits']==1280
    assert primary['source_sha256']==cross['source_sha256']==prior['source_sha256']
    assert len(primary['source_sha256'])==25
    assert set(primary['results'])==set(cross['results'])==set(prior['results'])=={
        'A8->A9-even','A8->A9-odd','A9->A11-even','A9->A11-odd'}
    assert primary['source_sha256'][OUTER]==bindings['sha256']['outer_primary.json']
    assert prior['primary_sha256']==bindings['sha256']['primary.json']
    assert prior['crosscheck_sha256']==bindings['sha256']['crosscheck.json']
    source_check={'mode':'bound_package_inputs_only','count':25}
    if a.repo:
        repo=a.repo.resolve();git=['git','-c','safe.directory='+repo.as_posix(),'-C',str(repo)]
        assert subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()==PIN
        for rel,h in primary['source_sha256'].items():
            raw=(repo/rel).read_bytes();assert hashlib.sha256(raw).hexdigest()==h
            assert raw==subprocess.check_output(git+['show',PIN+':'+rel])
        source_check={'mode':'all_25_working_files_equal_pinned_git_blobs','count':25}
    results={}
    for key in primary['results']:
        runs=[audit_case(d['results'][key],source,key,prior['results'][key]) for d in [primary,cross]]
        merged={'dimension':runs[0]['dimension'],'probe_index_one_based':runs[0]['probe_index_one_based']}
        for name in runs[0]:
            if name in merged or name=='directional_axes':continue
            upper=name.endswith('_upper');value=(max if upper else min)(r[name] for r in runs)
            assert value>0,(key,name)
            merged[name]=bound(value,upper)
        merged['directional_axes']=[]
        for i in range(merged['dimension']):
            merged['directional_axes'].append({
                'beta_lower':bound(min(r['directional_axes'][i]['beta_lower'] for r in runs)),
                'beta_upper':bound(max(r['directional_axes'][i]['beta_upper'] for r in runs),True)})
        results[key]=merged
        print(key,'probe',merged['probe_index_one_based'],'beta >=',merged['beta_probe_lower']['outward'],
              'bands <=',merged['deep_band_cutoff_upper']['outward'],'and >=',merged['high_band_cutoff_lower']['outward'],flush=True)
    out={'status':'RATIONAL_SCHUR_MECHANISM_AUDIT_PASS','research_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN',
         'source_commit':PIN,'input_sha256':bindings['sha256'],'source_check':source_check,
         'results':results,'formula_checks':formula_checks(),'entrywise_relaxation_examples':entry_relaxations(primary,cross,prior),
         'deep_band_inverse_energy_fraction_lower':'3/4','high_band_energy_fraction_lower':'1/2',
         'maximizer_band_fractions_lower':'1/2 inverse energy and 1/2 energy',
         'maximizer_direction_isolated':False,'individual_true_eigenvectors_identified':False,
         'large_resolvent_solves_rerun':False,'uses_existing_new_terminal_positivity':True,
         'forward_renewal_proved':False,'scope':'Directional witnesses and spectral-band consequences; the true 2D maximizer and eigenmode lineage remain unresolved.'}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('ALL FOUR DIRECTIONAL MECHANISM CHECKS PASS',flush=True)

if __name__=='__main__':main()
