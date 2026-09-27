> Historischer Entwicklungs-/Reproduktionsbericht. Aktueller Paketeinstieg: [O8/O9](../README.md).

# O8: positiver lokaler Reservecheck bei A₈

27. September 2026 · **AUTHOR_DERIVED_LOCAL / EXTERNAL_REVIEW_OPEN**

Die neu eingeschlossenen Matrizen bei **A₈=log(8)/2** bestehen den gerichteten Reservecheck in beiden Paritäten: **jeweils 191 strikt positive LDL-Pivots**. Zusammen mit der dokumentierten Herleitung des vollständigen Formraums, der hohen Reserve und des Fehlerbudgets ergibt sich ein lokaler autorenseitiger Nachweis für die konkrete C1a-Fortführung aus O1–O7.

Ein gemeinsamer rationaler Reserveboden ist

\[
q_A[u]\ge 1{,}2\cdot10^{-29}\|u\|_2^2,
\qquad
I-R_A^*R_A\succeq\eta I,
\qquad
\eta=\frac{24}{23\cdot10^{30}+24}>10^{-30}.
\]

Die Endpunktrechnung gilt zunächst für A=A₈. Die bereits hergeleiteten rohen isometrischen Transporte und die Formnaturality übertragen den Boden auf **1≤A≤A₈**. Die unabhängige analytische Abnahme bleibt offen. Der O8-Status im Repository wurde nicht geändert; O9 und O10 bleiben eigene Aufgaben.

## Ergebnis der tatsächlichen Rechnung

| Parität | Positive gerichtete Pivots | Physischer Reserveboden, ungefähr | Defektreserveboden, ungefähr |
|---|---:|---:|---:|
| Gerade | 191 von 191 | 1,23256343485·10⁻²⁹ | 1,07179429117·10⁻³⁰ |
| Ungerade | 191 von 191 | 8,61066526013·10⁻²⁷ | 7,48753500881·10⁻²⁸ |

Die Dezimalwerte dienen der Übersicht. Maßgeblich sind die gerichteten Intervalle in [reserve_refined.json](reserve_refined.json) und deren exakte rationale Abrundung in [common_reserve.json](common_reserve.json).

Der erste vorgeschlagene Test mit hoher physischer Reserve **1/2** scheiterte: Nach 189 geraden beziehungsweise 190 ungeraden positiven Pivots folgte jeweils ein strikt negativer Pivot. Dieser Befund betrifft die hinreichende Untermatrix. Er widerlegt keine tatsächliche Terminalquelle.

Anschließend wurde die hohe Reserve analytisch auf **2/3** verbessert. Dafür wurden die Gamma-Kernuntergrenze, der konstante Verlust und die Shift-Schranke gezielt verschärft. Elf zusätzliche exakte rationale Vergleiche bestätigen die verwendeten Konstanten. Mit dieser Reserve bestehen **dieselben** L₀-/G₀-Matrizen und **dasselbe** Fehlerbudget den vollständigen Test.

## Was die geprüfte Matrix erfasst

- Neuer Endpunkt, d₂=2/3 und d₄=4/3 exakt; fünf Integrationszellen auf der positiven Intervallhälfte.
- Gamma-Grad 160; neue uniforme Restabschätzung auf 0≤t/2≤21/20.
- Vollständige Kopplungs-Grams einschließlich V², aller Shift-Mischterme und aller Gamma-Kreuzterme.
- Mellinkorrektur auf beiden Seiten der tatsächlichen Kopplung. Die hohe rechte Korrektur wird ausdrücklich im Fehlerbudget bezahlt.
- Gesamter hoher Formraum mit genau 191 niedrigen Koordinaten je Parität. Grad 544 begrenzt ausschließlich den polynomialen Gamma-Anteil; die übrige hohe Antwort wird durch vollständige Integrale erfasst.
- 2048-Bit-Arb-Rechnung, Speicherung mit 100 gerichteten Dezimalstellen und anschließendes erneutes Einlesen der Intervalle.

Mit μ=2, γ_K=(21/10)ε, e_L=4γ_K, e_B=2γ_K+24ε_p und δ=2/3 lautet die tatsächlich geprüfte Untereinschließung

\[
F_{p,\delta}=L_0-e_LI-\delta^{-1}
\left(\frac{1001}{1000}G_0+1001e_B^2I\right).
\]

Die physische Reserve folgt aus σ=1/tr(F⁻¹) und einer oberen Schranke b für die vollständige Kopplungsnorm:

\[
c_{\mathrm{phys},p}=\frac{\min(\sigma_p,\delta)}{4(1+b_p/\delta)^2},
\qquad
\eta_p\ge\frac{c_{\mathrm{phys},p}}{c_{\mathrm{phys},p}+23/2}.
\]

Die vollständige Herleitung steht in [PROOF.md](PROOF.md), insbesondere §§1–4 und §7. Die dortigen §§2–5 erklären zunächst den ursprünglichen 1/2-Test; §7 enthält die ausgeführte Verschärfung und das positive Endergebnis.

## Dateien und Prüfrollen

| Datei | Inhalt |
|---|---|
| [a8_model.json.gz](a8_model.json.gz) | Beide 191×191-L₀- und G₀-Intervallmatrizen, Momente, Gamma-Koeffizienten und Generatorbindungen |
| [reserve_refined_lower_matrices.json.gz](reserve_refined_lower_matrices.json.gz) | Beide vollständig bezahlten Untermatrizen für δ=2/3 |
| [reserve_refined.json](reserve_refined.json) | 20 bestandene Prüfgruppen, sämtliche 382 positiven Pivotintervalle und Reserveumrechnung |
| [refined_tail.json](refined_tail.json) | Elf exakte rationale Vergleiche für den neuen hohen Boden 2/3 |
| [normalization_results.json](normalization_results.json) | 233 Kontrollvergleiche am kleinen Modell N=15, M=16; zusätzliche Zusammenstellung der vollständigen Funktionen durch direkte Integration |
| [reserve_results.json](reserve_results.json) | Erster, gescheiterter hinreichender Test mit δ=1/2; zugehöriger damaliger Checker: check_a8_half.py |
| [input_bindings.json](input_bindings.json) | Herkunft und Hashes der verwendeten Repository-Eingaben |
| [SHA256SUMS](../SHA256SUMS) | Dateihashes des Pakets einschließlich der Herleitung, Prüfer, Matrizen und Protokolle |

Die kleine Kontrollrechnung prüft Skalierung und Zusammensetzung der Modellmatrizen. Sie ist keine zweite unabhängige Implementierung des gesamten 191D-Nachweises. Die analytische Bedeutung der vollständigen Grams und die Formraumidentifikation bleiben ausdrücklich Gegenstand des externen Reviews.

## Reproduktion

Python 3.13 und **python-flint 0.9.0** wurden verwendet. Aus diesem Verzeichnis, beispielsweise in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe refine_tail.py
.\.venv\Scripts\python.exe check_a8.py --high-floor 2/3 --output repeated_reserve.json
.\.venv\Scripts\python.exe check_common_reserve.py
```

Der zweite Prüfer schreibt den erneut berechneten Reservebefund nach `repeated_reserve.json`. `check_common_reserve.py` liest dagegen den ausgelieferten Befund `reserve_refined.json` und prüft seine Bindungen sowie die gemeinsame rationale Abrundung. Der vollständige Neuaufbau der Matrizen ist separat möglich:

```powershell
.\.venv\Scripts\python.exe generate_a8.py --degree 383 --gamma 160 --precision 2048 --output rebuilt_model.json.gz
.\.venv\Scripts\python.exe check_a8.py --model rebuilt_model.json.gz --high-floor 2/3 --output rebuilt_reserve.json
```

Für die kleine Kontrollrechnung wird ihr Eingabemodell mitgeliefert:

```powershell
.\.venv\Scripts\python.exe check_normalization_a8.py --model normalization_model.json.gz --output repeated_normalization.json
```

Die Skripte schreiben lokale Ergebnisdateien. Protokolle enthalten Laufzeiten; die Reproduktionsanforderung sind einschließende Intervalle und die angegebenen positiven Reserveböden, keine identischen Laufzeiten. Für die ausgelieferten Dateien gelten die Hashes in `SHA256SUMS`.

## Provenienz und Repository-Stand

Die mathematischen Eingaben stammen aus dem gepinnten Main-Tree `fb0c6a0b3a73bd1a2039b95f1e65ac8023133f0a` zu Commit `876f9c79d555019217c745923cae3bef5da8af17`. Die gezielt verwendeten Quelldateien sind in `input_bindings.json` mit ihren Repositorypfaden und unveränderten Hashes gebunden.

Die frühere Vorbereitung liegt im Paket unverändert unter `../o8-vorbereitung/`. Ihre Aussagen „noch nicht ausgeführt“ sowie die damaligen Main-/PR-Beobachtungen beschreiben diesen älteren Stand. Maßgeblich für die jetzt ausgeführte Rechnung sind dieser Bericht und `PROOF.md`.

Bei der Fortsetzung wurde Main bereits als **12ccf274de2188fd226eec9cea4f27ccf631acba** zurückgelesen: PR #173 ist integriert und die vorbereitete Kurzbeschreibung übernommen. Dieser Dokumentationsmerge hat die mathematischen Eingabedateien nicht verändert. Im Rahmen der hier dokumentierten O8-Rechnung wurden keine GitHub-Schreibzugriffe, CI-Läufe oder Registry-Promotionen ausgeführt.
