# NEU-44.R — Rückbindung: NEU-44.X/X' schließt NEU-137 Schritte S1 und S2

> Stand: 8. Juli 2026.  
> Typ: Verifikationseintrag (Rücklese).  
> Anschluss: NEU-44.X, NEU-44.X', NEU-137.

---

## Zweck

NEU-137.5 enthält eine offene Schritt-Liste:

| Schritt | Inhalt | Alter Status |
|---|---|---|
| S1 | Rang-Struktur von $C_p^{rel}$ verifizieren | ❓[O] |
| S2 | $\|C_p^{rel}(C_p^{rel})^\sharp\|_{\mathcal{S}_1} \leq \|C_p^{rel}\|^2$ formal beweisen | ❓[O] |
| S3 | $\sum_p (\log p)^2/p^{1+\beta} < \infty$ für $\beta > 0$ | ✓[M] |
| S4 | Gleichmäßigkeit in $\beta \geq \beta_0$ | ❓[O] |
| S5 | Fredholm-Determinante | ❓[O] — Folgeprogramm |

Dieser Eintrag schließt S1 und S2.

---

## 44.R.1 Abschluss von S1

**NEU-44.X, Satz 44.X.1** beweist: $C_p^{rel}$ ist Rang-1-Operator.

**NEU-44.X', Abschnitt 44.X'.1–2** zeigt: Die Rang-1-Eigenschaft bleibt stabil unter Lanczos-Grenzübergang und Gramform-Triage (Rang uniformly beschränkt).

$$\Rightarrow \text{S1: } \checkmark\text{[V]}$$

---

## 44.R.2 Abschluss von S2

**NEU-44.X, Korollar 44.X.2** liefert für Rang-1-Operatoren die exakte Gleichheit:

$$\left\|C_p^{rel}(C_p^{rel})^\sharp\right\|_{\mathcal{S}_1} = \|C_p^{rel}\|^2 = |c_p|^2.$$

Damit gilt sogar Gleichheit (nicht nur $\leq$) in S2.

$$\Rightarrow \text{S2: }\checkmark\text{[V]}$$

---

## 44.R.3 Konsequenz für NEU-137

Mit S1 ✓ und S2 ✓ sowie dem bekannten S3 ✓ folgt der Kernsatz von NEU-137 vollständig:

$$\boxed{\Sigma_{rel}^{ren}(\beta) \in \mathcal{S}_1 \quad \text{für jedes feste } \beta > 0,}$$

gleichmäßig für $\beta \geq \beta_0 > 0$ (S4 folgt unmittelbar aus der dominierenden Reihe $\sum_p (\log p)^2/p^{1+\beta_0} < \infty$).

$$\Rightarrow \text{S4: }\checkmark\text{[V]} \text{ (durch Majorantenargument aus S2+S3)}$$

---

## 44.R.4 Aktualisierter Statusblock NEU-137.5

| Schritt | Inhalt | Neuer Status |
|---|---|---|
| S1 | Rang-Struktur von $C_p^{rel}$ | ✓[V] — NEU-44.X |
| S2 | Spurklassen-Abschätzung | ✓[V] — NEU-44.X, Kor. 44.X.2 |
| S3 | Summierbarkeit $\sum_p (\log p)^2/p^{1+\beta}$ | ✓[M] |
| S4 | Gleichmäßigkeit $\beta \geq \beta_0$ | ✓[V] — Majorantenargument |
| S5 | Fredholm-Determinante | ❓[O] — Folgeprogramm |

**Der Kernsatz von NEU-137 ist damit vollständig bewiesen** (unter den Annahmen aus NEU-134, NEU-135.D, NEU-44).

---

## Verweise

- **NEU-44.X**: Rang-1-Beweis
- **NEU-44.X'**: Stabilität
- **NEU-137**: Spurklassen-Verifikation
- **NEU-134**: skalare Koeffizienten $c_p$
- **NEU-135.D**: Norm-Abschätzung
