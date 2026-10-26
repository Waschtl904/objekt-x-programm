# Abhängigkeitskarte und konkrete Prüfstufen

Status aller neuen analytischen Anwendungen: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Diese Karte erschließt die Originaltexte; sie fügt keine neue mathematische Annahme hinzu.

| Schritt | Voraussetzungen und genaue Rolle | Originalbelege | Prüfung |
| --- | --- | --- | --- |
| Historischer Funktions- und Domänenanschluss | H1: physische Q-Darstellung, Nullfortsetzungen, Domänen und Momentadjungierte | [H1–H4](historical/HYPOTHESEN.txt), [Quellenkarte](historical/HYPOTHESEN_QUELLEN.json) | Analytischer Abgleich der benannten historischen Anker; kein Rechenlauf ersetzt ihn. |
| Historische Quellen und Inversen | H2: ganze ursprüngliche F-/J-/Phi-Quellen; H3: gebundene Form-, Antwort- und Koerzivitätszertifikate; H4: historische Modell-/Quadratur-/Brückenbelege in ihrem ursprünglichen Umfang | [Quellenbindungen](historical/SOURCE_BINDINGS.json), [tatsächliche Eingänge](evidence/REPRODUCTION_INPUTS.json) | Ursprüngliche Anwendbarkeit getrennt von den neuen Transporten prüfen. Die alte Kraftcap 10 ist keine pauschale neue Fo-plus-T-Cap. |
| Neue globale Unterform | Tatsächliches BB*, neue ganze Kopplungsmajorante, Young-Parameter 1e-16 mit Gegenterm, delta1=1.84298, Fo-Block und Gammareserve 1e-40 I | [Formordnung](proofs/FULL_FORM_ORDER.txt), [Gammareserve](evidence/GAMMA_RESERVE.json), [Koeffizientenbindung](evidence/GAMMA_COEFFICIENT_EXACT_AUDIT.json) | Neue analytische Form-/Domänenprüfung. Der [historische Hochraumreview](historical/high-floor/GPT1-ANALYTISCHE-PRUEFUNG.txt) bestätigt nicht automatisch diese Route. |
| Gemeinsamer 108er-Block | F12, J84 und h12 samt allen Mischblöcken; Quellen-, D-, K- und Arithmetikpreise vor Elimination | [Quellenkette](proofs/SOURCE_INTERFACE_CHAIN.txt), [D-Anwendung](proofs/DIRECT_D_APPLICATION.txt), [Nahnullargument](proofs/NEAR_ZERO_PROOF.txt), [endliche Daten](evidence/SOURCE_ARITHMETIC_CLOSURE.json) | Analytische Fehleranwendung prüfen; danach `audit_closed_source_gap.py` für den rationalen endlichen Abschluss. |
| Koordinaten und Reservematrix | Ein rationales invertierbares B, eine gemeinsame Abbildung y(c)=Y B^-1 c; C=B*GpB und A=C^-1 | [Testabbildung](evidence/COMMON_TEST_MAP_EXACT.json), [Geometrie](evidence/JOINT_TAIL_GEOMETRY.json), [Geometrieprüfer](checkers/joint_tail_geometry.py), [Restlemma](proofs/JOINT_REST_LEMMA.txt) | `joint_tail_geometry.py`: exakte positive LDL-Pivots von C und Inversidentität. `verify_joint_rest_lemma.py`: getrennte algebraische Negativkontrollen an Gegenbeispielen, kein Replay der tatsächlichen Geometrie. Physische Koordinatenzuordnung analytisch prüfen. |
| Ganze Residualnormen | Fo und vollständiges T, neue Quellen-/Metrikpreise, Kernquadratur, innerer Streifen, Konturen und Randstücke | [ganze Anwendung](proofs/WHOLE_SOURCE_APPLICATION.txt), [Konturbeweis](proofs/NEW_CONTOUR_APPLICATION.txt), [Restresultat](evidence/JOINT_REST_BUDGET.json) | Norm-/Energieeinheiten und Koerzivitätsfaktoren prüfen. `verify_handoff.py --directory ...` rekombiniert alle 4.704 gespeicherten Abschnitte und beide Randstücke je Richtung. |
| Gemeinsamer Schluss | H ist tatsächlicher Restgram; theta=sum_ij abs(A_ij) n_i n_j<1, einschließlich aller Mischterme | [Restlemma](proofs/JOINT_REST_LEMMA.txt), [Vergleichssatz](proofs/COMPARISON_THEOREM.txt) | Analytische Spurabschätzung und Variationsidentität; rationale Schlusswerte mit `joint_rest_budget.py` nachvollziehen. |

## Archividentität zuerst

Der separat mitgelieferte Prüfer ist byteidentisch zu
`workspace/work/breakthrough-2026-10-25/verify_handoff.py` im Originalarchiv.
Mit Python 3.13 und nur Standardbibliothek:

```text
python -B Objekt-X-Neuer-Vergleich-Grad11-GPT2-2026-10-26-Pruefer.py --zip Objekt-X-Neuer-Vergleich-Grad11-GPT2-2026-10-26.zip
```

Dieser Aufruf prüft alle Archivmitglieder gegen das ursprüngliche Manifest.
Archivgröße und äußerer SHA-256 stehen zusätzlich in [ARCHIVE_IDENTITY.json](ARCHIVE_IDENTITY.json).

## Gespeicherte rationale Belege rekombinieren

Nach dem Entpacken in einen eigenen Arbeitsordner:

```text
python -B Objekt-X-Neuer-Vergleich-Grad11-GPT2-2026-10-26-Pruefer.py --directory PFAD_ZUM_ENTPACKTEN_PAKET
```

Das prüft Dateibindungen und berechnet den gemeinsamen Restschluss aus den gespeicherten
Belegen neu. Es ist keine frische Integration und keine unabhängige analytische Prüfung.
Ein bereits durchgeführter Autoren-Auslieferungscheck steht in [DELIVERY_CHECK.json](DELIVERY_CHECK.json).

Weitere exakte Prüfungen sind in [REPRODUCE.txt](REPRODUCE.txt) beschrieben. Aus dem
Arbeitsverzeichnis `workspace/work/breakthrough-2026-10-25` einer separaten entpackten Kopie:

```text
python -B audit_closed_source_gap.py
python -B verify_joint_rest_lemma.py
python -B audit_core_geometry.py
python -B audit_whole_kernel_bindings.py
```

Diese Befehle erzeugen Ergebnisdateien erneut; anschließend ist diese Arbeitskopie
nicht mehr ungeändert manifestgebunden. Das ursprüngliche Archiv separat erhalten.
`joint_tail_geometry.py` prüft und erzeugt die Geometrie ebenfalls erneut. Diesen
Aufruf in einer eigenen zweiten Arbeitskopie ausführen: Das neue Laufzeitfeld
ändert den Dateihash, auf den der gespeicherte gemeinsame Restschluss verweist.
Mathematische Ergebnisfelder getrennt vergleichen, nicht die neuen Laufzeiten.
Die Lesekopien unter `checkers/` sind zum Einsehen bestimmt, nicht als vollständige
Standalone-Installation. Ein eventueller frischer numerischer Replay soll erst nach
analytischer Prüfung gezielt begründet werden; diese Veröffentlichung startet keinen.

## Getrenntes Abschlussvotum

Erforderlich ist ein begründetes PASS unter vollständig benannten Voraussetzungen,
ein konkreter Fehler oder UNRESOLVED. Getrennt ausweisen: eigene analytische Prüfung,
historische Übernahmen, Byteprüfung, gespeicherte rationale Rekombination und frischer
Replay. Auch ein positives projektinternes Votum wäre keine externe Begutachtung.
Checkliste 3/10 und Punkt 4 bleiben durch die Bereitstellung unverändert.
