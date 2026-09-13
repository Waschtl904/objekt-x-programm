# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie, in der Primzahlpotenz- und archimedische Beiträge der vollständigen Weil-Form aus demselben Mechanismus hervorgehen. Arbeitsname: **Objekt X**.

> **Redaktioneller Stand: 13. September 2026.**  
> Eine gemeinsame positive Prime-/archimedische Featurearchitektur ist konstruiert. Die aktuelle harte Restfrage ist ein expliziter gewichteter Prime-Überlappungsoperator. Eine vollständige positive Objekt-X-Realisierung und ein RH-Beweis liegen nicht vor.

## Hier beginnen

1. **[Aktueller Arbeitsstand](CURRENT-FRONT.md)**
2. **[Review correction / Prime overlap](audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md)**
3. **[COMMON-JUMP-Audit](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md)**
4. **[Q0 / first channel](audits/P11_NP_GAP_Q0_FIRST_CHANNEL_2026-09-13.md)**
5. **[Forschungsroadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)**
6. **[DAG](00-uebersicht/DAG.md)**

## COMMON-JUMP

Für die unitäre Translation `T_t` setze

```math
K_t=T_{t/2}-T_{-t/2}.
```

Archimedes und Primzahlpotenzen verwenden dieselbe positive Operatorfamilie. Auf der Nullpolklasse

```math
D_{NP}=\ker M(0)\cap\ker M(1)
```

gilt exakt

```math
\boxed{Q_W(v)=\|X_av\|^2-\Gamma_a\|v\|^2.}
```

Das ist die forward Object-X candidate architecture `✓[M]_part`.

## Q0 / erster archimedischer Kanal

Die archimedische Dichte zerfällt in

```math
\alpha_m=2m+\frac12
```

mit Einzelkanälen

```math
A_\alpha
=\frac2\alpha(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1}.
```

Für

```math
Q_0=-\partial_x^2+\frac14
```

ist

```math
\boxed{A_{1/2}Q_0=-4\partial_x^2,}
```

und

```math
Q_0:C_c^\infty(-a,a)\cong D_{NP}(a)
```

support-erhaltend.

Für alle höheren Kanäle liefert ein exakter Schur-Test

```math
\boxed{
A_\alpha\succeq\frac2\alpha e^{-\alpha a}I.
}
```

## Kleinfenster: wichtige Korrektur

Die eigene Architektur reproduziert analytisch eine Kleinfenster-Coercivity. Das ist **kein neuer Kleinfenster-Positivitätssatz der Literatur**: Suzuki Theorem 1.4 beweist bereits eine stärkere unbedingte Positivität auf der vollen lokalen Klasse.

Daher:

```text
COMMON-JUMP/Q0 interne Reproduktion       ✓[M]_part
Short-window positivity als neuer Satz    ×[M]
```

Der zugehörige projektinterne Bound besitzt einen eigenen Arb-Exact-Head-Gate für den Schwellenwert `a_*`.

## Die eigentliche Wand: Prime overlap

Nach exakter Zentrierung cancelt die gesamte Prime-Diagonalmasse gegen den Prime-Anteil der Schwelle. Definiere

```math
\mathcal A(v)
=\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}\|K_tv\|^2dt
-\kappa_*\|v\|^2.
```

Dann gilt auf Nullpol

```math
\boxed{
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
}
```

wobei

```math
\boxed{
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
}
```

Für `log n>=2a` sind die verschobenen Träger disjunkt und die Korrelation verschwindet exakt.

Damit ist der all-window Rest nicht ein nackter exponentiell wachsender Skalar, sondern die operatorielle Dominationsfrage

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\mathbf O_a|_{D_{NP}(a)}.
}
```

## Q0 transportiert auch den Prime overlap

Für `v=Q0u` gilt

```math
\boxed{
Re<T_t v,v>
=Re<T_tu'',u''>
+\frac12Re<T_tu',u'>
+\frac1{16}Re<T_tu,u>.
}
```

Die arithmetische Restfrage wird damit zu einer endlichen Summe von Shift-Korrelationen auf den Sobolev-Ebenen `0,1,2`.

## Neue Hauptfront

`NP-OVERLAP` fragt nach einer scharfen Kontrolle dieses komprimierten Prime-Power-Overlap-Operators. Vorrang haben:

- sein positives Spektrum auf Nullpol und nach Parität;
- die Randvariable `delta_n=2a-log n`;
- der `Q0`-Sobolevtransport;
- die Rückbindung an die bereits bewiesene Prime-Power-AR(1)/Weil-tail-Struktur.

Die finite Gamma-null ladder ist mathematisch legitim, aber auxiliary, solange sie den Prime-overlap nicht quantitativ kontrolliert.

## Status

```text
COMMON-JUMP common geometry                    ✓[M]
Q0 first-channel / support map                 ✓[M]
centered Prime-overlap decomposition           ✓[M]
short-window internal reproduction             ✓[M]_part
short-window novelty claim                     ×[M]
forward Object-X candidate architecture        ✓[M]_part
all-a NP-OVERLAP                               ?[O]
full positive Object-X realization / RH        ?[O]
publication novelty of architecture            ?[O]
```

## Firewalls

- bekannte Kleinfensterpositivität nicht als Neuheit beanspruchen;
- `Gamma_a` nicht isoliert mit dem zentrierten Rest verwechseln;
- finite Ritz-Minima sind obere Schranken für das wahre Infimum;
- kein fixes Fenster ist für sich als RH-äquivalent behauptet;
- Registry und Arbeitsdefinition werden nicht automatisch promoviert;
- RH bleibt offen.

Ausarbeitungen: [papers/](papers/) · Audits: [audits/](audits/) · Registry: [ACTIVE_THEOREM_REGISTRY](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md) · Einstieg: [EINSTIEGSPROMPT](EINSTIEGSPROMPT.md).

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff).