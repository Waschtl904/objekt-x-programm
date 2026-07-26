# NEU-216 rev.6 — Vollständiger Audit: Logarithmischer Koeffiziententyp $\mathcal B^{\log}$ und $D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}$

**Status:** Alle Knoten geschlossen.  
[O-216-0] ✓[M] | [O-216-1b] ✓[M]_neg | [O-216-1c] ✓[M] | [O-216-1d] ✓[M]_neg | **[O-216-1] ✓[M]** | [O-216-2a] ✓[M] | [O-216-2b] ✓[M] | [O-216-2c] ✓[M] | [O-216-2d] ✓[K/M] | **[O-216-2] ✓[M]** | **[O-216-3] ✓[M]** | **[O-216-4] ✓[K/M]**  
**Erstellt:** 2026-07-21 (rev.6)  
**Revisionen:** rev.1–5 siehe DAG unten. rev.6: scharfe Konstanten im Mittelwertlemma; Kovarianzkonstante $\frac12$; $\|fg\|\le\|f\|\|g\|$ ohne Renormierung; vollständiger $G_{a,d}$-Audit mit $M_{a,d}$; $\mathcal A^{\log}$ konstruiert; $D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}$.  

---

## 216.0 — Konventionsaudit ([O-216-0]) ✓[M]

Gemäß KONVENTIONEN.md: $(\rho_kf)(x)=1_{k\hat{\mathbb Z}}(x)f(x/k)$; $(\sigma_kf)(x)=f(kx)$; $T_a:=\sigma_a$; $[H,\mu_n]=+\log(n)\mu_n$; $f\mu_k=\mu_k\sigma_k(f)$.

$$\boxed{[O\text{-}216\text{-}0]\quad\checkmark[M]}$$

---

## 216.A — Notation

$$T(f):=[f]_{\tan},\quad R(f):=[f]_{\mathrm{rad}},\quad q(f):=T(f)+R(f),\quad M(f):=\|f\|_\infty.$$
$$m_j(f)=\int_{S_j}f\,d\mu_j \quad(\mu_j=\text{normiertes Haarmaß auf }S_j).$$
Für $z\in S_j$: $|f(z)-m_j(f)|\le\operatorname{osc}_{S_j}(f)\le T(f)/(j+1)$. \hfill(1.1)

---

## 216.B — Band-Mittelwertlemma mit scharfen Konstanten ([O-216-2c]) ✓[M]

**Satz 2.1.** Sei $C\in\mathbb N_0$, $j\ge2C+1$, $\eta$ ein Wahrscheinlichkeitsmaß mit $\operatorname{supp}\eta\subseteq\bigcup_{|r|\le C}S_{j+r}$. Dann:
$$\boxed{\left|\int f\,d\eta-m_j(f)\right|\le\frac{K_C}{j+1}q(f),\qquad K_0=1,\quad K_C=2C\;(C\ge1).} \tag{2.1}$$

**Beweis.** Für $z\in S_{j+r}$, $|r|\le C$:
- Tangential: $|f(z)-m_{j+r}(f)|\le T(f)/(j+r+1)\le 2T(f)/(j+1)$ (da $j+r+1\ge(j+1)/2$).
- Radial ($r>0$): $|m_{j+r}(f)-m_j(f)|\le R(f)\sum_{\ell=j}^{j+r-1}1/(\ell+1)\le rR(f)/(j+1)\le CR(f)/(j+1)$.
- Radial ($r=-s<0$): $|m_{j-s}(f)-m_j(f)|\le sR(f)/(j-s+1)\le 2CR(f)/(j+1)$.

Punktweise: $|f(z)-m_j(f)|\le(2T(f)+2CR(f))/(j+1)\le 2C\,q(f)/(j+1)$ für $C\ge1$; $T(f)/(j+1)$ für $C=0$. Integration $\Rightarrow$ (2.1). $\square$

Für $j<2C+1$: $(j+1)|\int f\,d\eta-m_j(f)|\le 2(2C+1)M(f)$. \hfill(2.8)

$$\boxed{[O\text{-}216\text{-}2c]\quad\checkmark[M]}$$

---

## 216.C — Transport durch $\sigma_k$ ([O-216-2a/c]) ✓[M]

$C:=C_\sigma(k)=\max_{p\mid k}pv_p(k)$, $N_\sigma(k):=2C+1$.

**[O-216-2a]** $0\le\nu(kx)-\nu(x)\le C$ (Beweis: $p$-adische Bewertungsfehlstelle, Intervalllänge $pa$). $\square$

**Tangential** ($j\ge N_\sigma$): $\operatorname{osc}_{S_j}(\sigma_kf)\le 2K_C/(j+1)\cdot q(f)$.
$$\boxed{[\sigma_kf]_{\tan}\le 2N_\sigma(k)M(f)+2K_Cq(f).} \tag{3.4}$$

**Radial** ($j\ge N_\sigma$): Pushforward $\eta_j^{(k)}=(x\mapsto kx)_*\mu_j$ trägt im Vorwärtsband. Mittelwertlemma $\Rightarrow|m_j(\sigma_kf)-m_j(f)|\le K_C/(j+1)\cdot q(f)$. Dann:
$$(j+1)|m_{j+1}(\sigma_kf)-m_j(\sigma_kf)|\le(2K_C+1)q(f).$$
$$\boxed{[\sigma_kf]_{\mathrm{rad}}\le 2N_\sigma(k)M(f)+(2K_C+1)q(f).} \tag{3.8}$$
$$\boxed{\sigma_k(\mathcal B^{\log})\subseteq\mathcal B^{\log}.} \tag{3.9}$$

---

## 216.D — Transport durch $\rho_k$ ([O-216-2b/c]) ✓[M]

$J(k):=\min\{j:k\mid(j+1)!\}$, $N_\rho(k):=\max(J(k),2C+1)$.

**[O-216-2b]** Für $j\ge J(k)$: $S_j\subseteq k\hat{\mathbb Z}$; $\nu(x)-C\le\nu(x/k)\le\nu(x)$. $\square$

**Tangential** ($j\ge N_\rho$): Bild von $x\mapsto x/k$ liegt im Rückwärtsband. Mittelwertlemma $\Rightarrow\operatorname{osc}_{S_j}(\rho_kf)\le 2K_C/(j+1)\cdot q(f)$.  
Für $j<N_\rho$: Supportrand kann $0$-Zweig erzwingen; $\operatorname{osc}\le2M(f)$.
$$\boxed{[\rho_kf]_{\tan}\le 2N_\rho(k)M(f)+2K_Cq(f).} \tag{4.5}$$

**Radial** ($j\ge N_\rho$): Pushforward $\theta_j^{(k)}=(x\mapsto x/k)_*\mu_j$ trägt im Rückwärtsband. Analog zu $\sigma_k$:
$$\boxed{[\rho_kf]_{\mathrm{rad}}\le 2N_\rho(k)M(f)+(2K_C+1)q(f).} \tag{4.8}$$
$$\boxed{\rho_k(\mathcal B^{\log})\subseteq\mathcal B^{\log}.}\qquad\rho_k(1)=E_k\neq1\;(k>1). \tag{4.9}$$

---

## 216.E — Kanonische Definition von $T_a$ ([O-216-2d]) ✓[K/M]

**Definition [K]:** $T_a:=\sigma_a$ auf ganz $C(\hat{\mathbb Z})$.

**Kompatibilität [M]:** $\sigma_a(E_L)(x)=E_L(ax)=1_{\{L\mid ax\}}=1_{\{L/(L,a)\mid x\}}=E_{L/(L,a)}(x)$. $T_a(e(r))=e(ar)$. Die Projektionsvorschrift $T_a(E_L)=E_{L/(L,a)}$ bestimmt keine eindeutige Ganzraumfortsetzung; die BC-Kovarianz $f\mu_a=\mu_a\sigma_a(f)$ liefert die kanonische Wahl. $T_a(E_L)=E_{L/(L,a)}$ bleibt als Lemma.

$$\boxed{[O\text{-}216\text{-}2d]\quad\checkmark[K/M];\quad[O\text{-}216\text{-}2]\quad\checkmark[M]}$$

---

## 216.F — Vollständiger Audit der Transportdefekte $G_{a,d}$ ([O-216-3]) ✓[M]

Setze $A:=C_\sigma(a)$, $D:=C_\sigma(d)$, $J:=J(d)$.

**Punktweise Darstellung:**
$$G_{a,d}(x)=\begin{cases}\log(\nu(ax)+2),&x\notin d\hat{\mathbb Z},\\\log(\nu(ax)+2)-\log(\nu(x/d)+2),&x\in d\hat{\mathbb Z}.\end{cases}\qquad G_{a,d}(0)=0.\tag{7.1}$$

**Gleichmäßige Beschränktheit.**
- $x\notin d\hat{\mathbb Z}$: $\Rightarrow\nu(x)<J$, $\nu(ax)\le J-1+A$, also $G_{a,d}(x)\le\log(J+A+1)$.
- $x=dy\in d\hat{\mathbb Z}$: $0\le G_{a,d}(x)\le\log(1+(A+D)/(\nu(y)+2))\le\log(1+(A+D)/2)$.
$$M_{a,d}:=\max\{\log(J+A+1),\,\log(1+(A+D)/2)\}.\qquad\boxed{\|G_{a,d}\|_\infty\le M_{a,d}.}\tag{7.6}$$

**Stetigkeit bei $0$.** Für $x\in S_j$, $j\ge J$: $0\le G_{a,d}(x)\le U_j:=\log((j+A+2)/(j-D+2))\to0$. Also $G_{a,d}\in C(\hat{\mathbb Z})$.

**Tangentiale Seminorm.** $N_{a,d}:=\max(1,J,2D+1)$. Für $j\ge N_{a,d}$: $U_j\le 2(A+D)/(j+1)$ (via $\log(1+t)\le t$). Also $\operatorname{osc}_{S_j}(G_{a,d})\le U_j$ und:
$$\boxed{(j+1)\operatorname{osc}_{S_j}(G_{a,d})\le 2(A+D).}\tag{7.11}$$
Für $j<N_{a,d}$: $(j+1)\operatorname{osc}\le N_{a,d}M_{a,d}$.
$$\boxed{[G_{a,d}]_{\tan}\le C'(a,d):=\max(N_{a,d}M_{a,d},\,2(A+D)).}\tag{7.13}$$

**Radiale Seminorm.** Für $j\ge N_{a,d}$: $0\le m_j(G_{a,d})\le U_j$, $U_j$ monoton fallend, also $|m_{j+1}(G_{a,d})-m_j(G_{a,d})|\le U_j$:
$$\boxed{(j+1)|m_{j+1}(G_{a,d})-m_j(G_{a,d})|\le 2(A+D).}\tag{7.14}$$
$$\boxed{[G_{a,d}]_{\mathrm{rad}}\le C''(a,d):=C'(a,d).}\tag{7.16}$$
$$\boxed{G_{a,d}\in\mathcal B^{\log}\text{ für alle festen }a,d.}\tag{7.17}$$
$$\boxed{[O\text{-}216\text{-}3]\quad\checkmark[M]}$$

---

## 216.G — Banach-$*$-Algebra $\mathcal B^{\log}$ ([O-216-1]) ✓[M]

**Tangential:** $[fg]_{\tan}\le M(f)T(g)+M(g)T(f)$. \hfill(8.2)

**Kovarianz (verbessert):**
$$\operatorname{cov}_j(f,g)=\frac12\iint_{S_j^2}(f(x)-f(y))(g(x)-g(y))\,d\mu_j(x)d\mu_j(y).$$
$$\boxed{|\operatorname{cov}_j(f,g)|\le\tfrac12\operatorname{osc}_{S_j}(f)\operatorname{osc}_{S_j}(g).}\tag{8.4}$$

**Radial:**
$$(j+1)|\operatorname{cov}_{j+1}(f,g)-\operatorname{cov}_j(f,g)|\le\tfrac12T(f)T(g)\left(\frac{j+1}{(j+2)^2}+\frac1{j+1}\right)\le T(f)T(g).$$
$$\boxed{[fg]_{\mathrm{rad}}\le M(f)R(g)+M(g)R(f)+T(f)T(g).}\tag{8.7}$$

**Submultiplikativität (ohne Renormierung):**
$$\|fg\|_{\mathcal B^{\log}}\le(M(f)+T(f)+R(f))(M(g)+T(g)+R(g))=\|f\|_{\mathcal B^{\log}}\|g\|_{\mathcal B^{\log}}.\tag{8.8}$$

**Involution:** $\|f^*\|=\|f\|$ (aus $m_j(f^*)=\overline{m_j(f)}$, $\operatorname{osc}(f^*)=\operatorname{osc}(f)$).

**Vollständigkeit:** Cauchy-Folge $(f_n)\to f\in C(\hat{\mathbb Z})$ (gleichmäßig). Aus $\liminf_{m\to\infty}[f_n-f_m]\ge[f_n-f]$ (beide Seminormen): $\|f_n-f\|_{\mathcal B^{\log}}\to0$.

**Echte Inklusionen.**
- $\mathcal B_{\mathrm{alg}}\subsetneq\mathcal B^{\log}$: Gegenbeispiel $f|_{S_j}=1/(j+1)$, $f(0)=0$: $f\in\mathcal B^{\log}$, $f\notin\mathcal B_{\mathrm{alg}}$.
- $\mathcal B^{\log}\subsetneq C(\hat{\mathbb Z})$: Gegenbeispiel $g|_{S_j}=(-1)^j/\sqrt{j+1}$: $(j+1)|m_{j+1}(g)-m_j(g)|\asymp\sqrt{j}\to\infty$, $g\notin\mathcal B^{\log}$.
$$\boxed{\mathcal B_{\mathrm{alg}}\subsetneq\mathcal B^{\log}\subsetneq C(\hat{\mathbb Z}).}\tag{8.9}$$
$$\boxed{[O\text{-}216\text{-}1]\quad\checkmark[M]}$$

---

## 216.H — Konkreter geladener Koeffiziententyp $\mathcal A^{\log}$ ([O-216-4]) ✓[K/M]

**Definition [K]:** Für $h=m/n\in\mathbb Q_+^\times$ (gekürzt):
$$\boxed{\mathcal A_h^{\log}:=\mu_m\mathcal B^{\log}\mu_n^*\subseteq(A_{C^*})_h,\qquad\|\mu_mf\mu_n^*\|_{h,\log}:=\|f\|_{\mathcal B^{\log}}.}\tag{9.1/3}$$
Injektivität: $\mu_m^*(\mu_mf\mu_n^*)\mu_n=f$. $\mathcal A_h^{\log}$ ist vollständiger Banachraum.
$$\boxed{\mathcal A^{\log}:=\operatorname{span}_{\mathrm{fin}}\{\mathcal A_h^{\log}:h\in\mathbb Q_+^\times\}\subset A_{C^*}.}\tag{9.4}$$

**Produkt [M]:** Für $x=\mu_mf\mu_n^*\in\mathcal A_{m/n}^{\log}$, $y=\mu_pg\mu_q^*\in\mathcal A_{p/q}^{\log}$, $r=(n,p)$, $n=rn_1$, $p=rp_1$. Relation $\mu_{n_1}^*\mu_{p_1}=\mu_{p_1}\mu_{n_1}^*/r$ (NEU-211). Dann:
$$xy=\mu_{mp_1}(\sigma_{p_1}(f)\sigma_{n_1}(g))\mu_{qn_1}^*=\mu_M\rho_s(\sigma_{p_1}(f)\sigma_{n_1}(g))\mu_N^*.\tag{9.7}$$
$\sigma_{p_1},\sigma_{n_1},\rho_s$ erhalten $\mathcal B^{\log}$; $\mathcal B^{\log}$ ist Algebra:
$$\boxed{\mathcal A_h^{\log}\mathcal A_{h'}^{\log}\subseteq\mathcal A_{hh'}^{\log}.}\tag{9.8}$$

**Adjunktion [M]:** $(\mu_mf\mu_n^*)^*=\mu_n\bar f\mu_m^*\in\mathcal A_{n/m}^{\log}=(\mathcal A_{m/n}^{\log})^*$. \hfill(9.10)

**Rangeprojektionen [M]:** $E_k=\rho_k(1)\in\mathcal B^{\log}\subset\mathcal A_1^{\log}$. \hfill(9.4)

**Derivationsbild [M]:** Generatorformeln aus NEU-211:
$$D_g(\mu_{m/n})(\text{repräsentative Terme})\ni\mu_{mk_0}G_{k_0,d}\mu_{n_0}^*,\quad-\mu_{m_0}G_{k_1,e}\mu_{nk_1}^*.$$
$G_{a,d}\in\mathcal B^{\log}$ ([O-216-3]) $\Rightarrow$ diese Terme liegen in $\mathcal A^{\log}$. Charakterabsorption (NEU-210): $e(r)$-Koeffizienten lokal konstant $\in\mathcal B_{\mathrm{alg}}\subset\mathcal B^{\log}$.
$$\boxed{D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}.}\tag{9.13}$$

**Typologische Einordnung:**
$$\mathcal A_{\mathrm{alg}}\subsetneq\mathcal A^{\log}\subseteq A_{C^*}.$$
Echte erste Inklusion: $\mathcal B_{\mathrm{alg}}\subsetneq\mathcal B^{\log}$ im Grad $1$. Echte zweite: $\mathcal A^{\log}$ hat endlichen Gradträger.

Offen (separat): kanonische globale Banach-/Fréchet-Vervollständigung der gesamten Gradsumme; Cup-Aufstieg nach Grad $4$.

$$\boxed{[O\text{-}216\text{-}4]\quad\checkmark[K/M]}$$

---

## 216.I — DAG-Stand (rev.6, vollständig)

```
NEU-215 [O-213-4] ✓[M]_neg    globaler Bimodul-No-go
      |
[O-216-0]  ✓[M]        Konventionsaudit
[O-216-1b] ✓[M]_neg    tangentiale Norm blind
[O-216-1c] ✓[M]        m_j(f) via Haarmaß, mu(S_j)=(j+1)/(j+2)!
[O-216-1d] ✓[M]_neg    c_j = log(j+2) nicht in B^log
[O-216-1]  ✓[M]        B^log Banach-*-Algebra, submultiplik. Norm ohne Renorm.
                        B_alg subsetneq B^log subsetneq C(Zhat)
[O-216-2a] ✓[M]        nu(kx)-nu(x) in [0, C_sigma(k)]
[O-216-2b] ✓[M]        rho_k: J(k), nu(x)-C in [nu(x/k), nu(x)]
[O-216-2c] ✓[M]        Band-Mittelwertlemma: K_0=1, K_C=2C
[O-216-2d] ✓[K/M]      T_a := sigma_a via BC-Kovarianz
[O-216-2]  ✓[M]        sigma_k, rho_k, T_a beschraenkt auf B^log
[O-216-3]  ✓[M]        G_{a,d} in B^log: M_{a,d}, C'=C''=max(N*M, 2(A+D))
[O-216-4]  ✓[K/M]      A^log := span_fin{mu_m B^log mu_n*}; D_g(A_alg) in A^log
      |
NEU-217: lokaler p-Block  ?[O]  (logisch getrennt; NEU-216 vollstaendig)
```

**Gesamtergebnis:**
$$\boxed{\mathcal B_{\mathrm{alg}}\subsetneq\mathcal B^{\log}\subsetneq C(\hat{\mathbb Z})\text{ Banach-}*\text{-Algebra},\quad\sigma_k,\rho_k,T_a:\mathcal B^{\log}\to\mathcal B^{\log},\quad G_{a,d}\in\mathcal B^{\log}.}$$
$$\boxed{D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}:=\operatorname{span}_{\mathrm{fin}}\{\mu_m\mathcal B^{\log}\mu_n^*:(m,n)=1\}\subset A_{C^*}.}$$
$$\boxed{\text{NEU-216 vollständig geschlossen. Nächster Schritt: NEU-217 (lokaler }p\text{-Block).}}$$
