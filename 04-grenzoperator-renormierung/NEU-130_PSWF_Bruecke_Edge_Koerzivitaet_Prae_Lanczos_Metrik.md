# NEU-130 — PSWF-Brücke: Edge-Koerzivität als Modell für Prä-Lanczos-Metrik

> Stand: Juli 2026. Verbindet `prolate-gram-coercivity` (Papers I–XXII) mit dem Fragenkatalog
> über die gemeinsame Kontrollfrage der Rand-/Übergangsschicht-Koerzivität.
> **Kein Ersatz für NEU-129** (direkter Lanczos-Test), sondern analytische Methodenlieferung.

---

## Zentralthese

$$\boxed{\text{PSWF ist der analytische Modellfall für die Prä-Lanczos-Kontrollfrage.}}$$

Nicht: „PSWF beweist RH."  
Sondern präziser:

$$\boxed{\text{PSWF zeigt, wie eine kanonische Konzentrationsgeometrie eine gefährliche Rand-/Edge-Schicht stabilisieren kann.}}$$

Und genau das suchen wir bei Objekt XXX.

---

## 1. Parallele Kontrollfragen

Die RH-/Jacobi-Spur steht aktuell an:

> Gibt es eine intrinsische positive Prä-Lanczos-Metrik $W_N$?

$$b_{1,N}^{W} \asymp 1, \qquad \frac{b_{2,N}^{W}}{b_{1,N}^{W}} = O(1).$$

Die PSWF-Spur steht an:

$$\inf_{\|f\|=1,\, f \in \mathrm{Edge}} \langle (A_{N,c} - K_c)f, f\rangle > 0 \; ?$$

Das ist formal nicht dasselbe, aber **strukturell äquivalent** in folgender Hinsicht:

$$\boxed{\text{Kann eine Rand-/Übergangsschicht durch eine kanonische Operatorgeometrie koerziv gemacht werden?}}$$

| Programm | Kritische Zone | Operatorgeometrie |
|---|---|---|
| PSWF | Edge | Konzentrationsoperator $A_{N,c}$ + $K_c$ |
| Jacobi/RH | Erste zwei Lanczos-Stufen / Doppelbarriere | $H_{\mathrm{rel},N}$, $W_N$ |

---

## 2. Die tiefste Analogie: B-strong und Nelson/Schur

Der potentielle Transfer:

$$\text{B-strong} \quad\Longleftrightarrow\quad \text{Nelson-/Schur-Kontrolle}$$

Konkret:

$$P_{kl} \leq C^2 c^{1/2} \qquad \text{vs.} \qquad \sum_b |\Theta_{ba}|^2 \leq C^2 \ell(a)^2.$$

**Beides sind quadratische Energiekontrollen**, keine punktweisen Abschätzungen. Man zeigt
nicht, dass jedes einzelne Matrixelement brutal klein ist — sondern dass die *gesamte
Schichtenergie* kontrolliert bleibt.

Konsequenz für NEU-129:

$$\boxed{\text{Die Doppelbarriere darf nicht punktweise, sondern muss koerziv/energetisch gelesen werden.}}$$

---

## 3. PSWF als Modell für $\beta_0$-Fixierung

Warnung aus NEU-128B:

$$\beta = s \Rightarrow \Sigma_N(s) \text{ ist Weyl-Funktion, keine Metrik.}$$

Für $W_N$ brauchen wir $\beta = \beta_0 > 0$: fest, geometrisch, spektralparameter-unabhängig.

**PSWF-Paradigma:** Der Konzentrationsparameter $c$ ist nicht der Spektralparameter der
Resolvente — er ist ein **geometrischer Skalenparameter**. Deshalb:

$$c \;\text{(PSWF)} \quad \longleftrightarrow \quad \beta_0 \;\text{oder feste Normierungsskala von } W_N$$

$$\boxed{\text{PSWF liefert das Paradigma: Metrikparameter festhalten, Spektralparameter separat behandeln.}}$$

---

## 4. Drei Projektionen von Objekt XXX

Aus dem Brückenprotokoll (Juli 2026) sind $H_{\lim}$, $D_{\mathrm{Edge}}$, $D_{\mathrm{rel}} = \overline{iJ^-}$
möglicherweise drei Projektionen desselben hypothetischen Objekt XXX:

$$X \longrightarrow \begin{cases}
H_{\lim} & \text{PSWF-/SOT-Projektion,}\\
D_{\mathrm{Edge}} & \text{PSWF-Randkoerzivitäts-Projektion,}\\
D_{\mathrm{rel}} = \overline{iJ^-} & \text{relative Jacobi-/Primkanten-Projektion.}
\end{cases}$$

Die beiden Repos sind damit **nicht lose nebeneinander** — sie sind verschiedene Schatten
desselben Objekts.

---

## 5. Vorsicht: Kein dekorativer Import

Der saubere Transfer muss über eine gemeinsame **Abstraktionsform** laufen:

$$\text{Konzentrationsoperator} + \text{kommutierender/relativer Generator} + \text{Edge-Koerzivität} \Rightarrow \text{stabile Trunkierung.}$$

Dann fragt man: Hat $H_{\mathrm{rel},N}$ dieselbe abstrakte Struktur?

**Logische Kette:**

$$\text{PSWF} \Rightarrow \text{Modellaxiome für Prä-Lanczos-Koerzivität} \Rightarrow \text{Test an } H_{\mathrm{rel},N}.$$

---

## 6. Leitfragen für diesen Eintrag

1. Welche PSWF-Bedingung entspricht $W_N > 0$?
2. Welche PSWF-Bedingung entspricht $b_{1,N}^{W} \asymp 1$?
3. Welche PSWF-Bedingung entspricht $b_{2,N}^{W}/b_{1,N}^{W} = O(1)$?
4. Ist B-strong ($P_{kl} \leq C^2 c^{1/2}$) eine Instanz derselben Schur-/Nelson-Kontrolle wie NEU-54/55?
5. Gibt es ein abstraktes „Edge-Koerzivitäts-Lemma", das beide Programme umfasst?

---

## 7. Gesamturteil

Die PSWF-Reihen können wahrscheinlich nicht direkt die fehlende $W_N$-Konstruktion geben.
Aber sie geben etwas fast ebenso Wichtiges:

$$\boxed{\text{Sie können zeigen, welche Art von Schätzung überhaupt realistisch ist.}}$$

Das ist das entscheidende Gegengewicht zu den No-Go-Sätzen im Fragenkatalog.

$$\boxed{\text{Die PSWFs sind nicht das Dach über dem Projekt.}}$$

$$\boxed{\text{Sie sind ein bereits freigelegter Seitenflügel desselben Tempels.}}$$

Vielleicht erkennt man am Seitenflügel, wie die tragenden Bögen des Hauptbaus konstruiert
sein müssen.

---

## Verweise

- NEU-129: Direkter Lanczos-Test (wird durch diesen Eintrag **nicht** ersetzt)
- NEU-54/55: Nelson-/Schur-Kontrollbedingungen
- NEU-128B: Warnung $\beta = s$ (Weyl-Funktion, keine Metrik)
- NEU-125: Intrinsische Feshbach-Skala vor Lanczos
- `prolate-gram-coercivity`: Papers I–XXII, insb. B-strong-Lücke (Paper XXII)
- `ebene-XVI-objekt-x.md`: Dreiprojektion von Objekt XXX
