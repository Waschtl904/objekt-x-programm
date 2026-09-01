# P11/R32 — SW1 M1-ND IMG4 Analytic Gates Candidate

> **Stand:** 31. August 2026  
> **Branch:** \`research/sw1-m1-nd-img3-eliminator\`  
> **Status:** interne adversariale Schließung der IMG4-Gates 1–9 als **AI-GREEN candidate**; keine Promotion.
>
> Dieser Text ergänzt
> \`P11_R32_SW1_M1_ND_IMG4_SMALLR_KERNEL_NOGO_CANDIDATE.md\`
> und behandelt ausschließlich die bisher offenen analytischen Übergänge.
>
> **Wichtige Vereinfachung:** Der Kernkonstruktionssatz IMG4.28 benutzt weder die
> IMG3-Neumann-Kontraktion noch eine quantitative P12-Beobachtbarkeit. Es genügt
> \[
> \mathscr T_B=V^*(I+A)V\ge I.
> \]
> P12 wird nur für die zusätzliche Interpretation benötigt, dass der gefundene
> Kernel kein äußerer Hubkernel, sondern ein echter indirekter Cross-Gram-Kernel ist.

---

# 1. Gate 1 — A8 dominiert den tatsächlichen Offdiagonalgraphen von \(\mathscr T_B\)

Auf der positiven physischen Horizonhälfte ist

\[
\mathscr T:=I+A
\]

durch A1-R0 bis A1-R7 vollständig beschrieben. Die nichtdiagonalen Source-Maps
sind exakt

\[
\tau_{\pm a},\qquad
\tau_{\pm T},\qquad
r_a,\ r_T,\ r_{3a},\ r_{4a},\ r_{2b}.
\tag{G1.1}
\]

Für den unteren Chamber vereinigt A7 die A1-Rowintervalle mapweise und erhält
exakt die neun Aktivitätsdomänen A7.1–A7.9.

Der neue Crosscheck

\[
\texttt{scripts/certify\_sw1\_m1\_nd\_img4\_gate1\_gate9\_graph\_p12.py}
\]

rekonstruiert diese Vereinigung am festen

\[
\varepsilon_0=\Delta/4
\]

erneut direkt aus den A1-Rowarchetypen und prüft exakt:

\[
\boxed{
D_{\rm A1}(\phi)=D_{\rm A7}(\phi)
\quad
\text{für alle neun Maps }\phi.
}
\tag{G1.2}
\]

Insbesondere werden die beiden heiklen Tailrows explizit geprüft:

\[
R6:
\quad
r_T,\ r_{3a},\ r_{4a},\ \tau_{-a},\ r_{2b},
\tag{G1.3}
\]

\[
R7:
\quad
\tau_{-T},\ r_{3a},\ r_{4a},\ \tau_{-a},\ r_{2b},
\tag{G1.4}
\]

mit sämtlichen zugehörigen Koeffizienten strikt ungleich null.

Damit enthält A8 gerade auch die fünfarmige R6/R7-Verzweigung.

Für IMG4 wird nicht einmal vollständige Graphgleichheit benötigt. Es genügt

\[
\boxed{
\operatorname{Graph}_{\rm off}(\mathscr T)
\subseteq
\mathcal G_{\rm A8}.
}
\tag{G1.5}
\]

Eventuelle spätere Koeffizientenaggregation kann nur aktive Kanten löschen,
nicht neue affine Source-Maps erzeugen. Daher bleibt G1.5 auch für den vollständig
aggregierten Operator gültig.

Unter der bereits in IMG3 gehärteten unitären positiven-Halbachsenidentifikation

\[
\mathscr T_B=V^*\mathscr T V
\tag{G1.6}
\]

ist der Offdiagonalgraph von \(\mathscr T_B\) exakt derselbe physische Graph in
Liftkoordinaten.

**Gate 1: intern GREEN.**

---

# 2. Gate 2 — 65 Layer / 390 formale Zustände / 780 physische Zustände

Das arithmetische IMG4-Certificate beweist exakt, dass bei

\[
\varepsilon_0=\Delta/4
\]

die Rotationen mit

\[
-14\le n\le14
\]

den regulären Separatorbereich a.e. über den ganzen \(L\)-Kreis treffen.

Daher enthält jeder 29er-Indexblock für fast jede Startphase mindestens einen
regulären A8-Separator.

Für einen Knoten mit Index \(m_0\) kann deshalb gewählt werden

\[
n_-\in[m_0-32,m_0-4],
\]

\[
n_+\in[m_0+1,m_0+29].
\]

A8.13 sperrt die Komponente in

\[
[n_-,n_++3],
\]

also in höchstens

\[
65
\]

Rotationslagen. Pro Lage existieren im formalen Zwei-Blatt-Cover höchstens sechs
physische Liftzustände. Damit

\[
\boxed{
\#C_{\rm formal}(x)\le390
}
\tag{G2.1}
\]

für fast jede Startphase.

## 2.1 Sheet-Kollisionspräzisierung

A8.10B zeigt, dass auf globalen Sheet-Kollisionsstrata durch den physischen
Quotienten höchstens zwei formale Komponenten

\[
C\cup J_K(C)
\]

verklebt werden. Dort wäre also nur der punktweise grobe Bound

\[
780
\]

automatisch.

Diese Kollisionsstrata sind jedoch abzählbar: eine Kollision verlangt

\[
2x_0\equiv2b+k\Delta\pmod L
\]

für ein \(k\in\mathbb Z\). Für jedes \(k\) entstehen nur endlich viele
Restklassen; über \(k\in\mathbb Z\) ist die Ausnahmemenge abzählbar.

A8.10B zeigt zusätzlich, dass auf einem globalen Sheet-Kollisionsstratum die
physische Sättigung einer formalen Komponente höchstens
\[
C\cup J_K(C)
\]
ist.  Auf der regulären Menge, auf der der explizite 390-State-Bound gilt,
folgt daher
\[
\boxed{
\#C_{\rm phys}(x)\le 2\cdot390=780
\quad\text{a.e.}
}
\tag{G2.2}
\]

Wichtig: Aus der expliziten \(\pm14\)-Deckung folgt **kein punktweise
universeller** 780-Bound auf den Separator-Endpunkt-/Midpoint-Orbits. Diese
Ausnahmemenge ist jedoch abzählbar und damit Lebesgue-null; A8.14 garantiert
dort weiterhin Endlichkeit. Für den Mass-Transport-Schritt wird ausschließlich
die a.e.-Schranke G2.2 benötigt.

**Gate 2: intern GREEN mit a.e. 780-Quotientenbound.**

---

# 3. Gate 3 — Mass Transport

Sei \(X=(0,T_0)\) mit Lebesguemaß \(\mu\).

Die neun A7-Generatoren sind partielle Borel-Isomorphismen zwischen offenen
Intervallen. Sie sind Translationen oder Reflexionen und besitzen daher
Jacobi-Betrag \(1\). Ihre inversen Maps/Domänen sind ebenfalls im A7-Graphing
enthalten:

- \(\tau_{+a}\leftrightarrow\tau_{-a}\),
- \(\tau_{+T}\leftrightarrow\tau_{-T}\),
- jede Reflexion ist involutiv auf ihrer Aktivitätsdomäne.

Damit erzeugen sie eine abzählbare maßtreue Borel-Äquivalenzrelation
\(\mathcal E\).

Sei

\[
U_R
\]

die Vereinigung der sechs KNF-Samplinghalbfenster und

\[
V_R=\operatorname{Sat}_{\mathcal E}(U_R).
\]

Definiere

\[
N_U(x)
=
\sum_{y\mathrel{\mathcal E}x}1_{U_R}(y)
=
\#([x]_{\mathcal E}\cap U_R).
\]

Für \(x\in V_R\) gilt

\[
N_U(x)\ge1.
\]

Daher

\[
\mu(V_R)
\le
\int_XN_U(x)\,d\mu(x).
\tag{G3.1}
\]

### 3.1 Self-contained proof of Mass Transport

Enumerate all finite words in the nine A7 generators and their inverses:
\[
w_1,w_2,\ldots.
\]
Every \(w_n\) is a partial affine isometry and therefore a
measure-preserving Borel bijection between its domain and range.

The relation is
\[
\mathcal E
=
\bigcup_{n\ge1}\operatorname{Graph}(w_n).
\]
In particular the saturation
\[
V_R
=
\bigcup_{n\ge1}
w_n\bigl(U_R\cap\operatorname{dom}w_n\bigr)
\]
is measurable.

For a measurable set \(A\subset\mathcal E\), define its left counting
measure
\[
M_L(A)
=
\int_X
\#\{y:(x,y)\in A\}\,d\mu(x).
\]
Disjointify \(A\) along the word graphs:
\[
A_1=A\cap\operatorname{Graph}(w_1),
\]
and recursively
\[
A_n
=
\bigl(A\cap\operatorname{Graph}(w_n)\bigr)
\setminus
\bigcup_{j<n}A_j.
\]
Each \(A_n\) is the graph of a restriction of \(w_n\) to some measurable
domain \(D_n\). Hence
\[
M_L(A_n)=\mu(D_n).
\]
After flipping coordinates,
\[
A_n^\top
\]
is the graph of the corresponding restriction of \(w_n^{-1}\) to
\(w_n(D_n)\). Since \(w_n\) preserves Lebesgue measure,
\[
M_L(A_n^\top)
=
\mu(w_n(D_n))
=
\mu(D_n)
=
M_L(A_n).
\]
The pieces \(A_n\) are disjoint, and therefore so are their flips. By
countable additivity,
\[
\boxed{
M_L(A)=M_L(A^\top).
}
\]
Für die vorliegende Anwendung genügt nun die einzelne messbare Relationsteilmenge

\[
A_U
:=
\mathcal E\cap(X\times U_R).
\]

Dann ist

\[
M_L(A_U)
=
\int_X
\#([x]_{\mathcal E}\cap U_R)\,d\mu(x)
=
\int_XN_U(x)\,d\mu(x).
\tag{G3.2}
\]

Nach Flip-Invarianz gilt

\[
M_L(A_U)
=
M_L(A_U^\top).
\]

Aber

\[
A_U^\top
=
\mathcal E\cap(U_R\times X),
\]

also

\[
\boxed{
\int_XN_U(x)\,d\mu(x)
=
\int_{U_R}\#[y]_{\mathcal E}\,d\mu(y).
}
\tag{G3.2a}
\]

Damit wird kein allgemeiner Mass-Transport-Satz für beliebige Dichten benötigt;
die konkrete Identität folgt direkt aus der bereits bewiesenen
Flip-Invarianz des Zählmaßes.

Mit dem a.e. Bound G2.2:

\[
\int_{U_R}\#[y]_{\mathcal E}\,d\mu(y)
\le
780\,\mu(U_R).
\]

Also

\[
\boxed{
\mu(V_R)
\le
780\,\mu(U_R).
}
\tag{G3.3}
\]

Da die sechs KNF-Halbfens­ter a.e. disjunkt sind,

\[
\mu(U_R)=6R,
\]

und daher

\[
\boxed{
\mu(V_R)\le4680R.
}
\tag{G3.4}
\]

**Gate 3: intern GREEN.**

---

# 4. Gate 4 — \(V_R\) reduziert den vollständigen Horizonoperator

Für diesen Gate ist es sauberer, physische und Basislift-Projektion strikt zu
trennen.

Sei auf der positiven physischen Horizonhälfte

\[
M_{V_R}h
:=
1_{V_R}h.
\tag{G4.1}
\]

Nach Gate 1 ist jeder nichtdiagonale Term von

\[
\mathscr T=I+A
\]

von der Form

\[
(T_\phi h)(x)
=
c_\phi(x)\,1_{D_\phi}(x)\,h(\phi(x)),
\tag{G4.2}
\]

wobei \(\phi\) eine A7-Graphing-Map ist.

Weil \(V_R\) eine Vereinigung vollständiger \(\mathcal E\)-Klassen ist, gilt
für fast jedes aktive \(x\in D_\phi\)

\[
\boxed{
1_{V_R}(x)=1_{V_R}(\phi(x)).
}
\tag{G4.3}
\]

Daher

\[
\begin{aligned}
(M_{V_R}T_\phi h)(x)
&=
1_{V_R}(x)c_\phi(x)1_{D_\phi}(x)h(\phi(x))\\
&=
c_\phi(x)1_{D_\phi}(x)1_{V_R}(\phi(x))h(\phi(x))\\
&=
(T_\phi M_{V_R}h)(x).
\end{aligned}
\]

Also

\[
M_{V_R}T_\phi=T_\phi M_{V_R}
\tag{G4.4}
\]

für jeden nichtdiagonalen Pullbackterm. Alle Diagonalterme sind
Multiplikationsoperatoren und kommutieren ebenfalls mit \(M_{V_R}\). Durch
endliche Summation:

\[
\boxed{
M_{V_R}\mathscr T
=
\mathscr T M_{V_R}.
}
\tag{G4.5}
\]

Koeffizientencancellation ist harmlos: sie entfernt lediglich bereits
kommutierende Summanden.

Nun benutze die in IMG3 gehärtete unitäre Identifikation

\[
V:\mathscr B_H^0\to\mathscr H_+,
\qquad
\mathscr T_B=V^*\mathscr T V.
\]

Definiere die **Basislift-Projektion**

\[
\boxed{
\Pi_{V_R}:=V^*M_{V_R}V.
}
\tag{G4.6}
\]

Dann folgt aus G4.5 exakt

\[
\boxed{
\Pi_{V_R}\mathscr T_B
=
\mathscr T_B\Pi_{V_R}.
}
\tag{G4.7}
\]

Damit wird keine physische Punktprojektion stillschweigend mit einer
Basisliftprojektion identifiziert; die beiden sind explizit unitär
transportiert.

Ferner

\[
\mathscr T_B
=
V^*(I+A)V
\ge I.
\]

Also ist \(\mathscr T_B\) beschränkt invertierbar. Aus G4.7 folgt

\[
\boxed{
\Pi_{V_R}\mathscr T_B^{-1}
=
\mathscr T_B^{-1}\Pi_{V_R}.
}
\tag{G4.8}
\]

Äquivalent reduziert der zu \(V_R\) gehörige Basislift-Unterraum
\(\mathscr T_B\) und sein Inverses.

Crucial firewall:

- kein \(J_R\) wird benutzt;
- es wird nicht der freie KNF-Gramoperator \(J_R^*(I+A)J_R\) reduziert;
- zuerst wird auf dem ambienten Horizonraum \(\mathscr B_H^0\) invertiert;
- erst anschließend wird für den konstruierten Vektor die KNF-Mitgliedschaft
  \(f\in\mathscr B_K\) bewiesen.

Damit trifft die A9-Warnung über zusätzliche \(J_R\)-Koordinatenkanten diesen
Schritt nicht.

**Gate 4: intern GREEN.**

---

# 5. Gate 5 — Hub-Sichtbarkeit mit explizitem Annulustransport

Analog zum Horizontransport definiere für \(g\in\mathscr B_W\) zunächst die
positive Rekonstruktion

\[
\widetilde g(x)=g_k([x]_L),
\qquad
x=[x]_L+kL\in(R,S).
\]

Setze auf dem symmetrischen Annulus

\[
(Wg)(x)
=
\frac1{\sqrt2}
\begin{cases}
\widetilde g(x),&x>0,\\
-\widetilde g(-x),&x<0.
\end{cases}
\tag{G5.1}
\]

Wegen der disjunkten Liftmasken gilt

\[
\begin{aligned}
\|Wg\|_{\mathscr H_-^{\rm ann}}^2
&=
2\int_R^S\frac12|\widetilde g(x)|^2\,dx\\
&=
\sum_{k=0}^2
\int_{\mathbb T_L}
n_k(\theta)|g_k(\theta)|^2\,d\theta\\
&=
\|g\|_{\mathscr B_W}^2.
\end{aligned}
\]

Die surjektive Rückrichtung ist genau die IMG0-Annulusrekonstruktion. Somit

\[
\boxed{
W:\mathscr B_W\to\mathscr H_-^{\rm ann}
\text{ unitär}.
}
\tag{G5.2}
\]

IMG0 rekonstruiert aus \(g\) die physische Annulusfunktion

\[
w_g(x)=\sqrt2\,\widetilde g(x)
\]

auf der positiven Seite mit ungerader Fortsetzung. Daher

\[
\boxed{
w_g=2Wg.
}
\tag{G5.3}
\]

Sei

\[
H:=HE_{\mathcal A}
\]

der physische Huboperator. Für physisches ungerades \(w\) lautet der positive
Output

\[
(Hw)(x)
=
p[w(x-a)-w(x+a)]
+r[w(x-b)-w(x+b)]
+q[w(x-T)-w(x+T)].
\tag{G5.4}
\]

Für einen geraden physischen Output \(h\) ist nach IMG0 die
\(P_0\)-Basisliftkomponente

\[
\frac1{\sqrt2}h,
\]

während nach IMG3

\[
V^*h=\sqrt2\,h
\]

in Basisliftnotation gilt. Da der physische Annulusinput zu \(g\) gleich
\(2Wg\) ist, folgt für den effektiven Hubblock exakt

\[
\boxed{
\mathcal H_R
=
V^*HW.
}
\tag{G5.5}
\]

Es fehlt also auch im Hubblock kein versteckter Faktor.

## 5.1 Sichtbarer Annulus

Für \(x>0\) hängen die sechs physikalischen Sourcewerte in G5.4 nur von

\[
|x-a|,\quad x+a,\quad
|x-b|,\quad x+b,\quad
|x-T|,\quad x+T
\tag{G5.6}
\]

nach Schnitt mit dem positiven Annulus \((R,S)\) ab.

Jede Map in G5.6 ist \(1\)-Lipschitz und stückweise Translation oder Reflexion.
Daher vergrößert sie eindimensionales Lebesguemaß nicht.

Sei \(W_R^{\rm vis}\) die Vereinigung der positiven Annulusquellen, die aus
\(V_R\) durch diese sechs Maps gesehen werden. Dann

\[
\boxed{
|W_R^{\rm vis}|
\le
6|V_R|
\le
28080R.
}
\tag{G5.7}
\]

Wähle \(g\in\mathscr B_W\) so, dass die zugehörige positive physische
Annulusfunktion außerhalb \(W_R^{\rm vis}\) getragen ist. Dann

\[
M_{V_R}H(Wg)=0.
\]

Mit G4.6 und G5.5:

\[
\begin{aligned}
\Pi_{V_R}\mathcal H_Rg
&=
V^*M_{V_R}V\,V^*HWg\\
&=
V^*M_{V_R}HWg\\
&=0.
\end{aligned}
\]

Also

\[
\boxed{
\Pi_{V_R}\mathcal H_Rg=0.
}
\tag{G5.8}
\]

Dies ist die präzise Basisliftform der früher verkürzten Aussage
\(P_{V_R}\mathcal H_Rg=0\).

**Gate 5: intern GREEN.**

---

# 6. Gate 6 — KNF

Der KNF-Descriptor lautet für \(0<u<R\)

\[
0=
p[f(a-u)-f(a+u)]
+r[f(b-u)-f(b+u)]
+q[f(T-u)-f(T+u)].
\tag{G6.1}
\]

Die sechs Punkte durchlaufen exakt die sechs Halbfenster von \(U_R\).

Daher

\[
f|_{U_R}=0
\Longrightarrow
C_Kf=0
\Longrightarrow
f\in\mathscr B_K.
\tag{G6.2}
\]

Endpunkte sind Nullmengen und ändern die \(L^2\)-Aussage nicht.

**Gate 6: intern GREEN.**

---

# 7. Gate 7 — tatsächlicher \(\mathscr N_R\)-Kernel

IMG2 definiert exakt

\[
\boxed{
\mathscr N_R(f,g)
=
D_Rf+\mathcal R_Rf+\mathcal H_Rg.
}
\tag{G7.1}
\]

Mit

\[
\mathscr T_B:=D_R+\mathcal R_R
\]

ist dies

\[
\boxed{
\mathscr N_R(f,g)
=
\mathscr T_Bf+\mathcal H_Rg.
}
\tag{G7.2}
\]

Wähle am IMG4-Punkt

\[
0\ne w\in\mathscr B_W
\]

mit positivem Träger im Blindset

\[
B_0=(R_0,S_0)\setminus W_{R_0}^{\rm vis}.
\]

Setze

\[
f
=
-\mathscr T_B^{-1}\mathcal H_{R_0}w.
\tag{G7.3}
\]

Nach Gate 5

\[
\Pi_{V_{R_0}}\mathcal H_{R_0}w=0.
\]

Nach Gate 4

\[
\Pi_{V_{R_0}}f
=
-\mathscr T_B^{-1}
\Pi_{V_{R_0}}\mathcal H_{R_0}w
=
0.
\]

Da \(\Pi_{V_{R_0}}=V^*M_{V_{R_0}}V\), verschwindet die zu \(f\) gehörige
positive physische Horizonrekonstruktion auf \(V_{R_0}\). Insbesondere gilt
wegen

\[
U_{R_0}\subset V_{R_0},
\]

dass alle sechs KNF-Samplewerte verschwinden. Gate 6 liefert

\[
f\in\mathscr B_K.
\]

Schließlich ergibt G7.3 exakt

\[
\mathscr N_{R_0}(f,w)=0.
\]

Weil \(w\ne0\),

\[
\boxed{
(f,w)\ne0,
\qquad
\ker\mathscr N_{R_0}\ne\{0\}.
}
\tag{G7.4}
\]

**Gate 7: intern GREEN.**

---

# 8. Gate 8 — Nullmengen

Es treten drei Typen von Nullmengen auf:

1. A1/A7-Zellendpunkte;
2. der A8-Midpoint \(s=\Delta/2\) und seine Rotationsvorbilder;
3. globale P/\(\overline Q\)-Sheet-Kollisionsphasen.

Die erste Menge ist endlich.

Die zweite ist eine abzählbare Vereinigung von Rotationsvorbildern einer
endlichen Punktmenge und daher abzählbar.

Die dritte ist nach

\[
2x_0\equiv2b+k\Delta\pmod L,
\qquad k\in\mathbb Z,
\]

ebenfalls abzählbar.

Jede A7-Generatorword ist eine partielle affine Isometrie. Das Bild und Urbild
einer Nullmenge unter einem solchen Wort ist wieder eine Nullmenge. Eine
abzählbare Vereinigung solcher Bilder/Ur­bilder bleibt Null.

Somit können sämtliche Ausnahmemengen vor der Mass-Transport- und
Reducing-Subspace-Konstruktion entfernt werden, ohne einen positiven
\(L^2\)-Anteil zu verlieren.

**Gate 8: intern GREEN.**

---

# 9. Gate 9 — P12-Kompatibilität

Dieser Gate ist für den Kernbeweis G7.4 **nicht notwendig**, sondern nur für
die Interpretation des Kernels als indirekten Schur-/Cross-Gram-Kernel.

Der explizite Punkt ist

\[
\varepsilon_0=\Delta/4,
\qquad
R_0=T/100000,
\qquad
\sigma_0=R_0/2,
\]

\[
T_0=T+\varepsilon_0.
\]

P12-A15.1b2f verlangt im Mixed Strip

\[
2a<T_0<c=\frac12\log5,
\]

\[
0<R<T,
\qquad
0<\sigma\le R,
\qquad
\sigma<\varepsilon<\varepsilon_{\max}.
\]

Die trivialen Radius-/Tailungleichungen werden im neuen Gate-Certificate exakt
geprüft.

Für die einzige zusätzliche arithmetische Horizonfrage

\[
T+\Delta/4<\frac12\log5
\]

erhält man nach Multiplikation mit \(8\)

\[
5\log2+2\log3<4\log5,
\]

äquivalent zu

\[
2^5\,3^2<5^4.
\]

Und tatsächlich

\[
288<625.
\]

Damit liegt der Witnesspunkt exakt im gebuchten P12 all-radius
restricted-tail sector. Daher gilt dort

\[
\ker(HE_{\mathcal A}|_-)=\{0\}.
\]

Für unser \(w\ne0\) ist also

\[
HE_{\mathcal A}w\ne0.
\]

Der IMG4-Kernel ist somit kein äußerer Hubkernel, sondern ein echter indirekter
Schur-/Cross-Gram-Annihilator.

**Gate 9: intern GREEN.**

---

# 10. Gesamtverdict dieses internen Reviews

Nach dem aktuellen internen adversarialen Durchgang sind die ursprünglich
offenen Gates 1–9 konsistent geschlossen.

Der wichtigste strukturelle Kern ist:

\[
\boxed{
\text{A8-FREE-Sättigung}
+
\text{Mass Transport}
+
\text{Reducing Subspace}
+
\text{Hub-Blindset}
}
\]

und nicht die IMG3-Neumannreihe.

Damit lautet der aktuelle interne Kandidatenstatus:

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SMALLR}:
\text{AI-GREEN negative candidate}
}
\]

mit Kandidatenaussage

\[
\boxed{
\ker\mathscr N_{R_0}\ne\{0\}.
}
\]

Über die bereits etablierte IMG0-Kernelidentifikation würde dies nach
unabhängiger Bestätigung auch

\[
\ker\Gamma_I\ne\{0\}
\]

am expliziten Witnesspunkt ergeben.

## Promotions-Firewall

Noch **keine** \(\checkmark[M]_{\rm neg}\)-Promotion in diesem Dokument.

Für Promotion ist noch ein unabhängiger adversarialer Review erforderlich,
der mindestens diese vier Punkte eigenständig bestätigt:

1. A1/A7/A8-Graphdomination einschließlich R6/R7;
2. Mass-Transport-Schritt G3.1–G3.4;
3. Reducing-Subspace-Schritt G4.2–G4.5;
4. Kernelkonstruktion G7.3–G7.4 auf dem tatsächlichen Domain
   \(\mathscr B_K\oplus\mathscr B_W\).

Die übrigen Gates sind dann unterstützende Scope-/Nullmengen-/P12-Prüfungen.

Keine Objekt-X- oder RH-Folgerung.
