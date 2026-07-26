# NEU-151 — Normalisierungs- und Typaudit der Primkanaloperatoren

> Stand: 11. Juli 2026.
> Vorgänger: NEU-150 (Rückbindung Mellin-Operator-Spur).
> Zweck: Reines Normalisierungs- und Typaudit. Kein Beweis neuer Abschätzungen.
> Nächste freie Nummer: NEU-152.

---

## 151.0 — Definitionen und Quellenimport

**Import aus NEU-44.X (Stand 8. Juli 2026):**

Der relative Primkanaloperator $C_p^{\mathrm{rel}}$ ist definiert als

$$C_p^{\mathrm{rel}} := c_p \cdot \bigl(e_1^{(p)} \otimes f_3^{(p)*}\bigr),$$

wobei:
- $e_1^{(p)} \in H_1$: normierter Basisvektor des ersten Schichtkanals, $\|e_1^{(p)}\| = 1$,
- $f_3^{(p)} \in H_3^{\mathrm{rel}}$: normierter Basisvektor des relativen dritten Schichtkanals, $\|f_3^{(p)}\| = 1$,
- $c_p \in \mathbb{C}$: skalarer Kanalgewichtskoeffizient zum Prim $p$ (Extraktion: NEU-134, Normkonvention: NEU-135.D).

Der primäre Eigenvektor-Kandidat ist:
$$\Psi_p := C_p^{\mathrm{rel}} f_3^{(p)} = c_p \cdot e_1^{(p)}.$$

Der zugehörige Dichte-Operator ist:
$$P_p := C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^* = |c_p|^2 \cdot \bigl|e_1^{(p)}\bigr\rangle\!\bigl\langle e_1^{(p)}\bigr|.$$

**Statusmarker:** ✅[Import, NEU-44.X]

---

## 151.1 — Rang-eins-Struktur von $C_p^{\mathrm{rel}}$

**Satz 151.1:** $C_p^{\mathrm{rel}}$ ist ein Rang-1-Operator.

**Beweis (Import aus NEU-44.X, Satz 44.X.1):**
Das Bild von $C_p^{\mathrm{rel}}$ ist $\mathrm{span}(c_p \cdot e_1^{(p)})$, also eindimensional.
Da $c_p \neq 0$ für alle Primzahlen $p$ (NEU-134), gilt $\mathrm{rank}(C_p^{\mathrm{rel}}) = 1$. $\square$

**Stabilität unter Approximationen (Import aus NEU-44.X'):**
Die Rang-1-Eigenschaft bleibt erhalten:
- unter normkonvergenten Lanczos-Grenzwerten $c_p^{(N)} \to c_p$ (NEU-123),
- unter Gramform-Triage (NEU-127): der Rang bleibt $\leq$ const (uniformly in $p$), was für die Spurklassen-Summierbarkeit genügt.

**Statusmarker:** ✅[Import, NEU-44.X] für Rang-1; ✅[M] für Stabilität

---

## 151.2 — Exakter Normkollaps

Für einen Rang-1-Operator der Form $C_p^{\mathrm{rel}} = c_p \cdot (e_1^{(p)} \otimes f_3^{(p)*})$ mit $\|e_1^{(p)}\| = \|f_3^{(p)}\| = 1$ kollabieren alle drei Normen auf Ebene der Singulärwerte:

$$\|C_p^{\mathrm{rel}}\|_{\mathrm{op}} = \|C_p^{\mathrm{rel}}\|_{\mathcal{S}_2} = \|C_p^{\mathrm{rel}}\|_{\mathcal{S}_1} = |c_p|.$$

Auf der quadrierten Ebene:

$$\|C_p^{\mathrm{rel}}\|_{\mathrm{op}}^2 = \|C_p^{\mathrm{rel}}\|_{\mathcal{S}_2}^2 = |c_p|^2.$$

Da $\Psi_p = C_p^{\mathrm{rel}} f_3^{(p)} = c_p e_1^{(p)}$ mit dem normerreichenden Vektor $f_3^{(p)}$ definiert ist, gilt:

$$\|\Psi_p\|^2 = |c_p|^2.$$

Für $P_p = C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^* = |c_p|^2 \cdot |e_1^{(p)}\rangle\langle e_1^{(p)}|$ gilt separat:

$$\|P_p\|_{\mathrm{op}} = \|P_p\|_{\mathcal{S}_1} = \mathrm{Tr}(P_p) = |c_p|^2.$$

**Zentrale Identität:**

$$\boxed{\|\Psi_p\|^2 = \|C_p^{\mathrm{rel}}\|_{\mathrm{op}}^2 = \|C_p^{\mathrm{rel}}\|_{\mathcal{S}_2}^2 = \mathrm{Tr}(P_p) = |c_p|^2}$$

**Wichtige Abgrenzung:** Die beiden Normkollapse dürfen nicht in einer einzigen Kette vermischt werden:
- $\|C_p^{\mathrm{rel}}\|_{\mathcal{S}_1} = |c_p|$ (nicht $|c_p|^2$),
- $\|P_p\|_{\mathcal{S}_1} = |c_p|^2$ (nicht $|c_p|$).

**Statusmarker:** ✅[M] (direkte Rechnung aus dem NEU-44.X-Modell; gilt innerhalb dieses Modells ohne weitere offene Hypothesen)

---

## 151.3 — Typaudit: $P_p$ ist kein Projektor

**Satz 151.2:** $P_p$ ist im Allgemeinen **kein orthogonaler Projektor**.

**Beweis:**

$$P_p^2 = \bigl(|c_p|^2 \cdot |e_1^{(p)}\rangle\langle e_1^{(p)}|\bigr)^2 = |c_p|^4 \cdot |e_1^{(p)}\rangle\langle e_1^{(p)}| = |c_p|^2 \cdot P_p.$$

Die Projektionseigenschaft $P_p^2 = P_p$ ist daher nur für $|c_p|^2 \in \{0, 1\}$ erfüllt — in allen anderen Fällen ist $P_p$ kein Projektor. $\square$

**Dauerhafte Notationsbereinigung:**

Um Verwechslungen in späteren Blättern zu vermeiden, wird ab sofort unterschieden:

$$\pi_p := |e_1^{(p)}\rangle\langle e_1^{(p)}| \qquad \text{(orthogonale Rang-1-Projektion, } \pi_p^2 = \pi_p\text{)},$$

$$P_p := |c_p|^2 \cdot \pi_p \qquad \text{(gewichteter positiver Rang-1-Operator, } P_p^2 = |c_p|^2 P_p\text{)}.$$

Damit gilt:
- $\mathrm{Tr}(\pi_p) = 1$,
- $\mathrm{Tr}(P_p) = |c_p|^2$.

**Statusmarker:** ✅[M] (elementare Rechnung); ⚠[Notationsbereinigung] — Bezeichnung $\pi_p$ ab NEU-151 verbindlich

---

## 151.4 — Gesicherte obere Schranke für $|c_p|^2$

**Import aus NEU-134 und NEU-135.D:**

$$|c_p|^2 = O\!\left(\frac{(\log p)^2}{p}\right).$$

Äquivalent mit der Observable $R_p^{\mathrm{obs}} := \log(p)/|c_p|^2$ aus NEU-144:

$$R_p^{\mathrm{obs}} \gtrsim \frac{p}{\log p}.$$

Die obere Schranke für $|c_p|^2$ liefert also nur die **einseitige** untere Schranke für $R_p^{\mathrm{obs}}$.

**Statusmarker:** ✅[M, Import NEU-134 / NEU-135.D]

---

## 151.5 — Fehlende termweise untere Schranke; Übergabe an NEU-152

Die Importkette sichert nur die obere Schranke. Offen bleibt:

$$|c_p|^2 \gtrsim \frac{(\log p)^2}{p} \qquad \text{(termweise, für alle Primzahlen } p\text{)}.$$

Dies wäre äquivalent zu:

$$R_p^{\mathrm{obs}} \lesssim \frac{p}{\log p},$$

und zusammen mit 151.4 würde folgen:

$$R_p^{\mathrm{obs}} \asymp \frac{p}{\log p} \qquad \Longleftrightarrow \qquad |c_p|^2 \asymp \frac{(\log p)^2}{p}.$$

**Kandidaten für NEU-152 (noch nicht ausgeführt):**
- Euler-Produkt-/Determinantenidentität: liefert höchstens dyadische oder gemittelte Schranken, keine termweise Schranke ohne zusätzliches Separationslemma.
- Positivitätsargument über $\sum_p a_p(s)$: aus der positiven Gesamtsumme folgt im Allgemeinen keine gleichmäßige untere Schranke für jedes Glied.

**Statusmarker:** ❓[O] — Übergabe an NEU-152

---

## 151.6 — Rote Warnung: $R_p$-Notationskollision

> ⚠ **ROTE WARNUNG — vor Verwendung in nachfolgenden Blättern lesen**

In NEU-144 ist der Eigenwert der primdiagonalen Observable $R$ definiert als:

$$R_p := \frac{\log p}{|c_p|^2}.$$

In früheren Entwürfen zu NEU-151 erschien ein zweiter Faktor $R_p$ als „Spektralgewicht" in

$$\|\widetilde{\Psi}_p\|^2 = (\log p)^2 R_p,$$

was — falls es sich um dieselbe Größe handelt — zu dem formalen Widerspruch

$$R_p^2 = \frac{1}{\log p}$$

führen würde, der mit der Zielasymptotik $R_p \asymp p/\log p$ unvereinbar ist.

**Auflösung:** In NEU-44.X taucht $R_p$ nicht in der Rolle eines Spektralgewichts auf. Die Kollision stammt aus dem Entwurf, nicht aus dem Quellblatt. Ab NEU-151 gilt:

- $R_p^{\mathrm{obs}} := \log(p)/|c_p|^2$ — Eigenwert der primdiagonalen Observable $R$ (NEU-144).
- Jede andere spektralgewichtige Größe ist umzubenennen (Vorschlag: $w_p$, $\rho_p$ oder $\mathcal{R}_p$).

**Statusmarker:** ⚠[Rote Warnung] — keine offene mathematische Frage, sondern obligatorische Notationsbereinigung

---

## 151.7 — Skalare versus operatorwertige Finite-Part-Regularisierung

Drei logische Ebenen müssen unterschieden werden:

**Ebene 1** (finite Primlabelsumme, festes $X$, kompakt getragenes $\varphi$): Endliche Summe über Primzahlen, $S_{\varphi,X}(\beta)$ wohldefiniert.
**Statusmarker:** ✅[M] (direkt aus der Rang-1-Diagonalisierung)

**Ebene 2** (skalarer Finite-Part-Grenzwert): $\mathrm{FP}\lim_{X \to \infty} S_{\varphi,X}(\beta)$ als skalare Mellin-Aussage.
**Statusmarker:** ✅[M, NEU-148 / NEU-149]

**Ebene 3** (operatorwertiger Grenzwert $\in \mathcal{S}_1$): Es ist unklar, ob überhaupt ein Operator

$$\mathrm{FP}\lim_{X \to \infty} T_X \in \mathcal{S}_1$$

existiert. Selbst wenn er existiert, ist die Vertauschung

$$\mathrm{Tr}\!\left(\mathrm{FP}\lim_X T_X\right) = \mathrm{FP}\lim_X \mathrm{Tr}(T_X)$$

nicht automatisch gültig; sie erfordert eine Spurklassen-Restkontrolle im Operatorsinne.

**Präzisierung:** Bei einer Finite-Part-Regularisierung ist zunächst offen, ob überhaupt ein operatorwertiger regulierter Grenzwert definiert werden kann — oder ob nur der skalare regulierte Spurwert existiert. Dies ist eine Definitionsfrage, nicht nur eine unbewiesene Vertauschung.

**Statusmarker:** ❓[O] — offene Definitionsfrage, unabhängig von NEU-152

---

## 151.8 — Audit der Importkette NEU-44 → NEU-135.D → NEU-144

| Import-Schritt | Inhalt | Status |
|---|---|---|
| NEU-44 → NEU-44.X | Definition $C_p^{\mathrm{rel}}$, Rang-1-Beweis | ✅[V] |
| NEU-44.X → NEU-134 | Skalarer Koeffizient $c_p$, Extraktion der Kanalgewichte | ✅[M] |
| NEU-134 → NEU-135.D | Normkonvention, Welt-2-Entscheidung, obere Schranke $|c_p|^2 = O((\log p)^2/p)$ | ✅[M] |
| NEU-135.D → NEU-144 | $R_p^{\mathrm{obs}} = \log(p)/|c_p|^2$, Eigenwert der primdiagonalen Observable $R$ | ✅[M] |
| NEU-150 → NEU-151 | Primlabel-Seite der Mellin-Operator-Spur: abgeschlossen | ✅[M] |
| NEU-151 → NEU-152 | Termweise untere Schranke für $|c_p|^2$: offen | ❓[O] |

Die Importkette ist soweit geprüft konsistent. Kein Schritt in dieser Kette hängt an einer offenen Hypothese außerhalb von 151.5 und 151.7.

**Statusmarker:** ✅[Audit]

---

## Offene Punkte nach NEU-151

| Nummer | Inhalt | Status |
|---|---|---|
| O-151-1 | Termweise untere Schranke $|c_p|^2 \gtrsim (\log p)^2/p$ | ❓[O] → NEU-152 |
| O-151-2 | Operatorwertiger Finite-Part-Grenzwert $\in \mathcal{S}_1$, Vertauschbarkeit mit Spur | ❓[O] → eigenständiger Eintrag |
| O-151-3 | Rang-Erhaltung unter Gramform-Triage: „Rang $\leq$ const" ist plausibel, aber noch nicht streng bewiesen | ⚠[M plausibel, NEU-44.X'] |

---

## Verweise

- **NEU-44.X**: Rang-1-Definition und Normidentitäten für $C_p^{\mathrm{rel}}$
- **NEU-44.X'**: Rang-1-Stabilität unter Störungen und Lanczos-Approximationen
- **NEU-134**: Extraktion der skalaren Kanalgewichte $c_p$
- **NEU-135.D**: Normkonvention und obere Schranke
- **NEU-144**: Primdiagonale Observable $R$, Eigenwert $R_p^{\mathrm{obs}}$
- **NEU-148, NEU-149**: Skalare Mellin-Finite-Part-Spur (Ebene 2)
- **NEU-150**: Primlabel-Rückbindung (Ebene 2, geschlossen)
- **NEU-152** *(reserviert)*: Nichtentartung der Primkanalgewichte — termweise untere Schranke für $|c_p|^2$
