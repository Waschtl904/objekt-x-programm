# P12 End-to-End Referee — corrections and A15.1b2c descent

**Date:** 2026-08-21 (correction pass)
**Repository:** `Waschtl904/objekt-x-programm`
**Papers head at start:** `c11350e` (P12 initial commits)

## Purpose

This audit corrects two errors in the initial P12 commits and books
the new A15.1b2c descent theorem.

## Errors identified in prior P12 commits

### Error 1: H-source equation in b2b

The initial `P12_A15_1b2b_MixedSubWedgeA.tex` (in commit `9093475`) wrote
the H-source at $u = 2a + x$ as

$$p\, g(a + x) + r\, g(e + x) - p\, g(x) = 0.$$

This is wrong.  Derivation from the canonical operator formula
$H_{T_0} = P_{T_0} \sum_{(p,k)} c_{p,k}\, D_{k\log p}\, E_{T_0}$
with $D_s = U_{s/2} - U_{-s/2}$ and $(U_a f)(u) = f(u - a)$ at
$u = 2a + x$ produces the three active branch pairs

- $(2,1)$: $D_{\log 2}f(u) = f(a + x) - f(3a + x)$; second term
  deleted by $P_{T_0}$;
- $(3,1)$: $D_{\log 3}f(u) = f(e + x) - f(c_{\rm up} + x)$; second
  term deleted;
- $(2,2)$: $D_{2\log 2}f(u) = f(x) - f(4a + x)$; second term deleted.

With weights $c_{2,1} = p$, $c_{3,1} = r$, $c_{2,2} = q$, the correct
H-source is

$$\boxed{p\, h(a + x) + r\, h(e + x) + q\, h(x) = 0.}$$

The last term has coefficient $q$ (not $p$) and enters with the sign
of the forward translation (positive, not with fold subtraction).

**Consequence.** The reasoning in the original b2b Step 3 that used
the H-source to derive a cascade $h(y + d) = -(r/p) h(y)$ on
$(e, e + \min(R, \varepsilon))$ is invalidated in that form.

### Error 2: Illegitimate use of $\sigma < e/2$

The original b2b proof also stated "$\sigma < e/2 \le R < x$, the
$H$-term vanishes".  But $\varepsilon_{\max} = c - T = \tfrac12\log(5/4)
\approx 0.11157$, which is larger than $e/2 \approx 0.07192$, so
$\sigma < e/2$ is not implied by the chamber definition.

**Consequence.** The original claim
"$e/2 \le R < e \Rightarrow \ker L = \{0\}$" (unrestricted tail) is
downgraded to $?[O]$.

## Corrections applied

### 1. b2b restricted to $\sigma \le R$

The revised `P12_A15_1b2b_MixedSubWedgeA.tex` proves

$$e/2 \le R < e, \quad T < S < T_0, \quad \sigma := S - T \le R
  \implies \ker L = \{0\}.$$

Under $\sigma \le R$, the tail defect $H\, \mathbf 1_{x < \sigma}$
vanishes for every $x \ge R$, so the E-equation is homogeneous
throughout the lower support and no H-source is needed.  The remaining
proof is a clean transcription of the weighted-reflection kill on
$(R, e) \cup (e, d) \cup (d, a)$, followed by reduction to
Theorem~\ref{thm:p12-b1} (A15.1b1).

The core reduction $h(x) = \alpha h(d - x)$ with
$\alpha = pr/(p^2 - q^2)$ and its iteration
$(1 - \alpha^2) h(x) = 0$ now rest on $\alpha > 1$ elementary from
A14.3a inequalities (Lemma \texttt{lem:p12-alpha-elementary}), no
transcendence input beyond $\log 2, \log 3$ being independent from
unique factorisation.

Verdict:
$$\boxed{\text{A15.1b2b (restricted-tail, } \sigma \le R)\quad \checkmark[M].}$$

### 2. b2a proof reordered

The old b2a claimed the A14.3a upper source applies "verbatim".  With
$T < S$ this is not literally correct because new tail values appear.
The clean order is:

- Lower kill on $(R, a)$ via the same $(p^2 - q^2)$ mechanism;
- H-source-free tail kill via $(E_\sigma)$ giving $H = 0$;
- Support collapses to $(R, T)$, reduce to Theorem~\ref{thm:p12-b1}.

The theorem itself was already correct; only the manuscript proof
sequence needed patching.  Verdict of the theorem is unchanged
$\checkmark[M]$.

### 3. New: A15.1b2c descent to $R = d/2$

The new `P12_A15_1b2c_MixedStripDescentToDHalf.tex` establishes

$$2a < T_0 < c, \quad d/2 \le R < e, \quad T < S < T_0
  \implies \ker L = \{0\},$$

covering both Case (i) $\sigma \le R$ (via b2b) and Case (ii)
$\sigma > R$ (new content).

**Case (ii) mechanism.**  A finite $13\times 13$ typed linear system
$M_{13}\, v = 0$ on 13 visibility-stable target values in
$(R, \sigma)$ has coefficient matrix with determinant

$$\det M_{13} = -2\, p^7\, q\, r\, (p^2 - q^2)\, (2p^2 - q^2).$$

Non-vanishing follows from an elementary lemma:
$p, q, r > 0$; $p^2 - q^2 = q^2(2^{3/2} - 1) > 0$;
$2p^2 - q^2 = q^2(4\sqrt 2 - 1) > 0$.  Numerically
$\det M_{13} \approx -1.26\cdot 10^{-4}$.  All factors verified.

Consequence: $h(x_0) = 0$ and $H(x_0) = 0$ for every $x_0 \in (R,
\sigma)$; the defect strip is cleared; the residual lower half kills
via A15.1b2a-style reflection; and A15.1b1 closes the upper half.

Verdict:
$$\boxed{\text{A15.1b2c (mixed strip descent to } R = d/2)\quad \checkmark[M].}$$

**Combined with b2a:** for $2a < T_0 < c$ and $T < S < T_0$,
kernel triviality holds throughout the mixed strip $d/2 \le R < T$.
This is Corollary~\ref{cor:p12-mixed-strip-consolidated}.

## Consolidated status after correction

| Item | Verdict |
|---|---|
| A15.1b0 pure-tail injectivity ($S < T$) | $\checkmark[M]$ |
| A15.1b1 horizon-open $S = T$ endpoint | $\checkmark[M]$ |
| A15.1b2a mixed strip $R \ge e$ | $\checkmark[M]$ (proof reordered) |
| A15.1b2b mixed strip Sub-wedge A restricted-tail ($e/2 \le R < e$, $\sigma \le R$) | $\checkmark[M]$ |
| A15.1b2c mixed strip descent to $R = d/2$ | $\checkmark[M]$ |
| Consolidated: $d/2 \le R < T$ | $\checkmark[M]$ (Cor.~\ref{cor:p12-mixed-strip-consolidated}) |
| Sub-wedge A full tail ($e/2 \le R < d/2$, $\sigma > R$) | $?[O]$ |
| Descent below $R = d/2$ | $?[O]$ (point-orbit closes every tested rep. in $\le$ 19 typed reductions; finite cell cover not yet established) |
| Exact corner $T_0 = T = S$ | $?[O]$ |
| Chamber wall $T_0 = c$ | $?[O]$ |

## Firewall

Unchanged.  All statements above are modulus-layer.  R14 firewall of
P11 preserved.  No polar-gauge, terminal-transport, Object-X, or RH
consequence follows.

## Adversarial cross-checks performed

1. **H-source coefficient/sign:** re-derived from the canonical hub
   formula, confirmed against the P11 (2.5) definition of $H_{T_0}$.
2. **$\alpha > 1$ lower bound:** derived elementary from $t > \sqrt{2/3}$
   (equivalent to $9\log 3 > 8\log 2$, obvious) and
   $\beta^2 = 2^{-3/2}$ exact.  Numerically $\alpha \approx 1.4368$.
3. **Determinant factorisation:** all four factor signs verified from
   closed forms.  Numerically $\det M_{13} \approx -1.26\cdot 10^{-4}$,
   consistent with the sign pattern.
4. **Local LaTeX compilation:** tectonic 0.15.0 pass (two runs, no
   undefined or multiply-defined references).

## Not decided by this correction

- The initial P12 commit `9093475` contained an incorrect b2b proof.
  The correction rewrites b2b restricted to $\sigma \le R$, and
  introduces b2c to cover the full $R \ge d/2$ strip.
- The false unrestricted b2b statement is not `\times[M]` — it may
  still be true, but its previous proof was invalid.  It is now
  $?[O]$ in Open Problem \texttt{open:p12-subwedgeA-fulltail}
  restricted to $e/2 \le R < d/2, \sigma > R$.
- Descent below $R = d/2$ is a strong `?[O]` with numerical
  point-orbit evidence for triviality throughout, awaiting a finite
  visibility-cell cover argument.
