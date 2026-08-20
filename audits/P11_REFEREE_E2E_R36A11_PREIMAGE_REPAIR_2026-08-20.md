# P11 End-to-End Referee R36-A11 — Preimage repair of folded exposed-cell peeling

Date: 2026-08-20

## Status and supersession

This note is a targeted correction to
`audits/P11_REFEREE_E2E_R36A_LOCALIZED_HUB_RANGE_KERNEL_GATE_2026-08-19.md`.
It supersedes only the old folded exposed-cell statement R36-A11 and the folded peeling
scheme built directly on that old statement. R36-A9 and R36-A10 are unaffected.

Repo base for this correction:

`main = 1d1b530c7d707dd17a6d656574abae24ac29ee5f`.

The old R36-A11 used an image condition of the form

\[
B(I)\subset Z,
\]

where \(B(I)\) lives in the observation variable \(u\), whereas the known-zero region
\(Z\subset(R,S)\) lives in the source variable \(x\) on which \(h\) is defined. This is not
type-correct and does not justify the proof.

Therefore

\[
\boxed{\text{R36-A11(old)}\quad\times[M].}
\]

No earlier peeling run used this lemma to conclude kernel triviality, so this correction does
not retract any proved R36-A, R36-B, or R30-F conclusion.

---

## 1. Terminal-independent branch family

Keep the half-annulus operator from R36-A9:

\[
(L_{R,S,T_0}h)(u)
=\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\Bigl[
\operatorname{sgn}(u-\tau_{p,k})\mathbf1_{(R,S)}(|u-\tau_{p,k}|)
 h(|u-\tau_{p,k}|)
-\mathbf1_{(R,S)}(u+\tau_{p,k})h(u+\tau_{p,k})
\Bigr],
\]

with

\[
\tau_{p,k}=\frac{k\log p}{2},
\qquad
c_{p,k}=\sqrt{\log p}\,p^{-3k/4},
\qquad
\mathcal P_{T_0}=\{(p,k):\tau_{p,k}\le T_0\}.
\]

For each active shift \(\tau\), split the folded geometry into injective affine branches on
source subdomains:

\[
B_{\tau,+}(x)=x+\tau,
\qquad w_{\tau,+}=+c_\tau,
\]

\[
B_{\tau,->}(x)=x-\tau
\quad\text{on }D_{\tau,->}:=(R,S)\cap(\tau,\infty),
\qquad w_{\tau,->}=-c_\tau,
\]

\[
B_{\tau,-<}(x)=\tau-x
\quad\text{on }D_{\tau,-<}:=(R,S)\cap(-\infty,\tau),
\qquad w_{\tau,-<}=-c_\tau.
\]

For the plus branch take \(D_{\tau,+}:=(R,S)\). These branches are defined
terminal-independently as maps into \((0,\infty)\) wherever their displayed formula is
positive; terminal admissibility is imposed only when evaluating at \(u\in(0,T_0)\).
After the R36-A10 breakpoint decomposition, every branch used below is an affine isometry on
its cell-domain and has nonzero weight.

Equivalently, for a.e. \(u\in(0,T_0)\),

\[
\boxed{
(L_{R,S,T_0}h)(u)
=\sum_{\beta:\,u\in B_\beta(D_\beta)}
 w_\beta\,h(B_\beta^{-1}(u)).
}
\tag{A11'.1}
\]

The sum is finite.

Status:

\[
\boxed{\text{branch preimage representation}\quad\checkmark[M].}
\]

---

## 2. R36-A11' — folded known-zero exposed-cell lemma

### Lemma R36-A11' (preimage-correct exposed cell)

Let \(Z\subset(R,S)\) be a measurable **known-zero region** for \(h\), i.e.
\(h=0\) a.e. on \(Z\). Let \(\beta_*\) be one branch, and let
\(I\subset D_{\beta_*}\) be a nonempty open interval contained in a single affine branch
cell. Put

\[
J:=B_{\beta_*}(I).
\]

Assume

\[
J\subset(0,T_0),
\]

and for every competing branch \(\beta\ne\beta_*\),

\[
\boxed{
B_\beta^{-1}\bigl(J\cap B_\beta(D_\beta)\bigr)
\subset Z
\quad\text{modulo null sets}.
}
\tag{A11'.2}
\]

Then every \(h\in L^2(R,S)\) satisfying
\(L_{R,S,T_0}h=0\) a.e. on \((0,T_0)\) obeys

\[
\boxed{h=0\quad\text{a.e. on }I.}
\tag{A11'.3}
\]

### Proof

For a.e. \(u\in J\), the distinguished branch contributes

\[
w_{\beta_*}h(B_{\beta_*}^{-1}(u)).
\]

Any competing branch \(\beta\ne\beta_*\) either has
\(u\notin B_\beta(D_\beta)\), in which case it contributes nothing, or has a preimage

\[
B_\beta^{-1}(u)
\in
B_\beta^{-1}\bigl(J\cap B_\beta(D_\beta)\bigr)
\subset Z
\]

modulo null sets, so its contribution vanishes because \(h=0\) a.e. on \(Z\).
Thus (A11'.1) reduces on \(J\) to

\[
w_{\beta_*}h(B_{\beta_*}^{-1}(u))=0
\quad\text{a.e. }u\in J.
\]

Since \(w_{\beta_*}\ne0\) and \(B_{\beta_*}\) is an affine isometry, null sets are preserved
under pullback and hence \(h=0\) a.e. on
\(I=B_{\beta_*}^{-1}(J)\).
\(\square\)

Status:

\[
\boxed{\text{R36-A11'}\quad\checkmark[M].}
\]

---

## 3. Repaired folded peeling

Set

\[
K_0^-:=(R,S),
\qquad
Z_n^-:=(R,S)\setminus K_n^-.
\]

At stage \(n\), remove every open interval
\(I\subset K_n^-\cap D_{\beta_*}\) contained in a single affine branch cell for which

\[
J=B_{\beta_*}(I)\subset(0,T_0)
\]

and for every competing branch \(\beta\ne\beta_*\),

\[
\boxed{
B_\beta^{-1}\bigl(J\cap B_\beta(D_\beta)\bigr)
\subset Z_n^-
\quad\text{modulo null sets}.
}
\tag{A11'.4}
\]

Define \(K_{n+1}^-\) by deleting the union of all such exposed intervals.

### Proposition (peeling correctness)

For every \(n\ge0\) and every \(h\in\ker L_{R,S,T_0}\),

\[
h=0\quad\text{a.e. on }(R,S)\setminus K_n^-.
\]

### Proof

Induct on \(n\). The statement is vacuous for \(n=0\). If it holds at stage \(n\), then
\(Z_n^-\) is a known-zero region. Every interval removed in forming \(K_{n+1}^-\) satisfies
R36-A11', hence \(h=0\) a.e. there. This proves the induction step.
\(\square\)

Let

\[
K_\infty^-:=\bigcap_{n\ge0}K_n^-.
\]

Then

\[
\boxed{
|K_\infty^-|=0
\Longrightarrow
\ker L_{R,S,T_0}=\{0\}.
}
\tag{A11'.5}
\]

Contrapositively,

\[
\ker L_{R,S,T_0}\ne\{0\}
\Longrightarrow
|K_\infty^-|>0.
\]

No converse is claimed. A positive-measure residual is only an unexposed / multi-hit region;
it does not construct a kernel vector.

Status:

\[
\boxed{\text{folded preimage peeling}\quad\checkmark[M]\text{ (sufficiency only; no run yet).}}
\]

---

## 4. Status firewall

The odd-sector identification from R36-A9 remains

\[
\boxed{
U_-(\ker L_{R,S,T_0})
=
\ker(H_{T_0}E_A)\cap L^2_{\rm odd}(A).
}
\]

Hence triviality of \(\ker L\) kills only the **odd annihilator route**. It does not imply
full dense range, because R36-A1 requires triviality of the entire kernel, including the even
sector:

\[
\overline{\operatorname{Ran}(P_AH_{T_0})}=L^2(A)
\iff
\ker(H_{T_0}E_A)=\{0\}.
\]

Conversely, a nonzero odd kernel vector helps the annihilator route only if it also pairs
nontrivially with \(d_{R,S}\).

Current statuses after this repair:

| Item | Status |
|---|---|
| R36-A9 odd-sector unitary identification | ✓[M] |
| R36-A10 affine folded branch geometry | ✓[M] |
| R36-A11(old) image-based exposed-cell lemma | ×[M] |
| R36-A11' preimage-correct exposed-cell lemma | ✓[M] |
| folded preimage peeling | ✓[M] sufficiency only; not run |
| full R36-A kernel triviality | ?[O] |
| odd kernel triviality \(\ker L=?\{0\}\) | ?[O] |
| R36-B annihilator obstruction | ✓[M] conditional |
| R30-F | ?[O] |

## 5. Next node

Do **not** run a terminal-unspecified peeling. The active shift family and terminal admissibility
depend on \(T_0\). Before a general chamber analysis, establish the exact one-shift oracle in
the first P11 terminal chamber and use it as a regression theorem for any future peeling
implementation.

No statement about Object X, terminal transport, polar gauge, or RH is made here.
