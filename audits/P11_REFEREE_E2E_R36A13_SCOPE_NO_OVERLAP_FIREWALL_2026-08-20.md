# P11 End-to-End Referee R36-A13 — Scope / no-overlap citation firewall

Date: 2026-08-20

This note is a scope addendum to
`P11_REFEREE_E2E_R36A13_ONE_SHIFT_ODD_KERNEL_ORACLE_2026-08-20.md`.
It changes no theorem proved there; it fixes the citation scope so that the phrase
"one-shift" is not misread as the mathematical reason for the kernel classification.

## 1. Convention

Throughout P11 and R36,

\[
\boxed{\tau_{p,k}=\frac{k\log p}{2}}.
\]

In the first P11 terminal chamber the unique active shift is

\[
\tau=\tau_{2,1}=\frac{\log 2}{2},
\qquad
\frac{\log 2}{2}\le T_0<\frac{\log 3}{2}.
\]

Since \(\frac{\log 3}{2}<\log 2=2\tau\), one has \(T_0<2\tau\).

## 2. Exact scope of the middle-case theorem

R36-A13.1 is proved under the explicit hypotheses

\[
\boxed{0<R<\tau<S<T_0<2\tau.}
\]

The theorem is therefore a **one-shift no-overlap theorem**, not a theorem saying that
"one active shift" by itself always forces an infinite-dimensional kernel.

Indeed,

\[
S<T_0<2\tau
\quad\Longrightarrow\quad
S-R<2\tau.
\]

For a single shift, the plain-plus image is

\[
(R+\tau,S+\tau),
\]

whereas the relevant folded-minus image reaches only to \(S-\tau\). These image regions
can overlap only if

\[
R+\tau<S-\tau
\quad\Longleftrightarrow\quad
\boxed{S-R>2\tau.}
\]

Thus the first terminal chamber is automatically in the no-overlap regime.

## 3. Citation firewall outside the no-overlap regime

If \(S-R>2\tau\), the two image regions overlap. On the overlap the one-shift equation
contains the relation

\[
\boxed{h(x+2\tau)=h(x)}
\]

where both arguments lie in \((R,S)\). This additional translation recursion is absent from
the proof of R36-A13.1 and can change the kernel structure.

Therefore the following statement is **not proved** and must not be cited from A13:

> one active shift implies an infinite-dimensional odd kernel.

The proved statement is instead:

> under \(0<R<\tau<S<T_0<2\tau\), equivalently in the first P11 one-shift chamber with the
> shift strictly inside \((R,S)\), the odd kernel is exactly the antisymmetric central family
> described in R36-A13.1 and is infinite-dimensional.

## 4. First-chamber iff statement, also in words

Throughout

\[
\frac{\log2}{2}\le T_0<\frac{\log3}{2},
\qquad 0<R<S<T_0,
\]

R36-A13 proves

\[
\boxed{
\ker L_{R,S,T_0}\ne\{0\}
\quad\Longleftrightarrow\quad
R<\frac{\log2}{2}<S.
}
\]

**In words:** in the first P11 terminal chamber, the odd localized kernel is nontrivial
exactly when the unique active shift \(\tau_{2,1}=\log2/2\) lies strictly inside the positive
half-annulus \((R,S)\). If the shift lies at or outside either endpoint, the odd kernel is
trivial.

This statement concerns only the odd localized kernel via R36-A9. It says nothing about the
even localized kernel or full R36-A kernel triviality.

## 5. Status firewall

This addendum changes no program-level status:

- R36-A13.1 / A13.2 / A13.3: \(\checkmark[M]\) in their stated hypotheses.
- First-terminal-chamber odd-kernel iff classification: \(\checkmark[M]\).
- Wider one-shift regimes with \(S-R>2\tau\): not classified here.
- Full R36-A kernel triviality: \(?[O]\).
- R36-B pairing/nonorthogonality: not decided by A13 alone.
- R30-F: \(?[O]\).
- No Object-X, polar-gauge, terminal-transport, or RH conclusion is made.
