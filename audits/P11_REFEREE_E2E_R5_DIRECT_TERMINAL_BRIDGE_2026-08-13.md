# P11 END-TO-END REFEREE AUDIT — R5: DIRECT TERMINAL BRIDGE

**Datum:** 2026-08-13  
**Modul:** `papers/P11_sections/P11_Direct_Terminal_Bridge.tex`  
**Knoten:** `thm:jet-expansion`, `thm:absolute-no-go`, `prop:parity`, `thm:jet-complete`, `thm:cross-terminal`, `thm:smooth-odd-core`  
**Auditmodus:** End-to-End-Referee.

---

# 0. Gesamturteil

Die mathematischen Aussagen des Blocks überstehen den Direktaudit. Ein lokaler Self-Containment-Defekt bleibt im Beweis von `thm:smooth-odd-core`: die exakte Dilation inequality (DT.25) wird aus einer im P11-Paper nicht dargestellten "explicit positive series" importiert.

Die benötigte Core-Aussage folgt jedoch bereits aus der im Paper vorhandenen Symbolvergleichbarkeit `w(\xi)\asymp\log(2+|\xi|)`; der Satz ist daher nicht widerlegt, aber sein aktueller Paperbeweis soll lokal ersetzt werden.

Gesamtstatus:

\[
\boxed{
[\mathrm{P11\text{-}R5\text{-}DIRECT}]
=\checkmark[M]_{\rm part}.
}
\]

---

# 1. Full constant-mode boundary expansion

Für festes `r\le R` ist der primitive Anteil von

\[
\Phi_T(r)
=\sum_{e^{2(T-r)}<p^k\le e^{2T}}
\sqrt{\log p}\,p^{-3k/4}
\]

durch

\[
\sum_{e^{2(T-r)}<p\le e^{2T}}
\sqrt{\log p}\,p^{-3/4}
\]

gegeben. Partial summation mit `\vartheta(x)=x+O(xe^{-c\sqrt{\log x}})` und der Substitution

\[
x=e^{2(T-s)}
\]

gibt

\[
\sqrt2\,e^{T/2}T^{-1/2}
\int_0^r e^{-s/2}(1-s/T)^{-1/2}ds
\]

mit einem auf festem `r` superpolynomiell kleinen PNT-Rest relativ zur `T^{-M}`-Skala.

Für `k\ge2` ist bereits der `k=2`-Beitrag von Ordnung `O(e^{-T/2}\,\mathrm{poly}(T))`, also exponentiell kleiner als `e^{T/2}T^{-N}` für jedes feste `N`; höhere `k` sind noch kleiner.

Die binomiale Expansion

\[
(1-s/T)^{-1/2}
=\sum_{m=0}^Mc_m(s/T)^m+O_{R,M}(T^{-M-1})
\]

liefert exakt die Jets

\[
I_m(r)=\int_0^r s^me^{-s/2}ds
\]

und damit die behauptete Expansion.

Zero extension ändert die Jetintegrale auf dem alten Support nicht.

\[
\boxed{[\mathrm{R5\text{-}JET}]\;\checkmark[M].}
\]

---

# 2. Absolute terminal-metric no-go

Für ein festes nichtnegatives `f\in C_c^\infty((0,R))`, `f\ne0`, gilt

\[
\beta_R^{(0)}(f)>0
\]

und daher

\[
|\ell_T(f)|\asymp e^{T/2}T^{-1/2}.
\]

Die grobe, aber ausreichende Denominatorabschätzung

\[
\langle\mathbf1_T,A_T\mathbf1_T\rangle=O(T^2)
\]

ergibt

\[
\sigma_T(J_{R,T}f)
\gtrsim_f e^T/T^3.
\]

Da

\[
\langle G_{R,T}f,f\rangle_{X,R}
=
\|J_{R,T}f\|_{X,T}^2
=
\mathfrak c_{\Gamma,R}[f]
+
\sigma_T(J_{R,T}f),
\]

divergiert ein fester Matrixkoeffizient. Insbesondere `\|G_{R,T}\|\to\infty`.

Eine schwach oder stark konvergente Operatorfolge in `\mathcal B(\mathcal K_{X,R})` wäre nach Uniform Boundedness normbeschränkt; dies ist ausgeschlossen.

Kleine Notationsreparatur: Im Modul steht an dieser Stelle einmal `q_{\Gamma,R}(f)` statt der sonst verwendeten `\mathfrak c_{\Gamma,R}[f]`. Die mathematische Identität ist eindeutig, aber die Notation sollte vereinheitlicht werden.

\[
\boxed{[\mathrm{R5\text{-}ABS}]\;\checkmark[M].}
\]

---

# 3. Parität und Jet-Vollständigkeit

`D_s` vertauscht Parität, während die Cutofftiefe nur von `|u|` abhängt. Daher antikommutieren `H_R` und `R_R` mit den passenden Reflection-Operatoren; `R_R^*R_R` und `B_R` kommutieren. Die Gammaform ist wegen des geraden Multipliers reflection invariant.

Damit ist die Reflection ein unitärer Involutionsoperator im `X`-Graph-Hilbertraum und erzeugt die orthogonale Zerlegung

\[
\mathcal K_{X,R}=\mathcal K_{X,R}^+\oplus^{\perp_X}\mathcal K_{X,R}^-.
\]

Für odd `f` ist

\[
\beta_R^{(m)}(f)=2\int_0^RI_m(r)f(r)dr.
\]

Setzt man

\[
F(s)=\int_s^R f(r)dr,
\]

so liefert Fubini aus dem Verschwinden aller Jets

\[
\int_0^R s^me^{-s/2}F(s)ds=0
\qquad(m\ge0).
\]

Polynomdichte in `L^2((0,R),e^{-s/2}ds)` erzwingt `F=0`, also `f=0`.

Da die Jetfunktionale bereits in `L^2` stetig sind und die Graphnorm `L^2` dominiert, folgt die Graphraumidentität

\[
\bigcap_m\ker\beta_R^{(m)}=\mathcal K_{X,R}^+.
\]

\[
\boxed{[\mathrm{R5\text{-}PARITY/JET}]\;\checkmark[M].}
\]

---

# 4. Cross-terminal kernel und Cauchy identity

Mit

\[
K_{R,S}^{T,U}
=(W_{R,S}^{[T]})^*W_{R,S}^{[U]}
\]

und der Isometrie beider `W` gilt

\[
\begin{aligned}
\|(W^{[U]}-W^{[T]})f\|^2
&=\|W^{[U]}f\|^2+\|W^{[T]}f\|^2
 -2\operatorname{Re}\langle W^{[U]}f,W^{[T]}f\rangle\\
&=2\|f\|^2
 -2\operatorname{Re}\langle f,(W^{[T]})^*W^{[U]}f\rangle.
\end{aligned}
\]

Die explizite Formel für `K_{R,S}^{T,U}` folgt durch Einsetzen der beiden terminal gauges. Es gibt keinen Grund für Selfadjointness, und das Paper behauptet sie ausdrücklich nicht.

\[
\boxed{[\mathrm{R5\text{-}CROSS}]\;\checkmark[M].}
\]

---

# 5. Smooth odd graph core — Satz korrekt, aktuelle Begründung nicht vollständig paperintern

Der aktuelle Beweis setzt

\[
w(\xi)=1+g_\infty(\xi)
\]

und behauptet aus einer "explicit positive series"

\[
w(\lambda\xi)\le\lambda^2w(\xi)
\qquad(\lambda\ge1).
\tag{R5.1}
\]

Diese positive series wird im P11-Paper jedoch nicht dargestellt. Im End-to-End-Modus darf sie daher nicht als versteckter Audit-/Vorwissensimport verwendet werden.

## Interne Reparatur aus der bereits bewiesenen Symbolvergleichbarkeit

Das Paper hat bereits

\[
c\log(2+|\xi|)
\le w(\xi)
\le C\log(2+|\xi|).
\]

Fixiere `a_0\in(0,1)`. Für `a\in[a_0,1]` gilt

\[
\log(2+|\xi|/a)
\le C_{a_0}\log(2+|\xi|),
\]

also

\[
\boxed{
w(\xi/a)\le C_{a_0}'w(\xi).
}
\tag{R5.2}
\]

Für die inward dilation

\[
F_a(x)=a^{-1/2}F(x/a)
\]

ist

\[
\widehat{F_a}(\xi)=a^{1/2}\widehat F(a\xi).
\]

Nach `\eta=a\xi` zeigt (R5.2), dass die Dilationsoperatoren für `a\in[a_0,1]` gleichmäßig beschränkt auf `L^2(wd\xi)` sind. Auf der dichten Klasse glatter kompakt unterstützter Fourierfunktionen ist

\[
F_a\to F
\]

für `a\uparrow1` unmittelbar; uniforme Beschränktheit erweitert dies auf den ganzen Gamma-Formraum.

Gleichzeitig schrumpft der Support von `[-R,R]` nach `[-aR,aR]` und liegt damit positiv vom Rand entfernt.

Für festes `a<1` kann anschließend mit einer Standardmollifier `\rho_\varepsilon` und `\varepsilon<(1-a)R` geglättet werden. Im Fourierbild multipliziert Mollifikation mit `\widehat\rho(\varepsilon\xi)\to1`; dominated convergence im gewichteten L2 liefert Formnormkonvergenz, während der Support in `(-R,R)` bleibt.

Damit ist

\[
C_c^\infty(-R,R)
\]

tatsächlich Gamma-formdicht. Wegen der festen Normäquivalenz zwischen Gamma- und `X`-Graphnorm ist es auch `X`-graphdicht. Die bounded odd projection liefert die odd Dichte.

**Befund:** Der Satz ist mathematisch korrekt, aber (R5.1) ist als gegenwärtige Paperbegründung nicht self-contained. Er soll durch (R5.2) und die obige Strong-Continuity-Argumentation ersetzt werden.

\[
\boxed{[\mathrm{R5\text{-}TC0}]\;\checkmark[M]_{\rm statement}\; +\;\times[M]_{\rm current\ self\text{-}contained\ proof}.}
\]

---

# 6. Dense-core reduction

Nach dem Core-Ergebnis ist die Reduktion rein normtheoretisch. Da

\[
\|W_{R,S,-}^{[T]}\|=1,
\]

gilt für `x` und eine Core-Approximation `f`

\[
\|W_Ux-W_Tx\|
\le2\|x-f\|+\|W_Uf-W_Tf\|.
\]

Cauchy convergence auf dem dichten Core erweitert sich daher auf den gesamten odd Graphraum.

\[
\boxed{[\mathrm{R5\text{-}DENSE}]\;\checkmark[M].}
\]

---

# 7. Firewall

Der Block trennt ausdrücklich:

- Divergenz der absoluten `G_{R,T}`;
- mögliche relative Cancellation in `W_{R,S}^{[T]}`;
- fixed-core Cauchy reduction;
- offene asymptotische Square-root-Geometrie.

Es wurde keine implizite Behauptung

\[
K_{R,S}^{T,U}\to I
\]

oder

\[
W_{R,S,-}^{[T]}\text{ strong Cauchy}
\]

gefunden.

\[
\boxed{[\mathrm{R5\text{-}FW}]\;\checkmark[M].}
\]

---

# 8. Referee-Reparatur aus R5

Vor einem vollständigen End-to-End-PASS des Direct-Terminal-Moduls:

1. `DT.25` nicht aus einer im Paper unsichtbaren positiven Serie importieren, sondern Core-Dichte aus `w\asymp\log` wie in §5 beweisen.
2. Einmal `q_{\Gamma,R}` durch die kanonische Notation `\mathfrak c_{\Gamma,R}` ersetzen.

Danach ist für diesen Block kein neuer mathematischer Forschungsinput nötig; nur ein erneuter Referee-Sekundencheck.
