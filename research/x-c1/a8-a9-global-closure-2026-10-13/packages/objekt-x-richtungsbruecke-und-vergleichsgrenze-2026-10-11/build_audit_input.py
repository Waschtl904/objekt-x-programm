from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
def read(p):return json.loads(p.read_bytes())
fin=ROOT/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09'
paths={'bridge':ROOT/'work/inherited/Objekt-X-Unendlicher-Rest-Vergleich-2026-10-09/work/infinite-tail-2026-10-09/FINITE_BRIDGE.json',
 'schur':fin/'work/gamma-low-2026-10-09/SCHUR_SHELL_TIGHT_4096.json',
 'review':HERE/'review-rebuild/BRIDGE_OBSTRUCTION_INPUT.json',
 'half':fin/'work/remainder-integration-check-v2/originals/half-inverse/expected/1536.json'}
bs=read(paths['bridge'])['cases'];ss=read(paths['schur'])['cases'];rv=read(paths['review'])['cases'];hf=read(paths['half'])['blocks'];cases=[]
for p,label in enumerate(['EVEN','ODD']):
 paths[f'galerkin_{label}']=ROOT/f'work/galerkin84-2026-10-10/GALERKIN_{label}_3072.json'
 paths[f'inverse_{label}']=fin/f'work/gamma-low-2026-10-09/CERTIFICATE_{label}_gamma224_tight_4096.json'
 paths[f'basis_{label}']=ROOT/f'work/basis-coverage-2026-10-10/BASIS_{label}.json'
 g=read(paths[f'galerkin_{label}']);c=read(paths[f'inverse_{label}'])
 keys=['C84_model','B84_model','H84_model','H84_operator_error_scalar','C84_D0_inverse_metric_error_norm','R84_operator_error_scalar','weighted_low_error_squared']
 cases.append({'parity':label.lower(),'bridge':bs[p+2],'schur':ss[p],'review':rv[p],
  'galerkin':{k:g[k] for k in keys},'potential':{k:g['optional_positive_potential_comparison'][k] for k in ['potential84_model','Bplus_operator_error_scalar']},
  'certificate':{k:c[k] for k in ['rho','model_upper_energy','energy_model_error_gram']},
  'S':hf[p]['half_inverse_centre_rational_Q_coefficients'],'D':read(paths[f'basis_{label}'])['D_rational']})
out={'status':'BOUND_FINITE_INPUT_EXTRACT','cases':cases,'sources':{k:{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in paths.items()}}
(HERE/'AUDIT_INPUT.json').write_text(json.dumps(out,indent=2)+'\n')
