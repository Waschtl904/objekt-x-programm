# P11-O3a — Paritätsreduzierte Konditions-Firewall

**Datum:** 2026-08-11
**Knoten:** `[P11-O3a]`
**Vorgänger:** O3 (symmetrized Jensen contraction and conditioning firewall)
**Abhängigkeiten:** C2, C5 (§6–§14), C5d
**Modus:** `PASS-A ACTIVE`
**Scope:** Vier Resultate; kein O4, keine Residualroute, kein SYN, kein Seal.

---

## 0. Auditstatus

\[
\boxed{
\begin{aligned}
[P11\text{-}O3a]
&\quad \checkmark[M]_{\rm O3a.1\;full\text{-}space\;conditioning\;no\text{-}go}\\
&+\checkmark[M]_{\rm O3a.2\;exact\;parity\;reduction}\\
&+\checkmark[M]_{\rm O3a.3\;odd\;variational\;conditioning}\\
&+\checkmark[M]_{\rm O3a.4\;C4\text{-}lower\text{-}bounds\;insufficient\;for\;\kappa\to\infty}\\
&+?[O]_{\chi^{R,-}_{T,U}\;\rm bounded?}\\
&+?[O]_{\chi^{R,-}_{T,U}\to\infty?}\\
&+?[O]_{\chi^{R,-}_{T,U}\|\Theta^-_{T,U}\|\to0?}
\end{aligned}
}
\]

---

## 1. Vorgänger und Kontext

O3 hat auf dem vollen Raum $\mathcal{K}_{X,R}$ die Abschätzung

\[
\|Q - W_{T}\|^2 \leq 2\chi^R_{T,U}\|\Theta_{T,U}\|
\]

etabliert, wobei

\[
\chi^R_{T,U} = \kappa(A^R_{T,U})^{1/4},
\qquad
A^R_{T,U} = G_{R,T}^{-1/2}G_{R,U}G_{R,T}^{-1/2}.
\]

C7-CLOSE hat festgestellt: P11 Original-Transport-Readiness = FAIL, und der starke ungerade Terminallimes

\[
W_{R,S,-}^{[T]} \xrightarrow[T\to\infty]{\rm strong} W_{R,S,-}^{[\infty]}
\]

bleibt das offene Originalziel. Der Readiness-Audit bestätigt diesen Status.

O3a zielt darauf, die Konditions-Firewall von O3 **exakt auf den ungeraden Sektor zu reduzieren** und dabei den Vollraum-No-Go sauber zu isolieren.

---

## 2. O3a.1 — Full-Space Conditioning No-Go

### Satz O3a.1

*Für alle $R < T$ (fest) gilt:*

\[
\boxed{
\chi^R_{T,U} \longrightarrow +\infty \qquad (U \to \infty).
}
\tag{O3a.1}
\]

*Insbesondere: $\sup_{U > T} \chi^R_{T,U} = +\infty$, und es gibt keine uniforme Vollraum-Konditionsschranke.*

### Beweis

**Schritt 1 — Variationsidentität.**
Aus C2 (Metrik-Kokyklus, finite-horizon Terminal-Gauge) gilt für beliebiges $f \in \mathcal{K}_{X,R}$, $f \neq 0$, mit $x = G_{R,T}^{1/2}f$:

\[
\frac{\langle A^R_{T,U} x, x\rangle}{\|x\|^2_{X,R}}
= \frac{\langle G_{R,U} f, f\rangle_{X,R}}{\langle G_{R,T} f, f\rangle_{X,R}}.
\tag{O3a-var}
\]

Daher

\[
\|A^R_{T,U}\|
= \sup_{0 \neq f \in \mathcal{K}_{X,R}}
\frac{\langle G_{R,U} f, f\rangle}{\langle G_{R,T} f, f\rangle}.
\]

**Schritt 2 — Ungerade Richtung divergiert.**
Wähle $0 \neq f_- \in C^\infty_{c,\mathrm{odd}}((-R,R))$. Nach C5 (Satz C1zB2C5.1 + C1zB2C5.32): Es existiert

\[
m(f_-) := \min\{m \geq 0 : \beta_R^{(m)}(f_-) \neq 0\} < \infty,
\]

und

\[
\langle G_{R,U} f_-, f_- \rangle_{X,R}
= \sigma_U(J_{R,U}f_-)
\geq c_{f_-} \frac{e^U}{U^{2m(f_-)+3}}
\longrightarrow +\infty.
\]

Da $T$ fest ist, gilt $\langle G_{R,T} f_-, f_-\rangle_{X,R} < \infty$. Also

\[
\frac{\langle G_{R,U} f_-, f_- \rangle}{\langle G_{R,T} f_-, f_-\rangle}
\longrightarrow +\infty,
\]

woraus $\|A^R_{T,U}\| \to \infty$ folgt.

**Schritt 3 — Gerade Richtung bleibt beschränkt.**
Wähle $0 \neq f_+ \in C^\infty_{c,\mathrm{even}}((-R,R))$. Nach C5d: $\sigma_U(J_{R,U}f_+) = O_{R,f_+}(U^{-1}) \cdot e^U / e^U$ konvergiert gegen die endliche Gamma-Grenzform, d.h.

\[
\langle G_{R,U} f_+, f_+\rangle \longrightarrow q_{\Gamma,R}(f_+) < \infty.
\]

Daher

\[
\|(A^R_{T,U})^{-1}\|^{-1}
= \inf_{0\neq f} \frac{\langle G_{R,U}f,f\rangle}{\langle G_{R,T}f,f\rangle}
\leq \frac{\langle G_{R,U}f_+,f_+\rangle}{\langle G_{R,T}f_+,f_+\rangle}
\longrightarrow \frac{q_{\Gamma,R}(f_+)}{\langle G_{R,T}f_+,f_+\rangle} < \infty.
\]

**Schritt 4 — Konditionszahl.**
Damit gilt

\[
\kappa(A^R_{T,U})
= \|A^R_{T,U}\| \cdot \|(A^R_{T,U})^{-1}\|
\geq \|A^R_{T,U}\| \cdot c > 0
\longrightarrow +\infty,
\]

und somit $\chi^R_{T,U} = \kappa(A^R_{T,U})^{1/4} \to +\infty$. $\square$

### Firewall O3a.1-FW

\[
\boxed{
\forall T > R \text{ fest}: \sup_{U > T} \chi^R_{T,U} = +\infty.
}
\]

Dies widerlegt jede uniforme Vollraum-Konditionsschranke. Aus dieser Aussage wird **keine** gemeinsame $T, U \to \infty$-Asymptotik abgeleitet; die Aussage gilt für jedes feste $T$.

---

## 3. O3a.2 — Exakte Paritätsreduktion

### Satz O3a.2

*Alle O3-Identitäten restriktieren sich exakt auf den ungeraden Sektor $\mathcal{K}^-_{X,R}$.*

### Beweis

**Paritätszerlegung (C5 §6, C1zB2C5.14):**

\[
\mathcal{K}_{X,R} = \mathcal{K}^+_{X,R} \oplus^{\perp_X} \mathcal{K}^-_{X,R}.
\]

**Operatorintertwining (C5 §7–§8, C1zB2C5.17–C1zB2C5.20):**
Alle relevanten Operatoren kommutieren mit der Reflexion $\mathsf{P}_R$:

\[
[G_{R,T}, \mathsf{P}_R] = 0, \quad [G_{R,T}^{\pm 1/2}, \mathsf{P}_R] = 0,
\]
\[
J_{R,S}\mathsf{P}_R = \mathsf{P}_S J_{R,S}, \quad W^{[T]}_{R,S}\mathsf{P}_R = \mathsf{P}_S W^{[T]}_{R,S}.
\]

Daher zerfallen alle Operatoren in Paritätsblöcke:

\[
A^R_{T,U} = A^{R,+}_{T,U} \oplus A^{R,-}_{T,U},
\]
\[
W^{[T]}_{R,S} = W^{[T]}_{R,S,+} \oplus W^{[T]}_{R,S,-},
\]
\[
Q = Q_+ \oplus Q_-, \quad \Theta_{T,U} = \Theta^+_{T,U} \oplus \Theta^-_{T,U}.
\]

**Restriktierte O3-Abschätzung:**
Da die O3-Kontraktions-Firewall auf dem ungeraden Sektor eine eigenständige Isometrie-/Jensen-Struktur trägt, gilt exakt:

\[
\boxed{
\|Q_- - W_{T,-}\|^2 \leq 2\chi^{R,-}_{T,U} \|\Theta^-_{T,U}\|,
}
\tag{M-odd}
\]

wobei

\[
\chi^{R,-}_{T,U} := \kappa(A^{R,-}_{T,U})^{1/4},
\qquad
A^{R,-}_{T,U} := A^R_{T,U}\big|_{\mathcal{K}^-_{X,R}}. \quad \square
\]

### Firewall O3a.2-FW

Die Vollraumgröße $\chi^R_{T,U}$ ist nicht das relevante Objekt für das Klasse-O-Ziel. Die korrekte Konditions-Firewall ist $\chi^{R,-}_{T,U}$.

---

## 4. O3a.3 — Odd Variational Conditioning

### Definition

Setze für $f \in \mathcal{K}^-_{X,R}$, $f \neq 0$:

\[
\rho_{T,U}(f) := \frac{\langle G_{R,U} f, f\rangle_{X,R}}{\langle G_{R,T} f, f\rangle_{X,R}}.
\]

### Satz O3a.3

*Für alle $T < U$ und $R < T$ gilt:*

\[
\boxed{
\|A^{R,-}_{T,U}\| = \sup_{0 \neq f \in \mathcal{K}^-_{X,R}} \rho_{T,U}(f),
}
\tag{O3a.3-sup}
\]

\[
\boxed{
\|(A^{R,-}_{T,U})^{-1}\|^{-1} = \inf_{0 \neq f \in \mathcal{K}^-_{X,R}} \rho_{T,U}(f),
}
\tag{O3a.3-inf}
\]

und daher

\[
\boxed{
\kappa(A^{R,-}_{T,U})
= \frac{\sup_{f_- \neq 0}\, \rho_{T,U}(f_-)}{\inf_{f_- \neq 0}\, \rho_{T,U}(f_-)},
\qquad
\chi^{R,-}_{T,U} = \kappa(A^{R,-}_{T,U})^{1/4}.
}
\tag{O3a-core}
\]

### Beweis

Die Formeln (O3a.3-sup) und (O3a.3-inf) folgen direkt aus der spektralen Charakterisierung der Operatornorm und der Inversen-Norm auf einem separablen Hilbertraum, zusammen mit der quadratischen Formdarstellung

\[
\langle A^{R,-}_{T,U} x, x\rangle_{X,R}
= \rho_{T,U}(G_{R,T}^{-1/2}x)
\]

für $x = G_{R,T}^{1/2}f \in G_{R,T}^{1/2}(\mathcal{K}^-_{X,R})$.

Die Paritätsinvarianz aller Metrikoperatoren (O3a.2) garantiert, dass das Variationsproblem auf $\mathcal{K}^-_{X,R}$ verbleibt.

(O3a-core) ist dann die direkte Konsequenz aus (O3a.3-sup)/(O3a.3-inf) und der Definition der Konditionszahl. $\square$

### Interpretation

(O3a-core) reduziert die abstrakte Operatorfrage vollständig auf eine **konkrete Frage über relative Wachstumsraten ungerader Vektoren**: Wie unterschiedlich skalieren $\langle G_{R,U}f_-, f_-\rangle$ für verschiedene $f_-$, wenn $U \to \infty$?

---

## 5. O3a.4 — C4-Untergrenzen allein nicht hinreichend für $\kappa \to \infty$

### Satz O3a.4

*Aus der C4-Untergrenzenhierarchie*

\[
q^X_U(J_{R,U}f_-) \geq c_{f_-} \frac{e^U}{U^{2m(f_-)+3}}
\]

*allein folgt nicht $\kappa(A^{R,-}_{T,U}) \to \infty$.*

### Begründung

Die Untergrenze zeigt, dass $\rho_{T,U}(f_-)$ für jeden einzelnen $f_-$ divergiert. Für (O3a-core) ist aber der **Quotient von Supremum und Infimum** über alle ungeraden Richtungen entscheidend.

Konkret: Wenn alle ungeraden Richtungen dieselbe leading-order Skalierung $\sim e^U$ teilen — also

\[
\rho_{T,U}(f_-) \asymp \frac{e^U}{U^{2m(f_-)+3} \cdot \langle G_{R,T}f_-,f_-\rangle}
\]

mit demselben Exponenten für alle $f_-$ unabhängig von $m(f_-)$ — dann könnte

\[
\frac{\sup \rho_{T,U}}{\inf \rho_{T,U}} \longrightarrow C < \infty
\]

nicht ausgeschlossen werden. Ein Vektor mit $m=5$ könnte durch einen anderen, vom Konstantenmode-Zertifikat nicht erfassten Mechanismus mit derselben Größenordnung $e^U / U^3$ wachsen.

Für den Nachweis $\kappa(A^{R,-}_{T,U}) \to \infty$ wird daher mindestens eine der folgenden zusätzlichen Strukturen benötigt:

\[
\boxed{
\text{(a) obere Schranke: } q^X_U(J_{R,U}f_-) \lesssim C(f_-)\frac{e^U}{U^{2m(f_-)+3}},
}
\]

oder

\[
\boxed{
\text{(b) asymptotische Zwei-Seiten-Schärfe: } q^X_U(J_{R,U}f_-) \asymp C(f_-)\frac{e^U}{U^{2m(f_-)+3}},
}
\]

oder

\[
\boxed{
\text{(c) Gauge-Intertwining: } \mathscr{E}^{T,U}_{R,S}(C^{T\to U}_R)^{-1} \to 0 \text{ stark auf odd Core.}
}
\]

Falls (b) gilt, folgt sofort: Wähle $f_-$ mit $m(f_-)=0$ und $g_-$ mit $m(g_-)=1$. Dann

\[
\frac{\rho_{T,U}(f_-)}{\rho_{T,U}(g_-)}
\asymp \frac{U^5}{U^3} = U^2 \longrightarrow \infty,
\]

woraus $\kappa(A^{R,-}_{T,U}) \geq U^2 / C \to \infty$ und $\chi^{R,-}_{T,U} \to \infty$ folgen würde. $\square$

### Nächster Suchauftrag

\[
\boxed{
\text{Gibt es im committed Material C4–C5d bereits eine obere Boundary-Jet-Schranke?}
}
\]

Gesucht: ein Ausdruck $q^X_U(Jf) = \text{expliziter erster-Jet-Term} + \text{kontrollierter Rest}$, der (a) oder (b) liefert.

Falls ja: odd-sector conditioning No-Go beweisbar.
Falls nein: neuer Lemma-Knoten `sharp odd boundary-jet asymptotics` zu eröffnen.

---

## 6. Gesamtstatusmatrix

| Größe | Status | Quelle |
|---|---|---|
| $\chi^R_{T,U} \to \infty$ ($T$ fest, $U\to\infty$) | ✓ **[M]** No-Go | O3a.1, C5+C5d |
| Vollraum uniform beschränkt | ✗ **widerlegt** | O3a.1 |
| $A^R_{T,U} = A^{R,+} \oplus A^{R,-}$ | ✓ **[M]** | O3a.2, C5 §6–8 |
| (M-odd): $\|Q_- - W_{T,-}\|^2 \leq 2\chi^{R,-}_{T,U}\|\Theta^-_{T,U}\|$ | ✓ **[M]** | O3a.2 |
| Variationsformel (O3a-core) | ✓ **[M]** | O3a.3 |
| C4-Untergrenzen allein $\Rightarrow \kappa \to \infty$ | ✗ **nicht bewiesen** | O3a.4 |
| $\chi^{R,-}_{T,U}$ uniform beschränkt? | **?[O]** | offen |
| $\chi^{R,-}_{T,U} \to \infty$? | **?[O]** | offen, abhängig von upper bound |
| $\Theta^-_{T,U} \to 0$? | **?[O]** | offen |
| $\chi^{R,-}_{T,U}\|\Theta^-_{T,U}\| \to 0$? | **?[O]** | Klasse-O-Ziel |
| $W^{[T]}_{R,S,-}$ stark Cauchy? | **?[O]** | C7-CLOSE Originalziel |

---

## 7. Persistente Firewalls

### O3a-FW1 — Vollraum vs. odd Sektor

\[
\boxed{
\chi^R_{T,U} \to \infty
\not\Rightarrow
\chi^{R,-}_{T,U} \to \infty.
}
\]

Die Divergenz entsteht durch paritätsasymmetrische Skalierung (even: Gamma-Limes, odd: Boundary-Jet-Divergenz) und beweist nicht, dass alle odd Richtungen relativ verschieden skalieren.

### O3a-FW2 — C7C-FW8 (geerbt)

\[
\boxed{
\kappa(A^{R,-}_{T,U}) \to \infty
\not\Rightarrow
W^{[T]}_{R,S,-} \text{ konvergiert nicht stark.}
}
\]

Selbst ein odd-sector conditioning No-Go wäre noch nicht Nichtkonvergenz des relativ gewhiteten Terminal-Gauges.

### O3a-FW3 — Produktgröße ist das Ziel

Die logisch relevante Klasse-O-Größe ist das **Produkt**

\[
\chi^{R,-}_{T,U} \|\Theta^-_{T,U}\|,
\]

nicht jeder Faktor einzeln. Auch $\chi^{R,-} \to \infty$ (Ausgang C) wäre nur dann ein wirklicher schwerer Negativbefund, wenn zusätzlich gezeigt werden kann, dass das Produkt strukturell nicht gegen null gehen kann.

### O3a-FW4 — Asymptotik nur für festes T

Satz O3a.1 gilt verbindlich als

\[
\forall T > R \text{ fest}: \chi^R_{T,U} \xrightarrow{U\to\infty} +\infty.
\]

Daraus wird keine beliebige gemeinsame $T, U \to \infty$-Aussage abgeleitet.

---

## 8. Strategische Arbeitslinie

\[
\boxed{
\text{O3a}
\longrightarrow
\text{C4–C5d upper-bound audit}
\longrightarrow
\begin{cases}
\chi^{R,-}_{T,U} \to \infty \text{ beweisen (Ausgang B/C)}, \\
\text{oder: sharp-jet-Lemma eröffnen.}
\end{cases}
}
\]

Kein O4, keine Residualroute, kein SYN, kein Seal.

Der Übergabestatus **P11 PASS-A ACTIVE / SYN BLOCKED** bleibt unverändert.
