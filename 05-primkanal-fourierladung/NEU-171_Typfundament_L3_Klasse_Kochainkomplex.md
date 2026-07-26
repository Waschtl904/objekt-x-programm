# NEU-171 — Typfundament der $L_3$-Klasse und ihres Fouriergrades

**Status:** Audit offen. Keine Konstruktion, kein Nichtverschwindensnachweis.
**Vorgänger im DAG:** NEU-170c → NEU-170d → NEU-171.
**Gesperrt bis Abschluss dieses Blatts:** $[L_3]\in HH^4(B_3,\cdot)$, $dP^{\mathrm{ch}}=P^{\mathrm{ch}}d$, jede Route-A- und Route-B-Aussage.
**Nächster Knoten (bedingt):** Route A (Repräsentantenbrücke) oder Route B ($P^{\mathrm{ch}}$-Kettenprojektor) — erst nach Abschluss gemäß Fall A, B oder C.

---

## 171.0 — DAG-Position und Entscheidungsfrage

$$\text{NEU-170c} \longrightarrow \text{NEU-170d} \longrightarrow \boxed{\text{NEU-171}}.$$

Der DAG-Audit NEU-170d hat festgestellt:

$$[L_3] \;\not\!\longmapsto\; L_3^\circ = e_1V_1,$$

d.h. der kanonische Einmodenpfad gilt nur konditional. Die zentrale Lücke ist strukturell:

$$\boxed{\text{Welcher konkrete Kochainkomplex trägt die Klasse }[L_3]?}$$

Dieses Blatt legt ausschließlich fest, **welche** Objekte typmäßig vorliegen müssen — es konstruiert keinen Repräsentanten und beweist keine Nichtverschwindensaussage.

---

## 171.1 — Kandidatenquellen und ihr Status

Als Kandidatenquellen für das Typfundament gelten:

| Blatt | Gegenstand | Status für NEU-171 |
|---|---|---|
| NEU-72 | Adelischer Skalierungsquotient / BC-Zeitlängen | *Kandidat* — noch nicht Nachweis |
| NEU-170b | Ursprungsdefinition Repräsentantenstatus $L_3$ | *Kandidat* — noch nicht Nachweis |

**Wichtig:** Diese Blätter sind Ausgangsmaterial für die Auditierfragen unten. Dass eine der Quellen eine Algebra oder einen Komplex *erwähnt*, macht sie nicht zum Typnachweis.

---

## 171.2 — Atomare Auditierfragen

$$[O\text{-}171\text{-}1]: \quad \text{Definiert NEU-72 eine konkrete Algebra }B_3\text{ oder nur einen adelischen Quotienten?}$$

$$[O\text{-}171\text{-}2]: \quad \text{Ist ein Kochainraum }C^4(B_3,M)\text{ einschließlich Koeffizientenbimodul }M\text{ definiert?}$$

$$[O\text{-}171\text{-}3]: \quad \text{Ist das Differential }d\colon C^n\to C^{n+1}\text{ explizit festgelegt?}$$

$$[O\text{-}171\text{-}4]: \quad \text{Ist }L_3\text{ ein Kochain, Kozykel, Algebraelement oder Operator?}$$

$$[O\text{-}171\text{-}5]: \quad \text{Besitzt der Komplex eine Fouriergradierung, die }d\text{ erhält?}$$

Diese fünf Fragen sind unabhängig voneinander zu beantworten. Insbesondere darf $[O\text{-}171\text{-}2]$ nicht aus einer positiven Antwort auf $[O\text{-}171\text{-}1]$ erschlossen werden — die Existenz einer Algebra impliziert noch keinen definierten Kochainraum.

---

## 171.3 — Typvorbehalt: Koeffizientenbimodul

Bevor $[L_3]\in HH^4(B_3,\cdot)$ geschrieben werden darf, muss der Koeffizientenbimodul $M$ bestimmt sein. Zwei nicht äquivalente Optionen:

$$[O\text{-}171\text{-}2a]: \quad [L_3]\in HH^4(B_3,B_3)$$

$$[O\text{-}171\text{-}2b]: \quad [L_3]\in HH^4(B_3,M_\sigma)$$

wobei $M_\sigma$ ein durch einen Automorphismus $\sigma$ getwisteter Bimodul wäre. Diese Unterscheidung ist für alle späteren Aussagen über den Fouriergrad und den Kettenprojektor $P^{\mathrm{ch}}$ relevant.

$$\boxed{\text{Solange }M\text{ nicht feststeht, bleibt }[L_3]\in HH^4(B_3)\text{ eine unzulässige Kurznotation.}}$$

---

## 171.4 — Fouriergradierung: Bedingung und Konsequenz

Eine Fouriergradierung auf dem Komplex $(C^\bullet, d)$ liegt genau dann vor, wenn:

$$C^\bullet = \bigoplus_{q\in\Gamma} C^\bullet_q, \qquad d\bigl(C^\bullet_q\bigr) \subseteq C^{\bullet+1}_q$$

für eine abelsche Gruppe $\Gamma$ (den Fouriergraduierungsmonoid). Ob diese Bedingung erfüllt ist, entscheidet über die Zulässigkeit des Kettenprojektors:

$$P^{\mathrm{ch}} := \sum_{q\neq 0} P_q.$$

Nur wenn $d$ die Fouriergrade erhält, gilt $dP^{\mathrm{ch}} = P^{\mathrm{ch}}d$ als strukturelle Aussage — andernfalls ist die Route B in dieser Form negativ entschieden, ohne Route A auszuschließen.

---

## 171.5 — Schlusslogik: drei Ausgänge

Nach Beantwortung der Fragen $[O\text{-}171\text{-}1]$ bis $[O\text{-}171\text{-}5]$ mündet dieses Blatt in genau einen der drei Ausgänge:

**Fall A — Vollständig definiert:**

$(C^\bullet, d)$ ist explizit festgelegt, $M$ ist bestimmt, die Fouriergradierung ist $d$-verträglich.

$$\Rightarrow \text{Beide Routen A und B sind freigeschaltet.}$$

**Fall B — Komplex definiert, Fourierverträglichkeit offen:**

$(C^\bullet, d)$ und $M$ liegen vor, aber $d(C^\bullet_q)\subseteq C^{\bullet+1}_q$ ist ungeklärt.

$$\Rightarrow \text{Route A freigeschaltet; Route B (}P^{\mathrm{ch}}\text{-Kettenprojektor) gesperrt.}$$

**Fall C — Ausgangskomplex oder Typ von $L_3$ unbestimmt:**

Mindestens eine der Fragen $[O\text{-}171\text{-}1]$ bis $[O\text{-}171\text{-}4]$ bleibt ohne positive Antwort.

$$\Rightarrow \text{Beide Routen gesperrt. Nächster Schritt: Typrekonstruktion aus NEU-20/NEU-28.}$$

---

## 171.6 — Strukturelle Abgrenzung

Dieses Blatt legt die **minimale typkorrekte Ausgangsarchitektur** fest. Es gilt:

- Kein Repräsentant $L_3^\circ$ wird konstruiert.
- Keine Nichtverschwindensaussage ($[L_3]\neq 0$, $C_L\neq 0$, etc.) wird behauptet.
- Die negativen Befunde aus NEU-170a–170d werden **nicht als Unmöglichkeitssätze** interpretiert.

Die kausale Kette lautet:

$$\text{Kochainkomplex} \longrightarrow \text{Kohomologieklasse} \longrightarrow \text{zulässige Repräsentanten} \longrightarrow \text{Operatorrealisierung.}$$

Route A benötigt für die Abbildung

$$\operatorname{Rep}_{\mathrm{op}}([L_3]) \longrightarrow \operatorname{End}(\mathcal{H})$$

bereits einen festgelegten Ausgangskomplex. Ohne diesen blieben Kochains, Algebraelemente und Hilbertoperatoren vermischt.

---

## 171.7 — Offene Punkte

| Punkt | Inhalt | Voraussetzung |
|---|---|---|
| $[O\text{-}171\text{-}1]$ | Algebratyp von $B_3$ (konkret vs. adelisch) | Direktlektüre NEU-72 |
| $[O\text{-}171\text{-}2]$ | Kochainraum $C^4(B_3,M)$ mit Bimodul $M$ | $[O\text{-}171\text{-}1]$ positiv |
| $[O\text{-}171\text{-}2a/2b]$ | $M=B_3$ oder $M=M_\sigma$? | $[O\text{-}171\text{-}2]$ positiv |
| $[O\text{-}171\text{-}3]$ | Explizites Differential $d$ | $[O\text{-}171\text{-}2]$ positiv |
| $[O\text{-}171\text{-}4]$ | Typ von $L_3$: Kochain / Kozykel / Element / Operator | Unabhängig |
| $[O\text{-}171\text{-}5]$ | Fouriergradierung $d$-verträglich? | $[O\text{-}171\text{-}3]$ positiv |

---

## Referenzverknüpfungen im DAG

| Blatt | Rolle für NEU-171 |
|---|---|
| NEU-72 | Kandidatenquelle $B_3$ / adelischer Quotient |
| NEU-170b | Kandidatenquelle Ursprungsdefinition $L_3$ |
| NEU-170c | Direktaudit erste $L_3$-Definition (NEU-20/NEU-28) |
| NEU-170d | DAG-Audit: Diagnose $[L_3]\not\mapsto L_3^\circ=e_1V_1$ |
| Route A (gesperrt) | $\operatorname{Rep}_{\mathrm{op}}([L_3])\to\operatorname{End}(\mathcal{H})$ |
| Route B (gesperrt) | $P^{\mathrm{ch}}$-Kettenprojektor, $dP^{\mathrm{ch}}=P^{\mathrm{ch}}d$ |
