# P11 NP-DUAL-COMP — Screw redundancy, autocorrelation relaxation, and exact rank-2 completion

**Date:** 2026-09-13  
**Status:** theorem-level project audit; no Registry promotion.  
**Parent main:** `d3842cd47c443a05fd2a2ff43ed8667ef713f31a` / PR #110.  

## 1. Purpose

PR #110 introduced the null-pole correlation gauge and the pole-cleared Prime discrepancy

```math
d\mathfrak D(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dt)
-2\cosh(t/2)dt.
```

This audit performs the required redundancy check against Suzuki's screw-function representation and then replaces the potentially over-relaxed scalar-autocorrelation SDP idea by an exact factor-level finite-rank completion theorem.

The conclusions are:

1. `\mathfrak D` is **not** a literature-new arithmetic object; it is exactly the derivative of the Prime+polar component already present in Suzuki's screw function.
2. The null-pole use of that component as a correlation gauge remains an exact project identity.
3. A scalar Turán formulation using only positive definiteness, support and one autocorrelation moment is **not equivalent** to the true null-pole class.
4. Null-pole autocorrelations satisfy two exact linear necessary constraints, but these still do not characterize the factor-level null-pole condition.
5. Fixed-window NP-GAP admits an exact rank-2 completion duality on the original function/form domain.
6. A finite numerical SDP is not automatically a proof: a rigorous infinite-dimensional tail certificate is still required.

No all-window positivity and no RH claim is made.

---

## 2. Imported COMMON-JUMP notation

For fixed `a>0`, on functions supported in `(-a,a)`, let

```math
q_a(v,w)
:=\langle X_av,X_aw\rangle-\Gamma_a\langle v,w\rangle,
```

with

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
+\kappa_*,
\qquad
\kappa_*=\log\pi-\psi(1/4).
```

Define the two moment functionals

```math
E_+(v)=\int_{-a}^a v(x)e^{x/2}dx,
\qquad
E_-(v)=\int_{-a}^a v(x)e^{-x/2}dx,
```

and the moment map

```math
\mathcal Ev=(E_+(v),E_-(v))^T\in\mathbb C^2.
```

Then

```math
D_{NP}(a)=\ker\mathcal E,
```

and the full local Weil form is

```math
\boxed{
Q_W^a(v,w)
=q_a(v,w)+\langle\mathcal Ev,P\mathcal Ew\rangle_{\mathbb C^2},
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
}
```

Thus on null-pole,

```math
Q_W^a=q_a.
```

---

## 3. Literature audit: `\mathfrak D` is contained in Suzuki's screw function `✓[M]`

Suzuki, *Weil's quadratic form via the screw function* (arXiv:2606.09096v2), writes the screw function with the explicit Prime/polar part

```math
g_0(t)
=\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n),
```

and

```math
r_0(t)=-4(e^{t/2}+e^{-t/2}-2).
```

For `t>0` away from Prime-Power jump points,

```math
\frac d{dt}g_0(t)
=\sum_{\log n\le t}\frac{\Lambda(n)}{\sqrt n},
```

while

```math
\frac d{dt}r_0(t)
=-2e^{t/2}+2e^{-t/2}
=-4\sinh(t/2).
```

Therefore

```math
\boxed{
\mathfrak D(t)
=\frac d{dt}\bigl(g_0(t)+r_0(t)\bigr),
\qquad t>0.
}
```

Distributionally on the positive half-line,

```math
\boxed{
d\mathfrak D=(g_0+r_0)''.
}
```

Hence:

```text
pole-cleared discrepancy identity                    ✓[M]
D as a literature-new arithmetic object              ×[M]
null-pole gauge/use of this known component           ✓[M]
publication novelty of the use/architecture           ?[O]
```

This correction does not invalidate PR #110's identities; it only corrects novelty interpretation.

Suzuki also relates the full screw kernel directly to the localized Weil form through `B_a=D^*G_aD`, so the appearance of this Prime+polar block is structurally canonical rather than fitted.

---

## 4. External fixed-window baseline / Landau--Widom firewall

Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law* (arXiv:2608.24827v2), gives an unconditional full-class certificate at window radius `L=0.8`:

```math
Q(f)\ge 8.9\times10^{-18}\|f\|_2^2.
```

The same work obtains extremely small certified upper bounds at larger windows and identifies the Landau--Widom plunge scale, while explaining a doubly-exponential frequency barrier for its pointwise-envelope lower-bound route.

Project consequence:

- a future fixed-window certificate below or at `a=0.8` is not a literature extension;
- any computational NP-DUAL certificate intended as a new fixed-window result should target `a>0.8`;
- tiny positive gaps are expected and must not be interpreted as evidence of a missing macroscopic term;
- any finite-matrix route requires a rigorous tail mechanism.

---

## 5. Autocorrelation transform and loss of factor information

For `v\in L^2(-a,a)` define

```math
C_v(t)=\langle T_tv,v\rangle.
```

Then `C_v(-t)=\overline{C_v(t)}` and `supp(C_v)\subset[-2a,2a]`.

For real `s`, direct Fubini calculation gives the bilateral Laplace transform

```math
\boxed{
H_v(s)
:=\int_{\mathbb R}e^{st}C_v(t)dt
=E_s(v)\,\overline{E_{-s}(v)},
}
```

where

```math
E_s(v)=\int_{-a}^a v(x)e^{sx}dx.
```

At `s=1/2`, null-pole means

```math
E_{1/2}(v)=E_{-1/2}(v)=0.
```

Therefore `H_v` has a zero of order at least two at `s=1/2` (and by symmetry at `-1/2`).

### Information loss

The scalar autocorrelation sees the **product**

```math
E_s(v)\overline{E_{-s}(v)},
```

not the two factors separately. Thus a scalar positive-definite function satisfying the induced moment conditions need not come from a factor satisfying both null-pole conditions.

This is the basic firewall against treating a one-moment Turán program as an exact reformulation.

---

## 6. Two exact necessary autocorrelation gauges `✓[M]`

Restrict for clarity to real `v`; complex positivity splits into real and imaginary parts because all kernels and moment functionals are real.

Then `C_v` is real and even, and

```math
H_v(s)=2\int_0^{2a}C_v(t)\cosh(st)dt.
```

Null-pole gives

```math
H_v(1/2)=0,
\qquad
H_v'(1/2)=0.
```

Hence every real null-pole autocorrelation satisfies

```math
\boxed{
L_0(C_v)
:=\int_0^{2a}C_v(t)\cosh(t/2)dt=0,
}
```

and

```math
\boxed{
L_1(C_v)
:=\int_0^{2a}t\,C_v(t)\sinh(t/2)dt=0.
}
```

Consequently, on the null-pole class one may add to the Prime measure any linear combination

```math
\eta_0\cosh(t/2)dt
+\eta_1 t\sinh(t/2)dt
```

without changing its pairing with `C_v`.

The canonical pole-cleared choice from PR #110 corresponds, under this normalization, to

```math
(\eta_0,\eta_1)=(2,0).
```

The second coefficient is a genuine dual gauge parameter available to extremal/SDP certificates.

---

## 7. Even the two scalar constraints are not sufficient `×[M]`

The conditions `L_0(C)=L_1(C)=0` are necessary but still do not characterize null-pole factors.

Indeed the three real linear functionals on `C_c^\infty(-a,a)`

```math
v\mapsto E_{1/2}(v),
\qquad
v\mapsto E'_{1/2}(v)=\int xv(x)e^{x/2}dx,
\qquad
v\mapsto E_{-1/2}(v)
```

are linearly independent because the functions

```math
e^{x/2},\qquad xe^{x/2},\qquad e^{-x/2}
```

are linearly independent on every nonempty interval.

Hence there exists real `v\in C_c^\infty(-a,a)` such that

```math
E_{1/2}(v)=E'_{1/2}(v)=0,
\qquad
E_{-1/2}(v)\ne0.
```

For this `v`,

```math
H_v(1/2)=H_v'(1/2)=0,
```

so its autocorrelation satisfies both `L_0=L_1=0`, but `v\notin D_{NP}(a)`.

Therefore:

```text
one-moment Turan class = exact null-pole class         ×[M]
two scalar double-zero moments = exact null-pole class ×[M]
L0,L1 as necessary linear gauges                       ✓[M]
```

A scalar Turán/positive-definite optimization with these constraints is an **outer relaxation**. A positivity certificate on the relaxation is sufficient for NP-GAP, but a counterexample in the relaxation does not falsify NP-GAP.

---

## 8. Form-domain setup for exact duality

Let `\mathcal D_a` be the closed form domain of `q_a` on `L^2(-a,a)` (or initially the smooth core, followed by closure).

Because the COMMON-JUMP positive part is nonnegative,

```math
q_a(v)\ge-\Gamma_a\|v\|_2^2.
```

Thus the shifted form

```math
p_a(v,w)
:=q_a(v,w)+(\Gamma_a+1)\langle v,w\rangle
```

is positive and defines a form norm.

The moment map

```math
\mathcal E:\mathcal D_a\to\mathbb C^2
```

is continuous in the form norm because each `E_\pm` is already bounded on `L^2(-a,a)`.

It is surjective on the smooth core: choose two compactly supported smooth correctors whose moment vectors are linearly independent. Hence there exists a bounded finite-dimensional right inverse

```math
R_a:\mathbb C^2\to C_c^\infty(-a,a)\subset\mathcal D_a,
\qquad
\mathcal ER_a=I_2.
```

Every `v\in\mathcal D_a` decomposes uniquely as

```math
v=k+R_ay,
\qquad
k\in\ker\mathcal E,
\qquad
y=\mathcal Ev.
```

---

## 9. Strict rank-2 completion theorem `✓[M]`

### Theorem

Assume there exists `\delta>0` such that

```math
q_a(k)\ge\delta\|k\|_2^2
\qquad
(k\in\ker\mathcal E).
```

Then there exists `\lambda_a>0` such that

```math
\boxed{
q_a(v)+\lambda_a\|\mathcal Ev\|_{\mathbb C^2}^2\ge0
\qquad
(v\in\mathcal D_a).
}
```

Equivalently,

```math
\boxed{
q_a+\lambda_a\mathcal E^*\mathcal E\succeq0
}
```

as a form on the full domain.

Conversely, any Hermitian completion

```math
q_a(v)+\langle H\mathcal Ev,\mathcal Ev\rangle\ge0
```

implies `q_a\ge0` on `ker E`.

### Proof

Write `v=k+R_ay`, `k\in ker E`, `y=Ev`.

Since `p_a` is positive,

```math
|p_a(k,R_ay)|
\le p_a(k)^{1/2}p_a(R_ay)^{1/2}.
```

On `ker E`, strict coercivity gives

```math
p_a(k)
=q_a(k)+(\Gamma_a+1)\|k\|^2
\le\left(1+\frac{\Gamma_a+1}{\delta}\right)q_a(k).
```

Because `R_a\mathbb C^2` is finite dimensional, there are constants `C_1,C_2` such that

```math
|q_a(k,R_ay)|\le C_1 q_a(k)^{1/2}|y|,
```

and

```math
q_a(R_ay)\ge-C_2|y|^2.
```

Therefore

```math
q_a(v)
\ge q_a(k)-2C_1q_a(k)^{1/2}|y|-C_2|y|^2
\ge\frac12q_a(k)-C_3|y|^2.
```

Taking `\lambda_a\ge C_3` gives the result.

The reverse implication follows by setting `Ev=0`.

### Interpretation

Strict NP-GAP at fixed `a` is equivalent to existence of a positive **rank-at-most-two completion** of the centered COMMON-JUMP form. A general Hermitian `2x2` matrix `H_a` may be optimized, but existence already follows with `H_a=\lambda_a I_2`.

---

## 10. Exact semidefinite epsilon-completion `✓[M]`

Without a strict margin, a fixed finite completion need not exist because null directions can couple linearly to the two-dimensional complement.

The exact semidefinite statement is:

```math
\boxed{
q_a\ge0\text{ on }\ker\mathcal E
\iff
\forall\varepsilon>0\ \exists\lambda_{a,\varepsilon}>0:
q_a+\varepsilon I+
\lambda_{a,\varepsilon}\mathcal E^*\mathcal E\succeq0.
}
```

### Forward direction

If `q_a\ge0` on `ker E`, then

```math
q_a(k)+\varepsilon\|k\|^2\ge\varepsilon\|k\|^2
```

is strict there. Apply the strict theorem to the shifted form `q_a+\varepsilon I`.

### Reverse direction

Restrict the completed inequality to `ker E`:

```math
q_a(k)+\varepsilon\|k\|^2\ge0.
```

Let `\varepsilon\downarrow0`.

This is the exact fixed-window dual reformulation appropriate for the potentially zero-gap case.

---

## 11. Connection with the actual Weil pole block

Recall

```math
Q_W^a
=q_a+\mathcal E^*P\mathcal E,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

Therefore:

- `H=P` is not an arbitrary completion: it is exactly the physical/classical pole block of the full Weil form;
- proving
  ```math
  q_a+\mathcal E^*P\mathcal E\succeq0
  ```
  is full fixed-window Weil positivity;
- NP-GAP on the null-pole class asks only for positivity on `ker E`, equivalently for existence of **some** completion (strictly, or with epsilon in the semidefinite case), not necessarily `P`.

This gives a concrete finite-dimensional dual parameter space without pretending that the final Weil pole matrix has already been recovered.

---

## 12. Why this is a better SDP interface

A discretized SDP can now optimize over:

1. coefficients of `v` in a predeclared basis;
2. a Hermitian `2x2` completion matrix `H` (four real parameters), or simply a scalar penalty `lambda`;
3. rigorous tail/envelope variables needed to certify the infinite-dimensional remainder.

The null-pole constraints are preserved **exactly at factor level** rather than replaced by a scalar autocorrelation moment.

However:

```text
finite PSD matrix without tail control != theorem
```

A rigorous certificate must include an analytic or interval-certified bound on the orthogonal complement / unresolved frequency tail.

Zhu's 2026 fixed-window work illustrates both the power and the severe scaling limits of one such finite-envelope strategy. The present completion formulation does not by itself prove that the doubly-exponential barrier is avoided.

---

## 13. Turán / Fejer--Riesz scope correction

The scalar autocorrelation problem is genuinely related to Turán-type extremal problems: `C_v` is positive definite and compactly supported.

Boas--Kac--Krein factorization supplies half-support convolution roots under suitable hypotheses. Nevertheless, two cautions are binding here:

1. the scalar autocorrelation forgets which factor carries the two zeros at `±1/2`;
2. continuous Turán duality is an infinite-dimensional theorem and an exact finite SDP does not appear automatically from the words “Fejer--Riesz”.

The recent Kolountzakis--Lev--Matolcsi work explicitly distinguishes the automatic finite-group duality from the continuous case, where duality requires proof.

Therefore scalar Turán/SDP remains useful as a **sufficient relaxation** or exploratory dual, while `NP-DUAL-COMP` on the factor/form domain is the exact route.

---

## 14. Recommended computational theorem gate

The next theorem-producing numerical target should not repeat known short-window positivity.

Predeclare a fixed radius

```text
a_test > 0.8
```

with `a_test=1.0` the natural first stress point.

Required certificate architecture:

1. choose a fixed basis and truncation rule before observing the sign;
2. build the interval matrix of `q_a` and the exact two moment rows;
3. optimize a Hermitian `2x2` completion `H` or scalar `lambda`;
4. prove PSD of the resolved block in Arb;
5. prove a rigorous lower bound for the unresolved tail / Schur complement;
6. only then promote a fixed-window positivity theorem.

A positive finite Galerkin eigenvalue alone remains only an upper-bound diagnostic for the true infimum.

---

## 15. Status

```text
COMMON-JUMP architecture                               ✓[M]
Q0 / support-preserving null-pole map                  ✓[M]
prime/polar discrepancy identity                       ✓[M]
D as literature-new arithmetic object                  ×[M]
Suzuki screw redundancy of D                           ✓[M]
null-pole correlation gauge/use                        ✓[M]
one-moment Turan = exact null-pole class               ×[M]
two scalar double-zero moments = exact null-pole       ×[M]
L0,L1 necessary autocorrelation gauges                 ✓[M]
strict rank-2 completion equivalence                   ✓[M]
semidefinite epsilon-completion equivalence             ✓[M]
finite exact SDP certificate beyond a=0.8              ?[O]
all-a NP-GAP / completion                              ?[O]
forward Object-X candidate architecture                ✓[M]_part
full positive Object-X realization / RH                ?[O]
publication novelty of architecture/use                ?[O]
```

Registry and Object-X working definition remain unchanged.

---

## 16. Firewalls

Do not claim:

- `mathfrak D` itself is a new arithmetic object;
- one or two scalar autocorrelation moments characterize null-pole factors;
- Fejer--Riesz/Turan automatically yields a finite exact SDP;
- a finite PSD truncation proves the infinite-dimensional gap without tail control;
- existence of an arbitrary completion `H` identifies the Weil pole matrix `P`;
- fixed-window positivity is RH-equivalent;
- all-window NP-GAP, Object X, or RH is solved;
- publication novelty is established.
