# NEU-220o — Randflucht, Resolvententreue und erweiterter Polkanal

**Katalog-ID:** NEU-220o  
**Knoten:** [O-220-1-PD5a3f2-boundary-escape-and-resolvent-fidelity]  
**Vorgänger:** NEU-220n (Commit 6bbfd22) — Fensteroperatoren ✓[K/M]  
**Status:** ✓[K/M]_part (PD5a3f2a–e) / ?[O] (PD5a3f2f–g)

---

## Auditprotokoll NEU-220n → NEU-220o

NEU-220n hatte die fünf Hindernisse für den globalen Grenzoperator korrekt isoliert, aber einen sechsten No-go-Befund offen gelassen:

> **Randflucht:** Der Poloperator $B_{\mathrm{pole},R}$ konvergiert stark-resolventen gegen $0$, während seine Testfunktionsform exakt zum nichtverschwindenden $q_{\mathrm{pole}}$ stabilisiert.

Dieser Befund zeigt, dass **starke Resolventenkonvergenz kein treuer Grenzbegriff für die Weil-Form ist** und den erweiterten Randkanal zum mathematisch notwendigen nächsten Schritt macht.

---

## PD5a3f2a — Exakte Formstabilisierung ✓[M]

Für $a, b \in C_c^\infty(\mathbb{R})$ existiert $R_0 > 0$ mit $\operatorname{supp}(a), \operatorname{supp}(b) \subseteq [-R_0,R_0]$. Für alle $R \ge R_0$ gilt kanalweise:

- **Polterm:** $\ell_\pm|_{\mathcal{H}_R}$ sind für $R \ge R_0$ konstant (Nullfortsetzung verändert die Integrale nicht).
- **Primterm:** Nur $n$ mit $\log n \le \operatorname{diam}(\operatorname{supp}(a))$ tragen bei; das ist $R$-unabhängig.
- **Gammaterm:** Die Fourierform der nullfortgesetzten Funktion hängt nicht von $R$ ab.

$$
\boxed{\mathfrak{W}_R(a,b) = \mathfrak{W}(a,b) \qquad \text{für alle }R \ge R_0.}
$$

Die Fensterfamilie besitzt daher einen exakten Grenzwert im LF-Sinn:

$$
\mathfrak{W} = \varinjlim_R \mathfrak{W}_R \quad \text{auf } C_c^\infty(\mathbb{R}).
$$

Das ist **stärker als punktweise asymptotische Konvergenz**, liefert aber noch keinen globalen selbstadjungierten Operator.

---

## PD5a3f2b — Exakter Spektralaudit des Polfensters ✓[M]

Auf $\mathcal{H}_R = L^2([-R,R])$ sei

$$
e_{+,R}(u) = \mathbf{1}_{[-R,R]}(u)\,e^{u/2}, \qquad e_{-,R}(u) = \mathbf{1}_{[-R,R]}(u)\,e^{-u/2}.
$$

Dann

$$
\|e_{\pm,R}\|^2 = \int_{-R}^R e^{\pm u}\,du = 2\sinh R,
\qquad
\langle e_{-,R}, e_{+,R}\rangle = \int_{-R}^R 1\,du = 2R.
$$

Der Gram-Block von $B_{\mathrm{pole},R} = |e_{-,R}\rangle\langle e_{+,R}| + |e_{+,R}\rangle\langle e_{-,R}|$ auf $\operatorname{span}\{e_{-,R},e_{+,R}\}$ lautet (nach Normierung):

$$
M_R = \begin{pmatrix} 0 & \langle e_{-,R},e_{+,R}\rangle \\ \langle e_{+,R},e_{-,R}\rangle & 0 \end{pmatrix}
= \begin{pmatrix} 0 & 2R \\ 2R & 0 \end{pmatrix}.
$$

Die tatsächlichen Eigenwerte von $B_{\mathrm{pole},R}$ erhält man aus dem nicht orthonormierten Paar $(e_{-,R},e_{+,R})$; mit $G = \begin{pmatrix}2\sinh R & 2R\\ 2R & 2\sinh R\end{pmatrix}$ als Gram-Matrix und $A = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ lautet das verallgemeinerte Eigenwertproblem $Ac = \lambda Gc$. Die beiden nicht-trivialen Eigenwerte sind:

$$
\boxed{\lambda_{+,R} = 2\sinh R + 2R, \qquad \lambda_{-,R} = 2R - 2\sinh R.}
$$

**Wachstum:**

$$
\|B_{\mathrm{pole},R}\| = \lambda_{+,R} = 2\sinh R + 2R \sim e^R,
\qquad
\inf\sigma(B_{\mathrm{pole},R}) = \lambda_{-,R} \sim -e^R.
$$

Somit läuft **sowohl** die Operatornorm **als auch** die untere Schranke exponentiell gegen $\pm\infty$. Uniforme semibeschränkte Formmethoden für die Polfenstersequenz sind damit blockiert.

---

## PD5a3f2c — Randflucht: Spektralprojektionen konvergieren stark gegen 0 ✓[M]

Die normierten Eigenvektoren zu $\lambda_{\pm,R}$ sind Linearkombinationen von $e_{+,R}$ und $e_{-,R}$, die sich an den Fensterrändern $\pm R$ konzentrieren. Für festes $f \in L^2(\mathbb{R})$ gilt

$$
\langle f, e_{\pm,R}\rangle_{L^2} = \int_{-R}^R f(u)\,e^{\pm u/2}\,du \;\longrightarrow\; \int_{\mathbb{R}} f(u)\,e^{\pm u/2}\,du
$$

nur, wenn das letzte Integral konvergiert — was für allgemeines $f \in L^2$ **nicht gilt**. Tatsächlich sind die **normierten** Vektoren $(2\sinh R)^{-1/2}e_{\pm,R}$ schwach gegen $0$ konvergent (da $\|e_{\pm,R}\| \sim e^{R/2}$). Daher:

$$
Q_R := P_{+,R} + P_{-,R} \longrightarrow 0 \quad \text{stark in } L^2(\mathbb{R}).
$$

Für die Resolvente ($z \in \mathbb{C}\setminus\mathbb{R}$):

$$
(B_{\mathrm{pole},R}-z)^{-1} = -\frac{1}{z}(I-Q_R)
+ \frac{1}{\lambda_{+,R}-z}P_{+,R}
+ \frac{1}{\lambda_{-,R}-z}P_{-,R}.
$$

Da $|\lambda_{\pm,R}| \to \infty$ und $P_{\pm,R} \to 0$ stark:

$$
\boxed{B_{\mathrm{pole},R} \longrightarrow 0 \quad \text{in starker Resolventenkonvergenz}.}
$$

---

## PD5a3f2d — No-go-Satz: Starke Resolventenkonvergenz ist nicht formtreu ✓[M]_neg

Gleichzeitig gilt für alle $a, b \in C_c^\infty(\mathbb{R})$ und alle $R \ge R_0$:

$$
\langle a, B_{\mathrm{pole},R}\, b\rangle_{\mathcal{H}_R} = \overline{\ell_-(a)}\,\ell_+(b) + \overline{\ell_+(a)}\,\ell_-(b) = q_{\mathrm{pole}}(a,b) \ne 0 \text{ im Allgemeinen}.
$$

Der Wert ist $R$-stabil, aber der Resolventengrenzwert ist $0$. Das ergibt:

$$
\boxed{\begin{gathered}
B_{\mathrm{pole},R} \xrightarrow{\mathrm{s.r.}} 0,\\
\text{aber } \langle a, B_{\mathrm{pole},R}\, b\rangle \to q_{\mathrm{pole}}(a,b) \ne 0.
\end{gathered}}
$$

**Mechanismus:** Die Randzustände $e_{\pm,R}$ "fliehen" mit wachsendem $R$ nach $\pm\infty$. Die Resolvente sieht nur die Lücke zwischen den entweichenden Eigenwerten, nicht den Testfunktionsbeitrag.

**Konsequenz:**

$$
\boxed{\text{Starke Resolventenkonvergenz allein ist kein treuer Grenzbegriff für die Weil-Form.}}
$$

Naive starke Resolventenkonvergenz von $W_R$ zu benutzen und zu behaupten, der Grenzwert realisiere $\mathfrak{W}$, ist damit als **gesperrter Beweisweg** klassifiziert (✓[M]_neg).

---

## PD5a3f2e — Zwei verschiedene Grenzprobleme ✓[K/M]

| Problem | Aussage | Status |
|---------|---------|--------|
| **Formgrenze** | $\mathfrak{W}_R(a,b) \to \mathfrak{W}(a,b)$ auf $C_c^\infty$ | ✓[M] (exakt, ab $R_0$) |
| **Operatorgrenze** | $\exists W$ selbstadjungiert mit $\langle a,Wb\rangle = \mathfrak{W}(a,b)$ und $W_R \xrightarrow{\mathrm{s.r.}} W$ | ?[O] |

Die Operatorgrenze **benötigt** zusätzlich zur Resolventenkonvergenz den Nachweis, dass der Grenzwert die stabilisierten Testfunktionsmatrixelemente erhält. Genau das ist durch Randflucht des Polterms nicht automatisch.

---

## PD5a3f2f — Natuerlicher Randkanal: Pontryagin-(1,1)-Komponente ✓[K/M]

Der Polterm besitzt eine kanonische endliche Darstellung ohne Randflucht. Setze

$$
L_\partial a = \begin{pmatrix}\ell_-(a)\\ \ell_+(a)\end{pmatrix} \in \mathbb{C}^2,
\qquad
J_\partial = \begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Dann

$$
\boxed{q_{\mathrm{pole}}(a,b) = \langle L_\partial a,\, J_\partial L_\partial b\rangle_{\mathbb{C}^2}.}
$$

$J_\partial$ ist selbstadjungiert mit Signatur $(1,1)$: Der Randkanal ist eine **Pontryagin-Komponente** vom Typ $\Pi_1$. Auf $\mathcal{H}_R$ ist $L_{\partial,R}$ beschränkt; auf $L^2(\mathbb{R})$ ist $L_\partial$ unbeschränkt, aber auf $C_c^\infty$ wohldefiniert.

### Erweiterter Fensterraum

Anstelle des divergierenden Rang-2-Operators in $[-R,R]$ sollte der Polkanal als **fester expliziter Randkanal** im erweiterten Raum

$$
\boxed{\mathcal{H}_R^{\mathrm{ext}} = \mathcal{H}_R \oplus \mathbb{C}^2}
$$

geführt werden. Der erweiterte Fensteroperator lautet dann

$$
W_R^{\mathrm{ext}} = G_{\infty,R} \oplus 0_{\mathbb{C}^2} + B_{\mathrm{fin},R} \oplus 0 + J_{\partial}\text{-Kopplung},
$$

wobei die $J_\partial$-Kopplung durch die Randfunktionale $L_\partial$ vermittelt wird. Dann können die Randzustände beim Grenzübergang $R\to\infty$ **nicht nach $\pm\infty$ entweichen**, weil sie im festen $\mathbb{C}^2$-Kanal verankert sind.

---

## PD5a3f2g — Sechstes Hindernis und offene Konstruktion ?[O]

Die in NEU-220n benannten fünf Hindernisse werden um das sechste ergänzt:

| Nr. | Hindernis | Ursache |
|-----|-----------|---------|
| 1 | Fehlende $R$-unabh. untere Schranke | $\inf\sigma(B_{\mathrm{pole},R}) \sim -e^R$ |
| 2 | Normwachstum Polblock | $\|B_{\mathrm{pole},R}\| \sim e^R$ |
| 3 | Normwachstum Primblock | Wächst mit $\pi(e^{2R})$ |
| 4 | Keine starke Resolventenkonvergenz (naiv) | $B_{\mathrm{pole},R} \xrightarrow{\mathrm{s.r.}} 0 \ne q_{\mathrm{pole}}$ |
| 5 | Positivität des Grenzobjekts | Wäre RH-stark |
| **6** | **Randflucht** | **Resolventenkonvergenz löscht nicht-$L^2$-stetige Formanteile aus** |

Der nächste Konstruktionsschritt ist die vollständige Realisierung von $W_R^{\mathrm{ext}}$ auf $\mathcal{H}_R^{\mathrm{ext}} = \mathcal{H}_R \oplus \mathbb{C}^2$ mit Nachweis:
1. $W_R^{\mathrm{ext}}$ ist selbstadjungiert auf $\mathcal{H}_R^{\mathrm{ext}}$ (im Krein- oder Pontryagin-Sinn).
2. $\langle (a,L_\partial a), W_R^{\mathrm{ext}}(b,L_\partial b)\rangle = \mathfrak{W}(a,b)$ für $a,b \in C_c^\infty((-R,R))$.
3. Unter geeignetem direktem Limes $R\to\infty$ bleibt der $\mathbb{C}^2$-Kanal erhalten.

---

## Knotentabelle

| Teilaufgabe | Inhalt | Status |
|-------------|--------|--------|
| PD5a3f2a | Exakte Formstabilisierung auf $C_c^\infty$ | ✓[M] |
| PD5a3f2b | Spektralaudit $\lambda_{\pm,R} = 2\sinh R \pm 2R$, Normwachstum $\sim e^R$ | ✓[M] |
| PD5a3f2c | $Q_R \to 0$ stark; $B_{\mathrm{pole},R} \xrightarrow{\mathrm{s.r.}} 0$ | ✓[M] |
| PD5a3f2d | No-go: s.r.-Konvergenz nicht formtreu | ✓[M]_neg (gesperrter Beweisweg) |
| PD5a3f2e | Zwei Grenzprobleme getrennt: Formgrenze (✓[M]) vs. Operatorgrenze (?[O]) | ✓[K/M] |
| PD5a3f2f | Pontryagin-(1,1)-Randkanal; erweiterter Raum $\mathcal{H}_R^{\mathrm{ext}}$ | ✓[K/M] |
| PD5a3f2g | Sechstes Hindernis; $W_R^{\mathrm{ext}}$-Konstruktion | ?[O] |

```
[O-220-1-PD5a3f2-boundary-escape-and-resolvent-fidelity]
  → ✓[K/M]_part  (PD5a3f2a–f abgeschlossen)
  → ?[O]          (PD5a3f2g: W_R^ext Konstruktion und globaler Limes)
```

---

## Strategische Konsequenz

$$
\boxed{\text{Die Fensteroperatoren approximieren die Weil-Form exakt auf dem Testkern,}
\text{ aber der naive Resolventengrenzwert kann Randinformation verlieren.}}
$$

Der erweiterte Randkanal $\mathcal{H}_R^{\mathrm{ext}} = \mathcal{H}_R \oplus \mathbb{C}^2$ ist damit keine optionale Variante, sondern der **mathematisch notwendige nächste Schritt** zur randkanaltreuen Grenzwertbildung.

---

## Abhängigkeiten

| Referenz | Inhalt |
|----------|--------|
| NEU-220n (6bbfd22) | Fensteroperatoren $(\mathcal{H}_R,W_R)$, fünf Hindernisse |
| NEU-220m rev.2 (bf2445a) | Korrekte Gesamtpolarisation, Typklassifikation |
| NEU-220l (ddac5ff) | Weil-Quadratik, Amplitudenraum |
| Connes (1999) | Spurformel, BC-Kern |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
