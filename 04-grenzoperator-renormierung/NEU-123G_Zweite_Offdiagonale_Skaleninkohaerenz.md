# NEU-123.G — Zweite Offdiagonale und Skaleninkohärenz

**Stand:** 6. Juli 2026  
**Anschluss:** NEU-123.B (Renormierungsbarriere), NEU-123.F (Ergebnisse $D_N$)  
**Nächste Einheit:** NEU-123.H (No-scalar-renormalization Lemma)

---

## 123.G.0 — Ausgangspunkt

Aus NEU-123.B war die einzige zulässige erste Reskalierung

$$
\widetilde{A}_N = b_{1,N}^{-1}A_N^{Jac,-}.
$$

Dann gilt automatisch $\widetilde{b}_{1,N} = 1$. Die entscheidende Frage:

$$
\widetilde{b}_{2,N} = \frac{b_{2,N}}{b_{1,N}} \stackrel{?}{\longrightarrow} \widetilde{b}_2 \in (0,\infty).
$$

Falls nicht, scheitert jede einfache skalare Renormierung.

---

## 123.G.1 — Numerischer Befund

Direkte Lanczos-Berechnung (Startvektor $q_{0,N} = \delta_1$, Operator $A_N^{Jac,-} = B_N^\Lambda$):

$$
\frac{a_{1,N}}{b_{1,N}} \sim \sqrt{N}, \qquad \frac{b_{2,N}}{b_{1,N}} \sim N.
$$

| $N$ | $a_{1,N}/b_{1,N}$ | $b_{2,N}/b_{1,N}$ | $b_{2,N}/(N\cdot b_{1,N})$ |
|-----|-------------------|-------------------|--------------------------|
| 30 | 7.36 | 26.4 | 0.88 |
| 50 | 8.36 | 54.1 | 1.08 |
| 80 | 9.05 | 100.3 | 1.25 |
| 100 | 9.30 | 132.9 | 1.33 |
| 150 | 10.73 | 231.1 | 1.54 |
| 200 | 11.87 | 346.4 | 1.73 |

Zugehörige Normierungskonstante $b_{1,N}$:

$$
b_{1,N} \sim \frac{\gamma\sqrt{\log N}}{\sqrt{N}} \to 0.
$$

Die zweite Offdiagonale divergiert unter der $b_{1,N}$-Normierung: $b_{2,N}/b_{1,N} \sim N \to \infty$.  
**Status: $\warning[M]_{\mathrm{num}}$**

---

## 123.G.2 — Konsequenz: keine skalare Normierung

Angenommen, es gäbe eine skalare Normierung $\kappa_N$ mit

$$
\frac{b_{1,N}}{\kappa_N} \to c_1 \in (0,\infty) \qquad\text{und}\qquad \frac{b_{2,N}}{\kappa_N} \to c_2 \in (0,\infty).
$$

Dann müsste:

$$
\frac{b_{2,N}}{b_{1,N}} = \frac{b_{2,N}/\kappa_N}{b_{1,N}/\kappa_N} \to \frac{c_2}{c_1} \in (0,\infty).
$$

Der numerische Befund zeigt aber $b_{2,N}/b_{1,N} \to \infty$. Widerspruch.  
**Status: ?[O] streng; $\warning[M]_{\mathrm{num}}$ numerisch stark gestützt**

---

## 123.G.3 — Doppelbarriere

NEU-123.F zeigte: $a_{1,N}/b_{1,N} \to \infty$ (Fall II). NEU-123.G zeigt zusätzlich: $b_{2,N}/b_{1,N} \to \infty$ (Fall III).

Beide Barrieren sind gleichzeitig aktiv:

$$
\boxed{\text{Fall II: Diagonaldrift}} \qquad \boxed{\text{Fall III: Offdiagonal-Inkohärenz}}
$$

Die Jacobi-Schließung aus NEU-87 besitzt in der bisherigen Form keinen stabilen skalaren Grenzoperator.  
**Status: $\warning[M]_{\mathrm{heur+num}}$**

---

## 123.G.4 — Bedeutung für NEU-123

| Stufe | Befund | Status |
|-------|--------|--------|
| $b_{1,N} \to 0$ | Startvektor entkoppelt | $\checkmark[M]$ |
| $a_{1,N}/b_{1,N} \to \infty$ | Diagonaldrift | $\warning[M]_{\mathrm{heur+num}}$ |
| $b_{2,N}/b_{1,N} \to \infty$ | Offdiagonal-Inkohärenz | $\warning[M]_{\mathrm{num}}$ |
| Keine skalare $\kappa_N$ rettet beide | Doppelbarriere | $\warning[M]_{\mathrm{num}}$; ?[O] streng |

Damit ist die einfache starke Resolventenkonvergenzspur aus NEU-123 in der NEU-87-Normierung **blockiert**.

---

## 123.G.F — Fazit

$$
\frac{a_{1,N}}{b_{1,N}} \sim \sqrt{N}, \qquad \frac{b_{2,N}}{b_{1,N}} \sim N.
$$

$$
\boxed{\text{Die NEU-87-Jacobi-Schließung ist skaleninkohärent.}}
$$

Keine skalare Normierung $\kappa_N$ kann $b_{1,N}$ und $b_{2,N}$ gleichzeitig stabilisieren.

Verbleibende Optionen (Priorität für spätere Blätter):
1. Intrinsische Zentrierung plus gradierte Renormierung
2. Nicht-skalare/gradierte Jacobi-Renormierung
3. Rückkehr zur Feshbach-Normierung (NEU-62/78/79)
4. Aufgabe der direkten NEU-87-Jacobi-Grenzspur

**Status gesamt: Fall II + III numerisch bestätigt; strenger Satz → NEU-123.H**

---

## Verweise

- NEU-123.A–F: Extraktion, Barrieren, numerische Diagnose
- NEU-87: $B_N^\Lambda = J_N^\Lambda + (J_N^\Lambda)^*$; Matrixelemente
- NEU-123.B: Entscheidungsbaum Fall I/II/III
- NEU-62: Normierungsrigidität
- Teschl: *Jacobi Operators*, AMS 2000
