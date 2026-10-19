# Vorab festgelegter Diagnose- und Abnahmeumfang

Nur der verstärkte Untervergleich Q_lower,* mit K_*=K+(13/10^8)G_F vom Head a09f052a6c856f6a75f8b9942b9d78f8f6506ea1, derselbe gerade #238-Zeuge und das unveränderte K_P-Budget. Keine Richtungssuche, neue Integration oder vollständige Dualrechnung.

Einmalige Auswahl: 84x84-Mittelpunktsystem H_model w=nu_model, H_model=(D_mid-U_model)_JJ-a0* K_*^-1 a0 (der positive eta-q-Abzug wird konservativ nicht genutzt). Genau eine Lösung, keine Starts/Varianten. Auf 50 Dezimalstellen gerundete rationale Koeffizienten werden vor dem gerichteten Test in CANDIDATE.json eingefroren und committed. Die Skalierung dieses Testvektors wird danach nicht geändert.

Der unabhängige Auswertungslauf verwendet diese exakten rationalen Koeffizienten. Pflicht: Eingabebindungen, K_*-Identität, gemeinsame nu-Identität, vollständige gerichtete Basisenergie, gerichtete Paarung einschließlich a_fin- und ganzer Residualmodellfehler, obere Formschranke am festen Vektor einschließlich D/U/a_fin-Fehler. Die alten F-J-Fehler bleiben unverändert.

Einziger positiver Entscheidungsfall: veröffentlichte rationale Untergrenze > Budgetobergrenze => SCHUR_UNDERFORM_COMPARISON_EXCLUDED. Sonst SCHUR_LOWER_TEST_OPEN, niemals Teilpass oder Dualreserve. Fehler/Timeout führen zu keiner mathematischen Klassifikation. 30 Minuten harte Grenze pro Aufruf.

Pflichtabnahme: frischer vollständiger Repository-Archiv-Replay, getrennte bytegleiche Rekonstruktion der eingefrorenen Auswahl und des Zertifikats; Registry-Validator, deterministische Ansichten, Registry-Tests und Diffprüfung. Historische Pakete unverändert. Veröffentlichung auf eigenem Forschungsbranch ohne Merge. AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.
