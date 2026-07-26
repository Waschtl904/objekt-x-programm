# NEU-127 — Kanalseiten-Gramform-Triage: Klasse A vs. Klasse B

**Stand:** 6. Juli 2026
**Typ:** Triage-Blatt (Registerblatt, kein Beweisblatt, kein Konstruktionsblatt)
**Anschluss:** NEU-40 (Feshbach-Selbstenergie, Positivität), NEU-41 (Σ_N(β)-Struktur),
              NEU-62 (γ_N skalar), NEU-75 (Θ-Faktorisierung), NEU-79 (κ_N skalar),
              NEU-123.H/I (Jacobi-Renormierungsverbot), NEU-125 (Skalar-Ausschluss)

> **Hinweis:** NEU-126 (Rückleseprotokoll W_N, geplante Lektüre NEU-62) existiert nicht
> im Katalog. Die Blätter 126.A und 126.B sind verloren gegangen; nur der Gesamtzweck
> und 126.C sind bekannt. Eine Rekonstruktion aus Zusammenfassungen wurde bewusst
> unterlassen. Der inhaltliche Anschluss erfolgt direkt über NEU-125 und NEU-127.

**Ziel:** Systematische Sichtung aller vorhandenen Feshbach-/Graph-Operatoren auf eine
intrinsische, positive, nichtskalare Kanalseitenmetrik W_N, die vor Kollaps/Lanczos lebt
und als Prä-Lanczos-Gewichtung

$$\widehat{B}_N^\Lambda \;\mapsto\; W_N^{1/2}\,\widehat{B}_N^\Lambda\, W_N^{1/2}$$

taugen könnte. Zentrale Neuerung: Die Kandidaten werden in zwei qualitativ verschiedene
Klassen geordnet — **Klasse A** (Kanalseiten-Gramoperatoren, rein geometrisch) und
**Klasse B** (Kopplungs- und Selbstenergieformen, arithmetisch geladen).

---

## 127.0 — Leitfrage

Nach NEU-123.H/I und NEU-125 steht fest:

1. **Skalar-Ausschluss:** Jede Gewichtung W_N = c_N I vor Lanczos ist auf Jacobi-Datenebene
   äquivalent zu einer skalaren Renormierung J_N ↦ c_N J_N. Sie kann die Doppelbarriere

$$b_{1,N} \to 0, \qquad \frac{b_{2,N}}{b_{1,N}} \to \infty$$

   nicht lösen. (NEU-125)

2. **Post-Lanczos-Verbot:** Diagonale Jacobi-Ähnlichkeiten J_N ↦ D_N^{-1} J_N D_N verletzen
   entweder die Produktbarriere $b_{1,N}^+ b_{1,N}^- = b_{1,N}^2$ oder die
   Selbstadjungiertheit/Herglotz-Struktur. Verboten. (NEU-123.I)

3. **Neuformulierung der offenen Frage:** Nach der Rücklese von NEU-40, 62, 75, 77, 78 lautet
   die Frage nicht mehr

   > „Welche Skala macht den Jacobi-Limes richtig?"

   sondern:

   > **„Ist der eigentliche Freiheitsgrad gar nicht skalar, sondern die Wahl einer kanonischen
   > positiven Form auf der Prä-Lanczos-Feshbach-Ebene?"**

Die Leitfrage dieses Blattes lautet daher:

$$\boxed{ \text{Existiert ein intrinsisches } W_N > 0,\; W_N \neq c_N I, \text{ vor Kollaps/Lanczos, aus bestehenden Operatoren wie } \Pi_N^*\Pi_N,\; S_N^*S_N,\; R_N^*R_N,\; C_N^\#C_N,\; \Sigma_N(\beta),\; W_{\mathrm{res,rel}}? }$$

Und falls ja: Trägt diese Form bereits arithmetische Information **(Klasse B)** oder ist sie
rein geometrisch **(Klasse A)**?

**NEU-127 konstruiert kein W_N. Es definiert die zulässige Suchklasse und verhindert,
dass skalare Normalisierungen, post-Lanczos-Ähnlichkeiten oder nichtpositive Formen
fälschlich als Ausweg erscheinen.**

---

## 127.1 — Zulässigkeitskriterien für W_N

Ein Kandidat W_N ist nur dann zulässig, wenn alle folgenden Bedingungen erfüllt sind:

1. **Prä-Lanczos-Lage**
   W_N muss vor der Lanczos-Extraktion auf Feshbach-/Graph-Ebene definiert sein:
   $$\widehat{B}_N^\Lambda \;\mapsto\; W_N^{1/2}\,\widehat{B}_N^\Lambda\, W_N^{1/2}$$
   Nachträgliche Jacobi-Ähnlichkeiten J_N ↦ D_N^{-1} J_N D_N fallen unter NEU-123.I
   und sind verboten.

2. **Positivität**
   W_N > 0 (selbstadjungiert, positiv definit). Nur dann ist
   $W_N^{1/2} \widehat{B}_N^\Lambda W_N^{1/2}$ bei selbstadjungiertem $\widehat{B}_N^\Lambda$
   wieder selbstadjungiert.

3. **Nichtskalarität**
   W_N ≠ c_N I. Skalargewichtungen können die Quotienten $b_{j+1,N}/b_{j,N}$ nicht
   verändern und sind durch NEU-125 ausgeschlossen.

4. **Intrinsizität**
   W_N darf nicht nachträglich an $b_{j,N}$ oder numerische Befunde angepasst werden.
   Es muss aus einer bereits vorhandenen Struktur stammen.

5. **Herglotz-Kompatibilität**
   Die transformierte Größe muss weiterhin einen selbstadjungierten Operator erzeugen
   und damit eine Herglotz-Stieltjes-Funktion im Sinne von NEU-119.

6. **Zweistufen-Kontrolle**
   W_N muss nicht nur $b_{1,N}^W \asymp 1$ ermöglichen, sondern auch
   $$\frac{b_{2,N}^W}{b_{1,N}^W} = O(1)$$
   oder wenigstens eine nichtdivergente zweite Offdiagonale plausibel machen. Eine
   reine „b_1-Rettung" ohne Kontrolle der zweiten Stufe verschiebt die Doppelbarriere nur.

---

## 127.2 — Hauptunterscheidung: Klasse A vs. Klasse B

Die Kandidaten zerfallen in zwei qualitativ verschiedene Klassen:

| | **Klasse A** | **Klasse B** |
|---|---|---|
| Herkunft | Feshbach-/Kollapsgeometrie | Feshbach-Kopplung selbst |
| Positivität | formal-geometrisch: $\langle x, \Pi_N^*\Pi_N x\rangle = \|\Pi_N x\|^2 \geq 0$ | inhaltlich aus Feshbach-Elimination |
| Arithmetischer Gehalt | keiner | Euler-Kumulanten, Primstruktur |
| NEU-40-Befund | nicht betroffen | **zentral**: Positivität stammt aus Elimination |
| Priorität | nachrangig | **hoch** |

**Architektonische Konsequenz:** Klasse B ist nicht nur „auch positiv" — die Positivität
trägt bereits Information über die Primstruktur. Das ist ein qualitativer Unterschied, der
sich bei der späteren Konstruktion als entscheidend herausstellen könnte.

### 127.2A — Klasse A: Kanalseiten-Gramoperatoren

Positivität ist hier formal: $\langle x, \Pi_N^* \Pi_N x\rangle = \|\Pi_N x\|^2 \geq 0$,
und analog für $S_N^* S_N$, $R_N^* R_N$. Die Frage ist, ob diese Formen tatsächlich
Krylov-Schichten nichttrivial differenzieren.

| Operator | Herkunft | Positivität | Nichtskalar? | Bisher dokumentiert | Status |
|---|---|---|---|---|---|
| $\Pi_N^* \Pi_N$ | Kollapsgeometrie (NEU-77/78) | formal ✓ | möglich | implizit in NEU-77, nicht als Metrik | ❓[O] |
| $S_N^* S_N$ | partiell isom. Shift (NEU-77) | formal ✓ | möglich | $S_N$ als part. Isometrie; Gramform implizit | ❓[O] |
| $R_N^* R_N$ | r-Gewicht/Resolventenstruktur (NEU-75/78) | formal ✓ | möglich | als Operator vorhanden, keine Metrik | ❓[O] |

**Wichtig:** $\Pi_N \Pi_N^* = \kappa_N I$ (NEU-79) ist skalar und ausgeschlossen.
Die offene Frage ist, ob $\Pi_N^* \Pi_N$ auf der Kanalseite nichtskalar ist.

### 127.2B — Klasse B: Kopplungs- und Selbstenergieformen

Positivität stammt hier inhaltlich aus der Feshbach-Elimination — nicht bloß aus einer
Hilbertraumidentität. Das ist der Befund aus NEU-40.

| Operator | Formel | Positivität | Arithmetischer Gehalt | Status |
|---|---|---|---|---|
| $C_N^\# C_N$ | Feshbach-Kopplung (NEU-40/41) | strukturell ✓ | direkt aus Kopplung | ❓[O] — **Priorität** |
| $C_p^\# C_p$ | pro Primkanal $p$ | strukturell ✓ | primweise Kopplung | ❓[O] |
| $\Sigma_N(\beta)$ | $= C_N E_N(\beta)^{-1} C_N^\# = \sum_{p \leq N} (1-p^{-\beta})^{-1} C_p C_p^\#$ | ⚠[M] aus NEU-40 | Euler-Gewichte $(1-p^{-\beta})^{-1}$ | ⚠[M]/❓[O] → NEU-41 |
| $W_{\mathrm{res,rel}}$ | relative Weil-/Spurpaarung (NEU-43/44) | zu prüfen | graph-kategoriale Primkantenstruktur | ❓[O] |

**NEU-40-Befund (zentral):** In NEU-40 existiert nicht nur ein positiver Operator, sondern
ein Operator, dessen Positivität inhaltlich aus der Feshbach-Elimination stammt. $\Sigma_N(\beta)$
deformiert den Jacobi-Resolvent $z - D_N - \ldots$ in Richtung Mangoldt-/Primstruktur. Die
Gewichte $(1 - p^{-\beta})^{-1}$ sind direkt mit Euler-Kumulanten verknüpft.

---

## 127.3 — Ausschlussmatrix

| Kandidat | Prä-Lanczos? | positiv? | nichtskalar? | intrinsisch? | Quotient änderbar? | Klasse | Status |
|---|---|---|---|---|---|---|---|
| $c_N I$ | ja | ja | **nein** | evtl. | nein | — | ausgeschlossen (NEU-125) |
| $\kappa_N I$ | ja | ja | **nein** | ja | nein | — | unzureichend (NEU-79) |
| $\gamma_N I$ | ja | ja | **nein** | ja | nein | — | unzureichend (NEU-62) |
| $\Pi_N^* \Pi_N$ | ja | zu prüfen | möglich | möglich | ja | **A** | ❓[O] — Kandidat |
| $S_N^* S_N$ | ja | ja | möglich | möglich | ja | **A** | ❓[O] — Kandidat |
| $R_N^* R_N$ | ja | ja | möglich | möglich | ja | **A** | ❓[O] — Kandidat |
| $C_N^\# C_N$ | ja | ja | möglich | ja | ja | **B** | ❓[O] — **Priorität** |
| $\Sigma_N(\beta)$ | ja | ⚠[M] | möglich | ja | ja | **B** | ⚠[M]/❓[O] → NEU-41 |
| $W_{\mathrm{res,rel}}$ | ja | zu prüfen | möglich | möglich | ja | **B** | ❓[O] — Kandidat |
| $D_N^{-1} J_N D_N$ | **nein** | irrelevant | ja | nein | formal ja | — | **verboten** (NEU-123.I) |

---

## 127.4 — Minimaler Wirkungstest für jeden Kandidaten

Für jeden zulässigen Kandidaten $W_N$ sind drei Größen auf der Jacobi-Seite zu untersuchen:

$$a_{0,N}^W := \langle \Omega_N, \widehat{B}_N^W \Omega_N \rangle$$

$$(b_{1,N}^W)^2 := \bigl\| \widehat{B}_N^W \Omega_N - a_{0,N}^W \Omega_N \bigr\|^2$$

$$\frac{b_{2,N}^W}{b_{1,N}^W}$$

Ein Kandidat $W_N$ besteht den Minimaltest nur, wenn:
- $a_{0,N}^W = 0$ oder kontrolliert klein bleibt,
- $b_{1,N}^W \asymp 1$ (erste Stufe stabilisiert),
- $b_{2,N}^W / b_{1,N}^W = O(1)$ oder zumindest nicht wie $N$ divergiert.

**Wenn $b_{2,N}^W / b_{1,N}^W \sim N$ weiterbesteht, ist der Kandidat trotz möglicher
$b_1$-Stabilisierung unzureichend.** Die Doppelbarriere muss auf beiden Stufen gebrochen
werden.

---

## 127.5 — Prüfplan: Drei Fragen für NEU-41

Für die Klasse-B-Kandidaten, insbesondere $\Sigma_N(\beta)$, sind bei der Lektüre von NEU-41
genau drei Fragen zu stellen:

1. **Kanonizität:** Ist $\Sigma_N(\beta)$ kanonisch definiert, oder hängt seine Definition noch von
   Hilfsentscheidungen ab (Basiswahl, Projektionen, Regularisierung)?

2. **Interpretationsebene:** Erscheint $\Sigma_N(\beta)$ lediglich als Schur-Komplement, oder wird es
   bereits als Energie-, Quadratik- oder Stabilitätsform interpretiert?

3. **Faktorisierung (entscheidend):** Gibt es eine natürliche Darstellung

$$\Sigma_N(\beta) = A_N^* A_N \qquad\text{oder}\qquad \Sigma_N(\beta) = W_N^{1/2} B W_N^{1/2},$$

   aus der sich eine Gram-Interpretation unmittelbar ergibt?

Wenn NEU-41 bereits implizit eine Faktorisierung dieser Art enthält, wäre das wesentlich
stärker als die bloße Beobachtung $\Sigma_N(\beta) \geq 0$.

---

## 127.F — Fazit und Entscheidungspfad

**Was NEU-127 abschließt:**

- NEU-62 und NEU-79 sind als rein skalare Normalisierungsblätter klassifiziert;
  $\gamma_N$ bzw. $\kappa_N$ sind keine operatorwertigen $W_N$-Metriken. ✓[M]
- NEU-75 liefert die Kreuzprodukt-Faktorisierung $\Theta = M_{e_n} \partial_\theta \delta_{BC}$
  und klärt $\log n$ vs. $\Lambda(n)$, führt aber keine positive Kanalseitenmetrik ein. ✓[M]
- NEU-125: Jede skalare Gewichtung ist ausgeschlossen. ✓[M]
- NEU-123.I: Post-Lanczos-Ähnlichkeiten sind verboten. ✓[M]
- Die Kandidaten zerfallen sauber in Klasse A (formale Gram-Geometrie) und Klasse B
  (arithmetisch geladene Feshbach-Selbstenergie). ✓[M]

**Was offen bleibt:**

$$\boxed{ \text{Findet sich in NEU-40/41/44/77/78 eine intrinsische, positive, nichtskalare Kanalseitenmetrik } W_N \text{ (Klasse A oder B)?} }$$

**Empfohlene Reihenfolge:**
1. **NEU-41:** Klasse-B-Prüfung mit den drei Fragen aus 127.5 ($\Sigma_N(\beta)$-Faktorisierung) — höchste Priorität.
2. **NEU-44:** Klasse-B-Prüfung relative Weil-Paarung / Primkantenstruktur.
3. **NEU-77/78:** Klasse-A-Prüfung $\Pi_N^*\Pi_N$, $S_N^*S_N$, $R_N^*R_N$.

Wenn ja → NEU-128: prä-Lanczos-Konstruktion.
Wenn nein → die Feshbach-Lanczos-Route ist in ihrer aktuellen Form durch keine
intrinsische Kanalseitenmetrik stabilisierbar.

**Gesamtstatus:** ❓[O] — Triage abgeschlossen, Kandidatenliste und Klasse-A/B-Unterscheidung
etabliert, keine $W_N$-Entscheidung getroffen.
