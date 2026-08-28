# CURRENT FRONT — Objekt X / P11-R32

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 28. August 2026  
> **Verifizierte Main-Basis:** `83e03c6d69ce6dfae2b433977548dd1cd308ebc7`  
> **Aktiver mathematischer Stand:** `HT-A4b-SW1-M` ist promotet — Promotionsrecord `audits/P11_R32_HT_A4B_SW1_M_PROMOTION.md`, Kandidat gemergt in `b06f50f12973e781b87db8b06e54fd590a053b10` (PR #10)  
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
`papers/P12_Adelic_Hub_Injectivity_Program.tex`, Corollary `cor:p12-consolidated`.

SW1 liegt vollständig in diesem Bereich. Daher muss die äußere Hub-Injektivität für den SW1-Angriff **nicht neu bewiesen** werden.

### 2.2 SW1-Membership — jetzt promotet

\[
\boxed{
\mathrm{HT\!-\!A4b\!-\!SW1\!-\!M}:\checkmark[M]
}
\]

Die uniforme Membership \((Z,Z,Z,Z,Z,Z)\) für \(s,a-s,a+s,T-s,2d-s,T+s\) sowie \(I_b\cap I_-=\emptyset\) und \(I_b\cap I_+\neq\emptyset\iff\varepsilon>\Delta/2\) sind promotet. Kanonischer Promotionsrecord: `audits/P11_R32_HT_A4B_SW1_M_PROMOTION.md`. Kandidatenaudit: `audits/P11_R32_HT_A4B_SW1_SELF_CONTAINED_THEOREM_CANDIDATE.md`, gemergt in `main@b06f50f12973e781b87db8b06e54fd590a053b10` (PR #10). Keine Mitpromotion von HT-A4b global, HT-RED, A0 oder Schur-Cross-Gram.

### 2.3 Weitere Tail-/FG-Kandidaten

HT-A1, HT-A2, HT-A3 und HT-A4a sind unabhängig GREEN geprüfte Kandidaten, aber nicht formal promotet.

FG-1, FG-TR1, die \(\widehat\Phi_R\)-Normalform und CG-FG1 sind ebenfalls Kandidaten-/Kompositionsresultate ohne formale Promotion.

Exakte Status- und Quellenliste:
[ACTIVE_THEOREM_REGISTRY](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

---

## 3. Nächster mathematischer Schritt

**Keine weitere Chamber-Katalogisierung als Default.**

Auf SW1 wird jetzt das vollständige augmentierte Rohsystem aufgestellt:

\[
(I+A)y+HE_{\mathcal A}w=0,
\qquad
E_I^*Hy=0.
\]

Mit der jetzt promoteten SW1-Membership wird die Tail-Zeile in direkten Blindkoordinaten geschrieben. Der bekannte Pivot besitzt die Form

\[
(1+\kappa)z(T+s)
+\beta_0z(s)
+\beta_-z(a-s)
+\beta_+z(a+s)
+\beta_Tz(T-s)
+\beta_bz(2d-s)
+\text{Annulus-/}w\text{-Terme}
=0,
\]

wobei
\[
1+\kappa>0.
\]

Erster Eliminationsschritt:
\[
z(T+s)
\]
eindeutig eliminieren.

Danach ist zu prüfen, ob zusätzliche Beobachtungszeilen die verbleibenden fünf \(z\)-Kanäle und die Annulusvariablen sukzessive töten.

### Erfolgsausgang

Falls die innere Rechnung
\[
y=0
\]
erzwingt, kann anschließend P12-RT \(\checkmark[M]\) für den äußeren Hub verwendet werden, um \(w=0\) zu folgern.

### Negativausgang

Falls ein nichttrivialer Restfreiheitsgrad oder Gegenvektor überlebt, ist dieser explizit zu isolieren. Dann ist SW1 allein für den vollständigen Schur-Abschluss nicht ausreichend.

Beide Ausgänge sind verwertbare Forschungsergebnisse.

---

## 4. Was derzeit ausdrücklich **nicht** bearbeitet wird

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

## 5. Warum Round 29 / \(M_{68}\) aktuell nicht gebraucht wird

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

## 6. Lesereihenfolge für jede neue Arbeitssitzung

Vor einer neuen Rechnung ist in dieser Reihenfolge zu lesen:

1. **`CURRENT-FRONT.md`** — Was ist heute die aktive Frage?
2. **`00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`** — Welche Resultate dürfen mit welchem Status benutzt werden?
3. **Kanonische Quelle des benötigten Inputs** — Paper oder Promotionsrecord.
4. **Aktueller Kandidatenaudit / aktiver PR** — nur die konkrete Front.
5. **Historische Audits / Journal** — nur bei einer klar benannten Provenienz-, Fehler- oder Gegenbeispielfrage.

Nicht mit einer Volltextsuche durch das ganze Repo beginnen, solange Stufen 1–4 die Frage beantworten.

---

## 7. Epistemische Autorität

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

`CURRENT-FRONT.md` und die Registry sind **Navigationsdateien**. Bei einem Konflikt entscheiden die kanonischen mathematischen Quellen.

---

## 8. Fünf-Punkte-Regel für mathematisch relevante Merges

Ein mathematisch relevanter Merge gilt operativ erst dann als vollständig abgeschlossen, wenn alle fünf Punkte erfüllt sind:

1. **PR gemergt** — exakter Merge-Commit bekannt.
2. **Main mechanisch verifiziert** — tatsächlicher Main-SHA und Diff geprüft.
3. **Registry geprüft** — falls Status, Scope, Quelle oder aktive Abhängigkeit betroffen sind, `ACTIVE_THEOREM_REGISTRY.md` aktualisieren.
4. **Front aktualisiert** — `CURRENT-FRONT.md` auf neuen Main-SHA, aktuellen offenen Knoten und nächsten Schritt bringen.
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

## 9. Änderungen an dieser Datei

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

## 10. Aktueller Kurzstatus

\[
\boxed{
\begin{array}{ll}
\text{P12 restricted-tail outer Hub} & \checkmark[M] \\
\text{HT-A4b-SW1-M} & \checkmark[M] \\
\text{HT-RED} & ?[O] \\
\text{A0} & ?[O] \\
\text{Schur Cross-Gram} & ?[O]
\end{array}
}
\]

**Nächster Default:** vollständiges augmentiertes SW1-System aufstellen und Tail-Pivot \(z(T+s)\) eliminieren (Full-Rest-/Schur-Elimination), statt weiterer globaler Chamber-Ausweitung.
