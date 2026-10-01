"""Directed rational certificate of a projector obstruction with transported moments."""
from pathlib import Path,PurePosixPath
from fractions import Fraction as F
import argparse,hashlib,importlib,io,json,os,subprocess,sys,tempfile,zipfile

BASE=Path(__file__).resolve().parent
ARCHIVE='Gemeinsame-Transportmomente-2026-09-30.zip'
SHA='446df19299f27532c90e7aeed6759e55978546afd3e4ea0d0716742358f1cf33'
ROOT='canonical-transport-moment-gate-2026-09-30'
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

def load_input(temp,replay=False):
 folder=temp/'transport';files=unpack((BASE/'inputs'/ARCHIVE).read_bytes(),folder)
 if replay:
  target=temp/'upstream-replay.json'
  run=subprocess.run([sys.executable,'-B',str(folder/'verify_transport_gate.py'),'--out',str(target)],
   env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,check=True)
  assert not run.stderr and target.read_bytes()==files['verification.json']
  print('Upstream transport, odd-projector, Schur-defect and discriminant replays: byte-identical PASS',flush=True)
 sys.path.insert(0,str(folder));up=importlib.import_module('verify_transport_gate')
 return folder,files,up

def moments(v,y,ga,la,gb,lb,nu):
 ba=v.addmat(ga,v.scale(la,F(1,17)));bb=v.addmat(gb,v.scale(lb,F(1,17)))
 z=v.mm(y,v.inverse(bb,True))
 mass=v.symmetric(v.submat(ga,v.mm(v.mm(z,gb),v.tr(z))))
 energy=v.symmetric(v.submat(la,v.mm(v.mm(z,lb),v.tr(z))))
 return {'mass':mass,'energy':energy,
  'b_defect':v.symmetric(v.submat(ba,v.mm(z,v.tr(y)))),
  'support_defect':v.symmetric(v.submat(energy,v.scale(mass,nu)))}

def contained(v,a,box):
 b=v.matrix(box)
 assert len(a)==len(b) and all(len(x)==len(y) for x,y in zip(a,b))
 assert all(b[i][j][0]<=x[0]<=x[1]<=b[i][j][1] for i,row in enumerate(a) for j,x in enumerate(row))

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);args=p.parse_args()
 paramsraw=(BASE/'parameters.json').read_bytes();params=json.loads(paramsraw);assert F(params['correction_coefficient'])==F(1,4)
 with tempfile.TemporaryDirectory(prefix='projector-transport-') as name:
  temp=Path(name);folder,files,up=load_input(temp,True)
  old,v,df,_=up.dependencies(temp/'dependencies',False);e=up.e;tm=up.tm
  source=json.loads(df['inputs/primary.json']);outer=json.loads(df['inputs/outer_primary.json'])
  projected=json.loads(df['inputs/projected_verification.json']);inherited=json.loads(files['verification.json'])
  assert params['integration_base']==inherited['integration_base']
  models={name:e.measure(source['results'][rk],outer['trials'][name]) for name,rk in [('A9-odd','A8->A9-odd'),('A11-odd',KEY)]}
  ga,la,gb,lb=(e.intervals(v,m) for m in [models['A9-odd']['GP'],models['A9-odd']['LP'],models['A11-odd']['GP'],models['A11-odd']['LP']])
  nu=models['A11-odd']['nu'];gai=v.inverse(ga,True)
  o=e.midpoint(outer['results'][KEY]['trial_overlap']);prevparams=json.loads(files['parameters.json'])
  rotation=tm.rotation_data(o,list(map(F,prevparams['row_weights'])))
  points={'central':F(0),'rotated':F(prevparams['root_parameter'])}
  results={};pencils={};vectors={}
  for label,t in points.items():
   y=e.mm(e.mm(e.mm(models['A9-odd']['GP'],o),tm.cayley(rotation,t)),models['A11-odd']['GP'])
   pencil=e.pencil(y,models['A11-odd']);pencils[label]=pencil
   yi=e.intervals(v,y);before=moments(v,yi,ga,la,gb,lb,nu)
   assert all(p[0]>0 for p in e.positive_interval(v,before['mass']))
   # This interval encloses the exact rational C=I+H0 GA^-1/4.
   correction=v.addmat(v.eye(6),v.scale(v.mm(before['mass'],gai),F(1,4)))
   corrected_y=v.mm(correction,yi);after=moments(v,corrected_y,ga,la,gb,lb,nu)
   pivots={field:e.positive_interval(v,a) for field,a in after.items()}
   # GA>0 and H0>0 make C similar to a positive definite matrix.
   # Consequently ker(CY)=ker(Y); no uncertain component division is needed.
   corrected_yn=v.mm(corrected_y,e.intervals(v,pencil['N']))
   assert all(x[0]<=0<=x[1] for row in corrected_yn for x in row)
   # Independent interval evaluation of the exact polynomial mass identity.
   h=before['mass'];a=v.mm(h,gai);ah=v.mm(a,h);aah=v.mm(a,ah)
   mass_formula=v.addmat(v.addmat(v.scale(h,F(1,2)),v.scale(ah,F(7,16))),v.scale(aah,F(1,16)))
   v.intersectmat(after['mass'],mass_formula)
   proj,k=old.projector(v,pencil)
   assert v.rational(proj)==inherited['projectors'][label]
   col=1 if label=='central' else 0;vectors[label]=v.mm(e.intervals(v,pencil['N']),[[row[col]] for row in k])
   runs={}
   for runname in ('primary.json','crosscheck.json'):
    data=json.loads(df['inputs/'+runname]);bounds=projected['runs'][runname]
    contained(v,corrected_y,bounds['results'][KEY]['Y'])
    # The existing full pencil checker is applied to the unchanged kernel
    # and moments. Corrected Y containment is checked separately above;
    # exact Ynew N=0 follows from C(Yold N)=0.
    tests=old.check_pencil(v,pencil,data['results'][KEY],bounds['results'][KEY],models['A11-odd'])
    measures={name:old.check_measure(v,models[name],data['results'][rk],outer['trials'][name],bounds['trials'][name])
      for name,rk in [('A9-odd','A8->A9-odd'),('A11-odd',KEY)]}
    runs[runname]={'pencil':tests,'measures':measures,'corrected_Y_in_certified_entry_box':True}
   results[label]={'runs':runs,'correction':correction,'corrected_Y':corrected_y,
    'transported_moments':after,'ldl_pivots':pivots,
    'minimum_pivot_displays':{field:v.sci(min(p[0] for p in pp)) for field,pp in pivots.items()},
    'same_exact_kernel_and_projector':True,'projector':proj}
   print(label,'ALL strengthened moment constraints PASS; minimum pivots',results[label]['minimum_pivot_displays'],flush=True)
  u,w=vectors['central'],vectors['rotated'];uv=v.mm(v.mm(v.tr(u),gb),w)[0][0]
  uu=v.mm(v.mm(v.tr(u),gb),u)[0][0];ww=v.mm(v.mm(v.tr(w),gb),w)[0][0]
  assert uu[0]>0 and ww[0]>0
  cos2=v.div(v.square(uv),v.mul(uu,ww))[1];assert 0<=cos2<F(1,100)
  cs=v.sqrt_upper(cos2);sn=v.sqrt_lower(1-cos2);angle=F(90)-v.angle_degrees(v.point(cs/sn))[1]
  assert angle==F(inherited['physical_comparison']['angle_degrees_lower']) and angle>F('89.987266')
  out={'status':'TRANSPORT_MOMENT_FAMILY_PROJECTOR_OBSTRUCTION_CERTIFIED',
   'research_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN','integration_base':params['integration_base'],
   'upstream_archive_sha256':SHA,'parameters_sha256':hashlib.sha256(paramsraw).hexdigest(),
   'upstream_byte_exact_replay':True,'results':results,
   'physical_comparison':{'cosine_squared_upper':cos2,'projector_distance_lower':sn,'angle_degrees_lower':angle},
   'both_examples_satisfy_transport_high_support':True,'full_physical_realization_of_all_trial_data_claimed':False,
   'actual_odd_projector_localized':False,'actual_maximizer_band_moments_computed':False,
   'forward_renewal_theorem_proved':False,'A13_inputs_read':False,'large_operator_solves_rerun':False}
  args.out.write_text(json.dumps(v.rational(out),indent=2)+'\n',encoding='utf-8',newline='\n')
  print('Physical angle >= 89.987266 degrees. No actual odd localization is claimed.',flush=True)
if __name__=='__main__':main()
