# Richtungssuche neu bilanziert

**EXPLORATORY / EXTERNAL_REVIEW_OPEN.** Ungerichtete Raumdiagnose nach #235;
die früheren gerichteten Einzelzertifikate bleiben unverändert.

116 alte Suchläufe neu bewertet, 73 neue gerade und 72 neue ungerade Starts.
**Keiner erfüllt das vorab festgelegte Auswahlkriterium:** positive Marge von
mindestens 1 Prozent der Schwelle, positiv bei beiden Auflösungen und größer
als das Zehnfache der beobachteten skalaren Kontrollabweichung.

| Diagnose | gerade | ungerade |
|---|---:|---:|
| beste neue Marge | −0.068445 | −0.045654 |
| maximales I_0-/Schwellenverhältnis des numerischen Raums | 0.918952 | 0.863890 |
| zusätzliche Modellmajorante mit vorhandenen Supportbudgets | 0.998543 | 0.926109 |

Die Raummajoranten sind **nicht gerichtet zertifiziert**. Insbesondere die
kleine gerade Reserve von rund 0.15 Prozent erhält keine Beweiswertung.
Es wird kein neuer Kandidat eingefroren und keine teure Einzelzertifizierung
gestartet. Weitere Verengung des abgeschlossenen Kandidaten wird zurückgestellt.

Nächster sinnvoller Arbeitsumfang: vollständige W9-Residualfeatures und
gewichtete Modellfehler bilanzieren, dann den Energievergleich diagnostisch
aufbauen. Der Rang-eins-Skalar bildet nur einen Teil dieser Energie ab.

[Herleitung, Kontrollen, Grenzen und Datenbedarf](PROOF.md).
Numerische K-Grame, gemeinsame Transportmatrizen und sämtliche Ranglisten in `data/`.

```sh
python3 -m pip install -r research/x-c1/shell-search-reassessment-2026-10-17/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 -B research/x-c1/shell-search-reassessment-2026-10-17/verify.py
```

Der Replay nutzt ausschließlich vorhandene hashgebundene Repository-Eingaben
und startet keine Kindprozesse. Er ist keine unabhängige mathematische Prüfung.
