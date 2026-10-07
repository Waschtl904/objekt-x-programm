Objekt X — Acht Quellen, A8→A9
5. Oktober 2026. AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.

Lesereihenfolge:
1. BERICHT.txt: Ergebnis, Bedeutung, Grenzen und nächste Aufgabe.
2. PROOF.txt: mathematischer Schluss und übernommene Annahmen.
3. EXACT_CHECK.json: zwei getrennt rational geprüfte Schlusszertifikate.
4. REMAINDER_CANDIDATE.txt: präzise noch offene Restobligation.

Rationale Böden gegen die vorab festgelegte physische L2-Quellgrammatrix:
gerade 4e-12; ungerade 3e-11. Der gesamte alte Raum ist berücksichtigt.
Die gesamte neue Quotientenfamilie und Objekt X bleiben offen.

Das ursprüngliche Vier-Quellen-Archiv bleibt unter inputs/ bytegleich
erhalten und enthält alle gebundenen alten Modelle und Hilfsmodule.
Die neuen Programme, Ergebnisse beider Präzisionen, rationalen Antworten
und Diagnosen liegen separat. baseline/ erhält den offenen ersten
Gamma-128-Versuch. Die begründete Verfeinerung ist vor ihren Ergebnissen
in REFINEMENT.json festgehalten.

Reproduktion mit Python 3.13 und python-flint 0.9.0:
  python -m pip install -r requirements.txt
  python -B reproduce.py --out ../acht-quellen-replay

Das Ausgabeziel muss neu sein und außerhalb dieses Pakets liegen.
Der Wrapper prüft sämtliche Paketdateien und das Originalarchiv, führt
3072 und 4096 Bit aus und prüft beide Schlusszertifikate exakt. Alle
eingeschlossenen Integrale müssen zu den Referenzintervallen passen.
Separat gerundete Majoranten dürfen im ausdrücklich begrenzten Rahmen
variieren; ihre positiven rationalen Schlussböden werden jeweils erneut
geprüft. Der ursprüngliche Formraumbeweis und die großen Operatormodelle
bleiben gebundene Eingaben, keine neue externe Begutachtung.

Nur Archiv-/Paketprüfung, ohne erneute Mathematikrechnung:
  python -B reproduce.py --check-only --out ../acht-quellen-input-check

Die Rechnungen bei beiden Präzisionen wurden tatsächlich ausgeführt.
Der fertige Archivwrapper wurde zusätzlich im Prüfmodus ausgeführt;
die unveränderten Rechnungen wurden nicht ein drittes Mal wiederholt.
Dies wird im externen Abschlussbeleg ausdrücklich ausgewiesen.

GitHub wurde in dieser Untersuchung nicht verändert. Ausgangspunkt ist
Main 040c1c2f75753d0daa680c55b14b88524955f851. Der bisherige globale
Verifikationssnapshot wird durch dieses lokale Ergebnis nicht verändert.
