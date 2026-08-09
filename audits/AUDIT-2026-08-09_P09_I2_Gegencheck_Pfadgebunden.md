# P09 / I2 — Pfadgebundener Gegencheck und Seal

**Datum:** 9. August 2026  
**SYN-Ziel:** P09 — BC + Hochschild  
**Paket:** I2 — äußere Derivationen und singuläre Potentialroute  
**Bezugsblatt:** `AUDIT-2026-08-09_P09_I2_Aeussere_Derivationen_Singulaere_Potentialroute_Reconciliation.md`  
**Status:** `VALID — KEIN KONKRETER GEGENBEFUND; I2 SEALED`

---

## 1. Gegencheck-Ergebnis

Der externe Gegencheck beantwortet die fünf atomaren Prüfungen des I2-Reconciliation-Blatts ohne konkreten Gegenbefund.

Verbindlich bleibt dabei die Formulierung des Reconciliation-Blatts selbst. Der Gegencheck ist ein **Bestätigungs-/Fehlersuchlauf**, kein neuer Primärbeweis und kein Superseding-Dokument.

---

## 2. Bestätigte atomare Punkte

### G1 — NEU-193/194

Bestätigt wird die im I2-Audit eingefrorene Trennung:

- der zweite NEU-193 konstruiert einen geladenen Dualzyklus;
- die Paarung detektiert den vollständig alternierenden Vier-Slot-Anteil;
- die symmetrische NEU-176-Schablone ist für diesen Zeugen blind (`Alt_4 L=0`);
- das determinantische Modell aus NEU-194 besitzt Paarungswert `24`, scheitert aber am Hochschild-Kozykeltest (`bL != 0`).

Daraus folgt **keine** geladene HH4-Klasse auf `A_Q^alg`.

### G2 — NEU-205

Bestätigt wird:

- die historische Sandwichformel ist falsch und `SUPERSEDED`;
- der kandidatenspezifische No-go für die drei konkreten dyadischen Platzierungen L/R/S bleibt nach Korrektur bestehen;
- die Aussage „Divergenz für jedes nichttriviale r“ ist zu stark;
- Architektur III ist durch NEU-205 nicht ausgeschlossen und bleibt `?[O]`.

### G3 — NEU-208

Bestätigt wird die korrigierte Normformel

\[
\|B_k\|=\sum_{p\mid k}\log\frac{v_p(k)+2}{2},
\]

nicht die alte Max-Norm. Der qualitative positive Befund bleibt: neutrale, normunbeschränkte analytische Derivation mit Ziel `A_{C^*}`; kein geladener algebraischer Schluss.

### G4 — NEU-210/211

Bestätigt wird der korrigierte Endstand

\[
D_g^{\rm corr}(e(r))=\mu_m C_{m,n;r}\mu_n^*,
\]

mit punktweiser Normkonvergenz für jedes feste `a in A_alg`. Der positive I2-Hauptbefund bleibt

\[
[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},A_{C^*})_g,
\qquad g\neq1.
\]

Die historische Setzung `D_g(e(r))=0` ist `×[M]`.

### G5 — Provenienz und Reichweite

Bestätigt wird:

- `NEU-198` fehlt als Live-Datei; daher keine eigenständige SYN-Provenienz daraus;
- `NEU-222` ist ein lokaler später Trassen-/Statusanker, kein pauschaler Superseder sämtlicher I2-Befunde;
- aus I2 folgt weder
  `HH^1(A_alg,A_alg)_g != 0`
  noch
  `HH^4(A,A)_ch != 0`.

Diese Zieltyp-/Cup-Firewall ist verbindlich für I3.

---

## 3. Seal

\[
\boxed{\text{P09 / I2 PASS A COMPLETE — Gegencheck ohne Befund — SEALED}}
\]

I2 wird nur bei einem konkreten neuen mathematischen Gegenbefund atomar wieder geöffnet.

**Nächster Block:** I3 — NEU-212–218, einschließlich drei NEU-217-Dateien und zwei NEU-218-Dateien.
