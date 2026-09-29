# Reproduktion des A₁₁-Spektralblocks

## Umfang

Dieses Paket zertifiziert den kanonischen Spektralraum unter q/b = 10⁻⁴, seine Dimension und den Gap seines vollständigen Komplements. Es enthält keine numerische echte Eigenbasis, keinen neuen physisch transportierten Spektralraum und keinen neuen κ-Lauf.

`fixed_vectors.json` enthält die alten rationalen **Testvektoren**. `old_projection.json` ist die unveränderte, hashgebundene Projektionsdatei des vorausgehenden Komplement-Pakets. Beide Dateien enthalten aus Gründen der unveränderten Bindung auch die anderen alten Terminals; die neue Rechnung verwendet ausschließlich ihre A₁₁-Einträge.

## Voraussetzungen

- Ein vorhandener Checkout mit HEAD exakt `d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`.
- Python 3.13; für die gerichtete Spektralrechnung zusätzlich python-flint 0.9.0.
- Der unabhängige Ganzzahlprüfer benötigt ausschließlich die Python-Standardbibliothek und die gelieferten rationalen Prüffaktoren.
- Nur zur optionalen Neuerzeugung dieser Faktoren: NumPy und SciPy. Verwendet wurden NumPy 2.3.3 und SciPy 1.17.1. Ihre Gleitkommaergebnisse werden ausschließlich als Vorschläge behandelt.

Die Skripte benutzen den tatsächlich verwendeten Git-Pfad `C:\Program Files\Git\cmd\git.exe`. Auf einem anderen System ist die Variable `git` entsprechend anzupassen. Kein Skript wechselt Branches, ändert Referenzen oder schreibt Repository-Dateien.

## Gerichtete Spektralschranken erneut berechnen

Im Paketverzeichnis:

```text
python true_spectrum_a11.py --repo PFAD_ZUM_REPOSITORY --old-projection old_projection.json --out replay-512 --bits 512
python true_spectrum_a11.py --repo PFAD_ZUM_REPOSITORY --old-projection old_projection.json --out replay-768 --bits 768
```

Die vollständige Isolation der 285 Vergleichseigenwerte pro Parität benötigt mehrere Minuten. Der installierte gerichtete Arb-Eigenwertalgorithmus muss alle Werte einschließen und trennen; ein Scheitern wird nicht als bestanden behandelt. Es wird kein ungeprüfter approximativer Eigenwertmodus verwendet.

Diese Eigenwerte gehören zu F. Die Ausgabe `physical_bounds` entsteht erst durch die im Bericht hergeleitete vollständige Schurvergleichsabschätzung und die physischen Testquellen mit ihrer Massenmatrix. Sie darf nicht mit dem bloßen Spektrum von F verwechselt werden.

## Unabhängigen Rang- und Übertragungsprüfer ausführen

Direkt auf den gelieferten Ergebnissen:

```text
python verify_a11_spectral_cut.py --repo PFAD_ZUM_REPOSITORY --vectors fixed_vectors.json --proposal cut_preconditioners.json.gz --primary spectral_bounds.json --crosscheck spectral_bounds_crosscheck.json --projection old_projection.json --out replay-verification.json
```

Für neue Spektralläufe die beiden `--primary`-/`--crosscheck`-Pfade entsprechend durch `replay-512/spectral_bounds.json` und `replay-768/spectral_bounds.json` ersetzen.

Der Prüfer rekonstruiert F−sI+VV* und −V*(F−sI)V aus den ursprünglichen gepinnten Intervallmatrizen und den rationalen Vektoren. Dafür werden gerichtete Ganzzahlintervalle mit 200 Dezimalstellen benutzt. Die vorgeschlagenen Faktoren R und T werden durch exakte Rest- und Normabschätzungen validiert. Die resultierende Rangzählung setzt die zuvor berechneten F-Eigenwerte nicht voraus.

Die vollständige Kopplungsspur γ und der Massennormbound ρ stammen weiterhin aus der gerichteten Arb-Rechnung. Der Ganzzahlprüfer kontrolliert deren hinreichende Obergrenzen γ < 60 und ρ < 1003/1000 anhand der ausgegebenen rationalen Einschließungen und prüft die anschließende Übertragung auf Q exakt. Die ursprünglichen Terminalintegrale werden nicht neu aufgebaut.

## Prüffaktoren optional neu vorschlagen

```text
python propose_a11_cut.py --repo PFAD_ZUM_REPOSITORY --vectors fixed_vectors.json --out replay-cut-preconditioners.json.gz
```

Anschließend diese Datei mit `--proposal` an den unabhängigen Prüfer übergeben. Die Ausgabe des Vorschlagsskripts allein ist kein Zertifikat. Die exakt gespeicherten rationalen Dreiecksfaktoren, ihre Struktur und alle Restschranken werden erst im Replay geprüft.

## Maßgebliche Daten

- `verification.json / physical_eigenvalue_bounds`: abschließend rational kontrollierte physische μ- und optimale τ-Schranken. Die Untergrenzen sind gegenüber den primären Zahlen zusätzlich um einen Faktor 1−10⁻¹² verkleinert und exakt in die Vergleichsungleichung eingesetzt.
- `true_spectral_projector_rank`: acht je Parität.
- `minimal_rank_for_b_gap_at_least_cut`: acht für die ausdrücklich gewählte Schwelle 1/10000.
- `trial_to_true_projector_leakage_squared_upper_exact`: Lageeinschließung des echten Raums relativ zum alten physischen Testraum; kein behaupteter Eigenvektorfehler auf der winzigen Formenergieskala.
- `repair_floor_exact` und `negative_compression_positive_pivots`: unabhängige Rangzertifikate.
- `bound_source_sha256`: fünf gepinnte Repository-Quellen einschließlich der beiden analytischen Beweisdateien.

Die Hashliste bindet alle Paketdateien. Laufzeiten sind nicht deterministisch. Main, Registry, historische Quellen und vorhandene globale Verifikationsstände bleiben unverändert.
