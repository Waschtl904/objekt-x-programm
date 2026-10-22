# Objekt-X-Programm

Ein offenes, KI-gestütztes mathematisches Forschungsjournal zur Konstruktion von Objekt X.

**Objekt X ist das Ziel einer noch unvollständigen Konstruktion:** Gesucht wird
eine kompatible positive Geometrie, welche die relevante Weil-Form exakt
darstellt. Das Programm untersucht dazu gemeinsame Prim-/Gamma-Operatoren,
endliche positive Kammern und deren Fortsetzung.

**Objekt X hat Vorrang.** Erst nach seiner erfolgreichen Konstruktion wird der
mögliche Anschluss an die Riemannsche Vermutung verfolgt. Die Anforderungen
an X, einschließlich der vollständigen geeigneten Testklasse, bleiben erhalten.

**Ein Beweis der Riemannschen Hypothese liegt nicht vor.** Globale
Weil-Positivität und die vollständige Konstruktion von Objekt X bleiben offen.
Die projektintern hergeleiteten Ergebnisse sind zur externen Prüfung offen.

## Einstieg

| Ich möchte … | Einstieg |
| --- | --- |
| Idee, Entwicklung und Grenzen verstehen | [Gesamtüberblick](00-uebersicht/OBJEKT_X_GESAMTUEBERBLICK.md) |
| Die weitere Forschungsrichtung verstehen | [Strategie für Objekt X](00-uebersicht/OBJEKT_X_FORSCHUNGSSTRATEGIE.md) |
| Das Projekt kritisch begutachten | [Leitfaden für externe Begutachtung](00-uebersicht/EXTERNE_BEGUTACHTUNG.md) |
| Den integrierten Stand und offene Aufgaben prüfen | [Aktueller Stand](00-uebersicht/CURRENT_STATE.md) · [Nächste Aufgaben](00-uebersicht/NEXT_GATES.md) |
| Einen konkreten Satz und seine Belege finden | [Ergebnisregister](00-uebersicht/SURVIVOR_REGISTRY.md) |
| Dateien, Manuskripte oder ältere Ansätze einordnen | [Dokumentationswegweiser](00-uebersicht/DOKUMENTATIONSWEGWEISER.md) |

## Forschungsstand in Kürze

Die folgende Zusammenfassung bezieht sich auf den integrierten Forschungsstand
und die Folgepakete bis **20. Oktober 2026**. Den operativen Status, die genauen Voraussetzungen und
die gepinnten Beweisanker verwaltet das
[Forschungsregister](00-uebersicht/RESEARCH_STATE.yaml).

| Bereich | Dokumentierter Stand | Aussagegrenze |
| --- | --- | --- |
| Endliche positive Geometrie | Drei positive Kammern bis $A_{11}=\log(11)/2$, mit kompatiblen Transporten | Kein Positivitätssatz für beliebig große Horizonte |
| Hoher und niedriger Schuranteil | Vollständige Reduktion auf einen endlichen kritischen Rest für jeden festen endlichen Horizont | Die Positivität dieses Rests muss jeweils begründet werden |
| Kanonische Richtung für A9→A11 | Maximaler Schur-Eigenwert in beiden Paritäten einfach; gerade Richtung lokalisiert | Ungerade ist die gesamte Ausgangsfamilie weiterhin `UNRESOLVED` |
| Ungerade Winkeldiagnose | Gemeinsamer Y-Kernel: central ≤2.933357°, quarter ≤3.070163°, half ≤3.642693°; Endpunktfolge: five_eighths ≤4.933780° | Bedingte Schnitte; Root bleibt `UNRESOLVED` |
| H₀-Folgeuntersuchung | Exaktes Hindernis für die benannte letzte Drei-Cut-Relaxation | Kein ursprünglicher Operatorgegenzeuge; vollständiges H₀ unentschieden |
| Konstruktiver Anschluss A8→A9 | [Bedingter globaler Schurabschluss](research/x-c1/a8-a9-global-closure-2026-10-13/README.md): vollständiger Formdualrest und positiver Anschluss auf dem ganzen neuen Raum | Gebundene Operator-, Domänen- und Raumzerlegungsvoraussetzungen; weitere konstruktive Übergänge und allgemeine Fortsetzung offen; der ursprüngliche Tail ist inzwischen bedingt geschlossen |
| A9-Inverserneuerung | [Gemeinsame A9-Inversmajorante und Boden 2/3 W_X](research/x-c1/a9-inverse-renewal-2026-10-13/README.md) auf dem ganzen neuen hohen Schurrest nach Basis84-Elimination | Wiederverwendbarer bedingter Baustein; der nachfolgende feste W9-Vergleich scheitert, andere zulässige Vergleiche bleiben offen |
| Ursprünglicher Basis84-Tail | [Komplementwechsel und Gegenprüfung](research/x-c1/basis84-tail-closure-2026-10-14/README.md): tau auf Z84 mindestens 2/3 W_X; Restriktionsinverse höchstens 3/2 I; Ziel 1/20 geschlossen | Bedingt auf die gebundenen Voraussetzungen; kein Boden 2/3 auf ganz A9; ersetzt keine neue vollständige Residualbilanz |
| Gerichtete Skalartests | [Konstante Schalenrichtung z0](research/x-c1/l00-z0-directed-interval-2026-10-17/PROOF.md) und [fester gerader Kandidat](research/x-c1/coherent-k-frozen-even-2026-10-17/PROOF.md) liefern keinen Ausschluss | Keine Bestätigung der Antwortregel; die weitere Richtungssuche blieb ohne qualifizierten Kandidaten |
| Fester K*-Untervergleich | [Gerichtete Formfehlerschärfung](research/x-c1/w9-schur-form-error-even-2026-10-19/PROOF.md) schließt jeden W >= Q_lower,*^-1 beim festen geraden Zeugen, der eingefrorenen Antwortregel und ihrem Budget aus | Andere Unterformen, Antwortregeln und Majoranten der tatsächlichen A9-Inverse bleiben offen; keine negative Weil-Richtung und kein Abschluss von Punkt 4 |
| Globales Ziel | Arbeitsdefinition und erforderliche Übergänge sind formuliert | Kofinale positive Familie, globaler Readout, vollständige Weil-Gramidentität und RH bleiben offen |

Die hier zusammengefassten projektinternen Ergebnisse tragen den Status
`AUTHOR_DERIVED` beziehungsweise für die benannten Ausschlüsse
`AUTHOR_DERIVED_NO_GO`, jeweils mit `EXTERNAL_REVIEW_OPEN`. Das bedeutet: projektintern hergeleitet,
mit angegebenen Beweisen und Zertifikaten; die unabhängige externe Prüfung ist
offen. Ein erfolgreicher Rechenlauf bestätigt seinen ausgewiesenen Prüfumfang.

Aktuelle Arbeit außerhalb von `main` ist in den
[offenen Pull Requests](https://github.com/Waschtl904/objekt-x-programm/pulls)
sichtbar. Für ein Urteil über einen solchen Vorschlag sind dessen eigener
Commit, Belegumfang und Integrationsstatus anzugeben.
`PENDING_STATUS_REVIEW` im Register bezeichnet eine ausstehende fachliche
Statuseinordnung und kann auch für bereits integrierte Pakete gelten.
Merge, Statuseinordnung und unabhängige externe Prüfung sind getrennte Schritte.

## Neuer Vergleich vom 21. Oktober: fester gerader Zeuge besteht

Der [restzentrierte Kontrollweg](research/x-c1/w9-residual-centered-control-even-2026-10-21/PROOF.md)
liefert unter gebundenen Voraussetzungen eine vollständige obere Energie
<53.950924907669e-6 bei einer Budgetuntergrenze >54.117169360708e-6.
Die ganze gemeinsame Restfunktion, Rand- und Modellfehler sind enthalten.
Das ist ein lokaler Fortschritt gegenüber den beiden Hindernissen aus #250.
Die äußere Antwortregel und der Zeuge bleiben unverändert. Der gesamte
Grad-11-Raum, beide Paritäten, Punkt 4 und externe Prüfung bleiben offen.
Das Paket ist durch [PR #252](https://github.com/Waschtl904/objekt-x-programm/pull/252)
auf `main` integriert (Merge `4ede0b70e2df1f133c762d7b0e6527338d597874`).
Der Merge ändert weder den mathematischen Status noch den externen Prüfstatus.
Der genaue
[Reproduktionsstatus](research/x-c1/w9-residual-centered-control-even-2026-10-21/ACCEPTANCE.json)
und die früheren Ausschlussresultate bleiben getrennt.

## Bilanz vom 20. Oktober: Kontrollweg beendet, neue Unterform offen

Die Kette **#245–#250** ist als begrenzte Untersuchung abgeschlossen.
Der vorgeschlagene obere Kontrollweg wird **vorerst nicht weiterverfolgt**.
Die neue Unterform selbst bleibt mathematisch offen. Diese Konsolidierung
startet keinen weiteren Rechenauftrag und behauptet keine Main-Integration.

| Abgeschlossen unter den gebundenen Voraussetzungen | Weiter offen |
| --- | --- |
| Neue Unterform ausgewählt; Teilpass und anschließender Ausschluss des festen Gesamtvergleichs (#245–#247) | Erfolgreicher vollständiger Vergleich mit der neuen Unterform |
| Feste Young-Gewichtsfamilie ausgeschlossen (#248) | Andere zulässige Vergleiche und die tatsächliche vollständige Inversenergie |
| Positiver eta-q-Zusatz ausgewertet und bei unveränderten übrigen Grenzen zu klein (#249) | Gesamter variationaler Rest |
| Vorgeschlagener oberer Kontrollweg ungeeignet (#250) | Gemeinsamer Restnachweis, der mögliche Aufhebungen erhält |

Die [Machbarkeitsprüfung #250](research/x-c1/w9-rest-feasibility-even-2026-10-20/PROOF.md)
weist **zwei eigenständige Hindernisse** aus:

1. Die obere F-Einschließung liegt mit etwa 54.475251e-6 bereits ohne
   Restenergie über der Budgetuntergrenze von etwa 54.117169e-6.
2. Der vorhandene E-Transport ist selbst bei optimalen exakten
   Darstellungskoeffizienten unbrauchbar teuer. Seine kleinste gewichtete
   Koeffizientenenergie liegt bei etwa 5.78e40. Das ist ein Preis dieser
   Majorante, keine untere Schranke der tatsächlichen Restenergie.

Ein besserer Formboden oder andere Koeffizienten retten diesen Kontrollweg
nicht. Eine engere D/U-Fehlergrenze würde zunächst nur das erste Hindernis
bearbeiten. Vor einer Wiederaufnahme braucht es eine konkrete gemeinsame
Herleitung mit quantitativer Aussicht sowohl für die F-Hülle als auch für
das vollständige Residuum samt seinen Aufhebungen. Höhere Präzision allein
begründet keinen neuen Lauf.

Die [gemeinsame Checkliste und Belegkette](00-uebersicht/OBJEKT_X_FORSCHUNGSSTRATEGIE.md#konsolidierung-vom-20-oktober-kontrollweg-beendet-methodenentscheidung-offen)
hält Ergebnisse, Wiederverwendung und Wiederaufnahmebedingungen zusammen.
Die bisherigen Beweis- und Abnahmeanker bleiben erhalten.
**Punkt 4, N12 und externe Prüfung bleiben offen.**
`AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN` wird durch diese Dokumentation
nicht geändert. Die abgeschlossenen Prüfaufgaben sind keine Aufwandsquote
und kein Scheitern von Objekt X.

## Arbeitsbilanz und Integration vom 19. Oktober

Die Forschungskette #232–#239 ist über [PR #241](https://github.com/Waschtl904/objekt-x-programm/pull/241)
zusammengeführt und nach Main übernommen.
Die korrigierten Eingabelader aus #231 bleiben erhalten.
Der [Integrationsnachweis](00-uebersicht/integrationsnachweise/PR241_2026-10-19.md)
trennt übernommene große Integrationen, gezielte Replays und die technische
Reparatur einer historischen Quelltextbindung. Die vorhandene Registerpflege
aus #240 bildet die Grundlage der aktuellen Variantenbilanz.

Die gemeinsamen Quellen, Paarungen und Fehlergrame bleiben wiederverwendbar.
Für dieselbe ausgeschlossene K*-Unterform mit derselben Antwortregel und
demselben Budget werden keine weiteren Obermajorantenverfeinerungen oder
RL-Rechnungen zur Rettung dieses Vergleichs verfolgt. Ein neuer Ansatz muss
die geänderte Ausschlussvoraussetzung, übernommene Daten und eine quantitative
Begründung für einen begrenzten Test benennen. Die Auswahl eines solchen
Ansatzes ist offen; diese Integration startet keine neue Großrechnung.

Die vorhandene endliche A11-Positivität unter ihren Voraussetzungen ist ein bekannter Prüffall.
Die aktuelle Aufgabe verlangt einen konstruktiven A9→A11-Anschluss, der sie
nicht voraussetzt und seine vollständigen Zertifikate erneuert. Daher bleiben
Punkt 4, N12, allgemeine Fortsetzung und Objekt X offen. Erledigte
Arbeitspakete sind keine Prozentangabe für den fertigen Beweis.

## Tailabschluss vom 14. Oktober

Die [beiden Tailpakete](research/x-c1/basis84-tail-closure-2026-10-14/README.md) sind gemeinsam integriert und auf GitHub
mit vollständigem rationalem Paket-Replay nachgeprüft. Die großen globalen
Integrationen wurden übernommen. Unter den gebundenen Voraussetzungen schließt
der Komplementwechsel den ursprünglichen Basis84-Tail mit Boden 2/3 W_X;
für seine Restriktionsinverse gilt höchstens 3/2 I.
Für spätere vollständige Hilbertresiduen auf diesem Rest ist damit der Faktor
3/2 statt 20 verfügbar. Der frühere offene Tailstatus ist durch diesen neuen
Beweisanschluss überholt. Neue Residualgrame, weitere Horizonte und externe
Gesamtbegutachtung bleiben offen.
[Integrations- und Prüfbelege](00-uebersicht/integrationsnachweise/PR221_2026-10-14.md).

## Vorangehender Integrationsstand vom 14. Oktober

Die [Domänen- und Fortsetzungsherleitung](research/x-c1/a9-domain-continuation-2026-10-13/README.md)
und die [A9-Inverserneuerung](research/x-c1/a9-inverse-renewal-2026-10-13/README.md)
sind mit Originalarchiven, Quellenabgleich und automatischen Replays integriert.
Der ganze neue hohe Schurrest hat nach Aufnahme der 84 Antwortfunktionen
mindestens 2/3 W_X. Die gemeinsame A9-Inversmajorante liefert eine konkrete
Ausgangsbasis für neue Kräfte; deren vollständige Integrale bleiben zu berechnen.
Die gesonderte lokale Fortsetzungsbreite ist praktisch unbrauchbar klein und
kein A9→A11-Schritt. Externe Begutachtung und die globalen Aufgaben bleiben offen.
[Paketinventar und Integrationsbelege](00-uebersicht/integrationsnachweise/A9_PAKETABGLEICH_2026-10-14.md)
zeigen, wo die damals 18 lokal versiegelten Ausgangspakete erhalten sind.
Die beiden neuen Tailarchive sind im obigen Nachtrag zusätzlich gebunden.

## Integrationsstand vom 13. Oktober

Der [bedingte globale Schurabschluss A8→A9](research/x-c1/a8-a9-global-closure-2026-10-13/README.md)
führt die Arbeiten seit dem 7. Oktober einschließlich aller Originalpakete,
Gegenprüfungen und verworfenen Hilfsschranken zusammen. Unter den gebundenen
Operator-, Domänen- und vollständigen Raumzerlegungsvoraussetzungen ist der
Positivitätsübergang geschlossen. Der gesamte Formdualrest kostet weniger als
0,3954 % bzw. 0,6967 % seines Matrixbudgets. Der damals noch offene Tailboden
1/20 ist durch den Nachtrag vom 14. Oktober bedingt geschlossen. Weitere Horizonte
und Objekt X bleiben offen. [PR #216 und seine Prüfbelege](00-uebersicht/integrationsnachweise/PR216_2026-10-13.md)
binden den tatsächlichen Forschungshead, Mergecommit und die erfolgreiche Main-CI.
Externe Begutachtung bleibt offen.

## Mathematischer Ansatz

Ausgangspunkt ist die physische finite Weil-Form. Ein gemeinsamer
Prim-/Gamma-Mediator trennt sie in einen positiven Anteil und einen Defekt.
Eine vollständige Schurreduktion macht den niedrigen Rest zum entscheidenden
Positivitätsproblem. Bisherige endliche Kammern liefern Bausteine für eine
Fortsetzung; ein allgemeiner Mechanismus zur Erneuerung ihrer positiven
Reserve fehlt noch.

```text
Finite Weil-Form → gemeinsamer Mediator → Defekt- und Schurreduktion
                → positive Kammern bis A11
                → [offen] positive Fortsetzung auf unbeschränkte Horizonte
                → [offen] vollständiges Objekt X mit exakter Weil-Gramidentität
                → danach: möglicher Anschluss an RH
```

Die [Arbeitsstrategie](00-uebersicht/OBJEKT_X_FORSCHUNGSSTRATEGIE.md) setzt beim
vollständigen neuen Schurrest an. Neue Terminalpositivität darf in seiner
Begründung nicht vorausgesetzt werden. Winkel- und Momentdiagnosen dienen
konkret benannten Abschätzungen dieser Fortsetzung.

Die [Architektur](00-uebersicht/OBJEKT_X_ARCHITECTURE.md) erklärt die Rollen
dieser Übergänge. Die [Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)
legt die Anforderungen an Objekt X fest, insbesondere die vollständige
Testklasse und eine Konstruktion ohne vorausgesetzte Weil-Positivität.

## Belege, Reproduktion und Geschichte

- **Beweise:** Das [Ergebnisregister](00-uebersicht/SURVIVOR_REGISTRY.md)
  führt zu den jeweiligen Beweispaketen. Deren Voraussetzungen und
  Geltungsbereiche sind für die Aussagen entscheidend.
- **Reproduktion:** Paket-READMEs beschreiben Eingaben, Software und konkrete
  Prüfläufe; etwa die [Kammerkette bis A11](research/x-c1/chambers-through-a11-2026-09-28/README.md),
  der [gemeinsame Y-Kernel](research/x-c1/canonical-y-kernel-second-order-2026-10-03/README.md)
  und die [H₀-Folgeuntersuchungen](research/x-c1/canonical-h0-followups-2026-10-03/README.md).
  Analytischer Beweis, Zertifikatsreplay und unabhängiger Review sind getrennt ausgewiesen.
- **Geschichte:** Das [Archiv](00-uebersicht/ARCHIVE_INDEX.md) bewahrt frühere
  Kandidaten, Fehler, Korrekturen und verworfene Ansätze. Datierte Statusangaben
  beschreiben den damaligen Stand. Historische Originale behalten ihre Pfade
  und ihren Wortlaut am jeweiligen Quellcommit. Für die
  [verlegten Root-Dateien](00-uebersicht/archiv/root-journal-2026-10-03/README.md)
  sind Originalbytes sowie alte und neue Pfade dokumentiert.

Die versiegelten Originalpakete behalten auch ihre damaligen Integrationsangaben.
Ein dortiges `PENDING_STATUS_REVIEW` oder `RESEARCH_BRANCH_UNMERGED` beschreibt
den ursprünglichen Paketstand. Die heutige Aufnahme ist im
[Forschungsregister](00-uebersicht/RESEARCH_STATE.yaml) und
in den jeweiligen Integrationsnachweisen dokumentiert:
[#206](00-uebersicht/integrationsnachweise/PR206_2026-10-03.md),
[#211](00-uebersicht/integrationsnachweise/PR211_2026-10-04.md),
[#213](00-uebersicht/integrationsnachweise/PR213_2026-10-07.md) und
[#216](00-uebersicht/integrationsnachweise/PR216_2026-10-13.md).

Diese README dient der Orientierung. Die lesbaren Statusansichten werden aus
`RESEARCH_STATE.yaml` erzeugt; mathematische Aussagen beruhen auf den dort
gebundenen Quellen.

## Autor, Mitarbeit und Zitation

Das Projekt wird von **Sebastian Schmalnauer** geführt und mit Unterstützung
verschiedener KI-Agenten entwickelt. Diese Mitwirkung und interne Kontrollen
ersetzen keine unabhängige fachliche Begutachtung. Eine Neuheitsbewertung
erfordert einen Vergleich mit der einschlägigen Literatur.

Für konkrete Einwände bitte Satz, Datei, Commit und Begründung nennen.
[CONTRIBUTING](CONTRIBUTING.md) beschreibt geeignete Beiträge und regelt ihre Prüfung.
Die [A1-Prüfsteuerung](00-uebersicht/A1_CI_WIEDERVERWENDUNG.md) erklärt,
wann der gebundene Matrixnachweis wiederverwendet wird und wann eine neue
Rechnung erforderlich ist. Ein erfolgreicher kurzer Abgleich ist kein neuer
mathematischer Nachweis.
Die [Herkunft des Journals](00-uebersicht/HERKUNFT.md) ist separat dokumentiert.

Zitation und Herkunft: [CITATION.cff](CITATION.cff) · [ATTRIBUTION](ATTRIBUTION.md).
Bei Verwendung einen konkreten Commit angeben. Originale Repository-Inhalte
stehen, soweit nicht anders angegeben, unter [CC BY 4.0](LICENSE).
Für Drittmaterial gelten die jeweiligen Rechte und Lizenzen.
