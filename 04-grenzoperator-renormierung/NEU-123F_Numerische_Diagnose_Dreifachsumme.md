# NEU-123.F — Numerische Diagnose der paritätskorrigierten Dreifachsumme

**Stand:** 6. Juli 2026  
**Anschluss:** NEU-123.C (Kernidentität), NEU-123.D (paritätskorrigierte Heuristik), NEU-123.E (Sieve-Parity-Barriere)  
**Nächste Einheit:** NEU-123.G (Divisorsummenmodell $\Lambda_R$, nach ersten numerischen Daten)

---

## 123.F.0 — Ausgangspunkt

Aus NEU-123.C/D gilt:

$$
D_N := \frac{T_N}{S_N^{3/2}}, \qquad S_N = \sum_{k \leq N}\Lambda(k)^2 \sim N\log N.
$$

Paritätskorrigierte Heuristik (NEU-123.D): $T_N \asymp N^2\log N$, also

$$
D_N \asymp \sqrt{\frac{N}{\log N}}.
$$

Normalisierte Prüfgröße:

$$
\widetilde{D}_N := D_N\cdot\sqrt{\frac{\log N}{N}}.
$$

Wenn die paritätskorrigierte HL-Heuristik zutrifft: $\widetilde{D}_N \to c > 0$.  
Zusätzlich wird der reine Zweierpotenz-Anteil separat gemessen:  

$$
T_N^{(2)} := 2\log 2\sum_{2^r \leq N}\sum_{m \leq N-2^r}m\,\Lambda(m)\,\Lambda(m+2^r),
$$

$$
D_N^{(2)} := \frac{T_N^{(2)}}{S_N^{3/2}}, \qquad
\widetilde{D}_N^{(2)} := D_N^{(2)}\cdot\sqrt{\frac{\log N}{N}}.
$$

**Status: ?[O]**

---

## 123.F.1 — Zu berechnende Größen

Für jedes $N$ protokollieren:

| Größe | Definition |
|--------|------------|
| $S_N$ | $\sum_{k \leq N}\Lambda(k)^2$ |
| $T_N$ | $2\sum_{h=2}^{N}\Lambda(h)\sum_{m \leq N-h}m\,\Lambda(m)\Lambda(m+h)$ |
| $T_N^{(2)}$ | $2\log 2\sum_{2^r \leq N}\sum_{m \leq N-2^r}m\,\Lambda(m)\Lambda(m+2^r)$ |
| $D_N$ | $T_N / S_N^{3/2}$ |
| $D_N^{(2)}$ | $T_N^{(2)} / S_N^{3/2}$ |
| $\widetilde{D}_N$ | $D_N\sqrt{\log N/N}$ |
| $\widetilde{D}_N^{(2)}$ | $D_N^{(2)}\sqrt{\log N/N}$ |

Die Skalenfrage lautet: $D_N \sim \sqrt{N/\log N}$ oder nicht?

**Status: ?[O]**

---

## 123.F.2 — Diagnose-Fälle

### Fall A — Paritätskorrigierte Drift sichtbar

$\widetilde{D}_N^{(2)} \to c > 0$: Heuristik aus NEU-123.D bestätigt. $T_N^{(2)} \asymp N^2\log N$, Fall II numerisch stark gestützt.

### Fall B — Drift sichtbar, aber nicht über Zweierpotenz-Shifts

$\widetilde{D}_N$ stabilisiert, $\widetilde{D}_N^{(2)} \to 0$: Paritätsanalyse aus NEU-123.D unvollständig. Andere $\Lambda(h)$-Schichten tragen stärker.

### Fall C — Keine Drift sichtbar

$\widetilde{D}_N \to 0$: heuristische Diagonaldrift-Diagnose fraglich. Rückprüfung NEU-123.C/D erforderlich.

---

## 123.F.3 — Numerischer Mindesttest

Mindestens: $N = 10^3,\; 10^4,\; 10^5,\; 10^6$ (soweit rechnerisch möglich).

Wichtig ist nicht absolute Genauigkeit, sondern die **Skalenfrage**: Wächst $D_N$ wie $\sqrt{N/\log N}$?

---

## 123.F.4 — Methodische Sperre

Ein numerisch positiver Befund beweist **nicht** $T_N \gg N^{3/2+\varepsilon}$. Er darf nicht als $\checkmark[M]$ in die Operator-Kette eingesetzt werden. Zulässige Statusaufwertung:

$$
\warning[M]_{\mathrm{heur}} \;\longrightarrow\; \warning[M]_{\mathrm{heur+num}}.
$$

Der strenge Status ?[O] für das Minimalziel bleibt bis zu einem analytischen Beweis bestehen.

**Status: $\checkmark[M]$**

---

## 123.F.F — Fazit

NEU-123.F entscheidet numerisch, ob die in NEU-123.D/E erwartete Skala sichtbar ist. Der zentrale Plot:

$$
\boxed{\widetilde{D}_N = \frac{T_N}{S_N^{3/2}}\cdot\sqrt{\frac{\log N}{N}}.}
$$

Stabilisiert $\widetilde{D}_N$ bei positivem Wert: Fall II numerisch bestätigt.  
Fällt $\widetilde{D}_N \to 0$: Drift-Heuristik zurückzustufen.

**Status: ?[O]**

---

## Verweise

- NEU-123.C: Kernidentität $a_{1,N}/b_{1,N} = T_N/S_N^{3/2}$
- NEU-123.D: Paritätskorrektur; $T_N \asymp N^2\log N$ (HL)
- NEU-123.E: Sieve-Parity-Barriere; Modellersatz $\Lambda_R$ geplant
- NEU-122.0: Anti-Fitting-Axiom
