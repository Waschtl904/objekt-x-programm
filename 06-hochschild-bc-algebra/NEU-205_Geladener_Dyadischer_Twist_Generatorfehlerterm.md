# NEU-205 — Geladener Dyadischer Twist: Generatorfehlerterm und Ausschluss naiver Verschiebungsansätze

**Status:** revidiert v2 (2026-07-19) — [O-205-4] korrigiert, Arch. (II) und (III) ausgeschlossen  
**Erstellt:** 2026-07-19  
**Vorgänger:** NEU-204 ([O-204-5] ✓[M]_neg, neutral)  
**Ziel:** Erster exakter Fehlerterm im $e(r)$-Kommutator für homogen geladene Varianten von $X_N$

---

## 205.0 — Motivation und Rahmen

NEU-204 konstruierte eine neutrale äußere Derivation $D \in \operatorname{Der}(A_{\mathrm{alg}}, A_{C^*})_1$. Für eine geladene Derivation $D_g$ mit $g \neq 1$ müsste $D_g(e(r)) \neq 0$ gelten.

Der naive Ansatz: Ersetze $X_N$ durch $Y_N := V_g X_N$, wobei $V_g \in A_g$ ein homogener Verschiebungsfaktor ist. Ziel dieses Knotens ist die exakte Berechnung des Fehlerterms $[Y_N, e(r)]$ für drei natürliche Platzierungen:
$$Y_N^{(L)} := V_g X_N, \qquad Y_N^{(R)} := X_N V_g, \qquad Y_N^{(S)} := \mu_m X_N \mu_n^*.$$

---

## 205.1 — Grundrelation: $e(r)$-Kommutator in der BC-Algebra

Die Standardrelationen:
$$\mu_k e(r) = e(kr)\mu_k, \qquad e(r)\mu_k^* = \mu_k^* e(kr). \tag{205.1.1}$$

Für $V_g = \mu_m\mu_n^*$, $g = m/n$, $(m,n)=1$:
$$[\mu_m\mu_n^*, e(r)] = \mu_m(e(nr)-e(mr))\mu_n^*. \tag{205.1.2}$$

Ferner liegt $M_{g,r} := e(nr)-e(mr) \in B_{\mathrm{alg}}$ lokal konstant auf $\widehat{\mathbb{Z}}$, und
$$M_{g,r}(0) = e(0)-e(0) = 0.$$
Daher existiert eine nichtleere kloffen-offene Umgebung $U \ni 0$ in $\widehat{\mathbb{Z}}$ mit $M_{g,r}|_U = 0$.

---

## 205.2 — Fall (L): Naive Linksverschiebung $Y_N^{(L)} = V_g X_N$

Da $X_N \in B_{\mathrm{alg}}$ abelsch:
$$\boxed{[Y_N^{(L)}, e(r)] = [V_g, e(r)]\,X_N = \mu_m M_{g,r} \mu_n^* X_N.} \tag{205.2.1}$$

**Untere Schranke für den konkreten dyadischen $X_N$.** Mit $X_N = \sum_{j=0}^{N-1}c_j q_j + c_N P_N$ wirkt $\mu_n^* X_N$ auf Schale $v_2 = J$ (für $n$ ungerade und $k = 2^J \cdot u$, $n \mid u$) durch den Koeffizienten $c_J$. Da $M_{g,r}$ außerhalb von $U$ gleichmäßig positiv ist und die dyadischen Schalen $q_J \cdot \ell^2(\mathbb{N}^\times)$ für alle $J$ außerhalb von $U$ Spektrum tragen:
$$\|[Y_N^{(L)}, e(r)]\|_{v_2=J} \geq \|M_{g,r}|_{q_J}\| \cdot c_J \longrightarrow \infty. \tag{205.2.2}$$

Somit divergiert $\|[Y_N^{(L)}, e(r)]\|$ für den konkret geprüften dyadischen $X_N$ und $r \notin \frac{1}{m-n}\mathbb{Z}$.

**Wichtige Einschränkung.** Die obere Schranke $\|[Y_N^{(L)}, e(r)]\| \leq 2\|X_N\|$ mit $\|X_N\| \to \infty$ allein liefert keine Divergenz. Das Argument verwendet wesentlich die spektrale Struktur des dyadischen $X_N$ auf den hohen Schalen.

**Status: [O-205-1] $\checkmark[M]_{\mathrm{neg}}$** — kandidatenspezifisch für den dyadischen $X_N$ und $g \neq 1$.

---

## 205.3 — Fall (R): Naive Rechtsverschiebung $Y_N^{(R)} = X_N V_g$

$$[Y_N^{(R)}, e(r)] = X_N [V_g, e(r)] = X_N \mu_m M_{g,r} \mu_n^*. \tag{205.3.1}$$

Dieselbe untere Schrankenstrategie wie in §205.2.

**Status: [O-205-2] $\checkmark[M]_{\mathrm{neg}}$** — kandidatenspezifisch, symmetrisch zu Fall (L).

---

## 205.4 — Fall (S): Sandwich $Y_N^{(S)} = \mu_m X_N \mu_n^*$

Mit den BC-Relationen $\mu_n^* e(r) = e(nr)\mu_n^*$ und $e(r)\mu_m = \mu_m e(mr)$:
$$\mu_m X_N \mu_n^* e(r) = \mu_m X_N e(nr) \mu_n^* = e(mnr)\,\mu_m X_N \mu_n^*, \tag{205.4.1}$$
$$e(r)\,\mu_m X_N \mu_n^* = \mu_m e(mr) X_N \mu_n^* = e(mr)\,\mu_m X_N \mu_n^* \cdot (\text{rechts}). \tag{205.4.2}$$

Der Fehlerterm ist multiplikativ:
$$\boxed{[Y_N^{(S)}, e(r)] = (e(mnr)-e(mr))\, Y_N^{(S)}.} \tag{205.4.3}$$

Für den konkreten dyadischen $X_N$ gilt $\|Y_N^{(S)}\| = \|X_N\| = c_N \to \infty$, und $\|e(mnr)-e(mr)\| > 0$ für $r$ außerhalb einer endlichen Ausnahmemenge.

**Status: [O-205-3] $\checkmark[M]_{\mathrm{neg}}$** — kandidatenspezifisch.

---

## 205.5 — Revidierter Dilemma-Satz (v2)

**Was nicht gilt (Korrektur gegenüber v1):**

Aus $\|X_N\| \to \infty$ allein folgt für allgemeines $X_N \in B_{\mathrm{alg}}$ **keine** Divergenz von $\|[V_g X_N, e(r)]\|$. Gegenbeispiel: Wählt man $X_N = t_N p$ mit $p = 1_U \in B_{\mathrm{alg}}$ und $U$ die Nullumgebung mit $M_{g,r}|_U = 0$, so gilt $\|X_N\| = t_N \to \infty$ aber $[V_g X_N, e(r)] = \mu_m M_{g,r} \mu_n^* X_N = 0$ (da $M_{g,r} \cdot p = 0$). Sogar für tiefer wachsende $p_N = E_{L_N}$ (sukzessive durch alle relevan-ten Charakterordnungen teilbar) kann $[V_g X_N, e(r)] = 0$ für jeden festen $r$ ab einem $N_0(r)$ gelten.

Ferner: Äußerheit erfordert nicht notwendig $\|X_N\| \to \infty$; eine approximierende Implementiererfolge könnte normbeschränkt, aber nicht normkonvergent sein.

**Was gesichert ist:**

$$\boxed{\text{Für den konkreten dyadischen }X_N\text{ aus NEU-204 und }g\neq1}$$
$$\boxed{\text{divergieren }\|[V_g X_N, e(r)]\|\text{ für alle drei Platzierungen (L), (R), (S).}} \tag{205.5.1}$$

Das Argument benutzt wesentlich die Ausschöpfung aller dyadischen Schalen durch $X_N$ und die Positivität von $M_{g,r}$ auf dem dyadischen Hochbewertungsschwanz.

**Status: [O-205-4] $\checkmark[M]_{\mathrm{part}}$** — dyadisches Dilemma bewiesen; keine universelle Aussage für beliebiges $X_N \in B_{\mathrm{alg}}$.

---

## 205.6 — Ausschluss von Architektur (II): keine Projektionen in $A_g$, $g \neq 1$

**Satz.** Für $g \neq 1$ gilt: $A_g$ enthält keine nichttrivialen Projektionen.

**Beweis.** Sei $q \in A_g$ eine Projektion, also $q^2 = q$. Da $A_{\mathrm{alg}} = \bigoplus_h A_h$ direkt graduiert ist, liegt $q^2 \in A_{g^2}$ und $q \in A_g$. Aus $q^2 = q \neq 0$ folgt $g^2 = g$ in $\mathbb{Q}_+^\times$, also $g = 1$. Widerspruch. Alternativ: $q = q^*$ impliziert $q \in A_g \cap A_{g^{-1}}$; für $g \neq 1$ ist $g \neq g^{-1}$, also $q = 0$. $\square$

$$\boxed{g \neq 1 \Longrightarrow A_g \text{ enthält keine nichttrivialen Projektionen.}} \tag{205.6.1}$$

**Status: [O-205-5b] $\checkmark[M]_{\mathrm{neg}}$** — Architektur (II) in der formulierten Projektionsform ausgeschlossen.

---

## 205.7 — Architektur (III): relationsangepasster Twist ausgeschlossen

Für einen $N$-abhängigen Twist $V_g(N) \in A_g$ mit $\|[V_g(N), e(r)]\| \cdot \|X_N\| \to 0$ müsste $\|V_g(N)\| \to 0$ gelten. Ein homogenes Element $V_g(N) = \mu_m f_N \mu_n^*$ mit $\|V_g(N)\| \to 0$ könnte höchstens aus $f_N \in B_{\mathrm{alg}}$ mit $\|f_N\| \to 0$ bestehen. Ein solches Element ist kein Isometrieelement und erzeugt kein nicht-verschwindendes Potential. Die Kommutatoren $[V_g(N) X_N, \mu_k]$ würden ebenfalls gegen null gehen — kein äußerer Beitrag.

**Status: [O-205-5c] $\checkmark[M]_{\mathrm{neg}}$** — Architektur (III) ausgeschlossen.

---

## 205.8 — Richtige nächste Architektur: homogene Partialisometrieschalen

Aus (205.6.1) folgt: Geladene Schalen können keine Projektionen sein. Der natürliche Ersatz sind **Partialisometrien** $w_j \in A_g$ mit Orthogonali-tätsbedingungen:
$$w_j^* w_\ell = 0 \quad (j \neq \ell) \qquad \text{oder} \qquad w_j w_\ell^* = 0. \tag{205.8.1}$$

Der natürliche Modelltyp ist:
$$w_j = \mu_m p_j \mu_n^*, \qquad g = \frac{m}{n}, \tag{205.8.2}$$
wobei die neutralen Projektionen $p_j \in B_{\mathrm{alg}}$ an die Nullmengen der Charakterdifferenzen $M_{g,r} = e(nr)-e(mr)$ angepasst werden müssen:
$$\operatorname{supp}(p_j) \subseteq \{x \in \widehat{\mathbb{Z}} : M_{g,r}(x) = 0\} \quad \text{für relevante } r. \tag{205.8.3}$$

Dies führt auf den nächsten atomaren Knoten:

$$\boxed{\texttt{NEU-206\_Homogene\_Partialisometrieschalen\_Orthogonalitaet\_und\_Charakterkern.md}}$$

mit zwei unmittelbaren Teilzielen:

- **[O-206-1] $\checkmark[M]_{\mathrm{neg}}$** (bereits gesichert durch §205.6): keine nichttrivialen Projektionen in $A_g$, $g \neq 1$.
- **[O-206-2] ?[O]**: Existenz einer Familie $w_j \in A_g$ gemäß (205.8.2) mit $w_j^* w_\ell = 0$ $(j \neq \ell)$, normkonvergenten Kommutatoren mit jedem $e(r)$, und nicht-innerer Grenzderivation.

---

## 205.9 — Endstatus (v2)

| Knoten | Status | Inhalt |
|---|---|---|
| [O-205-1] | $\checkmark[M]_{\mathrm{neg}}$ | naive Linksverschiebung $V_g X_N$ (dyadisch): normdivergenter $e(r)$-Fehlerterm |
| [O-205-2] | $\checkmark[M]_{\mathrm{neg}}$ | naive Rechtsverschiebung $X_N V_g$ (dyadisch): symmetrisch ausgeschlossen |
| [O-205-3] | $\checkmark[M]_{\mathrm{neg}}$ | Sandwich $\mu_m X_N \mu_n^*$ (dyadisch): multiplikativer Fehlerterm, divergiert |
| [O-205-4] | $\checkmark[M]_{\mathrm{part}}$ | dyadisches Dilemma bewiesen; **keine** universelle Aussage für $X_N \in B_{\mathrm{alg}}$ allgemein |
| [O-205-5a] | ?[O] | Architektur (I): modifiziertes $\tilde{q}_j \notin B_{\mathrm{alg}}$ mit summierbaren Kommutatoren |
| [O-205-5b] | $\checkmark[M]_{\mathrm{neg}}$ | Architektur (II): keine nichttrivialen Projektionen in $A_g$, $g \neq 1$ |
| [O-205-5c] | $\checkmark[M]_{\mathrm{neg}}$ | Architektur (III): $N$-abhängiger Twist inkompatibel mit Äußerheit |

**Zentraler Befund (NEU-205):**

$$\boxed{\text{Die drei naiven geladenen Platzierungen des dyadischen }X_N\text{ scheitern kandidatenspezifisch.}}$$
$$\boxed{\text{Kein universeller Ausschlusssatz für beliebiges }X_N\in B_{\mathrm{alg}}.}$$

---

## 205.10 — DAG-Stand (v2)

```
[O-199-3]_sing (?[O])
      |
      +---> [O-203-4] ✓[M]  (analytisch neutral: NEU-204)
      |           |
      |           +---> [O-204-1..3] ✓[K/M/M]
      |           +---> [O-204-4/5]  ✓[M]_neg  (kein HH^1_alg, neutral)
      |
      +---> geladene Route ?[O]
                  |
                  +---> naive (L/R/S) dyadisch  [O-205-1..3] ✓[M]_neg
                  +---> dyadisches Dilemma       [O-205-4]   ✓[M]_part
                  +---> Arch. (II) Projektionen  [O-205-5b]  ✓[M]_neg
                  +---> Arch. (III) Twist        [O-205-5c]  ✓[M]_neg
                  +---> Arch. (I) modif. Schalen [O-205-5a]  ?[O]
                  +---> Partialisometrieschalen  [O-206-2]   ?[O]  --> NEU-206
```
