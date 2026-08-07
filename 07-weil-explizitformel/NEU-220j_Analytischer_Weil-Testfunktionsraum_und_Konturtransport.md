# NEU-220j — Analytischer Weil-Testfunktionsraum und Konturtransport

**Knoten:** `[O-220-1-PD5a1-contour-shift-Weil-distribution]`  
**Stand:** 26. Juli 2026  
**Vorgänger:** NEU-220i (✓[K/M] für $\sigma>1$), NEU-220h (Direktaudit)  
**Präzisierung:** Der Engpass liegt nicht bei $\sigma\searrow\tfrac12$ für festes
Schwartz-$h$, sondern beim Konturtransport eines festen holomorphen Weil-Kerns.

---

## 0. Was aus NEU-220i bestehen bleibt

$$
\boxed{\Lambda_{\mathrm{fin},\sigma}(h)
= \frac1{2\pi}\int_{\mathbb R}-\frac{\zeta'}{\zeta}(\sigma+it)\,h(t)\,dt
= \sum_{n\ge2}\Lambda(n)n^{-\sigma}\hat h_0(\log n)
\quad(\sigma>1)\quad\checkmark[K/M].}
$$

Dieser Ausdruck ist absolut konvergent, reellwertig auf geradem reellen $h$,
mit direkter Primzahlpotenzstruktur. Er ist die Basis für den Konturtransport.

**Warum $\sigma\searrow\tfrac12$ nicht genügt:** Für festes $h\in\mathcal S(\mathbb R)$
bleibt $h(t)$ auf der reellen Achse definiert. Das Ersetzen von $\sigma$ ändert
nur den Auswertungspunkt von $\zeta'/\zeta$, liefert aber keine zulässige
Konturverschiebung mit Residuensatz.

---

## 1. Aufbau des holomorphen Weil-Testkerns

### 1.1 Ausgangsdaten

Sei $g\in C_c^\infty(\mathbb R)$ reell und gerade. Definiere die gesamte Funktion:

$$
h(z) := \int_{\mathbb R} g(u)\,e^{izu}\,du.
$$

$h$ ist eine **ganze Funktion vom Paley-Wiener-Typ** (PW): holomorph auf $\mathbb C$,
und für $|\Im(z)|\le R$ (mit $\mathrm{supp}(g)\subset[-R,R]$) gilt
$|h(z)|\le C_N(1+|z|)^{-N}$ für alle $N\ge0$ (Abfall in Horizontalstreifen).

Aus der Geradheit von $g$ folgt $h(-z)=h(z)$, also $h$ gerade.

### 1.2 Holomorpher Weil-Testkern

$$
\boxed{F_h(s) := h\!\left(\frac{s-\tfrac12}{i}\right).}
$$

**Eigenschaften:**

| Eigenschaft | Beweis |
|---|---|
| $F_h(\tfrac12+it) = h(t)$ (kritische Linie) | Direktes Einsetzen |
| $F_h(1-s) = F_h(s)$ (Symmetrie) | $h(-z)=h(z)$ und $\frac{(1-s)-1/2}{i} = -\frac{s-1/2}{i}$ |
| $F_h$ ganz auf $\mathbb C$ | $h$ ganz, Komposition mit affiner Abbildung |
| Abfall in Vertikalstreifen | PW-Eigenschaft von $h$ |

Die Symmetrie $F_h(1-s)=F_h(s)$ baut die funktionale $s\leftrightarrow1-s$-Symmetrie
typkorrekt in den Testkern ein.

### 1.3 Testfunktionsraum

Definiere den **analytischen Weil-Testfunktionsraum:**

$$
\boxed{\mathcal{W} := \bigl\{F_h\mid g\in C_c^\infty(\mathbb R),\,g\text{ reell, gerade}\bigr\}.}
$$

$\mathcal{W}$ ist ein Untervektorraum von $\mathcal{O}(\mathbb C)\cap\mathcal{PW}$
(ganze PW-Funktionen mit Symmetrie $F(1-s)=F(s)$).

**Topologie auf $\mathcal{W}$ (autoritativ):** $\mathcal{W}$ trägt die von $C_{c,\mathrm{even}}^\infty(\mathbb{R})$ via $g \mapsto F_h$ transportierte LF-Topologie (induktiver Limes der Fréchet-Räume $C_{c,\mathrm{even}}^\infty([-R,R])$, $R\nearrow\infty$). Die Abbildung $g\mapsto F_h$ ist eine topologische Bijektion. Stetigkeit von $F_h\mapsto I_{\mathrm{fin},\sigma}(h)$ als Funktional auf $\mathcal{W}$ folgt unmittelbar aus der Stetigkeit der Fouriertransformation auf $C_c^\infty(\mathbb{R})$.

---

## 2. Konturkompatible endliche Form für $\sigma>1$

### 2.1 Definition

Für $F_h\in\mathcal{W}$ und $\sigma>1$ setze:

$$
\boxed{I_{\mathrm{fin},\sigma}(h) := \frac1{2\pi i}\int_{\Re(s)=\sigma}-\frac{\zeta'}{\zeta}(s)\,F_h(s)\,ds.}
$$

### 2.2 Beziehung zu $\Lambda_{\mathrm{fin},\sigma}$

Mit $s=\sigma+it$:

$$
I_{\mathrm{fin},\sigma}(h)
= \frac1{2\pi}\int_{\mathbb R}-\frac{\zeta'}{\zeta}(\sigma+it)\,F_h(\sigma+it)\,dt
= \frac1{2\pi}\int_{\mathbb R}-\frac{\zeta'}{\zeta}(\sigma+it)\,h\!\left(t-i(\sigma-\tfrac12)\right)dt.
$$

Der Unterschied zu $\Lambda_{\mathrm{fin},\sigma}$:

$$
\Lambda_{\mathrm{fin},\sigma}(h): \quad h(t) \qquad
I_{\mathrm{fin},\sigma}(h): \quad h\!\left(t-i(\sigma-\tfrac12)\right).
$$

Nur $I_{\mathrm{fin},\sigma}$ stammt von einem festen holomorphen Kern $F_h$.

### 2.3 Das Weil-Gewicht entsteht automatisch

Einsetzen von $-\zeta'/\zeta(s) = \sum_{n\ge2}\Lambda(n)n^{-s}$ (absolut konvergent für $\sigma>1$):

$$
I_{\mathrm{fin},\sigma}(h)
= \sum_{n\ge2}\Lambda(n)n^{-\sigma}\cdot
\frac1{2\pi}\int_{\mathbb R}h\!\left(t-i(\sigma-\tfrac12)\right)e^{-it\log n}\,dt.
$$

Konturruckverschiebung um $i(\sigma-\tfrac12)$ (PW-Abfall rechtfertigt dies):

$$
\frac1{2\pi}\int_{\mathbb R}h\!\left(t-i(\sigma-\tfrac12)\right)e^{-it\log n}\,dt
= e^{(\sigma-\frac12)\log n}\cdot\frac1{2\pi}\int_{\mathbb R}h(t)e^{-it\log n}\,dt
= n^{\sigma-\frac12}\,\hat h_0(\log n).
$$

Damit:

$$
n^{-\sigma}\cdot n^{\sigma-\frac12} = n^{-1/2},
$$

und:

$$
\boxed{I_{\mathrm{fin},\sigma}(h) = \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,g(\log n).}
$$

**Das Ergebnis ist $\sigma$-unabhängig.** Genau das ist das Weil-Gewicht $\Lambda(n)/\sqrt n$.
Der holomorphe Testkern $F_h$ stellt sicher, dass der Konturtransport
kein $\sigma$-Rest hinterlässt.

$$
\boxed{I_{\mathrm{fin},\sigma}(h) = I_{\mathrm{fin},\sigma'}(h)\quad\text{für alle }\sigma,\sigma'>1
\quad\checkmark[M].}
$$

---

## 3. Residuenformel: Buchhaltungsentscheidung

### 3.1 Zwei Buchhaltungen

**Variante A — Endliche Buchhaltung mit $\zeta'/\zeta$:**

Verschiebe die Kontur von $\Re(s)=\sigma>1$ nach $\Re(s)=\sigma'<0$.
Residuensatz liefert Beiträge von:

| Singularität von $-\zeta'/\zeta$ | Residuum | $F_h$-Auswertung |
|---|---|---|
| Pol $s=1$ | $+1$ | $F_h(1) = h(-i/2)$ |
| Nichttriviale Nullstelle $\rho=\beta+i\gamma$ (Vielfachheit $m_\rho$) | $-m_\rho$ | $F_h(\rho)=h\bigl(\gamma-i(\beta-\tfrac12)\bigr)$ |
| Triviale Nullstelle $s=-2k$ | $-1$ | $F_h(-2k)=h\bigl(i(2k+\tfrac12)\bigr)$ |

**Variante B — Abgeschlossene Buchhaltung mit $\xi'/\xi$:**

Zerlege:
$$
-\frac{\xi'}{\xi}(s) = -\frac1s - \frac1{s-1} - \frac{\Gamma_{\mathbb R}'}{\Gamma_{\mathbb R}}(s) - \frac{\zeta'}{\zeta}(s).
$$

Dann hat $-\xi'/\xi$ nur Pole bei den nichttrivialen Nullstellen $\rho$ (mit Residuum $-m_\rho$),
die Gamma- und Polterme reorganisieren die trivialen Nullstellen.

### 3.2 Buchhaltungswahl für NEU-220

Da NEU-220d–f bereits $\Lambda_\Gamma$ (archimedischer Gammaterm) separat konstruiert haben,
muss Doppelzählung vermieden werden. Die sauberste Variante:

$$
\boxed{\text{Variante B (}\xi'/\xi\text{) mit anschließender typisierter Zerlegung.}}
$$

**Typisierte Zerlegung:**

$$
-\frac{\xi'}{\xi}(s)F_h(s)\,\longrightarrow\,
\underbrace{\Lambda_\mathrm{zeros}(F_h)}_{\text{nichttriviale Nullst.}}
+\underbrace{\Lambda_\mathrm{fin}(F_h)}_{\text{Primzahlpotenz}}
+\underbrace{\Lambda_\Gamma(h)}_{\text{archimedisch, PD-4c3}}
+\underbrace{\Lambda_\mathrm{pole}(F_h)}_{\text{Pol bei }s=0,1}.
$$

Dabei entspricht $\Lambda_\mathrm{fin}(F_h) = I_{\mathrm{fin},\sigma}(h)$ dem $\sigma$-unabhängigen
Primzahlpotenzterm aus §2.

### 3.3 Nullstellenauswertung ohne RH-Annahme

Für eine allgemeine nichttriviale Nullstelle $\rho=\beta+i\gamma$ (ohne RH-Annahme):

$$
\boxed{F_h(\rho) = h\!\left(\gamma - i\!\left(\beta-\tfrac12\right)\right).}
$$

Einschränkungen:
- Nur unter RH ($\beta=\tfrac12$) reduziert sich dies zu $F_h(\rho) = h(\gamma)\in\mathbb R$.
- Allgemein ist $F_h(\rho)\in\mathbb C$ (da $h$ ganz, aber nicht notwendig reellwertig
  außerhalb der reellen Achse).

Die Nullstellensumme muss in der Form $\sum_\rho m_\rho F_h(\rho)$ geführt werden,
nicht als $\sum_\rho m_\rho h(\gamma_\rho)$.

**Konsequenz für die Pole bei $s=0$ und $s=1$:**

$$
F_h(1) = h(-i/2), \qquad F_h(0) = h(i/2).
$$

In der symmetrisierten Form ($s=0$ und $s=1$ zusammen):

$$
F_h(0)+F_h(1) = h(i/2)+h(-i/2).
$$

Das ist nicht $\hat h_0(0)$ (wie in NEU-220i heuristisch angegeben),
sondern eine Auswertung des holomorphen $h$ an imaginären Punkten.

---

## 4. Offener Knoten: Konvergenz der globalen Residuensumme

Nach Buchhaltungsentscheidung (Variante B) und Konturtransport ist die
verbleibende Frage:

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-contour-shift-Weil-distribution}]\quad?[O].}
$$

**Präzise Aufgabe:**

1. Zeige, dass $\sum_\rho m_\rho F_h(\rho)$ absolut konvergiert für $F_h\in\mathcal{W}$
   (Abschätzung über PW-Abfall und Nullstellendichte $N(T)\sim\frac{T}{2\pi}\log T$).
2. Rechtfertige die Konturverschiebung von $\Re(s)=\sigma>1$ nach $\Re(s)\to-\infty$
   (Abschätzung von $\int F_h(s)\xi'/\xi(s)$ auf Horizontalstrecken).
3. Identifiziere $\Lambda_\mathrm{fin}(F_h) = I_{\mathrm{fin},\sigma}(h)$ aus §2
   als den Primzahlpotenzterm der expliziten Formel.
4. Schließe den Teilknoten `[O-220-1-PD5a1-logderivative-trace]` durch
   die typisierte Kette:

$$
\mathcal{W}\ni F_h\longmapsto I_{\mathrm{fin},\sigma}(h) = \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n)\in\mathbb R.
$$

---

## 5. Atomare Zielkette

$$
\boxed{
g\in C_c^\infty(\mathbb R)
\longrightarrow h\in\mathcal{PW}(\mathbb C)
\longrightarrow F_h(s)=h\!\left(\tfrac{s-1/2}{i}\right)
\longrightarrow I_{\mathrm{fin},\sigma}(h)
\longrightarrow \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n).
}
$$

Status: Alle Schritte bis zum letzten ✓[M]; Konvergenz der globalen
Residuensumme und Konturverschiebungsjustifikation ?[O].

---

## 6. DAG-Update nach NEU-220j

```
PD-5a1  checkmark[M]_part
  |-- PD-5a1a--d  checkmark[M]_part  (aus NEU-220h)
  |-- [Sfin-ratio-v0]           checkmark[M]_neg  (NEU-220i)
  |-- [Sfin-RH-obstruction-v0] checkmark[M]_neg  (NEU-220i)
  |-- Lambda_{fin,sigma} sigma>1  checkmark[K/M]  (NEU-220i/j)
  |-- Weil-Testkern F_h, W-Raum  checkmark[M]     (NEU-220j Abschnitt 1)
  |-- Topologie auf W: LF-Transport von C_{c,even}^infty(R)  checkmark[M]  (NEU-220j Abschnitt 1.3)
  |-- I_{fin,sigma} sigma-unabh.  checkmark[M]     (NEU-220j Abschnitt 2)
  |-- Buchhaltungsentscheidung   checkmark[M]     (NEU-220j: Variante B, xi'/xi)
  |-- F_h(rho) ohne RH           checkmark[M]     (NEU-220j Abschnitt 3)
  `-- [contour-shift-Weil-distribution]  ?[O]     (Konvergenz + Konturverschiebung)
       Aufgabe: abs. Konvergenz Summe_rho m_rho F_h(rho),
                Horizontalabschaetzung, Identifikation Lambda_fin
```

---

*Datei: `katalog/NEU-220j_Analytischer_Weil-Testfunktionsraum_und_Konturtransport.md` | 26. Juli 2026 (Topologie-Patch: 07. August 2026)*  
*Kernresultat: $\mathcal{W}$-Raum konstruiert; Topologie: LF-Transport von $C_{c,\mathrm{even}}^\infty(\mathbb{R})$ \checkmark[M]; $I_{\mathrm{fin},\sigma}$ $\sigma$-unabhängig \checkmark[M]; Buchhaltung Variante B gewählt; $F_h(\rho)$ ohne RH-Annahme; Engpass präzisiert*  
*Quellen: NEU-220i (§1–2), NEU-220d–f ($\Lambda_\Gamma$)*
