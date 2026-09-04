# P11 R43 — terminal metric increment definition audit

Date: 2026-09-04

## Status and firewall

This audit performs the destructive definition check requested before any positive-shell
or Loewner-monotonicity argument is imported into B-FLAGMOD.

It does **not** prove B-FLAGMOD, B-FLAGTIGHT, Strong Terminal/C6, Object X, or RH.
It creates no freeze, no new formal independent-GREEN booking, and no new `✓[M]`.
R43 remains OPEN.

The main distinction is:

1. exact fixed-source terminal metric identities;
2. exact decomposition of the horizon-dependent Schur energy;
3. unconditional metric-increment control of the B-FLAGMOD leakage;
4. a strictly conditional Loewner-positive accelerator;
5. a firewall against silently replacing the frozen Schur geometry by a new-shell-only
   positive Gram sum.

---

## 1. Frozen definition of the terminal metric

Fix one source radius `X>0` and two terminal horizons

\[
X<U<V.
\]

Frozen R4 defines the zero-extension graph transition

\[
J_{X,T}=E_{X,T}:\mathcal K_X(X)\longrightarrow\mathcal K_X(T)
\]

and the terminal metric on the **fixed source graph Hilbert space**

\[
\boxed{
G_{X,T}:=J_{X,T}^*J_{X,T}.
}
\tag{MI1}
\]

Hence `G_{X,U}` and `G_{X,V}` are operators on the same fixed Hilbert space.  Their
comparison requires no moving-space identification.

For every fixed source vector `f`,

\[
\boxed{
\langle f,G_{X,T}f\rangle_{X,X}
=q_T^X(E_{X,T}f).
}
\tag{MI2}
\]

Define the genuine terminal metric increment

\[
\boxed{
\Delta G_X^{U,V}:=G_{X,V}-G_{X,U}.
}
\tag{MI3}
\]

Then

\[
\boxed{
\langle f,\Delta G_X^{U,V}f\rangle_{X,X}
=q_V^X(E_{X,V}f)-q_U^X(E_{X,U}f).
}
\tag{MI4}
\]

This difference is formed **before any shell reindexing**.

---

## 2. Exact Gamma cancellation: all terminal variation is Schur variation

Frozen R4 gives, for zero extension,

\[
\mathfrak c_{\Gamma,T}(E_{X,T}f)
=\mathfrak c_{\Gamma,X}(f).
\tag{MI5}
\]

The finite-level candidate form is

\[
q_T^X(g)
=\mathfrak c_{\Gamma,T}[g]+\langle\Sigma_Tg,g\rangle.
\tag{MI6}
\]

Therefore the Gamma terms cancel exactly in (MI4):

\[
\boxed{
\langle f,\Delta G_X^{U,V}f\rangle_{X,X}
=
\langle\Sigma_VE_{X,V}f,E_{X,V}f\rangle
-
\langle\Sigma_UE_{X,U}f,E_{X,U}f\rangle.
}
\tag{MI7}
\]

Thus every possible Loewner-monotonicity statement for `T -> G_{X,T}` is, on the frozen
construction, entirely a statement about the terminal Schur term.

---

## 3. Frozen Schur structure and why new-shell-only is not automatic

The manuscript defines

\[
\boxed{
\Sigma_T=H_TB_TH_T^*,
\qquad
B_T=(I+R_T^*R_T)^{-1}.
}
\tag{MI8}
\]

The hub itself is

\[
\boxed{
H_T
=P_T\sum_{p^k\le e^{2T}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_T.
}
\tag{MI9}
\]

Two different kinds of terminal dependence are already visible in the frozen formula:

1. **new-shell activation:** the index set `p^k <= e^{2T}` grows with `T`;
2. **old-shell geometry:** even for an already active `(p,k)`, the finite-window operator
   `P_T D_{k log p} E_T` depends on `T`.

The scalar coefficient

\[
\sqrt{\log p}\,p^{-3k/4}
\]

itself is horizon independent.  Thus at primitive hub level there is no scalar
old-weight reweighting; the old contribution changes through geometry.

There is, however, a further global terminal dependence through the Feshbach conditioning

\[
B_T=(I+R_T^*R_T)^{-1},
\tag{MI10}
\]

and `R_T` is itself horizon dependent.  Hence the effective Schur weights/couplings of
old channels can change even when the primitive hub coefficient is fixed.

Accordingly, the frozen definitions do **not** justify the replacement

\[
\Delta G_X^{U,V}
\stackrel?=
\sum_{U<\tau(\lambda)\le V}
\omega_{X,\lambda}\Phi_{X,\lambda}^*\Phi_{X,\lambda}
\tag{MI11?}
\]

with fixed positive atoms.  Such a formula would require a new theorem showing that all
post-entry atoms and effective weights are horizon independent in a suitable fixed-space
realization.

This audit makes no theorem-level claim that such a representation is impossible.  It is
simply **not supplied by the frozen definitions**.

---

## 4. Exact old-conditioning / old-geometry / new-shell split of the Schur energy

For fixed `f` define

\[
v_T(f):=H_T^*E_{X,T}f\in L^2(-T,T).
\tag{MI12}
\]

Then the terminal Schur energy is

\[
s_T(f):=
\langle\Sigma_TE_{X,T}f,E_{X,T}f\rangle
=
\langle v_T(f),B_Tv_T(f)\rangle.
\tag{MI13}
\]

Let

\[
\iota:=E_{U,V}:L^2(-U,U)\to L^2(-V,V)
\]

and define the exact geometry increment

\[
d_{U,V}(f):=v_V(f)-\iota v_U(f).
\tag{MI14}
\]

Then, without any sign assumption,

\[
\boxed{
\begin{aligned}
s_V(f)-s_U(f)
={}&
\langle v_U,
(\iota^*B_V\iota-B_U)v_U\rangle\\
&+2\operatorname{Re}\langle d_{U,V},B_V\iota v_U\rangle
+\langle d_{U,V},B_Vd_{U,V}\rangle.
\end{aligned}
}
\tag{MI15}
\]

The first term is the **old-conditioning** term.  It contains the change of the nonlinear
Feshbach denominator and has no sign from positivity of `B_U,B_V` alone.

The geometry increment can be split exactly at the hub level.  Write

\[
\Lambda_T:=\{(p,k):p^k\le e^{2T}\}
\]

and

\[
K_{p,k;T}:=P_TD_{k\log p}E_T,
\qquad
a_{p,k}:=\sqrt{\log p}\,p^{-3k/4}.
\]

Then

\[
H_T=\sum_{(p,k)\in\Lambda_T}a_{p,k}K_{p,k;T}.
\]

Consequently

\[
\boxed{
d_{U,V}=d_{\rm old\text{-}geom}^{U,V}+d_{\rm new}^{U,V},
}
\tag{MI16}
\]

where

\[
\begin{aligned}
d_{\rm old\text{-}geom}^{U,V}(f)
&:=
\sum_{(p,k)\in\Lambda_U}a_{p,k}
\Bigl(
K_{p,k;V}^*E_{X,V}
-\iota K_{p,k;U}^*E_{X,U}
\Bigr)f,\\
d_{\rm new}^{U,V}(f)
&:=
\sum_{(p,k)\in\Lambda_V\setminus\Lambda_U}a_{p,k}
K_{p,k;V}^*E_{X,V}f.
\end{aligned}
\tag{MI17}
\]

Thus the requested destructive split exists, but it is **not** a sum of separately
positive Schur-energy increments: MI15 contains an old-conditioning term and cross terms
between the old and new geometry.

---

## 5. Loewner monotonicity: separate weaker gate, presently OPEN

The weak positivity question is

\[
\boxed{
\Delta G_X^{U,V}\ge0
\quad ?
}
\tag{MI18}
\]

for fixed source `X` and all sufficiently late, or all, `U<V`.

MI7 reduces this exactly to

\[
\langle\Sigma_VE_{X,V}f,E_{X,V}f\rangle
\ge
\langle\Sigma_UE_{X,U}f,E_{X,U}f\rangle
\quad\forall f.
\tag{MI19}
\]

Neither positivity of each `Sigma_T` nor positivity of each `B_T` implies MI19.  The exact
split MI15 has terms of undetermined sign.  Frozen R4 proves positivity/invertibility of
each terminal metric and the pullback identity, but no Loewner monotonicity theorem is
imported here.

Therefore:

\[
\boxed{
[\mathrm{R43\text{-}MI\text{-}LOEWNER}]\quad ?[O].
}
\tag{MI20}
\]

Positive new-shell-only Gram additivity is strictly stronger than MI18 and remains
unbooked.

---

## 6. Normalized relative metric increment

For fixed source `X` define

\[
\boxed{
\mathbf H_X^{U,V}
:=
G_{X,U}^{-1/2}
\Delta G_X^{U,V}
G_{X,U}^{-1/2}.
}
\tag{MI21}
\]

The boldface notation is used here only to avoid confusion with the manuscript's hub
operator `H_T`.

Equivalently, if

\[
A_X^{U,V}
:=G_{X,U}^{-1/2}G_{X,V}G_{X,U}^{-1/2},
\]

then

\[
\boxed{
\mathbf H_X^{U,V}=A_X^{U,V}-I.
}
\tag{MI22}
\]

No sign is needed for this identity.

For the fixed pair `R<S`, frozen O1 compression gives

\[
W_U^*A_S^{U,V}W_U=A_R^{U,V},
\]

hence

\[
\boxed{
W_U^*\mathbf H_S^{U,V}W_U
=
\mathbf H_R^{U,V}.
}
\tag{MI23}
\]

---

## 7. Unconditional B-FLAGMOD metric-increment bound

Put

\[
P_U:=W_UW_U^*
\]

and

\[
\boxed{
\mathscr E_{U,V}
:=(I-P_U)\mathbf H_S^{U,V}W_U.
}
\tag{MI24}
\]

The previous B-FLAGMOD reduction identified this as the A-level off-range defect.  Since
`I-P_U` is an orthogonal projection and `W_U` is an isometry,

\[
\boxed{
\|\mathscr E_{U,V}\|
\le
\|\mathbf H_S^{U,V}\|.
}
\tag{MI25}
\]

This requires **no Loewner positivity**.

Therefore Loewner monotonicity is an accelerator, not a prerequisite for attacking
B-FLAGMOD.  A direct quantitative theorem showing sufficiently strong cofinal/partition
smallness of

\[
\|\mathbf H_S^{U,V}\|
\]

would already control the A-level modulus leakage.

Bookkeeping status:

\[
\boxed{
[\mathrm{R43\text{-}MI1}]\quad
\|\mathscr E_{U,V}\|\le\|\mathbf H_S^{U,V}\|.
}
\tag{MI26}
\]

This is exact elementary Hilbert-space algebra, but it does not by itself provide the
needed terminal decay.

---

## 8. Conditional Loewner-positive accelerator

Assume, conditionally,

\[
\Delta G_R^{U,V}\ge0,
\qquad
\Delta G_S^{U,V}\ge0.
\tag{MI27}
\]

Then by congruence

\[
\mathbf H_R^{U,V}\ge0,
\qquad
\mathbf H_S^{U,V}\ge0.
\]

The exact compression-variance identity is

\[
\boxed{
\mathscr E_{U,V}^*\mathscr E_{U,V}
=
W_U^*(\mathbf H_S^{U,V})^2W_U
-(\mathbf H_R^{U,V})^2.
}
\tag{MI28}
\]

Since

\[
(\mathbf H_S^{U,V})^2
\le
\|\mathbf H_S^{U,V}\|\,\mathbf H_S^{U,V},
\]

compression and MI23 give the stronger operator estimate

\[
\boxed{
0\le
\mathscr E^*\mathscr E
\le
\|\mathbf H_S\|\,\mathbf H_R
-\mathbf H_R^2
\le
\|\mathbf H_S\|\,\mathbf H_R.
}
\tag{MI29}
\]

Hence

\[
\boxed{
\|\mathscr E_{U,V}\|^2
\le
\|\mathbf H_S^{U,V}\|\,
\|\mathbf H_R^{U,V}\|.
}
\tag{MI30}
\]

The retained negative square yields additionally

\[
\boxed{
\|\mathscr E_{U,V}\|
\le
\tfrac12\|\mathbf H_S^{U,V}\|,
}
\tag{MI31}
\]

because `0 <= H_R <= ||H_S|| I` and the scalar function `x(c-x)` is bounded by `c^2/4`
on `[0,c]`.

Thus the useful conditional bound is

\[
\boxed{
\|\mathscr E\|^2
\le
\min\left\{
\|\mathbf H_S\|\|\mathbf H_R\|,
\frac14\|\mathbf H_S\|^2
\right\}.
}
\tag{MI32}
\]

This is a **conditional theorem**: its premise MI27 remains OPEN.

---

## 9. Sylvester bridge and coercivity firewall

The square-root modulus mismatch

\[
\mathscr M
=(A_S^{U,V})^{1/2}W_U
-W_U(A_R^{U,V})^{1/2}
\]

satisfies exactly

\[
(A_S^{U,V})^{1/2}\mathscr M
+\mathscr M(A_R^{U,V})^{1/2}
=
\mathscr E_{U,V}.
\tag{MI33}
\]

For each fixed pair `U<V`, put

\[
\alpha_X(U,V)
:=
\inf\sigma\bigl((A_X^{U,V})^{1/2}\bigr)>0.
\]

Then the standard positive Sylvester representation gives

\[
\boxed{
\|\mathscr M\|
\le
\frac{\|\mathscr E\|}
{\alpha_S(U,V)+\alpha_R(U,V)}.
}
\tag{MI34}
\]

Frozen R4/C2 gives a fixed-source lower bound for each **absolute** future metric,

\[
G_{X,T}\ge c_XI,
\]

uniform in terminal `T` for fixed source `X`.  This alone does **not** yield a cofinal
uniform positive lower bound for `A_X^{U,V}` as both `U,V -> infinity`, because

\[
A_X^{U,V}
\ge
c_XG_{X,U}^{-1},
\]

and the absolute future metrics are not known to have uniformly bounded norm.

Therefore the pair-dependent Sylvester denominator in MI34 remains explicit.

No terminal-uniform coercivity is silently booked.

---

## 10. What the definitions audit decides

| Question | Result |
|---|---|
| `G_{X,U}` and `G_{X,V}` act on the same fixed source graph space | **YES — frozen R4** |
| Exact difference can be formed before reindexing | **YES — MI3/MI4** |
| Gamma contribution changes with terminal horizon | **NO — cancels exactly** |
| All terminal variation is in the Schur term | **YES — MI7** |
| Primitive hub coefficients of already active prime powers change with horizon | **NO — coefficients are fixed** |
| Old channel geometry can change with horizon | **YES — `P_T D_s E_T` changes** |
| Feshbach conditioning can change old effective couplings | **YES — `B_T=(I+R_T^*R_T)^{-1}` changes** |
| Frozen definitions imply new-shell-only positive Gram additivity | **NO SUCH IMPLICATION** |
| Frozen results prove `Delta G_X^{U,V} >= 0` | **NOT FOUND / OPEN** |
| Positivity is required for `||E|| <= ||H_S||` | **NO** |
| Loewner positivity sharpens the leakage estimate | **YES — conditionally, MI29–MI32** |
| Positivity alone closes B-FLAGMOD | **NO** |
| Cofinal quantitative smallness/summability of normalized increments | **OPEN** |

---

## 11. Sharpened live target: B-METINC inside B-FLAGMOD

The definitions audit changes the order of attack.

The first quantitative target need not be positivity.  Define

\[
\boxed{
\textbf{B-METINC: control }
\|\mathbf H_X^{U,V}\|
=
\left\|
G_{X,U}^{-1/2}(G_{X,V}-G_{X,U})G_{X,U}^{-1/2}
\right\|
}
\tag{MI35}
\]

cofinally, in a form compatible with the terminal-partition summability required by
B-FLAGDYN.

A proof of Loewner monotonicity would strengthen this route through MI29–MI32, and a
positive atom/new-shell theorem could then be used to estimate MI35 arithmetically.  But
neither is logically required before a direct estimate of MI35 is attempted.

Thus the current modulus sub-tree is

\[
\boxed{
\begin{array}{c}
\text{direct B-METINC control}
\\[-1mm]
\text{or}\quad
[\text{Loewner positivity}+\text{quantitative increment control}]
\end{array}
\Longrightarrow
\text{B-FLAGMOD}
}
\tag{MI36}
\]

subject to the explicit pairwise Sylvester conditioning factor and the existing projected
B-FLAGDYN summability requirement.

The stronger new-shell-only representation is an optional arithmetic route to B-METINC,
not the definition of the gate.

---

## 12. Governance

- R43: OPEN.
- `R43-MI-LOEWNER`: OPEN.
- B-METINC: OPEN.
- B-FLAGMOD: OPEN.
- B-FLAGPHASE: OPEN.
- B-FLAGTIGHT: OPEN.
- B-SIGN: OPEN.
- Strong Terminal/C6: OPEN.
- no freeze;
- no new formal independent GREEN;
- no new `✓[M]`;
- R38–R42 unchanged/frozen;
- R37/G4c separate and open;
- no Object-X/RH promotion.
