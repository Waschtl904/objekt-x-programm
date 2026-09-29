# Reproduktion der äußeren Masse und Kopplung

## Voraussetzungen und Umfang

- Repository-Checkout mit HEAD exakt `d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`.
- Python 3.13 und Git.
- Für die gerichteten physischen Integrale: python-flint 0.9.0.
- Für die beiden Ganzzahl-/Rationalprüfer genügt die Python-Standardbibliothek.
- Nur zur optionalen Neuerzeugung der A₈-Prüffaktoren: NumPy 2.3.3 und SciPy 1.17.1, wie im ausgeführten Lauf.

Alle Skripte lesen das Repository. Ausgabepfade außerhalb des Repositorys verwenden. Sie wechseln keine Branches und ändern keine Repository-Dateien oder Referenzen. Git wird im Suchpfad gesucht; als Rückfall dient der bekannte Windows-Pfad.

Das Paket bestimmt die 1×1- beziehungsweise 2×2-Außenmassenform der kanonischen Ergänzungen durch rigorose Projektoreinschließungen. Die verwendeten Polynomräume sind Hilfsräume. Ihre Basen werden nicht zu echten Eigenvektoren umbenannt.

## 1. Rationale Schlussprüfung auf gelieferten Daten

Im entpackten Paketverzeichnis:

```text
python verify_outer_mass.py --repo PFAD_ZUM_REPOSITORY --primary primary.json --crosscheck crosscheck.json --transport-reference transport_reference.zip --a8-gap a8_gap_verification.json --a8-proposal a8_gap_proposals.json.gz --out replay-verification.json
```

Der Prüfer kontrolliert den fest gebundenen Referenz-SHA, die vollständigen drei verschachtelten Manifeste, die Repository-Blobs und die Überlappung beider gerichteter Rechnungen. Anschließend berechnet er mit exakten Brüchen und nach außen gerundeten Ganzzahlquadratwurzeln erneut:

1. Rayleigh-Obergrenzen aus den physischen Ritz-Matrizen;
2. Projektorfehler aus diesen Grenzen und den vollständigen Spektral-Gaps;
3. die kleinste Singularwertgrenze der alten/neuen Hilfsraumüberlappung;
4. Abstand und Polarprojektion zwischen Hilfsergänzung und kanonischem E;
5. äußere E-Massenmatrizen, Eigenwertintervalle und Loewner-Faktoren;
6. die absolute geometrische Kopplungsschranke und die Vergleichsgrenze aus bekannter Positivität.

Erfolg endet mit `ALL RATIONAL OUTER MASS AND COUPLING CHECKS PASS`. Dieser Replay setzt die gerichteten Integralintervalle voraus; er baut die ursprünglichen Terminalintegrale nicht neu auf.

## 2. Drei unveränderte Eingangsdaten vorbereiten

```text
python prepare_outer_inputs.py --reference transport_reference.zip --out replay-inputs
```

Dies prüft alle Referenzmanifeste und schreibt ausschließlich die drei fest benannten Dateien `fixed_vectors.json`, `rank_reference.zip` und `transport_verification.json` in den angegebenen Arbeitsordner. Das Referenzarchiv selbst bleibt unverändert.

## 3. Neue A₈-Gaps unabhängig wiederholen

```text
python verify_a8_outer_gap.py --repo PFAD_ZUM_REPOSITORY --reference replay-inputs/rank_reference.zip --proposal a8_gap_proposals.json.gz --out replay-a8-gap.json
```

Der Standardbibliothek-Prüfer verwendet die vollständigen ursprünglichen F- und Kopplungsintervalle. Die parameterabhängige Schurabschätzung, die positive Reparatur und fünf negative Vergleichsrichtungen je Parität werden mit Ganzzahlintervallen bei 200 Dezimalstellen überprüft. Er endet mit `ALL A8 GAP CHECKS PASS`.

Die geprüften physischen Parameter sind 209/50000 (gerade) und 13999/200000 (ungerade). Die Massenschranke 1003/1000 und die früheren Ränge werden aus gebundenen Eingangszertifikaten übernommen.

Nur falls neue rationale Faktoren vorgeschlagen werden sollen:

```text
python propose_a8_outer_gap.py --repo PFAD_ZUM_REPOSITORY --vectors replay-inputs/fixed_vectors.json --out replay-a8-proposals.json.gz
```

Diese Datei danach an `verify_a8_outer_gap.py` übergeben. Die Gleitkomma-Cholesky-Suche ist nur ein Vorschlag; erst der Ganzzahl-Replay zertifiziert ihn.

## 4. Gerichtete Massenberechnungen neu ausführen

Mit installiertem python-flint 0.9.0:

```text
python outer_mass_bounds.py --repo PFAD_ZUM_REPOSITORY --vectors replay-inputs/fixed_vectors.json --transport replay-inputs/transport_verification.json --a8-gap a8_gap_verification.json --bits 1024 --extra-nodes 0 --out replay-primary.json
python outer_mass_bounds.py --repo PFAD_ZUM_REPOSITORY --vectors replay-inputs/fixed_vectors.json --transport replay-inputs/transport_verification.json --a8-gap a8_gap_verification.json --bits 1280 --extra-nodes 8 --out replay-crosscheck.json
```

Die Skripte verwenden 594 beziehungsweise 602 Gauss-Legendre-Knoten. Die Integranden sind Polynome innerhalb der exakten Integrationsordnung. Koeffizienten, Nullfortsetzung, Endpunkte, Momentkorrekturen und Knotengewichte werden gerichtet eingeschlossen. Die zusätzliche Knotenanzahl prüft dieselben exakten Integrale mit einer anderen Quadraturordnung.

Danach Schritt 1 mit `--primary replay-primary.json --crosscheck replay-crosscheck.json` wiederholen.

Falls in Schritt 3 eine frische A₈-Ergebnisdatei verwendet wird, dieselbe Datei in **beiden** gerichteten Läufen und der Schlussprüfung einsetzen. Ihre Hashbindung gehört zu den neuen Eingaben; Laufzeiten ändern den Datei-SHA. Bei neu vorgeschlagenen Faktoren entsprechend auch `--a8-proposal` ersetzen.

## Bedeutung der Ausgabedaten

- `auxiliary_outer_mass_matrix`: gerichtete Außenmassenform auf dem ausdrücklich definierten Hilfsraum F, nicht auf E.
- `canonical_E_basis`: mathematisch definierte L²-Polarprojektion der Hilfsbasis auf das echte E. Numerische Eigenvektoren werden dafür nicht vorausgesetzt.
- `canonical_E_outer_mass_matrix_entry_intervals`: gemeinsame sichere Eintragseinschließungen für die wahre E-Matrix in dieser Basis.
- `loewner_lower_factor_exact` / `loewner_upper_factor_exact`: zusätzlich sichere multiplikative Matrixgrenzen relativ zur wahren Hilfsmatrix.
- `canonical_E_outer_mass_eigenvalues`: maßgebliche positive Spektralintervalle. Das erste Intervall schließt mₒᵤₜ ein.
- `geometric_pulled_back_b_coupling_upper_exact`: absolute Schranke für qᵦ(Tx,e), normiert durch ‖x‖ᵦₐ‖e‖ᵦᵦ; kein κ-Wert.

Der separat gespeicherte Residuentest lieferte keine schärferen Projektorfehler. Die rationale Schlussprüfung verwendet ausschließlich den Energie-/Gap-Nachweis; sie ist nicht von einem Erfolg dieses zusätzlichen Tests abhängig.

## Grenzen der Reproduktion

Die alten Rang- und Transportzertifikate sowie die ursprünglichen analytischen Form-/Tail-Nachweise sind Eingaben. Zwei Präzisionsläufe mit derselben Arb-Implementierung sind keine zwei unabhängig entwickelten Modelle. Der rationale Replay prüft die Schlussfolgerungen unabhängig von Arb, setzt aber dessen gerichtete Integralintervalle voraus.

`primary.log`, `crosscheck.log`, `a8_gap_replay.log` und `rational_replay.log` enthalten die vollständig ausgeführten erfolgreichen Läufe. `SHA256SUMS` bindet alle Paketdateien außer sich selbst. Kein relativer κ-Test und keine neue Terminalpositivität werden behauptet.
