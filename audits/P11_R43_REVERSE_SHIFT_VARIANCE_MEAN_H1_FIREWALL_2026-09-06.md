# P11 / R43 — reverse prime-shift variance, mean penalty, and H1 firewall

**Date:** 2026-09-06  
**Status:** exact local algebraic repair stacked on PR #72; reverse-normal decay remains OPEN  
**Exact parent head:** `25c27bd7f0646e7a63c3cba109336c6414fee72b`  
**Parent PR:** #72 — primitive-band Galerkin graph proxy diagnostic

## 0. Purpose and firewall

PR #70 identifies the exact primitive multichannel least-squares split

\[
F_{\min}
=
\sum_p w_p|x_p-\bar x_w|^2
+
\frac{W}{1+W}|\bar x_w|^2,
\qquad
W=\sum_p w_p,
\qquad
\bar x_w=\frac1W\sum_p w_p x_p.
\tag{VM0}
\]

PR #72 then shows numerically, under old primitive graph normalization, that different profiles have very different optimized extension costs. In particular the graph-normalized constant profile is expensive even though its prime-shift variance is zero.

This note destructively audits the proposed route

```text
small physical H1 derivative of x_rev
    => small prime-shift variance
    => cheap reverse extension
    => reverse-normal stretch decay.
```

The first implication has a clean exact form, but the second implication is false without a separate estimate on the coherent weighted mean. In addition, the current R43 operator stack gives only an L2 contraction for the geometric-mean transport, not an H1 regularization theorem.

No reverse-normal decay, no cheap full P11 extension, no FD23-UNIF, no B-FLAGDYN/TIGHT, no Strong Terminal/C6, no Object-X realization, and no RH claim is made.

---

## 1. Weighted Hilbert variance identity

Let `\mathcal P` be a finite active prime set, with positive weights

\[
w_p>0,
\qquad
W:=\sum_{p\in\mathcal P}w_p,
\qquad
\ell_p:=\log p,
\qquad
\bar\ell:=\frac1W\sum_p w_p\ell_p.
\tag{VM1}
\]

Let `H` be any Hilbert space and let `a_p\in H`. Put

\[
\bar a_w:=\frac1W\sum_p w_pa_p.
\]

Then the standard weighted pair-variance identity is

\[
\boxed{
\frac1{2W}
\sum_{p,q}w_pw_q\|a_p-a_q\|_H^2
=
\sum_p w_p\|a_p-\bar a_w\|_H^2.
}
\tag{VM2}
\]

### Proof

Expanding the square,

\[
\sum_{p,q}w_pw_q\|a_p-a_q\|^2
=
2W\sum_pw_p\|a_p\|^2
-2\left\|\sum_pw_pa_p\right\|^2.
\]

Dividing by `2W` gives exactly the weighted variance about `\bar a_w`. `\square`

### Local Draft booking

```text
R43-COND-WEIGHTED-HILBERT-PAIR-VARIANCE-IDENTITY ✓[M]
```

---

## 2. Exact H1 control of the prime-shift variance

Take `H=L^2(\mathbb R)` and, for a function `x\in H^1(\mathbb R)`, put

\[
a_p:=\tau_{\ell_p}x,
\qquad
(\tau_hx)(z):=x(z-h).
\tag{VM3}
\]

The fundamental theorem of calculus in `L^2` gives

\[
\boxed{
\|\tau_ax-\tau_bx\|_2
\le |a-b|\,\|x'\|_2.
}
\tag{VM4}
\]

Define the integrated weighted prime-shift variance

\[
\mathcal V_{\mathcal P}(x)
:=
\frac1{2W}
\sum_{p,q}w_pw_q
\|\tau_{\ell_p}x-\tau_{\ell_q}x\|_2^2.
\tag{VM5}
\]

Then VM4 gives

\[
\mathcal V_{\mathcal P}(x)
\le
\frac1{2W}
\sum_{p,q}w_pw_q(\ell_p-\ell_q)^2\,\|x'\|_2^2.
\]

The scalar weighted-pair identity yields

\[
\frac1{2W}
\sum_{p,q}w_pw_q(\ell_p-\ell_q)^2
=
\sum_pw_p(\ell_p-\bar\ell)^2.
\]

Hence

\[
\boxed{
\mathcal V_{\mathcal P}(x)
\le
S_{2,\mathcal P}\,\|x'\|_2^2,
\qquad
S_{2,\mathcal P}
:=
\sum_pw_p(\ell_p-\bar\ell)^2.
}
\tag{VM6}
\]

Equivalently, if one normalizes the variance by an additional factor `W`,

\[
\widehat{\mathcal V}_{\mathcal P}(x)
:=\frac1W\mathcal V_{\mathcal P}(x),
\]

then

\[
\widehat{\mathcal V}_{\mathcal P}(x)
\le
\sigma_{\ell,\mathcal P}^2\|x'\|_2^2,
\qquad
\sigma_{\ell,\mathcal P}^2
:=\frac1W S_{2,\mathcal P}.
\tag{VM7}
\]

### Normalization correction

For the PR-#70 least-squares variance term itself, the relevant scale is the **unnormalized** weighted variance in VM2/VM5. Therefore the coefficient is `S_{2,\mathcal P}`, not `S_{2,\mathcal P}/W`.

A sufficient H1 target for

\[
\mathcal V_{\mathcal P}(x)=O(\varepsilon_U)
\]

is therefore

\[
\boxed{
\|x'\|_2^2
=O\!\left(\frac{\varepsilon_U}{S_{2,\mathcal P}}\right),
}
\tag{VM8}
\]

not merely `O(\varepsilon_U)` unless `S_{2,\mathcal P}=O(1)`.

### Local Draft booking

```text
R43-COND-PRIME-SHIFT-H1-VARIANCE-BOUND ✓[M]
```

Scope: abstract finite active-prime set and genuine physical `H^1` regularity. No statement that the actual reverse-normal vector belongs to `H^1` or satisfies VM8.

---

## 3. Exact primitive least-squares decomposition has two gates, not one

At one common new-strip point, PR #70 considers

\[
F(y)=|y|^2+\sum_pw_p|y+x_p|^2.
\tag{VM9}
\]

Its exact minimizer is

\[
y_*=-\frac{W}{1+W}\bar x_w,
\tag{VM10}
\]

and

\[
\boxed{
F(y_*)
=
\underbrace{\sum_pw_p|x_p-\bar x_w|^2}_{\text{incoherent / variance}}
+
\underbrace{\frac{W}{1+W}|\bar x_w|^2}_{\text{coherent / mean penalty}}.
}
\tag{VM11}
\]

Thus small prime-shift variance controls only the first component.

### Exact obstruction

If all `x_p` are equal to one common nonzero value `c`, then

\[
\sum_pw_p|x_p-\bar x_w|^2=0,
\]

but

\[
F(y_*)
=
\frac{W}{1+W}|c|^2>0.
\tag{VM12}
\]

Therefore

\[
\boxed{
\text{prime-shift variance control alone does not imply cheap extension.}
}
\tag{VM13}
\]

The PR-#72 graph-normalized constant proxy is a concrete finite Galerkin manifestation of VM12: it has perfect shift coherence but a non-negligible optimized extension increment.

### Local negative Draft booking

```text
R43-COND-PRIME-SHIFT-VARIANCE-ALONE-CHEAP-EXTENSION-NOGO ✓[M]_neg
```

Scope: the exact primitive multichannel least-squares mechanism. This is not a no-go for structured reverse-normal decay; it says the coherent mean component must also be controlled.

---

## 4. Correct two-component primitive target

For a common integration domain `Z` and a fixed active prime set, define

\[
m_x(z):=\frac1W\sum_pw_p x(z-\ell_p).
\tag{VM14}
\]

The integrated primitive optimized cost splits as

\[
\boxed{
\mathcal E_{\rm prim}(x)
=
\mathcal V_{\mathcal P,Z}(x)
+
\mathcal M_{\mathcal P,Z}(x),
}
\tag{VM15}
\]

where

\[
\mathcal V_{\mathcal P,Z}(x)
:=
\int_Z\sum_pw_p|x(z-\ell_p)-m_x(z)|^2\,dz,
\tag{VM16}
\]

and

\[
\mathcal M_{\mathcal P,Z}(x)
:=
\int_Z\frac{W}{1+W}|m_x(z)|^2\,dz.
\tag{VM17}
\]

Thus a sufficient primitive-channel route requires **both**

\[
\boxed{
\mathcal V_{\mathcal P,Z}(x_{\rm rev})
=O\left(\frac{\log U}{U}\right)
}
\tag{VM18?}
\]

and

\[
\boxed{
\mathcal M_{\mathcal P,Z}(x_{\rm rev})
=O\left(\frac{\log U}{U}\right).
}
\tag{VM19?}
\]

These are separate mechanisms. VM18 is a coherence/modulus problem. VM19 is an amplitude/localization problem for the coherent component.

The full P11 extension still contains depth and nonprimitive terms, so VM18--VM19 are roadmap subtargets, not a full reverse-extension theorem.

Suggested roadmap labels:

```text
ROADMAP-COND-REVERSE-PRIME-SHIFT-VARIANCE-CONTROL   ?[O]
ROADMAP-COND-REVERSE-PRIME-SHIFT-MEAN-CONTROL       ?[O]
ROADMAP-COND-REVERSE-CHEAP-SPATIAL-EXTENSION         ?[O]
ROADMAP-COND-REVERSE-NORMAL-STRETCH-DECAY            ?[O]
```

---

## 5. Geometric-mean transport gives L2 contraction only

PR #57 defines

\[
\mathcal Q_{U,V}
=B_U\#\widetilde B_{U,V},
\qquad
\widetilde B_{U,V}:=\iota^*B_V\iota,
\tag{VM20}
\]

and proves

\[
0<B_U\preceq I,
\qquad
0<\widetilde B_{U,V}\preceq I.
\]

Monotonicity of the operator geometric mean therefore gives only

\[
\boxed{
0<\mathcal Q_{U,V}\preceq I.
}
\tag{VM21}
\]

The stronger inequality

\[
\mathcal Q_{U,V}\preceq B_U
\tag{VM22?}
\]

is **not** available from these premises. It would follow, for example, from the additional Loewner relation `\widetilde B_{U,V}\preceq B_U`, but the current COND analysis does not assert such a relation; indeed the old-conditioning increment is not sign-definite globally.

Most importantly, VM21 is an `L^2` operator-order/norm statement. It contains no Sobolev gain and no commutator estimate with the physical derivative.

No current Draft theorem gives

\[
\|\partial_z\mathcal Q_{U,V}v\|_2
\lesssim \|v\|_2,
\tag{VM23?}
\]

or even

\[
\|\partial_z\mathcal Q_{U,V}v\|_2
\lesssim \|v'\|_2
\tag{VM24?}
\]

uniformly in the terminal parameters.

### Firewall booking

```text
R43-COND-GEOMETRIC-TRANSPORT-L2-NOT-H1-FIREWALL ✓[M]
```

Meaning: the existing proved implication is `Q<=I` in `L^2`; no H1 regularization follows from that statement alone. This is a scope statement, not a theorem that the actual Q fails to preserve any Sobolev space.

---

## 6. The structured hub is a translation filter, not an intrinsic smoother

PR #56 gives, for fixed source support,

\[
v_U(f)=H_U^*E_{R,U}f
=-P_U\sum_{p^k\le e^{2U}}
\sqrt{\log p}\,p^{-3k/4}
D_{k\log p}E_Rf.
\tag{VM25}
\]

At each fixed finite horizon this is a finite linear combination of translations/differences with scalar damping. Translations do not suppress physical frequency: on any regime in which the zero extension has genuine `H^1` regularity,

\[
\partial_z D_sE_Rf
=D_s\partial_zE_Rf.
\tag{VM26}
\]

Thus the factor `p^{-3k/4}` damps channels in prime-power index, but by itself is not a physical low-pass multiplier in the Fourier variable dual to `z`.

Consequently the present formula VM25 does not by itself prove

\[
\|\partial_z H_U^*E_{R,U}f\|_2
=o(1)
\]

for the moving reverse-normal datum.

### Firewall booking

```text
R43-COND-HUB-PRIME-POWER-DAMPING-NOT-PHYSICAL-H1-SMOOTHING ✓[M]
```

Again this records insufficiency of the currently proved mechanism; it does not rule out additional regularity coming from the special source normal or cancellations in the full sum.

---

## 7. Source-normal smoothness is not yet a proved physical H1 theorem

The exact reverse-normal datum from PR #68 is

\[
f_{R;U,V}^{\rm rev}
=(G_{R,\mathrm{cond}}^{U,V})^{-1/2}\varepsilon_R,
\tag{VM27}
\]

and

\[
x_{R;U,V}^{\rm rev}
=\mathcal Q_{U,V}H_U^*E_{R,U}f_{R;U,V}^{\rm rev}.
\tag{VM28}
\]

The current reverse-normal audit treats `\varepsilon_R` as the fixed unit source normal. No theorem in the active stack identifies VM27 with a physical `H^1` function with a terminal-uniform derivative bound, and inverse metric whitening is not automatically Sobolev-neutral.

Therefore the proposed statement

\[
\boxed{
\|\partial_zx_{R;U,V}^{\rm rev}\|_2^2
=O\left(\frac{\log U}{U}\right)
}
\tag{VM29?}
\]

remains an **open additional regularity hypothesis**, not a consequence of the existing R43 stack.

Even if VM29 were proved, it would address only the variance component VM18; one would still need VM19 and the nonprimitive/depth terms required by the full Schur extension.

Suggested optional roadmap label:

```text
ROADMAP-COND-REVERSE-PHYSICAL-H1-REGULARITY ?[O]
```

This is a sufficient-route subquestion, not a newly necessary condition for every possible proof.

---

## 8. Revised preferred attack

The primitive multichannel geometry suggests an orthogonal decomposition in prime-channel space:

```text
weighted channel vector x_p(z)
        |
        +--> coherent component span{(1,1,...)}
        |       controlled by weighted mean m_x(z)
        |
        +--> orthogonal component
                controlled by weighted variance
```

The next proof should therefore attack the two components separately on the actual structured reverse-normal vector:

1. **coherent amplitude:** exploit the special source normal, the fixed-source hub shell, and the `p^{-3k/4}` channel amplitudes to estimate the weighted mean contribution;
2. **incoherent variation:** seek a direct translation-coherence estimate for `QH^*Ef_rev`; an H1 estimate is one possible sufficient route, but not the only one;
3. only after both primitive pieces are controlled should one restore the full martingale-depth/nonprimitive terms in the PR-#68 Schur least-squares functional.

This is weaker than demanding global H1 regularization and more faithful to the exact extension algebra.

---

## 9. Status ledger

New exact/local Draft bookings:

```text
R43-COND-WEIGHTED-HILBERT-PAIR-VARIANCE-IDENTITY          ✓[M]
R43-COND-PRIME-SHIFT-H1-VARIANCE-BOUND                    ✓[M]
R43-COND-PRIME-SHIFT-VARIANCE-ALONE-CHEAP-EXTENSION-NOGO ✓[M]_neg
R43-COND-GEOMETRIC-TRANSPORT-L2-NOT-H1-FIREWALL           ✓[M]
R43-COND-HUB-PRIME-POWER-DAMPING-NOT-PHYSICAL-H1-SMOOTHING ✓[M]
```

Retained OPEN:

```text
ROADMAP-COND-REVERSE-PRIME-SHIFT-VARIANCE-CONTROL ?[O]
ROADMAP-COND-REVERSE-PRIME-SHIFT-MEAN-CONTROL     ?[O]
ROADMAP-COND-REVERSE-PHYSICAL-H1-REGULARITY        ?[O]  optional sufficient route
ROADMAP-COND-REVERSE-CHEAP-SPATIAL-EXTENSION       ?[O]
ROADMAP-COND-REVERSE-NORMAL-STRETCH-DECAY          ?[O]
FD23-UNIF                                           ?[O]
GEO / NEW / phase                                   ?[O]
B-FLAGDYN / B-FLAGTIGHT                            ?[O]
B-SIGN / B-ORIENT                                   ?[O]
Strong Terminal / C6                               ?[O]
Object-X realization / RH                          ?[O]
```

No Registry promotion. Keep Draft.

---

## 10. Destructive review checklist

A fresh review should verify:

1. VM2 with the exact `1/(2W)` normalization;
2. the coefficient in VM6, especially the absence of an extra `1/W` for the PR-#70 unnormalized variance term;
3. the distinction between VM6 and the additionally normalized VM7;
4. the exact mean-penalty obstruction VM11--VM13;
5. that `Q<=I` is the proved PR-#57 order statement, while `Q<=B_U` is not imported;
6. that no Sobolev mapping theorem for `Q` is silently assumed;
7. that `p^{-3k/4}` is channel-index damping and not automatically physical Fourier smoothing;
8. that no physical H1 regularity is inferred from the source-normal/whitening notation;
9. that VM18 and VM19 are roadmap subtargets for the primitive channel only, not a full P11 extension theorem;
10. that reverse-normal decay, FD23, Strong Terminal/C6, Object X, and RH remain OPEN.
