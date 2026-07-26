# NEU-165 — Import der $R_{p,j}$-Wirkung: Matrixstruktur, Basisnullmengen und gemeinsamer Kern

## Status

$$\boxed{\ ?[O]\ }$$

Ziel dieses Blattes ist zunächst kein vorweggenommener Existenz- oder Leerheitsbeweis, sondern ein vollständiger **Strukturbericht**:

- explizite Wirkungsformel für jedes relevante $R_{p,j}$,
- Bestimmung der Basisnullmengen,
- Entscheidung der Diagonalitätsfrage,
- Berechnung des vollständigen gemeinsamen Kerns,
- Prüfung des speziellen Kandidaten $e_{1-p}V_p$.

Ein Status $\checkmark[M]$ ist erst dann zulässig, wenn die importierten Formeln tatsächlich aus den früheren Blättern abgelesen und die daraus folgenden Kernbedingungen vollständig bewiesen wurden.

---

## 165.A — Eingaben und Quellenabgleich

### 165.A.1 — Relevante Eingaben

Die Untersuchung verwendet:

- **NEU-157**: Definition des linearen Zulässigkeitsraums und der Nebenbedingungsoperatoren $R_{p,j}$;
- **NEU-159**: Mitgliedschafts- bzw. Dualzeugenkriterium;
- **NEU-164 rev.2**: Entscheidungsknoten für den Basiszeugen $e_{1-p}V_p$;
- ggf. **NEU-155/156**: Rückbindung an $C_p^{\mathrm{rel}}$, $T_p$ und die Residualform;
- **OP-4.1**: erst beim abschließenden Positivitäts- oder Nichtverschwindungsschritt.

### 165.A.2 — Quellenwarnung

Vor dem eigentlichen Import ist festzustellen, in welchem Blatt die Operatoren $R_{p,j}$ **tatsächlich** definiert werden.

NEU-159 scheint nach dem gegenwärtigen Architekturstand primär ein Mitgliedschafts- bzw. Dualzeugenblatt zu sein. Falls die eigentliche Definition von $R_{p,j}$ bereits in NEU-157 oder einem früheren Blatt steht, muss NEU-165 genau diese Quelle nennen.

Die Positivität aus OP-4.1 ist für die Berechnung von $R_{p,j}(e_uV_p)$ **nicht** erforderlich. Sie darf erst importiert werden, nachdem ein zulässiger Vektor mit nichtverschwindendem Bild konstruiert wurde.

---

## 165.B — Typendisziplin: Indexmenge versus Vektorraum

Setze
$$\varepsilon_{p,u} := e_u V_p.$$

Sei $I_p$ die Menge derjenigen Indizes $u \neq 0$, für welche
$$\varepsilon_{p,u} \in \mathcal{E}_p^{\mathrm{ch}} \cap \bigcap_j \operatorname{dom}(R_{p,j})$$
gilt.

Der **vollständige lineare Zulässigkeitsraum** ist
$$\mathcal{E}_p^{\mathrm{adm}} := \mathcal{E}_p^{\mathrm{ch}} \cap \ker(\pi_{\mathrm{prim}}) \cap \bigcap_j \ker(R_{p,j}).$$

Davon ist die **Menge der zulässigen Basisindizes** zu unterscheiden:
$$I_p^{\mathrm{adm}} := \left\{ u \in I_p : \varepsilon_{p,u} \in \mathcal{E}_p^{\mathrm{adm}} \right\}.$$

Damit gilt:
$$I_p^{\mathrm{adm}} \quad \text{ist eine Indexmenge},$$
während
$$\mathcal{E}_p^{\mathrm{adm}} \quad \text{ein Vektorraum ist.}$$

Insbesondere ist der Ausdruck
$$\bigcap_j N_j \cap \ker(\pi_{\mathrm{prim}}) \cap \mathcal{E}_p^{\mathrm{ch}}$$
**typwidrig**, wenn $N_j$ Mengen von Indizes $u$ sind.

Falls aus NEU-41 bereits gesichert ist, dass
$$\pi_{\mathrm{prim}}(e_u V_p) = 0 \qquad (u \neq 0),$$
ist die Primärbedingung für einzelne Basisvektoren automatisch erfüllt. Sie bleibt dennoch Bestandteil der Definition des vollständigen Vektorraums.

---

## 165.C — Allgemeine Matrixdarstellung

Für jeden relevanten Index $j$ sind zunächst Definitionsbereich und Zielraum festzuhalten:
$$R_{p,j} : \operatorname{dom}(R_{p,j}) \subseteq \mathcal{E}_p^{\mathrm{ch}} \longrightarrow Y_{p,j}.$$

Nach Wahl einer geeigneten linear unabhängigen Familie
$$\{\eta_{p,j,v}\}_{v \in J_{p,j}} \subseteq Y_{p,j}$$
ist die Wirkung in der Form
$$R_{p,j}(\varepsilon_{p,u}) = \sum_{v \in J_{p,j}} r_{p,j}(v,u)\, \eta_{p,j,v}$$
zu schreiben.

Die Koeffizienten $r_{p,j}(v,u)$ bilden die vollständige **Strukturmatrix** des Operators auf dem betrachteten Basisraum.

Erst aus dieser Matrix darf entschieden werden, welcher Strukturfall vorliegt.

---

## 165.D — Strukturklassifikation

### 165.D.1 — Diagonalfall

Der Operator ist auf der Familie $\{\varepsilon_{p,u}\}$ **diagonal**, wenn
$$R_{p,j}(\varepsilon_{p,u}) = \lambda_{p,j}(u)\, \varepsilon_{p,u}$$
oder, bei abweichendem Zielraum, wenigstens
$$R_{p,j}(\varepsilon_{p,u}) = \lambda_{p,j}(u)\, \eta_{p,j,u}$$
mit einer linear unabhängigen Familie $\{\eta_{p,j,u}\}_u$ gilt.

Dann **entkoppeln** die einzelnen Indizes $u$.

### 165.D.2 — Rang-eins- oder projektiver Fall

Es kann eine Darstellung
$$R_{p,j}(x) = \ell_{p,j}(x)\, \psi_{p,j}$$
vorliegen. Für Basisvektoren folgt dann
$$R_{p,j}(\varepsilon_{p,u}) = \ell_{p,j}(\varepsilon_{p,u})\, \psi_{p,j}.$$

Hier können lineare Kombinationen im Kern liegen, **obwohl kein einzelner Basisvektor im Kern liegt**.

### 165.D.3 — Gemischter Fall

Im allgemeinen Fall treten mehrere Ausgangskomponenten auf:
$$R_{p,j}(\varepsilon_{p,u}) = \sum_v r_{p,j}(v,u)\, \eta_{p,j,v}.$$

Der gemeinsame Kern wird dann durch ein gekoppeltes lineares Gleichungssystem bestimmt.

### 165.D.4 — Arithmetische Abhängigkeit ist kein eigener Strukturfall

Eine polynomiale, kombinatorische oder charaktertheoretische Abhängigkeit von $u$ ist keine vierte Operatorstruktur.

Sie kann vielmehr **innerhalb jedes der drei Fälle** auftreten, etwa als
$$\lambda_{p,j}(u) = P_{p,j}(u),$$
als
$$\ell_{p,j}(\varepsilon_{p,u}) = \chi_j(u) - 1$$
oder als arithmetische Formel für die Matrixeinträge $r_{p,j}(v,u)$.

---

## 165.E — Basisnullmengen

Für jeden Operator definiere die **Basisnullmenge**
$$N_{p,j}^{\mathrm{bas}} := \left\{ u \in I_p : R_{p,j}(\varepsilon_{p,u}) = 0 \right\}.$$

Dann ist die Menge der Basisindizes, welche sämtliche Nebenbedingungen erfüllen,
$$I_p^{\mathrm{adm}} = \bigcap_j N_{p,j}^{\mathrm{bas}},$$
sofern die Bedingungen $\varepsilon_{p,u} \in \mathcal{E}_p^{\mathrm{ch}}$ und $\pi_{\mathrm{prim}}(\varepsilon_{p,u}) = 0$ bereits in der Definition von $I_p$ enthalten bzw. für $u \neq 0$ automatisch erfüllt sind.

Diese Gleichung beschreibt ausschließlich die **zulässigen einzelnen Basisvektoren**. Sie beschreibt im nichtdiagonalen Fall noch **nicht** den vollständigen Raum $\mathcal{E}_p^{\mathrm{adm}}$.

---

## 165.F — Vollständiger Kern für lineare Kombinationen

Sei
$$x = \sum_{u \in F} a_u\, \varepsilon_{p,u}, \qquad F \subset I_p\ \text{endlich}.$$

Dann gilt
$$R_{p,j}(x) = \sum_v \left( \sum_{u \in F} r_{p,j}(v,u)\, a_u \right) \eta_{p,j,v}.$$

Wegen der linearen Unabhängigkeit der Zielfamilie ist $R_{p,j}(x) = 0$ äquivalent zu
$$\sum_{u \in F} r_{p,j}(v,u)\, a_u = 0 \quad \text{für alle } v.$$

Der vollständige gemeinsame Kern auf dem algebraischen Basisraum ist daher
$$\left\{ (a_u)_u : \sum_u r_{p,j}(v,u)\, a_u = 0 \ \text{für alle } j, v \right\}.$$

Damit ist die **zentrale logische Trennung**:

$$I_p^{\mathrm{adm}} = \varnothing$$

bedeutet zunächst nur: **Kein einzelner Basisvektor erfüllt alle Nebenbedingungen.**

Daraus folgt im Allgemeinen **nicht**
$$\mathcal{E}_p^{\mathrm{adm}} = \{0\}.$$

Lineare Auslöschung zwischen verschiedenen Indizes bleibt möglich.

---

## 165.G — Diagonalitätslemma

**Lemma 165.G.1**

Sei
$$B_p^{\mathrm{alg}} := \operatorname{span}\{\varepsilon_{p,u}\}_{u \in I_p},$$
wobei die Familie $\{\varepsilon_{p,u}\}_{u \in I_p}$ linear unabhängig sei.

Angenommen, für alle $j$ und $u$ gilt
$$R_{p,j}(\varepsilon_{p,u}) = \lambda_{p,j}(u)\, \eta_{p,j,u},$$
wobei für jedes feste $j$ die Familie $\{\eta_{p,j,u}\}_{u \in I_p}$ linear unabhängig ist.

Dann gilt
$$\ker\!\left(\bigoplus_j R_{p,j}\right) \cap B_p^{\mathrm{alg}} = \operatorname{span}\left\{ \varepsilon_{p,u} : \lambda_{p,j}(u) = 0 \text{ für alle } j \right\}.$$

**Beweis**

Für $x = \sum_{u \in F} a_u\, \varepsilon_{p,u}$ gilt
$$R_{p,j}(x) = \sum_{u \in F} a_u\, \lambda_{p,j}(u)\, \eta_{p,j,u}.$$

Aus der linearen Unabhängigkeit der Zielfamilie folgt
$$R_{p,j}(x) = 0 \iff a_u\, \lambda_{p,j}(u) = 0 \quad \text{für alle } u.$$

Gelten sämtliche Gleichungen für alle $j$, so kann $a_u \neq 0$ nur für solche Indizes auftreten, für die $\lambda_{p,j}(u) = 0$ für alle $j$ gilt. Damit folgt die Behauptung. $\square$

**Folgerung 165.G.2**

Ist
$$\bigcap_j N_{p,j}^{\mathrm{bas}} = \varnothing$$
und ist die gemeinsame Diagonalstruktur im Sinn von Lemma 165.G.1 bewiesen, dann gilt
$$\mathcal{E}_p^{\mathrm{adm}} \cap B_p^{\mathrm{alg}} = \{0\}.$$

In diesem Fall existiert im betrachteten algebraischen Basisraum **auch kein linear kombinierter Zeuge**.

Für eine Hilbertraumvervollständigung ist zusätzlich zu prüfen, dass die Operatoren geschlossen bzw. gemeinsam diagonal realisiert sind und die koordinatenweise Argumentation auch für unendliche Reihen zulässig bleibt.

---

## 165.H — Konkreter Importauftrag

Für jeden relevanten Operator $R_{p,j}$ sind die folgenden Punkte abzuarbeiten.

### 165.H.1 — Definition

Notiere die exakte Definition von $R_{p,j}$ einschließlich Definitionsbereich, Zielraum und aller Regularitäts- oder Konvergenzbedingungen.

### 165.H.2 — Wirkung auf einem festen Basisvektor

Berechne für allgemeines $u \neq 0$
$$R_{p,j}(e_u V_p).$$

Der Ausdruck ist vollständig zu vereinfachen. Insbesondere sind alle Abhängigkeiten von $u$, $p$, $j$ sichtbar zu halten.

### 165.H.3 — Matrixträger

Bestimme $\operatorname{supp}_v r_{p,j}(v,u)$. Damit wird entschieden, ob ein einzelner Eingangsindex $u$

- genau eine Zielkomponente,
- eine von $u$ unabhängige Zielrichtung, oder
- mehrere Zielkomponenten

erzeugt.

### 165.H.4 — Basisnullmenge

Bestimme
$$N_{p,j}^{\mathrm{bas}} = \{u : R_{p,j}(e_u V_p) = 0\}.$$

### 165.H.5 — Diagonalitätsentscheidung

Klassifiziere $R_{p,j}$ als **diagonal**, **rang-eins/projektiv** oder **gemischt**.

Die bloße Tatsache, dass der Koeffizient arithmetisch von $u$ abhängt, genügt **nicht** als Diagonalitätsnachweis.

### 165.H.6 — Gemeinsamer Kern

Nach dem Import sämtlicher $j$ ist entweder $\bigcap_j N_{p,j}^{\mathrm{bas}}$ zu berechnen oder, im nichtdiagonalen Fall, das vollständige Gleichungssystem
$$\sum_u r_{p,j}(v,u)\, a_u = 0 \quad \text{für alle } j, v$$
zu lösen.

---

## 165.I — Vorrangiger Testindex $u = 1-p$

Der in NEU-164 rev.2 ausgezeichnete Kandidat ist
$$\varepsilon_{p,1-p} = e_{1-p} V_p.$$

Für jeden $j$ ist separat zu prüfen:
$$R_{p,j}(e_{1-p} V_p) = 0.$$

Damit erhält man die endliche oder abzählbare Testliste
$$e_{1-p} V_p \in \mathcal{E}_p^{\mathrm{adm}} \iff \begin{cases} e_{1-p} V_p \in \mathcal{E}_p^{\mathrm{ch}}, \\[2mm] \pi_{\mathrm{prim}}(e_{1-p} V_p) = 0, \\[2mm] R_{p,j}(e_{1-p} V_p) = 0 \quad \text{für alle } j. \end{cases}$$

Die bloße Mitgliedschaft $e_{1-p} V_p \in \mathcal{E}_p^{\mathrm{adm}}$ beweist **noch nicht automatisch** $Q_p^{\mathrm{rel}} \neq 0$.

Für diesen Schluss muss zusätzlich die in NEU-164 verwendete Nichtverschwindungsbedingung verifiziert sein, beispielsweise
$$T_p(e_{1-p} V_p) \neq 0$$
oder die entsprechende positive Residualnorm
$$\left\langle T_p(e_{1-p} V_p),\, T_p(e_{1-p} V_p) \right\rangle_{W^{\mathrm{res}}} > 0.$$

Falls NEU-164 genau diesen letzten Schritt bereits unter expliziten Voraussetzungen beweist, sind diese Voraussetzungen hier wörtlich zu importieren.

---

## 165.J — Korrigierte Fallverzweigung

### Fall A — Der spezielle Basiszeuge funktioniert

Es gilt $e_{1-p} V_p \in \mathcal{E}_p^{\mathrm{adm}}$ und zusätzlich $T_p(e_{1-p} V_p) \neq 0$.

Dann folgt unter den Positivitätsvoraussetzungen aus NEU-164 bzw. OP-4.1:
$$Q_p^{\mathrm{rel}} \neq 0.$$

Status: $\checkmark[M]$ sofern alle Importschritte vollständig bewiesen sind.

### Fall B — Ein anderer Basiszeuge funktioniert

Es gilt $I_p^{\mathrm{adm}} \neq \varnothing$, $1-p \notin I_p^{\mathrm{adm}}$.

Dann wähle $u_* \in I_p^{\mathrm{adm}}$ und prüfe separat $T_p(e_{u_*} V_p) \neq 0$.

Die bloße Zulässigkeit reicht auch hier nicht aus, wenn $T_p$ den Kandidaten annihilieren könnte.

### Fall C — Keine gemeinsamen Basisnullstellen, gemeinsame Diagonalität bewiesen

Es gilt $I_p^{\mathrm{adm}} = \varnothing$ **und** zugleich die gemeinsame Diagonalstruktur aus Lemma 165.G.1.

Dann folgt
$$\mathcal{E}_p^{\mathrm{adm}} \cap B_p^{\mathrm{alg}} = \{0\}.$$

Damit ist nicht nur der einzelne Basiszeugenweg, sondern **der gesamte Weg über lineare Kombinationen** innerhalb dieses Basisraums geschlossen.

Ein „Rückfall auf einen linear kombinierten Zeugen" ist in diesem Fall logisch ausgeschlossen.

### Fall C' — Keine Basisnullstelle, Diagonalität nicht bewiesen

Es gilt $I_p^{\mathrm{adm}} = \varnothing$, aber mindestens ein $R_{p,j}$ ist projektiv, gemischt oder strukturell noch nicht bestimmt.

Dann ist der Basistest nicht entscheidend. Es muss das vollständige System
$$\sum_u r_{p,j}(v,u)\, a_u = 0$$
untersucht werden.

Dieser Fall führt zu einem eigenen Kernblatt: **NEU-165b oder NEU-166: gekoppelter gemeinsamer Kern der $R_{p,j}$**.

### Fall D — Nichtdiagonaler linear kombinierter Zeuge

Es gilt $I_p^{\mathrm{adm}} = \varnothing$, aber das gekoppelte System besitzt eine nichttriviale Lösung $(a_u)_u \neq 0$.

Dann liefert $x = \sum_u a_u e_u V_p$ einen zulässigen linearen Zeugen. Anschließend ist zu prüfen: $T_p(x) \neq 0$.

### Fall E — Vollständiger Kern trivial

Die vollständige Matrixanalyse ergibt $\mathcal{E}_p^{\mathrm{adm}} = \{0\}$.

Dann kollabiert der gesamte durch diese Nebenbedingungen definierte Zeugenraum. Die Architektur muss entweder

- die Definition von $\mathcal{E}_p^{\mathrm{adm}}$,
- die Wahl der Nebenbedingungen $R_{p,j}$, oder
- den zugrunde gelegten charakteristischen Teilraum

revidieren.

---

## 165.K — Minimaler erster Rechenschritt

Der epistemisch sauberste Einstieg besteht in der Wahl eines einzelnen, konkret definierten Operators $R_{p,j_0}$.

Zu berechnen ist:
$$R_{p,j_0}(e_u V_p) \quad \text{für allgemeines } u \neq 0.$$

Danach sind unmittelbar festzuhalten:
$$r_{p,j_0}(v,u), \qquad N_{p,j_0}^{\mathrm{bas}}, \qquad \operatorname{supp}_v r_{p,j_0}(v,u),$$
sowie die Klassifikation **diagonal / projektiv / gemischt**.

Dieser erste vollständig importierte Einzelfall entscheidet, ob die weitere Untersuchung über gemeinsame Nullstellen oder über ein gekoppeltes lineares Gleichungssystem fortgeführt werden muss.

---

## 165.L — Ergebnisformular

Nach Abschluss des Imports ist für jeden $j$ eine Tabellenzeile auszufüllen:

| Operator | Definitionsbereich | Formel für $R_{p,j}(e_u V_p)$ | Struktur | $N_{p,j}^{\mathrm{bas}}$ |
|---|---|---|---|---|
| $R_{p,j}$ | | | diagonal / projektiv / gemischt | |

Anschließend:
$$\bigcap_j N_{p,j}^{\mathrm{bas}} = \boxed{\phantom{\varnothing}}$$
und
$$\mathcal{E}_p^{\mathrm{adm}} \cap B_p^{\mathrm{alg}} = \boxed{\phantom{\{0\}}}.$$

Abschließend ist einer der Fälle **A–E** ausdrücklich zu markieren.

---

## Offene Aufgaben

$$\boxed{\text{[O-165-1]}}$$
Exakte Quellstelle und Definition jedes $R_{p,j}$ bestimmen.

$$\boxed{\text{[O-165-2]}}$$
Für jedes $j$ die Formel $R_{p,j}(e_u V_p)$ importieren.

$$\boxed{\text{[O-165-3]}}$$
Gemeinsame Diagonalität beweisen oder widerlegen.

$$\boxed{\text{[O-165-4]}}$$
Basisindexmenge $I_p^{\mathrm{adm}}$ berechnen.

$$\boxed{\text{[O-165-5]}}$$
Im nichtdiagonalen Fall den vollständigen gemeinsamen Kern bestimmen.

$$\boxed{\text{[O-165-6]}}$$
Für jeden gefundenen zulässigen Zeugen $x$ zusätzlich $T_p(x) \neq 0$ bzw. die erforderliche Positivitätsaussage beweisen.

---

**Drei vermiedene Überbehauptungen:**
$I_p^{\mathrm{adm}} = \varnothing$ bedeutet **nicht** automatisch $\mathcal{E}_p^{\mathrm{adm}} = \{0\}$; im bewiesenen Diagonalfall gibt es **keinen** Rückfall auf Kombinationen; und Zulässigkeit allein beweist **noch nicht** $Q_p^{\mathrm{rel}} \neq 0$, solange die Nichtvernichtung durch $T_p$ nicht feststeht.
