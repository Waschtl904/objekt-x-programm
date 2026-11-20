"""Bounded source/schema audit and exact algebra; no operator evaluation."""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read_bound(root, entries):
    snapshot = {}
    for name, item in entries.items():
        p = (root / item['path']).resolve()
        need(p.is_relative_to(root), 'Escaping input: ' + name)
        raw = p.read_bytes()
        need(sha(raw) == item['sha256'], 'Input hash: ' + name)
        snapshot[name] = raw
    return snapshot


def load(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def scale(a, s):
    return [s*x for x in a]


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def mv(a, x):
    return [dot(row, x) for row in a]


def quadratic(a, x):
    return dot(x, mv(a, x))


def algebra():
    # Exact fixed-W example: all old residual information is identical.
    W = [[Q(2), Q(1)], [Q(1), Q(2)]]
    need(W[0][0]-1 >= 0 and
         (W[0][0]-1)*(W[1][1]-1)-W[0][1]**2 >= 0,
         'W-I must be positive semidefinite')
    rows = []
    for sign in (Q(1), Q(-1)):
        phi, r0 = [sign, Q(0)], [Q(0), Q(1)]
        C = add(phi, r0)
        F, A12, d, t0 = dot(phi, C), dot(phi, phi), Q(5, 2), Q(1)
        K0 = d-2*t0*F+t0*t0*A12
        E0, beta, gamma = quadratic(W, r0), quadratic(W, phi), dot(phi, mv(W, r0))
        g, a = F-A12*t0, A12
        for s in (Q(-1, 2), Q(0), Q(1, 100), Q(1, 2)):
            t = t0+s
            r = add(C, scale(phi, -t))
            K, E = d-2*t*F+t*t*A12, quadratic(W, r)
            need(K == K0-2*s*g+s*s*a, 'Budget line identity')
            need(E == E0-2*s*gamma+s*s*beta, 'Energy line identity')
            need(K-E == K0-E0+2*s*(gamma-g)+s*s*(a-beta), 'Joint line identity')
        s = Q(1, 2)
        K, E = K0-2*s*g+s*s*a, E0-2*s*gamma+s*s*beta
        rows.append(dict(sign=str(sign), A12=str(A12), F=str(F), K0=str(K0),
                         E0=str(E0), beta=str(beta), gamma=str(gamma),
                         C_norm_squared=str(dot(C, C)), K_new=str(K), E_new=str(E),
                         margin=str(K-E), true_Schur=str(d-dot(C, C))))
    for k in ('A12', 'F', 'K0', 'E0', 'beta', 'C_norm_squared', 'K_new', 'true_Schur'):
        need(rows[0][k] == rows[1][k], 'Countermodel common data: ' + k)
    need(Q(rows[0]['margin']) > 0 > Q(rows[1]['margin']), 'Opposite decisions')

    # Also check nonzero budget slope: the countermodels above have g=0.
    A = [[Q(2), Q(0)], [Q(0), Q(3)]]
    phi, C, t0, v, d = [Q(1), Q(1)], [Q(3), Q(2)], Q(2, 7), Q(3, 11), Q(5)
    D = mv(A, phi)
    F, A12 = dot(phi, C), dot(phi, D)
    r0 = add(C, scale(D, -t0))
    g, a = v*(F-A12*t0), v*v*A12
    gamma, beta = dot(scale(D, v), mv(W, r0)), quadratic(W, scale(D, v))
    K0, E0 = d-2*t0*F+t0*t0*A12, quadratic(W, r0)
    need(g != 0, 'Nonzero budget-slope control')
    for s in (Q(-2, 3), Q(1, 5), Q(7, 11)):
        t = t0+s*v
        K, E = d-2*t*F+t*t*A12, quadratic(W, add(C, scale(D, -t)))
        need(K == K0-2*s*g+s*s*a, 'Non-Galerkin budget identity')
        need(E == E0-2*s*gamma+s*s*beta, 'Non-Galerkin energy identity')
        need(K-E == K0-E0+2*s*(gamma-g)+s*s*(a-beta), 'Non-Galerkin joint identity')

    # Nonparallel and nonunit examples ensure the rank-two correction is present.
    for f, u in (([Q(2), Q(-3), Q(1)], [Q(5), Q(1), Q(-2)]),
                 ([Q(1, 3), Q(2, 5)], [Q(-7, 4), Q(3, 2)])):
        n2, fu = dot(f, f), dot(f, u)
        Y = [[(u[i]*f[j]+f[i]*u[j])/n2-fu*f[i]*f[j]/n2**2
              for j in range(len(f))] for i in range(len(f))]
        need(all(Y[i][j] == Y[j][i] for i in range(len(f)) for j in range(len(f))),
             'Symmetric response update')
        need(mv(Y, f) == u, 'Exact prescribed coefficient change')
    return {'joint_line_identities': True, 'nonzero_budget_slope_checked': True,
            'symmetric_update_identity': True,
            'fixed_weight_countermodels': rows,
            'countermodels_are_Object_X_data': False}


def interval(x):
    a, b = map(Q, x)
    need(a <= b, 'Reversed interval')
    return a, b


def scalar_interval(s, x):
    a, b = interval(x)
    return (s*a, s*b) if s >= 0 else (s*b, s*a)


def run(snapshot, source_commit):
    pairs, candidate, kp, pilot, form, pre = [load(snapshot[k]) for k in
        ('pairs_even', 'candidate_even', 'kp_even', 'pilot_result', 'form_result', 'preflight_result')]
    dims = {'Phi_star_h': (191, 12), 'high_Gram': (12, 12),
            'high_cross_models': (287, 12), 'bare_F_J_pairs': (96, 12),
            'Fhat': (12, 12), 'G_W': (12, 12), 'T': (12, 12)}
    for key, (n, m) in dims.items():
        need(len(pairs[key]) == n and all(len(r) == m for r in pairs[key]), 'Shape: ' + key)
    need(pairs['parity'] == 'even', 'Parity')
    need(candidate['pairs_sha256'] == pilot['pairs_sha256'] == sha(snapshot['pairs_even']),
         'Same old residual pairs')
    need(pilot['candidate_sha256'] == kp['candidate_sha256'] ==
         form['physical_candidate_sha256'] == sha(snapshot['candidate_even']), 'Same witness')
    need(pilot['K_P_certificate_sha256'] == form['K_P_certificate_sha256'] ==
         sha(snapshot['kp_even']), 'Same budget')
    need(pilot['frozen_response_changed'] is False and pilot['new_integrations'] is False,
         'Pilot scope changed')
    need(form['new_integrations'] is False and form['physical_witness_changed'] is False,
         'Form refinement scope changed')
    need(form['outcome'] == 'SCHUR_UNDERFORM_COMPARISON_EXCLUDED', 'Inherited decision')
    need(Q(form['inverse_energy_lower'])-Q(kp['K_P_interval'][1]) ==
         Q(form['lower_minus_budget_upper']) > 0, 'Inherited endpoints')
    for name in ('scale_99_100', 'scale_101_100'):
        need(pre['parities']['even']['variants'][name]['outcome'] ==
             'TRANSFER_BOUND_INCONCLUSIVE', 'Old scaling result must remain open')
    raw_c = list(map(Q, candidate['raw_coefficients']))
    f0 = [scalar_interval(c, x) for c, x in zip(raw_c, pairs['Fhat'][0])]
    f0 = [sum((x[i] for x in f0), Q(0)) for i in (0, 1)]
    need(f0[0] > 0 or f0[1] < 0, 'Nonzero fixed model source not established')
    # The W-normalization is positive, so it cannot change nonvanishing.
    n2 = [Q(0), Q(0)]
    for i in range(12):
        for j in range(12):
            lo, hi = scalar_interval(raw_c[i]*raw_c[j], pairs['G_W'][i][j])
            n2[0] += lo
            n2[1] += hi
    need(n2[0] > 0, 'Physical raw witness norm')
    return {
        'status': 'AUTHOR_DERIVED', 'review_status': 'EXTERNAL_REVIEW_OPEN',
        'source_commit': source_commit,
        'decision': 'NO_DATA_SUPPORTED_RESPONSE_CANDIDATE',
        'parity': 'even', 'checked_pair_shapes': {k: list(v) for k, v in dims.items()},
        'same_residual_pairs_in_K_pilot': True, 'same_witness_and_budget_in_Schur_refinement': True,
        'Fhat_raw_witness_first_coordinate_interval': list(map(str, f0)),
        'raw_physical_W_norm_squared_interval': list(map(str, n2)),
        'inherited_frozen_response_exclusion_gap': form['lower_minus_budget_upper'],
        'scaling_variants_99_100_and_101_100_remain_open': True,
        'new_energy_data_for_one_fixed_line': ['beta=<Dv,V Dv>', 'gamma=Re<Dv,V r0>'],
        'new_weighted_model_and_integration_error_control_required': True,
        'data_gap_scope': 'stored old residual features; no impossibility from full source definitions claimed',
        'algebra_controls': algebra(),
        'candidate_selected': False, 'new_operator_evaluations': False,
        'new_quadrature': False, 'new_RL': False, 'old_certifiers_rerun': False,
        'general_response_class_excluded': False, 'positive_transition_claimed': False,
        'selection_checklist_item_completed': False, 'milestone_4_closed': False,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repository', type=Path, default=ROOT)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    need(__debug__, 'python -O is not supported')
    need(args.check or args.output is not None, 'Choose --check or --output')
    root = args.repository.resolve()
    binding_bytes = (HERE/'INPUT_BINDINGS.json').read_bytes()
    binding = json.loads(binding_bytes)
    expected = None
    if args.check:
        manifest = json.loads((HERE/'MANIFEST.json').read_bytes())
        own = read_bound(HERE, {k: {'path': k, 'sha256': v} for k, v in manifest.items()})
        need(own['INPUT_BINDINGS.json'] == binding_bytes, 'Binding snapshot changed')
        expected = own['RESULT.json']
    snapshot = read_bound(root, binding['files'])
    result = run(snapshot, binding['source_commit'])
    out = (json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)+'\n').encode()
    if args.check:
        need(out == expected, 'Result replay differs')
        print('PASS: bound source audit and exact algebra replay are byte-identical')
    if args.output:
        args.output.write_bytes(out)


if __name__ == '__main__':
    main()
