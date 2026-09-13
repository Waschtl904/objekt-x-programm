# P11 Audit — Continuous OU factorization and the 2D moment quotient at a=1/2

**Datum:** 13. September 2026  
**Basis:** Critical-half branch nach dem Prime-2 bad-channel PASS.  
**Rolle:** theorem-level Strukturaudit fuer den verbleibenden `CRIT-HALF-COMPRESS-1`-Gate.  
**Registry:** unveraendert.  
**Nonclaim:** die volle `a=1/2`-Positivitaet ist noch nicht geschlossen.

---

## 0. Kurzurteil

Zwei weitere exakte Reduktionen werden verfuegbar.

Erstens besitzt **jede** Gamma-Resolventenstufe eine kausale OU-/Innovationsfaktorisierung

```math
\boxed{
A_\mu
=\frac2\mu V_\mu^*V_\mu,
\qquad
V_\mu=\partial_x(\partial_x+\mu)^{-1}.
}
```

Der zugehoerige Zustand

```math
y_\mu=(\partial_x+\mu)^{-1}v
```

erfuellt die skalare Markov-Gleichung

```math
y_\mu'+\mu y_\mu=v.
```

Abtastung dieses Zustands in Schrittweite `h=log p` beim Gamma-Grundwert `mu=1/2` liefert exakt

```math
q_p=e^{-h/2}=p^{-1/2},
```

also den P11-AR(1)-Parameter. Der diskrete P11-Tail-/Innovationsmechanismus ist damit die logarithmische Abtastung des kontinuierlichen Gamma-Grund-OU-Kanals.

Zweitens reduziert sich beim Spezialgate `a=1/2`, `p=2` nach Herausnahme der separat NULLPOL Rand- und Komplementunterraeume der verbleibende Momententransfer **exakt auf zwei komplexe Freiheitsgrade**:

```math
\boxed{
\dim\left(
\mathscr H_{NP,1/2}/(U\oplus W)
\right)=2.
}
```

Damit wird die volle Positivitaetsfrage, sobald `Q|_{U\oplus W}` coerciv geschlossen ist, zu einer `2 x 2` Hermite-Weyl-/Schur-Matrix auf den beiden Critical-half Randladungen.

Status:

```text
continuous Gamma OU innovation factorization            ✓[M]
P11 q_p as exact sampled Gamma-ground OU transition      ✓[M]
NULLPOL closes both ground OU exterior states             ✓[M]
ground Gamma channel Dirichlet estimate                  ✓[M]
2D moment-transfer quotient at a=1/2                     ✓[M]
bad Prime-2 channel U                                    ✓[M] positive (previous audit)
coercivity on U direct-sum W                             ?[O]
2x2 effective Weyl/Schur matrix                          ?[O]
full a=1/2 NP-GAP                                        ?[O]
```

---

# 1. Kausaler OU-Resolvent

Fuer `mu>0` definiere auf `L^2(R)` den kausalen Resolventen

```math
(R_\mu^+f)(x)
:=
\int_{-\infty}^x e^{-\mu(x-y)}f(y)\,dy.
```

Dann

```math
R_\mu^+=(\partial_x+\mu)^{-1}
```

im ueblichen schwachen Sinn und sein Fouriermultiplikator ist

```math
\frac1{\mu+iz}.
```

Setze

```math
\boxed{
V_\mu
:=\partial_xR_\mu^+
=I-\mu R_\mu^+.
}
```

Der Fouriermultiplikator von `V_mu` ist

```math
\frac{iz}{\mu+iz}.
```

Daher

```math
V_\mu^*V_\mu
\quad\widehat{}\quad
\frac{z^2}{z^2+\mu^2}.
```

Fuer die Gamma-Stufe

```math
A_\mu(D)
=\frac2\mu\frac{D^2}{D^2+\mu^2}
```

folgt exakt

```math
\boxed{
A_\mu=\frac2\mu V_\mu^*V_\mu.
}
```

Dies ist eine vorwaerts konstruierte positive Faktorisierung jeder einzelnen archimedischen Resolventenstufe.

---

# 2. Zustandsraum-/Markovform

Sei

```math
y_\mu=R_\mu^+v.
```

Dann

```math
\boxed{
y_\mu'+\mu y_\mu=v,}
```

und

```math
V_\mu v=y_\mu'.
```

Somit

```math
\boxed{
\langle v,A_\mu v\rangle
=\frac2\mu\|y_\mu'\|_2^2.
}
```

Fuer `v` mit Traeger in `[-a,a]` ist `y_mu(x)=0` fuer `x<=-a`. Nach dem rechten Traegerrand gilt

```math
y_\mu(x)
=e^{-\mu(x-a)}y_\mu(a),
```

mit

```math
\boxed{
y_\mu(a)=e^{-\mu a}E_{\mu,+}(v),
\qquad
E_{\mu,+}(v)=\int e^{\mu x}v(x)dx.}
```

Daher kann die Energie auch auf dem endlichen Fenster geschrieben werden als

```math
\boxed{
\langle v,A_\mu v\rangle
=\frac2\mu\int_{-a}^a|y_\mu'(x)|^2dx
+|y_\mu(a)|^2.
}
```

Der letzte Term ist exakt die Energie des exponentiellen rechten Aussenschwanzes.

Die anti-kausale Faktorisierung mit `( -\partial_x+mu)^{-1}` liefert spiegelbildlich den linken Aussenzustand und `E_{mu,-}`.

---

# 3. NULLPOL schliesst den Gamma-Grundzustand an beiden Enden

Fuer den Grundmodus

```math
\mu_0=\frac12
```

sind

```math
E_{\mu_0,+}(v)=E_+(v)=M(v)(1),
```

und anti-kausal

```math
E_{\mu_0,-}(v)=E_-(v)=M(v)(0).
```

Auf NULLPOL verschwinden beide. Fuer den kausalen Grundzustand

```math
y_0=(\partial_x+1/2)^{-1}v
```

gilt daher

```math
\boxed{
y_0(-a)=y_0(a)=0.}
```

Insbesondere liegt `y_0` in `H_0^1(-a,a)` und

```math
\boxed{
\langle v,A_{1/2}v\rangle
=4\|y_0'\|_2^2.
}
```

Da

```math
v=y_0'+\frac12y_0
```

und der Randterm verschwindet,

```math
\|v\|^2
=\|y_0'\|^2+\frac14\|y_0\|^2.
```

Mit Dirichlet-Poincare

```math
\|y_0\|^2
\le\left(\frac{2a}{\pi}\right)^2\|y_0'\|^2
```

folgt die explizite Ground-mode-Schranke

```math
\boxed{
\langle v,A_{1/2}v\rangle
\ge
\frac{4}{1+a^2/\pi^2}\|v\|^2
\qquad(v\in\mathscr D_{NP,a}).
}
```

Diese benutzt beide Critical-half Randbedingungen in der Zustandsraumform und kein Weil-Positivitaetsinput.

---

# 4. P11-AR(1) ist die exakte logarithmische Abtastung dieses Zustands

Die skalare Zustandsgleichung liefert fuer jedes `h>0`

```math
\boxed{
y_\mu(x+h)
=e^{-\mu h}y_\mu(x)
+
\int_x^{x+h}e^{-\mu(x+h-s)}v(s)ds.}
```

Setze jetzt den **Gamma-Grundwert**

```math
\mu=\frac12
```

und einen Primschritt

```math
h_p=\log p.
```

Dann ist der Zustandsuebergang exakt

```math
\boxed{
e^{-\mu h_p}=e^{-\log p/2}=p^{-1/2}=q_p.}
```

Bei iterierter Abtastung entsteht somit dieselbe AR(1)-Rekursion

```math
y_{k+1}=q_py_k+\text{segment innovation}
```

wie im P11-Kanalindex-Ledger.

Die normierten, voneinander disjunkten Segmentinnovationen liefern die bekannte Zerlegung

```math
R_{q_p}=T_{q_p}^*T_{q_p}+u_pu_p^*.
```

Damit ist die fruehere diskrete Tail-/Hub-Faktorisierung nicht nur mit demselben Kovarianzkern kompatibel: sie ist die **diskrete Zustandsraumabtastung des kontinuierlichen Gamma-Grund-OU-Kanals**.

---

# 5. Prime-2-Faserdekomposition bei a=1/2

Setze wie im Threshold-Audit

```math
h=\log2,
\qquad
b=\frac{1-h}{2},
\qquad
c=h-\frac12.
```

Dann zerfaellt

```math
H=L^2(-1/2,1/2)
```

orthogonal als

```math
\boxed{
H=H_+\oplus H_-\oplus H_M,
}
```

wobei

```math
H_+=\operatorname{Ran}P_+,
\qquad
H_-=\operatorname{Ran}P_-,
```

die symmetrischen/antisymmetrischen Zwei-Rand-Fasern sind und

```math
H_M=L^2(-c,c)
```

der mittlere Einblattbereich ist.

Setze

```math
K:=H_-\oplus H_M.
```

Die Prime-2-Form ist in dieser Zerlegung diagonal:

```math
C_2=-w_2P_+ + w_2P_-,
\qquad
w_2=\frac{\log2}{\sqrt2}.
```

---

# 6. Momentabbildungen auf beiden Seiten sind surjektiv

Definiere die Critical-half Randladungsabbildung

```math
\mathcal E f=(E_+(f),E_-(f))\in\mathbb C^2.
```

Auf `H_+` gilt ueber die Isometrie `S_+ : L^2(-b,b)->H_+`

```math
\mathcal E(S_+g)
=\sqrt2\cosh(h/4)\,\mathcal E_b(g).
```

Die beiden Funktionen `e^{x/2}` und `e^{-x/2}` sind auf jedem nichtleeren Intervall linear unabhaengig. Daher ist

```math
\mathcal E_b:L^2(-b,b)\to\mathbb C^2
```

surjektiv, also auch `E|_{H_+}`.

Auf `K` ist bereits die Einschraenkung auf den Mittelraum `H_M=L^2(-c,c)` surjektiv. Somit

```math
\boxed{
\mathcal E|_{H_+}:H_+\twoheadrightarrow\mathbb C^2,
\qquad
\mathcal E|_K:K\twoheadrightarrow\mathbb C^2.}
```

---

# 7. Der separat NULLPOL-Unterraum und der 2D Quotient

Definiere

```math
U:=H_+\cap\ker\mathcal E,
```

```math
W:=K\cap\ker\mathcal E.
```

Dann ist

```math
U\oplus W\subset\mathscr H_{NP}:=\ker\mathcal E\subset H.
```

Fuer `v=p+k` mit `p in H_+`, `k in K` lautet die globale NULLPOL-Bedingung

```math
\mathcal E p+\mathcal E k=0.
```

Definiere auf `H_NP` die Quotientenkoordinate

```math
\boxed{
\mathfrak m(v):=\mathcal E p=-\mathcal E k\in\mathbb C^2.}
```

Dann

```math
\ker\mathfrak m=U\oplus W.
```

Wegen der Surjektivitaet aus §6 ist `m` selbst surjektiv. Der erste Isomorphiesatz liefert daher

```math
\boxed{
\mathscr H_{NP}/(U\oplus W)
\cong\mathbb C^2.}
```

Insbesondere

```math
\boxed{
\dim_\mathbb C\bigl(\mathscr H_{NP}/(U\oplus W)\bigr)=2.}
```

Dies ist eine exakte algebraische Aussage; keine Positivitaet wird dafuer vorausgesetzt.

---

# 8. Konsequenz fuer den verbleibenden Schur-Gate

Der vorherige Audit hat bereits fuer den gesamten negativen Prime-Kanal

```math
\boxed{
Q_{1/2}|_U\succeq\frac1{20}I.}
```

bewiesen.

Angenommen, der naechste Gate zeigt zusaetzlich eine Coercivity

```math
Q_{1/2}|_{U\oplus W}\succeq\delta I
```

mit `delta>0`. Dann kann `U direct-sum W` in der vollen NULLPOL-Form geshortet werden.

Waehle beliebige lineare Rechtsinverse der Momentabbildungen und damit fuer `m in C^2` einen Repraesentanten

```math
r(m)=p(m)+k(-m)\in\mathscr H_{NP}.
```

Definiere die effektive Quotientenform

```math
\boxed{
q_{eff}(m)
:=
\inf_{h\in U\oplus W}
Q_{1/2}(r(m)+h).
}
```

Wegen der Coercivity ist das Infimum eindeutig durch das Schur-Minimum realisiert und `q_eff` ist eine Hermiteform auf `C^2`. Daher existiert eine eindeutige `2 x 2` Hermitematrix `M_eff` mit

```math
q_{eff}(m)=m^*M_{eff}m.
```

Dann gilt exakt

```math
\boxed{
Q_{1/2}\succeq0\text{ auf }\mathscr H_{NP}
\iff
M_{eff}\succeq0,
}
```

vorausgesetzt der coercive Gate auf `U direct-sum W` ist geschlossen.

Somit besteht der verbleibende `a=1/2`-Angriff aus zwei klar getrennten Aufgaben:

```text
(A) coercivity on the separately-NULLPOL block U direct-sum W;
(B) positivity of one 2x2 effective critical-half Weyl matrix.
```

---

# 9. Warum die numerisch schwache Richtung nicht dem bad channel entspricht

Der negative Prime-Kanal `U` besitzt bereits eine theorem-level positive Reserve. Daher kann eine fast-null Richtung der vollen Form nicht innerhalb von `U` liegen.

Die Quotientenzerlegung zeigt den einzigen algebraisch neuen Mechanismus ausserhalb `U direct-sum W`: eine Funktion kann auf `H_+` **nichtzero** Critical-half Ladungen tragen und diese durch entgegengesetzte Ladungen im Komplement `K` exakt neutralisieren.

Dieser Mechanismus wird hier als

```text
critical-half moment transfer
```

bezeichnet.

Er besitzt genau zwei komplexe Koordinaten `E_+` und `E_-`. Das ist der natuerliche Kandidat fuer die verbleibende kleine Eigenrichtung.

Dies ist eine Strukturdiagnose; ein numerischer Eigenvektor wird nicht als Beweisinput verwendet.

---

# 10. Naechster Gate

Prioritaet ist jetzt nicht mehr eine globale `a=1/2`-Suche, sondern:

1. `OU-SCHUR-A`: beweise Coercivity auf `U direct-sum W`, wobei der Ground-OU-Kanal und die Prime-2-Diagonalisierung exakt benutzt werden;
2. `OU-SCHUR-B`: berechne/charakterisiere danach die `2x2` Weyl-Matrix `M_eff` ueber die beiden Randladungen;
3. erst nach PASS von A+B Fortsetzung im ein-Prime-Intervall `log2/2<a<log3/2`.

Die kausale OU-Faktorisierung macht fuer Schritt 1 jeden Gamma-Modus zu einem eindimensionalen Zustandskanal. Das ist die bevorzugte Schur-/Riccati-Darstellung.

---

# 11. Firewalls

Nicht behauptet wird:

- `Q|_{U direct-sum W}` sei bereits coerciv;
- die `2x2` effektive Matrix sei bereits berechnet oder positiv;
- die Quotientenreduktion allein beweise fixed-window Positivitaet;
- die kontinuierliche OU-Faktorisierung allein liefere Object X;
- globales NP-GAP oder RH seien geloest.
