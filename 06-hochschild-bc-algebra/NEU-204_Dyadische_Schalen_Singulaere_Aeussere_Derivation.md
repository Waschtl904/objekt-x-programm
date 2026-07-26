# NEU-204 — Dyadische Schalen: singuläre äußere Derivation mit analytischem Zieltyp

**Status:** vollständiger Kandidatenaudit  
**Erstellt:** 2026-07-19  
**Vorgänger:** NEU-203  
**Ziel:** Entscheidung des dyadischen Schalenkandidaten für $[O\text{-}203\text{-}4]$

---

## 204.0 — Quellen- und Typkorrektur

Wir verwenden die Standardrelation der Bost–Connes-Algebra:
$$\rho_n(e(r)) = \mu_n e(r)\mu_n^* = \frac{1}{n}\sum_{ns=r}e(s). \tag{204.0.1}$$

Für $r=0$ folgt:
$$E_n := \mu_n\mu_n^* = \frac{1}{n}\sum_{ns=0}e(s). \tag{204.0.2}$$

Damit gilt bereits algebraisch:
$$E_n \in B_{\mathrm{alg}} = \mathbb{C}[\mathbb{Q}/\mathbb{Z}]. \tag{204.0.3}$$

Insbesondere liegen $P_j := E_{2^j}$, $q_j := P_j - P_{j+1}$ sowie jedes endliche Potential $X_N$ in $B_{\mathrm{alg}}$.

### Korrektur an NEU-203.0

Die dortige typologische Aussage $E_n, z_p \notin B_{\mathrm{alg}}$ ist im verwendeten Standardmodell falsch. Korrekt ist:
$$E_n,\, z_p \in B_{\mathrm{alg}}. \tag{204.0.4}$$

Die übrigen Resultate von NEU-203 werden dadurch nicht aufgehoben. Zu unterscheiden ist:
$$z_p \neq 0 \text{ in } B_{\mathrm{alg}}/[B_{\mathrm{alg}}, B_{\mathrm{alg}}] = B_{\mathrm{alg}},$$
während
$$z_p = 0 \text{ in } A_{\mathrm{alg}}/[A_{\mathrm{alg}}, A_{\mathrm{alg}}].$$

---

## 204.1 — Dyadische Projektionsgeometrie

Setze:
$$P_j := \mu_{2^j}\mu_{2^j}^*, \qquad P_0 = 1. \tag{204.1.1}$$

Da $\mu_{2^{j+1}} = \mu_{2^j}\mu_2$:
$$P_{j+1} = \mu_{2^j}\mu_2\mu_2^*\mu_{2^j}^* \leq \mu_{2^j}\mu_{2^j}^* = P_j. \tag{204.1.2}$$

Für $q_j := P_j - P_{j+1}$ folgt daher:
$$q_j^2 = q_j = q_j^*. \tag{204.1.4}$$

Ferner $P_j P_\ell = P_{\max(j,\ell)}$, woraus für $j \neq \ell$:
$$q_j q_\ell = 0. \tag{204.1.6}$$

Teleskopieren liefert:
$$1 = P_0 = \sum_{j=0}^{N-1} q_j + P_N. \tag{204.1.7}$$

In der kanonischen Semigruppendarstellung auf $\ell^2(\mathbb{N}^\times)$:
$$P_j\delta_n = \begin{cases}\delta_n, & 2^j \mid n,\\ 0, & 2^j \nmid n,\end{cases} \qquad q_j\delta_n = \begin{cases}\delta_n, & v_2(n)=j,\\ 0, & v_2(n)\neq j.\end{cases} \tag{204.1.8}$$

---

## 204.2 — Gesättigte Potentiale und exakte Normen

Definiere:
$$c_j := \log(j+2) \tag{204.2.0}$$

$$\boxed{X_N := \sum_{j=0}^{N-1} c_j q_j + c_N P_N.} \tag{204.2.1}$$

Wegen (204.1.7) ist $X_N$ bezüglich der orthogonalen Zerlegung $1 = q_0 + \cdots + q_{N-1} + P_N$ diagonal mit Eigenwerten $c_0 < c_1 < \cdots < c_{N-1} < c_N$. Daher:
$$\boxed{\|X_N\| = c_N = \log(N+2).} \tag{204.2.2}$$

Für $M > N$:
$$X_M - X_N = \sum_{j=N}^{M-1}(c_j - c_N)q_j + (c_M - c_N)P_M. \tag{204.2.3}$$

Da $c_j - c_N < c_M - c_N$ für alle $j < M$:
$$\boxed{\|X_M - X_N\| = c_M - c_N = \log\!\left(\frac{M+2}{N+2}\right).} \tag{204.2.4}$$

Mit $M = 2N$ folgt $\|X_{2N} - X_N\| \to \log 2 > 0$. Also ist $(X_N)$ nicht norm-Cauchy.

---

## 204.3 — Exakte Verschiebungsrelationen

**Lemma 204.3.1:** Für alle $j, a \geq 0$:
$$\boxed{P_j S_a = S_a P_{(j-a)_+}, \qquad (j-a)_+ := \max(j-a,0),} \tag{204.3.1}$$
wobei $S_a := \mu_{2^a}$.

**Beweis.** Für $j \geq a$: $\mu_{2^j} = \mu_{2^a}\mu_{2^{j-a}}$, also
$$P_j S_a = \mu_{2^a}\mu_{2^{j-a}}\mu_{2^{j-a}}^*\mu_{2^a}^*\mu_{2^a} = S_a P_{j-a}.$$
Für $j < a$: $S_a = \mu_{2^j}\mu_{2^{a-j}}$, also $P_j S_a = S_a = S_a P_0$. $\square$

**Lemma 204.3.2:** Für ungerades $u$:
$$\boxed{P_j \mu_u = \mu_u P_j.} \tag{204.3.2}$$
Dies folgt aus $\mu_{2^j}\mu_u = \mu_u\mu_{2^j}$ und $\mu_{2^j}^*\mu_u = \mu_u\mu_{2^j}^*$ für $(2^j,u)=1$.

Insbesondere kommutieren $q_j$, $X_N$, $B_a$ mit allen $\mu_u$, $\mu_u^*$ für ungerades $u$.

---

## 204.4 — Vollständige endliche Kommutatorformel

Für $N \geq a$ folgt aus (204.3.1):
$$X_N S_a = S_a \left(\sum_{j=0}^{N-a-1} c_{j+a} q_j + c_N P_{N-a}\right). \tag{204.4.1}$$

Andererseits:
$$S_a X_N = S_a \left(\sum_{j=0}^{N-1} c_j q_j + c_N P_N\right). \tag{204.4.2}$$

Da $P_{N-a} - P_N = \sum_{j=N-a}^{N-1} q_j$:
$$\boxed{[X_N, S_a] = S_a C_{N,a},} \tag{204.4.4}$$
mit dem vollständigen Ausdruck:
$$\boxed{C_{N,a} = \sum_{j=0}^{N-a-1}(c_{j+a}-c_j)q_j + \sum_{j=N-a}^{N-1}(c_N - c_j)q_j.} \tag{204.4.5}$$

Der erste Summand liefert für $N \to \infty$ den Grenzwert $B_a$. Der zweite Summand ist der obere Randterm. Der Sättigungsterm $c_N P_N$ kompensiert alle verbleibenden $P_N$- und $P_{N-a}$-Terme exakt; nach (204.4.5) verbleibt nur eine endliche Linearkombination der Schalen $q_j$.

Für $N < a$:
$$C_{N,a} = \sum_{j=0}^{N-1}(c_N - c_j)q_j. \tag{204.4.6}$$

---

## 204.5 — Normgrenzwert der Generatorkommutatoren

Setze:
$$d_j^{(a)} := c_{j+a} - c_j = \log\!\left(\frac{j+a+2}{j+2}\right). \tag{204.5.1}$$

Für festes $a \geq 1$: $d_j^{(a)} > 0$, streng fallend, $d_j^{(a)} \to 0$.

Wegen paarweiser Orthogonalitt der $q_j$:
$$\left\|\sum_{j=J}^{K} d_j^{(a)} q_j\right\| = \max_{J \leq j \leq K} d_j^{(a)} = d_J^{(a)}. \tag{204.5.4}$$

Somit konvergiert:
$$\boxed{B_a := \sum_{j=0}^{\infty} d_j^{(a)} q_j} \tag{204.5.5}$$
in $B_{C^*} = C^*(\mathbb{Q}/\mathbb{Z}) \subset A_{C^*}$, mit:
$$\boxed{\|B_a\| = d_0^{(a)} = \log\!\left(\frac{a+2}{2}\right).} \tag{204.5.6}$$

Setze $B_0 := 0$.

### Konvergenz der Randformel gegen $B_a$

Für $N \geq a$ gilt auf den Schalen $j < N-a$: $C_{N,a}$ und $B_a$ stimmen exakt überein. Auf den oberen Randschalen:
$$\|C_{N,a} - B_a\| \leq \max\{c_{N+a-1}-c_N,\, d_N^{(a)}\} \longrightarrow 0. \tag{204.5.8}$$

Folglich:
$$\boxed{\lim_{N\to\infty}[X_N, \mu_{2^a}] = \mu_{2^a} B_a.} \tag{204.5.9}$$

Für $k = 2^a u$, $u$ ungerade, kommutieren $C_{N,a}$, $B_a$ mit $\mu_u$:
$$\boxed{\lim_{N\to\infty}[X_N, \mu_k] = \mu_k B_a, \qquad a = v_2(k).} \tag{204.5.10}$$

Da $X_N = X_N^*$:
$$\boxed{\lim_{N\to\infty}[X_N, \mu_k^*] = -B_a \mu_k^*.} \tag{204.5.11}$$

Da $X_N \in B_{\mathrm{alg}}$ abelsch:
$$\boxed{[X_N, e(r)] = 0 \qquad \forall\, r \in \mathbb{Q}/\mathbb{Z}.} \tag{204.5.12}$$

---

## 204.6 — Konstruktion der Derivation auf dem algebraischen Kern

Für jeden Generator $g \in \{e(r), \mu_k, \mu_k^*\}$ existiert nach §204.5 der Normgrenzwert $D(g) := \lim_{N\to\infty}[X_N, g]$.

Für ein algebraisches Wort $w = g_1 \cdots g_m$ gilt für jedes $N$:
$$[X_N, w] = \sum_{\ell=1}^{m} g_1 \cdots g_{\ell-1} [X_N, g_\ell] g_{\ell+1} \cdots g_m. \tag{204.6.2}$$

Die Summe ist endlich; jeder Summand hat einen Normgrenzwert. Daher existiert $D(w)$, ist darstellungsunabhängig und respektiert alle definierenden BC-Relationen.

Die Leibnizregel:
$$D(ab) = \lim_N [X_N, ab] = \lim_N([X_N, a]b + a[X_N, b]) = D(a)b + aD(b). \tag{204.6.4}$$

$$\boxed{D: A_{\mathrm{alg}} \longrightarrow A_{C^*}} \tag{204.6.5}$$
ist eine wohldefinierte Derivation mit
$$D(e(r)) = 0, \quad D(\mu_k) = \mu_k B_{v_2(k)}, \quad D(\mu_k^*) = -B_{v_2(k)}\mu_k^*. \tag{204.6.6/7/8}$$

Da $X_N = X_N^*$:
$$\boxed{D(a^*) = -D(a)^*.} \tag{204.6.9}$$

Die Derivation $\delta := iD$ erfüllt die übliche $*$-Konvention $\delta(a^*) = \delta(a)^*$.

$D$ ist eine normunbeschränkte Derivation auf der dichten $*$-Unteralgebra $A_{\mathrm{alg}} \subset A_{C^*}$. Abschließbarkeit oder graphnormliche Stetigkeit werden in diesem Knoten nicht behauptet.

---

## 204.7 — Neutralität und Normunbeschränktheit

Jedes $X_N$ hat Grad $1$, also erhält $\operatorname{ad}(X_N)$ jeden homogenen Grad. Für den Grenzwert:
$$\boxed{D\bigl((A_{\mathrm{alg}})_g\bigr) \subseteq (A_{C^*})_g.} \tag{204.7.1}$$

Der Kandidat ist neutral ($\deg D = 1_\Gamma$). Im Allgemeinen gilt $D\bigl((A_{\mathrm{alg}})_g\bigr) \not\subseteq (A_{\mathrm{alg}})_g$.

Da $\mu_{2^a}$ Isometrie:
$$\|D(\mu_{2^a})\| = \|\mu_{2^a} B_a\| = \|B_a\| = \log\!\left(\frac{a+2}{2}\right) \longrightarrow \infty, \qquad \|\mu_{2^a}\| = 1. \tag{204.7.3}$$

Somit ist $D$ normunbeschränkt und besitzt keine beschränkte Derivationsfortsetzung auf ganz $A_{C^*}$.

---

## 204.8 — Nichtinnerheit bezüglich $A_{C^*}$

Betrachte die kanonische Semigruppendarstellung $\pi: A_{C^*} \to B(\ell^2(\mathbb{N}^\times))$ mit $\pi(\mu_k)\delta_n = \delta_{kn}$, $\pi(e(r))\delta_n = \chi_r(n)\delta_n$.

Die Familie $\{\pi(e(r))\}$ trennt die Basisvektoren: Für $m \neq n$ existiert $r$ mit $\chi_r(m) \neq \chi_r(n)$. Jeder beschränkte Operator im gemeinsamen Kommutanten ist daher diagonal.

Angenommen, es gibt einen beschränkten Implementierer $T$ mit $\pi(D(a)) = [T, \pi(a)]$. Aus $D(e(r)) = 0$ folgt, dass $T$ diagonal ist:
$$T\delta_n = h(n)\delta_n \quad \text{für eine beschränkte Folge } h. \tag{204.8.4}$$

$B_1$ wirkt auf der Schale $v_2(n) = j$ durch $d_j^{(1)} = c_{j+1} - c_j$. Aus $D(\mu_2) = \mu_2 B_1$ folgt:
$$\boxed{h(2n) - h(n) = c_{v_2(n)+1} - c_{v_2(n)}.} \tag{204.8.5}$$

Für ungerades $n$ ergibt Iteration:
$$h(2^J n) - h(n) = \sum_{j=0}^{J-1}(c_{j+1}-c_j) = c_J - c_0 = \log(J+2) - \log 2 \longrightarrow \infty. \tag{204.8.6}$$

Widerspruch zur Beschränktheit von $h$. Wäre $D = \operatorname{ad}(x)$ mit $x \in A_{C^*}$, so wäre $T = \pi(x)$ ein solcher beschränkter Implementierer. Daher:
$$\boxed{D \text{ ist nicht inner als Derivation } A_{\mathrm{alg}} \to A_{C^*}.} \tag{204.8.7}$$

**Präzisierung:** Im algebraischen Vektorraum der endlich getragenen Folgen implementiert der diagonale Operator
$$H\delta_n := c_{v_2(n)}\delta_n \tag{204.8.8}$$
die Generatorformeln: $\pi(D(a)) = [H, \pi(a)]$. Der bewiesene Befund ist ausschließlich die Abwesenheit eines **beschränkten** Implementierers und insbesondere eines Implementierers aus $A_{C^*}$. Nichtimplementierbarkeit durch unbeschränkte Operatoren wird nicht behauptet.

---

## 204.9 — Algebraischer Zieltyp scheitert bereits auf $\mu_2$

Unter der Fourieridentifikation $B_{C^*} = C^*(\mathbb{Q}/\mathbb{Z}) \cong C(\widehat{\mathbb{Z}})$:
$$P_j = \mathbf{1}_{2^j\widehat{\mathbb{Z}}}, \qquad q_j = \mathbf{1}_{2^j\widehat{\mathbb{Z}} \setminus 2^{j+1}\widehat{\mathbb{Z}}}. \tag{204.9.1}$$

$B_1$ entspricht der stetigen Funktion auf $\widehat{\mathbb{Z}}$:
$$B_1(x) = \begin{cases} c_{v_2(x)+1} - c_{v_2(x)}, & x \neq 0,\\ 0, & x = 0. \end{cases} \tag{204.9.2}$$

Stetigkeit bei $0$ folgt aus $c_{j+1} - c_j \to 0$. $B_{\mathrm{alg}} = \mathbb{C}[\mathbb{Q}/\mathbb{Z}]$ entspricht genau den lokal konstanten Funktionen auf $\widehat{\mathbb{Z}}$.

$B_1$ ist bei $0$ nicht lokal konstant: Jede Umgebung $2^J\widehat{\mathbb{Z}}$ enthält Elemente mit exakter $2$-adischer Bewertung $J$, auf denen $B_1$ den positiven Wert $c_{J+1}-c_J > 0$ annimmt. Daher:
$$\boxed{B_1 \notin B_{\mathrm{alg}}.} \tag{204.9.3}$$

Angenommen $D(\mu_2) = \mu_2 B_1 \in A_{\mathrm{alg}}$. Dann wäre $B_1 = \mu_2^* D(\mu_2) \in A_{\mathrm{alg}}$, und da $B_1$ neutral im abelschen $C^*$-Sektor liegt, folgte $B_1 \in A_{\mathrm{alg}} \cap B_{C^*} = B_{\mathrm{alg}}$ — Widerspruch zu (204.9.3). Somit:
$$\boxed{D(\mu_2) \notin A_{\mathrm{alg}}.} \tag{204.9.5}$$

Der korrekte positive Typ ist ausschließlich:
$$\boxed{D \in \operatorname{Der}(A_{\mathrm{alg}}, A_{C^*})_1.} \tag{204.9.6}$$

---

## 204.10 — Endstatus

$$[O\text{-}204\text{-}1] \qquad \checkmark[K]$$

Die gesättigte dyadische Folge $X_N = \sum_{j=0}^{N-1}c_j q_j + c_N P_N$ ist typkorrekt in $B_{\mathrm{alg}} \subset A_{\mathrm{alg}}$ konstruiert und nicht norm-Cauchy.

$$[O\text{-}204\text{-}2] \qquad \checkmark[M]$$

Alle Generatorkommutatoren konvergieren in Norm. Sie definieren eine wohldefinierte neutrale Derivation $D: A_{\mathrm{alg}} \to A_{C^*}$ mit den Formeln (204.6.6/7/8). Die Derivation ist bezüglich der $C^*$-Norm unbeschränkt.

$$[O\text{-}204\text{-}3] \qquad \checkmark[M]$$

Die Derivation ist nicht inner mit Implementierer aus $A_{C^*}$; in der kanonischen Semigruppendarstellung existiert kein beschränkter Implementierer.

$$[O\text{-}204\text{-}4] \qquad \checkmark[M]_{\mathrm{neg}}$$

Die Behauptung, dieser Kandidat liefere eine algebraische Klasse in $HH^1(A_{\mathrm{alg}}, A_{\mathrm{alg}})$, ist für den konkret geprüften Kandidaten ausgeschlossen, weil $D(\mu_2) \notin A_{\mathrm{alg}}$.

$$[O\text{-}204\text{-}5] \qquad \checkmark[M]_{\mathrm{neg}}$$

Der Kandidat ist neutral: $D\bigl((A_{\mathrm{alg}})_g\bigr) \subseteq (A_{C^*})_g$ mit Gewicht $1_\Gamma$. Eine geladene Variante $g \neq 1$ folgt daraus nicht.

---

## 204.11 — DAG-Konsequenz und offene Route

Der offene Knoten $[O\text{-}203\text{-}4]$ besitzt einen positiven analytischen Teiltreffer:
$$\boxed{\exists\, D \in \operatorname{Der}(A_{\mathrm{alg}}, A_{C^*})_1 \text{ normunbeschränkt und } A_{C^*}\text{-äußer}.}$$

Nicht geschlossen werden dadurch:

- $D(A_{\mathrm{alg}}) \subseteq A_{\mathrm{alg}}$ ?$[O]$
- $\exists\, D_g \in \operatorname{Der}(A_{\mathrm{alg}}, A_{\mathrm{alg}})_g$, $g \neq 1$ ?$[O]$
- Typkorrekte Kopplung an Cup-/Dualzyklusapparat (NEU-193–NEU-198) ?$[O]$

```
[O-199-3]_sing (?[O])
      |
      +---> [O-203-4] ✓[M]  (analytische neutrale Route: NEU-204)
      |           |
      |           +---> [O-204-1] ✓[K]
      |           +---> [O-204-2] ✓[M]
      |           +---> [O-204-3] ✓[M]
      |           +---> [O-204-4] ✓[M]_neg  (kein alg. HH^1)
      |           +---> [O-204-5] ✓[M]_neg  (neutral, nicht geladen)
      |
      +---> geladene Route  ?[O]  (nächste Architekturentscheidung)
```

**Offene Architekturentscheidung:**
$$\boxed{\text{Kann die dyadische Schalenregularisierung durch einen homogenen Faktor geladen werden,}\\\text{ohne die Konvergenz der Kommutatoren mit } e(r) \text{ zu zerstören?}}$$
