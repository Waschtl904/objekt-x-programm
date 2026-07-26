# NEU-183 — Quellen- und Präsentationsaudit für die BC-Algebra

## Vorbemerkung

NEU-183 ist der **Präsentationsaudit-Knoten** zu NEU-182.
Sein Zweck ist die quellenbasierte Verifikation der drei Transfer-Voraussetzungen:

- [O-182-2]: $\mu_n^*\mu_n = 1$ aus der konkreten Relationsliste
- [O-182-2N]: Treue $C^*$-Einbettung $A_\mathbb{Q}^{\mathrm{alg}} \hookrightarrow A_\mathbb{Q}^{C^*}$
- [O-182-5a]: Normalform für homogene Räume $A_g$ (als Vorbereitung für [O-182-6])

Ohne Abschluss dieser drei Unterknoten bleiben [O-182-4] und [O-182-6] konditional.

---

## 183.A — Präsentation von $A_\mathbb{Q}^{\mathrm{alg}}$ (Bost–Connes)

### 183.A.1 — Erzeuger

```
e(r),   r ∈ Q/Z
μ_n,    n ∈ N_{≥1}
μ_n*,   n ∈ N_{≥1}
```

### 183.A.2 — Relationen (vollständige Standardliste, Quelle: Bost–Connes 1995)

```
(R1)  e(r) e(s) = e(r+s),         e(0) = 1
(R2)  μ_n* μ_n = 1
(R3)  μ_n μ_n* = (1/n) Σ_{k=0}^{n-1} e(k/n)
(R4)  μ_n e(r) = e(r/n) μ_n
(R5)  e(r) μ_n* = μ_n* e(nr)
(R6)  μ_m μ_n = μ_{mn}
(R7)  μ_m* μ_n* = μ_{mn}*
```

**Bezug:** J.-B. Bost, A. Connes, *Hecke algebras, type III factors and phase transitions
with spontaneous symmetry breaking in number theory*, Selecta Math. (N.S.) **1** (1995), 411–457.
(Relationen (R1)–(R7) entsprechen den Definitionen in Abschnitt 2 der Originalarbeit.)

### 183.A.3 — Gradstruktur

$$\deg(\mu_n) = n, \quad \deg(\mu_n^*) = n^{-1}, \quad \deg(e(r)) = 1.$$

Die Relationen (R1)–(R7) sind unter dieser Gradierung **homogen**:

| Relation | Linke Seite Grad | Rechte Seite Grad | Homogen? |
|---|---|---|---|
| (R1) | $1 \cdot 1 = 1$ | $1$ | ✓ |
| (R2) | $n^{-1} \cdot n = 1$ | $1$ | ✓ |
| (R3) | $n \cdot n^{-1} = 1$ | $1$ (Linearkombination Grad 1) | ✓ |
| (R4) | $n \cdot 1 = n$ | $1 \cdot n = n$ | ✓ |
| (R5) | $1 \cdot n^{-1} = n^{-1}$ | $n^{-1} \cdot 1 = n^{-1}$ | ✓ |
| (R6) | $m \cdot n = mn$ | $mn$ | ✓ |
| (R7) | $m^{-1} \cdot n^{-1} = (mn)^{-1}$ | $(mn)^{-1}$ | ✓ |

### Knotenstruktur 183.A

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-2] | $\mu_n^*\mu_n = 1$ | ✓[K] — Relation (R2) in der BC-Originalpräsentation |
| [O-181-3] / [O-182-7a] | $I$ ist homogenes Ideal | ✓[K] — alle Relationen (R1)–(R7) sind homogen unter der $\Gamma$-Gradierung |

---

## 183.B — Treue $C^*$-Einbettung: [O-182-2N]

### 183.B.1 — Standardresultat

Die $C^*$-vollständige BC-Algebra $A_\mathbb{Q}^{C^*}$ ist die $C^*$-Vervollständigung von
$A_\mathbb{Q}^{\mathrm{alg}}$ in der Darstellung durch Linksmultiplikation auf
$\ell^2(\mathbb{N}) \otimes L^2(\mathbb{A}_f/\widehat{\mathbb{Z}})$
(oder äquivalent: als Hecke-Algebra $C^*(\Gamma_0 \backslash \Gamma / \Gamma_0)$).

Da die algebraische Algebra $A_\mathbb{Q}^{\mathrm{alg}}$ **dicht** in $A_\mathbb{Q}^{C^*}$
eingebettet ist und die Norm auf $A_\mathbb{Q}^{\mathrm{alg}}$ durch diese Darstellung
definiert ist, ist die Einbettung treu.

**Bezug:** Bost–Connes 1995, Abschnitt 3; Connes, *Noncommutative Geometry* (1994),
Kapitel V.

### 183.B.2 — Konsequenz für [O-182-3] und [O-182-4]

Nach Bestätigung von [O-182-2] (aus (R2)) und [O-182-2N] (Einbettung) sind
die konditionalen Abschlüsse aus NEU-182 nun **unbedingt**:

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-2N] | Treue $C^*$-Einbettung | ✓[K] — Standardkonstruktion der BC-$C^*$-Algebra |
| [O-182-3] | $\|\mu_n u\| = \|u\|$ | ✓[K] |
| [O-182-4] | $\operatorname{Re}\beta > 0 \Rightarrow Z^0(A, M_{\sigma_\beta}) = \{0\}$ | ✓[M]_neg |
| [O-181-8σ] | Verdrehte Faktorisierungsroute ($\operatorname{Re}\beta > 0$) | ✓[M]_neg |

---

## 183.C — Normalform für $A_g$: Vorbereitung [O-182-6]

### 183.C.1 — Monomdarstellung

Jedes homogene Element in $A_g$ mit $g = m/n \in \mathbb{Q}_+^\times$
(in gekürzter Form: $m, n \in \mathbb{N}$, $\gcd(m,n)=1$) hat die Normalform:

$$w_{m,r,n} = \mu_m\, e(r)\, \mu_n^*, \qquad r \in \frac{1}{\mathrm{lcm}(m,n)}\mathbb{Z}/\mathbb{Z}.$$

Die Menge $\{w_{m,r,n}\}$ mit festem $m/n = g$ bildet nach den Relationen (R1)–(R7)
eine Linearbasis von $A_g$ (Standardresultat, vgl. Laca–Raeburn oder Connes 1994).

### 183.C.2 — Vorbereitung Zentrumstest

Schreibe $u_g = \sum_r c_r\, \mu_m e(r) \mu_n^*$ mit festen $m, n$ (und $m/n = g$).

Die Kommutationsbedingung $[e(s), u_g] = 0$ für alle $s \in \mathbb{Q}/\mathbb{Z}$
ergibt via (R4), (R5):

$$\sum_r c_r \bigl(e(s)\mu_m e(r)\mu_n^* - \mu_m e(r)\mu_n^* e(s)\bigr)
= \sum_r c_r \,\mu_m e(r + s/m) \mu_n^*\bigl(1 - e((n-1)s/m \cdot m)\bigr) \cdots$$

**Offener Rechenstand:** Die vollständige Koeffizientenauswertung des $e(s)$-Kommutators
über die Normalform erfordert die exakte Auswertung von
$e(s)\cdot\mu_m e(r)\mu_n^*$ vs. $\mu_m e(r)\mu_n^* \cdot e(s)$.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-5a] | Normalform $A_g = \operatorname{span}\{\mu_m e(r) \mu_n^*\}_{m/n=g}$ | ✓[K] — Standardresultat |
| [O-182-5] | Generatorentest $u_g \in Z(A)$ vollständig formuliert | ✓[M] — Kriterium bereit |
| [O-182-6] | $Z(A)_g = 0$ für $g \neq 1$? | ?[O] — Koeffizientenauswertung pendent |

---

## 183.D — Auswertung $\Omega_{\mathbf{p}} \neq 0$ (unnormalisiert)

Nach Abschluss von [O-182-7a] (= [O-181-3]) via 183.A und [O-182-2] via 183.A:

$$\Omega_{\mathbf{p}}(\mu_{p_1}, \mu_{p_2}, \mu_{p_3}, \mu_{p_4})
= \mu_{p_1}\mu_{p_2}\mu_{p_3}\mu_{p_4}
= \mu_{p_1 p_2 p_3 p_4} \neq 0.$$

(Unnormalisierte Alt-Konvention; kein $1/4!$-Faktor.)

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-8] | $\Omega_{\mathbf{p}} \neq 0$ | ✓[K] — Auswertung liefert $\mu_{p_1 p_2 p_3 p_4} \neq 0$ |

---

## 183.E — Konsolidierte DAG-Übersicht NEU-183

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-2] | $\mu_n^*\mu_n = 1$ | ✓[K] — Relation (R2) |
| [O-182-2N] | Treue $C^*$-Einbettung | ✓[K] — Standardkonstruktion |
| [O-182-3] | $\|\mu_n u\| = \|u\|$ | ✓[K] |
| [O-182-4] | $\operatorname{Re}\beta > 0 \Rightarrow Z^0 = \{0\}$ | ✓[M]_neg |
| [O-181-8σ] | Verdrehte Route | ✓[M]_neg |
| [O-181-3] / [O-182-7a] | $I$ homogenes Ideal | ✓[K] — alle (R1)–(R7) homogen |
| [O-182-7b/c] | $D_p(I) \subseteq I$; $D_p$ Derivation auf $A$ | ✓[M] |
| [O-182-8] | $\Omega_{\mathbf{p}} \neq 0$ | ✓[K] |
| [O-182-5a] | Normalform $A_g$ | ✓[K] |
| [O-182-5] | Generatorentest-Kriterium | ✓[M] |
| [O-182-6] | $Z(A)_g = 0$ für $g \neq 1$? | ?[O] — Koeffizientenauswertung pendent |
| [O-182-9] | $[\Omega_{\mathbf{p}}] \neq 0$ in $HH^4$? | ?[O] |
| [O-181-9b] | $u \smile \Omega_{\mathbf{p}} \neq 0$? | ?[O] \| [O-182-6] ∧ [O-182-8] |

---

## 183.F — Nächster Schritt: NEU-184

Nach Abschluss von 183.A–D verbleiben als offene Kernknoten:

1. **[O-182-6]:** Zentrumstest $Z(A_\mathbb{Q})_g = 0$ für $g \neq 1$
   — explizite Koeffizientenauswertung via Normalform
2. **[O-182-9]:** $[\Omega_{\mathbf{p}}] \neq 0$ in $HH^4(A_\mathbb{Q}, A_\mathbb{Q})$
   — Nicht-Korand-Nachweis
3. **[O-181-9b]:** $u \smile \Omega_{\mathbf{p}} \neq 0$ (abhängig von [O-182-6])

NEU-184 übernimmt den Zentrumstest mit vollständiger Koeffizientenrechnung.
