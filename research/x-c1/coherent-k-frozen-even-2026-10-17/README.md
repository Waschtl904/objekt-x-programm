# Fester gerader Kandidat: gemeinsamer k-Fehler

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**, unter den gebundenen Operator-,
Domänen- und Quellenmodellvoraussetzungen. Baut auf #234 auf.

| Größe | Gerichtetes Ergebnis |
|---|---:|
| L für den unveränderten geraden Kandidaten | [1.238460; 1.748815] |
| Ausschlussschwelle | etwa 3.31424941794 |
| gemeinsamer k-Support | < 9.372706e-6 |
| hoher Beitrag bei festem k_0 | < 0.255167454 |
| Reserve auch mit unterem tatsächlichem K_P-Endpunkt | > 1.56543546 |

**DOES_NOT_EXCLUDE_FOR_DIRECTION.** Der vorherige unentschiedene Test aus
#234 ist damit für diesen festen Kandidaten entschieden. Kein Regelbeweis,
kein N12-Abschluss, keine Aussage über alle Schalenrichtungen.

Die Rechnung verwendet die vorhandenen vollständigen Quellen- und Kopplungsgrame
für zwölf U8-Antworten. Sie benötigt keine neuen Funktionsnetze und bezahlt die
Änderung k-k_0 einmal im gemeinsamen Ellipsoid. Ein konservatives Normdreieck
zwischen endlichem und hohem Support bleibt ausdrücklich bestehen.

[Herleitung und vollständiges Budget](PROOF.md).
Exakte rationale Intervalle: `expected/COHERENT_K_EVEN.json`.

```sh
python3 -m pip install python-flint==0.9.0
python3 -B research/x-c1/coherent-k-frozen-even-2026-10-17/verify.py
```

Der Prüfer entnimmt zwei hashgebundene Eingaben direkt dem vorhandenen Stufe-3-Archiv.
Er bestätigt die exakte positive K-Metrik, Zusammensetzungsidentitäten und den
bytegleichen Replay. Er ersetzt keine externe mathematische Begutachtung.
Die ungerade Richtung und alle bisherigen Zertifikatsdateien bleiben unverändert.
