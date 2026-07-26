# NEU-73 — Vergleich der Theta-Matrix mit der BC-Derivation

**Status:** J_N^- = sum_n log(n) V_n R gesichert ✓/⚠[M]; [R,V_n]=nV_n (nicht r) ✓[M]; V_n~mu_n offen ❓[O]
**Datum:** 2026-06-30 (Korrektur: Operatorordnung; Quelle-r vs. Ziel-r; J_N^- = V_n R, nicht R_n V_n)
**Aufbaut auf:** NEU-72 (Theta ~ r log n; Faktorisierung [r] x [log n] kompatibel mit BC)

---

## Hauptergebnis ✓/⚠[M]

```
J_N^- = sum_{n in S_N} (log n) V_n R
```

wobei:
```
V_n eta_{(p,m,r,u)} = eta_{(p',m,r+n,u')}    [Verschiebungsoperator, Schritt +n]
R   eta_{(p,m,r,u)} = r * eta_{(p,m,r,u)}    [r-Multiplikation am Quellknoten]
```

Dann:
```
(J_N^- eta)_b = sum_n (log n) (V_n R eta)_b
             = sum_{n: T_n(a)=b} (log n) r(a) eta_a
             = Theta_{ba} eta_a
```

mit Theta_{ba} = r(a) log n.  Dies trifft exakt die gesicherte Matrixstruktur. ✓[M]

---

## Operatorordnungs-Korrektur: V_n R, nicht R_n V_n ✓[M]

**Falscher Ansatz (NEU-73 urspruenglich):**
```
J_N^- = sum_n (log n) R_n V_n    [Reihenfolge falsch]
```

**Warum falsch:** Bei R V_n eta_r = R eta_{r+n} = (r+n) eta_{r+n} entsteht
der **Zielfaktor** r+n, nicht der Quellfaktor r.

Korrekte Reihenfolge:
```
V_n R eta_r = V_n (r eta_r) = r eta_{r+n}    [Quellfaktor r]
```

Daher:
```
J_N^- = sum_n (log n) V_n R     [Quellfaktor r = r(a) korrekt]  ✓[M]
```

Alternative Schreibweise:
```
R_{src,n} := V_n R V_n^*  (auf dem Zielbild)
=> (log n) R_{src,n} V_n = (log n) V_n R    [aequivalent]
```

---

## Kommutatorrechnung: [R, V_n] = n V_n, nicht r V_n ✓[M]

```
[R, V_n] eta_r = R eta_{r+n} - V_n(r eta_r)
              = (r+n) eta_{r+n} - r eta_{r+n}
              = n V_n eta_r
=> [R, V_n] = n V_n    [Faktor n, NICHT r]
```

Daher ist Theta_{ba} ~ r log n **kein** direkter Kommutator [partial, H].
Die Faktorisierung ist:
```
Theta_{ba} = r(a) * log n  =  [Quell-r-Gewicht] x [BC-Zeitgewicht]
           aus:  J_N^- = sum_n (log n) V_n R
```

---

## Additive-Multiplikative Doppelstruktur: sauber sichtbar ✓/⚠[M]

```
J_N^- = sum_n (log n) V_n R
          ^             ^  ^
          |             |  |
     BC-Zeitgewicht     |  r-Multiplikation (Fourier-/Kreisseite)
                        |
                   Verschiebungsoperator (Transport)
```

- **r**: Quell-Fouriergewicht, Kreis-/Charakterseite
- **log n**: BC-Zeitgewicht, multiplikative Primseite
- **V_n**: Transport zwischen beiden Sektoren

Das ist eine **konkrete Operatorfaktorisierung**, nicht nur Kompatibilitaet. ✓/⚠[M]

---

## Offener Kern: Ist V_n ~ mu_n? ❓[O] -> NEU-74

In der BC-Algebra gilt:
```
mu_n e_k = e_{nk}    [multiplikativer Index-Shift]
sigma_t(mu_n) = n^{it} mu_n
delta_BC(mu_n) = [H, mu_n] = log(n) mu_n
```

Der Divisorgraph-Operator:
```
V_n eta_{(p,m,r,u)} = eta_{(p',m,r+n,u')}    [additiver r-Shift]
```

**Unterschied:** mu_n shiftet multiplikativ (k -> nk), V_n shiftet additiv (r -> r+n).

Aber: Unter der Exponential-Abbildung r |-> e(r) = exp(2 pi i r) gilt:
```
e(r) |-> e(r+n) = e(r) * e(n)    [multiplikative Phase]
```

D.h. auf dem Kreis/Torus entspricht der additive Shift r -> r+n dem
multiplikativen Shift e(r) -> e(n) * e(r) -- was einer Rotations-/
Phasenverschiebung entspricht, nicht dem BC-Skalierungsshift k -> nk. ⚠[M]

Die Identifikation V_n ~ mu_n erfordert daher entweder:
1. Eine andere Koordinatisierung (nicht r auf Z, sondern r auf Torus/Adeles)
2. Oder eine Feshbach-Projektion, die V_n auf den mu_n-Sektor reduziert

Status: ❓[O] -> NEU-74

---

## Status NEU-73

| Objekt | Status |
|---|---|
| J_N^- = sum_n (log n) V_n R | ✓[M] |
| Theta_{ba} = r(a) log n aus V_n R | ✓[M] |
| [R, V_n] = n V_n (nicht r V_n) | ✓[M] |
| Theta != [partial, H] (kein einfacher Kommutator) | ✓[M] |
| r = Fourier-/Quellgewicht; log n = BC-Zeitgewicht | ✓/⚠[M] |
| V_n ~ mu_n (BC-Isometrie) | ❓[O] -> NEU-74 |

---

## Literatur

- Bost & Connes: Selecta Math. 1 (1995) (mu_n, e(r), sigma_t, delta_BC)
- Connes & Marcolli: AMS 2008, Kap. 3 (Operatorordnung in BC-Algebra)
- Jacobi-Operatoren: Simon, B.: *Szego Theorem*, Princeton 2011 (V_n R vs R V_n)
