"""Sharpen only the fixed Schur test's a_fin square loss, with bound Grams."""
import json
from fractions import Fraction as Q
from flint import arb, arb_mat


def certify(previous, env, frozen_bytes, old_bytes):
    c = env['common']
    q, box, enc = c.q, c.box, c.enc
    need, quad = previous.need, previous.quad
    old, frozen = json.loads(old_bytes), json.loads(frozen_bytes)
    need(previous.sha(frozen_bytes) == old['test_vector_sha256'], 'Frozen test binding')
    need(old['physical_candidate_sha256'] == previous.sha(env['data']['candidate_even']), 'Physical witness binding')
    need(old['K_P_certificate_sha256'] == previous.sha(env['data']['kp_even']), 'Budget binding')
    need(old['budget_interval'] == env['kp']['K_P_interval'], 'Unchanged budget')
    need(old['outcome'] == 'SCHUR_LOWER_TEST_OPEN', 'Wrong predecessor')
    w = arb_mat([[q(x)] for x in frozen['raw_coefficients']])
    need(w.nrows() == 84 and w.ncols() == 1, 'Frozen dimension')
    W = env['energy'].w
    z = W['a'] * w
    r = W['Ki'] * z
    g = quad(W['GJ'], w)
    f = quad(W['GF'], r)
    n2 = quad(W['Ki'], z)
    need(n2.overlaps(box(old['form_a_Ki_model_norm_squared'])), 'Same model square')
    common = env['inp'].json('common')['cases'][0]
    raw = env['inp'].json('old_sources')['cases'][0]
    # Exactly the conservative #238 error Gram: retain the factor two and
    # the high-error overcoverage; do not substitute the smaller F-F price.
    EF = 2 * (c.mat(common['finite_feature_error_gram'])
              + c.mat(raw['old_certificate']['joint_high_source_error_gram']) / W['delta'])
    EJ = 2 * (box(common['tail_feature_error_scalar'])
              + box(raw['galerkin']['high_source_error_norm'])**2 / W['delta'])
    U = c.mat(common['U96_model'])
    UF = arb_mat([[U[i,j] for j in range(12)] for i in range(12)])
    UJ = arb_mat([[U[i,j] for j in range(12,96)] for i in range(12,96)])
    uF, uJ = quad(UF, r), quad(UJ, w)
    eF, eJ = quad(EF, r), EJ * quad(arb_mat([[int(i==j) for j in range(84)] for i in range(84)]), w)
    for name, v in [('uF',uF),('uJ',uJ),('eF',eF),('eJ',eJ),('g',g),('f',f)]:
        need(v >= 0, 'Unresolved or negative square: ' + name)
    dd = env['energy'].bounds['direct_energy_relative_error_upper']
    direct = dd * (f*g).sqrt()
    terms = {'model_F_error_J':(uF*eJ).sqrt(),
             'error_F_model_J':(eF*uJ).sqrt(),
             'error_F_error_J':(eF*eJ).sqrt()}
    cross_error = direct + sum(terms.values(), arb(0))
    loss = 2*cross_error
    coarse_loss = 2*W['da']*(f*g).sqrt()
    # All unaffected endpoints are inherited exactly, including the full
    # D/U diagonal error, pairing a_fin error, and whole residual error.
    base = Q(old['base_actual_energy_interval'][0])
    pairing = Q(old['pairing_actual_interval'][0])
    B = Q(old['form_B_model'][1])
    diagonal = Q(old['form_common_D_U_error'][1])
    model_square = Q(old['form_a_Ki_model_norm_squared'][0])
    exact_upper = Q(enc(loss)[1])
    scaled = exact_upper * 10**24
    loss_upper = Q(-((-scaled.numerator)//scaled.denominator), 10**24)
    square_lower = max(Q(0), model_square-loss_upper)
    H_upper = B+diagonal-square_lower
    lower = base+2*pairing-H_upper
    budget = Q(old['budget_interval'][1])
    threshold = base+2*pairing-(B+diagonal-model_square)-budget
    old_loss = Q(old['H_star_form_upper'])-(B+diagonal-model_square)
    gap = lower-budget
    return c.encode({
        'status':'AUTHOR_DERIVED', 'review_status':'EXTERNAL_REVIEW_OPEN',
        'source_commit':'35a74079409c2904e89d7628377eb2e5b1c8dcae', 'parity':'even',
        'outcome':'SCHUR_UNDERFORM_COMPARISON_EXCLUDED' if gap>0 else 'SCHUR_LOWER_TEST_OPEN',
        'criterion':'E_base_lower + 2 pairing_lower - H_star_upper > K_P_upper',
        'previous_result_sha256':previous.sha(old_bytes),
        'test_vector_sha256':previous.sha(frozen_bytes),
        'physical_candidate_sha256':old['physical_candidate_sha256'],
        'K_P_certificate_sha256':old['K_P_certificate_sha256'],
        'K_star_sha256':frozen['K_star_sha256'],
        'inherited_base_interval':old['base_actual_energy_interval'],
        'inherited_pairing_interval':old['pairing_actual_interval'],
        'inherited_pairing_errors':old['pairing_error_components'],
        'inherited_diagonal_D_U_error':old['form_common_D_U_error'],
        'inherited_budget_interval':old['budget_interval'],
        'strict_loss_threshold':str(threshold), 'working_loss_target':'123/100000000',
        'working_target_reached':loss_upper <= Q('1.23e-6'),
        'old_square_loss_upper':str(old_loss),
        'coarse_directional_square_loss':coarse_loss,
        'directional_Grams':{'model_F':uF,'model_J':uJ,'error_F':eF,'error_J':eJ,'GF_r':f,'GJ_w':g},
        'inherited_direct_relative_error':dd,
        'direct_cross_error':direct, 'feature_cross_errors':terms,
        'refined_square_loss':loss, 'refined_square_loss_upper':str(loss_upper),
        'model_square_interval':old['form_a_Ki_model_norm_squared'],
        'actual_square_lower':str(square_lower), 'H_star_form_upper':str(H_upper),
        'inverse_energy_lower':str(lower), 'lower_minus_budget_upper':str(gap),
        'loss_improvement_factor_lower':str(old_loss/loss_upper),
        'positive_eta_q_term_unused':True, 'nonnegative_error_square_unused':True,
        'all_other_bounds_unchanged':True, 'common_error_Gram_factor_two_retained':True,
        'high_error_overcoverage_retained':True, 'new_integrations':False,
        'new_linear_solve':False, 'RL_computed':False, 'adaptive_search':False,
        'K_star_changed':False, 'physical_witness_changed':False, 'test_vector_changed':False,
        'full_inverse_energy_upper_claimed':False, 'partial_pass':False, 'dual_reserve':None,
        'N12_closed':False, 'milestone_4_closed':False,
        'negative_claim_boundary':'For the frozen response and even physical witness, every W >= Q_lower_star^-1 exceeds the unchanged K_P budget. No exclusion of other lower forms, other responses or all majorants of the actual A9 inverse; no negative Weil direction.'})
