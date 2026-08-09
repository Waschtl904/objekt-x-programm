# P11-C1z-B1 — Source-windowed Gamma-Hub-Feshbach nach finite-adischer Konditionierung

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1z-B1]`  
**Vorgänger:** C1d, C1w, C1y, C1q-CORR, C1z-B  
**Status:**

\[
\boxed{[P11\text{-}C1z\text{-}B1]\quad\checkmark[K/M]_{\rm part}}
\]

---

## 0. Urteil

C1z-B1 führt die in C1z-B verlangte „Chirurgie nur noch am neutralen Hub“ erstmals als echte Operator-Feshbach-Konstruktion aus.

Der zentrale neue Befund lautet:

\[
\boxed{
\text{Nach source-windowed Gamma-Präkonditionierung besitzt das effektive Hub-Schurkomplement}
\text{ auf jedem festen Source-Level }R\text{ eine kompakte Inverse.}
}
\]

Äquivalent ist das normalisierte Hub-Schurkomplement eine positive kompakte Störung der Identität.

Damit wird die in C1y ausgeschlossene Klasse translationsinvarianter Multiplikatorregulatoren tatsächlich verlassen: Die positive Gamma-Inzidenz wird **nicht** auf dem ganzen Haar-\(L^2(\mathbb R)\) als Fouriermultiplikator benutzt, sondern über Nullfortsetzung auf den festen Source-Raum

\[
\mathscr H_R:=L^2(-R,R)
\]

komprimiert. Die Source-Grenze bricht Translationinvarianz; gleichzeitig erzwingt das Anwachsen des Gamma-Symbols im Frequenzraum eine kompakte Einbettung der Gamma-Formdomäne in \(L^2(-R,R)\).

Es entsteht dadurch ein echter endlicher Fredholm-/Kompaktheitsbaustein:

\[
\boxed{
C_{\Gamma,R}^{-1/2}F_R^{\rm hub}C_{\Gamma,R}^{-1/2}
=I+K_R(I+R_R^*R_R)^{-1}K_R^*,
}
\]

wobei \(K_R\) kompakt ist.

**Aber:** Dies schließt weder P10-O07 noch Objekt X. Insbesondere bleiben offen:

1. ein uniformer oder konvergenter Grenzübergang \(R\to\infty\);
2. eine konkrete Schattenklasse (insbesondere der P10-O07-\(S_4/S_2\)-Scope);
3. die exakte Identifikation des Schurkomplements mit der vollständigen Weilform;
4. die negative Gamma-Konstante \(A_\infty(0)\) und der Poldefekt;
5. Mosco-/Resolventenkompatibilität zwischen verschiedenen Source-Leveln.

Außerdem präzisiert C1z-B1 den vorherigen Sprachgebrauch: C1z-B macht den finite-adischen Rest auf jedem festen \(R\) endlich/source-lokal, aber **nicht bereits uniform beschränkt für \(R\to\infty\)**. Der konditionierte Rest muss im Feshbach-Nenner erhalten bleiben.

---

# 1. Verbindliche Ausgangsdaten

## 1.1 Source-Level

Für \(R>0\) setze

\[
\boxed{\mathscr H_R:=L^2(-R,R).}
\]

Sei

\[
E_R:\mathscr H_R\to L^2(\mathbb R)
\]

die Nullfortsetzung und

\[
P_R:=E_R^*:L^2(\mathbb R)\to\mathscr H_R
\]

die Restriktion auf \((-R,R)\).

Dann

\[
P_RE_R=I_{\mathscr H_R},
\qquad
E_RP_R=M_{1_{(-R,R)}}.
\]

Die Source-induzierte Prime-Power-Menge aus C1f/C1m lautet

\[
\boxed{
\mathcal N_R:=\{p^k:p^k\le e^{2R}\}.
}
\]

Sie ist für jedes feste \(R\) endlich.

---

## 1.2 Analytische Kantenoperatoren

Wie in C1c/C1d:

\[
\boxed{D_s:=U_{s/2}-U_{-s/2}.}
\]

Für \(n=p^k\) ist die Kantenlänge

\[
\ell_n=\log n=k\log p
\]

und das exakte positive Weil-Inzidenzgewicht

\[
\lambda_n=\frac{\Lambda(n)}{\sqrt n}
=\frac{\log p}{p^{k/2}}.
\]

---

## 1.3 BC-Sternzerlegung

Aus C1n/C1r:

\[
\zeta_{p^k}=p^{-k/2}\zeta_1+\eta_{p,k},
\qquad
\eta_{p,k}\in K_p^0,
\]

mit

\[
K_p^0\perp K_q^0\quad(p\ne q).
\]

C1z-B konstruiert einen source-gekoppelten finite-adischen Projektor \(\mathsf Q_R(u)\), der \(\zeta_1\) fixiert und die p-adischen Martingalstufen abhängig von \(u\) und \(R\) abschneidet.

Die zentrale Unitalitätsfirewall lautet

\[
\boxed{\mathsf Q_R(u)\zeta_1=\zeta_1.}
\]

---

# 2. Der verbleibende neutrale Huboperator

Der Hubkoeffizient eines Labels \(n\) ist

\[
\sqrt{\lambda_n}\,\langle\zeta_1,\zeta_n\rangle
=\sqrt{\lambda_n}\,n^{-1/2}.
\]

Für \(n=p^k\):

\[
\sqrt{\lambda_{p^k}}p^{-k/2}
=\sqrt{\log p}\,p^{-3k/4}.
\]

Definiere deshalb den **source-windowed neutralen Huboperator**

\[
\boxed{
H_R
:=
P_R
\sum_{n\in\mathcal N_R}
\sqrt{\Lambda(n)}\,n^{-3/4}
D_{\log n}
E_R
:\mathscr H_R\to\mathscr H_R.
}
\tag{C1zB1.1}
\]

Da \(\mathcal N_R\) endlich ist und jedes \(D_s\) beschränkt ist, ist \(H_R\) für jedes feste \(R\) ein beschränkter Operator.

Der höhere Prime-Power-Tail \(k\ge2\) ist wie in C1w/C1q-CORR absolut harmlos; der kritische aligned Hub stammt aus \(k=1\):

\[
\boxed{
H_R^{(1)}
=
P_R\sum_{p\le e^{2R}}
\sqrt{\log p}\,p^{-3/4}D_{\log p}E_R.
}
\tag{C1zB1.2}
\]

---

# 3. Der konditionierte Restoperator

C1z-B definiert nach der p-adischen Martingalkonditionierung einen finite-adischen Restanalyseoperator. Wir bezeichnen seine Restriktion auf das Source-Level abstrakt mit

\[
\boxed{
R_R:=\mathcal T_{R,{\rm res}}^{\bowtie}
:\mathscr H_R\longrightarrow\mathscr Y_R^0,
}
\tag{C1zB1.3}
\]

wobei \(\mathscr Y_R^0\) der von den auf Level \(R\) tatsächlich überlebenden p-adischen Reststufen erzeugte Hilbertraum ist.

Für jedes feste \(R\) ist die aktive Label-/Martingalmenge endlich; daher ist \(R_R\) eine endliche Summe beschränkter Translation-/Multiplikationskanäle und somit beschränkt.

**Wichtig:** „endlich auf festem \(R\)“ ist nicht dasselbe wie „uniform in \(R\) beschränkt“. Dieser Punkt wird jetzt separat geprüft.

---

# 4. Scope-Präzisierung: Der konditionierte Rest ist nicht schon global beschränkt

Fixiere

\[
0\ne a\in C_c^\infty((-r,r))
\]

für ein festes \(r>0\).

Für den primitiven Restkanal \(k=1\) gilt aus C1z-B

\[
\mathsf Q_R(u)\eta_{p,1}
=
1_{\{|u|\le R-\tfrac12\log p\}}\eta_{p,1}.
\]

Die Träger von

\[
D_{\log p}a
\]

liegen in zwei Intervallen um \(\pm\frac12\log p\) mit Radius \(r\). Falls

\[
\boxed{\log p+r\le R,}
\tag{C1zB1.4}
\]

liegt der gesamte Träger von \(D_{\log p}a\) im Bereich, auf dem der Indikator in C1z-B gleich eins ist.

Für zusätzlich

\[
\log p>2r
\]

sind die beiden verschobenen Kopien disjunkt und

\[
\|D_{\log p}a\|_2^2=2\|a\|_2^2.
\]

Da die \(K_p^0\)-Sektoren für verschiedene Primzahlen orthogonal sind, folgt die Untergrenze

\[
\begin{aligned}
\|R_Ra\|^2
&\ge
2\|a\|_2^2
\sum_{e^{2r}<p\le e^{R-r}}
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right).
\end{aligned}
\tag{C1zB1.5}
\]

Mit PNT/partieller Summation wächst die Primreihe in der Größenordnung \(\sqrt X\) bei \(X=e^{R-r}\). Insbesondere

\[
\boxed{
\|R_Ra\|^2\to\infty
\qquad(R\to\infty).
}
\tag{C1zB1.6}
\]

### Konsequenz

C1z-B hat korrekt bewiesen:

\[
\boxed{R_R\text{ ist für jedes feste }R\text{ endlich/source-lokal}.}
\]

Nicht bewiesen — und nach (C1zB1.6) für die direkte Norm sogar falsch — ist:

\[
\sup_R\|R_Ra\|<\infty
\]

für jedes feste nichttriviale \(a\).

Damit bleibt der konditionierte Rest **notwendiger Bestandteil des Schur-Nenners**. C1z-B1 ersetzt ihn nicht durch null.

Status: `✓[M]` Scope-Präzisierung; keine Korrektur der expliziten C1z-B-Statusmatrix nötig, da dort nur Endlichkeit für festes \(R\) behauptet wurde.

---

# 5. No-Go: Ein Source-Fenster allein reguliert den Hub nicht

Man könnte versuchen, nur den Ausgang auf \((-R,R)\) zu schneiden, also den bereits in (C1zB1.1) eingebauten Faktor \(P_R\) als Regulator zu interpretieren.

Das reicht nicht.

Für das oben fixierte \(a\in C_c^\infty((-r,r))\) und jede Primzahl mit

\[
\frac12\log p+r\le R
\]

gilt

\[
P_RD_{\log p}E_Ra=D_{\log p}a.
\]

Also lässt das Source-Fenster auf allen Primblöcken

\[
p\le e^{2(R-r)}
\]

die alte C1q-CORR-Geometrie **exakt unverändert**.

Wählt man innerhalb dieses Bereichs enge multiplikative Primblöcke

\[
X\le p\le(1+\varepsilon)X,
\qquad
(1+\varepsilon)X\le e^{2(R-r)},
\]

so greift der C1q-CORR-Blockmechanismus unverändert: Die positiven bzw. negativen Translationszentren liegen jeweils in einem kurzen Intervall und erzeugen große kohärente Blockinkremente.

Die \(k\ge2\)-Hubkoeffizienten sind absolut summierbar und können diesen primitiven Blockmechanismus nicht als globalen Tail kompensieren.

Daher:

\[
\boxed{
\text{reines Output-Windowing }P_R
\text{ beseitigt den aligned Hubtail nicht.}
}
\tag{C1zB1.7}
\]

Dies ist der gezielte Z-A-No-Go im jetzt relevanten Hub-Scope.

---

# 6. Der positive Gamma-Inzidenzoperator auf dem Source-Level

C1d schreibt den positiven Gammaanteil als

\[
\mathcal E_\infty(f,f)
=
\int_0^\infty
\omega_\infty(s)\|D_sf\|_2^2\,ds,
\]

mit

\[
\omega_\infty(s)=\frac{e^{-s/2}}{1-e^{-2s}}>0.
\]

Unter Fouriertransformation besitzt diese Form den nichtnegativen Multiplikator

\[
\boxed{
g_\infty(\xi)
:=A_\infty(\xi)-A_\infty(0)\ge0.
}
\tag{C1zB1.8}
\]

Aus der C1d-Reihenform mit

\[
a_j=j+\frac14
\]

folgt explizit

\[
\boxed{
g_\infty(\xi)
=
\sum_{j=0}^\infty
\frac{\xi^2/4}{a_j(a_j^2+\xi^2/4)}.
}
\tag{C1zB1.9}
\]

Jeder Summand ist als Funktion von \(|\xi|\) monoton wachsend.

Außerdem gilt

\[
\boxed{g_\infty(\xi)\longrightarrow\infty
\qquad(|\xi|\to\infty).}
\tag{C1zB1.10}
\]

### Beweis von (C1zB1.10)

Fixiere \(N\). Für jedes \(0\le j\le N\):

\[
\frac{\xi^2/4}{a_j(a_j^2+\xi^2/4)}
\longrightarrow\frac1{a_j}.
\]

Somit

\[
\liminf_{|\xi|\to\infty}g_\infty(\xi)
\ge
\sum_{j=0}^N\frac1{a_j}.
\]

Da die rechte Seite mit \(N\to\infty\) divergiert, folgt (C1zB1.10). `□`

Dieser Beweis benötigt keine RH-Annahme.

---

# 7. Source-windowed Gammaform

Auf \(\mathscr H_R=L^2(-R,R)\) definiere

\[
\boxed{
\mathfrak c_{\Gamma,R}[f,g]
:=
\langle f,g\rangle_{\mathscr H_R}
+
\int_0^\infty
\omega_\infty(s)
\langle D_sE_Rf,D_sE_Rg\rangle_{L^2(\mathbb R)}\,ds.
}
\tag{C1zB1.11}
\]

Äquivalent per Plancherel:

\[
\boxed{
\mathfrak c_{\Gamma,R}[f,f]
=
\frac1{2\pi}
\int_{\mathbb R}
\bigl(1+g_\infty(\xi)\bigr)
|\widehat{E_Rf}(\xi)|^2\,d\xi.
}
\tag{C1zB1.12}
\]

Die Formdomäne ist

\[
\mathcal D_{\Gamma,R}
:=
\left\{
f\in\mathscr H_R:
\int
(1+g_\infty(\xi))
|\widehat{E_Rf}(\xi)|^2d\xi<\infty
\right\}.
\]

Sie enthält \(C_c^\infty(-R,R)\) und ist daher dicht.

Da der gewichtete Fourier-\(L^2\)-Raum vollständig ist und \(E_R\) eine Isometrie auf den geschlossenen Unterraum der in \([-R,R]\) getragenen Funktionen ist, ist \(\mathfrak c_{\Gamma,R}\) geschlossen.

Außerdem

\[
\mathfrak c_{\Gamma,R}[f,f]\ge\|f\|_2^2.
\]

Daher existiert der zugehörige positive selbstadjungierte Operator

\[
\boxed{C_{\Gamma,R}\ge I.}
\tag{C1zB1.13}
\]

**Firewall:** Verwendet wird nur der positive Gamma-Inzidenzanteil plus die feste Hintergrundnorm. Der negative skalare Term \(A_\infty(0)\|f\|^2\) aus der vollständigen Gammaform wird hier nicht stillschweigend positiv gemacht.

---

# 8. Hauptlemma: Die Gamma-Formeinbettung auf \((-R,R)\) ist kompakt

## Satz C1zB1.1

Die Einbettung

\[
\boxed{
(\mathcal D_{\Gamma,R},\|\cdot\|_{\mathfrak c_{\Gamma,R}})
\hookrightarrow
\mathscr H_R
}
\tag{C1zB1.14}
\]

ist kompakt.

### Beweis

Sei \((f_m)\) in der Gamma-Formnorm beschränkt:

\[
\sup_m\mathfrak c_{\Gamma,R}[f_m,f_m]\le C.
\]

Setze \(F_m:=E_Rf_m\).

### Schritt 1 — uniforme Hochfrequenzkontrolle

Wegen der Monotonie von \(g_\infty\) in \(|\xi|\):

\[
\begin{aligned}
\frac1{2\pi}
\int_{|\xi|>M}|\widehat F_m(\xi)|^2d\xi
&\le
\frac{C}{1+g_\infty(M)}.
\end{aligned}
\]

Nach (C1zB1.10) geht die rechte Seite für \(M\to\infty\) gleichmäßig in \(m\) gegen null.

### Schritt 2 — der Niederfrequenzanteil ist kompakt

Für festes \(M\) betrachte

\[
T_{R,M}:\mathscr H_R\to L^2([-M,M]),
\qquad
(T_{R,M}f)(\xi)=\widehat{E_Rf}(\xi).
\]

Der Integralkern lautet

\[
K(\xi,u)=e^{i\xi u},
\qquad
(\xi,u)\in[-M,M]\times[-R,R].
\]

Damit

\[
\int_{-M}^M\int_{-R}^R|K(\xi,u)|^2du\,d\xi
=4MR<\infty.
\]

Also ist \(T_{R,M}\) Hilbert-Schmidt und insbesondere kompakt.

Der niederfrequente Anteil jeder formbeschränkten Folge besitzt daher eine konvergente Teilfolge.

### Schritt 3 — Zusammenfügen

Wähle zunächst \(M\) so groß, dass der Hochfrequenzanteil gleichmäßig kleiner als \(\varepsilon\) ist. Ziehe dann eine konvergente Teilfolge für den Niederfrequenzanteil. Plancherel liefert, dass diese Teilfolge in \(L^2(\mathbb R)\) und damit nach Restriktion in \(\mathscr H_R\) Cauchy ist.

Damit ist die Einbettung kompakt. `□`

---

# 9. Konsequenz: kompakte Gamma-Inverse

Aus Satz C1zB1.1 und \(C_{\Gamma,R}\ge I\) folgt

\[
\boxed{C_{\Gamma,R}^{-1}\in\mathcal K(\mathscr H_R).}
\tag{C1zB1.15}
\]

Ebenso ist per Funktionalkalkül

\[
\boxed{C_{\Gamma,R}^{-1/2}\in\mathcal K(\mathscr H_R).}
\tag{C1zB1.16}
\]

Hier bezeichnet \(\mathcal K\) die Klasse der kompakten Operatoren.

Dies ist der entscheidende Unterschied zum globalen C1y-Gammaoperator: Auf dem ganzen \(L^2(\mathbb R)\) ist der Gammaoperator ein translationsinvarianter Multiplikator und liefert keine Kompaktheit; auf dem festen Source-Level erzeugt die **Kombination aus Frequenzwachstum und räumlich beschränkter Quelle** eine kompakte Resolventengeometrie.

---

# 10. Gamma-präkonditionierter Hub

Definiere

\[
\boxed{
K_R
:=
C_{\Gamma,R}^{-1/2}H_R
:\mathscr H_R\to\mathscr H_R.
}
\tag{C1zB1.17}
\]

Da \(H_R\) beschränkt und \(C_{\Gamma,R}^{-1/2}\) kompakt ist,

\[
\boxed{K_R\in\mathcal K(\mathscr H_R).}
\tag{C1zB1.18}
\]

Dies ist bereits ein echter positiver Kompaktheitsgewinn: Der neutralen Prime-Hubinzidenz wird keine frei gewählte Labeldämpfung aufgeprägt. Stattdessen wird sie durch die **bereits vorhandene archimedische Gamma-Energie auf demselben Source-Fenster** präkonditioniert.

---

# 11. Exakte Operator-Feshbach-Identität

Betrachte den gemeinsamen Quellenoperator

\[
\boxed{
V_R:
\mathscr H_R\to
\mathscr H_R\oplus\mathscr Y_R^0,
\qquad
V_Rf=(H_Rf,R_Rf).
}
\tag{C1zB1.19}
\]

Auf dem Zielraum führe die positive Blockmetrik

\[
\boxed{
\mathbb B_R
:=
\begin{pmatrix}
C_{\Gamma,R}&0\\
0&I
\end{pmatrix}
+V_RV_R^*.
}
\tag{C1zB1.20}
\]

Als geschlossene positive Form ist dies wohldefiniert; der bounded Term \(V_RV_R^*\) ist eine Formstörung des coerciven Gamma-/Identitätsblocks.

Die Blockform lautet formal

\[
\mathbb B_R
=
\begin{pmatrix}
C_{\Gamma,R}+H_RH_R^*&H_RR_R^*\\
R_RH_R^*&I+R_RR_R^*
\end{pmatrix}.
\]

Da

\[
I+R_RR_R^*\ge I,
\]

ist der Restblock beschränkt invertierbar.

Das Hub-Schurkomplement ist

\[
\begin{aligned}
F_R^{\rm hub}
={}&C_{\Gamma,R}+H_RH_R^*\\
&-H_RR_R^*(I+R_RR_R^*)^{-1}R_RH_R^*.
\end{aligned}
\]

Mit der Standardidentität

\[
I-R_R^*(I+R_RR_R^*)^{-1}R_R
=(I+R_R^*R_R)^{-1}
\]

folgt exakt

\[
\boxed{
F_R^{\rm hub}
=
C_{\Gamma,R}
+H_R(I+R_R^*R_R)^{-1}H_R^*.
}
\tag{C1zB1.21}
\]

Dies ist die operatorielle, nicht-faserweise Version der alten C1w-Rechnung.

**Wichtig:** Der konditionierte Rest wird nicht verworfen. Seine gesamte Wirkung erscheint positiv im source-seitigen Nenner

\[
(I+R_R^*R_R)^{-1}.
\]

---

# 12. Normalisierte Feshbachform = Identität + positiver kompakter Operator

Setze

\[
A_R:=(I+R_R^*R_R)^{-1},
\qquad
0<A_R\le I.
\]

Dann

\[
\begin{aligned}
C_{\Gamma,R}^{-1/2}
F_R^{\rm hub}
C_{\Gamma,R}^{-1/2}
&=
I+K_RA_RK_R^*.
\end{aligned}
\]

Also

\[
\boxed{
\widetilde F_R^{\rm hub}
:=
C_{\Gamma,R}^{-1/2}
F_R^{\rm hub}
C_{\Gamma,R}^{-1/2}
=I+S_R,
}
\tag{C1zB1.22}
\]

mit

\[
\boxed{
S_R:=K_RA_RK_R^*\ge0.
}
\tag{C1zB1.23}
\]

Da \(K_R\) kompakt und \(A_R\) beschränkt ist,

\[
\boxed{S_R\in\mathcal K(\mathscr H_R).}
\tag{C1zB1.24}
\]

Damit ist das normalisierte effektive Hub-Schurkomplement eine **positive kompakte Störung der Identität**.

Insbesondere

\[
\boxed{
(\widetilde F_R^{\rm hub})^{-1}-I
=-(I+S_R)^{-1}S_R
\in\mathcal K(\mathscr H_R).
}
\tag{C1zB1.25}
\]

Dies ist ein echter endlicher Fredholm-Baustein.

---

# 13. Stärker: Das unnormalisierte Hub-Schurkomplement besitzt kompakte Inverse

Aus (C1zB1.22):

\[
F_R^{\rm hub}
=
C_{\Gamma,R}^{1/2}(I+S_R)C_{\Gamma,R}^{1/2}.
\]

Daher

\[
\boxed{
(F_R^{\rm hub})^{-1}
=
C_{\Gamma,R}^{-1/2}
(I+S_R)^{-1}
C_{\Gamma,R}^{-1/2}.
}
\tag{C1zB1.26}
\]

Beide äußeren Faktoren sind kompakt, der mittlere Faktor ist beschränkt. Somit

\[
\boxed{
(F_R^{\rm hub})^{-1}
\in\mathcal K(\mathscr H_R).
}
\tag{C1zB1.27}
\]

Also besitzt \(F_R^{\rm hub}\) auf jedem festen Source-Level eine kompakte Resolventengeometrie / diskrete effektive Hub-Spektralstruktur.

Status: `✓[K/M]` für festes \(R\).

---

# 14. Das Rest-Schurkomplement

Eliminiert man stattdessen den Gamma-Hub, erhält man

\[
\begin{aligned}
F_R^{\rm rest}
={}&I+R_RR_R^*\\
&-R_RH_R^*(C_{\Gamma,R}+H_RH_R^*)^{-1}H_RR_R^*.
\end{aligned}
\]

Mit der Woodbury-/Push-through-Identität folgt

\[
\boxed{
F_R^{\rm rest}
=
I+
R_R
\bigl(I+H_R^*C_{\Gamma,R}^{-1}H_R\bigr)^{-1}
R_R^*.
}
\tag{C1zB1.28}
\]

Dies zeigt präzise, wie die Gamma-Hubgeometrie auf den konditionierten Rest zurückwirkt:

\[
\boxed{
\text{Restenergie wird durch die positive source-Metrik }
I+H_R^*C_{\Gamma,R}^{-1}H_R
\text{ gescreent.}
}
\]

Für jedes feste \(R\) ist dies wohldefiniert und positiv.

Ein uniformer Bound von

\[
\left\|
R_R
(I+H_R^*C_{\Gamma,R}^{-1}H_R)^{-1/2}
\right\|
\]

für \(R\to\infty\) wird hier **nicht** behauptet. Genau dies ist nun eine der scharfen Grenzfragen.

---

# 15. Warum C1y nicht greift

C1y schließt positive Regulatoren aus, die auf dem globalen analytischen Raum mit allen Translationen \(U_t\) kommutieren. Der dortige Gammaoperator ist Fourier-diagonal.

C1z-B1 benutzt stattdessen die Form

\[
\mathfrak c_{\Gamma,R}[f,g]
=
\langle f,g\rangle
+\mathcal E_\infty(E_Rf,E_Rg)
\]

auf einem **festen Source-Intervall**.

Für generisches \(t\ne0\) ist

\[
U_tE_R\mathscr H_R
\not\subset E_R\mathscr H_R.
\]

Die Nullfortsetzungs-/Restriktionsgeometrie ist daher nicht translationsinvariant.

Äquivalent besitzt die komprimierte Gammaform keinen globalen Fourier-Fasermultiplikator auf \(\mathscr H_R\).

Somit liegt

\[
\boxed{C_{\Gamma,R}\text{ außerhalb des C1y-Kommutanten-Scope}.}
\tag{C1zB1.29}
\]

C1y wird nicht widerlegt; seine Scope-Firewall wird respektiert.

---

# 16. Bezug zur exakten Weilform

C1z-B1 benutzt ausschließlich bereits vorhandene Bausteine:

1. die exakten Weil-Lokalgewichte \(\lambda_n=\Lambda(n)/\sqrt n\);
2. den exakt aus der BC-GCD-Geometrie erzwungenen neutralen Faktor \(n^{-1/2}\);
3. die C1z-B-p-adische source-Konditionierung im Rest;
4. die positive Gamma-Inzidenzenergie aus C1d;
5. die feste Source-Grenze \((-R,R)\).

Es wird **kein** neuer additiver Weil-Kreuzterm eingeführt.

Insbesondere bleibt die NEU-250/P10-Firewall intakt:

\[
\boxed{
\text{Das Schurkomplement ist eine Kompression einer größeren positiven Geometrie,}
\text{kein zusätzlich zu }B_W\text{ addierter Mischsummand.}
}
\]

Aber ebenso wichtig:

\[
\boxed{
F_R^{\rm hub}\ne B_W|_{(-R,R)}
\text{ ist hier nicht bewiesen.}
}
\]

Die vollständige Weilform enthält weiterhin

- den negativen Gamma-Grundterm \(A_\infty(0)\langle\cdot,\cdot\rangle\),
- den kompensierten Prime-Baseline-Defekt,
- den positiven und negativen Polkanal.

C1z-B1 beweist daher eine **positive Kompressionsarchitektur**, keine Weil-Positivität.

---

# 17. Erster echter P10-O07-Kontakt — aber noch kein Abschluss

C1w/C1y scheiterten im O07-Scope bereits auf endlichem \(R\), weil der effektive Huboperator Fourier-diagonal blieb und daher auf dem nichtatomaren globalen \(L^2\) nicht kompakt war.

C1z-B1 liefert dagegen auf jedem festen \(R\):

\[
\boxed{
(\widetilde F_R^{\rm hub})^{-1}-I\in\mathcal K,
\qquad
(F_R^{\rm hub})^{-1}\in\mathcal K.
}
\]

Damit ist erstmals in P11 ein **source-kanonischer endlicher Kompaktheits-/Fredholm-Mechanismus** konstruiert, der nicht bloß aus einer endlichen Matrix im Labelraum stammt.

P10-O07 bleibt dennoch OPEN, denn nicht bewiesen sind:

1. \(S_R\in S_4\) oder irgendeine konkrete finite Schattenklasse;
2. der behauptete/gesuchte Ausschluss \(S_2\) im relevanten globalen Modell;
3. ein kompatibler Grenzoperator bei \(R\to\infty\);
4. Schattennormkontrolle uniform in \(R\);
5. Determinanten-/Fredholmgrenzwerte.

Status:

\[
\boxed{\text{O07: erster finite-level compactness contact, weiterhin }?[O].}
\]

---

# 18. Was C1z-B1 ausdrücklich nicht beweist

C1z-B1 beweist **nicht**:

1. RH;
2. \(B_W\ge0\);
3. Existenz von Objekt X;
4. globale Konvergenz des positiven Syntheseoperators;
5. uniforme Beschränktheit des konditionierten Restes;
6. uniforme Beschränktheit des Huboperators;
7. einen \(R\to\infty\)-Grenzwert von \(F_R^{\rm hub}\);
8. eine Schattenklassenzugehörigkeit;
9. Mosco-/starke Resolventenkonvergenz;
10. Identifikation des endlichen Schurkomplements mit Suzukis \(A_a\) oder \(T_{a,\lambda}\);
11. einen operatoriellen Finite Part des Prime-Baseline-Defekts.

Insbesondere wird die globale Positivitätsfrage nicht in einer neuen Verkleidung als bereits gelöst ausgegeben.

---

# 19. Statusmatrix

| Aussage | Status |
|---|---|
| C1z-B-Rest ist für jedes feste \(R\) source-lokal endlich | `✓[K/M]` aus C1z-B |
| C1z-B-Rest ist uniform in \(R\) normbeschränkt | `×[M]` im direkten Normscope |
| reines Source-Window \(P_R\) reguliert aligned Hubtail | `×[M]` |
| \(g_\infty\ge0\) und \(g_\infty(|\xi|)\to\infty\) | `✓[K/M]` |
| source-windowed Gammaform geschlossen und coerciv | `✓[K/M]` |
| Gamma-Formdomäne kompakt in \(L^2(-R,R)\) eingebettet | `✓[K/M]` |
| \(C_{\Gamma,R}^{-1}\) kompakt | `✓[K/M]` |
| Gamma-präkonditionierter Hub \(K_R\) kompakt | `✓[K/M]` |
| exakte Operator-Feshbach-Identität (C1zB1.21) | `✓[K/M]` |
| normalisierter Hub-Schurterm = \(I+\) positiver kompakter Operator | `✓[K/M]` |
| \((F_R^{\rm hub})^{-1}\) kompakt für festes \(R\) | `✓[K/M]` |
| C1y-Translations-No-Go anwendbar | `×[M]` — Scope verlassen |
| konkrete Schattenklasse | `?[O]` |
| uniformer \(R\to\infty\)-Grenzwert | `?[O]` |
| exakte Weilform = C1z-B1-Schurkomplement | `?[O]` / nicht bewiesen |
| P10-O07 geschlossen | `?[O]` — nein |

---

# 20. Strukturelle Einordnung

Nach C1z-B1 lautet die bisher präziseste P11-Architektur:

\[
\boxed{
\text{adelische Quelle}
\longrightarrow
\text{source-gekoppelte p-adische Konditionierung}
\longrightarrow
\text{BC-Hub/Rest-Spaltung}
\longrightarrow
\text{source-windowed Gamma-Präkonditionierung}
\longrightarrow
\text{Operator-Feshbach}.
}
\]

Der entscheidende Fortschritt gegenüber C1w ist nicht ein besser gewählter Skalar, sondern ein Wechsel der Kategorie:

\[
\boxed{
\text{Fourier-faserweise Algebra}
\quad\longrightarrow\quad
\text{nichttranslationinvariante Source-Operatorgeometrie}.}
\]

Und der entscheidende Fortschritt gegenüber C1z-B allein ist:

\[
\boxed{
\text{finite source-lokale Restgeometrie}
\quad\longrightarrow\quad
\text{echte kompakte effektive Hub-Resolventengeometrie auf jedem festen }R.
}
\]

Dies ist noch nicht Objekt X, aber erstmals entsteht genau die Art von Operatorphänomen — kompakte Resolventengeometrie nach kanonischer Kompression — die im früheren rein translationsinvarianten P11-Pfad strukturell unmöglich war.

---

# 21. Nächster atomarer Knoten

Der nächste Knoten darf jetzt nicht wieder die gesamte Konstruktion neu erfinden. Zwei konkrete Fragen sind übrig:

\[
\boxed{
[P11\text{-}C1z\text{-}B2]
\quad
\text{Schatten- und Large-}R\text{-Audit des Gamma-präkonditionierten Hub-Schurterms}.}
\]

Zu prüfen sind getrennt:

### B2-A — finite-level Schattenprofil

Für

\[
S_R=K_R(I+R_R^*R_R)^{-1}K_R^*
\]

bestimme, ob irgendeine source-kanonische Aussage

\[
S_R\in S_p
\]

folgt, insbesondere im P10-O07-relevanten Bereich.

### B2-B — Large-\(R\)-Screening

Untersuche

\[
H_R(I+R_R^*R_R)^{-1/2}
\]

beziehungsweise

\[
K_R(I+R_R^*R_R)^{-1/2}
\]

auf festen kompakten Testfunktionen und auf Source-Leveln. Entscheidend ist, ob die weiterhin wachsende konditionierte Restenergie gerade stark genug ist, den aligned Hub im **operatoriellen** Schurterm zu kontrollieren, ohne ihn wie in C1w vollständig auf null zu screenen.

Erst danach ist ein P11-C1z-Gesamturteil sinnvoll.

---

## 22. Endurteil

\[
\boxed{
[P11\text{-}C1z\text{-}B1]\quad\checkmark[K/M]_{\rm part}
}
\]

**Positiv abgeschlossen:**

- source-windowed positive Gammaform;
- kompakte Gamma-Inverse auf jedem festen Source-Level;
- kompakter Gamma-präkonditionierter Hub;
- exakte nicht-faserweise Feshbach-Identität;
- effektiver Hub = Gamma-Metrik + positiver Schurterm;
- normalisiert: Identität + positiver kompakter Operator;
- unnormalisierte effektive Hub-Inverse kompakt.

**Negativ/Firewall:**

- Windowing allein reicht nicht;
- der C1z-B-Rest ist nicht uniform in \(R\) beschränkt;
- noch keine Schatten-/Large-\(R\)-Kontrolle;
- keine Identität mit \(B_W\), keine RH-Folgerung.

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
