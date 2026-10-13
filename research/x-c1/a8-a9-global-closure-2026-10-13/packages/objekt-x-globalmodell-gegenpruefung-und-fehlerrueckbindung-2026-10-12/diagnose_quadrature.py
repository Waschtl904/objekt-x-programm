"""Recompute numerical quadrature diagnostics in the fixed directional metric.

This is NOT a quadrature-error or global-Gram certificate.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys
import numpy as np
from scipy.linalg import eigh
def read(p):return json.loads(p.read_bytes())
def main(pkg,inputs,points,out):
    from flint import arb,arb_mat,ctx
    ctx.prec=768
    def af(v):
        q=F(v);return arb(q.numerator)/q.denominator
    def mat(a):return arb_mat([[af(z) for z in row] for row in a])
    direction=read(pkg/'data/DIRECTIONAL_DERIVATIVE_TARGET.json');data=read(inputs)
    G=mat(direction['full_log_tail_Gram_rational_upper_3x3']);results=[]
    for i,label in enumerate(['EVEN','ODD']):
        r=data['cases'][i];d=direction['cases'][i];rho=af(r['rho']);K=mat(r['K12_new_rational'])
        D=arb_mat([[1-rho if j==k and j<191 else K[j-191,k-191] if j>=191 and k>=191 else 0 for k in range(203)] for j in range(203)])
        T=af(r['beta'])*(D-mat(r['M_upper_rational']));C=mat(d['coefficient_midpoints_3x203'])
        H=(af(d['derivative_target_coefficient_T'])*T-af(d['derivative_target_subtracted_coefficient_D'])*D-af(d['derivative_target_subtracted_coefficient_CtGC'])*C.transpose()*G*C)/10920
        L=[[arb(0) for _ in range(12)] for _ in range(12)]
        for j in range(12):
            for k in range(j+1):
                z=K[j,k]-sum((L[j][n]*L[k][n] for n in range(k)),arb(0));L[j][k]=z.sqrt() if j==k else z/L[k][k]
        Wi=arb_mat(L).transpose().inv()
        W=arb_mat([[1/(1-rho).sqrt() if j==k and j<191 else Wi[j-191,k-191] if j>=191 and k>=191 else 0 for k in range(203)] for j in range(203)])
        HD=W.transpose()*H*W
        assert max(float(HD[j,k].rad()) for j in range(203) for k in range(203))<1e-60
        hh=np.array([[float(HD[j,k].mid()) for k in range(203)] for j in range(203)]);hh=(hh+hh.T)/2
        group=[]
        for order in [128,256]:
            npz=points/f'EXPLORATORY_{label}_{order}.npz'
            if not npz.exists():continue
            v=np.load(npz);u=v['nodes'];ws=v['weights'];y=v['values'];t=2*u-1
            V=np.polynomial.legendre.legvander(t,103)*np.sqrt(2*np.arange(104)+1)
            coefficients=V.T@(ws[:,None]*y)
            rem=y-V@coefficients;gram=rem.T@(ws[:,None]*rem)
            want=v['gram'];assert np.max(np.abs(gram-want))<1e-15
            vals=eigh(gram,hh,eigvals_only=True)
            rec={'order':order,'weighted_sample_matrix_largest_eigenvalue_relative_to_H':float(vals[-1]),
                 'percent_of_H_numerical_only':float(100*vals[-1]),
                 'trace_relative_to_D_numerical_only':float(np.trace(gram)),
                 'max_eigenvalue_relative_to_D_numerical_only':float(np.linalg.eigvalsh(gram)[-1]),
                 'quadrature_error_included':False,'whole_interval_upper_bound':False}
            group.append(rec);print(label,rec,flush=True)
        results.append({'parity':label.lower(),'quadratures':group,
             'model_Gram_upper_certified':False,'physical_model_error_certified':False})
    out.write_text(json.dumps({'status':'NUMERICAL_DIAGNOSTIC_ONLY_NO_GLOBAL_UPPER_BOUND','cases':results,
         'full_remainder_certified':False,'tail_floor_1_over_20_certified':False},indent=2)+'\n')
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for key in ['package','inputs','points','out']:ap.add_argument('--'+key,type=Path,required=True)
    x=ap.parse_args();main(x.package,x.inputs,x.points,x.out)
