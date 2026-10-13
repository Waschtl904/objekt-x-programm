Objekt X — Antwortprüfung und tatsächlicher Außenresidual-Anschluss
11. Oktober 2026

Lesereihenfolge: BERICHT.txt, ANSCHLUSS_GPT2.txt, PROOF.txt.

Rein rationaler Replay, Standard-Python ohne Zusatzpakete:

python -B reproduce.py --responses-zip PFAD/Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip --parent-zip PFAD/Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip --dual-zip PFAD/Objekt-X-Unendlicher-Dualrest-und-Aussenrichtungen-2026-10-11.zip

Ohne -O ausführen: Assertions sind Teil der Prüfung. Alle drei Original-
archive werden über ihre SHA256 gebunden und nur in temporäre Verzeichnisse
entpackt. Der Replay prüft die neuen Antworten, den vorigen Dualraumanschluss,
alle neuen endlichen Anschlussbedingungen und die acht Residualbeiträge.
Er korrigiert ausdrücklich den CRLF/LF-Bytevergleich des Antwortpakets durch
einen JSON-Wertvergleich. Keine mathematische Kontrolle wird übersprungen.

Der Replay prüft gebundene Integraldateien; er integriert nicht neu.

Frische vollständige J84/K8-Integration, benötigt python-flint 0.9.0 und
den bisherigen Galerkin-Arbeitsbaum ROOT mit work/direct-rest84-2026-10-11:

python -B compute_external_cross.py --root ROOT --count 8 --bits 3072 --parity even --out NEU/CROSS_EVEN_3072.json

Entsprechend odd und 4096 Bit. Der Ausgabeweg darf vorher nicht existieren.
Das Skript berechnet vollständige hohe Funktionsintegrale einschließlich
aller Primzellen. Es speichert auch einen .high.json-Zwischenstand.

Auswertung der neuen festen Antworten auf diesen Außenrichtungen:

python -B analyze_external_residual.py --root ROOT --responses ANTWORTPAKET_ENTPACKT --probe DUALPAKET_ENTPACKT/data/PROBE_EVEN_3072.json --cross NEU/CROSS_EVEN_3072.json --connection data/CONNECTION.json --out NEU/RESIDUAL_EVEN_3072.json

Die Dateien unter data enthalten die vier frischen Integrationen, beide
Residualauswertungen, die rationale Prüfquittung und den Eingangsvergleich.
Der vollständige gewichtete Rest ab k104 ist weiterhin offen.
