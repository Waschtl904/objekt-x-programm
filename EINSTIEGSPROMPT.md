# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

## Arbeitskontext

Forschungsprogramm **Objekt X** zur Riemannschen Hypothese im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor und Research Assistant. Prüfe zuerst den aktuellen `main`-Stand live. Keine mathematische Promotion allein durch Merge, CI oder Numerik.

### Kanonische Hauptquellen

1. `CURRENT-FRONT.md`
2. `audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md`
3. `audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md`
4. `audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md`
5. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
6. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`
7. `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`

ChatGPT übernimmt sämtliche GitHub-/Repository-Arbeiten. Externe Modelle sind Reviewer/Auditoren. Statusmarker strikt trennen.

---

## Aktueller mathematischer Stand

### COMMON-JUMP / Q0

Auf Nullpol

```math
D_{NP}=ker M(0)\cap ker M(1)
```

gilt

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
```

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
Re\langle T_{\log n}v,v\rangle.
```

`Q0=-partial_x^2+1/4` parametrisiert `D_NP(a)` support-erhaltend und intertwined den ersten Gamma-Kanal exakt.

### Einzelshift `✓[M]` + enger No-Go

Für

```math
S_t=(T_t+T_{-t})/2
```

auf `(-a,a)`:

```math
\boxed{
||S_t||=\cos\frac{\pi}{\lceil2a/t\rceil+1}
}
```

für `0<t<2a`. Dieselbe Norm wird bereits auf `D_NP(a)` erreicht.

```text
single-shift null-pole norm improvement   ×[M]
```

Also keine Einzelshift-Normstrategie als Hauptweg weiterverfolgen.

### Vollständiger Prime-Power-Block = AR(1) `✓[M]`

Für

```math
ell_p=log p,
q_p=p^{-1/2}
```

ist nach Faserung modulo `ell_p`

```math
\boxed{
O_{p,a}^{(N)}=(\log p)(R_{q_p}^{(N)}-I_N),
\qquad R_q^{(N)}=(q^{|j-k|}).
}
```

Der positive Sektor des AR(1)-Symbols ist

```math
|theta|<arccos(q_p).
```

Für verschiedene Primzahlen sind die logarithmischen Gitter inkommensurabel.

---

## Nächster Default-Auftrag — MULTIPRIME-AR1

Zu beweisen bleibt

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\sum_pO_{p,a}|_{D_{NP}(a)}
\quad\forall a>0.
}
```

Arbeitsreihenfolge:

1. Quantifiziere die Inkompatibilität der positiven Niedrigfrequenzsektoren verschiedener `log p`-Gitter.
2. Prüfe, ob die bereits bewiesene Prime-Power-AR(1)/Markov-/Weil-tail-Faktorisierung eine gemeinsame Kontraktion liefert.
3. Nutze den Q0-Sobolevtransport der Overlap-Korrelationen.
4. Respektiere exakt die Randvariable `delta_n=2a-log n`.
5. Einzelshift-Normabschätzungen nur noch als Baseline/No-Go, nicht als Hauptmechanismus.

### Firewalls

- Inkommensurabilität ist noch keine quantitative suppression inequality.
- Short-window-Positivität ist literaturbekannt; nur die interne COMMON-JUMP/Q0-Herleitung ist projektintern neu strukturiert.
- Endliche Ritz-Minima sind obere Schranken für das wahre Infimum.
- Ein all-`a`-Beweis ist RH-hart; keine Weil-Positivität rückwärts verwenden.
- Registry und Arbeitsdefinition bleiben ohne separate Promotion unverändert.

## Status

```text
COMMON-JUMP / Q0                            ✓[M]
centered Prime-overlap                      ✓[M]
single-shift exact geometry                 ✓[M]
single-shift null-pole improvement          ×[M]
per-prime AR(1) fibers                      ✓[M]
collective multi-prime suppression          ?[O]
forward Object-X candidate architecture     ✓[M]_part
full positive Object-X / RH                 ?[O]
```
