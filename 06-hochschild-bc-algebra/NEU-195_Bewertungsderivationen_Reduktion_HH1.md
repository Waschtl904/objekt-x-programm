# NEU-195 — Bewertungsderivationen und Reduktion auf eine geladene 1-Derivation

## Vorbemerkung

Anknüpfung an NEU-194: Der determinantische Modellkochain scheitert an der Hochschild-Kozykelbedingung durch das erste äußere Face. Die Cup-/Shuffle-Route löst dieses Problem strukturell. Dieser Knoten konstruiert den kanonischen neutralen Vierkozykel und reduziert den geladenen Fall auf eine atomare $HH^1$-Frage.

---

## Ausgangsdaten

$$A = \bigoplus_{q\in\mathbb{Q}_+^\times} A_q, \qquad A_q A_r \subseteq A_{qr}.$$

Für jede Primzahl $p$: $v_p: \mathbb{Q}_+^\times \to \mathbb{Z}$ die $p$-adische Bewertung.

---

## 1. Kanonische neutrale 1-Derivationen

Definiere auf homogenen Elementen:

$$\boxed{\delta_p(a_q) := v_p(q)\, a_q, \qquad a_q \in A_q.} \tag{195.1}$$

Erweiterung durch Linearität auf ganz $A$.

**Derivationseigenschaft:** Für $a_q \in A_q$, $b_r \in A_r$:
$$\delta_p(a_q b_r) = v_p(qr)\,a_q b_r = \bigl(v_p(q)+v_p(r)\bigr)a_q b_r = \delta_p(a_q)b_r + a_q \delta_p(b_r).$$

$$\boxed{\delta_p \in Z^1(A,A).} \tag{195.2}$$

**Explizite Werte auf BC-Isometrien:**
$$\delta_p(\mu_n) = v_p(n)\mu_n, \qquad \delta_p(\mu_n^*) = -v_p(n)\mu_n^*, \qquad \delta_p(e(r)) = 0. \tag{195.3}$$

$e(r) \in A_1$ impliziert $v_p(1) = 0$. $\delta_p$ kommutiert mit der Zeitwirkung: Kochaingewicht $0$.

$$\boxed{[O\text{-}195\text{-}1] \quad \checkmark[M]}$$

---

## 2. Kanonischer neutraler Vierkozykel

Seien $p_1, p_2, p_3, p_4$ paarweise verschiedene Primzahlen. Definiere:

$$\boxed{\Omega_{\mathbf{p}} := \sum_{\sigma\in S_4} \operatorname{sgn}(\sigma)\, \delta_{p_{\sigma(1)}} \smile \delta_{p_{\sigma(2)}} \smile \delta_{p_{\sigma(3)}} \smile \delta_{p_{\sigma(4)}}.} \tag{195.4}$$

Explizit:
$$\Omega_{\mathbf{p}}(a_1,a_2,a_3,a_4) = \sum_{\sigma\in S_4} \operatorname{sgn}(\sigma) \prod_{j=1}^4 \delta_{p_{\sigma(j)}}(a_j). \tag{195.5}$$

**Kozykelbedingung:** Der Hochschildkorand ist eine graduierte Derivation bezüglich des Cup-Produkts:
$$b(F \smile G) = bF \smile G + (-1)^{\deg F} F \smile bG.$$

Da alle $\delta_{p_i}$ 1-Kozyklen sind ($b\delta_{p_i} = 0$), folgt per Induktion:

$$\boxed{b\Omega_{\mathbf{p}} = 0.} \tag{195.6}$$

Gewicht von $\Omega_{\mathbf{p}}$: 0 (alle Faktoren haben Gewicht 0).

$$\boxed{[O\text{-}195\text{-}2] \quad \checkmark[M]}$$

---

## 3. Exakte Auswertung auf den vier Primisometrien

Sei $P := p_1 p_2 p_3 p_4$. Für $\pi \in S_4$:
$$\delta_{p_i}(\mu_{p_{\pi(j)}}) = \delta_{i,\pi(j)}\, \mu_{p_{\pi(j)}}.$$

In der Summe (195.5) überlebt genau der Summand $\sigma = \pi$ (alle anderen haben mindestens einen verschwindenden Faktor):

$$\boxed{\Omega_{\mathbf{p}}(\mu_{p_{\pi(1)}}, \mu_{p_{\pi(2)}}, \mu_{p_{\pi(3)}}, \mu_{p_{\pi(4)}}) = \operatorname{sgn}(\pi)\,\mu_P.} \tag{195.7}$$

**Paarung mit dem neutralen Zyklus** $z_0^{1,\mathbf{p}} = \sum_\pi \operatorname{sgn}(\pi)\,\varepsilon_P \otimes \mu_{p_{\pi(1)}} \otimes \cdots \otimes \mu_{p_{\pi(4)}}$:

$$\left\langle \Omega_{\mathbf{p}}, z_0^{1,\mathbf{p}} \right\rangle = \sum_{\pi\in S_4} \operatorname{sgn}(\pi)^2\, \varepsilon_P(\mu_P) = 24. \tag{195.8}$$

Da $z_0^{1,\mathbf{p}}$ ein Zyklus ist, kann ein Hochschildrand nicht nichtverschwindend mit ihm paaren. Also:

$$\boxed{[\Omega_{\mathbf{p}}] \neq 0 \quad \text{in} \quad HH^4(A,A)_0.} \tag{195.9}$$

$$\boxed{[O\text{-}195\text{-}3] \quad \checkmark[M]}$$

Positiver Kohomologiebefund: Die Cup-/Shuffle-Architektur funktioniert im neutralen Sektor. Das Problem liegt ausschließlich in der Erzeugung eines nichttrivialen Gewichts.

---

## 4. Geladene Reduktion

Sei $g \in \mathbb{Q}_+^\times \setminus \{1\}$, $\lambda = \log g$. Gesucht: eine homogene Derivation
$$D_g: A \longrightarrow A, \qquad D_g(A_q) \subseteq A_{gq}, \tag{195.10}$$
$$D_g(ab) = D_g(a)b + aD_g(b). \tag{195.11}$$

Dann $D_g \in Z^1(A,A)_\lambda$.

Setze $D_1 := D_g$, $D_2 := \delta_{p_2}$, $D_3 := \delta_{p_3}$, $D_4 := \delta_{p_4}$ für drei weitere Primzahlen $p_2, p_3, p_4$ (verschieden von $p_1$). Definiere:

$$\boxed{\Omega_{D_g,\mathbf{p}} := \sum_{\sigma\in S_4} \operatorname{sgn}(\sigma)\, D_{\sigma(1)} \smile D_{\sigma(2)} \smile D_{\sigma(3)} \smile D_{\sigma(4)}.} \tag{195.12}$$

Da alle vier Faktoren 1-Kozyklen sind:
$$\boxed{b\Omega_{D_g,\mathbf{p}} = 0.} \tag{195.13}$$

Da genau ein Faktor Gewicht $\lambda$ trägt:
$$\boxed{\Omega_{D_g,\mathbf{p}} \in Z^4(A,A)_\lambda.} \tag{195.14}$$

Das äußere-Face-Problem aus NEU-194 tritt strukturell nicht mehr auf.

---

## 5. Paarungsformel für den geladenen Kandidaten

Für jedes $\pi \in S_4$ erzwingen die drei Bewertungsderivationen, dass genau die Slots mit $\mu_{p_2}, \mu_{p_3}, \mu_{p_4}$ getroffen werden; $D_g$ trifft $\mu_{p_1}$. Da $\varepsilon$ ein Charakter ist:

$$\varepsilon_{gP}\!\left( \Omega_{D_g,\mathbf{p}}(\mu_{p_{\pi(1)}}, \ldots, \mu_{p_{\pi(4)}}) \right) = \operatorname{sgn}(\pi)\, \varepsilon\!\left(D_g(\mu_{p_1})\right). \tag{195.15}$$

$$\boxed{\left\langle \Omega_{D_g,\mathbf{p}},\, z_{-\lambda}^{g,\mathbf{p}} \right\rangle = 4!\, \varepsilon\!\left(D_g(\mu_{p_1})\right).} \tag{195.16}$$

**Bedingter vollständiger Satz:**

$$\boxed{D_g \in \operatorname{Der}(A)_g,\quad \varepsilon(D_g(\mu_{p_1})) \neq 0 \quad\Longrightarrow\quad \begin{cases} b\Omega_{D_g,\mathbf{p}} = 0,\\[2mm] \langle\Omega_{D_g,\mathbf{p}},\, z_{-\lambda}^{g,\mathbf{p}}\rangle \neq 0,\\[2mm] [\Omega_{D_g,\mathbf{p}}] \neq 0. \end{cases}} \tag{195.17}$$

**Atomare $HH^1$-Reduktion:**

$$\boxed{\exists\, D_g: A \to A:\quad D_g(A_q) \subseteq A_{gq},\quad D_g\text{ Derivation},\quad \varepsilon(D_g(\mu_p)) \neq 0\;?} \tag{195.18}$$

---

## 6. Innere Derivation ist ausgeschlossen

Sei $x_g \in A_g$, $D_g = \operatorname{ad}(x_g)$, $D_g(a) = x_g a - ax_g$. Dann:
$$\varepsilon(D_g(a)) = \varepsilon(x_g)\varepsilon(a) - \varepsilon(a)\varepsilon(x_g) = 0.$$

Daher $\langle \Omega_{\operatorname{ad}(x_g),\mathbf{p}},\, z_{-\lambda}^{g,\mathbf{p}} \rangle = 0$.

Stärker: $\operatorname{ad}(x_g) = \pm b x_g$ ist ein Hochschildrand, also ist jedes Cup-Produkt mit $\operatorname{ad}(x_g)$ und sonst Kozyklen wiederum ein Rand:

$$\boxed{[\Omega_{\operatorname{ad}(x_g),\mathbf{p}}] = 0.} \tag{195.20}$$

$$\boxed{[O\text{-}195\text{-}4] \quad \checkmark[M]_{\mathrm{neg}}}$$

---

## 7. Multiplikatorversuch (zweite Route)

Für $x_g \in A_g$ setze $L_{x_g} := x_g \smile \Omega_{\mathbf{p}}$, d.h.
$$L_{x_g}(a_1,\ldots,a_4) = x_g \Omega_{\mathbf{p}}(a_1,\ldots,a_4).$$

Paarung: $\langle L_{x_g}, z_{-\lambda}^{g,\mathbf{p}} \rangle = 24\,\varepsilon(x_g). \tag{195.21}$

Korand:
$$\boxed{(bL_{x_g})(a_0,\ldots,a_4) = (a_0 x_g - x_g a_0)\,\Omega_{\mathbf{p}}(a_1,\ldots,a_4).} \tag{195.22}$$

$L_{x_g}$ ist genau dann ein Kozykel, wenn:
$$[a, x_g]\operatorname{Im}(\Omega_{\mathbf{p}}) = 0 \qquad \text{für alle } a \in A. \tag{195.23}$$

Hinreichendes Kriterium: $x_g \in Z(A) \cap A_g$.

$$\boxed{[O\text{-}195\text{-}5] \quad ?[O]:\quad \exists\,x_g \in A_g,\ \varepsilon(x_g) \neq 0,\ [A,x_g]\operatorname{Im}(\Omega_{\mathbf{p}}) = 0\;?}$$

---

## 8. Gesamtstand der geladenen Route

```
Neutraler Sektor:
  Omega_p in Z^4(A,A)_0     [O-195-2]  checkmark[M]
  [Omega_p] != 0            [O-195-3]  checkmark[M]  (Paarung = 24)

Geladener Sektor:
  Innere Derivation         [O-195-4]  checkmark[M]_neg  (Paarung = 0, Klasse = 0)
  Route A: nicht-innere D_g mit eps(D_g(mu_p)) != 0  --> [O-193-4]  ?[O]
  Route B: Multiplikator x_g mit [A,x_g]Im(Omega) = 0 --> [O-195-5]  ?[O]
```

### Zwei atomare Restfragen

| Route | Bedingung | Status |
|---|---|---|
| **A** | $\exists$ nicht-innere homogene Derivation $D_g$ mit $\varepsilon(D_g(\mu_p)) \neq 0$ | $?[O]$ |
| **B** | $\exists\, x_g \in A_g$, $\varepsilon(x_g) \neq 0$, $[A,x_g]\operatorname{Im}(\Omega_{\mathbf{p}}) = 0$ | $?[O]$ |

$$\boxed{\checkmark[M]_{\mathrm{part}}}$$

für die geladene Vierkozykelroute insgesamt. Die verbleibende atomare Restlücke ist die Existenz einer nicht-inneren homogenen Derivation $D_g$ mit $\varepsilon(D_g(\mu_p)) \neq 0$.

$$\boxed{\text{Nächster Schritt: explizite Konstruktion oder Ausschluss von }D_g \in \operatorname{Der}(A)_g \setminus \operatorname{Inn}(A)_g\text{ mit }\varepsilon(D_g(\mu_p)) \neq 0.}$$
