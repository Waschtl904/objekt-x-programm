Objekt X — nichtpolynomialer Randtest ab Grad 104

Zuerst BERICHT.txt lesen. Das Ergebnis ist ein UNTERGRAM bzw. notwendiger
Test. Die vollständige obere Restschranke ist weiterhin offen.

Portabler rationaler Replay, nur Python-Standardbibliothek:

python -B reproduce.py --responses-zip "PFAD/Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip" --parent-zip "PFAD/Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip"

Die beiden früheren großen Archive sind getrennte gebundene Eingaben.
Die zwei neueren Prüf-/Dualrestarchive liegen unter inputs. Jeder Hash
wird geprüft; alle Eingaben werden nur temporär entpackt. Der Prüfer des
Eingangs läuft vollständig, einschließlich der Antwortaudits und des
JSON-Wertvergleichs statt des fehlerhaften CRLF/LF-Bytevergleichs.

Danach berechnet audit_endpoint.py die Projektionskoeffizienten und die
vollständige Energieschranke rational neu, rekonstruiert beide 203er-
Residualzeilen und bezahlt sämtliche Fehler. Er bestätigt die Rang-eins-
Budgetschranken sowie konkrete untere Werte auf rationalen Richtungen.
Ausgaben werden als JSON-Werte verglichen. Ohne -O ausführen.

Erwarteter Abschluss: PASS_ENDPOINT_PACKAGE_FRESH_REPLAY
FULL_WEIGHTED_TAIL_UPPER_COMPUTED=false
FULL_REMAINDER_CERTIFIED=false

Vier neue Funktionsintegrationen liegen als ENDPOINT_*.json vor. Die
ANALYSIS_*.json enthalten ihre Zusammensetzung mit den festen Antworten.
AUDIT_ENDPOINT.json enthält die unabhängig rational geprüften Aussagen.
Die Felder L_outside_exact_model und Eplus beschreiben die geschlossene
obere Energieformel; eine Gleichheit mit einer ungeprüften endlichen
hohen Koeffizientensumme wird nicht benutzt.

Optionaler frischer Funktions-Neuaufbau mit python-flint/Arb und dem
historischen Arbeitsbaum ROOT (gleiche Abhängigkeiten wie Galerkin84):

python -B compute_endpoint.py --root "ROOT" --bits 3072 --cut-power 14 --parity even --out "NEU/ENDPOINT_EVEN_14_3072.json"

Entsprechend odd und 4096 Bit. Zielpfade dürfen nicht existieren.
Das Skript ist hier nicht als eigenständiger Ersatz für alle historischen
Quellpakete gedacht. Der portable rationale Replay benötigt diesen
historischen Arbeitsbaum und python-flint nicht.

build_endpoint_engine.py dokumentiert die Anpassung des vorhandenen
Galerkin-Quellenintegrators; endpoint_tail.py enthält den neuen Anschluss.
analyze_endpoint.py dokumentiert die ursprüngliche Arb-Auswertung im
historischen Arbeitsbaum. Maßgeblich für die unabhängige rationale
Gegenprüfung ist audit_endpoint.py.

Nächste offene Aufgabe: eine obere Einschließung über ALLE höheren
Richtungen der zusammengesetzten Residualfunktionen. Das Bestehen des
neuen Randtests ersetzt diese Aufgabe nicht.
