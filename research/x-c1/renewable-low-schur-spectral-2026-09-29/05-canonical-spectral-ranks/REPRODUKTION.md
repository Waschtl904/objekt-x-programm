# Reproduktion der kanonischen Spektralränge

## Voraussetzungen

- Vorhandener Repository-Checkout mit HEAD `d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`.
- Python 3.13. Die neue gerichtete Rechnung verwendet python-flint 0.9.0.
- Der Ganzzahlprüfer braucht nur die Standardbibliothek und Git.
- Nur zur optionalen Neuerzeugung der rationalen Faktoren: NumPy 2.3.3 und SciPy 1.17.1, wie im ausgeführten Lauf.

Git wird im Suchpfad gesucht; als Rückfall dient der tatsächlich verwendete Windows-Pfad. Alle Skripte lesen das Repository. Ihre Ausgabepfade sind außerhalb des Repositorys zu wählen. Es werden keine Branches oder Referenzen geändert.

Die mitgelieferte Datei `fixed_vectors.json` ist unverändert aus dem vorherigen Diagnosepaket übernommen. Sie enthält auch unbenutzte Richtungen. A₈ verwendet die ersten fünf und A₉ die ersten sechs je Parität ausschließlich als rationale Testquellen. Es werden keine neuen Eigenvektoren berechnet.

## 1. Gerichtete Eingaben neu berechnen

Im entpackten Paketverzeichnis:

```text
python spectral_rank_inputs.py --repo PFAD_ZUM_REPOSITORY --vectors fixed_vectors.json --bits 512 --out replay-inputs512.json
python spectral_rank_inputs.py --repo PFAD_ZUM_REPOSITORY --vectors fixed_vectors.json --bits 768 --out replay-inputs768.json
```

Die Rechnung bestimmt die vollständige Kopplungsspur, die Massennorm und die physischen Form-/L²-Grammatrizen bei beiden Terminals neu aus den gebundenen Modellintervallen. Die ursprünglichen Integralmodelle werden dabei nicht neu erzeugt. Es wird weder eine hohe Trunkierung diagonalisiert noch eine Eigenbasis berechnet.

## 2. Ganzzahl-Rangprüfung

Mit den gelieferten gerichteten Eingaben:

```text
python verify_spectral_ranks.py --repo PFAD_ZUM_REPOSITORY --vectors fixed_vectors.json --proposal proposals.json.gz --primary inputs512.json --crosscheck inputs768.json --out replay-verification.json
```

Für die frisch erzeugten Eingaben `--primary replay-inputs512.json --crosscheck replay-inputs768.json` einsetzen.

Geprüft werden:

1. Head, Repository-Blobs, Modellbindungen und vollständige hohe Tail-Bindungen.
2. Einschluss der exakten Formel F = L₀ − eₗI − δ⁻¹Hᵘᵖ durch die gespeicherten Intervalle.
3. Positivität von F−sI+VV* mit s=1/400 durch rationale Faktoren und exakte Normrestschranken.
4. Fünf beziehungsweise sechs positive Intervall-LDL-Pivots für −V*(F−sI)V.
5. Die vollständige Übertragung bei δ=2/3, γ=37 beziehungsweise 61 und ρ=1003/1000 auf μ=17/9999.
6. Der strikt kleinere maximale physische Rayleighquotient des entsprechenden Testraums einschließlich seiner Massenmatrix.
7. Überlappung der gerichteten Einschließungen beider Präzisionsläufe.

Der erfolgreiche Replay meldet viermal `PASS: exact physical rank` und abschließend `ALL SPECTRAL RANK CHECKS PASS`. Maßgeblich sind die rationalen Endpunkte, nicht gerundete Anzeigen. Laufzeiten sind nicht deterministisch.

## 3. Faktoren optional neu vorschlagen

```text
python propose_spectral_ranks.py --repo PFAD_ZUM_REPOSITORY --vectors fixed_vectors.json --out replay-proposals.json.gz
```

Diese Datei danach als `--proposal` im Ganzzahlprüfer verwenden. Die Gleitkomma-Faktorisierung allein ist kein Rangnachweis. Jeder vorgeschlagene Faktor wird vollständig nachgeprüft.

## A₁₁ als bestehende Referenz

`A11_reference.zip` ist das unveränderte vorherige Paket. Seine eigene `REPRODUKTION.md` beschreibt den damaligen 512-/768-Bit-Spektrallauf und den separaten Ganzzahlprüfer. Die neue A₈/A₉-Rangrechnung verwendet weder A₁₁-Eigenwerte noch seine Positivität, um die eigenen Rangzahlen herzuleiten.

`comparison.json` hält den SHA-256 des Referenzarchivs, dessen Verifikationsdatei und die drei Rangpaare fest. Die Prüfung dieser Bindungen und der Rangangaben ersetzt keinen erneuten A₁₁-Spektrallauf; im Bericht wird die Wiederverwendung ausdrücklich benannt.

`SHA256SUMS` bindet alle Dateien dieses Pakets außer der Hashliste selbst. Das ZIP enthält dieselben Dateien. Analytischer Status: AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN. Keine neue globale Positivitäts- oder Renewal-Aussage.
