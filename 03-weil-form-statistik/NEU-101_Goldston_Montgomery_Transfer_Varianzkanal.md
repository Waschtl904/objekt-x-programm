# NEU-101 — Goldston–Montgomery: Transfer-Varianzkanal

**Stand:** 1. Juli 2026 | **Patch 1:** 8. August 2026 | **Patch 2:** 8. August 2026
**Prüfart:** TARGETED-REAUDIT (Patch 2: Statuskorrektur GM-Äquivalenz)
**Vorgänger:** NEU-100 (Shift-Spektrum)
**Nächste Nummer:** NEU-102

> **Patch-2-Übersicht:** Dyadische Integralgröße kanonisiert; GM-Asymptotik
> von ✓[M] unter RH auf **CONDITIONAL** (RH + Strong Pair Correlation) korrigiert.

---

## Def. NEU-101.1 — Dyadische Kurzintervall-Varianz (kanonisch)

$$\boxed{ \mathcal V(M,H) := \frac1M\int_M^{2M}(\psi(x+H)-\psi(x)-H)^2\,dx }$$

mit $\psi(x)=\sum_{n\leq x}\Lambda(n)$ (Tschebyschow-Funktion).

> **Patch-Notiz 101.1:** Frühere Fassungen und P07-Skelett verwendeten die diskrete Summenform
> $\frac1M\sum_{m\leq M}(\sum_{m<n\leq m+H}\Lambda(n)-H)^2$. Die auditierte und in NEU-101
> verwendete Standardgröße ist die dyadische Integralgröße $\mathcal V(M,H)$ oben.
> P07 hat diese Definitionen gleichzusetzen, ohne sie als getrennte Objekte einzuführen.

**Status: ✓[M]** (Definition)

---

## Satz NEU-101.2 — GM-Varianzasymptotik (CONDITIONAL)

$$\boxed{ \mathcal V(M,H) \sim H\log(M/H)
\quad\text{für }1\leq H\leq M }$$

> **Patch-Notiz 101.2 (Patch 1 + Patch 2):**
>
> *Historischer Fehler (Patch 1):* Normierung $\frac{H}{M}\log(M/H)$ (falscher $1/M$-Faktor).
> Dieser Fehler ist korrigiert; die Asymptotik $H\log(M/H)$ ist der richtige Hauptterm.
>
> *Statusfehler (Patch 2):* Das Ergebnis ist **nicht** aus RH allein bewiesen.
> Goldston–Montgomery (1987) zeigen unter RH eine **Äquivalenz** zwischen dieser
> Kurzintervall-Varianzasymptotik und der Strong Pair Correlation Conjecture:

$$\boxed{ \text{RH + Strong Pair Correlation (SPC)}
\;\Longleftrightarrow\;
\mathcal V(M,H)\sim H\log(M/H) }$$

in den entsprechenden Uniformitätsbereichen für $H$.

SPC ist nicht aus RH allein beweisbar (derzeit).

**Status: CONDITIONAL** — gilt unter RH + SPC; ?[K] (konditional)

---

## Korollar NEU-101.3 — Selbstdualer Wert (CONDITIONAL)

Der selbstduale Wert bei $H=\frac12\sqrt{M}\log M$ liefert
$$\mathcal V(M,H)\bigg|_{H=\frac12\sqrt M\log M}
\sim \tfrac12\sqrt M\log M\cdot\log\bigl(\tfrac{2M}{\sqrt M\log M}\bigr)
\sim \tfrac14\sqrt M(\log M)^2.$$

**Status: CONDITIONAL** (unter RH + SPC)

---

## Satz NEU-101.4 — Transferlemma ?[O]

Der Transfer von $\mathcal V(M,H)$ auf den Weil-Quadratikobjekt-Kanal (NEU-091 ff.)
verlangt ein explizites Transferlemma. Dieses bleibt offen.

**Status: ?[O]**

---

## Status-Übersicht

| Punkt | Inhalt | Status |
|-------|--------|--------|
| 101.1 | Dyadische Varianz $\mathcal V(M,H)$ | ✓[M] (Definition) |
| 101.2 | $\mathcal V(M,H)\sim H\log(M/H)$ | CONDITIONAL (RH + SPC) |
| 101.3 | Selbstdualer Wert | CONDITIONAL (RH + SPC) |
| 101.4 | Transferlemma zum Weil-Kanal | ?[O] |

---

## Verweise

- **Goldston, D.A., Montgomery, H.L.:** *Pair correlation of zeros and primes in short intervals*, in: Analytic Number Theory (1987), S. 183–203
- **Chan, T.H.:** *Mean values of $\xi^\prime/\xi(s)$ in the critical strip*, J. Number Theory (2004)
- NEU-096/097: Skalentriage und selbstdualer Wert
- NEU-102: Formfaktor-Kalibrierung
