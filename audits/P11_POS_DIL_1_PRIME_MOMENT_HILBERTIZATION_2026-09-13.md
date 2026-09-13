# P11 / POS-DIL-1 — Prime-moment Hilbertization of the OX-GEN plane

> **Stand:** 13. September 2026  
> **Rolle:** theorem-level interner Audit der ersten POSITIVE-DILATION-Klasse; keine Registry-Promotion, keine Object-X-/RH-Folgerung.  
> **Basis:** `main@48d1656cdf9be877e57ca1187d5679733603f295`.  
> **Scope:** kompakt getragene Testfunktionen, insbesondere Nullfortsetzungen aus `H_0^1(-a,a)`; Suzukis `r_0`-Block. `r_1`, `c_aI` und die volle Weilform bleiben offen.

## 0. Kurzurteil

POS-DIL-1 lässt sich algebraisch schließen, ohne numerischen Input.

Es gibt zwei komplementäre Resultate.

1. **Enger No-Go:** Die volle Translationrepräsentation `rho(t)` besitzt auf dem selben Rang-2-Raum keine von Null verschiedene positive semidefinite Hilbertmetrik, die sie unitär/invariant macht. Eine erfolgreiche positive Erweiterung darf also nicht einfach `rho` auf `C^2` in eine unitäre Hilbertdarstellung umetikettieren.
2. **Positive Konstruktion:** Sobald die bereits vorhandenen Prime-Kanäle zusammen mit den normalisierten Exponentialmomenten `E_±` verwendet werden, entsteht eine kanonisch normalisierte positive Prime-moment-Featureabbildung. Ihr Hilbertnormquadrat ist **exakt**
   `|E_+|^2+|E_-|^2`, und der archimedische `R_0`-Term ist die Kompression einer kanonischen Zielraum-Involution durch genau dieselbe Abbildung.

Damit ist die minimale positive Rang-2-Masse nicht mehr nur eine abstrakt mögliche Diagonalergänzung. Sie wird in einer engen, vorab natürlichen Prime-moment-Klasse vorwärts aus vorhandenen Prime-Kanälen, Weilgewichten und `E_±` erzeugt.

**Firewall:** Dies ist noch keine kontraktive Einbettung in die vollständige positive Featureform `G_a^+`. Der nächste echte Gate ist deshalb ein Feature-Shorting-/Kontraktionsproblem.

---

## 1. Ausgangsdaten

Wie in OX-GEN-A sei

```math
\rho(t)=
\begin{pmatrix}
e^{-t/2}&0\\
0&e^{t/2}
\end{pmatrix},
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
J=-P.
```

Setze

```math
S=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
```

Dann

```math
\boxed{\rho(t)=e^{tS/2},\qquad 2\rho'(0)=S,\qquad S^2=P^2=I,\qquad PSP=-S.}
```

Insbesondere

```math
P\rho(t)P=\rho(-t).
```

Für

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}
```

gilt auf dem Rang-2-Quotienten

```math
\boxed{\mathcal EK_n=D_n\mathcal E,\qquad D_n=\lambda_nS.}
```

Die `R_0`-Form ist

```math
\boxed{R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle_{\mathbb C^2}.}
```

---

## 2. Krein-/Boost-Struktur der Generator-Ebene `✓[M]`

Aus `SJS=-J` folgt äquivalent `SJ=-JS`. Daher

```math
\rho(t)^*J\rho(t)=J.
```

Die Translationen sind auf der OX-GEN-Ebene also `J`-unitäre hyperbolische Boosts, nicht unitäre Operatoren für die positive Standardmetrik.

Außerdem

```math
D_n^*JD_n=-\lambda_n^2J,
```

wie bereits in OX-GEN-A gebucht.

Die zusätzliche Beobachtung hier ist, dass der normalisierte Prime-Kanal

```math
\boxed{D_n/\lambda_n=S=2\rho'(0)}
```

für **jedes** `n>=2` derselbe involutive Boost-Generator ist. Die diskreten Prime-Kanäle wählen daher keine neue Richtung im Quotientenraum; sie sampeln dieselbe Generatorrichtung mit verschiedenen Skalaren `lambda_n`.

---

## 3. POS-DIL-1A — minimale natürliche Companion-Klasse

Wir definieren als erste enge positive Companion-Klasse die Hermiteformen `M>=0` auf `C^2`, die beide bereits vorhandenen involutiven Symmetrien respektieren:

```math
\boxed{PMP=M,\qquad SMS=M.}
```

Diese Wahl ist bewusst schwächer als volle `rho`-Invarianz:

- `P` ist die räumliche Spiegelung auf dem Quotienten;
- `S=D_n/\lambda_n=2\rho'(0)` ist der von jedem nichttrivialen Prime-Kanal gelieferte normalisierte Generator;
- es wird keine unbekannte Weilform und kein nachträglich gefitteter Operator eingeführt.

Als positive Begleiter von `J` betrachten wir zusätzlich die Schur-/Blockbedingung

```math
\boxed{
\mathcal B(M)=
\begin{pmatrix}
M&J\\
J&M
\end{pmatrix}\succeq0.
}
```

Diese Klasse ließ vorab beide Ausgänge zu: sie hätte leer sein oder eine nichttriviale Familie positiver Begleiter enthalten können.

### Satz 3.1 — Symmetrierigidität `✓[M]`

Ist `M` hermitesch und erfüllt

```math
PMP=M,
\qquad
SMS=M,
```

so gilt notwendig

```math
\boxed{M=tI}
```

mit reellem `t`.

**Beweis.** Schreibe

```math
M=\begin{pmatrix}a&b\\\bar b&d\end{pmatrix}.
```

Aus `PMP=M` folgt `a=d` und `b\in\mathbb R`. Aus `SMS=M` folgt `b=0`. Also `M=aI`. `□`

### Satz 3.2 — scharfer positiver Begleiter `✓[M]`

Für `M=tI` gilt

```math
\mathcal B(tI)\succeq0
\quad\Longleftrightarrow\quad
t\ge1.
```

Denn `J` besitzt die Eigenwerte `±1`; die Blockmatrix zerfällt in die Eigenwerte `t±1`.

Folglich ist innerhalb der POS-DIL-1A-Klasse

```math
\boxed{M_{\min}=I}
```

der eindeutige minimale positive Begleiter.

Damit ist die Masse

```math
\boxed{\|\mathcal Ev\|^2=|E_+(v)|^2+|E_-(v)|^2}
```

nicht nur eine algebraisch mögliche Wahl: Spiegelung plus normalisierter Prime-Generator erzwingen sie bis auf einen Skalar, und die positive Schur-Bedingung fixiert den minimalen Skalar auf `1`.

**Minimalitäts-Firewall:** Gemeint ist die eindeutige minimale Form **innerhalb dieser vorab definierten Symmetrieklasse**, kein universeller Satz über alle denkbaren positiven Erweiterungen.

---

## 4. POS-DIL-1B — No-Go für volle positive `rho`-Invarianz `×[M]`

Nehme eine positive semidefinite Hermiteform `M` auf `C^2` mit

```math
\rho(t)^*M\rho(t)=M
```

für alle reellen `t`.

Ableiten bei `t=0` liefert

```math
SM+MS=0.
```

Für

```math
M=\begin{pmatrix}a&b\\\bar b&d\end{pmatrix}
```

folgt

```math
a=d=0.
```

Damit ist

```math
M=\begin{pmatrix}0&b\\\bar b&0\end{pmatrix}.
```

Eine solche Matrix ist nur dann positiv semidefinit, wenn `b=0`. Also

```math
\boxed{M=0.}
```

### Korollar 4.1 — kein exaktes unitäres Hilbert-Intertwining auf positivem Rang 2

Es gibt keine injektive Abbildung `V:C^2->H` in einen Hilbertraum und keine unitäre Gruppe `U_t` mit

```math
V\rho(t)=U_tV
```

für alle `t`.

Denn dann wäre `M=V^*V>0` und wegen der Unitärität `rho(t)^*M rho(t)=M`, im Widerspruch zum Satz.

**Scope:** Ausgeschlossen ist nur diese exakte positive/unitäre Intertwinerklasse. Größere Transferfunktionen, Koligationen, Kompressionen oder nichtunitäre positive Zielraumaktionen sind dadurch nicht ausgeschlossen.

---

## 5. POS-DIL-1C — Prime-moment Hilbertisierung `✓[M]`

Sei `N` eine endliche nichtleere Menge von Prime-Power-Indizes mit

```math
w_n=\frac{\Lambda(n)}{\sqrt n}>0.
```

Setze

```math
\boxed{
\kappa_N=\sum_{n\in N}w_n\lambda_n^2>0.
}
```

Definiere den positiven Hilbertraum

```math
\mathcal H_N=\bigoplus_{n\in N}\mathbb C^2
```

mit dem direkten Summen-Skalarprodukt und die Abbildung

```math
\boxed{
\iota_N z
=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,D_nz\bigr)_{n\in N}.
}
```

Da

```math
D_n^*D_n=\lambda_n^2I,
```

folgt exakt

```math
\boxed{\iota_N^*\iota_N=I.}
```

`iota_N` ist also eine Isometrie des Rang-2-Quotienten in einen positiven Hilbertraum.

Nun setze auf `H_N`

```math
\mathbb P_N=\bigoplus_{n\in N}P.
```

Wegen

```math
D_n^*PD_n
=\lambda_n^2SPS
=-\lambda_n^2P
=\lambda_n^2J
```

gilt

```math
\boxed{\iota_N^*\mathbb P_N\iota_N=J.}
```

Sogar die stärkere Intertwinerrelation gilt:

```math
\boxed{\mathbb P_N\iota_N=\iota_NJ.}
```

Die indefinite `J`-Form ist damit die Einschränkung einer selbstadjungierten unitären Involution auf demselben positiven Zielraum, dessen Norm die minimale positive Companion-Masse liefert.

---

## 6. Dieselbe Abbildung kommt direkt aus den vorhandenen Prime-Kanälen

Für Testfunktionen setze

```math
\boxed{
V_Nv=\iota_N\mathcal Ev.
}
```

Mit `E K_n=D_n E` folgt die vorwärts gerichtete Formel

```math
\boxed{
V_Nv
=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal E K_nv\bigr)_{n\in N}.
}
```

Die Konstruktion benutzt also genau:

- die vorhandenen Prime-Kanäle `K_n`;
- ihre Weilgewichte `w_n`;
- die bereits kanonisch normalisierten Funktionale `E_±`;
- eine einzige globale Normierung `kappa_N^{-1/2}`, die durch die Isometriebedingung erzwungen ist.

Kein `Q_{B_a}`, keine Weil-Positivität, keine RH-Annahme und keine rückwärts definierte Positivitätswurzel werden verwendet.

### Satz 6.1 — positive Masse als Prime-moment-Gram `✓[M]`

Für alle zulässigen `v,w` gilt

```math
\boxed{
\langle V_Nv,V_Nw\rangle_{\mathcal H_N}
=\langle\mathcal Ev,\mathcal Ew\rangle_{\mathbb C^2}.
}
```

Insbesondere

```math
\boxed{
\|V_Nv\|^2
=|E_+(v)|^2+|E_-(v)|^2.
}
```

Äquivalent:

```math
\boxed{
|E_+(v)|^2+|E_-(v)|^2
=\frac{1}{\kappa_N}
\sum_{n\in N}w_n\,\|\mathcal EK_nv\|_{\mathbb C^2}^2.
}
```

### Satz 6.2 — `R_0` im selben positiven Zielraum `✓[M]`

Für alle zulässigen `v,w` gilt

```math
\boxed{
R_0(v,w)
=\langle V_Nv,\mathbb P_NV_Nw\rangle_{\mathcal H_N}.
}
```

Damit entstehen der positive Minimalbegleiter und die indefinite archimedische Kreuzform aus **derselben** Prime-moment-Featureabbildung:

```text
positive Hilbertnorm on H_N  --->  |E_+|^2+|E_-|^2
same feature + involution P  --->  R_0
```

Dies ist der erste positive Hilbertraum-Umraum des OX-GEN-Rang-2-Blocks, der nicht durch Einsetzen einer beliebigen Blockdiagonale konstruiert wird, sondern durch vorhandene Prime-Kanäle und Weilgewichte.

---

## 7. Semidirektprodukt-Intertwining

Definiere auf `H_N`

```math
\boldsymbol\rho_N(t)=\bigoplus_{n\in N}\rho(t).
```

Da `D_n` und `rho(t)` beide Funktionen von `S` sind,

```math
D_n\rho(t)=\rho(t)D_n.
```

Also

```math
\boxed{\boldsymbol\rho_N(t)\iota_N=\iota_N\rho(t).}
```

Für die räumliche Spiegelung auf dem Quotienten ist wegen `D_nP=-PD_n`

```math
\boxed{(-\mathbb P_N)\iota_N=\iota_NP.}
```

Damit wird die Semidirektprodukt-Struktur exakt in den positiven Zielraum transportiert. Die Zielraum-Translationen `boldsymbol rho_N(t)` sind dabei weiterhin hyperbolisch und **nicht unitär** für die positive Hilbertnorm, im Einklang mit dem No-Go aus §4.

---

## 8. Direkte Verbindung zur AR(1)-Root/Hub-Struktur `✓[M]`

Für `n=p^k` setze

```math
q_p=p^{-1/2},
\qquad
u_{p,k}=q_p^k.
```

`nu_{p,k}` ist genau die Root-Komponente des AR(1)-Vektors `u_k=q^k` aus

```math
T_q^*T_q+uu^*=R_q.
```

Nun gilt

```math
\sqrt{w_{p,k}}\,\lambda_{p^k}
=\sqrt{\log p}\,p^{-k/4}
\bigl(p^{k/4}-p^{-k/4}\bigr)
=\sqrt{\log p}\,(1-q_p^k).
```

Daher

```math
\boxed{
\sqrt{w_{p,k}}\,D_{p^k}
=\sqrt{\log p}\,(1-u_k)S.
}
```

Die Kanalindex-Amplitude der Prime-moment-Dilatation ist also auf jedem Primast exakt

```text
flat coordinate  minus  AR(1) root coordinate.
```

Dies ist eine neue exakte Brücke zwischen der OX-GEN-Quotientenebene und der bereits vorhandenen Root/Hub-AR(1)-Geometrie.

**Firewall:** Daraus folgt nicht, dass der P11-Huboperator selbst mit `E_±` identifiziert wäre. Bewiesen ist die Gleichheit der Kanalindex-Amplitude `1-u_k` in der hier definierten Momentkompression.

---

## 9. Gewichtete Normierung

Für den vollständigen Prime-Power-Cutoff `n<=X` ist

```math
\kappa_X
=\sum_{n\le X}w_n\lambda_n^2.
```

Die bereits in OX-GEN-A bewiesene Generatoridentität liefert

```math
\boxed{
\kappa_X
=\psi(X)-A_X+\sum_{n\le X}\frac{\Lambda(n)}n,
\qquad
A_X=2\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.
}
```

Damit ist auch die globale Normierung der Prime-moment-Hilbertisierung vollständig durch bereits vorhandene arithmetische Daten bestimmt.

**Firewall:** `kappa_X` ist nicht mit Suzukis Skalarblock `c_a` identifiziert. Die vorliegende Konstruktion erklärt `c_aI` nicht.

---

## 10. Bezug zur lokalisierten positiven Prime-Featuregeometrie

Auf einem festen Fenster `H_0^1(-a,a)` ist `K_nv` kompakt getragen. Die Momentabbildung

```math
h\mapsto\mathcal Eh
```

ist auf dem kanonischen endlichen Träger von `K_nv` ein beschränkter Operator nach `C^2`.

Ist die im lokalen Prime-Featureblock tatsächlich verwendete aktive Menge

```math
N_a=\{n:\Lambda(n)>0,\ n\le e^{2a}\}
```

nichtleer, dann ist

```math
V_{N_a}v
=\kappa_{N_a}^{-1/2}
\bigl(\mathcal E(\sqrt{w_n}K_nv)\bigr)_{n\in N_a}
```

eine **gebundene, explizite Moment-Postkompression der bereits vorhandenen positiven Prime-Features**.

Für die Konvention `n<=e^{2a}` ist `N_a` ab

```math
a\ge\frac12\log2
```

nichtleer.

Unterhalb dieser Schwelle liefert der lokalisierte aktive Primeblock selbst keine solche Realisierung; dort müsste eine positive Kopplung zusätzliche globale Primekanäle oder die `log|D|`-/andere positive Geometrie verwenden.

---

## 11. Was dieser POS-DIL-1-Pass **nicht** beweist

Die Konstruktion ist absichtlich enger als ein vollständiger OX-GEN-A2'-Abschluss.

Nicht bewiesen ist:

1. dass `V_N` eine kontraktive Postkompression der **vollen** positiven Featureabbildung von `G_a^+` ist;
2. dass
   ```math
   \|\mathcal Ev\|^2\le G_a^+(v)
   ```
   im relevanten Scope gilt;
3. dass der volle Prime-Gramoperator durch `E` descendiert — das frühere No-Go bleibt unverändert;
4. dass die großen orthogonalen Komplementrichtungen der Prime-Features geometrisch irrelevant wären;
5. dass `log|D|`, `r_1` oder `c_aI` bereits integriert sind;
6. irgendeine vollständige positive Weil-Gram-Identität;
7. Object X oder RH.

Der Zielraum `H_N` ist größer als `C^2`, aber der von `iota_N` erzeugte Bereich ist weiterhin zweidimensional. Der Fortschritt liegt daher **nicht** in einer Dimensionsvergrößerung an sich, sondern darin, dass die positive Companion-Masse und `R_0` durch dieselbe vorwärts aus den echten Prime-Featureausgängen gebaute Momentabbildung realisiert werden.

---

## 12. Neuer echter Gate — POS-DIL-2 / FEATURE-SHORTING

Nach POS-DIL-1 lautet die nächste nichtzirkuläre Frage:

> **POS-DIL-2 / FEATURE-SHORTING.** Ist die kanonische Prime-moment-Abbildung auf dem relevanten positiven Featurebereich kontraktiv bzw. als kanonisches Shorting/Schur-Komplement der vollständigen positiven Prime-/`log|D|`-Geometrie realisierbar?

Eine scharfe erste Form ist

```math
\boxed{
\|\mathcal Ev\|^2\stackrel?\le G_a^+(v).
}
```

oder, äquivalent sobald die Featureabbildung typkorrekt als Hilbertraumabbildung fixiert ist, die Existenz einer **vorwärts definierten kontraktiven** Zielraumabbildung `C_a` mit

```math
C_a\mathcal F_a^+v=V_{N_a}v.
```

Diese Frage lässt beide Ausgänge offen:

- **PASS:** die minimale positive Rang-2-Masse sitzt tatsächlich kontraktiv in der vorhandenen positiven Featuregeometrie;
- **FAIL:** die Prime-moment-Hilbertisierung existiert, ist aber nicht als kontraktiver Defekt-/Schurbaustein der vorhandenen `G_a^+`-Geometrie verwendbar; dann muss die natürliche Klasse weiter verengt oder um Root/Hub-/`log|D|`-Struktur erweitert werden.

Dieser Gate verwendet weiterhin weder die fertige Weilform noch RH.

---

## 13. Statusbuchung

```text
POS-DIL-1A symmetry-rigid companion M=tI              ✓[M]
minimal block-positive companion M=I                  ✓[M]
full-rho positive same-space Hilbertization           ×[M]  [enger Scope]
Prime-moment Hilbertization V_N                       ✓[M]
R_0 from same positive target via target involution   ✓[M]
AR(1) root-complement amplitude 1-u_k                 ✓[M]
OX-GEN-A2' overall                                    ✓[M]_part
POS-DIL-2 / FEATURE-SHORTING                          ?[O]
r_1 / c_aI / full Object-X realization / RH           ?[O]
```

Keine Registry-Promotion aus diesem Audit allein.