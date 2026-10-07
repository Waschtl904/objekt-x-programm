Objekt X — vollständige Restdarstellung A8 -> A9, 5. Oktober 2026

Zum Lesen:
  BERICHT.txt       Ergebnis und Aussagegrenzen
  BEWEIS.txt        vollständige neue Herleitung, einschließlich Nachtrag
  PRUEFAUFTRAG.txt  begrenzter Auftrag für eine zweite Gegenprüfung

Zur Reproduktion der endlichen Arithmetik:
  python -B check_remainder.py

Erforderlich ist nur Python 3 mit Standardbibliothek. Der Aufruf gibt JSON
aus und schreibt keine Dateien. CHECK_RESULT.json ist die gespeicherte
erfolgreiche Ausgabe. Der Prüfer verifiziert die gebundenen Eingabekopien,
die alten kleinen Schlussmatrizen und die neuen exakten skalaren Tests.
Er baut keine Operatorintegrale auf. Die analytischen Domänen-, Dichte-
und Kompaktheitsbeweise benötigen eine gesonderte mathematische Prüfung.

inputs/ enthält unveränderte Belegtexte und die kleinen Schlussmatrizen.
Die großen ursprünglichen Archive werden nur durch ihre Prüfsummen
referenziert; dieses Paket enthält keinen vollständigen Operator-Replay.
SHA256SUMS bindet alle Dateien außer sich selbst.

Status: neue analytische Restdarstellung und exakte Geometrieprüfung;
vollständige Restpositivität OPEN, externe mathematische Prüfung OPEN.
