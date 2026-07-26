# NEU-123.B — Renormierungsbarriere der Jacobi-Koeffizienten

**Stand:** 5. Juli 2026  
**Anschluss:** NEU-123.A (Extraktion $a_{0,N}, b_{1,N}, a_{1,N}, b_{2,N}$), NEU-86/87  
**Nächste Einheit:** NEU-123.C (Auswertung der Quotiententests; Entscheidung über Grenzoperator)

---

## 123.B.0 — Befund aus NEU-123.A

Aus der Extraktion der ersten Lanczos-Daten (NEU-123.A) folgt:

$$
a_{0,N} = 0 \qquad \text{(exakt)}
$$

$$
b_{1,N} = \gamma_N\!\left(\sum_{n=2}^{N-1}\Lambda(n)^2\right)^{\!1/2}
\asymp \frac{\gamma\sqrt{\log N}}{\sqrt{N}} \;\longrightarrow\; 0.
$$

**Anmerkung zur Notation:** In NEU-123.A steht $\gamma_N = \gamma/N$; damit ist

$$
b_{1,N} = \frac{\gamma}{N}\sqrt{\sum_{n \leq N}\Lambda(n)^2}
\sim \gamma\sqrt{\frac{\log N}{N}}.
$$

Falls anderswo ein zusätzlicher Logfaktor erscheint, liegt eine abweichende $\gamma_N$-Konvention oder $\Lambda^2$-Abschätzung vor. Für die Qualitätsaussage ist das irrelevant — beide Skalen $→ 0$ — aber für die genaue $\kappa_N$-Skala in 123.B.1 ist die Formel

$$
\kappa_N = b_{1,N} \sim \gamma\sqrt{\frac{\log N}{N}}
$$

verbindlich zu verwenden.  
**Status: \(\checkmark[M]\) unter NEU-123.A**

### Degeneration des Startvektor-Spektralmaßes

Aus $b_{1,N} \to 0$ folgt: Der Startvektor $e_0 = \delta_1$ entkoppelt im unrenormierten Grenzbild vom Rest.
Das Weyl-Spektralmaß am Startvektor degeneriert:

$$
\mu_{e_0}^{A_\infty} = \delta_{a_0} = \delta_0.
$$

Insbesondere gilt für die unrenormierte Weyl-Funktion:

$$
m_{e_0,N}(z) \;\longrightarrow\; -\frac{1}{z}.
$$

Das ist nicht $m_{\mathrm{arith}}$. Der unrenormierte Operator kann $m_{\mathrm{arith}}$ am Startvektor nicht erzeugen.  
**Status: \(\checkmark[M]\)**

---

## 123.B.1 — Intrinsisch erzwungene erste Reskalierung

**Sperrvermerk:** Eine Reskalierung darf nicht nachträglich anhand von Zeta-Ordinaten, Bombieri-Gewichten oder $C_\xi$ gewählt werden (Anti-Fitting-Axiom, NEU-122.0).

Die einzige aus NEU-123.A **intrinsisch erzwungene** Skala ist

$$
\boxed{\kappa_N := b_{1,N}.}
$$

Man definiert den reskalierten Operator:

$$
\widetilde{A}_N := \kappa_N^{-1}\, A_N^{Jac,-}.
$$

Damit gilt automatisch:

$$
\widetilde{b}_{1,N} = 1.
$$

Dies ist keine Fitting-Normierung, sondern die kanonische erste Offdiagonal-Normierung des Jacobi-Operators: Man normiert auf die einzige Skala, die der Operator selbst im ersten Lanczos-Schritt setzt.  
**Status: \(\checkmark[M]\)**

---

## 123.B.2 — Neuer Konvergenztest nach Reskalierung

Die reskalierten Koeffizienten sind:

$$
\widetilde{a}_{j,N} := \frac{a_{j,N}}{\kappa_N}, \qquad
\widetilde{b}_{j,N} := \frac{b_{j,N}}{\kappa_N}.
$$

NEU-123.B muss für jedes feste $j$ prüfen, ob

$$
\widetilde{a}_{j,N} \to \widetilde{a}_j \in \mathbb{R}
\qquad \text{und} \qquad
\widetilde{b}_{j,N} \to \widetilde{b}_j \in (0,\infty).
$$

Die ersten beiden konkreten Quotiententests:

$$
\boxed{\frac{a_{1,N}}{b_{1,N}} \stackrel{?}{\longrightarrow} \widetilde{a}_1 \in \mathbb{R}}
$$

$$
\boxed{\frac{b_{2,N}}{b_{1,N}} \stackrel{?}{\longrightarrow} \widetilde{b}_2 \in (0,\infty)}
$$

Wenn bereits $a_{1,N}/b_{1,N} \to \infty$ oder $b_{2,N}/b_{1,N} \to 0$ oder $\infty$, scheitert die einfache skalare Renormierung.  
**Status: ?[O]**

---

## 123.B.3 — Diagonalproblem und Drift-Barriere

Die Offdiagonal-Normierung $\kappa_N = b_{1,N}$ löst nur das Problem $b_{1,N} \to 0$.
Sie löst **nicht automatisch** das Diagonalproblem.

Falls $a_{1,N} \gg b_{1,N}$, dann divergiert $a_{1,N}/b_{1,N}$, und der reskalierte Grenzoperator ist entweder nicht definiert oder hat $\widetilde{a}_1 = +\infty$ (Diagonaldrift-Barriere).

In diesem Fall wäre zusätzlich eine intrinsische **Zentrierung** zu prüfen:

$$
\kappa_N^{-1}\bigl(A_N^{Jac,-} - c_N I\bigr).
$$

Die kanonische Startvektor-Zentrierung lautet wegen $a_{0,N} = 0$:

$$
c_N = a_{0,N} = 0.
$$

Eine andere Wahl von $c_N$ ist nur zulässig, wenn sie aus der Operatorstruktur selbst folgt, nicht aus Zeta- oder Bombieri-Zieldaten.  
**Status: ?[O]**

---

## 123.B.4 — Erster heuristischer Verdacht: Diagonaldrift

Die Formel aus NEU-123.A für $a_{1,N}$:

$$
a_{1,N}
= \frac{\gamma/N}{\sum_k\Lambda(k)^2}
  \sum_{\substack{n,m\geq 2 \\ |n-m|\geq 2}}
  \Lambda(n)\Lambda(m)\,(1+\min(n,m))\,\Lambda(|n-m|).
$$

Diese Summe ist **nicht oszillatorisch**, sondern überwiegend positiv (alle Faktoren $\Lambda(n) \geq 0$, $\min(n,m) \geq 2$).

Ein grober Abschätzungsrahmen: Wenn die typischen $n,m \sim N/2$ und $\Lambda \sim \log N$, dann:

$$
\sum_{n,m} \Lambda(n)\Lambda(m)(1+\min(n,m))\Lambda(|n-m|)
\sim N^2 \cdot (\log N)^2 \cdot \frac{N}{2} \cdot \log N
= O(N^3(\log N)^3).
$$

Mit $\gamma/N$ und $\sum_k\Lambda(k)^2 \sim N\log N$:

$$
a_{1,N} \sim \frac{\gamma/N}{N\log N} \cdot N^3(\log N)^3
= \gamma N(\log N)^2.
$$

Demgegenüber:

$$
b_{1,N} \sim \gamma\sqrt{\frac{\log N}{N}}.
$$

Damit:

$$
\frac{a_{1,N}}{b_{1,N}}
\sim \frac{\gamma N(\log N)^2}{\gamma\sqrt{(\log N)/N}}
= N^{3/2}(\log N)^{3/2} \;\longrightarrow\; +\infty.
$$

$$
\boxed{a_{1,N} = O(b_{1,N})\;? \quad \textbf{Verdacht: Nein.}\quad a_{1,N}/b_{1,N}\to+\infty.}
$$

**Status: \(\warning[M]\) (heuristische Abschätzung, Skalenkontrolle in 123.C erforderlich)**

> **Bemerkung:** Die Abschätzung $a_{1,N} \sim \gamma N(\log N)^2$ ist grob. Die Dreifachsumme enthält den $\min(n,m)$-Faktor und die $|n-m| \geq 2$-Bedingung; eine präzise asymptotische Auswertung via Primzahlsatz für $\sum_{n}\Lambda(n)\Lambda(m)\Lambda(|n-m|)$ steht aus. Das qualitative Bild — Diagonaldrift — erscheint jedoch robust.

---

## 123.B.5 — Entscheidungsbaum

NEU-123.B hat drei mögliche Ausgänge:

### Fall I — Erfolgreiche skalare Renormierung

$$
\frac{a_{j,N}}{b_{1,N}} \to \widetilde{a}_j \in \mathbb{R}
\quad\text{und}\quad
\frac{b_{j,N}}{b_{1,N}} \to \widetilde{b}_j \in (0,\infty)
\quad\text{für feste }j.
$$

Dann entsteht ein nichttrivialer reskalierter Grenzoperator $\widetilde{A}_\infty$.  
NEU-123 wird mit $b_{1,N}^{-1}A_N^{Jac,-}$ fortgesetzt.  
**Status: ?[O]**

### Fall II — Offdiagonalen stabilisieren, Diagonalen divergieren

$$
\frac{b_{j,N}}{b_{1,N}} \to \widetilde{b}_j \in (0,\infty),
\quad\text{aber}\quad
\frac{a_{j,N}}{b_{1,N}} \to +\infty.
$$

Dann liegt eine **Diagonaldrift-Barriere** vor. Es muss geprüft werden, ob eine zusätzliche intrinsische Zentrierung

$$
\kappa_N^{-1}\bigl(A_N^{Jac,-} - c_N I\bigr)
$$

existiert, wobei $c_N$ aus der Operatorstruktur folgt (nicht aus Zeta-Daten).
Ohne solche Zentrierung scheitert der Jacobi-Grenzoperator.  
**Status: ?[O] — heuristischer Verdacht: dieser Fall liegt vor**

### Fall III — Auch Offdiagonalen skalieren inkohärent

$$
\frac{b_{2,N}}{b_{1,N}} \notin (0,\infty).
$$

Dann gibt es keine einfache skalare Renormierung. Die Jacobi-Schließung aus NEU-87 ist nicht stabil genug für einen Grenzoperator gemäß NEU-123.  
**Status: ?[O]**

---

## 123.B.F — Fazit

Der Befund $b_{1,N} \to 0$ aus NEU-123.A ist eine **echte Operator-Barriere**, kein Rechenartefakt:
der Startvektor entkoppelt im Grenzbild, das unrenormierte Weyl-Maß degeneriert zu $\delta_0$.

Die einzige intrinsisch zulässige erste Rettung ist $\kappa_N = b_{1,N}$.
NEU-123.B reduziert die Frage auf zwei konkrete Quotiententests:

$$
\boxed{\frac{a_{1,N}}{b_{1,N}} \stackrel{?}{\longrightarrow} \widetilde{a}_1 \in \mathbb{R}}
\qquad
\boxed{\frac{b_{2,N}}{b_{1,N}} \stackrel{?}{\longrightarrow} \widetilde{b}_2 \in (0,\infty)}
$$

Heuristisch deutet die Skalenabschätzung aus 123.B.4 auf

$$
\frac{a_{1,N}}{b_{1,N}} \sim N^{3/2}(\log N)^{3/2} \to +\infty
$$

hin — d.h. **Fall II (Diagonaldrift-Barriere)** ist der wahrscheinlichste Ausgang.  
Bis zur Auswertung in NEU-123.C bleibt der Status offen.  
**Status gesamt: \(\warning[M]\) — Barriere identifiziert; Quotiententests offen**

---

## 123.B.N — Nächste konkrete Rechnung (NEU-123.C)

Prioriät 1 (Entscheidend):
$$
\frac{a_{1,N}}{b_{1,N}} \sim \;?
$$
Präzise asymptotische Auswertung der Dreifachsumme
$\sum_{n,m}\Lambda(n)\Lambda(m)(1+\min(n,m))\Lambda(|n-m|)$
mit Primzahlsatz-Methoden.

Priorität 2 (Kontrolltest):
$$
\frac{b_{2,N}}{b_{1,N}} \sim \;?
$$
Explizite Formel für $b_{2,N}$ aus dem zweiten Lanczos-Residuum; Skalenvergleich mit $b_{1,N}$.

Priorität 3 (Falls Fall II bestätigt):
Identifikation einer intrinsischen Zentrierung $c_N$ aus der Operatorstruktur (z.B. $c_N = $ Diagonalmittel, Spur/Dimension, oder PNT-Abzählung).

---

## Verweise

- NEU-123.A: Extraktion $a_{0,N}=0$, $b_{1,N}$, $a_{1,N}$, $b_{2,N}$
- NEU-86: Nilpotenz-Barriere; $(J_N^\Lambda)^N=0$
- NEU-87: Jacobi-Schließung; Matrixelemente von $B_N^\Lambda$
- NEU-122.0: Anti-Fitting-Axiom (keine Zeta/Bombieri-Normierung)
- NEU-62: Normierungsrigidität, Jacobi-Limes
- NEU-78/79: Kanalzahl-Skalierung, Normierungs-NoGo
- Teschl: *Jacobi Operators and CMV Matrices*, AMS 2000 (Weyl-Funktion, Spektralmaß)
- Simon: *Szeg\H{o}'s Theorem and its Descendants*, PUP 2011 (Kap. 2: Jacobi-Matrizen)
