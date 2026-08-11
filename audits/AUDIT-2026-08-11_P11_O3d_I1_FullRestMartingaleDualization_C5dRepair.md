# P11-O3d-I1 — Full-Rest-Martingal-Dualisierung und Reparatur des C5d-Transfers

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3d-I1]`  
**Vorgänger:** O3d-PRECHECK-RECONCILIATION  
**Schnittstellen:** C1z-B1, C5c, C5d, C6q, C6s, O3a, O3b, O3c  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, keine Behauptung der primitiven Formdomination, kein odd matching upper bound, kein SYN, kein Seal.

---

## 0. Urteil

Der in O3d-PRECHECK identifizierte Gap

\[
R_T^*R_T\stackrel{?}{\ge}(R_T^{(1)})^*R_T^{(1)}
\]

muss für die C5d-Future-Zertifikate **nicht** gelöst werden.

C6s liefert eine kanonische vollständige Martingal-Analysezerlegung des vollen Rest-Grams. Daraus kann ein neuer Analyseoperator

\[
\widetilde R_T
\]

gebaut werden mit

\[
\boxed{\widetilde R_T^*\widetilde R_T=R_T^*R_T.}
\]

Im `a=0`-Future-Kanal ist dieser volle Analyseoperator exakt

\[
\text{primitiver Reflection-Edge}
+
\text{höherer Prime-Power-Tail},
\]

wobei der Tail auf den von C5c/C5d verwendeten Future-Primes operatornormmäßig exponentiell klein ist.

Daher lässt sich jedes der bereits konstruierten C5d-**primitiven Future-Zertifikate** direkt als Zertifikat für `\widetilde R_T` verwenden; der höhere `k\ge2`-Anteil des vollen Future-Kanals wird als zusätzlicher Source-Rest absorbiert.

Damit wird der Full-Rest-Schur-Upper-Transfer von C5d repariert, **ohne** die offene Formordnung zu benutzen.

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3d\text{-}I1]
&\quad \checkmark[M]_{\rm canonical\;full\text{-}rest\;martingale\;analysis}\\
&+\checkmark[M]_{\rm future\;a=0\;primitive+tail\;decomposition}\\
&+\checkmark[M]_{\rm future\;tail\;operator\;smallness}\\
&+\checkmark[M]_{\rm C5d\;full\text{-}rest\;dual\;transfer\;repaired}\\
&+\checkmark[M]_{\rm C5d.1\;restored}\\
&+\checkmark[M]_{\rm C5d.2\;restored}\\
&+\checkmark[M]_{\rm C5d.3\;restored}\\
&+\checkmark[M]_{\rm O3a.1\;restored}\\
&+?[O]_{R_T^*R_T\ge(R_T^{(1)})^*R_T^{(1)}}\\
&+?[O]_{\rm O3d\;odd\;matching\;upper\;bound}.
\end{aligned}
}
\]

Die offene primitive Formdomination bleibt ausdrücklich **offen und unbenutzt**.

---

# 1. C6s als kanonischer voller Analyseoperator

Fixiere `T>0` und setze

\[
\mathscr H_T:=L^2(-T,T).
\]

Aus C6s:

\[
\Omega_{p,a,T}
=
\left\{
|u|\le T-\frac{a+1}{2}\log p
\right\}
\]

bis auf irrelevante Randpunkte, und

\[
\Phi_{p,a,T}[f](u)
:=
\sum_{k\ge a+1}
p^{-3k/4}
K_{k\log p}f(u),
\]

wobei

\[
K_s=P_TD_sE_T,
\qquad
D_s=U_{s/2}-U_{-s/2}.
\]

C6s beweist die exakte sesquilineare Restform

\[
\boxed{
\langle R_Tf,R_Tg\rangle
=
\sum_p(\log p)(p-1)
\sum_{a\ge0}p^a
\int_{\Omega_{p,a,T}}
\Phi_{p,a,T}[f](u)
\overline{\Phi_{p,a,T}[g](u)}\,du.
}
\tag{I1.1}
\]

Definiere den kanonischen Martingal-Zielraum

\[
\boxed{
\mathscr Z_T
:=
\bigoplus_{p}
\bigoplus_{a\ge0}
L^2(\Omega_{p,a,T}).
}
\tag{I1.2}
\]

Bei festem `T` sind nur endlich viele `(p,a)` aktiv.

Definiere

\[
\boxed{
(\widetilde R_Tf)_{p,a}(u)
:=
\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,T}}(u)
\Phi_{p,a,T}[f](u).
}
\tag{I1.3}
\]

Dann folgt aus (I1.1) für alle `f,g`:

\[
\boxed{
\langle\widetilde R_Tf,\widetilde R_Tg\rangle_{\mathscr Z_T}
=
\langle R_Tf,R_Tg\rangle.
}
\tag{I1.4}
\]

Somit

\[
\boxed{
\widetilde R_T^*\widetilde R_T
=
R_T^*R_T.
}
\tag{I1.5}
\]

Dies ist stärker als eine bloße Normgleichheit; es ist die polarisierte C6s-Gramidentität.

Insbesondere ist der Feshbach-Nenner exakt

\[
\boxed{
A_T
=I+R_T^*R_T
=I+\widetilde R_T^*\widetilde R_T.
}
\tag{I1.6}
\]

---

# 2. Exakte Full-Rest-Dualform ohne primitive Dominanz

Für beliebiges `h\in\mathscr H_T` gilt daher die Standard-Feshbach-Dualität

\[
\boxed{
\langle h,A_T^{-1}h\rangle
=
\inf_{Y\in\mathscr Z_T}
\left(
\|h-\widetilde R_T^*Y\|_2^2
+
\|Y\|_{\mathscr Z_T}^2
\right).
}
\tag{I1.7}
\]

Dies folgt direkt aus

\[
A_T=I+\widetilde R_T^*\widetilde R_T.
\]

Damit lautet die korrekte Full-Rest-Zertifikatsfrage:

\[
\boxed{
h=\widetilde R_T^*Y+Z}
\tag{I1.8}
\]

mit Kontrolle von

\[
\|Y\|^2+\|Z\|^2.
\]

Die problematische Implikation

\[
\text{primitive certificate}
\Rightarrow
\text{full-rest upper bound}
\]

wird nicht mehr über eine Operatorordnung benutzt.

---

# 3. Der `a=0`-Kanal und das primitive Hauptstück

Setze

\[
c_{p,0}:=\sqrt{(\log p)(p-1)}.
\]

Aus (I1.3):

\[
(\widetilde R_Tf)_{p,0}
=
c_{p,0}
1_{\Omega_{p,0,T}}
\sum_{k\ge1}p^{-3k/4}K_{k\log p}f.
\tag{I1.9}
\]

Der `k=1`-Koeffizient ist

\[
c_{p,0}p^{-3/4}.
\]

Sein Quadrat ist

\[
(\log p)(p-1)p^{-3/2}
=
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right).
\]

Definiere daher wie C5c

\[
\boxed{
w_p:=\frac{\log p}{\sqrt p}\left(1-\frac1p\right).}
\tag{I1.10}
\]

Dann

\[
\boxed{
c_{p,0}p^{-3/4}=\sqrt{w_p}.}
\tag{I1.11}
\]

Somit zerfällt der volle `a=0`-Kanal exakt als

\[
\boxed{
(\widetilde R_Tf)_{p,0}
=
\underbrace{
\sqrt{w_p}
1_{\Omega_{p,0,T}}K_{\log p}f
}_{=:\,P_{p,T}f}
+
\underbrace{
 c_{p,0}1_{\Omega_{p,0,T}}
\sum_{k\ge2}p^{-3k/4}K_{k\log p}f
}_{=:\,E_{p,T}f}.
}
\tag{I1.12}
\]

`P_{p,T}` ist unter der kanonischen `\psi_{p,0}`-Identifikation exakt der primitive Restkanal, der in C5c/C5d verwendet wurde.

`E_{p,T}` ist nicht verworfen und nicht positiv herausgeschnitten; es ist der tatsächliche höhere Prime-Power-Tail **im selben vollen Martingalkanal**.

---

# 4. Uniforme Operatornorm des Future-Tails

Da

\[
K_s=P_TD_sE_T
\]

und `P_T,E_T` Kontraktionen sind sowie

\[
\|D_s\|\le2,
\]

gilt

\[
\boxed{\|K_s\|\le2.}
\tag{I1.13}
\]

Daher

\[
\begin{aligned}
\|E_{p,T}\|
&\le
2\sqrt{(\log p)(p-1)}
\sum_{k\ge2}p^{-3k/4}\\
&=
2\sqrt{(\log p)(p-1)}
\frac{p^{-3/2}}{1-p^{-3/4}}.
\end{aligned}
\]

Da `p>=2`, folgt mit absolutem `C`:

\[
\boxed{
\|E_{p,T}\|
\le
C\sqrt{\log p}\,p^{-1}.
}
\tag{I1.14}
\]

Nun betrachte nur die Future-Primes der C5c/C5d-Zertifikate. Sie erfüllen für ein festes `C_0`

\[
\frac12\log p\ge\frac T2-C_0,
\]

also

\[
p\ge e^{T-2C_0}.
\tag{I1.15}
\]

Sei

\[
E_T^{\rm fut}
:=
\bigoplus_{p\in\mathcal P_{\rm fut}(T)}E_{p,T}.
\]

Wegen der direkten Summe

\[
\|E_T^{\rm fut}\|^2
\le
\sum_{p\in\mathcal P_{\rm fut}(T)}
\|E_{p,T}\|^2.
\]

Mit (I1.14), und grob durch die Summe über alle ganzen Zahlen majorisiert,

\[
\begin{aligned}
\|E_T^{\rm fut}\|^2
&\le
C
\sum_{p\ge e^{T-2C_0}}
\frac{\log p}{p^2}\\
&\le
C
\sum_{n\ge e^{T-2C_0}}
\frac{\log n}{n^2}\\
&\le
C_{C_0}(T+1)e^{-T}.
\end{aligned}
\]

Damit

\[
\boxed{
\|E_T^{\rm fut}\|
\le
C_{C_0}\sqrt{T+1}\,e^{-T/2}.
}
\tag{I1.16}
\]

Dieser Satz benötigt keine zusätzliche PNT-Eingabe.

---

# 5. Lift eines primitiven Future-Zertifikats in den vollen Rest

Sei `\mathscr Y_{T,\rm prim}^{\rm fut}` der primitive Future-Zielraum aus C5c/C5d.

Unter der `\psi_{p,0}`-Identifikation ist er isometrisch mit dem `a=0`-Teil

\[
\mathscr Z_{T,0}^{\rm fut}
:=
\bigoplus_{p\in\mathcal P_{\rm fut}(T)}
L^2(\Omega_{p,0,T}).
\]

Bezeichne diese kanonische Isometrie mit

\[
\iota_T:
\mathscr Y_{T,\rm prim}^{\rm fut}
\to
\mathscr Z_{T,0}^{\rm fut}.
\]

Angenommen, ein C5c/C5d-Zertifikat hat die Form

\[
\boxed{
h=P_T^*Y+Z,}
\tag{I1.17}
\]

wobei `P_T=\bigoplus P_{p,T}` nur die verwendeten Future-Primes enthält.

Setze

\[
\widehat Y:=\iota_TY\in\mathscr Z_T
\]

und außerhalb des `a=0`-Future-Sektors `\widehat Y=0`.

Aus (I1.12):

\[
\widetilde R_T^*\widehat Y
=P_T^*Y+(E_T^{\rm fut})^*\widehat Y.
\]

Also

\[
\boxed{
h
=\widetilde R_T^*\widehat Y
+\widehat Z,}
\tag{I1.18}
\]

mit

\[
\boxed{
\widehat Z
:=
Z-(E_T^{\rm fut})^*\widehat Y.
}
\tag{I1.19}
\]

Für die Kosten gilt

\[
\begin{aligned}
\|\widehat Z\|^2
&\le
2\|Z\|^2
+2\|E_T^{\rm fut}\|^2\|\widehat Y\|^2.
\end{aligned}
\]

Da `\iota_T` isometrisch ist,

\[
\|\widehat Y\|=\|Y\|.
\]

Somit

\[
\boxed{
\|\widehat Y\|^2+\|\widehat Z\|^2
\le
(1+2\|E_T^{\rm fut}\|^2)\|Y\|^2
+2\|Z\|^2.
}
\tag{I1.20}
\]

Insbesondere bewahrt der Lift jede polynomial oder subexponentiell kontrollierte Zertifikatskostenskala.

---

# 6. Anwendung auf C5d

C5d konstruiert für jedes feste glatte gerade

\[
f\in C_c^\infty((-R,R))
\]

ein primitives Future-Zertifikat für den vollständigen Hubvektor

\[
h_{T,f}=H_T^*J_{R,T}f
\]

mit

\[
\boxed{
h_{T,f}=(R_T^{(1)})^*Y_{T,f}+Z_{T,f}}
\tag{I1.21}
\]

und

\[
\boxed{
\|Y_{T,f}\|^2+\|Z_{T,f}\|^2
\le
\frac{C_{R,f}}T
+C_{R,f}e^{-cT}.
}
\tag{I1.22}
\]

Die drei C5d-Komponenten werden sämtlich mit Future-Primes auf der Skala

\[
\frac12\log p\ge\frac T2-O(1)
\]

gescreent:

1. wachsender primitiver Block: C5c Future-Zellen mit `a_p>=T/2`;
2. fester primitive Small-Prime-Block: C5d Lemma C5d.1;
3. höherer Prime-Power-Hub: C5d Lemma C5d.1.

Daher ist §5 auf das gesamte `Y_{T,f}` anwendbar.

Es existieren also echte Full-Rest-Martingal-Zertifikate

\[
\boxed{
h_{T,f}=\widetilde R_T^*\widehat Y_{T,f}+\widehat Z_{T,f}}
\tag{I1.23}
\]

mit, wegen (I1.16),

\[
\boxed{
\|\widehat Y_{T,f}\|^2
+\|\widehat Z_{T,f}\|^2
\le
\frac{C'_{R,f}}T
+C'_{R,f}e^{-c'T}.
}
\tag{I1.24}
\]

Setze (I1.23) in die exakte Full-Rest-Dualform (I1.7) ein. Dann

\[
\boxed{
0\le
\sigma_T(J_{R,T}f)
\le
\frac{C'_{R,f}}T
+C'_{R,f}e^{-c'T}.
}
\tag{I1.25}
\]

Damit ist die zentrale C5d-Aussage wieder Full-Rest-zertifiziert:

\[
\boxed{
\sigma_T(J_{R,T}f)=O_{R,f}(T^{-1})
\qquad(f\text{ glatt und gerade}).
}
\tag{I1.26}
\]

Status:

\[
\boxed{[C5d.1]\quad\checkmark[M]_{\rm repaired\;full\text{-}rest}.}
\]

---

# 7. Wiederherstellung von C5d.2 und C5d.3

Die späteren C5d-Schritte benutzen nach C5d.1 keine primitive Formdomination mehr.

Aus Positivität der Schurform und Cauchy-Schwarz folgt für feste glatte gerade `f,g`:

\[
\boxed{
|\Sigma_T(f,g)|
\le
\frac{C_{R,f,g}}T+O(e^{-cT}).
}
\tag{I1.27}
\]

Damit

\[
\boxed{
q_T^X(J_{R,T}f,J_{R,T}g)
\to
q_{\Gamma,R}(f,g).
}
\tag{I1.28}
\]

Also

\[
\boxed{[C5d.2]\quad\checkmark[M]_{\rm restored}.}
\]

Für die Mosco-Konvergenz auf `\mathcal K_{X,R}^+` bleiben die ursprünglichen C5d-Argumente unverändert:

- Liminf aus
  \[
  \mathfrak q_{R,T}^+[f]\ge q_{\Gamma,R}(f)
  \]
  und schwacher Unterhalbstetigkeit;
- Limsup aus der dichten glatten geraden Core-Familie und (I1.28) mittels Diagonalfolge.

Daher

\[
\boxed{
\mathfrak q_{R,T}^+
\xrightarrow[M]{}
q_{\Gamma,R}^+.
}
\tag{I1.29}
\]

und somit

\[
\boxed{[C5d.3]\quad\checkmark[M]_{\rm restored}.}
\]

Die daraus in C5d gezogenen starken Resolventen- und negativen Potenzfolgen sind damit ebenfalls wieder auf der ursprünglichen Beweiskette verfügbar.

---

# 8. Rückwirkung auf O3a.1

O3a.1 benutzt zwei feste Richtungen:

1. eine ungerade Richtung mit
   \[
   \langle G_{R,U}f_-,f_-\rangle\to\infty;
   \]
2. eine gerade Richtung `f_+` mit beschränkter Zukunftsmetrik.

Durch (I1.26) gilt wieder

\[
\langle G_{R,U}f_+,f_+\rangle
=
q_{\Gamma,R}(f_+)
+O(U^{-1}),
\]

also bleibt der minimale Rayleighquotient nach oben durch eine feste Konstante beschränkt, während der maximale Rayleighquotient wegen der odd Richtung divergiert.

Daher ist der ursprüngliche Schluss wieder gültig:

\[
\boxed{
\forall T>R\text{ fest}:\qquad
\kappa(A^R_{T,U})\to\infty,
\qquad
\chi^R_{T,U}\to\infty
\quad(U\to\infty).
}
\tag{I1.30}
\]

Somit

\[
\boxed{[O3a.1]\quad\checkmark[M]_{\rm restored}.}
\]

O3a.2--O3a.4 waren bereits unangetastet.

---

# 9. Was ausdrücklich **nicht** bewiesen wurde

## FW1 — primitive Formdomination bleibt offen

Dieser Knoten beweist **nicht**

\[
R_T^*R_T\ge(R_T^{(1)})^*R_T^{(1)}.
\]

O3d-PRECHECK bleibt in dieser Aussage vollständig bestehen.

Der Repair umgeht die Frage durch den Gram-äquivalenten Full-Rest-Analyseoperator `\widetilde R_T`.

## FW2 — kein positiver `k=1`-Teilsummand

Aus (I1.12) wird nicht gefolgert

\[
\|\widetilde R_Tf\|^2\ge\|P_Tf\|^2.
\]

Der höhere Tail kann mit dem primitiven Term interferieren. Er wird ausschließlich **auf der Dualseite** als kleiner Adjungiertenfehler kontrolliert.

## FW3 — C1z-B1 primitive Lower-Extraktion bleibt offen

Die Reparatur von C5d ist asymmetrisch: Ein primitives **Dualzertifikat** kann wegen des kleinen Future-Tails perturbativ in ein Full-Rest-Zertifikat gehoben werden.

Daraus folgt keine allgemeine positive Lower-Extraktion

\[
\|R_Tf\|^2\ge\|R_T^{(1)}f\|^2.
\]

Daher bleibt der in der PRECHECK-Reconciliation gesetzte Dependency-Status für die C1z-B1-Lower-Extraktion bestehen.

## FW4 — odd matching upper bound bleibt offen

Dieser Knoten repariert den geraden C5d-Core und die darauf beruhende O3a.1-Aussage.

Noch nicht bewiesen ist für festen glatten ungeraden Test `f_-` mit erstem nichtverschwindendem Boundary-Jet `m(f_-)`:

\[
\sigma_T(J_{R,T}f_-)
\lesssim
\frac{e^T}{T^{2m(f_-)+2}}.
\]

O3c liefert weiterhin nur die scharfe Kandidaten-Lower-Skala

\[
\sigma_T(J_{R,T}f_-)
\gtrsim
\frac{e^T}{T^{2m(f_-)+2}}.
\]

Der nächste zulässige O3d-Unterknoten muss die **signed mean-zero Future-Edge-Konstruktion direkt im Full-Rest-Martingalmodell** ausführen.

---

# 10. Autoritative Statusmatrix nach O3d-I1

| Objekt | Status nach PRECHECK-Reconciliation | Status nach O3d-I1 |
|---|---:|---:|
| primitive Formdomination | `?[O]` | `?[O]` unverändert |
| C1z-B1 primitive Lower-Extraktion | `?[O]_dependency` | `?[O]_dependency` unverändert |
| C5d primitives Future-Zertifikat als primitives Statement | `✓[M]` | `✓[M]` |
| C5d.1 full-rest even Schur tail | `?[O]_dependency` | `✓[M] repaired` |
| C5d.2 even form/Gamma limit | `?[O]_dependency` | `✓[M] restored` |
| C5d.3 even Mosco/resolvent route | `?[O]_dependency` | `✓[M] restored` |
| O3a.1 full-space conditioning no-go | `?[O]_C5d dependency` | `✓[M] restored` |
| O3a.2--O3a.4 | `✓[M]` | `✓[M]` |
| O3b.1 | `✓[M]` | `✓[M]` |
| O3c full-rest constant-mode bound / odd lower certificate | `✓[M]` | `✓[M]` |
| O3d odd matching upper bound | `?[O]` | `?[O]` |

---

# 11. Nächster atomarer Auftrag

Der nächste zulässige Unterknoten ist

\[
\boxed{
[P11\text{-}O3d\text{-}I2]
\quad
\text{Signed Mean-Zero Future-Edge Certificate on the Full-Rest Martingale Target}.
}
\]

Zu zeigen ist für festen glatten ungeraden `f_-`:

1. exakte Boundary-Zerlegung des even Hubfunktionals in Mittelwert + mean-zero Kernel;
2. Source-Rest für den Mittelwert mit Kosten
   \[
   O\!\left(e^T/T^{2m(f_-)+2}\right);
   \]
3. signed Future-Edge-Dualzertifikat für den mean-zero Kernel;
4. Lift desselben über den hier bewiesenen Full-Rest-`a=0`-Perturbationsmechanismus;
5. daraus die matching upper bound
   \[
   \sigma_T(Jf_-)
   \lesssim
   e^T/T^{2m(f_-)+2}.
   \]

Kein Schluss auf `\kappa(A_- )` wird vor Abschluss dieses I2-Satzes gebucht.
