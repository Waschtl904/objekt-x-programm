# CURRENT FRONT — Objekt X / P11-R32

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 1. September 2026  
> **Aktuelle mathematische Basis:** `main@cf3d39a2e7787bc1c5b938390b6cdeec7943b0c2`. Die M1-ND-IMG4-SMALLR-Promotion ist integriert (`✓[M]_neg`). PR #49 (`research/sw1-m1-nd-salvage-phase-diagram`, geprüfter Head `2ed1583f074574c2fdb5a48203d63d520a86b5f6`) bleibt bewusst **offen und eingefroren** als intern adversarial GREEN geprüfter, aber unpromotierter Uniform-Blind-Wedge-Kandidat; finaler Review-Run `33532345053` SUCCESS. Frühere Promotions-/Certificate-Aussagen behalten ihre jeweils kanonischen Provenienzen.  
> **Aktiver mathematischer Stand:** A / finite-level Cross-Gram ist im universellen SW1-Sinn **negativ entschieden**; PR #49 verstärkt dies als Kandidat möglicherweise zu einem ganzen offenen Wedge, wird aber nicht weiter verändert und nicht promotet. **Aktive Forschung wechselt jetzt zu B / Strong Terminal.** Erster Zielknoten ist R27-F: den festen Gamma-Crossblock bzw. den Grenzdefekt `D_infty^-` entscheiden. Danach folgt separat R22-F: der positive fixed-vector Polar-Gauge-/Angle-Defect.  
> **Detailregistry:** [ACTIVE_THEOREM_REGISTRY](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md)

Diese Datei ist die **operative Navigationsschicht** des Repositories. Sie ist kein mathematischer Beweis und erzeugt keine Statuspromotion. Ihre Aufgabe ist, den gegenwärtigen Forschungsangriff, seine erlaubten Inputs und die ausdrücklich nicht benötigten Nebenfronten sichtbar zu halten.

---

## 1. Aktuelles Ziel

Die aktive Front ist **nicht** „Objekt X vollständig konstruieren“ und **nicht**
„RH beweisen“.

Operativ sind jetzt zwei Achsen getrennt:

1. **A / M1-ND-SALVAGE:** PR #49 ist als geprüfter Kandidat eingefroren; keine weitere Arbeit und keine Promotion ohne bewusstes Reopening.
2. **B / Strong Terminal:** aktive Forschungsachse; zuerst R27-F, danach R22-F.

Der bisherige universelle Zielknoten

\[
\ker\mathscr N_R=\{0\}
\qquad
\text{für alle SW1-Parameter}
\]

ist durch M1-ND-IMG4-SMALLR negativ entschieden.

Promotet ist der explizite Witness

\[
\boxed{
\varepsilon_0=\Delta/4,\qquad
R_0=T/100000,\qquad
\sigma_0=R_0/2,
}
\]

mit

\[
\boxed{
\ker\mathscr N_{R_0}\ne\{0\}.
}
\]

Status:

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SMALLR}:\checkmark[M]_{\rm neg}.
}
\]

Damit ist **universelle SW1-Cross-Gram-Nichtentartung in der aktuellen
finite-level Geometrie ausgeschlossen**.

Der neue eng gefasste Frontknoten lautet:

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SALVAGE}
}
\]

mit zwei möglichen Richtungen:

1. **Parameterklassifikation:** Bestimme den maximalen Restbereich, auf dem
   \(\ker\mathscr N_R=\{0\}\) noch möglich oder beweisbar ist.
2. **Architekturreparatur:** Ändere die finite-level Kopplung so, dass der
   durch FREE-Komponentensättigung erzeugte Small-\(R\)-Blindraum nicht mehr
   existiert.

Die allgemeine Aussage

\[
\forall\,0<\varepsilon<\Delta/2\ \exists R_\varepsilon^*>0:
\quad
0<R<R_\varepsilon^*,\ 0<\sigma<R
\Longrightarrow
\ker\mathscr N_R\ne0
\]

bleibt vorerst **Kandidat**, nicht mitpromotet.

**Scope-Firewall:** Die Promotion betrifft den tatsächlichen zulässigen Raum

\[
\mathscr B_K\oplus\mathscr B_W
\]

bzw. die dazu äquivalente IMG0/IMG2-Darstellung, nicht den größeren formalen
Slot-Ambientraum. Keine separate Promotion von \(\ker\Gamma_I\ne0\), kein
Objekt-X-Abschluss und keine RH-Folgerung.

---

## 2. Was bereits kostenlos zur Verfügung steht

### 2.1 Äußerer Hub — formal bewiesen

P12 liefert bereits:

\[
\boxed{
0<R<T,\qquad \sigma\le R
\Longrightarrow
\ker L_{R,S,T_0}^{\{a,b,2a\}}=\{0\}.
}
\]

Status:
\[
\boxed{\checkmark[M]}
\]

Quelle:
\`papers/P12_Adelic_Hub_Injectivity_Program.tex\`, Corollary \`cor:p12-consolidated\`.

SW1 liegt vollständig in diesem Bereich. Daher muss die äußere Hub-Injektivität für den SW1-Angriff **nicht neu bewiesen** werden.

### 2.2 Aktuelle Tail-/FG-/Kernel-Kandidaten

HT-A1, HT-A2, HT-A3 und HT-A4a sind AI-GREEN geprüfte Kandidaten, aber nicht formal promotet.

FG-1, FG-TR1, die \(\widehat\Phi_R\)-Normalform und CG-FG1 sind ebenfalls AI-GREEN Kandidaten-/Kompositionsresultate ohne formale Promotion.

SW1-KNF (\`audits/P11_R32_SW1_KNF_CANDIDATE.md\`, PR #15) ist ein AI-GREEN Kandidat, der auf SW1 eine vollständige sektorale Kernel-Normalform liefert und dort die globale FG-TR1-Blackbox ersetzt.

SW1-BL7 (\`audits/P11_R32_SW1_BL7_CANDIDATE.md\`, PR #16) ist ein AI-GREEN Kandidat: für \(s\in(R,\varepsilon)\) gilt \(2d+s\in(a+R,b-R)\subset\mathcal Z_{R,\mathrm{SW1}}^{\rm phys}\), für jedes \(s\), als siebter direkter Blindwert neben den sechs promoteten.

SW1-2TP (\`audits/P11_R32_SW1_2TP_CANDIDATE.md\`, PR #17) ist AI-GREEN + \`independent GREEN (certificate)\`: die beiden \(T\pm s\)-Rows wurden direkt aus den elf Wörtern von \(A\) hergeleitet; \(M_T\) ist uniform positiv invertierbar; das reproduzierbare Zertifikat \`scripts/certify_sw1_2tp_ledger.py\` (Python/SymPy 1.14.0) prüft 88 Echo-Fälle, Hub-Support, Pivot und Eigenkanäle mit PASS. Der Perplexity-Blindcheck ist dokumentiert FAIL und erzeugt kein cross-model GREEN.

SW1-AWI (\`audits/P11_R32_SW1_AWI_CANDIDATE.md\`, PR #18) ist AI-GREEN + \`independent GREEN (certificate)\`: die A-Wall-Dichotomie ist vollständig fallweise normalisiert; in der oberen Kammer wirkt die Kollision über die maßtreue Reflexion \(s\mapsto\Delta-s\), und der zugehörige Zwei-Kanal-Block ist strikt invertierbar. Das Vollzertifikat \`scripts/certify_sw1_awi.py\` (Python/SymPy 1.14.0) prüft Geometrie, Fixpunkt, Koeffizientenordnung, Eigenkanäle und Invertierbarkeit mit PASS. Perplexity ist PARTIAL/FAIL und erzeugt kein cross-model GREEN.

Keine dieser Kandidatenzeilen trägt eine Promotion; keine Aussage über A0, HT-RED oder \(\ker\Gamma_I\).

Exakte Status- und Quellenliste:
[ACTIVE_THEOREM_REGISTRY](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

---

## 3. Gemergter Zwischenmeilenstein: PR #10

PR #10 theorematisiert nur den einfachen SW1-Membership-Satz und ist inzwischen in \`main\` gemergt.

Ziel/Kern (§12, vollständig):
\[
\boxed{
\begin{array}{l}
s,\ a-s,\ a+s,\ T-s,\ 2d-s,\ T+s\ \text{sind auf SW1 direkte Blindwerte, }(Z,Z,Z,Z,Z,Z),\\
D_-,\ D_0,\ D_+,\ E,\ A_*>\varepsilon,\\
I_b\cap I_-=\emptyset,\qquad I_b\cap I_+\neq\emptyset\iff\varepsilon>\Delta/2,\\
\text{inkl. korrektem Berührungsfall bei }\varepsilon=\Delta/2.
\end{array}
}
\]

Der Beweis in PR #10 ist absichtlich selbständig und verwendet HT.17/18, HT.23–27, FG-TR1 und HT-A4a **nicht als Beweisblackboxen**.

Aktueller Status:

\[
\boxed{
\mathrm{HT\!-\!A4b\!-\!SW1\!-\!M}:\checkmark[M]
}
\]

Promotet mit kanonischem Promotionsrecord \`audits/P11_R32_HT_A4B_SW1_M_PROMOTION.md\`. Exakter adversarial und mechanisch geprüfter Review-Head: \`f8f9f107b9c6879611ecb492979737a5541141e9\`; Squash-Merge in main: \`b06f50f12973e781b87db8b06e54fd590a053b10\`. Keine Mitpromotion von HT-A4b global, HT-RED, A0 oder Schur-Cross-Gram.

---

## 4. Nächster mathematischer Schritt

PR #40 hat den bestehenden A2–A10-Stack rückwärts reconciliert.

Der historische erste Bruch der alten linearen Strategie liegt bei

\[
\boxed{
\mathrm{A3}\to\mathrm{A4},
}
\]

weil A4–A9 Struktur-/No-Go-/Separatoraussagen liefern, aber keine weitere Implikation
\[
\ker\Gamma_I=\{0\}.
\]

Operativ ist dieser alte Bruch jedoch durch A10-C0 umgangen: Statt \(\mathfrak G_R^{-1}\) explizit auszurechnen, wird der inversefreie Operator

\[
\boxed{
\mathscr C_R(\xi,w)
=
(I+A)J_R\xi+HE_{\mathcal A}w
}
\]

verwendet. PR #40 härtet die beidseitige Korrespondenz mit

\[
\Theta=J_R\oplus I_{\mathscr W},
\qquad
\Theta^{-1}(y,w)=(\Psi_Ry,w),
\]

und damit

\[
\boxed{
\ker\mathscr C_R
\xrightarrow{\sim}
\ker\mathcal K_{I,A}
\xrightarrow{\sim}
\ker\Gamma_I.
}
\]

C1C1 transportiert weiter mittels

\[
W=(U_H|_K)\oplus U_W
\]

auf den echten Bildraum

\[
\mathcal R_K\oplus\mathcal R_W,
\]

mit explizitem

\[
W^{-1}(F,G)
=
\bigl((U_H|_K)^{-1}F,U_W^{-1}G\bigr).
\]

Somit

\[
\boxed{
\ker\widehat{\mathscr C}_R
\cong
\ker\mathscr C_R
\cong
\ker\Gamma_I.
}
\]

Der Ambientraum ist ausdrücklich größer:
\[
WW^*=P_{\operatorname{Ran}W}\ne I_{\rm ambient}
\]
im Allgemeinen. Das PR-#40-Zertifikat konstruiert sogar einen nichttrivialen künstlichen Ambient-Kernelvektor; daher ist diese Scope-Grenze zwingend.

M1-FULL liefert im tatsächlichen \(r\)-Scope die exakte finite-range Darstellung

\[
\boxed{
(\widehat{\mathscr C}_R F)(\theta)
=
\sum_{j=-3}^{3}
M_j(\theta)F(\theta+j\Delta).
}
\]

Damit ist der frühere universelle M1-ND-Knoten nicht mehr offen, sondern
negativ entschieden.

### 4.1 M1-ND-SALVAGE — eingefrorener Kandidatenstand

1. Der promotierte Small-\(R\)-Kernelmechanismus bleibt feste Firewall.
2. PR #49 dokumentiert zusätzlich einen intern GREEN geprüften Kandidaten für den offenen Wedge
   \[
   0<\varepsilon<\frac{T-10\Delta}{8},\quad 0<R<\varepsilon,\quad 0<\sigma<R,
   \]
   mit explizitem \(R\)-unabhängigem Blindset. Dieser Satz ist **nicht promotet**.
3. PR #49 bleibt auf Head `2ed1583f074574c2fdb5a48203d63d520a86b5f6` eingefroren; keine weiteren Commits, solange A nicht bewusst wieder geöffnet wird.
4. Die Restparameterklassifikation bleibt `?[O]`, ist aber derzeit nicht die aktive Forschungsachse.

Ein punktweiser Rang- oder Determinantentest nur von \(M_0(\theta)\) genügt
weiterhin nicht.

**Firewall:** Die negative Promotion ist ein Satz über die aktuelle
M1-ND-Geometrie am expliziten Witness. PR #49 ist nur Kandidatenfortschritt.
Kein HT-RED, kein Objekt-X-Abschluss und keine RH-Folgerung.

### 4.2 Aktive Forschungsachse: B / Strong Terminal

Der historische C6-Strang ist lokal geschlossen und hat den residualspektralen
Blocker exportiert. Die heutige Strong-Terminal-Frage ist auf zwei getrennte
Restgates reduziert:

1. **R27-F / Modulus-Gate**
   [
   D_infty^-
   =
   T_{S,infty}W-WT_{R,infty}
   stackrel{?}=0.
   ]
   Äquivalent ist ein fester Gamma-Crossblock auf einem fixed window zu
   entscheiden. Dies ist der **nächste Default-Angriff**.

2. **R22-F / Polar-Gauge-Gate**
   [
   mathscr G_U=(V_U-W)^*(V_U-W)
   stackrel{s}{longrightarrow}0 ?
   ]
   Dieser fixed-vector Angle-Defect ist logisch separat und bleibt auch nach
   einem positiven R27-F zu prüfen.

Bereits vorhanden sind die finite Terminalalgebra, die negative absolute
Metrikgrenze, die Cross-Terminal-Cauchy-Identität, uniforme relative
Coercivity sowie Mosco-/Resolvent- und inverse-root-Grenzen.

---

## 5. Was derzeit ausdrücklich **nicht** bearbeitet wird

Nach der negativen M1-ND-Promotion bleiben folgende Fronten **nicht automatisch Priorität**; sie werden nur vorgezogen, wenn die neue Salvage-/Architekturroute sie benötigt:

- globale HT-A4b-Exhaustivität aller 15 Chambers;
- P12-Restproblem \(0<R<\rho,\ R<\sigma\);
- Round-29-/\(M_{68}\)-Übertragung;
- neue globale Low-Radius-Schwellen;
- Closed Range / bounded below;
- Konstruktion des finalen \(\mathcal K_X\);
- Objekt X als abgeschlossenes Objekt;
- RH.

**Wichtig:** „nicht Priorität“ bedeutet nicht „irrelevant“ oder „widerlegt“. A / PR #49 ist derzeit bewusst geparkt; B / Strong Terminal ist dagegen jetzt aktiv.

---

## 6. Warum Round 29 / \(M_{68}\) aktuell nicht gebraucht wird

Round 29 gehört zur schwierigen P12-Restfront mit
\[
R<\sigma.
\]

SW1 arbeitet dagegen mit
\[
\sigma\le R.
\]

Genau für diesen restricted-tail-Bereich besitzt P12 bereits ein globales \(\checkmark[M]\)-Resultat.

Daher lautet die operative Regel:

\[
\boxed{
\text{Kein Round-29-/}M_{68}\text{-Angriff, solange SW1 nicht als unzureichend erwiesen ist.}
}
\]

---

## 7. Lesereihenfolge für jede neue Arbeitssitzung

Vor einer neuen Rechnung ist in dieser Reihenfolge zu lesen:

1. **\`CURRENT-FRONT.md\`** — Was ist heute die aktive Frage?
2. **\`00-uebersicht/ACTIVE_THEOREM_REGISTRY.md\`** — Welche Resultate dürfen mit welchem Status benutzt werden?
3. **Kanonische Quelle des benötigten Inputs** — Paper oder Promotionsrecord.
4. **Aktueller Kandidatenaudit / aktiver PR** — nur die konkrete Front.
5. **Historische Audits / Journal** — nur bei einer klar benannten Provenienz-, Fehler- oder Gegenbeispielfrage.

Nicht mit einer Volltextsuche durch das ganze Repo beginnen, solange Stufen 1–4 die Frage beantworten.

---

## 8. Epistemische Autorität

Die Lesereihenfolge ist nicht identisch mit der mathematischen Autorität.

Für mathematische Aussagen gilt:

\[
\boxed{
\text{formaler Promotionsrecord / konsolidierter Paper-Satz}
>
\text{independent GREEN}
>
\text{AI-GREEN Kandidat}
>
\text{ungeprüfter Kandidat}
>
\text{historischer Entwurf}
}
\]

### 8.1 Statusnomenklatur (verbindlich)

\[
\boxed{\text{AI-GREEN}}
\]
= interne KI-Konstruktion plus kritische Zweitprüfung (durch dasselbe oder ein zweites KI-System im selben Kontext); **keine** unabhängige Verifikation.

**Subtypen von \`independent GREEN\`** (kumulativ buchbar; ein Kandidat kann mehrere Subtypen gleichzeitig tragen, ohne dass dies eine menschliche Prüfung suggeriert):

| Subtyp | Bedeutung | Pflichtangaben |
|---|---|---|
| **independent GREEN (cross-model)** | Ein separates Modell/System prüft den exakten Satz **ohne Kenntnis** unserer Zielrechnung. Für 2TP zwingend: frische Perplexity-Session ohne diesen Thread-Verlauf. Kennt die prüfende Session bereits unsere Zielmatrix/diesen Verlauf, wird das Ergebnis höchstens als „cross-model nonblind“ protokolliert — das erzeugt **kein** \`independent GREEN\`. | Typ, Methode, Prüfer/System (inkl. Blind-/Nonblind-Vermerk), exakter geprüfter Head, exakter Satz/Scope, Verdict |
| **independent GREEN (certificate)** | Reproduzierbares maschinelles/algebraisches Zertifikat (z. B. Python/SymPy/CAS-Skript), das den endlichen algebraischen Teil bestätigt. | zusätzlich: Tool/Version, Zertifikatsdatei bzw. Skriptpfad, exakter geprüfter Git-Head, reproduzierbares Ergebnis (Output dokumentiert) |
| **independent GREEN (human)** | Unabhängige Prüfung durch einen externen Menschen. | zusätzlich: Reviewer bzw. nachvollziehbare Review-Provenienz |

**Verbindliches Buchungsschema für jede \`independent GREEN\`-Zeile:**
\[
\boxed{
\text{Typ}+\text{Methode}+\text{Prüfer/System}+\text{exakter Head}+\text{exakter Satz/Scope}+\text{Verdict}
}
\]
Fehlt eine dieser Angaben, gilt die Buchung als unvollständig und darf nicht als \`independent GREEN\` gezählt werden.

\[
\boxed{\checkmark[M]}
\]
= formaler Objekt-X-interner Promotionsstatus, unabhängig davon, ob zusätzlich externe Begutachtung existiert. **Kein** Ersatz für Fachjournal- oder Peer-Review-Verifikation. Orthogonal zu allen obigen Subtypen — eine \`✓[M]\`-Promotion setzt keinen bestimmten \`independent GREEN\`-Subtyp voraus und umgekehrt.

**Beispiel für eine kumulative Buchung (Zielbild für SW1-2TP, noch nicht erreicht):**
\[
\boxed{
\text{AI-GREEN}+\text{independent GREEN (cross-model)}+\text{independent GREEN (certificate)}
}
\]
ohne dass dabei suggeriert wird, es liege bereits eine \`independent GREEN (human)\`-Prüfung vor.

### 8.2 Wo ein Mensch tatsächlich gebraucht wird

Für elementare, endliche Bausteine wie SW1-BL7 (\(a+R<2d+s<b-R\)) ist die Beweislast überschaubar; AI-GREEN plus ggf. cross-model/certificate ist ausreichend. Mit steigender Tragweite steigt die Schwelle:

- SW1-2TP: AI-GREEN + mindestens ein \`independent GREEN\`-Subtyp vor Promotion.
- \(\Delta\)-Descent: höhere Schwelle, mehrere Subtypen empfohlen.
- ein möglicher SW1-Gesamtsatz (\(\ker\mathcal K_{I,A}=\{0\}\) auf ganz SW1) oder eine öffentliche Behauptung eines großen Resultats: **independent GREEN (human)** durch einen externen Fachmathematiker wird empfohlen, bevor eine öffentliche Behauptung erfolgt — funktionalanalytische Domain-, Closure-, a.e.- und Operatoridentifikationsfragen können dort subtil werden.

\`CURRENT-FRONT.md\` und die Registry sind **Navigationsdateien**. Bei einem Konflikt entscheiden die kanonischen mathematischen Quellen.

---

## 9. Fünf-Punkte-Regel für mathematisch relevante Merges

Ein mathematisch relevanter Merge gilt operativ erst dann als vollständig abgeschlossen, wenn alle fünf Punkte erfüllt sind:

1. **PR gemergt** — exakter Merge-Commit bekannt.
2. **Main mechanisch verifiziert** — tatsächlicher Main-SHA und Diff geprüft.
3. **Registry geprüft** — falls Status, Scope, Quelle oder aktive Abhängigkeit betroffen sind, \`ACTIVE_THEOREM_REGISTRY.md\` aktualisieren.
4. **Front aktualisiert** — \`CURRENT-FRONT.md\` auf neuen Main-SHA, aktuellen offenen Knoten und nächsten Schritt bringen.
5. **Erst dann Abschluss buchen** — kein neuer mathematischer Angriff auf Basis eines veralteten operativen Frontstands.

Kurz:

\[
\boxed{
\text{Merge}
\to
\text{Main-Check}
\to
\text{Registry}
\to
\text{Current Front}
\to
\text{nächste Mathematik}
}
\]

---

## 10. Änderungen an dieser Datei

Diese Datei soll **klein und operativ** bleiben.

Sie wird geändert, wenn sich mindestens eines ändert:

- aktueller Main-SHA nach mathematisch relevantem Merge;
- aktiver Zielknoten;
- aktiver PR / Promotionskandidat;
- verwendbarer Inputstatus;
- nächster konkreter Rechenschritt;
- eine bewusst geparkte Front wird wieder aktiv;
- eine Änderung der Statusnomenklatur selbst (§8).

Sie soll **nicht** historische Forschungsprovenienz duplizieren. Dafür bleiben Journal, Papers, Audits und Promotionsrecords erhalten.

---

## 11. Aktueller Kurzstatus

\[
\boxed{
\begin{array}{ll}
\text{P12 restricted-tail outer Hub} & \checkmark[M] \\
\text{HT-A4b-SW1-M} & \checkmark[M] \\
\text{SW1-KNF} & \text{AI-GREEN candidate, keine Promotion} \\
\text{SW1-A-FOLD} & \text{AI-GREEN + independent GREEN (certificate, alg./mech. scope)} \\
\text{SW1-2TP} & \text{AI-GREEN + independent GREEN (certificate)} \\
\text{SW1-AWI} & \text{AI-GREEN + independent GREEN (certificate)} \\
\text{SW1-}\Delta\text{-DESCENT (gesamt)} & ?[O] \\
\text{SW1-A0} & \text{AI-GREEN + independent GREEN (certificate)} \\
\text{SW1-A1} & \text{AI-GREEN + independent GREEN (certificate)} \\
\text{SW1-A2} & \text{AI-GREEN + independent GREEN (certificate, alg./mech. scope)} \\
\text{SW1-A3} & \text{AI-GREEN + independent GREEN (certificate, alg./mech. scope)} \\
\text{SW1-A4} & \text{AI-GREEN + independent GREEN (certificate)} \\
\text{SW1-A5} & \text{AI-GREEN + independent GREEN (certificate)} \\
\text{SW1-A6} & \text{AI-GREEN + independent GREEN (certificate)} \\
\text{SW1-A7} & \text{AI-GREEN + independent GREEN (certificate)} \\
\text{SW1-A8} & \text{AI-GREEN + independent GREEN (certificate)} \\
\text{SW1-A9 gesamt} & ?[O] \text{; J0/J1/FS/DOM + SEP-SMALL zertifiziert} \\
\text{A10-H3-INF} & \text{AI-GREEN + independent GREEN (cross-model blind review)} \\
\text{A10-C2-M1-RAW} & \text{independent GREEN (certificate)} \\
\text{A10-C2-M1-FULL}(7/2) & \text{independent GREEN (certificate)} \\
\text{C1B2A-CHIRO} & \checkmark[M] \text{ + independent GREEN (certificate)} \\
\text{C1B2A-TRANSFER} & \checkmark[M] \\
\text{M1-FULL}(r),\ 3<r<4 & \text{kanonische Konsequenz aus Referenz-Certificate + Transfer} \\
\text{M1-ND-SMALLR} & \checkmark[M]_{\rm neg} \\
\text{SW1-A10 / M1-ND universal} & \checkmark[M]_{\rm neg}\text{ am expliziten Witness; Restparameterklassifikation }?[O] \\
\text{HT-RED} & ?[O] \\
\text{Schur Cross-Gram salvage/classification} & ?[O]
\end{array}
}
\]

**Nächster Default:** **M1-ND-SALVAGE / Parameterklassifikation** — den Bereich außerhalb des promotierten Small-`R`-No-Gos untersuchen und zugleich prüfen, welche minimale Kopplungsänderung den Blindraum beseitigt. Die bisherige universelle Injektivitätsroute wird nicht fortgesetzt.

**Firewall:** IMG1 bleibt in seinem dokumentierten Certificate-Scope unpromotiert. Neu promotiert ist ausschließlich `M1-ND-SMALLR: ✓[M]_neg` für den expliziten Witness auf \(\mathscr B_K\oplus\mathscr B_W\). Eine separate formale Promotion von \(\ker\Gamma_I\neq\{0\}\) wird hier nicht gebucht. Offen ist nun die Restparameterklassifikation bzw. Architekturreparatur; kein HT-RED, kein Objekt-X-Abschluss und keine RH-Folgerung.
