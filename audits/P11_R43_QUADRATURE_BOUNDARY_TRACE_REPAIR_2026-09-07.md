# P11 / R43: Randspur-Reparatur der Schur-Quadratur

Datum: 2026-09-07. Ausgangsstand:
`55a3a1617513cc5d82c47d0cfd606c6b0894c984`.
Dieser Audit dokumentiert einen gefundenen Quellenfehler und seine
konkrete Reparatur. Er gehört zum neuen Wurzelanker-Beweispaket;
keine Registry-Promotion.

## Früherer und korrigierter Stand

Der bisherige obere Beweis behauptete globale Hilbert-Lipschitz-Stetigkeit für
\[
\Phi_T(r)(v)=2k_T^0(v)\alpha(2r-v)
-2\widetilde k_T^0(2r-v)\alpha(v),\qquad k_T^0=k_T-K_T/T.
\]
Die Tilde bezeichnet die Nullfortsetzung von \((0,T)\).
Diese Behauptung ist falsch: Die Nullfortsetzung hat Rand-Sprünge,
die in der dortigen globalen Ableitungsbehauptung fehlen
([betroffene Formeln (6.21a–c)](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L279-L315)).

Wegen des festen Quellträgerabstands ist \(k_T(T)=0\), während
\(k_T^0(T-)=-K_T/T\). Bei \(r=(T+v)/2\) bewegt sich ein echter
Sprung durch den Träger von \(\alpha(v)\). Sein lokaler
\(L^2\)-Translationsmodul hat Größe
\((|K_T|/T)\sqrt{|h|}\), nicht \(O(|h|)\).

Die Reparatur verwendet skalare partielle Integration für jedes
feste \(v\), mit beiden Rand-Sprüngen. Zertifikat, Cutoffs und
vollständiger Rest-Lift bleiben unverändert; der kanonische
LaTeX-Beweis wird im selben Paket korrigiert.

## Vollständige Bilanz der Quadratur-Randspuren

Die vorhandenen Prime-Zellen und positiven Gewichte erfüllen
\[
\delta_I\asymp e^{-\frac45(T-r_I)},\qquad
\sum_{q:r_q\in I}\lambda_q^{(I)}=|I|.
\]
Das sind die ursprünglichen massennormierten Prime-Quadraturgewichte,
keine neuen Gewichte für eine Flagbudget-Summation
([Zellmassen und Kostenidentität](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L233-L278)).

Für \(L_T=(T+\varepsilon)/2\) setze
\[
d\mu_T=\sum_{I,q\in I}\lambda_q^{(I)}\delta_{r_q}
-1_{[0,L_T]}dr,\qquad F_T(r)=\mu_T([0,r]).
\]
Die exakte Zellmassenbilanz gibt bei konsistenter Endpunktzuordnung
\[
F_T=0\text{ an Zellrändern},\qquad
|F_T(r)|\le\delta_I\le Ce^{-\frac45(T-r)}.
\tag{QR1}
\]
Für fast jedes feste \(v\) besteht die Variation von
\(r\mapsto\Phi_T(r)(v)\) aus der regulären Ableitung
\[
4k_T^0(v)\alpha'(2r-v)-4k_T'(2r-v)\alpha(v)
\]
mit dem zweiten regulären Term nur für \(0<2r-v<T\), sowie
den Sprüngen
\[
-2k_T^0(0+)\alpha(v)\text{ bei }r=v/2,\qquad
+2k_T^0(T-)\alpha(v)\text{ bei }r=(T+v)/2.
\tag{QR2}
\]
Koinzidenzen mit den endlich vielen Quadraturatomen betreffen
nur eine Nullmenge von \(v\). Partielle Integration, danach
\(L^2\) und Minkowski, liefern
\[
\begin{aligned}
\|Z_T^{\mathrm{quad}}\|_2\le{}&
\int_0^{L_T}|F_T(r)|\|\partial_r\Phi_{T,\mathrm{reg}}(r)\|_2\,dr\\
&+2|k_T^0(0+)|\,\|\alpha(v)F_T(v/2)\|_2\\
&+2|k_T^0(T-)|\,\|\alpha(v)F_T((T+v)/2)\|_2.
\end{aligned}
\tag{QR3}
\]
Die feste Identifikation vom halben \(b\)-Raum zum geraden
Terminalraum ändert nur eine Abschätzungskonstante.
Dies ist keine Behauptung von Hilbert-BV-Regularität.

Aus dem vorhandenen Kernelbound folgt auf \(0\le r\le T/2\),
bis auf feste \(\varepsilon\)-Verschiebungen,
\[
\|\partial_r\Phi_{T,\mathrm{reg}}(r)\|_2
\le C_f\frac{e^{(T-2r)/2}}{\sqrt{1+T-2r}}
+C_\alpha |K_T|/T.
\]
Der wachsende Anteil verschwindet auf dem verbleibenden festen
Streifen oberhalb \(T/2\) durch \(a_*>\rho_f+2\varepsilon\)
([Kernelbound und Trägerabstand](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L94-L153)).
Die Exponenten im ersten Integranden ergeben
\(e^{-3T/10-r/5}\), mit beschränktem \(r\)-Integral.
Der konstante Teil ist durch \(C_\alpha |K_T|T^{-1}e^{-2T/5}\)
kontrolliert.

Auf dem festen Träger von \(\alpha\) gelten außerdem
\[
|F_T(v/2)|\le Ce^{-4T/5},\qquad
|F_T((T+v)/2)|\le Ce^{-2T/5},
\]
\[
|k_T^0(0+)|\le C_fe^{T/2}/\sqrt T+|K_T|/T,\qquad
|k_T^0(T-)|=|K_T|/T.
\]
Damit einschließlich beider Randspuren
\[
\boxed{\|Z_T^{\mathrm{quad}}\|_2
\le C_fe^{-3T/10}
+C_\alpha\frac{|K_T|}{T}e^{-2T/5}.}
\tag{QR4}
\]

## Kosten, voller Rest und beide benötigten Fehlerskalen

Die Zertifikatskosten hängen von \(C_T^-(r,\cdot)\), nicht
von einer falschen Ableitung des reflektierten \(\Phi_T\), ab.
Die feste Unterstützung von \(\alpha\) liefert mit \(u=\min(2r,T)\)
\[
\|C_T^-(r,\cdot)\|_2^2
\le C_f\left(\frac{e^{T-u}}{1+T-u}+\frac{|K_T|^2}{T^2}\right).
\]
Positive Massenkostenidentität und Teilung des Integrals bei \(T/4\)
geben unverändert
\[
\|Y_T^{\mathrm{prim},-}\|^2
\le C_f\left(T^{-1}+Te^{-T/4}
+\frac{|K_T|^2}{T^2}e^{-T/2}\right).
\tag{QR5}
\]
Die vorhandene Hebung in die echte \(a=0\)-Zeile behält sämtliche
höheren Potenzen. Ihr zusätzlicher Tailoperator hat Norm
\(O(\sqrt{T+1}e^{-T/2})\); primitive Formdominanz wird nicht benutzt
([vollständiger Rest-Lift](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L317-L359)).

- **Scharfe feste Quellenergie:** Bei festem endlichem ersten Jet \(m\)
  ist \(M_T^{\mathrm{cost}}=|K_T|^2/(2T)\asymp e^T/T^{2m+2}\).
  QR4 ist \(o(\sqrt{M_T^{\mathrm{cost}}})\), QR5 ist
  \(o(M_T^{\mathrm{cost}})\). Der obere Squeeze und insbesondere
  der scharfe \(m=0\)-Koeffizient eins bleiben erhalten.
- **Absolute Near-null-Quadratur:** In der betroffenen festen
  glatten Near-null-Familie aus R16 gilt \(K_T=O(\sqrt T)\),
  mit uniformer Kernelkonstante. QR4 ergibt dann tatsächlich
  \(Z_T^{\mathrm{quad}}=o(1)\), QR5 ergibt
  \(\|Y_T^{\mathrm{prim},-}\|^2=o(1)\)
  ([R16, kleine Masse und absolute Quadratur](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R16_TC1_NEARNULL_REMAINDER_2026-08-14.md#L99-L158)).
- **Feste Profilabsorption:** In R17 ist
  \(k_g^{(U)}(t)=2g(U-t)\) für festes glattes gerades \(g\)
  mit Mittelwert null. Die untere Spur ist für große \(U\)
  null, die obere ist \(2g(0)\) und nicht allgemein null.
  Der reguläre Ableitungsteil ist uniform beschränkt und in
  einem Streifen fester Breite um \(U/2\) getragen. QR1–QR3
  geben daher einschließlich der oberen Spur den absoluten
  Fehler \(O_g(e^{-2U/5})\). Auch diese nachgelagerte
  schriftliche Ableitungsbegründung wird explizit berichtigt
  ([R17, feste Profilabsorption](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_O3p_Vanishing_NearNull_Core.tex#L96-L145)).

Die frühere globale Hilbert-Lipschitzbehauptung wird zurückgenommen.
QR1–QR5 ersetzen sie mit beiden bilanzierten Randspuren und
reparieren die konkret betroffenen absoluten R16-/R17-Fehlerkanäle
ebenso wie die relative scharfe Quellenergie. Dies ist keine
pauschale neue Zertifizierung der gesamten älteren Auditkette.
