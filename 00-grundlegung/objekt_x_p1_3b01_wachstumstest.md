# X-P1.3b.0.1 — Wachstumstest für die Beurling-Charakterspur

> Angelegt: 17. Juni 2026
> Explizite Berechnung von C_{r,s} = sup_q |q^{-s}| / w_r(q) aus OP-1.6f-Gewicht.
> Ergebnis: Spaltung N^x (Dirichlet/Rohspur) vs Q_+^x (unitaer/Trace).
> Epistemischer Status: ✓ [M] (Rechnung elementar, direkt verifizierbar).

---

## Setup

```
q = prod_p p^{a_p}  in Q_+^x,   a_p in Z,  fast alle = 0
l(q) = sum_p |a_p| log p          (OP-1.6f.2 Wortlaenge)
w_r(q) = (1 + l(q))^r             (Beurling-Gewicht)
s = sigma + it,  C_{r,s} = sup_{q in Q_+^x}  |q^{-s}| / w_r(q)
```

Frage: Wann ist C_{r,s} < infty?

---

## Rechnung: Zwei Richtungen entlang einer Primzahl p

### Positive Richtung: q = p^k, k -> infty

```
l(p^k) = k log p
|q^{-s}| = p^{-k*sigma}

C_{r,s} >= p^{-k*sigma} / (1 + k log p)^r
```

Falls sigma < 0: Zaehler p^{k|sigma|} waechst exponentiell, Nenner polynomial.
```
==> C_{r,s} = infty   falls sigma < 0.
```

### Negative Richtung: q = p^{-k}, k -> infty

```
l(p^{-k}) = k log p
|q^{-s}| = |(p^{-k})^{-s}| = p^{k*sigma}

C_{r,s} >= p^{k*sigma} / (1 + k log p)^r
```

Falls sigma > 0: Zaehler p^{k*sigma} waechst exponentiell, Nenner polynomial.
```
==> C_{r,s} = infty   falls sigma > 0.
```

### Verbleibender Fall: sigma = 0

```
|q^{-it}| = 1   fuer alle q in Q_+^x

C_{r,it} = sup_q 1 / (1 + l(q))^r = 1   (fuer r >= 0)
```

---

## Ergebnis  ✓ [M]

```
┌────────────────────────────────────────────────────────────┐
│  C_{r,s} < infty   <=>   Re(s) = 0   (r >= 0)              │
│                                                             │
│  Die Beurling-Charakterspur auf Q_+^x mit polynomialem      │
│  Gewicht w_r ist nur auf der unitaeren Achse Re(s) = 0      │
│  automatisch stetig. Es gibt keine rechte Halbebene.        └────────────────────────────────────────────────────────────┘
```

**Ursache:** Q_+^x ist zweiseitig. Fuer sigma != 0 explodiert immer
eine der beiden Richtungen (q->infty oder q->0) exponentiell.
Polynomiales Beurling-Gewicht kann exponentielles Wachstum nicht kontrollieren.

---

## Semigruppen-Korrektur: Einschraenkung auf N^x

Auf der positiven Semigruppe N^x = {1, 2, 3, ...} entfaellt die negative Richtung.

```
n in N^x:   l(n) = log n,   n^{-sigma} / (1 + log n)^r
```

Beschraenkt gdw. sigma >= 0. Fuer den Waermekern:
```
K_s = sum_{n >= 1} n^{-s} U_n

sum_{n >= 1} |n^{-s}| / w_r(n) = sum_{n >= 1} n^{-sigma} / (1 + log n)^r
```

Konvergiert (fuer r >= 0) genau fuer Re(s) > 1.

Daher:
```
Ch_{X,r}(K_s; 0) = sum_{n >= 1} n^{-s}  ~  zeta(s),   Re(s) > 1.
```

Die Zeta-Rohspur ist N^x-seitig, nicht Q_+^x-seitig.

---

## Strukturelle Spaltung  ✓ [M]

```
┌────────────────────────────────────────────────────────────┐
│  N^x   = thermodynamische / Dirichlet-Seite                 │
│         BC-Partitionsfunktion Z_X(s) ~ zeta(s)              │
│         Konvergenz in Re(s) > 1                             │
│                                                             │
│  Q_+^x = Fourier- / Trace- / Absorptionsseite               │
│         unitaere Charaktere q^{-it}                         │
│         Connes-Spurformel / adel. Trace                     │
└────────────────────────────────────────────────────────────┘
```

Diese Spaltung ist kein Fehler im Programm, sondern eine strukturelle Beobachtung:
Sie spiegelt genau die bekannte Zweiteilung im BC-System wider:
- KMS-Zustände bei beta > 1: N^x-Seite, Dirichlet-Reihe, Partition zeta(beta)
- beta = 1 (Phasenuebergang): symmetrisierte Struktur, Q_+^x-Seite tritt hervor
- Spurformel/Absorptionsspektrum: Q_+^x-Seite, unitaere Charaktere

---

## Verbindung zu X-Axiomen

| Axiom | Rolle | Seite |
|-------|-------|-------|
| A2: Q_+^x-Graduierung | Gesamttraeger von X | beide |
| A3: Spektrum / H_X | Rohspur Z_X ~ zeta | N^x-Seite |
| A3: dlog-Spur Theta_X | Symmetrisierung -xi'/xi | Q_+^x-Seite |
| A4: Quasikristall | unitaere Charakterseite | Q_+^x-Seite |

---

## Naechster Schritt: X-P1.3b.0.2  ✗ [H]

```
┌────────────────────────────────────────────────────────────┐
│  Semigroup/Group-Splitting der Charakterspur:               │
│                                                             │
│  Formalisiere, wie Z_X(s) aus N^x entsteht und             │
│  wie die meromorphe Fortsetzung / dlog-Spur                 │
│  die Bruecke zur Q_+^x-Seite schlaegt.                      │
└────────────────────────────────────────────────────────────┘
```

Die Bruecke ist die meromorphe Fortsetzung von zeta(s) ueber Re(s) > 1 hinaus:
Dort, wo die N^x-Rohspur divergiert, lebt das Nullstellen-Spektrum.
Die Q_+^x-Seite (unitaere Charaktere) liefert dann den Rahmen fuer
die Spurformel / Absorptionsstruktur der Nullstellen.

**Status: ✗ [H] — naechster Schritt.**
