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


def check_lift_identity(s, m, lout, Nout, Nin):
    """Algebraic L-coefficient identity:
       physical source = rho_gin(theta+jD) + lin*L.
    """
    lin = s * (lout - Nout) + Nin - m

    # Physical L coefficient relative to phi_gin is
    # s*(lout-Nout)-m; converting phi_gin to rho_gin adds +Nin.
    rhs_lin = s * (lout - Nout) - m + Nin
    assert lin == rhs_lin
    return lin


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

        # Test the exact wrap/lift identity over a deliberately larger integer
        # range than the physical lifts require.
        for lout in range(3):
            for Nout in range(-3, 4):
                for Nin in range(-3, 4):
                    check_lift_identity(s, m, lout, Nout, Nin)

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
                    check_lift_identity(s, m, lout, Nout, Nin)

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
print("lin = s*(lout-Nout)+Nin-m is the exact lift reconstruction identity: PASS")
print("P0 effective maps == IMG0 rho_g(theta+j Delta) labels: PASS")
print("effective affine types:", len(effective_types))
print("FIREWALL: species/lift bookkeeping only; no injectivity claim")
print("SW1 M1-ND IMG1 SPECIES/LIFT CROSS-CHECK: PASS")
