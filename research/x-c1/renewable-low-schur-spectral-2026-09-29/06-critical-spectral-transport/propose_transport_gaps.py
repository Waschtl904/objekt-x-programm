"""Float proposals for whole-high parameter-dependent Schur gap certificates.

No eigenvalues/eigenvectors are computed. Every successful Cholesky remains
only a proposal until the separate integer-interval replay passes.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json
import numpy as np
from scipy.linalg import solve_triangular

CASES = {'A9': ('research/x-c1/chambers-through-a11-2026-09-28/a9',6,F(2,3)),
         'A11': ('research/x-c1/chambers-through-a11-2026-09-28/a11',8,F(1))}

def main():
    p=argparse.ArgumentParser()
    for k in ('repo','vectors','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();vec=json.loads(a.vectors.read_bytes());den=10**100;scale=10**16
    results={};sources={}
    for name,(rel,rank,delta) in CASES.items():
        folder=a.repo/rel
        def read(filename,zipped=False):
            raw=(folder/filename).read_bytes();sources[rel+'/'+filename]=hashlib.sha256(raw).hexdigest()
            return json.loads(gzip.decompress(raw) if zipped else raw)
        model=read(name.lower()+'_model.json.gz',True)
        receipt=read('reserve_results.json')
        lower=read('reserve_results_lower_matrices.json.gz',True)
        for parity in ('even','odd'):
            key=name+'-'+parity;rows=lower['parities'][parity]['lower_matrix'];n=len(rows)
            decode=lambda rows:np.array([[float(F(int(x[0])+int(x[1]),2*den)) for x in row] for row in rows])
            fm=decode(rows)
            hup=decode(model['parities'][parity]['complete_model_raw_high_Gram'])*1.001
            eb=F(receipt['parities'][parity]['coupling_operator_error_exact'])
            hup+=np.eye(n)*float(1001*eb*eb)
            v=np.array([[float(vec[key+'-'+str(j+1)]['coefficients'][i]) for j in range(rank)] for i in range(n)])
            # Search only a scalar cut; the preexisting trial columns stay fixed.
            def repair(mu):
                t=float(F(1003,1000))*mu;d=float(delta)
                return fm-t*np.eye(n)-t/(d*(d-t))*hup+v@v.T
            lo,hi=0.,min(.4,float(delta)/2)
            for _ in range(32):
                mid=(lo+hi)/2
                try:
                    x=repair(mid);np.linalg.cholesky((x+x.T)/2);lo=mid
                except np.linalg.LinAlgError:hi=mid
            # Safe rational proposal 5% below float transition, rounded down.
            mu=F(int(lo*.95*10**6),10**6)
            x=repair(float(mu));r=np.linalg.cholesky((x+x.T)/2).T
            t=solve_triangular(r,np.eye(n),lower=False)
            def grid(x):return [[str(int(round(float(x[i,j])*scale))) if j>=i else '0' for j in range(n)] for i in range(n)]
            results[key]={'rank':rank,'delta_exact':str(delta),'physical_gap_cut_exact':str(mu),
                          'rho_exact':'1003/1000','R_upper_grid':grid(r),'T_upper_grid':grid(t),
                          'float_proposal_boundary':lo}
            print(key,'proposed physical gap',str(mu),'float repair transition',lo,flush=True)
    out={'status':'PROPOSAL_ONLY_REQUIRES_INTEGER_REPLAY','factor_scale':str(scale),
         'source_sha256':sources,'vectors_sha256':hashlib.sha256(a.vectors.read_bytes()).hexdigest(),'results':results}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_bytes(gzip.compress((json.dumps(out,separators=(',',':'))+'\n').encode(),mtime=0))

if __name__=='__main__':main()
