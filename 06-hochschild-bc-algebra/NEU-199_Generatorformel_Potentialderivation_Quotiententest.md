# NEU-199 — Generatorformel der Potentialderivation und konkreter Kommutatorquotiententest

## 199.0 Ziel und DAG-Position

Dieser Knoten konkretisiert die in NEU-188 eingeführte Potentialroute so weit, dass der kohomologische Obstruktionspfeil aus NEU-198 tatsächlich ausgewertet werden kann.

Vorgelagerte Kette:
$$\text{NEU-188} \longrightarrow \text{NEU-196} \longrightarrow \text{NEU-197} \longrightarrow \text{NEU-198} \longrightarrow \text{NEU-199}.$$

Bereits abgeschlossen:

| Knoten | Status | Inhalt |
|---|---|---|
| [O-195-A2] | $\checkmark[M]_{\mathrm{neg}}$ | Augmentationsblindheit der punktierten Potentialroute |
| [O-197-2] | $\checkmark[M]$ | Klassifikation der Dualzyklen durch partiellen Kommutatorquotienten |
| [O-197-3] | $\checkmark[M]$ | Universelles Detektionskriterium |
| [O-198-1/2/3] | $\checkmark[M]$ | Kohomologische Faktorisierung des Obstruktionspfeils |

Offen:
$$[O\text{-}198\text{-}4]: \qquad \overline\Theta_{g,\mathbf p,i}\bigl([D_g^H]\bigr) \neq 0\;?$$

---

## 199.A Verbindliche Nichtziele

Dieser Knoten:
- postuliert keine neue geladene Derivation;
- ersetzt keinen fehlenden Relationennachweis durch eine formale Normalform;
- eröffnet noch keinen alternativen $HH^1$-Zweig;
- eröffnet noch keine neue Dualzyklenarchitektur;
- behauptet nicht, dass jede punktierte Potentialklasse auf die volle BC-Algebra erweitert werden kann.

Zuerst ist ausschließlich die vorhandene NEU-188-Potentialroute auf Generatorniveau zu auditieren.

---

## 199.B Ausgangsdaten aus NEU-188

Fixiere $A = B_3^{\mathrm{mod}} \cong \bigoplus_{q\in\mathbb Q_+^\times} A_q$, schreibe das geladene Gewicht in gekürzter Form als
$$g = \frac{m}{n}, \qquad (m,n)=1.$$

Sei $H: \widehat{\mathbb Z}\setminus\{0\} \to \mathbb C$ ein lokal konstantes punktiertes Potential. Der zugehörige formale homogene Multiplikator ist
$$u_H := \mu_m H \mu_n^*.$$

Für $k\in\mathbb N^\times$ sei $\Delta_k H := \alpha_k(H) - H$ mit $(\alpha_k H)(x) = H(kx)$. Falls $\Delta_k H$ eine lokal konstante Fortsetzung auf $\widehat{\mathbb Z}$ besitzt, bezeichne diese mit $F_k \in B \cong \operatorname{LC}(\widehat{\mathbb Z})$. Nach NEU-196 gilt $F_k(0) = 0$.

Der singuläre Kommutatoransatz:
$$D_g^H(a) := [u_H, a] = u_H a - a u_H,$$
sofern der jeweilige Kommutator ein reguläres Element von $A$ ist.

---

## 199.C Atomare Generatorfrage

Gesucht ist eine explizite Formel $D_g^H(\mu_k) \in A_{gk}$. Als allgemeine endliche Normalform:
$$\boxed{D_g^H(\mu_k) = \sum_{\nu=1}^{N_k} \mu_{m_{\nu,k}}\, F_{\nu,k}\, \mu_{n_{\nu,k}}^*} \tag{199.1}$$
mit $F_{\nu,k} \in B$ und $m_{\nu,k}/n_{\nu,k} = gk$.

---

## 199.D Konkrete Herleitung im teilerfremden Sektor

### 199.D.0 Formel auf dem Gruppenalgebrasektor

Aus den Kreuzrelationen $\mu_n^* e(r) = e(nr)\mu_n^*$ und $e(r)\mu_m = \mu_m e(mr)$ folgt:
$$\boxed{D_g^H(e(r)) = \mu_m\, c_r^H\, \mu_n^*, \qquad c_r^H := H\bigl(e(nr)-e(mr)\bigr).} \tag{199.10}$$

### 199.D.1 Generatorformel für teilerfremde $\mu_k$

Sei $(k,n)=1$. Dann $\mu_n^*\mu_k = \mu_k\mu_n^*$. Aus $f\mu_k = \mu_k\alpha_k(f)$:
$$u_H\mu_k = \mu_m H\mu_n^*\mu_k = \mu_m H\mu_k\mu_n^* = \mu_{mk}\alpha_k(H)\mu_n^*,$$
$$\mu_k u_H = \mu_{mk}H\mu_n^*.$$

Daher:
$$\boxed{D_g^H(\mu_k) = \mu_{mk}F_k\mu_n^*, \qquad F_k := \alpha_k(H)-H,} \tag{199.11}$$
für alle $k$ mit $(k,n)=1$, sofern $F_k\in B$. Gradcheck: $\deg(\mu_{mk}F_k\mu_n^*) = mk/n = gk$. $\checkmark$

### 199.D.2 Formel für $\mu_k^*$ bei $(k,mn)=1$

Sei $(k,mn)=1$. Dann darf $\mu_k^*\mu_m = \mu_m\mu_k^*$ verwendet werden:
$$u_H\mu_k^* = \mu_m H\mu_{nk}^*, \qquad \mu_k^* u_H = \mu_m\alpha_k(H)\mu_{nk}^*.$$

$$\boxed{D_g^H(\mu_k^*) = -\mu_m F_k\mu_{nk}^*.} \tag{199.12}$$

Gradcheck: $\deg(\mu_m F_k\mu_{nk}^*) = m/(nk) = g/k$. $\checkmark$

### 199.D.3 Semigruppenrelation im teilerfremden Untermonoid

Für $(k\ell,mn)=1$:
$$F_{k\ell} = \alpha_{k\ell}(H)-H = \alpha_\ell(F_k)+F_\ell. \tag{199.13}$$

Rechnung:
$$D_g^H(\mu_k)\mu_\ell + \mu_k D_g^H(\mu_\ell) = \mu_{mk\ell}\alpha_\ell(F_k)\mu_n^* + \mu_{mk\ell}F_\ell\mu_n^* = \mu_{mk\ell}F_{k\ell}\mu_n^* = D_g^H(\mu_{k\ell}).$$

$$\boxed{D_g^H(\mu_{k\ell}) = D_g^H(\mu_k)\mu_\ell + \mu_k D_g^H(\mu_\ell)} \tag{199.14}$$
im vollständigen teilerfremden Untermonoid $S_{m,n} := \{k\in\mathbb N^\times:(k,mn)=1\}$. $\checkmark$

### 199.D.4 Isometrierelation

Mit (199.11) und (199.12) bei $(k,mn)=1$:
$$D_g^H(\mu_k^*)\mu_k = -\mu_m F_k\mu_{nk}^*\mu_k = -\mu_m F_k\mu_n^*,$$
$$\mu_k^* D_g^H(\mu_k) = \mu_k^*\mu_{mk}F_k\mu_n^* = \mu_m F_k\mu_n^*.$$

$$\boxed{D_g^H(\mu_k^*)\mu_k + \mu_k^* D_g^H(\mu_k) = 0.} \tag{199.15}$$

Die Relation $\mu_k^*\mu_k = 1$ wird korrekt differenziert. $\checkmark$

### 199.D.5 Kreuzrelationen

Aus $[u_H, ab] = [u_H,a]b + a[u_H,b]$ folgt für $e(r)\mu_k = \mu_k e(kr)$ automatisch:
$$D_g^H(e(r))\mu_k + e(r)D_g^H(\mu_k) = D_g^H(\mu_k)e(kr) + \mu_k D_g^H(e(kr)). \tag{199.16}$$

Dies ist ein Identitätsnachweis in $A$, sofern sämtliche punktierte Koeffizienten regulär fortsetzbar sind.

---

## 199.E Statusentscheidung

| Knoten | Status | Inhalt |
|---|---|---|
| [O-199-1] | $\checkmark[M]_{\mathrm{part}}$ | $D_g^H(\mu_k) = \mu_{mk}F_k\mu_n^*$ für $(k,n)=1$ |
| [O-199-2] | $\checkmark[M]_{\mathrm{part}}$ | Relationenaudit vollständig auf $S_{m,n}$ |
| [O-199-1]$_{\mathrm{noncopr}}$ | $?[O]$ | Transferformel für $(k,mn)>1$ |

**Konkrete Partialtreffer:**
$$\boxed{D_g^H(\mu_k) = \mu_{mk}(\alpha_k(H)-H)\mu_n^* \qquad \text{für }(k,n)=1.}$$
$$\boxed{D_g^H(\mu_k^*) = -\mu_m(\alpha_k(H)-H)\mu_{nk}^* \qquad \text{für }(k,mn)=1.}$$

**Exakt benannte Restlücke:**
$$\boxed{\text{Generatorformeln für }k\text{ mit }(k,mn)>1,\text{ einschließlich Transfer- und Projektionskorrekturen.}}$$

---

## 199.F Konkreter Obstruktionspfeil (teilerfremder Sektor)

Wähle vier paarweise verschiedene Primzahlen $p_1,p_2,p_3,p_4$ mit $p_j\nmid mn$ für $j=1,\ldots,4$. Setze $P = p_1p_2p_3p_4$, $R_i = \prod_{j\neq i}\mu_{p_j}$.

Dann:
$$D_g^H(\mu_{p_i}) = \mu_{mp_i}F_{p_i}\mu_n^*.$$

Da alle $p_j$ teilerfremd zu $n$, gilt $\mu_n^*R_i = R_i\mu_n^*$. Mit $F_{p_i}R_i = R_i\alpha_{P/p_i}(F_{p_i})$:

$$\boxed{Y_{g,H,\mathbf p,i} = \mu_{mP}\, G_i^H\, \mu_n^*,} \tag{199.17}$$

wobei
$$\boxed{G_i^H := \alpha_{P/p_i}(F_{p_i}) = \alpha_P(H) - \alpha_{P/p_i}(H).} \tag{199.18}$$

---

## 199.G Reduktion auf einen $B$-Quotienten

Für $f\in B$ und $a_{j,f} := \mu_{mP/p_j}f\mu_n^* \in A_{gP/p_j}$:
$$[\mu_{p_j}, a_{j,f}] = \mu_{mP}f\mu_n^* - \mu_{mP}\alpha_{p_j}(f)\mu_n^* = \mu_{mP}(f - \alpha_{p_j}(f))\mu_n^*. \tag{199.19}$$

Im isolierten Normalformblock $(mP, n)$ reduziert sich die Quotientenfrage daher auf:

$$\boxed{G_i^H \in \sum_{j=1}^4 (1-\alpha_{p_j})B \quad\text{oder nicht?}} \tag{199.20}$$

Konkret:
$$\boxed{\alpha_P(H) - \alpha_{P/p_i}(H) \stackrel{?}{\in} \sum_{j=1}^4 (1-\alpha_{p_j})\operatorname{LC}(\widehat{\mathbb Z}).} \tag{199.21}$$

Dies ist der erste tatsächlich auswertbare Koeffiziententest für den Obstruktionspfeil.

---

## 199.H Quotientenentscheidung

Für jeden festen Testdatensatz $(g, H, \mathbf p, i)$ ist zu entscheiden:

$$\boxed{Y_{g,H,\mathbf p,i} \in \mathcal C_{gP,\mathbf p}} \quad \text{oder} \quad \boxed{Y_{g,H,\mathbf p,i} \notin \mathcal C_{gP,\mathbf p}.}$$

Nach (199.19)–(199.20) ist dies äquivalent zu:
$$G_i^H \in \sum_{j=1}^4(1-\alpha_{p_j})B \quad\text{oder nicht.}$$

**Positiver Detektionsbefund:** Falls $Y_{g,H,\mathbf p,i} \notin \mathcal C_{gP,\mathbf p}$, folgen nach NEU-198 gleichzeitig:
$$[D_g^H] \neq 0 \in HH^1(A,A)_g, \qquad [\Omega_{D_g^H,\mathbf p}] \neq 0 \in HH^4(A,A)_g,$$
und die Existenz eines expliziten Dualfunktionals $\varphi_{gP} \in Q_{gP,\mathbf p}^\vee$. Status: $[O\text{-}199\text{-}3(g,H,\mathbf p,i)]\;\checkmark[M]$.

**Negativer Detektionsbefund:** $[O\text{-}199\text{-}3(g,H,\mathbf p,i)]\;\checkmark[M]_{\mathrm{neg}}$ nur für diesen Kanal. Daraus folgt nicht $[D_g^H]=0$.

---

## 199.I Testmatrix

| $g=m/n$ | Potential $H$ | Primtupel $\mathbf p$ | Slot $i$ | $G_i^H = \alpha_P(H)-\alpha_{P/p_i}(H)$ | $G_i^H \in \sum_j(1-\alpha_{p_j})B$? | Status |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | $?[O]$ |

---

## 199.J Globale Entscheidungsschwellen

**Fall J.1 — Mindestens ein positiver Test ($G_i^H \notin \sum_j(1-\alpha_{p_j})B$):**
$$[O\text{-}193\text{-}4] \quad \checkmark[M], \qquad [L_{3,\lambda}]\neq0.$$
(Identifikation mit historisch intendiertem $L_3$ bleibt separat.)

**Fall J.2 — Einzelne negative Tests:** Nur lokale $\checkmark[M]_{\mathrm{neg}}$; kein neuer Zweig.

**Fall J.3 — Vollständiges Verschwinden in $\mathscr H_g$:**
$$\boxed{[O\text{-}199\text{-}4] \quad ?[O]: \quad \begin{cases} \text{neue geladene }HH^1\text{-Quelle außerhalb der Potentialroute,}\\ \text{oder neue Dualzyklenarchitektur außerhalb des NEU-197-Typs.} \end{cases}}$$

---

## 199.K Arbeitsreihenfolge

$$\boxed{\begin{aligned} 1.&\quad \text{Konkrete }H\text{ und Primtupel }\mathbf p\text{ mit }p_j\nmid mn\text{ wählen;}\\ 2.&\quad G_i^H = \alpha_P(H)-\alpha_{P/p_i}(H)\text{ berechnen;}\\ 3.&\quad G_i^H \in \sum_{j=1}^4(1-\alpha_{p_j})\operatorname{LC}(\widehat{\mathbb Z})\text{ entscheiden (199.21);}\\ 4.&\quad\text{Testmatrix 199.I befüllen;}\\ 5.&\quad\text{parallel: Transfer-/Projektionsformel für }(k,mn)>1\text{ nachziehen.} \end{aligned}}$$

---

## 199.L Aktueller DAG-Status

| Knoten | Status | Inhalt |
|---|---|---|
| [O-199-1] | $\checkmark[M]_{\mathrm{part}}$ | $D_g^H(\mu_k)=\mu_{mk}F_k\mu_n^*$ für $(k,n)=1$ |
| [O-199-2] | $\checkmark[M]_{\mathrm{part}}$ | Relationenaudit vollständig auf $S_{m,n}$ |
| [O-199-3]$_{\mathrm{copr}}$ | $?[O]$ | $B$-Quotiententest (199.21): $G_i^H\in\sum_j(1-\alpha_{p_j})B$? |
| [O-199-1]$_{\mathrm{noncopr}}$ | $?[O]$ | Transfer-/Projektionsformel für $(k,mn)>1$ |
| [O-199-4] | $?[O]$ | gesperrt bis Fall J.3 |

$$\boxed{\checkmark[M]_{\mathrm{part}}}$$

**Atomare Restfrage:**
$$\boxed{\alpha_P(H)-\alpha_{P/p_i}(H) \stackrel{?}{\in} \sum_{j=1}^4(1-\alpha_{p_j})\operatorname{LC}(\widehat{\mathbb Z}).}$$
