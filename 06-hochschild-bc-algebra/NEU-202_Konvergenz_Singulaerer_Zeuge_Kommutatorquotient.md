# NEU-202 — REVISION: Drei-Fehler-Audit zum Kandidaten $H_{\mathrm{sing}}$

**Status:** ✓[M]_neg (Gesamtkandidat widerlegt)  
**Erstellt:** 2026-07-19 (ursprünglich positiver Beweis-Versuch)  
**Revidiert:** 2026-07-19 (vollständige Fehlerkorrektur nach Audit)  
**Commit e77deb3 gilt als fehlerhaft.**  
**Vorgänger:** NEU-201 ([O-199-3]_sing ?[O])  

---

## Zusammenfassung des Audits

Der ursprüngliche Satz 202.1 (Behauptung: $H_{\mathrm{sing}} \in B$ norm-konvergent,
$[H_{\mathrm{sing}},\mu_2] \notin [B,B]$ via KMS-Test) ist in allen drei
tragenden Schritten widerlegt. Der Kandidat $H_{\mathrm{sing}}$ existiert
nicht als Element von $B$.

---

## [O-202-conv] ✓[M]_neg — Norm-Konvergenz ausgeschlossen

### Fehler im ursprünglichen Schritt 1

Die Behauptung war: $\sum_p \frac{1}{(\log p)^2} < \infty$ ("konvergente
Primreihe via Mertens"), woraus Norm-Konvergenz folge.

### Korrekte Widerlegung

**Augmentations-Schranke:** Der Augmentationscharakter
$\varepsilon: B \to \mathbb{C}$, $\varepsilon(\mu_n) = \varepsilon(e(r)) = 1$,
ist ein stetiges Algebrahomomorphismus mit $\|\varepsilon\| = 1$. Für
Partialsummen $H_F = \sum_{p \in F} \frac{1}{\log p}\,\mu_p e(1/p)$ gilt:
$$\|H_{F'} - H_F\| \geq |\varepsilon(H_{F'} - H_F)| = \sum_{p \in F' \setminus F} \frac{1}{\log p}.$$
Da $\sum_p \frac{1}{\log p} = +\infty$ (Mertens' zweiter Satz), sind
die Partialsummen **nicht norm-Cauchy**. ✓[M]_neg

**Zusatz — Die $\ell^2$-Behauptung ist ebenfalls falsch:**
$$\sum_p \frac{1}{(\log p)^2} \geq \frac{\pi(x)}{(\log x)^2} \sim \frac{x}{(\log x)^3} \longrightarrow \infty.$$
Mertens' Satz betrifft $\sum_{p \leq x} 1/p \sim \log\log x$, nicht
die hier verwendete Reihe.

**Zusatz — Nicht-Orthogonalität der Summanden:** Für $p \neq q$ prim gilt
$$\bigl(\mu_p e(1/p)\bigr)^* \mu_q e(1/q) = e(-1/p)\,\mu_p^* \mu_q e(1/q) \neq 0,$$
da $\mu_p^* \mu_q = \mu_q \mu_p^* \neq 0$ für $\gcd(p,q)=1$. Die
Summanden sind nicht orthogonal; das Orthogonalitätsargument in
Schritt 1 war unzulässig.

**Typfehler:** $\mu_p e(1/p)$ liegt im homogenen Grad $p$ der vollen
BC-Algebra $B = C^*(\mathbb{Q}/\mathbb{Z}) \rtimes \mathbb{N}$;
die Behauptung $H_{\mathrm{sing}} \in B$ war falsch typisiert.

---

## [O-202-comm] ✓[M]_part — Kommutatorformel nur für endliche $F$ gültig

### Korrekte Formel (endliche Partialsummen)

Für eine endliche Primzahlmenge $F$ ist korrekt:
$$[H_F,\, \mu_2] = \sum_{p \in F} \frac{1}{\log p}\, \mu_{2p}\bigl(e(2/p) - e(1/p)\bigr).$$

**Korrektur des $p=2$-Terms:** Im ursprünglichen Schritt 2 wurde
$e(1/2) = -1$ als skalare Algebrenidentität verwendet. Dies ist falsch:
$e(1/2)$ ist ein nichttriviales Gruppenelement von $\mathbb{Q}/\mathbb{Z}$
mit $e(1/2)^2 = 1$, aber $e(1/2) \neq -1$ als Algebrenelement. Der
korrekte $p=2$-Term lautet:
$$\frac{1}{\log 2}\,\mu_4\bigl(1 - e(1/2)\bigr) \quad (\neq \tfrac{2}{\log 2}\,\mu_4).$$

Da $H_{\mathrm{sing}}$ als Element von $B$ nicht existiert, ist auch
der behauptete unendliche Kommutator $[H_{\mathrm{sing}}, \mu_2]$ nicht
definiert. Die endliche Formel ist korrekt (✓[M]_part), der
unendliche Limes ist nicht wohlgeformt.

---

## [O-202-KMS] ✓[M]_neg — KMS-Test unzulässig und ergibt tatsächlich null

### Fehler im ursprünglichen Schritt 3

Es wurde behauptet: $\phi_\beta([a,b]) = 0$ für alle $a,b \in B$ und alle
KMS$_\beta$-Zustände $\phi_\beta$. Dies ist falsch: KMS-Zustände sind
**im Allgemeinen keine Spuren**.

### Korrekte Widerlegung: KMS-Wert verschwindet aus Symmetriegründen

Jeder Kommutatorterm $\mu_{2p}(e(2/p) - e(1/p))$ ist homogen bzgl.
der BC-Zeitentwicklung $\sigma_t$:
$$\sigma_t\!\bigl(\mu_{2p}(e(2/p)-e(1/p))\bigr) = (2p)^{it}\,\mu_{2p}(e(2/p)-e(1/p)).$$
KMS-Zustände sind zeitinvariant: $\phi_\beta \circ \sigma_t = \phi_\beta$. Damit:
$$\phi_\beta(a) = \phi_\beta(\sigma_t(a)) = (2p)^{it}\,\phi_\beta(a) \quad \forall\, t$$
$\Rightarrow \phi_\beta(a) = 0$ für jedes homogene $a$ mit nichttrivialem
Gewicht (hier Gewicht $2p \neq 1$).

Also:
$$\phi_\beta([H_F,\, \mu_2]) = 0$$
für jede endliche Partialsumme $H_F$. Der ursprüngliche KMS-Wert
$\frac{2}{\log 2}\cdot\frac{4^{1-\beta}}{\zeta(\beta)}$
entstand durch irrtümliche Auswertung von $\phi_\beta(\mu_4)$
anstelle von $\phi_\beta(\mu_4 \mu_4^*)$ (Grad-0-Projektion vs.
Grad-$4$-Isometrie). ✓[M]_neg

---

## DAG-Rückbau

```
[O-199-3]_sing (?[O])  — unverändert offen
      |
      +---> 201.A: Kandidat H_sing ✓[M]_neg
      |         Begründung: H_sing ∉ B (Augmentationsdivergenz,
      |         Typ-Fehler, keine Norm-Konvergenz)
      |
      +---> [O-202-conv] ✓[M]_neg  (Norm-Konvergenz ausgeschlossen)
      +---> [O-202-comm] ✓[M]_part (end. Kommutatorformel korrekt)
      +---> [O-202-KMS]  ✓[M]_neg  (KMS-Detektor verschwindet)
      |
      +---> [O-202-1], [O-202-2]: UNGÜLTIG
      |         (Folgeknoten entfallen, da H_sing nicht existiert)
      |
      +---> 201.B, 201.C: weiterhin ?[O]
                (benötigen neuen, wohldefinierten Kandidaten)
```

---

## Anforderungen an den nächsten Kandidaten

Ein zulässiger Nachfolger-Kandidat $x = \sum_p c_p\,x_p \in B$
muss gleichzeitig erfüllen:

1. **Augmentationsbedingung:** $\varepsilon(x_p) = 0$ für alle $p$
   (verhindert Augmentationsdivergenz).
2. **Norm-Cauchy-Nachweis:** $\sum_p \|c_p\, x_p\| < \infty$
   in der $C^*$-Norm von $B$.
3. **Quotienten-Detektor:** Nichtverschwindungstest über ein **traces** oder
   **quotiententreues** Funktional (kein allgemeiner KMS-Zustand);
   z.B. ein spurartiges Funktional auf $B/[B,B]$ oder
   ein $\text{Ext}^1$-Paarungstest.

**Kandidatenskizze für NEU-203:** Setze
$$y_p := \mu_p \mu_p^* - \frac{1}{p}\, \mathbf{1} \in B$$
(Rang-1-Projektion minus Skalarmultiple). Dann $\varepsilon(y_p) = 1 - \frac{1}{p}\to 1$
— immer noch nicht augmentationsneutral. Verbesserung:
$$z_p := \mu_p \mu_p^* - \mu_{p+1} \mu_{p+1}^* \in B,\quad \varepsilon(z_p) = 0$$
(Differenz zweier Projektionen gleichen Rangs, falls geeignet normiert).
Norm-Abschätzung und Kommutator-Test für $z_p$ sind Gegenstand von NEU-203.

---

## Statusübersicht (nach Revision)

| Teilfrage | Aussage | Status |
|-----------|---------|--------|
| [O-202-conv] | $H_{\mathrm{sing}}$ norm-konvergent? | ✓[M]_neg |
| [O-202-comm] | Kommutatorformel (endlich) korrekt? | ✓[M]_part |
| [O-202-KMS] | KMS-Nichtverschwindensdetektor? | ✓[M]_neg |
| 201.A (NEU-201) | Existenz singulärer Zeuge via $H_{\mathrm{sing}}$? | ✓[M]_neg |
| [O-199-3]_sing | Irgendeин singuläres $H$ sichtbar? | ?[O] |
