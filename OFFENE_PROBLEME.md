# Offene Probleme — COMMON-JUMP / NP-OVERLAP

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [Review correction / Prime overlap](audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md).

## Neu geklärt

### `[HIGHER-CHANNEL-EXPONENT]` — `✓[M]`

Der stärkere Bound

```math
A_\alpha\succeq\frac2\alpha e^{-\alpha a}I
```

folgt direkt aus dem Schur-Test für den komprimierten Resolventenkern. Die `e^{-alpha a}`/`e^{-2alpha a}`-Diskrepanz ist geschlossen.

### `[SHORT-WINDOW-BOOKING]`

```text
interne COMMON-JUMP/Q0-Coercivity   ✓[M]_part
neuer short-window Weil-Satz        ×[M]
```

Suzuki Theorem 1.4 enthält bereits eine stärkere volle-Klasse-Kleinfensterpositivität.

### `[PRIME-CENTERING]` — `✓[M]`

Auf Nullpol gilt exakt

```math
\boxed{Q_W(v)=\mathcal A(v)-\mathcal O_a(v)}
```

mit

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
```

Alle äußeren Prime-Kanäle und der gesamte Prime-Diagonalledger verschwinden nach exakter Zentrierung aus dem Restproblem.

### `[Q0-OVERLAP-TRANSPORT]` — `✓[M]`

Für `v=Q0u`:

```math
Re<T_t v,v>
=Re<T_tu'',u''>
+\frac12Re<T_tu',u'>
+\frac1{16}Re<T_tu,u>.
```

---

## Priorität 0 — `[NP-OVERLAP]` `?[O]`

Der harte Satz ist jetzt

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\mathbf O_a|_{D_{NP}(a)}
\quad\forall a>0.
}
```

mit

```math
\mathbf O_a
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\frac{T_{\log n}+T_{-\log n}}2.
```

### `[OVERLAP-SPEC]`

Bestimme das positive Spektrum von `O_a` nach Nullpolkompression. Besonders wichtig: gerade/ungerade Sektoren und die Entwicklung beim Eintritt neuer Prime-Power-Shifts.

### `[OVERLAP-EDGE]`

Für

```math
\delta_n=2a-\log n
```

muss eine scharfe Korrelationseinschränkung gefunden werden, die exakt bei `delta_n=0` verschwindet. Grobe Normschranken ohne Randgeometrie sind voraussichtlich zu schwach.

### `[OVERLAP-Q0]`

Nutze die Sobolev-Korrelationsform nach `v=Q0u`. Gesucht ist eine direkte Kontrolle der positiven Shift-Korrelationen durch den archimedischen Überschuss.

### `[OVERLAP-AR1]`

Prüfe, ob die bereits bewiesene Prime-Power-AR(1)/Weil-tail-Geometrie die gewichtete Summe der Shift-Korrelationen einschränkt. Diese Rückkopplung hat jetzt höhere Priorität als weitere reine Gamma-Kanalverbesserungen.

---

## Priorität 1 — `[GAMMA-LADDER]` auxiliary

Die Operatoren

```math
Q_m=-\partial_x^2+(2m+1/2)^2
```

erzeugen Mellin-Nullstellen bei `-2m` und `2m+1`. Endliche Mengen dieser Bedingungen bleiben im Connes--Consani-Scope zulässig; negative gerade Punkte sind triviale Zeta-Nullstellen.

Offen ist eine saubere simultane support-erhaltende Isomorphie/Faktorisierung und vor allem die Frage, ob sie **quantitativ** `O_a` kontrolliert. Ohne solche Kontrolle bleibt die Leiter auxiliary.

---

## Priorität 2 — Arb-/Numerikgates

- neuer Exact-Head-Arb-Gate für `a_*`;
- endliche Ritz-Minima bleiben obere Schranken für das wahre Infimum;
- numerische Overlap-Spektren dürfen nur als Diagnostik dienen, bis Intervallzertifikate vorliegen.

---

## Danach

```text
NP-OVERLAP all a
  |
  v
positive Weil form on global null-pole class
  |
  v
RH
```

Ein all-`a`-Beweis bleibt RH-hart.

## Firewalls

Nicht behaupten:

- Kleinfensterpositivität sei neu;
- `Gamma_a ~ 4e^a` sei als nackter Skalar die eigentliche Wand;
- die Mehrkanalleiter löse den Prime-overlap;
- ein fixes Fenster sei RH-äquivalent;
- positive Ritzwerte bewiesen Positivität;
- Object X oder RH seien gelöst.