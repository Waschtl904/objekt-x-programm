# N*Jp-Aufbau und Spike-Orthogonalität (2026-10-16)

**Status:** AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN / RESEARCH_BRANCH_UNMERGED. Art: DIAGNOSTIK mit gerichtet zertifizierten Teilstücken.

## Befund

Fortsetzung des Nachtrags von `a9-inverse-spike-calibration-2026-10-15`: Aufbau von
χ_t = N*Jt für die Spike-Richtung t = v (und p = P_upper v) in vier Stufen und erste
Paarungen mit den zwölf alten Quellen D_j = A9Φ_j der eingefrorenen N12-Regel.

| Stufe | Inhalt | Art |
| --- | --- | --- |
| 1 | Schalenteil χ_v|(a₈,a₉): ‖·‖_X = 2013,598 / 2199,971, Randschicht an a₈ | gerichtet zertifiziert (`940cd40e…`) |
| 2 | innere Quelle f_v = Π8[Q^np ψ_v]: ‖f_v‖ = 237738,80 / 268775,54, Log-Randterm, neun Sprünge | Diagnose (mpmath) |
| 3 | 191 niedrige Koordinaten c der U8-Antwort: ‖c_v‖ = 1,345·10¹³ / 1,022·10¹²; ‖χ_v‖ > 1,34·10¹³ | gerichtet zertifiziert (`ab7116f7…`) |
| 4 | ℓ_v(D_j) = ⟨χ_v, A9Φ_j⟩: Aufhebung auf 10⁻¹⁰ relativ, Rest rigoros ≤ 0,15; hoher U8-Anteil ≲ 10⁻³ | Diagnose (mpmath 150 Stellen) |

Kernaussage: Die riesigen L²-Normen (10¹³, W9-Untergrenze 10³¹) sind Koordinatenartefakte
der weichsten Mode des Common96-Kopfes (Eigenwert ≈ 1,3·10⁻²⁶). In der A9-Energie ist die
Spike-Richtung nahezu orthogonal zu allen zwölf alten Quellen; der untere N12-Skalartest
kann aus dem D12-Anteil praktisch nicht scheitern. Der Energie-Cauchy–Schwarz-Test zwischen
Common96 (Horizont a₈) und den D12-Funktionen (Horizont a₉) ist in allen 24 Fällen bestanden.

## Nicht behauptet

Kein Zertifikat des N12-Tests, keine Paarungen mit der neuen Schale (⟨χ_p, Cz⟩), kein ℓ_e,
kein K_P[z], keine W9-Energie, keine Aussage über A9→A11, Objekt X oder RH. Der kohärente
k-Fehler der Stufe-4-Diagnose ist nicht transportiert. Alle geerbten Voraussetzungen der
gebundenen Pakete werden übernommen, nicht geprüft.

## Reproduktion

```bash
python3 research/x-c1/nstar-jp-spike-orthogonality-2026-10-16/verify.py
```

Standardbibliothek; prüft alle Bindungen und spielt die beiden gerichteten Prüfer
(`certify.py`, `certify_stage3.py`, je 180 Dezimalstellen) gegen das im Repository gebundene
N*Jp-Brückenarchiv bytegenau nach (etwa 10–15 Minuten). Die mpmath-Diagnosen sind hashgebunden
und werden nicht neu gerechnet.

## Dateien

- `PROOF.md` kanonischer Text (SHA-gebunden in `META.yaml`); `reports/` die vier Arbeitsberichte
- `archives/` drei Archive: eigenes Diagnosepaket (Stufen 1–4), Stufe-1-Zertifikat, Stufe-3-Zertifikat
- `original/` sichtbare Kopien der Zertifikatspakete (ohne die 34 MB `inputs/*.gz` des Stufe-3-Pakets) und der Stufe-2-Prüfung (GPT 1)
- `stufe1/`, `stufe2/`, `stufe4/` Skripte und Ergebnisdateien der Diagnosen
- `SOURCE_BINDINGS.json` Hashes aller Dateien, Archivmitglieder und Repository-Abhängigkeiten
