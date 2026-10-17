"""Reassess old starts and screen new directions; never certify or adapt old candidates."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize

from build_k import HERE,DATA,bound


def num(x):return float(Fraction(x))


def psd(a,name):
    a=(a+a.T)/2
    vals,vecs=np.linalg.eigh(a)
    tol=1e-12*max(1,float(max(abs(vals))))
    if vals[0] < -tol:raise ValueError((name,vals[0],tol))
    return (vecs*np.maximum(vals,0))@vecs.T,{'min_eigenvalue':float(vals[0]),'max_eigenvalue':float(vals[-1]),'roundoff_clipped':int(sum(vals<0))}


def make_case(par,transport_resolution,k_resolution):
    t=json.loads((DATA/f'TRANSPORT_{par}_{transport_resolution}.json').read_text())
    k=json.loads((DATA/f'K_MAP_{par}_{k_resolution}.json').read_text())
    G=np.array(t['G_W']);L=np.linalg.cholesky(G);W=np.linalg.solve(L.T,np.eye(12))
    ell=np.array(t['I0_row'])@W
    mats={};diagnostics={}
    for key in ['common_k_gram','high_coordinate_gram','finite_feature_gram']:
        mats[key],diagnostics[key]=psd(W.T@np.array(t[key])@W,key)
    K=W.T@np.array(k['K_P_model'])@W
    K=(K+K.T)/2
    assert np.linalg.eigvalsh(K)[0]>0
    # Only the inherited model error and omitted near-zero majorant are paid here.
    # The quadrature maps remain undirected; resolution checks do not bound them.
    ek=num(t['K_model_error_upper'])+k['near_zero_W_unit_majorant_diagnostic']
    K_up=K+ek*np.eye(12)
    alpha=10*num(t['q'])/11;eps=num(t['D_model_scalar_error_upper'])
    def norm_grad(A,y):
        square=float(y@A@y)
        assert square>=-1e-11*max(1,np.linalg.norm(A,2))
        v=np.sqrt(max(0,square))
        return v,A@y/v if v>1e-25 else np.zeros(12)
    def calc(y):
        yn=np.linalg.norm(y);u=y/yn
        nk,gk=norm_grad(mats['common_k_gram'],u)
        nh,gh=norm_grad(mats['high_coordinate_gram'],u)
        nf,gf=norm_grad(mats['finite_feature_gram'],u)
        nK,gK=norm_grad(K_up,u)
        center=float(ell@u)
        radius=nk+t['high_coefficient']*nh+t['finite_feature_coefficient']*nf
        tau=np.sqrt(alpha)*nK+eps
        margin=center-radius-tau
        grad=ell-gk-t['high_coefficient']*gh-t['finite_feature_coefficient']*gf-np.sqrt(alpha)*gK
        grad=(grad-u*(u@grad))/yn
        row={'I0_midpoint':center,'coherent_radius_diagnostic':radius,'threshold_diagnostic':tau,'margin_diagnostic':margin,
             'relative_margin':margin/tau,'center_threshold_ratio':abs(center)/tau,'K_P_model':float(u@K@u),
             'k_finite_support':nk,'whole_high_support':t['high_coefficient']*nh,'finite_feature_error':t['finite_feature_coefficient']*nf,
             'coefficients':(W@u).tolist(),'whitened':u.tolist(),'physical_norm_squared':float((W@u)@G@(W@u))}
        return margin,grad,row
    # Exact formula for the MAXIMUM midpoint/energy ratio of this numerical model.
    ratio=np.sqrt(float(ell@np.linalg.solve(K,ell))/alpha)
    yratio=np.linalg.solve(K,ell);yratio/=np.linalg.norm(yratio)
    return {'calc':calc,'G':G,'W':W,'L':L,'ell':ell,'K':K,'matrices':mats,'diagnostics':diagnostics,
            'ratio_ceiling_diagnostic':float(ratio),'ratio_direction':yratio,
            'whitening_error':float(np.linalg.norm(W.T@G@W-np.eye(12),2))}


def run(par):
    hi=make_case(par,512,128);lo=make_case(par,384,64)
    old=json.loads(bound(f'research/x-c1/shell-polynomial-direction-search-2026-10-17/data/SEARCH_{par}.json'))
    frozen=json.loads(bound(f'research/x-c1/shell-polynomial-direction-search-2026-10-17/data/FROZEN_{par}.json'))
    def old_y(coeff):
        y=hi['L'].T@np.array(coeff);y/=np.linalg.norm(y)
        return -y if hi['ell']@y<0 else y
    frozen_y=old_y([num(v)for v in frozen['raw_exact_rational_coefficients']])
    baseline=hi['calc'](frozen_y)[2]
    frozen_scalar=json.loads(bound(f'research/x-c1/frozen-shell-direction-certificates-2026-10-17/expected/FROZEN_CERTIFICATE_{par}.json'))
    frozen_sharp=json.loads(bound(f'research/x-c1/sharp-kp-frozen-directions-2026-10-17/expected/SHARP_K_{par}.json'))
    calibration=max(abs(baseline['I0_midpoint']-sum(num(v)for v in frozen_scalar['I0'])/2),
                    abs(baseline['threshold_diagnostic']-sum(num(v)for v in frozen_sharp['threshold'])/2))
    if par=='even':
        coherent_ref=json.loads(bound('research/x-c1/coherent-k-frozen-even-2026-10-17/expected/COHERENT_K_EVEN.json'))
        calibration=max(calibration,abs(baseline['coherent_radius_diagnostic']-num(coherent_ref['radius_without_I0_width'][1])))
    old_rows=[]
    for r in old['all_starts']:
        row=hi['calc'](old_y(r['coefficients']))[2]
        row.update(old_start=r['start'],old_margin=r['margin_diagnostic'],old_optimizer_success=r['optimizer_success'])
        old_rows.append(row)
    old_rows.sort(key=lambda r:r['margin_diagnostic'],reverse=True)
    rng=np.random.default_rng(202610171+(par=='odd'))
    starts=[frozen_y,hi['ratio_direction'],hi['ell']/np.linalg.norm(hi['ell'])]
    starts += [old_y(r['coefficients'])for r in old['distinct_ranked_candidates']]
    for A in [hi['K'],hi['matrices']['high_coordinate_gram']]:
        _,v=np.linalg.eigh(A);starts.extend(v[:,j]for j in range(12))
    starts.extend(np.eye(12));starts.extend(rng.normal(size=(32,12)))
    rows=[]
    for idx,y in enumerate(starts):
        y=np.array(y);y/=np.linalg.norm(y)
        if hi['ell']@y<0:y=-y
        opt=minimize(lambda u:(-hi['calc'](u)[0],-hi['calc'](u)[1]),y,jac=True,method='SLSQP',
                     constraints=[{'type':'eq','fun':lambda u:float(u@u-1),'jac':lambda u:2*u}],
                     options={'maxiter':700,'ftol':1e-12})
        yy=opt.x/np.linalg.norm(opt.x)
        if hi['ell']@yy<0:yy=-yy
        _,gradient,row=hi['calc'](yy)
        # Evaluate exactly the same physical coefficients in the other resolution.
        low_y=lo['L'].T@np.array(row['coefficients'])
        low_row=lo['calc'](low_y)[2]
        spread=max(abs(row[key]-low_row[key])for key in ['I0_midpoint','coherent_radius_diagnostic','threshold_diagnostic','margin_diagnostic'])
        control_spread=max(spread,calibration)
        passed=row['margin_diagnostic']>=.01*row['threshold_diagnostic'] and low_row['margin_diagnostic']>0 and row['margin_diagnostic']>10*control_spread
        row.update(start=idx,optimizer_success=bool(opt.success),iterations=int(opt.nit),optimizer_message=str(opt.message),
                   projected_gradient_norm=float(np.linalg.norm(gradient)),resolution_spread=spread,observed_control_spread=control_spread,
                   alternate_resolution_margin=low_row['margin_diagnostic'],passes_predeclared_gate=bool(passed))
        rows.append(row)
        if idx%16==0:print(par,'start',idx,'margin',row['margin_diagnostic'],flush=True)
    rows.sort(key=lambda r:r['margin_diagnostic'],reverse=True)
    unique=[]
    for r in rows:
        if all(abs(np.dot(r['whitened'],v['whitened']))<1-1e-8 for v in unique):unique.append(r)
        if len(unique)>=8:break
    result={'status':'EXPLORATORY_NOT_DIRECTED_NO_N12_CLAIM','parity':par,'seed':202610171+(par=='odd'),
            'predeclared_gate':'margin >= 1 percent of threshold, positive at both resolutions, margin > 10 times observed scalar control spread',
            'new_starts':len(starts),'old_starts_reassessed':len(old_rows),'old_distinct_candidates':len(old['distinct_ranked_candidates']),
            'old_frozen_candidate':baseline,'old_reassessed_ranked':old_rows,'frozen_scalar_calibration_spread':calibration,
            'global_midpoint_ratio_diagnostic_128':hi['ratio_ceiling_diagnostic'],
            'global_midpoint_ratio_diagnostic_64':lo['ratio_ceiling_diagnostic'],
            'best_ratio_direction':hi['calc'](hi['ratio_direction'])[2],
            'best_margin_direction':rows[0],'distinct_ranked_candidates':unique,'all_new_starts':rows,
            'passing_starts':sum(r['passes_predeclared_gate']for r in rows),'whitening_error':hi['whitening_error'],
            'matrix_diagnostics':hi['diagnostics'],'next_directed_candidate_selected':False,
            'scope':'Only the numerical I0-centered support model on the real degree-11 shell space. No bound on an unknown high midpoint, full W9 residual energy, or all exact directions.'}
    (DATA/f'REASSESS_{par}.json').write_text(json.dumps(result,indent=2)+'\n')
    print(par,'best',rows[0]['margin_diagnostic'],'ratio ceiling',hi['ratio_ceiling_diagnostic'],'pass',result['passing_starts'],flush=True)
    return result


if __name__=='__main__':
    for par in ['even','odd']:run(par)
