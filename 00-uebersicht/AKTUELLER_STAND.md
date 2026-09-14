# Aktueller Stand — Objekt X / A1-FINITE-1104

> **Stand:** 14. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.

## Kanonische PSWF-Route

Gesichert sind die Completion-/Morse-/Parity-Struktur, der exakte `a=1`-Multiplikator und der `Omega=1551`-Gate

```math
m_1(\xi)>0.1\ (|\xi|\ge1551),
\qquad \|r\|_\infty<12.
```

Neu importiert wird Osipov Theorem 4:

```math
|\lambda_n^F|\le
\frac{\sqrt\pi c^n(n!)^2}{(2n)!\Gamma(n+3/2)},
\qquad
\mu_n=\frac{c}{2\pi}|\lambda_n^F|^2.
```

Für `c=1551`, `N=1102` hat der Arb-Gate bereits auf dem current-main-basierten Precursor-Head zertifiziert

```math
\mu_{1102}<10^{-43},
\quad \tau_{1102}>0.099,
\quad \text{Schur penalty}<1.5\times10^{-40}.
```

Nach finalem Exact-Head-Rerun reduziert dies den kanonischen Rest auf höchstens

```text
1104 = 552 even + 552 odd
```

Dimensionen. Zu beweisen bleibt einzig

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I.}
```

## Alternative Legendre-Route

PRs #117–#118 liefern unabhängig:

```text
M=2150,
1075 even + 1075 odd,
G=I,
finite target 1e-35,
quadrature operator error <4e-38.
```

Offen sind dort die finale intervalle Matrixassemblierung und positive Faktorisierung.

## Status

```text
canonical PSWF reduction <=1104                candidate ✓[K/M]
canonical resolved lower bound >=3e-39         ?[O]
Legendre orthonormal backend M=2150            ✓[K/M]
Legendre quadrature budget                     ✓[K/M]
Legendre finite positivity                     ?[O]
certified a=1 completion                       ?[O]
all-a NP-GAP                                   ?[O]
forward Object-X architecture                  ✓[M]_part
full positive Object-X / RH                    ?[O]
```
