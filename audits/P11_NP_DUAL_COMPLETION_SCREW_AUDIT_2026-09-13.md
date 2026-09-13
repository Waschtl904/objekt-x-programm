# P11 NP-DUAL-COMP — Screw redundancy, autocorrelation relaxation, and exact rank-2 completion

**Date:** 2026-09-13  
**Status:** theorem-level project audit; no Registry promotion.  
**Parent main:** `d3842cd47c443a05fd2a2ff43ed8667ef713f31a` / PR #110.

## 1. Purpose

This audit performs the required redundancy check of the PR #110 pole-cleared discrepancy against Suzuki's screw-function representation, audits the proposed Turán/SDP reduction, and proves an exact factor-level finite-rank completion theorem for fixed-window null-pole positivity.

Main conclusions:

1. the pole-cleared discrepancy is **not** a literature-new arithmetic object;
2. its null-pole gauge use remains exact;
3. scalar autocorrelation constraints do not exactly encode the two null-pole factor constraints;
4. fixed-window NP-GAP is exactly expressible as a rank-2 completion problem on the form domain;
5. finite numerical SDP positivity is not a theorem without rigorous tail control.

---

## 2. COMMON-JUMP notation

For fixed `a>0`, let

```math
q_a(v,w)
:=\langle X_av,X_aw\rangle-\Gamma_a\langle v,w\rangle,
```

and

```math
\mathcal Ev=(E_+(v),E_-(v))^T,
```

where

```math
E_+(v)=\int_{-a}^a v(x)e^{x/2}dx,
\qquad
E_-(v)=\int_{-a}^a v(x)e^{-x/2}dx.
```

Then

```math
D_{NP}(a)=\ker\mathcal E.
```

The full local Weil form is

```math
\boxed{
Q_W^a(v,w)
=q_a(v,w)+\langle\mathcal Ev,P\mathcal Ew\rangle_{\mathbb C^2},
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
}
```

Thus `Q_W^a=q_a` on null-pole.

---

## 3. Screw-function redundancy of the discrepancy `✓[M]`

Suzuki, *Weil's quadratic form via the screw function* (arXiv:2606.09096v2), contains the explicit Prime/polar pieces

```math
g_0(t)
=\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n),
```

and

```math
r_0(t)=-4(e^{t/2}+e^{-t/2}-2).
```

For `t>0`, away from jump points,

```math
\frac d{dt}g_0(t)
=\sum_{\log n\le t}\frac{\Lambda(n)}{\sqrt n},
```

and

```math
\frac d{dt}r_0(t)=-4\sinh(t/2).
```

Therefore the PR #110 cumulative discrepancy

```math
\mathfrak D(t)
=\sum_{\log n\le t}\frac{\Lambda(n)}{\sqrt n}-4\sinh(t/2)
```

satisfies

```math
\boxed{
\mathfrak D(t)=\frac d{dt}(g_0(t)+r_0(t)),\qquad t>0.
}
```

Distributionally on the positive half-line,

```math
\boxed{d\mathfrak D=(g_0+r_0)''.}
```

Suzuki also realizes the localized Weil form through the screw kernel by `B_a=D^*G_aD`. Hence the Prime+polar block is structurally canonical and literature-known.

Status:

```text
pole-cleared discrepancy identity                   ✓[M]
D as literature-new arithmetic object               ×[M]
null-pole gauge/use of known Prime+polar block       ✓[M]
publication novelty of architecture/use              ?[O]
```

---

## 4. External fixed-window baseline / Landau--Widom firewall

Xuefeng Zhu, arXiv:2608.24827v2, gives an unconditional full-class certificate

```math
Q(f)\ge 8.9\times10^{-18}\|f\|_2^2
```

at window radius `a=0.8`, together with extremely small certified upper bounds at larger windows and a Landau--Widom plunge law. The same work identifies a doubly-exponential frequency barrier for its pointwise-envelope lower-bound route.

Consequences:

- a new fixed-window literature extension must target `a>0.8`;
- tiny positive gaps are expected;
- finite-matrix positivity needs an independent rigorous tail mechanism;
- this project's completion formulation is not claimed to have overcome Zhu's barrier until such a tail theorem exists.

---

## 5. Autocorrelation transform and factor-information loss

For `v\in L^2(-a,a)` define

```math
C_v(t)=\langle T_tv,v\rangle.
```

Then

```math
C_v(-t)=\overline{C_v(t)},
\qquad
\operatorname{supp}C_v\subset[-2a,2a].
```

For real `s`, Fubini gives

```math
\boxed{
H_v(s)
:=\int_{\mathbb R}e^{st}C_v(t)dt
=E_s(v)\overline{E_{-s}(v)},
}
```

where

```math
E_s(v)=\int_{-a}^a v(x)e^{sx}dx.
```

Thus the scalar autocorrelation sees only the **product** of the two factors. It forgets how zeros are distributed between `E_s(v)` and `E_{-s}(v)`.

---

## 6. Two exact necessary autocorrelation gauges `✓[M]`

For real `v`, `C_v` is real and even, hence

```math
H_v(s)=2\int_0^{2a}C_v(t)\cosh(st)dt.
```

If `v\in D_{NP}(a)`, then

```math
E_{1/2}(v)=E_{-1/2}(v)=0.
```

So `H_v` has a zero of order at least two at `s=1/2`. Therefore

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
:=\int_0^{2a}tC_v(t)\sinh(t/2)dt=0.
}
```

Hence one may change the Prime measure, on the null-pole class, by any linear combination

```math
\eta_0\cosh(t/2)dt+\eta_1t\sinh(t/2)dt.
```

The PR #110 canonical pole-cleared gauge is `(eta_0,eta_1)=(2,0)` under this normalization.

---

## 7. Scalar Turán constraints are not exact `×[M]`

Even `L_0=L_1=0` does not imply factor-level null-pole.

The three real linear functionals

```math
v\mapsto E_{1/2}(v),
\qquad
v\mapsto E'_{1/2}(v)=\int xv(x)e^{x/2}dx,
\qquad
v\mapsto E_{-1/2}(v)
```

are independent because

```math
e^{x/2},\qquad xe^{x/2},\qquad e^{-x/2}
```

are linearly independent on every nonempty interval.

Therefore there exists real `v\in C_c^\infty(-a,a)` with

```math
E_{1/2}(v)=E'_{1/2}(v)=0,
\qquad
E_{-1/2}(v)\ne0.
```

Its autocorrelation satisfies `L_0=L_1=0`, but `v\notin D_{NP}(a)`.

Hence:

```text
one scalar moment = exact null-pole class             ×[M]
two scalar double-zero moments = exact null-pole      ×[M]
L0,L1 as necessary linear gauges                      ✓[M]
```

A scalar positive-definite/Turán optimization is an **outer relaxation**. Positivity on that larger class is sufficient for NP-GAP; failure on the relaxation does not falsify NP-GAP.

---

## 8. Form-domain setup

Let `\mathcal D_a` be the closed form domain of `q_a`. Since the COMMON-JUMP positive part is nonnegative,

```math
q_a(v)\ge-\Gamma_a\|v\|_2^2.
```

Define the positive shifted form

```math
p_a(v,w)
=q_a(v,w)+(\Gamma_a+1)\langle v,w\rangle.
```

The moment map

```math
\mathcal E:\mathcal D_a\to\mathbb C^2
```

is continuous in the form norm because it is already bounded on `L^2(-a,a)`.

It is surjective on the smooth core: the two weights `e^{x/2}` and `e^{-x/2}` are linearly independent, so two smooth compactly supported correctors with independent moment vectors can be chosen. Thus there is a finite-dimensional right inverse

```math
R_a:\mathbb C^2\to C_c^\infty(-a,a),
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

## 9. Strict rank-2 completion equivalence `✓[M]`

### Theorem

The following are equivalent.

**(A)** There exists `delta>0` such that

```math
q_a(k)\ge\delta\|k\|_2^2
\qquad(k\in\ker\mathcal E).
```

**(B)** There exist `lambda>0` and `mu>0` such that

```math
\boxed{
q_a(v)+\lambda\|\mathcal Ev\|_{\mathbb C^2}^2
\ge\mu\|v\|_2^2
\qquad(v\in\mathcal D_a).
}
```

Equivalently,

```math
\boxed{
q_a+\lambda\mathcal E^*\mathcal E\succeq\mu I.
}
```

### Proof `(A)=> (B)`

Write `v=k+R_ay`.

Since `p_a` is positive,

```math
|p_a(k,R_ay)|
\le p_a(k)^{1/2}p_a(R_ay)^{1/2}.
```

On `ker E`, assumption `(A)` gives

```math
p_a(k)
\le\left(1+\frac{\Gamma_a+1}{\delta}\right)q_a(k).
```

Because `R_a\mathbb C^2` is finite dimensional, there are constants `C_1,C_2` such that

```math
|q_a(k,R_ay)|\le C_1q_a(k)^{1/2}|y|,
```

```math
q_a(R_ay)\ge-C_2|y|^2.
```

Thus

```math
q_a(v)
\ge\frac12q_a(k)-C_3|y|^2
\ge\frac\delta2\|k\|^2-C_3|y|^2.
```

Choose `lambda>C_3`. Since `R_a` is bounded and

```math
v=k+R_ay,
```

there exists `C_R>0` with

```math
\|v\|^2\le C_R(\|k\|^2+|y|^2).
```

Therefore for some `mu>0`,

```math
q_a(v)+\lambda|y|^2
\ge\mu\|v\|^2.
```

### Proof `(B)=> (A)`

For `k\in ker E`, the completion term vanishes, so

```math
q_a(k)\ge\mu\|k\|^2.
```

This proves exact strict equivalence.

A general Hermitian `2x2` matrix `H_a` can be used in place of scalar `lambda I`; scalar completion already suffices for existence.

---

## 10. Exact semidefinite epsilon-completion `✓[M]`

The semidefinite statement is

```math
\boxed{
q_a\ge0\text{ on }\ker\mathcal E
\iff
\forall\varepsilon>0\ \exists\lambda_{a,\varepsilon}>0:
q_a+\varepsilon I+
\lambda_{a,\varepsilon}\mathcal E^*\mathcal E\succeq0.
}
```

### Forward

If `q_a\ge0` on `ker E`, then

```math
q_a+\varepsilon I\ge\varepsilon I
```

there. Apply the strict theorem to the shifted form.

### Reverse

Restrict to `ker E`:

```math
q_a(k)+\varepsilon\|k\|^2\ge0.
```

Let `epsilon` decrease to zero.

A fixed completion need not exist at a genuinely semidefinite boundary because null directions can couple linearly to the two-dimensional complement. The epsilon formulation is therefore the safe exact equivalence.

---

## 11. Relation to the actual Weil pole block

The full Weil form is

```math
Q_W^a=q_a+\mathcal E^*P\mathcal E,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

Therefore:

- `H=P` is exactly the classical pole block;
- `q_a+E^*PE>=0` is full fixed-window Weil positivity;
- null-pole positivity asks only for positivity of `q_a` on `ker E`, equivalently for some completion in the strict/epsilon sense;
- existence of an arbitrary completion does **not** identify the physical pole matrix `P`.

This is an exact finite-rank dual interface, not yet a full positive Object-X realization.

---

## 12. Turán / Fejer--Riesz scope correction

The scalar autocorrelation class is genuinely Turán-like: positive definite and compactly supported. Boas--Kac--Krein type factorization explains why half-support convolution roots are natural.

But:

1. scalar autocorrelation loses factor zero allocation;
2. the exact null-pole constraints live on the factor map `E`;
3. continuous Turán duality is not automatic merely because finite-group/finite-polynomial duality is familiar;
4. an exact finite SDP still requires a separate discretization and tail theorem.

Thus scalar Turán/SDP remains a sufficient relaxation or exploratory tool. `NP-DUAL-COMP` is the exact route.

---

## 13. Computational theorem gate

Current literature already certifies full-class positivity through `a=0.8`. The first potentially new fixed-window stress test is therefore

```text
a_test=1.0.
```

A valid certificate must predeclare and then rigorously verify:

1. basis and truncation;
2. interval entries for the form and both moment rows;
3. an optimized Hermitian `2x2` completion `H` or scalar `lambda`;
4. Arb PSD of the resolved block;
5. a rigorous lower bound for the unresolved tail / Schur complement.

A positive finite Galerkin eigenvalue alone remains diagnostic, because finite subspace minima are upper bounds for the true infimum.

---

## 14. Status

```text
COMMON-JUMP architecture                               ✓[M]
Q0 / support-preserving null-pole map                  ✓[M]
prime/polar discrepancy identity                       ✓[M]
D as literature-new arithmetic object                  ×[M]
Suzuki screw redundancy of D                           ✓[M]
null-pole correlation gauge/use                        ✓[M]
L0,L1 necessary autocorrelation gauges                 ✓[M]
scalar Turan moments = exact null-pole class            ×[M]
strict rank-2 coercive completion equivalence          ✓[M]
semidefinite epsilon-completion equivalence             ✓[M]
finite exact SDP certificate beyond a=0.8              ?[O]
all-a NP-GAP / completion                              ?[O]
forward Object-X candidate architecture                ✓[M]_part
full positive Object-X realization / RH                ?[O]
publication novelty of architecture/use                ?[O]
```

Registry and Object-X working definition remain unchanged.

## 15. Firewalls

Do not claim:

- `mathfrak D` itself is a new arithmetic object;
- one or two scalar autocorrelation moments characterize null-pole factors;
- Turán/Fejer--Riesz automatically gives a finite exact SDP;
- a finite PSD truncation proves the infinite-dimensional gap without tail control;
- existence of an arbitrary completion identifies the Weil pole matrix `P`;
- fixed-window positivity is RH-equivalent;
- all-window NP-GAP, Object X, or RH is solved;
- publication novelty is established.
