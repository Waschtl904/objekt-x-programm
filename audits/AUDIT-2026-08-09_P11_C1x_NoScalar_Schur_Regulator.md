# P11-C1x — No-scalar lemma für source-induzierte Hub-Feshbach-Regulatoren

**Datum:** 9. August 2026  
**Block:** P11 — Global Coupling and the Object-X Candidate Geometry  
**Status:** `✓[M]_{neg,scope}`  
**Vorgänger:** C1w

> **Scope-Firewall.** Das Resultat betrifft ausschließlich skalare positive Regulatoren `c_R I` in der kanonischen C1w-Hub/Rest-Feshbach-Spaltung. Es schließt keine operatorwertige, nichtdiagonale, fensterabhängige oder archimedisch gekoppelte Regulatormetrik aus.

---

## 0. Ausgangslage

Aus C1w, mit

\[
X=e^{2R},
\qquad
v_R(\xi)=h_R(\xi)\zeta_1+r_R(\xi),
\qquad
\rho_R(\xi):=\|r_R(\xi)\|^2,
\]

gilt für jedes feste `xi != 0`:

\[
|h_R(\xi)|^2
=O_\xi\!\left(\frac{\sqrt X}{\log X}\right),
\tag{C1x.1}
\]

und

\[
\rho_R(\xi)\ge c_\xi\sqrt X.
\tag{C1x.2}
\]

Damit

\[
\boxed{
\frac{\rho_R(\xi)}{1+|h_R(\xi)|^2}
\gtrsim_\xi \log X
\longrightarrow\infty.}
\tag{C1x.3}
\]

Insbesondere ist die Restenergie asymptotisch um mindestens einen logarithmischen Faktor größer als die Hubenergie.

---

# 1. Allgemeiner skalarer Regulator

Sei

\[
c_R>0
\]

beliebig, source-/cutoff-abhängig oder anderweitig vorgegeben. Betrachte

\[
B_{R,c_R}
:=
c_R I+\mathcal V_R\mathcal V_R^*.
\]

Aus C1w folgt faserweise exakt:

### Hub-Selbstenergie

\[
\boxed{
\Sigma_R^{\rm hub}(\xi)
=
\frac{c_R|h_R(\xi)|^2}{c_R+\rho_R(\xi)}.}
\tag{C1x.4}
\]

### Nichttrivialer Restanteil

Der Rang-eins-Restanteil hat Operatornorm

\[
\boxed{
\Tau_R^{\rm rest}(\xi)
=
\frac{c_R\rho_R(\xi)}{c_R+|h_R(\xi)|^2}.}
\tag{C1x.5}
\]

Die Frage lautet: Kann `c_R` so gewählt werden, dass gleichzeitig

\[
\Sigma_R^{\rm hub}(\xi)\not\to0
\]

und

\[
\sup_R\Tau_R^{\rm rest}(\xi)<\infty
\]

gilt?

---

# 2. Hauptsatz — beides ist inkompatibel

## Satz C1x.1

Für jedes feste `xi != 0` gilt:

\[
\boxed{
\liminf_{R\to\infty}\Sigma_R^{\rm hub}(\xi)>0
\quad\Longrightarrow\quad
\Tau_R^{\rm rest}(\xi)\to\infty.}
\tag{C1x.6}
\]

Umgekehrt:

\[
\boxed{
\sup_R\Tau_R^{\rm rest}(\xi)<\infty
\quad\Longrightarrow\quad
\Sigma_R^{\rm hub}(\xi)\to0.}
\tag{C1x.7}
\]

### Beweis

Nehme zunächst

\[
\Sigma_R^{\rm hub}(\xi)\ge\delta>0
\]

entlang eines Tails an. Aus (C1x.4):

\[
\delta
\le
\frac{c_R|h_R|^2}{c_R+\rho_R}
\le
\frac{c_R|h_R|^2}{\rho_R}.
\]

Daher

\[
\boxed{c_R\ge\delta\frac{\rho_R}{|h_R|^2}.}
\tag{C1x.8}
\]

Nun zwei Fälle.

### Fall A: `c_R >= |h_R|^2`

Dann

\[
\Tau_R^{\rm rest}
=
\frac{c_R\rho_R}{c_R+|h_R|^2}
\ge\frac12\rho_R
\to\infty.
\]

### Fall B: `c_R < |h_R|^2`

Dann

\[
\Tau_R^{\rm rest}
\ge
\frac{c_R\rho_R}{2|h_R|^2}.
\]

Mit (C1x.8):

\[
\Tau_R^{\rm rest}
\ge
\frac\delta2
\left(\frac{\rho_R}{|h_R|^2}\right)^2.
\]

Nach (C1x.1)–(C1x.3) wächst der Quotient mindestens logarithmisch, also

\[
\Tau_R^{\rm rest}
\gtrsim_{\xi,\delta}(\log X)^2
\to\infty.
\]

Damit ist (C1x.6) bewiesen.

Die Umkehrung (C1x.7) folgt kontrapositiv: Wäre `Sigma_hub` nicht gegen null, gäbe es eine Teilfolge mit positivem `liminf`, und auf dieser müsste `Tau_rest` divergieren.

`□`

---

# 3. Bedeutung für mögliche kanonische Skalen

Der Satz ist unabhängig davon, **woher** `c_R` kommt. Er erfasst insbesondere skalare Kandidaten aus

- Labelzahl `|N_R|`;
- Primzahlzahl `pi(e^{2R})`;
- `log X`, `R`, `sqrt(X)`;
- effektiver GCD-Dimension;
- einer skalaren Gamma-Masse;
- KMS-/Partitionsfunktions-Skalaren;
- jeder anderen positiven source-induzierten Zahl.

Keine solche skalare Wahl kann innerhalb des C1w-Hub-Schurmodells gleichzeitig den Hub nichttrivial und den Rest beschränkt halten.

Damit wird **keine einzelne Skalierung** verworfen, sondern die gesamte skalare Regulatorfamilie.

---

# 4. Verbindung zu P08/P10

Das Resultat ist strukturell analog zum P08-No-scalar-Prinzip, aber mathematisch davon unabhängig:

- P08 betrifft skalare Prä-Lanczos-Skalierung zweier Jacobi-Kanten unter einer Quotientendivergenz;
- C1x betrifft skalare positive Schur-Regulatoren der neuen BC-Hub/Rest-Geometrie.

Es darf daher nicht mit P10-O12 identifiziert werden, stärkt aber dieselbe strategische Diagnose:

\[
\boxed{\text{Die nächste brauchbare Metrik muss operatorwertig/nichtdiagonal sein.}}
\]

P10-O13 bleibt gerade deshalb die natürliche offene Tür.

---

# 5. Gamma als bloßer skalarer Regulator reicht ebenfalls nicht

C1d hat gezeigt, dass Gamma und Prime-Powers dieselbe Inzidenzfamilie `D_s` verwenden. Würde man den Gammaanteil in C1w jedoch nur auf einen positiven Skalar `c_R` reduzieren, fällt er unter Satz C1x.1.

Damit ist klar:

\[
\boxed{
\text{Eine erfolgreiche archimedische Kopplung muss ihre Operator-/Frequenzstruktur behalten;}
\\
\text{ein bloßer Gamma-Skalar kann den C1w-Konflikt nicht lösen.}}
\]

---

# 6. Was C1x nicht ausschließt

Ausdrücklich offen bleiben:

1. operatorwertige positive Regulatoren `C_R` statt `c_R I`;
2. nichtkommutierende source-window-/boundary-sensitive Regulatoren;
3. echte relative Quotienten mit wachsender Korrelation zwischen Primrestsektoren;
4. archimedische Operatorblöcke, die nicht auf einen Skalar reduziert werden;
5. Feshbach-Architekturen mit zusätzlichen Mediatorräumen;
6. Krein-/indefinite Vorformen mit anschließendem positivem globalem Quotienten, sofern sauber typisiert.

---

# 7. Gesamtaussage

\[
\boxed{
\text{C1x: Kein skalarer positiver }R\text{-abhängiger Schur-Regulator kann}
\\
\text{im C1w-Sternmodell gleichzeitig einen nichttrivialen Hub und einen beschränkten Rest liefern.}}
\]

Dies ist ein modellgebundener, aber vollständiger No-Go für die skalare Schur-Skalenfrage.

---

## 8. Nächster atomarer Knoten

\[
\boxed{\text{P11-C1y: operatorwertiger Regulator / archimedisch-primer Mischblock}}
\]

Erste Prüfroute:

- ersetze `c_R I` durch einen source-kanonischen positiven Operator `C_R`;
- teste zunächst den bereits vorhandenen archimedischen Inzidenzoperator aus C1d;
- prüfe Kommutativität mit dem Translationsfluss;
- falls `C_R=f_R(H_{trans})` weiterhin nur Fouriermultiplikation ist, entscheide sofort die Kompaktheitsfirewall;
- nur bei echter Nichtkommutativität beziehungsweise relativer Fensterstruktur lohnt ein Schatten-/Fredholmtest.

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
