# Audit-Kandidat: SW1-2TP — Simultaner \(T\pm s\)-2×2-Pivot

> **Stand:** 28. August 2026  
> **Repo-Basis dieses Audits:** `main@152150284c31af50dedb9e2ee4ac820d4692776c`  
> **Status:** `?[O]` — nur Zielformulierung und zu reproduzierende Hypothese, **kein Beweis enthalten**.  
> **Scope:** ausschließlich SW1, \(0<\sigma\le R<\varepsilon,\ R+\varepsilon<\Delta\); ausschließlich die simultane Elimination von \(y(T+s)\) und \(y(T-s)\).

---

## 0. Firewall (zuerst lesen)

Dieses Audit soll — wenn es AI-GREEN wird — **ausschließlich** zeigen, dass die \(T\pm s\)-Zeilen aus dem tatsächlichen elf-Wörter-Operator \(A\) die Form \(M_T\) besitzen und \(M_T\) invertierbar ist. Es beweist **nicht**:

- keine SW1-AWI (A-Wall-Involution \(s\leftrightarrow\Delta-s\));
- keinen \(\Delta\)-Descent;
- kein HT-RED (vollständige Full-Rest-/Schur-Elimination);
- kein A0;
- keine Aussage über \(\ker\Gamma_I\);
- keine Erweiterung von SW1-KNF oder SW1-BL7 — diese werden nur referenziert.

**Zusätzliche Promotionsschwelle (verbindlich, siehe Registry §4):** Selbst wenn dieses Audit AI-GREEN wird, erfolgt **keine formale Promotion** des 2TP-Satzes, bevor mindestens ein \`independent GREEN\` (externer Mensch, unabhängiger Modelllauf, oder maschinenprüfbares algebraisches Zertifikat, mit dokumentierter Methode/Reviewer/Head) für das 11-Wort-Ledger vorliegt. Grund: Ein einzelner Vorzeichen- oder Shiftfehler in den elf Wörtern könnte die gesamte spätere \(\Delta\)-Elimination verfälschen.

\[
\boxed{\text{SW1-2TP ist ein Pivot-Invertierbarkeitssatz, kein Injektivitätssatz und keine vollständige Row-Ableitung außerhalb des }T\pm s\text{-Blocks.}}
\]

---

## 1. Ziel

\[
\boxed{
M_T(s)
\begin{pmatrix}y(T+s)\\y(T-s)\end{pmatrix}
+\mathrm{Rest}(s)=0
}
\]

mit der zu beweisenden Kandidatenform
\[
M_T=\begin{pmatrix}1+\kappa&\beta_T\\\beta_T&1+\kappa\end{pmatrix}.
\]

Wenn \(M_T\) diese symmetrische Form besitzt, sind die Eigenwerte \(\lambda_\pm=1+\kappa\pm\beta_T\), und \(M_T\) ist genau dann invertierbar, wenn
\[
\det M_T=(1+\kappa)^2-\beta_T^2>0.
\]

---

## 2. Zu reproduzierende Hypothese — NICHT als Input verwenden

> **Warnung:** Der folgende Abschnitt ist eine aus früheren informellen Notizen übernommene Scratch-Formel. Er dient ausschließlich als Zielvorgabe ("was am Ende herauskommen sollte"), **nicht** als Beweisschritt oder Voraussetzung. Der eigentliche Beweis in Abschnitt 4 darf diesen Abschnitt an keiner Stelle zitieren oder verwenden.

Vermuteter allgemeiner Pivot (aus \`CURRENT-FRONT.md\` §4, Altfassung):
\[
(1+\kappa)z(T+s)
+\beta_0z(s)
+\beta_-z(a-s)
+\beta_+z(a+s)
+\beta_Tz(T-s)
+\beta_bz(2d-s)
+\text{Annulus-/}w\text{-Terme}
=0.
\]

Vermutete Konsequenz für die Summen-/Differenzkanäle: \(q\,w(s)\) verschwindet im Summenkanal \(y(T+s)+y(T-s)\) und erscheint im Differenzkanal \(y(T+s)-y(T-s)\) mit Faktor \(2q\). **Dies ist eine zu prüfende Vermutung, kein gesichertes Ergebnis.**

---

## 3. Vierstufiger Prüfauftrag (verbindliche Reihenfolge)

\[
\boxed{
11\text{-Wort-Ledger} \to T+s/T-s\text{-Rows} \to \det M_T>0 \to \text{Summe/Differenz-Kanäle}
}
\]

### Stufe 1 — 11-Wort-Ledger

Jedes der elf Wörter des Operators \(A\) ist einzeln durch den Support-/Shift-Filter zu schicken und sein Beitrag zur Zeile bei Argument \(T+s\) bzw. \(T-s\) explizit zu notieren. **Zu tun:**

- Vollständige Liste der elf Wörter aus der kanonischen \(A\)-Definition beschaffen (Quelle: zu benennen, vermutlich \`audits/P11_R32_TAIL_FG_PIVOT_CANDIDATE.md\` oder das zugrundeliegende Paper).
- Für jedes Wort: Trägt es zu Argument \(T+s\) bei? Zu \(T-s\)? Mit welchem Koeffizienten und welcher Verschiebung?
- Tabellarische Ledger-Form: Wort-ID, Beitrag bei \(T+s\), Beitrag bei \(T-s\), Beitrag bei anderen Argumenten (für den Rest-Term).

**Noch nicht ausgeführt in diesem Audit-Stand.**

### Stufe 2 — \(T+s\)/\(T-s\)-Rows

Aus dem Ledger die beiden vollständigen Zeilen zusammensetzen:
\[
0=c_{++}\,y(T+s)+c_{+-}\,y(T-s)+\mathrm{Rest}_+(s),\qquad
0=c_{-+}\,y(T+s)+c_{--}\,y(T-s)+\mathrm{Rest}_-(s).
\]
**Zu prüfen:** Gilt tatsächlich \(c_{++}=c_{--}=1+\kappa\) und \(c_{+-}=c_{-+}=\beta_T\) (d.h. ist \(M_T\) wirklich symmetrisch mit gleichen Diagonaleinträgen)? Das ist selbst Teil des zu beweisenden Satzes, nicht vorauszusetzen.

**Noch nicht ausgeführt in diesem Audit-Stand.**

### Stufe 3 — \(\det M_T>0\)

Sobald \(M_T\) exakt (nicht numerisch) bestimmt ist:
\[
\det M_T=(1+\kappa)^2-\beta_T^2>0 \iff |\beta_T|<1+\kappa.
\]
**Zu prüfen:** exakte Werte/Schranken für \(\kappa\) und \(\beta_T\) aus der kanonischen Quelle (z. B. HT-A2 für \(\kappa\)); ob \(|\beta_T|<1+\kappa\) auf ganz SW1 gilt oder zusätzliche Bedingungen braucht.

**Noch nicht ausgeführt in diesem Audit-Stand.**

### Stufe 4 — Summe/Differenz-Kanäle

Erst nachdem Stufen 1–3 unabhängig stehen, Summe und Differenz der beiden Rows bilden und prüfen, ob und wie \(q\,w(s)\) sich auf die beiden Kanäle verteilt. **Diese Stufe darf nicht vorab als Ergebnis angenommen werden** (siehe Abschnitt 2).

**Noch nicht ausgeführt in diesem Audit-Stand.**

---

## 4. Beweis

*(Bewusst leer. Der Beweis entsteht in einem späteren Commit auf diesem Branch, ausgehend von Stufe 1. Diese Datei wird dann in-place erweitert oder durch eine überarbeitete Fassung ersetzt.)*

---

## 5. Adversarialer Review-Auftrag (später, nach vollständigem Beweis)

1. Ledger vollständig (alle elf Wörter erfasst, keines übersehen).
2. Jeder Ledger-Eintrag korrekt gegen die kanonische \(A\)-Definition.
3. \(T+s\)/\(T-s\)-Rows korrekt aus dem Ledger zusammengesetzt.
4. Symmetrie \(c_{++}=c_{--}\), \(c_{+-}=c_{-+}\) tatsächlich bewiesen, nicht angenommen.
5. \(\det M_T>0\) exakt (nicht numerisch) gezeigt.
6. Summen-/Differenzkanalzerlegung korrekt durchgeführt.
7. \(q\,w(s)\)-Verteilung auf die Kanäle tatsächlich abgeleitet, nicht aus Abschnitt 2 übernommen.
8. Scope-Firewall vollständig eingehalten (Abschnitt 0).
9. Promotionsschwelle (independent GREEN / algebraisches Zertifikat) beachtet — keine Promotion allein auf AI-GREEN-Basis.

---

## 6. Erwarteter Nutzen bei Erfolg

Mit invertierbarem \(M_T\) ließen sich \(y(T+s)\) und \(y(T-s)\) simultan und eindeutig eliminieren — der eigentliche Full-Rest-Knoten der Kette. Dies allein ändert nichts an HT-RED, A0 oder \(\ker\Gamma_I\) und ist kein Ersatz für SW1-AWI oder \(\Delta\)-Descent.
