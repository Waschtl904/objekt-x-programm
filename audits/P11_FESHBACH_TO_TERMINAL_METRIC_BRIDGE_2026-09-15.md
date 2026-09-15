# P11 Audit — concrete Feshbach defect to terminal-metric bridge

**Datum:** 15. September 2026  
**Basis:** P11 finite-horizon form `q_R^X`, Gamma pullback invariance, exact Feshbach pullback block identity, frozen R14/R39 terminal formalism.  
**Rolle:** exakte Zuordnung der neuen konkreten Source-/Rest-Bloecke zu den spaeteren abstrakten Future-Metriken.  
**Registry:** unveraendert.  
**Nonclaim:** kein neuer Strong-Terminal-Beweis; keine Promotion von R39/C6; kein RH-Beweis.

---

## 0. Kurzurteil

Die in den spaeteren R14/R39-Audits verwendeten Terminalmetriken `G_{R,T}` und relativen Metriken `A_R(U)` sind auf dem konkreten P11-Operatorniveau vollstaendig durch den **Pullback-Defekt des Hub-Feshbachterms** bestimmt.

Fuer `R<T` setze

```math
\boxed{
D_{R,T}^{\Sigma}
:=E_{R,T}^*\Sigma_TE_{R,T}-\Sigma_R.
}
```

Da die Gammaform unter Nullfortsetzung exakt invariant ist,

```math
\boxed{
q_T^X(E_{R,T}f,E_{R,T}g)-q_R^X(f,g)
=\langle D_{R,T}^{\Sigma}f,g\rangle_{L^2(-R,R)}.
}
```

Mit der kanonischen Einbettung

```math
\iota_R:\mathcal K_{X,R}\hookrightarrow L^2(-R,R)
```

folgt fuer den Terminalmetric-Operator auf dem P11-Graphraum

```math
\boxed{
G_{R,T}
=I+\iota_R^*D_{R,T}^{\Sigma}\iota_R.
}
```

Damit sind die abstrakten Future-Metriken keine zusaetzliche unbekannte Schicht: ihr gesamter nichttrivialer Inhalt liegt im konkreten Feshbach-Pullbackdefekt.

Die zuvor isolierten Operatoren

```math
\Delta_{R,T},
\quad\mathfrak C_{R,T},
\quad K_0(R,T),
\quad K_1(R,T)
```

geben ueber die exakte Blockformel fuer `E^*Sigma_T E` eine explizite Source-Level-Zerlegung von `G_{R,T}` und damit auch der R14/R39-Relativmetriken.

Status:

```text
Gamma cancellation in future metric difference             ✓[M]
G_{R,T}=I+iota_R^* D_Sigma iota_R                          ✓[M]
concrete block data feed terminal metric                    ✓[M]
compactness of G_{R,T}-I at fixed R,T                       ✓[M]
identification with R14/R39 relative metric normalization   ✓[M]
new convergence theorem for R39 scalar phase/no-escape       ?[O]
Strong Terminal / C6                                         ?[O]
```

---

# 1. Finite-horizon P11 forms

Auf dem Source-Fenster `(-R,R)` lautet die positive P11-Kandidatenform

```math
q_R^X(f,g)
=\mathfrak c_{\Gamma,R}[f,g]
+\langle\Sigma_Rf,g\rangle_{L^2(-R,R)},
```

mit

```math
\Sigma_R
=H_R(I+R_R^*R_R)^{-1}H_R^*\succeq0.
```

Der zugehoerige Graph-Hilbertraum sei `K_{X,R}`.

Fuer `R<T` ist

```math
J_{R,T}:\mathcal K_{X,R}\to\mathcal K_{X,T},
\qquad
J_{R,T}f=E_{R,T}f
```

der P11-Uebergang durch Nullfortsetzung.

Der Terminalmetric-Operator ist per Definition

```math
\boxed{G_{R,T}=J_{R,T}^*J_{R,T}.}
```

Damit

```math
\langle f,G_{R,T}g\rangle_{X,R}
=q_T^X(E_{R,T}f,E_{R,T}g).
```

---

# 2. Die Gamma-Seite faellt aus dem Future-Defekt exakt heraus

P11 beweist

```math
\mathfrak c_{\Gamma,T}[E_{R,T}f,E_{R,T}g]
=\mathfrak c_{\Gamma,R}[f,g].
```

Daher

```math
\begin{aligned}
q_T^X(Ef,Eg)-q_R^X(f,g)
&=\langle E^*\Sigma_TE f,g\rangle_{L^2}\\
&\quad-\langle\Sigma_Rf,g\rangle_{L^2}.
\end{aligned}
```

Setze

```math
\boxed{
D_{R,T}^{\Sigma}
:=E_{R,T}^*\Sigma_TE_{R,T}-\Sigma_R.
}
```

Dann exakt

```math
\boxed{
q_T^X(Ef,Eg)-q_R^X(f,g)
=\langle D_{R,T}^{\Sigma}f,g\rangle_{L^2}.
}
```

Das komplette Future-Metrikproblem liegt somit in der Hub-Feshbach-Differenz; die Gamma-Backbone traegt keinen eigenen Pullbackdefekt.

---

# 3. Darstellung auf dem Graph-Hilbertraum

Sei

```math
\iota_R:\mathcal K_{X,R}\to L^2(-R,R)
```

die kanonische Einbettung.

Da `q_R^X(f)>=||f||_2^2`, ist `iota_R` beschraenkt. Fuer den beschraenkten selbstadjungierten `L^2`-Operator `D_{R,T}^Sigma` definiert

```math
\iota_R^*D_{R,T}^{\Sigma}\iota_R
```

einen beschraenkten selbstadjungierten Operator auf `K_{X,R}`.

Aus §2 folgt fuer alle Formvektoren

```math
\begin{aligned}
\langle f,(G_{R,T}-I)g\rangle_{X,R}
&=q_T^X(Ef,Eg)-q_R^X(f,g)\\
&=\langle\iota_Rf,D_{R,T}^{\Sigma}\iota_Rg\rangle_{L^2}.
\end{aligned}
```

Also

```math
\boxed{
G_{R,T}
=I+\iota_R^*D_{R,T}^{\Sigma}\iota_R.
}
```

Dies ist die exakte Concrete-to-Terminal-Metric-Bridge.

---

# 4. Fixed-window compactness

P11 beweist, dass die Einbettung

```math
\iota_R:\mathcal K_{X,R}\hookrightarrow L^2(-R,R)
```

fuer jedes feste `R` kompakt ist (Gamma-Graph-Confinement).

Da `D_{R,T}^{\Sigma}` auf `L^2(-R,R)` beschraenkt ist, ist

```math
\boxed{
G_{R,T}-I
=\iota_R^*D_{R,T}^{\Sigma}\iota_R
}
```

kompakt auf `K_{X,R}`.

Dies erklaert konkret die `I + compact`-Natur der fixed-source Future-Metrik, ohne daraus irgendeine terminale Kompaktheit bei `T->infty` zu folgern.

---

# 5. Einsetzen der exakten Feshbach-Pullbackdaten

Der Block-Audit fuer `R<T` schreibt den komprimierten inversen Restkern in den Daten

```math
\Delta_{R,T},
\qquad
\mathfrak C_{R,T},
\qquad
K_0(R,T),
\qquad
K_1(R,T).
```

Insbesondere ist

```math
(E^*B_TE)^{-1}
=B_R^{-1}+\Delta^*\Delta-\mathfrak C,
```

und `E^*Sigma_T E` besitzt die explizite positive Zweiblockform aus dem Pullback-Audit.

Damit ist

```math
D_{R,T}^{\Sigma}
=E^*\Sigma_TE-\Sigma_R
```

vollstaendig in diesen vorwaerts definierten Source-/Rest-/Hubdaten ausdrueckbar.

Folglich wird auch

```math
G_{R,T}-I
```

durch genau dieselben konkreten P11-Bloecke erzeugt.

---

# 6. Zuordnung zu R14/R39

Fixiere einen Basisterminalradius `T_0>R`. In der spaeteren P11-Notation ist

```math
X_R(U)
=(G_{R,U})^{1/2}(G_{R,T_0})^{-1/2}.
```

Sein positiver Polar-Modulus erfuellt

```math
A_R(U)
=X_R(U)^*X_R(U)
=(G_{R,T_0})^{-1/2}
 G_{R,U}
 (G_{R,T_0})^{-1/2}.
```

Mit §3 folgt daher

```math
\boxed{
A_R(U)
=(G_{R,T_0})^{-1/2}
\left[I+\iota_R^*D_{R,U}^{\Sigma}\iota_R\right]
(G_{R,T_0})^{-1/2}.
}
```

Analog fuer den Source-Radius `S`.

Damit liegt unter den abstrakten R14/R39-Modulusoperatoren eine konkrete Feshbach-Pullbackfamilie.

---

# 7. Konsequenz fuer die spaetere Strong-Terminal-Front

R39 reduziert die Modulusfrage nach weiteren Audits weitgehend auf eine skalare normale Richtung / phase-no-escape-Frage und trennt sie von der Polar-Gauge-Frage.

Der vorliegende Satz ersetzt diese spaetere Reduktion **nicht**. Er liefert vielmehr einen moeglichen konkreten Input:

```text
P11 Source/Rest/Hub data
        -> D_Sigma(R,U)
        -> G_{R,U}
        -> A_R(U)
        -> R38/R39 normal/phase gate.
```

Damit kann eine kuenftige Schaetzung des R39-Skalars auf die expliziten Bloecke

```math
\Delta,
\mathfrak C,
K_0,
K_1
```

zurueckgefuehrt werden, statt die Future-Metrik als Blackbox zu behandeln.

### Firewall

Aus der Identitaet

```math
G_{R,T}=I+\iota_R^*D_{R,T}^{\Sigma}\iota_R
```

folgt **kein** Vorzeichen fuer `G_{R,T}-I`, weil der Feshbach-Pullbackdefekt `D_{R,T}^Sigma` im Allgemeinen indefinit sein kann.

Ebenso folgt aus fixed-`T` compactness keine terminale Norm- oder Strong-Konvergenz. R39/C6 bleibt offen auf seinem eingefrorenen Status.
