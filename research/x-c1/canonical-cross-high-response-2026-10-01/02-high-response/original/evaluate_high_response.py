"""Propagate new actual Y bounds through the existing common physical model."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, subprocess, sys, tempfile
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
a=p.parse_args();repo=a.repo.resolve();raw=a.input.read_bytes();fresh=json.loads(raw)
git=['git','-c','safe.directory='+repo.as_posix(),'-C',str(repo)]
assert fresh['main']==subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()
assert fresh['status']=='EXPLORATORY_RIGOROUS_ENCLOSURES_NOT_GATE_ACCEPTANCE'
assert fresh['joint_residual_identity_checked'] and fresh['full_high_response_paid'] and not fresh['A13_inputs_used']
base=repo/'research/x-c1/canonical-odd-structural-open-2026-10-01/04-rational-box-gate'
sys.path.insert(0,str(base));import verify_box_gate as upstream
from box_math import BoxModel
with tempfile.TemporaryDirectory(prefix='cross-projector-propagation-') as directory:
 _,files,transport,old,v,df=upstream.dependencies(Path(directory),False)
 source=json.loads(df['inputs/primary.json']);outer=json.loads(df['inputs/outer_primary.json'])
 projected=json.loads(df['inputs/projected_verification.json']);inherited=json.loads(df['verification.json'])
 witness=json.loads(files['verification.json'])
 model=BoxModel(v,source,outer,projected,inherited)
 original=model.y;new=v.matrix(fresh['Y_direct_enclosure'])
 exclusions={}
 for label,row in witness['results'].items():
  w=v.matrix(row['corrected_Y']);bad=[]
  for i in range(6):
   for j in range(8):
    if w[i][j][1]<new[i][j][0] or w[i][j][0]>new[i][j][1]:
     bad.append({'entry':[i+1,j+1],'witness_interval':w[i][j],'new_actual_bound':new[i][j]})
  exclusions[label]=bad
 model.y=v.intersectmat(original,new);model.prepare()
 result=model.evaluate(model.root_box())
 assert result['filter_status']!='EXCLUDED','New actual bounds contradict inherited necessary constraints'
 direction=result.get('direction',{});sine=direction.get('sine_squared_to_common_reference')
 width=F(180)
 if sine and sine[1]<1:
  width=2*v.angle_degrees(v.point(v.sqrt_upper(sine[1]/(1-sine[1]))))[1]
 rotated_excluded=bool(exclusions['rotated'])
 green=bool(rotated_excluded and width<10)
 improved=[]
 for i in range(6):
  for j in range(8):
   if model.y[i][j]!=original[i][j]:improved.append([i+1,j+1])
 # Passing an outer bound never establishes a new coupled feasible completion.
 out={'status':'GREEN' if green else 'PARTIAL_GREEN' if rotated_excluded else 'UNRESOLVED','main':fresh['main'],
  'filter_receipt_sha256':hashlib.sha256(raw).hexdigest(),'new_Y_intersection':model.y,
  'entries_improved_relative_pre_cross_relaxation':improved,
  'new_target_improvements':[k for k,vv in fresh['targets'].items() if vv['strictly_improved']],
  'previous_counterfamily_exclusions':exclusions,
  'joint_model_evaluation':result,'physical_reference_coefficients':model.reference,
  'certified_common_corridor_total_degrees_upper':width,'GREEN_total_width_strictly_below':10,
  'actual_odd_projector_localized_under_target':green,
  'STRUCTURAL_OPEN_2_claimed':False,'new_feasible_completion_claimed':False,
  'full_nuisance_entry_uncertainties_retained':True,'same_N_for_all_moments':True,
  'norm_convention':'BB=GB+LB/17; inverse-response direction in physical GB metric',
  'research_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN','A13_inputs_used':False}
 a.out.write_text(json.dumps(v.rational(out),indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({'status':out['status'],'new_target_improvements':len(out['new_target_improvements']),
  'inherited_improved_entries':len(improved),
  'excluded_counterfamilies':[k for k,vv in exclusions.items() if vv],
  'corridor_total_degrees_upper':float(width)}))
