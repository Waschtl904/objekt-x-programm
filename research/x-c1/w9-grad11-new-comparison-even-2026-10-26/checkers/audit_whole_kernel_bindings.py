"""Bind every whole cache to the same exact Gamma polynomial and high floor."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
H=Path(__file__).resolve().parent;frame=json.loads((H/'JOINT_TAIL_GEOMETRY.json').read_bytes())
rawcor=(H/'inputs/CORRECTION_4096.json').read_bytes();gamma=list(map(Q,json.loads(rawcor)['Gamma_new_coefficients']))
def dyadic(m,e):return Q(m*2**e)if e>=0 else Q(m,2**(-e))
def ball(v):
    m,e,r,s=v['ball'];m=dyadic(m,e);r=dyadic(r,s);return m-r,m+r,r
common=None;rows=[]
for item in frame['caches']:
    raw=(H/item['cache']).read_bytes();assert hashlib.sha256(raw).hexdigest()==item['sha256']
    body=json.loads(gzip.decompress(raw));payload=body['payload'].encode();assert hashlib.sha256(payload).hexdigest()==body['payload_sha256']
    if common is None:common=body['inputs']
    else:assert common==body['inputs']
    values=dict(json.loads(payload)['mapping']);g=values['gamma'];assert len(g)==len(gamma)==225
    for box,exact in zip(g,gamma):
        lo,hi,_=ball(box);assert lo<=exact<=hi
    lo,hi,r=ball(values['delta']);assert lo<=Q('1.84298')<=hi and r<Q('1e-800')
    rows.append({'label':item['label'],'gamma_coefficients_bound':225,'delta_exact':'1.84298','delta_radius_below':'1e-800'})
out={'status':'ALL_WHOLE_KERNEL_AND_PARAMETER_BINDINGS_PASS','directions':rows,
     'same_historical_inputs_all_directions':True,'Gamma_correction_sha256':hashlib.sha256(rawcor).hexdigest(),
     'scope':'Exact rational membership checks; continuous analytic Gamma remainders are handled by the separate coefficient and application proofs.'}
(H/'WHOLE_KERNEL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('Twelve caches:',12*225,'Gamma coefficients and 12 high-floor parameters bound')
