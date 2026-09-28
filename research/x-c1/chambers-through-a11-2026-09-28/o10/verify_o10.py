"""Exact supporting checks for PROOF.md; no numerical sampling or status writes.

The infinite-dimensional claims are proved in PROOF.md. This checker verifies
polynomial identities, rational certificates, support geometry, and source
bindings. It does not replace independent analytical review.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import subprocess


def poly_add(a, b):
    out = dict(a)
    for exponent, value in b.items():
        out[exponent] = out.get(exponent, F(0)) + value
    return {exponent: value for exponent, value in out.items() if value}


def poly_scale(a, factor):
    return {exponent: value * factor for exponent, value in a.items() if value * factor}


def poly_sub(a, b):
    return poly_add(a, poly_scale(b, -1))


def poly_mul(a, b):
    out = {}
    for ex, vx in a.items():
        for ey, vy in b.items():
            exponent = tuple(x + y for x, y in zip(ex, ey))
            out[exponent] = out.get(exponent, F(0)) + vx * vy
    return {exponent: value for exponent, value in out.items() if value}


def poly_power(a, n):
    out = {(0,) * len(next(iter(a))): F(1)}
    for _ in range(n):
        out = poly_mul(out, a)
    return out


def variable(n, j):
    return {tuple(int(k == j) for k in range(n)): F(1)}


def derivative(a):
    return {(ex[0] - 1,): value * ex[0] for ex, value in a.items() if ex[0]}


def evaluate(a, x):
    return sum((value * x ** ex[0] for ex, value in a.items()), F(0))


def integral(a, lo, hi):
    return sum((value * (hi ** (ex[0] + 1) - lo ** (ex[0] + 1)) / (ex[0] + 1)
                for ex, value in a.items()), F(0))


def shifted(a, shift):
    x_minus_shift = {(1,): F(1), (0,): -shift}
    out = {}
    for ex, value in a.items():
        out = poly_add(out, poly_scale(poly_power(x_minus_shift, ex[0]), value))
    return out


def source(radius, power):
    phi = poly_power({(0,): radius ** 2, (2,): F(-1)}, power)
    u = poly_sub(derivative(derivative(phi)), poly_scale(phi, F(1, 4)))
    return phi, u


def correlation(u, radius_u, v, radius_v, shift):
    lo = max(-radius_u, shift - radius_v)
    hi = min(radius_u, shift + radius_v)
    if lo >= hi:
        return F(0)
    return integral(poly_mul(u, shifted(v, shift)), lo, hi)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repository', type=Path,
                        help='Read source commits from this local Git repository.')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    # Rational certificates for every new scalar constant in the proof.
    exp_lower = sum((F(7, 10) ** k / (1 if k < 2 else (2 if k == 2 else 6))
                     for k in range(4)), F(0))
    check('exp(7/10) degree-3 lower certificate exceeds 2', exp_lower > 2)
    check('sqrt(8) lower certificate', F(14, 5) ** 2 < 8)
    check('w8 upper certificate from log(2) and sqrt(8)', F(7, 10) / F(14, 5) == F(1, 4))
    check('log(8) upper certificate', 3 * F(7, 10) == F(21, 10) < 3)
    check('post-wall envelope bound', F(23, 2) + 2 * F(1, 4) == 12)
    check('low-frequency trigonometric majorant below 8 xi^2', F(21, 10) ** 2 / 2 < 8)
    check('g0 low-frequency coefficient at the split', 4 / (F(1, 4) + F(1, 2) ** 2) == 8)
    check('g0 high-frequency floor at the split', 4 * F(1, 2) ** 2 / (F(1, 4) + F(1, 2) ** 2) == 2)
    check('high-frequency g0 >= 2 after cross multiplication',
          4 * F(1, 4) == 2 * F(1, 4) + F(1, 2))
    check('envelope ratio lower certificate', 10 / (10 + 2 * F(1, 4)) == F(20, 21))
    check('T wall norm bound', 1 + F(1, 4) == F(5, 4))
    check('D wall norm bound', 1 + 2 * F(1, 4) / 5 == F(11, 10))
    check('Gamma floor at A9', F(4, 3) == 4 / F(3))
    check('Jensen T floor', F(4, 3) ** 2 / (F(4, 3) + 12) == F(2, 15))
    check('source/T norm equivalence', 1 + 17 / F(2, 15) == F(257, 2))
    check('defect norm squared bound', 12 / F(2, 15) == 90)
    check('old image reserve conversion', 1 / F(5, 4) ** 2 == F(16, 25))

    # Formal polynomial identities, not values on a finite frequency grid.
    g, k, omega, c, v, z = [variable(6, j) for j in range(6)]
    one = {(0,) * 6: F(1)}
    m = poly_sub(poly_add(g, omega), c)
    n = poly_add(poly_add(k, omega), c)
    h = poly_add(poly_add(g, k), poly_scale(omega, 2))
    w = poly_sub(poly_sub(g, k), poly_scale(c, 2))
    dm = poly_mul(v, poly_sub(one, z))
    dn = poly_mul(v, poly_add(one, z))
    mp, np = poly_add(m, dm), poly_add(n, dn)
    hp = poly_add(h, poly_scale(v, 2))
    wp = poly_sub(w, poly_scale(poly_mul(v, z), 2))
    check('old m+n=h as a polynomial identity', poly_add(m, n) == h)
    check('new m+n=h as a polynomial identity', poly_add(mp, np) == hp)
    check('old full difference of Gram squares', poly_sub(poly_power(m, 2), poly_power(n, 2)) == poly_mul(h, w))
    check('new full difference of Gram squares', poly_sub(poly_power(mp, 2), poly_power(np, 2)) == poly_mul(hp, wp))
    check('new signed form differs by -2 w8 cos', poly_sub(wp, w) == poly_scale(poly_mul(v, z), -2))
    check('full T cross-term expansion', poly_power(mp, 2) == poly_add(poly_add(poly_power(m, 2), poly_scale(poly_mul(m, dm), 2)), poly_power(dm, 2)))
    check('full D cross-term expansion', poly_power(np, 2) == poly_add(poly_add(poly_power(n, 2), poly_scale(poly_mul(n, dn), 2)), poly_power(dn, 2)))
    check('T Gamma/new-channel cross coefficient retained', poly_power(mp, 2).get((1, 0, 0, 0, 1, 1)) == -2)
    check('T old/new Prime cross coefficient retained', poly_power(mp, 2).get((0, 0, 0, 1, 1, 1)) == 2)

    # Exact activation endpoints: exponentiating 2A makes the threshold 8 or 9.
    def prime_power(q):
        for p in range(2, q + 1):
            if any(p % d == 0 for d in range(2, p)):
                continue
            power = p
            while power < q:
                power *= p
            if power == q:
                return True
        return False
    check('strict A8 endpoint set', [q for q in range(2, 9) if prime_power(q) and q < 8] == [2, 3, 4, 5, 7])
    check('strict A9 endpoint set', [q for q in range(2, 10) if prime_power(q) and q < 9] == [2, 3, 4, 5, 7, 8])
    check('only q8 enters between endpoints', [q for q in range(8, 9) if prime_power(q)] == [8])

    # Physical polynomial probes: u=(d^2/dx^2-1/4)phi has both Mellin moments zero.
    # Boundary vanishing and the exact derivative factors justify this analytically.
    for radius in [F(1), F(9, 8)]:
        for power in [3, 4]:
            phi, u = source(radius, power)
            for sign in [-1, 1]:
                factor = poly_sub(derivative(phi), poly_scale(phi, F(sign, 2)))
                check(f'Mellin total derivative factor radius={radius}, power={power}, sign={sign}',
                      poly_add(derivative(factor), poly_scale(factor, F(sign, 2))) == u)
            check(f'boundary values and derivatives radius={radius}, power={power}',
                  all(evaluate(poly, end) == 0 for end in [-radius, radius]
                      for poly in [phi, derivative(phi), derivative(derivative(phi)), u]))
    _, old_u = source(F(1), 3)
    _, old_v = source(F(1), 4)
    for shift in [F(-5, 2), F(-2), F(2), F(5, 2)]:
        check(f'old cross-source translation vanishes at shift {shift}',
              correlation(old_u, F(1), old_v, F(1), shift) == 0)
    _, new_u = source(F(9, 8), 3)
    new_overlap = correlation(new_u, F(9, 8), new_u, F(9, 8), F(2))
    check('new support can have strictly nonzero channel correlation', new_overlap > 0)

    # Independent finite model: raw maps can change both norms while preserving q.
    # It obeys the stated wall bounds but the larger carrier has a negative direction.
    t_old, d_old = F(2), F(1)
    t_new, d_new = F(2107, 1040), F(1093, 1040)
    mt, md = t_new / t_old, d_new / d_old
    ga, gb_old, gb_new = 1 - (d_old / t_old) ** 2, 1 - (d_new / t_new) ** 2, F(-3)
    check('finite model form naturality', t_old ** 2 - d_old ** 2 == t_new ** 2 - d_new ** 2 == 3)
    check('finite model distinct bounded transports', mt != md and F(20, 21) <= mt ** 2 <= F(25, 16) and F(20, 21) <= md ** 2 <= F(121, 100))
    check('finite model defect intertwining', (d_new / t_new) * mt == md * (d_old / t_old))
    check('finite model Gram compression', mt ** 2 * gb_old == ga)
    check('finite model compensated norm changes', mt ** 2 - 1 == (d_old / t_old) ** 2 * (md ** 2 - 1))
    check('finite model raw transports are not isometries', mt ** 2 != 1 and md ** 2 != 1)
    check('positive old compression does not imply full positivity', ga > 0 and gb_old > 0 and gb_new < 0)
    for kind, ratio in [('T', mt), ('D', md)]:
        def transport(a, b):
            return ratio if a == 0 and b == 1 else F(1)
        for a in [0, 1]:
            for b in range(a, 2):
                for c_label in range(b, 2):
                    check(f'{kind} chamber cocycle {a}{b}{c_label}',
                          transport(b, c_label) * transport(a, b) == transport(a, c_label))

    binding_path = root / 'SOURCE_BINDINGS.json'
    bindings = json.loads(binding_path.read_text(encoding='utf-8'))
    source_state = 'NOT_RECHECKED_NO_REPOSITORY_GIVEN'
    if args.repository:
        for item in bindings['inputs']:
            content = subprocess.check_output(['git', 'show', item['commit'] + ':' + item['path']], cwd=args.repository)
            check('pinned input ' + item['label'], hashlib.sha256(content).hexdigest() == item['sha256'])
        source_state = 'ALL_PINNED_BYTES_VERIFIED'
    result = {
        'status': 'O10_EXACT_SUPPORTING_CHECKS_PASS',
        'checks_passed': len(checks), 'checks': checks,
        'analytical_proof': 'PROOF.md',
        'analytical_review': 'EXTERNAL_REVIEW_OPEN',
        'scope': 'Raw q8 wall, 1<=A<=B<=C<=log(3); no full post-wall positivity',
        'source_bindings': source_state,
        'new_support_probe_correlation_exact': str(new_overlap),
        'finite_negative_direction': str(gb_new),
        'file_sha256': {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
                        for name in ['PROOF.md', 'verify_o10.py', 'SOURCE_BINDINGS.json']},
        'repository_status_promotion': False, 'github_writes': False,
    }
    output = args.output or root / 'CHECK_RESULTS.json'
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'status': result['status'], 'checks_passed': len(checks),
                      'source_bindings': source_state, 'output': str(output)}))


if __name__ == '__main__':
    main()
