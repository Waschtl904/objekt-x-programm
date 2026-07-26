# NEU-227 — Koordinatenwörterbuch und Spektralmaßform des Feshbach-Transfers

**Katalog-ID:** NEU-227
**Knoten:** `[O-226-2]` Wörterbuch `✓[M]` · `[O-226-1]` Spektralmaßform `✓[K/M]`
**Stand:** 26. Juli 2026
**Vorgänger:** NEU-226
**Ergebnis:** Beide Vorschaltknoten geschlossen. Der Einstiegspunkt verschiebt sich auf den
$u$-Regulator und den Gramoperator.

---

## 1. `[O-226-2]` — Kein Entweder-oder: zwei Stufen derselben Konstruktion

### 1.1 Die Auflösung

$$
\boxed{\ \text{NEU-51 (51.2) definiert die \textbf{Kopplung} } V_p; \qquad \text{NEU-55 (55.3) definiert die \textbf{Dynamik} von } J^-. \ }
$$

Sie sind keine konkurrierenden Definitionen desselben Operators. NEU-42 trennt bereits die
Primkopplung $m\mapsto pm$ vom Fouriertransport innerhalb eines festen $V_n$-Sektors.

### 1.2 Das exakte Wörterbuch

$$
\boxed{\ \eta_{p;m;s,u} \longleftrightarrow e_R V_M, \qquad M = pm, \qquad R = u+ps \ }
\tag{227.1}
$$

Die volle Sektorverschiebung $R\mapsto R+M$ liefert

$$
R+M = u+ps+pm = u + p(s+m),
$$

also in NEU-51-Koordinaten

$$
\boxed{\ s \longmapsto s+m . \ }
\tag{227.2}
$$

Auch das Gewicht stimmt: $R\log M = (u+ps)\log(pm)$.

$$
\boxed{\ r\mapsto r+n \quad\text{und}\quad s\mapsto s+m \quad\text{sind unter } n=pm,\ r=u+ps \ \textbf{dieselbe} \ \text{Bewegung.}\ }
$$

### 1.3 Einschränkung in zusammengesetzten Sektoren

In einem Sektor $V_M$ trägt $J^-$ nicht nur den Sprung $d=M$, sondern alle Bandkanten über
Teiler $d\mid M$. Unter $R=u+ps$ bedeutet $R\mapsto R\pm d$:

$$
u+ps \pm d = u + ps' \quad\Longleftrightarrow\quad d = p(s'-s) \quad\Longleftrightarrow\quad p\mid d .
$$

$$
\boxed{\ \text{Der Sprung bleibt genau dann in derselben } u\text{-Restklasse, wenn } p\mid d. \ \text{Für } p\nmid d \ \text{mischt er } u\text{-Klassen.}\ }
$$

Also: $s\mapsto s+m$ beschreibt den $d=M=pm$-Anteil, **nicht** den gesamten Operator in
zusammengesetzten Sektoren.

### 1.4 Rückwirkung auf NEU-225 — eine Lücke schließt sich

Im Primfall $M=p$ sind die Teiler $1$ und $p$. Der Kanal $d=1$ entfällt wegen $\log 1 = 0$;
der Kanal $d=p$ erfüllt $p\mid d$. Damit bleibt **nur ein** Sprung, und er erhält die
$u$-Restklasse.

$$
\boxed{\ \text{Die Annahme „bei festem } u\text{" in NEU-225 §3 ist damit \textbf{gerechtfertigt}, nicht bloß gesetzt.} \quad \checkmark[M] \ }
$$

Die Einzelkettenrechnung ist im Primsektor vollständig. In zusammengesetzten Sektoren ist sie
es nicht — dort bleibt `[O-225-3]` offen.

### 1.5 Quellenkritik — Umfang

$$
\boxed{\ \text{Die alte Darstellung wird \textbf{nicht} negativ geschlossen. Zurückzurollen ist allein ihre Verwendung \textbf{ohne} das Koordinatenwörterbuch.}\ }
$$

Der in NEU-226 §4 als `⚠[M]` geführte „Wörterbuchkonflikt" ist damit aufgelöst und wird durch
(227.1) ersetzt. `✓[M]` `[O-226-2]`

---

## 2. `[O-226-1]` — Spektralmaßform statt Eigenbasis

Sei $D := D_{\mathrm{rel}} = D_{\mathrm{rel}}^*$ mit projektionswertigem Spektralmaß
$E_D : \mathcal B(\mathbb R)\to\operatorname{Proj}(\mathcal H_{\mathrm{rel}})$.

### 2.1 Kreuzspektralmaß — Ersatz für die Eigenbasisannahme

$$
\boxed{\ \mu_{pq}^{a,b}(B) := \bigl\langle V_p a,\ E_D(B)\,V_q b\bigr\rangle_{\mathcal H_{\mathrm{rel}}}, \qquad B\in\mathcal B(\mathbb R) \ }
\tag{227.3}
$$

Ein komplexes endliches Borelmaß mit
$\lvert\mu^{a,b}_{pq}\rvert(\mathbb R) \le \lVert V_pa\rVert\,\lVert V_qb\rVert$.

Die Off-Diagonalität liegt **nicht notwendig in $D$**, sondern kann vollständig aus der
Überlappung von $\operatorname{Ran}V_p$ und $\operatorname{Ran}V_q$ stammen (NEU-226 §3).

### 2.2 Ersatz für (51.3)

$$
\boxed{\ \bigl\langle a,\ K_{pq}(z)\,b\bigr\rangle = \int_{\mathbb R}\frac{d\mu^{a,b}_{pq}(\lambda)}{\lambda-z}, \qquad K_{pq}(z) = V_p^*(D-z)^{-1}V_q \ }
\tag{227.4}
$$

Weder diskretes Spektrum noch die Existenz von Eigenvektoren $\eta_\alpha$ wird vorausgesetzt.

### 2.3 Ersatz für (51.4)

Operatorwertiges Kreuzmaß $M_{pq}(B) := V_p^*E_D(B)V_q$, dann im schwachen Operatorsinn

$$
\boxed{\ K_{pq}(z) = \int_{\mathbb R}\frac{dM_{pq}(\lambda)}{\lambda-z}, \qquad K_N(z) = \bigl(K_{pq}(z)\bigr)_{p,q\le N} \ }
\tag{227.5}
$$

$K_{pq}(z)\neq0$ ist mit kanalerhaltendem $D$ verträglich, sobald
$\operatorname{Ran}V_p \not\perp \operatorname{Ran}V_q$. Der Kollisionsmechanismus
$V_{pm} = V_{qm'}$ ist genau der Grund, weshalb der kollabierte Jacobi-Raum keine automatische
Primkantendiagonalität besitzt.

### 2.4 Ersatz für (51.7)

Sei $\mathscr E_N$ der Quellhilbertraum mit Orthonormalbasis $(e_j)_{j\in J_N}$ und
$\mu^{j,k}(B) = \langle Ve_j, E_D(B)Ve_k\rangle$. Dann

$$
\boxed{\ \sum_{j\in J_N}\int_{\mathbb R}\frac{d\mu^{j,j}(\lambda)}{\lvert\lambda-z\rvert} < \infty
\qquad\Longleftrightarrow\qquad
\bigl\lvert D-z\bigr\rvert^{-1/2}V \in \mathcal S_2 \ }
\tag{227.6}
$$

$$
\boxed{\ K_N(z)\in\mathcal S_2 \iff \sum_{j,k\in J_N}\Bigl\lvert \int_{\mathbb R}\frac{d\mu^{j,k}(\lambda)}{\lambda-z}\Bigr\rvert^2 < \infty
\quad\Bigl(= \operatorname{Tr}_{\mathscr E_N}\bigl(K_N(z)^*K_N(z)\bigr)\Bigr) \ }
\tag{227.7}
$$

### 2.5 Das Spurklassekriterium, nachgerechnet

Polarzerlegung $(D-z)^{-1} = U_z\lvert D-z\rvert^{-1}$ mit $B_z := \lvert D-z\rvert^{-1/2}V$:

$$
K_N(z) = B_z^*\,U_z\,B_z .
$$

**Verifikation der Vertauschung.** $B_z^*U_zB_z = V^*\lvert D-z\rvert^{-1/2}U_z\lvert D-z\rvert^{-1/2}V$
stimmt mit $V^*(D-z)^{-1}V$ überein, weil $U_z$ und $\lvert D-z\rvert^{-1/2}$ beide beschränkte
Borelfunktionen desselben selbstadjungierten $D$ sind ($\lvert D-z\rvert^2 = (D-x)^2+y^2$) und
daher kommutieren. `✓[M]`

$$
\boxed{\ \lvert D-z\rvert^{-1/2}V \in\mathcal S_2 \quad\Longrightarrow\quad K_N(z)\in\mathcal S_1 \ }
\tag{227.8}
$$

Hinreichend, für allgemeines komplexes $z$ **nicht** automatisch notwendig.

### 2.6 Der Nicht-$\mathcal S_1$-Zeuge

Für $z=x+iy$, $y>0$: $\operatorname{Im}(D-z)^{-1} = y\bigl((D-x)^2+y^2\bigr)^{-1}\ge0$, also

$$
\boxed{\ \operatorname{Im}K_N(z) = y\,V^*\bigl((D-x)^2+y^2\bigr)^{-1}V \ \ge\ 0 \ }
$$

$$
\operatorname{Tr}\operatorname{Im}K_N(z) = \sum_j \int_{\mathbb R}\frac{y}{(\lambda-x)^2+y^2}\,d\mu^{j,j}(\lambda)
\tag{227.9}
$$

Divergenz von (227.9) beweist $K_N(z)\notin\mathcal S_1$. Die $\mu^{j,j}$ sind positiv:
$\mu^{j,j}(B) = \lVert E_D(B)Ve_j\rVert^2$.

> **Vorbehalt.** Der Test darf **nicht** mit einer informellen „orthonormalen Primkanalbasis"
> angewendet werden. Erst der $u$-Regulator und die Hilbertisierung des Quellraums bestimmen,
> welche Indexfamilie tatsächlich orthonormal ist. `[O-226-3]`/`[O-226-4]`

### 2.7 Abgeleitete Schranke: der Zeuge verlangt $V\notin\mathcal S_2$

> **Abgeleitete Beobachtung (nicht Quellenaussage, aus (227.9) hergeleitet).**
> Der Poisson-Kern ist durch $1/y$ beschränkt, und $\mu^{j,j}(\mathbb R) = \lVert Ve_j\rVert^2$.
> Also
> $$\operatorname{Tr}\operatorname{Im}K_N(z) \ \le\ \frac1y\sum_j\lVert Ve_j\rVert^2 \ =\ \frac{\lVert V\rVert_2^2}{y}.$$

$$
\boxed{\ V\in\mathcal S_2 \quad\Longrightarrow\quad \operatorname{Im}K_N(z)\in\mathcal S_1 . \ }
$$

$$
\boxed{\ \text{Der Nicht-}\mathcal S_1\text{-Zeuge ist daher \textbf{nur möglich, wenn} } V\notin\mathcal S_2. \ }
$$

Das ist verträglich mit der strukturellen Vermutung $V\in\mathcal S_4\setminus\mathcal S_2$
und verschärft sie zur **Notwendigkeit**.

**Aber nicht hinreichend.** Da $\sigma(D)=\mathbb R$ mit absolutstetigem Typ (NEU-225), kann
die Spektralmasse ins Unendliche entweichen, wo der Poisson-Kern wie $y/\lambda^2$ abfällt.
$\sum_j\lVert Ve_j\rVert^2 = \infty$ ist notwendig, aber nicht hinreichend für Divergenz von
(227.9).

$$
\boxed{\ \text{`[O-226-6]` hängt damit direkt an `[O-226-3]`: der } u\text{-Regulator steuert } \lVert Ve_j\rVert. \ }
$$

### 2.8 Bimeasure-Form (formal)

$\Omega_V(B,C) := \operatorname{Tr}_{\mathscr E_N}\bigl(V^*E_D(B)V\,V^*E_D(C)V\bigr)$, dann formal

$$
\lVert K_N(z)\rVert_2^2 = \iint_{\mathbb R^2}\frac{d\Omega_V(\lambda,\mu)}{(\lambda-\bar z)(\mu-z)} .
$$

Erst nach Fixierung des Quellhilbertraums und Nachweis der Spurexistenz auswertbar. `⚠[M]`

### 2.9 Status

| Aussage | Status |
|---|---|
| Eigenbasisform (51.3)/(51.4)/(51.7) | `✓[M]_neg` gegen die Quelle |
| Spektralmaßumschreibung (227.3)–(227.9) | `✓[K/M]` |
| Polarzerlegungsargument (227.8) nachgerechnet | `✓[M]` |
| Nicht-$\mathcal S_1$-Zeuge verlangt $V\notin\mathcal S_2$ | `✓[M]` abgeleitet |
| $\mathcal S_1/\mathcal S_2$-Entscheidung | **gesperrt** durch Regulator und Quellhilbertisierung |

Die Weyl-Funktion bleibt die Boreltransformierte eines zyklischen Spektralmaßes. NEU-46s
lokale Interpretation wird **nicht beschädigt**, sondern von der diskreten Eigenbasisannahme
befreit. `✓[M]`

---

## 3. Revidierte Reihenfolge

| Knoten | Aufgabe | Status |
|---|---|---|
| `[O-226-2]` | Koordinatenwörterbuch (227.1)/(227.2) | **`✓[M]`** |
| `[O-226-1]` | Spektralmaßform | **`✓[K/M]`** |
| `[O-226-3]` | **$u$-Regulator intrinsisch bestimmen** und Konvergenz von $V_p$ | `❓[O]` — jetzt erster |
| `[O-226-4]` | Quellhilbertraum $\mathscr E$, Gramoperator, orthonormale Basis | `❓[O]` |
| `[O-226-5]` | $K(z)\in\mathcal S_2$ über (227.7) | `❓[O]` |
| `[O-226-6]` | $K(z)\notin\mathcal S_1$ über (227.9); **verlangt $V\notin\mathcal S_2$** | `❓[O]` |
| `[O-226-7]` | $\det_2(I-K(z))$ gegen die Weil-/$\Xi$-Schicht | `❓[O]` |
| `[O-225-3]` | Zusammengesetzte Sektoren: Sprünge mit $p\nmid d$ mischen $u$-Klassen | `❓[O]` |

> **Sperrvermerk.** Die endlichen Kollapsoperatoren aus NEU-77 können diese Schattenfragen
> nicht entscheiden: starke bzw. punktweise Konvergenz auf endlich getragenen Vektoren liefert
> keine Kontrolle der Schattennormen. `✓[M]`

> **Regel zum Regulator.** Die Summationsreichweite über $u$ ist ein **echter** Regulator. Sie
> entscheidet über Definiertheit, Beschränktheit und möglicherweise über den Übergang zwischen
> $\mathcal S_1$ und $\mathcal S_2$. Sie darf **nicht** nachträglich an $\Xi$-Daten angepasst
> werden — das wäre die Tautologiefalle aus X.neg (vgl. NEU-220s–w).

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-42 | Trennung Primkopplung $m\mapsto pm$ gegen Fouriertransport im festen $V_n$-Sektor |
| NEU-43/44 | $\tilde\omega_2$, relative Architektur, mögliche Kanalüberlappung |
| NEU-46 | lokale Matrixstellen als Streudaten — von der Eigenbasisannahme befreit |
| NEU-51 | (51.2) Kopplung, (51.1) $u$-Regulator, (51.3)/(51.4)/(51.7) ersetzt |
| NEU-55 | (55.3) Dynamik von $J^-$ |
| NEU-56 | (56.12) Weg-B-Spektralmaßform |
| NEU-77 | endliche Kollapsidentität; Punkte (D)/(E) als Sperrvermerk |
| NEU-225 | absolutstetiges Spektrum, Option B, Primfaserkette |
| NEU-226 | Primkanalüberlappung, Rückrollung der Orthonormalität |
