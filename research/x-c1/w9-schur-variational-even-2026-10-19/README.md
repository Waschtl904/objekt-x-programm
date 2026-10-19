# Variationaler Schur-Untertest: offen

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN** unter gebundenen Voraussetzungen.

Genau der verstärkte K_*-Untervergleich und der bisherige gerade Zeuge.
Ein 84er-Testvektor wurde einmal rational eingefroren; keine adaptive Suche.
Die vollständig bezahlte Untergrenze 4.55882875252e-5 liegt unter der
Budgetobergrenze 5.41171693787e-5: `SCHUR_LOWER_TEST_OPEN`.

Das ist **kein Teilpass und keine Dualreserve**. Die tatsächliche volle
Inversenergie bleibt nach oben offen. Der dominante Preis ist die
Formfehlerkontrolle des a_fin-Terms. Keine negative Weil-Richtung, kein
Majoranten-No-Go, kein Abschluss von N12 oder Meilenstein 4.

[Herleitung](PROOF.md) · [fester Testvektor](CANDIDATE.json) ·
[gerichtetes Zertifikat](RESULT.json) · [Abnahmequittung](ACCEPTANCE.json).

```sh
python research/x-c1/w9-schur-variational-even-2026-10-19/verify.py --check
```

Benötigt Python mit python-flint 0.9.0. Auswahl-Replay und gerichtete
Auswertung sind getrennt; beide Ausgaben müssen bytegleich sein.
Keine neue Quadratur, vollständige RL-Rechnung oder erneute 203er-Inverse.
Kein Merge und keine externe mathematische Abnahme.
