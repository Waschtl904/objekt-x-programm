# NEU-217 rev.3 — Lokaler $p$-Block

**Status:** [O-217-0] ✓[K/M] | [O-217-1a] ✓[K] | [O-217-1b] ✓[K/M] | [O-217-1c] ✓[M]$_\mathrm{neg}$ | [O-217-1d] ?[O] | [O-217-2a] ✓[M] | [O-217-2b] ?[O] | [O-217-2c] ?[O] | [O-217-3] ✓[M]  
**Erstellt:** 2026-07-21 (rev.3)  
**Revisionen:**
- rev.1: Initialstruktur.
- rev.2: O-217-0 ✓[K/M]; O-217-3 ✓[M]; O-217-2 aufgespalten; Gradkonflikt $\delta_p$ vs. $D_g$; $S\leftrightarrow\mu_p$ als Darstellungsrelation.
- rev.3: O-217-1 in 1a/1b/1c/1d aufgespalten; Faithfulness-Negativresultat (1c); O-217-2a koordinatenfrei ✓[M]; O-217-1d offen.

**Vorgänger:** NEU-216 rev.6 (vollständig); KONVENTIONEN.md rev.6

---

## 217.A — Typisierung $N$, $S$, $H_p$ ([O-217-0]) ✓[K/M]

$$\mathcal H_p:=\ell^2(\mathbb N_0),\qquad\mathcal C_p:=\operatorname{span}\{\delta_n:n\ge0\}.$$
$$N\delta_n:=n\delta_n,\qquad\operatorname{Dom}(N):=\left\{\xi:\sum_{n\ge0}n^2|\xi_n|^2<\infty\right\}.$$
$N$ selbstadjungiert; $\mathcal C_p\subset\operatorname{Dom}(N)$ invarianter Kern. Unilateraler Shift: $S\delta_n=\delta_{n+1}$, $S^*\delta_0=0$, $S^*\delta_n=\delta_{n-1}$ $(n\ge1)$. $S$ Isometrie; $S^*S=1$, $SS^*\neq1$.

Kommutatoren auf $\mathcal C_p$ mit beschränkten Fortsetzungen auf $\mathcal H_p$:
$$[N,S]=S,\qquad[N,S^*]=-S^*.$$
$$\boxed{H_p:=(\log p)N,\qquad[H_p,S]=(\log p)S,\quad[H_p,S^*]=-(\log p)S^*.}$$
$$\boxed{H_p\notin\mathcal A^{\log}.}\qquad\text{(unbeschränkter Implementierer, kein Koeffizient)}$$

$$\boxed{[O\text{-}217\text{-}0]\quad\checkmark[K/M]}$$

---

## 217.B — Vorzeichenkonsistenz ([O-217-3]) ✓[M]

Nach KONVENTIONEN.md (verbindlich): $[H,\mu_n]=+\log(n)\mu_n$, $[H,\mu_n^*]=-\log(n)\mu_n^*$. Unter $\pi_{p,x_0}(\mu_p)=S$:
$$[H_p,S]=(\log p)S\;✓,\qquad[H_p,S^*]=-(\log p)S^*\;✓.$$

$$\boxed{[O\text{-}217\text{-}3]\quad\checkmark[M]}$$

---

## 217.C — Abstrakte lokale $p$-Algebra: drei Ebenen ([O-217-1a]) ✓[K]

**Algebraischer lokaler Kern [K]:**
$$A_{(p),\mathrm{alg}} := \operatorname{span}\bigl\{\mu_p^a f\mu_p^{*b}: a,b\in\mathbb N_0,\; f\in B_{\mathrm{alg}}\bigr\} \subseteq A_{\mathrm{alg}}.$$

**Logarithmischer lokaler Koeffiziententyp [K]:**
$$A_{(p)}^{\log} := \operatorname{span}_{\mathrm{fin}}\bigl\{\mu_p^a f\mu_p^{*b}: a,b\in\mathbb N_0,\; f\in\mathcal B^{\log}\bigr\} \subseteq \mathcal A^{\log}.$$

**Abstrakte lokale $C^*$-Algebra [K] (koordinatenfrei):**
$$\boxed{A_{(p)} := C^*\bigl(C(\widehat{\mathbb Z}),\mu_p\bigr) \subseteq A_{C^*}.}$$
Keine konkrete Darstellung; Gleichheiten in $A_{(p)}$ sind Gleichheiten in $A_{C^*}$.

$$\boxed{[O\text{-}217\text{-}1a]\quad\checkmark[K]}$$

---

## 217.D — Kovariante Orbitdarstellung ([O-217-1b]) ✓[K/M]

**Konstruktion [K].** Wähle $x_0\in\widehat{\mathbb Z}\setminus p\widehat{\mathbb Z}$. Definiere auf $\mathcal H_p=\ell^2(\mathbb N_0)$:
$$\pi_{p,x_0}(f)\delta_n := f(p^n x_0)\delta_n,\qquad\pi_{p,x_0}(\mu_p) := S.$$

**Relationsverifikation [M].** Die vollständige BC-Relationsfamilie wird erfüllt:
$$S^*\pi_{p,x_0}(f)S\,\delta_n = f(p^{n+1}x_0)\delta_n = \pi_{p,x_0}(\sigma_p(f))\delta_n \qquad\Rightarrow\qquad S^*\pi(f)S=\pi(\sigma_p(f)).\tag{D.1}$$
Für $n\ge1$: $S\pi(f)S^*\delta_n=f(p^{n-1}x_0)\delta_n$. Da $x_0\notin p\widehat{\mathbb Z}$, gilt $p^nx_0\in p\widehat{\mathbb Z}\Leftrightarrow n\ge1$:
$$S\pi_{p,x_0}(f)S^* = \pi_{p,x_0}(\rho_p(f)).\tag{D.2}$$
$$S^*S=1,\qquad SS^*=\pi_{p,x_0}(E_p).\tag{D.3}$$
Sowohl die unitalen $\sigma_p$- als auch die nichtunitalen $\rho_p$-Relationen werden korrekt repräsentiert.

$$\pi_{p,x_0}: A_{(p)} \longrightarrow \mathcal B(\ell^2(\mathbb N_0))\quad\text{wohldefinierter }*\text{-Homomorphismus}.$$

$$\boxed{[O\text{-}217\text{-}1b]\quad\checkmark[K/M]}$$

---

## 217.E — Eine einzelne Orbitdarstellung ist nicht treu ([O-217-1c]) ✓[M]$_\mathrm{neg}$

**Orbithülle.** $X_{p,x_0}:=\overline{\{p^n x_0:n\ge0\}}\subseteq\widehat{\mathbb Z}$.

**Kern:**
$$\ker\bigl(\pi_{p,x_0}|_{C(\widehat{\mathbb Z})}\bigr)=\{f:f|_{X_{p,x_0}}=0\}.\tag{E.1}$$

**Echte Teilmenge.** Für jede Primzahl $q\neq p$ ist $p$ eine Einheit in $\mathbb Z_q$, also
$$v_q(p^n x_0)=v_q(x_0)\qquad\text{für alle }n\ge0.$$
Die $q$-adische Bewertung ändert sich entlang des Orbits nicht. Daher liegt $X_{p,x_0}$ in der echten abgeschlossenen Menge $\{x:\nu_q(x)=v_q(x_0)\}\subsetneq\widehat{\mathbb Z}$, und
$$X_{p,x_0}\subsetneq\widehat{\mathbb Z}.$$
Also existiert eine klopene Menge $U\subseteq\widehat{\mathbb Z}\setminus X_{p,x_0}$, und $f=1_U$ erfüllt $f\neq0$, $\pi_{p,x_0}(f)=0$.

$$\boxed{\pi_{p,x_0}|_{C(\widehat{\mathbb Z})}\text{ ist nicht treu}\;\Rightarrow\;\pi_{p,x_0}|_{A_{(p)}}\text{ ist nicht treu.}}$$

**Konsequenz.** Operatorgleichheiten in $A_{(p),x_0}^{\mathrm{orb}}:=\pi_{p,x_0}(A_{(p)})$ dürfen ohne zusätzlichen Trennungssatz nicht nach $A_{(p)}$ zurückgetragen werden. Die vormals vorgeschlagene Route "Faithfulness über Injektivität auf dem dichten algebraischen Kern" ist abgeschlossen: Sie scheitert bereits auf $B_{\mathrm{alg}}\subset C(\widehat{\mathbb Z})$.

$$\boxed{[O\text{-}217\text{-}1c]\quad\checkmark[M]_{\mathrm{neg}}}$$

---

## 217.F — Treue Darstellungsfamilie oder lokaler Trennungssatz ([O-217-1d]) ?[O]

Für Rüktransporte von $A_{(p),x_0}^{\mathrm{orb}}$ nach $A_{(p)}$ benötigt man eines von:
1. **Familie.** Eine trennende Familie $\{\pi_{p,x_\alpha}\}_{\alpha}$ von Orbitdarstellungen (z.B. über alle $x_0\in\widehat{\mathbb Z}\setminus p\widehat{\mathbb Z}$), deren direktes Produkt $\bigoplus_\alpha\pi_{p,x_\alpha}$ treu ist.
2. **Trennungssatz.** Einen abstrakten Trennungssatz für $A_{(p)}$ analog zum Fell-Theorem oder zur Tomiyama-Takesaki-Theorie.

Bis zur Klärung von [O-217-1d] bleiben alle Argumente, die eine Gleichheit in $A_{(p)}$ aus dem Orbitmodell ableiten wollen, als nicht vollständig typisiert zu kennzeichnen.

$$\boxed{[O\text{-}217\text{-}1d]\quad ?[O]}$$

---

## 217.G — Neutrale $p$-Gaugeableitung koordinatenfrei ([O-217-2a]) ✓[M]

**Lokale Gaugewirkung (abstrakt, ohne Darstellung).** Auf $A_{(p),\mathrm{alg}}$:
$$\gamma_t^{(p)}(f):=f\;(f\in B_{\mathrm{alg}}),\qquad\gamma_t^{(p)}(\mu_p):=p^{it}\mu_p.$$
Auf Monomen:
$$\gamma_t^{(p)}(\mu_p^a f\mu_p^{*b})=e^{it(a-b)\log p}\mu_p^a f\mu_p^{*b}.$$
Die Familie $(\gamma_t^{(p)})_{t\in\mathbb R}$ ist eine stark stetige Gruppe von $*$-Automorphismen auf $A_{(p)}$.

**Infinitesimaler Generator [M].** Auf $A_{(p),\mathrm{alg}}$:
$$\boxed{\delta_p^{(0)}(\mu_p^a f\mu_p^{*b}) := (a-b)(\log p)\mu_p^a f\mu_p^{*b}.}\tag{G.1}$$
Insbesondere:
$$\delta_p^{(0)}(f)=0,\quad\delta_p^{(0)}(\mu_p)=(\log p)\mu_p,\quad\delta_p^{(0)}(\mu_p^*)=-(\log p)\mu_p^*.$$

$\delta_p^{(0)}$ ist eine **gradneutrale** $*$-Derivation: $\delta_p^{(0)}(xy)=\delta_p^{(0)}(x)y+x\delta_p^{(0)}(y)$, $\delta_p^{(0)}(x^*)=\delta_p^{(0)}(x)^*$.

**Nicht beschränkt:** $\|\delta_p^{(0)}(\mu_p^a)\|=a\log p\to\infty$. Typ: unbeschränkter abgeschlossener Generator mit $A_{(p),\mathrm{alg}}\subset\operatorname{Dom}(\delta_p^{(0)})$.

**Orbitdarstellung [M].** Auf $\mathcal C_p$:
$$\pi_{p,x_0}\bigl(\delta_p^{(0)}(x)\bigr)=[H_p,\pi_{p,x_0}(x)].\tag{G.2}$$
$H_p$ ist konkreter Implementierer von $\delta_p^{(0)}$ im Orbitmodell, ohne selbst Koeffizient zu sein.

$$\boxed{[O\text{-}217\text{-}2a]\quad\checkmark[M]}$$

---

## 217.H — Gradkonflikt und geladene Faktorisierung ([O-217-2b]) ?[O]

**Typkonflikt (fixiert).** $\delta_p^{(0)}$ ist gradneutral, $D_g$ hat Grad $g$:
$$\boxed{\deg(\delta_p^{(0)})=1,\qquad\deg(D_g)=g.}$$
Für $g\neq1$ ist $\delta_p^{(0)}=D_g|_{A_{(p)}}$ typwidrig.

**Offene Frage.** Die Generatorformeln aus NEU-211 liefern auf homogenen Elementen Terme
$$D_g(\mu_{p^m/p^n}) = \mu_{p^a}G_{p^\alpha,p^\beta}\mu_{p^b}^* + \cdots$$
mit spezifischen $a,b,\alpha,\beta$ (abhängig von $\gcd$-Aufspaltungen). Zu klären:
- Lässt sich $D_g|_{A_{(p),\mathrm{alg}}}$ komponentenweise als $V_g^{(i)}\cdot\Delta_{g,p}^{(i)}$ schreiben, mit $V_g^{(i)}\in\mathcal A_g^{\log}$ und $\Delta_{g,p}^{(i)}$ neutral oder bimodulwertig?
- Vorsicht: Nicht notwendig eine globale Formel $D_g=V_g\delta_p^{(0)}$; je nach Generator unterschiedliche gekürzte homogene Faktoren (nichtteilerfremde Formeln aus NEU-211).

$$\boxed{[O\text{-}217\text{-}2b]\quad ?[O]}$$

---

## 217.I — Lokale Koeffizienten $G_{p^a,p^b}$ ([O-217-2c]) ?[O]

Aus [O-216-3] (✓[M]): $G_{p^a,p^b}\in\mathcal B^{\log}$ mit
$$A:=C_\sigma(p^a)=pa,\quad D:=C_\sigma(p^b)=pb,\quad C'(p^a,p^b)=\max\{N_{p^a,p^b}M_{p^a,p^b},\,2p(a+b)\}.$$

Offen:
1. Existiert ein $p$-lokaler Teilraum $\mathcal B_{(p)}^{\log}\subseteq\mathcal B^{\log}$, abgeschlossen unter $\sigma_p$, $\rho_p$, der alle $G_{p^a,p^b}$ enthält?
2. Sind $G_{p^a,p^b}$ Koeffizienten in den Generatorformeln von $D_g|_{A_{(p)}}$ (aus NEU-211), und damit **nicht** allein Werte von $\delta_p^{(0)}$ (welches auf Koeffizienten null liefert)? (Konkrete Manifestation des Gradkonflikts.)

$$\boxed{[O\text{-}217\text{-}2c]\quad ?[O]}$$

---

## 217.J — DAG-Stand (rev.3)

```
NEU-216 [O-216-4] K/M    D_g(A_alg) in A^log
      |
[O-217-0] K/M     H_p=(log p)N; Dom; C_p; [N,S]=S; [N,S*]=-S*; H_p not in A^log
[O-217-3] M       [H_p,S]=+log(p)S konsistent mit KONVENTIONEN.md
[O-217-1a] K      abstrakte Ebenen: A_(p,alg), A_(p)^log, A_(p)=C*(C(Zhat),mu_p)
[O-217-1b] K/M    kovariante Orbitdarst. pi_{p,x0}; sigma_p, rho_p, E_p Relationen
[O-217-1c] M_neg  Einzelne Orbitdarst. nicht treu (q-adische Bewertung)
[O-217-1d] ?[O]   Trennende Darstellungsfamilie ODER lokaler Trennungssatz
[O-217-2a] M      delta_p^(0) koordinatenfrei via gamma_t^(p); pi_{p,x0}(delta_p^(0)(x))=[H_p,pi(x)]
[O-217-2b] ?[O]   Gradkonflikt; geladene Faktorisierung V_g * Delta_{g,p}; no global D_g=V_g delta_p^(0)
[O-217-2c] ?[O]   G_{p^a,p^b} in B^log; p-lokaler Teilraum; Stellung in D_g vs delta_p^(0)
      |
[O-217-1d] blockiert: keine Rücktransporte aus Orbitmodell nach A_(p)
[O-217-2b] blockiert: erst nach NEU-211-Analyse der lokalen Generatorformeln
NEU-218: ... ?[O]
```

**Nächster offener Entscheidungspunkt:**
$$\boxed{[O\text{-}217\text{-}2b]:\text{ Komponentenweise Faktorisierung von }D_g|_{A_{(p),\mathrm{alg}}}\text{ via NEU-211-Generatorformeln.}}$$
