# NEU-67 — Primitive-Orbit-Reduktion und Mangoldt-Gewichtung

**Status:** Lambda = mu*log ✓[M]; log n != Lambda(n) ohne Extraktion ✓[M]; 1/k-Faktor ⚠[M]
**Datum:** 2026-06-29 (Korrektur A/B/C); 2026-06-30 (Schärfung: delta_BC liefert log n, NICHT Lambda(n) direkt)
**Aufbaut auf:** NEU-66 (Divisorpfade, log(p^k) != Lambda(p^k))
**Vorgriff auf:** NEU-75/76 (delta_BC <-> log n; Lambda(n) separat)

---

## WICHTIGE WARNUNG (NEU-75/76) ✓[M]

```
delta_BC(mu_n) = log(n) mu_n    [fuer ALLE n in N^x]
Lambda(n) = log(p)  falls n = p^k, 0 sonst    [Mangoldt]

log(n) =/=> Lambda(n)    direkt!
```

Der Uebergang log n -> Lambda(n) ist ein **separater arithmetischer Extraktionsschritt**:
```
Lambda(n) = (mu * log)(n) = -sum_{d|n} mu(d) log(d)    [Moebius-Mangoldt]
```

Ohne diesen Schritt liefert die BC-Derivation delta_BC nur log n-Gewichte,
nicht die Mangoldt-Funktion Lambda. ✓[M]

---

## Zentralproblem

Die natuerlichen Operatorgewichte aus J_N^- sind log(n) (via BC-Zeitgewicht).
Die explizite Formel braucht Lambda(n).

```
log(p^k) = k log(p)    [Operatorgewicht aus delta_BC]
Lambda(p^k) =   log(p)    [Mangoldt-Gewicht, Faktor k fehlt]
```

Der Unterschied ist strukturell: Faktor k muss auf 1 reduziert werden.

---

## Schluessel-Identitaet: Lambda = mu * log ✓[M]

```
log(n) = sum_{d|n} Lambda(d)    [vollstaendige Zerlegung]
Lambda(n) = sum_{d|n} mu(d) log(n/d) = (mu * log)(n)    [Moebius-Inversion]
```

Fuer n = p^k explizit:
```
(mu * log)(p^k) = log(p^k) - log(p^{k-1}) = k log(p) - (k-1) log(p) = log(p) = Lambda(p^k) ✓
```

Fuer zusammengesetzte n:
```
(mu * log)(n) = 0 = Lambda(n)  ✓
```

---

## Mechanismen A/B/C = dieselbe Korrektur ⚠[M]

Mechanismus A (Primitive-Cycle Reduction): sum_{m>=1} Tr(A^m)/m -> sum_gamma log p
Mechanismus B (Moebius-Inversion): Lambda = mu * log
Mechanismus C (Feshbach-Projektion): Schur-Komplement = geometrische Reihe

Alle drei sind Darstellungen desselben Vorgangs: Primitive-Orbit-Reduktion
= Moebius-Korrektur = Feshbach-/Logdet-Resummation.

```
-d/ds log(1-p^{-s}) = sum_{k>=1} log(p) p^{-ks}    [primitiv gewichtet]
log(1-p^{-s}) = -sum_{k>=1} p^{-ks}/k
-d/ds ...     = sum_{k>=1} k log(p) p^{-ks} * 1/k = sum_{k>=1} log(p) p^{-ks} ✓
```

Genau dieser 1/k-Faktor aus dem Logarithmus + k log(p) aus der Ableitung
erzeugt Lambda(p^k) = log(p) fuer alle k. ⚠[M]

---

## Warnung: log^2(n) ist nicht der richtige Ort ✓[M]

```
(mu * log^2)(p^k) = k^2 log^2(p) - (k-1)^2 log^2(p) = (2k-1) log^2(p) != Lambda(p^k)^2
```

Tr(A_N^2) = sum r^2 log^2(n) kann nicht direkt Mangoldt-Struktur tragen.
Der Mangoldt-Mechanismus erscheint in der Log-Det-Entwicklung
```
log Z_N(z) = -sum_{k>=1} Tr(A_N^k) / (k z^k)
```
nicht in den einzelnen Tr(A_N^k). Der 1/k-Faktor ist entscheidend. ✓[M]

---

## Warnung: mu nicht als Operatorgewicht ✓[M]

Moebius-Gewichte mu(d) sind vorzeichenwechselnd und duerfen nicht direkt
als Operatorgewicht eingebaut werden (zerstoert Selbstadjungiertheit).
mu erscheint in der arithmetischen Auswertung des relativen Determinantenquotienten,
nicht im Operator J_N^-. ✓[M]

---

## Status NEU-67

| Aussage | Status |
|---|---|
| log(n) != Lambda(n) fuer n = p^k, k > 1 | ✓[M] |
| delta_BC liefert log(n), nicht Lambda(n) direkt | ✓[M] |
| Lambda = mu * log (Moebius-Mangoldt) | ✓[M] |
| Mangoldt-Extraktion als separater Schritt | ✓[M] |
| Mechanismen A/B/C = eine Korrektur in drei Darstellungen | ⚠[M] |
| 1/k-Faktor in log Z_N erzeugt Lambda-Gewichtung | ⚠[M] |
| (mu * log^2)(p^k) != Lambda(p^k)^2 | ✓[M] (Warnung) |
| mu nicht als Operatorgewicht | ✓[M] |
| Vollstaendige Identifikation -partial log Z_N ~ Lambda | ❓[O] -> NEU-68 |

---

## Literatur

- Apostol, T.: *Introduction to Analytic Number Theory*, Springer 1976
  (Lambda = mu * log, Kap. 2)
- Selberg, A.: J. Indian Math. Soc. 20 (1956) (1/k-Resummation)
- Ruelle, D.: *Dynamical Zeta Functions*, Bull. AMS 1994 (Primitive-Cycle, 1/m)
- Connes & Marcolli: AMS 2008, Kap. 3 (delta_BC, log n vs Lambda)
- NEU-75: delta_BC <-> log n (nicht Lambda); Mangoldt-Extraktion separat
- NEU-76: No-Go fuer naive BC-*-Darstellung
