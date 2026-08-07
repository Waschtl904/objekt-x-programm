# NEU-259 — Direktaudit des finite-Intervall-Grenzwertwegs als Objekt-X-Träger

**Katalog-ID:** NEU-259  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** Fünf atomare Fragen zum Finite-Intervall-Grenzwertweg (Suzuki 2026). Strenge Trennung Satz/Vermutung. Identifikation des BC/Adelen-Eintrittspunkts.  
**Patch:** Zwei Suzuki-Ebenen explizit getrennt ($A_a$ vs. $\overline{\mathscr{D}}_{a,\theta}$); korrekte Kette $Q_W^a\to A_a\to T_{a,\lambda}\to\mathcal{H}(T_a)\to\overline{\mathscr{D}}_{a,\theta}$; $\sigma(A_a)\to\{\gamma_n\}$ $\times[M]$ (falsche Ebene); Objekt-X-Hypothese auf $\{\mathcal{H}(T_{a,\lambda(a)}),J_{a,b},\overline{\mathscr{D}}_{a,\theta(a)}\}$ präzisiert; drei freie Daten $\lambda(a),\theta(a),J_{a,b}$ als NEU-260-Auftrag.  
**Vorgänger:** NEU-258 $\checkmark$, NEU-257 (Patch), NEU-252 (Patch), NEU-250-Serie  
**Nachfolger:** NEU-260 (Arithmetische Kanonisierung der Suzuki-Daten $\lambda(a),\theta(a),J_{a,b}$)

---

## 0. Motivation und Diagramm

NEU-257 $\checkmark[K/M]$: $H_0=L^2(\mathbb{R})$ ist nicht der Weil-Abschlussraum. Suzuki 2026 liefert für jedes $a>0$ RH-frei einen selbstadjungierten Operator $A_a$ und — in einem zweiten Schritt — einen Hilbert-Pólya-artigen first-order Operator $\overline{\mathscr{D}}_{a,\theta}$. Die Gesamtkette:

$$
\boxed{ \mathcal{H}_a \quad\xrightarrow[a\to\infty]{\ ?\ }\quad \mathcal{K}_X \quad\xrightarrow[\mathrm{RH}]{\sim}\quad \mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma). } \qquad (0\text{-Diag})
$$

**Objekt X** (revidierte Kernhypothese nach Patch):
$$
\boxed{\left\{\mathcal{H}(T_{a,\lambda(a)}),\;J_{a,b},\;\overline{\mathscr{D}}_{a,\theta(a)}\right\}_{0<a<b},} \qquad (0\text{-Sys})
$$
mit arithmetisch bestimmten kanonischen Daten $\lambda(a)$, $\theta(a)$, $J_{a,b}$.

**Doppelte Aufgabe:** Suzuki liefert die Operatorhülle; BC/Adelen sollen die arithmetische Kanonizität der freien Daten $\lambda(a),\theta(a),J_{a,b}$ erklären.

---

## 0b. Zwei Suzuki-Ebenen (Patch)

$\times[M]$ **Vorherige Fassung:** $\sigma(A_a)\to\{\gamma_n\}$ als Suzuki-Vermutung eingetragen.

**Korrekte Zwei-Ebenen-Struktur nach Suzuki 2026:**

| Ebene | Objekt | Status | Bezug zu $\{\gamma_n\}$ |
|---|---|---|---|
| **Ebene 1** | $Q_W^a$, $A_a$, $\mathcal{H}(T_{a,\lambda})$ | $\checkmark$ **Satz** (RH-frei) | keiner direkt |
| **Ebene 2** | $\overline{\mathscr{D}}_{a,\theta}$ auf $\mathcal{H}(T_{a,\lambda})$ | $\checkmark$ **Satz** (sa. Erweiterung, RH-frei) | $\sigma(\overline{\mathscr{D}}_{a,\theta})$: reelle Nullstellen von $W(a,\theta;z)$ |
| **Grenzwert** | $\overline{\mathscr{D}}_{a,\theta(a)}\xrightarrow{a\to\infty}D_X$ | $\mathbf{Vermutung}$ | $\sigma(D_X)=\{\gamma_n\}$ |

**Korrekte Kette:**
$$
\boxed{Q_W^a\longrightarrow A_a\longrightarrow T_{a,\lambda}:=A_a-\lambda I\longrightarrow\mathcal{H}(T_{a,\lambda})\longrightarrow\overline{\mathscr{D}}_{a,\theta}.} \qquad (0\text{-Chain})
$$

**$A_a$ ist nicht Suzukis conjecturaler Hilbert-Pólya-Operator:**
$$
\boxed{A_a\;\neq\;\text{Suzukis conjecturaler Hilbert-Pólya-Operator.}\quad\times[M]\text{ (Vorfassung)}} \qquad (0\text{-notHP})
$$

Der conjecturale Grenzoperator mit $\sigma=\{\gamma_n\}$ ist ein first-order Operator $D_X$, der aus $\overline{\mathscr{D}}_{a,\theta(a)}$ im Limes entsteht.

---

## Frage 1 — RH-freie Existenz: Vollständige Kette

### 1.1 Ebene 1: $Q_W^a$, $A_a$ (Satz)

Für jedes $a>0$ ist $Q_W^a$ auf $L^2(-a,a)$ semibeschränkt und abschließbar (Kompaktintervall regularisiert; kein Widerspruch zu NEU-257). Die Friedrichs-Erweiterung:
$$
\boxed{A_a=A_a^*\ge-\lambda_a I\text{ auf }L^2(-a,a),\quad\lambda_a:=\inf\sigma(A_a)>-\infty,\quad\text{diskretes Spektrum.}\quad\checkmark\text{ (Satz)}} \qquad (1\text{-Aa})
$$

### 1.2 Ebene 1: $T_{a,\lambda}$ und $\mathcal{H}(T_{a,\lambda})$ (Satz)

Für $\lambda<\lambda_a$: $T_{a,\lambda}:=A_a-\lambda I>0$. Vervollständigung von $C_c^\infty(-a,a)$ bezüglich
$$
\|v\|_{T_{a,\lambda}}^2:=Q_W^a(v,v)-\lambda\|v\|_{L^2(-a,a)}^2=\langle T_{a,\lambda}^{1/2}v,T_{a,\lambda}^{1/2}v\rangle_{L^2}: \qquad (1\text{-Norm})
$$
$$
\boxed{\mathcal{H}(T_{a,\lambda}):=\overline{C_c^\infty(-a,a)}^{\|\cdot\|_{T_{a,\lambda}}}\quad\text{wohldefinierter Hilbertraum.}\quad\checkmark\text{ (Satz)}} \qquad (1\text{-HTa})
$$

**$\lambda$-Abhängigkeit:** $\mathcal{H}(T_{a,\lambda})$ hängt von der Wahl $\lambda<\lambda_a$ ab. Verschiedene $\lambda$ ergeben im Allgemeinen verschiedene (aber topologisch äquivalente) Hilberträume. Kanonische Wahl von $\lambda(a)$: $?[O]\to$ NEU-260.

### 1.3 Ebene 2: $\overline{\mathscr{D}}_{a,\theta}$ auf $\mathcal{H}(T_{a,\lambda})$ (Satz)

Auf $\mathcal{H}(T_{a,\lambda})$ betrachtet Suzuki
$$
\mathscr{D}_a=i\frac{d}{dx}\quad\text{(Defizienzindizes }(1,1)\text{ auf }\mathcal{H}(T_{a,\lambda})). \qquad (1\text{-Da})
$$

Für jeden Parameter $\theta\in[0,2\pi)$ existiert genau eine selbstadjungierte Erweiterung:
$$
\boxed{\overline{\mathscr{D}}_{a,\theta}=\overline{\mathscr{D}}_{a,\theta}^*\quad\text{auf }\mathcal{H}(T_{a,\lambda}).\quad\checkmark\text{ (Satz, von-Neumann-Erweiterungstheorie)}} \qquad (1\text{-Dbar})
$$

Deren Spektrum: reelle Nullstellen der charakteristischen Funktion $W(a,\theta;z)$.

### 1.4 Freie Daten

$$
\boxed{\text{Drei freie Daten ohne zusätzliche Struktur: }\lambda(a)<\lambda_a,\quad\theta(a)\in[0,2\pi),\quad J_{a,b}.} \qquad (1\text{-Free})
$$

---

## Frage 2 — Identifikation $B_W|_{C_c^\infty(-a,a)}\stackrel{?}{=}Q_W^a$

### 2.1 Stand nach NEU-258

NEU-258 $\checkmark[K/M]$: $W_{\rm NEU-252}=W_{\rm Lit}$ (alle Normierungsfaktoren). Suzuki definiert $Q_W^a$ explizit als die Weil-Explizitformel lokalisiert auf $C_c^\infty(-a,a)$ mit identischer Fourierkonvention.

Damit folgt für Gamma- und Primblock direkt:
$$
(B_\Gamma+B_{\rm fin})|_{C_c^\infty(-a,a)}=Q_{W,\Gamma+\rm fin}^a.\quad\checkmark[K/M] \qquad (2\text{-GamFin})
$$

### 2.2 Polterm-Vergleich

**Zu klären:** Suzukis endlicher Polbeitrag $Q_{W,\rm pole}^a$ enthalt möglicherweise Randterme, die im globalen $B_{\rm pole}$ nicht auftreten (da $B_{\rm pole}$ auf $C_c^\infty(\mathbb{R})$ definiert ist, ohne Randeffekte). Der Vergleich:
$$
B_{\rm pole}|_{C_c^\infty(-a,a)}\stackrel{?}{=}Q_{W,\rm pole}^a\quad?[O]\text{ (Polterm-Randaudit)} \qquad (2\text{-Pole})
$$

**Vermutung:** Da Suzuki $Q_W^a$ als direkte Restriktion der Weil-Quadratik beschreibt und NEU-258 alle Faktoren identifiziert, ist $(2\text{-Pole})$ sehr wahrscheinlich $\checkmark$, muss aber gegen Suzukis genaue Polterm-Definition auditiert werden, bevor hart gebucht.

$$
B_W|_{C_c^\infty(-a,a)}=Q_W^a\quad?[O]\text{ (offen bis Polterm-Randaudit)} \qquad (2\text{-Final})
$$

---

## Frage 3 — Satz vs. Vermutung im Grenzwert $a\to\infty$ (revidiert)

| Aussage | Status | Objekt |
|---|---|---|
| $Q_W^a$ semibeschränkt, abschließbar auf $L^2(-a,a)$ | $\checkmark$ **Satz** | Ebene 1 |
| $A_a=A_a^*$, diskretes Spektrum | $\checkmark$ **Satz** | Ebene 1 |
| $T_{a,\lambda}>0$, $\mathcal{H}(T_{a,\lambda})$ Hilbertraum | $\checkmark$ **Satz** | Ebene 1 |
| $\overline{\mathscr{D}}_{a,\theta}=\overline{\mathscr{D}}_{a,\theta}^*$ auf $\mathcal{H}(T_{a,\lambda})$ | $\checkmark$ **Satz** | Ebene 2 |
| $\sigma(A_a)\to\{\gamma_n\}$ | $\times[M]$ **falsche Ebene** | — |
| $\overline{\mathscr{D}}_{a,\theta(a)}\xrightarrow{a\to\infty}D_X$, $\sigma(D_X)=\{\gamma_n\}$ | $\mathbf{Vermutung}$ | Ebene 2, Grenzwert |
| Kanonische $J_{a,b}:\mathcal{H}(T_a)\to\mathcal{H}(T_b)$ | $?[O]$ **offen** | Formtopologie |
| $\mathcal{K}_X=\varinjlim_a\mathcal{H}(T_a)$ kanonisch | $?[O]$ **offen** | — |

$$
\boxed{\text{Satz-Bereich: alle endlichen Konstruktionen.}\quad\text{Vermutungs-Bereich: Grenzwert und Nullstellenspektrum.}} \qquad (3\text{-Split})
$$

---

## Frage 4 — Kanonische Übergangsabbildungen

### 4.1 $L^2$-Ebene: kanonisch $\checkmark$

Suzuki verwendet ausdrücklich:
$$
\boxed{L^2(-a,a)\hookrightarrow L^2(-b,b)\quad\text{durch Nullfortsetzung, kanonisch.}\quad\checkmark\text{ (Satz, Suzuki 2026)}} \qquad (4\text{-L2Emb})
$$

Die $J_{a,b}$ auf $L^2$-Ebene sind also bereits gelöst.

### 4.2 $\mathcal{H}(T_{a,\lambda})$-Ebene: offen

Die Formtopologie $\|\cdot\|_{T_{a,\lambda}}$ ist stärker als $\|\cdot\|_{L^2(-a,a)}$. Die Nullfortsetzungseinbettung aus $(4\text{-L2Emb})$ ist bezüglich $\|\cdot\|_{T_{b,\lambda}}$ im Allgemeinen nicht isometrisch (Randterme, $\lambda$-Abhängigkeit):
$$
\boxed{J_{a,b}^{\mathcal{H}}:\mathcal{H}(T_{a,\lambda(a)})\to\mathcal{H}(T_{b,\lambda(b)})\text{ kanonisch}:\quad?[O]\to\text{NEU-260}} \qquad (4\text{-HEmb})
$$

### 4.3 $\overline{\mathscr{D}}_{a,\theta}$-Ebene: offen

Kompatibilität der first-order Erweiterungen unter $J_{a,b}^{\mathcal{H}}$ (Intertwining $J_{a,b}^{\mathcal{H}}\overline{\mathscr{D}}_{a,\theta(a)}\sim\overline{\mathscr{D}}_{b,\theta(b)}J_{a,b}^{\mathcal{H}}$):
$$
\text{Operator-Kompatibilität }J_{a,b}^{\mathcal{H}}\text{ mit }\overline{\mathscr{D}}_{a,\theta(a)}:\quad?[O]\to\text{NEU-260} \qquad (4\text{-OpComp})
$$

---

## Frage 5 — BC/Adelen-Eintrittspunkt (präzisiert)

### 5.1 Drei freie Daten, drei Eintrittspunkte

$$
\boxed{\text{BC/KMS/Hecke}\longrightarrow\lambda(a),\;\theta(a),\;J_{a,b}.} \qquad (5\text{-BC})
$$

| Datum | Beschreibung | BC-Eintrittspunkt | Status |
|---|---|---|---|
| $\lambda(a)$ | Untere Schranke für $T_{a,\lambda}=A_a-\lambda I>0$; Formtopologie-Skalierung | KMS-Zustand / Energie | $?[O]\to$NEU-260 |
| $\theta(a)$ | Parameter der sa. Erweiterung $\overline{\mathscr{D}}_{a,\theta}$; Randbedingung | Frobenius/Hecke-Phasenselektion | $?[O]\to$NEU-260 |
| $J_{a,b}$ | Übergangsabbildung $\mathcal{H}(T_a)\to\mathcal{H}(T_b)$; Kompatibilitätsstruktur | Adelische Multiplikation / Dilatation | $?[O]\to$NEU-260 |

### 5.2 Was die NEU-250-Serie bereits liefert

Aus NEU-250-Serie $\checkmark[K/M]$: $\Lambda(p^k)/\sqrt{p^k}$ aus BC/Frobenius/Nakayama (Eintrittspunkt E1: Vorfaktor in $Q_W^a$). Das erklärt noch nicht, warum $\lambda(a)$, $\theta(a)$, $J_{a,b}$ arithmetisch kanonisch sind.

### 5.3 Strategische Kette

$$
\boxed{\underbrace{\text{BC/Adelen}}_{\text{arithm. Herkunft}}\xrightarrow{\lambda(a),\theta(a),J_{a,b}}\underbrace{\{\mathcal{H}(T_{a,\lambda(a)}),\overline{\mathscr{D}}_{a,\theta(a)},J_{a,b}\}_{a<b}}_{\text{Objekt X}}\xrightarrow{\text{RH}}\underbrace{\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)}_{\text{Weil-Hilbertraum}}.} \qquad (5\text{-Chain})
$$

---

## 6. Offene Punkte und Prioritäten

$$B_W|_{C_c^\infty(-a,a)}=Q_W^a\text{ (Polterm-Randaudit)}\quad?[O]\qquad(6\text{-a})$$
$$\text{Exakte }\lambda_a\text{-Abhängigkeit von }a\quad?[O]\qquad(6\text{-b})$$
$$\text{Kanonische }\lambda(a)\text{ aus BC/KMS}\quad?[O]\to\text{NEU-260}\qquad(6\text{-c})$$
$$\text{Kanonische }\theta(a)\text{ aus Frobenius/Hecke}\quad?[O]\to\text{NEU-260}\qquad(6\text{-d})$$
$$J_{a,b}^{\mathcal{H}}:\mathcal{H}(T_a)\to\mathcal{H}(T_b)\text{ kanonisch (Formtopologie)}\quad?[O]\to\text{NEU-260}\qquad(6\text{-e})$$
$$\text{Operator-Kompatibilität }J_{a,b}^{\mathcal{H}}\text{ mit }\overline{\mathscr{D}}_{a,\theta(a)}\quad?[O]\to\text{NEU-260}\qquad(6\text{-f})$$
$$\overline{\mathscr{D}}_{a,\theta(a)}\xrightarrow{a\to\infty}D_X,\;\sigma(D_X)=\{\gamma_n\}\quad\mathbf{Vermutung}\qquad(6\text{-g})$$
$$\mathcal{K}_X=\varinjlim_a\mathcal{H}(T_{a,\lambda(a)})\quad?[O]\qquad(6\text{-h})$$

---

## 7. Statusbuchungen

$$Q_W^a\text{ semibeschränkt, abschließbar auf }L^2(-a,a)\quad\checkmark[K/M]\text{ (Suzuki 2026)}\qquad(7\text{-a})$$
$$A_a=A_a^*,\text{ diskretes Spektrum, Friedrichs}\quad\checkmark[K/M]\qquad(7\text{-b})$$
$$T_{a,\lambda}>0,\;\mathcal{H}(T_{a,\lambda})\text{ Hilbertraum}\quad\checkmark[K/M]\qquad(7\text{-c})$$
$$\overline{\mathscr{D}}_{a,\theta}=\overline{\mathscr{D}}_{a,\theta}^*\text{ auf }\mathcal{H}(T_{a,\lambda})\quad\checkmark[K/M]\qquad(7\text{-d})$$
$$A_a\neq\text{conjecturaler Hilbert-Pólya-Operator}\quad\times[M]\qquad(7\text{-e})$$
$$\sigma(A_a)\to\{\gamma_n\}\quad\times[M]\text{ (falsche Ebene)}\qquad(7\text{-f})$$
$$\overline{\mathscr{D}}_{a,\theta(a)}\to D_X,\;\sigma(D_X)=\{\gamma_n\}\quad\mathbf{Vermutung}\text{ (Suzuki 2026)}\qquad(7\text{-g})$$
$$L^2(-a,a)\hookrightarrow L^2(-b,b)\text{ durch Nullfortsetzung kanonisch}\quad\checkmark[K/M]\qquad(7\text{-h})$$
$$J_{a,b}^{\mathcal{H}}:\mathcal{H}(T_a)\to\mathcal{H}(T_b)\quad?[O]\to\text{NEU-260}\qquad(7\text{-i})$$
$$(B_\Gamma+B_{\rm fin})|_{C_c^\infty(-a,a)}=Q_{W,\Gamma+\rm fin}^a\quad\checkmark[K/M]\qquad(7\text{-j})$$
$$B_{\rm pole}|_{C_c^\infty(-a,a)}=Q_{W,\rm pole}^a\quad?[O]\text{ (Randaudit)}\qquad(7\text{-k})$$
$$\text{Drei freie Daten }\lambda(a),\theta(a),J_{a,b}\text{: BC-Kanonisierungsauftrag}\quad?[O]\to\text{NEU-260}\qquad(7\text{-l})$$
$$\text{Objekt X }=\{\mathcal{H}(T_{a,\lambda(a)}),J_{a,b},\overline{\mathscr{D}}_{a,\theta(a)}\}\text{: revidierte Kernhypothese}\quad?[O]\qquad(7\text{-m})$$

---

## 8. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-258 | 1fa3745 | $W_{\rm NEU-252}=W_{\rm Lit}$ $\checkmark$ |
| NEU-257 (Patch) | f710da3 | Kato/KLMN $\times[M]$; $\mathcal{H}_W\cong\ell^2$ |
| NEU-252 (Patch) | 4ee78ed | $B_W$-Blockformeln M3 |
| NEU-250-Serie | div. | $\Lambda(p^k)/\sqrt{p^k}$ aus BC/Frobenius |
| Suzuki 2026 | Thm.~1.1, Abstract, \S{}2 | $Q_W^a$, $A_a$, $T_{a,\lambda}$, $\mathcal{H}(T_a)$, $\overline{\mathscr{D}}_{a,\theta}$; Grenzwertvermutung |
| Suzuki 2011/2025 | (1.2), Thm.~2.1 | $\mathcal{H}_W\cong L^2(\tau)$ unter RH |
| von Neumann | — | Selbstadjungierte Erweiterungen, Defizienzindizes |
| Kato 1966 | — | Friedrichs-Erweiterung |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch: zwei Suzuki-Ebenen getrennt; $\sigma(A_a)\to\{\gamma_n\}$ $\times[M]$; Objekt-X-Hypothese $(0\text{-Sys})$ auf $\{\mathcal{H}(T_{a,\lambda(a)}),J_{a,b},\overline{\mathscr{D}}_{a,\theta(a)}\}$ präzisiert; drei freie Daten als NEU-260-Auftrag.*
