# NEU-250 — Typaudit $[O\text{-}220\text{-}1f_0]$: Mindestarchitektur einer globalen Archimedes–Prim-Kopplung

**Stand:** 2026-08-05  
**Repository:** Waschtl904/objekt-x-programm  
**Vorgänger:** NEU-220c ($\checkmark[M]_{\mathrm{neg}}$, Commit 529e8b8)  
**Bezug:** OBJEKT-X-BESTANDSAUFNAHME.md, S12 / $[O\text{-}220\text{-}1f_0]$ (Commit 4194666)

---

## 1. Ausgangslage

Verbindlich bewiesen (NEU-220c):
$$
Q_\infty(f,h)=\frac{1}{2\pi}\int_{\mathbb R}\overline{\hat h(t)}\,\hat f(t)\,A_\infty(t)\,dt,
\qquad
A_\infty(t)=\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{it}{2}\right)-\log\pi.
$$
Mit $t_\infty=6.2898359888369027\ldots$: $A_\infty(t)<0\iff|t|<t_\infty$, und
$$\operatorname{ind}_-(Q_\infty)=\operatorname{ind}_+(Q_\infty)=\infty.$$
Weder Polterm noch endlich-rangige hermitesche Korrektur beseitigt den negativen Index. Daraus folgt S12 (Bestandsaufnahme) und der Knoten $[O\text{-}220\text{-}1f_0]$.

Dieser Typaudit klärt, was eine globale Kopplung mathematisch bedeuten kann, und schließt zwei naheliegende Fehldeutungen aus.

---

## 2. Gesamturteil

$$\boxed{[O\text{-}220\text{-}1f_0]\quad\checkmark[M]_{\mathrm{part}}}$$

Der Kopplungsknoten ist **typisiert, aber nicht konstruktiv gelöst**. Zwei naheliegende Deutungen sind negativ geschlossen:

1. Eine positive Blockform auf dem vollständigen direkten Summenraum mit festem Hauptdiagonalblock $A_\infty$ ist unmöglich.
2. Ein zusätzlicher hermitescher Kreuzterm kann nicht einfach zur bereits exakt festgelegten expliziten Formel addiert werden, ohne deren Wert zu verändern.

Die zulässige Architektur ist eine positive bzw. defektkontrollierte Form auf dem **kanonischen gemeinsamen Quellenbild** der archimedischen und primarithmetischen Daten — keine beliebige positive Blockmatrix.

---

## 3. Erstes No-Go: positive Vollblockmatrix unmöglich

Für hermitesche Blockform $\mathfrak q$ auf $H_\infty\oplus H_{\mathrm{pr}}$ mit $\mathfrak q\ge0$ auf dem Gesamtraum folgt für $x\in H_\infty$ (mit $y=0$): $\mathfrak q\big((x,0),(x,0)\big)=\langle x,A_\infty x\rangle\ge0$, also $A_\infty\ge0$. Widerspruch zu $\operatorname{ind}_-(A_\infty)=\infty$.

$$
\boxed{\begin{pmatrix}A_\infty & B_{\infty,\mathrm{pr}}\\ B_{\infty,\mathrm{pr}}^* & A_{\mathrm{pr}}\end{pmatrix}\ngeq0}
$$
auf dem vollständigen direkten Summenraum, **unabhängig von $B_{\infty,\mathrm{pr}}$**.

$$\boxed{[O\text{-}220\text{-}1f_0\text{-full-block}]\quad\checkmark[M]_{\mathrm{neg}}}$$

**Konsequenz:** Die Arbeitsnormalform darf nicht als positiver Operator auf einem freien direkten Summenraum interpretiert werden. Sinnvoll nur: auf einem echten Unterraum, auf einem Graphen, auf dem Abschluss eines gemeinsamen Quellenbildes, oder als symbolische Darstellung einer nichtorthogonalen Faktorisierung.

---

## 4. Zweites No-Go: kein zusätzlicher Kreuzterm ohne Umverteilung

Die explizite Formel legt bereits $Q_W=Q_{\mathrm{pole}}+Q_\infty+Q_{\mathrm{prime}}$ exakt fest. Ein zusätzlicher hermitescher Kreuzterm $Q_{\infty,\mathrm{pr}}^{\mathrm{cross}}$ müsste für alle $f$ verschwinden: $Q_{\infty,\mathrm{pr}}^{\mathrm{cross}}(f,f)=0$. Via Polarisation folgt $Q_{\infty,\mathrm{pr}}^{\mathrm{cross}}\equiv0$.

$$\boxed{[O\text{-}220\text{-}1f_0\text{-additive-cross}]\quad\checkmark[M]_{\mathrm{neg}}}$$

**Konsequenz:** Eine nichttriviale Kopplung kann nicht als vierter Summand hinzugefügt werden. Sie muss eine nichtorthogonale Faktorisierung der bereits vorhandenen Gesamtform sein, eine Umverteilung der lokalen Beiträge bei unveränderter Gesamtsumme, eine positive Form auf einem eingeschränkten gemeinsamen Quellenbild, oder Teil einer größeren Quellenarchitektur, deren Kompression die exakt normalisierte Weil-Form ergibt.

---

## 5. Verbindlicher gemeinsamer Quellraum

$$\mathcal D_W = C_c^\infty(\mathbb R).$$

Auf ihm wohldefiniert: $Q_\infty, Q_{\mathrm{pole}}, Q_{\mathrm{prime}}, Q_W$. Die archimedische Jordanzerlegung (NEU-220c) liefert $H_{\infty,\pm}=L^2(\{|t|\gtrless t_\infty\},\tfrac{|A_\infty(t)|}{2\pi}dt)$ mit $T_{\infty,\pm}f=\mathbf1_{\{|t|\gtrless t_\infty\}}\hat f$. Der negative archimedische Kanal ist damit bereits exakt typisiert.

---

## 6. Der primarithmetische Formtyp

Auf $\mathcal D_W$:
$$
Q_{\mathrm{prime}}(f,h) = -\sum_{p}\sum_{m\ge1}\frac{\log p}{p^{m/2}}\left[\langle h,\tau_{m\log p}f\rangle + \langle h,\tau_{-m\log p}f\rangle\right],
$$
mit $(\tau_xf)(u)=f(u+x)$. Für feste $f,h$ endliche Summe — exakt typisierte hermitesche Form.

**Noch nicht konstruiert:** ein kanonischer positiver Hilbertraum $H_{\mathrm{pr}}$ mit $Q_{\mathrm{prime}}(f,h)=\langle T_{\mathrm{pr}}f,T_{\mathrm{pr}}h\rangle$. Eine solche positive Darstellung darf **nicht vorausgesetzt** werden. Offener Zieltyp:
$$
Q_{\mathrm{prime}}(f,h) = [T_{\mathrm{pr}}f,T_{\mathrm{pr}}h]_{\mathrm{pr}},
$$
wobei $E_{\mathrm{pr}}$ ein noch zu konstruierender topologischer Vektorraum, $[\cdot,\cdot]_{\mathrm{pr}}$ eine hermitesche, möglicherweise indefinite Form, $T_{\mathrm{pr}}:\mathcal D_W\to E_{\mathrm{pr}}$ die vollständigen Primzahlpotenzdaten trägt.

$$\boxed{[O\text{-}220\text{-}1f_0\text{-prime-target}]\quad ?[O]}$$

**Warnung:** Die formale Folge $\left(\sqrt{\log p/p^{m/2}},\tau_{\pm m\log p}f\right)_{p,m,\pm}$ liegt ohne zusätzliche Regulierung im Allgemeinen **nicht** in einer gewöhnlichen $\ell^2$-Direktsumme. Ein primarithmetischer Hilbertraum darf nicht durch eine ungeprüfte $\ell^2$-Behauptung eingeführt werden.

---

## 7. Korrekte globale Architektur: gemeinsames Quellenbild

Mit konstruiertem $T_{\mathrm{pr}}:\mathcal D_W\to E_{\mathrm{pr}}$: gemeinsame Analyseabbildung
$$J_W f = (T_{\infty,+}f, T_{\infty,-}f, T_{\mathrm{pr}}f).$$

Der relevante Raum ist **nicht** das freie Produkt aller drei Zielräume, sondern das gemeinsame Quellenbild:
$$\mathcal G_W^{(0)} = J_W(\mathcal D_W), \qquad \mathcal G_W = \overline{\mathcal G_W^{(0)}}.$$

Nur auf diesem Raum können archimedische und primarithmetische Koordinaten als gekoppelt gelten: Für $(x_+,x_-,y)\in\mathcal G_W$ sind $x_+,x_-,y$ nicht unabhängig — sie stammen aus derselben Testfunktion. Insbesondere enthält $\mathcal G_W$ im Allgemeinen **nicht** alle Vektoren $(0,x_-,0)$. Damit entfällt das Vollblock-No-Go auf diesem eingeschränkten Raum.

$$\boxed{[O\text{-}220\text{-}1f_0\text{-common-source}]\quad\checkmark[K/M]}$$

---

## 8. Zulässige Form der globalen Kopplung

Eine global gekoppelte Objekt-X-Form ist eine hermitesche Form $\mathfrak B_X:\mathcal G_W^{(0)}\times\mathcal G_W^{(0)}\to\mathbb C$ mit $\mathfrak B_X(J_Wf,J_Wh)=Q_W(f,h)$.

Die Positivitätsfrage $\mathfrak B_X(\xi,\xi)\ge0\ \forall\xi\in\mathcal G_W^{(0)}$ ist äquivalent zu $Q_W(f,f)\ge0\ \forall f\in\mathcal D_W$ — **das darf nicht als bereits bewiesene Eigenschaft eingesetzt werden**.

Eine nichttautologische Konstruktion muss $\mathfrak B_X$ aus der arithmetischen Quellenstruktur erzeugen, **ohne** Nullstellenlagen, RH-Annahme, nachträgliche spektrale Projektion auf den positiven Teil, oder optimierte Matrixkorrektur als Eingabedaten zu verwenden.

---

## 9. Was $B_{\infty,\mathrm{pr}}$ korrekt bezeichnet

$B_{\infty,\mathrm{pr}}$ bezeichnet **nicht** einen beliebigen beschränkten Operator zwischen zwei frei gewählten Hilberträumen, sondern die nichtorthogonale Wechselwirkung innerhalb einer Faktorisierung
$$\mathfrak B_X = \mathfrak B_{\infty\infty}+\mathfrak B_{\mathrm{pr,pr}}+\mathfrak B_{\infty,\mathrm{pr}}+\mathfrak B_{\mathrm{pr},\infty}$$
auf $\mathcal G_W$. Die Diagonalteile dürfen nicht stillschweigend mit den isolierten Formen $Q_\infty$ und $Q_{\mathrm{prime}}$ identifiziert werden. Erforderlich ist nur: $\mathfrak B_X(J_Wf,J_Wh)=Q_{\mathrm{pole}}(f,h)+Q_\infty(f,h)+Q_{\mathrm{prime}}(f,h)$ — jede Umverteilung zwischen Diagonal- und Kreuzteilen muss diese Identität exakt erhalten.

---

## 10. Unendlich-Rang-Notwendigkeit

Auf $H_{\infty,-}$: $Q_\infty|_{-} = -\|T_{\infty,-}f\|_{H_{\infty,-}}^2$. Eine positive Korrekturform $K$, die diesen Anteil vollständig kompensiert, muss $K[x]\ge\|x\|_{H_{\infty,-}}^2$ erfüllen. Falls $K=C^*C$ faktorisiert: $\|Cx\|\ge\|x\|$ auf dem negativen Quellenbild. Damit ist $C$ injektiv, nach unten beschränkt, von abgeschlossenem Bild, **insbesondere von unendlichem Rang**.

$$\boxed{[O\text{-}220\text{-}1f_0\text{-infinite-rank}]\quad\checkmark[M]}$$

**Verschärfung:** Auch eine Folge endlicher Kopplungen mit bei wachsendem Cutoff beschränktem effektivem Rang kann den Grenzsektor nicht kontrollieren. Für ein tragfähiges Grenzmodell muss $\operatorname{rank}B_{\infty,\mathrm{pr}}^{(N)}\to\infty$ entlang der Approximation gelten.

---

## 11. Kanonizitätsaxiome K1–K10

| Axiom | Forderung |
|---|---|
| **K1** — Exakte Formelkompatibilität | $\mathfrak B_X(J_Wf,J_Wf)=Q_W(f,h)$ ohne Restterme, ohne Doppelzählung |
| **K2** — Gemeinsame Quelle | Alle Komponenten aus derselben Testfunktion $(T_{\infty,+}f,T_{\infty,-}f,T_{\mathrm{pr}}f)$; unabhängig optimierte Vektoren unzulässig |
| **K3** — Involutionskompatibilität | Verträglich mit $f^\sharp(u)=\overline{f(-u)}$, erzeugt hermitesche Form |
| **K4** — Vollständige Primzahlpotenzstruktur | Gewichtung exakt $\log p/p^{m/2}$ für alle $p,m\ge1$; reine Primzahlkopplung ohne Potenzen unvollständig |
| **K5** — Unendlich-Rang-Kontrolle | Kontrolliert den unendlichdimensionalen negativen archimedischen Quellenraum; endlichdimensionaler Randkanal ungenügend |
| **K6** — Cutoff-Kompatibilität | Kompatible Formen $\mathfrak B_{X;S,N}$ für endliche Prim-/Basis-Cutoffs mit explizit festgelegten Grenzübergängen |
| **K7** — Geschlossenheit | Abschließbar auf dichtem Kern; erst danach Darstellungssatz für $H_X$ |
| **K8** — Anti-Tautologie | Weder Nullstellen von $\zeta$ noch RH-äquivalente positive Projektion als Eingabe |
| **K9** — Arithmetische Intrinsizität | Aus vorhandenen arithmetischen Daten (BC-/adelische Skalierung, Primkantenkorrespondenzen, Wres-Paarung, Primzahlpotenztranslationen, Feshbach-/Streuungsdaten); frei angepasster Matrixblock nicht kanonisch |
| **K10** — Nichtorthogonalität | Zerfällt nicht in orthogonale direkte Summe lokaler Kanäle; $B_{\infty,\mathrm{pr}}\neq0$ notwendig, aber allein nicht hinreichend |

---

## 12. Schur-Komplement-Warnung

Naiver Ansatz mit $A_{\mathrm{pr}}>0$: $\begin{pmatrix}A_\infty&B\\B^*&A_{\mathrm{pr}}\end{pmatrix}\ge0 \Rightarrow A_\infty-BA_{\mathrm{pr}}^{-1}B^*\ge0$. Der Term $BA_{\mathrm{pr}}^{-1}B^*$ wird von $A_\infty$ **subtrahiert** — eine Kopplung an einen positiven freien Primblock verbessert den Schur-Komplementwert nicht, sondern verschärft die notwendige Positivitätsbedingung. Dies ist dieselbe strukturelle Sperre wie das Vollblock-No-Go (§3).

Ein Schur-Komplement wird nur sinnvoll, wenn die Blockform nicht auf dem vollen direkten Summenraum positiv sein soll, der Primblock nicht als unabhängiger positiver Hauptblock interpretiert wird, oder die effektive archimedische Form nicht mit dem festen $A_\infty$ identisch ist.

---

## 13. Numerischer Pilot: zulässiger Typ

Der Pilot darf **nicht** eine frei wählbare Matrix $B_{\infty,S,N}$ optimieren, bis die Gesamtmatrix positiv wird (numerische Tautologie). Zulässig ist nur: eine konkrete arithmetische Kandidatenformel für $B_{\infty,\mathrm{pr}}$, eine gemeinsame endliche Testfunktionsbasis $\mathcal D_N\subset\mathcal D_W$, auf derselben Basis berechnete $Q_{\infty,N}, Q_{\mathrm{prime},S,N}, Q_{\mathrm{pole},N}$, eine aus der Kandidatenformel abgeleitete Kopplungsmatrix, Prüfung des vollständigen gemeinsamen Quellenbildes.

Zu messen: Zahl negativer Eigenwerte von $Q_{\infty,N}$; Rang der Kandidatenkopplung; kleinster Singularwert auf dem negativen archimedischen Unterraum; Zahl verbleibender negativer Eigenwerte der Gesamtform; Stabilität unter $N$-/$S$-Vergrößerung; Abhängigkeit von Basis/Cutoff; Übereinstimmung mit der exakt normalisierten expliziten Formel.

**Sofortiges Ausschlusskriterium:** Falls $\operatorname{rank}B_{\infty,S,N}<\operatorname{ind}_-Q_{\infty,N}$ und keine andere unendlich-rangige positive Komponente wirkt, kann die Kopplung nicht alle negativen Richtungen kontrollieren.

---

## 14. Knotenstruktur

```
[O-220-1f0] Typ einer globalen Archimedes-Prim-Kopplung        ✓[M]_part
      |
      +-- full-block positivity                                ✓[M]_neg
      |     A_infty als fester Hauptblock unmoeglich
      |
      +-- additive cross term                                  ✓[M]_neg
      |     veraendert die exakt fixierte Weil-Form
      |
      +-- common-source architecture                           ✓[K/M]
      |     G_W = closure(J_W(D_W))
      |
      +-- prime target E_pr, T_pr, [.,.]_pr                     ?[O]
      |
      +-- infinite-rank necessity                               ✓[M]
      |
      +-- exact redistribution/factorization                    ?[O]
      |
      +-- canonical arithmetic construction                     ?[O]
      |
      +-- closability and positive completion                   ?[O]
      |
      +-- numerical coupling pilot                               gesperrt
            bis eine konkrete Kandidatenformel vorliegt
```

---

## 15. Revidierte Statusbuchung

| Knoten | Status | Befund |
|---|---|---|
| $[O\text{-}220\text{-}1f_0]$ | $\checkmark[M]_{\mathrm{part}}$ | Typisiert, Konstruktion offen |
| positive Vollblockmatrix mit festem $A_\infty$ | $\checkmark[M]_{\mathrm{neg}}$ | Hauptkompression wäre negativ |
| zusätzlicher hermitescher Kreuzterm | $\checkmark[M]_{\mathrm{neg}}$ | Mit exakter Weil-Zerlegung unvereinbar |
| gemeinsamer Quellenkern | $\checkmark[M]$ | $\mathcal D_W=C_c^\infty(\mathbb R)$ |
| archimedischer negativer Zielraum | $\checkmark[M]$ | $H_{\infty,-}$ exakt konstruiert |
| Primform auf $\mathcal D_W$ | $\checkmark[M]$ | Vollständige Primzahlpotenzform |
| primarithmetischer Zielraum $E_{\mathrm{pr}}$ | $?[O]$ | Noch keine kanonische Faktorisierung |
| gemeinsames Quellenbild $\mathcal G_W$ | $\checkmark[K/M]$ | Korrekte Grundarchitektur |
| Unendlich-Rang-Notwendigkeit | $\checkmark[M]$ | Endlich-rangige Kopplung ausgeschlossen |
| positive Vervollständigung | $?[O]$ | Hauptkonstruktionsproblem |
| global gekoppelter $H_X$ | $?[O]$ | Erst nach Formabschluss typisierbar |

---

## 16. Nächster konkreter Arbeitsknoten

$$\boxed{[O\text{-}220\text{-}1f_0a]\quad\text{Primarithmetischer Zieltyp}}$$

Gesucht: $E_{\mathrm{pr}}$, $T_{\mathrm{pr}}:\mathcal D_W\to E_{\mathrm{pr}}$, $[\cdot,\cdot]_{\mathrm{pr}}$ mit $Q_{\mathrm{prime}}(f,h)=[T_{\mathrm{pr}}f,T_{\mathrm{pr}}h]_{\mathrm{pr}}$. Erst wenn dieser Zieltyp vorliegt, kann $B_{\infty,\mathrm{pr}}$ mathematisch typisiert definiert werden.

$$\boxed{\text{Primzahlpotenzform} \longrightarrow \text{kanonischer primarithmetischer Zielraum} \longrightarrow \text{gemeinsames Quellenbild} \longrightarrow \text{Kopplungspilot.}}$$

**Wichtigster neuer Befund:**
$$\boxed{\text{Die Kopplung kann nicht einen negativen Hauptblock auf einem freien direkten Summenraum „retten“.}}$$
Sie muss die archimedischen und primarithmetischen Daten bereits quellseitig voneinander abhängig machen. Erst auf diesem gemeinsamen Bild ist globale Positivität mathematisch möglich.
