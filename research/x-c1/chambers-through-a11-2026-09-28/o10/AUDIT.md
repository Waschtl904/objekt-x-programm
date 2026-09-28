# O10: interner Abgleich der Herleitung

27. September 2026. Eigenprüfung der lokalen Herleitung; **keine unabhängige
externe Abnahme**. Maßgeblich ist der [Beweis](PROOF.md).

## Abgleich mit dem gebundenen O10-Rohinterface

| Anforderung | Nachweis | Geprüfte Grenze |
| --- | --- | --- |
| Richtige aktive Kanäle | §2, Gleichungen (5)–(6) | 8 bei A8 und 9 bei A9 jeweils ausgeschlossen |
| Gekoppelter neuer Mediator | §2, (7)–(9) | Derselbe geänderte Nenner und sämtliche Kreuzterme; keine Einzelkanal-Gramaddition |
| Vollständige Quellen | §3, (10)–(12) | Abschluss der ursprünglichen Zwei-Mellin-H¹₀-Quellen; positive verschobene Formnorm |
| Alter Raum wird korrekt fortgesetzt | §3, (13) | Nullfortsetzung ist für die verschobene Formnorm isometrisch |
| Beschränktheit des T-Wandquotienten | §4, (14)–(17) | Analytische Schranke auf der ganzen Frequenzachse, einschließlich der Umgebung von Null |
| Getrennter D-Wandquotient | §4, (16) | Eigene untere Zählerschranke `n_->kappa>5` |
| Beide Quotientenabstiege | §5, (20) | Bildvorschriften hängen nicht vom Quellvertreter ab |
| Erweiterung in die richtigen Carrier | §5, (18)–(22) | Grenzwerte bleiben in abgeschlossenen Bildräumen; keine Surjektivität auf größere Carrier unterstellt |
| Beide Quellenidentitäten | §5, (22) | Gelten durch Stetigkeit auf den vollständigen Quellen |
| Identität und beide Cocycle-Gesetze | §6, (23)–(24) | Alle Tripel bis A9, höchstens ein Wandwechsel |
| Neuer Gamma-/T-Floor | §7, (25)–(27) | Trägerbound neu bis A9 hergeleitet; kein übernommener alter Horizontsatz |
| Defektintertwining | §7, (28) | Beschränkte Produkte und dichter T-Quellenbereich ausdrücklich geprüft |
| Gramkompression | §8, (29)–(30) | Aus Formnaturality abgeleitet; rohe Wandisometrien werden nicht vorausgesetzt |
| Reichweite der O8-Reserve | §9, (31) | Nur der transportierte alte Teilraum wird positiv kontrolliert |

## Kritische Punkte der Eigenprüfung

1. **Nullfrequenz:** Der T-Quotient ist bei Null formal `0/0`. Die globale
   Schranke folgt aus `1-cos(ell xi)<=g0(xi)<=g(xi)` für alle Frequenzen.
   Der frei gewählte Einzelpunktwert verändert den L²-Operator nicht.
2. **Formnaturality ist eine Quellenaussage:** Das neue Symbol unterscheidet
   sich um `-2w8 cos(ell xi)`. Es verschwindet nicht punktweise. Erst die
   disjunkten alten physischen Träger lassen beide Translationspaarungen
   verschwinden. Die Argumentation gilt für beliebige zwei Quellen, nicht
   nur für eine diagonale Energie.
3. **Vollständigkeit:** Die verschobenen Gewichte sind beidseits der Wand
   gleichmäßig äquivalent zu `1+g`. Daher werden dieselben ursprünglichen
   Quellen vervollständigt; die T-/D-Abbildungen und die Quelleninklusionen
   besitzen die behaupteten stetigen Fortsetzungen.
4. **Carrier und Umgebungsraum:** Ein invertierbarer Multiplikator auf L²
   wird nur auf den jeweils alten Carrier eingeschränkt. Sein Bild liegt
   im neuen Carrier und ist abgeschlossen. Die globale L²-Invertierbarkeit
   liefert keine Surjektivität auf den gesamten neuen Carrier.
5. **Positivität:** `||R||<=sqrt(90)` ist ein Beschränktheitsnachweis. Die
   positive Kompression auf dem alten Bild lässt das Vorzeichen auf den
   neuen Richtungen offen. Der Prüfer enthält ein exaktes abstraktes Modell
   mit positivem altem Bild und negativer zusätzlicher Richtung.
6. **Kammergrenzen:** Die Plusformeln gelten nur für `A8<A<=A9`. Die
   Fortsetzung strikt rechts von A9 und der neue q=9-Kanal sind nicht erfasst.

## Ausgeführte Unterstützungskontrollen

`CHECK_RESULTS.json` dokumentiert 68 erfolgreiche Kontrollen mit exakten
rationalen Zahlen oder formalen Polynomen. Darin enthalten sind die
SHA-256-Abgleiche aller sieben gepinnten Eingaben. Frequenzgitter oder
Gleitkommatoleranzen werden nicht als Beweis der Multiplikatorschranken benutzt.

Die Datei bindet die geprüften Fassungen von Beweis, Prüfer und Eingaberegister
über SHA-256. Externe analytische Prüfung, Repository-Integration und
mathematische Statusübernahme sind damit nicht ausgeführt.
