"""Directed rational interval operations; no binary floating point."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse, hashlib, json, sys

sys.set_int_max_str_digits(0)
DIGITS = 160
SCALE = 10 ** DIGITS

def point(x):
    x = F(x)
    return x, x

def interval(x):
    a, b = map(F, x)
    assert a <= b
    return a, b

def rounded(x):
    a, b = x[0] * SCALE, x[1] * SCALE
    return F(a.numerator // a.denominator, SCALE), F(-((-b.numerator) // b.denominator), SCALE)

def add(a, b): return rounded((a[0] + b[0], a[1] + b[1]))
def neg(a): return -a[1], -a[0]
def sub(a, b): return add(a, neg(b))
def mul(a, b):
    vals = [x*y for x in a for y in b]
    return rounded((min(vals), max(vals)))
def div(a, b):
    assert b[0] * b[1] > 0, 'zero-containing divisor'
    return mul(a, (1 / b[1], 1 / b[0]))
def absolute(a): return max(abs(a[0]), abs(a[1]))
def total(xs):
    out = point(0)
    for x in xs: out = add(out, x)
    return out
def sqrt_upper(x):
    assert x >= 0, 'negative square-root bound'
    k = isqrt(x.numerator * SCALE*SCALE // x.denominator)
    if F(k*k, SCALE*SCALE) < x: k += 1
    out = F(k, SCALE)
    assert out*out >= x
    return out
def tr(a): return list(map(list, zip(*a)))
def matrix(a): return [[interval(x) for x in row] for row in a]
def mm(a, b):
    assert len(a[0]) == len(b)
    return [[total(mul(x,y) for x,y in zip(row,col)) for col in tr(b)] for row in a]
def inverse(a, positive_pivots=False):
    n = len(a)
    m = [row[:] + [point(i == j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot = m[j][j]
        if positive_pivots: assert pivot[0] > 0, ('unproved positive pivot', j)
        m[j] = [div(x, pivot) for x in m[j]]
        m[j][j] = point(1)
        for i in range(n):
            if i == j: continue
            c = m[i][j]
            m[i] = [sub(x, mul(c,y)) for x,y in zip(m[i],m[j])]
            m[i][j] = point(0)
    return [row[n:] for row in m]
def symmetric(a):
    n = len(a)
    out = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            lo, hi = max(a[i][j][0],a[j][i][0]), min(a[i][j][1],a[j][i][1])
            assert lo <= hi
            out[i][j] = lo,hi
    return out
def norm_upper(a):
    return max(sum(absolute(x) for x in row) for row in a)
def rational(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,(tuple,list)): return [rational(z) for z in x]
    if isinstance(x,dict): return {k:rational(v) for k,v in x.items()}
    return x
def sci(x, upper=False, digits=8):
    if not x: return '0'
    if x < 0: return '-' + sci(-x,not upper,digits)
    e = 0
    while x < 1: x *= 10; e -= 1
    while x >= 10: x /= 10; e += 1
    scale = 10**(digits-1); z = x*scale; k = z.numerator//z.denominator
    if upper and F(k) < z: k += 1
    return f'{k//scale}.{k%scale:0{digits-1}d}e{e:+d}'
def display(a): return [sci(a[0]),sci(a[1],True)]

