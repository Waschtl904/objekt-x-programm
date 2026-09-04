# P11 R43 — B-FLAGDYN current front

Date: 2026-09-04

This is a navigation/status file only. It creates no mathematical promotion.

## Provenance

- Base: `main@2102b538c220cd809ad876c425df4f30304eb997`
- Active branch: `research/r43-gcac-hardening`
- Canonical R43 core blob: `983b42949d6a4a1806c0b333727cb49000b99972`
- O1 modulus-phase companion: `audits/P11_R43_FLAGDYN_O1_MODULUS_PHASE_REDUCTION_2026-09-04.md`
- Terminal metric increment definitions audit: `audits/P11_R43_TERMINAL_METRIC_INCREMENT_DEFINITION_AUDIT_2026-09-04.md`
- Spectral-width refinement: `audits/P11_R43_B_METINC_SPECTRAL_WIDTH_REFINEMENT_2026-09-04.md`

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

Inside `B-FLAGMOD`, the primary quantitative sub-node is now the spectral-width route:

```text
B-METINC-WIDTH
   |
   | pairwise Sylvester bridge + projected modulus estimate
   v
B-FLAGMOD contribution to FD23
```

with separately auditable channels

```text
B-METINC-NEW
B-METINC-GEO
B-METINC-COND
```

Loewner positivity and a positive new-shell theorem are optional structural/arithmetic
results, not prerequisites for the logical B-METINC route.

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

is a separate structural gate and remains OPEN.

## B-METINC: exact off-diagonal identity

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

self-adjointness gives the exact identities

```text
||E_{U,V}||
 = ||(I-P_U) Hbold_S^{U,V} P_U||
 = ||[Hbold_S^{U,V},P_U]||.
```

## Positivity-free spectral-width refinement

Let

```text
lambda_- = inf spec(Hbold_S^{U,V}),
lambda_+ = sup spec(Hbold_S^{U,V}),
width(Hbold_S)=lambda_+-lambda_-.
```

Subtracting the spectral midpoint does not change the off-diagonal block. Hence

```text
||E_{U,V}|| <= (1/2) width(Hbold_S^{U,V}).
```

This is completely positivity-free. In particular, a two-sided bound

```text
-delta I <= Hbold_S^{U,V} <= epsilon I
```

implies

```text
||E_{U,V}|| <= (epsilon+delta)/2.
```

Loewner positivity is now only a special case: if `Hbold_S>=0`, then

```text
width(Hbold_S) <= ||Hbold_S||,
```

so the previous conditional half-norm estimate follows automatically.

`R43-MI-LOEWNER` therefore remains OPEN but is no longer needed even for the factor-`1/2`
leakage mechanism.

## Exact three-channel metric split

The Schur-energy difference can be telescoped exactly through three intermediate stages:

```text
old-conditioning  : change B_U -> B_V on embedded old data,
old-geometry      : change already-active P_T D_s E_T geometry at fixed B_V,
new-shell         : activate Lambda_V \ Lambda_U at fixed terminal-V geometry/B_V.
```

After Riesz representation and normalization,

```text
Hbold_X
 = Hbold_X,cond + Hbold_X,geo + Hbold_X,new.
```

No individual sign is supplied by the frozen definitions; even the new-shell energy
contains cross terms with already present terminal-V old geometry.

Spectral-width subadditivity yields the sufficient estimate

```text
||E||
 <= (1/2) width(Hbold_S,new)
    + ||Hbold_S,geo||
    + ||Hbold_S,cond||.
```

Thus the active B-METINC subtargets are:

```text
B-METINC-NEW   : new-shell spectral width,
B-METINC-GEO   : old-channel geometry drift,
B-METINC-COND  : Feshbach-conditioning drift.
```

## Full Sylvester conditioning factor

Let

```text
alpha_X(U,V)=inf spec((A_X^{U,V})^(1/2)) > 0.
```

The square-root mismatch satisfies

```text
||M|| <= ||E||/(alpha_S+alpha_R).
```

The actual projected modulus channel also contains `A_R^(-1/2)`, so the full
pairwise operator-norm chain is

```text
d_mod(m;U,V)
 <= ||E||/[alpha_R(alpha_S+alpha_R)]
 <= width(Hbold_S)/[2 alpha_R(alpha_S+alpha_R)].
```

The norm-only fallback is

```text
d_mod(m;U,V)
 <= ||Hbold_S||/[alpha_R(alpha_S+alpha_R)].
```

Both coercivity factors remain pairwise. No cofinal uniform positive lower bound is
currently booked.

## Summability firewall

Mere step smallness

```text
||Hbold_S^{U_k,U_{k+1}}|| -> 0
```

is not enough. A useful partition majorant is

```text
b_k
 = sup_{V in [U_k,U_{k+1}]}
   width(Hbold_S^{U_k,V})
   /[2 alpha_R(U_k,V)(alpha_S(U_k,V)+alpha_R(U_k,V))].
```

The total-variation requirement is

```text
sum_k b_k < infinity.
```

But this majorant alone does **not** imply the FD23 dominated-convergence limit. One also
needs, for each fixed interval `k`,

```text
Delta_{m,k}^{mod} -> 0  as m -> infinity.
```

Strong convergence `P_m->0` is pointwise on fixed vectors and does not automatically make
the supremum over `V in [U_k,U_{k+1}]` uniform. A sufficient extra mechanism would be
relative compactness of the corresponding modulus-vector family, for example from a
separately proved norm-continuity theorem in `V` on each compact interval.

No such continuity theorem is silently booked.

## Current open mathematical targets

### B-FLAGMOD / B-METINC-WIDTH

Seek a terminal partition with:

1. summable width/conditioning majorants;
2. fixed-interval projected-tail convergence;
3. quantitative control of the NEW/GEO/COND channels above.

This is a sufficient operator-norm route only. Failure of spectral-width control would not
disprove B-FLAGMOD; it would force a return to the genuinely projected normal/flag
quantity, which may be much smaller than the global operator norm.

### B-FLAGPHASE

Control the deep C6a-tail of the two-horizon polar-phase mismatch on the single fixed source normal.

R42 tangential polar convergence does not automatically close this normal two-horizon phase channel.

## Post-tightness gate

Under B-TIGHT,

```text
Strong Terminal  <=>  liminf_{T,U->infinity} L_{R,S}^{T,U} > -1.
```

Local sign-increment criteria additionally require one cofinal chain component.

## Open status

- `R43-MI-LOEWNER`: OPEN, optional structural theorem.
- `B-METINC-WIDTH`: OPEN.
- `B-METINC-NEW`: OPEN.
- `B-METINC-GEO`: OPEN.
- `B-METINC-COND`: OPEN.
- B-METINC: OPEN.
- B-FLAGMOD: OPEN.
- B-FLAGPHASE: OPEN.
- B-FLAGTIGHT: OPEN.
- B-SIGN: OPEN.
- Strong Terminal/C6: OPEN.
