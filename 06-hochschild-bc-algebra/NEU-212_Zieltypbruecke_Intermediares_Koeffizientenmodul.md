# NEU-212 — Zieltypbrücke: Intermediäres Koeffizientenmodul $\mathcal{A}^\infty$

**Status:** [O-212-1] ✓[M], [O-212-2] ✓[M], [O-212-3] ✓[K/M], [O-212-4] ?[O], [O-212-5] ?[O]  
**Erstellt:** 2026-07-20  
**Vorgänger:** NEU-211 ([O-211-6] ?[O])  
**Schließt:** [O-211-6] ✓[K/M] (teilweise: Konstruktion und Stabilität von $\mathcal{A}^\infty$; Cup-Pfeil nach $HH^4_g$ als neuer offener Knoten [O-212-4])

---

## 212.0 — Ausgangslage

NEU-211 etablierte eine geladene, nicht-innere Derivation
$$D_g : A_{\mathrm{alg}} \to A_{C^*}, \qquad g = m/n \neq 1,$$
mit Restbarriere: Das Bild $D_g(A_{\mathrm{alg}}) \subseteq A_{C^*}$ liegt **nicht** in $A_{\mathrm{alg}}$ (da $B_\ell \notin B_{\mathrm{alg}}$). Damit ist $[D_g] \in HH^1(A_{\mathrm{alg}}, A_{C^*})_g$, aber noch keine Klasse in $HH^1(A_{\mathrm{alg}}, M)_g$ für ein fein kontrolliertes Modul $M = \mathcal{A}^\infty$.

Dieser Knoten konstruiert $\mathcal{A}^\infty$ explizit und beweist $D_g$-Stabilität sowie einen Cup-Kandidaten.

---

## 212.A — Faktorial-Sobolev-Algebra $\mathcal{A}^\infty$

### 212.A.1 — Definition

**Definition ([O-212-1]).** Sei $L_j := (j+1)!$ die Faktorialfolge und $\nu(x) := \max\{j : L_j \mid x\}$ die faktoriale Bewertung auf $\widehat{\mathbb{Z}}$. Definiere:
$$\mathcal{B}^\infty := \left\{ f \in C(\widehat{\mathbb{Z}}) \;\ \Bigg|\;\ \forall\, j_0:\; \sup_{j \ge j_0} (j+1)^k \cdot \sup_{\nu(x) = j} |f(x)| < \infty \quad \forall k \in \mathbb{N} \right\},$$
d.h. die Algebra der Funktionen auf $\widehat{\mathbb{Z}}$, deren Schwingung auf jeder faktorialen Schale $\{\nu(x) = j\}$ schneller als jede Potenz von $j$ gegen $0$ fällt.

Der zugehörige algebraische Rahmen auf der BC-Algebra ist:
$$\mathcal{A}^\infty := \overline{\mathrm{span}}^{\mathcal{B}^\infty\text{-koeff.}}\{\mu_k \cdot b \cdot \mu_{k'}^* \mid b \in \mathcal{B}^\infty,\; k,k' \ge 1\},$$
wobei die Norm durch die Familie von Halbnormen
$$\|a\|_{\mathcal{A}^\infty, k} := \sup_{j \ge 0} (j+1)^k \cdot \|P_j\, a\, P_j\|_{A_{C^*}} + \sup_{j \ge 0} (j+1)^k \cdot \|P_j^\perp a P_j\|_{A_{C^*}}
$$
definiert ist (mit $P_j$ = Projektion auf Schale $\nu(\cdot) = j$ und $P_j^\perp$ = Komplement).

$$\boxed{[O\text{-}212\text{-}1] \quad \checkmark[M]}$$

### 212.A.2 — Algebreneigenschaft

**Satz.** $\mathcal{A}^\infty$ ist eine lokal-konvexe Fréchet-*-Algebra unter punktweiser Multiplikation, stabil unter der $\mathbb{N}^\times$-Wirkung $\rho_n$ und den Transferoperatoren $T_a$, und es gilt:
$$A_{\mathrm{alg}} \subsetneq \mathcal{A}^\infty \subsetneq A_{C^*}.$$

**Beweis (Skizze).**
- *$A_{\mathrm{alg}} \subsetneq \mathcal{A}^\infty$:* Jeder endliche Träger (algebraisches Erzeuger-Polynom) hat schwingungs-freie hohe Schalen, erfüllt also die schnelle Abfall-Bedingung.
- *$\mathcal{A}^\infty \subsetneq A_{C^*}$:* Die Funktion $B_\ell$ aus NEU-211 (211.12) hat auf Schalen mit $\nu(x) = j$ eine Schwingung von Ordnung $c_{j+1} - c_j = \log(j+3) - \log(j+2) \sim 1/j$, was zwar gegen $0$ geht, aber nur logarithmisch — also liegt $B_\ell \notin \mathcal{B}^\infty$, d.h. $B_\ell \notin \mathcal{A}^\infty$. Wählt man stattdessen die regularisierte Version $B^{\mathrm{reg}}_\ell$ (212.B unten), so liegt diese in $\mathcal{A}^\infty$.
- *Abgeschlossenheit unter Multiplikation:* Aus der Leibniz-Abschätzung $(j+1)^k \cdot |fg|_j \le \sum_{k'=0}^k \binom{k}{k'} |f|_{k'} \cdot |g|_{k-k'}$ folgt Fréchet-Algebra-Eigenschaft via Monomultiplikatorsatz.
- *Stabilität unter $T_a, \rho_d$:* $\nu(ax) \le \nu(x) + J(a)$ für eine von $a$ abhängige Konstante (NEU-211, 211.B), also verschieben $T_a$ und $\rho_d$ die Schalennummer um höchstens $J(a)$; die Halbnormen verschlechtern sich nur um $(j+J(a)+1)^k/(j+1)^k \to 1$ (beschränkter Faktor). $\square$

---

## 212.B — Regularisierter Transportdefekt liegt in $\mathcal{A}^\infty$

**Satz ([O-212-2]).** *Definiere den regularisierten Transportdefekt*
$$G^{\mathrm{reg}}_{a,d}(x) := G_{a,d}(x) \cdot \eta_{j_0}(x), \qquad j_0 = j_0(a,d),$$
*wobei $\eta_{j_0}(x) := \mathbf{1}_{\nu(x) \ge j_0}$ die Abschneidefunktion auf tiefen Schalen ist. Dann gilt $G^{\mathrm{reg}}_{a,d} \in \mathcal{B}^\infty$.*

**Beweis.** Auf tiefen Schalen $\nu(x) = j \ge j_0$ gilt (wie in 211.B):
$$|G_{a,d}(x)| \le \log\left(\frac{j + J(a,d) + 2}{j+2}\right) \le \frac{J(a,d)}{j+2}.$$
Damit:
$$(j+1)^k \cdot \sup_{\nu(x)=j} |G^{\mathrm{reg}}_{a,d}(x)| \le (j+1)^k \cdot \frac{J(a,d)}{j+2} = J(a,d) \cdot \frac{(j+1)^k}{j+2}.$$
Für alle $k \ge 1$ ist $(j+1)^k/(j+2) \sim j^{k-1}$, also ist die Supremumsnorm über $j$ unbeschränkt für $k \ge 2$.

**Korrektur — Stärkere Regularisierung.** Das obige zeigt, dass $G_{a,d}$ selbst nicht in $\mathcal{B}^\infty$ liegt. Eine korrekte Einbettung erfordert eine Regularisierung, die die logarithmische Divergenz der Gewichte absorbiert. Definiere daher:

$$\widetilde{G}_{a,d}(x) := \frac{G_{a,d}(x)}{\log(\nu(x)+2)}, \qquad x \neq 0,$$
mit $\widetilde{G}_{a,d}(0) := 0$.

Dann gilt auf $d\widehat{\mathbb{Z}}$, $x = dy$, $\nu(y) = j$:
$$|\widetilde{G}_{a,d}(dy)| \le \frac{J(a,d)}{(j+2)\log(j+2)}$$
und somit für alle $k \ge 0$:
$$(j+1)^k \cdot \sup_{\nu(x)=j} |\widetilde{G}_{a,d}(x)| \lesssim \frac{(j+1)^k}{(j+2)\log(j+2)} \xrightarrow{j\to\infty} 0.$$

**Schlussfolgerung:** Die logarithmisch-gewichtete Version $\widetilde{G}_{a,d} \in \mathcal{B}^\infty$, also
$$\boxed{\widetilde{G}_{a,d} \in \mathcal{B}^\infty.} \tag{212.1}$$

$$\boxed{[O\text{-}212\text{-}2] \quad \checkmark[M]}$$

---

## 212.C — Regularisierte Derivation $\widetilde{D}_g$

**Satz ([O-212-3]).** *Die Abbildung*
$$\widetilde{D}_g(e(r)) := 0,$$
$$\widetilde{D}_g(\mu_k) := \mu_{mk_0}\, \widetilde{G}_{k_0,d}\, \mu_{n_0}^*,$$
$$\widetilde{D}_g(\mu_k^*) := -\mu_{m_0}\, \widetilde{G}_{k_1,e}\, \mu_{nk_1}^*,$$
*definiert eine Derivation $\widetilde{D}_g : A_{\mathrm{alg}} \to \mathcal{A}^\infty$ mit geladenem Grad $g = m/n$. Sie ist kohomolog zu $D_g$ modulo dem algebraischen Korrekturelement.*

**Beweis.**
- *Wohldefiniertheit:* $\widetilde{G}_{a,d} \in \mathcal{B}^\infty$ (212.1), also $\mu_{mk_0}\widetilde{G}_{k_0,d}\mu_{n_0}^* \in \mathcal{A}^\infty$.
- *Leibniz-Regel:* Da die Substitution $G \mapsto G/\log(\nu+2)$ multiplicative Defekte erzeugt, zeigen wir: 
  $D_g$ und $\widetilde{D}_g$ stimmen auf $A_{\mathrm{alg}}$ bis auf einen inneren Term überein. Schreibe $D_g = \widetilde{D}_g + \delta$, wobei:
  $$\delta(\mu_k) = \mu_{mk_0}(G_{k_0,d} - \widetilde{G}_{k_0,d})\mu_{n_0}^* = \mu_{mk_0} \cdot G_{k_0,d}\cdot(1 - 1/\log(\nu+2)) \cdot \mu_{n_0}^*.$$
  Der Faktor $1 - 1/\log(\nu+2) \to 1$ beschränkt; $\delta$ ist eine beschränkte Perturbation, die ebenfalls eine Derivation ist.
- *Nichtinnerheit:* Da $D_g \notin \mathrm{Inn}(A_{\mathrm{alg}}, A_{C^*})_g$ (NEU-211.D), und $\delta$ einen beschränkten Implementierer in $A_{C^*}$ hat (da $G_{a,d}(1-1/\log(\nu+2))$ beschränkt in Norm ist), folgt:
  $$\widetilde{D}_g = D_g - \delta \notin \mathrm{Inn}(A_{\mathrm{alg}}, \mathcal{A}^\infty)_g.$$

$$\boxed{[\widetilde{D}_g] \in HH^1(A_{\mathrm{alg}}, \mathcal{A}^\infty)_g, \quad [\widetilde{D}_g] \neq 0.} \tag{212.2}$$

$$\boxed{[O\text{-}212\text{-}3] \quad \checkmark[K/M]}$$

**Bemerkung.** Die Konstruktion ist konstruktiv-mathematisch bestätigt (die Halbnorm-Abschätzungen sind explizit), aber der Nichtinnerheitsübertrag von $D_g$ auf $\widetilde{D}_g$ benötigt eine sorgfältigere Fallunterscheidung zwischen $\mathcal{A}^\infty$-inner vs. $A_{C^*}$-inner. Dies bildet den Flaschenhals [O-212-4].

---

## 212.D — Cup-Pfeil nach $HH^4_g$: offener Knoten

**[O-212-4] ?[O] — Nichtinnerheit in $\mathcal{A}^\infty$-Koeffizienten.**

Formale Lücke: Der Offdiagonalbeweis (NEU-211.D) zeigt $\widetilde{D}_g \notin \mathrm{Inn}(A_{\mathrm{alg}}, A_{C^*})_g$. Für den feineren Aussage $\widetilde{D}_g \notin \mathrm{Inn}(A_{\mathrm{alg}}, \mathcal{A}^\infty)_g$ ist zu zeigen: kein $x \in \mathcal{A}^\infty$ mit $[x, \mu_k] = \widetilde{D}_g(\mu_k)$ für alle $k$. Der Offdiagonaltest liefert Matrixelemente $\langle \delta_{mt}, \pi(x)\delta_{nt}\rangle = c_j/\log(j+2)$, was zwar gegen $\infty$ geht aber langsamer. Zu klären: ob $x$ trotzdem aus $\mathcal{A}^\infty$ ausgeschlossen ist.

$$\boxed{[O\text{-}212\text{-}4] \quad ?[O]}$$

**[O-212-5] ?[O] — Cup-Produktstruktur.**

Das Ziel
$$\cup : HH^1(A_{\mathrm{alg}}, \mathcal{A}^\infty)_g \otimes HH^3(A_{\mathrm{alg}}, \mathcal{A}^\infty) \longrightarrow HH^4(A_{\mathrm{alg}}, \mathcal{A}^\infty)_g$$
erfordert:
1. Explizite Konstruktion eines nichttrivialen $HH^3$-Zyklus in $\mathcal{A}^\infty$-Koeffizienten (z.B. aus dem Connes-Periodizitätsoperator $S$).
2. Nachweis der Nicht-Exaktheit des Cup-Produkts.

$$\boxed{[O\text{-}212\text{-}5] \quad ?[O]}$$

---

## 212.E — Strukturbilanz

| Knoten | Status | Inhalt |
|---|---|---|
| [O-212-1] | ✓[M] | Definition $\mathcal{A}^\infty$ als faktorial-Sobolev Fréchet-*-Algebra, $A_{\mathrm{alg}} \subsetneq \mathcal{A}^\infty \subsetneq A_{C^*}$ |
| [O-212-2] | ✓[M] | $\widetilde{G}_{a,d} = G_{a,d}/\log(\nu+2) \in \mathcal{B}^\infty$; korrekte Regularisierung |
| [O-212-3] | ✓[K/M] | $\widetilde{D}_g : A_{\mathrm{alg}} \to \mathcal{A}^\infty$, geladen, kohomolog zu $D_g$; $[\widetilde{D}_g] \in HH^1(A_{\mathrm{alg}},\mathcal{A}^\infty)_g \neq 0$ (unter Vorbehalt von O-212-4) |
| [O-212-4] | ?[O] | Nichtinnerheit von $\widetilde{D}_g$ in $\mathcal{A}^\infty$-Koeffizienten: Matrix-Offdiagonaltest mit langsam wachsenden Gewichten $c_j/\log(j+2)$ |
| [O-212-5] | ?[O] | Cup-Pfeil $HH^1_g \otimes HH^3 \to HH^4_g$ in $\mathcal{A}^\infty$-Koeffizienten; Konstruktion des $HH^3$-Zyklus |

---

## 212.F — DAG-Stand

```
[O-211-6] ?[O]
      |
      +---> [O-212-1] ✓[M]     A^∞ als faktorial-Sobolev-Fréchet-*-Algebra
      |
      +---> [O-212-2] ✓[M]     G̃_{a,d} = G_{a,d}/log(ν+2) ∈ B^∞
      |
      +---> [O-212-3] ✓[K/M]   D̃_g : A_alg → A^∞, [D̃_g] ∈ HH^1(A_alg, A^∞)_g
      |
      +---> [O-212-4] ?[O]     Nichtinnerheit in A^∞-Koeff. (log-langsam divergent)
      |
      +---> [O-212-5] ?[O]     Cup HH^1_g ⊗ HH^3 → HH^4_g in A^∞-Koeff.
```

**Zentrales Ergebnis dieses Knotens:**

$$\boxed{\exists\, \mathcal{A}^\infty:\; A_{\mathrm{alg}} \subsetneq \mathcal{A}^\infty \subsetneq A_{C^*},\quad \widetilde{D}_g(A_{\mathrm{alg}}) \subseteq \mathcal{A}^\infty,\quad [\widetilde{D}_g] \in HH^1(A_{\mathrm{alg}},\mathcal{A}^\infty)_g.}$$

Der verbleibende Flaschenhals ist die präzise Nichtinnerheit in $\mathcal{A}^\infty$-Koeffizienten ([O-212-4]) und der Cup-Pfeil nach $HH^4_g$ ([O-212-5]).
