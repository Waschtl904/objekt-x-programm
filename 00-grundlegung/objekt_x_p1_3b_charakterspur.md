# X-P1.3b — Kanonische Charakterspur und dlog-Spur

> Angelegt: 17. Juni 2026
> Einstieg in Typ-3-Spektralrealisierung (Meyer/Fréchet).
> Epistemischer Status: ✗ [H] soweit nicht anders markiert.

---

## Ausgangspunkt

Nach X-P1.3a ist Typ 3 (Meyer/Fréchet/Trace) der natürliche Einstieg.
Die naive Rohfrage
```
s  |-->  Tr_X(a^{-s})
```
ist jedoch zu früh:
- In einer Fréchet-Algebra ist a^{-s} nicht automatisch definiert.
- Eine Spurklasse ist nicht automatisch gegeben.
- Die Rohspur liefert zuerst zeta(s), *nicht* die Nullstellen.

Der entscheidende Schritt:
```
Tr(e^{-sD})       ~>  zeta(s)          [Rohspur, Nullstellen nicht sichtbar]
-d/ds log Tr(...)  ~>  -zeta'(s)/zeta(s)  [Primitivspur, Pole = Nullstellen]
```

---

## Korrigierte Leitfrage  ✗ [H]

```
┌────────────────────────────────────────────────────────────┐
│  Hat A_2D^r genügend Beurling-/Fréchet-Struktur,             │
│  um -zeta'/zeta oder -xi'/xi als kanonische                 │
│  Charakterspur des Q_+×-Flusses zu tragen?                  │
└────────────────────────────────────────────────────────────┘
```

**Nicht:** Hat A_2D^r schon die Nullstellen?
**Sondern:** Kann A_2D^r intern eine primitive dlog-Spur erzeugen?

---

## Minimales Modell

**Längengenerator:**
```
D_X u_n = (log n) u_n
```
Der Operator D_X erzeugt den Q_+×-Skalenfluss in der reduzierten Normalform;
die Q_+×-Graduierung aus A2 (Minimalaxiome) ist genau die Eigenraumzerlegung
von D_X.

**Rohspur (Erwartung):**
```
Z_X(s) = Tr_X(e^{-s D_X})
       = sum_{n >= 1} n^{-s}
       ~ zeta(s)     (in einer rechten Halbebene)
```
Die Nullstellen sind in Z_X nicht sichtbar; sie erscheinen erst in:

**Primitivspur / dlog-Spur:**
```
Theta_X(s) = -d/ds log Z_X(s)
           = -zeta'(s)/zeta(s)
           = sum_{n >= 1} Lambda(n) n^{-s}
```
wobei Lambda die von-Mangoldt-Funktion ist.

Die Pole von Theta_X liegen bei:
- s = 1  (Pol der Zeta-Funktion, archimedisch zu korrigieren)
- s = rho  (nichttriviale Nullstellen)
- s = -2k  (triviale Nullstellen, Gamma-Pol-Beiträge)

---

## Archimedische Vervollständigung

Um nur die nichttrivialen Nullstellen zu isolieren, wird die Gamma-Faktor-Korrektur
eingebaut. Die vollständige Zeta-Funktion:
```
xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
```
ist ganz und hat genau die nichttrivialen Nullstellen als Nullstellen.

**Vollständige Charakterspur:**
```
Theta_X^xi(s) = -d/ds log xi_X(s)
```

**Zielvergleich:**
```
Theta_X^xi(s)  ~  -xi'(s)/xi(s)
```
Die Pole von -xi'/xi liegen *genau* bei den nichttrivialen Nullstellen.

Wenn X-P1.3b gelingt, trägt A_2D^r ein Trace-/Distributionsspektrum
der nichttrivialen Nullstellen (Typ-3-Version von A3).

---

## Warum dieser Weg nicht RH voraussetzt

Der Vergleich Theta_X^xi ~ -xi'/xi ist eine meromorphe Strukturaussage,
keine Aussage über die Lage der Pole. RH würde erst später als:
- Positivitätseigenschaft der Charakterspur,
- Selbstadjungiertheit von D_X,
- oder Realitätsbedingung an die Pole
erscheinen.

Bis dahin: Nullstellen als Pole einer distributional trace, RH offen.

---

## Verbindung zur BC-Seite

Im Bost-Connes-System ist die Partitionsfunktion (KMS-Zustand bei beta):
```
Z_BC(beta) = zeta(beta)
```
Das ist genau die Rohspur Z_X mit s = beta. Die BC-Seite liefert also
automatisch den Ausgangspunkt für X-P1.3b.1.

Die Connes-Spurformel auf dem adel. Klassenraum ist dann die Typ-2-Version
desselben Schritts: Dort erscheinen die Nullstellen als Absorptionsspektrum
der Spurformel, und die explizite Formel ist eine Charakterformel auf
dem Q×-Quotientenraum.

Beide Seiten konvergieren auf denselben Schritt:
```
Rohspur Z_X ~ zeta  =>  dlog-Spur Theta_X ~ -zeta'/zeta.
```

---

## Arbeitszerlegung

### X-P1.3b.1 — Rohspur  ✗ [H]

Konstruiere einen Kandidaten-Spurausdruck
```
Z_X(s) = Tr_X(e^{-s D_X})
```
aus der Q_+×-Graduierung von A_2D^r.

Frage: In welchem Sinne ist Tr_X wohldefiniert?
(Nuklear-/Spurklasse-Norm? Beurling-gewichtete Spur? Charakterintegral?)

**Status: ✗ [H]**

### X-P1.3b.2 — Primitivspur  ✗ [H]

```
Theta_X(s) = -d/ds log Z_X(s)
```
Erwartung: Theta_X(s) ~ Lambda-Dirichlet-Reihe.

**Status: ✗ [H]**

### X-P1.3b.3 — Archimedische Vervollständigung  ✗ [H]

Einbau der Gamma-/Pi-Faktoren, Konstruktion von xi_X(s).
Erwartung: -d/ds log xi_X ~ -xi'/xi.

**Status: ✗ [H]**

### X-P1.3b.4 — Nullstellen als Pole  ✗ [H]

Vergleich Theta_X^xi mit -xi'/xi.
Falls übereinstimmend: X trägt Typ-3-Version von A3.

**Status: ✗ [H]**

---

## Gesamtbild: Spurkette

```
Q_+×-Graduierung von X
        |
        v
  Rohspur Z_X(s)  ~  zeta(s)          [X-P1.3b.1]
        |
    dlog |
        v
  Theta_X(s)  ~  -zeta'/zeta(s)       [X-P1.3b.2]
        |
  xi-Korr. |
        v
  Theta_X^xi  ~  -xi'/xi(s)           [X-P1.3b.3]
        |
        v
  Pole = nichttriviale Nullstellen      [X-P1.3b.4]
                                        Typ-3-Version von A3
```

---

## Entscheidende technische Vorfrage (X-P1.3b.0)

Bevor X-P1.3b.1 angreifbar wird:
```
In welchem Sinn ist eine Spur auf A_2D^r wohldefiniert?
```
Kandidaten:
- Wodzicki-Residuum (für DO-artige Algebren)
- Nuklearspur (ℓ^1-Norm der Singularwerte)
- Q_+×-equivariante Charakterspur (Integration über Charaktere)
- Beurling-gewichtete Spur (Verträglich mit OP-1-Normen)

Diese Vorfrage ist der eigentliche erste technische Schritt.

**Status: ✗ [H] — erste Arbeitsfrage in X-P1.3b.**
