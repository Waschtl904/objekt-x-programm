"""Float arithmetic proposes rational factors only; the integer replay proves.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json
import numpy as np
from scipy.linalg import solve_triangular
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
p.add_argument('--vectors',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
source=a.repo/'research/x-c1/chambers-through-a11-2026-09-28/a11/reserve_results_lower_matrices.json.gz'
raw=source.read_bytes();data=json.loads(gzip.decompress(raw));vectors=json.loads(a.vectors.read_bytes())
den=10**100;scale=10**16;out={}
for parity in ('even','odd'):
    rows=data['parities'][parity]['lower_matrix'];n=len(rows)
    fm=np.array([[float(F(int(x[0])+int(x[1]),2*den)) for x in row] for row in rows])
    v=np.array([[float(vectors['A11-'+parity+'-'+str(j+1)]['coefficients'][i]) for j in range(8)] for i in range(n)])
    repaired=fm-np.eye(n)/500+v@v.T
    r=np.linalg.cholesky((repaired+repaired.T)/2).T
    t=solve_triangular(r,np.eye(n),lower=False)
    def grid(x):return [[str(int(round(float(x[i,j])*scale))) if j>=i else '0' for j in range(n)] for i in range(n)]
    out[parity]={'R_upper_grid':grid(r),'T_upper_grid':grid(t)}
    print(parity,'rational factors proposed',flush=True)
result={'status':'PROPOSAL_ONLY_REQUIRES_INTEGER_REPLAY','cut_exact':'1/500','rank':8,
        'factor_scale':str(scale),'source_F_sha256':hashlib.sha256(raw).hexdigest(),
        'source_vectors_sha256':hashlib.sha256(a.vectors.read_bytes()).hexdigest(),'parities':out}
a.out.parent.mkdir(parents=True,exist_ok=True)
a.out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
