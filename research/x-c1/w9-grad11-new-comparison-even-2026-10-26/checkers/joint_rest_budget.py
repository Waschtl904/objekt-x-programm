"""Rational closure with every mixed residual term; partial reports never pass."""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import json,hashlib,sys,time,argparse
sys.set_int_max_str_digits(20000)
H=Path(__file__).resolve().parent;start=time.monotonic()
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
geom=json.loads((H/'JOINT_TAIL_GEOMETRY.json').read_bytes())
assert sha(H/'SOURCE_ARITHMETIC_CLOSURE.json')==geom['source_closure_sha256']
A=[[Q(x)for x in row]for row in geom['inverse']]
C=[[Q(x)for x in row]for row in geom['finite_gap_lower_in_basis']]
def sqrt_up(x):
    assert x>=0
    n=isqrt(x.numerator*10**160//x.denominator)
    if n*n*x.denominator<x.numerator*10**160:n+=1
    return Q(n,10**80)
beta=sqrt_up(Q(5,21));rows=[];errors=[];norms=[];missing=[]
for i in range(12):
    label='T'+str(i).zfill(2);d=H/('directed-whole-'+label)
    component=H/('COMPONENTS_'+label+'.json')
    if i:
        assert component.exists(),'Missing directional component receipt: '+label
        receipt=json.loads(component.read_bytes())
        assert receipt['label']==label
        assert receipt['model_binding_sha256']==sha(H/(label+'_MODEL_BINDING.json'))
        assert receipt['driver_sha256'] in [sha(H/'certify_direction_components.py'),sha(H/'certify_direction_components_v1.py')]
        for name,digest in receipt['files'].items():assert sha(H/name)==digest
    physical=H/('WHOLE_PHYSICAL_ERROR_DYNAMIC_'+label+'.json')
    if not physical.exists():physical=H/('WHOLE_PHYSICAL_ERROR_CLOSED_'+label+'.json')
    core=H/(('RETAINED_CORE_QUADRATURE_'if i==0 else'RETAINED_CORE_QUADRATURE_R2875_')+label+'.json')
    strip=H/('CORE_TAIL_VARIATION_'+label+'.json');small=H/('SMALL_MODEL_CHANGES_'+label+'.json')
    if not all(p.exists()for p in [physical,core,strip,small]):
        rows.append({'label':label,'status':'DIRECTIONAL_COMPONENTS_PENDING'});errors.append(Q());norms.append(None);missing.append(label);continue
    pq=json.loads(physical.read_bytes())['quantities'];cq=json.loads(core.read_bytes())['quantities'];sq=json.loads(strip.read_bytes())['quantities']
    assert Q(json.loads(small.read_bytes())['small_raw_upper'])<Q('1e-150')
    inner=Q(cq['combined_X_error'][1])+Q(sq['whole_X_error_from_strip_variation'][1])
    error=beta*inner+Q(pq['full_Qold_dual_error_expression'][1]);errors.append(error)
    row={'label':label,'known_non_model_error_norm_upper':str(error),'known_non_model_error_relative_square':float(A[i][i]*error**2)}
    if not (d/'BINDING.json').exists():row.update(status='OUTER_INTEGRATION_PENDING');norms.append(None);rows.append(row);continue
    bind=json.loads((d/'BINDING.json').read_bytes());count=bind['panel_count']
    files=[d/(str(k).zfill(4)+'.json')for k in range(count)]
    present=[p for p in files if p.exists()]
    row.update(complete_intervals=len(present),expected_intervals=count)
    if len(present)!=count:row.update(status='PARTIAL_OUTER_COVER');norms.append(None);rows.append(row);continue
    for name,digest in bind['sources'].items():assert sha(H/name)==digest
    assert sha(H/geom['caches'][i]['cache'])==bind['cache']==geom['caches'][i]['sha256']
    total=Q();parts=[]
    for k,path in enumerate(files):
        r=json.loads(path.read_bytes());assert r['index']==k and r['status']=='DIRECTED_NEW_MODEL_INTERVAL'
        assert Q(r['midpoint_difference'][1])<Q('1e-40')and Q(r['weighted_remainder'][1])<Q('1e-21')
        energy=Q(r['values']['model_Xnorm_squared_upper'][1]);assert energy>=0
        total+=energy;parts.append(sha(path))
    # Independent rational end bound: if d>=2^-k, then -log(d)<k.
    # d<2^-150 ensures -log(d)>100, using log(2)>2/3.
    oe=[[Q(x)for x in box]for box in bind['outer_edges']];depth=bind['depth']
    widths=[(oe[1][0]-oe[0][1],oe[1][1]-oe[0][0]),(oe[-1][0]-oe[-2][1],oe[-1][1]-oe[-2][0])]
    E=Q(json.loads((H/('CONTOUR_CAPS_'+label+'.json')).read_bytes())['whole_endpoint_log_squared_envelope']);tails=Q()
    for wl,wu in widths:
        dl,du=wl/2**depth,wu/2**depth;assert 0<dl<=du<Q(1,2**150)
        k=max(1,dl.denominator.bit_length()-dl.numerator.bit_length()+1)
        while Q(1,2**k)>dl:k+=1
        while k>1 and Q(1,2**(k-1))<=dl:k-=1
        tails+=2*E*E*du*(29+28*k+14*k*k+4*k**3+k**4)
    capcheck=H/('CAPS_APPLICATION_CHECK_'+label+'.json')
    assert capcheck.exists();checked=json.loads(capcheck.read_bytes())
    assert all(checked['checks'].values())
    assert checked['source_sha256']==sha(H/('ENDPOINT_INGREDIENTS_'+label+'.json'))
    assert checked['analytic_application_sha256']==sha(H/'NEW_CONTOUR_APPLICATION.txt')
    n=beta*sqrt_up(total+tails)+error;norms.append(n)
    row.update(status='FULL_DIRECTIONAL_BOUND_UNDER_AUTHOR_APPLICATION',model_energy_upper=str(total+tails),rational_endpoint_energy_upper=str(tails),
               whole_dual_norm_upper=str(n),diagonal_relative_price=float(A[i][i]*n*n),
               interval_manifest_sha256=hashlib.sha256(''.join(parts).encode()).hexdigest())
    rows.append(row)
known=sum((abs(A[i][j])*errors[i]*errors[j]for i in range(12)for j in range(12)),Q())
out={'status':'PARTIAL_COMMON_REST_BUDGET','directions':rows,'missing_component_sets':missing,
     'known_non_model_error_budget_expression':str(known),'all_non_model_components_present':not missing,
     'whole_joint_pass':False,'independent_analytic_review_complete':False,
     'common_frame_sha256':sha(H/'JOINT_TAIL_GEOMETRY.json'),'seconds':time.monotonic()-start}
if all(n is not None for n in norms):
    theta=sum((abs(A[i][j])*norms[i]*norms[j]for i in range(12)for j in range(12)),Q())
    audit=json.loads((H/'SOURCE_CLOSED_GAP_EXACT_AUDIT.json').read_bytes())
    assert audit['ledger_sha256']==geom['source_closure_sha256']
    out.update(status='COMMON_REST_AUTHOR_BOUND_COMPLETE',relative_rest_upper=str(theta),whole_joint_pass=theta<1,
               resulting_GW_floor=str((1-theta)*Q(audit['proved_W_floor_for_stored_ledger'])),
               qualification='New author application under H1-H4; targeted independent and external analytic review remain open.')
(args.output or H/'JOINT_REST_BUDGET.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('Whole directions complete',sum(n is not None for n in norms),'/12; missing component sets',missing)
print('Known error-only budget expression',float(known))
if 'relative_rest_upper'in out:print('Whole relative budget',float(Q(out['relative_rest_upper'])),'pass',out['whole_joint_pass'])
