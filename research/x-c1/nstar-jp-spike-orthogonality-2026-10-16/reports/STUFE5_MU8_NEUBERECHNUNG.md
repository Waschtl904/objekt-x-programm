# Stufe 5: Neuberechnung mit μ₈ und Normdiagnose

17. Oktober 2026 · NUMERICAL_DIAGNOSTIC_ONLY · externe Prüfung offen

## Neue Paarungen

Die korrigierte Rechnung wurde für beide Paritäten vollständig ausgeführt
(mpmath 1.4.1, 150 Dezimalstellen, 384 Gauss-Knoten je Zelle).
Aktuelle Dateien stehen in `stufe5/recomputed_mu8/`; die früheren Dateien
außerhalb dieses Verzeichnisses bleiben historische Fehlversuche.

| Größe | gerade | ungerade |
|---|---:|---:|
| I₀,p | −3,11964479885967344 | +4,59312241695157234 |
| I₀,v | −0,0000550981140891177 | +0,000490067006679781 |
| Änderung I₀,p durch μ₈ statt μ₉ | −0,000264692686229289 | +0,000785347235558739 |
| ‖h‖ | 0,3387150305 | 0,2947953094 |
| ‖h₈‖ | 0,3385309982 | 0,2934307063 |
| kohärenter ψ-k-Beitrag, diagnostisch | 0,0003549245381 | 0,00001695772098 |

Die separat ausgewertete algebraische Änderung
`−2 λ_total (1/μ₈−1/μ₉) ∫₀ᵃ⁸ m h`
stimmt mit der Differenz auf demselben Netz bis unter 3·10⁻¹⁴¹ überein.
Das bestätigt die Nennerkorrektur, ist kein Quadraturrestnachweis.
Die angezeigten Ziffern sind Rechenprotokoll, keine garantierten Dezimalstellen.
Ein hoher numerischer Rest wird hier nicht zur Verschiebung des Mittelpunktes
verwendet: Das nachfolgende Zertifikat muss bei I₀ zentriert werden und |r|≤R bezahlen.

## Aufklärung der y_f-Normabweichung (Richtung v)

Die aus dem gebundenen ganzen Modellgram gerichteten Modellnormen sind ungefähr
135,23727497710638 bzw. 147,07328274067595. Die ältere Anzeige 135,237 war
abgeschnitten und selbst keine nach oben gerundete Schranke.
Die tatsächliche Quelle benötigt zusätzlich die gebundenen Quellen-/k-Fehler.

| Berechnung | gerade | ungerade |
|---|---:|---:|
| altes Netz, gespeicherte Quellenwerte | 135,2385206620 | 147,0741664801 |
| gebundener ganzer Modellgram (gerundete Anzeige) | 135,2372749771 | 147,0732827407 |

`norm_diagnostic.py` rekonstruiert die grobe Netzrechnung mit 90 Stellen und
vergleicht sie mit dem gebundenen ganzen Modellgram. Die Differenzformel
`‖f‖² + γ_m a_f² − ‖Φ*f‖²` subtrahiert Größen um 10¹⁰. Die Abweichung der
kleinen Restnorm kann daher durch viel kleinere relative Fehler der großen
Normintegrale entstehen. Der gebundene fixed-k-Quellenmodellfehler ist um
viele Größenordnungen zu klein, um diese Abweichung zu erklären; ein Nenner-
oder Horizontwechsel der Modellquelle liegt hier nicht vor.

Zwei gespeicherte Quellenwerte pro Parität, nahe x=0,3 und x=0,8, wurden mit
dem bereits gebundenen direkten Gamma-Integrator `stufe2/qnp_psi.py` bei
55 Stellen neu gerechnet. Die Abweichungen liegen zwischen 3,2·10⁻¹⁵ und
6,9·10⁻¹⁵. Das stützt die Zuordnung zur groben Normquadratur; es zertifiziert
weder das ganze Quellenwertnetz noch einen neuen Integrationsrest.
Die mathematisch belastbare Auflösung lautet: Die alte Netz-Norm war keine
Obergrenze und wird verworfen; maßgeblich sind der gebundene ganze Modellgram
und die separat bezahlten tatsächlichen Quellen-/k-Fehler. Die Anzeige 135,237
war zusätzlich nach unten abgeschnitten. Alle Rohterme und Vergleiche stehen
in `YF_NORM_DIAGNOSTIC_*.json`. Es werden keine externen Library-Archive oder
Implementierungen in diesen PR übernommen.

## Vollständiger Budgetansatz und Übergabe an die gerichtete Rechnung

Für h=(C_p−D̂T)z₀ und h₈=Π₈h gelten unter den gebundenen Voraussetzungen

    L₀,₀ ∈ I₀ + [−Eψ−Ec−R, Eψ+Ec+R],
    Eψ = sqrt(b_F* G_p b_F),  b_F=F*h,
    Ec = e_Psi / sqrt(1−rho) · ‖C*Phi*h₈‖,
    R = H_hi,p · ‖h₈‖.

Erforderliche und einzeln nachzuweisende Fehlerquellen:

| Quelle | Behandlung |
|---|---|
| Modellkoeffizienten, transzendente Konstanten, Rechenrundung | vollständige Intervallauswertung der gebundenen Koeffizienten |
| F̂z₀ und Tz₀ | analytische Logmomente mit Taylorrest; Transport durch eingefrorenes X_fix |
| Kern- und Schalenintegrale | alle Sprungstellen als Zellgrenzen, analytischer Gauss-Rest |
| logarithmischer Endpunkt a₉ | explizite Integration einer Logmajorante bis zum Endpunkt |
| tatsächliches k in ψ | kohärentes Eψ mit eingefrorenem k₀, kein zusätzlicher alter e_ψ-Term |
| tatsächliche endliche Antwort c | Ec mit fixed-k- und k-change-Featurefehlern einschließlich Gamma-/Quellenmodellen |
| ganze hohe Antwort | R aus dem gebundenen hohen Normzertifikat; keine endliche Hochraumabschneidung |
| D−D̂ beim Vergleich zur tatsächlichen Regel | bereits separat in der gebundenen Ausschlussschwelle berücksichtigt |

Korrelationen werden nicht als Unabhängigkeit behandelt. ψ-, endlicher und
hoher Antwortfehler werden konservativ per Dreiecksungleichung summiert.
Nur der ψ-Anteil nutzt hier die exakte kohärente Zwölfermetrik; ein vollständiger
kohärenter Transport durch alle U₈-Antworten wird nicht behauptet.
Dieser Diagnose-PR zertifiziert die Tabelle noch nicht. Die gerichtete
Auswertung, der Beweis des Integrationsrestes und ein Replay werden getrennt
bereitgestellt. N12, weitere Schalenrichtungen und der ganze Energievergleich bleiben offen.

## Reproduktion und Pflichtprüfungen

Vom Repository aus:

```sh
P=research/x-c1/nstar-jp-spike-orthogonality-2026-10-16
python3 "$P/stufe5/prepare_inputs.py" /tmp/objekt-x-stage5-inputs
OBJEKT_X_STAGE5_INPUTS=/tmp/objekt-x-stage5-inputs OBJEKT_X_STAGE5_OUTPUT=/tmp/objekt-x-stage5-output python3 "$P/stufe5/l00.py" even
OBJEKT_X_STAGE5_INPUTS=/tmp/objekt-x-stage5-inputs OBJEKT_X_STAGE5_OUTPUT=/tmp/objekt-x-stage5-output python3 "$P/stufe5/l00.py" odd
python3 "$P/stufe5/test_psi_core.py"
python3 "$P/stufe5/norm_diagnostic.py"
```

Pflichtumfang dieser Revision: beide vollständigen Diagnoseläufe, Nennerregression,
algebraische Änderungsidentität, Normdiagnose, Hashbindungen, Beweisanker,
Registry-Validator und anwendbare CI am neuen Head. Die sieben unveränderten
Zertifikatsreplays prüfen ihre eigenen Aussagen und ersetzen keinen Test von I₀.
