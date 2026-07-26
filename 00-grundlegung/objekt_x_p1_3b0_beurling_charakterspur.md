# X-P1.3b.0 — Beurling-gewichtete Charakterspur

> Angelegt: 17. Juni 2026
> Vorfrage zu X-P1.3b.1: Welche Spur ist auf A_2D^r überhaupt wohldefiniert?
> Epistemischer Status: ✗ [H] soweit nicht anders markiert.

---

## Warum nicht Wodzicki oder Nuklearspur zuerst

- **Wodzicki-Residuum:** Verlangt sofort einen Pseudodifferentialkalkül mit Symbolkalkül.
  Für A_2D^r noch nicht vorhanden. Zu früh.
- **Nuklearspur:** Trace-Eindeutigkeit in lokalkonvexen/nuklearen Räumen verlangt
  zusätzliche Approximationseigenschaften; folgt nicht automatisch aus "Fréchet/nuklear".
- **Beurling-Charakterspur:** Schließt direkt an OP-1.6f an; braucht keinen externen
  Apparat; liefert sofort eine wohldefinierte Mellin-Halbn-Spur in einer rechten Halbebene.

---

## 1. Aufbau

Ein homogen zerlegtes Element von A_2D^r:
```
a = sum_{q in Q_+x} a_q U_q
```
wobei a_q im Koeffizientenraum liegt und U_q den Q_+x-Grad traegt.

Das Beurling-Gewicht w_r (aus OP-1.6f.2) liefert eine Halbnorm:
```
|a|_{r,w} = sum_{q in Q_+x} |a_q|_{2D} * w_r(q)
```

## 2. Beurling-Mellin-Charakterspur

Sei tau_0 ein kontinuierliches Grundfunktional auf dem Koeffizientenraum
(z.B. diagonale Erwartung, BC-KMS-Grundfunktional, Integration).

Formal:
```
Ch_{X,r}(a; s) := sum_{q in Q_+x} tau_0(a_q) * q^{-s}
```
Dies ist die **Beurling-gewichtete Mellin-Charakterspur**.

---

## 3. Wohldefiniertheit  ✗ [H]

Das Funktional ist stetig auf A_2D^r, sobald:
```
C_{r,s} := sup_{q in Q_+x}  |q^{-s}| / w_r(q)  < infinity
```
Denn dann:
```
|Ch_{X,r}(a; s)|  <=  |tau_0| * C_{r,s} * |a|_{r,w}
```

Erster technischer Befund:
```
┌────────────────────────────────────────────────────────────┐
│  Ch_{X,r}(.; s) ist in der durch C_{r,s} < inf bestimmten  │
│  Halbebene Omega_r wohldefiniert und stetig.               │
└────────────────────────────────────────────────────────────┘
```

**Status: ✗ [H] — zu verifizieren durch explizite Berechnung von Omega_r** (nächste Mini-Aufgabe).

---

## 4. Einschränkung: keine echte Spur  ✓ [M] (als Feststellung)

Für homogene Elemente a = f U_q, b = g U_p gilt:
```
ab = f * alpha_q(g) * U_{qp}
ba = g * alpha_p(f) * U_{pq} = U_{qp}  (da Q_+x abelsch)
```naber die Koeffizienten sind im Allgemeinen verschieden:
```
tau_0(f * alpha_q(g))  !=  tau_0(g * alpha_p(f))
```
Also:
```
┌────────────────────────────────────────────────────────────┐
│  Ch_{X,r} ist zunaechst nur Charakterspur/Halbspur,        │
│  keine volle Tracialitaet.                                 │
└────────────────────────────────────────────────────────────┘
```

Das ist für X-P1.3b akzeptabel: Typ 3 sucht ein Trace-/Charakter-Datum,
kein tracial state im C*-Sinne. Tracialität kann später auf einer
Unteralgebra, Diagonale, BC-Corner oder KMS-Twist geprüft werden.

---

## 5. Verbindung zur Rohspur

Formaler Wärmekern / Skalenträger:
```
K_s = sum_{n >= 1} n^{-s} U_n     (n in N^x subset Q_+x)
```
Beurling-Charakterspur liefert:
```
Z_X(s) := Ch_{X,r}(K_s; 0)
        = sum_{n >= 1} tau_0(1) * n^{-s}
        ~ zeta(s)     (falls tau_0(1) = 1, in Omega_r)
```
Das ist X-P1.3b.1 — vorbereitet.

---

## 6. Primitive Spur / dlog-Spur

Aus der Rohspur:
```
Theta_X(s) := -d/ds log Z_X(s)
            ~ -zeta'(s)/zeta(s)
            = sum_{n >= 1} Lambda(n) n^{-s}
```
Die Primrichtungen entstehen nicht durch Zusatzhypothese, sondern als
logarithmische Ableitung der Beurling-Rohspur. Das verbindet direkt
mit der Sieb-Interpretation aus stufen_0_VI:
```
Sieb streicht Vielfache  <-->  Lambda zaehlt, wie oft gestrichen wurde
                               (gewichtet mit log p)
```

---

## 7. Zusammenfassung: Was Beurling-Kandidatur liefert

```
┌────────────────────────────────────────────────────────────┐
│  LIEFERT:                                                   │
│  - wohldefiniertes Mellin-Charakterfunktional in Omega_r   │
│  - natürlichen Weg Z_X ~ zeta --> Theta_X ~ -zeta'/zeta    │
│  - direkten Anschluss an OP-1.6f (kein neuer Apparat)     │
│  - Verbindung zur Sieb-Interpretation (stufen_0_VI)        │
│                                                             │
│  NOCH NICHT:                                               │
│  - echte Spur auf vollem Kreuzprodukt                      │
│  - archimedisch vervollständigte xi-Korrektur              │
│  - Nullstellen als Pole (das ist X-P1.3b.4)                │
└────────────────────────────────────────────────────────────┘
```

---

## 8. Nächste Mini-Aufgabe (X-P1.3b.0.1)  ✗ [H]

```
┌────────────────────────────────────────────────────────────┐
│  Bestimme die Konvergenzhalbebene Omega_r von               │
│  Ch_{X,r}(a; s) explizit aus dem OP-1.6f-Gewicht w_r.      │
│                                                             │
│  Konkret: Wann ist                                         │
│  C_{r,s} = sup_q  |q^{-s}| / w_r(q)  < infinity?          │
└────────────────────────────────────────────────────────────┘
```

Die Antwort hängt von der genauen Form von w_r ab (OP-1.6f.2: w_r(q) = (1 + l(q))^r,
wobei l(q) = sum_p |a_p| log p die Wortlänge ist).

Konvergenz von C_{r,s} bedeutet: |q^{-s}| / (1 + l(q))^r ist gleichmaessig beschraenkt,
d.h. q^{-Re(s)} waechst langsamer als (1 + l(q))^r.

Einzelschritte:
1. Parametrisiere q = prod_p p^{a_p} in Q_+x, a_p in Z, fast alle = 0.
2. Berechne |q^{-s}| = q^{-Re(s)} = prod_p p^{-a_p Re(s)}.
3. Berechne l(q) = sum_p |a_p| log p.
4. Frage: Wachstumsvergleich von q^{-Re(s)} vs (1 + l(q))^r.

**Status: ✗ [H] — explizite Berechnung steht aus.**
