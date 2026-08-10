# P11-C1z-B2-C5d — Even-Core-Tailzerfall, Gamma-Metrik-Limes und Mosco-Konvergenz

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C5d]`  
**Vorgänger:** C1z-B2-C5c  
**Schnittstellen:** C1z-B/B1; C1z-B2-C2/C3/C4/C5/C5a/C5b/C5c; P03-Haar-L2-Firewall

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5d]
\quad
\checkmark[K/M]_{\rm part}
+\checkmark[M]_{\rm pos,even\text{-}core\text{-}tail}
+\checkmark[M]_{\rm pos,even\text{-}form\text{-}Cauchy}
+\checkmark[M]_{\rm pos,even\text{-}Mosco}
}
\]

mit den neuen Hauptbefunden

\[
\boxed{
\sigma_T(J_{R,T}f)=O_{R,f}(T^{-1})
\qquad
(f\in C_c^\infty((-R,R)),\ f\text{ gerade}),
}
\tag{C1zB2C5d.1}
\]

also nicht nur Punktbeschränktheit, sondern **Verschwinden** des vollständigen Hub-Feshbach-Schurterms auf dem glatten geraden Testcore,

\[
\boxed{
q_T^X(J_{R,T}f,J_{R,T}g)
\longrightarrow
q_{\Gamma,R}(f,g)
}
\tag{C1zB2C5d.2}
\]

für alle glatten geraden Tests `f,g`, und daraus auf der festen geraden Graphhälfte

\[
\boxed{
\mathfrak q_{R,T}^{+}
\xrightarrow[T\to\infty]{\rm Mosco}
q_{\Gamma,R}^{+}.
}
\tag{C1zB2C5d.3}
\]

Damit konvergieren die zugehörigen Zukunftsmetrikoperatoren auf dem geraden Sektor im starken Resolventensinn zur durch die reine Gammaform induzierten positiven invertierbaren Grenzmetrik.

**Firewall:** Dieser Knoten beweist noch nicht

1. Normkonvergenz von `G_{R,T}^+`;
2. starke Operatorkonvergenz von `G_{R,T}^+` selbst;
3. starke Konvergenz der positiven Quadratwurzeln `G_{R,T}^{1/2}`;
4. den Cauchy-Limes von `W_{R,S,+}^{[T]}`;
5. irgendeine Aussage über den ungeraden Boundary-Jet-Transport;
6. Objekt X oder RH.

Der neue positive Endpunkt ist ein **Mosco-/Resolventenlimes der geraden Zukunftsmetrik zur Gamma-Metrik**, nicht bereits der globale isometrische Transport.

---

# 0. Urteil und Korrektur der C5c-Zertifikatswahl

C5c bewies für jedes feste gerade

\[
f\in C_c^\infty((-R,R))
\]

eine `T`-uniforme primitive Observability-Ungleichung. Das diskrete Future-Prime-Zertifikat für den wachsenden Primblock hatte sogar Kosten

\[
O_f(T^{-1})+O_f(e^{-cT}).
\]

Ein `T`-unabhängiger konstanter Zertifikatsanteil blieb in C5c nur deshalb stehen, weil ein **fester endlicher Small-Prime-Block absichtlich same-prime behandelt** wurde.

C5d zeigt:

\[
\boxed{
\text{dieser feste Small-Prime-Anteil ist nicht intrinsisch.}
}
\]

Jeder feste kompakt getragene ungerade Source-Vektor kann selbst durch Future-Primes der Skala `q\asymp e^T` gescreent werden, und zwar mit exponentiell verschwindenden Zertifikatskosten.

Dasselbe gilt für den gesamten höheren Prime-Power-Hub `k\ge2`, weil dessen verschobene glatte Source-Profile eine uniform summierbare exponentiell gewichtete `H^1`-Norm besitzen.

Damit kann das C5c-Zertifikat so umgebaut werden, dass **kein konstanter Tail mehr übrig bleibt**.

---

# 1. Verbindliche Feshbach-Dualform

Für das Terminallevel `T` schreibe

\[
A_T:=I+R_T^*R_T,
\qquad
h_{T,f}:=H_T^*J_{R,T}f.
\]

Dann

\[
\boxed{
\sigma_T(J_{R,T}f)
=
\langle h_{T,f},A_T^{-1}h_{T,f}\rangle.
}
\tag{C1zB2C5d.4}
\]

Für jeden beschränkten Analyseoperator `R:H\to Y` gilt nach C5c

\[
\boxed{
\langle h,(I+R^*R)^{-1}h\rangle
=
\inf_{y\in Y}
\bigl(\|h-R^*y\|^2+\|y\|^2\bigr).
}
\tag{C1zB2C5d.5}
\]

Da

\[
R_T^*R_T\ge (R_T^{(1)})^*R_T^{(1)},
\]

genügt weiterhin ein Zertifikat allein im **primitiven Restzielraum**:

Falls

\[
h_{T,f}=(R_T^{(1)})^*Y_T+Z_T,
\]

dann

\[
\boxed{
\sigma_T(J_{R,T}f)
\le
\|Y_T\|^2+\|Z_T\|^2.
}
\tag{C1zB2C5d.6}
\]

C5d konstruiert `Y_T,Z_T` nun mit rechter Seite `O_f(1/T)`.

---

# 2. Erweiterte Boundary-Koordinate

Sei

\[
e\in\mathscr H_T^-,
\qquad e(-x)=-e(x).
\]

Es ist für C5d zweckmäßig, die Boundary-Koordinate auf die ganze reflektierte Strecke zu erweitern:

\[
\boxed{
b_T(t):=e(T-t),\qquad 0<t<2T.}
\tag{C1zB2C5d.7}
\]

Dann gilt automatisch

\[
\boxed{
b_T(2T-t)=-b_T(t).}
\tag{C1zB2C5d.8}
\]

Sei `q` primitiv und

\[
a_q=\tfrac12\log q,
\qquad
r_q=T-a_q.
\]

Für `0\le u\le r_q` setze

\[
t=r_q-u,
\qquad
s=r_q+u.
\]

Dann

\[
T-t=a_q+u,
\qquad
T-s=a_q-u.
\]

Mit der Ungeradheit von `e` folgt für **alle** `u\le r_q`, unabhängig davon, ob `u<a_q` oder `u>a_q`,

\[
\boxed{
D_{\log q}E_Te(u)
=b_T(t)+b_T(s),
\qquad t+s=2r_q.
}
\tag{C1zB2C5d.9}
\]

Die signless-reflection-edge-Geometrie aus C5c ist also nicht auf `r_q\le T/2` beschränkt. C5c benutzte diesen Scope nur als technische Vereinfachung.

Für C5d werden weiterhin ausschließlich Primzahlen mit

\[
a_q\ge T/2-O(1),
\]

also `q\asymp e^T` oder größer, benötigt.

---

# 3. Generisches Future-Screening-Lemma für einen glatten ungeraden Source-Vektor

Wir isolieren die Erweiterung von C5c, die den festen Small-Prime-Block beseitigt.

## Lemma C5d.1 — compact/interior future certificate

Sei für jedes `T` ein glatter ungerader Source-Vektor

\[
g_T\in C^1((-T,T)),
\qquad g_T(-x)=-g_T(x).
\]

Definiere die positive-Halbraum-Norm

\[
\boxed{
\mathcal W_T(g_T)
:=
\int_0^T e^{-x/2}
\bigl(|g_T(x)|^2+|g_T'(x)|^2\bigr)\,dx
+
\left|\int_0^T g_T(x)\,dx\right|^2.
}
\tag{C1zB2C5d.10}
\]

Falls

\[
\sup_T\mathcal W_T(g_T)<\infty,
\]

dann existieren primitive Future-Prime-Zertifikate

\[
Y_T^{g}\in\mathscr Y_{T,\rm prim}^0
\]

und Source-Reste `Z_T^g` mit

\[
\boxed{
g_T=(R_T^{(1)})^*Y_T^g+Z_T^g}
\tag{C1zB2C5d.11}
\]

und

\[
\boxed{
\|Y_T^g\|^2
\le
C_g e^{-T/2},
\qquad
\|Z_T^g\|_2
\le
C_g e^{-cT}.
}
\tag{C1zB2C5d.12}
\]

für ein `c>0`.

### Beweisstruktur

Auf der positiven Source-Hälfte gilt

\[
\langle g_T,e\rangle
=2\int_0^T g_T(x)e(x)dx
=
\int_0^T k_T^g(t)b_T(t)dt
\]

mit

\[
\boxed{k_T^g(t):=2g_T(T-t).}
\tag{C1zB2C5d.13}
\]

Verwende dieselbe feste Anchor-Dichte `alpha` aus C5c. Die signless triangle identity gilt ohne Änderung:

\[
b(t)
=
\int\alpha(s)[b(t)+b(s)]ds
-
\frac12\iint\alpha(s)\alpha(s')[b(s)+b(s')]dsds'.
\]

Damit wird `k_T^g` kontinuierlich exakt aus signless reflection edges dargestellt.

Für ein Target-Anchor-Paar `(t,s)` ist

\[
r=\frac{t+s}{2}.
\]

Der kontinuierliche primitive Restmaßfaktor ist wie in C5c

\[
m_T(r)=2e^{T-r}.
\]

Daher besitzt das kontinuierliche Dualzertifikat dieselbe Normabschätzung

\[
\|Y_{T,g}^{\rm cont}\|^2
\le
C_\alpha e^{-T}
\left(
\int_0^T e^{t/2}|k_T^g(t)|^2dt
+
|K_T^g|^2
\right),
\]

wobei

\[
K_T^g=\int_0^T k_T^g(t)dt.
\]

Mit `x=T-t`:

\[
e^{-T}
\int_0^T e^{t/2}|k_T^g(t)|^2dt
=
4e^{-T/2}
\int_0^T e^{-x/2}|g_T(x)|^2dx.
\]

Der Ableitungsterm für die Prime-Zellquadratur wird analog durch

\[
e^{-T/2}
\int_0^T e^{-x/2}|g_T'(x)|^2dx
\]

kontrolliert.

Der Anchor-Anchor-Term ist wegen `r=O(1)` noch kleiner; seine Kosten tragen einen Faktor `e^{-T}`.

Damit

\[
\boxed{
\|Y_{T,g}^{\rm cont}\|^2
\le
C\,e^{-T/2}\mathcal W_T(g_T).
}
\tag{C1zB2C5d.14}
\]

Für die Diskretisierung liegen die benötigten Prime-Mittelpunkte bei

\[
r=\frac{t+s}{2}\le\frac{T+O(1)}2,
\]

also

\[
a_q=T-r\ge T/2-O(1).
\]

Die in C5c bereits importierte unbedingte Short-interval-PNT auf `x^{3/5}` liefert deshalb in allen verwendeten Zellen genügend primitive Restmasse. Die exakt massennormalisierte Quadratur

\[
\lambda_q^{(I)}=|I|\frac{w_q}{W_I}
\]

wird unverändert verwendet.

Da `g_T` und `g_T'` durch `\mathcal W_T` kontrolliert werden und die Zellweiten auf der Skala `q\asymp e^T` exponentiell klein sind, ist der Source-Quadraturrest `O(e^{-cT})`.

Dies gibt (C1zB2C5d.11)--(C1zB2C5d.12). `□`

### Spezialfall

Für einen **festen** glatten kompakt getragenen ungeraden Vektor `g` gilt automatisch

\[
\sup_T\mathcal W_T(E_T^*g)<\infty.
\]

Daher kostet seine Future-Prime-Realisierung nur

\[
\boxed{O_g(e^{-T/2}).}
\tag{C1zB2C5d.15}
\]

Dies ersetzt den konstanten Same-Prime-Small-Block aus C5c.

---

# 4. Der primitive Small-Prime-Block verschwindet ebenfalls

C5c fixierte

\[
\mathcal P_{\rm small}
=\{p:\tfrac12\log p<a_*\}.
\]

Für `T` groß genug ist

\[
\boxed{
 g_f^{\rm small}
:=
\sum_{p\in\mathcal P_{\rm small}}
 c_pD_{\log p}^*f
}
\tag{C1zB2C5d.16}
\]

ein `T`-unabhängiger glatter kompakt getragener **ungerader** Source-Vektor.

Nach Lemma C5d.1 existiert daher ein Future-Prime-Zertifikat mit

\[
\boxed{
\|Y_{T}^{\rm small}\|^2
=O_f(e^{-T/2}),
\qquad
\|Z_T^{\rm small}\|_2=O_f(e^{-cT}).
}
\tag{C1zB2C5d.17}
\]

Der konstante Term aus `(C1zB2C5c.5)` war somit ausschließlich eine **nichtoptimale Zertifikatswahl**, kein echter terminaler Rest.

---

# 5. Der wachsende primitive Block bleibt `O(1/T)`

Für

\[
\mathcal P_{\rm grow}(T)
=\{p:a_*\le\tfrac12\log p\le T\}
\]

hat C5c bereits ein diskretes Future-Prime-Zertifikat konstruiert mit

\[
\boxed{
\|Y_T^{\rm grow}\|^2
\le
\frac{C_f}{T}+O_f(e^{-cT})
}
\tag{C1zB2C5d.18}
\]

und

\[
\boxed{
\|Z_T^{\rm grow}\|_2
\le
C_fe^{-cT}.
}
\tag{C1zB2C5d.19}
\]

Dies ist der dominante Tail des geraden primitiven Hubs.

Zusammen mit §4 folgt für den **vollständigen primitiven Hubvektor**

\[
h_{T,f}^{(1)}
=(H_T^{(1)})^*J_{R,T}f
\]

ein Zertifikat

\[
h_{T,f}^{(1)}
=(R_T^{(1)})^*Y_T^{(1)}+Z_T^{(1)}
\]

mit

\[
\boxed{
\|Y_T^{(1)}\|^2+\|Z_T^{(1)}\|^2
\le
\frac{C_f}{T}+O_f(e^{-cT}).
}
\tag{C1zB2C5d.20}
\]

Beim Addieren der Zertifikate wird keine Orthogonalität behauptet; die elementare Abschätzung

\[
\|u+v\|^2\le2\|u\|^2+2\|v\|^2
\]

reicht aus.

---

# 6. Höhere Prime-Powers besitzen uniform gewichtete Source-Regularität

Es bleibt

\[
h_{T,f}^{(\ge2)}
:=(H_T^{(\ge2)})^*J_{R,T}f.
\]

Für `n=p^k`, `k\ge2`, ist der Hubkoeffizient

\[
b_{p,k}
:=\sqrt{\log p}\,p^{-3k/4}
\]

und der halbe Translationsabstand

\[
a_{p,k}=\frac{k\log p}{2}.
\]

Setze

\[
\|g\|_{H^1_{-}}^2
:=
\int_0^\infty e^{-x/2}
\bigl(|g(x)|^2+|g'(x)|^2\bigr)dx.
\]

Für eine um `a` verschobene Kopie eines festen kompakten Tests gilt

\[
\|\tau_a f\|_{H^1_-}
\le
C_f e^{-a/4}.
\]

Daher, mit der Dreiecksungleichung im gewichteten Hilbertraum,

\[
\|h_{T,f}^{(\ge2)}\|_{H^1_-}
\le
C_f
\sum_p\sum_{k\ge2}
\sqrt{\log p}\,p^{-3k/4}p^{-k/8}.
\]

Die Reihe ist

\[
\boxed{
\sum_p\sum_{k\ge2}
\sqrt{\log p}\,p^{-7k/8}<\infty,
}
\tag{C1zB2C5d.21}
\]

weil bereits der `k=2`-Term wie

\[
\sqrt{\log p}\,p^{-7/4}
\]

summierbar ist.

Dasselbe gilt für die benötigte `L^1`-/Anchor-Momentkontrolle, da die ursprünglichen `k\ge2`-Hubkoeffizienten absolut summierbar sind.

Somit

\[
\boxed{
\sup_T
\mathcal W_T(h_{T,f}^{(\ge2)})<\infty.
}
\tag{C1zB2C5d.22}
\]

und Lemma C5d.1 liefert ein primitives Future-Zertifikat

\[
h_{T,f}^{(\ge2)}
=(R_T^{(1)})^*Y_T^{(\ge2)}+Z_T^{(\ge2)}
\]

mit

\[
\boxed{
\|Y_T^{(\ge2)}\|^2
=O_f(e^{-T/2}),
\qquad
\|Z_T^{(\ge2)}\|_2=O_f(e^{-cT}).
}
\tag{C1zB2C5d.23}
\]

**Wichtig:** Der höhere Prime-Power-Hub wird hier nicht mit seinen eigenen Restkanälen gescreent. Er wird durch denselben bereits kanonischen **primitiven Future-Rest** dual realisiert. Es wird kein neuer Regulator eingeführt.

---

# 7. Hauptsatz C5d.1 — vollständiger gerader Schurterm zerfällt wie `1/T`

Addiere die drei Zertifikate

1. primitiver Small-Prime-Block;
2. primitiver wachsender Block;
3. höherer Prime-Power-Hub.

Es existieren

\[
Y_{T,f}\in\mathscr Y_{T,\rm prim}^0,
\qquad
Z_{T,f}\in\mathscr H_T^-
\]

mit

\[
\boxed{
 h_{T,f}
=(R_T^{(1)})^*Y_{T,f}+Z_{T,f}
}
\tag{C1zB2C5d.24}
\]

und

\[
\boxed{
\|Y_{T,f}\|^2+\|Z_{T,f}\|^2
\le
\frac{C_{R,f}}{T}
+C_{R,f}e^{-cT}.
}
\tag{C1zB2C5d.25}
\]

Setze dies in die Feshbach-Dualform ein. Da der vollständige Rest mindestens so stark screenet wie sein primitiver Teil,

\[
\boxed{
0\le
\sigma_T(J_{R,T}f)
\le
\frac{C_{R,f}}{T}+C_{R,f}e^{-cT}.
}
\tag{C1zB2C5d.26}
\]

Also

\[
\boxed{
\sigma_T(J_{R,T}f)
\longrightarrow0
\qquad(T\to\infty)
}
\tag{C1zB2C5d.27}
\]

für jeden festen glatten geraden Test.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,even\text{-}core\text{-}tail}.}
\]

Dies ist strikt stärker als die C5c-Punktbeschränktheit.

---

# 8. Bilineare Schurform verschwindet ebenfalls

Definiere die positive sesquilineare Schurform

\[
\boxed{
\Sigma_T(f,g)
:=
\langle A_T^{-1/2}h_{T,f},
A_T^{-1/2}h_{T,g}\rangle.
}
\tag{C1zB2C5d.28}
\]

Dann

\[
\Sigma_T(f,f)=\sigma_T(J_{R,T}f).
\]

Cauchy--Schwarz liefert

\[
|\Sigma_T(f,g)|^2
\le
\Sigma_T(f,f)\Sigma_T(g,g).
\]

Mit (C1zB2C5d.26):

\[
\boxed{
|\Sigma_T(f,g)|
\le
\frac{C_{R,f,g}}{T}
+O_{f,g}(e^{-cT})
}
\tag{C1zB2C5d.29}
\]

für feste glatte gerade `f,g`.

Da der Gammaanteil unter Nullfortsetzung exakt invariant ist,

\[
q_{\Gamma,T}(J_{R,T}f,J_{R,T}g)
=q_{\Gamma,R}(f,g),
\]

folgt

\[
\boxed{
q_T^X(J_{R,T}f,J_{R,T}g)
=
q_{\Gamma,R}(f,g)+\Sigma_T(f,g)
\longrightarrow
q_{\Gamma,R}(f,g).
}
\tag{C1zB2C5d.30}
\]

Insbesondere ist für `U,T\to\infty`

\[
\boxed{
\left|
q_U^X(J_{R,U}f,J_{R,U}g)
-q_T^X(J_{R,T}f,J_{R,T}g)
\right|
\le
C_{R,f,g}
\left(\frac1T+\frac1U\right)
+o(1).
}
\tag{C1zB2C5d.31}
\]

Dies ist der **intrinsische terminale Cauchy-Satz auf dem glatten geraden Formcore**.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,even\text{-}form\text{-}Cauchy}.}
\]

Die in C5c vorgeschlagene Differenzform

\[
h_{U,f}-h_{T,f}=R^*y_{T,U}+z_{T,U}
\]

ist damit nicht mehr notwendig, um Tail-Stabilität der relevanten Feshbachenergie zu beweisen. Die stärkere intrinsische Aussage ist, dass **jeder einzelne Terminal-Schurterm selbst gegen null geht**.

---

# 9. Die natürliche Grenzmetrik ist die reine Gamma-Metrik

Fixiere nun ein altes Level `R` und arbeite auf dem geraden Graphhilbertraum

\[
\mathcal K_{X,R}^{+}.
\]

Sein natives Skalarprodukt sei

\[
\langle\cdot,\cdot\rangle_{X,R},
\qquad
\|f\|_{X,R}^2=q_R^X(f).
\]

Auf diesem festen Hilbertraum definiere die Gammaform

\[
\gamma_R(f,g):=q_{\Gamma,R}(f,g).
\]

Aus C1z-B2-C gilt auf Level `R`

\[
q_{\Gamma,R}(f)
\le
q_R^X(f)
\le
(1+\|H_R\|^2)q_{\Gamma,R}(f).
\]

Daher ist `gamma_R` ein **beschränktes und koerzives** Skalarprodukt bezüglich der nativen `X`-Norm:

\[
\boxed{
\frac1{1+\|H_R\|^2}\|f\|_{X,R}^2
\le
\gamma_R(f,f)
\le
\|f\|_{X,R}^2.
}
\tag{C1zB2C5d.32}
\]

Nach Riesz existiert somit ein eindeutiger beschränkter positiver invertierbarer Operator

\[
\boxed{
\Gamma_R^+\in\mathcal B(\mathcal K_{X,R}^+)
}
\tag{C1zB2C5d.33}
\]

mit

\[
\boxed{
\langle\Gamma_R^+f,g\rangle_{X,R}
=q_{\Gamma,R}(f,g).
}
\tag{C1zB2C5d.34}
\]

und

\[
\boxed{
\frac1{1+\|H_R\|^2}I
\le
\Gamma_R^+
\le I.
}
\tag{C1zB2C5d.35}
\]

Die gerade Terminalmetrik hat also erstmals einen **kanonischen expliziten Grenzkandidaten**: nicht einen neu gewählten Counterterm, sondern schlicht die bereits vorhandene source-windowed Gamma-Geometrie.

---

# 10. Zukunftsformen auf dem festen alten Graphraum

Für `T>R` definiere

\[
\boxed{
\mathfrak q_{R,T}^{+}[f]
:=
\langle G_{R,T}f,f\rangle_{X,R}
=
q_T^X(J_{R,T}f),
\qquad
f\in\mathcal K_{X,R}^{+}.
}
\tag{C1zB2C5d.36}
\]

Alle diese Formen sind für festes `T` beschränkt und positiv auf dem ganzen Hilbertraum `K_{X,R}^+`.

Außerdem gilt für alle `f`

\[
\boxed{
\mathfrak q_{R,T}^{+}[f]
\ge
q_{\Gamma,R}(f)
=
\langle\Gamma_R^+f,f\rangle_{X,R}.
}
\tag{C1zB2C5d.37}
\]

Denn der Schurterm ist positiv.

Auf dem glatten geraden Core

\[
\mathcal C_R^+
:=C_c^\infty((-R,R))\cap\mathcal K_{X,R}^+
\]

folgt aus §7

\[
\boxed{
\mathfrak q_{R,T}^{+}[f]
\longrightarrow
q_{\Gamma,R}(f)
\qquad(f\in\mathcal C_R^+).
}
\tag{C1zB2C5d.38}
\]

---

# 11. Hauptsatz C5d.2 — Mosco-Konvergenz auf der geraden Graphhälfte

Wir benutzen, dass `C_R^+` ein dichter Formcore in `K_{X,R}^+` ist.

## Mosco-Liminf

Sei

\[
f_T\rightharpoonup f
\quad\text{schwach in }\mathcal K_{X,R}^{+}.
\]

Aus (C1zB2C5d.37):

\[
\mathfrak q_{R,T}^{+}[f_T]
\ge
q_{\Gamma,R}(f_T).
\]

Da `Gamma_R^+` beschränkt positiv ist, ist

\[
f\mapsto q_{\Gamma,R}(f)
=\| (\Gamma_R^+)^{1/2}f\|_{X,R}^2
\]

schwach unterhalbstetig. Daher

\[
\boxed{
\liminf_{T\to\infty}
\mathfrak q_{R,T}^{+}[f_T]
\ge
q_{\Gamma,R}(f).
}
\tag{C1zB2C5d.39}
\]

## Mosco-Limsup / Recovery sequence

Sei `f\in K_{X,R}^+`. Wähle

\[
f_n\in\mathcal C_R^+,
\qquad
f_n\to f
\quad\text{in }\|\cdot\|_{X,R}.
\]

Dann wegen der Beschränktheit von `Gamma_R^+`

\[
q_{\Gamma,R}(f_n)\to q_{\Gamma,R}(f).
\]

Für jedes feste `n` liefert (C1zB2C5d.38) ein `T_n` mit

\[
T\ge T_n
\Longrightarrow
\mathfrak q_{R,T}^{+}[f_n]
\le
q_{\Gamma,R}(f_n)+\frac1n.
\]

Wähle `T_n` streng wachsend und definiere diagonal

\[
f_T:=f_n
\qquad(T_n\le T<T_{n+1}).
\]

Dann

\[
f_T\to f
\]

stark und

\[
\boxed{
\limsup_{T\to\infty}
\mathfrak q_{R,T}^{+}[f_T]
\le
q_{\Gamma,R}(f).
}
\tag{C1zB2C5d.40}
\]

Damit ist die Mosco-Konvergenz bewiesen:

\[
\boxed{
\mathfrak q_{R,T}^{+}
\overset{M}{\longrightarrow}
q_{\Gamma,R}^{+}.
}
\tag{C1zB2C5d.41}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,even\text{-}Mosco}.}
\]

---

# 12. Operatorfolgen: starker Resolventenlimes und negative Potenzen

Der zu `mathfrak q_{R,T}^+` gehörige positive Operator auf dem festen Hilbertraum `K_{X,R}^+` ist genau

\[
G_{R,T}^+.
\]

Der Grenzoperator ist `Gamma_R^+`.

Aus Mosco-Konvergenz folgt der starke Resolventenlimes

\[
\boxed{
G_{R,T}^+
\longrightarrow
\Gamma_R^+
\qquad\text{im starken Resolventensinn}.
}
\tag{C1zB2C5d.42}
\]

C1/C2 liefern die `T`-unabhängige Untergrenze

\[
G_{R,T}^+
\ge
c_RI,
\qquad
c_R:=\frac1{1+\|H_R\|^2}>0.
\]

Nach (C1zB2C5d.35) gilt dieselbe Untergrenze auch für `Gamma_R^+`.

Daher können bounded continuous functions auf `[c_R,\infty)` angewandt werden. Insbesondere

\[
\boxed{
(G_{R,T}^+)^{-1}
\longrightarrow
(\Gamma_R^+)^{-1}
\quad\text{stark},
}
\tag{C1zB2C5d.43}
\]

und

\[
\boxed{
(G_{R,T}^+)^{-1/2}
\longrightarrow
(\Gamma_R^+)^{-1/2}
\quad\text{stark}.
}
\tag{C1zB2C5d.44}
\]

Dies ist für den späteren Terminal-Gauge-Limes ein wesentlicher neuer positiver Input.

**Firewall:** Für die positive Quadratwurzel `x\mapsto\sqrt x` ist die Funktion auf `[c_R,\infty)` unbeschränkt. Aus starkem Resolventenlimes allein folgt daher nicht automatisch

\[
(G_{R,T}^+)^{1/2}\to(\Gamma_R^+)^{1/2}
\]

stark auf dem ganzen Hilbertraum.

Genau dort sitzt jetzt der verbleibende gerade Transportengpass.

---

# 13. Was aus dem ursprünglich vorgeschlagenen Differenz-Dualzertifikat geworden ist

C5c schlug als nächste Zielgleichung schematisch vor

\[
h_{U,f}-h_{T,f}
=R^*y_{T,U}+z_{T,U},
\qquad
\|y_{T,U}\|^2+\|z_{T,U}\|^2\to0.
\]

Beim Vergleich verschiedener Terminallevel leben jedoch

- die Source-Hilberträume,
- die Restzielräume,
- die source-windowed Projektoren

zunächst in verschiedenen endlichen Geometrien. Eine solche Gleichung benötigt daher zusätzliche Einbettungsnotation und ist nicht der kanonischste Weg.

C5d erhält eine stärkere, intrinsische Aussage ohne diesen Typisierungsballast:

\[
\boxed{
\|A_T^{-1/2}h_{T,f}\|^2
=\sigma_T(J_{R,T}f)
\longrightarrow0.
}
\tag{C1zB2C5d.45}
\]

Damit folgt die Cauchy-Eigenschaft der zurückgezogenen **metrischen Formen** unmittelbar, ohne `h_U-h_T` in einen künstlich gemeinsamen Restzielraum zu zwingen.

Der richtige verbleibende Vergleich ist nun auf der bereits gemeinsamen alten Graphhälfte `K_{X,R}^+` formuliert und lautet

\[
G_{R,T}^+\overset{M/s.r.}{\longrightarrow}\Gamma_R^+.
\]

---

# 14. Konsequenz für den geraden relativen Transport

Für `R<S<T` ist

\[
W_{R,S,+}^{[T]}
=
(G_{S,T}^+)^{1/2}
J_{R,S}^+
(G_{R,T}^+)^{-1/2}.
\]

C5d liefert jetzt bereits die **Source-Hälfte** des terminalen Gauge-Limes:

\[
(G_{R,T}^+)^{-1/2}
\to
(\Gamma_R^+)^{-1/2}
\quad\text{stark}.
\]

Außerdem ist die Gammaform selbst exakt unter Nullfortsetzung kompatibel:

\[
q_{\Gamma,S}(J_{R,S}f,J_{R,S}g)
=q_{\Gamma,R}(f,g).
\]

Daraus folgt die metrische Pullback-Identität

\[
\boxed{
\Gamma_R^+
=(J_{R,S}^+)^*\Gamma_S^+J_{R,S}^+.
}
\tag{C1zB2C5d.46}
\]

Der natürliche gerade Grenztransport wäre somit

\[
\boxed{
W_{R,S,+}^{[\Gamma]}
:=(\Gamma_S^+)^{1/2}
J_{R,S}^+
(\Gamma_R^+)^{-1/2}.
}
\tag{C1zB2C5d.47}
\]

und ist automatisch isometrisch:

\[
(W_{R,S,+}^{[\Gamma]})^*W_{R,S,+}^{[\Gamma]}=I.
\]

Auch der Kokyklus folgt exakt aus der Gamma-Pullback-Identität.

**Aber:** C5d beweist noch nicht

\[
W_{R,S,+}^{[T]}	o W_{R,S,+}^{[\Gamma]}
\]

stark. Dafür muss die Wirkung der **positiven Target-Quadratwurzel** auf der speziellen Folge

\[
J_{R,S}^+(G_{R,T}^+)^{-1/2}f
\]

kontrolliert werden.

Damit ist der nächste Engpass nicht mehr Prime-Screening, sondern eine präzise Quadratwurzel-/Energie-Konvergenzfrage.

---

# 15. Statusmatrix

| Aussage | Status |
|---|---|
| generisches Future-Screening für gewichtete glatte odd Source-Vektoren | `✓[M]` |
| fester primitiver Small-Prime-Block kostet terminal nur `O(e^{-T/2})` | `✓[M]` |
| wachsender primitiver Block kostet `O(1/T)` | `✓[M]` aus C5c |
| höhere Prime-Powers besitzen uniforme gewichtete Source-Regularität | `✓[M]` |
| höhere Prime-Power-Hub durch primitiven Future-Rest screenbar | `✓[M]` |
| vollständiger gerader Schurterm `sigma_T(Jf)=O_f(1/T)` | `✓[M]` |
| bilineare Schurform verschwindet auf glattem even core | `✓[M]` |
| even-core Zukunftsformen sind Cauchy | `✓[M]` |
| kanonischer Grenzwert = Gammaform | `✓[M]` |
| Gamma-Grenzmetrik `Gamma_R^+` bounded + positiv invertierbar | `✓[M]` |
| Mosco-Konvergenz `mathfrak q_{R,T}^+ -> q_Gamma,R^+` | `✓[M]` |
| starker Resolventenlimes `G_{R,T}^+ -> Gamma_R^+` | `✓[M]` |
| starke Konvergenz `(G_{R,T}^+)^{-1/2}` | `✓[M]` |
| starke Konvergenz `(G_{R,T}^+)^{1/2}` | `?[O]` |
| `W_{R,S,+}^{[T]} -> W_{R,S,+}^{[Gamma]}` | `?[O]` |
| ungerader relativer Transport | `?[O]` |
| Objekt X / RH | `?[O]` |

---

# 16. Scope-Firewalls

C5d beweist **nicht**:

1. eine `T`-uniforme Operatornormschranke für `G_{R,T}^+`;
2. Normresolventen-Konvergenz;
3. Normkonvergenz der Zukunftsmetriken;
4. starke Konvergenz der positiven Quadratwurzeln auf allen Vektoren;
5. den starken geraden Terminaltransportlimes;
6. Cancellation des ungeraden Boundary-Jets;
7. eine Identifikation mit P04/Suzuki;
8. P10-O07;
9. Objekt X;
10. RH.

Insbesondere darf die Mosco-Konvergenz nicht zu einer stärkeren Operatornormaussage hochgestuft werden.

---

# 17. Strukturelles Gesamtbild nach C5d

Der gerade C1z-Kanal lautet nun

\[
\boxed{
\begin{array}{c}
\text{Boundary-Jet identisch blind}\\
\downarrow\\
\text{keine ungerade primitive Restnullmode}\\
\downarrow\\
\text{kein fester Primblock quantitativ koerziv}\\
\downarrow\\
\text{Future-Screening }d\mapsto d/2\\
\downarrow\\
\text{explizites Future-Prime-Dualzertifikat}\\
\downarrow\\
\text{keine Prime-Mikrostruktur-Divergenz auf glattem Core}\\
\downarrow\\
\textbf{vollständiger Schurterm }O(1/T)\to0\\
\downarrow\\
\textbf{Zukunftsmetrik }\overset{Mosco}{\longrightarrow}\textbf{ Gamma-Metrik}\\
\downarrow\\
\text{inverse Quadratwurzel konvergiert stark}\\
\downarrow\\
\textbf{nur noch Target-Quadratwurzel/Transport offen.}
\end{array}}
\]

Dies ist der erste echte **Grenzmetrik-Satz** des C1z-Strangs auf einer vollständigen Paritätshälfte.

---

# 18. Nächster atomarer Knoten

Der nächste Schritt ist nun erzwungen:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5e]
\quad
\text{Even terminal gauge: target-square-root / transport convergence audit}.
}
\]

Der natürliche Grenztransport ist bereits kanonisch festgelegt:

\[
W_{R,S,+}^{[\Gamma]}
=(\Gamma_S^+)^{1/2}
J_{R,S}^+
(\Gamma_R^+)^{-1/2}.
\]

Zu prüfen ist nur noch

\[
\boxed{
W_{R,S,+}^{[T]}
\stackrel?\longrightarrow
W_{R,S,+}^{[\Gamma]}
\quad\text{stark}.
}
\]

Nach C5d ist die Source-Inverse bereits stark konvergent. Der verbleibende mathematische Inhalt liegt ausschließlich darin, ob Mosco-Konvergenz plus die exakte Energieidentität auf den speziellen transportierten Vektoren ausreicht, um

\[
(G_{S,T}^+)^{1/2}
J_{R,S}^+
(G_{R,T}^+)^{-1/2}f
\]

stark zur Gamma-Version zu schicken.

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
