# P11/R32 — SW1 M1-ND IMG4 Small-R Cross-Gram Kernel No-Go Candidate

> **Stand:** 31. August 2026  
> **Branch:** research/sw1-m1-nd-img3-eliminator  
> **Status:** \`AI-GREEN candidate\` für einen **negativen** M1-ND-Satz an einem expliziten SW1-Parameterpunkt.  
> **Keine Promotion.** Vor einer Buchung als \(\checkmark[M]_{\rm neg}\) ist unabhängiges adversariales Review erforderlich.
>
> **Behaupteter Kandidatensatz:**
> \[
> \boxed{
> \ker\mathscr N_R\ne\{0\}
> }
> \]
> für den expliziten Punkt
> \[
> \varepsilon_0=\Delta/4,\qquad
> R_0=T/100000,\qquad
> \sigma_0=R_0/2.
> \]
>
> Dies ist ein No-Go gegen die globale M1-ND-Nichtentartung im gesamten SW1-Scope, **nicht** gegen P12-Hub-Injektivität und nicht automatisch gegen andere Parameterfenster oder andere Objekt-X-Architekturen.

---

## 0. Ausgangspunkt

IMG2/IMG3 schreiben den effektiven Operator auf den sechs Basisfunktionskanälen als

\[
\mathscr N_R(f,g)
=
\mathscr T_B f+\mathcal H_R g,
\]

mit

\[
\mathscr T_B=D_R+\mathcal R_R
=
V^*(I+A)V
\]

auf dem positiven Horizon-Basisraum

\[
\mathscr B_H^0,
\]

und zulässigem Horizonunterraum

\[
\mathscr B_K
=
\ker C_K.
\]

Der KNF-Descriptor ist

\[
(C_Kf)(u)
=
p[f(a-u)-f(a+u)]
+r[f(b-u)-f(b+u)]
+q[f(T-u)-f(T+u)],
\qquad
0<u<R.
\]

Der Annulusoperator \(\mathcal H_R\) ist die odd-folded Basisdarstellung von \(HE_{\mathcal A}\).

M1-ND verlangt

\[
\ker\mathscr N_R=\{0\}.
\]

IMG4 konstruiert einen nichttrivialen Kernelvektor für einen expliziten kleinen Radius.

---

# Teil I — Feste untere Chamber-Scheibe

## 1. Explizite Parameter

Setze die physischen Konstanten

\[
T=\log2,
\]

\[
\Delta
=
\log3-\frac32\log2
=
\frac12\log\frac98,
\]

\[
L
=
2\log2-\log3
=
\log\frac43.
\]

Wähle

\[
\boxed{
\varepsilon_0=\frac{\Delta}{4}.
}
\tag{IMG4.1}
\]

Damit

\[
0<\varepsilon_0<\frac{\Delta}{2}.
\]

Wir befinden uns also strikt im unteren A8-Chamber.

Später setzen wir

\[
\boxed{
R_0=\frac{T}{100000},
\qquad
\sigma_0=\frac{R_0}{2},
\qquad
S_0=T+\sigma_0.
}
\tag{IMG4.2}
\]

Das arithmetische Certificate prüft exakt

\[
0<\sigma_0<R_0<\varepsilon_0,
\]

sowie

\[
R_0+\varepsilon_0<\Delta.
\]

Damit liegt der Punkt strikt im SW1-Scope.

---

# Teil II — Explizite Separator-Hitting-Schranke

## 2. A8-Separator

Für

\[
0<\varepsilon<\Delta/2
\]

definiert A8 den regulären Separatorbereich

\[
S_\varepsilon^{\rm reg}
=
(\varepsilon,\Delta/2)
\cup
(\Delta/2,\Delta-\varepsilon).
\]

Bei \(\varepsilon_0=\Delta/4\) ist dies

\[
S_{\varepsilon_0}^{\rm reg}
=
(\Delta/4,\Delta/2)
\cup
(\Delta/2,3\Delta/4).
\tag{IMG4.3}
\]

A8.13 beweist:

\[
t_n\in S_{\varepsilon_0}^{\rm reg}
\Longrightarrow
\text{kein roher FREE/A1-Pfad verbindet }
m\le n-1
\text{ mit }
m\ge n+4.
\tag{IMG4.4}
\]

Das ist der 3-Schichten-Separator.

---

## 3. Exakte \(\pm14\)-Trefferdeckung

Das neue Certificate

\`scripts/certify_sw1_m1_nd_img4_smallR_separator_visibility.py\`

arbeitet ausschließlich mit exakten linearen Formen

\[
A\log2+B\log3,
\qquad
A,B\in\mathbb Q.
\]

Das Vorzeichen einer solchen Form wird nach Nennerklärung auf einen exakten Ganzzahlvergleich

\[
2^m\ ?\ 3^n
\]

reduziert.

Damit wird ohne Gleitkomma-Evidenz geprüft:

\[
\boxed{
\bigcup_{n=-14}^{14}
\left[
(\Delta/4,3\Delta/4)-n\Delta
\right]
=
\mathbb T_L
\quad\text{bis auf Endpunkte}.
}
\tag{IMG4.5}
\]

Der Punkt \(\Delta/2\) selbst gehört wegen der A8-Degeneration nicht zum regulären Separator. Ebenso sind die Intervallendpunkte nicht enthalten.

Die Menge aller Startphasen, deren gesamter irrationaler Orbit jemals einen dieser endlich vielen ausgeschlossenen Punkte trifft, ist jedoch

\[
\bigcup_{m\in\mathbb Z}
\left(
F-m\Delta
\right)
\]

mit endlichem \(F\subset\mathbb T_L\), also abzählbar und damit Lebesgue-null.

Folglich gilt für **fast jede** Startphase \(t_0\):

> Für jeden Index \(m\in\mathbb Z\) existiert
> \[
> j\in[-14,14]\cap\mathbb Z
> \]
> mit
> \[
> t_{m+j}\in S_{\varepsilon_0}^{\rm reg}.
> \]

Insbesondere enthält jeder Block von 29 aufeinanderfolgenden Rotationsindizes einen regulären Separator.

---

# Teil III — Expliziter FREE-Komponentenbound

## 4. A8-Barrieren links und rechts

Fixiere einen rohen FREE-Komponentenknoten mit Rotationsindex \(m_0\).

Wir benötigen nach A8.14 einen linken Separator

\[
n_-\le m_0-4.
\]

Betrachte den 29er-Indexblock

\[
[m_0-32,m_0-4].
\]

Er enthält a.e. einen regulären Separator. Also können wir wählen

\[
m_0-32
\le n_-\le
m_0-4.
\tag{IMG4.6}
\]

Analog besitzt

\[
[m_0+1,m_0+29]
\]

einen regulären Separator

\[
m_0+1
\le n_+\le
m_0+29.
\tag{IMG4.7}
\]

A8.14 legt die gesamte Zusammenhangskomponente dann in

\[
[n_-,n_++3].
\]

Daher enthält ihr Rotationsindexsupport höchstens

\[
(m_0+29+3)-(m_0-32)+1
=
65
\]

Indexlagen:

\[
\boxed{
N_{\rm layer}\le65
\quad\text{a.e.}
}
\tag{IMG4.8}
\]

Nach A5/A8 existieren pro Rotationslage höchstens sechs physische Horizon-Liftzustände.

Somit:

\[
\boxed{
\#\mathcal C_{\rm formal}(x)\le
6\cdot65
=
390.
\]

A8.10B zeigt zusätzlich, dass der physische Sheet-Kollisionsquotient höchstens
zwei formale Komponenten verklebt. Daher verwenden wir im Maßargument außerhalb der abzählbaren Separator-/Kollisionsausnahmemenge den a.e. physischen Bound

\[
\boxed{
\#\mathcal C_{\rm phys}(x)\le780
}
\tag{IMG4.9}
\]

Wichtig: Dieser Bound betrifft den rohen FREE/A1-Graphen von \(I+A\), nicht den augmentierten HUB-Graphen.

---

# Teil IV — Die KNF-Beobachtungsmenge

## 5. Sechs Samplinghalbfenster

Auf der positiven Halbachse setze

\[
\begin{aligned}
U_R
:={}&
(a-R,a)\cup(a,a+R)\\
&\cup(b-R,b)\cup(b,b+R)\\
&\cup(T-R,T)\cup(T,T+R).
\end{aligned}
\tag{IMG4.10}
\]

Die bereits bewiesenen SW1-KNF-Supportrelationen zeigen, dass diese sechs Halbfenster a.e. disjunkt im Horizon liegen.

Daher

\[
\boxed{
|U_R|=6R.
}
\tag{IMG4.11}
\]

Wenn eine Horizonfunktion \(f\) auf \(U_R\) verschwindet, dann gilt unmittelbar

\[
C_Kf=0.
\]

Also

\[
f|_{U_R}=0
\Longrightarrow
f\in\mathscr B_K.
\tag{IMG4.12}
\]

---

# Teil V — FREE-Sättigung und Mass Transport

## 6. Saturierte Horizonmenge

Sei \(\sim_{\rm free}\) die messbare Äquivalenzrelation des rohen FREE/A1-Graphen auf dem positiven Horizon.

Definiere

\[
\boxed{
V_R
:=
\{x:
[x]_{\rm free}\cap U_R\ne\varnothing
\}.
}
\tag{IMG4.13}
\]

Also ist \(V_R\) die Vereinigung aller FREE-Komponenten, welche ein KNF-Samplingfenster treffen.

Wegen IMG4.9 und A8.10B besitzen die physischen Äquivalenzklassen a.e. höchstens 780 Elemente; die Separator-Endpunkt-/Midpoint- und globalen Sheet-Kollisionsstrata sind abzählbar und damit für die Maßschranke irrelevant.

Alle erzeugenden FREE-Kanten sind partielle Translationen oder Reflexionen mit Jacobi-Betrag \(1\). Die Lebesguemaßklasse ist daher unter der Äquivalenzrelation invariant.

Für

\[
N_U(x)
:=
\#([x]_{\rm free}\cap U_R)
\]

gilt auf \(V_R\)

\[
N_U(x)\ge1.
\]

Der elementare Mass-Transport-Satz für endliche maßtreue Äquivalenzrelationen liefert

\[
\int N_U(x)\,dx
=
\int_{U_R}\#[y]_{\rm free}\,dy.
\]

Daher

\[
\begin{aligned}
|V_R|
&\le
\int N_U(x)\,dx\\
&\le
780|U_R|.
\end{aligned}
\]

Mit IMG4.11:

\[
\boxed{
|V_R|
\le
4680R.
}
\tag{IMG4.14}
\]

Die abzählbare A8-Rand-/Degenerationsausnahmemenge ändert diese \(L^2\)-Aussage nicht.

---

# Teil VI — \(V_R\) reduziert den FREE-Horizon-Operator

## 7. Invarianz

Der Operator

\[
\mathscr T_B=I+A
\]

ist nach A1 eine endliche Summe von

- Multiplikationstermen,
- partiellen Translationen,
- partiellen Reflexionen,

deren nichtdiagonale Graphkanten genau im rohen FREE/A1-Graphen liegen.

Da \(V_R\) eine Vereinigung vollständiger Zusammenhangskomponenten ist, besitzt keine dieser Kanten einen Endpunkt in \(V_R\) und den anderen in \(V_R^c\).

Sei auf der physischen positiven Horizonhälfte
\[
M_{V_R}h=1_{V_R}h.
\]
Wegen der FREE-Sättigung kommutiert \(M_{V_R}\) mit jedem physischen A1-Pullbackterm
und damit mit \(I+A\).

Mit der unitären IMG3-Identifikation
\[
V:\mathscr B_H^0\to\mathscr H_+,
\qquad
\mathscr T_B=V^*(I+A)V,
\]
definiere
\[
\boxed{
\Pi_{V_R}:=V^*M_{V_R}V.
}
\]
Dann
\[
\boxed{
\Pi_{V_R}\mathscr T_B
=
\mathscr T_B\Pi_{V_R}.
}
\tag{IMG4.15}
\]

Da \(\mathscr T_B\ge I\) invertierbar ist,

\[
\boxed{
\Pi_{V_R}\mathscr T_B^{-1}
=
\mathscr T_B^{-1}\Pi_{V_R}.
}
\tag{IMG4.16}
\]

Also reduziert der zu \(V_R\) gehörige Basislift-Unterraum den Horizonoperator
und sein Inverses.

Dies ist der entscheidende Unterschied zum früheren B96-Atomversuch: \(V_R\) ist eine echte **Graphkomponentensättigung**, keine nichtinvariante endliche Zellpartition.

---

# Teil VII — Was der Hub auf \(V_R\) vom Annulus sehen kann

## 8. Sichtbarer Annulus

Der odd-folded Drei-Shift-Hub besitzt pro Horizon-Ausgabepunkt höchstens sechs physische Quellbranches:

\[
x\mapsto |x\pm a|,
\qquad
x\mapsto |x\pm b|,
\qquad
x\mapsto |x\pm T|.
\]

Nach Schnitt mit dem positiven Annulus

\[
(R,S)
\]

sind dies partielle affine Isometrien.

Definiere die von \(V_R\) aus sichtbare positive Annulusmenge

\[
W_R^{\rm vis}
\]

als die Vereinigung aller Annulusquellen, die von mindestens einem der sechs Hubbranches aus einem Punkt von \(V_R\) erreicht werden.

Jeder Branch vergrößert Lebesguemaß nicht. Daher

\[
|W_R^{\rm vis}|
\le
6|V_R|.
\]

Mit IMG4.14:

\[
\boxed{
|W_R^{\rm vis}|
\le
28080R.
}
\tag{IMG4.17}
\]

Definiere zusätzlich den unitären Annulustransport
\[
W:\mathscr B_W\to\mathscr H_-^{\rm ann}
\]
durch \((Wg)(x)=2^{-1/2}\widetilde g(x)\) auf der positiven Seite und ungerade
Fortsetzung. IMG0 rekonstruiert den physischen Annulusinput als \(w_g=2Wg\),
und daher gilt exakt
\[
\mathcal H_R=V^*H W,
\qquad H=HE_{\mathcal A}.
\]

Wenn die positive physische Annulusfunktion außerhalb von
\(W_R^{\rm vis}\) getragen ist, gilt
\[
M_{V_R}H(Wg)=0,
\]
also
\[
\boxed{
\Pi_{V_R}\mathcal H_Rg=0.
}
\tag{IMG4.18}
\]

---

# Teil VIII — Explizit positive Blindmenge

## 9. Maßvergleich am Punkt IMG4.2

Für

\[
R_0=T/100000,
\qquad
\sigma_0=R_0/2
\]

ist

\[
S_0=T+\sigma_0.
\]

Der positive Annulus besitzt Länge

\[
\begin{aligned}
S_0-R_0
&=
T-\frac{R_0}{2}\\
&=
\left(
1-\frac1{200000}
\right)T.
\end{aligned}
\tag{IMG4.19}
\]

Andererseits

\[
28080R_0
=
\frac{28080}{100000}T
=
\frac{351}{1250}T.
\tag{IMG4.20}
\]

Das Certificate prüft exakt

\[
\frac{351}{1250}
<
1-\frac1{200000}.
\]

Tatsächlich bleibt eine sehr große Marge:

\[
\left(
1-\frac1{200000}-\frac{351}{1250}
\right)T
>
\frac7{10}T.
\tag{IMG4.21}
\]

Also besitzt

\[
\boxed{
B_0
:=
(R_0,S_0)\setminus W_{R_0}^{\rm vis}
}
\]

positive Lebesguemaßlänge.

---

# Teil IX — Konstruktion des Kernelvektors

## 10. Annulusfunktion

Wähle

\[
0\ne w_+\in L^2(B_0).
\]

Erweitere \(w_+\) ungerade auf den symmetrischen Annulus; in Basisliftnotation sei der resultierende Annulusvektor

\[
0\ne w\in\mathscr B_W.
\]

Nach IMG4.18:

\[
\Pi_{V_{R_0}}\mathcal H_{R_0}w=0.
\tag{IMG4.22}
\]

Setze

\[
\boxed{
f
:=
-\mathscr T_B^{-1}\mathcal H_{R_0}w.
}
\tag{IMG4.23}
\]

Wegen der Reduktionsidentität IMG4.16:

\[
\begin{aligned}
\Pi_{V_{R_0}}f
&=
-\mathscr T_B^{-1}
\Pi_{V_{R_0}}\mathcal H_{R_0}w\\
&=0.
\end{aligned}
\]

Da \(\Pi_{V_{R_0}}=V^*M_{V_{R_0}}V\), verschwindet die zu \(f\) gehörige
positive physische Horizonrekonstruktion auf \(V_{R_0}\), insbesondere auf

\[
U_{R_0}\subset V_{R_0}.
\]

Nach IMG4.12:

\[
\boxed{
f\in\mathscr B_K.
}
\tag{IMG4.24}
\]

Per Definition von \(f\):

\[
\boxed{
\mathscr T_Bf+\mathcal H_{R_0}w=0.
}
\tag{IMG4.25}
\]

Damit

\[
\boxed{
(f,w)\in
\ker\mathscr N_{R_0}.
}
\tag{IMG4.26}
\]

Da \(w\ne0\),

\[
\boxed{
(f,w)\ne(0,0).
}
\tag{IMG4.27}
\]

Somit:

\[
\boxed{
\ker\mathscr N_{R_0}\ne\{0\}.
}
\tag{IMG4.28}
\]

---

# Teil X — Verhältnis zu P12

## 11. Kein Widerspruch zu äußerer Hub-Injektivität

Am gewählten Punkt gilt

\[
\sigma_0=R_0/2<R_0.
\]

Damit liegt er im P12 all-radius restricted-tail sector. Nach der bereits gebuchten Rückbindung ist

\[
\ker(HE_{\mathcal A}|_-)=\{0\}.
\]

Für das gewählte \(w\ne0\) gilt daher sogar

\[
HE_{\mathcal A}w\ne0.
\]

Der IMG4-Kernel ist also ausdrücklich **kein** einfacher äußerer Hubkernel.

Er ist ein echter indirekter Schur-/Cross-Gram-Annihilator:

\[
0\ne HE_{\mathcal A}w
\in
(I+A)\mathcal K_{R_0}.
\]

Damit wäre exakt die bisher offene Range-Transversalität negativ entschieden:

\[
\boxed{
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+A)\mathcal K_{R_0}
\ne\{0\}.
}
\tag{IMG4.29}
\]

Äquivalent:

\[
\boxed{
\ker(\mathscr M_I^*\mathscr M_A)
\ne\{0\}
}
\]

am gewählten Parameterpunkt.

---

# Teil XI — Was dieser Kandidat zerstört und was nicht

## 12. Negative Konsequenz für M1-ND

IMG0 liefert die Kernelbijektion

\[
\ker\mathscr N_R
\cong
\ker\widehat{\mathscr C}_R
\cong
\ker\Gamma_I
\]

im deklarierten finite-level Scope.

Falls der vorliegende IMG4-Beweis adversarial GREEN erhält, folgt am expliziten Punkt

\[
\boxed{
\ker\Gamma_I\ne\{0\}.
}
\tag{IMG4.30}
\]

Damit wäre die **globale Behauptung**, M1-ND gelte auf dem gesamten SW1-Scope, widerlegt.

Zulässige negative Buchung nach unabhängiger Prüfung wäre dann etwa:

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SMALLR}:
\checkmark[M]_{\rm neg}.
}
\]

## 13. Keine weitergehenden Schlussfolgerungen

Nicht bewiesen wird:

- Degeneration für jeden SW1-Parameterpunkt;
- Degeneration für mittlere oder große \(R\);
- ein globaler unendlicher-dimensionaler Kernel für alle Parameter;
- Scheitern jeder möglichen finite-level Geometrie;
- Scheitern von Objekt X insgesamt;
- eine Aussage über die Riemannsche Vermutung.

Der Befund würde ausschließlich zeigen:

> Die aktuelle M1-ND-Nichtentartungsstrategie kann **nicht auf ganz SW1** gelten, weil für hinreichend kleine Radien ein positiver Annulus-Blindraum gegenüber der FREE-Sättigung der KNF-Beobachtungsmenge existiert.

---

# Teil XII — Audit-Gates

Vor jeder Promotion müssen unabhängig geprüft werden:

1. **A8-Übertrag:** Ist der rohe A1-Graf exakt der Graph des Horizon-Horizon-Blocks \(\mathscr T_B\) nach IMG0/IMG1-Reduktion?
2. **Separatorbound:** Folgt aus der exakten \(\pm14\)-Trefferdeckung wirklich der a.e. 65-Layer-/390-formal-State- und 780-physical-State-Bound?
3. **Mass Transport:** Ist
   \[
   |V_R|\le780|U_R|
   \]
   für die konkrete partielle maßtreue Äquivalenzrelation korrekt?
4. **Reducing Subspace:** Ist \(V_R\) für den vollständig aggregierten Horizonoperator einschließlich aller Gates tatsächlich reduzierend?
5. **Hub-Sichtbarkeit:** Sind sechs partielle affine Isometrien eine gültige vollständige Obergrenze für die positive odd-folded HUB-Abtastung?
6. **KNF:** Reicht \(f|_{U_R}=0\) exakt für \(f\in\mathscr B_K\)?
7. **Kerneltransport:** Ist IMG4.23–IMG4.28 exakt dieselbe \(\mathscr N_R\)-Kernelgleichung wie IMG0/IMG2?
8. **Nullmengen:** Können A8-Rand-/Degenerationsphasen ohne versteckte positive Maßvergrößerung entfernt werden?
9. **P12-Kompatibilität:** Liegt der Witnesspunkt tatsächlich im gebuchten all-radius restricted-tail sector?

Bis diese neun Gates unabhängig GREEN sind:

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SMALLR}:
\text{AI-GREEN candidate only}.
}
\]
