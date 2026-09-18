# Kritisches mathematisches Review von PR #137

Prüfstand: **8074d14508873e09068222b9703b1f34e8607fc6**, 18. September 2026.
Reviewer: GPT 2, mit eigener Autorenschaft an Teilen der geprüften Kette.
**Autorenseitiges Review; keine unabhängige externe Begutachtung.**

## Urteil und Umfang

Für den konsolidierten positiven Hauptsatz habe ich nach Prüfung der
analytischen Argumente und der Zertifikatsrechnung **keinen neuen
blockierenden mathematischen Fehler gefunden**:

\[
 Q_W[u]>10^{-13}\|u\|_2^2,\qquad
 0<a\le B=\frac{\log5}{2},\quad 0\ne u\in\mathcal W_a,
\]
\[
\mathcal W_a=H^1_0((-a,a))\cap\ker E_+\cap\ker E_-.
\]

Das ist ein positives Urteil für diesen präzisen Satz. Es ist weder eine
pauschale Freigabe sämtlicher historischer Aussagen in PR #137 noch ein
Beweis für größere Fenster. Der Forschungsstatus bleibt
**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**. Dieses Review führt keine
Hochstufung auf AUTHOR-VERIFIED und keine Merge-Entscheidung herbei.

Die neu ausgeschriebenen analytischen Begründungen stehen in
[ANALYTIC_DETAILS.md](ANALYTIC_DETAILS.md). Insbesondere habe ich die
Formbereichsfrage des Endpunktbeweises geprüft, nicht aus bestandenen
Matrixrechnungen auf einen unendlichdimensionalen Satz geschlossen.

## Befunde mit Handlungsbedarf

### R1: Die vorgeschlagene orthogonale H1-Core/Shell-Zerlegung ist falsch

Fundstelle: `window-gap-monotonicity-2026-09-18/PROOF.md`, Zeilen 147-153;
auch die offene Shell-Formulierung im Konsolidierungspaket wiederholt sie.
Der Befund wurde bereits im Nachtrag `8074d145` dokumentiert.

Die alte Quellklasse E=J(W_B^even) ist kein abgeschlossener Unterraum des
umgebenden L2-Raums. Relative Abgeschlossenheit innerhalb der H1-Quellen
liefert keine orthogonale Zerlegung dieses unvollständigen Raums. Noch
konkreter: Die L2-Projektion auf den Abschluss von E kann bei +/-B einen
Sprung erzeugen und liegt dann nicht in H1. Eine glatte zulässige Quelle
mit u(B)=1 und getrennt verschwindendem Core- und Shell-cosh-Moment
liefert genau dieses Gegenbeispiel.

**Erforderlich vor Benutzung dieser zukünftigen Konstruktion:** eine
zulässige Zerlegung mit bewiesenem Formbereich, Trace- und Momenttransport
herstellen oder die betreffende Darstellung ausdrücklich als nicht
etablierte formale Vorlage kennzeichnen. Das vollständige Gegenargument
steht im früheren Nachtrag `pr137-consolidation-audit-2026-09-18/OPEN_PROBLEMS.md`, O1.

**Auswirkung:** Blockiert diese Shell-Beweisroute in der vorliegenden
Form. Betrifft weder den Monotoniesatz in Abschnitten 1-4 noch den
positiven Endpunktsatz. Dieser verwendet einen anderen, gültigen
Legendre-Low/Tail-Split im größeren geschlossenen Formbereich.

### R2: Historische Prüfsummen sind nicht durchgehend konsistent

Unter 19 gebundenen historischen Manifesten sind fünf mit insgesamt neun
Einträgen veraltet. Betroffen sind `analytic-waxing-function`,
`connected-193_500`, `connected-19_50`, `connected-387_1000` und
`node-schur-waxing`, jeweils vom 17. September. Eine reine CRLF/LF-Umrechnung
erklärt die Abweichungen nicht. Die exakten Soll-/Ist-Werte stehen im
früheren Nachtrag `historical_manifest_audit.json`.

**Erforderlich für eine vollständige Integritätsbehauptung:** die
historischen Zertifikate versioniert aufarbeiten oder ausdrücklich als
historisch und nicht erneut zertifiziert ausnehmen. Keine stillschweigende
Neugenerierung historischer Hashes oder Hochstufung alter Logs.

**Auswirkung:** Keine pauschale Aussage, sämtliche Dateien dieser PR seien
SHA-konsistent. Die sieben zentralen Pakete der hier geprüften Kette sind
konsistent und wurden mit gebundenen, unveränderten Eingaben reproduziert.
Der positive Hauptsatz hängt nicht von den veralteten Waxing-Zertifikaten ab.

### R3: Die konkrete Bandroutine behandelt zusammenfallende Grenzen nicht

Neue reproduzierte Implementierungsgrenze in
`prime-power-segment-4-2026-09-18/check_segment.py`, Zeilen 361-374:
`shift_grams` sammelt alle Bandgrenzen, sortiert sie und verlangt strikt
getrennte Intervalle, ohne bewiesen identische Grenzen zusammenzufassen.
Die exakten rationalen Shifts d1=4/5 und d2=6/5 liefern beide die Grenze
1/5. Der Aufruf bricht an Zeile 374 mit AssertionError ab.

Der beigefügte Checker reproduziert dieses Verhalten ausdrücklich als
bekannte Einschränkung. Sein PASS bedeutet hier, dass die Ablehnung
reproduziert wurde, nicht dass diese Konfiguration unterstützt wird.

**Erforderlich für eine allgemeine Implementierung:** exakte Gleichheiten
von Grenzen erkennen und zusammenfassen; bei lediglich überlappenden
Intervallen Gleichheit nicht raten, sondern verfeinern oder gesondert
abschätzen. Mathematisch sind gleichzeitige Eintrittsereignisse zulässig.

**Auswirkung:** Kein falsches Positivitätszertifikat; die Routine bricht
sicher ab. Bei B=log5/2 sind die verwendeten Grenzen zertifiziert strikt
getrennt. Der Hauptsatz ist nicht betroffen. Der abstrakte Satz für
endliche aktive Mengen ist allgemeiner als diese konkrete Routine.

## Was mathematisch geprüft wurde

Die additive explizite Formel wurde mit der angezeigten Originalformel
in [Suzuki, arXiv:2606.09096v2, Abschnitt 1.1](https://arxiv.org/html/2606.09096v2)
abgeglichen. Diese Prüfung betrifft Normierung und Vorzeichen der Formel;
sie importiert keine globale Positivität aus dieser Arbeit. Der Übergang
zur Connected-Form, die Polelimination mit genau zwei Momenten, die
archimedische Konstante und die Gewichte log(p)/p^(k/2) stimmen damit überein.
Insbesondere erhält der Kanal 4 das Gewicht log2/2.

Für die Referenzform wurden die Identität des singulären Energieteils mit
der harmonischen Legendre-Diagonale, der geschlossene Formbereich und die
Zulässigkeit endlicher polynomialer Projektionen begründet. Die positiven
Tailböden beziehen sich auf den gesamten unendlichen Tail. Die logarithmischen
und Translations-Tails gehen über vollständige Gram-/Parseval-Identitäten
ein; allein der exakt polynomiale Gamma-Modellanteil besitzt endlichen
Support. Sämtliche geordneten gemischten Shift-Terme bleiben enthalten.

Die exakte Momentrekonstruktion und ihr unendlicher Rest wurden als
beschränkter Formfehler kontrolliert. Dazu genügt die Wirkung des ansonsten
unbeschränkten Operators auf den einzelnen polynomialen Momentträger.
Geprüft wurden außerdem die unterschiedlichen Normgewichte in inverser
Schur-Spur und Kopplungsspur, die tatsächliche unendlichdimensionale
Schur-Transformation und deren inverse Norm. Am Schluss wird die gesamte
rücktransformierte Untergrenze durch 1+beta dividiert.

Die physische Nullfortsetzung erhält Norm, Form und beide Momente. Wegen
der verschwindenden Randspuren bleibt sie in H1_0. Damit trägt der
Endpunktbeweis das ganze Intervall ohne Parameterraster. Der Monotoniesatz
benötigt nur die Inklusion zulässiger Testmengen, keine Shell-Zerlegung.

Die explizite gerade Fast-Null-Quelle ist eine tatsächliche H1_0-Quelle
mit exakt korrigiertem cosh-Moment; das sinh-Moment verschwindet durch
Parität. Ihr Rayleigh-Quotient ist eine obere Schranke des optimalen Gaps.
Eine inverse Iteration zur Auswahl rationaler Koeffizienten ersetzt dabei
nicht die anschließende gerichtete Energieeinschließung.

## Reproduktion und zusätzliche Gegenrechnungen

Die sieben vollständigen Checker-Replays des unmittelbar vorangegangenen
Konsolidierungsreviews werden mit unveränderten Eingaben übernommen:
Prime-2: 22, Prime-2/3: 23, aktive Mengen: 381, universelle Familie: 349,
Segment bis B: 15, ausgewählte Quellenfamilie: 27, Monotonie: 5 Prüfgruppen.
Alle sieben Läufe bestanden; Ausgaben, Zeiten und Hashes sind in
`pr137-consolidation-audit-2026-09-18/replay_results.json` und `replays/`
gespeichert. Diese Zahlen sind verschieden zugeschnittene Prüfgruppen,
kein Maß mathematischer Beweissicherheit.

Hinzu kommen **678 bestandene exakte beziehungsweise rationale gerichtete
Intervallprüfungen** mit separat ausgeschriebenen Formeln:

| Gegenrechnung | Anzahl |
|---|---:|
| Rodrigues-Basis / singuläre Eigenidentitäten | 129 + 129 |
| Vollständige Gamma-Bildpolynome durch direkte Dreiecksintegration | 84 |
| Logarithmische Off-Diagonal-Einträge | 74 |
| Beta-Shift-Einträge aus direkter Bandintegration | 123 |
| Geordnete gemischte Shift-Gram-Einträge | 41 |
| V-Shift-Einträge aus separaten logarithmischen Stammfunktionen | 41 |
| Gerichtete Vorzeichen- und Kehrwertfälle | 56 |
| Dokumentierte Ablehnung kollidierender Grenzen | 1 |

Der neue Checker bindet 44 Eingabedateien durch SHA-256. Er verwendet die
vorhandene Intervallarithmetik zum Vergleich mit separat berechneten
rationalen Integralen bzw. analytischen Stammfunktionen. Das ist eine
zusätzliche Implementierungskontrolle, keine vollständig unabhängige
Arithmetikbibliothek. Die endlich vielen Tests ersetzen die allgemeinen
analytischen Begründungen nicht. Weder Quadratur noch numerische
Eigenwerte werden als Beweis eingesetzt.

## Aussagegrenzen und Empfehlung

Die reproduzierte normierte Endpunktuntergrenze liegt even oberhalb von
1.04238900475e-13 und odd oberhalb von 2.383164924426e-11. Somit bleibt der
konservativ formulierte gemeinsame Satz mit 10^-13 bestehen. Die positiven
Tailböden über 0.7194 bzw. 0.7348 allein würden dafür nicht genügen.

Die bekannte Quelle mit R_B ungefähr 3.29629e-12 setzt auch für spätere
Fenster nur eine obere Schranke des optimalen Gaps. Dieser Wert ist kein
uniform verfügbarer Puffer. Ein skalarer zukünftiger Schur-Abzug kleiner
als 3.3e-12 wäre deshalb noch kein All-Source-Beweis; dafür müsste man
beispielsweise die zertifizierte Untergrenze 10^-13 oder eine gültige
richtungsabhängige relative Abschätzung benutzen.

Ich empfehle, den konsolidierten Satz bis log5/2 als positiven,
autorenseitig kritisch geprüften Meilenstein weiterzuführen. R1 bleibt
als verworfene formale Shell-Zerlegung markiert; R2 und R3 bleiben als
Integritäts- bzw. Implementierungsgrenzen sichtbar. Kein Ergebnis für
alle Quellen rechts von B, bei log7/2 oder bei a=1 folgt hieraus.
Die ausgewählte transportierte Quellenfamilie ist kein solcher Satz.

Eine externe unabhängige Begutachtung bleibt offen. Dieses Review
beansprucht weder eine vollständige Neuderivation jeder historischen
Waxing-Behauptung noch eine neue unabhängige Zertifizierung sämtlicher
Details der speziellen Quellenfamilie bis log7/2. PR #137 bleibt Draft,
offen und ungemergt; main und Registry bleiben unverändert.
