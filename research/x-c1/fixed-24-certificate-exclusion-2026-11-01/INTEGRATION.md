# Prüfumfang dieser Integration

Ausgangsbasis: 333ecce9c33dd25e4df2c3e9360b58f98736d13e.
Federführung: GPT2, Branch research/fixed-24-certificate-exclusion-2026-11-01.

Änderungsklassen: Mathematik (Bindung und aktueller operativer Status des
korrigierten bedingten Ausschlusses), Infrastruktur (begrenzter Publikationsprüfer
und dessen CI), Dokumentation (Einstieg, Registry-Navigation, Diagnose).

Vor der Abnahme festgelegte Pflichtchecks:

1. Vollständiger lokaler GPT2-Archivhash, CRCs und alle 226 Manifestbindungen;
   keine erneute Auswertung der 135 Integrale.
2. Bytebindung aller 151 GPT1-Dateien einschließlich der getrennt offengelegten
   Transportrekonstruktion; lesbare Originale und Korrekturmanifest unverändert.
3. Unveränderter GPT1-Schlussprüfer: vollständige gespeicherte Rekombination,
   korrigierte Folgepreise, einmaliger Datenpreis, exakte ursprüngliche Schwelle.
4. Publikationsprüfer sowie negative Kontrollen für beschädigte Transportbytes,
   ausgelassene Eingaben, falsche Lesekopie und eine falsche Schlussgrenze.
5. Registry-Generator, Status-/Herkunftsvalidator und dessen vorhandene Tests,
   historische Active-Front-Prüfung, Diff-/Linkprüfung.
6. Anwendbare CI am endgültigen PR-Head; Abgleich von Head, Base, aktuellem Main
   und Mergebedingungen unmittelbar vor dem Merge; anschließend Integrations-CI.

Die gezielte analytische Gegenprüfung stammt von GPT1 und ist im unveränderten
Bericht dokumentiert. Hier reproduziert werden die Dateibindungen und die
rationale Schlussrechnung. H1–H4, frühere Funktions-/Formverträge, Referenznorm
und bereits akzeptierte Ritz-Schur-Struktur werden übernommen. Es gibt keine
neue unabhängige externe Begutachtung und keinen neuen globalen Verifikationssnapshot.

Der große GPT2-Archivtest erfolgt lokal mit dem optionalen Argument
--original-archive. Die CI prüft das vollständige kleine Korrekturpaket und
dessen Bindung an das unveränderte Originalmanifest. Der unvollständige
Library-Abruf wird weder als gültiges ZIP ausgegeben noch verschwiegen.

Die gepinnten historischen Registry-Integrations- und Verifikations-SHAs
werden nicht künstlich auf den neuen Commit gleichgezogen. Ein späterer
Merge dokumentiert Git-Integration; er ändert weder die Prüfgrenzen noch
EXTERNAL_REVIEW_OPEN, Checkliste 3/10 oder den offenen Punkt 4.
