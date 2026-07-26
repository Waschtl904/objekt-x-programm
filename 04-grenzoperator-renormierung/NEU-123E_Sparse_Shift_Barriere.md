# NEU-123.E — Sparse-Shift-Barriere für die Mangoldt-Dreifachsumme

**Stand:** 6. Juli 2026  
**Anschluss:** NEU-123.D (paritätskorrigierte Heuristik $T_N \asymp N^2 \log N$)  
**Nächste Einheiten:** NEU-123.F (numerischer Test $D_N$), NEU-123.G (Divisorsummenmodell $T_{N,R}^{(2)}$)

---

## 123.E.0 — Ausgangspunkt

Aus NEU-123.D gilt:

$$
T_N = 2\sum_{h=2}^{N}\Lambda(h)\sum_{m \leq N-h}m\,\Lambda(m)\Lambda(m+h).
$$

Wegen der Paritätsbarriere liefern primmäßig relevante Hauptterme nur die dünnen geraden Shifts $h = 2^r$. Der relevante positive Kern:

$$
T_N^{(2)} := 2\log 2\sum_{2^r \leq N}\sum_{m \leq N-2^r}m\,\Lambda(m)\,\Lambda(m+2^r).
$$

Das Minimalziel:

$$
\boxed{T_N^{(2)} \gg N^{3/2+\varepsilon}.}
$$

**Status: $\checkmark[M]$ als Reduktion (aus NEU-123.D)**

---

## 123.E.1 — Warum dies kein Bombieri–Vinogradov-Problem ist

Bombieri–Vinogradov kontrolliert die **Verteilung** von Primzahlen in arithmetischen Progressionen im Mittel über Moduli $q \leq \sqrt{N}$. Das liefert:

$$
\sum_{q \leq \sqrt{N}}\max_{(a,q)=1}\left|\pi(X;q,a) - \frac{X}{\phi(q)}\right| \ll \frac{X}{(\log X)^A}.
$$

Hier geht es jedoch um **additive Zweipunktkorrelationen** $\Lambda(m)\Lambda(m+2^r)$ auf einer dünnen Shiftmenge. Das ist keine Verteilung in Restklassen, sondern eine Prim-Paar-Frage. Bombieri–Vinogradov liefert deshalb **keinen** Lower Bound der Form

$$
\sum_{2^r \leq N}\sum_{m \leq N-2^r}m\,\Lambda(m)\,\Lambda(m+2^r) \gg N^{3/2+\varepsilon}.
$$

**Status: $\checkmark[M]$**

---

## 123.E.2 — Nähe zu Goldston–Yıldırım, aber keine direkte Ableitung

Goldston–Yıldırım (2003, 2007) untersuchten höhere Korrelationen von **abgeschnittenen Divisorsummen** $\Lambda_R(n)$ als Modelle für $\Lambda(n)$. Diese liefern u.a.:

$$
\sum_{m \leq X}\Lambda_R(m)\Lambda_R(m+h) \sim \mathfrak{S}(h)\,X \quad (R = X^\theta,\,\theta < 1)
$$

als Mittelwertaussage über $h$ in guten Parameterregimes.

Für NEU-123.E benötigt man aber einen Lower Bound für die **echte** Mangoldt-Korrelation $\Lambda(m)\Lambda(m+2^r)$ im Mittel über die sparse Shiftmenge $\{2^r : 2^r \leq N\}$. Das ist:
- **stärker** als ein Divisorsummen-Modellsatz (weil $\Lambda_R \neq \Lambda$)
- **stärker** als eine Singularreihen-Mittelwertidentität (weil keine Untergrenzen)

Eine direkte Ableitung aus Goldston–Yıldırım ist nicht möglich.  
**Status: $\warning[M]$ Nähe vorhanden; direkte Ableitung: ?[O]**

---

## 123.E.3 — Singularreihen-Mittelwerte erklären die Heuristik

Gallaghers Mittelwertsatz (1976) und Pintz’ moderne Behandlung zeigen, dass im Mittel über $h \leq H$:

$$
\frac{1}{H}\sum_{h \leq H}\mathfrak{S}(h) \sim 1.
$$

Für die Zweierpotenz-Shifts gilt speziell $\mathfrak{S}(2^r) \asymp 1$ (keine ungeraden Primteiler in $h$, Eulerfaktoren konvergieren zur Konstante $2C_2 \asymp 1.32$). Damit erwartet man:

$$
\sum_{m \leq N-2^r}m\,\Lambda(m)\,\Lambda(m+2^r) \asymp N^2 \quad\text{(HL, für typische }r\text{)}
$$

und somit:

$$
T_N^{(2)} \asymp N^2 \log N, \qquad \frac{a_{1,N}}{b_{1,N}} \asymp \sqrt{\frac{N}{\log N}}.
$$

Singularreihen-Mittelwerte liefern jedoch **keine Untergrenzen** für die echten Primpaarkorrelationen.  
**Status: $\warning[M]$ heuristisch stark; streng: ?[O]**

---

## 123.E.4 — Die eigentliche Barriere: sparse Polignac-artige Aussage

Ein Lower Bound $T_N^{(2)} \gg N^{3/2+\varepsilon}$ würde insbesondere erzwingen, dass für unendlich viele $N$ viele Paare

$$
(m,\; m+2^r), \quad m \leq N,\; 2^r \leq N,
$$

beiden in $\operatorname{supp}(\Lambda)$ liegen. Der Primzahlanteil entspricht Paaren $(p, p+2^r)$ mit $p$ prim und $p + 2^r$ prim oder Primzahlpotenz.

Das ist eine **sparse Polignac-artige Aussage**: nicht ein fester gerader Abstand, sondern Abstände aus der exponentiell dünnen Menge $\{2, 4, 8, 16, \ldots\}$.

Diese Situation liegt in der **Sieve-Parity-Barriere** von Selberg: Kombinatorische Siebe liefern natürlicherweise nur **Obergrenzen** für Paar-Zählungen $\pi_2(X, h) = \#\{p \leq X : p+h \text{ prim}\}$, keine Untergrenzen. Untergrenzen erfordern analytische Methoden (Kreismethode, Mittelwertsätze), die ihrerseits unbedingte Paar-Asymptotik verlangen.

$$
\boxed{\text{Das Minimalziel berührt die Sieve-Parity-Barriere.}}
$$

**Status: ?[O]**

---

## 123.E.5 — Konsequenz für die Operator-Kette

Falls das Minimalziel unbewiesen bleibt:

- Fall II (Diagonaldrift-Barriere) ist heuristisch stark gestützt
- Fall II kann **streng nicht geschlossen** werden
- Die Statusmarkierung bleibt: $\warning[M]$ heuristisch; ?[O] streng

Falls das Minimalziel bewiesen wird ($T_N \gg N^{3/2+\varepsilon}$):

- $\tilde{a}_{1,N} \to +\infty$ ist gesichert
- Fall II ist $\checkmark[M]$
- NEU-123.B/C/D werden auf $\checkmark[M]$ hochgestuft

**Status: $\warning[M]$ heuristisch; ?[O] streng**

---

## 123.E.6 — Modellersatz mit abgeschnittener Divisorsumme

Als Zwischenstufe ersetzt man $\Lambda$ durch eine Goldston–Yıldırım-artige abgeschnittene Divisorsumme:

$$
\Lambda_R(n) = \sum_{\substack{d | n \\ d \leq R}} \mu(d)\log(R/d).
$$

Dann:

$$
T_{N,R}^{(2)} := 2\log 2\sum_{2^r \leq N}\sum_{m \leq N-2^r}m\,\Lambda_R(m)\,\Lambda_R(m+2^r).
$$

Für Modellgewichte $\Lambda_R$ sind Mittelwert-Korrelationen zugränglich (Goldston–Yıldırım-Methode). Wenn man zeigen kann:

$$
T_{N,R}^{(2)} \asymp N^2\log N \quad\text{für }R = N^\theta,\;\theta < 1,
$$

dann ist das kein Beweis für $T_N^{(2)}$, aber ein starkes **Strukturindiz**:

$$
\boxed{\text{Die Diagonaldrift kommt bereits im Divisorsummenmodell vor.}}
$$

Wenn schon das Modell die Drift nicht zeigt, liegt möglicherweise ein Fehler in der heuristischen Gewichtung vor.

**Status: ?[O] — geplant für NEU-123.G**

---

## 123.E.7 — Numerischer Test (Plan für NEU-123.F)

Parallel zum theoretischen Minimalziel numerische Messung:

$$
D_N := \frac{T_N}{S_N^{3/2}}.
$$

Nach der paritätskorrigierten Heuristik:

$$
D_N \asymp \sqrt{\frac{N}{\log N}}.
$$

Daher teste **Stabilisierung** von:

$$
\tilde{D}_N := D_N \cdot \sqrt{\frac{\log N}{N}} = \frac{T_N}{S_N^{3/2}} \cdot \sqrt{\frac{\log N}{N}}.
$$

Wenn $\tilde{D}_N \to c > 0$: paritätskorrigierte HL-Heuristik bestätigt.  
Wenn $\tilde{D}_N \to 0$: Drift schwächer als $\sqrt{N/\log N}$; Grenzskalierung offen.  
Wenn $\tilde{D}_N \to \infty$: Drift stärker; naive $N^3$-Heuristik näher.

**Status: ?[O] — geplant für NEU-123.F**

---

## 123.E.F — Fazit

NEU-123.E identifiziert die arithmetische Lücke hinter der Operatorbarriere. Das Minimalziel

$$
\boxed{T_N \gg N^{3/2+\varepsilon}}
$$

ist eine **sparse-shift Prim-Paar-Untergrenze** über $h = 2^r$. Sie ist:
- schwächer als volle Hardy–Littlewood-Vermutung
- **stärker** als Bombieri–Vinogradov und reine Singularreihen-Mittelwerte
- an der **Sieve-Parity-Barriere** von Selberg

### Statusmatrix

| Punkt | Aussage | Status |
|-------|---------|--------|
| Paritätskorrektur (nur $h=2^r$ primär) | $\checkmark[M]$ | |
| Bombieri–Vinogradov liefert keinen LB | $\checkmark[M]$ | |
| GY-Modell–Nähe, keine direkte Ableitung | $\warning[M]$ | |
| Singularreihen-Mittelwert-Heuristik $T_N \asymp N^2 \log N$ | $\warning[M]$ HL | |
| Triviale untere Schranke $T_N \gg N$ | $\checkmark[M]$ | |
| Minimalziel $T_N \gg N^{3/2+\varepsilon}$ streng | ?[O] | |
| Operator-Fall II ($\tilde{a}_{1,N} \to \infty$) | ?[O] streng; $\warning[M]$ heuristisch | |

---

## 123.E.N — Nächste Einheiten

**NEU-123.F — Numerischer Test:**  
Berechne $D_N = T_N/S_N^{3/2}$ und $\tilde{D}_N = D_N\sqrt{\log N / N}$ für $N = 50, 100, 500, 1000, 5000$.  
Entscheide: stabilisiert $\tilde{D}_N$, fällt sie, oder wächst sie?

**NEU-123.G — Divisorsummenmodell:**  
Ersetze $\Lambda \to \Lambda_R$ ($R = N^{1/2}$). Berechne $T_{N,R}^{(2)}$.  
Frage: Zeigt das Modell dieselbe Drift $\asymp N^2 \log N$?  
Wenn ja: Strukturindiz für Fall II aus Modelloperator.  
Wenn nein: Rückfrage an heuristische Gewichtung.

---

## Verweise

- NEU-123.D: Paritätskorrektur; $T_N \asymp N^2 \log N$ (HL); $a_{1,N}/b_{1,N} \asymp \sqrt{N/\log N}$
- NEU-123.B: Entscheidungsbaum Fall I/II/III
- NEU-122.0: Anti-Fitting-Axiom
- Selberg: Sieve-Parity-Problem (Upper-Bound-Siebe liefern keine Untergrenze für Paare)
- Gallagher (1976): Singularreihen-Mittelwerte; $\frac{1}{H}\sum_{h \leq H}\mathfrak{S}(h) \sim 1$
- Goldston–Yıldırım (2003/2007): Korrelationen abgeschnittener Divisorsummen
- Pintz (2010+): Moderne Singularreihen-Behandlung, GPY-Methode
- Bombieri–Vinogradov (1965): Verteilung in Restklassen (hier: nicht ausreichend)
- Hardy–Littlewood (1923): Primzahlpaarvermutung und $\mathfrak{S}(h)$
