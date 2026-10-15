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

statt `W_X / 65000` bzw. `W_X / 11000` auf ganz `T`. Die A9-Inversmajorante hat
also die Gestalt `C_off W_X^-1 + C_spike (Jv)(Jv)^*` mit `C_off < 5` und
`C_spike ~ 6e4 / 1e4`. Die Uniformitätsforderung (H3) des Reduktionspakets
betrifft an A9 genau eine Richtung.

## Konsequenz für A9->A11

Der Residualpreis `<Rz, U_9 Rz>` ist durch `C_off ||Rz||^2 + C_spike |<Jv, Rz>|^2`
beschränkt. Der gesamte Schwierigkeitsgrad von (H1) liegt im Skalar `<Jv, Rz>`
je Parität; seine Berechnung ist ein billiger Vortest vor den vollständigen
gemeinsamen Energien. Eine erneuerbare Regel muss `Jv` in die endliche
Antwortbasis aufnehmen oder die Budgetlücke in dieser Richtung schärfer
einschließen. Ob `lambda_min(E) ~ 1e-19` echte Kritikalität oder ein
Einschließungsartefakt ist, bleibt offen (PROOF.md, 5c).

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
