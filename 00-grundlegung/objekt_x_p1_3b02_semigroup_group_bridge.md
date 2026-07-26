# X-P1.3b.0.2 — Semigroup/Group-Bridge der Charakterspur

> Angelegt: 17. Juni 2026
> Wie gelangt man von der N^x-Rohspur zur Q_+^x-Trace-/Absorptionsseite?
> Epistemischer Status: ✓ [M] fuer Beurling-Befund; ◇ [EXT/INT] fuer KMS-/Connes-Interpretation.

---

## Ausgangslage (aus X-P1.3b.0.1  ✓ [M])

```
C_{r,s} < inf  <=>  Re(s) = 0   auf Q_+^x
Z_X(s) ~ zeta(s)                 auf N^x,  Re(s) > 1
```

Offene Frage:
```
Wie gelangt man von der N^x-Rohspur zur Q_+^x-Trace-/Absorptionsseite?
```

---

## Statuskorrektur gegenueber X-P1.3b.0.1

- Beurling-Wachstumstest: **✓ [M]** (elementare Rechnung, intern)
- "Spiegelt exakt KMS-Phasenstruktur": **◇ [EXT/INT]**
  (inhaltlich plausibel; benutzt externe BC-Theorie; interner Vergleichsmorphismus
   noch nicht gebaut)
- Connes' Lesart der expliziten Formel als Trace-Formel auf Adele-Klassenraum:
  **◇ [EXT]** (Connes 1999)

---

## 1. Die Brücke ist kein Konvergenzschritt  ✓ [M]

Die Beurling-Rechnung zeigt: Die meromorphe Fortsetzung
```
Re(s) > 1  -->  C
```
ist *nicht* durch die A_2D^r-Norm allein erklaert. Die Norm kontrolliert
nur Re(s) > 1 (N^x-Seite) und Re(s) = 0 (Q_+^x-Seite).

Die Fortsetzung ist ein zusaetzlicher **Renormalisierungs- und Completion-Schritt**,
der die semigruppale Dirichlet-Spur in ein gruppales Randwert-/Trace-Datum verwandelt.

---

## 2. Brückendiagramm  ✓ [M] (Struktur); ✗ [H] (interne Konstruktion)

```
       N^x
        |
        v
  Z_X(s) ~ zeta(s)          Re(s) > 1      [X-P1.3b.1]
        |
    -d/ds log
        |
        v
  Theta_X ~ -zeta'/zeta(s)   Re(s) > 1      [X-P1.3b.2]
        |
   xi-Completion
   (Renormalisierung)
        |
        v
  -xi'(s)/xi(s)              meromorph auf C [X-P1.3b.3]
        |
    s = 1/2 + it
        |
        v
  Q_+^x-unitaere Trace-/Absorptionsseite    [X-P1.3b.4]
```

**Pole von -xi'/xi = nichttriviale Nullstellen.**

---

## 3. Die Funktionalgleichung als Symmetrisierer  ✗ [H] (intern zu formulieren)

Die Funktionalgleichung von xi:
```
xi(s) = xi(1-s)
```
wird nach Zentrierung s = 1/2 + z zur Symmetrie:
```
Xi(z) := xi(1/2 + z)   ==>   Xi(z) = Xi(-z)
```
Diese Symmetrie entspricht strukturell der Inversion
```
q  <-->  q^{-1}   auf Q_+^x.
```

Der **wichtigste neue Satz** dieses Blattes:
```
+-------------------------------------------------------------+
| Die Funktionalgleichung ist die algebraische Sichtbarkeit   |
| der Inversion q <-> q^{-1} auf Q_+^x.                      |
+-------------------------------------------------------------+
```

Folgerung:
```
N^x erzeugt zeta (einseitig, positiv),
Q_+^x traegt die symmetrisierte Trace-Formel (zweiseitig, unitaer).
```

**Status: ✗ [H] — intern noch nicht als Algebramorphismus gebaut.**

---

## 4. Unitaere Trace-Seite  ◇ [EXT/INT]

Auf der unitaeren Achse s = 1/2 + it entsteht:
```
Theta_X^xi(t) := -Xi_X'(it) / Xi_X(it)
```
Formal: ein Charakterdatum auf dem Dualen von Q_+^x mit Charakteren q^{-it}.
Nullstellen erscheinen als Pole/Resonanzen der logarithmischen Charakterspur.

**Status: ◇ [EXT/INT] — Connes-/Meyer-Analogie; interne Realisierung offen.**

---

## 5. Primseitige Symmetrisierung  ✗ [H]

Die Dirichlet-Reihe
```
sum_{n >= 1} Lambda(n) n^{-s}   (Re(s) > 1)
```
lebt zunaechst auf N^x. Nach xi-Completion und Funktionalgleichung wird sie
symmetrisiert: Beitraege bei log n *und* -log n, also:
```
N^x  subset  Q_+^x   zusammen mit n <-> n^{-1}
```
Das ist die logarithmische Einbettung N^x -> Q_+^x, symmetrisiert durch die
Funktionalgleichung.

**Status: ✗ [H] — intern zu konstruieren in X-P1.3b.0.3.**

---

## 6. Rollenverteilung (Zusammenfassung)

```
+---------------------------------------------------------------+
| N^x   = Rohspur-Seite                                        |
|         Z_X(s) ~ zeta(s),  Re(s) > 1                        |
|                                                               |
| Q_+^x = unitaere Spurformel-Seite                            |
|         q^{-it},  Absorptionsspektrum, Nullstellen als Pole  |
|                                                               |
| Brücke = meromorphe Fortsetzung + xi-Completion              |
|         + Funktionalgleichung (= Symmetrisierer)             |
+---------------------------------------------------------------+
```

---

## Naechster Schritt: X-P1.3b.0.3  ✗ [H]

```
+-------------------------------------------------------------+
| Konstruiere die xi-Completion intern als Symmetrisierer     |
| der Beurling-Charakterspur:                                 |
|                                                             |
| Z_X(s)  auf  N^x   (Beurling, konvergent Re(s) > 1)        |
|   |                                                         |
|  xi-Sym                                                     |
|   |                                                         |
| xi_X(s) auf Q_+^x  (symmetrisch, Xi(z) = Xi(-z))           |
+-------------------------------------------------------------+
```

Frage: Welcher interne Schritt auf A_2D^r entspricht dem Gamma-Faktor
pi^{-s/2} Gamma(s/2) in der xi-Vervollstaendigung?

Diese Frage beruehrt den archimedischen Faktor -- und damit moeglicherweise
die einzige Stelle, wo A_2D^r (das nur endliche Stellen sieht) an seine
Grenzen stoesst und eine externe archimedische Ergaenzung braucht.

**Status: ✗ [H] — naechste Frage.**
