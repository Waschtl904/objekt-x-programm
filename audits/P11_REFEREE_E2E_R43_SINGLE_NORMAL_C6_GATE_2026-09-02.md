# P11 End-to-End Referee R43 — single-normal C6 gate and quantitative edge remainder

Date: 2026-09-02

## Purpose

Start from the frozen R42 codimension-one reduction and attack the **only remaining fixed-pair
Strong-Terminal / C6 degree of freedom** without presupposing its sign.

For fixed
\[
0<R<S
\]
write
\[
W_U:=W_{R,S}^{[U]},
\qquad
K^{T,U}:=K_{R,S}^{T,U}=(W_T)^*W_U.
\]
Frozen R42 proves strong convergence of \(W_U\) on
\[
H_R^0:=\ker\beta_R^{(0)}
\]
and reduces full Strong Terminal to the orbit of one fixed unit normal
\(\varepsilon_R\in(H_R^0)^\perp\).

R43 has four initial tasks:

1. identify \(\varepsilon_R\) inside the already canonical boundary-jet flag;
2. state the remaining C6 observable as the zeroth canonical cross-frame coefficient;
3. test the tempting "jet zero dominates, therefore the normal converges" argument and
   record exactly why the present fixed-vector asymptotics do not justify it;
4. sharpen the R17 near-null estimate from \(o(1)\) to \(O(U^{-1})\), thereby locating the
   next possible higher-order obstruction at the rescaled quantity \(U D_U\).

Status: **AI-GREEN internal exploratory candidate only**.  No freeze, no canonical
\(\checkmark[M]\) promotion, no R37/G4c input.

---

## 1. The last R42 normal is the canonical zeroth jet layer

Work in the odd source graph Hilbert space
\[
\mathcal H_R:=\mathcal K_{X,R}^{-}.
\]
Let
\[
H_R^0=\ker\beta_R^{(0)}.
\]
Frozen R42 chooses the unit Riesz normal \(\varepsilon_R\) by
\[
H_R^0=\varepsilon_R^\perp,
\qquad
\|\varepsilon_R\|_{X,R}=1.
\tag{R43.1}
\]

The earlier canonical jet-flag construction C6a defines
\[
\mathcal H_R^{[m]}
=
\bigcap_{j<m}\ker\beta_R^{(j)}
\]
and the one-dimensional orthogonal layers
\[
\mathcal L_{R,m}
=
\mathcal H_R^{[m]}
\ominus
\mathcal H_R^{[m+1]}.
\]
In particular
\[
\mathcal H_R^{[0]}=\mathcal H_R,
\qquad
\mathcal H_R^{[1]}=H_R^0,
\]
so
\[
\mathcal L_{R,0}
=
\mathcal H_R\ominus H_R^0
=
\mathbb C\varepsilon_R.
\tag{R43.2}
\]

C6a fixes the phase of its unit vector \(e_{R,0}\) by
\[
\beta_R^{(0)}(e_{R,0})>0.
\]
Fix the same positive phase for the Riesz normal.  Then
\[
\boxed{
\varepsilon_R=e_{R,0}.
}
\tag{R43.3}
\]

Thus the last Strong-Terminal degree of freedom is not an arbitrary complement vector: it is
exactly the **zeroth canonical boundary-jet layer**.

---

## 2. Neutral single-scalar formulation

Define
\[
\boxed{
L_{R,S}^{T,U}
:=
\operatorname{Re}
\langle
e_{R,0},
K_{R,S}^{T,U}e_{R,0}
\rangle_{X,R}.
}
\tag{R43.4}
\]
By the exact R5/R39 cross-terminal identity and \(\|e_{R,0}\|=1\),
\[
\boxed{
\|W_Ue_{R,0}-W_Te_{R,0}\|_{X,S}^2
=
2-2L_{R,S}^{T,U}.
}
\tag{R43.5}
\]

Combined with frozen R42 strong convergence on \(H_R^0\),
\[
\boxed{
W_U\text{ is strongly Cauchy}
\iff
L_{R,S}^{T,U}\to1
\quad(T,U\to\infty).
}
\tag{R43.6}
\]

The R43 question is deliberately outcome-neutral:

- \(L^{T,U}\to1\): Strong Terminal holds for the fixed pair;
- if there exist cofinal \(T_n,U_n\) with \(L^{T_n,U_n}\le1-\delta\), \(\delta>0\):
  Strong Terminal fails;
- failure of the two-parameter limit also gives failure of Strong Terminal.

No argument below assumes the first alternative.

In boundary-profile coordinates, (R43.3) says that (R43.4) is exactly the **zeroth canonical
cross-frame coefficient** left unresolved by the earlier C6/C6a Gram-angle firewall.

---

## 3. Exact normal-orbit geometry after R42

Put
\[
w_U:=W_Ue_{R,0}.
\tag{R43.7}
\]
Then
\[
\|w_U\|=1.
\]

Frozen R42 gives an isometric tangential limit
\[
W_U|_{H_R^0}
\xrightarrow[s]{}
W_{R,S}^{(0)}
\]
and therefore every weak cluster \(w\) of \(w_U\) satisfies
\[
w\perp\operatorname{Ran}W_{R,S}^{(0)}.
\tag{R43.8}
\]
R42 also constructs the explicit nonzero Gamma defect direction
\[
d_{R,S}
=
\tau_{S,\infty}
-
\theta_{R,S}
W_{R,S}^{(0)}\tau_{R,\infty},
\qquad
\|d_{R,S}\|^2=1-\theta_{R,S}^2>0,
\]
and proves
\[
w\perp d_{R,S}.
\tag{R43.9}
\]
Hence
\[
\boxed{
w\in
\bigl(\operatorname{Ran}W_{R,S}^{(0)}\bigr)^\perp
\cap
d_{R,S}^{\perp}.
}
\tag{R43.10}
\]

The remaining task is therefore a **no-escape / uniqueness problem for one unit orbit**.

---

## 4. Why zeroth-jet dominance alone does not close R43

The canonical source inclusion is lower triangular in the jet bases:
\[
J_{R,S}e_{R,m}
=
\sum_{k\ge m}a_{k,m}^{R,S}e_{S,k},
\qquad
a_{m,m}^{R,S}>0.
\tag{R43.11}
\]
For fixed smooth vectors, the terminal metric separates the first active jet orders by powers
of \(U^2\).  It is therefore tempting to infer
\[
W_Ue_{R,0}\stackrel?{\longrightarrow}e_{S,0}.
\tag{R43.12}
\]

That inference is **not justified by the current fixed-vector asymptotics**.

Indeed,
\[
W_Ue_{R,0}
=
G_{S,U}^{1/2}
J_{R,S}
G_{R,U}^{-1/2}e_{R,0}.
\tag{R43.13}
\]
The vector
\[
G_{R,U}^{-1/2}e_{R,0}
\]
depends on \(U\).  R42 shows that after normalization its base-Hilbert direction actually
moves into the tangential hard-constraint space.  Tiny higher-jet components invisible in
the fixed graph norm may subsequently be amplified by \(G_{S,U}^{1/2}\) back to order one.

This is exactly the functional-calculus / moving-vector firewall already isolated in R15,
R18 and C6a.  In particular:

\[
\boxed{
\text{fixed-vector jet scale separation}
\not\Rightarrow
W_Ue_{R,0}\to e_{S,0}.
}
\tag{R43.14}
\]

A positive proof of (R43.12) requires a uniform tail theorem or a sufficiently deep
moving-vector expansion.  No such statement is imported here.

---

## 5. Quantitative refinement of the R17 near-null core

Fix smooth odd \(f_0,f_m\) of first jet orders \(0\) and \(m>0\), and put
\[
z_U
=
f_m
-
\frac{\ell_U(f_m)}{\ell_U(f_0)}f_0,
\qquad
\ell_U(z_U)=0.
\tag{R43.15}
\]
The direct boundary expansion gives
\[
z_U-f_m=O(U^{-m})
\tag{R43.16}
\]
in every fixed seminorm on the two-dimensional smooth source block.

R17 proves only
\[
D_U(z_U,z_U)\to0.
\]
We now retain the quantitative information already present in the R16/R17 certificate.

### 5.1 First future-edge certificate

R16 gives, uniformly on the bounded family \(z_U\),
\[
h_U(z_U)
=
\widetilde R_U^*\widehat Y_U^{(1)}
+
r_U
+
Z_U^{\rm quad}
+
Z_U^{\rm tail},
\tag{R43.17}
\]
with
\[
\boxed{
\|\widehat Y_U^{(1)}\|^2=O(U^{-1}).
}
\tag{R43.18}
\]

The source quadrature error can be kept quantitative.  The R1 source-representer estimate
uses cells of width
\[
|I|\ll e^{-\frac45(U-r)}
\]
and
\[
\|\partial_r\Phi_U(r)\|
\ll
\frac{e^{(U-2r)/2}}{\sqrt{1+(U-2r)_+}}
\]
uniformly on the fixed two-dimensional family.  Hence the \(k_U\)-part of the summed
quadrature error is
\[
O\!\left(Ue^{-3U/10}\right).
\tag{R43.19}
\]
The constant part is
\[
O(|K_U|e^{-2U/5}).
\tag{R43.20}
\]
The full-rest lift satisfies
\[
\|E_U^{\rm fut}\|
\ll
\sqrt U\,e^{-U/2},
\]
so with (R43.18) its induced source tail is exponentially small as well.

Thus once \(K_U\) is controlled polynomially, both
\[
Z_U^{\rm quad},\quad Z_U^{\rm tail}
\]
are exponentially small up to harmless powers of \(U\).

### 5.2 Quantitative convergence of the bounded hub remainder

R17 writes the ambient limiting remainder as
\[
h_{\rm rem,\infty}
=
\mathcal H_{\rm rem,\infty}^*f_m
\]
with a finite low-primitive block plus the absolutely convergent series
\[
\sum_p\sum_{k\ge2}
\sqrt{\log p}\,p^{-3k/4}
D_{k\log p}^*E_Rf_m.
\tag{R43.21}
\]

For \(L>0\), the coefficient tail with \(k\log p>L\) satisfies
\[
\sum_{\substack{p,\ k\ge2\\k\log p>L}}
\sqrt{\log p}\,p^{-3k/4}
\ll
(1+L)^C e^{-L/4}
\tag{R43.22}
\]
for a harmless fixed \(C\).  The worst exponent is the \(k=2\) tail; all \(k\ge3\)
decay faster.

Since translations preserve \(L^1\) and \(L^2\), (R43.16) and (R43.22) give
\[
\boxed{
\|E_Uh_U^{\rm rem}(z_U)-h_{\rm rem,\infty}\|_{L^1\cap L^2}
=
O(U^{-m})+O(e^{-cU})
}
\tag{R43.23}
\]
for some \(c=c_R>0\).

Because \(h_{\rm rem,\infty}\) has zero integral, R17's identity
\[
K_U
=
-\langle h_U^{\rm rem}(z_U),1_U\rangle
\]
therefore sharpens to
\[
\boxed{
K_U=O(U^{-m})+O(e^{-cU}).
}
\tag{R43.24}
\]
Consequently
\[
\left\|
\frac{K_U}{2U}1_U
\right\|_2^2
=
O(U^{-2m-1})+O(e^{-cU}).
\tag{R43.25}
\]

### 5.3 A growing finite mean-zero truncation

Let \(g_U\) be the finite partial sum of (R43.21) containing every translation difference
with shift at most \(U/2\), together with the finite low-primitive block.

Then:

- \(g_U\) is smooth, even and has zero integral;
- its \(L^1,L^2,C^1\) norms are uniformly bounded, because the coefficient series is
  absolutely summable in the corresponding translated seminorms;
- its support lies inside
  \[
  [-R-U/4,R+U/4];
  \]
- by (R43.22),
  \[
  \|h_{\rm rem,\infty}-g_U\|_2=O(e^{-cU}).
  \tag{R43.26}
  \]

The R17 future-edge absorption can now be applied **uniformly to this growing truncation**.
Indeed
\[
k_{g_U}^{(U)}(t)=2g_U(U-t),
\]
and directly
\[
e^{-U}\int_0^U
e^{t/2}|k_{g_U}^{(U)}(t)|^2dt
=
4e^{-U/2}
\int_0^U e^{-x/2}|g_U(x)|^2dx
\ll e^{-U/2}.
\tag{R43.27}
\]
Its active cells remain in a fixed positive fraction of the future region
(\(U-r\ge U/2-O_R(1)\)); the uniform \(C^1\) bound and the same short-interval quadrature
therefore give exponentially small source error and full-rest tail.

Hence there exist \(Y_U^{(2)}\) and \(E_U^{(2)}\) such that
\[
g_U
=
\widetilde R_U^*Y_U^{(2)}
+
E_U^{(2)},
\tag{R43.28}
\]
with
\[
\boxed{
\|Y_U^{(2)}\|^2+\|E_U^{(2)}\|_2^2
=
O(e^{-cU}).
}
\tag{R43.29}
\]

### 5.4 Quantitative dual bound

Combine (R43.17) and (R43.28).  By (R43.23)--(R43.26),
\[
\|r_U-g_U\|_2
=
O(U^{-m})+O(e^{-cU}).
\tag{R43.30}
\]
Insert
\[
Y=\widehat Y_U^{(1)}+Y_U^{(2)}
\]
into the exact dual formula
\[
\sigma_U(Jz_U)
=
\inf_Y
\left(
\|h_U(z_U)-\widetilde R_U^*Y\|_2^2+\|Y\|^2
\right).
\]
Using (R43.18)--(R43.20), (R43.29)--(R43.30),
\[
D_U(z_U,z_U)
=
\sigma_U(Jz_U)
\ll
U^{-1}+U^{-2m}+e^{-cU}.
\]
Therefore
\[
\boxed{
D_U(z_U,z_U)=O(U^{-1}).
}
\tag{R43.31}
\]

This strictly sharpens the frozen R17 statement \(D_U\to0\), but does not alter R17
retroactively.

---

## 6. What the quantitative upgrade does and does not buy

For the first residual jet \(m=1\), which is the layer entering R41/R42,
\[
D_U(z_U,z_U)=O(U^{-1}).
\tag{R43.32}
\]
Thus at the next rescaled order the Schur core is no longer an unspecified \(o(1)\): it is at
most exactly the scale that can compete with the \(U^{-1}\) correction of the affine Gamma
minimizer.

The next sharp scalar is therefore
\[
\boxed{
\mathcal D_U
:=
U\,D_U(z_U,z_U).
}
\tag{R43.33}
\]
R43 currently proves only
\[
0\le\mathcal D_U\le C.
\tag{R43.34}
\]

Three possibilities remain:

1. \(\mathcal D_U\to0\): the third layer is purely Gamma/jet to first correction;
2. \(\mathcal D_U\to d>0\) (or a nontrivial quadratic form on the constrained first-jet
   layer): a genuine future-edge form enters the third layer;
3. \(\mathcal D_U\) has multiple clusters: the higher-order normal geometry may itself
   retain terminal memory.

Therefore
\[
\boxed{
\text{the next higher-order gate is the bounded family }U D_U,
\text{ not the old unscaled }D_U.
}
\tag{R43.35}
\]

No value or limit for (R43.33) is claimed.

---

## 6A. The scalar \(UD_U\) is not itself a relative gauge diagnostic

The quantitative upgrade (R43.31) makes
\[
UD_U(z_U,z_U)
\]
bounded, but the frozen R17 source-compatibility identity remains exact at every \(U\).

If \(0<R<S\), the same fixed smooth pair is transported by zero extension and
\[
z_U^S=J_{R,S}z_U^R.
\]
R17 gives identically
\[
D_U^{(S)}(z_U^S,z_U^S)
=
D_U^{(R)}(z_U^R,z_U^R).
\]
Multiplying by \(U\) changes nothing:
\[
\boxed{
U D_U^{(S)}(z_U^S,z_U^S)
=
U D_U^{(R)}(z_U^R,z_U^R).
}
\tag{R43.36}
\]

Therefore even a complete scalar limit
\[
UD_U(z_U,z_U)\to d
\]
would **not by itself** distinguish the source and target polar geometries.  This is the
third-layer version of the R17/R18 source-compatible Gram firewall.

Hence the correct possible third-layer object must retain off-block information.

### Finite-block rescaled edge-form candidate

Let \(E\subset C_c^\infty((-R,R))_{\rm odd}\cap H_R^0\) be a fixed finite-dimensional
smooth subspace.  Choose a fixed smooth \(f_{0,R}\) with
\[
\beta_R^{(0)}(f_{0,R})\ne0
\]
and define the exact terminal boundary-null correction
\[
\mathcal N_{R,U}y
:=
y-
\frac{\ell_U(y)}{\ell_U(f_{0,R})}f_{0,R},
\qquad y\in E.
\tag{R43.37}
\]
Then
\[
\ell_U(\mathcal N_{R,U}y)=0,
\qquad
\mathcal N_{R,U}y\to y.
\]

The R16 finite-dimensional uniformization together with the quantitative R43 refinement
is uniform on the unit sphere of \(E\).  Consequently
\[
D_U(\mathcal N_{R,U}y,\mathcal N_{R,U}y)
\le
\frac{C_E}{U}\|y\|^2
\qquad(y\in E)
\tag{R43.38}
\]
for all sufficiently large \(U\).

Define the positive sesquilinear form
\[
\boxed{
\mathfrak e_{R,U}^{E}(y,z)
:=
U\,
D_U(
\mathcal N_{R,U}y,
\mathcal N_{R,U}z
).
}
\tag{R43.39}
\]
Then
\[
0\le \mathfrak e_{R,U}^{E}\le C_E I_E.
\tag{R43.40}
\]
Thus every terminal sequence has a subsequence along which the finite matrix of
\(\mathfrak e_{R,U}^{E}\) converges to a positive semidefinite form on \(E\).

For source-compatible comparison, choose at level \(S\)
\[
f_{0,S}:=J_{R,S}f_{0,R}.
\]
Terminal compatibility of \(\ell_U\) gives
\[
\mathcal N_{S,U}J_{R,S}
=
J_{R,S}\mathcal N_{R,U}
\quad\text{on }E,
\tag{R43.41}
\]
and terminality of \(D_U\) gives the exact pullback identity
\[
\boxed{
\mathfrak e_{S,U}^{J E}(Jy,Jz)
=
\mathfrak e_{R,U}^{E}(y,z).
}
\tag{R43.42}
\]

So any third-order edge layer extracted from these rescaled forms is itself
source-compatible on the nested block.  The genuinely new relative information can only
appear in its coupling to the target complement before square-root/polar functional
calculus.

This identifies the correct third-layer analogue of the R18 frontier:
\[
\boxed{
\text{not the scalar }UD_U,
\quad\text{but a rescaled edge form plus its target off-block.}
}
\tag{R43.43}
\]

The definition (R43.39) is presently a finite-block exploratory device.  Independence of the
choice of the correction vector \(f_{0,R}\), existence of a global closed limiting edge form,
and control of its target off-block are all open.

---

## 7. Current R43 decision tree

The shortest presently justified routes to the final C6 scalar are:

### Route A — direct normal cross-kernel

Attack
\[
L_{R,S}^{T,U}
=
\operatorname{Re}
\langle e_{R,0},K^{T,U}e_{R,0}\rangle
\]
directly using the exact metric formula
\[
K^{T,U}
=
G_{R,T}^{-1/2}J^*
G_{S,T}^{1/2}G_{S,U}^{1/2}
JG_{R,U}^{-1/2}.
\]
This is the exact Strong-Terminal observable, but currently retains full square-root
functional calculus.

### Route B — normal tail compactness

Prove a uniform canonical-jet tail estimate for the single orbit \(W_Ue_{R,0}\).  Together
with convergence of every finite coordinate, such a tail estimate would prevent weak escape
and force strong convergence.

### Route C — third hard-constraint layer

Determine the limit structure of \(U D_U\) and combine it with the next boundary coefficient
\[
\frac{3}{8U^2}\beta^{(2)}
\]
to obtain the next moving-vector asymptotic beyond R42.  This is the first route on which the
remaining normal channel can enter without violating the R42 eta-blindness theorem.

At the present head none of A--C is yet closed.

---

## 8. Governance / firewall

R43 uses:

- frozen R39: exact cross-terminal Cauchy criterion;
- frozen R42: codimension-one reduction and tangential strong terminal limit;
- canonical C4/C6/C6a: complete jet flag and canonical jet ONB;
- canonical R1/R16/R17: future-edge certificate and vanishing near-null core.

It uses no R37/G4c conclusion.

R43 does **not** prove:

- \(L_{R,S}^{T,U}\to1\);
- convergence or nonconvergence of \(W_Ue_{R,0}\);
- convergence of \(a_U\);
- a limit for \(UD_U\);
- full Strong Terminal / C6;
- Object X;
- RH.

Current booking:
\[
\boxed{
\text{R43 Phase I: AI-GREEN internal exploratory candidate only.}
}
\]
