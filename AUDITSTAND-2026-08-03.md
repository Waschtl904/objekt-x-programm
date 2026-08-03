# Auditstand 2026-08-03 — Verbindliches Kontrollblatt

> **Dieses Blatt ist die kanonische Eingangsschnittstelle für jede neue Entwurfsdatei
> im HH-Strang (06-hochschild-bc-algebra).**
> Vollständige Belege: ARCHIV-AUDIT-NEU210.md, ARCHIV-AUDIT-NEU211.md, ARCHIV-AUDIT-NEU212.md.

---

## VERWENDBARE RESULTATE

| Knoten | Aussage | Status |
|---|---|---|
| [O-210-1] | $Z_g = \{0\}$ für $g \neq 1$ — exakt bewiesen via Pontrjagin/Torfreiheit | ✓[M] |
| [O-210-2] | Faktoriales Potential $X_N$, $\operatorname{Sing}(X) = \{0\}$ | ✓[K/M] |
| [O-210-3] | $\mu_k$-Kommutatoren: $\lim_N [X_N, \mu_k] = \mu_k B_k$ in Norm, **nur für $j \geq k$** | ✓[M]_part |
| [O-210-4a] | $M(0)=0 \Rightarrow MX_N$ schließlich exakt konstant | ✓[M] |
| [O-211-1] | Nichtteilerfremde Nica-/gcd-Formeln exakt | ✓[M] |
| [O-211-2] | $G_{a,d;N} \to G_{a,d}$ in Norm | ✓[M] |
| [O-211-3corr] | Korrekte Charakterwirkung: $D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r} \mu_n^*$ | ✓[M] |
| [O-211-4corr] | Nichtinnerheit via Offdiagonaltest: $c_{\nu(t)} \to \infty$ | ✓[M] |
| [O-charged-HH1-analytic] | $[D_g^{\mathrm{corr}}] \neq 0$ in $HH^1(A_{\mathrm{alg}}, A_{C^*})_g$ | **✓[M]** |
| [O-212-1a] | Neutraler nichtunitaler Schnellabfallraum $\mathcal S_0$ | ✓[K/M] |
| [O-212-char] | Korrigierter Charakterkoeffizient $C_{m,n;r}$ hat endlichen Schalenträger und liegt in $\mathcal S_0$ | ✓[M] |
| [O-212-4a] | Offdiagonal-Divergenzbeweis der Log-Regularisierung ausgeschlossen | ✓[M]_neg |

---

## NICHT VERWENDBARE BEHAUPTUNGEN

| Knoten | Falsche Aussage | Ersetzt durch |
|---|---|---|
| [O-209-6c] | $M_{g,r} X_N \to 0$ in Norm | [O-209-6d]: schließlich konstant ✓[M] |
| [O-210-4b] | $M_{g,r} X_N \to 0$ | [O-210-4a]: schließlich konstant ✓[M] |
| [O-211-3] geschrieben | $D_g(e(r)) := 0$ | $D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r} \mu_n^*$ |
| [O-211-4] geschrieben | Nichtinnerheitsschluss auf Basis $D_g(e(r))=0$ | Schluss gilt für $D_g^{\mathrm{corr}}$ ✓[M] |
| [O-212-1] geschrieben | $A_{\mathrm{alg}}\subseteq \mathcal A^\infty$ | widerlegt: $1,e(r)\notin\mathcal B^\infty$ |
| [O-212-2] | $\widetilde G_{a,d}\in\mathcal B^\infty$ nach Tail/Log-Regularisierung | widerlegt: nur $O(1/(j\log j))$ |
| [O-212-3] | $\widetilde D_g(e(r)):=0$ definiert eine Derivation | widerlegt: verletzt BC-Kreuzrelation |
| [O-212-3HH] | $[\widetilde D_g]\in HH^1(A_{\mathrm{alg}},\mathcal A^\infty)_g$ | bedeutungslos, da keine Derivation |
| Bandformel ohne Einschränkung | $P_j \leq T_k(P_j) \leq P_{j-k}$ für alle $j$ | Gilt **nur für $j \geq k$** |
| NEU-222 §0 Klammersatz | [O-209-6] vollständig geschlossen | [O-209-6c] ×[M]; [O-209-6d] ✓[M] |

---

## OFFENE BEWEISPFLICHTEN (HH-Strang)

| Knoten | Inhalt |
|---|---|
| [O-211-6] | Intermediäres Koeffizientenmodul / Zieltypbrücke bleibt vollständig offen |
| [O-charged-HH1-algebraic] | Geladene Klasse in $HH^1(A_{\mathrm{alg}}, A_{\mathrm{alg}})_g$ |
| [O-212-5] | Cup-Brücke: typkorrekte Koeffizientenmultiplikation, HH³-Partner, Nichtexaktheit |
| NEU-216 bis NEU-222 re-audit | Kompatibilität von $D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r} \mu_n^*$ mit Log-Koeffiziententyp, Cup-Produkt und Vierkozykel |

---

## AUDITPFAD (zu bearbeiten)

```text
NEU-216 → NEU-217 → NEU-218 → NEU-222
```

NEU-212 ist nun abgeschlossen und negativ verbucht. Jede Folgedatei muss prüfen: Ist die korrigierte Charakterwirkung
$D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r} \mu_n^*$ mit dem jeweiligen Koeffizientenmodul,
dem Cup-Produkt und dem behaupteten Vierkozykel kompatibel?

---

## PARALLELE FORSCHUNGSBAHN (unberührt vom Charakterfehler)

- NEU-57 / alternativer Vergleichsoperator für HP-2 (Konfinement)
- Regulierte Mangoldt-Spur im kritischen Streifen $0 < \Re\beta \leq 1$
- Hebungsabstieg und zyklisches Tripel (NEU-221e)

---

*Erstellt: 2026-08-03 · Basis: ARCHIV-AUDIT-NEU210.md, ARCHIV-AUDIT-NEU211.md, ARCHIV-AUDIT-NEU212.md*
*Letzte Aktualisierung: nach Abschluss Direktaudit NEU-212*
