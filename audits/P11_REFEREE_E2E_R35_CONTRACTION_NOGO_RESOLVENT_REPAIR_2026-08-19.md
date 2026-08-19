# P11 End-to-End Referee R35 — Contraction no-go for \(R_{T_0}\), exact resolvent remainder, and repair of R34's Neumann tail

Date: 2026-08-19

## Target

Close the R34-C spectral-gap question (module `P11_O3ae_HubOffSupport_Representation.tex`,
audit R34) in its **contraction-route form**, and repair an imprecise formulation in the R34
audit concerning the divergent Neumann "tail." No polar-gauge, terminal-transport, Object-X,
or RH consequence is drawn. R30-F and R32-F remain `?[O]`.

## Repo sync

`main` at start of this audit: `43fac94695399b245b6fe1893997ac3d534df3b7` — "Add P11 R34
Neumann-series audit for B_{T0} and open spectral-gap gate."

Inputs: P11 §2 definitions of \(\eta_{p,k}\) (2.1), \(J_{p,R}\) (2.2), \(\mathsf Q_R\) (2.3),
\(H_{T_0}\) (2.5), \(R_{T_0}\) (2.6); R34 audit.

---

## 1. Two-prime lower bound: \(T_0>\log3\Rightarrow\|R_{T_0}\|>1\)

### Setup

For \(p\in\{2,3\}\) put \(\tau_p:=\tfrac12\log p\). Fix \(T_0>\log3\) and choose
\[
0<\varepsilon<\min\Bigl\{T_0-\log3,\ \tfrac{\tau_2}{3},\ \tfrac{\tau_3-\tau_2}{3}\Bigr\}.
\]
Let \(f\in L^2(-T_0,T_0)\), \(\|f\|=1\), \(\operatorname{supp}f\subset(-\varepsilon,\varepsilon)\).
For \(p=2,3\) set the target windows
\[
W_{p,\pm}:=(\pm\tau_p-\varepsilon,\pm\tau_p+\varepsilon).
\]
By the choice of \(\varepsilon\), the four windows \(W_{2,\pm},W_{3,\pm}\) are pairwise disjoint
and disjoint from \((-\varepsilon,\varepsilon)\).

### Theorem R35-A (contraction lower bound)

Let \(\Pi_p\) denote the orthogonal projection of the \(R_{T_0}\)-target field
\(\bigoplus_q L^2(\mathbb R)\otimes(\text{$q$-sector})\) onto
\((\mathbf 1_{W_{p,+}}\oplus\mathbf 1_{W_{p,-}})\otimes(\text{$p$-sector})\). Then
\[
\boxed{
\|\Pi_pR_{T_0}f\|^2=2(\log p)\,p^{-1/2}\Bigl(1-\frac1p\Bigr),\qquad p\in\{2,3\},
}
\tag{R35.1}
\]
and since the \(p=2\) and \(p=3\) target sectors are orthogonal,
\[
\boxed{
\|R_{T_0}f\|^2\ \ge\ \|\Pi_2R_{T_0}f\|^2+\|\Pi_3R_{T_0}f\|^2
=\frac{\log2}{\sqrt2}+\frac{4\log3}{3\sqrt3}\approx1.335830.
}
\tag{R35.2}
\]
Hence
\[
\boxed{
T_0>\log3\ \Longrightarrow\ 
\|R_{T_0}\|\ \ge\ \sqrt{\frac{\log2}{\sqrt2}+\frac{4\log3}{3\sqrt3}}\approx1.15578>1.
}
\tag{R35.3}
\]

### Proof

For \(k=1\), by (2.1), \(\eta_{p,1}=\sqrt{p-1}\,p^{-1/2}\psi_{p,0}\), so
\(\|\eta_{p,1}\|^2=(p-1)/p=1-1/p\). By (2.2), for \(|u|<\tau_p+\varepsilon\le\log3+\varepsilon<T_0\)
(using \(\varepsilon<T_0-\log3\)), the depth \(J_{p,T_0}(u)\ge1\), so by (2.3)–(2.4) the full
\(k=1\) mark survives: \(\mathsf Q_{T_0}(u)\eta_{p,1}=\eta_{p,1}\) on both windows \(W_{p,\pm}\).

The rest operator's \(k=1\) summand for prime \(p\) is
\(\sqrt{\log p}\,p^{-1/4}(D_{\log p}E_{T_0}f)(u)\otimes\mathsf Q_{T_0}(u)\eta_{p,1}\), and
\((D_{\log p}f)(u)=f(u-\tau_p)-f(u+\tau_p)\). Since \(\operatorname{supp}f\subset(-\varepsilon,\varepsilon)\)
and \(\varepsilon<\tau_p/3\) for both \(p\), the two shifted copies \(f(\cdot-\tau_p)\) (supported
in \(W_{p,+}\)) and \(f(\cdot+\tau_p)\) (supported in \(W_{p,-}\)) have disjoint supports; hence
\[
\|\Pi_p(D_{\log p}E_{T_0}f)\|^2=\|f(\cdot-\tau_p)\|^2+\|f(\cdot+\tau_p)\|^2=2.
\]
On each window, no \(k\ge2\) copy of the same prime sector intrudes: for \(p=2\), \(k=2\) shifts
are centered at \(\pm\log2=2\tau_2\), and \(2\tau_2-\varepsilon>\tau_2+\varepsilon\) because
\(\varepsilon<\tau_2/3<\tau_2/2\); for \(p=3\), \(k=2\) shifts are at \(\pm\log3=2\tau_3\), and
analogously disjoint from \(W_{3,\pm}\) for \(\varepsilon<\tau_3/3\). Combined with orthogonality of
different prime sectors in the target field (P11 §2), this gives, after multiplying by the
coefficient \(c_{p,1}^2=(\log p)p^{-1/2}\) and the mark norm \(\|\eta_{p,1}\|^2=1-1/p\),
\[
\|\Pi_pR_{T_0}f\|^2=(\log p)p^{-1/2}\Bigl(1-\frac1p\Bigr)\cdot2=2(\log p)p^{-1/2}\Bigl(1-\frac1p\Bigr),
\]
which is (R35.1). Numerically, \(p=2\): \(2(\log2)2^{-1/2}(1/2)=(\log2)/\sqrt2\approx0.49013\);
\(p=3\): \(2(\log3)3^{-1/2}(2/3)=4(\log3)/(3\sqrt3)\approx0.84571\). Since \(\Pi_2\) and \(\Pi_3\)
project onto orthogonal subspaces (different prime sectors), Pythagoras applied to the
orthogonal decomposition of \(R_{T_0}f\) gives the lower bound (\(\ge\) rather than \(=\), since
other \((p,k)\) summands may add further nonnegative energy) stated in (R35.2). Taking square
roots and using \(\|f\|=1\) gives (R35.3). \(\square\)

Status: \(\boxed{\text{R35-A}\quad\checkmark[M].}\)

### Corollary R35-B (contraction no-go)

\[
\boxed{
\text{For every }T_0>\log3:\qquad \|R_{T_0}\|<1\quad\text{is false}.
}
\]
Equivalently, hypothesis (R34.3) of Proposition R34-B fails identically on the entire range
\(T_0>\log3\), which includes every terminal horizon of eventual interest for large-horizon
questions in this program.

Status: \(\boxed{\text{R35-B, the large-horizon contraction route for R34-C}\quad\checkmark[M]_{\rm neg}.}\)

### Scope

R35-A/B do **not** decide \(\|R_{T_0}\|<1\) for \(0<T_0\le\log3\) (small horizons are untouched).
They do **not** say anything about boundedness or positivity of \(B_{T_0}\), which hold
unconditionally regardless of \(\|R_{T_0}\|\) (Lemma R35-D below). They do **not** rule out
regularity of \(g_{R,S}\) by any other route.

---

## 2. Repair of R34's Neumann "tail"

The R34 audit (§2) writes the divergent-looking tail \(\sum_{n>N}(-1)^n(R_{T_0}^*R_{T_0})^nw\)
as if it were meaningful even when \(\|R_{T_0}^*R_{T_0}\|\ge1\). By R35-B this is now known to
occur on the entire range \(T_0>\log3\), so this formulation must be corrected: at
\(\|A\|\ge1\) (with \(A:=R_{T_0}^*R_{T_0}\)) the infinite series \(\sum_{n>N}(-A)^nw\) need not
converge at all, and "tail" language presupposing convergence of the full series is not
available.

### Lemma R35-C (exact finite resolvent identity)

For every bounded \(A\ge0\), every \(N\ge0\), and \(B:=(I+A)^{-1}\),
\[
\boxed{
B=\sum_{n=0}^N(-A)^n+(-1)^{N+1}A^{N+1}B.
}
\tag{R35.4}
\]
This holds with **no** norm hypothesis on \(A\).

### Proof

Induction on \(N\). For \(N=0\): \((I+A)B=I\Rightarrow B=I-AB\), which is (R35.4) with \(N=0\).
Assume (R35.4) at \(N\). Then
\[
B=\sum_{n=0}^N(-A)^n+(-1)^{N+1}A^{N+1}B
=\sum_{n=0}^N(-A)^n+(-1)^{N+1}A^{N+1}(I-AB)
=\sum_{n=0}^{N+1}(-A)^n+(-1)^{N+2}A^{N+2}B,
\]
using \(B=I-AB\) in the last step. \(\square\)

Status: \(\boxed{\text{R35-C}\quad\checkmark[M],\text{ unconditional.}}\)

**Correction directive for R34:** the phrase "the partial-sum tail
\(\sum_{n>N}(-1)^n(R_{T_0}^*R_{T_0})^nw\)" in R34 §3 item 1 must be replaced by the exact
resolvent remainder
\[
\boxed{(-1)^{N+1}(R_{T_0}^*R_{T_0})^{N+1}B_{T_0}w,}
\]
which is well defined by (R35.4) regardless of \(\|R_{T_0}\|\). The mathematical question R34
intended — whether this remainder lies in a fixed Sobolev class for some finite \(N\) — survives
this correction verbatim; only the divergent-series language is repaired.

### Lemma R35-D (unconditional rescaled Neumann representation)

For every bounded \(A\ge0\) and every \(M\ge\|A\|\), with \(Q_M:=(MI-A)/(1+M)\),
\[
0\le Q_M\le\frac{M}{1+M}I,\qquad \|Q_M\|\le\frac{M}{1+M}<1,
\]
and
\[
\boxed{
B=(I+A)^{-1}=\frac1{1+M}\sum_{n=0}^\infty Q_M^n,
}
\tag{R35.5}
\]
convergent in operator norm.

### Proof

Since \(0\le A\le MI\), \(0\le MI-A\le MI\), giving the stated bound on \(Q_M\), hence
\(\|Q_M\|<1\) and the geometric series \(\sum Q_M^n=(I-Q_M)^{-1}\) converges in norm. Direct
computation gives \(I-Q_M=(1+A)/(1+M)\), so
\((I-Q_M)^{-1}=(1+M)(I+A)^{-1}=(1+M)B\), i.e. \(B=(1+M)^{-1}(I-Q_M)^{-1}=(1+M)^{-1}\sum_nQ_M^n\).
\(\square\)

Status: \(\boxed{\text{R35-D}\quad\checkmark[M],\text{ unconditional (holds for every bounded }A\ge0\text{, no gap needed).}}\)

### What R35-C/D do and do not settle

They show that **no spectral gap of \(R_{T_0}\) is a prerequisite for the existence of some
convergent series representation of \(B_{T_0}\)**. This means R34-C, read as "does a
Neumann-type series for \(B_{T_0}\) exist," is now answered unconditionally in the affirmative
by (R35.5) — trivially, and without any new input into the regularity of \(g_{R,S}\). What
remains genuinely open is **not existence of a series**, but whether the operators
\(A^{N+1}\) (finite resolvent remainder, R35-C) or \(Q_M^n\) (rescaled series, R35-D) possess any
concrete regularity-, support-, or range-improving structure. That is a **smoothing /
fingerprint** question about the iterated action of \(A=R_{T_0}^*R_{T_0}\), not a spectral-gap
question, and it is not decided here.

---

## 3. Split verdict on R34-C

| Reading of R34-C | Status after R35 |
|---|---|
| (a) Naive unscaled contraction route: does \(\|R_{T_0}\|<1\) hold (for large horizons)? | `✗[M]` — false for every \(T_0>\log3\) (R35-A/B) |
| (b) Does *some* norm-convergent series representation of \(B_{T_0}\) exist at all? | `✓[M]` — always, unconditionally (R35-D) |
| (c) Do the iterated remainder terms carry regularity/support structure usable for R32-F(i)? | `?[O]` — genuinely open, unaffected by (a)/(b) |

The R34 audit's framing conflated (a) and (c) under one open-problem label. R35 separates
them: (a) is now closed negatively for large horizons, (b) is a triviality that was not the
real obstruction, and (c) is the only surviving mathematical content, now stated without any
reference to a spectral gap.

---

## 4. Consequence for the R32-F route map

Because (a) is dead for \(T_0>\log3\), Strategy (i) of Open Problem R32-F ("regularity of
\(g_{R,S}\) via a Neumann series requiring a spectral gap") is not viable in that form for the
large terminal horizons of ultimate interest. The residual content (c) could in principle still
be pursued directly on \(A^{N+1}\) or \(Q_M^n\), but this audit does not pursue it, in line with
the programme decision to move next to Strategy (ii): the localized annular range/annihilator
fingerprint of \(\Sigma_{T_0}=H_{T_0}B_{T_0}H_{T_0}^*\), to be opened as R36. R36 must *first*
decide whether \(\ker(H_{T_0}E_{\mathcal A})\) is nontrivial before attempting to construct an
annihilator witness \(y\); this is flagged explicitly as R36-A and is not addressed here.

---

## 5. Verdict and remaining status

| Item | Status |
|---|---|
| R35-A two-prime lower bound \(\|R_{T_0}\|\ge1.1557\ldots\) for \(T_0>\log3\) | ✓[M] |
| R35-B contraction route dead for \(T_0>\log3\) | ✓[M]\(_{\rm neg}\) |
| R35-C exact finite resolvent remainder identity | ✓[M], unconditional |
| R35-D unconditional rescaled Neumann representation of \(B_{T_0}\) | ✓[M], unconditional |
| R34-C (a) naive contraction reading | ✗[M] for \(T_0>\log3\) |
| R34-C (b) existence of any convergent series for \(B_{T_0}\) | ✓[M], trivial |
| R34-C (c) regularity/fingerprint of iterated remainder | ?[O] |
| Regularity of \(g_{R,S}\) on \(\mathcal A_{R,S}\) | not obtained |
| R32-F | ?[O] unchanged |
| R30-F | ?[O] unchanged |
| Polar gauge / terminal transport / Object-X / RH | not addressed |

### Adversarial defence

One could object that the disjointness/orthogonality argument in R35-A is only sketched. It is
not: the choice of \(\varepsilon\) is explicit and simultaneously guarantees (i) full retention
of the \(k=1\) mark via the depth condition (2.2)–(2.4), (ii) disjointness of the two shifted
copies of \(f\) from each other and from \(\operatorname{supp}f\), and (iii) disjointness from the
\(k\ge2\) shifts of the same prime. All three follow from elementary interval arithmetic given
the stated bound on \(\varepsilon\); no asymptotic or non-explicit step is used. One could also
object that (R35.2) is only a lower bound, not an exact value of \(\|R_{T_0}\|^2\) — this is
correct and intended: a lower bound already suffices to falsify \(\|R_{T_0}\|<1\).

### What R35 explicitly does not deliver

- No value or bound for \(\|R_{T_0}\|\) when \(T_0\le\log3\).
- No regularity statement for \(g_{R,S}\).
- No resolution of R32-F or R30-F.
- No polar-gauge, terminal-transport, Object-X, or RH consequence.
- No pursuit of the residual smoothing question (c); that is left for a possible future audit,
  distinct from R36.
