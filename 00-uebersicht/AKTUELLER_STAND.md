# Aktueller Stand — 2026-08-08 (Audit-Update 2)

---

## SYN-Audit-Regel

$$\text{NEU-Serie}\to\text{SYN-Entwurf}\to\text{SYN-Direktaudit}\to\text{kanonische Tagesreferenz.}$$

| Manuskript | Audit-Status |
|---|---|
| P01 | Entwurf (P01-Audit ausstehend) |
| P02 | Patch 2 (2026-08-08): $\mathcal{S}_{\rm adel}^{\rm amp}$, $R_{\rm PW}$, $g_{a,b}$ korrigiert; freizugeben nach Gegenprüfung |
| P03 | $\checkmark$ SYN-Audit 2026-08-08 **kanonische Tagesreferenz** |
| P04 | $\checkmark$ SYN-Audit 2026-08-08 (Forschungsfront: NEU-260b.2) |

---

## Synthese-Manuskripte (papers/)

| ID | Titel | Status | Quellknoten |
|---|---|---|---|
| **P01** | BC Prime Power Weights | Entwurf (Audit ausstehend) | NEU-250b–j |
| **P02** | Adelic Weil Amplitude Port | Patch 2 (Audit-Freigabe ausstehend) | NEU-250n–r, 252 |
| **P03** | Haar-$L^2$ Firewall | $\checkmark$ **kanonische Tagesreferenz** | NEU-253–258 |
| **P04** | Finite Weil Geometry | $\checkmark$ (Forschungsfront aktiv) | NEU-259–260b.2 |

---

## Aktive Forschungsfront

| Knoten | Titel | Status |
|---|---|---|
| NEU-260a | $\lambda$-Gauge-Audit | $\checkmark[K/M]$ |
| NEU-260b | $\theta$-Selektionsaudit | $\checkmark[K/M]$ (Parität $\to\mathbb{Z}_2$) |
| NEU-260b.1 | $\mathbb{Z}_2$-Selektion (Kandidaten) | $\checkmark[K/M]$ (Patch 2: Stetigkeit $\times$, KMS-Lücke, Frob-Konvention) |
| **NEU-260b.2** | Paritätsselektion durch Suzuki-Grenzfunktion | $\checkmark[K/M]$ **höchste Priorität** |
| NEU-260c | Grenznormalisierung $\phi(a,z)$ | $?[O]$ |
| NEU-260d | $J_{a,b}$-Geometrie | $?[O]$ |

---

## Zentrale offene Leitfrage (aktualisiert)

$$\boxed{\text{Kann die analytische Suzuki-Grenzstruktur }+P\text{ bereits eindeutig erzwingen?}}$$

Konkret (NEU-260b.2 $\checkmark[K/M]$, konditional):
$$\text{Suzuki-Grenzrelation}\Longrightarrow\varepsilon(a)=+1\text{ asymptotisch.}$$

Was noch offen bleibt:
1. Suzukis Grenzrelation selbst beweisen (impliziert RH).
2. Asymptotisches $\varepsilon=+1$ auf alle $a>0$ propagieren ($\to$ nach Konstruktion analytischer Familie).
3. Falls Suzuki-Argument nicht reicht: BC/KMS oder Frobenius als Vorzeichen-Selektor (nachrangig, Typisierungslücken bekannt).

~~Wie wählen Stetigkeit/BC/Frobenius das Vorzeichen?~~ (veraltet, ersetzt durch Suzuki-Grenzstruktur-Frage)

---

## Hart gebuchte Resultate (vollständige Liste)

$$W_{\rm NEU\text{-}252}=W_{\rm Lit}\quad\checkmark[K/M]\quad\text{(NEU-258)}$$
$$B_W\text{ semibeschränkt auf }C_c^\infty(\mathbb{R})\text{ rel. }L^2(du)\Leftrightarrow\text{RH}\quad\checkmark[K/M]\quad\text{(NEU-257)}$$
$$B_W\text{ nicht abschließbar auf }L^2(du)\text{ unter RH (}\mu_W\not\ll du\text{)}\quad\checkmark[K/M]\quad\text{(NEU-257)}$$
$$\text{KLMN auf }L^2(\mathbb{R}):\;\times[M]\quad\text{(NEU-257)}$$
$$\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\text{ unter RH}\quad\checkmark[K/M]\quad\text{(NEU-257, Suzuki 2025)}$$
$$Q_W^a\text{ semibeschränkt, abschließbar auf }L^2(-a,a)\quad\checkmark[K/M]\quad\text{(NEU-259)}$$
$$A_a=A_a^*,\text{ diskretes Spektrum, }\lambda_a\text{ stetig in }a\quad\checkmark[K/M]\quad\text{(NEU-259)}$$
$$\lambda_{\rm can}(a)=\lambda_a-1\text{ (bequeme Konvention; }\lambda=0\text{ RH-konditional)}\quad\checkmark[K/M]\quad\text{(NEU-260a)}$$
$$\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})\quad\checkmark[K/M]\quad\text{(NEU-260a)}$$
$$U_a:\mathcal{N}_{+,a}\to\mathcal{N}_{-,a}\text{ intrinsisch; }\mathcal{N}_{\pm}=\operatorname{span}\{v_\pm\},\;T_av_\pm=e^{\pm x}\quad\checkmark[K/M]\quad\text{(NEU-260b)}$$
$$PA_a=A_aP\quad\checkmark[M]/\text{Suzuki 2026}$$
$$Pv_+=v_-\quad\checkmark[K/M]\quad\text{(NEU-260b)}$$
$$U(1)\xrightarrow{\text{Parität}}\{+P,-P\}\cong\mathbb{Z}_2\quad\checkmark[K/M]\quad\text{(NEU-260b)}$$
$$W(a,0;-z)=-W(a,0;z)\quad(+P\text{-Zweig ungerade})\quad\checkmark[K/M]\quad\text{(NEU-260b.2)}$$
$$W(a,\pi;-z)=+W(a,\pi;z)\quad(-P\text{-Zweig gerade})\quad\checkmark[K/M]\quad\text{(NEU-260b.2)}$$
$$F(-z)=-F(z),\;F(z)=cz+O(z^3),\;c\neq0\quad\checkmark[K/M]\quad\text{(NEU-260b.2)}$$
$$\theta=\pi\text{ inkompatibel mit Suzuki-Grenzrelation (Hurwitz/Rouché)}\quad\checkmark[K/M]\text{ (konditional)}\quad\text{(NEU-260b.2)}$$
$$\varepsilon(a)=+1\text{ für hinreichend großes }a\text{ (konditional auf Grenzrelation)}\quad\checkmark[K/M]\text{ (konditional)}\quad\text{(NEU-260b.2)}$$
$$\Lambda(p^k)/\sqrt{p^k}\text{ aus BC/Frobenius}\quad\checkmark[K/M]\quad\text{(NEU-250-Serie)}$$

---

## Objekt-X-Hypothese (aktuell)

$$\text{Objekt X} = \left\{\mathcal{H}(T_a^{\rm w}),\;J_{a,b},\;\overline{\mathscr{D}}_{a,\varepsilon(a)\cdot P}\right\}_{0<a<b}$$

mit $\varepsilon(a)=+1$ asymptotisch (konditional), $\phi(a,z)$ (offen), $J_{a,b}$ (offen).

Unter RH (Objekt-X-Konjektur): $\mathcal{K}_X:=\varinjlim_a\mathcal{H}(T_a)\xrightarrow{\rm RH}\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)$.

---

*Zuletzt aktualisiert: 2026-08-08 (SYN-Audit Update 2: P02 Patch 2; Leitfrage auf Suzuki-Grenzstruktur fokussiert; NEU-260b.2 als höchste Priorität)*
