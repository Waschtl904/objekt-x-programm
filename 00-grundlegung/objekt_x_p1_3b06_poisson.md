# X-P1.3b.0.6 — Endliche Fourier-/Poisson-Symmetrie

> Angelegt: 17. Juni 2026
> Die endliche Symmetrie ist nicht Fourier auf Q_+^x, sondern Poisson auf A_f.
> Kandidat (c) ist der richtige strukturelle Mechanismus.
> Epistemischer Status: ✓ [M] fuer Diagnose; ✗ [H] fuer Vergleich mit S(A_f).

---

## Ausgangspunkt (aus X-P1.3b.0.5)

Archimedischer Teil klar:
```
X_infty = S(R), g_infty(x) = e^{-pi x^2}, F_infty(g_infty) = g_infty.
```

Volle Funktionalgleichung xi_X(s) = xi_X(1-s) hangt an endlicher Symmetrie F_f auf X_f = A_2D^r.

Drei Kandidaten:
(a) adel. Fourier-Transformation auf Q_+^x-Seite
(b) BC-involutiver Automorphismus
(c) Poisson-Summenformel-Interpretation

---

## Korrektur: F_f ist nicht primar Fourier auf Q_+^x  ✓ [M]

```
Q_+^x ist multiplikativ --> Charaktere q^{-it} (Mellin-/Skalenseite).

Fourier-Transformation in Funktionalgleichung = additive Fourier-Transformation
auf den Adelen A_f x R, nicht auf Q_+^x allein.
```

```
+-------------------------------------------------------------+
| Q_+^x traegt die Charaktere, aber nicht die Poisson-        |
| Fourier-Transformation. Die richtige endliche Fourier-Seite |
| lebt auf A_f, nicht auf Q_+^x.                              |
+-------------------------------------------------------------+
```

---

## Warum BC-Involution allein unzureichend  ✓ [M]

BC-Algebra hat:
- Isometrien mu_n und Adjunkte mu_n^*
- partielle Inversion n <-> n^{-1}
- semigruppale Rueckwaertsoperatoren

Aber keine Poisson-Fourier-Transformation --> kein s <-> 1-s automatisch.

```
BC-Involution = Schatten der Inversion, aber nicht die Fourier-Symmetrie.
```

---

## Die richtige endliche Symmetrie: Poisson auf A_f  ✓ [M]

Endliche Fourier-Symmetrie lebt auf Schwartz-Bruhat-Raum:
```
X_f^{Pois} := S(A_f)
```

Auf S(A_f) gibt es additive Fourier-Transformation:
```
F_f: S(A_f) --> S(A_f)
```

Definiert durch nichttrivialen additiven Charakter Psi_f: A_f --> S^1
und selbstduales Haarmass:
```
F_f(phi)(y) = int_{A_f} phi(x) Psi_f(xy) dx
```

---

## Endlicher Standardvektor  ✓ [M]

```
1_Zhat in S(A_f)   (char. Funktion von Zhat = prod_p Z_p)
```

Selbstduale Normalisierung:
```
F_f(1_Zhat) = 1_Zhat
```

Das ist der endliche Gegenpart zu F_infty(g_infty) = g_infty.

Globaler Standardvektor:
```
Phi_0 = 1_Zhat otimes g_infty   -->   F_ad(Phi_0) = Phi_0
```

---

## Endliche Zeta-Spur als adel. Version von Z_X  ✓ [M]

```
int_{A_f^x} 1_Zhat(x) |x|^s d^x x = prod_p (1-p^{-s})^{-1} ~ zeta(s)
```

Das ist die adel. Version der diskret gefundenen Rohspur Z_X(s) = sum_{n>=1} n^{-s}.

```
+-------------------------------------------------------------+
| A_2D^r liefert eine diskrete/Beurling-Schattenform         |
| von S(A_f).                                                 |
+-------------------------------------------------------------+
```

---

## Globale Poisson-Symmetrie = Ursprung der Funktionalgleichung  ✓ [M]

```
S(A) = S(A_f) hat-otimes S(R)
F_ad = F_f hat-otimes F_infty
```

Funktionalgleichung entsteht aus:
1. F_ad(Phi_0) = Phi_0  (Selbstdualitaet des Standardvektors)
2. Poisson-Summenformel fuer Einbettung Q --> A

Das ist der eigentliche Ursprung von s <-> 1-s.

---

## Konsequenz fuer A_2D^r  ✗ [H]

```
+-------------------------------------------------------------+
| F_f ist nicht direkt ein Automorphismus von A_2D^r.         |
|                                                             |
| Man braucht einen Vergleich:                                |
|   A_2D^r  -->  S(A_f)                                       |
| oder Realisierung von A_2D^r als Beurling-/BC-Corner        |
| von S(A_f).                                                 |
+-------------------------------------------------------------+
```

Diagnosefrage:
```
Enthaelt A_2D^r eine endliche Schwartz-Bruhat-/Poisson-Realisierung?
```

Falls ja --> F_f intern rekonstruierbar.
Falls nein --> F_f bleibt externer adel. Zusatz.

---

## Bewertung der drei Kandidaten  ✓ [M]

| Kandidat | Status | Grund |
|----------|--------|-------|
| (a) Fourier auf Q_+^x | x (falsch) | nur q^{-it}, nicht additive Poisson-Fourier |
| (b) BC-Involution | unzureichend | partielle Inversion, aber kein s <-> 1-s |
| (c) Poisson-Summenformel | ✓ richtig | F_ad(Phi_0)=Phi_0 + Poisson auf Q->A |

---

## Neuer Kernsatz  ✓ [M]

```
+-------------------------------------------------------------+
| Die Funktionalgleichung lebt nicht auf der multiplikativen  |
| Gruppe allein, sondern auf der additiven Adelseite.         |
+-------------------------------------------------------------+
```

Verschiebung der naechsten Frage:
```
[alt]  Finde F_f auf Q_+^x
[neu]  Vergleiche A_2D^r mit S(A_f)
```

---

## Naechster Schritt: X-P1.3b.0.7  ✗ [H]

```
+-------------------------------------------------------------+
| Ist A_2D^r ein Beurling-/BC-Schatten der endlichen          |
| Schwartz-Bruhat-Seite S(A_f)?                               |
|                                                             |
| Konkret:                                                    |
| (a) Existiert Morphismus A_2D^r --> S(A_f)?                |
| (b) Sind Beurling-Laenge und p-adische Norm kompatibel?    |
| (c) Traegt A_2D^r eine endliche Fourier-/Poisson-Struktur? |
+-------------------------------------------------------------+
```

**Status: ✗ [H] -- naechste Frage.**
