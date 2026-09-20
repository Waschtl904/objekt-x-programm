# Full-shell directional Schur certificate

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.

At B=log(5)/2, test the pinned physical near-null source after its exact
L2 projection off the trace corrector psi. For every 0<b-B<=10^-20:

- the scalar trace diagnostic is enclosed separately and c_v>0 is certified;
- an exact trace Riesz approximant leaves a residual bounded on the ENTIRE
  trace-plus-L2 shell, using its anisotropic positive pivot;
- eta_v<1-4*10^-11 and r_v>5449/10^16=5.449e-13;
- the whole reduced-core Schur estimate and odd continuation remain open.

The source has physical norm squared about 0.16543536. The last bound is
an energy remainder for that fixed source, not its Rayleigh quotient.
No finite shell matrix, quadrature proof, third Mellin condition, or A1.

`PROOF.md` supplies the full analytic argument. `STATUS_DE.md` is the
German result summary. `input_bindings.json` freezes 41 repository inputs
at anchor `1f7628b20e4bd7b3588ae36cfdf66c3f1656d1ca`.

From the repository root, using Python 3 and only its standard library:

```text
python research/x-c1/near-null-reduced-schur-direction-2026-09-19/check_direction.py --verify
```

There are 31 new checks, plus replay of 28 coordinate checks and 43 full
shell pivot checks. The command checks input SHA-256/Git blob bindings,
reproduces JSON and log, and verifies the seven SHA-256 payload entries.
The hash manifest excludes itself. `--write` regenerates the saved
results and manifest and is intended for author-side package maintenance.

The checker imports the pinned near-null arithmetic implementation, then
evaluates the source and cusp-corrector pairings by reflected-half exact
integration. Its reuse of interval primitives is explicit. The finite
checks do not replace the analytic domain and complete-tail proofs.

The package also corrects an audit statement: for fixed b, absolute
coercivity and Theta_0<1 are equivalent here because the Schur subtraction
is a bounded positive operator. A uniform equivalence requires uniform
constants. Neither entire-core gate is proved by the directional result.

Append-only research. No change to main, no reopening of merged PR #137,
and no new PR or merge.
