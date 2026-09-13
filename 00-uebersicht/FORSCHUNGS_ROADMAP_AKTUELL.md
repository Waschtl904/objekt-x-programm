# Objekt X — kanonische Forschungsroadmap v3.1

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Operative Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Nullpol-Filter bleibt verbindlich

```math
D_{NP}=\ker M(0)\cap\ker M(1),
\qquad E|_{D_{NP}}=0.
```

Connes–Consani Proposition C.1 liefert den global RH-äquivalenten Weil-Scope; keine fixed-window-Äquivalenz wird importiert.

## 2. COMMON-JUMP abgeschlossen `✓[M]`

Die gemeinsame Generatorfamilie ist

```math
K_t=T_{t/2}-T_{-t/2}.
```

Archimedes und Primzahlpotenzen sind kontinuierlicher bzw. atomarer Teil derselben positiven Maß-/Featuregeometrie

```math
\mu_a
=
\frac{e^{-t/2}}{1-e^{-2t}}dt
+
\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}.
```

Damit gilt für alle `a>0`

```math
Q_W(v,w)
=\langle Ev,PEw\rangle
+\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle,
```

und auf Nullpol

```math
Q_W(v,w)=\langle X_av,X_aw\rangle-\Gamma_a\langle v,w\rangle.
```

`NP-R1`, `NP-COMMON` und die cutoff-Gauge-Struktur sind damit `✓[M]` geschlossen/subsumiert.

## 3. NP-GAP-A hat jetzt einen exakten Einstieg `✓[M]`

Die archimedische Dichte zerfällt als

```math
\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m\ge0}e^{-\alpha_m t},
\qquad
\alpha_m=2m+\frac12.
```

Mit

```math
A_\alpha=\int_0^\infty e^{-\alpha t}K_t^*K_t\,dt
```

gilt exakt

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

folgt

```math
\boxed{
A_{1/2}=4I-Q_0^{-1},
\qquad
A_{1/2}Q_0=-4\partial_x^2.
}
```

Nur bei `alpha=1/2` cancelt der Resolventennenner. Die frühere `1/2`-Beobachtung ist damit theorematisch erklärt.

## 4. Support-erhaltende Nullpolfaktorisierung `✓[M]`

Der Green-Kern

```math
Q_0^{-1}(x,y)=e^{-|x-y|/2}
```

zeigt direkt, dass die beiden äußeren Tails genau durch `E_+` und `E_-` gesteuert werden. Deshalb

```math
\boxed{
Q_0:C_c^\infty(-a,a)\xrightarrow{\cong}D_{NP}(a)
}
```

support-erhaltend.

Für `v=Q_0u` wird der erste Kanal lokal:

```math
\boxed{
\langle v,A_{1/2}v\rangle
=4\|u''\|^2+\|u'\|^2.
}
```

## 5. NP-GAP-Basisabschätzungen `✓[M]`

Auf Nullpol liefert Dirichlet-Poincaré

```math
\boxed{
\langle v,A_{1/2}v\rangle
\ge
\frac{4\pi^2}{\pi^2+a^2}\|v\|^2.
}
```

Für jeden höheren Kanal liefert der positive Resolventenkern per Schur-Test

```math
\boxed{
\langle v,A_\alpha v\rangle
\ge
\frac{2}{\alpha}e^{-\alpha a}\|v\|^2.
}
```

Damit ist erstmals echte Coercivity des COMMON-JUMP-Operators aus seiner eigenen Generatorstruktur gewonnen, nicht aus Weil-Positivität rückwärts.

## 6. Short-window NP-GAP abgeschlossen `✓[M]_part`

Setze

```math
B(a)
=
\frac{4\pi^2}{\pi^2+a^2}
+
\sum_{m=1}^\infty\frac{2}{\alpha_m}e^{-\alpha_m a}.
```

`B` ist stetig und streng fallend von `+infinity` nach `0`. Sei `a_*` die eindeutige positive Lösung

```math
B(a_*)=\kappa_*,
\qquad
\kappa_*=\log\pi-\psi(1/4).
```

Für

```math
0<a<\min\{a_*,\tfrac12\log2\}
```

enthält der kanonische Cutoff noch keine Prime-Power-Atome und es gilt

```math
\boxed{
\|X_av\|^2\ge\Gamma_a\|v\|^2
\qquad(v\in D_{NP}(a)).
}
```

Also ist NP-GAP für einen nichtleeren short-window-Bereich analytisch bewiesen.

## 7. Neue Default-Priorität — den bewiesenen Bereich vergrößern

Der offene Kern lautet weiterhin

```math
\boxed{
\lambda_{NP}(a)
\ge\Gamma_a
\quad\text{für jedes }a>0.
}
```

Die Forschungsreihenfolge wird jetzt enger:

1. **NP-GAP-EXTEND:** verbessere die Kanaluntergrenzen über den elementaren Schur-Test hinaus;
2. nutze die exakte `Q_0`-Parametrisierung bei möglichst vielen Kanälen oder bei deren Summe;
3. analysiere den Übergang am ersten Prime-Cutoff `2a=log2` ohne post-hoc Gegenbuchung;
4. prüfe nonlocal-Poincare-, Paley-Wiener-, de-Branges- und Prolate-Mechanismen nur vorwärts;
5. Numerik dient ausschließlich zum Falsifizieren/Lenken und braucht für Promotion Arb-Zertifikate.

## 8. Wichtiger Numerik-Hinweis

Für endliche Nullpol-Unterräume `V_N` gilt

```math
\lambda_{NP}^{(N)}(a)\ge\lambda_{NP}(a).
```

Ritz-Minima sind also **obere Schranken** für das wahre Infimum. Ein positiver endlicher Gap beweist nichts; ein zertifizierter Wert unter `Gamma_a` würde dagegen falsifizieren.

## 9. Object-X-Pfad

```text
COMMON-JUMP common positive geometry ✓[M]
        |
        v
Q0 first-channel intertwining ✓[M]
        |
        v
short-window NP-GAP ✓[M]_part
        |
        | extend to every a>0
        v
full NP-GAP ?[O]
        |
        v
Weil positivity on global null-pole class
        |
        v
RH
```

Die Architekturfrage ist damit weiter verengt: Objekt X besitzt einen konkreten positiven Kandidatenoperator und einen ersten bewiesenen Coercivity-Bereich; offen ist die globale Fortsetzung des Gaps.

## 10. Auxiliary / separate

- OX-GEN-A = exakte Pole-layer geometry;
- POS-DIL #101--#105 = auxiliary full-class route;
- Prime-Power AR(1) = eigenständige positive Struktur;
- PR #91, PR #49, R37/G4c separat.

## 11. Firewalls

- short-window NP-GAP != all-`a` NP-GAP;
- kein einzelnes fixes Fenster wird als RH-äquivalent behauptet;
- nicht zertifizierte Ritzwerte bekommen keinen strengen Numerikstatus;
- `forward Object-X architecture` != vollständige positive Objekt-X-Realisierung;
- Publikationsneuheit bleibt `?[O]`;
- keine Registry-Promotion durch Roadmap/CI.