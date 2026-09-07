# P11 / R43 — structured COND Schur-leakage reduction

**Date:** 2026-09-05  
**Status:** exact local reduction on the structured COND front; `B-METINC-COND` and Strong Terminal remain OPEN

## 0. Scope and governance firewall

Work at the post-PR-54 base

```text
434cd6bd49b66e49d4e8b556fd18687fe9887ffa
```

and retain the frozen notation

\[
M=R_V\iota,
\qquad
S=R_VP_{\mathcal N},
\qquad
\Phi_S=SS^*(I+SS^*)^{-1},
\qquad
C=(I-\Pi_{U,V})M,
\]

with

\[
\Pi_{U,V}M=\jmath_{U,V}R_U,
\qquad
M^*M-R_U^*R_U=C^*C.
\]

Thus

\[
\boxed{
K_{U,V}^{\rm Schur}
:=M^*(I+SS^*)^{-1}M-R_U^*R_U
=C^*C-M^*\Phi_SM.
}
\tag{SL1}
\]

The structured old-source vector remains the pre-no-go vector

\[
\boxed{
v_U(f)=H_U^*E_{X,U}f.
}
\tag{SL2}
\]

This note proves only exact support/reduction statements and a sufficient quantitative target for the **negative scalar part of the Schur sign operator**. It does **not** prove a decay estimate, a sign theorem for structured `COND`, a telescoping theorem, Strong Terminal/C6, Object X, or RH.

A crucial firewall is that a scalar estimate on

\[
(-\langle v_U,K_{U,V}^{\rm Schur}v_U\rangle)_+
\]

is not by itself an estimate on

\[
\Delta s_{\rm cond}^{U,V}(f)
=\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle.
\]

Indeed block inversion gives a nonlinear resolvent dependence on `K_{U,V}^{\rm Schur}`. No such implication is booked below.

---

## 1. Exact two-species structure of `C`

The frozen residual map is

\[
(R_Tx)(u)
=\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Tx(u)\otimes\mathsf Q_T(u)\eta_{p,k}.
\tag{SL3}
\]

For `U<V`, old-source zero extension satisfies `E_V\iota=E_U`, and on `|u|<U` the residual mark projections are nested. Hence the complement of `\Pi_{U,V}` has two orthogonal species:

1. **old spatial window / newly resolved martingale details** on `|u|<U`;
2. **new spatial residual strip** on `U<|u|<V`.

More explicitly, for `x\in\mathcal H_U`, the first component is

\[
\mathbf 1_{|u|<U}
\sum_{p,k}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Ux(u)
\otimes
\bigl(\mathsf Q_V(u)-\mathsf Q_U(u)\bigr)\eta_{p,k},
\tag{SL4}
\]

while the second is

\[
\mathbf 1_{U<|u|<V}
\sum_{p,k}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Ux(u)
\otimes
\mathsf Q_V(u)\eta_{p,k}.
\tag{SL5}
\]

They are orthogonal because the spatial supports are disjoint; within the old window the retained and newly resolved martingale levels are orthogonal by construction of `\Pi_{U,V}`.

Consequently

\[
\boxed{
Cx=0
\iff
C_{\rm fine}x=0
\text{ and }
C_{\rm strip}x=0.
}
\tag{SL6}
\]

In particular, for the structured vector `v_U`, a strip-only argument cannot characterize `Cv_U=0`: it must also control the old-window/new-fine component.

### Local booking

```text
R43-COND-C-TWO-SPECIES-RESIDUAL-DECOMPOSITION ✓[M]
```

This is an exact unpacking of the already frozen residual nesting, not a new sign theorem.

---

## 2. Exact saturated-leakage identity

For every admissible old-source vector `x`, put

\[
\mathcal L_{U,V}(x)
:=\langle Mx,\Phi_SMx\rangle.
\tag{SL7}
\]

Using the push-through identity

\[
S^*(I+SS^*)^{-1}=(I+S^*S)^{-1}S^*,
\]

we obtain

\[
\boxed{
\mathcal L_{U,V}(x)
=\langle S^*Mx,(I+S^*S)^{-1}S^*Mx\rangle
=\|(I+S^*S)^{-1/2}S^*Mx\|^2.
}
\tag{SL8}
\]

This is the naturally **saturated** nuisance leakage. It is preferable to replacing `\Phi_S` by a crude factor involving `\|S\|`, since `\Phi_S` itself stays bounded by the target projection even when `\|S\|` grows.

Functional calculus also gives

\[
0\preceq\Phi_S\preceq
P_{\overline{\operatorname{Ran}S}}\preceq I,
\]

hence

\[
\boxed{
\mathcal L_{U,V}(x)
\le
\|P_{\overline{\operatorname{Ran}S}}Mx\|^2
\le\|Mx\|^2.
}
\tag{SL9}
\]

The still stronger but potentially over-demanding sufficient bound

\[
\mathcal L_{U,V}(x)\le\|S^*Mx\|^2
\tag{SL10}
\]

follows from `(I+S^*S)^{-1}\preceq I`.

---

## 3. Negative Schur defect is controlled entirely by saturated leakage

From (SL1), for every `x`,

\[
\langle x,K_{U,V}^{\rm Schur}x\rangle
=\|Cx\|^2-\mathcal L_{U,V}(x).
\tag{SL11}
\]

Since `\|Cx\|^2\ge0`, the elementary scalar inequality `(b-a)_+\le b` for `a,b\ge0` yields

\[
\boxed{
\bigl(-\langle x,K_{U,V}^{\rm Schur}x\rangle\bigr)_+
\le
\mathcal L_{U,V}(x)
=\|(I+S^*S)^{-1/2}S^*Mx\|^2.
}
\tag{SL12}
\]

Therefore, on the actual structured vector,

\[
\boxed{
\bigl(-\langle v_U,K_{U,V}^{\rm Schur}v_U\rangle\bigr)_+
\le
\|(I+S^*S)^{-1/2}S^*Mv_U\|^2.
}
\tag{SL13}
\]

This is stronger as a research reduction than separately trying to lower-bound `\|Cv_U\|`: for an **upper bound on the negative part only**, the positive residual increment `\|Cv_U\|^2` can be discarded. It remains essential for an actual sign theorem or for excluding kernel witnesses.

### Local booking

```text
R43-COND-SCHUR-NEGATIVE-PART-LEAKAGE-BOUND ✓[M]
```

No decay rate is included in this booking.

---

## 4. Source-side normal-equation form of the leakage

Since `S=R_VP_{\mathcal N}` and `M=R_V\iota`, with `P_{\mathcal N}` orthogonal,

\[
\boxed{
S^*Mx
=P_{\mathcal N}R_V^*R_V\iota x
=P_{\mathcal N}A_V\iota x.
}
\tag{SL14}
\]

Thus the unregularized nuisance leakage of the structured vector is exactly

\[
\boxed{
S^*Mv_U(f)
=P_{\mathcal N}A_V\iota H_U^*E_{X,U}f.
}
\tag{SL15}
\]

In source space this lies entirely in the new-source summand `\mathcal N`. The next quantitative problem is therefore an off-diagonal Gram/normal-equation estimate, not merely a target-strip support estimate.

The saturated quantity actually needed by (SL13) is

\[
\boxed{
\left\|
(I+S^*S)^{-1/2}
P_{\mathcal N}A_V\iota H_U^*E_{X,U}f
\right\|.
}
\tag{SL16}
\]

This formulation keeps the regularization that is lost in the crude `\|S^*Mv_U\|` bound.

---

## 5. Exact structured-witness test

The arbitrary-source kernel witness mechanism can occur on the structured range at a pair `(U,V)` **if and only if** there exists source data `f` with `v_U(f)\ne0` such that simultaneously

\[
C_{\rm fine}v_U(f)=0,
\tag{SL17}
\]

\[
C_{\rm strip}v_U(f)=0,
\tag{SL18}
\]

and

\[
P_{\mathcal N}A_V\iota v_U(f)\ne0.
\tag{SL19}
\]

Equivalently, using (SL2),

\[
H_U^*E_{X,U}f
\in
\ker C
\setminus
\ker(P_{\mathcal N}A_V\iota).
\tag{SL20}
\]

This is only a criterion. The intersection in (SL20) is **not** proved empty or nonempty here. Therefore the arbitrary-source no-go still does not transfer to the structured range.

---

## 6. Quantitative reserve target

For any `\eta>0`, a sufficient estimate for the desired structured Schur-defect reserve is

\[
\boxed{
\|(I+S^*S)^{-1/2}S^*Mv_U(f)\|
\le A_{X,f}\,e^{-(2+\eta/2)U}
}
\tag{SL21}
\]

along the chosen cofinal terminal chain. Then (SL13) gives

\[
\boxed{
\bigl(-\langle v_U,K_{U,V}^{\rm Schur}v_U\rangle\bigr)_+
\le A_{X,f}^2e^{-(4+\eta)U}.
}
\tag{SL22}
\]

The previously proved one-sided step-floor reserve theorem shows why the exponent `4+\eta` is summability-compatible on chains satisfying

\[
h_j\ge ce^{-4U_j}.
\]

However, **(SL21) itself is OPEN**, and no canonical-COND telescoping conclusion is drawn from (SL22) without a separate resolvent-transfer argument.

A stronger but not necessary target would be

\[
\|S^*Mv_U(f)\|
\lesssim_{X,f}e^{-(2+\eta/2)U}.
\tag{SL23}
\]

The saturated target (SL21) should be attacked first.

---

## 7. Adversarial checks and failure modes

1. **Strip-only fallacy.** `C` contains old-window/new-fine martingale energy as well as new-strip energy. A proof controlling only (SL5) cannot characterize `Cv_U`.
2. **Unsaturated-`S` fallacy.** Since `\|S\|` may grow cofinally, inserting `\|S\|` before exploiting `(I+S^*S)^{-1/2}` can destroy the useful scale. The exact object is (SL16).
3. **Scalar-Schur versus inverse fallacy.** A bound on (SL13) does not automatically bound the structured inverse difference `\Delta s_{\rm cond}`. A separate resolvent-transfer estimate is required.
4. **Witness-transfer fallacy.** The known arbitrary-source witness proves nothing about the nonemptiness of (SL20).
5. **No hidden rate.** Neither `e^{-(2+\eta/2)U}` nor `e^{-(4+\eta)U}` is proved here; they are explicit sufficient targets only.

---

## 8. Status ledger

New theorem-level local bookings:

```text
R43-COND-C-TWO-SPECIES-RESIDUAL-DECOMPOSITION ✓[M]
R43-COND-SCHUR-NEGATIVE-PART-LEAKAGE-BOUND    ✓[M]
```

Retained OPEN nodes:

```text
R43-COND-STRUCTURED-WITNESS-EXCLUSION ?[O]
R43-COND-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
R43-COND-EPSILON-RELAXED-TELESCOPE ?[O]
R43-COND-PARTITION-SELECTIVE-PSD ?[O]
B-METINC-COND ?[O]
B-METINC ?[O]
B-FLAGMOD / B-FLAGDYN ?[O]
B-FLAGTIGHT ?[O]
B-SIGN / B-ORIENT ?[O]
Strong Terminal / C6 ?[O]
Object X / RH ?[O]
```

The existing negative arbitrary-source results and the step-floor results are unchanged.

## 9. Next attack

The preferred next object is the saturated source-strip leakage

\[
\mathscr L_{U,V}(f)
:=
(I+S^*S)^{-1/2}
P_{\mathcal N}A_V\iota H_U^*E_{X,U}f.
\]

The next proof attempt should expand this in the fixed-source prime-power shells forced by `H_U^*E_{X,U}f`, retain the regularizing factor, and seek an `m`-tail before terminal summation. In parallel, (SL17)–(SL19) provide the exact adversarial test for whether the old interval-kernel witness can survive the structured range.
