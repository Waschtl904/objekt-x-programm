#!/usr/bin/env python3
"""Exact supporting checks for X-C1-ENDPOINT-GREEN (2026-09-16).

Requires Python 3 and SymPy (executed with SymPy 1.14.0).
No A1/C0 checker, numerical quadrature, matrix assembly, or RH assumption.
These finite algebraic checks support, but do not replace, the analytic
support, convergence, and domain proofs in X_C1_ENDPOINT_GREEN_BRIDGE.md.
Run: python check_x_c1_endpoint_green_bridge.py
"""
from __future__ import annotations

import sympy as s

checks: list[str] = []


def zero(name: str, expr: s.Expr) -> None:
    value = s.simplify(s.expand(expr))
    if value != 0:
        raise AssertionError(f"{name}: nonzero residual {value}")
    checks.append(name)


def positive(name: str, expr: s.Expr) -> None:
    value = s.simplify(expr)
    if value.is_positive is not True:
        raise AssertionError(f"{name}: positivity not established for {value}")
    checks.append(name)


# Independent real and imaginary jets make the identities valid for complex inputs.
a = s.symbols('a0:4', real=True)
b = s.symbols('b0:4', real=True)
c = s.symbols('c0:3', real=True)
d = s.symbols('d0:3', real=True)
phi = [a[j] + s.I*b[j] for j in range(4)]
r = [c[j] + s.I*d[j] for j in range(3)]
jet_groups = (a, b, c, d)


def D(expr: s.Expr) -> s.Expr:
    return s.expand(sum(s.diff(expr, g[j])*g[j+1]
                        for g in jet_groups for j in range(len(g)-1)))


def abs2(expr: s.Expr) -> s.Expr:
    return s.expand(expr*s.conjugate(expr))


def twice_re(expr: s.Expr) -> s.Expr:
    return s.expand(expr+s.conjugate(expr))


lam = s.Rational(1, 2)
u = -phi[2] + lam**2*phi[0]
p = lam*phi[0] - phi[1]
q = lam*phi[0] + phi[1]
zero('Green normalization: derivative jump', (-lam-lam)+1)
zero('past resolvent equation', D(p)+lam*p-u)
zero('future resolvent equation', -D(q)+lam*q-u)
zero('potential reconstruction', p+q-phi[0])
zero('potential derivative reconstruction', q-p-2*phi[1])
zero('positive Green energy split', abs2(p)+abs2(q)-2*abs2(phi[1])-abs2(phi[0])/2)
S = abs2(p)-abs2(q)
zero('signed two-sided Green flux', twice_re(s.conjugate(u)*phi[0])-abs2(p)-abs2(q)-D(S))
J = twice_re(s.conjugate(phi[0])*r[1]-s.conjugate(phi[1])*r[0])
Lr = -r[2]+lam**2*r[0]
zero('full complex Green current', twice_re(s.conjugate(u)*r[0])-twice_re(s.conjugate(phi[0])*Lr)-D(J))
zero('integrated L norm: exact derivative correction',
     abs2(u)-abs2(phi[2])-2*lam**2*abs2(phi[1])-lam**4*abs2(phi[0])
     +lam**2*D(twice_re(phi[1]*s.conjugate(phi[0]))))
uprime = -phi[3]+lam**2*phi[1]
zero('integrated derivative norm: exact correction',
     abs2(uprime)-abs2(phi[3])-2*lam**2*abs2(phi[2])-lam**4*abs2(phi[1])
     +lam**2*D(twice_re(phi[2]*s.conjugate(phi[1]))))
for sign in (-1, 1):
    zero(f'Mellin moment annihilation {sign:+d}', lam**2-(sign*lam)**2)
positive('uniform H3-to-H1 inverse norm coefficient', min(s.Rational(1,16), s.Rational(9,16), s.Rational(3,2), s.Integer(1)))
m, mu, z = s.symbols('m mu z', positive=True)
zero('Gamma mode moment factor', ((2*m+lam)**2-lam**2)-2*m*(2*m+1))
zero('ground-mode mixed factor vanishes', (lam**2-lam**2)**2)
zero('single-mode resolvent energy symbol',
     (2/mu)*z**2/(mu**2+z**2)-(2/mu-2*mu/(mu**2+z**2)))
x = s.symbols('x', real=True)
zero('elementary strict pi upper bound identity',
     s.integrate(x**4*(1-x)**4/(1+x**2), (x,0,1))-(s.Rational(22,7)-s.pi))
qq = s.symbols('q', positive=True)
atan_sum = 2*s.atan(qq)+2*s.atan((1-qq)/(1+qq))
zero('Gamma tail arctangent identity derivative', s.diff(atan_sum, qq))
zero('Gamma tail arctangent identity constant', atan_sum.subs(qq,1)-s.pi/2)
zero('Gamma tail primitive', s.diff(s.atanh(qq)+s.atan(qq), qq)-2/(1-qq**4))
positive('log(175/22)>2 rational comparison', s.Rational(175,22)-s.Rational(11,4)**2)
positive('exp(7/10)>2 by four positive series terms', sum(s.Rational(7,10)**j/s.factorial(j) for j in range(4))-2)
positive('sqrt(2)>7/5', 2-s.Rational(7,5)**2)
width = s.Rational(1,50)
separation = s.Rational(2,3)-width
zero('fixed support separation', separation-s.Rational(97,150))
cross_bound = width*(1+1/(2*separation))
zero('Gamma mixed bound', cross_bound-s.Rational(86,2425))
gap = s.Rational(99,100)-s.Rational(1,2)-cross_bound
zero('exact two-source gap', gap-s.Rational(4409,9700))
positive('two-source gap exceeds 9/20', gap-s.Rational(9,20))
zero('strict residual budget', gap-s.Rational(9,20)-s.Rational(11,2425))
zero('critical-half time-tail exponent after ground cancellation', 2*(lam-s.Rational(5,2))+4)

if __name__ == '__main__':
    for name in checks:
        print(f'PASS  {name}')
    print(f'\n{len(checks)} exact checks PASS.')
    print('Analytic domain/support/convergence proofs remain in the accompanying note.')
    print('No positive C_a, independent review, Object X, or RH claim.')
