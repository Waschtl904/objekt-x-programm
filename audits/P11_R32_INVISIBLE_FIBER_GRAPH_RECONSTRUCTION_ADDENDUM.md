# P11/R32 — FG-Rekonstruktionsaddendum: exakte Branch-Domains und Exhaustivität

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** `audits/P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md`.  
**Ziel:** die für FG-1 entscheidende Exhaustivitäts-/Rekonstruktionsstelle funktionalanalytisch präzisieren. Insbesondere werden die Horizon-Cuts als echte Branch-Domains und nicht nur formal als Indikatoren behandelt.

---

## 1. Setup

Im Drei-Shift-Fenster
\[
2a<T_0<c=\tfrac12\log5,
\qquad T_0=T+\varepsilon,
\qquad T=2a,
\]
mit
\[
a=\tfrac12\log2,
\quad b=\tfrac12\log3,
\quad d=b-a,
\quad e=T-b,
\]
sei
\[
0<R<a.
\]
Für gerade `y` gilt auf `0<u<R`
\[
(E_I^*Hy)(u)
=p[y(a-u)-y(a+u)]
+r[y(b-u)-y(b+u)]
+q[y(T-u)-y(T+u)],
\]
wobei Werte außerhalb `(-T_0,T_0)` als Null verstanden werden.

Der positive gesampelte physische Bereich ist
\[
\mathcal U_R
=
\bigcup_{\tau\in\{a,b,T\}}
(\tau-R,\tau+R)\cap(0,T_0).
\]

---

## 2. Exakte Branch-Domains

Wir verwenden sechs Branchindizes
\[
\mathcal I=\{A_-,A_+,B_-,B_+,C_-,C_+\}.
\]
Ihre echten Parameterdomains sind
\[
D_{A_-}=D_{A_+}=D_{B_-}=D_{C_-}=(0,R),
\]
\[
\boxed{D_{B_+}=(0,\min\{R,e+\varepsilon\})},
\]
\[
\boxed{D_{C_+}=(0,\min\{R,\varepsilon\})}.
\]
Die zugehörigen affinen Branchkarten sind
\[
\pi_{A_-}(u)=a-u,
\quad
\pi_{A_+}(u)=a+u,
\]
\[
\pi_{B_-}(u)=b-u,
\quad
\pi_{B_+}(u)=b+u,
\]
\[
\pi_{C_-}(u)=T-u,
\quad
\pi_{C_+}(u)=T+u.
\]
Da `R<a`, liegen die vier unverkürzten Branches vollständig in `(0,T_0)`. Die beiden verkürzten Domains sind exakt
\[
T_0-b=e+\varepsilon,
\qquad
T_0-T=\varepsilon.
\]

Ferner gilt exakt
\[
\boxed{
\mathcal U_R=\bigcup_{i\in\mathcal I}\pi_i(D_i)
}
\]
bis auf Endpunkte.

---

## 3. Branch-Hilbertraum und Gluing-Unterraum

Definiere
\[
\mathscr B_R:=\bigoplus_{i\in\mathcal I}L^2(D_i).
\]
Für `F=(F_i)_i in B_R` wird auf jedem nichtleeren physischen Überlapp
\[
O_{ij}:=\pi_i(D_i)\cap\pi_j(D_j)
\]
die Gluing-Bedingung verlangt:
\[
\boxed{
F_i(\pi_i^{-1}(t))=F_j(\pi_j^{-1}(t))
\quad\text{für a.e. }t\in O_{ij}.
}
\tag{RA.1}
\]
Bezeichne den Raum aller solcher Familien mit
\[
\mathfrak G_R\subset\mathscr B_R.
\]

Jede Bedingung (RA.1) ist der Kern eines beschränkten Differenzoperators zwischen `L2`-Restriktionen auf `O_ij`; da es nur endlich viele Branchpaare gibt, ist
\[
\boxed{\mathfrak G_R\text{ ein abgeschlossener Hilbert-Unterraum von }\mathscr B_R.}
\tag{RA.2}
\]
Mehrfachüberlappungen erfordern keine zusätzliche Bedingung: paarweises a.e. Gluing ist transitiv außerhalb einer endlichen Vereinigung von Nullmengen.

---

## 4. Pullback und Rekonstruktion

Für `g in L^2(U_R)` definiere
\[
(J_Rg)_i:=g\circ\pi_i\in L^2(D_i).
\]
Da jede `pi_i` affine Maßtreue mit Ableitung `+-1` ist, gilt
\[
\|J_Rg\|_{\mathscr B_R}^2
=
\int_{\mathcal U_R}m_R(t)|g(t)|^2\,dt,
\tag{RA.3}
\]
wobei
\[
m_R(t):=\#\{i:t\in\pi_i(D_i)\}
\]
die Branch-Multiplizität ist. Es gilt a.e.
\[
1\le m_R(t)\le6.
\]
Damit
\[
\boxed{
\|g\|_{L^2(U_R)}^2
\le
\|J_Rg\|_{\mathscr B_R}^2
\le
6\|g\|_{L^2(U_R)}^2.
}
\tag{RA.4}
\]
Insbesondere ist `J_R` beschränkt und injektiv, und sein Bild liegt in `G_R`.

### Surjektivität auf den Gluing-Raum

Sei umgekehrt `F in G_R`. Ordne die sechs Branches fest. Zerlege `U_R` messbar in disjunkte Mengen
\[
P_1:=\pi_1(D_1),
\qquad
P_k:=\pi_k(D_k)\setminus\bigcup_{j<k}\pi_j(D_j).
\]
Auf `P_k` setze
\[
(R_RF)(t):=F_k(\pi_k^{-1}(t)).
\]
Diese Definition ist messbar. Wegen des Gluings stimmt sie a.e. mit jeder anderen verfügbaren Branchdarstellung überein. Zudem
\[
\|R_RF\|_{L^2(U_R)}^2
\le
\sum_i\|F_i\|_{L^2(D_i)}^2<\infty.
\]
Also `R_RF in L2(U_R)` und
\[
J_RR_RF=F
\quad\text{a.e.}
\]
Während umgekehrt
\[
R_RJ_Rg=g
\quad\text{a.e.}
\]
gilt.

Damit ist
\[
\boxed{
J_R:L^2(\mathcal U_R)\xrightarrow{\sim}\mathfrak G_R
}
\tag{RA.5}
\]
ein kanonischer beschränkter linearer Isomorphismus mit beschränktem Inversen. Er ist bezüglich des ungegewichteten Direktproduktnorms im Allgemeinen **nicht unitär**, weil physische Überlappungen mehrfach gezählt werden.

---

## 5. Exakter Row-Operator

Um alle sechs Beiträge auf `(0,R)` zu vergleichen, bezeichne mit `E_i` die Nullfortsetzung von `L2(D_i)` nach `L2(0,R)`. Definiere
\[
\boxed{
\Lambda_R F
:=
p(E_{A_-}F_{A_-}-E_{A_+}F_{A_+})
+r(E_{B_-}F_{B_-}-E_{B_+}F_{B_+})
+q(E_{C_-}F_{C_-}-E_{C_+}F_{C_+}).
}
\tag{RA.6}
\]
Dann ist `Lambda_R:G_R -> L2(0,R)` beschränkt.

Für `g in L2(U_R)` ist wegen der exakten Horizon-Domains
\[
\boxed{
\Lambda_RJ_Rg=E_I^*H\,g_{\rm even}
}
\tag{RA.7}
\]
auf `(0,R)`, wobei `g_even` die gerade Fortsetzung auf den gesampelten physischen Bereich bezeichnet und außerhalb davon Null ist.

---

## 6. Blind-/Sample-Zerlegung des gesamten Quellenraums

Sei
\[
\mathcal Z_R^{\rm phys}:=(0,T_0)\setminus\mathcal U_R.
\]
Jedes gerade
\[
y\in L^2(-T_0,T_0)^+
\]
zerfällt eindeutig orthogonal nach positivem physischem Support als
\[
\boxed{
y=y_{\rm blind}+y_{\rm samp},}
\tag{RA.8}
\]
wobei `y_blind` positiv in `Z_R^phys` und `y_samp` positiv in `U_R` getragen ist.

Da `E_I^*H` ausschließlich Punkte aus `U_R` abtastet,
\[
E_I^*Hy_{\rm blind}=0.
\]
Somit
\[
y\in\mathcal N_I
\iff
\Lambda_RJ_R(y_{\rm samp}|_{(0,T_0)})=0.
\]
Mit (RA.5) folgt die exhaustive Normalform
\[
\boxed{
\mathcal N_I
\cong
\mathcal Z_R^+
\oplus
\{F\in\mathfrak G_R:\Lambda_RF=0\}.
}
\tag{RA.9}
\]
Die erste Summe ist die echte orthogonale physische Supportzerlegung. Das Zeichen `cong` im zweiten Summanden bedeutet den beschränkten kanonischen Branch-Isomorphismus (RA.5), nicht eine naive unitäre Identifikation mit dem sechsfachen Direktprodukt.

---

## 7. Was damit wirklich klassifiziert ist

(RA.9) ist **exhaustiv** im folgenden Sinn: Jede Lösung von `E_I^*Hy=0` liegt entweder im automatisch blinden physischen Supportanteil oder ihr gesampelter Anteil ist exakt eine geglühte sechs-Branch-Familie im Kernel einer einzigen beschränkten Row-Relation.

Dies ist jedoch **keine endlichdimensionale Klassifikation**. `G_R` und `ker Lambda_R` sind im Allgemeinen unendlichdimensionale Funktionalräume. Es wird insbesondere nicht behauptet:

- endlich viele irreduzible Schalentypen;
- endlich viele domain-beschränkte Orbits;
- dass CTX/NS/ST den gesamten gegluehten Kernel erzeugen;
- irgendeine neue Schur-Transversalität.

Die richtige nächste Frage bleibt die Zerlegung von
\[
\ker\Lambda_R\cap\mathfrak G_R
\]
unter der domain-beschränkten Overlap-Pseudogruppe.

---

## 8. Kandidatenstatus

Dieses Addendum präzisiert ausschließlich FG-1 und die zugehörige Functional-Analysis-Firewall.

- **FG-1:** weiterhin `?[O]` bis unabhängiges vollständiges GREEN der Rekonstruktion.

Keine Promotion ohne explizite Freigabe.
