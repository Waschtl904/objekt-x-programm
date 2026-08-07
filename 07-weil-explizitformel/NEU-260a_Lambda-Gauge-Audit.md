# NEU-260a — $\lambda$-Gauge-Audit

**Katalog-ID:** NEU-260a  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** (1) Topologische Äquivalenz $\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})$ $\checkmark[K/M]$; (2) Spektralinvarianz $\sigma(\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)})\stackrel{?}{=}\sigma(\overline{\mathscr{D}}_{a,\theta'}^{(\lambda_2)})$ $?[O]$.  
**Vorgänger:** NEU-260 (Hauptknoten)  

---

## 0. Fragestellung

Für $\lambda_1 < \lambda_2 < \lambda_a := \inf\sigma(A_a)$ entstehen Hilberträume
$$
\mathcal{H}(T_{a,\lambda_i}):=\overline{C_c^\infty(-a,a)}^{\|\cdot\|_{T_{a,\lambda_i}}}, \qquad \|v\|_{T_{a,\lambda}}^2 := Q_W^a(v,v) - \lambda\|v\|_{L^2(-a,a)}^2. \qquad (0\text{-Def})
$$
Auf jedem existiert eine $S^1$-Familie $\overline{\mathscr{D}}_{a,\theta}^{(\lambda)}$ von sa. Erweiterungen von $i\frac{d}{dx}$.

**Frage 1 (Topologie):** $\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})$ kanonisch?

**Frage 2 (Spektrum):** $\sigma(\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)}) = \sigma(\overline{\mathscr{D}}_{a,\theta'(\lambda_1,\lambda_2,\theta)}^{(\lambda_2)})$ für geeignetes $\theta'$?

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

Die Defizienträume $\mathcal{N}_{\pm i}^{(\lambda)} := \ker(\mathscr{D}_a^{*,(\lambda)}\mp i)$ sind je eindimensional und werden durch $\iota_{\lambda_1,\lambda_2}$ isomorph abgebildet, aber **nicht notwendig unitär**. Die Parametrisierungsverschiebung $\theta\mapsto\theta'$ hängt davon ab, wie $\iota_{\lambda_1,\lambda_2}$ die normierten Defizientvektoren dreht.

$$
\boxed{\exists\,\theta'(\lambda_1,\lambda_2,\theta)\text{ s.d. }\sigma\left(\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)}\right) = \sigma\left(\overline{\mathscr{D}}_{a,\theta'}^{(\lambda_2)}\right)?\quad?[O]} \qquad (2\text{-SpecInv})
$$

### 2.2 Suzukis Aussage (kein Satz)

Suzuki schreibt ausdrücklich, dass die Nullstellen von $W(a,\theta;z)$ **erwartungsgemäß** $\lambda$-unabhängig sein sollten; unter RH kann $\lambda=0$ gewählt werden. Er **beweist** die $\lambda$-Unabhängigkeit nicht.

$$
\sigma(W(a,\theta;z))\text{ ist }\lambda\text{-unabhängig: Suzuki-Erwartung, kein Satz.}\quad?[O] \qquad (2\text{-Suzuki})
$$

### 2.3 Praktische Konsequenz

Solange $(2\text{-SpecInv})$ offen ist, soll jeder folgende Knoten eine explizite Wahl $\lambda(a)$ mitführen. Natürlicher Kandidat: $\lambda(a)=0$ (falls $\lambda_a>0$) oder eine arithmetisch motivierte Wahl $\to$ NEU-260b kann $\lambda=0$ als Konvention setzen, falls die $\theta$-Selektion unabhängig von $\lambda$ formulierbar ist.

$$
\text{Kanonische }\lambda(a)\text{-Konvention: niedrige Priorität; nach NEU-260b neu bewerten.}\quad?[O] \qquad (2\text{-Conv})
$$

---

## 3. Statusbuchungen

$$\mathcal{H}(T_{a,\lambda_1})\cong\mathcal{H}(T_{a,\lambda_2})\text{ (kanonisch)}\quad\checkmark[K/M]\qquad(3\text{-a})$$
$$C_{\lambda_1,\lambda_2,a}=(\lambda_a-\lambda_1)/(\lambda_a-\lambda_2)\quad\checkmark[K/M]\qquad(3\text{-b})$$
$$\lambda\text{ ist Gauge für Hilbertraumtopologie}\quad\checkmark[K/M]\qquad(3\text{-c})$$
$$\sigma(\overline{\mathscr{D}}_{a,\theta}^{(\lambda_1)})=\sigma(\overline{\mathscr{D}}_{a,\theta'}^{(\lambda_2)})\text{ (Spektralinvarianz)}\quad?[O]\qquad(3\text{-d})$$
$$\theta\mapsto\theta'(\lambda_1,\lambda_2,\theta)\text{ (Parametrisierungsverschiebung)}\quad?[O]\qquad(3\text{-e})$$
$$\lambda\text{-Unabhängigkeit }W(a,\theta;z)\text{-Nullstellen (Suzuki): Erwartung, kein Satz}\quad?[O]\qquad(3\text{-f})$$
$$\lambda(a)=0\text{ als Konvention nach NEU-260b neu bewerten}\quad?[O]\qquad(3\text{-g})$$

---

## 4. Übergang zu NEU-260b

$$
\boxed{\lambda\text{-Audit: Topologie }\checkmark[K/M].\quad\text{Spektralinvarianz: }?[O]\text{ (präzise eingegrenzt).}\quad\text{Nächster Knoten: NEU-260b }(\theta\text{-Selektion).}} \qquad (4\text{-Close})
$$

---

## 5. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-260 | Hauptknoten | Klassifikation |
| NEU-259 (Patch 2) | 7ce07e0 | $\lambda$ als Gauge abgestuft |
| Suzuki 2026 | Abstract, §2 | $T_{a,\lambda}$, $W(a,\theta;z)$, $\lambda$-Erwartung |
| von Neumann | — | Defizienträume, $\theta$-Parametrisierung |
| Kato 1966 | — | Formäquivalenz |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Schließt $\lambda$-Topologiefrage $\checkmark$; öffnet Spektralinvarianz präzise $?[O]$. Gibt NEU-260b frei.*
