# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

> **Stand: 13. September 2026.**  
> COMMON-JUMP liefert eine gemeinsame Prime-/archimedische positive Featurearchitektur. Fixed-window Nullpolpositivität ist als Rang-2-Completionproblem kanonisiert. Für den ersten Stresspunkt `a=1` ist inzwischen der **gesamte unendlichdimensionale Prolate-Tail rigoros positiv**; offen ist der endliche 1490-Moden-Schur-Abschluss. Eine vollständige positive Objekt-X-Realisierung und RH bleiben offen.

## Hier beginnen

1. [CURRENT-FRONT](CURRENT-FRONT.md)
2. [A1 high-frequency / Prolate tail](audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md)
3. [A1 Morse / Completion diagnostic](audits/P11_NP_DUAL_A1_MORSE_DIAGNOSTIC_2026-09-13.md)
4. [NP-DUAL-COMP](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md)
5. [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md)
6. [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)

## 1. Exact completion interface

```math
q_a(v)=\|X_av\|^2-\Gamma_a\|v\|^2,
\qquad
\mathcal Ev=(E_+(v),E_-(v))^T,
\qquad
D_{NP}(a)=\ker\mathcal E.
```

Strict rank-2 Completion, Morse-Index-Filter, Reflection/Parity-Reduktion und die kanonische Completion `lambda=1` sind `✓[M]`.

## 2. Exact `a=1` Fourier form

Für zero-extended `v` mit `supp(v) subset (-1,1)` gilt

```math
\boxed{
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi
}
```

mit

```math
\boxed{
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
}
```

Die Fensterbedingung erzeugt keinen zusätzlichen quadratischen Rest; sie beschränkt nur die zulässige Paley--Wiener-Klasse.

## 3. Certified high-frequency positivity

Eine elementare Digamma-Reihenuntergrenze mit rigorosem Integralrest wird in einem 256-bit-Arb-Gate ausgewertet und zertifiziert

```math
\boxed{m_1(\xi)>0.04\qquad(|\xi|\ge2300).}
```

Global gilt zugleich `m_1>=-Gamma_1`.

## 4. Rigorous Prolate tail

Sei `C_2300` der Zeit-Band-Konzentrationsoperator auf `[-1,1]` für das Frequenzband `[-2300,2300]`.

Die explizite nichtasymptotische Karnik--Romberg--Davenport-Schranke liefert, durch Arb ausgewertet,

```math
\boxed{\lambda_{1490}(2300)<0.0035.}
```

Für das orthogonale Komplement der ersten `1490` timelimitierten PSWF-Moden folgt damit

```math
\boxed{
q_1(v)>0.01\|v\|^2.
}
```

**Der unendlichdimensionale Prolate-Tail ist damit theorematisch geschlossen.**

Die ersten `1490` PSWF-Moden teilen sich wegen Reflection in `745` even und `745` odd Moden.

## 5. Was bei `a=1` noch fehlt

Für die kanonische Completion

```math
A_1=q_1+\mathcal E^*\mathcal E
```

und die Zerlegung

```math
L^2(-1,1)=R_{1490}\oplus T_{1490}
```

ist bereits

```math
A_{TT}>0.01I.
```

Der verbleibende Gate ist rein

```math
\boxed{
A_{RR}-A_{RT}A_{TT}^{-1}A_{TR}\succeq0.
}
```

Also:

- resolved `1490 x 1490` Formmatrix, parity-separiert `745+745`;
- Arb-zertifizierte finite Inertia/PSD;
- rigorose resolved--tail Kopplungsnorm;
- finaler Schur-Komplement-Abschluss.

Das ist jetzt die **A1-SCHUR**-Front.

## 6. Literaturkontext

Marcus Chuk, arXiv:2608.24827, verwendet denselben exakten compact-window Weil-Symbolmultiplikator und zertifiziert volle Weil-Positivität bei `L=0.8` mit einer anderen finite-reduction/envelope-Methode.

Ein abgeschlossener `a=1`-Schur-Gate wäre deshalb der erste Kandidat dieser Completionroute oberhalb dieses publizierten Lower-Bound-Fensters. Noch wird keine Literaturerweiterung behauptet.

## 7. Nicht-zertifizierte Diagnostik bleibt getrennt

Die früheren Dirichlet-Ritzwerte bis `N=12` und das beobachtete numerische `lambda≈1` bleiben reine Diagnostik. Der neue Tail-Satz zertifiziert sie nicht rückwirkend.

## 8. Status

```text
COMMON-JUMP / Q0                              ✓[M]
rank-2 completion / Morse / parity            ✓[M]
canonical lambda=1 identity                    ✓[M]
exact a=1 Fourier multiplier                   ✓[M]
high-frequency positivity                      ✓[K/M]
full infinite Prolate tail positivity          ✓[K/M]
resolved 1490-mode Arb block                   ?[O]
resolved-tail coupling                         ?[O]
final a=1 Schur certificate                    ?[O]
all-a NP-GAP                                   ?[O]
forward Object-X architecture                  ✓[M]_part
full positive Object-X / RH                    ?[O]
```

## Firewalls

- PSWF basis diagonalisiert den Konzentrationsoperator, nicht `q_1`.
- Positive Tail-Coercivity beweist den vollen `a=1`-Operator noch nicht.
- Finite resolved PSD ohne Crossblock-Schur ist kein Theorem.
- Fixed-window `a=1` ist nicht RH-äquivalent.
- Registry und Objekt-X-Arbeitsdefinition bleiben ohne separate Promotion unverändert.

Lizenz: [CC BY 4.0](LICENSE).
