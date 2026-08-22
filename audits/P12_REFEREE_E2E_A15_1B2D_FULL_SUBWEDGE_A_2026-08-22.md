# P12 End-to-End Referee — A15.1b2d full Sub-wedge A and b2c proof reconstruction

**Date:** 2026-08-22
**Repository:** `Waschtl904/objekt-x-programm`
**Papers head at start:** `2eff382`

## Purpose

Two items:

1. **b2c proof reconstruction.**  The prior b2c manuscript
   (commit `2eff382`) named the $13\times 13$ block only sketchily
   ("some values, ..., six further values") and gave the determinant
   $-2 p^{7} q r (p^{2} - q^{2})(2p^{2} - q^{2})$ without an
   elimination path.  Independent reconstruction confirms the
   determinant and further reduces the system by triangular
   elimination to the single scalar identity
   \[
   \frac{2 q r}{p^{3}}\,(2p^{2} - q^{2})\, h(x) = 0.
   \]
   This is stronger than the determinant version and is now the
   published proof.
2. **New theorem b2d: full Sub-wedge A injectivity for $e/2 \le R < d/2$.**
   Closes the previously open slice `open:p12-subwedgeA-fulltail`
   (Sub-wedge A full tail).  Together with b2c this closes the entire
   mixed strip $e/2 \le R < T$.

## 1. b2c: triangular elimination

Take $x \in (R, \sigma)$ visibility-stable (Case (ii) of b2c).  The
E-defect equation reduces immediately to
$p h(x) - q h(a - x) - p H(x) = 0$ (the $r h(d-x)$ term vanishes since
$d - x < R$).

Twelve further source relations at typed locations
$u \in \{a + x, T + x, a - x, a + (a - x), T + (a - x), T - x, b + x,
b - x, 3a - x, a + b - x, b + (a - x), 2b - x\}$
give a $13\times 13$ homogeneous system on the visibility set
$V$ of $13$ interior values.

Symbolic triangular reduction (starting from $u = T + x$ which
eliminates $H(x)$ in terms of $h(a - x)$ and $h(x)$, then
substituting into successive equations) collapses the system to
the single row
\[
\frac{2 q r}{p^{3}}\,(2 p^{2} - q^{2})\, h(x) = 0.
\]

**Non-vanishing.** $p, q, r > 0$ elementary; $2 p^{2} - q^{2}
= q^{2}(4\sqrt{2} - 1) > 0$ elementary.  Hence $h(x) = 0$ and by
back-substitution $H(x) = 0$.

**Determinant cross-check.** Independent evaluation gives
$\det M_{13} = -2 p^{7} q r (p^{2} - q^{2})(2p^{2} - q^{2})$.  The
two extra factors $p^{7}$ and $(p^{2} - q^{2})$ cancel during
triangular elimination and are not required for the injectivity
conclusion; they appear only as artifacts of the full-determinant
computation.

**Verdict.**
$$\boxed{\text{A15.1b2c (via triangular elimination)}\quad \checkmark[M].}$$

## 2. b2d: full Sub-wedge A ($e/2 \le R < d/2$)

**Two natural thresholds.**  Set $\kappa := e - \delta = 2e - d$ and
$\lambda := d - \sigma$.  Numerically $\kappa \approx 0.0849495$.
Because $\sigma < \varepsilon_{\max} = \tfrac12\log(5/4) < 2\delta$
(numerically $0.1116 < 0.1178$), always $\kappa < \lambda$:
$\lambda - \kappa = 2\delta - \sigma > 0$.

**Case A ($\sigma \le d/2$).**  Cell decomposition:
$(R, \kappa) \cup (\kappa, \sigma)$.  Both cells produce a $19\times 19$
typed block with coefficient matrix
$\det M_{\pm} = \pm p^{8} r (p^{2} - q^{2})^{3} F$, where
\[
F = 2 p^{4} - 3 p^{2} q^{2} - p^{2} r^{2} + q^{4} - q^{2} r^{2}.
\]

**Case B ($\sigma > d/2$).**  Cell decomposition:
$(R, \kappa) \cup (\kappa, \lambda) \cup (\lambda, \sigma)$.  The first
two cells are handled by the same $19\times 19$ blocks as in Case A.
The third cell $(\lambda, \sigma)$ admits a $13$-value triangular
elimination whose scalar reduction is the b2c factor
$(2 q r / p^{3})(2p^{2} - q^{2})$.

**Elementary $F < 0$.**  Set $B := (q/p)^{2} = 2^{-3/2}$ and
$\theta := (r/p)^{2} = (\log 3 / \log 2)(2/3)^{3/2}$.  Then
\[
F / p^{4} = (2 - 3B + B^{2}) - (1 + B)\,\theta,
\]
and we prove
\[
\frac{2 - 3B + B^{2}}{1 + B} \;<\; \frac{4}{5} \;<\; \theta.
\]

**Left inequality.**  Substitute $B = 1/(2\sqrt 2)$ and clear
denominators: the inequality is equivalent to $53 < 38\sqrt{2}$,
whose square is $2809 < 2888$.

**Right inequality.**  $\theta > (3/2)(2/3)^{3/2} = \sqrt{2/3}$ using
$\log 3 / \log 2 > 3/2 \iff 3 > 2\sqrt 2 \iff 9 > 8$.  Then
$\sqrt{2/3} > 4/5 \iff 2/3 > 16/25 \iff 50 > 48$.

Both are elementary.  Hence $F < 0$, and both $19$-blocks are
invertible.

**Third-cell mechanism.**  For $x_{0} \in (\lambda, \sigma)$ the
elimination gives $h(x_{0}) = 0$; the equation at $u = T - x_{0}$
reads $p h(a - x_{0}) - q h(x_{0}) = 0$, so $h(a - x_{0}) = 0$.
For $h(d - x_{0})$: if $d - x_{0} \le R$, zero by support; otherwise
$d - x_{0} \in (\lambda, \sigma)$ and the same third-cell elimination
applies.  Substituting into the defect equation yields $H(x_{0}) = 0$.

**Reduction to b2b/b1.**  Once $h = 0$ on $(R, \sigma)$ and $H = 0$
on $(0, \sigma)$-visibility, the defect equation is homogeneous on
$(\sigma, a)$; the weighted-reflection kill of b2b applies; tail
value $H(t)$ for $0 < t < R$ vanishes as well (all coefficients
land in $(R, a)$ already killed or below $R$).  Support collapses to
$(R, T)$; A15.1b1 closes the residual.

**Verdict.**
$$\boxed{\text{A15.1b2d (full Sub-wedge A)}\quad \checkmark[M].}$$

## 3. Consolidated status after b2c reconstruction and b2d

| Item | Verdict |
|---|---|
| A15.1b0 pure-tail injectivity ($S < T$) | $\checkmark[M]$ |
| A15.1b1 horizon-open $S = T$ endpoint | $\checkmark[M]$ |
| A15.1b2a mixed strip $R \ge e$ | $\checkmark[M]$ |
| A15.1b2b mixed strip Sub-wedge A restricted-tail ($e/2 \le R < e$, $\sigma \le R$) | $\checkmark[M]$ |
| A15.1b2c mixed strip descent to $R = d/2$ (triangular elim.) | $\checkmark[M]$ |
| A15.1b2d full Sub-wedge A ($e/2 \le R < d/2$) | $\checkmark[M]$ |
| Consolidated: $e/2 \le R < T$ | $\checkmark[M]$ (Cor.~\ref{cor:p12-mixed-strip-descent-to-ehalf}) |
| Descent below $R = e/2$ | $?[O]$ |
| Exact corner $T_0 = T = S$ | $?[O]$ |
| Chamber wall $T_0 = c$ | $?[O]$ |

## 4. Point-orbit evidence below $R = e/2$

Independent point-orbit computation (finite typed elimination, not
Galerkin) tested at $R = 0.07$ (below $e/2 \approx 0.0719$) closes
every tested representative; the elimination factor again contains
$F$.  A finite visibility-cell cover with a uniform closure bound is
not yet established.

**Verdict:** $?[O]$; strong numerical/exact-orbit evidence for
kernel triviality throughout $0 < R < e/2$; a proof requires
completing the visibility-cell enumeration.

## 5. Firewall

Unchanged.  R14 firewall from P11 preserved.  Even a full closure of
Open Problem~\ref{open:p12-below-ehalf} would decide only
localized-hub kernel triviality; by R36-A1 (P11) this is dense range
of $P_{\mathcal A} H_{T_0}$, a modulus-layer statement.  Neither
polar-gauge convergence nor strong terminal transport nor a canonical
mediator for Object~X follow.

## 6. Adversarial checks performed

1. Elementary lower bound $\theta > 4/5$: verified numerically
   ($\theta \approx 0.8627$) and by the chain $\theta > \sqrt{2/3}
   > 4/5$; both steps elementary.
2. Elementary upper bound $(2 - 3B + B^{2})/(1 + B) < 4/5$: verified
   numerically ($\approx 0.7863$) and via
   $53 < 38\sqrt{2}, 2809 < 2888$; elementary.
3. $F < 0$: $F \approx -6.21\cdot 10^{-3}$, consistent with the
   elementary chain.
4. Third-cell / b2c factor $(2qr/p^{3})(2p^{2} - q^{2}) \approx 0.900$
   strictly positive; identical between b2c triangular reduction and
   b2d third-cell reduction.
5. $\kappa < \lambda$: from $\varepsilon_{\max} \approx 0.1116 <
   2\delta \approx 0.1178$; elementary.
6. User's test configuration $(R, \sigma) = (0.08, 0.110)$ verified
   in Sub-wedge A full-tail ($R \in [e/2, d/2)$, $\sigma > R$) with
   Case-B decomposition ($\sigma > d/2$).
