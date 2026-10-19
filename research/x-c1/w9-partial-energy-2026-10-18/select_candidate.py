"""Exploratory generalized eigenvector, frozen BEFORE its directed K_P run."""
import argparse
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from flint import ctx
from common import Inputs,box,need
from assemble import Energy,load_pairs


def floats(A):
    return np.array([[float(A[i,j].mid())for j in range(A.ncols())]for i in range(A.nrows())])


def main():
    ap=argparse.ArgumentParser();ap.add_argument('pairs',type=Path);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();ctx.prec=800;inp=Inputs();data=load_pairs(args.pairs);energy=Energy(inp,data)
    E=floats(energy.total);G=floats(energy.G)
    K=np.array(inp.json('kp_model_'+data['parity'])['K_P_model'])
    values,vectors=eigh((E+E.T)/2,(K+K.T)/2)
    candidates=[('generalized_eigenvector_'+str(j),vectors[:,j])for j in range(12)]
    candidates+=[('sum_top_two',vectors[:,-1]+vectors[:,-2]),
                 ('difference_top_two',vectors[:,-1]-vectors[:,-2]),
                 ('z0',np.eye(12)[0]),
                 ('previous_frozen',np.array([float(Fraction(v))
                    for v in inp.json('old_candidate_'+data['parity'])['raw_exact_rational_coefficients']]))]
    ranking=[]
    for name,c in candidates:
        c=c/np.sqrt(c@G@c)
        if c[np.argmax(np.abs(c))]<0:c=-c
        # Each candidate's coefficients are exact decimal rationals. The
        # partial error is already included in its lower energy; the K model
        # denominator remains exploratory until the separate K_P certificate.
        raw=[format(v,'.17g')for v in c]
        tested=energy.certificate(raw,'7400911/250000',name)
        lower=float(Fraction(tested['partial_actual_energy_interval'][0]))
        kmid=float(c@K@c);need(kmid>0,'Positive exploratory K model')
        ranking.append({'name':name,'raw_coefficients':raw,'model_energy':float(c@E@c),
                        'model_K_P':kmid,'partial_energy_lower_for_ranking':lower,
                        'error_adjusted_exploratory_ratio':lower/kmid,
                        'model_W_norm_squared':float(c@G@c)})
    ranking.sort(key=lambda item:item['error_adjusted_exploratory_ratio'],reverse=True)
    best=ranking[0];raw=best['raw_coefficients']
    result={'status':'EXPLORATORY_CANDIDATE_FROZEN_NOT_A_CERTIFICATE','parity':data['parity'],
            'pairs_sha256':data['_source_sha256'],
            'raw_coefficients':raw,'model_generalized_eigenvalues':values.tolist(),
            'selected_candidate':best['name'],'ranking':ranking,
            'model_energy':best['model_energy'],'model_K_P':best['model_K_P'],
            'model_W_norm_squared':best['model_W_norm_squared'],
            'selection_includes_partial_error':True,'K_model_is_certified':False,
            'new_rule_selected':False,'N12_closed':False}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(data['parity'],'partial/K model maximum',values[-1],flush=True)


if __name__=='__main__':main()
