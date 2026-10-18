# Abnahmeumfang vor dem Abnahmelauf

Mathematische Änderung: neue zulässige skalare Inversgewichtung, gerichteter
Transfer der unveränderten #238-Komponenten und begrenztes Familien-No-Go.
Keine Änderung übernommener Eingaben, Funktionen oder Richtungen.

Verpflichtend:

- Neue Herleitung gegen Abschnitte 2 und 6 der gebundenen Inversherleitung
  prüfen; echte Loewner-Verkleinerung, Trade und Hilfsuntervergleich trennen.
- `preflight.py --check` aus einem frischen Archiv aller getrackten Dateien;
  EXPECTED bytegleich, alle verwendeten Datei-/Mitgliedsbindungen gültig.
- Exakte Negativkontrollen für zu kleinen P-Faktor und unbezahlten Kreuzterm.
- Abweisung von python -O und einer manipulierten gebundenen Datei.
- Registry-Validator, generierte Ansichten, bestehende Registry-Tests,
  Diff-/Scope-Kontrolle. Keine Änderung historischer Mathematikdateien.
- Veröffentlichter Tree identisch zum lokal geprüften finalen Tree.

Nicht Teil dieses Auftrags: Wiederholung großer #238-Integrationen,
R_L-Solve, neue Antwortmatrix- oder Richtungssuche, externe Fachprüfung,
Merge oder Prüfung anderer PRs. Eine Veröffentlichung startet nur die
ohnehin anwendbare Repository-CI; laufende CI ist kein Erfolg.
