# NEU-200 — Reguläre Potentiale sind im Quotienten unsichtbar

## Vorbemerkung und Einordnung

Der Test mit Charakteristikfunktionen offener Untergruppen (Abschnitt 199.G/199.I) ist vollständig entscheidbar und liefert einen negativen Quotientenbefund, der sich auf **alle** global regulären Potentiale $H \in B$ verallgemeinert. Dieser Knoten schließt damit den regulären Untersektor von [O-199-3] ab und benennt exakt, welche Art von $H$ als nächstes benötigt wird.

Vorgelagerte Kette: $\text{NEU-196} \to \text{NEU-197} \to \text{NEU-198} \to \text{NEU-199} \to \text{NEU-200}.$

---

## 1. Allgemeiner Verschwindungssatz für $H \in B$

Sei $H \in B = \operatorname{LC}(\widehat{\mathbb Z})$ bereits auf ganz $\widehat{\mathbb Z}$ lokal konstant (also **regulär**, nicht nur punktiert). Für das teilerfremde Primtupel $\mathbf p = (p_1,p_2,p_3,p_4)$, $P = p_1p_2p_3p_4$, lautet der Koeffizient aus NEU-199 (199.18):
$$G_i^H = \alpha_P(H) - \alpha_{P/p_i}(H).$$

Wegen der Kommutativität der Skalierungswirkungen gilt:
$$\begin{aligned} G_i^H &= \alpha_{P/p_i}\bigl(\alpha_{p_i}(H)-H\bigr)\\ &= -(1-\alpha_{p_i})\,\alpha_{P/p_i}(H). \end{aligned}$$

Da $H \in B$, liegt auch $-\alpha_{P/p_i}(H) \in B$. Somit:
$$\boxed{G_i^H \in (1-\alpha_{p_i})B \subseteq \sum_{j=1}^4(1-\alpha_{p_j})B.} \tag{200.1}$$

Folglich verschwindet die Quotientenklasse:
$$\boxed{[G_i^H] = 0 \quad\text{in}\quad \frac{B}{\sum_{j=1}^4(1-\alpha_{p_j})B}.} \tag{200.2}$$

Das gilt für **jedes** global reguläre Potential, nicht nur für ein Beispiel.

---

## 2. Expliziter Kommutatorzeuge

Das Zielelement ist $Y_{g,H,\mathbf p,i} = \mu_{mP}G_i^H\mu_n^*$. Setze
$$a_{i,H} := -\mu_{mP/p_i}\,\alpha_{P/p_i}(H)\,\mu_n^* \in A_{gP/p_i}.$$

Dann liefert die Kommutatorformel aus NEU-199 (199.19):
$$[\mu_{p_i}, a_{i,H}] = \mu_{mP}\bigl(-\alpha_{P/p_i}(H) + \alpha_P(H)\bigr)\mu_n^* = Y_{g,H,\mathbf p,i}.$$

Also explizit:
$$\boxed{Y_{g,H,\mathbf p,i} = [\mu_{p_i}, a_{i,H}] \in [\mu_{p_i}, A_{gP/p_i}] \subseteq \mathcal C_{gP,\mathbf p}.} \tag{200.3}$$

Damit gilt:
$$\boxed{\overline\Theta_{g,\mathbf p,i}([D_g^H]) = 0.} \tag{200.4}$$

---

## 3. Konkretes Beispiel: $H_N = \mathbf{1}_{N\widehat{\mathbb Z}}$

Setze $H_N := \mathbf{1}_{N\widehat{\mathbb Z}}$, $N \in \mathbb N^\times$. Für $k \in \mathbb N^\times$ gilt $\alpha_k(H_N)(x) = H_N(kx)$. Die Bedingung $kx \in N\widehat{\mathbb Z}$ ist äquivalent zu $x \in \frac{N}{\gcd(N,k)}\widehat{\mathbb Z}$. Daher:
$$\boxed{\alpha_k(H_N) = \mathbf{1}_{\frac{N}{\gcd(N,k)}\widehat{\mathbb Z}}.} \tag{200.5}$$

Insbesondere $F_k = \mathbf{1}_{\frac{N}{\gcd(N,k)}\widehat{\mathbb Z}} - \mathbf{1}_{N\widehat{\mathbb Z}}$. Für den Quotientenkoeffizienten folgt:
$$\boxed{G_i^{H_N} = \mathbf{1}_{\frac{N}{\gcd(N,P)}\widehat{\mathbb Z}} - \mathbf{1}_{\frac{N}{\gcd(N,P/p_i)}\widehat{\mathbb Z}}.} \tag{200.6}$$

Auch dieser Ausdruck ist $G_i^{H_N} = -(1-\alpha_{p_i})\alpha_{P/p_i}(H_N)$, also ein expliziter Korand.

### Spezialfall $p_i \nmid N$

Dann $\gcd(N,P) = \gcd(N,P/p_i)$, und daher bereits als Funktion:
$$\boxed{G_i^{H_N} = 0.} \tag{200.7}$$

### Spezialfall $p_i \mid N$

Dann kann $G_i^{H_N}$ als Differenz zweier verschiedener Charakteristikfunktionen nicht null sein. Seine Quotientenklasse verschwindet trotzdem, weil es der explizite $(1-\alpha_{p_i})$-Korand aus (200.1) ist:
$$\boxed{G_i^{H_N} \neq 0 \text{ möglich, aber } [G_i^{H_N}] = 0.} \tag{200.8}$$

Das trennt sauber zwischen Nichtverschwindung als Funktion und Nichtverschwindung im Kommutatorquotienten.

---

## 4. Strukturelle Bedeutung

Die Identität $G_i^H = -(1-\alpha_{p_i})\alpha_{P/p_i}(H)$ gilt formal auch für ein punktiertes Potential. Der Unterschied ist ausschließlich: $\alpha_{P/p_i}(H)$ muss bei einem singulären $H$ nicht in $B$ liegen.

Damit misst die Quotientenklasse $[G_i^H]$ exakt die Frage, ob der formale primitive Ausdruck $-\alpha_{P/p_i}(H)$ durch reguläre Funktionen ersetzt werden kann.

$$\boxed{[G_i^H] \text{ ist eine Rand-Singularitätsobstruktion, keine gewöhnliche Nichtverschwindungsobstruktion.}}$$

Ein positiver Quotientenbefund kann daher nur aus einem echt punktierten, bei $0$ nicht regulär fortsetzbaren Potential kommen.

---

## 5. Neuer Status

Der reguläre Testsektor kann geschlossen werden als:
$$\boxed{[O\text{-}199\text{-}3]_{\mathrm{reg}} \quad \checkmark[M]_{\mathrm{neg}}.}$$

**Präzise Aussage:** Für jedes $H \in \operatorname{LC}(\widehat{\mathbb Z})$, jedes zulässige teilerfremde Primtupel $\mathbf p$ und jeden Slot $i$ verschwindet $\overline\Theta_{g,\mathbf p,i}([D_g^H])$.

Dies ist kein Ausschluss der punktierten Potentialroute. Es schließt nur deren global regulären Untersektor aus.

---

## 6. Anforderung an den nächsten Testkandidaten

Der nächste sinnvolle Test darf keine Charakteristikfunktion einer offenen Untergruppe als Potential verwenden. Benötigt wird ein konkretes $H$, das
$$H \in \operatorname{LC}(\widehat{\mathbb Z}\setminus\{0\}), \qquad H \notin \operatorname{LC}(\widehat{\mathbb Z}),$$
erfüllt, während gleichzeitig
$$F_k = \alpha_k(H) - H \in B$$
für die relevanten $k = p_1,p_2,p_3,p_4$ gilt.

Genau bei einem solchen singulären Potential ist der Quotiententest erstmals nicht tautologisch null.

---

## 7. Aktualisierter DAG-Status

| Knoten | Status | Inhalt |
|---|---|---|
| [O-199-3]$_{\mathrm{reg}}$ | $\checkmark[M]_{\mathrm{neg}}$ | Alle global regulären $H\in B$ sind Quotienten-unsichtbar |
| [O-199-3]$_{\mathrm{sing}}$ | $?[O]$ | Test mit echt punktiertem, bei $0$ singulärem $H$ ausständig |
| [O-199-1]$_{\mathrm{noncopr}}$ | $?[O]$ | Transfer-/Projektionsformel für $(k,mn)>1$ (unverändert offen) |
| [O-199-4] | $?[O]$ | weiterhin gesperrt bis Fall J.3 |

**Nächster Arbeitsauftrag:**
$$\boxed{\text{Konstruiere ein singuläres Potential } H \in \operatorname{LC}(\widehat{\mathbb Z}\setminus\{0\})\setminus\operatorname{LC}(\widehat{\mathbb Z}) \text{ mit } F_{p_j}\in B \text{ für } j=1,\ldots,4, \text{ und werte } G_i^H \text{ aus.}}$$
