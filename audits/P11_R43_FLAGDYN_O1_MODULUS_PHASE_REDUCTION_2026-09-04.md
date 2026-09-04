# P11 R43 — B-FLAGDYN: O1 modulus/phase reduction

Date: 2026-09-04

## Purpose and governance

Refine the fixed-source B-FLAGDYN front using the already frozen/exact O1 decomposition of a two-horizon terminal-gauge defect.

This note proves two algebraic reductions:

1. the O1 Jensen/compression defect is not independent of O1 range leakage;
2. the deep-flag variation of the unresolved normal orbit is bounded by exactly two projected O1 channels: a normalized modulus channel and a polar-phase channel.

R43 remains OPEN. No freeze, no new formal independent-GREEN booking, no `✓[M]`, no Strong-Terminal/C6 closure, and no Object-X/RH promotion.

---

## 1. Setup

Fix `0<R<S` and terminals `U<V`. Write

\[
W_U:=W_{R,S}^{[U]},\qquad W_V:=W_{R,S}^{[V]}.
\]

Let the exact C2 horizon-gauge changes be

\[
C_X^{U\to V}
:=G_{X,V}^{1/2}G_{X,U}^{-1/2},
\qquad X\in\{R,S\},
\]

so that

\[
\boxed{
W_V=C_S^{U\to V}W_U(C_R^{U\to V})^{-1}.
}
\tag{FD1}
\]

For brevity put

\[
C_X=C_X^{U\to V},
\qquad
A_X=C_X^*C_X,
\]

and let

\[
C_X=\mathcal U_XA_X^{1/2}
\]

be the polar decomposition. Thus

\[
C_X^{-1}=A_X^{-1/2}\mathcal U_X^*.
\]

Let

\[
R_U:=W_UW_U^*
\]

be the projection onto the moving range.

O1 defines

\[
\boxed{
\mathscr L
:=(I-R_U)A_S^{1/2}W_U,
}
\tag{FD2}
\]

\[
\boxed{
\mathscr J
:=A_R^{1/2}-W_U^*A_S^{1/2}W_U\ge0,
}
\tag{FD3}
\]

and

\[
\boxed{
\mathscr P
:=\mathcal U_SW_U\mathcal U_R^*-W_U.
}
\tag{FD4}
\]

The exact O1 defect formula is

\[
\boxed{
W_V-W_U
=
\mathcal U_S(\mathscr L-W_U\mathscr J)
A_R^{-1/2}\mathcal U_R^*
+\mathscr P.
}
\tag{FD5}
\]

---

## 2. New exact modulus-lock identity

Define the positive compression

\[
B:=W_U^*A_S^{1/2}W_U.
\tag{FD6}
\]

By definition of `\mathscr J`,

\[
\boxed{
B=A_R^{1/2}-\mathscr J.
}
\tag{FD7}
\]

Also

\[
R_UA_S^{1/2}W_U
=W_UW_U^*A_S^{1/2}W_U
=W_UB.
\]

Together with FD2,

\[
\boxed{
A_S^{1/2}W_U=W_UB+\mathscr L.
}
\tag{FD8}
\]

The two summands are orthogonal because

\[
W_U^*\mathscr L
=W_U^*(I-R_U)A_S^{1/2}W_U
=0.
\]

Taking adjoint products in FD8 and using the exact O1 compression identity

\[
W_U^*A_SW_U=A_R
\]

gives

\[
\boxed{
A_R=B^2+\mathscr L^*\mathscr L.
}
\tag{FD9}
\]

Therefore

\[
\boxed{
B^2=A_R-\mathscr L^*\mathscr L.
}
\tag{FD10}
\]

Since `B\ge0`, uniqueness of the positive square root yields

\[
\boxed{
B=(A_R-\mathscr L^*\mathscr L)^{1/2}.
}
\tag{FD11}
\]

Combining FD7 and FD11,

\[
\boxed{
\mathscr J
=A_R^{1/2}
-(A_R-\mathscr L^*\mathscr L)^{1/2}.
}
\tag{FD12}
\]

Equivalently, expanding `B^2=(A_R^{1/2}-\mathscr J)^2`,

\[
\boxed{
\mathscr L^*\mathscr L
=A_R^{1/2}\mathscr J
+\mathscr J A_R^{1/2}
-\mathscr J^2.
}
\tag{FD13}
\]

### Consequence

The O1 range-leakage defect `\mathscr L` and Jensen/compression defect `\mathscr J` are **not independent modulus obstructions**. Once `A_R` and `\mathscr L` are known, `\mathscr J` is fixed by FD12.

In particular,

\[
\boxed{
\mathscr L=0
\iff
\mathscr J=0.
}
\tag{FD14}
\]

The forward implication follows from FD12. The reverse implication follows from FD13.

This does **not** prove either defect is small for the P11 terminal family; it only removes a false degree of freedom in the modulus bookkeeping.

A standard operator square-root continuity estimate also gives the optional norm consequence

\[
\|\mathscr J\|
\le
\|\mathscr L\|,
\tag{FD15}
\]

because `B=(B^2)^{1/2}` and

\[
\|A_R^{1/2}-(B^2)^{1/2}\|
\le
\|A_R-B^2\|^{1/2}
=
\|\mathscr L^*\mathscr L\|^{1/2}
=
\|\mathscr L\|.
\]

FD15 is a convenient sufficient norm comparison; the exact algebraic content is FD9--FD14.

---

## 3. Exact deep-flag two-defect inequality

Let

\[
P_m:=P_{\mathcal H_S^{[m]}},
\qquad
w_U:=W_U\varepsilon_R,
\]

and

\[
q_m(U):=\|P_mw_U\|^2=\|P_mh_U\|^2.
\]

By the reverse triangle inequality,

\[
\boxed{
\left|
\sqrt{q_m(V)}-\sqrt{q_m(U)}
\right|
\le
\|P_m(W_V-W_U)\varepsilon_R\|.
}
\tag{FD16}
\]

Insert the exact O1 decomposition FD5 and define

\[
\boxed{
\mathfrak d_{m,\mathrm{mod}}(U,V)
:=
\left\|
P_m\mathcal U_S
(\mathscr L-W_U\mathscr J)
A_R^{-1/2}\mathcal U_R^*
\varepsilon_R
\right\|,
}
\tag{FD17}
\]

\[
\boxed{
\mathfrak d_{m,\mathrm{ph}}(U,V)
:=
\|P_m\mathscr P\varepsilon_R\|.
}
\tag{FD18}
\]

Then exactly

\[
\boxed{
\left|
\sqrt{q_m(V)}-\sqrt{q_m(U)}
\right|
\le
\mathfrak d_{m,\mathrm{mod}}(U,V)
+
\mathfrak d_{m,\mathrm{ph}}(U,V).
}
\tag{FD19}
\]

Both defect terms vanish identically at zero terminal separation `V=U`, because then

\[
C_R=C_S=I,
\qquad
A_R=A_S=I,
\qquad
\mathcal U_R=\mathcal U_S=I,
\qquad
\mathscr L=\mathscr J=\mathscr P=0.
\]

Thus FD19 is a genuine local terminal-increment inequality, unlike the earlier partial-isometry off-flag block.

By FD12, the modulus term FD17 contains only one genuinely independent O1 modulus defect, `\mathscr L`; the `\mathscr J` part is its induced square-root/compression correction.

---

## 4. Summable two-defect criterion for B-FLAGTIGHT

Choose a terminal partition

\[
U_0<U_1<U_2<\cdots\to\infty.
\]

Define

\[
\boxed{
\Delta_{m,k}^{\mathrm{mod}}
:=
\sup_{V\in[U_k,U_{k+1}]}
\mathfrak d_{m,\mathrm{mod}}(U_k,V),
}
\tag{FD20}
\]

and

\[
\boxed{
\Delta_{m,k}^{\mathrm{ph}}
:=
\sup_{V\in[U_k,U_{k+1}]}
\mathfrak d_{m,\mathrm{ph}}(U_k,V).
}
\tag{FD21}
\]

Iterating FD19 yields, for every `V\in[U_k,U_{k+1}]`,

\[
\sqrt{q_m(V)}
\le
\sqrt{q_m(U_0)}
+
\sum_{j\le k}
\left(
\Delta_{m,j}^{\mathrm{mod}}
+
\Delta_{m,j}^{\mathrm{ph}}
\right).
\tag{FD22}
\]

For fixed `U_0`, C6a completeness gives

\[
q_m(U_0)\to0
\qquad(m\to\infty).
\]

Therefore:

### Proposition FD-B-FLAGDYN

If a terminal partition exists such that

\[
\boxed{
\lim_{m\to\infty}
\sum_{k\ge0}
\left(
\Delta_{m,k}^{\mathrm{mod}}
+
\Delta_{m,k}^{\mathrm{ph}}
\right)
=0,
}
\tag{FD23}
\]

then

\[
\boxed{
\lim_{m\to\infty}
\sup_{U\ge U_0}q_m(U)=0,
}
\tag{FD24}
\]

and hence B-FLAGTIGHT holds.

FD23 is a sufficient criterion stronger than the exact iterated-limsup B-FLAGTIGHT gate. No necessity is claimed.

---

## 5. What is now genuinely open

The previous phrase "three sources of flag motion" overcounts the independent O1 modulus data. The exact algebra says:

- `A_R` is the positive source relative metric;
- `\mathscr L` is the genuinely new modulus range-leakage defect;
- `\mathscr J` is determined by `A_R` and `\mathscr L` through FD12;
- `\mathscr P` is the independent polar-phase mismatch.

Thus the active derivative-free B-FLAGDYN front can be sharpened to two projected channels:

\[
\boxed{
\textbf{B-FLAGMOD: projected normalized modulus leakage}
}
\]

and

\[
\boxed{
\textbf{B-FLAGPHASE: projected polar-phase mismatch.}
}
\]

R38--R42 do not presently close either channel on the fixed source normal. In particular, the R42 tangential polar convergence results concern fixed tangential directions and do not silently imply the two-horizon normal phase bound FD18.

No terminal derivative or generator is introduced.

---

## 6. Current chain

The sharpened research tree is

\[
\boxed{
\text{GC-AC candidate-closed}
\longrightarrow
\left[
\text{B-FLAGMOD}
+
\text{B-FLAGPHASE}
\right]
\Longrightarrow
\text{B-FLAGTIGHT}
\longrightarrow
\text{B-SIGN}.
}
\]

The middle implication is the sufficient two-defect criterion FD23, not an equivalence.
