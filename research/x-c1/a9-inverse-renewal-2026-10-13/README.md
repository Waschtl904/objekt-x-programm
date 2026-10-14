# A9: erneuerte Inverse und vollständiger hoher Schurrest

Nach zusätzlicher Elimination der Basis84 gilt für den ganzen neuen L-orthogonalen Schurrest mindestens 2/3 W_X; explizite gemeinsame A9-Inversmajorante aus dem vollständigen globalen Residualvergleich.

**Bedingtes Autorenresultat; externe mathematische Begutachtung offen.**
Der Boden 2/3 bezieht sich auf den neuen Rest nach A8, F12 und Basis84; er beweist nicht den alten gesonderten Tailboden 1/20.

- [Vollständiger Beweisanschluss und Voraussetzungen](PROOF.md).
- [Unveränderter Ergebnisbericht](original/BERICHT.txt).
- [Originalherleitung](original/HERLEITUNG.txt).
- [Konkreter Gegenprüfungsauftrag](original/ANSCHLUSS_GPT1.txt).
- [Alle Originaldateien und ihre Hashbindungen](SOURCE_BINDINGS.json).

Vom Repository-Stamm, Python 3.12/3.13, Standardbibliothek:

```sh
python -B -m unittest discover -s tests -p test_a9_sealed_replay.py -v
python -u -B scripts/replay_a9_sealed.py --package research/x-c1/a9-inverse-renewal-2026-10-13 --output ../a9-inverse-renewal-2026-10-13-check
```

Das Ausgabeziel muss neu und außerhalb des Repositorys liegen. Der Replay
prüft jedes gespeicherte Original, jeden enthaltenen Dateihash und alle lesbaren
Kopien, rekonstruiert das gebundene Schurarchiv und führt den unveränderten
ursprünglichen Prüfer einschließlich Quellenfeldabgleich aus. Die neue Quittung
muss vollständig mit [EXPECTED_SEALED_REPLAY.json](reports/EXPECTED_SEALED_REPLAY.json)
übereinstimmen. Die vollständige rationale Vorgängerkette ist bereits im
globalen Abschluss integriert; ihre großen Integrationen werden nicht neu erzeugt.

Die beiden vollständigen 287er-Prüfungen wiederholen 574 positive LDL-Pivots und die neuen Moment-/Inverskonstanten.
Die analytische Herleitung wird dabei nicht maschinell bewiesen.
Historische Aussagen wie „GitHub wurde nicht verändert“ beziehen sich auf den
Erstellungszeitpunkt der unverändert aufbewahrten Originale.
