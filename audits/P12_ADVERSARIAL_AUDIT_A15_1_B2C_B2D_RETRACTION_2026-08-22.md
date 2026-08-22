# P12 Adversarial Audit — b2c and b2d proof retractions; P1/P2 verified

**Date:** 2026-08-22 (second round, adversarial)
**Repository head at start:** `07a068f`
**Retraction commit:** `a6b4595`
**Auditor:** Perplexity, in strict adversarial mode requested by user.

## 0. Summary

Two proof retractions and three verified new lemmas.

**Retractions ($\times[M]$ on proof; theorem statement not refuted):**

1. **b2c proof.** Uses $u = 3a - x$ and $u = 2b - x$ as elimination
   sources. For $x \in (R, \sigma)$ with $\sigma < \varepsilon_{\max}
   = \tfrac12\log(5/4)$, both source positions exceed
   $c = \tfrac12\log 5$ and hence $T_{0} < c$; they lie strictly
   outside the source horizon $(0, T_{0})$.
2. **b2d proof.** Asserts two $19\times 19$ blocks and a Case-B
   third-cell reduction identical to the retracted b2c triangular
   factor.  The 19 sources are neither enumerated nor is the
   cancellation table given; the Case-B step inherits the b2c defect.

**Statements not refuted.** Theorems~\ref{thm:p12-b2c} and
\ref{thm:p12-b2d} revert to $?[O]$.

**New verified lemmas (independent of retracted proofs):**

3. **P1/P2 identities** from GPT's 6 raw source equations are
   symbolically valid, with explicit multiplier vectors.
4. **Case-B non-degeneracy** $c_{0} = 2r/p > 1$ from an elementary
   inequality $\log 3 > \log 2$.
5. **Under $\sigma \le d/2$:** for every $0 < x < \sigma$,
   $H(d - x) = 0$, hence P1 collapses to $H(x) + l(x) = 0$; and for
   $\sigma < x < \min(\varepsilon, d - \sigma)$, $l(x) = 0$ — a new
   horizon-generated null interval on the upper half.

**Status of the 13-source horizon-legal certificate proposed by GPT:**
neither confirmed nor refuted.  Verifying it requires the 7--8
additional raw source equations at
$\{d - x, T - d + x, 2d - x, a + b - x, T + \delta - x, T - \delta + x, 3d - x, 3e + x\}$,
which need the full operator-side convention to be spelled out.  A
row-multiplier vector was proposed by GPT but not exhibited.

## 1. Horizon violation in the retracted b2c

Repo b2c manuscript (commit `2eff382`, retracted here in `a6b4595`)
uses among its 13 sources the positions $u = T + (a - x) = 3a - x$
and $u = 2b - x$.  For $x \in (R, \sigma)$ with
$\sigma < \varepsilon_{\max} = \tfrac12\log(5/4)$:

$$
3a - x \;>\; 3a - \sigma \;>\; 3a - \varepsilon_{\max}
= 3a - \tfrac12\log(5/4) \approx 0.9281,
$$
$$
2b - x \;>\; 2b - \varepsilon_{\max}
= \log 3 - \tfrac12\log(5/4) \approx 0.9870.
$$

Both exceed $c = \tfrac12\log 5 \approx 0.8047$ and hence
$T_{0} < c$.  Neither is a legal source position.  Additionally, the
manuscript step "repeat the triangular elimination at
$x_{1} = a - x_{0}$" requires $u = T + x_{1} = 3a - x_{0}$, which is
again outside the horizon.

## 2. Documentation gap in the retracted b2d

The manuscript claims two $19\times 19$ typed blocks
(Lemma~\ref{lem:p12-b2d-19blocks}) with determinant
$\pm p^{8} r (p^{2} - q^{2})^{3} F$ and forwards the enumeration
to the audit file.  Neither the manuscript nor the audit exhibits
the 19 typed source positions or a symbolic cancellation table.
The Case-B third-cell reduction (Lemma~\ref{lem:p12-b2d-thirdcell})
lists 13 source points including $u = 3a - x$ (renamed at the level
of arithmetic combination as $T + (a - x)$) and $u = 2b - x$
(as $a + b - x$ in some presentations — check: $a + b - x =
a + (a + d) - x = 2a + d - x$, which is $T + d - x$, INSIDE horizon
if $d - x < \sigma$; but GPT's audit lists both $a+b-x$ and
$2b-x$ separately.  On re-inspection GPT's critique explicitly
targets $2b - x$ and $3a - x$; the repo b2d Case-B list of 13 in
Lemma~\ref{lem:p12-b2d-thirdcell} contains $3a-x$ and $2b-x$ verbatim.)

Both suffice for retraction of the proof.

## 3. P1/P2 identities: symbolic proof

Take GPT's six raw source equations verbatim as axioms:

\begin{align*}
A^-:\quad & -p h(x) - p l(x) - r h(d + x) - r H(d - x) - q h(a + x) = 0, \\
A^+:\quad & p h(x) - p H(x) - r h(d - x) - q h(a - x) = 0, \\
B^-:\quad & p h(d - x) - p H(d - x) - r h(x) - q h(e + x) = 0, \\
B^+:\quad & p h(d + x) + r h(x) - q h(e - x) = 0, \\
T^-:\quad & p h(a - x) + r h(e - x) - q h(x) = 0, \\
T^+:\quad & p h(a + x) + r h(e + x) + q h(x) = 0.
\end{align*}

The coefficient matrix (rows: equations, columns:
$h(x), h(a-x), h(a+x), h(d-x), h(d+x), h(e-x), h(e+x), l(x), H(x), H(d-x)$)
has rank $6$ over $\mathbb Q(p, q, r)$.

### 3.1 P1: $H(x) + l(x) = -2 (r/p)\, H(d - x)$

The unique row-multiplier vector
$$
(c_{A^-}, c_{A^+}, c_{B^-}, c_{B^+}, c_{T^-}, c_{T^+})
= \bigl(-\tfrac{1}{p},\; -\tfrac{1}{p},\; -\tfrac{r}{p^{2}},\;
-\tfrac{r}{p^{2}},\; -\tfrac{q}{p^{2}},\; -\tfrac{q}{p^{2}}\bigr)
$$
yields
\[
c_{A^-} A^- + c_{A^+} A^+ + c_{B^-} B^- + c_{B^+} B^+ + c_{T^-} T^- + c_{T^+} T^+
\;=\; H(x) + l(x) + \frac{2r}{p}\, H(d - x).
\]

Symbolic verification (sympy `linsolve` on the $6\times 10$ system)
confirms the multiplier vector and reduces the combination to zero
identically.

### 3.2 P2: $H(x) - l(x) = 2 D(x) / p^{2}$

with $D(x) := (p^{2} - q^{2} - r^{2})\, h(x)
+ q r\,[h(e - x) - h(e + x)]$.

Row-multiplier vector
$$
(c_{A^-}, c_{A^+}, c_{B^-}, c_{B^+}, c_{T^-}, c_{T^+})
= \bigl(+\tfrac{1}{p},\; -\tfrac{1}{p},\; -\tfrac{r}{p^{2}},\;
+\tfrac{r}{p^{2}},\; -\tfrac{q}{p^{2}},\; +\tfrac{q}{p^{2}}\bigr).
$$

Symbolic verification confirms this and reduces the combination
to zero identically.

### 3.3 Sanity check against Repo b2b

$A^+$ from GPT reads $p h(x) - p H(x) - r h(d - x) - q h(a - x) = 0$,
which is identical (as a symbolic identity in the visible values) to
Repo b2b's $E_{\sigma}$-source equation
$p h(x) - r h(d - x) - q h(a - x) - p H(x) = 0$
at $x \in (d, \sigma)$ (in the sub-case $\mathrm{sgn}(x - d) = -1$).
This is one independent Repo-verified anchor for GPT's axiom system.

**Status of the other five axioms** (namely $A^-, B^\pm, T^\pm$):
they are not currently anchored in the Repo.  The audit trusts them
as given by GPT for the purposes of the P1/P2 derivations, but flags
that they must be re-derived from the fully-spelled-out operator
convention before any $\checkmark[M]$-grade result depending on them
is booked.

## 4. Case-B non-degeneracy: $c_{0} = 2r/p > 1$

$c_{0} = 2r/p = 2 \sqrt{\log 3 / \log 2}\cdot (2/3)^{3/4}$
$\approx 1.8577 > 1$.  Elementary: $c_{0} > 1 \iff 4 r^{2} > p^{2}
\iff 4 \log 3 \cdot 2^{3/2} > \log 2 \cdot 3^{3/2}
\iff \log 3 / \log 2 > 3\sqrt{3}/(8\sqrt{2}) \approx 0.4593$.
Since $\log 3 > \log 2$ and $3\sqrt{3}/(8\sqrt{2}) < 1$, the
inequality follows from $\log 3 > \log 2$ (equivalent to $3 > 2$).

Consequence: the $2\times 2$ system
\[
\begin{pmatrix} 1 & c_{0} \\ c_{0} & 1 \end{pmatrix}
\begin{pmatrix} H(x) \\ H(d - x) \end{pmatrix}
= \begin{pmatrix} -l(x) \\ -l(d - x) \end{pmatrix}
\]
has determinant $1 - c_{0}^{2} \approx -2.451 \ne 0$; hence $H(x)$
and $H(d - x)$ are uniquely determined by $l(x), l(d - x)$ on the
overlap interval $I = (d - \sigma, \sigma)$.

**Status:** $\checkmark[M]$ under the assumption that GPT's 6 axioms
are correct raw source equations.

## 5. Sub-case $\sigma \le d/2$: new horizon-generated null interval

Under $\sigma \le d/2$, for every $x \in (0, \sigma)$:
$d - x \ge d - \sigma \ge d/2 \ge \sigma$, so $H(d - x) = 0$
(zero-extension of $H$ outside $(0, \sigma)$).

From P1: $H(x) + l(x) = 0$, i.e. $H(x) = -l(x)$ for all
$x \in (0, \sigma)$.

For $x \in (\sigma, \min(\varepsilon, d - \sigma))$: $H(x) = 0$
(since $x > \sigma$) and $H(d - x) = 0$ (since $d - x > \sigma$).
P1 forces $l(x) = 0$.

$l(x) = h(T - x)$, so $h$ vanishes on
$(T - \min(\varepsilon, d - \sigma), T - \sigma)$, a nonempty
open sub-interval of the upper half $(a, T)$.

**Status:** $\checkmark[M]$ under the same assumption.

## 6. What remains to close b2c and b2d

To promote b2c from $?[O]$ to $\checkmark[M]$ via GPT's proposal:

1. **Explicit 13-source certificate.**  Provide the 13 raw source
   equations at
   $\{a+x, b-x, T+x, T-x, d-x, T-d+x, 2d-x, a+b-x, e+x, T+\delta-x,
   T-\delta+x, 3d-x, 3e+x\}$, and a row-multiplier vector
   $(c_{1}, \dots, c_{13})$ such that
   $\sum c_{k}\,\text{eq}_{k} = [2 (p^{2} - q^{2})(2p^{2} - q^{2})
   / (p^{2} r)]\, h(x)$.
2. **Horizon check per source.** Verify each source position lies
   in $(0, T_{0})$ throughout the b2c defect stratum
   $d/2 \le R < e$, $\sigma > R$, $x \in (R, \sigma)$.
3. **Operator-convention check.** Anchor the seven source equations
   at $\{d-x, T-d+x, 2d-x, a+b-x, T+\delta-x, T-\delta+x, 3d-x, 3e+x\}$
   in the same convention that produces $A^\pm, B^\pm, T^\pm$.

Task 1 is symbolic; Task 2 is elementary once each source position
is written out; Task 3 needs the full operator definition (currently
only implicit in the Repo).

## 7. Firewall

R14 firewall of P11 unchanged.  No P12 statement in this audit
crosses to polar gauge, terminal transport, Object~X, or RH.  Even a
full closure of both retracted theorems would produce a
modulus-layer statement only (dense range of the annular hub
projection $P_{\mathcal A} H_{T_{0}}$).

## 8. Committed changes this round

- `papers/P12_Adelic_Hub_Injectivity_Program.tex`: retraction note in
  abstract; consolidated corollary reduced to strata (i)--(iv); two
  open problems booked (`open:p12-subwedgeA-open` for
  $e/2 \le R < e, \sigma > R$; `open:p12-below-ehalf` unchanged).
- `papers/P12_sections/P12_A15_1b2c_MixedStripDescentToDHalf.tex`:
  retraction framebox at top; theorem tagged "proof retracted"; proof
  environment tagged "Retracted proof, kept for archival adversarial
  review".
- `papers/P12_sections/P12_A15_1b2d_MixedSubWedgeAFullTail.tex`:
  same retraction framebox and tags.
- `audits/P12_ADVERSARIAL_AUDIT_A15_1_B2C_B2D_RETRACTION_2026-08-22.md`:
  this file.

Consolidated proven front after retraction:
$$
\boxed{2a < T_{0} < c,\quad e \le R < T,\quad T \le S \le T_{0}
\implies \ker L_{R,S,T_{0}}^{\{a,b,2a\}} = \{0\}}
$$
plus b2b Sub-wedge~A restricted-tail $e/2 \le R < e$, $\sigma \le R$.
