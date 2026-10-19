"""Independent standard-library endpoint audit; no Arb and no engine import."""
from fractions import Fraction as Q
from math import isqrt


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sqrt_upper(x):
    need(x >= 0, 'Negative audit square')
    scale = 10**90
    a = x * scale**2
    k = isqrt(a.numerator // a.denominator)
    if Q(k*k) < a:
        k += 1
    need(Q(k*k, scale**2) >= x, 'Integer square-root enclosure')
    return Q(k, scale)


def check(result, old):
    for new, previous in [('inherited_base_interval','base_actual_energy_interval'),
                          ('inherited_pairing_interval','pairing_actual_interval'),
                          ('inherited_pairing_errors','pairing_error_components'),
                          ('inherited_diagonal_D_U_error','form_common_D_U_error'),
                          ('inherited_budget_interval','budget_interval'),
                          ('model_square_interval','form_a_Ki_model_norm_squared')]:
        need(result[new] == old[previous], 'Changed inherited endpoints: ' + new)
    g = {k:Q(v[1]) for k,v in result['directional_Grams'].items()}
    direct = Q(result['inherited_direct_relative_error'][1])*sqrt_upper(g['GF_r']*g['GJ_w'])
    features = sum(sqrt_upper(g[a]*g[b]) for a,b in
                   [('model_F','error_J'),('error_F','model_J'),('error_F','error_J')])
    price = Q(result['refined_square_loss_upper'])
    need(price >= 2*(direct+features), 'Loss does not cover independent endpoint calculation')
    square = max(Q(0),Q(old['form_a_Ki_model_norm_squared'][0])-price)
    H = Q(old['form_B_model'][1])+Q(old['form_common_D_U_error'][1])-square
    lower = Q(old['base_actual_energy_interval'][0])+2*Q(old['pairing_actual_interval'][0])-H
    gap = lower-Q(old['budget_interval'][1])
    need(str(H) == result['H_star_form_upper'], 'Form endpoint')
    need(str(lower) == result['inverse_energy_lower'], 'Full lower endpoint')
    need(str(gap) == result['lower_minus_budget_upper'], 'Budget comparison')
    outcome = 'SCHUR_UNDERFORM_COMPARISON_EXCLUDED' if gap>0 else 'SCHUR_LOWER_TEST_OPEN'
    need(outcome == result['outcome'], 'One-sided outcome')
    need(result['partial_pass'] is False and result['dual_reserve'] is None, 'Invalid two-sided implication')
    return 'PASS_RATIONAL_ENDPOINT_AUDIT'
