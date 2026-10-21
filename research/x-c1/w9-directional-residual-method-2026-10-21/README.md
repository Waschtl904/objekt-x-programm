# Begrenzter Methodenpilot nach #250

Die richtungsbezogene Auswertung vorhandener Featurefehler bringt F(Jw)
unter das Budget. Eine bereits bewiesene Inversabschätzung, angewandt auf
das ganze neue Residuum statt auf nu, vermeidet den ungünstigen globalen
Formboden und die riesigen Kosten der Darstellung X_ans u=w.

Das endliche Restleck ist bezahlt. **Die ganze L-Dualenergie ist offen.**
Ein oberer Nachweis <=1.9e-8 wäre für den festen geraden Zeugen ausreichend;
diese Zahl ist ein Ziel, kein Messergebnis. Keine Regelbestätigung und kein
Abschluss von Punkt 4/N12. AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.

Siehe [PROOF.md](PROOF.md), insbesondere §5 für den begrenzten Folgepilot.
Reproduktion vom Repository-Stamm:

```sh
python -m pip install -r research/x-c1/w9-directional-residual-method-2026-10-21/requirements.txt
python research/x-c1/w9-directional-residual-method-2026-10-21/verify.py --check
python research/x-c1/w9-directional-residual-method-2026-10-21/audit.py
```

Alte Mathematik und Ergebnisdateien wurden nicht geändert. Integration und
externe Prüfung sind nicht durch lokalen Replay ersetzt.
