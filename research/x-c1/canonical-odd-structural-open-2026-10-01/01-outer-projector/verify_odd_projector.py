"""Outer-family projector obstruction; explicitly not a physical countermodel."""
from pathlib import Path, PurePosixPath
from fractions import Fraction as F
import argparse, hashlib, importlib, io, json, os, subprocess, sys, tempfile, zipfile
import completion_math as e

ARCHIVE='Gemeinsames-Schurdefekt-Proportionalitaetsgate-2026-09-30.zip'
ARCHIVE_SHA='4ed89ec928ba1573c6f295bf4038588568c1e5b9f4fdff69ee8e318eb4733c5b'
ROOT='canonical-schur-defect-2026-09-30'
KEY='A9->A11-odd'

def unpack(raw,dest):
    assert hashlib.sha256(raw).hexdigest()==ARCHIVE_SHA,'upstream archive hash mismatch'
    files={}
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        for info in z.infolist():
            p=PurePosixPath(info.filename)
            assert not p.is_absolute() and '..' not in p.parts and '\\' not in info.filename
            assert p.parts[0]==ROOT and len(p.parts)>1 and not info.is_dir()
            name='/'.join(p.parts[1:]);assert name not in files
            files[name]=z.read(info)
    manifest=dict((name,sha) for sha,name in (line.split('  ',1) for line in files['SHA256SUMS'].decode().splitlines()))
    assert set(manifest)==set(files)-{'SHA256SUMS'}
    for name,sha in manifest.items():assert hashlib.sha256(files[name]).hexdigest()==sha
    for name,raw in files.items():
        target=dest/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
    return files

def orders(v,point,lower=None,upper=None):
    a=e.intervals(v,point);result={}
    if lower is not None:
        piv=e.positive_interval(v,v.submat(a,v.matrix(lower)))
        result['lower_order_min_pivot']=min(x[0] for x in piv)
    if upper is not None:
        piv=e.positive_interval(v,v.submat(v.matrix(upper),a))
        result['upper_order_min_pivot']=min(x[0] for x in piv)
    return result

def check_measure(v,model,r,trial,bounds):
    s,t,lp,gp,zp,h=(model[k] for k in ['S','T','LP','GP','ZP','H']);nu=model['nu']
    assert nu==F(trial['physical_complement_gap_lower_exact'])
    assert e.contain(s,trial['physical_Ritz_matrix'])
    checks={}
    for name,a in [('S',s),('T',t),('LP',lp),('GP',gp),('H',h)]:
        checks[name+'_min_pivot']=min(p[0] for p in e.positive_interval(v,e.intervals(v,a)))
    checks['resolvent_orders']=orders(v,t,r['trial_resolvent_lower'],r['trial_resolvent_upper'])
    theta=F(trial['physical_trial_max_Rayleigh_upper_exact'])
    e.positive_interval(v,e.intervals(v,e.sub(e.scale(gp,theta),lp)))
    assert theta<F(17,9999)<nu
    eta=list(map(F,bounds['eta']))
    assert all(0<h[i][i]<=eta[i]**2 for i in range(len(h)))
    for a,k in [(gp,'projected_Gram'),(lp,'projected_energy'),(zp,'projected_inverse')]:assert e.contain(a,bounds[k]),k
    assert e.sub(s,lp)==e.scale(h,nu) and e.sub(t,zp)==e.scale(h,1/nu)
    assert zp==e.mm(e.mm(gp,e.inv(lp)),gp)
    checks['single_measure_with_high_atom']=True
    checks['maximum_mass_bound_ratio']=max(h[i][i]/eta[i]**2 for i in range(len(h)))
    return checks

def check_pencil(v,p,r,nr,model):
    y,n,g,l,z,m,rr=(p[k] for k in ['Y','N','G','L','Z','M','R'])
    assert e.contain(y,nr['Y']) and e.contain(n,nr['N'])
    assert e.mm(y,n)==[[F(0),F(0)] for _ in range(6)]
    for a,k in [(g,'G0'),(l,'L0'),(z,'Z0')]:assert e.contain(a,nr['compressed_moment_entries'][k]),k
    checks={'energy_orders':orders(v,l,r['energy_Loewner_lower_in_raw_basis'],r['energy_Loewner_upper_in_raw_basis'])}
    en=e.compressed(n,model['S']);nu=model['nu']
    e.positive_interval(v,e.intervals(v,e.sub(en,l)))
    e.positive_interval(v,e.intervals(v,e.sub(e.scale(g,F(r['physical_energy_uniform_upper_exact'])),l)))
    e.positive_interval(v,e.intervals(v,p['W']))
    lo=v.submat(v.mm(v.mm(v.tr(e.intervals(v,n)),v.matrix(r['trial_resolvent_lower'])),e.intervals(v,n)),v.scale(e.intervals(v,en),1/nu**2))
    hi=v.mm(v.mm(v.tr(e.intervals(v,n)),v.matrix(r['trial_resolvent_upper'])),e.intervals(v,n))
    e.positive_interval(v,v.submat(e.intervals(v,z),lo));e.positive_interval(v,v.submat(hi,e.intervals(v,z)))
    # These two stored boxes enclose N-dependent bound matrices. They are
    # not fixed Loewner matrices that must all lie below/above this Z.
    for current,field in [(lo,'inverse_lower_family_in_raw_basis'),(hi,'inverse_upper_family_in_raw_basis')]:
        family=v.matrix(r[field])
        assert all(family[i][j][0]<=current[i][j][0]<=current[i][j][1]<=family[i][j][1] for i in range(2) for j in range(2)),field
    checks['inherited_inverse_bound_matrices_in_their_entry_families']=True
    checks['all_stated_outer_constraints']=True
    return checks

def projector(v,p):
    # T=M^-1 R has the same two generalized eigenvalues. Everything before
    # sqrt is exact rational, including cancellation in the discriminant.
    t=e.mm(e.inv(p['M']),p['R']);tr=t[0][0]+t[1][1]
    det=t[0][0]*t[1][1]-t[0][1]*t[1][0];delta=tr*tr-4*det
    assert det>0 and delta>0
    gap=(v.sqrt_lower(delta),v.sqrt_upper(delta))
    beta_plus=v.div(v.add(v.point(tr),gap),v.point(2))
    beta_minus=v.div(v.point(det),beta_plus)
    k=v.submat(e.intervals(v,t),v.scale(v.eye(2),0))
    for j in range(2):k[j][j]=v.sub(k[j][j],beta_minus)
    # K=(beta_plus-beta_minus)*Pi_plus. Scale cancels in the physical projector.
    g=e.intervals(v,p['G']);dg=v.determinant(g);rootg=(v.sqrt_lower(g[0][0][0]),v.sqrt_upper(g[0][0][1]))
    j=[[rootg,v.div(g[0][1],rootg)],[v.point(0),(v.sqrt_lower(v.div(dg,g[0][0])[0]),v.sqrt_upper(v.div(dg,g[0][0])[1]))]]
    jk=v.mm(j,k);cov=v.mm(jk,v.tr(jk));den=v.trace(cov);assert den[0]>0
    pp=[[v.div(x,den) for x in row] for row in cov]
    result={'beta_minus':beta_minus,'beta_plus':beta_plus,'beta_gap':gap,'physical_projector':pp,
            'projector_trace_denominator':den,'projector_display':[[v.display(x) for x in row] for row in pp]}
    return result,k

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    base=Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(prefix='odd-projector-') as tmp:
        folder=Path(tmp)/ROOT;files=unpack((base/'inputs'/ARCHIVE).read_bytes(),folder)
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        replay=Path(tmp)/'schur-replay.json'
        run=subprocess.run([sys.executable,'-B',str(folder/'verify_schur_defect.py'),'--out',str(replay)],env=env,check=True,capture_output=True,text=True)
        assert not run.stderr and replay.read_bytes()==files['verification.json']
        print('Both upstream rational certifiers replay byte-identically: PASS',flush=True)
        sys.path.insert(0,str(folder));schur=importlib.import_module('verify_schur_defect')
        depfiles=schur.checked_archive(files['inputs/'+schur.ARCHIVE]);dep=Path(tmp)/'discriminant'
        for name,raw in depfiles.items():
            target=dep/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
        sys.path.insert(0,str(dep));v=importlib.import_module('verify_joint_discriminant')
        primary=json.loads(depfiles['inputs/primary.json']);outer=json.loads(depfiles['inputs/outer_primary.json'])
        projected=json.loads(depfiles['inputs/projected_verification.json']);old=json.loads(depfiles['verification.json'])
        params_raw=(base/'parameters.json').read_bytes();params=json.loads(params_raw)
        r=primary['results'][KEY];nr=projected['runs']['primary.json']['results'][KEY]
        models={}
        for name,rkey in [('A9-odd','A8->A9-odd'),('A11-odd',KEY)]:
            models[name]=e.measure(primary['results'][rkey],outer['trials'][name])
        print('Exact common moment measures constructed for A9 and A11.',flush=True)
        center=e.midpoint(outer['results'][KEY]['trial_overlap']);n0=e.annihilator(center)
        f=e.midpoint(r['trial_resolvent_upper_factor']);h0=e.mm([f[0][:6]],e.inv([row[:6] for row in center]))[0]
        vertex=[[F(nr['Y'][i][j][1 if h0[i]*n0[j][1]>0 else 0]) for j in range(8)] for i in range(6)]
        t=F(params['root_parameter']);assert 0<t<1
        ys={'central':center,'rotated':e.add(e.scale(center,1-t),e.scale(vertex,t))}
        pencils={name:e.pencil(y,models['A11-odd']) for name,y in ys.items()}
        run_results={}
        for run_name in ['primary.json','crosscheck.json']:
            data=json.loads(depfiles['inputs/'+run_name]);rb=projected['runs'][run_name]
            measures={name:check_measure(v,models[name],data['results'][rkey],outer['trials'][name],rb['trials'][name]) for name,rkey in [('A9-odd','A8->A9-odd'),('A11-odd',KEY)]}
            tests={}
            for name,p in pencils.items():
                tests[name]=check_pencil(v,p,data['results'][KEY],rb['results'][KEY],models['A11-odd'])
            run_results[run_name]={'measures':measures,'pencils':tests}
            print(run_name,'all explicitly listed outer-family constraints: PASS',flush=True)
        outputs={};vectors={}
        for name,p in pencils.items():
            result,k=projector(v,p);outputs[name]=result
            for run_name in run_results:
                inherited=old['results'][run_name][KEY]
                assert result['beta_gap'][0]>=F(inherited['gap_lower'])
                assert result['beta_minus'][1]<=F(inherited['beta_minus_interval'][1])
                assert result['beta_plus'][0]>=F(inherited['beta_plus_interval'][0])
                assert result['beta_plus'][1]<=F(inherited['beta_plus_interval'][1])
            col=1 if name=='central' else 0
            vectors[name]=v.mm(e.intervals(v,p['N']),[[row[col]] for row in k])
            print(name,'P11',v.display(result['physical_projector'][0][0]),'P22',v.display(result['physical_projector'][1][1]),flush=True)
        gp=e.intervals(v,models['A11-odd']['GP']);u=vectors['central'];w=vectors['rotated']
        uv=v.mm(v.mm(v.tr(u),gp),w)[0][0]
        uu=v.mm(v.mm(v.tr(u),gp),u)[0][0];ww=v.mm(v.mm(v.tr(w),gp),w)[0][0]
        assert uu[0]>0 and ww[0]>0
        cos2=v.div(v.square(uv),v.mul(uu,ww))[1];assert 0<=cos2<1
        cos_upper=v.sqrt_upper(cos2);sin_lower=v.sqrt_lower(1-cos2)
        angle_lower=F(90)-v.angle_degrees(v.point(cos_upper/sin_lower))[1]
        # Necessary physical cross-Gram condition, using enlarged diagonal blocks.
        au=v.addmat(v.eye(6),v.scale(v.matrix(outer['trials']['A9-odd']['physical_Ritz_matrix']),F(1,17)))
        bu=v.addmat(v.eye(8),v.scale(v.matrix(outer['trials']['A11-odd']['physical_Ritz_matrix']),F(1,17)))
        y=e.intervals(v,ys['rotated'])
        defect=v.submat(au,v.mm(v.mm(y,v.inverse(bu,True)),v.tr(y)))
        assert defect[5][5][1]<0
        print('Physical angle between the two upper modes >=',v.sci(angle_lower),'degrees.',flush=True)
        print('Rotated example violates necessary cross b-Gram: diagonal 6',v.display(defect[5][5]),flush=True)
        out={'status':'OUTER_FAMILY_PROJECTOR_OBSTRUCTION_AND_MISSING_CROSS_GRAM_CERTIFIED',
             'research_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN',
             'source_commit':old['source_commit'],'integration_base':old['integration_base'],
             'upstream_archive_sha256':ARCHIVE_SHA,'upstream_byte_exact_replay':True,
             'parameters_sha256':hashlib.sha256(params_raw).hexdigest(),'results':run_results,
             'projectors':outputs,'physical_comparison':{'cosine_squared_upper':cos2,'projector_distance_lower':sin_lower,'angle_degrees_lower':angle_lower},
             'rotated_cross_gram_diagonal_6':defect[5][5],
             'both_outer_examples_have_simple_upper_eigenvalue':True,
             'examples_realized_by_one_moment_measure_per_chamber':True,
             'common_physical_transport_realization_claimed':False,
             'actual_odd_projector_localized':False,'tight_common_cross_gram_family_decided':False,
             'large_operator_solves_rerun':False,'global_result_proved':False}
        args.out.write_text(json.dumps(v.rational(out),indent=2)+'\n',encoding='utf-8',newline='\n')
    print('OUTER PROJECTOR OBSTRUCTION CERTIFIED; ACTUAL ODD LOCALIZATION REMAINS OPEN.',flush=True)

if __name__=='__main__':main()
