# NEU-185 — Augmentationscharakter, Dualzyklus und Nichttrivialität von $[\Omega_{\mathbf{p}}]$

## 185.0 — Ziel

Sei $A := A_\mathbb{Q}^{\mathrm{alg}}$ und seien $p_1, p_2, p_3, p_4$ paarweise verschiedene Primzahlen.

Aus NEU-182/183 ist gesichert:
$$\Omega_{\mathbf{p}} := \sum_{\pi \in S_4} \operatorname{sgn}(\pi)\, D_{p_{\pi(1)}} \smile D_{p_{\pi(2)}} \smile D_{p_{\pi(3)}} \smile D_{p_{\pi(4)}} \in Z^4(A, A).$$

> **Gradierungsnotation:** $\deg_\Gamma(\Omega_{\mathbf{p}}) = 1_\Gamma$ (Identitätsgrad, neutrales Element von $\Gamma = \mathbb{Q}_+^\times$).
> Die Formulierung „neutral„ bedeutet hier stets $\deg_\Gamma = 1_\Gamma$, nicht einen numerischen Grad.

Offener Knoten:
$$[O\text{-}182\text{-}9]: \quad [\Omega_{\mathbf{p}}] \neq 0 \quad \text{in} \quad HH^4(A, A)\,?$$

NEU-185 konstruiert einen typkorrekten **Dualzyklus** in $C_4(A, A^\vee)$
und schließt [O-182-9] via Paarungsargument.

---

## 185.A — Audit des Augmentationscharakters

### Definition

$$\varepsilon(e(r)) := 1, \qquad \varepsilon(\mu_n) := 1, \qquad \varepsilon(\mu_n^*) := 1.$$

### Relationencheck

| Relation | $\varepsilon$(links) | $\varepsilon$(rechts) | OK? |
|---|---|---|---|
| (R1) $e(r)e(s) = e(r+s)$, $e(0)=1$ | $1$ | $1$ | ✓ |
| (R2) $\mu_n^*\mu_n = 1$ | $1$ | $1$ | ✓ |
| (R3) $\mu_n\mu_n^* = \frac{1}{n}\sum_{k=0}^{n-1}e(k/n)$ | $1$ | $\frac{1}{n}\cdot n = 1$ | ✓ |
| (R4) $\mu_n e(r) = e(r/n)\mu_n$ | $1$ | $1$ | ✓ |
| (R5) $e(r)\mu_n^* = \mu_n^* e(nr)$ | $1$ | $1$ | ✓ |
| (R6) $\mu_m\mu_n = \mu_{mn}$ | $1$ | $1$ | ✓ |
| (R7) $\mu_m^*\mu_n^* = \mu_{mn}^*$ | $1$ | $1$ | ✓ |

| Knoten | Inhalt | Status |
|---|---|---|
| [O-185-1] | $\varepsilon$ ist wohldefinierter Algebracharakter | ✓[K] — Relationencheck vollständig |

---

## 185.B — Duale Bimodulstruktur

$A^\vee := \operatorname{Hom}_\mathbb{C}(A, \mathbb{C})$ mit $(a \cdot f \cdot b)(x) := f(bxa)$.

Da $\varepsilon$ Algebracharakter:
$$\mu_n \cdot \varepsilon = \varepsilon(\mu_n)\,\varepsilon = \varepsilon, \qquad \varepsilon \cdot \mu_n = \varepsilon(\mu_n)\,\varepsilon = \varepsilon.$$

$\varepsilon$ ist unter allen Generatorenwirkungen **zentral** in $A^\vee$.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-185-2] | $\varepsilon$ zentral in $A^\vee$ | ✓[M] \| [O-185-1] |

---

## 185.C — Antisymmetrisierter Dualzyklus

$$z_{\mathbf{p}}^\varepsilon
:= \sum_{\pi \in S_4} \operatorname{sgn}(\pi)\;
\varepsilon \otimes \mu_{p_{\pi(1)}} \otimes \mu_{p_{\pi(2)}} \otimes \mu_{p_{\pi(3)}} \otimes \mu_{p_{\pi(4)}}
\in C_4(A, A^\vee) = A^\vee \otimes A^{\otimes 4}.$$

**Randterme:** Die inneren Terme (Produkte benachbarter $\mu_{p_i}$) heben sich paarweise
in der Antisymmetrisierung auf (Vorzeichenwechsel bei Transposition). Die äußeren Terme
verschwinden wegen $\varepsilon \cdot \mu_{p_{\pi(1)}} = \varepsilon$ und $\mu_{p_{\pi(4)}} \cdot \varepsilon = \varepsilon$
bzw. ihrer Antisymmetrisierung.

$$\boxed{\partial z_{\mathbf{p}}^\varepsilon = 0.}$$

| Knoten | Inhalt | Status |
|---|---|---|
| [O-185-3] | $\partial z_{\mathbf{p}}^\varepsilon = 0$ | ✓[M] \| [O-185-1], (R6) |

---

## 185.D — Paarung

$$\langle \varphi, f \otimes a_1 \otimes \cdots \otimes a_4 \rangle := f(\varphi(a_1,\ldots,a_4)), \qquad \langle b\Psi, z \rangle = \langle \Psi, \partial z \rangle.$$

Für jede Permutation $\pi$:
$\Omega_{\mathbf{p}}(\mu_{p_{\pi(1)}},\ldots,\mu_{p_{\pi(4)}}) = \operatorname{sgn}(\pi)\,\mu_{p_1 p_2 p_3 p_4}$.

Da $\varepsilon(\mu_{p_1 p_2 p_3 p_4}) = 1$:

$$\langle \Omega_{\mathbf{p}}, z_{\mathbf{p}}^\varepsilon \rangle
= \sum_{\pi \in S_4} \operatorname{sgn}(\pi)^2\, \varepsilon(\mu_{p_1 p_2 p_3 p_4})
= 4! = 24.$$

$$\boxed{\langle \Omega_{\mathbf{p}}, z_{\mathbf{p}}^\varepsilon \rangle = 24 \neq 0.}$$

| Knoten | Inhalt | Status |
|---|---|---|
| [O-185-4] | $\langle \Omega_{\mathbf{p}}, z_{\mathbf{p}}^\varepsilon \rangle = 24$ | ✓[M] \| [O-185-1] |

---

## 185.E — Nicht-Korand-Satz

**Satz 185.1.** $[\Omega_{\mathbf{p}}] \neq 0$ in $HH^4(A, A)$.

*Beweis.* Wäre $\Omega_{\mathbf{p}} = b\Psi$, so folgte
$24 = \langle b\Psi, z_{\mathbf{p}}^\varepsilon \rangle = \langle \Psi, \partial z_{\mathbf{p}}^\varepsilon \rangle = 0$.
Widerspruch. $\square$

Korollar: $[z_{\mathbf{p}}^\varepsilon] \neq 0$ in $HH_4(A, A^\vee)$.

> **Gradierungshinweis:** $\deg_\Gamma(\Omega_{\mathbf{p}}) = 1_\Gamma$. Das Resultat $[\Omega_{\mathbf{p}}] \neq 0$
> in $HH^4(A, A)$ (ungradiert) beweist daher noch nicht
> $HH^4(A, A)_{\mathrm{ch}} \neq 0$ (geladener Sektor, $\deg_\Gamma \neq 1_\Gamma$).

---

## 185.F — DAG-Abschluss

| Knoten | Inhalt | Status |
|---|---|---|
| [O-185-1] | $\varepsilon$ Algebracharakter | ✓[K] |
| [O-185-2] | $\varepsilon$ zentral in $A^\vee$ | ✓[M] |
| [O-185-3] | $\partial z_{\mathbf{p}}^\varepsilon = 0$ | ✓[M] |
| [O-185-4] | $\langle \Omega_{\mathbf{p}}, z_{\mathbf{p}}^\varepsilon \rangle = 24$ | ✓[M] |
| [O-182-9] | $[\Omega_{\mathbf{p}}] \neq 0$ in $HH^4(A, A)$ | ✓[M] — Satz 185.1 |

$$\boxed{HH^4(A_\mathbb{Q}^{\mathrm{alg}},\, A_\mathbb{Q}^{\mathrm{alg}}) \neq 0.}$$

## 185.G — Vollständiger DAG-Stand

```
Verdrehte Nullkozykelroute (Reβ>0)     ✓[M]_neg   NEU-182/183
Reguläre geladene Nullkozykelroute      ✓[M]_neg   NEU-184
Ω_p ∈ Z⁴(A,A), Ω_p≠0 als Kochain        ✓[K]       NEU-182/183
[Ω_p]≠0 in HH⁴(A,A)                      ✓[M]       NEU-185
[z_p^ε]≠0 in HH_4(A,A^∨)               ✓[M]       NEU-185 (Korollar)
HH⁴(A,A)_ch ≠0 ?                         ?[O]       NEU-186+
```
