#!/usr/bin/env python3
"""Exact rational ledger for the complete reduced-core logarithmic shell gate.

The analytic whole-domain argument is in PROOF.md. No floating-point
calculation, numerical eigenvalue, quadrature, or finite shell model is used.
The dyadic width is verified symbolically, without constructing its denominator.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PARENT = 'research/x-c1/near-null-reduced-schur-direction-2026-09-19'
ANCHOR = 'd145ba88c86d4d0de665355bf3bff15844dbf414'
PUBLICATION_PARENT = '4ab3341f0e2190cc967affd460c1f370f7918ebc'
A_GAUGE = 'research/x-c1/a-gauge-conditioning-2026-09-19'
PAYLOAD = ['PROOF.md', 'README.md', 'STATUS_DE.md', 'check_all_core.py',
           'input_bindings.json', 'all_core_results.json', 'all_core_checks.log']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=HERE.parents[2])
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--write', action='store_true')
    modes.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    checks, ledger = [], {}

    def ok(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    def decimal(x, upper=False):
        x = F(x)
        scale = 10**36
        k = -((-x.numerator*scale)//x.denominator) if upper else (x.numerator*scale)//x.denominator
        sign = '-' if k < 0 else ''
        k = abs(k)
        return sign + str(k//scale) + '.' + str(k % scale).zfill(36)

    def value(name, lo, hi=None):
        lo = F(lo)
        hi = lo if hi is None else F(hi)
        if lo > hi:
            raise AssertionError(name + ' reversed interval')
        ledger[name] = {'lo': str(lo), 'hi': str(hi),
                        'outward_decimal': [decimal(lo), decimal(hi, True)]}

    binding = json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
    ok('input anchor is the inherited published research head', binding['anchor'] == ANCHOR)
    ok('publication parent preserves the concurrent A-gauge package', binding['publication_parent'] == PUBLICATION_PARENT)
    paths = [x['path'] for x in binding['files']]
    ok('57 distinct immutable input files', len(paths) == len(set(paths)) == 57)
    for item in binding['files']:
        raw = (root/item['path']).read_bytes()
        if len(raw) != item['bytes'] or hashlib.sha256(raw).hexdigest() != item['sha256']:
            raise AssertionError('input bytes/SHA256: ' + item['path'])
        if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() != item['git_blob']:
            raise AssertionError('input Git blob: ' + item['path'])
    ok('all input byte counts SHA256 and Git blob bindings match', True)
    print('Reproducing inherited full-shell direction and domain certificates', flush=True)
    environment = os.environ.copy()
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    replay = subprocess.run(
        [sys.executable, '-B', str(root/PARENT/'check_direction.py'), '--verify', '--root', str(root)],
        capture_output=True, text=True, check=True, env=environment)
    ok('parent direction 31 coordinate 28 and shell 43 checks reproduce',
       not replay.stderr and 'TOTAL 31 NEW EXACT CHECKS PASS' in replay.stdout
       and 'INHERITED coordinate replay: 28 PASS; full shell pivot replay: 43 PASS' in replay.stdout
       and 'REPLAY and all seven direction-package SHA256 hashes PASS' in replay.stdout)
    gauge_replay = subprocess.run(
        [sys.executable, '-B', str(root/A_GAUGE/'check_a_gauge.py'), '--verify', '--root', str(root)],
        capture_output=True, text=True, check=True, env=environment)
    ok('concurrent complete A-gauge theorem 9 arithmetic checks reproduce',
       not gauge_replay.stderr and 'TOTAL 9 A-GAUGE ARITHMETIC CHECKS PASS' in gauge_replay.stdout
       and 'REPLAY and all seven A-gauge package SHA256 hashes PASS' in gauge_replay.stdout)
    parent = json.loads((root/PARENT/'direction_results.json').read_text(encoding='utf-8'))
    vals = parent['values']

    def low(name):
        return F(vals[name]['lo'])

    def high(name):
        return F(vals[name]['hi'])

    eps, h0, sqrt_h0 = F(1, 10**13), F(1, 10**20), F(1, 10**10)
    delta = eps/32
    exponent = 10**16
    log_floor = F(exponent, 2)
    ok('physical inherited source gap and shell normalization', eps > 0 and delta == F(1, 32*10**13))
    ok('parent physical psi norm exceeds one half', low('psi_norm_squared') > F(1, 2))
    ok('parent physical psi energy is positive and below three twentieths',
       0 < low('q_psi_psi') <= high('q_psi_psi') < F(3, 20))
    tau_lo = eps*low('psi_norm_squared')/high('q_psi_psi')
    tau_hi = eps*high('psi_norm_squared')/low('q_psi_psi')
    ok('all-core trace reserve exceeds ten thirds epsilon', tau_lo > F(10, 3)*eps and tau_hi < 1)
    value('all_core_trace_reserve_tau', tau_lo, tau_hi)
    value('all_core_trace_operator_norm_upper', 0, 1-tau_lo)
    complement = 1-tau_lo-low('rho_e')
    ok('entire energy-orthogonal complement trace norm below 4.2e-11',
       0 < complement < F(42, 10**12))
    value('full_complement_trace_operator_norm_upper', 0, complement)
    value('trace_direction_complement_mixed_squared_upper', 0, high('rho_e')*complement)

    shell_loss = h0*(826+32*10**13*832**2)
    ok('uniform shell Young and moment losses are below three', shell_loss < 3)
    ok('growing shell floor exceeds log floor on whole original interval', 2*46-16-shell_loss > 46)
    value('shell_uniform_Young_and_moment_loss_upper', shell_loss)
    ok('sqrt h0 retained exactly without underflow', sqrt_h0**2 == h0)
    ok('physical even reflection radical bounded rationally', F(3, 2)**2 > 2)
    gamma_upper = 3 + F(15, 8)*sqrt_h0
    ok('full Carleman plus opposite-core Gamma coefficient below four', gamma_upper < 4)
    ok('all four arithmetic shifts plus Gamma coefficient below twelve', gamma_upper + 2*4 < 12)
    value('complete_L2_core_shell_pairing_coefficient_upper', 12)
    ok('chi Gamma Cauchy-Schwarz coefficient below forty', 106*15 < 40**2)
    ok('chi bounded remainder coefficient below sixty', 14**2*18 < 60**2)
    ok('moment residual coefficient below thirteen', 12 + 120*sqrt_h0 < 13)
    value('complete_residual_coefficient_upper', 13)
    ok('dyadic exponent is positive integer and at least eighty', isinstance(exponent, int) and exponent >= 80)
    ok('small integer power proves hstar below h0', 2**80 > 10**20)
    # log 2 > 1/2 follows analytically from integral_1^2 dx/x > 1/2.
    # Therefore log(2/h) >= (exponent+1)log 2 > exponent/2.
    ok('dyadic width implies required positive logarithmic floor', F(exponent+1, 2) > log_floor > 0)
    beta = F(169)/(eps*log_floor)
    ok('entire residual beta equals 169 over 500 and is below one', beta == F(169, 500) and beta < 1)
    sigma = (1-beta)*eps
    eta_margin_lo, eta_margin_hi = (1-beta)*tau_lo, (1-beta)*tau_hi
    target_margin = 2*eps
    ok('entire reduced-core relative margin exceeds 2e-13', eta_margin_lo > target_margin)
    ok('entire reduced-core absolute reserve is 331 over 500 epsilon', sigma == F(331, 500)*eps)
    value('dyadic_exponent', exponent)
    value('logarithmic_floor', log_floor)
    value('full_residual_relative_upper', beta)
    value('R0_absolute_lower', sigma)
    value('derived_Theta_margin_lower_bound', eta_margin_lo, eta_margin_hi)
    value('published_Theta0_upper', 1-target_margin)
    # For 0<x<1, 1-sqrt(1-x)>x/2; this is a strict block-form factor.
    ok('block square-root lower bound has a positive rational witness',
       0 < target_margin < 1 and (1-target_margin/2)**2 > 1-target_margin)
    physical = (target_margin/2)*delta/65
    ok('physical norm factor 65 and shell factor 32 both paid', physical == F(1, 2080*10**26))
    ok('original L2-gauge physical gap is strictly above 1e-30', physical > F(1, 10**30))
    value('original_L2_gauge_physical_gap_strict_lower', physical)
    ok('entire A-gauge relative bound is below nine twenty-fifths', beta < F(9, 25))
    gauge_physical = F(2, 5)*delta/65
    ok('A-gauge physical conversion pays forward 65 and shell 32', gauge_physical == F(1, 5200*10**13))
    ok('stronger A-gauge physical gap exceeds 1e-17', gauge_physical > F(1, 10**17))
    value('entire_A_gauge_Theta_upper', beta)
    value('physical_gap_strict_lower', gauge_physical)
    value('published_physical_gap_strict_lower', F(1, 10**17))
    old_beta_lower, old_beta_upper = F(169)/(47*eps), F(169)/(46*eps)
    ok('original h0 sufficient comparison fails without a negativity conclusion', old_beta_lower > 10**13)
    value('comparison_beta_at_original_h0', old_beta_lower, old_beta_upper)

    # Universal algebra in a rational Laurent polynomial ring. X and Y are
    # real/imaginary parts of a(w,psi), so their squared sum is |a(w,psi)|^2.
    names = ['Q', 'X', 'Y', 'A', 'W', 'n', 'eps', 'beta', 'ell', 'L']
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
            return self + -P.of(other)

        def __rsub__(self, other):
            return P.of(other) + -self

        def __mul__(self, other):
            d = {}
            for k, v in self.d.items():
                for j, u in P.of(other).d.items():
                    index = tuple(a+b for a, b in zip(k, j))
                    d[index] = d.get(index, F(0))+v*u
            return P(d)

        __rmul__ = __mul__

        def __eq__(self, other):
            return self.d == P.of(other).d

        def derivative(self, name):
            i = names.index(name)
            result = {}
            for k, v in self.d.items():
                if k[i]:
                    kk = list(k)
                    kk[i] -= 1
                    result[tuple(kk)] = k[i]*v
            return P(result)

    def var(name, power=1):
        key = list(zero)
        key[names.index(name)] = power
        return P({tuple(key): 1})

    Q, X, Y, A, W, n, ep, be, ell, L = [var(name) for name in names]
    Ai = var('A', -1)
    abs_g_squared = X*X+Y*Y
    ok('complex trace elimination cancels exactly in real and imaginary parts',
       Q-2*abs_g_squared*Ai+abs_g_squared*Ai == Q-abs_g_squared*Ai)
    ok('shifted positive-form Cauchy-Schwarz retains positive norm slack',
       A*Q-(Q-ep*W)*(A-ep*n) == ep*n*Q+ep*W*(A-ep*n))
    ok('trace residual annihilation is an exact Laurent identity', X-X*Ai*A == 0 and Y-Y*Ai*A == 0)
    ok('full residual majorant retains mixed trace terms exactly',
       ell+be*(Q-ell) == Q-(1-be)*(Q-ell))
    ok('operator majorant is beta I plus one-minus-beta trace operator',
       ell+be*(Q-ell) == be*Q+(1-be)*ell)
    ok('negative algebra control detects an omitted trace term', be*(Q-ell) != ell+be*(Q-ell))
    linear = 8*L+450
    square = (4*L+644)*(4*L+644)
    ok('uniform shell loss monotonicity derivatives are exact',
       linear-linear.derivative('L') == 8*L+442
       and square-square.derivative('L') == (4*L+644)*(4*L+636))

    report = {
        'status': 'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
        'anchor': ANCHOR,
        'publication_parent': PUBLICATION_PARENT,
        'verdict': 'ENTIRE-REDUCED-CORE-POSITIVE-ON-DYADIC-SUBINTERVAL / ORIGINAL-WIDTH-UNDECIDED',
        'certified_window': {'B': 'log(5)/2', 'h': '0 < h <= 2^(-10000000000000000)',
                             'width_base': 2, 'width_exponent': exponent,
                             'exact_positive_rational_width': True},
        'original_window': '0 < h <= 10^-20',
        'original_full_width_gate_certified': False,
        'all_core_operator_norm_certified_on_stated_subinterval': True,
        'even_all_source_continuation_on_stated_subinterval': True,
        'odd_continuation_closed': False,
        'negative_physical_source_certified': False,
        'fixed_near_null_source_changed': False,
        'mellin_constraints': 2, 'A1_used': False,
        'finite_core_or_shell_truncation': False,
        'bound_inputs': len(paths),
        'new_exact_checks': len(checks),
        'inherited_replay_checks': {'direction': 31, 'coordinate': 28, 'shell': 43, 'a_gauge': 9},
        'inherited_replay_stdout_sha256': hashlib.sha256(replay.stdout.encode('utf-8')).hexdigest(),
        'a_gauge_replay_stdout_sha256': hashlib.sha256(gauge_replay.stdout.encode('utf-8')).hexdigest(),
        'endpoint_theorem': 'Imported with physical epsilon=10^-13; not rerun in full here',
        'arithmetic': 'integer/Fraction; inherited outward interval endpoints; compressed exact dyadic power',
        'analytic_proof': 'PROOF.md; finite algebra does not replace the full-domain estimates',
        'passed_checks': checks, 'values': ledger,
    }
    jsontext = json.dumps(report, indent=2, sort_keys=True)+'\n'
    logtext = ('INHERITED direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS\n'
               + '\n'.join('PASS '+name for name in checks)+'\n'
               + '\n'.join(name+' '+str(v['outward_decimal']) for name, v in ledger.items())+'\n'
               + 'TOTAL '+str(len(checks))+' NEW EXACT CHECKS PASS\n'+report['verdict']+'\n')
    if args.write:
        (HERE/'all_core_results.json').write_text(jsontext, encoding='utf-8', newline='\n')
        (HERE/'all_core_checks.log').write_text(logtext, encoding='utf-8', newline='\n')
        manifest = ''.join(hashlib.sha256((HERE/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in PAYLOAD)
        (HERE/'SHA256SUMS').write_text(manifest, encoding='ascii', newline='\n')
    if args.verify:
        ok_bytes = ((HERE/'all_core_results.json').read_bytes() == jsontext.encode('utf-8')
                    and (HERE/'all_core_checks.log').read_bytes() == logtext.encode('utf-8'))
        if not ok_bytes:
            raise AssertionError('new JSON/log replay mismatch')
        entries = (HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        if [line.split('  ', 1)[1] for line in entries] != PAYLOAD:
            raise AssertionError('payload manifest membership/order')
        for line in entries:
            digest, name = line.split('  ', 1)
            if hashlib.sha256((HERE/name).read_bytes()).hexdigest() != digest:
                raise AssertionError('payload SHA256: '+name)
        print('REPLAY and all seven all-core-package SHA256 hashes PASS')
    print(logtext, end='')


if __name__ == '__main__':
    main()
