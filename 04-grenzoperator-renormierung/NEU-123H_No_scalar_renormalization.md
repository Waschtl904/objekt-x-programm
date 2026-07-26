# NEU-123.H — No-scalar-renormalization Lemma

**Stand:** 6. Juli 2026  
**Anschluss:** NEU-123.G (numerischer Befund $b_{2,N}/b_{1,N} \sim N$)  
**Nächste Einheit:** NEU-123.I (gradierte Renormierung oder Feshbach-Rückkehr)

---

## 123.H.0 — Ziel

Formaler Beweis, dass kein skalarer Normierungsfaktor $\kappa_N$ beide ersten Offdiagonalen
$b_{1,N}$ und $b_{2,N}$ eines Jacobi-Operators gleichzeitig stabilisieren kann, sofern deren
Quotient divergiert.

---

## 123.H.1 — Lemma (No-scalar-renormalization)

**Lemma NEU-123.H.1.** Seien $(b_{1,N})_{N\geq1}$ und $(b_{2,N})_{N\geq1}$ zwei positive reelle Folgen mit

$$
\frac{b_{2,N}}{b_{1,N}} \to \infty \quad (N\to\infty).
$$

Dann existiert **keine** Folge $(\kappa_N)_{N\geq1}$ mit $\kappa_N > 0$ derart, dass

$$
\frac{b_{1,N}}{\kappa_N} \to c_1 \in (0,\infty)
\qquad\text{und}\qquad
\frac{b_{2,N}}{\kappa_N} \to c_2 \in (0,\infty)
$$

gleichzeitig gelten.

**Beweis.**
Angenommen, eine solche Folge $\kappa_N$ existiert. Dann:

$$
\frac{b_{2,N}}{b_{1,N}}
= \frac{b_{2,N}/\kappa_N}{b_{1,N}/\kappa_N}
\to \frac{c_2}{c_1} \in (0,\infty).
$$

Das widerspricht der Voraussetzung $b_{2,N}/b_{1,N} \to \infty$. $\square$

**Status: $\checkmark[M]$** (elementares Quotientenargument)

---

## 123.H.2 — Anwendung auf NEU-87-Jacobi-Schließung

Aus NEU-123.G (numerisch) gilt:

$$
\frac{b_{2,N}}{b_{1,N}} \sim N \to \infty.
$$

Damit sind die Voraussetzungen von Lemma NEU-123.H.1 numerisch erfüllt.

**Korollar NEU-123.H.2.** *Unter der Annahme $b_{2,N}/b_{1,N} \to \infty$ existiert keine skalare Normierung
$\kappa_N$, welche den reskalierten Operator $\kappa_N^{-1}A_N^{Jac,-}$ in einen stabilen
Jacobi-Grenzoperator mit $\widetilde{b}_1, \widetilde{b}_2 \in (0,\infty)$ überführt.*

**Status: $\checkmark[M]$ bedingt** (unter numerischem Befund $b_{2,N}/b_{1,N} \to \infty$);  
Strenger Beweis von $b_{2,N}/b_{1,N} \to \infty$: **?[O]** (hängt an Sieve-Parity-Barriere, NEU-123.E)

---

## 123.H.3 — Schärfung: was eine gradierte Renormierung leisten müsste

Das Lemma zeigt: Eine **skalare** Normierung reicht nicht. Eine gradierte (indexabhängige) Renormierung
der Form

$$
\widetilde{A}_N = D_N^{-1} A_N^{Jac,-} D_N
$$

mit einer Diagonalmatrix $D_N = \mathrm{diag}(d_{0,N}, d_{1,N}, d_{2,N}, \ldots)$ ist nicht durch das
Lemma ausgeschlossen. Sie transformiert die Jacobi-Koeffizienten als:

$$
\widetilde{a}_{j,N} = a_{j,N}, \qquad
\widetilde{b}_{j,N} = \frac{d_{j-1,N}}{d_{j,N}} b_{j,N}.
$$

Um $\widetilde{b}_{1,N} = b_{1,N}/d_{1,N} \cdot d_{0,N}$ und $\widetilde{b}_{2,N} = b_{2,N}/d_{2,N} \cdot d_{1,N}$
zu stabilisieren, müsste:

$$
\frac{d_{0,N}}{d_{1,N}} \sim \frac{1}{b_{1,N}} \sim \sqrt{\frac{N}{\log N}},
\qquad
\frac{d_{1,N}}{d_{2,N}} \sim \frac{1}{b_{2,N}} \sim \frac{\sqrt{N}}{\log N}.
$$

Diese gradierten Skalierungen wären **nicht** intrinsisch aus einer einzigen Operatorgröße herleitbar —
es sei denn, die Indexabhängigkeit folgt aus einer eigenständigen arithmetischen Struktur.

**Frage für NEU-123.I:** Gibt es in der Feshbach-Architektur (NEU-62/78/79) eine intrinsische
gradiierte Normierung?

**Status: ?[O]**

---

## 123.H.4 — Sperrvermerk: keine externe Normierung

Eine gradierte Renormierung darf nicht anhand von:
- Riemann-Nullstellen $\gamma_k$
- $C_\xi \approx +0.0231$ (NEU-121.Cfix)
- Bombieri-Gewichten $Q_N^{Bomb}$
- anderen Zeta-Zieldaten

konstruiert werden. Jede zulässige gradierte Normierung muss aus der Operatorstruktur von
$A_N^{Jac,-}$ selbst folgen (Anti-Fitting-Axiom, NEU-122.0).

**Status: $\checkmark[M]$ (Sperrvermerk)**

---

## 123.H.F — Fazit

$$
\boxed{\text{Lemma NEU-123.H.1: Keine skalare Normierung } \kappa_N \text{ kann } b_{1,N} \text{ und } b_{2,N} \text{ gleichzeitig stabilisieren, falls } b_{2,N}/b_{1,N} \to \infty.}
$$

Korollar: Die NEU-87-Jacobi-Schließung besitzt keine stabile skalare Grenzoperator-Spur.

Der Beweis des Lemmas ist elementar ($\checkmark[M]$). Die Anwendung ist **bedingt** auf den
numerischen Befund $b_{2,N}/b_{1,N} \to \infty$ ($\warning[M]_{\mathrm{num}}$); streng hängt sie
an der Sieve-Parity-Barriere (NEU-123.E, ?[O]).

### Statusmatrix

| Punkt | Status |
|-------|--------|
| Lemma NEU-123.H.1 (reine Analysis) | $\checkmark[M]$ |
| Anwendung: $b_{2,N}/b_{1,N} \to \infty$ numerisch | $\warning[M]_{\mathrm{num}}$ |
| Anwendung streng | ?[O] (Sieve-Parity-Barriere) |
| Sperrvermerk gegen externe Normierung | $\checkmark[M]$ |
| Gradierte Renormierung aus Feshbach-Struktur | ?[O] → NEU-123.I |

---

## Verweise

- NEU-123.G: numerischer Befund $b_{2,N}/b_{1,N} \sim N$
- NEU-123.E: Sieve-Parity-Barriere; $T_N \gg N^{3/2+\varepsilon}$ streng offen
- NEU-122.0: Anti-Fitting-Axiom
- NEU-62: Normierungsrigidität
- NEU-78/79: Feshbach-Normierung
- Teschl: *Jacobi Operators*, AMS 2000, Kap. 1 (Jacobi-Matrizen und Spektraltheorie)
