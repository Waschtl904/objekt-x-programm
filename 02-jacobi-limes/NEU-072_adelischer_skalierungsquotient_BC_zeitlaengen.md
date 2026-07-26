# NEU-72 — Adélischer Skalierungsquotient und BC-Zeitlängen

**Status:** BC-Rahmen ✓[M]; Theta ~ BC-Derivation kompatibel ⚠[M]; A_N ~ U_t ✗[M]
**Datum:** 2026-06-30 (Korrektur: BC != gamma_N-Renormierung; A_N ~ Derivation, nicht U_t; Orbits adel. vorsichtig)
**Aufbaut auf:** NEU-71 (multiplikativ-adélischer Quotient nötig; Frobenius mod m unzureichend)

---

## Leitfrage

```
Ist der additive Divisorgraph nur die Jacobi-/Feshbach-Darstellung
einer multiplikativen BC-Derivation?
```

Brücke:
```
Theta_{ba} ~ r log n  <=?>  delta_BC(mu_n) = log(n) mu_n
```

---

## Korrektur 1: BC-Zeit ist kein gamma_N ✓[M]

**Frühere Formulierung (unpräzise):**
```
"BC-Zeit = nicht-skalare Renormierung gamma_N(n)"
```

**Korrektur:**

Die BC-Zeitentwicklung sigma_t(mu_n) = n^{it} mu_n liefert den Generator
```
H mu_n = (log n) mu_n    [intrinsischer Hamiltonian]
```

Das ist keine cutoff-abhängige Renormierung wie gamma_N. Es ist eine
**feste logarithmische Zeitentwicklung**.

Kohärenz mit NEU-58:
```
NEU-58: kein skalares gamma_N kann Divisorgeometrie uniform bändigen.
NEU-72: der richtige Maßstab ist nicht skalar, sondern im BC-Hamilton
        H = log n intrinsisch kodiert.
```

Das ist kohärent, aber keine Renormierung im engen Sinn. ✓[M]

---

## Korrektur 2: A_N^{Jac,-} ~ BC-Derivation, nicht U_t ✓[M]

**Szenario I (revidiert als falsch):** A_N^{Jac,-} ~ U_t = e^{itH}

U_t ist **unitär**, A_N^{Jac,-} ist **selbstadjungiert/off-diagonal**.
Die Identifikation mit U_t selbst ist strukturell unzutreffend. ✗[M]

**Korrekte Analogie:**
```
A_N^{Jac,-}  ~  Jacobi-/Feshbach-Realisierung der BC-Derivation:
delta_BC(mu_n) = [H, mu_n] = (log n) mu_n
```

oder einer kommutatoriellen Variante:
```
[partial, V_n] e_r = r * (Transport)      [Fourier-/r-Faktor]
[H, V_n] e_r      = (log n) * (Transport) [BC-Zeitfaktor]
```

Der Matrixeintrag:
```
Theta_{ba} ~ r log n = [r-Faktor] * [log n-Faktor]
```

kann als Produkt zweier Kommutator-/Derivationsbeiträge gelesen werden. ⚠[M]

**Präzisierter offener Punkt (-> NEU-73):**
```
A_N^{Jac,-}  =?  Feshbach-/Jacobi-Modell der BC-Derivation auf relativem Testsektor
```

---

## Korrektur 3: Adélische Orbits vorsichtig formulieren ✓[M]

**Frühere Formulierung:**
```
"x |-> p^k x auf A_Q/Q^* liefert geschlossene Bahnen wie endlicher Graph"
```

**Korrektur:**

Primzahlen erscheinen im adélischen Klassenraum als **Skalierungs-/Modul-Orbits
der Idelklassenaktion**, deren Zeitgewicht log p in der Spurformel auftaucht.

Das ist keine endliche Frobenius-Periodizität und keine additive Graphperiode.
Formale "primitive Orbits" auf A_Q/Q^* sind keine endlichen Graphzyklen,
sondern Fixpunkt-/Orbitdaten des Moduloperators. ✓[M]

**Korrekte Aussage:**
```
|p|_adel = p^{-1}  =>  Zeitgewicht log p in Connes-Spurformel  [Weil-explizite Formel]
```

---

## Hauptbefund NEU-72 ⚠[M]

```
Die Matrixgewichte Theta_{ba} ~ r log n sind kompatibel mit der
BC-Derivation delta_BC(mu_n) = log(n) mu_n.
```

**Faktorisierung:**
```
r log n  =  [Fourier-/Kreisfaktor r]  x  [BC-Zeitfaktor log n]
```

- r kommt von der Kreis-/Fourierseite (Charakter e(r) = exp(2 pi i r) in BC)
- log n kommt von der BC-/Primseite (Hamilton H = log n)

Das ist die additive-multiplikative Doppelstruktur in A_N^{Jac,-}. ⚠[M]

---

## BC-System: Rahmen ✓[M]

```
A_Q = C*(Z_hat ⋊ N^x)
sigma_t(mu_n) = n^{it} mu_n
sigma_t(e(r)) = e(r)              [e(r) = exp(2pi i r)]

Generator: H mu_n = (log n) mu_n
Zustandssumme: Z_BC(beta) = Tr(e^{-beta H}) = zeta(beta)  [beta > 1]
```

Charaktere:
```
e(r) mu_n = mu_n e(rn)    [Verschiebung von r um Faktor n]
```

Das entspricht genau der Divisorstruktur:
```
V_n e_r = e_{r+n}   (additiver Schritt)  <-->  e(r) mu_n = mu_n e(rn)  (multip. Skalierung)
```

Die Verbindung additiv (r+n) <-> multiplikativ (rn mod 1) ist die
**Exponentialisierung**: r |-> e(r) = exp(2 pi i r). ⚠[M]

---

## Szenarien (revidiert)

| Szenario | Mechanismus | Status |
|---|---|
| I: A_N ~ U_t | unitär vs. s.a. | ✗[M] |
| II: A_N ~ BC-Derivation delta_BC | Theta ~ r log n kompatibel | ⚠[M] -> NEU-73 |
| III: Multiplikative Koordinate auf I_N | neue Koordinatisierung | ❓[O] |
| Additiv->Multiplikativ via e(r) | Exp.-Abbildung r |-> e(r) | ⚠[M] |

---

## Status NEU-72

| Objekt | Status |
|---|---|
| BC-Zeit H = log n (kein gamma_N) | ✓[M] |
| A_N ~ U_t | ✗[M] |
| A_N ~ BC-Derivation delta_BC | ⚠[M] (kompatibel, nicht bewiesen) |
| Theta_{ba} = r log n = [r] x [log n] Faktorisierung | ⚠[M] |
| Additiv r+n <-> Multiplikativ e(rn) via Exp. | ⚠[M] |
| Adélische Orbits: Modul-/Zeitgewicht log p | ✓[M] |

---

## Literatur

- Bost, J.-B. & Connes, A.: Selecta Math. 1 (1995) (BC-System, e(r), mu_n, sigma_t)
- Connes, A. & Marcolli, M.: *Noncommutative Geometry, Quantum Fields and Motives*,
  AMS 2008, Kap. 3 (Derivation delta_BC, explizite Formel)
- Connes, A.: Selecta Math. 5 (1999) (Spurformel, Idelklassenaktion, |p|_adel)
- Laca, M. & Raeburn, I.: J. London Math. Soc. 59 (1999) (Z_hat ⋊ N^x)
