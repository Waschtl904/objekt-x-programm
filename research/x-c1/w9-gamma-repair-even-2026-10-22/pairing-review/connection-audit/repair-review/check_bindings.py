from pathlib import Path
import json,hashlib
from fractions import Fraction as F
B=Path(__file__).resolve().parent;A=B.parent;R=B/'received';P=A/'repo/research/x-c1/w9-residual-centered-control-even-2026-10-21'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((P/'MANIFEST.json').read_bytes());binding=json.loads((R/'Pruefdaten/bindings.json').read_bytes());checks={}
for k,h in binding['source_bindings'].items():assert sha(P/k)==h,k
checks['source_bindings']=len(binding['source_bindings'])
for p in (R/'Gefrorene-Energieabschnitte').glob('*.json'):
 rel='whole/taylor-model-panels-205/'+p.name
 assert sha(p)==manifest[rel]==sha(P/rel),rel
checks['frozen_energy_files']=len(list((R/'Gefrorene-Energieabschnitte').glob('*.json')))
audit=json.loads((R/'Eingangsprotokoll/model-pairing-check.json').read_bytes())
for row in audit['panel_receipts']:
 name=f"{row['index']:04}.json"
 assert sha(R/'Abschnitte'/name)==row['sha256']==sha(A/'pairing-panels'/name),name
checks['previous_signed_panel_bindings']=len(audit['panel_receipts'])
for name,h in binding['new_panel_receipts'].items():assert sha(R/'Abschnitte'/name)==h,name
checks['new_signed_panel_bindings']=len(binding['new_panel_receipts'])
ours=json.loads((A/'fixed-source-investigation/kernel-correction.json').read_bytes())['rows'];their=json.loads((R/'Pruefdaten/kernel-orientation-81.json').read_bytes())['rows']
assert len(ours)==len(their)==84
exact=overlap=0
for x,y in zip(ours,their):
 a=x['signed_corrected_minus_original_pairing'];b=y['orientation_correction']
 exact+=list(map(F,a))==list(map(F,b))
 assert max(F(a[0]),F(b[0]))<=min(F(a[1]),F(b[1])),x['coordinate']
 overlap+=1
checks['kernel_correction_intervals_exactly_equal_to_independent_adjoint_route']=exact
checks['kernel_correction_intervals_overlap']=overlap
for k,path in [('WHOLE_RESULT.json','whole/WHOLE_RESULT.json'),('FINITE_RESULT.json','RESULT.json')]:assert sha(R/'Pruefdaten/budget-inputs'/k)==sha(P/path)
checks['budget_input_bindings']=2
x=(R/'Pruefdaten/rational-audit.json').read_bytes();y=(B/'work/Pruefdaten/rational-audit.json').read_bytes();assert json.loads(x)==json.loads(y)
checks['rational_replay_semantically_exact']=True;checks['rational_replay_only_CRLF_difference']=x.replace(b'\r\n',b'\n')==y
out={'checks':checks,'archive_sha256':sha(A.parent/'upload/Objekt-X-Kernfehler-und-Anschlussreparatur-2026-10-22-Nachweise.zip'),'original_main_commit':binding['main_binding']}
(B/'binding-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
