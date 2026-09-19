# Scalar-gap restart summability barrier and the block-adaptive escape route

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `ca3849ab2a5abf6268ee892109a293332c1030e9`.
Preserved parallel restart: `829019d7e62f936ab4db903bb9c7758edf427609`.

This package isolates a structural limitation of the two currently proved
restart mechanisms. It does **not** show that the true variational gap becomes
zero, and it does not show that non-summable transport is impossible. It proves
only that the two published sufficient restart laws, when iterated using only
one scalar global-gap budget, can certify at most a summable total new width.

The conclusion is therefore architectural:

> A non-summable transport proof must either improve the width law itself or
> transport additional internal block reserves instead of repeatedly paying
> every new shell from the worst global All-Source gap.

No new Mellin condition, A1, source selection, endpoint positivity claim,
Strong Terminal, C1-GEOM, Object X or RH claim is introduced.

## 1. Exact monotonicity firewall

Let lambda(a) be the optimal two-Mellin Rayleigh infimum on the full source
space at half-width a. Exact physical zero extension gives, for a<=b,

\[
\boxed{\lambda(b)\le\lambda(a).}
\tag{1}
\]

Thus the true optimal physical gap cannot be regenerated upward by enlarging
the window. A later certificate may of course improve a previously crude
lower bound, but any genuine "reserve renewal" must not be interpreted as an
increase of the true variational minimum.

This distinction matters below: the reserves which may be renewed are
directional, tail, profile, Schur, or other internal block reserves.

## 2. The halving-gap restart is necessarily summable

The restart theorem in `ca3849a` says that a certified gap epsilon can be
continued with gap epsilon/2 provided

\[
0<h\le 2^{-\lceil1600/\epsilon\rceil}.
\tag{2}
\]

Iterate only this certified rule. Starting from epsilon_0>0, put

\[
\epsilon_n=2^{-n}\epsilon_0,\qquad
N_n=\left\lceil {1600\over\epsilon_n}\right\rceil,\qquad
h_n\le2^{-N_n}.
\tag{3}
\]

Since

\[
N_n\ge 2^n {1600\over\epsilon_0},
\]

if

\[
t=2^{-\lceil1600/\epsilon_0\rceil},
\]

then \(0<t\le1/2\) and

\[
h_n\le t^{2^n}\le t^{n+1}.
\]

Therefore

\[
\boxed{
\sum_{n\ge0}h_n
\le {t\over1-t}\le2t<\infty.
}
\tag{4}
\]

Hence the published halving-gap scalar restart, by itself, cannot certify a
non-summable or macroscopic endpoint advance.

For the currently largest proved All-Parity endpoint
\(B+5\cdot10^{-19}\), the published gap is \(3\cdot10^{-16}\), so the
first restart exponent is already at least

\[
\left\lceil{1600\over3\cdot10^{-16}}\right\rceil
=5\,333\,333\,333\,333\,333\,334.
\]

This number is only a scale diagnostic; the summability statement (4) is the
theorem.

## 3. Positive-gap-floor schedules under the 829019d law are also summable

The restart theorem used in `829019d` permits a target
\(0<\gamma<\epsilon\). Write

\[
m=\epsilon-\gamma>0.
\]

One of its sufficient width conditions is

\[
h\le
2\exp\!\left[-{17+32/m+3\gamma\over2}\right]
\le 2e^{-16/m}.
\tag{5}
\]

Consider **any** scalar-gap schedule based only on that sufficient law,

\[
\epsilon_{n+1}=\epsilon_n-m_n,\qquad m_n>0,
\tag{6}
\]

which retains a positive limiting gap

\[
\epsilon_n\downarrow\epsilon_*>0.
\]

Then

\[
\sum_{n\ge0}m_n=\epsilon_0-\epsilon_*<\infty.
\tag{7}
\]

For all sufficiently large n, \(0<m_n\le1\). The elementary Taylor bound

\[
e^{16/m}\ge{(16/m)^2\over2}={128\over m^2}
\]

gives

\[
2e^{-16/m}\le {m^2\over64}<m^2.
\tag{8}
\]

Combining (5)-(8),

\[
\sum h_n
\le \sum_{\text{finite initial}}h_n+\sum_{\text{tail}}m_n^2<\infty,
\tag{9}
\]

because a summable positive sequence is bounded and hence its squares are
summable.

Therefore:

\[
\boxed{
\text{Every positive-gap-floor iteration that uses only the published }
829019d\text{ scalar width law has summable guaranteed widths.}
}
\tag{10}
\]

This is stronger than checking one particular schedule.

## 4. Combined scalar-gap barrier

Equations (4) and (10) isolate the common obstruction.

* Fixed fractional gap loss plus the `ca3849a` width law gives a
  super-geometrically shrinking, summable endpoint advance.
* Retaining a positive gap floor with the `829019d` target-gap law forces
  summable gap losses \(m_n\), while its exponential \(e^{-16/m_n}\)
  dependence again makes the guaranteed widths summable.

Thus neither currently proved **scalar-global-gap** restart law can by itself
produce

\[
\sum_n h_n=\infty
\]

or a positive uniform step lower bound.

This does **not** establish a no-go for the actual Weil form. It is a no-go
for these two sufficient scalar certificate mechanisms.

## 5. What must change

There are only two logical escape routes from the barrier:

1. **Milder width dependence.** Replace the exponential-in-inverse-reserve
   law by a quantitatively milder law, e.g. an algebraic dependence on the
   relevant reserve.
2. **Non-scalar reserve transport.** Do not charge the entire new shell to the
   worst All-Source gap. Split the core into soft and hard pieces and transport
   their reserves separately.

The second route is now the preferred local front. The existing certificates
already exhibit the required scale separation:

* the global All-Parity gap is tiny;
* the complete even and odd infinite tails have order-one endpoint floors;
* the fixed low spaces are finite dimensional;
* complete core/profile couplings and mixed-block Grams are already available.

A block-adaptive theorem should therefore keep a finite soft Schur block
explicit while using the much larger tail/profile reserve for the hard
directions. The scalar gap should appear only in the genuinely soft block,
not in the full-core shell pivot.

## 6. Scope firewall

Closed here:

* exact summability barrier for the `ca3849a` halving-gap restart;
* exact summability barrier for every positive-gap-floor schedule using the
  published `829019d` target-gap width law;
* clarification that true gap renewal upward is forbidden by exact
  variational monotonicity;
* identification of block-adaptive reserve transport or a milder width law
  as the required escape from these two scalar mechanisms.

Still open:

* a block-adaptive reserve-renewal theorem;
* a non-summable or uniform-step transport;
* actual transport to the channel-7 threshold;
* Connected Unit-Window Coercivity;
* historical Strong Terminal;
* full C1-GEOM, Object X, global Weil positivity and RH.
