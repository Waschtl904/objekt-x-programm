# P11 End-to-End Referee R34 — Neumann-series route to $g_{R,S}$ regularity and the spectral-gap gate for $B_{T_0}$

Date: 2026-08-19 (corrected 2026-08-19 by R35; see "Correction notice" below)

## Correction notice (added by R35)

This audit originally spoke of "the partial-sum tail $\sum_{n>N}(-1)^n(R_{T_0}^*R_{T_0})^nw$"
in §3 as if this infinite series were meaningful even when $\|R_{T_0}^*R_{T_0}\|\ge1$. This is
not legitimate: at $\|A\|\ge1$ (with $A:=R_{T_0}^*R_{T_0}$) the series $\sum_{n>N}(-A)^nw$ need
not converge at all, so it cannot be called a "tail." Audit R35
(`P11_REFEREE_E2E_R35_CONTRACTION_NOGO_RESOLVENT_REPAIR_2026-08-19.md`) shows this case
($\|R_{T_0}\|\ge1$) actually occurs for every $T_0>\log3$, and replaces the divergent-tail
language by the exact, unconditional finite resolvent remainder identity
\[
B_{T_0}=\sum_{n=0}^N(-A)^n+(-1)^{N+1}A^{N+1}B_{T_0}
\]
(R35-C), which holds with no norm hypothesis on $A$. All instances of "tail" below should be
read as this exact remainder term, not as a divergent infinite sum.

Furthermore, R35 shows the spectral gap $\|R_{T_0}\|<1$ is **not** a necessary gate for a
convergent series representation of $B_{T_0}$ at all: R35-D gives an unconditional
rescaled Neumann series $B_{T_0}=(1+M)^{-1}\sum_nQ_M^n$ for any $M\ge\|R_{T_0}^*R_{T_0}\|$,
convergent in operator norm regardless of whether $\|R_{T_0}\|<1$. Consequently, **Open
Problem R34-C below must no longer be read as "does a Neumann representation of $B_{T_0}$
exist"** (R35-D answers that trivially and unconditionally in the affirmative). R34-C is
split by R35 into:

- (a) the naive unscaled contraction route $\|R_{T_0}\|<1$ — closed **negatively** by R35-A/B
  for every $T_0>\log3$;
- (c) whether the iterated remainder $A^{N+1}$ (or $Q_M^n$) carries regularity/support
  structure usable for R32-F(i) — this remains genuinely **open**, and is now a regularity/
  fingerprint question about the iterates, not a spectral-gap question.

The text of §§1–4 below is retained for historical provenance but must be read through this
correction; in particular the phrase "spectral gap" in the original title and in Open Problem
R34-C no longer designates a necessary gate.

## Target

Execute Strategy (i) of Open Problem R32-F (module `P11_O3ae_HubOffSupport_Representation.tex`):
study the regularity of
\[
g_{R,S}=-B_{T_0}H_{T_0}E_{S,T_0}j_{R,S},\qquad B_{T_0}=(I+R_{T_0}^*R_{T_0})^{-1},
\]
via a Neumann-series expansion of $B_{T_0}$, as suggested at the close of R33.

No polar-gauge, terminal-transport, Object-X, or RH consequence is drawn.

## Repo sync

`main` at start of this audit: `a745281d7d465e08ab2356004dc6fbaac1222ea9` — "Integrate P11 R33 Gamma symbol bridge into O3 chain".

Inputs: R32 audit/module (`P11_O3ae_HubOffSupport_Representation.tex`), R33 audit/module
(`P11_O3af_Gamma_Symbol_Bridge.tex`, referenced), definition of $R_{T_0}$ and $B_{T_0}$ from
P11 §2.

---

## 1. The unconditional resolvent identity

### Lemma R34-A

For every $w\in L^2(-T_0,T_0)$, setting $x:=B_{T_0}w$,
\[
\boxed{x = w - R_{T_0}^*R_{T_0}\,x.}
\tag{R34.1}
\]

### Proof

Immediate from $(I+R_{T_0}^*R_{T_0})x=w$. $\square$

Status: $\checkmark[M]$ — this is an exact fixed-point identity, valid for every bounded
positive $R_{T_0}^*R_{T_0}$, with no norm hypothesis.

---

## 2. Why the identity alone does not give a full-series Neumann expansion

Iterating (R34.1) formally suggests
\[
x \;\overset{?}{=}\; \sum_{n=0}^\infty (-1)^n (R_{T_0}^*R_{T_0})^n w.
\tag{R34.2}
\]
This full infinite series converges in operator norm to $(I+R_{T_0}^*R_{T_0})^{-1}$ **iff**
$\|R_{T_0}^*R_{T_0}\|<1$, equivalently $\|R_{T_0}\|<1$. Boundedness of $B_{T_0}$ (which
holds unconditionally, since $R_{T_0}^*R_{T_0}\ge0$ makes $(I+R_{T_0}^*R_{T_0})^{-1}$
bounded with $\|B_{T_0}\|\le1$ regardless of $\|R_{T_0}\|$) does **not** imply
$\|R_{T_0}\|<1$. If $\|R_{T_0}\|\ge1$ — which R35 shows actually holds for every
$T_0>\log3$ — the *full* series (R34.2) diverges in norm and cannot be used termwise to
transfer regularity from $w$ to $x$ by naive truncation. **This does not, however, mean no
convergent series representation of $B_{T_0}$ exists at all**; see R35-D for an unconditional
rescaled alternative, and R35-C for the exact finite remainder identity that replaces any
informal "tail."

### Proposition R34-B (conditional Neumann representation)

If
\[
\|R_{T_0}\|<1
\tag{R34.3}\label{eq:r34-gap}
\]
then for every $w\in L^2(-T_0,T_0)$,
\[
\boxed{
B_{T_0}w=\sum_{n=0}^\infty(-1)^n(R_{T_0}^*R_{T_0})^n w,
}
\tag{R34.4}
\]
with convergence in $L^2$-norm, geometrically fast: the $N$-term truncation error is
bounded by $\|R_{T_0}\|^{2N+2}\|w\|/(1-\|R_{T_0}\|^2)$.

### Proof

Standard Neumann series for $(I+A)^{-1}$ with $A=R_{T_0}^*R_{T_0}\ge0$ bounded and
$\|A\|<1$ (guaranteed by \eqref{eq:r34-gap} since $\|A\|\le\|R_{T_0}\|^2$). $\square$

Status: $\boxed{\text{R34-B}\quad \checkmark[M]\ \text{conditional on (R34.3), which R35 shows fails for }T_0>\log3.}$

---

## 3. What (R34.3) is not currently known to hold — [superseded for $T_0>\log3$ by R35-A/B]

The operator $R_{T_0}$ is the finite-horizon remainder map introduced in P11 §2
(the "rest" operator complementary to the source hub $H_{T_0}$ in the Feshbach
decomposition of the truncated Weil form). At the time of this audit, nothing in R1–R33
established a quantitative bound $\|R_{T_0}\|<1$; the repository only recorded:

- boundedness of $R_{T_0}$ (used implicitly since $B_{T_0}$ is asserted bounded), and
- boundedness/positivity of $B_{T_0}$ itself, which as noted holds regardless of
  \eqref{eq:r34-gap}.

**R35 has since resolved this negatively for $T_0>\log3$**: a two-window, two-prime
projection argument gives the explicit lower bound $\|R_{T_0}\|\ge\sqrt{\log2/\sqrt2+4\log3/(3\sqrt3)}\approx1.1558>1$
for every $T_0>\log3$, so (R34.3) is false on that entire range.

### Open Problem R34-C (spectral gap for $R_{T_0}$) — [see correction notice above]

~~Decide whether $\|R_{T_0}\|<1$~~ **Superseded.** As corrected above, R34-C now designates only
the residual regularity/fingerprint question (c): does $(R_{T_0}^*R_{T_0})^{N}$ (equivalently,
the exact remainder $A^{N+1}B_{T_0}$ of R35-C, or the rescaled iterates $Q_M^n$ of R35-D) map
$L^2$ into a fixed high-Sobolev class $H^\alpha(-T_0,T_0)$, or otherwise carry usable
support/regularity structure, for some finite $N$ — independent of any spectral-gap hypothesis,
which is now known to fail. The original two remarks below are retained for provenance:

1. **A weaker sufficient substitute.** Full norm control is not necessary if one only
   wants finitely many terms to control regularity on a fixed annulus
   $\mathcal A_{R,S}$: it suffices that the exact remainder $(-1)^{N+1}(R_{T_0}^*R_{T_0})^{N+1}B_{T_0}w$
   (R35-C) lie in a fixed high-Sobolev class $H^\alpha(-T_0,T_0)$ for some finite $N$. This
   reduces R34-C(c) to a **smoothing** question rather than a **norm** question. Compactness/
   smoothing of $R_{T_0}^*R_{T_0}$ is plausible on structural grounds but is not established in
   the repository either.
2. **Non-uniqueness of the decomposition.** Even a positive resolution of R34-C(c) only yields
   regularity of $x=B_{T_0}w$, hence of $g_{R,S}$, on the *whole* interval $(-T_0,T_0)$ in the
   topological sense available; it does not by itself upgrade $g_{R,S}$ to **real-analytic** on
   the annulus $\mathcal A_{R,S}$, which is what R32-F(i) actually needs.

Status: $\boxed{\text{R34-C(a) naive contraction route}\quad \times[M]\ \text{for }T_0>\log3\ \text{(R35-B)};\qquad \text{R34-C(c) regularity/fingerprint}\quad ?[O]\ \text{unchanged.}}$

---

## 4. What this audit adds and does not add

| Item | Status |
|---|---|
| R34-A unconditional fixed-point identity $x=w-R_{T_0}^*R_{T_0}x$ | ✓[M] |
| R34-B Neumann representation of $B_{T_0}$, conditional on $\|R_{T_0}\|<1$ | ✓[M] (conditional; hypothesis now known false for $T_0>\log3$, see R35) |
| R34-C(a) spectral gap $\|R_{T_0}\|<1$ | ✗[M] for $T_0>\log3$ (R35-A/B) |
| R34-C(c) regularity/fingerprint of iterated remainder | ?[O] — still open |
| Regularity (let alone analyticity) of $g_{R,S}$ on $\mathcal A_{R,S}$ | not obtained |
| R32-F | ?[O] unchanged |
| R30-F | ?[O] unchanged |

### What R34 changes

- It converts the vague suggestion "Neumann-series expansion of $B_{T_0}$" from R33's
  closing paragraph into a precisely stated conditional theorem (R34-B) plus an
  explicit, named missing hypothesis (originally R34-C, now split by R35 into (a)/(c)).
- It identifies that even a full resolution of the regularity question would need a further
  step (Sobolev-to-analytic upgrade) before touching R32-F(i).

### What R34 explicitly does not deliver (as originally written)

- No proof or disproof of $\|R_{T_0}\|<1$ — **now disproved for $T_0>\log3$ by R35**.
- No regularity statement for $g_{R,S}$.
- No progress on R32-F(ii) (the fingerprint-property strategy), which remains an
  independent, undecided alternative route.
- No polar-gauge, terminal-transport, Object-X, or RH consequence.

### Adversarial defence

One might object that boundedness of $B_{T_0}$ already "morally" suggests
$\|R_{T_0}\|<1$. This is false in general: $(I+A)^{-1}$ is bounded with norm $\le1$ for
**every** $A\ge0$ bounded, including $\|A\|$ arbitrarily large. So no inference from
boundedness of $B_{T_0}$ to smallness of $\|R_{T_0}\|$ is available — and indeed R35 shows
$\|R_{T_0}\|>1$ occurs generically for $T_0>\log3$.

### Next mathematical target (as of this audit; superseded by R35 §4)

R35 shows fork (a) below is closed negatively for $T_0>\log3$ and recommends proceeding to
Strategy (ii) (R32-F(ii)), opened as R36:

- (a) ~~Attempt to bound $\|R_{T_0}\|$ directly~~ — closed negatively by R35-A/B for $T_0>\log3$.
- (b) Pursue R32-F(ii) instead (the fingerprint-property strategy) — recommended next step,
  taken up starting with R36-A (localized-range/annihilator-kernel triviality test).
