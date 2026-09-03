# Objekt X — strategische Forschungsroadmap

> **HISTORISCHER SNAPSHOT.** Diese Roadmap ist durch
> [FORSCHUNGS_ROADMAP_2026-09-03.md](FORSCHUNGS_ROADMAP_2026-09-03.md)
> als operative Priorisierung ersetzt worden. Sie bleibt am ursprünglichen Pfad, damit
> historische Links und Provenienz nicht brechen. Insbesondere sind die damaligen
> Angaben „A offen“ und „B / R27-F“ heute nicht mehr operativ.
>

> **Stand:** 2026-08-26  
> **Status:** Arbeitspriorisierung, **keine mathematische Implikationskette**.  
> **Definition:** Die kanonische Definition von Objekt X bleibt ausschließlich in
> [`OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).
>
> Diese Roadmap legt fest, welche offenen Fronten derzeit strategisch zuerst bearbeitet
> werden sollen. Sie behauptet weder, dass diese Reihenfolge notwendig oder eindeutig ist,
> noch dass ein späterer Punkt logisch aus einem früheren folgt. Neue Mathematik darf die
> Reihenfolge jederzeit ändern.
>
> **Aktualitätshinweis — 1. September 2026:** Diese Datei bleibt als
> strategischer Snapshot vom 26. August erhalten. Für den operativen Status
> gelten \`CURRENT-FRONT.md\` und \`ACTIVE_THEOREM_REGISTRY.md\`.
>
> - **A / finite-level Cross-Gram:** der universelle SW1-Nichtentartungsanspruch
>   ist inzwischen durch M1-ND-IMG4-SMALLR am expliziten Witness
>   \`✓[M]_neg\`. PR #49 ist zusätzlich ein **offener, eingefrorener
>   AI-GREEN candidate** für einen ganzen negativen Wedge
>   \[
>   0<\varepsilon<\frac{T-10\Delta}{8},\quad
>   0<R<\varepsilon,\quad
>   0<\sigma<R,
>   \]
>   aber nicht promotet und nicht gemergt.
> - **B / Strong Terminal:** weiterhin \`?[O]\`, aber nicht mehr als
>   unstrukturierte C6-Frage. Die absolute Terminalmetrik besitzt keinen
>   beschränkten Grenzoperator; relative Mosco-/Resolvent- und inverse-root-
>   Grenzbausteine sind vorhanden. Der nächste aktive Gate ist **R27-F**
>   (fixed Gamma-Crossblock / \(D_\infty^-=0?\)); danach separat **R22-F**
>   (Polar-Gauge-/Angle-Defect).
> - **Aktive Forschung:** B / R27-F. A / PR #49 bleibt eingefroren, bis es
>   bewusst wieder geöffnet wird.

---

## 0. Leseregel: Pfeile bedeuten Priorität, nicht Theorem

Die Kurzform

\[
\boxed{
\mathrm A\ \longrightarrow\ \mathrm B\ \longrightarrow\ \mathrm C\ \longrightarrow\ \mathrm D\ \longrightarrow\ \mathrm E
}
\]

ist **nur eine strategische Arbeitsreihenfolge**.

Insbesondere gelten folgende Firewalls:

- **A beweist B nicht, setzt B nicht voraus und wird von B nicht vorausgesetzt.**
  Finite-level Cross-Gram-Nichtentartung und Strong-Terminal-Konvergenz sind verschiedene
  offene Achsen.
- **B beweist A nicht, setzt A nicht voraus und wird von A nicht vorausgesetzt.**
  Beide Fronten können unabhängig und parallel bearbeitet werden.
- **C kann prinzipiell auch ohne vorherigen Abschluss von A oder B formuliert werden.**
  A und B sind derzeit die aussichtsreichsten bekannten **Arbeitsfronten zur Gewinnung bzw.
  Prüfung X-relevanter Kandidatenbausteine**, aber keine definitorisch notwendigen
  Eingangstore zu jedem denkbaren X-Kandidaten.
- **C -> D ist eine methodische Projektabhängigkeit, keine mathematische Implikation.**
  Ohne einen konkret spezifizierten X-Kandidaten mit Hilbertraum, Testklasse und
  Zuordnung kann die verlangte Gram-Identität nicht sinnvoll an diesem Kandidaten geprüft
  werden. Die Existenz eines X-Kandidaten beweist D selbstverständlich nicht.
- **D -> E ist ebenfalls keine automatische Schlussfolgerung.** Selbst eine exakte
  Gram-Identität muss noch auf der richtigen vollständig normalisierten Weil-Form und der
  richtigen Testklasse liegen und anschließend präzise mit dem einschlägigen
  Weil-Kriterium rückgebunden werden. Erst diese separate Prüfung kann eine RH-Konsequenz
  tragen.

Damit ist die Roadmap ausdrücklich **kein Beweisdiagramm**.

---

## A. Finite-level Cross-Gram-Nichtentartung

### Ziel

Der derzeit schärfste lokal angreifbare Test ist

\[
\boxed{\ker\Gamma_I=\{0\}\ ?[O],}
\]

mit

\[
\Gamma_I
=E_I^*HBH^*E_{\mathcal A}
=\mathscr M_I^*\mathscr M_A.
\]

Äquivalent ist ohne zusätzliche Injektivitätsannahme die Preimage-Form

\[
\Gamma_R^{-1}\!\left(
\mathcal Z_R^+\oplus\{0\}\oplus L^2(\mathcal V_R)
\right)=\{0\}\ ?
\]

und auf den global bewiesenen P12-Injektivitätsstrata zusätzlich die relative
Range-Transversalität.

### Bevorzugter Angriff

Die Schur-Inversenelimination reduziert die Kernfrage auf das augmentierte System

\[
\mathcal K_{I,A}(y,w)=0,
\qquad
\mathcal K_{I,A}
\binom yw
=
\binom{(I+A)y+HE_{\mathcal A}w}{E_I^*Hy},
\qquad A=R^*R.
\]

Mit der vollen Fiber-Graph-Koordinatennormalform

\[
E_I^*H\,\widehat\Phi_R(z,f,h)=f
\]

wird für \(y\in\mathcal K_R=\ker(E_I^*H|_+)\) kanonisch

\[
y=\widehat\Phi_R(z,0,h),
\]

so dass die zu analysierende Gleichung lautet

\[
\boxed{
(I+R^*R)\widehat\Phi_R(z,0,h)+HE_{\mathcal A}w=0.
}
\]

Im Drei-Shift-Fenster besitzt \(R^*R\) nach der aktuellen SE-Reduktion genau elf
endliche \(K^*M_\Omega K\)-Wortterme. Die bevorzugte erste Testregion ist

\[
T<S<T_0,
\qquad
\sigma=S-T\le R,
\]

weil dort die äußere Hub-Injektivität bereits global verfügbar ist.

### A0 — Randfall-/Uniformitäts-Firewall

Vor einer globalen Buchung von A muss geklärt werden, dass die Zerlegung der elf
Restwörter nach ihren Cutoff-Wänden den **gesamten** freien Koordinatenraum

\[
(z,h)\in\mathcal Z_R^+\oplus L^2(\mathcal V_R)
\]

abdeckt. Insbesondere sind Horizontschwanz, Cutoff-Grenzen und alle in der
Fiber-Graph-Klassifikation getrennt auftretenden Randlagen explizit mitzunehmen.

Ein Beweis auf offenen Zellen mit ausgeschlossenen Randlagen oder nur auf einer echten
Teilklasse von \((z,h)\) schließt A **nicht**. Ein solcher Befund ist höchstens
`✓[M]_part` bzw. Kandidatenfortschritt, je nach Auditstand.

### Konkrete Arbeitsfolge innerhalb A

1. Odd/even-Faltung festlegen.
2. Die drei Hub-Shifts \(a,b,T\) explizit einsetzen.
3. Die drei Rest-Martingaleblöcke einsetzen.
4. Alle elf \(K^*M_\Omega K\)-Wörter nach Cutoff-Wänden zerlegen.
5. A0 vollständig prüfen: keine unbehandelten Schwanz-/Randklassen.
6. Auf dem ersten globalen P12-Stratum das Rohsystem aufbauen.
7. Nach einer endlichen invertierbaren Rohmatrix oder einem exakten Gegenvektor suchen.
8. Erst nach vollständiger Randfallabdeckung über Promotion oder No-Go entscheiden.

**Status:** `?[O]`. Kein aktueller Befund beweist \(\ker\Gamma_I=\{0\}\).

---

## B. Strong Terminal / C6-Konvergenz

### Ziel

Unabhängig von A bleibt die globale Stabilitätsfrage offen: Konvergieren die relevanten
finite-level Übergänge bzw. Metriken stark zu einer terminalstabilen globalen Geometrie?
Symbolisch steht hierfür die historische C6-/Strong-Terminal-Frage, etwa in der Form

\[
W_{R,S,-}^{[T]}\longrightarrow W_{R,S,-}^{[\infty]}
\quad\text{stark?}
\]

Die heutige Objekt-X-Definition identifiziert X **nicht** mit einem solchen Grenzoperator.
Eine positive Lösung von B wäre daher ein starker X-Kandidatenbaustein, aber weder ein
Beweis von A noch bereits ein X-Kandidat oder Objekt X.

**Status:** `?[O]`.

---

## C. Erster echter X-Kandidat

### Ziel

Formuliere einen konkreten intrinsischen und nicht-zirkulären Vorschlag für eine
**gemeinsame Prime-/Archimedes-Geometrie**, der spezifiziert,

- aus welchen unabhängig definierten arithmetisch-analytischen Daten er entsteht,
- wie Primzahlpotenz- und archimedischer Kanal in derselben Geometrie erscheinen,
- welche gemeinsame Mediator-/Gram-Struktur sie koppelt,
- welche Testklasse und Normalisierung vorgeschlagen werden,
- und wie daraus die vollständige Weil-Form hervorgehen soll.

A und B dürfen diesen Kandidaten motivieren oder tragen, sind aber **keine definitorischen
Voraussetzungen für C**. Umgekehrt beweist ein formulierter X-Kandidat weder A noch B.

Die heutigen Strukturen FG-1, FG-TR1, \(\widehat\Phi_R\), Schur-Cross-Gram und CG-FG1
bleiben bis auf Weiteres **X-Kandidatenbausteine**, nicht X-Kandidaten.

**Status:** Es ist derzeit kein X-Kandidat im Sinn der kanonischen Definition konstruiert.

---

## D. Exakte vollständige Weil-Gram-Identität

### Ziel

Für einen konkret spezifizierten X-Kandidaten ist zu beweisen, dass auf einer geeigneten
Weil-Testklasse die vollständig und korrekt normalisierte Weil-Form exakt als

\[
\boxed{
Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}
}
\]

erscheint.

Eine Darstellung nur eines positiven Quadratanteils ist ein wichtiger Zwischenbaustein,
aber **kein Abschluss von D**. Ebenso zählt eine nachträgliche GNS-/Hilbertraum-
Faktorisierung aus bereits bekannter Positivität nicht als Objekt-X-Konstruktion.

**Abhängigkeit in dieser Roadmap:** D benötigt einen spezifizierten Kandidaten aus C, um
überhaupt als Kandidatenprüfung formuliert zu werden. C impliziert D jedoch nicht.

**Status:** `?[O]` / noch kein geeigneter X-Kandidat vorhanden.

---

## E. Präzise Weil-Kriterium-/RH-Rückbindung

### Ziel

Nach einer exakten Kandidatenrechnung in D ist separat zu verifizieren,

1. welche Weil-Form exakt realisiert wurde,
2. auf welcher Testfunktionsklasse,
3. mit welcher Fourier-/Gamma-/Pol-Normalisierung,
4. welche Positivitätsaussage daraus folgt,
5. und welches präzise Weil-Kriterium auf genau diesem Scope die Rückbindung an RH trägt.

Kein früherer Roadmap-Punkt darf diese Rückbindung vorwegnehmen. Insbesondere folgt aus
A, B oder C **keine** RH-Aussage. Auch D allein darf erst nach diesem Scope-/Kriteriumscheck
als RH-relevant interpretiert werden.

**Status:** `?[O]` als endgültige Rückbindungsstufe des Objekt-X-Programms.

---

## Quantitative Nebenfronten

Closed Range, bounded below, uniforme Winkel und quantitative Coercivity bleiben wichtige
stärkere Fragen. Sie sind derzeit **nicht** in A hineinzulesen und keine Voraussetzung für
den bloßen Injektivitätstest \(\ker\Gamma_I=\{0\}\). Sie können parallel verfolgt werden,
sobald ein konkreter Nutzen für A, B oder einen X-Kandidaten sichtbar ist.

---

## Kanonische Referenzen zum Stand 2026-08-26

- `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md` — Definition und
  X-Kandidaten-Hierarchie.
- `00-uebersicht/P11_R32_STATUS_2026-08-25.md` — Post-Freeze-Statusaddendum mit Update
  2026-08-26.
- `audits/P11_R32_SCHUR_CROSSGRAM_AUDIT.md` — Cross-Gram-Form des offenen Schur-Tests.
- `audits/P11_R32_SCHUR_INVERSE_ELIMINATION_AUDIT.md` — inversefreie Rohoperatorroute
  und 11-Wort-Reduktion.
- `audits/P11_R32_INNER_DENSITY_NOGO_AUDIT.md` — No-Go für den zu starken
  Dichtheits-Suffizienzweg.

---

**Kurzfassung:**

\[
\boxed{
\begin{array}{ll}
\mathbf A & \ker\Gamma_I=\{0\}\ ?[O]\\[1mm]
\mathbf B & \text{Strong Terminal / C6-Konvergenz }?[O]\\[1mm]
\mathbf C & \text{erster echter X-Kandidat}\\[1mm]
\mathbf D & Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}\\[1mm]
\mathbf E & \text{präzise Weil-Kriterium-/RH-Rückbindung.}
\end{array}
}
\]

**Leseregel bleibt:** strategische Reihenfolge, keine Theorem-Kette.
