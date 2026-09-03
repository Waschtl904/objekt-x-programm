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
Consequently
\[
Q\longmapsto a_Q
\]
is a holomorphic family in
\[
\mathcal B(\mathscr V_I,\mathscr V_I^*).
\tag{R43.10z}
\]

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
are holomorphic \(\mathscr V_I^*\)-valued functions of \(Q\), because the explicit
kernels
\[
\phi_m(u)=\operatorname{sgn}(u)I_m(|u|)
\]
are entire in the radial variable away from the fixed sign and are uniformly bounded on
compact \(Q\)-sets.

Let
\[
A(Q):\mathscr V_I\to\mathscr V_I^*
\]
be the coercive operator represented by \(a_Q\).  Uniform coercivity on \(I\), together
with (R43.10z), gives a locally holomorphic inverse
\[
A(Q)^{-1}.
\]
Put
\[
u_{j,Q}:=A(Q)^{-1}b_{j,Q},
\qquad j=0,1.
\tag{R43.10ab}
\]
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
is holomorphic and is exactly the pulled-back constrained Gamma-Riesz vector:
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
is real analytic on \((0,\infty)\).

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

The reduction R43.10n--v is algebraic; the real-analyticity step R43.10w--af and the
GC-M1 implication R43.10ag--aj are **new and not yet independently reviewed**.

At the present head none of A--D closes the final C6 gate.  Route D is the current primary
research direction because it is terminal-free.

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
  **GC-M1 itself remains open.**

Accordingly:
\[
\boxed{
\text{R43.10n--v: independently reviewed GREEN;}
}
\]
\[
\boxed{
\text{R43.10w--af: analytic candidate only;}\qquad
\text{GC-M1: open structural gate.}
}
\]

No claim that GC-M1 is true is booked at this head.

Current booking:
\[
\boxed{
\text{R43 Phase I: mixed reviewed/candidate status; overall still OPEN.}
\]
