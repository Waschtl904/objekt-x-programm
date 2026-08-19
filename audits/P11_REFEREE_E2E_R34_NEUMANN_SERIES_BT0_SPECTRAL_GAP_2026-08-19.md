# P11 End-to-End Referee R34 — Neumann-series route to $g_{R,S}$ regularity and the spectral-gap gate for $B_{T_0}$

Date: 2026-08-19

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

## 2. Why the identity alone does not give a Neumann series

Iterating (R34.1) formally gives
\[
x \;\overset{?}{=}\; \sum_{n=0}^\infty (-1)^n (R_{T_0}^*R_{T_0})^n w.
\tag{R34.2}
\]
This series converges in operator norm to $(I+R_{T_0}^*R_{T_0})^{-1}$ **iff**
$\|R_{T_0}^*R_{T_0}\|<1$, equivalently $\|R_{T_0}\|<1$. Boundedness of $B_{T_0}$ (which
holds unconditionally, since $R_{T_0}^*R_{T_0}\ge0$ makes $(I+R_{T_0}^*R_{T_0})^{-1}$
bounded with $\|B_{T_0}\|\le1$ regardless of $\|R_{T_0}\|$) does **not** imply
$\|R_{T_0}\|<1$. If $\|R_{T_0}\|\ge1$, (R34.2) diverges in norm and cannot be used
termwise to transfer regularity from $w$ to $x$.

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

Status: $\boxed{\text{R34-B}\quad \checkmark[M]\ \text{conditional on (R34.3)}.}$

---

## 3. What (R34.3) is not currently known to hold

The operator $R_{T_0}$ is the finite-horizon remainder map introduced in P11 §2
(the "rest" operator complementary to the source hub $H_{T_0}$ in the Feshbach
decomposition of the truncated Weil form). Nothing in the audits R1–R33 establishes a
quantitative bound $\|R_{T_0}\|<1$; the repository only records:

- boundedness of $R_{T_0}$ (used implicitly since $B_{T_0}$ is asserted bounded), and
- boundedness/positivity of $B_{T_0}$ itself, which as noted holds regardless of
  \eqref{eq:r34-gap}.

A search of the P11 paper sections and the C1–C7/O1–O3af audit chain turns up no place
where $\|R_{T_0}\|$ is estimated numerically or structurally. This is therefore a
genuinely new gap, not a previously closed and merely uncited fact.

### Open Problem R34-C (spectral gap for $R_{T_0}$)

Decide whether $\|R_{T_0}\|<1$, or more precisely obtain any explicit bound
$\|R_{T_0}\|\le1-\delta(T_0)$ for some $\delta(T_0)>0$, possibly $T_0$-dependent.

Two remarks sharpen the target:

1. **A weaker sufficient substitute.** Full norm control is not necessary if one only
   wants finitely many terms of (R34.2) to control regularity on a fixed annulus
   $\mathcal A_{R,S}$: it suffices that the partial-sum tail
   $\sum_{n>N}(-1)^n(R_{T_0}^*R_{T_0})^n w$ lie in a fixed high-Sobolev class
   $H^\alpha(-T_0,T_0)$ for some finite $N$, even if the full series diverges in
   operator norm. This reduces R34-C to a **smoothing** question rather than a **norm**
   question: does $(R_{T_0}^*R_{T_0})^{N}$ map $L^2$ into $H^\alpha_{\mathrm{loc}}$ for some
   finite $N=N(\alpha)$? Compactness/smoothing of $R_{T_0}^*R_{T_0}$ is plausible on
   structural grounds (it is built from a difference of a finite-rank-type hub
   correction and a resolvent-smoothed remainder) but is not established in the
   repository either.
2. **Non-uniqueness of the decomposition.** Even a positive resolution of R34-C
   (in either the norm form or the smoothing form) only yields regularity of $x=B_{T_0}w$,
   hence of $g_{R,S}$, on the *whole* interval $(-T_0,T_0)$ in the topological sense
   available; it does not by itself upgrade $g_{R,S}$ to **real-analytic** on the
   annulus $\mathcal A_{R,S}$, which is what R32-F(i) actually needs. Sobolev
   smoothing of arbitrarily high but finite order does not imply analyticity.

Status: $\boxed{\text{R34-C}\quad ?[O].}$

---

## 4. What this audit adds and does not add

| Item | Status |
|---|---|
| R34-A unconditional fixed-point identity $x=w-R_{T_0}^*R_{T_0}x$ | ✓[M] |
| R34-B Neumann representation of $B_{T_0}$, conditional on $\|R_{T_0}\|<1$ | ✓[M] (conditional) |
| R34-C spectral gap $\|R_{T_0}\|<1$ (or smoothing substitute) | ?[O] — new |
| Regularity (let alone analyticity) of $g_{R,S}$ on $\mathcal A_{R,S}$ | not obtained |
| R32-F | ?[O] unchanged |
| R30-F | ?[O] unchanged |

### What R34 changes

- It converts the vague suggestion "Neumann-series expansion of $B_{T_0}$" from R33's
  closing paragraph into a precisely stated conditional theorem (R34-B) plus an
  explicit, named missing hypothesis (R34-C).
- It identifies that even a full resolution of R34-C would need a further step
  (Sobolev-to-analytic upgrade) before touching R32-F(i), and flags a weaker
  "smoothing" reformulation of R34-C that might be more tractable than the full norm
  bound.

### What R34 explicitly does not deliver

- No proof or disproof of $\|R_{T_0}\|<1$.
- No regularity statement for $g_{R,S}$.
- No progress on R32-F(ii) (the fingerprint-property strategy), which remains an
  independent, undecided alternative route.
- No polar-gauge, terminal-transport, Object-X, or RH consequence.

### Adversarial defence

One might object that boundedness of $B_{T_0}$ already "morally" suggests
$\|R_{T_0}\|<1$. This is false in general: $(I+A)^{-1}$ is bounded with norm $\le1$ for
**every** $A\ge0$ bounded, including $\|A\|$ arbitrarily large (e.g. $A=NI$ on a
subspace gives $(1+N)^{-1}\to0$, still perfectly bounded). So no inference from
boundedness of $B_{T_0}$ to smallness of $\|R_{T_0}\|$ is available; R34-C is a genuine,
independent question.

### Next mathematical target

Two forks, either of which is a legitimate next audit:

- (a) Attempt to bound $\|R_{T_0}\|$ directly from its definition in P11 §2 (likely via
  Schur-test or explicit kernel estimates), aiming at R34-C in norm form.
- (b) Pursue R32-F(ii) instead (the fingerprint-property strategy), which does not
  require resolving R34-C at all and may be structurally shorter.
