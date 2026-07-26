# NEU-218 — Grad-3-Partner und geladener Cup-Aufstieg

## Einordnung im DAG

Direkter Nachfolger von NEU-217 / [O-217-2c-6d] (Commit `604e6c6`).

**Voraussetzung (vollständig bewiesen):**
$$
[D_g] \in HH^1\!\left(A_{\mathrm{alg}},\, \mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g \setminus\{0\}.
$$

**Aktueller Stand:**
$$
L^{\mathrm{cup}}_{g;\mathbf{p}} := D_g\smile\Theta^\wedge_{p_1,p_2,p_3}
\in Z^4\!\left(A_{\mathrm{alg}},\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g.
$$

**Noch offen:**
$$
\boxed{[L^{\mathrm{cup}}_{g;\mathbf{p}}]\neq0 \quad ?[O]}
$$

---

## [O-218-1a] — Quellenbefund NEU-192/193

> **Status: ✓[M]$_{\mathrm{neg,Quelle}}$**

NEU-193 konstruiert $z_{-\lambda}^{g,\mathbf{p}}\in C_4(A_{\mathrm{alg}},A_{\mathrm{alg}}^\vee)_{-\lambda}$.
Kein expliziter neutraler Grad-3-Kozykel mit $N_3$ und bewiesener Randgleichung vorhanden. $\square$

---

## [O-218-1b] — Globale neutrale Primableitungen

> **Status: ✓[K/M]**

$$
\boxed{\delta_p^{(0)}(a_h) := v_p(h)\log(p)\cdot a_h.} \tag{D}
$$

Wohldefiniertheit, Leibnizregel, Gradneutralität, paarweise Kommutation: geprüft.
$\delta_p^{(0)}(a^*)=-\delta_p^{(0)}(a)^*$; erst $i\delta_p^{(0)}$ ist $*$-Derivation. $\square$

---

## [O-218-1c] — Grad-3-Kozykel

> **Status: ✓[K/M]** (Ableitungsalternierung); **✓[M]$_{\mathrm{neg}}$** (Eingabealternierung)

$$
\boxed{\Theta^\wedge_{p_1,p_2,p_3}(a_1,a_2,a_3)
:=\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\,
\delta_{p_{\sigma(1)}}^{(0)}(a_1)\,\delta_{p_{\sigma(2)}}^{(0)}(a_2)\,\delta_{p_{\sigma(3)}}^{(0)}(a_3).} \tag{1}
$$

$b\Theta^\wedge=0$; $\deg\Theta^\wedge=1_\Gamma$.
$\Theta^{\mathrm{in}}$ durch explizites Gegenbeispiel widerlegt. $\square$

---

## [O-218-1d] — Nichttrivialität $[\Theta^\wedge]\neq0$

> **Status: ✓[K/M]**

$$
\langle\Theta^\wedge_{p_1,p_2,p_3}, z^\varepsilon_{p_1,p_2,p_3}\rangle
=6\prod_{i=1}^3\log p_i\neq0. \qquad\square
$$

---

## [O-218-2] — Koeffizientenkopplung $\beta$

> **Status: ✓[K/M]**

$$
\boxed{\beta(m\otimes a)=ma,\qquad M_4=\mathfrak{M}_{\mathrm{glob}}^{\log}.} \tag{3}
$$

---

## [O-218-3] — Expliziter Grad-4-Cup-Kozykel

> **Status: ✓[K/M]**

$$
\boxed{L^{\mathrm{cup}}_{g;\mathbf{p}}(a_1,a_2,a_3,a_4)
:= D_g(a_1)\cdot\Theta^\wedge_{p_1,p_2,p_3}(a_2,a_3,a_4).} \tag{4}
$$

$bL^{\mathrm{cup}}_{g;\mathbf{p}}=0$; $\deg=g$. $\square$

---

## [O-218-4] — Nichtverschwindensbeweis

> **Status: ✓[M]$_{\mathrm{part}}$**

Typaudit: NEU-193-Paarung nicht typdefiniert.
Augmentationsnullresultat: $\varepsilon(D_g(a))=0$ schließt augmentationsbasierten Zeugen aus;
es folgt nicht $[L^{\mathrm{cup}}]=0$.

---

## [O-218-4-nichtaug] — Nichtaugmentativer Zeuge

> **Status: ✓[M]$_{\mathrm{part}}$ (bedingt durch [SO-Q])**

**Setzung:** $C := \operatorname{span}_{\mathbb{C}}\{am-ma\mid a\in A,\,m\in M\}$.

**Korrektur SO-1-Äquivalenz (✓[M]$_{\mathrm{neg}}$):**
$(W)\;C\mu_P\subseteq C$ sichert nur Wohldefiniertheit;
$(I)\;R_{\mu_P}^{-1}(C)=C$ ist unabhängige Injektivitätsbedingung.

**Resttermzerlegung:**
$$
\boxed{[a,m]\mu_P = [a,m\mu_P] + m[\mu_P,a].} \tag{2.1}
$$

**Direkter Quotientenknoten:**
$$
\boxed{[\mathrm{SO\text{-}Q}]:\quad \eta_{q,P}:=\overline{D_g(\mu_q)\mu_P}\neq0 \text{ in } M/C \quad ?[O].}
$$

**Implikationskette unter [SO-Q]:**
- $\varphi:=\lambda\circ\pi_C$, zentral: $a\cdot\varphi=\varphi\cdot a$ (3.2)
- $z_\varphi:=\sum_{\pi\in S_4}\operatorname{sgn}(\pi)\,\varphi\otimes\mu_{r_{\pi(1)}}\otimes\cdots\otimes\mu_{r_{\pi(4)}}$,
 $\;\partial z_\varphi=0$ (4.2)
- $\langle L^{\mathrm{cup}}_{g;\mathbf{p}},\,z_\varphi\rangle = 6\prod\log p_i\cdot\varphi(D_g(\mu_q)\mu_P)\neq0$ (5.1)

**Spurzustand-Ausschluss (✓[M]$_{\mathrm{neg}}$):** $\tau(D_g(\mu_q)\mu_P)=0$ via Tracialität und $\mu_q\mu_P=\mu_P\mu_q$.

**KMS-Pfad:** ?[O]$_{\mathrm{sekundär}}$ (getwistete Kettenarchitektur).

---

## [SO-Q-Audit] — Korrekturaudit: Nica-Formel und Grenzen des Baker-Schritts

> **Status:** Nica-Formel ✓[M]; Baker-Gewichtstrennung ✓[M]$_{\mathrm{neg}}$; [SO-Q] ?[O].

### 1. Exakte Nica-Relation

Setze $d:=(P,n)$, $P=dP'$, $n=dn'$, $(P',n')=1$.

Vorwärts:
$$
\mu_n^*\mu_P = \mu_{n'}^*\mu_{P'} \tag{2.1}
$$
Rückwärts:
$$
\mu_P\mu_n^* = \mu_{P'}E_d\mu_{n'}^* \tag{2.2}
$$
Subtraktion:
$$
\boxed{[\mu_P,\mu_n^*] = \mu_{P/d}(E_d-1)\mu_{n/d}^*.} \tag{2.3}
$$
Restterm im Kommutatorraum:
$$
\boxed{m[\mu_P,\mu_n^*] = m\mu_{P/d}(E_d-1)\mu_{n/d}^*.} \tag{2.4}
$$
Für $(P,n)=1$ gilt $d=1$, $E_1=1$:
$$
\boxed{[\mu_P,\mu_n^*]=0 \qquad \text{für }(P,n)=1.} \tag{2.5}
$$

$$
\boxed{[\mathrm{SO\text{-}1a\text{-Nica-Formel}}]\quad\checkmark[M].}
$$

### 2. Primträgeraussage des Nica-Faktors

Da $d\mid P=p_1p_2p_3$ folgt $v_q(d)=0$ für $q\notin\{p_1,p_2,p_3\}$:
$$
\boxed{\text{Der Nica-Faktor }\mu_{P/d}(E_d-1)\mu_{n/d}^*
\text{ trägt keinen }q\text{-Primindex.}} \tag{3.1}
$$

Dies ist eine Aussage über Monomindizes, **nicht** über skalare Koeffizienten von $m$.
Das vorgeschaltete $m\in M$ kann weiterhin $q$-abhängige Anteile besitzen.

$$
\boxed{\text{"Nica-Term trägt keinen }\log q\text{-Beitrag"}\quad\checkmark[M]_{\mathrm{neg}}.}
$$

### 3. Fehlerprotokoll: Baker-basierte Gewichtstrennung

> **Status: ✓[M]$_{\mathrm{neg}}$ — voriger Commit [9ad0355c] wird an diesem Punkt zurückgerollt.**

**Fehler 1: Fehlende kanonische Koeffizientenabbildung.**
Eine wohldefinierte lineare Abbildung
$$
\operatorname{coef}_{\log q}: M_{gqP}\longrightarrow V
$$
ist im komplexen Bimodul $M=\mathfrak{M}_{\mathrm{glob}}^{\log}$ nicht definiert.
Da $M$ ein komplexer Vektorraum ist, gilt für jedes $u\in M$:
$$
(\log q)\cdot u = (\log p_1)\cdot\frac{\log q}{\log p_1}\cdot u, \tag{4.1}
$$
wobei $\frac{\log q}{\log p_1}\in\mathbb{C}$. Damit gibt es ohne zusätzliche rationale
Modellstruktur keine eindeutige Zerlegung
$$
m = (\log q)m_q + \sum_i(\log p_i)m_i + m_0.
$$

**Fehler 2: Baker löst dieses Problem nicht.**
Die arithmetische Bedingung
$$
\log q\notin\operatorname{span}_{\mathbb{Q}}\{\log p_1,\log p_2,\log p_3\} \tag{AC}
$$
ist richtig und folgt elementar aus eindeutiger Primfaktorzerlegung
(aus $a\log q+\sum b_i\log p_i=0$, $a,b_i\in\mathbb{Q}$ folgt $q^A\prod p_i^{B_i}=1$, also $A=B_i=0$).
Bakers Theorem ist hierfür nicht erforderlich.

Über $\mathbb{C}$ gilt trivialerweise $\log q=\frac{\log q}{\log p_1}\cdot\log p_1$.
Da Koeffizienten in $C$ in $\mathbb{C}$ liegen, liefert $\mathbb{Q}$-lineare Unabhängigkeit
keine Trennung im komplexen Quotientenraum.

$$
\boxed{[\mathrm{SO\text{-}Q\text{-Baker}}]\quad\checkmark[M]_{\mathrm{neg}}.} \tag{4.2}
$$

**Fehler 3: Universelle Gewichtsformel für Kommutatoren nicht gültig.**
Die angesetzte Formel
$$
[a_h, m_s] \;â\u0086¦\; \sum_\ell(v_\ell(h)-v_\ell(s))\log\ell \tag{5.1}
$$
gilt für einen allgemeinen Kommutator nicht. $m_s\in M_s$ ist ein allgemeines
Element des komplexen Bimoduls; der Grad legt nur die Komponente fest, nicht
den skalaren Logarithmenfaktor. Für jedes $c\in\mathbb{C}$ ist $c[a_h,m_s]$
wieder ein Kommutator.

$$
\boxed{\text{Universelle Gewichtsaussage (5.1)}\quad\checkmark[M]_{\mathrm{neg}}.}
$$

**Fehler 4: Implikation $[D_g]\neq0\Rightarrow\alpha_{g,q}\neq0$ nicht gültig.**
Nichttrivialität in $HH^1$ bedeutet nur, dass $D_g$ nicht inner ist;
sie impliziert nicht $D_g(\mu_q)\neq0$ für jeden Generator. Ein positiver
$q$-spezifischer Befund benötigt mindestens eine der Bedingungen:
- Explizite Generatorformel $D_g(\mu_q)=\mu_{mq}G_q\mu_n^*$ mit $G_q\neq0$; oder
- $q$-spezifische Normdivergenz: aus $D_g(\mu_q)=0$ folgte per Leibniz
 $D_g(\mu_{q^r})=0$ für alle $r$, im Widerspruch zur Divergenz.

$$
\boxed{[D_g]\neq0\Rightarrow\alpha_{g,q}\neq0\quad\text{in angegebener Allgemeinheit}\quad\checkmark[M]_{\mathrm{neg}}.}
$$

### 4. Mathematisch belastbare Normalform des Zielelements

Unter den Voraussetzungen $g=m/n$, $(m,n)=1$, $q,p_i\nmid mn$, und
mit der expliziten Generatorformel $D_g(\mu_q)=\mu_{mq}G_q\mu_n^*$:
$$
\begin{aligned}
D_g(\mu_q)\mu_P
&= \mu_{mq}G_q\mu_n^*\cdot\mu_P\\
&= \mu_{mq}G_q\mu_P\mu_n^*\\
&= \mu_{mqP}\,\sigma_P(G_q)\,\mu_n^*.
\end{aligned}
\tag{7.1}
$$
(Zweite Zeile: $\mu_n^*\mu_P=\mu_{n'}^*\mu_{P'}=\mu_P\mu_n^*$ unter Teilerfremdheit;
dritte Zeile: $\mu_qG_q\mu_P=\mu_{qP}\sigma_P(G_q)$, Semigruppenwirkung.)

Die Zerlegung $\alpha_{g,q}\kappa_{q,P}m_{gqP}^{(\log)}+r_{g,q}\mu_P$
ist erst verwendbar, wenn $m_{gqP}^{(\log)}$, $r_{g,q}$, $\alpha_{g,q}$, $\kappa_{q,P}$
explizit definiert und ihre Eindeutigkeit bewiesen sind.

$$
\boxed{\text{Belastbare Normalform: }D_g(\mu_q)\mu_P
= \mu_{mqP}\,\sigma_P(G_q)\,\mu_n^*.} \tag{7.1}
$$

### 5. Korrekte Restformulierung des Quotientenproblems

Voller Quotientenknoten (unverandert offen):
$$
\boxed{[\mathrm{SO\text{-}Q}]:\quad D_g(\mu_q)\mu_P \notin [A,M] \quad ?[O].}
$$

In Normalform:
$$
\boxed{\mu_{mqP}\,\sigma_P(G_q)\,\mu_n^* \notin [A,M] \quad ?[O].} \tag{8.1}
$$

Für den alternierenden Zyklus genügt es, den kleineren Raum
$$
C_\partial := \sum_{r\in\{q,p_1,p_2,p_3\}}[\mu_r,M]
$$
zu betrachten. Das reduziert die Koinvariantenfrage auf:
$$
\boxed{[\mathrm{SO\text{-}Q}_\sigma]:\quad
\sigma_P(G_q) \notin \sum_{r\in\{q,p_1,p_2,p_3\}}(1-\sigma_r)B^{\log}
\quad ?[O].} \tag{8.2}
$$

Ein positiver Beweis benötigt ein Funktional $\Lambda: B^{\log}\to\mathbb{C}$ mit
$$
\Lambda((1-\sigma_r)F)=0\quad\forall r\in\{q,p_1,p_2,p_3\},
\qquad\text{aber}\qquad
\Lambda(\sigma_P(G_q))\neq0,
$$
oder eine Wachstumsschätzung via Følner-Summen:
$$
\prod_{r\in\{q,p_1,p_2,p_3\}}\left(\sum_{k=0}^{N-1}\sigma_r^k\right)\cdot(1-\sigma_r^N)
= \text{Teleskopidentität}.
$$

---

## Revidierte Statusverteilung

| Knoten | Inhalt | Status |
|---|---|---|
| [O-218-1a–1d] | Quellenbefund, $\delta_p^{(0)}$, $\Theta^\wedge$, Paarung | ✓[M/K/M] |
| [O-218-2–3] | Bimoduliso, Cup-Kozykel | ✓[K/M] |
| [O-218-4] | Typaudit, Augmentationsnull | ✓[M]$_{\mathrm{part}}$ |
| SO-1-Äquivalenz | $C\mu_P\subseteq C\Leftrightarrow$ Injektivität | ✓[M]$_{\mathrm{neg}}$ |
| SO-1a-Nica-Formel | $[\mu_P,\mu_n^*]=\mu_{P/d}(E_d-1)\mu_{n/d}^*$ | **✓[M]** |
| Primträger Nica | $v_q(d)=0$ für $q\notin\{p_i\}$ | **✓[M]** |
| Baker [AC] | $\log q\notin\mathbb{Q}\text{-span}\{\log p_i\}$ | ✓[M] (elementar) |
| [SO-Q-Baker] | Baker als Quotientendetektor | **✓[M]$_{\mathrm{neg}}$** |
| Univ. Gewichtsformel (5.1) | $[a_h,m_s]$ hat kanonischen $\log$-Koeff. | **✓[M]$_{\mathrm{neg}}$** |
| $[D_g]\neq0\Rightarrow\alpha_{g,q}\neq0$ | generatorspezifische Nichtnullheit | **✓[M]$_{\mathrm{neg}}$** |
| Spurzustand | $\tau(D_g(\mu_q)\mu_P)=0$ | ✓[M]$_{\mathrm{neg}}$ |
| KMS-Pfad | getwistete Hochschild-Kettenarchitektur | ?[O]$_{\mathrm{sekundär}}$ |
| **[SO-Q]** | $D_g(\mu_q)\mu_P\notin C$ | **?[O]** |
| **[SO-Q$_\sigma$]** | $\sigma_P(G_q)\notin\sum_r(1-\sigma_r)B^{\log}$ | **?[O] primär** |
| [O-218-4-nichtaug] | bedingte Ketten+Paarungsarchitektur gültig | ✓[M]$_{\mathrm{part}}$ |

---

## DAG-Pfad (aktualisiert)

```
[O-217-2c-6d]  [D_g] in HH^1_g \ {0}                         [M]
       |
  [O-218-1a..3]  Kozykelkonstruktion vollstaendig               [K/M]
       |
  [O-218-4]    Augmentationsnull; Typaudit                     [M]_part
       |
  [O-218-4-nichtaug]
       |
       +-- Spurzustand: tau=0 via Tracialitaet                  [M]_neg
       +-- KMS-Pfad: getwistete Architektur                    ?[O] sekundaer
       |
       +-- Quotientenpfad (primaer):
           |
           SO-1a-Nica-Formel: [mu_P, mu_n*] = mu_{P/d}(E_d-1)mu_{n/d}*  [M]
           Primtraeger: v_q(d)=0                                [M]
           Baker [AC]: log q Q-unabh. von log p_i (elementar)  [M]
           |
           FEHLER-Protokoll [M]_neg:
             - kein kanonischer log q-Koeffizient auf kompl. M
             - Baker liefert keine C-Trennung
             - Universalformel (5.1) fuer Modulkommutatoren ungueltig
             - [D_g]!=0 => alpha_{g,q}!=0 ohne Generator-Spezifikation
           |
           Belastbare Normalform (7.1):
             D_g(mu_q)*mu_P = mu_{mqP} * sigma_P(G_q) * mu_n*
           |
           [SO-Q]: D_g(mu_q)*mu_P not in C                     ?[O]
           |
           [SO-Q_sigma]: sigma_P(G_q) not in                   ?[O] PRIMAER
                sum_{r in {q,p1,p2,p3}} (1-sigma_r) B^log
           |
           Strategie: Lambda: B^log -> C mit
             Lambda((1-sigma_r)F)=0 fuer alle r, aber
             Lambda(sigma_P(G_q)) != 0
           Oder: Foelner-Wachstumsschaetzung sigma_P(G_q)
           |
           v
       [SO-Q] erledigt => phi_com, z_phi, Paarung (5.1)        [M]_part
           |
           v
  [L^cup] != 0 in HH^4(A_alg, M)_g                            (?[O] -> [M])
           |
           v
        Objekt X.3
```
