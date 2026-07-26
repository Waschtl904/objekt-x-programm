# NEU-162 — Quantoren- und Zulässigkeitstest für $L_3^\circ = e_1V_1$

**Stand:** 15. Juli 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-161 rev.5  
**Ziel:** Entscheidung der Quantorenfrage aus NEU-161.B: freie Einmodenwahl oder konditionaler Einzelterm?

---

## 162.A — Exakter Quantorenimport aus NEU-42 §6 und §10

### Wortlaut §6

> "Daß $h(pm) = \log p + \log m$, nicht automatisch $\log p$. Daher muss entweder
> $L_3^\circ$ auf $m=1$ projizieren, oder relativ normalisiert werden."

**Quantorenstatus §6:** $L_3^\circ$ ist hier noch **nicht festgelegt**. Die Aussage ist eine
**Bedingung**, die eine zulässige Wahl erfüllen muss — kein Verbot, keine Festlegung.
Der Wahlquantor ist **offen**. ✓ [M]

### Wortlaut §10

> "Für $\hat\varepsilon_p = e_uV_p,\ u\neq 0$ und $L_3^\circ = \ell_{s,m}e_sV_m,\ s\neq 0$:
> $$\Psi_p = -us\log(p)\ell_{s,m}\,\Pi_{J,N}(e_{u+ps}V_{pm}) \in V_{pm}\text{-Sektor.}$$
> Mit $T_p^{\mathrm{rel}}$ wirkt: $T_p^{\mathrm{rel}}\Psi_p = \log p\,\Psi_p$."

**Quantorenstatus §10:** Die Rechnung gilt **universell** für alle zulässigen Paare
$(\hat\varepsilon_p, L_3^\circ)$ der angegebenen Form. Sie ist nicht konditional auf
einen einzigen festgelegten Vektor. Das $\ell_{s,m}$ in §10 ist ein **freier Skalarparameter**,
kein aus festen Daten analytisch bestimmter Koeffizient. ✓ [M]

### Quantorenbefund

$$\boxed{
\text{NEU-42 §6 und §10 enthalten einen freien Wahlquantor für }L_3^\circ.
}$$

Die Schreibweise $L_3^\circ = \ell_{s,m}e_sV_m$ meint: **eine beliebige Einmodenwahl**
$L_3^\circ = \ell\, e_sV_m$ mit freiem $\ell\in\mathbb{C}\setminus\{0\}$, $s\neq 0$.
Nicht: ein festgelegter Vektor mit analytisch bestimmten Fourier-Koeffizienten.

Status: ✓ [M]

---

## 162.B — Zulässigkeitsklasse $\mathcal{A}_3^\circ$

Aus §6 und §10 lesen wir die genauen Bedingungen ab:

$$\mathcal{A}_3^\circ := \bigl\{\, \ell\,e_sV_m \;:\; s\neq 0,\ \ell\in\mathbb{C}\setminus\{0\},\ m=1 \text{ oder relativ normalisiert}\,\bigr\}.$$

Explizit:
- **Bedingung (i):** $s \neq 0$ (damit der Skalarfaktor $-us\log p\,\ell\neq 0$ möglich ist)
- **Bedingung (ii):** $\ell \neq 0$ (freie Wahl, nicht bewiesen werden muss)
- **Bedingung (iii):** $m = 1$ **oder** relative Normalisierung (§6-Bedingung)

Status: ✓ [M] als Definition aus Quelltext

---

## 162.C — Positiver Ausgang: $e_1V_1 \in \mathcal{A}_3^\circ$

### Prüfung

| Bedingung | Kandidat $L_3^\circ = e_1V_1$ ($s_0=1, m_0=1, \ell=1$) | Erfüllt? |
|---|---|---|
| (i) $s\neq 0$ | $s_0 = 1 \neq 0$ | ✓ |
| (ii) $\ell\neq 0$ | $\ell = 1 \neq 0$ | ✓ |
| (iii) $m=1$ oder rel. norm. | $m_0 = 1$ — erste Option direkt | ✓ |

$$\boxed{e_1V_1 \in \mathcal{A}_3^\circ.}$$

Status: ✓ [M]

### Folgerung

$$\exists\, L_3^\circ \in \mathcal{A}_3^\circ \quad\text{mit}\quad \ell_{1,1} = 1,\ s_0 = 1 \neq 0.$$

$$\boxed{\checkmark[M]_{\exists\text{-Wahl}}}$$

Der Fourierladungs-Engpass aus NEU-161.B ist damit **geschlossen**.

---

## 162.D — Universeller Skalarfaktor für alle Primzahlen

Mit $\hat\varepsilon_p = e_{u_0}V_p$, Zielindex $r_* = 1$, und $L_3^\circ = e_1V_1$:

$$u_0 = r_* - p\cdot s_0 = 1 - p.$$

Für jede Primzahl $p\geq 2$: $u_0 = 1-p \neq 0$. ✓ [M]

Der skalare Faktor der relativen Rohkopplung:

$$-u_0 s_0 \log p \cdot \ell_{s_0,m_0} = -(1-p)\cdot 1\cdot \log p\cdot 1 = (p-1)\log p \neq 0.$$

$$\boxed{-u_0 s_0 \log p\cdot\ell_{s_0,m_0} = (p-1)\log p \neq 0 \quad\text{für alle }p\geq 2.}$$

Status: ✓ [M]

Damit ist Bedingung 1 des relativen Zeugen (NEU-161.D) **universell und explizit** erfüllt.

---

## 162.E — Kanonische Zeugenparameter

$$\boxed{
L_3^\circ = e_1V_1, \qquad u_0 = 1-p, \qquad E_*^{\mathrm{rel}} = E_{1;\,1\to p}^{\mathrm{rel}}.
}$$

Die Zeugenroute NEU-161.C–E öffnet sich mit diesem universellen Kandidaten.

---

## 162.F — Verbleibende offene Bedingungen

Drei Bedingungen des relativen Zeugen (NEU-161.D) sind noch zu prüfen:

| Bedingung | Status |
|---|---|
| $-u_0s_0\log p\,\ell_{s_0,m_0}\neq 0$ | ✓ [M] — **162.D** |
| $E_*^{\mathrm{rel}} = E_{1;\,1\to p}^{\mathrm{rel}} \neq 0$ | ❓ [O] — NEU-163 |
| $E_*^{\mathrm{rel}} \notin \overline{\operatorname{span}}\{E_\lambda^{\mathrm{rel}}:\lambda\neq *\}$ (lokale Separation) | ❓ [O] — NEU-163 |
| Rohkopplung definiert Vektor des relativen Raums | ❓ [O] — NEU-163 (Konvergenzbedingung) |

---

## Statusmatrix NEU-162

| Aussage | Status |
|---|---|
| §6, §10 enthalten freien Wahlquantor für $L_3^\circ$ | ✓ [M] |
| Zulässigkeitsklasse $\mathcal{A}_3^\circ$ definiert | ✓ [M] |
| $e_1V_1 \in \mathcal{A}_3^\circ$ | ✓ [M] |
| $\checkmark[M]_{\exists\text{-Wahl}}$ für NEU-161.B | ✓ [M] |
| $(p-1)\log p \neq 0$ für alle $p\geq 2$ | ✓ [M] |
| $E_{1;\,1\to p}^{\mathrm{rel}} \neq 0$ | ❓ [O] — NEU-163 |
| Lokale Separation $E_*^{\mathrm{rel}}$ | ❓ [O] — NEU-163 |
| Rohkopplung als Hilbertraumvektor | ❓ [O] — NEU-163 |

---

## Fazit

Der Fourierladungs-Engpass (NEU-161) ist durch den Quantorentest aufgelöst:
$L_3^\circ = e_1V_1$ ist eine **freie, explizite, zulässige Wahl** in $\mathcal{A}_3^\circ$.
Der Skalarfaktor $(p-1)\log p$ ist universell für alle Primzahlen $p\geq 2$ nichtverschwindend.

$$\boxed{\text{Nächster Schritt: NEU-163 — Nichtverschwindung und Separation von }E_{1;\,1\to p}^{\mathrm{rel}}.}$$
