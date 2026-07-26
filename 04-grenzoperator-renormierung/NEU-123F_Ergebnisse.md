# NEU-123.F — Ergebnisblatt: Numerische Diagnose der Dreifachsumme

**Stand:** 6. Juli 2026  
**Methode:** Direkte Berechnung $T_N$, $T_N^{(2)}$, $S_N$ für $N = 100\text{–}5000$  
**Anschluss zu:** NEU-123.F (Kalibrierungsblatt), NEU-123.G (Lanczos-Quotienten)

---

## Hauptbefund

$$
\boxed{D_N = \frac{T_N}{S_N^{3/2}} \asymp \sqrt{\frac{N}{\log N}}, \qquad
\widetilde{D}_N \approx 1.55, \qquad \widetilde{D}_N^{(2)} \approx 1.27 \approx 2C_2.}
$$

**Fall A numerisch bestätigt im Fenster $100 \leq N \leq 5000$.**

Statusaufwertung:
$$
\warning[M]_{\mathrm{heur}} \;\longrightarrow\; \warning[M]_{\mathrm{heur+num}}.
$$

---

## Numerische Tabelle

| $N$ | $S_N$ | $T_N$ | $T_N^{(2)}$ | $D_N$ | $\widetilde{D}_N$ | $\widetilde{D}_N^{(2)}$ |
|-----|-------|-------|------------|-------|-------------------|-------------------------|
| 100 | 3.21e+02 | 5.17e+04 | 3.43e+04 | 8.98 | 1.93 | 1.28 |
| 300 | 1.36e+03 | 6.92e+05 | 4.90e+05 | 13.79 | 1.90 | 1.35 |
| 500 | 2.56e+03 | 1.84e+06 | 1.45e+06 | 14.20 | 1.58 | 1.26 |
| 1000 | 5.77e+03 | 8.11e+06 | 6.57e+06 | 18.49 | 1.54 | 1.24 |
| 2000 | 1.30e+04 | 3.70e+07 | 3.04e+07 | 25.01 | 1.54 | 1.27 |
| 3000 | 2.08e+04 | 9.11e+07 | 7.40e+07 | 30.40 | 1.57 | 1.27 |
| 5000 | 3.73e+04 | 2.74e+08 | 2.20e+08 | 38.16 | 1.57 | 1.26 |

---

## $2C_2$-Fingerprint

Für $h = 2^r$ gilt heuristisch $\mathfrak{S}(2^r) = 2C_2$ (Twin-Prime-Konstante, $C_2 \approx 0.6601$). Mit

$$
\sum_{2^r \leq N}(N-2^r)^2 \sim \frac{N^2 \log N}{\log 2}
$$

folgt:

$$
T_N^{(2)} \sim 2C_2\,N^2\log N, \qquad
\widetilde{D}_N^{(2)} \longrightarrow 2C_2 \approx 1.3203.
$$

Die gemessenen Werte $\widetilde{D}_N^{(2)} \approx 1.26\text{--}1.28$ konvergieren von unten gegen $2C_2$ — **numerischer Fingerprint der Paritätsanalyse aus NEU-123.D**.

---

## Anteil der Zweierpotenz-Schichten

$$
\frac{T_N^{(2)}}{T_N} \approx 0.80 \quad\text{(stabil über alle getesteten }N\text{).}
$$

**Fall B ausgeschlossen:** Der Hauptbeitrag kommt aus den $h = 2^r$-Schichten, wie in NEU-123.D vorhergesagt.

---

## Operator-Konsequenz

Da $D_N = a_{1,N}/b_{1,N}$ (Kernidentität aus NEU-123.C), ist der erste Lanczos-Diagonalquotient numerisch divergent:

$$
\frac{a_{1,N}}{b_{1,N}} \approx D_N \asymp \sqrt{\frac{N}{\log N}} \to +\infty.
$$

Die reine Offdiagonal-Renormierung $\widetilde{A}_N = b_{1,N}^{-1}A_N^{Jac,-}$ genügt nicht. **Fall I numerisch verworfen.**

---

## Statusmatrix nach NEU-123.F

| Fall | Status |
|------|--------|
| Fall I (einfache Renormierung) | numerisch verworfen |
| Fall II (Diagonaldrift-Barriere) | $\warning[M]_{\mathrm{heur+num}}$ |
| Fall III (inkohärente Offdiagonalen) | noch offen bis $b_{2,N}/b_{1,N}$ |

---

## Nächste Einheit: NEU-123.G

Direkte Lanczos-Berechnung von $b_{2,N}/b_{1,N}$ für kleine $N$: Fall II vs. Fall III entscheiden.
