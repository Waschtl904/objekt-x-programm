# NEU-220u — Spektraldeterminante, Schattenklasse und Resolventenspur

**Katalog-ID:** NEU-220u
**Knoten:** [O-220-1-PD5a3f8-spectral-determinant-normal-form]
**Vorgänger:** NEU-220t (Commit 7b02a03) — Metrikblock-Klassifikation ✓[K/M]_part
**Status:** ✓[K/M]_part, konditional (PD5a3f8a–f) / ?[O] (PD5a3f8g, RH-stark)

---

## Ausgangsforderung

Der aus NEU-220t exportierte Auftrag „unabhängiger selbstadjungierter Operator + spektrale Determinante = ξ“ wird hier in der korrekten Schattenklasse typisiert. Die Metrikkorrektur im tautologischen Nullstellenraum ist endgültig ausgeschlossen (NEU-220t); der nächste sinnvolle Schritt ist die präzise Determinantenform, gegen die ein unabhängiger adelischer Kandidat getestet werden muss.

---

## PD5a3f8a — \(\Xi(z) = \xi(1/2+iz)\) und Symmetrie ✓[K]

Setze \(\Xi(z) := \xi(\tfrac12+iz)\). Aus \(\xi(s) = \xi(1-s)\) folgt

$$
\Xi(-z) = \Xi(z).
$$

Unter RH sind die Nullstellen von \(\Xi\) reell und treten als \(\pm\gamma\) mit Vielfachheiten auf (klassische Hadamard-Produktdarstellung von \(\zeta\) bzw. \(\xi\)). Da \(\Xi(0) = \xi(1/2) \ne 0\), ist

$$
\boxed{D_\Xi(z) := \frac{\Xi(z)}{\Xi(0)}}
$$

ganz, gerade und bei \(z=0\) gleich 1.

---

## PD5a3f8b — N(T) und Schattenklassenzwang ✓[K/M]

Unter RH seien \(0 < \gamma_1 \le \gamma_2 \le \cdots\) die positiven Nullstellenordinaten mit Vielfachheiten. Die Riemann-von-Mangoldt-Formel

$$
N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T)
$$

liefert via partieller Summation:

$$
\sum_{\gamma>0}\gamma^{-p}
\begin{cases}
<\infty, & p>1,\\
=\infty, & p\le1.
\end{cases}
$$

Für einen positiven Operator \(A_+\) mit Eigenwerten \(\gamma>0\):

$$
\boxed{A_+^{-1}\in\mathcal{S}_p \quad\Longleftrightarrow\quad p>1.}
$$

Insbesondere \(A_+^{-1} \in \mathcal{S}_2\), \(A_+^{-1} \notin \mathcal{S}_1\), aber \(A_+^{-2} \in \mathcal{S}_1\). Das bestimmt die zulässige Determinantenklasse vollständig.

---

## PD5a3f8c — Erste Normalform: quadrierter Fredholm-Determinant ✓[K/M], konditional

Unter RH: \(A_+ e_\gamma = \gamma e_\gamma\) auf \(\mathcal{H}_+ = \ell^2(\{\gamma>0\}, m_\gamma)\). Da \(A_+^{-2} \in \mathcal{S}_1\), ist \(\det(I - z^2 A_+^{-2})\) ein gewöhnlicher Fredholm-Determinant. Paarung der Nullstellen \(\pm\gamma\), Geradheit von \(\Xi\), und Konvergenz von \(\sum\gamma^{-2}\) liefern:

$$
\boxed{\frac{\Xi(z)}{\Xi(0)} = \det(I-z^2A_+^{-2}) = \prod_{\gamma>0}\left(1-\frac{z^2}{\gamma^2}\right)^{m_\gamma}.}
$$

Kein zusätzlicher Exponentialfaktor: Ein nullstellenfreier Quotient zweier ganzer Funktionen der Ordnung \(\le 1\) ist \(e^{az+b}\); Geradheit erzwingt \(a=0\), Normierung bei \(z=0\) erzwingt \(b=0\). Exakte Determinantennormalform.

---

## PD5a3f8d — Zweite Normalform: Carleman–Fredholm-Determinant ✓[K/M], konditional

Signierter Operator \(H_Z = A_+ \oplus (-A_+)\), Spektrum \(\{\pm\gamma\}\). Da \(H_Z^{-1} \in \mathcal{S}_2\setminus\mathcal{S}_1\), existiert \(\det(I-zH_Z^{-1})\) **nicht** in gewöhnlicher Form. Der Carleman-Fredholm-Determinant zweiter Ordnung ist korrekt:

$$
\det{}_2(I-zH_Z^{-1}).
$$

Paarweise: \(\left(1-\tfrac{z}{\gamma}\right)e^{z/\gamma}\left(1+\tfrac{z}{\gamma}\right)e^{-z/\gamma} = 1-\tfrac{z^2}{\gamma^2}\). Somit:

$$
\boxed{\frac{\Xi(z)}{\Xi(0)} = \det{}_2(I-zH_Z^{-1}).}
$$

Beide Normalformen sind äquivalent:

$$
\boxed{\det(I-z^2A_+^{-2}) = \det{}_2(I-zH_Z^{-1}).}
$$

---

## PD5a3f8e — Negativaudit von \(\det(I-zH^{-1})\) ✓[M]_neg

Der Kandidat \(\Xi(z)/\Xi(0) = \det(I-zH^{-1})\) mit **gewöhnlichem** Fredholm-Determinanten ist wegen \(H^{-1} \notin \mathcal{S}_1\) typologisch falsch:

$$
\boxed{\checkmark[M]_{\mathrm{neg}}.}
$$

Dies gilt auch für eine Metrikkorrektur im tautologischen Nullstellenraum selbst — beide Wege sind endgültig ausgeschlossen (vgl. NEU-220t).

---

## PD5a3f8f — Resolventenspur und Momenthierarchie ✓[M], konditional

Aus \(D_\Xi(z) = \det(I-z^2A_+^{-2})\) folgt für \(z \notin \operatorname{spec}(A_+)\):

$$
\frac{D_\Xi'(z)}{D_\Xi(z)} = -2z\,\operatorname{Tr}\left((A_+^2-z^2)^{-1}\right).
$$

Da \(\Xi'(z) = i\,\xi'(1/2+iz)\), erhält man die autoritative Spurform:

$$
\boxed{i\frac{\xi'}{\xi}\left(\frac12+iz\right) = -2z\,\operatorname{Tr}\left((A_+^2-z^2)^{-1}\right).}
$$

Dies ist ein deutlich präziseres Ziel als „Determinante = ξ“. Ein unabhängiger adelischer Operator müsste genau diese Identität liefern.

**Spur-Moment-Bedingungen:** Für \(|z| < \gamma_1\):

$$
\log\frac{\Xi(z)}{\Xi(0)} = \operatorname{Tr}\log(I-z^2A_+^{-2}) = -\sum_{k\ge1}\frac{z^{2k}}{k}\operatorname{Tr}(A_+^{-2k}).
$$

$$
\boxed{\operatorname{Tr}(A_+^{-2k}) = -\frac{k}{(2k)!}\left.\frac{d^{2k}}{dz^{2k}}\log\Xi(z)\right|_{z=0}.}
$$

Diese Identitäten liefern eine Hierarchie konkreter, endlicher Tests für jeden adelischen Operatorkandidaten. Alle Zahlen \(-\tfrac{k}{(2k)!}(\log\Xi)^{(2k)}(0)\) müssen positive reelle Zahlen sein, falls sie als Spuren positiver Operatorpotenzen realisiert werden — eine notwendige, aber keine hinreichende Konsistenzbedingung für RH.

---

## Exakte Äquivalenz zur RH

$$
\boxed{\mathrm{RH}}
$$

ist äquivalent zur Existenz eines invertierbaren selbstadjungierten Operators \(H_X\) mit \(H_X^{-1} \in \mathcal{S}_2\), symmetrischem diskretem Spektrum und

$$
\boxed{\det{}_2(I-zH_X^{-1}) = \frac{\Xi(z)}{\Xi(0)} \qquad \forall z\in\mathbb{C}.}
$$

**Rückrichtung:** Eigenwerte von \(H_X\) sind reell ⇒ Nullstellen des regulierten Determinanten liegen auf der reellen \(z\)-Achse ⇒ entsprechende Nullstellen von \(\xi(1/2+iz)\) liegen auf \(\operatorname{Re}s = 1/2\).

**Hinrichtung:** Unter RH kann \(H_X\) tautologisch als Diagonaloperator mit Eigenwerten \(\pm\gamma\) konstruiert werden.

Die bloße Äquivalenz ist noch kein Fortschritt gegen RH. Der Fortschritt müsste in der quellseitigen (adelischen) Konstruktion von \(H_X\) liegen.

---

## PD5a3f8g — Nichttautologische Zulassungskriterien für \(H_X\) ?[O], RH-stark

Ein Kandidat aus der BC-/adelischen Architektur darf nur dann als echter Hilbert–Pólya-Kandidat gelten, wenn alle folgenden Punkte **unabhängig von der Nullstellenliste** bewiesen werden:

- **HP-1:** \(H_X = H_X^*\)
- **HP-2:** \(H_X\) besitzt kompakten Resolventen
- **HP-3:** \(H_X^{-1} \in \mathcal{S}_2 \setminus \mathcal{S}_1\)
- **HP-4:** \(N_{H_X}(T) = \tfrac{T}{\pi}\log\tfrac{T}{2\pi} - \tfrac{T}{\pi} + O(\log T)\) (beidseitiges Spektrum; halbierte Formel für \(A_+\))
- **HP-5:** \(\det_2(I-zH_X^{-1}) = \Xi(z)/\Xi(0)\)
- **HP-6:** Die Determinantenidentität folgt aus einer Spur-, Streu- oder relativen Determinantenformel
- **HP-7:** Nullstellenlagen werden nirgendwo als Eingabedaten benutzt

Der Hadamard-Produktcharakter von \(\zeta\) bzw. \(\xi\) zeigt, warum die Determinantenidentität sämtliche nichttrivialen Nullstellen einschließlich ihrer Vielfachheiten festlegt.

### Leitformel des Programms

$$
\boxed{i\frac{\xi'}{\xi}\left(\frac12+iz\right) = -2z\,\operatorname{Tr}\left((A_X^2-z^2)^{-1}\right).}
$$

Nicht die Nullstellen sollen als Spektrum eingesetzt werden — diese Identität soll aus der adelischen Operatorarchitektur folgen; erst dann wären die Nullstellen gezwungen, das Spektrum eines selbstadjungierten Operators zu sein.

---

## Knotentabelle

| Teilaufgabe | Inhalt | Status |
|---|---|---|
| PD5a3f8a | \(\Xi(z)=\xi(1/2+iz)\), Geradheit, Normierung | ✓[K] |
| PD5a3f8b | N(T); Schattenklassenzwang \(A_+^{-1}\in\mathcal{S}_2\setminus\mathcal{S}_1\) | ✓[K/M] |
| PD5a3f8c | \(\det(I-z^2A_+^{-2})\) exakte Normalform | ✓[K/M], konditional |
| PD5a3f8d | \(\det_2(I-zH_Z^{-1})\); Äquivalenz beider Normalformen | ✓[K/M], konditional |
| PD5a3f8e | \(\det(I-zH^{-1})\) typologisch falsch (Negativaudit) | ✓[M]_neg |
| PD5a3f8f | Resolventenspurform \(\xi'/\xi\); Spur-Moment-Hierarchie | ✓[M], konditional |
| PD5a3f8g | Nichttautologische HP-1–HP-7-Kriterien für \(H_X\) | ?[O], RH-stark |

```
[O-220-1-PD5a3f8-spectral-determinant-normal-form]
  -> ✓[K/M]_part, konditional  (PD5a3f8a-f abgeschlossen)
  -> ?[O]                       (PD5a3f8g: unabhaengiger adelischer H_X, RH-stark)
```

---

## Gesamtbilanz

| Aussage | Status |
|---|---|
| Metrikkorrektur im tautologischen Nullstellenraum | ✓[M]_neg |
| Gewöhnlicher Determinant \(\det(I-zH^{-1})\) | ✓[M]_neg |
| Quadrierter Determinant \(\det(I-z^2A_+^{-2})\) | ✓[K/M], konditional |
| \(\det_2(I-zH^{-1})\) | ✓[K/M], konditional |
| Resolventenspurform von \(\xi'/\xi\) | ✓[M], konditional |
| Unabhängiger adelischer \(H_X\) | ?[O], RH-stark |
| Adelische Herleitung der Determinantenidentität | ?[O], RH-stark |

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-220t (7b02a03) | Metrikblock-Klassifikation, off-axis-Trägheit, Similarity-No-go |
| NEU-220s rev.2 (11aa74c) | Kreinraum, \(J_\kappa\), \(\mathcal{E}_{\mathcal{Z}}\), \(Z_{\mathcal{Z}}\) |
| Titchmarsh (1986) | Riemann-von-Mangoldt-Formel, Hadamard-Produkt |
| Simon (2005) | Spurideale \(\mathcal{S}_p\), regulierte Determinanten \(\det_2\) |
| Connes (1999) | BC-Kern, adelischer Rahmen |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
