Objekt X — gemeinsamer signierter C-Inversenblock, 7. Oktober 2026

Zuerst lesen: BERICHT.txt.
Analytische Ableitung: HERLEITUNG.txt.
Rationale Prüfquittung: EXACT_CHECK.json.
Maschinenlesbarer Status: STATE.json.

Schnelle Reproduktion, nur Python-Standardbibliothek:

  python reproduce.py

Dies prüft alle Dateihashes und rekonstruiert die rationalen gemeinsamen
Schlussmatrizen. Es startet keine alten oder neuen Operatorintegrationen.

Neue Rechenstufe vollständig wiederholen:

  python -m pip install python-flint==0.9.0
  python reproduce.py --recompute-new --destination /absoluter/neuer/leerer/ordner

Unter Windows einen geeigneten absoluten Windows-Pfad verwenden. Der
Zielfolder muss leer sein und außerhalb dieses Pakets liegen. Die vier
neuen Integrationsläufe benutzen 3072 bzw. 4096 Bit. Die gespeicherten
Vorgängerdaten bleiben Eingaben; deren früheren langen Läufe werden
dadurch ausdrücklich nicht wiederholt. Zeitangaben und Quellhashes der
neu erzeugten Ergebnisdateien können sich ändern. Ein identischer
komprimierter Archivhash ist kein Abnahmekriterium eines neuen Laufs.

Die unveränderte ursprüngliche U00-Paketfassung liegt zusätzlich unter
inputs/. Ihr SHA256 ist in SOURCE_BINDINGS.json festgehalten. Die zur
direkten neuen Rechnung benötigten Dateien stehen bereits in work/.

Das neue Paket enthält gemeinsame Einschließungen, keine exakten Werte
der tatsächlichen unendlichen Inversen. Das Scheitern seiner U00-
Obermatrizen ist kein negativer Zeuge für die tatsächliche Form.

Der Nachweis zum Nicht-C-Anteil gilt für die konkret angegebenen vier
Mittelpunktgrame und vier skalaren gemeinsamen Young-Hüllen. Er schließt
bessere Fehlergrame und erhaltene Kreuzkorrelationen nicht aus.

Die ursprünglichen Operator-/Formidentitäten und Majoranten bleiben
gebundene Voraussetzungen. Keine externe fachmathematische Begutachtung.
G01, gamma01, beta_tail und der volle Restgate bleiben offen.


Technischer Nachtrag vom 8. Oktober 2026

Der schnelle Pr�fer normalisiert eingebettete Windows-Pfade beim Lesen.
Alle bestehenden numerischen Ergebnisdateien bleiben bytegleich. K�nftige
Response-Ausgaben schreiben portable Pfade mit /.

compute_cross.py berechnet seine Integrale tats�chlich mit 3072 bzw.
4096 Bit. enclose_response.py rechnet anschlie�end mit 1024 Bit. Die
Dateinamen RESPONSE_3072/4096 kennzeichnen die Eingabeintegrale. Es sind
keine zwei vollst�ndigen Response-Arithmetiken mit diesen Pr�zisionen.
Die rationale Schlusspr�fung ben�tigt keine Flie�kommaarithmetik.

Mathematische Aussagen und gebundene Eingaben sind unver�ndert.
Die urspr�ngliche Paketdatei vom 7. Oktober wird nicht �berschrieben.
