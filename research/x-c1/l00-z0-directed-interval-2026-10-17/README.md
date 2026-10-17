# L₀,₀: vollständiges gerichtetes Intervall für z₀

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**, bedingt auf die gebundenen Operator-, Domänen- und Quellenzertifikate. Baut auf dem Diagnose-PR #230 auf.

| Parität | L₀,₀ | Ausschlussschwelle |
|---|---:|---:|
| gerade | [−407,736; 401,497] | 980,113997 |
| ungerade | [−2,646; 11,832] | 398,766496 |

Dieser gebundene Skalartest mit z₀ liefert keinen Ausschluss. N12 und der volle Energievergleich bleiben offen. Der hohe Anteil wird vollständig durch seine Normschranke bezahlt; kein numerischer hoher Mittelpunkt wird verwendet.

[Herleitung und Fehlerbudget](PROOF.md). Exakte rationale Ergebnisse in `expected/`.

```sh
python3 -m pip install python-flint==0.9.0
python3 research/x-c1/l00-z0-directed-interval-2026-10-17/verify.py
```

Pflichtprüfung: Eingabe- und Eigenbindungen, beide vollständigen Intervallläufe, exakte k₀-Zuordnung, Endpunkt- und analytische Quadraturreste, bytegleicher Replay beider Ergebnisdateien. Externe mathematische Prüfung bleibt offen. Die unveränderten Vorgängerzertifikate sind keine neue unabhängige Prüfung ihrer großen Quellenintegrationen.
