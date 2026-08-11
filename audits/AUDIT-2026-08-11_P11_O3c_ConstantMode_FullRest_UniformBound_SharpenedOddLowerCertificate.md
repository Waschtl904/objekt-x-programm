# P11-O3c — Constant-Mode Full-Rest Uniform Bound und verschärftes Odd-Lower-Certificate

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3c]`  
**Vorgänger:** O3b  
**Quellen:** C1r, C1z-B, C1z-B1, C3, C4, C5, O3a, O3b  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, keine Residualroute, kein SYN, kein Seal.

---

## 0. Urteil

Der C3/C4-Konstantenmode-Nenner war bisher nur grob durch

\[
\langle \mathbf 1_T,A_T\mathbf 1_T\rangle=O(T^2)
\]

kontrolliert. Diese Schranke verwendete lediglich

\[
\|\mathsf Q_T(u)\eta_{p,k}\|\le1
\]

und ignorierte die exakte p-adische Martingalstruktur der source-gekoppelten Konditionierung.

O3c setzt die exakte Formel aus C1z-B ein und beweist stattdessen

\[
\boxed{
\sup_{T>0}\|R_T\mathbf1_T\|^2<\infty.
}
\tag{O3c.1}
\]

Daher gilt

\[
\boxed{
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=2T+O(1).
}
\tag{O3c.2}
\]

Für einen festen glatten ungeraden alten/source Testvektor `f_-` mit erstem nichtverschwindendem Boundary-Jet `m` verbessert sich damit die C4-Konstantenmode-Untergrenze von

\[
\frac{e^T}{T^{2m+3}}
\]

auf

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\ge
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}
\bigl(1+O_{R,f_-,m}(T^{-1})\bigr).
}
\tag{O3c.3}
\]

Insbesondere

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\gtrsim_{R,f_-,m}
\frac{e^T}{T^{2m+2}}.
}
\tag{O3c.4}
\]

Dies verändert die Interpretation von O3b wesentlich:

- Satz O3b.1 bleibt korrekt;
- seine primitive Zertifikatskosten-Untergrenze `e^T/T^{2m+2}` liegt nun **auf derselben Skala** wie das verschärfte echte Feshbach-Lower-Certificate;
- die frühere Schlussfolgerung, die primitive C5d-artige Zertifikatsroute sei bereits aus Skalengründen um einen Faktor `T` zu grob, ist damit superseded;
- ob eine primitive oder full-rest Dualroute eine **matching upper bound** auf der neuen Skala konstruiert, bleibt offen.

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3c]
&\quad \checkmark[M]_{\rm full\text{-}rest\;constant\text{-}mode\;uniform\;bound}\\
&+\checkmark[M]_{\rm denominator\;2T+O(1)}\\
&+\checkmark[M]_{\rm sharpened\;odd\;constant\text{-}mode\;lower\;certificate}\\
&+\checkmark[M]_{\rm O3b\;scale\;reinterpretation}\\
&+?[O]_{\rm matching\;odd\;upper\;bound}\\
&+?[O]_{\chi^{R,-}_{T,U}\;\rm bounded/divergent}\\
&+?[O]_{\chi_-\|\Theta_-\|\to0}.
\end{aligned}
}
\]

---

# 1. Verbindliche Operatoren

Auf

\[
\mathscr H_T=L^2(-T,T)
\]

sei

\[
\mathbf1_T:=1_{(-T,T)}.
\]

Wie in C3:

\[
A_T:=I+R_T^*R_T
\]

und

\[
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=\|\mathbf1_T\|_2^2+\|R_T\mathbf1_T\|^2.
\tag{O3c.5}
\]

Da

\[
\|\mathbf1_T\|_2^2=2T,
\tag{O3c.6}
\]

reduziert sich die Nennerfrage auf die exakte Größe von

\[
\|R_T\mathbf1_T\|^2.
\]

Der konditionierte Rest aus C3/C1z-B ist

\[
R_Ta(u)
=
\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Ta(u)
\otimes
\mathsf Q_T(u)\eta_{p,k}.
\tag{O3c.7}
\]

Verschiedene Primsektoren `K_p^0` sind nach C1r orthogonal.

---

# 2. Exakte Martingalkoordinaten

C1r konstruiert für jeden Primsektor eine orthonormale Basis

\[
\{\psi_{p,j}:j\ge0\}
\]

mit

\[
\boxed{
\eta_{p,k}
=
\sqrt{p-1}
\sum_{j=0}^{k-1}
p^{(j-k)/2}\psi_{p,j}.
}
\tag{O3c.8}
\]

C1z-B definiert die source-gekoppelte Tiefe

\[
\boxed{
J_{p,T}(u)
=
\max\left\{0,
\left\lfloor
\frac{2(T-|u|)_+}{\log p}
\right\rfloor
\right\}
}
\tag{O3c.9}
\]

und den Level-Cutoff

\[
\mathsf Q_T(u)\psi_{p,j}
=
1_{\{j<J_{p,T}(u)\}}\psi_{p,j}.
\tag{O3c.10}
\]

Daher

\[
\boxed{
\mathsf Q_T(u)\eta_{p,k}
=
\sqrt{p-1}
\sum_{j=0}^{\min(k-1,J_{p,T}(u)-1)}
p^{(j-k)/2}\psi_{p,j}.
}
\tag{O3c.11}
\]

Diese Formel ist der Input, den C3 in seiner groben `O(T^2)`-Schätzung noch nicht ausgenutzt hatte.

---

# 3. Zwei exakte Nullmechanismen

Fixiere `p` und schreibe

\[
L_p:=\log p,
\qquad
J:=J_{p,T}(u).
\]

## 3.1 Boundary-Level `J=0`

Ist

\[
J=0,
\]

so ist die Summe in (O3c.11) leer. Daher

\[
\boxed{
\mathsf Q_T(u)\eta_{p,k}=0
\qquad\forall k\ge1.
}
\tag{O3c.12}
\]

Auf der äußersten source-Boundary-Schale verschwindet der gesamte konditionierte Rest exakt.

## 3.2 Interior-Level `k\le J`

Ist

\[
k\le J,
\]

so folgt aus der Definition von `J`:

\[
|u|+\frac{kL_p}{2}\le T.
\]

Somit liegen beide Punkte

\[
u\pm\frac{kL_p}{2}
\]

im Source-Fenster und

\[
\boxed{
D_{kL_p}E_T\mathbf1_T(u)=0.
}
\tag{O3c.13}
\]

Der Rest kann auf der Konstantenmode daher nur in der Zwischenlage

\[
\boxed{1\le J<k}
\tag{O3c.14}
\]

beitragen.

Dies erklärt zugleich erneut den C3/C5a-Befund für `k=1`: Der primitive Rest verschwindet auf `1_T` vollständig.

---

# 4. Exakte Norm des überlebenden Restvektors

Sei nun

\[
1\le J=j<k.
\]

Aus (O3c.11) und der Orthonormalität der `psi_{p,j}` folgt

\[
\begin{aligned}
\|\mathsf Q_T(u)\eta_{p,k}\|^2
&=(p-1)
\sum_{\ell=0}^{j-1}p^{\ell-k}\\
&=(p-1)p^{-k}\frac{p^j-1}{p-1}\\
&=p^{j-k}-p^{-k}.
\end{aligned}
\]

Also exakt

\[
\boxed{
\|\mathsf Q_T(u)\eta_{p,k}\|^2
=p^{j-k}-p^{-k}
\le p^{j-k}.
}
\tag{O3c.15}
\]

Damit

\[
\boxed{
\|\mathsf Q_T(u)\eta_{p,k}\|
\le p^{(j-k)/2}.
}
\tag{O3c.16}
\]

---

# 5. Pointwise Prime-Sektor-Bound

Definiere wie in C3

\[
F_{p,T}(u)
:=
\sum_{k\ge2}
\sqrt{L_p}\,p^{-k/4}
D_{kL_p}E_T\mathbf1_T(u)
\mathsf Q_T(u)\eta_{p,k}.
\tag{O3c.17}
\]

Der primitive Term `k=1` ist identisch null und darf ausgelassen werden.

Auf einer Schale mit

\[
J_{p,T}(u)=j\ge1
\]

verschwinden nach §3 alle Terme `k\le j`. Für `k>j` gilt

\[
|D_{kL_p}E_T\mathbf1_T(u)|\le1
\]

und (O3c.16). Daher

\[
\begin{aligned}
\|F_{p,T}(u)\|
&\le
\sqrt{L_p}
\sum_{k>j}
p^{-k/4}p^{(j-k)/2}\\
&=
\sqrt{L_p}\,p^{j/2}
\sum_{k>j}p^{-3k/4}\\
&=
\frac{\sqrt{L_p}}{1-p^{-3/4}}
\,p^{-j/4-3/4}.
\end{aligned}
\]

Somit

\[
\boxed{
\|F_{p,T}(u)\|
\le
\frac{\sqrt{\log p}}{1-p^{-3/4}}
\,p^{-j/4-3/4}
\qquad(J_{p,T}(u)=j\ge1).
}
\tag{O3c.18}
\]

Für `J=0` gilt nach (O3c.12) sogar `F_{p,T}(u)=0`.

---

# 6. Integration über die Source-Schalen

Setze

\[
S_{p,j}(T)
:=
\{u\in(-T,T):J_{p,T}(u)=j\}.
\]

Da

\[
J_{p,T}(u)
=
\left\lfloor
\frac{2(T-|u|)}{L_p}
\right\rfloor
\]

im Inneren des Source-Fensters, entspricht eine volle `j`-Schale auf jeder Seite einer radialen Breite `L_p/2`. Daher gilt unabhängig von `T`:

\[
\boxed{
|S_{p,j}(T)|\le L_p.
}
\tag{O3c.19}
\]

Mit (O3c.18):

\[
\begin{aligned}
\|F_{p,T}\|_2^2
&\le
\sum_{j\ge1}
|S_{p,j}(T)|
\frac{L_p}{(1-p^{-3/4})^2}
p^{-j/2-3/2}\\
&\le
\frac{L_p^2}{(1-p^{-3/4})^2}
p^{-3/2}
\sum_{j\ge1}p^{-j/2}.
\end{aligned}
\]

Die geometrische Reihe liefert

\[
\sum_{j\ge1}p^{-j/2}
=
\frac{p^{-1/2}}{1-p^{-1/2}}.
\]

Also

\[
\boxed{
\|F_{p,T}\|_2^2
\le
\frac{(\log p)^2}{(1-p^{-3/4})^2(1-p^{-1/2})}
\frac1{p^2}.
}
\tag{O3c.20}
\]

Die rechte Seite ist **unabhängig von `T`**.

---

# 7. Satz O3c.1 — uniformer Full-Rest-Bound auf der Konstantenmode

Da nach C1r

\[
K_p^0\perp K_q^0
\qquad(p\ne q),
\]

addieren sich die Primsektornormen quadratisch:

\[
\|R_T\mathbf1_T\|^2
=
\sum_p\|F_{p,T}\|_2^2.
\tag{O3c.21}
\]

Aus (O3c.20):

\[
\|R_T\mathbf1_T\|^2
\le
\sum_p
\frac{(\log p)^2}{(1-p^{-3/4})^2(1-p^{-1/2})}
\frac1{p^2}.
\]

Für `p>=2` sind die beiden Nennerfaktoren uniform von null getrennt, und

\[
\sum_p\frac{(\log p)^2}{p^2}<\infty.
\]

Daher existiert eine absolute endliche Konstante `C_res` mit

\[
\boxed{
\|R_T\mathbf1_T\|^2
\le C_{\rm res}
\qquad\forall T>0.
}
\tag{O3c.22}
\]

also

\[
\boxed{
\sup_{T>0}\|R_T\mathbf1_T\|^2<\infty.
}
\tag{O3c.23}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm full\text{-}rest\;constant\text{-}mode\;uniform\;bound}.}
\]

**Bemerkung.** Dieser Satz widerspricht C3 nicht. C3 bewies nur die gröbere wahre Aussage

\[
\|R_T\mathbf1_T\|^2=O(T^2)
\]

durch den Verlust der exakten Martingalgewichte. O3c schärft diese Abschätzung.

---

# 8. Korollar O3c.2 — exakte lineare Nennerskala

Aus

\[
A_T=I+R_T^*R_T,
\]

(O3c.6) und (O3c.22):

\[
2T
\le
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=
2T+\|R_T\mathbf1_T\|^2
\le
2T+C_{\rm res}.
\]

Somit

\[
\boxed{
\langle\mathbf1_T,A_T\mathbf1_T\rangle
=2T+O(1)
=2T\bigl(1+O(T^{-1})\bigr).
}
\tag{O3c.24}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm denominator\;2T+O(1)}.}
\]

Die bisherige C3/C4-Nennerskala `O(T^2)` war daher nicht scharf; der vollständige konditionierte Rest wächst auf der Konstantenmode überhaupt nicht mit `T`.

---

# 9. Korollar O3c.3 — verschärftes Boundary-Jet-Lower-Certificate

Fixiere

\[
0\ne f_-\in C_c^\infty((-R,R)),
\qquad f_-(-u)=-f_-(u),
\]

und sei

\[
m=m(f_-)
:=
\min\{j\ge0:\beta_R^{(j)}(f_-)\ne0\}.
\]

C4 beweist die scharfe skalare Hubpaarung

\[
\boxed{
\langle J_{R,T}f_-,H_T\mathbf1_T\rangle
=
-\sqrt2\,c_m\beta_R^{(m)}(f_-)
\frac{e^{T/2}}{T^{m+1/2}}
\bigl(1+O_{R,f_-,m}(T^{-1})\bigr).
}
\tag{O3c.25}
\]

Daher

\[
|\langle Jf_-,H_T\mathbf1_T\rangle|^2
=
2c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+1}}
\bigl(1+O(T^{-1})\bigr).
\tag{O3c.26}
\]

Die Feshbach-Variationsungleichung aus C3/C4 lautet

\[
\sigma_T(Jf_-)
\ge
\frac{|\langle Jf_-,H_T\mathbf1_T\rangle|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}.
\tag{O3c.27}
\]

Setzt man (O3c.24) und (O3c.26) ein, erhält man für den konkreten Konstantenmode-Rayleighquotienten

\[
\boxed{
\frac{|\langle Jf_-,H_T\mathbf1_T\rangle|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}
=
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}
\bigl(1+O_{R,f_-,m}(T^{-1})\bigr).
}
\tag{O3c.28}
\]

Folglich

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\ge
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}
\bigl(1+O(T^{-1})\bigr).
}
\tag{O3c.29}
\]

und insbesondere

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\gtrsim
\frac{e^T}{T^{2m+2}}.
}
\tag{O3c.30}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm sharpened\;odd\;constant\text{-}mode\;lower\;certificate}.}
\]

Für `m=0` verbessert sich damit der ursprüngliche C3-Bound

\[
e^T/T^3
\]

auf

\[
\boxed{e^T/T^2.}
\]

Für `m=1` verbessert sich C4 entsprechend von `e^T/T^5` auf

\[
\boxed{e^T/T^4.}
\]

Allgemein gewinnt die C4-Hierarchie exakt einen Faktor `T`.

---

# 10. Reinterpretation von O3b

O3b.1 bewies für jede **primitive** Dualzerlegung

\[
h_{T,f_-}
=(R_T^{(1)})^*Y_T+Z_T
\]

die notwendige Kostenuntergrenze

\[
\boxed{
\|Z_T\|^2
\gtrsim
\frac{e^T}{T^{2m+2}}.
}
\tag{O3c.31}
\]

Dieser Satz bleibt vollständig korrekt.

O3b verglich diese Skala jedoch mit der damals einzigen bekannten C4-Lower-Skala

\[
\frac{e^T}{T^{2m+3}}
\]

und interpretierte die primitive Zertifikatsroute deshalb als um einen Faktor `T` zu teuer für eine matching upper bound.

Nach O3c ist dieser Vergleich superseded. Denn nun ist bereits für den **echten** Schurterm bewiesen:

\[
\sigma_T(Jf_-)
\gtrsim
\frac{e^T}{T^{2m+2}}.
\]

Damit gilt stattdessen:

\[
\boxed{
\text{O3b.1-Zertifikatsuntergrenze}
\quad\text{und}\quad
\text{O3c-Konstantenmode-Lower-Certificate}
\text{ liegen auf derselben Skala.}
}
\tag{O3c.32}
\]

### Konsequenz

Die folgende ältere O3b-Interpretation darf nicht mehr verwendet werden:

\[
\boxed{
\text{„primitive C5d-Zertifikatsarchitektur ist aus Skalengründen zu grob.“}
}
\]

Korrekt ist jetzt nur:

\[
\boxed{
\text{Eine primitive matching-upper-bound-Route müsste Kosten höchstens und mindestens auf der Skala }
 e^T/T^{2m+2}
\text{ erreichen.}
}
\tag{O3c.33}
\]

Ob sie das kann, ist offen.

Insbesondere ist die **volle Restgeometrie nicht mehr allein durch O3b.1 als notwendiger nächster Weg erzwungen**. Sie bleibt eine zulässige Route, aber primitive Dualscreening-Methoden sind nach der neuen Skalierung wieder offen.

Status:

\[
\boxed{\checkmark[M]_{\rm O3b\;scale\;reinterpretation}.}
\]

---

# 11. Was O3c nicht beweist

O3c beweist **keine** obere Schranke

\[
\sigma_T(Jf_-)
\lesssim
\frac{e^T}{T^{2m+2}}.
\]

Daher beweist O3c keine Zwei-Seiten-Asymptotik

\[
\sigma_T(Jf_-)
\asymp
\frac{e^T}{T^{2m+2}}.
\]

Ebenso beweist O3c nicht:

1. dass verschiedene odd Richtungen mit verschiedenen ersten Jets tatsächlich verschiedene relative Wachstumsraten besitzen;
2. dass
   \[
   \kappa(A^{R,-}_{T,U})\to\infty;
   \]
3. dass `chi_-` beschränkt oder divergent ist;
4. dass
   \[
   \chi_-\|\Theta_-\|\to0
   \]
   gilt oder scheitert;
5. dass der odd relative Terminaltransport konvergiert oder nicht konvergiert;
6. eine Aussage über O4;
7. P11-Readiness;
8. Objekt X;
9. RH.

---

# 12. Neue atomare Leitfrage

Nach O3c ist der nächste atomare Test nicht mehr

\[
\text{„muss die volle Restgeometrie die Konstantenmode auf }T^2\text{-Skala screenen?“}
\]

— diese Vermutung ist falsch: der Rest ist auf `1_T` sogar uniform beschränkt.

Der neue scharfe Test lautet:

\[
\boxed{
[P11\text{-}O3d]
\quad
\text{Odd matching-upper-bound audit auf der Skala }
\frac{e^T}{T^{2m+2}}.
}
\]

Primär zu prüfen ist, ob für feste glatte odd Tests mit erstem Jet `m` eine upper bound

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\le
C_{R,f_-}
\frac{e^T}{T^{2m+2}}
}
\tag{O3c.34}
\]

bewiesen oder widerlegt werden kann.

Erst eine solche matching upper bound würde eine echte Zwei-Seiten-Skala liefern und die O3a-Konditionsfrage substantiell weiterbringen.

---

# 13. Statusmatrix

| Aussage | Status |
|---|---|
| C3 `O(T^2)`-Restbound war gültig | `✓[M]` |
| C3 `O(T^2)`-Restbound ist scharf | `×[M]` |
| `sup_T ||R_T 1_T||^2 < infinity` | `✓[M]` |
| `<1_T,A_T1_T>=2T+O(1)` | `✓[M]` |
| C4 odd Lower-Certificate `e^T/T^(2m+2)` | `✓[M]` |
| O3b.1 primitive Residualkosten-Bound | `✓[M]` |
| O3b „Faktor-T zu grob“-Interpretation | `×[M]`, superseded durch O3c |
| matching odd upper bound | `?[O]` |
| odd Zwei-Seiten-Asymptotik | `?[O]` |
| `kappa(A_-)->infinity` | `?[O]` |
| `chi_- ||Theta_-|| -> 0` | `?[O]` |
| odd strong terminal transport | `?[O]` |
| O4 / SYN / Seal | nicht freigegeben |

---

# 14. Gate-Firewalls

## O3c-FW1 — Lower Certificate ≠ Asymptotik

\[
\boxed{
\sigma_T(Jf_-)
\gtrsim e^T/T^{2m+2}
\not\Rightarrow
\sigma_T(Jf_-)
\asymp e^T/T^{2m+2}.
}
\]

## O3c-FW2 — Nennerkontrolle ≠ Feshbach-Supremumkontrolle

Die exakte Skala des **einen** Variationsvektors `1_T` kontrolliert den gesamten Schurterm nur von unten.

## O3c-FW3 — O3b.1 bleibt Satz, nur seine Interpretation ändert sich

\[
\boxed{
\|Z_T\|^2\gtrsim e^T/T^{2m+2}
}
\]

bleibt korrekt für primitive Dualzerlegungen.

## O3c-FW4 — Primitive Route wieder offen ≠ primitive Route bewiesen

O3c entfernt nur den bisherigen Skaleneinwand. Es konstruiert kein matching primitives Zertifikat.

## O3c-FW5 — keine Konditionsentscheidung

Ohne upper bounds beziehungsweise Zwei-Seiten-Asymptotik bleibt

\[
\chi_{R,-}^{T,U}
\]

offen.

## O3c-FW6 — keine Transportentscheidung

Auch eine spätere Konditionsdivergenz allein würde den odd Transport nicht automatisch widerlegen; der O3-Produktterm

\[
\chi_-\|\Theta_-\|
\]

bleibt maßgeblich.

---

# 15. Endurteil

\[
\boxed{
[P11\text{-}O3c]
\quad
\checkmark[M]_{\rm strong\;sharpening}
\;+
?[O]_{\rm matching\;odd\;upper}.
}
\]

Der volle konditionierte Rest screenet die C3/C4-Konstantenmode **nicht polynomial wachsend**, sondern bleibt darauf uniform beschränkt. Der Feshbach-Nenner besitzt daher die scharfe lineare Skala `2T+O(1)`. Dadurch gewinnt die gesamte odd Boundary-Jet-Untergrenze exakt einen Faktor `T`, und die in O3b diagnostizierte primitive Faktor-`T`-Obstruktion verschwindet als Obstruktion: Ihre Skala ist nun gerade die natürliche Kandidatenskala für eine matching odd upper bound.

P11 bleibt `PASS-A ACTIVE`; kein O4, kein SYN, kein Seal.
