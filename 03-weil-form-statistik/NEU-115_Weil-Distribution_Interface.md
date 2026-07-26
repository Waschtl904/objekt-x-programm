# NEU-115 — Weil-Distribution als Interface zwischen Spektralschatten und Objekt X

**Stand: 1. Juli 2026**

---

## Ausgangslage (nach NEU-114)

Nach dem Kursabgleich NEU-114 existieren zwei parallele Spuren:

```
Spur A:  Pi_gamma(X) = m_arith  ->  Q_Weil
Spur B:  X  ->  W_res^top       ->  Q_Weil
```

Der direkte Vergleich

```
W_res^top  ->?  Q_Weil         (Test 114.3)
```

ist jedoch kategorial zu grob:

- `W_res^top` ist eine **Spur-/Distributionsstruktur** (lineare Form)
- `Q_Weil` ist eine **Quadratform** (bilinear, nach Faltung/Pairing entstanden)

Eine direkte Identifikation würde eine neue kategoriale Vermischung erzeugen —
analog zum No-Go `X = m_arith` (NEU-114).

---

## Neues Zwischenobjekt: Weil-Distribution W_xi

**Definition 115.1 — Weil-Distribution (explizite-Formel-Distribution):**

```
W_xi  :  PW_t  ->  C
```

definiert durch die vier normalisierten Beiträge der expliziten Formel:

```
W_xi  =  W_zeros  +  W_Gamma  +  W_prime  +  W_{pole/triv}
```

wobei:

```
W_zeros[f]      =  sum_gamma  f-hat(gamma)          (Nullstellenbeitrag, linear)
W_Gamma[f]      =  archimedischer/Gamma-Beitrag
W_prime[f]      =  sum_p sum_k  f(log p^k) log p    (Primzahlbeitrag)
W_{pole/triv}[f]=  Pol- und triviale Nullstellen-Beitraege
```

`W_xi` ist eine **lineare Distribution** auf dem Paley-Wiener-Raum `PW_t`.

**Übergang zur Quadratform:**

Die Weil-Quadratform entsteht erst durch Pairing mit dem geeigneten
Bombieri-Testfunktionsobjekt:

```
Q_Weil[f]  =  < W_xi, f* * f >
```

oder in der aequivalenten Bombieri-Normalisierung auf `PW_t`.

---

## Neue Rückbindungsarchitektur (ab NEU-115)

```
Spur A:   m_arith  -->  W_xi  -->  Q_Weil
Spur B:   W_res^top -->  W_xi  -->  Q_Weil
```

Beide Spuren treffen sich **nicht** direkt in `Q_Weil`, sondern im gemeinsamen
Zwischenobjekt `W_xi` auf dem Bombieri-Testfunktionsraum `PW_t`.

**Vollständige Kette (Spur B):**

```
X  ->  W_res^top  ->  W_xi  ->  Q_Weil  ->  RH
```

**Vollständige Kette (Spur A):**

```
Pi_gamma(X) = m_arith  ->  W_xi  ->  Q_Weil  ->  RH
```

---

## Präzisierter Test 114.3 (ersetzt den Originaltest)

**Originaltest 114.3 (zu grob):**

```
W_res^top  ->?  Q_Weil
```

**Präzisierter Test 115.A (NEU-115):**

```
W_res^top  =?  W_xi    auf dem Bombieri-Testfunktionsraum PW_t
```

Status: ❓[O]  <- zentraler Rückbindungstest (NEU-116)

Erst wenn diese Gleichheit der Distributionen/Spuren gilt, folgt:

```
W_res^top  ->  Q_Weil
```

---

## No-Go NEU-115 (kategorialer Schutzsatz)

**Satz 115.0 (No-Go, kategorial):**

```
W_res^top  =  Q_Weil
```

ist **kategorial falsch**. ✗[M]

Begründung: `W_res^top` ist eine lineare Spur-/Distributionsform;
`Q_Weil` ist eine quadratische Form. Sie leben auf verschiedenen
kategorialen Ebenen.

**Korrekte Kette:**

```
W_res^top  =?  W_xi,     W_xi  ~>  Q_Weil
```

---

## Satzstatusmatrix (NEU-115)

| Satz | Inhalt | Status |
|---|---|---|
| 115.0 | `W_res^top = Q_Weil` ist kategorial falsch | ✗[M] |
| 115.1 | Definition W_xi als lineare Weil-Distribution auf PW_t | ✓[M] |
| 115.2 | Q_Weil = < W_xi, f* * f > (Pairing-Konstruktion) | ✓/⚠[M] |
| 115.3 | m_arith -> W_xi (Spur A Interface) | ❓[O] |
| 115.4 | W_res^top =? W_xi (Spur B Interface, Test 115.A) | ❓[O] |
| 115.5 | Konvergenz/Normierung W_xi auf PW_t exakt | ❓[O] (NEU-113) |

---

## Konsequenzen für die Arbeitsteilung

```
NEU-113:  Bombieri-Normalisierung von RECHTS
          Q_Weil = < W_xi, f* * f > exakt fixieren
          Vorzeichen, Normierung, Konvergenz auf PW_t
          <- Flaschenhals Spur A

NEU-115:  Definition des gemeinsamen Interface W_xi
          Zwei-Spuren-Architektur (dieses Dokument)

NEU-116:  Rückbindungstest W_res^top =? W_xi
          Zentraler Test Spur B
          <- Flaschenhals Spur B (präzisiert)
```

---

## Aktualisierter kritischer Pfad (ab NEU-115)

```
Feshbach-Kollaps (NEU-77)                      [M]
  +
Herglotz-Weil-Brücke (NEU-112)                [M]/?[O]
  m_arith = Pi_gamma(X)
  +
NEU-113: Bombieri-Normalisierung               <- FLASCHENHALS SPUR A
  W_xi auf PW_t: W_zeros/W_Gamma/W_prime/W_pole exakt
  Q_Weil = < W_xi, f* * f >
  +
NEU-115: Interface W_xi definiert              [M] (dieses Dokument)
  +
NEU-116: Rückbindungstest W_res^top =? W_xi   <- FLASCHENHALS SPUR B
  +
m_arith(z) Herglotz  <=>  RH  (NEU-63D)       ⚠[M]
```
