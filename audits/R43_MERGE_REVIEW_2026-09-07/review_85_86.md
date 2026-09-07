# Exact-Head-Merge-Review: PR85 / PR86

**7. September 2026 — frische destruktive Prüfung, ausschließlich Forschungsartefakte.**

## Aktuelles Votum und geschlossene Blockerhistorie

| PR | Exakt geprüfter Head | Votum |
|---|---|---|
| 85 | `4381c73e4220953899d8484a0ed58cd4815256d9` | **READY innerhalb des dokumentierten lokalen/endlichen Forschungsumfangs** |
| 86 | `8f49e2397ff991b378600b092ce9b52c26b58fd0` | **READY innerhalb des dokumentierten lokalen/endlichen Forschungsumfangs** |

**Beide PRs sind innerhalb des dokumentierten Forschungsumfangs READY.** Der neue lokale PR86-Head `8f49e2397ff991b378600b092ce9b52c26b58fd0` hat exakt den zuvor mathematisch geprüften Head `a7f00fd6ef4824f2aecc934b52088127112a2b5f` als einzigen Elterncommit. Die enge Nachprüfung bestätigt ausschließlich drei ersetzte `uses:`-Zeilen; Code, Berichte, Berechtigungen und Kommandoumfang sind unverändert. Provenienz: `review_86_pinning_closure_8f49e239.json` und `review_86_pinning_closure_8f49e239.diff`.

**Historie B86-1 — GESCHLOSSEN:** Der ursprüngliche Head `a7f00fd6ef4824f2aecc934b52088127112a2b5f` war wegen `checkout@v4`, `setup-python@v5` und `upload-artifact@v4` in Workflow-Zeilen 16/20/34 **BLOCKED**; sein Workflow-Blob war `0d101a96803c1125ffec8fb46bba7b2ae7897e52`. Der Blocker wurde unmittelbar gemeldet und betraf ausschließlich unveränderliches Action-Pinning, nicht die Mathematik. ([Ursprünglicher Workflow](https://github.com/Waschtl904/objekt-x-programm/blob/a7f00fd6ef4824f2aecc934b52088127112a2b5f/.github/workflows/r43-xband-anchor-recheck.yml))

**Geprüfte Schließung am neuen Head:**
- `checkout@11bd71901bbe5b1630ceea73d27597364c9af683`
- `setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
- `upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`

Der neue Workflow-Blob ist `24b8540571b44431c8226558a9e7d41e9e8a7421`. Die ersten beiden Pins entsprechen PR85; der übergeordnete Agent meldete die Verifikation aller Pins gegen die offiziellen GitHub-Repositories. Diese Nachprüfung prüfte unabhängig den exakten Einsatz und den unveränderten Diff-Umfang, nicht erneut die Upstream-Refs. Provenienz: `review_86_pinning_closure_8f49e239.json`. Dieses READY gilt nur für den genannten neuen Head; kein Publish, Merge oder GitHub-CI-Lauf durch den Reviewer.

## Identität und tatsächlicher Umfang

PR85 besteht gegenüber `3e4e5a73679db9f88624869587c4bd3bc3fec266` ausschließlich aus fünf neuen Dateien; PR86 fügt gegenüber PR85 ausschließlich drei Dateien hinzu. Der spätere Pinning-Fix verändert nur den Inhalt des neuen PR86-Workflows. Am neuen PR86-Head stimmen alle fünf PR85-Blobs, beide PR86-Forschungsblobs und beide Elternskript-Blobs unverändert mit der Erstprüfung überein; auch die neuen Arbeitsdateien entsprechen ihren Git-Blobs und der Git-Status ist sauber. Keine Übernahme einer Prüfung von `fe907714…`, keine Repository-Edits oder GitHub-Schreiboperationen durch den Reviewer. Provenienz: `review_85_86_manifest.json`, `review_86_pinning_closure_8f49e239.json`.

| PR | Vollständig gelesene Datei | Git-Blob |
|---|---|---|
| 85 | [r43-schur-xband-comm.yml](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/.github/workflows/r43-schur-xband-comm.yml) | `2eb779a03a57c572c09d1635a1cf8977fa0762ba` |
| 85 | [P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.md](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.md) | `1fb38e6692e1a289d71cf3f3c15b35f106407198` |
| 85 | [P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.py](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.py) | `d50f249a20c7114ce18c337740c70507dfe863c1` |
| 85 | [P11_R43_SCHUR_XBAND_COMM_2026-09-07.md](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_COMM_2026-09-07.md) | `3f5d0e758fc1578b12e6fa6ab89c37b77e17bb6f` |
| 85 | [P11_R43_SCHUR_XBAND_COMM_2026-09-07.py](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_COMM_2026-09-07.py) | `61e700872e0637dbc34145bf7039f0cac3f0b3f3` |
| 86 | `.github/workflows/r43-xband-anchor-recheck.yml` — neuer lokaler Head `8f49e239…` | `24b8540571b44431c8226558a9e7d41e9e8a7421` |
| 86 | [P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.md](https://github.com/Waschtl904/objekt-x-programm/blob/a7f00fd6ef4824f2aecc934b52088127112a2b5f/audits/P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.md) | `49afc81a489ae93d943cfe86a4e058a79ee84b57` |
| 86 | [P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.py](https://github.com/Waschtl904/objekt-x-programm/blob/a7f00fd6ef4824f2aecc934b52088127112a2b5f/audits/P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.py) | `a76a6529a50caaad36ef32ffecec4f70bc650861` |

Die importierten Elternskripte haben die erwarteten Blobs `237bf3406debcc3d2ec757ce547d3759c55a1fc2` (83) und `bb0ccb9e788bb0949ab1ea01b80ad6f6ce5fef4d` (84); deren unveränderte Assertion-Suiten wurden über `--parents` mit ausgeführt. (COMM-Lauf: `pr85_comm_run.stdout.log`, COMM-Ergebnis: `pr85_comm_run.json`)

## Unabhängige mathematische Prüfung

1. **Symmetrische Amplituden und Ankerdefekt: korrekt.** Aus \(a_i=a_s+e\), \(a_j=a_s-e\), \(c_i=c_s-e\), \(c_j=c_s+e\) folgt durch Ausmultiplizieren über komplexen Hilberträumen
   \[ (I_i+I_j)/2=2\operatorname{Re}\langle a_s,c_s\rangle-2\|e\|^2. \]
   Der negative Mittelwert ist daher nicht die symmetrische Interferenz; PR86 verwendet die gegenüber PR85 insgesamt umgekehrte physische Orientierung, aber konsequent für beide Amplituden, also ohne Energie-/Interferenzänderung. ([Anker-Lemma](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.md), [Recheck-Lemma](https://github.com/Waschtl904/objekt-x-programm/blob/a7f00fd6ef4824f2aecc934b52088127112a2b5f/audits/P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.md))

2. **Kompression nicht unterschlagen.** Die vollständige Operatoridentität
   \[a_i-a_j=R_i\big([T_h,B]\,(T_{-h}-I)+B(T_hT_{-h}-I)\big)v\]
   ist durch unabhängiges Ausmultiplizieren bestätigt; der zweite Term ist bei beliebigen Randdaten erforderlich, auf den getesteten kompakten Hub-Quellenräumen jedoch null. Unsere neue Rekonstruktion ergibt für den ausgelassenen vollen Q-Beobachtungsoperator Frobeniusnorm **1.55054354313**, nicht null; zusätzlich wurden komplexe Gaußinteger-Kontrollen und die exakte Randprojektion \(T_{-2}T_2-I\) geprüft. ([Anker-Beweis](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.md), unabhängige Tests: `independent_exact_head_85_86.json`)

3. **Quellen-Grams und generalisierte Spektren: korrekt begrenzt.** PR86 hebt seine spaltenweisen Hilfsnormierungen mit \(\sqrt G\) tatsächlich wieder auf; die realen Basis-/Operatormatrizen ergeben echte, vor der Quellen-Normierung aufgebaute quadratische Formen, die auch komplexe Koeffizienten zulassen. Unsere eigene Cholesky-Whitening-Auswertung reproduziert alle **27 Anker-/Quellenraumfälle** und prüft die ausgegebenen extremalen Koeffizienten erneut an den tatsächlichen symmetrischen Amplituden. ([Implementierung](https://github.com/Waschtl904/objekt-x-programm/blob/a7f00fd6ef4824f2aecc934b52088127112a2b5f/audits/P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.py), unabhängige Spektren und Zeugen: `independent_exact_head_85_86.json`)

   Für Q, X=8, symmetrisch: \(\epsilon_{sup}=0.0920709415211\), \(I_s/\|a_s\|^2\in[-0.0665525409727,0.135008661320]\), \(V/\|a_s\|^2\in[0.936047713997,1.141533967353]\), \(V/G\in[0.00469652413941,0.0855379955748]\). Damit ist die Interferenz numerisch **vorzeichenindefinit** im vollständigen sieben-dimensionalen Raum, trotz positiver Werte für die drei glatten Q-Quellen; keine allgemeine Positivität oder fast vollständige Auslöschung wird fälschlich behauptet. (unabhängige Spektren: `independent_exact_head_85_86.json`, [begrenzte Aussagen](https://github.com/Waschtl904/objekt-x-programm/blob/a7f00fd6ef4824f2aecc934b52088127112a2b5f/audits/P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.md))

4. **Schur-/Sylvestergewichtung: korrekt.** Der aus vollständiger Graphadjazenz unabhängig extrahierte Stern-Schurterm bestätigt \(K=VAR+MEAN\succeq0\), mit dem Nenner aus **allen** aktiven Kanälen, sowie \(BT=(A+K)^{-1}\). Aus \(QAQ=BT\) folgen die richtige Kommutatorreihenfolge und \(H\widehat D+\widehat D H=\widehat F\), mit \(H=A^{1/2}QA^{1/2}\); die scharfe inverse Norm beträgt **0.686690037106 nur in gewichteter Frobeniusnorm**, die grobe obere Schranke in ungewichteter Frobeniusnorm **1198.11769696**. Der Rang-eins-Sättigungsfall ist nachgerechnet; kein direkter Schluss auf die Beobachtungsseminorm ist erlaubt oder im Text behauptet. ([Schur-/Stabilitätsbeweis](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_COMM_2026-09-07.md), unabhängige Tests: `independent_exact_head_85_86.json`)

5. **Randlemmas: korrekt im festen Proxy.** Der BT-Resolventenkommutator benutzt \(A+K\), nicht \(A\); beide Exkursionsterme der Kompressionsformel bleiben erhalten. Die beobachteten Präbilder liegen bereits im Randkragen; der Grad-/Diagonaleintrag-Beweis für die positive Worst-Case-Untergrenze funktioniert für BU und BT, aber wird nicht auf kanonische Quellen übertragen. Beispielsweise für h=2: Transfernormen **2.85188116353 / 2.13912277777**, konservative positive Untergrenze **0.00905674408441**. ([Randbeweise](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_COMM_2026-09-07.md), unabhängige Randtests: `independent_exact_head_85_86.json`)

6. **Komplexe Normen und Off-grid-Firewall: korrekt.** Die komplexen Tests verwenden \(x^*Ax\), Betragsquadrate und \(2\operatorname{Re}\langle a,c\rangle\), einschließlich nichttrivialer Phasen und nichtunitärer Skalierung; `.T` in Quellen-Grams betrifft tatsächlich reelle Basis-/Operatormatrizen. Der ursprüngliche off-grid COMM-Zweig bleibt ausdrücklich reell; Bandmittelwerte werden dort mit einem expliziten, vorzeichenrichtig interferierenden Rest von Zentrumsauswertungen getrennt. Alle gemeinsamen Zweibreitenwerte und 27 seitenaggregierten Paarwerte stimmen zwischen PR85/86 überein; Q-X8-Sweep neu ausgewertet: Exponent **2.00132710665**, Inter-max/min **1.01715901616**. ([Phasen-Scope](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.md), [COMM-Bridge](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_COMM_2026-09-07.md), 63 Quervergleiche: `cross_implementation_85_86.json`)

## Ausführung des Erststands und Sicherheitsumfang

Die mathematischen Erstläufe erfolgten mit `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`, ohne `-O`; JSON, CSV, stdout/stderr ausschließlich außerhalb des Repositories. Lokale Umgebung: **Python 3.14.3 / NumPy 2.5.2 / SciPy 1.18.1**, also **nicht** die dokumentierte bzw. CI-gepinnte Umgebung 3.13.5/2.3.5/1.17.0; ein GitHub-CI-Lauf wird hier nicht behauptet. (Laufprotokoll COMM: `pr85_comm_run.execution.json`, Laufprotokoll Phase: `pr85_phase_run.execution.json`, Laufprotokoll Recheck: `pr86_recheck_run.execution.json`, Umgebung: `pr86_recheck_run.json`)

| Lauf | Ergebnis | Höchster protokollierter Fehler |
|---|---|---:|
| COMM einschließlich Original-Eltern 83/84 | Exit 0; 1011 gespeicherte Identitätslabels | 4.64814e-12 |
| ANCHOR_PHASE | Exit 0; 724 eindeutige Checks | 4.27550e-14 |
| ANCHOR_RECHECK | Exit 0; 108 CSV-Datenzeilen | 2.76814e-13 |
| Eigene neue Rekonstruktion, keine PR-/Alt-Review-Imports | PASS; 231 numerische Checks + exakte kleine Algebra-Kontrollen | 1.06844e-12 |
| Quervergleich der beiden Implementierungen | PASS; 63 Vergleiche | 2.23432e-15 absolut |

Die Fehlerzahlen haben unterschiedliche Normierungen und sind **keine Intervallfehlergrenzen**. (COMM: `pr85_comm_run.json`, Phase: `pr85_phase_run.json`, Recheck: `pr86_recheck_run.json`, Gegenrechnung: `independent_exact_head_85_86.json`, Quervergleich: `cross_implementation_85_86.json`)

- **PR85-Workflow:** `pull_request`/manueller Lauf, `contents: read`, Checkout auf Event-Head-SHA plus explizitem Head-Gleichheitstest, keine persistierten Credentials; beide offiziellen Actions vollständig SHA-gepinnt, feste Python-/Bibliotheksversionen, feste Kommandos zu den geprüften Skripten und hashgeprüften Eltern. Keine PR-Titel-/Body-Interpolation, keine Secrets oder Registry-/Git-Schreibbefehle. ([Workflow 85](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/.github/workflows/r43-schur-xband-comm.yml))
- **PR86-Workflow, neuer Head:** weiterhin nur Repository-Leserechte, Event-Head-Checkout ohne persistierte Credentials, feste Kommandos und begrenzter Upload der drei benannten Ergebnisdateien; kein `pull_request_target`, keine Secrets, kein Repository-Schreibbefehl. **Alle drei Actions sind jetzt vollständig SHA-gepinnt; B86-1 ist geschlossen.** Der übrige Workflow ist byteidentisch zum geprüften Erststand. Ein expliziter Head-Gleichheitstest sowie feste Runner-/Python-Patchversion bleiben optionale Reproduzierbarkeitshärtungen, keine Blocker. Provenienz: `review_86_pinning_closure_8f49e239.json` und `.diff`.

**Keine erneuten Mathematikläufe beim Pinning-Fix:** Alle sechs Code-/Berichtsblobs und beide ausgeführten Elternskript-Blobs sind unverändert; die oben dokumentierten Ergebnisse bleiben diesen identischen Inhalten zugeordnet. Die Nachprüfung bestand ausschließlich aus Head-/Eltern-/Diff-/Blob- und Workflow-Scope-Prüfung. Provenienz: `review_86_pinning_closure_8f49e239.json`.

## Nicht als Blocker gewertet

Die Dokumente lassen kanonische Quelle/analytisches Q, kontinuierliche oder bewegte Fenster, gerichtete Rundung und Intervallzertifikate ausdrücklich offen; aus den Proxys wird weder Strong Terminal/C6 noch Objekt X/RH oder ein Registry-Status abgeleitet. Das entspricht dem autorisierten Merge von korrekt abgegrenzten Forschungsartefakten: **diese offenen Brücken sind keine Merge-Blocker**. ([PR85-Firewalls](https://github.com/Waschtl904/objekt-x-programm/blob/4381c73e4220953899d8484a0ed58cd4815256d9/audits/P11_R43_SCHUR_XBAND_COMM_2026-09-07.md), [PR86-Firewalls](https://github.com/Waschtl904/objekt-x-programm/blob/a7f00fd6ef4824f2aecc934b52088127112a2b5f/audits/P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.md))
