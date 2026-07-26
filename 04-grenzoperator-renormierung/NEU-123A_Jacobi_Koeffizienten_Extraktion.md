# NEU-123.A — Erste Jacobi-Koeffizienten: Extraktion aus NEU-86/87

**Stand:** 5. Juli 2026  
**Anschluss:** NEU-123 (Jacobi-Grenzoperator, Resolventenkonvergenz), NEU-86/87  
**Nächste Einheit:** NEU-123.B (Konvergenz $a_{j,N} \to a_j$, $b_{j,N} \to b_j$)

---

## Indexkonvention (Sperrvermerk)

NEU-121 verwendete $a_1$ für den ersten Diagonaleintrag.  
Ab NEU-123 gilt verbindlich:

$$
\boxed{\text{Lanczos-Basis startet bei }q_{0,N};\quad\text{erster Diagonaleintrag ist }a_{0,N}.}
$$

Ein Off-by-one zwischen Moment-1-Test und Jacobi-Rekursion ist damit gesperrt.  
**Status: ✓[M] (Konvention)**

---

## Ausgangsobjekt: $A_N^{Jac,-}$

Aus NEU-86/87 ist der relevante selbstadjungierte Operator:

$$
A_N^{Jac,-} \;=\; B_N^\Lambda \;=\; J_N^\Lambda + (J_N^\Lambda)^*
$$

auf $\ell^2(I_N)$, $I_N = \{1,\ldots,N\}$, mit

$$
\langle \delta_s,\, J_N^\Lambda\,\delta_r\rangle
= \frac{\gamma r}{N}\,\Lambda(s-r)\cdot\mathbf{1}_{s>r,\;s-r\leq N-r}.
$$

Die symmetrisierten Matrixelemente (NEU-87) sind:

$$
\langle \delta_s,\, A_N^{Jac,-}\,\delta_r\rangle
= \frac{\gamma\,\min(r,s)}{N}\,\Lambda(|s-r|)\cdot\mathbf{1}_{|s-r|\geq 2},
$$

mit Trunkierung durch $I_N$.  
**Status: ✓[M]**

---

## Startvektor

$$
q_{0,N} := \delta_1 \;\in\;\ell^2(I_N).
$$

> **Bemerkung:** Falls in einem späteren Blatt $\Omega_N$ als normierter GNS-Vektor verwendet wird, muss $q_{0,N} = \Omega_N$ gesetzt und die Übereinstimmung $\Omega_N = \delta_1$ oder eine abweichende Wahl explizit begründet werden. Bis dahin gilt $q_{0,N} = \delta_1$.

---

## Lanczos-Schritt 0 → $a_{0,N}$

$$
a_{0,N}
= \langle q_{0,N},\, A_N^{Jac,-}\,q_{0,N}\rangle
= \langle \delta_1,\, A_N^{Jac,-}\,\delta_1\rangle.
$$

Aus den Matrixelementen: $|s - 1| \geq 2$ verlangt $s \geq 3$. Damit:

$$
\langle \delta_s,\, A_N^{Jac,-}\,\delta_1\rangle
= \frac{\gamma\cdot 1}{N}\,\Lambda(s-1)\cdot\mathbf{1}_{s \geq 3}.
$$

Für $s = 1$ (Diagonale): $|1-1|=0 < 2$, also **kein Beitrag**.

$$
\boxed{a_{0,N} = 0.}
$$

**Status: ✓[M]**

> **Mechanismus:** Der Ausschluss $|s-r| \geq 2$ in $B_N^\Lambda$ sperrt alle Sprünge der Länge $0$ und $1$.  
> Da $\Lambda(1) = 0$ (keine Primzahlpotenz bei $n=1$) und der Diagonalterm $n=0$ nicht existiert, ist der erste Lanczos-Diagonaleintrag exakt null.

---

## Lanczos-Schritt 0 → Residuum $r_{1,N}$ und $b_{1,N}$

$$
r_{1,N} = A_N^{Jac,-}\,q_{0,N} - a_{0,N}\,q_{0,N}
= A_N^{Jac,-}\,\delta_1.
$$

Explizit:

$$
A_N^{Jac,-}\,\delta_1
= \sum_{s \geq 3}^{N} \frac{\gamma}{N}\,\Lambda(s-1)\,\delta_s
= \frac{\gamma}{N}\sum_{n=2}^{N-1}\Lambda(n)\,\delta_{1+n}.
$$

(Die Trunkierung ergibt $s = 1+n \leq N$, also $n \leq N-1$.)

$$
b_{1,N} = \|r_{1,N}\| = \frac{\gamma}{N}\sqrt{\sum_{n=2}^{N-1}\Lambda(n)^2}.
$$

Mit $\sum_{n\leq N}\Lambda(n)^2 \asymp N\log N$:

$$
\boxed{b_{1,N} \asymp \frac{\gamma}{N}\sqrt{N\log N} = \frac{\gamma\sqrt{\log N}}{\sqrt{N}} \;\longrightarrow\; 0.}
$$

**Status: ✓[M] (Größenordnung); ?[O] (Grenzwert $b_1 := \lim_{N\to\infty} b_{1,N}$ — Stufe NEU-123.B)**

---

## Lanczos-Schritt 1 → $q_{1,N}$, $a_{1,N}$, $b_{2,N}$

$$
q_{1,N} = \frac{r_{1,N}}{b_{1,N}}
= \frac{\sum_{n=2}^{N-1}\Lambda(n)\,\delta_{1+n}}{\sqrt{\sum_{n=2}^{N-1}\Lambda(n)^2}}.
$$

### Diagonaleintrag $a_{1,N}$

$$
a_{1,N} = \langle q_{1,N},\, A_N^{Jac,-}\,q_{1,N}\rangle.
$$

Mit $q_{1,N} = \frac{1}{b_{1,N}N/\gamma}\sum_{n}\Lambda(n)\delta_{1+n}$ ergibt sich:

$$
a_{1,N}
= \frac{1}{\|r_{1,N}\|^2}
  \sum_{n,m=2}^{N-1}\Lambda(n)\Lambda(m)
  \langle\delta_{1+n},\,A_N^{Jac,-}\,\delta_{1+m}\rangle.
$$

Die Matrixelemente:

$$
\langle\delta_{1+n},\,A_N^{Jac,-}\,\delta_{1+m}\rangle
= \frac{\gamma\min(1+n,1+m)}{N}\,\Lambda(|n-m|)\cdot\mathbf{1}_{|n-m|\geq 2}.
$$

Also:

$$
\boxed{a_{1,N}
= \frac{\gamma/N}{\sum_{k}\Lambda(k)^2}
  \sum_{\substack{n,m \geq 2 \\ |n-m|\geq 2}}
  \Lambda(n)\Lambda(m)\,(1+\min(n,m))\,\Lambda(|n-m|).}
$$

**Status: ✓[M] (Formel); ?[O] (asymptotische Auswertung — NEU-123.B)**

### Zweites Residuum und $b_{2,N}$

$$
r_{2,N} = A_N^{Jac,-}\,q_{1,N} - a_{1,N}\,q_{1,N} - b_{1,N}\,q_{0,N},
$$

$$
b_{2,N} = \|r_{2,N}\|.
$$

Die explizite Formel folgt aus den obigen Matrixelementen; sie ist eine gewichtete Doppelsumme in $\Lambda(n)^2\Lambda(m)$.  
**Status: ?[O] (explizite Auswertung — NEU-123.B)**

---

## Kernbefund: Diagnose für NEU-123.B

| Koeffizient | Wert / Größenordnung | Status |
|-------------|---------------------|--------|
| $a_{0,N}$ | $= 0$ exakt | ✓[M] |
| $b_{1,N}$ | $\asymp \gamma\sqrt{\log N}/\sqrt{N} \to 0$ | ✓[M] Größe; ?[O] Grenzwert |
| $a_{1,N}$ | Doppelsumme in $\Lambda^3$, Formel oben | ✓[M] Formel; ?[O] Limes |
| $b_{2,N}$ | Doppelsumme in $\Lambda^2 \cdot \Lambda$, Formel folgt | ?[O] |

**Kritische Beobachtung:** $b_{1,N} \to 0$.  
Das bedeutet: Wenn $b_{1,N} \to 0$, dann degeneriert der Jacobi-Operator im Limes zu einem Diagonal-Operator mit $a_{j,\infty}$ auf der Diagonalen und $b_{j,\infty} = 0$. Das Spektralmaß von $A_\infty$ wäre dann diskret und durch $\{a_{j,\infty}\}$ bestimmt — **kein** absolutstetiges Spektrum.

Das ist der erste echte Operator-Test der Blockkette. Er muss in NEU-123.B explizit adressiert werden:

$$
\boxed{b_{1,N} \to 0 \;\Rightarrow\; \text{Jacobi-Limes degeneriert: } A_\infty \text{ diagonal. Kein GUE-Spektrum ohne Renormierung.}}
$$

**Status: ⚠[M] — kritische Warnung für NEU-123.B**

---

## Sperrvermerk für NEU-123.B

NEU-123.B darf den Jacobi-Limes $A_\infty$ **nicht** als selbstverständlich nicht-degeneriert annehmen.  
Die Frage, ob eine Reskalierung $\tilde{b}_{j,N} = b_{j,N}/\kappa_N$ für eine geeignete Folge $\kappa_N \to 0$ einen nicht-trivialen Limes ergibt, muss explizit untersucht werden.

---

## Verweise

- NEU-86: Nilpotenz-Barriere; $J_N^\Lambda$ nilpotent
- NEU-87: Jacobi-Schließung; $B_N^\Lambda = J_N^\Lambda + (J_N^\Lambda)^*$; Matrixelemente
- NEU-123: Jacobi-Grenzoperator; Resolventenkonvergenz (Rahmen)
- NEU-121.Cfix: $C_\xi \approx +0.0231$; gesperrter Zielwert $-0.549$
- NEU-62: Normierungsrigidität, Jacobi-Limes
- Simon: *Trace Ideals*, AMS 2005
- Teschl: *Jacobi Operators and CMV Matrices*, AMS 2000
