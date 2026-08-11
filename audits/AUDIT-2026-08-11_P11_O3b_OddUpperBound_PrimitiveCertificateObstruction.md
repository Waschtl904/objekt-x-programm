# P11-O3b — Odd-Source-Upper-Bound-Audit und Primitive-Certificate-Obstruction

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3b]`  
**Vorgänger:** O3a (paritätsreduzierte Konditions-Firewall)  
**Audit-Scope:** C4, C5, C5a, C5b, C5c, C5d  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, keine Residualroute, kein SYN, kein Seal.

---

## 0. Auditstatus

\[
\boxed{
\begin{aligned}
[P11\text{-}O3b]
&\quad \checkmark[M]_{\rm C5d\;dual\;upper\text{-}bound\;machinery\;identified}\\
&+\checkmark[M]_{\rm parity\;scope\;separated}\\
&+\checkmark[M]_{\rm primitive\text{-}certificate\;obstruction\;on\;odd\;source}\\
&+\checkmark[K/M]_{\rm no\;sufficient\;odd\text{-}source\;sharp\;upper\;bound\;in\;audited\;C4\text{-}C5d\;scope}\\
&+?[O]_{\rm full\text{-}rest\;even\text{-}hub\;screening}\\
&+?[O]_{\rm sharp\;odd\;boundary\text{-}jet\;asymptotics}\\
&+?[O]_{\chi^{R,-}_{T,U}\;\rm bounded/divergent}.
\end{aligned}
}
\]

Der zentrale neue Befund ist **nicht** bloß, dass im Altmaterial keine passende odd Obergrenze gefunden wurde. Es gibt eine präzise strukturelle Barriere gegen die direkte Wiederverwendung der C5c/C5d-**primitiven** Dualzertifikatsroute im ungeraden Source-Sektor.

---

# 1. Leitfrage aus O3a

O3a reduzierte die odd Konditionsfrage auf

\[
\rho_{T,U}(f_-)
:=
\frac{\langle G_{R,U}f_-,f_-\rangle}
{\langle G_{R,T}f_-,f_-\rangle},
\]

und

\[
\boxed{
\kappa(A^{R,-}_{T,U})
=
\frac{\sup_{f_-\ne0}\rho_{T,U}(f_-)}
{\inf_{f_-\ne0}\rho_{T,U}(f_-)}.
}
\tag{O3b.1}
\]

C4/C5 liefern für jeden festen nichttrivialen glatten odd Testvektor mit erstem nichtverschwindendem Boundary-Jet

\[
m(f_-):=\min\{m\ge0:\beta_R^{(m)}(f_-)\ne0\}
\]

die Untergrenze

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\ge
c_{R,f_-,m}
\frac{e^T}{T^{2m(f_-)+3}}.
}
\tag{O3b.2}
\]

O3a hat korrekt gefirewallt, dass daraus allein keine Aussage über

\[
\kappa(A^{R,-}_{T,U})
\]

folgt. Gesucht wurde daher im bereits committed C4--C5d-Material eine passende obere Schranke oder Zwei-Seiten-Asymptotik.

---

# 2. Inventar C4/C5: vollständiger odd Jet, aber nur Unterzertifikat

C4 besitzt die exakte Metrikzerlegung

\[
\boxed{
\langle G_{R,T}f,f\rangle
=q_{\Gamma,R}(f)+\sigma_T(J_{R,T}f),
}
\tag{O3b.3}
\]

mit

\[
\sigma_T(g)
=
\langle H_T^*g,A_T^{-1}H_T^*g\rangle,
\qquad
A_T=I+R_T^*R_T.
\]

Für

\[
\mathbf1_T:=1_{(-T,T)}
\]

verwendet C4 die Variationsuntergrenze

\[
\boxed{
\sigma_T(Jf)
\ge
\frac{|\langle Jf,H_T\mathbf1_T\rangle|^2}
{\langle\mathbf1_T,A_T\mathbf1_T\rangle}.
}
\tag{O3b.4}
\]

Die Hubkopplung besitzt bei erstem nichtverschwindendem Jet `m` die scharfe skalare Entwicklung

\[
\boxed{
\langle Jf_-,H_T\mathbf1_T\rangle
=
-\sqrt2\,c_m\beta_R^{(m)}(f_-)
\frac{e^{T/2}}{T^{m+1/2}}
\bigl(1+O(T^{-1})\bigr).
}
\tag{O3b.5}
\]

und C4 benutzt

\[
\langle\mathbf1_T,A_T\mathbf1_T\rangle=O(T^2)
\]

zur Herleitung von (O3b.2).

C5 beweist zusätzlich

\[
\bigcap_{m\ge0}\ker\beta_R^{(m)}
=\mathcal K_{X,R}^{+},
\]

also: jeder nichttriviale glatte odd Testvektor besitzt einen endlichen ersten nichtverschwindenden Jet und divergiert absolut.

**Auditbefund:** C4/C5 liefern damit eine vollständige Hierarchie von **Lower Certificates** auf dem odd Source-Core. Sie liefern jedoch keine obere Kontrolle des vollen Feshbach-Supremums und keine Zwei-Seiten-Asymptotik von `sigma_T`.

Insbesondere ist die vollständige asymptotische Entwicklung in C4 eine Entwicklung der **einen skalaren Kopplung an `1_T`**, nicht des gesamten Schurterms `sigma_T`.

---

# 3. Exakte Paritätsbarriere aus C5/C5a

C5 beweist

\[
H_T^*\mathsf P_T=-\mathsf P_TH_T^*,
\]

also den Paritätswechsel des Hubs.

Damit gilt:

\[
f_+\text{ gerade}
\quad\Longrightarrow\quad
h_{T,f_+}:=H_T^*Jf_+\text{ ungerade},
\]

während

\[
\boxed{
f_-\text{ ungerade}
\quad\Longrightarrow\quad
h_{T,f_-}:=H_T^*Jf_-\text{ gerade}.}
\tag{O3b.6}
\]

C5a formuliert denselben Unterschied ausdrücklich:

- im **ungeraden Source-Sektor** ist `h_T` gerade und koppelt an `1_T`;
- im **geraden Source-Sektor** ist `h_T` ungerade und daher orthogonal zu `1_T`.

Der primitive konditionierte Rest besitzt für genügend großes `T` die exakte Nullmode

\[
\boxed{
\ker R_T^{(1)}=\mathbb C\mathbf1_T,
}
\tag{O3b.7}
\]

insbesondere

\[
R_T^{(1)}\mathbf1_T=0.
\tag{O3b.8}
\]

Genau deshalb ist die C3/C4-Konstantenmode im geraden Source-Kanal blind, im odd Source-Kanal aber der Divergenzdetektor.

---

# 4. Was C5b/C5c/C5d tatsächlich upper-bounded

C5b und C5c lösen das Observability-/Prime-Frame-Problem für einen **festen glatten geraden alten/source Test** `f_+`. Der zugehörige Hubvektor ist ungerade, und das Variationsproblem läuft auf dem ungeraden Terminal-Source-Sektor.

C5d macht daraus eine echte Feshbach-Obergrenze. Für

\[
h_{T,f}=H_T^*Jf
\]

gilt allgemein die Dualform

\[
\boxed{
\sigma_T(Jf)
=
\inf_Y
\bigl(\|h_{T,f}-R_T^*Y\|^2+\|Y\|^2\bigr).
}
\tag{O3b.9}
\]

Da

\[
R_T^*R_T\ge (R_T^{(1)})^*R_T^{(1)},
\]

verwendet C5d hinreichend ein primitives Zertifikat

\[
h_{T,f_+}=(R_T^{(1)})^*Y_T+Z_T
\]

und erhält

\[
\boxed{
\sigma_T(Jf_+)
\le
\|Y_T\|^2+\|Z_T\|^2.
}
\tag{O3b.10}
\]

Das generische Future-Screening-Lemma C5d.1 ist ausdrücklich für **glatte ungerade Source-/Hubvektoren** `g_T` formuliert. Für den geraden alten Test ist dies genau die benötigte Parität.

Die resultierende Schranke lautet

\[
\boxed{
0\le\sigma_T(Jf_+)
\le
\frac{C_{R,f_+}}{T}+C_{R,f_+}e^{-cT}.
}
\tag{O3b.11}
\]

**Firewall O3b-FW1:**

\[
\boxed{
\text{C5d upper bound for even old/source }f_+
\not\Rightarrow
\text{odd old/source upper bound for }f_-.
}
\]

Die beiden Fälle besitzen entgegengesetzte Hubparität.

---

# 5. Neuer Satz O3b.1 — Primitive-Certificate-Obstruction

## Satz

Sei

\[
0\ne f_-\in C_c^\infty((-R,R))
\]

ungerade und `m=m(f_-)` sein erster nichtverschwindender Boundary-Jet. Setze

\[
h_{T,f_-}:=H_T^*J_{R,T}f_-.
\]

Betrachte irgendeine primitive Dualzerlegung

\[
\boxed{
h_{T,f_-}=(R_T^{(1)})^*Y_T+Z_T.}
\tag{O3b.12}
\]

Dann gilt für genügend großes `T`

\[
\boxed{
\|Z_T\|_2^2
\ge
c_{R,f_-,m}
\frac{e^T}{T^{2m+2}}.
}
\tag{O3b.13}
\]

Insbesondere kann eine ausschließlich auf `R_T^(1)` basierende C5d-artige Zertifikatsroute **keine** Schurterm-Obergrenze der gewünschten Boundary-Jet-Skala

\[
\sigma_T(Jf_-)
\lesssim
\frac{e^T}{T^{2m+3}}
\tag{O3b.14}
\]

über die Zertifikatskosten `||Y_T||^2+||Z_T||^2` liefern.

## Beweis

Aus (O3b.8) folgt

\[
\langle (R_T^{(1)})^*Y_T,\mathbf1_T\rangle
=
\langle Y_T,R_T^{(1)}\mathbf1_T\rangle
=0.
\]

Daher erzwingt jede Zerlegung (O3b.12)

\[
\boxed{
\langle Z_T,\mathbf1_T\rangle
=
\langle h_{T,f_-},\mathbf1_T\rangle.
}
\tag{O3b.15}
\]

Aber

\[
\langle h_{T,f_-},\mathbf1_T\rangle
=
\langle J_{R,T}f_-,H_T\mathbf1_T\rangle,
\]

und C4 gibt mit (O3b.5)

\[
|\langle h_{T,f_-},\mathbf1_T\rangle|^2
\asymp_{R,f_-,m}
\frac{e^T}{T^{2m+1}}.
\tag{O3b.16}
\]

Da

\[
\|\mathbf1_T\|_2^2=2T,
\]

liefert Cauchy--Schwarz

\[
\|Z_T\|_2^2
\ge
\frac{|\langle Z_T,\mathbf1_T\rangle|^2}
{\|\mathbf1_T\|_2^2}
\ge
c_{R,f_-,m}
\frac{e^T}{T^{2m+2}}.
\]

Das ist (O3b.13). `□`

## Bedeutung

Die primitive Zertifikatskosten-Untergrenze liegt um exakt einen Faktor `T` **über** der C4-Feshbach-Untergrenze

\[
\frac{e^T}{T^{2m+3}}.
\]

Das beweist **nicht**, dass der wahre Schurterm größer als die gewünschte Skala sein muss. Es beweist nur:

\[
\boxed{
\text{Die primitive C5d-Zertifikatsarchitektur ist im odd Source-Kanal zu grob für eine matching upper bound.}
}
\tag{O3b.17}
\]

---

# 6. Warum die volle Restgeometrie jetzt wesentlich wird

Der vorige No-Go betrifft ausschließlich den primitiven Rest `R_T^(1)`.

C4 verwendet im tatsächlichen Feshbach-Operator dagegen

\[
A_T=I+R_T^*R_T
\]

mit dem **vollen** Rest.

Während

\[
R_T^{(1)}\mathbf1_T=0,
\]

ist für den vollen Nenner nur die committed Abschätzung

\[
\boxed{
\langle\mathbf1_T,A_T\mathbf1_T\rangle=O(T^2)
}
\tag{O3b.18}
\]

relevant für den C4-Lower-Bound.

Damit erscheint ein strukturell wichtiger Unterschied:

- höhere Prime-Powers im **Hub** sind in C5a/C5d für den even-source Tail kontrollierbar bzw. harmlos;
- höhere bzw. nichtprimitive Beiträge im **Rest/Feshbach-Nenner** können im odd-source Konstantenmode-Kanal gerade die zusätzliche Screening-Skala liefern, die der primitive Rest nicht besitzt.

**Firewall O3b-FW2:**

\[
\boxed{
\text{higher-prime-power hub harmless}
\not\Rightarrow
\text{higher-prime-power rest irrelevant}.
}
\]

Für den odd Source-Upper-Bound darf der volle Rest daher nicht ohne neuen Beweis durch den primitiven Rest ersetzt werden.

---

# 7. Warum die triviale Obergrenze nicht genügt

Aus

\[
0<A_T^{-1}\le I
\]

folgt zwar immer

\[
\boxed{
\sigma_T(Jf_-)
\le
\|h_{T,f_-}\|_2^2.
}
\tag{O3b.19}
\]

Im auditierten C4--C5d-Scope liegt jedoch **keine** jet-sensitive Abschätzung der Form

\[
\|h_{T,f_-}\|_2^2
\lesssim
\frac{e^T}{T^{2m(f_-)+3}}
\]

oder eine andere hinreichend scharfe `m`-abhängige Normabschätzung vor.

C4 kontrolliert asymptotisch die skalare Projektion

\[
\langle h_{T,f_-},\mathbf1_T\rangle,
\]

nicht die volle Hubnorm.

Damit kann (O3b.19) die in O3a benötigte relative Wachstumsseparation nicht liefern.

---

# 8. Auditresultat des C4--C5d Upper-Bound-Scans

Die Quellenrollen sind jetzt:

| Knoten | Upper-Bound-relevanter Befund | Reicht für odd `f_-`? |
|---|---|---|
| C4 | vollständige asymptotische Entwicklung von `<h,1_T>` + Feshbach-Untergrenze | **Nein** — Lower Certificate |
| C5 | Jet vollständig auf odd Source + Parität | **Nein** — keine Schur-Obergrenze |
| C5a | exakte Hubparität; `R_T^(1)1_T=0`; even-source Variationsreduktion | **Nein** — zeigt gerade die Paritätsbarriere |
| C5b | Boundary-Screening / Prime-Frame-Analyse für festen even Source-Test | **Nein** — komplementärer Kanal |
| C5c | explizites Dualzertifikat für even Source / odd Hub | **Nein** — komplementärer Kanal |
| C5d | `sigma_T(Jf_+)=O(1/T)` via primitive Future-Screening | **Nein** — Lemma benötigt odd Hub; primitive odd-source Route durch O3b.1 blockiert |

Daher gilt als **Scope-Audit**, nicht als universeller No-Go:

\[
\boxed{
\text{Im committed C4--C5d-Material liegt keine hinreichende sharp odd-source upper bound vor.}
}
\tag{O3b.20}
\]

Status:

\[
\boxed{\checkmark[K/M]_{\rm scope\text{-}audit}.}
\]

**Firewall O3b-FW3:** Die Abwesenheit im auditierten Scope ist keine Aussage, dass eine solche Obergrenze falsch oder unbeweisbar ist.

---

# 9. Präziser nächster analytischer Zielknoten

Der nächste fehlende Satz sollte nicht unscharf `odd upper bound` heißen. O3b lokalisiert ihn genauer als

\[
\boxed{
\textbf{Full-Rest Even-Hub Screening / Sharp Odd Boundary-Jet Feshbach Asymptotics.}
}
\tag{O3b.21}
\]

Für einen festen glatten odd Test `f_-` mit erstem Jet `m` wäre ein hinreichendes Ziel beispielsweise

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\le
C_{R,f_-}
\frac{e^T}{T^{2m+3}},
}
\tag{O3b.22}
\]

oder stärker

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\asymp
C_{R,f_-}
\frac{e^T}{T^{2m+3}}.
}
\tag{O3b.23}
\]

Eine duale Route müsste dabei die **volle** Feshbach-Dualform verwenden:

\[
\sigma_T(Jf_-)
=
\inf_Y
\left(
\|h_{T,f_-}-R_T^*Y\|^2+\|Y\|^2
\right),
\tag{O3b.24}
\]

nicht nur den primitiven Rest.

Alternativ kann eine direkte primal/Feshbach-Analyse den geraden Hubraum in die Konstantenmode und ihren Komplementärraum zerlegen und beide Beiträge samt Cross-Term kontrollieren.

---

# 10. Konsequenz für die odd Konditionsfrage

O3b entscheidet weiterhin **nicht**

\[
\chi^{R,-}_{T,U}\text{ bounded?}
\]

oder

\[
\chi^{R,-}_{T,U}\to\infty?
\]

Der konditionale O3a-Schluss bleibt unverändert:

Falls für zwei feste odd Tests `f_-,g_-` mit

\[
m(f_-)=0,
\qquad
m(g_-)=1
\]

matching Zwei-Seiten-Asymptotiken der Form (O3b.23) bewiesen werden, dann

\[
\frac{\rho_{T,U}(f_-)}{\rho_{T,U}(g_-)}
\asymp C_{R,T,f,g}U^2\to\infty,
\]

also

\[
\kappa(A^{R,-}_{T,U})\to\infty,
\qquad
\chi^{R,-}_{T,U}\to\infty
\]

für festes `T` und `U->infty`.

Aber auch dann gilt weiterhin die geerbte Firewall

\[
\boxed{
\kappa(A^{R,-}_{T,U})\to\infty
\not\Rightarrow
W_{R,S,-}^{[T]}\text{ konvergiert nicht stark}.
}
\tag{O3b.25}
\]

Die O3-Klasse wird durch das Produkt

\[
\chi^{R,-}_{T,U}\|\Theta^-_{T,U}\|
\]

entschieden, nicht durch `chi` allein.

---

# 11. Persistente Firewalls

### O3b-FW1 — Paritätskanäle nicht vertauschen

C5d ist ein starker Upper-Bound-Satz, aber für `even old/source -> odd hub`. Der gesuchte Kanal ist `odd old/source -> even hub`.

### O3b-FW2 — Hub vs. Rest

Die Summabilität oder Harmlosigkeit höherer Prime-Power-**Hub**anteile erlaubt nicht, höhere Prime-Power-**Rest**anteile im odd Konstantenmode-Screening zu verwerfen.

### O3b-FW3 — Primitive Obstruction ist kein Full-Rest-No-Go

O3b.1 widerlegt nur die matching-upper-bound-Leistung einer ausschließlich primitiven Dualzertifikatsarchitektur. Die volle Restgeometrie bleibt offen.

### O3b-FW4 — Scope-Audit ist kein Unmöglichkeitssatz

`No sufficient theorem found in C4--C5d` bedeutet nicht `no theorem can exist`.

### O3b-FW5 — Konditionierung ist nicht Transport

Selbst ein zukünftiger odd Konditions-No-Go entscheidet nicht automatisch den starken relativen Terminaltransport.

### O3b-FW6 — keine Gate-Hochstufung

O3b triggert weder O4 noch C8 noch Readiness-PASS noch SYN noch Seal.

---

# 12. Strategische Arbeitslinie

\[
\boxed{
\text{O3b}
\longrightarrow
\text{full-rest even-hub screening audit}
\longrightarrow
\begin{cases}
\text{sharp odd Feshbach upper/two-sided asymptotic},\\
\text{oder neuer präziser Full-Rest-No-Go / fehlendes Lemma.}
\end{cases}
}
\]

Der Übergabestatus bleibt

\[
\boxed{
\texttt{P11 PASS-A ACTIVE / ORIGINAL TRANSPORT OPEN / SYN BLOCKED}.
}
\]
