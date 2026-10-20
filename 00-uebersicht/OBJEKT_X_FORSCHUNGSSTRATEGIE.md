# Forschungsstrategie für die Konstruktion von Objekt X

## Aktuelle Entscheidung vom 20. Oktober: keine Großrechnung auf diesem Kontrollweg

- [x] Vollständigen oberen Testendpunkt bestimmen: F_up etwa 54.475251e-6
  liegt über Budget_lo etwa 54.117169e-6; gemeinsame D/U-Formfehlerhülle
  als größten Preis identifiziert.
- [x] Exakte Antwortdarstellung prüfen: Rang 84, aber bereits ihre
  günstigste E_new-gewichtete Koeffizientenenergie beträgt etwa 5.78e40.
- [x] Formboden und erforderlichen Restpreis bestimmen:
  kappa>3.24380497686e-6; die nötige ganze Restobergrenze ist mit diesem
  F_up negativ und daher nicht erfüllbar.
- [ ] Einen anderen gemeinsamen Kontrollweg mit quantitativer Aussicht
  für F-Hülle und vollständiges Residuum begründen; kein Kandidat ausgewählt.
- [ ] Punkt 4 und externe fachliche Prüfung abschließen.

Der [Gesamtbericht](../research/x-c1/w9-rest-feasibility-even-2026-10-20/PROOF.md)
entscheidet die Machbarkeit der vorgeschlagenen Abschätzung:
**UPPER_CONTROL_ROUTE_TOO_COARSE**. Dies ist kein Ausschluss der Unterform.
Keine neue Integration und keine Suche nach anderen Koeffizienten zur
Rettung derselben E-Majorante; deren Mindestpreis ist bereits eingeschlossen.
Fehlende scharfe gemeinsame L-Dualdaten sind benannt. Kein Folgeauftrag gestartet.

## Zusatz vom 20. Oktober: positiver eta-q-Anteil geprüft

- [x] eta q[Jw] am unveränderten Vektor aus #248 mit vorhandenem direkten
  Formsandwich einschließen: [8.78184963678; 8.78184963679]e-10.
- [x] Alte Grenzen unverändert übernehmen und den unteren Gesamtansatz
  ergänzen: >53.19429074226e-6; weiterhin `SCHUR_LOWER_TEST_OPEN`.
- [ ] Die Kontrollierbarkeit des ganzen variationalen Restes
  ||nu_new-H_new Jw||²_(H_new^-1) mit vorhandenen vollständigen Dualdaten
  und einer zertifizierten Formuntergrenze quantitativ vorprüfen.
- [ ] Punkt 4 und externe fachliche Prüfung abschließen.

Auch die obere eta-q-Grenze deckt weniger als 0.095067 % der bisherigen
Lücke. Diesen Term weiter zu verengen ist bei sonst gleichen Grenzen
keine entscheidende Verbesserung. Die verbleibende Lücke ist keine Reserve.
Der [Bericht](../research/x-c1/w9-eta-q-even-2026-10-20/PROOF.md)
nennt die genaue Residualidentität und einen begrenzten Kontrollweg.
Keine neue Integration, Suche oder automatische Folgerechnung wurde gestartet.
Die folgenden Abschnitte halten die vorausgehenden Entscheidungen fest.

## Nachtrag vom 20. Oktober: Gewichte ausgeschlossen, neue Unterform offen

Der [begrenzte gekoppelte Schurtest](../research/x-c1/w9-new-k-schur-underform-even-2026-10-20/PROOF.md)
ist abgeschlossen. Die zwei Ergebnisse bleiben getrennt:

- [x] Die ganze feste Young-Gewichtsfamilie mit den rationalen #246/#247-Endpunkten
  ausschließen: Energie >65.23831878691e-6 gegenüber Budget <54.11716937864e-6.
- [x] Genau einen rationalen variationalen Testvektor für K_new am unveränderten
  physischen Zeugen auswerten: Untergrenze >53.19341255729e-6, `SCHUR_LOWER_TEST_OPEN`.
- [ ] Vor einer oberen Großrechnung die bislang nicht kontrollierten Beiträge
  quantitativ begrenzen. Der offene Test ist keine Reserve.
- [ ] Punkt 4 und externe fachliche Prüfung abschließen.

Für unverändertes K_new und P_new_upper sind weitere Gewichtsexperimente
begründet beendet. Der offene gekoppelte Test beweist weder ein Scheitern
aller Majoranten von Q_new^-1 noch eine ausreichende Verbesserung durch
einen engeren oberen Vergleich. Auch die Ursache des Hindernisses ist damit
noch nicht abschließend lokalisiert. Eine quantitative Vorprüfung müsste den
ungenutzten eta-q-Gewinn sowie den verbleibenden variationalen Gewinn
einschließlich des unendlichen Raums und aller Fehler kontrollieren.

Ein einzelner interner Testvektor wurde für die neue Unterform vorab
eingefroren; der physische Zeuge, die äußere Antwort und das Budget blieben
gleich. Alle vorhandenen Paarungen und gemeinsamen Fehlergrame wurden
übernommen. Keine neue Integration, adaptive Richtungssuche, parallele
Antwortmatrix-Suche oder automatische Nachschärfungsserie.
Das Autorenresultat bleibt extern offen und ist keine Main-Integration.
Die folgenden Abschnitte dokumentieren die vorherigen Entscheidungen.

## Fortschreibung vom 20. Oktober: Auswahl, Teilpass und Dualentscheidung

Der begrenzte Forschungszweig #245–#247 ist unter den gebundenen Voraussetzungen
entschieden: **FULL_FIXED_COMPARISON_EXCLUDED_BY_DUAL_LOWER**. Die drei Pakete
sind gestapelte offene Entwürfe, keine hier behauptete Main-Integration.
Ihr Status bleibt `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`; die Einträge bleiben
`PENDING_STATUS_REVIEW`. Diese Dokumentation übernimmt die veröffentlichten
Belege und verschiebt weder Beweisanker noch `verified_through`.

| Stufe | Aussage | Gepinnter Beleg |
| --- | --- | --- |
| #245, Auswahl | K_new und feste Gewichte sind zulässig; die neue Unterform unterscheidet sich von K_star | [Herleitung auf a60f760](https://github.com/Waschtl904/objekt-x-programm/blob/a60f7602335f654ca7b42e8362e47af243e20462/research/x-c1/w9-matrix-error-selection-2026-10-20/PROOF.md) |
| #246, Teiltest | Teilenergie in [53.68719767242; 53.90213205365] ×10^-6; gerichtete Reserve >2.15037307060e-7 | [Ergebnis auf 93cf629](https://github.com/Waschtl904/objekt-x-programm/blob/93cf629d5efdbf93d6a3cfef8cb849134f1f72ff/research/x-c1/w9-matrix-error-pilot-even-2026-10-20/RESULT.json) |
| #247, Gesamtentscheidung | Dualenergie >1.369503316340e-6; Gesamtenergie >69.15149379521e-6 gegenüber Budget <54.11716937864e-6 | [Ergebnis auf d7a0a32](https://github.com/Waschtl904/objekt-x-programm/blob/d7a0a327140e51452be6c2dcd8995f7660089e58/research/x-c1/w9-dual-preflight-even-2026-10-20/EXPECTED.json) und [Herleitung](https://github.com/Waschtl904/objekt-x-programm/blob/d7a0a327140e51452be6c2dcd8995f7660089e58/research/x-c1/w9-dual-preflight-even-2026-10-20/PROOF.md) |

Der gerichtete Abstand ist >15.03432441658e-6, rund 27,8 % der
Budgetobergrenze. Der Teilpass bleibt bestehen: Er enthielt den Dualterm
ausdrücklich nicht. Die Gesamtentscheidung betrifft nur die ausgewählte
vollständige W_new-Majorante mit K_new, den festen Gewichten, der eingefrorenen
Antwortregel und ihrem Budget am festen geraden Zeugen. Sie ist kein Ausschluss
der tatsächlichen A9-Inverse, aller Majoranten der neuen Unterform, anderer
Gewichte oder anderer Antwortregeln und liefert keine negative Weil-Richtung.
Der ältere K_star-Klassenausschluss aus #239 behält seinen eigenen Scope.

Die korrekte Abbruchregel verwendet die **Gesamtuntergrenze**:

    E_full,lower = E_partial,lower + (a/beta) D_full,lower > K_P,upper.

Eine Dualobergrenze <1.90434988323e-8 wäre hinreichend für Erfolg gewesen.
Für den Ausschluss ist dagegen eine Dualuntergrenze oberhalb der getrennten
Schwelle (K_P,upper - E_partial,lower)/(a/beta) maßgeblich, etwa
3.807788423766e-8. Die nachgewiesene Untergrenze übersteigt diese rund
36-fach. Eine zu große Obergrenze allein wäre unentschieden geblieben.

Abgeschlossene Aufgaben dieses Zweigs:

- [x] Einen zulässigen Kandidaten und seine Gewichte einfrieren (#245).
- [x] Teilenergie und alle betroffenen Fehler gemeinsam einschließen (#246).
- [x] Den vollständigen festen Vergleich durch eine gültige Dualuntergrenze entscheiden (#247).
- [x] Belege, Wiederverwendung und Stopplinie gemeinsam festhalten.
- [ ] Externe fachliche Prüfung der gebundenen Kette abschließen.
- [ ] Punkt 4: vollständigen konstruktiven A9→A11-Anschluss herstellen.

Diese Häkchen zählen erledigte Aufgaben, keine Prozentanteile an Objekt X.
Für die ausgeschlossene feste Kombination entfallen obere Dualeinschließung,
neue Restintegration und zusätzliche Präzision als nächste Arbeitsschritte.
Ein konkreter mathematischer Einwand, Provenienzfehler oder reproduzierbarer
Zertifikatsfehler bleibt ein Grund, den Befund erneut zu prüfen.

Vor einem neuen Versuch müssen gemeinsam vorliegen:

1. Eine konkrete Änderung der Gewichte, Unterform oder Antwortregel und die
   genaue Voraussetzung des bisherigen Ausschlusses, die dadurch entfällt.
2. Eine quantitative Aussicht für die **vollständige** Energie einschließlich
   Dualterm, zugehörigem K_P-Budget und sämtlichen betroffenen Fehlern. Ein
   besserer Teilwert allein genügt nach #246–#247 nicht.
3. Das Inventar unverändert übernommener Quellen, Paarungen und Fehlergrame
   sowie der wegen der Änderung tatsächlich neu benötigten Größen.
4. Genau ein begrenzter Entscheidungstest mit Aufwandgrenze, Abnahme- und
   Stopkriterien; keine automatische Varianten- oder Nachschärfungsserie.

Noch ist kein solcher neuer Kandidat ausgewählt. Die grundsätzliche Offenheit
anderer Vergleiche ist keine quantitative Begründung für einen weiteren Lauf.
Meilenstein 4, N12, allgemeine Fortsetzung und Objekt X bleiben offen.

Die bisherigen frischen Paket-Replays werden mit ihren eigenen Rechenankern
übernommen: [#245-Abnahme](https://github.com/Waschtl904/objekt-x-programm/blob/a60f7602335f654ca7b42e8362e47af243e20462/research/x-c1/w9-matrix-error-selection-2026-10-20/ACCEPTANCE.json),
[#246-Abnahme](https://github.com/Waschtl904/objekt-x-programm/blob/93cf629d5efdbf93d6a3cfef8cb849134f1f72ff/research/x-c1/w9-matrix-error-pilot-even-2026-10-20/ACCEPTANCE.json),
[#247-Abnahme](https://github.com/Waschtl904/objekt-x-programm/blob/d7a0a327140e51452be6c2dcd8995f7660089e58/research/x-c1/w9-dual-preflight-even-2026-10-20/ACCEPTANCE.json).
Dieser Nachtrag ändert keine Eingaben, Zertifikate oder Prüfregeln. Seine
Abnahme umfasst Diff-, Verweis- und Registerprüfung einschließlich erzeugter
Ansichten; unveränderte Funktionsintegrationen und Zertifikatsreplays sind
dafür kein erneuter lokaler Pflichtlauf. Die anwendbare CI bleibt erforderlich.

## Fortschreibung vom 19. Oktober: feste Vergleichsklasse beendet

Die [Formfehlerschärfung am festen geraden Zeugen](../research/x-c1/w9-schur-form-error-even-2026-10-19/PROOF.md)
liefert eine untere Inversenergie oberhalb des zugehörigen K_P-Budgets.
Damit scheitert jeder obere Vergleich W >= Q_lower,*^-1 bei genau dieser
K*-Unterform, eingefrorenen Antwortregel und unverändertem Budget, unter den
gebundenen Voraussetzungen. Die Forschungskette und die späteren
Main-Korrekturen sind über [PR #241](https://github.com/Waschtl904/objekt-x-programm/pull/241)
zusammengeführt und nach Main übernommen; die Variantenbilanz aus #240
ist im Register erhalten.

Für denselben Vergleich folgt daraus eine Stopplinie: keine weitere
Obermajorantenverfeinerung, neue Richtungssuche oder RL-Rechnung mit dem Ziel,
den bereits vorhandenen Gegenzeugen zu beseitigen. Die frühere offene
Schur-Untergrenze bleibt eine korrekte gröbere Abschätzung; der Nachfolger
entscheidet ihre offene Frage. Ein konkreter mathematischer oder
Provenienzeinwand bleibt ein Grund, den Befund erneut zu prüfen.

Vor dem nächsten Rechenauftrag ist festzuhalten:

1. Welche Voraussetzung des Ausschlusses ändert der vorgeschlagene Ansatz?
2. Welche vorhandenen Quellen, gemeinsamen Paarungen und Fehlergrame werden
   übernommen, und welche Größen müssen wegen der Änderung erneuert werden?
3. Welche quantitative Abschätzung rechtfertigt genau einen begrenzten Test,
   und welches Ergebnis beendet diesen Weg?

Bei einer anderen Antwortregel sind Residuum, K_P-Budget und Fehler gemeinsam
zu ändern. Eine andere Unterform benötigt ihre eigene Zulässigkeit und
vollständige Restkontrolle. Andere zulässige Majoranten der tatsächlichen
A9-Inverse bleiben ebenfalls offen, soweit sie nicht der ausgeschlossenen
Klasse angehören. Eine bessere Variante wird hier nicht behauptet oder
automatisch gestartet. Ein positiver vollständiger Anschluss benötigt
weiterhin beide Paritäten und die gesamte Energie einschließlich Dualterm
oder einer bewiesenen Ersatzabschätzung.

Die vorhandenen endlichen Positivitätssätze und der konstruktive A8→A9-Anschluss
bleiben unter ihren Voraussetzungen bestehen. Der neue A9→A11-Anschluss,
Meilenstein 4, N12, allgemeine Erneuerbarkeit und externe Prüfung bleiben offen.
[NEXT_GATES](NEXT_GATES.md) ist die operative Aufgabenliste; die folgenden
datierten Zwischenstände sind als Entwicklungsgeschichte zu lesen.

Stand 3. Oktober 2026. Arbeitsstrategie auf Grundlage der gelesenen Beweispakete und der lokalen Folgeuntersuchungen. Dieses Dokument beweist keine neue Terminalpositivität und verändert keinen mathematischen Registerstatus.

Fortgeschrieben nach GPT 1s Rückmeldung vom selben Tag. Neu präzisiert sind die vollständige Blockdarstellung in einer unabhängig positiven Hilbertnorm, die gemeinsame Auswertung korrigierter Quellen und eine obere Schranke für die inverse alte Residualenergie. Der zuvor vorgeschlagene isolierte Test des H₀-Blocks (4,5) entfällt aufgrund des übermittelten Grenzberichts; dessen neue Zahlenzertifikate wurden hier nicht erneut reproduziert.

## Fortschreibung vom 15. Oktober: vollständige Zertifikate erneuern

Der [verbindliche A9→A11-Arbeitsauftrag](../research/x-c1/a9-a11-certificate-calibration-2026-10-15/WORK_ORDER.md)
präzisiert den nächsten Schritt als Kalibrierung einer erneuerbaren vollständigen
Zertifikatsklasse. Gefordert sind vollständige Residualenergie, eine positive
Vergleichsform mit auswertbarer Inverse, die neue gemeinsame Inversmajorante
und ihre nächste Schnittstelle. Die bekannte A11-Positivität darf keine Eingabe
sein. Eine feste Dimension oder gleichbleibende Reserve ist nicht erforderlich.

Das [bedingte Inversfortsetzungslemma](../research/x-c1/conditional-inverse-propagation-2026-10-15/PROOF.md)
liefert die analytische Ausgabeformel, wenn die vollständige Bilanz bewiesen ist.
Es ist als AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN und ausstehende Statusprüfung
erfasst. Die zwölf Algebra-Kontrollen begründen keinen arithmetischen Erneuerungssatz.

Der Auftrag trennt PASS, CERTIFICATE_FAIL, MATHEMATICAL_FAIL und UNRESOLVED.
Kofinalität wird parallel untersucht. Exakte Formidentifikation und Readout
bleiben von einem bloßen positiven Untervergleich getrennt. Vor A11→A13 werden
Eingaben, Antwortregel, Vergleichsklasse, Fehlerbudget und Abnahme eingefroren.
Der konstruktive A9→A11-Zertifikatszustand bleibt UNRESOLVED.

## Fortschreibung vom 14. Oktober: ursprünglicher Tail geschlossen

Der [gemeinsame Tail-Nachtrag](../research/x-c1/basis84-tail-closure-2026-10-14/README.md) schließt den ursprünglichen
W_X-orthogonalen Basis84-Tail unter den gebundenen Voraussetzungen:
tau|Z84 >= (2/3) W_X und A_Z^-1 <= (3/2) I. Der neue Komplementwechsel
begründet die Übertragung vom zuvor behandelten L-orthogonalen Schurrest.
Die frühere offene Forderung 1/20 ist damit erledigt; der alte hinreichende
268-Funktional-Fittest muss dafür nicht abgeschlossen werden.

Für neue vollständige Hilbertresiduen auf Z84 kann hier 3/2 statt 20 benutzt
werden. Die gerichtete Inversmajorante bleibt zusätzlich verfügbar. Nächste
Forschungsaufgabe sind die vollständigen gemeinsamen Quellenenergien und
Residuen für A9→A11 sowie die externe Prüfung der analytischen Gesamtkette.
Weitere konstruktive Horizonte, Wiederholbarkeit und Objekt X bleiben offen.

Die folgenden datierten Zwischenstände bleiben Entwicklungsgeschichte.
Ihre damaligen offenen Tailstatus werden durch diesen Abschnitt überholt.

## Vorangehende Fortschreibung vom 14. Oktober

Die [konkrete A9-Inverserneuerung](../research/x-c1/a9-inverse-renewal-2026-10-13/README.md)
liefert nun eine gemeinsame Majorante für beliebige neue Quellen. Nach
Schurelimination der 84 Antwortfunktionen besitzt der ganze neue hohe Rest
mindestens 2/3 W_X, unter den gebundenen Voraussetzungen. Die konkrete
[Domänenherleitung](../research/x-c1/a9-domain-continuation-2026-10-13/PROOF.md)
liegt als extern noch zu begutachtender Autorenbeweis vor.

Der nächste Rechenauftrag ist damit die vollständige gemeinsame Quellenenergie
für A9→A11 gegen diese Majorante: alte Inversenergie, Zwölferanteil, ganzer
L-Dualgram und 84 endliche Antwortkoordinaten. Alle Kreuzfehler bleiben gemeinsam.
Eine bloße endliche Projektion genügt nicht. Die allgemeine Wiederholbarkeit
des Erneuerungsschritts und eine kofinale Horizontfolge bleiben offen.
Der neue Boden gilt auf einem anderen Rest als der alte offene Tailboden 1/20.

## Fortschreibung vom 13. Oktober

Der [bedingte globale A8→A9-Schurabschluss](../research/x-c1/a8-a9-global-closure-2026-10-13/README.md)
schließt den ersten konstruktiven Anschluss einschließlich des unendlichen
Formdualrests, unter den gebundenen Operator-, Domänen- und Raumzerlegungsannahmen.
Die im Zwischenstand vom 7. Oktober noch fehlende globale Restbilanz ist damit
auf diesem Beweisweg hergestellt. Die Chronologie dokumentiert auch die
widerlegten Zwischenbedingungen; deren alte Ziele werden nicht weiterverfolgt.

Nächste Aufgaben sind die externe Prüfung der benannten analytischen
Voraussetzungen und die Formulierung derselben konstruktiven Regel für A9→A11.
Dessen bereits bekannte Terminalpositivität darf in diesem Rücktest nicht
vorausgesetzt werden. Erst eine übertragbare, quantitativ präzise Regel
rechtfertigt den prospektiven nächsten Horizonttest. Der gesonderte Tailboden
1/20 bleibt offen; der A8→A9-Schluss benötigt ihn nicht.

Der [Integrationsnachweis](integrationsnachweise/PR216_2026-10-13.md) trennt
Replay und übernommene Integrationen. Die folgenden datierten Abschnitte
bleiben als Entwicklungsgeschichte erhalten; die aktuelle Reihenfolge steht
in [NEXT_GATES](NEXT_GATES.md).

## Historischer Zwischenstand: Umsetzung bis zum 7. Oktober

Stand 7. Oktober 2026: Die unten empfohlene Eingabeklassifikation und der
Aufbau des ersten Anschlusses sind inzwischen bearbeitet. Der
[Vier-Quellen-Anschluss](../research/x-c1/a8-four-source-inverse-energy-2026-10-04/README.md)
und das [Acht-Quellen-/Restpaket](../research/x-c1/a8-a9-remainder-progress-2026-10-07/README.md)
führen zu vollständigen Restkoordinaten, einem eingefrorenen Pilotraum,
Halbinverseneinschließungen und partiellen gewichteten Fehlergramen.

Der nächste Schritt ist die gemeinsame Kontrolle der sechs empfindlichen
alten Kraftkombinationen und der vier C-Kopplungen. Danach fehlen weiterhin
U00, Kreuzgramm und die vollständige komprimierte Tailnorm. Der volle
B_R-Gate und eine wiederverwendbare Fortsetzungsregel bleiben offen.
Die operative Reihenfolge steht in [NEXT_GATES](NEXT_GATES.md). Die folgenden
Herleitungen und Vorschläge behalten ihren ursprünglichen Stand.

## Ziel und Entscheidung

**Das primäre Ziel ist Objekt X. Erst nach seiner Konstruktion wird der mögliche Anschluss an die Riemannsche Vermutung verfolgt.** Diese vom Nutzer festgelegte Reihenfolge bestimmt die folgenden Prioritäten. Die mathematischen Anforderungen an X bleiben dabei vollständig erhalten.

Die Hauptarbeit soll sich auf einen **konstruktiven Fortsetzungssatz für die gemeinsame positive Geometrie** konzentrieren. Die gegenwärtige Winkeldiagnose wird zu einer begrenzten Hilfsuntersuchung. Sie soll eine genau benannte Energie- oder Kopplungsschranke liefern; ihr Abschluss wird nicht länger ohne Begründung zur Voraussetzung aller weiteren Arbeit gemacht.

Die zentrale Forschungsfrage lautet:

> Welche aus den gemeinsamen Prim-/Gamma-Daten herleitbare Schranke kontrolliert den vollständigen neuen Schurrest, ohne die Positivität des neuen Terminals vorauszusetzen, und liefert damit einen kompatiblen positiven Readout für die vergrößerte Quellenklasse?

Ein *Readout* bezeichnet hier die lineare Abbildung der Quellen in den gemeinsamen Hilbertraum. Der *Schurrest* ist die Form auf den neuen Richtungen, nachdem die Antwort des bereits kontrollierten Teils vollständig berücksichtigt wurde.

Diese Empfehlung ist eine begründete Wahl des nächsten Forschungswegs. Dass der gesuchte Fortsetzungssatz existiert oder mit den jetzigen Daten bewiesen werden kann, ist offen.

## Maßstab für Objekt X

Die [aktuelle Arbeitsdefinition](https://github.com/Waschtl904/objekt-x-programm/blob/b1a734a0a6526ea17cbfce594d877974fd70cc01/00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md) verlangt eine intrinsische gemeinsame Prim-/Gamma-Geometrie und die exakte Identität

\[
Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}
\]

auf einer geeigneten, vollständig ausgewiesenen Testklasse. Die Konstruktion darf weder die gewünschte Gesamtpositivität noch RH voraussetzen. Ein positiver Teilanteil oder eine nachträgliche abstrakte Faktorisierung einer schon positiven Form genügt nicht.

Strategischen Fortschritt messen wir deshalb an vier konkreten Leistungen:

1. **Konstruktion:** Eine neue Abbildung oder Geometrie entsteht aus unabhängig angegebenen arithmetisch-analytischen Daten.
2. **Exakte Identität:** Die vollständige Form wird einschließlich der Kreuzterme, Normalisierungen und unendlichen Reste erfasst.
3. **Kompatibilität:** Die Readouts stimmen bei Quellenfortsetzung und zulässigen Koordinatenwechseln überein.
4. **Geltungsbereich:** Die Quellenklasse und ihre Erschöpfung werden präzise kontrolliert.

Die Testklasse gehört schon zur Definition von X. Sie kann daher nicht vollständig auf eine spätere RH-Phase verschoben werden. Der Schluss aus der fertigen Konstruktion auf RH ist eine nachgelagerte Aufgabe.

## Geprüfter Ausgangspunkt

Die Strategie wurde auf Grundlage von Main `b1a734a0a6526ea17cbfce594d877974fd70cc01`, dem ursprünglichen PR-206-Beweishead `c5c779d42a866db0b21ef02b18d3585e1a7450ec` und den folgenden lokalen Untersuchungen erarbeitet. Die [Folgepakete](../research/x-c1/canonical-h0-followups-2026-10-03/README.md) erhalten ihre ursprünglichen Quellenbindungen. Der aktuelle Integrations- und Registerstatus steht in [CURRENT_STATE](CURRENT_STATE.md); diese Strategie verschiebt keine Beweisanker.

Die folgende Bilanz übernimmt den ausgewiesenen Umfang der Quellen. Sie ist keine erneute vollständige Prüfung aller Operatorintegrale. Die Forschungsresultate bleiben `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`.

| Vorhandener Baustein | Bedeutung für die Strategie |
| --- | --- |
| Physische Quellenräume, zwei Mellinbedingungen, Nullfortsetzungen und Formverträglichkeit | Die Quellenfortsetzung muss nicht neu erfunden werden. |
| Gemeinsamer spektraler Prim-/Gamma-Mediator mit exaktem Defekt | Es gibt eine konkrete, vor der Positivitätsentscheidung definierte Konstruktion. |
| Rohe T-/D-Transporte und Cocycle auf jedem endlichen Horizont | Die algebraische Transportarchitektur ist weitgehend vorhanden. |
| Positive Abschlüsse und kompatible Transporte bis A11 | Sie sind die Ausgangsgeometrie und dienen als bekannte Prüffälle. |
| Vollständiger positiver hoher Anteil auf jedem festen endlichen Horizont | Der schwierige Rest kann jeweils endlich dargestellt werden; die nötige Dimension darf wachsen. |
| Sehr starke tatsächliche Schurkopplung bei A8→A9 und A9→A11 | Eine komfortable relative Reserve darf nicht als erwartete Lösung eingeplant werden. |
| Gemeinsamer Y-Kernel und lokale H₀-Diagnosen | Sie zeigen konkrete Verluste von Abhängigkeiten, schließen Root aber nicht. |

Die einschlägigen Quellen sind der [Mediatorbeweis](https://github.com/Waschtl904/objekt-x-programm/blob/b1a734a0a6526ea17cbfce594d877974fd70cc01/research/x-c1/c1-coupled-spectral-mediator-2026-09-20/PROOF.md), das [allgemeine Wandgesetz](https://github.com/Waschtl904/objekt-x-programm/blob/b1a734a0a6526ea17cbfce594d877974fd70cc01/research/x-c1/chambers-through-a11-2026-09-28/wall/PROOF.md), der [Satz über den hohen Anteil](https://github.com/Waschtl904/objekt-x-programm/blob/b1a734a0a6526ea17cbfce594d877974fd70cc01/research/x-c1/chambers-through-a11-2026-09-28/high-tail/PROOF.md) und die [kanonischen Kopplungsschranken](https://github.com/Waschtl904/objekt-x-programm/blob/b1a734a0a6526ea17cbfce594d877974fd70cc01/research/x-c1/canonical-schur-coupling-2026-09-30/02-resolvent-moments/PROOF.md).

## Drei strategische Folgerungen

### Die kleine Reserve ist teilweise echte Geometrie

Für A9→A11 ist der tatsächliche relative Rest der festgelegten kanonischen Zerlegung eingeschlossen durch

\[
5.2319\cdot10^{-17}\le1-\kappa_{\rm gerade}\le3.0103\cdot10^{-12},
\]
\[
3.1660\cdot10^{-17}\le1-\kappa_{\rm ungerade}\le3.5804\cdot10^{-11}.
\]

Diese Intervalle sind keine genaue Messung einer einzelnen Größenordnung. Sie beweisen aber, dass die starke Kopplung dieser Räume nicht durch bessere Intervallarithmetik verschwinden wird. Eine andere Basis innerhalb derselben festgelegten Teilräume ändert κ nicht.

Eine sinnvolle Fortsetzung muss sehr unterschiedliche Energieskalen mitführen. Eine positive Vergleichsmatrix, welche die einzelnen schwachen Richtungen erhält, ist dafür plausibler als ein einziger komfortabler skalarer Mindestabstand. Ob eine solche Vergleichsmatrix erneuerbar ist, bleibt zu beweisen.

### Der Winkel ist ein Hilfsmittel

Bereits der [relative κ-Beweis, Abschnitt 5](https://github.com/Waschtl904/objekt-x-programm/blob/b1a734a0a6526ea17cbfce594d877974fd70cc01/research/x-c1/canonical-schur-coupling-2026-09-30/01-relative-kappa/PROOF.md) zeigt: Ein sehr kleiner gewöhnlicher Projektorabstand kann mit einem extrem kleinen relativen Schurrest zusammenfallen. Bei einer nahezu energielosen Richtung verstärkt die inverse Energie selbst winzige Beimischungen.

Die Grenze von 10° bleibt ein klar definiertes Diagnoseziel. Sie wird jedoch erst dann zur strategisch erforderlichen Schwelle, wenn ein Anschlusslemma daraus die tatsächlich benötigte Energie- oder Kopplungsgrenze ableitet. Ein solches Lemma kann auch einen viel kleineren Winkel, eine energiegewichtete Abweichung oder gar keine einzelne Eigenrichtung verlangen.

### Die aktuelle Geometrie wird teilweise rückblickend definiert

Die kanonischen Räume verwenden bisher positive Spektralprojektoren und die inverse Energie des bereits positiven neuen Terminals. Auch der [kritische Spektraltransport](https://github.com/Waschtl904/objekt-x-programm/blob/b1a734a0a6526ea17cbfce594d877974fd70cc01/research/x-c1/renewable-low-schur-spectral-2026-09-29/06-critical-spectral-transport/PROOF.md) benutzt die neue Positivität ausdrücklich.

Diese Konstruktionen sind für die Analyse der bewiesenen Kammern sinnvoll. Für einen vorwärts gerichteten Satz müssen die benötigten Räume und Abschätzungen zugänglich sein, bevor das Vorzeichen des neuen Terminals feststeht. Insbesondere kann ein Projektor auf `(0,τ)` eine eventuell negative neue Richtung nicht als kritische Richtung erfassen.

## Hauptuntersuchung zur konstruktiven Fortsetzung

### Räume ohne vorausgesetztes neues Vorzeichen wählen

Als erster Ansatz sollen vollständige physische Quellenkoordinaten verwendet werden: alter Kern, neue Profile und der vollständig kontrollierte hohe Anteil. Die bestehenden Quotienten- und Mellinkorrekturen sind dabei zu erhalten. Es darf keine dritte Momentbedingung entstehen.

Alternativ kommt ein unabhängig zertifizierter Spektralschnitt in Betracht, der **alle** Richtungen unter einer positiven Schwelle umfasst, einschließlich möglicher negativer und Nullrichtungen. Hierfür wären die Existenz, die Rangkontrolle und die Komplementgrenze eigenständig zu beweisen. Eine bloße Ersetzung des Intervalls im bisherigen Projektorsymbol genügt nicht; auch die bisherigen Transportbeweise müssten angepasst werden.

Für die erste Prüfung sind physische Koordinaten vorzuziehen: Ihre Definition hängt unmittelbar an den Quellen und nicht am gewünschten neuen Vorzeichen. Historische Core/Profile-Arbeiten liefern Vorarbeiten, beweisen aber noch keinen allgemeinen Fortsetzungssatz.

### Vollständige Blockdarstellung in einer verschobenen Formnorm

Eine konkrete, zunächst abstrakte Raumwahl folgt aus dem vorhandenen allgemeinen Wandgesetz. Fixiere alte und neue Horizonte `a<b≤L<∞`. Aus der gemeinsamen Rohform ist unabhängig von neuer Positivität eine Schranke

\[
|q_t[u]-\Gamma[u]|\le s_L\|u\|_2^2\qquad(t\le L)
\]

verfügbar. Wähle ein festes `ρ>s_L` für diesen gesamten Vergleich. Dann sind

\[
b_t^\rho(u,v)=q_t(u,v)+\rho\langle u,v\rangle_{L^2}
\]

vollständige Hilbertnormen auf den bereits definierten Formräumen F_t, äquivalent zur Gamma-Formnorm. Diese Hilfsnorm ist keine Gram-Realisierung der unverschobenen Weil-Form.

Die Nullfortsetzung `J:F_a→F_b` ist b^ρ-isometrisch. Ihr Bild ist deshalb abgeschlossen. Es gibt die exakte Zerlegung

\[
F_b=JF_a\oplus_{b_b^\rho}\mathcal N_{a,b},
\qquad\mathcal N_{a,b}=(JF_a)^{\perp_{b_b^\rho}}.
\]

Sie erfasst alle neuen Quellen. Das Komplement wird nicht als endlichdimensional angenommen. Seine Projektion hängt von der neuen verschobenen Form ab, deren Positivität bereits aus der unabhängigen Semibeschränktheit folgt. Sie verwendet keinen positiven Spektralprojektor der neuen unverschobenen Form.

q_b ist eine beschränkte hermitesche Form in dieser Hilbertnorm. Der Rieszoperator besitzt somit auf der vollständigen Zerlegung einen Blockoperator

\[
\mathcal Q_b=\begin{pmatrix}\mathsf A&\mathsf C\\\mathsf C^*&\mathsf D\end{pmatrix}.
\]

Der alte Block stellt genau q_a dar, weil die Formnaturality gilt. Aus dem alten vollständigen Boden `q_a≥c_a||·||²`, `c_a>0`, folgt

\[
\frac{c_a}{c_a+\rho}I\preceq\mathsf A\preceq I.
\]

Denn `b_a^ρ[u]≤(1+ρ/c_a)q_a[u]`, und `q_a[u]≤b_a^ρ[u]`. Damit ist der vollständige alte Block beschränkt invertierbar, ohne neue Gesamtpositivität zu verwenden. Die Residual- und Schurformeln gelten hier für beschränkte Operatoren auf den vollständigen Hilberträumen. Im Folgenden heißen diese Blöcke weiterhin A, C und D.

Die Orthogonalität liefert außerdem die konkrete Kreuzform

\[
q_b(Ju,v)=-\rho\langle Ju,v\rangle_{L^2}
\qquad(u\in F_a,\ v\in\mathcal N_{a,b}).
\]

**Gewonnen ist eine vollständige vorzeichenunabhängige Definition der Blöcke.** Noch nicht gewonnen sind berechenbare enge Einschließungen der Projektion und Kopplung oder die Positivität des Schurrests. Auch die b^ρ-orthogonale Wahl kann numerisch ungünstig sein. Eine explizite Core/Profile-Darstellung bleibt eine Alternative, sobald ihre vollständige Formraumidentifikation auf den neuen Übergängen begründet ist. Die historischen Kleinfenstersätze dürfen dafür nicht unverändert außerhalb ihres Scopes eingesetzt werden.

### Das erforderliche Lemma präzisieren

Nach einer gerechtfertigten Blockdarstellung sei

\[
\mathcal Q=\begin{pmatrix}A&C\\C^*&D\end{pmatrix},\qquad A\succ0.
\]

A steht hier für einen bereits positiv kontrollierten Block, nicht für den Horizontparameter. Die vollständige hohe Antwort muss in dieser Darstellung entweder erhalten oder mit einer bewiesenen Schranke eingeschlossen sein. Insbesondere darf eine vorherige Elimination nicht stillschweigend den alten positiven Block verändern, ohne diese Veränderung zu bezahlen.

In der vollständigen Operatorfassung sei P ein beschränkter Operator vom neuen in den alten Hilbertraum. Für eine solche unabhängig gewählte Näherung an die Lösung von `AP=C` definiere

\[
E=C-AP,\qquad
K=D-C^*P-P^*C+P^*AP.
\]

Dann gilt exakt

\[
\boxed{D-C^*A^{-1}C=K-E^*A^{-1}E.}
\]

Die Formel erfordert keine inverse neue Gesamtform. Sie nutzt nur A⁻¹. P darf numerisch vorgeschlagen werden; erst seine rationale Festlegung und das bezahlte Residuum E haben Beweiswert.

**Der konkrete Fortsetzungsgate lautet:** Aus zulässigen alten Zertifikaten und neuen Prim-/Gamma-Rohdaten sind eine positive Vergleichsmatrix W sowie Schranken

\[
E^*A^{-1}E\preceq\Gamma,
\qquad K\succeq\Gamma+\eta W,
\qquad W\succ0,\quad\eta>0
\]

herzuleiten. Auf einem unendlichen vollständigen Hilbertraum muss W dabei ein beschränkter koerziver Vergleichsoperator sein, also W≽wI mit w>0, wenn eine beschränkt invertierbare neue Terminalreserve benötigt wird. Nach einer begründeten endlichen Reduktion genügt eine positiv definite Vergleichsmatrix. Dann ist der vollständige neue Schurrest im jeweiligen Sinn positiv. Die Größe η darf vom Schritt abhängen und klein sein. W muss unabhängig spezifiziert sein; `W=neuer Schurrest` wäre keine hilfreiche Konstruktion.

Die Standardalgebra ist bereits eindeutig. **Die neue mathematische Arbeit besteht in der gemeinsamen Prim-/Gamma-Abschätzung für K und Γ sowie in ihrer erneuerbaren Form.** Bloßes Einsetzen einer bereits bewiesenen Zielpositivität würde diese Arbeit nicht leisten.

Gerade K enthält die entscheidenden Auslöschungen. Seine Beiträge sollen deshalb aus denselben Quellenvariablen gemeinsam aufgebaut werden, bevor Intervalle oder Normschranken eingesetzt werden. Vier unabhängig eingeschlossene Summanden könnten den bekannten Verlust gemeinsamer Abhängigkeiten erneut erzeugen. Die Genauigkeitsanforderung wird relativ zu W und der gewünschten Reserve η festgelegt.

GPT 1 konkretisiert dies durch die korrigierten Quellen `Ψ=V−JUP`, wobei JU die alten Quellen und V die neuen Profile beschreibt. Direkt gilt

\[
K=q_b(\Psi,\Psi),\qquad E=q_b(JU,\Psi).
\]

Die gemeinsame Mediatoridentität formuliert die benötigte Reserve somit als

\[
\|D_b\Psi y\|^2+\|A^{-1/2}Ey\|^2+\eta\langle y,Wy\rangle
\le\|T_b\Psi y\|^2.
\]

D_b bezeichnet hier den Defektreadout, nicht den unteren Diagonalblock D. Die Formeln gelten nur auf der gerechtfertigten vollständigen Darstellung; ein nicht erfasster hoher Anteil muss zusätzlich erhalten oder bezahlt werden.

Die Wahl von P verändert den exakten Schurrest **nicht**. Weil `K=S+E* A⁻¹ E`, verbessert eine Verringerung des Residuums für sich genommen nicht die wahre Reserve. Optimiert werden soll der nachgewiesene Abstand `K_−−Γ`, also die Qualität des gemeinsamen Zertifikats.

### Obere inverse Residualenergie aus alten Spektralbändern

Zuerst wird geprüft, ob vorhandene vollständige alte Resolventenschranken das benötigte Γ bereits liefern. Falls nicht, ist GPT 1s Bandvorschlag eine konkrete Verfeinerung. Er verwendet den alten positiven Block A in der festgelegten Hilbertdarstellung, nicht die inverse neue Gesamtform.

Für disjunkte Spektralbänder `I_j⊂[a_j,b_j]⊂(0,∞)` setze

\[
M_j=E^*\mathbf1_{I_j}(A)E,\quad
L_j=E^*A\mathbf1_{I_j}(A)E,\quad
Z_j=E^*A^{-1}\mathbf1_{I_j}(A)E.
\]

Die gemeinsame positive Momentblockbedingung liefert bei invertierbarem L_j eine **Untergrenze** `Z_j≽M_j L_j⁻¹ M_j`. Für den Schurabzug wird dagegen eine Obergrenze gebraucht. Diese folgt aus

\[
\frac{a+b-\lambda}{ab}-\frac1\lambda
=\frac{(\lambda-a)(b-\lambda)}{ab\lambda}\ge0
\quad(a\le\lambda\le b).
\]

Integration gegen das gemeinsame Spektralmaß ergibt

\[
Z_j\preceq\frac{(a_j+b_j)M_j-L_j}{a_jb_j}.
\]

Wenn die Bänder zusammen mit einem Rest oberhalb δ>0 das gesamte Residualspektrum abdecken, folgt

\[
E^*A^{-1}E\preceq
\Gamma_{\rm band}:=
\sum_j\frac{(a_j+b_j)M_j-L_j}{a_jb_j}
+\delta^{-1}M_{\rm rest}.
\]

Bandendpunkte, vollständige Abdeckung und alle Momenthüllen müssen unabhängig zertifiziert sein. Für die Auswertung wird eine obere Loewner-Schranke für M_j und eine untere für L_j benötigt, oder eine schärfere gemeinsame Einschließung ihrer Kombination. Eintragsweise Grenzen dürfen nicht ungeprüft als Matrixordnung verwendet werden.

Auf dem vollständigen neuen Komplement sind dies Operatorbedingungen; erst nach einer begründeten vollständigen Reduktion werden daraus endliche Matrizen. Die Bänder gehören außerdem zum gewählten alten Rieszoperator A. Bereits vorhandene Bänder des physischen Q_a oder einer anderen Normierung dürfen nur nach bewiesener Umrechnung übernommen werden.

Die skalare Identität und ihre Matrixfassung wurden zusätzlich mit exakten rationalen Beispielen kontrolliert. Es liegen dadurch noch keine berechneten Residualmomente für A8→A9 oder A9→A11 vor.

### Warum dies direkt Objekt X dient

Mit `S=D−C* A⁻¹ C` gilt

\[
\mathcal Q[(x,y)]
=\|A^{1/2}(x+A^{-1}Cy)\|^2+\|S^{1/2}y\|^2.
\]

Besitzt der alte Block bereits einen konstruierten Gram-Readout, kann dessen Darstellung anstelle der ersten abstrakten Quadratwurzel verwendet werden. Die Kreuzkopplung ist in `x+A⁻¹Cy` enthalten. Es werden keine einzelnen signierten Primkanäle zu positiven unabhängigen Blöcken erklärt.

Die Formel zeigt, welches geometrische Objekt ein erfolgreiches Fortsetzungslemma liefern würde: eine Erweiterung des alten Readouts um die kontrollierte neue Schurform. Sie ersetzt weder die Intrinsizitätsprüfung noch die Konsistenz bei unterschiedlichen Zerlegungen.

Für die bestehende C1a-Familie ist der Anschluss über die bereits bewiesene Transportformel vorzuziehen:

\[
X_A=\Delta_AT_A,\qquad
U^X_{A,B}=\Delta_BM^T_{A,B}\Delta_A^{-1},
\qquad\Delta_A=(I-R_A^*R_A)^{1/2}.
\]

Das Wandgesetz beweist Isometrie und Cocycle, sobald beide vollständigen Terminalreserven unabhängig vorliegen. Diese Kompatibilität soll wiederverwendet werden. Ein neuer Gramfaktor muss ihr durch ein nachgewiesenes Intertwining zugeordnet werden; eine Sammlung einzelner Choleskyfaktoren reicht dafür nicht.

Ein zusätzlicher Vorteil dieser Architektur ist bereits erkennbar: Sind solche Daten für eine gegen unendlich gehende Folge von Horizonten bewiesen, liefert das isometrische System den Hilbert-Direktlimes. Dafür müssen die einzelnen inversen Quadratwurzeln nicht eine gemeinsame Normschranke besitzen, und ein punktweiser Grenzwert ihrer Fourierdarstellungen ist nicht erforderlich. Die exakten isometrischen Übergänge übernehmen die Identifikation. Offen bleiben die positive Folge selbst und die Rückbindung ihrer Quellenunion an die vollständige geeignete Testklasse.

Strikte Positivität ist hier die praktische Voraussetzung der vorhandenen invertierbaren Transportformel. Die Objekt-X-Definition verlangt grundsätzlich eine positive semidefinite Gram-Form und erlaubt damit einen Kern. Falls künftig nur Semidefinitheit erreichbar ist, muss der Übergang über die expliziten Readout-Bilder und gegebenenfalls deren Abschluss neu begründet werden. Das Scheitern einer strikten Reserve wäre nicht automatisch ein Ausschluss von Objekt X.

### An den bekannten Übergängen prüfen

Die erste Anwendung erfolgt auf A8→A9 und A9→A11 in beiden Paritäten. Dafür wird vorab eine Liste zulässiger Eingaben erstellt.

**Zulässig** sind die alte Positivität, die gemeinsame analytische Form, vorzeichenunabhängig gewonnene neue Matrixintervalle, Mellindaten, vollständige hohe Schranken und exakt gebundene Fehlerbudgets.

**Als Begründung der neuen Positivität unzulässig** sind deren bisheriger positiver Terminalboden, die daraus abgeleitete positive inverse Gesamtform, allein auf neuer Positivität beruhende Cauchy–Schwarz-Schätzungen und entsprechende positive Projektor- oder κ-Aussagen. Auch indirekte Abhängigkeiten in gespeicherten Eingabedateien sind zu prüfen.

Die bekannten Zielzertifikate bleiben anschließend Vergleichsmaßstab. Dieser Rücktest ist kein vollständig unbeeinflusster Blindversuch: Wir kennen seine Ergebnisse. Er prüft, ob die vorgeschlagene Begründung logisch ohne die Zielpositivität auskommt.

**Erfolg:** dieselbe ausdrücklich formulierte Abschätzungsregel liefert in beiden Übergängen einen positiven vollständigen Schurrest und eine nachvollziehbare Readout-Erweiterung. Eine wiederverwendbare Regel darf Daten und Dimension des jeweiligen Übergangs verwenden; sie darf nicht für jeden Fall einen anderen unbegründeten Mechanismus erfinden.

**Nicht ausreichend:** dieselben Zielmatrizen erneut positiv zu faktorisieren, ohne eine neue Fortsetzungsabschätzung oder einen erkennbar wiederverwendbaren Zusammenhang zu gewinnen.

**Falls der Test scheitert:** Festhalten, ob die Raumwahl, die Kopplung, die relative Fehlergröße oder die unendliche Antwort den Nachweis verhindert. Nur ein genau benannter mathematischer Grund rechtfertigt eine Änderung des Ansatzes.

## Begrenzte Untersuchung der gemeinsamen Matrixbedingungen

Die lokalen Drei-Cut-Ergebnisse schließen eine größere Suche mit denselben drei skalaren Bedingungen als Lösung ihres definierten Problems aus. Der neue Zeuge besteht alle drei Cuts und wird von einer anderen gemischten H₀-Richtung ausgeschlossen. Das begründet eine gemeinsame Behandlung von Matrixbedingungen. Es beweist nicht, dass H₀ allein Root entscheidet. [Gebundener Grenznachweis](../research/x-c1/canonical-h0-followups-2026-10-03/reports/three_cut/REPORT.md)

Wenn eine nachgewiesene Verbindung zum Fortsetzungsresiduum E oder zu K diese Untersuchung rechtfertigt, soll der Diagnosetest die ursprünglichen Variablen gemeinsam erhalten:

\[
Y_LX+Y_R=0,
\qquad (G_B+L_B/17)C_T=Y^*,
\qquad H_0=G_A-C_T^*G_BC_T\succeq0.
\]

Der spätere übermittelte Bericht von GPT 1 gibt einen exakten Grenznachweis auch für den gesamten Hauptblock (4,5) an. Dieser isolierte Zwischentest wird deshalb nicht begonnen; der neue Zahlenbeleg ist hier noch nicht unabhängig reproduziert. Gegenstand eines begründeten weiteren Tests wäre die vollständige H₀-Bedingung. Hinzu kommen die vorhandenen gemeinsamen Momentbedingungen und die definite Struktur des symmetrischen Eigenwertproblems. Höhere Reste werden an ihre Erzeugergleichungen gebunden, soweit rigoros möglich. Eine konkrete Verbindung des bisherigen H₀-Systems zu E oder K ist bisher nicht nachgewiesen.

Diese Bedingungen enthalten Produkte und sind im Allgemeinen kein einfaches lineares semidefinites Programm. Ein SDP kann eine äußere Relaxation oder ein Hilfsmittel zur Zertifikatssuche liefern. Seine numerische Ausgabe allein ist kein Beweis für die ursprüngliche Familie.

Die Kontrollen umfassen die beiden bekannten unzulässigen Zeugen, die fünf bekannten vollständigen zulässigen Modellpunkte und die bisherigen 19 Domänen. Die fünf Punkte werden nicht als fünf unabhängig rekonstruierte ursprüngliche Operatoren ausgegeben. Die acht Diagnoseboxen bleiben eine unvollständige Auswahl.

### Bandmomente ohne vorherige Richtungslokalisierung

Für eine feste Basis V der tatsächlichen zweidimensionalen Ergänzung und ein Spektralband I im bereits positiven bekannten Terminal lassen sich gemeinsam betrachten:

\[
M_I=V^*\mathbf1_I(Q_B)V,\quad
E_I=V^*Q_B\mathbf1_I(Q_B)V,\quad
Z_I=V^*Q_B^{-1}\mathbf1_I(Q_B)V.
\]

Diese Matrizen beschreiben das ganze E. Ihre Definition verlangt keine vorherige Auswahl des maximierenden Vektors. Aus dem gemeinsamen Spektralmaß folgt

\[
\begin{pmatrix}E_I&M_I\\M_I&Z_I\end{pmatrix}\succeq0.
\]

Für `I⊂[a,b]` mit `0<a≤b` gelten außerdem

\[
aM_I\preceq E_I\preceq bM_I,
\qquad b^{-1}M_I\preceq Z_I\preceq a^{-1}M_I.
\]

Bei vollständiger Bandzerlegung summieren sie sich zu G, L und Z. Damit lassen sich Fragen zu allen Richtungen formulieren, bevor eine einzelne Richtung eng lokalisiert ist. Ein endlicher Satz solcher Bedingungen ist zunächst nur notwendig; er beweist keine vollständige Realisierbarkeit durch das ursprüngliche Spektralmaß.

**Wichtig:** Die benötigten scharfen Bandmatrizen sind dadurch noch nicht berechnet. Z_I und die kanonische Ergänzung verwenden hier die bekannte Terminalpositivität. Sie dienen der Diagnose und dürfen nicht unverändert als unabhängige Vorwärtsdaten für einen neuen Terminal auftreten.

### Abnahme und Ende dieses Diagnosetests

Vor einer größeren Rechnung wird genau festgelegt, welche Energie-, Moment- oder Residualschranke die Hauptuntersuchung benötigt. Die Matrixrechnung soll diese Schwelle zertifizieren oder zeigen, welche zusätzliche Information fehlt.

Das Ausschließen der beiden bekannten Gegenzeugen ist ein notwendiger Kontrolltest, aber noch kein Erfolgsnachweis. Auch eine kleine Verbesserung einer Winkelzahl genügt nicht allein.

Für die erste Untersuchung bleiben die Eingabedaten fest. Es gibt keine offene Folge immer neuer Einzelcuts oder adaptiver Bäume. Nach einer vorab begrenzten Implementierungs- und Prüfphase wird entschieden:

- Die benötigte Schranke ist bewiesen: in das Anschlusslemma übernehmen.
- Ein exakter Zeuge besteht die verstärkte Relaxation: deren Aussagegrenze dokumentieren und die genau fehlende Bindung benennen.
- Die Auswertung bleibt unentschieden: keine mathematische Unmöglichkeit behaupten; weitere Rechenarbeit nur bei einer konkreten neuen Informationserwartung.

Neue Operatorinformationen sind später zulässig, wenn vorher feststeht, welcher Eintrag oder welches Moment in welcher Genauigkeit die entscheidende Schranke verbessert. So wird auch eine neue Y58- oder L_B-Rechnung zu einer begründeten Messaufgabe.

## Reihenfolge der nächsten Entscheidungen

| Etappe | Prüffrage | Konkretes Ergebnis |
| --- | --- | --- |
| 1 | Welche vorhandenen Formeln setzen die neue Positivität schon voraus? | Eingabeliste für einen vorwärts gerichteten Beweis, einschließlich indirekter Abhängigkeiten. |
| 2 | Welche signunabhängige Blockdarstellung erlaubt die Schurformel mit altem positiven A? | Exakte Darstellung mit vollständigem Tail und ausdrücklich benannten neuen Ungleichungen. |
| 3 | Funktioniert dieselbe Regel bei A8→A9 und A9→A11? | Positiver, unabhängig begründeter Schurrest oder präzise lokalisierter Fehlversuch. |
| 4 | Hilft die gemeinsame H₀-/Momentgeometrie bei genau dieser Ungleichung? | Begrenzter Diagnosetest mit vorher benannter benötigter Schranke. |
| 5 | Besteht der festgelegte Kandidat einen zusätzlichen Übergang? | Erst jetzt prospektiver A11→A13-Test mit eingefrorener Aussage und Fehlerbudget. |
| 6 | Lassen sich die Voraussetzungen der Regel für eine unbeschränkte Horizontfolge beweisen? | Ein echter Erneuerungssatz oder ein genau benanntes Hindernis der vorgeschlagenen Regel. |

Die Etappen 2 und 4 können sich inhaltlich ergänzen. Die Hauptuntersuchung wartet nicht automatisch auf ein Winkelzertifikat. A13 ist zunächst ein zusätzlicher Test der formulierten Regel; sein erfolgreicher Einzelnachweis wäre noch kein allgemeiner Satz. PR #187 wird durch diese Strategie nicht verändert.

Für die unbeschränkte Fortsetzung muss zusätzlich bewiesen werden, dass die gewählten Horizonte tatsächlich gegen unendlich gehen. Ein überall positiver lokaler Schritt kann sich zu einer endlichen Gesamtweite summieren. Eine einheitliche positive Reserve ist nicht erforderlich; eine bloße Folge von jeweils erfolgreich ausgeführten Einzelrechnungen ersetzt keinen Satz für alle weiteren Schritte.

Die Anzahl kritischer Richtungen darf wachsen. Die beobachteten Ränge 5→6→8 und die Ergänzungsdimensionen 1 beziehungsweise 2 sind keine globale Dimensionsannahme. Auch der Shift 17 darf außerhalb seines bewiesenen Horizonts nicht unverändert vorausgesetzt werden; das allgemeine Wandgesetz verwendet horizontabhängige Hilbertnormen.

## Wann ein anderer Konstruktionsansatz sinnvoll wird

Die jetzige C1a-Familie bleibt der erste Ansatz, weil sie konkrete Readouts, Defekte, Quellenbindungen und Transporte besitzt. Wenn die vorwärts gerichtete Untersuchung keine erneuerbare Ungleichung erkennen lässt, sollte eine klar abgegrenzte alternative Konstruktion hinzukommen.

Eine Alternative muss vor einer großen Rechnung mindestens angeben:

- aus welchen arithmetisch-analytischen Daten der gemeinsame Träger und Readout entstehen;
- welche neue Identität oder Ungleichung gegenüber C1a gewonnen wird;
- weshalb die bekannten Ausschlüsse kurzer Reichweite plus endlichen Ranges sowie isolierter positiver Primblöcke nicht greifen;
- welche bislang schwierige Abschätzung sie verbessert, ohne deren Ergebnis vorauszusetzen.

Eine reine Umformulierung als positiver Kern, Faktorisierung oder Operatorerweiterung leistet dies noch nicht. Die klassische Theorie von [Baidiuk und Hassi](https://arxiv.org/abs/1403.5133) liefert passende Werkzeuge für Blockoperatoren, Schurkomplemente und Faktorisierungen. Sie liefert nicht automatisch die arithmetische Positivitätsbedingung unseres konkreten Operators.

Für einen gezielten Vergleich bietet [Suzukis Darstellung über die Schraubenfunktion](https://arxiv.org/html/2606.09096v1) eine andere Beschreibung der Weil-Form durch kontinuierliche Kerne. Zu prüfen wäre eine genaue Abbildung zwischen dieser Darstellung und unseren Zwei-Mellin-Quellen sowie eine dadurch tatsächlich stärkere lokale Abschätzung. Die globale Grenzbehauptung dort ist offen; der heuristische globale Teil arbeitet unter RH. Beides darf nicht als unabhängige positive Konstruktion übernommen werden.

Der [Preprint von Zhu, Version 2](https://arxiv.org/html/2608.24827v2) behandelt zertifizierte Fensterpositivität und sehr kleine variationale Reserven. Er ist ein sinnvoller Vergleich für Normierung, Testklasse und numerische Konditionierung. Seine beobachteten Abfallmuster sind kein bewiesenes Erneuerungsgesetz unseres Programms; allgemeine asymptotische Aussagen haben dort teilweise zusätzliche Voraussetzungen. Eine universelle Schranke für sämtliche Objekt-X-Ansätze wird daraus nicht abgeleitet.

Eine Alternative erhält Vorrang, wenn sie eine überprüfbar neue Ungleichung oder eine einfachere exakte gemeinsame Geometrie liefert. Eine neue Bezeichnung für denselben offenen Positivitätsschritt genügt dafür nicht.

## Überprüfung der Grundlage

Die A11-Kette bleibt der Ausgangspunkt. Eine unabhängige Prüfung ihrer Verbindung von Originalform, Mellinbedingungen, Integralaufbau, Matrixintervallen, hoher Antwort und Normrückrechnung ist sinnvoll. Sie begleitet die Konstruktionsarbeit und konzentriert sich auf tatsächlich verwendete Abhängigkeiten.

Bereits abgeschlossene Großrechnungen werden bei konkretem Prüfbedarf wiederholt. Weitere bytegleiche Replays derselben Eingaben können die Reproduzierbarkeit bestätigen, schließen aber keine neue analytische Lücke. Zustimmung mehrerer KI-Systeme ist kein Ersatz für eine fachliche Prüfung dieser Kette.

## Mathematischer Anhang zu den vorgeschlagenen Tests

### Beweis der Residualformel

Im endlichen hermiteschen Fall mit A≻0 gilt für

\[
R=\begin{pmatrix}I&-P\\0&I\end{pmatrix}
\]

die exakte Kongruenz

\[
R^*\mathcal Q R=\begin{pmatrix}A&E\\E^*&K\end{pmatrix}.
\]

Aus `E=C−AP` folgt durch Ausmultiplizieren

\[
E^*A^{-1}E=C^*A^{-1}C-C^*P-P^*C+P^*AP.
\]

Die Differenz mit K ergibt die angegebene Formel. Der übliche Schurkomplementsatz liefert anschließend Positivität, falls `K−Γ≽ηW≻0` und `E* A⁻¹ E≼Γ` bewiesen sind. Für unbeschränkte Formen müssen Domänen, die Wirkung der Kopplung und die erforderlichen Stetigkeits- beziehungsweise Faktorisierungsannahmen zusätzlich begründet werden. Dieser endliche Beweis überspringt diesen Übergang nicht.

### Warum alter Boden und positiver hoher Anteil nicht genügen

Die reellen Matrizen

\[
Q_t=\begin{pmatrix}1&2&0\\2&4+t&0\\0&0&2\end{pmatrix}
\]

haben dieselbe positive alte Einschränkung auf der ersten Koordinate, dieselbe alte/neue Kreuzkopplung und denselben positiven hohen Block auf der dritten Koordinate. Ihr neuer Schurrest ist t. Bei `t=1/10` ist Q_t positiv; bei `t=−1/10` besitzt sie eine negative Richtung.

Dieses Beispiel konkretisiert die bereits im Wandgesetz benannte logische Lücke. Es ist kein Modell oder Gegenbeispiel der ursprünglichen Weil-Form. Für den gewünschten Vorwärtssatz wird eine zusätzliche Eigenschaft der tatsächlichen Prim-/Gamma-Daten benötigt.

### Beweis der gemeinsamen Momentbedingung

Sei `dΣ(λ)=V* dP(λ)V` das positive matrixwertige Spektralmaß des bekannten positiven Terminals. Für beliebige Koeffizientenvektoren x und y ist

\[
\begin{aligned}
\binom{x}{y}^*
\begin{pmatrix}E_I&M_I\\M_I&Z_I\end{pmatrix}
\binom{x}{y}
&=\int_I(\sqrt\lambda x+\lambda^{-1/2}y)^*
\,d\Sigma(\lambda)\,
(\sqrt\lambda x+\lambda^{-1/2}y)\\
&\ge0.
\end{aligned}
\]

Die Bandgrenzen folgen aus den skalaren Ungleichungen für λ auf `[a,b]` durch Integration gegen dieses Maß. Die Formel ist eine allgemeine Gram-Identität, keine neue Spektralberechnung für Root.

### Ausgeführte Kontrollen

Die Residual- und Kongruenzformeln wurden zusätzlich in sechs nichttrivialen rationalen Matrixfällen exakt kontrolliert, einschließlich positiver und negativer Schurreste. Das Beispiel Q_t wurde in beiden Vorzeichen geprüft. Eine gemeinsame Momentmatrix wurde aus einem rationalen diskreten Spektralmaß auf zwei Koordinaten rekonstruiert und ihre Block-Gram-Identität exakt verglichen. Alle Kontrollen bestanden.

Die allgemeinen Begründungen stehen oben; endliche Beispiele ersetzen sie nicht. Es wurden in dieser Strategiearbeit keine neuen Operatorintegrale, keine neuen Root-Zertifikate und keine A13-Rechnung ausgeführt. Die damalige lokale Erarbeitung änderte weder GitHub noch das mathematische Register. Die anschließende Integration dokumentiert die Projektpriorität in `AGENTS.md` und die operative Reihenfolge in [NEXT_GATES](NEXT_GATES.md). Die mathematischen Aussagegrenzen bleiben bestehen.

## Ursprüngliche Empfehlung vom 3. Oktober 2026

**Vorwärts gerichtete Schurfortsetzung aus alten positiven Quellen und neuen gemeinsamen Prim-/Gamma-Daten.**

Der erste Arbeitsauftrag ist, für A8→A9 und A9→A11 die zulässigen Eingaben zu bestimmen und eine vorzeichenunabhängige vollständige Blockdarstellung aufzubauen. Anschließend wird die Residualformel auf genau die dabei fehlende relative Abschätzung zugeschnitten. Erst diese Abschätzung legt fest, ob wir bandweise Momentmatrizen, eine engere Richtung, bestimmte neue Operatorinformationen oder eine andere Raumwahl benötigen.

Das würde die Arbeit unmittelbar auf die Konstruktion von Objekt X ausrichten: Jede erfolgreiche Abschätzung soll einen klar benannten Teil seines Readouts oder seiner kompatiblen Erweiterung liefern.
