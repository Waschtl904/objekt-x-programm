# Reduced shell coordinate theorem

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Mathematical anchor: `6f24422ee8e074d387e9656e5307b607edb6c809`.
Publication parent: `309f7be2c4d3033ce15e49c497c3698879d61185`.
The concurrent quotient package is preserved; this supplement makes form-domain
surjectivity and the coupled H1 traces explicit. No new endpoint and no merge.

[PROOF.md](PROOF.md) isolates three exact statements:

1. A bounded bijection K_B^0 direct-sum X -> K_b, with zero kernel and
   squared norm factors 1/32 and 65. Orthogonality is PHYSICAL L2(dx).
2. A bijection of the closed form spaces F_B^0 direct-sum F_D -> F_b,
   including a proof of surjectivity and two-sided graph norm control.
3. The exact H1 source preimage is a coupled trace subspace:
   w(B)+t=s(B), s(b)=0. The reduced core w need not have zero endpoint trace.

This corrects the schematic H1_0-product formulation in the supplied review.
No physical source is removed and no third Mellin condition is imposed.
A_0 is a form compression; C_0 and its adjoint use the stated L2 products.
The reduced Schur estimate and odd continuation remain open.
See [STATUS_DE.md](STATUS_DE.md) for the German explanation.

From repository root, Python 3.10+, standard library only:

```text
python research/x-c1/reduced-shell-coordinate-theorem-2026-09-19/check_quotient.py --verify
```

Do not use Python -O. The checker verifies bound inputs, replays the inherited
pivot certificate, checks exact coefficient identities and norm factors,
compares saved output, and checks SHA256SUMS. Finite algebra does not replace
the analytic closure or surjectivity proofs. No quadrature or numerical
spectral approximation is used. Allow a few seconds on a typical machine.
