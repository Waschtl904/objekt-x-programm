# P11 Audit — exact Feshbach pullback block identity

**Datum:** 15. September 2026  
**Basis:** exact Rest pullback monotonicity and P11 Feshbach kernel `B_R=(I+R_R^*R_R)^{-1}`.  
**Rolle:** exakte Blockreduktion des nichttrivialen Radius-/Terminaldefekts.  
**Registry:** unveraendert.  
**Nonclaim:** kein Beweis terminaler Konvergenz; kein Vorzeichenclaim fuer die Differenz der Feshbachterme; kein RH-Beweis.

---

## 0. Kurzurteil

Nach der positiven Rest-Inkrementidentitaet bleibt beim inversen Restkern ein exakt lokalisierter Konkurrenzmechanismus.

Fuer `0<R<S` zerlege

```math
L^2(-S,S)
=E_{R,S}L^2(-R,R)\oplus\mathscr N_{R,S}.
```

Mit

```math
A:=R_SE_{R,S},
\qquad
C:=R_SQ_{R,S}
```

(`Q_{R,S}` = orthogonale Projektion auf den neuen Source-Komplementraum) gilt

```math
\boxed{
E_{R,S}^*B_SE_{R,S}
=
\left[I+A^*(I+CC^*)^{-1}A\right]^{-1}.
}
```

Aus der Rest-Inkrementidentitaet

```math
A^*A
=R_R^*R_R+\Delta_{R,S}^*\Delta_{R,S}
```

folgt aequivalent

```math
\boxed{
(E^*B_SE)^{-1}
=B_R^{-1}
+\Delta^*\Delta
-\mathfrak C_{R,S},
}
```

mit

```math
\boxed{
\mathfrak C_{R,S}
=A^*C(I+C^*C)^{-1}C^*A\succeq0.
}
```

Der komprimierte Zukunftskern wird somit durch die Konkurrenz zweier **manifest positiver** Operatoren bestimmt:

```text
+ neue Restinnovationen       Delta*Delta
- neue Source-Rueckkopplung   C_feedback.
```

Dies ist eine exakte Reduktion, keine Abschaetzung.

Status:

```text
compression-of-inverse block formula                    ✓[M]
positive future-source feedback operator                 ✓[M]
exact inverse defect identity                            ✓[M]
old/new Rest orthogonality => inverse monotone decrease  ✓[M]
general sign of E^*B_SE-B_R                              ?[O]
corresponding sign/limit of Sigma pullback               ?[O]
```

---

# 1. Source-Blockzerlegung

Schreibe kurz

```math
E=E_{R,S},
\qquad
P=EE^*,
\qquad
Q=I-P.
```

Dann ist

```math
L^2(-S,S)=\operatorname{Ran}E\oplus\operatorname{Ran}Q.
```

Definiere

```math
A:=R_SE,
\qquad
C:=R_SQ.
```

Relativ zu dieser Zerlegung lautet

```math
I+R_S^*R_S
=
\begin{pmatrix}
I+A^*A&A^*C\\
C^*A&I+C^*C
\end{pmatrix}.
```

Der untere Block ist strikt positiv:

```math
I+C^*C\succeq I.
```

---

# 2. Schur-Komplement des neuen Source-Raums

Das Schur-Komplement des unteren Blocks ist

```math
\mathscr S_{R,S}
=I+A^*A
-A^*C(I+C^*C)^{-1}C^*A.
```

Die Standardidentitaet

```math
I-C(I+C^*C)^{-1}C^*
=(I+CC^*)^{-1}
```

liefert

```math
\boxed{
\mathscr S_{R,S}
=I+A^*(I+CC^*)^{-1}A.
}
```

Da der obere linke Block der Inversen eines positiven Blockoperators die Inverse seines Schur-Komplements ist,

```math
\boxed{
E^*(I+R_S^*R_S)^{-1}E
=\mathscr S_{R,S}^{-1}.
}
```

Also mit `B_S=(I+R_S^*R_S)^{-1}`

```math
\boxed{
E^*B_SE
=
\left[I+A^*(I+CC^*)^{-1}A\right]^{-1}.
}
```

---

# 3. Einsetzen der exakten Rest-Inkrementidentitaet

Der Rest-Monotonie-Audit liefert

```math
A^*A
=E^*R_S^*R_SE
=R_R^*R_R+\Delta^*\Delta.
```

Setze

```math
\boxed{
\mathfrak C_{R,S}
:=A^*C(I+C^*C)^{-1}C^*A.
}
```

Dann

```math
\mathfrak C_{R,S}\succeq0
```

und

```math
\mathscr S_{R,S}
=I+R_R^*R_R+\Delta^*\Delta-\mathfrak C_{R,S}.
```

Da

```math
B_R^{-1}=I+R_R^*R_R,
```

folgt die zentrale Identitaet

```math
\boxed{
(E^*B_SE)^{-1}
=B_R^{-1}
+\Delta_{R,S}^*\Delta_{R,S}
-\mathfrak C_{R,S}.
}
```

---

# 4. Interpretation des Feedbackterms

Der Operator

```math
C=R_SQ
```

ist die Restabbildung der **neuen Source-Freiheitsgrade** im groesseren Fenster.

Der Kreuzoperator

```math
C^*A
```

misst, wie stark alte und neue Source-Vektoren im selben finite-adischen Restziel korrelieren.

Damit ist

```math
\mathfrak C_{R,S}
=A^*C(I+C^*C)^{-1}C^*A
```

genau die positive Feshbach-Rueckkopplung, die beim Eliminieren des neuen Source-Komplements auf den alten Source-Raum zurueckwirkt.

Ohne diese Kopplung (`C^*A=0`) gaebe es nur die positive Restinnovation.

---

# 5. Orthogonaler Spezialfall

Falls

```math
C^*A=0,
```

also die alten und neuen Source-Bilder unter `R_S` orthogonal sind, gilt

```math
\mathfrak C_{R,S}=0
```

und daher

```math
(E^*B_SE)^{-1}
=B_R^{-1}+\Delta^*\Delta
\succeq B_R^{-1}.
```

Somit

```math
\boxed{E^*B_SE\preceq B_R.}
```

Jede Abweichung von dieser naiven inversen Monotonie wird also vollstaendig durch die old/new Source-Kopplung `C^*A` getragen.

---

# 6. Allgemeine Sandwich-Aussage

Da

```math
0\prec(I+CC^*)^{-1}\preceq I,
```

folgt

```math
0\preceq A^*(I+CC^*)^{-1}A\preceq A^*A.
```

Daher

```math
\boxed{
(I+A^*A)^{-1}
\preceq
E^*B_SE
\preceq I.
}
```

Mit

```math
A^*A=B_R^{-1}-I+\Delta^*\Delta
```

ist die linke Seite explizit

```math
\boxed{
(B_R^{-1}+\Delta^*\Delta)^{-1}
\preceq E^*B_SE.
}
```

Eine allgemeine Ordnung zwischen `E^*B_SE` und `B_R` folgt daraus nicht.

---

# 7. Pullback des Hub-Feshbachterms: exakte Blockform

Der P11-Schurterm ist

```math
\Sigma_S=H_SB_SH_S^*.
```

Setze

```math
K:=H_S^*E:L^2(-R,R)\to L^2(-S,S)
```

und zerlege

```math
K=EK_0+K_1,
\qquad
K_0=E^*K,
\qquad
K_1=QK.
```

Schreibe

```math
D:=I+C^*C,
\qquad
M:=I+A^*A-A^*CD^{-1}C^*A.
```

Dann liefert die Standard-Blockinverse fuer jeden alten Source-Vektor die exakte quadratische Zerlegung

```math
\boxed{
E^*\Sigma_SE
=
(K_0-A^*CD^{-1}K_1)^*M^{-1}
(K_0-A^*CD^{-1}K_1)
+K_1^*D^{-1}K_1.
}
```

Beide Summanden sind positiv.

Damit ist der Pullback des Zukunfts-Hubterms vollstaendig in vier explizite Daten zerlegt:

```text
A = alte Source -> Restziel,
C = neue Source -> Restziel,
K0 = alter Source-Anteil des Zukunftshubs,
K1 = neuer Source-Anteil des Zukunftshubs.
```

Die erste Klammer ist der durch Rest-Feedback korrigierte alte Hub; der zweite Summand ist die direkte positive neue-Source-Hubenergie.

---

# 8. Der konkrete Terminal-Gate

Statt des gesamten Zukunftsoperators muss fuer festen alten Radius `R` nun die Familie

```math
\Delta_{R,S},
\qquad
\mathfrak C_{R,S},
\qquad
K_0(R,S),
\qquad
K_1(R,S)
```

unter `S->infty` verstanden werden.

Das Terminalproblem ist damit auf folgende konkrete Fragen reduziert:

```text
1. Wie gross ist future-source feedback C_feedback relativ zur positiven Restinnovation Delta*Delta?
2. Stabilisiert der feedback-korrigierte alte Hub K0-A*CD^-1K1?
3. Verschwindet / konvergiert der direkte neue-Source-Hubterm K1*D^-1K1 nach der bereits bekannten Terminalnormalisierung?
4. Ist diese Blockreduktion mit den bestehenden P11-Metriktransporten G_{R,T}, W_{R,S}^{[T]} kompatibel?
```

Diese Daten sind vorwaerts aus den vorhandenen P11-Operatoren definiert; kein Weil-Positivitaetsinput wird verwendet.
