# Audit-Kandidat: SW1-Δ-DESCENT — Stage 1/2: Rows bei 2d±s

> **Stand:** 29. August 2026  
> **Repo-Basis:** main@83f07adf9136d416181d6f38779cd452eb6a4472  
> **Status:** Gesamtziel SW1-Δ-DESCENT weiterhin `?[O]`; **Stage 1/2 = AI-GREEN + independent GREEN (certificate)**; keine Promotion.  
> **Scope:** ausschließlich die direkte 11-Wort-Ableitung und Hub-Auswertung bei \(x=2d\pm s\) auf SW1.

---

## 0. Firewall

Dieses Audit beweist noch **keine** \(\Delta\)-Rekurrenz und keine finite Terminierung.

Insbesondere kein:
- HT-RED;
- A0;
- \(\ker\Gamma_I=\{0\}\);
- Full-Rest-Abschluss;
- Objekt X;
- RH.

Die historischen Scratch-Formeln für \((Ay)(2d\pm s)\) werden **nicht als Input** verwendet. Input sind nur HT.3/HT.4 aus audits/P11_R32_TAIL_FG_PIVOT_CANDIDATE.md sowie die bereits auf main verfügbaren SW1-2TP-/SW1-AWI-Strukturen erst **nach** Abschluss der direkten Row-Ableitung.

---

## 1. Setup

\[
a=\frac12\log2,\qquad b=\frac12\log3,\qquad T=2a,
\]
\[
d=b-a,\qquad e=T-b,\qquad \Delta=d-e=2d-a,
\]
und
\[
0<\sigma\le R<\varepsilon,\qquad R+\varepsilon<\Delta,\qquad T_0=T+\varepsilon.
\tag{DD.1}
\]

Für
\[
R<s<\varepsilon
\tag{DD.2}
\]
setzen wir
\[
x_\pm:=2d\pm s=a+\Delta\pm s.
\tag{DD.3}
\]

Die Vier-Echo-Formel lautet
\[
\begin{aligned}
(W_{\delta,\eta}^{(\lambda)}y)(x)
={}&-\chi_\lambda(x-\delta)\widetilde y(x-\delta-\eta)
+\chi_\lambda(x-\delta)\widetilde y(x-\delta+\eta)\\
&+\chi_\lambda(x+\delta)\widetilde y(x+\delta-\eta)
-\chi_\lambda(x+\delta)\widetilde y(x+\delta+\eta),
\end{aligned}
\tag{DD.4}
\]
mit
\[
\chi_\lambda(u)=1_{\{|u|\le T_0-\lambda\}}.
\]

---

## 2. Stage 1 — vollständiges 11-Wort-Ledger

### 2.1 Uniformes Gate-Muster

Für beide Rows \(x=2d\pm s\) gilt auf ganz SW1:

- Wörter 1–6 und 11: linkes Gate \(x-\delta\) offen;
- Wörter 7–10: linkes Gate geschlossen;
- für alle elf Wörter: rechtes Gate \(x+\delta\) geschlossen.

Damit können nur \(E_1,E_2\) der Wörter 1–6 und 11 beitragen.

Die einzige nicht-uniforme **Source-Horizon**-Entscheidung tritt bei \(x=2d-s\) auf:
\[
T+\Delta-s<T_0
\iff
s>\Delta-\varepsilon.
\tag{DD.5}
\]

Definiere deshalb
\[
J:=(\Delta-\varepsilon,\varepsilon).
\tag{DD.6}
\]
Ist \(\varepsilon<\Delta/2\), ist \(J\) leer. Bei \(\varepsilon=\Delta/2\) bleibt nur der L²-nullige Berührfall. Ist \(\varepsilon>\Delta/2\), ist dies exakt der bereits durch SW1-AWI normalisierte Überlapp.

### 2.2 Row \(x=2d+s\)

| Wort | überlebender Beitrag |
|---:|---|
| 1 | \(-c_1y(2e-s)+c_1y(2d+s)\) |
| 2 | \(-c_2y(T-\Delta-s)\) |
| 3 | \(0\) |
| 4 | \(-c_4y(T-\Delta-s)+c_4y(\Delta+s)\) |
| 5 | \(+c_5y(2d+s)\) |
| 6 | \(0\) |
| 7 | \(0\) |
| 8 | \(0\) |
| 9 | \(0\) |
| 10 | \(0\) |
| 11 | \(-c_{11}y(T-s)+c_{11}y(2d+s)\) |

Exakt acht Echo-Beiträge überleben.

### 2.3 Row \(x=2d-s\), außerhalb \(J\)

Für
\[
s<\Delta-\varepsilon
\tag{DD.7}
\]
gilt:

| Wort | überlebender Beitrag |
|---:|---|
| 1 | \(-c_1y(2e+s)+c_1y(2d-s)\) |
| 2 | \(-c_2y(T-\Delta+s)\) |
| 3 | \(0\) |
| 4 | \(-c_4y(T-\Delta+s)+c_4y(\Delta-s)\) |
| 5 | \(+c_5y(2d-s)\) |
| 6 | \(0\) |
| 7 | \(0\) |
| 8 | \(0\) |
| 9 | \(0\) |
| 10 | \(0\) |
| 11 | \(-c_{11}y(T+s)+c_{11}y(2d-s)\) |

Wieder exakt acht Echo-Beiträge.

### 2.4 Row \(x=2d-s\), auf \(J\)

Für
\[
s>\Delta-\varepsilon
\tag{DD.8}
\]
überleben zusätzlich genau
\[
+c_2y(T+\Delta-s)
\]
aus Wort 2 und
\[
+c_6y(T+\Delta-s)
\]
aus Wort 6.

Also insgesamt zehn Echo-Beiträge.

Da
\[
c_2+c_6=\beta_+,
\tag{DD.9}
\]
ist die gesamte Umschaltung exakt
\[
1_J(s)\,\beta_+\,y(T+\Delta-s).
\tag{DD.10}
\]

**Struktureller Punkt:** Für \(s\in J\) ist
\[
t:=\Delta-s\in J\subset(R,\varepsilon),
\]
also
\[
T+\Delta-s=T+t
\]
wieder eine echte SW1-Tail-Koordinate. Genau hier kann später SW1-2TP eingesetzt werden; dies wird in Stage 1 noch nicht benutzt.

---

## 3. Stage 2 — aggregierte A-Rows

Mit
\[
\alpha_b:=c_1+c_5+c_{11}>0,
\tag{DD.11}
\]
\[
\beta_-:=-c_2-c_4,\qquad
\beta_+:=c_2+c_6,\qquad
\beta_b:=-c_{11},
\tag{DD.12}
\]
und \(c_4=c_2\) folgt

\[
\boxed{
\begin{aligned}
(Ay)(2d+s)
={}&-c_1y(2e-s)
+\alpha_b y(2d+s)
+\beta_-y(T-\Delta-s)\\
&+c_2y(\Delta+s)
+\beta_b y(T-s).
\end{aligned}}
\tag{DD.13}
\]

Für die gespiegelte Row:
\[
\boxed{
\begin{aligned}
(Ay)(2d-s)
={}&-c_1y(2e+s)
+\alpha_b y(2d-s)
+\beta_-y(T-\Delta+s)\\
&+c_2y(\Delta-s)
+\beta_b y(T+s)
+1_J(s)\beta_+y(T+\Delta-s).
\end{aligned}}
\tag{DD.14}
\]

Die einzige Piecewise-Struktur ist damit exakt der bereits bekannte AWI-Bereich \(J\).

---

## 4. Stage 2 — Hub bei \(2d\pm s\)

Für den Annulus-Hub
\[
(HE_{\mathcal A}w)(u)
=
p[w(u-a)-w(u+a)]
+r[w(u-b)-w(u+b)]
+q[w(u-T)-w(u+T)]
\tag{DD.15}
\]
sind bei \(u=2d\pm s\) sämtliche rechten Äste annulus-tot.

Da
\[
2d-a=\Delta,\qquad
2d-b=-e,\qquad
2d-T=-2e,
\]
und \(w\) ungerade ist, folgt uniform auf SW1:
\[
\boxed{
(HE_{\mathcal A}w)(2d+s)
=
p\,w(\Delta+s)-r\,w(e-s)-q\,w(2e-s),
}
\tag{DD.16}
\]
\[
\boxed{
(HE_{\mathcal A}w)(2d-s)
=
p\,w(\Delta-s)-r\,w(e+s)-q\,w(2e+s).
}
\tag{DD.17}
\]

Für die unteren Schranken gilt insbesondere
\[
\Delta-s>R
\]
aus \(R+s<R+\varepsilon<\Delta\), und ebenso \(e-s>R\), \(2e-s>R\). Für die oberen Schranken:
\[
\Delta+s<2\Delta<e<T,
\]
\[
e+s<e+\Delta=d<T,
\]
\[
2e+s<2e+\Delta=a<T.
\]
Damit liegen alle sechs linken Argumentbeträge strikt im Annulus. Für die rechten Äste ist bereits der kleinste Fall
\[
(2d-s)+a=T+\Delta-s>T+R\ge T+\sigma=S,
\]
also sind sämtliche rechten Äste annulus-tot.

---

## 5. Augmentierte Rows

Aus
\[
(I+A)y+HE_{\mathcal A}w=0
\]
folgt
\[
\boxed{
\begin{aligned}
0={}&(1+\alpha_b)y(2d+s)
+\beta_-y(T-\Delta-s)
+c_2y(\Delta+s)
+\beta_b y(T-s)
-c_1y(2e-s)\\
&+p\,w(\Delta+s)-r\,w(e-s)-q\,w(2e-s),
\end{aligned}}
\tag{DD.18}
\]
und
\[
\boxed{
\begin{aligned}
0={}&(1+\alpha_b)y(2d-s)
+\beta_-y(T-\Delta+s)
+c_2y(\Delta-s)
+\beta_b y(T+s)\\
&+1_J(s)\beta_+y(T+\Delta-s)
-c_1y(2e+s)\\
&+p\,w(\Delta-s)-r\,w(e+s)-q\,w(2e+s).
\end{aligned}}
\tag{DD.19}
\]

Der direkte Diagonalpivot
\[
1+\alpha_b>1
\tag{DD.20}
\]
ist strikt positiv. Das allein beweist noch keine \(\Delta\)-Rekurrenz.

---

## 6. Zertifikatsstatus und nächste Stufe

Das reproduzierbare Skript scripts/certify_sw1_delta_descent_stage12.py prüft:
- beide Gate-Muster in den unteren/oberen \(s+\varepsilon\)-Kammern;
- acht überlebende Echos bei \(2d+s\);
- acht Echos bei \(2d-s\) außerhalb \(J\);
- zehn Echos bei \(2d-s\) auf \(J\);
- die eindeutige Umschaltung \(\beta_+y(T+\Delta-s)\);
- die aggregierten A-Profile;
- die Hub-Source-Identitäten;
- \(1+\alpha_b>1\).

Die lokal ausgeführte identische Skriptfassung liefert mit SymPy 1.14.0:
\[
\boxed{\text{PASS}.}
\]

Der adversariale Re-Review des technisch korrigierten Heads ist für den Scope von Stage 1/2 bestanden.

Damit gilt ausschließlich für die direkte Row-/Hub-Stufe:
\[
\boxed{
\mathrm{SW1\!-\!\Delta DESCENT\ (Stage\ 1/2)}:
\text{AI-GREEN}
+
\text{independent GREEN (certificate)}
}
\]

Zertifikatsprovenienz:
- Tool: Python + SymPy 1.14.0;
- Skript: scripts/certify_sw1_delta_descent_stage12.py;
- zertifizierter Scope: Gate-/Horizon-Ledger, Echo-Zählung, eindeutige (J)-Umschaltung, aggregierte A-Rows, Hub-Source-Identitäten, positiver direkter Diagonalpivot;
- Ergebnis: PASS.

Das **Gesamtziel** SW1-Δ-DESCENT bleibt ausdrücklich offen:
\[
\boxed{\mathrm{SW1\!-\!\Delta DESCENT}:?[O].}
\]

Nächste Stufe:

1. ersetze die \(T\pm s\)-Kanäle mit dem zertifizierten SW1-2TP;
2. behandle auf \(J\) den zusätzlichen Tailwert \(T+\Delta-s\) mit \(t=\Delta-s\) und SW1-2TP/AWI;
3. identifiziere danach, ob die verbleibenden \(\Delta\pm s\)-Kanäle tatsächlich eine **geschlossene** Rekurrenz erzeugen;
4. beweise erst dann finite Terminierung.

Keine Promotion.
