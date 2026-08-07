# NEU-250j — Trägertrennung zwischen von-Mangoldt-Sektoren und Primfaserüberlappungen

**Katalog-ID:** NEU-250j  
**Vorgänger:** NEU-250i (vollständiger primitiver Koeffizient), NEU-250h (Quellenabbildung)  
**Status:** J1–J4 ✓[M]; J5 Entscheidungsbefund (J-B vorläufig, Mediatorweg J-A offen)

---

## 0. Ausgangslage und Ziel

NEU-250g–i haben die lokalen arithmetischen Gewichte $\Lambda(p^k)/\sqrt{p^k}$ vollständig aus BC-Strukturen hergeleitet. Die naheliegende Folgefrage lautete zunächst: Koppeln die bereits im Repo verankerten Graphbasisüberlappungen $K_{pq}\neq0$ (aus $2\cdot3=3\cdot2$) die lokalen Kanäle global?

Dieser Knoten zeigt, dass diese Frage eine **Trägertrennung** verlangt, bevor sie beantwortet werden kann: Die Mengen, auf denen $\Lambda(M)\neq0$ gilt, und die Mengen, auf denen Kreuzprimkollisionen $pm_p=qm_q$ möglich sind, sind **disjunkt**. Die Graphbasisüberlappung und die Weil-Koeffizientenfamilie leben strukturell auf verschiedenen Trägern.

---

## J1 — Notationsbereinigung: $k$ vs. $m$

In KONVENTIONEN.md §X.3 (Wörterbuch, verbindlich ab NEU-227) bezeichnet $m$ die **Fasernummer** in
$$
\eta_{p;m;s,u} \longleftrightarrow e_R V_M, \qquad M = pm, \qquad R = u+ps.
$$

Für den **Weil-Primzahlpotenzsektor** verwenden wir ab sofort den Exponenten $k$:
$$
\boxed{M = p^k, \qquad k \geq 1, \qquad p \text{ prim.}} \qquad (1)
$$

Die zugehörige Graphfaser für diesen Weil-Sektor ist dann
$$
\boxed{m = p^{k-1}.} \qquad (2)
$$

*Warum:* Im Wörterbuch $M = pm$ ergibt $M = p^k = p \cdot p^{k-1}$ die Faser $m = p^{k-1}$.  
Für $k=1$: $M = p$, $m = 1$ (primitive Kette, NEU-225 vollständig gerechtfertigt).  
Für $k=2$: $M = p^2$, $m = p$ (zusammengesetzte Faser, NEU-227 Warnung aktiv).  

Die Indexvariable $m$ ist damit im Folgenden **reserviert** für die Fasernummer im Graphwörterbuch; der Exponent der Primzahlpotenz heißt stets $k$.

Status: ✓[M], reine Notationsbereinigung, kein mathematischer Inhalt.

---

## J2 — Kollisionskriterium für $K_{pq}\neq0$

Nach KONVENTIONEN.md §X.3 (Überlappungsbild):
> Über verschiedene $(p,m)$ hinweg ist das Skalarprodukt generisch $\neq0$; verschiedene $(p,m)$ können dasselbe $V_{pm}$ treffen (etwa $2\cdot3=3\cdot2$). Genau diese Überlappung erzeugt $K_{pq}\neq0$ (51.5).

Präzisierung: Für $p\neq q$ tritt eine Kreuzprimkollision auf bei
$$
pm_p = qm_q = M, \qquad p\neq q. \qquad (3)
$$

Necessary and sufficient condition: Da $p \mid M$ und $q \mid M$ mit $p\neq q$, besitzt $M$ **mindestens zwei verschiedene Primteiler**:
$$
\boxed{\omega(M) \geq 2.} \qquad (4)
$$

Hier ist $\omega(M)$ die Anzahl der verschiedenen Primteiler von $M$.  
Klassische Beispiele: $M=6=2\cdot3$, $M=10=2\cdot5$, $M=12=2^2\cdot3$.

Status: ✓[M], direkte Folge aus der multiplikativen Struktur von $\mathbb{N}$.

---

## J3 — Von-Mangoldt-Trägertrennung (Hauptsatz)

**Satz (Trägertrennung):**
$$
\omega(M) \geq 2 \implies \Lambda(M) = 0. \qquad (5)
$$

*Beweis:* Die von-Mangoldt-Funktion ist
$$
\Lambda(M) = \begin{cases} \log p & M = p^k,\ p\text{ prim},\ k\geq1 \\ 0 & \text{sonst.} \end{cases}
$$
Wenn $\omega(M) \geq 2$, besitzt $M$ mindestens zwei verschiedene Primteiler; $M$ ist also keine Primzahlpotenz. Damit $\Lambda(M) = 0$. $\square$

Die Umkehrung ist ebenso klar: $\Lambda(M) \neq 0 \implies M = p^k \implies \omega(M) = 1$, also existiert kein zweiter Primteiler $q\neq p$ mit $q\mid M$. Es gibt daher keine Darstellung $M = qm_q$ mit $q\neq p$.

**Korollar (disjunkte Träger):**
$$
\boxed{\operatorname{supp}\Lambda \cap \operatorname{supp}(\text{Kreuzprimkollision}) = \varnothing.} \qquad (6)
$$

Die natürliche Zerlegung des Monoids $\mathbb{N}_{\geq2}$ lautet:
$$
\mathbb{N}_{\geq2} = \underbrace{\mathcal{P}^*}_{\Lambda\neq0} \sqcup \underbrace{\mathcal{M}}_{\omega(M)\geq2,\ \Lambda=0}, \qquad (7)
$$
wobei $\mathcal{P}^* = \{p^k : p\text{ prim},\ k\geq1\}$.

| Sektor | $\Lambda(M)$ | $p\neq q$-Kollision möglich | $D_{\rm rel}$-Eigenvektor |
|---|---|---|---|
| $M=p^k\in\mathcal{P}^*$ | $\log p\neq0$ | nein | nein (kein Eigenwert) |
| $M\in\mathcal{M}$, $\omega(M)\geq2$ | $0$ | ja | nein (kein Eigenwert) |

Status: ✓[M], elementare Zahlentheorie; keine neuen Konstruktionen benötigt.

---

## J4 — Dynamischer Firewall-Test: Ist $\mathcal{H}_{\mathcal{P}^*}$ invariant unter $D_{\rm rel}$ und $\Theta$?

Nach KONVENTIONEN.md §X.3 (Wörterbuch, Θ-Faser-Invarianz):
> $\Theta\eta_{p;m;r,u} = \sum_{n\mid m}\alpha_n r\,\eta_{p;m;r+n,u}$, wobei $p$ unbewegt bleibt und die Faser $m$ invariant ist.

Das hat zwei unmittelbare Konsequenzen:

**Θ bewegt $m$ nicht.** Ein Vektor $\eta_{p;m;r,u}$ mit Fasernummer $m = p^{k-1}$ (Weil-Primzahlpotenzsektor $M=p^k$) wird von $\Theta$ ausschließlich zu Vektoren $\eta_{p;m;r+n,u}$ mit **derselben** Faser $m=p^{k-1}$ und **demselben** Primkanal $p$ transportiert.

**Θ mischt keine Primkanäle.** Ein Basisvektor im $p$-Kanal ($\eta_{p;\cdot;\cdot;\cdot}$) wird durch $\Theta$ nicht in einen $q$-Kanal ($q\neq p$) transportiert, da $p$ verbindlich unbewegt ist.

Da $D_{\rm rel} = \overline{iJ^-}$ mit $J^- = \frac12(\Theta - \Theta^\dagger)$ (KONVENTIONEN.md §X.3, 37.1) und $\Theta^\dagger$ dieselbe Faserstruktur respektiert:
$$
\boxed{D_{\rm rel}:\mathcal{H}_{\mathcal{P}^*} \longrightarrow \mathcal{H}_{\mathcal{P}^*} \quad \text{(primkanalinvariant).}} \qquad (8)
$$

Nach KONVENTIONEN.md §X.3 hat $D_{\rm rel}$ **keine Eigenwerte** (NEU-225, 52.D0). Die Spektralwirkung ist ausschließlich über das projektionswertige Spektralmaß $E_{D_{\rm rel}}$ und die Kreuzspektralmaße $\mu^{a,b}_{pq}$ zu formulieren.

**Befund:** Die bisherige Dynamik ($\Theta$, $D_{\rm rel}$) transportiert Vektoren in $\mathcal{H}_{\mathcal{P}^*}$ nicht in den Mischsektor $\mathcal{H}_{\mathcal{M}}$. Die Graphbasisüberlappung $K_{pq}\neq0$ entsteht aus der Geometrie des gesamten Graphraums, betrifft aber den Weil-Träger $\mathcal{P}^*$ strukturell nicht.

$$
\boxed{K_{pq}\neq0\text{ im gesamten Graphraum} \not\Rightarrow K_{pq}\neq0\text{ auf }\mathcal{H}_{\mathcal{P}^*}.} \qquad (9)
$$

Status: ✓[M], direkte Anwendung von KONVENTIONEN.md §X.3 (Θ-Faser-Invarianz + Spektralmaßwarnung).

---

## J5 — Harte Entscheidung: J-A oder J-B?

### Konditionale Ausgangslage

J4 hat gezeigt: Die Graphbasisüberlappung $K_{pq}\neq0$ aus $2\cdot3=3\cdot2$ liegt auf $\mathcal{M}$ (nicht auf $\mathcal{P}^*$), und die vorhandene Dynamik $\Theta/D_{\rm rel}$ transportiert nicht zwischen $\mathcal{H}_{\mathcal{P}^*}$ und $\mathcal{H}_{\mathcal{M}}$. Damit stellt sich die Frage: Existiert eine *andere* kanonische Quelle im Repo, die $\mathcal{H}_{\mathcal{P}^*}\leftrightarrow\mathcal{H}_{\mathcal{M}}$ verbindet?

### Ausgang J-B (vorläufig aktiv)

Nach aktuellem Repositorystand (KONVENTIONEN.md, NEU-225, NEU-226, NEU-227, NEU-228) existiert kein solcher Operator. Es gibt:
- kein kanonisches Bild von $V_{p^k}$ in einen Mischsektor,
- keine Darstellung der Kreuzspektralmaße $\mu^{a,b}_{pq}$ als Transfer zwischen $\mathcal{P}^*$ und $\mathcal{M}$,
- keine adelische Faltung oder Quellenkarte, die $\mathcal{H}_{\mathcal{P}^*}\to\mathcal{H}_{\mathcal{M}}$ erzwingt.

$$
\boxed{\text{Die Graphbasisüberlappung aus }2\cdot3=3\cdot2\text{ ist nicht die gesuchte globale Objekt-X-Kopplung.}} \qquad (\text{J-B})
$$

### Ausgang J-A (offen, nicht widerlegt)

Denkbar ist ein **Mediatorweg**:
$$
\mathcal{H}_{\mathcal{P}^*} \to \mathcal{H}_{\mathcal{M}} \to \mathcal{H}_{\mathcal{P}^*}, \qquad (10)
$$
wobei $\mathcal{H}_{\mathcal{M}}$ als geometrischer Mediatorraum dient, ohne selbst einen diagonalen Weil-Koeffizienten zu tragen. Diese Möglichkeit wäre hochinteressant: Die Mischsektoren $\mathcal{M}$ könnten Off-Diagonalgeometrie für eine globale Kopplung liefern, ohne $\Lambda$-Gewichte zu tragen.

Voraussetzungen für J-A:
1. Existenz eines Operators $F: \mathcal{H}_{\mathcal{P}^*} \to \mathcal{H}_{\mathcal{M}}$, der aus vorhandenen Repo-Strukturen stammt (Kandidat: adelisches Quellenbild $\mathcal{S}_{\rm adel}$, nichtorthogonale globale Faktorisierung).
2. Kompatibilität mit der KMS-Dynamik und der Zeitentwicklung $[H,\mu_n]=+\log(n)\mu_n$.
3. Keine Verletzung der Spektralmaßbedingung von KONVENTIONEN.md §X.3.

J-A ist **nicht widerlegt**, aber auch nicht konstruiert. Ein eigener Knoten (NEU-250k oder $\mathcal{S}_{\rm adel}$-Knoten) wäre der nächste Schritt.

---

## Strukturbild und Implikation für das Gesamtprogramm

NEU-250g–i haben erklärt: **woher die richtigen lokalen arithmetischen Gewichte kommen.**  
NEU-250j entscheidet: **ob die vorhandene Graphgeometrie diese Kanäle global koppeln kann.**

Das strukturelle Bild ist:

$$
\begin{array}{c|c|c|c}
\text{Sektor} & \Lambda(M) & K_{pq}\text{-Kollision} & \Theta/D_{\rm rel}\text{-Transport}\\
\hline
M=p^k & \log p & \text{nein} & \text{nur innerhalb }p\text{-Kanal}\\
M\in\mathcal{M},\,\omega(M)\ge2 & 0 & \text{ja} & \text{möglich, ohne }Λ\text{-Gewicht}
\end{array}
$$

Die lokale Arithmetik (NEU-250g–i) und die globale Nichtorthogonalität (NEU-226, $K_{pq}$) leben strukturell auf **disjunkten Trägern**. Das erklärt, warum beide Eigenschaften im bisherigen Programmverlauf in verschiedenen Konstruktionsteilen aufgetaucht sind.

**Konsequenz für das Gesamtprogramm:** Die gesuchte globale Kopplung kann nicht allein aus der Graphbasisüberlappung $2\cdot3=3\cdot2$ gewonnen werden. Als Kandidaten für den nächsten Knoten verbleiben:
- adelisches Quellenbild $\mathcal{S}_{\rm adel}$ (bereits motiviert),
- nichtorthogonale Faktorisierung über $\mathcal{H}_{\mathcal{M}}$ als Mediatorraum (J-A, offen),
- $W_\infty$-Kopplung als archimedischer Beitrag (H3 aus NEU-250h, nach wie vor offen).

---

## Knotentabelle

| Schritt | Inhalt | Status |
|---|---|---|
| J1 | Notation: $M=p^k$ (Weil), $m=p^{k-1}$ (Faser); Trennung $k$ vs. $m$ | ✓[M] |
| J2 | Kollisionskriterium: $pm_p=qm_q,\ p\neq q \Leftrightarrow \omega(M)\geq2$ | ✓[M] |
| J3 | Trägertrennung: $\operatorname{supp}\Lambda \cap \operatorname{supp}(K_{pq}\text{-Kollision})=\varnothing$ | ✓[M] |
| J4 | Dynamischer Firewall: $\Theta/D_{\rm rel}$ primkanalinvariant, $K_{pq}$ nicht auf $\mathcal{P}^*$ | ✓[M] |
| J5-B | Graphbasisüberlappung ist nicht die Objekt-X-Kopplung | ✓[M]$_{\rm neg}$ (vorläufig) |
| J5-A | Mediatorweg $\mathcal{H}_{\mathcal{P}^*}\to\mathcal{H}_{\mathcal{M}}\to\mathcal{H}_{\mathcal{P}^*}$ über $\mathcal{S}_{\rm adel}$ | offen |

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| KONVENTIONEN.md §X.3 | Θ-Faser-Invarianz; $K_{pq}\neq0$-Überlappungsbild; Spektralmaßwarnung |
| NEU-250i (73153ee) | Vollständiger primitiver Koeffizient $\Lambda(p^k)/\sqrt{p^k}$ auf $\mathcal{P}^*$ |
| NEU-226 (0d22c9f) | Globaler Feshbach-Transfer, Schattenklasse, $K_{pq}$-Primkanalüberlappung |
| NEU-227 (921e458) | Koordinatenwörterbuch; Kreuzspektralmaße $\mu^{a,b}_{pq}$ |
| NEU-225 (68beb9c) | $D_{\rm rel}$ hat keine Eigenwerte (52.D0); Primfaserdiagonalisierung |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/objekt-x-programm.*
