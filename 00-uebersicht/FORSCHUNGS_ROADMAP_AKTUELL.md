> [!WARNING]
> **HISTORICAL SNAPSHOT**
>
> As of: historical roadmap snapshot  
> Retained for provenance; do **not** use this file to identify the current research frontier.
>
> Canonical current state: `00-uebersicht/RESEARCH_STATE.yaml` and generated `00-uebersicht/CURRENT_STATE.md`.
> This supersedes only the navigation role, not historical mathematical content.

# Objekt X — kanonische Forschungsroadmap v3.12

> **Stand:** 14. September 2026; Registry und Arbeitsdefinition unverändert.

## Gate C0 — Completionstruktur `✓[M]`

```text
COMMON-JUMP / Q0
rank-2 completion / Morse / parity
canonical lambda=1
exact a=1 Fourier multiplier
moment-augmented Prolate Schur theorem
```

## Gate C1 — Omega1551 `✓[K/M]`

```math
m_1(\xi)>0.1\quad(|\xi|\ge1551),
\qquad \|r\|_\infty<12.
```

## Gate C2 — Osipov N1102 `✓[M] / ✓[K/M]`

At predeclared `c=1551`, `N=1102`, Exact-Head Arb certifies

```math
\mu_{1102}<10^{-43},
\quad \tau_{1102}>0.099,
\quad \text{Schur penalty}<1.5\times10^{-40}.
```

## Gate C3 — Canonical mathematical reduction `✓[K/M] / ?[O]`

The smallest certified finite reduction is

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

on at most

```text
1104 total = 552 even + 552 odd.
```

The reduction is certified; the finite lower bound remains `?[O]`.

## Gate C4 — Operational execution backend `✓[M]`

For the first full computer certificate, use the already prepared orthonormal Legendre backend:

```text
M=2150
1075 even + 1075 odd
Gram I exactly
finite target 1e-35
panel width <=0.4
Gauss-Legendre q=40
quadrature operator error <4e-38
```

Reason: the PSWF route is smaller but still needs a certified resolved spectral basis; Legendre already has exact basis/Gram/parity plus closed tail/cross and quadrature budgets.

This is an execution choice only. PSWF/Osipov remains the canonical smaller mathematical reduction.

## Gate C5E — C-even `?[O]`

First certify

```math
\boxed{A_e\succeq10^{-35}I_{1075}}.
```

Protocol:

1. fixed common-node Arb matrix assembly;
2. certified #118 quadrature radius included in entries;
3. positive moment rank-one block;
4. untrusted approximate preconditioner frozen to dyadic points;
5. Arb congruence `V^T(A_e-1e-35 I)V`;
6. fail-closed interval Cholesky/LDL.

Allowed precision ladder only:

```text
512 -> 768 -> 1024 -> 1536 -> 2048 -> 3072 bits.
```

No target/basis/quadrature retuning inside this gate.

## Gate C5O — C-odd `?[O]`

Only after C-even succeeds, certify

```math
\boxed{A_o\succeq10^{-35}I_{1075}}
```

with the same frozen architecture and an independent certificate artifact.

## Gate C6 — certified a=1 completion `?[O]`

Both Legendre parity certificates plus the already certified #117 full-space transfer imply

```text
L_1 >= 0
  => canonical lambda=1 completion >=0
  => fixed-window a=1 null-pole positivity.
```

Alternatively a future direct PSWF finite certificate may close the same gate.

## Gate C7 — all-window mechanism `?[O]`

Only after fixed-window `a=1`:

```text
a=1 theorem
  |
further windows / structural scaling
  |
all-a NP-GAP
  |
RH-hard global criterion
```

## Firewalls

- B defines architecture only; no finite positivity is claimed.
- A pivot interval containing `0` is undecided.
- Working precision may increase; target, basis size and quadrature rule may not be retuned inside C.
- Legendre execution does not supersede the smaller PSWF reduction.
- Fixed-window `a=1`, Object X and RH remain open.
