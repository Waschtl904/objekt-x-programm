# NEU-231 — OX-1a: Algebraischer und topologischer Rohträger von Objekt X

**Status:** `✅ [K]` (Definitionell) — Vorbehalt: Kompatibilität mit bestehenden $A_{2D}^r$-Modulen zu prüfen (OX-1a.2)  
**Datum:** 2026-08-04  
**Strang:** 00 — Grundlegung  
**Vorgänger:** NEU-230 (OX-1 Zerlegung), NEU-44 (relative Primkanten), NEU-42 (Fourier-Hebung)  
**Nachfolger:** NEU-232 (OX-1b — intrinsische lokale positive Formen $B_p$)

---

## 0. Status und Ziel

Dieses Dokument konkretisiert den Teilknoten $[OX\text{-}1a]$ und definiert den kinematischen Rohträger $\mathcal{D}_X^{\mathrm{kin}}$.

Die Definition erfüllt folgende Anforderungen:

- Die relativen Primkanten $n \to pn$ bleiben vollständig markiert.
- Primzahlpotenzen entstehen **intrinsisch** durch wiederholte Kantenkomposition.
- Gemischte Primrichtungen ($p \neq q$) besitzen bereits einen algebraischen Träger.
- Der archimedische und der polare Sektor sind typisiert.
- Die gesamte Konstruktion trägt eine explizite Modulstruktur über $A := A_{2D}^{r}$.

> Es wird noch keine positive Form, kein Hilbertraum, keine Weil-Identität und kein
> Nullstellenspektrum vorausgesetzt. Der Rohträger ist die kinematische Bühne für
> die später zu konstruierende Gluungsform $B_X$.

---

## 1. Verwendete Grunddaten

Für OX-1a wird $A = A_{2D}^{r}$ als bereits fixierte lokal konvexe Algebra verwendet.
Benötigt werden ausschließlich:

- die komplexe Vektorraumstruktur;
- die lokal konvexe Topologie;
- die Multiplikation in $A$;
- die dadurch definierte linke Modulwirkung.

> Nicht benötigt: eine positive Spur, ein Skalarprodukt oder eine Hilbertraumdarstellung
> von $A$. Insbesondere wird keine Form $\langle a,b\rangle_A$ vorausgesetzt.

---

## 2. Der relative Primkantengraph

**Definition 2.1 — Vertices.**
Die Menge der arithmetischen Vertices ist
\[
V := \mathbb{N}_{\ge 1}.
\]
Ein Vertex $n \in V$ repräsentiert den ganzzahligen Index $n$, nicht einen Primkanal.

**Definition 2.2 — Gerichtete Primkanten.**
Für jede Primzahl $p$ und jedes $n \ge 1$ wird eine gerichtete, markierte Kante
\[
e_{n,p}: n \longrightarrow pn
\]
eingeführt. Die Gesamtmenge der Primkanten ist
\[
E_{\mathrm{rel}} := \bigl\{ e_{n,p} \;:\; n \in \mathbb{N}_{\ge 1},\; p \in \mathbb{P} \bigr\}.
\]
Quell- und Zielabbildungen:
\[
s(e_{n,p}) = n, \qquad t(e_{n,p}) = pn.
\]
Primmarkierung und logarithmische Kantenlänge:
\[
\operatorname{pr}(e_{n,p}) = p, \qquad \lambda(e_{n,p}) = \log p.
\]

> Die Primrichtung bleibt erhalten, auch wenn verschiedene faktorisierte Wege
> denselben ganzzahligen Zielindex erreichen.

---

## 3. Die kanonische Pfadhülle

Der reine Kantenträger enthält nur die Zeitinkremente $\log p$. Die arithmetischen
Zeiten $r\log p$ der Primzahlpotenzen entstehen erst durch wiederholte Komposition
derselben Primkante. Daher wird der Kantengraph unter endlicher Pfadkomposition
abgeschlossen.

**Definition 3.1 — Relative Primpfade.**
Ein Primpfad der Länge $r \ge 1$ ist ein Tupel
\[
\pi = (n;\, p_1, \ldots, p_r), \qquad n \in \mathbb{N}_{\ge 1},\; p_j \in \mathbb{P}.
\]
Er repräsentiert den gerichteten Weg
\[
n \longrightarrow p_1 n \longrightarrow p_2 p_1 n \longrightarrow \cdots \longrightarrow p_r \cdots p_1 n.
\]
Quelle, Ziel, kombinatorische und logarithmische Länge:
\[
s(\pi) = n, \qquad t(\pi) = n\prod_{j=1}^{r} p_j, \qquad |\pi| = r,
\qquad \lambda(\pi) = \log\frac{t(\pi)}{s(\pi)}.
\]
Die Menge aller positiven Primpfade:
\[
\mathsf{P}_{\mathrm{rel}}^{+} := \bigsqcup_{r \ge 1} \bigl\{ (n;\,p_1,\ldots,p_r) \bigr\}.
\]

**Definition 3.2 — Primladungsvektor.**
Für jede Primzahl $q$:
\[
\nu_q(\pi) := \#\bigl\{ j \in \{1,\ldots,r\} : p_j = q \bigr\}.
\]
Der vollständige Ladungsvektor $\bigl(\nu_q(\pi)\bigr)_{q \in \mathbb{P}}$ hat endlichen
Träger, und
\[
\lambda(\pi) = \sum_{q \in \mathbb{P}} \nu_q(\pi) \log q.
\]

**Definition 3.3 — Primzahlpotenzpfade.**
Für $p \in \mathbb{P}$ und $r \ge 1$:
\[
\pi_{n,p}^{(r)} := (n;\underbrace{p,\ldots,p}_{r}), \qquad t\bigl(\pi_{n,p}^{(r)}\bigr) = p^r n, \qquad \lambda = r\log p.
\]
Damit sind die Prime-Power-Zeiten bereits **kinematisch** im Rohträger enthalten.

**Definition 3.4 — Gemischte Primpfade.**
Ein Pfad $\pi$ heißt gemischt, wenn $\#\operatorname{supp}\,\nu(\pi) \ge 2$.
Beispiel: $(n;\,p,q)$ mit $p \neq q$. Solche Pfade bilden den ersten intrinsischen
algebraischen Ort für spätere Off-Diagonal-Kopplungen zwischen verschiedenen
Primrichtungen.

---

## 4. Pfadkomposition

Zwei Pfade $\pi = (n;\,p_1,\ldots,p_r)$ und $\eta = (m;\,q_1,\ldots,q_s)$ heißen
**komponierbar**, wenn $m = t(\pi)$. Ihre Komposition:
\[
\eta \circ \pi := (n;\,p_1,\ldots,p_r,q_1,\ldots,q_s).
\]
Es gilt $s(\eta \circ \pi) = s(\pi)$, $t(\eta \circ \pi) = t(\eta)$,
$\lambda(\eta \circ \pi) = \lambda(\pi) + \lambda(\eta)$,
$\nu_q(\eta \circ \pi) = \nu_q(\pi) + \nu_q(\eta)$.
Die Pfadkomposition ist assoziativ.

> **Bemerkung 4.1 — Keine vorzeitige Kommutativitätsrelation.**
> Die Pfade $(n;\,p,q)$ und $(n;\,q,p)$ besitzen denselben Endpunkt $pqn$, bleiben
> im Rohträger aber **zunächst verschieden**. Die Identifikation beider Pfade würde
> bereits eine Quotientierung einführen, deren Verträglichkeit mit der späteren
> positiven Form, der Off-Diagonal-Gluung, den relativen Primmarkierungen und dem
> Skalierungsfluss erst bewiesen werden müsste. OX-1a verwendet daher den maximal
> markierten, kollisionsfreien Pfadträger.

---

## 5. Arithmetischer Rohmodul

**Definition 5.1 — Freier Pfadmodul.**
\[
\mathcal{D}_{\mathrm{arith}}^{\mathrm{alg}}
:= \bigoplus_{\pi \in \mathsf{P}_{\mathrm{rel}}^{+}}^{\mathrm{alg}} A\,\varepsilon_\pi.
\]
Ein Element: $\sum_{\pi \in F} a_\pi \varepsilon_\pi$ mit $F \subset \mathsf{P}_{\mathrm{rel}}^{+}$ endlich,
$a_\pi \in A$. Linke $A$-Wirkung: $b \cdot \sum a_\pi \varepsilon_\pi = \sum (ba_\pi)\varepsilon_\pi$.
$\mathcal{D}_{\mathrm{arith}}^{\mathrm{alg}}$ ist ein freier linker $A$-Modul mit Basis
$\{\varepsilon_\pi : \pi \in \mathsf{P}_{\mathrm{rel}}^{+}\}$.

**Definition 5.2 — Ein-Kanten-Untermodul.**
\[
\mathcal{D}_{\mathrm{edge}}^{\mathrm{alg}}
:= \bigoplus_{e \in E_{\mathrm{rel}}}^{\mathrm{alg}} A\,\varepsilon_e
\;\subset\; \mathcal{D}_{\mathrm{arith}}^{\mathrm{alg}}.
\]

**Proposition 5.3 — Minimalität der Pfadhülle.**
$\mathcal{D}_{\mathrm{arith}}^{\mathrm{alg}}$ ist der kleinste freie linke $A$-Modul, der
alle Ein-Kanten-Symbole $\varepsilon_{e_{n,p}}$ enthält und für jede endliche komponierbare
Folge von Primkanten einen eindeutig markierten Pfadgenerator enthält. Insbesondere
enthält er intrinsisch $\varepsilon_{\pi_{n,p}^{(r)}}$ für alle Primzahlpotenzen $p^r$
sowie gemischte Generatoren $\varepsilon_{(n;p,q)}$.

---

## 6. Kanonische Zerlegung des arithmetischen Sektors

**Definition 6.1 — Reine $p$-Sektoren.**
\[
\mathcal{D}_p^{\mathrm{pure}}
:= \bigoplus_{\substack{\pi \in \mathsf{P}_{\mathrm{rel}}^{+} \\ \operatorname{supp}\,\nu(\pi) = \{p\}}}^{\mathrm{alg}} A\,\varepsilon_\pi.
\]
Dieser Sektor enthält sämtliche wiederholten $p$-Pfade und damit die Zeiten
$\log p,\; 2\log p,\; 3\log p, \ldots$

**Definition 6.2 — Gemischter Sektor.**
\[
\mathcal{D}_{\mathrm{mix}}^{\mathrm{alg}}
:= \bigoplus_{\substack{\pi \in \mathsf{P}_{\mathrm{rel}}^{+} \\ \#\operatorname{supp}\,\nu(\pi) \ge 2}}^{\mathrm{alg}} A\,\varepsilon_\pi.
\]

Kanonische algebraische Zerlegung des arithmetischen Rohmoduls:
\[
\mathcal{D}_{\mathrm{arith}}^{\mathrm{alg}}
= \Bigl(\bigoplus_{p \in \mathbb{P}}^{\mathrm{alg}} \mathcal{D}_p^{\mathrm{pure}}\Bigr)
\oplus \mathcal{D}_{\mathrm{mix}}^{\mathrm{alg}}.
\]

> **Bedeutung für OX-1c.** Der gemischte Sektor liefert noch keine Off-Diagonal-Kopplung
> $B_{pq}$, aber einen intrinsischen Träger, auf dem sie konstruiert werden kann.
> Die spätere Frage lautet nicht mehr nur: *Wie koppelt man zwei getrennte Räume
> $\mathcal{D}_p$ und $\mathcal{D}_q$?* Sondern präziser: *Kann $B_X$ aus der
> Wechselwirkung reiner und gemischter Pfadsektoren entstehen?*

---

## 7. Archimedischer Rohsektor

Als archimedischer Testkern wird zunächst $\mathscr{D}_\infty := C_c^\infty(\mathbb{R}_u)$
gewählt, wobei $u = \log x$ die natürliche additive Koordinate des Skalierungsflusses ist.

**Definition 7.1.**
\[
\mathcal{D}_\infty^{\mathrm{alg}}
:= \bigl(A \odot C_c^\infty(\mathbb{R}_u)\bigr)\varepsilon_\infty.
\]
Ein typisches Element: $\sum_{j=1}^N a_j \otimes f_j,\varepsilon_\infty$ mit $a_j \in A$,
$f_j \in C_c^\infty(\mathbb{R})$. Linke $A$-Wirkung: $b \cdot (a \otimes f,\varepsilon_\infty) = (ba \otimes f,\varepsilon_\infty)$.

> **Bemerkung 7.2.** Die Wahl von $C_c^\infty(\mathbb{R})$ fixiert nur einen glatten
> Testkern in logarithmischer Koordinate. Sie behauptet noch nicht, dass dieser Raum
> die endgültige Weil-Testfunktionsklasse ist, der Gammafaktor auf ihm als positive
> Form realisiert ist, oder der spätere archimedische Operator bestimmt wäre.
> Diese Fragen gehören zu **OX-1d**.

---

## 8. Polarer Rohsektor

**Definition 8.1.**
\[
\mathcal{D}_{\mathrm{pole}}^{\mathrm{alg}}
:= A\,\varepsilon_0 \oplus A\,\varepsilon_1.
\]
Die formalen Generatoren $\varepsilon_0$, $\varepsilon_1$ sind den Polen der vervollständigten
Zetafunktion bei $s=0$ und $s=1$ zugeordnet. Diese Definition typisiert nur zwei
Randrichtungen; sie legt weder ihre Normierung noch ihre spätere Einbettung in
die Weil-Form fest.

---

## 9. Gesamter algebraischer Rohträger

**Definition 9.1 — Kinematischer Objekt-X-Kern.**
\[
\boxed{
\mathcal{D}_X^{\mathrm{kin,alg}}
:= \mathcal{D}_\infty^{\mathrm{alg}}
\oplus \mathcal{D}_{\mathrm{arith}}^{\mathrm{alg}}
\oplus \mathcal{D}_{\mathrm{pole}}^{\mathrm{alg}}
}
\]

Ausgeschrieben:
\[
\mathcal{D}_X^{\mathrm{kin,alg}}
= \Bigl(A \odot C_c^\infty(\mathbb{R}),\varepsilon_\infty\Bigr)
\oplus \Bigl(\bigoplus_{\pi \in \mathsf{P}_{\mathrm{rel}}^{+}}^{\mathrm{alg}} A\,\varepsilon_\pi\Bigr)
\oplus A\,\varepsilon_0 \oplus A\,\varepsilon_1.
\]

Ein allgemeines Element:
\[
\xi = \xi_\infty + \sum_{\pi \in F} a_\pi \varepsilon_\pi + a_0 \varepsilon_0 + a_1 \varepsilon_1
\]
mit endlichem Pfadträger $F$. Projektionen: $P_\infty$, $P_{\mathrm{arith}}$, $P_{\mathrm{pole}}$.

---

## 10. Lokal konvexe Topologie

OX-1a definiert noch keine Hilbert-Norm. Der Rohträger erhält ausschließlich eine
natürliche lokal konvexe Topologie.

**10.1 Arithmetischer Sektor.**
\[
\mathcal{D}_{\mathrm{arith}}^{\mathrm{kin}}
:= \bigoplus_{\pi \in \mathsf{P}_{\mathrm{rel}}^{+}}^{\mathrm{lc}} A\,\varepsilon_\pi
\]
(feinste lokal konvexe Topologie, für die alle kanonischen Inklusionen
$A\,\varepsilon_\pi \hookrightarrow \mathcal{D}_{\mathrm{arith}}^{\mathrm{kin}}$ stetig sind).

**10.2 Archimedischer Sektor.**
\[
\mathcal{D}_\infty^{\mathrm{kin}}
:= \bigl(A \otimes_\pi C_c^\infty(\mathbb{R})\bigr)\varepsilon_\infty
\]
(projektive Tensorprodukttopologie; keine Hilbertraumvervollständigung).

**10.3 Polarer Sektor.** Endliche Produkttopologie auf $A\,\varepsilon_0 \oplus A\,\varepsilon_1$.

**Definition 10.4 — Topologischer Rohträger.**
\[
\boxed{
\mathcal{D}_X^{\mathrm{kin}}
:= \mathcal{D}_\infty^{\mathrm{kin}}
\oplus \mathcal{D}_{\mathrm{arith}}^{\mathrm{kin}}
\oplus \mathcal{D}_{\mathrm{pole}}^{\mathrm{kin}}
}
\]
$\mathcal{D}_X^{\mathrm{kin}}$ ist ein lokal konvexer linker $A$-Modul.
Seine Hilbertisierung ist ausdrücklich **nicht** Teil von OX-1a.

---

## 11. Kanonische kinematische Operatoren

**Definition 11.1 — Primzähloperatoren.**
Für jede Primzahl $q$: $N_q(\varepsilon_\pi) := \nu_q(\pi)\,\varepsilon_\pi$.

**Definition 11.2 — Logarithmischer Längenoperator.**
\[
\Lambda_{\mathrm{arith}}(\varepsilon_\pi) := \lambda(\pi)\,\varepsilon_\pi
= \Bigl(\sum_{q} (\log q)\,\nu_q(\pi)\Bigr)\varepsilon_\pi.
\]
Für eine Ein-Kante: $\Lambda_{\mathrm{arith}}(\varepsilon_{e_{n,p}}) = (\log p)\,\varepsilon_{e_{n,p}}$.
Für einen reinen $p$-Pfad der Länge $r$: $\Lambda_{\mathrm{arith}}(\varepsilon_{\pi_{n,p}^{(r)}}) = (r\log p)\,\varepsilon_{\pi_{n,p}^{(r)}}$.

Die Definition unterscheidet sauber zwischen dem lokalen Kanteninkrement $\log p$
und der akkumulierten Prime-Power-Zeit $r\log p$.

**Definition 11.3 — Kombinatorischer Gradoperator.**
$R(\varepsilon_\pi) := |\pi|\,\varepsilon_\pi$.

> **Bemerkung 11.4.** Keiner dieser Operatoren wird in OX-1a als symmetrisch
> oder selbstadjungiert bezeichnet. Solche Aussagen erfordern zuerst eine positive
> Form (OX-1b, OX-1c, OX-1e).

---

## 12. Quell-, Ziel- und Randabbildungen

Hilfsobjekt: $\mathcal{V}_A^{\mathrm{alg}} := \bigoplus_{n \ge 1}^{\mathrm{alg}} A\,\delta_n$.

**Definition 12.1.**
\[
s_*(a\,\varepsilon_\pi) := a\,\delta_{s(\pi)}, \qquad
t_*(a\,\varepsilon_\pi) := a\,\delta_{t(\pi)}, \qquad
\partial_{\mathrm{rel}} := t_* - s_*.
\]
Diese Abbildungen sind rein algebraisch. Es wird noch keine exakte Folge, keine
Homologie und keine geschlossene Differentialstruktur behauptet.

---

## 13. Arithmetische Trunkierungen

Für endliche Primzahlmenge $S \subset \mathbb{P}$ und $N \ge 1$:
\[
\mathsf{P}(S,N)
:= \bigl\{ \pi \in \mathsf{P}_{\mathrm{rel}}^{+} :\;
\operatorname{supp}\,\nu(\pi) \subseteq S,\;
s(\pi) \le N,\; t(\pi) \le N \bigr\}.
\]

**Definition 13.1.**
\[
\mathcal{D}_{\mathrm{arith}}(S,N)
:= \bigoplus_{\pi \in \mathsf{P}(S,N)} A\,\varepsilon_\pi.
\]
Für $S \subseteq S'$, $N \le N'$: kanonische Inklusion
$\mathcal{D}_{\mathrm{arith}}(S,N) \hookrightarrow \mathcal{D}_{\mathrm{arith}}(S',N')$.
Algebraisch:
\[
\mathcal{D}_{\mathrm{arith}}^{\mathrm{alg}}
= \varinjlim_{S,N} \mathcal{D}_{\mathrm{arith}}(S,N).
\]

> Archimedische Cutoffs werden hier nicht festgelegt; sie gehören zu OX-1d und OX-1e.

---

## 14. Symmetrien des Rohträgers

**14.1 Basisverschiebung.**
Für $k \in \mathbb{N}_{\ge 1}$: $M_k(n;\,p_1,\ldots,p_r) := (kn;\,p_1,\ldots,p_r)$.
Es gilt $\nu_q(M_k\pi) = \nu_q(\pi)$, $\lambda(M_k\pi) = \lambda(\pi)$.
Algebraische Wirkung: $M_k(a\,\varepsilon_\pi) := a\,\varepsilon_{M_k\pi}$.

**14.2 Keine Nullstellenwirkung.**
Auf $\mathcal{D}_X^{\mathrm{kin}}$ wird keine Wirkung unter Verwendung der Zahlen
$\gamma_n$ definiert. Der Rohträger ist vollständig unabhängig vom bekannten
Nullstellenspektrum.

---

## 15. Was mit OX-1a ausdrücklich nicht definiert wird

Die Definition von $\mathcal{D}_X^{\mathrm{kin}}$ enthält noch keine der folgenden Strukturen:
$B_p$, $B_{pq}$, $B_\infty$, $B_{\mathrm{pole}}$, $B_X$, Skalarprodukt,
positive semidefinite Form, Radikalquotient, Hilbertraumvervollständigung,
selbstadjungierten Operator $H_X$, Gram-Realisierung der Weil-Form,
Einbettung des Gammafaktors, Identifikation mit Nullstellenfrequenzen,
kommunikative Quotientierung der Primpfade, hebungsabhängige Fourierladung
oder vorausgesetzte RH-Positivität.

Insbesondere wird nicht definiert:
\[
\mathcal{K}_X := \overline{\mathcal{D}_X^{\mathrm{kin}} / \operatorname{Rad}(Q_W)}^{\,Q_W}.
\]

---

## 16. Gesicherte kinematische Eigenschaften

| Knoten | Aussage | Status |
|---|---|---|
| **K1** | Kollisionsfreie Primmarkierung: $e_{n,p}$ und $e_{m,q}$ bleiben als verschiedene Generatoren erhalten | `✅ [K]` |
| **K2** | Intrinsische Primzahlpotenzzeiten: $\lambda(\pi_{n,p}^{(r)}) = r\log p$ durch Komposition | `✅ [K]` |
| **K3** | Intrinsischer gemischter Träger: $\varepsilon_{(n;p,q)}$ für $p \neq q$ in $\mathcal{D}_{\mathrm{mix}}^{\mathrm{alg}}$ | `✅ [K]` |
| **K4** | Kanonische Sektorzerlegung: $\mathcal{D}_\infty^{\mathrm{alg}} \oplus \bigoplus_p \mathcal{D}_p^{\mathrm{pure}} \oplus \mathcal{D}_{\mathrm{mix}}^{\mathrm{alg}} \oplus \mathcal{D}_{\mathrm{pole}}^{\mathrm{alg}}$ | `✅ [K]` |
| **K5** | Nullstellenfreiheit: kein Bestandteil verwendet die Werte $\gamma_n$ | `✅ [K]` |
| **K6** | Keine vorweggenommene Positivität: unabhängig von der Weil-Positivität | `✅ [K]` |

---

## 17. Noch offene Fragen innerhalb von OX-1a

| Knoten | Frage |
|---|---|
| **OX-1a.1** | Geordnete oder kommutative Pfade: Sollen $(n;p,q)$ und $(n;q,p)$ durch eine kohärente Relation verbunden oder quotientiert werden? |
| **OX-1a.2** | Verträglichkeit mit der vorhandenen $A_{2D}^r$-Struktur: freier linker Modul oder Bimodul? |
| **OX-1a.3** | Archimedische Testklasse: bleibt $C_c^\infty(\mathbb{R})$ der endgültige Kern oder wird ein Schwartz-Raum bzw. Mellin-invarianter Kern benötigt? |
| **OX-1a.4** | Polarer Rang: erzwingen Funktionalgleichung und Randbedingungen einen Quotienten oder eine zusätzliche Symmetrierelation? |
| **OX-1a.5** | Topologische Vervollständigung: richtige Vervollständigung hängt von $B_p$, $B_{pq}$, $B_\infty$ ab und gehört zu OX-1e |

---

## 18. Abschlussurteil zu OX-1a

Der kinematische Rohträger ist:

\[
\boxed{
\mathcal{D}_X^{\mathrm{kin}}
= \Bigl(A_{2D}^r \otimes_\pi C_c^\infty(\mathbb{R})\Bigr)\varepsilon_\infty
\oplus \Bigl(\bigoplus_{\pi \in \mathsf{P}_{\mathrm{rel}}^{+}}^{\mathrm{lc}} A_{2D}^r\,\varepsilon_\pi\Bigr)
\oplus A_{2D}^r\,\varepsilon_0
\oplus A_{2D}^r\,\varepsilon_1.
}
\]

Der entscheidende arithmetische Bestandteil ist nicht nur die direkte Summe der
Ein-Kanten-Räume $\bigoplus_{n,p} A_{2D}^r\,\varepsilon_{e_{n,p}}$, sondern deren
**minimale markierte Pfadhülle**. Diese enthält gleichzeitig:

- lokale Primkanten ($r=1$, logarithmisches Inkrement $\log p$);
- Prime-Power-Pfade ($r \ge 2$, Zeit $r\log p$ durch Komposition);
- gemischte Primpfade (intrinsischer Träger für spätere Off-Diagonal-Gluung).

Damit sind die kinematischen Voraussetzungen für OX-1b und OX-1c vorhanden, ohne
bereits eine positive Form oder eine künstliche Off-Diagonal-Kopplung einzubauen.

Der Teilknoten OX-1a kann nach Überprüfung der Kompatibilität mit den bereits
definieren $A_{2D}^r$-Modulen definitionell geschlossen werden.

---

## Nächster Hauptknoten

\[
\boxed{
[OX\text{-}1b] \quad
\text{Konstruktion intrinsischer lokaler positiver Formen } B_p
\text{ auf den reinen } p\text{-Pfadsektoren.}
}
\]

---

*Erstellt: 2026-08-04 · Epistemischer Status: Definitionell geschlossen vorbehaltlich OX-1a.2  
Keine zirkuläre Voraussetzung eingebaut · Offene Folgefragen OX-1a.1–5 explizit gelistet*
