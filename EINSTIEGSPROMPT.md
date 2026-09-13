# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

## Arbeitskontext

Forschungsprogramm **Objekt X** zur Riemannschen Hypothese im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor und Research Assistant. Prüfe zuerst den aktuellen `main`-Stand live. Keine mathematische Promotion allein durch Merge, CI oder Numerik.

### Kanonische Quellen

1. `CURRENT-FRONT.md`
2. `00-uebersicht/AKTUELLER_STAND.md`
3. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
4. `00-uebersicht/DAG.md`
5. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`
6. `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`

Aktuelle Hauptaudits:

- `audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md`
- `audits/P11_NP_GAP_Q0_FIRST_CHANNEL_2026-09-13.md`
- `audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md`

### Governance

ChatGPT übernimmt sämtliche GitHub-/Repository-Arbeiten. Externe Modelle dienen ausschließlich als Reviewer/Auditoren. Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`.

---

## Aktueller mathematischer Stand

### 1. COMMON-JUMP `✓[M]`

```math
K_t=T_{t/2}-T_{-t/2}.
```

Archimedischer Ort und Primzahlpotenzen entstehen als kontinuierlicher bzw. atomarer Teil derselben positiven `K_t`-Featuregeometrie. Mit

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
+\log\pi-\psi(1/4)
```

gilt für jedes `a>0`

```math
Q_W(v,w)
=\langle Ev,PEw\rangle
+\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle.
```

Auf Nullpol `D_NP=ker M(0) cap ker M(1)`:

```math
\boxed{
Q_W(v,w)=\langle X_av,X_aw\rangle-\Gamma_a\langle v,w\rangle.
}
```

### 2. Archimedische Resolventenkanäle `✓[M]`

```math
\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m\ge0}e^{-\alpha_m t},
\qquad
\alpha_m=2m+\frac12.
```

Für

```math
A_\alpha=\int_0^\infty e^{-\alpha t}K_t^*K_tdt
```

gilt

```math
\boxed{
A_\alpha
=\frac{2}{\alpha}
(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1}.
}
```

### 3. Exakter `Q_0`-First-Channel-Satz `✓[M]`

Mit

```math
Q_0=-\partial_x^2+\frac14
```

folgt für `alpha_0=1/2`

```math
\boxed{
A_{1/2}=4I-Q_0^{-1},
\qquad
A_{1/2}Q_0=-4\partial_x^2.
}
```

Nur beim ersten Kanal cancelt der Resolventennenner.

### 4. Support-erhaltende Nullpolparametrisierung `✓[M]`

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

### 5. Short-window NP-GAP `✓[M]_part`

Dirichlet-Poincaré und Schur-Tests liefern

```math
\langle v,A_{1/2}v\rangle
\ge\frac{4\pi^2}{\pi^2+a^2}\|v\|^2,
```

```math
\langle v,A_\alpha v\rangle
\ge\frac{2}{\alpha}e^{-\alpha a}\|v\|^2.
```

Daraus folgt analytisch ein nichtleerer Bereich ausreichend kleiner Fenster, in dem

```math
\boxed{
\|X_av\|^2\ge\Gamma_a\|v\|^2
\qquad(v\in D_{NP}(a))
}
```

bereits bewiesen ist.

---

## Nächster Default-Auftrag — `NP-GAP-EXTEND`

Der verbleibende harte Satz ist

```math
\boxed{
\lambda_{NP}(a)\ge\Gamma_a
\quad\text{für jedes }a>0.
}
```

Arbeite in dieser Reihenfolge:

1. Verbessere die höheren Kanaluntergrenzen über den elementaren Schur-Test hinaus.
2. Nutze die exakte `Q_0`-Parametrisierung und prüfe, ob die Summe der Resolventenkanäle einen stärkeren lokalen Operator ergibt.
3. Analysiere den ersten Prime-Cutoff `2a=log2` exakt; keine post-hoc Gegenmasse.
4. Prüfe nonlocal-Poincare-, Paley-Wiener-, de-Branges- und Prolate-Mechanismen nur vorwärts.
5. Ein enger No-Go gegen eine natürliche Klasse zählt als Fortschritt.

### Zirkularitäts-Firewall

Ein Beweis des Bounds für alle Fenster wäre bereits RH. Niemals Weil-Positivität, RH oder einen rückwärts aus positiver Weilform definierten Operator als Input verwenden.

### Numerik-Firewall

Endlichdimensionale Ritz-Minima sind **obere Schranken** für das wahre Infimum. Positive endliche Ritz-Gaps beweisen nichts. Nicht Arb-zertifizierte Werte nicht promoten.

---

## Status

```text
COMMON-JUMP architecture                         ✓[M]
Q0 first-channel intertwining                    ✓[M]
support-preserving null-pole Q0 map              ✓[M]
short-window NP-GAP                              ✓[M]_part
forward Object-X candidate architecture          ✓[M]_part
NP-GAP for every a>0                             ?[O]
full positive Object-X realization / RH          ?[O]
publication novelty                              ?[O]
```

Registry und Arbeitsdefinition werden nicht automatisch promoviert.