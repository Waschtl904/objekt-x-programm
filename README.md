# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

> **Stand: 13. September 2026.**  
> COMMON-JUMP liefert die gemeinsame Prime-/archimedische Featurearchitektur. Für `a=1` reduzieren rigorose Fourier-, Prolate- und Schur-Schranken den offenen fixed-window Satz kanonisch auf höchstens `1212` Dimensionen. Zusätzlich existiert nun ein orthonormaler Legendre-Zertifikatsbackend, dessen analytischer Quadraturfehler bereits rigoros weit unter dem finalen Matrixziel liegt. Objekt X und RH bleiben offen.

## Hier beginnen

1. [CURRENT-FRONT](CURRENT-FRONT.md)
2. [A1 Legendre quadrature budget](audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md)
3. [A1 Legendre finite backend](audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md)
4. [A1 Omega1551 reduction](audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md)
5. [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)

## Kanonische `a=1`-Reduktion

Exakt gilt

```math
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi.
```

Exact-Head Arb zertifiziert

```math
m_1(\xi)>0.1\quad(|\xi|\ge1551),
\qquad
\|r\|_\infty<12,
```

und die moment-augmentierte PSWF-Schur-Reduktion liefert bei `N=1210`

```math
\lambda_{1210}<1.5\times10^{-42},
\qquad
\text{Schur penalty}<2.2\times10^{-39}.
```

Damit genügt kanonisch nur noch

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

auf höchstens

```text
1212 total = 606 even + 606 odd.
```

Dieser finite Satz ist noch offen.

## Alternative orthonormale Legendre-Route

Für

```math
T_n(x)=\sqrt{n+\frac12}P_n(x),
\qquad n=0,\ldots,2149,
```

ist die Basis orthonormal. Die alternative Route reduziert auf

```text
1075 even + 1075 odd
```

mit predeclared target

```math
10^{-35}I.
```

Die kleinere PSWF-Route bleibt kanonisch; die Legendre-Route ist ein expliziter Zertifikatsbackend mit Gram `I`.

### Certified quadrature budget

Der neue Exact-Head-Arb-Gate fixiert

```text
panel width <=0.4
Gauss-Legendre order 40
analytic strip |Im xi|<=0.4.
```

Er beweist auf der analytischen Fortsetzung

```math
|r(z)|<42
```

und daraus für jeden `1075 x 1075` Paritätsblock

```math
\boxed{\|K-\widetilde K\|_{op}<4\times10^{-38}.}
```

Der tatsächliche zertifizierte Wert liegt bei ungefähr `3.9534e-38`; der analytische Quadraturfehler ist damit mehr als Faktor `250` kleiner als das `1e-35` Matrixziel.

## Was jetzt noch fehlt

Für den Legendre-Backend bleiben nur:

- hochpräzise Matrixassemblierung;
- rigorose Special-function/Rounding-Enclosures;
- verifizierte LDL/Cholesky-/Inertia-Prüfung beider Paritätsblöcke;
- explizites Residual/Weyl-Budget inklusive des bereits geschlossenen Quadraturfehlers.

Ein Pivotintervall mit `0` ist **undecided**, nicht positiv.

## Status

```text
COMMON-JUMP / completion / parity            ✓[M]
Omega1551 / PSWF-Schur finite reduction      ✓[K/M]
canonical 1212-dimensional finite gate       ?[O]
Legendre orthonormal backend M=2150          ✓[K/M]
Legendre quadrature operator error <4e-38    ✓[K/M]
Legendre final finite PSD                    ?[O]
certified a=1 completion                     ?[O]
all-a NP-GAP                                 ?[O]
forward Object-X architecture                ✓[M]_part
full positive Object-X / RH                  ?[O]
```

## Bibliographic note

Current arXiv v2 metadata for arXiv:2608.24827 lists **Xuefeng Zhu** as author. Earlier project text temporarily attributing the preprint to Marcus Chuk is bibliographically superseded; the mathematical benchmark statements are unchanged.

Registry und Objekt-X-Arbeitsdefinition bleiben ohne separate Promotion unverändert.

Lizenz: [CC BY 4.0](LICENSE).
