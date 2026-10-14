Objekt-X-A9-Gesamtboden-und-Lokale-Fortsetzung-2026-10-13
AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Einstieg: BERICHT.txt, danach HERLEITUNG.txt und ANSCHLUSS_GPT1.txt.

Neu unter gebundenen Eingaben:
q_A9 >= 1e-207 I in physischem L2 auf dem ganzen Formraum;
q_t >= 1e-421 I für log3 <= t <= log3+exp(-10^215).
Der zweite Radius ist eine exakte symbolische positive Zahl, nicht 0.

Python3 mit Standardbibliothek genügt:
  python reproduce.py
Optional mit dem unveränderten Originalpaket:
  python reproduce.py --schur-package <Original-Schurpaket.zip>

Der schnelle Replay prüft Manifest, unveränderte vollständige S-Quelldatei,
24 neue Bruch-LDL-Pivots, 24 unabhängige ganzzahlige Hauptminoren,
16 Achtspaltengram-Pivots, die rationalen Reihen- und Normabschätzungen
und synthetische Gegenkontrollen. Er stimmt mit CHECK.json überein.
Die Zusatzoption bindet K12 und alle übernommenen Schurskalare direkt
an das Originalarchiv. Analytische Sätze stehen im Beweistext; sie sind
nicht maschinell formalisiert. Alte große Integrationen werden nicht
nochmals ausgeführt.

sources/ enthält unveränderte historische Texte und die ursprüngliche
S-Datei. Deren frühere Offenheitsfelder bleiben Herkunftsdaten; die
aktuellen Aussagen und Grenzen stehen ausschließlich in den neuen
Dateien. SOURCE_BINDINGS.json enthält Originalpfade und Prüfsummen.

Offen: externe mathematische Prüfung, arithmetische Identität als
Herkunftseingabe, gesonderter alter Tailboden1/20, praktisch nutzbare
weitere Horizontübergänge, Kofinalität, Objekt X, RH.
