# Audit-Kandidat: SW1-2TP — Simultaner \(T\pm s\)-2×2-Pivot

> **Stand:** 28. August 2026  
> **Repo-Basis dieses Audits:** `main@152150284c31af50dedb9e2ee4ac820d4692776c`  
> **Status:** `AI-GREEN candidate + independent GREEN (certificate)` — vollständiger 2TP-Beweis intern kritisch geprüft und algebraisch zertifiziert; **keine Promotion**.  
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

**Status:** AI-GREEN am Head `b71ca37ebfede86a36a28e1e3260c0cc26fedcde`; zusätzlich `independent GREEN (certificate)` am Head `0ff3bfa532c34a0ee07e227358e0cfd2262ffde2` durch scripts/certify_sw1_2tp_ledger.py (SymPy 1.14.0, 88 Echo-Fälle, PASS). Der separate Perplexity-Blindcheck ist dokumentiert FAIL und zählt nicht als independent GREEN.

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

**Status:** AI-GREEN; Row-Zusammensetzung und Annulus-Hub-Zeichen separat am exakten Zwischenhead `be6096f2625125bb7399d2e45fb4bd2fec918d1e` gegengeprüft.

Aus dem Ledger werden die Wortgewichte gruppiert. Mit
\[
\kappa:=c_1+c_5+c_9+c_{10}+c_{11},
\tag{2TP.6}
\]
\[
\beta_0:=-c_1+c_7=-c_1+c_3,
\tag{2TP.7}
\]
\[
\beta_-:=-c_2-c_4,
\qquad
\beta_+:=c_4+c_8=c_2+c_6,
\tag{2TP.8}
\]
\[
\beta_T:=-c_3-c_5-c_7-c_{10},
\qquad
\beta_b:=-c_{11},
\tag{2TP.9}
\]
wobei \(c_7=c_3,\ c_4=c_2,\ c_8=c_6\) direkt aus der Elf-Wort-Liste folgen, ergibt sich für jedes \(s\in(R,\varepsilon)\):

\[
\boxed{
\begin{aligned}
(Ay)(T+s)
={}&
\kappa y(T+s)
+\beta_0y(s)
+\beta_-y(a-s)
+\beta_+y(a+s)\\
&+\beta_Ty(T-s)
+\beta_by(2d-s).
\end{aligned}}
\tag{2TP.10}
\]

Die gespiegelte Row ist
\[
\boxed{
\begin{aligned}
(Ay)(T-s)
={}&
\kappa y(T-s)
+\beta_0y(s)
+\beta_-y(a+s)
+\beta_+y(a-s)\\
&+\beta_Ty(T+s)
+\beta_by(2d+s).
\end{aligned}}
\tag{2TP.11}
\]

Damit wird die Symmetrie des \(T\pm s\)-Blocks aus dem Ledger abgeleitet, nicht vorausgesetzt.

#### Annulus-Hub direkt aus der kanonischen Hubdefinition

Aus RB.3–RB.7 in audits/P11_P12_R32_RUECKBINDUNG_AUDIT.md gilt für den ungeraden Annulussektor
\[
(HE_{\mathcal A}w)(u)
=
p[w(u-a)-w(u+a)]
+r[w(u-b)-w(u+b)]
+q[w(u-T)-w(u+T)]
\tag{2TP.12}
\]
mit
\[
p=\sqrt{\log2}\,2^{-3/4},
\qquad
r=\sqrt{\log3}\,3^{-3/4},
\qquad
q=\sqrt{\log2}\,2^{-3/2}.
\tag{2TP.13}
\]

Für \(u=T+s\) sind die drei rechten Äste \(u+a,u+b,u+T\) außerhalb des Annulus; die linken Äste sind \(a+s,e+s,s\). Daher
\[
\boxed{
(HE_{\mathcal A}w)(T+s)
=
p\,w(a+s)+r\,w(e+s)+q\,w(s).
}
\tag{2TP.14}
\]

Für \(u=T-s\) sind wiederum die drei rechten Äste außerhalb des Annulus. Die linken Äste sind
\[
a-s,\qquad e-s,\qquad -s.
\]
Auf SW1 gilt \(a-s>R,\ e-s>R,\ s>R\); alle drei Beträge liegen unter \(S=T+\sigma\). Wegen der Oddheit von \(w\),
\[
w(-s)=-w(s),
\]
folgt
\[
\boxed{
(HE_{\mathcal A}w)(T-s)
=
p\,w(a-s)+r\,w(e-s)-q\,w(s).
}
\tag{2TP.15}
\]

Die rechten Äste sind uniform annulus-tot. Für den kleinsten Fall bei \(u=T-s\),
\[
(T-s)+a-S
=
a-s-\sigma
>
a-2\varepsilon
>
a-2\Delta
>
0,
\]
weil \(\sigma\le R<\varepsilon\), \(s<\varepsilon\) und \(2\Delta<a\). Die \(b\)- und \(T\)-Äste liegen noch weiter rechts.

#### Beide augmentierten Rows

Aus
\[
(I+A)y+HE_{\mathcal A}w=0
\]
folgen somit
\[
\boxed{
\begin{aligned}
0={}&
(1+\kappa)y(T+s)
+\beta_Ty(T-s)
+\beta_0y(s)
+\beta_-y(a-s)
+\beta_+y(a+s)\\
&+\beta_by(2d-s)
+p\,w(a+s)+r\,w(e+s)+q\,w(s),
\end{aligned}}
\tag{2TP.16}
\]
und
\[
\boxed{
\begin{aligned}
0={}&
\beta_Ty(T+s)
+(1+\kappa)y(T-s)
+\beta_0y(s)
+\beta_-y(a+s)
+\beta_+y(a-s)\\
&+\beta_by(2d+s)
+p\,w(a-s)+r\,w(e-s)-q\,w(s).
\end{aligned}}
\tag{2TP.17}
\]

Folglich ist der interne Tailblock exakt
\[
\boxed{
M_T=
\begin{pmatrix}
1+\kappa & \beta_T\\
\beta_T & 1+\kappa
\end{pmatrix}.
}
\tag{2TP.18}
\]

Damit ist Stufe 2 hergeleitet. Die Invertierbarkeit von \(M_T\) wird erst in Stufe 3 bewertet.

### Stufe 3 — \(\det M_T>0\)

Aus der Elf-Wort-Liste gilt exakt
\[
c_3=c_5=c_7=\frac{\log2}{8},
\qquad
c_{10}=\frac{\log2}{4}.
\]
Daher
\[
\boxed{
\beta_T
=
-c_3-c_5-c_7-c_{10}
=
-\frac58\log2.
}
\tag{2TP.19}
\]

Ferner
\[
\kappa=c_1+c_5+c_9+c_{10}+c_{11}>0
\tag{2TP.20}
\]
als Summe strikt positiver Gewichte.

Die Eigenwerte des symmetrischen Blocks (2TP.18) sind
\[
\lambda_\Sigma:=1+\kappa+\beta_T,
\qquad
\lambda_\Delta:=1+\kappa-\beta_T.
\tag{2TP.21}
\]

Da \(0<\log2<1\),
\[
\lambda_\Sigma
=
1+\kappa-\frac58\log2
>
1-\frac58
=
\frac38>0,
\tag{2TP.22}
\]
und
\[
\lambda_\Delta
=
1+\kappa+\frac58\log2
>
1>0.
\tag{2TP.23}
\]

Somit
\[
\boxed{
\det M_T
=
\lambda_\Sigma\lambda_\Delta
=
(1+\kappa)^2-\beta_T^2
>0.
}
\tag{2TP.24}
\]

Die Positivität ist uniform; sie benötigt außer der festen Elf-Wort-Struktur keine zusätzliche SW1-Unterkammer.

Insbesondere
\[
\boxed{
M_T^{-1}
=
\frac1{(1+\kappa)^2-\beta_T^2}
\begin{pmatrix}
1+\kappa&-\beta_T\\
-\beta_T&1+\kappa
\end{pmatrix}.
}
\tag{2TP.25}
\]

Damit können \(y(T+s)\) und \(y(T-s)\) für fast jedes \(s\in(R,\varepsilon)\) gleichzeitig und eindeutig aus den übrigen Row-Kanälen rekonstruiert/elimininiert werden.

### Stufe 4 — Summe/Differenz-Kanäle

Definiere
\[
Y_\Sigma(s):=y(T+s)+y(T-s),
\qquad
Y_\Delta(s):=y(T+s)-y(T-s).
\tag{2TP.26}
\]

Addition von (2TP.16) und (2TP.17) ergibt
\[
\boxed{
\begin{aligned}
0={}&
\lambda_\Sigma Y_\Sigma(s)
+2\beta_0y(s)\\
&+(\beta_-+\beta_+)\,[y(a-s)+y(a+s)]\\
&+\beta_b\,[y(2d-s)+y(2d+s)]\\
&+p\,[w(a+s)+w(a-s)]\\
&+r\,[w(e+s)+w(e-s)].
\end{aligned}}
\tag{2TP.27}
\]
Der \(q\,w(s)\)-Kanal hebt sich **exakt** weg.

Subtraktion der \(T-s\)-Row von der \(T+s\)-Row liefert
\[
\boxed{
\begin{aligned}
0={}&
\lambda_\Delta Y_\Delta(s)\\
&+(\beta_+-\beta_-)\,[y(a+s)-y(a-s)]\\
&+\beta_b\,[y(2d-s)-y(2d+s)]\\
&+p\,[w(a+s)-w(a-s)]\\
&+r\,[w(e+s)-w(e-s)]\\
&+2q\,w(s).
\end{aligned}}
\tag{2TP.28}
\]

Damit ist die frühere Scratch-Vermutung nun abgeleitet:
\[
\boxed{
q\,w(s)\text{ verschwindet im symmetrischen Kanal und erscheint als }2q\,w(s)
\text{ im antisymmetrischen Kanal.}
}
\tag{2TP.29}
\]

Da \(\lambda_\Sigma,\lambda_\Delta>0\), sind beide Kanäle separat invertierbar:
\[
Y_\Sigma=-\lambda_\Sigma^{-1}\,\mathrm{Rest}_\Sigma,
\qquad
Y_\Delta=-\lambda_\Delta^{-1}\,\mathrm{Rest}_\Delta.
\tag{2TP.30}
\]

Dies ist exakt der simultane \(T\pm s\)-2×2-Pivot. Es ist **noch keine** Aussage, dass die verbleibenden Restkanäle verschwinden. Insbesondere werden hier weder SW1-AWI noch \(\Delta\)-Descent, HT-RED, A0 oder \(\ker\Gamma_I=\{0\}\) bewiesen.

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

### 4.2 Stufe 2: Row-Zusammensetzung

Die Aggregation des zertifizierten Ledgers ergibt (2TP.10)–(2TP.11). Die Annulus-Hub-Beiträge werden unabhängig aus der kanonischen Hubformel (2TP.12) hergeleitet und liefern (2TP.14)–(2TP.15). Zusammen mit dem Identitätsterm in \(I+A\) entstehen die beiden augmentierten Rows (2TP.16)–(2TP.17) und damit der symmetrische interne Block (2TP.18).

### 4.3 Stufe 3: uniforme Pivotpositivität

Aus den exakten Wortgewichten folgt (2TP.19). Zusammen mit \(\kappa>0\) und \(\log2<1\) erhält man die parameterunabhängigen unteren Schranken (2TP.22)–(2TP.23), also die positive Determinante (2TP.24) und die explizite Inverse (2TP.25).

### 4.4 Stufe 4: Eigenkanäle

Addition und Subtraktion der beiden augmentierten Rows diagonalisiert \(M_T\). Dies liefert (2TP.27)–(2TP.28): \(q\,w(s)\) cancelt im symmetrischen Kanal und erscheint mit Koeffizient \(2q\) im antisymmetrischen Kanal.

### 4.5 Beweisstatus

Alle vier Stufen sind hergeleitet und im finalen Gesamt-Recheck bestanden.

Status:
\[
\boxed{
\mathrm{SW1\!-\!2TP}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

Das reproduzierbare Zertifikat liegt unter scripts/certify_sw1_2tp_ledger.py und prüft die 88 Echo-Fälle, beide Hub-Supportmuster, die exakten Gewichte, die Pivotpositivität sowie die Summe/Differenz-Algebra. Tool/Version und exakter geprüfter Head werden im PR-#17-Reviewrecord dokumentiert.

Der separate Perplexity-Blindcheck ist dokumentiert **FAIL** und erzeugt ausdrücklich kein independent GREEN (cross-model).

Dieser Status ist **keine formale Promotion** und keine externe menschliche Fachbegutachtung.

---

## 5. Finaler adversarialer Review

1. Ledger vollständig (alle elf Wörter erfasst, keines übersehen).
2. Jeder Ledger-Eintrag korrekt gegen die kanonische \(A\)-Definition.
3. \(T+s\)/\(T-s\)-Rows korrekt aus dem Ledger zusammengesetzt.
4. Symmetrie \(c_{++}=c_{--}\), \(c_{+-}=c_{-+}\) tatsächlich bewiesen, nicht angenommen.
5. \(\det M_T>0\) exakt (nicht numerisch) gezeigt.
6. Summen-/Differenzkanalzerlegung korrekt durchgeführt.
7. \(q\,w(s)\)-Verteilung auf die Kanäle tatsächlich abgeleitet, nicht aus Abschnitt 2 übernommen.
8. Scope-Firewall vollständig eingehalten (Abschnitt 0).
9. Promotionsschwelle (independent GREEN / algebraisches Zertifikat) beachtet — keine Promotion allein auf AI-GREEN-Basis.

**Finales Verdict:** Alle neun Punkte bestanden. Gesamtstatus `AI-GREEN candidate + independent GREEN (certificate)`, keine Promotion.

---

## 6. Erwarteter Nutzen bei Erfolg

Mit invertierbarem \(M_T\) ließen sich \(y(T+s)\) und \(y(T-s)\) simultan und eindeutig eliminieren — der eigentliche Full-Rest-Knoten der Kette. Dies allein ändert nichts an HT-RED, A0 oder \(\ker\Gamma_I\) und ist kein Ersatz für SW1-AWI oder \(\Delta\)-Descent.
