# X-P1.3b.0.7 — A_2D^r als Beurling-/BC-Schatten von S(A_f)

> Angelegt: 17. Juni 2026
> A_2D^r = S(A_f)? Nein. Aber: A_2D^r ~ R_{f,r} = radialer Beurling-Schatten von S(A_f).
> Epistemischer Status: ✓ [M] fuer radiale Struktur; ✗ [H] fuer Vergleichsmorphismus Psi_f.

---

## Ausgangsfrage (aus X-P1.3b.0.6)

Die Funktionalgleichung lebt auf der additiven Adelseite A_f, nicht auf Q_+^x allein.
Frage:
```
Ist A_2D^r ein Beurling-/BC-Schatten von S(A_f)?
```

Schwaecher und realistischer:
```
Traegt A_2D^r die radiale Q_+^x-Projektion von S(A_f)?
```

---

## 1. Radiale Gitterfunktionen auf A_f  ✓ [M]

Fuer q in Q_+^x setze:
```
E_q := 1_{q*Zhat}  in  S(A_f)
```

Die Mengen q*Zhat sind kompakt-offene additive Untergruppen von A_f.
Die Familie {E_q : q in Q_+^x} ist eine natuerliche radiale Familie in S(A_f):
Sie misst nur die Skala q des Standardgitters Zhat.

---

## 2. Fourier-Transformation der Gitterfunktionen  ✓ [M]

Mit selbstdualer Haarmaß-Normalisierung:
```
F_f(1_L) = vol(L) * 1_{L^perp}
```

Fuer L = q*Zhat:
```
L^perp = q^{-1} * Zhat,   vol(q*Zhat) = |q|_f = q^{-1}

==>  F_f(E_q) = q^{-1} * E_{q^{-1}}
```

Die endliche Fourier-Transformation vertauscht exakt die Skala:
```
q  <-->  q^{-1}
```

---

## 3. Halbdichte-Normalisierung  ✓ [M]

Definiere normalisierte Vektoren:
```
eta_q := q^{1/2} * 1_{q*Zhat}   in  S(A_f)
```

Dann:
```
F_f(eta_q) = q^{1/2} * F_f(E_q)
           = q^{1/2} * q^{-1} * E_{q^{-1}}
           = q^{-1/2} * E_{q^{-1}}
           = eta_{q^{-1}}
```

Auf normalisierten Vektoren:
```
+-----------------------------------------------------+
| F_f(eta_q) = eta_{q^{-1}}      (unitaere Inversion) |
+-----------------------------------------------------+
```

Die Halbdichte q^{1/2} ist der strukturelle Ursprung der Zentrierung s = 1/2 + it.

---

## 4. Radialer Schwartz-Bruhat-Schattenraum  ✓ [M]

```
R_f^{fin} := span{eta_q : q in Q_+^x}  ⊂  S(A_f)
```

Dieser Raum ist unter F_f stabil:
```
F_f(eta_q) = eta_{q^{-1}}  in  R_f^{fin}
```

Beurling-Vervollstaendigung:
```
R_{f,r} := { sum_{q in Q_+^x} c_q eta_q  :  sum_q |c_q| (1+l(q))^r < inf }
```

Da l(q) = l(q^{-1}), ist F_f auf R_{f,r} wohldefiniert:
```
F_f(sum_q c_q eta_q) = sum_q c_q eta_{q^{-1}}
```

```
+-------------------------------------------------------------+
| R_{f,r} ist ein Fourier-stabiler Beurling-Schatten von S(A_f). |
+-------------------------------------------------------------+
```

---

## 5. Vergleich mit A_2D^r  ✓ [M]

A_2D^r enthaelt bereits:
- Q_+^x-Graduierung
- symmetrisches Laengengewicht l(q) = l(q^{-1})
- Beurling-Summierbarkeit mit Gewicht w_r(q) = (1+l(q))^r
- BC-/Semigruppen-Rohspur auf N^x ⊂ Q_+^x

Das entspricht genau den Daten von R_{f,r}.

```
+-------------------------------------------------------------+
| A_2D^r ist nicht S(A_f), sondern ein Beurling-BC-Modell   |
| von R_{f,r} = S(A_f)^{rad}.                                |
+-------------------------------------------------------------+
```

---

## 6. Semigruppen-Rohspur als positiver Kegel  ✓ [M]

Rohspur Z_X(s) ~ zeta(s) entsteht aus N^x ⊂ Q_+^x (Skalen q = n).
Fourier-Symmetrie verlangt volle Skalenfamilie q in Q_+^x,
weil F_f die Skala n in n^{-1} verwandelt.

```
N^x  --> Zeta-Rohspur   (einseitig, positiv)
Q_+^x --> Fourier-Stabilit ät   (zweiseitig, symmetrisch)
```

---

## 7. Schattenkriterien fuer Psi_f: A_2D^r --> R_{f,r}  ✗ [H]

Ein Vergleichsmorphismus Psi_f muss erfuellen:

**(i) Gradtreue:**
```
fuer homogene Elemente vom Grad q:  Psi_f(a_q) in C * eta_q
```

**(ii) Gewichtstreue:**
```
Beurling-Gewichte stimmen ueberein: w_r(q) = (1+l(q))^r
```

**(iii) Fourier-Kompatibilitaet:**
```
Psi_f(a_{q^{-1}}) = F_f(Psi_f(a_q))    (bis Halbdichte-Normalisierung)
```

**(iv) Rohspur-Kompatibilitaet:**
```
Auf N^x:  Z_X(s) = sum_{n>=1} n^{-s}  ↔  endliche Zeta-Spur
```

**Status: ✗ [H] -- Konstruktion steht aus (naechster Schritt X-P1.3b.0.8).**

---

## 8. Strukturdiagramm

```
A_2D^r  ~  R_{f,r}  ⊂  S(A_f)  ⊃  Phi_0 = 1_Zhat otimes g_infty
   |            |          |
 Beurling   radiale     volle
  Rohspur  Projektion  Poisson
   Z_X(s)  F_f(eta_q)  F_ad(Phi_0)=Phi_0
     |       = eta_{q^-1}    |
  zeta(s)   q <-> q^{-1}  xi(s)=xi(1-s)
```

---

## Ergebnis  ✓ [M]

```
+-------------------------------------------------------------+
| A_2D^r ≈ R_{f,r} ⊂ S(A_f)^{rad}                          |
|                                                             |
| A_2D^r ist die radiale Beurling-Projektion der             |
| endlichen Poisson-Geometrie.                                |
|                                                             |
| Endliche Fourier-Symmetrie auf diesem Schatten:            |
|   q  <-->  q^{-1}                                          |
|                                                             |
| Halbdichte q^{1/2} erklaert kritische Zentrierung s=1/2+it |
+-------------------------------------------------------------+
```

---

## Weg zur Funktionalgleichung

```
A_2D^r  -->  R_{f,r}  -->  S(A_f)  -->  Poisson  -->  xi(s) = xi(1-s)
  (Psi_f,    (Einbettung   (glob. FT +
  X-P0.8)     X-P0.7 ✓)   Poisson-Summe)
```

---

## Naechster Schritt: X-P1.3b.0.8  ✗ [H]

```
+-------------------------------------------------------------+
| Konstruktion des Vergleichsmorphismus                       |
|   Psi_f: A_2D^r  -->  R_{f,r}                             |
|                                                             |
| Zu zeigen: Psi_f erfuellt Kriterien (i)-(iv) aus X-P0.7   |
| Zu konstruieren: explizite Abbildung auf homogenen Elementen|
+-------------------------------------------------------------+
```

**Status: ✗ [H] -- naechste Frage.**
