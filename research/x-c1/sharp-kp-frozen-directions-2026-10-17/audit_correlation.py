"""Independent numerical control, not a directed bound or external review.

Evaluate the physical lift with local Legendre polynomials and integrate each
real overlap numerically. No polynomial-product or exponential primitives from
the certifier are used by this second calculation.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from fractions import Fraction
import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
mp.mp.dps = 100

def number(value):
    value = Fraction(value)
    return mp.mpf(value.numerator) / value.denominator

def midpoint(pair):
    return (number(pair[0]) + number(pair[1])) / 2

def main():
    nodes, weights = mp.gauss_quadrature(64, "legendre")
    def integrate(f, lo, hi):
        mid, half = (lo + hi) / 2, (hi - lo) / 2
        return half * mp.fsum(w * f(mid + half * x) for x, w in zip(nodes, weights))
    a, b = mp.log(3), mp.log(11) / 2
    h = b - a
    maxima = []
    with tempfile.TemporaryDirectory(prefix="objekt-x-correlation-audit-") as td:
        for parity in ("even", "odd"):
            env = dict(os.environ, OBJEKT_X_SHARP_K_OUTPUT=td,
                       OBJEKT_X_CORRELATION_PROBE="1")
            subprocess.run([sys.executable, "-B", str(HERE / "certify.py"), parity],
                           env=env, check=True)
            probe = json.loads((Path(td) / f"CORRELATION_PROBE_{parity}.json").read_text())
            candidate = json.loads((ROOT / "research/x-c1/shell-polynomial-direction-search-2026-10-17/data" / f"FROZEN_{parity}.json").read_text())
            coefficients = list(map(number, candidate["raw_exact_rational_coefficients"]))
            eps = 1 if parity == "even" else -1
            m = lambda x: mp.cosh(x / 2) if eps == 1 else mp.sinh(x / 2)
            mu = (eps * a + mp.sinh(a)) / 2
            def raw(x):
                t = 2 * (x - a) / h - 1
                return mp.fsum(c * mp.sqrt((2 * j + 1) / (2 * h)) * mp.legendre(j, t)
                               for j, c in enumerate(coefficients))
            lamraw = integrate(lambda x: raw(x) * m(x), a, b)
            norm = mp.sqrt(mp.fsum(c * c for c in coefficients) + 2 * lamraw ** 2 / mu)
            amplitude = -lamraw / (mu * norm)
            pieces = [(-b, -a, lambda x: eps * raw(-x) / norm),
                      (-a, a, lambda x: amplitude * m(x)),
                      (a, b, lambda x: raw(x) / norm)]
            differences = []
            for row in probe:
                r = midpoint(row["r"])
                direct = mp.mpf(0)
                for ai, bi, fi in pieces:
                    for aj, bj, fj in pieces:
                        lo, hi = max(ai, aj-r), min(bi, bj-r)
                        if hi > lo:
                            direct += integrate(lambda x: fi(x) * fj(x+r), lo, hi)
                differences.append(abs(direct-midpoint(row["C"])))
            maximum = max(differences)
            assert maximum < mp.mpf("1e-60"), (parity, maximum)
            maxima.append(maximum)
            print(parity, len(probe), "physical autocorrelation controls; max difference",
                  mp.nstr(maximum, 8), flush=True)
    print("PASS: 24 independent numerical correlation controls (<1e-60); not a certificate")

if __name__ == "__main__":
    main()
