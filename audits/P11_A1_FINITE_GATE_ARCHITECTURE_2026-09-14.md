# P11 A1-FINITE-GATE — final finite certificate architecture

**Date:** 2026-09-14  
**Status:** proof-architecture audit; no finite positivity theorem is claimed.  
**Parent main:** `a4a9a03859c0be0b38fdc42d137524a4c4388d95` / PR #120.  
**Registry:** unchanged.  
**Object-X working definition:** unchanged.

---

## 1. Purpose

PR #120 reduces the canonical `a=1` PSWF/Schur obligation to

```math
(L_1)_{RR}\succeq 3\times10^{-39}I
```

on at most

```text
1104 = 552 even + 552 odd
```

dimensions.  This is the smallest certified reduction currently available.

However, a direct computer proof on that PSWF space would still require a rigorous construction/enclosure of the PSWF resolved subspace and of the two moment-augmented parity bases.

PRs #117--#118 provide an alternative orthonormal Legendre backend.  It is larger (`1075 x 1075` per parity) but already has:

- exact Gram matrix `I`;
- exact parity separation;
- explicit Fourier transforms by spherical Bessel functions;
- a certified full-space tail/cross transfer at `M=2150`;
- a predeclared finite target `1e-35`;
- a certified analytic quadrature operator error `<4e-38` per parity block.

This audit makes the **operational decision for the next computation**:

> Keep PSWF/Osipov `<=1104` as the canonical mathematical reduction, but use the Legendre backend as the primary execution route for the first full finite certificate.

This is a certification-engineering choice, not a theorem promotion and not a claim that the Legendre route is mathematically smaller.

---

## 2. Fixed exact finite blocks

Use the orthonormal Legendre basis on `[-1,1]`

```math
T_n(x)=\sqrt{n+\frac12}\,P_n(x),
\qquad n=0,\ldots,2149.
```

Set

```text
even degrees: 0,2,...,2148  -> 1075 vectors
odd degrees:  1,3,...,2149  -> 1075 vectors.
```

The metric is exactly

```math
G_e=G_o=I.
```

For the bounded lower operator

```math
L_1=0.1I+K+\mathcal E^*\mathcal E,
```

with

```math
r(\xi)=(m_1(\xi)-0.1)\mathbf1_{[-1551,1551]}(\xi),
```

the same-parity matrix entries are

```math
(A_p)_{nm}
=0.1\delta_{nm}+K_{nm}+2a_na_m,
```

where

```math
a_n=\langle T_n,e^{x/2}\rangle
=2\sqrt{n+\frac12}\,i_n(1/2),
```

and

```math
K_{nm}
=\frac{4\sqrt{\nu_n\nu_m}}{\pi}
(-1)^{(m-n)/2}
\int_0^{1551}r(\xi)j_n(\xi)j_m(\xi)\,d\xi,
\qquad \nu_n=n+\frac12.
```

The completion term is the positive rank-one block `2aa^T` in **both** parity sectors.  Opposite parities decouple exactly.

The final finite claims to certify are exactly

```math
\boxed{A_e\succeq10^{-35}I_{1075}},
```

```math
\boxed{A_o\succeq10^{-35}I_{1075}}.
```

Together with the already certified #117 Legendre tail/cross transfer, either pair proves `L_1>=0`, hence the canonical `a=1` completion.

---

## 3. Why C uses Legendre first

### 3.1 PSWF route

Advantages:

- only `<=552 x 552` per parity after PR #120;
- smallest current finite obligation.

Additional proof burden still needed:

- rigorous construction of the first 1102 PSWF resolved subspace;
- certified spectral projector/eigenvector enclosures for the commuting Sturm--Liouville operator;
- rigorous moment augmentation and Gram control;
- then the finite form matrix and inertia proof.

### 3.2 Legendre route

Costs:

- `1075 x 1075` per parity.

But already closed:

- exact basis and exact Gram `I`;
- exact parity;
- tail/cross theorem and constants;
- analytic quadrature remainder `<4e-38` in operator norm.

Therefore the remaining proof burden is narrower:

```text
rigorous matrix assembly
        +
verified positive factorization.
```

This makes Legendre the lower-risk **execution backend** for C, while PSWF remains the canonical smaller mathematical reduction and an independent future cross-check.

---

## 4. Fixed quadrature layer imported from #118

Do not retune the integration rule in C.  Keep exactly

```text
frequency interval: [0,1551]
panel width:        <=0.4
Gauss-Legendre q:   40
analytic strip:     |Im xi|<=0.4
```

The existing Exact-Head Arb audit certifies

```math
|r(z)|<42
```

on the strip and

```math
\boxed{\varepsilon_{Q,op}<4\times10^{-38}}
```

for each parity block.

Implementation rule:

1. evaluate the fixed Gauss matrix in Arb;
2. after assembly, add the proved uniform analytic quadrature radius to every same-parity entry;
3. the resulting interval matrix must enclose the **exact** parity block.

Therefore the final factorization can act directly on an interval enclosure of the exact matrix.  No post-hoc floating-point Weyl correction is permitted.

---

## 5. Special-function evaluation architecture

### 5.1 Common-node evaluation

The matrix must be assembled by common quadrature nodes, not one independent special-function call per matrix entry.

At a quadrature node `xi`, compute one rigorous vector

```math
(j_0(\xi),\ldots,j_{2149}(\xi))
```

and reuse it for all same-parity outer products at that node.

### 5.2 Two evaluation regimes

Predeclare two deterministic regimes.

**Near zero (`0<xi<=1`):** use the entire spherical-Bessel representation

```math
j_n(z)
=\frac{z^n}{(2n+1)!!}
\,{}_0F_1\!\left(;n+\frac32;-\frac{z^2}{4}\right),
```

with Arb/ACB enclosures.

**Away from zero (`xi>1`):** use a scaled exact downward three-term recurrence.  Direct Arb half-integer Bessel evaluations supply a high-order anchor pair; the exact recurrence propagates downward.  A separately evaluated deterministic normalization pivot fixes the scale.

Fail closed if:

- an anchor or normalization denominator interval contains `0`;
- any Bessel enclosure is non-finite;
- a recurrence produces a non-finite ball.

Increasing working precision is allowed.  Changing the mathematical target, basis size, or quadrature rule inside C is not.

### 5.3 Moment vector

Compute

```math
a_n=2\sqrt{n+\tfrac12}\,i_n(1/2)
```

with Arb using the positive modified-spherical-Bessel series/bounds already used in #117.  No numerical quadrature is needed for the moment block.

---

## 6. Matrix assembly protocol

For each parity independently:

1. create the exact diagonal `0.1 I` in Arb;
2. assemble the Gauss approximation to `K` using common-node batches and symmetric rank updates;
3. add the analytic entry-radius from #118;
4. add the positive rank-one moment block `2aa^T`;
5. enforce/check interval symmetry;
6. log the largest entry radius and a checksum/hash of the deterministic matrix artifact.

Opposite parity entries are identically zero and are never assembled.

The common-node batching parameter is an implementation/performance parameter only; changing batch size does not alter the proof object.

---

## 7. Verified factorization architecture

Direct interval Cholesky in Legendre degree order is **not** the default because the spectrum is expected to span many orders of magnitude and wrapping can destroy pivots.

Use the following proof-safe preconditioning pattern separately in even and odd sectors.

### Step 1 — untrusted proposal

From the midpoint matrix, compute any high-quality approximate eigenbasis or Cholesky/eigenvector proposal `V`.

This proposal has **zero proof status**.  Ordinary floating point or non-interval multiprecision may be used here.

### Step 2 — freeze

Freeze the entries of `V` to dyadic real numbers represented as exact Arb points.

### Step 3 — interval congruence

Form entirely in Arb

```math
C
=V^T\left(A-10^{-35}I\right)V.
```

Because `A` is already an interval enclosure of the exact block, `C` encloses the exact congruence.

### Step 4 — fail-closed interval Cholesky/LDL

Run verified interval Cholesky/LDL on `C`.

Acceptance criterion:

```text
every decisive pivot interval has strictly positive lower endpoint.
```

If this succeeds then `C>0`.  In particular `V` must be nonsingular (a singular `V` would give a nonzero null vector of `C`), so congruence proves

```math
A-10^{-35}I>0.
```

No separate faith in the approximate eigensolver is required.

A pivot interval containing `0` means **undecided**, never positive.

---

## 8. Predeclared precision ladder

C may increase precision but may not alter the target or basis after seeing pivots.

Use the fixed ladder

```text
512 bits
768 bits
1024 bits
1536 bits
2048 bits
3072 bits
```

At each precision the entire accepted proof stage must be recomputed or deterministically re-enclosed.

Stop at the first precision where all proof checks pass.

If `3072` bits still leaves an undecided pivot, C ends **undecided**.  A different basis, target, quadrature scheme or preconditioner family then requires a new separately declared research pass.

---

## 9. Split C into two runs

To reduce runtime and failure coupling:

### C-even

Certify

```math
A_e\succeq10^{-35}I_{1075}.
```

Run this first.  The even sector is the natural hard gate because for the canonical `lambda=1` completion it coincides with the physical Weil pole sign on even functions.

### C-odd

Only after C-even succeeds, certify

```math
A_o\succeq10^{-35}I_{1075}.
```

The odd canonical completion contains the positive `E^*E` rank-one contribution and is kept as a separate certificate/artifact.

No fixed-window `a=1` promotion occurs after only one parity succeeds.

---

## 10. Required certificate outputs

Each parity run must record at least:

```text
exact repository head SHA
certificate script hash
python-flint version
working precision
quadrature constants/hash
matrix dimension
maximum matrix-entry radius
proposal/preconditioner hash (non-proof metadata)
smallest certified pivot lower endpoint
all acceptance assertions
```

Recommended artifacts:

- deterministic interval-matrix or reproducible matrix seed/data;
- frozen dyadic preconditioner;
- pivot log;
- compact JSON certificate summary.

The proof must remain reproducible from repository source plus pinned dependencies; an opaque binary factor alone is insufficient.

---

## 11. Independent cross-checks

Cross-checks are encouraged but do not replace the proof path.

Predeclare a small set of low, middle, high and off-diagonal entries in each parity block for independent `acb.integral` or equivalent replay.  The independently integrated interval must overlap the common-node matrix interval.

Any non-overlap is a hard bug and blocks certification.

These checks are diagnostic redundancy, not an additional mathematical assumption.

---

## 12. Acceptance and firewalls

C succeeds only if **both** parity certificates prove the fixed `1e-35` shifts.

Then #117's already certified tail/cross transfer yields

```math
L_1\succeq0,
```

and hence the canonical `a=1` completion.

Do not change within C:

- `M=2150`;
- `1075` modes per parity;
- target `1e-35`;
- panel width `<=0.4`;
- Gauss order `40`;
- analytic strip `0.4`.

Allowed adaptation:

- only working precision along the fixed ladder;
- deterministic implementation batching;
- an untrusted proposal/preconditioner, because its correctness is re-proved by interval congruence and factorization.

Do not claim in B:

- either finite parity block is positive;
- `a=1` is proved;
- the Legendre backend supersedes the smaller PSWF reduction;
- all-`a` NP-GAP, Object X or RH.

---

## 13. Status after B

```text
canonical PSWF/Osipov reduction <=1104                    ✓[K/M]
Legendre orthonormal finite backend                        ✓[K/M]
Legendre tail/cross transfer                               ✓[K/M]
Legendre quadrature operator error <4e-38                  ✓[K/M]
final finite certificate architecture                      ✓[M]
C-even: A_e >=1e-35 I                                      ?[O]
C-odd:  A_o >=1e-35 I                                      ?[O]
fixed-window a=1 completion                                ?[O]
all-a NP-GAP / full Object X / RH                          ?[O]
```

The next computational pass is therefore **C-even only**.
