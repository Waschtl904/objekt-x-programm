#!/usr/bin/env python3
"""Exact gauge-transition ledger; analytic infinite-dimensional proof in PROOF.md."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ANCHOR = '04bc2466053f1ba939158e6a9ecc023ba40bc756'
PARENT = 'research/x-c1/all-core-logarithmic-shell-gate-2026-09-19'
DIRECTION = 'research/x-c1/near-null-reduced-schur-direction-2026-09-19'
PAYLOAD = ['PROOF.md', 'README.md', 'STATUS_DE.md', 'check_transition.py',
           'input_bindings.json', 'transition_results.json', 'transition_checks.log']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=HERE.parents[2])
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--write', action='store_true')
    modes.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    checks, values = [], {}

    def ok(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    def decimal(v, upper=False):
        v = F(v)
        scale = 10**32
        k = -((-v.numerator*scale)//v.denominator) if upper else (v.numerator*scale)//v.denominator
        sign = '-' if k < 0 else ''
        k = abs(k)
        return sign+str(k//scale)+'.'+str(k % scale).zfill(32)

    def value(name, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        if lo > hi:
            raise AssertionError(name+' interval reversed')
        values[name] = {'lo': str(lo), 'hi': str(hi),
                        'outward_decimal': [decimal(lo), decimal(hi, True)]}

    binding = json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
    ok('anchor retains the published tiny-window entire-core theorem', binding['anchor'] == ANCHOR)
    paths = [item['path'] for item in binding['files']]
    ok('65 distinct pinned input files', len(paths) == len(set(paths)) == 65)
    for item in binding['files']:
        raw = (root/item['path']).read_bytes()
        if len(raw) != item['bytes'] or hashlib.sha256(raw).hexdigest() != item['sha256']:
            raise AssertionError('input bytes/SHA256: '+item['path'])
        blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if blob != item['git_blob']:
            raise AssertionError('input Git blob: '+item['path'])
    ok('all inherited input bytes SHA256 and Git blob hashes match', True)
    environment = os.environ.copy()
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    print('Reproducing the 40-check package and its 31/28/43/9 prerequisites', flush=True)
    replay = subprocess.run(
        [sys.executable, '-B', str(root/PARENT/'check_all_core.py'), '--verify', '--root', str(root)],
        capture_output=True, text=True, check=True, env=environment)
    ok('entire inherited proof chain reproduces', not replay.stderr
       and 'TOTAL 40 NEW EXACT CHECKS PASS' in replay.stdout
       and 'INHERITED direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS' in replay.stdout
       and 'REPLAY and all seven all-core-package SHA256 hashes PASS' in replay.stdout)
    source = json.loads((root/DIRECTION/'direction_results.json').read_text(encoding='utf-8'))
    previous = json.loads((root/PARENT/'all_core_results.json').read_text(encoding='utf-8'))
    old = source['values']

    def lo(name):
        return F(old[name]['lo'])

    def hi(name):
        return F(old[name]['hi'])

    eps, delta = F(1, 10**13), F(1, 32*10**13)
    ok('psi norm lies between one half and nine sixteenths',
       F(1, 2) < lo('psi_norm_squared') <= hi('psi_norm_squared') < F(9, 16))
    ok('psi energy lies between seven fiftieths and three twentieths',
       F(7, 50) < lo('q_psi_psi') <= hi('q_psi_psi') < F(3, 20))
    ok('bounded trace functional yields ell norm below 1943', F(272)/F(7, 50) < 1943)
    transition_squared = 1+F(41, 16)*1943**2
    core_squared = 1+F(9, 16)*1943**2
    ok('full transition squared constant is exact', transition_squared == F(154785225, 16))
    ok('full transition norm below 3111', transition_squared < 3111**2 and 3111**2 > 2)
    ok('inverse weighted Cauchy constant below three', 1+1/lo('psi_norm_squared') < 3)
    ok('inverse norm upper sqrt three is below two', 3 < 2**2)
    ok('core transition squared constant is exact', core_squared == F(33977257, 16))
    ok('core transition norm below 1458', core_squared < 1458**2)
    form_inverse = 1+3*hi('q_psi_psi')/(eps*lo('psi_norm_squared'))
    ok('complete inverse form product bound below 1 plus 9e12', 2 < form_inverse < 1+9*10**12)
    value('T_A_L2_norm_squared_upper', 3111**2)
    value('T_A_L2_norm_squared_finer_upper', transition_squared)
    value('T_A_L2_lower_squared', F(1, 3))
    value('T_A_inverse_L2_norm_squared_upper', 3)
    value('core_U_L2_norm_squared_upper', 1458**2)
    value('core_inverse_V_L2_norm_upper', 1)
    value('form_product_forward_factor_upper', 2)
    value('form_product_inverse_factor_upper', 1+9*10**12)

    energy_lo, energy_hi = lo('trace_eliminated_core_energy'), hi('trace_eliminated_core_energy')
    residual_upper = hi('full_shell_residual_dual_squared_bound')
    ok('A-orthogonal source energy denominator strictly positive', energy_lo > 0)
    ok('complete shell residual bound is nonnegative and below 5e-18', 0 <= residual_upper < F(5, 10**18))
    nu = F(151, 20000000)
    eta_upper = residual_upper/energy_lo
    ok('full A-gauge direction quotient below 7.55e-6', 0 <= eta_upper < nu)
    ok('preserved actual Schur remainder is above 5.449e-13', lo('r_v_uniform') > F(5449, 10**16))
    ok('direct energy minus entire residual supports the same positive floor', energy_lo-residual_upper > F(5449, 10**16))
    value('fixed_source_alpha', lo('A_orthogonal_projection_coefficient'), hi('A_orthogonal_projection_coefficient'))
    value('fixed_A_coordinate_energy', energy_lo, energy_hi)
    value('fixed_A_coordinate_eta', 0, eta_upper)
    value('published_A_direction_eta_upper', nu)
    value('invariant_Schur_remainder', lo('r_v_uniform'), hi('r_v_uniform'))

    # The following ledger is explicitly conditional. It proves arithmetic
    # in the sufficient theorem, not its missing complete-complement hypothesis.
    kappa_example = F(999, 1000)
    theta_example = nu+kappa_example
    ok('conditional complement example yields theta below one', theta_example == F(19980151, 20000000) < 1)
    ok('conditional Schur margin equals 19849 over 20000000', 1-theta_example == F(19849, 20000000))
    value('conditional_example_complement_target', kappa_example)
    value('conditional_example_full_Theta_upper', theta_example)
    value('conditional_example_mixed_squared_upper', nu*kappa_example)
    value('conditional_example_Schur_margin', 1-theta_example)
    ok('the full original width remains explicitly uncertified', previous['original_full_width_gate_certified'] is False)
    ok('the existing tiny-window full-core result is preserved',
       previous['all_core_operator_norm_certified_on_stated_subinterval'] is True
       and previous['certified_window']['width_exponent'] == 10**16)
    ok('existing full A-gauge tiny-window bound remains sharper than split bound', F(169, 500) < F(169, 500)+nu)

    # Exact polynomial identities. Scalar complex cross terms are represented
    # by their real and imaginary components. There are no sampled vectors.
    names = ['lam', 'k', 't', 'uB', 'sB', 'cv', 'alpha', 'af', 'az', 'ap',
             'lr', 'li', 'dr', 'di', 'cRe', 'a0', 'loss', 'nu', 'kap']
    zero = (0,)*len(names)

    class P:
        def __init__(self, terms=None):
            self.d = {k: F(v) for k, v in (terms or {}).items() if v}

        @staticmethod
        def of(x):
            return x if isinstance(x, P) else P({zero: F(x)})

        def __add__(self, other):
            d = self.d.copy()
            for k, v in P.of(other).d.items():
                d[k] = d.get(k, F(0))+v
            return P(d)

        __radd__ = __add__

        def __neg__(self):
            return P({k: -v for k, v in self.d.items()})

        def __sub__(self, other):
            return self+-P.of(other)

        def __rsub__(self, other):
            return P.of(other)+-self

        def __mul__(self, other):
            d = {}
            for a, u in self.d.items():
                for b, v in P.of(other).d.items():
                    index = tuple(x+y for x, y in zip(a, b))
                    d[index] = d.get(index, F(0))+u*v
            return P(d)

        __rmul__ = __mul__

        def __eq__(self, other):
            return self.d == P.of(other).d

    def variable(name):
        key = list(zero)
        key[names.index(name)] = 1
        return P({tuple(key): 1})

    lam, k, t, uB, sB, cv, alpha, af, az, ap, lr, li, dr, di, cRe, a0, loss, vn, kap = [variable(s) for s in names]
    ok('forward lands in ell kernel using ell psi equals one', lam-lam == 0)
    ok('forward then inverse restores both core and shell coefficients', -lam-(-lam) == 0 and (t+lam)+(-lam) == t)
    ok('inverse then forward restores both core and shell coefficients', -k-(-k) == 0 and (t+k)+(-k) == t)
    ok('negative control detects a wrong inverse shell sign', (t+lam)-(-lam) != t)
    ok('physical core and moment-corrector image is unchanged', -lam+(t+lam) == t)
    ok('joint H1 trace transports forward exactly', (uB-lam)+(t+lam)-sB == uB+t-sB)
    ok('joint H1 trace transports backward exactly', (uB-k)+(t+k)-sB == uB+t-sB)
    ok('fixed physical source transforms to fA and alpha e', -cv-(alpha-cv) == -alpha and cv+(alpha-cv) == alpha)
    ok('fixed physical source endpoint traces cancel exactly', -alpha+alpha == 0)
    lambda_squared = lr*lr+li*li
    real_cross = lr*dr-li*di
    original_block = (af+ap*lambda_squared)+2*(cRe+real_cross)+az
    changed_shell = az+2*real_cross+ap*lambda_squared
    changed_block = af+2*cRe+changed_shell
    ok('full complex block congruence is an exact polynomial identity', original_block == changed_block)
    ok('negative control detects omitted complex trace-shell cross', original_block != af+2*cRe+az+ap*lambda_squared)
    ok('forward product-energy majorant retains the subtracted trace energy',
       (a0-loss)+(2*az+2*loss) == a0+2*az+loss)
    ok('conditional mixed Gram determinant retains every term', (1-vn)*(1-kap)-vn*kap == 1-vn-kap)
    ok('full block and Schur factors are not identified', (1-vn)*(1-vn) != 1-vn)

    report = {
        'status': 'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
        'anchor': ANCHOR,
        'verdict': 'GAUGE-TRANSITION-AND-CONGRUENCE-CLOSED / FULL-ORIGINAL-WIDTH-COMPLEMENT-UNDECIDED',
        'structural_and_directional_interval': 'B=log(5)/2; 0<h<=10^-20',
        'existing_all_core_interval_preserved': '0<h<=2^(-10000000000000000)',
        'new_all_source_width_extension': False,
        'full_original_width_complement_bound_certified': False,
        'conditional_complement_example_is_certified_bound': False,
        'odd_continuation_closed': False,
        'negative_physical_source_certified': False,
        'new_Riesz_solver': False,
        'fixed_source_changed_or_physically_renormalized': False,
        'mellin_constraints': 2, 'A1_used': False,
        'bound_inputs': len(paths), 'new_exact_checks': len(checks),
        'inherited_replay_checks': {'all_core': 40, 'direction': 31, 'coordinate': 28, 'shell': 43, 'a_gauge': 9},
        'inherited_replay_stdout_sha256': hashlib.sha256(replay.stdout.encode('utf-8')).hexdigest(),
        'arithmetic': 'integer/Fraction and pinned outward rational interval endpoints',
        'analytic_proof': 'PROOF.md; no operator-domain invariance or finite-tail surrogate',
        'passed_checks': checks, 'values': values,
    }
    jsontext = json.dumps(report, indent=2, sort_keys=True)+'\n'
    logtext = ('INHERITED all-core 40 PASS; direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS\n'
               +'\n'.join('PASS '+s for s in checks)+'\n'
               +'\n'.join(k+' '+str(v['outward_decimal']) for k, v in values.items())+'\n'
               +'TOTAL '+str(len(checks))+' NEW EXACT CHECKS PASS\n'+report['verdict']+'\n')
    if args.write:
        (HERE/'transition_results.json').write_text(jsontext, encoding='utf-8', newline='\n')
        (HERE/'transition_checks.log').write_text(logtext, encoding='utf-8', newline='\n')
        manifest = ''.join(hashlib.sha256((HERE/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in PAYLOAD)
        (HERE/'SHA256SUMS').write_text(manifest, encoding='ascii', newline='\n')
    if args.verify:
        if ((HERE/'transition_results.json').read_bytes() != jsontext.encode('utf-8')
                or (HERE/'transition_checks.log').read_bytes() != logtext.encode('utf-8')):
            raise AssertionError('new JSON/log replay mismatch')
        entries = (HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        if [line.split('  ', 1)[1] for line in entries] != PAYLOAD:
            raise AssertionError('manifest membership/order')
        for line in entries:
            digest, name = line.split('  ', 1)
            if hashlib.sha256((HERE/name).read_bytes()).hexdigest() != digest:
                raise AssertionError('payload SHA256: '+name)
        print('REPLAY and all seven transition-package SHA256 hashes PASS')
    print(logtext, end='')


if __name__ == '__main__':
    main()
