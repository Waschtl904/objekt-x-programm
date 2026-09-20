# Local source directed system and the Objekt-X interface lemma

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `a0ea6f80f317e4ef1132fc02c86be5bd2064e738`.

This package implements the requested strategic firewall between the local
Shell-Schur transport programme and Objekt X. It proves that a canonical
directed system already exists at the level of physical two-Mellin source
spaces and their closed Hermitian forms. It then states exactly the additional
positive-readout compatibility which would turn such local data into a genuine
Objekt-X candidate.

The result does **not** construct Objekt X. In particular, the positive Hilbert
structure used below for the directed carrier is the shifted graph inner product
`q+17 I`, not the desired Weil Gram form. No positivity of the full Weil form,
no RH, no C1-GEOM and no global Prime/Gamma mediator is assumed or concluded.

## 1. Canonical physical source spaces

Fix the presently relevant band

\[
B={\log5\over2}\le a<1.
\]

Work in physical coordinates on the full real line. Define

\[
\mathcal K_a
=
\left\{
u\in L^2(\mathbb R):
\operatorname{supp}u\subset[-a,a],
\ E_+u=E_-u=0
\right\},
\]

where

\[
E_\pm u=\int_{\mathbb R}u(x)e^{\pm x/2}\,dx.
\]

Let

\[
\mathcal W_a
=
H^1_0((-a,a))\cap\ker E_+\cap\ker E_-,
\]

understood after physical zero extension to the full line. Let \(q_a\) denote
the connected two-Mellin nonpole form on this source class.

For \(a\le b<1\), define

\[
J_{a,b}u=u
\]

as the same full-line function, now regarded as supported inside \([-b,b]\).
In reference coordinates this is the already proved formula

\[
(J_{a,b}f)(\xi)
=
\sqrt{b/a}\,
f((b/a)\xi)\,
1_{\{|\xi|<a/b\}}.
\tag{1}
\]

The physical formulation is primary: \(J_{a,b}\) is simply zero extension.

## 2. Exact directed-system theorem on actual sources

The inherited exact window identity gives

\[
\|J_{a,b}u\|_2=\|u\|_2,
\qquad
q_b[J_{a,b}u]=q_a[u]
\tag{2}
\]

for every actual source \(u\in\mathcal W_a\). Polarization of the Hermitian
quadratic forms therefore gives the full sesquilinear identity

\[
\boxed{
q_b(J_{a,b}u,J_{a,b}v)=q_a(u,v)
}
\qquad(u,v\in\mathcal W_a).
\tag{3}
\]

Physical moments are literally unchanged by zero extension, hence
\(J_{a,b}\mathcal W_a\subset\mathcal W_b\). Reflection commutes with
\(J_{a,b}\), so the even and odd invariant subspaces form directed subsystems.

Most importantly, physical zero extension is strictly compositional:

\[
\boxed{
J_{a,a}=I,
\qquad
J_{b,c}J_{a,b}=J_{a,c}
}
\qquad(B\le a\le b\le c<1).
\tag{4}
\]

In reference coordinates (4) follows directly from the scale factors
\(\sqrt{b/a}\sqrt{c/b}=\sqrt{c/a}\) and the nested support cutoffs.

Thus the composition law between local **source spaces** is already proved.
What remains open for Objekt X is not this source-level law, but a compatible
positive mediator/readout law above it.

## 3. Closed form spaces form an isometric directed Hilbert system

The restart package proves on \(B\le a<1\) the uniform semibound

\[
q_a[u]\ge-16\|u\|_2^2.
\tag{5}
\]

Hence

\[
\langle u,v\rangle_{a,17}
:=
q_a(u,v)+17\langle u,v\rangle_{L^2}
\tag{6}
\]

is a positive inner product on \(\mathcal W_a\), with

\[
\|u\|_{a,17}^2\ge\|u\|_2^2.
\]

Let

\[
\mathcal F_a
=
\overline{\mathcal W_a}^{\|\cdot\|_{a,17}}.
\tag{7}
\]

Equations (2)--(3) show exactly

\[
\|J_{a,b}u\|_{b,17}=\|u\|_{a,17}.
\tag{8}
\]

Therefore \(J_{a,b}\) extends uniquely to an isometric embedding

\[
\boxed{
J_{a,b}:\mathcal F_a\hookrightarrow\mathcal F_b.
}
\tag{9}
\]

The composition law (4) extends by density. Consequently

\[
\boxed{
(\mathcal F_a,J_{a,b})_{B\le a<b<1}
}
\tag{10}
\]

is a genuine directed system of Hilbert spaces.

Its Hilbert direct limit exists canonically:

\[
\mathcal F_{\rm dir}^{(17)}
:=
\varinjlim_{B\le a<1}(\mathcal F_a,J_{a,b}).
\tag{11}
\]

The compatible \(L^2\) pairing and the compatible forms define on the
algebraic direct limit a Hermitian form

\[
q_{\rm dir}([u,a],[v,b])
:=
q_c(J_{a,c}u,J_{b,c}v)
\tag{12}
\]

for any \(c\ge a,b\). Equation (3) makes (12) independent of the chosen
common endpoint.

This is a real local-to-global **carrier interface**. It is not Objekt X:
its Hilbert positivity comes from the artificial shift \(+17I\), while
\(q_{\rm dir}\) itself is not known positive on the whole directed band.

## 4. Prime and archimedean channel naturality

The Prime and Gamma data are most canonical in physical full-line
coordinates.

For each prime power \(q=p^k\), put

\[
w_q={\Lambda(q)\over\sqrt q}
\]

and define the physical Prime pairing

\[
\mathcal P_q(u,v)
=
w_q\,
\langle u,
(\tau_{\log q}+\tau_{-\log q})v\rangle.
\tag{13}
\]

Define the archimedean jump pairing

\[
\mathcal G(u,v)
=
\int_0^\infty
k(r)\,
\langle\tau_ru-u,\tau_rv-v\rangle\,dr.
\tag{14}
\]

These are full-line observables, so zero extension does not change them:

\[
\boxed{
\mathcal P_q(J_{a,b}u,J_{a,b}v)=\mathcal P_q(u,v),
\qquad
\mathcal G(J_{a,b}u,J_{a,b}v)=\mathcal G(u,v).
}
\tag{15}
\]

If a channel becomes active only after enlarging the ambient window, then
\(\log q\ge2a\) and its correlation on an old source is zero by support
separation. Thus the active-set enlargement is automatically compatible
with the directed source system.

This is an important X-interface fact: the Prime and archimedean
**observables** already form natural data over the same source-directed
system. What is not proved is that they arise as projections or components
of one common **positive** mediator geometry.

## 5. Shell quotient and gauges are coordinate charts, not the directed maps

The Shell-Schur programme supplies, on certified local edges, complete
core/profile charts

\[
\Psi_{a,b}^{p}:
\mathcal F_a^{p}\oplus\mathcal P_{a,b}^{p}
\xrightarrow{\sim}
\mathcal F_b^{p},
\tag{16}
\]

with exact moment correction and the actual \(H^1\) gluing conditions.
The trace duplication was removed by quotient/gauge analysis; in the final
full-core/profile coordinates there is no second independent physical trace.

Therefore the raw trace coordinate, the quotient coordinate and the A-gauge
must be interpreted as **charts on the same physical source space**, not as
new physical degrees of freedom and not as candidates for \(J_{a,b}\).

Whenever two certified charts \(\Psi_\alpha,\Psi_\beta\) describe the same
\(\mathcal F_b^p\), their overlap map is canonically

\[
R_{\alpha\beta}
=
\Psi_\beta^{-1}\Psi_\alpha.
\tag{17}
\]

Where three charts coexist,

\[
R_{\beta\gamma}R_{\alpha\beta}=R_{\alpha\gamma}.
\tag{18}
\]

This cocycle identity is formal from the physical target space. The open
problem is not chart composition itself; it is endpoint-uniform control and
compatibility of a future positive readout under these chart changes.

## 6. The exact C0/C1 Objekt-X interface

The preceding results motivate a precise two-layer interface.

### C0 — canonical signed source/form system: CLOSED on the current band

C0 consists of

\[
\mathfrak C_0
=
\left(
\mathcal F_a,\,
J_{a,b},\,
q_a,\,
\{\mathcal P_q\}_q,\,
\mathcal G,\,
\text{parity}
\right)_{B\le a<b<1}.
\tag{19}
\]

On the current band:

* \(J_{a,b}\) is canonical and compositional;
* \(q_a\) is exactly natural under \(J_{a,b}\);
* parity is natural;
* Prime channel observations are natural;
* the archimedean jump observation is natural;
* the graph-shifted Hilbert direct limit exists.

This is **not** yet a positive Weil-Gram geometry.

### C1 — compatible intrinsic positive readout: OPEN

A C1 realization would require Hilbert spaces \(\mathcal H_a\), maps

\[
T_a:\mathcal F_a\to\mathcal H_a
\]

and isometric embeddings

\[
I_{a,b}:\mathcal H_a\to\mathcal H_b
\]

such that

\[
I_{b,c}I_{a,b}=I_{a,c},
\tag{20}
\]

\[
\boxed{
T_bJ_{a,b}=I_{a,b}T_a,
}
\tag{21}
\]

and, on the correct local Weil class,

\[
\boxed{
q_a(u,v)=\langle T_au,T_av\rangle_{\mathcal H_a}.
}
\tag{22}
\]

Crucially, the data \((\mathcal H_a,T_a,I_{a,b})\) must be constructed
intrinsically from the Prime/archimedean mechanism and must not be obtained
by first assuming positivity of \(q_a\) and then taking its abstract
GNS/quotient completion.

## 7. Conditional direct-limit Gram theorem

Assume a cofinal family of endpoints carries C1 data satisfying
(20)--(22). Then the Hilbert direct limit

\[
\mathcal K_X^{\rm cand}
=
\varinjlim_a(\mathcal H_a,I_{a,b})
\tag{23}
\]

exists. Define

\[
T_X[u,a]=[T_au,a].
\tag{24}
\]

Equation (21) makes \(T_X\) well-defined, and (22) gives

\[
\boxed{
q_{\rm dir}(F,G)
=
\langle T_XF,T_XG\rangle_{\mathcal K_X^{\rm cand}}.
}
\tag{25}
\]

Thus the missing mathematical step to a genuine X-candidate is now sharply
located: construct the **C1 compatible positive readout** without assuming
the desired positivity.

Even (25) would still need a cofinal source/test-class theorem identifying
the directed source class with the exact Weil test class required by the
Weil criterion. Hence C1 compatibility is necessary for this route but is
not by itself RH.

## 8. Relation to historical Suzuki/NEU-259 transition maps

The maps proved here are the zero-extension maps on the current
Shell-Schur source/form spaces \(\mathcal F_a\). They do **not** prove the
historical open maps

\[
J_{a,b}^{\mathcal H}:
\mathcal H(T_{a,\lambda(a)})
\to
\mathcal H(T_{b,\lambda(b)})
\]

from the Suzuki/NEU-259 architecture, and they do not prove intertwining of
Suzuki's self-adjoint operators.

Therefore the new C0 directed system does not silently promote the historical
Suzuki direct-limit candidate. It is a different, presently better-grounded
local source/form interface.

## 9. Current transport interface

The transport strand now supplies two strategic C0 inputs:

1. at fixed core \(B\), block-adaptive profile transport reaches
   \(B+5\cdot10^{-13}\);
2. on every moving endpoint \(B\le a\le1\), the complete reconstructed
   high tail can be renewed with physical floor \(>1/41\).

The remaining scalable transport gate is finite-dimensional:

\[
\boxed{
\text{MOVING 191D LOW-BLOCK + PROFILE RESERVE RENEWAL}.
}
\tag{26}
\]

A new width-only commit which does not improve the scaling law or close one
of the interfaces below should not be treated as the strategic front.

## 10. Strategic stop rule

A future mathematical commit counts as a strategic Objekt-X/transport advance
only if it closes at least one of:

1. a non-summable or uniform-step transport law;
2. a moving internal reserve with a non-collapsing scaling law;
3. a canonical source/readout transition map;
4. a composition/intertwining law not already implied by physical zero
   extension;
5. an intrinsic common Prime/Gamma mediator;
6. the moving 191-dimensional Low/Profile interface;
7. an explicitly named C1 or Objekt-X interface;
8. the exact global Weil test-class / Gram identification.

Pure constant improvement or another microscopic width enlargement remains
valid local research, but it is not the next strategic step unless it reveals
one of these scalable mechanisms.

## 11. Scope firewall

Closed here:

* canonical source-level directed system on \(B\le a<1\);
* exact composition of physical zero-extension maps;
* exact form compatibility and graph-Hilbert isometries;
* a canonical shifted Hilbert direct-limit carrier;
* naturality of Prime and archimedean observables;
* identification of Shell-Schur quotient/gauges as coordinate charts;
* the conditional C1-to-direct-limit Gram theorem.

Still open:

* any intrinsic positive C1 readout satisfying (20)--(22);
* a common Prime/Gamma mediator geometry;
* moving 191D Low/Profile reserve renewal;
* non-summable transport;
* actual all-source arrival at \(\log7/2\) or \(1\);
* Connected Unit-Window Coercivity and full C1-GEOM;
* a complete X-candidate, exact global Weil-Gram identity and RH.
