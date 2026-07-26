# NEU-213 — Revisionsaudit NEU-212: Bimodul-Regularisierung und Nichtinnerheitserhalt

**Status:** [O-213-1] ✓[M] (Fehleraudit), [O-213-2] ✓[M]_neg, [O-213-3] ?[O], [O-213-4] ?[O], [O-213-5] ?[O]  
**Erstellt:** 2026-07-20  
**Vorgänger:** NEU-212 ([O-212-1..5], teilweise fehlerhaft)  
**Korrigiert:** [O-212-1] → ✓[M]_part, [O-212-2] → ?[O], [O-212-3] → ?[O] (gesplittet in 3a/3b/3c), [O-212-4] → [O-212-4a] ✓[M]_neg  
**Ziel:** Vollständige Fehlerkorrektur von NEU-212; präzise Neuformulierung der offenen Bimodul- und Nichtinnerheitsfrage

---

## 213.0 — Anlass

NEU-212 enthielt zwei sachliche Fehler, die den behaupteten Fortschritt zurücknehmen. Dieser Knoten führt das Korrekturaudit durch, bevor irgendein Cup-Aufstieg versucht wird. Es wird **keine neue Derivation konstruiert** — der Knoten ist rein revisorisch.

---

## 213.A — Fehler 1: Scheinbare Divergenz des Offdiagonaltests

**Behauptung in NEU-212 (211.D-Analogon, [O-212-4]):** Die regularisierten Matrixelemente $c_j/\log(j+2)$ divergieren wie im ursprünglichen Offdiagonaltest.

**Nachrechnung.** Aus NEU-210/211 gilt exakt $c_j = \log(j+2)$. Also:
$$\frac{c_j}{\log(j+2)} = \frac{\log(j+2)}{\log(j+2)} = 1 \quad \text{für jedes } j. \tag{213.1}$$

**Satz ([O-213-1]).** *Die Folge $c_j/\log(j+2)$ ist konstant gleich $1$ und divergiert nicht.*

**Beweis.** Direktes Einsetzen von $c_j = \log(j+2)$ in (213.1). $\square$

$$\boxed{[O\text{-}213\text{-}1] \quad \checkmark[M]}$$

**Korrigierter Befund.**

**Satz ([O-213-2], = korrigiertes [O-212-4]).** *Der in NEU-212 vorgeschlagene Nichtinnerheitsbeweis für $\widetilde D_g$ via divergierender Matrixelemente $c_j/\log(j+2)$ ist unzulässig, da diese Folge konstant ist.*

$$\boxed{[O\text{-}212\text{-}4a] \quad \checkmark[M]_{\mathrm{neg}}} \tag{213.2}$$

**Tragweite.** Dies beweist **nicht**, dass $\widetilde D_g$ inner ist — es schließt lediglich den vorgeschlagenen Beweisweg aus. Die Frage nach Innerheit/Nichtinnerheit von $\widetilde D_g$ bleibt offen (siehe 213.D unten, [O-213-4]).

$$\boxed{[O\text{-}213\text{-}2] \quad \checkmark[M]_{\mathrm{neg}}}$$

---

## 213.B — Fehler 2: Leibniz-Regel unter Regularisierung

**Problem.** NEU-212.C definierte $\widetilde D_g(a) := R(D_g(a))$ mit $R(\xi) := \xi/\log(\nu+2)$ und behauptete, dies definiere eine Derivation. Das ist im Allgemeinen falsch.

**Nachrechnung.** Für eine Derivation $D_g$ gilt $D_g(ab) = D_g(a)b + aD_g(b)$. Wendet man einen linearen Operator $R$ auf die Werte an:
$$\widetilde D_g(ab) = R\bigl(D_g(a)b + aD_g(b)\bigr). \tag{213.3}$$
Damit $\widetilde D_g(ab) = \widetilde D_g(a)b + a\widetilde D_g(b)$ gilt, benötigt man
$$R(\xi b) = R(\xi)\,b, \qquad R(a\xi) = a\,R(\xi) \qquad \forall\, a,b \in A_{\mathrm{alg}}, \tag{213.4}$$
d.h. $R$ muss ein **$A_{\mathrm{alg}}$-Bimoduloperator** sein.

**Satz ([O-213-3]).** *Der Operator $R(\xi) = \xi/\log(\nu+2)$, angewendet auf $\xi \in B_{C^*}$, ist im Allgemeinen kein $A_{\mathrm{alg}}$-Bimoduloperator, da die Skalarfunktion $1/\log(\nu+2)$ nicht mit den $\mu_k$-Transporten kommutiert:*
$$\mu_k \cdot R(\xi) \neq R(\mu_k \cdot \xi) \quad \text{im Allgemeinen}, \tag{213.5}$$
*weil $\mu_k$ die Faktorialtiefe $\nu$ nichttrivial verschiebt ($\nu(kx) \neq \nu(x)$ i.A.), während $1/\log(\nu(x)+2)$ punktweise auf dem Argument $x$ ausgewertet wird, nicht auf dem transportierten Argument.*

**Beweis (Gegenbeispielskizze).** Sei $\xi = \delta_x$ (Punktmasse bei $x$, formal). Dann $R(\xi)$ trägt Gewicht $1/\log(\nu(x)+2)$. Nach Transport durch $\mu_k$ (Multiplikation mit Verschiebung $x \mapsto kx$) trägt $\mu_k\xi$ die Position $kx$, und $R(\mu_k\xi)$ trägt Gewicht $1/\log(\nu(kx)+2) \neq 1/\log(\nu(x)+2) = $ Gewicht von $\mu_k R(\xi)$, sofern $\nu(kx) \neq \nu(x)$ (was für die meisten $k,x$ zutrifft, da der abelsche Sektor unter den $\mu_k$-Transporten nicht zentral ist). $\square$

$$\boxed{[O\text{-}213\text{-}3] \quad \checkmark[M]_{\mathrm{neg}}} \quad \text{(für die spezifische Wahl } R = 1/\log(\nu+2)\text{)}$$

**Konsequenz.** Die in NEU-212.C behauptete Leibniz-Eigenschaft von $\widetilde D_g$ ist **nicht bewiesen** und mit der gewählten Regularisierung wahrscheinlich falsch. Die drei Teilfragen aus NEU-212 werden wie folgt neu geöffnet:

$$\boxed{[O\text{-}212\text{-}3a] \quad ?[O]: \quad \widetilde D_g \text{ erfüllt die Leibnizregel (offen, mutmaßlich falsch für } R=1/\log(\nu+2)\text{)}}$$
$$\boxed{[O\text{-}212\text{-}3b] \quad ?[O]: \quad \widetilde D_g \text{ respektiert sämtliche BC-Relationen}}$$
$$\boxed{[O\text{-}212\text{-}3c] \quad ?[O]: \quad \exists\, x \in \mathcal A^\infty \text{ oder } A_{C^*} \text{ mit } \widetilde D_g - D_g = \operatorname{ad}_x}$$

---

## 213.C — Weitere in NEU-212 unbelegte Punkte

### 213.C.1 — Nur neutraler Raum $B^\infty$, kein geladener Typ

Die Fréchet-$*$-Algebra $\mathcal B^\infty \subset C(\widehat{\mathbb Z})$ aus NEU-212.A ist per Konstruktion ein **neutraler** (ungeladener) Funktionsraum. Die behauptete geladene Algebra
$$\mathcal A^\infty = \bigoplus_h^{\mathrm{alg}} \mathcal A_h^\infty$$
wurde in NEU-212 nicht explizit als gradierte Summe mit Stabilität unter $\mu_k(\cdot), (\cdot)\mu_k, \mu_k^*(\cdot), (\cdot)\mu_k^*$ konstruiert und bewiesen. Damit ist nur $\mathcal B^\infty$, nicht $\mathcal A^\infty$ im vollen geladenen Sinn, gesichert.

$$\boxed{[O\text{-}212\text{-}1] \to \checkmark[M]_{\mathrm{part}}} \quad \text{(nur für } \mathcal B^\infty\text{, neutral)}$$

### 213.C.2 — Ursprungsdefinition und Stetigkeit von $\log(\nu(x)+2)$

An $x = 0 \in \widehat{\mathbb Z}$ ist $\nu(0) = +\infty$ (jede Faktorialzahl teilt $0$), sodass $\log(\nu(0)+2)$ formal divergiert. Eine Regularisierungsfunktion, die auf $\log(\nu(x)+2)$ aufbaut, muss:
1. einen expliziten Grenzwert bei $x \to 0$ festlegen,
2. Stetigkeit auf ganz $\widehat{\mathbb Z}$ (inklusive Umgebung von $0$) nachweisen,
3. Transportverträglichkeit mit $T_a, \rho_d$ prüfen.

Keiner dieser drei Punkte wurde in NEU-212 durchgeführt.

$$\boxed{[O\text{-}212\text{-}2] \to \; ?[O]}$$

---

## 213.D — Die eigentliche offene Kernfrage

Nach Korrektur der beiden Fehler bleibt die Konstruktionsaufgabe von NEU-211/212 ungelöst, aber jetzt präzise formuliert:

**[O-213-4] ?[O] — Bimodul-verträgliche, nichtinnerheits-erhaltende Regularisierung.**

$$\boxed{\text{Existiert ein } A_{\mathrm{alg}}\text{-Bimoduloperator } R : A_{C^*} \to \mathcal A^\infty \text{ (für ein geeignetes } \mathcal A^\infty\text{) mit}}$$
$$\boxed{R \circ D_g \text{ ist eine Derivation}, \quad R \circ D_g \notin \operatorname{Inn}(A_{\mathrm{alg}}, \mathcal A^\infty)_g\;?}$$

Notwendige Bedingungen an $R$:
1. **Bimodulinvarianz:** $R(a\xi b) = aR(\xi)b$ für alle $a,b \in A_{\mathrm{alg}}$, $\xi \in A_{C^*}$ (nicht nur Skalarmultiplikation mit einer $\nu$-abhängigen Funktion, da diese nicht mit $\mu_k$-Transport kommutiert, siehe 213.B).
2. **Zielraumkontrolle:** $R(A_{C^*}) \subseteq \mathcal A^\infty$ für ein wohldefiniertes, unter Produkt/Adjunktion/Transport stabiles $\mathcal A^\infty$.
3. **Nichtinnerheitserhalt:** $R$ darf die divergente Information aus dem Offdiagonaltest (NEU-211.D) nicht durch die Regularisierung selbst neutralisieren — dies muss explizit durch einen neuen (korrekten) Matrixelementtest oder ein anderes Nichtinnerheitskriterium nachgewiesen werden, nicht durch bloße Beschränktheit der Differenz $R\circ D_g - D_g$.

**Kandidatenrichtungen (unbewiesen, nur Vorschläge für NEU-214):**
- Ein Bimodul-Mittelungsoperator, der über die $\mu_k$-Bahn statt punktweise über $\nu(x)$ regularisiert (d.h. $R$ wirkt auf ganze Bahnorbits $\{k \cdot x : k \ge 1\}$ gleichmäßig, nicht auf einzelne Punkte).
- Ein Diracoperator-Kalkül (Spektraltriple-Ansatz aus NEU-211.F), bei dem $\mathcal A^\infty$ als glatte Domäne definiert wird und $R$ aus einer Resolventenglättung entsteht, die per Konstruktion mit der Modulstruktur kommutiert.
- Untersuchung, ob überhaupt ein Bimoduloperator mit den gewünschten Eigenschaften existieren **kann** (evtl. weiteres No-go-Resultat).

$$\boxed{[O\text{-}213\text{-}4] \quad ?[O]}$$

**[O-213-5] ?[O] — Cup-Pfeil bleibt vollständig blockiert**, solange [O-213-4] offen ist. Kein Fortschritt zu $HH^4_g$ ist vor Klärung von [O-213-4] sinnvoll versuchbar.

$$\boxed{[O\text{-}213\text{-}5] \quad ?[O]}$$

---

## 213.E — Korrigierte Strukturbilanz (ersetzt NEU-212.E)

| Knoten | Alter Status (NEU-212) | Korrigierter Status | Grund |
|---|---|---|---|
| [O-212-1] | ✓[M] | ✓[M]_part | Nur neutraler Raum $\mathcal B^\infty$ gesichert; geladene gradierte Algebra $\mathcal A^\infty$ nicht bewiesen |
| [O-212-2] | ✓[M] | ?[O] | Ursprungsdefinition, Stetigkeit, Transportverträglichkeit von $\log(\nu+2)$ ungeprüft |
| [O-212-3] | ✓[K/M] | ?[O] (→ 3a/3b/3c) | Leibniz-Regel unter Regularisierung nicht bewiesen; Kohomologieaussage unbelegt |
| [O-212-4] | (Ankündigung offen) | [O-212-4a] ✓[M]_neg | $c_j/\log(j+2)=1$; vorgeschlagener Divergenzbeweis unzulässig |
| [O-212-5] | ?[O] | ?[O] | Weiterhin durch [O-213-4] blockiert |
| [O-213-1] | — | ✓[M] | Rechenfehler identifiziert und korrigiert |
| [O-213-2] | — | ✓[M]_neg | Divergenztest widerlegt (nicht: Innerheit bewiesen) |
| [O-213-3] | — | ✓[M]_neg | $R=1/\log(\nu+2)$ ist kein $A_{\mathrm{alg}}$-Bimoduloperator |
| [O-213-4] | — | ?[O] | **Zentrale offene Frage:** bimodul-verträgliche, nichtinnerheits-erhaltende Regularisierung |
| [O-213-5] | — | ?[O] | Cup-Pfeil, blockiert durch O-213-4 |

---

## 213.F — DAG-Stand

```
[O-211-6] ?[O]
      |
      +---> [O-212-1] ✓[M]_part   Nur B^∞ (neutral) gesichert, nicht A^∞ (geladen)
      |
      +---> [O-212-2] ?[O]        Ursprung/Stetigkeit/Transport von log(ν+2) ungeprüft
      |
      +---> [O-212-3] ?[O]
      |         +---> [O-212-3a] ?[O]   Leibnizregel für D~_g (mutmaßlich falsch für R=1/log(ν+2))
      |         +---> [O-212-3b] ?[O]   BC-Relationen respektiert?
      |         +---> [O-212-3c] ?[O]   Konkretes x mit D~_g - D_g = ad_x?
      |
      +---> [O-212-4a] ✓[M]_neg   c_j/log(j+2) = 1 (konstant, keine Divergenz)
      |
      +---> [O-213-1] ✓[M]       Rechenfehler-Nachweis
      +---> [O-213-2] ✓[M]_neg   Divergenztest widerlegt (Innerheit weiterhin unbekannt)
      +---> [O-213-3] ✓[M]_neg   1/log(ν+2) kein A_alg-Bimoduloperator
      +---> [O-213-4] ?[O]        HAUPTFRAGE: bimodul-verträglicher, nichtinnerheits-erhaltender R?
      +---> [O-213-5] ?[O]        Cup HH^1_g ⊗ HH^3 → HH^4_g, blockiert durch O-213-4
```

**Zentrales Ergebnis dieses Revisionsknotens:**

$$\boxed{\text{NEU-212 enthielt einen Rechenfehler (213.1) und einen Leibniz-Typfehler (213.4/213.5); beide korrigiert.}}$$
$$\boxed{\text{Der Existenznachweis } [D_g]\in HH^1(A_{\mathrm{alg}},A_{C^*})_g \text{ aus NEU-211 bleibt unberührt.}}$$
$$\boxed{\text{Offen: } \exists\, A_{\mathrm{alg}}\text{-Bimoduloperator } R \text{ mit } R\circ D_g \text{ Derivation nach } \mathcal A^\infty, \text{ nicht inner?}}$$

NEU-214 sollte diese Bimodul-Regularisierungsfrage [O-213-4] direkt angehen — entweder durch Konstruktion eines Kandidaten (z.B. Bahn-Mittelung statt Punktregularisierung) oder durch ein weiteres No-go-Resultat.
