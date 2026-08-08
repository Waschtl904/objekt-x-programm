# NEU-260a — $\lambda$-Gauge-Audit

**Katalog-ID:** NEU-260a  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch 1: 2026-08-08a; Patch 2: 2026-08-08b)  
**Auftrag:** (1) Topologische Äquivalenz $\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})$ $\checkmark[K/M]$; (2) Spektralinvarianz $?[O]$; (3) RH-freier Gauge-Fix.  
**Patch 1 (2026-08-08a):** $\lambda=0$ als RH-konditional markiert; $\lambda_{\rm can}(a)=\lambda_a-1$ eingetragen.  
**Patch 2 (2026-08-08b):** Kanonizität von $\lambda_a-1$ präzisiert: bequeme Normierung, nicht einzig mögliche.

---

## 0. Fragestellung

Für $\lambda_1 < \lambda_2 < \lambda_a := \inf\sigma(A_a)$:
$$
\|v\|_{T_{a,\lambda}}^2 := Q_W^a(v,v) - \lambda\|v\|_{L^2(-a,a)}^2. \qquad (0\text{-Def})
$$

---

## 1. Topologische Äquivalenz $\checkmark[K/M]$

$$
\|v\|_{T_{a,\lambda_2}}^2 \le \|v\|_{T_{a,\lambda_1}}^2 \le \frac{\lambda_a-\lambda_1}{\lambda_a-\lambda_2}\cdot\|v\|_{T_{a,\lambda_2}}^2. \qquad (1\text{-Equiv})
$$

$$
\boxed{\iota_{\lambda_1,\lambda_2}: \mathcal{H}(T_{a,\lambda_1}) \xrightarrow{\;\cong\;} \mathcal{H}(T_{a,\lambda_2}).\quad\checkmark[K/M]\text{ (RH-frei)}} \qquad (1\text{-Iso})
$$

$\lambda$ ist Gauge für Hilbertraumtopologie. $\checkmark[K/M]$

---

## 2. Spektralinvarianz $?[O]$ (niedrige Priorität nach NEU-260b)

Suzuki: Nullstellen von $W(a,\theta;z)$ erwartungsgemäß $\lambda$-unabhängig; kein Satz. $?[O]$

---

## 3. RH-freier Gauge-Fix (Patch 2 korrigiert)

### 3.1 $\lambda=0$ ist RH-konditional $\times[M]$ als RH-freie Konvention

Suzuki darf $\lambda=0$ unter RH wählen ($A_a>0$ gilt unter RH). Ohne RH: $\lambda_a<0$ möglich, dann $T_{a,0}=A_a$ nicht positiv.

$$
\boxed{\lambda=0\text{ ist RH-konditional.}\quad\times[M]\text{ als RH-freie Konvention.}} \qquad (3\text{-RH0})
$$

### 3.2 RH-freier Gauge-Fix: Familie, nicht Einzelwert

Für jedes $c>0$:
$$
\boxed{\lambda_{a,c} := \lambda_a - c \quad\Rightarrow\quad T_{a,c} = A_a-(\lambda_a-c)I = (A_a-\lambda_aI)+cI \ge cI > 0.\quad\checkmark[K/M]\text{ (RH-frei)}} \qquad (3\text{-Family})
$$

**Kanonische Konvention:** $c=1$ ist bequem (natürliche Normierung, passend zur von-Neumann-Konvention mit Defizienzpunkten $\pm i$). Aber die Zahl $1$ ist nur Motivation, keine mathematische Kanonizität.

$$
\boxed{\lambda_{\rm can}(a) := \lambda_a-1 \text{ ist bequeme kanonische Konvention, nicht einzig möglicher RH-freier Gauge-Fix.}\quad\checkmark[M]} \qquad (3\text{-Can})
$$

$$
\boxed{\text{Verbindung }c=1\leftrightarrow\text{Defizienzpunkte }\pm i\text{: Motivation, keine mathematische Kanonizität.}} \qquad (3\text{-Motiv})
$$

---

## 4. Statusbuchungen

$$\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})\quad\checkmark[K/M]\qquad(4\text{-a})$$
$$C_{\lambda_1,\lambda_2,a}=(\lambda_a-\lambda_1)/(\lambda_a-\lambda_2)\quad\checkmark[K/M]\qquad(4\text{-b})$$
$$\lambda\text{ ist Gauge für Hilbertraumtopologie}\quad\checkmark[K/M]\qquad(4\text{-c})$$
$$\lambda=0\text{ ist RH-konditional}\quad\times[M]\text{ als RH-freie Konvention}\qquad(4\text{-d})$$
$$\lambda_{a,c}=\lambda_a-c,\;T_{a,c}\ge cI\;(c>0)\quad\checkmark[K/M]\text{ (RH-frei)}\qquad(4\text{-e})$$
$$\lambda_{\rm can}=\lambda_a-1\text{: bequeme Konvention, nicht einzig möglich}\quad\checkmark[M]\qquad(4\text{-f})$$
$$\text{Verbindung }c=1\leftrightarrow\pm i\text{: Motivation}\quad\times[M]\text{ als Kanonizitätsargument}\qquad(4\text{-g})$$
$$\sigma(\overline{\mathscr{D}}_{a,\theta}^{(\lambda)})\text{ }\lambda\text{-unabhängig (Suzuki-Erwartung)}\quad?[O]\text{ (niedrige Prio)}\qquad(4\text{-h})$$

---

*Lizenz: CC BY 4.0.  Patch 2 (2026-08-08b): $\lambda_a-1$ als bequeme, nicht einzig kanonische Konvention.*
