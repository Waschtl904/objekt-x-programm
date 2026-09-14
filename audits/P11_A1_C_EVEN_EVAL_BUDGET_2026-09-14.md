# P11 A1 C-EVEN-EVAL — full Gauss-node evaluation-error certificate

**Date:** 2026-09-14  
**Parent:** C-even branch on top of PR #121.  
**Status:** `✓[M] / ✓[K/M]` for the evaluation-error layer only.  
**Registry / Object-X working definition:** unchanged.

## 1. Scope

This audit closes only the special-function / node-evaluation part of the frozen C-even Legendre certificate.  It does **not** prove

```math
A_e\succeq10^{-35}I_{1075}.
```

The frozen mathematical parameters remain

```text
M=2150
1075 even Legendre modes
Omega=1551
panel width <=0.4
Gauss-Legendre q=40
head target = 1e-35
```

and the already certified analytic quadrature remainder remains

```math
\varepsilon_Q<4\times10^{-38}.
```

## 2. Node perturbation theorem imported from C-even engine audit

For

```math
K_e^{(Q)}=\sum_s\alpha_s b_sb_s^T
```

and point proposals `alpha0_s,b0_s`, with

```math
|\alpha_s-\alpha_s^0|\le e_{\alpha,s},
\qquad
\|b_s-b_s^0\|\le e_{b,s},
```

and `B_s=||b_s^0||`,

```math
\|\alpha_s b_sb_s^T-\alpha_s^0b_s^0(b_s^0)^T\|_{op}
\le
 e_{\alpha,s}(B_s+e_{b,s})^2
+|\alpha_s^0|(2B_se_{b,s}+e_{b,s}^2).
```

Status: `✓[M]`.

## 3. Exact even-energy tail theorem

For the normalized even Fourier vector

```math
b_n(x)=(-1)^{n/2}\sqrt{\frac{2(2n+1)}\pi}\,j_n(x),
\qquad n=0,2,4,\ldots,
```

the spherical-Bessel addition theorem gives

```math
\boxed{
\|b_{\rm even}^{\infty}(x)\|_2^2
=\frac{1+j_0(2x)}\pi.
}
```

This converts all unresolved high-order coordinates into one rigorous `l2` remainder instead of componentwise interval radii.

Status: `✓[M]`.

## 4. Direct turning-anchor engine

The successful exact-head engine uses

- low side: elementary `j_0,j_1` plus upward recurrence;
- direct Arb high anchors above the turning zone;
- downward recurrence only across the short high-to-turning interval;
- exact interval intersection in the overlap region;
- the parity-energy identity for the unresolved high tail.

The high anchor is fixed by

```text
n_hi ~= x + 24 x^(1/3) + 32.
```

The frozen precision ladder showed that `3072` bits is the first allowed precision at which the predeclared representative-node target

```math
e_b<10^{-43}
```

holds at all four frozen test nodes.

Earlier long Miller/CF engines failed fail-closed from interval wrapping.  Those failures are engineering no-gos only, not mathematical no-gos for the Legendre route.

## 5. Full 155120-node exact-head sweep

The fixed quadrature contains

```text
3878 panels x 40 nodes = 155120 positive-frequency Gauss nodes.
```

The exact-head workflow

```text
A1 C-even evaluation shards Arb certificate
```

splits those panels into `32` deterministic round-robin shards.  Every shard runs at `3072` bits and must certify at every node

```math
\boxed{e_{b,s}<10^{-43}.}
```

All `32/32` shards passed on exact head

```text
66dc9d7b1441802cb523ec05156d49eaebe5e8fb.
```

No node failed the uniform vector-error gate.

A representative high-frequency shard had worst certified

```text
max e_b < 1.35e-58,
```

showing substantial clearance below `1e-43`.

Status: `✓[K/M]`.

## 6. Scalar-alpha contribution

Each shard also bounds the scalar coefficient-radius contribution from the same nodewise perturbation theorem.  The 32 jobs use a preallocated total budget

```math
\boxed{\varepsilon_{\alpha}<10^{-39}},
```

implemented as `<10^{-39}/32` per shard.

All 32 shard budgets passed.  Observed Arb radii are in practice vastly smaller than this allocation.

Status: `✓[K/M]`.

## 7. Global vector-error budget

The exact even-energy identity implies

```math
\|b_s\|\le\sqrt{2/\pi}.
```

Since `||r||_infty<12` and the positive Gauss weights integrate the interval length `1551`,

```math
\sum_s|\alpha_s|\le12\cdot1551=18612.
```

With the uniform certified node bound

```math
e_b\le10^{-43},
```

the exact-head Arb summary gate gives

```math
\boxed{
\varepsilon_{\rm vector}
<2.9700454891325861\times10^{-39}
<3\times10^{-39}.
}
```

The logged interval was

```text
[2.9700454891325860007273104269994861344290728956567e-39 +/- 5.55e-90].
```

## 8. Closed evaluation-error bound

Combining the vector part and the separately reserved scalar-alpha part,

```math
\boxed{
\varepsilon_{\rm eval}
<3.9700454891325861\times10^{-39}
<4\times10^{-39}.
}
```

The exact-head summary job `eval-budget` completed successfully after all 32 shards had succeeded.

Status: `✓[K/M]`.

## 9. Updated finite ledger

The C-even ledger is now

```math
\varepsilon_{\rm tot}
=
\underbrace{\varepsilon_Q}_{<4e-38}
+
\underbrace{\varepsilon_{\rm eval}}_{<4e-39}
+
\varepsilon_{\rm gemm}
+
\varepsilon_{\rm moment}
+
\varepsilon_{\rm storage}.
```

The next task is therefore no longer special-function enclosure.  It is the deterministic midpoint/fixed-point matrix layer.

Preferred proof-safe construction:

1. quantize weighted proposal vectors onto an exact dyadic grid;
2. form the midpoint Gauss matrix by exact integer Gram products;
3. thereby aim for
   ```text
   epsilon_gemm = 0,
   epsilon_storage = 0;
   ```
4. certify the dyadic quantization error independently;
5. form and certify the finite moment rank-one block;
6. only then attempt the final verified congruence / LDL factorization.

## 10. Firewall / status

```text
node perturbation theorem                              ✓[M]
even Bessel energy identity                            ✓[M]
direct turning-anchor engine                           ✓[K/M]_part
all 155120 Gauss nodes e_b <1e-43                     ✓[K/M]
scalar-alpha evaluation budget <1e-39                 ✓[K/M]
global vector evaluation budget <3e-39                ✓[K/M]
global epsilon_eval <4e-39                            ✓[K/M]
analytic quadrature epsilon_Q <4e-38                  ✓[K/M]
midpoint/GEMM/storage ledger                           ?[O]
moment finite-block ledger                             ?[O]
C-even A_e >=1e-35 I                                  ?[O]
C-odd                                                  not started
fixed-window a=1                                       ?[O]
```

No finite positivity, fixed-window `a=1`, all-window NP-GAP, Object X or RH claim follows from this evaluation certificate alone.
