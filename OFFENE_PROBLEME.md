# Offene Probleme — A1-FINITE-CERT

> **Stand:** 14. September 2026.  
> Operative Audits: [A1 finite gate architecture](audits/P11_A1_FINITE_GATE_ARCHITECTURE_2026-09-14.md) · [A1 Osipov N1102](audits/P11_A1_OSIPOV1102_REDUCTION_2026-09-14.md) · [A1 Legendre backend](audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md) · [A1 Legendre quadrature budget](audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md).

## Geschlossen

### `[A1-OSIPOV-1102]` `✓[M] / ✓[K/M]`

```math
\mu_{1102}<10^{-43},
\qquad
\text{Schur penalty}<1.5\times10^{-40}.
```

Damit ist die kanonische mathematische Restreduktion höchstens

```text
1104 = 552 even + 552 odd.
```

### `[A1-LEGENDRE-TAIL]` `✓[K/M]`

Alternative orthonormale Vollraumroute:

```text
M=2150
1075 even + 1075 odd
G=I exactly
finite target=1e-35
```

Tail/Cross sind zertifiziert.

### `[A1-LEGENDRE-QBUDGET]` `✓[K/M]`

Für jeden Legendre-Paritätsblock ist der analytische Quadratur-Operatorfehler zertifiziert:

```math
\|K-\widetilde K\|_{op}<4\times10^{-38}.
```

### `[A1-FINITE-ARCH]` `✓[M]`

Die Ausführungsarchitektur für den ersten vollständigen finite Gate ist fixiert:

- Legendre ist der operative Zertifikatsbackend;
- PSWF/Osipov bleibt die kleinere kanonische mathematische Reduktion;
- `M=2150`, `1075` pro Parität, target `1e-35` werden in C nicht retuned;
- quadrature rule bleibt width `<=0.4`, Gauss `q=40`, strip `0.4`;
- Arb-Intervallmatrix + dyadisch eingefrorener untrusted preconditioner + intervalle Congruence/Cholesky;
- Precision ladder: `512,768,1024,1536,2048,3072` bits;
- Pivotintervall mit `0` = undecided.

---

## Priorität 0 — `[C-EVEN]` `?[O]`

Als nächstes **nur** den geraden Block zertifizieren:

```math
\boxed{A_e\succeq10^{-35}I_{1075}}.
```

Pflichten:

1. common-node Arb assembly;
2. spherical-Bessel vector evaluation with fail-closed recurrence;
3. exact/Arb moment rank-one block;
4. certified #118 quadrature radius in every matrix entry;
5. deterministic interval symmetry checks;
6. untrusted midpoint preconditioner frozen to dyadic points;
7. Arb congruence `V^T(A_e-1e-35 I)V`;
8. verified positive pivots at one fixed precision-ladder level;
9. reproducible matrix/preconditioner/pivot artifacts.

No odd-block work in the same pass if even has not certified.

---

## Priorität 1 — `[C-ODD]` `?[O]`

Only after C-even succeeds:

```math
\boxed{A_o\succeq10^{-35}I_{1075}}.
```

Use the identical fixed protocol and a separate certificate artifact.

---

## Danach — `[A1-CERT]` `?[O]`

```text
C-even green
   +
C-odd green
   +
#117 certified full-space transfer
   |
   v
L_1 >=0
   |
canonical a=1 completion
```

A future direct PSWF finite certificate remains an independent alternate closure route.

---

## Firewalls

- B is architecture, not a positivity result.
- Do not lower `1e-35` after seeing a matrix.
- Do not change `M`, quadrature or basis inside C.
- Only precision may increase along the fixed ladder.
- Float eigenvalues/preconditioners are proposals only.
- Fixed-window `a=1`, all-a NP-GAP, Object X and RH remain open.
