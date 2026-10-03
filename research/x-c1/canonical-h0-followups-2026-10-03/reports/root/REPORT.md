# Objekt X — Endpunkt-Nachrechnung und gemeinsamer H₀-Root-Test

3. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

## Ergebnis

**five_eighths ist mit einem physischen Gesamtwinkel ≤ 4,933780° nachgerechnet. Der anschließende gemeinsame H₀-/F-Test schließt Root nicht.**

Der Test kombiniert erstmals in dieser lokalen Folge die beiden notwendigen quadratischen H₀-Bedingungen direkt mit den Linienpolynomen. Er verwendet weiterhin ausschließlich die gebundenen Daten von PR #206. Es wurden keine Operatorintegrale, Y58-Dualdaten, neuen L_B-Daten, A13-Rechnungen oder adaptiven Eingabebäume erzeugt. GitHub wurde nicht verändert.

## Was aus dem übermittelten Bericht bestätigt wurde

Die SHA-256-Werte des vorherigen Rücktest-ZIP, seines Manifests und von PULLBACK_AUDIT.json stimmen mit den vorhandenen Dateien überein. Die neuen GPT-1-Prüfer, H0_CUTS.json und das dort erwähnte Folge-ZIP wurden nicht mitgeliefert. Ihre Bytegleichheit wird deshalb nicht behauptet. Die hier vorliegenden Programme rekonstruieren die beschriebenen Rechnungen aus dem zuvor versiegelten Quellpaket; ihre eigenen Dateihashes sind entsprechend andere.

Der vollständige Relaxationszeuge bleibt für sämtliche freien A-seitigen Vervollständigungen ausgeschlossen: (H₀)₅₅ < −11/10⁶ und (H₀)₆₆ < −43/4000. Die vier Y-Randwerte allein sind nicht ausgeschlossen. Die positive Diskriminante seines ungekürzten Stifts macht den vollständigen Punkt nicht zulässig.

## Endpunktverbesserung und physischer Winkel

Für F(s)=αs²+βs+γ ist F′(s)=2αs+β bei festem Eingabedatum affin. Deshalb schließt die Hülle der beiden gemeinsam ausgewerteten Ableitungsendpunkte die Ableitung auf dem ganzen Fenster ein. Sie wird mit den bereits vorhandenen gültigen Ableitungsschranken geschnitten. Alle ursprünglichen Modellreste bleiben bezahlt.

Auf dem bedingten Vier-Y-Schnitt five_eighths isoliert das Fenster [0,9/256] den maximalen Ast. Der anschließende Transport mit den ursprünglichen N- und G_B-Modellen ergibt einen Gesamtwinkel von höchstens 4,933780° nach oben gerundet. Gesamtwinkel bedeutet zweimal die obere Abweichung zur unveränderten physischen Referenz.

| Fall | Maximaler Ast | Gesamtwinkel, nach oben gerundet |
|---|---|---:|
| point/central | isoliert | 1.903077° |
| point/five_eighths | isoliert | 2.316014° |
| point/half | isoliert | 2.180335° |
| point/quarter | isoliert | 1.967736° |
| point/two_thirds | isoliert | 2.360824° |
| root | UNRESOLVED | offen |
| slice/central | isoliert | 2.933357° |
| slice/five_eighths | isoliert | 4.933780° |
| slice/half | isoliert | 3.642652° |
| slice/quarter | isoliert | 3.070163° |
| slice/two_thirds | UNRESOLVED | offen |
| Acht Diagnoseboxen | UNRESOLVED | offen |

Es sind neun maximale Linien auf 19 Fällen. Die acht Diagnoseboxen bilden keine Root-Überdeckung. Die H₀-Polynome wurden für diese Winkelrechnung noch nicht benutzt.

## Die beiden notwendigen H₀-Bedingungen

Mit B=G_B+L_B/17, yᵢ=Yᵀeᵢ und aᵢ⁺=upper((G_A)ᵢᵢ) lautet jede Bedingung

Ψᵢ = aᵢ⁺ − 2wᵢᵀyᵢ + wᵢᵀG_Bwᵢ + (2/17)wᵢᵀL_Bwᵢ + ‖L_Bwᵢ‖²/(289η) ≥ 0.

Hier ist η=2499/2500. Rationale Gershgorin-Zeilensummen beweisen auf ganz Root G_B ⪰ ηI; die tatsächliche Untergrenze liegt bei ungefähr 0,99962764844949.

Die Herleitung folgt aus quadratischer Ergänzung und G_B⁻¹ ⪯ η⁻¹I. Für cᵢ=B⁻¹yᵢ gilt cᵢᵀG_Bcᵢ ≥ 2wᵢᵀyᵢ − wᵢᵀBG_B⁻¹Bwᵢ; zudem ist BG_B⁻¹B = G_B + 2L_B/17 + L_BG_B⁻¹L_B/289. Zusammen mit cᵢᵀG_Bcᵢ≤aᵢ⁺ ergibt das Ψᵢ≥0.

Die festen Vektoren für i=5,6 werden aus B_*⁻¹G_B,*cᵢ,* am bekannten Zeugen gewonnen und auf 10⁻¹⁶ gerundet, zur nächsten Zahl mit halben Fällen nach oben. Die Ungleichung gilt für jeden festen rationalen Vektor; die Unzulässigkeit des Auswahlpunkts beeinträchtigt sie nicht. Jedes Polynom enthält 80 lineare und 260 quadratische Nichtnullterme in 80 ursprünglichen Symbolen.

Beide Polynome schließen den vollständigen Zeugen aus. Alle fünf bekannten vollständigen Punktfälle bleiben mit zehn nichtnegativen unteren Cut-Grenzen erhalten. Keine der 19 ganzen Fallboxen wird durch die einfache Cut-Auswertung ausgeschlossen. Für diese Domänenkontrolle werden Mittelpunkte und Radien exakt neu parametrisiert. Der anschließende Multiplikatortest verwendet ausschließlich Root, also ohne Koordinatenwechsel.

## Der ausgeführte gemeinsame Root-Test

Für jede Zielfunktion f=P+R mit |R|≤e und feste λ₅,λ₆≥0 wird die Untergrenze von P−λ₅Ψ₅−λ₆Ψ₆−e berechnet. Auf zulässigen Eingaben ist sie eine gültige Untergrenze für f. Die vollständigen gemeinsamen Koeffizienten werden zuerst kombiniert. Erst anschließend werden lineare Terme mit ihrem eigenen Quadrat exakt minimiert; gemischte Produkte werden einzeln eingeschlossen. Es wird keine starke Dualität vorausgesetzt.

Die Suche umfasst s=k/1024 für k=−128,…,128 sowie die zusätzlichen Endpunkte ±1/2 und ±2: 261 verschiedene Koordinaten. Für jede werden −F(s), F(s) und F′(s) geprüft, insgesamt 783 Ziele. Das bekannte Fenster [0,9/256] und alle fünf ursprünglichen symmetrischen Kandidatenfenster sind enthalten.

Für die numerische Kandidatensuche sind die Cuts positiv mit 10⁵ beziehungsweise 10² skaliert. Zunächst werden alle Paare aus {0}∪{2ᵏ: k=−20,…,10} geprüft; danach folgen höchstens 42 Verfeinerungsstufen mit je zwölf Durchläufen und 16 Richtungen. Die Kandidaten werden auf rationale Zahlen mit Nenner 2⁴⁰ gerundet. Ausschließlich ihre anschließende exakte rationale Auswertung entscheidet über ein Zertifikat. Sämtliche F-Fehlerradien bleiben enthalten. Die bisherige Koeffizienten-Intervallauswertung bleibt als zusätzlicher gültiger Einschluss erhalten.

**Vier Reserven auf Root für [0,9/256]**, nach positiver Normierung durch 10²⁰. Die Dezimalzahlen dienen nur der Orientierung; die Entscheidungen verwenden vollständige rationale Werte.

| Ziel | Bisher beste Untergrenze | Mit beiden H₀-Bedingungen |
|---|---:|---:|
| -F(0) | -0.017698748826 | -0.017698748826 |
| F(9/256) | -0.100639627832 | -0.0997947378643 |
| F′(0) | -0.0684308451155 | -0.0684308451155 |
| F′(9/256) | -1.35041877016 | -1.35041877016 |

Vor dem Schnitt mit den geerbten Koeffizienten-Schranken verbessern sich die gemeinsamen Polynom-Untergrenzen bei 708 der 783 Ziele. Danach bleiben 271 Verbesserungen übrig. Kein Rand- oder Ableitungsziel erhält in diesem Test eine strikt positive Reserve; es entsteht kein zertifiziertes Root-Fenster.

**Aussagegrenze:** Das ist das Ergebnis einer endlichen Multiplikator- und Fenstersuche mit dem beschriebenen Bereichsauswerter. Es ist kein Unmöglichkeitsbeweis für die beiden H₀-Bedingungen, andere Multiplikatoren, weitere notwendige Bedingungen oder eine stärkere gemeinsame Polynomauswertung. Die Rechnung entscheidet auch keine dominante Ursache des Wrapping-Verlusts auf ganz Root.

Der nächste mathematische Ansatz müsste konkret eine stärkere gemeinsame Schranke begründen. Aus diesem Ergebnis allein folgt kein Anlass für neue Operatorrechnung oder einen großen adaptiven Baum.

## Prüfungen und Reproduktion

- Zwei bytegleiche Endpunktläufe und zwei bytegleiche Erzeugungen der Cut- und Domänendateien. PULLBACK.json bleibt bytegleich mit dem vorherigen Paket.
- Separater Bereichs-/Newton-Audit: 19 Fälle, 59 Randwert-/Ableitungstripel, neun maximale Linien und 36 Newton-Schritte. 13 verschiedene Winkelumrechnungen werden mit Arb bei 768 Bit geprüft.
- Der separate rationale Root-Audit rekonstruiert beide Cut-Koeffizientensätze unmittelbar aus der Matrixformel und kontrolliert alle 783 ausgewählten Multiplikator-Untergrenzen einschließlich der geerbten Intervalle. Negative Kontrollen verwerfen ein falsches Multiplikatorvorzeichen und einen verfälschten Fehlerradius.
- Reproduktionswrapper mit geschlossenem SHA-256-Manifest und eingebundenem vorherigem Quell-ZIP. Das fertige Paket wird zusätzlich im Audit-Modus geprüft.

Für den Standardlauf werden Python 3.11 oder neuer und python-flint 0.9.0 benötigt:

```text
python -m pip install -r requirements-audit.txt
python -B reproduce.py --out ../h0-root-replay
```

Der Standardlauf rekonstruiert Endpunkt- und Cut-Dateien und prüft alle gespeicherten Multiplikatoren exakt. Er wiederholt nicht die numerische Suche. Mit `--audit-only` werden die gelieferten Dateien direkt geprüft; mit `--repeat-search` kann zusätzlich die numerische Suche erneut ausgeführt werden (NumPy 2.3.5). Deren Gleitkomma-Kandidaten können plattformabhängig variieren; ihre rationalen Zertifikate werden stets neu geprüft.

Die Operatorintegrale und sämtliche ursprünglichen Koeffizientenmodelle werden nicht unabhängig neu aufgebaut. Die geerbte physische Modellkonstruktion wird wiederverwendet. Diese lokale Rechnung und ihre separaten Arithmetikprüfer sind keine externe Begutachtung.

## Herkunft und unveränderte Grenzen

- PR #206, gebundener Head: `c5c779d42a866db0b21ef02b18d3585e1a7450ec`.
- Vorheriges Rücktest-ZIP: `3cc4c4989ec0fe0f10b8451ee064374fa6252d83f47239d79a95b6b59b2a1e74`.
- Vorheriges Manifest: `ae45783a44fdaca348d120a31c656ef48330b20bd34af0a925840fb60950abed`.
- Ursprüngliches PR-Quell-ZIP: `b6f6078172ac97f5dcd61fb0ed76acd44e0b0a2c53a82ac554c831cd6732a663`.

Root, slice/two_thirds und die acht Diagnoseboxen bleiben UNRESOLVED. Der five_eighths-Abschluss ist bedingt auf seinen Vier-Y-Schnitt. PR #187/A13, der globale Verifikationssnapshot und alle Operatorquellen wurden nicht verändert. Allgemeines Renewal, kofinale Positivität, globales Objekt X und RH bleiben offen. Ein aktueller Live-Status von GitHub wird mit dieser lokalen Rechnung nicht behauptet.
