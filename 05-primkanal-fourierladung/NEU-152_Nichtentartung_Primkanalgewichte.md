# NEU-152 — Nichtentartung der Primkanalgewichte

> Stand: 13. Juli 2026.  
> Vorgänger: NEU-151 (Normalisierungs- und Typaudit).  
> Grundlage: Rücklesung NEU-134 (12. Juli 2026), NEU-41-Quellenbefund (12./13. Juli 2026).  
> Zweck: Architektur und Prüffrage. Kein abgeschlossener Beweis.  
> Nächste freie Nummer: NEU-154.

---

## Prüffrage

Gibt es $A > 0$ und $p_0$, sodass für alle Primzahlen $p \ge p_0$

$$|c_p|^2 \ge A \frac{(\log p)^2}{p}?$$

Äquivalent (mit $R_p^{\mathrm{obs}} := \log(p)/|c_p|^2$ aus NEU-144):

$$R_p^{\mathrm{obs}} \lesssim \frac{p}{\log p}.$$

Zusammen mit der bereits gesicherten oberen Schranke (NEU-151, \S4) wäre das

$$R_p^{\mathrm{obs}} \asymp \frac{p}{\log p} \qquad\Longleftrightarrow\qquad |c_p|^2 \asymp \frac{(\log p)^2}{p}.$$

---

## 152.0 — Exakte Rücklesung der Definition von $c_p$ aus NEU-134

### 152.0.1 Die explizite Formel

Aus NEU-134, \S134.1 (Import aus NEU-41, Fourier-Hebung):

$$\widetilde{\Psi}_p = -\sum_{u\neq 0}\sum_{s,m} a_{p,u}\,\ell_{s,m}\,u\,s\,\log p\;
E^{\mathrm{rel}}_{u+ps;\,m\xrightarrow{p}pm},$$

wobei:
- $a_{p,u} \in \mathbb{C}$: Fourier-Koeffizienten der Primkanten-Hebung (aus NEU-41),
- $\ell_{s,m}$: Schleifenlängengewichte,
- $u \in \mathbb{Z}\setminus\{0\}$, $s \in \mathbb{Z}$, $m$: Kanalindex,
- $E^{\mathrm{rel}}_{u+ps;\,m\to pm}$: normierte Basisvektoren des relativen Graphraums $W_{\mathrm{res,rel}}$.

Wegen Kantendiagonalität von $W_{\mathrm{res,rel}}$ gilt:

$$|c_p|^2 = \|\widetilde{\Psi}_p\|^2_{W_{\mathrm{res,rel}}}
= (\log p)^2 \sum_m \left\|\sum_{u,s} a_{p,u}\,\ell_{s,m}\,u\,s\;
E^{\mathrm{rel}}_{u+ps;\,m\to pm}\right\|^2_{W_{\mathrm{res}}}.$$

(Dabei ist die Normkonvention $\|\varepsilon_p\| = 1$ angenommen; vgl. NEU-134, Fall A. Ob NEU-44 diese Konvention verwendet, ist in \S134.0 noch als \textbf{offene Frage} markiert — erste Arbeitsaufgabe für NEU-152.)

### 152.0.2 Normierungsfaktoren und Struktur

Die Formel zerlegts sich in zwei Teile:

$$|c_p|^2 = \underbrace{(\log p)^2}_{\text{Vorfaktor aus Hebung}} \cdot \underbrace{\sum_m \|F_{p,m}\|^2_{W_{\mathrm{res}}}}_{=: B_p},$$

mit der Abkürzung

$$F_{p,m} := \sum_{u,s} a_{p,u}\,\ell_{s,m}\,u\,s\; E^{\mathrm{rel}}_{u+ps;\,m\to pm}.$$

Die Prüffrage NEU-152 reduziert sich damit exakt auf:

$$B_p \stackrel{?}{\ge} \frac{A}{p}.$$

### 152.0.3 Faktorisierung und normierte Amplitude

Setzt man $a_p := \frac{\sqrt{p}}{\log p}\,c_p$, so ist

$$|a_p|^2 = p \cdot B_p.$$

Die Prüffrage äquivaliert zu:

$$|a_p| \ge c > 0 \quad \text{(gleichmäßig in }p\text{)}.$$

Die Größenordnung $(\log p)/\sqrt{p}$ ist durch den Vorfaktor $(\log p)^2$ und das angestrebte $B_p \sim 1/p$ bereits **in der Struktur eingebaut**. Das eigentliche Problem ist:

$$\boxed{\text{Nicht die Größenordnung ist das Hauptproblem, sondern die gleichmäßige Nichtauslöschung.}}$$

---

## 152.1 — Strukturanalyse: Was ist $a_p$?

### 152.1.1 Antwort auf die fünf Diagnosefragen

**Frage 1: Ist $c_p$ positiv, normartig, Matrixelement oder oszillatorische Summe?**

Laut NEU-134, \S134.1: $c_p$ ist eine **mehrfach indexierte oszillatorische Summe** über $(u, s, m)$ mit komplexen Vorfaktoren $a_{p,u} \cdot \ell_{s,m} \cdot u \cdot s$. Das ist **Fall C** der Architektur (NEU-151.5): Auslöschung zwischen einzelnen Termen ist strukturell möglich.

Genauer: $B_p = \sum_m \|F_{p,m}\|^2$ ist eine **Summe von Normen** (also reell und nichtnegativ). Damit ist $|c_p|^2 = (\log p)^2 B_p \ge 0$ trivialerweise erfüllt. Die Auslóschungsfrage betrifft nicht das Vorzeichen von $|c_p|^2$, sondern ob $B_p$ durch **Interferenz innerhalb jedes $F_{p,m}$** klein werden kann.

**Frage 2: Welche obere Schranke wurde tatsächlich bewiesen?**

In NEU-134 wurde die Formel aufgestellt und $A_p^{\mathrm{rel}} = p|c_p|^2 = O((\log p)^2)$ als **Szenario 2** identifiziert (unter der Annahme $B_p = O(1/p)$). Die strikte obere Schranke $|c_p|^2 = O((\log p)^2/p)$ stammt aus NEU-135.D als Normkonventionsentscheidung, nicht aus einem direkten Beweis über $B_p$.

Explizit: NEU-134 benennt als **harten Prüfstein** (\S134.6)

$$\|\widetilde{\Psi}_p\|^2_{W_{\mathrm{res,rel}}} \stackrel{?}{=} O\!\left(\frac{1}{p(\log p)^2}\right).$$

Dieser Prüfstein ist als \textbf{offen} markiert.

**Frage 3: Wo kann Auslöschung auftreten?**

Auslöschung tritt innerhalb von $F_{p,m} = \sum_{u,s} a_{p,u}\,\ell_{s,m}\,u\,s\, E^{\mathrm{rel}}_{u+ps;\,m\to pm}$ auf. Konkret:
- Die Koeffizienten $a_{p,u} \cdot u$ können mit wechselnden Vorzeichen in $u$ auftreten.
- Die Schleifenlängengewichte $\ell_{s,m} \cdot s$ enthalten weitere ganzzahlige Faktoren.
- Die Basisvektoren $E^{\mathrm{rel}}_{u+ps;\,m\to pm}$ sind orthogonal für verschiedene $u+ps$-Werte (wegen Kantendiagonalität), aber innerhalb fester $m$-Fasern nicht notwendig orthogonal für verschiedene $(u,s)$-Paare mit gleichem $u+ps$.

**Frage 4: Gibt es bereits numerische Werte von $a_p$?**

In NEU-134 sind keine numerischen Werte angegeben.

**Frage 5: Mögliche Teilfolgen mit $|a_p| \to 0$?**

Nicht untersucht. Muss Teil des Falsifikationstests (152.3) sein.

---

## 152.2 — Fallunterscheidung nach Struktur von $a_p$

**Fall A (günstig):** Es existiert $m_0(p)$ mit $\|F_{p,m_0}\|^2 \ge A/p$.  
Dann folgt $|a_p|^2 \ge pA/p = A > 0$.

**Fall B (kritisch):** Für jedes $m$ gilt $\|F_{p,m}\|^2 = o(1/p)$, aber $\sum_m \|F_{p,m}\|^2 \ge A/p$ durch kollektive Masse.

**Fall C (ungünstig):** $\sum_m \|F_{p,m}\|^2 = o(1/p)$ entlang einer Teilfolge.

**Statusmarker:** \textbf{Strukturanalyse abgeschlossen; Fallentscheidung A/B/C offen} ❓[O]

---

## 152.3 — Minimaltest auf mögliche Falschheit (Falsifikationstest)

$$|a_p| = \frac{\sqrt{p}}{\log p}\,|c_p|, \qquad \inf_{p \le P} |a_p|, \qquad \arg(c_p)$$

sowie mögliche Teilfolgen mit $|a_p| \to 0$.

**Status:** ❓[O] — Numerische Werte von $|a_p|$ fehlen.

---

## 152.4 — Abgestufte Ersatzresultate

**Stufe I** (dyadische Masse): $\sum_{P < p \le 2P} |c_p|^2 \gtrsim \log P$.  
**Stufe II** (Maximum): $\max_{P < p \le 2P} |c_p|^2 \gtrsim (\log P)^2/P$.  
**Stufe III** (positive Dichte): $\#\{p \in (P,2P] : |c_p|^2 \ge \delta (\log P)^2/P\} \ge \eta P/\log P$.  
**Stufe IV** (termweise für alle $p \ge p_0$): volle Prüffrage.

| Methode | Erreichbare Stufe | Limitierung |
|---|---|---|
| Euler-Produkt / Determinantenidentität | I | Keine Trennung einzelner Primkanäle |
| Spektraltheorie von $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}$ | II–III | Benötigt Kontrolle von $\sigma_{\min}$ |
| Direkte Analyse $a_{p,u}$ aus NEU-41 | II–IV | Benötigt Koeffizientenidentifikation |
| Winkel-/Überlappungsschranke | IV | Benötigt geometrische Trennung der Fasern |

---

## 152.5 — Kritische Importlücke: Normkonvention in NEU-44

NEU-134, \S134.0 lässt die Normkonvention für $\varepsilon_p$ ausdrücklich offen. Erst nach Verifikation von NEU-44 ist der Import aus NEU-135.D vollständig belegbar.

**Statusmarker:** ⚠[Importlücke] — Beweisschritt 0 für NEU-152

---

## 152.6 — Vorrangbarriere: NEU-153

> **Hinzugefügt 13. Juli 2026.**

Die Zielgröße $|c_p|^2$ ist derzeit **hebungsrelativ**: Sie hängt von der Wahl der Fourier-geladenen Primhebung $\widehat{\varepsilon}_p$ ab. Die Wohlbestimmtheitsbedingung (41.4) aus NEU-41 ist nicht bewiesen (Status: ❓[O]). Ihre intrinsische Wohldefiniertheit wird in **NEU-153** geprüft.

Konsequenz: Alle Aussagen zur Nichtentartung in diesem Blatt sind bis zum Abschluss von NEU-153 entweder **hebungsrelativ** oder **bedingt** (auf Ausgang I, II oder III von NEU-153).

$$\boxed{|c_p|^2 \text{ ist bis auf Weiteres hebungsrelativ. Wohldefiniertheit: NEU-153.}}$$

**Status von NEU-152:** ❓[O], abhängig von NEU-153.

---

## Offene Aufgaben für NEU-152

| Schritt | Inhalt | Voraussetzung | Status |
|---|---|---|---|
| **152-A** | Normkonvention $\varepsilon_p$ aus NEU-44 direkt lesen | NEU-44 Quellblatt | ❓[O] — Priorität 1 |
| **152-B.2** | Hebungsunabhängigkeit: Vorrang— Wohldefiniertheit von $|c_p|^2$ | **NEU-153** | ❓[O] — jetzt in NEU-153 |
| **152-B.1** | $W_{\mathrm{res}}$-Norm der Basisvektoren $E_{r,pm}$; nach NEU-153 | NEU-128B | ❓[O] |
| **152-C** | Schleifenlängengewichte $\ell_{s,m}$: Abfall in $s$, $m$-Faserstruktur | NEU-44 / NEU-41 | ❓[O] |
| **152-D** | Fallunterscheidung A/B/C entscheiden (152.2) | 152-A, 152-B, 152-C | ❓[O] |
| **152-E** | Falsifikationstest: numerische $|a_p|$ für kleine Primzahlen | 152-A, 152-B | ❓[O] |
| **152-F** | Stufenresultat I (dyadische Masse) via Euler-Produkt | 152-D | ❓[O] |
| **152-G** | Stufenresultat IV (termweise) — falls A/B gilt | 152-D | ❓[O] |

---

## Verweise

- **NEU-134**: Kanalgewichte, explizite Formel für $|c_p|^2$, drei Szenarien
- **NEU-41**: Fourier-Hebung, Koeffizienten $a_{p,u}$, Wohlbestimmtheitsbedingung (41.4)
- **NEU-44**: Relative Primkanten-Struktur, Normkonvention für $\varepsilon_p$
- **NEU-135.D**: Welt-2-Entscheidung, obere Schranke
- **NEU-151**: Typaudit, gesicherte obere Schranke
- **NEU-153**: Hebungsunabhängigkeit — Vorrangbarriere
- **NEU-128A/128B**: Kanonizität von $\Sigma_N(\beta)$, Bestätigung Status ❓[O] für (41.4)
