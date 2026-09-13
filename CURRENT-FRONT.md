# CURRENT FRONT — Objekt X / COMMON-JUMP → NP-GAP

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 13. September 2026; keine Registry-Promotion.  
> **Kanonische Hauptaudits:** [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md) · [Q0 first channel / short-window NP-GAP](audits/P11_NP_GAP_Q0_FIRST_CHANNEL_2026-09-13.md).  
> Vorheriger strategischer Filter: [Nullpol-Reklassifikation](audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Registry und Arbeitsdefinition bleiben unverändert.

## 1. Nullpol-Hauptklasse

Mit

```math
M(v)(s)=\int_{\mathbb R}v(x)e^{(s-1/2)x}\,dx
```

gilt

```math
E_-(v)=M(v)(0),\qquad E_+(v)=M(v)(1).
```

Auf

```math
\mathscr D_{NP}=\ker M(0)\cap\ker M(1)
```

verschwinden `R_0` und `\mathcal E`. Connes–Consani Proposition C.1 liefert global einen RH-äquivalenten Weil-Scope mit diesen Nullbedingungen. Keine fixed-`a`-Äquivalenz wird behauptet.

## 2. COMMON-JUMP `✓[M]`

Setze

```math
K_t:=T_{t/2}-T_{-t/2},
\qquad
K_t^*K_t=2I-T_t-T_{-t}.
```

Archimedes und Primzahlpotenzen benutzen exakt diese eine positive Featurefamilie:

```math
\mu_a
=
\frac{e^{-t/2}}{1-e^{-2t}}dt
+
\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}.
```

Die vorwärts konstruierte Hilbert-Featureabbildung `\mathcal X_a` erfüllt

```math
\langle\mathcal X_av,\mathcal X_aw\rangle
=
\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}
\langle K_tv,K_tw\rangle dt
+
\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
\langle K_{\log n}v,K_{\log n}w\rangle.
```

Die exakte Schwelle ist

```math
\kappa_*=\log\pi-\psi(1/4)
=\log(8\pi)+\gamma+\frac\pi2,
```

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}+\kappa_*.
```

Für jedes `a>0` gilt exakt

```math
\boxed{
Q_W(v,w)
=
\langle\mathcal Ev,P\mathcal Ew\rangle
+
\langle\mathcal X_av,\mathcal X_aw\rangle
-
\Gamma_a\langle v,w\rangle.
}
```

Auf Nullpol:

```math
\boxed{
Q_W(v,w)
=
\langle\mathcal X_av,\mathcal X_aw\rangle
-
\Gamma_a\langle v,w\rangle.
}
```

Damit sind `log|D|`, `R_1`, Prime shifts und Exterior-shell-Masse in derselben zentrierten Jump-Gram-Struktur subsumiert.

## 3. Cutoff-Gauge `✓[M]`

Neue äußere Prime-Atome erfüllen auf einem kleineren alten Träger

```math
\langle K_{\log n}v,K_{\log n}w\rangle
=2\langle v,w\rangle.
```

Positive Gramform und Schwelle wachsen deshalb exakt gleich. Der gaugeinvariante Gegenstand ist

```math
\mathcal X_a^*\mathcal X_a-\Gamma_aI.
```

## 4. Archimedische Resolventenkanäle `✓[M]`

Die Dichte besitzt die exakte positive Zerlegung

```math
\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m=0}^\infty e^{-\alpha_m t},
\qquad
\alpha_m=2m+\frac12.
```

Für

```math
A_\alpha:=\int_0^\infty e^{-\alpha t}K_t^*K_t\,dt
```

gilt exakt

```math
\boxed{
A_\alpha
=\frac{2}{\alpha}
(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1}.
}
```

Damit ist jeder archimedische Kanal ein positiver Resolventenkanal derselben Jump-Familie.

## 5. `Q_0` trifft den ersten Kanal exakt `✓[M]`

Setze

```math
Q_0:=-\partial_x^2+\frac14.
```

Für `alpha_0=1/2` gilt

```math
\boxed{
A_{1/2}=4I-Q_0^{-1},
\qquad
A_{1/2}Q_0=-4\partial_x^2.
}
```

Für `alpha>0` cancelt der Resolventennenner in `A_\alpha Q_0` nur bei `alpha=1/2`. Die frühere Beobachtung `alpha_0=1/2` ist damit keine bloße Skalenanalogie mehr, sondern eine exakte und innerhalb dieser Kanalfolge eindeutige Intertwining-Identität.

## 6. Support-erhaltende Nullpol-Parametrisierung `✓[M]`

Der Green-Kern von `Q_0^{-1}` ist

```math
G_0(x)=e^{-|x|/2}.
```

Für `supp(v) subset (-a,a)` sind die äußeren Tails von `Q_0^{-1}v` exakt

```math
e^{-x/2}E_+(v)\quad(x>a),
\qquad
e^{x/2}E_-(v)\quad(x<-a).
```

Daher

```math
\boxed{
Q_0:C_c^\infty(-a,a)
\xrightarrow{\cong}
\mathscr D_{NP}(a)
}
```

support-erhaltend. Für `v=Q_0u` wird der erste archimedische Kanal lokal:

```math
\boxed{
\langle v,A_{1/2}v\rangle
=4\|u''\|_2^2+\|u'\|_2^2.
}
```

## 7. Erste quantitative Coercivity `✓[M]`

Mit dem ersten Dirichlet-Eigenwert

```math
\lambda_1(a)=\frac{\pi^2}{4a^2}
```

folgt

```math
\boxed{
\langle v,A_{1/2}v\rangle
\ge
\frac{4\pi^2}{\pi^2+a^2}\|v\|_2^2,
\qquad v\in\mathscr D_{NP}(a).
}
```

Für jeden höheren Kanal liefert der positive Resolventenkern per Schur-Test für auf `(-a,a)` getragenes `v`

```math
\boxed{
\langle v,A_\alpha v\rangle
\ge
\frac{2}{\alpha}e^{-\alpha a}\|v\|_2^2.
}
```

## 8. NP-GAP auf kurzen Fenstern `✓[M]_part`

Definiere

```math
B(a)
:=
\frac{4\pi^2}{\pi^2+a^2}
+
\sum_{m=1}^\infty
\frac{2}{\alpha_m}e^{-\alpha_m a}.
```

`B` ist stetig und streng fallend, mit `B(a)->infinity` für `a downarrow 0` und `B(a)->0` für `a->infinity`. Sei `a_*` die eindeutige positive Lösung

```math
B(a_*)=\kappa_*.
```

Dann gilt für

```math
0<a<\min\{a_*,\tfrac12\log2\}
```

unkonditional

```math
\boxed{
\|\mathcal X_av\|^2\ge\Gamma_a\|v\|_2^2
\qquad(v\in\mathscr D_{NP}(a)).
}
```

Also ist NP-GAP für einen **nichtleeren short-window-Bereich bewiesen**.

Das ist ein echter Teilabschluss, aber kein all-`a`-Satz und kein RH-Beweis.

## 9. Verbleibender Hauptengpass — NP-GAP global `?[O]`

Offen bleibt

```math
\boxed{
\lambda_{NP}(a)
:=
\inf_{0\ne v\in\mathscr D_{NP}(a)}
\frac{\|\mathcal X_av\|^2}{\|v\|_2^2}
\stackrel{?}{\ge}\Gamma_a
\quad\text{für jedes }a>0.
}
```

Für die Familie aller Fenster ist dies die verbleibende RH-äquivalente Lower-Frame-/Spektralgap-Frage. Ein einzelnes festes `a` ist nicht als RH-äquivalent behauptet.

## 10. Numerik-Firewall

Endlichdimensionale Nullpol-Ritzwerte erfüllen für einen Teilraum `V_N`

```math
\lambda_{NP}^{(N)}(a)\ge\lambda_{NP}(a).
```

Sie sind **obere Schranken** für das wahre Infimum. Positive endliche Ritz-Gaps beweisen daher nichts Globales. Die während der Exploration genannten Werte sind nicht Arb-zertifiziert und werden nicht als `✓[N]` geführt.

## 11. Status

```text
COMMON-JUMP exact common feature architecture          ✓[M]
NP-R1 / NP-COMMON / cutoff-gauge structure             ✓[M]
forward Object-X candidate architecture                ✓[M]_part
Q0 first-channel intertwining                          ✓[M]
Q0 support-preserving null-pole bijection              ✓[M]
short-window NP-GAP                                    ✓[M]_part
NP-GAP for all a>0                                     ?[O]
full positive Object-X realization                     ?[O]
publication novelty                                    ?[O]
RH                                                     ?[O]
```

OX-GEN-A bleibt die exakte Polschicht. POS-DIL #101--#105 bleibt eine mathematisch gültige auxiliary full-class route. PR #91, PR #49 und R37/G4c bleiben separate Nebenfronten.

## 12. Firewalls

Nicht behaupten:

- NP-GAP sei für alle `a>0` bewiesen;
- ein positives endliches Ritz-Spektrum zertifiziere den globalen Gap;
- ein einzelnes fixes Fenster sei RH-äquivalent;
- die volle positive Objekt-X-Realisierung liege bereits vor;
- Publikationsneuheit sei geklärt;
- Registry oder Arbeitsdefinition seien automatisch promoviert;
- RH sei bewiesen.