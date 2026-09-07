# R43: Verschwindende Hub-Sprünge und bedingte terminale Orientierung

**Unabhängiger analytischer Gegencheck, 7. September 2026.** Die erste unabhängige Konstruktion untersuchte den sauberen Worktree `/home/user/workspace/r43_global_attack` am Commit `775158ee656d03bc3601857e8cb0e47fa791caf1`, einschließlich des korrigierten LOCAL-O1-Textes; dessen lokaler Quellstandvermerk nennt noch den älteren Ausgangscommit, die hier verwendeten Basisbelege sind dagegen auf den tatsächlich gelesenen neuen Stand gepinnt. Anschließend wurden der eingereichte lokale Beweis und sein finaler Änderungsdiff an den unten ausgewiesenen exakten Commits geprüft. ([LOCAL-O1](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

## 0. Finaler Exact-Head-Review des lokalen Parent-Beweises

**Urteil: SCOPED READY für J1–J11 einschließlich der neuen Verschärfung J7′. Kein mathematischer Blocker; keine offene Randkorrektur.**

Exakter **lokaler, unveröffentlichter** Prüfstand:

- Commit: `528153ec944a8201afe9235a53d96afc944fa9fc`
- Unmittelbarer Parent: `e7813fc7c5e1120a1e8aa5c9b26aff1d0bb9dea9`
- Veröffentlichte Definitionsbasis: `775158ee656d03bc3601857e8cb0e47fa791caf1`
- Datei: `audits/P11_R43_HUB_JUMP_DECAY_AND_CONDITIONAL_ORIENTATION_2026-09-07.md`
- Git-Blob: `501ea5acfdcbb812ba25534b9d4503ab307a18aa`
- Umfang der lokalen Datei: 423 Zeilen
- Gesicherte lokale Prüfkopie: `c6_jump_orientation_reviewed_local_528153ec.md`
- Gesicherter exakter Änderungsdiff: `c6_jump_orientation_exact_diff_528153ec.txt`

**Veröffentlichungsfirewall:** Weder `e7813fc...` noch `528153ec...` wird hier als online verfügbarer GitHub-Stand verlinkt. Die Online-Belege in diesem Bericht führen auf die veröffentlichte Definitionsbasis; die obigen exakten Commit-/Blobangaben bezeichnen lokal mit Git gelesene Prüfgegenstände. Die öffentlich referenzierbaren Voraussetzungen sind insbesondere die feste Pullback-Isometrie und die lokale Graphnormregularität. ([P11, (4.1)–(4.8)](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L599-L715); [korrigiertes LOCAL-O1](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

**Prüfumfang:** Der vorausgegangene vollständige Gegencheck von J1–J11 am lokalen Parent-Blob `4df927c3a8d30c18274a644de99aece44f6dfaa4` wird übernommen; zusätzlich ist der gesamte Diff der Orientierungsdatei zum finalen Head geprüft. Dieser Diff enthält ausschließlich den neuen Absatz mit J7′ in Zeilen 213–245 sowie die Ergänzung `T_* notin A` in Zeile 269. Die übrigen mathematischen Teile des geprüften Orientierungssatzes sind unverändert.

**Ausgeschlossen:** J12–J15, jetzt in Zeilen 338–403, sowie die im finalen Commit zusätzlich angelegte Datei `P11_R43_COND_FIXED_OLD_ALL_FUTURE_UNIFORMITY_2026-09-07.md`. Für diese Teile erfolgt durch dieses Urteil keine Freigabe. Das Urteil gilt nicht pauschal für den gesamten Commit.

| Teil des finalen lokalen Beweises | Finale Zeilen | Reviewbefund |
|---|---:|---|
| Feste Graphräume, Graphadjunkt, terminalunabhängiges \(c_X\), rechte Übergangswerte | 26–57 | READY, unverändert. |
| Eindeutige Aktivierung und Hubmajorante J1 | 45–82 | READY, unverändert. |
| Hubinkrement J2–J3 und identische starke Resolventengrenze | 84–109 | READY, unverändert. |
| Schur-/Graphsprung J4–J6 | 111–139 | READY, unverändert; \(64te^{-t}\) bleibt die korrekte Konstante. |
| Ursprünglicher Transportsprung J7–J9 | 141–205 | READY, unverändert; gültige gröbere Rate. |
| Neue Isometrieverschärfung J7′ | 213–245 | READY, neu exakt geprüft; Faktorstellungen und Konstante stimmen. |
| Reellheit und feste Phasenwahl | 249–258 | READY, unverändert. |
| Bedingter Orientierungssatz J10 und präzisierter Startpunkt | 260–303 | READY; die frühere nichtblockierende Randpräzisierung ist durch Zeile 269 erledigt. |
| Bedingtes Tightness-\(\iff\)-C6 in J11 | 305–336 | READY, unverändert; GC-AC-/R42-Abhängigkeiten bleiben explizit. |

**Destruktiver Recheck von J7′:** Die Identität in Zeilen 234–238 ergibt sich, indem die Differenz mit \(G_{R,+}^{1/2}\) rechts multipliziert und \(W_-G_{R,-}^{1/2}=G_{S,-}^{1/2}J\) eingesetzt wird. Kein Faktor wird vertauscht. Aus der exakten Pullback-Isometrie und der einseitigen Operatornormkonvergenz folgt \(W_-^*W_-=I\). Die beiden Wurzeldifferenzen kosten jeweils \(1/(2\sqrt{c_X})\), die rechte Inverswurzel \(1/\sqrt{c_R}\); mit \(\delta_t=64te^{-t}\) ergibt sich exakt

\[
\|W_+-W_-\|
\le32\left(\frac{\|J\|}{\sqrt{c_Sc_R}}+\frac1{c_R}\right)te^{-t}.
\]

Damit ist weder ein wachsender oberer Metrikfaktor noch eine weitere Konvergenzannahme nötig. Der neue lokale Absatz setzt genau die folgende veröffentlichte Isometrie-/Normgrenzwertstruktur ein. ([P11, (4.6)–(4.8)](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L599-L715); [LOCAL-O1, §§5–6](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

**Destruktiver Recheck des Startpunkts:** Weil die Aktivierungsmenge lokal endlich ist, kann nach jeder erforderlichen Modulus-/Sprungschwelle ein \(T_*\notin\mathcal A\) gewählt werden. Jede danach relevante Aktivierung liegt strikt rechts von \(T_*\); beide einseitigen Grenzen werden deshalb durch tatsächliche Werte des gewählten Schwanzes kontrolliert. Die Ergänzung behebt die frühere Randpräzisierung ohne zusätzliche Hypothese.

**Freigabegrenze:** SCOPED READY ist das mathematische Urteil dieses delegierten exakten Gegenchecks, keine automatische Registry-/Freeze-Buchung. Es bestätigt nur den bedingten Wegfall des eigenständigen Orientierungsgates nach starker Rest-Tightness; weder B-FLAGTIGHT selbst, GC-AC noch unbedingtes C6 werden hierdurch abgeschlossen.

## 1. Ergebnis und präzise Reichweite

**Der vorgeschlagene Sprung- und Orientierungsschluss ist richtig.** Die vorgeschlagene Operatornormschranke für die Sprünge des normierten Transports kann sogar verbessert werden: Mit den unten definierten festen Graphkonstanten gilt an jeder Hub-Aktivierung \(t>S\)

\[
\boxed{
\|W_{t+}-W_{t-}\|
\le K_{R,S}\,t e^{-t},
\qquad
K_{R,S}
=32\left(
\frac{\|J_{R,S}\|}{\sqrt{c_Sc_R}}+\frac1{c_R}
\right).
}
\tag{J1}
\]

Die neue Abschätzung verwendet die exakte Isometrie bereits vor dem Grenzübergang; sie benötigt weder GC-AC noch Tightness noch eine terminale Konvergenzannahme. Der Beweis erfolgt in §§2–5 aus den tatsächlichen Hub-/Rest- und Graphdefinitionen. ([P11, (2.5)–(3.3)](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L225-L328); [P11, (4.1)–(4.8)](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L599-L715))

Für die tatsächliche reelle Normalbahn auf dem **vollen reellen Terminalschwanz** folgt daraus:

\[
\boxed{
|b_V|\longrightarrow1
\quad\Longrightarrow\quad
\exists \sigma_{R,S}\in\{-1,1\},\ V_*:
\ \operatorname{sgn}b_V=\sigma_{R,S}\quad(V\ge V_*).
}
\tag{J2}
\]

Damit ist B-SIGN **keine zusätzliche unabhängige Beweisverpflichtung nach einem Beweis von \(|b_V|\to1\)**. Die Folgerung behauptet weder \(|b_V|\to1\) noch unbedingte Orientierung; insbesondere wird nicht behauptet, das schließlich konstante Vorzeichen sei positiv. Die Reellheit und die volle reelle Parametermenge sind hierbei entscheidende Eigenschaften des bestehenden R43-Rahmens. ([R43.44–R43.47](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L3338-L3505); [R43.65–R43.66a](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L4398-L4463))

Unter dem bestehenden R42-Tangentialgrenzsatz und dem **bedingt übernommenen GC-AC-/Zyklizitätsstack**, der \(h_V\rightharpoonup0\) liefert, ergibt sich daher für jedes feste Paar \(0<R<S\):

\[
\boxed{
\mathrm{StrongTerminal}_{R,S}
\quad\Longleftrightarrow\quad
\mathrm{B\!-\!FLAGTIGHT}_{R,S}
\quad\Longleftrightarrow\quad |b_V|\to1.
}
\tag{J3}
\]

Die Eingänge und beide Richtungen werden in §8 getrennt ausgewiesen; GC-AC selbst wird hier nicht neu bewiesen oder zertifiziert. ([R42, §7A](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md); [R43, GC-AC-Geltungsbereich](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L2675-L2751))

## 2. Feste Räume, tatsächlicher Rest und Grenzwerttopologien

Fixiere \(0<R<S\), setze \(\mathcal H_X=\mathcal K_{X,X}^{-}\) für \(X=R,S\), und schreibe \(J=J_{R,S}:\mathcal H_R\to\mathcal H_S\). Sämtliche nachfolgenden Quellmetrikadjunktionen und Transportnormen sind **Graphraum**-Adjunktionen und -Normen; der rohe Umgebungsraum ist separat \(\mathscr H=L^2(\mathbb R)\). ([LOCAL-O1, §§1, 5–6](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

Verwende auf \(\mathscr H\)

\[
M_V=1_{(-V,V)},\qquad
D_s=U_{s/2}-U_{-s/2},\qquad \|D_s\|\le2.
\]

Der tatsächliche eingebettete Hub ist

\[
\widehat H(V)
=M_V\sum_{p^k\le e^{2V}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}M_V.
\tag{J4}
\]

Insbesondere steht hier der scharfe Hub-Cutoff \(p^k\le e^{2V}\), nicht ein geglätteter Ersatz. ([P11, (2.5)](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L225-L328); [LOCAL-O1, LI6](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

### 2.1 Warum der vollständige Rest an einer Hub-Aktivierung nicht springt

Auf einem beliebigen festen Intervall \(V\le B<\infty\) wird der Rest in den festen Zeilenraum
\(\mathscr Z_B=\bigoplus_{(p,a)\in\mathcal I_B}L^2(\mathbb R)\) eingebettet, mit

\[
\begin{aligned}
\mathcal I_B&=\{(p,a):(a+1)\log p\le2B\},\\
K_B(p)&=\left\lfloor4B/\log p\right\rfloor,\\
c_{p,a}&=\sqrt{(\log p)(p-1)p^a},\\
M_{p,a}(V)&=1_{\{|u|<V-(a+1)\log p/2\}},\\
(\widehat R(V)f)_{p,a}
&=c_{p,a}M_{p,a}(V)
\sum_{k=a+1}^{K_B(p)}
p^{-3k/4}D_{k\log p}M_Vf.
\end{aligned}
\tag{J5}
\]

Bei nichtpositivem Radius ist die jeweilige Maske leer. Dies ist die exakte Martingalzeilendarstellung des P11-Rests: Die \(k\)-Summanden innerhalb einer Zeile bleiben kohärent, und der Rest wird ausdrücklich **nicht** bei \(e^{2V}\) abgeschnitten. Eine aktive Translation kann \(p^k\) bis \(e^{4V}\) benötigen. ([P11, (2.6) und anschließende effektive Endlichkeit](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L225-L328); [LOCAL-O1, LI3–LI4](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

Zur unabhängigen Kontrolle der Stetigkeit: Alle auftretenden Masken konvergieren bei \(V_n\to V\) fast überall; dominierte Konvergenz auf \(|f|^2\) liefert starke Konvergenz. Dies gilt auch beim Entstehen einer Maske aus Radius null. Die endlich vielen Produkte in J5 sind daher stark stetig. Ihre Adjunkte haben die umgekehrte Reihenfolge

\[
c_{p,a}M_V\sum_{k=a+1}^{K_B(p)}
p^{-3k/4}D_{k\log p}^{*}M_{p,a}(V)
\]

und sind ebenfalls stark stetig. Daraus folgt starke-* Stetigkeit des **vollständigen** \(\widehat R(V)\), nicht Operatornormstetigkeit der Rohmasken.

Folglich ist \(\widehat R(V)^*\widehat R(V)\) stark stetig. Für

\[
\widehat B(V)=
(I+\widehat R(V)^*\widehat R(V))^{-1},
\qquad 0<\widehat B(V)\le I,
\]

liefert die Resolventenidentität starke Stetigkeit; wegen Selbstadjungiertheit ist dies hier auch starke-* Stetigkeit. Der tatsächlich eingebettete inverse Operator lautet

\[
\widehat B(V)=E_V B_VP_V+(I-M_V),
\tag{J6}
\]

nicht bloß \(E_VB_VP_V\). Die beidseitige Fensterstütze des Hubs eliminiert den zusätzlichen Außenblock in der Schurform. ([LOCAL-O1, LI5–LI8](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

Diese Einbettung ist von der Wahl des ausreichend großen \(B\) unabhängig: zusätzlich aufgenommene Zeilen oder Translationen sind auf dem betrachteten Terminalintervall identisch null. Auch Aktivierungen von Restmasken oder Änderungen ihrer Überlappungsgeometrie erzeugen somit keinen weiteren starken Sprung.

### 2.2 Einseitige Grenzen sind zunächst starke, nicht Normgrenzen

Auf jeder Zelle ohne Hub-Aktivierung ist \(\widehat H(V)\) stark-* stetig. An einer Aktivierung \(t\) besitzt sie starke-* Grenzen \(H_-\) und \(H_+\); wegen des tatsächlichen Cutoffs „\(\le\)“ gilt \(\widehat H(t)=H_+\). Da \(\widehat B(V)\) zweiseitig stark stetig ist, sind die beiden starken Schurgrenzen

\[
\Sigma_- =H_-B_tH_-^*,\qquad
\Sigma_+=H_+B_tH_+^*,\qquad B_t=\widehat B(t).
\tag{J7}
\]

Dabei sind \(H_\pm\) Hubgrenzen, keine Paritätsbezeichnungen. Normabschätzungen für die Differenz der **Grenzoperatoren** sind zulässig, obwohl Normgrenzwerte der rohen Familie \(\widehat\Sigma(V)\) nicht behauptet werden. Genau diese Unterscheidung wahrt den in LOCAL-O1 verwendeten Kompakttransfer. ([LOCAL-O1, §§4–5](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

## 3. Einzelaktivierung, Hubgröße und Schursprung

### 3.1 Keine unkontrollierte Kollision von Primzahlpotenzen

Sei

\[
t=\frac12\log n,\qquad n=p^k,\quad p\ \text{prim},\ k\ge1.
\]

Ist zugleich \(n=q^\ell\) mit \(q\) prim, so erzwingt eindeutige Primfaktorzerlegung \(q=p\) und \(\ell=k\). Es gibt daher genau **einen** neu hinzukommenden Hub-Summanden; nichtprime Basen, etwa \(64=4^3\), sind keine zusätzlichen Indizes. Die beiden Translationen dieses einen Summanden sind bereits in \(D_{2t}\) enthalten.

Somit gilt exakt

\[
H_+=H_-+D_t^{\mathrm{jump}},
\qquad
D_t^{\mathrm{jump}}
=a_n M_tD_{2t}M_t,
\qquad
a_n=\sqrt{\log p}\,n^{-3/4}.
\tag{J8}
\]

Insbesondere

\[
\|D_t^{\mathrm{jump}}\|\le2a_n,\qquad
a_n\le\sqrt{2t}\,e^{-3t/2}.
\tag{J9}
\]

Ein verschwindender Aktivierungssprung wird hier gerade nicht angenommen: Bei \(V=t\) können die um \(t\) verschobenen Fenster bereits positive Überlappung haben. J8 ist eine unmittelbare Auswertung des tatsächlichen Hubs J4.

### 3.2 Elementare, globale Hubmajorante

Setze

\[
h_t=2\sum_{p^k\le e^{2t}}\sqrt{\log p}\,p^{-3k/4}.
\]

Die Menge der Primzahlpotenzen mit primen Basen ist ohne Mehrfachzählung eine Teilmenge der ganzen Zahlen \(m\ge2\). Für \(N=\lfloor e^{2t}\rfloor\) folgt daher

\[
\begin{aligned}
h_t
&\le2\sqrt{2t}\sum_{m=2}^{N}m^{-3/4}\\
&\le2\sqrt{2t}\int_1^{N}x^{-3/4}\,dx\\
&=8\sqrt{2t}(N^{1/4}-1)\\
&\le8\sqrt{2t}\,e^{t/2}.
\end{aligned}
\tag{J10}
\]

Für \(N=1\) ist die Summe leer und dieselbe letzte Schranke gültig. Es wird kein Primzahlsatz und keine numerische Näherung verwendet. Insbesondere

\[
\|H_\pm\|\le h_t,\qquad
h_t^2\le128t e^t.
\tag{J11}
\]

### 3.3 Exakter Differenzausdruck ohne fehlenden quadratischen Term

Mit \(D=D_t^{\mathrm{jump}}\) und \(0<B_t\le I\) gilt

\[
\begin{aligned}
\Sigma_+-\Sigma_-
&=D B_tH_+^*+H_-B_tD^*,\\
\|\Sigma_+-\Sigma_-\|
&\le\|D\|(\|H_+\|+\|H_-\|)\\
&\le4h_ta_n\\
&\le64t e^{-t}.
\end{aligned}
\tag{J12}
\]

Der Term \(DB_tD^*\) steckt bereits in \(DB_tH_+^*\); er wurde nicht weggelassen. Ebenso wird keine Positivität von \(\Sigma_+-\Sigma_-\) benötigt. Die wichtige Voraussetzung ist das **identische** \(B_t\) in beiden starken Grenzen, bewiesen in §2, nicht die Monotonie einer Restkompression.

## 4. Transfer in die tatsächlichen festen Graphmetriken

Sei \(i_X:\mathcal H_X\to L^2(-X,X)\) die feste Graphraumeinbettung und \(j_X=E_Xi_X\). Aus

\[
\mathfrak c_{\Gamma,X}[f]
\le q_X[f]
\le(1+\|H_X^{\mathrm{hub}}\|^2)\mathfrak c_{\Gamma,X}[f],
\qquad
\mathfrak c_{\Gamma,X}[f]\ge\|f\|_2^2
\]

folgen \(\|j_X\|\le1\) und die Kompaktheit von \(j_X\) über die feste Gamma-Einbettung. ([P11, Gamma-Graphraum und (3.3)](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L225-L328); [LOCAL-O1, §5.1](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

Bezeichnet \(\Gamma_X\) den Operator der Gamma-Form im **festen** Graphraum, so ist

\[
G_{X,V}
=\Gamma_X+j_X^*\widehat\Sigma(V)j_X.
\tag{J13}
\]

\(\Gamma_X\) ist terminalunabhängig, aber im Allgemeinen nicht die Identität. Das Adjunkt \(j_X^*:\mathscr H\to\mathcal H_X\) ist nicht mit roher \(L^2\)-Restriktion gleichzusetzen. ([LOCAL-O1, LI9](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

Aus starker Konvergenz einer lokal uniform beschränkten Familie \(S_V\) und Kompaktheit von \(j_X\) folgt \(\|(S_V-S)j_X\|\to0\): Ein endliches Netz des kompakten Bildes der Einheitskugel reduziert die Behauptung auf endlich viele feste Vektoren. Damit liefert J13 Operatornormstetigkeit der Metrik auf jeder Zelle und echte einseitige **Operatornorm**grenzen an den Aktivierungen.

Die Graphmetrik hat deshalb den tatsächlichen Sprung

\[
\Delta_tG_X
=G_{X,t+}-G_{X,t-}
=j_X^*(\Sigma_+-\Sigma_-)j_X,
\qquad
\|\Delta_tG_X\|\le\delta_t:=64t e^{-t}.
\tag{J14}
\]

Für jeden zulässigen Terminalradius \(V>X\), also ohne globale obere Beschränkung von \(V\), gilt

\[
c_XI\le G_{X,V},
\qquad
c_X=(1+\|H_X^{\mathrm{hub}}\|^2)^{-1}>0.
\tag{J15}
\]

Dies ist eine **quellradiusabhängige, terminalunabhängige** Schranke; es wird keine positive Untergrenze aus dem großen terminalen Restoperator benötigt. An den Grenzen einer Aktivierung \(t>S\) gilt zusätzlich

\[
G_{X,t\pm}\le M_tI,\qquad
M_t=1+h_t^2\le1+128t e^t.
\tag{J16}
\]

Die untere Schranke gilt also für alle zulässigen \(V\), die obere hier am festgehaltenen \(t\), nicht uniform auf dem gesamten unendlichen Terminalschwanz. ([P11, (4.4)–(4.5)](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L599-L715); [LOCAL-O1, LI10](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

## 5. Normierter Transportsprung: ursprüngliche und verbesserte Konstante

### 5.1 Wurzeln ohne Kommutativitätsannahme

Für positive beschränkte Operatoren \(A,B\ge cI\) setze \(Z=A^{1/2}-B^{1/2}\). Die nichtkommutative Sylvester-Identität

\[
A^{1/2}Z+ZB^{1/2}=A-B
\]

liefert

\[
Z=\int_0^\infty e^{-sA^{1/2}}(A-B)e^{-sB^{1/2}}\,ds,
\qquad
\|Z\|\le\frac{\|A-B\|}{2\sqrt c}.
\tag{J17}
\]

Außerdem ist die korrekt geordnete Identität

\[
A^{-1/2}-B^{-1/2}
=A^{-1/2}(B^{1/2}-A^{1/2})B^{-1/2}
\]

gültig, woraus

\[
\|A^{-1/2}-B^{-1/2}\|
\le\frac{\|A-B\|}{2c^{3/2}}
\tag{J18}
\]

folgt. Diese Argumente kontrollieren auch die einseitigen Normgrenzen der Wurzeln und Inversen; ein vertauschtes Inversenprodukt wird nicht verwendet. ([LOCAL-O1, LI12–LI16](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429))

### 5.2 Die vorgeschlagene Abschätzung ist korrekt

Schreibe \(G_{X,\pm}=G_{X,t\pm}\). Für

\[
W_\pm=G_{S,\pm}^{1/2}JG_{R,\pm}^{-1/2}
\]

ergibt die direkte Produktdifferenz

\[
\boxed{
\|W_+-W_-\|
\le\frac{\|J\|\delta_t}{2}
\left[
\frac1{\sqrt{c_Sc_R}}+
\frac{\sqrt{M_t}}{c_R^{3/2}}
\right].
}
\tag{J19}
\]

Für \(t\ge1\) gilt \(\sqrt{M_t}\le(1+8\sqrt2)\sqrt t\,e^{t/2}\), also

\[
\|W_+-W_-\|
\le K^{\mathrm{alt}}_{R,S}t^{3/2}e^{-t/2},
\]

\[
K^{\mathrm{alt}}_{R,S}
=32\|J\|
\left[
\frac1{\sqrt{c_Sc_R}}+
\frac{1+8\sqrt2}{c_R^{3/2}}
\right].
\tag{J20}
\]

Damit ist auch die ursprünglich vorgeschlagene Rate vollständig bestätigt.

### 5.3 Die Isometrie eliminiert den wachsenden oberen Metrikfaktor

Die exakte Pullback-Identität \(J^*G_{S,V}J=G_{R,V}\) impliziert \(W_V^*W_V=I\). Da sie in den einseitigen Operatornormgrenzen erhalten bleibt, gilt auch \(W_\pm^*W_\pm=I\), insbesondere \(\|W_-\|=1\). ([P11, (4.6)–(4.8)](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L599-L715))

Jetzt werden die Identitäten

\[
W_\pm G_{R,\pm}^{1/2}=G_{S,\pm}^{1/2}J
\]

subtrahiert, wobei sämtliche Faktorstellungen erhalten bleiben:

\[
\boxed{
W_+-W_-
=
\left[
(G_{S,+}^{1/2}-G_{S,-}^{1/2})J
-W_-(G_{R,+}^{1/2}-G_{R,-}^{1/2})
\right]G_{R,+}^{-1/2}.
}
\tag{J21}
\]

Somit folgt allein mit J17 und J15

\[
\begin{aligned}
\|W_+-W_-\|
&\le
\frac{\delta_t}{2\sqrt{c_R}}
\left(\frac{\|J\|}{\sqrt{c_S}}+\frac1{\sqrt{c_R}}\right)\\
&\le
32\left(\frac{\|J\|}{\sqrt{c_Sc_R}}+\frac1{c_R}\right)t e^{-t}.
\end{aligned}
\tag{J22}
\]

Dies beweist J1. Der Fortschritt gegenüber J19 besteht darin, dass \(G_{S,-}^{1/2}J\) nicht durch \(\sqrt{M_t}\|J\|\) abgeschätzt, sondern exakt als \(W_-G_{R,-}^{1/2}\) verwendet wird. Eine Inverswurzel-Differenz ist für J22 gar nicht mehr erforderlich.

### 5.4 Vollständig durch die Quellradien ausgedrückte Konstante

Definiere

\[
d_X:=1+128Xe^X.
\]

J10 und die feste Graphübergangsschranke ergeben

\[
c_X^{-1}\le d_X,\qquad
\|J\|\le\sqrt{1+\|H_S^{\mathrm{hub}}\|^2}=c_S^{-1/2}\le\sqrt{d_S}.
\]

Daher kann in J1 die explizite größere Konstante

\[
\boxed{
\overline K_{R,S}=32\left(d_S\sqrt{d_R}+d_R\right)
}
\tag{J23}
\]

verwendet werden; sie enthält keine unbekannte terminale Konditionszahl. Die benötigte Übergangsschranke ist die tatsächliche Graphschranke aus P11, nicht die \(L^2\)-Norm der Nullerweiterung. ([P11, (4.1)–(4.4)](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L599-L715))

## 6. Parität und Reellheit: zwei verschiedene Prüfungen

### 6.1 Der Hub wechselt die Parität; die Schurform erhält sie

Sei \(\mathcal P f(u)=f(-u)\), mit zeilenweiser Spiegelung \(\mathcal P_{\mathscr Z}\) im Restraum. Die Masken sind gerade und

\[
\mathcal P D_s=-D_s\mathcal P.
\]

Deshalb antikommutiert der Hub mit \(\mathcal P\), und
\(\widehat R(V)\mathcal P=-\mathcal P_{\mathscr Z}\widehat R(V)\). Es folgt

\[
\mathcal P\widehat R(V)^*\widehat R(V)
=\widehat R(V)^*\widehat R(V)\mathcal P,
\quad
\mathcal P\widehat B(V)=\widehat B(V)\mathcal P,
\quad
\mathcal P\widehat\Sigma(V)=\widehat\Sigma(V)\mathcal P.
\]

Die Rechnung wird daher korrekt zuerst auf dem vollen \(L^2\)-Raum ausgeführt und erst danach auf die ungerade Graphgeometrie eingeschränkt. Für einen ungeraden Testvektor wirkt \(H^*\) zunächst in den geraden Sektor, dort wirkt \(B\), danach geht \(H\) zurück in den ungeraden Sektor. Eine vorherige Ersetzung des Hubs durch einen ungerade-zu-ungerade-Block wäre falsch.

Das Gamma-Symbol ist gerade und reell, also erhält auch die Gamma-Form die Parität. Damit erhalten die tatsächlichen Metriken, ihre positiven Wurzeln und \(W_V\) den ungeraden Sektor. ([R33, Proposition R33-C](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R33_GAMMA_SYMBOL_BRIDGE_2026-08-19.md#L60-L115); [P11, Definitionen](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L225-L328))

### 6.2 Die kanonische Normalbahn ist reell

Alle Masken, Translationen und Hub-/Restgewichte sind reell. Die Gamma-Form ist wegen ihres reellen geraden Symbols mit komplexer Konjugation verträglich; folglich sind es auch die Graphadjunktionen, die positiven Metrikwurzeln und \(W_V\). Der kanonisch mit \(\beta_X^{(0)}(\varepsilon_X)>0\) fixierte Riesznormalvektor ist reell. Daher

\[
w_V=W_V\varepsilon_R,\qquad
b_V=\langle w_V,\varepsilon_S\rangle\in[-1,1].
\tag{J24}
\]

Dieser Beweis der Reellheit verwendet keine GC-AC-Folgerung, auch wenn er im Repository unter der übergreifenden GC-AC-Überschrift steht. ([R43.44–R43.45](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L3338-L3505))

Aus der Isometrie und der festen orthogonalen Zerlegung folgt ebenfalls ohne GC-AC

\[
h_V=w_V-b_V\varepsilon_S\in\mathcal H_S^0,
\qquad
\|h_V\|^2=1-b_V^2.
\tag{J25}
\]

Die reelle Eigenschaft ist unentbehrlich: Die abstrakte komplexe Bahn \(w_V=e^{iV}\varepsilon_S\) wäre stetig, hätte keine Sprünge und \(|b_V|=1\), aber keinen Grenzwert. Sie ist kein Modell der reellen P11-Bahn, sondern ein Gegenbeispiel gegen das Weglassen der Reellheitsvoraussetzung.

## 7. Quantifizierter Orientierungssatz auf dem ganzen reellen Schwanz

### 7.1 Verfügbare Regularität und explizite Sprungschwelle

Die Aktivierungsmenge

\[
\mathcal E=\left\{\tfrac12\log(p^k):p\ \text{prim},\ k\ge1\right\}
\]

ist lokal endlich: In jedem beschränkten Terminalintervall liegen nur endlich viele entsprechende ganze Zahlen. Nach §§2–5 ist \(V\mapsto W_V\) auf jeder offenen Zelle operatornormstetig, besitzt an jedem Übergang beide Operatornormgrenzen und stimmt dort mit dem rechten Grenzwert überein. Die gleiche Aussage gilt für den reellen Skalar \(b_V\). Zudem

\[
|b_{t+}-b_{t-}|
\le\|W_{t+}-W_{t-}\|
\le K_{R,S}t e^{-t}\longrightarrow0
\qquad(t\in\mathcal E,\ t\to\infty).
\tag{J26}
\]

Für \(K=K_{R,S}\), alternativ \(K=\overline K_{R,S}\), ist beispielsweise

\[
T_{\mathrm{jump}}
=\max\{S+1,\ 2,\ 2\log(4K/e)\}
\tag{J27}
\]

eine vollständig explizite Schwelle mit

\[
|b_{t+}-b_{t-}|\le\tfrac12
\qquad(t\in\mathcal E,\ t\ge T_{\mathrm{jump}}).
\tag{J28}
\]

Denn \(t e^{-t/2}\le2/e\) für \(t\ge0\), also
\(Kt e^{-t}\le(2K/e)e^{-t/2}\). J27 kontrolliert nur die Sprünge, nicht die zwischen ihnen stattfindende Bewegung.

### 7.2 Abstraktes Lemma

**Lemma.** Sei \(b:[A,\infty)\to\mathbb R\) rechtsstetig, außerhalb einer lokal endlichen Menge \(\mathcal E\) stetig, mit beiden einseitigen Grenzen an deren Punkten. Angenommen,

\[
\lim_{\substack{t\to\infty\\t\in\mathcal E}}
|b(t+)-b(t-)|=0,
\qquad
\liminf_{V\to\infty}|b(V)|>0.
\]

Dann ist das Vorzeichen von \(b\) schließlich konstant.

**Beweis.** Wähle \(\alpha>0\) und \(A_1\), sodass \(|b(V)|\ge\alpha\) für alle \(V\ge A_1\), und verschiebe die Schwelle so weit nach rechts, dass jeder spätere Sprung kleiner als \(2\alpha\) ist. Auf jeder offenen Zelle kann sich das Vorzeichen wegen des Zwischenwertsatzes nicht ändern. Ihre einseitigen Randwerte haben ebenfalls Betrag mindestens \(\alpha\): Sie sind Grenzen tatsächlicher später Terminalwerte. Entgegengesetzte Vorzeichen an den beiden Seiten eines Sprunges würden eine Sprunggröße mindestens \(2\alpha\) erzwingen, im Widerspruch zur Wahl der Schwelle. Der tatsächliche Wert am Sprung stimmt mit dem rechten Wert überein und kann deshalb keinen isolierten abweichenden Vorzeichenwert erzeugen. Zwischen beliebigen zwei endlichen späteren Terminalwerten liegen nur endlich viele Übergänge; Vorzeichenkonstanz wird über diese endliche Zellenkette fortgesetzt. Also haben alle späteren Werte dasselbe Vorzeichen. \(\square\)

### 7.3 Anwendung unter \(|b_V|\to1\)

Angenommen, \(|b_V|\to1\) auf dem **vollen** reellen Schwanz \(V>S\). Es existiert dann \(T_{\mathrm{mod}}\), sodass

\[
|b_V|\ge\tfrac34\qquad(V\ge T_{\mathrm{mod}}).
\]

Wähle \(V_*>\max\{T_{\mathrm{mod}},T_{\mathrm{jump}}\}\). Für jeden Übergang \(t\ge V_*\) haben beide Grenzwerte Betrag mindestens \(3/4\). Entgegengesetzte Vorzeichen würden einen Sprung mindestens \(3/2\) verlangen, während J28 höchstens \(1/2\) zulässt. Innerhalb der Zellen verhindert der Zwischenwertsatz einen Vorzeichenwechsel. Damit folgt J2.

Die Schwelle \(T_{\mathrm{mod}}\) bleibt von einem zukünftigen Tightness-/Modulusbeweis abhängig; ihre Existenz wird hier nicht aus LOCAL-O1 oder J1 hergeleitet. Auch eine vorab gegebene äquidistante oder arithmetische Terminalfolge wird nicht eingeschoben: Der R43-Parameter ist der volle reelle Schwanz, sodass jedes endliche Verbindungsintervall im Definitionsbereich liegt. ([R43, tatsächlicher Terminalbereich](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L4398-L4463))

Schließlich liefert \(|b_V|\to1\) zusammen mit der festen Orientierung \(\sigma=\sigma_{R,S}\)

\[
b_V\to\sigma,\qquad
w_V\longrightarrow\sigma\varepsilon_S,
\qquad
\boxed{\|w_V-\sigma\varepsilon_S\|^2=2(1-|b_V|)}
\quad(V\ge V_*).
\tag{J29}
\]

Die letzte Identität folgt aus \(\|w_V\|=\|\varepsilon_S\|=1\) und \(\sigma b_V=|b_V|\). Damit wird Normalbahnkonvergenz bewiesen, nicht vorausgesetzt.

## 8. GC-AC, Tightness und Strong Terminal: getrennte logische Ebenen

### 8.1 Was ohne GC-AC bewiesen ist

Aus den tatsächlichen endlichen P11-Definitionen und der überprüften lokalen Graphregularität folgen J1, die Reellheit von \(b_V\), J25 und

\[
|b_V|\to1
\ \Longrightarrow\
\mathrm{B\!-\!SIGN}
\ \Longrightarrow_{\ |b_V|\to1\ }\
w_V\to\sigma\varepsilon_S.
\tag{J30}
\]

GC-AC ist kein Eingang dieser Implikation. Ihr Modulus-Eingang ist jedoch eine echte zusätzliche asymptotische Hypothese.

### 8.2 Wo GC-AC tatsächlich gebraucht wird

Der bestehende GC-AC-/Gamma-Zyklizitätsstack liefert in R43.10da die Konzentration aller schwachen Cluster von \(w_V\) auf \(\mathbb C\varepsilon_S\); daraus folgt R43.48:

\[
h_V\rightharpoonup0.
\tag{J31}
\]

Genau dieser Schluss wird hier **bedingt** importiert, mit den im Repository angegebenen Eingängen zur skalaren Multiplizität, absoluten Stetigkeit der höheren Jetmaße und Totalität. Weder die skalare Multiplizität noch die Literatur-/Realisierungsschnittstellen werden durch den Sprungbeweis ersetzt. ([R43, §§3K.5–3K.6 und Status](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L2675-L2751); [R43.48](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L3338-L3505))

Die tatsächliche kanonische Flagge hat

\[
P_S^{[m]}\mathcal H_S^0
=\overline{\operatorname{span}}\{e_{S,n}:n\ge m\},
\]

und der primäre Tightness-Eingang lautet

\[
\mathrm{B\!-\!FLAGTIGHT}:\qquad
\lim_{m\to\infty}\limsup_{V\to\infty}
\|P_S^{[m]}h_V\|=0.
\tag{J32}
\]

Dies ist eine asymptotische Schwanzbedingung mit der angegebenen Reihenfolge der Quantoren, nicht automatisch eine uniforme Aussage auf einem einmal festgelegten vollständigen Terminalschwanz. ([R43.54–R43.57b](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L3507-L3619))

Unter J31 gilt für jedes feste \(m\)

\[
\|(I-P_S^{[m]})h_V\|\longrightarrow0,
\]

weil dieser Teil von \(h_V\) in einem festen endlichdimensionalen Raum liegt. Die orthogonale Zerlegung und J32 liefern dann

\[
\begin{aligned}
\limsup_{V\to\infty}\|h_V\|^2
&=\limsup_{V\to\infty}\|P_S^{[m]}h_V\|^2
\longrightarrow0\qquad(m\to\infty).
\end{aligned}
\]

Damit

\[
\boxed{
[h_V\rightharpoonup0]
\quad\Longrightarrow\quad
\bigl[
\mathrm{B\!-\!FLAGTIGHT}
\iff\|h_V\|\to0
\iff |b_V|\to1
\bigr].
}
\tag{J33}
\]

Ohne J31 wäre Flag-Tightness allein nicht genug: Eine abstrakte konstante Bahn \(h_V=e_{S,1}\), \(b_V=0\) hat verschwindende tiefe Flag-Tails, aber keine verschwindende Restnorm. Dieses Beispiel widerlegt nur das Weglassen des schwachen Nullgrenzeingangs, nicht eine P11-Aussage.

### 8.3 R42 erweitert die Normalbahnkonvergenz auf den ganzen ungeraden Raum

R42.51–R42.52 liefern für \(f_0\in\mathcal H_R^0\) den starken Grenzwert

\[
W_Vf_0\longrightarrow W_{R,S}^{(0)}f_0,
\qquad
W_{R,S}^{(0)}:\mathcal H_R^0\to\mathcal H_S^0
\ \text{isometrisch}.
\]

R42.58 reduziert deshalb Strong Terminal für das feste Paar genau auf die Normalbahn. Dieser vorhandene unendlichdimensionale Tangentialsatz wird übernommen, nicht aus den kleinen Sprüngen neu gefolgert. ([R42, §7A.5 und §7A.7](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md))

Unter J33 und J29 folgt für \(f=f_0+z\varepsilon_R\) somit

\[
\boxed{
W_Vf\longrightarrow
W_{R,S}^{(\infty)}f
:=
W_{R,S}^{(0)}f_0+z\sigma_{R,S}\varepsilon_S.
}
\tag{J34}
\]

Die beiden Zielkomponenten sind orthogonal, also ist \(W_{R,S}^{(\infty)}\) eine Isometrie. Umgekehrt erzwingt Strong Terminal unter J31 einen starken Grenzwert von \(h_V\), dessen schwacher Grenzwert null ist; daher \(\|h_V\|\to0\), und J32 folgt. Dies beweist J3 in beiden Richtungen.

**Der reduzierte Beweisauftrag lautet deshalb:** Unter dem bestehenden R42-/GC-AC-Stack genügt der Beweis der tatsächlichen globalen B-FLAGTIGHT-Bedingung. Danach ist keine zusätzliche Vorzeichen-/Antipodenschranke mehr als unabhängiger analytischer Eingang erforderlich.

## 9. Grenzen und zerstörerischer Gegencheck

| Möglicher Fehler | Ergebnis des Gegenchecks |
|---|---|
| Rest versehentlich beim Hub-Cutoff abgeschnitten | Ausgeschlossen durch J5: sichere lokale Restobergrenze \(e^{4B}\), kohärente Summen innerhalb jeder Martingalzeile. |
| Gleiches \(B_t\) links und rechts nur angenommen | Stark-* Stetigkeit von Rest und Resolvente ist in §2 aus den tatsächlichen Masken hergeleitet. |
| Starke Rohgrenzen mit Normgrenzen verwechselt | Rohgrenzen bleiben starke-* Grenzen; erst das feste kompakte \(j_X\) gibt die benötigten Normgrenzen der Graphmetriken. |
| Mehrere Prime-Powers am selben \(t\) erzeugen unkontrollierten Faktor | Eindeutige Primfaktorzerlegung lässt genau einen Hubindex zu; beide Translationsrichtungen sind im Faktor 2 enthalten. |
| Quadratischer Hubinkrementterm fehlt | In J12 ist \(DB_tD^*\) in \(DB_tH_+^*\) enthalten. |
| Odd-Sektor falsch vor dem Hub abgeschnitten | §6 behält die Paritätswechsel des Hubs und des Rests; eingeschränkt wird erst die paritätserhaltende Schur-/Graphmetrik. |
| Graphadjunkt durch \(L^2\)-Restriktion ersetzt | J13 verwendet das tatsächliche feste Graphadjunkt \(j_X^*\). |
| Untere Spektralschranke verschlechtert sich mit \(t\) | J15 hängt nur vom festen Quellradius ab. |
| Nichtkommutative Inversreihenfolge vertauscht | J17–J18 und insbesondere J21 sind explizit geordnet. |
| Isometrie der einseitigen Grenztransporte fehlt | Sie folgt entweder aus der Normgrenze tatsächlicher Isometrien oder direkt aus der grenzwertstabilen Pullback-Identität. |
| Einzelner abweichender Wert am Sprung umgeht den Beweis | Der tatsächliche „\(\le\)“-Cutoff ist rechtsstetig; es gibt keinen dritten isolierten Wert. |
| Unendlich viele Sprünge werden unzulässig gemeinsam überquert | Zwischen beliebigen zwei endlichen Terminals liegen nur endlich viele Zellen; der Beweis verwendet endliche Fortsetzung, keine unendliche Sprungsumme. |
| Komplexe Phase statt reellem Vorzeichen | Die kanonische P11-Normalbahn ist reell; ohne diese Eigenschaft wäre der Orientierungssatz falsch. |
| Lokale Regularität als globale Tightness ausgegeben | J32 bleibt eine zusätzliche offene asymptotische Bedingung. |

Die Rohdefinitionen, Normgrenzwertschritte und festen Graphschranken dieser Tabelle beziehen sich auf den korrigierten LOCAL-O1-Stand und die zugehörigen P11-Definitionen. ([LOCAL-O1](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md#L103-L429); [P11, Graphtransporte](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L599-L715))

Insbesondere wird **keine** der folgenden Aussagen bewiesen:

- eine globale Modulusbedingung \(|b_V|\to1\) oder globale B-FLAGTIGHT aus LOCAL-O1 allein;
- eine uniforme Schranke für alle endlichen Inkremente \(W_V-W_U\) allein aus J1;
- endliche totale Variation, summierbare Sprungvariation oder ein FD23-Summierbarkeitsabschluss;
- ein terminaler Generator, eine Ableitung oder eine kontrollierte Bewegung innerhalb aller großen Zellen;
- eine positive statt lediglich schließlich konstante Orientierung;
- eine uniforme Orientierungsschwelle über alle Quellpaare, Konvergenz in Operatornorm oder eine neue Aussage über den geraden Sektor;
- ein unbedingter Strong-Terminal-/C6-, Objekt-X- oder RH-Abschluss.

Kleine einzelne Sprünge verhindern unter einem positiven Abstand von \(b_V\) zu null lediglich den Wechsel zwischen den beiden reellen Vorzeichenkomponenten. Sie verhindern ohne Tightness keine Flucht der Normalbahn in immer tiefere Richtungen zwischen den Sprüngen. Der abstrakte lokal stetige Fluchtmechanismus aus LOCAL-O1 bleibt deshalb als Firewall gegen „lokal kompakt \(\Rightarrow\) global tight“ vollständig wirksam. ([LOCAL-O1, vollständiger Beweis einschließlich §9](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md))

**Schlussbuchung dieses Befundes:** Analytische Bestätigung des Sprunglemmas, verbessert zu J22, sowie bedingter Wegfall des separaten B-SIGN-Gates nach \(|b_V|\to1\). Globales B-FLAGTIGHT bleibt die zu beweisende asymptotische Hauptbedingung. Durch diesen Gegencheck wurden keine Repository-Dateien, keine GitHub-Ressourcen und keine Registry-/Freeze-Einträge geändert.
