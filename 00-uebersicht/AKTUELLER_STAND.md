# Aktueller Stand — Objekt X / A1-FINITE-1212

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [A1 Omega1551](../audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md), [A1 Legendre quadrature budget](../audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md).

## 1. Kanonische `a=1`-Reduktion

Rank-2 Completion, Morse/Parity, exakte Fourierform sowie die Prolate-Schur-Reduktion sind geschlossen. Exact-Head Arb zertifiziert

```math
m_1(\xi)>0.1\quad(|\xi|\ge1551),
\qquad
\|r\|_\infty<12,
```

und mit `N=1210`

```math
\lambda_{1210}<1.5\times10^{-42},
\qquad
\text{Schur penalty}<2.2\times10^{-39}.
```

Damit bleibt kanonisch nur

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

auf höchstens `1212 = 606 even + 606 odd` Dimensionen. Dieser Satz ist `?[O]`.

## 2. Orthogonale Legendre-Alternative

PR #117 liefert zusätzlich eine basisexplizite orthonormale Route mit den ersten `2150` normalisierten Legendrepolynomen. Die finite Matrix zerfällt in

```text
1075 even + 1075 odd
```

und hat den predeclared sufficient target

```math
10^{-35}I.
```

Die kleinere PSWF-Reduktion bleibt kanonisch; die Legendre-Route ist ein alternativer Zertifikatsbackend mit Gram `I`.

## 3. Quadraturfehler ist geschlossen `✓[K/M]`

Der neue Arb-Gate fixiert

```text
panel width <= 0.4,
Gauss order 40,
strip |Im xi|<=0.4.
```

Er zertifiziert

```math
|r(z)|<42
```

auf der analytischen Fortsetzung und daraus

```math
\boxed{
\|K-\widetilde K\|_{op}<4\times10^{-38}
}
```

für jeden `1075 x 1075` Paritätsblock.

Der tatsächliche Exact-Head-Wert liegt bei etwa `3.9534e-38`. Damit ist die analytische Quadraturtrunkation mehr als Faktor `250` kleiner als das Legendre-Headziel `1e-35`.

## 4. Verbleibender Legendre-Gate

Offen ist jetzt nur noch:

1. hochpräzise Assemblierung der beiden Paritätsmatrizen;
2. rigoroses Special-function/Rounding-Budget zusätzlich zum bereits geschlossenen Quadraturbudget;
3. verifizierte LDL/Cholesky- oder gleichwertige Inertia-Prüfung von
   ```math
   A_{e,o}-10^{-35}I.
   ```

Ein Pivotintervall, das `0` enthält, ist `undecided`, nicht positiv.

## 5. Status

```text
canonical PSWF finite reduction <=1212        ✓[K/M]
canonical resolved lower bound >=3e-39        ?[O]
Legendre orthonormal backend M=2150           ✓[K/M]
Legendre quadrature operator error <4e-38     ✓[K/M]
Legendre even/odd finite positivity           ?[O]
certified a=1 completion                      ?[O]
all-a NP-GAP                                  ?[O]
forward Object-X architecture                 ✓[M]_part
full positive Object-X / RH                   ?[O]
```
