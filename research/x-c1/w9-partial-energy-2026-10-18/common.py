"""Bound, immutable inputs and directed arithmetic for the W9 partial energy."""
import gzip
import hashlib
import io
import json
from fractions import Fraction
from pathlib import Path
from types import MappingProxyType
import zipfile

from flint import arb, arb_poly, arb_mat, acb, acb_poly

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def q(x):
    if not isinstance(x, (str, int, Fraction)):
        x = str(x)
    x = Fraction(x)
    return arb(x.numerator) / x.denominator


def box(x):
    need(Fraction(x[0]) <= Fraction(x[1]), 'Reversed interval')
    return q(x[0]).union(q(x[1]))


def mat(x):
    return arb_mat([[box(v) for v in r] for r in x])


def ratmat(x):
    return arb_mat([[q(v) for v in r] for r in x])


def enc(x):
    need(x.is_finite(), 'Nonfinite output')
    # A fixed outward rational grid avoids archiving thousands of irrelevant
    # mantissa digits. This rounding is part of the enclosure, not a midpoint.
    scale = 10**80
    lo = Fraction(str(x.lower().fmpq())) * scale
    hi = Fraction(str(x.upper().fmpq())) * scale
    floor = lo.numerator // lo.denominator
    ceil = -((-hi.numerator) // hi.denominator)
    return [str(Fraction(floor, scale)), str(Fraction(ceil, scale))]


def encode(x):
    if isinstance(x, arb):
        return enc(x)
    if isinstance(x, arb_mat):
        return [[enc(x[i, j]) for j in range(x.ncols())] for i in range(x.nrows())]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def trace(x):
    need(x.nrows() == x.ncols(), 'Nonsquare trace')
    return sum((x[i, i] for i in range(x.nrows())), arb(0))


def norm(x):
    return sum((abs(x[i, j]).upper()**2 for i in range(x.nrows())
                for j in range(x.ncols())), arb(0)).sqrt()


def pad(x, error):
    need(error >= 0, 'Negative error')
    return x + arb(0, error.upper())


def legs(n):
    out = [arb_poly([1]), arb_poly([0, 1])]
    t = out[1]
    for k in range(1, n - 1):
        out.append(((2*k+1)*t*out[k] - k*out[k-1]) * (arb(1)/(k+1)))
    return out[:n]


def pint(f, lo=arb(0), hi=arb(1)):
    f = f.integral()
    return f(hi) - f(lo)


def columns(polys, rows=None):
    rows = rows if rows is not None else max(map(len, polys))
    return arb_mat([[p[i] for p in polys] for i in range(rows)])


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), arb(0))


class Poly:
    def __init__(self, p):
        self.p = arb_poly(p)
        self.c = acb_poly(list(self.p))

    def __call__(self, x):
        return self.c(x) if isinstance(x, acb) else self.p(x)


class Inputs:
    """Only checked byte snapshots are parsed, including nested archive members."""
    def __init__(self, binding_bytes=None):
        raw_spec = (HERE/'INPUT_BINDINGS.json').read_bytes() if binding_bytes is None else binding_bytes
        spec = json.loads(raw_spec)
        data = {}
        for alias, entry in spec['files'].items():
            path = (ROOT/entry['path']).resolve()
            need(path.is_relative_to(ROOT), 'Escaping input path')
            raw = path.read_bytes()
            need(hashlib.sha256(raw).hexdigest() == entry['sha256'], alias)
            data[alias] = raw
        for alias, entry in spec['members'].items():
            need(entry['archive'] in data, 'Archive dependency order')
            with zipfile.ZipFile(io.BytesIO(data[entry['archive']])) as archive:
                raw = archive.read(entry['member'])
            need(hashlib.sha256(raw).hexdigest() == entry['sha256'], alias)
            data[alias] = raw
        self.data = MappingProxyType(data)

    def json(self, alias):
        raw = self.data[alias]
        return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def mellin(n, a):
    z = a/2
    term = z**n * 2**n * arb.fac_ui(n) / arb.fac_ui(2*n+1)
    total = term
    for k in range(1, 256):
        term *= z*z/(2*k*(2*n+2*k+1))
        total += term
    ratio = z*z/(2*256*(2*n+513))
    return pad(total, abs(term).upper()*ratio/(1-ratio))
