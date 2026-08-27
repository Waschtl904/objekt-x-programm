# P11/R32 — A-Wall-Reduktion der elf Full-Rest-Gram-Wörter

**Status:** Kandidat; keine Promotion.  
**Arbeitsname:** `NEU-A-WALL-1`.  
**Repo-Basis:** `main@db02e468b23f4f6270d6153f2cee949fb604981e`.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Provenienz:** `P11_R32_SCHUR_INVERSE_ELIMINATION_AUDIT.md`, `P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md`, `FORSCHUNGS_ROADMAP_2026-08-26.md`.

> Interner algebraischer Vorcheck: GREEN.  
> Projektstatus bis zu unabhängigem Review und ausdrücklicher Promotion: `?[O]`.

---

## 0. Aussage in einem Satz

Im Drei-Shift-Fenster

\[
2a<T_0<c:=\frac12\log5
\]

zerfällt

\[
A=R^*R
\]

nach SE.15–SE.16 in exakt elf \(K^*M_\Omega K\)-Wörter. Jedes dieser Wörter besitzt eine explizite Vier-Echo-Punktformel, und sämtliche inneren physischen Cutoff-/Horizon-Wände dieser elf Wörter kollabieren auf die endliche Menge

\[
\boxed{
\mathscr W_A^\circ
=
\pm\{
\varepsilon,\,
a-\varepsilon,\,
a+\varepsilon,\,
2d-\varepsilon,\,
T-\varepsilon
\}.
}
\]

Dabei gilt \(T_0=T+\varepsilon\).

Dies reduziert die Rest-Geometrie erheblich, beweist aber weder die Schur-Crossblock-Injektivität noch den Abschluss von A0.

---

## 1. Setup und Notation

Setze

\[
a=\frac12\log2,
\qquad
b=\frac12\log3,
\qquad
T=2a=\log2,
\]

\[
c=\frac12\log5,
\qquad
T_0=T+\varepsilon,
\qquad
0<\varepsilon<c-T.
\]

Ferner

\[
d=b-a,
\qquad
e=T-b,
\qquad
a=d+e,
\]

und

\[
\Delta:=d-e
=\frac12\log\frac98>0.
\]

Numerisch:

\[
a\approx0.3465735903,
\quad
b\approx0.5493061443,
\quad
T\approx0.6931471806,
\]

\[
d\approx0.2027325541,
\quad
e\approx0.1438410362,
\]

\[
\Delta\approx0.0588915178,
\qquad
\frac{\Delta}{2}\approx0.0294457589.
\]

Für den Horizontoperator gilt

\[
K_s^{\rm tr}:=
P_{T_0}D_sE_{T_0},
\qquad
D_s:=U_{s/2}-U_{-s/2}.
\]

Wir benutzen die Konvention

\[
(U_t f)(x)=f(x-t).
\]

Für \(\lambda>0\) schreibe

\[
\chi_\lambda(u)
:=
1_{\{|u|\le T_0-\lambda\}}.
\]

Definiere das elementare Gram-Wort

\[
\boxed{
W_{\delta,\eta}^{(\lambda)}
:=
(K_{2\delta}^{\rm tr})^*
M_{\{|u|\le T_0-\lambda\}}
K_{2\eta}^{\rm tr}.
}
\tag{A.1a}
\]

Alle Funktionen werden bei Auswertungen außerhalb \((-T_0,T_0)\) durch Null fortgesetzt; diese Nullfortsetzung wird mit \(\widetilde y\) bezeichnet.

---

## 2. Vier-Echo-Punktformel

### Lemma A-W1 — Schiefadjungiertheit des trunkierten Shiftoperators

Aus

\[
U_t^*=U_{-t}
\]

folgt

\[
D_s^*
=
U_{-s/2}-U_{s/2}
=
-D_s.
\]

Da

\[
P_{T_0}=E_{T_0}^*,
\]

gilt

\[
\boxed{
(K_s^{\rm tr})^*
=
-K_s^{\rm tr}.
}
\tag{A.1b}
\]

### Lemma A-W2 — Vier-Echo-Formel

Für \(y\in L^2(-T_0,T_0)\) gilt a.e. auf \((-T_0,T_0)\)

\[
\boxed{
\begin{aligned}
(W_{\delta,\eta}^{(\lambda)}y)(x)
={}&
-\chi_\lambda(x-\delta)
 \widetilde y(x-\delta-\eta)
\\
&+
\chi_\lambda(x-\delta)
 \widetilde y(x-\delta+\eta)
\\
&+
\chi_\lambda(x+\delta)
 \widetilde y(x+\delta-\eta)
\\
&-
\chi_\lambda(x+\delta)
 \widetilde y(x+\delta+\eta).
\end{aligned}
}
\tag{A.1}
\]

#### Beweis

Zunächst

\[
K_{2\eta}^{\rm tr}y(u)
=
\widetilde y(u-\eta)-\widetilde y(u+\eta).
\]

Setze

\[
g(u)
=
\chi_\lambda(u)
[
\widetilde y(u-\eta)-\widetilde y(u+\eta)
].
\]

Wegen (A.1b) gilt

\[
W_{\delta,\eta}^{(\lambda)}y
=
-K_{2\delta}^{\rm tr}g.
\]

Somit

\[
(W_{\delta,\eta}^{(\lambda)}y)(x)
=
-g(x-\delta)+g(x+\delta),
\]

und Einsetzen von \(g\) liefert exakt (A.1). \(\square\)

Insbesondere ist die Vorzeichenfolge

\[
\boxed{-\;+\;+\;-}.
\]

---

## 3. Exakte Elf-Wort-Zerlegung

Nach SE.12–SE.14:

\[
\Phi_{2,0}
=
2^{-3/4}K_{\log2}^{\rm tr}
+
2^{-3/2}K_{2\log2}^{\rm tr}
+
2^{-9/4}K_{3\log2}^{\rm tr},
\]

\[
\Phi_{2,1}
=
2^{-3/2}K_{2\log2}^{\rm tr},
\]

\[
\Phi_{3,0}
=
3^{-3/4}K_{\log3}^{\rm tr}.
\]

Da

\[
\log2=2a,
\qquad
2\log2=2T,
\qquad
3\log2=6a=2(3a),
\qquad
\log3=2b,
\]

lassen sich alle Wörter in der Notation (A.1a) schreiben.

Die Cutoffparameter sind \(\lambda=a\) für \(\Omega_{2,0}\), \(\lambda=T\) für \(\Omega_{2,1}\) und \(\lambda=b\) für \(\Omega_{3,0}\).

| Nr. | Wort | Koeffizient |
|---:|---|---:|
| 1 | \(W_{a,a}^{(a)}\) | \((\log2)2^{-3/2}\) |
| 2 | \(W_{a,T}^{(a)}\) | \((\log2)2^{-9/4}\) |
| 3 | \(W_{a,3a}^{(a)}\) | \((\log2)2^{-3}\) |
| 4 | \(W_{T,a}^{(a)}\) | \((\log2)2^{-9/4}\) |
| 5 | \(W_{T,T}^{(a)}\) | \((\log2)2^{-3}\) |
| 6 | \(W_{T,3a}^{(a)}\) | \((\log2)2^{-15/4}\) |
| 7 | \(W_{3a,a}^{(a)}\) | \((\log2)2^{-3}\) |
| 8 | \(W_{3a,T}^{(a)}\) | \((\log2)2^{-15/4}\) |
| 9 | \(W_{3a,3a}^{(a)}\) | \((\log2)2^{-9/2}\) |
| 10 | \(W_{T,T}^{(T)}\) | \((\log2)/4\) |
| 11 | \(W_{b,b}^{(b)}\) | \(2(\log3)/(3\sqrt3)\) |

Also

\[
\boxed{
\begin{aligned}
A={}&
(\log2)2^{-3/2}W_{a,a}^{(a)}
+
(\log2)2^{-9/4}W_{a,T}^{(a)}
\\
&+
(\log2)2^{-3}W_{a,3a}^{(a)}
+
(\log2)2^{-9/4}W_{T,a}^{(a)}
\\
&+
(\log2)2^{-3}W_{T,T}^{(a)}
+
(\log2)2^{-15/4}W_{T,3a}^{(a)}
\\
&+
(\log2)2^{-3}W_{3a,a}^{(a)}
+
(\log2)2^{-15/4}W_{3a,T}^{(a)}
\\
&+
(\log2)2^{-9/2}W_{3a,3a}^{(a)}
+
\frac{\log2}{4}W_{T,T}^{(T)}
\\
&+
\frac{2\log3}{3\sqrt3}W_{b,b}^{(b)}.
\end{aligned}
}
\tag{A.2}
\]

Die beiden formal gleichen Shiftpaare \(W_{T,T}^{(a)}\) und \(W_{T,T}^{(T)}\) dürfen nicht zusammengezogen werden, da ihre Multiplikatorfenster verschieden sind.

---

## 4. Vollständige innere Wall-Liste der elf Wörter

Aus (A.1) können nur zwei Typen räumlicher Wände entstehen.

### 4.1 Multiplikatorwände

\[
|x\pm\delta|=T_0-\lambda.
\tag{A.3}
\]

### 4.2 Source-Horizon-Wände

\[
|x\pm\delta\pm\eta|=T_0.
\tag{A.4}
\]

Auf der positiven Halbachse \(0<x<T_0\) ergibt direktes Einsetzen:

| Wort | innere Gate-Wände | zusätzliche Source-Horizon-Wände |
|---|---|---|
| \(W_{a,a}^{(a)}\) | \(\varepsilon\) | \(\varepsilon\) |
| \(W_{a,T}^{(a)}\) | \(\varepsilon\) | \(a-\varepsilon,\ a+\varepsilon\) |
| \(W_{a,3a}^{(a)}\) | \(\varepsilon\) | \(\varepsilon,\ T-\varepsilon\) |
| \(W_{T,a}^{(a)}\) | \(a-\varepsilon\) | \(a-\varepsilon,\ a+\varepsilon\) |
| \(W_{T,T}^{(a)}\) | \(a-\varepsilon\) | \(T-\varepsilon\) |
| \(W_{T,3a}^{(a)}\) | \(a-\varepsilon\) | \(a+\varepsilon\) |
| \(W_{3a,a}^{(a)}\) | \(T-\varepsilon\) | \(\varepsilon,\ T-\varepsilon\) |
| \(W_{3a,T}^{(a)}\) | \(T-\varepsilon\) | \(a+\varepsilon\) |
| \(W_{3a,3a}^{(a)}\) | \(T-\varepsilon\) | keine weitere innere Wand |
| \(W_{T,T}^{(T)}\) | \(T-\varepsilon\) | \(T-\varepsilon\) |
| \(W_{b,b}^{(b)}\) | \(2d-\varepsilon\) | \(2d-\varepsilon\) |

Damit kollabiert die gesamte positive innere Wall-Menge auf

\[
\boxed{
\mathscr W_{A,+}^{\circ}
=
\{
\varepsilon,\,
a-\varepsilon,\,
a+\varepsilon,\,
2d-\varepsilon,\,
T-\varepsilon
\}.
}
\tag{A.5}
\]

Durch Parität folgt

\[
\boxed{
\mathscr W_A^\circ
=
\pm\mathscr W_{A,+}^{\circ}.
}
\tag{A.6}
\]

Zusätzlich existieren nur die äußeren Horizontgrenzen \(x=\pm T_0\).

---

## 5. Warum keine weiteren inneren Echos auftreten

Die formal weitesten Source-Echos der 2-adischen Neunergruppe besitzen Shiftgrößen \(5a\) bzw. \(6a\).

Im gesamten Drei-Shift-Fenster gilt

\[
2T_0<\log5.
\]

Andererseits

\[
5a
=
\frac52\log2
>
\log5,
\]

denn

\[
5a-\log5
=
\frac12\log\frac{32}{25}>0.
\tag{A.7}
\]

Somit \(5a>2T_0\). A fortiori \(6a>2T_0\).

Diese weit entfernten Adjoint-/Source-Echos können daher keinen inneren Horizon-Kontakt erzeugen.

Das aktive Source-Echoalphabet reduziert sich auf

\[
\boxed{
\{0,\pm a,\pm T,\pm3a,\pm4a,\pm2b\}.
}
\tag{A.8}
\]

---

## 6. Wall-Ordnung und die einzige interne Kollision

Für \(0<\varepsilon<c-T\) sind alle relativen Ordnungen der fünf positiven Wände fest, mit genau einer Ausnahme.

Es gilt

\[
2d-a=d-e=\Delta.
\]

Daher

\[
(2d-\varepsilon)-(a+\varepsilon)
=
\Delta-2\varepsilon.
\tag{A.9}
\]

Somit gibt es exakt zwei offene Wall-Order-Chambers.

### Chamber I

Für

\[
0<\varepsilon<\frac{\Delta}{2}
\]

gilt

\[
\boxed{
0<
\varepsilon<
a-\varepsilon<
a+\varepsilon<
2d-\varepsilon<
T-\varepsilon<
T_0.
}
\tag{A.10}
\]

### Chamber II

Für

\[
\frac{\Delta}{2}<\varepsilon<c-T
\]

gilt

\[
\boxed{
0<
\varepsilon<
a-\varepsilon<
2d-\varepsilon<
a+\varepsilon<
T-\varepsilon<
T_0.
}
\tag{A.11}
\]

Auf der einzigen inneren Kollisionsfläche

\[
\boxed{
\varepsilon=\frac{\Delta}{2}
}
\tag{A.12}
\]

fallen \(a+\varepsilon=2d-\varepsilon\) zusammen.

Damit besitzt die reine A-Wort-Geometrie genau zwei offene Wall-Order-Chambers plus diese degenerierte Parametergrenze.

---

## 7. Korrektur zweier scheinbarer A0-Randprobleme

### 7.1 Räumliche Cutoff-Wände sind keine zusätzlichen \(L^2\)-Klassen

Für festes \(\lambda\) ist

\[
\{|x|=T_0-\lambda\}
\]

eine endliche Punktmenge und damit Lebesgue-Nullmenge.

Der Wert des Indikators \(1_{\{|x|\le T_0-\lambda\}}\) auf diesen einzelnen Randpunkten ändert den Multiplikationsoperator auf \(L^2\) nicht.

Daher erzeugen die räumlichen Cutoff-Wände selbst **keine eigene funktionalanalytische A0-Randklasse**.

Dies ist von Parameterwerten zu unterscheiden, an denen sich die Zelltopologie ändert. Solche Parametergrenzen bleiben A0-relevant.

### 7.2 Keine neue Martingale-Klasse bei \(T_0\to c^-\)

Die in SE.12–SE.14 abgeschnittenen tieferen Terme bleiben uniform inaktiv.

Für die 2-adischen Blöcke:

\[
5a-\log5
=
\frac12\log\frac{32}{25}
>0.
\tag{A.13}
\]

Für den nächsten 3-adischen Term:

\[
3b-\log5
=
\frac12\log\frac{27}{25}
>0.
\tag{A.14}
\]

Da stets \(2T_0<\log5\), bleiben damit

- der \(k=4\)-Term in \(\Phi_{2,0}\),
- der \(k=3\)-Term in \(\Phi_{2,1}\),
- der \(k=2\)-Term in \(\Phi_{3,0}\)

mit strikt positivem, von \(T_0\) unabhängigem Abstand ausgeschlossen.

Daher entsteht durch den Grenzübergang \(T_0\to c^-\) **keine neue Full-Rest-Martingale-Randklasse**.

---

## 8. Was von A0 tatsächlich offen bleibt

Die Roadmap-A0-Firewall verlangt weiterhin die Abdeckung des vollständigen freien Koordinatenraums

\[
(z,h)
\in
\mathcal Z_R^+
\oplus
L^2(\mathcal V_R).
\]

FG-TR1 liefert im Bereich \(0<R<a\) kandidatenweise

\[
\mathcal K_R
\cong
\mathcal Z_R^+
\oplus
L^2(\mathcal V_R),
\]

und für \(y\in\mathcal K_R\) die volle Koordinatenform

\[
y=\widehat\Phi_R(z,0,h).
\]

Die verbleibende Gleichung ist damit

\[
\boxed{
(I+A)\widehat\Phi_R(z,0,h)
+
HE_{\mathcal A}w
=
0.
}
\tag{A.15}
\]

Die Wall-Reduktion dieses Audits bestimmt \(A\) als explizite endliche Shift-/Cutoff-Summe, zieht aber die freie \(z\)- und \(h\)-Geometrie noch nicht vollständig durch diese elf Wörter.

Auf der bevorzugten ersten P12-Testregion

\[
0<R<a,
\qquad
T<S<T_0,
\qquad
\sigma:=S-T\le R,
\tag{A.16}
\]

müssen insbesondere die derzeit identifizierten Parameterdegenerationen in einer vollständigen gemeinsamen Zellzerlegung berücksichtigt werden:

\[
\boxed{
R=\varepsilon,\qquad
R=\frac e2,\qquad
R=\frac d2,\qquad
R=d,\qquad
R=e+\varepsilon,
}
\tag{A.17}
\]

\[
\boxed{
\sigma=R,
\qquad
\varepsilon=\frac{\Delta}{2}.
}
\tag{A.18}
\]

Ihre Bedeutungen sind verschieden:

- \(R=\varepsilon\): Horizon-Tail-/\(T+R=T_0\)-Übergang;
- \(R=e/2\): erste relevante \(b/T\)-Sample-Overlap-Grenze;
- \(R=d/2\): \(a/b\)-Sample-Overlap-/Connectivity-Grenze;
- \(R=d\): Beginn der zweiten triangulären Rekonstruktionsschicht;
- \(R=e+\varepsilon\): \(b+R=T_0\)-Horizon-Clipping;
- \(\sigma=R\): restricted-tail-Stratumgrenze;
- \(\varepsilon=\Delta/2\): Kollision der A-Wände \(a+\varepsilon\) und \(2d-\varepsilon\).

Diese Liste ist die für den derzeit bevorzugten ersten Stratum-Angriff identifizierte Parameter-Firewall. Sie ist nicht als globale Klassifikation außerhalb dieses Scopes zu lesen.

Besonders relevant bleibt für

\[
R<\varepsilon
\]

der physische Horizontschwanz

\[
(T+R,T_0),
\]

der zur blinden freien Komponente \(\mathcal Z_R^+\) beiträgt.

---

## 9. Konsequenz für die nächste Rechnung

Nach diesem Audit besteht kein Grund, zunächst eine numerische Fourier-/Legendre-Diskretisierung als Beweisschritt einzuführen.

Der nächste exakte Operatorangriff sollte vielmehr die Abbildung

\[
\boxed{
(z,h)
\longmapsto
A\,\widehat\Phi_R(z,0,h)
}
\tag{A.19}
\]

auf der gemeinsamen Wall-/Fiber-Graph-Zerlegung explizit bestimmen.

Erst falls die resultierende Echo-/Cell-Elimination die unendlichdimensionalen freien Koordinaten auf ein endliches geschlossenes Profil reduziert, wäre eine endliche Determinante eine beweisrelevante Option.

Alternativ ist auf denselben Zellen nach einem exakten nichttrivialen Gegenvektor zu suchen.

Insbesondere ist die Klasse \(R<\varepsilon\) wegen des freien Horizontschwanzes eine natürliche Falsifikationsregion.

---

## 10. Firewall

`NEU-A-WALL-1` behauptet ausschließlich:

1. die Vier-Echo-Punktformel (A.1);
2. die exakte Expansion von \(A\) in elf gewichtete Wörter;
3. den Fünf-Wände-Kollaps (A.5)–(A.6);
4. die Zwei-Chamber-Ordnung mit Kollision bei \(\varepsilon=\Delta/2\);
5. dass räumliche Cutoff-Randpunkte als Nullmengen keine eigene \(L^2\)-Klasse bilden;
6. dass die tieferen Martingaleterme bis \(T_0\to c^-\) uniform inaktiv bleiben.

Es folgt **nicht**:

- A0 ist geschlossen;
- \((I+A)\widehat\Phi_R(z,0,h)\) ist auf dem vollen freien Raum bereits analysiert;
- der augmentierte Blockkern ist trivial;
- \(\ker\Gamma_I=\{0\}\);
- eine bounded-below- oder Closed-Range-Aussage;
- Strong Terminal Transport;
- ein Kandidat für Objekt X;
- RH.

Insbesondere bleiben

\[
\boxed{
\text{A0: }?[O]
}
\]

und

\[
\boxed{
\ker\Gamma_I=\{0\}\ ?[O].
}
\]

---

## 11. Kandidatenstatus und Review-Auftrag

```text
NEU-A-WALL-1 FOUR-ECHO FORMULA: independently GREEN candidate
NEU-A-WALL-1 ELEVEN-WORD EXPANSION: independently GREEN candidate
NEU-A-WALL-1 FIVE-WALL COLLAPSE: independently GREEN candidate
NEU-A-WALL-1 WALL-ORDER CHAMBERS: independently GREEN candidate
A0 FULL FREE-COORDINATE COVERAGE: ?[O]
SCHUR CROSS-GRAM INJECTIVITY: ?[O]
```

Die vier oben promovierten Komponenten haben einen unabhängigen adversarialen Review gegen den exakten PR-Diff (PR #5, Merge-Commit `264e8ff27213b40190853e20f4639bb5c185bf9f`) bestanden: Adjungiertenschritt, alle vier Vorzeichen/Argumente in (A.1), alle elf Koeffizienten in (A.2), sämtliche Gate-/Source-Horizon-Wände in §4, Ausschluss weiterer \(5a\)-/\(6a\)-Echos, die Zwei-Chamber-Wallordnung, die Nullmengenargumentation in §7.1 und die uniformen Gaps (A.13)–(A.14).

`independently GREEN candidate` ist ausdrücklich **keine** formale mathematische Promotion (`✓[M]`), sondern die repo-formale Buchung eines bestandenen unabhängigen Reviews auf Kandidatenebene. A0 und die Schur-Cross-Gram-Injektivität bleiben unverändert `?[O]`.

Vor einer Promotion sind mindestens adversarial zu prüfen:

1. der Adjungiertenschritt \((K_s^{\rm tr})^*=-K_s^{\rm tr}\);
2. alle vier Vorzeichen und vier Argumente in (A.1);
3. alle elf Koeffizienten in (A.2);
4. jede Gate- und Source-Horizon-Wand der Tabelle in §4;
5. das Ausschließen sämtlicher zusätzlicher \(5a\)- und \(6a\)-Echos;
6. die Behauptung, dass nur \(a+\varepsilon\) und \(2d-\varepsilon\) ihre Ordnung wechseln können;
7. die Nullmengenargumentation in §7.1;
8. die uniformen Gaps (A.13)–(A.14);
9. die klare Trennung zwischen diesem Wall-Audit und der weiterhin offenen \((z,h)\)-Analyse;
10. die Scope-Firewall in §10.

Keine formale Promotion ohne unabhängiges GREEN gegen den exakten PR-Diff und ausdrückliche Projektfreigabe.
