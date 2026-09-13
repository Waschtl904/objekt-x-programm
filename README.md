# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie, in der Primzahlpotenz- und archimedische Beiträge der vollständigen Weil-Form aus demselben Mechanismus hervorgehen. Arbeitsname: **Objekt X**.

> **Redaktioneller Stand: 13. September 2026.**  
> Eine gemeinsame positive Prime-/archimedische Featurearchitektur ist konstruiert, und für einen nichtleeren Bereich kurzer Fenster ist der zugehörige Nullpol-Frame-Gap analytisch bewiesen. Eine vollständige positive Objekt-X-Realisierung und ein RH-Beweis liegen nicht vor.

## Hier beginnen

1. **[Aktueller Arbeitsstand](CURRENT-FRONT.md)**
2. **[COMMON-JUMP-Audit](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md)**
3. **[Q0 / short-window NP-GAP](audits/P11_NP_GAP_Q0_FIRST_CHANNEL_2026-09-13.md)**
4. **[Nullpol-Reklassifikation](audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md)**
5. **[Aktueller Stand](00-uebersicht/AKTUELLER_STAND.md)**
6. **[Forschungsroadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)**
7. **[DAG](00-uebersicht/DAG.md)**

## Gemeinsame Prime-/archimedische Jump-Geometrie

Für die unitäre Translation `T_t` setze

```math
\boxed{K_t=T_{t/2}-T_{-t/2}.}
```

Archimedes und Primzahlpotenzen verwenden exakt dieselbe Operatorfamilie. Das gemischte positive Maß ist

```math
\mu_a
=
\frac{e^{-t/2}}{1-e^{-2t}}dt
+
\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}.
```

Die daraus gebaute Hilbert-Featureabbildung `X_a` besitzt eine positive Gramform.

Mit

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
+\log\pi-\psi(1/4)
```

gilt für jedes `a>0`

```math
\boxed{
Q_W(v,w)
=\langle Ev,PEw\rangle
+\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle.
}
```

Auf der Nullpolklasse

```math
D_{NP}=\ker M(0)\cap\ker M(1)
```

verschwindet die Polschicht:

```math
\boxed{
Q_W(v,w)=\langle X_av,X_aw\rangle-\Gamma_a\langle v,w\rangle.
}
```

## Neuer exakter `Q_0`-Treffer

Die archimedische Dichte zerfällt als

```math
\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m\ge0}e^{-\alpha_m t},
\qquad
\alpha_m=2m+\frac12.
```

Jeder Einzelkanal hat die exakte Resolventenform

```math
\boxed{
A_\alpha
=\frac{2}{\alpha}
(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1}.
}
```

Für den ersten Kanal `alpha_0=1/2` und

```math
Q_0=-\partial_x^2+\frac14
```

gilt

```math
\boxed{
A_{1/2}=4I-Q_0^{-1},
\qquad
A_{1/2}Q_0=-4\partial_x^2.
}
```

Nur bei `alpha=1/2` cancelt der Resolventennenner. Die Übereinstimmung mit der Nullpolskala `1/2` ist damit eine exakte Intertwining-Identität, nicht nur ein numerischer Hinweis.

## Support-erhaltende Nullpolparametrisierung

Der Green-Kern von `Q_0^{-1}` ist

```math
G_0(x-y)=e^{-|x-y|/2}.
```

Für eine in `(-a,a)` getragene Funktion sind die beiden äußeren Tails genau proportional zu `E_+` beziehungsweise `E_-`. Deshalb

```math
\boxed{
Q_0:C_c^\infty(-a,a)\xrightarrow{\cong}D_{NP}(a)
}
```

support-erhaltend.

Für `v=Q_0u` wird der erste nichtlokale Jump-Kanal lokal:

```math
\boxed{
\langle v,A_{1/2}v\rangle
=4\|u''\|^2+\|u'\|^2.
}
```

## Erster bewiesener Bereich des NP-GAP

Dirichlet-Poincaré liefert

```math
\langle v,A_{1/2}v\rangle
\ge
\frac{4\pi^2}{\pi^2+a^2}\|v\|^2,
```

während jeder höhere Kanal per Schur-Test

```math
\langle v,A_\alpha v\rangle
\ge
\frac{2}{\alpha}e^{-\alpha a}\|v\|^2
```

erfüllt.

Damit folgt analytisch ein nichtleerer short-window-Bereich, in dem

```math
\boxed{
\|X_av\|^2\ge\Gamma_a\|v\|^2
\qquad(v\in D_{NP}(a))
}
```

bereits unkonditional bewiesen ist.

Status:

```text
COMMON-JUMP common geometry                 ✓[M]
Q0 first-channel intertwining               ✓[M]
short-window NP-GAP                         ✓[M]_part
forward Object-X candidate architecture     ✓[M]_part
NP-GAP for every a>0                        ?[O]
full positive Object-X realization / RH     ?[O]
publication novelty                         ?[O]
```

## Was jetzt noch offen ist

Der verbleibende harte Satz lautet

```math
\boxed{
\lambda_{NP}(a)
:=
\inf_{0\ne v\in D_{NP}(a)}
\frac{\|X_av\|^2}{\|v\|^2}
\stackrel{?}{\ge}\Gamma_a
\quad\text{für jedes }a>0.
}
```

Für die Familie aller Fenster ist dies über das globale restricted Weil-Kriterium die verbleibende RH-äquivalente Frame-/Spektralgap-Frage.

## Firewalls

- Short-window NP-GAP ist nicht der all-`a`-Satz.
- Kein einzelnes fixes Fenster wird als RH-äquivalent behauptet.
- Endlichdimensionale Ritz-Minima sind obere Schranken für das wahre Infimum; positive nicht zertifizierte Ritz-Gaps beweisen nichts.
- COMMON-JUMP plus Teil-Gap ist noch keine vollständige positive Objekt-X-Realisierung.
- Keine Publikationspriorität wird beansprucht.
- Registry und Arbeitsdefinition werden nicht automatisch promoviert.

OX-GEN-A bleibt die exakte Polschicht. POS-DIL #101--#105 bleibt eine mathematisch gültige auxiliary full-class route.

Ausarbeitungen: [papers/](papers/) · Audits: [audits/](audits/) · Registry: [ACTIVE_THEOREM_REGISTRY](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md) · Einstieg: [EINSTIEGSPROMPT](EINSTIEGSPROMPT.md).

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff).