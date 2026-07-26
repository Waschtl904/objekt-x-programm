# NEU-123.D — Paritätskorrigierte Dreifachsumme und Diagonaldrift-Test

**Stand:** 5. Juli 2026  
**Anschluss:** NEU-123.C (Dreifachsumme $T_N$, naive HL-Heuristik $T_N \asymp N^3$)  
**Nächste Einheit:** NEU-123.E (Minimalunterbau $T_N \gg N^{3/2+\varepsilon}$ streng oder numerisch; Zentrierungssuche)

---

## 123.D.0 — Ausgangspunkt

Aus NEU-123.C gilt:

$$
\frac{a_{1,N}}{b_{1,N}} = \frac{T_N}{S_N^{3/2}},
\qquad S_N = \sum_{k \leq N}\Lambda(k)^2 \sim N\log N.
$$

Mit der Schichtzelegung $h = |n-m|$:

$$
T_N = 2\sum_{h=2}^{N}\Lambda(h)\,C_h(N-h),
\qquad
C_h(X) := \sum_{m \leq X} m\,\Lambda(m)\,\Lambda(m+h).
$$

Die Diagonaldrift-Frage ist:

$$
\boxed{T_N \gg S_N^{3/2} \sim N^{3/2}(\log N)^{3/2} \;?}
$$

**Status: \(\checkmark[M]\) als Reduktion (aus NEU-123.C)**

---

## 123.D.1 — Paritätskorrektur der naiven Heuristik

Die naive Heuristik $T_N \asymp N^3$ aus NEU-123.C setzt implizit voraus, dass **alle** Shifts $h \leq N$ einen Primpaar-Hauptterm liefern. Das ist falsch.

**Lokale Paritätsregel:** Für die Primpaarkorrelation
$$
\sum_{m \leq X}\Lambda(m)\,\Lambda(m+h)
$$
gilt: Ist $h$ ungerade, so sind $m$ und $m+h$ von verschiedener Parität. Beide können nicht zugleich ungerade Primzahlen sein. Ein Hauptterm entsteht nur für **gerade** $h$.

Da zusätzlich $\Lambda(h) \neq 0$ benötigt wird, sind die geraden Hauptterm-Shifts genau

$$
h = 2^r \quad (r \geq 1),
$$

denn die einzigen geraden Primzahlpotenzen sind Zweierpotenzen. Damit ist der primäre Hauptterm von $T_N$ **nicht** gleichmäßig über alle $h \leq N$ verteilt, sondern konzentriert auf die dünne Menge

$$
\{2^r : 1 \leq r \leq \lfloor\log_2 N\rfloor\}.
$$

**Status: \(\checkmark[M]\)**

> **Bemerkung:** Zusätzliche Beiträge kommen von geraden zusammengesetzten Shifts $h = 2k$ mit $k$ zusammengesetzt (z.B. $h = 6, 10, \ldots$), aber $\Lambda(h) = 0$ für alle nicht-primzahlpotenz $h$. Damit sind nur $h = 2^r$ relevant.

---

## 123.D.2 — Paritätskorrigierte HL-Heuristik

Beschränke auf $h = 2^r$ mit $\Lambda(2^r) = \log 2$. Für gerade Shifts $h$ gibt die HL-Mittelwertvermutung:

$$
C_h(X) = \sum_{m \leq X} m\,\Lambda(m)\,\Lambda(m+h)
\sim \frac{1}{2}\,\mathfrak{S}(h)\,X^2.
$$

Für $h = 2^r$ hat die Singulärreihenkonstante die Form

$$
\mathfrak{S}(2^r) = 2C_2 \asymp 1,
$$

da keine ungeraden Primteiler in $h$ auftreten und die Eulerfaktoren für $p \nmid h$ sich zu einer absolut konvergenten Konstante zusammensetzen. Damit:

$$
C_{2^r}(N - 2^r) \asymp (N - 2^r)^2 \asymp N^2.
$$

Der Beitrag aller Zweierpotenz-Shifts:

$$
T_N \asymp (\log 2)\sum_{r=1}^{\lfloor\log_2 N\rfloor} N^2
= (\log 2)\cdot\lfloor\log_2 N\rfloor \cdot N^2
\asymp N^2 \log N.
$$

Damit:

$$
\frac{T_N}{S_N^{3/2}} \asymp \frac{N^2 \log N}{N^{3/2}(\log N)^{3/2}}
= \sqrt{\frac{N}{\log N}} \;\longrightarrow\; +\infty.
$$

$$
\boxed{\text{Paritätskorrigierte Heuristik: }\frac{a_{1,N}}{b_{1,N}} \asymp \sqrt{\frac{N}{\log N}} \to +\infty.}
$$

Fall II bleibt bestehen — aber mit kleinerer Skala als in NEU-123.C erwartet.

**Korrektur gegenüber NEU-123.C:**

| Version | $T_N$ Heuristik | $a_{1,N}/b_{1,N}$ |
|---------|-----------------|--------------------|
| NEU-123.C (naive HL) | $\asymp N^3$ | $\asymp N^{3/2}/(\log N)^{3/2}$ |
| NEU-123.D (paritätskorrigiert) | $\asymp N^2 \log N$ | $\asymp \sqrt{N/\log N}$ |

Beide divergieren. Die qualitative Diagnose **Fall II** bleibt unverändert.  
**Status: \(\warning[M]\) heuristisch; HL-abhängig**

---

## 123.D.3 — Unbedingter Minimalbeitrag

Ohne jede Heuristik existieren Beiträge der Form
$m = 2^r$, $h = 2^r$, $m+h = 2^{r+1}$:

$$
\Lambda(2^r)\,\Lambda(2^r)\,(1+2^r)\,\Lambda(2^r) = (\log 2)^3\,(1+2^r).
$$

Daraus:

$$
T_N \geq c\sum_{r\,:\,2^{r+1} \leq N} 2^r = c\left(\frac{N}{2} - 1\right) \gg N.
$$

Das ist eine **bedinungslose** untere Schranke, aber zu schwach für die Diagonaldrift:

$$
N \ll N^{3/2}(\log N)^{3/2}.
$$

**Status: \(\checkmark[M]\) — echter Unterbeitrag, nicht entscheidend**

---

## 123.D.4 — Das eigentliche Minimalziel

Für die Diagonaldrift-Barriere genügt bereits:

$$
\boxed{T_N \gg N^{3/2+\varepsilon} \quad\text{für irgendein }\varepsilon > 0.}
$$

Denn dann:

$$
\frac{T_N}{S_N^{3/2}} \gg \frac{N^{3/2+\varepsilon}}{N^{3/2}(\log N)^{3/2}}
= \frac{N^\varepsilon}{(\log N)^{3/2}} \longrightarrow +\infty.
$$

Eine hinreichende Form wäre der Sparse-Shift-Test:

$$
\sum_{r=1}^{\lfloor\log_2 N\rfloor} C_{2^r}(N-2^r) \gg N^{3/2+\varepsilon}.
$$

Dies ist eine **Primpaarkorrelationsaussage über Zweierpotenz-Shifts** — deutlich schwächer als volle HL-Vermutung.

> **Warum das schwerer ist als es aussieht:** Die Korrelation $\sum_{m \leq X}\Lambda(m)\Lambda(m+2^r)$ ist für **jeden festen** Shift $2^r$ bedingt unbewiesen (Goldbach-artig). Was man kennt, sind Mittelwertaussagen über $h$ (Vinogradov, Goldston–Yıldırım), nicht Einzelschift-Asymptotik.

**Status: ?[O]**

---

## 123.D.5 — Was man ohne HL beweisen kann

Ohne Primpaar-Vermutungen sind folgende Schranken bekannt oder erreichbar:

| Methode | Ergebnis | Reicht für Drift? |
|---------|----------|--------------------|
| Trivialschranke (D.3) | $T_N \gg N$ | Nein |
| Cauchy-Schwarz auf $C_h$ | $T_N \gg N \cdot \|\Lambda\|_2^2 \sim N^2\log N$ | Ja, wenn erreichbar |
| Vinogradov-Mittelwert über $h$ | $\sum_{h \leq H} C_h(X) \gg H \cdot X^2$ (HL im Mittel) | Ja, für Mittelwert |
| Einzelshift $h = 2$ | Unbewiesene Twingold-Primheuristik | Nein |

Der vielversprechendste Ansatz ohne volle HL ist der **Mittelwert über $h$**: Für
$$
\sum_{h \leq H} \sum_{m \leq X} m\,\Lambda(m)\,\Lambda(m+h),
$$
kann man mit Vinogradov-Methoden und dem Primzahlsatz in arithmetischen Progressionen einen Hauptterm der Form $\Theta(H \cdot X^2)$ erwarten. Eingeschränkt auf $H = \log N$ Zweierpotenz-Shifts wäre das $\Theta(N^2 \log N)$ — der paritätskorrigierte HL-Wert.

**Status: ?[O] — kein bedingungsloser Beweis; Vinogradov-Mittelwert als Kandidat**

---

## 123.D.6 — Konsequenz bei Bestätigung (Fall II)

Falls $T_N/S_N^{3/2} \to +\infty$, dann $\tilde{a}_{1,N} \to +\infty$. Die reine Offdiagonal-Renormierung
$$
\widetilde{A}_N = b_{1,N}^{-1}\,A_N^{Jac,-}
$$
scheitert am Diagonalterm. Da $\operatorname{Tr}(A_N^{Jac,-}) = 0$ (NEU-87), liefert das Spurmittel $c_N = 0$ — keine zusätzliche Information.

Die Suche nach einer intrinsischen Zentrierung $c_N \neq 0$ aus der Feshbach-Blockstruktur ist damit die nächste Aufgabe (NEU-123.E).  
**Status: ?[O]**

---

## 123.D.7 — Falls das Minimalziel scheitert (Fall I reopen)

Falls man nur $T_N = O(S_N^{3/2})$ findet, wäre $a_{1,N}/b_{1,N}$ beschränkt — arithmetisch überraschend, da es starke Dünnheit der Zweierpotenz-Shift-Korrelationen verlangen würde. In diesem Fall:
- Rückkehr zu NEU-123.B
- Prüfung $b_{2,N}/b_{1,N}$ via viertem Moment $\mu_{4,N}$
- Entscheidung Fall I vs. Fall III

**Status: ?[O] — unwahrscheinliches Szenario, aber methodisch offen**

---

## 123.D.F — Fazit

NEU-123.D korrigiert die naive Heuristik aus NEU-123.C:

$$
T_N \asymp N^3 \quad\text{(NEU-123.C, zu groß)} \qquad\longrightarrow\qquad T_N \asymp N^2\log N \quad\text{(NEU-123.D, paritätskorrigiert).}
$$

Die qualitative Diagnose ändert sich nicht:

$$
\frac{T_N}{S_N^{3/2}} \asymp \sqrt{\frac{N}{\log N}} \longrightarrow +\infty.
$$

$$
\boxed{\text{Fall II: Diagonaldrift-Barriere — heuristisch stark gestützt, paritätskorrigiert.}}
$$

Streng benötigt man nicht volle HL-Vermutung, sondern nur:

$$
\boxed{T_N \gg N^{3/2+\varepsilon} \quad\text{für ein }\varepsilon > 0.}
$$

Unbedingt gesichert ist nur $T_N \gg N$ (Zweierpotenzbeitrag).

### Statusmatrix

| Punkt | Aussage | Status |
|-------|---------|--------|
| Paritätskorrektur ($h$ ungerade blockiert) | \(\checkmark[M]\) | |
| Zweierpotenz-Hauptterm-Heuristik $T_N \asymp N^2\log N$ | \(\warning[M]\) HL | |
| Triviale untere Schranke $T_N \gg N$ | \(\checkmark[M]\) | |
| Minimalziel $T_N \gg N^{3/2+\varepsilon}$ (streng) | ?[O] | |
| Operator-Fall II ($\tilde{a}_{1,N} \to +\infty$) | ?[O] streng; \(\warning[M]\) heuristisch | |

---

## 123.D.N — Nächste Aufgaben (NEU-123.E)

**Priorität 1:** Vinogradov-Mittelwertansatz für $\sum_{r} C_{2^r}(N-2^r) \gg N^{3/2+\varepsilon}$.

**Priorität 2:** Falls Priorität 1 scheitert: numerische Auswertung von $T_N/S_N^{3/2}$ für $N = 100, 1000, 10000$.

**Priorität 3:** Suche intrinsische Zentrierung $c_N$ aus Feshbach-Blockstruktur (falls Fall II bestätigt).

---

## Verweise

- NEU-123.C: Naive Heuristik $T_N \asymp N^3$; Kernidentität $a_{1,N}/b_{1,N} = T_N/S_N^{3/2}$
- NEU-123.B: Renormierungsbarriere; Entscheidungsbaum Fall I/II/III
- NEU-87: $\operatorname{Tr}(B_N^\Lambda) = 0$
- NEU-122.0: Anti-Fitting-Axiom
- Hardy–Littlewood (1923): Singulärreihenkonstante $\mathfrak{S}(h)$
- Goldston–Yıldırım (2003, 2007): Kurzabstandskorrelationen; $\sum_m\Lambda(m)\Lambda(m+h)$ im Mittel
- Vinogradov: Primzahlen in arithmetischen Progressionen; Mittelwertmethode
