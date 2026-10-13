Objekt X — gemeinsame U00-Rechnung A8->A9
7. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Ergebnis: Die rationalen gemeinsamen U00-Rückfallmajoranten sind berechnet.
I8-U00 besitzt in keinem der beiden Läufe eine positive Reserve. Dies ist
kein negativer Zeuge der tatsächlichen Form und kein Vollrestzertifikat.

Zuerst lesen:
  BERICHT.txt       Ergebnisse, Budget und nächster Engpass
  HERLEITUNG.txt    analytische Ableitung und Aussagegrenzen
  EXACT_CHECK.json  separate rationale Schlussprüfung

Der Ordner work/u00-2026-10-07 enthält neue Programme, alle vier
3072-/4096-Bit-Paare von Mittelpunkt- und Funktionalrechnungen sowie die
beiden rationalen Schlussmatrizen. Die work-Verzeichnisstruktur erhält
die ursprünglichen relativen Rechenpfade und ermöglicht einen portablen
Nachlauf. work/remainder-integration-check-v2/originals enthält die
tatsächlich benötigten gebundenen Eingaben und Hilfsprogramme. Die
ursprünglichen vollständigen Archive bleiben im kanonischen Repository.

Schnellprüfung, nur Python-Standardbibliothek:

  python reproduce.py

Sie kontrolliert sämtliche Paketdateien, rekonstruiert U00 und die
Richtungsbudgets mit Fraction, prüft die relativen C-Residualschranken und
vergleicht 10.520 neue Intervalleinträge zwischen beiden Präzisionen.
Sie rekonstruiert keine Operatorintegrale und ersetzt keine externe
mathematische Begutachtung.

Vollständiger numerischer Nachlauf:

  python -m pip install python-flint==0.9.0
  python reproduce.py --full --destination PFAD_ZU_NEUEM_LEEREM_ORDNER

Getestete Umgebung: Windows, Python 3.13, python-flint 0.9.0. Für den
vollständigen Nachlauf ist python-flint in der benutzten Python-Umgebung
erforderlich. Der Nachlauf arbeitet in einem neuen Verzeichnis und lässt
dieses Paket unverändert. Er kann mehrere zehn Minuten dauern. Es wird
keine Netzwerkverbindung vom Rechenprogramm benutzt.

Die historische Rundungspräzisierung in ROUNDING_BOUND_UPDATE.json
behandelt den winzigen Fehler der Rechenpolynome mit der vollen
Schalennorm. Die gespeicherten Modellfehler wurden dafür konservativ
vergrößert; alle Integrale blieben unverändert. Ein frischer Vollnachlauf
verwendet die korrigierte Norm unmittelbar und kann deshalb geringfügig
schärfere Modellfehlerschranken ausgeben. Bytegleichheit ganzer Läufe
wird wegen Laufzeiten und konservativer Hüllen nicht behauptet.

Keine neue Pilotgeometrie, keine neue Horizontrechnung, kein G01 oder
beta_tail. FULL_REMAINDER_CERTIFIED bleibt false. Die aktuelle
Objekt-X-Arbeitsdefinition bleibt unverändert.

Repository: https://github.com/Waschtl904/objekt-x-programm
Gebundener Ausgangsstand: da50f0a21691e6fd253163e612a2af2898606581
Dieses neue Paket wurde lokal erstellt; es wurde noch nicht in main
eingetragen oder gepusht.
