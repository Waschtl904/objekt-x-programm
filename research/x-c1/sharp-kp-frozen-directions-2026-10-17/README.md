# Schärferes K_P für die beiden festen Kandidaten

Die vollständige direkte Form und der bisher weggelassene positive Antwortterm
werden gerichtet berechnet. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN** unter den
gebundenen Operator-, Domänen- und Quellenmodellvoraussetzungen.

| Parität | K_P, nach außen gerundet | neue Schwelle | unverändertes L |
|---|---:|---:|---:|
| gerade | [0,000213400114547; 0,000213400114550] | [3,314249417943; 3,314249417944] | [−12,293; 15,280] |
| ungerade | [3,911146161770442; 3,911146161770490] | [182,550050826232; 182,550050826233] | [118,635; 186,422] |

Beide neuen Tests sind **INCONCLUSIVE_FOR_DIRECTION**. Die alten Tests mit
gröberen Majoranten waren Nichtausschlusstests; sie entschieden den Vergleich
mit diesen schärferen Schwellen noch nicht. Keine Kandidatenänderung, keine
neue L-Paarung und kein N12-Abschluss.

Die [Herleitung](PROOF.md) enthält die ganze Autokorrelationsenergie, den
bezahlten Nahbereich, alle sieben Primverschiebungen, den Rest bis unendlich,
die exakte rationale S0-Matrix und den zweiseitigen Modellfehler. Maßgeblich
sind die exakten rationalen Intervalle in `expected/SHARP_K_*.json`.

Reproduktion im Repository mit Python 3.12 und den gebundenen Abhängigkeiten:

```sh
python -m pip install -r research/x-c1/sharp-kp-frozen-directions-2026-10-17/requirements.txt
python -B research/x-c1/sharp-kp-frozen-directions-2026-10-17/verify.py
```

Der Prüfer verlangt zwei bytegleiche Zertifikate und 24 separate numerische
Autokorrelationskontrollen. Die Quellen stammen ausschließlich aus gebundenen
Repository-Dateien und dem vorhandenen Antwortarchiv. Ein Replay bestätigt
Determinismus und Eingabebindung; die externe mathematische Prüfung bleibt offen.

Der nächste relevante Schritt ist ein engeres endliches/hohes Antwortbudget
für dieselben eingefrorenen Richtungen. Eine weitere Verkleinerung der bereits
winzigen K_P-Integrationsreste würde die Entscheidung nicht ändern.
