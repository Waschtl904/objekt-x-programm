# NEU-220 — Gammafaktor: Quelltyp und Zielraum

**Datei:** `katalog/NEU-220_Gammafaktor_Quelltyp_und_Zielraum.md`  
**Datum:** 2026-07-25  
**Repository:** Waschtl904/rh-fragenkatalog  
**Typ:** Eröffnungsknoten — konstruktiv, kein Reparaturpfad  
**Vorgänger:** NEU-219_Finalaudit_Gesamtabschluss.md (Commit 102c6ef)  
**Exportierter Ursprungsknoten:** `[O-219-6]` Weil-/Gammafaktorpfad  

---

## Atomarer Knoten

$$\boxed{[O\text{-}220\text{-}1\text{-Gamma-source-target-type}] \quad ?[O]}$$

**Status:** offen  
**Charakter:** Erstmalige typkorrekte Konstruktion des archimedischen Bausteins. Noch keine Kopplung an $D_g$, keinen vollständigen Weil-Kozykel, keine Positivitätsbehauptung.

---

## Ziel

Gesucht ist eine typkorrekte Kette

$$\mathcal{S}_\infty \xrightarrow{\;\mathcal{M}\;} \widehat{\mathcal{S}}_\infty \xrightarrow{\;\Lambda_\Gamma\;} \mathbb{C},$$

wobei:

- $\mathcal{S}_\infty$ ein expliziter archimedischer Testfunktionsraum auf $\mathbb{R}_+^\times$ ist;
- $\mathcal{M}$ die Mellintransformation mit vollständig fixierter Normierung ist;
- $\Lambda_\Gamma$ eine stetige Distribution oder quadratische Form ist;
- ihre Auswertung exakt den archimedischen $\Gamma'/\Gamma$-Beitrag der gewünschten Weil-Explizitformel erzeugt.

**Zentrale Typfrage:**

$$\boxed{\Lambda_\Gamma \in \mathcal{S}_\infty' \qquad\text{oder}\qquad \Lambda_\Gamma \text{ entsteht als Spur-/Formauswertung eines Skalierungsgenerators?}}$$

Diese beiden Möglichkeiten werden anfangs **parallel** geprüft, aber **nicht vermischt**.

---

## Pflichtentscheidungen

### PD-1 — Testfunktionsraum $\mathcal{S}_\infty$

Zu entscheiden ist, ob
$$\mathcal{S}_\infty = \mathcal{S}(\mathbb{R}_+^\times)$$
mit multiplikativem Haarmaß $dx/x$ genügt oder ob zusätzliche Symmetrie-, Realitäts- oder Randbedingungen nötig sind.

Insbesondere muss die Involution fixiert werden, etwa
$$f^\sharp(x) = \overline{f(x^{-1})},$$
und es muss klar sein, welcher Unterraum später zur Weil-Symmetrie $s \mapsto 1-s$ passt.

**Status:** $?[O]$

### PD-2 — Mellin-Normierung

Vor jeder Rechnung muss die Konvention fixiert sein. Zwei Kandidaten:

$$\text{(a)}\quad (\mathcal{M}f)(s) = \int_0^\infty f(x)\,x^s\,\frac{dx}{x}$$

$$\text{(b)}\quad (\mathcal{M}f)(s) = \int_0^\infty f(x)\,x^{s+1/2}\,\frac{dx}{x} \qquad\text{(um }1/2\text{ zentriert)}$$

Unterschiedliche Zentrierungen verschieben den Skalierungsgenerator und den Gamma-Term. Sie sind **nicht** kosmetisch austauschbar.

**Status:** $?[O]$

### PD-3 — Exakter Gammafunktionaltyp

Gesucht ist eine konkrete Formel
$$\Lambda_\Gamma(f) = \langle T_\Gamma, \mathcal{M}f \rangle, \qquad T_\Gamma \in \widehat{\mathcal{S}}_\infty'.$$

Zu prüfen sind:

| Eigenschaft | Anforderung |
|---|---|
| Stetigkeit | $\Lambda_\Gamma: \mathcal{S}_\infty \to \mathbb{C}$ stetig |
| Konvergenz | Das Integral bzw. die Distributionspaarung konvergiert |
| Symmetrie | $T_\Gamma$ ist invariant unter $s \mapsto 1-s$ bzw. $t \mapsto -t$ |
| Realität | $\Lambda_\Gamma(f^\sharp) = \overline{\Lambda_\Gamma(f)}$ auf geeignetem reellen Unterraum |
| Gamma-Abhängigkeit | Explizite Abhängigkeit von der gewählten Gamma-Normierung dokumentiert |

Naturkandidat:
$$T_\Gamma(s) = \frac{\Gamma'}{\Gamma}\!\left(\frac{s}{2}\right) + \frac{\Gamma'}{\Gamma}\!\left(\frac{1-s}{2}\right) \qquad\text{(symmetrisierter Weil-Gamma-Term)}$$

oder in der additiveren Form über den Digamma-Operator.

**Status:** $?[O]$

### PD-4 — Operatorischer Ursprung (Skalierungsgenerator)

Parallel zu PD-3 ist zu prüfen, ob der Skalierungsgenerator
$$H_\infty \sim -i\, x\frac{d}{dx} \quad\text{auf}\quad L^2(\mathbb{R}_+^\times, dx/x)$$
den Gamma-Term durch eine regulierte Spur, relative Spur oder quadratische Form erzeugen kann.

Eine formale Gleichung $\operatorname{Tr}(f(H_\infty)) = \Lambda_\Gamma(f)$ reicht **nicht**. Anzugeben sind:

- Definitionsbereich und Selbstadjungiertheit von $H_\infty$;
- Spektrum (unitäre Gruppe $\mathbb{R}$, Spektralmaß $d\mu$);
- nötige Regularisierung (Zeta-Regularisierung, Heat-Kernel, relative Spur);
- Vergleich mit dem Distributionsansatz aus PD-3.

**Status:** $?[O]$

### PD-5 — Schnittstelle zur endlichen adelischen Seite

Am Ende dieses Knotens muss lediglich der **zukünftige Anschlusstyp** feststehen, z.B.
$$\Lambda_{\mathrm{fin}} \oplus \Lambda_\Gamma \qquad\text{oder}\qquad \mathcal{S}_{\mathbb{A}} \simeq \mathcal{S}_{\mathrm{fin}}\,\widehat\otimes\,\mathcal{S}_\infty.$$

Noch **nicht** zu beweisen: dass diese Summe bereits die vollständige Weil-Form oder Objekt $X$ liefert.

Zu fixieren sind:
- welcher Typ von $\mathcal{S}_{\mathrm{fin}}$ aus der BC-/adelischen Architektur heraustritt;
- welche Topologie auf dem Tensorprodukt verwendet wird (projektiv, injektiv, $\pi$-Produkt);
- ob die Kopplung über ein gemeinsames Skalarprodukt oder eine Paarung läuft.

**Status:** $?[O]$

---

## Strukturdiagnose: zwei parallele Wege

| Weg | Beschreibung | Entscheidungsknoten |
|---|---|---|
| **Weg A** — Distributions-$\Lambda_\Gamma$ | $T_\Gamma \in \widehat{\mathcal{S}}_\infty'$ direkt als Gammafunktional | PD-3 |
| **Weg B** — Operator-Spur | $H_\infty$ auf $L^2(\mathbb{R}_+^\times)$, regulierte Spur | PD-4 |

Weg A und Weg B dürfen anfangs parallel bearbeitet werden. Sobald einer der Wege ein $\checkmark[M]$-Resultat produziert, wird der andere auf Kompatibilität geprüft. Falls beide ein $\checkmark[M]_{\mathrm{neg}}$ liefern, wird ein neuer Reparaturknoten $[O\text{-}220\text{-}1\text{-}\mathrm{repair}]$ eröffnet.

---

## Erfolgskriterien

**$\checkmark[K/M]$** sobald alle fünf vorhanden sind:

1. Vollständig definierter archimedischer Testfunktionsraum $\mathcal{S}_\infty$ mit Involution
2. Fixierte Mellin- und Involutionskonvention
3. Stetige, exakt auswertbare Gamma-Distribution $\Lambda_\Gamma$ mit Symmetrie- und Realitätsbeweis
4. Nachweis, dass $\Lambda_\Gamma$ den richtigen archimedischen $\Gamma'/\Gamma$-Term erzeugt
5. Typisierter Anschlussport zur endlichen BC-/adelischen Architektur

**$\checkmark[M]_{\mathrm{part}}$** wenn nur die Distribution gelingt, aber ihr operatorischer oder adelischer Anschluss offen bleibt.

---

## Motivation: Warum dieser Knoten Objekt $X$ direkt voranbringt

NEU-219 hat bewiesen, was nicht genügt:
$$\text{endlicher adelischer Basislift} + \text{skalares Orbitgewicht.}$$

NEU-220-1 soll erstmals konstruieren, was strukturell fehlt:

$$\boxed{\text{einen eigenständigen archimedischen Baustein mit korrektem Quell- und Zieltyp.}}$$

Damit wäre Objekt $X$ nicht nur durch Negativbedingungen eingegrenzt — wir hätten erstmals einen **Kandidaten für eine neue Komponente** des fünfteiligen Gesamtobjekts.

---

## Strategischer Fortgang

$$\boxed{\text{Gamma-Quelltyp} \longrightarrow \text{Gamma-Distribution} \longrightarrow \text{endliche/archimedische Kopplung} \longrightarrow \text{Weil-Form} \longrightarrow \text{Positivitätsraum.}}$$

---

## Nachfolgeknoten (gesperrt bis PD-1 bis PD-5 entschieden)

| Knoten | Inhalt | Freigabebedingung |
|---|---|---|
| `[O-220-2-Gamma-distribution-proof]` | Vollständiger Beweis der Gamma-Distribution | PD-2 und PD-3 abgeschlossen |
| `[O-220-3-operator-trace-regularization]` | Skalierungsgenerator und regulierte Spur | PD-4 abgeschlossen |
| `[O-220-4-finite-archimedean-coupling]` | Kopplung $\mathcal{S}_{\mathrm{fin}} \widehat\otimes \mathcal{S}_\infty$ | PD-5 abgeschlossen |
| `[O-220-2-noncanonical-rotation-repairs]` | Nichtkanonische Rotationsreparaturen (aus NEU-219) | Unabhängig; vorerst geparkt |

---

## Abhängigkeiten

| Datei | Rolle |
|---|---|
| `NEU-219_Finalaudit_Gesamtabschluss.md` | Vorgänger; exportiert `[O-219-6]` |
| `NEU-219y_Unit-Slot-Zeuge_...md` | Beweist, dass skalarer Lift nicht genügt |
| `NEU-211_...` (Dg-Formeln) | Verbleibt als Ankerpunkt für spätere Kopplung |
| `METHODIK_O219_Strukturdiagnose.md` | Methodenbasis für Entscheidungsstruktur |
