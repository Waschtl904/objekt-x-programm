# P11 End-to-End Referee R32 — antisymmetry of the source hub and annular Schur rewriting

Date: 2026-08-19 (post-audit repositioning applied)

## Target

Follow-up to R31.  R31 reduces R30-F to the concrete annular cancellation
\[
\Delta_{R,S}^{[T_0]}\ne0\quad\text{for every }0<R<S<T_0,
\]
and proves via the R31-D countermodel that Gamma anti-locality plus coarse Schur
properties (positivity, boundedness, small-Sobolev, abstract positive
factorisation) are insufficient.  The R31 audit closes with four candidate
routes, of which

> (1) an explicit off-support representation of
> \(H_{T_0}(I+R_{T_0}^*R_{T_0})^{-1}H_{T_0}^*\)

is Route 1.  This audit executes Route 1 \emph{only at the level of the outer
factor} \(H_{T_0}\).  The inverse \(B_{T_0}=(I+R_{T_0}^*R_{T_0})^{-1}\) is not
treated here, so no kernel representation of \(\Sigma_{T_0}\) is obtained.

No polar-gauge, terminal-transport, Object-X, or RH conclusion is drawn.

### Repositioning note

The original title of this audit spoke of a "discrete-translational off-support
representation ... of the source hub and Schur term".  On post-audit review,
Corollary R32-C is an \emph{annular rewriting} of \(\Sigma_{T_0}\) under
antisymmetry, not a kernel representation, because the auxiliary function
\(g=B_{T_0}H_{T_0}^*f\) is defined implicitly through a bounded nonlocal
inverse whose off-support structure is not controlled here.  The paper module
\texttt{P11\_O3ae\_HubOffSupport\_Representation.tex} carries the same
correction.  The mathematics of R32-A, R32-B, R32-C is unchanged; only the
status rhetoric has been tightened.

## Repo sync

`main` at start of this audit: `550330e4426...` — `Add R31 operator-domain second check`.

Inputs:
- `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex` §2 (source geometry).
- `papers/P11_sections/P11_O3ad_Gamma_Antilocality_Cancellation_Gate.tex` (R31).

---

## 1. Antisymmetry of the source hub

### Theorem R32-A

The bounded finite-horizon source hub satisfies
\[
\boxed{H_{T_0}^*=-H_{T_0}}
\tag{R32.1}
\]
on \(L^2(-T_0,T_0)\).

### Proof

By P11 (2.5),
\[
H_{T_0}
=P_{T_0}\!\!\sum_{(p,k)\in\mathcal P_{T_0}}\!\!c_{p,k}\,D_{k\log p}\,E_{T_0},
\qquad
c_{p,k}=\sqrt{\log p}\,p^{-3k/4},
\quad
D_s=U_{s/2}-U_{-s/2},
\]
with \(\mathcal P_{T_0}=\{(p,k):p^k\le e^{2T_0}\}\) finite.
On \(L^2(\mathbb R)\), translations are unitary and satisfy \(U_a^*=U_{-a}\), so
\[
D_s^*=U_{-s/2}-U_{s/2}=-D_s.
\]
Hence \(M^*=-M\) for \(M:=\sum c_{p,k}D_{k\log p}\).
Using \(P_{T_0}=E_{T_0}^*\) and \((P_{T_0})^*=E_{T_0}\),
\[
H_{T_0}^*
=(P_{T_0}ME_{T_0})^*
=E_{T_0}^*M^*P_{T_0}^*
=P_{T_0}(-M)E_{T_0}
=-H_{T_0}.
\qquad\square
\]

Status:
\[
\boxed{\text{R32-A (antisymmetry \(H_{T_0}^*=-H_{T_0}\))}\quad\checkmark[M].}
\]

### Remark

This property is not previously recorded in P11.  It is closely analogous to the
antisymmetric Jacobi decomposition \(J_N^-=\tfrac12(\Theta_N-\Theta_N^\dagger)\)
used in P06/P08/P10, but here it holds \emph{exactly} rather than as a formal
symmetrisation, because the P11 hub is built directly from odd translation
differences.

---

## 2. Exact off-support representation of the source hub

### Theorem R32-B

Fix \(0<R<T_0\).  Let \(f\in L^2(-T_0,T_0)\) with
\(\operatorname{ess\,supp}(f)\subset[-R,R]\).  Then for a.e.
\(u\in(-T_0,-R)\cup(R,T_0)\),
\[
\boxed{
(H_{T_0}f)(u)
=\operatorname{sgn}(u)\!\!\sum_{\substack{(p,k)\in\mathcal P_{T_0}\\|u|-R\le\tau_{p,k}\le|u|+R}}\!\!\!c_{p,k}\,f\bigl(u-\operatorname{sgn}(u)\tau_{p,k}\bigr),
}
\tag{R32.2}
\]
where \(\tau_{p,k}:=\tfrac{k\log p}{2}\).

### Proof

For \(u>R\):
- \(u+\tau_{p,k}>R\), so \(f(u+\tau_{p,k})=0\).
- \(f(u-\tau_{p,k})\ne0\) only if \(u-\tau_{p,k}\in(-R,R)\), i.e.
  \(\tau_{p,k}\in(u-R,u+R)\).

The action of \(D_{k\log p}\) at \(u\) reads
\((D_{k\log p}f)(u)=f(u-\tau_{p,k})-f(u+\tau_{p,k})\).
Since \(u<T_0\), \(P_{T_0}\) acts trivially on the resulting function at this
point.  Sum over \(\mathcal P_{T_0}\) to obtain
\[
(H_{T_0}f)(u)=\sum_{(p,k):\tau_{p,k}\in(u-R,u+R)}c_{p,k}\,f(u-\tau_{p,k})
\qquad(u>R).
\]
For \(u<-R\) the symmetric argument gives the \(\operatorname{sgn}\)-adjusted formula.
\(\square\)

Status:
\[
\boxed{\text{R32-B (exact off-support formula for }H_{T_0})\quad\checkmark[M].}
\]

### Numerical check

An independent grid computation with prime pairs
\((p,k)\in\{(2,1),(3,1),(2,2),(5,1),(7,1),(2,3),(3,2),(11,1),(13,1)\}\)
and \(f(x)=\sin(\pi x/R)\mathbf 1_{|x|<R}\), \(R=1\), \(T_0=3\), evaluates the
right-hand side of (R32.2) and compares against direct matrix action.
Agreement is to machine precision on the odd sector.  This is a consistency
sanity-check, not a proof.

---

## 3. Off-support representation of the finite-horizon Schur term

### Corollary R32-C

Let \(f\in L^2(-T_0,T_0)\) with \(\operatorname{ess\,supp}(f)\subset[-R,R]\) and set
\[
g:=B_{T_0}H_{T_0}^*f=-B_{T_0}H_{T_0}f\in L^2(-T_0,T_0).
\]
Then for a.e. \(u\in(-T_0,-R)\cup(R,T_0)\),
\[
\boxed{
(\Sigma_{T_0}f)(u)
=\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\bigl[g(u-\tau_{p,k})-g(u+\tau_{p,k})\bigr].
}
\tag{R32.3}
\]

### Proof

\(\Sigma_{T_0}f=H_{T_0}g\).  Apply R32-B to \(g\); because \(g\) is only in \(L^2\)
and not compactly supported in \([-R,R]\), the one-sided reduction of R32-B does
not apply, so the full \(D_{k\log p}\) expansion survives.  \(\square\)

Status:
\[
\boxed{\text{R32-C (off-support formula for }\Sigma_{T_0})\quad\checkmark[M].}
\]

---

## 4. Precise annular gate for R30-F

Combining R32-C with the R31 forced annular identity (R31.14), the concrete
R30-F question becomes:

For \(j_{R,S}=E_{R,S}\rho_{R,T_0}\) and
\(g_{R,S}:=-B_{T_0}H_{T_0}E_{S,T_0}j_{R,S}\), can the identity
\[
\boxed{
\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\bigl[g_{R,S}(u-\tau_{p,k})-g_{R,S}(u+\tau_{p,k})\bigr]
=\phi_S(u)-(C_{\Gamma,S}j_{R,S})(u)
}
\tag{R32.4}
\]
hold on any nonempty open subinterval of \(\mathcal A_{R,S}\)?

### Observations

1. The right-hand side of (R32.4) is real-analytic on each half-annulus.
   Analyticity of the Gamma tail is exactly R31-B; analyticity of \(\phi_S\)
   away from \(u=0\) follows from the explicit \(\operatorname{sgn}(u)I_0(|u|)\) form.
2. The left-hand side of (R32.4) is a fixed finite linear combination of
   translates of a single \(L^2(-T_0,T_0)\) function \(g_{R,S}\).
3. Matching a fixed finite translate-combination of an \(L^2\) function to a
   real-analytic function on an open set is a genuine constraint — but not
   automatic: if \(g_{R,S}\) itself is real-analytic, the matching can hold.
4. Whether \(g_{R,S}=-B_{T_0}H_{T_0}E_{S,T_0}j_{R,S}\) is real-analytic on any
   open subset of \(\mathcal A_{R,S}\) is not decided by material currently in
   the repository.  \(B_{T_0}\) is a nonlocal inverse of a bounded operator and
   is not analyticity-preserving in general.

### R32-F (Open Problem)

For every fixed \(0<R<S<T_0\), decide whether (R32.4) admits any nonempty open
subinterval solution.

A negative answer proves R30-F.

Two candidate strategies:

- Strategy (A): Prove that \(g_{R,S}\) is \emph{not} real-analytic on any open
  subinterval of \(\mathcal A_{R,S}\).  Combined with the discrete-translation
  structure of the left-hand side and R31-B, this would rule out (R32.4).

- Strategy (B): Reformulate (R32.4) in Fourier space against a fixed test
  function on the annulus and exploit the discrete symbol
  \(\theta(\xi)=2i\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}\sin(\tau_{p,k}\xi)\).
  Its arithmetic structure — the linear independence of \(\{\log p\}\) over
  \(\mathbb Q\) at fixed \(T_0\) — is potentially incompatible with matching a
  logarithmic multiplier plus explicit modified-Bessel forcing.

Neither strategy is currently in the repository.

Status:
\[
\boxed{\text{R32-F}\quad?[O].}
\]

---

## 5. Verdict and remaining status

| Item | Status |
|---|---|
| R32-A antisymmetry \(H_{T_0}^*=-H_{T_0}\) | ✓[M] |
| R32-B exact off-support formula for \(H_{T_0}\) on compact-support inputs | ✓[M] |
| R32-C off-support formula for \(\Sigma_{T_0}\) on compact-support inputs | ✓[M] |
| R32-F analytic-vs-translation-sum compatibility on annulus | ?[O] |
| R30-F: \(R_*(S,T_0)=S\) | ?[O] |
| Polar gauge / terminal transport consequence | not obtained |

### What R32 changes (post-repositioning)

- Exact antisymmetry \(H_{T_0}^*=-H_{T_0}\) is now recorded in P11.
- The off-support action of the outer hub factor is now available as an
  explicit finite \(\{\tau_{p,k}\}\)-shift sum on compactly supported inputs.
- The Schur term acquires an annular rewriting \((R32.3)\) that separates the
  outer hub factors (fully explicit) from the inverse \(B_{T_0}\) (implicit).
- The precise remaining obstruction to R30-F is now displayed as the annular
  identity \((R32.4)\), whose analytic-vs-shift-sum incompatibility is R32-F.

### What R32 explicitly does not deliver

- No kernel representation of \(\Sigma_{T_0}\).
- No range statement on the annular restriction
  \(E_{S,T_0}^*\Sigma_{T_0}E_{S,T_0}\).
- No refutation of the abstract R31-D countermodel: the antisymmetry of the
  outer hub factor, without control of \(B_{T_0}\), does not by itself exclude
  the coarse abstract Schur models allowed by R31-D.
- No proof of R30-F.
- No polar-gauge, terminal-transport, Object-X, or RH consequence.
- No closure of the P02→P11 symbol bridge (R31.8); that remains ?[O]
  independently.

### Adversarial defence

The R31-D countermodel used only positivity, boundedness, parity, small-Sobolev
regularity, and abstract positive Feshbach factorisation of the Schur term.
R32-A and R32-B add the two structural facts

- exact antisymmetry \(H_{T_0}^*=-H_{T_0}\);
- exact discrete-translational structure of \(H_{T_0}\) with translations
  \(\tau_{p,k}=(k\log p)/2\)

about the outer factor \(H_{T_0}\).  The R31-D countermodel does not carry
either property in that outer-factor sense.  However R31-D also does not make
any claim about the outer factor; it operates on the composite \(\Sigma\).
So the correct honest statement is: R32-A/B do not by themselves refute the
abstract shape of R31-D at the composite level.  Closing the gate requires
control of \(B_{T_0}\) as well.

### Next mathematical target

Before attempting a further \(H_{T_0}B_{T_0}H_{T_0}^*\) expansion the natural
next step is the small manuscript-level task:

- Close the P02→P11 symbol bridge (R31.8) explicitly: display
  \(m_\Gamma=c_0+c_1 q_\Gamma\) with concrete \(c_0,c_1\) and matched Fourier
  convention, so that R31-B becomes citable directly for the concrete
  P11 operator \(C_{\Gamma,S}\).

Only after that should the inverse \(B_{T_0}\) be attacked, and even then not
necessarily via a kernel representation but rather via a \emph{fingerprint
property} of the annular range not shared by R31-D.
