"""Directed scalar reweighting of bound #238 certificates; no integration."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from types import MappingProxyType, ModuleType

from flint import arb, ctx

HERE = Path(__file__).resolve().parent
OLD = Q(11, 10)
P_KEY = 'P_upper_J_star_nu'


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def snapshot(root, bindings):
    spec = json.loads(bindings)
    data = {}
    for alias, entry in spec['files'].items():
        path = (root / entry['path']).resolve()
        need(path.is_relative_to(root), 'Escaping input path')
        raw = path.read_bytes()
        need(sha(raw) == entry['sha256'], 'Input binding: ' + alias)
        data[alias] = raw
    common = ModuleType('bound_w9_majorant_common')
    common.__file__ = str(root / spec['files']['common']['path'])
    exec(compile(data['common'], common.__file__, 'exec'), common.__dict__)
    inputs = common.Inputs(binding_bytes=data['inherited_inputs'])
    return common, inputs, MappingProxyType(data)


def admissible(a, b, c):
    """Exact 2x2 PSD test, before any square roots or floating arithmetic."""
    return (a*(1-c) >= 1 and b*(1-c) >= 1 and
            (a*(1-c)-1)*(b*(1-c)-1) >= c)


def sharp_b(a, c):
    need(a*(1-c) > 1, 'Insufficient dual weight')
    return (a-1)/(a*(1-c)-1)


def partial(common, previous, budget, b):
    q, box, enc = common.q, common.box, common.enc
    scale = q(b/OLD)
    energies = previous['component_model_energies']
    errors = previous['feature_error_norms']
    model = sum((box(v)*(scale if k == P_KEY else 1)
                 for k, v in energies.items()), arb(0))
    # The coherent P-feature error, including a_fin exactly once, scales
    # with sqrt(b/(11/10)). The other three features do not change.
    ferr2 = sum((q(v[1])**2*(scale if k == P_KEY else 1)
                 for k, v in errors.items()), arb(0))
    ferr = ferr2.sqrt().upper()
    # Wpartial(b) <= max(1,b/(11/10)) Wpartial(old). This transports
    # the whole residual-model error without making a full-W norm claim.
    rerr = q(previous['residual_model_error_norm'][1]) * q(max(Q(1), b/OLD)).sqrt()
    need(model.lower() > 0, 'Nonpositive partial model energy')
    lo = max(arb(0), model.lower().sqrt()-ferr-rerr.upper())**2
    hi = (model.upper().sqrt()+ferr+rerr.upper())**2
    interval = [enc(lo)[0], enc(hi)[1]]
    if Q(interval[0]) > Q(budget[1]):
        outcome = 'PARTIAL_ENERGY_EXCLUDES_FOR_DIRECTION'
    elif Q(interval[1]) <= Q(budget[0]):
        outcome = 'PARTIAL_ENERGY_BELOW_ACTUAL_BUDGET_FOR_DIRECTION'
    else:
        outcome = 'INCONCLUSIVE_PARTIAL_ENERGY_FOR_DIRECTION'
    return {'P_weight': str(b), 'partial_model_energy': model,
            'reweighted_feature_error_norm_upper': ferr,
            'reweighted_residual_error_norm_upper': rerr.upper(),
            'partial_actual_energy_interval': interval,
            'K_P_interval_unchanged': budget,
            'lower_energy_minus_budget_upper': q(interval[0])-q(budget[1]),
            'budget_lower_minus_upper_energy': q(budget[0])-q(interval[1]),
            'outcome': outcome, 'full_energy_upper_claimed': False}


def run(root, bindings):
    need(__debug__, 'Do not use python -O')
    ctx.prec = 800
    common, inp, data = snapshot(root, bindings)
    receipt = json.loads(data['closure_acceptance'])['reserve_review']['independent_rational_review']
    need(receipt['source_zip_sha256'] == '65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba', 'Closure provenance')
    cap = {case['parity']: case for case in receipt['cases']}
    q, enc = common.q, common.enc
    out = {'status': 'AUTHOR_DERIVED_EXTERNAL_REVIEW_OPEN',
           'source_commit': '5e5462d478cf700797de80dd0a77f7e7d0f20ad7',
           'response_matrix_changed': False, 'frozen_directions_changed': False,
           'new_integrations': False, 'RL_computed': False,
           'N12_closed': False, 'milestone_4_closed': False, 'parities': {}}
    for par in ('even', 'odd'):
        previous = json.loads(data['comparison_'+par])
        candidate = json.loads(data['candidate_'+par])
        kp = json.loads(data['kp_'+par])
        need(candidate['pairs_sha256'] == sha(data['pairs_'+par]), 'Candidate pairing binding')
        need(previous['pairs_sha256'] == sha(data['pairs_'+par]), 'Comparison pairing binding')
        need(previous['raw_coefficients'] == candidate['raw_coefficients'], 'Frozen coefficients')
        need(kp['candidate_sha256'] == sha(data['candidate_'+par]), 'Frozen K candidate')
        need(previous['K_P_certificate_sha256'] == sha(data['kp_'+par]), 'K certificate binding')
        budget = previous['budget_interval_or_upper']
        need(Q(budget[0]) <= Q(kp['K_P_interval'][0]) and
             Q(budget[1]) >= Q(kp['K_P_interval'][1]), 'Same outward K enclosure')
        inverse = inp.json('inverse_'+par)
        c = Q(cap[par]['new_simple_cap'])
        beta = Q(inverse['beta'])
        need(Q(cap[par]['beta']) == beta, 'Same beta')
        need(Q(cap[par]['new_complete_QR_upper']) < c < Q(inverse['residual_cap']) < Q(1,121), 'Full residual cap')
        a = OLD
        b = sharp_b(a, c)
        need(admissible(a, b, c) and b < OLD, 'Loewner improvement')
        need(not admissible(a, b-Q(1,10**12), c), 'Illicit factor decrease rejected')
        need(not admissible(Q(1), Q(1), c), 'Unpaid cross term rejected')
        variants = {'original': (OLD, OLD), 'same_dual_sharper_P': (a, b)}
        # An explicit admissible trade, not a claimed global improvement:
        # lower P weight, higher full-dual weight.
        bt = Q(51, 50)
        at = sharp_b(bt, c)  # symmetric boundary equation
        need(admissible(at, bt, c), 'Trade admissibility')
        variants['P_51_50_dual_trade'] = (at, bt)
        row = {'beta': str(beta), 'full_residual_cap': str(c),
               'original_residual_cap': inverse['residual_cap'],
               'matrix_unchanged_sha256': sha(json.dumps(inp.json('frozen_response')['parities'][par]['X'], separators=(',', ':')).encode()),
               'candidate_sha256': sha(data['candidate_'+par]),
               'variants': {}}
        for name, (a, b) in variants.items():
            need(admissible(a, b, c), 'Variant admissibility')
            result = partial(common, previous, budget, b)
            result.update(dual_weight=str(a), coefficient_before_RL=str(a/beta),
                          coefficientwise_no_larger_than_old=(a <= OLD and b <= OLD),
                          admissibility_determinant=str((a*(1-c)-1)*(b*(1-c)-1)-c))
            # Conditional sufficient threshold for the ACTUAL full dual
            # energy B=<nu,RL nu>, after all its own errors are paid.
            room = q(budget[0])-q(result['partial_actual_energy_interval'][1])
            result['sufficient_actual_RL_upper_threshold'] = room*q(beta/a)
            if name == 'original':
                old = previous['partial_actual_energy_interval']
                need(Q(result['partial_actual_energy_interval'][0]) <= Q(old[1]) and
                     Q(result['partial_actual_energy_interval'][1]) >= Q(old[0]), 'Old interval consistency')
            row['variants'][name] = result
        # b>=1 for the entire admissible diagonal-Young family (even for
        # any hypothetical smaller c>=0). This is a lower comparison,
        # NOT an inverse majorant. Its even rejection excludes the family.
        floor = partial(common, previous, budget, Q(1))
        floor['is_inverse_majorant'] = False
        floor['role'] = 'AUXILIARY_FAMILY_LOWER_COMPARISON_ONLY'
        row['universal_P_weight_one_floor'] = floor
        out['parities'][par] = row
    need(out['parities']['even']['universal_P_weight_one_floor']['outcome'] ==
         'PARTIAL_ENERGY_EXCLUDES_FOR_DIRECTION', 'Even family obstruction')
    need(all(out['parities'][p]['variants']['same_dual_sharper_P']['outcome'] ==
             'PARTIAL_ENERGY_EXCLUDES_FOR_DIRECTION' for p in ('even','odd')), 'Sharp variant decisions')
    need(out['parities']['odd']['variants']['P_51_50_dual_trade']['outcome'] ==
         'PARTIAL_ENERGY_BELOW_ACTUAL_BUDGET_FOR_DIRECTION', 'Odd trade decision')
    out['controls'] = {'unpaid_cross_term_rejected': True,
                       'below_admissible_P_weight_rejected': True,
                       'same_bound_response_directions_and_budgets': True}
    return common.encode(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repository', type=Path)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    need(__debug__, 'Do not use python -O')
    need(args.check or args.output is not None, 'Specify --check or --output')
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
    raw = (json.dumps(run(root, checked['INPUT_BINDINGS.json']), indent=2)+'\n').encode()
    if args.check:
        need(raw == checked['EXPECTED.json'], 'Majorant preflight replay differs')
        print('PASS: majorant preflight byte-equal; no integration or RL solve')
    if args.output:
        args.output.write_bytes(raw)


if __name__ == '__main__':
    main()
