# NEU-215 rev.4 — Zentralisatorbeweis und globaler Bimodul-No-go

**Status:** [O-215-0] ✓[M]_neg,Quelle; [O-215-1] ✓[M]; [O-215-B1] ✓[M]; [O-215-B2] ✓[M]; [O-215-B3] ✓[M]; [O-215-2]=[O-214-2] ✓[M]; [O-215-3]=[O-214-3] ✓[M]; [O-213-4] ✓[M]_neg  
**Erstellt:** 2026-07-21 (rev.4)  
**Revisionen:** rev.1: Einfachheitsfehler. rev.2: Treuelücke. rev.3: MASA vollständig. rev.4: B2-Relationsverwechslung $\rho_k\leftrightarrow\sigma_k$ korrigiert.  
**Vorgänger:** NEU-214 rev.2  
**Schließt:** [O-214-2] ✓[M], [O-214-3] ✓[M], [O-213-4] ✓[M]_neg

---

## 215.0 — Quellenfehler (aus rev.1/rev.2 übernommen)

$A_{C^*}$ ist **nicht einfach** (Laca–Raeburn 1996, nichttrivialer primitiver Idealraum; Takeishi). Der Schluss $\pi\neq 0 \Rightarrow \pi$ treu ist daher unzulässig.

$$\boxed{[O\text{-}215\text{-}0] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}$$

**Typfehler in Weg A (rev.2) dokumentiert.** Der Quotient $\mathbb Q_+^\times/\hat{\mathbb Z}^\times$ ist nicht definiert ($\hat{\mathbb Z}^\times \not\subseteq \mathbb Q_+^\times$). Die korrekte Eckbasisidentifikation lautet $p\,\ell^2(\mathbb Q_+^\times) = \ell^2(\mathbb N^\times)$ via $v_p(q)\ge 0$ $\forall p$ $\Leftrightarrow$ $q\in\mathbb N^\times$. Weg A ist nicht nötig, da Weg B kürzer ist.

---

## 215.A — Reduktion auf das Zentrum

**Lemma.** $\operatorname{Cent}_{A_{C^*}}(A_{\mathrm{alg}}) = Z(A_{C^*})$.

**Beweis.** Da $A_{\mathrm{alg}}$ normdicht in $A_{C^*}$ ist: Für $x\in A_{C^*}$ mit $[x,a]=0$ $\forall a\in A_{\mathrm{alg}}$ und $b\in A_{C^*}$, wähle $a_n\to b$; dann $[x,b]=\lim_n[x,a_n]=0$. $\square$

Es genügt daher $Z(A_{C^*})=\mathbb C\cdot 1$ zu beweisen.

---

## 215.B — MASA-Eigenschaft von $C(\hat{\mathbb Z})\subset A_{C^*}$

**Satz (B1).** *$B_{C^*}=C(\hat{\mathbb Z})$ ist eine MASA in $A_{C^*}$.*

**Beweis.**

**Schritt (i) — Topologische Freiheit.** Für $q\in\mathbb Q_+^\times$, $q\neq 1$:
$$\{x\in\mathbb A_f : qx=x\} = \{x:(q-1)x=0\} = \{0\},$$
da $q-1\neq 0$ in $\mathbb Q$ und damit keine offene Teilmenge von $\mathbb A_f$ punktweise fixiert wird. Die Wirkung ist topologisch frei.

**Schritt (ii) — MASA im Kreuzprodukt.** Nach dem Standardsatz für topologisch freie Wirkungen amenabler Gruppen (Archbold–Spielberg; Pedersen \S 7.8): Ist $\alpha: G\curvearrowright C_0(X)$ topologisch frei mit $G$ amenabel, dann ist $C_0(X)$ eine MASA im reduzierten Kreuzprodukt. Da $\mathbb Q_+^\times$ abelsch (amenabel) ist, gilt volles = reduziertes Kreuzprodukt, und $C_0(\mathbb A_f)$ ist MASA in $C_0(\mathbb A_f)\rtimes\mathbb Q_+^\times$.

**Schritt (iii) — Eckpunktübertragung.** $A_{C^*}\cong p(C_0(\mathbb A_f)\rtimes\mathbb Q_+^\times)p$ (Laca–Raeburn 1996, Thm. 2.2). Ist $D\subseteq C$ eine MASA und $p\in D$ eine Projektion, so ist $pDp$ eine MASA in $pCp$ (elementar: jedes $pcp$ mit $[pcp,pDp]=0$ liegt in $D'\cap C=D$, also $pcp\in pDp$). Mit $D=C_0(\mathbb A_f)$, $pDp\cong C(\hat{\mathbb Z})$: $C(\hat{\mathbb Z})$ ist MASA in $A_{C^*}$. $\square$

$$\boxed{[O\text{-}215\text{-}B1] \quad \checkmark[M]}$$

---

## 215.C — Multiplikationsinvarianz (B2, korrigiert rev.4)

**Begriffsklarstellung.** In der BC-Algebra gibt es zwei verschiedene Endomorphismen des abelschen Sektors:
$$\rho_k(f) := \mu_k f\mu_k^*, \qquad \rho_k(1) = \mu_k\mu_k^* = E_k \neq 1 \quad (k>1),$$
$$\sigma_k(f) := \mu_k^* f\mu_k, \qquad \sigma_k(1) = \mu_k^*\mu_k = 1.$$
In Fourierform auf $C(\hat{\mathbb Z})$: $(\sigma_k f)(x) = f(kx)$. Diese beiden Abbildungen sind verschieden; $\rho_k$ ist kein unitärer Automorphismus, $\sigma_k$ schon.

**Lemma (B2).** *Sei $f\in C(\hat{\mathbb Z})$ mit $[f,\mu_k]=0$ in $A_{C^*}$. Dann $\sigma_k(f)=f$, d.h. $f(kx)=f(x)$ für alle $x\in\hat{\mathbb Z}$.*

**Beweis.** Aus $f\mu_k = \mu_k f$ multipliziere links mit $\mu_k^*$:
$$\mu_k^* f\mu_k = \mu_k^*\mu_k f = 1\cdot f = f.$$
Da $\mu_k^* f\mu_k = \sigma_k(f)$ und $(\sigma_k f)(x) = f(kx)$:
$$\boxed{f(kx) = f(x) \qquad \forall\, k\in\mathbb N^\times,\; x\in\hat{\mathbb Z}.} \tag{215.B2}$$
$\square$

$$\boxed{[O\text{-}215\text{-}B2] \quad \checkmark[M]}$$

---

## 215.D — Konstanz durch Faktorialkonvergenz (B3)

**Lemma (B3).** *Sei $f\in C(\hat{\mathbb Z})$ mit $f(kx)=f(x)$ für alle $k\in\mathbb N^\times$, $x\in\hat{\mathbb Z}$. Dann $f\equiv f(0)$.*

**Beweis.** Setze $k=j!$. Für jedes feste $y\in\hat{\mathbb Z}$:
$$v_p(j!\cdot y) \ge v_p(j!) \to \infty \quad (j\to\infty) \quad \forall\, p,$$
also $j!\cdot y\to 0$ in $\hat{\mathbb Z}$. Aus der Multiplikationsinvarianz und Stetigkeit:
$$f(y) = f(j!\cdot y) \xrightarrow{j\to\infty} f(0).$$
Also $f(y)=f(0)$ für alle $y$. $\square$

$$\boxed{[O\text{-}215\text{-}B3] \quad \checkmark[M]}$$

---

## 215.E — Zentralisatorsatz (vollständig)

**Satz ([O-215-2]=[O-214-2]).**
$$\boxed{\operatorname{Cent}_{A_{C^*}}(A_{\mathrm{alg}}) = Z(A_{C^*}) = \mathbb C\cdot 1.} \tag{215.10}$$

**Beweis.** Sei $x\in Z(A_{C^*})$. Da $C(\hat{\mathbb Z})$ MASA ist (B1): $x\in C(\hat{\mathbb Z})$, schreibe $x=f$. Aus $[f,\mu_k]=0$ folgt $f(kx)=f(x)$ (B2). Dann $f\equiv f(0)$ (B3). Also $x=f(0)\cdot 1\in\mathbb C\cdot 1$. $\square$

$$\boxed{[O\text{-}215\text{-}2] = [O\text{-}214\text{-}2] \quad \checkmark[M]}$$

---

## 215.F — Globaler Bimodul-No-go (vollständig, verschärft)

**Satz ([O-215-3]=[O-214-3]).** *Sei $\mathcal A^\infty\subsetneq A_{C^*}$ ein echter Teilraum mit $1\in\mathcal A^\infty$, und $R:A_{C^*}\to\mathcal A^\infty$ ein normstetiger $A_{\mathrm{alg}}$-Bimoduloperator. Dann $R=0$.*

**Beweis.** Nach [O-214-1]: $R(a)=ar$ mit $r=R(1)\in\operatorname{Cent}_{A_{C^*}}(A_{\mathrm{alg}})=\mathbb C\cdot 1$ (215.E). Also $r=\lambda\cdot 1$, $R=\lambda\,\mathrm{id}$ auf $A_{C^*}$. Für $\lambda\neq 0$: $R(A_{C^*})=A_{C^*}\subseteq\mathcal A^\infty$, Widerspruch. Also $\lambda=0$. $\square$

$$\boxed{R:A_{C^*}\to\mathcal A^\infty\subsetneq A_{C^*}\text{ stetiger globaler }A_{\mathrm{alg}}\text{-Bimoduloperator}\Longrightarrow R=0.} \tag{215.11}$$

$$\boxed{[O\text{-}215\text{-}3]=[O\text{-}214\text{-}3] \quad \checkmark[M]}$$
$$\boxed{[O\text{-}213\text{-}4] \quad \checkmark[M]_{\mathrm{neg}}}$$

---

## 215.G — Strukturbilanz (rev.4)

| Knoten | Status | Inhalt |
|---|---|---|
| [O-215-0] | ✓[M]_neg,Quelle | $A_{C^*}$ nicht einfach; Einfachheitsargument unzulässig |
| [O-215-1] | ✓[M] | Matrixbeweis: $\pi(\operatorname{Cent})\subseteq\mathbb C I$ (Diagonalität + Konstanz) |
| [O-215-B1] | ✓[M] | MASA: topol. freie $\mathbb Q_+^\times$-Wirkung, Amenabilität, Eckpunktübertragung |
| [O-215-B2] | ✓[M] | $[f,\mu_k]=0\Rightarrow\mu_k^*f\mu_k=f\Rightarrow f(kx)=f(x)$ (korrekte Relation $\sigma_k$) |
| [O-215-B3] | ✓[M] | $j!\cdot y\to 0\Rightarrow f(y)=f(0)$, keine Darstellung nötig |
| [O-215-2]=[O-214-2] | ✓[M] | $Z(A_{C^*})=\operatorname{Cent}_{A_{C^*}}(A_{\mathrm{alg}})=\mathbb C\cdot 1$ |
| [O-215-3]=[O-214-3] | ✓[M] | $R:A_{C^*}\to\mathcal A^\infty\Rightarrow R=0$ |
| [O-213-4] | ✓[M]_neg | Globales Bimodul-No-go vollständig |

---

## 215.H — DAG-Stand (rev.4)

```
[O-215-0] ✓[M]_neg,Quelle   A_C* nicht einfach

Weg B (vollständig):
  Cent_{A_C*}(A_alg) = Z(A_C*)          [Dichte, 215.A]
      |
  [B1] MASA: topol. freie Q_+^x-Wirkung, Amenabilität
      => x = f ∈ C(Z^)
      |
  [B2] [f,mu_k]=0 => mu_k* f mu_k = mu_k* mu_k f = f
      => sigma_k(f)=f, f(kx)=f(x)
      |
  [B3] j!*y->0 in Z^ => f(y)=f(0)
      |
  [O-215-2] ✓[M]    Z(A_C*) = C·1  <== [O-214-2] ✓[M]
      |
  [O-215-3] ✓[M]    R=0  <== [O-214-3] ✓[M]
      |
  [O-213-4] ✓[M]_neg   No-go vollständig

─── Offene Front ───
[O-214-4b] ?[O]   Nichtinnerheitskriterium ohne c_j→∞
[NEU-216]  ?      B^log/A^log: G_{a,d} ∈ B^log direkt
```

**Zentrales Ergebnis (rev.4):**

$$\boxed{[f,\mu_k]=0 \Longrightarrow \mu_k^*f\mu_k = f \Longrightarrow f(kx)=f(x) \Longrightarrow f\equiv f(0).}$$
$$\boxed{Z(A_{C^*})=\mathbb C\cdot 1 \quad \text{(MASA + }\sigma_k\text{-Invarianz + Faktorialkonvergenz).}}$$
$$\boxed{R:A_{C^*}\to\mathcal A^\infty\subsetneq A_{C^*}\text{ stetiger globaler }A_{\mathrm{alg}}\text{-Bimoduloperator}\Longrightarrow R=0.}$$
$$\boxed{\text{Nächstes Ziel: }\mathcal B^{\log}\text{ und }G_{a,d}\in\mathcal B^{\log}\text{ (NEU-216).}}$$
