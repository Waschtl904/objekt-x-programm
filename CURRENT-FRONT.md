# CURRENT FRONT — Objekt X / P11-R32

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 31. August 2026  
> **Kanonische mathematische Basis:** PR #34, Squash-Merge \`6ac0141b2de3a0b2af98fff6d11c403fe3b379b6\`; **Status-/Navigationssync:** PR #35, Squash-Merge \`25235a9e10ddb6d7244dd27bbc29bf03ada8cd1d\`. Die reproduzierbaren Certificate-Aussagen zitieren weiterhin die tatsächlich im CI geprüften Script-Blobs.  
> **Aktiver mathematischer Stand:** Der C-Strang von SW1-A10 ist bis zur tatsächlichen-\(r\)-M1-Matrixdarstellung geschlossen: M1-RAW und M1-FULL(7/2) sind kanonische reproduzierbare Certificate-Ergebnisse; C1B2A-CHIRO und C1B2A-TRANSFER sind im dokumentierten Scope \`✓[M]\`; damit gilt M1-FULL(\(r\)) für jedes \(3<r<4\) auf offenen Parameterkammern und offenen Kreisatomen. **Keine** Folgerung zu \(\ker\Gamma_I\). Aktiver nächster Knoten ist Roadmap A: **finite-level Cross-Gram-Nichtentartung \(\ker\Gamma_I=\{0\}?\)**, beginnend mit der Odd/even-Faltung.  
> **Detailregistry:** [ACTIVE_THEOREM_REGISTRY](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md)

Diese Datei ist die **operative Navigationsschicht** des Repositories. Sie ist kein mathematischer Beweis und erzeugt keine Statuspromotion. Ihre Aufgabe ist, den gegenwärtigen Forschungsangriff, seine erlaubten Inputs und die ausdrücklich nicht benötigten Nebenfronten sichtbar zu halten.

---

## 1. Aktuelles Ziel

Die aktive Front ist **nicht** „Objekt X vollständig konstruieren“ und **nicht** „RH beweisen“.

Der aktuelle eng gefasste Zielknoten lautet:

\[
\boxed{
\text{Schur-/Cross-Gram-Nichtentartung auf dem einfachen SW1-Parameterwedge}
}
\]

mit
\[
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta,
\qquad
S=T+\sigma,
\qquad
T_0=T+\varepsilon.
\]

Die operative Ja/Nein-Frage ist nach PR #40 nun in ihrer kleinsten aktuellen Form:

\[
\boxed{
\mathrm{M1\text{-}ND}:
\qquad
\widehat{\mathscr C}_R F=0
\Longrightarrow
F=0
\quad
\text{für }F\in\mathcal R_K\oplus\mathcal R_W\ ?
}
\]

Durch die explizit gehärteten Kernelbijektionen ist dies äquivalent zu

\[
\boxed{
\mathscr C_R(\xi,w)=0
\Longrightarrow
\xi=w=0
}
\]

und damit zu

\[
\boxed{
\ker\Gamma_I=\{0\}.
}
\]

**Ambient-Firewall:** \(\widehat{\mathscr C}_R\) darf für M1-ND nicht auf dem gesamten formalen Slotraum getestet werden. Zulässig ist nur der echte C1C1-Bild-/Konsistenzraum
\[
\mathcal R_K\oplus\mathcal R_W,
\]
oder eine exakt äquivalent parametrisierte Darstellung dieses Raums.

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

Damit ist der **einzige aktive mathematische Knoten**

\[
\boxed{
\mathrm{M1\text{-}ND}:
\ker\widehat{\mathscr C}_R=\{0\}
\quad
\text{auf }\mathcal R_K\oplus\mathcal R_W\ ?
}
\]

### 4.1 Zwingende Reihenfolge für M1-ND

1. Den Bild-/Konsistenzraum \(\mathcal R_K\oplus\mathcal R_W\) in M1-Koordinaten explizit charakterisieren.
2. Prüfen, wie die sieben Verschiebungslagen diesen zulässigen Zustandsraum koppeln.
3. Eine äquivalente finite-state Transfer-/Rekurrenzform ableiten, **ohne** einen möglicherweise singulären Außenblock unzulässig zu invertieren.
4. Erst dann Nichtentartung entscheiden:
   \[
   F=0
   \]
   für jede zulässige \(L^2\)-Lösung oder einen exakten zulässigen Gegenvektor konstruieren.

Ein punktweiser Rang- oder Determinantentest nur von \(M_0(\theta)\) genügt nicht.

**Firewall:** Kein Resultat aus PR #40 beweist M1-ND. Keine Promotion, kein HT-RED, kein Objekt-X-Abschluss und keine RH-Folgerung.

---

## 5. Was derzeit ausdrücklich **nicht** bearbeitet wird

Solange der SW1-Angriff nicht scheitert, sind folgende Fronten **nicht Priorität**:

- globale HT-A4b-Exhaustivität aller 15 Chambers;
- P12-Restproblem \(0<R<\rho,\ R<\sigma\);
- Round-29-/\(M_{68}\)-Übertragung;
- neue globale Low-Radius-Schwellen;
- Closed Range / bounded below;
- Polar Gauge / Strong Terminal Transport;
- Konstruktion des finalen \(\mathcal K_X\);
- Objekt X als abgeschlossenes Objekt;
- RH.

**Wichtig:** „nicht Priorität“ bedeutet nicht „irrelevant“ oder „widerlegt“. Diese Fronten werden nur bewusst geparkt, bis der einfachste SW1-Test entschieden ist.

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
\text{SW1-A10 gesamt} & ?[O] \text{ nur noch bzgl. Nichtentartung/Injektivität} \\
\text{HT-RED} & ?[O] \\
\text{Schur Cross-Gram} & ?[O]
\end{array}
}
\]

**Nächster Default:** M1-ND — zuerst den echten C1C1-Bild-/Konsistenzraum \(\mathcal R_K\oplus\mathcal R_W\) in den siebenlagigen M1-Koordinaten explizit charakterisieren; danach eine zulässige Transfer-/Rekurrenzform ableiten und Injektivität oder einen exakten zulässigen Gegenvektor entscheiden.

**Merge-Firewall:** PR #34 promotet ausschließlich C1B2A-CHIRO und C1B2A-TRANSFER im dokumentierten Scope; PR #35 ist reine Status-/Navigationssynchronisation. M1-RAW und M1-FULL(7/2) sind Certificate-Ergebnisse ohne eigene \`✓[M]\`-Promotion. Insbesondere folgen weder \(\ker\Gamma_I=\{0\}\) noch \(\ker\Gamma_I\neq\{0\}\), kein HT-RED, kein Objekt-X-Abschluss und keine RH-Folgerung.
