# Offene Probleme — COMMON-JUMP / NP-GAP

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md), [Q0/short-window NP-GAP](audits/P11_NP_GAP_Q0_FIRST_CHANNEL_2026-09-13.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md).

## Neu geschlossen

### `[NP-R1]`, `[NP-COMMON]`, `[NP-SCALAR-GAUGE]` — `✓[M]`

COMMON-JUMP liefert die gemeinsame positive Operatorfamilie

```math
K_t=T_{t/2}-T_{-t/2}
```

für den kontinuierlichen archimedischen Anteil und die atomaren Prime-Power-Anteile. Die zentrierte Nullpolform ist

```math
\boxed{Q_W|_{NP}=X_a^*X_a-\Gamma_aI.}
```

### `[NP-GAP-A1]` archimedische Kanalzerlegung — `✓[M]`

```math
\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m\ge0}e^{-\alpha_m t},
\qquad
\alpha_m=2m+\frac12,
```

und

```math
\boxed{
A_\alpha
:=\int_0^\infty e^{-\alpha t}K_t^*K_tdt
=\frac{2}{\alpha}(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1}.
}
```

### `[NP-GAP-A2]` erster Kanal trifft `Q_0` exakt — `✓[M]`

Mit

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

Nur bei `alpha=1/2` cancelt der Resolventennenner. Die frühere `1/2`-Beobachtung ist damit theorematisch geschlossen.

### `[NP-GAP-A3]` support-erhaltende Nullpolparametrisierung — `✓[M]`

Der Green-Kern `e^{-|x-y|/2}` zeigt

```math
\boxed{
Q_0:C_c^\infty(-a,a)\xrightarrow{\cong}D_{NP}(a)
}
```

support-erhaltend. Für `v=Q_0u`:

```math
\boxed{
\langle v,A_{1/2}v\rangle
=4\|u''\|^2+\|u'\|^2.
}
```

### `[NP-GAP-SHORT]` — `✓[M]_part`

Aus Dirichlet-Poincaré und Schur-Tests folgt mit

```math
B(a)
=
\frac{4\pi^2}{\pi^2+a^2}
+
\sum_{m=1}^\infty\frac{2}{\alpha_m}e^{-\alpha_m a}
```

ein nichtleerer short-window-Bereich, in dem

```math
\boxed{
\|X_av\|^2\ge\Gamma_a\|v\|^2
\qquad(v\in D_{NP}(a))
}
```

unkonditional bewiesen ist.

---

## Priorität 0 — `[NP-GAP-EXTEND]` `?[O]`

Der harte Rest ist jetzt nicht mehr, *ob* die Architektur Coercivity liefern kann, sondern wie weit der bewiesene Bereich fortgesetzt werden kann:

```math
\boxed{
\lambda_{NP}(a)\ge\Gamma_a
\quad\text{für alle }a>0.
}
```

### Pflichtfragen

1. Kann die exakte `Q_0`-Faktorisierung auf die Summe der höheren Kanäle stärker übertragen werden als mit dem elementaren Schur-Test?
2. Welche scharfe Untergrenze besitzt die komprimierte Resolvente `(L+alpha^2)^{-1}` auf `(-a,a)`?
3. Was passiert am ersten Prime-Cutoff `2a=log2`? Die Schwelle springt um `2 Lambda(2)/sqrt2`, der zugehörige `K_{log2}`-Kanal ist aber innerhalb des Fensters nicht diagonal.
4. Gibt es eine monotone Fortsetzung oder ein Schur-Komplement, das archimedische und neue Prime-Kanäle gemeinsam kontrolliert?
5. Können Prolate-/Paley-Wiener-/de-Branges-Strukturen die fast-extremalen Richtungen erklären, ohne Weil-Positivität rückwärts einzubauen?

---

## Numerik-Firewall

Für einen endlichen Nullpol-Unterraum `V_N` gilt

```math
\lambda_{NP}^{(N)}(a)\ge\lambda_{NP}(a).
```

Ritz-Minima sind daher **obere** Schranken für das wahre Infimum. Positive endliche Gaps beweisen nichts. Nur ein zertifizierter Wert unter `Gamma_a` würde unmittelbar falsifizieren.

Die während der Exploration genannten positiven Werte sind nicht Arb-zertifiziert und erhalten keinen strengen Numerikstatus.

---

## Danach

```text
NP-GAP for every a>0
  |
  v
positive Weil form on global null-pole class
  |
  v
RH
```

Ein all-`a`-Beweis wäre bereits RH. Zirkularitätskontrolle bleibt deshalb bindend.

## Auxiliary / separate

- OX-GEN-A: exakte Pole-layer geometry;
- POS-DIL #101--#105: auxiliary full-class route;
- Prime-Power AR(1): eigenständige positive Struktur;
- R37/G4c, PR #91, PR #49 separat.

## Firewalls

Nicht behaupten:

- short-window NP-GAP sei der globale Gap;
- ein einzelnes fixes `a` sei RH-äquivalent;
- positive Ritzwerte zertifizierten den Gap;
- die vollständige positive Objekt-X-Realisierung liege vor;
- Publikationsneuheit sei geklärt;
- Object X oder RH seien bewiesen.