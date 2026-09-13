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
- `audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md`

### Governance

ChatGPT übernimmt sämtliche GitHub-/Repository-Arbeiten. Externe Modelle dienen als Reviewer/Auditoren. Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`.

---

## Aktueller mathematischer Stand

### 1. COMMON-JUMP `✓[M]`

```math
K_t=T_{t/2}-T_{-t/2}
```

erzeugt archimedischen und Prime-Power-Anteil in einer gemeinsamen positiven Featuregeometrie. Auf Nullpol:

```math
\boxed{Q_W(v)=\|X_av\|^2-\Gamma_a\|v\|^2.}
```

### 2. Q0 / erster Gamma-Kanal `✓[M]`

```math
A_\alpha
=\frac2\alpha(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1},
```

```math
Q_0=-\partial_x^2+\frac14,
```

```math
\boxed{A_{1/2}Q_0=-4\partial_x^2.}
```

Außerdem

```math
Q_0:C_c^\infty(-a,a)\cong D_{NP}(a)
```

support-erhaltend.

### 3. Höhere Kanäle `✓[M]`

Der Schur-Test beweist

```math
\boxed{
A_\alpha\succeq\frac2\alpha e^{-\alpha a}I
}
```

auf Funktionen mit Träger in `(-a,a)`. Die Exponentendiskrepanz aus dem externen Review ist geschlossen.

### 4. Short-window-Korrektur

Die eigene Architektur reproduziert Kleinfenster-Coercivity, aber die Positivität für kleine Fenster ist nicht neu: Suzuki Theorem 1.4 beweist eine stärkere volle-Klasse-Aussage.

```text
COMMON-JUMP/Q0 interne Reproduktion      ✓[M]_part
neuer short-window Weil-Satz             ×[M]
```

Ein separater Arb-Gate zertifiziert den projektinternen Schwellenwert `a_*`.

### 5. Neue exakte Restform `✓[M]`

Definiere

```math
\mathcal A(v)
=\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}\|K_tv\|^2dt
-\kappa_*\|v\|^2.
```

Dann auf Nullpol:

```math
\boxed{Q_W(v)=\mathcal A(v)-\mathcal O_a(v)}
```

mit

```math
\boxed{
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
}
```

Die Prime-Diagonalmasse cancelt exakt. Der arithmetische Rest besteht ausschließlich aus den überlappenden inneren Prime-Power-Shifts.

### 6. Q0-Transport des overlap `✓[M]`

Für `v=Q0u`:

```math
Re<T_t v,v>
=Re<T_tu'',u''>
+\frac12Re<T_tu',u'>
+\frac1{16}Re<T_tu,u>.
```

---

## Nächster Default-Auftrag — NP-OVERLAP

Zu beweisen ist

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\mathbf O_a|_{D_{NP}(a)}
\quad\text{für alle }a>0.
}
```

Arbeitsreihenfolge:

1. Bestimme das positive Spektrum von `O_a` nach Nullpolkompression, getrennt nach Parität.
2. Nutze den exakten `Q0`-Sobolevtransport der Shift-Korrelationen.
3. Finde scharfe Abschätzungen in der Überlappungsbreite `delta_n=2a-log n`, insbesondere für `delta_n downarrow0`.
4. Verknüpfe diese Frage mit der bereits bewiesenen Prime-Power-AR(1)/Weil-tail-Struktur.
5. Behandle die finite Gamma-null ladder nur auxiliary, solange sie `O_a` nicht quantitativ kontrolliert.

### Zirkularitäts-Firewall

Ein all-`a`-Beweis wäre bereits RH. Niemals Weil-Positivität oder RH als Input zurückverwenden.

### Numerik-Firewall

Endlichdimensionale Ritz-Minima sind obere Schranken für das wahre Infimum. Positive endliche Ritz-Gaps beweisen nichts. Intervall-/Arb-Zertifikate getrennt kennzeichnen.

---

## Status

```text
COMMON-JUMP architecture                         ✓[M]
Q0 first-channel / support map                   ✓[M]
centered Prime-overlap form                      ✓[M]
short-window internal reproduction               ✓[M]_part
short-window novelty                             ×[M]
forward Object-X candidate architecture          ✓[M]_part
NP-OVERLAP for every a>0                         ?[O]
full positive Object-X realization / RH          ?[O]
```

Registry und Arbeitsdefinition werden nicht automatisch promoviert.