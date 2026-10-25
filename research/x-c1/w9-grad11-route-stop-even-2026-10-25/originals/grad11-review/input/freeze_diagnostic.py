from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
H=Path(__file__).resolve().parent
src=(H/'SPECTRUM.json').read_bytes();d=json.loads(src)
grid=10**12
v=[]
for x in d['first_critical_raw_vector']:
    y=Q(str(x))*grid+Q(1,2)
    v.append(str(Q(y.numerator//y.denominator,grid)))
out={'status':'FROZEN_DIAGNOSTIC_DIRECTION_BEFORE_DIRECTED_EVALUATION',
 'selection':'Smallest generalized model eigenvector of K_model-F for the fixed published T; 12-decimal rational rounding, nearest, ties upward.',
 'source_sha256':hashlib.sha256(src).hexdigest(),'raw_coefficients':v,
 'response_changed':False,'inner_T_changed':False,'role':'diagnostic physical direction, not an optimized response',
 'claim_before_directed_evaluation':'MODEL_ONLY'}
target=H/'DIAGNOSTIC-DIRECTION.json'
if target.exists():raise RuntimeError('Refuse to overwrite frozen direction')
target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
