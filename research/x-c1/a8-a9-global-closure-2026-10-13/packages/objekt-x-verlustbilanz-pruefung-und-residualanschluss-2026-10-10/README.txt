Objekt X — Prüfung der Verlustbilanz und voller Residualanschluss
10. Oktober 2026

Zuerst PRUEFVERMERK.txt lesen.
RESIDUALANSCHLUSS.txt enthält die neue konditionale Herleitung.
PRUEFAUFTRAG_GPT2.txt enthält den nächsten konkreten Rechenauftrag.

Die tatsächliche vollständige 203x203-Grambedingung bleibt offen.
Die alten vollständigen Quellintegrationen wurden nicht alle wiederholt.
Neu wiederholt wurden beide direkten Kalibrierungsintegrationen.
Siehe PRUEFVERMERK.txt für den genauen Prüfungsumfang und seine Grenzen.

Reproduzieren:
Python 3.12 und python-flint==0.9.0 installieren. Das unveränderte,
separat übergebene Originalarchiv wird zusätzlich benötigt; sein
SHA256 steht in SOURCE_BINDINGS.json. Es ist nicht nochmals eingebettet.

  python reproduce_review.py /pfad/Objekt-X-Gemeinsame-Verlustbilanz-2026-10-10.zip --work /neuer/arbeitsordner

Optional bei einer Installation von python-flint außerhalb des Standardpfads:
  --deps /pfad/zum/python-modulordner

Mit zusätzlicher Wiederholung der beiden gezielten direkten Integrationen:
  --direct-integrations

Der Arbeitsordner muss neu sein und benötigt Platz zum Entpacken aller
Vorgänger. Das Prüfskript verändert keines der Originalarchive.

independent_checks.py benötigt für seine eigene Rechnung nur die Python-
Standardbibliothek. Es rekonstruiert die Fehlerintervalle exakt rational,
prüft gespeicherte Kalibrierungsdaten und enthält eindeutig markierte
synthetische Matrixtests. Die ursprünglichen Integrationen werden von
diesem Skript nicht neu ausgeführt.

expected/ enthält die in dieser Prüfung tatsächlich erzeugten Ergebnisse,
darunter die zwei neuen direkten Integrationsausgaben und deren Logs.
Sie sind keine Daten für den noch fehlenden vollständigen Restgram.

FULL_REMAINDER_CERTIFIED=false.
