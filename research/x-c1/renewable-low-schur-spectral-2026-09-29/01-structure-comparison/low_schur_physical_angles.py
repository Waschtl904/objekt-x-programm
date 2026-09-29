"""Exploratory physical overlaps of stored diagnostic eigenvectors.

Zero extension is integrated on the smaller physical interval. This is
ordinary floating-point geometry, never a positivity certificate.
"""
from pathlib import Path
import argparse,json,math
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
data=json.loads(a.input.read_bytes())
def coeffs(v):
    c=np.zeros(max(v['degrees'])+1)
    c[v['degrees']]=np.array(v['coefficients'],dtype=float)*np.sqrt(2*np.array(v['degrees'])+1)
    parity=int(v['parity']=='odd');c[parity]=float(v['carrier_coefficient'])*math.sqrt(2*parity+1)
    return c
def gram(vs):
    x=np.array([v['coefficients'] for v in vs],dtype=float)
    carrier=np.array([float(v['carrier_coefficient']) for v in vs])
    return x@x.T+np.outer(carrier,carrier)
def invsqrt(g):
    vals,vecs=np.linalg.eigh(g);assert vals.min()>0
    return (vecs/np.sqrt(vals))@vecs.T
results={}
for parity in ('even','odd'):
  for left,right in [('A8','A9'),('A9','A11'),('A8','A11')]:
    vs=[[data[f'{name}-{parity}-{i}'] for i in (1,2,3)] for name in (left,right)]
    rho=vs[0][0]['endpoint']/vs[1][0]['endpoint'];g0,g1=map(gram,vs)
    records=[]
    for nodes in (640,704):
      x,w=np.polynomial.legendre.leggauss(nodes)
      f0=np.array([np.polynomial.legendre.legval(x,coeffs(v)) for v in vs[0]])
      f1=np.array([np.polynomial.legendre.legval(rho*x,coeffs(v)) for v in vs[1]])
      overlap=math.sqrt(rho)/2*(f0*w)@f1.T
      whitened=invsqrt(g0)@overlap@invsqrt(g1)
      sv=np.linalg.svd(whitened,compute_uv=False)
      new_inside=rho/2*((f1*f1)*w).sum(axis=1)/np.diag(g1)
      records.append({'nodes':nodes,'physical_overlap_first_direction':float(abs(overlap[0,0])/math.sqrt(g0[0,0]*g1[0,0])),
        'three_mode_principal_cosines':sv.tolist(),'new_mode_mass_outside_old_support':(1-new_inside).tolist(),
        'overlap_matrix':overlap.tolist()})
    assert np.max(np.abs(np.array(records[0]['overlap_matrix'])-records[1]['overlap_matrix']))<1e-10
    results[left+'->'+right+'-'+parity]={'status':'FLOATING_POINT_DIAGNOSTIC','quadrature_comparison':records}
a.output.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:{'overlap':v['quadrature_comparison'][-1]['physical_overlap_first_direction'],
  'principal_cosines':v['quadrature_comparison'][-1]['three_mode_principal_cosines'],
  'shell_mass':v['quadrature_comparison'][-1]['new_mode_mass_outside_old_support']} for k,v in results.items()},indent=2))
