# P11/R32 — SW1 M1-ND SMALL-R Negative Promotion

> **Datum:** 1. September 2026  
> **Promotionsstatus:** \(\checkmark[M]_{\rm neg}\)  
> **Promotierter Satz:** expliziter Small-\(R\)-Witness gegen universelle M1-ND-Nichtentartung auf SW1  
> **Kanonischer geprüfter Head vor Promotion:** \`ad0a59a4c086f207ff3bdd9e31cebdafdfe646ec\`  
> **Vollständiger CI-Lauf:** GitHub Actions Run \`33467557472\` — SUCCESS  
> **Governance:** Die ursprünglich verlangte strukturell unabhängige Drittprüfung wird für diese Promotion ausdrücklich **gewavet**, weil keine solche Instanz verfügbar ist. Dieser Waiver betrifft nur den Prozessstatus, nicht den mathematischen Scope. Es wird **kein** \`independent GREEN (external)\` behauptet.

---

## 1. Promotierter Satz

Setze

\[
T=\log2,
\qquad
\Delta=\log3-\frac32\log2,
\]

und wähle

\[
\boxed{
\varepsilon_0=\frac{\Delta}{4},
\qquad
R_0=\frac{T}{100000},
\qquad
\sigma_0=\frac{R_0}{2}.
}
\tag{P.1}
\]

Dann liegt der Parameterpunkt strikt im SW1-Scope und für den effektiven
IMG0/IMG2-Operator

\[
\mathscr N_{R_0}:
\mathscr B_K\oplus\mathscr B_W
\longrightarrow
\mathscr B_H^0
\]

gilt

\[
\boxed{
\ker\mathscr N_{R_0}\ne\{0\}.
}
\tag{P.2}
\]

Damit ist die universelle Behauptung

\[
\ker\mathscr N_R=\{0\}
\quad
\text{für alle SW1-Parameter}
\]

widerlegt.

Die zulässige Objekt-X-interne Buchung lautet deshalb

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SMALLR}:
\checkmark[M]_{\rm neg}.
}
\tag{P.3}
\]

---

## 2. Nicht promotiert

Diese Promotion behauptet **nicht**:

- \(\ker\mathscr N_R\ne0\) für jeden SW1-Parameter;
- Degeneration im oberen Chamber;
- die allgemeine Small-\(R\)-Familienaussage für jedes feste
  \(0<\varepsilon<\Delta/2\);
- eine separate formale Promotion von IMG0;
- eine separate \(\checkmark[M]_{\rm neg}\)-Buchung für
  \(\ker\Gamma_I\ne0\);
- Scheitern jeder möglichen finite-level Geometrie;
- Scheitern von Objekt X;
- irgendeine Aussage über RH.

Die allgemeine Lower-Chamber-Small-\(R\)-Aussage in
\`P11_R32_SW1_M1_ND_IMG4_GENERAL_SMALLR_NOGO_CANDIDATE.md\`
bleibt ein separater Kandidat.

---

## 3. Beweiskern

### 3.1 FREE-Graph und Komponenten

A1/A7/A8 liefern den vollständigen physischen FREE-Offdiagonalgraphen mit den
neun Maps

\[
\tau_{\pm a},\quad
\tau_{\pm T},\quad
r_a,\ r_T,\ r_{3a},\ r_{4a},\ r_{2b}.
\]

Der unabhängige Rohwort-Crosscheck

\[
\texttt{scripts/certify\_sw1\_m1\_nd\_img4\_gateA\_direct\_words.py}
\]

wertet die elf ursprünglichen Vier-Echo-Wörter direkt aus und beweist:

- genau diese neun nichtidentischen Maps;
- keine zehnte Map;
- exakt die A7.1–A7.9-Domänen;
- vollständige fünfarmige R6/R7-Supports;
- kanonische A1-Aggregatkoeffizienten.

Run \`33466183465\`: SUCCESS.

Bei \(\varepsilon_0=\Delta/4\) trifft jeder reguläre Phasenpunkt innerhalb
\(\pm14\) Rotationsschritten einen A8-Separator. Daraus folgt a.e. ein
65-Layer-Bound, also höchstens 390 formale Zustände. A8.10B verdoppelt auf
höchstens

\[
\boxed{780}
\]

physische Zustände a.e.

### 3.2 Mass Transport

Sei \(U_R\) die Vereinigung der sechs KNF-Samplinghalbfenster und

\[
V_R=\operatorname{Sat}_{\mathcal E}(U_R)
\]

ihre Sättigung unter der vollständigen A7/A8-Äquivalenzrelation.

Die neun Generatoren sind partielle maßtreue Borel-Isomorphismen.
Das Certificate

\[
\texttt{scripts/certify\_sw1\_m1\_nd\_img4\_gateB\_pmp\_graphing.py}
\]

prüft inverse Domänen, Involutionsdomänen und Jacobi-Betrag \(1\).
Run \`33466259101\`: SUCCESS.

Die Flip-Invarianz des Zählmaßes auf

\[
A_U=\mathcal E\cap(X\times U_R)
\]

liefert

\[
\int_X\#([x]_{\mathcal E}\cap U_R)\,dx
=
\int_{U_R}\#[y]_{\mathcal E}\,dy.
\]

Mit dem a.e.-780-Bound:

\[
|V_R|
\le780|U_R|
=
4680R.
\tag{P.4}
\]

### 3.3 Reducing Subspace

Auf dem physischen Horizon sei

\[
M_{V_R}h=1_{V_R}h.
\]

Da \(V_R\) vollständig \(\mathcal E\)-gesättigt ist,

\[
1_{V_R}(x)=1_{V_R}(\phi(x))
\]

auf jeder aktiven FREE-Kante \((x,\phi(x))\). Somit kommutiert
\(M_{V_R}\) mit jedem nichtdiagonalen A1-Pullback und mit allen
Diagonalmultiplikatoren:

\[
M_{V_R}(I+A)=(I+A)M_{V_R}.
\]

Mit der unitären IMG3-Identifikation

\[
V:\mathscr B_H^0\to\mathscr H_+,
\qquad
\mathscr T_B=V^*(I+A)V,
\]

definiere

\[
\Pi_{V_R}:=V^*M_{V_R}V.
\]

Dann

\[
\Pi_{V_R}\mathscr T_B
=
\mathscr T_B\Pi_{V_R}.
\]

Da \(I+A\ge I\),

\[
\mathscr T_B\ge I
\]

und daher

\[
\boxed{
\Pi_{V_R}\mathscr T_B^{-1}
=
\mathscr T_B^{-1}\Pi_{V_R}.
}
\tag{P.5}
\]

Kein \(J_R\) wird hier eingeführt.

### 3.4 Hub-Blindset

Für den Annulusbasisraum existiert der unitäre Transport

\[
W:\mathscr B_W\to\mathscr H_-^{\rm ann}
\]

und der effektive Hubblock ist exakt

\[
\mathcal H_R=V^*H W,
\qquad
H=HE_{\mathcal A}.
\]

Die sechs positiven Hub-Source-Maps sind

\[
|x-a|,\ x+a,\ |x-b|,\ x+b,\ |x-T|,\ x+T.
\]

Sie vergrößern Lebesguemaß nicht. Also

\[
|W_R^{\rm vis}|
\le6|V_R|
\le28080R.
\tag{P.6}
\]

Am Witnesspunkt gilt exakt

\[
28080R_0<S_0-R_0,
\qquad S_0=T+\sigma_0.
\]

Das Certificate

\[
\texttt{scripts/certify\_sw1\_m1\_nd\_img4\_gateD\_domain\_support.py}
\]

prüft zusätzlich die KNF-Fenster, die Annulus-Liftabdeckung, die Hub-Steigungen
und die strikte Blindmaßmarge.
Run \`33467546123\`: SUCCESS.

Damit besitzt der positive Annulus ein Blindset \(B_0\) positiven Maßes.

Wähle

\[
0\ne w_+\in L^2(B_0)
\]

und über IMG0 den zugehörigen

\[
0\ne g\in\mathscr B_W.
\]

Dann

\[
\Pi_{V_{R_0}}\mathcal H_{R_0}g=0.
\]

Setze

\[
f=-\mathscr T_B^{-1}\mathcal H_{R_0}g.
\]

Mit P.5:

\[
\Pi_{V_{R_0}}f=0.
\]

Also verschwindet die physische Horizonrekonstruktion von \(f\) auf
\(V_{R_0}\), insbesondere auf den sechs KNF-Samplinghalbfenstern
\(U_{R_0}\). Da \(\mathscr B_K\) exakt durch die KNF-Row charakterisiert ist,

\[
f\in\mathscr B_K.
\]

Schließlich

\[
\mathscr N_{R_0}(f,g)
=
\mathscr T_Bf+\mathcal H_{R_0}g
=
0.
\]

Wegen \(g\ne0\) ist das Kernelpaar nichttrivial. Das beweist P.2.

---

## 4. Drei letzte adversariale Restpunkte

Die vor der Promotion verbliebenen Modellrat-Einwände werden wie folgt
geschlossen.

### 4.1 Mittelpunkt-Auswertung ist zellvollständig

Der direkte Gate-A-Crosscheck evaluiert jede offene R0–R7-Zelle an einem
Mittelpunkt. Dies ist vollständig, weil das ursprüngliche A1-Certificate
\`scripts/certify_sw1_a1_raw_archetypes.py\` **alle** positiven inneren
Gate- und Source-Wände direkt aus den elf Rohwörtern rekonstruiert.

Es erhält in beiden \(\varepsilon\)-Chambers exakt

\[
\boxed{
\{\varepsilon,\ a-\varepsilon,\ a+\varepsilon,\ 2d-\varepsilon,\ T-\varepsilon\}.
}
\tag{P.7}
\]

Das sind genau die R0–R7-Zellgrenzen. Jede Gatebedingung ist das Vorzeichen
einer affinen Funktion von \(x\); innerhalb eines offenen Intervalls ohne
Nullstelle ist ihr Vorzeichen konstant. Daher repräsentiert die Mittelpunkt-
Auswertung die gesamte offene Zelle.

### 4.2 Sättigung der Exceptional-Nullmenge bleibt null

Sei \(N\) die Vereinigung aus

- A1/A7-Zellendpunkten,
- Separator-Endpunkt-/Midpoint-Orbits,
- globalen Sheet-Kollisionsphasen.

Diese Menge ist null; im vorliegenden expliziten Modell sogar abzählbar.

Die Äquivalenzrelation \(\mathcal E\) wird durch endlich viele partielle
maßtreue Borel-Isomorphismen erzeugt. Die Menge aller endlichen Generatorwörter
ist abzählbar. Daher

\[
\operatorname{Sat}_{\mathcal E}(N)
=
\bigcup_{w}
w\bigl(N\cap\operatorname{dom}w\bigr).
\]

Jeder Summand ist wieder eine Nullmenge, also

\[
\boxed{
\mu(\operatorname{Sat}_{\mathcal E}(N))=0.
}
\tag{P.8}
\]

Es entsteht durch die außergewöhnlichen Klassen keine versteckte positive
Maßmasse.

### 4.3 Klasseninvarianz und Komponentenbound sind logisch getrennt

Die Reducing-Subspace-Identität benutzt ausschließlich

\[
V_R=\operatorname{Sat}_{\mathcal E}(U_R).
\]

Daraus folgt definitionsgemäß die Klasseninvarianz

\[
1_{V_R}(x)=1_{V_R}(\phi(x))
\]

auf jeder Graphkante, unabhängig davon, ob die betreffende Klasse endlich,
außergewöhnlich oder groß ist.

Der Bound

\[
\#[x]_{\mathcal E}\le780
\quad\text{a.e.}
\]

wird **nur** in der Mass-Transport-Abschätzung P.4 verwendet.

Damit wird aus einem a.e.-Komponentenbound keine punktweise
Operatorinvarianz abgeleitet.

---

## 5. Review- und Governance-Buchung

Die Beweiskette wurde mehrfach adversarial intern und cross-model geprüft.

Vor Promotion lag das externe Review-Packet vor:

\[
\texttt{audits/P11\_R32\_SW1\_M1\_ND\_IMG4\_EXTERNAL\_REVIEW\_PACKET.md}.
\]

Der anschließend berichtete Modellvergleich ergab:

- Gate A materiell GREEN;
- pmp-Prämisse von Gate B konsensuell GREEN;
- Gate C algebraisch unbestritten, Dissens ausschließlich über die
  Nullmengen-/a.e.-Naht;
- Gate D abhängig von C;
- ein Modell vollständiges GREEN A–D;
- ein Modell PARTIAL genau wegen der in §4.2–4.3 nun explizit geschlossenen
  Nullmengennaht;
- ein Modell enthielt sich aus Governance-/Unabhängigkeitsgründen, ohne einen
  mathematischen Gegenfehler zu identifizieren.

Eine echte strukturell unabhängige Drittinstanz ist nicht verfügbar. Auf
explizite Entscheidung des Projektinhabers vom 1. September 2026 wird die
zusätzliche externe-Unabhängigkeitsbedingung für **diese interne
Objekt-X-Promotion** gewavet.

Daher wird **nicht** gebucht:

\[
\text{independent GREEN (external)}.
\]

Gebucht wird ausschließlich der interne mathematische Status

\[
\boxed{
\checkmark[M]_{\rm neg}.
}
\]

---

## 6. Kanonische Provenienz

Kernquellen:

- \`audits/P11_R32_SW1_M1_ND_IMG4_SMALLR_KERNEL_NOGO_CANDIDATE.md\`
- \`audits/P11_R32_SW1_M1_ND_IMG4_ANALYTIC_GATES_CANDIDATE.md\`
- \`audits/P11_R32_SW1_M1_ND_IMG4_EXTERNAL_REVIEW_PACKET.md\`
- \`audits/P11_R32_SW1_M1_ND_IMAGE_SPACE_CANDIDATE.md\`
- \`audits/P11_R32_SW1_A1_FINITE_CELL_RAW_OPERATOR_CANDIDATE.md\`
- \`audits/P11_R32_SW1_A7_FINITE_STATE_COCYCLE_CANDIDATE.md\`
- \`audits/P11_R32_SW1_A8_LOWER_FINITE_COMPONENTS_CANDIDATE.md\`

Mechanische Gegenchecks:

- \`scripts/certify_sw1_m1_nd_img4_smallR_separator_visibility.py\`
- \`scripts/certify_sw1_m1_nd_img4_gateA_direct_words.py\`
- \`scripts/certify_sw1_m1_nd_img4_gateB_pmp_graphing.py\`
- \`scripts/certify_sw1_m1_nd_img4_gateD_domain_support.py\`
- \`scripts/certify_sw1_m1_nd_img4_gate1_gate9_graph_p12.py\`

Promotionsbasis:

- geprüfter Pre-Promotion-Head:
  \`ad0a59a4c086f207ff3bdd9e31cebdafdfe646ec\`;
- vollständiger Provenienzlauf:
  \`33467557472\` — SUCCESS.

---

## 7. Konsequenz für die aktive Front

Die bisherige universelle Zielaussage

\[
\ker\mathscr N_R=\{0\}
\quad\text{auf dem gesamten SW1-Wedge}
\]

ist negativ entschieden.

Der nächste mathematische Frontknoten ist daher **nicht** mehr der Beweis
universeller M1-ND-Injektivität, sondern:

1. Klassifikation des nichtdegeneraten Restbereichs, falls vorhanden;
2. Bestimmung eines maximalen Parameterwedge mit möglicher Cross-Gram-
   Nichtentartung;
3. oder architektonische Änderung des finite-level Couplings, welche den
   Small-\(R\)-Blindraum beseitigt.

Die allgemeine Lower-Chamber-Small-\(R\)-Familienaussage bleibt bis zu einer
separaten Promotion Kandidat.

---

## 8. Firewall

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SMALLR}:
\checkmark[M]_{\rm neg}
}
\]

bedeutet ausschließlich:

> Die aktuelle effektive M1-ND-Geometrie besitzt am expliziten SW1-
> Small-\(R\)-Witness einen nichttrivialen zulässigen Kernelvektor.

Kein RH-Schluss. Keine Aussage über alle Parameter. Keine Aussage, dass
Objekt X als Gesamtprogramm gescheitert ist.
