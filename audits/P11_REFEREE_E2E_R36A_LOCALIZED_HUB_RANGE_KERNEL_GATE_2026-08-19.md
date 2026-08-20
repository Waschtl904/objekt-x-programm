# P11 End-to-End Referee R36-A — Localized hub range: canonical consolidated status

Date: 2026-08-19; consolidated 2026-08-20

> **SUPERSESSION / CANONICAL-STATUS NOTICE.**  The historical version of this audit at
> commit `1d1b530c7d707dd17a6d656574abae24ac29ee5f` contained the original
> R36-A11 folded exposed-cell lemma with the image-space hypothesis `B(I) ⊂ Z` and marked
> that statement `✓[M]`.  That statement is **not type-correct**: `B(I)` lies in the
> observation variable `u`, whereas the known-zero region `Z ⊂ (R,S)` lies in the source
> variable `x` on which `h` is defined.  Therefore the original statement is now
> `R36-A11(old) ×[M]`.
>
> The canonical replacement is
> `audits/P11_REFEREE_E2E_R36A11_PREIMAGE_REPAIR_2026-08-20.md`, introduced by commit
> `012df409ef73577c141d8dea5e3704638f071a62`.  It proves the preimage-correct
> `R36-A11' ✓[M]` and the repaired folded peeling in the sufficiency direction.
>
> The full pre-consolidation historical text of this file remains permanently recoverable at
> commit `1d1b530c7d707dd17a6d656574abae24ac29ee5f`.  This consolidated file is the
> current status entry point and must be preferred over the historical A11 line.

## 0. Dependency audit of the superseded A11

The old A11 was introduced in commit
`1d1b530c7d707dd17a6d656574abae24ac29ee5f`.  No further commit landed on `main`
between that commit and the targeted repair `012df409ef73577c141d8dea5e3704638f071a62`.
Consequently no later repository audit could have newly used A11(old) before the repair.
The only affected downstream item was the folded peeling scheme defined in the same historical
R36-A audit.  No concrete peeling run and no kernel-triviality theorem had been derived from it.

Hence the correction is local:

- R36-A9 remains `✓[M]`;
- R36-A10 remains `✓[M]`;
- R36-A11(old) is `×[M]`;
- R36-A11' is `✓[M]`;
- the old image-test folded peeling is retracted;
- the repaired preimage folded peeling is `✓[M]` in the sufficiency direction only;
- no proved R36-A, R36-B, or R30-F conclusion is retracted.

---

## 1. Target and unchanged first gate

Fix

\[
0<R<S<T_0,
\qquad
A:=(-S,-R)\cup(R,S),
\]

and

\[
T_A:=P_AH_{T_0}:L^2(-T_0,T_0)\to L^2(A).
\]

The exact adjoint identity remains

\[
T_A^*=H_{T_0}^*E_A=-H_{T_0}E_A,
\]

and therefore

\[
\boxed{
\overline{\operatorname{Ran}(P_AH_{T_0})}=L^2(A)
\iff
\ker(H_{T_0}E_A)=\{0\}.
}
\]

Status: `R36-A1 ✓[M]`.

The density firewall is unchanged: triviality of the full kernel yields dense range only; it
does not imply that the concrete target lies in the actual range.

---

## 2. Concrete hub convention

The canonical shift and weight conventions are

\[
\boxed{
\tau_{p,k}=\frac{k\log p}{2},
\qquad
c_{p,k}=\sqrt{\log p}\,p^{-3k/4},
\qquad
\mathcal P_{T_0}=\{(p,k):\tau_{p,k}\le T_0\}.
}
\]

For `y ∈ L^2(A)`, the kernel equation is

\[
\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\bigl[(E_Ay)(u-\tau_{p,k})-(E_Ay)(u+\tau_{p,k})\bigr]=0
\]

for almost every `u ∈ (-T_0,T_0)`.

Status: `R36-A2 ✓[M]`.

The historical full-line exposed-cell lemma, outer support constraint, and full-annulus peeling
remain as proved in the immutable historical audit:

- R36-A3 full-line known-zero exposed-cell lemma: `✓[M]`;
- R36-A4 outer support constraint via `τ_max`: `✓[M]`;
- R36-A5/A6 full-annulus peeling correctness and sufficiency: `✓[M]`.

These statements are logically separate from the superseded folded A11.

---

## 3. Parity and odd-sector reduction

Let `(Jf)(u)=f(-u)`.  The anticommutation identity is

\[
\boxed{H_{T_0}J=-JH_{T_0}.}
\]

Thus `H_{T_0}` flips parity:

\[
H_{T_0}:\text{odd}\to\text{even},
\qquad
H_{T_0}:\text{even}\to\text{odd}.
\]

Status: `R36-A7 ✓[M]`.

The concrete target `d_{R,S}` is odd, so every even annihilator kernel vector pairs to zero
with it.  Only the odd kernel can feed the simple R36-B annihilator test.

Status: `R36-A8 ✓[M]`.

Define

\[
(U_-h)(x)=\frac1{\sqrt2}\operatorname{sgn}(x)h(|x|)
\mathbf1_{\{R<|x|<S\}}.
\]

Then `U_-:L^2(R,S)→L^2_odd(A)` is unitary and

\[
\boxed{
U_-(\ker L_{R,S,T_0})
=
\ker(H_{T_0}E_A)\cap L^2_{\rm odd}(A).
}
\]

Status: `R36-A9 ✓[M]`.

The folded half-annulus operator is

\[
(L_{R,S,T_0}h)(u)
=\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\Bigl[
\operatorname{sgn}(u-\tau_{p,k})\mathbf1_{(R,S)}(|u-\tau_{p,k}|)
 h(|u-\tau_{p,k}|)
-\mathbf1_{(R,S)}(u+\tau_{p,k})h(u+\tau_{p,k})
\Bigr].
\]

The corrected branch geometry of R36-A10 remains canonical and `✓[M]`.

---

## 4. Historical R36-A11(old) — superseded and false as stated

The historical A11 used a source interval `I`, an output interval `J=B_*(I)`, and a
known-zero region `Z⊂(R,S)`, but required for competitors an image condition of the form

\[
B(I)\subset Z.
\]

This compares subsets of different typed spaces and does not imply that the competing source
preimages at a fixed `u∈J` lie in the known-zero region.  Competitors may arise from source
points outside `I`.  Therefore its proof does not establish the claim.

\[
\boxed{\text{R36-A11(old)}\quad\times[M].}
\]

The folded peeling scheme built directly on that image test is likewise superseded.

\[
\boxed{\text{old image-test folded peeling}\quad\times[M]\text{ as a proof scheme}.}
\]

This is a correction of an invalid proof, not a theorem showing the opposite exposed-cell
conclusion in every configuration.

---

## 5. Canonical R36-A11' — preimage-correct exposed cell

For each active shift `τ`, use terminal-independent injective affine branch pieces

\[
B_{\tau,+}(x)=x+\tau,
\qquad w_{\tau,+}=+c_\tau,
\]

\[
B_{\tau,->}(x)=x-\tau
\quad(x>\tau),
\qquad w_{\tau,->}=-c_\tau,
\]

\[
B_{\tau,-<}(x)=\tau-x
\quad(x<\tau),
\qquad w_{\tau,-<}=-c_\tau.
\]

After the R36-A10 cell decomposition, write the operator almost everywhere as

\[
(Lh)(u)=
\sum_{\beta:\,u\in B_\beta(D_\beta)}
 w_\beta h(B_\beta^{-1}(u)).
\]

Let `Z⊂(R,S)` be a measurable known-zero region for `h`, let `β_*` be a distinguished branch,
and let `I⊂D_{β_*}` be a nonempty open interval inside one affine branch cell.  Put

\[
J=B_{\beta_*}(I)\subset(0,T_0).
\]

The correct exposed-cell hypothesis is

\[
\boxed{
B_\beta^{-1}\bigl(J\cap B_\beta(D_\beta)\bigr)
\subset Z
\quad\text{modulo null sets}
}
\]

for every competing branch `β≠β_*`.  Then

\[
\boxed{h=0\quad\text{a.e. on }I.}
\]

Status:

\[
\boxed{\text{R36-A11'}\quad\checkmark[M].}
\]

Canonical source: `P11_REFEREE_E2E_R36A11_PREIMAGE_REPAIR_2026-08-20.md`, commit
`012df409ef73577c141d8dea5e3704638f071a62`.

---

## 6. Canonical folded preimage peeling

Set

\[
K_0^-=(R,S),
\qquad
Z_n^-=(R,S)\setminus K_n^-.
\]

At stage `n`, remove only intervals satisfying the R36-A11' preimage condition with `Z_n^-`.
The induction gives, for every `h∈ker L`,

\[
h=0\quad\text{a.e. on }(R,S)\setminus K_n^-.
\]

Therefore

\[
\boxed{
|K_\infty^-|=0
\Longrightarrow
\ker L_{R,S,T_0}=\{0\}.
}
\]

No converse is claimed.  A positive-measure residual is only an unexposed/multi-hit region and
does not itself construct a kernel vector.

Status:

\[
\boxed{\text{folded preimage peeling}\quad\checkmark[M]\text{ (sufficiency only).}}
\]

---

## 7. A13 oracle now on main

The first-terminal-chamber odd kernel is no longer globally open.  The canonical A13 audit is
`P11_REFEREE_E2E_R36A13_ONE_SHIFT_ODD_KERNEL_ORACLE_2026-08-20.md`, with the scope firewall
`P11_REFEREE_E2E_R36A13_SCOPE_NO_OVERLAP_FIREWALL_2026-08-20.md`.

For

\[
\tau=\tau_{2,1}=\frac{\log2}{2},
\qquad
\frac{\log2}{2}\le T_0<\frac{\log3}{2},
\]

one has

\[
\boxed{
\ker L_{R,S,T_0}\ne\{0\}
\iff
R<\frac{\log2}{2}<S.
}
\]

In the nontrivial middle case

\[
0<R<\tau<S<T_0<2\tau,
\qquad
r=\min\{S-\tau,\tau-R,2\tau-T_0\},
\]

and the kernel consists exactly of functions supported in `(τ-r,τ+r)` and antisymmetric about
`τ`; it is infinite-dimensional.  The regression firewall is

\[
\boxed{C_{T_0}:=(\tau-r,\tau+r)\subseteq K_\infty^-\quad\text{modulo null sets}.}
\]

The theorem is a **one-shift no-overlap** theorem, not a global one-shift theorem.  In wider
annuli with `S-R>2τ`, a translation relation `h(x+2τ)=h(x)` can arise and A13's classification
must not be extrapolated.

Status: `R36-A13 ✓[M]` in its stated scope.

---

## 8. R36-B, full-range firewall, and current route map

The conditional annihilator lemma remains:

if

\[
0\ne y\in\ker(H_{T_0}E_A),
\qquad
\langle y,d_{R,S}\rangle\ne0,
\]

then

\[
P_A\Sigma_{T_0}j_{R,S}\ne d_{R,S}.
\]

Status: `R36-B ✓[M] conditional`.

Odd-kernel triviality kills only the odd annihilator route.  It does **not** imply the full
dense-range criterion, because R36-A1 needs triviality of the entire kernel, including the even
sector.

### Canonical status table

| Item | Current status |
|---|---|
| R36-A1 adjoint identity / dense-range equivalence | ✓[M] |
| R36-A2 explicit finite translation kernel equation | ✓[M] |
| R36-A3 full-line known-zero exposed-cell lemma | ✓[M] |
| R36-A4 outer support constraint | ✓[M] |
| R36-A5/A6 full-annulus peeling sufficiency | ✓[M] |
| R36-A7 anticommutation and parity flip | ✓[M] |
| R36-A8 only odd kernel can pair with odd `d_{R,S}` | ✓[M] |
| R36-A9 unitary odd-sector reduction | ✓[M] |
| R36-A10 corrected folded branch geometry | ✓[M] |
| **R36-A11(old) image-test exposed-cell lemma** | **×[M]** |
| **R36-A11' preimage-correct exposed-cell lemma** | **✓[M]** |
| old image-test folded peeling | ×[M] as proof scheme |
| repaired folded preimage peeling | ✓[M] sufficiency only |
| R36-A13 first-chamber/no-overlap odd-kernel oracle | ✓[M] in scope |
| full R36-A kernel triviality | ?[O] |
| R36-B annihilator obstruction | ✓[M] conditional |
| R30-F | ?[O] |

---

## 9. Next node

The next mathematical node is **not** another unscoped peeling run.  A13 supplies an exact
odd-kernel oracle.  The next question is whether this exact kernel detects the concrete defect
`d_{R,S}` and whether the resulting nonorthogonality feeds the mismatch theorem through a fully
written adjunction step.

That work belongs in a separate A13c-style audit and must keep three levels distinct:

1. exact structure of the odd kernel (A13);
2. nonorthogonality of that kernel to `d_{R,S}`;
3. the adjunction/range implication leading, if proved, to a concrete mismatch statement.

No statement here proves R30-F, Object X, terminal transport, polar gauge, or RH.
