#!/usr/bin/env python3
"""M1-ND IMG1 species/lift cross-check.

Purpose
-------
Close the review question whether IMG1's free_sr/hub_sr/Nwrap/m machinery
introduces any species algebra beyond the already documented IMG0 extension
F_{g,k}=f_k o rho_g.

This script re-derives the source species, M1 shift j, integer L-wrap m and
input-lift formula directly from the physical affine source equation. It then
compares that derivation against:
  * the canonical M1-FULL free_sr/hub_sr tables, and
  * the independently committed IMG0 free_op_relation/hub_op_relation rules.

No IMG1 helper is imported or used.

Scope: finite/algebraic species and lift bookkeeping only. No injectivity.
"""

from fractions import Fraction as F

import certify_sw1_a10_c2_m1_full_b96 as m1
import certify_sw1_m1_nd_image_space as img0

print("SW1 M1-ND IMG1 SPECIES/LIFT CROSS-CHECK")

G = [
    ("P0", +1, 0, 0),
    ("P1", +1, 1, 0),
    ("Q0", -1, 0, 4),
    ("Q1", -1, 1, 4),
]
GDICT = {g[0]: g for g in G}

assert G == m1.G
assert G == img0.GDATA


def derive_source(s, lam_src, k_src, gout):
    """Solve source affine coordinates from
         t = s*x + lam_src*L + k_src*Delta
       with x represented by output species gout.

    Returns (gin_name, j, m), where
      phi_gin(theta+j Delta)
        = s*phi_gout(theta) + lam_src L + k_src Delta + m L.
    The sign convention for m matches M1-FULL:
      m = eta_in/2 - (s*eta_out/2 + lam_src).
    """
    _, so, etao, kapo = gout
    si = s * so

    cL = s * F(etao, 2) + lam_src
    twice_cL = 2 * cL
    assert twice_cL.denominator == 1
    etai = int(twice_cL) % 2

    gin = next(g for g in G if g[1] == si and g[2] == etai)
    _, _, _, kapi = gin

    cD = s * kapo + k_src
    j = F(cD - kapi, si)
    assert j.denominator == 1
    j = int(j)

    m = F(etai, 2) - cL
    assert m.denominator == 1
    m = int(m)

    # Exact coefficient identities behind the species/shift relation.
    assert si * j + kapi == cD
    assert F(etai, 2) - cL == m
    return gin[0], j, m


def affine_phi_coeffs(g, j=0):
    """Formal coefficients of phi_g(theta + j*Delta)
       in the basis (theta, L, Delta).
    """
    _, sg, eta, kappa = g
    return (F(sg), F(eta, 2), F(sg * j + kappa))


def add_coeffs(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale_coeffs(q, a):
    return tuple(F(q) * x for x in a)


def check_lift_identity_formal(s, lam_src, k_src, gout, gin_name, j, m, lout, Nout, Nin):
    """Non-tautological formal coefficient check.

    Build the physical source and the reconstructed species/lift coordinate
    by two different algebraic routes in the formal basis (theta, L, Delta).

    physical:
      x_out = rho_gout(theta) + lout*L
      t     = s*x_out + lam_src*L + k_src*Delta

    reconstructed:
      rho_gin(theta+j*Delta) + lin*L

    The check first derives lin from the independently built L-coefficients,
    then compares it with the IMG1 formula.
    """
    gout_phi = affine_phi_coeffs(gout, 0)
    gout_rho = add_coeffs(gout_phi, (F(0), -F(Nout), F(0)))
    xout = add_coeffs(gout_rho, (F(0), F(lout), F(0)))

    physical = add_coeffs(
        scale_coeffs(s, xout),
        (F(0), F(lam_src), F(k_src)),
    )

    gin = GDICT[gin_name]
    gin_phi = affine_phi_coeffs(gin, j)
    gin_rho = add_coeffs(gin_phi, (F(0), -F(Nin), F(0)))

    # Derive the required lift from the independently constructed formal
    # source coefficients, rather than defining both sides by the same formula.
    assert physical[0] == gin_rho[0]
    assert physical[2] == gin_rho[2]
    lin_from_physical = physical[1] - gin_rho[1]
    assert lin_from_physical.denominator == 1
    lin_from_physical = int(lin_from_physical)

    lin_formula = s * (lout - Nout) + Nin - m
    assert lin_formula == lin_from_physical

    reconstructed = add_coeffs(gin_rho, (F(0), F(lin_formula), F(0)))
    assert reconstructed == physical
    return lin_formula


def phi_direct(gname, theta):
    _, sg, eta, kappa = GDICT[gname]
    return sg * theta + F(eta, 2) * m1.L + kappa * m1.D


def rho_direct(gname, theta):
    z = phi_direct(gname, theta)
    return z - (z // m1.L) * m1.L


THETA_SAMPLES = tuple(
    sorted({
        F(0),
        m1.L * F(1, 19),
        m1.L * F(2, 17),
        m1.L * F(3, 13),
        m1.L * F(5, 11),
        m1.L * F(7, 16),
        m1.L * F(9, 17),
        m1.L * F(11, 19),
        m1.L * F(13, 17),
        m1.L * F(15, 16),
        m1.L * F(18, 19),
    })
)


def check_lift_identity_theta(s, lam_src, k_src, gout, gin_name, j, m, lout, theta):
    """Exact coordinate check at a rational theta.

    This does not use m1.Nwrap. Nout/Nin are computed independently from the
    direct affine representatives, and the physical source coordinate is
    compared against rho_gin(theta+j*Delta)+lin*L.
    """
    gout_name = gout[0]
    phi_out = phi_direct(gout_name, theta)
    Nout = phi_out // m1.L
    xout = rho_direct(gout_name, theta) + lout * m1.L

    physical = s * xout + lam_src * m1.L + k_src * m1.D

    shifted = theta + j * m1.D
    phi_in = phi_direct(gin_name, shifted)
    Nin = phi_in // m1.L
    rho_in = rho_direct(gin_name, shifted)

    lin_formula = s * (lout - Nout) + Nin - m

    q = (physical - rho_in) / m1.L
    assert q.denominator == 1
    lin_from_coordinate = int(q)

    assert lin_formula == lin_from_coordinate
    assert physical == rho_in + lin_formula * m1.L
    return lin_formula


# FREE: x_src = s*x_out + lam*L + k*Delta.
free_checked = 0
for br in m1.FREE:
    name, s, lam, k = br
    img0_br = next(x for x in img0.FREE if x[0] == name)
    assert img0_br == br

    for gout in G:
        gin, j, m = derive_source(s, lam, k, gout)
        assert m1.free_sr[(name, gout[0])] == (gin, j, m, s)

        img0_gin, img0_j = img0.free_op_relation(img0_br, gout)
        assert img0_gin[0] == gin
        assert img0_j == j

        # Universal formal coefficient check over a deliberately larger wrap
        # range, plus exact rational-theta coordinate checks.
        for lout in range(3):
            for Nout in range(-3, 4):
                for Nin in range(-3, 4):
                    check_lift_identity_formal(
                        s, lam, k, gout, gin, j, m, lout, Nout, Nin
                    )
            for theta in THETA_SAMPLES:
                check_lift_identity_theta(
                    s, lam, k, gout, gin, j, m, lout, theta
                )

        free_checked += 1

# HUB physical branch x = s*t + lam*L + k*Delta is solved as
# t = s*x - s*lam*L - s*k*Delta.
hub_checked = 0
for ch in m1.HUB:
    name, s, lam, k, coeff = ch
    img0_ch = next(x for x in img0.HUB if x[0] == name)
    assert img0_ch == ch

    lam_src = -s * lam
    k_src = -s * k

    for gout in G:
        gin, j, m = derive_source(s, lam_src, k_src, gout)
        assert m1.hub_sr[(name, gout[0])] == (gin, j, m, s)

        img0_gin, img0_j = img0.hub_op_relation(img0_ch, gout)
        assert img0_gin[0] == gin
        assert img0_j == j

        for lout in range(3):
            for Nout in range(-3, 4):
                for Nin in range(-3, 4):
                    check_lift_identity_formal(
                        s, lam_src, k_src, gout, gin, j, m, lout, Nout, Nin
                    )
            for theta in THETA_SAMPLES:
                check_lift_identity_theta(
                    s, lam_src, k_src, gout, gin, j, m, lout, theta
                )

        hub_checked += 1

assert free_checked == 10 * 4 == 40
assert hub_checked == 9 * 4 == 36

# P0 effective map is exactly IMG0's rho_g(theta+j Delta) label.
effective_types = set()
for br in m1.FREE:
    gin, j, _, _ = m1.free_sr[(br[0], "P0")]
    g = GDICT[gin]
    own = (g[1], F(g[2], 2), g[1] * j + g[3])
    img0_g, img0_j = img0.free_op_relation(br, GDICT["P0"])
    assert own == img0.effective_base_map(img0_g, img0_j)
    effective_types.add(own)

for ch in m1.HUB:
    gin, j, _, _ = m1.hub_sr[(ch[0], "P0")]
    g = GDICT[gin]
    own = (g[1], F(g[2], 2), g[1] * j + g[3])
    img0_g, img0_j = img0.hub_op_relation(ch, GDICT["P0"])
    assert own == img0.effective_base_map(img0_g, img0_j)
    effective_types.add(own)

assert len(effective_types) == 12

print("FREE source relations checked:", free_checked)
print("HUB source relations checked:", hub_checked)
print("M1 gin/j tables == direct physical derivation == IMG0 gin/j: PASS")
print("M1 m is exactly the integer L-wrap from the same affine relation: PASS")
print("lin formula == lift derived from independent formal source coefficients: PASS")
print("physical source == rho_gin(theta+j Delta)+lin*L on exact theta samples: PASS")
print("exact theta-coordinate lift checks:", (free_checked + hub_checked) * 3 * len(THETA_SAMPLES))
print("P0 effective maps == IMG0 rho_g(theta+j Delta) labels: PASS")
print("effective affine types:", len(effective_types))
print("FIREWALL: species/lift bookkeeping only; no injectivity claim")
print("SW1 M1-ND IMG1 SPECIES/LIFT CROSS-CHECK: PASS")
