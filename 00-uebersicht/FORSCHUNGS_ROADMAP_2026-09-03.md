# Objekt X — strategische Forschungsroadmap

> **Stand:** 2026-09-03
> **Status:** Arbeitspriorisierung, **keine mathematische Implikationskette**.
> **Operative Quellen:** [CURRENT-FRONT](../CURRENT-FRONT.md) und
> [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md).
> **Definition:** Die kanonische Definition von Objekt X bleibt ausschließlich in
> [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).
>
> Diese Roadmap ersetzt die strategische Roadmap vom 26. August 2026 als operative
> Priorisierung. Die alte Datei bleibt als historischer Snapshot erhalten.

---

## 0. Leseregel

Die Roadmap beschreibt **Arbeitsfronten**, keine Beweiskette.

Insbesondere gilt weiterhin:

- A, B und der separate R37-Analytikpfad sind logisch voneinander getrennte Fronten.
- Ein positiver Abschluss von B wäre ein starker Kandidatenbaustein, aber noch kein Objekt X.
- C ist die Konstruktion eines echten X-Kandidaten.
- D ist eine separate exakte Weil-Gram-Prüfung an einem spezifizierten Kandidaten.
- E ist erst danach die präzise Weil-Kriterium-/RH-Rückbindung.

Kurzform:

\[
\boxed{
\mathrm{A}_{\rm finite}
\quad\parallel\quad
\mathrm{B}_{\rm terminal}
\quad\parallel\quad
\mathrm{R37}_{\rm analytic}
\qquad\leadsto\qquad
\mathrm C\to\mathrm D\to\mathrm E
}
\]

Die Pfeile nach C bedeuten strategische Reife, nicht logische Implikation.

---

## A. Finite-level Cross-Gram / SW1 — universelle Route negativ entschieden

### Alter Zielknoten

Die Roadmap vom 26. August führte als aktive Frage

\[
\ker\Gamma_I=\{0\}\ ?[O]
\]

im universellen SW1-Sinn.

### Heutiger Stand

Dieser universelle Nichtentartungsanspruch ist **nicht mehr offen**. Der explizite
M1-ND-IMG4-SMALLR-Gegenvektor hat die universelle Route negativ entschieden.

Damit ist A als universeller positiver Weg strategisch **geschlossen**.

Separat existiert PR #49 als eingefrorener, unpromotierter Kandidat für einen ganzen
negativen Blind-Wedge. Dieser Kandidat ist für die heutige Strong-Terminal-Arbeit nicht
notwendig und wird nicht parallel weiterentwickelt.

### Buchung

\[
\boxed{
\mathrm A:
\text{ universelle SW1-Injektivitätsroute negativ geschlossen;}
\quad
\text{Salvage-/Wedge-Kandidat geparkt.}
}
\]

A liefert weder einen Strong-Terminal-No-Go noch eine Aussage über Objekt X oder RH.

---

## B. Strong Terminal / C6 — aktive Hauptfront

### Ziel

Für feste Radien \(0<R<S\) ist zu entscheiden, ob der echte Future-Transport
\[
W_{R,S}^{[U]}
\]
für \(U\to\infty\) stark konvergiert.

Diese Frage ist unabhängig von A.

### B0 — R38 bis R42: strukturelle Reduktion

R38--R42 sind jeweils

\[
\boxed{
\text{FROZEN — independently verified AI-GREEN}
}
\]

ohne automatische kanonische \(\checkmark[M]\)-Promotion.

Die Kette liefert insbesondere:

- Modulus-/WOT-Clustergeometrie;
- exakten Cross-Terminal-Cauchy-Gate;
- Dualnormalen-Skala und zweiten Gamma-Layer;
- strikte intrinsische Monotonie \(\gamma_R<\gamma_S\);
- tangentiale Polar-Konvergenz;
- starke Konvergenz des **echten** Future-Transports auf
  \[
  H_R^0=\ker\beta_R^{(0)}.
  \]

Damit bleibt für jedes feste Paar nur noch eine Normalrichtung.

Mit
\[
\varepsilon_R=e_{R,0}
\]
ist Strong Terminal äquivalent zu
\[
\boxed{
\operatorname{Re}
\langle
\varepsilon_R,
K_{R,S}^{T,U}\varepsilon_R
\rangle
\to1
\qquad(T,U\to\infty).
}
\]

### B1 — R43: terminalfreie Gamma-Dichte

R43 ist **OPEN** mit gemischtem reviewed/candidate Status.

Bereits extern destruktiv GREEN sind insbesondere:

- R43.1--R43.6;
- R43.10a--R43.10m;
- R43.10n--R43.10v;
- die explizit reparierte Analytizitätsargumentation R43.10ak--R43.10au;
- Lemma R43-GC1 als selbständiger Hilbertraum-/Hardy-Baustein.

Die Krein--de-Branges-Literaturschnittstelle wurde source-checked und dabei präzisiert:
Diagonalität des kanonischen Hamiltonians liefert einen skalaren odd channel, aber nicht
automatisch absolute Stetigkeit der natürlichen Radiusvariable.

Daraus entstand die Trennung

\[
\mathrm{GC\!-\!M1}_{\rm scalar}
\qquad\text{und}\qquad
\mathrm{GC\!-\!AC}.
\]

Aktuell gilt:

\[
\boxed{
\mathrm{GC\!-\!M1}_{\rm scalar}
\text{ candidate-GREEN}
}
\]

und §3K liefert den neuen, noch unabhängig zu prüfenden Kandidaten

\[
\boxed{
\mathrm{GC\!-\!AC}
\text{ candidate-closed}
}
\]

über die totale Familie höherer constrained Gamma-Rieszvektoren
\[
\{g_{m,S}:m\ge1\}.
\]

Die Kernidee:

1. die Jets \(\beta_S^{(m)}\) sind auf dem odd finite-window Raum total;
2. die Rieszvektoren \(g_{m,S}\) sind daher dicht in \(H_S^0\);
3. jedes einzelne Radius-Nestmaß
   \[
   d\|P_Q^\Gamma g_{m,S}\|^2=d\gamma_m(Q)
   \]
   ist absolut stetig in \(Q\);
4. ein gemeinsamer singulär-kontinuierlicher Nestkanal wäre zu allen dichten
   \(g_{m,S}\) orthogonal und ist daher unmöglich.

**Nächster B1-Gate:** unabhängiger destruktiver Review von R43 §3K und des
\(\mathrm{GC\!-\!M1}_{\rm scalar}\)-Inputs.

### B2 — letzter Normal-Skalar

Falls der B1-Kandidat hält, kollabiert jeder schwache Cluster der letzten Normalbahn auf
\[
\mathbb C\varepsilon_S.
\]

Dann bleibt nur
\[
\boxed{
b_U
:=
\langle
W_{R,S}^{[U]}\varepsilon_R,
\varepsilon_S
\rangle.
}
\]

Der endgültige Strong-Terminal-Gate lautet dann
\[
\boxed{
b_U\to b,
\qquad
|b|=1
\quad?
}
\]

Mögliche Ausgänge:

- positiver Abschluss: Strong Terminal für das feste Paar;
- persistenter Norm-/Phasendefekt: konkreter Strong-Terminal-No-Go;
- fehlende Cauchy-/Grenzkonvergenz: ebenfalls negativer Abschluss.

### B3 — Governance-Abschluss

Erst wenn B1 und B2 unabhängig geschlossen sind:

1. R43 final auditieren;
2. Strong-Terminal-Status exakt buchen;
3. entscheiden, welche Aussagen kanonisch promotierbar sind;
4. prüfen, welche Teile in ein konsolidiertes P11-Nachfolgepaper gehören.

---

## R. Separater R37-Analytikpfad — G4c bleibt offen

R37 bleibt **separat** von B.

Der finite/algebraische R37-Certificate-Scope ist reproduzierbar GREEN, aber der interne
analytische Promotionsblocker G4c bleibt offen:

\[
\text{reales Segment}
\to
\text{holomorphe Identität auf dem Annulus}
\to
\text{Laurent-Separation}.
\]

R38--R43 dürfen R37 nicht rückwirkend promotieren.

### Nächster R37-Schritt

Nur wenn strategisch wieder aufgenommen:

- G4c vollständig unabhängig schließen oder widerlegen;
- danach erst R37 als ganzen Satz neu bewerten.

R37 ist **nicht** der nächste Default, solange B/R43 produktiv bleibt.

---

## C. Erster echter X-Kandidat

### Ziel

Formuliere einen intrinsischen, nicht-zirkulären Kandidaten für eine gemeinsame
Prime-/Archimedes-Geometrie, der mindestens spezifiziert:

- den Hilbertraum bzw. die intrinsische Geometrie;
- den gemeinsamen Mediator-/Gram-Mechanismus;
- den Prime-power-Kanal;
- den archimedischen Kanal;
- Testklasse und Normalisierung;
- die nichtorthogonale globale Kopplung.

A und B können Kandidatenbausteine liefern, sind aber keine definitorisch notwendigen
Voraussetzungen.

### Status

\[
\boxed{
\text{Noch kein X-Kandidat im Sinn der kanonischen Arbeitsdefinition.}
}
\]

---

## D. Exakte vollständige Weil-Gram-Identität

Für einen konkret spezifizierten Kandidaten aus C ist separat zu beweisen:

\[
\boxed{
Q_W(f,g)
=
\langle T_Xf,T_Xg\rangle_{\mathcal K_X}
}
\]

auf der richtigen vollständig normalisierten Weil-Testklasse.

Nicht ausreichend sind:

- nur ein positiver Teil der Weil-Form;
- eine nachträgliche GNS-Faktorisierung bereits vorausgesetzter Positivität;
- getrennte orthogonale Prime-/Archimedes-Kanäle ohne gemeinsamen geometrischen Ursprung.

### Status

\[
?[O]
\]

weil noch kein geeigneter X-Kandidat vorliegt.

---

## E. Weil-Kriterium / RH-Rückbindung

Erst nach D ist separat zu prüfen:

1. welche Weil-Form exakt realisiert wurde;
2. auf welcher Testklasse;
3. mit welchen Fourier-/Gamma-/Pol-Normalisierungen;
4. welche Positivität exakt folgt;
5. welches präzise Weil-Kriterium auf diesem Scope gilt.

Kein Resultat aus A, B, R37 oder C allein ist eine RH-Aussage.

---

## F. Konsolidierungs- und Publikationsspur

Parallel zur Mathematik:

1. R38--R43 nach Abschluss der aktuellen Front in einen konsolidierten Strong-Terminal-
   Abschnitt bzw. ein eigenständiges Paper überführen;
2. P11-Freeze unangetastet lassen; spätere Strong-Terminal-Arbeit als Post-Freeze-Linie
   sauber trennen;
3. P12 weiterhin als separaten Adelic-Hub-Injektivitätsstrang behandeln;
4. ältere NEU-/SYN-Navigationssnapshots archivieren, ohne ihre Provenienz zu verlieren;
5. CURRENT-FRONT, ACTIVE_THEOREM_REGISTRY und diese Roadmap als operative
   Einstiegsschicht klein und aktuell halten.

---

## Wo stehen wir auf dieser Roadmap?

Nach **Meilensteinen**:

- A: negativ entschieden / strategisch abgeschlossen;
- B: tief fortgeschritten, aber mathematisch noch offen;
- C: noch nicht erreicht als konkretes Deliverable;
- D: offen;
- E: offen.

Eine grobe Meilensteinposition wäre daher etwa

\[
\boxed{
\text{zwischen dem ersten und zweiten großen Roadmapblock, ungefähr }35\%-40\%
}
\]

wenn man nur die Anzahl strategischer Stufen zählt.

Diese Prozentzahl ist **keine Schätzung der verbleibenden mathematischen Schwierigkeit**.
C--E könnten schwerer sein als alles bisherige zusammen.

---

## Nächste Default-Arbeitsfolge

1. **R43 §3K extern destruktiv prüfen**:
   höhere Jet-Totalität, höhere Gamma-Rieszvektoren, absolute Stetigkeit der
   \(\gamma_m\)-Nestmaße, Maßargument \(\Rightarrow\) GC-AC.
2. Falls GREEN: **Gamma-Dichtefront schließen** und R43 auf den Normal-Skalar \(b_U\)
   reduzieren.
3. **\(b_U\) direkt angreifen**: Existenz, Betrag, Phase.
4. Strong Terminal positiv oder negativ entscheiden.
5. Erst danach strategisch wählen:
   - B-Ergebnis in X-Kandidatenarchitektur überführen;
   - oder R37/G4c wieder aufnehmen;
   - oder einen neuen unabhängigen C-Kandidatenpfad öffnen.

---

## Kanonische Referenzen

- CURRENT-FRONT.md
- 00-uebersicht/ACTIVE_THEOREM_REGISTRY.md
- audits/P11_REFEREE_E2E_R38_MODULUS_WEAK_CLUSTER_GEOMETRY_2026-09-01.md
- audits/P11_REFEREE_E2E_R39_STRONG_TERMINAL_BASELINE_FIREWALL_2026-09-01.md
- audits/P11_REFEREE_E2E_R40_DUAL_NORMAL_NEXT_ORDER_SCALE_2026-09-01.md
- audits/P11_REFEREE_E2E_R41_SECOND_ORDER_HARD_CONSTRAINT_GAMMA_LAYER_2026-09-01.md
- audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md
- audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md
- 00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md

---

**Kurzfassung**

\[
\boxed{
\begin{array}{ll}
\mathbf A & \text{universelle finite SW1-Route negativ geschlossen}\\[1mm]
\mathbf B & \text{Strong Terminal: aktive Front, aktuell R43 / GC-AC }\to b_U\\[1mm]
\mathbf R & \text{R37/G4c separat offen}\\[1mm]
\mathbf C & \text{erster echter X-Kandidat}\\[1mm]
\mathbf D & Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}\\[1mm]
\mathbf E & \text{präzise Weil-Kriterium-/RH-Rückbindung}
\end{array}
}
