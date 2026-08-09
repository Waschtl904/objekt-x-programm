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
- **Markdown-Finalcommit:** `22f07a31`
- **Pass-A-Basis:** `PASS-A-PROTOKOLL.md`; Abschluss NEU-091–120, Commit `baa3975b`
- **GM-Synchronisationscommit:** NEU-101 Patch 3, Commit `92d731d1`
- **Externcheck-Targeted-Reaudit:** `audits/AUDIT-2026-08-09_P07_Externcheck_GM_aN_Targeted-Reaudit.md`, Commit `57441d87`
- **NEU-120 Patch 2:** Commit `410d0a91` — kanonische Zentrierung `A=Re m_arith(i)=0`; notwendiger Test `m_N^ren→m_arith` lokal gleichmäßig `⇒ a_N→0`
- **Knotenbasis:** NEU-091–120
- **Superseding SYN-Konventionen:** P02 für die kanonische Fourier-/Paley-Wiener-/Weilform-Typisierung
- **P03-Rolle:** Stil- und Konventionsabgleich; keine zusätzlichen P07-Aussagen importiert
- **Externcheck-Befund:** behaupteter `H=M`-Fehler trifft den Live-Stand nicht; P07 verwendet `H=√M`. Der GM-$H$-Bereich `1≤H≤M^{1-ε}` bleibt nach Quellengegencheck unverändert; keine falsche Untergrenze `M^ε` importiert.
- **LaTeX-Prüfart:** lokaler SYN-Transfer von Patch 4; kein Vollneuaudit von NEU-091–120
- **LaTeX-Erstcommit:** `12c77795`
- **LaTeX-Patch-4-Commit:** `e2ab077f`
- **LaTeX-Endstatus:** `SYN FROZEN ✓[K/M]`
- **Auditbefund:** kein neuer Konflikt im GM-Korollar; neue notwendige Symmetrie-/Normalisierungsbedingung `a_N→0` bewiesen; eigentliche Jacobi/Herglotz-Konvergenz und Tail-Kontrolle bleiben offen

---

## P08 — Renormalized Prime Operators and Finite-Part Structures

- **LaTeX-Ziel:** `papers/P08_Renormalized_Prime_Operators_and_Finite_Part_Structures.tex`
- **Kanonische Markdown-Quelle:** `papers/P08_Renormalized_Prime_Operators_and_Finite_Part_Structures.md`
- **Markdown-Status:** `SYN FINAL AUDITED`
- **Markdown-Erstcommit:** `29101001`
- **Markdown-Finalcommit:** `31c93d50`
- **Pass-A-Basis:** `audits/AUDIT-2026-08-09_P08_PassA_FINAL_SEAL.md`, Commit `964c602b`; H-T1 bis H-T5 vollständig reconciliiert
- **Knotenbasis:** Live-Block `04-grenzoperator-renormierung/`, NEU-121–150 gemäß Inventar; NEU-126/129 fehlen live; NEU-123F liegt in zwei verschiedenen Dateien vor
- **SYN-Primärcheck:** `audits/AUDIT-2026-08-09_P08_SYN_Primaercheck.md`, Commit `f3330c2f`; Urteil `OHNE KONKRETEN GEGENBEFUND`
- **SYN-Zweitcheck:** `audits/AUDIT-2026-08-09_P08_SYN_Zweitcheck_Pfadgebunden.md`, Commit `3d3b8864`; Urteil `OHNE KONKRETEN GEGENBEFUND`
- **LaTeX-Prüfart:** reiner SYN-Transferaudit; kein erneuter Vollaudit von NEU-121–150
- **LaTeX-Commit:** `d283c34c`
- **LaTeX-Transferaudit:** `audits/AUDIT-2026-08-09_P08_LaTeX_SYN_Transferaudit.md`, Commit `3f12e0ef`; Urteil `OHNE KONKRETEN GEGENBEFUND`
- **LaTeX-Kompilierung:** in dieser Sitzung nicht ausgeführt; Connector-Datei nicht lokal materialisiert, Container ohne DNS zum Raw-GitHub-Endpunkt; kein erfolgreicher Compile wird behauptet
- **LaTeX-Endstatus:** `SYN FROZEN ✓[K/M]`
- **Kernbefund:** strenger Kollaps `b_{1,N}→0` im unrenormierten symmetrischen Jacobi-Pfad; feste-`β`-Spurklasse nur `CONDITIONAL ✓[M]_{model}` unter modellrelativem Rang-`≤1` plus quantitativer `c_p`-Schranke; T2 und Nichtentartung erst für primdiagonales Mangoldt-`R`; exakter Mellin-Kanal über `Ψ_{φ,X}`; Prime-only-`S_{φ,X}`-Mellin-Identität gesperrt; operatorieller Finite Part bleibt offen
- **Zentrale Firewall:** `Tr_reg := AC[-ζ'/ζ]` bleibt Definition und beweist keine operatorielle Regularisierung; keine Objekt-X-/Hilbert–Pólya-Konstruktion, kein RH-Beweis
- **Weiterleitung:** gesicherte No-Gos → P10; intrinsische Lift-/Gram-/T2-/Nichtentartungs- und globale Schatten/Fredholm-Geometrie → P11; Finite-to-Infinite-Weil-Grenzfragen → P12

---
