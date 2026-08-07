# NEU-250p — Direktaudit: Halbgewichtstransfer $J_{1/2}$ und Tate-Zentrierung

**Katalog-ID:** NEU-250p  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** Vier atomare Beweise für die Kette $\mathcal{S}(\mathbb{A}_\mathbb{Q})\xrightarrow{P_{\rm Haar}}\mathcal{S}(\mathbb{R})\xrightarrow{J_{1/2}}\mathcal{S}_\infty\xrightarrow{\mathcal{M}_\infty}\mathcal{S}(\mathbb{R})_t$. Zusätzlich: $J_\alpha$-Familie und Weil-Selbstdualität.  
**Gesamtausgang:** $\checkmark[K/M]$ für Beweise 1–4. Alte (8-d) $\times[M]$; neue (8-d-korr): Typkorrektheit $(\alpha>0)$ + Weil-Selbstdualität $\Rightarrow\alpha=\tfrac12$ $\checkmark[K/M]$.  
**Vorgänger:** NEU-250o (Fehlerkorrektur: $P_{\rm Haar}\to\mathcal{S}(\mathbb{R})$; $J_{1/2}$-Kette hier bewiesen)

---

## 0. Die Kette

$$
\boxed{
\mathcal{S}(\mathbb{A}_\mathbb{Q})
\xrightarrow{\;P_{\rm Haar}\;}
\mathcal{S}(\mathbb{R})
\xrightarrow{\;J_{1/2}\;}
\mathcal{S}_\infty
\xrightarrow{\;\mathcal{M}_\infty\;}
\mathcal{S}(\mathbb{R})_t.
} \qquad (0\text{-Chain})
$$

Arbeitsannahme: $\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})$ (NEU-250o, 1-Cond).

---

## 1. Beweis 1: $P_{\rm Haar}$ wohldefiniert und stetig

$$
\boxed{P_{\rm Haar}F(x_\infty) := \int_{\hat{\mathbb{Z}}} F(x_\infty, x_{\rm fin})\,dx_{\rm fin}.} \qquad (1\text{-Def})
$$

Für $F\in\mathcal{S}(\mathbb{A}_\mathbb{Q})$ ist das Integral absolut konvergent ($\hat{\mathbb{Z}}$ kompakt, $\operatorname{vol}(\hat{\mathbb{Z}})=1$). Jede Schwartz-Halbnorm von $P_{\rm Haar}F$ wird durch entsprechende Halbnormen von $F$ majorisiert.

$$
\boxed{P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\longrightarrow\mathcal{S}(\mathbb{R})\quad\checkmark[K/M].} \qquad (1\text{-Result})
$$

---

## 2. Beweis 2: $J_\alpha$-Familie und $J_{1/2}:\mathcal{S}(\mathbb{R})\to\mathcal{S}_\infty$ stetig

### 2.1 Allgemeine $J_\alpha$-Familie

**Definition:**
$$
\boxed{J_\alpha h(x) := x^\alpha h(x),\qquad x>0,\quad\alpha>0.} \qquad (2\text{-Def})
$$

**Satz:** Für jedes $\alpha>0$ gilt $J_\alpha:\mathcal{S}(\mathbb{R})\to\mathcal{S}_\infty$ stetig.

*Beweis.* Setze $G_\alpha(y):=(\Phi J_\alpha h)(y)=e^{\alpha y}h(e^y)$.

- **$y\to-\infty$:** $|G_\alpha(y)|=e^{\alpha y}|h(e^y)|\le C\,e^{\alpha y}\to 0$ (da $\alpha>0$ und $h$ beschränkt). Exponentieller Abfall für **alle** $\alpha>0$.
- **$y\to+\infty$:** $|h(e^y)|\le C_N e^{-Ny}$ für alle $N\ge 0$ (Schwartz-Abfall). Also $|G_\alpha(y)|\le C_N e^{(\alpha-N)y}\to 0$ für $N>\alpha$.
- **Ableitungen:** Induktiv: $\frac{d^k}{dy^k}G_\alpha(y)$ ist eine endliche Summe von Termen $e^{(\alpha+j)y}h^{(j)}(e^y)$ ($0\le j\le k$), alle Schwartz. $\square$

$$
\boxed{J_\alpha:\mathcal{S}(\mathbb{R})\longrightarrow\mathcal{S}_\infty\quad\checkmark[K/M]\quad\text{für alle }\alpha>0.} \qquad (2\text{-Result})
$$

### 2.2 Konsequenz für (8-d) der ersten Fassung

Da $J_\alpha\to\mathcal{S}_\infty$ für **alle** $\alpha>0$ funktioniert, erzwingt der Typwechsel $\mathcal{S}(\mathbb{R})\to\mathcal{S}_\infty$ allein nur $\alpha>0$, nicht $\alpha=\tfrac12$.

$$
\boxed{\text{Alte (8-d): }\alpha=\tfrac12\text{ folgt allein aus dem Typwechsel}\quad\times[M].} \qquad (2\text{-NoGo})
$$

---

## 3. Beweis 3: $\mathcal{M}_\infty\circ J_\alpha = Z_{\rm Tate}^+(\cdot,\alpha+it)$

**Einsetzen** $f=J_\alpha h$ in die autoritative Mellin-Formel (NEU-220a):

$$
\mathcal{M}_\infty(J_\alpha h)(t)
=\int_0^\infty x^\alpha h(x)\cdot x^{it}\,\frac{dx}{x}
=\int_0^\infty h(x)\,x^{\alpha+it}\,\frac{dx}{x}.
$$

$$
\boxed{\mathcal{M}_\infty(J_\alpha h)(t) = Z_{\rm Tate}^+(h,\alpha+it)
:= \int_0^\infty h(x)\,x^{\alpha+it}\,d^\times x.} \qquad (3\text{-Tate})
$$

Hinweis: $Z_{\rm Tate}^+$ bezeichnet den **positiven Halbachsenanteil** von Tates lokaler Zeta-Funktion (nur $\mathbb{R}_+^\times$, nicht volles $\mathbb{R}^\times$). Die vollständige Tate-Zeta läuft über $\mathbb{R}^\times$ und ergibt bei geradem $h$ einen zusätzlichen Faktor 2 (siehe Beweis 4).

Damit:

$$
\boxed{(\mathcal{M}_\infty\circ J_\alpha\circ P_{\rm Haar}\,F)(t)
= Z_{\rm Tate}^+(P_{\rm Haar}F,\,\alpha+it).\quad\checkmark[K/M].} \qquad (3\text{-Result})
$$

---

## 4. Beweis 4: Parität und Faktor-2-Check ($\mathbb{R}^\times$ vs.\ $\mathbb{R}_+^\times$)

Tates lokale Zetafunktion am reellen Ort:
$$
Z_{\rm Tate}(h,s) = \int_{\mathbb{R}^\times}h(x)|x|^s\,d^\times x
= \int_0^\infty h(x)x^s\,d^\times x + \int_0^\infty h(-x)x^s\,d^\times x. \qquad (4\text{-Split})
$$

Für **gerades $h$** (d.h.\ $h(-x)=h(x)$; die Geradheitsbedingung gilt für $h$, nicht für $J_\alpha h$, da letzteres nur auf $x>0$ definiert ist):
$$
\boxed{Z_{\rm Tate}(h,s)=2\,Z_{\rm Tate}^+(h,s)\quad\text{für gerades }h.} \qquad (4\text{-Even})
$$

Faktor 2 ist eine Normierungskonstante; kein Vorzeichen- oder Paritätsfehler. Vorfaktor-Audit analog NEU-220a §6 bewusst offen gehalten.

$$
\boxed{\text{Kein versteckter Vorzeichen- oder Paritätsfehler.}\quad\checkmark[K/M].} \qquad (4\text{-Result})
$$

---

## 5. Selektion $\alpha=\tfrac12$ durch Weil-Selbstdualität

### 5.1 Ausgangspunkt: Weil-Symmetrie aus NEU-220a

NEU-220a (Satz PD-2d, autoritativ) fixiert:
$$
\boxed{s\longleftrightarrow 1-s \qquad\Longleftrightarrow\qquad t\longleftrightarrow -t.} \qquad (5\text{-Weil})
$$

Diese Symmetrie ist bekannt und unabhängig von RH.

### 5.2 Invarianzbedingung

Nimm allgemein $s=\alpha+it$ mit $\alpha>0$ fest. Unter $s\mapsto 1-s$:
$$
1-s = (1-\alpha)-it.
$$

Die vertikale Linie $\Re s=\alpha$ wird auf die Linie $\Re s=1-\alpha$ abgebildet. Sie ist genau dann **invariant** unter der Weil-Symmetrie, wenn
$$
\alpha = 1-\alpha,
$$
also:
$$
\boxed{\alpha = \tfrac12.} \qquad (5\text{-Fix})
$$

### 5.3 Was das bedeutet

Der archimedische Port $\mathcal{M}_\infty\circ J_\alpha\circ P_{\rm Haar}$ wertet auf der Linie $\Re s=\alpha+it$ aus. Damit er mit der bekannten Weil-Symmetrie $s\mapsto 1-s$ kompatibel ist — d.h.\ der Port selbst auf einer selbstdualen Linie zentriert ist — muss $\alpha=\tfrac12$ gewählt werden.

### 5.4 Was das nicht bedeutet

Dieser Schritt beweist **nicht** die Riemann-Hypothese. Die Funktionalgleichung und die Symmetrieachse $\Re s=\tfrac12$ sind bekannt. Wir erklären hier nur, warum unser archimedischer Port, wenn er Weil-kompatibel sein soll, genau bei $\alpha=\tfrac12$ zentriert werden muss. Ob die Nullstellen auf dieser Achse liegen, bleibt offen.

### 5.5 Neue Buchung (ersetzt alte (8-d))

$$
\boxed{\text{Typkorrektheit }(\alpha>0)+\text{Weil-Selbstdualität }(s\mapsto1-s)\;\Longrightarrow\;\alpha=\tfrac12.\quad\checkmark[K/M].} \qquad (5\text{-Result})
$$

Oder kompakt:
$$
\boxed{\text{Typkorrektheit }+\text{Selbstdualität}\;\Longrightarrow\;\alpha=\tfrac12.} \qquad (8\text{-d-korr})
$$

---

## 6. Gesamtergebnis

$$
\boxed{
\mathcal{S}(\mathbb{A}_\mathbb{Q})
\xrightarrow{\;P_{\rm Haar}\;\checkmark[K/M]\;}
\mathcal{S}(\mathbb{R})
\xrightarrow{\;J_{1/2}\;\checkmark[K/M]\;}
\mathcal{S}_\infty
\xrightarrow{\;\mathcal{M}_\infty\;\checkmark[K/M]\;}
\mathcal{S}(\mathbb{R})_t.
} \qquad (6\text{-Chain})
$$

Masterformel:
$$
\boxed{
(\mathcal{M}_\infty\circ J_{1/2}\circ P_{\rm Haar}\,F)(t)
= Z_{\rm Tate}^+\!\left(P_{\rm Haar}F,\,\tfrac12+it\right)
= \int_0^\infty (P_{\rm Haar}F)(x)\,x^{1/2+it}\,d^\times x.
} \qquad (6\text{-Master})
$$

**Warum $\alpha=\tfrac12$, präzise:**

$$
\boxed{
\begin{aligned}
&\text{Der Typwechsel }\mathcal{S}(\mathbb{R})\xrightarrow{J_\alpha}\mathcal{S}_\infty\text{ erlaubt alle }\alpha>0.\\
&\text{Die Weil-Symmetrie }s\mapsto1-s\text{ (NEU-220a, PD-2d) selektiert eindeutig }\alpha=\tfrac12.\\
&\tfrac12\text{ ist der einzige selbstduale Wert innerhalb der typkorrekten Familie }J_\alpha.
\end{aligned}
} \qquad (6\text{-Why})
$$

---

## 7. Offene Punkte

| Punkt | Status |
|---|---|
| $\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})$ Topologie | $?[O]$ — NEU-245c |
| Faktor-2 Normierung (gerades $h$) | Bewusst offen, Vorfaktor-Audit später |
| $J_{1/2}$-Bild in $\mathcal{S}_{\infty,W}$? | Nein (nicht kompakt getragen) — NEU-250o |
| M3 Polarisation über $\mathcal{S}_\infty$ | Nächster Schritt |

---

## 8. Statusbuchungen

$$
P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}(\mathbb{R})\quad\checkmark[K/M]\qquad(\text{Beweis 1}) \qquad (8\text{-a})
$$

$$
J_\alpha:\mathcal{S}(\mathbb{R})\to\mathcal{S}_\infty\quad\checkmark[K/M]\quad\forall\,\alpha>0\qquad(\text{Beweis 2}) \qquad (8\text{-b})
$$

$$
\mathcal{M}_\infty\circ J_\alpha\circ P_{\rm Haar} = Z_{\rm Tate}^+(\cdot,\alpha+it)\quad\checkmark[K/M]\qquad(\text{Beweis 3+4}) \qquad (8\text{-c})
$$

$$
\boxed{\text{Alte (8-d): }\alpha=\tfrac12\text{ aus Typwechsel allein}\quad\times[M].} \qquad (8\text{-d-alt, zurückgezogen})
$$

$$
\boxed{\text{(8-d-korr): Typkorrektheit }(\alpha>0)+\text{Weil-Selbstdualität}\;\Rightarrow\;\alpha=\tfrac12\quad\checkmark[K/M].} \qquad (8\text{-d-korr})
$$

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250o | 18ebb2a | Fehlerkorrektur; $P_{\rm Haar}\to\mathcal{S}(\mathbb{R})$; $J_{1/2}$-Kette hier |
| NEU-220a | 653c8a9 | $\mathcal{M}_\infty$ autoritativ; $\mathcal{S}_\infty$-Definition; Weil-Symmetrie PD-2d |
| NEU-220j | 41e28cf | $\mathcal{W}$, LF-Topologie |
| NEU-245c | 1ef32ab | $\mathcal{S}_{\rm adel}$ Konstruktion $?[O]$ |
| NEU-250m | ce1a7af | M1--M4; M3 Polarisation $?[O]$ |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2026-08-07: (8-d) $\times[M]$; $J_\alpha$-Familie $\forall\alpha>0$; Weil-Selbstdualität selektiert $\alpha=\tfrac12$ $\checkmark[K/M]$; $Z_{\rm Tate}^+$ klargestellt; Geradheitsbedingung auf $h$ bezogen.*
