"""Decision evidence only: a 12-source error bound and a 12x12 K certificate.

No pilot energy, 84/203 solve, new pairing, quadrature, or RL solve is run.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from types import MappingProxyType, ModuleType

from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
STEP = Q(13, 10**8)
GAMMA_F_CAP = Q(38072933, 125000000000000)


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def snapshot(root, binding_bytes):
    spec = json.loads(binding_bytes)
    data = {}
    for alias, entry in spec['files'].items():
        path = (root / entry['path']).resolve()
        need(path.is_relative_to(root), 'Escaping input path')
        raw = path.read_bytes()
        need(sha(raw) == entry['sha256'], 'Input binding: '+alias)
        data[alias] = raw
    common = ModuleType('bound_structural_decision_common')
    common.__file__ = str(root / spec['files']['common']['path'])
    exec(compile(data['common'], common.__file__, 'exec'), common.__dict__)
    inputs = common.Inputs(binding_bytes=data['inherited_inputs'])
    return common, inputs, MappingProxyType(data)


def ldl_positive(matrix):
    n = matrix.nrows()
    need(n == matrix.ncols(), 'Nonsquare positivity test')
    need(all(matrix[i,j].overlaps(matrix[j,i]) for i in range(n) for j in range(n)),
         'Asymmetric source enclosure')
    lower = arb_mat(n, n)
    pivots = []
    for j in range(n):
        pivot = matrix[j,j]-sum((lower[j,k]**2*pivots[k] for k in range(j)), arb(0))
        need(pivot > 0, 'Nonpositive or unresolved LDL pivot')
        pivots.append(pivot)
        lower[j,j] = 1
        for i in range(j+1, n):
            lower[i,j] = (matrix[i,j]-sum((lower[i,k]*lower[j,k]*pivots[k]
                                         for k in range(j)), arb(0)))/pivot
    return pivots


def run(root, binding_bytes):
    need(__debug__, 'Do not use python -O')
    ctx.prec = 800
    common, inputs, data = snapshot(root, binding_bytes)
    q, mat, ratmat, trace, box = common.q, common.mat, common.ratmat, common.trace, common.box
    c = inputs.json('common')['cases'][0]
    need(c['parity'] == 'even', 'Wrong parity')
    co = inputs.json('coherent')['parities']['even']
    inherited = json.loads(data['comparison_even'])
    candidate = json.loads(data['candidate_even'])
    kp = json.loads(data['kp_even'])
    need(candidate['pairs_sha256'] == sha(data['pairs_even']) == inherited['pairs_sha256'], 'Frozen pairing binding')
    need(inherited['raw_coefficients'] == candidate['raw_coefficients'], 'Frozen direction')
    need(kp['candidate_sha256'] == sha(data['candidate_even']), 'Frozen K_P direction')
    need(inherited['K_P_certificate_sha256'] == sha(data['kp_even']), 'Frozen budget binding')
    def first12(matrix):
        return arb_mat([[matrix[i,j] for j in range(12)] for i in range(12)])
    gf_rows = [row[:12] for row in c['G96_rational'][:12]]
    GF = ratmat(gf_rows)
    gpivots = ldl_positive(GF)
    U = first12(mat(c['U96_model']))
    EF = mat(c['finite_feature_error_gram'])
    need(EF.nrows() == EF.ncols() == 12, 'Finite error dimension')
    e2, tau = trace(GF.inv()*EF), trace(GF.inv()*U)
    need(e2 > 0 and tau > 0, 'Positive feature traces')
    gamma = 2*(e2*tau).sqrt()+e2
    need(gamma < q(GAMMA_F_CAP), 'Unproved finite error cap')
    K = ratmat(co['K_rational'])
    Kstar_rows = [[str(Q(co['K_rational'][i][j])+STEP*Q(gf_rows[i][j]))
                  for j in range(12)] for i in range(12)]
    Kstar = ratmat(Kstar_rows)
    # The sandwich contains all inherited direct errors. EF bounds the
    # COMPLETE finite source-feature error; no high term is removed.
    gap = first12(mat(c['D96_lower_model']))-U-q(GAMMA_F_CAP)*GF-Kstar
    gap_pivots = ldl_positive(gap)
    majorant = json.loads(data['majorant_expected'])['parities']['even']
    weights = json.loads(data['weights'])['even']
    floor = majorant['universal_P_weight_one_floor']
    inverse = inputs.json('inverse_even')
    dimensions = {}
    for key, dims in {'D96_lower_model':(96,96),'D96_upper_model':(96,96),
                      'U96_model':(96,96),'G96_rational':(96,96),
                      'finite_cross_C84_new_model':(12,84)}.items():
        rows = c[key]
        need(len(rows) == dims[0] and all(len(row) == dims[1] for row in rows), key+' dimension')
        dimensions[key] = list(dims)
    for key, dims in {'E_rational':(203,203),'X84x203_rational':(84,203),
                      'P_upper_rational':(84,84)}.items():
        rows = inverse[key]
        need(len(rows) == dims[0] and all(len(row) == dims[1] for row in rows), key+' dimension')
        dimensions[key] = list(dims)
    # Evidence about a limited U8 constant improvement, not its full effect.
    eps = Q(1,10**6)
    raw_floor = Q(6529,1000)-Q(491,200)-Q(9,4)-Q(1,500)
    ceiling = (raw_floor-16*eps-12*eps**2)/(1+eps**2)
    delta = Q(c['delta'])
    need(Q('1.82198') < ceiling, 'Proposed delta outside inherited inequality')
    high = box(inherited['component_model_energies']['high_U8'])
    direct_high_saving = high*q(1-delta/ceiling)
    summary = json.loads(data['response_summary'])['cases'][0]
    mcap = Q(summary['M_actual_normalized_upper_scalar'])
    ell = Q(summary['model_loss_generalized_eigenvalue_upper'])
    need(ell < mcap < 1, 'Stored Schur constants')
    out = {'status':'AUTHOR_DERIVED_EXTERNAL_REVIEW_OPEN',
           'source_commit':'849e4d7f6a2bde34d83c4b1acc8dd2c8213c7b50',
           'selected_pilot':'EVEN_K12_LOCAL_FEATURE_ERROR_WITH_COHERENT_SCHUR_UPDATE',
           'pilot_energy_executed':False, 'pilot_P_upper_built':False,
           'new_pairings_or_integrations':False, 'RL_computed':False,
           'frozen_response_matrix_changed':False, 'frozen_direction_changed':False,
           'K_P_changed':False, 'milestone_4_closed':False,
           'dimensions':dimensions,
           'K_preliminary_certificate':{
               'finite_feature_error_metric_trace':e2,'finite_model_metric_trace':tau,
               'gamma_F_enclosure':gamma,'gamma_F_rational_cap':str(GAMMA_F_CAP),
               'old_common96_gamma_enclosure':c['complete_energy_relative_error'],
               'K_star_definition':'K + (13/100000000) G_F',
               'step_in_G_F_metric':str(STEP),
               'K_star_canonical_rows_sha256':sha(json.dumps(Kstar_rows,separators=(',',':')).encode()),
               'G_F_positive_pivots':gpivots,'K_star_upper_gap_positive_pivots':gap_pivots,
               'positive_pivot_counts':[12,12],
               'relative_increment_trace_upper':(q(STEP)*trace(ratmat(co['K_inverse_rational'])*GF)).upper(),
               'energy_improvement_magnitude_certified':False},
           'existing_even_decision_scales':{
               'old_partial_energy':inherited['partial_actual_energy_interval'],
               'K_P_interval':kp['K_P_interval'],
               'scalar_family_floor_gap':floor['lower_energy_minus_budget_upper'],
               'same_dual_sharper_P_gap':majorant['variants']['same_dual_sharper_P']['lower_energy_minus_budget_upper'],
               'partial_model_energy_radius':box(inherited['partial_model_energy']).rad(),
               'a_fin_relative_error_upper':weights['a_fin_relative_error_upper']},
           'U8_limited_constant_headroom':{
               'delta_old':str(delta),'delta_candidate':str(Q('1.82198')),
               'ceiling_from_same_analytic_estimate':str(ceiling),
               'direct_high_model_energy_saving_at_ceiling':direct_high_saving,
               'is_bound_on_full_comparison_improvement':False},
           'Schur_existing_scalar_diagnostics':{
               'M_upper_relative_D':str(mcap),'model_loss_upper':str(ell),
               'difference_over_old_gap':str((mcap-ell)/(1-mcap)),
               'is_new_directional_energy_certificate':False},
           'candidate_sha256':sha(data['candidate_even']),
           'K_P_certificate_sha256':sha(data['kp_even'])}
    return common.encode(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repository', type=Path)
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    need(__debug__, 'Do not use python -O')
    need(args.check or args.output, 'Specify --check or --output')
    checked = {}
    if args.check:
        for name, digest in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            path = (HERE/name).resolve()
            need(path.is_relative_to(HERE), 'Escaping package path')
            raw = path.read_bytes()
            need(sha(raw) == digest, 'Package binding: '+name)
            checked[name] = raw
    else:
        checked['INPUT_BINDINGS.json'] = (HERE/'INPUT_BINDINGS.json').read_bytes()
    root = (args.repository if args.repository is not None else HERE.parents[2]).resolve()
    raw = (json.dumps(run(root, checked['INPUT_BINDINGS.json']),indent=2)+'\n').encode()
    if args.check:
        need(raw == checked['EXPECTED.json'], 'Decision evidence replay differs')
        print('PASS: decision evidence byte-equal; K admissibility only, pilot energy not run')
    if args.output:
        args.output.write_bytes(raw)


if __name__ == '__main__':
    main()
