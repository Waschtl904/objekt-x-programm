# P11 / Objekt X — Hard-Audit Survivor Ledger

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** knappe Uebergabe nach dem destruktiven Audit dieses Forschungsastes.  
**Registry:** unveraendert.  
**Nonclaim:** kein RH-Beweis, kein Object-X-Abschluss, kein Publikationsneuheitsclaim.

---

## 0. Urteil

Nach absichtlich destruktiver Gegenpruefung bleibt ein kleinerer, aber mathematisch klarerer Kern uebrig.

Der Ast hat **kein neues RH-Kriterium** gefunden. Die endgueltige Frequenzbereichsform setzt sich exakt zum klassischen Lagarias-Objekt

```math
G(s)=\frac{\xi'}{\xi}\left(\frac12+s\right)
```

zusammen. Bekannt ist

```math
RH
\iff
\operatorname{Re}G(s)>0
\qquad(\operatorname{Re}s>0).
```

Der moegliche projektspezifische Wert liegt daher nur in einer konstruktiven Zeit-/Zustandsraumgeometrie, die diese bekannte positive-real-Funktion **vorwaerts** aus den bereits vorhandenen P11-/OU-/Gamma-Daten realisiert.

---

# 1. Ueberlebende exakte Saetze

### S1. NULLPOL ist Critical-half Green-Range

```math
C_c^\infty(-a,a)\cap\ker M(0)\cap\ker M(1)
=
(-\partial_x^2+1/4)C_c^\infty(-a,a).
```

Die zwei Mellinbedingungen sind exakt das Verschwinden der beiden aeusseren Green-Ladungen fuer den Kern `exp(-|x-y|/2)`.

**Status:** `✓[M]`.

### S2. P11 Prime-Power-Ledger ist sampled OU/Green

Nach Weil-Diagonalnormalisierung:

```math
R_q(j,k)=q^{|j-k|},
\qquad q=p^{-1/2}.
```

Hub + Innovationen ergeben exakt den stationaeren AR(1)-Kern.

**Status:** `✓[M]` fuer den Kanalindex-Ledger; keine Gleichsetzung mit dem vollen raeumlichen P11-Operator.

### S3. P11-Masken sind stopped OU

Mit

```math
L_R(x)=2(R-|x|),
\qquad
m_p(x)=\lfloor L_R(x)/\log p\rfloor,
```

ist die lokale normalisierte Kovarianz

```math
R_q^{(m)}(j,k)=q^{j+k-2\min(j,k,m)}.
```

Die Tiefeninkremente sind positiv Rang eins.

**Status:** `✓[M]`.

### S4. Universeller stopped Critical-half-Kern

```math
G_L(s,t)
=\exp\left(-\frac{s+t}{2}+\min(s,t,L)\right).
```

P11 ist seine exakte logarithmische Gitterabtastung. Seine inverse Kovarianz ist in der Kanaltiefe erneut `-partial_t^2+1/4`.

**Status:** `✓[M]`.

### S5. Exaktes boundary-tail shorting

Diskret:

```math
Y_m=\sqrt{1-q^2}\sum_{k\ge m}q^{k-m}X_k
```

und

```math
\sum_{r=1}^{m-1}
\frac{\|Y_r-qY_{r+1}\|^2}{1-q^2}
+\|Y_m\|^2
=
\sum_{r<m}\|X_r\|^2+\|Y_m\|^2.
```

Der aeussere Tail wird kontraktiv auf genau einen normierten exponentiellen Boundary-Modus gekuerzt.

Kontinuierlich gilt dieselbe Identitaet fuer

```math
Y(u)=\int_u^\infty e^{-(t-u)/2}X(t)dt.
```

**Status:** `✓[M]`.

### S6. Ein universelles Jump-Feld fuer alle Primzahlen

```math
X_v(t)=e^{-t/4}K_tv
```

liefert

```math
\sqrt{w_{p,k}}K_{k\log p}v
=\sqrt{\log p}\,X_v(k\log p).
```

Jeder Primast tastet dasselbe kontinuierliche Feld auf seinem logarithmischen Gitter ab.

**Status:** `✓[M]`.

### S7. Prime-Pole-Diskrepanznormalform

```math
\Delta
=\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}
-e^{t/2}dt.
```

Auf NULLPOL hebt sich der glatte Prime-Hauptterm exakt gegen den Gamma-Grundmodus auf. Der grosse fensterabhaengige Diagonalskalar verschwindet aus der window-free Darstellung.

**Status:** `✓[M]`.

### S8. Critical-half Finite-Part-Transfer

Der kanonische Abel-Finite-Part-Tail ist

```math
J_\Delta(L)
=e^{L/2}\left(
L-\gamma-
\sum_{\log n<L}\frac{\Lambda(n)}n
\right),
```

mit

```math
J_\Delta(0)=-\gamma,
\qquad
d\Delta=\frac12J_\Delta dL-dJ_\Delta.
```

Damit koppelt die Diskrepanz exakt an den first-order Critical-half-Port

```math
D_+=\partial_x+\frac12.
```

**Status:** `✓[M]`.

### S9. Kausale Volterra-Faktorisierung

Mit

```math
(V_Jv)(x)=\int_{-\infty}^xJ_\Delta(x-y)v(y)dy
```

und `D_-=D_+^*` gilt

```math
D_-V_J+V_J^*D_+
=2\gamma I+\mathcal C_\Delta.
```

**Status:** `✓[M]`.

### S10. Hoehere Gamma-Schicht ist eine stabile kausale Filterbank

Fuer

```math
\mu_m=2m+\frac12,
\qquad m\ge1,
\qquad y_m=(\partial_x+\mu_m)^{-1}v,
```

ist

```math
\int_0^\infty h_1(t)\|K_tv\|^2dt
=
\sum_{m\ge1}\frac2{\mu_m}\|y_m'\|^2.
```

**Status:** `✓[M]`.

### S11. Causal NULLPOL-Normalform

```math
Q_W(v)
=
\sum_{m\ge1}\frac2{\mu_m}\|y_m'\|^2
-c_*\|v\|^2
-2\operatorname{Re}\langle D_+v,V_Jv\rangle,
```

mit

```math
c_*=\log(8\pi)+\frac\pi2-4-\gamma>0.
```

**Status:** `✓[M]` als Identitaet; Positivitaet offen.

### S12. Eulerfaktor ist der adjungierte P11-AR(1)-Resolvent

```math
T_q^*=\sqrt{1-q^2}(I-qS)^{-1}.
```

Am Root-Impuls ist die Transferfunktion

```math
\frac1{1-qz}.
```

Mit `q=p^{-1/2}` und `z=e^{-s\log p}` ist dies exakt

```math
\frac1{1-p^{-(s+1/2)}}.
```

**Status:** `✓[M]`; der Eulerfaktor an sich ist klassisch, die Identifikation mit dem vorhandenen P11-Choleskyfaktor ist der projektinterne Brueckenpunkt.

### S13. Strong-Terminal-Geometrie

Normalisiert gilt

```math
\|R_q-R_q^{(m)}\|=\frac{1+q}{1-q},
```

also strong, aber keine Normkonvergenz.

Mit Weilgewichten gilt im festen Innenraum fuer Tiefe `L>=2`

```math
\sup_p\|C_p-C_p^{(m_p(L))}\|
\le C_0Le^{-L/2}.
```

Die bewegte Randzone `L_R(x) approx 0` erklaert, warum global Strong-Terminal natuerlich ist, waehrend feste innere Quellen exponentiell gut konvergieren.

**Status:** `✓[M]` fuer den Kanal-Gram-Mechanismus; kein neuer voller raeumlicher C6-Satz.

---

# 2. Explizit geschlossene / verworfene Klassen

```text
pointwise scattering multiplier positivity                    ×[M]
primewise contractive P11 innovation -> bare jump shorting     ×[M]
reverse primewise contraction                                  ×[M]
scalar Hub repair of stopped-tail defect                       ×[M]
local positive critical-rate finite-part Hamiltonian           ×[M]
static higher-Gamma lower-frame repair of lost OU tail         ×[M]
fixed-window prolate as a scalable all-window RH strategy      demoted
```

Der Hard Audit hat ausserdem die alte Orbitketten-Exaktheitsformel korrigiert:

```math
N(t)=\lceil L/t\rceil
```

(statt `floor(L/t)+1` an den ganzzahligen Verhaeltnissen).

---

# 3. Literaturkollision / was NICHT neu ist

Nicht als Neuheit beanspruchen:

```text
- RH als positive-real/Herglotz-Kriterium fuer xi'/xi;
- Lagarias-Positivitaet;
- Zeta-bezogene Kontroll-/Transfer-Systeme allgemein;
- Prolate/Paley-Wiener/Toeplitz-Methoden fuer Weil-Positivitaet;
- Eulerprodukt als Fredholm-/Diagonal-Determinantenschreibweise;
- AR(1), OU, Green-Kerne oder passive Realisierungstheorie fuer sich.
```

Die Frequenzbereichsverdichtung ist exakt

```math
\boxed{
\frac{\xi'}{\xi}\left(\frac12+s\right)
=
(s-\tfrac12)\widehat J_\Delta(s)
+
\sum_{m\ge1}\frac{s}{\mu_m(s+\mu_m)}
-\frac{c_*}{2}.
}
```

Das zugehoerige positive-real RH-Kriterium ist klassisch. Der Forschungswert dieses Astes kann deshalb nur in der **konstruktiven Herleitung der Komponenten aus P11/stopped-OU/overlap-cone** liegen.

---

# 4. Der eine verbleibende Gate

Die einzige Route, die nach dem Hard Audit noch als substantiell genug fuer Objekt X erscheint, lautet:

```math
\boxed{
\text{Konstruiere direkt aus der gestoppten P11-OU-Filtration,}
\atop
\text{dem kontinuierlichen Pol-Compensator und der Gamma-Filterbank}
\text{einen positiven Storage-/konservativen Zustandsraum, dessen}
\text{Transfer automatisch }\xi'/\xi(1/2+s)\text{ ist.}
}
```

Der Zustandsraum muss **vor** jeder Verwendung von Weil-Positivitaet, Lagarias-Positivitaet oder RH definiert sein.

### PASS

Ein kanonischer, coefficient-free positiver Block / Storage-Satz wird aus den vorhandenen OU-/Boundary-Daten abgeleitet und liefert die kausale Normalform. Dann waere die rechte-Halbebenen-Passivitaet strukturell und wuerde ueber das bekannte Lagarias-Kriterium RH implizieren.

### FAIL

Wenn bereits die natuerliche Storage-Klasse, die nur aus

```text
- stopped OU innovation states,
- normalized boundary-tail states,
- continuous compensator,
- higher Gamma filter states,
- canonical overlap-cone incidence
```

besteht, den exakten `R=1` Prime-2 mixed witness nicht reproduzieren kann, wird diese gesamte Architekturklasse als No-Go geschlossen.

Keine freien Kalibrierkoeffizienten duerfen nach dem Witness angepasst werden.

---

# 5. Empfehlung fuer externen Hauptagenten

Nicht die 30+ Audits einzeln lesen. Zuerst genau diese Datei, danach nur die Primarproofs fuer S1, S3/S4, S5/S6, S8/S9, S12/S13.

Destruktiver Reviewauftrag:

```text
A. Pruefe jede Survivor-Identitaet unabhaengig.
B. Suche zuerst nach Normalisierungs-/Randtermfehlern in S5, S8 und S9.
C. Pruefe, ob die P11-Euler-Resolventidentitaet S12 ueber das skalare
   Impulsmodell hinaus irgendwo ueberinterpretiert wird.
D. Pruefe die Strong-vs-Norm-Aussage S13 mit den echten Weilgewichten.
E. Akzeptiere das Lagarias-Kriterium als bekannte Zielidentitaet; bewerte nur,
   ob die konkrete P11/OU-Geometrie einen nichtzirkulaeren Storage-Kandidaten
   liefert.
```

Das ist der aktuelle ehrliche Forschungsstand.