# O10: lokales Beweis- und Prüfpaket

27. September 2026 · Basis `main@69eb8773acd483978e2453019d1e2d5cf009a990`

## Ergebnis

Der [vollständige Beweis](PROOF.md) konstruiert den gekoppelten rohen
`q=8`-Wandübergang für alle `1 <= A <= B <= C <= A9=log(3)`.
Die beiden verschiedenen Wandtransporte sind beschränkt:

- `sqrt(20/21) ||x|| <= ||M^T x|| <= (5/4) ||x||`;
- `sqrt(20/21) ||y|| <= ||M^D y|| <= (11/10) ||y||`.

Bewiesen werden Quellen- und Quotientenverträglichkeit, Fortsetzung auf die
abgeschlossenen Bildräume, beide Cocycle-Gesetze, Defektintertwining und
Formnaturality. Die alten Kammertransporte werden exakt fortgesetzt.
`q=8` tritt erst strikt rechts von A8 ein; bei A9 bleibt `q=9` ausgeschlossen.

Die Herleitung ist lokal abgeschlossen; **externe analytische Prüfung bleibt
offen**. Das Paket wurde noch nicht in das Repository übernommen. Die dortige
O10-Obligation und alle globalen Statuswerte bleiben unverändert.

## Prüfung und Dateien

- [PROOF.md](PROOF.md): analytischer Nachweis einschließlich Vollständigkeit,
  Dichte und sämtlicher Frequenzen.
- [AUDIT.md](AUDIT.md): Abgleich mit den einzelnen O10-Anforderungen.
- [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json): sieben Eingaben mit Commit,
  Pfad und SHA-256.
- [verify_o10.py](verify_o10.py): reproduzierbarer Prüfer, nur Python-Standardbibliothek.
- [CHECK_RESULTS.json](CHECK_RESULTS.json): **68 erfolgreiche exakte Prüfungen**;
  alle sieben Quellenbytes gegen ihre gespeicherten Commits geprüft.
- `SHA256SUMS`: Manifest dieses lokalen Pakets.

Die Kontrollen umfassen rationale Konstanten, formale Symbolidentitäten,
Kreuzterme, strikte Aktivierungsendpunkte, exakte Translationsintegrale und
Mellin-annullierende Testquellen. Ein endliches abstraktes Gegenmodell prüft,
dass positive alte Gramkompression keinen positiven gesamten neuen Carrier
erzwingt. Dieses Modell ist **kein Gegenbeispiel gegen die konkrete Weil-Form**.

Die endlichen Kontrollen ersetzen den analytischen Beweis oder eine externe
Prüfung nicht. Es wurden keine neuen O8-Matrizen berechnet.

Reproduktion aus dem Paketverzeichnis:

```sh
python verify_o10.py --repository PFAD_ZUM_REPOSITORY --output REPLAY_RESULTS.json
```

Die angegebenen Commits müssen im lokalen Git-Repository verfügbar sein.
Ohne `--repository` laufen die algebraischen Kontrollen; die erneute Prüfung
der Quellenbytes wird im Ergebnis ausdrücklich als nicht ausgeführt markiert.
Das Skript liest das Repository und schreibt nur die angegebene Ergebnisdatei.

## Nächster mathematischer Schritt

Für die erste Kammer rechts der Wand fehlt eine positive Reserve auf dem
**gesamten** neuen Terminalraum. Die alte O8-Reserve kontrolliert lediglich
das transportierte alte Bild, dort mit Defektboden mindestens
`(16/25) * 24/(23*10^30+24)`.

Ein nächstes Paket muss die neuen Quellen und ihre vollständigen Kopplungen
kontrollieren. Eine erneute endliche Reduktion braucht eigene Tail- und
Kodimensionsnachweise. Erst nach einer solchen Terminalreserve können die
positiven korrigierten Transporte über die Wand konstruiert werden.

Unbeschränkte/kofinale positive Fortsetzung, globale Weil-Positivität,
Objekt X und RH bleiben offen.
