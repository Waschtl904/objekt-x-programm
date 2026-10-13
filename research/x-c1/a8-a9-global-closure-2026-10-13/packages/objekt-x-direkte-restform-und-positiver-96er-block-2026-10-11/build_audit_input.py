from pathlib import Path
import json,gzip,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
def read(p):
 b=p.read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)
fin=ROOT/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09'
op=fin/'work/remainder-integration-check-v2/originals/weighted-response/inputs/a8_model.json.gz';old=read(op)
paths={'old':op,'floor':fin/'work/high-floor-2026-10-08/check_floor.py'};cases=[]
for label in ['EVEN','ODD']:
 cp=fin/f'work/gamma-low-2026-10-09/CERTIFICATE_{label}_gamma224_tight_4096.json';c=read(cp)
 gp=ROOT/f'work/galerkin84-2026-10-10/GALERKIN_{label}_3072.json';g=read(gp)
 paths[f'inverse_{label}']=cp;paths[f'galerkin_{label}']=gp
 ck=['F_integer_matrix','F_denominator','HB_integer_matrix','HB_denominator','old_coupling_error_norm',
     'source_c_model','source_Bh_model','source_h_gram_model','source_h_gram_upper_rational','joint_low_source_error_gram','joint_high_source_error_gram']
 gk=['old_low_c_model','old_low_Bh_model','H84_model','complete_source_high_cross_model','direct_cross_model',
     'source_model_error_norm','high_source_error_norm','old_coupling_error_norm']
 cases.append({'parity':label.lower(),'old_certificate':{k:c[k] for k in ck},'galerkin':{k:g[k] for k in gk},
  'old_raw_coupling_gram':old['parities'][label.lower()]['complete_model_raw_high_Gram']})
out={'cases':cases,'old_raw_moments':old['raw_low_moments'],
 'sources':{k:{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in paths.items()}}
(HERE/'REFINED_INPUT.json').write_text(json.dumps(out,indent=2)+'\n')
