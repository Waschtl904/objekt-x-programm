# Audit-Kandidat: SW1-Δ-DESCENT — Stage 1/2: Rows bei 2d±s

> **Stand:** 29. August 2026  
> **Repo-Basis:** main@83f07adf9136d416181d6f38779cd452eb6a4472  
> **Status:** Gesamtziel SW1-Δ-DESCENT weiterhin `?[O]`; Stages 1/2–9 zertifiziert; **Stage 10A Wall/Fold + äußerer Durchgangsblock hergeleitet, globaler Restblock auf (J_B) offen**; keine Promotion.  
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

### 8A.1 Erweiterter äußerer Companionblock für \(m=2,3\) und für \(m=4\) unterhalb der Stage-6-Wall

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

Die direkte 11-Wort-Klassifikation liefert für
\[
m\in\{2,3\}
\]
auf ganz SW1 dieselben drei A-Rows. Für \(m=4\) gelten dieselben Rows genau in der unteren Stage-6-Unterkammer
\[
s+\varepsilon<h_3=a-4\Delta.
\tag{DD.102b'}
\]
Oberhalb dieser Wall schaltet im \(u_4\)-Companion-Ledger zusätzliche Struktur zu; diese Region wird jedoch bereits durch den direkten Stage-6-Fold in 2TP geschlossen und benötigt den äußeren \(u_4\)-Block nicht.

In den genannten Bereichen gelten:

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

Folglich gilt für \(m=2,3\) auf ganz SW1 und für \(m=4\) unter DD.102b' erneut
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
auf; dort gilt wegen \(s+\varepsilon<h_3\) weiterhin DD.102h und ermöglicht die Fortsetzung zur vierten äußeren Schale. In der oberen Stage-6-Unterkammer ist diese Fortsetzung nicht nötig, weil DD.118 bereits direkt in den zertifizierten 2TP-Pivot faltet.


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

**Review-/Zertifikatsstatus Stages 5, 5B, 6.**

- Stage 5: `scripts/certify_sw1_delta_descent_stage5.py`, Python/SymPy 1.14.0, Blob `b6e196fce9343fa082aeacee26a76dbdec5f4013`, PASS.
- Stage 5B: `scripts/certify_sw1_delta_descent_stage5b.py`, Python/SymPy 1.14.0, Blob `e0fdc02c95764178a5c62caa7971f6bc10c400f6`, PASS.
- Stage 6: `scripts/certify_sw1_delta_descent_stage6.py`, Python/SymPy 1.14.0, Blob `158bf530c065266ad670d42a8aeb43b2ebddd03b`, PASS.

Für diese drei lokal formulierten Stufen gilt jeweils
\[
\boxed{\text{AI-GREEN + independent GREEN (certificate)}}.
\]

Dies ist **keine** Promotion und noch **kein** vollständiger SW1-Δ-DESCENT.



## 10. Stage 7 — endlicher Abschluss des neuen y-Schalengraphen

Stage 7 schließt **nur die Hierarchie neu entstehender y-Rowtypen**. Sie beweist noch nicht, dass die verbleibende w-Gleichung trivialen Kern besitzt.

### 10.1 Erweiterter lokaler 2TP-Pivot für \(0<u<\varepsilon\)

Die direkte 11-Wort-Klassifikation der beiden Rows \(T\pm u\) benötigt für die reine Row-Algebra nicht \(u>R\). Für
\[
0<u<\varepsilon<\Delta
\tag{DD.119}
\]
überleben in beiden Rows exakt 16 Echos, und es gelten dieselben A-Formeln wie in SW1-2TP:

\[
\boxed{
\begin{aligned}
(Ay)(T+u)
={}&
\kappa y(T+u)
+\beta_0y(u)
+\beta_-y(a-u)
+\beta_+y(a+u)\\
&+\beta_Ty(T-u)
+\beta_by(2d-u),
\end{aligned}}
\tag{DD.120}
\]

\[
\boxed{
\begin{aligned}
(Ay)(T-u)
={}&
\kappa y(T-u)
+\beta_0y(u)
+\beta_-y(a+u)
+\beta_+y(a-u)\\
&+\beta_Ty(T+u)
+\beta_by(2d+u).
\end{aligned}}
\tag{DD.121}
\]

Mit der Nullfortsetzung des Annulusprofils \(w\) gelten zugleich
\[
\boxed{
(HE_{\mathcal A}w)(T+u)
=
p\,w(a+u)+r\,w(e+u)+q\,w(u),
}
\tag{DD.122}
\]
\[
\boxed{
(HE_{\mathcal A}w)(T-u)
=
p\,w(a-u)+r\,w(e-u)-q\,w(u).
}
\tag{DD.123}
\]

Falls \(u<R\), ist insbesondere \(w(u)=0\); die Formel selbst bleibt unverändert.

Der Tailblock bleibt
\[
M_T=
\begin{pmatrix}
1+\kappa&\beta_T\\
\beta_T&1+\kappa
\end{pmatrix}>0,
\tag{DD.124}
\]
also ist der lokale \(T\pm u\)-Pivot für jedes \(0<u<\varepsilon\) algebraisch invertierbar.

**Firewall:** Diese Erweiterung ist kein neuer Blindheits- oder Membershipsatz. Für \(u<R\) werden die übrigen Profile nicht als blind bezeichnet; lediglich die beiden \(T\)-Rows sind invertierbar gekoppelt.

### 10.2 Zweite Wall
Setze
\[
h_4:=a-5\Delta,
\qquad
g_6:=6\Delta-a.
\tag{DD.125}
\]
Dann
\[
0<g_6<h_4<h_3,
\qquad
h_4+g_6=\Delta.
\tag{DD.126}
\]

In der unteren Stage-6-Unterkammer
\[
s+\varepsilon<h_3
\]
tritt nun die zweite Wall
\[
s+\varepsilon=h_4
\tag{DD.127}
\]
auf.

Falls
\[
h_4<s+\varepsilon<h_3,
\tag{DD.128}
\]
ist
\[
x_4:=2d+4\Delta+s
=
T-(h_4-s).
\tag{DD.129}
\]
Aus \(s+\varepsilon>h_4\) folgt
\[
|h_4-s|<\varepsilon
\tag{DD.130}
\]
bis auf den Nullmengenfall \(s=h_4\). Daher liegt \(x_4\) exakt in einem der beiden erweiterten \(T\pm u\)-Rows aus DD.120–DD.124.

Somit endet die neue y-Schalenhierarchie in dieser mittleren Unterkammer bereits an Schale 4.

### 10.3 Unterste Unterkammer: vierte äußere Schalenrow

Bleibt
\[
s+\varepsilon<h_4.
\tag{DD.131}
\]
Dann liegt \(x_4\) noch außerhalb des erweiterten \(T\)-Strips. Die direkte 11-Wort-Klassifikation liefert exakt acht Echos:

\[
\boxed{
\begin{aligned}
(Ay)(2d+4\Delta+s)
={}&
-c_1y(2e-4\Delta-s)
+\alpha_b y(2d+4\Delta+s)\\
&+\beta_-y(T-5\Delta-s)
+c_2y(5\Delta+s)
+\beta_b y(T-4\Delta-s).
\end{aligned}}
\tag{DD.132}
\]

Der Hub lautet ohne zusätzliche Vorzeichenkammer
\[
\boxed{
\begin{aligned}
(HE_{\mathcal A}w)(2d+4\Delta+s)
={}&
p\,w(5\Delta+s)\\
&+r\,w(4\Delta+s-e)
+q\,w(4\Delta+s-2e).
\end{aligned}}
\tag{DD.133}
\]

Der nächste Companionparameter ist
\[
u_5:=5\Delta+s.
\tag{DD.134}
\]

### 10.4 Terminaler \(u_5\)-Companionblock

Unter DD.131 gilt
\[
u_5<a.
\]
Die beiden Rows bei \(u_5\) und \(a-u_5\) behalten exakt die äußere Form DD.102c–DD.102d.

Für die Row bei \(T-u_5\) entscheidet nur noch die terminale Wall
\[
q:=g_6+s
\quad\text{gegen}\quad
\varepsilon.
\tag{DD.135}
\]

#### Fall A: \(q<\varepsilon\)

Dann ist das Wort-11-Gate aktiv, und der vollständige Companionblock ist wieder
\[
M_O>0
\]
mit der nichtverschwindenden Kopplung \(\beta_b y(2d+u_5)\).

Der nächste Schalenwert ist aber
\[
2d+u_5
=
2d+5\Delta+s
=
T+q.
\tag{DD.136}
\]
Wegen \(0<q<\varepsilon\) fällt er unmittelbar in den erweiterten 2TP-Pivot DD.119–DD.124.

#### Fall B: \(q>\varepsilon\)

Dann liegt
\[
2d+u_5=T+q>T+\varepsilon=T_0,
\tag{DD.137}
\]
also ist dieser nächste y-Wert horizon-tot.

Gleichzeitig schließt im \(T-u_5\)-Row exakt das Wort-11-Gate. Der terminale Companionblock lautet
\[
\boxed{
M_{O,0}
=
\begin{pmatrix}
1+c_1&0&-c_1\\
0&1+c_1&c_2\\
-c_1&c_2&1+c_1+c_5
\end{pmatrix}.
}
\tag{DD.138}
\]

Auch
\[
\boxed{M_{O,0}>0.}
\tag{DD.139}
\]
Es existiert in diesem Fall überhaupt kein neuer \(D_+\)-Kanal mehr.

Der Gleichheitsfall \(q=\varepsilon\) liegt auf einer einzelnen Wall und ist als \(L^2\)-Grenz-/Nullmengenfall unschädlich.

### 10.5 Exhaustive finite y-shell closure

Damit ist die neue y-Schalenhierarchie auf ganz SW1 in drei Hauptfälle zerlegt:

\[
\boxed{
\begin{array}{ll}
s+\varepsilon>h_3
&
\Rightarrow
\text{Fold bei }D_+(3\Delta+s)\text{ in SW1-2TP},\\[1mm]
h_4<s+\varepsilon<h_3
&
\Rightarrow
\text{Fold bei }D_+(4\Delta+s)\text{ in extended 2TP},\\[1mm]
s+\varepsilon<h_4
&
\Rightarrow
\text{höchstens noch }D_+(5\Delta+s),\\
&
\quad\text{danach extended 2TP oder Horizon-Tod.}
\end{array}}
\tag{DD.140}
\]

Somit:
\[
\boxed{
\text{Nach spätestens fünf Δ-Schritten entsteht kein neuer y-Schalentyp mehr.}
}
\tag{DD.141}
\]

Dies ist ein **endlicher Abschluss des y-Schalengraphen**, noch nicht die Trivialität des gesamten augmentierten Kerns.

### 10.6 Verbleibender Engpass

Nach DD.141 ist der nächste mathematische Knoten nicht mehr geometrische Schalenexhaustivität, sondern die tatsächliche **w-Elimination** in dem nun endlichen y-Schur-System:

\[
\boxed{
\text{finite y-shell closure}
\;\Longrightarrow\;
\text{derive exact induced annulus operator on }w.
}
\tag{DD.142}
\]

Erst wenn dieser induzierte w-Operator trivialen Kern besitzt, wäre der SW1-Δ-DESCENT als Eliminationsmechanismus geschlossen.

**Stage-7-Reviewstatus.** Der erweiterte lokale 2TP-Pivot, die zweite Wall \(h_4\), die achtechoige vierte äußere Schalenrow, beide terminalen \(u_5\)-Companionblöcke und der endgültige Horizon-/2TP-Abschluss wurden separat adversarial geprüft und durch
`scripts/certify_sw1_delta_descent_stage7.py`
mit Python/SymPy 1.14.0 reproduzierbar zertifiziert (PASS).

Zertifizierter Script-Blob:
`b5ec192cd672e24774c448cefcc4a5c48353d191`.

Damit gilt ausschließlich für Stage 7:
\[
\boxed{
\mathrm{SW1\!-\!\Delta DESCENT\ (Stage\ 7)}:
\text{AI-GREEN}
+
\text{independent GREEN (certificate)}
}
\]

Das Gesamtziel bleibt weiterhin
\[
\boxed{\mathrm{SW1\!-\!\Delta DESCENT}:?[O].}
\]



## 11. Stage 8 — pointwise KNF-Sampled-/B-Differenzblock

Stage 7 schließt den neuen y-Schalengraphen. Für den Übergang zu einem reinen Annulusoperator muss nun die KNF-Innenrelation tatsächlich eingesetzt werden.

Definiere für jedes Zentrum \(c\)
\[
D_c(s):=y(c+s)-y(c-s).
\tag{DD.143}
\]

### 11.1 Direkte Rows bei \(e\pm s\) und \(d\pm s\)

Die elf Wörter liefern uniform auf SW1:

\[
\boxed{
(Ay)(e+s)
=
-c_1y(b-s)+c_1y(e+s)+c_2y(a+e+s),
}
\tag{DD.144}
\]
\[
\boxed{
(Ay)(e-s)
=
-c_1y(b+s)+c_1y(e-s)+c_2y(a+e-s).
}
\tag{DD.145}
\]

Ferner
\[
\boxed{
(Ay)(d+s)
=
-c_1y(a+e-s)+c_1y(d+s)+c_2y(b+s),
}
\tag{DD.146}
\]
\[
\boxed{
(Ay)(d-s)
=
-c_1y(a+e+s)+c_1y(d-s)+c_2y(b-s).
}
\tag{DD.147}
\]

### 11.2 Direkte Rows bei \(b\pm s\)

Uniform gilt
\[
\boxed{
\begin{aligned}
(Ay)(b+s)
={}&
-c_1y(e-s)
+\alpha_b y(b+s)
+\beta_-y(a+e-s)\\
&+c_2y(d+s)
+\beta_b y(b-s),
\end{aligned}}
\tag{DD.148}
\]

\[
\boxed{
\begin{aligned}
(Ay)(b-s)
={}&
-c_1y(e+s)
+\alpha_b y(b-s)
+\beta_-y(a+e+s)\\
&+c_2y(d-s)
+\beta_b y(b+s).
\end{aligned}}
\tag{DD.149}
\]

Damit besitzt der reine \(b\)-Antisymmetriekanal bereits den strikten Pivot
\[
1+\alpha_b-\beta_b
=
1+c_1+c_5+2c_{11}>1.
\tag{DD.150}
\]

### 11.3 Direkte Rows bei \((a+e)\pm s\)

Es gilt
\[
\boxed{
\begin{aligned}
(Ay)(a+e+s)
={}&
-c_1y(d-s)
+\alpha_b y(a+e+s)
+\beta_-y(b-s)\\
&+c_2y(e+s)
+\beta_b y(b+\Delta-s),
\end{aligned}}
\tag{DD.151}
\]

\[
\boxed{
\begin{aligned}
(Ay)(a+e-s)
={}&
-c_1y(d+s)
+\alpha_b y(a+e-s)
+\beta_-y(b+s)\\
&+c_2y(e-s)
+\beta_b y(b+\Delta+s).
\end{aligned}}
\tag{DD.152}
\]

Der einzige neue y-Differenzkanal ist somit
\[
D_{b+\Delta}(s).
\tag{DD.153}
\]

### 11.4 Punktweiser \(4\times4\)-Differenzblock

Subtrahiere jeweils die Minus-Row von der Plus-Row und addiere den Identitätsterm aus \(I+A\). Setze
\[
X_B(s)
:=
\begin{pmatrix}
D_e(s)\\
D_d(s)\\
D_b(s)\\
D_{a+e}(s)
\end{pmatrix}.
\tag{DD.154}
\]

Schreibe die entsprechenden Hub-Differenzen kompakt als
\[
W_c(s)
:=
(HE_{\mathcal A}w)(c+s)
-
(HE_{\mathcal A}w)(c-s),
\tag{DD.155}
\]
und
\[
W_B(s)
:=
\begin{pmatrix}
W_e(s)\\W_d(s)\\W_b(s)\\W_{a+e}(s)
\end{pmatrix}.
\]

Dann gilt punktweise a.e.
\[
\boxed{
M_BX_B(s)
+
c_{11}e_4D_{b+\Delta}(s)
+
W_B(s)
=0,
}
\tag{DD.156}
\]
wobei
\[
\boxed{
M_B=
\begin{pmatrix}
1+c_1&0&c_1&c_2\\
0&1+c_1&c_2&c_1\\
c_1&c_2&1+c_1+c_5+2c_{11}&2c_2\\
c_2&c_1&2c_2&1+c_1+c_5+c_{11}
\end{pmatrix}.
}
\tag{DD.157}
\]

Das Zertifikat bestätigt
\[
\boxed{M_B>0.}
\tag{DD.158}
\]

### 11.5 Die Kopplung zum nächsten B-Zentrum verschwindet nicht

Setze
\[
A_0:=1+c_1,
\]
und eliminiere zunächst die ersten beiden Koordinaten. Der Schurblock auf den Koordinaten \(D_b,D_{a+e}\) besitzt den positiven Offdiagonalterm
\[
\eta_B
=
2c_2-\frac{2c_1c_2}{1+c_1}
=
\frac{2c_2}{1+c_1}>0.
\tag{DD.159}
\]

Da der Schurblock positiv definit ist, ist sein Inversen-Offdiagonale strikt negativ:
\[
(M_B^{-1})_{3,4}<0.
\tag{DD.160}
\]

Folglich enthält die rekonstruierte \(D_b\)-Koordinate den externen Kanal \(D_{b+\Delta}\) mit Koeffizient
\[
\boxed{
\gamma_B
:=
-c_{11}(M_B^{-1})_{3,4}>0.
}
\tag{DD.161}
\]

Insbesondere
\[
\boxed{\gamma_B\ne0.}
\tag{DD.162}
\]

Damit existiert neben der bereits geschlossenen \(2d+\)-Schalenpropagation eine zweite, echte Differenzpropagation zum Zentrum \(b+\Delta\).

### 11.6 Globale Reflexions-Firewall

Der punktweise Block DD.156 darf **noch nicht** als globaler direkter Summenblock auf \(L^2(R,\varepsilon)\) behandelt werden.

Denn auf dem AWI-Bereich
\[
J=(\Delta-\varepsilon,\varepsilon)
\]
und mit
\[
t=\Delta-s
\]
gelten die physischen Identitäten
\[
\boxed{
e+s=d-t,
}
\tag{DD.163}
\]
und
\[
\boxed{
a+e+s=b-t.
}
\tag{DD.164}
\]

Damit identifizieren sich die \(e/d\)- bzw. \((a+e)/b\)-Profile unter **derselben maßtreuen Involution**
\[
s\longmapsto\Delta-s
\]
wie in SW1-AWI.

Folglich lautet der aktuelle Status ausdrücklich:

\[
\boxed{
\text{Stage 8 pointwise algebra: candidate/certifiable;}
\quad
\text{globaler }L^2\text{-B-Block: }?[O].
}
\tag{DD.165}
\]

Der nächste zwingende Schritt ist ein eigener reflektierter B-Block-Audit auf \(J\), bevor \(\gamma_B\) zu einer globalen Rekurrenz oder zu einem induzierten \(w\)-Operator verwendet werden darf.

**Stage-8-Pointwise-Reviewstatus.** Die acht direkten Rows, der konstante Differenzblock \(M_B\), seine positive Definitheit, der nichtverschwindende Koeffizient \(\gamma_B>0\) sowie die beiden Reflexionsidentitäten wurden separat adversarial geprüft und durch
`scripts/certify_sw1_delta_descent_stage8_pointwise.py`
mit Python/SymPy 1.14.0 reproduzierbar zertifiziert (PASS).

Zertifizierter Script-Blob:
`12ddf9577e7f4c377480b96c311d643beb452625`.

Damit gilt ausschließlich:
\[
\boxed{
\mathrm{Stage\ 8\ pointwise}:
\text{AI-GREEN}
+
\text{independent GREEN (certificate)}
}
\]

Der globale reflektierte \(L^2(J)\)-Block bleibt ausdrücklich
\[
\boxed{?[O]}.
\]



## 12. Stage 9 — globaler reflektierter B-Block auf \(J\)

Stage 8 pointwise darf auf \(J\) nicht direkt integriert werden. Wir quotientieren daher zuerst die physische Doppelzählung.

### 12.1 Halbe Orbitdomäne und zwölf eindeutige Profile

Nur im oberen AWI-Fall
\[
\varepsilon>\frac{\Delta}{2}
\]
ist \(J\) nichtleer. Setze
\[
K:=(\Delta-\varepsilon,\Delta/2),
\qquad
t:=\Delta-s
\quad (s\in K).
\tag{DD.166}
\]
Dann parametrisiert \(K\) jeden nichttrivialen Reflexionsorbit \(\{s,t\}\subset J\) genau einmal; der Fixpunkt \(s=t=\Delta/2\) ist \(L^2\)-null.

Mit
\[
C:=a+e=b-\Delta
\]
gelten die vier exakten Identifikationen
\[
e+s=d-t,\qquad
d-s=e+t,
\tag{DD.167}
\]
\[
b-s=C+t,\qquad
C+s=b-t.
\tag{DD.168}
\]

Damit bleiben von den nominell sechzehn Profilen bei
\[
e\pm s,\ d\pm s,\ b\pm s,\ C\pm s
\]
und denselben acht Profilen bei \(t\) exakt zwölf eindeutige physische Kanäle.

Wir ordnen sie als
\[
\boxed{
\begin{aligned}
X_J(s):=(
&y(e-s),\,y(e+s),\,y(d-s),\,y(d+s),\\
&y(b-s),\,y(b+s),\,y(C-s),\,y(C+s),\\
&y(e-t),\,y(d+t),\,y(b+t),\,y(C-t)
)^T .
\end{aligned}}
\tag{DD.169}
\]

Die zwölf zugehörigen Bildintervalle über \(K\) sind bis auf Randpunkte paarweise disjunkt. Der Pullback
\[
\mathcal E_J:L^2(K)^{12}\to H_{T_0}^+
\tag{DD.170}
\]
ist daher nach der kanonischen Maßidentifikation isometrisch auf seinen physischen Bildraum.

### 12.2 Exakter 12-Kanal-Block

Setze
\[
Q_s:=y(b+\Delta+s),
\qquad
Q_t:=y(b+\Delta+t).
\tag{DD.171}
\]

Die direkten elf-Wort-Rows an den zwölf eindeutigen Punkten ergeben
\[
\boxed{
\mathbb B_JX_J
+
\beta_b(e_7Q_s+e_{12}Q_t)
+
W_J
=0,
}
\tag{DD.172}
\]
wobei \(W_J\) die zwölf entsprechenden Hubwerte bezeichnet.

Die Matrix \(\mathbb B_J\) ist reell-symmetrisch. Noch wichtiger:
\[
\boxed{
\mathbb B_J
=
\mathcal E_J^*(I+A)\mathcal E_J
\ge I.
}
\tag{DD.173}
\]
Denn \(A=R_{T_0}^*R_{T_0}\ge0\).

Damit ist der globale reflektierte B-Block bereits als Operator auf dem korrekt quotientierten Profilraum strikt positiv.

### 12.3 Reflexionspermutation

Die Involution \(s\leftrightarrow t\) permutiert die zwölf Koordinaten in den Paaren
\[
(1,9),\ (2,3),\ (4,10),\ (5,8),\ (6,11),\ (7,12).
\tag{DD.174}
\]

Sei \(\mathsf P\) die zugehörige unitäre Permutationsinvolution. Dann
\[
\mathsf P^2=I,
\qquad
\mathsf P^*=\mathsf P,
\qquad
[\mathbb B_J,\mathsf P]=0.
\tag{DD.175}
\]

Folglich zerfällt
\[
L^2(K)^{12}
=
\mathcal H_+\oplus\mathcal H_-
\tag{DD.176}
\]
in symmetrische/antisymmetrische Reflexionssektoren.

### 12.4 Die beiden exakten \(6\times6\)-Blöcke

Für
\[
\sigma\in\{+1,-1\}
\]
schreibe
\[
Z_\sigma
=
(z_1,\ldots,z_6)^T
\]
für die Paar-Summen (\(\sigma=+1\)) bzw. Paar-Differenzen (\(\sigma=-1\)) der sechs Paare aus DD.174.

Dann reduziert sich DD.172 auf
\[
\boxed{
B_\sigma Z_\sigma
+
\beta_b e_6 Q_\sigma
+
W_\sigma
=0,
}
\tag{DD.177}
\]
mit
\[
Q_\sigma:=Q_s+\sigma Q_t.
\tag{DD.178}
\]

Der konstante Reflexionsblock ist
\[
\boxed{
B_\sigma=
\begin{pmatrix}
1+c_1&0&0&0&-c_1&c_2\\
0&1+c_1&0&-c_1+\sigma c_2&0&0\\
0&0&1+c_1&0&c_2&-c_1\\
0&-c_1+\sigma c_2&0&1+\alpha_b-2\sigma c_2&-c_{11}&0\\
-c_1&0&c_2&-c_{11}&1+\alpha_b&-2c_2\\
c_2&0&-c_1&0&-2c_2&1+\alpha_b
\end{pmatrix}.
}
\tag{DD.179}
\]

Da DD.179 nur die unitäre Reflexionsreduktion von DD.173 ist,
\[
\boxed{
B_+\ge I,
\qquad
B_-\ge I.
}
\tag{DD.180}
\]
Insbesondere sind beide Blöcke invertierbar.

### 12.5 Globale nächste-Zentrum-Koordinate

Die aktuellen \(b\)-Differenzen erfüllen
\[
D_b(s)+\sigma D_b(t)
=
z_5-z_4.
\tag{DD.181}
\]

Für das nächste Zentrum \(b+\Delta\) setze
\[
N_\sigma
:=
D_{b+\Delta}(s)+\sigma D_{b+\Delta}(t).
\tag{DD.182}
\]

Wegen
\[
b+\Delta-s=b+t,
\qquad
b+\Delta-t=b+s
\tag{DD.183}
\]
gilt exakt
\[
\boxed{
N_\sigma
=
Q_\sigma-\sigma z_5.
}
\tag{DD.184}
\]

Aus DD.177 folgt
\[
Z_\sigma
=
-B_\sigma^{-1}
\bigl(\beta_b e_6Q_\sigma+W_\sigma\bigr).
\tag{DD.185}
\]

Setze
\[
a_\sigma:=
\langle e_5,B_\sigma^{-1}e_6\rangle .
\tag{DD.186}
\]
Dann
\[
N_\sigma
=
\nu_\sigma Q_\sigma
+
\sigma\langle e_5,B_\sigma^{-1}W_\sigma\rangle,
\tag{DD.187}
\]
mit
\[
\boxed{
\nu_\sigma
=
1+\sigma\beta_b a_\sigma.
}
\tag{DD.188}
\]

Aus \(B_\sigma\ge I\) folgt
\[
\|B_\sigma^{-1}\|\le1,
\qquad
|a_\sigma|\le1.
\tag{DD.189}
\]
Ferner ist aus den bereits bewiesenen Koeffizientenschranken
\[
|\beta_b|=c_{11}<\frac12.
\tag{DD.190}
\]
Daher
\[
\boxed{
\nu_\sigma
\ge
1-|\beta_b||a_\sigma|
>
\frac12.
}
\tag{DD.191}
\]

Somit kann \(Q_\sigma\) in beiden Reflexionssektoren eindeutig durch
\[
N_\sigma
\quad\text{und}\quad
W_\sigma
\]
rekonstruiert werden.

### 12.6 Konsequenz

Der Stage-8-Firewall ist damit geschlossen:

\[
\boxed{
\text{Der globale reflektierte B-Block auf }J
\text{ ist strikt invertierbar.}
}
\tag{DD.192}
\]

Außerhalb \(J\) gilt bereits der punktweise positive Block \(M_B\). Auf \(J\) gilt DD.192. Daher kann die B-Differenzelimination auf ganz SW1 global durchgeführt werden, ohne physische Profile doppelt zu zählen.

Zusätzlich ist die Weitergabe an das nächste Zentrum \(b+\Delta\) in beiden Reflexionssektoren nichtsingulär, da
\[
\nu_\pm>\frac12.
\tag{DD.193}
\]

**Firewall:** Dies beweist noch nicht, dass die gesamte B-Zentrumskette endlich terminiert und noch nicht, dass der induzierte Annulusoperator auf \(w\) trivialen Kern besitzt.

Der nächste offene Knoten ist daher:
\[
\boxed{
\text{B-Zentrum-Propagation ab }b+\Delta.
}
\tag{DD.194}
\]

**Stage-9-Reviewstatus.** Der 16→12-Quotient, die disjunkten halben Orbitintervalle, der exakte 12-Kanal-Kompressionsblock, die Reflexionspermutation, beide (6\times6)-Sektoren und die Schranke \(\nu_\pm>1/2\) wurden separat adversarial geprüft und durch
`scripts/certify_sw1_delta_descent_stage9.py`
mit Python/SymPy 1.14.0 reproduzierbar zertifiziert (PASS).

Zertifizierter Script-Blob:
`990a6bbd26b8f853fb22a54b8b310a5b4a376896`.

Damit gilt für Stage 9:
\[
\boxed{
\mathrm{Stage\ 9}:
\text{AI-GREEN}
+
\text{independent GREEN (certificate)}
}
\]



## 13. Stage 10A — B-Zentrum-Wall \(h_B\), äußerer Durchgangsblock und innerer Fold

Setze
\[
B_1:=b+\Delta,
\qquad
B_2:=b+2\Delta,
\tag{DD.195}
\]
und
\[
E_0:=e-\Delta,
\qquad
D_1:=d+\Delta,
\qquad
F_0:=a+e-\Delta.
\tag{DD.196}
\]

Dann gilt die feste Identität
\[
\boxed{
h_B:=E_0=e-\Delta=a-e-2\Delta=T-B_1.
}
\tag{DD.197}
\]

Ferner
\[
\Delta<h_B<2\Delta.
\tag{DD.198}
\]

Die neue Wall ist
\[
s+\varepsilon=h_B.
\tag{DD.199}
\]

Definiere
\[
J_B:=(h_B-\varepsilon,\varepsilon).
\tag{DD.200}
\]
Sie ist genau dann nichtleer, wenn
\[
\varepsilon>\frac{h_B}{2}.
\]

### 13.1 Unterhalb der Wall: uniformer äußerer Differenzblock

Falls
\[
s+\varepsilon<h_B,
\tag{DD.201}
\]
liefern die direkten elf-Wort-Rows:

\[
\boxed{
(Ay)(E_0+s)
=
-c_1y(B_1-s)
+c_1y(E_0+s)
+c_2y(F_0+s),
}
\tag{DD.202}
\]

\[
\boxed{
(Ay)(E_0-s)
=
-c_1y(B_1+s)
+c_1y(E_0-s)
+c_2y(F_0-s),
}
\tag{DD.203}
\]

\[
\boxed{
(Ay)(D_1+s)
=
-c_1y(F_0-s)
+c_1y(D_1+s)
+c_2y(B_1+s),
}
\tag{DD.204}
\]

\[
\boxed{
(Ay)(D_1-s)
=
-c_1y(F_0+s)
+c_1y(D_1-s)
+c_2y(B_1-s),
}
\tag{DD.205}
\]

\[
\boxed{
\begin{aligned}
(Ay)(B_1+s)
={}&
-c_1y(E_0-s)
+\alpha_b y(B_1+s)
+\beta_-y(F_0-s)\\
&+c_2y(D_1+s)
+\beta_b y(C-s),
\end{aligned}}
\tag{DD.206}
\]

\[
\boxed{
\begin{aligned}
(Ay)(B_1-s)
={}&
-c_1y(E_0+s)
+\alpha_b y(B_1-s)
+\beta_-y(F_0+s)\\
&+c_2y(D_1-s)
+\beta_b y(C+s),
\end{aligned}}
\tag{DD.207}
\]

\[
\boxed{
\begin{aligned}
(Ay)(F_0+s)
={}&
-c_1y(D_1-s)
+\alpha_b y(F_0+s)
+\beta_-y(B_1-s)\\
&+c_2y(E_0+s)
+\beta_b y(B_2-s),
\end{aligned}}
\tag{DD.208}
\]

\[
\boxed{
\begin{aligned}
(Ay)(F_0-s)
={}&
-c_1y(D_1+s)
+\alpha_b y(F_0-s)
+\beta_-y(B_1+s)\\
&+c_2y(E_0-s)
+\beta_b y(B_2+s).
\end{aligned}}
\tag{DD.209}
\]

Setze
\[
X_{B,1}(s)
:=
\begin{pmatrix}
D_{E_0}(s)\\
D_{D_1}(s)\\
D_{B_1}(s)\\
D_{F_0}(s)
\end{pmatrix}.
\tag{DD.210}
\]

Nach Subtraktion der Minus- von der Plus-Row und Hinzunahme des Identitätsterms ergibt sich

\[
\boxed{
M_{B,1}X_{B,1}
+
c_{11}e_3D_C
+
c_{11}e_4D_{B_2}
+
W_{B,1}
=0,
}
\tag{DD.211}
\]
mit

\[
\boxed{
M_{B,1}
=
\begin{pmatrix}
1+c_1&0&c_1&c_2\\
0&1+c_1&c_2&c_1\\
c_1&c_2&1+\alpha_b&2c_2\\
c_2&c_1&2c_2&1+\alpha_b
\end{pmatrix}.
}
\tag{DD.212}
\]

Der Block zerfällt unter der Paarreflexion
\[
(E_0,D_1)\leftrightarrow(E_0,D_1),
\qquad
(B_1,F_0)\leftrightarrow(B_1,F_0)
\]
in die beiden \(2\times2\)-Blöcke

\[
K_\sigma
=
\begin{pmatrix}
1+c_1&c_1+\sigma c_2\\
c_1+\sigma c_2&1+\alpha_b+2\sigma c_2
\end{pmatrix},
\qquad
\sigma=\pm1.
\tag{DD.213}
\]

Beide sind strikt positiv definit; damit
\[
\boxed{M_{B,1}>0.}
\tag{DD.214}
\]

Außerdem
\[
\det K_+-\det K_-
=
4c_2>0.
\tag{DD.215}
\]

Daher ist
\[
(M_{B,1}^{-1})_{3,4}<0.
\tag{DD.216}
\]

Somit ist der durch Schur-Elimination induzierte Durchgangskoeffizient vom alten Zentrum \(C\) zum nächsten Zentrum \(B_2\)

\[
\boxed{
\gamma_{B,1}
:=
-c_{11}^2(M_{B,1}^{-1})_{3,4}
>0.
}
\tag{DD.217}
\]

Insbesondere verschwindet die \(B\)-Zentrum-Propagation unterhalb der Wall nicht.

### 13.2 Oberhalb der Wall: neue Reflexion \(s\mapsto h_B-s\)

Sei
\[
s+\varepsilon>h_B.
\tag{DD.218}
\]
Dann
\[
u:=h_B-s
\tag{DD.219}
\]
erfüllt
\[
R<u<\varepsilon.
\tag{DD.220}
\]

Wegen \(h_B>\Delta\) gilt sogar
\[
u+\varepsilon>\Delta,
\]
also
\[
u\in J.
\tag{DD.221}
\]

Die vier exakten Profilidentitäten lauten

\[
\boxed{
E_0-s=u,
}
\tag{DD.222}
\]
\[
\boxed{
D_1+s=a-u,
}
\tag{DD.223}
\]
\[
\boxed{
F_0-s=a+u,
}
\tag{DD.224}
\]
\[
\boxed{
B_1+s=T-u.
}
\tag{DD.225}
\]

Damit sind die direkten Rows bei
\[
E_0-s,\quad D_1+s,\quad F_0-s,\quad B_1+s
\]
**exakt** die bereits zertifizierten inneren Rows bei
\[
u,\quad a-u,\quad a+u,\quad T-u.
\]

Da \(u\in J\), gehört dieser Fold zum bereits zertifizierten Stage-4/AWI-\(10\times10\)-Block.

Insbesondere ist die gesamte „Plus-Hälfte“ der neuen \(B_1\)-Wall kein neuer unbekannter Rowtyp.

### 13.3 Was oberhalb der Wall noch offen bleibt

Die komplementären vier Profile
\[
E_0+s,\qquad
D_1-s,\qquad
B_1-s,\qquad
F_0+s
\tag{DD.226}
\]
bleiben außerhalb dieses unmittelbaren Folds.

Ihre vier direkten Rows besitzen wiederum einen symmetrischen positiven Rohblock, koppeln jedoch zugleich an
\[
C+s
\quad\text{und}\quad
B_2-s.
\]

Bevor daraus eine globale Weitergabe \(B_1\to B_2\) abgeleitet werden darf, muss geprüft werden, ob diese Restprofile über die neue Involution
\[
\boxed{
\mathcal J_B:s\mapsto h_B-s
}
\tag{DD.227}
\]
mit den bereits gefalteten inneren Profilen auf \(J_B\) physisch überlappen.

Daher lautet der Stage-10A-Status:

\[
\boxed{
\begin{array}{l}
\text{unterhalb }s+\varepsilon=h_B:
\text{ positiver Durchgangsblock mit }\gamma_{B,1}>0;\\[1mm]
\text{oberhalb }s+\varepsilon=h_B:
\text{ Plus-Hälfte faltet exakt in den bekannten inneren AWI/2TP-Block;}\\[1mm]
\text{globaler Restblock auf }J_B:
?[O].
\end{array}}
\tag{DD.228}
\]

Dies ist noch keine globale \(B_1\to B_2\)-Rekurrenz.

**Stage-10A-Reviewstatus.** Die Wallidentität, alle acht unteren elf-Wort-Rows, der positive Durchgangsblock \(M_{B,1}\), die exakte Vorzeichenformel \(\gamma_{B,1}>0\) sowie die vier oberen Fold-Identitäten wurden separat adversarial geprüft und durch
`scripts/certify_sw1_delta_descent_stage10a.py`
mit Python/SymPy 1.14.0 reproduzierbar zertifiziert (PASS).

Zertifizierter Script-Blob:
`2b199ccbb193b83b89edc709c2563120caa426b5`.

Damit gilt ausschließlich für Stage 10A:
\[
\boxed{
\mathrm{Stage\ 10A}:
\text{AI-GREEN}
+
\text{independent GREEN (certificate)}
}
\]

Der globale Restquotient auf \(J_B\) bleibt ausdrücklich \(?[O]\).



## 14. Stage 10B — kombinierte Reflexionsgruppe und endliche Parameterorbits

Stage 10A zeigt, dass auf \(J_B\) die neue Reflexion
\[
r_B(s):=h_B-s
\tag{DD.229}
\]
mit der bereits vorhandenen AWI-Reflexion
\[
r_\Delta(s):=\Delta-s
\tag{DD.230}
\]
zusammentrifft.

### 14.1 Die Komposition ist eine feste Translation

Setze
\[
\boxed{
k_B:=h_B-\Delta=e-2\Delta>0.
}
\tag{DD.231}
\]

Dann
\[
\boxed{
r_\Delta\circ r_B(s)=s-k_B,
}
\tag{DD.232}
\]
und
\[
\boxed{
r_B\circ r_\Delta(s)=s+k_B.
}
\tag{DD.233}
\]

Die von \(r_\Delta,r_B\) erzeugte Parametergruppe ist damit die eindimensionale Diederstruktur
\[
s\longmapsto s+n k_B,
\qquad
s\longmapsto \Delta-s+n k_B,
\qquad
n\in\mathbb Z.
\tag{DD.234}
\]

### 14.2 Exakte Größenordnung des Translationsschritts

Für die festen Konstanten gilt
\[
\boxed{
0<k_B<\frac{\Delta}{2},
}
\tag{DD.235}
\]
und sogar
\[
\boxed{
2k_B<\Delta<3k_B.
}
\tag{DD.236}
\]

Die linke Ungleichung ist äquivalent zu
\[
\Delta-2k_B
=
6\Delta-a
=
g_6>0,
\tag{DD.237}
\]
also exakt dem bereits in Stage 7 zertifizierten positiven Terminalslack.

Die rechte Ungleichung
\[
3k_B-\Delta>0
\tag{DD.238}
\]
ist eine weitere feste Konstantenungleichung; sie wird im Stage-10B-Zertifikat exakt geprüft.

### 14.3 Uniforme Endlichkeit jedes kombinierten Orbits

Der gesamte SW1-Parameterstrip besitzt Länge
\[
\varepsilon-R<\varepsilon<\Delta<3k_B.
\tag{DD.239}
\]

Betrachte zunächst eine Translationsklasse
\[
\{s+n k_B:n\in\mathbb Z\}.
\]
Vier verschiedene Punkte dieser Klasse hätten Spannweite mindestens
\[
3k_B>\varepsilon-R,
\]
und können daher nicht sämtlich in \((R,\varepsilon)\) liegen.

Somit enthält jede Translationsklasse höchstens drei aktive Parameterpunkte.

Ein voller diederischer Orbit ist die Vereinigung von höchstens zwei solchen Klassen:
\[
\{s+n k_B\}
\cup
\{\Delta-s+n k_B\}.
\]

Daher gilt die uniforme Schranke
\[
\boxed{
\#\bigl(\mathcal O(s)\cap(R,\varepsilon)\bigr)\le6.
}
\tag{DD.240}
\]

### 14.4 Konsequenz für den globalen Stage-10-Rest

Die Überlagerung der beiden Reflexionsmechanismen kann somit **keine unendliche neue Parameterkaskade** erzeugen.

Nach Wahl einer messbaren Orbitfundamentalmenge zerfällt der globale Rest auf \(J_B\) in endliche physische Profilorbits mit höchstens sechs Parameterpunkten.

Auf jedem solchen Orbit müssen die nominalen Stage-10-Profile noch physisch quotientiert und die zugehörige endliche Kompressionsmatrix von \(I+A\) explizit aufgebaut werden.

Der nächste Schritt ist daher endlich-dimensional:
\[
\boxed{
\text{Stage 10C: Orbit-Quotient und endlicher Restblock für }|\mathcal O|\le6.
}
\tag{DD.241}
\]

**Firewall:** DD.240 beweist Endlichkeit der Parametergeometrie, aber noch nicht die Invertierbarkeit jedes vollständigen Stage-10C-Blocks und noch keine globale \(B_1\to B_2\)-Rekurrenz.

**Stage-10B-Reviewstatus.** Die beiden Reflexionskompositionen, der Translationsschritt \(k_B\), die exakten Ungleichungen \(2k_B<\Delta<3k_B\) und die uniforme Orbitabschätzung \(\#\mathcal O\le6\) wurden separat adversarial geprüft und durch
`scripts/certify_sw1_delta_descent_stage10b.py`
mit Python/SymPy 1.14.0 reproduzierbar zertifiziert (PASS).

Zertifizierter Script-Blob:
`f774ef96d0e7b02dcca06f1c5d8462207d6f3604`.

Damit gilt für Stage 10B:
\[
\boxed{
\mathrm{Stage\ 10B}:
\text{AI-GREEN}
+
\text{independent GREEN (certificate)}
}
\]

Der nächste offene Knoten bleibt Stage 10C: expliziter physischer Quotient je endlichem Orbittyp und Klassifikation der verbleibenden \(B_2\)-Kanäle.



## 15. Stage 10C — oberer \(h_B\)-Orbitquotient schließt ohne neuen \(B_2\)-Randkanal

Stage 10C behandelt ausschließlich die obere B-Wall-Kammer
\[
s\in J_B=(h_B-\varepsilon,\varepsilon).
\tag{DD.242}
\]

Setze wie zuvor
\[
u:=r_B(s)=h_B-s,
\qquad
t:=r_\Delta(s)=\Delta-s.
\tag{DD.243}
\]

Aus Stage 10A/10B gilt
\[
u\in J,
\qquad
t\in J,
\tag{DD.244}
\]
und der kombinierte Orbit von \(s\) unter \(r_B,r_\Delta\) besitzt höchstens sechs aktive Parameterpunkte.

### 15.1 Die beiden scheinbar externen Restkanäle sind orbitintern

Die obere Stage-10A-Resthälfte koppelt nur noch an
\[
C+s
\quad\text{und}\quad
B_2-s.
\]
Beide sind exakt keine neuen Profile:

\[
\boxed{
C+s=b-t.
}
\tag{DD.245}
\]

\[
\boxed{
B_2-s=B_1+t.
}
\tag{DD.246}
\]

Damit liegen beide Kanäle bereits in den Stage-9-/Stage-10-Profilfamilien am reflektierten Parameter
\[
t=r_\Delta(s),
\]
also im selben endlichen kombinierten Orbit.

### 15.2 Auch \(B_2+s\) ist bereits im inneren AWI-Fold enthalten

Der in der gefalteten \(F_0-s=a+u\)-Row auftretende Wort-11-Kanal ist
\[
B_2+s.
\]
Es gilt
\[
\boxed{
B_2+s
=
T+(s-k_B).
}
\tag{DD.247}
\]

Andererseits
\[
s-k_B
=
\Delta-u
=
r_\Delta(u).
\tag{DD.248}
\]

Da \(u\in J\), ist auch
\[
r_\Delta(u)\in J\subset(R,\varepsilon).
\tag{DD.249}
\]

Somit
\[
\boxed{
B_2+s=T+r_\Delta(u)
}
\tag{DD.250}
\]
und dieser Kanal ist exakt der \(T+\)-Partner im bereits zertifizierten Stage-4/AWI-\(10\times10\)-Block zum Parameterpaar
\[
\{u,\Delta-u\}.
\]

Insbesondere ist auch \(B_2+s\) **kein neuer externer y-Kanal**.

### 15.3 Endlicher physischer Masterraum

Sei \(\mathcal O\subset(R,\varepsilon)\) ein aktiver kombinierter Orbit aus Stage 10B.

Wir bilden den tatsächlichen physischen \(L^2\)-Raum \(\mathcal V_{\mathcal O}\) als den von folgenden bereits zertifizierten Profilräumen erzeugten Raum:

1. den Stage-9-B-Profilen aller \(q\in\mathcal O\);
2. den unteren Stage-10A-Durchgangsprofilen für diejenigen \(q\in\mathcal O\) mit
   \[
   q+\varepsilon<h_B;
   \]
3. den oberen Stage-10A-Restprofilen für
   \[
   q\in\mathcal O\cap J_B;
   \]
4. den zu \(r_B(q)\in J\) gehörigen Stage-4/AWI-Profilräumen;
5. den dadurch bereits enthaltenen erweiterten \(T\pm\)-Profilen aus Stage 7.

Physisch identische Profile werden **nicht** als getrennte Koordinaten gezählt; \(\mathcal V_{\mathcal O}\) ist der tatsächliche Unterraum im Hub-Hilbertraum, nicht eine formale direkte Summe nomineller Labels.

Wegen
\[
\#\mathcal O\le6
\]
und der endlichen Profilzahl jeder der fünf Bausteinfamilien ist \(\mathcal V_{\mathcal O}\) ein endlich erzeugter Profilraum.

### 15.4 Exhaustive y-Closure auf dem Orbit

Für jeden direkten Rowtyp, der in \(\mathcal V_{\mathcal O}\) verwendet wird, sind alle y-Echos bereits durch die Stages 4, 7, 9 und 10A exhaustiv klassifiziert.

Die einzigen Stage-10A-Kanäle, die vor dem Quotienten nominell außerhalb lagen, sind:

- \(C+s\), geschlossen durch DD.245;
- \(B_2-s\), geschlossen durch DD.246;
- \(B_2+s\), geschlossen durch DD.247–DD.250.

Daher erzeugt die Projektion des augmentierten Systems auf \(\mathcal V_{\mathcal O}\) **keinen weiteren y-Randkanal**.

Es bleibt exakt
\[
\boxed{
K_{\mathcal O}Y_{\mathcal O}
+
H_{\mathcal O}w
=
0,
}
\tag{DD.251}
\]
wobei
\[
K_{\mathcal O}
=
P_{\mathcal V_{\mathcal O}}
(I+A)
\big|_{\mathcal V_{\mathcal O}}.
\tag{DD.252}
\]

### 15.5 Uniforme Invertierbarkeit des Masterblocks

Da
\[
A=R_{T_0}^*R_{T_0}\ge0,
\]
gilt auf jedem \(\mathcal V_{\mathcal O}\)
\[
\boxed{
K_{\mathcal O}\ge I.
}
\tag{DD.253}
\]

Somit
\[
\boxed{
\|K_{\mathcal O}^{-1}\|\le1
}
\tag{DD.254}
\]
uniform in Orbittyp, Orbitgröße und SW1-Parametern.

Daher können sämtliche y-Profile des oberen Stage-10-Orbits eindeutig eliminiert werden:
\[
\boxed{
Y_{\mathcal O}
=
-K_{\mathcal O}^{-1}H_{\mathcal O}w.
}
\tag{DD.255}
\]

### 15.6 Oberer Stage-10-Zweig ist y-seitig terminal

Aus DD.245–DD.255 folgt

\[
\boxed{
s+\varepsilon>h_B
\Longrightarrow
\text{kein neuer }B_2\text{- oder sonstiger y-Randtyp.}
}
\tag{DD.256}
\]

Die gesamte obere B-Wall-Kammer fällt nach physischem Orbitquotienten in einen endlichen, uniform invertierbaren y-Schurblock zurück.

Damit ist die B-Zentrum-Propagation auf der oberen Stage-10-Kammer **y-seitig beendet**.

### 15.7 Was global noch offen bleibt

Unterhalb der Wall
\[
s+\varepsilon<h_B
\]
bleibt dagegen der in Stage 10A zertifizierte nichtverschwindende Durchgang
\[
\gamma_{B,1}>0
\]
zum echten nächsten Zentrum
\[
B_2=b+2\Delta.
\]

Daher ist der nächste globale Knoten nun eindeutig:

\[
\boxed{
\text{Stage 11: untere B-Wall-Kammer — direkte Analyse des Zentrums }B_2.
}
\tag{DD.257}
\]

**Firewall:** Stage 10C schließt nur die y-Geometrie der oberen B-Wall-Kammer. Der induzierte Annulusoperator auf \(w\) und die untere \(B_2\)-Propagation bleiben offen.

**Stage-10C-Reviewstatus.** Die drei entscheidenden Abschlussidentitäten
\[
C+s=b-(\Delta-s),\qquad
B_2-s=B_1+(\Delta-s),\qquad
B_2+s=T+(s-k_B)=T+r_\Delta(r_B(s))
\]
sowie die Verschachtelung \(J_B\subset J\) und die orbitinterne Parameterlage wurden separat adversarial geprüft und durch
`scripts/certify_sw1_delta_descent_stage10c.py`
mit Python/SymPy 1.14.0 reproduzierbar zertifiziert (PASS).

Zertifizierter Script-Blob:
`e38adc4130f56666a4b216ab93183de9a26ae88c`.

Die Invertierbarkeit des Orbit-Masterblocks folgt operatorisch aus
\[
P_{\mathcal V_\mathcal O}(I+A)|_{\mathcal V_\mathcal O}\ge I,
\]
nicht aus einer numerischen Matrixabschätzung.

Damit gilt für Stage 10C:
\[
\boxed{
\mathrm{Stage\ 10C}:
\text{AI-GREEN}
+
\text{independent GREEN (certificate)}
}
\]



## 16. Stage 11 — terminaler Abschluss der unteren \(B_2\)-Kammer

Nach Stage 10C bleibt nur noch die untere B-Wall-Kammer
\[
s+\varepsilon<h_B,
\]
in der Stage 10A den echten Durchgang
\[
B_1\longrightarrow B_2=b+2\Delta
\]
mit \(\gamma_{B,1}>0\) erzeugt.

Setze
\[
\boxed{
k_B:=e-2\Delta=T-B_2>0.
}
\tag{DD.258}
\]

Dann
\[
B_2=T-k_B.
\tag{DD.259}
\]

Die Lage der beiden Punkte \(B_2\pm s\) relativ zum erweiterten \(T\)-Strip wird vollständig durch
\[
s+\varepsilon
\quad\text{und}\quad
s+k_B
\]
bestimmt.

Bis auf die beiden Nullmengen-Walls
\[
s+\varepsilon=k_B,
\qquad
s+k_B=\varepsilon,
\tag{DD.260}
\]
zerfällt die untere Stage-10-Kammer in genau drei Fälle.

### 16.1 Fall I — beide \(B_2\)-Äste außerhalb des erweiterten T-Strips

Sei
\[
s+\varepsilon<k_B.
\tag{DD.261}
\]

Definiere
\[
E_2:=e-2\Delta=k_B,
\qquad
D_2:=d+2\Delta,
\qquad
F_2:=C-2\Delta,
\tag{DD.262}
\]
sowie
\[
F_1:=C-\Delta.
\tag{DD.263}
\]

Die direkten elf-Wort-Rows liefern exakt

\[
\boxed{
(Ay)(E_2+s)
=
-c_1y(B_2-s)+c_1y(E_2+s)+c_2y(F_2+s),
}
\tag{DD.264}
\]

\[
\boxed{
(Ay)(E_2-s)
=
-c_1y(B_2+s)+c_1y(E_2-s)+c_2y(F_2-s),
}
\tag{DD.265}
\]

\[
\boxed{
(Ay)(D_2+s)
=
-c_1y(F_2-s)+c_1y(D_2+s)+c_2y(B_2+s),
}
\tag{DD.266}
\]

\[
\boxed{
(Ay)(D_2-s)
=
-c_1y(F_2+s)+c_1y(D_2-s)+c_2y(B_2-s),
}
\tag{DD.267}
\]

\[
\boxed{
\begin{aligned}
(Ay)(B_2+s)
={}&
-c_1y(E_2-s)
+\alpha_b y(B_2+s)
+\beta_-y(F_2-s)\\
&+c_2y(D_2+s)
+\beta_b y(F_1-s),
\end{aligned}}
\tag{DD.268}
\]

\[
\boxed{
\begin{aligned}
(Ay)(B_2-s)
={}&
-c_1y(E_2+s)
+\alpha_b y(B_2-s)
+\beta_-y(F_2+s)\\
&+c_2y(D_2-s)
+\beta_b y(F_1+s),
\end{aligned}}
\tag{DD.269}
\]

\[
\boxed{
\begin{aligned}
(Ay)(F_2+s)
={}&
-c_1y(D_2-s)
+(c_1+c_5)y(F_2+s)\\
&+\beta_-y(B_2-s)
+c_2y(E_2+s),
\end{aligned}}
\tag{DD.270}
\]

\[
\boxed{
\begin{aligned}
(Ay)(F_2-s)
={}&
-c_1y(D_2+s)
+(c_1+c_5)y(F_2-s)\\
&+\beta_-y(B_2+s)
+c_2y(E_2-s).
\end{aligned}}
\tag{DD.271}
\]

Der Wort-11-Nachfolger
\[
B_3:=b+3\Delta
\tag{DD.272}
\]
ist hier vollständig horizon-tot. Denn
\[
B_3=T+g_3,
\qquad
g_3:=3\Delta-e,
\tag{DD.273}
\]
und
\[
g_3-k_B>0.
\tag{DD.274}
\]
Aus DD.261 folgt daher
\[
g_3-s>\varepsilon,
\]
also
\[
B_3-s>T_0
\]
und erst recht \(B_3+s>T_0\).

Für
\[
X_{B,2}
:=
(D_{E_2},D_{D_2},D_{B_2},D_{F_2})^T
\]
ergibt sich

\[
\boxed{
M_{B,2}X_{B,2}
+
c_{11}e_3D_{F_1}
+
W_{B,2}
=0,
}
\tag{DD.275}
\]
mit

\[
\boxed{
M_{B,2}
=
\begin{pmatrix}
1+c_1&0&c_1&c_2\\
0&1+c_1&c_2&c_1\\
c_1&c_2&1+\alpha_b&2c_2\\
c_2&c_1&2c_2&1+c_1+c_5
\end{pmatrix}>0.
}
\tag{DD.276}
\]

Es gibt in Fall I **keinen neuen \(B_3\)-Randkanal**.

### 16.2 Fall II — ein T-Fold und ein äußerer Companion

Sei
\[
s+\varepsilon>k_B,
\qquad
s+k_B>\varepsilon.
\tag{DD.277}
\]

Dann liegt
\[
B_2+s
=
T-(k_B-s)
\quad\text{oder}\quad
T+(s-k_B)
\tag{DD.278}
\]
mit
\[
|s-k_B|<\varepsilon.
\tag{DD.279}
\]
Also ist \(B_2+s\) ein erweiterter 2TP-Tail.

Für den anderen Ast setze
\[
q:=k_B+s.
\tag{DD.280}
\]
Dann
\[
q>\varepsilon,
\qquad
R<q<2\Delta,
\tag{DD.281}
\]
und
\[
\boxed{
B_2-s=T-q.
}
\tag{DD.282}
\]

Damit fällt \(B_2-s\) exakt in den bereits zertifizierten äußeren Stage-4-Companionblock zum Parameter \(q\).

Die beiden übrigen y-Kanäle dieses Companionblocks sind ebenfalls nicht neu:

\[
\boxed{
a+q=F_2+s,
}
\tag{DD.283}
\]

\[
\boxed{
2d+q=F_1+s.
}
\tag{DD.284}
\]

Somit erzeugt auch Fall II keinen neuen y-Randtyp.

### 16.3 Fall III — beide \(B_2\)-Äste sind erweiterte 2TP-Tails

Sei
\[
s+k_B<\varepsilon.
\tag{DD.285}
\]

Dann
\[
B_2-s=T-(k_B+s)
\tag{DD.286}
\]
mit
\[
0<k_B+s<\varepsilon.
\]

Außerdem
\[
B_2+s
=
T\pm|s-k_B|,
\tag{DD.287}
\]
und
\[
|s-k_B|<k_B+s<\varepsilon.
\tag{DD.288}
\]

Damit liegen **beide** \(B_2\)-Äste im erweiterten lokalen 2TP-Pivot aus Stage 7.

Auch Fall III erzeugt keinen neuen y-Randtyp.

### 16.4 Simultaner physischer Masterblock

In Fall I koppelt DD.275 zurück an die bereits vorhandene (F_1)-Koordinate aus Stage 10A. Deshalb wird **nicht** aus der getrennten Positivität von (M_{B,1}) und (M_{B,2}) auf eine sequenzielle Invertierbarkeit geschlossen.

Stattdessen sei (mathcal V_{11}) der tatsächliche physische (L^2)-Raum, der von den Stage-10A- und Stage-11-Profilen des jeweiligen endlichen Parametersatzes erzeugt wird, nach Identifikation physisch gleicher Profile und unter Hinzunahme der in Fall II/III bereits zertifizierten Stage-4-/2TP-Profilräume.

Nach DD.264–DD.288 gibt es in keinem der drei Fälle einen y-Kanal außerhalb dieses endlichen Raums:
- Fall I: (B_3) ist horizon-tot;
- Fall II: (B_2+s) ist 2TP-intern und (B_2-s) liegt im Stage-4-Companionblock;
- Fall III: beide (B_2)-Äste sind 2TP-intern.

Daher ist der gekoppelte y-Operator exakt die Kompression
[
oxed{
K_{11}
=
P_{mathcal V_{11}}(I+A)|_{mathcal V_{11}}
ge I.
}
	ag{DD.288a}
]

Somit
[
oxed{
|K_{11}^{-1}|le1.
}
	ag{DD.288b}
]

Die gesamte gekoppelte Stage-10A/11-y-Familie kann daher simultan und eindeutig in Abhängigkeit von (w) eliminiert werden.

### 16.5 Exhaustivität und terminaler B-Abschluss

Außerhalb der Nullmengen-Walls DD.260 sind die drei Fälle exhaustiv:

- entweder \(s+\varepsilon<k_B\) — Fall I;
- oder \(s+\varepsilon>k_B\), und dann entweder
  \(s+k_B>\varepsilon\) — Fall II,
  oder \(s+k_B<\varepsilon\) — Fall III.

In jedem Fall ist die \(B_2\)-Propagation y-seitig terminal:

\[
\boxed{
\text{kein neuer }B_3\text{- oder sonstiger y-Zentrumstyp entsteht.}
}
\tag{DD.289}
\]

Zusammen mit Stage 10C folgt daher für die bisher untersuchte äußere Parameterzone (s\in(R,\varepsilon)):

\[
\boxed{
\text{Die gesamte äußere B-Zentrum-Hierarchie ist endlich geschlossen.}
}
\tag{DD.290}
\]

Kombiniert mit der Stage-7-y-shell-Closure ist damit die **äußere y-Geometrie für (s\in(R,\varepsilon))** endlich eliminierbar.

### 16.6 Verbleibender innerer KNF-Sample-Scope

DD.290 schließt noch **nicht automatisch** die fünf freien KNF-Samplekoordinaten
\[
y(a+u),\quad y(b-u),\quad y(b+u),\quad y(T-u),\quad y(T+u),
\qquad 0<u<R,
\]
aus KNF.17–KNF.21.

Die zweite augmentierte Gleichung ist durch die Wahl (y\in\mathcal K_R) bereits in KNF eingebaut; der linke (a-u)-Branch wird durch KNF.11 rekonstruiert. Bevor ein reiner Annulusoperator behauptet werden darf, muss aber noch gezeigt werden, dass die **erste** augmentierte Gleichung auch diese fünf freien inneren Samplekoordinaten durch dieselbe endliche Row-Geometrie kontrolliert.

Wegen
\[
u+\varepsilon<R+\varepsilon<\Delta
\]
liegt der gesamte innere Samplebereich strikt außerhalb aller bisherigen AWI-Überlappkammern. Der nächste Schritt ist daher:
\[
\boxed{
\text{Stage 12: innerer KNF-Sample-Abschluss für }0<u<R.
}
\tag{DD.290a}
\]

Erst **nach** Stage 12 darf der nächste Knoten als induzierter Annulusoperator formuliert werden:

\[
\boxed{
\mathcal L_{\mathrm{ann}}w=0,
}
\tag{DD.291}
\]
der durch Schur-Elimination sämtlicher nun endlich geschlossener y-Blöcke entsteht.

Zu beweisen bleibt:

\[
\boxed{
\ker\mathcal L_{\mathrm{ann}}=\{0\}\ ?
}
\tag{DD.292}
\]

**Firewall:** DD.290 ist eine endliche **äußere** y-Geometrie-/Eliminationsaussage auf (s\in(R,\varepsilon)). Der innere KNF-Samplebereich (0<u<R) bleibt bis Stage 12 offen. Insbesondere beweist Stage 11 noch nicht DD.292, kein HT-RED, kein A0 und keine Aussage über \(\ker\Gamma_I\).


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
