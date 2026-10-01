"""Joint projector geometry from existing actual projected Gram bounds.
Prepared before integration; execution requires the integrated registry.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,subprocess,sys
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--main',required=True);p.add_argument('--out',type=Path,required=True)
a=p.parse_args();repo=a.repo.resolve();git=['git','-c','safe.directory='+repo.as_posix(),'-C',str(repo)]
assert subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()==a.main
state=json.loads((repo/'00-uebersicht/RESEARCH_STATE.yaml').read_bytes())
assert not state['pending_packages'] and any(r['id']=='CANONICAL-ODD-BOX-STRUCTURAL-OPEN' and r['integration_status']=='MERGED' for r in state['results'])
assert not a.out.exists()
sys.path.insert(0,str(repo/'research/x-c1/canonical-joint-maximizers-2026-09-30/02-joint-discriminant'))
import verify_joint_discriminant as v
sources={}
def read(rel):
 raw=(repo/rel).read_bytes();assert raw==subprocess.check_output(git+['show',a.main+':'+rel])
 sources[rel]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
projected=read('research/x-c1/canonical-joint-maximizers-2026-09-30/01-projected-overlap/verification.json')
outer=read('research/x-c1/renewable-low-schur-spectral-2026-09-29/07-canonical-extension-outer-mass/primary.json')
def gram(name):
 return v.symmetric(v.intersectmat(v.matrix(projected['runs']['primary.json']['trials'][name]['projected_Gram']),v.matrix(projected['runs']['crosscheck.json']['trials'][name]['projected_Gram'])))
ga,gb=gram('A9-odd'),gram('A11-odd')
oa=outer['trials']['A9-odd'];ob=outer['trials']['A11-odd']
sa,sb=v.matrix(oa['physical_Ritz_matrix']),v.matrix(ob['physical_Ritz_matrix'])
o=v.matrix(outer['results']['A9->A11-odd']['trial_overlap']);nu=F(ob['physical_complement_gap_lower_exact'])
ea=v.submat(ga,v.mm(ga,ga));eb=v.submat(gb,v.mm(gb,gb))
ha=v.submat(v.eye(6),ga);hb=v.submat(v.eye(8),gb)
ea_diag=[min(ea[i][i][1],ha[i][i][1],ga[i][i][1]) for i in range(6)]
eb_diag=[min(eb[j][j][1],hb[j][j][1],gb[j][j][1]) for j in range(8)]
assert min(ea_diag+eb_diag)>=0
oa_rest=v.submat(v.eye(6),v.mm(o,v.tr(o)));ob_rest=v.submat(v.eye(8),v.mm(v.tr(o),o))
a_rest=v.mm(v.mm(ga,oa_rest),ga);b_rest=v.mm(v.mm(gb,ob_rest),gb)
ga_o=v.mm(ga,o);center=v.mm(ga_o,gb)
ky=[];yy=[];target={}
for i in range(6):
 kr=[];yr=[]
 for j in range(8):
  assert a_rest[i][i][1]>=0 and b_rest[j][j][1]>=0 and ob_rest[j][j][1]>=0
  # VA=UA GA+EA with EA*EA=GA-GA^2; the same holds at B.
  r1=v.sqrt_upper(ea_diag[i]*b_rest[j][j][1])
  r2=v.sqrt_upper(eb_diag[j]*a_rest[i][i][1])
  r3=v.sqrt_upper(ea_diag[i]*eb_diag[j])
  geometric=v.add(center[i][j],(-(r1+r2+r3),r1+r2+r3))
  # Forward formnaturality controls the B-high part of J VA_i.
  r4=v.sqrt_upper(ea_diag[i]*ob_rest[j][j][1])
  r5=v.sqrt_upper(sa[i][i][1]/nu*hb[j][j][1])
  forward=v.add(ga_o[i][j],(-(r4+r5),r4+r5))
  kij=v.intersect(geometric,forward);kr.append(kij)
  qr=v.sqrt_upper(sa[i][i][1]*sb[j][j][1])/17
  yij=v.add(kij,(-qr,qr));yr.append(yij)
  if i in (4,5) and j==7:
   target['Y'+str(i+1)+'8']={'joint_center':center[i][j],'geometric_radius_terms':[r1,r2,r3],
    'forward_center':ga_o[i][j],'forward_radius_terms':[r4,r5],'energy_radius':qr,'K':kij,'Y':yij}
 ky.append(kr);yy.append(yr)
report={'status':'EXPLORATORY_RIGOROUS_ENCLOSURES_NOT_GATE_ACCEPTANCE','stage':'A','main':a.main,
 'source_sha256':sources,'method':'common projector Gram identities and forward high support',
 'K_direct_enclosure':ky,'Y_direct_enclosure':yy,'targets':target,
 'joint_residual_identity_checked':True,'full_high_response_paid':True,
 'new_shifted_operator_solves':False,'signed_high_cross_products_individually_computed':False,
 'A13_inputs_used':False,'actual_odd_angle_certified':False}
a.out.write_text(json.dumps(v.rational(report),indent=2)+'\n',encoding='utf-8',newline='\n')
for key,item in target.items():print(key,'Y',v.display(item['Y']),'radii',[float(x) for x in item['forward_radius_terms']])
