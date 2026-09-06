# P11 / R43 — reverse reflection audit and common-mode firewall

**Date:** 2026-09-06  
**Status:** exact/local reflection reduction on top of PR #80; reverse-normal decay remains OPEN  
**Exact parent head:** `645d2bafe3c0f74fbfc769d4958ecf93316ae165`  
**Parent PR:** #80 — `R43: shellwise collar refinement and common-mode obstruction`

## 0. Purpose and correction

PR #80 proves that the universal old-graph collar route is sharp at the scale

\[
F_U(r)=\|\chi_{U,r}x_{\rm rev}\|^2\lesssim r/U,
\]

and that this gives only `O(1)` weighted occupancy on a dyadic step `V-U\asymp U`.  The normalized constant residual-difference mode saturates the universal `r/U` scale.

A natural next proposal was therefore:

1. identify the reflection parity of the fixed source normal `\varepsilon_R`;
2. propagate that parity through
   \[
   f_{\rm rev}
   \xrightarrow{E_{R,U}}
   E_{R,U}f_{\rm rev}
   \xrightarrow{H_U^*}
   v_U
   \xrightarrow{\mathcal Q_{U,V}}
   x_{\rm rev};
   \]
3. hope that `x_rev` is odd, hence orthogonal to the constant/common mode;
4. possibly exploit opposite signs on the two new-strip sides in the exact Schur/least-squares problem.

The definitions show that this proposed parity mechanism has the **opposite** outcome.

The source geometry used by R40--R42 is already the **odd source sector**.  Consequently the canonical reverse source is odd, the antisymmetric half-shift hub flips it to an **even** target vector, and the geometric-mean resolvent preserves that even parity.  Thus the actual reverse transported vector lies in the same reflection sector as constants.

Moreover, the finite-window hub does not have an exact mean-zero identity on odd sources: terminal half-shifts can create a nonzero constant Fourier coefficient.  Finally, the unique Schur least-squares correction is also even when the input is even, so there is no parity-forced opposite-sign cancellation between the two spatial strip sides.

This note records those facts and closes only the **parity/common-mode shortcut**.  It does **not** prove that the actual canonical `x_rev` has a nonzero constant component.  The exact Schur/least-squares correlation route remains open.

No reverse-normal stretch decay, FD23-UNIF, FLAGDYN/TIGHT, Strong Terminal/C6, Object X, or RH statement is claimed.

---

## 1. Reflection notation

For every symmetric interval `(-T,T)` define the unitary involution

\[
(J_T h)(u):=h(-u).
\tag{RF1}
\]

On the ambient line write `J_\infty` for the same reflection.

For zero extension and restriction between symmetric intervals,

\[
E_{R,U}J_R=J_UE_{R,U},
\qquad
P_UJ_\infty=J_UP_U.
\tag{RF2}
\]

For the frozen translation convention, with

\[
D_s=U_{s/2}-U_{-s/2},
\]

reflection reverses the translation:

\[
J_\infty U_tJ_\infty=U_{-t}.
\]

Hence

\[
\boxed{
J_\infty D_sJ_\infty=-D_s.
}
\tag{RF3}
\]

For

\[
K_{p,k;T}=P_TD_{k\log p}E_T,
\]

(RF2)--(RF3) give

\[
\boxed{
J_TK_{p,k;T}J_T=-K_{p,k;T}.
}
\tag{RF4}
\]

Thus every finite-window half-shift difference flips reflection parity.

---

## 2. The R40--R42 source geometry is odd

The relevant source parity is not inferred from a naive interpretation of `\beta_R^{(0)}` as an even point-evaluation functional.

The canonical sources themselves fix the sector:

- R40 defines
  \[
  A_X(U)=A_{T_0,U}^{X,-}
  \]
  as the **baseline-whitened odd relative metric**.
- R40's recovery construction explicitly chooses fixed **smooth odd** vectors `f_0,f_1`.
- R41 chooses a smooth odd `g_0` with
  \[
  \widehat\beta_X^{(0)}(g_0)=1,
  \]
  and states that the first two odd jet functionals are represented on smooth odd sources by the nonproportional kernels `I_0,I_1`.
- R42 gives the intrinsic formula
  \[
  \gamma_X
  =
  \sup_{0\ne f\in\mathcal K_{X,X}^{-},\ \beta_X^{(0)}(f)=0}
  \frac{|\beta_X^{(1)}(f)|^2}{\mathfrak c_{\Gamma,X}[f]}.
  \]
- R42 defines `\varepsilon_R` as the unit Riesz normal of `\beta_R^{(0)}` in the fixed source graph Hilbert space.

Thus the underlying fixed source vector space containing `\varepsilon_R` is the odd source space.  In ambient reflection language,

\[
\boxed{
J_R\varepsilon_R=-\varepsilon_R.
}
\tag{RF5}
\]

This is not a separate sign choice attached to the phase convention for the Riesz vector: every vector in the underlying `(-)` source sector has this parity.

### Consequence for the conditioning square root

PR #68 defines

\[
f_{R;U,V}^{\rm rev}
=(G_{R,\mathrm{cond}}^{U,V})^{-1/2}\varepsilon_R.
\tag{RF6}
\]

The operator acts on the same fixed odd source Hilbert space.  Therefore

\[
\boxed{
J_Rf_{R;U,V}^{\rm rev}=-f_{R;U,V}^{\rm rev}.
}
\tag{RF7}
\]

No separate ambient commutation theorem for `G_{R,cond}` is required to obtain RF7.  Restricted to the odd source space, reflection is simply `-I`, so every source-space operator commutes with that restricted reflection trivially.

### Local booking

```text
R43-COND-REVERSE-SOURCE-ODD-SECTOR ✓[M]_local
```

---

## 3. The hub flips the reverse source to the even target sector

PR #56 proves

\[
H_U^*
=-H_U
\]

and, for a fixed source datum,

\[
v_U(f)=H_U^*E_{R,U}f.
\tag{RF8}
\]

Because the hub is a real linear combination of the operators `K_{p,k;U}`, RF4 implies

\[
\boxed{
J_UH_U^*J_U=-H_U^*.
}
\tag{RF9}
\]

Apply RF9 to the odd reverse source RF7.  By RF2,

\[
J_UE_{R,U}f_{\rm rev}
=-E_{R,U}f_{\rm rev}.
\]

Therefore

\[
\begin{aligned}
J_Uv_U(f_{\rm rev})
&=J_UH_U^*E_{R,U}f_{\rm rev}\\
&=-H_U^*J_UE_{R,U}f_{\rm rev}\\
&=H_U^*E_{R,U}f_{\rm rev}.
\end{aligned}
\]

Hence

\[
\boxed{
J_Uv_U(f_{\rm rev})=v_U(f_{\rm rev}).
}
\tag{RF10}
\]

The reverse hub vector is **even**, not odd.

### Local booking

```text
R43-COND-REVERSE-HUB-EVEN-PARITY ✓[M]_local
```

---

## 4. Reflection symmetry of the residual normal operator

Use the PR #56 full-rest factorization

\[
A_T:=R_T^*R_T
=\sum_p\sum_{a\ge0}T_{p,a;T}^*T_{p,a;T},
\tag{RF11}
\]

where

\[
T_{p,a;T}
=
\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,T}}
\sum_{k\ge a+1}p^{-3k/4}K_{p,k;T}.
\tag{RF12}
\]

PR #61 records, up to boundary-null sets,

\[
\boxed{
\Omega_{p,a,T}
=
\{u:|u|+(a+1)a_p\le T\},
\qquad a_p=\tfrac12\log p.
}
\tag{RF13}
\]

Thus `\Omega_{p,a,T}` is reflection symmetric, and multiplication by its indicator commutes with `J_T`.

Combining this with RF4,

\[
\boxed{
J_TT_{p,a;T}J_T=-T_{p,a;T}.
}
\tag{RF14}
\]

Consequently each positive row square commutes with reflection:

\[
J_TT_{p,a;T}^*T_{p,a;T}J_T
=T_{p,a;T}^*T_{p,a;T}.
\]

Summing the positive factorization gives

\[
\boxed{
J_TA_TJ_T=A_T.
}
\tag{RF15}
\]

Therefore

\[
\mathscr A_T:=I+A_T
\]

and every bounded Borel function of `\mathscr A_T` commute with `J_T`.  In particular

\[
\boxed{
J_TB_TJ_T=B_T,
\qquad
B_T=(I+R_T^*R_T)^{-1}.
}
\tag{RF16}
\]

### Local booking

```text
R43-COND-RESIDUAL-NORMAL-REFLECTION-SYMMETRY ✓[M]_local
```

---

## 5. Reflection symmetry of the compressed resolvent and geometric mean

Let

\[
\iota=E_{U,V}:L^2(-U,U)\to L^2(-V,V).
\]

Symmetric zero extension intertwines reflections:

\[
\iota J_U=J_V\iota,
\qquad
J_U\iota^*=\iota^*J_V.
\tag{RF17}
\]

For

\[
\widetilde B_{U,V}:=\iota^*B_V\iota,
\]

RF16--RF17 give

\[
\boxed{
J_U\widetilde B_{U,V}J_U=\widetilde B_{U,V}.
}
\tag{RF18}
\]

PR #57 defines

\[
\mathcal Q_{U,V}:=B_U\#\widetilde B_{U,V}.
\tag{RF19}
\]

The positive operator geometric mean is equivariant under unitary conjugation:

\[
J(A\#B)J=(JAJ)\#(JBJ).
\tag{RF20}
\]

Applying RF16 and RF18,

\[
\boxed{
J_U\mathcal Q_{U,V}J_U=\mathcal Q_{U,V}.
}
\tag{RF21}
\]

Thus the geometric-mean transport preserves target reflection parity.

### Local booking

```text
R43-COND-GEOMEAN-REFLECTION-COMPATIBILITY ✓[M]_local
```

---

## 6. Exact parity of the transported reverse-normal vector

PR #68 defines

\[
x_{R;U,V}^{\rm rev}
=\mathcal Q_{U,V}H_U^*E_{R,U}f_{R;U,V}^{\rm rev}.
\tag{RF22}
\]

RF10 says the vector entering `\mathcal Q` is even, and RF21 says `\mathcal Q` preserves parity.  Therefore

\[
\boxed{
J_Ux_{R;U,V}^{\rm rev}
=x_{R;U,V}^{\rm rev}.
}
\tag{RF23}
\]

This is the opposite of the initially proposed parity mechanism.

The normalized constant profile

\[
x_{\rm const}(u)=(2U)^{-1/2}
\]

is also even.  Hence reflection parity alone does **not** exclude the common-mode obstruction identified in PR #80.

### Firewall

RF23 does **not** assert

\[
\langle x_{R;U,V}^{\rm rev},1\rangle\ne0.
\]

It says only that parity supplies no orthogonality to constants.

### Route-status booking

```text
R43-COND-REVERSE-PARITY-COMMON-MODE-ELIMINATION ×[M]_neg,local
```

This marks failure of the proposed **parity route**, not failure of common-mode elimination by some other special identity.

---

## 7. The finite-window hub is not mean-zero on odd sources

One might still hope for an independent identity

\[
\langle 1,H_U^*E_{R,U}f\rangle=0
\quad\text{for every odd }f.
\tag{RF24?}
\]

This is false in general because the finite terminal window truncates the two translated copies differently.

Take an odd `g` supported in `[-R,R]`.  For a half-shift magnitude `a\in[0,U]`, consider

\[
D_{2a}g=U_ag-U_{-a}g.
\]

With the convention `(U_ag)(x)=g(x-a)`, direct change of variables gives

\[
\int_{-U}^{U}D_{2a}g(x)\,dx
=
\int_{-U-a}^{U-a}g(t)\,dt
-
\int_{-U+a}^{U+a}g(t)\,dt.
\tag{RF25}
\]

If

\[
a\le U-R,
\]

both intervals contain the whole support and both integrals vanish because `g` is odd.  Thus

\[
\int_{-U}^{U}D_{2a}g=0.
\tag{RF26}
\]

If instead

\[
U-R<a\le U,
\]

put `b=U-a\in[0,R)`.  Intersecting with the support and using oddness yields

\[
\begin{aligned}
\int_{-U}^{U}D_{2a}g
&=\int_{-R}^{b}g(t)\,dt-\int_{-b}^{R}g(t)\,dt\\
&=-2\int_b^R g(t)\,dt.
\end{aligned}
\tag{RF27}
\]

Therefore

\[
\boxed{
\int_{-U}^{U}D_{2a}g
=
\begin{cases}
0,&0\le a\le U-R,\\[1mm]
-2\displaystyle\int_{U-a}^{R}g(t)\,dt,&U-R<a\le U.
\end{cases}
}
\tag{RF28}
\]

The opposite frozen sign convention for translations flips the overall sign only; nonvanishing is unchanged.

The nonzero region in RF28 is precisely the terminal half-shift shell already isolated by PR #56.

Choose, for example, a smooth odd `g` with `g(t)>0` on a nontrivial subset of `(0,R)`.  For any terminal shift whose lower limit enters that positive region, RF28 is nonzero.  Hence there is no operator identity RF24 on the odd source sector.

Since the hub is a positive real weighted sum of such half-shift differences (up to the fixed global adjoint sign), oddness by itself cannot enforce zero mean after finite-window truncation.

### Route-status booking

```text
R43-COND-ODD-SOURCE-HUB-MEAN-ZERO ×[M]_neg,local
```

Again, this is a no-go for a **universal structural identity**.  It does not determine the mean of the one canonical reverse-normal datum.

---

## 8. Reflection parity of the exact Schur least-squares correction

PR #68 retains the exact extension-cost formula

\[
\langle x,K_{U,V}^{\rm Schur}x\rangle
=
\inf_{y\in\mathcal N}
\left(
\|R_V(\iota x-y)\|^2+\|y\|^2
\right)
-\|R_Ux\|^2,
\tag{RF29}
\]

where

\[
\mathcal N=L^2((-V,V)\setminus(-U,U)).
\]

The new-strip space is invariant under `J_V`.  Because `A_V=R_V^*R_V` commutes with reflection by RF15, the strictly convex objective

\[
F_x(y)
:=
\langle \iota x-y,A_V(\iota x-y)\rangle
+\|y\|^2
\tag{RF30}
\]

satisfies

\[
F_{J_Ux}(J_Vy)=F_x(y).
\tag{RF31}
\]

The `+\|y\|^2` term makes the minimizer unique.  Equivalently, with the PR #55 notation

\[
M=R_V\iota,
\qquad
S=R_VP_{\mathcal N},
\]

it is

\[
\boxed{
y_*(x)=(I+S^*S)^{-1}S^*Mx.
}
\tag{RF32}
\]

For even `x`, RF31 and uniqueness imply

\[
\boxed{
J_Vy_*(x)=y_*(x).
}
\tag{RF33}
\]

In particular, for `x=x_rev`, the least-squares correction on the positive and negative new strips has the **same reflection parity**, not opposite parity.

Therefore the proposed mechanism

```text
x_rev odd
  -> opposite signs on the two strip sides
  -> direct two-sided cancellation
```

is unavailable: its premise is false, and the exact minimizer inherits even parity.

### Important firewall

RF33 does **not** make the Schur/least-squares route useless.  The exact denominator can still exploit:

- prime-shift coherence;
- cancellation among different translated preimages;
- the weighted variance/mean decomposition from PR #70/#74;
- saturation through `(I+S^*S)^{-1}`;
- special structure of the actual canonical `x_rev` beyond reflection parity.

What RF33 rules out is only a free gain coming from an **odd left-versus-right strip sign**.

### Route-status booking

```text
R43-COND-REVERSE-PARITY-OPPOSITE-STRIP-CANCELLATION ×[M]_neg,local
```

---

## 9. Corrected reflection chain

The exact parity chain is

\[
\boxed{
\begin{array}{c}
\varepsilon_R\in\mathcal K^-\quad\text{odd}\\
\Downarrow\ (G_{R,\mathrm{cond}}^{U,V})^{-1/2}\\
f_{\rm rev}\quad\text{odd}\\
\Downarrow\ E_{R,U}\\
E_{R,U}f_{\rm rev}\quad\text{odd}\\
\Downarrow\ H_U^*\ \text{(parity flip)}\\
v_U(f_{\rm rev})\quad\text{even}\\
\Downarrow\ \mathcal Q_{U,V}\ \text{(parity preserving)}\\
x_{\rm rev}\quad\text{even}.
\end{array}
}
\tag{RF34}
\]

Thus the earlier proposed conclusion

\[
x_{\rm rev}\text{ odd}\Rightarrow\langle x_{\rm rev},1\rangle=0
\]

cannot be used in the canonical reverse channel.

---

## 10. Status ledger

New exact/local bookings:

```text
R43-COND-REVERSE-SOURCE-ODD-SECTOR                   ✓[M]_local
R43-COND-REVERSE-HUB-EVEN-PARITY                     ✓[M]_local
R43-COND-RESIDUAL-NORMAL-REFLECTION-SYMMETRY         ✓[M]_local
R43-COND-GEOMEAN-REFLECTION-COMPATIBILITY            ✓[M]_local
R43-COND-REVERSE-PARITY-COMMON-MODE-ELIMINATION      ×[M]_neg,local
R43-COND-ODD-SOURCE-HUB-MEAN-ZERO                    ×[M]_neg,local
R43-COND-REVERSE-PARITY-OPPOSITE-STRIP-CANCELLATION ×[M]_neg,local
```

All are local Draft-source bookings only.  No theorem Registry promotion or independent-review status is created.

Retained OPEN:

```text
ROADMAP-COND-REVERSE-CANONICAL-COMMON-MODE-COEFFICIENT
ROADMAP-COND-REVERSE-PRIME-SHIFT-MEAN-CONTROL
ROADMAP-COND-REVERSE-PRIME-SHIFT-VARIANCE-CONTROL
ROADMAP-COND-REVERSE-EXACT-SCHUR-CORRELATION-DECAY
ROADMAP-COND-REVERSE-NORMAL-STRETCH-DECAY
FD23-UNIF
B-FLAGMOD / B-FLAGDYN
B-FLAGTIGHT
B-SIGN / B-ORIENT
Strong Terminal / C6
Object X
RH
```

---

## 11. Next attack

The reflection audit removes two tempting shortcuts:

1. universal collar control cannot beat the PR-#80 `O(1)` dyadic weighted scale;
2. parity does not remove the sharp constant sector and does not create opposite-strip signs.

The surviving structured route is therefore narrower and cleaner:

\[
\boxed{
\text{analyze the exact Schur/least-squares correlations on the even }x_{\rm rev},
\text{ before replacing them by a positive occupancy majorant.}
}
\]

A useful next calculation should start from the exact primitive pointwise least-squares formula of PR #70/#74 and retain the actual prime-shift values generated by

\[
x_{\rm rev}=\mathcal Q_{U,V}H_U^*E_{R,U}f_{\rm rev}.
\]

The target is not a left/right sign cancellation.  It is a structured estimate showing that the coherent weighted mean and/or weighted prime-shift variance is smaller for this canonical even vector than for the universal graph unit ball.

No such estimate is claimed in this note.
