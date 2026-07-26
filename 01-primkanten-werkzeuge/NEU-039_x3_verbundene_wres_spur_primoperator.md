# NEU-39 — X.3.9: Verbundene \(Wres\)-Spur und BC-intrinsischer Primoperator \(\mathcal P_N\)

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-36–38  
**Ziel:** Erzeuge die Mangoldt-Schicht

\[
\frac{\zeta_N'}{\zeta_N}(\beta)
=
-\sum_{n\in S_N}\Lambda_N(n)n^{-\beta}
\]

nicht aus der naiven KMS-Spur, sondern aus einer verbundenen/logarithmischen \(Wres\)-Spur auf dem primitiven Primsektor.

---

## 0. Ausgangspunkt

NEU-38 hat die drei Ebenen getrennt:

\[
\text{KMS-Normierung}
\Rightarrow
\zeta_N(\beta)^{-1}
=
\sum_{n\in S_N}\mu_N(n)n^{-\beta},
\]

\[
\text{verbundene/logarithmische Spur}
\Rightarrow
\frac{\zeta_N'}{\zeta_N}(\beta)
=
-\sum_{n\in S_N}\Lambda_N(n)n^{-\beta},
\]

\[
\text{Gamma-Korrektur}
\Rightarrow
\frac{\xi'}{\xi}.
\]

Damit ist klar:

\[
\boxed{
\text{Mangoldt entsteht nicht auf der naiven Trace-Ebene.}
}
\]

Mangoldt entsteht erst auf der Euler-kumulativen, also verbundenen/logarithmischen Ebene.

NEU-39 konstruiert genau diese Ebene endlich bei \(N\).

---

## 1. Warum der naive Primoperator falsch ist

Ein naheliegender, aber falscher Kandidat wäre

\[
\mathcal P_N^{naiv}(\beta)
=
\sum_{p\le N}p^{-\beta}V_p.
\]

Dann gilt wegen der Kommutativität von \(N^\times\):

\[
(\mathcal P_N^{naiv})^k
=
\sum_{p_1,\dots,p_k\le N}
(p_1\cdots p_k)^{-\beta}V_{p_1\cdots p_k}.
\]

Es treten also gemischte Wörter auf:

\[
pq,\quad pqr,\quad p^2q,\dots
\]

Die daraus entstehende logarithmische Spur wäre strukturell von der Form

\[
\log\left(1-\sum_{p\le N}p^{-\beta}\right),
\]

nicht

\[
\sum_{p\le N}\log(1-p^{-\beta}).
\]

Also:

\[
\boxed{
\mathcal P_N^{naiv}
\text{ ist nicht der Euler-Primoperator.}
}
\]

Status: ✓ [M]

---

## 2. Der richtige Primsektor: primitive Richtungen, nicht Produkte

Sei

\[
S_N:=\langle p\le N\rangle
\]

die von den Primzahlen \(p\le N\) erzeugte freie kommutative Halbgruppe.

Die Eulerproduktstruktur kommt nicht aus der gesamten Halbgruppe \(S_N\), sondern aus ihren primitiven Generatoren:

\[
\operatorname{Prim}_N
:=
\{p:\ p\le N,\ p\text{ prim}\}.
\]

Definiere den endlichen primitiven Primraum

\[
\mathfrak p_N
:=
\bigoplus_{p\le N}\mathbb C\,\varepsilon_p.
\]

Dieser Raum ist BC-intrinsisch als Grad-1-Primquotient der freien kommutativen Monoidstruktur zu verstehen:

\[
\mathfrak p_N
\cong
\operatorname{Gr}_\Omega^1(S_N)
\]

bzw. auf der Algebra-Seite als der von den Symbolklassen der \(V_p\) erzeugte primitive Quotient.

Wichtig:

\[
\mathfrak p_N
\text{ ist kein Unteralgebra-Produktsektor,}
\]

sondern der primitive Erzeugersektor.  
Produkte \(pq\) entstehen erst in der symmetrischen Algebra

\[
\operatorname{Sym}(\mathfrak p_N),
\]

nicht in \(\mathfrak p_N\) selbst.

Status: ✓ [M]

---

## 3. Definition des BC-Primoperators

Auf \(\mathfrak p_N\) definieren wir den endlichen Primoperator

\[
\boxed{
\mathcal P_N(\beta)\varepsilon_p
=
p^{-\beta}\varepsilon_p.
}
\tag{39.1}
\]

Äquivalent:

\[
\mathcal P_N(\beta)
=
\bigoplus_{p\le N}p^{-\beta}\operatorname{id}_{\mathbb C\varepsilon_p}.
\]

Dies ist kein willkürlicher Nullstellenoperator.  
Er verwendet nur:

1. die primitive Zerlegung von \(N^\times\),
2. die BC-Zeit-/KMS-Gewichtung \(p^{-\beta}\),
3. die endliche Primtrunkierung \(p\le N\).

Status: ✓ [M] als endlicher Euler-Primoperator.

---

## 4. Verbundene \(Wres\)-Spur auf dem Primsektor

Die \(Wres\)-Paarung aus OP-4.1 lebt auf dem \(B_3\)-Sektor.  
Für den primitiven Primquotienten verwenden wir die durch \(L_3^\circ\) normalisierte verbundene Spur:

\[
\operatorname{Tr}_{Wres,N}^{conn}
:
\operatorname{End}(\mathfrak p_N)\to\mathbb C
\]

mit der Normalisierung

\[
\boxed{
\operatorname{Tr}_{Wres,N}^{conn}
(\operatorname{id}_{\mathbb C\varepsilon_p})=1
}
\tag{39.2}
\]

für jede primitive Primrichtung \(p\le N\).

Diese Normierung ist genau die endliche Primkanal-Normierung.  
Sie ist die verbundene Version der \(Wres\)-Spur: sie zählt primitive Eulerkanäle einmal und ignoriert gemischte Produktwörter auf der primitiven Ebene.

Damit gilt:

\[
\boxed{
\operatorname{Tr}_{Wres,N}^{conn}
(\mathcal P_N(\beta)^k)
=
\sum_{p\le N}p^{-k\beta}.
}
\tag{39.3}
\]

Status: ✓ [M] innerhalb des primitiven Primquotienten.  
Die vollständige Realisierung als stetiger Quotient von \(B_3\) hängt weiterhin an OP-4.1a: ⚠ [M].

---

## 5. Euler-Kumulanten-Identität

Definiere die verbundene Euler-Funktion

\[
\boxed{
\Phi_N(\beta)
:=
\operatorname{Tr}_{Wres,N}^{conn}
\log(1-\mathcal P_N(\beta)).
}
\tag{39.4}
\]

Für \(\Re(\beta)>1\) ist wegen \(p^{-\beta}<1\):

\[
\log(1-\mathcal P_N(\beta))
=
-\sum_{k\ge1}\frac1k\mathcal P_N(\beta)^k.
\]

Also:

\[
\Phi_N(\beta)
=
-\sum_{k\ge1}\frac1k
\operatorname{Tr}_{Wres,N}^{conn}(\mathcal P_N(\beta)^k).
\]

Mit (39.3):

\[
\Phi_N(\beta)
=
-\sum_{k\ge1}\frac1k
\sum_{p\le N}p^{-k\beta}.
\]

Vertauschen der endlichen Primsumme mit der absolut konvergenten \(k\)-Summe liefert:

\[
\Phi_N(\beta)
=
\sum_{p\le N}\log(1-p^{-\beta}).
\]

Somit:

\[
\boxed{
\Phi_N(\beta)
=
\log\prod_{p\le N}(1-p^{-\beta})
=
-\log \zeta_N(\beta).
}
\tag{39.5}
\]

Status: ✓ [M]

---

## 6. Mangoldt aus der logarithmischen Ableitung

Differenziere (39.5):

\[
\partial_\beta \Phi_N(\beta)
=
\sum_{p\le N}
\frac{\log(p)p^{-\beta}}{1-p^{-\beta}}.
\]

Also:

\[
\partial_\beta \Phi_N(\beta)
=
\sum_{p\le N}\sum_{k\ge1}
\log(p)p^{-k\beta}.
\]

Die endliche Mangoldt-Funktion \(\Lambda_N\) auf \(S_N\) ist:

\[
\Lambda_N(n)
=
\begin{cases}
\log p,& n=p^k,\ p\le N,\ k\ge1,\\
0,& n\text{ hat mindestens zwei verschiedene Primfaktoren}.
\end{cases}
\]

Daher:

\[
\boxed{
\partial_\beta \Phi_N(\beta)
=
\sum_{n\in S_N}\Lambda_N(n)n^{-\beta}.
}
\tag{39.6}
\]

Da

\[
\frac{\zeta_N'}{\zeta_N}(\beta)
=
-\sum_{n\in S_N}\Lambda_N(n)n^{-\beta},
\]

folgt:

\[
\boxed{
-\partial_\beta
\operatorname{Tr}_{Wres,N}^{conn}
\log(1-\mathcal P_N(\beta))
=
\frac{\zeta_N'}{\zeta_N}(\beta).
}
\tag{39.7}
\]

Dies ist die gesuchte Euler-Kumulanten-Identität in BC-Sprache.

Status: ✓ [M]

---

## 7. Interpretation: Warum gemischte Produkte verschwinden

Die verbundene Spur zählt nicht Elemente der ganzen Halbgruppe \(S_N\), sondern primitive Eulerkanäle.

Formal:

\[
\operatorname{Tr}^{conn}
\log(1-\mathcal P_N)
\]

ist der logarithmische Kumulant der freien kommutativen Monoidzerlegung

\[
S_N
\cong
\bigoplus_{p\le N}\mathbb N\cdot p.
\]

Der Logarithmus verwandelt Produktfaktorisierung in Summe:

\[
\log\prod_{p\le N}(1-p^{-\beta})
=
\sum_{p\le N}\log(1-p^{-\beta}).
\]

Deshalb überleben in der verbundenen Spur genau die Primzahlpotenz-Kanäle

\[
p^k,
\]

nicht die gemischten Produktkanäle

\[
p^a q^b,\qquad p\ne q.
\]

Status: ✓ [M]

---

## 8. Verhältnis zu Möbius

NEU-38 zeigte:

\[
\frac{1}{\zeta_N(\beta)}
=
\sum_{n\in S_N}\mu_N(n)n^{-\beta}.
\]

Das ist die naive KMS-Normierung.

NEU-39 zeigt dagegen:

\[
-\partial_\beta\log\zeta_N(\beta)
=
-\frac{\zeta_N'}{\zeta_N}(\beta)
=
\sum_{n\in S_N}\Lambda_N(n)n^{-\beta}.
\]

Damit ist die Beziehung:

\[
\boxed{
\text{Möbius}=\text{multiplikative Inversion},
}
\]

\[
\boxed{
\text{Mangoldt}=\text{logarithmischer Euler-Kumulant}.
}
\]

Status: ✓ [M]

---

## 9. Kopplung an \(L_3^\circ\)

Die Normierung in (39.2) ist durch \(L_3^\circ=C_L^{-1}L_3\) zu verstehen.

Ohne Normierung erhält man:

\[
\operatorname{Tr}_{Wres,N}^{conn,L_3}
(\operatorname{id}_{\mathbb C\varepsilon_p})
=
C_L.
\]

Dann wird (39.7) zu:

\[
-\partial_\beta
\operatorname{Tr}_{Wres,N}^{conn,L_3}
\log(1-\mathcal P_N(\beta))
=
C_L\frac{\zeta_N'}{\zeta_N}(\beta).
\]

Mit \(L_3^\circ\) verschwindet der Faktor \(C_L\).

Status: ✓ [M]

---

## 10. Gamma-Korrektur bleibt getrennt

NEU-39 erzeugt nur die endliche nichtarchimedische Euler-Schicht:

\[
\frac{\zeta_N'}{\zeta_N}.
\]

Die vollständige \(\xi\)-Schicht benötigt zusätzlich:

\[
\frac{\xi'}{\xi}(s)
=
\frac{\zeta'}{\zeta}(s)
+
\text{archimedische Gamma-/Polterme}.
\]

Daher bleibt:

\[
\boxed{
\text{intrinsische Gamma-Faktor-Realisierung}
}
\]

weiterhin ein eigener offener Punkt.

Status: ❓ [O]

---

## 11. Einbettung in die X.3-Kette

Die bisherige X.3-Kette lautet nun:

\[
J_N^-
\Rightarrow
\text{Jacobi-Cauchy-Transformierte}
\]

\[
\phi_\beta+\Delta_\beta^{-1}
\Rightarrow
\zeta_N^{-1}
\]

\[
\operatorname{Tr}_{Wres}^{conn}\log(1-\mathcal P_N)
\Rightarrow
\frac{\zeta_N'}{\zeta_N}
\]

\[
\Gamma\text{-Korrektur}
\Rightarrow
\frac{\xi'}{\xi}.
\]

Damit ist die Mangoldt-Schicht geschlossen, aber ihre Kopplung an den Jacobi-Operator \(D_N^-\) ist noch nicht automatisch bewiesen.

Der neue offene Punkt ist:

\[
\boxed{
\text{Kompatibilität von }\mathcal P_N
\text{ mit }J_N^-\text{ und }D_N^-.
}
\]

Status: ❓ [O]

---

## 12. Vergleich mit NEU-37

NEU-37 zeigte:

\[
H_N^-(z)
=
\sum_{n,a,M}\text{Jacobi-Cauchy-Transformierte}.
\]

NEU-39 zeigt separat:

\[
-\partial_\beta
\operatorname{Tr}_{Wres,N}^{conn}
\log(1-\mathcal P_N(\beta))
=
\frac{\zeta_N'}{\zeta_N}(\beta).
\]

Damit ist klar:

\[
H_N^-(z)
\neq
\frac{\zeta_N'}{\zeta_N}(z)
\]

ohne zusätzliche Identifikation.

Die fehlende Brücke muss die beiden Funktionen verbinden:

\[
\boxed{
\text{Jacobi-Resolvent von }D_N^-
\quad\longleftrightarrow\quad
\text{Euler-Kumulant von }\mathcal P_N.
}
\]

Status: ❓ [O]

---

## 13. Möglicher Brückenoperator

Ein natürlicher Ansatz ist ein zweistufiger Operator:

\[
\mathbb D_N
=
D_N^-
\oplus
\mathcal E_N,
\]

wobei

\[
\mathcal E_N
\]

die Euler-/Primkanal-Komponente mit

\[
\det(1-\mathcal P_N(\beta))
=
\zeta_N(\beta)^{-1}
\]

trägt.

Dann müsste gezeigt werden, dass die \(Wres\)-Frobeniuskopplung über \(L_3^\circ\) diese beiden Komponenten nicht additiv nebeneinanderstellt, sondern durch einen Schur-Komplement-/Feshbach-Mechanismus koppelt:

\[
\det(s-\mathbb D_N)
=
\det(s-D_N^-)\cdot
\det(1-\mathcal P_N(s))
\cdot
\det(\text{Kopplung}).
\]

Der nichttriviale Zielausdruck wäre:

\[
\partial_s\log\det_{Wres}(s-\mathbb D_N)
=
\frac{\xi_N'}{\xi_N}(s)+\varepsilon_N(s).
\]

Status: ❓ [O]

---

## 14. Satz 39.1 — Euler-Kumulanten-Satz

Für den primitiven Primoperator

\[
\mathcal P_N(\beta)\varepsilon_p=p^{-\beta}\varepsilon_p
\]

und die normalisierte verbundene \(Wres\)-Spur gilt:

\[
\operatorname{Tr}_{Wres,N}^{conn}
\log(1-\mathcal P_N(\beta))
=
-\log\zeta_N(\beta).
\]

Folglich:

\[
-\partial_\beta
\operatorname{Tr}_{Wres,N}^{conn}
\log(1-\mathcal P_N(\beta))
=
\frac{\zeta_N'}{\zeta_N}(\beta).
\]

Status: ✓ [M]

---

## 15. Satz 39.2 — No-Go für den naiven Halbgruppenoperator

Der Operator

\[
\mathcal P_N^{naiv}=\sum_{p\le N}p^{-\beta}V_p
\]

erzeugt wegen gemischter Wörter nicht das Eulerprodukt

\[
\prod_{p\le N}(1-p^{-\beta}).
\]

Er ist daher kein gültiger Primoperator für die Mangoldt-Schicht.

Status: ✓ [M]

---

## 16. Statusmatrix

| Aussage | Status |
|---|---:|
| primitiver Primsektor \(\mathfrak p_N\) | ✓ [M] |
| blockdiagonaler Primoperator \(\mathcal P_N\) | ✓ [M] |
| verbundene \(Wres\)-Spur auf \(\mathfrak p_N\) | ✓ [M] / OP-4.1a global ⚠ |
| \(\operatorname{Tr}^{conn}\log(1-\mathcal P_N)=-\log\zeta_N\) | ✓ [M] |
| Mangoldt durch \(-\partial_\beta\) | ✓ [M] |
| No-Go für \(\sum p^{-\beta}V_p\) | ✓ [M] |
| Gamma-Faktor-Intrinsifizierung | ❓ [O] |
| Kopplung \(\mathcal P_N\leftrightarrow J_N^-\) | ❓ [O] |
| Einbau in einen einzigen geometrischen Operator \(D_X^{geom}\) | ❓ [O] |

---

## 17. Fazit

NEU-39 schließt die Mangoldt-Schicht auf endlichem Niveau:

\[
\boxed{
\mathcal P_N
+
\operatorname{Tr}_{Wres}^{conn}
\Longrightarrow
\frac{\zeta_N'}{\zeta_N}.
}
\]

Der entscheidende Fortschritt ist die Korrektur:

\[
\text{Mangoldt kommt nicht aus der naiven KMS-Spur,}
\]

sondern aus

\[
\boxed{
\text{dem logarithmischen Euler-Kumulanten der primitiven Primkanäle.}
}
\]

Der neue Engpass ist nicht mehr die Erzeugung von Mangoldt selbst, sondern die Verbindung dieser Euler-Kumulanten-Schicht mit dem Jacobi-Operator aus \(D_N^-\):

\[
\boxed{
\text{NEU-40: Kopplung von }\mathcal P_N
\text{ und }J_N^- \text{ via } Wres\text{-Frobenius-Schur-Komplement.}
}
