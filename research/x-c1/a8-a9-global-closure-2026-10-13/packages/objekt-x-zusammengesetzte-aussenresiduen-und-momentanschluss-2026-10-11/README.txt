Objekt X — Zusammengesetzte Außenresiduen und Momentanschluss
Stand 11. Oktober 2026

Zuerst BERICHT.txt lesen. Alle Aussagen bleiben an die analytischen
Voraussetzungen der Vorgänger gebunden. Der unendliche Rest ab Grad 104
ist offen. Dieses Paket schließt A8->A9 und den Tailboden 1/20 nicht.

Portabler rationaler Replay (Python 3, nur Standardbibliothek):

python -B reproduce.py --responses-zip "PFAD/Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip" --common-zip "PFAD/Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip"

Die zwei früheren ZIPs sind getrennte, durch SHA256 gebundene Eingaben.
Das 5-MB-Eingangspaket zum unendlichen Dualrest ist unter inputs enthalten.
Alle Archive werden in ein frisches temporäres Verzeichnis entpackt;
Pfadausbrüche und symbolische Links werden zurückgewiesen.

Der Replay prüft die neuen und drei Eingangsmanifeste, führt den rationalen
Prüfer des eingesandten Pakets aus und rekonstruiert beide neuen
8x203-Residualmatrizen. Er bezahlt alle hier verwendeten Fehlergrößen neu
und prüft je Parität 203 positive rationale Pivots. Außerdem vergleicht
er die 3072/4096-Bit-Einschließungen der neuen Kreuzintegrale.
Mit --full-input-replay wird zusätzlich der rationale Replay des früheren
Antwortpakets gestartet; dabei werden dessen geerbte gebundene Eingaben
geprüft. Es ist kein neuer Funktionsintegrationslauf.

Erwarteter Abschluss:
PASS_COMPOSED_RESIDUAL_PACKAGE_FRESH_REPLAY
FULL_REMAINDER_CERTIFIED=false

HERLEITUNG.txt enthält Definitionen, Fehlerrechnung und das offene Ziel.
AUDIT_EXTERIOR.json enthält die rational geprüften neuen Schranken.
ATTACHMENT_GATES.json enthält die zwei endlichen Gates und den bezahlten
vollständigen Momentpreis. CROSS_*.json enthalten die vier neuen
vollständigen Kreuzintegrationen. EXTERIOR_*.json enthalten die neuen
zusammengesetzten Residualzeilen; die ergänzenden diagnostischen Strahlen
darin sind kein gesonderter Gegenzeugenbeweis des rationalen Replays.
INFINITE_REDUCTION_LOCAL.json dokumentiert den Neuaufbau der eingesandten
Geometrie auf unseren konkret gebundenen Vorgängerdateien.

Optionaler Funktions-Neuaufbau mit python-flint/Arb:
compute_cross.py ist die tatsächlich verwendete neue Integration. Sie
benötigt den bereits eingerichteten historischen Arbeitsbaum mit den
Originalquellen unter work/inherited, work/galerkin84-2026-10-10,
work/tail-probe-2026-10-10 und work/direct-rest84-2026-10-11. Die großen
historischen Quellpakete werden hier nicht nochmals dupliziert.
Der portable rationale Replay oben benötigt diesen Arbeitsbaum nicht.

Beispiel im bestehenden Arbeitsbaum, je Parität und für 3072/4096 Bit:
python -B compute_cross.py --root "ARBEITSBAUM" --proposal "EINGANG/data/even_proposal.json" --probe-model "EINGANG/data/PROBE_EVEN_3072.json" --count 8 --bits 4096 --parity even --out "NEUER_PFAD/CROSS_EVEN_4096.json"

--probe-model bleibt auch beim 4096-Bit-Lauf auf der festen Datei von
3072 Bit: sonst würden andere rationale Arbeitsfunktionen integriert.
Der Ausgabepfad darf noch nicht existieren. Für odd entsprechend ändern.
analyze_exterior.py dokumentiert die Arb-Zusammensetzung auf dem ursprünglichen
Arbeitsbaum. Der portable unabhängige Prüfer ist audit_exterior.py.

Keine Optimierung -O: Die Prüfer benutzen bewusst aktive Assertions.
Es werden keine externen Nachrichten, Commits oder Veröffentlichungen
für diesen Rechenschritt benötigt.
