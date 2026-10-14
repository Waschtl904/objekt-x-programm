# A9: Domänenherleitung, Gesamtboden und lokale Fortsetzung

Formdichte, vollständige Kern-/Schalenzerlegung und verwendete Operatordomänen für die konkrete Form; bedingter physischer A9-Boden 10^-207 und lokale Fortsetzung bis log(3)+exp(-10^215) mit Boden 10^-421.

**Bedingtes Autorenresultat; externe mathematische Begutachtung offen.**
Die extrem kleine lokale Breite ist kein Übergang A9->A11 und keine kofinale Fortsetzung; die Böden sind konservative Untergrenzen.

- [Vollständiger Beweisanschluss und Voraussetzungen](PROOF.md).
- [Unveränderter Ergebnisbericht](original/BERICHT.txt).
- [Originalherleitung](original/HERLEITUNG.txt).
- [Konkreter Gegenprüfungsauftrag](original/ANSCHLUSS_GPT1.txt).
- [Alle Originaldateien und ihre Hashbindungen](SOURCE_BINDINGS.json).

Vom Repository-Stamm, Python 3.12/3.13, Standardbibliothek:

```sh
python -B -m unittest discover -s tests -p test_a9_sealed_replay.py -v
python -u -B scripts/replay_a9_sealed.py --package research/x-c1/a9-domain-continuation-2026-10-13 --output ../a9-domain-continuation-2026-10-13-check
```

Das Ausgabeziel muss neu und außerhalb des Repositorys liegen. Der Replay
prüft jedes gespeicherte Original, jeden enthaltenen Dateihash und alle lesbaren
Kopien, rekonstruiert das gebundene Schurarchiv und führt den unveränderten
ursprünglichen Prüfer einschließlich Quellenfeldabgleich aus. Die neue Quittung
muss vollständig mit [EXPECTED_SEALED_REPLAY.json](reports/EXPECTED_SEALED_REPLAY.json)
übereinstimmen. Die vollständige rationale Vorgängerkette ist bereits im
globalen Abschluss integriert; ihre großen Integrationen werden nicht neu erzeugt.

Die neuen rationalen Böden, Zwölfermetriken, Basisdaten und Fortsetzungskonstanten werden erneut geprüft.
Die analytische Herleitung wird dabei nicht maschinell bewiesen.
Historische Aussagen wie „GitHub wurde nicht verändert“ beziehen sich auf den
Erstellungszeitpunkt der unverändert aufbewahrten Originale.
