# P11 End-to-End Referee R36-A13c — Gamma pairing rigidity and first-chamber mismatch

Date: 2026-08-20

## Purpose and firewall

This note is a separate continuation after the canonical A11' repair and the exact A13
first-terminal-chamber odd-kernel oracle.  It answers two questions that A13 intentionally left
open:

1. does the exact odd kernel pair nontrivially with the concrete annular defect
   `d_{R,S}`?;
2. does such a nonzero pairing rigorously force the annular mismatch and hence
   `s_{R,S,T_0} != 0`?

The answer is positive in the middle part of the first terminal chamber.  The proof has three
separate levels and they must not be conflated:

- A13: exact odd-kernel structure;
- A13c: Gamma-tail rigidity excludes local reflection symmetry of `d_{R,S}`;
- an explicit adjunction lemma: every localized hub-kernel vector annihilates the full Schur
  range.

No statement about R30-F for all `0<R<S<T_0`, full R36-A kernel triviality, terminal
transport, polar gauge, Object X, or RH is made.

Canonical inputs:

- R31 / `P11_O3ad_Gamma_Antilocality_Cancellation_Gate.tex`;
- R32 / `P11_O3ae_HubOffSupport_Representation.tex`;
- R33 / `P11_O3af_Gamma_Symbol_Bridge.tex`;
- R36-A9 odd-sector unitary identification;
- R36-A13 exact first-chamber/no-overlap odd-kernel oracle.

---

## 1. Typed Schur adjunction

Work on the terminal Hilbert space `L^2(-T_0,T_0)`.  The concrete finite-horizon Schur term is

\[
\Sigma_{T_0}=H_{T_0}B_{T_0}H_{T_0}^*,
\qquad
B_{T_0}=(I+R_{T_0}^*R_{T_0})^{-1},
\]

with

\[
H_{T_0}^*=-H_{T_0}.
\]

Let

\[
A=(-S,-R)\cup(R,S),
\qquad
E_A:L^2(A)\to L^2(-T_0,T_0)
\]

be zero extension and `P_A=E_A^*` restriction.  If `f` is an S-level vector, write
`\widetilde f=E_{S,T_0}f` for its zero extension to the terminal window.

### Lemma R36-A13c.1 (kernel annihilates the full Schur range)

If

\[
y\in\ker(H_{T_0}E_A),
\]

then for every terminal vector `F` one has

\[
\boxed{
\langle y,P_A\Sigma_{T_0}F\rangle_{L^2(A)}=0.
}
\tag{A13c.1}
\]

Consequently

\[
\boxed{
y\perp\overline{\operatorname{Ran}(P_A\Sigma_{T_0})}.}
\tag{A13c.2}
\]

### Proof

Using `P_A^*=E_A`, the concrete Schur factorization, and adjunction,

\[
\begin{aligned}
\langle y,P_A\Sigma_{T_0}F\rangle_A
&=\langle E_Ay,H_{T_0}B_{T_0}H_{T_0}^*F\rangle_{T_0}\\
&=\langle H_{T_0}^*E_Ay,B_{T_0}H_{T_0}^*F\rangle_{T_0}.
\end{aligned}
\]

Since `H_{T_0}^*=-H_{T_0}` and `H_{T_0}E_Ay=0`, the first factor is zero.  This proves
(A13c.1).  Orthogonality to the closure follows by continuity of the inner product.
`\square`

Status:

\[
\boxed{\text{R36-A13c.1}\quad\checkmark[M].}
\]

This is stronger than the single-vector inequality used in the earlier conditional R36-B
lemma: a localized hub-kernel vector annihilates the entire restricted Schur range.

---

## 2. Pairing reduction on the exact A13 kernel

Assume the A13 middle regime

\[
0<R<\tau<S<T_0<2\tau,
\]

and put

\[
r=\min\{S-\tau,\tau-R,2\tau-T_0\}>0.
\]

A13 gives

\[
\ker L_{R,S,T_0}
=
\left\{
 h:\operatorname{ess\,supp}h\subset(\tau-r,\tau+r),\quad
 h(\tau+t)=-h(\tau-t)\text{ a.e. }0<t<r
\right\}.
\]

Via R36-A9,

\[
U_-(\ker L_{R,S,T_0})
=
\ker(H_{T_0}E_A)\cap L^2_{\rm odd}(A).
\]

The annular defect is

\[
\boxed{
d_{R,S}:=P_A(\phi_S-C_{\Gamma,S}j_{R,S}),
\qquad
j_{R,S}=E_{R,S}\rho_{R,T_0}.
}
\tag{A13c.3}
\]

It is odd.

For `h` in the exact A13 kernel define

\[
g(t):=h(\tau+t),\qquad 0<t<r.
\]

Then `h(\tau-t)=-g(t)`.  Since

\[
(U_-h)(x)=\frac1{\sqrt2}\operatorname{sgn}(x)h(|x|)
\]

on the annulus and both `U_-h` and `d_{R,S}` are odd,

\[
\boxed{
\langle U_-h,d_{R,S}\rangle_A
=\sqrt2\int_0^r
 g(t)\,\overline{\bigl[d_{R,S}(\tau+t)-d_{R,S}(\tau-t)\bigr]}\,dt
}
\tag{A13c.4}
\]

for the convention linear in the first slot; with the opposite convention the harmless
conjugations are reversed.

Therefore

\[
\boxed{
\exists\,0\ne h\in\ker L:\
\langle U_-h,d_{R,S}\rangle\ne0
\iff
d_{R,S}(\tau+\cdot)-d_{R,S}(\tau-\cdot)\not\equiv0
\text{ in }L^2(0,r).
}
\tag{A13c.5}
\]

Indeed the right-half datum `g` is arbitrary in `L^2(0,r)`.

Status:

\[
\boxed{\text{pairing reduction}\quad\checkmark[M].}
\]

---

## 3. Exact Gamma-tail form of the defect

On the positive annulus `(R,S)`, the inherited vector `j_{R,S}` is supported in `[-R,R]`.
R31 gives the exact off-support Gamma tail with

\[
\lambda_n=2n+\frac12,
\qquad
M_n(j):=\int_{-R}^{R}j(y)e^{\lambda_n y}\,dy.
\]

R33 fixes the P11 affine symbol bridge with the explicit normalization

\[
\boxed{c_1=1.}
\tag{A13c.6}
\]

Thus, for `x>R`,

\[
(C_{\Gamma,S}j)(x)
=-\sum_{n=0}^\infty e^{-\lambda_n x}M_n(j),
\tag{A13c.7}
\]

where the series converges normally on every `x>=R+delta`.

Since on the positive side

\[
\phi_S(x)=2(1-e^{-x/2}),
\]

we obtain

\[
\boxed{
d_{R,S}(x)
=2+\sum_{n=0}^\infty A_ne^{-(2n+1/2)x},
\qquad x>R,
}
\tag{A13c.8}
\]

with

\[
A_0=M_0(j)-2,
\qquad
A_n=M_n(j)\quad(n\ge1).
\tag{A13c.9}
\]

Equivalently, with

\[
G(z):=\sum_{n=0}^\infty A_nz^n,
\]

one has

\[
\boxed{
d_{R,S}(x)-2=e^{-x/2}G(e^{-2x}).}
\tag{A13c.10}
\]

The moment estimate `|M_n(j)|=O(e^{(2n+1/2)R})` shows that `G` is holomorphic on

\[
|z|<e^{-2R}.
\]

---

## 4. Gamma reflection-rigidity lemma

### Theorem R36-A13c.2 (no local reflection symmetry outside the source support)

Fix `R<tau` and suppose a nonempty symmetric interval

\[
(\tau-\varepsilon,\tau+\varepsilon)\subset(R,S)
\]

is available.  Then the positive-annulus defect cannot be reflection-symmetric about `tau` on
that interval:

\[
\boxed{
d_{R,S}(\tau+t)\not\equiv d_{R,S}(\tau-t)
\quad\text{for }0<t<\varepsilon.
}
\tag{A13c.11}
\]

Equivalently, its odd part about `tau` is nonzero in `L^2(0,\varepsilon)`.

### Proof

Assume for contradiction that

\[
d(\tau+t)=d(\tau-t)
\]

for all sufficiently small real `t`; equality a.e. would imply the same conclusion because
both sides are real-analytic on the positive annulus.

Set

\[
q:=e^{-2\tau},
\qquad
z:=e^{-2t}.
\]

Using (A13c.10), cancellation of the constant `2` gives

\[
G(q/z)=z^{1/2}G(qz).
\tag{A13c.12}
\]

Square to remove the local square-root branch and put

\[
H:=G^2.
\]

Then

\[
H(q/z)=zH(qz).
\]

With

\[
w=qz
\]

this becomes the exact functional equation

\[
\boxed{
H(q^2/w)=\frac{w}{q}H(w).
}
\tag{A13c.13}
\]

Both sides are holomorphic on the annulus

\[
\boxed{
\mathcal R_{R,\tau}
=\{w:q^2e^{2R}<|w|<e^{-2R}\}.
}
\tag{A13c.14}
\]

The annulus is nonempty exactly when

\[
q^2e^{2R}<e^{-2R}
\iff
R<\tau.
\tag{A13c.15}
\]

Thus the same strict inequality that places the reflection centre outside the source support is
exactly the condition needed for a nonempty Laurent domain.

Equation (A13c.13) is initially obtained on a real arc around `w=q`.  Both sides are holomorphic
on the connected annulus `\mathcal R_{R,\tau}`, so the identity theorem extends it to the whole
annulus.

Write

\[
H(w)=\sum_{n=0}^\infty b_nw^n
\]

in the disk `|w|<e^{-2R}`.  On the annulus,

\[
H(q^2/w)=\sum_{n=0}^\infty b_nq^{2n}w^{-n},
\]

which contains only powers `w^0,w^{-1},w^{-2},...`, whereas

\[
\frac{w}{q}H(w)
=\sum_{n=0}^\infty \frac{b_n}{q}w^{n+1}
\]

contains only powers `w^1,w^2,...`.  Uniqueness of Laurent expansions forces

\[
b_n=0\quad\text{for every }n,
\]

hence `H=0`, `G=0`, and `A_n=0` for every `n`.

Therefore

\[
M_n(j)=0\quad(n\ge1),
\qquad
M_0(j)=2.
\tag{A13c.16}
\]

It remains to use the higher moments.  With `t=e^{2y}`, define the finite complex measure
`mu` on

\[
K=[e^{-2R},e^{2R}]
\]

by the pushforward of `e^{y/2}j(y)dy`.  Then

\[
M_n(j)=\int_K t^n\,d\mu(t).
\]

The vanishing `M_n=0` for every `n>=1` says that `mu` annihilates the span of
`{t,t^2,t^3,...}`.  Because `K` is compact and separated from `0`, this span is dense in
`C(K)`: for any `f in C(K)`, the function `f(t)/t` is continuous and can be uniformly
approximated by polynomials, so `f` is uniformly approximated by `tP(t)`.  Hence `mu=0`.
Therefore `j=0`, which forces `M_0(j)=0`, contradicting `M_0(j)=2`.

The assumed reflection symmetry is impossible.
`\square`

Status:

\[
\boxed{\text{R36-A13c.2}\quad\checkmark[M].}
\]

### Scope remark

This rigidity lemma itself does **not** use the number of active hub shifts, the one-shift
hypothesis, or `T_0<2tau`.  It uses only the exact R31/R33 Gamma tail, the explicit jet
`phi_S`, a reflection centre `tau>R`, and a nonempty symmetric subinterval contained in the
positive annulus.  In a genuine multi-shift kernel it applies only if the kernel contains an
appropriate vector with a single-centre antisymmetry; it does not manufacture such a vector.

---

## 5. First-terminal-chamber pairing theorem

Let

\[
\tau_2:=\tau_{2,1}=\frac{\log2}{2},
\qquad
\tau_3:=\tau_{3,1}=\frac{\log3}{2}.
\]

Assume

\[
\boxed{
0<R<\tau_2<S<T_0<\tau_3.
}
\tag{A13c.17}
\]

A13 applies because `T_0<tau_3<2tau_2`.  It supplies the infinite-dimensional exact kernel
with radius

\[
r=\min\{S-\tau_2,\tau_2-R,2\tau_2-T_0\}>0.
\]

Theorem A13c.2 applied with `tau=tau_2` gives

\[
d_{R,S}(\tau_2+\cdot)-d_{R,S}(\tau_2-\cdot)\not\equiv0
\quad\text{in }L^2(0,r).
\]

By (A13c.5) there exists

\[
0\ne h\in\ker L_{R,S,T_0}
\]

such that for

\[
y:=U_-h
\]

one has

\[
\boxed{
y\in\ker(H_{T_0}E_A),
\qquad
\langle y,d_{R,S}\rangle\ne0.
}
\tag{A13c.18}
\]

Status:

\[
\boxed{\text{first-chamber nonorthogonal annihilator}\quad\checkmark[M].}
\]

---

## 6. Concrete mismatch theorem

Let

\[
\widetilde j:=E_{S,T_0}j_{R,S}.
\]

The S-level annular Schur value is the restriction of the terminal Schur vector:

\[
P_A\Sigma_{T_0}\widetilde j.
\]

Lemma A13c.1 and (A13c.18) give

\[
\langle y,P_A\Sigma_{T_0}\widetilde j\rangle=0
\]

but

\[
\langle y,d_{R,S}\rangle\ne0.
\]

Hence

\[
\boxed{
P_A\Sigma_{T_0}\widetilde j\ne d_{R,S},
}
\tag{A13c.19}
\]

indeed

\[
\boxed{
d_{R,S}\notin\overline{\operatorname{Ran}(P_A\Sigma_{T_0})}.}
\tag{A13c.20}
\]

For the R31 residual

\[
\Delta_{R,S}^{[T_0]}
=\phi_S-(C_{\Gamma,S}+\Sigma_S^{[T_0]})j_{R,S},
\]

its annular restriction is

\[
P_A\Delta_{R,S}^{[T_0]}
=d_{R,S}-P_A\Sigma_{T_0}\widetilde j.
\]

Thus (A13c.19) implies

\[
\Delta_{R,S}^{[T_0]}\ne0.
\]

R31's exact annular cancellation criterion gives

\[
\Delta_{R,S}^{[T_0]}=0
\iff
s_{R,S,T_0}=0.
\]

Therefore:

### Theorem R36-A13c.3 (first-chamber strict mismatch)

If

\[
\boxed{
0<R<\frac{\log2}{2}<S<T_0<\frac{\log3}{2},
}
\]

then

\[
\boxed{
s_{R,S,T_0}\ne0.
}
\tag{A13c.21}
\]

Status:

\[
\boxed{\text{R36-A13c.3}\quad\checkmark[M].}
\]

This is a genuine positive mismatch theorem on an explicit open parameter region.  It is not
R30-F because for fixed `S,T_0` it covers only `R<tau_2` with `tau_2<S`.

---

## 7. B1 / B2 / A1 separation in the first terminal chamber

To prevent opposite kernel statements from being carried under one label, separate the three
questions.

### R36-B1 — odd annihilator obstruction

B1 asks whether there exists

\[
0\ne y\in\ker(H_{T_0}E_A)
\]

with

\[
\langle y,d_{R,S}\rangle\ne0.
\]

Throughout the first terminal chamber

\[
\tau_2\le T_0<\tau_3,
\qquad
0<R<S<T_0,
\]

A13 and A13c give the exact classification

\[
\boxed{
\text{R36-B1 fires}
\iff
R<\tau_2<S.
}
\tag{A13c.22}
\]

If `R<tau_2<S`, A13c constructs a nonorthogonal odd annihilator and proves mismatch.
If `tau_2` lies at or outside `(R,S)`, A13 says the odd localized kernel is trivial.  Since
`d_{R,S}` is odd and the kernel splits by parity, every remaining even kernel vector pairs to
zero with `d_{R,S}`.  Hence B1 cannot fire there.

Thus the **B1 route** is completely decided in the first terminal chamber.

### R36-B2 — odd-kernel-triviality fact

The statement

\[
\ker(H_{T_0}E_A)\cap L^2_{\rm odd}(A)=\{0\}
\]

holds in the first chamber exactly when `tau_2` is not strictly inside `(R,S)`.  This kills B1
only; it is not a dense-range theorem.

### R36-A1 — full dense-range gate

The full criterion remains

\[
\overline{\operatorname{Ran}(P_AH_{T_0})}=L^2(A)
\iff
\ker(H_{T_0}E_A)=\{0\}.
\]

The even kernel is still open, so neither B2 nor A13 decides R36-A1.

---

## 8. Canonical status table

| Item | Status |
|---|---|
| R36-A9 odd-sector identification | ✓[M] |
| R36-A13 exact first-chamber/no-overlap odd kernel | ✓[M] |
| R36-A13c.1 Schur-range adjunction | ✓[M] |
| R36-A13c.2 Gamma reflection rigidity | ✓[M] |
| first-chamber nonorthogonal annihilator for `R<tau_2<S` | ✓[M] |
| R36-A13c.3 strict mismatch on `0<R<tau_2<S<T_0<tau_3` | ✓[M] |
| first-chamber B1 route | fully classified: fires iff `R<tau_2<S` |
| odd kernel outside the middle case | ✓[M] trivial |
| even localized kernel | ?[O] |
| full R36-A kernel triviality | ?[O] |
| R30-F | ?[O] |

---

## 9. Next target

The first-terminal-chamber odd annihilator route is now closed in both directions.  The next
multi-shift question should not start from an asymptotic-growth heuristic.  In the two-shift
chamber the folded equation is a coupled finite four-point relation with unequal explicit
weights

\[
c_{p,1}=\sqrt{\log p}\,p^{-3/4},
\]

and only finitely many orbit points fit inside the bounded support window.  A natural next node
is therefore a finite-rank / finite-orbit analysis of the two-shift relation, with A13 and A13c
retained as regression and pairing firewalls.

R30-F remains strictly open.
