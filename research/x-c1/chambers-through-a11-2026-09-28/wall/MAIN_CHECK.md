# Main-Abgleich zur Quellenbindung

27. September 2026

Beim ersten Abgleich stand Main auf `74b753f52b1d1655507811d23790330250cf1b02`.
Seit dem im A9-Paket beobachteten `a77950be...` waren ein kumulativer Audittext
und zwei Korrekturen seiner Darstellung hinzugekommen.

Während dieser Arbeit wurde zusätzlich
[PR #177](https://github.com/Waschtl904/objekt-x-programm/pull/177) integriert.
Der abschließend für die Quellenbindung gelesene Stand ist
`7f154559fef92d16b890d24e1ae86faa8f4f6d87`.
Der Vergleich zu `a77950be...` enthält sieben Commits und drei betroffene Dateien:

- den kumulativen Audittext;
- NEU-220f: Unterscheidung des definierten Gamma-Phasenoperators
  `+i S*∂S` vom üblichen Wigner-Smith-Vorzeichen `−i S*∂S`;
- NEU-220g: Präzisierungen zu adelischen Nullschnitt-Restriktionen und zur
  Stetigkeit beziehungsweise Typisierung von Punktauswertung/Augmentation.

Die Änderungen wurden inhaltlich gelesen. Keine gebundene C1a-, O10- oder
A9-Eingabedatei ist betroffen. Das neue Lemma verwendet die ausdrücklich
definierte nichtnegative Gamma-Reihe, physische Quellen und endliche
gekoppelte Prime-Symbole. Es benötigt weder die korrigierte
Zeitverzögerungsinterpretation noch eine der adelischen Augmentationsbehauptungen.

Dieser Abgleich bestätigt die Bedeutung der konkret verwendeten Eingaben.
Er ist kein neuer Gesamtaudit der frühen adelischen Konstruktionen.
Die Quellencommits bleiben unverändert gebunden; der spätere Main-Commit
ersetzt keinen mathematischen Verifikationsanker.

`MAIN_CHECK.json` und `inputs/REVIEWED_MAIN_CHANGES.json` enthalten den
commitgebundenen Vergleich. Der lokale Repository-Arbeitsbaum wurde nicht geändert.
