# NEU-219 Blockaudit I — KMS- und Twist-Triage

**Quelldateien:** NEU-219a bis NEU-219g (vollständig gelesen 2026-08-04)  
**Gesamtstatus Block I:** $\checkmark[M]$ für alle abgeschlossenen Teilstrecken; struktureller Engpass: Ladungsobstruktion.

---

## 1. Entscheidungstabelle Block I

| Route | Endstatus | Begründung |
|-------|-----------|------------|
| Gewöhnlicher BC-KMS-Zustand als direkter Detektor | $\checkmark[M]_{\mathrm{neg}}$ | $\omega_\beta(\eta_{q,P})=0$ wegen $H=gqP\neq 1$, $\beta>0$ |
| Expliziter Neutralisierer $a_0^{\mathrm{neu}}$, Reduktion | $\checkmark[K/M]$ | NEU-219b: $\Phi_{\beta,\chi}(a_0^{\mathrm{neu}},\mu_q,\ldots)=n^{-\beta}(\prod\log p_i)\omega_\beta(\sigma_P(G_q))$ |
| Diagonale KMS-Auswertung $\omega_{\beta,\chi}(\sigma_P(G_q))>0$ | $\checkmark[M]$ | NEU-219c: $G_q\ge 0$, strikter Summand für $k=L_J/(Pq)$ |
| Getwisteter Hochschildrand $b^{\sigma_\beta}\Phi_{\beta,\chi}=0$ | $\checkmark[K/M]$ | NEU-219d: folgt aus $bL=0$ und KMS-Identität in $\sigma_\beta$-Orientierung |
| Falsche Orientierung $b^{\theta_\beta}\Phi=0$ | $\checkmark[M]_{\mathrm{neg}}$ | NEU-219d: Faktor $(h^\beta-h^{-\beta})a_5\neq 0$ |
| Standard-getwistete Zyklizität $\lambda_{\sigma_\beta}\Phi=\Phi$ | $\checkmark[M]_{\mathrm{neg}}$ | NEU-219d: $T_{\sigma_\beta}\Phi=g^{-\beta}\Phi\neq\Phi$ wegen $g\neq 1$ |
| Externe $\mathbb{Z}$-Eigenlinie $E_{g,\beta}$ (formale $T$-Kompensation) | $\checkmark[K]$ | NEU-219e: konstruiert, aber keine zyklische Theorie |
| Unitales $\sigma_\beta$-äquivariantes $A_{\mathrm{alg}}$-Bimodul dim 1 | $\checkmark[M]_{\mathrm{neg}}$ | NEU-219e: $k^\beta=1$ für $k\ge2$, $\beta>0$ unmöglich |
| Gewöhnliche Zyklisierung $w=g^{-\beta}\neq 1$ Eigenraum | $\checkmark[M]_{\mathrm{neg}}$ | NEU-219f: $[\Phi]_{\mathrm{zyklisiert}}=0$ |
| $g^{-\beta}$-Gewichtsunterkomplex als para-Buchführung | $\checkmark[K/M]$ | NEU-219f: wohldefinierter $b^{\sigma_\beta}$-Unterkomplex |
| $\mathcal{H}_\Gamma=\mathbb{C}[\mathbb{Q}_+^\times]$-Modulalgebra kanonisch | $\checkmark[M]_{\mathrm{neg}}$ | NEU-219g: Gradierung liefert nur Komodul, keine Wirkung |
| $\mathcal{H}_\beta=\mathbb{C}[\mathbb{Z}]$ wirkt durch $\sigma_\beta$ | $\checkmark[K/M]$ | NEU-219g: typkorrekte minimale Hopf-Modulalgebra |
| Abstrakte 1-dim. SAYD-Linien über $\mathcal{H}_\beta$ | $\checkmark[K/M]$ | NEU-219g: vorhanden für $c^r=1$ |
| SAYD: KMS-Twist **und** Ladung $g\neq 1$ gleichzeitig | $\checkmark[M]_{\mathrm{neg}}$ | NEU-219g: SAYD-Stabilität $c=1$ vs. Ladungskompensation $c=g^{-\beta}$ |

---

## 2. Struktureller Befund

Der KMS-Zweig etabliert eine konkrete, universell positive, gradkompensierte Funffachauswertung und einen gültigen getwisteten Hochschildrand. Er scheitert ausschließlich an einer **einzigen wiederholten Ladungsobstruktion**: $T_{\sigma_\beta}\Phi = g^{-\beta}\Phi \neq \Phi$.

Dieses Hindernis erscheint in drei äquivalenten Formulierungen:
- Zyklizitätsoperator: $\lambda^{n+1}\Phi = g^{-\beta}\Phi \neq \Phi$
- Para-/zyklisches Modell: $w$-Eigenraum mit $w\neq 1$ wird zyklisch annihiliert
- Hopf-SAYD: Stabilitätsbedingung und Ladungscharakter kollidieren

$$
\boxed{
\text{Strukturelle Ladungsobstruktion: }
T_{\sigma_\beta}\Phi_{\beta,\chi} = g^{-\beta}\Phi_{\beta,\chi}.
\text{ Alle Standardwege beseitigen sie nicht.}
}
$$

---

## 3. Offene Primärknoten nach Block I

| Knoten | Inhalt | Pfad | Status |
|--------|--------|------|--------|
| $[O\text{-}219\text{-}5d3]$ | Nichtstandardmäßiger $A$-relativer Hopf-Koeffizient | Hopf-relativ | $?[O]$ |
| $[O\text{-}219\text{-}5e1]$ | Dilatationsalgebra mit invertierbarem $u_g$ | Crossed-Product | $?[O]$ **primär** |
| $[O\text{-}219\text{-}1]$ | $\eta_{q,P}\notin[A,M]$ (voller Quotient) | gewöhnlich | $?[O]$ |

---

## 4. Revidierter DAG (Block I konsolidiert)

```
NEU-219a:  omega_beta(eta_{q,P}) = 0 wegen H != 1                [M]_neg
NEU-219b:  Neutralisierer a0_neu, Reduktion Phi = n^{-beta}*...  [K/M]
NEU-219c:  omega_beta(sigma_P(G_q)) > 0 fuer alle beta>1, chi    [M]
NEU-219d:  b^{sigma_beta} Phi = 0 (sigma = theta^{-1})           [K/M]
           T_{sigma_beta} Phi = g^{-beta} Phi != Phi              [M]_neg
NEU-219e:  externe Eigenlinie E_{g,beta}                          [K]
           unitales A-Bimodul dim 1                               [M]_neg
NEU-219f:  g^{-beta}-Gewichtsunterkomplex                        [K/M]
           Zyklisierung w!=1 -> [Phi]=0                           [M]_neg
NEU-219g:  H_beta = C[Z] Modulalgebra                            [K/M]
           SAYD: KMS-Twist + Ladung g gleichzeitig                [M]_neg
              (Stabilität c=1 vs. Ladung c=g^{-beta})
             |
             +-- [O-219-5d3] A-relativer Hopf-Koeffizient        ?[O]
             |
             +-- [O-219-5e1] Dilatationsalgebra, u_g             ?[O] PRIMAER
                              -> Block III/IV
```

---

## 5. Buchungsposten

$$
\boxed{
\Phi_{\beta,\chi}\in Z^4_{\sigma_\beta,\mathrm{Hoch}}(A_{\mathrm{alg}}),\quad
\Phi_{\beta,\chi}\neq 0,\quad
\Phi_{\beta,\chi}\notin Z^4_{\sigma_\beta,\lambda}(A_{\mathrm{alg}})\;(g\neq 1).
}
$$

Der strukturell stärkste verbleibende Pfad zur Beseitigung der Ladungsobstruktion ist die **Dilatationsalgebra** mit invertibarem $u_g$ ($[O\text{-}219\text{-}5e1]$), die in Block II (adelisch/Morita) und Block III (kanonischer Basislift) weiterverfolgt wird. Der SAYD-Pfad reformuliert die Ladungsobstruktion, beseitigt sie aber nicht.

---

**Erstellt:** 2026-08-04  
**Nächster Block:** Block II — `NEU-219h` bis `NEU-219n` (Dilatation, Laca-Abgleich, adelischer Lift, Morita)
