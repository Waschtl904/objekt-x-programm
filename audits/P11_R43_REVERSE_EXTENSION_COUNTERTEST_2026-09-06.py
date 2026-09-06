#!/usr/bin/env python3
"""
P11 / R43 — adversarial countertest for the naive bulk/collar extension idea.

Scope:
- no theorem proof;
- no reverse-normal decay claim;
- no statement about Strong Terminal / C6 / Object X / RH.

The script checks two local facts used in the destructive review of the
reverse-normal extension route stacked on PR #68.

(1) A point may lie outside the r=8 log U terminal collar and still acquire
    a newly resolved martingale level when U is replaced by V, because a
    large prime half-shift can satisfy

        J_{p,U}(u)=0 < J_{p,V}(u).

    At the same time the centered k=1 half-shift can connect one old-source
    point to one point in the new spatial strip.  Hence "bulk => old/new
    residual metrics coincide" is false in general.

(2) In the PR-#68 least-squares formula the correction variable y belongs to
    the new strip N.  Therefore the formal choice y=iota*x_bulk is type-invalid:
    iota*x_bulk lives in the embedded old source summand, not in N.

The numerical witness uses the known Mersenne prime p=2^127-1.
"""

from math import floor, log


def J(p: int, T: float, u: float) -> int:
    """Frozen P11 martingale depth J_{p,T}(u)."""
    return max(0, floor(2.0 * max(T - abs(u), 0.0) / log(p)))


def in_old(U: float, z: float) -> bool:
    return abs(z) < U


def in_new_strip(U: float, V: float, z: float) -> bool:
    return U < abs(z) < V


def main() -> None:
    # Known Mersenne prime.
    p = (1 << 127) - 1

    U = 80.0
    V = 100.0
    u = 40.0
    r = 8.0 * log(U)
    a_p = 0.5 * log(p)

    jU = J(p, U, u)
    jV = J(p, V, u)

    z_minus = u - a_p
    z_plus = u + a_p

    # The point u is genuinely outside the PR-#64 collar.
    assert U - abs(u) > r

    # Nevertheless the new horizon resolves one additional level there.
    assert jU == 0
    assert jV == 1

    # One centered half-shift endpoint is old-supported and the other lies
    # in the new spatial strip.
    assert in_old(U, z_minus)
    assert in_new_strip(U, V, z_plus)

    # Type firewall for the variational correction:
    # u is an old-source point, therefore an embedded bulk value cannot
    # itself be an admissible y in N.
    assert in_old(U, u)
    assert not in_new_strip(U, V, u)

    # The correct geometry is strip-valued and prime-shifted:
    # z_plus - z_minus = log p.
    assert abs((z_plus - z_minus) - log(p)) < 1e-12

    print("R43 reverse-extension countertest: PASS")
    print(f"U={U}, V={V}, r=8logU={r:.12f}")
    print(f"p=2^127-1={p}")
    print(f"a_p=0.5 log p={a_p:.12f}")
    print(f"u={u}, distance to old boundary={U-abs(u):.12f}")
    print(f"J_p,U(u)={jU}, J_p,V(u)={jV}")
    print(f"half-shift endpoints: {z_minus:.12f}, {z_plus:.12f}")
    print("Conclusion: bulk collar escape alone does not imply C_fine vanishes.")
    print("Any cheap extension must be N-valued and prime-shift aware.")


if __name__ == "__main__":
    main()
