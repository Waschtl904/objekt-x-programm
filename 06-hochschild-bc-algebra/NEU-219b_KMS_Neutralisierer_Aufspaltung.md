# NEU-219b — Expliziter KMS-Neutralisierer und Aufspaltung [O-219-5b]

**DAG-Position:** Nachfolger von NEU-219a (Commit 6a56047).  
**Voraussetzung:** Getwisteter Quotient $[A,M]_{\theta_\beta}$ etabliert ✓[K/M]; KMS-Negativbefund $\omega_\beta(\eta_{q,P})=0$ ✓[M]$_{\mathrm{neg}}$.

---

## 1. Expliziter neutralisierender Faktor

Schreibe wie bisher
$$
g = \frac{m}{n},\qquad P = p_1 p_2 p_3,\qquad H = \frac{mqP}{n},
$$
mit $q, p_1, p_2, p_3 \nmid mn$.

Der explizite Gegenfaktor ist
$$
\boxed{ a_0^{\mathrm{neu}} := \mu_n \mu_{mqP}^* \in (A_{\mathrm{alg}})_{H^{-1}}, }
$$
denn $\deg(a_0^{\mathrm{neu}}) = n/(mqP) = H^{-1}$.

---

## 2. Reduktion auf den diagonalen Wert

Die ausgezeichnete Auswertung von $L^{\mathrm{cup}}_{g;\mathbf{p}}$ ergibt:
$$
\Theta^\wedge_{p_1,p_2,p_3}(\mu_{p_1},\mu_{p_2},\mu_{p_3}) = \left(\prod_{i=1}^3 \log p_i\right)\mu_P.
$$

Daher:
$$
a_0^{\mathrm{neu}}\, L^{\mathrm{cup}}_{g;\mathbf{p}}(\mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3})
= \left(\prod_{i=1}^3 \log p_i\right) \mu_n \mu_{mqP}^* D_g(\mu_q)\mu_P.
$$

Mit der Normalform $D_g(\mu_q)\mu_P = \mu_{mqP}\,\sigma_P(G_q)\,\mu_n^*$ und $\mu_{mqP}^*\mu_{mqP} = 1$:

$$
\boxed{
a_0^{\mathrm{neu}}\, L^{\mathrm{cup}}_{g;\mathbf{p}}(\mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3})
= \left(\prod_{i=1}^3 \log p_i\right) \rho_n(\sigma_P(G_q)).
} \tag{1}
$$

wobei $\rho_n(F) := \mu_n F \mu_n^*$ die Kompressions-Einbettung bezeichnet.

Der Gesamtausdruck liegt in der **neutralen Komponente** $(A_{C^*})_1$; die frühere Gewichtsauslöschung greift nicht mehr.

---

## 3. KMS-Auswertung

Für die Bost–Connes-Zeitwirkung gilt $\alpha_{i\beta}(\mu_n) = n^{-\beta}\mu_n$. Daher für diagonales $F$:
$$
\omega_\beta(\rho_n(F))
= \omega_\beta(\mu_n F \mu_n^*)
= \omega_\beta\!\left( F\mu_n^* \alpha_{i\beta}(\mu_n) \right)
= n^{-\beta}\,\omega_\beta(F).
$$

Die ausgezeichnete KMS-Auswertung reduziert sich damit exakt auf:

$$
\boxed{
\Phi_\beta\!\left( a_0^{\mathrm{neu}}, \mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3} \right)
= n^{-\beta} \left(\prod_{i=1}^3 \log p_i\right) \omega_\beta\!\left( \sigma_P(G_q) \right).
} \tag{2}
$$

Der erste konkrete Nichtverschwindensknoten des KMS-Pfades ist daher:

$$
\boxed{ [O\text{-}219\text{-}5b\text{-NV}]: \quad \omega_\beta(\sigma_P(G_q)) \neq 0
\text{ für mindestens einen geeigneten KMS-Zustand?} \quad ?[O]. }
$$

---

## 4. Aufspaltung von [O-219-5b] in atomare Knoten

### [O-219-5b1] — Expliziter Neutralisierer und Reduktion

**Status:** ✓[K/M]

Der explizite Gegenfaktor $a_0^{\mathrm{neu}} = \mu_n\mu_{mqP}^*$ ist konstruiert. Die Reduktionen (1) und (2) sind vollständig berechnet.

$$\boxed{ [O\text{-}219\text{-}5b1] \quad \checkmark[K/M]. }$$

### [O-219-5b2] — Diagonale KMS-Auswertung

**Status:** ?[O] — primärer nächster Knoten

$$
\boxed{ \omega_\beta(\sigma_P(G_q)) \neq 0 \quad ?[O]. }
$$

Hier ist $G_q \in B^{\log}$ ein konkretes beschränktes Element von $A_{C^*}$, und $\sigma_P$ wirkt stabil auf $B^{\log}$. Zu entscheiden ist, ob für mindestens einen der bekannten extremalen KMS$_\beta$-Zustände ($\beta > 1$) der Wert $\omega_\beta(\sigma_P(G_q)) \neq 0$.

**Struktur der Entscheidung:** Die extremalen KMS-Zustände bei $\beta > 1$ sind durch Gibbs-Maße auf $\widehat{\mathbb{Z}}$ gegeben:
$$
\omega_\beta^{(\chi)}(f) = \frac{1}{\zeta(\beta)} \sum_{n=1}^\infty n^{-\beta} f(\chi/n),
\qquad \chi \in \widehat{\mathbb{Z}}^\times,
$$
wobei die Summe über $n$ und $f$ als Funktion auf $\widehat{\mathbb{Z}}$ aufgefasst wird.

Für $\sigma_P(G_q)$ lautet die Auswertung:
$$
\omega_\beta^{(\chi)}(\sigma_P(G_q)) = \frac{1}{\zeta(\beta)} \sum_{n=1}^\infty n^{-\beta} G_q(Pn\chi).
$$

Mittels der punktweisen Formel $G_q(x) = c_{\nu(qx)} - c_{\nu(x)} = \mathscr{X}(qx) - \mathscr{X}(x)$ für $x \neq 0$ und der Standardabschätzungen aus NEU-218 (Abschnitte 5–8) ist zu prüfen, ob diese Reihe für geeignete $\chi$ von null verschieden und konvergent ist.

**Strategische Priorität:** Scheitert [O-219-5b2] für alle BC-KMS-Zustände, ist der KMS-Zeuge trotz korrekter Gradkompensation ausgeschlossen. Gelingt er für einen Zustand, steht ein expliziter nichtverschwindender neutraler Testwert bereit.

### [O-219-5b3] — Getwisteter Hochschildrand

**Status:** ?[O] (bedingt durch [O-219-5b2])

$$
\boxed{ b_{\theta_\beta}\Phi_\beta = 0 \quad ?[O]. }
$$

Zu prüfen: Mit dem getwisteten Rand
$$
(b_{\theta_\beta}f)(a_0, \ldots, a_n)
:= \sum_{i=0}^{n-1}(-1)^i f(\ldots, a_i a_{i+1}, \ldots)
+ (-1)^n f(\theta_\beta(a_n)a_0, a_1, \ldots, a_{n-1})
$$
gilt $b_{\theta_\beta}\Phi_\beta = 0$ genau dann, wenn $\omega_\beta$ mit der getwisteten Algebramultiplikation verträglich ist. Dies folgt aus der KMS-Gleichung selbst, sofern $L^{\mathrm{cup}}_{g;\mathbf{p}}$ ein Hochschild-Kozykel ist (was aus NEU-218 bekannt ist), und $\omega_\beta$ auf der Normalform korrekt zieht. Formale Verifikation ausstehend.

### [O-219-5b4] — Getwistete zyklische Rotation

**Status:** ?[O] (bedingt durch [O-219-5b2])

$$
\boxed{ \lambda_{\theta_\beta}\Phi_\beta = \Phi_\beta \quad ?[O]. }
$$

Der getwistete Zyklizitätsoperator:
$$
(\lambda_{\theta_\beta}f)(a_0, \ldots, a_n)
:= (-1)^n f(\theta_\beta(a_n), a_0, \ldots, a_{n-1}).
$$

Für Grad-$n$-Kochains auf homogenen Elementen mit Gesamtgrad 1 ergibt der Twist einen zusätzlichen Faktor $\deg(a_n)^{-\beta}$. Die Zyklizitätsfrage hängt davon ab, ob dieser Faktor durch die KMS-Gewichte von $\omega_\beta$ kompensiert wird.

---

## 5. Revidierter DAG (KMS-Pfad vollständig)

```
[O-219-5a]  getwisteter Quotient [A,M]_{theta_beta}       [K/M]
      |
[O-219-5b1] a0_neu = mu_n*mu_{mqP}^*, Reduktionen (1)(2)  [K/M]
      |
[O-219-5b2] omega_beta(sigma_P(G_q)) != 0                 ?[O]  PRIMAER
      |
      +-- falls positiv:
      |       |
      |  [O-219-5b3]  b_{theta_beta} Phi_beta = 0          ?[O]
      |       |
      |  [O-219-5b4]  lambda_{theta_beta} Phi_beta = Phi_beta ?[O]
      |
      +-- falls negativ:
              Kein KMS-Zeuge; Pfad (B) geschlossen.
              Rueckfall auf Pfad (A): [O-219-1] via Struktur/Foelner.
```

---

## 6. Gesamtstatustabelle (Update)

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-1] | $\eta_{q,P} \notin [A,M]$ (voller Quotient) | ?[O] primär Pfad A |
| [O-219-1a-KMS] | $\omega_\beta(\eta_{q,P})=0$ | ✓[M]$_{\mathrm{neg}}$ |
| [O-219-5a] | Getwisteter Quotient $[A,M]_{\theta_\beta}$ | ✓[K/M] |
| **[O-219-5b1]** | $a_0^{\mathrm{neu}}$, Reduktion (1)(2) | **✓[K/M]** |
| [O-219-5b2] | $\omega_\beta(\sigma_P(G_q)) \neq 0$ | ?[O] primär Pfad B |
| [O-219-5b3] | $b_{\theta_\beta}\Phi_\beta = 0$ | ?[O] bedingt |
| [O-219-5b4] | $\lambda_{\theta_\beta}\Phi_\beta = \Phi_\beta$ | ?[O] bedingt |

---

**Primärer nächster Audit:** [O-219-5b2] — diagonale KMS-Auswertung $\omega_\beta(\sigma_P(G_q)) \stackrel{?}{\neq} 0$.
