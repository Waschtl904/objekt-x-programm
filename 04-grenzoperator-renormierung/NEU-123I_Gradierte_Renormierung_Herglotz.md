# NEU-123.I — Gradierte Renormierung und Herglotz-Zulässigkeit

**Stand:** 6. Juli 2026  
**Anschluss:** NEU-123.G (Skaleninkohärenz), NEU-123.H (No-scalar-Lemma)  
**Nächste Einheit:** Rückkehr zu NEU-62/78/79 (Feshbach-Skala) oder NEU-123.J (gewichteter Hilbertraum)

---

## Leitprinzip

$$
\boxed{\text{Gradierte Renormierung darf nicht die Herglotz-Eigenschaft opfern.}}
$$

Die Weyl-Herglotz-Struktur ist der Grund, warum Jacobi-Operatoren überhaupt in die RH-Kette eingeführt wurden (NEU-119). Eine algebraische Stabilisierung der Jacobi-Koeffizienten, die diese Struktur zerstört, rettet die Matrix, aber nicht den Operator.

---

## 123.I.0 — Ausgangslage

Aus NEU-123.H gilt: keine skalare Normierung $\kappa_N$ stabilisiert $b_{1,N}$ und $b_{2,N}$ gleichzeitig ($\checkmark[M]$ bedingt auf $b_{2,N}/b_{1,N} \to \infty$, numerisch $\warning[M]_{\mathrm{num}}$). Die naheliegende Frage ist daher, ob eine **gradierte** Normierung die Situation rettet.

---

## 123.I.1 — Nichtunitäre Diagonalsimilarität ist nicht automatisch zulässig

Für die Similarität $\widetilde{A}_N = D_N^{-1}A_N^{Jac,-}D_N$ mit $D_N = \mathrm{diag}(d_{0,N}, d_{1,N}, \ldots)$ entstehen an der $j$-ten Kante **zwei verschiedene gerichtete Einträge**:

$$
\widetilde{b}_{j,N}^{+} = b_{j,N}\frac{d_{j,N}}{d_{j-1,N}}, \qquad
\widetilde{b}_{j,N}^{-} = b_{j,N}\frac{d_{j-1,N}}{d_{j,N}}.
$$

Im Allgemeinen $\widetilde{b}_{j,N}^{+} \neq \widetilde{b}_{j,N}^{-}$, also ist $D_N^{-1}A_N^{Jac,-}D_N$ in $\ell^2(\mathbb{N}_0)$ **nicht selbstadjungiert**. Damit ist es kein Jacobi-Operator im Sinne von NEU-119 und erzeugt keine Weyl-Herglotz-Funktion.

**Status: $\checkmark[M]$**

---

## 123.I.2 — Produktbarriere der gerichteten Kanten

Die beiden gerichteten Kanten erfüllen:

$$
\widetilde{b}_{j,N}^{+}\cdot\widetilde{b}_{j,N}^{-} = b_{j,N}^2.
$$

Wenn $b_{1,N} \to 0$, kann man durch Wahl von $D_N$ höchstens **eine Richtung** stabilisieren. Etwa $\widetilde{b}_{1,N}^{+} = 1$ erzwingt $\widetilde{b}_{1,N}^{-} = b_{1,N}^2 \to 0$. Der symmetrische Jacobi-Charakter ist unrettbar verloren.

Eine gradierte Diagonalsimilarität ist daher keine zulässige Rettung der selbstadjungierten Jacobi-Spur, solange kein neuer Hilbertraum mit passendem Skalarprodukt eingeführt und kontrolliert wird.

**Status: $\checkmark[M]$**

---

## 123.I.3 — Variante A: Gewichteter Hilbertraum

$D_N^{-1}A_N^{Jac,-}D_N$ kann selbstadjungiert sein in einem $N$-abhängigen gewichteten Hilbertraum $\ell^2(w_N)$ mit Gewichten $w_{j,N} = d_{j,N}^2$. Damit das eine Operator-Grenzspur liefert, müssen zusätzlich gezeigt werden:

1. Die Hilberträume $\ell^2(w_N)$ konvergieren in einem kontrollierten Sinn.
2. Die Weyl-Vektoren $\Omega_N$ konvergieren in dieser Hilbertraumstruktur.
3. Die Resolventen bleiben Herglotz-kompatibel.
4. Der Grenzoperator ist selbstadjungiert in einem **festen** Grenzraum.

Ohne diese vier Punkte ist die gewichtete Similarität nur eine algebraische Umformung.

**Status: ?[O]**

---

## 123.I.4 — Variante B: Symmetrische Formrenormierung

Statt Similarität eine symmetrische Formrenormierung:

$$
\widehat{A}_N = D_N A_N^{Jac,-} D_N.
$$

Dann bleiben die Matrixeinträge symmetrisch:

$$
\widehat{b}_{j,N} = d_{j-1,N}d_{j,N}\,b_{j,N}, \qquad \widehat{a}_{j,N} = d_{j,N}^2\,a_{j,N}.
$$

Das ist wieder selbstadjungiert auf $\ell^2$, aber **nicht spektral äquivalent** zu $A_N^{Jac,-}$. Zulässig nur, wenn $D_N$ intrinsisch aus Feshbach-Blockstruktur, Formnorm oder ursprünglicher Quadratform folgt. Darf nicht nachträglich aus $C_\xi$, $\{\gamma_k\}$, $\mu_\xi$, $Q_N^{Bomb}$ gewählt werden (NEU-122.0).

**Status: ?[O]**

---

## 123.I.5 — Variante C: Renormierung vor der Jacobi-Schließung

Die strukturell sauberste Möglichkeit:

$$
B_N^\Lambda \;\longrightarrow\; \widehat{B}_N^\Lambda \;\longrightarrow\; \widehat{A}_N^{Jac,-}.
$$

Nicht: $A_N^{Jac,-} \to \widetilde{A}_N$ nachträglich. Stattdessen Renormierung **vor** dem Lanczos-Schritt auf Feshbach-Blockebene, etwa durch:

- Feshbach-Norm
- Schur-Komplement-Skala
- Block-Kovarianz
- PNT-Diagonalmittel

Dann ist die gradierte Struktur nicht gefittet, sondern vom ursprünglichen Operator erzwungen.

$$
\boxed{\text{Strukturell sauberste Spur: zurück zu NEU-62/78/79 und dort die intrinsische Feshbach-Skala suchen.}}
$$

**Status: ?[O]**

---

## 123.I.6 — Entscheidungskriterium (Zulässigkeitsfilter)

| Variante | Form | Selbstadjungiert | Herglotz-kompatibel | Zulässig |
|----------|------|-----------------|---------------------|----------|
| Skalare Normierung $\kappa_N^{-1}A_N$ | $\kappa_N \in \mathbb{R}$ | ✓ | ✓ | ✗ (NEU-123.H) |
| Nichtunitäre Similarität $D_N^{-1}A_ND_N$ | in $\ell^2$ | ✗ | ✗ | **✗** |
| Gewichteter Hilbertraum | $D_N^{-1}A_ND_N$ in $\ell^2(w_N)$ | konditional | offen | ?[O] |
| Symmetrische Formren. $D_NA_ND_N$ | Quadratform | ✓ | offen | ?[O] |
| Vor-Jacobi-Renormierung $\widehat{B}_N^\Lambda$ | Feshbach-Ebene | ✓ | ✓ (intrinsisch) | ?[O] |

**Status: $\checkmark[M]$ als methodischer Filter**

---

## 123.I.F — Fazit

NEU-123.H schließt jede skalare Renormierung aus. NEU-123.I zeigt, dass eine gradierte Diagonalsimilarität $D_N^{-1}A_N^{Jac,-}D_N$ keine automatische Rettung ist — sie zerstört die Selbstadjungiertheit in $\ell^2$ und damit die Weyl-Herglotz-Eigenschaft.

### Statusmatrix

| Punkt | Status |
|-------|--------|
| Nichtunitäre Similarität als Jacobi-Rettung | $\times[M]$ |
| Produktbarriere $\widetilde{b}^+\widetilde{b}^- = b^2$ | $\checkmark[M]$ |
| Gewichteter Hilbertraum (Variante A) | ?[O] |
| Symmetrische Formrenormierung (Variante B) | ?[O] |
| Vor-Jacobi-Renormierung via Feshbach (Variante C) | ?[O] |
| Zulässigkeitsfilter als methodisches Prinzip | $\checkmark[M]$ |

---

## Verweise

- NEU-123.H: No-scalar-renormalization Lemma
- NEU-123.G: $b_{2,N}/b_{1,N} \sim N$ (numerisch)
- NEU-119: Weyl-Herglotz-Funktion; Jacobi-Operatoren und Spektraltheorie
- NEU-122.0: Anti-Fitting-Axiom
- NEU-62/78/79: Feshbach-Normierung und Blockstruktur
- Teschl: *Jacobi Operators*, AMS 2000 (Selbstadjungiertheit, Herglotz-Charakter)
- Simon: *Szegő's Theorem and Its Descendants*, Princeton 2011 (Herglotz-Repräsentation)
