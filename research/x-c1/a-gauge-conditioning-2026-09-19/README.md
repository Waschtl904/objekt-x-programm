# A-gauge conditioning package

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.

This package replaces the reduced physical-L2 gauge by the core-energy-orthogonal gauge at `B=log(5)/2`, for `0<b-B<=10^-20`.

It proves:

- the fixed functional `w -> q_B(w,psi)` extends boundedly to the physical core `L2`, with the conservative explicit bound `|q_B(w,psi)| < 272 ||w||_2`;
- the already certified `q_B[psi] > 0.14` gives `|ell_A(w)| < 1943 ||w||_2`;
- `Phi_A : K_{B,A}^0 direct-sum (C direct-sum L2(B,b)) -> K_b` is a bounded bijection;
- uniform physical conditioning
  `N_A^2/140000000 <= ||Phi_A||_2^2 <= 65 N_A^2`;
- the form-domain and actual-H1 source statements remain exact, with the same gluing condition `w(B)+t=s(B)`;
- the pure trace cross channel vanishes identically: `c_A(w,e)=0`.

The full reduced-core Schur bound remains open. In particular, the package does not assert all-source positivity for any new endpoint and does not close the odd sector.

`check_a_gauge.py --verify` replays the parent near-null certificate, verifies the pinned input hashes and the finite rational arithmetic used in the displayed constants. The checker is not a replacement for the analytic L2-functional, form-domain, or H1-gluing arguments in `PROOF.md`.

Append-only research on `research/x-c1-inherited-resonance-shell-schur-2026-09-18`. No PR, no merge, no change to `main`.
