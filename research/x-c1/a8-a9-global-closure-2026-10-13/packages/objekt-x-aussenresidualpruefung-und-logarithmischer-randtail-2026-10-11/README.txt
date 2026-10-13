Objekt X — Außenresidualprüfung und vollständiger logarithmischer Randtail
11. Oktober 2026

Zuerst BERICHT.txt, dann ENDPOINT_PROOF.txt und LOG_TAIL_METHOD.txt lesen.
Für GPT 2: ANSCHLUSS_GPT2.txt. Alle Aussagen behalten die geerbten
analytischen Voraussetzungen und EXTERNAL_REVIEW_OPEN.

Portabler rationaler Replay mit Standard-Python:

python -B reproduce.py --responses-zip PFAD/Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip --common-zip PFAD/Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip

Das gerade geprüfte 6-MB-Außenresidualpaket ist unverändert eingebettet.
Alle Archive werden nur temporär entpackt und durch SHA256 gebunden.
Der eigene Replay prüft die unabhängigen Kreuzreferenzen, baut den
vollständigen Logmodell-Gram rein rational neu auf und rekonstruiert
alle äußeren Randkoeffizienten samt ihren 204er-Budgetzertifikaten.
Mit --full-input-replay wird auch der bereits lokal bestandene volle
rationale Replay des eingebetteten Außenresidualpakets ausgeführt.
Es werden dabei keine Funktionsintegrationen wiederholt.

Nicht mit -O ausführen. Assertions gehören zu den Prüfern.

Optionale neue Arb-Endpunktauswertung (benötigt python-flint 0.9.0 und
den historischen Galerkin-Arbeitsbaum mit den gebundenen Basisdateien):

python -B compute_outer_endpoint.py --root ARBEITSBAUM --responses ENT_PACKTE_NEUE_ANTWORTEN --out NEU/OUTER_ENDPOINT.json

Die rein rationale Nachprüfung verwendet die im Paket enthaltenen
gebundenen Q-, D-, S-Basisintervalle. Deren analytische Herkunft und
Isometrie sind geerbte Voraussetzungen, keine neue Basisbehauptung.

Der vollständige tatsächliche Residualrest ab Grad 104 bleibt offen.
Ein global eingeschlossener isolierter Logterm ist kein Ersatz für
die übrigen Residualteile oder ihre Kreuzterme.
