# P11/R32 — SW1 M1-ND SALVAGE-A0 Phase-Diagram Firewall

> **Stand:** 1. September 2026  
> **Branch:** `research/sw1-m1-nd-salvage-phase-diagram`  
> **Status:** Arbeitsdefinition / AI-GREEN candidate scope only; keine Promotion.  
> **Input:** `M1-ND-IMG4-SMALLR: ✓[M]_neg`, IMG3 linear visibility,
> A7/A8 FREE graphing, IMG4 Mass-Transport/Reducing mechanism.

---

## 1. Zweck

Nach der negativen Promotion des expliziten Small-`R`-Witness ist die
universelle SW1-Injektivitätsfrage beendet. Die neue Frage ist nicht

\[
\ker\mathscr N_R=\{0\}\quad\text{auf ganz SW1?}
\]

sondern:

> Wo liegt die tatsächliche geometrische Degenerationsregion, und wo beginnt
> überhaupt ein Parameterbereich, in dem Transversalität noch möglich ist?

Dieses Dokument verhindert insbesondere den Fehlschluss

\[
\boxed{
\text{volle geometrische Sichtbarkeit}
\not\Longrightarrow
\ker\mathscr N_R=\{0\}.
}
\tag{S0.1}
\]

---

## 2. Parameterraum und Defekt

Im unteren SW1-Chamber betrachten wir

\[
0<\varepsilon<\Delta/2,
\qquad
0<R<\varepsilon,
\qquad
0<\sigma<R.
\]

Sei \(U_R\) die Vereinigung der sechs KNF-Samplinghalbfenster und

\[
V_{\varepsilon,R}
:=
\operatorname{Sat}_{\mathcal E_\varepsilon}(U_R)
\]

ihre vollständige Sättigung unter dem tatsächlichen A7/A8-FREE-Graphing.

Sei \(W^{\rm vis}_{\varepsilon,R,\sigma}\subset(R,S)\),
\(S=T+\sigma\), die **tatsächliche** positive Annulus-Sichtbarkeitsmenge
unter den sechs Hub-Source-Maps

\[
|x-a|,\ x+a,\ |x-b|,\ x+b,\ |x-T|,\ x+T.
\]

Definiere den geometrischen Defekt

\[
\boxed{
\beta(\varepsilon,R,\sigma)
:=
\bigl|(R,S)\setminus
W^{\rm vis}_{\varepsilon,R,\sigma}\bigr|.
}
\tag{S0.2}
\]

Die degenerierte geometrische Region ist

\[
\mathcal D_{\rm blind}
=
\{(\varepsilon,R,\sigma):\beta>0\}.
\]

IMG4 liefert dort durch denselben Reducing-/Blindset-Mechanismus einen
nichttrivialen zulässigen Kernel.

---

## 3. Drei logisch verschiedene Regime

### BLIND

\[
\boxed{\beta>0.}
\]

Dann existiert ein positiver Annulus-Blindsetanteil. Unter den bereits
promotierten IMG4-Gates folgt ein nichttrivialer zulässiger Kernel.

### VISIBLE

\[
\boxed{\beta=0.}
\]

Dies bedeutet ausschließlich geometrische Supportdeckung.

Es folgt **nicht**

\[
\ker\mathscr N_R=\{0\}.
\]

Koeffizientencancellation, lineare Abhängigkeit und fehlende Transversalität
bleiben möglich.

### TRANSVERSAL

Erst eine quantitative Operatorabschätzung der Form

\[
\boxed{
\|\mathscr N_R(f,g)\|
\ge
c(\varepsilon,R,\sigma)
\bigl(\|f\|+\|g\|\bigr),
\qquad c>0,
}
\tag{S0.3}
\]

oder eine äquivalente exakte Injektivitäts-/Coercivity-Aussage würde den
nichtdegeneraten Bereich schließen.

Damit gilt die zwingende Reihenfolge

\[
\boxed{
\text{BLIND}
\to
\text{VISIBLE}
\to
\text{TRANSVERSAL}.
}
\tag{S0.4}
\]

Keine Stufe darf übersprungen werden.

---

## 4. Wände und Randstrata

Explizit getrennt zu behandeln sind mindestens

\[
\sigma=R,
\qquad
R=\varepsilon,
\qquad
\varepsilon=\Delta/2.
\]

Der aktuelle SALVAGE-Angriff benutzt zunächst nur das offene untere Gebiet.
Der Rand \(R=\varepsilon\) darf als **monotone Majoranten-Geometrie**
verwendet werden, aber nicht als admissibler SW1-Punkt.

---

## 5. Warum \(M_N\le288N+144\) keine uniforme Blindheit beweist

IMG3 liefert für endliche Neumann-Tiefe \(N\)

\[
M_N^{\rm lin}
\le
288N+144
\]

mögliche affine Annulus-Samplingmaps und damit

\[
|W^{\rm vis}_{N}|
\le
(288N+144)R.
\tag{S0.5}
\]

Für fixes \(N\) und \(R\downarrow0\) ist das stark.

Für adaptive Tiefe \(N=N(R)\) folgt aber nur die notwendige
Deckungsbedingung

\[
(288N+144)R\ge S-R.
\]

Insbesondere ist

\[
N=\Omega(1/R)
\]

notwendig, aber die Phasenzahl allein erzwingt **keinen**
\(R\)-unabhängigen Blindanteil.

Tatsächlich: Sobald

\[
(288N+144)R\ge T,
\]

ist die reine Zähl-/Längeninformation mit einer vollständigen Überdeckung
eines Annulusintervalls der Länge \(<T\) kompatibel. Ob die **wirklichen**
Phasenlagen diese Überdeckung erreichen, ist eine zusätzliche geometrische
Frage.

Daher:

\[
\boxed{
M_N\le288N+144
\text{ ist ein Tiefen-No-Go, kein globaler Blindheitsbeweis.}
}
\tag{S0.6}
\]

---

## 6. Monotoner Majoranten-Trick

Für festes \(\varepsilon\) hängt das FREE-Graphing nicht von \(R\) ab.
Aus

\[
0<R_1<R_2<\varepsilon
\]

folgt

\[
U_{R_1}\subset U_{R_2}
\quad\Longrightarrow\quad
V_{\varepsilon,R_1}
\subset
V_{\varepsilon,R_2}.
\tag{S0.7}
\]

Definiere deshalb den **maximalen KNF-Samplingmajoranten**

\[
U_\varepsilon^{\max}
=
a+(-\varepsilon,\varepsilon)
\cup
b+(-\varepsilon,\varepsilon)
\cup
T+(-\varepsilon,\varepsilon)
\]

und

\[
V_\varepsilon^{\max}
=
\operatorname{Sat}_{\mathcal E_\varepsilon}
(U_\varepsilon^{\max}).
\]

Findet man ein messbares

\[
B_\varepsilon\subset(\varepsilon,T)
\]

mit positivem Maß, das von **keinem** Hub-Sourcewert aus
\(V_\varepsilon^{\max}\) getroffen wird, dann ist dasselbe
\(B_\varepsilon\) für **jedes**

\[
0<R<\varepsilon,
\qquad
0<\sigma<R
\]

blind.

Dies ist entscheidungsstärker als jede \(1-cR\)-Union-Bound-Schätzung.

---

## 7. Neuer exakter Kandidat aus dem ersten Phase-Diagramm-Scan

Setze

\[
h
:=
d-3\Delta.
\]

Die Konstantenidentitäten ergeben

\[
\boxed{
h
=
\frac{T-10\Delta}{4}
>0.
}
\tag{S0.8}
\]

Der direkte Saturationsscan des tatsächlichen A7-Graphings bei der
Majorantenwahl \(R=\varepsilon\) zeigt einen auffälligen exakten
Kandidaten:

\[
\boxed{
\varepsilon_c
:=
\frac h2
=
\frac{T-10\Delta}{8}
\approx
0.22123729809\,\Delta.
}
\tag{S0.9}
\]

Für

\[
0<\varepsilon<\varepsilon_c
\]

erscheinen vierzehn gleich breite blinde Intervalle mit Breite

\[
g_\varepsilon
=
h-2\varepsilon
=
\frac{T-10\Delta-8\varepsilon}{4}.
\tag{S0.10}
\]

Die beobachteten linken Grundpositionen sind

\[
\mathcal C=
\{
0,\Delta,2\Delta,3\Delta,
d,d+\Delta,d+2\Delta,
a,a+\Delta,a+2\Delta,a+3\Delta,
b,b+\Delta,b+2\Delta
\}.
\tag{S0.11}
\]

Der natürliche Kandidat ist daher

\[
B_\varepsilon^{\rm cand}
=
\bigcup_{c\in\mathcal C}
(c+\varepsilon,\ c+h-\varepsilon).
\tag{S0.12}
\]

Falls die FREE-Sättigungs-/Hub-Exklusion für S0.12 exakt bewiesen wird, folgt

\[
|B_\varepsilon^{\rm cand}|
=
14(h-2\varepsilon)
=
\boxed{
\frac72
(T-10\Delta-8\varepsilon)
}
>0,
\tag{S0.13}
\]

**unabhängig von \(R\)**.

Das wäre ein wesentlich stärkerer No-Go-Wedge als der bisherige
Small-\(R\)-Union-Bound.

### Status dieser Beobachtung

S0.8–S0.11 sind exakt identifizierte Konstanten-/Musterkandidaten.

Die entscheidende Inklusion

\[
B_\varepsilon^{\rm cand}
\cap
W^{\rm vis}(V_\varepsilon^{\max})
=
\varnothing
\tag{S0.14}
\]

ist **noch nicht bewiesen**.

Daher keine Promotion und noch keine Buchung als negativer Satz.

---

## 8. Nächste Gates

### SALVAGE-A1 — exact maximal-saturation cells

Für

\[
0<\varepsilon<\varepsilon_c
\]

die Sättigung von \(U_\varepsilon^{\max}\) unter allen neun A7-Maps
symbolisch als endliche Intervallzellen klassifizieren.

### SALVAGE-A2 — 14-gap exclusion

Für jede der sechs Hub-Source-Maps beweisen, dass ihre Bilder der
SALVAGE-A1-Sättigung S0.12 nicht treffen.

Erst dann darf gebucht werden:

\[
\beta(\varepsilon,R,\sigma)
\ge
\frac72(T-10\Delta-8\varepsilon)
\]

für den gesamten entsprechenden Wedge.

### SALVAGE-A3 — true coverage threshold

Nur außerhalb dieses Wedges die tatsächliche Nullstelle

\[
\beta(\varepsilon,R,\sigma)=0
\]

kartieren.

### SALVAGE-A4 — transversality

Nur auf \(\beta=0\) eine Coercivity-/Injektivitätsanalyse starten.

---

## 9. Firewall

- Die alte Schwelle \(T/28080\) ist nur ein grober hinreichender
  Blindheitsbound.
- \(M_N\le288N+144\) beweist keine uniforme Blindheit bei adaptivem \(N\).
- \(\beta=0\) beweist keine Injektivität.
- S0.9–S0.14 sind aktuell **Kandidaten**, keine Promotion.
- Keine separate Aussage über \(\ker\Gamma_I\), Objekt X oder RH.
