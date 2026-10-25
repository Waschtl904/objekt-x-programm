from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
import numpy as np
H=Path(__file__).resolve().parent
d=json.loads((H/'MODEL.json').read_bytes());m=d['matrices']
def mat(name):return np.array([[float((Q(x[0])+Q(x[1]))/2)for x in row]for row in m[name]])
def spectrum(A,G):
    L=np.linalg.cholesky(G);Li=np.linalg.inv(L)
    C=Li@A@Li.T;C=(C+C.T)/2
    vals,vec=np.linalg.eigh(C)
    return vals,np.linalg.solve(L.T,vec)
G,K,F,B,Z=[mat(n)for n in ['G_W','K_model_ONLY','F_model','basis_B','finite_Z_model']]
A=K-F;Ab=B.T@A@B;Gb=B.T@G@B
values,vectors=spectrum(A,G)
comp,cv=spectrum(Ab[2:,2:],Gb[2:,2:])
old,ov=spectrum(Ab[:2,:2],Gb[:2,:2])
S=Ab[:2,:2]-Ab[:2,2:]@np.linalg.solve(Ab[2:,2:],Ab[2:,:2])
restSchur=Ab[2:,2:]-Ab[2:,:2]@np.linalg.solve(Ab[:2,:2],Ab[:2,2:])
v=vectors[:,0]
if v[np.argmax(abs(v))]<0:v=-v
c=Q(1977,500000);beta=Q(20209999981781,182190000000000);eps=Q(1,10)
aD=float((1+eps)/(beta*(1-c)));aZ=float((1+c/eps)/(1-c))
Az=A-aZ*Z
vZ,zvec=spectrum(Az,G)
out={'status':'MODEL_DIAGNOSTIC_NOT_DIRECTED','model_sha256':hashlib.sha256((H/'MODEL.json').read_bytes()).hexdigest(),
     'gap_generalized_eigenvalues':values.tolist(),'old_block_generalized_eigenvalues':old.tolist(),
     'kernel_T_generalized_eigenvalues':comp.tolist(),'old_Schur_after_kernel':S.tolist(),
     'kernel_Schur_after_old_eigenvalues':np.linalg.eigvalsh(restSchur).tolist(),
     'first_critical_raw_vector':v.tolist(),'first_critical_basis_vector':np.linalg.solve(B,v).tolist(),
     'direction_K_model':float(v@K@v),'direction_F_model':float(v@F@v),'direction_Z_model':float(v@Z@v),
     'T_norm_spectral_model':float(np.linalg.norm(mat('T_raw'),2)),
     'diagonals_in_basis':{'K':np.diag(B.T@K@B).tolist(),'F':np.diag(B.T@F@B).tolist(),'gap':np.diag(Ab).tolist(),'Z':np.diag(B.T@Z@B).tolist()},
     'cross_block_gap':Ab[:2,2:].tolist(),'D_weight':aD,'Z_weight':aZ,
     'gap_after_Z_model_eigenvalues':vZ.tolist(),
     'max_matrix_entry_interval_radius':{k:max(float((Q(x[1])-Q(x[0]))/2)for row in m[k]for x in row)for k in ['G_W','F_model','finite_Z_model']}}
(H/'SPECTRUM.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
