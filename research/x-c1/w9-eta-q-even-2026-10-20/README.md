# Positiver eta-q-Zusatz am eingefrorenen geraden Schurtest

**SCHUR_LOWER_TEST_OPEN — AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.**

- eta q[Jw] liegt in [8.78184963678; 8.78184963679]e-10.
- Aktualisierte Inversenergie-Untergrenze: >53.19429074226e-6.
- Unverändertes Budget: [54.11716936070; 54.11716937864]e-6.
- Der Zusatz deckt weniger als 0.095067 % der bisherigen Lücke. Auch
  seine Obergrenze reicht bei unveränderten übrigen Grenzen nicht aus.
- Kein Teilpass, keine Reserve, kein Ausschluss der neuen Unterform.
  Die feste Young-Familie bleibt ausgeschlossen; Punkt 4 bleibt offen.

Vektor und sämtliche bisherigen Fehlergrenzen aus #248 bleiben unverändert.
Nur zwei vorhandene direkte Formmatrizen werden exakt rational ausgewertet.
Keine neue Integration, Lösung eines Systems oder Richtungssuche.

[Herleitung und begrenzter nächster Kontrollweg](PROOF.md).
Der offene Rest ist die vollständige variationale Residualenergie
||nu_new-H_new Jw||²_(H_new^-1), einschließlich des unendlichen Raums.
Ihre Kontrolle wurde nicht begonnen.

Reproduktion vom Repository-Root, Python-Standardbibliothek:

```text
python -B research/x-c1/w9-eta-q-even-2026-10-20/verify.py --check
python -B research/x-c1/w9-eta-q-even-2026-10-20/audit.py
```

[Abnahmeplan](ACCEPTANCE_PLAN.md), [Quittung](ACCEPTANCE.json),
[Eingabebindungen](INPUT_BINDINGS.json), [exakte Endpunkte](RESULT.json).

Technische Revision vom 21. Oktober 2026: [portable Pfadbehandlung und
verbindliche Regressionstests](PORTABILITY.md). Die historische Quittung
bleibt an ihren ursprünglichen Verifikationscommit gebunden. Die neue
Paketbindung ändert weder mathematische Eingaben noch Ergebnisbytes.
