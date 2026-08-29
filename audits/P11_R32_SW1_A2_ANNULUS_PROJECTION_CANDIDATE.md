# P11/R32 — SW1-A2 Canonical Annulus Projection Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a1-finite-cell@bb4df3a29c787d4e6981a99781e5de1c86737a51  
> **Status:** AI-GREEN candidate nach internem adversarialen Re-Review; kein independent GREEN; keine Promotion.  
> **Scope:** exakte funktionalanalytische Elimination des gesamten \(y\)-Anteils. Keine Injektivität des induzierten Annulusoperators.

---

## 0. Ziel

Auf SW1 betrachten wir den augmentierten Operator aus SE-1
\[
\mathcal K_{I,A}(y,w)
=
\bigl((I+A)y+HE_{\mathcal A}w,\ E_I^*Hy\bigr).
\tag{A2.1}
\]

Setze
\[
\mathscr H_+:=L^2(-T_0,T_0)^+,
\qquad
\mathscr W:=\mathscr H_{\mathcal A}^-,
\]
und
\[
\boxed{
K:=\mathcal K_R
=
\ker(E_I^*H|_{\mathscr H_+}).
}
\tag{A2.2}
\]

Da \(E_I^*H\) beschränkt ist, ist \(K\subset\mathscr H_+\) ein abgeschlossener Unterraum.
Sei
\[
P:=P_K
\]
die orthogonale Projektion auf \(K\).

Ferner setze
\[
\boxed{
\mathscr T:=I+A.
}
\tag{A2.3}
\]

Wegen
\[
A=R_{T_0}^*R_{T_0}\ge0
\]
gilt
\[
\boxed{
\mathscr T\ge I.
}
\tag{A2.4}
\]

---

## 1. Die positive Kompression auf den inneren Kernel

Definiere
\[
\boxed{
G:=P\mathscr T|_K:K\to K.
}
\tag{A2.5}
\]

Für \(k,\ell\in K\) gilt
\[
\langle Gk,\ell\rangle
=
\langle\mathscr T k,\ell\rangle,
\]
also ist \(G\) selbstadjungiert auf \(K\).

Ferner
\[
\langle Gk,k\rangle
=
\langle\mathscr T k,k\rangle
\ge
\|k\|^2.
\tag{A2.6}
\]

Somit
\[
\boxed{
G\ge I_K,
\qquad
G^{-1}\in\mathcal B(K),
\qquad
\|G^{-1}\|\le1.
}
\tag{A2.7}
\]

Dies ist ein rein funktionalanalytischer Schluss; keine Zell- oder Orbitapproximation wird verwendet.

---

## 2. Kanonische schiefe Projektion

Definiere
\[
\boxed{
Q_{\mathscr T,K}
:=
I-\mathscr T G^{-1}P
\quad\text{auf }\mathscr H_+.
}
\tag{A2.8}
\]

Der Operator ist beschränkt.

### A2-P1 — Range

Es gilt
\[
P Q_{\mathscr T,K}
=
P-P\mathscr T G^{-1}P
=
P-GG^{-1}P
=
0.
\tag{A2.9}
\]

Daher
\[
\operatorname{Ran}Q_{\mathscr T,K}
\subset K^\perp.
\]

Umgekehrt gilt für \(v\in K^\perp\)
\[
Pv=0
\]
und somit
\[
Q_{\mathscr T,K}v=v.
\tag{A2.10}
\]

Also
\[
\boxed{
\operatorname{Ran}Q_{\mathscr T,K}=K^\perp.
}
\tag{A2.11}
\]

Insbesondere fixiert \(Q_{\mathscr T,K}\) seinen Bildraum und ist daher idempotent:
\[
\boxed{
Q_{\mathscr T,K}^2=Q_{\mathscr T,K}.
}
\tag{A2.12}
\]

### A2-P2 — Kernel

Für \(k\in K\) gilt
\[
P\mathscr T k=Gk.
\]
Daher
\[
Q_{\mathscr T,K}\mathscr T k
=
\mathscr T k-\mathscr T G^{-1}Gk
=
0.
\]
Somit
\[
\mathscr T K
\subset
\ker Q_{\mathscr T,K}.
\tag{A2.13}
\]

Umgekehrt impliziert
\[
Q_{\mathscr T,K}z=0
\]
die Identität
\[
z
=
\mathscr T G^{-1}Pz
\in
\mathscr T K.
\tag{A2.14}
\]

Folglich
\[
\boxed{
\ker Q_{\mathscr T,K}
=
\mathscr T K
=
(I+A)\mathcal K_R.
}
\tag{A2.15}
\]

Da \(\mathscr T\) beschränkt invertierbar und \(K\) abgeschlossen ist, ist auch
\[
\mathscr T K
\]
abgeschlossen.

Damit ist \(Q_{\mathscr T,K}\) exakt die beschränkte schiefe Projektion
\[
\boxed{
\mathscr H_+
=
\mathscr T K
\dotplus
K^\perp,
}
\tag{A2.16}
\]
auf \(K^\perp\) entlang \(\mathscr T K\).

---

## 2A. Orthogonale \(2\times2\)-Blockform

Relativ zur orthogonalen Zerlegung
\[
\mathscr H_+
=
K\oplus K^\perp
\]
schreibe
\[
\boxed{
\mathscr T
=
\begin{pmatrix}
G&C^*\\
C&D
\end{pmatrix},
}
\tag{A2.16a}
\]
wobei
\[
\boxed{
C
=
P_{K^\perp}\mathscr T|_K
=
P_{K^\perp}A|_K.
}
\tag{A2.16b}
\]

Dann besitzt A2.8 exakt die Blockform
\[
\boxed{
Q_{\mathscr T,K}
=
\begin{pmatrix}
0&0\\
-CG^{-1}&I_{K^\perp}
\end{pmatrix}.
}
\tag{A2.16c}
\]

Denn für \(z=z_K+z_\perp\) ist
\[
Pz=z_K
\]
und
\[
\mathscr T G^{-1}z_K
=
z_K
+
CG^{-1}z_K
\]
in der Zerlegung \(K\oplus K^\perp\).

Somit
\[
\boxed{
Q_{\mathscr T,K}z
=
z_\perp-CG^{-1}z_K.
}
\tag{A2.16d}
\]

Diese Form macht die verbleibende Nichtlokalität vollständig explizit: sie sitzt ausschließlich im positiven Kompressionsinversen \(G^{-1}\).

---

## 3. Der induzierte Annulusoperator

Setze
\[
Z:=HE_{\mathcal A}:\mathscr W\to\mathscr H_+.
\tag{A2.17}
\]

Definiere
\[
\boxed{
\mathcal L_{\rm ann}^{\rm SW1}
:=
Q_{\mathscr T,K}\,HE_{\mathcal A}.
}
\tag{A2.18}
\]

Explizit:
\[
\boxed{
\mathcal L_{\rm ann}^{\rm SW1}
=
\left[
I-(I+A)
\bigl(P(I+A)|_K\bigr)^{-1}P
\right]
HE_{\mathcal A}.
}
\tag{A2.19}
\]

Der Zielraum ist kanonisch
\[
K^\perp.
\]

Mit A2.16d folgt zusätzlich die exakte Schurform
\[
\boxed{
\mathcal L_{\rm ann}^{\rm SW1}
=
P_{K^\perp}HE_{\mathcal A}
-
C\,G^{-1}P_KHE_{\mathcal A}.
}
\tag{A2.19a}
\]

Wegen A2.15 gilt unmittelbar
\[
\boxed{
\mathcal L_{\rm ann}^{\rm SW1}w=0
\iff
HE_{\mathcal A}w
\in
(I+A)\mathcal K_R.
}
\tag{A2.20}
\]

Dies ist die Range-Transversalitätsbedingung SE.8–SE.9 als Kern eines einzelnen beschränkten Operators.

---

## 4. Exakte Rekonstruktion von \(y\)

Sei
\[
w\in\ker\mathcal L_{\rm ann}^{\rm SW1}.
\]

Setze
\[
z:=HE_{\mathcal A}w.
\]

Nach A2.20 liegt \(z\in\mathscr T K\). Der eindeutige zugehörige Kernelvektor ist
\[
\boxed{
k
=
G^{-1}Pz
\in K,
}
\tag{A2.21}
\]
denn
\[
Pz
=
P\mathscr T k
=
Gk.
\]

Setze
\[
\boxed{
y_w:=-G^{-1}PHE_{\mathcal A}w.
}
\tag{A2.22}
\]

Dann \(y_w\in K\), also
\[
E_I^*Hy_w=0.
\tag{A2.23}
\]

Außerdem folgt aus A2.20
\[
HE_{\mathcal A}w
=
\mathscr T G^{-1}PHE_{\mathcal A}w,
\]
also
\[
\mathscr T y_w+HE_{\mathcal A}w=0.
\tag{A2.24}
\]

Somit
\[
\boxed{
(y_w,w)\in\ker\mathcal K_{I,A}.
}
\tag{A2.25}
\]

---

## 5. Umkehrung und Kernelbijektion

Sei umgekehrt
\[
(y,w)\in\ker\mathcal K_{I,A}.
\]

Die zweite Gleichung liefert
\[
y\in K.
\]

Aus der ersten Gleichung
\[
\mathscr T y+HE_{\mathcal A}w=0
\]
folgt
\[
HE_{\mathcal A}w=-\mathscr T y\in\mathscr T K.
\]
Nach A2.15 also
\[
\mathcal L_{\rm ann}^{\rm SW1}w=0.
\]

Die Projektion des augmentierten Kernes auf \(w\) ist injektiv, weil bei \(w=0\)
\[
\mathscr T y=0
\]
und wegen \(\mathscr T\ge I\) auch \(y=0\).

Damit ist
\[
\boxed{
\ker\mathcal L_{\rm ann}^{\rm SW1}
\xrightarrow{\ \sim\ }
\ker\mathcal K_{I,A},
\qquad
w\longmapsto
\left(
-G^{-1}PHE_{\mathcal A}w,\ w
\right).
}
\tag{A2.26}
\]

---

## 6. Exakte Übereinstimmung mit dem Schur-Kern

SE-1 liefert bereits die Bijektion
\[
\ker\mathcal S_{I,A}
\longleftrightarrow
\ker\mathcal K_{I,A}
\]
mit
\[
\mathcal S_{I,A}
=
E_I^*H(I+A)^{-1}H^*E_{\mathcal A}.
\]

Kombiniert mit A2.26 folgt
\[
\boxed{
\ker\mathcal L_{\rm ann}^{\rm SW1}
=
\ker\mathcal S_{I,A}
}
\tag{A2.27}
\]
als Teilräume des ungeraden Annulusraums.

Auf diesem Kernel stimmt auch die rekonstruierte \(y\)-Koordinate mit SE-1 überein:
\[
\boxed{
-G^{-1}PHE_{\mathcal A}w
=
(I+A)^{-1}H^*E_{\mathcal A}w,
}
\tag{A2.28}
\]
weil \(H^*=-H\) und beide Seiten die eindeutige erste augmentierte Gleichung lösen.

Damit ist A2 keine neue, stärkere Kernbedingung, sondern eine kanonische inversefreie Quotientenrealisierung desselben Schur-Kerns.

---

## 7. Quotienteninterpretation

Da
\[
\mathscr T K
\]
abgeschlossen ist, existiert der Quotient
\[
\mathscr H_+/\mathscr T K.
\]

Die schiefe Projektion A2.8 induziert einen beschränkten Isomorphismus
\[
\boxed{
\mathscr H_+/\mathscr T K
\;\xrightarrow{\sim}\;
K^\perp,
\qquad
[z]\longmapsto Q_{\mathscr T,K}z.
}
\tag{A2.29}
\]

Der Annulusoperator A2.18 ist damit genau die Quotientenklasse der Hubausgabe
\[
HE_{\mathcal A}w
\]
in einer konkreten \(K^\perp\)-Repräsentation.

Die Schur-Frage lautet nun präzise:
\[
\boxed{
\ker\mathcal S_{I,A}=\{0\}
\iff
\ker\mathcal L_{\rm ann}^{\rm SW1}=\{0\}.
}
\tag{A2.30}
\]

---

## 7A. Exakte Cross-Gram-Reconciliation

Setze
\[
\boxed{
J:=\mathscr T^{1/2}K.
}
\tag{A2.29a}
\]

Da \(\mathscr T^{1/2}\) beschränkt invertierbar ist, ist \(J\) abgeschlossen.

Für \(v\in\mathscr H_+\) gilt
\[
\begin{aligned}
v\in J^\perp
&\iff
\langle v,\mathscr T^{1/2}k\rangle=0
\quad\forall k\in K\\
&\iff
\mathscr T^{1/2}v\in K^\perp.
\end{aligned}
\]
Also
\[
\boxed{
J^\perp
=
\mathscr T^{-1/2}K^\perp.
}
\tag{A2.29b}
\]

Da
\[
K=\ker(E_I^*H|_+),
\]
liefert Hilbertraumdualität
\[
K^\perp
=
\overline{\operatorname{Ran}(H^*E_I)}.
\tag{A2.29c}
\]

Definiere wie im Cross-Gram-Audit
\[
\mathscr M_I
:=
\mathscr T^{-1/2}H^*E_I,
\qquad
\mathscr M_A
:=
\mathscr T^{-1/2}H^*E_{\mathcal A}.
\tag{A2.29d}
\]

Dann
\[
\boxed{
J^\perp
=
\overline{\operatorname{Ran}\mathscr M_I}.
}
\tag{A2.29e}
\]

Nun setze
\[
\widehat Q
:=
\mathscr T^{1/2}
P_{J^\perp}
\mathscr T^{-1/2}.
\tag{A2.29f}
\]

Es gilt
\[
\ker\widehat Q
=
\mathscr T^{1/2}J
=
\mathscr T K,
\]
und
\[
\operatorname{Ran}\widehat Q
=
\mathscr T^{1/2}J^\perp
=
K^\perp.
\]
Außerdem fixiert \(\widehat Q\) den Raum \(K^\perp\).

Die Projektion mit Bild \(K^\perp\) und Kern \(\mathscr T K\) ist eindeutig. Nach A2.11 und A2.15 folgt daher
\[
\boxed{
Q_{\mathscr T,K}
=
\mathscr T^{1/2}
P_{J^\perp}
\mathscr T^{-1/2}.
}
\tag{A2.29g}
\]

Wegen
\[
H^*=-H
\]
ist
\[
\mathscr M_A
=
-\mathscr T^{-1/2}HE_{\mathcal A}.
\]
Somit
\[
\boxed{
\mathcal L_{\rm ann}^{\rm SW1}
=
-\mathscr T^{1/2}
P_{\overline{\operatorname{Ran}\mathscr M_I}}
\mathscr M_A.
}
\tag{A2.29h}
\]

Da \(\mathscr T^{1/2}\) injektiv ist,
\[
\boxed{
\ker\mathcal L_{\rm ann}^{\rm SW1}
=
\ker\!\left(
P_{\overline{\operatorname{Ran}\mathscr M_I}}
\mathscr M_A
\right).
}
\tag{A2.29i}
\]

Und nach der Standardidentität
\[
\ker\mathscr M_I^*
=
\left(\overline{\operatorname{Ran}\mathscr M_I}\right)^\perp
\]
folgt exakt
\[
\boxed{
\ker\mathcal L_{\rm ann}^{\rm SW1}
=
\ker(\mathscr M_I^*\mathscr M_A).
}
\tag{A2.29j}
\]

Damit sind die drei bisher getrennt verwendeten Formen exakt identisch:

\[
\boxed{
\begin{array}{c}
\text{augmentierter Blockkern}\\
\Updownarrow\\
\ker\mathcal L_{\rm ann}^{\rm SW1}\\
\Updownarrow\\
\text{Cross-Gram-Kern }\ker(\mathscr M_I^*\mathscr M_A).
\end{array}
}
\tag{A2.29k}
\]

Die Quadratwurzel wird hier nur zur geometrischen Reconciliation benutzt; die Definition A2.18 des Annulusoperators selbst bleibt in der inversefreien \(\mathscr T\)-Kompressionsform.

---

## 8. Rolle von P12 auf SW1

Für die Kernelgleichheit A2.27 ist keine äußere Hub-Injektivität nötig.

Auf SW1 gilt aber zusätzlich der formal bewiesene P12-Satz
\[
\ker(HE_{\mathcal A}|_-)=\{0\}.
\tag{A2.31}
\]

Daher kann A2.20 auf SW1 auch als echte Bildraum-Transversalität gelesen werden:
\[
\boxed{
\ker\mathcal L_{\rm ann}^{\rm SW1}=\{0\}
\iff
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+A)\mathcal K_R
=
\{0\}.
}
\tag{A2.32}
\]

Ohne A2.31 wäre A2.20 als Preimage-/Kernelstatement die primäre Form.

---

## 9. Verbindung zu A0/A1

A2 selbst ist funktionalanalytisch allgemeiner als die SW1-Zellzerlegung.

A0 und A1 liefern aber genau die Daten, die für eine **explizite** Analyse von
\[
G=P(I+A)|_K
\]
und damit von
\[
Q_{\mathscr T,K}
\]
auf SW1 benötigt werden:

- A0: vollständige freie Koordinatenabdeckung;
- A1: vollständige operatorwertige finite-cell Darstellung von \(I+A\);
- SW1-KNF: explizite Koordinatisierung von \(K\).

Zieht man \(G\) durch den KNF-Isomorphismus
\[
\Psi_R:K\to
\mathcal F_R
:=
\mathcal Z_R^+\oplus L^2(\mathcal V_R^{\rm SW1}),
\]
so erhält man
\[
\boxed{
\widetilde G
:=
\Psi_R G\Psi_R^{-1}.
}
\tag{A2.33}
\]

Da \(\Psi_R\) nur ein beschränkter Isomorphismus und im Allgemeinen **nicht unitär** ist, darf in der gewöhnlichen Direktproduktnorm nicht schlicht
\(\widetilde G\ge I\) behauptet werden.

Definiere stattdessen auf \(\mathcal F_R\) das transportierte Skalarprodukt
\[
\boxed{
\langle \xi,\eta\rangle_{\Psi}
:=
\langle\Psi_R^{-1}\xi,\Psi_R^{-1}\eta\rangle_{\mathscr H_+}.
}
\tag{A2.33a}
\]

Bezüglich dieses Skalarprodukts ist \(\Psi_R\) unitär und daher
\[
\boxed{
\widetilde G
\text{ ist selbstadjungiert und }
\widetilde G\ge I
\quad\text{in }(\mathcal F_R,\langle\cdot,\cdot\rangle_\Psi).
}
\tag{A2.33b}
\]

In der gewöhnlichen Direktproduktnorm bleibt jedenfalls
\[
\boxed{
\widetilde G^{-1}
=
\Psi_R G^{-1}\Psi_R^{-1},
\qquad
\|\widetilde G^{-1}\|
\le
\|\Psi_R\|\,\|\Psi_R^{-1}\|.
}
\tag{A2.33c}
\]

Die nächste Rechnung muss daher nicht mehr nach dem richtigen Annulusoperator suchen.
Er ist A2.18 bereits kanonisch festgelegt.

Offen ist nun seine explizite Reduktion bzw. Injektivität.

---

## 10. Nächster Knoten

Der nächste aktive Knoten ist
\[
\boxed{
\text{A3: explizite KNF-/finite-cell Darstellung von }
\widetilde G^{-1}PHE_{\mathcal A}
\text{ bzw. von }
\mathcal L_{\rm ann}^{\rm SW1}.
}
\tag{A2.34}
\]

Dabei sind zwei Ergebnisse möglich:

1. eine endliche Orbit-/Transferreduktion, die
   \[
   \ker\mathcal L_{\rm ann}^{\rm SW1}=\{0\}
   \]
   beweist;

2. ein exakter nichttrivialer \(w\)-Gegenvektor.

**Firewall:** A2 beweist nur die exakte Kernelreduktion auf einen kanonischen Annulusoperator.
Es beweist noch keine Injektivität, kein HT-RED, keine Closed-Range-/bounded-below-Aussage,
kein Objekt X und keine RH-Folgerung.
