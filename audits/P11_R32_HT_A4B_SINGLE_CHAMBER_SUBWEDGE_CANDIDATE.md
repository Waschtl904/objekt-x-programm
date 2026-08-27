# P11/R32 — HT-A4b-SW1: Single-FG-Chamber-Subwedge unter \(R+\varepsilon<\Delta\)

**Status:** Rechenkandidat; keine Promotion.  
**Arbeitsname:** HT-A4b-SW1.  
**Repo-Basis:** main@9d85df51f926d976d7d685dc0000fd7ff41609fb.  
**Scope:** ausschließlich die restricted-tail-Klasse
\[
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta,
\]
mit
\[
T<S=T+\sigma<T_0=T+\varepsilon<c.
\]
**Abhängigkeit:** HT-A4a FG CLASSIFICATION OF SIX ARGUMENTS: independently GREEN candidate.  
**Firewall:** keine globale Promotion von HT-A4b, HT-RED, A0 oder Schur-Cross-Gram-Injektivität.

---

## 0. Ziel

Das vollständige HT-A4b-Problem auf dem offenen Dreieck
\[
0<R<\varepsilon<c-T
\]
enthält im aktuellen Tail-FG-Audit zehn Parameterflächen und 15 offene Tail-FG-Chambers.

Dieses Audit prüft bewusst nur den kleineren offenen Subwedge
\[
\boxed{
\mathfrak W_{\rm SW1}
=
\{(R,\varepsilon):
0<R<\varepsilon,\ R+\varepsilon<\Delta\}.
}
\tag{SW1.1}
\]

Hier bezeichnet „Inneres von \(\mathfrak W_{\rm SW1}\)“ ausschließlich das offene \((R,\varepsilon)\)-Parametergebiet (SW1.1). Der restricted-tail-Parameter \(\sigma\) wird zusätzlich durch
\[
0<\sigma\le R
\]
zugelassen. Insbesondere ist die Randfläche \(\sigma=R\) **mit enthalten**; sie ist keine weitere HT.31-FG-Wand, da die Tail-FG-Membership in HT.24–HT.27 und die zehn HT.31-Flächen nur von \((R,\varepsilon)\) abhängen.

Zu zeigen ist:

1. Alle fünf inneren Tail-FG-\(s\)-Wände liegen auf \(\mathfrak W_{\rm SW1}\) strikt rechts des Integrationsintervalls \((R,\varepsilon)\).
2. Damit ist die Fiber-Graph-Klassifikation der sechs Tail-Argumente auf dem gesamten \(s\)-Intervall konstant.
3. Keine der zehn HT.31-Parameterflächen schneidet das Innere von \(\mathfrak W_{\rm SW1}\).
4. \(\mathfrak W_{\rm SW1}\) ist nichtleer und mit einem \(R\to0\)-Descent vereinbar.
5. Die separat bekannte A-Wall-/HT-A3-Kollision bei \(\varepsilon=\Delta/2\) bleibt sichtbar und darf nicht mit der FG-Chamber-Struktur verwechselt werden.

---

## 1. Konstanten und Ordnung

Es gelten
\[
d=b-a=\frac12\log\frac32,
\qquad
e=T-b=\frac12\log\frac43,
\]
\[
\Delta=d-e=\frac12\log\frac98,
\qquad
\varepsilon_{\max}=c-T=\frac12\log\frac54.
\]

Numerisch:
\[
\Delta\approx0.05889151783,
\qquad
\varepsilon_{\max}\approx0.11157177566,
\]
\[
e\approx0.14384103623,
\qquad
d\approx0.20273255405.
\]

Insbesondere
\[
\boxed{
0<\Delta<\varepsilon_{\max}<e<d.
}
\tag{SW1.2}
\]

Außerdem
\[
e>2\Delta,
\]
denn
\[
e-2\Delta
=
\frac12\log\frac{256}{243}>0.
\tag{SW1.3}
\]

Damit
\[
C:=\frac{e-\Delta}{2}>\frac{\Delta}{2}.
\tag{SW1.4}
\]

---

## 2. Sofortige Folgen der Standing-Hypothese

Aus
\[
0<R<\varepsilon,
\qquad
R+\varepsilon<\Delta
\]
folgt
\[
2R<R+\varepsilon<\Delta,
\]
also
\[
\boxed{
R<\frac{\Delta}{2}.
}
\tag{SW1.5}
\]

Ferner
\[
\boxed{
\varepsilon<\Delta-R<\Delta.
}
\tag{SW1.6}
\]

Damit liegt \(\mathfrak W_{\rm SW1}\) vollständig in Zone I des Tail-FG-Audits.

---

## 3. Alle fünf Tail-FG-\(s\)-Wände sind inaktiv

Nach HT.28 sind die fünf inneren Wände
\[
D_-=\Delta-R,
\qquad
D_0=\Delta,
\qquad
D_+=\Delta+R,
\]
\[
E=e-R,
\qquad
A_*=d-R.
\]

Für \((R,\varepsilon)\in\mathfrak W_{\rm SW1}\) gilt wegen (SW1.6)
\[
D_-=\Delta-R>\varepsilon.
\tag{SW1.7}
\]

Dann
\[
D_0=\Delta>D_->\varepsilon,
\tag{SW1.8}
\]
und
\[
D_+=\Delta+R>\Delta>\varepsilon.
\tag{SW1.9}
\]

Wegen \(e>\Delta\)
\[
E=e-R>\Delta-R=D_->\varepsilon.
\tag{SW1.10}
\]

Wegen \(d>e\)
\[
A_*=d-R>e-R=E>\varepsilon.
\tag{SW1.11}
\]

Somit
\[
\boxed{
D_-,D_0,D_+,E,A_*\notin(R,\varepsilon),
}
\tag{SW1.12}
\]
und sogar alle fünf liegen strikt rechts von \(\varepsilon\).

Es gibt daher auf dem gesamten offenen \(s\)-Intervall keinen Tail-FG-Umschaltpunkt.

---

## 4. Vollständige Membership-Tabelle der sechs Tail-Argumente

Sei
\[
R<s<\varepsilon
\]
und
\[
y=\widehat\Phi_R(z,0,h)\in\mathcal K_R.
\]

Die drei nach HT.23 permanent blinden Werte sind
\[
y(s)=z(s),
\qquad
y(a-s)=z(a-s),
\qquad
y(T+s)=z(T+s).
\tag{SW1.13}
\]

Für \(a+s\) liegt der HT.24-Wechsel bei
\[
s=d-R=A_*.
\]
Nach (SW1.11) ist \(A_*>\varepsilon\), also
\[
\boxed{
y(a+s)=z(a+s).
}
\tag{SW1.14}
\]

Für \(T-s\) liegt der HT.25-Wechsel bei
\[
s=e-R=E.
\]
Nach (SW1.10) ist \(E>\varepsilon\), also
\[
\boxed{
y(T-s)=z(T-s).
}
\tag{SW1.15}
\]

Für \(2d-s\) gilt wegen
\[
s<\varepsilon<\Delta-R
\]
die strikte Ungleichung
\[
\Delta-s>R.
\]
Daher
\[
|s-\Delta|>R
\]
und nach HT.26
\[
\boxed{
y(2d-s)=z(2d-s).
}
\tag{SW1.16}
\]

Damit lautet die vollständige Membership-Tabelle:

| Argument | Typ auf ganz \((R,\varepsilon)\) |
|---|---|
| \(s\) | \(Z\) |
| \(a-s\) | \(Z\) |
| \(a+s\) | \(Z\) |
| \(T-s\) | \(Z\) |
| \(2d-s\) | \(Z\) |
| \(T+s\) | \(Z\) |

Insbesondere ist das HT-A4a-Tripel
\[
\boxed{ZZZ}
\tag{SW1.17}
\]
auf dem gesamten Tail-Intervall konstant.

Der private \(x_0\)-Ast ist hier vakuum:
\[
s<\varepsilon<\Delta,
\]
also kann der Bereich
\[
\Delta<s<\Delta+R
\]
nicht erreicht werden.

Damit tritt der \(X\)-Ast auf \(\mathfrak W_{\rm SW1}\) überhaupt nicht auf. HT.27 ist in diesem Subwedge daher **vakuum erfüllt**; die in PR #8 ausdrücklich dokumentierte TR.13-Provenienzabhängigkeit wird für diese Parameterklasse nicht benötigt.

---

## 5. Herkunft und Ausschluss aller zehn HT.31-Flächen

Die zehn Flächen aus HT.31 entstehen vollständig aus Randtreffern der fünf \(s\)-Wände sowie der einzigen aktiven Wall-Wall-Kollision.

### 5.1 \(D_-\)-Randtreffer

\[
D_-=\varepsilon
\iff
\varepsilon=\Delta-R.
\]

Dies ist exakt die Randfläche
\[
R+\varepsilon=\Delta
\]
von \(\mathfrak W_{\rm SW1}\), nicht dessen Inneres.

\[
D_-=R
\iff
R=\frac{\Delta}{2},
\]
unmöglich im Inneren wegen (SW1.5).

### 5.2 \(D_0\)-Randtreffer

\[
D_0=\varepsilon
\iff
\varepsilon=\Delta,
\]
unmöglich wegen \(\varepsilon<\Delta-R<\Delta\).

\[
D_0=R
\iff
R=\Delta,
\]
unmöglich wegen \(R<\Delta/2\).

### 5.3 \(D_+\)-Randtreffer

\[
D_+=\varepsilon
\iff
\varepsilon=\Delta+R,
\]
unmöglich, da bereits \(\varepsilon<\Delta-R\).

### 5.4 \(E\)-Randtreffer

\[
E=\varepsilon
\iff
R+\varepsilon=e.
\]

Da \(e>\Delta\), widerspricht dies \(R+\varepsilon<\Delta\).

\[
E=R
\iff
R=\frac e2.
\]

Da \(e>\Delta\), gilt \(e/2>\Delta/2\), im Widerspruch zu (SW1.5).

### 5.5 \(A_*\)-Randtreffer

\[
A_*=\varepsilon
\iff
R+\varepsilon=d,
\]
unmöglich wegen \(d>\Delta\).

\[
A_*=R
\iff
R=\frac d2,
\]
unmöglich wegen \(d/2>\Delta/2>R\).

### 5.6 Einzige aktive Wall-Wall-Kollision

Die einzige HT.31-Wall-Wall-Fläche ist
\[
R=C=\frac{e-\Delta}{2}.
\]

Nach (SW1.4)
\[
C>\frac{\Delta}{2}>R,
\]
also liegt auch diese Fläche außerhalb des Subwedges.

Damit gilt
\[
\boxed{
\text{Keine der zehn HT.31-Flächen schneidet das Innere von }\mathfrak W_{\rm SW1}.
}
\tag{SW1.18}
\]

---

## 6. Identifikation mit Chamber I.1

In §12 des Tail-FG-Audits lautet Chamber I.1:
\[
0<R<\frac{\Delta}{2},
\qquad
\varepsilon<\Delta-R.
\]

Nach (SW1.5)–(SW1.6) ist dies auf \(\mathfrak W_{\rm SW1}\) erfüllt.

Daher
\[
\boxed{
\mathfrak W_{\rm SW1}\subset \mathrm{I.1}.
}
\tag{SW1.19}
\]

Da
\[
\varepsilon<\Delta-R
\iff
R+\varepsilon<\Delta,
\]
ist \(\mathfrak W_{\rm SW1}\) gerade der \(R<\varepsilon\)-Teil der I.1-Bedingung.

Im hier relevanten Tail-Sektor kollabiert die **Fiber-Graph-Membership-Geometrie** somit auf genau einen offenen Typ:
\[
\boxed{ZZZ.}
\tag{SW1.20}
\]

---

## 7. Nichtleere und explizite Zeugen für beide Unterkammern und die Wand

Da §9 zeigt, dass die volle A-Wall-Geometrie innerhalb des Single-FG-Chambers an
\[
\varepsilon=\frac{\Delta}{2}
\]
zerfällt, werden die beiden offenen Unterkammern und die Degenerationsfläche getrennt bezeugt.

### 7.1 Unterkammer \(\varepsilon<\Delta/2\)

Setze
\[
R_-=\frac{\Delta}{6},
\qquad
\varepsilon_-=\frac{\Delta}{3},
\qquad
\sigma_-=\frac{\Delta}{12}.
\]

Dann
\[
0<\sigma_-<R_-<\varepsilon_-<\frac{\Delta}{2},
\]
und
\[
R_-+\varepsilon_-=\frac{\Delta}{2}<\Delta.
\]

Also liegt dieser Punkt im restricted-tail-SW1 und bezeugt die untere offene A-Wall-Unterkammer.

### 7.2 Degenerationsfläche \(\varepsilon=\Delta/2\)

Setze
\[
R_0=\frac{\Delta}{4},
\qquad
\varepsilon_0=\frac{\Delta}{2},
\qquad
\sigma_0=\frac{\Delta}{8}.
\]

Dann
\[
0<\sigma_0<R_0<\varepsilon_0,
\]
und
\[
R_0+\varepsilon_0=\frac{3\Delta}{4}<\Delta.
\]

Somit ist
\[
\boxed{
(R_0,\varepsilon_0)\in\mathfrak W_{\rm SW1},
\qquad
\varepsilon_0=\frac{\Delta}{2}.
}
\tag{SW1.21}
\]

Die Parameterwand schneidet den Subwedge also tatsächlich und ist keine formale oder leere Grenzmenge.

### 7.3 Unterkammer \(\varepsilon>\Delta/2\)

Setze
\[
R_+=\frac{\Delta}{10},
\qquad
\varepsilon_+=\frac{3\Delta}{5},
\qquad
\sigma_+=\frac{\Delta}{20}.
\]

Dann
\[
0<\sigma_+<R_+<\frac{\Delta}{2}<\varepsilon_+,
\]
und
\[
R_++\varepsilon_+
=
\frac{7\Delta}{10}
<
\Delta.
\]

Also liegt auch dieser Punkt im restricted-tail-SW1 und bezeugt die obere offene A-Wall-Unterkammer.

Damit sind beide offenen Unterkammern sowie die dazwischenliegende Parameterwand explizit nichtleer bezeugt.


---

## 8. Verträglichkeit mit einem \(R\to0\)-Descent

Fixiere irgendein
\[
0<\varepsilon_*<\Delta.
\]

Für jede Folge
\[
R_n\downarrow0
\]
mit schließlich
\[
R_n<\min\{\varepsilon_*,\Delta-\varepsilon_*\}
\]
gilt
\[
0<R_n<\varepsilon_*,
\qquad
R_n+\varepsilon_*<\Delta.
\]

Mit beispielsweise
\[
\sigma_n=\frac{R_n}{2}
\]
gilt zusätzlich
\[
0<\sigma_n\le R_n.
\]

Somit ist die Standing-Hypothese
\[
R+\varepsilon<\Delta
\]
mit einem \(R\to0\)-Descent im restricted-tail-Stratum kompatibel.

Dies ist nur eine Parameterverträglichkeitsaussage. Es folgt daraus keine C6-, Strong-Terminal- oder Konvergenzaussage.

Die Einschränkung \(R+\varepsilon<\Delta\) beschränkt dabei **Konstruktionsparameter**, nicht den freien \((z,h)\)-Koordinatenraum. Sie ist daher kategorial kein A0-Abschluss und auch kein Wegdefinieren freier Koordinaten. Ob ein auf diesem Parameterwedge gewonnener Nichtentartungssatz für die spätere globale Konstruktion ausreicht, bleibt eine separate Downstream-Frage.

---

## 9. Wichtige Nuance: HT-A3/A-Wall kollabiert nicht vollständig

Die erste HT-A3-Kollision ist HT.17:
\[
I_b\cap I_-\ne\varnothing
\iff
\varepsilon-R>\Delta.
\]

Unter
\[
R+\varepsilon<\Delta
\]
gilt
\[
\varepsilon-R<\varepsilon+R<\Delta,
\]
also
\[
\boxed{
I_b\cap I_-=\varnothing.
}
\tag{SW1.23}
\]

Die zweite HT-A3-Kollision ist HT.18:
\[
I_b\cap I_+\ne\varnothing
\iff
R<\frac{\Delta}{2}<\varepsilon.
\]

Auf \(\mathfrak W_{\rm SW1}\) ist \(R<\Delta/2\) automatisch. Daher reduziert sich diese Bedingung zu
\[
\boxed{
I_b\cap I_+\ne\varnothing
\iff
\varepsilon>\frac{\Delta}{2}.
}
\tag{SW1.24}
\]

Folglich besitzt der Single-FG-Chamber-Subwedge weiterhin die bereits aus NEU-A-WALL-1 bekannte Parameterwand
\[
\boxed{
\varepsilon=\frac{\Delta}{2}.
}
\tag{SW1.25}
\]

Genauer:

- für \(\varepsilon<\Delta/2\): kein \(I_b\)-/\(I_+\)-Overlap;
- für \(\varepsilon=\Delta/2\): die offenen Shells berühren sich nur an einem \(L^2\)-nulligen Endpunkt;
- für \(\varepsilon>\Delta/2\): positiver \(I_b\)-/\(I_+\)-Overlap.

Daher
\[
\boxed{
\text{ein FG-Chamber bedeutet nicht ein vollständiges A0-Wall-Chamber.}
}
\tag{SW1.26}
\]

Die volle A-Wall/Fiber-Graph-Geometrie des Subwedges zerfällt weiterhin in zwei offene A-Wall-Unterkammern plus die Parameterdegenerationsfläche \(\varepsilon=\Delta/2\).

Diese Fläche ist eine echte Parameterkonfiguration und darf nicht als \(L^2\)-Nullmenge wegdefiniert werden.

---

## 10. Kandidatenurteil

Der eingeschränkte Kandidatensatz lautet:

Unter
\[
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta,
\]
liegen alle fünf Tail-FG-\(s\)-Wände strikt außerhalb von \((R,\varepsilon)\). Die sechs Tail-Argumente sind auf dem gesamten \(s\)-Intervall direkte Blind-\(z\)-Koordinaten; der \(x_0\)-Ast tritt nicht auf. Keine der zehn HT.31-Flächen schneidet das Innere dieses Subwedges.

Arbeitsstatus vor unabhängigem Review:

    HT-A4b-SW1 SINGLE-FG-CHAMBER SUBWEDGE: ?[O]

    HT-A4b TAIL-FG COMMON REFINEMENT EXHAUSTIVITY: ?[O]
    HT-RED TAIL GAUSSIAN ELIMINATION:              ?[O]
    A0 FULL FREE-COORDINATE COVERAGE:              ?[O]
    SCHUR CROSS-GRAM INJECTIVITY:                  ?[O]

Insbesondere wird **nicht** behauptet, dass die globale 15-Chamber-Exhaustivität bereits geprüft oder geschlossen ist.

---

## 11. Konsequenz für die nächste Rechnung

Falls HT-A4b-SW1 unabhängiges GREEN erhält, kann der erste exakte Downstream-Angriff auf dem Subwedge mit der uniformen Tail-Membership
\[
(Z,Z,Z,Z,Z,Z)
\]
arbeiten.

Dabei muss die A-Wall-Aufspaltung
\[
\varepsilon<\Delta/2,
\qquad
\varepsilon=\Delta/2,
\qquad
\varepsilon>\Delta/2
\]
weiterhin getrennt bleiben.

Dieses Audit selbst führt **keine** Downstream-Elimination durch.

---

## 12. Firewall

Aus HT-A4b-SW1 folgt nicht:

- globale Exhaustivität der zehn HT.31-Flächen / 15 Chambers;
- HT-A4b global;
- HT-RED;
- Trivialität des reduzierten Kernes;
- A0-Abschluss;
- \(\ker\Gamma_I=\{0\}\);
- Schur-Cross-Gram-Injektivität;
- Closed Range / bounded below;
- Strong Terminal Transport;
- Objekt X;
- RH.

---

## 13. Adversarialer Review-Auftrag

Vor einer Statusbuchung sind unabhängig zu prüfen:

1. die Ordnung \(0<\Delta<\varepsilon_{\max}<e<d\);
2. \(e>2\Delta\) und damit \(C>\Delta/2\);
3. die Folgerungen \(R<\Delta/2\) und \(\varepsilon<\Delta-R\);
4. dass alle fünf \(s\)-Wände \(D_-,D_0,D_+,E,A_*\) strikt rechts von \(\varepsilon\) liegen;
5. die sechs Membership-Zeilen (SW1.13)–(SW1.16);
6. dass der \(x_0\)-Ast nicht auftritt, HT.27 auf SW1 vakuum erfüllt ist und damit die TR.13-Abhängigkeit dort nicht benötigt wird;
7. die Herkunft jeder der zehn HT.31-Flächen und ihr Ausschluss aus dem offenen \((R,\varepsilon)\)-Inneren;
8. die Identifikation mit Chamber I.1;
9. die drei Zeugen für \(\varepsilon<\Delta/2\), \(\varepsilon=\Delta/2\) und \(\varepsilon>\Delta/2\);
10. die \(R\to0\)-Verträglichkeit und die Unterscheidung Parameterrestriktion vs. freie Koordinaten;
11. die HT-A3-Nuance anhand HT.17/HT.18: \(I_b\cap I_-\) ist ausgeschlossen, \(I_b\cap I_+\) bleibt genau für \(\varepsilon>\Delta/2\) möglich;
12. dass die allowed boundary \(\sigma=R\) keine zusätzliche HT.31-FG-Wand erzeugt;
13. die Scope-Firewall.

Keine Promotion und kein Merge ohne unabhängiges GREEN gegen den exakten PR-Diff.
