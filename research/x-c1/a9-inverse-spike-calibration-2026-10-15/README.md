# A9-Inversspektrum: Ein-Richtungs-Verstärkung (2026-10-15)

**Status:** AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN / RESEARCH_BRANCH_UNMERGED. Art: DIAGNOSTIK mit exakten Zertifikaten.

## Befund

Die „schwierige endliche Verstärkung" der A9-Inversen, die rationale 84x84-Matrix
`P_upper` je Parität aus dem gebundenen A9-Inversarchiv, ist bis auf eine Richtung
von Ordnung eins. Exakt rational zertifiziert:

| Parität | Zerlegung | Schärfe | Ursprung |
| --- | --- | --- | --- |
| gerade | `P_upper <= 56620 v v^T + 2.1 I` | `v^T P v = 56619.81`, `w ⊥ v: w^T P w = 2.0448` | `lambda_min(E) <= 4.2e-19` |
| ungerade | `P_upper <= 9373 v v^T + 0.37 I` | `v^T P v = 9372.44`, `w ⊥ v: w^T P w = 0.3516` | `lambda_min(E) <= 8.3e-18` |

Bedingt auf die Identitäten (1.1), (2.4), (3.3) des A9-Pakets folgt auf dem
`W_X`-orthogonalen Komplement **eines** Vektors `J v` je Parität

```text
H_* >= W_X / 4.68 (gerade),   H_* >= W_X / 2.77 (ungerade)
```

statt `W_X / 65000` bzw. `W_X / 11000` auf ganz `T`. Das ist eine obere Hülle
des Summanden `H_*^-1` der A9-Majorante, kein unteres Gewicht der vollen `W9`
(die zusätzlich A8-Energie, Zwölferenergie und Quellentransformation `N`
enthält).

## Korrekter Anschluss (korrigiert am 16. Oktober)

Oberer Diagnoseskalar `<Jv, N R_hat z>` mit der Quellentransformation `N`;
unterer Ausschlusstest `R* W9 R >= (11/10) |<Jp, N R z>|^2 / q` mit
`p = P_upper v`, `q = v* P_upper v`. Keine Aussage über ein Scheitern der
eingefrorenen N12-Regel. Ob `lambda_min(E) ~ 1e-19` echte Kritikalität oder ein
Einschließungsartefakt ist, bleibt offen (PROOF.md, 5e). Die erste Fassung
enthielt hier unbegründete Dominanz- und Vererbungsaussagen; siehe
Korrekturvermerk in PROOF.md.

## Nachtrag 16. Oktober

Gebunden: Budgetpaket `7f712994…beb1f5e` (Artefaktfrage: kein Artefakt, `u*E u`
relativ zu `u*D203 u` 2.9 ppm / 17 ppm, M-Fehlerpreis 0.88 % / 0.0056 %;
untere Verstärkung der reduzierten Vergleichsinversen auf `JXu` > 55000 / 9300)
und N*Jp-Paket `b48e3895…6d57b` (Funktionsdefinitionen, `U8`-Aktion, `Jt`- und
`k`-Einschließungen für `t = v`, `P_upper v`). Konditionszahl von `E` korrigiert
(ungerade `1.2e17`). Replay beider Pakete: `scripts/replay_spike_budget_nstar.py`.
Offen: `chi`-Integrale und Ausschlusstest.

## Nicht behauptet

Keine neue A9-Schranke, keine A11-Aussage, kein Beweis von `H_9`, keine
Deutung der Fast-Nullrichtung, keine Prüfung der analytischen A9-Voraussetzungen.

## Reproduktion

```bash
python3 research/x-c1/a9-inverse-spike-calibration-2026-10-15/verify.py
```

Standardbibliothek, exakte Bruchrechnung, etwa 2,5 Minuten. Liest das SHA-gebundene
A9-Archiv aus dem Repository und die rationalen Zeugen in `WITNESSES.json`.

## Dateien

- `PROOF.md` kanonischer Text (SHA-gebunden in `META.yaml`)
- `WITNESSES.json` rationale Zeugen `v_hat`, `w_orth`, `u_E_min`, `u_E_second` je Parität
- `verify.py` exakte Kontrollen
