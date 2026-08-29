# P11/R32 — SW1-A0 Full Free-Coordinate Coverage Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-delta-descent@d73d3fdf4b1f919fc9526fc09ce206866b472704  
> **Status:** `AI-GREEN candidate + independent GREEN (certificate)` — A0 Full Free-Coordinate Coverage auf SW1 exhaustiv geprüft; **keine Promotion**.  
> **Scope:** ausschließlich A0/Randfall-/Uniformitäts-Firewall auf SW1. Keine Schur-Injektivität.

---

## 0. Exakte Bedeutung von A0

Die kanonische Roadmap verlangt vor dem eigentlichen finite-level Cross-Gram-Angriff, dass die gemeinsame 11-Wort-/Hub-Zellzerlegung den vollständigen freien Koordinatenraum

\[
(z,h)\in
\mathcal Z_R^+
\oplus
L^2(\mathcal V_R^{\rm SW1})
\tag{A0.1}
\]

abdeckt.

A0 ist damit eine **Coverage-/Exhaustivitätsaussage**. Es behauptet noch nicht, dass der auf diesen Zellen entstehende Rohoperator injektiv ist.

Input:

1. SW1-KNF:
   \[
   \mathcal K_R
   \cong
   \mathcal Z_R^+
   \oplus
   L^2(\mathcal V_R^{\rm SW1});
   \]
2. Stage 12 des gestapelten SW1-Δ-DESCENT-Kandidaten: der Sample-Summand
   \(L^2(\mathcal V_R^{\rm SW1})\) ist vollständig als Row-Scope behandelt;
3. der auditierte A-Wall-Kollaps:
   \[
   \mathscr W_{A,+}^{\circ}
   =
   \{\varepsilon,\ a-\varepsilon,\ a+\varepsilon,\ 2d-\varepsilon,\ T-\varepsilon\}.
   \tag{A0.2}
   \]

Die positiven inneren Hub-Supportwände sind
\[
\sigma,\qquad e+\sigma,\qquad a+\sigma,
\tag{A0.3}
\]
zusätzlich zu den Samplingfenstergrenzen
\[
a\pm R,\qquad b\pm R,\qquad T\pm R.
\tag{A0.4}
\]

---

## 1. SW1 kollabiert die alte Parameter-Firewall

Auf SW1:
\[
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta.
\tag{A0.5}
\]

Daraus
\[
2R<R+\varepsilon<\Delta,
\]
also
\[
\boxed{R<\frac{\Delta}{2}.}
\tag{A0.6}
\]

Da
\[
\Delta<e<d,
\]
folgt
\[
\boxed{
R<\frac{\Delta}{2}<\frac e2<\frac d2<d.
}
\tag{A0.7}
\]

Damit sind innerhalb SW1 die historischen Parameterwände
\[
R=\frac e2,\qquad
R=\frac d2,\qquad
R=d
\]
unmöglich.

Ebenso ist \(R=\varepsilon\) ausgeschlossen, und
\[
R=e+\varepsilon
\]
ist wegen \(R<\varepsilon<e+\varepsilon\) ausgeschlossen.

Als echte SW1-Randlagen verbleiben nur
\[
\boxed{\sigma=R}
\tag{A0.8}
\]
und
\[
\boxed{\varepsilon=\frac{\Delta}{2}.}
\tag{A0.9}
\]

Die erste ändert nur eine Hub-Supportgrenze innerhalb des Samplefensters; die zweite ist die bekannte Kollision
\[
a+\varepsilon=2d-\varepsilon.
\tag{A0.10}
\]

---

## 2. Exakter blinder KNF-Raum

Modulo Endpunkte ist
\[
\boxed{
\mathcal Z_{R,\rm SW1}^{\rm phys}
=
Z_1\dot\cup Z_2\dot\cup Z_3\dot\cup Z_4
}
\tag{A0.11}
\]
mit
\[
Z_1=(0,a-R),
\tag{A0.12}
\]
\[
Z_2=(a+R,b-R),
\tag{A0.13}
\]
\[
Z_3=(b+R,T-R),
\tag{A0.14}
\]
\[
Z_4=(T+R,T+\varepsilon).
\tag{A0.15}
\]

Insbesondere ist der historische Horizontschwanz \(Z_4\) ausdrücklich enthalten.

---

## 3. Gemeinsame A-/Hub-Wände auf dem blinden Raum

Auf \(Z_1\) gilt die strikte Ordnung
\[
\boxed{
0<
\sigma<
\varepsilon<
e+\sigma<
a-\varepsilon<
a-R.
}
\tag{A0.16}
\]

Hier ist \(\sigma<R<\varepsilon\) für die offene \(\sigma<R\)-Unterkammer angenommen. Für \(\sigma=R\) bleibt dieselbe Ordnung; es kollabiert keine positive \(z\)-Zelle, weil \(R\) selbst keine zusätzliche innere A-/Hub-Wand von \(Z_1\) ist.

Die knappen Schritte:
\[
(e+\sigma)-\varepsilon
=
(e-\Delta)
+
[\Delta-(R+\varepsilon)]
+
(R+\sigma)
>0,
\tag{A0.17}
\]
und
\[
(a-\varepsilon)-(e+\sigma)
=
(d-\Delta)
+
[\Delta-(R+\varepsilon)]
+
(R-\sigma)
>0.
\tag{A0.18}
\]

Ferner
\[
(a-R)-(a-\varepsilon)=\varepsilon-R>0.
\]

Auf \(Z_2\) liegen exakt die beiden A-Wände
\[
a+\varepsilon,\qquad 2d-\varepsilon.
\tag{A0.19}
\]
Beide liegen strikt im Inneren von \(Z_2\), denn
\[
(2d-\varepsilon)-(a+R)
=
\Delta-(R+\varepsilon)>0,
\tag{A0.20}
\]
\[
(b-R)-(a+\varepsilon)
=
d-(R+\varepsilon)>d-\Delta>0.
\tag{A0.21}
\]

Ihre Reihenfolge wird ausschließlich durch
\[
(2d-\varepsilon)-(a+\varepsilon)
=
\Delta-2\varepsilon
\tag{A0.22}
\]
bestimmt.

Auf \(Z_3\) liegt exakt die A-Wand
\[
T-\varepsilon,
\tag{A0.23}
\]
und
\[
(T-\varepsilon)-(b+R)
=
e-(R+\varepsilon)
>
e-\Delta>0,
\tag{A0.24}
\]
\[
(T-R)-(T-\varepsilon)=\varepsilon-R>0.
\tag{A0.25}
\]

Auf \(Z_4\) liegt keine weitere innere A-/Hub-Wand.

Die zusätzliche Hub-Wand
\[
a+\sigma
\]
liegt wegen \(\sigma\le R\) im Samplefenster
\[
(a,a+R]
\]
und erzeugt daher keine blinde \(z\)-Zelle.

---

## 4. A0-Zellen — Chamber I

Sei
\[
0<\varepsilon<\frac{\Delta}{2}.
\tag{A0.26}
\]

Dann ist \(\mathcal Z_R^+\) a.e. die orthogonale Summe der folgenden elf offenen Supportzellen:

\[
\boxed{
\begin{aligned}
C_1&=(0,\sigma),\\
C_2&=(\sigma,\varepsilon),\\
C_3&=(\varepsilon,e+\sigma),\\
C_4&=(e+\sigma,a-\varepsilon),\\
C_5&=(a-\varepsilon,a-R),\\
C_6&=(a+R,a+\varepsilon),\\
C_7&=(a+\varepsilon,2d-\varepsilon),\\
C_8&=(2d-\varepsilon,b-R),\\
C_9&=(b+R,T-\varepsilon),\\
C_{10}&=(T-\varepsilon,T-R),\\
C_{11}&=(T+R,T+\varepsilon).
\end{aligned}}
\tag{A0.27}
\]

Auf jedem \(C_j\) ist das aktive Gate-/Source-Horizon-Muster aller elf Wörter von \(A\) konstant; ebenso ist das aktive Hub-Supportmuster konstant.

---

## 5. A0-Zellen — Chamber II

Sei
\[
\frac{\Delta}{2}<\varepsilon<\Delta-R.
\tag{A0.28}
\]

Dann bleiben \(C_1,\ldots,C_5,C_9,C_{10},C_{11}\) unverändert, während \(Z_2\) exakt in

\[
\boxed{
\begin{aligned}
C_6'&=(a+R,2d-\varepsilon),\\
C_7'&=(2d-\varepsilon,a+\varepsilon),\\
C_8'&=(a+\varepsilon,b-R)
\end{aligned}}
\tag{A0.29}
\]
zerfällt.

Auch hier sind A-Wort- und Hub-Supportmuster auf jeder Zelle konstant.

---

## 6. Degenerationsfläche \(\varepsilon=\Delta/2\)

Für
\[
\varepsilon=\frac{\Delta}{2}
\tag{A0.30}
\]
gilt
\[
a+\varepsilon=2d-\varepsilon.
\tag{A0.31}
\]

Die mittlere Zelle aus Chamber I/II kollabiert auf einen einzelnen räumlichen Punkt. Damit besitzt \(Z_2\) a.e. nur die beiden Zellen
\[
(a+R,a+\varepsilon),
\qquad
(a+\varepsilon,b-R).
\tag{A0.32}
\]

Da ein einzelner räumlicher Punkt Lebesgue-Nullmaß besitzt, entsteht keine zusätzliche \(L^2\)-Koordinatenklasse.

Somit ist auch die Parameter-Degenerationsfläche vollständig abgedeckt.

---

## 7. Sample-Summand \(h\)

Der freie Sample-Summand ist
\[
\mathcal V_R^{\rm SW1}
=
(a,a+R)
\cup
(b-R,b+R)
\cup
(T-R,T+R).
\tag{A0.33}
\]

Stage 12 des gestapelten SW1-Δ-DESCENT-Audits behandelt diesen gesamten Summanden.

Die einzige zusätzliche positive Hubwand im Inneren dieses freien Sample-Summanden ist
\[
a+\sigma.
\tag{A0.34}
\]

Für \(\sigma<R\) teilt sie
\[
(a,a+R)
\]
in
\[
(a,a+\sigma),
\qquad
(a+\sigma,a+R).
\tag{A0.35}
\]

Für
\[
\sigma=R
\]
fällt sie auf den rechten Rand \(a+R\), wiederum ohne neue \(L^2\)-Klasse.

Die \(b\)- und \(T\)-Sampleintervalle besitzen innerhalb SW1 keine weitere gemeinsame A-/Hub-Wand.

Der linke \(a\)-Branch
\[
(a-R,a)
\]
ist keine freie \(h\)-Koordinate; er wird durch KNF.11 eindeutig rekonstruiert.

---

## 8. A0-Coverage-Satz

Unter SW1 gilt a.e.:

1. jeder freie blinde \(z\)-Supportpunkt liegt in genau einer Zelle aus (A0.27), (A0.29) oder der degenerierten Variante (A0.32);
2. jeder freie Sample-\(h\)-Supportpunkt liegt in einer der Samplezellen aus §7;
3. alle räumlichen Zellgrenzen bilden eine endliche Nullmenge;
4. die einzigen verbleibenden Parametergrenzen \(\sigma=R\) und \(\varepsilon=\Delta/2\) wurden explizit behandelt;
5. der Horizontschwanz
   \[
   (T+R,T_0)
   \]
   ist \(C_{11}\) und nicht ausgelassen.

Damit:

\[
\boxed{
\text{A0 FULL FREE-COORDINATE COVERAGE ist auf SW1 exhaustiv reduziert.}
}
\tag{A0.36}
\]

Genauer:
\[
\boxed{
\mathcal Z_R^+
=
\bigoplus_{\text{A0-Zellen }C}
L^2_{\rm even}(C\cup(-C))
}
\tag{A0.37}
\]
a.e., ergänzt um den vollständig behandelten Sample-Summanden aus Stage 12.

---

## 9. Was A0.36 ausdrücklich NICHT beweist

A0.36 ist ausschließlich der Roadmap-Punkt „keine unbehandelte freie Koordinaten-/Randklasse“.

Es beweist **nicht**:

- dass die Rohgleichung auf jeder A0-Zelle bereits gelöst ist;
- dass der resultierende gekoppelte Zelloperator injektiv ist;
- \(\ker\Gamma_I=\{0\}\);
- HT-RED;
- Closed Range / bounded below;
- Objekt X;
- RH.

Der nächste mathematische Knoten ist nach erfolgreichem Review daher

\[
\boxed{
\text{A1: vollständiges finite-cell Rohsystem auf den A0-Zellen.}
}
\tag{A0.38}
\]

Dort ist entweder ein endlicher invertierbarer Zell-/Orbitoperator oder ein exakter Gegenvektor zu suchen.

---

## 10. Review-/Zertifikatsstatus

Der A0-Coverage-Satz wurde adversarial gegen die SW1-KNF-, A-Wall- und Stage-12-Eingaben gegengeprüft.

Das reproduzierbare Zertifikat
`scripts/certify_sw1_a0_coverage.py`
prüft mit Python/SymPy 1.14.0:

- den SW1-Kollaps (R<\Delta/2) und damit den Ausschluss der historischen R-Wände;
- die vollständige positive Hub-Wall-Liste im Horizont;
- sämtliche Zelllängen in beiden offenen \(\varepsilon\)-Chambers;
- die Degenerationsfläche \(\varepsilon=\Delta/2\);
- die explizite Horizontschwanzzelle;
- die exakte Gleichheit der Zelllängensumme mit dem gesamten blinden Supportmaß.

Committed Script-Blob:
`dcc30ffd51cda487efd34b90b58f8c7913e988d1`.

Exakte committed Ausführung: **PASS**.

Damit gilt:
\[
\boxed{
\mathrm{SW1\!-\!A0\ Coverage}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

Keine Promotion. Insbesondere bleibt A1 / die Injektivität des gekoppelten finite-cell Rohsystems offen.


