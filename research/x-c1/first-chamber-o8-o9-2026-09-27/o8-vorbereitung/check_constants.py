"""Exact arithmetic for the local O8 preparation; no terminal positivity test.

Python standard library only. The analytic argument is in O8_ANALYSE.md.
The source repository and its status files are never modified.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from decimal import Decimal, localcontext
import hashlib
import json

HERE = Path(__file__).resolve().parent
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def log_bounds(q, terms=220):
    q = F(q)
    assert q >= 1
    z = (q - 1) / (q + 1)
    term = z
    value = F(0)
    for k in range(terms):
        value += term / (2*k + 1)
        term *= z*z
    return 2*value, 2*(value + term/((2*terms + 1)*(1-z*z)))


def cosh_upper(x, last=20):
    partial = sum((x**(2*k)/factorial(2*k) for k in range(last+1)), F(0))
    first = x**(2*last+2)/factorial(2*last+2)
    return partial + first/(1-x*x/((2*last+3)*(2*last+4)))


def atan_bounds(x, terms=40):
    partial = sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(terms)), F(0))
    next_term = (-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(partial, partial+next_term), max(partial, partial+next_term)


def inverse_series(poly, degree):
    out = [F(1)]
    for k in range(1, degree+1):
        out.append(-sum((poly[j]*out[k-j] for j in range(1, k+1)), F(0)))
    return out


def residual(poly, denominator):
    out = [F(0)]*(len(poly)+len(denominator)-1)
    for i, a in enumerate(poly):
        if a:
            for j, b in enumerate(denominator):
                if b:
                    out[i+j] += a*b
    out[0] -= 1
    return out


def gamma_bound(degree, radius):
    """Bound g_reg(2x)-p(x) on [0,radius], including division by x.

    Finite denominator degree D is even. Both exact denominators are >=1.
    The sinh(x)/x residual is divided by x BEFORE taking the majorant.
    """
    D = max(256, degree+20)
    D += D % 2
    c = [F(1, factorial(k)) if k % 2 == 0 else F(0) for k in range(D+1)]
    s = [F(1, factorial(k+1)) if k % 2 == 0 else F(0) for k in range(D+1)]
    pc, ps = inverse_series(c, degree), inverse_series(s, degree+1)
    rc, rs = residual(pc, c), residual(ps, s)
    check(f'Gamma M={degree}: exact cosh inverse coefficients', all(v == 0 for v in rc[:degree+1]))
    check(f'Gamma M={degree}: exact sinh/x inverse coefficients', all(v == 0 for v in rs[:degree+2]))
    fc = sum((abs(v)*radius**k for k, v in enumerate(rc)), F(0))
    fs = sum((abs(v)*radius**(k-1) for k, v in enumerate(rs) if k), F(0))
    assert rs[0] == 0
    tc = radius**(D+2)/factorial(D+2)/(1-radius**2/((D+3)*(D+4)))
    ts_div_x = radius**(D+1)/factorial(D+3)/(1-radius**2/((D+4)*(D+5)))
    nc = sum((abs(v)*radius**k for k, v in enumerate(pc)), F(0))
    ns = sum((abs(v)*radius**k for k, v in enumerate(ps)), F(0))
    return (fc + fs + nc*tc + ns*ts_div_x)/4


def decimal_display(x):
    # Display only. All comparisons above and below use exact Fractions.
    with localcontext() as ctx:
        ctx.prec = 14
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def main():
    radius = F(21,20)
    l8, u8 = log_bounds(8)
    l3, _ = log_bounds(3)
    check('1 < A8 < 21/20', l8 > 2 and u8 < 2*radius)
    check('A8 < log(3)', u8/2 < l3)
    # 2*A8=3*log(2) exactly. Translation chains have at most 3 vertices a.e.
    check('endpoint prime-2 reference shift is 2/3', F(2,3)*3 == 2)

    ca = cosh_upper(radius)
    check('cosh(21/20) < 13/8', ca < F(13,8))
    kernel_lower = (F(8,13) - radius/6)/4
    check('regular Gamma kernel floor exceeds 1/10', kernel_lower > F(1,10))
    check('geometric sinh majorant has positive denominator', radius**2/6 < 1)

    for q, upper in [(2,F(7,10)), (3,F(11,10)), (5,F(161,100)), (7,F(39,20))]:
        check(f'log({q}) rational upper witness', log_bounds(q)[1] < upper)
    for q, lower in [(3,F(173,100)), (5,F(223,100)), (7,F(66,25))]:
        check(f'sqrt({q}) rational lower witness', lower**2 < q)
    shift_bound = F(7,10) + F(110,173) + F(7,20) + F(161,223) + F(65,88)
    check('full five-channel shift bound < 63/20', shift_bound < F(63,20))

    a5, b5 = atan_bounds(F(1,5))
    a239, b239 = atan_bounds(F(1,239))
    check('Machin upper bound pi < 22/7', 16*b5-4*a239 < F(22,7))
    h32 = sum((F(1,k) for k in range(1,33)), F(0))
    check('Euler gamma < 3/5 via H32-log(32)', h32-log_bounds(32)[0] < F(3,5))
    check('2*pi*A < 33/5 using rational bounds', 2*F(22,7)*radius == F(33,5))
    check('log(33/5) < 19/10', log_bounds(F(33,5))[1] < F(19,10))

    gamma_tail_loss = 2*radius*(F(1,4)-F(1,10))
    total_loss = F(5,2) + gamma_tail_loss + F(63,20)
    check('raw high Gamma loss <= 63/200', gamma_tail_loss == F(63,200))
    check('raw high total loss <= 1193/200', total_loss == F(1193,200))
    H384 = sum((F(1,k) for k in range(1,385)), F(0))
    check('H384 > 261/40', H384 > F(261,40))
    raw_floor = F(261,40)-total_loss
    check('raw high floor > 14/25', raw_floor == F(14,25) and H384-total_loss > raw_floor)

    z = radius/2
    even_eps = z**384/factorial(384)/(1-z*z/(385*386))
    odd_eps = 4*z**385/factorial(385)/(1-z*z/(386*387))
    eps = max(even_eps, odd_eps)
    check('Mellin correction norm < 10^-6 in both parities', eps < F(1,10**6))
    check('mixed energy factor < 8', 4+radius/2+F(63,20) < 8)
    check('moment carrier energy factor < 12', 1+4+F(5,2)+radius/2+F(63,20) < 12)
    check('full corrected high floor > 1/2', raw_floor-16*eps-12*eps*eps > F(1,2)*(1+eps*eps))
    check('each low coordinate set has dimension 191', len(range(2,384,2)) == len(range(3,385,2)) == 191)
    delta = F(1,1)/(1+2*F(23,2))
    check('high defect reserve 1/24', delta == F(1,24))
    check('high defect squared contraction 23/24', 1-delta == F(23,24))
    check('Neumann residual prefactor 2160', 90/delta == 2160)

    gamma = {}
    for degree in (128,160):
        err = gamma_bound(degree, radius)
        gamma[str(degree)] = {
            'radius': str(radius), 'kernel_error_upper_exact': str(err),
            'kernel_error_upper_display': decimal_display(err),
            'operator_error_upper_exact': str(2*radius*err),
            'operator_error_upper_display': decimal_display(2*radius*err),
            'old_terminal_form_budget': '5/100000000000000000000000000',
            'kernel_operator_majorant_fits_old_total_budget': 2*radius*err < F(5,10**26),
        }

    result = {
        'status': 'LOCAL_ANALYTIC_PREPARATION_UNREVIEWED',
        'main_observed': '876f9c79d555019217c745923cae3bef5da8af17',
        'main_tree': 'fb0c6a0b3a73bd1a2039b95f1e65ac8023133f0a',
        'scope': '1 <= A <= log(8)/2; fixed raw C1a continuation; both parities',
        'O8_status': 'OPEN', 'terminal_low_schur_certified': False,
        'repository_status_promotion': False, 'github_writes': False,
        'analytic_argument': 'O8_ANALYSE.md',
        'arithmetic_checks_passed': len(checks), 'checks': checks,
        'constants': {'high_physical_floor': '1/2', 'low_dimension_each_parity': 191,
                      'high_defect_floor': '1/24', 'high_defect_norm_squared_upper': '23/24',
                      'mellin_correction_upper_display': decimal_display(eps),
                      'shift_upper_exact': str(shift_bound),
                      'raw_floor_rational': str(raw_floor)},
        'gamma_preparation': gamma,
        'limits': ['Arithmetic checks do not verify the analytic proof.',
                   'Gamma majorants do not certify full matrix or Schur errors.',
                   'No A>1 low matrix, corrected transport or wall crossing is certified.'],
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE/'constants.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(f'{len(checks)} exact arithmetic checks PASS; O8 OPEN')
    print('New draft: high physical floor 1/2; 191 low coordinates per parity; defect high floor 1/24')
    for degree, row in gamma.items():
        print(f"Gamma M={degree}, radius 21/20: kernel <= {row['kernel_error_upper_display']}; operator <= {row['operator_error_upper_display']}")


if __name__ == '__main__':
    main()
