# Audit-Kandidat: SW1-AWI — A-Wall-Involution und Reflexionsnormalform

> **Stand:** 28. August 2026  
> **Repo-Basis dieses Audits:** \`main@6da2ed81ed0d513bc6b700b782afc6e4b4284657\`  
> **Status:** \`?[O]\` — vollständiger Beweiskandidat, noch kein AI-GREEN / keine Promotion.  
> **Scope:** ausschließlich SW1-A-Wall-Kopplung zwischen den physischen Branches \(a+s\) und \(2d-s\).

---

## 0. Firewall

Dieses Audit behauptet ausschließlich eine endliche Reflexionsnormalform für den A-Wall-Überlapp auf SW1.

Es beweist **nicht**:

- keinen \(\Delta\)-Descent;
- kein HT-RED;
- kein A0;
- keine Trivialität des augmentierten Kernels;
- keine Aussage \(\ker\Gamma_I=\{0\}\);
- keine globale Chamber-Exhaustivität;
- keine Promotion von SW1-KNF, SW1-BL7 oder SW1-2TP;
- kein Objekt X und keine RH-Folgerung.

Der einzige 2TP-Input ist der bereits auf \`main\` verfügbare Koeffizientenblock
\[
\beta_+\,y(a+s)+\beta_b\,y(2d-s)
\]
in der \(T+s\)-Row.

---

## 1. Setup

Es gelten
\[
a=\frac12\log2,\qquad
b=\frac12\log3,\qquad
T=2a,
\]
\[
d=b-a,\qquad
e=T-b,\qquad
\Delta=d-e=2d-a,
\]
sowie SW1:
\[
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta.
\tag{AWI.1}
\]

Die beiden A-Wall-Shells sind
\[
I_+=(a+R,a+\varepsilon),
\tag{AWI.2}
\]
\[
I_b=(2d-\varepsilon,2d-R)
=(a+\Delta-\varepsilon,a+\Delta-R).
\tag{AWI.3}
\]

Der bekannte A-Wall-Schnitt ist nichtleer genau für
\[
\varepsilon>\frac{\Delta}{2}.
\tag{AWI.4}
\]

Für den oberen Fall definieren wir
\[
\boxed{
J:=(\Delta-\varepsilon,\varepsilon).
}
\tag{AWI.5}
\]

Aus SW1 folgt
\[
\Delta-\varepsilon>R,
\qquad
\varepsilon<\Delta-R,
\tag{AWI.6}
\]
also
\[
\boxed{J\subset(R,\varepsilon).}
\tag{AWI.7}
\]

---

## 2. Lemma AWI-1 — exakte Parametrisierung des physischen Überlapps

Unter \(\varepsilon>\Delta/2\) gilt
\[
\boxed{
I_+\cap I_b
=
(a+\Delta-\varepsilon,\ a+\varepsilon).
}
\tag{AWI.8}
\]

Ferner sind für \(s,t\in(R,\varepsilon)\)
\[
a+s=2d-t
\]
genau dann gleich, wenn
\[
\boxed{s+t=\Delta.}
\tag{AWI.9}
\]

### Beweis

Wegen \(\Delta-\varepsilon>R\) ist die größere linke Grenze von \(I_+\) und \(I_b\)
\[
a+\Delta-\varepsilon.
\]
Wegen \(\varepsilon<\Delta-R\) ist die kleinere rechte Grenze
\[
a+\varepsilon.
\]
Da \(\varepsilon>\Delta/2\), ist
\[
\Delta-\varepsilon<\varepsilon,
\]
also ist das Intervall nichtleer und (AWI.8) folgt.

Weiter:
\[
a+s=2d-t
\iff
a+s=a+\Delta-t
\iff
s+t=\Delta.
\]
\(\square\)

---

## 3. Lemma AWI-2 — die A-Wall-Involution

Definiere
\[
\boxed{
\mathcal J_\Delta(s):=\Delta-s.
}
\tag{AWI.10}
\]

Dann ist
\[
\mathcal J_\Delta:J\to J
\]
eine maßtreue Involution:
\[
\boxed{
\mathcal J_\Delta^2=\mathrm{id}.
}
\tag{AWI.11}
\]

Ihr einziger Fixpunkt ist
\[
s=\frac{\Delta}{2},
\tag{AWI.12}
\]
also eine \(L^2\)-Nullmenge.

### Beweis

Für
\[
\Delta-\varepsilon<s<\varepsilon
\]
gilt
\[
\Delta-\varepsilon<\Delta-s<\varepsilon.
\]
Damit ist \(J\) invariant. Außerdem
\[
\mathcal J_\Delta(\mathcal J_\Delta(s))
=
\Delta-(\Delta-s)=s.
\]
Die Ableitung ist \(-1\), also ist die Transformation maßtreu. Der Fixpunkt folgt aus
\[
s=\Delta-s.
\]
\(\square\)

---

## 4. Lemma AWI-3 — physische Branchidentifikation

Sei \(y\) eine \(L^2\)-Funktion auf dem positiven Horizont. Definiere auf \(J\) die Pullbacks
\[
h_+(s):=y(a+s),
\qquad
h_b(s):=y(2d-s)
\quad\text{a.e.}
\tag{AWI.13}
\]

Dann gilt
\[
\boxed{
h_b(s)=h_+(\Delta-s)
}
\quad\text{für fast jedes }s\in J.
\tag{AWI.14}
\]

### Beweis

Wegen \(2d=a+\Delta\):
\[
2d-s=a+\Delta-s.
\]
Da \(\Delta-s\in J\), folgt direkt
\[
h_b(s)
=
y(a+\Delta-s)
=
h_+(\Delta-s).
\]
Die affine Pullback-Abbildung erhält Nullmengen, daher gilt die Identität a.e. \(\square\)

---

## 5. Reflexionsoperator auf \(L^2(J)\)

Definiere
\[
\mathsf R_\Delta:L^2(J)\to L^2(J),
\qquad
(\mathsf R_\Delta h)(s):=h(\Delta-s).
\tag{AWI.15}
\]

Dann
\[
\boxed{
\mathsf R_\Delta^2=I,
\qquad
\mathsf R_\Delta^*=\mathsf R_\Delta,
\qquad
\|\mathsf R_\Delta h\|_2=\|h\|_2.
}
\tag{AWI.16}
\]

Also ist \(\mathsf R_\Delta\) eine selbstadjungierte unitäre Involution.

Die orthogonalen Projektoren auf die symmetrischen bzw. antisymmetrischen Profile sind
\[
P_{\rm sym}:=\frac12(I+\mathsf R_\Delta),
\qquad
P_{\rm asym}:=\frac12(I-\mathsf R_\Delta).
\tag{AWI.17}
\]

---

## 6. A-Wall-Block aus SW1-2TP

Aus SW1-2TP stammt im \(T+s\)-Rowrest der A-Wall-Anteil
\[
\beta_+\,y(a+s)+\beta_b\,y(2d-s).
\tag{AWI.18}
\]

Mit
\[
\beta_+
=
(\log2)\left(2^{-9/4}+2^{-15/4}\right)>0,
\tag{AWI.19}
\]
\[
\beta_b
=
-\frac{2\log3}{3\sqrt3}<0.
\tag{AWI.20}
\]

Auf \(J\) und mit \(h=h_+\) wird (AWI.18) wegen Lemma AWI-3 zu
\[
\boxed{
\mathcal C_A h
=
\beta_+ h+\beta_b\mathsf R_\Delta h.
}
\tag{AWI.21}
\]

Damit
\[
\boxed{
\mathcal C_A
=
(\beta_++\beta_b)P_{\rm sym}
+
(\beta_+-\beta_b)P_{\rm asym}.
}
\tag{AWI.22}
\]

Die A-Wall-Kopplung ist somit ein endlicher Zwei-Kanal-Reflexionsblock.

---

## 7. Lemma AWI-4 — beide Reflexionskanäle sind strikt invertierbar

Es gilt
\[
\boxed{
\beta_++\beta_b<0,
\qquad
\beta_+-\beta_b>0.
}
\tag{AWI.23}
\]

Insbesondere ist
\[
\boxed{\mathcal C_A\text{ invertierbar auf }L^2(J).}
\tag{AWI.24}
\]

### Beweis

Zunächst
\[
2^{-9/4}<\frac14,
\qquad
2^{-15/4}<\frac18,
\qquad
\log2<1.
\]
Daher
\[
0<\beta_+<\frac38.
\tag{AWI.25}
\]

Setze
\[
c_{11}:=\frac{2\log3}{3\sqrt3}=-\beta_b.
\]

Die benötigte untere Schranke für \(\log3\) ist elementar: Für
\[
F(x):=\log x-\frac{2(x-1)}{x+1}
\]
gilt
\[
F(1)=0,
\qquad
F'(x)
=
\frac{(x-1)^2}{x(x+1)^2}>0
\quad (x>1).
\]
Daher
\[
\log3>\frac{2(3-1)}{3+1}=1.
\]

Außerdem
\[
\sqrt3<\frac74
\]
(denn \(3<49/16\)). Somit
\[
c_{11}
>
\frac{2}{3(7/4)}
=
\frac8{21}
>
\frac38.
\tag{AWI.26}
\]

Somit
\[
c_{11}>\beta_+>0.
\]
Wegen \(\beta_b=-c_{11}\):
\[
\beta_++\beta_b
=
\beta_+-c_{11}<0,
\]
und
\[
\beta_+-\beta_b
=
\beta_++c_{11}>0.
\]
\(\square\)

Explizit:
\[
\boxed{
\mathcal C_A^{-1}
=
\frac1{\beta_++\beta_b}P_{\rm sym}
+
\frac1{\beta_+-\beta_b}P_{\rm asym}.
}
\tag{AWI.27}
\]

Äquivalent:
\[
\boxed{
\mathcal C_A^{-1}
=
\frac{\beta_+I-\beta_b\mathsf R_\Delta}
{\beta_+^2-\beta_b^2}.
}
\tag{AWI.28}
\]

---

## 8. Gesamtdichotomie auf SW1

### 8.1 Untere A-Wall-Unterkammer

Falls
\[
\varepsilon<\frac{\Delta}{2},
\]
ist
\[
I_+\cap I_b=\varnothing.
\]
Es gibt keine A-Wall-Branchidentifikation.

### 8.2 Degenerationsfläche

Falls
\[
\varepsilon=\frac{\Delta}{2},
\]
berühren sich nur die Abschlüsse in einem einzigen Punkt
\[
a+\frac{\Delta}{2}.
\]
Für \(L^2\)-Zwecke ist dies eine Nullmenge; es entsteht kein nichttrivialer Überlappraum.

### 8.3 Obere A-Wall-Unterkammer

Falls
\[
\varepsilon>\frac{\Delta}{2},
\]
ist der gesamte Überlapp durch
\[
\mathcal J_\Delta:s\mapsto\Delta-s
\]
erfasst und der zugehörige A-Wall-Koeffizientenblock \(\mathcal C_A\) ist invertierbar.

Damit lautet der Kandidatensatz:
\[
\boxed{
\text{Auf ganz SW1 erzeugt die A-Wall entweder keinen }L^2\text{-Überlapp oder einen invertierbaren Zwei-Kanal-Reflexionsblock.}
}
\tag{AWI.29}
\]

---

## 9. Was daraus noch nicht folgt

Die Invertierbarkeit von \(\mathcal C_A\) bedeutet nur, dass die physische Identifikation zwischen \(a+s\) und \(2d-s\) keine zusätzliche unkontrollierte A-Wall-Freiheit erzeugt.

Sie beweist **nicht**, dass der gesamte Rest der augmentierten Rows verschwindet.

Der nächste mathematische Schritt nach einem erfolgreichen Review wäre daher weiterhin separat:
\[
\boxed{\Delta\text{-Descent}.}
\]

---

## 10. Review-Checkliste

1. Ist \(I_+\cap I_b\) exakt parametrisiert?
2. Ist \(J=(\Delta-\varepsilon,\varepsilon)\) wirklich vollständig und invariant?
3. Ist \(a+s=2d-t\iff s+t=\Delta\) korrekt und exhaustiv?
4. Ist die a.e.-Pullback-Identifikation \(h_b=\mathsf R_\Delta h_+\) sauber?
5. Ist \(\mathsf R_\Delta\) unitär, selbstadjungiert und involutiv?
6. Ist der 2TP-A-Wall-Input exakt \(\beta_+y(a+s)+\beta_by(2d-s)\)?
7. Sind \(\beta_+\) und \(\beta_b\) korrekt?
8. Ist \(c_{11}>\beta_+\) exakt bewiesen?
9. Sind beide Eigenkanäle strikt von Null getrennt?
10. Ist die Firewall gegen \(\Delta\)-Descent / HT-RED / A0 / \(\ker\Gamma_I\) eingehalten?

Bis zum separaten Re-Review bleibt der Status
\[
\boxed{\mathrm{SW1\!-\!AWI}:?[O].}
\]
