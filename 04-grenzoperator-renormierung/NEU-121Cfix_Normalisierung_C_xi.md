# NEU-121.Cfix — Korrektur der $C_\xi$-Normalisierung

**Datum:** 4. Juli 2026
**Anschluss:** NEU-121, NEU-122.C
**Status:** ✓[M] — geschlossenes Korrekturblatt

> Dieses Blatt schließt den Normalisierungskonflikt aus NEU-121 und NEU-122.C.
> Es ist kein Hauptblatt, sondern ein bindendes Addendum.

---

## Cfix.1 — Definition und direkter Zahlenwert

Verwendet wird die klassische Riemannsche Xi-Funktion

$$\xi(s) = \tfrac{1}{2}\,s(s-1)\,\pi^{-s/2}\,\Gamma(s/2)\,\zeta(s).$$

Dann gilt $\xi(0) = \tfrac{1}{2}$. Der logarithmische Ableitungswert bei $s = 0$ ist

$$\frac{\xi'(0)}{\xi(0)} = -1 - \frac{\gamma_E}{2} + \frac{1}{2}\log(4\pi).$$

Daher:

$$C_\xi := -\frac{\xi'(0)}{\xi(0)} = 1 + \frac{\gamma_E}{2} - \frac{1}{2}\log(4\pi).$$

Numerische Auswertung:

$$\gamma_E \approx 0.5772156649, \qquad \tfrac{1}{2}\log(4\pi) \approx 1.2655121235,$$

$$C_\xi = 1 + 0.2886078 - 1.2655121 \approx +0.0230957.$$

$$\boxed{C_\xi = -\frac{\xi'(0)}{\xi(0)} \approx +0.0230957.}$$

✓[M]

---

## Cfix.2 — Hadamard-Summeninterpretation

Aus der Hadamard-Produktdarstellung von $\xi$ folgt formal

$$\frac{\xi'(s)}{\xi(s)} = \sum_\rho^{\mathrm{sym}} \frac{1}{s - \rho},$$

wobei die Summe symmetrisch über konjugierte Nullstellenpaare $(\rho, 1-\rho)$ ausgeführt wird.
Bei $s = 0$:

$$-\frac{\xi'(0)}{\xi(0)} = \sum_\rho^{\mathrm{sym}} \frac{1}{\rho}.$$

Damit:

$$\sum_\rho^{\mathrm{sym}} \frac{1}{\rho} = 1 + \frac{\gamma_E}{2} - \frac{1}{2}\log(4\pi) \approx +0.0230957.$$

Diese Summe ist **symmetrisch** zu verstehen (nicht als absolut konvergente rohe Summe über $1/\gamma_k$).

✓[M]

---

## Cfix.3 — Konsequenz: Sperrung des Werts $-0.549$

Der Zahlenwert $-0.549$ stimmt nicht mit $-\xi'(0)/\xi(0)$ überein.

Zwei zulässige Möglichkeiten:

| Option | Konsequenz |
|--------|-----------|
| **A** | Zielwert bleibt $C_\xi = -\xi'(0)/\xi(0)$ | Korrekter Zahlenwert ist $\approx +0.0231$; NEU-121-Angabe $-0.549$ wird korrigiert |
| **B** | Zielwert $-0.549$ ist gewollt | Dieser Koeffizient stammt aus einer anderen renormierten $\xi$-Konvention; er muss explizit als $C_\xi^{\mathrm{ren}}$ hergeleitet und von $C_\xi$ getrennt werden |

Bis eine Herleitung für Option B vorliegt:

$$\boxed{-0.549 \text{ ist als Momentzielwert gesperrt.}}$$

✓[M] für die Korrektur; ?[O] für mögliche alternative Renormierung $C_\xi^{\mathrm{ren}}$

---

## Cfix.4 — Sperrregel für künftige Momenttests

Alle künftigen Momenttests der Form

$$R_N \langle \Omega_N, A_N^{\mathrm{Jac},-} \Omega_N \rangle \;\longrightarrow\; C_\xi$$

verwenden ab jetzt:

$$\boxed{C_\xi = 1 + \frac{\gamma_E}{2} - \frac{1}{2}\log(4\pi) \approx +0.0230957.}$$

Ein anderer Zielwert ist nur erlaubt, wenn vorher eine Größe $C_\xi^{\mathrm{ren}}$ definiert und aus einer expliziten renormierten $\xi$-Konvention hergeleitet wird. Diese Herleitung muss in einem eigenen Blatt stehen und auf das Anti-Fitting-Axiom (NEU-122.0) geprüft werden.

✓[M]

---

## Cfix.F — Fazit

Der Normalisierungskonflikt aus NEU-121/NEU-122.C ist aufgelöst:

$$\boxed{C_\xi = -\frac{\xi'(0)}{\xi(0)} = \sum_\rho^{\mathrm{sym}} \frac{1}{\rho} = 1 + \frac{\gamma_E}{2} - \frac{1}{2}\log(4\pi) \approx +0.0230957.}$$

Der frühere Wert $-0.549$ ist nicht mit dieser Definition kompatibel und wird bis zu einer separaten Herleitung als $C_\xi^{\mathrm{ren}}$ gesperrt.

✓[M]

---

## Querverweise

- NEU-121: Renormierter Moment-1-Test (Zahlenwert $-0.549$ ursprünglich) ⚠[M]
- NEU-122.C: Normalisierungskonflikt festgestellt ✓[M]
- NEU-122.0: Anti-Fitting-Axiom ✓[M]
- NEU-123: Operator-Fundament (ohne $C_\xi$-Abhängigkeit) ?[O]

---

*Katalog: rh-fragenkatalog | Einheit: NEU-121.Cfix | Erstellt: 2026-07-04*
