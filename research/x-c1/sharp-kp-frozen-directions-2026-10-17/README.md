# Schärferes K_P für die beiden festen Kandidaten

Die vollständige direkte Form und der bisher weggelassene positive Antwortterm
werden gerichtet berechnet. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN** unter den
gebundenen Operator-, Domänen- und Quellenmodellvoraussetzungen.

| Parität | K_P, nach außen gerundet | neue Schwelle | engeres L |
|---|---:|---:|---:|
| gerade | [0,000213400114547; 0,000213400114550] | [3,314249417943; 3,314249417944] | [−5,961; 8,948] |
| ungerade | [3,911146161770442; 3,911146161770490] | [182,550050826232; 182,550050826233] | [135,497; 169,560] |

**Gerade: INCONCLUSIVE_FOR_DIRECTION. Ungerade: DOES_NOT_EXCLUDE_FOR_DIRECTION.**
Zusätzlich wird das hohe Paarungsbudget aus der gebundenen orthogonalen
Low/High-Koordinatenzerlegung verfeinert; der nichtisometrische Momentlift
bleibt ausdrücklich bezahlt. Es werden keine neuen Paarungen integriert und
keine Kandidaten verändert. Der ungerade Nichtausschluss bestätigt die Regel
nicht und beendet N12 nicht.

Die [Herleitung](PROOF.md) enthält die ganze Autokorrelationsenergie, den
bezahlten Nahbereich, alle sieben Primverschiebungen, den Rest bis unendlich,
die exakte rationale S0-Matrix und den zweiseitigen Modellfehler. Maßgeblich
sind die exakten rationalen Intervalle in `expected/SHARP_K_*.json` (K_P und Vergleich vor dem Nachtrag) sowie
`expected/PROJECTED_HIGH_*.json` (aktueller engerer Vergleich; PROOF §8).

Reproduktion im Repository mit Python 3.12 und den gebundenen Abhängigkeiten:

```sh
python -m pip install -r research/x-c1/sharp-kp-frozen-directions-2026-10-17/requirements.txt
python -B research/x-c1/sharp-kp-frozen-directions-2026-10-17/verify.py
```

Der Prüfer verlangt vier bytegleiche Ergebnisdateien und 24 separate numerische
Autokorrelationskontrollen. Die Quellen stammen ausschließlich aus gebundenen
Repository-Dateien und dem vorhandenen Antwortarchiv. Ein Replay bestätigt
Determinismus und Eingabebindung; die externe mathematische Prüfung bleibt offen.

Der nächste relevante Schritt ist ein engeres endliches/hohes Antwortbudget
für den weiterhin unentschiedenen geraden Kandidaten. Eine weitere Verkleinerung der bereits
winzigen K_P-Integrationsreste würde die Entscheidung nicht ändern.
