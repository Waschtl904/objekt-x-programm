# Vollständiger Restvergleich am festen geraden Zeugen

**Der restzentrierte Vergleich besteht für den unveränderten geraden Zeugen.**
Unter den gebundenen Voraussetzungen gilt

    Energie < 53.950924907669e-6 < 54.117169360708e-6 < Budget.

Die sichere Reserve beträgt >0.166244453040e-6, rund 0.307 % des Budgets.
Der gemeinsame vollständige Rest erhält die Aufhebungen. Der richtungsbezogene
D/U-Preis und der neue Quellen-Fehlertransport bearbeiten beide Hindernisse
aus #250. Physischer Zeuge, interner Vektor, K_new, Antwort und Budget sind fest.

- [Herleitung und Aussagegrenze](PROOF.md)
- [Vollständiges gemeinsames Ergebnis](whole/WHOLE_RESULT.json)
- [Analytische Rand-, Integrations- und Modellreste](whole/ANALYTIC_CAPS.md)
- [Endliche Vorstufe](RESULT.json) und [rationaler Skalaraudit](AUDIT.json)
- [Vorab festgelegte Abnahme](WORK_ORDER.md) und [Prüfstatus](ACCEPTANCE.json)

Vom Repository-Stamm:

```text
python -u -B research/x-c1/w9-residual-centered-control-even-2026-10-21/verify.py --check
python -B research/x-c1/w9-residual-centered-control-even-2026-10-21/whole_verify.py
python -B research/x-c1/w9-residual-centered-control-even-2026-10-21/test_controls.py
python -B research/x-c1/w9-residual-centered-control-even-2026-10-21/test_whole.py
```

Diese Prüfungen kontrollieren die Bindungen, die endliche Rechnung und den
gespeicherten vollständigen Endpunktaudit. Sie wiederholen keine Integration.
Die vollständige frische Neuberechnung ist ausdrücklich verfügbar:

```text
python -u -B research/x-c1/w9-residual-centered-control-even-2026-10-21/whole_verify.py --recompute
```

Reproduktionsumgebung: Python 3.13.7, python-flint 0.9.0; endliche Rechnung
1024 Bit, Funktions- und Quellenkontrolle 3072 Bit. Der volle Replay baut
beide Kernmodelle und alle 411 Taylorabschnitte neu auf und kann über eine
Stunde dauern. Die ursprünglichen Entwicklungsquellen bleiben unverändert.
Der portable Starter ersetzt genau einen gebundenen historischen Pfad;
die fremden Explorationsabschnitte nach `cuts=[]` in whole_model_integrate.py
werden vom vollständigen Certifier nicht ausgeführt. Laufzeiten in
Abschnittsprotokollen sind keine mathematischen Ergebnisfelder.

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.** Der ganze Grad-11-Raum, ungerade
Parität, Punkt 4, N12 und Objekt X bleiben offen. Die endlichen Offen-Flags
in RESULT.json gehören zum engeren Umfang dieser Vorstufe; maßgeblich für
den vollständigen Vergleich ist whole/WHOLE_RESULT.json. Der Merge ist
ein separater Vorgang und wird hier nicht behauptet.
