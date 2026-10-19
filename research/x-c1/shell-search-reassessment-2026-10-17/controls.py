"""Resolution, inherited-certificate and whole-space numerical diagnostics."""
import json
from fractions import Fraction

import numpy as np
from scipy.optimize import minimize_scalar

from build_k import HERE, DATA, bound


def num(v):return float(Fraction(v))


def main():
    results={}
    for par in ('even','odd'):
        maps=[json.loads((DATA/f'K_MAP_{par}_{n}.json').read_text())for n in (64,128)]
        transports=[json.loads((DATA/f'TRANSPORT_{par}_{n}.json').read_text())for n in (384,512)]
        search=json.loads((DATA/f'REASSESS_{par}.json').read_text())
        t=transports[1];G=np.array(t['G_W']);W=np.linalg.inv(np.linalg.cholesky(G)).T
        K=np.array(maps[1]['K_P_model']);alpha=10*num(t['q'])/11
        deltaK=float(np.linalg.norm(W.T@(K-np.array(maps[0]['K_P_model']))@W,2))
        assert deltaK<1e-9
        assert max(abs(x['checks']['frozen_K_difference'])for x in maps)<1e-9
        guard=[]
        for resolution,tt,kk in zip((64,128),transports,maps):
            A=np.array(kk['K_P_model'])-num(tt['K_model_error_upper'])*G
            S=np.linalg.inv(np.linalg.cholesky(A)).T
            ell=np.array(tt['I0_row'])@S/np.sqrt(alpha)
            B=tt['high_coefficient']**2/alpha*(S.T@np.array(tt['high_coordinate_gram'])@S)
            def majorant(logt):
                weight=np.exp(logt)
                return float(np.sqrt(np.linalg.eigvalsh((1+weight)*np.outer(ell,ell)+(1+1/weight)*B)[-1]))
            opt=minimize_scalar(majorant,bounds=(-12,12),method='bounded')
            weight=float(format(np.exp(opt.x),'.12g'))
            # Choose one positive rational weight. It need not be an exact minimizer.
            extra=np.sqrt(np.linalg.eigvalsh(S.T@np.array(tt['common_k_gram'])@S)[-1]/alpha)
            extra+=tt['finite_feature_coefficient']*np.sqrt(np.linalg.eigvalsh(S.T@np.array(tt['finite_feature_gram'])@S)[-1]/alpha)
            extra+=num(tt['D_model_scalar_error_upper'])*np.sqrt(np.linalg.eigvalsh(S.T@G@S)[-1]/alpha)
            total=majorant(np.log(weight))+extra
            # Sensitivity only: this 1e-10 perturbation is NOT a certified error bound.
            stress=A-1e-10*G;SS=np.linalg.inv(np.linalg.cholesky(stress)).T
            ll=np.array(tt['I0_row'])@SS/np.sqrt(alpha)
            BB=tt['high_coefficient']**2/alpha*(SS.T@np.array(tt['high_coordinate_gram'])@SS)
            stress_extra=np.sqrt(np.linalg.eigvalsh(SS.T@np.array(tt['common_k_gram'])@SS)[-1]/alpha)
            stress_extra+=tt['finite_feature_coefficient']*np.sqrt(np.linalg.eigvalsh(SS.T@np.array(tt['finite_feature_gram'])@SS)[-1]/alpha)
            stress_extra+=num(tt['D_model_scalar_error_upper'])*np.sqrt(np.linalg.eigvalsh(SS.T@G@SS)[-1]/alpha)
            stress_total=float(np.sqrt(np.linalg.eigvalsh((1+weight)*np.outer(ll,ll)+(1+1/weight)*BB)[-1])+stress_extra)
            guard.append({'K_resolution':resolution,'positive_weight_rational':str(Fraction(str(weight))),
                          'whole_space_support_ratio_upper_diagnostic':total,'margin_to_one_diagnostic':1-total,
                          'stress_K_minus_1e_minus_10_G_ratio':stress_total})
        ref=json.loads(bound(f'research/x-c1/frozen-shell-direction-certificates-2026-10-17/expected/FROZEN_CERTIFICATE_{par}.json'))
        row=search['old_frozen_candidate']
        icenter=sum(num(v)for v in ref['I0'])/2
        assert abs(row['I0_midpoint']-icenter)<1e-8
        results[par]={'K_resolution_W_operator_difference':deltaK,'K_frozen_reference_differences':[m['checks']['frozen_K_difference']for m in maps],
                      'old_frozen_I0_difference':row['I0_midpoint']-icenter,
                      'global_midpoint_ratio_64':search['global_midpoint_ratio_diagnostic_64'],
                      'global_midpoint_ratio_128':search['global_midpoint_ratio_diagnostic_128'],
                      'whole_space_support_guard_diagnostic':guard,'certified_whole_space_result':False}
        if par=='even':
            prior=json.loads(bound('research/x-c1/coherent-k-frozen-even-2026-10-17/expected/COHERENT_K_EVEN.json'))
            radius=num(prior['radius_without_I0_width'][1])
            results[par]['old_frozen_common_radius_difference']=row['coherent_radius_diagnostic']-radius
            assert abs(row['coherent_radius_diagnostic']-radius)<1e-7
    out={'status':'EXPLORATORY_NOT_DIRECTED','data':results,'new_certification_triggered':False,
         'warning':'No quadrature enclosure for the full matrices. Resolution, calibration and sensitivity tests are not certified error bounds.'}
    (DATA/'CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
    return out


if __name__=='__main__':main()
