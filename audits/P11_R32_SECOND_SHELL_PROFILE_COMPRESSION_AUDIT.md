# P11/R32 — zweite Schale: exakte Profilkompression des Full-Rest-Operators

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** SE-1/SE-2, SS-1a, SS-L.  
**Ziel:** die 10/11 ambient aktiven Full-Rest-Wörter der zweiten nichtzentralen Schale nach Kompression auf denselben Schalenraum exakt organisieren. Es wird **nicht** behauptet, dass der Schalenraum unter `A=R^*R` invariant ist.

## 1. Setup

Im Drei-Shift-Fenster
\[
2a<T_0<c=\tfrac12\log5,
\qquad a=\tfrac12\log2,
\quad b=\tfrac12\log3,
\quad T=2a,
\]
setze
\[
d=b-a,
\qquad e=T-b,
\qquad \varepsilon=T_0-T.
\]
Fixiere
\[
\frac d2\le R<e,
\qquad \ell=e-R.
\]
Sei
\[
\rho:=\frac rq>0,
\]
wobei
\[
p=\sqrt{\log2}\,2^{-3/4},
\qquad
q=\sqrt{\log2}\,2^{-3/2},
\qquad
r=\sqrt{\log3}\,3^{-3/4}.
\]

Parametrisiere die zweite Schale durch
\[
U_R:L^2(0,\ell)\to\mathscr H^+,
\]
\[
(U_Rf)(b+u)=f(u),
\qquad
(U_Rf)(T-u)=\rho f(u),
\qquad 0<u<\ell,
\]
und setze sie gerade fort; außerhalb der vier Schalenintervalle ist `U_R f=0`.
Dann
\[
\boxed{
\|U_Rf\|_2^2=2(1+\rho^2)\|f\|_{L^2(0,\ell)}^2.
}
\tag{SP.1}
\]
Also ist
\[
V_R:=\frac{1}{\sqrt{2(1+\rho^2)}}U_R
\]
eine Isometrie auf den Schalenraum.

## 2. Disjunkte positive Pre-Adjoint-Kanäle

Schreibe im `(2,0)`-Block
\[
\Phi_{20}=\alpha_1K_1+\alpha_2K_2+\alpha_3K_3,
\]
mit
\[
\alpha_1=2^{-3/4},\quad
\alpha_2=2^{-3/2},\quad
\alpha_3=2^{-9/4}.
\]
Für `y=U_R f` besitzt die positive Hälfte der maskierten rechten Outputs folgende Profilkanäle.

### K1
\[
x=d+u:\quad K_1y=-f(u),\qquad 0<u<\ell,
\]
\[
x=a-u:\quad K_1y=-\rho f(u),\qquad 0<u<\ell.
\]
Die Intervalle sind
\[
(d,d+\ell),\qquad(a-\ell,a).
\]

### K2
\[
x=u:\quad K_2y=\rho f(u),\qquad 0<u<\ell,
\]
\[
x=e-u:\quad K_2y=f(u),\qquad 0<u<\ell.
\]
Die Intervalle sind
\[
(0,\ell),\qquad(R,e).
\]

### K3 nach M20
\[
x=a+u:\quad K_3y=\rho f(u),\qquad 0<u<\min\{\ell,\varepsilon\},
\]
und, nur falls `epsilon>R`,
\[
x=a+e-u:\quad K_3y=f(u),
\qquad e-\varepsilon<u<\ell.
\]
Die zugehörigen Intervalle sind
\[
(a,a+\min\{\ell,\varepsilon\})
\]
und gegebenenfalls
\[
(a+R,a+\varepsilon).
\]

Diese positiven Intervalle sind paarweise disjunkt. Entscheidend sind
\[
\ell<R,
\qquad e<d,
\qquad d+\ell=a-R<d+R=a-\ell,
\]
und
\[
a+\ell<a+R.
\]
Daher gibt es im `L^2(Omega20)`-Skalarprodukt zwischen verschiedenen rechten `K_k`-Kanälen auf `S_{R,2}^+` keine Cross-Terme.

### (2,1)
Nach der Maske `|x|<epsilon` bleiben genau die beiden Profilstücke
\[
\rho f(u)1_{u<\varepsilon},
\qquad
f(u)1_{u>e-\varepsilon}.
\]

### (3,0)
Mit `K_b=K_{log3}^{tr}` gilt auf der positiven Hälfte
\[
x=u:\quad K_by=-f(u),
\]
\[
x=e-u:\quad K_by=-\rho f(u),
\qquad 0<u<\ell.
\]
Beide Kanäle liegen vollständig in `Omega30`.

## 3. Exakte Restform auf dem Profil

Setze
\[
J_\varepsilon(u)
:=\rho^2 1_{\{u<\varepsilon\}}
+1_{\{u>e-\varepsilon\}}.
\tag{SP.2}
\]
Aus der exakten SE-2-Gewichtung der drei Restblöcke folgt für `f,g in L^2(0,ell)`
\[
\boxed{
\langle A U_Rf,U_Rg\rangle
=2\int_0^\ell
\bigl[A_0+\kappa J_\varepsilon(u)\bigr]
 f(u)\overline{g(u)}\,du,
}
\tag{SP.3}
\]
mit
\[
\boxed{
A_0=(1+\rho^2)(p^2+q^2+2r^2),
}
\tag{SP.4}
\]
und
\[
\boxed{
\kappa=q^2\bigl(2+2^{-3/2}\bigr)>0.
}
\tag{SP.5}
\]

### Koeffizientenbilanz

- `(2,0)`, `K1` und `K2` liefern den konstanten Anteil
  \[
  (1+\rho^2)(p^2+q^2).
  \]
- `(2,0)`, `K3` liefert
  \[
  q^2 2^{-3/2}J_\varepsilon(u).
  \]
- `(2,1)` liefert
  \[
  2q^2J_\varepsilon(u).
  \]
- `(3,0)` liefert
  \[
  2r^2(1+\rho^2).
  \]

Damit ergibt sich (SP.3).

## 4. Theorem SP-1 — skalare Schalenkompression

Für die normierte Isometrie `V_R` gilt exakt
\[
\boxed{
V_R^* A V_R=M_{\mu_R},
}
\tag{SP.6}
\]
mit der stückweise konstanten positiven Gewichtsfunktion
\[
\boxed{
\mu_R(u)
=p^2+q^2+2r^2
+\frac{q^2(2+2^{-3/2})}{1+\rho^2}
\left(
\rho^2 1_{\{u<\varepsilon\}}
+1_{\{u>e-\varepsilon\}}
\right).
}
\tag{SP.7}
\]
Insbesondere
\[
\mu_R(u)\ge p^2+q^2+2r^2>0.
\]

Dies ist eine echte Kompression der scheinbaren `10/11`-Komplexität: ambient sind zehn Full-Rest-Wörter auf der Schale nicht identisch null, aber nach Projektion auf denselben Schalenraum ist die Restform diagonal und sogar reine Multiplikation im Profilkoordinatensystem.

## 5. Exakte komprimierte erste Blockgleichung

Für späteren Schur-Gebrauch ist auch der Hub auf dem Schalenprofil explizit. Setze
\[
h_0:=q-r\rho=\frac{q^2-r^2}{q}<0,
\qquad
s_0:=-h_0=\frac{r^2-q^2}{q}>0.
\]
Auf der positiven Achse besitzt `H U_R g` exakt drei nichtverschwindende Kanäle innerhalb des Horizonts:
\[
x=e-u:\quad h_0 g(u),
\]
\[
x=d+u:\quad -p g(u),
\]
\[
x=a-u:\quad -p\rho g(u),
\qquad 0<u<\ell.
\tag{SP.8}
\]
Der zentrale `b/T`-Kanal bei `x=u` verschwindet exakt wegen `q rho=r`, also wegen der Unsichtbarkeitsrelation.

Definiere
\[
C_R(u):=(1+\rho^2)+A_0+\kappa J_\varepsilon(u)>0.
\tag{SP.9}
\]
Ist `(U_Rf,w)` ein augmentiertes Blockkernpaar, dann folgt durch Testen der ersten Blockgleichung gegen alle `U_Rg` die notwendige Profilgleichung
\[
\boxed{
C_R(u)f(u)
+s_0 1_{\{e-u<S\}}w(e-u)
+p 1_{\{d+u<S\}}w(d+u)
+p\rho 1_{\{a-u<S\}}w(a-u)
=0
}
\tag{SP.10}
\]
für fast jedes `0<u<ell`.

Diese Gleichung ist **nur eine komprimierte notwendige Gleichung** des vollen ambient Blocksystems. Sie ist nicht äquivalent zur vollen ersten Blockgleichung.

## 6. Firewall

SP-1 beweist:

- exakte Profilkompression `V_R^* A V_R=M_mu` auf der zweiten Schale;
- exakte skalare Restform trotz 10/11 ambient aktiver Wörter;
- die notwendige komprimierte Profilgleichung (SP.10).

SP-1 beweist **nicht**:

- `A S_{R,2}^+ subset S_{R,2}^+`;
- dass die zehn ambient Wörter als Operatoren verschwinden oder sich zu einem einzigen ambient Wort addieren;
- Schur-Transversalität der zweiten Schale;
- trivialen vollen augmentierten Blockkern;
- vollen Schur-Crossblock;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Kandidatenstatus:

- **SP-1:** `?[O]` bis unabhängiges GREEN.

Bei vollständigem GREEN wäre zulässig:

- **SP-1:** `✓[M]_part` — exakte skalare Profilkompression der zweiten Schale und notwendige komprimierte Blockgleichung.

Keine Promotion ohne explizite Freigabe.
