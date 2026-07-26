# NEU-134 — Extraktion der relativen Kanalgewichte aus NEU-44

> Stand: Juli 2026.  
> Anschluss: NEU-133 (Primschalen-Abel-Lemma), NEU-44 (relative Primkanten-Struktur).  
> **Kernfrage:** Ist $A_p^{rel} = p\|C_p^{rel}\|^2$ beschränkt?

---

## Leitmotiv

$$\boxed{\text{Hat Objekt }X\text{ operative Prä-Lanczos-Positivität — oder nur eine elegante relative Buchhaltung?}}$$

Die Antwort hängt vollständig davon ab, ob

$$\boxed{p\|C_p^{rel}\|^2 = O(1).}$$

---

## 134.0 Normkonvention für $\varepsilon_p$

Aus NEU-44 gilt:

$$C_p^{rel}\varepsilon_p = \widetilde{\Psi}_p \in \bigoplus_m H_{m\xrightarrow{p}pm}.$$

**Fall A:** $\varepsilon_p$ normiert, $\|\varepsilon_p\|_{\mathfrak{p}_N} = 1$.
Dann direkt:
$$\|C_p^{rel}\|^2 = \|\widetilde{\Psi}_p\|_{W_{res,rel}}^2.$$

**Fall B:** $\varepsilon_p$ nicht normiert (z.B. $\varepsilon_p = e_p$, Standardbasisvektor).
Dann:
$$\|C_p^{rel}\|^2 = \frac{\|\widetilde{\Psi}_p\|_{W_{res,rel}}^2}{\|\varepsilon_p\|_{\mathfrak{p}_N}^2}.$$

**Offene Frage:** Welche Normkonvention wird in NEU-44 verwendet?
Die Antwort bestimmt, ob die $1/p$-Dämpfung im Zähler oder Nenner sitzt.

---

## 134.1 Formel für $\|\widetilde{\Psi}_p\|_{W_{res,rel}}^2$

Aus NEU-41 hat die Hebung die Form:

$$\widetilde{\Psi}_p = -\sum_{u\neq 0}\sum_{s,m} a_{p,u}\ell_{s,m}\,u\,s\,\log p\; E^{rel}_{u+ps;\,m\xrightarrow{p}pm}.$$

Wegen Kantendiagonalität von $W_{res,rel}$:

$$\|\widetilde{\Psi}_p\|^2_{W_{res,rel}}
= (\log p)^2 \sum_m \left\|\sum_{u,s} a_{p,u}\ell_{s,m}\,u\,s\,
E^{rel}_{u+ps;\,m\xrightarrow{p}pm}\right\|^2_{W_{res}}.$$

---

## 134.2 Die Kernbilanz: Woher kommt $1/p$?

Die normierte Schalenenergie lautet dann:

$$A_p^{rel} = p\|C_p^{rel}\|^2
= p(\log p)^2 \sum_m \left\|\sum_{u,s} a_{p,u}\ell_{s,m}\,u\,s\,
E^{rel}_{u+ps;\,m\xrightarrow{p}pm}\right\|^2_{W_{res}}.$$

Damit $A_p^{rel} = O(1)$ gilt, muss der Gesamtausdruck
$p(\log p)^2 \cdot (\ldots)$ beschränkt sein. Das bedeutet:

$$\sum_m \left\|\sum_{u,s} a_{p,u}\ell_{s,m}\,u\,s\,
E^{rel}_{u+ps;\,m\xrightarrow{p}pm}\right\|^2_{W_{res}}
= O\!\left(\frac{1}{p(\log p)^2}\right).$$

**Die $1/p$-Dämpfung muss in der Fourier-Hebung selbst entstehen** —
entweder durch:

| Quelle | Mechanismus |
|---|---|
| $a_{p,u} \sim (p\log p)^{-1}$ | Fourier-Koeffizientenabfall |
| $\|E^{rel}_{u+ps;\ldots}\|_{W_{res}} \sim p^{-1/2}$ | Gewichtsnorm der Basis |
| $\ell_{s,m} \sim p^{-\alpha}$ | Schleifenlängen-Abfall |
| Kombination der drei | Synergistische Dämpfung |

---

## 134.3 Drei Szenarien und ihre Konsequenzen

**Szenario 1: $A_p^{rel} \leq C$ (H3-rel gilt)**

$$\sum_{p\sim 2^m}\|C_p^{rel}\|^2 = O\!\left(\frac{1}{m}\right).$$

Die dyadische Primschalen-Schalenenergie fällt harmonisch ab. Das Primschalen-Abel-Lemma (NEU-133) ist anwendbar. Die Doppelbarriere hat eine operative Lösung.

**Szenario 2: $A_p^{rel} \sim (\log p)^2$**

$$\sum_{p\sim 2^m}\|C_p^{rel}\|^2 = O\!\left(\frac{m^2}{m}\right) = O(m).$$

Die Schalenenergie wächst logarithmisch. Kancellation durch H1-rel müss
stärker sein als $O(1/m)$ — schwierig, aber nicht ausgeschlossen.

**Szenario 3: $A_p^{rel} \sim p^\alpha$, $\alpha > 0$**

$$\sum_{p\sim 2^m}\|C_p^{rel}\|^2 = O\!\left(\frac{2^{m\alpha}}{m}\right) \to \infty.$$

Exponentielles Wachstum. H3-rel verletzt. Das Primschalen-Abel-Lemma bricht zusammen. Die relative Self-Energy $\Sigma_{rel,N}(\beta_0)$ wäre zwar positiv, aber ohne Summationskontrolle.

---

## 134.4 Mangoldt-Warnung: $\log p$-Faktor

Die Formel enthält explizit $(\log p)^2$ als Vorfaktor aus der Hebungsstruktur.
Das ist nicht trivial:

$$\sum_{p\sim 2^m}\frac{(\log p)^2}{p} \sim m.$$

Selbst wenn $\|\widetilde{\Psi}_p\|^2_{W_{res,rel}} \sim p^{-1}$ gilt (Szenario 1 ohne den $\log$-Faktor), ergibt sich:

$$A_p^{rel} = p(\log p)^2 \cdot O(p^{-1}) = O((\log p)^2).$$

Das wäre Szenario 2. Der $\log p$-Faktor aus der Primkanten-Hebung ist also
**genau der kritische Term**, der über Szenario 1 vs. 2 entscheidet.

$$\boxed{\text{Schlüsselfrage: Liegt }\|\widetilde{\Psi}_p\|^2_{W_{res,rel}} = O\bigl(p^{-1}(\log p)^{-2}\bigr)\text{ oder nur }O(p^{-1})?}$$

---

## 134.5 Statusdiagnose

| Größe | Status | Abhängigkeit |
|---|---|---|
| Normkonvention für $\varepsilon_p$ | ❓[O] | NEU-44 muss gelesen werden |
| $\|\widetilde{\Psi}_p\|^2_{W_{res,rel}}$ explizit | ❓[O] | Formel steht, Abschätzung offen |
| $A_p^{rel} \leq C$ (H3-rel) | ❓[O] | Szenario 1 vs. 2 vs. 3 |
| Szenario 1: Abel anwendbar | ❓[O] | abhängig von $\log p$-Verhalten |

$$\boxed{\checkmark[M]\text{ Formel aufgestellt.}\quad ?[O]\text{ quantitative Abschätzung.}}$$

---

## 134.6 Der neue harte Prüfstein

$$\boxed{\left\|\widetilde{\Psi}_p\right\|^2_{W_{res,rel}} \stackrel{?}{=} O\!\left(\frac{1}{p(\log p)^2}\right).}$$

Wenn ja: $A_p^{rel} = O(1)$, H3-rel gilt, das Primschalen-Abel-Lemma greift.
Wenn nein: Die Doppelbarriere bleibt ein Kancellationsproblem ohne operative Lösung über diesen Weg.

---

## Verweise

- **NEU-133**: Primschalen-Abel-Lemma — die drei Schlüsselgrößen
- **NEU-44**: Relative Primkanten-Struktur, $C_p^{rel}$-Definition
- **NEU-41**: Fourier-Hebung $\psi_p$, Koeffizientenstruktur
- **NEU-128B**: Warnung $\beta = s$: Weyl-Funktion, keine Metrik
- **NEU-125**: Skalare Renormierung unzureichend
