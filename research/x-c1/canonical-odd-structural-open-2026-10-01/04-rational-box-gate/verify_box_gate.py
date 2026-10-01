"""Four-variable rational branching with certified feasible point witnesses."""
from pathlib import Path,PurePosixPath
from fractions import Fraction as F
import argparse,copy,hashlib,importlib,io,json,os,subprocess,sys,tempfile,zipfile
from box_math import BoxModel,VARIABLES,split_box,covers_point,classify

BASE=Path(__file__).resolve().parent
ARCHIVE='Projektorgrenze-trotz-Transportmomenten-2026-09-30.zip'
SHA='5c5922ed739695d3baa7578c0e1bca05a4b758c969ea8768858c40207dd4904f'
ROOT='canonical-projector-transport-obstruction-2026-09-30'

def unpack(raw,dest):
 assert hashlib.sha256(raw).hexdigest()==SHA,'upstream archive hash mismatch'
 files={}
 with zipfile.ZipFile(io.BytesIO(raw)) as z:
  for info in z.infolist():
   path=PurePosixPath(info.filename)
   assert not path.is_absolute() and '..' not in path.parts and '\\' not in info.filename
   assert path.parts[0]==ROOT and len(path.parts)>1 and not info.is_dir()
   key='/'.join(path.parts[1:]);assert key not in files;files[key]=z.read(info)
 manifest={n:h for h,n in (line.split('  ',1) for line in files['SHA256SUMS'].decode().splitlines())}
 assert set(manifest)==set(files)-{'SHA256SUMS'}
 for name,h in manifest.items():assert hashlib.sha256(files[name]).hexdigest()==h
 for name,data in files.items():
  p=dest/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 return files

def dependencies(temp,replay=False):
 folder=temp/'previous';files=unpack((BASE/'inputs'/ARCHIVE).read_bytes(),folder)
 if replay:
  target=temp/'previous-replay.json'
  run=subprocess.run([sys.executable,'-B',str(folder/'verify_projector_transport.py'),'--out',str(target)],
   env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,check=True)
  assert not run.stderr and target.read_bytes()==files['verification.json']
  print('Full upstream witness construction and all embedded replays: byte-identical PASS',flush=True)
 sys.path.insert(0,str(folder));previous=importlib.import_module('verify_projector_transport')
 _,_,transport=previous.load_input(temp/'transport-input',False)
 old,v,df,_=transport.dependencies(temp/'old-input',False)
 return folder,files,transport,old,v,df

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
 parameters_raw=(BASE/'parameters.json').read_bytes();params=json.loads(parameters_raw)
 assert params['variables']==list(VARIABLES) and params['split_cycle']==['Y58','Y68','Y57','Y67']
 assert params['initial_priority_depth']==2 and params['max_depth']>=2 and params['max_nodes']>=7
 with tempfile.TemporaryDirectory(prefix='odd-box-gate-') as name:
  temp=Path(name);_,files,transport,old,v,df=dependencies(temp,True);e=transport.e
  source=json.loads(df['inputs/primary.json']);outer=json.loads(df['inputs/outer_primary.json'])
  projected=json.loads(df['inputs/projected_verification.json']);inherited=json.loads(df['verification.json'])
  witness=json.loads(files['verification.json'])
  assert witness['integration_base']==params['integration_base']
  assert witness['both_examples_satisfy_transport_high_support']
  model=BoxModel(v,source,outer,projected,inherited);model.target=F(params['target_sine_squared_upper'])
  models={name:e.measure(source['results'][rk],outer['trials'][name]) for name,rk in [('A9-odd','A8->A9-odd'),('A11-odd',model.key)]}
  fixed={letter+suffix:e.intervals(v,models[chamber][field]) for chamber,suffix in [('A9-odd','A'),('A11-odd','B')]
    for letter,field in [('G','GP'),('L','LP'),('Z','ZP')]}
  witnesses={};coordinates={}
  for label,row in witness['results'].items():
   point=copy.copy(model);point.full=fixed;point.y=v.matrix(row['corrected_Y']);point.prepare()
   coords=point.root_box();assert covers_point(model.root_box(),coords)
   coordinates[label]=coords
   check=point.evaluate(coords);assert check['filter_status']=='NOT_EXCLUDED'
   # A feasible point is supplied by the fully replayed coupled construction.
   # These positive interval pivots additionally guard its transport enclosure.
   pivots={key:e.positive_interval(v,a) for key,a in point.transport(point.y).items()}
   assert 'sine_squared_to_common_reference' in check['direction'],check['direction']
   witnesses[label]={'certified_feasible_point_from_replayed_construction':True,
    'coordinates':coords,'coordinate_display':{k:v.display(x) for k,x in coords.items()},
    'transport_pivots':pivots,'direction':check['direction']}
   print(label,'feasible point, physical sin^2 to fixed reference',v.display(check['direction']['sine_squared_to_common_reference']),flush=True)
  separation=F(witness['physical_comparison']['angle_degrees_lower'])
  target_angle=v.angle_degrees(v.point(v.sqrt_upper(model.target/(1-model.target))))[1]
  assert separation>2*target_angle
  frontier=[{'id':'root','depth':0,'box':model.root_box()}];nodes=[];leaves=[];status='UNRESOLVED'
  while frontier:
   next_frontier=[]
   for node in frontier:
    evaluated=model.evaluate(node['box']);node.update(evaluated)
    node['witnesses']=[k for k,p in coordinates.items() if covers_point(node['box'],p)]
    assert not (node['filter_status']=='EXCLUDED' and node['witnesses']),'false rejection of a certified feasible point'
    for label in node['witnesses']:
     if witnesses[label]['direction']['sine_squared_to_common_reference'][0]>model.target:
      assert not node.get('direction',{}).get('within_target_corridor',False),'false direction enclosure'
    nodes.append(node)
    can_split=node['filter_status']!='EXCLUDED' and node['depth']<params['max_depth'] and len(nodes)+len(frontier)+len(next_frontier)+2<=params['max_nodes']
    if node['depth']<params['initial_priority_depth'] and can_split:
     key=params['split_cycle'][node['depth']%4];left,right=split_box(node['box'],key);node['split_variable']=key
     next_frontier.extend([{'id':node['id']+side,'depth':node['depth']+1,'box':b} for side,b in [('L',left),('R',right)]])
    else:leaves.append(node)
   if next_frontier:
    frontier=next_frontier;continue
   containing={label:[n['id'] for n in leaves if label in n['witnesses']] for label in witnesses}
   distinct=all(containing.values()) and any(a!=b for a in containing['central'] for b in containing['rotated'])
   status=classify(leaves,distinct and separation>2*target_angle)
   if status!='UNRESOLVED':break
   # Continue adaptively only when the mathematical outcome is undecided.
   candidates=[n for n in leaves if n['filter_status']!='EXCLUDED' and not n.get('direction',{}).get('within_target_corridor',False) and n['depth']<params['max_depth']]
   if not candidates or len(nodes)+2>params['max_nodes']:break
   selected=max(candidates,key=lambda n:max((n['box'][k][1]-n['box'][k][0])/(model.root_box()[k][1]-model.root_box()[k][0]) for k in VARIABLES))
   leaves.remove(selected);key=params['split_cycle'][selected['depth']%4];left,right=split_box(selected['box'],key);selected['split_variable']=key
   frontier=[{'id':selected['id']+side,'depth':selected['depth']+1,'box':b} for side,b in [('L',left),('R',right)]]
  assert status=='STRUCTURAL_OPEN'
  # Every recorded split exactly partitions its parent with a shared boundary.
  by_id={n['id']:n for n in nodes}
  for node in nodes:
   if 'split_variable' in node:
    left,right=split_box(node['box'],node['split_variable'])
    assert by_id[node['id']+'L']['box']==left and by_id[node['id']+'R']['box']==right
  out={'status':status,'research_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN','integration_base':params['integration_base'],
   'upstream_archive_sha256':SHA,'upstream_byte_exact_replay':True,'parameters_sha256':hashlib.sha256(parameters_raw).hexdigest(),
   'full_nuisance_entry_uncertainties_retained':True,'norm_convention':'BB=GB+LB/17; X=BB^-1 Y*',
   'reference_coefficients':model.reference,'target_sine_squared_upper':model.target,'target_angle_degrees_upper':target_angle,
   'nodes':nodes,'leaf_ids':[x['id'] for x in leaves],'witnesses':witnesses,
   'physical_separation_degrees_lower':separation,'node_count':len(nodes),'leaf_count':len(leaves),
   'excluded_leaf_count':sum(n['filter_status']=='EXCLUDED' for n in leaves),
   'stop_reason':'two fully certified feasible completions in distinct surviving boxes exceed the common target corridor',
   'box_survival_alone_claimed_feasible':False,'actual_odd_projector_localized':False,
   'full_physical_realization_of_all_trial_data_claimed':False,'large_operator_solves_rerun':False,'A13_inputs_used':False}
  args.out.write_text(json.dumps(v.rational(out),indent=2)+'\n',encoding='utf-8',newline='\n')
  print(status,':',len(nodes),'nodes,',len(leaves),'leaves; physical witness separation >= 89.987266 degrees.',flush=True)
if __name__=='__main__':main()
