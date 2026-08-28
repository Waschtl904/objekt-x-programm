# CURRENT FRONT — Objekt X / P11-R32

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 28. August 2026  
> **Verifizierte Main-Basis:** \`0c98c03a332dc7c8e479edc77d8cada678eec376\` (Squash-Merge PR #15, SW1-KNF-Kandidat GREEN, keine Promotion)  
> **Aktiver mathematischer Stand:** `HT-A4b-SW1-M` ist promotet (\`✓[M]\`); zusätzlich `SW1-KNF` als neuer OVERALL GREEN Kandidat ohne Promotion verfügbar (\`audits/P11_R32_SW1_KNF_CANDIDATE.md\`, PR #15)  
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

HT-A1, HT-A2, HT-A3 und HT-A4a sind unabhängig GREEN geprüfte Kandidaten, aber nicht formal promotet.

FG-1, FG-TR1, die \(\widehat\Phi_R\)-Normalform und CG-FG1 sind ebenfalls Kandidaten-/Kompositionsresultate ohne formale Promotion.

**Neu:** SW1-KNF (\`audits/P11_R32_SW1_KNF_CANDIDATE.md\`, PR #15) ist ein OVERALL GREEN Kandidat, der auf SW1 eine vollständige sektorale Kernel-Normalform liefert — disjunkte Samplingfenster \(I_a,I_b,I_T\), explizite Rekonstruktion, \(\mathcal K_R\cong\mathcal Z_R^+\oplus L^2(\mathcal V_R^{SW1})\) — und ersetzt auf SW1 die globale FG-TR1-Blackbox. Keine Promotion, keine Aussage über A0, HT-RED oder \(\ker\Gamma_I\).

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

**Kein weiterer allgemeiner Tail-Pivot-Ansatz mehr als Default.** Mit SW1-KNF steht die vollständige Koordinatenbasis des inneren Kernels bereits zur Verfügung.

Der nächste konkrete Schritt ist eng:

\[
\boxed{
\mathrm{SW1\text{-}KNF} \to \mathrm{SW1\text{-}BL7} \to \mathrm{SW1\text{-}2TP} \to \mathrm{SW1\text{-}AWI} \to \Delta\text{-Descent}
}
\]

**Unmittelbarer nächster Kandidat: SW1-BL7.** Zeige, dass auch \(2d+s\) für \(s\in(R,\varepsilon)\) ein direkter Blindwert ist:
\[
s\in(R,\varepsilon)\quad\Longrightarrow\quad 2d+s\in\mathcal Z_{R,\mathrm{SW1}}^{\rm phys}\quad\text{a.e.}
\]
Noch nicht Teil dieses Schritts: der simultane \(T\pm s\)-2×2-Pivot (SW1-2TP), die A-Wall-Involution (SW1-AWI) und der \(\Delta\)-Descent.

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
\text{GREEN-Kandidat}
>
\text{ungeprüfter Kandidat}
>
\text{historischer Entwurf}
}
\]

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
- eine bewusst geparkte Front wird wieder aktiv.

Sie soll **nicht** historische Forschungsprovenienz duplizieren. Dafür bleiben Journal, Papers, Audits und Promotionsrecords erhalten.

---

## 11. Aktueller Kurzstatus

\[
\boxed{
\begin{array}{ll}
\text{P12 restricted-tail outer Hub} & \checkmark[M] \\
\text{HT-A4b-SW1-M} & \checkmark[M] \\
\text{SW1-KNF} & \text{OVERALL GREEN candidate, keine Promotion} \\
\text{HT-RED} & ?[O] \\
\text{A0} & ?[O] \\
\text{Schur Cross-Gram} & ?[O]
\end{array}
}
\]

**Nächster Default:** SW1-BL7 (siebter Blindwert \(2d+s\)) als eigenes Teilaudit, dann SW1-2TP, SW1-AWI, \(\Delta\)-Descent.
