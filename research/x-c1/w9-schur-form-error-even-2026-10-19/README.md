# Fester gerader Schurtest: Formfehler gezielt geschärft

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**, unter gebundenen Voraussetzungen.

Der gemeinsame Feature-Fehlergram senkt den a_fin-Formfehlerpreis von
9.7687e-6 auf höchstens 1.7454980553957797e-8. Der feste Vektor, K_star,
physische Zeuge, Antwortmatrix, K_P-Budget und sämtliche übrigen Fehler
bleiben unverändert. Keine neue Integration oder Richtungssuche.

Gerichtete Untergrenze >55.33955587587e-6, Budgetobergrenze <54.11716937864e-6;
der exakte Abstand ist >1.22238649724e-6.
**SCHUR_UNDERFORM_COMPARISON_EXCLUDED**: Alle oberen Majoranten der Inverse
genau dieser Unterform scheitern an diesem festen Vergleich. Andere
Unterformen/Antwortregeln bleiben offen. Keine negative Weil-Richtung,
kein Teilpass, keine Dualreserve und kein Abschluss von Meilenstein 4.

[Herleitung](PROOF.md) · [Ergebnis](RESULT.json) · [Abnahme](ACCEPTANCE.json)

```sh
python research/x-c1/w9-schur-form-error-even-2026-10-19/verify.py --check
```

Benötigt python-flint 0.9.0. Prüft Hashbindungen, vollständige neue Untergrenze,
unabhängigen rationalen Endpunktaudit und Bytegleichheit. Alte Auswahl,
Integrationen und unveränderte Zertifikate werden übernommen.
