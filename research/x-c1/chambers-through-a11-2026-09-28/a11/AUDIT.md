# Prüfumfang A11

Die lokale Herleitung betrifft die feste C1a-Familie und die ursprünglichen
zwei Mellinbedingungen. Alle Aussagen sind auf 1≤A≤log(11)/2 beschränkt.

## Tatsächlich ausgeführt

1. Das vollständige A9-Manifest wurde vor Übernahme der Programme geprüft.
2. Neue achtteilige Shiftgeometrie, gemeinsame Shift-/Potentialverluste,
   Gamma-Radius, hohe Momente und sieben commitgebundene Quellen: 187 Checks.
3. Alternative Integralzusammensetzung des vollständigen Modellbildes bei
   N15/M16: 245 Vergleiche. Diese ersetzt keine große zweite Integralrechnung.
4. Vollständiger neuer Aufbau N571/M416 bei 3072 Bit; alle sieben Kanäle,
   V², S², logarithmische und Gamma-Kreuzterme, beide Paritäten.
5. Nach dem gescheiterten direkten Intervallversuch: exakt rationale
   Kongruenz der unveränderten vollständigen F-Intervalle, je 285 positive
   Gershgorin-Zeilenmargen und 285 positive Arb-LDL-Pivots. Die exakte
   Frobeniusnorm von P bezahlt die ursprünglichen niedrigen Koordinaten.
6. Eigenständige Ganzzahlintervallimplementierung: je 285 positive Pivots,
   Gamma-Residual aus den gelieferten Polynomkoeffizienten, neue Fehlerterme,
   tatsächliche Matrixeinschließungen, eigene vollständige Kongruenzprodukte,
   Zeilenmargen, Normrückrechnung und gemeinsame Reserve erneut geprüft.

Gemeinsamer physischer Boden: `1/100000000000000000000000000000000000000000000000000`. Gemeinsamer Defektboden: `1/1300000000000000000000000000000000000000000000000001`.

## Grenzen

Die Ganzzahlprüfung importiert weder Arb noch den Generator oder dessen
Checker. Ihr Integralmodell bleibt eine Eingabe. Beide Implementierungen
wurden in dieser Aufgabe ausgeführt; eine organisatorisch unabhängige
externe Gesamtprüfung wird damit nicht behauptet. Die allgemeinen Abschluss-,
Operator- und Positivitätsargumente sind weiterhin extern zu prüfen.

Die Behauptung des allgemeinen erneuerbaren hohen Tails steht als analytischer
Satz in GENERAL_TAIL_PRINCIPLE.md. Die 187 Kontrollen beziehen sich auf die
konkrete A11-Instanz; sie sind kein Computerbeweis der Aussage für alle Horizonte.

Ein positiver hoher Raum entscheidet den endlichen niedrigen Schurrest nicht.
Der lokale Erfolg liefert weder eine allgemeine Terminalreserve noch eine
globale Konstruktion von Objekt X.

## Herkunft und Erhalt

Die frühen A9- und Wandbeweise unter inputs/ sind unveränderte historische
Eingaben. Ihre relativen Links beziehen sich auf die damaligen Pakete.
ENGINE_BINDINGS.json und ENGINE_ADAPTATION.diff dokumentieren die unmittelbare
A9-Abstammung; deren Repository-Vorlagen sind zusätzlich gebunden.
Die früheren Pakete und ihre ZIPs werden nicht verändert.

Es erfolgten keine GitHub-Schreibzugriffe, Registry-Promotionen, Commit-/Branch-
Änderungen oder Taglöschungen. Die frühere O8/O9-Hintergrundfortsetzung bleibt
pausiert. MAIN_CHECK.md dokumentiert den gelesenen Vergleich mit paralleler
Repository-Arbeit.
