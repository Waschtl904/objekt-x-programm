# P11 END-TO-END REFEREE AUDIT — R2: FINITE-WINDOW SCHATTEN NO-GO

**Datum:** 2026-08-13  
**Paper:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`  
**Knoten:** Theorem `thm:schatten`, Gleichung (3.7)  
**Auditmodus:** End-to-End-Referee; historische Audits nicht als Beweisinput verwendet.

---

## 0. Behauptung

Für

\[
R>\frac12\log2
\]

setzt das Paper

\[
K_R=C_{\Gamma,R}^{-1/2}H_R,
\qquad
S_R=K_RB_RK_R^*,
\qquad
B_R=(I+R_R^*R_R)^{-1},
\]

und behauptet

\[
\boxed{S_R\in\mathcal K}
\]

aber

\[
\boxed{S_R\notin\mathcal S_p\quad\text{für jedes endliche }p\ge1.}
\tag{R2.1}
\]

---

# 1. Kompaktheit

Aus dem endlichen Gamma-Fenster folgt

\[
C_{\Gamma,R}^{-1}\in\mathcal K.
\]

Für den positiven kompakten Operator `C_{\Gamma,R}^{-1}` ist auch

\[
C_{\Gamma,R}^{-1/2}
=(C_{\Gamma,R}^{-1})^{1/2}
\in\mathcal K.
\]

Da `H_R` und `B_R` bei festem `R` beschränkt sind,

\[
K_R=C_{\Gamma,R}^{-1/2}H_R\in\mathcal K
\]

und somit

\[
S_R=K_RB_RK_R^*\in\mathcal K.
\]

Status:

\[
\boxed{[\mathrm{R2\text{-}K}]\;\checkmark[M].}
\]

---

# 2. Lokalisierte Fourierfamilie

Wähle ein Intervall

\[
I=[a,a+L]\Subset(-R,R)
\]

und

\[
e_m(u)=L^{-1/2}1_I(u)e^{2\pi imu/L}.
\]

Dann ist `(e_m)` orthonormal, denn für `m\ne n`

\[
\int_I e^{2\pi i(m-n)u/L}du=0.
\]

Für ein Intervall `J` und Frequenz `\omega` gilt

\[
|\widehat{1_Je^{i\omega\cdot}}(\xi)|^2
\lesssim_J
\min\{1,|\xi-\omega|^{-2}\}.
\]

Mit

\[
m_\Gamma(\xi)\asymp\log(2+|\xi|)
\]

und

\[
\log(2+|\omega+\eta|)
\lesssim
\log(2+|\omega|)+\log(2+|\eta|)
\]

folgt

\[
\boxed{
\mathfrak c_{\Gamma,R}[e_m]
\le C_I\log(2+m).
}
\tag{R2.2}
\]

Status:

\[
\boxed{[\mathrm{R2\text{-}FOURIER}]\;\checkmark[M].}
\]

---

# 3. Inverse-Gamma-Lower-Bound

Für einen positiven Operator `C\ge I` und einen Vektor im Formbereich gilt

\[
\|f\|^2
=|\langle C^{-1/2}f,C^{1/2}f\rangle|
\le
\|C^{-1/2}f\|\,\|C^{1/2}f\|.
\]

Also

\[
\langle C^{-1}f,f\rangle\,\mathfrak c_C[f]
\ge\|f\|^4.
\tag{R2.3}
\]

Mit (R2.2) ergibt dies

\[
\|C_{\Gamma,R}^{-1/2}e_m\|^2
\gtrsim
\frac1{\log(2+m)}.
\]

Die im Paper verwendete Ungleichung ist daher im Form-Sinn korrekt; eine Operator-Domain-Annahme ist nicht nötig.

Status:

\[
\boxed{[\mathrm{R2\text{-}INV}]\;\checkmark[M].}
\]

---

# 4. Isolierte primitive `p=2`-Translationskopie

Bei festem `R` enthält

\[
H_R=P_R\sum_{p^k\le e^{2R}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_R
\]

nur endlich viele Shiftlängen

\[
\mathcal A_R
:=\left\{\pm\frac{k}{2}\log p:p^k\le e^{2R}\right\}.
\]

Da

\[
a_2:=\frac12\log2<R
\]

und `a_2` in dieser endlichen Menge von jeder anderen Shiftlänge verschieden ist, ist

\[
\delta_R:=\min\{|a_2-a|:a\in\mathcal A_R,\ a\ne a_2\}>0
\]

(wenn keine andere Länge vorhanden ist, ist die Trennung trivial).

Wähle `I` um `0` so klein, dass

\[
|I|<\delta_R/3,
\qquad
I+a_2\Subset(-R,R).
\]

Dann gibt es auf `I+a_2` genau eine aktive Kopie des lokalisierten Vektors: die gewählte primitive `p=2`-Translation. Alle anderen verschobenen Supports sind disjunkt. Daher

\[
\boxed{
\|H_Re_m\|_2\ge c_R>0
}
\tag{R2.4}
\]

uniform in `m`.

Da `H_Re_m` eine **endliche** Linearkombination von verschobenen bzw. an den Fenstergrenzen abgeschnittenen Intervall-Fourierfunktionen mit derselben Frequenzordnung ist, liefert die Rechnung aus §2

\[
\boxed{
\mathfrak c_{\Gamma,R}[H_Re_m]
\le C_R\log(2+m).
}
\tag{R2.5}
\]

Damit folgt aus (R2.3)

\[
\boxed{
\|K_Re_m\|^2
=\|C_{\Gamma,R}^{-1/2}H_Re_m\|^2
\gtrsim_R
\frac1{\log(2+m)}.
}
\tag{R2.6}
\]

Status:

\[
\boxed{[\mathrm{R2\text{-}ISOLATION}]\;\checkmark[M].}
\]

---

# 5. Orthonormalfamilientest für `\mathcal S_q`

Dies ist der erste potentielle Hochrisikosprung im Paper.

Angenommen

\[
K_R\in\mathcal S_q,
\qquad q\ge2.
\]

Setze

\[
A:=K_R^*K_R\ge0,
\qquad r:=q/2\ge1.
\]

Für jeden Einheitsvektor `e` gilt durch Jensen für die Spektralmaße

\[
\langle Ae,e\rangle^r
\le\langle A^re,e\rangle.
\]

Für jede orthonormale Familie `(e_m)` folgt daher

\[
\sum_m\|K_Re_m\|^q
=
\sum_m\langle Ae_m,e_m\rangle^{q/2}
\le
\sum_m\langle A^{q/2}e_m,e_m\rangle
\le
\operatorname{Tr}(A^{q/2})
<\infty.
\tag{R2.7}
\]

Dies widerspricht (R2.6), weil

\[
\sum_m(\log(2+m))^{-q/2}=\infty.
\]

Also

\[
K_R\notin\mathcal S_q
\qquad(q\ge2).
\]

Für `0<q<2` folgt dasselbe aus

\[
\mathcal S_q\subset\mathcal S_2.
\]

Status:

\[
\boxed{[\mathrm{R2\text{-}ONF}]\;\checkmark[M].}
\]

---

# 6. Vom `K_R`-No-Go zum `S_R`-No-Go

Wegen

\[
0\le R_R^*R_R\le\|R_R\|^2I
\]

gilt

\[
B_R=(I+R_R^*R_R)^{-1}
\ge
\beta_RI,
\qquad
\beta_R=(1+\|R_R\|^2)^{-1}>0.
\]

Damit

\[
S_R=K_RB_RK_R^*
\ge
\beta_RK_RK_R^*.
\tag{R2.8}
\]

Für positive kompakte Operatoren liefert das Min-Max-Prinzip

\[
\lambda_n(S_R)
\ge
\beta_R\lambda_n(K_RK_R^*).
\]

Wäre `S_R\in\mathcal S_p` für ein endliches `p\ge1`, dann wäre daher auch

\[
K_RK_R^*\in\mathcal S_p.
\]

Die Singulärwerte erfüllen

\[
s_n(K_RK_R^*)=s_n(K_R)^2,
\]

also

\[
K_R\in\mathcal S_{2p},
\]

im Widerspruch zu §5.

Status:

\[
\boxed{[\mathrm{R2\text{-}TRANSFER}]\;\checkmark[M].}
\]

---

# 7. Scope-Firewall

Der Satz widerlegt nur finite Schattenordnung der **konkreten** endlichen Gamma-preconditioned Feshbach-Geometrie. Der anschließende Remark verweigert ausdrücklich den Schluss auf ein globales Object-X-No-Go oder auf die Unmöglichkeit eines anderen Fredholm-Mechanismus.

Kein unzulässiger Schluss auf den starken Terminaltransport wurde gefunden.

Status:

\[
\boxed{[\mathrm{R2\text{-}FW}]\;\checkmark[M].}
\]

---

# 8. Gesamturteil

Der End-to-End-Gegencheck findet keinen mathematischen Defekt in Theorem `thm:schatten`.

\[
\boxed{
[\mathrm{P11\text{-}R2\text{-}SCHATTEN}]
=\checkmark[M].
}
\]

Der Paperbeweis ist an zwei Stellen knapp (Intervallisolation und Orthonormalfamilientest), aber beide Schritte folgen direkt aus den im Paper definierten Objekten und benötigen keine historische Auditdatei als mathematischen Input.

**Referee-Ergebnis:** PASS.

Nächster unabhängiger Hochrisikoknoten: `thm:mosco` (Mosco/strong-resolvent Gamma limit), insbesondere die form-norm dichte Kompaktsupportapproximation und die Behauptung, dass die finite-window inverses die variational projections liefern.
