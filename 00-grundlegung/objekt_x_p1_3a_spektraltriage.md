# X-P1.3a — Spektralrealisierungs-Triage

> Angelegt: 17. Juni 2026
> Vorbedingung für Axiom A3: Spektraltyp muss gewählt sein, bevor H_X konstruiert wird.
> Epistemischer Status: ✗ [H] soweit nicht anders markiert.

---

## Warum Triage zuerst

Die Formulierung
```
A3: Es gibt H_X mit spec(H_X) = { gamma_rho }
```
ist zu stark und würde A3 aus dem ✗-Bereich heimlich hochstufen.

Vor jedem Konstruktionsversuch muss entschieden sein:
```
Welche Spektralrealisierung der Nullstellen ist kompatibel
mit der Q_+×-Graduierung von X?
```
Das ist die Brücke von A2 (Graduierung) zu A3 (Spektrum).

---

## Drei Realisierungstypen

### Typ 1 — Hilbert–Pólya-Punktspektrum  ✗ [H]

Ein selbstadjungierter Operator H_X mit
```
spec(H_X) = { gamma_rho : rho = 1/2 + i*gamma_rho nichttriviale Nullstelle }
```
als echtes Punktspektrum (Eigenwerte).

Das ist die stärkste Form; direkt äquivalent zu RH.

**Probleme für X:**
- H_X müsste in A_2D^r oder A_BC^{C*} leben — unklar, ob ein solcher Operator
  dort überhaupt existiert.
- Punkt-Eigenwerte und Beurling-/Graduierungsstruktur passen nicht automatisch
  zusammen: Graduierung ist eine globale Algebra-Struktur, Punktspektrum ist
  eine Operator-Eigenschaft.
- Kein Konstruktionsvorschlag bekannt.

**Status: ✗ [H] — stärkste, direktäquivalente Form; für X-P1 nicht als Einstieg geeignet.**

---

### Typ 2 — Connes-Absorptionsspektrum  ⋄ [EXT]

Connes' Realisierung (adel. Klassenraum / "Spectral Interpretation of Zeros"):

- Nullstellen erscheinen *nicht* als Eigenwerte, sondern als **Absorptionslinien**:
  fehlende Spektrallinien eines adel. Flusses.
- Der Connes-Operator D auf dem adel. Raum X_Q = Q× \ A_Q^1
  hat Spektrum = alle Punkte von Re(s) = 1/2, *minus* die Nullstellen.
- Nichtkritische Nullstellen (falls vorhanden) erscheinen als Resonanzen.
- Die explizite Formel ist eine **Spurformel** auf X_Q unter der Q×-Wirkung.

**Passung zu X:**
- Passt gut zu A2 (Q_+×-Graduierung) und zur BC-Seite (π_C).
- Der adel. Raum X_Q ist direkt mit dem BC-Corner verwandt
  (C_0(A_f) ⋊ Q_+× ist der "Zahlenfeld-Fall" dieses Konstrukts).
- Absorptionsspektrum ist kompatibel mit Q_+×-Skalenstruktur:
  die fehlenden Linien liegen bei den Nullstellen *der Q_+×-invarianten Spurformel*.

**Status: ⋄ [EXT] — extern belegt (Connes 1998/1999); Verbindung zu A_2D^r intern zu prüfen.**

Literatur:
- Connes, "Trace Formula in Noncommutative Geometry and the Zeros of
  the Riemann Zeta Function" (1999), arXiv:math/9811068.

---

### Typ 3 — Spur-/Distributionsspektrum (Meyer-Weg)  ⋄ [EXT]

Meyer (aufbauend auf Connes) konstruiert einen Operator auf einem
nuklearen Fréchet-Raum, der die nichttrivialen Nullstellen als Spektrum
enthalt oder realisiert — aber nicht als naive Eigenwerte:

- Die Nullstellen erscheinen als Pole oder Werte in einer **Spurformel**
  (Charakterformel, Distribution Spur).
- Der Trägerraum ist Fréchet/nuklear, nicht ein klassischer Hilbertraum.
- Das Spektrum ist kein Punkt-Spektrum im Hilbert-Sinn, sondern ein
  **distributional spectrum** (Pol der meromorphen Fortsetzung einer Spur).

**Passung zu X:**
- A_2D^r ist Fréchet. Dieser Typ ist damit natürlicher mit unserer Algebra
  kompatibel als Typ 1.
- Spurformel auf Fréchet-Algebren ist in der NCG-Literatur bekannt
  (Wodzicki-Residuum, Connes-Spurformel).
- Kein Eigenwert-Prüflemma nötig; stattdessen: Hat die Spur von e^{-tH_X}
  die richtige Nullstellen-Enkodierung?

**Status: ⋄ [EXT] — Meyer-Konstruktion extern belegt; Übertragung auf A_2D^r intern offen.**

Literatur:
- Meyer, "On a Representation of the Idele Class Group Related to Primes
  and Zeros of L-Functions" (2005), Duke Math. J.

---

## Vergleichstabelle

| | Typ 1: Hilbert-Pólya | Typ 2: Connes-Absorption | Typ 3: Spur/Distribution |
|---|---|---|---|
| Spektraltyp | Punktspektrum (Eigenwerte) | Absorptionslinien (fehlend) | Pole der Spur (Distribution) |
| Trägerraum | Hilbert | Adel. L^2-Raum | Fréchet/nuklear |
| RH-Äquivalenz | Direkt (äquivalent) | Impliziert SI der crit. Linie | Bedingt |
| Q_+×-Kompatibilität | Unklar | Hoch (BC-Corner) | Hoch (A_2D^r Fréchet) |
| Passung zu A_2D^r | Gering | Mittel | Hoch |
| Extern belegt | Hilbert-Pólya: offen | Connes 1999 | Meyer 2005 |
| Status | ✗ [H] | ⋄ [EXT] | ⋄ [EXT] |

---

## Empfehlung für X-P1.3b

Für den Objekt-X-Ast ist **Typ 3** der natürlichste Einstieg:

- A_2D^r ist Fréchet-artig – Meyer-Konstruktion passt strukturell.
- Kein Hilbert-Operator nötig; stattdessen Spur auf Fréchet-Algebra.
- Verbindung zur expliziten Formel über Spurformel-Analogie ist intern prüfbar.

**Typ 2** ist die Fallback-Option, wenn die BC-Corner-Verbindung
die Adel-Konstruktion direkt liefert.

**Typ 1** bleibt ✗ [H] und wird nicht verfolgt, bis Typ 2 oder Typ 3 blockiert.

---

## Nächste Frage: X-P1.3b  ✗ [H]

```
Gibt es auf A_2D^r (oder ihrem Bild in A_BC^{C*})
eine kanonische Spur Tr_X derart, dass die meromorphe Fortsetzung
von s ↦ Tr_X(a^{-s}) Pole bei den nichttrivialen Nullstellen hat?
```

Das wäre die Typ-3-Version von A3 — und direkt angreifbar aus der
Fréchet-/Beurling-Struktur von A_2D^r heraus.

**Status: ✗ [H], nächste Frage.**
