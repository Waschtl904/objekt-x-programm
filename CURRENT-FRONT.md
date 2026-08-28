# CURRENT FRONT — Objekt X / P11-R32

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 28. August 2026  
> **Verifizierte Main-Basis:** \`5740a38ad4c24e27b7352512e57fb095b245e4d5\` (Squash-Merge PR #16, SW1-BL7-Kandidat AI-GREEN, keine Promotion)  
> **Aktiver mathematischer Stand:** `HT-A4b-SW1-M` ist promotet (\`✓[M]\`, Objekt-X-interner Status); zusätzlich `SW1-KNF` und `SW1-BL7` als AI-GREEN Kandidaten ohne Promotion verfügbar  
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

Keine der beiden Zeilen trägt eine Promotion; keine Aussage über A0, HT-RED oder \(\ker\Gamma_I\).

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

**Unmittelbarer nächster Kandidat: SW1-2TP.** Zeige, dass aus dem tatsächlichen elf-Wörter-Operator \(A\) die beiden gekoppelten Gleichungen bei \(T+s\) und \(T-s\) entstehen:
\[
0=(1+\kappa)y(T+s)+\beta_Ty(T-s)+\cdots,\qquad
0=\beta_Ty(T+s)+(1+\kappa)y(T-s)+\cdots,
\]
mit Tail-Block
\[
M_T=\begin{pmatrix}1+\kappa&\beta_T\\\beta_T&1+\kappa\end{pmatrix},\qquad
\lambda_\pm=1+\kappa\pm\beta_T.
\]

**Methodische Regel:** Die beiden Rows müssen aus den elf Wörtern von \(A\) neu abgeleitet werden — nicht aus einer übernommenen Scratch-Formel. Prüfreihenfolge:
\[
\boxed{
11\text{-Wort-Ledger} \to T+s/T-s\text{-Rows} \to \det M_T>0 \to \text{Summe/Differenz-Kanäle}
}
\]
Erst am Ende wird geprüft, ob \(q\,w(s)\) im Summenkanal verschwindet und im Differenzkanal mit Faktor \(2q\) erscheint — dies darf nicht als vorausgesetzte Formel eingehen.

**Promotionsschwelle für SW1-2TP:** Selbst bei AI-GREEN keine Promotion, bevor mindestens ein \`independent GREEN\` (irgendein Subtyp gemäß §8) oder ein reproduzierbares algebraisches Zertifikat für das 11-Wort-Ledger vorliegt.

**Erforderliche Prüfkette für SW1-2TP (verbindlich, ex ante festgelegt):**
\[
\boxed{
\text{Herleitung (GPT)} \to \text{AI-GREEN (Zweitprüfung)} \to \text{blinder Cross-Model-Check (Perplexity, frische Session)} \to \text{algebraisches Zertifikat}
}
\]
Der Cross-Model-Check erhält ausschließlich Definitionen, SW1-Bedingungen, die elf Wortdaten und die Aufgabenstellung — **keine** Zielmatrix \(M_T\) und keinen Verweis auf diesen Thread. Erfolgt der Check stattdessen in einer Session, die diesen Verlauf bereits kennt, wird das Ergebnis höchstens als „cross-model nonblind“ protokolliert und erzeugt **kein** \`independent GREEN\`.

Noch nicht Teil dieses Schritts: SW1-AWI (A-Wall-Involution \(s\leftrightarrow\Delta-s\)) und der \(\Delta\)-Descent.

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
\text{HT-RED} & ?[O] \\
\text{A0} & ?[O] \\
\text{Schur Cross-Gram} & ?[O]
\end{array}
}
\]

**Nächster Default:** SW1-2TP (simultaner \(T\pm s\)-2×2-Pivot), abgeleitet aus den elf Wörtern von \(A\); Prüfkette gemäß §4/§8 (AI-GREEN → cross-model → certificate) vor Promotion; danach SW1-AWI, \(\Delta\)-Descent.
