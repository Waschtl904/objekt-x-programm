# Audit-Kandidat: SW1-Δ-DESCENT — Stage 1/2: Rows bei 2d±s

> **Stand:** 29. August 2026  
> **Repo-Basis:** main@83f07adf9136d416181d6f38779cd452eb6a4472  
> **Status:** Gesamtziel SW1-Δ-DESCENT weiterhin `?[O]`; **Stage 1/2 und Stage 3 jeweils AI-GREEN + independent GREEN (certificate)**; keine Promotion.  
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

## 6. Stage 3 — 2TP-Schur-Elimination und exakter Nichtabschluss

### 6.1 Notation für den zertifizierten 2TP-Pivot

Setze
\[
\tau:=1+\kappa,\qquad
\theta:=\beta_T,\qquad
D_T:=\tau^2-\theta^2>0,
\tag{DD.21}
\]
und
\[
D_+(s):=y(2d+s),\qquad
D_-(s):=y(2d-s).
\tag{DD.22}
\]

Definiere die 2TP-Restterme ohne die \(2d\)-Profile:
\[
\begin{aligned}
F_+(s):={}&
\beta_0y(s)+\beta_-y(a-s)+\beta_+y(a+s)\\
&+p\,w(a+s)+r\,w(e+s)+q\,w(s),
\end{aligned}
\tag{DD.23}
\]
\[
\begin{aligned}
F_-(s):={}&
\beta_0y(s)+\beta_-y(a+s)+\beta_+y(a-s)\\
&+p\,w(a-s)+r\,w(e-s)-q\,w(s).
\end{aligned}
\tag{DD.24}
\]

Dann sind die zertifizierten 2TP-Rows äquivalent zu
\[
\begin{pmatrix}
\tau&\theta\\
\theta&\tau
\end{pmatrix}
\binom{y(T+s)}{y(T-s)}
=
-\binom{F_+(s)+\beta_bD_-(s)}
{F_-(s)+\beta_bD_+(s)}.
\tag{DD.25}
\]

Somit
\[
y(T+s)
=
-\frac{
\tau[F_++\beta_bD_-]
-\theta[F_-+\beta_bD_+]}
{D_T},
\tag{DD.26}
\]
\[
y(T-s)
=
\frac{
\theta[F_++\beta_bD_-]
-\tau[F_-+\beta_bD_+]}
{D_T}.
\tag{DD.27}
\]

### 6.2 Die verschobenen Restprofile

Schreibe
\[
\begin{aligned}
G_+(s):={}&
\beta_-y(T-\Delta-s)
+c_2y(\Delta+s)
-c_1y(2e-s)\\
&+p\,w(\Delta+s)-r\,w(e-s)-q\,w(2e-s),
\end{aligned}
\tag{DD.28}
\]
\[
\begin{aligned}
G_-(s):={}&
\beta_-y(T-\Delta+s)
+c_2y(\Delta-s)
-c_1y(2e+s)\\
&+p\,w(\Delta-s)-r\,w(e+s)-q\,w(2e+s).
\end{aligned}
\tag{DD.29}
\]

Dann lauten DD.18–DD.19
\[
(1+\alpha_b)D_+ +\beta_b y(T-s)+G_+=0,
\tag{DD.30}
\]
\[
(1+\alpha_b)D_- +\beta_b y(T+s)+G_-
+1_J(s)\beta_+y(T+\Delta-s)=0.
\tag{DD.31}
\]

### 6.3 Effektiver \(2\times2\)-Schur-Pivot für \(D_\pm\)

Einsetzen von DD.26–DD.27 ergibt
\[
\boxed{
K_DD_+(s)+L_DD_-(s)+\widehat G_+(s)=0,
}
\tag{DD.32}
\]
\[
\boxed{
L_DD_+(s)+K_DD_-(s)+\widehat G_-(s)
+1_J(s)\beta_+y(T+\Delta-s)=0,
}
\tag{DD.33}
\]
mit
\[
K_D
=
1+\alpha_b-\frac{\tau\beta_b^2}{D_T},
\qquad
L_D
=
\frac{\theta\beta_b^2}{D_T},
\tag{DD.34}
\]
und
\[
\widehat G_+
=
G_+
+\frac{\beta_b}{D_T}\,[\theta F_+-\tau F_-],
\tag{DD.35}
\]
\[
\widehat G_-
=
G_-
+\frac{\beta_b}{D_T}\,[-\tau F_++\theta F_-].
\tag{DD.36}
\]

Die Eigenwerte dieses neuen symmetrischen Blocks sind
\[
\mu_\Sigma
=
K_D+L_D
=
1+\alpha_b-\frac{\beta_b^2}{\tau+\theta},
\tag{DD.37}
\]
\[
\mu_\Delta
=
K_D-L_D
=
1+\alpha_b-\frac{\beta_b^2}{\tau-\theta}.
\tag{DD.38}
\]

### 6.4 Exakte uniforme Positivität

Aus SW1-2TP:
\[
\tau+\theta>\frac38,
\qquad
\tau-\theta>1.
\tag{DD.39}
\]

Ferner
\[
|\beta_b|
=
c_{11}
=
\frac{2\log3}{3\sqrt3}
<\frac12.
\tag{DD.40}
\]

Für die letzte Schranke genügt:
\[
e^{9/8}
>
1+\frac98+\frac{(9/8)^2}{2}
+\frac{(9/8)^3}{6}
+\frac{(9/8)^4}{24}
=
\frac{100331}{32768}
>3,
\]
also
\[
\log3<\frac98.
\]
Außerdem \(\sqrt3>3/2\). Daher
\[
c_{11}
<
\frac{2(9/8)}{3(3/2)}
=
\frac12.
\]

Da \(\alpha_b>0\),
\[
\boxed{
\mu_\Sigma
>
1-\frac{(1/2)^2}{3/8}
=
\frac13>0,
}
\tag{DD.41}
\]
und
\[
\boxed{
\mu_\Delta
>
1-\frac{(1/2)^2}{1}
=
\frac34>0.
}
\tag{DD.42}
\]

Folglich ist der effektive \(D_\pm\)-Block uniform invertierbar.

### 6.5 Was auf dem AWI-Bereich \(J\) passiert

Für \(s\in J\) setze
\[
t:=\Delta-s\in J\subset(R,\varepsilon).
\tag{DD.43}
\]
Dann
\[
T+\Delta-s=T+t,
\]
also darf exakt der zertifizierte 2TP-Pivot bei Parameter \(t\) eingesetzt werden.

Dabei gilt physisch
\[
D_-(t)=y(2d-t)=y(a+s),
\tag{DD.44}
\]
während
\[
D_+(t)=y(2d+t)
\tag{DD.45}
\]
ein weiterer blinder \(2d+\)-Kanal bleibt.

Explizit enthält
\[
\beta_+y(T+t)
\]
nach 2TP einen nichtverschwindenden Term
\[
\boxed{
\frac{\beta_+\theta\beta_b}{D_T}\,D_+(t),
}
\tag{DD.46}
\]
dessen Koeffizient ungleich Null ist. AWI identifiziert den \(D_-(t)\)-Branch mit \(y(a+s)\), beseitigt aber \(D_+(t)\) nicht.

### 6.6 Exakte Blindlage der verschobenen Companion-Profile

Setze
\[
u_\pm:=\Delta\pm s.
\tag{DD.47}
\]
Aus SW1 folgt
\[
u_\pm>R.
\tag{DD.48}
\]

Ferner liegen für beide Vorzeichen die drei physischen Punkte
\[
u_\pm,\qquad a-u_\pm,\qquad T-u_\pm
\tag{DD.49}
\]
im exakten KNF-Blindbereich.

Genauer:
\[
0<u_\pm<a-R,
\qquad
0<a-u_\pm<a-R,
\tag{DD.50}
\]
und
\[
b+R<T-u_\pm<T-R.
\tag{DD.51}
\]

Für den knappsten Fall \(u_+=\Delta+s\) benutzt man
\[
s+R<\Delta,
\qquad
2\Delta<e,
\]
woraus
\[
T-u_+-(b+R)
=
e-\Delta-s-R
>
e-2\Delta
>0
\]
folgt.

Damit sind insbesondere
\[
y(\Delta\pm s),\qquad
y(2e\mp s)=y(a-u_\pm),\qquad
y(T-\Delta\mp s)=y(T-u_\pm)
\tag{DD.52}
\]
echte freie \(Z_R^+\)-Koordinaten der SW1-KNF-Normalform.

### 6.7 Stage-3-Negativresultat: 2TP + AWI schließen den Δ-Descent noch nicht

Die Koeffizienten der drei verschobenen \(y\)-Profile in \(G_\pm\) sind
\[
\beta_-\ne0,\qquad c_2\ne0,\qquad -c_1\ne0.
\tag{DD.53}
\]

Nach SW1-KNF sind diese Profile im blinden Bereich freie Koordinaten; sie werden von der inneren Kernelgleichung nicht rekonstruiert.

Daher liefern DD.32–DD.33 zwar einen **neuen uniform invertierbaren Schur-Pivot für \(D_\pm\)**, aber noch **keine geschlossene Rekurrenz in \(w\)** und auch keine geschlossene Rekurrenz ausschließlich in den bisherigen \(s\)-Profilen.

Auf \(J\) kommt nach 2TP zusätzlich der freie Kanal \(D_+(t)\) aus DD.46 hinzu.

Somit:
\[
\boxed{
\text{SW1-2TP + SW1-AWI + die Rows bei }2d\pm s
\text{ allein schließen den }\Delta\text{-Descent nicht.}
}
\tag{DD.54}
\]

Dies ist **kein No-Go gegen einen Δ-Descent mit weiteren Rows**. Es lokalisiert exakt die fehlende Stufe:

\[
\boxed{
\text{Companion-Rows für }
u,\ a-u,\ T-u
\quad\text{mit }u=\Delta\pm s.
}
\tag{DD.55}
\]

Der nächste Angriff ist daher nicht „Rekurrenz behaupten“, sondern die direkte 11-Wort-Ableitung dieser Companion-Rows.

**Stage-3-Reviewstatus.** Der exakte Schur-Pivot, die Schranken
\[
\mu_\Sigma>\frac13,\qquad \mu_\Delta>\frac34,
\]
die nichtverschwindende \(J\)-Zusatzkopplung und die KNF-Blindlage der Companionprofile wurden separat adversarial gegengeprüft und durch
scripts/certify_sw1_delta_descent_stage3.py
mit Python/SymPy 1.14.0 reproduzierbar zertifiziert (PASS).

Damit gilt ausschließlich für Stage 3:
\[
\boxed{
\mathrm{SW1\!-\!\Delta DESCENT\ (Stage\ 3)}:
\text{AI-GREEN}
+
\text{independent GREEN (certificate)}
}
\]

Das Gesamtziel bleibt:
\[
\boxed{\mathrm{SW1\!-\!\Delta DESCENT}:?[O].}
\]


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
