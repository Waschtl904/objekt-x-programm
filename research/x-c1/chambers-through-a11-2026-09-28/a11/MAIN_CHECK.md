# Abgleich mit den neuen Repository-Korrekturen

**Lesend beobachteter Main:** `fab93ccb77508c1cf0b46ddcfead799549c48813`.
Die lokale Arbeitskopie bleibt auf `69eb8773acd483978e2453019d1e2d5cf009a990`.
Sie enthält nur den vorher bestehenden unversionierten Python-Cache.

Seit dem im Wandpaket dokumentierten Stand `7f154559fef92d16b890d24e1ae86faa8f4f6d87`
kamen [PR #178](https://github.com/Waschtl904/objekt-x-programm/pull/178),
[PR #179](https://github.com/Waschtl904/objekt-x-programm/pull/179) und
Fortschreibungen des kumulativen Audittextes hinzu. Der vollständige Vergleich
liegt bytegebunden als `inputs/REVIEWED_MAIN_CHANGES.json` bei.
Die anschließende Audit-Ergänzung bis zum oben genannten Stand ist vollständig
in `inputs/REVIEWED_MAIN_AUDIT_EXTENSION.json` erfasst und gelesen. Sie betrifft
ausschließlich den kumulativen Text: die endlichen Suzuki-Stufen, deren
Shift-Positivität und die offenen globalen Übergänge. Die A11-Eingaben bleiben
auch in diesem weiteren Vergleich unverändert.
Der letzte Vergleich ab `26ed5597a487a585f2e06c38c7441a575d1687b1` enthält
zusätzlich [PR #180](https://github.com/Waschtl904/objekt-x-programm/pull/180)
und dessen Audit-Ergänzung. Er ist vollständig unter
`inputs/REVIEWED_MAIN_P02_P03_AUDIT.json` gespeichert und gelesen.

## Geprüfte Bedeutung für A11

- **PR178:** In NEU-255/256 werden Fourier-Shift, Gamma-Vorfaktor und die
  Abfallbehauptung für Schwartz-Funktionen korrigiert. Die A11-Rechnung
  verwendet den unveränderten expliziten Gamma-Kern der gebundenen
  Universalform, die unitäre Fourierkonvention und gerade Symbole. Sie
  verwendet weder den fehlerhaften historischen Vorfaktor noch dessen
  Hochfrequenzargument. Die sieben konkreten mathematischen Eingaben sind
  von diesem Diff nicht betroffen.
- **PR179:** NEU-259/260a unterscheiden positive Spektralverschiebungen von
  der Positivität der unverschobenen Weil-Form. Ein gemeinsamer Shift für
  sämtliche Horizonte wird dort als bereits RH-relevant ausgewiesen.
  A11 benutzt die Hilfsnorm q+17||.||² nur auf dem nachgewiesenen endlichen
  Horizont. Die geprüfte Matrixuntergrenze betrifft q selbst, ohne positiven
  Shift. Der allgemeine Tail-Satz erlaubt eine mit dem Horizont wachsende
  Kodimension; er behauptet keinen globalen unteren Boden der Gesamtform.
- **Globaler Haar-L²-Abschluss:** Aus der lokalen Formvollständigkeit wird
  kein Abschluss der globalen Weil-Form auf Haar-L² abgeleitet. Eine solche
  Behauptung ist keine Voraussetzung unseres Arguments.
- **PR180:** P02 verwendet nun konsistent den endlichen adelischen
  Vakuumvektor statt der Integration über alle endlichen Adelen; P03 wird
  dazu synchronisiert. Eine Polterm-Konjugation wird berichtigt und die
  fehlende Positivitätsverstärkung durch surjektiven Pullback explizit
  festgehalten. A11 beginnt mit der festgelegten physischen Quellenform
  und den beiden ursprünglichen Nullmomenten. Es benutzt keinen solchen
  adelischen Port als Positivitätsbeweis. Keine der sieben gebundenen
  mathematischen Eingaben ist in diesem Drei-Dateien-Diff geändert.

Die sieben Eingaben wurden zusätzlich gegen ihre festgelegten Git-Commits
geprüft. Der frühere Main-Abgleich samt Bindungen bleibt unter `inputs/`
erhalten. Der beobachtete Main-Snapshot ist keine Zusage, dass keine weitere
parallele Repository-Arbeit stattfindet.

Dieses Paket enthält lokale Forschungsergebnisse. Es schreibt weder
Main noch Registry und ändert keine Branches, Tags oder historischen Quellen.
