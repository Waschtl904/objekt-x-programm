"""Synthetic exact controls; all finite examples extend by an identity tail on l2."""
from pathlib import Path
from itertools import combinations, permutations
from copy import deepcopy
import argparse
import json
from check_certificate import F, mat, tr, eye, scale, add, sub, mul, gram, inverse, positive, certify, Inconclusive

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def serial(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, list):
        return [serial(v) for v in x]
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    return x


def determinant(a):
    # Small independent Leibniz determinant: no LDL and no matrix inverse.
    n = len(a)
    total = F(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        value = F((-1)**inversions)
        for i in range(n):
            value *= a[i][perm[i]]
        total += value
    return total


def principal_psd(a):
    return all(determinant([[a[i][j] for j in ids] for i in ids]) >= 0
               for k in range(1, len(a)+1) for ids in combinations(range(len(a)), k))


def coverage_input(j, l):
    w = gram(j)
    b = mul(l, j)
    p = mul(inverse(w), tr(b))
    e = sub(tr(l), mul(j, p))
    ue = gram(e)
    g = mul(l, tr(l))
    via_expansion = add(sub(sub(g, mul(b, p)), mul(tr(p), tr(b))), gram(p, w))
    require(via_expansion == ue, 'Joint Gram expansion disagrees with direct error functions')
    hj = [g[i]+b[i] for i in range(len(g))] + [tr(b)[i]+w[i] for i in range(len(w))]
    v = eye(len(l)) + scale(p, F(-1))
    require(gram(v, hj) == ue, 'Block Gram congruence failed')
    pi = mul(mul(j, inverse(w)), tr(j))
    require(mul(pi, pi) == pi and tr(pi) == pi, 'Full Hilbert projection failed')
    complement = sub(eye(len(j)), pi)
    require(mul(l, complement) == mul(tr(e), complement), 'Complement identity failed')
    data = {'schema': 'objekt-x-coverage/1', 'kind': 'SYNTHETIC_ONLY',
            'alpha': '1/10', 'leakage_budget': '1/20',
            'basis_gram_lower': w, 'basis_gram_upper': w,
            'leakage_gram_upper': ue}
    return serial(data), {'W': w, 'P': p, 'E': e, 'Pi_Z': complement}


def failed(data, expected):
    try:
        certify(data)
    except Inconclusive as exc:
        require(str(exc) == expected, 'Unexpected failed gate: '+str(exc))
        return
    raise ValueError('Expected rejection: '+expected)


def run():
    cases = {}
    j = mat([[1, 1], [0, 1], [0, 0], [0, 0]])
    l = mat([[1, 2, '1/10', 0], [2, -1, 0, '1/20']])
    good, aux = coverage_input(j, l)
    w, pz = aux['W'], aux['Pi_Z']
    require(w != eye(2), 'Nonorthogonal basis control is trivial')
    wrong_pi = mul(j, tr(j))
    require(mul(wrong_pi, wrong_pi) != wrong_pi, 'Missing-Gram-inverse control is trivial')
    require(certify(good)['status'] == 'PASS_CONDITIONAL_COVERAGE', 'Coverage failed')
    cases['nonorthogonal_basis_and_full_joint_gram'] = 'PASS'

    t = mat([[2, '1/5', '1/10', 0], ['1/5', 3, 0, '1/10'],
             ['1/10', 0, 1, '1/5'], [0, '1/10', '1/5', 2]])

    def schur_data(operator):
        baseline = add(sub(operator, scale(eye(4), F(1, 10))), gram(l))
        require(principal_psd(baseline), 'Synthetic global lower-form hypothesis failed')
        a = [row[2:] for row in operator[2:]]
        require(principal_psd(sub(a, scale(eye(2), F(1, 20)))), 'Synthetic full tail floor failed')
        b = mul(pz, mul(operator, j))
        actual_response = mul(inverse(a), b[2:])
        y = [[F(0), F(0)], [F(0), F(0)]] + scale(actual_response, F(1, 2))
        r = sub(b, mul(pz, mul(operator, y)))
        ky = gram(sub(j, y), operator)
        direct_schur = sub(gram(j, operator), gram(b[2:], inverse(a)))
        residual_schur = sub(ky, gram(r[2:], inverse(a)))
        require(direct_schur == residual_schur, 'Full residual Schur identity failed')
        require(principal_psd(sub(direct_schur, sub(ky, scale(gram(r), 20)))), 'Residual charge is not an upper charge')
        data = deepcopy(good)
        data['schur'] = serial({'K_lower': ky, 'residual_gram_upper': gram(r), 'eta': F(1, 10),
            'normalization': {'response_gram_upper': gram(y),
                              'response_norm_bound': F(1, 10), 'residual_norm_bound': F(1, 10)}})
        return data, direct_schur

    full, actual = schur_data(t)
    report = certify(full)
    require(report['status'] == 'PASS_CONDITIONAL_SCHUR', 'Positive Schur fixture failed')
    require(report['conditional_R12_floor'] == '5/961', 'Norm-return constant differs')
    require(principal_psd(sub(actual, scale(w, F(1, 10)))), 'Independent Schur margin check failed')
    require(principal_psd(sub(t, scale(eye(4), F(5, 961)))), 'Independent full norm-floor check failed')
    cases['positive_schur_residual_and_norm_return'] = report

    negative_t = [row[:] for row in t]
    negative_t[0][0] = F(-1)
    negative, neg_schur = schur_data(negative_t)
    require(neg_schur[0][0] < 0, 'Negative actual Schur control is missing')
    failed(negative, 'FINITE_SCHUR_INCONCLUSIVE')
    cases['positive_tail_with_negative_finite_schur'] = 'REJECTED_AS_REQUIRED'

    duplicate_rows, _ = coverage_input(mat([[1], [0], [0]]), mat([[1, 0, 0], [2, 0, 0]]))
    require(certify(duplicate_rows)['status'] == 'PASS_CONDITIONAL_COVERAGE', 'Redundant rows were incorrectly rejected')
    cases['redundant_functional_rows_need_no_inverse'] = 'PASS'

    near, _ = coverage_input(mat([[1], [0], [0]]), mat([[1, 0, 0], [1, '1/100', 0]]))
    require(certify(near)['status'] == 'PASS_CONDITIONAL_COVERAGE', 'Small extra direction was not paid')
    require(determinant(mat([[1, 0], [1, '1/100']])) != 0, 'Near-rank control is actually rank deficient')
    cases['rank_two_functionals_with_one_trial_direction'] = 'PASS_WITH_PAID_NONZERO_LEAKAGE'

    hidden, _ = coverage_input(mat([[1], [0], [0]]), mat([[1, 0, 1]]))
    failed(hidden, 'COVERAGE_BOUND_INCONCLUSIVE')
    forged = deepcopy(hidden)
    forged['leakage_gram_upper'] = [['0']]
    require(certify(forged)['operator_input_verified'] is False, 'Checker promoted false enclosure metadata')
    cases['hidden_direction_full_gram_rejected'] = 'PASS'
    cases['truncated_false_enclosure_can_pass_algebra_only'] = {
        'demonstrated': True, 'lesson': 'Full-operator enclosure must be established separately; the numerical checker cannot infer it.'}

    coherent = deepcopy(hidden)
    coherent['leakage_gram_upper'] = [['1/16']]
    failed(coherent, 'COVERAGE_BOUND_INCONCLUSIVE')
    naive = deepcopy(coherent)
    naive['leakage_gram_upper'] = [['1/32']]
    require(certify(naive)['status'] == 'PASS_CONDITIONAL_COVERAGE', 'Cross-error counterexample malformed')
    require(F(1, 8)**2+F(1, 8)**2 == F(1, 32) and (F(1, 8)+F(1, 8))**2 == F(1, 16), 'Cross-error arithmetic failed')
    cases['coherent_errors_need_cross_terms_or_young_charge'] = 'PASS'

    singular = deepcopy(good)
    singular['basis_gram_lower'] = [['1', '1'], ['1', '1']]
    failed(singular, 'BASIS_GRAM_NOT_CERTIFIED')
    boundary = deepcopy(good)
    boundary['leakage_gram_upper'] = [['1/20', '0'], ['0', '1/20']]
    require(certify(boundary)['conditional_tail_floor'] == '1/20', 'Semidefinite boundary should pass')
    require(positive(mat([[0, 0], [0, 1]])), 'Valid singular PSD rejected')
    require(not positive(mat([[0, 1], [1, 0]])), 'Zero pivot with nonzero off-diagonal accepted')
    cases['singular_basis_rejected_and_psd_boundary_handled'] = 'PASS'

    bad_float = deepcopy(good)
    bad_float['alpha'] = 0.1
    try:
        certify(bad_float)
    except ValueError:
        cases['floating_input_rejected'] = 'PASS'
    else:
        raise ValueError('Floating input was accepted')

    return ({'scope': 'SYNTHETIC_ALGEBRA_ONLY', 'cases': cases,
             'actual_operator_data_evaluated': False, 'full_remainder_certified': False},
            {'synthetic_pass.json': full, 'synthetic_hidden_tail.json': hidden,
             'synthetic_negative_schur.json': negative, 'synthetic_near_rank.json': near})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-fixtures', action='store_true', help='Authoring only: save deterministic examples and check receipt')
    args = parser.parse_args()
    result, fixtures = run()
    if args.write_fixtures:
        (ROOT/'examples').mkdir(exist_ok=True)
        for name, data in fixtures.items():
            (ROOT/'examples'/name).write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
        (ROOT/'checks.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    else:
        require(result == json.loads((ROOT/'checks.json').read_bytes()), 'Stored check receipt mismatch')
        for name, data in fixtures.items():
            require(data == json.loads((ROOT/'examples'/name).read_bytes()), 'Stored example mismatch: '+name)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
