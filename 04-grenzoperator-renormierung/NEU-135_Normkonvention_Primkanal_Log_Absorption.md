# NEU-135 — Normkonvention des Primkanals und Log-Absorption

> Stand: Juli 2026.  
> Anschluss: NEU-134 (Prüfstein $A_p^{rel}$), NEU-44 (Primkanal $\varepsilon_p$), NEU-41 (Fourier-Hebung).

---

## Leitfrage

$$\boxed{\text{Trägt }\varepsilon_p\text{ die Primclock-Norm }\log p\text{ bereits intrinsisch?}}$$

Oder anders formuliert:

$$\boxed{\text{Ist }\log p\text{ Kanalgewicht oder Kopplungsgewicht?}}$$

---

## 135.0 Das Problem in drei Zeilen

Aus NEU-41/134 gilt:

$$\|\widetilde{\Psi}_p\|^2_{W_{res,rel}} \sim (\log p)^2 \cdot R_p,$$

wobei $R_p$ der "Rest" nach Herausziehen des Primclock-Faktors ist.
Der normierte Kanaloperator ist:

$$\|C_p^{rel}\|^2 = \frac{\|\widetilde{\Psi}_p\|^2}{\|\varepsilon_p\|^2}.$$

Alles hängt davon ab, was $\|\varepsilon_p\|^2$ ist.

---

## 135.1 Die zwei Welten

### Welt 1: Mangoldt-Norm (Log absorbiert)

Wenn $\varepsilon_p$ die Primclock-Norm trägt:

$$\|\varepsilon_p\|_{\mathfrak{p}_N}^2 \sim (\log p)^2,$$

dann folgt:

$$\|C_p^{rel}\|^2 = \frac{(\log p)^2 \cdot R_p}{(\log p)^2} = R_p.$$

Falls zusätzlich $R_p = O(1/p)$, dann gilt:

$$A_p^{rel} = p\|C_p^{rel}\|^2 = p \cdot R_p = O(1). \quad \checkmark\text{ H3-rel stark}$$

**Physikalische Lesart:** Der Primkanal ist mit seinem natürlichen Mangoldt-Gewicht $\log p$ normiert. Die Kopplung $C_p^{rel}$ misst die Hebungsstärke relativ zu diesem Gewicht. Der $\log p$-Faktor ist dann kein "freier" Beitrag, sondern Teil der Kanalidentität.

---

### Welt 2: Standardnorm (Log nicht absorbiert)

Wenn $\varepsilon_p$ schlicht normiert ist:

$$\|\varepsilon_p\|_{\mathfrak{p}_N} = 1,$$

dann bleibt:

$$\|C_p^{rel}\|^2 = (\log p)^2 \cdot R_p.$$

Falls $R_p = O(1/p)$:

$$A_p^{rel} = p(\log p)^2 \cdot O(1/p) = O((\log p)^2). \quad \text{H3-rel nur logarithmisch}$$

**Physikalische Lesart:** Der Primclock-Faktor $\log p$ stammt aus der Mangoldt-Funktion $\Lambda(p) = \log p$ und gehört zur Kopplungsstruktur. Er ist nicht normiert weg.

---

## 135.2 Die Normfrage in der pN-Algebra

In der Primkanal-Algebra $\mathfrak{p}_N$ gibt es zwei natürliche Normen:

| Norm | Definition | $\|e_p\|^2$ |
|---|---|---|
| Standardnorm | $\|e_p\|^2 = 1$ | $1$ |
| Mangoldt-Norm | $\|e_p\|^2 = \log p$ | $\log p$ |
| Mangoldt-Quadrat-Norm | $\|e_p\|^2 = (\log p)^2$ | $(\log p)^2$ |
| $\ell^2(\mathbb{N}, \Lambda)$ | Gewichteter Raum mit $\Lambda(n)$ | $\log p$ für Primzahlen |

Die Mangoldt-Funktion $\Lambda(p) = \log p$ ist die kanonische Gewichtsfunktion der Primzahlen in der analytischen Zahlentheorie. Es ist **sehr natürlich**, dass $\varepsilon_p$ in einem gewichteten Raum sitzt, dessen Gewicht genau $\log p$ oder $(\log p)^2$ ist.

---

## 135.3 Hinweis aus der Euler-Produkt-Struktur

Der klassische Zusammenhang:

$$-\frac{\zeta'}{\zeta}(s) = \sum_p \frac{\log p}{p^s - 1} = \sum_p \sum_{k=1}^\infty \frac{\log p}{p^{ks}}$$

zeigt, dass die natürliche Gewichtung der Primzahlen in der Zeta-Funktion genau $\log p$ ist (der Mangoldt-Faktor).

Wenn die Norm auf $\mathfrak{p}_N$ konsistent mit dieser Euler-Produkt-Struktur gewählt ist, dann sollte:

$$\|\varepsilon_p\|^2 \sim \log p,$$

was Welt 1 (log teilweise absorbiert, $(\log p)^{1/2}$ statt $(\log p)^1$) oder bei quadratischer Norm Welt 1 vollständig realisiert.

---

## 135.4 Operativer Entscheidungsbaum

```
   Welche Norm hat ε_p in 𝔭_N?
           /            \
  ‖ε_p‖² ~ (log p)²   ‖ε_p‖² = 1
         |                   |
   Log absorbiert        Log nicht absorbiert
         |                   |
   A_p^rel = O(1)     A_p^rel ~ (log p)²
         |                   |
   H3-rel STARK        H3-rel LOG-VERLUST
         |                   |
   Abel direkt      verstärktes Abel nötig
```

---

## 135.5 Was in NEU-44 zu suchen ist

Konkrete Fragen an NEU-44:

1. **Wo lebt $\varepsilon_p$?** In $\ell^2(\mathbb{N})$, in $\mathfrak{p}_N$ mit Standardnorm, oder in einem gewichteten Raum?
2. **Gibt es eine explizite Normformel** für $\varepsilon_p$ oder $e_p$?
3. **Ist $\log p$ bereits als Normierungsfaktor eingebaut** (z.B. $\varepsilon_p = (\log p)^{-1} e_p$)?
4. **Wie ist die Dualität** zwischen $\mathfrak{p}_N$ und dem Wres-Raum definiert?

---

## 135.6 Statusdiagnose

| Frage | Status |
|---|---|
| Norm von $\varepsilon_p$ in $\mathfrak{p}_N$ | ❓[O] — NEU-44 muss gelesen werden |
| Log-Absorption in $\|C_p^{rel}\|^2$ | ❓[O] — abhängig von obigem |
| H3-rel stark oder mit Log-Verlust | ❓[O] — Entscheidung offen |
| Euler-Produkt-Konsistenz der Norm | ✓[M] — Mangoldt-Gewicht ist natürlich |

---

## 135.7 Klar-Entscheidungssatz

$$\boxed{\text{Log absorbiert} \Rightarrow \text{H3-rel stark, Abel direkt anwendbar.}}$$

$$\boxed{\text{Log nicht absorbiert} \Rightarrow \text{H3-rel mit logarithmischem Verlust, verstärktes Abel-Lemma nötig.}}$$

Der architektonische Unterschied zwischen beiden Welten ist:

- **Welt 1:** $C_p^{rel}$ ist ein echter Kopplunsoperator mit $1/p$-Dämpfung.
- **Welt 2:** $C_p^{rel}$ trägt noch den Primclock-Faktor $\log p$ und muss erst durch Kancellation gezogen werden.

Die Entscheidung fällt in NEU-44, nicht hier.

---

## Verweise

- **NEU-134**: Prüfstein $A_p^{rel} = O(1)$?
- **NEU-44**: Primkanal $\varepsilon_p$, Normkonvention
- **NEU-41**: Fourier-Hebung, $\log p$-Faktor
- **NEU-133**: Primschalen-Abel-Lemma
- **NEU-128B**: Warnung: $\beta = s$ gibt Weyl, keine Metrik
