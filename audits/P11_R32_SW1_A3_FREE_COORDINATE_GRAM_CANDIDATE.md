# P11/R32 — SW1-A3 Free-Coordinate Gram Reduction Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a2-annulus-projection@8bf6a8acf1a25e66bba6edc460c08b3dac9918e7  
> **Status:** AI-GREEN candidate nach internem Re-Review; kein independent GREEN; keine Promotion.  
> **Scope:** exakte KNF-Koordinatisierung des positiven Kompressionsinversen aus A2. Keine Injektivität.

---

## 0. Ausgangspunkt

A2 setzt
\[
K=\mathcal K_R
\subset
\mathscr H_+:=L^2(-T_0,T_0)^+,
\qquad
\mathscr T:=I+A\ge I,
\]
\[
P:=P_K,
\qquad
G:=P\mathscr T|_K\ge I.
\]

Der induzierte Annulusoperator lautet
\[
\mathcal L_{\rm ann}^{\rm SW1}
=
\left[
I-\mathscr T G^{-1}P
\right]
HE_{\mathcal A}.
\tag{A3.1}
\]

SW1-KNF liefert den beschränkten Isomorphismus
\[
\Psi_R:
K
\xrightarrow{\sim}
\mathcal F_R,
\qquad
\mathcal F_R
:=
\mathcal Z_R^+
\oplus
L^2(\mathcal V_R^{\rm SW1}).
\tag{A3.2}
\]

Für die Standard-Hilbertraumstruktur auf \(\mathcal F_R\) setzen wir
\[
\boxed{
J_R:=\Psi_R^{-1}:\mathcal F_R\to K.
}
\tag{A3.3}
\]

---

## 1. Der richtige positive KNF-Operator

Definiere
\[
\boxed{
\mathfrak G_R
:=
J_R^*\mathscr T J_R
=
J_R^*(I+A)J_R
\quad\text{auf }\mathcal F_R.
}
\tag{A3.4}
\]

Im Gegensatz zur bloßen Ähnlichkeitstransformation
\[
\Psi_R G\Psi_R^{-1}
\]
ist \(\mathfrak G_R\) bezüglich des gewöhnlichen Skalarprodukts auf
\(\mathcal F_R\) selbstadjungiert und positiv.

Für \(\xi\in\mathcal F_R\):
\[
\langle\mathfrak G_R\xi,\xi\rangle
=
\langle\mathscr T J_R\xi,J_R\xi\rangle
\ge
\|J_R\xi\|^2.
\tag{A3.5}
\]

Aus
\[
\xi
=
\Psi_RJ_R\xi
\]
folgt
\[
\|\xi\|
\le
\|\Psi_R\|\,\|J_R\xi\|.
\]
Damit
\[
\boxed{
\langle\mathfrak G_R\xi,\xi\rangle
\ge
\|\Psi_R\|^{-2}\|\xi\|^2.
}
\tag{A3.6}
\]

Also
\[
\boxed{
\mathfrak G_R
\ge
\|\Psi_R\|^{-2}I_{\mathcal F_R},
}
\tag{A3.7}
\]
und somit
\[
\boxed{
\mathfrak G_R^{-1}\in\mathcal B(\mathcal F_R),
\qquad
\|\mathfrak G_R^{-1}\|
\le
\|\Psi_R\|^2.
}
\tag{A3.8}
\]

---

## 2. Gram-Faktorisierung

Da
\[
A=R_{T_0}^*R_{T_0},
\]
gilt exakt
\[
\boxed{
\mathfrak G_R
=
J_R^*J_R
+
(R_{T_0}J_R)^*(R_{T_0}J_R).
}
\tag{A3.9}
\]

Damit ist \(\mathfrak G_R\) ein echter positiver Gramoperator der vollständigen freien KNF-Koordinaten.

Schreibe
\[
\mathcal F_R
=
\mathcal Z_R^+
\oplus
L^2(\mathcal V_R^{\rm SW1}).
\]
Dann besitzt \(\mathfrak G_R\) die Blockform
\[
\boxed{
\mathfrak G_R
=
\begin{pmatrix}
\mathfrak G_{zz}&\mathfrak G_{zh}\\
\mathfrak G_{hz}&\mathfrak G_{hh}
\end{pmatrix},
}
\tag{A3.10}
\]
mit
\[
\mathfrak G_{hz}=\mathfrak G_{zh}^*.
\]

Da der blinde Anteil und der rekonstruierte Sample-Anteil von \(J_R(z,h)\) a.e. disjunkte physische Supporte besitzen, hat der Identitätsteil \(J_R^*J_R\) keine \(z/h\)-Kreuzterme.

Somit entstehen
\[
\mathfrak G_{zh},\ \mathfrak G_{hz}
\]
ausschließlich aus dem Rest-Gramanteil
\[
(R_{T_0}J_R)^*(R_{T_0}J_R).
\tag{A3.11}
\]

---

## 3. Exakte Identität für das Kompressionsinverse

Definiere
\[
\boxed{
\mathcal R_K
:=
J_R\mathfrak G_R^{-1}J_R^*
:
\mathscr H_+\to K.
}
\tag{A3.12}
\]

Wir zeigen
\[
\boxed{
\mathcal R_K
=
G^{-1}P.
}
\tag{A3.13}
\]

Sei \(z\in\mathscr H_+\) und setze
\[
\xi
:=
\mathfrak G_R^{-1}J_R^*z,
\qquad
k:=J_R\xi\in K.
\tag{A3.14}
\]

Für jedes
\[
\ell=J_R\eta\in K
\]
gilt
\[
\begin{aligned}
\langle\mathscr T k,\ell\rangle
&=
\langle\mathscr T J_R\xi,J_R\eta\rangle\\
&=
\langle\mathfrak G_R\xi,\eta\rangle\\
&=
\langle J_R^*z,\eta\rangle\\
&=
\langle z,J_R\eta\rangle\\
&=
\langle z,\ell\rangle.
\end{aligned}
\tag{A3.15}
\]

Daher
\[
P\mathscr T k
=
Pz.
\]
Weil \(k\in K\),
\[
Gk=Pz.
\]
Also
\[
k=G^{-1}Pz.
\]

Nach A3.14 ist aber
\[
k=J_R\mathfrak G_R^{-1}J_R^*z.
\]
Damit folgt A3.13.

---

## 4. Vollständig koordinatisierter Annulusoperator

Einsetzen von A3.13 in A3.1 liefert

\[
\boxed{
\mathcal L_{\rm ann}^{\rm SW1}
=
\left[
I
-
(I+A)
J_R
\mathfrak G_R^{-1}
J_R^*
\right]
HE_{\mathcal A}.
}
\tag{A3.16}
\]

Die rekonstruierte \(y\)-Koordinate eines Kernelkandidaten ist damit

\[
\boxed{
y_w
=
-
J_R
\mathfrak G_R^{-1}
J_R^*
HE_{\mathcal A}w.
}
\tag{A3.17}
\]

Dies ist dieselbe \(y\)-Koordinate wie in A2, nun aber vollständig auf die freien KNF-Koordinaten
\[
(z,h)
\]
zurückgeführt.

---

## 5. Variationsform

Für festes \(w\) setze
\[
z_w:=HE_{\mathcal A}w.
\]

Die freie Koordinate
\[
\xi_w
=
\mathfrak G_R^{-1}J_R^*z_w
\]
ist äquivalent die eindeutige Lösung des coerciven Variationsproblems

\[
\boxed{
\langle
(I+A)J_R\xi_w,
J_R\eta
\rangle
=
\langle
HE_{\mathcal A}w,
J_R\eta
\rangle
\quad
\forall\eta\in\mathcal F_R.
}
\tag{A3.18}
\]

Äquivalent ist \(\xi_w\) der eindeutige Minimierer des reellen Teils des quadratischen Funktionals
\[
\boxed{
\mathcal E_w(\xi)
=
\frac12
\langle\mathfrak G_R\xi,\xi\rangle
-
\operatorname{Re}
\langle J_R^*HE_{\mathcal A}w,\xi\rangle.
}
\tag{A3.19}
\]

Die strikte Coercivität A3.7 gibt Existenz und Eindeutigkeit ohne zusätzliche Closed-Range-Annahme.

---

## 6. Finite-cell Struktur von \(\mathfrak G_R\)

A0 liefert die exhaustive freie Koordinatenpartition.

A1 liefert auf jeder dieser Zellen die vollständige Darstellung von
\[
(I+A)J_R
\]
durch endlich viele

- Restriktionen;
- Nullfortsetzungen;
- Translationen;
- Reflexionen;

mit Jacobi-Betrag \(1\).

Der KNF-Rekonstruktionsoperator \(J_R\) selbst besteht ebenfalls nur aus endlich vielen solchen Pullbacks plus festen Skalaren
\[
1,\quad r/p,\quad q/p.
\]

Daher ist
\[
\boxed{
\mathfrak G_R=J_R^*(I+A)J_R
}
\]
auf der A0/A1-Zellzerlegung eine **explizite endliche operatorwertige Gram-Matrix** auf
\[
\mathcal Z_R^+
\oplus
L^2(\mathcal V_R^{\rm SW1}).
\tag{A3.20}
\]

Die Matrixeinträge bleiben Operatoren zwischen \(L^2\)-Intervallen. A3 behauptet keine Reduktion auf eine skalare endliche Matrix.

---

## 7. Was damit wirklich noch offen ist

A3 beseitigt eine wichtige Koordinatenunschärfe:

Nicht mehr gesucht werden muss, wie man \(G^{-1}\) korrekt durch die nichtunitäre KNF-Normalform zieht.

Der exakte freie Koordinatenoperator ist
\[
\mathfrak G_R=J_R^*(I+A)J_R,
\]
und
\[
G^{-1}P
=
J_R\mathfrak G_R^{-1}J_R^*.
\]

Offen bleibt nun ausschließlich die konkrete Wirkung von
\[
\mathfrak G_R^{-1}
\]
auf
\[
J_R^*HE_{\mathcal A}w
\]
und anschließend die Injektivität von A3.16.

---

## 8. Nächster Knoten

Der nächste aktive Knoten ist daher

\[
\boxed{
\text{A4: Struktur von }\mathfrak G_R
\text{ auf den A0-Zellen — Blockgraph, Orbits und mögliche Triangularität.}
}
\tag{A3.21}
\]

Insbesondere ist zu prüfen, ob

1. der freie Zellgraph unter den Translationen/Reflexionen in endlich große Orbits zerfällt;
2. eine gerichtete/trianguläre Zellordnung existiert;
3. oder ein echter unendlicher Transfermechanismus verbleibt.

Erst ein solcher Befund entscheidet, ob
\[
\mathfrak G_R^{-1}
\]
explizit lokal/finit berechenbar wird oder ob eine andere funktionalanalytische Injektivitätsmethode nötig ist.

**Firewall:** A3 beweist keine Injektivität von
\(\mathcal L_{\rm ann}^{\rm SW1}\), keinen trivialen Schur-Kern, kein HT-RED,
keine Closed-Range-/bounded-below-Aussage, kein Objekt X und keine RH-Folgerung.
