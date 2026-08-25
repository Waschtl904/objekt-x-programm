# P11/R32 — Triangular Row Splitting des gesampelten Fiber-Graph-Kerns

**Status:** neuer Kandidat; keine Promotion.  
**Arbeitsname:** `FG-TR1`.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** `P11_R32_INVISIBLE_FIBER_GRAPH_RECONSTRUCTION_ADDENDUM.md` und `P11_R32_FG_EXHAUSTIVITY_CLOSURE.md`.

## 0. Aussage in einem Satz

Die Fiber-Graph-Kernelgleichung ist im gesamten zulässigen Bereich `0<R<a` nicht zyklisch, sondern **zweistufig triangulär**: der linke `A_-`-Branch ist bis auf genau eine mögliche `B_-`-Rückkopplung ein privater Kanal, und diese Rückkopplung kann wegen `a<2d` niemals ein zweites Mal iterieren. Dadurch lässt sich der gesamte gesampelte Kernel explizit durch freie `L2`-Daten auf der rechten physischen Sample-Seite parametrisieren.

---

## 1. Setup

Setze

\[
a=\frac12\log2,
\qquad b=\frac12\log3,
\qquad T=2a,
\]

\[
d=b-a,
\qquad e=T-b,
\qquad 0<R<a.
\]

Dann

\[
\boxed{a=d+e.}
\tag{TR.1}
\]

Ferner

\[
d-e
=\frac12\log\frac98>0,
\]

also

\[
\boxed{d>e,\qquad a<2d.}
\tag{TR.2}
\]

Die letzte Ungleichung ist äquivalent zu `9>8`.

Sei

\[
L_R:=\Lambda_RJ_R:L^2(\mathcal U_R)\longrightarrow L^2(0,R).
\tag{TR.3}
\]

In physischen Koordinaten lautet

\[
(L_Rg)(u)
=p[g(a-u)-g(a+u)]
+r[g(b-u)-g(b+u)]
+q[g(T-u)-g(T+u)],
\tag{TR.4}
\]

wobei Werte außerhalb `(0,T_0)` bzw. außerhalb des aktiven gesampelten Bereichs als Null verstanden werden.

Der folgende Split benötigt nur

\[
\boxed{p\ne0.}
\tag{TR.5}
\]

Dies ist im kanonischen P11-Hub erfüllt: die neutralen Prime-Power-Hubgewichte haben die Form

\[
\sqrt{\log \ell}\,\ell^{-3k/4}>0
\]

für jede aktive Primzahl `ell` und `k>=1`; insbesondere verschwindet der Koeffizient des ersten `2`-Kanals nicht. `FG-TR1` benutzt keine weitere Vorzeichenannahme an `r,q`.

---

## 2. Linker privater Sample-Kanal

Definiere

\[
I_R^-:=(a-R,a),
\qquad
\mathcal V_R:=\mathcal U_R\cap(a,T_0).
\tag{TR.6}
\]

A.e. gilt die disjunkte Zerlegung

\[
\boxed{
\mathcal U_R=I_R^-\,\dot\cup\,\mathcal V_R.
}
\tag{TR.7}
\]

Denn das linkeste der drei Samplingfenster ist das `a`-Fenster; unterhalb `a` ist daher der gesamte gesampelte Bereich genau `(a-R,a)`.

Schreibe

\[
x(u):=g(a-u),\qquad0<u<R.
\tag{TR.8}
\]

Die fünf übrigen Auswertungsstellen liegen für `0<u<R<a` rechts von `a`, mit genau einer möglichen Ausnahme:

- `a+u>a`;
- `T-u>a`, weil `u<a`;
- `b+u>a`;
- `T+u>a`;
- `b-u=a+d-u` liegt rechts von `a` für `u<d`, aber links von `a` für `u>d`.

Für `u>d` gilt exakt

\[
\boxed{
b-u=a-(u-d),}
\tag{TR.9}
\]

also

\[
g(b-u)=x(u-d).
\tag{TR.10}
\]

Entscheidend ist nun: Falls `d<u<R`, dann

\[
0<u-d<R-d<a-d=e<d.
\tag{TR.11}
\]

Die Rückkopplung landet somit **immer in der ersten Schicht `0<u<d`**. Eine zweite Rückkopplung `u-d-d` ist nie nötig. Der scheinbare Overlap-Graph ist für die Row-Gleichung daher zweistufig triangulär.

---

## 3. Explizite Rekonstruktion aus Row-Daten und rechter freier Seite

Seien beliebig

\[
f\in L^2(0,R),
\qquad
h\in L^2(\mathcal V_R).
\]

Sei `h_tilde` die Nullfortsetzung von `h` auf `(0,T_0)\setminus\mathcal V_R`.

Wir suchen eindeutig `g in L2(U_R)` mit

\[
L_Rg=f,
\qquad
g|_{\mathcal V_R}=h.
\tag{TR.12}
\]

### Erste Schicht: `0<u<min{R,d}`

Hier liegt auch `b-u` rechts von `a`. Daher ist die Row-Gleichung direkt nach `x(u)=g(a-u)` auflösbar:

\[
\boxed{
\begin{aligned}
x_0(u)
={}&\widetilde h(a+u)
-\frac rp\bigl[\widetilde h(b-u)-\widetilde h(b+u)\bigr]\\
&-\frac qp\bigl[\widetilde h(T-u)-\widetilde h(T+u)\bigr]
+\frac1p f(u).
\end{aligned}
}
\tag{TR.13}
\]

### Zweite Schicht: `d<u<R`

Dieser Fall existiert nur wenn `R>d`. Nun ist `b-u=a-(u-d)` und der dort auftretende linke Wert bereits durch die erste Schicht bekannt. Also

\[
\boxed{
\begin{aligned}
x_1(u)
={}&\widetilde h(a+u)
-\frac rp\bigl[x_0(u-d)-\widetilde h(b+u)\bigr]\\
&-\frac qp\bigl[\widetilde h(T-u)-\widetilde h(T+u)\bigr]
+\frac1p f(u).
\end{aligned}
}
\tag{TR.14}
\]

Wegen (TR.11) ist `x_0(u-d)` immer definiert; keine dritte Formel und keine unendliche Rekursion treten auf.

Setze anschließend

\[
g(t)=h(t)\quad(t\in\mathcal V_R),
\]

und

\[
g(a-u)=
\begin{cases}
x_0(u),&0<u<\min\{R,d\},\\
x_1(u),&d<u<R.
\end{cases}
\tag{TR.15}
\]

Die Stelle `u=d` ist eine Nullmenge.

Direktes Einsetzen in (TR.4) ergibt

\[
\boxed{L_Rg=f.}
\tag{TR.16}
\]

Eindeutigkeit folgt ebenfalls schichtweise: auf der ersten Schicht bestimmt (TR.4) wegen `p!=0` den einzigen möglichen Wert `x_0`; auf der zweiten Schicht ist der einzige zusätzliche linke Wert `x_0(u-d)` bereits festgelegt, also ist auch `x_1` eindeutig.

---

## 4. Beschränkter Koordinatenisomorphismus

Definiere

\[
\boxed{
\Theta_R:L^2(\mathcal U_R)
\longrightarrow
L^2(0,R)\oplus L^2(\mathcal V_R),
\qquad
\Theta_Rg=(L_Rg,g|_{\mathcal V_R}).
}
\tag{TR.17}
\]

`Theta_R` ist beschränkt, weil `L_R` und die Restriktion beschränkt sind.

Die Formeln (TR.13)–(TR.15) definieren `Theta_R^{-1}`. Alle darin vorkommenden Operationen sind endlich viele

- Restriktionen,
- Nullfortsetzungen,
- Translationen/Reflexionen mit Jacobi-Betrag `1`,
- Multiplikationen mit den festen Skalaren `1/p`, `r/p`, `q/p`.

Daher ist `Theta_R^{-1}` beschränkt. Somit

\[
\boxed{
\Theta_R:L^2(\mathcal U_R)
\xrightarrow{\sim}
L^2(0,R)\oplus L^2(\mathcal V_R)
}
\tag{TR.18}
\]

ein beschränkter linearer Isomorphismus.

In diesen Koordinaten ist der Row-Operator schlicht die erste Projektion:

\[
\boxed{
L_R=\operatorname{pr}_1\circ\Theta_R.
}
\tag{TR.19}
\]

Das ist die zentrale Strukturreduktion.

---

## 5. Expliziter beschränkter Rechtsinverse

Setze in der Rekonstruktion `h=0`. Dann vereinfacht sich die linke Lösung zu

\[
(Q_Rf)(a-u)
=
\begin{cases}
\dfrac1p f(u),&0<u<\min\{R,d\},\\[2mm]
\dfrac1p f(u)-\dfrac r{p^2}f(u-d),&d<u<R,
\end{cases}
\tag{TR.20}
\]

und `Q_Rf=0` auf `V_R`.

Damit

\[
\boxed{L_RQ_R=I_{L^2(0,R)}.}
\tag{TR.21}
\]

Also ist `L_R` für **jedes `0<R<a` split-surjektiv** und besitzt einen expliziten beschränkten Rechtsinversen.

---

## 6. Vollständige Parametrisierung des gesampelten Kernes

Aus (TR.18)–(TR.19) folgt sofort

\[
\ker L_R
=\Theta_R^{-1}(\{0\}\oplus L^2(\mathcal V_R)).
\]

Daher ist die Restriktion auf die rechte Sample-Seite ein beschränkter Isomorphismus

\[
\boxed{
\ker L_R\xrightarrow{\sim}L^2(\mathcal V_R).
}
\tag{TR.22}
\]

Über den bereits bewiesenen Branch-Isomorphismus `J_R` folgt

\[
\boxed{
\mathfrak G_R\cap\ker\Lambda_R
\xrightarrow{\sim}
L^2(\mathcal V_R).
}
\tag{TR.23}
\]

Damit ist der gesampelte Gluing-Kernel nicht nur „durch eine endliche Branchrelation beschrieben“, sondern besitzt eine **explizite freie physische Koordinate**: beliebige `L2`-Daten auf `V_R`; die linke Seite `(a-R,a)` wird daraus eindeutig und beschränkt rekonstruiert.

---

## 7. Kombination mit dem blinden Summanden

Mit dem Exhaustivitätsabschluss

\[
\mathcal N_I\cong
\mathcal Z_R^+\oplus(\mathfrak G_R\cap\ker\Lambda_R)
\]

folgt als Kandidatenkorollar

\[
\boxed{
\mathcal N_I
\cong
\mathcal Z_R^+\oplus L^2(\mathcal V_R),
\qquad0<R<a.
}
\tag{TR.24}
\]

Der Isomorphismus ist beschränkt und explizit konstruierbar.

Dies ist stärker als eine bloße Klassifikation nach endlich vielen Shell-/Orbittypen: für die **innere Unsichtbarkeitsgleichung allein** ist keine weitere Orbitzerlegung nötig, um den gesamten Lösungsraum zu parametrisieren.

---

## 8. Bedeutung für die nächste Forschungsfront

(TR.24) zeigt zugleich, warum `N_I` groß bleibt: die lokale Hub-Unsichtbarkeitsgleichung lässt eine ganze freie `L2(V_R)`-Koordinate übrig.

Der nächste sinnvolle Operator ist deshalb nicht mehr `E_I^*H` isoliert. Man sollte die zusätzliche Full-Rest-/Schur-Bedingung durch `Theta_R^{-1}` ziehen und auf den freien Koordinaten

\[
(z,h)\in\mathcal Z_R^+\oplus L^2(\mathcal V_R)
\]

untersuchen. Die bekannten Mechanismen CTX-1, NS-1 und ST-1 werden damit als bereits kontrollierte Teilgeometrien eines einzigen reduzierten Operators interpretierbar.

Strategisches Ziel:

\[
\boxed{
\text{Schur/Full-Rest-Bedingung}\circ
\Phi_R\circ(\mathrm{id}\oplus J_R\Theta_R^{-1}(0,\cdot))
}
\]

als Operator auf den **freien physischen Koordinaten** explizit bestimmen und auf Injektivität/Transversalität prüfen.

---

## 9. Firewall

`FG-TR1` behauptet ausschließlich Struktur der lokalen inneren Row-Gleichung. Es folgt **nicht**:

- `N_I={0}` — im Gegenteil, (TR.24) macht die verbleibende Freiheit explizit;
- Trivialität des augmentierten Blockkerns;
- Injektivität des vollen Schur-Crossblocks;
- Closed Range / bounded below / uniforme Winkel für den globalen Block;
- Strong Terminal Transport;
- Objekt X oder RH.

Ebenso wird keine endliche Dimension behauptet. `L2(V_R)` ist bei positiver Länge unendlichdimensional.

---

## 10. Kandidatenstatus

```text
FG-TR1 TRIANGULAR ROW SPLITTING: ?[O]
```

Für eine Promotion wäre mindestens unabhängig zu prüfen:

1. die a.e.-Zerlegung (TR.7);
2. dass `B_-` der einzige Branch ist, der den linken Kanal zusätzlich trifft;
3. die arithmetische Schranke `a<2d` und damit die Tiefe eins der Rückkopplung;
4. die Formeln (TR.13)–(TR.16);
5. Beschränktheit von `Theta_R^{-1}`;
6. der explizite Rechtsinverse (TR.20)–(TR.21);
7. die Kernelisomorphismen (TR.22)–(TR.24);
8. die Scope-Firewall.

Keine Promotion ohne unabhängiges GREEN und ausdrückliche Projektfreigabe.
