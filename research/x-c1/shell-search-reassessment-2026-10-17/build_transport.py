"""Numerical degree-11 maps with the single-k transport of #235.

The inherited quadrature maps are undirected. Directed source constants do not
turn the assembled maps or their optimization into a certificate.
"""
import gzip
import io
import json
import sys
import zipfile
from fractions import Fraction
from pathlib import Path

import numpy as np
from flint import arb, arb_mat, ctx

from build_k import HERE, DATA, bound, member, q
ROOT = HERE.parents[2]
ORIGINAL = 'research/x-c1/nstar-jp-spike-orthogonality-2026-10-16/original/'


def box(v):
    return q(v[0]).union(q(v[1]))


def mat(rows):
    return arb_mat([[box(v) for v in row] for row in rows])


def trace(a):
    return sum((a[i,i] for i in range(a.nrows())),arb(0))


def matrix(a):
    return [[float(a[i,j].mid()) for j in range(a.ncols())] for i in range(a.nrows())]


def load(path):
    return json.loads(bound(path))


def build(par, resolution):
    ctx.prec = 800
    sigma = int(par=='odd')
    bind = json.loads((HERE/'INPUT_BINDINGS.json').read_text())
    with zipfile.ZipFile(io.BytesIO(bound(bind['stage3_archive']))) as z:
        def prepared(name):
            raw = member(z,'inputs/'+name)
            import hashlib
            assert hashlib.sha256(raw).hexdigest()==bind['prepared_sha256'][name]
            return json.loads(gzip.decompress(raw))['cases'][sigma]
        raw, common = prepared('REFINED_INPUT.json.gz'),prepared('REFINED_COMMON96.json.gz')
    d=load(f'research/x-c1/shell-polynomial-direction-search-2026-10-17/data/MAPS_{par}_{resolution}.json')
    coherent=load(ORIGINAL+'gpt2-kp-und-kohaerenter-transport/expected/COHERENT_TRANSPORT_INPUTS.json')['parities'][par]['directions']['p']
    high=load(ORIGINAL+'gpt2-stufe4-hochantwort/expected/COMPLETE_HIGH_RESPONSE.json')[par]
    hp=high['directions']['lower_Pv']
    finite=load(ORIGINAL+'gpt2-stufe3-endliche-u8-antwort/expected/FINITE_ACTION.json')[par]['directions']['lower_Pv']
    C=arb_mat([[arb(int(v))/int(common['inverse_congruence_denominator']) for v in row]for row in common['inverse_congruence_integer_matrix']])
    G=arb_mat([[q(v)for v in row]for row in coherent['metric_G_equals_eta_squared_K_inverse']])
    delta,rho=q(common['delta']),q(common['rho'])
    lowF=mat(raw['old_certificate']['source_c_model']);B_yF=mat(raw['old_certificate']['source_Bh_model'])
    V_F=C.transpose()*(lowF-B_yF/delta);C_F=C*V_F/(1-rho)
    CP=arb_mat([[q(str(v))for v in row]for row in d['feature_factor']])
    Bf=arb_mat([[q(str(v))for v in row]for row in d['b_F']])
    # Recover Phi* h from C* Phi* h using high-precision arithmetic. The
    # stored doubles remain undirected inputs, not exact physical data.
    Phi=C.transpose().solve(CP)
    reconstruction = C.transpose()*Phi-CP
    assert all(reconstruction[i,j].contains(0)for i in range(191)for j in range(12))
    a=Bf-V_F.transpose()*CP/(1-rho)
    common_k=a.transpose()*G*a
    H_F=mat(raw['old_certificate']['source_h_gram_model']);G0=mat(raw['old_raw_coupling_gram'])/10**100
    R_F=H_F-B_yF.transpose()*C_F-C_F.transpose()*B_yF+C_F.transpose()*G0*C_F
    traceGR=trace(G*R_F);assert traceGR>0
    EF=mat(common['finite_feature_error_gram']);EH=mat(raw['old_certificate']['joint_high_source_error_gram'])
    eF=trace(G*EF).sqrt();ey=trace(G*EH).sqrt()
    eB=q(raw['old_certificate']['old_coupling_error_norm'][1]);J=q(high['tr_X_HB'][1]).sqrt()
    ec=eB*trace(G*(C_F.transpose()*C_F)).sqrt()
    c0=arb_mat([[box(v)]for v in finite['c_model']]);efixed=q(finite['fixed_k_feature_error_bound'][1])
    fixed_r=box(hp['full_model_high_difference_norm_squared']).sqrt()+q(hp['y_fixed_k_error_upper'][1])+eB*(c0.transpose()*c0)[0,0].sqrt()+J*efixed
    high_coeff=(fixed_r+traceGR.sqrt()+ey+ec+J*eF)/delta
    feature_coeff=(efixed+eF)/(1-rho).sqrt()
    H8=arb_mat([[q(str(v))for v in row]for row in d['H8_gram']])
    high_gram=q(high['full_M_norm_squared'][1])*H8-Phi.transpose()*Phi
    out={'status':'EXPLORATORY_NOT_DIRECTED','parity':par,'inherited_resolution':resolution,
         'G_W':d['G_W'],'I0_row':d['I0_row'],'common_k_gram':matrix(common_k),
         'high_coordinate_gram':matrix(high_gram),'finite_feature_gram':matrix(CP.transpose()*CP),
         'high_coefficient':float(high_coeff.upper()),'finite_feature_coefficient':float(feature_coeff.upper()),
         'q':d['q'],'D_model_scalar_error_upper':d['D_model_scalar_error_upper'],'K_model_error_upper':d['K_model_error_upper'],
         'fixed_high_coordinate_r_bound':float(fixed_r.upper()),'common_k_high_HS_bound':float(traceGR.sqrt().upper()),
         'scope':'One k ellipsoid; numerical Phi recovered from stored C*Phi maps. No directed integration remainder claimed.'}
    DATA.mkdir(exist_ok=True,parents=True)
    (DATA/f'TRANSPORT_{par}_{resolution}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(par,resolution,'high coeff',out['high_coefficient'],'feature coeff',out['finite_feature_coefficient'],flush=True)
    return out


if __name__=='__main__':
    build(sys.argv[1],int(sys.argv[2]))
