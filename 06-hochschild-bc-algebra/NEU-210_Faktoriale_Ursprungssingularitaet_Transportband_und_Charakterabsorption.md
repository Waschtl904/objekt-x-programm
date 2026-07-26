# NEU-210 — Faktoriale Ursprungssingularität, Transportband und Charakterabsorption

**Status:** [O-210-1] ✓[M], [O-210-2] ✓[K], [O-210-3] ✓[M], [O-210-4] ✓[M], [O-210-5] ✓[M]_part; [O-210-6] ?[O]  
**Erstellt:** 2026-07-20  
**Vorgänger:** NEU-209 ([O-209-5] ?[O], [O-209-6] ?[O])  
**Schließt:** [O-209-5] ✓[M], [O-209-6] ✓[M]  
**Ziel:** Exakte Berechnung von $Z_g$; Konstruktion des faktorialen Ursprungspotentials; Nachweis des Transportbandes und der Charakterabsorption; geladener Sandwichkandidat im teilerfremden Sektor

---

## 210.0 — Ausgangslage

NEU-209 hat zwei offene Knoten hinterlassen:
- **[O-209-5]:** Berechnung der gemeinsamen Charakterkernmenge $Z_g$.
- **[O-209-6]:** Konstruktion eines Potentials mit $\operatorname{Sing}(X) \subseteq \{0\}$ und separierbaren Transportdifferenzen.

NEU-210 schließt beide Knoten und identifiziert den bislang stärksten direkten Kandidaten für den geladenen Weg zu Objekt $X$.

**Typologische Vorbemerkung.** Ein positiver Befund aus [O-210-6] würde liefern:
$$D_g : A_{\mathrm{alg}} \longrightarrow A_{C^*}$$
mit geladenem Grad $g = m/n$. Das ist noch nicht $[L_3] \in HH^4$. Erforderlich blieben: $D_g(A_{\mathrm{alg}}) \subseteq A_{\mathrm{alg}}$, $[D_g] \neq 0 \in HH^1(A_{\mathrm{alg}}, A_{\mathrm{alg}})_g$, und anschließend ein typkorrekter Cup-Pfeil nach $HH^4_g$. Der Faktorialkandidat wäre ein **konstruktiver Vorläufer** der Schicht $X.3$, nicht bereits ihre Realisierung.

---

## 210.A — Exakte Berechnung der gemeinsamen Charakterkernmenge

**Formelaudit.** Für $Y = \mu_m b\mu_n^*$ mit $b \in B$ liefern die Standardrelationen
$$e(r)\mu_m = \mu_m e(mr), \qquad \mu_n^* e(r) = e(nr)\mu_n^*$$
den Kommutator
$$[Y, e(r)] = \mu_m b e(nr)\mu_n^* - \mu_m e(mr) b\mu_n^* = \boxed{\mu_m\bigl(e(nr)-e(mr)\bigr)b\,\mu_n^*.} \tag{210.1}$$

Der relevante Fehlermultiplikator ist daher
$$\boxed{M_{m,n;r} = e(nr) - e(mr).} \tag{210.2}$$

**Audithinweis.** Falls in NEU-205 oder NEU-209 stattdessen $e(mnr)-e(mr)$ steht, ist diese Stelle zu korrigieren: Für $n=1$ würde jener Ausdruck identisch verschwinden, obwohl $g=m\neq 1$ geladen sein kann.

**Satz ([O-210-1]).** *Für jeden nichtneutralen reduzierten Grad $g = m/n \neq 1$ gilt*
$$\boxed{Z_g = \bigcap_{r \in \mathbb Q/\mathbb Z} Z(M_{m,n;r}) = \{0\}.} \tag{210.3}$$

**Beweis.** Sei $x \in \widehat{\mathbb Z}$ mit $M_{m,n;r}(x) = 0$ für alle $r \in \mathbb Q/\mathbb Z$. Dann gilt
$$e(r)\bigl((n-m)x\bigr) = 1 \quad\text{für alle } r.$$
Da $\mathbb Q/\mathbb Z$ die Punkte von $\widehat{\mathbb Z}$ trennt (Pontrjagin-Dualität), folgt $(n-m)x = 0$. Da $\widehat{\mathbb Z} \cong \prod_p \mathbb Z_p$ torsionsfrei ist und $m \neq n$, folgt $x = 0$. $\square$

**Schließt [O-209-5] ✓[M].**

$$\boxed{[O\text{-}210\text{-}1] \quad \checkmark[M]}$$

---

## 210.B — Faktoriale Ursprungssingularität

**Definition ([O-210-2]).** Setze
$$L_j := (j+1)!, \qquad P_j := E_{L_j}, \qquad q_j := P_j - P_{j+1}. \tag{210.4}$$

Eigenschaften:
- $P_0 = 1$, $P_{j+1} \le P_j$, $q_j q_\ell = 0$ für $j \neq \ell$.
- Da $v_p((j+1)!) \to \infty$ für jede Primzahl $p$: $\bigcap_{j\ge 0} L_j\widehat{\mathbb Z} = \{0\}.$ \tag{210.5}

Definiere logarithmische Koeffizienten $c_j := \log(j+2)$ und das faktoriale Potential
$$\boxed{X_N := \sum_{j=0}^{N-1} c_j q_j + c_N P_N.} \tag{210.6}$$

Für $x \neq 0$ sei $\nu(x) := \max\{j : x \in L_j\widehat{\mathbb Z}\}$ (wohldefiniert wegen (210.5)). Dann:
$$X_N(x) = c_{\min(\nu(x),N)}. \tag{210.7}$$

Für $x \neq 0$ stabilisiert $X_N(x) = c_{\nu(x)}$ ab $N > \nu(x)$; für $x = 0$ gilt $X_N(0) = c_N \to \infty$. Somit:
$$\boxed{\operatorname{Sing}(X) = \{0\}.} \tag{210.8}$$

**Schließt [O-209-6] ✓[M].**

$$\boxed{[O\text{-}210\text{-}2] \quad \checkmark[K]}$$

---

## 210.C — Transportband und normkonvergente Kommutatoren

**Satz ([O-210-3]).** *Für jedes $k \ge 1$ gilt das Transportband*
$$\boxed{P_j \le E_{L_j/k} \le P_{j-k},} \tag{210.12}$$
*und die $\mu_k$-Kommutatoren konvergieren in Norm.*

**Beweis des Transportbandes.** Für $j \ge k$ gilt $k \mid (j+1)!$, also $L_j/k \in \mathbb N$. Das Produkt der $k$ aufeinanderfolgenden Zahlen $(j-k+2)\cdots(j+1)$ enthält eine durch $k$ teilbare Zahl und ist daher durch $k$ teilbar. Es folgt $(j-k+1)! \mid (j+1)!/k$, also
$$L_{j-k} \mid \frac{L_j}{k} \mid L_j, \tag{210.11}$$
und mit umgekehrter Inklusionsrichtung der Rangeprojektionen: $P_j \le E_{L_j/k} \le P_{j-k}$.

**Gleichmäßiges Transportband.** Für $x \neq 0$:
$$\nu(x) \le \nu(kx) \le \nu(x) + k. \tag{210.13}$$

**Normkonvergenz.** Definiere auf $\widehat{\mathbb Z}\setminus\{0\}$
$$B_k(x) := c_{\nu(kx)} - c_{\nu(x)}, \qquad B_k(0) := 0. \tag{210.14}$$

Aus (210.13):
$$0 \le B_k(x) \le c_{\nu(x)+k} - c_{\nu(x)} = \log\left(\frac{\nu(x)+k+2}{\nu(x)+2}\right) \longrightarrow 0 \quad (\nu(x) \to \infty). \tag{210.16}$$

Da $\nu(x) \to \infty$ für $x \to 0$ in $\widehat{\mathbb Z}$, ist $B_k$ stetig bei $0$, also $B_k \in C(\widehat{\mathbb Z}) = B_{C^*}$.

Algebraisch gilt $X_N\mu_k = \mu_k T_k(X_N)$ mit $T_k(E_L) := E_{L/(L,k)}$, also
$$[X_N, \mu_k] = \mu_k(T_k(X_N) - X_N). \tag{210.17}$$

Die Funktionen $B_{k,N} := T_k(X_N) - X_N$ konvergieren gleichmäßig gegen $B_k$: Für $\nu(x) < N-k$ ist die Sättigung irrelevant; auf dem Tail gilt $|B_{k,N}(x)|, |B_k(x)| \le c_N - c_{N-k} \to 0$. Daher:
$$\boxed{\lim_{N\to\infty}[X_N, \mu_k] = \mu_k B_k,} \tag{210.18}$$
$$\boxed{\lim_{N\to\infty}[X_N, \mu_k^*] = -B_k\mu_k^*.} \tag{210.19}$$

Da $X_N \in B_{\mathrm{alg}}$: $[X_N, e(r)] = 0$.

$$\boxed{[O\text{-}210\text{-}3] \quad \checkmark[M]}$$

---

## 210.D — Charakterabsorption

**Satz ([O-210-4]).** *Sei $M \in B_{\mathrm{alg}}$ lokal konstant mit $M(0) = 0$. Dann existiert $J$ mit*
$$MP_J = 0,$$
*und für alle $N \ge J$ gilt exakt*
$$\boxed{MX_N = \sum_{j=0}^{J-1} c_j Mq_j.} \tag{210.21}$$
*Die Folge $(MX_N)$ wird schließlich konstant.*

**Beweis.** Da $M$ lokal konstant ist, faktorisiert es über $\widehat{\mathbb Z}/L_J\widehat{\mathbb Z}$ für ein geeignetes $J$. Da $M(0) = 0$ und $L_J\widehat{\mathbb Z}$ eine offene Umgebung von $0$ ist auf der $M$ verschwindet, gilt $MP_J = 0$. Für $j \ge J$: $q_j \le P_j \le P_J$, also $Mq_j = 0$. Ebenso $MP_N = 0$ für $N \ge J$. Die Summe (210.21) folgt direkt. $\square$

**Konsequenz für den geladenen Kandidaten.** Für $Y_N := \mu_m X_N \mu_n^*$ ergibt sich aus (210.1) und (210.21):
$$[Y_N, e(r)] = \mu_m M_{m,n;r} X_N \mu_n^*.$$
Da $M_{m,n;r}(0) = e(0) - e(0) = 0$ und $M_{m,n;r}$ lokal konstant, stabilisiert $M_{m,n;r}X_N$ nach endlich vielen Schritten für jedes feste $r$.

$$\boxed{[O\text{-}210\text{-}4] \quad \checkmark[M]}$$

---

## 210.E — Geladener Sandwichkandidat: teilerfremder Sektor

**Satz ([O-210-5], partiell).** *Der geladene Kandidat $Y_N = \mu_m X_N \mu_n^*$ besitzt:*
- *Konvergente $e(r)$-Kommutatoren für alle $r$ (aus 210.D).*
- *Für $(k, mn) = 1$: konvergenten $\mu_k$-Kommutator mit Grenzwert $\mu_{mk} B_k \mu_n^*$.*

**Beweis des teilerfremden Sektors.** Für $(k, mn) = 1$ gilt $\mu_k \mu_m = \mu_{km}$ und $\mu_n^* \mu_k = \mu_k \mu_n^*$ (da $(k,n)=1$). Daher:
$$[Y_N, \mu_k] = \mu_{mk}(T_k(X_N) - X_N)\mu_n^*,$$
was in Norm gegen $\mu_{mk} B_k \mu_n^*$ konvergiert. $\square$

**Verbleibender Engpass.** Der nichtteilerfremde Sektor $(k, mn) \neq 1$ erfordert eine vollständige Reduktion von $\mu_n^* \mu_k$ mit den exakten BC-Relationen und Rangeprojektionen. Dort können Rand- oder Gradfehler entstehen. Dies ist derselbe nichtteilerfremde Engpass wie in NEU-199.

$$\boxed{[O\text{-}210\text{-}5] \quad \checkmark[M]_{\mathrm{part}}}$$

---

## 210.F — Offener Knoten: vollständiger Generatoraudit

**[O-210-6] ?[O] — Nichtteilerfremder Sektor und Nichtinnerheitstest.**

Zu leisten:
1. Vollständige Reduktion von $[Y_N, \mu_k]$ für $(k, mn) \neq 1$ mit den exakten BC-Relationen aus NEU-199/205.
2. Nachweis, dass die Grenzkommutatorformel $D_g(\mu_k) = \lim_N [Y_N, \mu_k]$ alle BC-Relationen respektiert (insbesondere die Isometrierelation und die Rangeprojektion).
3. **Nichtinnerheitstest:** Nachweis $[D_g] \neq 0 \in HH^1(A_{\mathrm{alg}}, A_{C^*})_g$.
4. **Zieltyptest:** Prüfung, ob $D_g(A_{\mathrm{alg}}) \subseteq A_{\mathrm{alg}}$ und ob ein typkorrekter Cup-Pfeil nach $HH^4_g$ existiert.

$$\boxed{[O\text{-}210\text{-}6] \quad ?[O]}$$

---

## 210.G — Synthesebefund

Die beiden zuvor konkurrierenden Anforderungen aus NEU-209 sind erstmals gleichzeitig erfüllt:

$$\boxed{\begin{aligned}
&\text{Singularität nur bei }\{0\} &&\Longrightarrow && e(r)\text{-Fehler werden absorbiert,}\\
&\text{beschränktes Faktorial-Transportband} &&\Longrightarrow && \mu_k\text{-Differenzen konvergieren.}
\end{aligned}}$$

Der Faktorialkandidat $Y_N = \mu_m X_N \mu_n^*$ ist der bislang stärkste direkte Kandidat für den geladenen Weg zu Objekt $X$. Er ist jedoch ein **konstruktiver Vorläufer** der Schicht $X.3$, nicht bereits ihre Realisierung: Zwischen diesem Kandidaten und $[L_3] \in HH^4$ liegen noch der vollständige Generatoraudit, der Nichtinnerheitstest und der Cup-Pfeil.

---

## 210.H — Strukturbilanz

| Knoten | Status | Inhalt |
|---|---|---|
| [O-210-1] | ✓[M] | $Z_g = \{0\}$ für alle $g = m/n \neq 1$; schließt [O-209-5] |
| [O-210-2] | ✓[K] | Faktorielle Kette $L_j=(j+1)!$, Potential $X_N$, $\operatorname{Sing}(X)=\{0\}$; schließt [O-209-6] |
| [O-210-3] | ✓[M] | Transportband $P_j \le E_{L_j/k} \le P_{j-k}$; normkonvergente $\mu_k,\mu_k^*$-Kommutatoren |
| [O-210-4] | ✓[M] | $M(0)=0 \Rightarrow MX_N$ stabilisiert exakt; $e(r)$-Absorb. für $Y_N=\mu_mX_N\mu_n^*$ |
| [O-210-5] | ✓[M]_part | Konvergenz von $[Y_N,\mu_k]$ im teilerfremden Sektor $(k,mn)=1$ |
| [O-210-6] | ?[O] | Nichtteilerfremder Sektor; Nichtinnerheitstest; Zieltyptest |

---

## 210.I — DAG-Stand

```
[O-209-5] → [O-210-1] ✓[M]    Z_g = {0} exakt berechnet
[O-209-6] → [O-210-2] ✓[K]    Faktorialkette, Sing(X) = {0}
             [O-210-3] ✓[M]    Transportband, μ_k-Konvergenz
             [O-210-4] ✓[M]    Charakterabsorption, e(r)-Konvergenz
             [O-210-5] ✓[M]_part  Y_N = μ_m X_N μ_n*: teilerfremd ✓
             [O-210-6] ?[O]    nichtteilerfremd + Nichtinnerheit + Zieltyp
                               (Haupt-Flaschenhals geladene Route → X)
```
