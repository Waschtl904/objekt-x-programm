# NEU-217 — [O-217-2b] Komponentenweise gcd-Fallzerlegung von $D_g$ und [O-217-2c] Lokaler Defekt-Bimodul

## Einordnung im DAG

Dieser Knoten ist der direkte Nachfolger des Commit `af67f77`, der die lokale neutrale
$p$-Mechanik vollständig abschließt. Er importiert:

- NEU-211: Generatorformeln $D_g(\mu_{p^r})$ und $D_g(\mu_{p^r}^*)$ mit $G_{k,d}$-Defekttermen.
- [O-170d]: DAG-bereinigter Status von $\delta_p^{(0)}$ auf $A_{(p)}$.
- [O-193-1c]: Gewichtskomplementarität, analog für geladene Derivationen.

Drei architektonische Fakten sind ab `af67f77` als gesichert eingetragen:

1. $\delta_p^{(0)}$ lebt abstrakt auf $A_{(p)}$, gradneutral, ohne treue Hilbertraumdarstellung.
2. $H_p = (\log p)N$ ist ein konkreter Implementierer im Orbitmodell, nicht abstrakt.
3. $D_g$ ist eine geladene Derivation; ihre Gradverschiebung entsteht nicht aus $\delta_p^{(0)}$ allein.

**Dieser Knoten behandelt nicht** die Operatorrealisierung (NEU-189/190), die
Hochschild-Kohomologie (NEU-193) oder die globale Faktorisierung $D_g = V_g \delta_p^{(0)}$.

**Präziser Gesamtstatus von NEU-217.** Der zentrale lokale Zweig [O-217-2c-1]–[O-217-2c-5b]
ist abgeschlossen ✓[M]. Der Knoten NEU-217 insgesamt erhält **nicht** pauschal ✓[M],
solange [O-217-1d], [O-217-2b-5/6] und [O-217-2c-6] noch offen oder partiell sind.

---

## [O-217-2b] — Vollständige gcd-Fallzerlegung

### Setup und Notation

Sei $g = m/n$ in gekürzter Darstellung, $(m,n)=1$. Die NEU-211-Formeln:
$$
D_g(\mu_{p^r}) = \mu_{m k_r}\, G_{k_r, d_r}\, \mu_{n_r}^*, \tag{1}
$$
$$
D_g(\mu_{p^r}^*) = -\mu_{m_r}\, G_{\ell_r, e_r}\, \mu_{n \ell_r}^*, \tag{2}
$$
mit $d_r = (n,p^r)$, $e_r = (m,p^r)$ und den zugehörigen Faktorisierungen.

### [O-217-2b-1] — Strukturfakten zu $(m,n)=1$ ✓[K]

Fälle A ($p\nmid mn$), B ($p^\alpha\|m$, $p\nmid n$), C ($p^\beta\|n$, $p\nmid m$). $\square$

### [O-217-2b-2] — Fall A ✓[M]

$D_g(\mu_{p^r}) = \mu_{mp^r}G_{p^r,1}\mu_n^*$, $D_g(\mu_{p^r}^*) = -\mu_m G_{p^r,1}\mu_{np^r}^*$. $\square$

### [O-217-2b-3] — Fall B ✓[M]

Regimewechsel bei $r=\alpha$; für $r\geq\alpha$:
$D_g(\mu_{p^r}^*) = -\mu_{m'}G_{p^{r-\alpha},p^\alpha}\mu_{np^{r-\alpha}}^*$. $\square$

### [O-217-2b-4] — Fall C ✓[M]

Regimewechsel bei $r=\beta$; für $r\geq\beta$:
$D_g(\mu_{p^r}) = \mu_{mp^{r-\beta}}G_{p^{r-\beta},p^\beta}\mu_{n'}^*$. $\square$

### [O-217-2b-5] — Komponentenweise Struktur ✓[M]$_{\mathrm{part}}$

$D_g|_{A_{(p),\mathrm{alg}}} = \sum_{\tau\in\mathcal{T}_{g,p}} V_{g,p}^{(\tau)}\circ\Delta_{g,p}^{(\tau)}$, $|\mathcal{T}_{g,p}|\leq 2$.
Explizite Operatoridentifikation steht aus. $\square$

### [O-217-2b-6] — Verhältnis zu $\delta_p^{(0)}$ ✓[M]$_{\mathrm{part}}$

Kein globaler Faktor $V_g$; Typvorlage steht, Konstruktion offen. $\square$

---

## [O-217-2c] — Lokaler Defekt-Bimodul $M_{(p)}^{\log}$

**Vorbemerkung.** Erforderlich ist ein stabiler Koeffizientenmodul
$A_{(p),\mathrm{alg}}\cdot M_{(p)}^{\log}\cdot A_{(p),\mathrm{alg}} \subseteq M_{(p)}^{\log}$,
nicht eine Algebrastruktur.

### [O-217-2c-1] — Lineare Defektspanne ✓[K]

$$S_{(p)}^{\log} := \overline{\operatorname{span}\{G_{p^a,p^b}:a,b\geq 0\}}^{\|\cdot\|_{B^{\log}}}. \quad\square$$

### [O-217-2c-2] — $\sigma_p$-Transportidentitäten ✓[M]

$$\sigma_p(G_{p^a,p^b}) = G_{p^{a+1},p^{b-1}}\;(b\geq 1), \tag{T1}$$
$$\sigma_p(G_{p^a,1}) = G_{p^{a+1},1} - G_{p,1}. \tag{T2}$$
Korollar: $\sigma_p(S_{(p)}^{\log})\subseteq S_{(p)}^{\log}$. $\square$

### [O-217-2c-3] — $\rho_p$-Transportidentitäten ✓[M]

$$\rho_p(G_{1,p^b}) = G_{1,p^{b+1}} - G_{1,p}, \tag{T3}$$
$$\rho_p(G_{p^a,p^b}) = G_{p^{a-1},p^{b+1}} - (1-E_p)G_{p^{a-1},p}\;(a\geq 1). \tag{T4}$$
Strukturstelle: $\rho_p$ erzeugt Multiplikation mit $1-E_p\in B_{\mathrm{alg}}$. $\square$

### [O-217-2c-4] — Bimodulstabilität von $M_{(p)}^{\log}$ ✓[M]

$$M_{(p)}^{\log} := \overline{\operatorname{span}\{b_0 G_{p^a,p^b} b_1 : a,b\geq 0,\; b_i\in B_{(p),\mathrm{alg}}\}}^{\|\cdot\|}, \tag{6}$$
$B_{(p),\mathrm{alg}} = \operatorname{alg}\{E_{p^r}:r\geq 0\}$.
$\sigma_p$- und $\rho_p$-Stabilität aus (T1)–(T4) und $\sigma_p(E_{p^r})=E_{p^{r-1}}$,
$\rho_p(E_{p^r})=E_{p^{r+1}}$; $(1-E_p)G\in M_{(p)}^{\log}$ per Def. $\square$

### [O-217-2c-5] — $D_g(A_{(p),\mathrm{alg}})\subseteq M_{g,p}^{\log}$ ✓[M]

$$M_{g,p}^{\log} := \operatorname{span}_{\mathrm{fin}}\{\mu_u\,\xi\,\mu_v^* : \xi\in M_{(p)}^{\log},\,(u,v)\text{ aus Regimetabelle}\}.$$

| Fall | Gen. | $(u,v)$ | $\xi$ |
|---|---|---|---|
| A | $\mu_{p^r}$ | $(mp^r,n)$ | $G_{p^r,1}$ |
| A | $\mu_{p^r}^*$ | $(m,np^r)$ | $G_{p^r,1}$ |
| B, $r<\alpha$ | $\mu_{p^r}^*$ | $(m/p^r,n)$ | $G_{1,p^r}$ |
| B, $r\geq\alpha$ | $\mu_{p^r}^*$ | $(m',np^{r-\alpha})$ | $G_{p^{r-\alpha},p^\alpha}$ |
| C, $r<\beta$ | $\mu_{p^r}$ | $(m,n/p^r)$ | $G_{1,p^r}$ |
| C, $r\geq\beta$ | $\mu_{p^r}$ | $(mp^{r-\beta},n')$ | $G_{p^{r-\beta},p^\beta}$ |

$$\boxed{D_g(A_{(p),\mathrm{alg}}) \subseteq M_{g,p}^{\log},} \tag{7}$$
$$D_g|_{A_{(p),\mathrm{alg}}} \in Z^1\!\left(A_{(p),\mathrm{alg}},\, M_{g,p}^{\log}\right). \quad\square$$

---

### [O-217-2c-5b] — Lokale Nichtinnerheit

> **Status: ✓[M]**
>
> *Korrekturnotiz (Commit nach b82ccb8):* Das ursprüngliche Gradpaarargument
> (Schritt 2/3 in b82ccb8) trägt die Nichtinnerheit nicht: Ein fester Kommutator
> $[W,\mu_{p^r}]$ erzeugt bereits durch $d_r=(v,p^r)$ selbst $r$-abhängige äußere
> Monome und kann daher einen Regimewechsel reproduzieren. Der Beweis wird vollständig
> durch das folgende Normdivergenzbeweis ersetzt.

**Ziel.**
$$
\boxed{[D_g|_{A_{(p),\mathrm{alg}}}] \neq 0 \quad\text{in}\quad HH^1(A_{(p),\mathrm{alg}},\, M_{g,p}^{\log}).}
$$

#### Schritt 1 — $p$-adischer Testpunkt und Faktorialtiefe

Definiere $y^{(p)} = (y_q)_q \in \widehat{\mathbb{Z}}$ durch $y_p = 1$, $y_q = 0$ ($q\neq p$).
Für die Faktorialtiefe gilt
$$
\nu(y^{(p)}) = p-2. \tag{N1}
$$
Setze
$$
\lambda_p(s) := \max\{j\geq 0 : v_p((j+1)!) \leq s\}. \tag{N2}
$$
Dann
$$
\nu(p^s y^{(p)}) = \lambda_p(s), \qquad \lambda_p(s) \longrightarrow \infty\quad(s\to\infty). \tag{N3}
$$

#### Schritt 2 — Normunbeschränktheit der Defektterme

Setze $x_b = p^b y^{(p)}$. Aus der punktweisen Formel für die Transportdefekte:
$$
G_{p^a,p^b}(x_b) = \log(\lambda_p(a+b)+2) - \log p. \tag{N4}
$$
Daher
$$
\boxed{\|G_{p^a,p^b}\|_\infty \geq \log\!\left(\frac{\lambda_p(a+b)+2}{p}\right),} \tag{N5}
$$
und insbesondere
$$
a+b \longrightarrow \infty \quad\Longrightarrow\quad \|G_{p^a,p^b}\|_\infty \longrightarrow \infty. \tag{N6}
$$

#### Schritt 3 — $a_r + b_r = r$ in allen Fällen

Die Fallzerlegung aus [O-217-2b] liefert:

| Fall | $a_r$ | $b_r$ | $a_r+b_r$ |
|---|---|---|---|
| A: $p\nmid mn$ | $r$ | $0$ | $r$ |
| B: $p^\alpha\|m$, $r\geq\alpha$ | $r-\alpha$ | $\alpha$ | $r$ |
| C: $p^\beta\|n$, $r\geq\beta$ | $r-\beta$ | $\beta$ | $r$ |

In allen drei Fällen gilt für alle hinreichend großen $r$:
$$
a_r + b_r = r \longrightarrow \infty. \tag{N7}
$$

#### Schritt 4 — Äußere Isometrien erhalten die Norm

Für jedes neutrale $\xi$ und Isometrien $\mu_u, \mu_v$:
$$
\mu_u^*(\mu_u\xi\mu_v^*)\mu_v = \xi,
$$
also
$$
\boxed{\|\mu_u\xi\mu_v^*\| = \|\xi\|.} \tag{N8}
$$
Damit:
$$
\boxed{\|D_g(\mu_{p^r})\| = \|G_{p^{a_r},p^{b_r}}\| \longrightarrow \infty.} \tag{N9}
$$

#### Schritt 5 — Widerspruch zu einem Implementierer

Angenommen, $W_{g,p} \in M_{g,p}^{\log} \subseteq A_{C^*}$ erfülle
$D_g(x) = W_{g,p}x - xW_{g,p}$ für alle $x\in A_{(p),\mathrm{alg}}$.
Da $\|\mu_{p^r}\| = 1$, müsste gelten:
$$
\|D_g(\mu_{p^r})\| = \|[W_{g,p},\mu_{p^r}]\| \leq 2\|W_{g,p}\| \tag{N10}
$$
für alle $r$. Das widerspricht (N9).

**Satz (lokale Nichtinnerheit).**
$$
\boxed{D_g|_{A_{(p),\mathrm{alg}}} \notin B^1\!\left(A_{(p),\mathrm{alg}},\, M_{g,p}^{\log}\right).} \tag{N11}
$$

**Korollar.**
$$
\boxed{[D_g|_{A_{(p),\mathrm{alg}}}] \in HH^1\!\left(A_{(p),\mathrm{alg}},\, M_{g,p}^{\log}\right) \setminus \{0\}.} \tag{N12}
$$

**Bemerkung.** Kein Normdichtheitsargument erforderlich: Die Testelemente $\mu_{p^r}$
liegen bereits in $A_{(p),\mathrm{alg}}$, und der Kommutatorschranke (N10) genügt
für den Widerspruch. $\square$

---

### [O-217-2c-6] — Lokal-globaler Klebeknoten

> **Status: ?[O]** — entsperrt

Vier getrennte Aufgaben:

1. **Fremd-Primstabilität:** $\sigma_q(M_{(p)}^{\log})\subseteq M_{(p)}^{\log}$,
   $\rho_q(M_{(p)}^{\log})\subseteq M_{(p)}^{\log}$ für $q\neq p$.
2. **Kreuzprodukte:** Verhalten von $M_{(p)}^{\log}\cdot M_{(q)}^{\log}$, $q\neq p$.
3. **Globaler Koeffizientenmodul:**
   $$M_g^{\log} \supseteq \sum_p M_{g,p}^{\log};$$
   Typfrage: direkte Summe $\bigoplus_p$ oder gemischter Abschluss
   (Faktorialtiefe koppelt Primkomponenten).
4. **Globaler Landungsnachweis:** $D_g(A_{\mathrm{alg}}) \subseteq M_g^{\log}$.

$\square$

### [O-217-2c-alg] — Multiplikative Abgeschlossenheit ?[O] nachrangig

---

## DAG-Pfad: $Z^1 \to HH^1 \to$ globaler Typ $\to$ Grad-4-Aufstieg

```
geladene Derivation D_g
        │
        ▼
[O-217-2b] gcd-Fallzerlegung                               ✓[M]_part
        │
        ▼
[O-217-2c-1]–[O-217-2c-5]  D_g ∈ Z^1(A_(p),alg, M_g,p^log)  ✓[M]
        │
        ▼
[O-217-2c-5b]  [D_g] ≠ 0 in HH^1  (Normdivergenzbeweis)       ✓[M]
        │
        ▼
[O-217-2c-6]  lokal-globaler Klebeknoten                      ?[O]
   ├─ q≠p Stabilität
   ├─ Kreuzprodukte M_(p)^log · M_(q)^log
   ├─ Konstruktion M_g^log ⊇ Σ_p M_g,p^log
   └─ D_g(A_alg) ⊆ M_g^log
        │
        ▼
  HH^1(A_alg, M_g^log)  — globaler Grad-1-Baustein
        │
        ▼
  Cup-Produkt ∪ [HH^3-Partner]  → Grad-4-Klasse
        │
        ▼
     Objekt X.3
```

---

## DAG-Knotenstatus

| Knoten | Inhalt | Status |
|---|---|---|
| [O-217-2b-1] | Fallzerlegung A, B, C | ✓[K] |
| [O-217-2b-2] | Fall A | ✓[M] |
| [O-217-2b-3] | Fall B | ✓[M] |
| [O-217-2b-4] | Fall C | ✓[M] |
| [O-217-2b-5] | Endlich viele Faktoren; Typvorlage | ✓[M]$_{\mathrm{part}}$ |
| [O-217-2b-6] | Kein globaler $V_g$; Typvorlage | ✓[M]$_{\mathrm{part}}$ |
| [O-217-2c-1] | Lineare Defektspanne $S_{(p)}^{\log}$ | ✓[K] |
| [O-217-2c-2] | $\sigma_p$-Transport (T1)–(T2) | ✓[M] |
| [O-217-2c-3] | $\rho_p$-Transport (T3)–(T4); Strukturstelle $1-E_p$ | ✓[M] |
| [O-217-2c-4] | $M_{(p)}^{\log}$ Bimodul; $\sigma_p$-, $\rho_p$-Stabilität | ✓[M] |
| [O-217-2c-5] | $D_g(A_{(p),\mathrm{alg}})\subseteq M_{g,p}^{\log}$; $D_g\in Z^1$ | ✓[M] |
| [O-217-2c-5b] | Lokale Nichtinnerheit via Normdivergenzbeweis; $[D_g]\neq 0$ in $HH^1$ | ✓[M] |
| [O-217-2c-6] | Lokal-globaler Klebeknoten; $M_g^{\log}$; globaler Landungsnachweis | ?[O] |
| [O-217-2c-alg] | Multiplikative Abgeschlossenheit (optional) | ?[O] nachrangig |
