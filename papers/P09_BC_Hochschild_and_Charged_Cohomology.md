# P09 — Bost–Connes, Hochschild and Charged Cohomology

**Status:** SYN CANDIDATE — PASS A SEALED  
**Datum:** 9. August 2026  
**Pass-A-Basis:** `audits/AUDIT-2026-08-09_P09_PassA_FINAL_SEAL.md`  
**Scope:** BC-/Hochschild-Strang `06-hochschild-bc-algebra/`, NEU-174–219 + NEU-222 als reiner Superseding-Scan  

> Dieses SYN-Paper enthält ausschließlich den am 9. August 2026 reconciliierten Endstand. Historische Zwischenbehauptungen werden nicht als aktive Resultate übernommen. Insbesondere sind `D_g(e(r))=0`, die starke NEU-212-Regularisierung und `t\Phi_0=g^{-\beta}\Phi_0` für den kanonischen Basislift `SUPERSEDED`.

---

## Abstract

P09 konsolidiert den Bost–Connes-/Hochschild-Strang des Objekt-X-Programms. Der algebraische Grundblock besitzt eine nichttriviale **neutrale** Hochschild-4-Klasse; eine geladene Selbstkoeffizientenklasse folgt daraus nicht. Der entscheidende geladene Fortschritt entsteht stattdessen über eine singuläre faktoriale Potentialroute. Sie liefert für jeden nichtneutralen Grad `g` eine korrigierte äußere Derivation

\[
[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},A_{C^*})_g,
\]

die nicht algebraisch wertig ist. Ein logarithmischer Koeffiziententyp `B^log/A^log` und der globale Bimodul `M_glob^log` reparieren die Zieltypfrage ohne einen nachträglichen Bimodul-Glätter. Über einen Grad-3-Partner entsteht anschließend der nichttriviale geladene Cup

\[
\boxed{
[D_g^{\rm corr}]\smile[\Theta^\wedge]
\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

Die weitere zyklische Verfeinerung ist jedoch nicht automatisch möglich. Eine gradneutralisierte KMS-Auswertung liefert für `beta>1` einen nichtverschwindenden getwisteten Hochschildkozykel, aber der Standard-Zyklisierungsschritt annihiliert den nichttrivialen Gewichtssektor. Im adelischen Dilatationsmodell existiert ein kanonischer Basislift `L~_0`, doch ein expliziter Unit-Slot-Zeuge beweist stärker

\[
\boxed{t\Phi_0\neq C\Phi_0\qquad\forall C\in\mathbb C.}
\]

Damit besitzt der kanonische skalare Lift keine globale konstante Rotationseigenrelation. P09 konstruiert weder einen zyklischen Ersatzrepräsentanten noch eine Weil-/Gamma-, Gram-, Hilbert–Pólya- oder Objekt-X-Endstruktur und enthält keinen RH-Beweis.

---

## §1 — Bindende Typ- und Statusfirewalls

### 1.1 Algebraischer Kern und Koeffizienten

`A_alg` bezeichnet den algebraischen Bost–Connes-Kern. Drei Koeffiziententypen sind strikt zu unterscheiden:

\[
A_{\rm alg}
\subset A_{C^*},
\qquad
\mathcal A^{\log}\subset A_{C^*},
\qquad
\mathfrak M_{\rm glob}^{\log}\subset\mathcal A^{\log}.
\]

Aus einer nichttrivialen Klasse mit Koeffizienten in `A_{C^*}` oder `M_glob^log` folgt **keine** nichttriviale Selbstkoeffizientenklasse in `HH^*(A_alg,A_alg)`.

### 1.2 Korrigierte geladene Derivation

Historische Formeln mit

\[
D_g(e(r))=0
\]

sind `SUPERSEDED`. Bindend ist

\[
\boxed{
D_g^{\rm corr}(e(r))
=
\mu_m C_{m,n;r}\mu_n^*,
\qquad g=m/n.
}
\]

Die Grenzdefinition entsteht als **punktweiser Normgrenzwert auf jedem festen** `a in A_alg`; eine gleichmäßige Konvergenz in Derivationsoperatornorm wird nicht behauptet.

### 1.3 Faktoriale Absorption

Die historische starke Behauptung

\[
M X_N\to0
\]

ist `×[M]`. Korrekt ist die stärkere strukturelle Präzisierung in anderer Richtung:

\[
\boxed{M(0)=0\Longrightarrow MX_N\text{ ist für }N\gg1\text{ exakt konstant}.}
\]

### 1.4 Hochschild ist nicht zyklisch

Ein nichttrivialer Hochschild-Cup in Grad 4 liefert weder automatisch eine gewöhnliche zyklische Klasse noch eine getwistete, KMS- oder Hopf-zyklische Klasse. Diese Übergänge werden in P09 separat auditiert.

---

## §2 — Algebraischer BC/Hochschild-Grundblock

### Satz 2.1 — Neutraler algebraischer HH4-Befund

Der neutrale Grundblock liefert eine nichttriviale algebraische Hochschild-4-Klasse

\[
\boxed{[\Omega_p]\neq0\in HH^4(A_{\rm alg},A_{\rm alg})_1.}
\]

Der verwendete Alternierungsnachweis ist unnormalisiert; die ausgezeichnete Paarung besitzt entsprechend den Faktor `4!=24`.

### Firewall 2.2 — Kein geladener Selbstkoeffiziententransfer

Aus Satz 2.1 folgt nicht

\[
HH^4(A_{\rm alg},A_{\rm alg})_g\neq0
\qquad(g\neq1).
\]

Die frühen geladenen Polynom-/Produktmodelle sind Modellkonstruktionen oder werden durch spätere Alternierungs- und Kozykeltests begrenzt.

### Satz 2.3 — Alternierungs-No-go für die frühe symmetrische Schablone

Der geladene Dualzyklus sieht nur den vollständig alternierenden Anteil `Alt_4 L`. Die frühe symmetrische Produktschablone besitzt

\[
\operatorname{Alt}_4L=0
\]

und ist für diesen Zeugen unsichtbar. Ein determinantischer Modellkandidat kann zwar mit Wert `24` paaren, scheitert aber am Hochschildrand. Dies ist ein struktureller Kandidaten-No-go, kein globaler No-go für geladene `HH^4`.

---

## §3 — Singuläre Potentialroute und geladene äußere HH1-Klasse

### Satz 3.1 — Charakterkern und Ursprungssingularität

Für jeden nichtneutralen reduzierten Grad `g=m/n` gilt

\[
\boxed{Z_g=\{0\}.}
\]

Die faktoriale Kette

\[
L_j=(j+1)!,
\qquad
P_j=1_{L_j\widehat{\mathbb Z}}
\]

liefert ein singuläres Profil mit

\[
\operatorname{Sing}(X)=\{0\}.
\]

Der frühere No-go gegen **exakt** unter allen Primtransporten geschlossene totale Teilbarkeitsketten widerspricht dieser Konstruktion nicht: Die faktoriale Route arbeitet mit einem normkontrollierten Transportband, nicht mit exakter Schließung.

### Satz 3.2 — Normkonvergente Transportdefekte

Für feste Generatoren entstehen normkonvergente Transportdefekte `G_{a,d}`. Der korrekte August-Endstand umfasst sowohl die nichtteilerfremden gcd-/Nica-Fälle als auch den Charakterterm der geladenen Derivation.

### Satz 3.3 — Geladene analytische Nichtinnerheit

Für `g!=1` gilt

\[
\boxed{
[D_g^{\rm corr}]
eq0
\in HH^1(A_{\rm alg},A_{C^*})_g.
}
\]

Die Nichtinnerheit wird durch einen Offdiagonaltest gegen beschränkte Implementierer nachgewiesen.

### Firewall 3.4 — Kein algebraischer Zieltyp

Die konkrete faktoriale Derivation landet im Allgemeinen nicht in `A_alg`. Daher bleibt

\[
HH^1(A_{\rm alg},A_{\rm alg})_g\neq0
\]

für diesen Kandidaten offen.

### No-go 3.5 — Reguläre Potentiale und nachträgliche Glättung

Normkonvergente Potentialimplementierer liefern nur innere bzw. im relevanten Quotienten unsichtbare Derivationen. Außerdem gilt ein Bimodul-Rigiditäts-No-go: Ein globaler normstetiger `A_alg`-Bimoduloperator

\[
R:A_{C^*}\to\mathcal A^\infty\subsetneq A_{C^*}
\]

kann nicht als nichttrivialer universeller Glätter die Zieltypfrage lösen.

---

## §4 — Logarithmischer Koeffiziententyp und geladener HH4-Cup

### Satz 4.1 — Logarithmische Banach-*-Algebra

Die kanonische Reparatur des gescheiterten Schwartz-Zieltyps ist die direkte Konstruktion

\[
\boxed{
\mathcal B_{\rm alg}\subsetneq\mathcal B^{\log}\subsetneq C(\widehat{\mathbb Z}),
}
\]

mit stabilen Operationen `sigma_k`, `rho_k`, `T_a` und

\[
G_{a,d}\in\mathcal B^{\log}.
\]

Daraus entsteht die graduierte algebraische `*`-Algebra `A^log`.

### Satz 4.2 — Zieltypbrücke

Die korrigierte Derivation erfüllt

\[
\boxed{
D_g^{\rm corr}(A_{\rm alg})\subseteq\mathcal A^{\log},
\qquad
[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},\mathcal A^{\log})_g.
}
\]

### Satz 4.3 — Globaler Koeffizientenbimodul

Der globale logarithmische Bimodul `M_glob^log` ist unter der `A_alg`-Bimodulstruktur und den benötigten Transporten stabil. Damit

\[
\boxed{
[D_g^{\rm corr}]\neq0
\in HH^1(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

Lokale stärkere Behauptungen mit `M_{g,p}^log` werden nicht migriert, solange die volle lokale Bimodultypisierung fehlt.

### Satz 4.4 — Nichttrivialer geladener Cup

Für drei geeignete Primrichtungen besitzt der Grad-3-Partner `Theta^wedge` einen typkorrekten Cup mit der geladenen Derivation. Der Mehrparameter-Følner-Nachweis konstruiert einen partiellen Modulquotienten, einen Dualzeugen und eine nichtverschwindende Paarung. Daraus folgt

\[
\boxed{
[D_g^{\rm corr}]\smile[\Theta^\wedge]
\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

### Firewall 4.5 — Partieller Quotient genügt

Der Beweis benötigt **nicht** den vollen Quotienten

\[
\mathfrak M_{\rm glob}^{\log}/[A_{\rm alg},\mathfrak M_{\rm glob}^{\log}].
\]

Dessen Struktur bleibt offen. Ebenso folgt aus Satz 4.4 keine Klasse in `HH^4(A_alg,A_alg)_g`.

---

## §5 — KMS-Neutralisierung und getwisteter Hochschildkozykel

### Satz 5.1 — Direkter geladener KMS-Detektor verschwindet

Für ein homogenes nichtneutrales Zielelement `eta` erzwingt die KMS-Gleichung

\[
\boxed{\omega_\beta(\eta)=0\qquad(\beta>0).}
\]

Ein KMS-Zustand ist keine gewöhnliche Spur und annihiliert im Allgemeinen nicht den gewöhnlichen Modulkommutatorraum `[A,M]`.

### Satz 5.2 — Explizite Gradneutralisierung

Ein Gegenfaktor vom inversen Gesamtgrad neutralisiert die KMS-Gewichtsauslöschung. Für `beta>1` reduziert die ausgezeichnete Auswertung auf

\[
\omega_{\beta,\chi}(\sigma_P(G_q)),
\]

und es gilt für alle extremalen Gibbs-Zustände im bewiesenen Bereich

\[
\boxed{\omega_{\beta,\chi}(\sigma_P(G_q))>0.}
\]

Der kritische Fall `beta=1` wird durch diese Gibbs-Rechnung nicht entschieden.

### Satz 5.3 — Korrekte Twistkonvention

Für die Standard-Letztrandkonvention ist

\[
\boxed{
\sigma_\beta=\alpha_{-i\beta}=\theta_\beta^{-1}.
}
\]

Mit dieser Orientierung und `bL=0` folgt

\[
\boxed{
b^{\sigma_\beta}\Phi_{\beta,\chi}=0,
\qquad
0\neq\Phi_{\beta,\chi}
\in Z^4_{\sigma_\beta,\mathrm{Hoch}}(A_{\rm alg}).
}
\]

### Satz 5.4 — Ladungsobstruktion des konkreten I4-Repräsentanten

Für diese rohe KMS-Kochain gilt

\[
\boxed{
T_{\sigma_\beta}\Phi_{\beta,\chi}
=g^{-\beta}\Phi_{\beta,\chi}.
}
\]

Für `g!=1`, `beta>0` liegt sie damit in einem nichttrivialen `T`-Eigenraum und ist kein standardmäßiger getwisteter zyklischer Kozykel.

**Präzedenz-Firewall:** Diese Aussage betrifft `Phi_{beta,chi}` aus I4. Sie ist nicht mit dem späteren kanonischen Basislift `Phi_0` zu identifizieren.

---

## §6 — Parazyklische und Hopf-SAYD-No-gos

### Satz 6.1 — Gewichtssektor

Der Eigenraum

\[
C^\bullet_{\sigma,w}(A),
\qquad
T\varphi=w\varphi,
\]

ist ein `b^sigma`-Unterkomplex. Für `w!=1` wird dieser Sektor jedoch bei der gewöhnlichen Invarianten-/Koinvarianten-Zyklisierung annihiliert, da `1-T` dort invertierbar ist.

### Satz 6.2 — Externe Eigenlinie ist keine zyklische Koeffiziententheorie

Eine externe eindimensionale Eigenlinie kann den `T`-Eigenwert formal kompensieren, definiert aber weder die benötigten Koflächen, Kodegenerationen noch einen zyklischen Rotationsoperator.

### Satz 6.3 — Kein eindimensionales unitales äquivariantes A-Bimodul

Es existiert für `beta>0` kein eindimensionales unital-nichtdegeneriertes `sigma_beta`-äquivariantes `A_alg`-Bimodul, das den gewünschten modularen Reparaturtyp liefert.

### Satz 6.4 — Standard-SAYD-Kollision

Die `Q_+^x`-Gradierung liefert kanonisch eine **Koaktion**, nicht bereits eine kanonische Aktion der Gruppenalgebra. Der reparierte minimale Hopf-Typ

\[
\mathcal H_\beta=\mathbb C[\mathbb Z]
\]

wirkt durch `sigma_beta`. Im Standard-SAYD-Setup kollidieren jedoch exakter KMS-Twist, Ladungskompensation und Stabilität. Damit repariert der Standard-SAYD-Pfad die Ladungsobstruktion nicht.

Ein nichtstandardmäßiger `A`-relativer Hopf-Koeffizient bleibt offen.

---

## §7 — Adelische Dilatation, Morita-Ecke und Orbitmarkierung

### Satz 7.1 — Laca-Dilatation

Die nichtunitalen BC-Endomorphismen besitzen die adelische automorphe Dilatation

\[
\widetilde B=C_0(\mathbb A_f),
\qquad
(\gamma_rF)(a)=F(r^{-1}a),
\]

mit Crossed Product

\[
\widetilde A=C_0(\mathbb A_f)\rtimes_\gamma\mathbb Q_+^\times.
\]

Für `e=1_{\widehat Z}` gilt die Full-Corner-Realisierung des BC-Systems.

### Satz 7.2 — Exakte algebraische Ecke

Für den gewählten algebraischen Kern gilt nicht nur C*-Morita-Äquivalenz, sondern die explizit nachgerechnete Gleichheit

\[
\boxed{e\widetilde A_{\rm alg}e=j_A(A_{\rm alg}).}
\]

Der algebraische Eckprojektor ist voll; der Kern besitzt lokale Einheiten.

### Satz 7.3 — Orbitkollaps

Die unmarkierten gesättigten Orbitmodule sind nicht verschieden:

\[
\boxed{N_k=N_0\qquad\forall k\in\mathbb Z.}
\]

Daher ist die globale unmarkierte Multiplikationsabbildung der algebraischen Orbitsumme nicht injektiv. Die Orbitinformation muss extern markiert werden:

\[
\mathcal N_{\rm tag}
=
\bigoplus_{k\in\mathbb Z}^{\rm alg}N_0\delta_k.
\]

### Satz 7.4 — Markiertes Modulgewicht

Auf `N_tag` existiert eine typkorrekte Eigenfamilie `Omega_lambda`. Die Multiplikation mit `U_{g^{-1}}` erhält den Orbitindex; sie ist **nicht** der externe Shift `T^{-1}`.

---

## §8 — Kanonischer Basislift und endgültiger Rotations-No-go

### Satz 8.1 — Kanonischer Basislift

Der kanonische Ecklift wird erstmals explizit definiert durch

\[
\boxed{
\widetilde L_0
=
\eta_0\circ j_M\circ L^{\rm cup}
:
A_{\rm alg}^{\otimes4}\to I_0.
}
\]

Er ist ein Hochschildkozykel:

\[
\boxed{\widetilde L_0\in Z^4(A_{\rm alg},I_0).}
\]

Die Recovery-Identität ist typkorrekt als Inklusion

\[
\Pi_0\circ\eta_0
=
\iota_{M_0\hookrightarrow N_0}
\]

zu lesen; nach Eckkompression erhält man `id_{M_0}`.

### Satz 8.2 — Grad und Orbitindex sind verschieden

Der Lift trägt weiterhin den BC-Grad `g`, lebt aber vollständig im Orbit-Nullsummanden:

\[
\boxed{\kappa=0,\qquad\varepsilon=0.}
\]

Damit ist jedes Orbitgewicht `lambda` auf dem kanonischen Lift wirkungslos.

### Rollback 8.3 — Kein globaler Exponent `s`

Die historischen Zwischenbehauptungen

\[
t\Phi_0=g^{-\beta}\Phi_0,
\qquad
s=-1
\]

sind `SUPERSEDED`. KMS, Twistkommutation und Gradinformation allein liefern keine Rotation von

\[
L(a_0,a_1,a_2,a_3)
\quad\text{zu}\quad
L(a_1,a_2,a_3,a_4).
\]

### Satz 8.4 — Unit-Slot-No-go

Die explizite Cup-Form besitzt unterschiedliche Determinanten- und Derivationsslots auf den beiden Rotationsseiten. Für

\[
(a_0,a_1,a_2,a_3,a_4)
=
(\mu_P^*,\mu_{p_1},\mu_{p_2},\mu_{p_3},1)
\]

gilt

\[
\Phi_0(a_0,\ldots,a_4)=0,
\]

während

\[
(t\Phi_0)(a_0,\ldots,a_4)
=
-\left(\prod_{i=1}^3\log p_i\right)
 n^{-\beta}\omega_{\beta,\chi}(G_P)
\neq0
\]

für `beta>1` und die zulässigen extremalen KMS-Zustände.

Daher

\[
\boxed{
t\Phi_0\neq C\Phi_0
\qquad\forall C\in\mathbb C.
}
\]

Dies ist der autoritative kanonische Rotations-No-go.

### Firewall 8.5 — Was dadurch nicht ausgeschlossen ist

Der Unit-Slot-Zeuge schließt **nicht** aus:

1. einen anderen zyklischen oder getwistet-zyklischen Repräsentanten derselben Hochschildklasse;
2. einen genuin orbitverschiebenden nichtkanonischen Lift;
3. eine andere Koeffizientenkategorie;
4. eine archimedische/Weil-/Gamma-Korrektur.

Diese Möglichkeiten werden außerhalb des kanonischen Basislifts weitergeführt.

---

## §9 — Offene Endknoten

Nach der P09-Reconciliation bleiben insbesondere offen:

1. **Geladene Selbstkoeffizientenklasse:**
   \[
   HH^1(A_{\rm alg},A_{\rm alg})_g\neq0\quad ?
   \]
2. **Geladene HH4-Selbstkoeffizientenklasse:**
   \[
   HH^4(A_{\rm alg},A_{\rm alg})_g\neq0\quad ?
   \]
3. volle Struktur von `M/[A,M]`;
4. topologische Banach-/Fréchet-Vervollständigung des logarithmischen Zieltyps;
5. lokale Resttypisierung `[O-217-1d]`, `[O-217-2b-5]`, `[O-217-2c-5land]`;
6. KMS-Grenzfall `beta=1` in der I4-Diagonalauswertung;
7. nichtstandardmäßiger `A`-relativer Hopf-Koeffizient;
8. `[O-219-cyclic-representative]`;
9. genuin orbitverschiebender nichtkanonischer Lift;
10. `[O-219-6]` — Weil-/Gammafaktorpaarung.

---

## §10 — Routing zu den folgenden SYN-Papers

### P10 — No-Go-Sammlung

P10 kann isolierte Kandidaten-No-gos spiegeln, insbesondere verworfene konkrete Potential-, Glättungs-, Orbit- und Zyklisierungskandidaten. Struktur-No-gos, die zum Verständnis des positiven P09-Pfads notwendig sind, bleiben zugleich in P09.

### P11 — Globale Kopplung und Objekt-X-Geometrie

P09 konstruiert **keine** globale nichtorthogonale Gramkopplung, keinen Mediator zwischen Primkanälen und archimedischem Anteil und keinen Objekt-X-Hilbertraum. Diese Aufgaben gehören nach P11.

### NEU-220 / Weil-Gamma-Pfad

Der kanonische Rotations-No-go exportiert den archimedischen Reparaturbedarf nach NEU-220. Ein möglicher positiver Fortgang muss die vollständige Weilform einschließlich Gammafaktor typkorrekt mit der kohomologischen Struktur verbinden.

---

## §11 — Gesamturteil

P09 schließt einen langen Suchstrang mit einem klaren asymmetrischen Ergebnis:

\[
\boxed{
\text{geladene Hochschildstruktur: positiv bis }HH^4
}
\]

aber

\[
\boxed{
\text{kanonische skalare zyklische Rotation: negativ.}
}
\]

Der positive Kern ist keine bloße formale Konstruktion: Die geladene äußere Derivation ist nichttrivial, ihr logarithmischer Koeffiziententyp ist explizit, der Grad-4-Cup besitzt einen Nichtverschwindenszeugen, und die adelische Dilatation ist strukturell typisiert. Gleichzeitig verhindern die Koeffizienten- und Zyklizitätsfirewalls, daraus vorschnell eine zyklische Klasse, eine Weil-Identität oder einen Hilbert–Pólya-Operator abzuleiten.

\[
\boxed{
\text{P09 enthält keinen RH-Beweis und konstruiert Objekt X nicht.}
}
\]