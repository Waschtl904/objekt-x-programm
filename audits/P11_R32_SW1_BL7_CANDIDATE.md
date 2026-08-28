# Audit-Kandidat: SW1-BL7 — Siebter direkter Blindwert \(2d+s\)

> **Stand:** 28. August 2026  
> **Repo-Basis dieses Audits:** `main@242f1c2684a982067d45633c2b559cd149557396`  
> **Status:** `?[O]` — neuer Kandidat, noch kein adversariales GREEN, keine Promotion.  
> **Scope:** ausschließlich SW1, \(0<\sigma\le R<\varepsilon,\ R+\varepsilon<\Delta\); ausschließlich der siebte Blindwert \(2d+s\).

---

## 0. Firewall (zuerst lesen)

Dieses Audit beweist — wenn es GREEN wird — **ausschließlich**, dass \(2d+s\) für \(s\in(R,\varepsilon)\) auf SW1 ein direkter Blindwert ist (a.e.). Es beweist **nicht**:

- kein SW1-2TP (simultaner \(T\pm s\)-2×2-Pivot);
- keine SW1-AWI (A-Wall-Involution \(s\leftrightarrow\Delta-s\));
- keinen \(\Delta\)-Descent;
- kein HT-RED (Full-Rest-/Schur-Elimination);
- kein A0;
- keine Aussage über \(\ker\Gamma_I\);
- keine Erweiterung oder Modifikation von SW1-KNF (`audits/P11_R32_SW1_KNF_CANDIDATE.md`, bereits GREEN, PR #15) — dieses Audit **verwendet** SW1-KNF nur als Referenzrahmen für den Blindbereich, ändert es aber nicht.

\[
\boxed{\text{SW1-BL7 ist ausschließlich ein zusätzlicher Blindwert-Nachweis, kein Pivot- oder Injektivitätssatz.}}
\]

---

## 1. Kandidatenbehauptung

\[
\boxed{
s\in(R,\varepsilon)\quad\Longrightarrow\quad 2d+s\in\mathcal Z_{R,\mathrm{SW1}}^{\rm phys}\quad\text{a.e.}
}
\]

wobei \(\mathcal Z_{R,\mathrm{SW1}}^{\rm phys}\) der in SW1-KNF exakt bestimmte Blindbereich ist:
\[
\mathcal Z_{R,\mathrm{SW1}}^{\rm phys} = (0,a-R)\cup(a+R,b-R)\cup(b+R,T-R)\cup(T+R,T+\varepsilon).
\]

---

## 2. Beweisskizze (zu verifizieren)

Ziel: \(2d+s\) liegt außerhalb aller drei Samplingfenster \(I_a,I_b,I_T\) und innerhalb \((0,T_0)\).

**Schritt 1 — Abstand zu \(a\).**
\[
(2d+s)-a = \Delta+s > R.
\]
*Zu prüfen:* exakte Identität \(2d-a=\Delta\) bzw. \(2d+s-a=\Delta+s\) gegen die kanonischen Definitionen von \(a,b,d,\Delta\) im Rahmen; Vorzeichen und Größenordnung von \(\Delta+s\) versus \(R\).

**Schritt 2 — Abstand zu \(b\).**
\[
b-(2d+s) = e-s > e-\varepsilon > R.
\]
*Zu prüfen:* exakte Identität \(b-2d=e\); dass \(e-\varepsilon>R\) tatsächlich aus den globalen Parameterordnungsannahmen folgt (nicht nur aus SW1 selbst) — ggf. Referenz auf zusätzliche Rahmenbedingung nachtragen.

**Schritt 3 — Abstand zu \(T\).**
\[
T-(2d+s) = 2e-s > R.
\]
*Zu prüfen:* exakte Identität \(T-2d=2e\); Konsistenz mit Schritt 2 (beide verwenden \(e\)); dass \(2e-s>R\) für alle \(s\in(R,\varepsilon)\) gilt, insbesondere am oberen Rand \(s\to\varepsilon\).

**Schritt 4 — Enthaltenheit in \((0,T_0)\).**
\[
2d+s < T_0 = T+\varepsilon.
\]
*Zu prüfen:* explizit, ob dies aus Schritt 3 (\(T-(2d+s)>R>0\)) bereits folgt oder eine separate Abschätzung braucht.

**Schritt 5 — a.e.-Präzisierung.**
*Zu prüfen:* ob "a.e." hier nur die übliche Nullmenge der Randfälle (\(s=R\) oder \(s=\varepsilon\)) betrifft oder ob zusätzliche degenerierte Parameterkonstellationen (z. B. \(\Delta+s=R\) exakt) ausgeschlossen werden müssen.

---

## 3. Konsistenzprüfung gegen bereits promotete Blindwerte

Der promotete Satz (`audits/P11_R32_HT_A4B_SW1_M_PROMOTION.md`, \(\checkmark[M]\)) listet die sechs Blindwerte
\[
s,\ a-s,\ a+s,\ T-s,\ 2d-s,\ T+s.
\]

**Zu prüfen:** dass \(2d+s\) tatsächlich ein *siebter*, bisher nicht erfasster Wert ist — keine versteckte Identität mit einem der sechs bereits promoteten Werte modulo der SW1-Parameterrelationen (insbesondere gegen \(2d-s\) und \(T+s\) abzugleichen, da beide strukturell ähnlich sind).

---

## 4. Adversarialer Review-Auftrag (vor GREEN einzeln zu prüfen)

1. Identität \(2d-a=\Delta\) exakt gegen kanonische Quelle.
2. Identität \(b-2d=e\) exakt gegen kanonische Quelle.
3. Identität \(T-2d=2e\) exakt gegen kanonische Quelle (und Konsistenz mit Punkt 2).
4. \((2d+s)-a=\Delta+s>R\) für alle \(s\in(R,\varepsilon)\).
5. \(b-(2d+s)=e-s>R\) für alle \(s\in(R,\varepsilon)\), insbesondere Herkunft der Zusatzbedingung \(e-\varepsilon>R\).
6. \(T-(2d+s)=2e-s>R\) für alle \(s\in(R,\varepsilon)\).
7. \(2d+s<T_0\) für alle \(s\in(R,\varepsilon)\).
8. Keine versteckte Identität mit einem der sechs bereits promoteten Blindwerte.
9. Präzise a.e.-Formulierung (Randfälle explizit benannt).
10. Scope-Firewall vollständig eingehalten (Abschnitt 0).

Kein GREEN ohne alle zehn Punkte einzeln bestanden. Keine Promotion, keine Registry-/Front-Änderung, solange dieser Status `?[O]` ist.

---

## 5. Erwarteter Nutzen bei GREEN

Mit SW1-BL7 stünde ein siebter direkter Blindwert zur Verfügung, der für die Auswertung der Row bei \(2d\pm s\) im Rahmen des \(\Delta\)-Descent-Ansatzes relevant wird (ähnliche Struktur wie die bekannte \(\Delta\)-Ketten-Argumentation). Dies allein ändert nichts an HT-RED, A0 oder \(\ker\Gamma_I\) und ist kein Ersatz für SW1-2TP oder SW1-AWI.
