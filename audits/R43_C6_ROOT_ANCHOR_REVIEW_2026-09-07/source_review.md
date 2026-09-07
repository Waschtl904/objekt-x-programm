# C6-Wurzelanker: destruktiver Quellen- und Beweisreview

**Prüfdatum:** 7. September 2026. **Pin:**
`55a3a1617513cc5d82c47d0cfd606c6b0894c984`.
Erster geprüfter Kandidat: `/home/user/workspace/c6_direct_noescape.md`,
insbesondere N5–N16.

**Zusätzlich vollständig geprüfter kanonischer Entwurf PA1–PA19:**
`/home/user/workspace/r43_global_budget_55a3/audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md`.
Exakter Git-Dateiblob `d6489e38e82185406eb41b9464eb72ff18dfde71`;
SHA-256 `b938c167decf1a326c7d823e5537bba8c527374ef218b55ed703324f6260e5da`;
12.770 Bytes, 343 Zeilen. Der Entwurf ist im geprüften Zustand untracked,
also **kein** Bestandteil des gepinnten Commits. Keine Repository-Änderung
durch diesen Review.

## Urteil: SCOPED GREEN

**Der neue positive Wurzelanker ist mathematisch korrekt.** Die benötigten
Quellinputs sind am Pin tatsächlich in den ursprünglichen P11-Graphnormen
mit der richtigen gemeinsamen Skala und dem scharfen Koeffizienten
vorhanden. Der Beweis erfordert weder uniforme Metriknormen noch eine
uniforme Rang-eins-Restabschätzung. Die korrekte Folgerung ist
\[
\boxed{W_{R,S}^{[U]}e_{R,0}\longrightarrow e_{S,0}}
\]
für jedes feste \(0<R<S\), auf dem ganzen reellen Terminaltail. Zusammen
mit dem bereits vorausgesetzten starken tangentialen R42-Transport schließt
dies B-FLAGTIGHT und den fixed-pair-C6/Strong-Terminal-Schritt.
Der genaue algebraische und analytische Scope wird unten nachgewiesen;
die vorhandenen Eingänge sind
[P11, Metrik/Pullback/Transport, Zeilen 665–715](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L665-L715),
[P11, scharfe Odd-Asymptotik, Zeilen 764–793](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L764-L793),
[R42, tangentialer Limes und C6-Reduktion, Zeilen 1322–1480](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1322-L1480).

**Quellenhärtung:** Im ausformulierten alten P11-Quadraturbeweis gibt es eine
nicht explizit behandelte Endpunktspur bei der Nullerweiterung von \(k_U^0\).
Das ist kein Defekt des neuen Wurzellemmas. §5 unten gibt eine explizite
Hölder-Randabschätzung, die auf der ausschließlich benötigten festen
glatten Skala alle Fehler \(o(\sqrt{M_U})\) macht und den alten scharfen
Koeffizienten erhält. Ohne diese Ergänzung sollte die dortige rohe globale
Lipschitzbehauptung nicht wörtlich wiederholt werden:
[Odd-Beweis, Zeilen 272–315](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L272-L315).

## 1. Scharfe Quellskala: kein versteckter Radiusfaktor

Setze im **ursprünglichen** festen Graphraum
\(\mathcal H_X=\mathcal K_{X,X}^-\)
\[
\lambda_U=\frac{e^U}{U^2},\qquad M_{X,U}=\lambda_U^{-1}G_{X,U}.
\]
Die gepinnte Formel (6.1) ist eine echte Äquivalenz mit **exaktem**
Vorfaktor
\[
\sigma_U(E_{X,U}f)
=c_m^2|\beta_X^{(m)}(f)|^2
\frac{e^U}{U^{2m+2}}(1+o_f(1)),
\]
nicht nur eine \(\asymp\)-Aussage. Es ist \(c_0=1\). Daher gilt für jedes
feste glatte ungerade \(f\)
\[
\langle M_{X,U}f,f\rangle\to|\beta_X^{(0)}(f)|^2.
\tag{R1}
\]
Für \(\beta_X^{(0)}(f)=0\), \(f\ne0\), liefert die Jetvollständigkeit
einen endlichen ersten \(m\ge1\), und dieselbe Formel ergibt null im Limes.
Die feste Gammaenergie verschwindet nach Division durch \(\lambda_U\).
Es gibt hier keinen \(X\)-abhängigen skalaren Faktor, der bei \(R\to S\)
übersehen worden wäre:
[P11, Zeilen 764–793](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L764-L793),
[Jetvollständigkeit, Zeilen 210–245](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Direct_Terminal_Bridge.tex#L210-L245).

**Minimaler Eingang (zusätzliche Reduktion):** Tatsächlich ist weder die
Asymptotik für \(m\ge1\) noch Jetvollständigkeit nötig. Für ein festes glattes
\(f_0\) mit \(\beta(f_0)=1\) und jedes feste glatte \(g\in\ker\beta\)
haben \(f_0,f_0+g,f_0-g\) alle nullten Jet eins. Ihre skalierten
Energien konvergieren also allein mit dem Fall \(m=0\) gegen eins.
Die exakte Parallelogrammidentität gibt
\[
E_U(g)=\tfrac12\{E_U(f_0+g)+E_U(f_0-g)\}-E_U(f_0)\to0.
\]
Damit folgt R1 aus **nur** der scharfen \(m=0\)-Aussage. Der folgende
Wurzelanker importiert daher keinerlei Vollständigkeit der höheren Jets.

Die glatte Dichte ist im **Graphraum**, nicht bloß in \(L^2\), bewiesen.
Die übliche Korrektur durch einen festen glatten Vektor mit nichtnulltem
nulltem Jet liefert auch Dichte im Hyperraum \(\ker\beta_X^{(0)}\):
[P11-DT.24, Zeilen 296–338](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Direct_Terminal_Bridge.tex#L296-L338).

## 2. Globaler Unterbau: vollständiger Rest, richtige Normierung

Die exakte Cauchy–Schwarz-Untergrenze lautet für **alle** Graphvektoren
\[
\langle G_{X,U}f,f\rangle
\ge\frac{|\ell_{X,U}(f)|^2}{d_U},
\quad
d_U=\langle1_U,(I+R_U^*R_U)1_U\rangle=2U+O(1).
\]
Sie benutzt den vollen Rest; weder die Feshbach-Resolvente noch
Cross-Power-Terme sind entfernt:
[TC1, Zeilen 76–157](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_TC1_MixedJet.tex#L76-L157),
[vollständiger Konstantenmodus, Zeilen 29–78](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L29-L78).

R27 liefert **Dualnormkonvergenz**
\[
e^{-U/2}U^{1/2}\ell_{X,U}\to-\sqrt2\,\beta_X^{(0)},
\]
nicht nur punktweise Funktionalkonvergenz. Somit
\[
\alpha_{X,U}:=-\ell_{X,U}/\sqrt{\lambda_Ud_U}
\longrightarrow\beta_X^{(0)}
\]
in der Dualnorm desselben ursprünglichen Graphraums. Das Minuszeichen ist
korrekt; \(\sqrt{\lambda_Ud_U}\sim\sqrt2e^{U/2}U^{-1/2}\):
[R27, Zeilen 128–173](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md#L128-L173).

Seien \(\nu_{X,U},\nu_X\) die zugehörigen Rieszvektoren. Dann
\[
\nu_{X,U}\to\nu_X,\qquad
M_{X,U}\ge \nu_{X,U}\nu_{X,U}^*.
\tag{R2}
\]
Das ist eine Ordnung auf dem ganzen festen Hilbertraum. Es gibt keine
unerlaubte Ersetzung des Graphadjunkts durch eine rohe Restriktion und
keine baseline-Kongruenz von Quadratwurzeln.

## 3. Unabhängige Prüfung des Wurzellemmabeweises

Sei \(D\) der dichte glatte Kern, \(\beta(f)=\langle f,\nu\rangle\),
\(\rho=\|\nu\|>0\), \(e=\nu/\rho\). Wähle \(f\in D\) mit
\(\beta(f)=1\), und setze \(x_U=M_U^{1/2}f\).

1. Aus R1 folgt \(\|x_U\|^2\to1\), also Beschränktheit.
2. Für festes \(g\in D\cap\ker\beta\) ist
   \(\|M_U^{1/2}g\|^2\to0\). Selbstadjungiertheit liefert
   \(\langle x_U,g\rangle=\langle f,M_U^{1/2}g\rangle\to0\).
3. Dichte im Hyperraum und Beschränktheit von \(x_U\) implizieren:
   jeder schwache Teilfolgengrenzwert hat die Form \(ce\), \(|c|\le1\).
4. Operator-Monotonie der positiven Quadratwurzel in R2 gibt
   \[
   M_U^{1/2}\ge
   \frac{\nu_U\nu_U^*}{\|\nu_U\|}.
   \]
   Daher
   \[
   \langle x_U,f\rangle\ge
   |\langle f,\nu_U\rangle|^2/\|\nu_U\|\to1/\rho.
   \]
5. Am schwachen Grenzwert ist die linke Seite \(c/\rho\).
   Sie ist reell; deshalb \(c\ge1\). Mit \(|c|\le1\) folgt \(c=1\).
   Eindeutiger schwacher Limes und Konvergenz der Normen liefern
   \(x_U\to e\) stark.

Der Beweis ist auch komplex korrekt bei linear-im-ersten-Argument-Konvention:
\(\langle e,f\rangle=\overline{\beta(f)}/\rho=1/\rho\).
Für allgemeines \(f\in D\) ergibt Skalierung
\[
\boxed{M_U^{1/2}f\to\beta(f)e.}
\tag{R3}
\]
Es wurde nicht vorausgesetzt, dass \(\sup_U\|M_U\|<\infty\), und die
Konvergenz wird nicht durch Dichte auf alle Eingabevektoren von
\(M_U^{1/2}\) fortgesetzt. Schwache Teilfolgen genügen, da die Graphräume
separabel sind; alternativ funktioniert das Argument für beliebige
Sequenzen \(U_n\to\infty\) und beweist damit den vollen reellen Limes.

**Kein Gegenmodell gefunden:** Der mögliche Mechanismus
„beschränkte Energien, aber Energieflucht zu hohen Indizes“ scheitert
hier genau an Schritt 4 und dessen Sättigung in Schritt 5. Ohne globalen
Rang-eins-Unterbau wäre der Schluss nicht gerechtfertigt.

## 4. Der Übergang zum wirklichen Transport ist exakt

Wähle ein einziges glattes reelles \(f_R\) mit
\(\beta_R(f_R)=1\) und \(f_S=J_{R,S}f_R\).
Nullerweiterung erhält Glattheit, kompakten Innenträger und den Jet:
[P11-DT.6, Zeilen 43–62](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Direct_Terminal_Bridge.tex#L43-L62).
Wegen **derselben** \(\lambda_U\) gelten für
\[
x_{X,U}=\lambda_U^{-1/2}G_{X,U}^{1/2}f_X
\]
die Identitäten
\[
W_Ux_{R,U}=x_{S,U},\qquad \|W_U\|=1.
\]
Damit
\[
\|W_Ue_R-e_S\|
\le\|e_R-x_{R,U}\|+\|x_{S,U}-e_S\|\to0.
\tag{R4}
\]
Diese Rechnung ist genau die Quellidentität in P11, nicht die
relative-baseline-Modulusisometrie \(Q_U\):
[P11, Zeilen 665–715](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L665-L715).

Es findet kein Grenzübergang durch \(G_{S,U}^{1/2}\) auf einem unbekannten
Fehler statt. Die beiden Wurzelanker werden zuerst durch R3 kontrolliert;
erst danach wird die normeinsbeschränkte tatsächliche Isometrie verwendet.

Die Riesznormalen mit positivem nulltem Jet sind die kanonischen
\(e_{X,0}\), nicht zusätzliche frei wählbare Normalen:
[R43, Zeilen 41–99](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L41-L99).
Somit folgt
\[
\sup_{m\ge1}\|P_S^{[m]}W_Ue_{R,0}\|
\le\|W_Ue_{R,0}-e_{S,0}\|\to0.
\]
Das ist sogar stärker als B-FLAGTIGHTs iterierter Limes.
R42s vorhandener starker tangentialer Limes ergänzt den Normalenlimes
zum starken Limes auf dem gesamten festen **ungeraden** Graphraum:
[R42, Zeilen 1322–1366 und 1427–1480](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1322-L1480).

## 5. Härtung des alten scharfen Full-rest-Oberbeweises

Der relevante Quellenbeweis extrahiert
\[
h_U=h_U^{\rm grow}+h_U^{\rm rem},\quad
K_U=\langle h_U^{\rm grow},1_U\rangle,\quad
M_U^{\rm cost}=|K_U|^2/(2U),
\]
mit \(\|h_U^{\rm rem}\|=O_f(1)\) und
\(M_U^{\rm cost}\sim c_m^2|\beta^{(m)}(f)|^2e^U/U^{2m+2}\).
Die signed-edge-Zertifikate und ihre tatsächliche Full-rest-Hebung liefern
dann die scharfe obere Schranke mit Koeffizient eins:
[Odd-Beweis, Zeilen 94–229 und 317–387](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L94-L387).

**Der engste rohe Textpunkt:** \(k_U^0=k_U-K_U/U\) hat im Allgemeinen
nichtverschwindende Randwerte bei \(0,U\). Die Nullerweiterung hat deshalb
Sprünge. In
\[
\Phi_U(r)(v)=2k_U^0(v)\alpha(2r-v)
-2k_U^0(2r-v)\alpha(v)
\]
ist die bewegte zweite Randkante dann nicht ohne Weiteres \(L^2\)-Lipschitz
in \(r\); die formale Ableitung im Paper lässt diese Spuren ungeschrieben.
Insbesondere darf man die dortige „konstante Ableitung null“-Aussage nicht
auf die nullerweiterte Konstante an den Endpunkten anwenden:
[Odd-Beweis, Zeilen 279–315](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L279-L315),
[R1-Reconciliation, Zeilen 40–74](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R1_RECONCILIATION_2026-08-13.md#L40-L74).

**Explizite Reparatur ohne jede Änderung des Zertifikats.**
Setze
\[
A_U:=C_f\left(e^{U/2}/\sqrt U+|K_U|/U\right).
\]
Die Quellschranke (6.10) impliziert
\(\|k_U^0\|_\infty+\|(k_U^0)'\|_\infty\le A_U\) auf \((0,U)\).
Für die tatsächliche Nullerweiterung \(\widetilde k_U^0\) gelten beim
Verschieben um \(2h\) zwei elementare Fälle:

1. Außerhalb der beiden überquerten Randintervalle gilt der gewöhnliche
   Mittelwertsatz mit Fehler höchstens \(2A_U|h|\).
2. Die überquerten Randintervalle haben Gesamtlänge höchstens \(4|h|\);
   dort beträgt der Fehler höchstens \(2A_U\).

Da \(\alpha(v)\) einen festen kompakten Träger hat, folgt für \(|h|\le1\)
direkt
\[
\|\alpha(v)\{
\widetilde k_U^0(2r+2h-v)-\widetilde k_U^0(2r-v)\}\|_{L^2_v}
\le C_\alpha A_U\sqrt{|h|}.
\]
Der andere Teil
\(k_U^0(v)[\alpha(2r+2h-v)-\alpha(2r-v)]\)
hat Norm höchstens \(C_\alpha A_U|h|\).
Somit erfüllt der **unveränderte** echte Source-Representer global
\[
\boxed{\|\Phi_U(r+h)-\Phi_U(r)\|_2
\le C_\alpha A_U\sqrt{|h|}.}
\tag{R5}
\]
Diese Hölder-\(1/2\)-Schranke schließt beide bewegten Randspuren ein.

Für die unveränderten positiven massennormierten
\(\lambda_q^{(I)}\), deren Summe exakt \(|I|\) ist, folgt unmittelbar
\[
\left\|\sum_{q:r_q\in I}\lambda_q^{(I)}\Phi_U(r_q)
-\int_I\Phi_U(r)\,dr\right\|_2
\le C_\alpha A_U|I|^{3/2}.
\]
Die echten Zellen überdecken \(O(U)\) gesamte \(r\)-Länge und erfüllen
\(\max_I|I|\le C e^{-2U/5}\). Deshalb
\[
\boxed{\|Z_U^{\rm quad}\|_2
\le C_\alpha U A_U e^{-U/5}
=o_f(\sqrt{M_U^{\rm cost}}).}
\tag{R6}
\]
Im benötigten Fall \(m=0\) ist der Quotient durch
\(C_fU^{3/2}e^{-U/5}\) beschränkt; auch jedes feste endliche \(m\)
wäre zulässig. Es wird **keine** absolute exponentielle Kleinheit des
Fehlers behauptet, nur die erforderliche relative Kleinheit.
Die Massenkostenidentität und die diskrete Zertifikatskostenabschätzung
bleiben unverändert, weil das Zertifikat selbst überhaupt nicht geändert
wurde:
[Odd-Beweis, Zeilen 218–270 und 301–310](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L218-L310).

Alle benutzten zukünftigen Primzahlen erfüllen weiterhin
\(\tfrac12\log q\ge U/2-O(1)\); die echte \(a=0\)-Hebung mit
higher-power-Fehlernorm
\(O(\sqrt{U+1}e^{-U/2})\) bleibt unverändert:
[Odd-Beweis, Zeilen 317–359](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L317-L359).
Damit sind auch die bisher ungeschriebenen Randspurfehler
\(o_f(\sqrt{M_U^{\rm cost}})\), die Zertifikatskosten bleiben
\(o_f(M_U^{\rm cost})\), und das scharfe obere Squeeze mit Koeffizient eins
bleibt erhalten. Es ist kein zusätzliches uniformes Graphraumtheorem nötig.

## 6. Abgleich mit dem neuen Metrik-Restgegenbeweis

Die eigene parallele Metrikanalyse beweist einen tatsächlich divergenten
TC1-Rest von mindestens Ordnung \(e^{U/2}/U^3\) auf festen \(m=0\)-Vektoren.
Das **widerspricht dem Wurzelanker nicht**: nach der hier verwendeten
führenden Normierung \(\lambda_U=e^U/U^2\) ist diese neue Restuntergrenze
von relativer Ordnung \(e^{-U/2}/U\), also verschwindend.
Der neue Normalbeweis braucht keine additive Beschränktheit dieses Restes.
Deshalb ist die Rang-eins-plus-beschränkt-Route zwar falsch, der positive
Wurzelanker kann dennoch erfolgreich sein.

## 7. Präziser Freigabe-Scope

- **GREEN:** N5–N16 sowie kanonisch PA1–PA19; globale Rang-eins-Ordnung;
  duale Riesz-Normkonvergenz;
  positive Wurzelmonotonie; Normsättigung; exaktes Intertwining;
  wirklicher Normalorbit \(W_Ue_{R,0}\to e_{S,0}\).
- **GREEN relativ zu den genannten vorhandenen P11/R42-Eingängen:**
  B-FLAGTIGHT und fixed-pair-C6/Strong Terminal auf dem ursprünglichen
  ungeraden Graphraum. Der glatte scharfe Oberbeweis kann mit §5 auch
  hinsichtlich der Randspuren ausformuliert werden.
- **Nicht bewiesen:** uniforme Konvergenz in \(R,S\), Operatornormkonvergenz
  des ganzen Transports, Rate, summierbares positives Variationsbudget,
  bounded-remainder-Metrikzerlegung, R37/G4c, Objekt-X-Realisierung oder RH.
- **Governance:** Dieses GREEN ist ein lokaler unabhängiger mathematischer
  Gegencheck, keine öffentliche Repository-Promotion und keine Behauptung,
  der gepinnte Repositorytext habe den neuen Schluss bereits verbucht.

**Kleine explizite Indexpräzisierung im kanonischen Entwurf:** PA17–PA18
sind mit \(m\ge1\) zu schreiben. Wenn \(P_0\) als Projektion auf
\(\mathcal H_S^{[0]}=\mathcal H_S\) mitgezählt würde, wäre
\(P_0\varepsilon_S=0\) falsch. Der Text spricht zwar von „tiefen“
Flagprojektionen, sollte den positiven Indexbereich aber ausschreiben.
Dies ändert weder den Normalbeweis noch den B-FLAGTIGHT-Schluss:
[kanonische Flagdefinition, Zeilen 59–85](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L59-L85).
