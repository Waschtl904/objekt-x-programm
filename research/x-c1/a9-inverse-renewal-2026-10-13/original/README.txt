Objekt X — A9-Inverserneuerung und vollständiger hoher Schurrest

Lesereihenfolge
  BERICHT.txt: Ergebnis und genaue Grenze des neuen Fortschritts.
  HERLEITUNG.txt: vollständige neue analytische Argumentation.
  ANSCHLUSS_GPT1.txt: vorgeschlagene unabhängige Gegenprüfung.

Rationaler Replay, Python 3, nur Standardbibliothek:
  python reproduce.py

Mit erneutem direktem Abgleich aller E- und X-Felder mit den Vorgängern:
  python reproduce.py --schur-package "PFAD/ZUM/Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13.zip"

Die 574 gerichteten positiven LDL-Pivots, alle neuen rationalen Konstanten
und Gegenkontrollen werden vollständig wiederholt. Der Replay prüft das
Manifest und vergleicht sämtliche mathematischen Ergebnisfelder mit
AUDIT.json. Laufzeit und optionaler ursprünglicher Feldabgleich werden
beim Inhaltsvergleich gesondert behandelt. REPLAY.json und REPLAY-audit.json
werden erzeugt; die versiegelten Eingabedateien werden nicht verändert.

INVERSE_EVEN.json und INVERSE_ODD.json enthalten E203, X84x203 und die
neuen P_upper84-Matrizen als exakte Brüche. Ihr Feld "status" bezeichnet
absichtlich den Status beim Erzeugen: Kandidat vor rationaler Prüfung.
Die bestandene nachfolgende Prüfung steht in AUDIT.json. Ein positives
numerisches Eigenwertbild wird nirgendwo als Zertifikat verwendet.

Optionaler Neubau der beiden Kandidaten, benötigt python-flint:
  python build.py --schur-package "PFAD/ZUM/Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13.zip" --output-dir rebuilt

Danach können die neu erzeugten Dateien zusammen mit audit.py in rebuilt
geprüft werden. Der Neubau ist für das rationale Zertifikat nicht nötig.
Die optional verwendete Arb-Inverse muss selbst nicht als Beweis vertraut
werden: Das ganze nachfolgende rationale Schurblockzertifikat genügt.

sources enthält unveränderte Herkunftstexte und frühere Prüfquittungen.
SOURCE_BINDINGS.json dokumentiert deren Bytes und SHA256. Ein Kopieren
der Texte ist keine erneute Prüfung sämtlicher analytischer Aussagen.
Die großen ursprünglichen Integrationen und ihre vollständigen Fehler-
einschließungen bleiben gebundene Voraussetzungen. Sie werden hier nicht
erneut erzeugt. Die ganze historische Rechenkette liegt im Schurarchiv.

Keine externe mathematische Begutachtung wird behauptet. Der neue Boden
2/3 gilt auf dem genau bezeichneten neuen Rest nach zusätzlichen 84
endlichen Richtungen. Der alte Tailboden 1/20, weitere konstruktive
Horizonte, Kofinalität, Objekt X insgesamt und RH bleiben offen.
