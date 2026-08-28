#!/usr/bin/env python3
"""
Exact algebraic certificate for Objekt-X SW1-AWI.

Scope:
- fixed identities 2d=a+Delta and the A-wall reflection law;
- exact A-wall coefficient signs;
- 2x2 reflection-block diagonalization and invertibility.

Requires: sympy
"""
import sympy as sp

a = sp.log(2) / 2
b = sp.log(3) / 2
T = 2 * a
d = b - a
e = T - b
Delta = d - e

assert sp.simplify(2*d - a - Delta) == 0

s = sp.symbols("s", real=True)
j = sp.simplify(Delta - s)

# Physical collision identity:
assert sp.simplify((a+s) - (2*d-j)) == 0
assert sp.simplify(Delta-j-s) == 0  # J_Delta^2(s)=s

beta_plus = sp.log(2) * (
    2**sp.Rational(-9,4) + 2**sp.Rational(-15,4)
)
c11 = 2*sp.log(3) / (3*sp.sqrt(3))
beta_b = -c11

assert beta_plus.is_positive is True
assert beta_b.is_negative is True
assert sp.simplify(sp.Rational(3,8)-beta_plus).is_positive is True
assert sp.simplify(c11-sp.Rational(3,8)).is_positive is True
assert sp.simplify(c11-beta_plus).is_positive is True

mu_sym = sp.simplify(beta_plus + beta_b)
mu_asym = sp.simplify(beta_plus - beta_b)

assert mu_sym.is_negative is True
assert mu_asym.is_positive is True

Rmat = sp.Matrix([[0,1],[1,0]])
I2 = sp.eye(2)
C = sp.simplify(beta_plus*I2 + beta_b*Rmat)

vs = sp.Matrix([1,1])
va = sp.Matrix([1,-1])

assert sp.simplify(C*vs - mu_sym*vs) == sp.zeros(2,1)
assert sp.simplify(C*va - mu_asym*va) == sp.zeros(2,1)
assert sp.simplify(C.det() - (beta_plus**2-beta_b**2)) == 0
assert C.det().is_nonzero is True

Cinv = sp.simplify((beta_plus*I2-beta_b*Rmat)/(beta_plus**2-beta_b**2))
assert sp.simplify(C*Cinv-I2) == sp.zeros(2)

# ---- Exact chamber geometry certificate via positive slack parametrizations ----

r0, u0, g0, h0, theta = sp.symbols("r0 u0 g0 h0 theta", positive=True)

# Upper chamber: eps > Delta/2.
# Parametrization:
#   R=r0,
#   eps=r0+g0+h0,
#   Delta=2*r0+2*g0+h0.
# Then Delta-(R+eps)=g0>0 and 2*eps-Delta=h0>0.
R_u = r0
eps_u = r0 + g0 + h0
Delta_u = 2*r0 + 2*g0 + h0
assert sp.simplify(Delta_u - (R_u + eps_u) - g0) == 0
assert sp.simplify(2*eps_u - Delta_u - h0) == 0

# In s-coordinates the overlap is J=(Delta-eps, eps)
Jlo_u = sp.simplify(Delta_u - eps_u)
Jhi_u = sp.simplify(eps_u)
assert sp.simplify(Jlo_u - (r0+g0)) == 0
assert sp.simplify(Jhi_u - (r0+g0+h0)) == 0
assert sp.simplify(Jlo_u - R_u - g0) == 0
assert sp.simplify((Delta_u-R_u) - Jhi_u - g0) == 0
assert sp.simplify(Jhi_u - Jlo_u - h0) == 0

# Reflection invariance on the open interval:
# write s=Jlo+theta with 0<theta<h0 formally; then t=Delta-s=Jlo+(h0-theta).
s_u = sp.simplify(Jlo_u + theta)
t_u = sp.simplify(Delta_u - s_u)
assert sp.simplify(t_u - (Jlo_u + h0 - theta)) == 0
assert sp.simplify(Delta_u - t_u - s_u) == 0

# Unique fixed point is the midpoint and lies in upper-chamber J.
fix_u = sp.simplify(Delta_u/2)
assert sp.simplify(fix_u - (Jlo_u + h0/2)) == 0
assert sp.simplify((Jlo_u+Jhi_u)/2 - fix_u) == 0

# Lower chamber: eps < Delta/2.
# Parametrize R=r0, eps=r0+u0, Delta=2*r0+2*u0+h0.
# Then Delta-(R+eps)=u0+h0>0 and Delta-2eps=h0>0.
R_l = r0
eps_l = r0 + u0
Delta_l = 2*r0 + 2*u0 + h0
assert sp.simplify(Delta_l - (R_l+eps_l) - (u0+h0)) == 0
assert sp.simplify(Delta_l - 2*eps_l - h0) == 0
assert sp.simplify((Delta_l-eps_l) - eps_l - h0) == 0
# Hence left endpoint of I_b is strictly to the right of right endpoint of I_+.

# Degenerate chamber: eps = Delta/2.
R_e = r0
eps_e = r0 + u0
Delta_e = 2*r0 + 2*u0
assert sp.simplify(Delta_e - (R_e+eps_e) - u0) == 0
assert sp.simplify(Delta_e - 2*eps_e) == 0
assert sp.simplify((Delta_e-eps_e) - eps_e) == 0
# Thus open intervals have empty intersection and closures touch in exactly one endpoint.

print("SW1-AWI CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("geometry: lower/equal/upper chamber split certified exactly")
print("upper overlap J=(Delta-eps, eps): certified")
print("reflection invariance and unique midpoint fixed point: certified")
print("2d=a+Delta and collision law: certified")
print("beta_plus < 3/8 < c11=-beta_b: certified")
print("symmetric eigenvalue beta_plus+beta_b < 0")
print("antisymmetric eigenvalue beta_plus-beta_b > 0")
print("A-wall reflection block invertible")
