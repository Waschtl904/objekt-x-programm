# Begrenzte Vorprüfung neuer Antwortmatrizen bei festem W9

18. Oktober 2026. Ausgangspunkt ist #238, Head
`19d27b12c06500e2b1266e560a13f67974991f1d`.
**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**, unter den gebundenen Voraussetzungen.

Die exakte Inverse der A12-Mittelpunktmatrix und das bereits vorhandene
Mittel der gerichteten Invershüllen (`audit_S`) beheben den gescheiterten
Vergleich nicht: Die beiden in #238 eingefrorenen Richtungen schließen auch
diese Varianten aus. Residualänderung, tatsächliches K_P und Fehlerpreise
werden gemeinsam angepasst. Es werden keine neuen Kandidaten gesucht.

| Variante | gerade | ungerade |
|---|---|---|
| X0 aus #238 | Ausschluss bleibt | Ausschluss bleibt |
| Exakte Mittelpunktinverse | Ausschluss bleibt | Ausschluss bleibt |
| Vorhandenes Hüllenmittel S | Ausschluss bleibt, Abstand > 6.3646e-6 | Ausschluss bleibt, Abstand > 1.15545e-7 |
| 0.99 X0 / 1.01 X0 | Transfergrenze unbrauchbar grob | Transfergrenze unbrauchbar grob |

Die letzte Zeile bedeutet **unentschieden**. Die riesige Normmajorante belegt
keinen großen tatsächlichen Fehler und schließt diese Varianten nicht aus.
Ein größeres K_P allein ist ebenfalls keine Verbesserung des Vergleichs.

Keine große Rechnung: nur rationale 12×12-Matrizen, bereits gespeicherte
gerichtete Ergebnisse und Polynom-Stammfunktionen. Keine neue Quadratur,
kein neuer gemeinsamer Paarungslauf und kein R_L-Lauf.

```sh
python research/x-c1/w9-response-preflight-2026-10-18/preflight.py --check
```

`PROOF.md` enthält Dateninventar, gemeinsame Änderungsformeln, den
gerichteten Transfer und den Entscheidungs-/Aufwandsvergleich.
`EXPECTED.json` enthält die rationalen Intervalle; `INPUT_BINDINGS.json`
bindet 16 direkte Dateien sowie einen zusätzlichen Archivbestandteil.
Die 36 Dateien und 20 Archivmitglieder des übernommenen #238-Eingangspakets
werden beim Lauf ebenfalls vollständig hashgeprüft.

**Entscheidung:** Die beiden nahezu identischen Ersatzmatrizen werden nicht
weiter verfolgt. Für eine strukturell andere Matrix fehlen die gewichteten
Antwort- und Kreuzgrame. Aus dieser Vorprüfung ergibt sich noch kein
überzeugender Ersatzkandidat. Als nächster begrenzter Schritt ist deshalb
die zulässige Verschärfung der Inversmajorante zu prüfen; eine neue große
Antwortintegration erhält hier keine Freigabe. Der allgemeine Matrixweg
bleibt offen. Für einen positiven vollständigen Vergleich muss auch R_L
oder eine andere gültige obere Ersatzabschätzung bezahlt werden.

Meilenstein 4, N12 insgesamt und Objekt X bleiben offen. #238 und seine
Zertifikate werden weder geändert noch erneut vollständig integriert.
