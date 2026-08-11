# P11-O3d-PRECHECK — Primitive Form-Domination Firewall vor dem Odd Matching Upper Bound

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3d-PRECHECK]`  
**Vorgänger:** O3b-SYNC, O3c  
**Schnittstellen:** C1r, C1z-B, C1z-B1, C5a, C5c, C5d, O3a, O3b  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, keine Residualroute, kein SYN, kein Seal.

---

## 0. Urteil

Der geplante O3d-Matching-Upper-Bound darf **noch nicht** über die primitive C5c/C5d-Dualroute gebucht werden.

Der Grund ist eine ältere, bislang nicht separat bewiesene Formordnung in C5d:

\[
\boxed{
R_T^*R_T\ge (R_T^{(1)})^*R_T^{(1)}.
}
\tag{PRE.1}
\]

C5d benutzt (PRE.1), um ein Dualzertifikat für den primitiven Rest `R_T^(1)` unmittelbar als Upper-Bound-Zertifikat für den vollständigen Feshbach-Nenner zu verwenden.

Aus den verbindlichen C1r/C1z-B-Definitionen folgt (PRE.1) jedoch **nicht automatisch**: Die verschiedenen Prime-Power-Beiträge `k=1,2,...` eines festen Primkanals landen kohärent im selben BC-Restsektor `K_p^0` und sind dort nicht orthogonal.

Der vorliegende Knoten beweist deshalb zwei Dinge:

1. die bisherige automatische Begründung von (PRE.1) ist unzulässig;
2. die tatsächliche Wahrheit oder Falschheit von (PRE.1) bleibt ein neues offenes Problem.

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3d\text{-}PRECHECK]
&\quad \checkmark[M]_{\rm k\text{-}cross\text{-}terms\;nonorthogonal}\\
&+\checkmark[M]_{\rm cross\text{-}term\;sign\;indefinite\;at\;source\;level}\\
&+\checkmark[M]_{\rm automatic\;primitive\;domination\;invalid}\\
&+?[O]_{R_T^*R_T\ge(R_T^{(1)})^*R_T^{(1)}}\\
&+?[O]_{\rm C5d\;full\text{-}rest\;upper\;transfer\;repair}\\
&+?[O]_{\rm O3d\;matching\;odd\;upper\;bound}.
\end{aligned}
}
\]

**Wichtig:** Dies ist kein Gegenbeweis gegen (PRE.1). Es ist ein harter Proof-Gap gegen seine bisherige automatische Verwendung.

---

# 1. Verbindliche Restgeometrie aus C1r/C1z-B

Für eine feste Primzahl `p` besitzt der BC-Restsektor die kanonische ONB

\[
\{\psi_{p,j}:j\ge0\}
\]

und

\[
\boxed{
\eta_{p,k}
=\sqrt{p-1}\sum_{j=0}^{k-1}p^{(j-k)/2}\psi_{p,j}.
}
\tag{PRE.2}
\]

Die source-gekoppelte Konditionierung wirkt durch

\[
\boxed{
\mathsf Q_T(u)\psi_{p,j}
=1_{\{j<J_{p,T}(u)\}}\psi_{p,j}.
}
\tag{PRE.3}
\]

Damit

\[
\boxed{
\mathsf Q_T(u)\eta_{p,k}
=\sqrt{p-1}
\sum_{j=0}^{\min(k-1,J_{p,T}(u)-1)}
 p^{(j-k)/2}\psi_{p,j}.
}
\tag{PRE.4}
\]

Der vollständige Restoperator lautet schematisch

\[
\boxed{
R_Te(u)
=
\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Te(u)
\otimes
\mathsf Q_T(u)\eta_{p,k}.
}
\tag{PRE.5}
\]

Verschiedene `p`-Sektoren sind orthogonal. Verschiedene `k` innerhalb desselben `p`-Sektors sind es im Allgemeinen **nicht**.

---

# 2. Explizite Nichtorthogonalität von `k=1` und `k=2`

Auf jeder Source-Zone mit

\[
J_{p,T}(u)\ge1
\]

gilt

\[
\mathsf Q_T(u)\eta_{p,1}
=\sqrt{p-1}\,p^{-1/2}\psi_{p,0}.
\tag{PRE.6}
\]

Für `k=2` gilt bereits bei `J=1`

\[
\mathsf Q_T(u)\eta_{p,2}
=\sqrt{p-1}\,p^{-1}\psi_{p,0},
\tag{PRE.7}
\]

und bei `J\ge2`

\[
\mathsf Q_T(u)\eta_{p,2}
=\sqrt{p-1}
\bigl(p^{-1}\psi_{p,0}+p^{-1/2}\psi_{p,1}\bigr).
\tag{PRE.8}
\]

In beiden Fällen ist

\[
\boxed{
\left\langle
\mathsf Q_T(u)\eta_{p,1},
\mathsf Q_T(u)\eta_{p,2}
\right\rangle
=(p-1)p^{-3/2}\ne0.
}
\tag{PRE.9}
\]

Damit ist der primitive `k=1`-Restkanal **kein orthogonaler Summand** des vollen `p`-Restkanals.

Dies allein blockiert bereits die naive Folgerung

\[
\|R_Te\|^2
\ge
\|R_T^{(1)}e\|^2
\]

aus einer vermeintlichen Pythagoras-Zerlegung.

---

# 3. Die Kreuzterme besitzen kein festes Vorzeichen

Schreibe für einen festen Primkanal formal

\[
R_{T,p}e
=V_{p,1}e+V_{p,\ge2}e.
\]

Dann

\[
\boxed{
\|R_{T,p}e\|^2
=
\|V_{p,1}e\|^2
+\|V_{p,\ge2}e\|^2
+2\operatorname{Re}
\langle V_{p,1}e,V_{p,\ge2}e\rangle.
}
\tag{PRE.10}
\]

Wegen (PRE.9) enthält bereits der `k=1`/`k=2`-Kreuzterm einen Source-Faktor proportional zu

\[
\operatorname{Re}
\left\langle
D_{\log p}E_Te,
D_{2\log p}E_Te
\right\rangle
\]

auf Zonen, auf denen beide konditionierten BC-Vektoren überleben.

Im unbeschnittenen Inneren haben die beiden Translationsdifferenzen auf einer Fouriermode `e^{i\xi u}` die Multiplikatoren

\[
2i\sin\left(\frac{\xi\log p}{2}\right),
\qquad
2i\sin(\xi\log p).
\]

Deren reelles Produkt ist proportional zu

\[
\sin\left(\frac{\xi\log p}{2}\right)
\sin(\xi\log p)
=
2\sin^2\left(\frac{\xi\log p}{2}\right)
\cos\left(\frac{\xi\log p}{2}\right),
\tag{PRE.11}
\]

und wechselt mit dem Kosinus das Vorzeichen.

Durch glatte, im Source-Inneren lokalisierte Wellenpakete kann dieselbe Vorzeichenindefinitheit auf finite Source-Level übertragen werden, solange die betrachteten Translationen nicht vom Rand abgeschnitten werden.

Daher gilt:

\[
\boxed{
\text{die }k=1/k\ge2\text{-Kreuzterme sind nicht strukturell nichtnegativ.}
}
\tag{PRE.12}
\]

Dies beweist **nicht**, dass die Gesamtdifferenz

\[
R_T^*R_T-(R_T^{(1)})^*R_T^{(1)}
\]

tatsächlich einen negativen Eigenwert besitzt. Es beweist aber, dass eine solche Positivität einen eigenen globalen Satz benötigt.

---

# 4. Audit von C5d

C5d setzt in seiner verbindlichen Feshbach-Dualform ausdrücklich

\[
R_T^*R_T\ge(R_T^{(1)})^*R_T^{(1)}
\tag{PRE.13}
\]

und folgert daraus, dass ein primitives Dualzertifikat

\[
h_{T,f}=(R_T^{(1)})^*Y_T+Z_T
\]

direkt

\[
\sigma_T(Jf)
\le\|Y_T\|^2+\|Z_T\|^2
\]

für den vollen Schurterm liefert.

Im committed C5d steht an dieser Stelle kein separater Beweis von (PRE.13). Wegen §§2--3 kann (PRE.13) auch nicht allein aus

- der Orthogonalität verschiedener Primsektoren,
- der Positivität der einzelnen Restgewichte,
- oder der Existenz des primitiven `k=1`-Kanals

gefolgert werden.

Daher wird der Transfer

\[
\boxed{
\text{primitive certificate}\Rightarrow\text{full-rest Schur upper bound}
}
\tag{PRE.14}
\]

bis zu einem neuen Beweis von (PRE.13) oder einem alternativen Full-Rest-Dualzertifikat als **offen** gefirewallt.

---

# 5. Rückwirkung auf C1z-B1

C1z-B1 benutzt bei seiner damaligen Restdivergenz-Untergrenze ebenfalls die Idee, aus dem vollen Rest direkt die primitive `k=1`-Masse positiv herauszuziehen.

Wegen derselben inner-prime `k`-Kreuzterme ist auch eine solche Untergrenze nicht allein durch die Kreuzprimorthogonalität gerechtfertigt.

Dies betrifft **nicht** die Definition von `R_T`, die finite-Level-Beschränktheit oder die Feshbach-Konstruktion selbst. Es betrifft nur Aussagen, die eine positive Dominanz des vollen Restes über einen ausgewählten `k`-Teil benötigen.

Status:

\[
\boxed{
\text{C1z-B1 primitive lower extraction: RE-AUDIT REQUIRED.}
}
\tag{PRE.15}
\]

---

# 6. Was sicher bestehen bleibt

Der neue Befund berührt nicht:

1. die C1r-Martingalbasis;
2. die exakte C1z-B-Konditionierungsformel;
3. die C3/C4-Variationsuntergrenze, die mit dem **vollen** Nenner arbeitet;
4. O3c, denn dort wurde `R_T1_T` direkt als voller Restvektor abgeschätzt und keine primitive Formdominanz benutzt;
5. den verifizierten O3c-Satz
   \[
   \sup_T\|R_T1_T\|^2<\infty,
   \qquad
   \langle1_T,A_T1_T\rangle=2T+O(1);
   \]
6. das verschärfte odd Lower Certificate
   \[
   \sigma_T(Jf_-)
   \gtrsim
   e^T/T^{2m+2};
   \]
7. O3b.1 als reine Aussage über die Kosten **jeder angenommenen primitiven Dualzerlegung**; seine Beweisform benötigt keine Behauptung, dass ein solches Zertifikat den vollen Schurterm upper-bounded.

---

# 7. Aussagen mit Dependency-Risk

Bis zur Klärung von (PRE.13) dürfen folgende Resultate nicht als durch die bisherige primitive-Dominanz-Route abgeschlossen behandelt werden:

\[
\boxed{
\begin{aligned}
&\text{C5d full-rest even-core Schur upper/tail decay},\\
&\text{C5d daraus abgeleitete even-core Form-Cauchy/Mosco-Folgerungen},\\
&\text{jede spätere Aussage, die C5d gerade Terminalbeschränktheit wesentlich benutzt},\\
&\text{O3d primitive matching upper bound für odd }f_-.
\end{aligned}
}
\tag{PRE.16}
\]

Dies ist zunächst eine **Dependency-Firewall**, keine pauschale Widerlegung dieser Sätze.

Insbesondere wird in diesem PRECHECK noch kein historischer Status rückwirkend überschrieben. Nach adversarial Countercheck ist zu entscheiden, welche Statuszeilen formal gepatcht werden müssen.

---

# 8. Die zwei zulässigen Reparaturrouten

## Route A — Formdomination wirklich beweisen

Zeige direkt

\[
\boxed{
R_T^*R_T-(R_T^{(1)})^*R_T^{(1)}\ge0
}
\tag{PRE.17}
\]

unter Einbeziehung **aller** inner-prime `k`-Kreuzterme und der source-abhängigen Konditionierung.

Wegen (PRE.9)--(PRE.12) ist dies kein formaler Einzeiler, sondern ein echter Positivitätssatz.

## Route B — Full-Rest-Dualzertifikat

Verzichte vollständig auf (PRE.17) und konstruiere das Dualzertifikat direkt für

\[
R_T
\]

statt für `R_T^(1)`.

Für O3d ist Route B konzeptionell besonders natürlich: O3c hat bereits gezeigt, dass die **volle** nichtprimitive Restgeometrie auf der Konstantenmode überraschend gut kontrolliert ist.

---

# 9. O3d-Status nach dem PRECHECK

Der signed-Future-Edge-Ansatz für odd `f_-` bleibt mathematisch attraktiv:

- der even Terminalsektor erzeugt signed reflection edges
  \[
  b(t)-b(2r-t);
  \]
- nach Abspaltung eines Residualprofils `q_T` mit
  \[
  \int q_T=1,
  \qquad
  \|q_T\|_2^2=O(T^{-1}),
  \]
  hat der zu screenende Hubkern Mittelwert null;
- die unvermeidbare Residualkosten-Skala ist dann exakt
  \[
  |\langle h_T,1_T\rangle|^2/T
  \asymp e^T/T^{2m+2}.
  \]

Aber bevor daraus ein Upper Bound für den **vollen** Schurterm gebucht werden darf, muss entweder Route A oder Route B geschlossen werden.

Daher:

\[
\boxed{
[P11\text{-}O3d]\quad ?[O]_{\rm matching\ odd\ upper\ bound}
}
\]

bleibt vorerst offen.

---

# 10. Gesamtfirewall

\[
\boxed{
\texttt{O3c VERIFIED / PRIMITIVE FORM DOMINATION UNPROVEN / O3d BLOCKED ON REPAIR}
}
\]

und weiterhin

\[
\boxed{
\texttt{NO O4 / NO SYN / NO SEAL / ORIGINAL ODD TRANSPORT OPEN}.
}
\]
