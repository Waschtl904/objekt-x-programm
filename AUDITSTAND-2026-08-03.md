# Auditstand 2026-08-04 — Verbindliches Kontrollblatt

> **Dieses Blatt ist die kanonische Eingangsschnittstelle für jede neue Entwurfsdatei
> im HH-Strang (06-hochschild-bc-algebra).**
> Vollständige Belege: ARCHIV-AUDIT-NEU210–212, ARCHIV-AUDIT-NEU216, ARCHIV-AUDIT-NEU217.

---

## VERWENDBARE RESULTATE

| Knoten | Aussage | Status |
|---|---|---|
| [O-210-1] | $Z_g = \{0\}$ für $g \neq 1$ | ✓[M] |
| [O-210-2] | Faktoriales Potential $X_N$, $\operatorname{Sing}(X) = \{0\}$ | ✓[K/M] |
| [O-210-3] | $\mu_k$-Kommutatoren in Norm, **nur für $j \geq k$** | ✓[M]_part |
| [O-210-4a] | $M(0)=0 \Rightarrow MX_N$ schließlich konstant | ✓[M] |
| [O-211-1] | Nichtteilerfremde Nica-/gcd-Formeln | ✓[M] |
| [O-211-2] | $G_{a,d;N} \to G_{a,d}$ in Norm | ✓[M] |
| [O-211-3corr] | $D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r} \mu_n^*$ | ✓[M] |
| [O-211-4corr] | Nichtinnerheit via Offdiagonaltest | ✓[M] |
| [O-charged-HH1-analytic] | $[D_g^{\mathrm{corr}}] \neq 0$ in $HH^1(A_{\mathrm{alg}}, A_{C^*})_g$ | **✓[M]** |
| [O-212-1a] | Neutraler nichtunitaler Schnellabfallraum $\mathcal S_0$ | ✓[K/M] |
| [O-212-char] | $C_{m,n;r}$ hat endlichen Schalenträger | ✓[M] |
| [O-216-1] | $\mathcal B_{\mathrm{alg}} \subsetneq \mathcal B^{\log} \subsetneq C(\widehat{\mathbb Z})$; unitale Banach-$*$-Algebra | ✓[M] |
| [O-216-2] | $\sigma_k, \rho_k, T_a$ erhalten $\mathcal B^{\log}$ | ✓[M] |
| [O-216-3] | $G_{a,d} \in \mathcal B^{\log}$ | ✓[M] |
| [O-216-4a] | $\mathcal A^{\log}$ graduierte algebraische $*$-Algebra | ✓[K/M] |
| [O-216-4b] | $D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \subseteq \mathcal A^{\log}$ | **✓[M]** |
| [O-216-4c] | $[D_g^{\mathrm{corr}}] \neq 0$ in $HH^1(A_{\mathrm{alg}}, \mathcal A^{\log})_g$ | **✓[M]** |
| **[O-211-6a]** | **Zieltypbrücke algebraisch geschlossen** | **✓[M]** |
| [O-217-2b-1--4] | gcd-Fallzerlegung auf $\mu_{p^r}, \mu_{p^r}^*$ | ✓[M] |
| [O-217-2c-2/3] | Lokale Transportidentitäten (mit $r\ge1$ bei $\sigma_p(E_{p^r})$) | ✓[M] |
| [O-217-2c-6b-stab] | Globale Schnittstabilität von $M_{\mathrm{glob}}^{\log}$ | ✓[M] |
| [O-217-2c-6c] | $D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \subseteq (\mathfrak M_{\mathrm{glob}}^{\log})_g$ | **✓[M]** |
| **[O-217-2c-6d]** | **$[D_g^{\mathrm{corr}}]\neq0$ in $HH^1(A_{\mathrm{alg}},\mathfrak M_{\mathrm{glob}}^{\log})_g$** | **✓[M]** |
| lokale Nichtinnerheit | $[D_g^{\mathrm{corr}}\vert_{A_{(p)}}]\neq0$ in $HH^1(A_{(p),\mathrm{alg}},A_{C^*})_g$ | ✓[M] |

---

## NICHT VERWENDBARE BEHAUPTUNGEN

| Knoten | Falsche Aussage | Ersetzt durch |
|---|---|---|
| [O-209-6c] | $M_{g,r} X_N \to 0$ | [O-209-6d] ✓[M] |
| [O-211-3] geschrieben | $D_g(e(r)) := 0$ | $D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r} \mu_n^*$ |
| [O-212-1] | $A_{\mathrm{alg}} \subseteq \mathcal A^\infty$ | widerlegt |
| [O-212-2] | Log-Regularisierung in $\mathcal B^\infty$ | widerlegt |
| [O-212-3] | $\widetilde D_g(e(r)):=0$ ist Derivation | widerlegt |
| NEU-216 gcd mit $1/r$ | $\mu_{n_1}^*\mu_{p_1}=\mu_{p_1}\mu_{n_1}^*/r$ | kein Faktor $1/r$ |
| NEU-217 Gaugegen. | $\delta_p^{(0)}$ ist infin. Generator und $*$-Derivation | nur $(1/i)\partial_p$; $\partial_p=i\delta_p^{(0)}$ ist der Generator |
| Formel (G1) | $G_{nk/\delta,d/\delta}$ | $G_{nk,d/\delta}$ (erster Index ist $nk$) |
| lokale $Z^1/HH^1$ mit $M_{g,p}^{\log}$ | $D_g\vert_{A_{(p)}}\in Z^1(A_{(p)},M_{g,p}^{\log})$ | nicht typisiert |
| NEU-222 \S0 | [O-209-6] vollst. geschlossen | [O-209-6c] ×[M] |

---

## KANONISCHE DEFINITIONEN ($\mathcal B^{\log}$)

$$L_j=(j+1)!,\quad P_j=1_{L_j\widehat{\mathbb Z}},\quad S_j=L_j\widehat{\mathbb Z}\setminus L_{j+1}\widehat{\mathbb Z}$$

$$\nu(x)=\max\{j:(j+1)!\mid x\}\;(x\neq0),\qquad C_\sigma(1)=0$$

$$m_j(f)=\int_{S_j}f\,d\mu_j,\quad [f]_{\tan}=\sup_j(j+1)\operatorname{osc}_{S_j}(f),\quad [f]_{\mathrm{rad}}=\sup_j(j+1)|m_{j+1}(f)-m_j(f)|$$

$$|f|_{\mathcal B^{\log}}=|f|_\infty+[f]_{\tan}+[f]_{\mathrm{rad}}$$

**Korrekte gcd-Relation** ($r=(n,p), n=rn_1, p=rp_1, (n_1,p_1)=1$): $\mu_n^*\mu_p=\mu_{p_1}\mu_{n_1}^*$ (kein $1/r$).

**Korrekte Produktformel**: $s=(mp_1,qn_1),\ M=mp_1/s,\ N=qn_1/s,\ (\mu_mf\mu_n^*)(\mu_pg\mu_q^*)=\mu_M\rho_s(\sigma_{p_1}(f)\sigma_{n_1}(g))\mu_N^*$.

**Globaler Bimodul**: $\mathfrak M_{\mathrm{glob}}^{\log}=\overline{\operatorname{span}_{\mathrm{fin}}\{a\xi b:a,b\in A_{\mathrm{alg}},\xi\in M_{\mathrm{glob}}^{\log}\}}\subseteq\mathcal A^{\log}$.

---

## OFFENE BEWEISPFLICHTEN (HH-Strang)

| Knoten | Inhalt |
|---|---|
| [O-217-1d] | Trennende Darstellungsfamilie oder Gauge-Eindeutigkeitssatz |
| [O-217-2b-5] | $V$-$\Delta$-Faktorisierung typisieren |
| [O-217-2c-5land] | Charakterwerte in lokaler Regimetabelle; volle $A_{(p),\mathrm{alg}}$-Bimodulstruktur von $M_{g,p}^{\log}$ |
| [O-216-top] / [O-211-6] topol. | Globale Banach-/Fréchet-Topologie auf $\mathcal A^{\log}$ |
| [O-216-cup] | Grad-3-Partner, Cup-Kozykel, Nichtexaktheit in $HH^4$ |

---

## AUDITPFAD (zu bearbeiten)

```text
NEU-218 (Grad3-Cup-Aufstieg) → NEU-218 (Abschluss) → NEU-222
```

Bei NEU-218 zu prüfen:
1. Konkreter Grad-3-Kozykel $\Theta_3$ und sein Koeffizientenbimodul
2. Hochschildrand $b\Theta_3=0$ vollständig?
3. Cup-Produkt $D_g^{\mathrm{corr}}\smile\Theta_3$ typkorrekt?
4. Multiplikation $\mathfrak M_{\mathrm{glob}}^{\log}\otimes_{A_{\mathrm{alg}}}N\to M_4$?
5. Nichtexaktheit in $HH^4$ oder nur Nichtverschwindung?
6. Import der falschen Charakterwirkung oder untypisierten lokalen Klasse?

---

## PARALLELE FORSCHUNGSBAHN

- NEU-57 / Vergleichsoperator HP-2 (Konfinement)
- Mangoldt-Spur im kritischen Streifen $0<\Re\beta\le1$
- Hebungsabstieg / zyklisches Tripel (NEU-221e)

---

*Letzte Aktualisierung: 2026-08-04 · nach Direktaudit NEU-217-Block*
