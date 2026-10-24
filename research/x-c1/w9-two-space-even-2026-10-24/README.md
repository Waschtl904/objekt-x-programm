# Bedingter Vergleich auf dem eingefrorenen geraden Zweiraum

Unter H1–H4 besteht der gemeinsame Vergleich für alle **reellen** Linearkombinationen
der beiden festgelegten Richtungen. Die gezielte mathematische Gegenprüfung durch
GPT 1 und die anschließende technische Gegenprüfung durch GPT 2 sind abgeschlossen.
`AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN` bleiben bestehen.

[PROOF.md](PROOF.md) führt Satz, Voraussetzungen und Prüfgrenzen zusammen.
[STATUS.json](STATUS.json) beschreibt den bedingten Stand vor Integration.
[ARCHIVES.json](ARCHIVES.json) bindet die drei unveränderten Archive.
[READABLE_COPIES.json](READABLE_COPIES.json) bindet alle lesbaren Auszüge byteweise.

Die erste Restenergie ist durch den separaten [L1-Beleg](L1_REFERENCE.json) gedeckt.
Für die zweite Richtung gilt die eigene [Quellenanwendung](author-text/APPLICATION.txt).
Originale und Schutzrevision wurden nicht nachträglich bearbeitet. Ihre damaligen
PENDING-Vermerke bleiben stehen; das spätere [GPT-2-Votum](technical-gpt2/CONCLUSION.json)
schließt die technische Gegenprüfung separat ab. Es gilt nur für den dort genannten
exakten Revisionshash, nicht pauschal für spätere Änderungen.

Zur Abnahme dienen ausschließlich die geschützten Einstiege der Revision.
Die [Reproduktionsanleitung](REPRODUKTION.txt) startet keine neue Quadratur.
Die tatsächlichen Veröffentlichungs-Heads und CI-Läufe sind im zugehörigen Draft-PR
getrennt von den historischen Prüfständen dokumentiert. Punkt 4 bleibt offen.

Veröffentlichungsanschluss: ARCHIVE_CHUNKS.json bindet die großen ZIPs als
geordnete Binärteile. verify.py setzt exakt die Originalbytes zusammen; keine
Neu-Verpackung, keine Änderung der Schutzrevision oder ihrer Testprotokolle.
L1_REFERENCE.json bindet den benötigten Draft #258 an seinen vollständigen Head.
Begrenzter Paket-/Replaytest: python -B research/x-c1/w9-two-space-even-2026-10-24/verify.py --replay
