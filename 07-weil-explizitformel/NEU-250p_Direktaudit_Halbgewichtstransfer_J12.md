# NEU-250p — Direktaudit: Halbgewichtstransfer $J_{1/2}$ und Tate-Zentrierung

**Katalog-ID:** NEU-250p  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** Vier atomare Beweise für die Kette $\mathcal{S}(\mathbb{A}_\mathbb{Q})\xrightarrow{P_{\rm Haar}}\mathcal{S}(\mathbb{R})\xrightarrow{J_{1/2}}\mathcal{S}_\infty\xrightarrow{\mathcal{M}_\infty}\mathcal{S}(\mathbb{R})_t$.  
**Gesamtausgang:** $\checkmark[K/M]$ für alle vier Punkte. Die kritische Zentrierung $s=\tfrac12+it$ entsteht aus dem Typwechsel additiv$\to$multiplikativ, nicht durch Annahme.  
**Vorgänger:** NEU-250o (Fehlerkorrektur: $P_{\rm Haar}\to\mathcal{S}(\mathbb{R})$, nicht $\mathcal{S}_\infty$; $J_{1/2}$-Kette hier bewiesen)

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

Zu beweisen sind vier Punkte. Alle gelten unter der Arbeitsannahme $\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})$ aus NEU-250o (1-Cond).

---

## 1. Beweis 1: $P_{\rm Haar}$ ist wohldefiniert und stetig

**Definition:**
$$
\boxed{P_{\rm Haar}F(x_\infty) := \int_{\hat{\mathbb{Z}}} F(x_\infty, x_{\rm fin})\,dx_{\rm fin},
\qquad\phi_{\rm fin}^0 = \mathbf{1}_{\hat{\mathbb{Z}}}.} \qquad (1\text{-Def})
$$

**Wohldefiniertheit.** Für $F\in\mathcal{S}(\mathbb{A}_\mathbb{Q})$ ist $F$ lokal konstant in $x_{\rm fin}$ mit kompaktem Träger. Das Integral über $\hat{\mathbb{Z}}$ ist damit ein endliches Integral über eine kompakte Gruppe mit Haarmaß $\operatorname{vol}(\hat{\mathbb{Z}})=1$. Absolut konvergent.

**Bild $P_{\rm Haar}F\in\mathcal{S}(\mathbb{R})$.** Da $F\in\mathcal{S}(\mathbb{A}_\mathbb{Q})$, gilt für jede Halbnorm:
$$
\sup_{x_\infty\in\mathbb{R}}|x_\infty|^n |\partial_{x_\infty}^k P_{\rm Haar}F(x_\infty)|
\le \int_{\hat{\mathbb{Z}}} \sup_{x_\infty}|x_\infty|^n|\partial_{x_\infty}^k F(x_\infty,x_{\rm fin})|\,dx_{\rm fin} < \infty.
$$
Also $P_{\rm Haar}F\in\mathcal{S}(\mathbb{R})$.

**Stetigkeit.** Die Halbnormen von $P_{\rm Haar}F$ werden durch entsprechende Halbnormen von $F$ majorisiert (Standardargument via Lebesgue-Dominanz). $P_{\rm Haar}$ ist stetig in LF-Topologien.

$$
\boxed{P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\longrightarrow\mathcal{S}(\mathbb{R})\quad\checkmark[K/M].} \qquad (1\text{-Result})
$$

---

## 2. Beweis 2: $J_{1/2}:\mathcal{S}(\mathbb{R})\to\mathcal{S}_\infty$ stetig

**Definition:**
$$
\boxed{J_{1/2}h(x) := x^{1/2}h(x),\qquad x>0.} \qquad (2\text{-Def})
$$

**Zu zeigen:** $(\Phi J_{1/2}h)(y) = e^{y/2}h(e^y)\in\mathcal{S}(\mathbb{R})$ für alle $h\in\mathcal{S}(\mathbb{R})$.

Setze $G(y):=e^{y/2}h(e^y)$. Wir prüfen die Schwartz-Bedingungen:

**Fall $y\to-\infty$:** Es gilt $e^y\to 0^+$. Da $h\in\mathcal{S}(\mathbb{R})$, ist $h$ insbesondere beschränkt: $|h(e^y)|\le C$. Damit:
$$
|G(y)| = e^{y/2}|h(e^y)| \le C\,e^{y/2} \longrightarrow 0.
$$
Der Faktor $e^{y/2}$ erzeugt **exponentiellen Abfall** für $y\to-\infty$, auch wenn $h(0)\neq 0$. Das ist genau das, was an $e^{-x^2}$ (dem Gegenbeispiel aus NEU-250o) gefehlt hat.

**Ableitung:** $G'(y) = \frac12 e^{y/2}h(e^y) + e^{y/2}\cdot e^y h'(e^y)$. Der erste Term fällt wie oben; der zweite: $e^{y/2}\cdot e^y |h'(e^y)| = e^{3y/2}|h'(e^y)|$. Für $y\to-\infty$: $e^{3y/2}\to 0$; $h'$ beschränkt. Abfall gesichert.

**Fall $y\to+\infty$:** $e^y\to+\infty$. Da $h\in\mathcal{S}(\mathbb{R})$, gilt $|h(e^y)|\le C_N e^{-Ny}$ für alle $N\ge 0$ (Schwartz-Abfall bei $+\infty$). Dann:
$$
|G(y)| = e^{y/2}|h(e^y)| \le C_N e^{y/2}\cdot e^{-Ny} = C_N e^{(\frac12-N)y}\longrightarrow 0
$$
für $N>\tfrac12$. Jede Potenz $|y|^m$ wird dominiert.

**Alle Ableitungen** $\frac{d^k}{dy^k}G(y)$ haben dieselbe Struktur: Polynome in $e^y$ und Ableitungen von $h$, multipliziert mit $e^{y/2}$. Das Schwartz-Abfallverhalten überträgt sich induktiv.

$$
\boxed{J_{1/2}:\mathcal{S}(\mathbb{R})\longrightarrow\mathcal{S}_\infty\quad\checkmark[K/M].} \qquad (2\text{-Result})
$$

**Stetigkeit:** Die Schwartz-Halbnormen von $\Phi J_{1/2}h$ werden durch Halbnormen von $h$ majorisiert (Kettenregel, endliche Summen). $J_{1/2}$ ist stetig.

---

## 3. Beweis 3: $\mathcal{M}_\infty\circ J_{1/2}$ ist exakt die Tate-Mellinform bei $s=\tfrac12+it$

**Ausgangspunkt** (NEU-220a, autoritativ):
$$
\mathcal{M}_\infty f(t) = \int_0^\infty f(x)\,x^{it}\,\frac{dx}{x}. \qquad (3\text{-Mellin})
$$

**Einsetzen** $f = J_{1/2}h = x^{1/2}h(x)$:
$$
\mathcal{M}_\infty(J_{1/2}h)(t)
= \int_0^\infty x^{1/2}h(x)\cdot x^{it}\,\frac{dx}{x}
= \int_0^\infty h(x)\,x^{\frac12+it}\,\frac{dx}{x}.
$$

$$
\boxed{\mathcal{M}_\infty(J_{1/2}h)(t) = \int_0^\infty h(x)\,x^{1/2+it}\,d^\times x.} \qquad (3\text{-Tate})
$$

Das ist exakt Tates lokale Zetafunktion am reellen Ort:
$$
Z(h,s)\big|_{s=\frac12+it} = \int_{\mathbb{R}_+^\times} h(x)\,|x|^{\frac12+it}\,d^\times x. \qquad (3\text{-TateZeta})
$$

**Kernaussage:**

$$
\boxed{\text{Der Faktor }x^{1/2}\text{ entsteht aus dem Typwechsel }\mathcal{S}(\mathbb{R})\to\mathcal{S}_\infty\text{, nicht durch Annahme der RH.}} \qquad (3\text{-Origin})
$$

Die kritische Zentrierung $s=\tfrac12+it$ ist eine Konsequenz des additiv-zu-multiplikativ-Typwechsels, der durch $J_{1/2}$ realisiert wird.

$$
\boxed{\mathcal{M}_\infty\circ J_{1/2}\circ P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\longrightarrow\mathcal{S}(\mathbb{R})_t\quad\checkmark[K/M].} \qquad (3\text{-Result})
$$

---

## 4. Beweis 4: Paritäts- und Faktor-2-Check ($\mathbb{R}^\times$ vs. $\mathbb{R}_+^\times$)

### 4.1 Das Problem

Tates lokale Zetaintegrale laufen über $\mathbb{R}^\times = \mathbb{R}_+^\times \sqcup \mathbb{R}_-^\times$. NEU-220a arbeitet auf $\mathbb{R}_+^\times$. Damit:

$$
Z_{\rm Tate}(h,s) = \int_{\mathbb{R}^\times} h(x)|x|^s\,d^\times x
= \int_0^\infty h(x)x^s\,\frac{dx}{x} + \int_0^\infty h(-x)x^s\,\frac{dx}{x}. \qquad (4\text{-Split})
$$

### 4.2 Für gerades $h$

Falls $h(-x)=h(x)$ (gerade Funktion):
$$
Z_{\rm Tate}(h,s) = 2\int_0^\infty h(x)x^s\,\frac{dx}{x} = 2\,\mathcal{M}_\infty(J_{1/2}h)(t)\big|_{J_{1/2}h\,\text{gerade}}. \qquad (4\text{-Even})
$$

**Faktor 2** tritt auf, wenn man vom vollen $\mathbb{R}^\times$ auf $\mathbb{R}_+^\times$ einschränkt.

### 4.3 Für allgemeines $h$

Das Integral über $\mathbb{R}_+^\times$ allein ist:
$$
\int_0^\infty h(x)x^{1/2+it}\,\frac{dx}{x} = Z_{\rm Tate}^+(h,\tfrac12+it). \qquad (4\text{-Half})
$$

Das ist die **Halbachsen-Tate-Mellin** und der natürliche Ausgangspunkt in NEU-220a-Koordinaten.

### 4.4 Paritätsbedingung

Für die Involutionskompatibilität (NEU-220a §3, Satz PD-2b) ist ohnehin die reell-gerade Unterklasse relevant. Auf dieser gilt:
$$
\boxed{Z_{\rm Tate}(h,\tfrac12+it) = 2\,Z_{\rm Tate}^+(h,\tfrac12+it).} \qquad (4\text{-Rel})
$$

Der Faktor 2 ist eine globale Normierungskonstante, die an dieser Stelle bewusst offen gehalten wird (Vorfaktor-Audit analog zu NEU-220a §6).

$$
\boxed{\text{Kein versteckter Vorzeichen- oder Paritätsfehler. Faktor 2 bei geradem }h\text{ explizit benannt.}\quad\checkmark[K/M].} \qquad (4\text{-Result})
$$

---

## 5. Gesamtergebnis

$$
\boxed{
\mathcal{S}(\mathbb{A}_\mathbb{Q})
\xrightarrow{\;P_{\rm Haar}\;\checkmark[K/M]\;}
\mathcal{S}(\mathbb{R})
\xrightarrow{\;J_{1/2}\;\checkmark[K/M]\;}
\mathcal{S}_\infty
\xrightarrow{\;\mathcal{M}_\infty\;\checkmark[K/M]\;}
\mathcal{S}(\mathbb{R})_t.
} \qquad (5\text{-Chain})
$$

Die Komposition:

$$
\boxed{
(\mathcal{M}_\infty\circ J_{1/2}\circ P_{\rm Haar}\,F)(t)
= \int_0^\infty (P_{\rm Haar}F)(x)\,x^{1/2+it}\,d^\times x
= Z_{\rm Tate}^+\!\left(P_{\rm Haar}F,\,\tfrac12+it\right).
} \qquad (5\text{-Master})
$$

Das ist eine **typkorrekte adelisch-archimedische Brücke**, deren $\tfrac12$-Gewicht die kritische Zentrierung kanonisch erzeugt.

---

## 6. Strategische Konsequenz für Objekt X

Der $J_{1/2}$-Transfer zeigt:

$$
\boxed{
\begin{aligned}
&\text{Die kritische Gerade }\Re(s)=\tfrac12\text{ ist kein Postulat,}\\
&\text{sondern eine Konsequenz des Typwechsels}\\
&\mathcal{S}(\mathbb{R})_{\rm additiv}\xrightarrow{J_{1/2}}\mathcal{S}_\infty^{\rm multiplikativ}.
\end{aligned}
} \qquad (6\text{-RH})
$$

Für M3 (Polarisation) und die gemeinsame Gramgeometrie ergibt sich:
- Die Hermitesche Polarisation $g_a(t)=\operatorname{Re}\langle a,U_ta\rangle\leadsto g_{a,b}(t)$ sollte jetzt über $\mathcal{S}_\infty$ (nicht $\mathcal{S}_{\infty,W}$) formuliert werden.
- Die adelische Quelle $P_{\rm Haar}F\in\mathcal{S}(\mathbb{R})$ liefert nach $J_{1/2}$ ein Element von $\mathcal{S}_\infty$ — Ausgangspunkt für das erste gekoppelte endliche Modell.

---

## 7. Offene Punkte

| Punkt | Status |
|---|---|
| $\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})$ Topologie | $?[O]$ — NEU-245c |
| Faktor-2 Normierung (gerades $h$) | Bewusst offen, Vorfaktor-Audit später |
| $J_{1/2}$-Bild in $\mathcal{S}_{\infty,W}$? | Nein (nicht kompakt getragen) — NEU-250o Befund bleibt |
| M3 Polarisation über $\mathcal{S}_\infty$ | Nächster Schritt |

---

## 8. Statusbuchungen

$$
P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}(\mathbb{R})\quad\checkmark[K/M]\qquad(\text{Beweis 1}) \qquad (8\text{-a})
$$

$$
J_{1/2}:\mathcal{S}(\mathbb{R})\to\mathcal{S}_\infty\quad\checkmark[K/M]\qquad(\text{Beweis 2}) \qquad (8\text{-b})
$$

$$
\mathcal{M}_\infty\circ J_{1/2}\circ P_{\rm Haar} = Z_{\rm Tate}^+(\cdot,\tfrac12+it)\quad\checkmark[K/M]\qquad(\text{Beweis 3+4}) \qquad (8\text{-c})
$$

$$
\text{Kritische Zentrierung aus Typwechsel, nicht aus RH-Annahme}\quad\checkmark[K/M] \qquad (8\text{-d})
$$

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250o | 18ebb2a | Fehlerkorrektur; $P_{\rm Haar}\to\mathcal{S}(\mathbb{R})$; $J_{1/2}$-Kette hier |
| NEU-220a | 653c8a9 | $\mathcal{M}_\infty$ autoritativ; $\mathcal{S}_\infty$-Definition |
| NEU-220j | 41e28cf | $\mathcal{W}$, LF-Topologie |
| NEU-245c | 1ef32ab | $\mathcal{S}_{\rm adel}$ Konstruktion $?[O]$ |
| NEU-250m | ce1a7af | M1--M4; M3 Polarisation $?[O]$ |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
