"""Independent assembly: prior 65 + newly replayed 16, previous adjoint kernel correction,
and radius-corrected signed core-tail replay. No model fitting or new direction."""
import sys,json
from pathlib import Path
from fractions import Fraction as F
B=Path(__file__).resolve().parent;A=B.parent
sys.path.insert(0,str(A))
from load_context import *
R=B/'received';W=B/'work/pairing-refinement';J=values['J'];a,b,hs=(values[k] for k in ('a','b','hs'))
extra=set(list(range(32,40))+list(range(238,246)))
selected=set(json.loads((R/'Eingangsprotokoll/model-pairing-check.json').read_bytes())['selected_panels'])|extra
assert len(selected)==81
mom=arb_mat(96,1);tf=arb(0);ofactor=arb(0)
new_receipts=[]
for i in range(411):
 source=WHOLE/f'taylor-model-panels-205/{i:04}.json';old=json.loads(source.read_bytes())
 lo,hi=c.box(old['lo']),c.box(old['hi']);width=(hi-lo).upper();assert width>0
 if i in selected:
  p=W/f'extra-panels/{i:04}.json' if i in extra else R/f'Abschnitte/{i:04}.json'
  row=json.loads(p.read_bytes());assert row['index']==i
  assert c.box(row['lo']).overlaps(lo) and c.box(row['hi']).overlaps(hi)
  mom+=mat(row['moments']);tf+=(2*width*q(row['taylor_error_X_squared'][1])).sqrt().upper()
  if i in extra:
   received=json.loads((R/f'Abschnitte/{i:04}.json').read_bytes())
   assert row['order']==received['order']
   for x,y in zip(row['moments'],received['moments']):assert c.box(x[0]).overlaps(c.box(y[0]))
   new_receipts.append({'index':i,'moments_overlapping':96,'sha256':sha(p.read_bytes()),'maximum_midpoint_control':row['midpoint_control'],'order':row['order'],'seconds':row['seconds']})
 else:ofactor+=(2*width*q(old['model_Xnorm_squared_upper'][1])).sqrt().upper()
outer=json.loads((WHOLE/'taylor-model-panels-205/BINDING.json').read_bytes())['outer_edges'];oe=list(map(c.box,outer));ef=arb(0)
for d in [(oe[1]-a)*arb(2)**(-205),(b-oe[2])*arb(2)**(-205)]:
 assert 0<d<1;t=-d.log();ef+=(2*q('1e20')*d*(t*t+2*t+3)).upper()
partial=J.transpose()*mom
finite=json.loads((R/'Eingangsprotokoll/finite-bridge.json').read_bytes())['coordinates']
correction=json.loads((A/'fixed-source-investigation/kernel-correction.json').read_bytes())['rows']
tail=json.loads((W/'core-tail.json').read_bytes());remain=q(tail['remaining_core_X_error'][1])
rows=[]
for i in range(84):
 sup=sum((abs(J[k,i]).upper()*(arb(2*k+1)/(2*hs)).sqrt() for k in range(96)),arb(0)).upper()
 integration=(sup*(tf+ofactor+ef)).upper()
 tailprice=(remain*sum((J[k,i]**2 for k in range(96)),arb(0)).upper().sqrt()).upper()
 encpartial=c.enc(partial[i,0]);model=finite[i]['expanded_model'];C=correction[i]['signed_corrected_minus_original_pairing'];H=tail['rows'][i]['signed_core_tail_correction']
 # Exact rational complete arithmetic hull, not midpoint or mere overlap.
 lo=F(encpartial[0])-F(model[1])+F(C[0])+F(H[0]);hi=F(encpartial[1])-F(model[0])+F(C[1])+F(H[1])
 ie=F(c.enc(integration)[1]);he=F(c.enc(tailprice)[1]);error=ie+he
 magnitude=max(abs(lo),abs(hi));assert magnitude<=error, i+1
 rows.append({'coordinate':i+1,'raw_difference':[str(lo),str(hi)],'integration_error_upper':str(ie),'remaining_core_error_upper':str(he),'complete_error_envelope':str(error),'margin':str(error-magnitude),'full_arithmetic_interval_contained':True})
contour=json.loads((W/'contour-review.json').read_bytes());rl=F(contour['normalized_radius'][0]);M=F(contour['corrected_contour_bound'][1]);cauchy=M*rl**(-8)/(1-1/rl);assert cauchy<F('2e-88')
received=json.loads((R/'Pruefdaten/core-tail.json').read_bytes())
assert all(x==y for x,y in zip(tail['rows'],received['rows']))
out={'status':'REPLAYED_16_PANELS_AND_RADIUS_REPAIRED_CORE_TAIL_FULL_HULL_CHECK_PASSED_CONDITIONALLY','selected_panels':sorted(selected),'new_panels':new_receipts,'rows':rows,'all_84_pass':True,'minimum_margin':str(min(F(r['margin'])for r in rows)),'maximum_integration_error':str(max(F(r['integration_error_upper']) for r in rows)),'maximum_raw_difference_absolute':str(max(max(abs(F(x))for x in r['raw_difference'])for r in rows)),'core_tail_84_serialized_rows_unchanged_after_contour_fix':True,'corrected_cauchy_remainder_upper':str(cauchy),'corrected_cauchy_remainder_simple_cap':'2e-88','inherited_analytic_caps_independently_reproved':False,'external_acceptance':'OPEN','repository_modified':False}
(B/'reassembly-audit.json').write_text(json.dumps(out,indent=2)+'\n')
for k in ['status','all_84_pass','minimum_margin','maximum_integration_error','maximum_raw_difference_absolute','corrected_cauchy_remainder_simple_cap']:print(k,float(F(out[k])) if k in ['minimum_margin','maximum_integration_error','maximum_raw_difference_absolute','corrected_cauchy_remainder_simple_cap'] else out[k])
