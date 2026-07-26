# NEU-123.C — Dreifachsumme und Diagonaldrift-Test

**Stand:** 5. Juli 2026  
**Anschluss:** NEU-123.A (Koeffizientenextraktion), NEU-123.B (Renormierungsbarriere)  
**Nächste Einheit:** NEU-123.D (strenger/numerischer Beweis $T_N/S_N^{3/2}\to\infty$; Zentrierungssuche)

---

## 123.C.0 — Ausgangspunkt und Kernreduktion

Aus NEU-123.A/B gilt $a_{0,N} = 0$ und:

$$
b_{1,N} = \frac{\gamma}{N}\,S_N^{1/2}, \qquad S_N := \sum_{k \leq N} \Lambda(k)^2.
$$

Weiter ist

$$
a_{1,N} = \frac{\gamma/N}{S_N}\,T_N,
$$

wobei

$$
T_N := \sum_{\substack{n,m \leq N \\ n,m \geq 2 \\ |n-m| \geq 2}}
\Lambda(n)\,\Lambda(m)\,(1+\min(n,m))\,\Lambda(|n-m|).
$$

Der Operator-$\gamma/N$-Faktor kürzt sich vollständig heraus:

$$
\boxed{\frac{a_{1,N}}{b_{1,N}} = \frac{T_N}{S_N^{3/2}}.}
$$

Die Frage nach Diagonaldrift ist damit **exakt** die Frage nach der Wachstumsordnung von $T_N$ relativ zu $S_N^{3/2}$.  
Dies ist ein **arithmetisches Summenblatt**, kein weiteres Operatorblatt.  
**Status: \(\checkmark[M]\) als Reduktion**

---

## 123.C.1 — PNT-Einsatz für $S_N$

Aus dem Primzahlsatz in der Form $\sum_{k \leq N} \Lambda(k) \sim N$ folgt die Standardabschätzung:

$$
S_N = \sum_{k \leq N} \Lambda(k)^2 \sim N \log N.
$$

(Begründung: $\Lambda(k) \leq \log k$, und der Hauptbeitrag kommt von Primzahlen $p \leq N$ mit $\Lambda(p) = \log p$; dann $\sum_{p \leq N}(\log p)^2 \sim N \log N$ via PNT mit Fehlerterm.)

Damit:

$$
S_N^{3/2} \sim N^{3/2}(\log N)^{3/2}.
$$

Divergenz von $a_{1,N}/b_{1,N}$ folgt bereits aus $T_N \gg N^{3/2}(\log N)^{3/2}$.  
**Status: \(\checkmark[M]\) für Reduktionslogik; Feinform abhängig von PNT-Version**

---

## 123.C.2 — Struktur der Dreifachsumme

Mit Substitution $h = |n-m|$, $h \geq 2$, und Ausnutzung der Symmetrie $n \leftrightarrow m$:

$$
T_N = 2\sum_{h=2}^{N-2} \Lambda(h) \sum_{m=2}^{N-h} \Lambda(m)\,\Lambda(m+h)\,(1+m),
$$

bis auf Randkorrekturen $O(N^2 \log N)$. Der innere Ausdruck ist eine **gewichtete additive Primkorrelation**:

$$
\sum_{m \leq N-h} m\,\Lambda(m)\,\Lambda(m+h),
$$

die für jede feste Verschiebung $h$ eine Hardy–Littlewood-artige Struktur hat, hier aber noch mit dem äußeren Gewicht $\Lambda(h)$ über alle $h$ gemittelt wird.

Damit ist $T_N$ eine **über alle Verschiebungen $h$ gemittelte HL-Korrelationssumme**, gewichtet mit $\Lambda(h)$:  
nicht eine Einzelkorrelation bei fester Verschiebung, sondern eine dreifache Faltungsstruktur.

**Status: \(\checkmark[M]\)**

---

## 123.C.3 — Heuristische Hauptordnung (Hardy–Littlewood)

Für feste oder typische Verschiebungen $h$ gibt die HL-Mittelwertvermutung:

$$
\sum_{m \leq X} \Lambda(m)\,\Lambda(m+h) \sim \mathfrak{S}(h)\,X,
$$

und mit dem linearen Gewicht $m$:

$$
\sum_{m \leq X} m\,\Lambda(m)\,\Lambda(m+h) \sim \frac{1}{2}\,\mathfrak{S}(h)\,X^2.
$$

Hier ist $\mathfrak{S}(h) = 2C_2 \prod_{p|h, p>2}\frac{p-1}{p-2}$ die Singulärreihenkonstante (bei $h$ gerade, für Primzahlpaare).

Einsatz in $T_N$:

$$
T_N \sim 2 \cdot \frac{1}{2} \sum_{h=2}^{N} \Lambda(h)\,\mathfrak{S}(h)\,(N-h)^2
\sim N^2 \sum_{h \leq N} \Lambda(h)\,\mathfrak{S}(h).
$$

Mit $\sum_{h \leq N} \Lambda(h)\,\mathfrak{S}(h) \asymp N$ (da $\mathfrak{S}(h) = O(1)$ im Mittel und $\sum_{h \leq N}\Lambda(h) \sim N$):

$$
\boxed{T_N \asymp N^3 \quad (\text{HL-Heuristik}).}
$$

Damit:

$$
\frac{a_{1,N}}{b_{1,N}} = \frac{T_N}{S_N^{3/2}} \asymp \frac{N^3}{N^{3/2}(\log N)^{3/2}}
= \frac{N^{3/2}}{(\log N)^{3/2}} \longrightarrow +\infty.
$$

**Robuste Formulierung (ohne Fixierung des Logfaktors):**

$$
\boxed{\text{Unter HL-Mittelwertheuristik: }\frac{a_{1,N}}{b_{1,N}} \gtrsim \frac{N^{3/2}}{(\log N)^{3/2}} \to +\infty.}
$$

Der genaue Logexponent ($3/2$ oder $3$ oder anderes) hängt von der Präzision der $\mathfrak{S}(h)$-Mittelung ab und ist für die Qualitatsaussage (Divergenz) zweitrangig.  
**Status: \(\warning[M]\) heuristisch; HL-abhängig**

---

## 123.C.4 — Grobe Positivitätsdiagnose (ohne HL)

Alle Summanden von $T_N$ sind nichtnegativ:

$$
\Lambda(n)\,\Lambda(m)\,(1+\min(n,m))\,\Lambda(|n-m|) \geq 0.
$$

Es gibt keine oszillatorische Auslöschung. Damit ist jede Stabilisierung

$$
T_N = O(S_N^{3/2}) = O(N^{3/2}(\log N)^{3/2})
$$

arithmetisch **unplausibel ohne starke Dünnheitsannahme** für Mangoldt-Additionskorrelationen.

Konkret: $T_N = O(N^{3/2}(\log N)^{3/2})$ würde bedeuten, dass die Summe
$\sum_{m \leq N} m\,\Lambda(m)\,\Lambda(m+h)$ für die meisten $h$ um viele Größenordnungen kleiner ist als das $\Theta(N^2)$ der HL-Heuristik. Das ist unter keiner bekannten Lückentheorie plausibel.  
**Status: \(\warning[M]\)**

---

## 123.C.5 — Entscheidung Fall I vs. Fall II

| Fall | Bedingung | Konsequenz |
|------|-----------|------------|
| **Fall I** | $T_N = O(S_N^{3/2})$ | $\tilde{a}_{1,N}$ beschränkt; einfache Offdiagonal-Renormierung rettet Grenzoperator |
| **Fall II** | $T_N/S_N^{3/2} \to +\infty$ | $\tilde{a}_{1,N} \to +\infty$; Diagonaldrift-Barriere; reine Offdiagonal-Renormierung scheitert |
| **Fall III** | $b_{2,N}/b_{1,N} \notin (0,\infty)$ | Auch Offdiagonalen inkohärent; keine skalare Renormierung |

HL-Heuristik und Positivitätsdiagnose sprechen klar für **Fall II**.  
**Status: ?[O] streng; \(\warning[M]\) heuristisch stark gestützt**

---

## 123.C.6 — Konsequenz bei Fall II: Zentrierungssuche

Falls Fall II bestätigt, braucht man zusätzlich eine intrinsische Zentrierung:

$$
\kappa_N^{-1}\bigl(A_N^{Jac,-} - c_N I\bigr).
$$

Da $a_{0,N} = 0$: die Startvektor-Zentrierung ist $c_N = 0$. Eine von null verschiedene Zentrierung $c_N \neq 0$ erfordert eine Herleitung aus der Operatorstruktur.

**Intrinsische Kandidaten (zulässig):**

| Kandidat | Herleitung |
|----------|------------|
| $c_N = \frac{1}{|I_N|}\operatorname{Tr}(A_N^{Jac,-})$ | Spurmittel; $\operatorname{Tr}(B_N^\Lambda) = 0$ (NEU-87), also $c_N = 0$ | 
| $c_N = a_{1,N}$ | Zentriert auf zweiten Diagonaleintrag; aber dann ist $\tilde{a}_{1,N} = 0$ by definition, nicht durch Konvergenz |
| $c_N$ aus PNT-Diagonalmittel der Feshbach-Blöcke | Noch nicht hergeleitet |

Da $\operatorname{Tr}(B_N^\Lambda) = 0$ (NEU-87: $\operatorname{Tr}(J_N^\Lambda) = 0$), liefert das Spurmittel $c_N = 0$ — keine zusätzliche Information.  
Die Zentrierungsfrage bleibt offen.

**Sperrvermerk:** Eine Zentrierung anhand von $C_\xi$, $\gamma_k$, $Q_N^{Bomb}$ oder Nullstellenordinaten ist durch NEU-122.0 und NEU-124.S verboten.  
**Status: ?[O]**

---

## 123.C.7 — Momentformel für $b_{2,N}/b_{1,N}$

Die Jacobi-Momente des Startvektors $e_0$ erfüllen:

$$
\mu_{\ell,N} := \langle e_0,\,(A_N^{Jac,-})^\ell\,e_0\rangle.
$$

Aus der Lanczos-Rekursion folgt:

$$
\mu_{2,N} = b_{1,N}^2, \qquad
\mu_{3,N} = a_{1,N}\,b_{1,N}^2, \qquad
\mu_{4,N} = (a_{1,N}^2 + b_{1,N}^2 + b_{2,N}^2)\,b_{1,N}^2.
$$

Damit:

$$
b_{2,N}^2 = \frac{\mu_{4,N}}{b_{1,N}^2} - a_{1,N}^2 - b_{1,N}^2,
$$

$$
\frac{b_{2,N}^2}{b_{1,N}^2}
= \frac{\mu_{4,N}}{b_{1,N}^4} - \left(\frac{a_{1,N}}{b_{1,N}}\right)^2 - 1.
$$

Falls $a_{1,N}/b_{1,N} \to +\infty$, dann muss $\mu_{4,N}/b_{1,N}^4$ auf derselben Skala divergieren, damit $b_{2,N}/b_{1,N}$ endlich bleibt. Dies ist der Test zwischen Fall II und Fall III.

Der vierte Moment $\mu_{4,N} = \langle e_0, (A_N^{Jac,-})^4 e_0\rangle$ hängt von einer Vierfach-Mangoldt-Summe ab — Auswertung in NEU-123.D.  
**Status: ?[O]**

---

## 123.C.F — Fazit

NEU-123.C reduziert die Renormierungsbarriere aus NEU-123.B vollständig auf die arithmetische Dreifachsumme:

$$
\boxed{\frac{a_{1,N}}{b_{1,N}} = \frac{T_N}{S_N^{3/2}}, \qquad
T_N = \sum_{\substack{n,m \leq N \\ |n-m| \geq 2}} \Lambda(n)\Lambda(m)(1+\min(n,m))\Lambda(|n-m|).}
$$

Die HL-Heuristik ergibt $T_N \asymp N^3$, also:

$$
\frac{a_{1,N}}{b_{1,N}} \gtrsim \frac{N^{3/2}}{(\log N)^{3/2}} \longrightarrow +\infty.
$$

Diagnose: **Fall II (Diagonaldrift-Barriere)** ist der wahrscheinlichste Ausgang.  
Die reine Offdiagonal-Normierung $\kappa_N = b_{1,N}$ reicht nicht.
Da $\operatorname{Tr}(B_N^\Lambda) = 0$, liefert das natürliche Spurmittel keine zusätzliche Zentrierung.

$$
\boxed{\text{Diagonaldrift-Barriere. Intrinsische Zentrierung }c_N\text{ aus Operatorstruktur erforderlich — offen.}}
$$

**Status gesamt: ?[O] streng; \(\warning[M]\) heuristisch stark gestützt**

---

## 123.C.N — Nächste Aufgaben (NEU-123.D)

**Priorität 1 (Entscheidend):**  
Strenges oder numerisches Argument für $T_N \gg S_N^{3/2}$, möglichst ohne volle HL-Vermutung.
Minimalziel: $T_N \geq c\, N^{3/2+\varepsilon}$ für ein $\varepsilon > 0$.

**Priorität 2 (Kontrolltest):**  
Vierte Momentformel $\mu_{4,N}$ auswerten; daraus $b_{2,N}/b_{1,N}$ bestimmen;
Fall II vs. Fall III entscheiden.

**Priorität 3 (Falls Fall II bestätigt):**  
Identifikation eines intrinsischen $c_N \neq 0$ aus Feshbach-Blockstruktur oder PNT-Diagonalmittel der Blöcke $H_N$.

---

## Verweise

- NEU-123.A: Extraktion $a_{0,N}=0$, $b_{1,N}$, $a_{1,N}$ (Formel), $b_{2,N}$
- NEU-123.B: Renormierungsbarriere; $\kappa_N = b_{1,N}$; Entscheidungsbaum Fall I/II/III
- NEU-87: $B_N^\Lambda$, Matrixelemente, $\operatorname{Tr}(B_N^\Lambda) = 0$
- NEU-122.0: Anti-Fitting-Axiom
- NEU-124.S: Sperrvermerk Spektraldaten
- Hardy–Littlewood (1923): Primzahlpaarvermutung und Singulärreihenkonstante $\mathfrak{S}(h)$
- Goldston–Yıldırım (2003): Kurzabstandskorrelationen für $\Lambda$; Methoden für $\sum_{m}\Lambda(m)\Lambda(m+h)$
- Simon: *Szeg\H{o}'s Theorem*, PUP 2011, Kap. 2 (Momentformel für Jacobi-Koeffizienten)
