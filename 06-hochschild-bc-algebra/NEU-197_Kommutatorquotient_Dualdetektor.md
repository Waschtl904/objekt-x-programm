# NEU-197 — Kommutatorquotient und universeller Dualdetektor

## Vorbemerkung

NEU-196 schließt den Augmentationsdetektor $\varepsilon_h$ gegenüber der NEU-188-Potentialroute aus. Dieser Knoten klassifiziert **alle** zulässigen Koeffizientenfunktionale des antisymmetrischen Zyklus durch den partiellen Kommutatorquotienten $Q_{h,\mathbf{p}}$ und reduziert die Restfrage auf eine einzige algebraische Entscheidung.

Fixiere: $\mathbf{p} = (p_1,p_2,p_3,p_4)$ paarweise verschiedene Primzahlen, $P = p_1p_2p_3p_4$, $g \in \mathbb{Q}_+^\times$, $\lambda = \log g$, $h = gP$.

$$A = \bigoplus_{q\in\mathbb{Q}_+^\times} A_q.$$

---

## 1. Partieller Kommutatorquotient

$$\boxed{\mathcal{C}_{h,\mathbf{p}} := \sum_{i=1}^4 [\mu_{p_i}, A_{h/p_i}] \subseteq A_h.} \tag{197.1}$$

$$\boxed{Q_{h,\mathbf{p}} := A_h / \mathcal{C}_{h,\mathbf{p}}.} \tag{197.2}$$

Homogenität: $\mu_{p_i}a$ und $a\mu_{p_i}$ für $a \in A_{h/p_i}$ liegen beide in $A_{p_i \cdot h/p_i} = A_h$. $\checkmark$

$$\boxed{[O\text{-}197\text{-}1] \quad \checkmark[K]}$$

---

## 2. Allgemeiner geladener Dualkettenkandidat

Sei $\varphi_h \in A^\vee$ mit homogenem Träger auf $A_h$: $\varphi_h = \varphi_h \circ P_h$.

$$\boxed{z_{\varphi_h}^{\mathbf{p}} := \sum_{\pi\in S_4} \operatorname{sgn}(\pi)\, \varphi_h \otimes \mu_{p_{\pi(1)}} \otimes \mu_{p_{\pi(2)}} \otimes \mu_{p_{\pi(3)}} \otimes \mu_{p_{\pi(4)}}.} \tag{197.3}$$

Gewicht: $\varphi_h$ hat duales Gewicht $-\log h$; vier Algebrafaktoren tragen $+\log P$. Zusammen:
$$-\log h + \log P = -\log g = -\lambda, \qquad z_{\varphi_h}^{\mathbf{p}} \in C_4(A,A^\vee)_{-\lambda}.$$

---

## 3. Exaktes Zykluskriterium

**Innere Randterme** verschwinden paarweise wegen $\mu_{p_i}\mu_{p_j} = \mu_{p_j}\mu_{p_i}$ (vgl. NEU-193).

**Äußere Randterme** ergeben nach Gruppierung:

$$\partial z_{\varphi_h}^{\mathbf{p}} = \sum_{i=1}^4 (-1)^{i-1} \bigl(\varphi_h \cdot \mu_{p_i} - \mu_{p_i} \cdot \varphi_h\bigr) \otimes \operatorname{Alt}_3(\mu_{p_1},\ldots,\widehat{\mu_{p_i}},\ldots,\mu_{p_4}). \tag{197.4}$$

Für $a \in A$:
$$\bigl(\varphi_h \cdot \mu_{p_i} - \mu_{p_i} \cdot \varphi_h\bigr)(a) = \varphi_h(\mu_{p_i}a) - \varphi_h(a\mu_{p_i}) = \varphi_h([\mu_{p_i},a]). \tag{197.5}$$

Wegen des homogenen Trägers kann nur $a \in A_{h/p_i}$ beitragen. Die vier Terme liegen in verschiedenen dualen Gradsektoren $A_{h/p_i}^\vee$; keine zusätzliche Auslöschung zwischen verschiedenem $i$.

$$\boxed{\partial z_{\varphi_h}^{\mathbf{p}} = 0 \iff \varphi_h(\mathcal{C}_{h,\mathbf{p}}) = 0.} \tag{197.6}$$

$$\boxed{z_{\varphi_h}^{\mathbf{p}} \text{ ist ein Zyklus} \iff \varphi_h \text{ faktorisiert über } Q_{h,\mathbf{p}}.} \tag{197.7}$$

**Vollständige Klassifikation:**
$$\bigl\{\varphi_h : \partial z_{\varphi_h}^{\mathbf{p}} = 0\bigr\} \cong Q_{h,\mathbf{p}}^\vee. \tag{197.8}$$

$$\boxed{[O\text{-}197\text{-}2] \quad \checkmark[M]}$$

---

## 4. Paarung mit dem geladenen Cup-Kozykel

Sei $D_g \in \operatorname{Der}(A)_g$, $D_1 = D_g$, $D_2 = \delta_{p_2}$, $D_3 = \delta_{p_3}$, $D_4 = \delta_{p_4}$. Der NEU-195-Kozykel $\Omega_{D_g,\mathbf{p}}$.

Definiere das homogene Zielelement:

$$\boxed{Y_{D_g,\mathbf{p}} := D_g(\mu_{p_1})\,\mu_{p_2}\mu_{p_3}\mu_{p_4} \in A_h.} \tag{197.9}$$

Gradrechnung: $D_g(\mu_{p_1}) \in A_{gp_1}$, also $Y_{D_g,\mathbf{p}} \in A_{gp_1 \cdot p_2 p_3 p_4} = A_{gP} = A_h$. $\checkmark$

Bei der Auswertung erzwingen die drei Bewertungsderivationen $\delta_{p_2}, \delta_{p_3}, \delta_{p_4}$, dass $D_g$ auf den Slot mit $\mu_{p_1}$ trifft. Da $\mu_{p_2}, \mu_{p_3}, \mu_{p_4}$ untereinander kommutieren und $\varphi_h$ auf $\mathcal{C}_{h,\mathbf{p}}$ verschwindet, liefern alle 24 Permutationen denselben Wert:

$$\boxed{\left\langle \Omega_{D_g,\mathbf{p}},\, z_{\varphi_h}^{\mathbf{p}} \right\rangle = 4!\, \varphi_h\!\left(Y_{D_g,\mathbf{p}}\right).} \tag{197.10}$$

---

## 5. Universelles Detektionskriterium

Sei $[Y_{D_g,\mathbf{p}}] \in Q_{h,\mathbf{p}}$ die Quotientenklasse.

$$\boxed{\exists\,\varphi_h \in A^\vee:\; \partial z_{\varphi_h}^{\mathbf{p}}=0,\; \left\langle \Omega_{D_g,\mathbf{p}}, z_{\varphi_h}^{\mathbf{p}} \right\rangle \neq 0 \quad\iff\quad [Y_{D_g,\mathbf{p}}] \neq 0 \text{ in } Q_{h,\mathbf{p}}.} \tag{197.11}$$

**Beweis.**
($\Rightarrow$) Ein solches $\varphi_h$ verschwindet auf $\mathcal{C}_{h,\mathbf{p}}$ (wegen (197.6)) und erfüllt $\varphi_h(Y_{D_g,\mathbf{p}}) \neq 0$. Also $Y_{D_g,\mathbf{p}} \notin \mathcal{C}_{h,\mathbf{p}}$.

($\Leftarrow$) Sei $[Y_{D_g,\mathbf{p}}] \neq 0$. Da der algebraische Dual eines Vektorraums Punkte trennt, existiert $\ell \in Q_{h,\mathbf{p}}^\vee$ mit $\ell([Y_{D_g,\mathbf{p}}]) \neq 0$. Setze $\varphi_h := \ell \circ (A_h \to Q_{h,\mathbf{p}}) \circ P_h$. Dann $\varphi_h|_{\mathcal{C}_{h,\mathbf{p}}} = 0$, also $z_{\varphi_h}^{\mathbf{p}}$ Zyklus, und $\langle\Omega_{D_g,\mathbf{p}}, z_{\varphi_h}^{\mathbf{p}}\rangle = 24\,\ell([Y_{D_g,\mathbf{p}}]) \neq 0$. $\square$

$$\boxed{[O\text{-}197\text{-}3] \quad \checkmark[M]}$$

---

## 6. Logische Einordnung von NEU-196

Der Augmentationscharakter $\varepsilon_h = \varepsilon \circ P_h$ faktorisiert wegen der Multiplikativität von $\varepsilon$ über $Q_{h,\mathbf{p}}$. NEU-196 beweist:
$$\varepsilon_h(Y_{D_g,\mathbf{p}}) = 0.$$

Das heißt: $\varepsilon_h$ als **ein** Element von $Q_{h,\mathbf{p}}^\vee$ annulliert $[Y_{D_g,\mathbf{p}}]$. Es folgt **nicht** $[Y_{D_g,\mathbf{p}}] = 0$.

$$\boxed{\begin{aligned} \text{NEU-196:}&\quad \text{ein bestimmtes Funktional ist blind;}\\[1mm] \text{NEU-197:}&\quad \text{alle möglichen Funktionale sind blind}\\[1mm] &\quad \iff [Y_{D_g,\mathbf{p}}] = 0 \text{ im Kommutatorquotienten.} \end{aligned}} \tag{197.12}$$

Die logische Trennung ist jetzt exakt.

---

## 7. Atomarer Restknoten [O-197-4]

Für einen konkreten NEU-188-Potentialkandidaten $D_g^H$:

$$\boxed{[O\text{-}197\text{-}4]:\quad \left[D_g^H(\mu_{p_1})\,\mu_{p_2}\mu_{p_3}\mu_{p_4}\right] \neq 0 \quad\text{in}\quad Q_{gP,\mathbf{p}}\;?} \tag{197.13}$$

Status: $?[O]$

Ein neuer singulärer Auswertungsoperator muss nicht ad hoc postuliert werden. Er existiert algebraisch genau dann, wenn diese Klasse im partiellen Kommutatorquotienten nicht verschwindet.

**Präzise Reformulierung:** Liegt
$$Y_{D_g^H,\mathbf{p}} = D_g^H(\mu_{p_1})\,\mu_{p_2}\mu_{p_3}\mu_{p_4}$$
in
$$\mathcal{C}_{gP,\mathbf{p}} = \sum_{i=1}^4 [\mu_{p_i},\, A_{gP/p_i}]$$
oder nicht?

---

## 8. DAG-Gesamtstand

```
[O-197-1]  checkmark[K]   Kommutatorquotient Q_{h,p} wohldefiniert und homogen
[O-197-2]  checkmark[M]   Zykluskriterium: phi_h Zyklus <=> phi_h faktorisiert ueber Q_{h,p}
[O-197-3]  checkmark[M]   universelles Detektionskriterium (197.11): [Y] != 0 <=> Detektor existiert
[O-197-4]  ?[O]           [D_g^H(mu_p1) mu_p2 mu_p3 mu_p4] != 0 in Q_{gP,p} ?

NEU-196-Einordnung:
  eps_h annulliert [Y]   -- ein Funktional ist blind
  [Y] = 0 ?              -- offene Frage (NEU-197 reduktion)

[O-193-4]  ?[O]  jetzt exakt reduziert auf [O-197-4]
[O-193-5]  ?[O]  gesperrt an [O-193-4]
```

| Knoten | Inhalt | Status |
|---|---|---|
| [O-197-1] | $Q_{h,\mathbf{p}}$ wohldefiniert | $\checkmark[K]$ |
| [O-197-2] | Vollständige Klassifikation der Zyklusfunktionale | $\checkmark[M]$ |
| [O-197-3] | Universelles Detektionskriterium via $Q_{h,\mathbf{p}}^\vee$ | $\checkmark[M]$ |
| [O-197-4] | $[Y_{D_g^H,\mathbf{p}}] \neq 0$ in $Q_{gP,\mathbf{p}}$? | $?[O]$ |

$$\boxed{\checkmark[M]_{\mathrm{part}}}$$

$$\boxed{\text{Atomare Restfrage: } Y_{D_g^H,\mathbf{p}} \in \mathcal{C}_{gP,\mathbf{p}} \text{ oder nicht?}}$$
