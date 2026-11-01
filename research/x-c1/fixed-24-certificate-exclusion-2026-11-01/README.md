# Korrigierter Ausschluss des festen 24er-Zertifikatsraums

Stand 1. November 2026. Der zuvor offene Gradiententest ist nach GPT1s
gezielter Gegenprüfung **unter H1–H4 und den übernommenen physischen
Funktions-/Formverträgen bestanden**. Damit ist die ganze festgelegte
24er-Zertifikatsfamilie bedingt ausgeschlossen. Kandidat, y_0, Antwort,
singuläre Außenmetrik und Schurkorrektur bleiben unverändert.

| Maßgebliche Größe | Gerichtete Grenze nach GPT1 |
| --- | --- |
| Physischer hoher Rest r | ≤ 0,058383477345103 |
| Vollständiger Datenpreis, genau einmal | < 0,004356223514 |
| Gesamtenergie gᵀ M_-⁻¹ g | ≤ 0,000949781310484370 |
| Schwelle E_* | ≥ 0,000972717481018334 |
| Positiver Abstand | ≥ 0,000022936170533964 |

GPT1 hat den Faktor sqrt(gamma) im neuen V-Transport durch einen ausreichenden
Preis für gamma ersetzt und sämtliche benannten Folgepreise bezahlt. Zusätzlich
wird die bereits bestätigte D12-Kappe 2,632e-50 übernommen. Die günstigeren
GPT2-Autorenwerte sind historisch und werden nicht als aktuelle Grenzen benutzt.
Die [unveränderte GPT1-Schlussabnahme](review/BERICHT.txt), ihre
[exakten rationalen Ergebnisse](review/GPT1_FINAL_REVIEW.json) und der
[Schlusszusammenhang](PROOF.md) dokumentieren dies.

## Original und Korrektur getrennt

Das [GPT2-Originalrelease](https://github.com/Waschtl904/objekt-x-programm/releases/tag/gpt2-physical-rest-2026-10-31)
enthält das unveränderte Archiv vom 31. Oktober: 267.597.341 Byte,
SHA-256 0ae5879e0783a88d102def93c5cce3a768e42dbc3c09209bac703822a154515e.
Beim lokalen Integrationslauf wurden die ganzen Archivbytes, alle CRCs und
alle 226 Manifestbindungen geprüft. Die Integrale wurden nicht wiederholt.

**Besonderheit des GPT1-Transports:** Zwei Abrufe des verlinkten Library-Archivs
lieferten dieselben 3.225.840 Byte, abgeschnitten innerhalb eines ZIP-Mitglieds.
Der unveränderte Abruf liegt deshalb als ausdrücklich unvollständige
[Quelldatei](archives/GPT1-Library-Abruf-unvollstaendig-2026-11-01.bin) bei.
Ein Hash eines vollständigen ursprünglichen GPT1-ZIP wird nicht behauptet.

Die vier neuen GPT1-Dateien und sein vollständiges Manifest waren bereits
vollständig mit lokalen ZIP-CRCs lesbar. Sämtliche fehlenden Dateien wurden
aus dem erhaltenen GPT2-Original beziehungsweise dem darin enthaltenen
GPT1-Datenarchiv übernommen. **Alle 151 Dateilängen und SHA-256-Werte stimmen
mit GPT1s unverändertem Manifest überein.** Die ausführbare
[Transportrekonstruktion](archives/Objekt-X-GPT1-Gezielte-Schlussabnahme-2026-11-01-Transportrekonstruktion.zip)
ist deshalb separat benannt und gebunden: 4.287.227 Byte, SHA-256
fffbe431f10f7cf2c64c0de9bb135132db1b0d2d9dd9fef16ac0f39e6f74096b.
Sie ist kein behauptetes bytegleiches Original-ZIP. Herkunft jeder Datei
und beide Transportidentitäten stehen in [ARCHIVE.json](ARCHIVE.json).

## Begrenzte Nachrechnung

Vom Repository-Stamm, Python 3.11 oder neuer, nur Standardbibliothek:

~~~text
python -B research/x-c1/fixed-24-certificate-exclusion-2026-11-01/verify_publication.py
~~~

Der Prüfer kontrolliert die Publikationsdateien, den unveränderten unvollständigen
Abruf, alle Mitglieder der vollständigen Transportrekonstruktion, GPT1s
Manifest und die lesbaren Originalkopien. Anschließend führt er GPT1s
unveränderten rationalen Schlussprüfer aus: gespeicherte gemeinsame Schätzer,
135 Abschnitte, beide positiven Endstreifen, Korrekturfolgen, einmaliger
Datenpreis und die ursprüngliche strikte Energieungleichung.

Optional prüft die Option `--original-archive PFAD_ZUM_GPT2_ZIP` das gesamte
große Original. Die CI lädt dieses 267-MB-Archiv nicht erneut; ihre
Nachrechnung bindet die ausgewählten Eingaben an dessen unverändertes Manifest.
[Prüfumfang und Pflichtchecks](INTEGRATION.md) trennen diese Leistungen.
Die [gespeicherte Diagnose](DIAGNOSE.md) beginnt keine neue Kandidatenrechnung.

## Abgeschlossen und weiterhin offen

Keine weitere Datenfehlerprüfung, Referenzzertifizierung, Restverfeinerung
für mehr Abstand oder Kandidatenserie innerhalb derselben 24er-Familie.
Ein konkreter Widerspruch oder Bindungsfehler bleibt ein Wiederöffnungsgrund.

Der Befund behauptet weder Negativität der tatsächlichen Komplement-Schurform
noch einen positiven Anschluss. GPT1s nächste Aufgabe ist genau eine
analytisch begründete Methodenentscheidung: engere zulässige Inversenergie
oder eine nachweislich außerhalb des ausgeschlossenen Raums liegende
Antworterweiterung, mit Erfolgsbedingung und Operator-/Domänenverträgen.
Keine A11-Zielpositivität als Eingabe und keine ungeprüfte Operatorwirkung auf V.

Projektinterne Gegenprüfung, reproduzierte rationale Rechnung, externe
Begutachtung und Git-Integration bleiben getrennt. AUTHOR_DERIVED_NO_GO /
EXTERNAL_REVIEW_OPEN; Punkt 4, konstruktiver A9→A11-Anschluss, unendliches
Komplement und Objekt X bleiben offen. Checkliste weiterhin 3/10.
