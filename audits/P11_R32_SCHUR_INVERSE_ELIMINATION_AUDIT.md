# P11/R32 — Schur-Inversenelimination und augmentierte endliche Shift-Geometrie

**Status:** Kandidat; keine Promotion.  
**Repo-Basis:** `main@06d4290394314edea89d0d04dc824a6b40c52d59`.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Ziel:** den nach der P11↔P12-Rückbindung verbleibenden Schur-Kern
\[
\ker(E_I^*\Sigma_{T_0}E_{\mathcal A})
\]
exakt von der nichtlokalen Inversen
\(B_{T_0}=(I+R_{T_0}^*R_{T_0})^{-1}\)
zu befreien und als gekoppeltes endliches Translations-/Cutoff-System zu formulieren.

---

## 1. Fester Horizont und Parität

Fixiere
\[
0<R<S<T_0,
\qquad
2a<T_0<c:=\frac12\log5,
\]
mit
\[
a=\frac12\log2,
\qquad b=\frac12\log3,
\qquad T=2a=\log2.
\]
Auf
\[
\mathscr H:=L^2(-T_0,T_0)
\]
setze
\[
H:=H_{T_0},
\qquad
\mathcal R:=R_{T_0},
\qquad
A:=\mathcal R^*\mathcal R\ge0,
\qquad
B:=(I+A)^{-1}.
\]
P11 beweist
\[
H^*=-H.
\]
Der Hub wechselt die Parität, \(A\) und \(B\) erhalten sie.

Seien
\[
I=(-R,R),
\qquad
\mathcal A=(-S,-R)\cup(R,S),
\]
mit Nullfortsetzungen \(E_I,E_{\mathcal A}\).
Für die hier relevante ungerade Annulusquelle gilt
\[
HE_{\mathcal A}:\mathscr H_{\mathcal A}^-\to\mathscr H^+.
\]

Der echte post-P12-Schur-Kern ist der Kern des Operators
\[
\boxed{
\mathcal S_{I,A}:=E_I^*\Sigma_{T_0}E_{\mathcal A}
=E_I^*HBH^*E_{\mathcal A}.
}
\tag{SE.1}
\]

---

## 2. Exakte Elimination der nichtlokalen Inversen

Definiere den augmentierten Blockoperator
\[
\boxed{
\mathcal K_{I,A}
:\mathscr H^+\oplus\mathscr H_{\mathcal A}^-
\longrightarrow
\mathscr H^+\oplus\mathscr H_I^-
}
\tag{SE.2}
\]
durch
\[
\boxed{
\mathcal K_{I,A}
\binom{y}{w}
:=
\binom{(I+A)y+HE_{\mathcal A}w}{E_I^*Hy}.
}
\tag{SE.3}
\]
Die Typisierung ist korrekt:

- \(y\) ist gerade;
- \((I+A)y\) ist gerade;
- \(HE_{\mathcal A}w\) ist gerade;
- \(Hy\) ist ungerade;
- \(E_I^*Hy\in\mathscr H_I^-\).

### Theorem SE-1 — Schur-Inversenelimination

Es gibt eine lineare Bijektion
\[
\boxed{
\ker\mathcal S_{I,A}
\longleftrightarrow
\ker\mathcal K_{I,A}
}
\tag{SE.4}
\]
gegeben durch
\[
\boxed{
 w\longmapsto
 \left(BH^*E_{\mathcal A}w,\,w\right).
}
\tag{SE.5}
\]
Insbesondere
\[
\boxed{
\ker\mathcal S_{I,A}=\{0\}
\iff
\ker\mathcal K_{I,A}=\{0\}.
}
\tag{SE.6}
\]

### Beweis

Sei zunächst \(w\in\ker\mathcal S_{I,A}\) und setze
\[
y:=BH^*E_{\mathcal A}w.
\]
Dann
\[
(I+A)y=H^*E_{\mathcal A}w=-HE_{\mathcal A}w,
\]
also ist die erste Komponente von \(\mathcal K_{I,A}(y,w)\) null. Außerdem
\[
E_I^*Hy
=E_I^*HBH^*E_{\mathcal A}w
=\mathcal S_{I,A}w
=0.
\]
Somit \((y,w)\in\ker\mathcal K_{I,A}\).

Umgekehrt erfülle \((y,w)\in\ker\mathcal K_{I,A}\). Aus der ersten Gleichung folgt wegen der Invertierbarkeit von \(I+A\)
\[
y=-(I+A)^{-1}HE_{\mathcal A}w
=BH^*E_{\mathcal A}w.
\]
Die zweite Gleichung gibt dann
\[
0=E_I^*Hy
=E_I^*HBH^*E_{\mathcal A}w
=\mathcal S_{I,A}w.
\]
Damit ist \(w\in\ker\mathcal S_{I,A}\).

Schließlich kann ein Kernelpaar mit \(w=0\) nichttrivial sein: aus
\[
(I+A)y=0
\]
folgt \(y=0\). Daher ist die Projektion des Blockkerns auf die \(w\)-Komponente injektiv und (SE.5) tatsächlich bijektiv. \(\square\)

---

## 3. Äquivalente inversefreie Range-Transversalität

Setze den inneren Unsichtbarkeitsraum
\[
\boxed{
\mathcal K_R:=\ker(E_I^*H|_{\mathscr H^+}).
}
\tag{SE.7}
\]
Für \(w\in\mathscr H_{\mathcal A}^-\) schreibe
\[
z:=HE_{\mathcal A}w.
\]
Die Schur-Kernbedingung ist wegen \(H^*=-H\) äquivalent zu
\[
E_I^*HBz=0,
\]
also
\[
Bz\in\mathcal K_R.
\]
Da \(B^{-1}=I+A\), gilt exakt
\[
\boxed{
 z\in (I+A)\mathcal K_R.
}
\tag{SE.8}
\]
Daraus folgt die zweite exakte Form:
\[
\boxed{
\ker\mathcal S_{I,A}=\{0\}
\iff
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+A)\mathcal K_R
=\{0\},
}
\tag{SE.9}
\]
**sofern** auf dem betrachteten Stratum
\[
\ker(HE_{\mathcal A}|_-)=\{0\}
\]
gilt. Diese letzte Injektivität ist genau die P11↔P12-Rückbindung auf den global bewiesenen P12-Strata.

Ohne P12-Injektivität bleibt die sichere Aussage: nichttriviale Schur-Kerne entsprechen über (SE.5) exakt nichttrivialen Blockkernpaaren. Für die reine Range-Schnitt-Formulierung muss zwischen \(w\ne0\) und \(z=HE_Aw\ne0\) unterschieden werden.

---

## 4. Warum dies R32 strukturell verändert

P11/R32 hatte die konkrete Schwierigkeit, dass
\[
B=(I+R^*R)^{-1}
\]
als nichtlokaler inverser Operator keine endliche Propagations- oder Supportregel besitzt. SE-1 benötigt **keinerlei** Propagationsaussage über \(B\): die Inverse verschwindet vollständig aus dem zu prüfenden Blocksystem.

Übrig bleiben nur
\[
H,
\qquad
A=R^*R,
\qquad
E_I,
\qquad
E_{\mathcal A},
\qquad
I.
\]
Bei festem Horizont sind \(H\) und \(R\) endliche translations-/cutoff-basierte Operatoren. Daher ist auch \(A=R^*R\) ein endliches Operatorwort aus Translationen und Intervallmultiplikatoren.

Dies beweist **noch nicht** die Injektivität von \(\mathcal K_{I,A}\). Es beseitigt aber genau die nichtlokale Inverse als Hindernis für eine P12-artige Rohoperatoranalyse.

---

## 5. Exakte Rest-Kanäle im Drei-Shift-Fenster

P11s Full-Rest-Martingalefaktorisierung gibt
\[
\widetilde R^*\widetilde R=R^*R=A
\]
mit
\[
(\widetilde Rf)_{p,j}
=\sqrt{(\log p)(p-1)p^j}\,
1_{\Omega_{p,j}}\Phi_{p,j}[f],
\]
\[
\Phi_{p,j}
=\sum_{k\ge j+1}p^{-3k/4}K_{k\log p}^{\rm tr},
\qquad
K_s^{\rm tr}:=P_{T_0}D_sE_{T_0}.
\]

Im gesamten Fenster
\[
2a<T_0<c=\frac12\log5
\]
sind nur die Primsektoren \(p=2,3\) möglich. Die nichtleeren Martingaletiefen sind exakt
\[
\boxed{(p,j)=(2,0),(2,1),(3,0).}
\tag{SE.10}
\]
Die Radien lauten
\[
\Omega_{2,0}=\{|u|\le T_0-a\},
\]
\[
\Omega_{2,1}=\{|u|\le T_0-2a\},
\]
\[
\Omega_{3,0}=\{|u|\le T_0-b\}.
\tag{SE.11}
\]

Auf diesen jeweiligen Outputfenstern verschwinden alle hinreichend tiefen \(k\)-Terme identisch. Exakt aktiv bleiben:

### (2,0)-Block
\[
\boxed{
\Phi_{2,0}
=2^{-3/4}K_{\log2}^{\rm tr}
+2^{-3/2}K_{2\log2}^{\rm tr}
+2^{-9/4}K_{3\log2}^{\rm tr}.
}
\tag{SE.12}
\]
Der \(k=3\)-Term ist möglich, weil \(T_0>2a\). Der \(k=4\)-Term ist auf \(\Omega_{2,0}\) unmöglich, denn dafür wäre
\[
5a<2T_0<\log5,
\]
aber \(5a=\frac52\log2>\log5\).

### (2,1)-Block
\[
\boxed{
\Phi_{2,1}
=2^{-3/2}K_{2\log2}^{\rm tr}.
}
\tag{SE.13}
\]
Der \(k=2\)-Term ist möglich wegen \(T_0>2a\); \(k=3\) würde wieder \(5a<2T_0\) verlangen und ist daher unmöglich.

### (3,0)-Block
\[
\boxed{
\Phi_{3,0}
=3^{-3/4}K_{\log3}^{\rm tr}.
}
\tag{SE.14}
\]
Der \(k=2\)-Term würde
\[
3b<2T_0<\log5
\]
verlangen; aber
\[
3b=\frac32\log3>\log5.
\]

Damit besitzt \(A=R^*R\) im gesamten Drei-Shift-Fenster die exakte Darstellung
\[
\boxed{
\begin{aligned}
A={}&(\log2)\,\Phi_{2,0}^*M_{\Omega_{2,0}}\Phi_{2,0}\\
&+2(\log2)\,\Phi_{2,1}^*M_{\Omega_{2,1}}\Phi_{2,1}\\
&+2(\log3)\,\Phi_{3,0}^*M_{\Omega_{3,0}}\Phi_{3,0}.
\end{aligned}
}
\tag{SE.15}
\]
Nach Expansion von (SE.12)--(SE.14) sind dies
\[
\boxed{9+1+1=11}
\tag{SE.16}
\]
endliche \(K^*M_\Omega K\)-Wortterme.

Somit besteht die erste Zeile von \(\mathcal K_{I,A}\) aus dem Identitätsterm, 11 Rest-Gram-Wörtern und dem drei-shiftigen Hubterm. Es gibt **keine** Operatorinverse mehr.

---

## 6. Bezug zu DN-1

DN-1 zeigt für \(0<R<a\), dass
\[
\mathcal K_R=\ker(E_I^*H|_+)\ne\{0\}.
\]
SE.9 präzisiert deshalb die echte verbleibende Frage:

Nicht
\[
\mathcal K_R=\{0\},
\]
sondern
\[
\boxed{
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+R^*R)\mathcal K_R
\stackrel?=\{0\}.
}
\tag{SE.17}
\]

Dies ist eine inversefreie relative Lagefrage zweier explizit endlich erzeugter Shift-/Cutoff-Strukturen.

---

## 7. Neue konkrete Forschungsfront

Der nächste sinnvolle mathematische Angriff ist daher nicht ein weiterer abstrakter Satz über \(B\), sondern:

1. Odd/even falten;
2. die drei Hub-Shifts \(a,b,T\) einsetzen;
3. die drei Rest-Martingaleblöcke (SE.12)--(SE.14) einsetzen;
4. die 11 \(K^*M_\Omega K\)-Wörter nach ihren Cutoff-Wänden zerlegen;
5. auf einem ersten P12-globalen Parameterstratum das gekoppelte Rohsystem \(\mathcal K_{I,A}(y,w)=0\) aufbauen;
6. nach einer endlichen invertierbaren Rohmatrix bzw. nach einem exakten Gegenvektor suchen.

Die natürliche erste Testregion ist der all-radius restricted-tail sector
\[
T<S<T_0,
\qquad
\sigma=S-T\le R,
\]
weil dort die äußere Hub-Injektivität bereits global \(\checkmark[M]\) ist und keine Low-radius-Faser-Firewall stört.

---

## 8. Firewall / Status

Bis zu unabhängigem Review:

- **SE-1 Schur-Inversenelimination:** `?[O]` als Auditkandidat;
- **SE-2 Drei-Rest-Block-/11-Wort-Reduktion:** `?[O]` als Auditkandidat;
- **Schur-Crossblock-Injektivität:** weiterhin `?[O]`;
- **Strong Terminal Transport:** weiterhin `?[O]`;
- **P11-wide global Gram/mediator closure:** weiterhin `?[O]`.

Nicht behauptet werden:

- dass \(\mathcal K_{I,A}\) bereits injektiv ist;
- dass die 11 Wortterme eine kleine oder numerisch gut konditionierte Matrix ergeben;
- dass P12-Injektivität quantitative Coercivity liefert;
- dass DN-1 einen Schur-Annihilator erzeugt;
- irgendeine Polar-Gauge-, Strong-Terminal-, Objekt-X- oder RH-Konsequenz.

**Architektonischer Kandidatenbefund:** Der bisherige R32-Blocker „nichtlokale Inverse \(B\)“ ist für die reine Schur-Kernfrage durch ein exakt äquivalentes augmentiertes System eliminierbar. Der verbleibende Operator ist bei festem Horizont endlich translations-/cutoff-generiert und damit prinzipiell der P12-Rohoperator-Technik zugänglich.