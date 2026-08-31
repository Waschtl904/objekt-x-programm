#!/usr/bin/env python3
"""SW1 A2-A10 reconciliation: kernel-bijection hardening certificate.

Finite algebraic/mechanical scope only.

Checks:
- J/Psi are two-sided inverses in a nontrivial exact model;
- Theta = J direct-sum I has explicit two-sided inverse;
- the C0 coordinate change preserves a nontrivial kernel in both directions;
- tall isometric C1C1 embeddings are bijections onto their image spaces;
- W^{-1}W = I and WW^{-1} = I on Ran(W);
- WW^{-1} is NOT the identity on the larger ambient slot space;
- the transported operator has exactly W(ker C) as its kernel on Ran(W);
- an explicit ambient-only artificial kernel vector exists, demonstrating why
  M1-ND must be restricted to the true C1C1 image/consistency space.

This does not certify the infinite-dimensional closed-image/isometry theorem;
that remains the separate Hilbert-space argument/review.
"""
import sympy as sp

print("SW1 A2-A10 KERNEL BIJECTION CERTIFICATE")

# ---------------------------------------------------------------------------
# 1. C0: exact KNF coordinate isomorphism J = Psi^{-1}.
# ---------------------------------------------------------------------------
Psi = sp.Matrix([[2, 1], [1, 1]])
J = Psi.inv()
I2 = sp.eye(2)

assert J * Psi == I2
assert Psi * J == I2

# Theta = J direct-sum I_W, with dim(W)=1 in the exact model.
Theta = sp.diag(1, 1, 1)
Theta[:2, :2] = J
Theta_inv = sp.diag(1, 1, 1)
Theta_inv[:2, :2] = Psi
I3 = sp.eye(3)

assert Theta_inv * Theta == I3
assert Theta * Theta_inv == I3

# ---------------------------------------------------------------------------
# 2. C0 kernel transport: C = [T J | Z], Kfirst = [T | Z].
#    This model deliberately has a nontrivial one-dimensional kernel.
# ---------------------------------------------------------------------------
T = sp.Matrix([[3, 1], [1, 2]])
Z = sp.Matrix([[1], [2]])

Kfirst = T.row_join(Z)
C = (T * J).row_join(Z)

assert Kfirst * Theta == C
assert C.rank() == 2
assert Kfirst.rank() == 2

ker_C = C.nullspace()
ker_K = Kfirst.nullspace()
assert len(ker_C) == 1
assert len(ker_K) == 1

v = ker_C[0]
y = Theta * v
assert C * v == sp.zeros(2, 1)
assert Kfirst * y == sp.zeros(2, 1)
assert Theta_inv * y == v

u = ker_K[0]
x = Theta_inv * u
assert Kfirst * u == sp.zeros(2, 1)
assert C * x == sp.zeros(2, 1)
assert Theta * x == u

# Projection to the W-coordinate is injective on ker(C):
# w=0 would force (T J) xi=0, hence xi=0.
TJ = T * J
assert TJ.det() != 0
assert v[2] != 0

# Explicit inverse kernel parametrization by the W-coordinate in this model.
w = sp.symbols("w")
xi_of_w = -(TJ.inv() * Z) * w
candidate = xi_of_w.col_join(sp.Matrix([w]))
assert sp.simplify(C * candidate) == sp.zeros(2, 1)

# ---------------------------------------------------------------------------
# 3. C1C1: exact tall isometries onto proper image subspaces.
# ---------------------------------------------------------------------------
UH = sp.Matrix([
    [sp.Rational(3,5), 0],
    [sp.Rational(4,5), 0],
    [0, sp.Rational(5,13)],
    [0, sp.Rational(12,13)],
])
UW = sp.Matrix([
    [sp.Rational(8,17)],
    [sp.Rational(15,17)],
])

assert UH.T * UH == sp.eye(2)
assert UW.T * UW == sp.eye(1)

# W = UH|_K direct-sum UW : K plus W -> R_K plus R_W.
W = sp.zeros(6, 3)
W[:4, :2] = UH
W[4:, 2:] = UW
W_inv_on_image = W.T

assert W_inv_on_image * W == I3

P_image = W * W_inv_on_image
assert P_image * W == W
assert P_image != sp.eye(6)

# Every actual image vector is recovered exactly.
a, b, c = sp.symbols("a b c")
x_generic = sp.Matrix([a, b, c])
F_generic = W * x_generic
assert P_image * F_generic == F_generic
assert W_inv_on_image * F_generic == x_generic

# ---------------------------------------------------------------------------
# 4. Transported operator and exact kernel on the true image space.
# ---------------------------------------------------------------------------
Chat = UH * C * W_inv_on_image

# Forward direction: each original kernel vector maps to a transported kernel.
Fv = W * v
assert Chat * Fv == sp.zeros(4, 1)
assert W_inv_on_image * Fv == v

# Reverse direction on Ran(W):
# Chat(W x) = UH C x, and UH is injective because UH^T UH = I.
assert Chat * W == UH * C
assert UH.T * (Chat * W) == C

# Hence x is in ker(C) iff W x is in ker(Chat) intersect Ran(W).
# Check this with the exact nontrivial kernel basis.
assert len(C.nullspace()) == 1
assert C * v == sp.zeros(2, 1)
assert Chat * (W * v) == sp.zeros(4, 1)

# ---------------------------------------------------------------------------
# 5. Ambient firewall: artificial kernel vectors exist outside Ran(W).
# ---------------------------------------------------------------------------
# z is orthogonal to the first UH column, hence orthogonal to all of Ran(W).
z_ambient = sp.Matrix([
    sp.Rational(-4,5),
    sp.Rational(3,5),
    0,
    0,
    0,
    0,
])
assert W_inv_on_image * z_ambient == sp.zeros(3, 1)
assert P_image * z_ambient == sp.zeros(6, 1)
assert z_ambient != sp.zeros(6, 1)
assert Chat * z_ambient == sp.zeros(4, 1)

# Therefore the ambient kernel is strictly larger than the valid-image kernel.
assert not (P_image * z_ambient == z_ambient)

print("J/Psi two-sided inverse: PASS")
print("Theta two-sided inverse and C0 kernel transport: PASS")
print("C0 nontrivial kernel reverse parametrization: PASS")
print("C1C1 W^{-1}W = I: PASS")
print("C1C1 WW^{-1} = I on Ran(W): PASS")
print("ambient WW^{-1} != I firewall: PASS")
print("transported-kernel equality on true image space: PASS")
print("explicit artificial ambient-only kernel vector: PASS")
print(f"sympy={sp.__version__}")
print("SW1 A2-A10 KERNEL BIJECTION CERTIFICATE: PASS")
