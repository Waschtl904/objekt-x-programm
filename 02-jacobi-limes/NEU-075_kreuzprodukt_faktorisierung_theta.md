# NEU-75 — Kreuzprodukt-Faktorisierung Theta = M_{e_n} partial_theta delta_BC

**Status:** Monomenrechnung gesichert ✓[M]; Weil-Verbindung nur partiell ⚠[M]; Operatoridentitat ❓[O]
**Datum:** 2026-06-30 (Korrektur: delta_BC liefert log n, NICHT Lambda(n) direkt; Mangoldt separat)
**Aufbaut auf:** NEU-74 (V_n ~ M_{e_n}; log n aus delta_BC)

---

## Hauptsatz NEU-75.1 (Monomenversion) ✓[M]

Auf Monomen e_r mu_n der BC-Algebra:
```
Theta(e_r mu_n) := r log(n) e_{r+n} mu_n
= M_{e_n} partial_theta delta_BC (e_r mu_n)
```

**Monomenrechnung:**
```
Schritt 1: delta_BC(e_r mu_n) = e_r delta_BC(mu_n) = log(n) e_r mu_n
Schritt 2: partial_theta [log(n) e_r mu_n] = log(n) * r e_r mu_n = r log(n) e_r mu_n
Schritt 3: M_{e_n} [r log(n) e_r mu_n] = r log(n) e_{r+n} mu_n    ✓[M]
```

Konsistenzproben:
- Theta = 0 fuer r = 0 (keine Diagonalterme) ✓
- Theta = 0 fuer n = 1 (log 1 = 0) ✓

---

## Drei-Faktor-Struktur ✓[M]

```
Theta  =  M_{e_n}          *  partial_theta     *  delta_BC
           ^                      ^                   ^
    Kreischarakter-          Fourier-Derivation    BC-Zeit-Derivation
    verschiebung r->r+n      (r-Gewicht)           (log n-Gewicht)
    (Translation, additiv)   (Kreisseite)          (multiplikative Primseite)
```

**Wichtige Unterscheidung (NEU-74):**
```
mu_m M_{e_r} mu_m^* ~ M_{e_{mr}}    [BC-Kovarianz: Dilatation r -> mr]
M_{e_n} e_r = e_{r+n}               [J_N^-: Translation r -> r+n]
```
Das sind verschiedene Geometrien. ✓[M]

---

## Weil-Verbindung: nur partiell gesichert ⚠[M]

**Gesichert:**
```
delta_BC(mu_n) = log(n) mu_n    fuer alle n in N^x
```

**Nicht automatisch gesichert:**
```
log(n) =/=> Lambda(n)    (von Mangoldt-Funktion)
```

Denn Lambda(n) = log p falls n = p^k (Primpotenz), sonst 0.
Delta_BC liefert log n fuer ALLE n in S_N, nicht nur Primpotenzen.

**Separater Extraktionsschritt noetig:** \warning[M]
```
log n ---[Primsektor-Projektion P_prime]--> Lambda(n)
```

z.B. via Moebius-Inversion oder Primpotenz-Projektion:
```
Lambda(n) = -sum_{d|n} mu(d) log(d)    [Moebius-Mangoldt]
```

oder via Prime-Power-Sektoren:
```
P_prime: eta_{(p,m,r,u)} |-> eta  falls m = p^k, 0 sonst
```

**Korrekte Weil-Verbindung (abgestuft):**
```
delta_BC <-> log n        [gesichert, ✓[M]]
log n => Lambda(n)        [nur nach Mangoldt-Projektion, ⚠[M]]
```

---

## Offener Kern: Operatorversion auf l^2(I_N) ❓[O] -> NEU-76

Gesucht: *-Darstellung oder labelabhaengiger Symboloperator S derart, dass
```
J_N^- = Pi S R D_BC Pi^*    auf l^2(I_N)
```

Mit S(e_r mu_n) = e_{r+n} mu_n (labelabhaengig, nicht fixes f in C(T)).

Status: ❓[O] -> NEU-76

---

## Status NEU-75

| Objekt | Status |
|---|---|
| Monomenrechnung r log n e_{r+n} mu_n | ✓[M] |
| Drei-Faktor-Struktur M_{e_n} partial_theta delta_BC | ✓[M] |
| delta_BC <-> log n (nicht Lambda(n)) | ✓[M] |
| log n -> Lambda(n) (Mangoldt-Extraktion) | ⚠[M] (separater Schritt) |
| Operatoridentitat auf l^2(I_N) | ❓[O] -> NEU-76 |
| Naive *-Darstellung C(T) x| N^x | vermutlich ✗[M] (No-Go, NEU-76) |

---

## Literatur

- Bost & Connes: Selecta Math. 1 (1995)
- Connes & Marcolli: AMS 2008, Kap. 3
- Weil: Comm. Sem. Math. Univ. Lund (1952)
- Meyer: Duke Math. J. 127 (2005) (Spurformel, Lambda vs log n)
- Hardy & Wright: *An Introduction to the Theory of Numbers*, Kap. 17 (Mangoldt)
