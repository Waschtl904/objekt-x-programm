# SYN_PROVENIENZ

Stand: 9. August 2026

Dieses Register dokumentiert die Provenienz konsolidierter SYN-Papers.
Es ersetzt weder die NEU-Forschungsknoten noch deren Audits und Patches.

---

## P05 — Relative Prime Channels and Arithmetic Edge Geometry

- **LaTeX-Ziel:** `papers/P05_Relative_Prime_Channels_and_Arithmetic_Edge_Geometry.tex`
- **Kanonische Markdown-Quelle:** `papers/P05_Relative_Prime_Channels_and_Arithmetic_Edge_Geometry.md`
- **Markdown-Status:** `SYN FINAL AUDITED`
- **Markdown-Finalcommit:** `bc49413f`
- **Pass-A-Basis:** Gruppe F (`F1 + F2 + F3 + F4 PASS A COMPLETE`), `PASS-A-PROTOKOLL.md`, Commit `9c23fc49`
- **Knotenbasis:** F1 NEU-039–045/44-Familie; F2 NEU-151–173; F3 NEU-225–227; F4 NEU-250f Patch 1, NEU-250g–r gemäß ordnerübergreifender Provenienz
- **SYN-Primärcheck:** `audits/AUDIT-2026-08-09_P05_SYN_Primaercheck.md`, Commit `54374bdf`
- **SYN-Zweitcheck:** `audits/AUDIT-2026-08-09_P05_SYN_Zweitcheck_Pfadgebunden.md`, Commit `f50f3502`; Urteil `OHNE KONKRETEN GEGENBEFUND`
- **SYN-Disambiguierungen:** `c_p` Kanal-Amplitude; `\kappa_p^{tr}` Transportkoeffizient; `\mathscr K_p^{lift}` Liftkern; `\mathscr Q_p^{quot}` Quotientenraum; `\Pi_p^{(1)}` Rang-1-Projektion; `\pi_p^{sym}` Symmetriedarstellung; `h_p^{conn}` vs. `h_p^{bal}`
- **LaTeX-Prüfart:** reiner SYN-Transferaudit; kein Vollneuaudit der historischen NEU-Knoten
- **LaTeX-Erstcommit:** `e9455dc8`
- **LaTeX-Syntaxpatch:** `9a64120a` — fehlende schließende Klammer in der neuen Quotienten-Notation; rein technisch, keine mathematische Änderung
- **LaTeX-Transferaudit:** `audits/AUDIT-2026-08-09_P05_LaTeX_SYN_Transferaudit.md`, Commit `673ca306`
- **LaTeX-Endstatus:** `SYN FROZEN ✓[K/M]`
- **Auditbefund:** kein Status-, Typ-, Formel- oder Routingkonflikt; offene Punkte bleiben offen
- **Weiterleitung:** P06 Feshbach/Schatten/Spektralmaß; P09 BC/Hochschild-Typfundament; P11 globale nichtorthogonale Gramkopplung und Mediator

---

## P06 — Jacobi–Feshbach and Divisor Graph

- **LaTeX-Ziel:** `papers/P06_Jacobi_Feshbach_and_Divisor_Graph.tex`
- **Kanonische Markdown-Quelle:** `papers/P06_Jacobi_Feshbach_and_Divisor_Graph.md`
- **Markdown-Status:** `SYN FINAL AUDITED`
- **Markdown-Finalcommit:** `1ab1f004`
- **Pass-A-Basis:** Gruppe G (`P06 PASS A COMPLETE — doppelt geprüft`), `PASS-A-PROTOKOLL.md`, Commit `e32cfecb`; technischer Notationsfix `5bd6ff06`
- **Knotenbasis:** historischer Kern NEU-058–090; GX1 NEU-040/045/046–056; GX2 NEU-223–228; P06/P11-Interface NEU-228b/229
- **Targeted-Reaudits:** G-T1 NEU-050 `fbff73d9`; G-T2 NEU-062 `2b6cb2e8`; G-T3 NEU-066 `d8746ea1`; G-T4 NEU-090 `52197cdd`; G-T5 NEU-089 `dd0fd3a3`
- **Pass-A-Zweitcheck:** `audits/AUDIT-2026-08-09_P06_PassA_Zweitcheck_Pfadgebunden.md`, Commit `b40af085`; Urteil `OHNE KONKRETEN GEGENBEFUND`
- **SYN-Primärcheck:** `audits/AUDIT-2026-08-09_P06_SYN_Primaercheck.md`, Commit `b077a814`; zwei lokale Draftkorrekturen, danach kein verbleibender Gegenbefund
- **SYN-Zweitcheck:** `audits/AUDIT-2026-08-09_P06_SYN_Zweitcheck_Pfadgebunden.md`, Commit `7c570498`; Urteil `P06-SYN-ZWEITCHECK OHNE KONKRETEN GEGENBEFUND`
- **SYN-Draftkorrektur:** `10c06c4` — kollektiver Koppler `V_N` als Zeilenoperator statt orthogonaler Ziel-Direktsumme; Bipartitheit nur als hinreichende Zusatzbedingung
- **LaTeX-Prüfart:** reiner SYN-Transferaudit; kein Vollneuaudit der historischen NEU-Knoten
- **LaTeX-Erstcommit:** `d7d76c7d`
- **LaTeX-Kompilierung:** lokal zweimal `pdflatex`, Exit-Code 0, 8 Seiten, keine undefinierten Referenzen
- **LaTeX-Transferaudit:** `audits/AUDIT-2026-08-09_P06_LaTeX_SYN_Transferaudit.md`, Commit `1b1a7173`
- **LaTeX-Endstatus:** `SYN FROZEN ✓[K/M]`
- **Kernbefund:** Transportgenerator statt HP-Endoperator; Kreuzspektralmaßform statt diskreter NEU-051-Eigenbasis; endliche Feshbachidentität ohne Schattennormlimes; konkrete NEU-088–90-Schleifenskalierung kollabiert auf `D_N(z)→1`, ohne allgemeinen Feshbach-No-Go
- **Weiterleitung:** intrinsische Lift-/Quell-/Gramgeometrie, Mischblock `β_p`, globale nichtorthogonale Kopplung und globale Fredholm-/Schattenrealisierung → P11; zusammengesetzte Sektoren `[O-225-3]` bleiben offen

---

## P07 — Weil-Form Statistics

- **LaTeX-Ziel:** `papers/P07_Weil_Form_Statistics.tex`
- **Kanonische Markdown-Quelle:** `papers/P07_Weil_Form_Statistics.md`
- **Markdown-Status:** `SYN FINAL AUDITED`
- **Markdown-Finalcommit:** `6a162f92`
- **Pass-A-Basis:** `PASS-A-PROTOKOLL.md`; Abschluss NEU-091–120, Commit `baa3975b`
- **Synchronisationscommit:** NEU-101 Patch 3, Commit `92d731d1`
- **Knotenbasis:** NEU-091–120
- **Superseding SYN-Konventionen:** P02 für die kanonische Fourier-/Paley-Wiener-/Weilform-Typisierung
- **P03-Rolle:** Stil- und Konventionsabgleich; keine zusätzlichen P07-Aussagen importiert
- **LaTeX-Prüfart:** reiner SYN-Transferaudit; kein Vollneuaudit von NEU-091–120
- **LaTeX-Commit:** `12c77795`
- **LaTeX-Endstatus:** `SYN FROZEN ✓[K/M]`
- **Auditbefund:** kein neuer mathematischer Konflikt; kein NEU-Knoten wieder geöffnet

---
