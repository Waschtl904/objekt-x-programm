# Kritische Spektralräume, Transport und kanonische Ergänzungen

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.** Diese zusammenhängende Forschungsfamilie
veröffentlicht sieben lokale Durchläufe vom 28.–29. September 2026 auf der bereits
positiven C1a-Kette bis A11. Die operative Übernahme erfolgt nach der Forschungsintegration
in einem getrennten Registry-Sync; maßgeblich ist die
[Registry](../../../00-uebersicht/RESEARCH_STATE.yaml).

## Beweiskette und Aussageumfang

| Block | Ergebnis | Grenze |
| --- | --- | --- |
| [01 Strukturvergleich](01-structure-comparison/PROOF.md) | Vergleich der Schurmatrizen, rationalen Testquellen und kritischen Diagnoserichtungen | Approximative Eigenvektoren sind keine echten Spektralräume |
| [02 Kritische Kopplung](02-critical-subspace-coupling/PROOF.md) | Retrospektive κ<1-Zertifikate für alte Diagnoseräume der Ränge 1–3 | Benutzt bereits die neue Terminalpositivität |
| [03 Alter Komplement-Gap](03-old-complement-gap/PROOF.md) | 120 Zeugen für die untersuchten alten Räume der Ränge 1–20; diese Wahl liefert keinen robusten Gap | Kein No-Go für alle Räume derselben Dimension |
| [04 Echter A11-Spektralraum](04-a11-true-spectral-space/PROOF.md) | Acht echte kritische Richtungen je Parität bei q/b<10^-4 | Vollständige High-Schur-Elimination, keine bloße Modentrunkierung |
| [05 Kanonische Ränge](05-canonical-spectral-ranks/PROOF.md) | 5→6→8 je Parität bei A8→A9→A11; zusammen 10→12→16 | Endpunktzählung lokalisiert keine Geburt an einer Wand |
| [06 Spektraltransport](06-critical-spectral-transport/PROOF.md) | Injektiver Transport, schärfere Komplement-Gaps und kanonische Ergänzungen E der Dimension 1 bzw. 2 je Parität | Setzt den bereits positiven gemeinsamen Horizont voraus |
| [07 Außenmasse und Kopplung](07-canonical-extension-outer-mass/PROOF.md) | Rigorose äußere L2-Massenintervalle der echten Ergänzungen und absolute Kopplungsschranken | Die geometrische Schranke ist kein relativer Renewal-κ-Wert |

Die Zertifikatsdimensionen 191/296/285 sind von den echten kritischen Spektralrängen
5/6/8 zu unterscheiden. Die Mellinkorrektur ist nicht unitär: physisch maßgeblich
ist das verallgemeinerte Problem mit der Massenmatrix G=M* M, nicht das isolierte
Spektrum einer F-Vergleichsmatrix. Sämtliche Aussagen verwenden die vollständigen
analytischen Form- und Tail-Bindungen der bestehenden O8–A11-Kette.

## Transport und kleine neue Räume

Für b=q+17||·||² und P_A=1_(0,10^-4)(𝒜_A) sei K_A=ran P_A.
Physische Nullfortsetzung J erhält q und b. Auf dem bereits positiven Horizont gilt
mit α_A=sup σ(𝒜_A|K_A), β_B=inf σ(𝒜_B|K_B^⊥):

```math
\|(I-P_B)JP_A\|_b\le\sqrt{\alpha_A/\beta_B},\qquad
\|P_BJx\|_b\ge\sqrt{1-\alpha_A/\beta_B}\,\|x\|_b.
```

Damit ist T=P_BJ|K_A injektiv. Die Nichtabnahme der Ränge folgt unter diesen
Hypothesen; eine allgemeine strikte Zunahme für alle Horizonte wird nicht behauptet.
Die kanonische Ergänzung E=K_B⊖_b TK_A hat Dimension 1 (A8→A9) bzw. 2 (A9→A11)
je Parität. Das robuste Spektralkomplement K_B^⊥ ist q-entkoppelt von beiden
niedrigen Blöcken. Die Kopplung innerhalb K_B bleibt zu kontrollieren:

```math
q_B(Tx,e)=-17\langle Jx,e\rangle_{L^2}.
```

Kleine b-Projektorfehler liefern keine relative Kontrolle der winzigen
q-Energien. Auch ein Cocycle der projizierten kritischen Transporte folgt nicht
automatisch aus dem Cocycle der physischen Nullfortsetzung.

## Jüngster Block: rigorose Außenmasse

Die Intervalle schließen das **Minimum** der äußeren L2-Masse bei L2-Norm eins
auf dem echten kanonischen E ein. Beim zweidimensionalen E ist die Obergrenze
des Minimums keine Obergrenze für jede Richtung.

| Übergang | Parität | dim E | Minimale äußere Masse, nach außen gerundet |
| --- | --- | ---: | ---: |
| A8→A9 | gerade | 1 | [0.9717 %, 2.5620 %] |
| A8→A9 | ungerade | 1 | [5.7863 %, 12.8947 %] |
| A9→A11 | gerade | 2 | [0.1284 %, 1.2872 %] |
| A9→A11 | ungerade | 2 | [2.1727 %, 8.1344 %] |

Der jeweils zweite Außenmasseneigenwert bei A9→A11 liegt in
[30.8802 %, 40.1089 %] (gerade) bzw. [38.6315 %, 57.6612 %] (ungerade).
Die schwächste äußere Richtung liegt damit überwiegend im alten Intervall.
Die Rechnung überträgt rigorose Hilfsraummatrizen durch Projektor- und
Polarabschätzungen auf das echte E; die Hilfsbasis wird nicht als echte
Eigenbasis ausgegeben. Eine Zuordnung zu einzelnen Prime-/Shift-Kanälen fehlt.

## Herkunft, unveränderte Originale und Reproduktion

Alle ausgelieferten Dateien, Logs, Referenzarchive und ursprünglichen Hashlisten
sind bytegetreu erhalten. `PROOF.md` ist jeweils eine bytegleiche Kopie des
ursprünglichen Hauptberichts. Zusätze sind META-Dateien und diese gemeinsame
Integrationsschicht. Historische Formulierungen wie „Repository unverändert“
oder „Außenmasse noch nicht numerisch bestimmt“ beschreiben den damaligen
Durchlauf; Block 07 ist der jüngere Stand. Die Originalmanifeste beziehen sich
auf die Originaldateien; das Familienmanifest bindet zusätzlich die Integration.

[SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) bindet die Quelle
`d16ba43ebb20f2c61f43379fc65d7a9b9dba76de` und die Integrationsbasis
`023e8e27f82510bf2cdeb010b82a51cab80ead37`. Die dazwischenliegenden Änderungen
betreffen P12-Scope, Gesamtüberblick und kumulativen Audit. Die gebundenen C1a-
Quellen sind unverändert. Die getrennte q11/A13-Vorbereitung aus PR #187 ist
keine Eingabe und wird durch diese Familie nicht integriert.

Mit Python 3.13, Git und den [fixierten Bibliotheken](requirements.txt):

```text
python -m pip install -r research/x-c1/renewable-low-schur-spectral-2026-09-29/requirements.txt
python research/x-c1/renewable-low-schur-spectral-2026-09-29/replay.py --output /NEUER/PFAD/replay
```

`--case 1` bis `--case 7` führt einen einzelnen Block aus; `--verify-only` prüft
alle originalen und verschachtelten Manifeste sowie die Commitbindungen.
Der vollständige Replay prüft zuerst die gespeicherten Zertifikate, wiederholt
dann die ausgelieferten Arb-Rechnungen bei beiden Präzisionen und wendet die
zugehörigen rationalen Prüfer auf die neuen Ergebnisse an. Die optionale Suche
nach Prüffaktoren wird nicht wiederholt: ihre fixierten rationalen Vorschläge
werden vollständig validiert. Die approximative Winkelrechnung bleibt Diagnostik.

Der Replay erzeugt einen isolierten Checkout am Originalcommit außerhalb der
Arbeitskopie. Ausschließlich in temporären Skriptkopien ersetzt er den festen
Windows-Git-Pfad durch das verfügbare Git; mathematischer Code bleibt gleich.
Alle frischen Ergebnisse und Logs bleiben erhalten. Originale Terminalintegrale
werden nicht neu aufgebaut; zwei Arb-Läufe sind keine zweite unabhängige Engine.
Der separate Ganzzahl-Replay prüft die darauf aufbauende Zertifikatsarithmetik.

## Offen

Nächster struktureller Schritt ist die energiegewichtete tatsächliche
L2-Überlappung zwischen K_A und E sowie ein relativer κ-Test mit bezahlten
S- und D_E-Energien. Allgemeine erneuerbare Low-Schur-Positivität, weitere volle
Terminals, eine kofinale positive Familie, globales Objekt X, volle
Weil-Positivität und RH bleiben offen. Der globale Verifikationssnapshot und
historische Beweisanker werden durch diese Veröffentlichung nicht verschoben.
