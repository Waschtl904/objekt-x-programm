# All-parity shrinking-step iteration lemma

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.

Starting from the local all-parity theorem in `a659047`, this package proves
that the shell transport can be restarted from a newly positive endpoint.
On the fixed local band

`log(5)/2 <= a <= log(5)/2 + 10^-2`

the even and odd profile correctors, active prime-power set, disjoint
core-input geometry, complete core/profile coupling and profile floor admit
endpoint-uniform constants.

If the complete two-Mellin form at `a` has gap `epsilon>0`, then for every
`0<gamma<epsilon` an explicit sufficiently small right width `h>0` preserves
gap at least `gamma` at `a+h`.

Applied to the all-parity gap `3e-15` at `B+1e-20`, the package constructs
an explicit infinite strictly increasing sequence

`b_(n+1)=b_n+2^(-4*10^16*2^n)`

with certified gaps

`epsilon_n = 1e-15*(1+2^(1-n)) > 1e-15`.

Thus local transport is genuinely restartable and infinitely iterable with
a positive gap floor. The step widths shrink extremely rapidly. No uniform
positive step size, macroscopic Window Amplification, crossing of `log(7)/2`,
Connected Unit-Window Coercivity, Strong Terminal, Object X or RH is claimed.
