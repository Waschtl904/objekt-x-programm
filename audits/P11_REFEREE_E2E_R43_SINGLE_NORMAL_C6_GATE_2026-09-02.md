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

## 3A. Intermediate-radius orthogonality and a fixed Gamma cyclicity gate

There is a second exact reduction which uses the finite-terminal source cocycle.

Fix an intermediate source radius
\[
R<Q<S.
\]
Let
\[
\tau_{X,U}\to\tau_{X,\infty}\in H_X^0
\]
be the frozen R42 future-normal limit at level \(X\), and define the fixed target vector
\[
\boxed{
g_{Q,S}
:=
W_{Q,S}^{(0)}\tau_{Q,\infty}
\in H_S^0.
}
\tag{R43.10a}
\]

Frozen R42 gives
\[
W_{Q,S}^{[U]}\tau_{Q,U}
\longrightarrow
W_{Q,S}^{(0)}\tau_{Q,\infty}
=
g_{Q,S}
\tag{R43.10b}
\]
strongly: use \(\tau_{Q,U}\to\tau_{Q,\infty}\), the isometry bound on \(W_{Q,S}^{[U]}\),
and R42.51 on the fixed tangential vector \(\tau_{Q,\infty}\).

The same-terminal source cocycle gives
\[
W_{R,S}^{[U]}
=
W_{Q,S}^{[U]}W_{R,Q}^{[U]}.
\tag{R43.10c}
\]
Hence, with \(w_U=W_{R,S}^{[U]}\varepsilon_R\),
\[
\begin{aligned}
\langle
w_U,
W_{Q,S}^{[U]}\tau_{Q,U}
\rangle
&=
\langle
W_{R,Q}^{[U]}\varepsilon_R,
\tau_{Q,U}
\rangle\\
&=
\langle
\varepsilon_R,
(W_{R,Q}^{[U]})^*\tau_{Q,U}
\rangle.
\end{aligned}
\]
R42.32 for the pair \(R<Q\) gives exactly
\[
(W_{R,Q}^{[U]})^*\tau_{Q,U}
=
\theta_{R,Q}(U)\tau_{R,U},
\]
so
\[
\langle
w_U,
W_{Q,S}^{[U]}\tau_{Q,U}
\rangle
=
\theta_{R,Q}(U)
\langle\varepsilon_R,\tau_{R,U}\rangle.
\tag{R43.10d}
\]
But
\[
\tau_{R,U}\to\tau_{R,\infty}\in H_R^0
=
\varepsilon_R^\perp.
\]
Therefore
\[
\boxed{
\langle w_U,g_{Q,S}\rangle
\longrightarrow0
\qquad
\text{for every }R<Q<S.
}
\tag{R43.10e}
\]

Thus every weak cluster \(w\) of the last normal orbit satisfies, in addition to
(R43.8)--(R43.10),
\[
w\perp g_{Q,S}
\qquad
\forall Q\in(R,S).
\tag{R43.10f}
\]

Define the fixed subspace
\[
\boxed{
\mathscr C_{R,S}
:=
\overline{
\operatorname{Ran}W_{R,S}^{(0)}
+
\operatorname{span}\{g_{Q,S}:R<Q<S\}
}.
}
\tag{R43.10g}
\]
Then
\[
\boxed{
\text{every weak cluster of }w_U
\text{ lies in }\mathscr C_{R,S}^{\perp}.
}
\tag{R43.10h}
\]

Since every generator in (R43.10g) belongs to \(H_S^0\),
\[
\mathscr C_{R,S}\subseteq H_S^0.
\]

### Fixed Gamma cyclicity gate

Under the frozen R42 Gamma-whitening unitary
\[
\mathcal J_S^\Gamma:H_S^0\to V_S,
\]
one has
\[
\mathcal J_S^\Gamma
\operatorname{Ran}W_{R,S}^{(0)}
=
Y_{R,S}V_R
\]
and, because
\[
\tau_{Q,\infty}
=
(\mathcal J_Q^\Gamma)^*\zeta_Q,
\]
\[
\mathcal J_S^\Gamma g_{Q,S}
=
Y_{Q,S}\zeta_Q.
\]
Therefore
\[
\boxed{
\mathscr C_{R,S}=H_S^0
}
\tag{R43.10i}
\]
is equivalent to the purely fixed constrained-Gamma density statement
\[
\boxed{
\overline{
Y_{R,S}V_R
+
\operatorname{span}\{
Y_{Q,S}\zeta_Q:R<Q<S
\}
}
=
V_S.
}
\tag{R43.10j}
\]

No terminal parameter occurs in (R43.10j).

If this **Gamma cyclicity gate** holds, every weak cluster of \(w_U\) must lie in
\[
(H_S^0)^\perp=\mathbb C\varepsilon_S.
\tag{R43.10k}
\]
In that case the full Strong-Terminal question reduces further to the one-parameter scalar
\[
b_U:=\langle w_U,\varepsilon_S\rangle:
\]
\[
\boxed{
\text{under (R43.10j), }
W_Ue_{R,0}\text{ converges strongly}
\iff
b_U\to b,\quad |b|=1.
}
\tag{R43.10l}
\]

The implication uses weak convergence plus equality of the limiting norm.  No sign or phase
for \(b\) is asserted.

At the present head, (R43.10j) is **open**.  Strict monotonicity
\(\gamma_Q<\gamma_S\) proves that the individual residual directions are nonzero, but by
itself does not prove cyclicity/density of their continuum family.

This is nevertheless a new separation of the last gate:
\[
\boxed{
\text{terminal normal escape}
\quad\Longrightarrow\quad
\text{fixed Gamma cyclicity question}
+
\text{one residual scalar phase/no-escape question}.
}
\tag{R43.10m}
\]

---

## 3B. Intrinsic Gamma projection nest

The terminal-free cyclicity gate R43.10j has a simpler intrinsic form.

Let
\[
\mathscr G_X^0
:=
\bigl(H_X^0,\mathfrak c_{\Gamma,X}\bigr)
\]
denote the constrained Gamma Hilbert space, and define
\[
\mathcal U_X^\Gamma
:
\mathscr G_X^0\longrightarrow V_X,
\qquad
\mathcal U_X^\Gamma f
:=
L_X^{1/2}B_X^{1/2}f.
\tag{R43.10n}
\]
By definition of the transported Gamma form,
\[
\|\mathcal U_X^\Gamma f\|^2
=
\mathfrak c_{\Gamma,X}[f],
\]
so \(\mathcal U_X^\Gamma\) is unitary onto \(V_X\).

Let \(g_X\in\mathscr G_X^0\) be the Gamma-Riesz vector from frozen R42.26c:
\[
\mathfrak c_{\Gamma,X}[f,g_X]
=
\beta_X^{(1)}(f).
\]
Then
\[
\boxed{
q_{1,X}
=
\mathcal U_X^\Gamma g_X.
}
\tag{R43.10o}
\]
Indeed, for \(f\in H_X^0\),
\[
\begin{aligned}
\langle
\mathcal U_X^\Gamma f,q_{1,X}
\rangle
&=
\langle
L_X^{1/2}B_X^{1/2}f,
L_X^{-1/2}b_{1,X}
\rangle\\
&=
\langle B_X^{1/2}f,b_{1,X}\rangle\\
&=
\beta_X^{(1)}(f)\\
&=
\langle
\mathcal U_X^\Gamma f,
\mathcal U_X^\Gamma g_X
\rangle,
\end{aligned}
\]
and surjectivity of \(\mathcal U_X^\Gamma\) gives (R43.10o).

For \(0<Q<S\), the frozen R38/R42 Gamma isometry satisfies
\[
\boxed{
Y_{Q,S}\mathcal U_Q^\Gamma
=
\mathcal U_S^\Gamma J_{Q,S}.
}
\tag{R43.10p}
\]
This is an exact algebraic cancellation:
\[
\begin{aligned}
Y_{Q,S}\mathcal U_Q^\Gamma
&=
L_S^{1/2}
\bigl(B_S^{1/2}J_{Q,S}B_Q^{-1/2}\bigr)
L_Q^{-1/2}
L_Q^{1/2}B_Q^{1/2}\\
&=
L_S^{1/2}B_S^{1/2}J_{Q,S}.
\end{aligned}
\]

Let
\[
P_Q^\Gamma
:
\mathscr G_S^0\to J_{Q,S}\mathscr G_Q^0
\]
be Gamma-orthogonal projection.  Frozen R42.26c--d and source compatibility give
\[
\boxed{
P_Q^\Gamma g_S
=
J_{Q,S}g_Q.
}
\tag{R43.10q}
\]
Consequently
\[
\boxed{
Y_{Q,S}\zeta_Q
=
-
\frac{
\mathcal U_S^\Gamma P_Q^\Gamma g_S
}{
\sqrt{\gamma_Q}
}.
}
\tag{R43.10r}
\]
Likewise
\[
Y_{R,S}V_R
=
\mathcal U_S^\Gamma
J_{R,S}\mathscr G_R^0.
\tag{R43.10s}
\]

Hence R43.10j is equivalent to the single-vector nest-cyclicity statement
\[
\boxed{
\overline{
J_{R,S}\mathscr G_R^0
+
\operatorname{span}
\{P_Q^\Gamma g_S:R<Q<S\}
}
=
\mathscr G_S^0.
}
\tag{R43.10t}
\]

Thus the continuum family in R43.10j consists of projections of **one fixed vector**
\(g_S\) onto one fixed increasing Gamma nest.

---

## 3C. The scalar nest measure is exactly \(\gamma_Q\)

The projection identity (R43.10q) gives
\[
\boxed{
\|P_Q^\Gamma g_S\|_{\Gamma,S}^2
=
\|g_Q\|_{\Gamma,Q}^2
=
\gamma_Q.
}
\tag{R43.10u}
\]
For \(0<Q_1<Q_2<S\), nested orthogonal projections satisfy
\[
P_{Q_1}^\Gamma P_{Q_2}^\Gamma=P_{Q_1}^\Gamma,
\]
so
\[
\boxed{
\|
(P_{Q_2}^\Gamma-P_{Q_1}^\Gamma)g_S
\|_{\Gamma,S}^2
=
\gamma_{Q_2}-\gamma_{Q_1}.
}
\tag{R43.10v}
\]
Frozen R42.26l therefore says precisely that the scalar spectral measure of \(g_S\)
for the radius nest charges every nonempty radius interval.

Strict increase alone is not enough for cyclicity.  Two abstract obstructions must be kept
separate:

1. a nest may have multiplicity \(>1\), in which case one vector cannot generate all
   multiplicity channels;
2. even in a multiplicity-one model, a vector can vanish on a positive-measure set with
   empty interior, so its cumulative norm can still increase on every interval without
   being cyclic.

The next subsection removes the second obstruction at the level of the natural radius
parameter.

---

## 3D. Real-analyticity of the intrinsic Gamma ratio function

We now show that
\[
Q\longmapsto\gamma_Q
\]
is real analytic on \((0,\infty)\).

### Fixed-domain dilation

Let
\[
(D_Qh)(u)
=
Q^{-1/2}h(u/Q),
\qquad
u\in(-Q,Q),
\tag{R43.10w}
\]
for odd \(h\) on \((-1,1)\).  Under the binding Fourier convention,
\[
\widehat{E_QD_Qh}(\xi)
=
Q^{1/2}\widehat{E_1h}(Q\xi).
\]
Therefore the pulled-back Gamma form is
\[
\boxed{
a_Q[h,k]
=
\frac1{2\pi}
\int_{\mathbb R}
m_\Gamma(\eta/Q)
\widehat{E_1h}(\eta)
\overline{\widehat{E_1k}(\eta)}
\,d\eta.
}
\tag{R43.10x}
\]

Fix a compact interval
\[
I=[Q_-,Q_+]\Subset(0,\infty).
\]
R33.3 and monotonicity of the positive R33 series imply uniform two-sided comparability
of
\[
m_\Gamma(\eta/Q),
\qquad Q\in I,
\]
with any one reference weight \(m_\Gamma(\eta/Q_*)\), \(Q_*\in I\).
Hence all forms \(a_Q\), \(Q\in I\), have one common Hilbert form domain
\(\mathscr V_I\), with equivalent norms.

The exact R33 series is
\[
m_\Gamma(\xi)
=
1+
\sum_{n=0}^\infty
\frac{\xi^2/4}{
y_n\bigl(y_n^2+\xi^2/4\bigr)
},
\qquad
y_n=n+\frac14.
\tag{R43.10y}
\]
For \(Q\) in a sufficiently small complex neighborhood of \(I\) contained in a fixed
sector
\[
|\arg Q|<\frac{\pi}{4},
\qquad
|Q|\ge \frac{Q_-}{2},
\]
every summand in
\[
m_\Gamma(\eta/Q)
\]
is holomorphic in \(Q\), and its denominator stays uniformly away from its purely
imaginary zero set.  On that neighborhood the series and all local \(Q\)-derivatives
are dominated, in form norm, by a constant multiple of one reference R33 weight.
At this point one convention matters.  On the real axis, \(a_Q\) is a Hermitian form,
so its Hilbert-space Riesz identification is conjugate-linear in one slot and must **not**
be treated as a holomorphic complex-linear operator.  For analyticity we instead pass to
the underlying real Hilbert form.

Let \(\mathscr V_I^{\mathbb R}\) be the real-valued odd form domain.  There \(a_Q\) is
real symmetric.  Complexify \(\mathscr V_I^{\mathbb R}\) and extend this real symmetric
form complex-bilinearly.  Denote the extension by
\[
\mathfrak a_Q^{\mathbb C}[h,k].
\]
Equivalently, in Fourier coordinates one may use
\[
\mathfrak a_Q^{\mathbb C}[h,k]
=
\frac1{2\pi}
\int_{\mathbb R}
m_\Gamma(\eta/Q)
\widehat{E_1h}(\eta)
\widehat{E_1k}(-\eta)
\,d\eta.
\]
For real \(Q\) and real \(h,k\) this is exactly the original Gamma form.  The same
form-norm estimates therefore show that its associated complex-linear operator
\[
A(Q):
\mathscr V_I^{\mathbb C}
\longrightarrow
(\mathscr V_I^{\mathbb C})'
\]
into the **complex-linear dual** is operator-norm holomorphic:
\[
\boxed{
Q\longmapsto A(Q)
\text{ is holomorphic.}
}
\tag{R43.10z}
\]
\[
\boxed{
\text{Complexify the real symmetric form, not the sesquilinear Hilbert-Riesz map.}
}
\tag{R43.10z0}
\]
All complex-analytic uses of \(A(Q)\) below refer to this bilinear complexification.
The ordinary sesquilinear Hilbert-Riesz map is used only on the positive real axis.

The pulled-back jet functionals
\[
b_{m,Q}(h)
:=
\beta_Q^{(m)}(D_Qh)
=
Q^{1/2}
\int_{-1}^{1}
h(y)\phi_m(Qy)\,dy
\tag{R43.10aa}
\]
are holomorphic \((\mathscr V_I^{\mathbb C})'\)-valued functions of \(Q\), because the
real jet functionals are extended complex-linearly and the explicit
kernels
\[
\phi_m(u)=\operatorname{sgn}(u)I_m(|u|)
\]
are entire in the radial variable away from the fixed sign and are uniformly bounded on
compact \(Q\)-sets.

At every real \(Q_0\in I\), coercivity of the real Gamma form makes the complexified
operator \(A(Q_0)\) an isomorphism.  By (R43.10z) and openness of the invertible group,
\(A(Q)\) remains invertible in a complex neighborhood of \(Q_0\), and
\[
A(Q)^{-1}
\]
is holomorphic there.
Put
\[
u_{j,Q}:=A(Q)^{-1}b_{j,Q},
\qquad j=0,1.
\tag{R43.10ab}
\]
Here the real jet functionals have been extended complex-linearly to the complexified real
form domain.  For positive real \(Q\), all coefficients are real, hence \(u_{j,Q}\) is
real and is exactly the usual Gamma-Riesz vector for the corresponding real functional.
On the real axis,
\[
d_Q:=b_{0,Q}(u_{0,Q})>0.
\]
Therefore locally
\[
\widetilde g_Q
=
u_{1,Q}
-
\frac{b_{0,Q}(u_{1,Q})}{d_Q}\,u_{0,Q}
\tag{R43.10ac}
\]
is holomorphic in the complexified bilinear problem, while for positive real \(Q\) it is
exactly the pulled-back constrained Gamma-Riesz vector:
\[
D_Q\widetilde g_Q=g_Q.
\]
Hence
\[
\boxed{
\gamma_Q
=
b_{1,Q}(\widetilde g_Q)
}
\tag{R43.10ad}
\]
is the restriction of a holomorphic scalar function and is therefore real analytic on
\((0,\infty)\).  The off-real analytic continuation is **not** being interpreted as a
Hilbert norm; the norm identity is asserted only for real \(Q>0\).

Combining this with the frozen strict monotonicity
\[
\gamma_{Q_1}<\gamma_{Q_2}
\qquad(Q_1<Q_2)
\]
gives
\[
\gamma_Q'\ge0
\]
everywhere.  Since \(\gamma'\) is real analytic and cannot vanish identically on any
nonempty interval,
\[
\boxed{
\gamma_Q'>0
\quad
\text{for all }Q>0
\text{ except at most a discrete set.}
}
\tag{R43.10ae}
\]
Thus
\[
\boxed{
d\nu_{g_S}(Q)
:=
d\|P_Q^\Gamma g_S\|_{\Gamma,S}^2
=
\gamma_Q'\,dQ
}
\tag{R43.10af}
\]
has strictly positive density for Lebesgue-a.e. radius.

The proof of (R43.10z), especially the uniform complex-sector domination of the R33
series in the common form norm, is a new analytic step and requires independent review
before any freeze.

---

## 3E. Cyclicity is reduced to one Gamma-nest multiplicity theorem

Define the constrained Gamma radius nest on the interval \((R,S)\):
\[
\mathcal N_{R,S}^\Gamma
:=
\{
P_Q^\Gamma-P_R^\Gamma:
R\le Q\le S
\}
\quad
\text{on }
\bigl(J_{R,S}\mathscr G_R^0\bigr)^\perp.
\tag{R43.10ag}
\]

Suppose this nest has a multiplicity-one Lebesgue model, i.e. there exists a unitary
\[
\mathcal W_{R,S}
:
\bigl(J_{R,S}\mathscr G_R^0\bigr)^\perp
\longrightarrow
L^2((R,S),dQ)
\]
such that
\[
\mathcal W_{R,S}
(P_Q^\Gamma-P_R^\Gamma)
\mathcal W_{R,S}^*
=
M_{1_{(R,Q]}}.
\tag{R43.10ah}
\]
Then by (R43.10v) and (R43.10af),
\[
\left|
\mathcal W_{R,S}
(I-P_R^\Gamma)g_S
\right|^2
=
\gamma_Q'
\quad\text{a.e. in the radius variable}.
\]
The right side is positive almost everywhere by (R43.10ae).  Hence
\[
(I-P_R^\Gamma)g_S
\]
is cyclic for the multiplication nest, and therefore
\[
\boxed{
\text{(R43.10ah)}
\Longrightarrow
\text{R43.10t}
\Longleftrightarrow
\text{R43.10j}.
}
\tag{R43.10ai}
\]

Thus the terminal-free Gamma-cyclicity problem is sharpened to one structural theorem:

\[
\boxed{
\textbf{GC-M1: }
\mathcal N_{R,S}^\Gamma
\text{ has multiplicity one in the natural radius/Lebesgue model.}
}
\tag{R43.10aj}
\]

The scalar-support part is already supplied by the analytic and strictly increasing
function \(\gamma_Q\).

### Why GC-M1 cannot be omitted

Strict increase of \(\gamma_Q\) alone does not prove cyclicity.  For example, in the
multiplicity-two standard nest
\[
L^2((R,S),dQ;\mathbb C^2)
\]
the vector
\[
g(Q)=(1,0)
\]
has strictly increasing cumulative norm on every interval but its nest-cyclic span misses
the entire second component.

Therefore no inference
\[
\gamma_{Q_1}<\gamma_{Q_2}\ \forall Q_1<Q_2
\Longrightarrow
\text{R43.10j}
\]
is permitted without a multiplicity theorem.

### Candidate routes to GC-M1

The exact Gamma geometry offers two natural routes, neither yet proved in the repository:

1. **weighted Paley--Wiener / canonical-system route:** after Fourier transform,
   \(\mathfrak c_{\Gamma,Q}\) is the exact R33-weighted Paley--Wiener norm on entire
   functions of type \(Q\); prove that the odd, one-constraint radius chain remains
   multiplicity one;
2. **triangular spectral-factor route:** factor the positive scalar R33 symbol and construct
   an explicit radius-triangular whitening of the constrained Gamma form.  A triangular
   factor with triangular inverse would identify the nest with the standard Volterra
   multiplicity-one nest.

These are now fixed, terminal-free operator-theoretic questions.

---

## 3F. Explicit repair of the R43.10z holomorphy gate

The second external review correctly isolated the missing point in R43.10z: the complex
sector must be controlled uniformly in both the spectral variable and the R33 summation
index.  We now supply that estimate explicitly.

Write
\[
m_Q(\eta)
:=
m_\Gamma(\eta/Q)
=
1+\sum_{n\ge0}s_n(Q,\eta),
\]
where, after multiplying numerator and denominator of R43.10y by \(4Q^2\),
\[
\boxed{
s_n(Q,\eta)
=
\frac{\eta^2}{
y_n\bigl(\eta^2+4y_n^2Q^2\bigr)
},
\qquad
y_n=n+\frac14.
}
\tag{R43.10ak}
\]

Fix a real reference point \(Q_0>0\).  Choose \(0<\rho<Q_0/4\), small enough that
the closed disk
\[
\mathbb D_{Q_0}:=\{Q:|Q-Q_0|\le2\rho\}
\]
lies in the sector
\[
|\arg Q|<\frac{\pi}{4}.
\]
There are constants \(c_0,C_0>0\), depending only on this disk, such that
\[
\operatorname{Re}Q^2\ge c_0Q_0^2,
\qquad
|Q|\le C_0Q_0
\qquad(Q\in\mathbb D_{Q_0}).
\tag{R43.10al}
\]
For real \(\eta\) and every \(n\ge0\),
\[
\begin{aligned}
\left|
\eta^2+4y_n^2Q^2
\right|
&\ge
\operatorname{Re}
\bigl(\eta^2+4y_n^2Q^2\bigr)\\
&=
\eta^2+4y_n^2\operatorname{Re}Q^2\\
&\ge
\eta^2+4c_0y_n^2Q_0^2.
\end{aligned}
\tag{R43.10am}
\]
Thus the poles
\[
Q=\pm\frac{i\eta}{2y_n}
\]
are uniformly excluded from \(\mathbb D_{Q_0}\), simultaneously for all real \(\eta\)
and all \(n\).

Comparison of (R43.10am) with the positive real denominator at \(Q_0\) gives
\[
\boxed{
|s_n(Q,\eta)|
\le
C\,s_n(Q_0,\eta)
\qquad
(Q\in\mathbb D_{Q_0}),
}
\tag{R43.10an}
\]
with \(C\) independent of \(n,\eta\).

Now restrict \(Q\) to the smaller disk
\[
|Q-Q_0|\le\rho.
\]
For every such \(Q\), the Cauchy circle of radius \(\rho\) remains inside
\(\mathbb D_{Q_0}\).  Applying the scalar Cauchy estimate to
\(Q\mapsto s_n(Q,\eta)\) and using (R43.10an) yields, for every integer \(k\ge0\),
\[
\boxed{
|\partial_Q^ks_n(Q,\eta)|
\le
C_{k,Q_0}\,s_n(Q_0,\eta),
}
\tag{R43.10ao}
\]
again uniformly in \(n,\eta\).

The R33 series is positive at the real point \(Q_0\), so summing (R43.10ao) gives
\[
\boxed{
|\partial_Q^km_Q(\eta)|
\le
C_{k,Q_0}\,m_{Q_0}(\eta).
}
\tag{R43.10ap}
\]
This is the common summable/form-norm majorant missing from the previous version of
R43.10z.

Let \(\mathscr V_{Q_0}\) be the fixed Hilbert form domain with norm
\[
\|h\|_{\mathscr V_{Q_0}}^2
=
\frac1{2\pi}
\int_\mathbb R
m_{Q_0}(\eta)
|\widehat{E_1h}(\eta)|^2\,d\eta.
\]
For \(h,k\) in the complexified fixed form domain, (R43.10ap), evenness of the
reference weight, and weighted Cauchy--Schwarz imply for the bilinear extension
\[
|\partial_Q^j\mathfrak a_Q^{\mathbb C}[h,k]|
\le
C_{j,Q_0}
\|h\|_{\mathscr V_{Q_0}}
\|k\|_{\mathscr V_{Q_0}}.
\tag{R43.10aq}
\]
The same estimate with \(j=2\) gives a uniform quadratic Taylor remainder in the
operator form norm.  Indeed, scalar Taylor's formula on the complex disk and
(R43.10aq) imply
\[
\|
A(Q+h)-A(Q)-hA_1(Q)
\|_{\mathcal B(\mathscr V_{Q_0},\mathscr V_{Q_0}^*)}
\le
C_{Q_0}|h|^2,
\]
where \(A_1(Q)\) is the bounded form obtained by integrating
\(\partial_Qm_Q\).  Thus no weak-to-strong shortcut is needed:
\[
\boxed{
Q\longmapsto A(Q)
\text{ is operator-norm holomorphic in }
\mathcal B(\mathscr V_{Q_0},\mathscr V_{Q_0}^*).
}
\tag{R43.10ar}
\]

For the jet functionals, define for complex \(Q\) near \(Q_0\)
\[
\Phi_m(Q,y)
:=
\operatorname{sgn}(y)\,I_m(Q|y|),
\qquad
I_m(z):=\int_0^z s^me^{-s/2}\,ds.
\tag{R43.10as}
\]
The function \(I_m\) is entire, and for positive real \(Q\),
\[
\Phi_m(Q,y)=\phi_m(Qy).
\]
Since the fixed interval \(y\in[-1,1]\) is bounded and
\(\mathscr V_{Q_0}\hookrightarrow L^2(-1,1)\) continuously — the fixed-domain norm
from R43.10al--R43.10ar contains the (L^2(-1,1)) term and hence dominates it — the maps
\[
Q\longmapsto b_{m,Q}\in\mathscr V_{Q_0}^*
\]
are locally holomorphic.

At real \(Q_0\), \(A(Q_0)\) is coercive.  By continuity, \(A(Q)\) remains invertible
in a smaller complex neighborhood, and the Banach-valued inverse theorem gives
holomorphic \(A(Q)^{-1}\).  Therefore the construction R43.10ab--R43.10ac is genuinely
holomorphic there, and
\[
\boxed{
Q\longmapsto\gamma_Q
\text{ is real analytic on }(0,\infty).
}
\tag{R43.10at}
\]
Together with frozen R42 strict monotonicity,
\[
\boxed{
\gamma_Q'>0
\quad\text{for every }Q>0
\text{ except at most a discrete set.}
}
\tag{R43.10au}
\]
Thus the scalar nest measure in R43.10af has a density that is positive Lebesgue-a.e.

This closes the specific proof-completeness objection to R43.10z internally.  The whole
block R43.10ak--R43.10au remains a new AI-GREEN candidate until independent review.

---

## 3G. Literature interface: scalarization of the full odd Gamma radius chain

We now attack GC-M1 itself.

Define the full Gamma spectral measure
\[
\boxed{
d\mu_\Gamma(\xi)
=
\frac1{2\pi}m_\Gamma(\xi)\,d\xi.
}
\tag{R43.10av}
\]
R33 gives
\[
m_\Gamma(\xi)\ge1,
\qquad
m_\Gamma(\xi)\asymp\log(2+|\xi|),
\]
so
\[
\int_\mathbb R\frac{d\mu_\Gamma(\xi)}{1+\xi^2}<\infty.
\tag{R43.10aw}
\]
Moreover \(\mu_\Gamma\) is even.

We use two standard Krein--de Branges inputs, recorded here as explicit literature
dependencies rather than silently importing them:

1. **Inverse exponential-type theorem.**  For a canonical Hamiltonian with spectral
   measure \(\mu\), the \(L^2(\mu)\)-completion of the Fourier class of functions with
   physical support in \([-Q,Q]\), when non-dense, is the de Branges space generated by
   the canonical system up to the canonical generalized-inverse type radius
   \(r=L_H(Q)\).
2. **Even-measure diagonalization.**  Every even positive Poisson-finite spectral
   measure admits a canonical realization with diagonal Hamiltonian.

A convenient source for (1) is the **published Inventiones version** of
Bessonov--Denisov, *Szegő condition, scattering, and vibration of Krein strings*,
Invent. Math. 234 (2023), 291--373, DOI 10.1007/s00222-023-01201-9,
**Theorem 2.4** (Inverse Krein--de Branges theorem on exponential type), together with
equations (2.7), (2.10), (2.18), and (2.21).  The authors' separately posted extended
version inserts an additional theorem earlier in Section 2.2 and therefore renumbers the
inverse theorem as Theorem 2.5.  Throughout R43, the phrase
"Bessonov--Denisov Theorem 2.4" means the published Inventiones version.  This is a
bibliographic version distinction only.
A convenient source for (2) is the even-measure/diagonal-Hamiltonian theorem quoted as
Theorem 2.6 in Zhang,
*Direct spectral problems for Paley--Wiener canonical systems* (2026).

### Fixed-radius Gamma core equals the weighted Fourier completion

Let
\[
\mathcal V_Q^\Gamma
=
\left\{
f\in\mathcal D(q_\Gamma):
\operatorname{supp}f\subset[-Q,Q]
\right\}.
\]
The P11 Gamma norm is
\[
\|f\|_{\Gamma}^2
=
\frac1{2\pi}
\int m_\Gamma(\xi)|\widehat f(\xi)|^2\,d\xi.
\]
We need the fixed-radius statement
\[
\boxed{
C_c^\infty((-Q,Q))
\text{ is dense in }\mathcal V_Q^\Gamma
\text{ for the Gamma form norm.}
}
\tag{R43.10ax0}
\]

To see this, first dilate inward.  For \(0<\lambda<1\), put
\[
f_\lambda(u)
=
\lambda^{-1/2}f(u/\lambda).
\]
Then
\[
\operatorname{supp}f_\lambda\subset[-\lambda Q,\lambda Q],
\]
and after the Fourier change of variables,
\[
\|f_\lambda\|_\Gamma^2
=
\frac1{2\pi}
\int
m_\Gamma(\eta/\lambda)|\widehat f(\eta)|^2\,d\eta.
\]
For \(\lambda\) in a fixed neighborhood of \(1\), R33.3 in both dilation
directions gives a uniform operator bound
\[
\|D_\lambda\|_{\mathcal B(\mathcal D(q_\Gamma),\mathcal D(q_\Gamma))}
\le C.
\tag{R43.10ax1}
\]
On Schwartz functions, \(D_\lambda g\to g\) in the Gamma form norm by direct dominated
convergence: the Fourier transforms are rapidly decreasing and
\(m_\Gamma(\xi)\asymp\log(2+|\xi|)\).  The global P11 Gamma proof already uses Schwartz
density in \(\mathcal D(q_\Gamma)\).  Uniform boundedness of \(D_\lambda\) near
\(\lambda=1\) therefore extends the convergence from the dense Schwartz core to every
\(f\in\mathcal D(q_\Gamma)\):
\[
\boxed{
D_\lambda f\to f
\quad\text{in the Gamma form norm as }\lambda\uparrow1.
}
\tag{R43.10ax2}
\]
For fixed \(\lambda<1\), convolve \(f_\lambda\) with a standard smooth mollifier of
radius smaller than \(Q(1-\lambda)\).  The result lies in
\(C_c^\infty((-Q,Q))\); on the Fourier side the mollifier multiplier converges pointwise
to \(1\) and is uniformly bounded, so another dominated-convergence argument in the
weight \(m_\Gamma\) gives form-norm convergence.  This proves (R43.10ax0).

Hence the Fourier image of the concrete full Gamma radius-\(Q\) form space is exactly
the \(L^2(\mu_\Gamma)\)-completion of the smooth support-\(Q\) Fourier class used below.

### Non-density is explicit for the concrete Gamma measure

Let \(\mathcal E_Q\) be the Fourier transforms of smooth functions supported in
\((-Q,Q)\).  Choose nonzero
\[
\psi\in C_c^\infty(\mathbb R\setminus[-Q,Q])
\]
and put
\[
G_\psi(\xi)
:=
\frac{\widehat\psi(\xi)}{m_\Gamma(\xi)}.
\]
Because \(m_\Gamma\ge1\),
\[
G_\psi\in L^2(\mu_\Gamma).
\]
For \(F=\widehat f\in\mathcal E_Q\),
\[
\begin{aligned}
\langle F,G_\psi\rangle_{L^2(\mu_\Gamma)}
&=
\frac1{2\pi}
\int_\mathbb R
\widehat f(\xi)
\overline{\widehat\psi(\xi)}
\,d\xi\\
&=
\langle f,\psi\rangle_{L^2(\mathbb R)}
=0.
\end{aligned}
\tag{R43.10ax}
\]
Thus \(\mathcal E_Q\) is not dense in \(L^2(\mu_\Gamma)\) for any finite \(Q\), so
the inverse exponential-type theorem applies at every radius.

Consequently the Fourier image of the full Gamma form space on \((-Q,Q)\) is exactly
a de Branges truncation.

Fix **one** diagonal canonical realization supplied by the even-measure theorem and denote
that chosen realization by
\[
H_\Gamma^{\mathrm{diag}}(t)
=
\begin{pmatrix}
h_1(t)&0\\
0&h_2(t)
\end{pmatrix}.
\]
No uniqueness of this Hamiltonian is asserted or needed.

For this chosen realization put
\[
\mathcal B_Q^\Gamma
=
B_{r(Q)},
\qquad
r(Q)=L_{H_\Gamma^{\mathrm{diag}}}(Q).
\tag{R43.10ay}
\]
The inverse exponential-type theorem uses the type clock
\[
T_{H_\Gamma^{\mathrm{diag}}}(r)
=
\int_0^r\sqrt{\det H_\Gamma^{\mathrm{diag}}(t)}\,dt.
\]

### Szegő hardening: every finite support radius is reached

The concrete density
\[
w_\Gamma(\xi)=\frac{m_\Gamma(\xi)}{2\pi}
\]
satisfies
\[
w_\Gamma(\xi)\ge\frac1{2\pi}
\]
and the Poisson-finiteness condition R43.10aw.  Moreover
\(m_\Gamma(\xi)\asymp\log(2+|\xi|)\) gives
\[
\int_{\mathbb R}
\frac{|\log w_\Gamma(\xi)|}{1+\xi^2}\,d\xi<\infty,
\]
so \(\mu_\Gamma\) lies in the spectral Szegő class.  The source-checked spectral Szegő
theorem therefore gives
\[
\sqrt{\det H_\Gamma^{\mathrm{diag}}}\notin L^1(\mathbb R_+).
\]
Hence
\[
T_{H_\Gamma^{\mathrm{diag}}}(r)\to\infty
\qquad(r\to\infty),
\]
and consequently
\[
\boxed{
r(Q)=L_{H_\Gamma^{\mathrm{diag}}}(Q)<\infty
\quad\text{for every finite }Q>0.
}
\tag{R43.10ay0}
\]
The defining property of the type clock now gives
\[
\boxed{
T_{H_\Gamma^{\mathrm{diag}}}(r(Q))=Q.
}
\tag{R43.10ay1}
\]
This closes the former finiteness assumption in R43.10ay1.  It does **not** imply
\(\det H_\Gamma^{\mathrm{diag}}>0\) a.e.

### The determinant-normalized PW route is unavailable

The concrete logarithmic growth also excludes \(\mu_\Gamma\) from the PW-sampling class
required by the stronger determinant-normalized correspondence.  From
\[
m_\Gamma(\xi)\asymp\log(2+|\xi|)
\]
there are \(c>0\) and \(x_0>0\) such that
\[
m_\Gamma(\xi)\ge c\log x
\qquad
(x\ge x_0,\ \xi\in[x,x+1]).
\]
Therefore
\[
\mu_\Gamma((x,x+1))
=
\frac1{2\pi}\int_x^{x+1}m_\Gamma(\xi)\,d\xi
\ge
\frac{c}{2\pi}\log x
\longrightarrow\infty,
\]
and hence
\[
\boxed{
\sup_{x\in\mathbb R}\mu_\Gamma((x,x+1))=\infty.
}
\tag{R43.10ay2}
\]
Thus Makarov--Poltoratski Theorem 3.6 cannot be applied here to deduce a diagonal
**and determinant-normalized** Hamiltonian.

This is a firewall about that literature route, not a theorem that no independent argument
could ever prove stronger regularity.

### Odd parity selects one scalar canonical coordinate

For the chosen diagonal realization let
\[
\Theta(t,z)
=
\binom{\Theta_+(t,z)}{\Theta_-(t,z)}
\]
solve the canonical system with the standard first-coordinate initial condition.  ODE
uniqueness gives
\[
\Theta_+(t,-z)=\Theta_+(t,z),
\qquad
\Theta_-(t,-z)=-\Theta_-(t,z).
\tag{R43.10ba}
\]
Thus first-coordinate states transform to even spectral functions and second-coordinate
states to odd spectral functions.

The odd part of the radius-\(Q\) de Branges truncation is therefore the image of
second-coordinate states \(X=(0,x_2)^t\) supported on \((0,r(Q))\), with norm
\[
\boxed{
\|X\|^2
=
\int_0^{r(Q)}h_2(t)|x_2(t)|^2\,dt.
}
\tag{R43.10bb}
\]
Hence the full odd Gamma truncation chain is a **scalar multiplicity-one support nest**:
\[
\boxed{
\mathcal B_{Q,\mathrm{odd}}^\Gamma
\simeq
L^2\!\left((0,r(Q)),h_2(t)\,dt\right).
}
\tag{R43.10az}
\]

Push this scalar state measure forward by the type coordinate
\[
Q=T_{H_\Gamma^{\mathrm{diag}}}(t).
\]
Then there is a scalar Borel measure \(\nu_\Gamma^{\mathrm{odd}}\) such that
\[
\boxed{
N_Q\simeq L^2((0,Q],d\nu_\Gamma^{\mathrm{odd}}),
\qquad 0<Q<S.
}
\tag{R43.10bc}
\]
This proves scalar multiplicity one, but it does **not** identify
\(d\nu_\Gamma^{\mathrm{odd}}\) with \(dQ\).

The intrinsic P11 radius chain is continuous: R43.10ax0--R43.10ax2 give left continuity,
and support closedness gives right continuity.  Therefore
\(\nu_\Gamma^{\mathrm{odd}}\) has no atoms.  A singular-continuous component in the natural
radius variable remains possible at this stage and is exactly the GC-AC issue isolated in
Section 3J.

### Source verification note

The literature interface has been checked against the original statements:

- Bessonov--Denisov, **published Inventiones version**, Theorem 2.4 gives the inverse
  exponential-type identification under Poisson finiteness and non-density; the separately
  posted extended version renumbers this inverse theorem as Theorem 2.5.  R43.10ax proves
  non-density explicitly.
- The type clock is
  \[
  T(\tau)=\int_0^\tau\sqrt{\det H(s)}\,ds,
  \]
  with \(T(L_Q)=Q\) whenever \(L_Q<\infty\).
- Zhang Theorem 2.6, equivalently Makarov--Poltoratski Theorem 3.5, gives existence of
  **a** diagonal realization for an even positive Poisson-finite measure; no uniqueness is
  asserted.
- The general theorem does not guarantee \(\det H\ne0\) a.e.
- The spectral Szegő input above gives \(L_Q<\infty\) for every finite \(Q\).
- Makarov--Poltoratski Theorem 3.6 is tied to the PW-sampling class and is inapplicable
  here because of R43.10ay2.

Thus the checked literature proves scalarity of the odd chain and reachability of every
finite type radius.  It does **not** by itself prove Lebesgue absolute continuity in the
natural \(Q\)-coordinate.


---

## 3H. A compatible codimension-one constraint preserves scalar nest multiplicity

The review correctly warned that a generic rank-one perturbation need not preserve nest
multiplicity.  Our constraint, however, is not a generic perturbation: it is the restriction
of **one fixed functional** along a scalar support nest.  That special structure admits an
explicit unitary model.

### Lemma R43-GC1 — constrained scalar support nest

Let
\[
H=L^2((0,S),dq),
\qquad
N_t=L^2((0,t),dq),
\]
and let \(h\in H\), \(h\ne0\).  Put
\[
M=h^\perp,
\qquad
M_t=N_t\cap M.
\tag{R43.10bd}
\]
Then the nest \(\{M_t:0\le t\le S\}\) on \(M\) has scalar multiplicity one.  More
precisely, there is a unitary
\[
\mathcal T_h:M\to L^2((0,S),dq)
\]
such that
\[
\boxed{
\mathcal T_h P_t^M
=
M_{1_{(0,t)}}\mathcal T_h,
}
\tag{R43.10be}
\]
where \(P_t^M\) is orthogonal projection of \(M\) onto \(M_t\).

### Proof

Define
\[
A(t):=\int_0^t|h(s)|^2\,ds,
\qquad
F_f(t):=\int_0^t f(s)\overline{h(s)}\,ds.
\tag{R43.10bf}
\]
For \(A(t)>0\),
\[
P_t^Mf
=
1_{(0,t)}
\left(
f-\frac{F_f(t)}{A(t)}h
\right),
\tag{R43.10bg}
\]
while if \(A(t)=0\), the correction term is zero.

Define, with the same convention on \(\{A=0\}\),
\[
\boxed{
(\mathcal T_hf)(t)
=
f(t)
-
h(t)\frac{F_f(t)}{A(t)}.
}
\tag{R43.10bh}
\]
Since
\[
dF_f=f\overline h\,dq,
\qquad
dA=|h|^2\,dq,
\]
the absolutely continuous quotient rule gives
\[
d\left(\frac{|F_f|^2}{A}\right)
=
2\operatorname{Re}
\left(
\frac{\overline{F_f}\,dF_f}{A}
\right)
-
\frac{|F_f|^2}{A^2}\,dA
\tag{R43.10bi}
\]
where \(A>0\).  Integrating (R43.10bi) yields
\[
\boxed{
\|P_t^Mf\|^2
=
\int_0^t|\mathcal T_hf(q)|^2\,dq.
}
\tag{R43.10bj}
\]
For \(f\in M\),
\[
F_f(S)=0,
\]
so at \(t=S\),
\[
\|\mathcal T_hf\|=\|f\|.
\tag{R43.10bk}
\]
Thus \(\mathcal T_h\) is an isometry.

The projection formula also gives the exact intertwining.  If \(s\le t\), the constant
subtracted in (R43.10bg) cancels inside the running quotient in (R43.10bh); if \(s>t\),
the projected vector has zero support and zero total \(h\)-moment.  Hence
\[
\mathcal T_h(P_t^Mf)
=
1_{(0,t)}\mathcal T_hf.
\tag{R43.10bl}
\]

It remains to prove that \(\mathcal T_h\) is onto.  Given
\(y\in L^2((0,S))\), define
\[
r(t)
:=
-\int_{(t,S]}
\frac{y(s)\overline{h(s)}}{A(s)}\,ds,
\tag{R43.10bm}
\]
with the integrand set to zero where \(A=0\), and put
\[
f:=y+hr.
\tag{R43.10bn}
\]
On \(\{h\ne0\}\), write
\[
z:=\frac{y}{h}.
\]
Then
\[
r(t)
=
-\int_{(t,S]}\frac{z(s)}{A(s)}\,dA(s).
\]
Because Lebesgue measure has no atoms, \(A\) is continuous.  On the measure space with
measure \(dA=|h|^2dq\), flat pieces of \(A\) have \(dA\)-measure zero.  The cumulative
coordinate
\[
u=A(t)
\]
therefore pushes \(dA\) to Lebesgue measure \(du\) on \((0,A(S))\), modulo null sets.
In this coordinate,
\[
r(t)
=
-\int_{A(t)}^{A(S)}
\frac{\widetilde z(u)}{u}\,du.
\]
The classical adjoint Hardy inequality now applies literally:
\[
\boxed{
\int_0^S|r|^2\,dA
\le
4\int_0^S|z|^2\,dA
=
4\int_{\{h\ne0\}}|y|^2\,dq
\le
4\|y\|_2^2.
}
\tag{R43.10bo}
\]
Hence
\[
hr\in L^2((0,S)).
\]
Moreover
\[
d(Ar)
=
r\,dA+A\,dr
=
r|h|^2\,dq+y\overline h\,dq
=
f\overline h\,dq.
\]
Both sides vanish at the initial zero set of \(A\), so
\[
F_f(t)=A(t)r(t).
\tag{R43.10bp}
\]
Since \(r(S)=0\),
\[
F_f(S)=0,
\]
thus \(f\in M\), and (R43.10bh) gives
\[
\mathcal T_hf=y.
\]
Therefore \(\mathcal T_h\) is unitary, and (R43.10be) proves scalar multiplicity one.
\(\square\)

The lemma remains valid for any scalar support model
\[
L^2((0,S),w(q)\,dq),
\qquad
0<w(q)<\infty\text{ a.e.},
\]
after the support-preserving unitary multiplication by \(w^{1/2}\).

More generally, let \(\nu\) be any finite **atomless** scalar Borel measure on \((0,S)\)
and consider the standard support nest
\[
N_t^\nu=L^2((0,t],d\nu).
\]
Its cumulative function
\[
A_\nu(t):=\nu((0,t])
\]
is continuous and nondecreasing.  The probability-integral-transform / generalized-inverse
map gives a unitary
\[
\mathcal C_\nu:
L^2((0,S),d\nu)
\longrightarrow
L^2((0,A_\nu(S)),ds)
\]
which sends the support projection \(1_{(0,t]}\) to
\(1_{(0,A_\nu(t)]}\), up to repetitions on \(\nu\)-null flat intervals.  Thus the
atomless scalar support nest is unitarily equivalent to the standard Lebesgue support nest
after cumulative-measure reparameterization.

Applying Lemma R43-GC1 in that coordinate proves:
\[
\boxed{
\text{a compatible codimension-one hyperplane preserves scalar multiplicity
for every atomless scalar support nest.}
}
\tag{R43.10bp0}
\]

---

## 3I. First scalar-multiplicity candidate and its GC-AC firewall

Return to the full odd Gamma nest from R43.10bc.  Fix the terminal source radius \(S\).
Let \(h_{0,S}\) be the Riesz representative, in the full odd Gamma Hilbert space at radius
\(S\), of the compatible first boundary functional \(\beta_S^{(0)}\).

For \(Q<S\), source compatibility gives
\[
\beta_Q^{(0)}(f)
=
\beta_S^{(0)}(J_{Q,S}f).
\]
Therefore, inside the full odd Gamma radius-\(S\) space,
\[
\boxed{
H_Q^0
=
N_Q\cap h_{0,S}^{\perp}.
}
\tag{R43.10bq}
\]
The intrinsic full odd nest is scalar and atomless by Sections 3G and 3J.3.  The
atomless-measure extension R43.10bp0 of Lemma R43-GC1 therefore gives
\[
\boxed{
\mathrm{GC\!-\!M1}_{\rm scalar}
\text{ at candidate level.}
}
\tag{R43.10br}
\]

This statement alone does **not** imply cyclicity of the first-jet vector in the natural
radius variable.  A scalar vector may vanish on a singular-continuous part of the scalar
representing measure.  The missing condition is exactly GC-AC:
\[
\nu_{R,S}\ll dQ.
\]

Accordingly, the earlier terminal-free conclusions are valid at this stage only under the
additional GC-AC hypothesis:
\[
\boxed{
\mathrm{GC\!-\!M1}_{\rm scalar}
+
\mathrm{GC\!-\!AC}
\Longrightarrow
\overline{
J_{R,S}\mathscr G_R^0
+
\operatorname{span}\{P_Q^\Gamma g_S:R<Q<S\}
}
=
\mathscr G_S^0.
}
\tag{R43.10bs}
\]
Equivalently,
\[
\boxed{
\mathrm{GC\!-\!AC}
\Longrightarrow
\overline{
Y_{R,S}V_R+
\operatorname{span}\{Y_{Q,S}\zeta_Q:R<Q<S\}
}
=
V_S.
}
\tag{R43.10bt}
\]
Under the same hypothesis every weak cluster \(w\) of
\[
w_U=W_{R,S}^{[U]}\varepsilon_R
\]
satisfies
\[
\boxed{
w\in(H_S^0)^\perp
=
\mathbb C\varepsilon_S.
}
\tag{R43.10bu}
\]

Even then this is **not yet Strong Terminal**.  The remaining scalar normal coefficient
\[
b_U
:=
\langle
W_{R,S}^{[U]}\varepsilon_R,
\varepsilon_S
\rangle
\tag{R43.10bv}
\]
must still satisfy
\[
\boxed{
b_U\to b,
\qquad
|b|=1
\quad?
}
\tag{R43.10bw}
\]

### Status of Sections 3F--3I

- R43.10ak--R43.10au: explicit analyticity repair, AI-GREEN candidate;
- R43.10av--R43.10bc: source-checked scalarization interface, hardened to avoid any
  determinant-normalized overclaim;
- Lemma R43-GC1 and R43.10bp0: self-contained scalar/codimension-one mechanism plus
  atomless-measure extension, AI-GREEN candidate;
- R43.10br: \(\mathrm{GC\!-\!M1}_{\rm scalar}\) candidate only;
- R43.10bs--R43.10bu: explicitly **conditional on GC-AC**.

Section 3K supplies the subsequent candidate proof of GC-AC.  No R37/G4c statement is used
or changed.


## 3J. Source-checked scalar multiplicity and the GC-AC split

The literature source check validates the inverse exponential-type and even-measure
diagonalization interfaces used in Section 3G, while also fixing exactly what they do and do
not imply.

### 3J.1 What the checked literature gives

Bessonov--Denisov, **published Inventiones version**, Theorem 2.4 identifies the intrinsic
smooth support-\(Q\) completion in \(L^2(\mu_\Gamma)\) with a de Branges truncation.  For the **chosen** diagonal realization
\(H_\Gamma^{\mathrm{diag}}\) from Section 3G,
\[
B_{L_Q},
\qquad
T(L_Q)=Q,
\qquad
T(r)=\int_0^r\sqrt{\det H_\Gamma^{\mathrm{diag}}(t)}\,dt.
\tag{R43.10bx}
\]
Zhang Theorem 2.6, equivalently Makarov--Poltoratski Theorem 3.5, gives existence of
**a diagonal canonical realization** of every even positive Poisson-finite measure, hence
of \(\mu_\Gamma\).  No uniqueness of that realization is asserted.

For the chosen diagonal Hamiltonian
\[
H_\Gamma^{\mathrm{diag}}(t)
=
\begin{pmatrix}
h_1(t)&0\\
0&h_2(t)
\end{pmatrix},
\]
the parity identities R43.10ba imply that the odd spectral subspace is the image of the
second coordinate only.  Therefore the **full odd canonical chain is scalar** before the
\(\beta^{(0)}\)-constraint.

The source-checked Szegő input also gives
\[
T(r)\to\infty,
\]
hence every finite support radius \(Q\) is reached:
\[
L_Q<\infty.
\]

### 3J.2 What the checked literature does not give

The general even-measure diagonalization theorem does **not** assert
\[
\det H_\Gamma^{\mathrm{diag}}>0
\quad\text{a.e.}
\]
Rank-one / zero-determinant pieces are allowed.

The stronger Makarov--Poltoratski correspondence with diagonal determinant-normalized
Hamiltonians is tied to the PW-sampling class.  Our concrete Gamma measure fails that
hypothesis by R43.10ay2:
\[
\sup_x\mu_\Gamma((x,x+1))=\infty.
\]
Therefore that theorem is not available to upgrade the natural radius model to Lebesgue
measure.

This is a literature-interface limitation, not a universal impossibility theorem for all
future methods.

### 3J.3 Atomlessness of the intrinsic P11 radius chain

The concrete P11 Gamma support spaces are continuous in the radius parameter.  The
fixed-radius core argument gives
\[
\overline{\bigcup_{q<Q}\mathcal V_q^\Gamma}^{\ \|\cdot\|_\Gamma}
=
\mathcal V_Q^\Gamma,
\tag{R43.10by}
\]
and support closedness gives
\[
\bigcap_{q>Q}\mathcal V_q^\Gamma
=
\mathcal V_Q^\Gamma.
\tag{R43.10bz}
\]
Hence the orthogonal projection nest is strongly continuous from both sides.  Its scalar
representing measure therefore has **no atoms**.

Thus, after scalar multiplicity one is known, the only possible hidden radius channel is
singular-continuous with respect to Lebesgue measure in the natural \(Q\)-coordinate.

### 3J.4 Why scalar multiplicity is realization-independent

The P11 projection nest
\[
\boxed{
\{P_Q^\Gamma:0<Q<S\}
}
\]
is defined intrinsically from the Gamma form and the support-constrained spaces \(H_Q^0\).
It exists before any canonical-system realization is selected.

On the Fourier side, the corresponding unconstrained support spaces are the intrinsic
closures
\[
\overline{\mathcal E_Q}^{\,L^2(\mu_\Gamma)}.
\]
A canonical system provides a **unitary model** of this already defined nested family; it
does not define the family itself.

Nest multiplicity is invariant under unitary equivalence.  Therefore the existence of
**one** diagonal realization exhibiting one odd coordinate is sufficient to prove scalar
multiplicity of the intrinsic odd Gamma nest.  No uniqueness of
\(H_\Gamma^{\mathrm{diag}}\) is required.

Lemma R43-GC1 is likewise not tied to Lebesgue measure in the original radius coordinate:
an atomless scalar support nest can first be placed in a standard scalar \(L^2\)-model by
its cumulative measure coordinate, and the same Hardy/Volterra construction applies to the
compatible hyperplane
\[
\beta^{(0)}=0.
\]

Hence, at candidate level,
\[
\boxed{
\text{the constrained intrinsic Gamma radius nest has scalar multiplicity one.}
}
\tag{R43.10ca}
\]

This is exactly
\[
\boxed{
\mathrm{GC\!-\!M1}_{\rm scalar}.
}
\]

### 3J.5 Exact remaining cyclicity obstruction before Section 3K

Let
\[
\nu_{R,S}
\]
be a scalar measure representing this constrained multiplicity-one nest in the natural
radius variable \(Q\in(R,S)\), and let \(G_{R,S}(Q)\) be the scalar representative of
\[
(I-P_R^\Gamma)g_S.
\]
Then
\[
d\gamma_Q
=
|G_{R,S}(Q)|^2\,d\nu_{R,S}(Q).
\tag{R43.10cb}
\]
The repaired analyticity theorem gives
\[
d\gamma_Q
=
\gamma_Q'\,dQ,
\qquad
\gamma_Q'>0
\quad\text{for a.e. }Q.
\tag{R43.10cc}
\]

By atomlessness,
\[
d\nu_{R,S}
=
w(Q)\,dQ+d\nu_{R,S}^{\mathrm{sc}}.
\tag{R43.10cd}
\]
Equating the Lebesgue and singular parts in R43.10cb--R43.10cc gives:

1. \(w(Q)>0\) for Lebesgue-a.e. \(Q\);
2. \(G_{R,S}(Q)\ne0\) for \(w(Q)dQ\)-a.e. \(Q\);
3. \(G_{R,S}=0\) for \(\nu_{R,S}^{\mathrm{sc}}\)-a.e. \(Q\).

Therefore
\[
\boxed{
(I-P_R^\Gamma)g_S
\text{ is cyclic}
\iff
\nu_{R,S}^{\mathrm{sc}}=0.
}
\tag{R43.10ce}
\]

This isolates
\[
\boxed{
\textbf{GC-AC: }
\nu_{R,S}\ll dQ.
}
\tag{R43.10cf}
\]

### 3J.6 Booking before the higher-jet argument

At the end of Section 3J alone the correct booking is
\[
\boxed{
\mathrm{GC\!-\!M1}_{\rm scalar}
\text{ candidate-GREEN;}
\qquad
\mathrm{GC\!-\!AC}
\text{ still requires an additional argument.}
}
\tag{R43.10cg}
\]

Section 3K supplies that additional candidate argument using the total higher-jet Riesz
family.  No R37/G4c conclusion is used, and no Strong-Terminal promotion is booked here.


## 3K. All constrained jet-Riesz vectors eliminate the singular-continuous radius channel

Section 3J isolates GC-AC as the only possible obstruction left after scalar multiplicity one.
There is, however, more information than the single first-jet Riesz vector \(g_S=g_{1,S}\):
the entire compatible jet family is available.

This closes the singular-continuous escape at candidate level without any lower bound on
\(\det H_\Gamma\).

### 3K.1 Totality of the integral jets on the odd finite window

For \(m\ge0\), recall
\[
\phi_m(u)
=
\operatorname{sgn}(u)I_m(|u|),
\qquad
I_m(r)
=
\int_0^r t^m e^{-t/2}\,dt,
\]
and
\[
\beta_S^{(m)}(f)
=
\int_{-S}^{S}f(u)\phi_m(u)\,du.
\]

Let \(f\in L^2(-S,S)\) be odd and suppose
\[
\beta_S^{(m)}(f)=0
\qquad
\forall m\ge0.
\tag{R43.10ch}
\]
By oddness,
\[
0
=
\frac12\beta_S^{(m)}(f)
=
\int_0^S f(u)I_m(u)\,du.
\]
Fubini gives
\[
\begin{aligned}
0
&=
\int_0^S
f(u)
\int_0^u t^m e^{-t/2}\,dt\,du\\
&=
\int_0^S
t^m e^{-t/2}
\left(
\int_t^S f(u)\,du
\right)dt.
\end{aligned}
\tag{R43.10ci}
\]
Put
\[
F_f(t):=\int_t^S f(u)\,du.
\]
Then the finite signed measure
\[
d\sigma_f(t)
=
e^{-t/2}F_f(t)\,dt
\]
annihilates every polynomial.  Polynomials are uniformly dense in
\(C([0,S])\), hence
\[
\sigma_f=0.
\]
Therefore \(F_f=0\) a.e., and since \(F_f\) is absolutely continuous with
\[
F_f'=-f
\]
a.e.,
\[
\boxed{
f=0.
}
\tag{R43.10cj}
\]

Thus
\[
\boxed{
\{\beta_S^{(m)}:m\ge0\}
\text{ is total on the odd finite-window }L^2\text{ space.}
}
\tag{R43.10ck}
\]

In particular, on
\[
H_S^0=\ker\beta_S^{(0)}
\]
the restricted family
\[
\boxed{
\{\beta_S^{(m)}|_{H_S^0}:m\ge1\}
\text{ is total.}
}
\tag{R43.10cl}
\]

Because
\[
\mathfrak c_{\Gamma,S}[f]\ge \|f\|_{L^2(-S,S)}^2,
\]
every \(\beta_S^{(m)}\) is continuous in the constrained Gamma Hilbert norm.

### 3K.2 Higher constrained Gamma-Riesz vectors

For every \(m\ge1\), let
\[
g_{m,Q}\in H_Q^0
\]
be the constrained Gamma-Riesz vector defined by
\[
\boxed{
\mathfrak c_{\Gamma,Q}[f,g_{m,Q}]
=
\beta_Q^{(m)}(f),
\qquad
f\in H_Q^0.
}
\tag{R43.10cm}
\]
For \(m=1\), this is the already frozen/reviewed vector
\[
g_{1,Q}=g_Q.
\]

Source compatibility gives, for \(Q<S\),
\[
\beta_S^{(m)}(J_{Q,S}f)
=
\beta_Q^{(m)}(f).
\]
Since zero extension is Gamma-isometric,
\[
\boxed{
P_Q^\Gamma g_{m,S}
=
J_{Q,S}g_{m,Q}.
}
\tag{R43.10cn}
\]

Define
\[
\gamma_m(Q)
:=
\|g_{m,Q}\|_{\Gamma,Q}^2.
\tag{R43.10co}
\]
Then
\[
\boxed{
\|P_Q^\Gamma g_{m,S}\|_{\Gamma,S}^2
=
\gamma_m(Q).
}
\tag{R43.10cp}
\]

### 3K.3 Every higher-jet nest measure is absolutely continuous in \(Q\)

Fix an arbitrary jet order
\[
m\ge1
\]
and a real reference radius \(Q_0>0\).  We now verify the fixed-domain analytic argument
for this arbitrary \(m\), rather than importing the first-jet proof by analogy.

Use the same complex disk \(\mathbb D_{Q_0}\) and fixed form domain
\(\mathscr V_{Q_0}\) as in R43.10al--R43.10ar, with \(A(Q)\) understood throughout in
the **complex-bilinear real-form complexification** fixed in R43.10z0.  In particular, no
sesquilinear Hilbert-Riesz map is being analytically continued.  The estimates there are
independent of the jet index and give an operator-norm holomorphic family
\[
Q\longmapsto
A(Q)
\]
with a holomorphic inverse \(A(Q)^{-1}\) on a smaller disk about \(Q_0\).

Choose the holomorphic branch of \(Q^{1/2}\) on this disk.  For the fixed order \(m\),
define
\[
\Phi_m(Q,y)
=
\operatorname{sgn}(y)I_m(Q|y|),
\qquad
I_m(z)
=
\int_0^z s^me^{-s/2}\,ds.
\]
Because \(I_m\) is entire, the pulled-back jet functional is
\[
\boxed{
b_{m,Q}(h)
=
Q^{1/2}
\int_{-1}^1
h(y)\Phi_m(Q,y)\,dy.
}
\tag{R43.10cq0}
\]
For every closed subdisk and every integer \(k\ge0\),
\[
\sup_{\substack{Q\text{ in subdisk}\\ |y|\le1}}
\left|
\partial_Q^k
\bigl(
Q^{1/2}\Phi_m(Q,y)
\bigr)
\right|
<\infty.
\]
Since
\[
\mathscr V_{Q_0}\hookrightarrow L^2(-1,1),
\]
Cauchy--Schwarz gives
\[
\boxed{
\|\partial_Q^k b_{m,Q}\|_{\mathscr V_{Q_0}^*}
\le
C_{m,k,Q_0}.
}
\tag{R43.10cq1}
\]

The dependence on the jet order can be made explicit locally.  Keep the smaller disk
\(|Q-Q_0|\le\rho\) and use the larger disk \(|Q-Q_0|\le2\rho\) from Section 3F.
Put
\[
M_{Q_0,\rho}:=Q_0+2\rho.
\]
For every complex \(z\),
\[
I_m(z)
=
z^{m+1}
\int_0^1
t^m e^{-tz/2}\,dt,
\]
hence on the larger disk and \(|y|\le1\),
\[
|I_m(Q|y|)|
\le
\frac{
M_{Q_0,\rho}^{m+1}e^{M_{Q_0,\rho}/2}
}{m+1}.
\tag{R43.10cq1a}
\]
The chosen square-root branch is uniformly bounded there.  Cauchy's derivative estimate
from the larger disk to the smaller one therefore gives, for every fixed \(k\ge0\),
\[
\boxed{
\sup_{|Q-Q_0|\le\rho}
\|\partial_Q^k b_{m,Q}\|_{\mathscr V_{Q_0}^*}
\le
C_{k,Q_0,\rho}
\frac{M_{Q_0,\rho}^{m+1}}{m+1},
}
\tag{R43.10cq1b}
\]
where the constant is independent of \(m\).  Thus the currently available local
higher-jet holomorphy constants can be chosen with at most exponential growth in the jet
order.

Since \(A(Q)^{-1}\), the zeroth-jet correction, and \(d_Q^{-1}\) are uniformly bounded
on a still smaller closed disk, the same argument yields the crude local bound
\[
\boxed{
\sup_{|Q-Q_0|\le\rho'}
\|\widetilde g_{m,Q}\|_{\mathscr V_{Q_0}}
\le
C'_{Q_0,\rho'}
\frac{M_{Q_0,\rho}^{m+1}}{m+1}.
}
\tag{R43.10cq1c}
\]

This is useful quantitative information, but it is **not** a B-JMOM estimate.  The bound
concerns the Section-3K higher-jet Riesz family.  Turning it into a weighted estimate for
the canonical C6a ONB coefficients would require quantitative control of the
orthogonalization/change-of-basis constants (equivalently suitable lower bounds for the
relevant finite jet Gram determinants).  No such uniform-in-\(m\) conditioning theorem is
currently booked.

Thus
\[
\boxed{
\text{explicit }C_{m,k,Q_0}\text{ growth}
\not\Rightarrow
\text{B-JMOM without a jet-basis conditioning theorem.}
}
\tag{R43.10cq1d}
\]

Thus
\[
\boxed{
Q\longmapsto b_{m,Q}\in\mathscr V_{Q_0}^*
\text{ is holomorphic.}
}
\tag{R43.10cq2}
\]
The same statement for \(m=0\) is already part of the Section 3F construction.

Set
\[
u_{m,Q}
=
A(Q)^{-1}b_{m,Q},
\qquad
u_{0,Q}
=
A(Q)^{-1}b_{0,Q},
\]
and
\[
d_Q
=
b_{0,Q}(u_{0,Q}).
\]
All three maps are holomorphic.  At the real point \(Q_0\),
\[
d_{Q_0}>0,
\]
so after shrinking the disk,
\[
d_Q\ne0.
\]
Hence
\[
\boxed{
\widetilde g_{m,Q}
=
u_{m,Q}
-
\frac{b_{0,Q}(u_{m,Q})}{d_Q}
u_{0,Q}
}
\tag{R43.10cq}
\]
is holomorphic as a \(\mathscr V_{Q_0}\)-valued map.

For positive real \(Q\), this vector is exactly the pulled-back constrained Gamma-Riesz
vector.  Indeed, if
\[
h\in\ker b_{0,Q},
\]
then
\[
\begin{aligned}
a_Q[h,\widetilde g_{m,Q}]
&=
a_Q[h,u_{m,Q}]
-
\frac{b_{0,Q}(u_{m,Q})}{d_Q}
a_Q[h,u_{0,Q}]\\
&=
b_{m,Q}(h)
-
\frac{b_{0,Q}(u_{m,Q})}{d_Q}
b_{0,Q}(h)\\
&=
b_{m,Q}(h).
\end{aligned}
\tag{R43.10cq3}
\]
Therefore
\[
D_Q\widetilde g_{m,Q}=g_{m,Q}.
\]

Evaluating the Riesz identity at \(g_{m,Q}\) gives
\[
\boxed{
\gamma_m(Q)
=
\|g_{m,Q}\|_{\Gamma,Q}^2
=
b_{m,Q}(\widetilde g_{m,Q}).
}
\tag{R43.10cq4}
\]
The right side is the restriction of a holomorphic scalar function from the complexified
bilinear problem to the positive real axis.  On that real axis it equals the genuine
Hilbert norm square; no such norm interpretation is made off the real axis.  Thus
\[
\boxed{
Q\longmapsto\gamma_m(Q)
\text{ is real analytic on }(0,\infty)
}
\tag{R43.10cr}
\]
for every fixed \(m\ge1\).

By R43.10cp,
\[
\gamma_m(Q)
=
\|P_Q^\Gamma g_{m,S}\|_{\Gamma,S}^2,
\]
so \(\gamma_m\) is nondecreasing in \(Q\).  Real analyticity implies local absolute
continuity; therefore its Lebesgue--Stieltjes measure is
\[
\boxed{
d\|P_Q^\Gamma g_{m,S}\|_{\Gamma,S}^2
=
d\gamma_m(Q)
=
\gamma_m'(Q)\,dQ.
}
\tag{R43.10cs}
\]
No strict-positivity statement for \(\gamma_m'\) is required.

Since \(m\ge1\) was arbitrary, R43.10cs holds for the whole countable higher-jet family.

### 3K.4 The Riesz family is dense in the constrained Gamma space

Suppose
\[
f\in H_S^0
\]
is Gamma-orthogonal to every \(g_{m,S}\), \(m\ge1\).  Then by (R43.10cm),
\[
\beta_S^{(m)}(f)=0
\qquad
\forall m\ge1.
\]
Since \(f\in H_S^0\),
\[
\beta_S^{(0)}(f)=0.
\]
The totality theorem R43.10cj therefore gives
\[
f=0.
\]
Hence
\[
\boxed{
\overline{
\operatorname{span}\{g_{m,S}:m\ge1\}
}^{\ \|\cdot\|_{\Gamma,S}}
=
H_S^0.
}
\tag{R43.10ct}
\]

### 3K.5 GC-AC follows from total absolutely-continuous Riesz data

Now use the scalar multiplicity-one conclusion from Section 3J.4.  This is a statement
about the **intrinsic** projection nest \(\{P_Q^\Gamma\}\), so it is independent of which
diagonal canonical realization was used to prove scalarity.  By the spectral theorem for a
scalar continuous nest, choose any scalar representing measure \(\nu_S\) in the natural
radius variable and a unitary model
\[
H_S^0
\simeq
L^2((0,S),d\nu_S),
\]
with
\[
d\nu_S
=
w(Q)\,dQ+d\nu_S^{\mathrm{sc}}
\]
and no atoms.

Fix this unitary identification once and for all for the remainder of Section 3K.5.
The density statement R43.10ct, the scalar representatives below, the measure decomposition
\(d\nu_S=w(Q)dQ+d\nu_S^{\mathrm{sc}}\), and the identity R43.10cu are all read inside
this **same** Hilbert model \(L^2((0,S),d\nu_S)\).  No change of scalar realization is
made during the contradiction argument.

Let \(G_m\) denote, in this fixed model, the scalar representative of \(g_{m,S}\).
By the projection-nest spectral theorem,
\[
\boxed{
d\gamma_m(Q)
=
|G_m(Q)|^2\,d\nu_S(Q).
}
\tag{R43.10cu}
\]
But (R43.10cs) says
\[
d\gamma_m\ll dQ.
\]
Therefore
\[
\boxed{
G_m=0
\quad
\nu_S^{\mathrm{sc}}\text{-a.e.}
}
\tag{R43.10cv}
\]
for every \(m\ge1\).

Because
\[
d\nu_S^{\mathrm{sc}}\perp dQ,
\]
choose first a Borel singular support \(E_0\subset(0,S)\) with
\[
|E_0|=0,
\qquad
\nu_S^{\mathrm{sc}}((0,S)\setminus E_0)=0.
\tag{R43.10cv0}
\]
For every \(m\ge1\), absolute continuity of \(d\gamma_m\) gives
\[
0=d\gamma_m(E_0)
=
\int_{E_0}|G_m(Q)|^2\,d\nu_S(Q)
=
\int_{E_0}|G_m(Q)|^2\,d\nu_S^{\mathrm{sc}}(Q).
\tag{R43.10cv1}
\]
Hence \(G_m=0\) \(\nu_S^{\mathrm{sc}}\)-a.e. on \(E_0\).  Since the jet family is
countable, intersect the corresponding full-measure sets to obtain one Borel
\(E\subset E_0\) such that
\[
\nu_S^{\mathrm{sc}}((0,S)\setminus E)=0,
\qquad
G_m|_E=0
\quad
\nu_S^{\mathrm{sc}}\text{-a.e. for every }m\ge1.
\tag{R43.10cv2}
\]
If
\[
\nu_S^{\mathrm{sc}}\ne0,
\]
then the closed subspace
\[
\mathcal H_E
:=
\{F\in L^2((0,S),d\nu_S):F=0\text{ a.e. on }E^c\}
\simeq
L^2(E,d\nu_S^{\mathrm{sc}})
\]
is nonzero.  Because \(|E|=0\), its ambient measure is purely the singular part there,
and R43.10cv2 makes \(\mathcal H_E\) orthogonal to every \(G_m\).  This contradicts
the density R43.10ct.

Therefore
\[
\boxed{
\nu_S^{\mathrm{sc}}=0.
}
\tag{R43.10cw}
\]

Equivalently:
\[
\boxed{
\textbf{GC-AC holds at candidate level.}
}
\tag{R43.10cx}
\]

This argument does **not** require pointwise positivity of \(\gamma_1'\), and it does not
require \(\det H_\Gamma>0\) a.e.  It uses only:

1. scalar multiplicity one of the constrained Gamma nest;
2. analyticity/absolute continuity of each higher-jet scalar nest measure;
3. totality of the compatible jet functionals.

### 3K.6 Consequence: terminal-free Gamma cyclicity closes at candidate level

Combining R43.10cx with Section 3J gives
\[
\boxed{
\overline{
J_{R,S}\mathscr G_R^0
+
\operatorname{span}\{P_Q^\Gamma g_S:R<Q<S\}
}
=
\mathscr G_S^0.
}
\tag{R43.10cy}
\]
Equivalently,
\[
\boxed{
\overline{
Y_{R,S}V_R+
\operatorname{span}\{Y_{Q,S}\zeta_Q:R<Q<S\}
}
=
V_S.
}
\tag{R43.10cz}
\]

Hence every weak cluster of
\[
w_U=W_{R,S}^{[U]}\varepsilon_R
\]
is forced onto the single target-normal line:
\[
\boxed{
w\in\mathbb C\varepsilon_S.
}
\tag{R43.10da}
\]

At this candidate stage, the entire terminal-free Gamma-density front is closed.

The remaining Strong-Terminal problem is therefore only
\[
\boxed{
b_U
=
\langle
W_{R,S}^{[U]}\varepsilon_R,
\varepsilon_S
\rangle
\to b,
\qquad
|b|=1
\quad?
}
\tag{R43.10db}
\]

### Status of Section 3K

Section 3K remains an **AI-GREEN candidate** derived after the source-checked GC-AC
split.  The all-(m) holomorphy step R43.10cq0--R43.10cs is now written explicitly rather
than imported by analogy, and Section 3K.5 records why the scalar model is independent of
the nonunique canonical realization.  The final measure-model step R43.10cu--R43.10cw
still depends on the scalar multiplicity-one candidate from Sections 3G--3J and requires
independent review on this hardened head before freeze.

No R37/G4c conclusion is used.  No Strong-Terminal promotion is booked.


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

Under the candidate GC-AC closure, Section 7A below makes this route exact.  Write
\[
W_U\varepsilon_R=b_U\varepsilon_S+h_U,
\qquad h_U\in H_S^0.
\]
Then \(b_U\in\mathbb R\), \(h_U\rightharpoonup0\), and
\[
\|h_U\|^2=1-b_U^2.
\]
Thus the unresolved no-escape problem is precisely whether the weakly vanishing tangential
remainder is uniformly tight in a fixed dense finite-dimensional exhaustion of \(H_S^0\).
Section 7A gives an if-and-only-if tail criterion.

### Route C — third hard-constraint / edge layer

Use the bounded rescaled edge forms
\[
\mathfrak e_{X,U}^{E}
=
U D_U(\mathcal N_{X,U}\cdot,\mathcal N_{X,U}\cdot)
\]
together with the next boundary coefficient
\[
\frac{3}{8U^2}\beta^{(2)}.
\]
The scalar \(UD_U(z_U,z_U)\) is source-compatible and cannot by itself decide the relative
polar angle; the genuinely new datum would be a target off-block before square-root/polar
functional calculus.

### Route D — Gamma radius-nest multiplicity

Use R43.10n--R43.10aj.  The reviewed intermediate-radius cyclicity gate is equivalent to
cyclicity of one fixed Gamma-Riesz vector \(g_S\) under the projection nest
\[
P_Q^\Gamma.
\]
The exact scalar nest distribution is
\[
\|P_Q^\Gamma g_S\|_{\Gamma,S}^2=\gamma_Q.
\]
The new candidate analysis further reduces the issue to:

\[
\boxed{
\textbf{GC-M1: }
\mathcal N_{R,S}^\Gamma
\text{ has scalar multiplicity one in the natural radius model.}
}
\]

The reduction R43.10n--v is externally GREEN.  Sections 3F--3I now supply a new
**candidate proof** of the previously open GC-M1 gate: R43.10ak--au repairs the analyticity
gap, R43.10av--bc scalarizes the full odd Gamma nest through a diagonal canonical system,
and Lemma R43-GC1 proves that the compatible \(\beta^{(0)}\) hyperplane constraint preserves
scalar nest multiplicity.

Sections 3J--3K now split and then candidate-close this route:

- \(\textbf{GC-M1}_{\rm scalar}\): scalar multiplicity one, candidate-GREEN;
- \(\textbf{GC-AC}\): candidate-closed by the total higher-jet Riesz family in
  R43.10cq0--R43.10cw.

The exact-head hardening review subsequently repaired two presentation-level proof hazards:
the Bessonov--Denisov theorem-number version ambiguity and the sesquilinear-Riesz
holomorphy convention.  The latter is now handled by the real symmetric form and its
complex-bilinear complexification R43.10z0.

Therefore Route D is no longer the active mathematical obstruction at candidate level.
It remains a review/freeze dependency.  Conditional on this candidate closure, the live
Strong-Terminal obstruction is the scalar \(b_U\) and its tangential no-escape defect
described next.

---

## 7A. Last Strong-Terminal scalar after GC-AC: reality and exact no-escape defect

Assume the candidate GC-AC conclusion R43.10cx, hence the terminal-free cyclicity
R43.10cy--R43.10da.  Put
\[
w_U:=W_{R,S}^{[U]}\varepsilon_R,
\qquad
b_U:=\langle w_U,\varepsilon_S\rangle.
\]

### 7A.1 The residual scalar is real

Let \(\mathcal C_Xf=\overline f\) be complex conjugation on the odd graph space.
The Gamma form, the finite hub/rest operators, the Schur term, and zero extension all have
real coefficients/kernels.  Therefore every finite-terminal metric \(G_{X,U}\) commutes
with \(\mathcal C_X\).  Positive functional calculus gives the same commutation for
\(G_{X,U}^{\pm1/2}\), and hence
\[
\mathcal C_S W_{R,S}^{[U]}
=
W_{R,S}^{[U]}\mathcal C_R.
\tag{R43.44}
\]

The boundary functional \(\beta_X^{(0)}\) is real.  Its normalized Riesz normal
\(\varepsilon_X\) is therefore fixed by conjugation when the canonical positive phase
\(\beta_X^{(0)}(\varepsilon_X)>0\) is chosen.  Consequently
\[
\boxed{
b_U\in\mathbb R,
\qquad -1\le b_U\le1.
}
\tag{R43.45}
\]
Thus the last phase ambiguity is only a possible **sign** ambiguity; there is no genuinely
complex terminal phase.

### 7A.2 Orthogonal defect decomposition

Because
\[
H_S^0=\varepsilon_S^\perp,
\]
define
\[
\boxed{
h_U
:=
P_{H_S^0}w_U
=
w_U-b_U\varepsilon_S.
}
\tag{R43.46}
\]
Since \(W_U\) is an isometry and \(\|\varepsilon_R\|=\|\varepsilon_S\|=1\),
\[
\boxed{
\|h_U\|^2
=
1-b_U^2.
}
\tag{R43.47}
\]

Candidate GC-AC gives R43.10da: every weak cluster of \(w_U\) lies in
\(\mathbb C\varepsilon_S\).  Hence
\[
\boxed{
h_U\rightharpoonup0
\quad\text{in }H_S^0.
}
\tag{R43.48}
\]
Indeed, a fixed tangential test vector detecting a nonzero subsequential limit would produce
a weak cluster of \(w_U\) with a nonzero \(H_S^0\)-component, contradicting R43.10da.

For two terminals \(T,U\), the fixed orthogonal splitting gives the exact identity
\[
\boxed{
\|w_U-w_T\|^2
=
(b_U-b_T)^2
+
\|h_U-h_T\|^2.
}
\tag{R43.49}
\]
Combining this with R43.5,
\[
\boxed{
2-2L_{R,S}^{T,U}
=
(b_U-b_T)^2
+
\|h_U-h_T\|^2.
}
\tag{R43.50}
\]

Since \(h_U\rightharpoonup0\), a strongly Cauchy \(h_U\)-orbit can only converge
strongly to zero.  Therefore, under candidate GC-AC,
\[
\boxed{
\text{Strong Terminal for the fixed pair }R<S
\iff
\bigl[b_U\text{ is Cauchy}\bigr]
\ &\bigl[b_U^2\to1\bigr].
}
\tag{R43.51}
\]
Equivalently,
\[
b_U\to+1
\quad\text{or}\quad
b_U\to-1.
\]
No sign is selected at this stage.

### 7A.3 Exact finite-dimensional tightness criterion for no escape

Choose any increasing finite-dimensional sequence
\[
F_1\subset F_2\subset\cdots\subset H_S^0
\]
whose union is dense in the candidate-closed cyclic space.  Such an exhaustion can be
chosen from a countable dense subset of the generators in R43.10g/R43.10cy: tangential
limit vectors from \(\operatorname{Ran}W_{R,S}^{(0)}\) together with intermediate-radius
Gamma generators.

For every fixed \(N\), weak convergence R43.48 and finite dimensionality imply
\[
\|P_{F_N}h_U\|\longrightarrow0.
\tag{R43.52}
\]
Hence
\[
1-b_U^2
=
\|P_{F_N}h_U\|^2
+
\|(I-P_{F_N})h_U\|^2,
\]
and therefore
\[
\boxed{
b_U^2\to1
\iff
\lim_{N\to\infty}
\limsup_{U\to\infty}
\|(I-P_{F_N})h_U\|
=
0.
}
\tag{R43.53}
\]

This is the exact **B-TIGHT** form of the last no-escape gate.  GC-AC supplies every fixed
coordinate; what remains is a uniform tail estimate preventing those coordinates from
running to infinity inside the fixed target graph Hilbert space.

Thus R43 has now separated the final scalar problem into two sharply stated tasks:

1. **B-TIGHT:** prove R43.53, equivalently \(b_U^2\to1\);
2. **B-SIGN/Cauchy:** prove that the real scalar \(b_U\) has one terminal sign/limit.

If a future theorem establishes suitable terminal continuity of \(b_U\), then B-TIGHT
would automatically force eventual sign constancy.  Such continuity is **not** imported
here; it is not presently a booked R4/R5 theorem.

### 7A.4 Canonical jet-ONB form of B-TIGHT

Use the complete canonical C6a jet ONB in the target,
\[
e_{S,0}=\varepsilon_S,
\qquad
\{e_{S,n}:n\ge1\}\text{ an ONB of }H_S^0.
\]

#### Coordinate-provenance firewall

These vectors are the **canonical C6a orthonormal basis in the fixed target graph Hilbert
metric**.  They are not the higher-jet Gamma-Riesz family
\(\{g_{m,S}\}\) used in Section 3K to close GC-AC.  Accordingly the coefficients below
are genuine ONB Fourier coefficients and Parseval is exact; no Riesz-basis or frame theorem
for the Section-3K Riesz vectors is being assumed.

The normalization is also already fixed by C6a: each one-dimensional jet layer is normalized
to graph-Hilbert norm one and its remaining phase is fixed by positivity of the first active
jet.  Thus the index \(n\) below labels canonical orthogonal jet **layers**; it is not a raw
derivative coefficient such as \(f^{(n)}(0)\) or \(f^{(n)}(0)/n!\).

Set
\[
c_{n,U}
:=
\langle
W_Ue_{R,0},
e_{S,n}
\rangle.
\tag{R43.54}
\]
Then
\[
c_{0,U}=b_U\in\mathbb R,
\qquad
c_{n,U}\longrightarrow0
\quad(n\ge1\text{ fixed})
\tag{R43.55}
\]
by R43.48.  Parseval gives the exact identity
\[
\boxed{
1-b_U^2
=
\sum_{n\ge1}|c_{n,U}|^2.
}
\tag{R43.56}
\]
Therefore
\[
\boxed{
\text{B-TIGHT}
\iff
\lim_{N\to\infty}
\limsup_{U\to\infty}
\sum_{n>N}|c_{n,U}|^2
=
0.
}
\tag{R43.57}
\]

This exhibits the remaining obstruction as an exact failure-of-uniform-summability problem:
GC-AC proves
\[
c_{n,U}\to0
\quad\text{for every fixed }n,
\]
but Strong Terminal still requires permission to pass that fixed-coordinate limit through
the infinite Parseval sum.

A concrete sufficient target is now immediate.  Let \(\omega_n\uparrow\infty\).  If one
can prove
\[
\boxed{
\sup_{U\ge U_0}
\sum_{n\ge1}
\omega_n|c_{n,U}|^2
<\infty,
}
\tag{R43.58}
\]
then
\[
\sum_{n>N}|c_{n,U}|^2
\le
\frac{1}{\omega_{N+1}}
\sum_{n>N}\omega_n|c_{n,U}|^2,
\]
uniformly in \(U\), and hence B-TIGHT follows.  The simplest named subgate is
\[
\boxed{
\textbf{B-JMOM: }
\sup_{U\ge U_0}
\sum_{n\ge1}(1+n)|c_{n,U}|^2
<\infty.
}
\tag{R43.59}
\]
B-JMOM is sufficient, not claimed necessary.

#### 7A.4a Canonical compact-resolvent reformulation

The ONB makes the abstract compactness route completely canonical.  Define the positive
selfadjoint **jet-number operator**
\[
\boxed{
N_S e_{S,n}=n e_{S,n},
\qquad n\ge1,
}
\tag{R43.59a}
\]
on \(H_S^0\), with
\[
\mathcal D(N_S)
=
\left\{
x=\sum_{n\ge1}x_ne_{S,n}:
\sum_{n\ge1}n^2|x_n|^2<\infty
\right\}.
\]
Its resolvent is compact because its eigenvalues have multiplicity one and tend to
\(+\infty\).  Its form domain is
\[
\mathcal D(N_S^{1/2})
=
\left\{
x:
\sum_{n\ge1}n|x_n|^2<\infty
\right\}.
\tag{R43.59b}
\]
Since
\[
h_U
=
\sum_{n\ge1}c_{n,U}e_{S,n},
\]
B-JMOM is exactly the uniform form-energy bound
\[
\boxed{
\sup_{U\ge U_0}
\left\|(I+N_S)^{1/2}h_U\right\|^2
<\infty.
}
\tag{R43.59c}
\]

More generally, for any monotone weight \(\rho_n\uparrow\infty\), define
\[
N_{S,\rho}e_{S,n}=\rho_ne_{S,n}.
\tag{R43.59d}
\]
Then \((I+N_{S,\rho})^{-1}\) is compact and
\[
\boxed{
\sup_{U\ge U_0}
\langle (I+N_{S,\rho})h_U,h_U\rangle
<\infty
\Longrightarrow
\text{B-TIGHT}.
}
\tag{R43.59e}
\]
Indeed the form-unit ball of a positive compact-resolvent operator is relatively compact in
\(H_S^0\).  Every subsequence of \(h_U\) therefore has a strongly convergent
subsubsequence; R43.48 forces every such strong limit to equal the unique weak limit \(0\).
Hence \(\|h_U\|\to0\).

Thus the polynomial choice \(\rho_n=1+n\) is only one convenient sufficient route.
Logarithmic, fractional, superlinear, or any other coercive weight is equally legitimate.

#### 7A.4b Higher-jet holomorphy does not by itself give B-JMOM

Section 3K proves local holomorphy for each fixed higher-jet Riesz datum and estimates of the
form
\[
\|\partial_Q^k b_{m,Q}\|
\le
C_{m,k,Q_0}.
\]
Those statements have the quantifier order
\[
\forall m\quad \exists C_{m,k,Q_0}<\infty.
\]
They do **not** provide any summable or coercively weighted control as \(m\to\infty\).
Moreover the Section-3K vectors \(g_{m,S}\) are a total Riesz family used for the GC-AC
measure argument, whereas R43.54 uses the distinct canonical C6a ONB \(e_{S,n}\).
Consequently there is currently no booked implication
\[
\{C_{m,k,Q_0}\text{ fixed-}m\text{ bounds}\}
\Longrightarrow
\text{R43.59c}.
\tag{R43.59f}
\]

Any attempt to derive B-TIGHT from Section 3K must therefore supply an additional quantitative
bridge: for example a controlled triangular/change-of-basis estimate from the higher-jet
Riesz data to the C6a ONB, or a direct estimate of the compact-resolvent energy
\(\langle N_{S,\rho}h_U,h_U\rangle\).

This identifies the primary B-TIGHT target as **uniform compactness of the normal remainder
in the fixed C6a coordinates**, not merely higher-jet holomorphy.

### 7A.5 Why R27 strong inverse-root convergence does not close B-TIGHT

One tempting shortcut is to upgrade the frozen R27 strong convergence
\[
A_X(U)^{-1/2}
\xrightarrow[s]{}
L_X^{-1/2}P_{V_X}
\]
to operator-norm convergence and then attempt to control the moving normal uniformly.
The available P11 geometry does not justify that upgrade.

Frozen R42 has
\[
a_0I\le L_X\le I
\quad\text{on the infinite-dimensional }V_X.
\]
Consequently
\[
L_X^{-1/2}\ge I
\quad\text{on }V_X,
\]
so the strong limit \(L_X^{-1/2}P_{V_X}\) is **not compact**.  The usual compact-dominance
route from strong to norm convergence is therefore unavailable.  Moreover the current
R24/R27 stack does not book an operator monotonicity in the terminal parameter \(U\) that
would supply an independent monotone-norm theorem.

Thus
\[
\boxed{
\text{R27 strong inverse-root convergence}
\not\Rightarrow
\text{the uniform jet-tail control R43.57.}
}
\tag{R43.60}
\]
This is a firewall against reintroducing the fixed-vector-to-uniformity jump in a disguised
functional-calculus form.

### 7A.6 Cross-terminal sign reduction and boundary-parameter firewall

The decomposition R43.46 also gives an exact scalar formula for the canonical R5/R39
two-terminal observable.  For terminals \(T,U\),
\[
\boxed{
L_{R,S}^{T,U}
=
b_Tb_U
+
\operatorname{Re}\langle h_T,h_U\rangle.
}
\tag{R43.61}
\]
Indeed,
\[
\langle w_T,w_U\rangle
=
b_Tb_U+\langle h_T,h_U\rangle
\]
because the normal/tangential splitting
\(H_S^0\oplus\mathbb C\varepsilon_S\) is orthogonal and the coefficients \(b_T,b_U\)
are real.

Under B-TIGHT, R43.47 gives
\[
\|h_U\|\longrightarrow0.
\]
Hence Cauchy--Schwarz yields the two-terminal asymptotic
\[
\boxed{
L_{R,S}^{T,U}-b_Tb_U
\longrightarrow0
\qquad(T,U\to\infty).
}
\tag{R43.62}
\]
Combining this with the exact R39 criterion therefore sharpens R43.51:
\[
\boxed{
\text{under candidate GC-AC + B-TIGHT,}qquad
\text{Strong Terminal}
\iff
b_Tb_U\longrightarrow1.
}
\tag{R43.63}
\]

This also makes a sign failure maximally visible.  If cofinal terminal sequences
\(T_n,U_n\to\infty\) have opposite asymptotic signs, then B-TIGHT gives
\[
b_{T_n}b_{U_n}\to-1,
\qquad
\operatorname{Re}\langle h_{T_n},h_{U_n}\rangle\to0,
\]
so
\[
\boxed{
L_{R,S}^{T_n,U_n}\to-1,
\qquad
\|w_{U_n}-w_{T_n}\|^2\to4.
}
\tag{R43.64}
\]
Thus the post-B-TIGHT remainder is exactly an orientation/sign-coherence problem, not a
small norm defect.  We call it
\[
\boxed{
\textbf{B-SIGN: eventual sign coherence of }b_U.
}
\tag{R43.65}
\]

There is a simple sufficient route which is useful to isolate even though it is not yet
proved for the concrete terminal family.  The weakest natural scalar regularity needed here
is the **intermediate value (Darboux) property** on a connected terminal tail.  Under
B-TIGHT, \(|b_U|>1/2\) for all sufficiently large \(U\).  A real Darboux function on the
connected interval \([U_0,\infty)\) cannot pass from the positive component to the negative
component without taking the value zero.  Consequently
\[
\boxed{
\text{B-TIGHT + eventual Darboux property of }b_U
\Longrightarrow
\text{B-SIGN}
\Longrightarrow
\text{Strong Terminal}.
}
\tag{R43.66}
\]
Eventual continuity or real analyticity would each imply the required Darboux property, but
they are stronger than necessary.  Direct eventual positivity of \(b_Tb_U\), or of the
cross coefficient \(L^{T,U}\) together with R43.62, is another sufficient orientation
route.

The parameter \(U\) here genuinely ranges over the connected real tail of terminal radii.
Nevertheless no Darboux, continuity, analyticity, or jump-control theorem for the concrete
map \(U\mapsto b_U\) is currently booked by R4/R5.  In particular the finite-adic
terminal formulas contain arithmetic cutoff/floor changes as \(U\) varies, so scalar
regularity must be proved rather than inferred from formal dependence on a real parameter.

Finally, the current P11 definition is
\[
b_U
=
\langle W_{R,S}^{[U]}\varepsilon_R,\varepsilon_S\rangle,
\]
a fixed matrix coefficient of the normalized finite-terminal transport.  No identity in the
present stack identifies \(b_U\) with a de Branges/canonical-system boundary parameter,
an Aleksandrov--Clark parameter, or a boundary condition at \(t=0\).  Therefore no
Clark-measure stability theorem may be imported to control its sign or modulus without a
new theorem establishing precisely such an identification:
\[
\boxed{
\text{current }b_U
\text{ is a transport coefficient, not a booked Clark/boundary parameter.}
}
\tag{R43.67}
\]

The live order of attack is therefore:

1. **B-TIGHT**: prove \(b_U^2\to1\), equivalently R43.53/R43.57;
2. **B-ORIENT**: prove either B-SIGN directly through R43.61--R43.63 or sufficient terminal
   orientation regularity such as R43.66.

B-JMOM remains only one sufficient route to the first item.

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

## External review ledger — Phase I head `5432ec1a9d845d63316a2eccc28662545a0c7619`

Independent destructive review of the exact Phase-I head reported:

- **R43.1--R43.6:** GREEN;
- **R43.10a--R43.10m:** GREEN, including the intermediate-radius cocycle reduction and the
  terminal-free Gamma cyclicity gate;
- **R43 §4 and §6A firewalls:** GREEN;
- **R43.31:** structurally plausible, but **not yet externally verified** because the
  quantitative estimates R43.19--R43.22 and the passage through R43.23--R43.30 remain
  insufficiently expanded.

Accordingly:
\[
\boxed{
\text{R43.10a--m: independently reviewed GREEN on the exact Phase-I head;}
}
\]
\[
\boxed{
\text{R43.31: AI-GREEN analytic candidate only.}
}
\]

No freeze is recorded for R43 as a whole.

**Post-review extension:** Commit `8f7ef972caf7ea1237db98be21b194cc645c6799`
added R43.10n--R43.10aj, later reconciled on mathematical head
`92acea23ecea203a823b3df22744dd086276ff59`.

A second independent destructive review of that exact mathematical head reported:

- **R43.10n--R43.10v:** GREEN. The intrinsic one-vector Gamma projection-nest reduction,
  the identity \(P_Q^\Gamma g_S=J_{Q,S}g_Q\), and
  \(\|P_Q^\Gamma g_S\|_{\Gamma,S}^2=\gamma_Q\) were checked and found correct.
- **R43.10w--R43.10af:** not yet GREEN. The analyticity route remains plausible, but
  R43.10z still needs an explicit uniform complex-sector denominator bound and a
  summable common majorant for the complete R33 series / local \(Q\)-derivatives.
- **R43.10ag--R43.10aj:** the conditional Hilbert-space implication
  `multiplicity-one Lebesgue model => cyclicity` is GREEN.
  **GC-M1 itself was still open on that reviewed head.**

Accordingly, for the exact reviewed head
`92acea23ecea203a823b3df22744dd086276ff59`:
\[
\boxed{
\text{R43.10n--v: independently reviewed GREEN;}
}
\]
\[
\boxed{
\text{R43.10w--af: analytic candidate only;}\qquad
\text{GC-M1: open on the reviewed head.}
}
\]

### Post-review GC-M1 candidate proof

After that review, the following mathematical commits were added:

- `6b030843d724defafad8110ae14e06f40b642fb3`: construct explicit
  R43.10z repair, canonical-system scalarization, Lemma R43-GC1, and candidate GC-M1 closure;
- `306094a8d92d9fd88d9c42c24709ff4110060033`: harden operator holomorphy,
  fixed-radius Gamma core and Hardy/Volterra details;
- `8880c0e9fe101802cdf86c1702ab1aab09addd3e`: repair the fixed-radius
  dilation-density argument using uniform dilation bounds plus Schwartz density;
- `bf22a185856e77279f8126211c3b760d8cbebc12`: harden the canonical
  type/determinant parametrization and exclude hidden jump channels.

Thus GC-M1 is no longer merely an unformulated open gate: there is now an explicit
**AI-GREEN candidate proof** in Sections 3F--3I.  None of those post-review statements is
covered by the external GREEN verdict above.

Booking at that post-review stage:
\[
\boxed{
\text{GC-M1: candidate-closed, independently unreviewed;}
}
\]
\[
\boxed{
\text{R43.10bs--bu: Gamma cyclicity / one-line weak-cluster confinement candidate only.}
}
\]

Historical booking at that stage:
\[
\boxed{
\text{R43 overall OPEN — reviewed lower layers + unreviewed GC-M1 candidate proof.}
}
\]
\[
\boxed{
\text{Strong Terminal / C6 remains }?[O];
\text{ the candidate reduction leaves the scalar }b_U\text{ gate.}
\]

### Current exact-head hardening after GC-AC and the \(b_U\) reduction

The historical external GREEN verdicts above remain scoped **only** to their stated exact
heads.  They are not silently propagated to later mathematics.

Subsequent hardening on branch \(\texttt{research/r43-gcac-hardening}\) added:

- the source-version/type-radius repair (published Bessonov--Denisov inverse theorem =
  Theorem 2.4; separately posted extended version = Theorem 2.5; generalized-inverse
  radius \(L_H(Q)\));
- the real-form complexification firewall R43.10z0 for Riesz analyticity;
- the explicit all-\(m\) higher-jet argument R43.10cq0--R43.10cw, which
  **candidate-closes GC-AC**;
- the explicit singular-support step R43.10cv0--R43.10cv2 in the final GC-AC
  measure contradiction;
- the real last scalar / no-escape decomposition R43.44--R43.53;
- the canonical jet-tail formulation R43.54--R43.59 and the R27 operator-norm shortcut
  firewall R43.60;
- the cross-terminal sign/orientation reduction R43.61--R43.67.

The current mathematical-content head for those statements is
\[
\boxed{
\texttt{7647bc257f72e9f42e5be367292f20ced2136171}
}
\]
with mathematical-content R43 blob
\[
\boxed{
\texttt{56cf95087c849d21c07ffa2748e975635728150c}.
}
\]
Relative to the earlier \(\texttt{ade2cd34...}\) hardening, this mathematical layer also:

- fixes the scalar model once for the whole R43.10ct--R43.10cw contradiction;
- records explicitly that R43.54 uses the canonical C6a ONB, not the Section-3K higher-jet
  Riesz family;
- introduces the canonical compact-resolvent jet-number operator R43.59a--R43.59e;
- records the quantifier/change-of-basis firewall R43.59f against deriving B-JMOM from
  fixed-\(m\) holomorphy alone;
- weakens the sufficient B-SIGN regularity route from continuity to the Darboux property.
- quantifies the local higher-jet holomorphy constants by the explicit at-most-exponential
  bound R43.10cq1a--R43.10cq1c and isolates the remaining uniform jet-basis conditioning
  gap R43.10cq1d.

Later commits which only reconcile review provenance or navigation do not enlarge that
mathematical proof scope.

A user-supplied Perplexity destructive review reports all seven GC-AC hardening targets GREEN
on the exact earlier head
\[
\texttt{c7c6f04cd601ea868cb536327504f6c90b3f0807}
\]
with R43 blob
\[
\texttt{74a91c71b8b08f60d448811c57ceeca6f6113c87}.
\]
Because that review explicitly reused destructive vectors from a previous turn, it is booked
as **external destructive GREEN (cross-model nonblind)** rather than formal
\(\texttt{independent GREEN (cross-model)}\).  It does not cover the later
R43.10cv0--cv2 or R43.61--R43.67 additions.

Current candidate booking is therefore:
\[
\boxed{
\mathrm{GC\!-\!M1}_{\rm scalar}
\text{ candidate-GREEN;}
\qquad
\mathrm{GC\!-\!AC}
\text{ candidate-closed;}
}
\]
\[
\boxed{
b_U\in\mathbb R,
\qquad
\text{Strong Terminal}
\iff
[b_U\text{ Cauchy}]\ \&\ [b_U^2\to1]
\quad\text{(conditional on candidate GC-AC).}
}
\]
Under B-TIGHT this sharpens to
\[
\boxed{
\text{Strong Terminal}
\iff
b_Tb_U\to1,
}
\]
and B-SIGN/B-ORIENT is the remaining orientation gate.  No identity with an
Aleksandrov--Clark or canonical-system boundary parameter is currently booked.

\[
\boxed{
\text{B-TIGHT remains the primary OPEN gate;}
\quad
\text{B-JMOM / compact-resolvent energy are sufficient subroutes;}
\quad
\text{B-SIGN/B-ORIENT remains secondary OPEN.}
}
\]

No new \(\texttt{independent GREEN}\), freeze, \(\checkmark[M]\), Strong-Terminal,
Object-X, or RH promotion is generated by this hardening pass.
