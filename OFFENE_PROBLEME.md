# Offene Probleme — NP-DISCREPANCY / NP-CORR

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [Pole-cleared discrepancy](audits/P11_NP_DISCREPANCY_POLE_CLEARED_CORRELATION_2026-09-13.md), [Prime-overlap AR(1)](audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md).

## Neu geschlossen

### `[SHIFT-NORM-SUM]` `×[M]`

Unabhängige Einzelshift-/Blocknormsummation verfehlt den all-window-Bereich exponentiell. Für `a<log n<2a` ist die Shift-Norm `1/2`, daher ist der separate Normbudget-Term mindestens

```math
2e^a(1+o(1)).
```

### `[RAW-PROLATE]` `×[M]` als hinreichender Mechanismus

Ein `a`-unabhängiger Zeit-Frequenz-Konzentrationsfaktor kann die rohe Prime-Multiplikatoramplitude `~e^a` nicht auf die benötigte Skala bringen. Prolate bleibt nur nach arithmetischer Zentrierung interessant.

### `[NULLPOLE-CORR-GAUGE]` `✓[M]`

```math
\int_0^{2a}2\cosh(t/2)\operatorname{Re}\langle T_tv,v\rangle dt=0
```

für `v in D_NP(a)`.

### `[PRIME-DISCREPANCY]` `✓[M]`

```math
d\mathfrak D(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dt)
-2\cosh(t/2)dt.
```

Dann

```math
\mathcal O_a(v)
=2\int Re\langle T_tv,v\rangle d\mathfrak D(t).
```

Kumulativ:

```math
\mathfrak D(T)
=\sum_{\log n\le T}\frac{\Lambda(n)}{\sqrt n}-4\sinh(T/2).
```

Der PNT-Hauptterm ist entfernt.

### `[POLE-CLEARED-ZETA]` `✓[M]`

```math
\mathcal L[d\mathfrak D](s)
=-\frac{d}{ds}\log[(s^2-1/4)\zeta(s+1/2)].
```

Die beiden Nullpolpunkte `0,1` erscheinen exakt als die herausgenommenen Polfaktoren.

---

## Priorität 0 — `[NP-CORR]` `?[O]`

Zu beweisen ist die strukturierte signed-pairing-Ungleichung

```math
\boxed{
\mathcal A(v)
\ge
-2\int_0^{2a}\mathfrak D(t)
\frac{d}{dt}\operatorname{Re}\langle T_tv,v\rangle dt
}
```

für alle `v in D_NP(a)` und alle `a>0`.

### Pflichtfragen

1. Welche Signwechsel-/Oszillationsinformation über `D(t)` ist wirklich nutzbar, ohne bereits RH einzubauen?
2. Welche Restriktionen erzwingt positive Definitheit der Autokorrelation zusätzlich zum cosh-Moment?
3. Was wird aus `C_v'(t)` nach `v=Q_0u`?
4. Wie erscheinen die exakten per-prime AR(1)-Blöcke innerhalb derselben Diskrepanz?
5. Kann ein centered Toeplitz-/Paley-Wiener-/Prolate-Argument das signed pairing kontrollieren?
6. Gibt es einen expliziten Korrelationszeugen, der diese ganze Mechanismusklasse falsifiziert?

### Harte Firewall

Ein polynomialer Absolutbound

```math
D(T)=O(T^K)
```

für irgendein festes `K` wäre bereits RH-hart. Gesucht ist daher **keine** globale absolute Diskrepanzmajorante, sondern Antikorrelation gegen die spezielle Testklasse.

---

## Priorität 1 — `[AR1-RECONNECT]`

Die exakten Fasern

```math
O_{p,a}^{(N)}=(\log p)(R_{p^{-1/2}}^{(N)}-I)
```

bleiben als lokale Struktur relevant. Ziel ist, die alte AR(1)/Markov-/Weil-tail-Faktorisierung in eine signed-correlation-Aussage für `dD` zu übersetzen.

---

## Priorität 2 — `[CENTERED-PROLATE]`

Prolate/Paley-Wiener nur noch auf der pole-cleared Diskrepanz testen. Ein Gate, das lediglich einen konstanten Konzentrationsfaktor für die rohe Prime-Amplitude verbessert, zählt nicht als Hauptfortschritt.

---

## Endziel

```text
NP-DISCREPANCY signed anti-correlation
        |
        v
all-a NP-GAP
        |
        v
global null-pole Weil positivity
        |
        v
RH
```

## Firewalls

- bekannte Kleinfensterpositivität bleibt Literaturbestand;
- Einzelshift-/Blocknorm-No-Go nicht auf kollektive signed mechanisms überdehnen;
- polynomialer D-Bound nicht als Zwischenziel verkaufen;
- Object X und RH bleiben offen.
