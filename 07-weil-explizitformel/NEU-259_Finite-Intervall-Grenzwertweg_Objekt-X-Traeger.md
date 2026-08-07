# NEU-259 — Direktaudit des finite-Intervall-Grenzwertwegs als Objekt-X-Träger

**Katalog-ID:** NEU-259  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch 2: 2026-08-07)  
**Auftrag:** Fünf atomare Fragen zum Finite-Intervall-Grenzwertweg (Suzuki 2026). Strenge Trennung Satz/Vermutung. Identifikation des BC/Adelen-Eintrittspunkts.  
**Patch 2:** $\lambda(a)$ als Hilfsverschiebung abgestuft; $\phi(a,z)$ als echtes viertes Grenzdatum ergänzt; $J_{a,b}$ als originale Objekt-X-Hypothese (nicht in Suzukis analytischer Vermutung benötigt) markiert; NEU-260-Auftrag auf vier Fragen A–D präzisiert.  
**Status:** Endlich-Ebene $\checkmark$ (Satz); Grenzdaten $\theta(a),\phi(a,z),J_{a,b}$: $?[O]$\to NEU-260.  
**Vorgänger:** NEU-258 $\checkmark$, NEU-257, NEU-252, NEU-250-Serie  
**Nachfolger:** NEU-260 (Kanonizitätsaudit der Suzuki-Grenzdaten und adelischen Übergangsstruktur)

---

## 0. Motivation und Diagramm

NEU-257 $\checkmark[K/M]$: $H_0=L^2(\mathbb{R})$ ist nicht der Weil-Abschlussraum. Suzuki 2026 liefert RH-frei für jedes $a>0$ eine Operatorkette und — in einem zweiten Schritt — einen Hilbert-Pólya-artigen first-order Operator $\overline{\mathscr{D}}_{a,\theta}$:

$$
\boxed{ \mathcal{H}(T_a) \quad\xrightarrow[a\to\infty]{\ ?\ }\quad \mathcal{K}_X \quad\xrightarrow[\mathrm{RH}]{\sim}\quad \mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma). } \qquad (0\text{-Diag})
$$

**Objekt X (revidierte Kernhypothese):**
$$
\boxed{\left\{\mathcal{H}(T_{a,\lambda(a)}),\;J_{a,b},\;\overline{\mathscr{D}}_{a,\theta(a)}\right\}_{0<a<b}} \qquad (0\text{-Sys})
$$
mit arithmetisch kanonisch bestimmten $\theta(a)$, $J_{a,b}$ (und kontrollierbarem $\lambda(a)$).

**Doppelte Aufgabe:** Suzuki liefert die Operatorhülle und eine analytische Grenzwertvermutung über $W(a,\theta;z)$. BC/Adelen sollen die kanonischen Grenzdaten $\theta(a),\phi(a,z),J_{a,b}$ liefern.

---

## 0b. Zwei Suzuki-Ebenen

| Ebene | Objekt | Status | Bezug zu $\{\gamma_n\}$ |
|---|---|---|---|
| **1** | $Q_W^a\to A_a\to T_{a,\lambda}\to\mathcal{H}(T_{a,\lambda})$ | $\checkmark$ Satz | keiner direkt |
| **2** | $\overline{\mathscr{D}}_{a,\theta}$ auf $\mathcal{H}(T_{a,\lambda})$ | $\checkmark$ Satz | $\sigma(\overline{\mathscr{D}}_{a,\theta})=$ Nullstellen von $W(a,\theta;z)$ |
| **Grenzwert** | $e^{\phi(a,z)}W(a,\theta(a);z)\to\frac{z^2\xi(1/2-iz)}{\xi'(1/2-iz)}$ | $\mathbf{Vermutung}$ | $\sigma(D_X)=\{\gamma_n\}$ |

**Korrekte Kette:**
$$
\boxed{Q_W^a\longrightarrow A_a\longrightarrow T_{a,\lambda}:=A_a-\lambda I\longrightarrow\mathcal{H}(T_{a,\lambda})\longrightarrow\overline{\mathscr{D}}_{a,\theta}.} \qquad (0\text{-Chain})
$$

$$
\boxed{A_a\;\neq\;\text{Suzukis conjecturaler Hilbert-Pólya-Operator.}\quad\times[M]} \qquad (0\text{-notHP})
$$

---

## 0c. Status der Grenzdaten (Patch 2)

$$
\boxed{\text{Vier Grenzdaten mit unterschiedlichem mathematischen Status:}} \qquad (0\text{-Data})
$$

| Datum | Charakter | Kanonisierungsbedarf | NEU-260-Frage |
|---|---|---|---|
| $\lambda(a)<\lambda_a$ | **Hilfsverschiebung** (Gauge): Spektrum von $W(a,\theta;z)$ nach Suzuki $\lambda$-unabhängig; Kontrolle beim Grenzwert analytisch relevant | eventuell kein echter Selektionsdatum; prüfen | **A** |
| $\theta(a)\in[0,2\pi)$ | **Echter Erweiterungsparameter**: $S^1$-Familie sa. Erweiterungen, Defizit $(1,1)$; genuines Selektionsproblem | BC/KMS/Frobenius-Phasenselektion | **B** |
| $\phi(a,z)$ | **Grenznormalisierung**: holomorpher Korrekturfaktor in Suzukis Grenzformel; Suzuki vermutet $\phi=0$ möglich, beweist es nicht | Arithmetische Bestimmbarkeit? $\phi=0$? | **C** |
| $J_{a,b}$ | **Originale Objekt-X-Hypothese**: nicht in Suzukis analytischer Vermutung; nötig für geometrischen globalen Grenzraum $\mathcal{K}_X$ | Adelische Multiplikation / Dilatation | **D** |

**Entscheidender Unterschied:**
$$
\boxed{\text{Suzuki braucht }J_{a,b}\text{ nicht für seine analytische Vermutung.}\quad\text{Objekt X braucht }J_{a,b}\text{ für den geometrischen globalen Grenzraum.}} \qquad (0\text{-Jab})
$$

---

## Frage 1 — RH-freie Existenz: Vollständige Kette

### 1.1 Ebene 1 (Satz)

$$
\boxed{A_a=A_a^*\ge-\lambda_a I,\quad\lambda_a:=\inf\sigma(A_a)>-\infty,\quad\text{diskretes Spektrum.}\quad\checkmark\text{ (Satz)}} \qquad (1\text{-Aa})
$$

### 1.2 $T_{a,\lambda}$ und $\mathcal{H}(T_{a,\lambda})$ (Satz)

Für $\lambda<\lambda_a$: $T_{a,\lambda}:=A_a-\lambda I>0$.
$$
\boxed{\mathcal{H}(T_{a,\lambda}):=\overline{C_c^\infty(-a,a)}^{\|\cdot\|_{T_{a,\lambda}}}\quad\text{wohldefinierter Hilbertraum.}\quad\checkmark\text{ (Satz)}} \qquad (1\text{-HTa})
$$

**$\lambda$-Abhängigkeit:** Verschiedene $\lambda<\lambda_a$ liefern topologisch äquivalente, aber nicht isometrische Hilberträume. Ob die $\overline{\mathscr{D}}_{a,\theta}$-Spektren $\lambda$-unabhängig sind: $\to$ Frage A/NEU-260.

### 1.3 Ebene 2: $\overline{\mathscr{D}}_{a,\theta}$ (Satz)

$$
\boxed{\overline{\mathscr{D}}_{a,\theta}=\overline{\mathscr{D}}_{a,\theta}^*\quad\text{auf }\mathcal{H}(T_{a,\lambda}),\quad\theta\in[0,2\pi),\quad\text{Defizit }(1,1).\quad\checkmark\text{ (Satz)}} \qquad (1\text{-Dbar})
$$

### 1.4 Suzukis Grenzwertvermutung (Vermutung)

$$
\boxed{e^{\phi(a,z)}W(a,\theta(a);z)\xrightarrow{a\to\infty}\frac{z^2\xi(1/2-iz)}{\xi'(1/2-iz)}\quad\text{lokal gleichmä\ss{}ig.}\quad\mathbf{Vermutung}} \qquad (1\text{-Conj})
$$

Suzuki bemerkt, dass $\phi(a,z)=0$ möglicherweise genügt, beweist es nicht.

---

## Frage 2 — Identifikation $B_W|_{C_c^\infty(-a,a)}\stackrel{?}{=}Q_W^a$

$$
(B_\Gamma+B_{\rm fin})|_{C_c^\infty(-a,a)}=Q_{W,\Gamma+\rm fin}^a.\quad\checkmark[K/M]\text{ (aus NEU-258)} \qquad (2\text{-GamFin})
$$

$$
B_{\rm pole}|_{C_c^\infty(-a,a)}\stackrel{?}{=}Q_{W,\rm pole}^a\quad?[O]\text{ (Polterm-Randaudit)} \qquad (2\text{-Pole})
$$

$$
B_W|_{C_c^\infty(-a,a)}=Q_W^a\quad?[O]\text{ (offen bis Polterm-Randaudit)} \qquad (2\text{-Final})
$$

---

## Frage 3 — Satz vs. Vermutung

| Aussage | Status |
|---|---|
| $Q_W^a$ semibeschränkt, abschließbar auf $L^2(-a,a)$ | $\checkmark$ **Satz** |
| $A_a=A_a^*$, diskretes Spektrum | $\checkmark$ **Satz** |
| $T_{a,\lambda}>0$, $\mathcal{H}(T_{a,\lambda})$ Hilbertraum | $\checkmark$ **Satz** |
| $\overline{\mathscr{D}}_{a,\theta}=\overline{\mathscr{D}}_{a,\theta}^*$ auf $\mathcal{H}(T_{a,\lambda})$ | $\checkmark$ **Satz** |
| $L^2(-a,a)\hookrightarrow L^2(-b,b)$ durch Nullfortsetzung | $\checkmark$ **Satz** (Suzuki) |
| Spektrum von $W(a,\theta;z)$ $\lambda$-unabhängig | $?[O]$ (Suzuki-Behauptung, kein Beweis) |
| $e^{\phi(a,z)}W(a,\theta(a);z)\to\xi$-Quotient | $\mathbf{Vermutung}$ |
| $J_{a,b}^{\mathcal{H}}$ kanonisch | $?[O]$, originale Objekt-X-Hypothese |
| $\mathcal{K}_X=\varinjlim_a\mathcal{H}(T_a)$ | $?[O]$ |

---

## Frage 4 — Kanonische Übergangsabbildungen

$L^2$-Einbettung durch Nullfortsetzung: kanonisch $\checkmark$ (Suzuki, Satz). $(4\text{-L2Emb})$

Auf Formtopologie-Ebene:
$$
\boxed{J_{a,b}^{\mathcal{H}}:\mathcal{H}(T_{a,\lambda(a)})\to\mathcal{H}(T_{b,\lambda(b)})\text{ kanonisch}:\quad?[O]\to\text{NEU-260-D}} \qquad (4\text{-HEmb})
$$

Operator-Intertwining (starke Form):
$$
\boxed{J_{a,b}\,\overline{\mathscr{D}}_{a,\theta(a)}\stackrel{?}{\subset}\overline{\mathscr{D}}_{b,\theta(b)}\,J_{a,b}.\quad?[O]\to\text{NEU-260-D}} \qquad (4\text{-Inter})
$$

Falls $(4\text{-Inter})$ gilt: $\{\mathcal{H}(T_a),J_{a,b},\overline{\mathscr{D}}_{a,\theta(a)}\}_{a<b}$ ist ein echtes gerichtetes Operatorensystem.

---

## Frage 5 — BC/Adelen-Eintrittspunkt (präzisiert)

$$
\boxed{\underbrace{\text{BC/Adelen}}_{\text{arithm. Herkunft}}\xrightarrow{\theta(a),\,\phi(a,z),\,J_{a,b}}\underbrace{\{\mathcal{H}(T_a),\overline{\mathscr{D}}_{a,\theta(a)},J_{a,b}\}_{a<b}}_{\text{Objekt X}}\xrightarrow{\text{RH}}\underbrace{\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)}_{\text{Weil-Hilbertraum}}.} \qquad (5\text{-Chain})
$$

Die NEU-250-Arithmetik liefert $\Lambda(p^k)/\sqrt{p^k}$ (Vorfaktor in $Q_W^a$) $\checkmark[K/M]$. Offen: $\theta(a)$, $\phi(a,z)$, $J_{a,b}$ $\to$ NEU-260.

---

## NEU-260-Vorstruktur: Vier Fragen A–D

$$
\boxed{\text{NEU-260 — Kanonizitätsaudit der Suzuki-Grenzdaten und adelischen Übergangsstruktur.}} \qquad
$$

| Frage | Inhalt | Ziel |
|---|---|---|
| **A** | $\lambda$-Invarianz: $\sigma(W(a,\theta;z))$ wirklich $\lambda$-unabhängig? | Falls ja: $\lambda$ Gauge; kein BC-Datum. Falls nein: $\lambda(a)$ aus KMS. |
| **B** | $\theta$-Selektion: BC/KMS/Frobenius $\Rightarrow$ kanonische Phase $e^{i\theta(a)}$? | Randbedingung aus Arithmetik |
| **C** | $\phi$-Normalisierung: Arithmetik bestimmt $\phi(a,z)$; $\phi=0$ zeigbar? | Sauberste Grenzformel |
| **D** | $J_{a,b}$-Geometrie: adelische Einbettung + Intertwining $(4\text{-Inter})$? | Gerichtetes Operatorensystem |

---

## 6. Offene Punkte

$$B_W|_{C_c^\infty(-a,a)}=Q_W^a\text{ (Polterm-Randaudit)}\quad?[O]\qquad(6\text{-a})$$
$$\lambda\text{-Invarianz von }\sigma(W(a,\theta;z))\quad?[O]\to\text{NEU-260-A}\qquad(6\text{-b})$$
$$\theta(a)\text{ aus BC/KMS/Frobenius}\quad?[O]\to\text{NEU-260-B}\qquad(6\text{-c})$$
$$\phi(a,z)\text{ aus Arithmetik; }\phi=0\text{?}\quad?[O]\to\text{NEU-260-C}\qquad(6\text{-d})$$
$$J_{a,b}^{\mathcal{H}}\text{ kanonisch + Intertwining}\quad?[O]\to\text{NEU-260-D}\qquad(6\text{-e})$$
$$\overline{\mathscr{D}}_{a,\theta(a)}\xrightarrow{a\to\infty}D_X,\;\sigma(D_X)=\{\gamma_n\}\quad\mathbf{Vermutung}\qquad(6\text{-f})$$
$$\mathcal{K}_X=\varinjlim_a\mathcal{H}(T_a)\quad?[O]\qquad(6\text{-g})$$

---

## 7. Statusbuchungen

$$Q_W^a\text{ semibeschränkt, abschließbar}\quad\checkmark[K/M]\qquad(7\text{-a})$$
$$A_a=A_a^*,\text{ diskretes Spektrum}\quad\checkmark[K/M]\qquad(7\text{-b})$$
$$T_{a,\lambda}>0,\;\mathcal{H}(T_a)\text{ Hilbertraum}\quad\checkmark[K/M]\qquad(7\text{-c})$$
$$\overline{\mathscr{D}}_{a,\theta}\text{ sa. auf }\mathcal{H}(T_a)\quad\checkmark[K/M]\qquad(7\text{-d})$$
$$A_a\neq\text{conjecturaler HP-Operator}\quad\times[M]\qquad(7\text{-e})$$
$$\sigma(A_a)\to\{\gamma_n\}\quad\times[M]\text{ (falsche Ebene)}\qquad(7\text{-f})$$
$$L^2(-a,a)\hookrightarrow L^2(-b,b)\text{ kanonisch}\quad\checkmark[K/M]\qquad(7\text{-g})$$
$$(B_\Gamma+B_{\rm fin})|_{C_c^\infty(-a,a)}=Q_{W,\Gamma+\rm fin}^a\quad\checkmark[K/M]\qquad(7\text{-h})$$
$$\lambda(a)\text{: Hilfsverschiebung, nicht primdr Selektionsdatum}\quad\checkmark[K/M]\qquad(7\text{-i})$$
$$\phi(a,z)\text{: echtes Grenzdatum (Suzuki-Vermutung, unbewiesen)}\quad\checkmark[K/M]\text{ (Statuskorrektur)}\qquad(7\text{-j})$$
$$J_{a,b}\text{: originale Objekt-X-Hypothese, nicht in Suzukis analytischer Vermutung}\quad\checkmark[K/M]\qquad(7\text{-k})$$
$$\text{NEU-260-Auftrag A–D: definiert}\quad\checkmark[K/M]\qquad(7\text{-l})$$

---

## 8. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-258 | 1fa3745 | $W_{\rm NEU-252}=W_{\rm Lit}$ |
| NEU-257 (Patch) | f710da3 | Kato $\times[M]$; $\mathcal{H}_W\cong\ell^2$ |
| NEU-252 (Patch) | 4ee78ed | $B_W$-Blockformeln |
| NEU-250-Serie | div. | $\Lambda(p^k)/\sqrt{p^k}$ aus BC/Frobenius |
| Suzuki 2026 | Thm.~1.1, Abstract, Conj. | $A_a$, $\mathcal{H}(T_a)$, $\overline{\mathscr{D}}_{a,\theta}$, $W(a,\theta;z)$, $\phi$-Vermutung |
| Suzuki 2011/2025 | Thm.~2.1 | $\mathcal{H}_W\cong L^2(\tau)$ unter RH |
| von Neumann | — | sa. Erweiterungen, Defizit $(1,1)$ |
| Kato 1966 | — | Friedrichs-Erweiterung |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2: $\lambda(a)$ als Gauge abgestuft; $\phi(a,z)$ ergänzt; $J_{a,b}$ als originale Hypothese markiert; NEU-260 A–D definiert.*
