# Reproduktion des kritischen Spektraltransports

## Umfang

Dieses Paket enthält den analytischen Transportsatz, neue vollständige Komplement-Gaps bei A₉/A₁₁ und daraus abgeleitete b-Normgrenzen für A₈→A₉ und A₉→A₁₁. Die kanonischen Ergänzungsräume werden basisfrei definiert; ein Satz zeigt, dass kein nichttrivialer Ergänzungsvektor im alten Intervall getragen ist.

Numerische echte Eigenvektoren, räumliche Massenprofile, Kanalzuordnungen und ein neuer κ-Test gehören nicht zur ausgeführten Rechnung. Die ursprünglichen Terminalmodelle und ihre analytischen Fehler-/Tail-Nachweise bleiben Eingaben.

## Voraussetzungen

- Python 3.13 und Git.
- Repository-Checkout mit HEAD exakt `d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`.
- Der neue Ganzzahl-Replay benötigt ausschließlich die Python-Standardbibliothek. Alle seine Dateien liegen im Paket.
- Nur zur optionalen Neuerzeugung der Prüffaktoren: NumPy 2.3.3 und SciPy 1.17.1, wie im ausgeführten Vorschlagslauf.

Die Skripte lesen das Repository und verändern keine Dateien oder Referenzen darin. Ausgabepfade außerhalb des Repositorys verwenden. Git wird im Suchpfad gesucht; als Rückfall dient `C:\Program Files\Git\cmd\git.exe`.

## Neuen vollständigen Replay ausführen

Im entpackten Paketverzeichnis:

```text
python verify_spectral_transport.py --repo PFAD_ZUM_REPOSITORY --reference rank_reference.zip --proposal gap_proposals.json.gz --out replay-verification.json
```

Der Prüfer liest das Referenzarchiv und dessen eingebettetes A₁₁-Paket direkt; ein Entpacken ist dafür nicht erforderlich. Der erwartete SHA-256 des Referenzarchivs ist im Prüfer festgehalten. Beide Manifeste werden vollständig überprüft. Die Modell-, Rang-, Massen- und analytischen Formnaturality-Bindungen werden auf den gepinnten Commit zurückgeführt.

Anschließend werden für beide Paritäten bei A₉ und A₁₁ rekonstruiert:

\[
\mathscr C(t)=F-tI-\frac{t}{\delta(\delta-t)}H^{up},
\qquad t=\frac{1003}{1000}\mu.
\]

Die Positivität von C(t)+VV* wird durch rationale Rest-/Normschranken geprüft. Sechs beziehungsweise acht positive Pivots für −V*C(t)V zählen die negativen Vergleichsrichtungen. Die gespeicherten vollständigen Rangzertifikate liefern die untere Zählrichtung im physischen Raum. Daraus entsteht der verbesserte Komplement-Gap.

Die anschließenden Transportgrenzen verwenden α/β sowie √(α/β) und √(1−α/β). Die sechsstelligen Quadratwurzelgrenzen werden mit Ganzzahlen nach außen gerundet und durch Quadrieren als rationale Ungleichungen überprüft.

Der erfolgreiche Lauf meldet vier bestandene Gap-Prüfungen, vier Transportzeilen und abschließend:

```text
ALL TRANSPORT AND GAP CHECKS PASS
```

`integer_replay.log` enthält das Protokoll des vollständig ausgeführten Laufs. Laufzeiten sind nicht deterministisch.

## Faktoren optional neu vorschlagen

Das Referenzarchiv enthält die unveränderten rationalen Testvektoren. Für einen neuen Vorschlagslauf zuerst in einen separaten Arbeitsordner entpacken:

```text
python -m zipfile -e rank_reference.zip replay-reference
python propose_transport_gaps.py --repo PFAD_ZUM_REPOSITORY --vectors replay-reference/fixed_vectors.json --out replay-gap-proposals.json.gz
```

Die resultierende Datei anschließend als `--proposal` im Ganzzahl-Replay verwenden. Die Cholesky-Suche variiert nur den skalaren Prüfparameter μ. Sie berechnet keine neuen Vektoren. Die vorhandenen V-Spalten dienen als rationale Prüfquellen und werden nicht als echte Eigenvektoren ausgegeben.

Ein positiver Gleitkomma-Cholesky-Lauf ist kein Zertifikat. Erst der anschließende Replay anhand der ursprünglichen Intervalle beweist die Positivität. Neu vorgeschlagene Schnitte und Faktoren können sich je nach Plattform leicht unterscheiden; jeder erfolgreiche Replay muss alle strikten Ungleichungen selbst erfüllen.

## Herkunft und Grenzen der Unabhängigkeit

- `rank_reference.zip` ist das unveränderte vorherige Rangpaket. Es enthält den ursprünglichen A₁₁-Spektralblock als weiteres Archiv.
- Die vier neuen parameterabhängigen Schur-Zertifikate und ihre Transportgrenzen werden mit einer Ganzzahlimplementierung geprüft.
- Die bereits bewiesenen Ränge und Massennormschranken werden aus ihren gebundenen Zertifikaten übernommen. Deren frühere Arb-Läufe und die ursprünglichen Terminalintegrale werden hier nicht neu ausgeführt.
- Formnaturality, Positivität, das Transportlemma und die Ortsaussage sind analytische Voraussetzungen beziehungsweise Beweise im Bericht. Die Programme sind kein formales Beweisassistenzsystem.
- `verification.json` enthält die exakten rationalen Gap-, Norm- und Singularwertgrenzen und alle Quellbindungen. `PACKAGE_AUDIT.json` protokolliert die Prüfung der gedruckten Grenzen und Paketbindungen.

`SHA256SUMS` bindet jede Paketdatei außer der Hashliste selbst. Das ZIP enthält identische Dateien. Status bleibt AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN; Main und Registry werden durch die Reproduktion nicht verändert.
