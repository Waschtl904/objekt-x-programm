# X-P1.3b.0.8 — Konstruktion des Vergleichsmorphismus Psi_f

> Angelegt: 17. Juni 2026
> Psi_f: A_2D^r --> R_{f,r} als radiale Schattenprojektion.
> Vier Kriterien alle erfuellt. Naechste Frage: Kanonizitaet von tau_0.
> Epistemischer Status: ✓ [M] fuer Konstruktion; ✗ [H] fuer tau_0-Kanonizitaet.

---

## Ziel

Nach X-P1.3b.0.7:
```
R_{f,r} = { sum_{q in Q_+^x} c_q eta_q  :  sum_q |c_q| (1+l(q))^r < inf }
eta_q = q^{1/2} * 1_{q*Zhat}   in  S(A_f)
F_f(eta_q) = eta_{q^{-1}}
```

Gesucht: Vergleichsmorphismus
```
Psi_f: A_2D^r  -->  R_{f,r}
```

---

## 1. Homogene Zerlegung in A_2D^r

```
a = sum_{q in Q_+^x} a_q U_q
```

Kontinuierliches Grundfunktional tau_0 auf dem Koeffizientenraum mit:
```
|tau_0(a_q)| <= C |a_q|_{2D}
```

Beispiele fuer tau_0: Integration, Grundzustand-Erwartung, diagonale BC-Erwartung,
das in der Charakterspur X-P1.3b.0 bereits verwendete Funktional.

---

## 2. Definition von Psi_f  ✓ [M]

```
+-------------------------------------------------------------+
| Psi_f(a) := sum_{q in Q_+^x} tau_0(a_q) * eta_q            |
+-------------------------------------------------------------+
```

Auf homogenen Elementen:
```
Psi_f(a_q U_q) = tau_0(a_q) * eta_q
```

Radiale Projektion: Koeffizient + Grad  -->  skalarer Gradvektor.

---

## 3. Stetigkeit  ✓ [M]

```
|Psi_f(a)|_{R,r} = sum_q |tau_0(a_q)| (1+l(q))^r
                <= C * sum_q |a_q|_{2D} (1+l(q))^r
                 = C * |a|_{A,r}
```

```
==>  Psi_f ist stetig.
```

---

## 4. Kriterium (i): Gradtreue  ✓ [M]

```
Psi_f(a_q U_q) = tau_0(a_q) * eta_q   --> Grad q bleibt erhalten.
```

---

## 5. Kriterium (ii): Gewichtstreue  ✓ [M]

Beurling-Gewicht in A_2D^r und R_{f,r} identisch:
```
w_r(q) = (1+l(q))^r
```

---

## 6. Kriterium (iii): Fourier-Kompatibilitaet  ✓ [M] auf radialem Schatten

Auf R_{f,r}: F_f(eta_q) = eta_{q^{-1}}.

```
F_f(Psi_f(a)) = F_f(sum_q tau_0(a_q) eta_q)
              = sum_q tau_0(a_q) eta_{q^{-1}}
              = sum_q tau_0(a_{q^{-1}}) eta_q   (Umindizierung)
              = Psi_f(Ja)
```

wobei die Grad-Inversion J definiert ist durch:
```
(Ja)_q := a_{q^{-1}}
```

```
==>  F_f(Psi_f(a)) = Psi_f(Ja)
```

Hinweis: J muss kein voller Automorphismus von A_2D^r sein;
es genuegt, dass die Gleichung nach radialer Projektion gilt.

---

## 7. Kriterium (iv): Rohspur-Kompatibilitaet  ✓ [M] unter tau_0(1)=1

Rohspur Z_X(s) ~ zeta(s) aus A_2D^r:
```
Z_X(s) = sum_{n >= 1} tau_0(1) n^{-s}  ~  zeta(s)   (falls tau_0(1) = 1)
```

Adel. Standardvektor eta_1 = 1_Zhat liefert:
```
Z_f(Psi_f(1); s) = sum_{n >= 1} n^{-s} = zeta(s)
```

```
==>  Z_X(s) ~ Z_f(Psi_f(1); s)   unter tau_0(1) = 1.
```

---

## 8. Was Psi_f nicht ist  ✓ [M]

```
+-------------------------------------------------------------+
| Psi_f ist kein Algebra-Homomorphismus.                      |
|                                                             |
| A_2D^r hat Koeffizientenstruktur + Kreuzproduktstruktur;   |
| R_{f,r} speichert nur den radialen Gradanteil.             |
|                                                             |
| Kern(Psi_f) = { a : tau_0(a_q) = 0 fuer alle q }          |
| ist gross (vergisst Koeffizientenstruktur).                  |
+-------------------------------------------------------------+
```

Psi_f ist ein **Schattenmorphismus**, keine Einbettung.

---

## 9. Kriteriencheckliste

| Kriterium | Ergebnis |
|-----------|----------|
| (i) Gradtreue | ✓ [M] |
| (ii) Gewichtstreue | ✓ [M] |
| (iii) Fourier-Kompatibilitaet | ✓ [M] (auf radialem Schatten) |
| (iv) Rohspur-Kompatibilitaet | ✓ [M] (unter tau_0(1) = 1) |

---

## Endbefund  ✓ [M]

```
+-------------------------------------------------------------+
| Psi_f(a) = sum_q tau_0(a_q) eta_q                           |
|                                                             |
| ist die kanonische radiale Projektion von A_2D^r            |
| auf den radialen Schwartz-Bruhat-Schatten R_{f,r}.         |
|                                                             |
| A_2D^r besitzt damit eine kanonische radiale Projektion auf |
| R_{f,r}  ⊂  S(A_f).                                         |
+-------------------------------------------------------------+
```

Pfad ist jetzt praezisiert:
```
A_2D^r  --Psi_f-->  R_{f,r}  --(Einbettung)-->  S(A_f)
```

---

## Abhaengigkeit von tau_0

```
+-------------------------------------------------------------+
| Psi_f ist kanonisch, sobald tau_0 gewaehlt ist.             |
|                                                             |
| Pruefffrage: Ist tau_0 kanonisch in A_2D^r?                 |
|   Falls ja:  Psi_f ist intern.                             |
|   Falls nein: Schattenmorphismus haengt an externer Wahl.   |
+-------------------------------------------------------------+
```

---

## Naechster Schritt: X-P1.3b.0.9  ✗ [H]

```
+-------------------------------------------------------------+
| Kanonizitaet des Grundfunktionals tau_0 in A_2D^r.          |
|                                                             |
| Kandidaten:                                                 |
| (a) KMS-Zustand bei beta = inf (Grundzustand)              |
| (b) traciales Grundfunktional der BC-Diagonale             |
| (c) Eindeutigkeit aus Spektralinvarianz (OP-1)              |
+-------------------------------------------------------------+
```

**Status: ✗ [H] -- naechste Frage.**
