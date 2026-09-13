# Objekt X — kanonische Forschungsroadmap v3.10

> **Stand:** 13. September 2026; Registry und Arbeitsdefinition unverändert.

## Gate C0 — Gesicherte Completionstruktur `✓[M]`

```text
COMMON-JUMP / Q0
rank-2 completion / Morse / parity
canonical lambda=1
exact a=1 Fourier multiplier
moment-augmented Prolate Schur theorem
```

## Gate C1 — Sharpened high-frequency band `✓[K/M]`

Exact-Head Arb zertifiziert

```math
\boxed{m_1(\xi)>0.1\quad(|\xi|\ge1551),}
```

und für

```math
r=(m_1-0.1)1_{[-1551,1551]}
```

```math
\|r\|_\infty<12.
```

## Gate C2 — Canonical PSWF finite reduction `✓[K/M]`

Für `N=1210`:

```math
\lambda_{1210}<1.5\times10^{-42},
\qquad
\text{Schur penalty}<2.2\times10^{-39}.
```

Daher genügt kanonisch

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

auf höchstens `1212 = 606 even + 606 odd` Dimensionen.

Dieser resolved lower bound bleibt `?[O]`.

## Gate C3 — Alternative orthonormale Legendre-Route `✓[K/M]`

Mit

```math
T_n(x)=\sqrt{n+\frac12}P_n(x),
\qquad n=0,\ldots,2149,
```

ist `G=I` exakt.  Der zertifizierte Legendre-Tail bei `M=2150` reduziert die alternative Route auf

```text
1075 even + 1075 odd
```

mit finite target

```math
10^{-35}I.
```

Die kleinere PSWF-Route bleibt kanonisch.

## Gate C4 — Legendre analytic quadrature budget `✓[K/M]`

Predeclared Integrationsbackend:

```text
panel width <=0.4
Gauss-Legendre q=40
analytic strip |Im xi|<=0.4
```

Exact-Head Arb zertifiziert

```math
|r(z)|<42,
```

sowie für jeden Paritätsblock

```math
\boxed{\|K-\widetilde K\|_{op}<4\times10^{-38}.}
```

Zwischenwerte:

```text
per-panel remainder <9.483e-45
per-entry remainder <3.678e-41
operator remainder  <3.954e-38
```

Damit liegt die analytische Quadraturtrunkation mehr als Faktor `250` unter dem `1e-35` Legendre-Headziel.

## Gate C5A — Canonical A1-FINITE-1212 `?[O]`

```math
(L_1)_{RR}\succeq3\times10^{-39}I
```

auf der moment-augmentierten PSWF-Reduktion.

## Gate C5B — LEGENDRE-MATRIX `?[O]`

Alternativ müssen die beiden orthonormalen Paritätsblöcke rigoros erfüllen

```math
A_e\succeq10^{-35}I,
\qquad
A_o\succeq10^{-35}I.
```

Noch erforderlich:

1. hochpräzise Matrixassemblierung;
2. rigoroses Special-function/Rounding-Budget;
3. verifizierte LDL/Cholesky-/Inertia-Prüfung;
4. Residual/Weyl-Abschluss unter Einbezug des bereits zertifizierten Quadraturfehlers.

## Gate C6 — certified a=1 completion `?[O]`

C5A **oder** C5B schließt den fixed-window `a=1`-Satz.

## Gate C7 — all-window mechanism `?[O]`

Erst danach:

```text
a=1 fixed-window theorem
  |
further windows / structural scaling
  |
all-a NP-GAP
  |
RH-hard global criterion.
```

## Firewalls

- Quadrature budget is not finite PSD.
- `3e-39` and `1e-35` are sufficient thresholds, not fitted eigenvalues.
- The Legendre backend does not supersede the smaller PSWF route.
- Fixed-window `a=1`, Object X and RH are not proved.
- Registry/Arbeitsdefinition unchanged.
