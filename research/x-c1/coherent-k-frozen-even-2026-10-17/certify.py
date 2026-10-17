"""Single-ellipsoid k transport for the fixed even candidate, using whole Grams.

No new operator quadrature, high-mode truncation, or numerical high midpoint.
The remaining high support is bounded by a Hilbert--Schmidt norm.
"""
import gzip
import hashlib
import io
import json
import zipfile
from fractions import Fraction
from pathlib import Path

from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ORIGINAL = 'research/x-c1/nstar-jp-spike-orthogonality-2026-10-16/original/'
FROZEN = 'research/x-c1/frozen-shell-direction-certificates-2026-10-17/'
SHARP = 'research/x-c1/sharp-kp-frozen-directions-2026-10-17/'


def q(value):
    value = Fraction(value)
    return arb(value.numerator) / value.denominator


def box(pair):
    assert Fraction(pair[0]) <= Fraction(pair[1])
    return q(pair[0]).union(q(pair[1]))


def mat(rows):
    return arb_mat([[box(value) for value in row] for row in rows])


def col(values):
    return arb_mat([[box(value)] for value in values])


def trace(matrix):
    assert matrix.nrows() == matrix.ncols()
    return sum((matrix[i, i] for i in range(matrix.nrows())), arb(0))


def enc(value):
    assert value.is_finite()
    return [str(value.lower().fmpq()), str(value.upper().fmpq())]


def intersect(a, b):
    assert (a.nrows(), a.ncols()) == (b.nrows(), b.ncols())
    for i in range(a.nrows()):
        for j in range(a.ncols()):
            assert a[i, j].overlaps(b[i, j]), (i, j)
    return a.nrows() * a.ncols()


def main(output=None):
    if not __debug__:
        raise RuntimeError('Run the certificate without python -O')
    ctx.prec = 800
    bindings = json.loads((HERE / 'INPUT_BINDINGS.json').read_text())
    def read_bytes(name):
        assert name in bindings['repository_files'], name
        raw = (ROOT / name).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == bindings['repository_files'][name], name
        return raw
    def load(name):
        return json.loads(read_bytes(name))
    # Check all proof and source bindings as well as the files actually parsed.
    for name in bindings['repository_files']:
        read_bytes(name)
    with zipfile.ZipFile(io.BytesIO(read_bytes(bindings['stage3_archive']))) as archive:
        def prepared(name):
            paths = [p for p in archive.namelist() if p.endswith('/inputs/' + name)]
            assert len(paths) == 1
            raw = archive.read(paths[0])
            assert hashlib.sha256(raw).hexdigest() == bindings['prepared_sha256'][name]
            return json.loads(gzip.decompress(raw))['cases'][0]
        raw = prepared('REFINED_INPUT.json.gz')
        common = prepared('REFINED_COMMON96.json.gz')
    old = load(FROZEN + 'expected/FROZEN_CERTIFICATE_even.json')
    projected = load(SHARP + 'expected/PROJECTED_HIGH_even.json')
    sharp = load(SHARP + 'expected/SHARP_K_even.json')
    frozen_path = 'research/x-c1/shell-polynomial-direction-search-2026-10-17/data/FROZEN_even.json'
    assert old['candidate_sha256'] == sharp['candidate_sha256'] == projected['candidate_sha256'] == bindings['repository_files'][frozen_path]
    assert projected['inherited_scalar_sha256'] == sharp['inherited_scalar_sha256'] == bindings['repository_files'][FROZEN + 'expected/FROZEN_CERTIFICATE_even.json']
    high = load(ORIGINAL + 'gpt2-stufe4-hochantwort/expected/COMPLETE_HIGH_RESPONSE.json')['even']
    hp = high['directions']['lower_Pv']
    finite = load(ORIGINAL + 'gpt2-stufe3-endliche-u8-antwort/expected/FINITE_ACTION.json')['even']['directions']['lower_Pv']
    psi = load(ORIGINAL + 'gpt1-stufe1-zertifikat/expected/PSI_CORRECTED.json')['data']['even']['directions']['lower_Pv']
    coherent = load(ORIGINAL + 'gpt2-kp-und-kohaerenter-transport/expected/COHERENT_TRANSPORT_INPUTS.json')['parities']['even']
    direction = coherent['directions']['p']
    assert psi['k_model_exact'] == direction['fixed_k0_rational']
    assert 'psi_actual-psi_model=-F*(k_actual-k_model)' in psi['analytic_function_error_structure']
    K = [[Fraction(v) for v in row] for row in coherent['K_rational']]
    Ki = [[Fraction(v) for v in row] for row in coherent['K_inverse_rational']]
    assert len(K) == len(Ki) == 12 and all(len(r) == 12 for r in K + Ki)
    assert all(K[i][j] == K[j][i] for i in range(12) for j in range(12))
    assert all(sum(K[i][k] * Ki[k][j] for k in range(12)) == int(i == j) for i in range(12) for j in range(12))
    # Exact LDL pivots establish positivity independently of rounded eigenvalues.
    work = [row[:] for row in K]
    pivots = []
    for k in range(12):
        pivot = work[k][k]
        assert pivot > 0
        pivots.append(str(pivot))
        for i in range(k + 1, 12):
            for j in range(k + 1, 12):
                work[i][j] -= work[i][k] * work[k][j] / pivot
    eta = Fraction(direction['eta_K_norm_upper'])
    assert eta > 0 and Fraction(psi['actual_k_minus_kmodel_K_norm_upper'][1]) <= eta
    metric = [[Fraction(v) for v in row] for row in direction['metric_G_equals_eta_squared_K_inverse']]
    assert all(metric[i][j] == eta**2 * Ki[i][j] for i in range(12) for j in range(12))
    G = arb_mat([[q(v) for v in row] for row in metric])
    C = arb_mat([[arb(int(v)) / int(common['inverse_congruence_denominator']) for v in row] for row in common['inverse_congruence_integer_matrix']])
    delta, rho = q(common['delta']), q(common['rho'])
    assert Fraction(common['delta']) == Fraction('18219/10000') and rho >= 0 and rho < 1
    assert C.nrows() == C.ncols() == 191
    low_F = mat(raw['old_certificate']['source_c_model'])
    B_yF = mat(raw['old_certificate']['source_Bh_model'])
    V_F = C.transpose() * (low_F - B_yF / delta)
    C_F = C * V_F / (1 - rho)
    ell, bF = col(old['Phi_star_h8']), col(old['b_F'])
    a = bF - C_F.transpose() * ell
    finite_support = (a.transpose() * G * a)[0, 0].sqrt()
    # Whole model high Gram: no finite high-mode expansion is introduced.
    H_F = mat(raw['old_certificate']['source_h_gram_model'])
    G0 = mat(raw['old_raw_coupling_gram']) / 10**100
    R_F = H_F - B_yF.transpose() * C_F - C_F.transpose() * B_yF + C_F.transpose() * G0 * C_F
    assert R_F.nrows() == R_F.ncols() == 12
    checks = {'R_F_symmetry_intersections': intersect(R_F, R_F.transpose())}
    U_F = mat([row[:12] for row in common['U96_model'][:12]])
    checks['whole_H_F_vs_U_F_identity_intersections'] = intersect(H_F, delta * (U_F - V_F.transpose() * V_F / (1 - rho)))
    k0 = arb_mat([[q(v)] for v in direction['fixed_k0_rational']])
    t = arb_mat([[q(v)] for v in psi['t_exact']])
    V_J = C.transpose() * (mat(raw['galerkin']['old_low_c_model']) - mat(raw['galerkin']['old_low_Bh_model']) / delta)
    c0 = col(finite['c_model'])
    checks['fixed_c0_reconstruction_intersections'] = intersect(c0, C * (V_J * t - V_F * k0) / (1 - rho))
    H_J = mat(raw['galerkin']['H84_model']) * q('91/50')
    H_FJ = mat(raw['galerkin']['complete_source_high_cross_model'])
    y0_square = (t.transpose() * H_J * t - 2 * k0.transpose() * H_FJ * t + k0.transpose() * H_F * k0)[0, 0]
    b0 = mat(raw['galerkin']['old_low_Bh_model']) * t - B_yF * k0
    r0_square = y0_square - 2 * (c0.transpose() * b0)[0, 0] + (c0.transpose() * G0 * c0)[0, 0]
    assert r0_square.overlaps(box(hp['full_model_high_difference_norm_squared']))
    checks['fixed_r0_whole_Gram_reconstruction_intersections'] = 1
    gamma = q(high['full_M_norm_squared'][1])
    high_square = gamma * box(old['norm_h8'])**2 - (ell.transpose() * ell)[0, 0]
    assert high_square > 0
    assert high_square.overlaps(box(projected['T_h_h8_norm_squared_majorant']))
    nu = high_square.sqrt()
    trace_GR = trace(G * R_F)
    assert trace_GR > 0
    high_model_support = nu / delta * trace_GR.sqrt()
    E_F = mat(common['finite_feature_error_gram'])
    E_hF = mat(raw['old_certificate']['joint_high_source_error_gram'])
    eB = q(raw['old_certificate']['old_coupling_error_norm'][1])
    J = q(high['tr_X_HB'][1]).sqrt()
    e_feature = trace(G * E_F).sqrt()
    e_y = trace(G * E_hF).sqrt()
    e_BcF = eB * trace(G * (C_F.transpose() * C_F)).sqrt()
    C_ell_norm = (ell.transpose() * C * C.transpose() * ell)[0, 0].sqrt()
    finite_model_support = C_ell_norm / (1 - rho).sqrt() * e_feature
    high_model_error_support = nu / delta * (e_y + e_BcF + J * e_feature)
    # A single support upper bound for H* h in the G ellipsoid. The unknown
    # finite/high cross term is bounded by the triangle inequality, not set to zero.
    supports = {'finite_common_k': finite_support, 'whole_high_common_k': high_model_support,
                'finite_source_error_in_k': finite_model_support, 'high_source_and_coupling_error_in_k': high_model_error_support}
    k_upper = sum((v.upper() for v in supports.values()), arb(0))
    assert all(v >= 0 and v.is_finite() for v in supports.values())
    e_fixed = q(finite['fixed_k_feature_error_bound'][1])
    fixed_finite = C_ell_norm / (1 - rho).sqrt() * e_fixed
    assert fixed_finite.overlaps(box(old['finite_response_fixed_k_error']))
    fixed_r = box(hp['full_model_high_difference_norm_squared']).sqrt() + q(hp['y_fixed_k_error_upper'][1]) + eB * (c0.transpose() * c0)[0, 0].sqrt() + J * e_fixed
    fixed_high = nu / delta * fixed_r
    source_error = box(old['source_model_scalar_error'])
    # Do NOT carry the previous psi-k, finite-k, or actual-k high budgets forward.
    radius = k_upper + fixed_finite.upper() + fixed_high.upper() + source_error.upper()
    I0 = box(old['I0'])
    L = I0 + arb(0, radius.upper())
    threshold = box(sharp['threshold'])
    budget = load(ORIGINAL + 'gpt2-kp-budgets/expected/BUDGET_BOUNDS.json')['parities']['even']
    assert Fraction(budget['q']) == Fraction(coherent['q'])
    alpha = q('10/11') * q(budget['q'])
    epsilon_D = q(budget['D_model_scalar_error_upper'])
    assert Fraction(sharp['K_P_upper_rational']) >= Fraction(sharp['actual_K_P_interval'][1])
    assert threshold.overlaps((alpha * q(sharp['K_P_upper_rational'])).sqrt() + epsilon_D)
    actual_energy_threshold = (alpha * box(sharp['actual_K_P_interval'])).sqrt()
    actual_residual_abs_upper = abs(L).upper() + epsilon_D
    # Stronger nonexclusion check also uses the LOWER actual K_P endpoint.
    assert actual_residual_abs_upper < actual_energy_threshold.lower()
    assert box(projected['L_interval']).contains(L)
    assert L > q('1.238460') and L < q('1.748815')
    assert abs(L).upper() < threshold.lower()
    result = {
        'status': 'AUTHOR_DERIVED_CONDITIONAL_COHERENT_K_EXTERNAL_REVIEW_OPEN',
        'parity': 'even', 'candidate_sha256': old['candidate_sha256'],
        'inherited_scalar_sha256': bindings['repository_files'][FROZEN + 'expected/FROZEN_CERTIFICATE_even.json'],
        'threshold_certificate_sha256': bindings['repository_files'][SHARP + 'expected/SHARP_K_even.json'],
        'k0_exact_rational': direction['fixed_k0_rational'], 'K_positive_pivots': pivots,
        'exact_K_Kinverse_identity_entries': 144, 'exact_metric_identity_entries': 144,
        'checks': checks, 'common_k_finite_covector': [enc(a[i, 0]) for i in range(12)],
        'whole_high_response_Gram': [[enc(R_F[i, j]) for j in range(12)] for i in range(12)],
        'trace_G_R_F': enc(trace_GR), 'high_coordinate_norm_bound': enc(nu),
        'k_support_components': {key: enc(v) for key, v in supports.items()},
        'single_common_k_support_upper': enc(k_upper),
        'fixed_k_finite_response_error': enc(fixed_finite),
        'fixed_k_high_response_bound': enc(fixed_high),
        'source_model_scalar_error': enc(source_error), 'I0': enc(I0),
        'radius_without_I0_width': enc(radius), 'L_interval': enc(L),
        'outward_decimal_L': ['1.238460', '1.748815'], 'threshold': enc(threshold),
        'threshold_minus_sup_abs_L': enc(threshold - abs(L).upper()),
        'actual_energy_threshold_interval': enc(actual_energy_threshold),
        'D_model_scalar_error_upper': enc(epsilon_D),
        'actual_residual_absolute_upper': enc(actual_residual_abs_upper),
        'actual_energy_threshold_minus_residual_upper': enc(actual_energy_threshold - actual_residual_abs_upper),
        'outcome': 'DOES_NOT_EXCLUDE_FOR_DIRECTION', 'precision_bits': ctx.prec,
        'high_midpoint_used': False, 'new_operator_integrations': False,
        'candidate_changed': False, 'N12_closed': False,
        'remaining_support_relaxation': 'triangle inequality between finite covector and whole high Hilbert-Schmidt support; no assumed independence',
    }
    out = Path(output) if output is not None else HERE / 'expected'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'COHERENT_K_EVEN.json').write_text(json.dumps(result, indent=2) + '\n')
    print('even: common k support', k_upper, 'fixed high', fixed_high, flush=True)
    print('L:', L.lower(), L.upper(), result['outcome'], flush=True)
    return result


if __name__ == '__main__':
    main()
