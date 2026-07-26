# NEU-220i — Direktaudit: Zeta-Quotient und endlicher Logableitungsport

**Knoten:** Direktaudit zu NEU-220h  
**Stand:** 26. Juli 2026  
**Zweck:** Vier Fehler in NEU-220h §5.2–5.3 korrigieren; neue Knoten setzen.

**Geschlossene Negativknoten (NEU-220h):**
- `[O-220-1-PD5a1-Sfin-ratio-v0]` → ✓[M]_neg
- `[O-220-1-PD5a1-Sfin-RH-obstruction-v0]` → ✓[M]_neg

**Zentraler Knoten bleibt offen:**
- `[O-220-1-PD5a1-logderivative-trace]` ?[O]

**Neuer Engpassknoten:**
- `[O-220-1-PD5a1-contour-shift-Weil-distribution]` ?[O]

---

## 1. Korrektur: $S_\zeta = S_\infty^{-1}$ (Fehler 1 und 2 in NEU-220h)

### 1.1 Definition des Quotienten

Setze $s = \tfrac12+it$ und definiere:

$$
S_\zeta(t) := \frac{\zeta(\tfrac12-it)}{\zeta(\tfrac12+it)} = \frac{\zeta(1-s)}{\zeta(s)}.
$$

### 1.2 Beweis $S_\zeta(t) = S_\infty(t)^{-1}$

Die Funktionalgleichung der vervollständigten Zetafunktion
$\xi(s) = \xi(1-s)$ mit
$\xi(s) = \tfrac12 s(s-1)\Gamma_{\mathbb R}(s)\zeta(s)$
liefert:

$$
\Gamma_{\mathbb R}(s)\zeta(s) = \Gamma_{\mathbb R}(1-s)\zeta(1-s),
$$

also

$$
\frac{\zeta(1-s)}{\zeta(s)} = \frac{\Gamma_{\mathbb R}(s)}{\Gamma_{\mathbb R}(1-s)}.
$$

Nach NEU-220f ist $S_\infty(t) = \Gamma_{\mathbb R}(1-s)/\Gamma_{\mathbb R}(s)$, also:

$$
\boxed{S_\zeta(t) = \frac{\Gamma_{\mathbb R}(s)}{\Gamma_{\mathbb R}(1-s)} = S_\infty(t)^{-1}.}
$$

**Konsequenz:** $S_\zeta$ ist kein unabhängiger endlicher Streufaktor. Er trägt keine neue Primzahl- oder Eulerinformation; er ist identisch mit dem Inversen des bereits konstruierten archimedischen Streufaktors.

### 1.3 Verhalten an Nullstellen von $\zeta$ auf der kritischen Linie

An einer Nullstelle $t_0$ mit $\zeta(\tfrac12+it_0)=0$ ist $S_\zeta(t_0)$ im
Zähler/Nenner-Sinne formal $0/0$. Die Funktionalgleichung liefert die
kanonische Fortsetzung:

$$
S_\zeta(t) = \frac{\Gamma_{\mathbb R}(s)}{\Gamma_{\mathbb R}(1-s)},
$$

die auf der gesamten reellen $t$-Achse glatt und unimodular ist
($\Gamma_{\mathbb R}$ hat auf $\{\Re(s)=\tfrac12\}$ weder Nullstellen noch Pole).

Die Nullstellen von $\zeta$ erzeugen daher keine nichtentfernbaren Singularitäten.
Sie heben sich im reflektierten Quotienten gerade heraus — was erklärt, warum
dieser Quotient die Nullstelleninformation verliert.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-Sfin-ratio-v0}]\quad\checkmark[M]_\mathrm{neg}.}
$$

---

## 2. Korrektur: RH-Aussage war umgekehrt (Fehler 1 in NEU-220h)

Die in NEU-220h §5.2 formulierte Behauptung, $S_\mathrm{fin}$ sei unitär und
singularitätenfrei *genau dann, wenn $\zeta$ keine Nullstellen auf der kritischen
Linie hätte*, war in doppelter Hinsicht falsch:

1. **Richtung:** Die Riemannsche Vermutung behauptet, dass *alle* nichttrivialen
   Nullstellen auf $\Re s=\tfrac12$ liegen, nicht dass dort keine liegen.
2. **Relevanz:** Da $S_\zeta = S_\infty^{-1}$ über die Gammafunktion ausgedrückt
   wird, enthält der Quotient die Nullstellen von $\zeta$ gar nicht explizit;
   sie heben sich heraus.

Die vermeintliche RH-Verknüpfung über diesen Quotienten ist damit geschlossen:

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-Sfin-RH-obstruction-v0}]\quad\checkmark[M]_\mathrm{neg}.}
$$

---

## 3. Korrektur: Logarithmische Ableitung enthält Realteil (Fehler 3 in NEU-220h)

NEU-220h §5.2 schrieb fälschlicherweise $-2i\,\mathrm{Im}(\zeta'/\zeta)$.
Die korrekte Rechnung:

Setze $A(t) = (\zeta'/\zeta)(\tfrac12+it)$. Wegen
$\zeta'(\tfrac12-it)/\zeta(\tfrac12-it) = \overline{A(t)}$ gilt:

$$
\frac{d}{dt}\log S_\zeta(t)
= -i\frac{\zeta'}{\zeta}\!\left(\tfrac12-it\right)
-i\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right)
= -i\overline{A(t)} - iA(t)
= -2i\,\mathrm{Re}\,A(t).
$$

Also:

$$
\boxed{\frac{d}{dt}\log S_\zeta(t) = -2i\,\mathrm{Re}\,\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right).}
$$

Der Zeitverzögerungsoperator:

$$
\boxed{iS_\zeta(t)^*S_\zeta'(t) = 2\,\mathrm{Re}\,\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right).}
$$

Da $S_\zeta = S_\infty^{-1}$ und nach NEU-220f $iS_\infty^* S_\infty' = \gamma_\infty^\mathrm{sym}$,
folgt:

$$
\boxed{iS_\zeta^*S_\zeta' = -\gamma_\infty^\mathrm{sym}.}
$$

Der Quotient reproduziert also lediglich den **negativen** archimedischen
Zeitverzögerungsterm. Keine neue Information.

---

## 4. Korrektur: Ableitung vs. logarithmische Ableitung (Fehler 4 in NEU-220h)

Für $\lambda_\mathrm{mod}(s) = C_L/\zeta(s)$ gilt:

$$
-\partial_s\!\left(\frac{C_L}{\zeta(s)}\right)
= C_L\frac{\zeta'(s)}{\zeta(s)^2}.
$$

Das ist **nicht** $\zeta'/\zeta$, sondern $\zeta'/\zeta^2$.

Die korrekte Beziehung über die **logarithmische Ableitung** lautet:

$$
\partial_s\log\lambda_\mathrm{mod}(s)
= \partial_s\bigl(\log C_L - \log\zeta(s)\bigr)
= -\frac{\zeta'(s)}{\zeta(s)}.
$$

Also:

$$
\boxed{\gamma_\mathrm{fin}(s) := -\frac{\zeta'}{\zeta}(s) = \partial_s\log\lambda_\mathrm{mod}(s).}
$$

Der Weg von $\lambda_\mathrm{mod}$ zu $\gamma_\mathrm{fin}$ führt über die logarithmische
Ableitung, nicht über die gewöhnliche Ableitung. Dieser Unterschied ist typkritisch:
$\zeta'/\zeta^2$ hat Doppelpole bei den Nullstellen, während $\zeta'/\zeta$ nur
einfache Pole hat.

---

## 5. Konstruktion von $\Lambda_{\mathrm{fin},\sigma}$ für $\sigma>1$

### 5.1 Absolut konvergente Primzahlpotenzform

Für $\Re(s) = \sigma > 1$ gilt absolut konvergent (aus dem Eulerprodukt von $\zeta$):

$$
\boxed{-\frac{\zeta'}{\zeta}(\sigma+it) = \sum_{n\ge2}\frac{\Lambda(n)}{n^\sigma}e^{-it\log n}}
$$

mit der von-Mangoldt-Funktion $\Lambda(n) = \log p$ falls $n=p^k$, sonst $0$.

### 5.2 Typisiertes Weil-Funktional für $\sigma>1$

Für $h\in\mathcal S(\mathbb R)$ und $\sigma>1$ definiere:

$$
\boxed{\Lambda_{\mathrm{fin},\sigma}(h) := \frac1{2\pi}\int_{\mathbb R}-\frac{\zeta'}{\zeta}(\sigma+it)\,h(t)\,dt.}
$$

Durch Vertauschen von Summe und Integral (gerechtfertigt durch absolute
Konvergenz für $\sigma>1$ und $h\in\mathcal S$):

$$
\Lambda_{\mathrm{fin},\sigma}(h)
= \sum_{n\ge2}\Lambda(n)\,n^{-\sigma}
\cdot\underbrace{\frac1{2\pi}\int_{\mathbb R}h(t)\,e^{-it\log n}\,dt}_{=:\hat h_0(\log n)},
$$

wobei $\hat h_0(u) = \frac1{2\pi}\int_\mathbb R h(t)e^{-itu}\,dt$ die gewöhnliche
Fouriertransformierte ist.

Damit ist $\Lambda_{\mathrm{fin},\sigma}$ für $\sigma>1$ ein vollständig typisiertes,
**absolut konvergentes** Distribution-artiges Funktional auf $\mathcal S(\mathbb R)$,
mit direkter Primzahlpotenzstruktur.

**Status:** $\Lambda_{\mathrm{fin},\sigma}$ für $\sigma>1$ ✓[M]. Dieser Ausdruck
ist die konvergente Basis für den nächsten Schritt.

### 5.3 Realität für gerades reelles $h$

Für reelles gerades $h$: Da $\Lambda(n)\in\mathbb R$ und
$n^{-\sigma}\in\mathbb R$ und $\hat h_0(\log n)\in\mathbb R$ (wegen
Geradheit von $h$), gilt:

$$
\Lambda_{\mathrm{fin},\sigma}(h) \in \mathbb R
\quad\text{für reelles gerades }h\text{ und }\sigma>1.
$$

Das Erfolgskriterium PD-5a1d ist für $\sigma>1$ erfüllt.

---

## 6. Der neue Engpassknoten: Konturverschiebung

### 6.1 Das Problem

Der physikalisch und zahlentheoretisch relevante Wert ist $\sigma=\tfrac12$.
Der Grenzübergang

$$
\sigma > 1 \longrightarrow \sigma = \tfrac12
$$

ist nicht einfach eine stetige Grenzwertbildung: $-\zeta'/\zeta(\tfrac12+it)$
hat Pole an den Nullstellen $\rho = \tfrac12+i\gamma$ von $\zeta$.

### 6.2 Was bei der Konturverschiebung entsteht

Bei der Verschiebung $\sigma\searrow\tfrac12$ entstehen (aus der expliziten
Formel) Residuen an:

| Singularität | Beitrag |
|---|---|
| Pol von $\zeta$ bei $s=1$ | $\hat h_0(0) = \frac1{2\pi}\int_\mathbb R h(t)\,dt$ |
| Nichttriviale Nullstellen $\rho=\tfrac12+i\gamma$ | $\hat h_0(\pm\gamma)$ (Residuenterm) |
| Triviale Nullstellen $s=-2k$ | $\hat h_0(\cdot)$ mit log. Korrekturen |
| Hauptwertteil auf $\Re(s)=\tfrac12$ | distributionelle Fortsetzung |

Das ist der Weil-Explizitformelmechanismus. Der Knoten ist:

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-contour-shift-Weil-distribution}]\quad?[O].}
$$

**Präzise Aufgabe dieses Knotens:**

1. Zeige, dass $\sigma\mapsto\Lambda_{\mathrm{fin},\sigma}(h)$ eine meromorphe
   Fortsetzung in $\sigma$ besitzt.
2. Identifiziere die Residuen bei $\sigma\to\tfrac12$ als Weil-Terme
   (Pol bei $s=1$, Nullstellensumme, Gamma-Korrekturen).
3. Definiere $\Lambda_\mathrm{fin}(h)$ als regulierten Grenzwert (Hauptwert
   oder Hadamard-Regularisierung):

$$
\Lambda_\mathrm{fin}(h) := \mathrm{r.v.}\lim_{\sigma\to 1/2}\Lambda_{\mathrm{fin},\sigma}(h)
$$

   mit explizit ausgeschriebenen Subtraktionstermen.
4. Prüfe Normalierungskompatibilität mit $\Lambda_\Gamma$ (Faktor $1/(2\pi)$).

### 6.3 Warum dies der richtige Engpass ist

Der Zeta-Quotient $S_\zeta = S_\infty^{-1}$ verlor die Nullstelleninformation,
weil er die Pole von $\zeta'/\zeta$ auf der kritischen Linie zum Verschwinden
brachte. Die Konturverschiebung hingegen *kontrolliert* genau diese Pole und
erhält sie als Residuen. Das ist der Mechanismus, durch den die Nullstellen
in die Weil-Formel eingehen.

---

## 7. Revidierter Status $X_\mathrm{fin}$-Schablone

Nach dem Direktaudit ist die korrekte Schablone:

$$
\boxed{
X_\mathrm{fin} = \bigl(L^2(\mathbb R,dt),\,\mathcal N_\mathrm{fin}=L^\infty(\mathbb R),\,
\tau_\mathrm{fin},\,M_{\gamma_{\mathrm{fin},\sigma}},\,\Lambda_{\mathrm{fin},\sigma}\bigr)
\quad(\sigma>1,\text{ konvergent})
}
$$

mit dem Knotenziel:

$$
\Lambda_{\mathrm{fin},\sigma}\xrightarrow{[\text{PD5a1-contour-shift}]}\Lambda_\mathrm{fin}\quad(\sigma\to\tfrac12).
$$

**Was gesichert ist:** Die Abbildungskette

$$
\mathcal S(\mathbb R)\xrightarrow{h\mapsto\Lambda_{\mathrm{fin},\sigma}(h)}\mathbb R
\quad(\sigma>1)
$$

mit expliziter Primzahlpotenzstruktur ✓[M].

**Was offen bleibt:**

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-contour-shift-Weil-distribution}]\quad?[O].}
$$

---

## 8. Zusammenfassung der Korrekturen und Statusabschluss

| Aussage aus NEU-220h §5.2–5.3 | Korrigierter Status |
|---|---|
| $S_\mathrm{fin}^{(0)} = \zeta(\tfrac12-it)/\zeta(\tfrac12+it)$ ist unabhängiger endlicher Streufaktor | ✓[M]_neg: $S_\zeta = S_\infty^{-1}$ |
| $S_\mathrm{fin}$ unitär $\Leftrightarrow$ $\zeta$ keine Nullstellen auf krit. Linie | ✓[M]_neg: RH-Aussage umgekehrt + Zusammenhang fehlt |
| $\frac{d}{dt}\log S_\zeta = -2i\,\mathrm{Im}(\zeta'/\zeta)$ | ✓[M]_neg: korrekt ist $-2i\,\mathrm{Re}(\zeta'/\zeta)$ |
| $-\partial_s(C_L/\zeta) = C_L\zeta'/\zeta$ | ✓[M]_neg: korrekt $C_L\zeta'/\zeta^2$; Weg zu $\zeta'/\zeta$ via $\partial_s\log\lambda_\mathrm{mod}$ |
| $\Lambda_\mathrm{fin}$ direkt auf $\Re(s)=\tfrac12$ typisiert | ✓[M]_part: $\Lambda_{\mathrm{fin},\sigma}$ für $\sigma>1$ ✓[M]; Konturverschiebung ?[O] |

### Offene Knoten nach NEU-220i

$$
[O\text{-}220\text{-}1\text{-PD5a1-logderivative-trace}]\quad?[O]
\quad\text{(Typisierung }M_{\gamma_\mathrm{fin}}\text{ semifinit)}
$$

$$
[O\text{-}220\text{-}1\text{-PD5a1-contour-shift-Weil-distribution}]\quad?[O]
\quad\text{(Weil-Mechanismus: }\sigma>1\to\tfrac12\text{)}
$$

Beide Knoten sind **nicht durch RH blockiert**, sondern durch
Distributionstheorie und analytische Fortsetzung.

---

*Datei: `katalog/NEU-220i_Direktaudit_Zeta-Quotient_und_Endlicher_Logableitungsport.md` | 26. Juli 2026*  
*Kernresultat: $S_\zeta=S_\infty^{-1}$ bewiesen; vier Fehler in NEU-220h korrigiert; $\Lambda_{\mathrm{fin},\sigma}$ für $\sigma>1$ konstruiert; Engpassknoten [contour-shift-Weil-distribution] geöffnet*
