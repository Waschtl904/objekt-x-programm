# NEU-167b — Abschluss von [O-167-2]: Keine zusätzlichen Kernbedingungen aus NEU-157 §157.H oder NEU-44

**Status:** Atomarer Nachtrag zu NEU-167. Schließt [O-167-2] negativ.  
**Vorgänger:** NEU-167 ([O-167-1] negativ geschlossen), NEU-157 rev.3 §157.H Gl. (157.B.1), NEU-44, NEU-165a/b.  
**Abhängigkeit:** [O-157-R2] wird mitgeschlossen.

---

## Ausgangsfrage [O-167-2]

Liefern NEU-157 rev.3, §157.H, Gleichung (157.B.1), oder NEU-44 zusätzliche nichttriviale
homogen-lineare Zulässigkeitsbedingungen

$$L_{p,a}: K_p \longrightarrow Y_{p,a}, \qquad L_{p,a}(k) = 0,$$

die Fall 1 aus NEU-166b nicht-leer machen könnten?

---

## 167b.A — Audit von NEU-157 rev.3

NEU-157 §157.H definiert den präprojektiven Rohoperator (Gl. (157.B.1)):

$$T_p^{pre}(e_u V_p) := -\sum_{s,m} \ell_{s,m}\, u\, s\log(p)\, e_{u+ps}V_{pm}, \qquad u \neq 0. \tag{157.B.1}$$

Unter einer Nichtverschwindensvoraussetzung wird bewiesen:

$$T_p^{pre}(e_u V_p) \neq 0.$$

Diese Aussage betrifft das **Bild** eines Kopplungsoperators. Sie ist keine Zulässigkeitsbedingung der Form $L_{p,a}(k) = 0$ auf $K_p$.

**§157.C.4:** Die dort formulierte Bedingung

$$K_p^{allow} \subseteq \ker(C_p)$$

ist eine Faktorisierungs- bzw. Hebungsunabhängigkeitsbedingung an $C_p$ — Bedingung (4) gemäß NEU-165b. Sie erzeugt keinen unabhängigen Regularitätsoperator $L_{p,a}: K_p \to Y_{p,a}$.

**§157.E:** Die dort auftretenden Operatoren $DF_{p,\alpha}(\widehat\varepsilon_p^{\,0})$ sind basispunktabhängige Tangentialoperatoren. Sie beschreiben den linearisierten Tangentialraum am Basispunkt, nicht die exakte globale Zulässigkeitsmenge — daher keine quellenfeste Familie $\{L_{p,a}\}$ im Sinne von §157.C.1.

$$\boxed{\text{NEU-157 rev.3 liefert keinen zusätzlichen nichttrivialen }L_{p,a}\text{-Operator auf }K_p.}$$

---

## 167b.B — Audit von NEU-44

NEU-44 behandelt die Zielraum- und Korrespondenzstruktur der Kopplung:

$$\mathcal{H}_{rel,N}, \qquad \kappa: \mathcal{H}_{rel,N} \to \mathcal{H}_{J,N}, \qquad W_{res,rel}, \qquad T_{rel}, \qquad C_p^{rel}.$$

Die dort definierte kantendiagonale $W_{res}$-Paarung

$$\delta_{p,q}\,\delta_{m,m'}\,\langle E_{r,pm}, E_{r',pm}\rangle_{W_{res}}$$

ist eine Struktur auf dem **relativen Zielraum**. Sie ist keine lineare Nebenbedingung auf dem Liftvariationsraum $K_p$.

NEU-44 konstruiert insbesondere keinen Operator

$$L_{p,a}: K_p \longrightarrow Y_{p,a}$$

mit einer exakten Zulässigkeitsbedingung $L_{p,a}(k) = 0$.

$$\boxed{\text{NEU-44 liefert keinen zusätzlichen nichttrivialen }L_{p,a}\text{-Operator auf }K_p.}$$

---

## 167b.C — Entscheidung

Zusammen mit dem negativen Abschluss von [O-167-1] (NEU-167) ergibt sich für den auditierten Quellenkegel

$$\{\text{NEU-41},\ \text{NEU-44},\ \text{NEU-157 rev.3},\ \text{NEU-165a/b},\ \text{NEU-166a/b},\ \text{NEU-167}\}$$

die leere Familie:

$$\boxed{A_p = \varnothing.}$$

Daher gilt:

$$\boxed{K_p^{hom} = K_p \cap \bigcap_{a \in A_p} \ker(L_{p,a}) = K_p.}$$

Die exakte Zulässigkeit wird im auditierten Quellenkegel **nicht** durch zusätzliche homogen-lineare Kerngleichungen eingeschränkt. Sie wird stattdessen bestimmt durch:

- $P_p^{ch}(\widehat\varepsilon_p) \neq 0$ — offene Nichtverschwindensbedingung (Bedingung (2)),
- $2\operatorname{Re} h_p(\widehat\varepsilon_p^{\,0}, k) + h_p(k,k) = 0$ — quadratische $W_{res}$-Normierungsbedingung (Bedingung (3)),
- Hebungsunabhängigkeit an $C_p$ — Faktorisierungsbedingung (Bedingung (4)).

---

## 167b.D — Präzisierung: „Im auditierten Quellenkegel leer"

**Fall 1 aus NEU-166b ist im auditierten Quellenkegel leer.**

Dies bedeutet nicht, dass die Zulässigkeitsmenge $\mathcal{M}_p$ leer ist. Es bedeutet ausschließlich: Ihre exakte Struktur wird nicht durch nichttriviale homogen-lineare Kerngleichungen $\{L_{p,a}(k) = 0\}_a$ beschrieben.

Ein absolut katalogweiter Ausschluss von Fall 1 wäre nur dann gerechtfertigt, wenn dokumentiert wird, dass sämtliche übrigen Vorgänger- und Seitenknoten des DAG auf Operatoren $L_{p,a}: K_p \to Y_{p,a}$ durchsucht wurden. Für die gegenwärtige DAG-Kette reicht der quellenkegelrelative Abschluss vollständig aus.

---

## 167b.E — Vorausschau: [O-167-3] und NEU-168

[O-167-3] bleibt offen. Seine korrekte Formulierung lautet:

> Reicht die nichtlineare Zulässigkeitsarchitektur — offene Ladungsbedingung, quadratische Normierungsbedingung, Faktorisierungsbedingung — für Zeugenexistenz, Operatorverlängerung und Quotientenabstieg aus?

Die Rohzeugenmenge ist:

$$\mathcal{M}_p^{wit} = \left\{ \widehat\varepsilon_p \in \mathcal{M}_p^{ch} : G_p^{raw}(\widehat\varepsilon_p) \neq 0 \right\}.$$

Auf dem modalen Bereich faktorisiert der Rohoperator (gestützt auf NEU-157 rev.3 §157.H Gl. (157.B.1)):

$$G_p^{raw} = B_p \circ P_p^{ch},$$

wobei

$$B_p\bigl((a_u)_u\bigr) = -\sum_{u \neq 0}\sum_{s,m} a_u\, \ell_{s,m}\, u\, s\log(p)\, e_{u+ps}V_{pm}.$$

Die präziseste atomare Zeugenbedingung lautet daher:

$$\boxed{\exists\, \widehat\varepsilon_p \in \mathcal{M}_p \quad\text{mit}\quad P_p^{ch}(\widehat\varepsilon_p) \notin \ker(B_p).}$$

Äquivalent: die mengentheoretische Nichttrivialitätsbedingung

$$\boxed{\mathcal{M}_p \not\subseteq \ker(B_p \circ P_p^{ch}).}$$

**Hinweis zur Terminologie für NEU-168:** Die Ausgangsfrage von NEU-168 sollte zunächst rein mengentheoretisch formuliert werden. Der Begriff „transversal" setzt eine glatte Mannigfaltigkeitsstruktur und einen wohldefinierten Tangentialraum der vollständigen exakten Menge voraus. Erst nach einer lokalen Glattheits- oder Quadrikregularitätsanalyse darf eine transversale Verlassensaussage gemacht werden.

---

## Statusänderungen

| Punkt | Status |
|---|---|
| [O-167-2] | ✓[M] — negativ geschlossen |
| [O-157-R2] | ✓[M] — negativ geschlossen, $A_p = \varnothing$ |
| Fall 1 (NEU-166b) | Im auditierten Quellenkegel leer |
| [O-167-3] | Offen — Architekturkompatibilitätsfrage für NEU-168 |

$$\boxed{[O\text{-}167\text{-}2] \quad \checkmark[M]\text{ — negativ geschlossen}.}$$

$$\boxed{[O\text{-}157\text{-}R2] \quad \checkmark[M]\text{ — negativ geschlossen, }A_p = \varnothing.}$$

$$\boxed{\text{Fall 1 aus NEU-166b ist im auditierten Quellenkegel leer.}}$$

---

## Referenzverknüpfungen im DAG

| Blatt | Abhängigkeit |
|---|---|
| NEU-167 [O-167-1] | Primärer Vorgänger; [O-167-1] negativ geschlossen |
| NEU-157 rev.3 §157.H Gl. (157.B.1) | Auditiert: kein $L_{p,a}$ |
| NEU-44 | Auditiert: kein $L_{p,a}$ |
| NEU-165b | Klassifikation Bedingungen (1)–(4); Referenzrahmen |
| NEU-166b Fall 1 | Quellenkegelrelativ leer durch diesen Befund |
| NEU-168 | Nächster Knoten: Zeugenbedingung $\mathcal{M}_p \not\subseteq \ker(B_p \circ P_p^{ch})$ |
