# NEU-260a — $\lambda$-Gauge-Audit

**Katalog-ID:** NEU-260a  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-08)  
**Auftrag:** (1) Topologische Äquivalenz $\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})$ $\checkmark[K/M]$; (2) Spektralinvarianz $\sigma(\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)})\stackrel{?}{=}\sigma(\overline{\mathscr{D}}_{a,\theta'}^{(\lambda_2)})$ $?[O]$; (3) RH-freier Gauge-Fix $\lambda_{\rm can}(a):=\lambda_a-1$ $\checkmark[K/M]$.  
**Patch:** $\lambda=0$ als RH-konditional markiert; $\lambda_{\rm can}(a)=\lambda_a-1$ als RH-freier kanonischer Gauge-Fix eingetragen.  
**Vorgänger:** NEU-260 (Hauptknoten)  

---

## 0. Fragestellung

Für $\lambda_1 < \lambda_2 < \lambda_a := \inf\sigma(A_a)$ entstehen Hilberträume
$$
\mathcal{H}(T_{a,\lambda_i}):=\overline{C_c^\infty(-a,a)}^{\|\cdot\|_{T_{a,\lambda_i}}}, \qquad \|v\|_{T_{a,\lambda}}^2 := Q_W^a(v,v) - \lambda\|v\|_{L^2(-a,a)}^2. \qquad (0\text{-Def})
$$
Auf jedem existiert eine $S^1$-Familie $\overline{\mathscr{D}}_{a,\theta}^{(\lambda)}$ von sa. Erweiterungen von $i\frac{d}{dx}$.

**Frage 1 (Topologie):** $\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})$ kanonisch? $\checkmark[K/M]$

**Frage 2 (Spektrum):** $\sigma(\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)}) = \sigma(\overline{\mathscr{D}}_{a,\theta'(\lambda_1,\lambda_2,\theta)}^{(\lambda_2)})$? $?[O]$

**Frage 3 (Gauge-Fix):** Welche Wahl $\lambda(a)$ ist RH-frei kanonisch? $\checkmark[K/M]$ (Patch)

---

## 1. Topologische Äquivalenz $\checkmark[K/M]$

### 1.1 Normenvergleich

Für $\lambda_1 < \lambda_2 < \lambda_a$:
$$
\|v\|_{T_{a,\lambda_1}}^2 = \underbrace{\left(Q_W^a(v) - \lambda_2\|v\|_2^2\right)}_{=\|v\|_{T_{a,\lambda_2}}^2} + (\lambda_2-\lambda_1)\|v\|_2^2. \qquad (1\text{-Split})
$$

Da $T_{a,\lambda_2}>0$:
$$
\|v\|_{T_{a,\lambda_2}}^2 \ge (\lambda_a-\lambda_2)\|v\|_2^2. \qquad (1\text{-LB})
$$

Aus $(1\text{-Split})$ und $(1\text{-LB})$:
$$
\boxed{\|v\|_{T_{a,\lambda_2}}^2 \le \|v\|_{T_{a,\lambda_1}}^2 \le C_{\lambda_1,\lambda_2,a}\cdot\|v\|_{T_{a,\lambda_2}}^2,} \qquad (1\text{-Equiv})
$$
mit
$$
\boxed{C_{\lambda_1,\lambda_2,a} := \frac{\lambda_a-\lambda_1}{\lambda_a-\lambda_2} \in (1,\infty).} \qquad (1\text{-Factor})
$$

### 1.2 Kanonischer Isomorphismus

Die Identität auf $C_c^\infty(-a,a)$ ist bezüglich beider Normen dicht und nach $(1\text{-Equiv})$ stetig mit stetigem Inversen. Kanonische Fortsetzung:
$$
\boxed{\iota_{\lambda_1,\lambda_2}: \mathcal{H}(T_{a,\lambda_1}) \xrightarrow{\;\cong\;} \mathcal{H}(T_{a,\lambda_2}).\quad\checkmark[K/M]\text{ (RH-frei, Satz)}} \qquad (1\text{-Iso})
$$

$\iota_{\lambda_1,\lambda_2}$ ist **nicht isometrisch** (Faktor $C_{\lambda_1,\lambda_2,a}\neq 1$), aber kanonisch.

$$
\lambda\text{ ist Gauge für Hilbertraumtopologie.}\quad\checkmark[K/M] \qquad (1\text{-Gauge})
$$

---

## 2. Spektralinvarianz: offen $?[O]$

### 2.1 Warum $(1\text{-Iso})$ allein nicht genügt

$\iota_{\lambda_1,\lambda_2}$ transportiert den minimalen Operator $\mathscr{D}_a = i\frac{d}{dx}$. Da $\iota_{\lambda_1,\lambda_2}$ nicht unitär ist, kann der Transport die von-Neumann-Parametrisierung $e^{i\theta}$ verschieben:
$$
\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)} \quad\xmapsto{\iota_{\lambda_1,\lambda_2}}\quad \overline{\mathscr{D}}_{a,\theta'(\lambda_1,\lambda_2,\theta)}^{(\lambda_2)}. \qquad (2\text{-Transport})
$$

Die Defizienträume $\mathcal{N}_{\pm,a}^{(\lambda)} := \ker(\mathscr{D}_a^{*,(\lambda)}\mp i)$ sind je eindimensional und werden durch $\iota_{\lambda_1,\lambda_2}$ isomorph abgebildet, aber nicht unitär. Die Parametrisierungsverschiebung $\theta\mapsto\theta'$ hängt davon ab, wie $\iota_{\lambda_1,\lambda_2}$ die normierten Defizientvektoren dreht.

$$
\boxed{\exists\,\theta'(\lambda_1,\lambda_2,\theta)\text{ s.d. }\sigma\left(\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)}\right) = \sigma\left(\overline{\mathscr{D}}_{a,\theta'}^{(\lambda_2)}\right)?\quad?[O]} \qquad (2\text{-SpecInv})
$$

### 2.2 Suzukis Aussage (kein Satz)

Suzuki schreibt ausdrücklich, dass die Nullstellen von $W(a,\theta;z)$ **erwartungsgemäß** $\lambda$-unabhängig sein sollten; unter RH kann $\lambda=0$ gewählt werden. Er **beweist** die $\lambda$-Unabhängigkeit nicht.

$$
\sigma(W(a,\theta;z))\text{ ist }\lambda\text{-unabhängig: Suzuki-Erwartung, kein Satz.}\quad?[O] \qquad (2\text{-Suzuki})
$$

---

## 3. RH-freier Gauge-Fix (Patch) $\checkmark[K/M]$

### 3.1 Warum $\lambda=0$ nicht als RH-freie Konvention taugt

Suzuki darf unter RH $\lambda=0$ wählen, weil RH $\Rightarrow$ $A_a>0$ $\forall a$. Aber:

$$
\boxed{\lambda=0\text{ ist RH-konditional: }T_{a,0}=A_a>0\text{ gilt nur unter RH.}\quad\times[M]\text{ als RH-freie Konvention.}} \qquad (3\text{-RH0})
$$

Scheitert RH, existiert ein $a_0$ mit $\lambda_{a_0} = \inf\sigma(A_{a_0}) < 0$. Dann wäre $T_{a_0,0}=A_{a_0}$ nicht positiv, und $\mathcal{H}(T_{a_0,0})$ in Suzukis Sinn nicht verfügbar.

### 3.2 Kanonischer RH-freier Gauge-Fix

$$
\boxed{\lambda_{\rm can}(a) := \lambda_a - 1, \qquad T_a^{\rm can} := A_a - (\lambda_a-1)I = (A_a-\lambda_a I) + I \ge I > 0.\quad\checkmark[K/M]\text{ (RH-frei)}} \qquad (3\text{-Can})
$$

**Warum das funktioniert:** $\lambda_a = \inf\sigma(A_a)$ existiert RH-frei (Suzuki beweist seine Existenz und Stetigkeit in $a$). Damit ist $A_a - \lambda_a I \ge 0$ und $T_a^{\rm can} = (A_a-\lambda_a I)+I \ge I$ unabhängig vom Vorzeichen von $\lambda_a$.

**Warum $-1$:** Der Verschiebungswert $1$ korrespondiert mit den Defizienzpunkten $\pm i$ in der von-Neumann-Theorie (Konvention $\mathscr{D}_a^* \pm iI$). Andere Werte $\delta>0$ wären topologisch äquivalent; $\delta=1$ ist die natürliche Wahl.

$$
\boxed{\lambda=0\text{ RH-konditional;}\quad\lambda_{\rm can}(a)=\lambda_a-1\text{ RH-freier Gauge-Fix.}\quad\checkmark[K/M]} \qquad (3\text{-Summary})
$$

**Konsequenz für folgende Knoten:** NEU-260b und spätere Knoten verwenden $\lambda=\lambda_{\rm can}(a)=\lambda_a-1$ als Standardwahl. Die Spektralinvarianzfrage $(2\text{-SpecInv})$ bleibt offen, hat aber mit dieser Konvention niedrige operative Priorität.

---

## 4. Statusbuchungen

$$\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})\text{ (kanonisch)}\quad\checkmark[K/M]\qquad(4\text{-a})$$
$$C_{\lambda_1,\lambda_2,a}=(\lambda_a-\lambda_1)/(\lambda_a-\lambda_2)\quad\checkmark[K/M]\qquad(4\text{-b})$$
$$\lambda\text{ ist Gauge für Hilbertraumtopologie}\quad\checkmark[K/M]\qquad(4\text{-c})$$
$$\lambda=0\text{ ist RH-konditional}\quad\times[M]\text{ als RH-freie Konvention}\qquad(4\text{-d})$$
$$\lambda_{\rm can}(a):=\lambda_a-1,\;T_a^{\rm can}\ge I\quad\checkmark[K/M]\text{ (RH-frei)}\qquad(4\text{-e})$$
$$\sigma(\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)})=\sigma(\overline{\mathscr{D}}_{a,\theta'}^{(\lambda_2)})\text{ (Spektralinvarianz)}\quad?[O]\text{ (niedrige Priorität)}\qquad(4\text{-f})$$
$$\lambda\text{-Unabhängigkeit }W(a,\theta;z)\text{-Nullstellen (Suzuki): Erwartung, kein Satz}\quad?[O]\qquad(4\text{-g})$$

---

## 5. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-260 | Hauptknoten | Klassifikation |
| NEU-259 (Patch 2) | 7ce07e0 | $\lambda$ als Gauge abgestuft |
| Suzuki 2026 | Abstract, \S{}2 | $T_{a,\lambda}$, $\mathcal{H}(T_{a,\lambda})$, $\lambda_a$ stetig, $\lambda=0$ unter RH |
| von Neumann | — | Defizienträume, Defizienzpunkte $\pm i$ |
| Kato 1966 | — | Formäquivalenz |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2026-08-08: $\lambda_{\rm can}(a)=\lambda_a-1$ als RH-freier Gauge-Fix $\checkmark[K/M]$. Gibt NEU-260b frei.*
