# CURRENT FRONT — Objekt X / P11-R32

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 28. August 2026  
> **Verifizierte Main-Basis:** \`dcbe0b005c03f6480693f79ff0d6db5f7ef34ae1\` (Squash-Merge PR #17, SW1-2TP AI-GREEN + independent GREEN (certificate), keine Promotion)  
> **Aktiver mathematischer Stand:** `HT-A4b-SW1-M` ist promotet (\`✓[M]\`, Objekt-X-interner Status); `SW1-KNF` und `SW1-BL7` sind AI-GREEN Kandidaten; `SW1-2TP` ist AI-GREEN + independent GREEN (certificate); alle drei ohne Promotion  
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

Die operative Ja/Nein-Frage ist:

\[
\boxed{
\mathcal K_{I,A}(y,w)=0
\quad\Longrightarrow\quad
y=w=0
\quad\text{auf SW1?}
}
\]

äquivalent zur entsprechenden Schur-/Cross-Gram-Injektivitätsfrage im zulässigen P12-Stratum.

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

Der aktuelle Pfad:

\[
\boxed{
\mathrm{SW1\text{-}KNF} \to \mathrm{SW1\text{-}BL7} \to \mathrm{SW1\text{-}2TP} \to \mathrm{SW1\text{-}AWI} \to \Delta\text{-Descent}
}
\]

Die ersten drei Bausteine sind jetzt auf \`main\` verfügbar; SW1-2TP ist zusätzlich reproduzierbar algebraisch zertifiziert.

**Unmittelbarer nächster Kandidat: SW1-AWI.**

Zu analysieren ist der verbleibende A-Wall-Überlapp im Fall
\[
\varepsilon>\frac{\Delta}{2},
\]
mit Überlappintervall
\[
J=(\Delta-\varepsilon,\varepsilon)
\]
und Involution
\[
\boxed{
\mathcal J_\Delta:s\mapsto\Delta-s.
}
\]

Ziel ist eine endliche Zwei-Kanal-/Reflexionsnormalform des A-Wall-Anteils, bevorzugt durch Zerlegung in symmetrische und antisymmetrische Profile unter \(\mathcal J_\Delta\). Die bereits zertifizierten \(T\pm s\)-Rows aus SW1-2TP dürfen als Input verwendet werden.

**Firewall:** Noch kein \(\Delta\)-Descent, kein HT-RED, kein A0 und keine Aussage über \(\ker\Gamma_I\). SW1-AWI soll ausschließlich die A-Wall-Kopplung normalisieren.

**Prüfdisziplin:** AI-GREEN ist intern; für algebraisch endliche Blöcke soll nach Möglichkeit wieder ein reproduzierbares Zertifikat erzeugt werden. Ein fehlgeschlagener Cross-Model-Check wird als FAIL dokumentiert und nicht in GREEN umgedeutet.

### Erfolgsausgang der Gesamtkette

Falls die innere Rechnung
\[
y=0
\]
erzwingt, kann anschließend P12-RT \(\checkmark[M]\) für den äußeren Hub verwendet werden, um \(w=0\) zu folgern.

### Negativausgang

Falls ein nichttrivialer Restfreiheitsgrad oder Gegenvektor überlebt, ist dieser explizit zu isolieren. Dann ist SW1 allein für den vollständigen Schur-Abschluss nicht ausreichend.

Beide Ausgänge sind verwertbare Forschungsergebnisse.

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
\text{SW1-BL7} & \text{AI-GREEN candidate, keine Promotion} \\
\text{SW1-2TP} & \text{AI-GREEN + independent GREEN (certificate), keine Promotion} \\
\text{SW1-AWI} & ?[O] \\
\text{HT-RED} & ?[O] \\
\text{A0} & ?[O] \\
\text{Schur Cross-Gram} & ?[O]
\end{array}
}
\]

**Nächster Default:** SW1-AWI (A-Wall-Involution \(s\mapsto\Delta-s\)) auf dem Überlappintervall \(J=(\Delta-\varepsilon,\varepsilon)\); danach \(\Delta\)-Descent.
