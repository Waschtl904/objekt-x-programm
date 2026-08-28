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

**Status dieses Branch-Heads:** ausgeführt; noch kein AI-GREEN, solange der neue Head nicht separat adversarial gegengeprüft ist.

Kanonische Inputquelle für Stufe 1 ist ausschließlich die Vier-Echo-Formel (HT.3) und die Elf-Wort-Liste (HT.4) aus audits/P11_R32_TAIL_FG_PIVOT_CANDIDATE.md:
\[
\begin{aligned}
(W_{\delta,\eta}^{(\lambda)}y)(x)
={}&-\chi_\lambda(x-\delta)\widetilde y(x-\delta-\eta)
+\chi_\lambda(x-\delta)\widetilde y(x-\delta+\eta)\\
&+\chi_\lambda(x+\delta)\widetilde y(x+\delta-\eta)
-\chi_\lambda(x+\delta)\widetilde y(x+\delta+\eta).
\end{aligned}
\tag{2TP.1}
\]
Die späteren fertigen Tail-Rows (HT.19)–(HT.21) werden nicht als Input verwendet.

Für
\[
x_\pm:=T\pm s,\qquad R<s<\varepsilon,
\tag{2TP.2}
\]
gilt auf SW1 uniform:

1. Für jedes der elf Wörter ist das \(x+\delta\)-Gate geschlossen; sämtliche \(E_3,E_4\)-Terme verschwinden.
2. Für jedes Wort ist das \(x-\delta\)-Gate offen. Bei \(E_1,E_2\) entscheidet nur noch der Source-Horizon.
3. Bei Wort 6, \(W_{T,3a}^{(a)}\), liegen beide Source-Argumente außerhalb \((-T_0,T_0)\); Wort 6 trägt zu beiden Rows Null bei.
4. Alle unten aufgeführten übrigen Quellen liegen strikt innerhalb des Horizons. Geradheit wird nur benutzt, um negative Source-Argumente als positive \(y(|\cdot|)\)-Profile zu schreiben.

Die Gate-Aussagen folgen aus \(T=2a\), \(T_0=T+\varepsilon\) und
\[
0<R<s<\varepsilon<\Delta<e<d<a.
\tag{2TP.3}
\]
Insbesondere gilt \(s+\varepsilon<2\varepsilon<2\Delta<a\), weil \(2\Delta<a\).

#### Vollständiges Ledger

| Nr. | Wort | Beitrag bei \(x=T+s\) | Beitrag bei \(x=T-s\) |
|---:|---|---|---|
| 1 | \(W_{a,a}^{(a)}\) | \(-c_1y(s)+c_1y(T+s)\) | \(-c_1y(s)+c_1y(T-s)\) |
| 2 | \(W_{a,T}^{(a)}\) | \(-c_2y(a-s)\) | \(-c_2y(a+s)\) |
| 3 | \(W_{a,3a}^{(a)}\) | \(-c_3y(T-s)\) | \(-c_3y(T+s)\) |
| 4 | \(W_{T,a}^{(a)}\) | \(-c_4y(a-s)+c_4y(a+s)\) | \(-c_4y(a+s)+c_4y(a-s)\) |
| 5 | \(W_{T,T}^{(a)}\) | \(-c_5y(T-s)+c_5y(T+s)\) | \(-c_5y(T+s)+c_5y(T-s)\) |
| 6 | \(W_{T,3a}^{(a)}\) | \(0\) | \(0\) |
| 7 | \(W_{3a,a}^{(a)}\) | \(-c_7y(T-s)+c_7y(s)\) | \(-c_7y(T+s)+c_7y(s)\) |
| 8 | \(W_{3a,T}^{(a)}\) | \(+c_8y(a+s)\) | \(+c_8y(a-s)\) |
| 9 | \(W_{3a,3a}^{(a)}\) | \(+c_9y(T+s)\) | \(+c_9y(T-s)\) |
| 10 | \(W_{T,T}^{(T)}\) | \(-c_{10}y(T-s)+c_{10}y(T+s)\) | \(-c_{10}y(T+s)+c_{10}y(T-s)\) |
| 11 | \(W_{b,b}^{(b)}\) | \(-c_{11}y(2d-s)+c_{11}y(T+s)\) | \(-c_{11}y(2d+s)+c_{11}y(T-s)\) |

Damit sind alle \(11\times4\) Echo-Möglichkeiten berücksichtigt: pro Wort sind \(E_3,E_4\) gate-tot; unter \(E_1,E_2\) überleben insgesamt exakt 16 Beiträge je Row.

**Wichtiger neuer Punkt:** Der Wert \(2d+s\) erscheint in der \(T-s\)-Row exakt im 3-adischen Wort 11. Seine direkte Blindheit ist durch SW1-BL7 separat AI-GREEN geprüft; diese Blindheit wird für das Ledger selbst nicht benötigt, wohl aber später für die freie-Koordinateninterpretation.

Stufe 1 ist damit algebraisch hergeleitet, aber noch nicht unabhängig zertifiziert.

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

## 4. Beweisstand

### 4.1 Stufe 1: Wort-für-Wort-Ableitung

Zur Nachprüfbarkeit werden die Source-Argumente vor Geradheitsreduktion explizit festgehalten.

Für \(x=T+s\) lauten die überlebenden \(E_1/E_2\)-Quellen:
\[
\begin{array}{c|c}
j & \text{überlebende Quellen}\\ \hline
1 & s,\ T+s\\
2 & s-a\\
3 & s-T\\
4 & s-a,\ a+s\\
5 & s-T,\ T+s\\
6 & \varnothing\\
7 & s-T,\ s\\
8 & a+s\\
9 & T+s\\
10 & s-T,\ T+s\\
11 & s-2d,\ T+s.
\end{array}
\tag{2TP.4}
\]

Für \(x=T-s\):
\[
\begin{array}{c|c}
j & \text{überlebende Quellen}\\ \hline
1 & -s,\ T-s\\
2 & -a-s\\
3 & -T-s\\
4 & -a-s,\ a-s\\
5 & -T-s,\ T-s\\
6 & \varnothing\\
7 & -T-s,\ -s\\
8 & a-s\\
9 & T-s\\
10 & -T-s,\ T-s\\
11 & -2d-s,\ T-s.
\end{array}
\tag{2TP.5}
\]

Da \(s<\varepsilon<\Delta<d<a<T\), sind \(s-T,s-a,s-2d<0\), und Geradheit ergibt genau die Profile der Ledger-Tabelle.

Für Wort 6 liegen die Beträge \(3a\pm s\) außerhalb des Source-Horizons:
\[
3a-s-(2a+\varepsilon)=a-(s+\varepsilon)>a-2\varepsilon>a-2\Delta>0,
\]
während \(3a+s>T_0\) unmittelbar ist. Die weiteren nicht aufgeführten \(E_1/E_2\)-Quellen der Wörter 2, 3, 8 und 9 liegen noch weiter außerhalb des Source-Horizons.

Damit ist Stufe 1 vollständig auf die elf kanonischen Wörter zurückgeführt.

### 4.2 Noch offen

Stufe 2 (Zusammensetzen der beiden Rows), Stufe 3 (exakte Pivot-Invertierbarkeit) und Stufe 4 (Hub-Summe/Differenz) bleiben absichtlich offen, bis dieser Ledger-Commit separat adversarial geprüft wurde.

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
