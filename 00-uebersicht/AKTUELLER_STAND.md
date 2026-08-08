# Aktueller Stand — 2026-08-08 (Audit-Update)

---

## SYN-Audit-Regel

$$\text{NEU-Serie}\to\text{SYN-Entwurf}\to\text{SYN-Direktaudit}\to\text{kanonische Tagesreferenz.}$$

| Manuskript | Audit-Status |
|---|---|
| P01 | Entwurf (ausstehend) |
| P02 | $\checkmark$ SYN-Audit 2026-08-08 |
| P03 | $\checkmark$ SYN-Audit 2026-08-08 |
| P04 | $\checkmark$ SYN-Audit 2026-08-08 (in Arbeit) |

---

## Synthese-Manuskripte (papers/)

| ID | Titel | Status | Quellknoten |
|---|---|---|---|
| **P01** | BC Prime Power Weights | Entwurf (P01-Audit ausstehend) | NEU-250b–j |
| **P02** | Adelic Weil Amplitude Port | $\checkmark$ SYN-Audit | NEU-250n–r, 252 |
| **P03** | Haar-$L^2$ Firewall | $\checkmark$ SYN-Audit | NEU-253–258 |
| **P04** | Finite Weil Geometry | $\checkmark$ SYN-Audit (in Arbeit) | NEU-259–260b.1 |

---

## Aktive Forschungsfront

| Knoten | Titel | Status |
|---|---|---|
| NEU-260a | $\lambda$-Gauge-Audit | $\checkmark[K/M]$ (Patch 2 fertig) |
| NEU-260b | $\theta$-Selektionsaudit | $\checkmark[K/M]$ (Parity $\to\mathbb{Z}_2$) |
| **NEU-260b.1** | $\mathbb{Z}_2$-Selektion $\varepsilon(a)$ | $?[O]$ **höchste Priorität** |
| NEU-260c | Grenznormalisierung $\phi(a,z)$ | $?[O]$ |
| NEU-260d | $J_{a,b}$-Geometrie | $?[O]$ |

---

## Offene Fragen (priorisiert)

1. **Höchste Priorität (NEU-260b.1): $\mathbb{Z}_2$-Selektionsproblem.**  
   $\varepsilon(a)\in\{+1,-1\}$: Stetigkeit in $a$ $\Rightarrow$ $\varepsilon=\mathrm{const}$?  
   BC/KMS-Zeitpfeil oder Frobenius-Orientierung $\Rightarrow$ $\varepsilon=+1$?

2. **NEU-260c:** $\phi(a,z)\equiv 0$ beweisbar?

3. **NEU-260d:** Adelische $J_{a,b}$ mit Intertwining $J_{a,b}\overline{\mathscr{D}}_{a,\theta(a)}\subset\overline{\mathscr{D}}_{b,\theta(b)}J_{a,b}$?

4. ~~$Q_W^a$-Spiegelungssymmetrie $\Rightarrow\theta_{\rm can}=0$?~~ **veraltet** (durch NEU-260b ersetzt)

---

## Hart gebuchte Resultate (vollständige Liste)

$$W_{\rm NEU\text{-}252}=W_{\rm Lit}\quad\checkmark[K/M]\quad\text{(NEU-258)}$$
$$B_W\text{ semibeschränkt auf }C_c^\infty(\mathbb{R})\text{ rel. }L^2(du)\Leftrightarrow\text{RH}\quad\checkmark[K/M]\quad\text{(NEU-257)}$$
$$B_W\text{ nicht abschließbar auf }L^2(du)\text{ unter RH (}\mu_W\not\ll du\text{)}\quad\checkmark[K/M]\quad\text{(NEU-257)}$$
$$\text{KLMN auf }L^2(\mathbb{R}):\;\times[M]\quad\text{(NEU-257)}$$
$$\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\text{ unter RH}\quad\checkmark[K/M]\quad\text{(NEU-257, Suzuki 2025)}$$
$$Q_W^a\text{ semibeschränkt, abschließbar auf }L^2(-a,a)\quad\checkmark[K/M]\quad\text{(NEU-259)}$$
$$A_a=A_a^*,\text{ diskretes Spektrum, }\lambda_a\text{ stetig in }a\quad\checkmark[K/M]\quad\text{(NEU-259)}$$
$$\lambda_{\rm can}(a)=\lambda_a-1\text{ (bequeme Konvention, nicht einzig möglich; }\lambda=0\text{ RH-konditional)}\quad\checkmark[K/M]\quad\text{(NEU-260a)}$$
$$\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})\quad\checkmark[K/M]\quad\text{(NEU-260a)}$$
$$\theta\text{-Gauge-Freiheit: }\theta\mapsto\theta+\beta-\alpha\quad\checkmark[K/M]\quad\text{(NEU-260b)}$$
$$U_a:\mathcal{N}_{+,a}\to\mathcal{N}_{-,a}\text{ intrinsisches Datum; }\mathcal{N}_{\pm}=\operatorname{span}\{v_\pm\},\;T_av_\pm=e^{\pm x}\quad\checkmark[K/M]\quad\text{(NEU-260b)}$$
$$PA_a=A_aP\quad\checkmark[M]/\text{Suzuki 2026}$$
$$P:\mathcal{H}(T_a)\to\mathcal{H}(T_a)\text{ unitär; }Pv_+=v_-\quad\checkmark[K/M]\quad\text{(NEU-260b)}$$
$$\boxed{U(1)\xrightarrow{\text{Weil-Parität}}\{+P,-P\}\cong\mathbb{Z}_2}\quad\checkmark[K/M]\quad\text{(NEU-260b)}$$
$$\Lambda(p^k)/\sqrt{p^k}\text{ aus BC/Frobenius}\quad\checkmark[K/M]\quad\text{(NEU-250-Serie)}$$

---

## Objekt-X-Hypothese (aktuell)

$$\boxed{\text{Objekt X} = \left\{\mathcal{H}(T_a^{\rm w}),\;J_{a,b},\;\overline{\mathscr{D}}_{a,\varepsilon(a)\cdot P}\right\}_{0<a<b}}$$

mit $\varepsilon(a)\in\{+1,-1\}$ (offen), $\phi(a,z)$ (offen), $J_{a,b}$ (offen).

Unter RH (Objekt-X-Konjektur): $\mathcal{K}_X:=\varinjlim_a\mathcal{H}(T_a)\xrightarrow{\rm RH}\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)$.

---

*Zuletzt aktualisiert: 2026-08-08 (SYN-Audit P02–P04; $\mathbb{Z}_2$-Priorität; veraltete Spiegelungssymmetrie-Frage gestrichen)*
