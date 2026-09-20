> [!WARNING]
> **HISTORICAL SNAPSHOT — nur die operative Navigation ist ersetzt.**
>
> As of: 2026-09-14
> Nicht zur Bestimmung der aktuellen Forschungsfront verwenden.
> Kanonischer Status: [RESEARCH_STATE.yaml](00-uebersicht/RESEARCH_STATE.yaml).
> Lesbarer Einstieg: [CURRENT_STATE.md](00-uebersicht/CURRENT_STATE.md).
> Der folgende Originalinhalt bleibt als Provenienz unverändert erhalten.
> Mathematische Inhalte werden durch diesen Hinweis nicht pauschal verworfen.

# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

> **Stand: 14. September 2026.**  
> COMMON-JUMP liefert die gemeinsame Prime-/archimedische Featurearchitektur. Für `a=1` reduzieren rigorose Fourier-, Prolate- und Schur-Schranken den offenen fixed-window Satz kanonisch auf höchstens `1104` Dimensionen. Zusätzlich existiert ein orthonormaler Legendre-Zertifikatsbackend mit bereits geschlossenem Tail/Cross- und Quadraturbudget. Objekt X und RH bleiben offen.

## Hier beginnen

1. [CURRENT-FRONT](CURRENT-FRONT.md)
2. [A1 Osipov N1102 reduction](audits/P11_A1_OSIPOV1102_REDUCTION_2026-09-14.md)
3. [A1 Omega1551 reduction](audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md)
4. [A1 Legendre quadrature budget](audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md)
5. [A1 Legendre finite backend](audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md)
6. [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)

## Kanonische `a=1`-Reduktion

Exakt gilt

```math
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi.
```

Exact-Head Arb zertifiziert

```math
m_1(\xi)>0.1\quad(|\xi|\ge1551),
\qquad
\|r\|_\infty<12.
```

Für die Prolate-Konzentration importieren wir Osipov Theorem 4:

```math
|\lambda_n^F|\le
\frac{\sqrt\pi\,c^n(n!)^2}{(2n)!\Gamma(n+3/2)},
\qquad
\mu_n=\frac{c}{2\pi}|\lambda_n^F|^2.
```

Mit den vorab festgelegten Werten

```text
c=1551,
N=1102
```

zertifiziert der 256-bit-Arb-Gate

```math
\boxed{\mu_{1102}<10^{-43}},
\qquad
\boxed{\tau_{1102}>0.099},
```

und

```math
\boxed{\text{Schur penalty}<1.5\times10^{-40}.}
```

Der tatsächliche zertifizierte Penalty-Upper-Bound liegt bei etwa `1.22873e-40`.

Damit genügt kanonisch nur noch

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

auf höchstens

```text
1104 total = 552 even + 552 odd.
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

Der Legendre-Tail/Cross ist zertifiziert. Zusätzlich beweist Exact-Head Arb für jeden Paritätsblock

```math
\boxed{\|K-\widetilde K\|_{op}<4\times10^{-38}.}
```

Diese Route ist größer als die kanonische PSWF-/Osipov-Reduktion, aber basisexplizit und besitzt Gram `I`.

## Was nach Durchlauf A noch fehlt

Nur endliche Operatorpositivität:

- kanonisch: höchstens `552 x 552` pro Parität gegen den Shift `3e-39`;
- alternativ: zwei orthonormale Legendre-Blöcke `1075 x 1075` gegen `1e-35`;
- jeweils mit rigoroser Matrixassemblierung, Special-function/Rounding-Enclosures und verifizierter LDL/Cholesky-/Inertia-Prüfung.

Ein Pivotintervall mit `0` ist **undecided**, nicht positiv.

## Status

```text
COMMON-JUMP / completion / parity             ✓[M]
Omega1551 multiplier / bounded remainder      ✓[K/M]
Osipov N=1102 finite reduction                ✓[K/M]
canonical <=1104-dimensional finite gate      ?[O]
Legendre orthonormal backend M=2150           ✓[K/M]
Legendre quadrature operator error <4e-38     ✓[K/M]
Legendre final finite PSD                     ?[O]
certified a=1 completion                      ?[O]
all-a NP-GAP                                  ?[O]
forward Object-X architecture                 ✓[M]_part
full positive Object-X / RH                   ?[O]
```

## Bibliographic note

Current arXiv v2 metadata for arXiv:2608.24827 lists **Xuefeng Zhu** as author. Earlier project text temporarily attributing the preprint to Marcus Chuk is bibliographically superseded; the mathematical benchmark statements are unchanged.

Registry und Objekt-X-Arbeitsdefinition bleiben ohne separate Promotion unverändert.

Lizenz: [CC BY 4.0](LICENSE).
