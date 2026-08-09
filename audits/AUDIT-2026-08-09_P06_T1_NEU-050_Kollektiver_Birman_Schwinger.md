# P06 G-T1 — Targeted-Reaudit NEU-050

**Datum:** 9. August 2026  
**SYN-Ziel:** P06 — Jacobi–Feshbach + Divisorgraph  
**Quellknoten:** `01-primkanten-werkzeuge/NEU-050_x3_kollektiver_birman_schwinger_operator.md`  
**Korrekturquellen:** NEU-051/052, NEU-225/226/227, P05 `SYN FROZEN`, F3-Primäraudit-Patch `87b82b1a`  
**Prüfart:** `TARGETED-REAUDIT`  
**Status:** **G-T1 COMPLETE — NEU-050 `INCORPORATED_part / RECONCILED`**

---

## 0. Prüfauftrag

Geprüft wurde ausschließlich:

1. welche Teile der kollektiven Birman–Schwinger-Architektur formal erhalten bleiben;
2. ob NEU-050 eine universelle Off-Diagonalität behauptet, die durch F3 zu präzisieren ist;
3. welche Divisor-/Nullstellen-/Fredholm-Aussagen nur Zielhypothesen sind;
4. wie die alte Herkunftserzählung über $L_3^\circ$ und `Wres` durch die spätere Kanalbild-/Spektralmaßform zu ersetzen ist.

Kein Vollneuaudit benachbarter Knoten.

---

## 1. Formale kollektive Architektur — bleibt erhalten

NEU-050 führt den kollektiven Kopplungsoperator in der Form

$$
\mathcal K_N(z)=V_N^*(D_{\rm rel}-z)^{-1}V_N,
\qquad
V_N=\sum_{p\le N}V_p,
$$

und die Blockmatrix

$$
K_{pq}(z):=V_p^*(D_{\rm rel}-z)^{-1}V_q
$$

ein.

Sobald die beteiligten Operatoren typkorrekt und wohldefiniert vorliegen, ist die algebraische Blockzerlegung

$$
\mathcal K_N(z)=\sum_{p,q\le N}K_{pq}(z)
$$

formal korrekt.

**Status:** `✓[M]` als abstrakte Operator-/Blockidentität **unter den Typvoraussetzungen**.

### Typfirewall

Dies konstruiert die intrinsischen $V_p$ nicht. Nach P05/NEU-228/229 bleiben Hebungsabstieg, gemeinsame Quellhilbertisierung und intrinsische Feshbach-Wohldefiniertheit gesperrt. Daher ist

$$
\boxed{\text{formale Feshbach-Architektur}\neq\text{intrinsisch konstruierter Objekt-X-Transfer}.}
$$

---

## 2. Hauptkorrektur — Off-Diagonalität ist generisch/non-forced, nicht universal

NEU-050 formuliert die volle Matrixarchitektur pointiert als

$$
\mathcal K_N=(K_{pq})_{p,q\le N}\neq\bigoplus_pK_p.
$$

Die spätere F3-Reconciliation präzisiert die Reichweite. Der robuste Befund ist:

- Primkanalbilder **können** nichttrivial überlappen;
- diese Überlappung kann Kreuzblöcke $K_{pq}$ erzeugen;
- Primblockdiagonalität ist **nicht strukturell erzwungen**;
- für ein konkretes Paar $p\neq q$ kann $K_{pq}$ dennoch verschwinden.

Daher ist die universelle Lesart

$$
K_{pq}(z)\neq0\qquad\forall p\neq q
$$

**nicht bewiesen**.

Kanonischer P06-Endsatz:

$$
\boxed{\operatorname{Ran}V_p\not\perp\operatorname{Ran}V_q
\ \text{kann generisch }K_{pq}(z)\neq0\text{ erzeugen;}
\ \mathcal K_N\text{ ist nicht a priori blockdiagonal.}}
$$

**Status:** `✓[M]` für die nicht-erzwungene Blockdiagonalität / mögliche Überlappung; universelles paarweises Nichtverschwinden `SUPERSEDED`.

---

## 3. Mechanismuskorrektur — Kanalbildüberlappung statt Primmischung von $D_{rel}$

NEU-050 deutet $K_{pq}$ als Interferenz über den gemeinsamen Resolventen. Die spätere Typisierung macht den Mechanismus präziser:

$$
K_{pq}(z)=V_p^*(D_{\rm rel}-z)^{-1}V_q
$$

kann off-diagonal sein, weil die Bilder der Kopplungen $V_p,V_q$ im gemeinsamen BC-/Graphraum überlappen. Daraus folgt **nicht**, dass $D_{\rm rel}$ selbst die Primlabels mischt.

Die historische Herkunftserzählung „$L_3^\circ$ + $\widetilde\omega_2$ + Wres erzeugen die Kreuzterme“ ist als konkrete intrinsische Konstruktion nicht gesichert, weil gerade die $L_3^\circ$-/Lift-/Wres-Abstiegsfragen später offen bzw. quellennegativ wurden.

**Endstatus:**

$$
\boxed{\text{Kanalbildüberlappung / Kreuzspektralmaß: P06-tauglich;}\quad
\text{intrinsische Quell-/Gramkonstruktion: }?[O]\to P11.}
$$

---

## 4. Spektralmaßform — verbindlicher Ersatz für die alte Eigenbasisdarstellung

NEU-050/051 entstanden vor der späteren Spektraltypklärung. Für P06 ist ausschließlich die NEU-227-Form verbindlich:

$$
\mu_{pq}^{a,b}(B):=\langle V_pa,E_D(B)V_qb\rangle,
$$

$$
\boxed{\langle a,K_{pq}(z)b\rangle
=\int_{\mathbb R}\frac{d\mu_{pq}^{a,b}(\lambda)}{\lambda-z}.}
$$

Damit wird keinerlei diskrete Eigenbasis von $D_{\rm rel}$ vorausgesetzt.

**Status:** `✓[K/M]` als verbindliche P06-Schreibweise.

---

## 5. Fredholm-/Determinantenebene — Architektur ja, Divisoridentität offen

### 5.1 Formal gültig

Ist $\mathcal K_N(z)$ in einer geeigneten Schattenklasse und holomorph in $z$, gelten die üblichen Fredholm-/Birman–Schwinger-Aussagen, etwa die Definition von

$$
\det(1-\mathcal K_N(z))
$$

im Spurklassenfall bzw. $\det_2$ im Hilbert–Schmidt-Fall.

**Status:** `✓[M]` formal/konditional auf die Schatten-/Holomorphievoraussetzungen.

### 5.2 Nicht bewiesen

NEU-050s Zielaussagen

$$
\operatorname{ord}_{z=\rho}\det(1-\mathcal K_\infty(z))=m_\rho
$$

und die Neutralität an trivialen Zetastellen sind **keine gesicherten Endresultate**. Ebenso ist der globale Grenzoperator $\mathcal K_\infty$ in der für Fredholmdeterminanten nötigen Topologie nicht konstruiert.

**Status:** `?[O]` / `CONDITIONAL`.

Die kollektive Determinante ist daher eine strukturell plausible Zielarchitektur, kein bereits realisierter Nullstellendetektor.

---

## 6. Schatten-/Konvergenzstatus

NEU-050 nennt Tr-Norm als bevorzugten Zieltopos. P06 übernimmt daraus **keine Konvergenzbehauptung**.

Spätere Korrekturen sichern:

1. $K_N$ ist auch bei festem $N$ nicht automatisch endlich-rangig;
2. NEU-77 liefert nur die endliche Feshbach-Identität und im Limes höchstens punktweise/starke Information auf kontrollierten Vektoren, keine Schattennormkonvergenz;
3. Schattenklasseneigenschaften des Grenztransfers können nicht aus den endlichen Trunkierungen geerbt werden;
4. die Entscheidung $\mathcal S_1$ gegen $\mathcal S_2$ hängt an der intrinsischen Lift-/Quellhilbertisierung.

**Status:** Schattenklasse und Fredholm-Limes `?[O]`.

---

## 7. Reconciliierte Statusmatrix NEU-050

| Aussage | Historische Rolle | P06-Endstatus |
|---|---|---|
| $\mathcal K_N=V_N^*(D_{rel}-z)^{-1}V_N$ | kollektive Architektur | `✓[M]` formal unter Typvoraussetzungen |
| $K_{pq}=V_p^*(D_{rel}-z)^{-1}V_q$ | Blockdefinition | `✓[M]` formal |
| volle Blockmatrix statt a priori Prim-Direktsumme | Hauptidee | `✓[M]` als **nicht erzwungene Blockdiagonalität** |
| $K_{pq}\neq0$ für jedes $p\neq q$ | mögliche Überlesart | `SUPERSEDED` / nicht bewiesen |
| generisch mögliche Kreuzblöcke durch überlappende Kanalbilder | spätere Präzisierung | `✓[M]` |
| $D_{rel}$ selbst mischt Primlabels | historische Fehlinterpretation | `×[M]` als notwendiger Mechanismus |
| diskrete Eigenbasisform von $K_{pq}$ | alter technischer Weg | `SUPERSEDED` durch NEU-227 |
| Kreuzspektralmaßform | heutige Form | `✓[K/M]` |
| Tr-Norm-Konvergenz $\mathcal K_N\to\mathcal K_\infty$ | Zieltopos | `?[O]` |
| $\det/\det_2$ wohldefiniert | abhängig von Schattenklasse | `CONDITIONAL` |
| Divisorordnung bei $\rho$ = Zetastellenmultiplizität | Endziel | `?[O]` |
| intrinsische $V_p$/Lift-/Gramquelle | Voraussetzung | `?[O]` → P11 |

---

## 8. Routing

### Nach P06

- abstrakte Schur-/Feshbach-/Birman–Schwinger-Architektur;
- $K_{pq}(z)$ als Blockoperator;
- Kreuzspektralmaße;
- Schatten-/Fredholmkriterien;
- charakteristische Werte und Determinanten **konditional** auf die fehlenden Voraussetzungen.

### Nach P11

- intrinsische Wahl/Definition der $V_p$ unabhängig vom Lift;
- Quellhilbertisierung und Gramoperator;
- Mischblock/verbundene Form;
- globale nichtorthogonale Kopplungsgeometrie.

---

## 9. Endurteil G-T1

$$
\boxed{\text{NEU-050: TARGETED-REAUDIT COMPLETE.}}
$$

$$
\boxed{\text{kollektive Birman--Schwinger-Architektur }\checkmark[M]_{part};
\quad\text{universelle Off-Diagonalität nicht bewiesen;}
\quad\text{Fredholm-/}\xi\text{-Realisierung }?[O].}
$$

**Endstatus für P06:** `INCORPORATED_part / RECONCILED`.
