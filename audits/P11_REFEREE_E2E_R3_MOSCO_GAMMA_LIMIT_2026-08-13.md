# P11 END-TO-END REFEREE AUDIT — R3: MOSCO / STRONG-RESOLVENT GAMMA LIMIT

**Datum:** 2026-08-13  
**Paper:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`  
**Knoten:** Theorem `thm:mosco`, Gleichungen (3.14)--(3.15)  
**Auditmodus:** End-to-End-Referee.

---

## 0. Behauptung

Auf `L^2(\mathbb R)` sei

\[
q_\Gamma(f)
=\frac1{2\pi}\int m_\Gamma(\xi)|\widehat f(\xi)|^2d\xi,
\qquad
m_\Gamma(\xi)\asymp\log(2+|\xi|),
\]

und

\[
\mathcal V_R
=\mathcal D(q_\Gamma)\cap\{f:\operatorname{supp}f\subset[-R,R]\}.
\]

Das Paper behauptet

\[
\Phi_R\xrightarrow[M]{}q_\Gamma
\]

und

\[
E_RC_{\Gamma,R}^{-1}P_R
\xrightarrow[s]{}
C_\Gamma^{-1},
\]

aber keine Normkonvergenz.

---

# 1. Formdichte der kompaktsupportierten Räume

`\mathcal V_R` ist monoton wachsend. Es bleibt zu zeigen, dass

\[
\overline{\bigcup_R\mathcal V_R}^{\|\cdot\|_{q_\Gamma}}
=\mathcal D(q_\Gamma).
\]

Im Fourierbild ist die Formdomäne das gewichtete Hilbertraum-L2

\[
L^2(\mathbb R,m_\Gamma(\xi)d\xi).
\]

Glatte kompakt unterstützte Fourierfunktionen sind dort dicht; ihre inversen Fouriertransformierten sind Schwartz. Für eine Schwartzfunktion `\phi` wähle glatte physikalische Cutoffs `\chi_R` mit `\chi_R=1` auf `[-R,R]` und setze `\phi_R=\chi_R\phi`.

Da für jedes feste `\varepsilon>0`

\[
m_\Gamma(\xi)
\lesssim_\varepsilon
(1+|\xi|^2)^\varepsilon,
\]

reicht z.B. Konvergenz in einem festen Sobolevraum `H^1`. Für Schwartz-`\phi` gilt

\[
\|(1-\chi_R)\phi\|_{H^1}\to0,
\]

also auch

\[
q_\Gamma[\phi_R-\phi]\to0.
\]

Damit ist die behauptete Formdichte korrekt.

Status:

\[
\boxed{[\mathrm{R3\text{-}DENS}]\;\checkmark[M].}
\]

---

# 2. Mosco-liminf und Recovery

Die abgeschlossene positive quadratische Form `q_\Gamma` ist als konvexe norm-lower-semicontinuous Funktion auch schwach lower semicontinuous.

Wenn

\[
f_R\rightharpoonup f
\]

in `L^2` und `\liminf\Phi_R(f_R)<\infty`, dann nach Auswahl einer Teilfolge `f_R\in\mathcal V_R` und

\[
q_\Gamma(f)
\le\liminf q_\Gamma(f_R)
=\liminf\Phi_R(f_R).
\]

Dies ist Mosco-liminf.

Die in §1 bewiesene Formdichte liefert für jedes `f\in\mathcal D(q_\Gamma)` eine Folge

\[
f_n\in\mathcal V_{R_n},
\qquad
f_n\to f
\]

im Formnorm. Durch monotone Wahl des Indexes für alle `R\ge R_n` erhält man eine Recovery-Familie.

Status:

\[
\boxed{[\mathrm{R3\text{-}MOSCO}]\;\checkmark[M].}
\]

---

# 3. Variationale Projektion

Sei

\[
u:=C_\Gamma^{-1}h.
\]

Dann charakterisiert die Formdarstellung `u` durch

\[
q_\Gamma(u,v)=\langle h,v\rangle
\qquad
(v\in\mathcal D(q_\Gamma)).
\tag{R3.1}
\]

Setze

\[
u_R:=E_RC_{\Gamma,R}^{-1}P_Rh\in\mathcal V_R.
\]

Die finite-window Variationsgleichung lautet für jedes `v\in\mathcal V_R`

\[
q_\Gamma(u_R,v)
=\langle P_Rh,P_Rv\rangle_{L^2(-R,R)}
=\langle h,v\rangle.
\tag{R3.2}
\]

Aus (R3.1)--(R3.2):

\[
\boxed{
q_\Gamma(u-u_R,v)=0
\qquad(v\in\mathcal V_R).
}
\tag{R3.3}
\]

Somit ist `u_R` exakt die `q_\Gamma`-orthogonale Projektion von `u` auf `\mathcal V_R`.

Da die geschlossenen Unterräume `\mathcal V_R` im Formhilbertraum monoton wachsen und ihre Vereinigung dicht ist,

\[
\|u_R-u\|_{q_\Gamma}\to0.
\]

Insbesondere

\[
\|u_R-u\|_2\to0.
\]

Damit ist (3.15) direkt bewiesen; es ist kein zusätzlicher abstrakter Resolvent-Satz nötig.

Status:

\[
\boxed{[\mathrm{R3\text{-}RES}]\;\checkmark[M].}
\]

---

# 4. Kein Norm-Resolvent-Limit

Für jedes feste `R` ist

\[
E_RC_{\Gamma,R}^{-1}P_R
\]

kompakt, sobald die finite-window Gamma-Einbettung kompakt ist.

Im Fourierbild ist dagegen

\[
C_\Gamma^{-1}
\cong M_{m_\Gamma^{-1}}.
\]

Da `m_\Gamma^{-1}` auf einer Menge positiven Maßes von Null weg beschränkt ist, ist dieser Multiplikationsoperator auf dem nichtatomaren `L^2(\mathbb R)` nicht kompakt: auf einer solchen Menge kann eine unendliche orthonormale Folge gewählt werden, deren Bilder keine normkonvergente Teilfolge besitzen.

Ein Operatornormlimit kompakter Operatoren wäre kompakt. Daher ist

\[
\boxed{
\|E_RC_{\Gamma,R}^{-1}P_R-C_\Gamma^{-1}\|\not\to0.
}
\]

Status:

\[
\boxed{[\mathrm{R3\text{-}NONNORM}]\;\checkmark[M].}
\]

---

# 5. Nebenbefund: `prop:gamma` ist wahr, aber im Paper unbegründet

Das Paper verwendet zuvor die Proposition, dass die finite-window Gamma-Formdomäne kompakt in `L^2(-R,R)` einbettet, gibt dort aber keinen Beweis.

Die Aussage lässt sich paperintern kurz beweisen. Für eine im Gamma-Formnorm beschränkte Folge mit Support in `[-R,R]` gilt für große `M`

\[
\int_{|\xi|>M}|\widehat f(\xi)|^2d\xi
\le
\frac{C}{\inf_{|\xi|>M}m_\Gamma(\xi)}
\to0
\]

uniform. Ferner

\[
\|\tau_hf-f\|_2^2
=\frac1{2\pi}\int|e^{ih\xi}-1|^2|\widehat f(\xi)|^2d\xi
\]

wird durch Frequenzsplit uniform klein für `h\to0`. Räumliche Tightness ist wegen des festen Supports automatisch. Kolmogorov--Riesz liefert relative Kompaktheit.

Daher ist die Proposition mathematisch korrekt, sollte für den finalen Paper-Self-Containment-Stand aber einen kurzen Beweis erhalten.

Status:

\[
\boxed{[\mathrm{R3\text{-}GAMMA\text{-}COMPACT}]\;\checkmark[M]_{\rm statement},\quad\times[M]_{\rm paper\ proof\ omission}.}
\]

Dieser Nebenbefund ändert den mathematischen PASS von Theorem `thm:mosco` nicht, gehört aber in den Referee-Reparaturbatch.

---

# 6. Firewall

Der anschließende Remark sagt ausdrücklich, dass der reine Gamma-Grenzübergang nicht den großen `R`-Grenzübergang der vollen Prime/Rest-Schur-Geometrie kontrolliert.

Keine implizite Aussage über

\[
K_{R,S}^{T,U}\to I
\]

oder starken Terminaltransport wurde gefunden.

\[
\boxed{[\mathrm{R3\text{-}FW}]\;\checkmark[M].}
\]

---

# 7. Gesamturteil

\[
\boxed{
[\mathrm{P11\text{-}R3\text{-}MOSCO}]
=\checkmark[M].
}
\]

**Referee-Ergebnis:** PASS für Theorem `thm:mosco`.

Offene Paper-Reparatur außerhalb des Satzes: kurzer Beweis von `prop:gamma`.

Nächster Referee-Block: graph transitions / pullback / finite-terminal isometry und insbesondere Prüfung, ob die Operatoren `G_{R,T}` wirklich in den angegebenen Hilberträumen korrekt adjungiert und invertiert werden.
