# P11 R43 — B-FLAGDYN current front

Date: 2026-09-04

This is a navigation/status file only. It creates no mathematical promotion.

## Provenance

- Base: `main@2102b538c220cd809ad876c425df4f30304eb997`
- Active branch: `research/r43-gcac-hardening`
- Current companion mathematical hardening head: `ca370c6b95c0a454da82376bc82b9e2261113e0d`
- Canonical R43 core blob: `983b42949d6a4a1806c0b333727cb49000b99972`
- O1 modulus-phase companion: `audits/P11_R43_FLAGDYN_O1_MODULUS_PHASE_REDUCTION_2026-09-04.md`
- Terminal metric increment definitions audit: `audits/P11_R43_TERMINAL_METRIC_INCREMENT_DEFINITION_AUDIT_2026-09-04.md`

## Governance

- R43: OPEN
- no freeze
- no new formal independent GREEN
- no new `✓[M]`
- R38–R42 unchanged/frozen
- R37/G4c separate and open
- no Strong-Terminal/C6, Object-X, or RH promotion

## Current chain

```text
GC-AC candidate-closed
        |
        v
B-FLAGMOD + B-FLAGPHASE
        |
        | sufficient two-defect criterion
        v
B-FLAGTIGHT
        |
        v
B-SIGN
        |
        v
Strong Terminal ?
```

The middle implication is sufficient only, not an equivalence.

Inside `B-FLAGMOD`, the current quantitative sub-node is `B-METINC`:

```text
B-METINC
   |
   | pairwise Sylvester bridge + projected modulus estimate
   v
B-FLAGMOD
```

Loewner positivity and a positive new-shell theorem are optional accelerators for
`B-METINC`, not prerequisites in the logical definition of the route.

## Exact B-FLAGTIGHT gate

For

```text
Q_{m,U} = W_U^* P_m W_U,
q_m(U) = <epsilon_R,Q_{m,U}epsilon_R> = ||P_m h_U||^2,
```

one has

```text
B-FLAGTIGHT  <=>  lim_m limsup_U q_m(U) = 0.
```

Jet-number/flag energy remains only a stronger sufficient tool.

## Cocycle firewall

The moving-range partial isometry

```text
T_{U->V}=W_V W_U^*
```

is exact bookkeeping but not a pure local terminal increment because

```text
T_{U->U}=P_{Ran W_U}.
```

Its off-flag block therefore contains a static range/flag principal-angle defect.

## Exact O1 modulus lock

For one terminal step `U<V`, let

```text
A_X = (C_X^{U->V})^* C_X^{U->V},
C_X^{U->V} = U_X A_X^(1/2),
L = (I-W_UW_U^*) A_S^(1/2) W_U,
J = A_R^(1/2) - W_U^* A_S^(1/2) W_U.
```

With

```text
B = W_U^* A_S^(1/2) W_U,
```

the exact identity is

```text
A_R = B^2 + L^*L,
B = (A_R-L^*L)^(1/2),
J = A_R^(1/2) - (A_R-L^*L)^(1/2).
```

Thus `J` is not an independent modulus obstruction. In particular

```text
L=0  <=>  J=0.
```

## Exact projected two-defect increment

Frozen O1 gives

```text
W_V-W_U
 = U_S (L-W_U J) A_R^(-1/2) U_R^* + P_phase.
```

Therefore

```text
|sqrt(q_m(V))-sqrt(q_m(U))|
 <= d_mod(m;U,V)+d_phase(m;U,V),
```

where

```text
d_mod
 = ||P_m U_S (L-W_UJ) A_R^(-1/2) U_R^* epsilon_R||,

d_phase
 = ||P_m P_phase epsilon_R||.
```

Both defects vanish identically for `V=U`.

A terminal partition for which the sums of the corresponding interval suprema tend to zero as `m->infinity` is sufficient for B-FLAGTIGHT.

## Terminal metric increment definitions audit

For fixed source `X` and horizons `X<U<V`, frozen R4 puts both future metrics on the same
fixed graph Hilbert space:

```text
G_{X,T}=J_{X,T}^*J_{X,T}.
```

The Gamma contribution is exactly invariant under zero extension. Therefore

```text
<f,(G_{X,V}-G_{X,U})f>
 = <Sigma_V E_{X,V}f,E_{X,V}f>
   - <Sigma_U E_{X,U}f,E_{X,U}f>.
```

All terminal variation sits in the Schur geometry

```text
Sigma_T = H_T B_T H_T^*,
B_T = (I+R_T^*R_T)^(-1).
```

The frozen hub has fixed primitive prime-power coefficients, but both the finite-window
operators `P_T D_s E_T` and the global Feshbach conditioning `B_T` are horizon dependent.
Thus a naive new-shell-only positive Gram difference is **not** supplied by the frozen
definitions.

Loewner monotonicity

```text
G_{X,V}-G_{X,U} >= 0  ?
```

is a separate weaker gate and remains OPEN.

## B-METINC: unconditional modulus input

Define the normalized true metric increment

```text
Hbold_X^{U,V}
 = G_{X,U}^(-1/2) (G_{X,V}-G_{X,U}) G_{X,U}^(-1/2)
 = A_X^{U,V}-I.
```

For

```text
P_U=W_UW_U^*,
E_{U,V}=(I-P_U) Hbold_S^{U,V} W_U,
```

one has unconditionally

```text
||E_{U,V}|| <= ||Hbold_S^{U,V}||.
```

Thus direct cofinal/partition control of normalized relative metric increments can feed
B-FLAGMOD without first proving positivity.

The live metric sub-gate is

```text
B-METINC:
control ||Hbold_X^{U,V}|| cofinally in a form compatible with B-FLAGDYN summability.
```

### Conditional Loewner accelerator

If, additionally,

```text
G_{R,V}-G_{R,U} >= 0,
G_{S,V}-G_{S,U} >= 0,
```

then

```text
0 <= E^*E
   <= ||Hbold_S|| Hbold_R - Hbold_R^2
   <= ||Hbold_S|| Hbold_R,
```

hence

```text
||E||^2 <= ||Hbold_S|| ||Hbold_R||,
||E|| <= (1/2)||Hbold_S||.
```

This is a conditional accelerator only. Positivity by itself still supplies no cofinal
smallness or summability.

## Sylvester conditioning firewall

The square-root mismatch satisfies the exact pairwise Sylvester equation. For each fixed
`U<V`, its norm is controlled by `||E_{U,V}||` with denominator

```text
alpha_S(U,V)+alpha_R(U,V),
alpha_X(U,V)=inf sigma((A_X^{U,V})^(1/2)) > 0.
```

No cofinal uniform lower bound for these pairwise relative spectral gaps is currently
booked. The fixed-source lower bound for absolute future metrics does not by itself give
such a uniform relative bound.

## Current open mathematical targets

### B-FLAGMOD / B-METINC

First try to control the normalized true future-metric increments directly. Separately,
Loewner monotonicity may be proved to sharpen the variance estimate; only after that is a
positive atom/new-shell decomposition worth pursuing as a quantitative arithmetic tool.

### B-FLAGPHASE

Control the deep C6a-tail of the two-horizon polar-phase mismatch on the single fixed source normal.

R42 tangential polar convergence does not automatically close this normal two-horizon phase channel.

## Post-tightness gate

Under B-TIGHT,

```text
Strong Terminal  <=>  liminf_{T,U->infinity} L_{R,S}^{T,U} > -1.
```

Local sign-increment criteria additionally require one cofinal chain component.
