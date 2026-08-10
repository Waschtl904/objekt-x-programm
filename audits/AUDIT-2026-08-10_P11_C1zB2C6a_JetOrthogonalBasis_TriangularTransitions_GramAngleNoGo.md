# P11-C1z-B2-C6a — Kanonische Jet-Orthonormalbasis, trianguläre Transitionen und Gram-Angle-No-Go

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6a]`  
**Direkte Voraussetzungen:** C1z-B2-C2, C1z-B2-C4, C1z-B2-C5, C1z-B2-C6  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6a]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,odd\text{-}total\text{-}divergence}
+
\checkmark[M]_{\rm pos,canonical\text{-}jet\text{-}ONB}
+
\checkmark[M]_{\rm pos,triangular\text{-}transitions}
+
\checkmark[M]_{\rm pos,dense\text{-}core\text{-}lifting}
+
\checkmark[M]_{\rm neg,self\text{-}Gram\text{-}only}
}
\]

C6a enthält zwei Reconciliation-Korrekturen und drei neue Strukturresultate.

1. **Reconciliation I:** Aus dem in C4 bereits auf dem vollen Graphraum formulierten Boundary-Jet-Divergenzsatz und der C5-Jetvollständigkeit folgt die absolute Terminaldivergenz für **jeden** nichtnull ungeraden Graphvektor. Die vorsichtigere C5/C6-Formulierung „auf einem dichten glatten Testkern“ wird damit supersediert.
2. **Reconciliation II:** Die C6-Firewall, die Jetquotienten erzeugten ohne zusätzliche Komplementwahl keine kanonische orthogonale Zerlegung, ist zu stark. Die bereits vorhandene native Hilbertmetrik `h_R` wählt die orthogonalen Komplemente kanonisch. Daraus entsteht eine kanonische eindimensionale Jet-Schichtzerlegung und nach Phasenfixierung eine kanonische Orthonormalbasis.
3. Die nativen Profiltransitionen sind in diesen Jetbasen exakt **untere Dreiecksmatrizen mit positiver Diagonale**.
4. Die endlichen terminalen Selbst-Grammatrizen besitzen eine kanonische Cholesky-Normalisierung, aber diese bestimmt die Cross-Terminal-Winkel nicht. Ein Gram-only-Cholesky-Beweis der C6-Cauchyfrage ist daher logisch unzureichend.
5. Eine universelle endliche Jetordnung ist trotzdem nicht nötig: Wegen der Isometrie aller Terminal-Gauges reicht Cauchy-Konvergenz auf der dichten Vereinigung der kanonischen endlichen Jetfenster für starke Konvergenz auf dem gesamten ungeraden Hilbertraum.

Nicht bewiesen wird weiterhin

\[
\boxed{
W_{R,S,-}^{[T]}
\longrightarrow
W_{R,S,-}^{[\infty]}
\quad\text{stark}.
}
\]

Der neue harte Punkt ist die Kontrolle der terminalabhängigen **Cross-Frame-Winkel beziehungsweise Jet-Tails**, nicht die bloße Selbst-Gram-Asymptotik.

---

# 0. Methodische Verkettung

C6a erbt nichts implizit.

## 0.1 Aus C2

Für `R<S<T` existieren die isometrischen Terminal-Gauges

\[
W_{R,S}^{[T]}
=
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2},
\]

mit

\[
(W_{R,S}^{[T]})^*W_{R,S}^{[T]}=I.
\]

Die gleichmäßige Operatornorm

\[
\|W_{R,S}^{[T]}\|=1
\]

wird in §12 für das Dense-Core-Lifting verwendet.

## 0.2 Aus C4

Für

\[
\mathcal H_R^-:=\mathcal K_{X,R}^-
\]

stehen die stetigen Boundary-Jet-Funktionale

\[
\beta_R^{(m)}:
\mathcal H_R^-\to\mathbb C,
\qquad m\ge0,
\]

zur Verfügung.

C4 beweist ihre lineare Unabhängigkeit und den Divergenzsatz:

Wenn

\[
\beta_R^{(0)}(f)=\cdots=\beta_R^{(m-1)}(f)=0,
\qquad
\beta_R^{(m)}(f)\ne0,
\]

dann

\[
\boxed{
\sigma_T(J_{R,T}f)
\ge
c_{R,f,m}
\frac{e^T}{T^{2m+3}}
\to+\infty.
}
\tag{C1zB2C6a.1}
\]

Wichtig für die Reconciliation: Satz C4.1 ist bereits für

\[
f\in\mathcal K_{X,R}
\]

formuliert, nicht nur für glatte Testvektoren.

## 0.3 Aus C5

Auf dem ungeraden Sektor ist der vollständige Jet vollständig:

\[
\boxed{
\bigcap_{m\ge0}\ker\beta_R^{(m)}
\cap\mathcal H_R^-
=\{0\}.
}
\tag{C1zB2C6a.2}
\]

Außerdem respektieren die nativen Transitionen jeden Jet:

\[
\boxed{
\beta_S^{(m)}J_{R,S}^-
=
\beta_R^{(m)}.
}
\tag{C1zB2C6a.3}
\]

## 0.4 Aus C6

Der Boundary-Transform identifiziert

\[
\mathcal H_R^-
\cong
(\mathscr A_R^-,h_R)
\]

unitär, und die Profile sind verschachtelt:

\[
\mathscr A_R^-
\subseteq
\mathscr A_S^-.
\]

Die Profilinklusion wird mit

\[
\iota_{R,S}:\mathscr A_R^-\hookrightarrow\mathscr A_S^-
\]

bezeichnet.

Die Zukunftsmetrik ist

\[
M_{R,T}
=
\mathfrak B_R G_{R,T}^-\mathfrak B_R^{-1}
\]

und der profilierte Terminal-Gauge

\[
\widetilde W_{R,S}^{[T]}
=
M_{S,T}^{1/2}
\iota_{R,S}
M_{R,T}^{-1/2}.
\tag{C1zB2C6a.4}
\]

---

# 1. Reconciliation I — absolute Odd-Divergenz gilt auf dem ganzen ungeraden Graphraum

C5 und C6 formulierten die bewiesene absolute Divergenz vorsichtshalber auf dem glatten kompakten ungeraden Testkern.

Diese Scope-Firewall ist nach direktem Rückvergleich mit C4 nicht nötig.

## Satz C1zB2C6a.1 — totale ungerade Terminaldivergenz

Für jedes

\[
0\ne f\in\mathcal K_{X,R}^-
\]

gilt

\[
\boxed{
\langle G_{R,T}^-f,f\rangle_{X,R}
\longrightarrow+\infty.
}
\tag{C1zB2C6a.5}
\]

Äquivalent, für

\[
F=\mathfrak B_Rf\ne0,
\]

gilt

\[
\boxed{
h_T(F,F)\longrightarrow+\infty.}
\tag{C1zB2C6a.6}
\]

### Beweis

Nach C5-Jetvollständigkeit können für `f\ne0` nicht alle `\beta_R^{(m)}(f)` verschwinden.

Wegen der Wohlordnung von `\mathbb N` existiert daher

\[
m(f)
:=
\min\{m\ge0:\beta_R^{(m)}(f)\ne0\}.
\]

Dann

\[
\beta_R^{(0)}(f)=\cdots=\beta_R^{(m(f)-1)}(f)=0,
\qquad
\beta_R^{(m(f))}(f)\ne0.
\]

C4 Satz C1zB2C4.1 gilt für `f\in\mathcal K_{X,R}` und liefert

\[
\sigma_T(J_{R,T}f)
\ge
c_f\frac{e^T}{T^{2m(f)+3}}
\to+\infty.
\]

Da

\[
\langle G_{R,T}f,f\rangle_{X,R}
=
q_{\Gamma,R}(f)+\sigma_T(J_{R,T}f),
\]

folgt (C1zB2C6a.5). Die Profilform (C1zB2C6a.6) ist C6. `□`

Status:

\[
\boxed{\checkmark[M]_{\rm pos,odd\text{-}total\text{-}divergence}.}
\]

### Supersedierter Scope

Supersediert wird ausschließlich die vorsichtigere Formulierung

\[
\text{„absolute Odd-Divergenz ist nur auf dem glatten dichten Testkern bewiesen“.}
\]

Nicht supersediert wird die Aussage, dass **kein absoluter positiver Odd-Terminalgrenzoperator** aus dieser Geometrie entsteht. Im Gegenteil: (C1zB2C6a.5) verschärft diesen Befund.

---

# 2. Die geschlossene Jetflagge

Arbeite nun im Boundary-Profilhilbertraum

\[
\mathcal H_R
:=
(\mathscr A_R^-,h_R).
\]

Für `m\ge0` setze

\[
\boxed{
\mathcal H_R^{[m]}
:=
\{F\in\mathscr A_R^-:
F^{(0)}(0)=\cdots=F^{(m-1)}(0)=0\},
}
\tag{C1zB2C6a.7}
\]

mit

\[
\mathcal H_R^{[0]}=\mathcal H_R.
\]

Jedes Jetfunktional ist stetig bezüglich `h_R`, weil es über `\mathfrak B_R^{-1}` einem stetigen `\beta_R^{(m)}` auf `\mathcal K_{X,R}^-` entspricht.

Daher ist jedes

\[
\mathcal H_R^{[m]}
\]

ein geschlossener Unterraum.

Aus C5 folgt

\[
\boxed{
\bigcap_{m\ge0}\mathcal H_R^{[m]}=\{0\}.
}
\tag{C1zB2C6a.8}
\]

Aus der linearen Unabhängigkeit der Jetfunktionale folgt für jedes `m`

\[
\boxed{
\operatorname{codim}_{\mathcal H_R^{[m]}}
\mathcal H_R^{[m+1]}=1.
}
\tag{C1zB2C6a.9}
\]

### Begründung von (C1zB2C6a.9)

`\mathcal H_R^{[m+1]}` ist der Kern der Einschränkung des `m`-ten Jetfunktionals auf `\mathcal H_R^{[m]}`.

Wäre diese Einschränkung null, dann läge das `m`-te Funktional im linearen Span der vorherigen Funktionale. Das widerspricht C4.

Ein nichtnull lineares Funktional besitzt einen Kern von Kodimension eins.

---

# 3. Reconciliation II — die native Metrik erzeugt kanonische orthogonale Jetschichten

C6 §10 enthielt die Firewall, aus den eindimensionalen Quotienten folge ohne zusätzliche Komplementwahl keine kanonische orthogonale Direktzerlegung.

Algebraisch, ohne Metrik, wäre diese Vorsicht richtig.

Im vorliegenden Problem ist aber die Hilbertmetrik `h_R` bereits Teil der vorhandenen Object-X-Geometrie. Deshalb gibt es eine kanonische Wahl des Komplements: das `h_R`-orthogonale Komplement.

Definiere

\[
\boxed{
\mathcal L_{R,m}
:=
\mathcal H_R^{[m]}
\ominus_{h_R}
\mathcal H_R^{[m+1]}.
}
\tag{C1zB2C6a.10}
\]

Wegen (C1zB2C6a.9) gilt

\[
\boxed{
\dim\mathcal L_{R,m}=1.
}
\tag{C1zB2C6a.11}
\]

Ferner

\[
\mathcal H_R^{[m]}
=
\mathcal L_{R,m}
\oplus^{\perp_{h_R}}
\mathcal H_R^{[m+1]}.
\tag{C1zB2C6a.12}
\]

Iteriert:

\[
\boxed{
\mathcal H_R
=
\left(
\bigoplus_{m=0}^{N}
\mathcal L_{R,m}
\right)
\oplus^{\perp_{h_R}}
\mathcal H_R^{[N+1]}.
}
\tag{C1zB2C6a.13}
\]

Die Unterräume `\mathcal H_R^{[N]}` sind geschlossen, absteigend und haben trivialen Schnitt. Für absteigende geschlossene Hilbertunterräume konvergieren die Orthogonalprojektionen stark gegen die Projektion auf den Schnitt. Daher

\[
P_{\mathcal H_R^{[N]}}
\xrightarrow[N\to\infty]{\rm s}
0.
\]

Aus (C1zB2C6a.13) folgt deshalb

\[
\boxed{
\mathcal H_R
=
\bigoplus_{m=0}^{\infty,\perp_{h_R}}
\mathcal L_{R,m}.
}
\tag{C1zB2C6a.14}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,canonical\text{-}jet\text{-}layers}.}
\]

### Präzise Supersession der C6-Firewall

Supersediert wird nur die Aussage, eine orthogonale Schichtzerlegung erfordere hier zusätzliche Struktur.

Korrekt ist:

- die **Filtration allein** wählt algebraisch keine Komplemente;
- die bereits vorhandene native Hilbertmetrik `h_R` wählt aber die orthogonalen Komplemente kanonisch;
- es wird keine externe Hardy-, Bergman-, Paley-Wiener- oder andere Norm eingeführt.

Der C6-No-Go gegen einen **festen endlichen** Jetquotienten bleibt vollständig bestehen, denn (C1zB2C6a.14) besitzt unendlich viele Schichten.

---

# 4. Kanonische Jet-Orthonormalbasis

Auf der eindimensionalen Schicht `\mathcal L_{R,m}` ist das `m`-te Jetfunktional nicht null.

Wähle zunächst einen `h_R`-Einheitsvektor

\[
e_{R,m}\in\mathcal L_{R,m}.
\]

Seine Phase ist die einzige verbleibende Freiheit. Fixiere sie durch

\[
\boxed{
\beta_R^{(m)}(\mathfrak B_R^{-1}e_{R,m})>0
\quad\text{reell}.
}
\tag{C1zB2C6a.15}
\]

Damit ist `e_{R,m}` eindeutig bestimmt.

Aus (C1zB2C6a.14) folgt:

## Satz C1zB2C6a.2 — kanonische Jet-ONB

\[
\boxed{
(e_{R,0},e_{R,1},e_{R,2},\ldots)
}
\tag{C1zB2C6a.16}
\]

ist eine kanonische `h_R`-Orthonormalbasis von `\mathscr A_R^-`.

Sie erfüllt die exakte Dreiecksbedingung

\[
\boxed{
\beta_R^{(k)}(\mathfrak B_R^{-1}e_{R,m})=0
\qquad(k<m),
}
\tag{C1zB2C6a.17}
\]

und

\[
\boxed{
\beta_R^{(m)}(\mathfrak B_R^{-1}e_{R,m})>0.
}
\tag{C1zB2C6a.18}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,canonical\text{-}jet\text{-}ONB}.}
\]

Diese Basis ist **level-kanonisch**. Noch nicht bewiesen ist, dass die Transitionen einzelne Basisvektoren auf entsprechende Basisvektoren schicken. Tatsächlich folgt nur eine trianguläre Aussage.

---

# 5. Kanonische endliche Jetfenster und exakte `E`-Abhängigkeit

Definiere

\[
\boxed{
E_{R,N}
:=
\operatorname{span}\{e_{R,0},\ldots,e_{R,N}\}.
}
\tag{C1zB2C6a.19}
\]

Dann

\[
E_{R,0}\subset E_{R,1}\subset\cdots
\]

und

\[
\boxed{
\overline{\bigcup_{N\ge0}E_{R,N}}^{h_R}
=\mathscr A_R^-.
}
\tag{C1zB2C6a.20}
\]

Die Jetkarte

\[
F\mapsto
(F(0),F'(0),\ldots,F^{(N)}(0))
\]

ist auf `E_{R,N}` injektiv, denn ihre Matrix in der Basis (C1zB2C6a.16) ist dreieckig mit nichtverschwindender Diagonale.

Noch stärker: `N` ist der minimale benötigte maximale Jetindex für dieses kanonische Fenster, denn

\[
e_{R,N}^{(0)}(0)=\cdots=e_{R,N}^{(N-1)}(0)=0
\]

aber

\[
e_{R,N}^{(N)}(0)\ne0.
\]

Damit gilt exakt

\[
\boxed{
M(E_{R,N})=N.
}
\tag{C1zB2C6a.21}
\]

Dies ist die gewünschte harte Persistenz der C6-Firewall:

\[
\boxed{
\text{Die benötigte Jetordnung wächst mit dem Fenster; es gibt keinen universellen endlichen Cutoff.}
}
\tag{C1zB2C6a.22}
\]

C6a behauptet nirgends eine von `E` unabhängige endliche Schranke.

---

# 6. Hauptsatz III — native Profiltransitionen sind triangulär

Fixiere `R<S`.

C5/C6 geben

\[
\iota_{R,S}(\mathcal H_R^{[m]})
\subseteq
\mathcal H_S^{[m]}.
\tag{C1zB2C6a.23}
\]

Entwickle

\[
\iota_{R,S}e_{R,m}
=
\sum_{k\ge0}
a_{k,m}^{R,S}e_{S,k}.
\]

Da der linke Vektor in `\mathcal H_S^{[m]}` liegt und

\[
\mathcal H_S^{[m]}
=
\overline{\operatorname{span}}\{e_{S,k}:k\ge m\},
\]

folgt

\[
\boxed{
a_{k,m}^{R,S}=0
\qquad(k<m).}
\tag{C1zB2C6a.24}
\]

Die Übergangsmatrix

\[
\mathbf A_{R,S}
=(a_{k,m}^{R,S})_{k,m\ge0}
\]

ist also in der natürlichen Jetordnung **untere Dreiecksmatrix**.

Für die Diagonale benutzt man Jetkompatibilität:

\[
\beta_S^{(m)}(\iota_{R,S}e_{R,m})
=
\beta_R^{(m)}(e_{R,m}).
\]

Alle Terme `e_{S,k}` mit `k>m` werden von `\beta_S^{(m)}` vernichtet. Daher

\[
\boxed{
a_{m,m}^{R,S}
=
\frac{
\beta_R^{(m)}(\mathfrak B_R^{-1}e_{R,m})
}{
\beta_S^{(m)}(\mathfrak B_S^{-1}e_{S,m})
}>0.
}
\tag{C1zB2C6a.25}
\]

## Satz C1zB2C6a.3

Jede native ungerade Profiltransition besitzt in den kanonischen Jet-ONBen die Form

\[
\boxed{
\mathbf A_{R,S}
=
\begin{pmatrix}
+&0&0&0&\cdots\\
*&+&0&0&\cdots\\
*&*&+&0&\cdots\\
*&*&*&+&\ddots\\
\vdots&\vdots&\vdots&\ddots&\ddots
\end{pmatrix},
}
\tag{C1zB2C6a.26}
\]

mit strikt positiver Diagonale.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,triangular\text{-}transitions}.}
\]

Das ist stärker als die bloße Inklusionsform von C6: Die gesamte native Odd-Transition lebt in einer kanonischen Hilbert-**Neststruktur** der Jetflagge.

**Firewall:** Triangulär bedeutet nicht diagonal. Höhere Jetlagen dürfen und können auftreten; ihre Kontrolle ist gerade Teil des verbleibenden Problems.

---

# 7. Zukunftsmetriken als Gramoperatoren der triangulären Transition

Für `R<T` ist die Profilinklusion

\[
\iota_{R,T}:
(\mathscr A_R^-,h_R)
\to
(\mathscr A_T^-,h_T)
\]

beschränkt und injektiv.

Aus C6 folgt

\[
\boxed{
M_{R,T}
=
\iota_{R,T}^{\dagger}\iota_{R,T},
}
\tag{C1zB2C6a.27}
\]

wobei `\dagger` das Hilbertadjungierte bezüglich `h_R,h_T` bezeichnet.

In den kanonischen Jet-ONBen ist daher formal/exakt als Operatoridentität

\[
\boxed{
\mathbf M_{R,T}
=
\mathbf A_{R,T}^{*}\mathbf A_{R,T}.
}
\tag{C1zB2C6a.28}
\]

Die absolute Divergenz aus §1 bedeutet für jeden nichtnull Koeffizientenvektor `x` mit endlichem Support

\[
\langle \mathbf M_{R,T}x,x\rangle
\to+\infty.
\]

Für den einzelnen kanonischen Layervektor `e_{R,m}` liefert C4 sogar

\[
\boxed{
h_T(e_{R,m},e_{R,m})
\ge
c_{R,m}
\frac{e^T}{T^{2m+3}}
}
\tag{C1zB2C6a.29}
\]

für hinreichend großes `T`.

**Asymptotik-Firewall:** C4 liefert aus dieser Variationsrichtung keine passende obere Schranke und keine vollständige Off-Diagonalasymptotik. Aus (C1zB2C6a.29) darf daher weder

\[
h_T(e_{R,m},e_{R,m})
\sim
C_{R,m}\frac{e^T}{T^{2m+3}}
\]

noch eine entsprechende asymptotische Cholesky-Diagonale behauptet werden.

---

# 8. Kanonische endliche Selbst-Grammatrizen

Auf dem kanonischen Fenster `E_{R,N}` definiere

\[
\boxed{
\mathbf G_{R,T}^{(N)}
:=
\bigl(h_T(e_{R,i},e_{R,j})\bigr)_{0\le i,j\le N}.
}
\tag{C1zB2C6a.30}
\]

Da `\iota_{R,T}` injektiv ist, ist `\mathbf G_{R,T}^{(N)}` positiv definit.

Daher existiert für jedes feste `R,N,T` die eindeutige Cholesky-Zerlegung

\[
\boxed{
\mathbf G_{R,T}^{(N)}
=
\mathbf L_{R,T}^{(N)}
\bigl(\mathbf L_{R,T}^{(N)}\bigr)^*,
}
\tag{C1zB2C6a.31}
\]

mit unterer Dreiecksmatrix `\mathbf L_{R,T}^{(N)}` und strikt positiver Diagonale.

Wegen der kanonischen Jetbasis und ihrer kanonischen Reihenfolge ist auch diese endliche Cholesky-Zerlegung kanonisch.

Sie liefert eine exakte finite-dimensional self-whitening-Koordinate:

Für den Koeffizientenvektor `x` eines `F\in E_{R,N}` gilt

\[
\boxed{
h_T(F,F)
=
\|\bigl(\mathbf L_{R,T}^{(N)}\bigr)^*x\|_{\ell^2}^{2}.}
\tag{C1zB2C6a.32}
\]

Bis hierhin ist der von C6 vorgeschlagene Gram/Cholesky-Pfad vollständig legitim.

Die entscheidende Frage ist aber, ob diese **Selbst-Gram-Daten** bereits den Cross-Terminal-Winkel bestimmen. Die Antwort ist nein.

---

# 9. Der exakte finite-dimensionale Cross-Frame-Winkel

Fixiere `R<S` und ein kanonisches Fenster

\[
E:=E_{R,N}.
\]

Für jedes `T>S` definiere den terminalen Frameoperator

\[
\boxed{
\Phi_T^E
:=
M_{S,T}^{1/2}
\iota_{R,S}|_E
:
E\to\mathscr A_S^-.
}
\tag{C1zB2C6a.33}
\]

Mit dem Pullback-Kokyklus aus C6 gilt

\[
\boxed{
(\Phi_T^E)^{\dagger}\Phi_T^E
=
P_E M_{R,T}|_E.
}
\tag{C1zB2C6a.34}
\]

In der kanonischen Basis von `E` ist die rechte Seite genau die Selbst-Grammatrix `\mathbf G_{R,T}^{(N)}`.

Da sie strikt positiv ist, besitzt `\Phi_T^E` die endliche Polarzerlegung

\[
\boxed{
\Phi_T^E
=
Q_T^E
\bigl(\mathbf G_{R,T}^{(N)}\bigr)^{1/2},
}
\tag{C1zB2C6a.35}
\]

wobei

\[
Q_T^E:E\to\mathscr A_S^-
\]

eine Isometrie ist.

Für zwei Terminale `T,U>S` folgt exakt

\[
\boxed{
(\Phi_T^E)^{\dagger}\Phi_U^E
=
\bigl(\mathbf G_{R,T}^{(N)}\bigr)^{1/2}
(Q_T^E)^{\dagger}Q_U^E
\bigl(\mathbf G_{R,U}^{(N)}\bigr)^{1/2}.
}
\tag{C1zB2C6a.36}
\]

Nach Self-Whitening bleibt also genau

\[
\boxed{
\bigl(\mathbf G_{R,T}^{(N)}\bigr)^{-1/2}
(\Phi_T^E)^{\dagger}\Phi_U^E
\bigl(\mathbf G_{R,U}^{(N)}\bigr)^{-1/2}
=
(Q_T^E)^{\dagger}Q_U^E.
}
\tag{C1zB2C6a.37}
\]

Die Matrix

\[
\boxed{
\Theta_{T,U}^E
:=(Q_T^E)^{\dagger}Q_U^E
}
\tag{C1zB2C6a.38}
\]

ist der finite-dimensionale **Cross-Frame-Winkel**.

Die Selbst-Grammatrizen bestimmen die radialen/metric factors. Die noch fehlende Information ist die relative Orientierung der terminalen isometrischen Frames.

---

# 10. Hauptsatz IV — Selbst-Grams beziehungsweise ihre Cholesky-Faktoren reichen logisch nicht aus

## Satz C1zB2C6a.4 — Gram-angle No-Go

Aus den beiden Selbst-Grammatrizen

\[
\mathbf G_T
=(\Phi_T)^*\Phi_T,
\qquad
\mathbf G_U
=(\Phi_U)^*\Phi_U
\]

allein lässt sich die Cross-Grammatrix

\[
\Phi_T^*\Phi_U
\]

im Allgemeinen nicht bestimmen.

Insbesondere bestimmen auch die eindeutigen Cholesky-Faktoren von `\mathbf G_T` und `\mathbf G_U` den Cross-Frame-Winkel

\[
Q_T^*Q_U
\]

nicht.

### Beweis durch minimales Gegenmodell

Sei

\[
E=\mathbb C,
\qquad
H=\mathbb C^2.
\]

Setze

\[
\Phi_T z
=ze_1
\]

und für einen Winkel `\theta`

\[
\Phi_U z
=z(\cos\theta\,e_1+\sin\theta\,e_2).
\]

Dann gilt für alle `\theta`

\[
\Phi_T^*\Phi_T=1,
\qquad
\Phi_U^*\Phi_U=1.
\]

Beide Selbst-Grammatrizen und beide Cholesky-Faktoren sind also identisch.

Aber

\[
\boxed{
\Phi_T^*\Phi_U
=\cos\theta.
}
\tag{C1zB2C6a.39}
\]

Der Cross-Terminal-Winkel kann trotz identischer Selbst-Grams beliebig variieren. `□`

Status:

\[
\boxed{\checkmark[M]_{\rm neg,self\text{-}Gram\text{-}only}.}
\]

### Scope-Firewall

Dieses abstrakte Gegenmodell behauptet **nicht**, dass im konkreten P11-System beliebige Winkel auftreten.

Es beweist genau die methodische Aussage:

\[
\boxed{
\text{Aus Selbst-Gram-/Cholesky-Asymptotik allein kann die C6-Cross-Terminal-Konvergenz nicht logisch folgen.}
}
\tag{C1zB2C6a.40}
\]

Für einen positiven Cauchysatz muss zusätzliche P11-spezifische Information die Winkel `\Theta_{T,U}^E` kontrollieren.

---

# 11. Zweite Firewall — Kompression und Funktionalkalkül vertauschen nicht

Es gibt noch einen zweiten Grund, warum eine reine endliche Gramrechnung vorsichtig behandelt werden muss.

Der volle profilierte Terminal-Gauge ist

\[
\widetilde W_{R,S}^{[T]}
=
M_{S,T}^{1/2}\iota_{R,S}M_{R,T}^{-1/2}.
\]

Sei `P_E` die `h_R`-orthogonale Projektion auf ein endliches Jetfenster `E`.

Im Allgemeinen gilt **nicht**

\[
\boxed{
P_E M_{R,T}^{-1/2}|_E
=
\bigl(P_E M_{R,T}|_E\bigr)^{-1/2}.
}
\tag{C1zB2C6a.41}
\]

Die Gleichheit wäre insbesondere gesichert, wenn `E` den Operator `M_{R,T}` reduziert. Eine solche Invarianz ist bisher nicht bewiesen.

Daher ist der endliche Framewinkel `\Theta_{T,U}^E` aus §9 ein exakter endlicher diagnostischer Winkel, aber ohne zusätzliche Reduktions-/Tailkontrolle noch **nicht identisch** mit der bloßen Kompression des vollen C6-Cross-Terminal-Kerns.

## Minimales Kompressionsgegenmodell

Sei

\[
H=\mathbb C^2,
\qquad
E=\operatorname{span}\{e_1\},
\]

und für `0<|\rho|<1`

\[
M_\rho
=
\begin{pmatrix}
1&\rho\\
\rho&1
\end{pmatrix}.
\]

Dann ist

\[
P_E M_\rho|_E=1
\]

für jedes `\rho`.

Die endliche Selbst-Grammatrix auf `E` sieht also keinerlei `\rho`-Abhängigkeit.

Aber

\[
M_\rho^{1/2}
=
\frac12
\begin{pmatrix}
\sqrt{1+\rho}+\sqrt{1-\rho}
&
\sqrt{1+\rho}-\sqrt{1-\rho}\\
\sqrt{1+\rho}-\sqrt{1-\rho}
&
\sqrt{1+\rho}+\sqrt{1-\rho}
\end{pmatrix},
\]

also

\[
\boxed{
P_E M_\rho^{1/2}|_E
=
\frac{\sqrt{1+\rho}+\sqrt{1-\rho}}{2},
}
\tag{C1zB2C6a.42}
\]

was von `\rho` abhängt.

Somit kann die Kompression von `M` die Kompression von `M^{1/2}` nicht bestimmen.

### Konsequenz

Ein C6b-Beweis über endliche Jetfenster braucht neben Selbst-Gram-Kontrolle mindestens eine Form von

\[
\boxed{
\text{Jet-Tail-/Reduktionskontrolle für }M_{R,T}^{\pm1/2}
}
\tag{C1zB2C6a.43}
\]

oder eine direkte Kontrolle der vollständigen Cross-Frame-Winkel.

---

# 12. Dense-Core-Lifting — keine universelle endliche Jetordnung nötig

Der Finite-Jet-No-Go aus C6 bleibt bestehen. Trotzdem ist eine universelle endliche Jetordnung **nicht erforderlich**, um starke Terminal-Gauge-Konvergenz zu beweisen.

Das folgt aus der Isometrie der Terminal-Gauges.

## Satz C1zB2C6a.5 — Dense-Core-Cauchy-Kriterium

Fixiere `R<S` und schreibe

\[
W_T:=W_{R,S,-}^{[T]}.
\]

Dann gilt

\[
\|W_T\|=1
\qquad\forall T>S.
\]

Sei

\[
\mathcal D_R
:=
\bigcup_{N\ge0}E_{R,N}.
\]

Nach (C1zB2C6a.20) ist `\mathcal D_R` dicht in `\mathcal K_{X,R}^-`.

Angenommen, für jedes

\[
f\in\mathcal D_R
\]

ist die Familie `W_Tf` für `T\to\infty` Cauchy.

Dann existiert eine eindeutige Isometrie

\[
W_\infty:
\mathcal K_{X,R}^-
\to
\mathcal K_{X,S}^-
\]

mit

\[
\boxed{
W_T\xrightarrow[T\to\infty]{\rm strong}W_\infty.
}
\tag{C1zB2C6a.44}
\]

### Beweis

Auf `\mathcal D_R` definiere

\[
W_\infty f:=\lim_{T\to\infty}W_Tf.
\]

Da jedes `W_T` eine Isometrie ist,

\[
\|W_\infty f\|
=
\lim_T\|W_Tf\|
=
\|f\|.
\]

Also ist `W_\infty` auf `\mathcal D_R` isometrisch und erweitert sich eindeutig auf den Abschluss, also auf den ganzen ungeraden Hilbertraum.

Für beliebiges `f` und `g\in\mathcal D_R` gilt

\[
\begin{aligned}
\|W_Tf-W_\infty f\|
&\le
\|W_T(f-g)\|
+\|W_Tg-W_\infty g\|
+\|W_\infty(g-f)\|\\
&=
2\|f-g\|
+\|W_Tg-W_\infty g\|.
\end{aligned}
\]

Zuerst wähle `g` dicht bei `f`, dann `T` groß. Daraus folgt starke Konvergenz. `□`

Status:

\[
\boxed{\checkmark[M]_{\rm pos,dense\text{-}core\text{-}lifting}.}
\]

### Methodische Konsequenz

Die korrekte Form der `E`-Abhängigkeit lautet:

\[
\boxed{
E_{R,N}
\text{ darf Jetordnung }N\text{ benötigen, und }N\to\infty
\text{ darf erst nach dem festen-Fenster-Test erfolgen.}
}
\tag{C1zB2C6a.45}
\]

Man braucht **keinen** universellen endlichen `M`.

Man braucht stattdessen für jedes feste `N` genügend Kontrolle, um Cauchy-Konvergenz auf `E_{R,N}` zu beweisen. Die Isometrie hebt diese fensterweise Konvergenz anschließend auf den ganzen Hilbertraum.

Dies respektiert exakt den C6-No-Go.

---

# 13. Was C4 für Cholesky tatsächlich liefert — und was nicht

Für jedes feste `N` und jeden nichtzero Vektor

\[
F=\sum_{m=0}^{N}x_m e_{R,m}
\]

sei

\[
m_0:=\min\{m:x_m\ne0\}.
\]

Wegen der Dreiecksstruktur der Jetbasis gilt

\[
\beta_R^{(0)}(F)=\cdots=\beta_R^{(m_0-1)}(F)=0
\]

und

\[
\boxed{
\beta_R^{(m_0)}(F)
=x_{m_0}\beta_R^{(m_0)}(e_{R,m_0})
e0.
}
\tag{C1zB2C6a.46}
\]

C4 liefert daher für jedes feste `F\ne0`

\[
\boxed{
h_T(F,F)
\ge
c_F\frac{e^T}{T^{2m_0+3}}.
}
\tag{C1zB2C6a.47}
\]

Das bestätigt eine echte **hierarchische Divergenz nach erstem aktivem Jetlayer**.

Aber daraus folgt nicht automatisch eine Matrixasymptotik

\[
\mathbf G_{R,T}^{(N)}
\sim
\text{explizite diagonale/trianguläre Modellmatrix}.
\]

Grund: Die C4-Variationsrechnung liefert eine Untergrenze über eine spezielle Terminal-Testmode. Sie kontrolliert nicht die volle Feshbachform von oben und nicht sämtliche Off-Diagonalrichtungen.

Insbesondere wird in C6a **nicht** behauptet:

- dass die Cholesky-Diagonale exakt `e^{T/2}T^{-m-3/2}` skaliert;
- dass die renormierte Cholesky-Matrix konvergiert;
- dass Off-Diagonalterme niedrigere Ordnung besitzen;
- dass die Cross-Frame-Winkel aus den C4-Koeffizienten berechenbar sind.

Diese Aussagen wären neue Mathematik und benötigen zusätzliche Schätzungen.

---

# 14. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6a |
|---|---|---|
| C1y | translationsinvariante Operatorregulatoren lösen den Hub/Rest-Konflikt im C1y-Scope nicht | unverändert; C6a benutzt nur vorhandene `h_R`-Geometrie und Boundary-Jets |
| B2-A | kein Schattenklassenabschluss durch Gamma-Präkonditionierung | unverändert |
| B2-B | naiver Haar-`L^2`-Grenzendpunkt reicht nicht | unverändert |
| C4 | unendliche Jet-Hierarchie; kein fixer endlicher Trunkat stabilisiert die rohe Metrik | unverändert; die kanonischen Fenster haben exakt wachsenden Cutoff `M(E_{R,N})=N` |
| C5 | vollständiger Jet erfasst den gesamten ungeraden Sektor | verstärkt mit C4 zur totalen Odd-Divergenz |
| C6 | kein treuer voller Transport durch festen endlichen Jetquotienten | unverändert |
| C6 | algebraische Boundary-Profiltrivialisierung und metrisches Whitening | direkte Grundlage |
| C6 | „keine kanonische orthogonale Schichtzerlegung ohne Komplementwahl“ | **präzise supersediert:** `h_R` liefert die kanonischen orthogonalen Komplemente |
| C5e | gerader starker Gamma-Gauge-Grenzwert | nur Vergleich, kein Import |

---

# 15. Synthesis-Gate

C6a ändert das Synthesis-Gate nicht.

P11 bleibt

\[
\boxed{\texttt{PASS-A ACTIVE}.}
\]

Gründe:

1. Der ungerade algebraische Kanal ist jetzt sogar in einer kanonischen Jet-ONB trianguliert.
2. Die absolute Odd-Metrik divergiert auf jedem nichtnull Vektor.
3. Der relative starke Gauge-Grenzwert ist weiterhin offen.
4. Die Selbst-Gram-/Cholesky-Route allein ist als unzureichend erkannt.
5. Die noch fehlende P11-spezifische Information betrifft Cross-Terminal-Winkel beziehungsweise Funktionalkalkül-/Jet-Tails.

Daher wird weiterhin kein `papers/P11` erzeugt.

---

# 16. Exakter nächster Arbeitsauftrag C6b

C6a zeigt, dass der nächste Knoten **nicht** einfach weitere Selbst-Grammatrizen berechnen sollte.

Der minimale neue Angriffspunkt lautet:

\[
\boxed{
\text{Kontrolle der Jet-Tails beziehungsweise Cross-Frame-Winkel}
\quad
\Theta_{T,U}^{E_{R,N}}
=(Q_T^{E_{R,N}})^\dagger Q_U^{E_{R,N}}.
}
\tag{C1zB2C6a.48}
\]

Zwei mögliche äquivalente Arbeitsrichtungen sind:

### Route A — direkte Cross-Frame-Kontrolle

Für jedes feste `N` zeigen

\[
\boxed{
\Theta_{T,U}^{E_{R,N}}
\longrightarrow I_{E_{R,N}}
\qquad(T,U\to\infty),
}
\tag{C1zB2C6a.49}
\]

mit zusätzlicher Kontrolle des Unterschieds zwischen dem restringierten endlichen Polarframe und der Restriktion des vollen Terminal-Gauges.

### Route B — Jet-Tail-/Reduktionskontrolle

Mit

\[
P_{R,N}:\mathscr A_R^-\to E_{R,N},
\qquad
Q_{R,N}:=I-P_{R,N},
\]

untersuchen, ob für festes `N` geeignete terminale Abschätzungen für

\[
\boxed{
Q_{R,N}M_{R,T}^{\pm1/2}P_{R,N}
}
\tag{C1zB2C6a.50}
\]

oder direkt für die Differenz

\[
\boxed{
P_{R,N}M_{R,T}^{-1/2}P_{R,N}
-
(P_{R,N}M_{R,T}P_{R,N})^{-1/2}
}
\tag{C1zB2C6a.51}
\]

gewonnen werden können.

Eine hinreichend starke Tailkontrolle würde die endliche Gram-/Cholesky-Analyse mit dem **vollen** C6-Cross-Terminal-Kern verbinden.

**Firewall für C6b:** `N` bleibt fest, während `T,U\to\infty` untersucht werden. Erst nach einem festen-Fenster-Cauchysatz darf über das Dense-Core-Lifting `N\to\infty` genommen werden. Keine universelle endliche Jetordnung wird postuliert.

---

# 17. Endurteil

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6a]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,odd\text{-}total\text{-}divergence}
+
\checkmark[M]_{\rm pos,canonical\text{-}jet\text{-}ONB}
+
\checkmark[M]_{\rm pos,triangular\text{-}transitions}
+
\checkmark[M]_{\rm pos,dense\text{-}core\text{-}lifting}
+
\checkmark[M]_{\rm neg,self\text{-}Gram\text{-}only}
}
\]

Der wesentliche Fortschritt ist zweifach.

Erstens besitzt der ungerade Boundary-Profilraum viel mehr kanonische Hilbertstruktur als C6 zunächst festhielt:

\[
\boxed{
\mathscr A_R^-
=
\bigoplus_{m\ge0}^{\perp h_R}
\mathcal L_{R,m},
}
\]

mit einer kanonischen Jet-Orthonormalbasis und triangulären nativen Transitionen.

Zweitens zeigt die endliche Gram-/Cholesky-Analyse exakt, warum dies den Terminalgrenzwert noch nicht entscheidet:

\[
\boxed{
\text{Selbst-Grams bestimmen die Metrikskalen, aber nicht die Cross-Terminal-Winkel.}
}
\]

Die gute Nachricht ist, dass der C6-Finite-Jet-No-Go den weiteren Weg nicht blockiert. Eine kanonische wachsende Folge endlicher Jetfenster reicht aus; ihre Jetordnung darf und muss mit `N` wachsen. Wegen der Isometrie der Terminal-Gauges würde ein Cauchysatz auf dieser dichten Vereinigung bereits den starken ungeraden Grenztransport auf dem gesamten Hilbertraum liefern.
