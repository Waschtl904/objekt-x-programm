# Audit-Kandidat: SW1-Δ-DESCENT — Stage 1/2: Rows bei 2d±s

> **Stand:** 29. August 2026  
> **Repo-Basis:** main@83f07adf9136d416181d6f38779cd452eb6a4472  
> **Status:** Gesamtziel SW1-Δ-DESCENT weiterhin `?[O]`; Stages 1–4 zertifiziert; Stage 5 PASS; **Stage 5B Companion-Brücke hergeleitet; Stage 6 isolierter Fold-Zertifikat PASS, Kettenstatus erst nach 5B-Zertifizierung**; keine Promotion.  
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


## 7. Stage 4 — Companion-Row-Blöcke

Stage 3 lokalisiert die fehlenden Profile bei
\[
u=\Delta\pm s.
\]
Wir leiten nun die benötigten Rows direkt aus den elf Wörtern von \(A\) ab.

### 7.1 Äußerer Companion-Bereich \(u>\varepsilon\)

Für die tatsächlich benötigten verschobenen Parameter gilt zusätzlich
\[
R<u<2\Delta<e.
\tag{DD.56}
\]

Die direkten 11-Wort-Ledger ergeben:

\[
\boxed{
(Ay)(u)
=
-c_1y(T-u)+c_1y(u)+c_2y(a+u).
}
\tag{DD.57}
\]

\[
\boxed{
(Ay)(a-u)
=
-c_1y(a+u)+c_1y(a-u)+c_2y(T-u).
}
\tag{DD.58}
\]

\[
\boxed{
\begin{aligned}
(Ay)(T-u)
={}&
-c_1y(u)
+\alpha_b y(T-u)
+c_2y(a-u)\\
&+\beta_-y(a+u)
+\beta_b y(2d+u).
\end{aligned}}
\tag{DD.59}
\]

Dabei
\[
\alpha_b=c_1+c_5+c_{11}.
\]

Die zugehörigen Hub-Rows sind
\[
\boxed{
\begin{aligned}
H_{\mathcal A}(u)
={}&
-p[w(a-u)+w(a+u)]\\
&-r[w(b-u)+w(b+u)]
-qw(T-u),
\end{aligned}}
\tag{DD.60}
\]

\[
\boxed{
H_{\mathcal A}(a-u)
=
-pw(u)-pw(T-u)-rw(d+u)-qw(a+u),
}
\tag{DD.61}
\]

\[
\boxed{
H_{\mathcal A}(T-u)
=
pw(a-u)+rw(e-u)-qw(u).
}
\tag{DD.62}
\]

Setze
\[
X_O(u)
:=
\begin{pmatrix}
y(u)\\y(a-u)\\y(T-u)
\end{pmatrix},
\quad
A_+(u):=y(a+u),
\quad
Q(u):=y(2d+u).
\tag{DD.63}
\]

Dann haben die drei augmentierten Rows die Form
\[
\boxed{
M_OX_O(u)
+r_OA_+(u)
+\beta_b e_3Q(u)
+h_O(u)
=0,
}
\tag{DD.64}
\]
mit
\[
M_O=
\begin{pmatrix}
1+c_1&0&-c_1\\
0&1+c_1&c_2\\
-c_1&c_2&1+\alpha_b
\end{pmatrix},
\tag{DD.65}
\]
\[
r_O=
\begin{pmatrix}
c_2\\-c_1\\\beta_-
\end{pmatrix}.
\tag{DD.66}
\]

Der Block ist strikt positiv definit. Tatsächlich sind die ersten beiden führenden Hauptminoren positiv, und
\[
\det M_O
=
(1+c_1)
\left[
(1+c_1)(1+\alpha_b)-c_1^2-c_2^2
\right].
\tag{DD.67}
\]
Wegen
\[
0<c_1<\frac12,\qquad 0<c_2<\frac14,\qquad \alpha_b>0
\]
ist
\[
(1+c_1)(1+\alpha_b)-c_1^2-c_2^2
>
1-\frac14-\frac1{16}
=
\frac{11}{16}>0.
\]
Also
\[
\boxed{M_O>0.}
\tag{DD.68}
\]

### 7.2 Äußerer Δ-Kopplungskoeffizient ist nicht Null

Aus DD.64:
\[
X_O
=
-M_O^{-1}
\bigl(r_OA_++\beta_b e_3Q+h_O\bigr).
\tag{DD.69}
\]

Der \(y\)-Teil von \(G_\pm\) ist genau
\[
r_O^TX_O.
\tag{DD.70}
\]

Setze
\[
S_O
:=
1+\alpha_b
-\frac{c_1^2+c_2^2}{1+c_1}>0.
\tag{DD.71}
\]
Direktes Lösen von \(M_Ox=e_3\) liefert
\[
r_O^TM_O^{-1}e_3
=
-\frac{2c_2}{(1+c_1)S_O}<0.
\tag{DD.72}
\]

Daher besitzt \(G_\pm\) nach Companion-Elimination den neuen Kanal \(Q(u)=y(2d+u)\) mit Koeffizient
\[
\boxed{
\gamma_Q
:=
-\beta_b\,r_O^TM_O^{-1}e_3
\ne0.
}
\tag{DD.73}
\]

Da \(\beta_b<0\) und DD.72 negativ ist, gilt sogar
\[
\gamma_Q<0.
\tag{DD.74}
\]

Damit ist die Verschiebung \(u=\Delta\pm s\) nicht nur formal sichtbar: sie trägt einen **nichtverschwindenden nächsten \(2d+\)-Kanal**.

### 7.3 Innerer Companion-Bereich \(R<u<\varepsilon\), außerhalb \(J\)

Definiere
\[
X_I(u)
:=
\begin{pmatrix}
y(u)\\
y(a-u)\\
y(a+u)\\
y(T-u)\\
y(T+u)
\end{pmatrix}.
\tag{DD.75}
\]

Für
\[
u+\varepsilon<\Delta
\tag{DD.76}
\]
liefern die direkten Rows bei
\[
u,\quad a-u,\quad a+u,
\]
zusammen mit dem zertifizierten 2TP-Paar \(T\pm u\) exakt
\[
\boxed{
M_5X_I(u)
+
\beta_b
\begin{pmatrix}
0\\0\\0\\D_+(u)\\D_-(u)
\end{pmatrix}
+h_5(u)
=0,
}
\tag{DD.77}
\]
wobei
\[
\boxed{
M_5=
\begin{pmatrix}
\alpha_0&c_2&c_2&\beta_0&\beta_0\\
c_2&\alpha_A&-c_1&\beta_+&\beta_-\\
c_2&-c_1&\alpha_A&\beta_-&\beta_+\\
\beta_0&\beta_+&\beta_-&\alpha_T&\beta_T\\
\beta_0&\beta_-&\beta_+&\beta_T&\alpha_T
\end{pmatrix},
}
\tag{DD.78}
\]
mit
\[
\alpha_0=1+2c_1,
\qquad
\alpha_A=1+c_1+c_5,
\qquad
\alpha_T=1+\kappa.
\tag{DD.79}
\]

Die drei neuen direkten A-Rows sind:
\[
\boxed{
(Ay)(u)
=
2c_1y(u)
+c_2[y(a-u)+y(a+u)]
+\beta_0[y(T-u)+y(T+u)].
}
\tag{DD.80}
\]

\[
\boxed{
\begin{aligned}
(Ay)(a-u)
={}&
c_2y(u)
+(c_1+c_5)y(a-u)
-c_1y(a+u)\\
&+\beta_+y(T-u)
+\beta_-y(T+u).
\end{aligned}}
\tag{DD.81}
\]

\[
\boxed{
\begin{aligned}
(Ay)(a+u)
={}&
c_2y(u)
-c_1y(a-u)
+(c_1+c_5)y(a+u)\\
&+\beta_-y(T-u)
+\beta_+y(T+u).
\end{aligned}}
\tag{DD.82}
\]

Die Hub-Komponenten sind
\[
\begin{aligned}
h_u={}&-p[w(a-u)+w(a+u)]
-r[w(b-u)+w(b+u)]-qw(T-u),\\
h_{a-}={}&-pw(u)-pw(T-u)-rw(d+u)-qw(a+u),\\
h_{a+}={}&pw(u)-rw(d-u)-qw(a-u),
\end{aligned}
\tag{DD.83}
\]
ergänzt um die bereits zertifizierten 2TP-Hubwerte bei \(T\pm u\).

Der Block DD.78 ist die exakte Profilmatrix der Kompression von \(I+A\) auf diese fünf disjunkten Kanäle. Da
\[
A=R_{T_0}^*R_{T_0}\ge0,
\]
folgt unmittelbar
\[
\boxed{M_5\ge I>0.}
\tag{DD.84}
\]

Das unabhängige Zertifikat prüft zusätzlich die Matrixeinträge direkt aus den elf Wörtern und bestätigt positive Definitheit symbolisch.

### 7.4 Innerer AWI-Bereich \(J\): endlicher reflektierter \(10\times10\)-Block

Sei
\[
u\in J,
\qquad
t:=\Delta-u\in J.
\tag{DD.85}
\]

Die Rows DD.80 und DD.81 bleiben unverändert. In DD.82 schaltet exakt Wort 11 zu:
\[
+c_{11}y(a+u)
+\beta_b y(T+t).
\tag{DD.86}
\]

Gleichzeitig ist in der 2TP-\(T+u\)-Row
\[
D_-(u)
=
y(2d-u)
=
y(a+t).
\tag{DD.87}
\]

Damit schließen die beiden reflektierten Fünferprofile
\[
X_I(u),\qquad X_I(t)
\]
zu einem endlichen Zehnerblock.

Sei \(E_{33}\) der \(5\times5\)-Matrixeintrag auf dem \(a+\)-Kanal und
\[
C_J
=
\beta_b(E_{35}+E_{53}),
\tag{DD.88}
\]
wobei die Indizes \(3=a+\), \(5=T+\) in der Reihenfolge DD.75 bezeichnen.

Dann ist der gekoppelte Block
\[
\boxed{
\mathbb M_J
=
\begin{pmatrix}
M_5+c_{11}E_{33}&C_J\\
C_J&M_5+c_{11}E_{33}
\end{pmatrix}.
}
\tag{DD.89}
\]

Unter symmetrischer/antisymmetrischer Reflexionszerlegung reduziert er sich auf
\[
M_5+c_{11}E_{33}\pm C_J.
\tag{DD.90}
\]

Auch dieser Block ist die exakte Kompression von \(I+A\) auf den durch die maßtreue AWI-Identifikation gebildeten Profilraum. Daher
\[
\boxed{
\mathbb M_J\ge I>0.
}
\tag{DD.91}
\]

Das Zertifikat bestätigt zusätzlich
\[
M_5+c_{11}E_{33}+C_J>0,
\qquad
M_5+c_{11}E_{33}-C_J>0.
\tag{DD.92}
\]

### 7.5 Konsequenz: echte Δ-Propagationsstruktur

Nach Stage 4 sind sämtliche in Stage 3 auftretenden Companionprofile
\[
y(u),\quad y(a-u),\quad y(T-u)
\]
eliminierbar.

Für
\[
u=\Delta+s
\]
gilt
\[
A_+(u)=y(a+\Delta+s)=D_+(s),
\tag{DD.93}
\]
während
\[
Q(u)=D_+(u)=D_+(\Delta+s).
\tag{DD.94}
\]

Für
\[
u=\Delta-s
\]
gilt entsprechend
\[
A_+(u)=D_-(s),
\qquad
Q(u)=D_+(\Delta-s).
\tag{DD.95}
\]

Damit reduziert sich die nächste Stufe tatsächlich auf eine Kopplung der Form
\[
\boxed{
D_\pm(s)
\longleftrightarrow
D_+(\Delta+s),\ D_+(\Delta-s)
\quad+\quad w\text{-Kanäle},
}
\tag{DD.96}
\]
mit nichtverschwindendem äußerem Kopplungskoeffizienten \(\gamma_Q\).

Dies ist die erste **echte Δ-Propagationsstruktur** des SW1-Angriffs.

Sie ist noch keine finite Rekurrenz, weil für
\[
u>\varepsilon
\]
die Row bei \(2d+u\) noch nicht hergeleitet wurde. Genau diese nächste Schale ist nun der einzige neue y-Rowtyp, der für die Fortsetzung benötigt wird.

**Stage-4-Reviewstatus.** Die Companion-Ledger in den drei Regimen, die positiven Blöcke \(M_O\), \(M_5\), die beiden reflektierten \(J\)-Blöcke sowie der nichtverschwindende nächste-Schalen-Koeffizient \(\gamma_Q<0\) wurden separat adversarial geprüft und durch
scripts/certify_sw1_delta_descent_stage4.py
mit Python/SymPy 1.14.0 reproduzierbar zertifiziert (PASS).

Zertifizierter Script-Blob:
`a96ea8521290b4cf9f369586047ba47193ca0342`.

Damit gilt ausschließlich für Stage 4:
\[
\boxed{
\mathrm{SW1\!-\!\Delta DESCENT\ (Stage\ 4)}:
\text{AI-GREEN}
+
\text{independent GREEN (certificate)}
}
\]

Das Gesamtziel bleibt `?[O]`.


## 8. Stage 5 — erste äußere Δ-Schale \(D_+(\Delta+s)\)

Stage 4 zeigt, dass der nächste nichtverschwindende y-Kanal
\[
D_+(\Delta+s)
=
y(2d+\Delta+s)
\]
tatsächlich auftritt. Wir leiten seine Row nun direkt aus HT.3/HT.4 ab.

### 8.1 Direkte 11-Wort-Row

Für
\[
R<s<\varepsilon
\]
setze
\[
x_1:=2d+\Delta+s.
\tag{DD.97}
\]

Die Gate-/Horizon-Klassifikation ist auf ganz SW1 uniform, unabhängig davon, ob \(s\in J\) liegt. Es überleben exakt acht Echo-Beiträge und sie gruppieren sich zu

\[
\boxed{
\begin{aligned}
(Ay)(2d+\Delta+s)
={}&
-c_1y(2e-\Delta-s)
+\alpha_b y(2d+\Delta+s)\\
&+\beta_-y(T-2\Delta-s)
+c_2y(2\Delta+s)
+\beta_b y(T-\Delta-s).
\end{aligned}}
\tag{DD.98}
\]

Dies wurde nicht durch formales Verschieben von DD.13 gewonnen, sondern erneut aus allen elf Wörtern abgeleitet.

### 8.2 Hub-Row

Bei \(u=2d+\Delta+s\) sind sämtliche rechten Hubäste außerhalb des Annulus. Für die linken Äste gilt

\[
u-a=2\Delta+s,
\]
\[
u-b=-(e-\Delta-s),
\]
\[
u-T=-(2e-\Delta-s).
\]

Da auf SW1
\[
e-\Delta-s>e-2\Delta>0,
\]
folgt mit der Oddheit von \(w\)

\[
\boxed{
(HE_{\mathcal A}w)(2d+\Delta+s)
=
p\,w(2\Delta+s)
-r\,w(e-\Delta-s)
-q\,w(2e-\Delta-s).
}
\tag{DD.99}
\]

Damit lautet die augmentierte erste äußere Schalenrow

\[
\boxed{
\begin{aligned}
0={}&
(1+\alpha_b)y(2d+\Delta+s)
+\beta_-y(T-2\Delta-s)
+c_2y(2\Delta+s)\\
&+\beta_b y(T-\Delta-s)
-c_1y(2e-\Delta-s)\\
&+p\,w(2\Delta+s)
-r\,w(e-\Delta-s)
-q\,w(2e-\Delta-s).
\end{aligned}}
\tag{DD.100}
\]

### 8.3 Exakte Verschiebungsstruktur

Vergleicht man DD.100 mit DD.18, so ist nun **post hoc** sichtbar:

\[
\begin{array}{c|c}
\text{Stage-1-Profil} & \text{Stage-5-Profil}\\ \hline
2d+s & 2d+(\Delta+s)\\
T-\Delta-s & T-2\Delta-s\\
\Delta+s & 2\Delta+s\\
T-s & T-\Delta-s\\
2e-s & 2e-\Delta-s
\end{array}
\tag{DD.101}
\]

Die Koeffizienten bleiben exakt
\[
1+\alpha_b,\quad \beta_-,\quad c_2,\quad \beta_b,\quad -c_1.
\]

Damit ist die erste äußere Δ-Propagation direkt reproduziert.

### 8.4 Noch kein allgemeines n-Lemma

DD.100 rechtfertigt **nicht** ohne weitere Gateprüfung die Formel für beliebiges
\[
2d+n\Delta+s.
\]

Tatsächlich nähert sich bei höheren Schalen das linke \(3a\)-Gate dem aktiven Bereich. Daher wird jede weitere Schale separat oder durch ein eigenes uniformes \(n\)-Lemma zu prüfen sein.

Der unmittelbar nächste Companionparameter ist
\[
v:=2\Delta+s.
\tag{DD.102}
\]
Für ihn müssen die Companion-Rows
\[
v,\qquad a-v,\qquad T-v
\]
direkt klassifiziert werden. Erst danach kann entschieden werden, ob DD.100 zu einer zweiten echten Δ-Propagation führt oder an einer neuen Wall zerfällt.


## 8A. Stage 5B — fehlende Companion-Brücke und zweite äußere Δ-Schale

Vor Verwendung von Stage 6 muss die in DD.102 ausdrücklich offene Zwischenstufe geschlossen werden.

### 8A.1 Erweiterter äußerer Companionblock für \(m=2,3,4\)

Setze
\[
u_m:=m\Delta+s,
\qquad
m\in\{2,3,4\}.
\tag{DD.102a}
\]

Da
\[
\varepsilon<\Delta<u_m<(m+1)\Delta\le5\Delta<a,
\tag{DD.102b}
\]
liegen alle drei Parameter strikt außerhalb des inneren Strips und noch links von \(a\).

Die direkte 11-Wort-Klassifikation liefert für **jedes**
\[
m\in\{2,3,4\}
\]
dieselben drei A-Rows:

\[
\boxed{
(Ay)(u_m)
=
-c_1y(T-u_m)+c_1y(u_m)+c_2y(a+u_m).
}
\tag{DD.102c}
\]

\[
\boxed{
(Ay)(a-u_m)
=
-c_1y(a+u_m)+c_1y(a-u_m)+c_2y(T-u_m).
}
\tag{DD.102d}
\]

\[
\boxed{
\begin{aligned}
(Ay)(T-u_m)
={}&
-c_1y(u_m)
+\alpha_b y(T-u_m)
+c_2y(a-u_m)\\
&+\beta_-y(a+u_m)
+\beta_b y(2d+u_m).
\end{aligned}}
\tag{DD.102e}
\]

Damit ist die y-Matrix **exakt dieselbe** wie in DD.65:
\[
\boxed{
M_O=
\begin{pmatrix}
1+c_1&0&-c_1\\
0&1+c_1&c_2\\
-c_1&c_2&1+\alpha_b
\end{pmatrix}>0.
}
\tag{DD.102f}
\]

Die Hubanteile werden ohne unnötige Vorzeichen-Fallzerlegung in ihrer kanonischen Form belassen:
\[
h_O(u_m)
:=
\begin{pmatrix}
(HE_{\mathcal A}w)(u_m)\\
(HE_{\mathcal A}w)(a-u_m)\\
(HE_{\mathcal A}w)(T-u_m)
\end{pmatrix}.
\tag{DD.102g}
\]
Alle eventuell wechselnden Vorzeichen einzelner \(w\)-Argumente betreffen nur die rechte Seite, nicht den invertierbaren y-Block.

Folglich gilt für \(m=2,3,4\) erneut
\[
X_O(u_m)
=
-M_O^{-1}
\bigl(r_Oy(a+u_m)+\beta_b e_3D_+(u_m)+h_O(u_m)\bigr),
\tag{DD.102h}
\]
mit demselben nichtverschwindenden Kopplungskoeffizienten
\[
\gamma_Q<0
\]
aus DD.73–DD.74.

### 8A.2 Fehlende zweite äußere Schalenrow

Setze
\[
x_2:=2d+2\Delta+s.
\tag{DD.102i}
\]

Die direkte 11-Wort-Klassifikation ist auf ganz SW1 uniform. Es überleben exakt acht Echos und

\[
\boxed{
\begin{aligned}
(Ay)(2d+2\Delta+s)
={}&
-c_1y(2e-2\Delta-s)
+\alpha_b y(2d+2\Delta+s)\\
&+\beta_-y(T-3\Delta-s)
+c_2y(3\Delta+s)
+\beta_b y(T-2\Delta-s).
\end{aligned}}
\tag{DD.102j}
\]

Für den Hub gilt exakt
\[
\boxed{
\begin{aligned}
(HE_{\mathcal A}w)(2d+2\Delta+s)
={}&
p\,w(3\Delta+s)\\
&+r\,w(2\Delta+s-e)
+q\,w(2\Delta+s-2e),
\end{aligned}}
\tag{DD.102k}
\]
wobei \(w\) als ungerade, annulus-getragene Funktion verstanden wird; die Formel benötigt daher keine zusätzliche Vorzeichenkammer.

Somit
\[
\boxed{
\begin{aligned}
0={}&
(1+\alpha_b)y(2d+2\Delta+s)
+\beta_-y(T-3\Delta-s)
+c_2y(3\Delta+s)\\
&+\beta_b y(T-2\Delta-s)
-c_1y(2e-2\Delta-s)\\
&+p\,w(3\Delta+s)
+r\,w(2\Delta+s-e)
+q\,w(2\Delta+s-2e).
\end{aligned}}
\tag{DD.102l}
\]

### 8A.3 Lückenlose Propagationskette bis Stage 6

Stage 5 erzeugt als Companionparameter
\[
u_2=2\Delta+s.
\]
DD.102h eliminiert dessen Companionprofile und erzeugt wegen
\[
\gamma_Q\ne0
\]
den nächsten Kanal
\[
D_+(u_2)=y(2d+2\Delta+s),
\]
dessen Row DD.102l nun direkt vorliegt.

Diese zweite Schalenrow enthält den Companionparameter
\[
u_3=3\Delta+s.
\]
Erneut liefert DD.102h den nächsten Kanal
\[
D_+(u_3)=y(2d+3\Delta+s).
\]

Damit ist der Übergang
\[
\boxed{
D_+(\Delta+s)
\longrightarrow
D_+(2\Delta+s)
\longrightarrow
D_+(3\Delta+s)
}
\tag{DD.102m}
\]
jetzt vollständig durch direkte Rows und invertierbare Companionblöcke belegt.

Für die untere Stage-6-Unterkammer tritt anschließend
\[
u_4=4\Delta+s
\]
auf; DD.102h gilt auch hierfür und ermöglicht die Fortsetzung zur vierten äußeren Schale.


## 9. Stage 6 — dritte äußere Schale und 2TP-Fold

Die direkte Iteration bleibt nicht beliebig uniform. Der erste neue Gate-Wall tritt bei der dritten äußeren Schale auf.

Setze
\[
h_3:=a-4\Delta.
\tag{DD.103}
\]

Für die festen Konstanten gilt
\[
\Delta<h_3<2\Delta.
\tag{DD.104}
\]
Äquivalent sind
\[
a-5\Delta>0,
\qquad
6\Delta-a>0.
\]

Betrachte
\[
x_3:=2d+3\Delta+s.
\tag{DD.105}
\]

### 9.1 Unterhalb der neuen Wall

Falls
\[
s+\varepsilon<h_3,
\tag{DD.106}
\]
bleibt die bisherige äußere Schalenstruktur erhalten. Es überleben exakt acht Echos und

\[
\boxed{
\begin{aligned}
(Ay)(2d+3\Delta+s)
={}&
-c_1y(2e-3\Delta-s)
+\alpha_b y(2d+3\Delta+s)\\
&+\beta_-y(T-4\Delta-s)
+c_2y(4\Delta+s)
+\beta_b y(T-3\Delta-s).
\end{aligned}}
\tag{DD.107}
\]

### 9.2 Oberhalb der Wall: exakter Rückfall in 2TP

Falls
\[
s+\varepsilon>h_3,
\tag{DD.108}
\]
setze
\[
t:=h_3-s=a-4\Delta-s.
\tag{DD.109}
\]

Dann gilt zunächst
\[
t<\varepsilon.
\]
Andererseits folgt aus \(R+\varepsilon<\Delta\)
\[
t
>
h_3-\varepsilon
>
h_3-(\Delta-R)
=
R+(a-5\Delta)
>
R.
\tag{DD.110}
\]

Also
\[
\boxed{t\in(R,\varepsilon).}
\tag{DD.111}
\]

Ferner
\[
2d+3\Delta+s
=
T-t.
\tag{DD.112}
\]

Die direkte 11-Wort-Klassifikation liefert nun exakt 16 Echos und

\[
\boxed{
\begin{aligned}
(Ay)(x_3)
={}&
\kappa y(T-t)
+\beta_0y(t)
+\beta_-y(a+t)
+\beta_+y(a-t)\\
&+\beta_Ty(T+t)
+\beta_by(2d+t).
\end{aligned}}
\tag{DD.113}
\]

Dies ist wortgleich die bereits zertifizierte gespiegelte 2TP-A-Row bei Parameter \(t\).

Die Profilidentitäten sind
\[
t=2e-3\Delta-s,
\tag{DD.114}
\]
\[
a+t=T-4\Delta-s,
\qquad
a-t=4\Delta+s,
\tag{DD.115}
\]
\[
T+t=3a-4\Delta-s,
\qquad
2d+t=T-3\Delta-s.
\tag{DD.116}
\]

Auch der Hub stimmt mit 2TP überein:
\[
\boxed{
(HE_{\mathcal A}w)(x_3)
=
p\,w(a-t)+r\,w(e-t)-q\,w(t).
}
\tag{DD.117}
\]

Damit ist auf der oberen Seite der neuen Wall **kein neuer Pivot nötig**:
\[
\boxed{
s+\varepsilon>h_3
\Longrightarrow
\text{dritte äußere Δ-Schale fällt exakt in SW1-2TP zurück.}
}
\tag{DD.118}
\]

### 9.3 Bedeutung für die finite Kette

Stage 6 erzeugt erstmals einen echten Fold-Mechanismus:

- unterhalb \(s+\varepsilon=h_3\) propagiert die äußere Δ-Schale weiter;
- oberhalb der Wall endet die neue Schalenhierarchie bereits nach drei Δ-Schritten im zertifizierten 2TP-System.

Damit ist eine unendliche uniforme Kaskade ausgeschlossen **für die obere Stage-6-Unterkammer**. Die untere Unterkammer DD.106 muss noch separat bis zur nächsten Wall verfolgt werden.


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
