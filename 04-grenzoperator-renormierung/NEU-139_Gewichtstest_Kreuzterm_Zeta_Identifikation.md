# NEU-139 — Von der Fredholm-Spur zur von-Mangoldt-Spur: Gewichtstest und Kreuzterm-Test

> Stand: 8. Juli 2026.  
> Anschluss: NEU-138 (Fredholm-Det., erste Spur), NEU-44.X (Rang-1, $|c_p|^2$), NEU-137 ($\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal{S}_1$).

---

## Ausgangspunkt und konzeptueller Bruch

Bis NEU-138 ist die Spurklassenmaschine vollständig:

$$\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal{S}_1 \quad (\beta>0).$$

Der neue Engpass ist **nicht mehr Topologie**, sondern **arithmetische Normalisierung**. Die Frage lautet:

$$\mathrm{Tr}\bigl(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\bigr) \stackrel{?}{=} -\frac{\zeta'}{\zeta}(\beta) = \sum_p \frac{\log p\; p^{-\beta}}{1-p^{-\beta}}.$$

NEU-137/138 liefern bisher nur:

$$\mathrm{Tr}\bigl(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\bigr) = \sum_p \frac{p^{-\beta}}{1-p^{-\beta}} |c_p|^2.$$

Ein Koeffizientenvergleich zeigt: die Identifikation mit $-\zeta'/\zeta$ hängt an zwei getrennten Tests.

---

## Test T1 — Gewichtstest

**Frage:**

$$\boxed{|c_p|^2 \stackrel{?}{=} \log p \quad \text{für alle Primzahlen } p.}$$

### 139.1.1 Was T1 bedeutet

Falls $|c_p|^2 = \log p$, folgt sofort:

$$\mathrm{Tr}\bigl(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\bigr) = \sum_p \frac{\log p\; p^{-\beta}}{1-p^{-\beta}} = -\frac{\zeta'}{\zeta}(\beta).$$

Die erste Fredholm-Spur identifiziert sich exakt mit dem von-Mangoldt-Kanal der Zetafunktion.

### 139.1.2 Verträglichkeit mit der Normabschätzung

Aus NEU-135.D gilt $|c_p|^2 = O((\log p)^2/p)$. Das ist verträglich mit $|c_p|^2 \sim \log p$ **nur falls** der führende Term tatsächlich $\log p$ lautet — d.h. falls die Abschätzung aus NEU-135.D zu grob ist und der wahre Wert $|c_p|^2 = \log p \cdot (1 + o(1))$ ist.

**Probe:** $\log p \leq (\log p)^2/p$ gilt für $p \leq e^p$, also nie für große $p$. Das heißt:

$$\log p = O\!\left(\frac{(\log p)^2}{p}\right) \iff \frac{p}{\log p} = O(1) \quad\text{— falsch für große }p.$$

**Diagnose:** $|c_p|^2 = \log p$ ist **nicht** mit der Abschätzung $|c_p|^2 = O((\log p)^2/p)$ aus NEU-135.D verträglich. Es gibt zwei Möglichkeiten:

| Szenario | Konsequenz |
|---|---|
| **T1a** Die NEU-135.D-Abschätzung ist zu grob; der wahre Wert ist $|c_p|^2 = \log p$ | Normalisierung muss revidiert werden |
| **T1b** $|c_p|^2 \neq \log p$; stattdessen $|c_p|^2 = a_p \log p$ mit $a_p \to 0$ | Spurführung über Korrekturen $d_p := |c_p|^2 - \log p$ |
| **T1c** $|c_p|^2 = \log p / p$ (logarithmisch gedämpft) | Zeta-Identifikation erfordert Renormierung um $p$ |

### 139.1.3 Spurkorrektur-Szenario (T1b)

Falls $|c_p|^2 = a_p \log p$ mit kontrollierbarem $a_p$, lautet die Spur:

$$\mathrm{Tr}\bigl(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\bigr) = \sum_p a_p \frac{\log p\; p^{-\beta}}{1-p^{-\beta}}.$$

Die Zeta-Identifikation erzwingt dann:

$$\sum_p (1-a_p) \frac{\log p\; p^{-\beta}}{1-p^{-\beta}} = 0 \quad \text{oder} \quad a_p \equiv 1.$$

Die Frage, ob $a_p \equiv 1$ aus der Konstruktion von $C_p^{\mathrm{rel}}$ folgt, ist der eigentliche Kern von T1.

**Status T1:** \u2753[O] — hängt an der expliziten Berechnung von $|c_p|^2$ aus der Definition in NEU-44.

---

## Test T2 — Kreuzterm-Orthogonalitätstest

**Frage:**

$$\boxed{\langle \Psi_p, \Psi_q \rangle = 0 \quad (p \neq q)?}$$

wobei $P_p = C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^\sharp = |\Psi_p\rangle\langle\Psi_p|$ (Rang-1, NEU-44.X).

### 139.2.1 Bedeutung für die Fredholm-Determinante

Die logarithmische Entwicklung der Fredholm-Determinante lautet:

$$\log\det(1-z\Sigma) = -\sum_{n\geq 1} \frac{z^n}{n}\,\mathrm{Tr}(\Sigma^n).$$

Für $n=2$ entsteht:

$$\mathrm{Tr}(\Sigma^2) = \left(\sum_p \frac{p^{-\beta}}{1-p^{-\beta}}\right)^2 \cdot \sum_{p,q} \frac{p^{-\beta}}{1-p^{-\beta}} \frac{q^{-\beta}}{1-q^{-\beta}} \mathrm{Tr}(P_p P_q).$$

Mit $P_p = |\Psi_p\rangle\langle\Psi_p|$ gilt:

$$\mathrm{Tr}(P_p P_q) = |\langle\Psi_p,\Psi_q\rangle|^2.$$

### 139.2.2 Zwei Szenarien

| Szenario | Konsequenz |
|---|---|
| **T2a** $\langle\Psi_p,\Psi_q\rangle = 0$ für $p\neq q$ | Alle Kreuzterme verschwinden; $\mathrm{Tr}(\Sigma^n) = \sum_p (\lambda_p)^n$; Fredholm-Det. ist reines Euler-Produkt |
| **T2b** $\langle\Psi_p,\Psi_q\rangle \neq 0$ | Zusätzliche Interferenzterme; Det. ist kein reines Euler-Produkt; Verbindung zu $\zeta$ komplizierter |

### 139.2.3 T2a: Eulerproduktsstruktur

Falls T2a gilt:

$$\det(1-z\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)) = \prod_p \left(1 - z\,\frac{p^{-\beta}}{1-p^{-\beta}}|c_p|^2\right).$$

Kombiniert mit T1 ($|c_p|^2 = \log p$):

$$\det(1-z\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)) = \prod_p \left(1 - z\,\frac{\log p\; p^{-\beta}}{1-p^{-\beta}}\right).$$

Dies ist ein Kandidat für eine **spektrale Darstellung von Null/Pol-Struktur der Riemannschen Zetafunktion**.

### 139.2.4 T2b: Interferenzterm-Kontrolle

Falls T2b gilt, müssen die Kreuzterme $|\langle\Psi_p,\Psi_q\rangle|^2$ kontrolliert werden. Eine hinreichende Bedingung für asymptotische Vernachlässigbarkeit wäre:

$$\sum_{p \neq q} |\langle\Psi_p,\Psi_q\rangle|^2 < \infty,$$

bzw. eine geeignete Abklingbedingung $|\langle\Psi_p,\Psi_q\rangle|^2 = O(1/(pq)^{1+\epsilon})$ für $\epsilon > 0$.

**Status T2:** \u2753[O] — hängt an der Geometrie des relativen Kanalraums $H_3^{\mathrm{rel}}$ und der Primorthogonalposition der Vektoren $\Psi_p$.

---

## 139.3 Gesamtdiagnose und Abhängigkeiten

```
NEU-44 (Definition C_p^rel)
         |
         v
NEU-44.X: Rang-1, |c_p|^2
         |
    _____|_____
   |           |
   v           v
 T1-Test     T2-Test
 |c_p|^2      Orth.
 = log p?     Psi_p ?
   |           |
   v           v
 Spur = -z'/z  Euler-Prod.
         |
         v
    RH-Rückbindung
```

| Test | Inhalt | Status | Abhängig von |
|---|---|---|---|
| **T1** | $|c_p|^2 \stackrel{?}{=} \log p$ | \u2753[O] | Explizite Berechnung aus NEU-44 |
| **T2** | $\langle\Psi_p,\Psi_q\rangle \stackrel{?}{=} 0$ | \u2753[O] | Geometrie von $H_3^{\mathrm{rel}}$ |
| **T1+T2** | $\mathrm{Tr}(\Sigma) = -\zeta'/\zeta$, reines Eulerprodukt | \u2753[O] | T1 \u2227 T2 |
| **RH-Bruch** | Det.-Nullstellen auf richtiger Linie | \u2753[O] | T1+T2 + Spektralanalyse |

---

## 139.4 Nächste Schritte

| Schritt | Inhalt | Priorität |
|---|---|---|
| NEU-139.T1 | Explizite Berechnung $|c_p|^2$ aus NEU-44 | 🔴 hoch |
| NEU-139.T2 | Orthogonalitätstest $\langle\Psi_p,\Psi_q\rangle$ aus Kanalgeometrie | 🔴 hoch |
| NEU-140 | Falls T1+T2: Euler-Produkt-Darstellung der Fredholm-Det. | folgt aus T1+T2 |
| NEU-141 | RH-Äquivalenz über Spektrallage | Endziel |

---

## Statusdiagnose

| Aussage | Status |
|---|---|
| $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal{S}_1$ | ✓[V] (NEU-137) |
| $\mathrm{Tr}(\Sigma) = \sum_p p^{-\beta}/(1-p^{-\beta})\cdot|c_p|^2$ | ✓[V] (NEU-138) |
| $\mathrm{Tr}(\Sigma) = -\zeta'/\zeta(\beta)$ (T1) | \u2753[O] |
| Kreuzterme $\langle\Psi_p,\Psi_q\rangle = 0$ (T2) | \u2753[O] |
| Fredholm-Det. = reines Eulerprodukt (T1+T2) | \u2753[O] |
| RH-Rückbindung | \u2753[O] — Endziel |

---

## Verweise

- **NEU-44 / NEU-44.X**: Definition $C_p^{\mathrm{rel}}$, $|c_p|^2$, Rang-1
- **NEU-134**: skalare Kanalgewichte
- **NEU-135.D**: Welt-2, Normabschätzung $|c_p|^2 = O((\log p)^2/p)$
- **NEU-137**: $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal{S}_1$
- **NEU-138**: Fredholm-Det., erste Spur
- **NEU-139.T1**: Gewichtstest (geplant)
- **NEU-139.T2**: Kreuzterm-Test (geplant)
