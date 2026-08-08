# NEU-101 — Goldston–Montgomery: Transfer-Varianzkanal

**Stand:** 1. Juli 2026 | **Patch 1:** 8. August 2026 | **Patch 2:** 8. August 2026 | **Patch 3:** 8. August 2026
**Prüfart:** TARGETED-REAUDIT (Patch 3: Synchronisation GM-Range + selbstdualer Punkt mit P07 final)
**Vorgänger:** NEU-100 (Shift-Spektrum)
**Nächste Nummer:** NEU-102

> **Patch-3-Übersicht:** Synchronisation mit `papers/P07_Weil_Form_Statistics.md` Patch 3/3 (Commit `6a162f92`):
> 1. GM-Uniformitätsbereich in 101.2 von pauschalem $1\leq H\leq M$ auf die prazise Formulierung
>    $1\leq H\leq M^{1-\varepsilon}$ (für jedes feste $\varepsilon>0$) korrigiert.
> 2. Kanonischer selbstdualer Punkt in 101.3 auf $H=\sqrt{M}$ korrigiert;
>    den Wert $\frac12\sqrt{M}\log M$ dort als Ergebnis, nicht als $H$-Wahl.

> **Patch-2-Übersicht:** Dyadische Integralgöße kanonisiert; GM-Asymptotik
> von ✓[M] unter RH auf **CONDITIONAL** (RH + Strong Pair Correlation) korrigiert.

---

## Def. NEU-101.1 — Dyadische Kurzintervall-Varianz (kanonisch)

$$\boxed{ \mathcal V(M,H) := \frac1M\int_M^{2M}(\psi(x+H)-\psi(x)-H)^2\,dx }$$

mit $\psi(x)=\sum_{n\leq x}\Lambda(n)$ (Tschebyschow-Funktion).

> **Patch-Notiz 101.1:** Frühere Fassungen und P07-Skelett verwendeten die diskrete Summenform
> $\frac1M\sum_{m\leq M}(\sum_{m<n\leq m+H}\Lambda(n)-H)^2$. Die auditierte und in NEU-101
> verwendete Standardgröße ist die dyadische Integralgöße $\mathcal V(M,H)$ oben.
> P07 hat diese Definitionen gleichzusetzen, ohne sie als getrennte Objekte einzuführen.

**Status: ✓[M]** (Definition)

---

## Satz NEU-101.2 — GM-Varianzasymptotik (CONDITIONAL)

Für jedes feste $\varepsilon>0$ gilt unter RH, uniform in $1\leq H\leq M^{1-\varepsilon}$:

$$\boxed{ \text{SPC} \;\Longleftrightarrow\; \mathcal V(M,H)\sim H\log(M/H) }$$

Die Äquivalenz ist im Sinne der Goldston–Montgomery-Uniformitätsbereiche zu verstehen.
Für $H\asymp M$ gelten abweichende Skalenregimes; die Aussage gilt nicht pauschal für alle $1\leq H\leq M$.

> **Patch-Notiz 101.2 (Patch 1 + Patch 2):**
>
> *Historischer Fehler (Patch 1):* Normierung $\frac{H}{M}\log(M/H)$ (falscher $1/M$-Faktor).
> Dieser Fehler ist korrigiert; die Asymptotik $H\log(M/H)$ ist der richtige Hauptterm.
>
> *Statusfehler (Patch 2):* Das Ergebnis ist **nicht** aus RH allein bewiesen.
> Goldston–Montgomery (1987) zeigen unter RH eine **Äquivalenz** zwischen dieser
> Kurzintervall-Varianzasymptotik und der Strong Pair Correlation Conjecture (SPC).
>
> *Rangekorrektur (Patch 3):* Pauschalem $1\leq H\leq M$ ersetzt durch
> $1\leq H\leq M^{1-\varepsilon}$ (für jedes feste $\varepsilon>0$). Synchron mit P07 §3.2.

SPC ist nicht aus RH allein beweisbar (derzeit).

**Status: CONDITIONAL** — gilt unter RH + SPC; ?[K] (konditional)

---

## Korollar NEU-101.3 — Selbstdualer Testwert (CONDITIONAL)

Der kanonische selbstduale Punkt ist $H=\sqrt{M}$. Dieser liegt im Gültigkeitsbereich von NEU-101.2
(da $\sqrt{M}=M^{1/2}\leq M^{1-\varepsilon}$ für $\varepsilon\leq\frac12$).
Konditional unter RH + SPC:
$$\boxed{ \mathcal V(M,\sqrt{M})\sim \sqrt{M}\log\sqrt{M} = \tfrac12\sqrt{M}\log M. }$$

> **Patch-Notiz 101.3 (Patch 3):** Korrektur des selbstdualen Punktes: Frühere Fassungen
> setzten irrtümlicherweise $H=\frac12\sqrt{M}\log M$ als "selbstdualen Wert"
> und erhielten $\frac14\sqrt{M}(\log M)^2$. Der kanonische selbstduale Punkt
> ist $H=\sqrt{M}$; $\frac12\sqrt{M}\log M$ ist der Varianzwert, nicht die $H$-Wahl.
> Synchron mit P07 Korollar 3.2a (Commit `6a162f92`).

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
| 101.2 | $\mathcal V(M,H)\sim H\log(M/H)$ uniform in $1\leq H\leq M^{1-\varepsilon}$ | CONDITIONAL (RH + SPC) |
| 101.3 | Selbstdualer Testwert $H=\sqrt{M}$, $\mathcal V\sim\frac12\sqrt{M}\log M$ | CONDITIONAL (RH + SPC) |
| 101.4 | Transferlemma zum Weil-Kanal | ?[O] |

---

## Verweise

- **Goldston, D.A., Montgomery, H.L.:** *Pair correlation of zeros and primes in short intervals*, in: Analytic Number Theory (1987), S. 183–203
- **Chan, T.H.:** *Mean values of $\xi^\prime/\xi(s)$ in the critical strip*, J. Number Theory (2004)
- NEU-096/097: Skalentriage und selbstdualer Wert
- NEU-102: Formfaktor-Kalibrierung
- **Synchronisation:** `papers/P07_Weil_Form_Statistics.md` Patch 3/3, Commit `6a162f92`
