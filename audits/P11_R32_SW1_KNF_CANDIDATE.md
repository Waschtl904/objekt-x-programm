# Audit-Kandidat: SW1-KNF — Disjoint-Window Kernel Normal Form

> **Stand:** 28. August 2026  
> **Repo-Basis dieses Audits:** \`main@f2a5afcf98cef2ff2b73b2cf62cca329cc98ef33\`  
> **Status:** \`?[O]\` — vollständiger Beweiskandidat, noch kein adversariales GREEN, keine Promotion.  
> **Scope:** ausschließlich SW1,
> \[
> 0<\sigma\le R<\varepsilon,\qquad R+\varepsilon<\Delta.
> \]

---

## 0. Firewall

Dieses Audit beansprucht — falls es nach unabhängigem Review GREEN wird — ausschließlich eine sektorale Koordinaten-Normalform des inneren Kernels auf SW1.

Es behauptet insbesondere **nicht**:

- globales FG-1;
- globales FG-TR1;
- A0 (volle freie-Koordinaten-Abdeckung);
- Trivialität von \(\mathcal K_R\);
- HT-RED (Full-Rest-/Schur-Elimination);
- \(\ker\Gamma_I=\{0\}\);
- Closed Range / bounded below;
- SW1-BL7;
- SW1-2TP;
- SW1-AWI;
- \(\Delta\)-Descent;
- Strong Terminal Transport, Objekt X oder RH.

\[
\boxed{\text{SW1-KNF ist eine sektorale Koordinaten-Normalform, kein Injektivitätssatz.}}
\]

Keine Aussage in diesem Audit erzeugt ohne separaten Promotionsvorgang ein \(\checkmark[M]\).

---

## 1. Setup und kanonische Konstanten

Wir arbeiten im Drei-Shift-Fenster mit
\[
a=\frac12\log2,\qquad
b=\frac12\log3,\qquad
T=2a=\log2,
\]
und setzen
\[
d:=b-a=\frac12\log\frac32,
\qquad
e:=T-b=\frac12\log\frac43,
\qquad
\Delta:=d-e=\frac12\log\frac98.
\]

Ferner
\[
T_0=T+\varepsilon.
\]

Auf SW1 gilt
\[
\boxed{
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta.
}
\tag{KNF.1}
\]

Für die inneren Hubgewichte verwenden wir die kanonischen drei aktiven Prime-Power-Koeffizienten
\[
p=\sqrt{\log2}\,2^{-3/4},
\qquad
r=\sqrt{\log3}\,3^{-3/4},
\qquad
q=\sqrt{\log2}\,2^{-3/2}.
\tag{KNF.2}
\]
Insbesondere
\[
\boxed{p>0.}
\tag{KNF.3}
\]

Die Formel (KNF.2) ist dieselbe Drei-Shift-Normalisierung wie in
\`audits/P11_P12_R32_RUECKBINDUNG_AUDIT.md\`, Gleichung (RB.4).

Sei
\[
\mathscr H_{T_0}^{+}
:=
L^2(-T_0,T_0)^{+}
\]
der gerade Sektor und
\[
I=(-R,R).
\]
Wir schreiben
\[
\boxed{
\mathcal K_R
:=
\ker\!\left(E_I^*H_{T_0}\big|_{\mathscr H_{T_0}^{+}}\right).
}
\tag{KNF.4}
\]
Die Abhängigkeit von \(T_0\) wird in der Notation unterdrückt, wie in der bestehenden P11/R32-Front.

Alle Aussagen über Intervalle und Zerlegungen unten sind als \(L^2\)-Aussagen **modulo Nullmengen** zu verstehen. Endpunkte und einzelne Zentren spielen daher keine Rolle.

---

## 2. Lemma SW1-KNF-1 — strikte Skalenordnung

Auf SW1 gilt
\[
\boxed{
2R<R+\varepsilon<\Delta<e<d<a<T.
}
\tag{KNF.5}
\]

### Beweis

Aus \(R<\varepsilon\) folgt
\[
2R<R+\varepsilon.
\]
Die zweite strikte Ungleichung ist genau (KNF.1):
\[
R+\varepsilon<\Delta.
\]

Für die festen Konstanten gilt
\[
\Delta<e
\iff
\frac98<\frac43
\iff
27<32,
\]
also
\[
\Delta<e.
\]

Ferner
\[
e<d
\iff
\frac43<\frac32
\iff
8<9.
\]
Damit
\[
e<d.
\]

Schließlich ist
\[
a=d+e>d
\]
und
\[
T=2a>a.
\]
Damit ist (KNF.5) vollständig bewiesen. \(\square\)

Eine unmittelbare Konsequenz ist
\[
\boxed{2R<d,\qquad 2R<e.}
\tag{KNF.6}
\]

---

## 3. Lemma SW1-KNF-2 — drei disjunkte Samplingfenster

Definiere
\[
I_a=(a-R,a+R),
\qquad
I_b=(b-R,b+R),
\qquad
I_T=(T-R,T+R).
\tag{KNF.7}
\]

Dann gilt auf SW1:

1. \(I_a,I_b,I_T\subset(0,T_0)\);
2. die drei Intervalle sind paarweise disjunkt;
3. ihre Reihenfolge ist
   \[
   a-R<a+R<b-R<b+R<T-R<T+R.
   \tag{KNF.8}
   \]

### Beweis

Zunächst ist wegen \(R<a\)
\[
a-R>0.
\]
Da \(a<b<T\), liegen auch die linken Endpunkte der beiden anderen Fenster positiv.

Am oberen Horizont gilt
\[
T+R<T+\varepsilon=T_0
\]
wegen \(R<\varepsilon\). Damit liegen auch \(I_a\) und \(I_b\), deren Zentren links von \(T\) liegen, vollständig unter \(T_0\).

Für die erste Lücke:
\[
(b-R)-(a+R)
=
(b-a)-2R
=
d-2R>0
\]
nach (KNF.6). Also
\[
a+R<b-R.
\]

Für die zweite Lücke:
\[
(T-R)-(b+R)
=
(T-b)-2R
=
e-2R>0.
\]
Also
\[
b+R<T-R.
\]

Damit folgt (KNF.8) und insbesondere die paarweise Disjunktheit. \(\square\)

### Branch-Identifikations-Firewall

Für \(0<u,v<R\) können physische Branchwerte aus verschiedenen Zentren nicht zusammenfallen, weil ihre Bilder in den drei disjunkten Intervallen \(I_a,I_b,I_T\) liegen.

Innerhalb desselben Fensters kann
\[
a-u=a+v
\]
mit \(u,v>0\) nicht auftreten; analog für \(b\) und \(T\). Die einzige formale Berührung der beiden Halbbranches wäre am Zentrum selbst, also \(u=v=0\), einer Nullmenge außerhalb des offenen Parameterintervalls.

Eine mögliche Gleichheit eines Branchwerts mit einer sonst ausgezeichneten Zahl des Programms, etwa \(2d\), erzeugt **keine** zusätzliche Branch-Identifikation: Für \(E_I^*H\) relevant sind ausschließlich Gleichheiten zwischen den tatsächlich auftretenden sechs Branchabbildungen
\[
a\pm u,\qquad b\pm u,\qquad T\pm u.
\]

---

## 4. Lemma SW1-KNF-3 — vollständige Horizon-Legalität

Für jedes
\[
0<u<R
\]
liegen alle sechs Branchwerte
\[
a-u,\ a+u,\ b-u,\ b+u,\ T-u,\ T+u
\]
in \((0,T_0)\).

Insbesondere
\[
\boxed{T+u<T_0.}
\tag{KNF.9}
\]

### Beweis

Die fünf Werte außer \(T+u\) liegen bereits wegen Lemma SW1-KNF-2 im Inneren der drei Samplingfenster.

Für den rechten Horizon-Branch:
\[
u<R<\varepsilon
\]
liefert
\[
T+u<T+\varepsilon=T_0.
\]
Weitere Horizon-Bedingungen treten in der Definition der inneren Row nicht auf. \(\square\)

---

## 5. Lemma SW1-KNF-4 — exakte innere Row

Für \(y\in\mathscr H_{T_0}^{+}\) gilt auf SW1 für fast jedes \(u\in(0,R)\)
\[
\boxed{
(E_I^*H_{T_0}y)(u)
=
p\,[y(a-u)-y(a+u)]
+
r\,[y(b-u)-y(b+u)]
+
q\,[y(T-u)-y(T+u)].
}
\tag{KNF.10}
\]

Daher
\[
y\in\mathcal K_R
\]
genau dann, wenn die rechte Seite von (KNF.10) für fast jedes \(u\in(0,R)\) verschwindet.

### Beweis

Im Drei-Shift-Fenster sind exakt die Prime-Powers \(2,3,4\) aktiv; ihre Halbverschiebungen sind \(a,b,T\) und ihre Koeffizienten sind \(p,r,q\). Die kanonische positive-Halbachsenform der inneren Row ist genau die in (KNF.10) geschriebene Differenzsumme; vgl. die identische physische Row in
\`audits/P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md\`, Gleichung (TR.4).

Lemma SW1-KNF-3 stellt sicher, dass auf SW1 keiner der sechs Werte durch den Horizon-Cut verschwindet.

Die zweite augmentierte Gleichung \(E_I^*H_{T_0}y=0\) enthält nur \(y\); Annulus- bzw. \(w\)-Terme gehören ausschließlich zur ersten augmentierten Gleichung
\[
(I+A)y+HE_{\mathcal A}w=0
\]
und treten in (KNF.10) nicht auf. \(\square\)

---

## 6. Lemma SW1-KNF-5 — explizite Rekonstruktion des linken \(a\)-Branches

Für \(y\in\mathcal K_R\) ist für fast jedes \(u\in(0,R)\)
\[
\boxed{
y(a-u)
=
y(a+u)
-\frac rp\,[y(b-u)-y(b+u)]
-\frac qp\,[y(T-u)-y(T+u)].
}
\tag{KNF.11}
\]

Umgekehrt erfüllt jede gerade \(L^2\)-Funktion, deren sechs Branchwerte (KNF.11) a.e. erfüllen, die innere Kernelgleichung.

### Beweis

Wegen \(p>0\) kann (KNF.10) eindeutig nach \(y(a-u)\) aufgelöst werden. Dies ergibt (KNF.11).

Umgekehrt liefert direktes Einsetzen von (KNF.11) in (KNF.10) identisch Null. \(\square\)

---

## 7. Exakter direkter Blindbereich auf SW1

Setze
\[
\mathcal U_R^{\rm SW1}
:=
I_a\cup I_b\cup I_T.
\tag{KNF.12}
\]

Der positive direkte Blindbereich ist, modulo Nullmengen,
\[
\boxed{
\mathcal Z_{R,\rm SW1}^{\rm phys}
=
(0,a-R)
\cup
(a+R,b-R)
\cup
(b+R,T-R)
\cup
(T+R,T+\varepsilon).
}
\tag{KNF.13}
\]

Definiere den geraden blinden Raum
\[
\boxed{
\mathcal Z_R^{+}
:=
\left\{
z\in\mathscr H_{T_0}^{+}:
\operatorname{ess\,supp}(z|_{(0,T_0)})
\subset
\mathcal Z_{R,\rm SW1}^{\rm phys}
\right\}.
}
\tag{KNF.14}
\]

Dann
\[
\boxed{\mathcal Z_R^{+}\subset\mathcal K_R.}
\tag{KNF.15}
\]

### Beweis der Exaktheit

Nach Lemma SW1-KNF-2 ist
\[
(0,T_0)
\setminus
(I_a\cup I_b\cup I_T)
\]
genau die Vereinigung in (KNF.13), bis auf Endpunkte.

Jeder Punkt dieses Komplements ist für kein \(u\in(0,R)\) einer der sechs Werte
\[
a\pm u,\qquad b\pm u,\qquad T\pm u.
\]
Er ist daher direkt unsichtbar für \(E_I^*H_{T_0}\).

Umgekehrt wird jeder Punkt im Inneren von \(I_a\cup I_b\cup I_T\), mit Ausnahme der drei Zentren \(a,b,T\), von genau einem der sechs Branches erreicht:

- \(t\in(a-R,a)\): \(t=a-u\);
- \(t\in(a,a+R)\): \(t=a+u\);
- analog für \(b\) und \(T\).

Die drei Zentren selbst sowie die Fensterendpunkte sind Nullmengen. Damit ist (KNF.13) als \(L^2\)-Blindbereich exakt, nicht nur eine Teilmenge. \(\square\)

---

## 8. Freie physische Koordinaten

Definiere
\[
\boxed{
\mathcal V_R^{\rm SW1}
=
(a,a+R)
\cup
(b-R,b+R)
\cup
(T-R,T+R).
}
\tag{KNF.16}
\]

Wegen Lemma SW1-KNF-2 ist dies a.e. die disjunkte Vereinigung der fünf freien Halbbranches
\[
(a,a+R),\quad
(b-R,b),\quad
(b,b+R),\quad
(T-R,T),\quad
(T,T+R).
\tag{KNF.17}
\]

Der einzige gesampelte positive Teil, der nicht in \(\mathcal V_R^{\rm SW1}\) liegt, ist
\[
(a-R,a),
\]
und genau dieser wird durch (KNF.11) rekonstruiert.

---

## 9. Theorem SW1-KNF — beschränkte Kernel-Normalform

Unter den SW1-Annahmen (KNF.1) ist die Abbildung
\[
\boxed{
\Psi_R:
\mathcal K_R
\longrightarrow
\mathcal Z_R^{+}\oplus L^2(\mathcal V_R^{\rm SW1}),
\qquad
\Psi_R(y)
=
\bigl(P_{\mathcal Z}y,\ y|_{\mathcal V_R^{\rm SW1}}\bigr)
}
\tag{KNF.18}
\]
ein beschränkter linearer Isomorphismus.

Hier ist \(P_{\mathcal Z}y\) die gerade Restriktion/Nullfortsetzung von \(y\) auf den in (KNF.13) definierten blinden Bereich.

Insbesondere
\[
\boxed{
\mathcal K_R
\cong
\mathcal Z_R^{+}
\oplus
L^2(\mathcal V_R^{\rm SW1})
\qquad\text{auf SW1}.
}
\tag{KNF.19}
\]

### Beweis — Schritt 1: Konstruktion der inversen Abbildung

Seien beliebig
\[
z\in\mathcal Z_R^{+},
\qquad
h\in L^2(\mathcal V_R^{\rm SW1}).
\]

Definiere auf \(0<u<R\) die fünf Pullbacks
\[
h_A(u):=h(a+u),
\]
\[
h_{B,-}(u):=h(b-u),
\qquad
h_{B,+}(u):=h(b+u),
\]
\[
h_{T,-}(u):=h(T-u),
\qquad
h_{T,+}(u):=h(T+u).
\tag{KNF.20}
\]

Setze
\[
\boxed{
x(u)
:=
h_A(u)
-\frac rp\,[h_{B,-}(u)-h_{B,+}(u)]
-\frac qp\,[h_{T,-}(u)-h_{T,+}(u)].
}
\tag{KNF.21}
\]

Definiere nun die positive Halbachse von \(y\) durch

- \(y=z\) auf \(\mathcal Z_{R,\rm SW1}^{\rm phys}\);
- \(y=h\) auf \(\mathcal V_R^{\rm SW1}\);
- \(y(a-u)=x(u)\) für \(0<u<R\);
- auf den endlich vielen verbleibenden End-/Zentrumspunkten beliebig, etwa \(0\).

Anschließend wird \(y\) gerade nach \((-T_0,0)\) fortgesetzt.

Die Bereiche sind a.e. disjunkt und überdecken \((0,T_0)\), also ist \(y\) wohldefiniert.

### Schritt 2: \(L^2\)-Beschränktheit der Rekonstruktion

Die fünf Pullbacks in (KNF.20) sind Translationen bzw. Reflexionen mit Jacobi-Betrag \(1\). Wegen der disjunkten Zerlegung (KNF.17) gilt
\[
\|h_A\|_2^2
+
\|h_{B,-}\|_2^2
+
\|h_{B,+}\|_2^2
+
\|h_{T,-}\|_2^2
+
\|h_{T,+}\|_2^2
=
\|h\|_{L^2(\mathcal V_R^{\rm SW1})}^2.
\tag{KNF.22}
\]

Für den Koeffizientenvektor in (KNF.21) liefert Cauchy-Schwarz punktweise
\[
|x(u)|^2
\le
C_{\rm KNF}
\left(
|h_A(u)|^2
+|h_{B,-}(u)|^2
+|h_{B,+}(u)|^2
+|h_{T,-}(u)|^2
+|h_{T,+}(u)|^2
\right),
\]
mit
\[
\boxed{
C_{\rm KNF}
=
1
+
2\left(\frac rp\right)^2
+
2\left(\frac qp\right)^2
<\infty.
}
\tag{KNF.23}
\]

Integration und (KNF.22) geben
\[
\boxed{
\|x\|_{L^2(0,R)}^2
\le
C_{\rm KNF}
\|h\|_{L^2(\mathcal V_R^{\rm SW1})}^2.
}
\tag{KNF.24}
\]

Da die gerade Fortsetzung die positive \(L^2\)-Masse lediglich verdoppelt, folgt für die rekonstruierte Funktion
\[
\boxed{
\|y\|_{\mathscr H_{T_0}^{+}}^2
\le
\|z\|_{\mathscr H_{T_0}^{+}}^2
+
2(1+C_{\rm KNF})
\|h\|_{L^2(\mathcal V_R^{\rm SW1})}^2.
}
\tag{KNF.25}
\]
Somit ist die inverse Rekonstruktionsabbildung beschränkt.

### Schritt 3: Die Rekonstruktion liegt im Kernel

Auf dem blinden Bereich trägt \(z\) zu keiner inneren Row bei.

Auf den drei Samplingfenstern besitzt die rekonstruierte Funktion genau die fünf vorgegebenen Branchwerte (KNF.20) und den linken \(a\)-Branch (KNF.21). Nach Lemma SW1-KNF-5 erfüllt sie damit für fast jedes \(u\in(0,R)\) die Gleichung (KNF.10).

Also
\[
E_I^*H_{T_0}y=0
\]
und damit
\[
y\in\mathcal K_R.
\]

### Schritt 4: Surjektivität

Die Konstruktion aus Schritten 1–3 zeigt für jedes
\[
(z,h)\in
\mathcal Z_R^{+}\oplus L^2(\mathcal V_R^{\rm SW1})
\]
ein \(y\in\mathcal K_R\) mit
\[
\Psi_R(y)=(z,h).
\]
Also ist \(\Psi_R\) surjektiv.

### Schritt 5: Injektivität / Eindeutigkeit

Sei
\[
\Psi_R(y)=(0,0).
\]
Dann verschwindet \(y\) auf dem gesamten blinden Bereich und auf allen fünf freien Branches.

Formel (KNF.11) erzwingt anschließend
\[
y(a-u)=0
\qquad\text{für fast jedes }u\in(0,R).
\]
Damit verschwindet \(y\) auf der ganzen positiven Halbachse bis auf Nullmengen und wegen Geradheit auch auf \((-T_0,0)\). Also
\[
y=0.
\]
Somit ist \(\Psi_R\) injektiv.

### Schritt 6: Beschränktheit von \(\Psi_R\)

\(P_{\mathcal Z}\) und die Restriktion auf \(\mathcal V_R^{\rm SW1}\) sind orthogonale Restriktionsoperatoren. Daher
\[
\|P_{\mathcal Z}y\|_{\mathscr H_{T_0}^{+}}
\le
\|y\|_{\mathscr H_{T_0}^{+}},
\]
und wegen Geradheit
\[
\|y|_{\mathcal V_R^{\rm SW1}}\|_2^2
\le
\frac12\|y\|_{\mathscr H_{T_0}^{+}}^2.
\]
Damit ist \(\Psi_R\) beschränkt.

Die Schritte 1–6 beweisen den beschränkten linearen Isomorphismus (KNF.18)–(KNF.19). \(\square\)

---

## 10. Adversarialer Review-Status der zehn Pflichtpunkte

Vor einem unabhängigen Review bleibt der formale Kandidatenstatus
\[
\boxed{\mathrm{SW1\!-\!KNF}:?[O].}
\]

Der vorliegende Beweis adressiert die zehn Pflichtpunkte wie folgt:

1. **\(2R<\Delta\):** explizit in Lemma SW1-KNF-1.
2. **Fenster in \((0,T_0)\):** explizit in Lemma SW1-KNF-2.
3. **Paarweise Disjunktheit:** explizit über \(d-2R>0\) und \(e-2R>0\).
4. **Keine versteckte Branchidentifikation:** eigener Firewall-Abschnitt nach Lemma SW1-KNF-2.
5. **\(T+u<T_0\):** Lemma SW1-KNF-3.
6. **Row/Rekonstruktion exakt:** Lemmas SW1-KNF-4 und SW1-KNF-5.
7. **Surjektivität:** Theorem SW1-KNF, Schritt 4.
8. **Beidseitige Beschränktheit:** Theorem SW1-KNF, Schritte 2 und 6.
9. **Blindbereich exakt:** Abschnitt 7, modulo \(L^2\)-Nullmengen.
10. **Scope-Firewall:** Abschnitt 0.

Kein GREEN und keine Promotion werden durch diese interne Beweisvervollständigung selbst erzeugt. Dafür ist der exakte neue PR-Head erneut adversarial zu prüfen.

---

## 11. Bedeutung bei späterem GREEN

Falls dieser exakte Satz adversarial GREEN bestätigt wird, steht auf SW1 eine vollständig sektorale Beschreibung des inneren Kernes zur Verfügung:
\[
\boxed{
\mathcal K_R
\cong
\mathcal Z_R^{+}
\oplus
L^2(\mathcal V_R^{\rm SW1}).
}
\]

Damit wäre für die **innere Kernelparametrisierung auf SW1** keine globale Fiber-Graph-/FG-TR1-Blackbox mehr nötig.

Dies ist nur eine Koordinatenreduktion. Insbesondere bleiben weiterhin offen:
\[
\mathrm{HT\!-\!RED},\qquad
\mathrm{A0},\qquad
\ker\Gamma_I=\{0\}.
\]

Die nächsten getrennten Kandidaten bleiben:
\[
\mathrm{SW1\!-\!BL7}
\to
\mathrm{SW1\!-\!2TP}
\to
\mathrm{SW1\!-\!AWI}
\to
\Delta\text{-Descent}.
\]
