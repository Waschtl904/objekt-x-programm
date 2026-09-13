# CURRENT FRONT — Objekt X / A1-FINITE-1212

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> **Hauptaudits:** [A1 Omega1551](audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md) · [A1 bounded Schur remainder](audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md) · [A1 Legendre finite backend](audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md) · [A1 Legendre quadrature budget](audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md).

## 1. Gesicherte Completion-Architektur `✓[M]`

Mit

```math
q_a=X_a^*X_a-\Gamma_aI,
\qquad
\mathcal E=(E_+,E_-),
```

ist `D_NP(a)=ker E`. Rank-2 Completion-Dualität, Morse-Index-Filter, Reflection/Parity-Reduktion und die kanonische Completion `lambda=1` sind geschlossen.

## 2. Exact `a=1` Fourier form `✓[M]`

Für zero-extended `v` mit Träger in `(-1,1)` gilt exakt

```math
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi,
```

```math
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

Die Fensterbedingung erzeugt keinen zusätzlichen quadratischen Rest.

## 3. Sharpened high-frequency certificate `✓[K/M]`

Exact-Head-Arb zertifiziert

```math
\boxed{m_1(\xi)>0.1\qquad(|\xi|\ge1551).}
```

Mit

```math
r=(m_1-0.1)\mathbf1_{[-1551,1551]}
```

ist zugleich

```math
\boxed{\|r\|_\infty<12.}
```

## 4. Moment-augmented Prolate Schur theorem `✓[M]`

Für die PSWFs des Bandes `[-1551,1551]` setze

```math
R_N=
\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\},
\qquad
T_N=R_N^\perp.
```

Dann `E|T_N=0`. Für

```math
L_1=0.1I+K+E^*E
```

gilt

```math
\|(L_1)_{RT}\|\le\|r\|_\infty\sqrt{\lambda_N},
```

```math
(L_1)_{TT}\succeq
[0.1-(\Gamma_1+0.1)\lambda_N]I.
```

## 5. Certified `N=1210` reduction `✓[K/M]`

Für `c_PSWF=1551` liefert Karnik--Romberg--Davenport plus Arb

```math
\lambda_{1210}<1.5\times10^{-42},
```

```math
\tau_{1210}>0.099,
```

und

```math
\boxed{\text{Schur penalty}<2.2\times10^{-39}.}
```

Der tatsächliche Exact-Head-Upper-Bound des Penalty ist etwa `2.11526e-39`.

## 6. Kanonischer letzter `a=1`-Gate — A1-FINITE `?[O]`

Vor jeder resolved-space Rechnung wurde der sufficient target festgelegt:

```math
\boxed{
(L_1)_{RR}\succeq3\times10^{-39}I.
}
```

Die ersten `1210` PSWF-Moden sind `605 even + 605 odd`; die Momentaugmentation erhöht die Dimension auf höchstens

```text
1212 total = 606 even + 606 odd.
```

Diese kleinere PSWF-Reduktion bleibt die **kanonische** finale Beweisobligation.

## 7. Alternative orthonormale Legendre-Backend `✓[K/M]`

PR #117 konstruiert zusätzlich eine explizite orthonormale Legendre-Route mit

```math
T_n(x)=\sqrt{n+\frac12}P_n(x),
\qquad n=0,\ldots,2149.
```

Damit ist die Gram-Matrix exakt `I`, Parität ist exakt und

```math
\widehat T_n(\xi)
=(-i)^n\sqrt{\frac{2(n+1/2)}{\pi}}j_n(\xi).
```

Der zertifizierte Legendre-Tail bei `M=2150` reduziert diese alternative Route auf zwei Paritätsblöcke

```text
1075 even + 1075 odd
```

mit predeclared finite target

```math
10^{-35}I.
```

Sie ist größer als die PSWF-Reduktion, aber basisexplizit und hat `G=I`.

## 8. Legendre quadrature budget `✓[K/M]`

Der neue Exact-Head-Arb-Gate fixiert vor Matrixassemblierung:

```text
panel width <= 0.4,
Gauss-Legendre order = 40,
analytic strip |Im xi| <= 0.4.
```

Er zertifiziert auf der komplexen Fortsetzung

```math
|r(z)|<42,
```

und daraus für alle Legendreordnungen bis `2149`

```math
|\text{matrix integrand}|<260000.
```

Mit Bernstein-Ellipse

```math
\rho=2+\sqrt5
```

folgt intervallrigoros

```text
per-panel error   < 9.483e-45
per-entry error   < 3.678e-41
```

und für jeden `1075 x 1075` Paritätsblock

```math
\boxed{
\|K-\widetilde K\|_{op}<4\times10^{-38}.
}
```

Dieser analytische Quadraturfehler liegt mehr als Faktor `250` unter dem Legendre-Headziel `1e-35`.

**Folge:** Für die Legendre-Route ist die Quadraturtrunkation kein offener Engpass mehr. Offen bleiben Matrixassemblierung mit rigorosem Special-function/Rounding-Budget und die verifizierte positive Faktorisierung der beiden Paritätsblöcke.

## 9. Status

```text
COMMON-JUMP / Q0                                      ✓[M]
rank-2 completion / Morse / parity                    ✓[M]
exact a=1 Fourier multiplier                          ✓[M]
Omega1551: m_1>0.1                                    ✓[K/M]
KRD / Schur 1212-dimensional finite reduction         ✓[K/M]
canonical PSWF resolved lower bound >=3e-39           ?[O]
Legendre M=2150 orthonormal backend                    ✓[K/M]
Legendre analytic quadrature error <4e-38              ✓[K/M]
Legendre even 1075x1075 lower bound >=1e-35            ?[O]
Legendre odd 1075x1075 lower bound >=1e-35             ?[O]
certified a=1 completion                              ?[O]
all-a NP-GAP                                          ?[O]
forward Object-X candidate architecture               ✓[M]_part
full positive Object-X / RH                           ?[O]
```

## 10. Literature metadata firewall

Current arXiv v2 metadata for arXiv:2608.24827 lists **Xuefeng Zhu** as author and notes that the author name/affiliation were updated in v2. Historical project text that temporarily stated `Marcus Chuk` is superseded bibliographic metadata; the mathematical benchmark claims are unchanged.

## 11. Firewalls

Do not claim:

- the Legendre quadrature-budget certificate proves either finite matrix positive;
- arithmetic/special-function evaluation and verified factorization are already certified;
- the Legendre route supersedes the smaller PSWF reduction;
- the resolved `3e-39` or Legendre `1e-35` lower bounds have been proved;
- fixed-window `a=1`, all-window NP-GAP, Object X, or RH is solved.
