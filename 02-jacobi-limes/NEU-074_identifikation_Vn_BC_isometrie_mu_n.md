# NEU-74 — Identifikation von V_n mit der BC-Isometrie mu_n im relativen Testsektor

**Status:** V_n ~ mu_n vermutlich falsch ✗/⚠[M]; V_n ~ M_{e_n} wahrscheinlicher ✓/⚠[M]
**Datum:** 2026-06-30 (Korrektur: r |-> r+n ist Charaktermultiplikation, nicht BC-Skalierung; p-adisch kein Ausweg)
**Aufbaut auf:** NEU-73 (J_N^- = sum_n log(n) V_n R; Theta = r(a) log n)

---

## Hauptkorrektur: V_n ~ M_{e_n}, nicht mu_n ✓[M]

Der Shift
```
V_n: e_r |-> e_{r+n}    [additiver r-Shift]
```

entspricht unter der Fourier-/Kreis-Identifikation e_r(theta) = e^{ir theta}
der **Multiplikation mit dem Kreischarakter e_n**:
```
(M_{e_n} f)(theta) = e_n(theta) f(theta) = e^{in theta} f(theta)
=> M_{e_n} e_r = e_{r+n}    [da e_n * e_r = e_{r+n}]
```

Daher:
```
V_n ~ M_{e_n}    [Charaktermultiplikation, nicht BC-Isometrie]  ✓[M]
```

Die BC-Isometrie mu_n wirkt hingegen multiplikativ auf den Index:
```
mu_n: e_k |-> e_{nk}    [Indexskalierung k -> nk]
```

**Translation** (r -> r+n) und **Skalierung** (k -> nk) sind strukturell verschieden:
- Translation r -> r+n: invertierbar, additiv, isometrisch auf l^2(Z)
- Skalierung k -> nk: nicht-surjektiv auf l^2(N), Isometrie aber nicht unitaer

**Fazit:** V_n != mu_n. ✗/⚠[M]

---

## Kandidat B: p-adische Reindizierung -- zurueckgestuft ✗[M]

**Argument gegen Kandidat B:**

Auch p-adisch sind Translation (r -> r+p) und Multiplikation (k -> pk)
strukturell verschieden:
- Translation r -> r+p auf Z_p: invertierbar (additive Gruppe)
- Multiplikation k -> pk auf Z_p: nicht invertierbar (p-adische Kontraktion, |pk|_p = |k|_p/p)

Diese Operationen sind nicht global konjugiert, weder real noch p-adisch.

**Fazit:** p-adische Reindizierung liefert V_n ~ mu_n nicht. ✗[M]

---

## Revidierte Kandidatentabelle

| Kandidat | Mechanismus | Status |
|---|---|---|
| V_n ~ mu_n (direkt) | Translation != Skalierung | ✗[M] |
| V_n ~ M_{e_n} (Charakter) | r -> r+n = Charaktermult. | ✓/⚠[M] |
| p-adische Reindizierung | Kontraktion != Translation | ✗[M] |
| Adeles-Einbettung (Kandidat C) | V_n = Charakteranteil, mu_n = Zeitlabel | ❓[O] |

---

## Neue Bruckenstruktur: Kreuzprodukt-Kopplung ⚠[M]

Die BC-Algebra traegt zwei getrennte Rollen:
```
e_r: Fourier-/Kreisseite   (Charakter, Torus T)
mu_n: BC-/Multiplikativseite  (Zeitlabel, Semigruppe N^x)
```

Monome in der BC-Algebra: e_r mu_n

Die Theta-Matrixstruktur Theta_{ba} ~ r log n entsteht als:
```
Theta = M_{e_n} * partial_theta * delta_BC
```

auf Monomen e_r mu_n:
```
partial_theta(e_r) = r e_r          [Fourier-Derivation: r-Gewicht]
delta_BC(mu_n) = log(n) mu_n        [BC-Derivation: log n-Gewicht]
M_{e_n}(e_r) = e_{r+n}             [Charakterverschiebung]

=> M_{e_n} partial_theta delta_BC (e_r mu_n) = r log n e_{r+n} mu_n  ⚠[M]
```

Das ist exakt die Theta-Matrixstruktur. ⚠[M] -> NEU-75

---

## Implikationen falls M_{e_n} partial_theta delta_BC = Theta ⚠[M]

Falls die Kreuzprodukt-Faktorisierung gilt:
```
J_N^- = sum_n (log n) V_n R
       ~ sum_n M_{e_n} * partial_theta * delta_BC
       = [Kreischarakter-Shift] x [Fourier-Derivation] x [BC-Derivation]
```

Dann ist die additive Divisorgraph-Struktur (J_N^-) eine
**Kreuzprodukt-Realisierung** der BC-Algebra-Derivation. ⚠[M]

---

## Status NEU-74

| Objekt | Status |
|---|---|
| V_n ~ mu_n | ✗/⚠[M] (Translation != Skalierung) |
| V_n ~ M_{e_n} | ✓/⚠[M] (Charaktermultiplikation) |
| p-adische Reindizierung | ✗[M] |
| log n aus delta_BC(mu_n) | ✓[M] |
| Theta ~ M_{e_n} partial_theta delta_BC | ⚠[M] -> NEU-75 |

---

## Literatur

- Bost & Connes: Selecta Math. 1 (1995) (e_r, mu_n, Kreuzproduktstruktur)
- Connes & Marcolli: AMS 2008, Kap. 3 (e_r mu_n als Monom-Basis)
- Rudin, W.: *Fourier Analysis on Groups*, Wiley 1962 (Charaktere, M_{e_n})
