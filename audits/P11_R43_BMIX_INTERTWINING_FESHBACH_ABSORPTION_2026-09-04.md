# P11 / R43 — BMIX intertwining defect and Feshbach absorption

**Date:** 2026-09-04  
**Scope:** R43 / B-METINC-GEO-BMIX only  
**Status:** local exact hardening results proved below; BMIX itself remains OPEN

## 0. Governance

This companion audit does **not** promote `B-METINC-GEO-BMIX`, `B-METINC-GEO`, `B-METINC`, `B-FLAGMOD`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, Object X, or RH.  It only sharpens the exact operator reduction of the fixed-terminal Feshbach mixing block.

The starting frozen definitions are the canonical P11 residual operator

\[
(R_Vf)(u)
=
\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Vf(u)
\otimes \mathsf Q_V(u)\eta_{p,k},
\]

with

\[
D_s=U_{s/2}-U_{-s/2},
\qquad
B_V=(I+R_V^*R_V)^{-1},
\]

and source-dependent martingale depth

\[
J_{p,V}(u)
=
\max\left\{0,
\left\lfloor\frac{2(V-|u|)_+}{\log p}\right\rfloor
\right\}.
\]

The previously isolated BMIX block is

\[
Q_BB_VQ_I,
\qquad
Q_I=1_{(-U,U)},
\quad Q_B=I-Q_I,
\quad X<U<V.
\]

## 1. Domain/codomain projection firewall

`R_V` does not act on one Hilbert space: its domain is the terminal source space and its codomain is the residual finite-adic field space.  Therefore the correct first-order defect uses two spatial projections.

Let

- `P:=Q_I` be multiplication by `1_{(-U,U)}` on the **domain** of `R_V`;
- `\widetilde P` be multiplication by the same indicator on the **residual codomain**;
- `Q:=I-P`, `\widetilde Q:=I-\widetilde P`.

Define the residual intertwining defect

\[
\boxed{
C_{V,U}:=R_VP-\widetilde P R_V.
}
\tag{BI1}
\]

This distinction is mandatory; writing `[R_V,P]` without identifying the codomain projection is type-incorrect.

### Proposition BI.1 — exact block form of the intertwining defect

One has

\[
C_{V,U}P=\widetilde Q R_VP,
\qquad
C_{V,U}Q=-\widetilde P R_VQ.
\tag{BI2}
\]

Hence relative to the decompositions

\[
\mathcal H_V=P\mathcal H_V\oplus Q\mathcal H_V,
\qquad
\mathcal K_V=\widetilde P\mathcal K_V\oplus\widetilde Q\mathcal K_V,
\]

`C_{V,U}` is purely off-diagonal and

\[
\boxed{
\|C_{V,U}\|
=
\max\{\|\widetilde Q R_VP\|,\|\widetilde P R_VQ\|\}.
}
\tag{BI3}
\]

**Proof.** Multiply (BI1) on the right by `P` and `Q`, use `P^2=P`, `PQ=0`, and split the codomain by `\widetilde P+\widetilde Q=I`.  The two resulting blocks have orthogonal domain and orthogonal range, so the norm is the maximum of their norms. ∎

## 2. Exact source commutator identity

Let

\[
A_V:=R_V^*R_V.
\]

Since

\[
C_{V,U}^*
=PR_V^*-R_V^*\widetilde P,
\]

a direct multiplication gives

\[
\boxed{
[A_V,P]
=R_V^*C_{V,U}-C_{V,U}^*R_V,
}
\tag{BI4}
\]

with commutator convention `[A,P]=AP-PA`.

Indeed,

\[
R_V^*C-C^*R_V
=R_V^*R_VP-R_V^*\widetilde P R_V
-PR_V^*R_V+R_V^*\widetilde P R_V
=A_VP-PA_V.
\]

The old crude consequence is

\[
\|[A_V,P]\|
\le 2\|R_V\|\,\|C_{V,U}\|.
\tag{BI5}
\]

The next section shows that this large factor `\|R_V\|` is unnecessary once the Feshbach resolvents already present in BMIX are retained.

## 3. Feshbach absorption removes the `2||R_V||` loss

Write

\[
B:=B_V=(I+A_V)^{-1}.
\]

Since `QP=0`,

\[
QBP=Q[B,P]P.
\]

Resolvent calculus gives

\[
[B,P]=-B[A_V,P]B.
\]

Insert (BI4):

\[
\boxed{
QBP
=-QBR_V^*C_{V,U}BP
+QBC_{V,U}^*R_VBP.
}
\tag{BI6}
\]

By polar decomposition / scalar functional calculus,

\[
\|R_VB\|
=
\|BR_V^*\|
=
\sup_{t\ge0}\frac{t}{1+t^2}
\le\frac12.
\tag{BI7}
\]

Therefore

\[
\begin{aligned}
\|QBP\|
&\le
\frac12\|C_{V,U}BP\|
+
\frac12\|C_{V,U}BQ\|\\
&\le
\|C_{V,U}B\|\\
&\le
\|C_{V,U}\|.
\end{aligned}
\tag{BI8}
\]

Thus:

\[
\boxed{
\|Q_BB_VQ_I\|
\le
\frac12\bigl(
\|C_{V,U}B_VQ_I\|
+
\|C_{V,U}B_VQ_B\|
\bigr)
\le
\|C_{V,U}B_V\|
\le
\|C_{V,U}\|.
}
\tag{BI9}
\]

### Status

`R43-BMIX-FESHBACH-ABSORPTION`: **✓[M] local exact operator theorem.**

This is strictly sharper structurally than first discarding both Feshbach factors and then using (BI5).  It does **not** prove that the right-hand side tends to zero.

## 4. Exact prime-power formula for the intertwining defect

Let `M_U` denote multiplication by `1_{(-U,U)}` on ambient `L^2(R)`.  Zero extension gives exactly

\[
E_VP=M_UE_V.
\]

The mark field `\mathsf Q_V(u)\eta_{p,k}` is a pointwise multiplier in the spatial variable, hence commutes with `\widetilde P`.  Consequently (BI1) becomes

\[
\boxed{
(C_{V,U}f)(u)
=
\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
\bigl([D_{k\log p},M_U]E_Vf\bigr)(u)
\otimes \mathsf Q_V(u)\eta_{p,k}.
}
\tag{BI10}
\]

This is an exact channel decomposition, not an estimate.

For the translation convention `(U_tg)(u)=g(u-t)`, one has

\[
([U_t,M_U]g)(u)
=
\bigl(1_{(-U,U)}(u-t)-1_{(-U,U)}(u)\bigr)g(u-t).
\tag{BI11}
\]

Hence each translation commutator is supported on the symmetric difference

\[
(-U,U)\,\triangle\,((-U,U)+t).
\]

For `D_s=U_{s/2}-U_{-s/2}`, the support of `[D_s,M_U]` lies in the union of the two corresponding boundary-crossing sets.

### Firewall

Support localization alone does **not** imply operator-norm smallness: whenever the crossing set is nonempty, a translation commutator can have norm of order one.  No decay of `\|C_{V,U}\|` is booked from (BI10)–(BI11).

## 5. Exact terminal dead layer from the martingale cutoff

A stronger local fact comes from the frozen source-dependent cutoff itself.

Let

\[
\delta:=V-U.
\]

For `u` in the outer terminal strip `U<|u|<V`,

\[
0<V-|u|<\delta.
\]

If

\[
\boxed{
0<\delta<\frac12\log2,
}
\tag{BI12}
\]

then for every prime `p\ge2`,

\[
\frac{2(V-|u|)}{\log p}
<
\frac{2\delta}{\log2}
<1,
\]

so

\[
J_{p,V}(u)=0
\]

for almost every `u` in that strip.  Therefore

\[
\mathsf Q_V(u)\eta_{p,k}=0
\]

for every `(p,k)`, and hence

\[
\boxed{
\widetilde Q R_V=0
\qquad
\text{whenever }0<V-U<\tfrac12\log2.
}
\tag{BI13}
\]

In particular,

\[
\boxed{
C_{V,U}P=0,
\qquad
C_{V,U}=-\widetilde P R_VQ
}
\tag{BI14}
\]

for such fine terminal steps.

### Status

`R43-RESIDUAL-DEAD-LAYER`: **✓[M] local exact frozen-definition theorem.**

This is one-sided: source vectors supported in the new outer strip may still be translated inward and produce residual output in `(-U,U)`.  Therefore (BI13) does **not** imply BMIX vanishing.

## 6. Exact martingale Gram kernel

For later quantitative work it is useful to record the covariance of the frozen residual marks.  Let

\[
q_{p,k;V}(u):=\mathsf Q_V(u)\eta_{p,k},
\qquad
J:=J_{p,V}(u),
\qquad
r:=\min\{k,\ell,J\}.
\]

Then direct summation of the martingale basis gives

\[
\boxed{
\langle q_{p,k;V}(u),q_{p,\ell;V}(u)\rangle
=
\begin{cases}
 p^{r-(k+\ell)/2}-p^{-(k+\ell)/2},&r\ge1,\\
 0,&r=0.
\end{cases}
}
\tag{BI15}
\]

In particular,

\[
0\le
\langle q_{p,k;V}(u),q_{p,\ell;V}(u)\rangle
\le
p^{-|k-\ell|/2},
\tag{BI16}
\]

and before cutoff

\[
\langle\eta_{p,k},\eta_{p,\ell}\rangle
=
p^{-|k-\ell|/2}-p^{-(k+\ell)/2}.
\tag{BI17}
\]

Thus the `k`-correlations inside one prime sector already have geometric off-diagonal decay.  This does not by itself control the sum over primes or the source-boundary operator norm.

### Status

`R43-RESIDUAL-MARK-GRAM`: **✓[M] local exact algebraic identity.**

## 7. What has and has not been gained

The old BMIX chain

```text
Q_B B_V Q_I
 -> [R_V^*R_V,Q_I]
 -> crude 2||R_V|| ||C_{V,U}||
```

can now be replaced by

```text
Q_B B_V Q_I
 -> exact Feshbach-absorbed defect
 -> ||C_{V,U} B_V||
 -> exact prime-power translation commutators.
```

For fine steps `V-U<log(2)/2`, the residual codomain has an exact dead outer layer and the defect becomes one-sided.

However:

1. `\|C_{V,U}\|` is not proved small;
2. shrinking support alone cannot give operator-norm decay;
3. the remaining one-sided term `\widetilde P R_VQ` may have order-one translation norm;
4. therefore `B-METINC-GEO-BMIX` remains OPEN;
5. the next quantitative target should preserve the `B_V` conditioning in `C_{V,U}B_V`, rather than immediately replace it by `\|C_{V,U}\|`.

This points to the conditioned quantity

\[
\boxed{
\mathfrak c_{U,V}^{\rm BMIX}:=\|C_{V,U}B_V\|
}
\tag{BI18}
\]

as a sharper sufficient BMIX majorant.

For a terminal partition with mesh below `log(2)/2`, the exact dead-layer theorem applies on every step.  No summability claim is made yet.

## 8. Live status after this audit

```text
B-METINC-GEO-BMIX [OPEN]
├─ R43-BMIX-FESHBACH-ABSORPTION ✓[M]  (local exact reduction)
├─ R43-RESIDUAL-DEAD-LAYER ✓[M]       (local fine-step theorem)
├─ R43-RESIDUAL-MARK-GRAM ✓[M]        (local exact algebra)
└─ conditioned BMIX decay/summability [OPEN]
```

All downstream project nodes remain OPEN.  No freeze and no project-level promotion is made.