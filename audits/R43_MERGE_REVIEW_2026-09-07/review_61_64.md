# R43 — unabhängiger Merge-Review PR61 / PR64

**Prüfdatum:** 07.09.2026. **Modus:** read-only; begrenzter Integrationsreview, keine neue Forschungsrunde und kein Gesamtaudit von P11.

## Aktueller Abschluss nach Minimalkorrektur — 07.09.2026

**PR61 bleibt READY. PR64 ist am korrigierten Head `ff327e3fb59dcfde7bd8260e779919961dd6f88d` ebenfalls READY innerhalb des dokumentierten lokalen Scopes; B64-1 ist geschlossen.** [Korrigierter Absatz, Z.404–412](https://github.com/Waschtl904/objekt-x-programm/blob/ff327e3fb59dcfde7bd8260e779919961dd6f88d/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L404-L412)

| PR64-Stand | Exakter Head | Blob der Primband-Notiz | Urteil |
|---|---|---|---|
| Ursprünglich, historisch | `7409b9a13028fb8dc0fc44fb210e4783b6feaf7c` | `a477c8bbe329bf45f7c1872c3779b0db02c0789b` | **BLOCKED** wegen der falschen Kern-/Optimalitätsillustration. [Alter Absatz](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L402-L404) |
| Nach Minimalkorrektur | `ff327e3fb59dcfde7bd8260e779919961dd6f88d` | `1ff5abd902f47e618a6d245a89c5fbee50297617` | **READY im dokumentierten Scope**; Kern-/Optimalitätsbehauptung ausdrücklich zurückgenommen. [Korrigierter Absatz, Z.404–412](https://github.com/Waschtl904/objekt-x-programm/blob/ff327e3fb59dcfde7bd8260e779919961dd6f88d/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L404-L412) |

Die exakte Parent-ID ist `7409b9a13028fb8dc0fc44fb210e4783b6feaf7c`; der vollständige Commit-Diff enthält nur die Ersetzung des alten Absatzes in Zeile 404 durch die neue Fassung in Zeilen 404–412 (**eine Datei, 9 Einfügungen, 1 Löschung**), und der Dateitext davor sowie danach ist unverändert. [Korrigierter Absatz, Z.404–412](https://github.com/Waschtl904/objekt-x-programm/blob/ff327e3fb59dcfde7bd8260e779919961dd6f88d/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L404-L412)

**Mathematische Abschlusskontrolle:** Die Masse des normierten konstanten Vektors in beiden Collars ist für \(0<r<U\) exakt \(r/U\); die behaltene primitive \(k=1\)-Differenz ist null, während höhere \(k\)-Randbeiträge nicht generell verschwinden, und die Ersatzfassung behauptet genau dies ohne Vollresidual-Kern- oder Optimalitätsfolgerung. [Korrigierter Absatz, Z.404–412](https://github.com/Waschtl904/objekt-x-programm/blob/ff327e3fb59dcfde7bd8260e779919961dd6f88d/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L404-L412)

**Keine Änderungen an CE1–CE42, keiner anderen Datei und keinem der vorher geprüften Scope-Firewalls; deshalb ist keine erneute Vollprüfung des Stacks erforderlich.** Die unten dokumentierte Erstprüfung samt explizitem Gegenbeleg bleibt als historische Begründung erhalten. [Korrigierter Absatz, Z.404–412](https://github.com/Waschtl904/objekt-x-programm/blob/ff327e3fb59dcfde7bd8260e779919961dd6f88d/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L404-L412)

Die Korrektur wurde ausschließlich am lokalen Commit geprüft; dieser Review hat weder gepusht noch GitHub geändert und prüft keine öffentliche Verfügbarkeit der commitfixierten Links.

---

## Ersturteil vor der PR64-Korrektur — historisch

| PR | Exakter Head | Urteil | Minimale Aktion |
|---|---|---|---|
| **61** | `e29545a6040640e754e885888826d1cf235df58c` | **READY innerhalb des dokumentierten lokalen Scopes** | Keine mathematische Änderung erforderlich; insbesondere bleiben RR34/RR35 einseitige skalare Reduktionen. [RR34–RR35, Z.508–590](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L508-L590) |
| **64** | `7409b9a13028fb8dc0fc44fb210e4783b6feaf7c` | **BLOCKED — eng begrenzte falsche lokale Aussage** | Absatz in **Zeile 404** streichen oder korrigieren: Ein konstanter Vektor ist **kein** Kernvektor des vollen Residualoperators. [PR64, Z.402–404](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L402-L404) |

**Wichtig:** Der PR64-Blocker betrifft die falsche Kern-/Schärfeillustration, nicht eine Widerlegung von CE23 oder CE35–CE42; deren Beweiskette benutzt den beanstandeten Absatz nicht. [CE23, Z.384–398](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L384-L398) [CE24–CE42, Z.414–727](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L414-L727)

**Kein Forschungsblocker:** Offene Strong-Terminal-, FD23-, FLAGDYN- und kanonische Reverse-Normal-Brücken werden hier nicht zur Merge-Voraussetzung gemacht; die geprüften Notizen beanspruchen diese globalen Folgerungen nicht. [PR61-Firewall, Z.594–609](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L594-L609) [PR64-Firewall, Z.725–756](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L725-L756)

## Exakte Prüfbasis und Blob-Gleichheit

- **PR61 gegen PR58:** Basis `0e57cf230291abd16ce88b0ceed95d68036799e5`, Head `e29545a6040640e754e885888826d1cf235df58c`; Delta ausschließlich die drei unten aufgeführten PR61-Notizen. [Hard11, exakter PR61-Stand](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_HARD11_LEVEL0_SATURATION_REDUCTION_2026-09-06.md)
- **PR64 gegen PR61:** Basis `e29545a6040640e754e885888826d1cf235df58c`, Head `7409b9a13028fb8dc0fc44fb210e4783b6feaf7c`; Delta ausschließlich die Primband-Notiz. [Primband, exakter PR64-Stand](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md)
- **Lokaler Integrationstip:** `a7f00fd6ef4824f2aecc934b52088127112a2b5f`; alle vier geprüften Dateien sind im Arbeitsbaum und im Tip blob-identisch zu den exakten PR-Ständen, der Arbeitsbaum war vor und nach dem Review unverändert. Die folgenden commitfixierten Belege bezeichnen deshalb exakt die gelesenen Inhalte. [Hard11, exakter PR61-Stand](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_HARD11_LEVEL0_SATURATION_REDUCTION_2026-09-06.md) [Peeling, exakter PR61-Stand](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_PRIMITIVE_LEVEL_PEELING_2026-09-06.md) [Cancellation, exakter PR61-Stand](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md) [Primband, exakter PR64-Stand](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md)

| PR | Geprüfte Notiz | Git-Blob |
|---|---|---|
| 61 | [P11_R43_HARD11_LEVEL0_SATURATION_REDUCTION_2026-09-06](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_HARD11_LEVEL0_SATURATION_REDUCTION_2026-09-06.md) | `784c7b5a55a012b4fdf509b4009f0c7b80c8c9bb` |
| 61 | [P11_R43_PRIMITIVE_LEVEL_PEELING_2026-09-06](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_PRIMITIVE_LEVEL_PEELING_2026-09-06.md) | `8d64282d25e56de4014dac5eb88d8a16bdf330df` |
| 61 | [P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md) | `59d2ff8601c90f6a24074ae8f6b7ba36d4aab2eb` |
| 64 | [P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md) | `a477c8bbe329bf45f7c1872c3779b0db02c0789b` |

Die zusätzlich konsultierten Definitionsdateien sind zwischen PR58, PR64 und Integrationstip ebenfalls blob-identisch; sie wurden nur für die unmittelbar benötigten Definitionen und Voridentitäten gelesen, nicht vollständig neu auditiert. [P11-Definitionen](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L133-L253) [TR9](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_TRANSLATION_SHELL_AND_RESOLVENT_TRANSFER_2026-09-05.md#L187-L224) [SL1–SL6](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_STRUCTURED_COND_LEAKAGE_REDUCTION_2026-09-05.md#L14-L129) [GM13–GM20](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_GEOMETRIC_MEAN_RESOLVENT_LEAKAGE_2026-09-06.md#L163-L277) [GN24–GN26](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_GOOD_NORMAL_TAIL_REDUCTION_2026-09-06.md#L440-L493)

## PR64-Blocker B64-1: übersehene höhere Randzeilen

**Fundstelle:** `TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE`, Zeile **404**, Abschnitt „Interpretation“. [PR64, Z.402–404](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L402-L404)

> “a normalized constant vector lies in the kernel of the old residual difference operator”

Das ist für den hier definierten **vollen** \(R_U\) falsch: Die Eligibility \(\lvert u\rvert+a_p\le U\) der behaltenen Level-0-Zeile gewährleistet beide Endpunkte nur für \(k=1\), während dieselbe Zeile auch alle \(k\ge2\)-Differenzen enthält. [CE4–CE5, Z.128–155](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L128-L155)

### Exakter Gegenbeleg, ohne Diskretisierungsannahme

Setze \(p=2\), \(a=\tfrac12\log2\), \(U=2a=\log2\) und \(x_U=(2U)^{-1/2}1_{(-U,U)}\); für jedes \(0<u<a\) ist die Zeile \((p,a_{\mathrm{level}})=(2,0)\) behalten, und die eingefrorene Half-Shift-/Nullfortsetzungsdefinition liefert, bis auf das globale Vorzeichen, folgende Werte. [Half-Shift und Nullfortsetzung, Z.133–151](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L133-L151) [K-Definition, TR1–TR3](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_TRANSLATION_SHELL_AND_RESOLVENT_TRANSFER_2026-09-05.md#L25-L54)

\[
K_{2,1;U}x_U(u)=0,\qquad
K_{2,2;U}x_U(u)=-(2U)^{-1/2},\qquad
K_{2,k;U}x_U(u)=0\quad(k\ge3).
\]

Einsetzen in **die vollständige gewichtete Zeile CE4**, nicht in einen ungewichteten Einzelterm, ergibt exakt
\[
T_{2,0;U}x_U(u)
=-\sqrt{\log2}\,2^{-3/2}(2\log2)^{-1/2}
=-\frac14,
\qquad 0<u<\frac12\log2.
\]
Somit ist schon der Beitrag dieses positiven Halbintervalls
\[
\|R_Ux_U\|^2\ge\frac{\log2}{32}>0.
\]
Das ist eine direkte Auswertung von CE4/CE5 und der Nullfortsetzung, keine numerische Vermutung. [CE4–CE5, Z.128–155](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L128-L155) [Half-Shift und Nullfortsetzung, Z.133–151](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L133-L151) [K-Definition, TR1–TR3](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_TRANSLATION_SHELL_AND_RESOLVENT_TRANSFER_2026-09-05.md#L25-L54)

Der Fehler verschwindet auch nicht im asymptotischen Regime: Für jedes \(U\ge\log2\) und \(u\in(U-2a,U-a)\) bleibt \(k=1\) null, \(k=2\) ist nicht null, und alle weiteren nichtverschwindenden Differenzen des konstanten Vektors haben dieselbe Orientierung, können den positiven \(k\)-gewichteten Beitrag also nicht aufheben. [CE4–CE5, Z.128–155](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L128-L155) [Half-Shift und Nullfortsetzung, Z.133–151](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L133-L151) [K-Definition, TR1–TR3](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_TRANSLATION_SHELL_AND_RESOLVENT_TRANSFER_2026-09-05.md#L25-L54)

### Minimale Korrektur

**Kleinste sichere Änderung:** den gesamten Interpretationsabsatz in Zeile 404 löschen; keine Formel CE1–CE42 und kein zusätzliches Lemma muss dafür verändert oder bewiesen werden. [PR64, Z.402–404](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L402-L404) [CE23, Z.384–398](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L384-L398) [CE24–CE42, Z.414–727](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L414-L727)

Falls eine Illustration gewünscht ist, genügt als Ersatz:

> “A normalized constant vector has collar mass squared exactly r/U. It annihilates the retained primitive k=1 differences, but not the full residual operator R_U: higher-k boundary contributions remain. No full-residual kernel or optimality claim is used here.”

Diese Ersatzformulierung behält die richtige elementare Collar-Masse bei, ohne die übersehenen \(k\ge2\)-Randzeilen erneut zu null zu setzen. [CE4–CE5, Z.128–155](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L128-L155) [PR64, Z.402–404](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L402-L404)

**Merge-Folge:** Den exakten, noch fehlerhaften Head nicht uneingeschränkt freigeben; nach dieser Ein-Absatz-Korrektur genügt eine punktuelle Diff-/Head-Kontrolle, keine zusätzliche Forschungsrunde und keine Wiederöffnung des gesamten Stacks.

## PR61: bestandene Kernprüfungen

### Gewichtete Zeilen und vollständige Horizontverschachtelung

Die verwendete Zeile
\[
T_{p,a;R}=\sqrt{(\log p)(p-1)p^a}\;
1_{\Omega_{p,a,R}}\sum_{k\ge a+1}p^{-3k/4}K_{p,k;R}
\]
stimmt exakt mit der martingalen Koordinatenentwicklung des Manuskripts überein; insbesondere wird weder der Faktor \((p-1)p^a\) ausgelassen noch fälschlich Orthogonalität verschiedener \(k\) desselben Primes angenommen. [P11, Z.350–407](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L350-L407) [H11.1–H11.2](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_HARD11_LEVEL0_SATURATION_REDUCTION_2026-09-06.md#L44-L65)

\(\Omega_{p,a,U}\subseteq\Omega_{p,a,V}\) und \(E_V\iota=E_U\) geben levelweise \(D_{a;U,V}\succeq0\); dabei enthält \(\sum_aD_a=C^*C\) sowohl neue Details im alten Fenster als auch neue räumliche Residualstreifen. [PL1–PL7, Z.21–124](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_PRIMITIVE_LEVEL_PEELING_2026-09-06.md#L21-L124) [beide Residualgattungen, SL3–SL6](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_STRUCTURED_COND_LEAKAGE_REDUCTION_2026-09-05.md#L73-L129)

### Hard11-Sättigung und Peeling

- **H11.24–H11.29:** Die positive Blockmatrix von \(B_{0,V}\) und \(Z_0\preceq S^*S\) geben den Schur-Absorptionsschritt mit korrekter Inversionsrichtung; belastet wird ausdrücklich der Horizont-\(V\)-Altdiagonalblock \(X_0\), nicht stillschweigend \(B_{0,U}\). [H11.23–H11.29, Z.305–415](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_HARD11_LEVEL0_SATURATION_REDUCTION_2026-09-06.md#L305-L415)
- **PL9:** Die Aufteilung \(\varepsilon I+Z_0\), \((1-\varepsilon)I+Z_1\), Operator-Cauchy und \(\varepsilon\downarrow0\) sind am festen endlichen Horizontpaar legitim und liefern genau die behauptete einseitige Peeling-Ungleichung. [PL8–PL11, Z.134–244](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_PRIMITIVE_LEVEL_PEELING_2026-09-06.md#L134-L244)
- **PL12–PL24:** Das Vorzeichen vor \(C^*C\) ist richtig; \(X_0-D_0=B_{0,U}\) und die entsprechende Level-1-Identität erklären die berechnete Last der alten Niedriglevelenergie, während \(a\ge2\) vollständig in der Restabschätzung bleibt. [PL12–PL25, Z.248–505](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_PRIMITIVE_LEVEL_PEELING_2026-09-06.md#L248-L505)

### Retained-row cancellation: keine ausgelassene Zeilengattung

Die gleiche orthogonale Zielprojektion \(\Pi\) wird auf **beide** Operatoren \(M\) und \(S\) angewandt, so dass die neuen Zeilen einen positiven Block mit Altdiagonale **exakt** \(C^*C\) bilden; Peeling plus das bereits vorhandene Minuszeichen in RR10 liefert RR12/RR13 ohne Restlast alter Levelenergie. [RR1–RR13, Z.23–188](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L23-L188)

„Cancellation“ bedeutet hier die exakte Aufhebung dieser Diagonallast **innerhalb einer oberen Schranke**, nicht die unzulässige Behauptung, der volle nichtlineare Leakage-Term sei additiv in den Zeilenkanälen. [RR10–RR13, Z.138–199](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L138-L199)

Für \(k=\ell=a+1=m\) liegen beide primitiven Endpunkte jeder behaltenen Zeile in \([-U,U]\); deshalb kann kein solcher Sum-Sign-Zweig in die neue Quellregion führen, während Zero-Shift-Terme ohnehin im Altraum bleiben und niedrigere nichtprimitive Diagonallevel ausdrücklich in RR27–RR29 erfasst werden. [RR19, Z.244–321](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L244-L321) [RR27–RR29, Z.410–443](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L410-L443)

### Summierbarkeit mit \(\beta=1/8\)

| Familie | Schlechtester Exponent in der gewichteten Prim-Potenz | Befund |
|---|---:|---|
| H11-Level-0-Rest, \(k+\ell\ge3\) | \(-17/16\) | Summierbar. [H11.17–H11.19](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_HARD11_LEVEL0_SATURATION_REDUCTION_2026-09-06.md#L231-L261) |
| PL-Hochlevel, \(a\ge2\) | \(-9/8\) | Summierbar, einschließlich Levelsumme. [PL19–PL21](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_PRIMITIVE_LEVEL_PEELING_2026-09-06.md#L410-L450) |
| RR-Differenz, \(m,d\ge1\) | \(-19/16\) | Summierbar. [RR22–RR24](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L353-L383) |
| RR-offdiagonale Summe, \(m,d\ge1\) | \(-17/16\) | Summierbar. [RR25–RR26](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L386-L407) |
| RR-behaltene diagonale Summe, \(m\ge2,\ a\le m-2\) | \(-7/4\) | Summierbar; gerade die nach primitiver Exklusion übrigen Level. [RR27–RR30](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L410-L456) |

Bei der Levelsumme entsteht kein versteckter horizonabhängiger Multiplizitätsfaktor: \(\sum_{a=0}^{m-1}(p-1)p^a=p^m-1\), beziehungsweise nach primitiver Exklusion \(\sum_{a=0}^{m-2}(p-1)p^a=p^{m-1}-1\); die restlichen Indexsummen sind für \(p\ge2\) geometrisch und die Primzahlensummen werden durch ganzzahlige Summen mit Exponent kleiner als \(-1\) dominiert. [H11.9](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_HARD11_LEVEL0_SATURATION_REDUCTION_2026-09-06.md#L138-L146) [RR20–RR30](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L331-L456)

Damit sind die Collar-plus-Tail-Konstante und RR34/RR35 uniform in \(U,V\); PR61 behauptet daraus noch keinen asymptotischen Decay und keine unnormalisierte Teleskopsummierbarkeit. [RR30–RR35 und Scope, Z.445–611](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L445-L611)

## PR64: tragfähige Hauptkette und Quantoren

1. **Primband / PNT:** CE2 folgt aus den angegebenen zweiseitigen Chebyshev-Schranken bei einer einmal fest gewählten hinreichend großen \(\Lambda\); es wird keine Aussage für beliebig schmale Primintervalle benötigt und die PNT ist kein zusätzlicher Input. [CE1–CE3, Z.38–124](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L38-L124)
2. **Gewichteter \(k\ge2\)-Fehler:** CE8/CE9 kontrollieren die Summe der **quadrierten** Tail-Normen nach Multiplikation mit \((\log p)(p-1)\) durch \(C\sum_p(\log p)p^{-2}\); die Extraktion von \(k=1\) in CE13 erfolgt daher legitim aus der positiven vollen Level-0-Energie, ohne die höheren Zeilenbeiträge zu ignorieren. [CE7–CE13, Z.169–271](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L169-L271)
3. **Eligibility und Bänder:** CE11 sorgt für \(u=z-\tfrac12\log p\in\Omega_{p,0,U}\); die Intervalle CE19 sind disjunkt bis auf Nullränder und bleiben in der richtigen positiven bzw. negativen Halbachse. [CE11–CE12](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L227-L250) [CE14–CE22](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L289-L381)
4. **Konstanten:** Aus CE14/CE15 folgt \(N=\lfloor(U-r)/(r+\delta_0)\rfloor-1\); beispielsweise \(r\ge\delta_0\), \(2r+\delta_0\ge t_{\rm pb}\), \(U\ge8r\) erlauben \(N\ge U/(8r)\), und CE2 gibt \(W_{\min}\ge c e^r\), so dass CE23 tatsächlich uniforme Konstanten hat. [CE14–CE23, Z.291–398](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L291-L398)
5. **Transportenergie:** CE25–CE28 folgen korrekt aus \(\mathcal Q\mathscr A_U\mathcal Q=\widetilde B_{U,V}\) und \(s_U+\Delta\); die separat verwendete Schranke \(\|x\|\le1\) folgt aus dem geerbten \(\mathcal Q^2\preceq B_U\), **nicht allein** aus CE28 mit rechter Seite \(1+\delta\). [CE25–CE28, Z.425–503](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L425-L503) [GN24–GN26](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_GOOD_NORMAL_TAIL_REDUCTION_2026-09-06.md#L451-L493)
6. **Absorption:** CE31 besitzt den Koeffizienten \(A_1(r/U)e^{-r}\) vor \(\delta\), der in dem angegebenen Regime kleiner als \(1/2\) gewählt werden kann; \(r=8\log U\) ist schließlich zulässig und liefert \(e^{-r/4}=U^{-2}\), also CE35/CE36 uniform für alle \(V>U\). [CE29–CE37, Z.513–640](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L513-L640)
7. **Homogenität und Scope:** Für Daten im endlichen terminalen Graph-Formbereich mit \(Q_U(f)>0\) sind CE38/CE39 uniforme **relative skalare** Schranken auf der Klasse \(x=\mathcal QH_U^*E_{X,U}f\); die Aussage betrifft \((\Delta s_{\rm cond})_+\), nicht den Betrag des signierten Inkrements, nicht dessen negative Seite und nicht den operatorweiten Knoten B-METINC-COND. [CE38–CE39 und Scope, Z.640–682](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L640-L682) [Graph-Formbereich](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L302-L336)
8. **Geometrische Kette:** \(\sum_j\log(U_02^j)/(U_02^j)<\infty\) begründet CE42 für die normierten Größen; daraus wird im Text richtigerweise weder rohe unnormalisierte Summierbarkeit noch die direkte FD23/FLAGDYN-Komposition abgeleitet. [CE40–CE42 und Firewall, Z.686–727](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L686-L727)

**Kleine, nicht blockierende Klarstellung:** Bei Zeile 503 wäre ein expliziter Verweis auf GN24/GN25 hilfreich; die benötigte Kontraktion ist jedoch in der exakten Basis bereits bewiesen, so dass hier kein weiteres Lemma fehlt. [PR64, Z.494–503](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L494-L503) [GN24–GN25](https://github.com/Waschtl904/objekt-x-programm/blob/0e57cf230291abd16ce88b0ceed95d68036799e5/audits/P11_R43_GOOD_NORMAL_TAIL_REDUCTION_2026-09-06.md#L451-L476)

## Abschluss der Erstprüfung — historisch, durch obige Korrektur ergänzt

- **PR61 jetzt im dokumentierten Draft-Scope freigabefähig.** [RR30–RR35 und Scope, Z.445–611](https://github.com/Waschtl904/objekt-x-programm/blob/e29545a6040640e754e885888826d1cf235df58c/audits/P11_R43_RETAINED_ROW_CANCELLATION_2026-09-06.md#L445-L611)
- **PR64 benötigt ausschließlich die lokale Korrektur in Zeile 404**, bevor der exakte Inhalt als mathematisch fehlerfrei freigegeben wird; danach nur den geänderten Absatz und neuen Head kontrollieren. [PR64, Z.402–404](https://github.com/Waschtl904/objekt-x-programm/blob/7409b9a13028fb8dc0fc44fb210e4783b6feaf7c/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L402-L404)
- **Keine Repo-Änderungen, keine GitHub-Schreibaktion, keine Registry-Promotion durch diesen Review.**

## Abschließende Freigabe des korrigierten PR64-Heads

**READY innerhalb des dokumentierten Scopes für `ff327e3fb59dcfde7bd8260e779919961dd6f88d`; der einzige zuvor gemeldete Blocker B64-1 ist durch den geprüften Ein-Absatz-Diff behoben.** Der Gegenbeleg bleibt gültig gegen die ausdrücklich zurückgezogene Aussage des alten Heads, nicht gegen die neue Fassung. [Korrigierter Absatz, Z.404–412](https://github.com/Waschtl904/objekt-x-programm/blob/ff327e3fb59dcfde7bd8260e779919961dd6f88d/audits/P11_R43_TRANSPORTED_COLLAR_PRIME_BAND_ESCAPE_2026-09-06.md#L404-L412)
