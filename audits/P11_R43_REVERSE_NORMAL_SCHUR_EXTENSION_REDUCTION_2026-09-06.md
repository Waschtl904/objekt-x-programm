# P11 / R43 — reverse-normal Schur extension-cost reduction

**Date:** 2026-09-06  
**Status:** exact/local reduction stacked on PR #66; reverse-normal decay remains OPEN  
**Exact parent head:** `7d8a9e47c96962f49afedba83f1090a1598f5386`  
**Parent PR:** #66 — `R43: one-sided COND cap to FLAGDYN via reverse-normal stretch`

## 0. Purpose and firewall

PR #66 reduces the old-conditioning O1 modulus channel to two explicit open gates:

1. reverse-normal stretch decay;
2. `FD23-UNIF`.

The present note attacks only the first gate.  It combines the PR-#57 geometric-mean Schur algebra with the exact reverse-normal datum from PR #66 and proves two equivalent local reductions:

- an exact **newly-resolved residual-energy formula** for the reverse stretch;
- an exact **least-squares / extension-cost formula** for the same Schur quantity.

The extension-cost form keeps the Schur saturation instead of discarding it and turns the remaining analytic problem into a concrete question: can the resolvent-transported reverse-normal vector be continued into the new spatial strip with asymptotically negligible extra residual cost?

No reverse-normal decay rate is proved here.  No `FD23-UNIF`, GEO/NEW channel, phase theorem, `B-FLAGDYN/TIGHT`, Strong Terminal/C6, Object-X realization, or RH statement is claimed.

All bookings below are local Draft-source bookings only; no Registry promotion is made.

---

## 1. Frozen old-conditioning and Schur notation

Fix a source radius `R` and horizons

\[
R<U<V.
\]

Retain the PR-#55/#57 residual notation

\[
M:=R_V\iota,
\qquad
S:=R_VP_{\mathcal N},
\qquad
\mathcal N:=L^2((-V,V)\setminus(-U,U)),
\]

and

\[
\Phi_S:=SS^*(I+SS^*)^{-1}.
\]

The exact Schur sign operator is

\[
\boxed{
K_{U,V}^{\rm Schur}
=M^*(I+SS^*)^{-1}M-R_U^*R_U
=C_{U,V}^*C_{U,V}-M^*\Phi_SM,
}
\tag{RE1}
\]

where `C_{U,V}` is the PR-#55 newly-resolved residual operator.  It must not be confused with the PR-#66 polar factor `C_{R,cond}^{U,V}`.

Put

\[
\mathscr A_U:=I+R_U^*R_U,
\qquad
B_U:=\mathscr A_U^{-1},
\qquad
\widetilde B_{U,V}:=\iota^*B_V\iota.
\]

PR #57 defines the positive geometric-mean transport

\[
\boxed{
\mathcal Q_{U,V}
:=B_U\#\widetilde B_{U,V}
}
\tag{RE2}
\]

and proves the exact Riccati identity

\[
\boxed{
\mathcal Q_{U,V}\,\mathscr A_U\,\mathcal Q_{U,V}
=\widetilde B_{U,V}.
}
\tag{RE3}
\]

For a fixed-source datum `f`, write

\[
v_U(f):=H_U^*E_{R,U}f,
\qquad
x_{U,V}(f):=\mathcal Q_{U,V}v_U(f).
\tag{RE4}
\]

PR #57 also proves

\[
\boxed{
\Delta s_{\rm cond}^{U,V}(f)
=-\langle x_{U,V}(f),K_{U,V}^{\rm Schur}x_{U,V}(f)\rangle.
}
\tag{RE5}
\]

---

## 2. The canonical reverse-normal source datum

Use the PR-#66 old-conditioning metric

\[
G_{R,\mathrm{cond}}^{U,V}
\]

and its terminal-`U` baseline metric `G_{R,U}`.  PR #66 defines

\[
A_{R,\mathrm{cond}}^{U,V}
=G_{R,U}^{-1/2}
G_{R,\mathrm{cond}}^{U,V}
G_{R,U}^{-1/2}
\]

and the polar factor

\[
C_{R,\mathrm{cond}}^{U,V}
=(G_{R,\mathrm{cond}}^{U,V})^{1/2}G_{R,U}^{-1/2}.
\]

Let `\varepsilon_R` be the fixed unit source normal from R42/R43.  Define

\[
\boxed{
f_{R;U,V}^{\rm rev}
:=(G_{R,\mathrm{cond}}^{U,V})^{-1/2}\varepsilon_R.
}
\tag{RE6}
\]

Then, exactly,

\[
\boxed{
q_{R,\mathrm{cond}}^{U,V}(f_{R;U,V}^{\rm rev})
=1.
}
\tag{RE7}
\]

Moreover

\[
\begin{aligned}
q_{R,U}(f_{R;U,V}^{\rm rev})
&=
\left\langle
(G_{R,\mathrm{cond}}^{U,V})^{-1/2}\varepsilon_R,
G_{R,U}
(G_{R,\mathrm{cond}}^{U,V})^{-1/2}\varepsilon_R
\right\rangle\\
&=
\|(C_{R,\mathrm{cond}}^{U,V})^{-1}\varepsilon_R\|^2.
\end{aligned}
\tag{RE8}
\]

Hence the PR-#66 reverse-normal stretch satisfies

\[
\boxed{
\rho^{\rm rev}_{R;U,V}
=
\bigl(
q_{R,U}(f_{R;U,V}^{\rm rev})
-q_{R,\mathrm{cond}}^{U,V}(f_{R;U,V}^{\rm rev})
\bigr)_+
=
\bigl(-\Delta s_{\rm cond}^{U,V}(f_{R;U,V}^{\rm rev})\bigr)_+.
}
\tag{RE9}
\]

This is a source-space identity; no R40/R41 asymptotic is imported.

---

## 3. Exact reverse-normal residual-energy identity

Put

\[
\boxed{
x_{R;U,V}^{\rm rev}
:=
\mathcal Q_{U,V}H_U^*E_{R,U}
f_{R;U,V}^{\rm rev}.
}
\tag{RE10}
\]

Applying RE5 to RE6 and using RE9 gives

\[
\rho^{\rm rev}_{R;U,V}
=
\bigl(
\langle x_{R;U,V}^{\rm rev},
K_{U,V}^{\rm Schur}
x_{R;U,V}^{\rm rev}\rangle
\bigr)_+.
\tag{RE11}
\]

Insert the exact decomposition RE1:

\[
\boxed{
\rho^{\rm rev}_{R;U,V}
=
\Bigl(
\|C_{U,V}x_{R;U,V}^{\rm rev}\|^2
-
\|\Phi_S^{1/2}Mx_{R;U,V}^{\rm rev}\|^2
\Bigr)_+.
}
\tag{RE12}
\]

Therefore

\[
\boxed{
\rho^{\rm rev}_{R;U,V}
\le
\|C_{U,V}x_{R;U,V}^{\rm rev}\|^2.
}
\tag{RE13}
\]

### Local draft booking

```text
R43-COND-REVERSE-NORMAL-C-ENERGY-REDUCTION ✓[M]
```

The booking is RE9--RE13 only.  It contains no terminal decay.

---

## 4. Exact old-graph normalization of the reverse vector

Use the Riccati identity RE3 with

\[
v=v_U(f_{R;U,V}^{\rm rev}),
\qquad
x=x_{R;U,V}^{\rm rev}.
\]

Then

\[
\begin{aligned}
\|x\|^2+\|R_Ux\|^2
&=
\langle x,\mathscr A_Ux\rangle\\
&=
\langle v,\widetilde B_{U,V}v\rangle\\
&=:s_{\rm cond}(f_{R;U,V}^{\rm rev}).
\end{aligned}
\tag{RE14}
\]

The conditioning form is Gamma plus the nonnegative Schur term, hence

\[
0\le s_{\rm cond}(f_{R;U,V}^{\rm rev})
\le q_{R,\mathrm{cond}}^{U,V}(f_{R;U,V}^{\rm rev})=1.
\]

Therefore

\[
\boxed{
\|x_{R;U,V}^{\rm rev}\|^2
+\|R_Ux_{R;U,V}^{\rm rev}\|^2
\le1.
}
\tag{RE15}
\]

PR #64's universal prime-band collar estimate may thus be applied to this moving datum without any circular factor involving `rho_rev`.  In particular, with `r=8\log U`,

\[
\boxed{
\|\chi_{U,8\log U}x_{R;U,V}^{\rm rev}\|^2
=O_R\!\left(\frac{\log U}{U}\right)
}
\tag{RE16}
\]

uniformly in `V>U`, in the same sufficiently-large-`U` regime as PR #64.

### Local draft booking

```text
R43-COND-REVERSE-NORMAL-OLD-GRAPH-NORMALIZATION ✓[M]
```

RE16 is only a collar-mass statement.  It does not imply RE13 decays, because `C_{U,V}` contains old-window/new-fine martingale energy as well as new-strip energy.

---

## 5. Why a raw `C`-collar theorem is not presently available

The P11 martingale depth is

\[
J_{p,U}(u)
=
\max\left\{0,
\left\lfloor
\frac{2(U-|u|)_+}{\log p}
\right\rfloor
\right\}.
\tag{RE17}
\]

Thus the old-window/new-fine part of `C_{U,V}` selects martingale coordinates lying above the old depth `J_{p,U}(u)` and below the new depth `J_{p,V}(u)`.

For each fixed prime/level this is a boundary-depth effect.  However, for large primes `\frac12\log p` is itself large, and `J_{p,U}(u)=0` can occur away from a fixed-width terminal collar.  A naive primewise estimate based only on the residual coefficient `p^{-k/4}` encounters the non-summable primitive `p^{-1/2}` square scale.

The structured pre-transport vector has the stronger hub coefficient `p^{-3k/4}`, but PR #57 proves only that `\mathcal Q_{U,V}` is a positive contraction; it does **not** prove preservation of spatial support or of the raw hub shell through the geometric-mean transport.  Hence the implication

```text
raw H_U^* shell
  => transported shell after Q_{U,V}
  => full C-energy decay
```

is not available in the present stack.

This is a firewall, not a no-go theorem.

---

## 6. Exact Schur least-squares / extension-cost formula

The preceding `C`-only estimate discards the favorable saturation term in RE12.  There is an exact variational form that retains it.

For an arbitrary target-residual vector `b`, consider

\[
F_b(y):=\|b-Sy\|^2+\|y\|^2,
\qquad y\in\mathcal N.
\]

The unique minimizer solves

\[
(I+S^*S)y=S^*b,
\]

so

\[
y_*=(I+S^*S)^{-1}S^*b.
\tag{RE18}
\]

Substitution, or the push-through identity, gives

\[
\boxed{
\inf_{y\in\mathcal N}
\bigl(\|b-Sy\|^2+\|y\|^2\bigr)
=
\langle b,(I+SS^*)^{-1}b\rangle.
}
\tag{RE19}
\]

Take `b=Mx`.  By the definition of `K_{U,V}^{Schur}`,

\[
\boxed{
\langle x,K_{U,V}^{\rm Schur}x\rangle
=
\inf_{y\in\mathcal N}
\Bigl(
\|Mx-Sy\|^2+\|y\|^2
\Bigr)
-\|R_Ux\|^2.
}
\tag{RE20}
\]

Since

\[
M=R_V\iota,
\qquad
S=R_VP_{\mathcal N},
\]

and `y` is already identified with its embedded new-strip vector,

\[
\boxed{
\langle x,K_{U,V}^{\rm Schur}x\rangle
=
\inf_{y\in\mathcal N}
\Bigl(
\|R_V(\iota x-y)\|^2+\|y\|^2
\Bigr)
-\|R_Ux\|^2.
}
\tag{RE21}
\]

For the reverse-normal vector RE10,

\[
\boxed{
\rho^{\rm rev}_{R;U,V}
=
\left[
\inf_{y\in\mathcal N}
\Bigl(
\|R_V(\iota x_{R;U,V}^{\rm rev}-y)\|^2+\|y\|^2
\Bigr)
-\|R_Ux_{R;U,V}^{\rm rev}\|^2
\right]_+.
}
\tag{RE22}
\]

Consequently every trial correction `y_{U,V}\in\mathcal N` yields the rigorous upper bound

\[
\boxed{
\rho^{\rm rev}_{R;U,V}
\le
\left[
\|R_V(\iota x_{R;U,V}^{\rm rev}-y_{U,V})\|^2
+\|y_{U,V}\|^2
-\|R_Ux_{R;U,V}^{\rm rev}\|^2
\right]_+.
}
\tag{RE23}
\]

### Local draft booking

```text
R43-COND-REVERSE-NORMAL-SCHUR-EXTENSION-VARIATIONAL ✓[M]
```

This is an exact finite-pair theorem.  It does not construct a useful trial correction.

---

## 7. New quantitative target: cheap spatial extension

RE23 identifies a sufficient terminal theorem that keeps the Schur saturation intact.

A particularly useful form would be to construct, for all sufficiently large `U` and in the required `V`-range, a new-strip correction

\[
y_{R;U,V}^{\rm ext}\in\mathcal N
\]

such that

\[
\boxed{
\|R_V(\iota x_{R;U,V}^{\rm rev}-y_{R;U,V}^{\rm ext})\|^2
+\|y_{R;U,V}^{\rm ext}\|^2
\le
\|R_Ux_{R;U,V}^{\rm rev}\|^2
+C_R\frac{\log U}{U}.
}
\tag{RE24?}
\]

Then RE23 would immediately imply

\[
\boxed{
\rho^{\rm rev}_{R;U,V}
=O_R\!\left(\frac{\log U}{U}\right).
}
\tag{RE25?}
\]

Roadmap-only label until theoremized:

```text
ROADMAP-COND-REVERSE-CHEAP-SPATIAL-EXTENSION
  type: research-subquestion
  math_status: null
  research_status: open
```

A weaker `o(1)` version of RE24 would already prove reverse-normal stretch decay, though the geometric-chain summability target in PR #66 asks for the quantitative `O(log U/U)` scale.

The already proved collar estimate RE16 is a natural input for constructing `y^{ext}`, but no extension operator with the required residual-cost estimate is currently available.

---

## 8. Relationship between the two reverse-normal routes

The two exact reductions are complementary.

### Route A — newly-resolved `C` energy

It is enough to prove

\[
\sup_{V>U}
\|C_{U,V}x_{R;U,V}^{\rm rev}\|^2
=O_R\!\left(\frac{\log U}{U}\right).
\tag{RE26?}
\]

This route discards saturation and may therefore be stronger than necessary.

### Route B — cheap extension / full Schur cancellation

It is enough to prove RE24.  This route retains the full cancellation represented by `(I+SS^*)^{-1}` and is therefore the preferred next attack.

The present audit does not prove either RE24 or RE26.

---

## 9. Status ledger

New exact local Draft-source bookings:

```text
R43-COND-REVERSE-NORMAL-C-ENERGY-REDUCTION          ✓[M]
R43-COND-REVERSE-NORMAL-OLD-GRAPH-NORMALIZATION     ✓[M]
R43-COND-REVERSE-NORMAL-SCHUR-EXTENSION-VARIATIONAL ✓[M]
```

Retained OPEN:

```text
ROADMAP-COND-REVERSE-NORMAL-STRETCH-DECAY ?[O]
ROADMAP-COND-REVERSE-C-ENERGY-DECAY        ?[O]
ROADMAP-COND-REVERSE-CHEAP-SPATIAL-EXTENSION ?[O]
FD23-UNIF / ROADMAP-COND-FD23-UNIF         ?[O]
GEO / NEW                                  ?[O]
B-FLAGPHASE                                ?[O]
full B-FLAGMOD / B-FLAGDYN                 ?[O]
B-FLAGTIGHT                                ?[O]
B-SIGN / B-ORIENT                          ?[O]
Strong Terminal / C6                       ?[O]
Object-X realization                       ?[O]
RH                                          ?[O]
```

No previously frozen result is modified or promoted.

---

## 10. Next attack

The preferred next calculation is now the extension-cost problem RE24, not a raw global bound on `C_{U,V}`.

A first constructive attempt should:

1. split the residual rows by displacement scale relative to a collar width `r`;
2. use the PR-#64 prime-band collar estimate to control the short-displacement boundary data of `x_rev`;
3. construct a new-strip trial correction only for those short rows;
4. keep the long-displacement part inside the exact martingale-level weights and seek an exponentially summable tail after cancellation;
5. retain the two primitive hard levels separately instead of summing them by an invalid absolute prime estimate.

The target is an explicit trial `y^{ext}` satisfying RE24 with `r\asymp\log U`.  Until such a construction is proved, reverse-normal decay remains open.
