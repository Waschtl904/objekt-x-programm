"""Joint Gram examples and a stricter inherited transport-moment exclusion."""
from pathlib import Path,PurePosixPath
from fractions import Fraction as F
import argparse,hashlib,importlib,io,json,os,subprocess,sys,tempfile,zipfile
import completion_math as e
import transport_math as tm

BASE=Path(__file__).resolve().parent
ARCHIVE='Ungerade-Extremalprojektoren-2026-09-30.zip'
SHA='0c7c99b21f3b77b31862cdc9cae952a7ecd76abe8bc7a2e73df3bbe14980573b'
ROOT='canonical-odd-projector-2026-09-30'
KEY='A9->A11-odd'

def unpack(raw,dest):
    assert hashlib.sha256(raw).hexdigest()==SHA,'upstream archive hash mismatch'
    files={}
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        for info in z.infolist():
            p=PurePosixPath(info.filename)
            assert not p.is_absolute() and '..' not in p.parts and '\\' not in info.filename
            assert p.parts[0]==ROOT and len(p.parts)>1 and not info.is_dir()
            name='/'.join(p.parts[1:]);assert name not in files;files[name]=z.read(info)
    entries={n:h for h,n in (line.split('  ',1) for line in files['SHA256SUMS'].decode().splitlines())}
    assert set(entries)==set(files)-{'SHA256SUMS'}
    for name,h in entries.items():assert hashlib.sha256(files[name]).hexdigest()==h
    for name,raw in files.items():
        target=dest/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
    return files

def dependencies(temp,replay):
    olddir=temp/'odd';files=unpack((BASE/'inputs'/ARCHIVE).read_bytes(),olddir)
    assert (BASE/'completion_math.py').read_bytes()==files['completion_math.py']
    if replay:
        output=temp/'odd-replay.json'
        run=subprocess.run([sys.executable,'-B',str(olddir/'verify_odd_projector.py'),'--out',str(output)],
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,check=True)
        assert not run.stderr and output.read_bytes()==files['verification.json']
        print('Upstream odd, Schur-defect and discriminant replays: byte-identical PASS',flush=True)
    sys.path.insert(0,str(olddir));old=importlib.import_module('verify_odd_projector')
    schurdir=temp/'schur';sf=old.unpack(files['inputs/'+old.ARCHIVE],schurdir)
    sys.path.insert(0,str(schurdir));schur=importlib.import_module('verify_schur_defect')
    df=schur.checked_archive(sf['inputs/'+schur.ARCHIVE]);dep=temp/'discriminant'
    for name,raw in df.items():
        target=dep/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
    sys.path.insert(0,str(dep));v=importlib.import_module('verify_joint_discriminant')
    return old,v,df,dep

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    paramsraw=(BASE/'parameters.json').read_bytes();params=json.loads(paramsraw)
    bindingraw=(BASE/'source_bindings.json').read_bytes();bindings=json.loads(bindingraw)
    for item in bindings['repository_inputs']:
        assert hashlib.sha256((BASE/'inputs'/item['input']).read_bytes()).hexdigest()==item['sha256']
    assert bindings['upstream_archive_sha256']==SHA
    with tempfile.TemporaryDirectory(prefix='transport-moments-') as tempname:
        old,v,df,_=dependencies(Path(tempname),True)
        data=json.loads(df['inputs/primary.json']);outer=json.loads(df['inputs/outer_primary.json'])
        pr=json.loads(df['inputs/projected_verification.json']);inherited=json.loads(df['verification.json'])
        models={name:e.measure(data['results'][rk],outer['trials'][name]) for name,rk in [('A9-odd','A8->A9-odd'),('A11-odd',KEY)]}
        ga,la=models['A9-odd']['GP'],models['A9-odd']['LP']
        gb,lb=models['A11-odd']['GP'],models['A11-odd']['LP'];nu=models['A11-odd']['nu']
        o=e.midpoint(outer['results'][KEY]['trial_overlap'])
        opiv=e.positive_interval(v,e.intervals(v,e.sub(e.eye(6),e.mm(o,e.trans(o)))))
        rotation=tm.rotation_data(o,list(map(F,params['row_weights'])))
        points={'central':F(0),'rotated':F(params['root_parameter'])}
        pencils={};transport={};projectors={};vectors={}
        for name,t in points.items():
            q=tm.cayley(rotation,t);y=e.mm(e.mm(e.mm(ga,o),q),gb)
            pencil=e.pencil(y,models['A11-odd']);pencils[name]=pencil
            moments=tm.transported_moments(y,ga,la,gb,lb,nu);record={}
            for field in ('mass','energy','b_defect'):
                piv=e.positive_interval(v,e.intervals(v,moments[field]))
                record[field+'_min_pivot']=min(x[0] for x in piv)
            defect=moments['support_defect'];assert all(defect[i][i]>0 for i in range(6))
            w,value=tm.negative_vector(defect)
            value_interval=v.rounded(v.point(value));assert value_interval[1]<0
            record.update({'support_defect':e.intervals(v,defect),'all_support_diagonals_positive':True,
                'negative_vector':w,'negative_quadratic_form':value_interval,'negative_quadratic_display':v.display(value_interval),
                'necessary_transport_support_violated':True})
            transport[name]=record
            result,k=old.projector(v,pencil);projectors[name]=result
            col=1 if name=='central' else 0
            vectors[name]=v.mm(e.intervals(v,pencil['N']),[[row[col]] for row in k])
            print(name,'full b-Gram, mass and energy: positive; transport witness',v.display(value_interval),flush=True)
        runs={}
        for runname in ('primary.json','crosscheck.json'):
            src=json.loads(df['inputs/'+runname]);pb=pr['runs'][runname]
            measures={name:old.check_measure(v,models[name],src['results'][rk],outer['trials'][name],pb['trials'][name])
                for name,rk in [('A9-odd','A8->A9-odd'),('A11-odd',KEY)]}
            checks={}
            for name,pencil in pencils.items():
                checks[name]=old.check_pencil(v,pencil,src['results'][KEY],pb['results'][KEY],models['A11-odd'])
                previous=inherited['results'][runname][KEY];p=projectors[name]
                assert p['beta_gap'][0]>=F(previous['gap_lower'])
                assert p['beta_minus'][1]<=F(previous['beta_minus_interval'][1])
                assert F(previous['beta_plus_interval'][0])<=p['beta_plus'][0]<=p['beta_plus'][1]<=F(previous['beta_plus_interval'][1])
            runs[runname]={'measures':measures,'pencils':checks}
            print(runname,'both fixed joint Gram completions satisfy all inherited outer constraints: PASS',flush=True)
        u,w=vectors['central'],vectors['rotated'];metric=e.intervals(v,gb)
        uv=v.mm(v.mm(v.tr(u),metric),w)[0][0]
        uu=v.mm(v.mm(v.tr(u),metric),u)[0][0];ww=v.mm(v.mm(v.tr(w),metric),w)[0][0]
        assert uu[0]>0 and ww[0]>0
        cos2=v.div(v.square(uv),v.mul(uu,ww))[1];assert 0<=cos2<F(1,100)
        cs=v.sqrt_upper(cos2);sn=v.sqrt_lower(1-cos2)
        angle=F(90)-v.angle_degrees(v.point(cs/sn))[1]
        assert angle>F(89)
        print('Same-space physical angle >=',v.sci(angle),'degrees',flush=True)
        output={'status':'JOINT_GRAM_ALTERNATIVES_EXCLUDED_BY_TRANSPORTED_HIGH_SUPPORT',
            'research_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN','integration_base':bindings['integration_base'],
            'source_commit':inherited['source_commit'],'upstream_archive_sha256':SHA,'upstream_byte_exact_replay':True,
            'parameters_sha256':hashlib.sha256(paramsraw).hexdigest(),'source_bindings_sha256':hashlib.sha256(bindingraw).hexdigest(),
            'midpoint_overlap_contraction_min_pivot':min(p[0] for p in opiv),'results':runs,'projectors':projectors,
            'transport_moments':transport,'physical_comparison':{'cosine_squared_upper':cos2,'projector_distance_lower':sn,
                'angle_degrees_lower':angle,'angle_degrees_lower_display':v.sci(angle)},
            'both_examples_satisfy_full_b_gram':True,'both_examples_satisfy_separate_transport_mass_energy_positivity':True,
            'both_examples_violate_transport_high_support':True,'common_physical_transport_realization_claimed':False,
            'actual_odd_projector_localized':False,'full_transport_moment_family_localization_decided':False,
            'bandwise_true_maximizer_moments_computed':False,'large_operator_solves_rerun':False,'global_result_proved':False}
        args.out.write_text(json.dumps(v.rational(output),indent=2)+'\n',encoding='utf-8',newline='\n')
    print('TRANSPORT MOMENT EXCLUSIONS CERTIFIED; ACTUAL ODD LOCALIZATION REMAINS OPEN.',flush=True)
if __name__=='__main__':main()
