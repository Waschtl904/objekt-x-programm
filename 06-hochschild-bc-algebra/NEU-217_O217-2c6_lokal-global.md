# NEU-217 — [O-217-2c-6] Lokal-globaler Klebeknoten

> **Aggregierter Status: ✓[K/M]**

## Einordnung im DAG

Voraussetzungen (alle ✓[M]):
- $M_{(p)}^{\log}$ stabiler $B_{(p),\mathrm{alg}}$-Bimodul; $\sigma_p$-, $\rho_p$-Stabilität.
- $D_g(A_{(p),\mathrm{alg}}) \subseteq M_{g,p}^{\log}$.
- $[D_g|_{A_{(p),\mathrm{alg}}}] \neq 0$ in $HH^1(A_{(p),\mathrm{alg}}, M_{g,p}^{\log})$. (Commit `b562530`)
- Fremdpriminstabilität: $\sigma_q(M_{(p)}^{\log})\not\subseteq M_{(p)}^{\log}$ für $q\neq p$. (Commit `2bf38f4`)

**Ergebnis dieses Knotens.**
$$
\boxed{D_g \in Z^1\!\left(A_{\mathrm{alg}},\,\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g, \qquad
[D_g] \neq 0 \text{ in } HH^1\!\left(A_{\mathrm{alg}},\, \mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g.}
$$

---

## [O-217-2c-6a] — Fremdprimwirkung auf $M_{(p)}^{\log}$

> **Status: ✓[M]$_{\mathrm{neg}}$** (Commit `2bf38f4`)

**[6a-T] ✓[M]:** $\sigma_q(G_{p^a,p^b}) = G_{qp^a,p^b} - \rho_{p^b}(G_{q,1})$;
$\rho_q(G_{p^a,p^b}) = G_{p^a,qp^b} - \sigma_{p^a}(G_{1,q})$.

**[6a-coeff] ✓[M]:** $\rho_q(E_{p^r})=E_qE_{p^r}\neq E_{p^r}$;
$\rho_q(B_{(p),\mathrm{alg}})\subseteq E_qB_{(p),\mathrm{alg}}\not\subseteq B_{(p),\mathrm{alg}}$.

**[6a-sep] ✓[M]$_{\mathrm{neg}}$:** Zwei-Punkt-Zeuge $\Lambda_{x,y}$:
$\sigma_q(M_{(p)}^{\log})\not\subseteq M_{(p)}^{\log}$ (S3);
$\rho_q(M_{(p)}^{\log})\not\subseteq M_{(p)}^{\log}$ (R3).

**Grenze:** Ob $\bigoplus_p M_{(p)}^{\log}$ als globale Konstruktion unzureichend ist,
bleibt ein eigenständiger Minimalitätstest; er blockiert weder die Modulstruktur
noch den Hochschildklassennachweis.

---

## [O-217-2c-6b] — Globaler neutraler Defektmodul

### [O-217-2c-6b-def] — Intrinsische Definition ✓[K]

$\mathscr{C}$: Familie aller abgeschlossenen $N\subseteq B^{\log}$ mit
$B_{\mathrm{alg}}NB_{\mathrm{alg}}\subseteq N$,
$\sigma_n(N)\subseteq N$, $\rho_n(N)\subseteq N$ $(n\geq 1)$, $G_{k,d}\in N$.
$$
M_{\mathrm{glob},G}^{\log} := \bigcap_{N\in\mathscr{C}} N. \tag{1}
$$
Robuster globaler Koeffizientenraum (mit explizitem $B_{\mathrm{alg}}$-Term,
da $B_{\mathrm{alg}}\not\subseteq M_{\mathrm{glob},G}^{\log}$ a priori):
$$
\boxed{M_{\mathrm{glob}}^{\log} := \overline{B_{\mathrm{alg}} + M_{\mathrm{glob},G}^{\log}}^{\,\|\cdot\|_{B^{\log}}}.} \tag{2}
$$
$B_{\mathrm{alg}}$ ist separat $\sigma_n$-, $\rho_n$-stabil; damit ist (2) unter allen
Transporten stabil. $\square$

### [O-217-2c-6b-stab] — Vollständige $\sigma_n$-, $\rho_n$-Stabilität ✓[M]

Folgt konstruktiv aus der Schnittdefinition (1): Stabilität ist unter beliebigen
Schnitten erhalten. Allgemeine Transportformel:
$$
\sigma_n(G_{k,d}) = G_{nk/\delta,\,d/\delta} - \rho_{d/\delta}(G_{n/\delta,1}),\quad
\delta:=\gcd(n,d). \tag{G1}
$$
Rechte Seite liegt in $M_{\mathrm{glob},G}^{\log}$ per (1). $\square$

---

## [O-217-2c-6c] — Globaler Landungsnachweis

> **Status: ✓[M]**

### Graduierter $A_{\mathrm{alg}}$-Koeffizientenbimodul

$$
\boxed{\mathfrak{M}_{\mathrm{glob}}^{\log} := \operatorname{span}_{\mathrm{fin}}\!\left\{a\,\xi\,b :\, a,b\in A_{\mathrm{alg}},\; \xi\in M_{\mathrm{glob}}^{\log}\right\} \subseteq \mathcal{A}^{\log}.} \tag{3}
$$

Einbettung: $M_{\mathrm{glob}}^{\log}\subseteq B^{\log}\hookrightarrow C(\widehat{\mathbb{Z}})\hookrightarrow A_{C^*}$ (NEU-216,
isometrisch); $A_{\mathrm{alg}}\subseteq\mathcal{A}^{\log}$; $\mathcal{A}^{\log}$ unter Multiplikation
abgeschlossen. Damit:
$$
\boxed{\mathfrak{M}_{\mathrm{glob}}^{\log}\subseteq\mathcal{A}^{\log}\subseteq A_{C^*}.} \tag{E}
$$

### Landung auf Generatoren (Leibnizschluss)

| Generator | $D_g$-Wert | Quelle | Liegt in |
|---|---|---|---|
| $\mu_k$ | $\mu_u G_{a,d}\mu_v^*$ | NEU-211 | $(\mathfrak{M}_{\mathrm{glob}}^{\log})_g$ |
| $\mu_k^*$ | $-\mu_{u'}G_{a',d'}\mu_{v'}^*$ | NEU-211 | $(\mathfrak{M}_{\mathrm{glob}}^{\log})_g$ |
| $e(r)$ | neutraler Charakterkoeffizient $\in B_{\mathrm{alg}}$ | Charakterabsorption | $B_{\mathrm{alg}}\subseteq M_{\mathrm{glob}}^{\log}$ |

$A_{\mathrm{alg}}$ von $\{e(r),\mu_k,\mu_k^*\}$ erzeugt; Leibnizregel + $A_{\mathrm{alg}}$-Bimodul:
$$
\boxed{D_g(A_{\mathrm{alg}}) \subseteq \left(\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g,
\qquad D_g \in Z^1\!\left(A_{\mathrm{alg}},\, \mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g.} \tag{4}
$$
$\square$

---

## [O-217-2c-6d] — Globale Nichtinnerheit

> **Status: ✓[M]**

**Ziel.**
$$
\boxed{[D_g]\in HH^1\!\left(A_{\mathrm{alg}},\, \mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g \setminus\{0\}.}
$$

### Normtreue der äußeren Isometrien (globaler Rahmen)

Für alle $\xi\in A_{C^*}$, $u,v\geq 1$: $\|\mu_u\|=\|\mu_v^*\|=1$ und
$\mu_u^*(\mu_u\xi\mu_v^*)\mu_v=\xi$, also:
$$
\boxed{\|\mu_u\xi\mu_v^*\|=\|\xi\|.} \tag{3}
$$

### Normdivergenz

NEU-211-Fallzerlegung: $D_g(\mu_{p^r})=\mu_{u_r}G_{p^{a_r},p^{b_r}}\mu_{v_r}^*$
mit $a_r+b_r=r\to\infty$.
$C(\widehat{\mathbb{Z}})\hookrightarrow A_{C^*}$ isometrisch (NEU-216), also
$\|G_{p^{a_r},p^{b_r}}\|_{A_{C^*}}=\|G_{p^{a_r},p^{b_r}}\|_\infty$.
$p$-adischer Testpunkt (Commit `b562530`):
$$
\|G_{p^{a_r},p^{b_r}}\|_\infty \geq \log\!\left(\frac{\lambda_p(r)+2}{p}\right) \longrightarrow\infty. \tag{5}
$$
Mit (3):
$$
\boxed{\|D_g(\mu_{p^r})\| = \|G_{p^{a_r},p^{b_r}}\|_\infty \longrightarrow\infty.} \tag{6}
$$

### Ausschluss eines globalen Implementierers

Angenommen $W_g\in\mathfrak{M}_{\mathrm{glob}}^{\log}\subseteq A_{C^*}$ (via (E)) erfülle
$D_g(x)=W_gx-xW_g$ auf $A_{\mathrm{alg}}$. Dann:
$$
\|D_g(\mu_{p^r})\|=\|[W_g,\mu_{p^r}]\|\leq 2\|W_g\| \tag{7}
$$
unabhängig von $r$. Widerspruch zu (6). $\square$
$$
\boxed{D_g\notin B^1\!\left(A_{\mathrm{alg}},\,\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g,
\qquad [D_g]\in HH^1\!\left(A_{\mathrm{alg}},\,\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g\setminus\{0\}.} \tag{8--9}
$$

### Zweiter Beweis via NEU-211

NEU-211 [O-211-4] hat bewiesen: kein $W\in A_{C^*}$ implementiert $D_g$ auf $A_{\mathrm{alg}}$.
Da $\mathfrak{M}_{\mathrm{glob}}^{\log}\subseteq A_{C^*}$ (via (E)), folgt (8) direkt.
Der Normdivergenzbeweis ist dennoch eigenständig wertvoll, weil er den Nachweis
innerhalb der NEU-217-Architektur reproduziert. $\square$

---

## Abschluss: Grad-1-Pfad vollständig

Der gesamte Pfad ist geschlossen:

```
geladene Derivation D_g
       |
       v
Z^1_lok  (O-217-2c-5)        [M]
       |
       v
HH^1_lok != 0  (O-217-2c-5b) [M]   Normdivergenzbeweis (b562530)
       |
       v
Fremdpriminstab. (O-217-2c-6a) [M]_neg  Zwei-Punkt-Zeuge (2bf38f4)
       |
       v
M_glob^log  (O-217-2c-6b)    [M]   intrinsische Konstruktion
       |
       v
Z^1_glob  (O-217-2c-6c)      [M]   Leibnizschluss
       |
       v
HH^1_glob != 0  (O-217-2c-6d) [M]  Normdivergenzbeweis global
       |
       v
  [D_g] in HH^1(A_alg, fM_glob^log)_g \ {0}
       |
       v
  NAECHSTER HAUPTBLOCK:
  [Theta_3] in HH^3(A_alg, N)_1
  Cup: [D_g] smile [Theta_3] in HH^4(A_alg, M_4)_g
  --> Grad-4-Schicht Objekt X.3
```

---

## Knotenstatus

| Knoten | Inhalt | Status |
|---|---|---|
| [O-217-2c-6a] | Fremdpriminstabilität $\sigma_q,\rho_q$ | ✓[M]$_{\mathrm{neg}}$ |
| [O-217-2c-6a-T] | Transportformeln (F1)--(F2) | ✓[M] |
| [O-217-2c-6a-coeff] | $\rho_q(E_{p^r})=E_qE_{p^r}$; Koeffizientenverlust | ✓[M] |
| [O-217-2c-6a-sep] | Zwei-Punkt-Zeuge; $\sigma_q$ (S3); $\rho_q$ (R3) | ✓[M]$_{\mathrm{neg}}$ |
| [O-217-2c-6b-def] | $M_{\mathrm{glob}}^{\log}$, intrinsische Def. (1)+(2) | ✓[K] |
| [O-217-2c-6b-stab] | $\sigma_n$-, $\rho_n$-Stabilität | ✓[M] |
| [O-217-2c-6c] | $D_g\in Z^1(A_{\mathrm{alg}},\mathfrak{M}_{\mathrm{glob}}^{\log})_g$ | ✓[M] |
| [O-217-2c-6d] | $[D_g]\neq 0$ in $HH^1(A_{\mathrm{alg}},\mathfrak{M}_{\mathrm{glob}}^{\log})_g$ | ✓[M] |
| **[O-217-2c-6]** | **Aggregiert** | **✓[K/M]** |
