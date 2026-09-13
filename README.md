# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

> **Stand: 13. September 2026.**  
> COMMON-JUMP liefert die gemeinsame Prime-/archimedische Featurearchitektur. Für `a=1` reduzieren rigorose Fourier-, Prolate- und Schur-Schranken den offenen fixed-window Satz auf eine finite resolved-space Untergrenze in höchstens `1212` Dimensionen. Objekt X und RH bleiben offen.

## Hier beginnen

1. [CURRENT-FRONT](CURRENT-FRONT.md)
2. [A1 Omega1551 reduction](audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md)
3. [A1 bounded Schur remainder](audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md)
4. [NP-DUAL-COMP](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md)
5. [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)

## Aktuelle `a=1`-Reduktion

Exakt gilt

```math
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi,
```

mit

```math
m_1(\xi)=\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

Ein Exact-Head-Arb-Zertifikat beweist

```math
\boxed{m_1(\xi)>0.1\quad(|\xi|\ge1551).}
```

Für

```math
r=(m_1-0.1)\mathbf1_{[-1551,1551]}
```

ist `||r||_infty<12` zertifiziert. Der moment-augmentierte Prolate-Split liefert mit `N=1210`

```math
\lambda_{1210}(1551)<1.5\times10^{-42},
```

und daraus

```math
\boxed{\text{Schur penalty}<2.2\times10^{-39}.}
```

Damit genügt jetzt nur noch

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

auf einem resolved Raum von höchstens

```text
1212 total = 606 even + 606 odd.
```

`3e-39` ist ein vorab deklarierter sufficient threshold, kein beobachteter Eigenwert.

## Status

```text
COMMON-JUMP / Q0                         ✓[M]
rank-2 completion / Morse / parity      ✓[M]
exact a=1 multiplier                    ✓[M]
Omega1551 high-frequency certificate    ✓[K/M]
N=1210 Prolate / Schur certificate      ✓[K/M]
1212-dimensional finite reduction       ✓[K/M]
resolved lower bound >=3e-39            ?[O]
certified a=1 completion                ?[O]
all-a NP-GAP                            ?[O]
forward Object-X architecture          ✓[M]_part
full positive Object-X / RH            ?[O]
```

## Bibliographic note

Current arXiv v2 metadata for arXiv:2608.24827 lists **Xuefeng Zhu** as author. Earlier project text temporarily attributing the preprint to Marcus Chuk is bibliographically superseded; the mathematical benchmark statements are unchanged.

Registry und Objekt-X-Arbeitsdefinition bleiben ohne separate Promotion unverändert.

Lizenz: [CC BY 4.0](LICENSE).
