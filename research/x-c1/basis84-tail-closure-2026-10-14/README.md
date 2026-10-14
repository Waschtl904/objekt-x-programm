# Bedingter Abschluss des ursprünglichen Basis84-Tails

Für beide Paritäten gilt auf dem ursprünglichen W_X-orthogonalen Z84
`tau >= (2/3) W_X` und `A_Z^(-1) <= (3/2) I`. Damit ist das frühere Ziel
1/20 unter den gebundenen Voraussetzungen geschlossen. Der gemeinsame Nachtrag
erhält sowohl das Komplementwechselpaket als auch seine Gegenprüfung.

- [Beweisanschluss, Voraussetzungen und genaue Statuskorrektur](PROOF.md).
- [Originalbericht](original/author/BERICHT.txt) und [Gegenprüfbericht](original/countercheck/BERICHT.txt).
- [Originalarchive und sämtliche Bytebindungen](SOURCE_BINDINGS.json).
- [Vorab festgelegte Abnahme](ACCEPTANCE_PLAN.md).

Vom Repository-Stamm, Python 3.13, Standardbibliothek:

```sh
python -B -m unittest discover -s tests -p test_basis84_tail_replay.py -v
python -u -B scripts/replay_basis84_tail.py --output ../basis84-tail-check
```

Das Ausgabeziel muss neu und außerhalb des Repositorys liegen. Dieser vollständige
Integrationslauf rechnet die 574 Pivots erneut; der schnelle Original-Paketlauf
prüft dagegen deren gespeicherte Quittung. Beide Umfänge werden getrennt ausgewiesen.
Große Integrationen werden nicht wiederholt. Die analytische Gesamtprüfung bleibt
extern offen; nächste Horizonte und Objekt X sind nicht abgeschlossen.

Aussagen der Originale wie „GitHub unverändert“ beschreiben deren Erstellung,
nicht den späteren Integrationsstand dieses Repositorys.
