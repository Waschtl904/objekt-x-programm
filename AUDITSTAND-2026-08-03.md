# Auditstand 2026-08-04 — Verbindliches Kontrollblatt

> **Dieses Blatt ist die kanonische Eingangsschnittstelle für jede neue Entwurfsdatei
> im HH-Strang (06-hochschild-bc-algebra).**
> Vollständige Belege: ARCHIV-AUDIT-NEU210.md, ARCHIV-AUDIT-NEU211.md,
> ARCHIV-AUDIT-NEU212.md, ARCHIV-AUDIT-NEU216.md.

---

## VERWENDBARE RESULTATE

| Knoten | Aussage | Status |
|---|---|---|
| [O-210-1] | $Z_g = \{0\}$ für $g \neq 1$ — exakt bewiesen | ✓[M] |
| [O-210-2] | Faktoriales Potential $X_N$, $\operatorname{Sing}(X) = \{0\}$ | ✓[K/M] |
| [O-210-3] | $\mu_k$-Kommutatoren in Norm, **nur für $j \geq k$** | ✓[M]_part |
| [O-210-4a] | $M(0)=0 \Rightarrow MX_N$ schließlich exakt konstant | ✓[M] |
| [O-211-1] | Nichtteilerfremde Nica-/gcd-Formeln exakt | ✓[M] |
| [O-211-2] | $G_{a,d;N} \to G_{a,d}$ in Norm | ✓[M] |
| [O-211-3corr] | $D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r} \mu_n^*$ | ✓[M] |
| [O-211-4corr] | Nichtinnerheit via Offdiagonaltest: $c_{\nu(t)} \to \infty$ | ✓[M] |
| [O-charged-HH1-analytic] | $[D_g^{\mathrm{corr}}] \neq 0$ in $HH^1(A_{\mathrm{alg}}, A_{C^*})_g$ | **✓[M]** |
| [O-212-1a] | Neutraler nichtunitaler Schnellabfallraum $\mathcal S_0$ | ✓[K/M] |
| [O-212-char] | $C_{m,n;r}$ hat endlichen Schalenträger, liegt in $\mathcal S_0$ | ✓[M] |
| [O-212-4a] | Offdiagonal-Divergenzbeweis der Log-Regularisierung ausgeschlossen | ✓[M]_neg |
| [O-216-1] | $\mathcal B_{\mathrm{alg}} \subsetneq \mathcal B^{\log} \subsetneq C(\widehat{\mathbb Z})$; unitale Banach-$*$-Algebra | ✓[M] |
| [O-216-2] | $\sigma_k, \rho_k, T_a = \sigma_a$ erhalten $\mathcal B^{\log}$ | ✓[M] |
| [O-216-3] | $G_{a,d} \in \mathcal B^{\log}$ | ✓[M] |
| [O-216-4a] | $\mathcal A^{\log} = \bigoplus_h^{\mathrm{alg}} \mu_m \mathcal B^{\log} \mu_n^*$; graduierte algebraische $*$-Algebra | ✓[K/M] |
| [O-216-4b] | $D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \subseteq \mathcal A^{\log}$ | **✓[M]** |
| [O-216-4c] | $[D_g^{\mathrm{corr}}] \neq 0$ in $HH^1(A_{\mathrm{alg}}, \mathcal A^{\log})_g$ | **✓[M]** |
| **[O-211-6a]** | **Zieltypbrücke algebraisch geschlossen** | **✓[M]** |

---

## NICHT VERWENDBARE BEHAUPTUNGEN

| Knoten | Falsche Aussage | Ersetzt durch |
|---|---|---|
| [O-209-6c] | $M_{g,r} X_N \to 0$ in Norm | [O-209-6d]: schließlich konstant ✓[M] |
| [O-210-4b] | $M_{g,r} X_N \to 0$ | [O-210-4a]: schließlich konstant ✓[M] |
| [O-211-3] geschrieben | $D_g(e(r)) := 0$ | $D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r} \mu_n^*$ |
| [O-212-1] geschrieben | $A_{\mathrm{alg}} \subseteq \mathcal A^\infty$ | widerlegt: $1, e(r) \notin \mathcal B^\infty$ |
| [O-212-2] | Log-Regularisierung in $\mathcal B^\infty$ | widerlegt: nur $O(1/(j\log j))$ |
| [O-212-3] | $\widetilde D_g(e(r)) := 0$ ist Derivation | widerlegt: BC-Kreuzrelation verletzt |
| NEU-216 gcd-Relation | $\mu_{n_1}^*\mu_{p_1} = \mu_{p_1}\mu_{n_1}^*/r$ | kein Faktor $1/r$: $\mu_n^*\mu_p = \mu_{p_1}\mu_{n_1}^*$ |
| NEU-222 §0 | [O-209-6] vollständig geschlossen | [O-209-6c] ×[M]; [O-209-6d] ✓[M] |

---

## KANONISCHE DEFINITIONEN ($\mathcal B^{\log}$)

Diese Definitionen sind verbindlich für alle HH-Entwurfsdateien ab NEU-217.

$$L_j = (j+1)!, \quad P_j = 1_{L_j\widehat{\mathbb Z}}, \quad S_j = L_j\widehat{\mathbb Z}\setminus L_{j+1}\widehat{\mathbb Z}$$

$$\nu(x) = \max\{j : (j+1)! \mid x\} \quad (x\neq0), \qquad C_\sigma(1)=0$$

$$m_j(f) = \int_{S_j} f\,d\mu_j, \qquad [f]_{\tan} = \sup_{j}(j+1)\operatorname{osc}_{S_j}(f), \qquad [f]_{\mathrm{rad}} = \sup_j(j+1)|m_{j+1}(f)-m_j(f)|$$

$$|f|_{\mathcal B^{\log}} = |f|_\infty + [f]_{\tan} + [f]_{\mathrm{rad}}$$

**Korrekte Produktformel** mit $r=(n,p), n=rn_1, p=rp_1, (n_1,p_1)=1$:
$$\mu_n^*\mu_p = \mu_{p_1}\mu_{n_1}^* \qquad \text{(kein Faktor }1/r)$$

$$s=(mp_1,qn_1),\quad M=mp_1/s,\quad N=qn_1/s,\quad (\mu_mf\mu_n^*)(\mu_pg\mu_q^*) = \mu_M\rho_s(\sigma_{p_1}(f)\sigma_{n_1}(g))\mu_N^*$$

---

## OFFENE BEWEISPFLICHTEN (HH-Strang)

| Knoten | Inhalt |
|---|---|
| [O-charged-HH1-algebraic] | Geladene Klasse in $HH^1(A_{\mathrm{alg}}, A_{\mathrm{alg}})_g$ |
| [O-211-6] topologisch | Globale Banach-/Fréchet-Topologie auf $\mathcal A^{\log}$ als Ganzes |
| [O-216-top] | Kontinuierlicher Hochschildkomplex mit $\mathcal A^{\log}$ |
| [O-216-cup] | Grad-3-Partner $\Theta$, Cup-Kozykel $D_g^{\mathrm{corr}}\smile\Theta$, Nichtexaktheit |
| NEU-217 bis NEU-222 re-audit | Kompatibilität mit $D_g^{\mathrm{corr}}$ und $\mathcal B^{\log}$ prüfen |

---

## AUDITPFAD (zu bearbeiten)

```text
NEU-217 (Lokaler p-Block) → NEU-217 (O217-2b) → NEU-217 (O217-2c6) → NEU-218 → NEU-222
```

Bei jedem Knoten zu prüfen:
1. Wird $D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r}\mu_n^*$ korrekt verwendet?
2. Ist der Koeffizientenraum ein $\mathcal B^{\log}$-kompatibler $A_{\mathrm{alg}}$-Bimodul?
3. Wird bereits ein Grad-3-Partner oder Cup-Produkt behauptet?

---

## PARALLELE FORSCHUNGSBAHN

- NEU-57 / alternativer Vergleichsoperator für HP-2 (Konfinement)
- Regulierte Mangoldt-Spur im kritischen Streifen $0 < \Re\beta \leq 1$
- Hebungsabstieg und zyklisches Tripel (NEU-221e)

---

*Letzte Aktualisierung: 2026-08-04 · nach Direktaudit NEU-216*  
*Basis: ARCHIV-AUDIT-NEU210 – NEU212, ARCHIV-AUDIT-NEU216*
