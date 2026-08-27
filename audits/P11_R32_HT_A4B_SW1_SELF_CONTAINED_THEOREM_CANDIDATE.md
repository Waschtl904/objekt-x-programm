# P11/R32 — HT-A4b-SW1: selbständiger Theorem-Kandidat ohne FG-Blackbox

**Status:** Theorem-Kandidat; keine Promotion.  
**Arbeitsname:** HT-A4b-SW1-M.  
**Repo-Basis:** main@de1bc09ae2e1b57083f3f44fc168e7cf2f8c8424.  
**Promotionsziel:** nach unabhängigem mathematischem und mechanischem GREEN gegebenenfalls
\[
\mathrm{HT\!-\!A4b\!-\!SW1\!-\!M}:\checkmark[M].
\]

**Scope:** nur der restricted-tail-Subwedge
\[
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta.
\]

**Harte Abhängigkeits-Firewall:** Der Beweis unten verwendet nicht HT.17, HT.18, HT.23–HT.27, FG-TR1 oder HT-A4a als mathematische Lemmas. Die für SW1 benötigten Spezialfälle werden direkt aus den Samplingfenstern und elementarer Intervallarithmetik bewiesen. Verweise auf ältere Labels erscheinen nur in einem nachgelagerten Vergleichsabschnitt.

---

## 0. Ziel und Satz

Setze
\[
a=\frac12\log2,
\qquad
b=\frac12\log3,
\qquad
T=2a=\log2,
\qquad
c=\frac12\log5,
\]
und
\[
d:=b-a,
\qquad
e:=T-b,
\qquad
\Delta:=d-e=2d-a.
\]

Seien
\[
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta,
\qquad
T_0:=T+\varepsilon.
\tag{M.1}
\]

Definiere
\[
\mathcal U_R
:=
\bigcup_{\tau\in\{a,b,T\}}
(\tau-R,\tau+R)\cap(0,T_0)
\tag{M.2}
\]
und
\[
\mathcal Z_R^{\rm phys}
:=
(0,T_0)\setminus\mathcal U_R.
\tag{M.3}
\]

Für ein gerades
\[
y\in L^2(-T_0,T_0)^+
\]
definiere den kanonischen Blindanteil \(z\) durch
\[
z(t)
:=
\begin{cases}
y(t),& |t|\in\mathcal Z_R^{\rm phys},\\
0,& |t|\in\mathcal U_R,
\end{cases}
\quad\text{a.e.}
\tag{M.4}
\]

### Satz HT-A4b-SW1-M

Unter (M.1) gilt für fast jedes
\[
s\in(R,\varepsilon):
\]
alle sechs Punkte
\[
s,\quad a-s,\quad a+s,\quad T-s,\quad 2d-s,\quad T+s
\tag{M.5}
\]
liegen in \(\mathcal Z_R^{\rm phys}\). Folglich
\[
\boxed{
\begin{aligned}
y(s)&=z(s),\\
y(a-s)&=z(a-s),\\
y(a+s)&=z(a+s),\\
y(T-s)&=z(T-s),\\
y(2d-s)&=z(2d-s),\\
y(T+s)&=z(T+s).
\end{aligned}
}
\tag{M.6}
\]

Insbesondere besitzt der SW1-Tail keine interne Sampling-Umschaltung und keinen \(X=x_0\)-Ast.

Zusätzlich definiere
\[
I_-:=(a-\varepsilon,a-R),
\qquad
I_+:=(a+R,a+\varepsilon),
\qquad
I_b:=(2d-\varepsilon,2d-R).
\tag{M.7}
\]

Dann
\[
\boxed{I_b\cap I_-=\varnothing}
\tag{M.8}
\]
und
\[
\boxed{
I_b\cap I_+\ne\varnothing
\iff
\varepsilon>\frac{\Delta}{2}.
}
\tag{M.9}
\]

Bei \(\varepsilon=\Delta/2\) ist der offene Mengenschnitt \(I_b\cap I_+\) leer, während die Abschlüsse genau einen gemeinsamen Endpunkt besitzen.

---

## 1. Exakte Konstantenordnung

Es gilt
\[
d=\frac12\log\frac32,
\qquad
e=\frac12\log\frac43,
\qquad
\Delta=\frac12\log\frac98,
\tag{M.10}
\]
und
\[
\varepsilon_{\max}:=c-T
=
\frac12\log\frac54.
\tag{M.11}
\]

Da
\[
1<\frac98<\frac54<\frac43<\frac32,
\]
folgt
\[
\boxed{
0<\Delta<\varepsilon_{\max}<e<d.
}
\tag{M.12}
\]

Ferner
\[
d<a
\]
wegen \(3/2<2\), also
\[
2d<2a=T.
\tag{M.13}
\]

Aus
\[
a=d+e
\]
folgt
\[
a>\Delta.
\tag{M.14}
\]

Schließlich
\[
e-2\Delta
=
\frac12\log\frac{256}{243}
>0,
\]
also
\[
\boxed{e>2\Delta.}
\tag{M.15}
\]

---

## 2. Unmittelbare Folgen des SW1-Wedges

Aus \(R<\varepsilon\) folgt
\[
2R<R+\varepsilon<\Delta,
\]
also
\[
\boxed{
R<\frac{\Delta}{2}.
}
\tag{M.16}
\]

Ebenso
\[
R+\varepsilon<\Delta
\iff
\varepsilon<\Delta-R,
\]
also
\[
\boxed{
\varepsilon<\Delta-R<\Delta.
}
\tag{M.17}
\]

Damit
\[
0<R<\varepsilon<\Delta<e<d<a<T.
\tag{M.18}
\]

Weil
\[
\Delta<\varepsilon_{\max}=c-T,
\]
gilt
\[
T<T_0=T+\varepsilon<c.
\tag{M.19}
\]

---

## 3. Alle sechs Zielpunkte liegen in \((0,T_0)\)

Sei
\[
R<s<\varepsilon.
\tag{M.20}
\]

Für \(s\) ist \(0<s<T_0\) klar.

Wegen
\[
s<\varepsilon<\Delta<a
\]
gilt
\[
a-s>0.
\]

Ferner
\[
a+s<a+\varepsilon<T+\varepsilon=T_0.
\]

Ebenso
\[
0<T-s<T<T_0.
\]

Wegen
\[
s<\varepsilon<\Delta<d
\]
gilt
\[
2d-s>d>0,
\]
und nach (M.13)
\[
2d-s<2d<T<T_0.
\]

Schließlich
\[
T<T+s<T+\varepsilon=T_0.
\]

Also
\[
\boxed{
s,\ a-s,\ a+s,\ T-s,\ 2d-s,\ T+s\in(0,T_0).
}
\tag{M.21}
\]

---

## 4. Direkter Blindheitsbeweis ohne HT.23–HT.27

Wir zeigen für jeden der sechs Punkte strikten Abstand \(>R\) zu allen drei Samplingzentren \(a,b,T\).

### 4.1 \(t=s\)

Aus
\[
R+s<R+\varepsilon<\Delta<a
\]
folgt
\[
a-s>R.
\tag{M.22}
\]

Da \(b>a\) und \(T>a\),
\[
b-s>a-s>R,
\qquad
T-s>a-s>R.
\tag{M.23}
\]

Also
\[
s\notin\mathcal U_R.
\tag{M.24}
\]

### 4.2 \(t=a-s\)

\[
|a-s-a|=s>R,
\tag{M.25}
\]
\[
b-(a-s)=d+s>R,
\tag{M.26}
\]
\[
T-(a-s)=a+s>R.
\tag{M.27}
\]

Also
\[
a-s\notin\mathcal U_R.
\tag{M.28}
\]

### 4.3 \(t=a+s\)

\[
|a+s-a|=s>R.
\tag{M.29}
\]

Weiter
\[
b-(a+s)=d-s.
\]
Aus
\[
R+s<R+\varepsilon<\Delta<d
\]
folgt
\[
d-s>R.
\tag{M.30}
\]

Außerdem
\[
T-(a+s)=a-s>R
\tag{M.31}
\]
wegen \(R+s<\Delta<a\).

Also
\[
a+s\notin\mathcal U_R.
\tag{M.32}
\]

### 4.4 \(t=T-s\)

\[
|T-s-T|=s>R.
\tag{M.33}
\]

Da \(b=T-e\),
\[
(T-s)-b=e-s.
\]
Wegen
\[
R+s<\Delta<e
\]
folgt
\[
e-s>R.
\tag{M.34}
\]

Zum Zentrum \(a\):
\[
(T-s)-a=a-s>R.
\tag{M.35}
\]

Also
\[
T-s\notin\mathcal U_R.
\tag{M.36}
\]

### 4.5 \(t=2d-s\)

Da
\[
2d-a=\Delta,
\]
gilt
\[
(2d-s)-a=\Delta-s>R
\tag{M.37}
\]
wegen \(R+s<\Delta\).

Weiter
\[
b-(2d-s)
=
(a+d)-2d+s
=
a-d+s
=
e+s
>R.
\tag{M.38}
\]

Und
\[
T-(2d-s)
=
2a-2d+s
=
2e+s
>R.
\tag{M.39}
\]

Also
\[
2d-s\notin\mathcal U_R.
\tag{M.40}
\]

### 4.6 \(t=T+s\)

\[
|T+s-T|=s>R,
\tag{M.41}
\]
\[
T+s-b=e+s>R,
\tag{M.42}
\]
\[
T+s-a=a+s>R.
\tag{M.43}
\]

Also
\[
T+s\notin\mathcal U_R.
\tag{M.44}
\]

### 4.7 Schluss

Aus (M.21), (M.24), (M.28), (M.32), (M.36), (M.40), (M.44):
\[
\boxed{
s,\ a-s,\ a+s,\ T-s,\ 2d-s,\ T+s
\in
\mathcal Z_R^{\rm phys}.
}
\tag{M.45}
\]

Nach (M.4) folgt unmittelbar (M.6).

Damit ist der Membership-Teil vollständig bewiesen, ohne allgemeine FG-Rekonstruktion.

---

## 5. Die fünf SW1-Membership-Wände direkt aus den Abstandsgleichungen

Für \(a+s\) gegen das \(b\)-Fenster:
\[
d-s=R
\iff
s=d-R=:A_*.
\tag{M.46}
\]

Für \(T-s\) gegen das \(b\)-Fenster:
\[
e-s=R
\iff
s=e-R=:E.
\tag{M.47}
\]

Für \(2d-s\) gegen das \(a\)-Fenster:
\[
|\Delta-s|=R,
\]
also
\[
s=\Delta-R=:D_-,
\qquad
s=\Delta+R=:D_+.
\tag{M.48}
\]

Der Wert
\[
D_0:=\Delta
\tag{M.49}
\]
trennt die beiden Vorzeichen von \(\Delta-s\).

Somit:
\[
D_-=\Delta-R,
\quad
D_0=\Delta,
\quad
D_+=\Delta+R,
\quad
E=e-R,
\quad
A_*=d-R.
\tag{M.50}
\]

Auf SW1 gilt
\[
D_-=\Delta-R>\varepsilon,
\tag{M.51}
\]
\[
D_0=\Delta>D_->\varepsilon,
\qquad
D_+>\Delta>\varepsilon,
\tag{M.52}
\]
\[
E=e-R>\Delta-R>\varepsilon,
\tag{M.53}
\]
\[
A_*=d-R>e-R>\varepsilon.
\tag{M.54}
\]

Daher
\[
\boxed{
D_-,D_0,D_+,E,A_*>\varepsilon.
}
\tag{M.55}
\]

---

## 6. Zehn bekannte Referenz-Parameterflächen sind auf SW1 ausgeschlossen

Definiere die zehn Referenzflächen
\[
\begin{array}{lll}
\Sigma_1:\ \varepsilon=\Delta-R,
&
\Sigma_2:\ R=\Delta/2,
&
\Sigma_3:\ \varepsilon=\Delta,
\\
\Sigma_4:\ R=\Delta,
&
\Sigma_5:\ \varepsilon=\Delta+R,
&
\Sigma_6:\ \varepsilon=e-R,
\\
\Sigma_7:\ R=e/2,
&
\Sigma_8:\ \varepsilon=d-R,
&
\Sigma_9:\ R=d/2,
\\
\Sigma_{10}:\ R=C:=(e-\Delta)/2.
\end{array}
\tag{M.56}
\]

Dieser Abschnitt behauptet nicht, dass (M.56) global die vollständige Chamberzerlegung erzeugt. Er beweist nur selbständig, dass keine dieser zehn bekannten Referenzflächen das offene SW1-Gebiet schneidet.

\(\Sigma_1\): ausgeschlossen durch \(\varepsilon<\Delta-R\).

\(\Sigma_2\): ausgeschlossen durch \(R<\Delta/2\).

\(\Sigma_3\): ausgeschlossen durch \(\varepsilon<\Delta\).

\(\Sigma_4\): ausgeschlossen durch \(R<\Delta/2<\Delta\).

\(\Sigma_5\): ausgeschlossen durch
\[
\varepsilon<\Delta-R<\Delta+R.
\]

\(\Sigma_6\): würde
\[
R+\varepsilon=e
\]
erzwingen, im Widerspruch zu
\[
R+\varepsilon<\Delta<e.
\]

\(\Sigma_7\): ausgeschlossen durch
\[
R<\Delta/2<e/2.
\]

\(\Sigma_8\): würde
\[
R+\varepsilon=d
\]
erzwingen, im Widerspruch zu
\[
R+\varepsilon<\Delta<d.
\]

\(\Sigma_9\): ausgeschlossen durch
\[
R<\Delta/2<d/2.
\]

Für \(\Sigma_{10}\) folgt aus \(e>2\Delta\):
\[
C=\frac{e-\Delta}{2}>\frac{\Delta}{2}>R.
\]

Somit
\[
\boxed{
\mathfrak W_{\rm SW1}
\cap
\bigcup_{j=1}^{10}\Sigma_j
=
\varnothing.
}
\tag{M.57}
\]

---

## 7. Direkter A-Wall-Beweis ohne HT.17/HT.18

Aus
\[
2d-a=\Delta
\]
folgt
\[
2d=a+\Delta.
\tag{M.58}
\]

Daher
\[
I_b
=
(a+\Delta-\varepsilon,\ a+\Delta-R).
\tag{M.59}
\]

### 7.1 \(I_b\cap I_-\)

Aus (M.7) und (M.59):
\[
I_b=I_-+\Delta.
\tag{M.60}
\]

Beide Intervalle haben Länge \(\varepsilon-R\). Da \(I_b\) um \(\Delta>0\) nach rechts verschoben ist,
\[
I_b\cap I_-\ne\varnothing
\iff
\Delta<\varepsilon-R.
\tag{M.61}
\]

Auf SW1
\[
\varepsilon-R<\varepsilon+R<\Delta.
\tag{M.62}
\]

Also
\[
\boxed{
I_b\cap I_-=\varnothing.
}
\tag{M.63}
\]

### 7.2 \(I_b\cap I_+\)

Die offenen Intervalle
\[
I_+=(a+R,a+\varepsilon)
\]
und
\[
I_b=(a+\Delta-\varepsilon,a+\Delta-R)
\]
schneiden sich genau dann, wenn
\[
a+R<a+\Delta-R
\tag{M.64}
\]
und
\[
a+\Delta-\varepsilon<a+\varepsilon.
\tag{M.65}
\]

Das ist äquivalent zu
\[
2R<\Delta
\tag{M.66}
\]
und
\[
\Delta<2\varepsilon.
\tag{M.67}
\]

Nach (M.16) gilt (M.66) auf SW1 automatisch. Also
\[
\boxed{
I_b\cap I_+\ne\varnothing
\iff
\varepsilon>\frac{\Delta}{2}.
}
\tag{M.68}
\]

### 7.3 Degenerationsfläche

Bei
\[
\varepsilon=\frac{\Delta}{2}
\]
gilt
\[
a+\Delta-\varepsilon
=
a+\frac{\Delta}{2}
=
a+\varepsilon.
\tag{M.69}
\]

Die linke Grenze von \(I_b\) ist damit gleich der rechten Grenze von \(I_+\). Da beide Intervalle offen sind,
\[
\boxed{
I_b\cap I_+=\varnothing.
}
\tag{M.70}
\]

Für die Abschlüsse gilt
\[
\boxed{
\overline I_b\cap\overline I_+
=
\left\{a+\frac{\Delta}{2}\right\}.
}
\tag{M.71}
\]

Der einzelne Berührpunkt ist als Output-/Integrationspunkt eine \(L^2\)-Nullmenge. Die Parameterkonfiguration \(\varepsilon=\Delta/2\) selbst bleibt eine echte Parameterwand.

---

## 8. Nichtleere der unterschiedenen Parameterklassen

Untere Unterkammer:
\[
R_-=\frac{\Delta}{6},
\qquad
\varepsilon_-=\frac{\Delta}{3},
\qquad
\sigma_-=\frac{\Delta}{12}.
\tag{M.72}
\]

Degenerationsfläche:
\[
R_0=\frac{\Delta}{4},
\qquad
\varepsilon_0=\frac{\Delta}{2},
\qquad
\sigma_0=\frac{\Delta}{8}.
\tag{M.73}
\]

Obere Unterkammer:
\[
R_+=\frac{\Delta}{10},
\qquad
\varepsilon_+=\frac{3\Delta}{5},
\qquad
\sigma_+=\frac{\Delta}{20}.
\tag{M.74}
\]

Restricted-tail-Rand:
\[
R_\partial=\sigma_\partial=\frac{\Delta}{6},
\qquad
\varepsilon_\partial=\frac{\Delta}{3}.
\tag{M.75}
\]

Direktes Einsetzen zeigt jeweils
\[
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta,
\]
und die behauptete Lage relativ zu \(\varepsilon=\Delta/2\).

---

## 9. Verträglichkeit mit \(R\to0\)

Fixiere
\[
0<\varepsilon_*<\Delta.
\]

Für jede Folge
\[
R_n\downarrow0
\]
mit schließlich
\[
R_n<\min\{\varepsilon_*,\Delta-\varepsilon_*\}
\]
gilt
\[
0<R_n<\varepsilon_*,
\qquad
R_n+\varepsilon_*<\Delta.
\]

Mit
\[
\sigma_n:=R_n/2
\]
gilt zusätzlich
\[
0<\sigma_n\le R_n.
\]

Dies ist nur eine Parameteraussage.

---

## 10. A0-Komplement-Firewall

Die Restriktion
\[
R+\varepsilon<\Delta
\]
beschränkt Konstruktionsparameter, nicht den freien \(L^2\)-Koordinatenraum eines bereits gewählten Horizonts.

Gleichzeitig legt
\[
T_0=T+\varepsilon
\]
die betrachtete Horizontskala fest. Ein kleineres \(\varepsilon\) ersetzt keine Analyse eines anderen oder größeren Horizonts.

Daher
\[
\boxed{
\text{HT-A4b-SW1-M ist kein A0-Abschluss.}
}
\tag{M.76}
\]

---

## 11. Vergleich mit älteren Kandidatenlabels — keine Beweisabhängigkeit

Erst nach Abschluss des selbständigen Beweises gilt als Vergleich:

- (M.6) ist der SW1-Spezialfall der früheren HT.23–HT.26-Membership-Klassifikation.
- Der \(X\)-Ast tritt nicht auf; HT.27/TR.13 wird hier nicht benötigt.
- (M.63) ist der SW1-Spezialfall der früheren HT.17-Kollision.
- (M.68)–(M.71) sind der SW1-Spezialfall der früheren HT.18-Kollision.
- (M.55) erklärt die Single-FG-Chamber-Struktur direkt.
- (M.57) ist nur ein Konsistenzcheck gegen zehn bekannte Referenzflächen; globale 15-Chamber-Exhaustivität wird nicht behauptet.

Keiner dieser älteren Kandidaten wird als Lemma verwendet.

---

## 12. Promotionsfähiger Kern

Der promotionsfähige Kern ist ausschließlich:

Unter
\[
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta
\]
liegen die sechs Punkte
\[
s,\ a-s,\ a+s,\ T-s,\ 2d-s,\ T+s
\]
für fast jedes \(s\in(R,\varepsilon)\) außerhalb aller drei Samplingfenster um \(a,b,T\). Daher sind sie direkte Blindwerte des kanonischen Supportsplits. Die fünf SW1-Membership-Wände liegen strikt rechts von \(\varepsilon\). Für die offenen A-Wall-Shells gilt
\[
I_b\cap I_-=\varnothing,
\qquad
I_b\cap I_+\ne\varnothing
\iff
\varepsilon>\Delta/2,
\]
mit leerem offenen Schnitt und genau einem Abschluss-Berührpunkt bei \(\varepsilon=\Delta/2\).

Nicht behauptet werden:

- globale HT-A4b-Exhaustivität der 15 Chambers;
- allgemeine FG-Exhaustivität;
- HT-RED;
- Trivialität des augmentierten Kernes;
- A0;
- \(\ker\Gamma_I=\{0\}\);
- Schur-Cross-Gram-Injektivität;
- Closed Range / bounded below;
- Strong Terminal Transport;
- Objekt X;
- RH.

---

## 13. Status vor unabhängigem Review

    HT-A4b-SW1-M SELF-CONTAINED THEOREM: ?[O]

    HT-A4b GLOBAL CHAMBER EXHAUSTIVITY:   ?[O]
    HT-RED:                               ?[O]
    A0:                                   ?[O]
    SCHUR CROSS-GRAM INJECTIVITY:         ?[O]

Eine spätere Promotion zu \(\checkmark[M]\) ist nur für den in §12 exakt abgegrenzten Satz vorgesehen.

---

## 14. Adversarialer Review-Auftrag

Unabhängig neu zu prüfen sind:

1. alle Konstantenidentitäten und Ordnungen in §1;
2. die SW1-Folgerungen in §2;
3. dass alle sechs Zielpunkte in \((0,T_0)\) liegen;
4. für jeden der sechs Punkte die drei Abstände zu \(a,b,T\) in §4;
5. dass daraus die Blindheitsaussage ohne FG-Rekonstruktionsblackbox folgt;
6. die Herleitung der fünf SW1-Membership-Wände direkt aus den Abstandsgleichungen;
7. die Ausschlüsse aller fünf Wände aus \((R,\varepsilon)\);
8. alle zehn einzelnen Referenzflächen-Ausschlüsse in §6, ohne globale Exhaustivität zu overclaimen;
9. die direkte Intervallrechnung in §7 ohne HT.17/HT.18;
10. die offene Intervallkonvention auf \(\varepsilon=\Delta/2\);
11. alle vier Nichtleerheitszeugen;
12. die \(R\to0\)-Parameteraussage;
13. die A0-Komplement-Firewall;
14. dass HT.17, HT.18, HT.23–HT.27, FG-TR1 und HT-A4a nirgendwo als Beweisprämisse benutzt werden;
15. die Scope-Firewall von §12.

Kein \(\checkmark[M]\) und kein Promotionsmerge ohne unabhängiges GREEN gegen den exakten PR-Diff.
