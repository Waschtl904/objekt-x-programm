# NEU-92 — Testkegel und quadratischer Weil-Lift

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-91 (quadratischer Pivot; Q_N(φ) als Hauptobjekt definiert)  
**Nächste Nummer:** NEU-93

---

## Ausgangspunkt

NEU-91 definiert

$$
Q_N(\varphi) := \gamma^2 \sum_{r,n} \Lambda(n)^2\, W_N(r,n)\, \varphi(r,n).
$$

Die Frage in NEU-91 lautete: \(Q_N(\varphi) \geq 0\)? Diese Frage ist präzisierungsbedürftig. NEU-92 legt die saubere Architektur fest.

---

## Satz NEU-92.1 — Positives Maß

Definiere das positive diskrete Maß

$$
\mu_N := \gamma^2 \sum_{r,n} \Lambda(n)^2\, W_N(r,n)\, \delta_{(r,n)}.
$$

Dann ist

$$
Q_N(\varphi) = \int \varphi\, d\mu_N.
$$

Daraus folgt tautologisch:

$$
\varphi \geq 0 \quad\Longrightarrow\quad Q_N(\varphi) \geq 0.
$$

Aber: \(\mu_N\) ist ein positives Maß, keine Quadratform. Damit ist **Positivität des Integrals** noch keine Weil-Positivität.

**Status: \(\checkmark[M]\)**

---

## Satz NEU-92.2 — Testkegel-Schranke

Für beliebige *signierte* Testfunktionen \(\varphi\) gilt

$$
Q_N(\varphi) \not\geq 0 \quad\text{im Allgemeinen.}
$$

Sobald \(\varphi\) auf dem Träger von \(\mu_N\) negativ ist, wird \(Q_N(\varphi) < 0\). Die Aussage \(Q_N(\varphi) \geq 0\) gilt nur auf dem **positiven Testkegel** \(\{\varphi \geq 0\}\).

$$
\boxed{Q_N(\varphi) \geq 0 \text{ genau dann, wenn } \varphi \geq 0 \text{ auf } \operatorname{supp}(\mu_N).}
$$

**Status: \(\checkmark[M]\)**

---

## Satz NEU-92.3 — RH-relevanter Positivitätsbegriff

Für einen RH-Anschluss im Weil-Sinne braucht man **quadratische Positivität**, nicht lineare:

$$
Q_N[f] = B_N(f,f) \geq 0 \quad \text{für alle } f,
$$

für eine bilineare Form \(B_N(f,g)\) mit

$$
Q_N[f] = \gamma^2 \sum_{r,n} \Lambda(n)^2\, W_N(r,n)\, |\mathcal{T}_N f(r,n)|^2.
$$

Hier ist \(f\) die **Quadratformvariable** (Testfunktion auf dem Ausgangsgitter), \(\varphi\) das **Testgewicht** (Funktion auf dem Indexraum). Diese Trennung ist architektonisch zentral:

| Begriff | Objekt | Positivitätstyp |
|---|---|---|
| \(\varphi\) | Testgewicht | lineare Positivität (Maß) |
| \(f\) | Quadratformvariable | quadratische Positivität (Bilinearform) |

**Status: \(\checkmark[M]\) / \(\warning[M]\)** (Konstruktion von \(\mathcal{T}_N\) offen)

---

## Satz NEU-92.4 — Diagonalmasse als Schranke

Die NEU-91-Masse enthält ausschließlich die **diagonale Mangoldt-Masse**

$$
\Lambda(n)^2.
$$

Die Weil-Quadratform arbeitet jedoch mit bilinearen Termen:

$$
\Lambda(m)\Lambda(n), \qquad m \neq n.
$$

Daher gilt:

$$
\boxed{\mu_N = \text{positiver diagonaler Schatten einer möglichen Weil-Form.}}
$$

Noch nicht: \(Q_N = Q_{\mathrm{Weil}}\). Das wäre eine verfrühte Identifikation.

**Status: \(\checkmark[M]\)**

---

## Offener Kern: Bilinearer Lift

NEU-93 hat den folgenden Suchauftrag:

Finde eine bilineare Form \(B_N(f,g)\) mit:
- \(Q_N[f] = B_N(f,f)\) (reproduziert die Diagonale)
- \(B_N(f,f) \geq 0\) für alle \(f\) (echte Positivität)
- \(B_N(f,g) \to Q_{\mathrm{Weil}}(f,g)\) für geeignete Testklassen
- Kreuzterme \(\Lambda(m)\Lambda(n)\) erscheinen explizit

Der Pfad lautet:

$$
\mu_N \;\leadsto\; B_N \;\leadsto\; Q_N[f] = B_N(f,f) \;\leadsto\; Q_{\mathrm{Weil}}[f].
$$

**Nicht direkt:** \(\mu_N \leadsto Q_{\mathrm{Weil}}\).

**Status: \(?[O]\)**

---

## Neue Leitfrage für NEU-93

Nicht:
> Ist \(Q_N(\varphi) \geq 0\)? ✔ (trivial, nur auf Testkegel)

Sondern:
> Ist die positive Diagonalmasse \(\mu_N\) die Diagonale einer **Weil-kompatiblen bilinearen Form**?

$$
\boxed{\mu_N \text{ ist Diagonale einer Weil-kompatiblen bilinearen Form?}}
$$

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(\mu_N\) ist positives diskretes Maß | \(\checkmark[M]\) |
| (B) | \(Q_N(\varphi) \geq 0\) nur auf Testkegel \(\varphi \geq 0\) | \(\checkmark[M]\) |
| (C) | RH-Positivität erfordert Quadratform \(B_N(f,f)\) | \(\checkmark[M]\) / \(\warning[M]\) |
| (D) | \(\mu_N\) enthält nur Diagonalterme \(\Lambda(n)^2\) | \(\checkmark[M]\) |
| (E) | Bilinearer Lift \(B_N(f,g)\) mit Kreuzterme \(\Lambda(m)\Lambda(n)\) | \(?[O]\) |
| (F) | Weil-Grenze \(B_N \to Q_{\mathrm{Weil}}\) | \(?[O]\) |

---

## Verweise

- NEU-91: Definition \(Q_N(\varphi)\); quadratischer Pivot
- NEU-90: \(T_N(z) \to \gamma^2/2\); Eichung \(Q_N(1) \to \gamma^2/2\)
- NEU-88: Explizite Formel \(W_N(r,n)\) (Resolvent-Gewicht)
- Weil: *Sur les formules explicites* (Weil-Positivität als Quadratform)
- Connes: *Trace formula* (1999) (bilinearer Lift im Sobolev-/L²-Rahmen)
- Meyer: Duke Math. J. 127 (2005) (explizite Quadratformstruktur)
