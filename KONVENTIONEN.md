# Verbindliche Konventionen (BC-Algebra)

> Diese Datei ist maßgeblich. Bei Widersprüchen zwischen Katalogeinträgen hat KONVENTIONEN.md Vorrang.

---

## 1. Basisrelationen der BC-Algebra $A_{C^*}$

$$\mu_k^*\mu_k = 1, \qquad \mu_k\mu_k^* = E_k \neq 1\;(k>1),$$
$$e(r)^*=e(-r),\quad e(r)e(s)=e(r+s),\quad e(0)=1,$$
$$\mu_k e(r)=e(kr)\mu_k, \qquad \mu_k^* e(r)=\frac1k\sum_{ks=r}e(s)\,\mu_k^*.$$

---

## 2. Endomorphismen des abelschen Sektors $C(\hat{\mathbb Z})$

| Symbol | Definition | Unital? | Fourierform |
|---|---|---|---|
| $\rho_k(f):=\mu_kf\mu_k^*$ | Range-Endomorphismus | **Nein**: $\rho_k(1)=E_k=1_{k\hat{\mathbb Z}}\neq 1$ | $(\rho_kf)(x)=1_{k\hat{\mathbb Z}}(x)\cdot f(x/k)$ |
| $\sigma_k(f):=\mu_k^*f\mu_k$ | Unitaler Endomorphismus | **Ja**: $\sigma_k(1)=1$ | $(\sigma_kf)(x)=f(kx)$ |

**Typologische Regel.** $\sigma_k,\rho_k$ wirken auf Funktionen; Punktabbildungen: $\phi_k(x)=kx$, $\psi_k(x)=x/k$. Der Ausdruck $\nu(\sigma_k(x))$ ist falsch; korrekt: $\nu(kx)$.

**Translation $T_a$ (kanonisch):**
$$\boxed{T_a := \sigma_a, \qquad (T_af)(x)=f(ax).}$$
Herleitung via BC-Kovarianz $f\mu_a=\mu_a\sigma_a(f)$; Verifikation: $\sigma_a(E_L)=E_{L/(L,a)}$, $T_a(e(r))=e(ar)$.

**BC-Kovarianzrelationen:**
$$f\mu_k = \mu_k\sigma_k(f), \qquad \mu_k^*f = \sigma_k(f)\mu_k^*.$$

---

## 3. Zeitentwicklung

$$[H,\mu_n]=+\log(n)\mu_n, \qquad [H,\mu_{p^m}]=m\log(p)\mu_{p^m}.$$

---

## 4. Rangeprojektionen

$$E_k=1_{k\hat{\mathbb Z}},\quad E_k\neq1\;(k>1),\quad E_1=1,\quad E_k=\rho_k(1)\in\mathcal B^{\log}.$$

---

## 5. Faktorialschalen und $\mathcal B^{\log}$ (NEU-216, vollständig)

$$L_j:=(j+1)!,\quad S_j:=L_j\hat{\mathbb Z}\setminus L_{j+1}\hat{\mathbb Z},\quad \nu(x):=j\;(x\in S_j),\quad\mu(S_j)=\frac{j+1}{(j+2)!}.$$
$$m_j(f):=\frac1{\mu(S_j)}\int_{S_j}f\,d\mu, \quad\|m_j\|=1.$$
$$[f]_{\tan}:=\sup_j(j+1)\operatorname{osc}_{S_j}(f),\quad [f]_{\mathrm{rad}}:=\sup_j(j+1)|m_{j+1}(f)-m_j(f)|.$$
$$\|f\|_{\mathcal B^{\log}}:=\|f\|_\infty+[f]_{\tan}+[f]_{\mathrm{rad}}.$$

**Submultiplikativität (ohne Renormierung):**
$$[fg]_{\tan}\le\|f\|_\infty[g]_{\tan}+\|g\|_\infty[f]_{\tan}, \qquad [fg]_{\mathrm{rad}}\le\|f\|_\infty[g]_{\mathrm{rad}}+\|g\|_\infty[f]_{\mathrm{rad}}+[f]_{\tan}[g]_{\tan}.$$
$$\boxed{\|fg\|_{\mathcal B^{\log}}\le\|f\|_{\mathcal B^{\log}}\|g\|_{\mathcal B^{\log}}.}$$

**Schalenbandkonstanten:**
$$C_\sigma(k):=\max_{p\mid k}p\,v_p(k),\quad C_\sigma(1):=0; \qquad 0\le\nu(kx)-\nu(x)\le C_\sigma(k)\;(x\neq0).$$
$$J(k):=\min\{j:k\mid(j+1)!\}; \qquad \nu(x)-C_\sigma(k)\le\nu(x/k)\le\nu(x)\;(j\ge J(k)).$$

**Band-Mittelwertlemma** (scharfe Konstanten):
$$K_0=1,\quad K_C=2C\;(C\ge1); \qquad \left|\int f\,d\eta-m_j(f)\right|\le\frac{K_C}{j+1}\,q(f),\quad q(f):=[f]_{\tan}+[f]_{\mathrm{rad}}.$$

**Transportstabilität:** $\sigma_k(\mathcal B^{\log})\subseteq\mathcal B^{\log}$, $\rho_k(\mathcal B^{\log})\subseteq\mathcal B^{\log}$, $T_a(\mathcal B^{\log})\subseteq\mathcal B^{\log}$.

**Transportdefekte:** $G_{a,d}\in\mathcal B^{\log}$ für alle festen $a,d$; $\|G_{a,d}\|_{\mathcal B^{\log}}\le C(a,d)<\infty$ mit expliziten $M_{a,d}$, $C'(a,d)=\max(N_{a,d}M_{a,d},2(A+D))$.

**Typtrennung:** $\mathcal B_{\mathrm{alg}}\subsetneq\mathcal B^{\log}\subsetneq C(\hat{\mathbb Z})$ (echte Inklusionen).

---

## 6. Geladener Koeffiziententyp $\mathcal A^{\log}$ (NEU-216, vollständig)

$$\mathcal A_h^{\log}:=\mu_m\mathcal B^{\log}\mu_n^*\quad((m,n)=1,\;h=m/n), \qquad \|\mu_mf\mu_n^*\|_{h,\log}:=\|f\|_{\mathcal B^{\log}}.$$
$$\mathcal A^{\log}:=\operatorname{span}_{\mathrm{fin}}\{\mathcal A_h^{\log}:h\in\mathbb Q_+^\times\}\subset A_{C^*}.$$
$$\mathcal A_h^{\log}\mathcal A_{h'}^{\log}\subseteq\mathcal A_{hh'}^{\log}, \qquad (\mathcal A_h^{\log})^*=\mathcal A_{h^{-1}}^{\log}, \qquad D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}.$$

---

## 7. Revisionshistorie

| Datum | Änderung |
|---|---|
| 2026-07-21 | Erstellt; $\rho_k/\sigma_k$ fixiert |
| 2026-07-21 | $\rho_k$-Fourierform; Seminormen |
| 2026-07-21 | $m_j$; Typtrennung |
| 2026-07-21 | Typ. Regel; $C_\sigma(k)$; $J(k)$ |
| 2026-07-21 | $T_a:=\sigma_a$; Mittelwertlemma; Transportstab. |
| 2026-07-21 | Vollst. Audit: scharfe Konstanten, submultiplik. Norm, $G_{a,d}$ explizit, $\mathcal A^{\log}$ |


---

## Operatorkonventionen X.3 (verbindlich ab NEU-225)

**Antisymmetrisierte Kopplung.** Verbindlich ist

$$J_N^- := \tfrac12\bigl(\Theta_N-\Theta_N^\dagger\bigr) \qquad (37.1)$$

Nur diese Fassung erfüllt $(J_N^-)^*=-J_N^-$ (54.3) und macht $D_{\mathrm{rel}}=\overline{iJ^-}$
selbstadjungiert. Die Schreibweise $\frac{1}{2i}(\Theta_N-\Theta_N^{\mathrm{Wres}})$ aus NEU-35
(Z. 220) und NEU-62 (Z. 98) bezeichnet einen **anderen, selbstadjungierten** Operator und heißt
ab sofort $S_N := \frac{1}{2i}(\Theta_N-\Theta_N^\dagger) = -iJ_N^-$. Beide dürfen nicht
gleichgesetzt werden.

**Graphbasis — korrigiert durch NEU-226 §4.** Die $\eta$-Familie ist **nicht** global
orthonormal. Verbindlich ist nur die Orthonormalität **innerhalb** einer Kette bei festem
$(p,m,u)$:

$$\langle\eta_{p;m;r,u},\eta_{p;m;r',u}\rangle=\delta_{rr'}$$

Über verschiedene $(p,m,u)$ hinweg ist das Skalarprodukt **unbestimmt und generisch $\neq0$**:
nach (51.2) gilt $\eta_{p;m;s,u}\sim e_{u+ps}V_{pm}$, und verschiedene $(p,m)$ treffen dasselbe
$V_{pm}$ (etwa $2\cdot3=3\cdot2$). Genau diese Überlappung erzeugt die Off-Diagonalterme
$K_{pq}\neq0$ (51.5). Die frühere Festlegung
$\langle\cdot,\cdot\rangle=\delta_{pp'}\delta_{mm'}\delta_{rr'}\delta_{uu'}$ aus NEU-225 §1.2
ist **zurückgerollt**. `✓[M]_neg`

Die Familie ist ferner **keine Eigenbasis** von $D_{\mathrm{rel}}$ (52.D0) — nach NEU-225 hat
$D_{\mathrm{rel}}$ überhaupt keine Eigenwerte. Formeln, die eine Eigenzerlegung
$D_{\mathrm{rel}}\eta_\alpha=\lambda_\alpha\eta_\alpha$ ansetzen (so (51.3)/(51.4)/(51.7)),
müssen auf Spektralmaßform umgeschrieben werden.

**Wörterbuch $(r,n)\leftrightarrow(p,m,r,u)$.** $r\in\mathbb Z$ Charakterindex, unter $\Theta$
um $+n$ verschoben; $n$ Isometrieindex, **erhalten**; $m$ Fasernummer, Kanten nur für $n\mid m$;
$p,u$ unbewegt. Also $\Theta\eta_{p;m;r,u}=\sum_{n\mid m}\alpha_n r\,\eta_{p;m;r+n,u}$ mit
$\alpha_n=-\gamma_N\log n$; wegen $\log1=0$ tragen nur Teiler $n>1$ bei. Die Faser $m$ ist
invariant.

> **Koordinatenwörterbuch — aufgelöst durch NEU-227 §1.** (55.3) und (51.2) sind keine
> konkurrierenden Definitionen, sondern **zwei Stufen derselben Konstruktion**: (51.2)
> definiert die *Kopplung* $V_p$, (55.3) die *Dynamik* von $J^-$. Verbindlich ist
>
> $$\eta_{p;m;s,u} \longleftrightarrow e_RV_M, \qquad M=pm, \qquad R=u+ps.$$
>
> Die volle Sektorverschiebung $R\mapsto R+M$ ist wegen $u+ps+pm=u+p(s+m)$ identisch mit
> $s\mapsto s+m$; auch das Gewicht stimmt, $R\log M=(u+ps)\log(pm)$. Ein allgemeiner Sprung
> $R\mapsto R\pm d$ bleibt genau dann in derselben $u$-Restklasse, wenn $p\mid d$; für
> $p\nmid d$ mischt er $u$-Klassen. Im Primsektor $M=p$ entfällt $d=1$ wegen $\log1=0$, und
> $d=p$ erfüllt $p\mid d$ — die Einzelkettenrechnung aus NEU-225 ist dort **vollständig und
> gerechtfertigt**. In zusammengesetzten Sektoren ist sie es nicht. `✓[M]`

**Spektraldarstellung.** $D_{\mathrm{rel}}$ hat **keine** Eigenwerte (NEU-225). Verwende
ausschließlich das projektionswertige Spektralmaß $E_{D_{\mathrm{rel}}}$ und die
Kreuzspektralmaße $\mu^{a,b}_{pq}(B)=\langle V_pa,E_D(B)V_qb\rangle$, also
$\langle a,K_{pq}(z)b\rangle=\int_{\mathbb R}(\lambda-z)^{-1}d\mu^{a,b}_{pq}(\lambda)$ (NEU-227 §2).
Keine Eigenbasisformeln.

**$u$-Regulator.** Die Summationsreichweite über $u$ in (51.2) ist ein **echter Regulator**
(51.1). Sie entscheidet über Definiertheit, Beschränktheit und den Übergang $\mathcal S_1$
gegen $\mathcal S_2$. Sie darf **nicht** nachträglich an $\Xi$-Daten angepasst werden.

**Effektiver Raum.** Verbindlich ist
$\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}=(\ker D_{\mathrm{rel}})^\perp=E_{D_{\mathrm{rel}}}(\mathbb R\setminus\{0\})\mathcal H_{\mathrm{rel}}$.
Die Fassung aus (55.0) mit $r\neq0$ **und** $m>1$ ist echt kleiner und nicht invariant (NEU-224 §5.3).
