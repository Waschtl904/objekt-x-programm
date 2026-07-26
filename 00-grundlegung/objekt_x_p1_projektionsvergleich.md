# X-P1 — Projektionsvergleich Dyson–Connes

> Angelegt: 17. Juni 2026
> Erster operativer Schritt im Objekt-X-Programm.
> Epistemischer Status: ✗ [H] soweit nicht anders markiert.
> Ziel: Nicht X konstruieren, sondern seine zwei sichtbarsten Schatten vergleichen.

---

## Grundidee

Objekt X hat (hypothetisch) zwei sichtbare Projektionen:
```
π_D : X  →  arithmetische Quasikristalle   (Dyson-Seite)
π_C : X  →  adèlische BC-Geometrie         (Connes-Seite)
```
Beide Projektionen sehen denselben Kamm:
```
log Q_+×  =  { k log p : p prim, k ∈ Z \{0} }
```
Das ist die erste gemeinsame Invariante von X.

---

## Die Dyson-Seite: π_D(X)

**Dysons arithmetischer Quasikristall (2009):**
Unter der Voraussetzung RH bilden die nichttrivialen Nullstellen
{ 1/2 + i*gamma_rho } eine Verteilung auf der reellen Achse (via Im(rho) = gamma_rho),
die sich wie ein eindimensionaler Quasikristall verhält:

- Aperiodisch, aber geordnet (keine Translation bringt das Muster zur Deckung).
- Die Fourier-Transformierte hat Punktmassen genau an:
```
supp(mu_hat_Dyson)  ⊆  { ± k log p : p prim, k ≥ 1 }
```
Dies ist die explizite Formel in Fourier-Gestalt:
Primzahlen und Primzahlpotenzen erscheinen als Frequenzen.

**Trägerdatum:**  log Q_+×, positiver Kegel.

---

## Die Connes-Seite: π_C(X)

**Connes' BC-Zeitentwicklung:**
Das BC-System C(Ẑ) ⋊ N× trägt eine kanonische Zeitentwicklung sigma_t,
definiert durch:
```
sigma_t(u_n) = n^{it} u_n,    u_n  Isometrien in BC
```
Die Spektralwerte dieser Zeitentwicklung (d.h. die möglichen Exponenten)
liegen in:
```
spec(sigma_t^{BC})  ⊆  log N×  ⊆  log Q_+×
```
Genauer: Im vollständigen adel. Bild (C_0(A_f) ⋊ Q_+×) ist die Zeitentwicklung
durch Q_+×-Skalierung gegeben; die Frequenzen sind log(q) für q ∈ Q_+×.

**Trägerdatum:**  log Q_+× (volle Gruppe).

---

## Erstes Prüflemma (X-P1.1)

```
┌────────────────────────────────────────────────────────────┐
│  Dysons Quasikristall-Spektrum und Connes' BC-Zeitentwicklung  │
│  haben dasselbe log-prime Trägerdatum:                         │
│                                                               │
│  supp(mu_hat_Dyson)  und  spec(sigma_t^{BC})                  │
│  sind beide in  log Q_+×  enthalten.                          │
└────────────────────────────────────────────────────────────┘
```

**Status: ✓ [M]** (für die Trägerinklusion; beide Seiten bekannt).

Dies ist kein neues Resultat, sondern eine Beobachtung:
Beide Projektionen lesen aus X dieselbe Gruppe log Q_+× heraus.

---

## Zentrale Frage (X-P1.2)  ✗ [H]

```
┌────────────────────────────────────────────────────────────┐
│  Welche Struktur muss X besitzen, damit beide Projektionen     │
│  denselben log-prime-Kamm sehen?                               │
└────────────────────────────────────────────────────────────┘
```

Minimale Antwort:
X muss eine kanonische Q_+×-Graduierung tragen, so dass:

(i)  π_D(X) diese Graduierung als Fourier-Träger sieht
     (Nullstellen als Exponenten der Graduierungscharaktere),
(ii) π_C(X) dieselbe Graduierung als Zeitentwicklungsfrequenzen sieht
     (n^{it}-Spektrum der BC-Dynamik).

Formuliert als Minimalforderung an X:
```
X trägt eine kanonische Q_+×-Graduierung,
kompatibel mit beiden Projektionen π_D und π_C.
```

Das ist eine präzisierte Version von Axiom A2 aus dem Minimalaxiome-Blatt,
aber jetzt mit konkretem Prüftest (Projektionsvergleich statt abstrakter Forderung).

---

## Was der Kamm strukturell leistet

Der log-prime-Kamm
```
log Q_+×  =  span_Z { log p : p prim }
```
ist nicht zufällig:

- Er erzeugt die Zeitentwicklung der BC-KMS-Zustände (Connes-Seite).
- Er erzeugt die Fourier-Frequenzen der expliziten Formel (Dyson-Seite).
- Er ist die Bild-Gruppe unter der Wortlänge L: Q_+× → R_+  (OP-1-Seite).
- Er ist der Träger der Gewichtsfunktion w_s aus OP-1.6f.2 (Beurling-Seite).

Der Kamm taucht also in *vier* verschiedenen Kontexten des Programms auf.
Das ist ein starker struktureller Fingerabdruck für X.

---

## Nächster Schritt: X-P1.3

Zu klären:
Gibt es ein kanonisches Objekt
```
H_X  in/über  A_2D^r  oder  A_BC^{C*}
```
dessen Spektrum genau { gamma_rho } (die imaginären Teile der Nullstellen) realisiert,
oder ist die Verbindung nur auf der Träger-Ebene (Kamm) und nicht auf der
Punkt-Ebene (einzelne Nullstellen) möglich?

Das wäre der Übergang von X-P1 (Kamm-Vergleich) zu X-P2 (Spektrum-Vergleich)
und damit zu Axiom A3.

**Status: ✗ [H], nächste Frage.**

---

## Was wir jetzt *nicht* tun

- Kein Beweis von A3 (spektrale Realisierung der Nullstellen).
- Kein Einbau von GUE.
- Keine Annahme von RH als Arbeitshypothese (außer wo explizit markiert).
- Kein Bau von X selbst.

Erster Arbeitsschritt ist Beobachtung und Strukturvergleich, nicht Konstruktion.
