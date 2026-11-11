# Offene native Herkunftsbindungen

Die folgenden Originale werden vom gespeicherten `SHARP_FORCE_SOLUTION_NATIVE`
referenziert. Die lokal vorhandenen November-5-Dateien sind integre Originale
des GPT2-Laufs, aber nicht mit diesen erwarteten Bytes identifiziert.

## QUELLEN_NATIVE.json.gz

- Erwarteter SHA256: `cac088af25f2f1fd3766b7a7517e3990e01c010f48e2e33c77bcfab8b7693a94`.
- Tatsächlicher SHA256: `c583d6e6667baab0206c1682f640603b085d6f3b26584b716787363f3946ff2c`.
- Betroffene Felder: `roots`, `cell_moments.left/right`, `lowq`, `square_q`, `mc`, `mu`, `gamma`, `eh`, `cross_raw`, `low12`, `me`, `source_errors[1]`.

## KRAFT_UND_LOESUNG_NATIVE.json.gz

- Erwarteter SHA256: `054d61c3a8e19d679e521de30c83c29c0903a7e4b6ae447b3af5a4a55500bd5b`.
- Tatsächlicher SHA256: `956736390926af666053805e3bf889f664cee70d26501d664825fe750ac3a960`.
- Betroffene Felder: `raw_QPhi[:,0:3]`, `errors.high12`, `errors.high22`, `solutionq_preconditioned (diagnostic old radius only)`.

## VERWENDETE_PRIMITIVE_NATIVE.json.gz

- Erwarteter SHA256: `1f2faaad525b2b9cdb06632acb9d784c336f6b4580eff9171b774e05fa6de56f`.
- Tatsächlicher SHA256: `edd4f048c83b91c4af729d8ca0e5455b0358061fbc911374ac7f16c690df0123`.
- Betroffene Felder: `degree=1100`, `entries[(endpoint,logs)] selected by saved_primitive_keys_used`.

Die scharfe X12-Ausgabe ist an das Budget gebunden. Offen bleibt die davor
liegende native Herkunft. Betroffen sind der übernommene X12-Vertrag, z2/C2,
der gemeinsame Budgetanschluss unter diesem Vertrag und die spätere Nutzung
der scharfen q-Kraft/-Lösung samt Fehlern. Die erste Restspalte benutzt diese
drei Eingänge nicht. Ihre gezielte Abnahme bleibt in ihrem dokumentierten Scope.

Interne Payload-Prüfsummen oder enthaltene Momentintervalle beweisen keine
Gleichheit aller benötigten Nutzdaten. Benötigt werden genau die erwarteten
Dateien aus `Objekt-X-Ganzkern-Einzelpass-und-GPT1-Abnahme-2026-11-05/lauf/`
oder ein reproduzierbarer, an diese Originale gebundener Nutzdatengleichheitsbeleg.
Die spätere GPT1-Ergebnisabnahme und der neue Zweitspaltennachtrag fehlen
ebenfalls als Originale; ihre Nichterreichbarkeit steht in SOURCE_INDEX.json.

Die Veröffentlichung dieses Bestands schließt keine dieser Lücken.
