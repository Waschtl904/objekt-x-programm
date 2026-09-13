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
- `audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md`

### Governance

ChatGPT übernimmt sämtliche GitHub-/Repository-Arbeiten. Externe Modelle dienen ausschließlich als Reviewer/Auditoren. Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`.

---

## Aktueller mathematischer Stand

### 1. Nullpol

```math
E_-(v)=M(v)(0),\qquad E_+(v)=M(v)(1).
```

Auf

```math
D_{NP}=\ker M(0)\cap\ker M(1)
```

verschwinden `R_0` und `E`. Global bleibt die Weil-Vorzeichenbedingung auf dieser Testklasse nach Connes–Consani Proposition C.1 RH-äquivalent. Keine fixed-`a`-Äquivalenz behaupten.

### 2. COMMON-JUMP-GRAM `✓[M]`

Die gemeinsame Operatorfamilie ist

```math
\boxed{K_t=T_{t/2}-T_{-t/2}.}
```

Archimedischer und nichtarchimedischer Anteil sind kontinuierlicher beziehungsweise atomarer Teil desselben positiven Jump-Maßes:

```math
\boxed{
\mu_a
=\frac{e^{-t/2}}{1-e^{-2t}}dt
+\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}.
}
```

Die Featureabbildung `X_a` erfüllt

```math
\langle X_av,X_aw\rangle
=
\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}
\langle K_tv,K_tw\rangle dt
+
\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
\langle K_{\log n}v,K_{\log n}w\rangle.
```

### 3. Exakte Schwelle

```math
\kappa_*=\log\pi-\psi(1/4)
=\log(8\pi)+\gamma+\frac\pi2,
```

```math
\boxed{
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}+\kappa_*.
}
```

### 4. Exakte Weil-Normalform für alle `a>0`

Für `supp(v),supp(w) subset [-a,a]`:

```math
\boxed{
Q_W(v,w)
=\langle Ev,PEw\rangle
+\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle.
}
```

Auf Nullpol:

```math
\boxed{
Q_W(v,w)=\langle X_av,X_aw\rangle-\Gamma_a\langle v,w\rangle.
}
```

Diese Identität ist unkonditional und vorwärts aus der expliziten Formel konstruiert. Sie beweist keine Positivität.

### 5. Strategischer Status

```text
NP-R1 separate geometry question                    closed/subsumed ✓[M]
NP-COMMON common Prime/archimedean geometry          ✓[M]
NP-SCALAR cutoff-gauge covariance                    ✓[M]
forward Object-X candidate architecture              ✓[M]_part
sharp frame/spectral gap                             ?[O]
```

OX-GEN-A bleibt die exakte Polschicht. POS-DIL #101--#105 bleibt auxiliary full-class geometry.

---

## Nächster Default-Auftrag — NP-GAP

Untersuche ausschließlich vorwärts den scharfen Bound

```math
\boxed{
\lambda_{NP}(a)
:=
\inf_{\substack{0\ne v\in C_c^\infty(-a,a)\\M(v)(0)=M(v)(1)=0}}
\frac{\|X_av\|^2}{\|v\|_2^2}
\stackrel{?}{\ge}\Gamma_a
}
```

für alle `a>0`.

Arbeitsreihenfolge:

1. Nutze die Nullpolbedingungen als `hat v(±i/2)=0`.
2. Prüfe die support-erhaltende Faktorisierung durch `Q_0=-d^2/dx^2+1/4`.
3. Suche nonlocal-Poincare-/Dirichlet-form-, Paley-Wiener-/sampling- oder de-Branges-Mechanismen.
4. Definiere jede getestete Mechanismusklasse **vor** dem Resultat.
5. Ein enger No-Go gegen eine natürliche Klasse zählt als Fortschritt.

### Zirkularitäts-Firewall

Ein Beweis des Bounds für alle Fenster wäre bereits RH. Daher niemals Weil-Positivität, RH, fertige Zeta-Nullstellenpositivität oder einen rückwärts daraus definierten Operator als Input verwenden.

---

## Nichtbehauptungen

- COMMON-JUMP ist noch keine vollständige positive Weil-Gram-Realisierung.
- Der Lower-Frame-Bound ist offen.
- Kein einzelnes fixes `a` wird als RH-äquivalent behauptet.
- Publikationsneuheit bleibt offen.
- Object X und RH sind nicht gelöst.
- Registry und Arbeitsdefinition werden nicht automatisch promoviert.