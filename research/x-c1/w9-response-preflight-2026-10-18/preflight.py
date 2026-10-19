"""Bounded response preflight: exact small matrices and polynomial primitives only.

No quadrature, adaptive search, RL solve, or whole pairing integration is run.
"""
import argparse
import gzip
import hashlib
import io
import json
import sys
import zipfile
from fractions import Fraction
from pathlib import Path
from types import ModuleType

from flint import arb, arb_mat, arb_poly, ctx, fmpq, fmpq_mat

HERE = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def source_snapshot(root, binding_bytes):
    spec = json.loads(binding_bytes)
    data = {}
    for alias, item in spec['files'].items():
        path = (root / item['path']).resolve()
        need(path.is_relative_to(root), 'Escaping source path')
        raw = path.read_bytes()
        need(digest(raw) == item['sha256'], 'Source binding: ' + alias)
        data[alias] = raw
    common = ModuleType('w9_preflight_bound_common')
    common.__file__ = str(root / spec['files']['common']['path'])
    exec(compile(data['common'], common.__file__, 'exec'), common.__dict__)
    inp = common.Inputs(binding_bytes=data['inherited_inputs'])
    member = spec['old_inverse_member']
    with zipfile.ZipFile(io.BytesIO(inp.data['response_archive'])) as z:
        raw = z.read(member['name'])
    need(digest(raw) == member['sha256'], 'Old inverse member binding')
    return common, inp, data, json.loads(raw)


def exact_matrix(rows):
    return fmpq_mat([[fmpq(str(x)) for x in row] for row in rows])


def rational_rows(a):
    return [[str(a[i, j]) for j in range(a.ncols())] for i in range(a.nrows())]


def matrix_digest(a):
    return digest(json.dumps(rational_rows(a), separators=(',', ':')).encode())


def response_norm(common, functions):
    """Physical operator bound from exact polynomial integrals and log norm.

    The common physical prefactor reduces the even/odd L2 norm to [0,1].
    The exact moment projection is contractive. All shifted polynomials are
    integrated only on their actual support, never on their extrapolation.
    """
    q, pint, legs = common.q, common.pint, common.legs
    a = arb(3).log()
    max_degree = max(len(f['D']['V_multiplier']) for f in functions)
    leg = legs(max_degree + 1)
    columns = []
    for f in functions:
        sp = f['D']
        p = arb_poly(list(map(q, sp['polynomial'])))
        v = arb_poly(list(map(q, sp['V_multiplier'])))
        # v=sum v_n P_n, |P_n|<=1 on [-1,1]. These are primitives,
        # not sampled supremum values.
        vmax = sum((abs(pint(v * leg[n], arb(-1), arb(1)) * (2*n+1)/2).upper()
                    for n in range(len(v))), arb(0))
        psquare = pint(p*p)
        need(psquare.lower() >= 0, 'Polynomial norm lost positivity')
        nrm = psquare.upper().sqrt() + vmax / arb(2).sqrt()
        nrm += abs(q(sp['moment_multiplier'])).upper() * (a/2).exp()
        for term in sp['shift_terms']:
            channel = int(term['channel'])
            shift = arb(1) if channel == 3 else arb(2) if channel == 9 else arb(channel).log()/a
            if int(term['translation_sign']) == 1:
                lo, hi = arb(0), 1-shift
            else:
                lo, hi = max(arb(0), shift-1), arb(1)
            if hi > lo:
                poly = arb_poly(list(map(q, term['polynomial'])))
                square = pint(poly*poly, lo, hi)
                need(square.lower() >= 0, 'Shift polynomial norm lost positivity')
                nrm += square.upper().sqrt()
            else:
                need(hi <= lo, 'Unresolved support ordering')
        columns.append(nrm.upper())
    return sum((v*v for v in columns), arb(0)).sqrt().upper(), columns


def algebra_controls():
    # A positive partial weight does not inherit W >= A^-1. In the scalar
    # example A=1, W=2, partial W=0, C=1, d=3/2, the partial margin grows
    # without bound as x grows, whereas the full comparison fails at x=3.
    from fractions import Fraction as Q
    for x in (Q(0), Q(1), Q(3)):
        k = Q(3, 2)-2*x+x*x
        full = k-2*(1-x)**2
        need(full == Q(1, 2)-(1-x)**2, 'Surplus identity')
    need(Q(3, 2)-6+9 > 0 and Q(1, 2)-(1-3)**2 < 0,
         'Partial optimization counterexample')
    # Full comparison increment, including the change in K.
    A, W, C, t0, step = Q(2), Q(3, 4), Q(5, 3), Q(2, 7), Q(-3, 11)
    r = C-A*t0
    budget_change = -2*(C-A*t0)*step + A*step*step
    energy_change = -2*step*A*W*r + step*step*A*W*A
    need(budget_change-energy_change ==
         2*step*(A*W*r+A*t0-C)-step*step*(A*W*A-A), 'Joint increment')
    return {'joint_budget_energy_increment': True,
            'full_surplus_identity': True,
            'partial_weight_optimization_counterexample': True}


def run(root, binding_bytes):
    need(__debug__, 'Do not use python -O')
    ctx.prec = 800
    common, inp, source, old_inverse = source_snapshot(root, binding_bytes)
    q, box, mat = common.q, common.box, common.mat
    norm, trace, enc = common.norm, common.trace, common.enc
    result = {'status': 'BOUNDED_AUTHOR_DERIVED_PREFLIGHT_EXTERNAL_REVIEW_OPEN',
              'source_commit': '19d27b12c06500e2b1266e560a13f67974991f1d',
              'new_quadrature': False, 'new_RL_calculation': False,
              'adaptive_matrix_search': False, 'W9_changed': False,
              'full_energy_upper_claimed': False, 'milestone_4_closed': False,
              'algebra_controls': algebra_controls(), 'parities': {}}
    for par in ('even', 'odd'):
        data = json.loads(gzip.decompress(source['pairs_'+par]))
        candidate = json.loads(source['candidate_'+par])
        previous = json.loads(source['comparison_'+par])
        kp = json.loads(source['kp_'+par])
        need(candidate['pairs_sha256'] == digest(source['pairs_'+par]), 'Candidate pairs')
        need(kp['candidate_sha256'] == digest(source['candidate_'+par]), 'K candidate')
        need(previous['K_P_certificate_sha256'] == digest(source['kp_'+par]), 'Previous K')
        F = mat(data['Fhat'])
        c = arb_mat([[q(v)] for v in candidate['raw_coefficients']])
        c /= (c.transpose()*mat(data['G_W'])*c)[0, 0].sqrt()
        f = F*c
        af = inp.json('fresh_A12')['parities'][par]
        fs = inp.json('functions')['parities'][par]
        A_exact = exact_matrix(af['midpoint'])
        X0 = exact_matrix(inp.json('frozen_response')['parities'][par]['X'])
        old = old_inverse['parities'][par]
        S = (exact_matrix(old['inverse_lower_Loewner']) +
             exact_matrix(old['inverse_upper_Loewner'])) / 2
        variants = {'fixed_X': X0, 'exact_midpoint_inverse': A_exact.inv(),
                    'audit_S': S, 'scale_99_100': X0*fmpq(99, 100),
                    'scale_101_100': X0*fmpq(101, 100)}
        A = common.ratmat(rational_rows(A_exact))
        X0a = common.ratmat(rational_rows(X0))
        G0 = common.ratmat(inp.json('response')['parities'][par]['fixed_X']['physical_TT_adjoint_upper'])
        dF = q(fs['whole_F12_operator_error_upper'])
        dA = q(af['whole_Loewner_radius'])
        dD = q(fs['whole_D12_operator_error_upper'])
        Dmodel, column_bounds = response_norm(common, fs['functions'])
        Dactual = Dmodel + dD
        w = box(json.loads(source['weights'])[par]['partial_W9_norm_upper'])
        Eold = list(map(q, previous['partial_actual_energy_interval']))
        direct = box(kp['direct_form'])
        row = {'D_model_operator_norm_upper': Dmodel,
               'D_model_column_norm_upper': column_bounds,
               'D_actual_operator_norm_upper': Dactual,
               'partial_W9_norm_upper': w.upper(), 'variants': {}}
        for name, X in variants.items():
            need(X == X.transpose(), 'Candidate symmetry')
            Xa = common.ratmat(rational_rows(X))
            t = Xa*f
            dt = common.ratmat(rational_rows(X-X0))*f
            shift = (w.upper().sqrt()*Dactual*norm(dt)).upper()
            elo = max(arb(0), Eold[0].sqrt()-shift)**2
            ehi = (Eold[1].sqrt()+shift)**2
            center = direct-2*(f.transpose()*t)[0, 0]+(t.transpose()*A*t)[0, 0]
            tnorm = norm(t)
            error = (2*dF*tnorm+dA*tnorm**2).upper()
            kval = common.pad(center, error)
            # Whole-shell coefficient/error transport for the changed rule.
            M = common.ratmat(rational_rows(X*X0.inv()))
            GX = M*G0*M.transpose()
            whole_t = trace(GX).upper().sqrt()
            energy_interval = [enc(elo)[0], enc(ehi)[1]]
            budget_interval = enc(kval)
            lower_gap = q(energy_interval[0])-q(budget_interval[1])
            outcome = ('FIXED_COMPARISON_STILL_EXCLUDED' if
                       Fraction(energy_interval[0]) > Fraction(budget_interval[1]) else
                       'TRANSFER_BOUND_INCONCLUSIVE')
            if name == 'fixed_X':
                need(kval.overlaps(box(kp['K_P_interval'])), 'Original K replay control')
                need(outcome == 'FIXED_COMPARISON_STILL_EXCLUDED', 'Original witness lost')
            row['variants'][name] = {
                'matrix_sha256': matrix_digest(X),
                'matrix_difference_Frobenius_upper': norm(Xa-X0a),
                'direction_coefficient_change_upper': norm(dt),
                'partial_energy_norm_change_upper': shift,
                'transferred_partial_energy_interval': energy_interval,
                'new_K_P_interval': budget_interval,
                'new_direct_K_model_error_upper_for_direction': error,
                'new_whole_response_norm_upper': whole_t,
                'new_uniform_direct_K_model_error_upper': 2*dF*whole_t+dA*whole_t**2,
                'new_weighted_answer_model_error_upper': w.upper().sqrt()*dD*whole_t,
                'lower_energy_minus_new_budget_upper': lower_gap,
                'outcome': outcome}
        result['parities'][par] = row
    return common.encode(result)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repository', type=Path)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    need(__debug__, 'Do not use python -O')
    need(args.check or args.output is not None, 'Specify --check or --output')
    snapshot = {}
    if args.check:
        own = json.loads((HERE/'MANIFEST.json').read_bytes())
        for name, sha in own.items():
            path = (HERE/name).resolve()
            need(path.is_relative_to(HERE), 'Escaping package path')
            source_bytes = path.read_bytes()
            need(digest(source_bytes) == sha, 'Package binding: '+name)
            snapshot[name] = source_bytes
    else:
        snapshot['INPUT_BINDINGS.json'] = (HERE/'INPUT_BINDINGS.json').read_bytes()
    repository = args.repository if args.repository is not None else HERE.parents[2]
    raw = (json.dumps(run(repository.resolve(), snapshot['INPUT_BINDINGS.json']), indent=2)+'\n').encode()
    if args.check:
        need(raw == snapshot['EXPECTED.json'], 'Preflight replay differs')
        print('PASS: bounded preflight byte-equal; no quadrature or RL run')
    if args.output:
        args.output.write_bytes(raw)


if __name__ == '__main__':
    main()
