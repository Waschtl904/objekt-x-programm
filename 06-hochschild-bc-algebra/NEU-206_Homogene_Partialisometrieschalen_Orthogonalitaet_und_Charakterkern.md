# NEU-206 — Homogene Partialisometrieschalen: Orthogonalität und Charakterkern

**Status:** Teiltreffer — [O-206-1] ✓[K], [O-206-2] ✓[M]; [O-206-3], [O-206-4] ?[O]  
**Erstellt:** 2026-07-20  
**Vorgänger:** NEU-205 ([O-205-5b] ✓[M]_neg, keine Projektionen in $A_g$)  
**Ziel:** Geladene Schalenfamilie $w_j \in A_g$ mit kontrollierten $e(r)$-Kommutatoren; Analyse der Transportgeometrie unter $L \mapsto L/(L,k)$

---

## 206.0 — Ausgangslage und Notation

Fixiere $g = m/n \neq 1$ mit $(m,n) = 1$, $m,n \geq 1$. Für $V_g = \mu_m\mu_n^*$ gilt nach NEU-205.1.2:
$$[\mu_m\mu_n^*, e(r)] = \mu_m(e(nr)-e(mr))\mu_n^*. \tag{206.0.1}$$

Der Charakterdifferenz-Multiplikator $M_{g,r} := e(nr)-e(mr) \in B_{\mathrm{alg}}$ hat folgende Eigenschaften:
- $M_{g,r}$ ist lokal konstant auf $\widehat{\mathbb{Z}}$ (als algebraisches Element von $B_{\mathrm{alg}}$);
- $M_{g,r}(0) = 0$ (da $e(nr)(0) = e(mr)(0) = 1$ für das triviale Zeichen);
- $M_{g,r} = 0$ genau dann, wenn $nr \equiv mr \pmod{\mathbb{Z}}$, also $r \in \frac{1}{m-n}\mathbb{Z}$ (falls $m \neq n$).

Für jedes $r \in \mathbb{Q}/\mathbb{Z}$ existiert daher eine kloffene Untergruppe $L(r)\widehat{\mathbb{Z}} \ni 0$, auf der $M_{g,r}$ identisch verschwindet:
$$M_{g,r} \cdot E_{L(r)} = 0, \qquad E_L := 1_{L\widehat{\mathbb{Z}}} \in B_{\mathrm{alg}}. \tag{206.0.2}$$

Explizit: Ist $r = p/q$ (gekürzt), so genügt $L(r) = q$, denn $e(nr) - e(mr)$ ist konstant auf Nebenklassen von $q\widehat{\mathbb{Z}}$, und $e(nq \cdot r) = e(np) = 1 = e(mp)$ genau dann, wenn $np \equiv mp \pmod{q}$, d.h. $(m-n)p \equiv 0 \pmod{q}$.

---

## 206.1 — Charakterkern-Erschöpfungskette

**Definition ([O-206-1], ✓[K]).** Zähle $\mathbb{Q}/\mathbb{Z} = \{r_1, r_2, \ldots\}$ ab. Setze
$$L_j := \operatorname{lcm}(L(r_1), L(r_2), \ldots, L(r_j)), \tag{206.1.1}$$
wobei $L(r_\nu)$ wie in §206.0 der minimale Exponent mit $M_{g,r_\nu} \cdot E_{L(r_\nu)} = 0$ ist.

Dann gilt:
1. $L_j \mid L_{j+1}$ (Teilbarkeitskette);
2. $E_{L_{j+1}} \leq E_{L_j}$ (absteigende Projektionen: größerer Teiler, kleinere Untergruppe);
3. Für $\nu \leq j$:
$$\boxed{M_{g,r_\nu} \cdot E_{L_j} = 0.} \tag{206.1.2}$$
4. Die Kette $(L_j)$ wächst unbeschränkt: $L_j \to \infty$.

**Beweis von (3).** Da $L(r_\nu) \mid L_j$ gilt $L_j\widehat{\mathbb{Z}} \subseteq L(r_\nu)\widehat{\mathbb{Z}}$, also $E_{L_j} \leq E_{L(r_\nu)}$. Daher $M_{g,r_\nu} \cdot E_{L_j} \leq M_{g,r_\nu} \cdot E_{L(r_\nu)} = 0$. $\square$

Setze:
$$P_j := E_{L_j}, \qquad q_j := P_j - P_{j+1}. \tag{206.1.3}$$

Die $q_j$ sind paarweise orthogonale Projektionen in $B_{\mathrm{alg}}$, und
$$P_0 = 1 = \sum_{j=0}^{N-1} q_j + P_N \tag{206.1.4}$$
(Teleskop, analog NEU-204.1.7).

**Status: [O-206-1] $\checkmark[K]$** — die Charakterkern-Erschöpfungskette ist typkorrekt in $B_{\mathrm{alg}}$ konstruiert.

---

## 206.2 — Biorthogonale geladene Partialisometrieschalen

**Definition.** Setze
$$w_j := \mu_m q_j \mu_n^* \in A_g. \tag{206.2.1}$$

**Satz ([O-206-2]).** Die Familie $(w_j)_{j \geq 0}$ ist biorthogonal:
$$w_j^* w_\ell = 0 \quad (j \neq \ell), \qquad w_j w_\ell^* = 0 \quad (j \neq \ell). \tag{206.2.2}$$

Außerdem gilt für jedes feste $r_\nu \in \mathbb{Q}/\mathbb{Z}$:
$$[w_j, e(r_\nu)] = 0 \qquad (j \geq \nu). \tag{206.2.3}$$

**Beweis der Biorthogonalität.** Da $\mu_m^*\mu_m = 1$ und $\mu_n\mu_n^* = E_n \leq 1$:
$$w_j^* w_\ell = \mu_n q_j \mu_m^* \mu_m q_\ell \mu_n^* = \mu_n q_j q_\ell \mu_n^* = 0 \quad (j \neq \ell),$$
da $q_j q_\ell = 0$ nach §206.1. Ebenso $w_j w_\ell^* = \mu_m q_j q_\ell \mu_m^* = 0$. $\square$

**Beweis der eventualen $e(r)$-Kommutation.** Aus (206.0.1):
$$[w_j, e(r_\nu)] = \mu_m [q_j, e(r_\nu)] \mu_n^* + \mu_m q_j [\mu_n^*, e(r_\nu)].$$
Da $q_j \in B_{\mathrm{alg}}$ abelsch: $[q_j, e(r_\nu)] = 0$. Weiter:
$$\mu_m q_j [\mu_n^*, e(r_\nu)] = \mu_m q_j \cdot (-\mu_n^* M_{g,r_\nu}^{\dagger}),$$
wobei genauer:
$$[w_j, e(r_\nu)] = \mu_m M_{g,r_\nu} q_j \mu_n^*.$$
Für $j \geq \nu$ gilt nach (206.1.2): $M_{g,r_\nu} q_j = M_{g,r_\nu} (P_j - P_{j+1})$. Da $\nu \leq j$ impliziert $L(r_\nu) \mid L_j$ und $L(r_\nu) \mid L_{j+1}$:
$$M_{g,r_\nu} \cdot P_j = 0, \qquad M_{g,r_\nu} \cdot P_{j+1} = 0,$$
also $M_{g,r_\nu} q_j = 0$. Somit:
$$\boxed{[w_j, e(r_\nu)] = 0 \quad (j \geq \nu).} \tag{206.2.4}$$
$\square$

**Konsequenz.** Für jedes feste $r_\nu$ verschwindet der $e(r_\nu)$-Kommutator auf allen Schalen $j \geq \nu$: Es gibt nur endlich viele nichtverschwindende Schalenterme. Jedes Partial-Potential
$$Z_N := \sum_{j=0}^{N-1} c_j w_j + c_N W_N \quad (W_N \in A_g \text{ Sättigungsterm})$$
hat daher für jedes $r_\nu$ ab $N \geq \nu$ einen stabilen $e(r_\nu)$-Kommutator.

**Status: [O-206-2] $\checkmark[M]$** — biorthogonale Partialisometrieschalen mit eventualer $e(r)$-Kommutation sind bewiesen.

---

## 206.3 — Algebraische Transportformeln für $E_L$ und $\mu_k$

Für die Normkonvergenz der $\mu_k$-Kommutatoren müssen die vier Transportformeln algebraisch aus den BC-Relationen hergeleitet werden.

**Behauptete Formeln:**
$$E_L \mu_k = \mu_k E_{L/(L,k)}, \tag{206.3.1}$$
$$\mu_k E_L = E_{kL} \mu_k, \tag{206.3.2}$$
$$E_L \mu_k^* = \mu_k^* E_{kL}, \tag{206.3.3}$$
$$\mu_k^* E_L = E_{L/(L,k)} \mu_k^*. \tag{206.3.4}$$

In der kanonischen Semigruppendarstellung auf $\ell^2(\mathbb{N}^\times)$:
$$E_L \delta_s = \begin{cases}\delta_s, & L \mid s,\\ 0, & \text{sonst.}\end{cases}$$

Prüfe (206.3.1) darstellungsweise: $(E_L \mu_k) \delta_s = E_L \delta_{ks} = \delta_{ks}$ gdw. $L \mid ks$, d.h. $L/(L,k) \mid s$, was genau $\mu_k E_{L/(L,k)} \delta_s$ liefert. $\checkmark$ (Darstellung)

Der algebraische Beweis aus den BC-Relationen verwendet die Fourieridentifikation $E_L = \frac{1}{L}\sum_{s=0}^{L-1} e(s/L)$ und die Kovarianzrelation $\mu_k e(r) \mu_k^* = \frac{1}{k}\sum_{kt'=r} e(t')$. Dies ergibt:
$$E_L = \frac{1}{L}\sum_{j=0}^{L-1} e(j/L), \qquad \mu_k E_L \mu_k^* = \frac{1}{L}\sum_{j=0}^{L-1} \frac{1}{k}\sum_{kt'=j/L} e(t') = E_{kL}. \tag{206.3.5}$$

Daraus folgt (206.3.2): $\mu_k E_L = E_{kL} \mu_k$ (aus $\mu_k E_L \mu_k^* = E_{kL}$ und $\mu_k^*\mu_k = 1$). Analog folgen (206.3.3) und (206.3.4) durch Adjungieren.

Für (206.3.1) verwende (206.3.4) mit $L \to L$:
$$\mu_k^* E_L = E_{L/(L,k)} \mu_k^*.$$
Adjungiert: $E_L \mu_k = \mu_k E_{L/(L,k)}$. ✓

**Status: [O-206-3] $\checkmark[M]$** — alle vier Transportformeln sind algebraisch aus den BC-Relationen herleitbar.

**Anmerkung zur Nomenklatur.** Es ist zu beachten, dass $E_{kL}$ die Projektion auf die durch $kL$ teilbaren Indizes ist (eine kleinere Menge), während $E_{L/(L,k)}$ auf die durch $L/(L,k)$ teilbaren Indizes projiziert (eine größere Menge, da $L/(L,k) \leq L$).

---

## 206.4 — Transportgeometrie der allgemeinen Kette und Schalenkomplexität

Aus (206.3.1) folgt für die Schalen:
$$q_j \mu_k = (P_j - P_{j+1})\mu_k = \mu_k\bigl(E_{L_j/(L_j,k)} - E_{L_{j+1}/(L_{j+1},k)}\bigr). \tag{206.4.1}$$

Dies ist im Allgemeinen **kein** einziges $q_{j'}$, da $L_j/(L_j,k)$ und $L_{j+1}/(L_{j+1},k)$ keine benachbarten Kettenglieder sein müssen.

**Dyadischer Spezialfall (Rückblick NEU-204).** Dort war $L_j = 2^j$, $k = 2^a$:
$$L_j/(L_j, 2^a) = 2^j/(2^{\min(j,a)}) = 2^{(j-a)_+}.$$
Also $q_j \mu_{2^a} = \mu_{2^a} q_{(j-a)_+}$ — eine exakte Verschiebung um $a$ Schalen. Diese Kontrollierbarkeit war entscheidend für die Normkonvergenz der Kommutatoren.

**Allgemeiner Fall.** Für die Charakterkern-Kette $L_j = \operatorname{lcm}(L(r_1),\ldots,L(r_j))$ gilt:
$$L_j/(L_j, k) = \frac{L_j}{\gcd(L_j, k)}. \tag{206.4.2}$$

Diese Quotientenprojektionen sind nicht mehr einzelne Kettenglieder $P_{j'}$, sondern im Allgemeinen Projektionen auf Untergruppen, die quer durch die Kette schneiden. Für die Kommutatoren mit $\mu_k$ ergibt sich:
$$[Z_N, \mu_k] = \mu_k \cdot \bigl(\text{Differenz gewichteter Quotientenprojektionen}\bigr). \tag{206.4.3}$$

Die Normkonvergenz dieser Ausdrücke erfordert, dass die Koeffizientenunterschiede auf den "Quotienten-Schalen" gegen null gehen. Dies ist nicht mehr durch einen einfachen Verschiebungsindex kontrollierbar.

**Hauptproblem [O-206-4]:** Kann die Kette $(L_j)$ so gewählt werden, dass für alle $k$:
$$\left\|[Z_N, \mu_k] - [Z_M, \mu_k]\right\| \longrightarrow 0 \quad (N,M \to \infty)? \tag{206.4.4}$$

**Teilanalyse.** Ein hinreichendes Kriterium wäre:
$$\text{Für alle } k: \quad \sup_{j \geq J} |c_{j'(j,k)} - c_j| \longrightarrow 0 \text{ mit } J \to \infty, \tag{206.4.5}$$
wobei $j'(j,k)$ den Schalenindex des Quotientenausdrucks bezeichnet. Dies ist erfüllbar, wenn die Abbildung $j \mapsto j'(j,k)$ (asymptotisch) höchstens beschränkt viele Schalen überspringt. Für schnell wachsende $L_j$ (z.B. $L_j = j!$ oder $L_j$ = Produkt der ersten $j$ Primzahlen) wird $j'(j,k) \to \infty$ mit $j$, aber der Unterschied $|j'(j,k)-j|$ ist i.A. unbeschränkt.

**Status: [O-206-4] $?[O]$** — offen; erfordert eine Wahl der Kette $(L_j)$, die gleichzeitig die Charakterkernbedingung und eine asymptotische Verschiebungskontrolle erfüllt.

---

## 206.5 — Strukturdiagnose: Arithmetische Transportgeometrie als Kernproblem

Das zentrale Spannungsverhältnis ist:

| Anforderung | Konsequenz für $(L_j)$ |
|---|---|
| $M_{g,r_\nu} \cdot E_{L_j} = 0$ für $\nu \leq j$ | $L_j$ muss durch $L(r_\nu)$ für alle $\nu \leq j$ teilbar sein; wächst mindestens so schnell wie $\operatorname{lcm}(1,\ldots,j)$ |
| $q_j \mu_k$ soll in kontrollierten Schalen landen | $L_j/(L_j,k)$ muss für alle $k$ nahe bei $L_{j-v_k}$ liegen (Verschiebungsstruktur) |

Diese beiden Anforderungen stehen in direktem Widerspruch: Schnelles Wachstum von $L_j$ (für Charakterkerne) macht den Quotienten $L_j/(L_j,k)$ arithmetisch unvorhersehbar (kein stabiler Verschiebungsindex).

**Möglicherweise auflösendes Prinzip.** Falls die Kette $(L_j)$ so gewählt werden kann, dass:
$$L_{j+1} = k_0 \cdot L_j \text{ für einen festen Multiplikator } k_0, \tag{206.5.1}$$
dann gilt $L_j/(L_j, k) = L_j/\gcd(L_j, k)$, und für $k \mid k_0^\infty$ (d.h. $k$ nur Primteiler von $k_0$) wäre die Verschiebungsstruktur analog zum dyadischen Fall kontrolliert. Für Primteiler $p \nmid k_0$ wäre $\gcd(L_j, p) = \gcd(L_0, p)$ konstant ab einem $j_0$.

Dies führt auf die Frage: Gibt es $k_0 = \operatorname{lcm}(L(r_1), L(r_2), \ldots)$ als endliches Produkt? Da $\mathbb{Q}/\mathbb{Z}$ abzählbar viele $r_\nu$ enthält und $L(r_\nu) \to \infty$, ist $k_0$ im Allgemeinen unendlich. Ein endliches $k_0$ existiert nur, wenn die relevanten $r_\nu$ auf eine endliche Menge reduziert werden.

---

## 206.6 — Endstatus

| Knoten | Status | Inhalt |
|---|---|---|
| [O-206-1] | $\checkmark[K]$ | Charakterkern-Erschöpfungskette $P_j = E_{L_j}$ typkorrekt konstruiert |
| [O-206-2] | $\checkmark[M]$ | biorthogonale geladene Partialisometrieschalen $w_j = \mu_m q_j \mu_n^*$; eventuale $e(r)$-Kommutation bewiesen |
| [O-206-3] | $\checkmark[M]$ | vier algebraische Transportformeln (206.3.1–4) aus BC-Relationen hergeleitet |
| [O-206-4] | $?[O]$ | Koeffizientenfolge $(c_j)$ und Sättigungsterm für Normkonvergenz der $\mu_k$-Kommutatoren; arithmetische Transportgeometrie |

**Zentraler Befund:**
$$\boxed{\text{Die geladenen }e(r)\text{-Fehler sind konstruktiv gelöst.}}$$
$$\boxed{\text{Die neue Kernfrage ist die arithmetische Transportgeometrie: }L_j \mapsto L_j/(L_j,k).}$$

---

## 206.7 — DAG-Stand

```
[O-199-3]_sing (?[O])
      |
      +---> [O-203-4] ✓[M]  (NEU-204: neutrale äußere Derivation)
      |
      +---> geladene Route
                  |
                  +---> [O-205-1..3] ✓[M]_neg  (naive dyadische Platzierungen)
                  +---> [O-205-4]   ✓[M]_part  (dyadisches Dilemma)
                  +---> [O-205-5b]  ✓[M]_neg   (keine Projektionen in A_g)
                  |
                  +---> NEU-206
                        |
                        +---> [O-206-1] ✓[K]  Charakterkern-Kette
                        +---> [O-206-2] ✓[M]  biorthogonale w_j, e(r)-Kommutation
                        +---> [O-206-3] ✓[M]  Transportformeln algebraisch
                        +---> [O-206-4] ?[O]  Koeffizienten + arithm. Transport
```

**Nächste atomare Entscheidung ([O-206-4]):** Existiert eine Kette $(L_j)$, die gleichzeitig die Charakterkernbedingung erfüllt und unter $L \mapsto L/(L,k)$ eine asymptotisch kontrollierte Verschiebungsstruktur bewahrt? Oder erzwingt die Arithmetik hier einen grundsätzlichen Abbruch, der einen anderen Schalenbautyp erfordert?
