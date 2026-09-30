# Kanonische relative Schurkopplung und Spektralmischung

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.** Vier zusammenhängende lokale Pakete
vom 29.–30. September 2026 werden auf der bereits positiven Kette bis A11
veröffentlicht. Beweisbasis ist `8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b`.
Die operative Übernahme folgt nach der Forschungsintegration in einem
separaten Sync der [Registry](../../../00-uebersicht/RESEARCH_STATE.yaml).

## Ergebnisse und Grenzen

| Block | Ergebnis | Aussagegrenze |
| --- | --- | --- |
| [01 Relative κ-Reduktion](01-relative-kappa/PROOF.md) | Exakte Reduktion auf Energie und inverse Energie des echten kanonischen E | Die dort geerbten konservativen Untergrenzen bestimmen die Nähe zu eins noch nicht |
| [02 Resolventenmomente](02-resolvent-moments/PROOF.md) | Vier rigorose beidseitige Restintervalle; tatsächliche starke kanonische Kopplung | Retrospektiv, unter bereits bewiesener neuer Terminalpositivität |
| [03 Schur-Mechanismus](03-schur-mechanism/PROOF.md) | Ein festgelegter echter Zeuge mischt weit getrennte Spektralenergien und erzwingt starke relative Kopplung | Der Zeuge ist nicht als tatsächlicher Maximierer isoliert |
| [04 Extremalgate und Korollar](04-extremal-gate/PROOF.md) | Verbesserte Restobergrenzen; symmetrisches Problem und exakte Alternativen in einer definierten endlichen Relaxation | Keine Isolation des tatsächlichen Maximierers, kein Entartungsbeweis für den ursprünglichen Operator |

Bei `b=q+17||u||²`, `K_A=ran 1_(0,10^-4)(Q_A(Q_A+17I)^-1)` und
`E=K_B ⊖_b P_B J K_A` sind die echten kritischen Ränge **5→6→8 je Parität**,
die Ergänzungsdimensionen **1 bzw. 2**. κ bezeichnet die **quadrierte**
energiegewichtete Kopplungsnorm. Für die Kompression H der Inversen gilt
`1-κ=1/λmax(D^(1/2) H D^(1/2))`; im Allgemeinen ist H nicht D^-1.

| Übergang | Parität | Restintervall aus Block 02 | Strenge Obergrenze aus Block 04 |
| --- | --- | --- | --- |
| A8→A9 | gerade | [3.2619e-9, 2.1432e-7] | 1−κ < 1.996e-7 |
| A8→A9 | ungerade | [2.0081e-9, 3.1340e-5] | 1−κ < 2.477e-5 |
| A9→A11 | gerade | [5.2319e-17, 3.0103e-12] | 1−κ < 1.371e-12 |
| A9→A11 | ungerade | [3.1660e-17, 3.5804e-11] | 1−κ < 8.005e-12 |

Die Intervalle aus Block 02 sind nach außen gerundet. Der zweite Rest ist
mindestens um Faktor 1000 gerade und 50 ungerade kleiner als der erste.
Eine einzelne tatsächliche Größenordnung und sämtliche absoluten
Terminalverluste sind dadurch nicht bestimmt.

Der Mechanismus benutzt einen zertifizierten Überlapp mit einer schwachen
Hilfsquelle: `|<u,v>|≥α`, `q[u]≤q_j` erzwingen
`<v,Q^-1v>≥α²/q_j`. Die Quelle wird nicht zum Eigenvektor erklärt.
Die bandweisen Schlüsse betreffen gewöhnliche bzw. inverse **Energieanteile**,
keine L2-Massenanteile. Der alte/neue Trialüberlapp bei A9→A11 ist gerade
größer als 0.9999, ungerade etwa 0.999882932 und damit kleiner als 0.9999.

Für das zweidimensionale Extremalproblem wird
`R0 x=β M0 x`, `M0=B0 L0^-1 B0=C C*`, symmetrisiert zu
`K=C^-1 R0 C^-*`. Die vorhandenen Intervalle erzwingen in keiner Parität
einen positiven Eigenwertabstand. Exakte Alternativen in der ausdrücklich
aufgelisteten gemeinsamen endlichen Zertifikatsrelaxation erlauben verschiedene
Maximierer; ungerade ist dort sogar `R0=β M0` möglich. Eine Realisierung durch
die vollständigen ursprünglichen Operatoren und Projektoren ist nicht bewiesen.
Diese Alternativen sind daher kein No-Go für den ursprünglichen Operator.

## Originale, Quellen und Reproduktion

Alle 41 Originaldateien, vier Referenzarchive und ursprünglichen Hashlisten
bleiben bytegleich. `PROOF.md` ist jeweils eine bytegleiche Berichtskopie;
META, diese Übersicht und der gemeinsame Replay sind die Integrationsschicht.
Historische offene Fragen oder Formulierungen wie „nur lokal“ beziehen sich
auf den jeweiligen ursprünglichen Durchlauf. Block 02 beantwortet die in
Block 01 noch offene Kopplungsfrage; Block 04 ergänzt das Korollar getrennt.
Der verworfene Entwicklungsstand `work/canonical-resolvent-primary.json`
ist keine Eingabe und wird nicht veröffentlicht.

[SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) und [SHA256SUMS](SHA256SUMS)
binden Originale, Archive, Integrationsdateien und die Repository-Eingaben.
Die Quellen werden gegen den Beweiscommit und den aktuellen Checkout geprüft.
Der portierbare Replay erzeugt einen isolierten Checkout am Beweiscommit und
führt die unveränderten vier rationalen Prüfer aus. Die Ergebnis-JSONs müssen
inhaltlich und bis auf plattformübliche Zeilenenden bytegleich sein.

Mit Python 3.13 und Git:

```text
python -m pip install -r research/x-c1/canonical-schur-coupling-2026-09-30/requirements.txt
python research/x-c1/canonical-schur-coupling-2026-09-30/replay.py --output /NEUER/PFAD/canonical-replay
```

`--verify-only` prüft ausschließlich Hashlisten, Archivinhalt und Quellen.
Der normale Lauf kontrolliert zusätzlich alle vier gespeicherten Zertifikate
und die fünf Intervall-Randfälle mit python-flint 0.9.0. Die vollständigen
großen Arb-Läufe bei 1024/1280 Bit sind bereits abgeschlossen und als
unveränderte Eingaben gebunden. Die neue CI wiederholt diese großen Lösungen
und die ursprünglichen Terminalintegrale nicht. Die rationalen Schlussprüfer
sind kein zweiter unabhängiger großer Matrixsolver. Die ursprünglichen
Reproduktionsanleitungen und der Solver bleiben vollständig verfügbar.

## Abnahme und nächster Forschungsblock

Verpflichtend für diese Integration: alle Original-/Archiv-/Familienhashes,
Git-Quellenbindungen, vier rationale Replays mit Ergebnisvergleich, fünf
Intervall-Randfälle, Registry-Validatoren und Regressionen, historischer
Frontcheck sowie sämtliche anwendbaren GitHub-Checks am finalen PR-Head.
Nach dem Merge werden der tatsächliche Main-Commit, der Zertifikatreplay
einschließlich Artefaktinhalt und die Registry-CI geprüft. Für den folgenden
Registry-Sync gelten dessen Validatoren, Regressionen, generierte Ansichten
und die durch die bestehende CI-Klassifikation bestimmte Route.

Der nächste fachliche Schritt sind zusätzliche gekoppelte Projektor- und
Überlappbeziehungen zwischen Y, N und den Momenten, die die endlichen
Alternativen ausschließen und eine tatsächliche Maximierer-Isolation erlauben.
Ein unabhängiger vorwärts gerichteter Renewal-Satz, kofinale Positivität,
globales Objekt X, volle Weil-Positivität und RH bleiben offen. Die separate
q11/A13-Vorbereitung aus PR #187 ist keine Eingabe. Historische Beweisanker
und der globale Verifikationssnapshot bleiben erhalten.
