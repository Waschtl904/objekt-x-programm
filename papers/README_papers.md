# Synthese-Manuskripte — Index

**Stand:** 2026-08-09; P11-Sonderupdate 2026-08-21  
**Stufen:** SYN (konsolidiert, intern) | PUB (publikationsreif)

---

## Drei Reifestufen erklärt

**NEU-Knoten** (in `active/` und `archive-nodes/`): Atomare Forschung. Darf Fehler, No-Gos, Patches, Statuswechsel, verworfene Ideen enthalten. Laborbuch und Provenienz.

**SYN-/P-Manuskripte** (diese Dateien): Nur der aktuell gültige mathematische Stand. Alte Fehlversuche werden höchstens kurz als No-Go erwähnt. Alle Definitionen werden konsolidiert. Format: LaTeX.

**PUB-Markierung**: Nur wenn eine zusammenhängende Aussage wissenschaftlich stark genug ist für Einreichung. Kein PUB-Stempel nur wegen Vollständigkeit.

---

## Manuskript-Liste

| ID | Datei | Titel | Stufe | Status |
|---|---|---|---|---|
| P01 | `P01_BC_Prime_Power_Weights.tex` | BC Prime Power Weights | SYN | Entwurf |
| P02 | `P02_Adelic_Weil_Amplitude_Port.tex` | Adelic Weil Amplitude Port | SYN | Entwurf |
| P03 | `P03_Haar_L2_Firewall.tex` | Haar-$L^2$ Firewall | SYN | Entwurf |
| P04 | `P04_Finite_Weil_Geometry.tex` | Finite Weil Geometry & Objekt-X-Schnittstelle | SYN | In Arbeit |
| P05 | `P05_Relative_Prime_Channels_and_Arithmetic_Edge_Geometry.tex` | Relative Prime Channels and Arithmetic Edge Geometry | SYN | **FROZEN ✓[K/M]** |
| P06 | `P06_Jacobi_Feshbach_and_Divisor_Graph.tex` | Jacobi–Feshbach and Divisor Graph | SYN | **FROZEN ✓[K/M]** |
| P07 | `P07_Weil_Form_Statistics.tex` | Weil-Form Statistics | SYN | **FROZEN ✓[K/M]** |
| P08 | `P08_Renormalized_Prime_Operators_and_Finite_Part_Structures.tex` | Renormalized Prime Operators and Finite-Part Structures | SYN | **FROZEN ✓[K/M]** |

### P11-Sonderstatus — 2026-08-21

`P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex` ist nach vollständigem mathematischem End-to-End-Audit und beobachtet grünem GitHub-Actions-Zwei-Pass-LaTeX-/Reference-Check auf `main@3d60e19697420040ea8fede5dd5fc87703dfe92e` formal

**FROZEN ✓[K/M]**

am ausdrücklich gewählten finite-horizon / Candidate-Geometry-Scope.

Strong odd terminal transport, finite-jet inverse-square-root control, konkrete polar-gauge Asymptotik und R30-F/R32-F bleiben `?[O]`; sie sind keine versteckten Voraussetzungen des eingefrorenen P11-Cores. Der kanonische Abschluss ist dokumentiert in `audits/P11_FREEZE_RECORD_2026-08-21.md`.

---

## Kanonische Kompressionsformel

$$\mathcal{S}_{\rm adel}^{\rm amp} \xrightarrow{R_{\rm PW}} \mathcal{A}_{\rm PW} \xrightarrow{(a,b)\mapsto g_{a,b}} \mathcal{G}_{\rm ev}^{\mathbb{C}} \xrightarrow{\rm Weil} B_W.$$

Diese eine Zeile ersetzt zehn NEU-Knoten für tagtägliche Arbeit. Die Knoten bleiben für Audit und Provenienz in `archive-nodes/`.

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm.*
