# P11 Audit — NULLPOL common jump-Gram geometry

**Datum:** 13. September 2026  
**Rolle:** theorem-level mathematischer Audit der aktuellen `NULLPOL-CORE`-Front.  
**Basis-Head:** `5efe38355d58fa4da67facb04b59c9717b1bf9a2` (PR #106).  
**Registry:** unverändert.  
**Object-X-Arbeitsdefinition:** unverändert.

## 0. Kurzurteil

Dieser Audit konstruiert aus der expliziten Weil-Formel eine gemeinsame positive Hilbert-/Gram-Geometrie, in der der archimedische Nichtpol-Anteil und die Prime-Power-Anteile **durch exakt dieselbe Translation-Differenz-Familie** erzeugt werden.

Für

```math
K_t:=T_{t/2}-T_{-t/2},\qquad t>0,
```

tritt archimedisch die positive kontinuierliche Dichte

```math
h(t):=\frac{e^{-t/2}}{1-e^{-2t}}
=\frac{e^{t/2}}{e^t-e^{-t}}>0
```

auf, während jede Primzahlpotenz `n=p^k` ein Atom bei `t=log n` mit Gewicht

```math
w_n:=\frac{\Lambda(n)}{\sqrt n}
```

liefert.

Für `v,w` mit Träger in `[-a,a]` wird eine positive Featureform

```math
\langle\mathcal X_a v,\mathcal X_a w\rangle
:=
\int_0^\infty h(t)\langle K_t v,K_t w\rangle\,dt
+
\sum_{\substack{n=p^k\\ \log n\le2a}}
w_n\langle K_{\log n}v,K_{\log n}w\rangle
```

definiert. Dann gilt exakt

```math
\boxed{
Q_W(v,w)
=
\langle\mathcal Ev,P\mathcal Ew\rangle
+
\langle\mathcal X_a v,\mathcal X_a w\rangle
-
\Gamma_a\langle v,w\rangle,
}
```

mit

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix},
```

und

```math
\boxed{
\Gamma_a
=
2\sum_{\substack{n=p^k\\ \log n\le2a}}
\frac{\Lambda(n)}{\sqrt n}
+
\kappa_*,
\qquad
\kappa_*:=\log\pi-\psi(1/4).
}
```

Die archimedische Konstante besitzt äquivalent die geschlossene Form

```math
\boxed{
\kappa_*
=
\log(8\pi)+\gamma+\frac\pi2.
}
```

Auf der Nullpolklasse

```math
\mathscr D_{NP}
:=
\{v:M(v)(0)=M(v)(1)=0\}
```

verschwindet der Rang-2-Polblock und es bleibt

```math
\boxed{
Q_W(v,w)
=
\langle\mathcal X_a v,\mathcal X_a w\rangle
-
\Gamma_a\langle v,w\rangle.
}
```

**Status:**

```text
same K_t family for archimedean + prime powers       ✓[M]
positive mixed jump-Gram form                        ✓[M]
closed archimedean threshold kappa_*                 ✓[M]
exact full pole+Gram-threshold normal form            ✓[M]
exact NULLPOL Gram-threshold normal form              ✓[M]
cutoff-gauge covariance of (Gram, threshold)          ✓[M]
NP-COMMON construction                                ✓[M]
forward Object-X candidate architecture               ✓[M]_part
full positive Object-X realization / RH               ?[O]
publication novelty                                   ?[O]
```

Der Fortschritt ist **nicht**, dass `Q_W>=0` bewiesen wäre. Der Fortschritt ist, dass nach Nullpol der gesamte nichtskalare Weil-Defekt in **einer einzigen positiven Prime/archimedischen Hilbert-Geometrie** liegt. Die verbleibende RH-Information ist ein scharfer Spektral-/Frame-Gap gegen den expliziten Skalar `Gamma_a`.

---

# 1. Ausgangsformel

Wir benutzen die additive Weil-Normierung aus Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2. Für geeignete Testfunktionen `f`:

```math
\begin{aligned}
W(f)
={}&
\int_{-\infty}^{\infty}
f(x)(e^{x/2}+e^{-x/2})\,dx\\
&-\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}f(\log n)
-\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}f(-\log n)\\
&-(\log4\pi+\gamma)f(0)\\
&-\int_0^\infty
\{f(t)+f(-t)-2e^{-t/2}f(0)\}
\frac{e^{t/2}}{e^t-e^{-t}}\,dt.
\end{aligned}
```

Setze

```math
Q_W(v,w):=W(v*\widetilde w),
\qquad
\widetilde w(x)=\overline{w(-x)}.
```

Alle folgenden Umformungen sind direkte algebraische Umformungen dieser expliziten Formel. Insbesondere wird **keine** Weil-Positivität und keine RH-Annahme verwendet.

---

# 2. Autokorrelation und der gemeinsame Kanal

Wir verwenden die unitäre Translation

```math
(T_tu)(x)=u(x-t)
```

auf `L^2(R)` und definieren

```math
K_t:=T_{t/2}-T_{-t/2}.
```

Da

```math
K_t^*K_t
=2I-T_t-T_{-t},
```

gilt polarisiert

```math
\boxed{
\langle K_t v,K_t w\rangle
=2\langle v,w\rangle
-\langle v,T_t w\rangle
-\langle v,T_{-t}w\rangle.
}
```

Für

```math
f=v*\widetilde w
```

ist

```math
f(0)=\langle v,w\rangle,
```

sowie

```math
f(t)=\langle v,T_t w\rangle,
\qquad
f(-t)=\langle v,T_{-t}w\rangle.
```

Somit

```math
\boxed{
f(t)+f(-t)
=2f(0)-\langle K_t v,K_t w\rangle.
}
```

Das ist die zentrale Identität des Audits.

---

# 3. Der Polblock

Definiere

```math
E_+(v)=\int_{\mathbb R}e^{x/2}v(x)\,dx,
\qquad
E_-(v)=\int_{\mathbb R}e^{-x/2}v(x)\,dx,
```

und

```math
\mathcal Ev=(E_+(v),E_-(v))^T.
```

Fubini liefert

```math
\int_{\mathbb R}(v*\widetilde w)(x)e^{x/2}\,dx
=E_+(v)\overline{E_-(w)},
```

```math
\int_{\mathbb R}(v*\widetilde w)(x)e^{-x/2}\,dx
=E_-(v)\overline{E_+(w)}.
```

Mit

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}
```

ist daher der gesamte Polbeitrag

```math
\boxed{
E_+(v)\overline{E_-(w)}
+E_-(v)\overline{E_+(w)}
=\langle\mathcal Ev,P\mathcal Ew\rangle.
}
```

Dies ist genau `-R_0` in der bisherigen OX-GRAM-Konvention.

Da

```math
M(v)(0)=E_-(v),
\qquad
M(v)(1)=E_+(v),
```

verschwindet dieser Term auf `D_NP` identisch.

---

# 4. Prime-Power-Terme sind exakt K_t-Atome

Setze

```math
w_n:=\frac{\Lambda(n)}{\sqrt n}.
```

Für `t_n=log n` gilt

```math
-f(t_n)-f(-t_n)
=
\langle K_{t_n}v,K_{t_n}w\rangle
-2\langle v,w\rangle.
```

Daher ist der gesamte Prime-Power-Beitrag

```math
\boxed{
\sum_{n\ge2}w_n
\left(
\langle K_{\log n}v,K_{\log n}w\rangle
-2\langle v,w\rangle
\right).
}
```

Diese Schreibweise ist als **zentrierte** Summe lokal endlich: Sind `v,w` in `[-a,a]` getragen und `log n>=2a`, dann sind die beiden verschobenen Träger disjunkt und

```math
\langle K_{\log n}v,K_{\log n}w\rangle
=2\langle v,w\rangle.
```

Somit verschwinden alle ausreichend großen zentrierten Summanden exakt.

Für eine positive Gramdarstellung wählen wir die endliche aktive Menge

```math
\mathcal P_a
:=
\{n=p^k:\log n\le2a\}.
```

Ob ein Grenzfall `log n=2a` ein- oder ausgeschlossen wird, ändert die zentrierte Form nicht, da der zugehörige Summand exakt null ist.

---

# 5. Der archimedische Integralterm ist derselbe K_t-Kanal

Definiere

```math
\boxed{
h(t):=
\frac{e^{t/2}}{e^t-e^{-t}}
=
\frac{e^{-t/2}}{1-e^{-2t}},
\qquad t>0.
}
```

Offensichtlich gilt

```math
h(t)>0.
```

Der Integralterm der expliziten Formel ist

```math
-\int_0^\infty
\{f(t)+f(-t)-2e^{-t/2}f(0)\}
h(t)\,dt.
```

Mit der Identität aus §2 wird dies exakt

```math
\begin{aligned}
&-\int_0^\infty
\left(
2f(0)-\langle K_tv,K_tw\rangle
-2e^{-t/2}f(0)
\right)h(t)\,dt\\
&=
\int_0^\infty
h(t)\langle K_tv,K_tw\rangle\,dt
-
2\langle v,w\rangle
\int_0^\infty h(t)(1-e^{-t/2})\,dt.
\end{aligned}
```

Damit ist der gesamte nichtskalare archimedische Nichtpol-Term bereits eine positive `K_t`-Gramform.

---

# 6. Exakte Auswertung der archimedischen Schwelle

Setze

```math
J
:=
2\int_0^\infty h(t)(1-e^{-t/2})\,dt.
```

Mit

```math
x=e^{-t/2}
```

erhält man

```math
\begin{aligned}
J
&=4\int_0^1
\frac{dx}{(1+x)(1+x^2)}.
\end{aligned}
```

Die Partialbruchzerlegung

```math
\frac1{(1+x)(1+x^2)}
=
\frac1{2(1+x)}
+\frac{1-x}{2(1+x^2)}
```

liefert

```math
\int_0^1\frac{dx}{(1+x)(1+x^2)}
=
\frac14\log2+\frac\pi8.
```

Also

```math
\boxed{
J=\log2+\frac\pi2.
}
```

Zusammen mit dem bereits explizit auftretenden Term

```math
\log4\pi+\gamma
```

folgt die feste archimedische Schwelle

```math
\boxed{
\kappa_*
=
\log4\pi+\gamma+J
=
\log(8\pi)+\gamma+\frac\pi2.
}
```

Mit der klassischen Digamma-Identität

```math
\psi(1/4)=-\gamma-\frac\pi2-3\log2
```

wird dies zu

```math
\boxed{
\kappa_*=\log\pi-\psi(1/4).
}
```

Diese Form ist intrinsisch archimedisch und stimmt mit dem `psi(1/4)-log pi`-Term in Suzukis Schraubenfunktionsentwicklung überein.

### Numerischer Gegencheck

Unabhängige Hochpräzisionsquadratur wurde für

```text
a = 0.2, 0.5, 0.8, 1.0
```

an der äquivalenten endlichen Renormierung durchgeführt; Integral- und geschlossene Form stimmten bis etwa `1e-42` überein. Dieser Gegencheck ist nur Diagnose; der Beweis oben ist exakt.

---

# 7. Die positive gemischte Hilbert-Geometrie

Für `a>0` definiere die positive gemischte Sprungmaß-Struktur

```math
\boxed{
\mu_a
=
h(t)\,dt
+
\sum_{n\in\mathcal P_a}w_n\delta_{\log n}.
}
```

Archimedisch ist sie kontinuierlich, nichtarchimedisch rein atomar.

Wichtig ist: **Beide Teile benutzen exakt dieselbe Operatorfamilie `K_t`.**

Ein natürlicher Hilbert-Zielraum ist

```math
\mathscr H_a
:=
L^2\bigl((0,\infty),h(t)dt;L^2(\mathbb R)\bigr)
\oplus
\bigoplus_{n\in\mathcal P_a}L^2(\mathbb R),
```

und die Featureabbildung

```math
\boxed{
\mathcal X_av
=
\left(
[t\mapsto K_tv],
[\sqrt{w_n}K_{\log n}v]_{n\in\mathcal P_a}
\right).
}
```

Dann

```math
\boxed{
\langle\mathcal X_av,\mathcal X_aw\rangle_{\mathscr H_a}
=
\int_0^\infty h(t)\langle K_tv,K_tw\rangle\,dt
+
\sum_{n\in\mathcal P_a}w_n
\langle K_{\log n}v,K_{\log n}w\rangle.
}
```

### Wohldefiniertheit

Für `v in H^1(R)` gilt für kleine `t`

```math
\|K_tv\|_2\le t\|v'\|_2.
```

Da

```math
h(t)\sim\frac1{2t}
\quad(t\downarrow0),
```

ist der Integrand nahe `0` von Ordnung `O(t)`.

Für große `t` gilt

```math
\|K_tv\|_2\le2\|v\|_2,
```

und

```math
h(t)=O(e^{-t/2}).
```

Somit ist der kontinuierliche Featurekanal insbesondere auf `C_c^infty` und `H^1` wohldefiniert.

---

# 8. Exakte gemeinsame Normalform

Setze

```math
A_a^{\rm prime}
:=
2\sum_{n\in\mathcal P_a}w_n
```

und

```math
\boxed{
\Gamma_a
:=
A_a^{\rm prime}+\kappa_*
=
2\sum_{n\in\mathcal P_a}\frac{\Lambda(n)}{\sqrt n}
+\log\pi-\psi(1/4).
}
```

Das Einsetzen der §§3–6 in die explizite Weil-Formel ergibt polarisiert:

```math
\boxed{
Q_W(v,w)
=
\langle\mathcal Ev,P\mathcal Ew\rangle
+
\langle\mathcal X_av,\mathcal X_aw\rangle
-
\Gamma_a\langle v,w\rangle,
}
```

für `v,w in C_c^infty(R)` mit Träger in `[-a,a]`.

Kein Teil dieser Identität benutzt RH.

Dies ist die neue **COMMON-JUMP-GRAM normal form**.

---

# 9. Nullpol-Reduktion

Auf

```math
\mathscr D_{NP}
=
\ker M(0)\cap\ker M(1)
```

gilt

```math
\mathcal Ev=0.
```

Daher reduziert sich die Form exakt zu

```math
\boxed{
Q_W(v,w)
=
\langle\mathcal X_av,\mathcal X_aw\rangle
-
\Gamma_a\langle v,w\rangle,
\qquad
v,w\in\mathscr D_{NP},
\quad
\operatorname{supp}v,\operatorname{supp}w\subset[-a,a].
}
```

Insbesondere

```math
\boxed{
Q_W(v)
=
\|\mathcal X_av\|^2
-
\Gamma_a\|v\|_2^2.
}
```

Damit sind nach Nullpol

- `R_0` vollständig verschwunden;
- `R_1` kein separater offener Geometriebaustein mehr;
- der `log|D|`-Anteil kein separater Geometriebaustein mehr;
- Prime-Power- und archimedische Nichtpol-Beiträge Teil **derselben** positiven Featurefamilie.

Der einzig verbleibende Defekt ist die scharfe skalare Schwelle `Gamma_a`.

---

# 10. Fourier-/Symbol-Gegencheck

Die archimedische Digamma-Differenz besitzt die positive Darstellung

```math
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)
-\psi\left(\frac14\right)
=
2\int_0^\infty h(t)(1-\cos zt)\,dt.
```

Ferner

```math
\|K_t\|_{\text{Fourier-Symbol}}^2
=2(1-\cos zt).
```

Damit hat die positive Common-Jump-Form auf der reellen Fourierachse das Symbol

```math
\boxed{
\Phi_a(z)
=
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)
-\psi(1/4)
+
2\sum_{n\in\mathcal P_a}w_n(1-\cos(z\log n)).
}
```

und

```math
\Phi_a(z)\ge0
\qquad(z\in\mathbb R),
```

weil sie bereits als Gram-Symbol konstruiert wurde.

Außerdem

```math
\Phi_a(0)=0.
```

Die zentrierte Weilform auf Nullpol ist gerade

```math
\Phi_a(D)-\Gamma_a I.
```

Einsetzen von `Gamma_a` liefert exakt Suzukis Fourier-Multiplikator ohne Polblock:

```math
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)
-\log\pi
-2\sum_{n\in\mathcal P_a}w_n\cos(z\log n).
```

Dies ist ein unabhängiger algebraischer Vorzeichen-/Faktorcheck.

---

# 11. Exakte Cutoff-Gauge-Kovarianz

Seien `0<a<b` und `v,w` bereits in `[-a,a]` getragen.

Jedes neue Prime-Power-Atom des größeren Cutoffs erfüllt

```math
2a<\log n\le2b.
```

Dann sind die beiden verschobenen Träger disjunkt und

```math
\boxed{
\langle K_{\log n}v,K_{\log n}w\rangle
=2\langle v,w\rangle.
}
```

Beim Übergang `a -> b` wächst daher die positive Gramform um

```math
2\sum_{\substack{n:\ 2a<\log n\le2b}}w_n\langle v,w\rangle,
```

und die Schwelle `Gamma` wächst um **genau denselben Skalar**.

Somit

```math
\boxed{
\langle\mathcal X_bv,\mathcal X_bw\rangle
-
\Gamma_b\langle v,w\rangle
=
\langle\mathcal X_av,\mathcal X_aw\rangle
-
\Gamma_a\langle v,w\rangle.
}
```

Das löst die bisherige Skalar-Gauge-Frage strukturell:

> Der isolierte Skalar ist nicht invariant; invariant ist die **zentrierte Gram-Paarung** `(positive feature Gram, matching threshold)`.

Die früheren Exterior-shell-Sätze sind damit keine getrennte Zusatzgeometrie, sondern die endliche Cutoff-Gauge-Kovarianz genau dieser Common-Jump-Struktur.

---

# 12. RH-äquivalente Spektralgap-Fassung

Connes–Consani Proposition C.1 liefert als importierten globalen Satz die RH-Äquivalenz der Weil-Vorzeichenbedingung auf der Nullpolklasse.

Jede kompakt getragene Nullpol-Testfunktion liegt in irgendeinem Fenster `[-a,a]`. Daher ist global äquivalent:

```math
\boxed{
RH
\Longleftrightarrow
\|\mathcal X_av\|^2
\ge
\Gamma_a\|v\|_2^2
}
```

für **jedes** `a>0` und jede glatte kompakt getragene Nullpol-Testfunktion mit Träger in `[-a,a]`.

Äquivalent ist die untere Frame-/Spektralgap-Bedingung

```math
\boxed{
\lambda_{NP}(a)
:=
\inf_{\substack{0\ne v\in C_c^\infty(-a,a)\\M(v)(0)=M(v)(1)=0}}
\frac{\|\mathcal X_av\|^2}{\|v\|_2^2}
\ge\Gamma_a
\quad\text{für alle }a>0.
}
```

### Firewall

Nicht behauptet wird, dass die Ungleichung für **ein einzelnes** festes `a` bereits RH-äquivalent wäre. Die Äquivalenz gilt für die Familie aller Fenster beziehungsweise für die globale Nullpolklasse.

---

# 13. Objekt-X-Bedeutung

Vor diesem Audit war die aktuelle Hauptfront:

```text
NP-R1
NP-SCALAR
NP-COMMON
```

Der Audit schließt zwei davon im strukturellen Sinn:

### NP-R1

`R_1` benötigt keine eigene Generatorfamilie. Zusammen mit der logarithmischen archimedischen Form wird er direkt Teil des kontinuierlichen `K_t`-Kanals mit positiver Dichte `h(t)dt`.

Status:

```text
NP-R1 separate geometry question -> geschlossen / subsumiert ✓[M]
```

### NP-COMMON

Die gemeinsame Prime-/archimedische Featurefamilie ist explizit:

```math
K_t=T_{t/2}-T_{-t/2}.
```

Prime powers sind Atome bei `t=log n`; der archimedische Ort ist die kontinuierliche Dichte `h(t)dt`.

Status:

```text
NP-COMMON positive common feature construction ✓[M]
```

### NP-SCALAR

Der nackte Skalar ist weiterhin cutoffabhängig, aber seine Abhängigkeit ist jetzt vollständig geometrisiert: er ist die passende Diagonalbuchung derselben neu eintretenden Prime-Features. Das invariant sinnvolle Objekt ist

```math
\mathcal X_a^*\mathcal X_a-\Gamma_aI.
```

Status:

```text
NP-SCALAR gauge covariance ✓[M]
sharp spectral threshold problem ?[O]
```

### Was ist der neue Engpass?

Nicht mehr die Suche nach einer gemeinsamen Generatorarchitektur.

Sondern nur noch:

```math
\boxed{
\text{Hat die positive Common-Jump-Gramform auf NULLPOL
 den scharfen unteren Frame bound }\Gamma_a
\text{ für alle }a>0?
}
```

Diese Frage ist global RH-äquivalent und darf deshalb nicht durch eine versteckte Rückwärtsdefinition beantwortet werden.

---

# 14. Warum dies als echter Projekt-Durchbruch zählt

Die Objekt-X-Leitregel verlangte entweder

1. einen echten gemeinsamen Baustein zu konstruieren, oder
2. die zulässige Architektur streng zu verkleinern.

Hier passiert beides:

- Prime-Power- und archimedische Nichtpol-Terme werden durch **dieselbe** nichtorthogonale Translation-Differenz-Geometrie erzeugt;
- der archimedische Anteil ist keine post-hoc Korrektur, sondern eine positive kontinuierliche Measure-Komponente derselben `K_t`-Familie;
- der Prime-Anteil ist die atomare Measure-Komponente;
- die bisher getrennten Fragen `log|D|`, `R_1`, exterior-shell mass und Prime shifts werden in einem Objekt vereinigt;
- auf der RH-äquivalenten Nullpolklasse bleibt diese Geometrie vollständig nichttrivial;
- übrig bleibt genau ein scharfer Spektralgap statt mehrerer unverbundener Defekte.

Dies ist daher ein **forward Object-X candidate architecture** im dokumentierten Sinn.

Es ist **noch keine vollständige positive Object-X-Realisierung**, weil

```math
\mathcal X_a^*\mathcal X_a\succeq\Gamma_a I
```

auf NULLPOL gerade die verbleibende tiefe Positivitätsfrage ist.

---

# 15. Literatur-/Neuheitsfirewall

Die verwendeten Ausgangsformeln sind klassisch beziehungsweise explizit in der aktuellen Literatur:

- Weil explizite Formel;
- Suzuki 2026, additive Weil-Normierung und Digamma-/Schraubenfunktionsformeln;
- Connes–Consani, Nullpol-Restriktion als RH-äquivalente globale Testklasse.

Der Audit beansprucht **keine Publikationspriorität** für die hier herausgestellte `K_t`-Jump-Gram-Reorganisation. Eine Websuche fand mindestens eine weitere aktuelle, nicht kanonische RH-Projektquelle mit einer sehr ähnlichen Translation-Energie-Umschreibung. Daher:

```text
Publikationsneuheit ?[O]
```

Der projektinterne mathematische Fortschritt ist davon unabhängig: Die bisherige OX-GRAM/OX-GEN-Front hatte diese vollständige Common-Jump-Identität und die daraus folgende NULLPOL-Spektralgap-Reduktion noch nicht als kanonisches Objekt isoliert.

---

# 16. Nichtbehauptungen

Nicht behauptet wird:

- RH sei bewiesen;
- `Q_W` sei unkonditional positiv;
- der untere Frame bound `Gamma_a` sei bewiesen;
- fixed-`a`-Positivität auf Nullpol sei einzeln RH-äquivalent;
- Publikationsneuheit sei geklärt;
- die Theorem-Registry werde automatisch promoviert;
- die bisherige OX-GEN-A-/POS-DIL-Mathematik sei falsch.

OX-GEN-A bleibt die exakte Polschicht. Die neue Common-Jump-Geometrie ist der nichtpolare positive Gegenpart.

---

# 17. Neuer Forschungsauftrag

Die Generatorfrage ist im beschriebenen Scope nicht mehr die Hauptfrage.

Nächster Gate:

```text
NP-GAP / COMMON-JUMP FRAME BOUND
```

Vorab festgelegt:

1. Arbeite mit dem bereits konstruierten positiven Operator/Formobjekt `X_a^*X_a`.
2. Nutze die Nullpolbedingungen nur vorwärts (z.B. als zwei Momentbedingungen beziehungsweise Fourier-Nullstellen bei `z=±i/2`).
3. Suche einen intrinsischen Mechanismus für den exakten unteren Frame bound `Gamma_a`.
4. Ein Beweis dieses Bounds für alle `a` wäre bereits RH; daher keine zirkuläre Weil-Positivität als Input.
5. Ein enger No-Go gegen natürliche lokale/Poincare-/Schur-Klassen zählt ebenfalls als Fortschritt.

Zusätzlich ist die Fourier-/Paley-Wiener-Fassung zu untersuchen:

```math
M(v)(0)=M(v)(1)=0
\Longleftrightarrow
\widehat v(i/2)=\widehat v(-i/2)=0.
```

Damit wird der neue Engpass zu einem expliziten, positiven, zweifach momentbeschränkten Frame-/Uncertainty-Problem.
