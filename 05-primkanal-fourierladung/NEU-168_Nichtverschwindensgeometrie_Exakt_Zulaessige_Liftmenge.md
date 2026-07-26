# NEU-168 — Nichtverschwindensgeometrie der exakt zulässigen Liftmenge

**Status:** Reduktions- und Entscheidungsblatt.  
**Vorgänger:** NEU-157 rev.3 → NEU-166a → NEU-166b → NEU-167 → NEU-167b → NEU-168.  
**Gesperrt:** Behauptung $\mathcal{M}_p^{wit,raw}\neq\varnothing$ solange kein expliziter Rohzeuge oder vollständiger geometrischer Schnittbeweis vorliegt.

---

## 168.0 — DAG-Position und Ziel

NEU-167 und NEU-167b haben ergeben:

$$A_p = \varnothing, \qquad K_p^{hom} = K_p$$

im auditierten Quellenkegel. Die exakte Zulässigkeitsmenge wird daher nicht durch zusätzliche nichttriviale homogen-lineare Kerngleichungen beschrieben.

Die verbleibenden Bedingungen sind:
- die offene Fourierladungsbedingung,
- die quadratische $W_{\mathrm{res}}$-Normierung,
- die Hebungsunabhängigkeits- bzw. Faktorisierungsbedingung,
- gegebenenfalls weitere quellenfest definierte nichtlineare Bedingungen.

Der Auftrag ist keine weitere Suche nach Operatoren $L_{p,a}$, sondern die mengentheoretische Zeugenfrage:

$$\boxed{\text{Enthält die exakt zulässige Liftmenge ein Element, dessen präprojektive Rohkopplung nicht verschwindet?}}$$

---

## 168.A — Kontrollierter modaler Rohbereich

NEU-157 rev.3, §157.H, Gleichung (157.B.1), definiert den präprojektiven Rohoperator auf geladenen Moden $e_u V_p$, $u \neq 0$. Zur Vermeidung eines nicht quellenfesten Koeffizientenimports wird die Formel zunächst operatoriell geschrieben:

$$G_p^{raw}(e_u V_p) := T_p^{pre}(e_u V_p), \qquad u \neq 0.$$

Dabei bezeichnet $G_p^{raw} := T_p^{pre}$ weiterhin eine Arbeitsdefinition aus NEU-166b und keine aus einer älteren Quelle importierte Symbolidentität.

Als minimal sicherer Definitionsbereich wird der algebraische modale Raum angesetzt:

$$D_{p,\mathrm{fin}}^{ch} := \operatorname{span}_{\mathrm{fin}}\{e_u V_p : u \neq 0\}.$$

Auf diesem Raum wird $G_p^{raw}$ linear fortgesetzt:

$$G_p^{raw}\!\left(\sum_{u\neq0}^{\mathrm{fin}} a_u e_u V_p\right) := \sum_{u\neq0}^{\mathrm{fin}} a_u\, T_p^{pre}(e_u V_p).$$

Da nur endliche Summen zugelassen werden, entstehen auf dieser Stufe keine Konvergenzfragen.

$$\boxed{G_p^{raw}\text{ ist auf }D_{p,\mathrm{fin}}^{ch}\text{ algebraisch wohldefiniert.}}$$

Eine Erweiterung auf unendliche Fourierentwicklungen oder auf den vollständigen Raum $D_p^{wit}$ bleibt offen.

---

## 168.B — Ladungsoperator und induzierter Operator $B_p$

Definiere den Koeffizienten- bzw. Ladungsoperator

$$P_p^{ch}: D_{p,\mathrm{fin}}^{ch} \longrightarrow c_{00}(\mathbb{Z}\setminus\{0\})$$

durch

$$P_p^{ch}\!\left(\sum_{u\neq0}^{\mathrm{fin}} a_u e_u V_p\right) := (a_u)_{u\neq0}.$$

Definiere anschließend

$$B_p: c_{00}(\mathbb{Z}\setminus\{0\}) \longrightarrow \operatorname{codom}(T_p^{pre})$$

durch

$$B_p((a_u)_u) := \sum_{u\neq0}^{\mathrm{fin}} a_u\, T_p^{pre}(e_u V_p).$$

Dann gilt auf dem kontrollierten modalen Rohbereich:

$$\boxed{G_p^{raw} = B_p \circ P_p^{ch} \quad\text{auf }D_{p,\mathrm{fin}}^{ch}.}$$

Insbesondere folgt:

$$\ker(P_p^{ch}) \subseteq \ker(G_p^{raw}).$$

Auf $D_{p,\mathrm{fin}}^{ch}$ ist $\ker(P_p^{ch}) = \{0\}$. Bei einer späteren Erweiterung auf Hebungen mit ungeladenen oder höheren Komponenten kann der Kern jedoch nichttrivial werden.

**Sperrklausel:** Die Faktorisierung $G_p^{raw} = B_p \circ P_p^{ch}$ darf zunächst nur auf demjenigen Bereich verwendet werden, auf dem nachgewiesen ist, dass $G_p^{raw}$ ausschließlich von den geladenen Fourierkoeffizienten abhängt. Sie darf nicht ohne Audit auf allgemeine Hebungen

$$\sum_{u\neq0} a_{p,u} e_u V_p + \text{höhere oder nullspurige Terme}$$

übertragen werden.

---

## 168.C — Exakte Liftmenge ohne Ladungsforderung

Wähle einen Basispunkt $\widehat{\varepsilon}_p^{\,0}$ mit $\pi_{\mathrm{prim}}(\widehat{\varepsilon}_p^{\,0}) = \varepsilon_p$. Jede weitere Hebung derselben Primärklasse besitzt die Form

$$\widehat{\varepsilon}_p^{\,0} + k, \qquad k \in K_p,$$

wobei $K_p := \ker(\pi_{\mathrm{prim}})$.

Definiere die exakte Liftmenge ohne Fourierladungsforderung:

$$\mathcal{M}_p := \left\{ \widehat{\varepsilon}_p^{\,0} + k : k \in K_p,\; \mathcal{Q}_p(k) = 0,\; \mathcal{F}_p(k) = 0 \right\}.$$

Hier bezeichnet

$$\mathcal{Q}_p(k) := 2\operatorname{Re} h_p(\widehat{\varepsilon}_p^{\,0}, k) + h_p(k,k)$$

die quadratische $W_{\mathrm{res}}$-Normierungsbedingung. Das Symbol $\mathcal{F}_p(k) = 0$ steht ausschließlich als Sammelnotation für alle zusätzlich quellenfest formulierten exakten Faktorisierungs- oder Hebungsunabhängigkeitsbedingungen. Es darf nicht als Linearitätsbehauptung interpretiert werden.

Falls keine solche eigenständige Gleichung auf dem Liftbereich konstruiert ist, ist $\mathcal{F}_p$ nicht künstlich einzuführen; dann wird $\mathcal{M}_p$ nur mit den tatsächlich vorhandenen Bedingungen definiert.

---

## 168.D — Geladene und zeugende Teilmengen

Die Fourier-geladene Teilmenge:

$$\mathcal{M}_p^{ch} := \left\{ \widehat{\varepsilon}_p \in \mathcal{M}_p : P_p^{ch}(\widehat{\varepsilon}_p) \neq 0 \right\} = \mathcal{M}_p \setminus \ker(P_p^{ch}).$$

Die präprojektive Zeugenmenge:

$$\mathcal{M}_p^{wit,raw} := \left\{ \widehat{\varepsilon}_p \in \mathcal{M}_p^{ch} : G_p^{raw}(\widehat{\varepsilon}_p) \neq 0 \right\}.$$

Daher gilt die rein mengentheoretische Äquivalenz:

$$\boxed{\mathcal{M}_p^{wit,raw} \neq \varnothing}$$

genau dann, wenn

$$\boxed{\mathcal{M}_p \not\subseteq \ker(P_p^{ch}) \cup \ker(G_p^{raw}).}$$

Dies ist die ursprüngliche Zeugenbedingung.

---

## 168.E — Vereinfachung unter der Rohfaktorisierung

Angenommen, auf dem relevanten Teil von $\mathcal{M}_p$ gilt quellenfest $G_p^{raw} = B_p \circ P_p^{ch}$. Dann folgt

$$\ker(P_p^{ch}) \subseteq \ker(G_p^{raw}),$$

somit

$$\ker(P_p^{ch}) \cup \ker(G_p^{raw}) = \ker(G_p^{raw}).$$

Die Zeugenbedingung vereinfacht sich zu:

$$\boxed{\mathcal{M}_p \not\subseteq \ker(G_p^{raw}).}$$

Äquivalent:

$$\boxed{\exists\, \widehat{\varepsilon}_p \in \mathcal{M}_p \quad\text{mit}\quad G_p^{raw}(\widehat{\varepsilon}_p) \neq 0.}$$

Wegen der Faktorisierung impliziert $G_p^{raw}(\widehat{\varepsilon}_p) \neq 0$ automatisch $P_p^{ch}(\widehat{\varepsilon}_p) \neq 0$. Die Fourierladungsbedingung muss in diesem Fall nicht zusätzlich geprüft werden.

Die schärfste atomare Zeugenbedingung lautet:

$$\boxed{\exists\, \widehat{\varepsilon}_p \in \mathcal{M}_p \quad\text{mit}\quad P_p^{ch}(\widehat{\varepsilon}_p) \notin \ker(B_p).}$$

**Stärkster neuer Punkt:** Die Vereinfachung

$$\mathcal{M}_p \not\subseteq \ker(P_p^{ch}) \cup \ker(G_p^{raw}) \quad\Longrightarrow\quad \mathcal{M}_p \not\subseteq \ker(G_p^{raw})$$

macht die offene Fourierladungsbedingung zu keinem zusätzlichen Hindernis: Nichtverschwindende Rohkopplung erzwingt automatisch nichtverschwindende Ladung.

---

## 168.F — Nullraum- und Kollisionsaudit von $B_p$

Die Nichtverschwindensfrage zerfällt in zwei logisch verschiedene Probleme.

### Problem F.1 — Ist $B_p$ selbst nichttrivial?

Hinreichend ist die Existenz eines Modus $u \neq 0$ mit $T_p^{pre}(e_u V_p) \neq 0$. NEU-157 §157.H liefert hierfür einen präprojektiven Nichtverschwindenssatz unter den dort ausdrücklich genannten Voraussetzungen:

$$\boxed{\text{NEU-157 rev.3, §157.H, Gleichung (157.B.1).}}$$

### Problem F.2 — Wie groß ist $\ker(B_p)$?

Selbst wenn jeder einzelne Modus nichttrivial abgebildet wird, können Linearkombinationen durch Zielkoordinatenkollisionen verschwinden:

$$\sum_{u\neq0} a_u\, T_p^{pre}(e_u V_p) = 0.$$

Zu prüfen ist, ob verschiedene Tripel $(u, s, m)$ der Rohformel dieselbe Zielmode erzeugen. Die Kollisionsrelation:

$$(u, s, m) \sim (u', s', m') \quad\Longleftrightarrow\quad e_{u+ps}V_{pm} = e_{u'+ps'}V_{pm'},$$

d.h. $u + ps = u' + ps'$ und $pm = pm'$. Für jede Zielkoordinate $\nu$ entsteht eine lineare Gleichung

$$\sum_{(u,s,m):\, u+ps=\nu_1,\, pm=\nu_2} \lambda_{p;u,s,m}\, a_u = 0,$$

wobei $\lambda_{p;u,s,m}$ den quellenexakten Koeffizienten aus Gleichung (157.B.1) bezeichnet. Damit ist $\ker(B_p)$ der Lösungsraum des vollständigen Kollisionssystems.

**Einfaches Nichtverschwindenskriterium:** Existieren $u_0 \neq 0$ und eine Zielkoordinate $\nu_0$, sodass der Koeffizient von $T_p^{pre}(e_{u_0} V_p)$ in $\nu_0$ nicht null ist und kein anderer geladener Modus im betrachteten Träger dieselbe Zielkoordinate $\nu_0$ erzeugt, dann gilt für jede Koeffizientenfolge mit $a_{u_0} \neq 0$:

$$B_p((a_u)_u) \neq 0.$$

Dies liefert einen elementaren Zeugen ohne vollständige Berechnung von $\ker(B_p)$.

---

## 168.G — Quadratische Normierung entlang einer Richtung

Sei $k \in K_p$ eine Richtung, die alle außer der quadratischen Bedingung bereits erfüllt. Betrachte die reelle Linie

$$\widehat{\varepsilon}_p^{\,0} + t k, \qquad t \in \mathbb{R}.$$

Die Normierungsbedingung lautet:

$$\mathcal{Q}_p(tk) = 2t\operatorname{Re} h_p(\widehat{\varepsilon}_p^{\,0}, k) + t^2 h_p(k,k) = 0.$$

Neben $t = 0$ existiert ein nichttrivialer Schnittpunkt $t_* \neq 0$, falls $h_p(k,k) \neq 0$ und $\operatorname{Re} h_p(\widehat{\varepsilon}_p^{\,0}, k) \neq 0$. Dann:

$$t_* = -\frac{2\operatorname{Re} h_p(\widehat{\varepsilon}_p^{\,0}, k)}{h_p(k,k)} \neq 0.$$

Falls außerdem $G_p^{raw}(k) \neq 0$ und der Rohoperator auf der affinen Variation linear bzw. differenzlinear wirkt, gilt

$$G_p^{raw}\bigl(\widehat{\varepsilon}_p(t_*)\bigr) \neq 0$$

vorbehaltlich eines möglichen Beitrags des Basispunkts und einer exakten Typprüfung.

**Eindimensionales hinreichendes Kriterium:** Ein Rohzeuge folgt, wenn eine Richtung $k \in K_p$ existiert mit:
- $\mathcal{F}_p(k) = 0$,
- $G_p^{raw}(k) \neq 0$,
- $h_p(k,k) \neq 0$,
- $\operatorname{Re} h_p(\widehat{\varepsilon}_p^{\,0}, k) \neq 0$,
- und die Rohkopplung am nichttrivialen Quadrikschnitt nicht durch den Basispunktbeitrag ausgelöscht wird.

**Entartete Fälle:**
- Falls $h_p(k,k) = 0$ und $\operatorname{Re} h_p(\widehat{\varepsilon}_p^{\,0}, k) = 0$: Die gesamte Linie liegt in der Normierungsquadrik.
- Falls $h_p(k,k) = 0$ und $\operatorname{Re} h_p(\widehat{\varepsilon}_p^{\,0}, k) \neq 0$: $t = 0$ ist der einzige Schnittpunkt.
- Falls $h_p(k,k) \neq 0$ und $\operatorname{Re} h_p(\widehat{\varepsilon}_p^{\,0}, k) = 0$: Ebenfalls $t = 0$ der einzige reelle Schnittpunkt entlang dieser Richtung.

Scheitert die eindimensionale Route, muss eine zweidimensionale Schnittebene untersucht werden; daraus darf noch keine Nichtexistenz geschlossen werden.

---

## 168.H — Entscheidungsbaum

| Schritt | Frage | Status |
|---|---|---|
| 1 | $G_p^{raw}$ auf modalem Unterraum wohldefiniert? | ✓ auf $D_{p,\mathrm{fin}}^{ch}$; Erweiterung offen |
| 2 | Faktorisierung $G_p^{raw} = B_p \circ P_p^{ch}$ auf kontrolliertem Bereich? | ✓ per Definition von $B_p$; volle Domäne offen |
| 3 | Ist $B_p \neq 0$? | Offen — [O-168-3], aus NEU-157 §157.H |
| 4 | Relevante Ladungsfolge außerhalb $\ker(B_p)$? | Offen — [O-168-3] Kollisionssystem |
| 5 | Schneidet $\mathcal{M}_p$ das Komplement von $\ker(G_p^{raw})$? | Offen — [O-168-4] bis [O-168-6] |
| 6 | Entscheidung $\mathcal{M}_p^{wit,raw} \neq \varnothing$ | Offen — [O-168-7] |

---

## 168.I — Offene Punkte

**[O-168-1]** Quellenfeste Bestimmung des vollständigen Definitionsbereichs von $G_p^{raw} = T_p^{pre}$. Insbesondere: Wirkt $G_p^{raw}$ ausschließlich auf der geladenen modalen Komponente oder auch auf höheren bzw. nullspurigen Termen?

**[O-168-2]** Nachweis der Faktorisierung $G_p^{raw} = B_p \circ P_p^{ch}$ auf der für $\mathcal{M}_p$ relevanten Domäne.

**[O-168-3]** Bestimmung des Kollisionssystems und des Nullraums $\ker(B_p)$.

**[O-168-4]** Konstruktion einer Richtung $k \in K_p$ mit $P_p^{ch}(k) \notin \ker(B_p)$.

**[O-168-5]** Prüfung, ob eine solche Richtung mit den exakten nichtlinearen Bedingungen außer der Normierung kompatibel ist.

**[O-168-6]** Lösung der quadratischen Normierungsbedingung entlang einer nichtverschwindenden Richtung oder, falls erforderlich, in einer zweidimensionalen Schnittebene.

**[O-168-7]** Entscheidung der zentralen Inklusion:

$$\boxed{\mathcal{M}_p \not\subseteq \ker(G_p^{raw})}$$

bzw. äquivalent, nach gesicherter Faktorisierung:

$$\boxed{\exists\, \widehat{\varepsilon}_p \in \mathcal{M}_p \quad\text{mit}\quad P_p^{ch}(\widehat{\varepsilon}_p) \notin \ker(B_p).}$$

---

## 168.J — Vorläufiger Status

Derzeit quellenfest:

$$A_p = \varnothing, \qquad K_p^{hom} = K_p.$$

Auf dem endlichen geladenen modalen Rohbereich:

$$G_p^{raw} = B_p \circ P_p^{ch}.$$

Noch nicht entschieden:

$$\boxed{\mathcal{M}_p \not\subseteq \ker(G_p^{raw}).}$$

Daher:

$$\boxed{\text{Die präprojektive Zeugenexistenz bleibt offen.}}$$

NEU-168 reduziert sie auf zwei konkrete mathematische Aufgaben:

$$\boxed{\text{Nullraum- bzw. Kollisionsanalyse von }B_p}$$

und

$$\boxed{\text{Schnitt der exakten Normierungsmenge mit }\operatorname{dom}(G_p^{raw})\setminus\ker(G_p^{raw}).}$$

---

## Commit-Regel

NEU-168 ist als Reduktions- und Entscheidungsblatt committed. Gesperrt bleibt ausschließlich die Behauptung $\mathcal{M}_p^{wit,raw} \neq \varnothing$, solange weder ein expliziter exakt zulässiger Rohzeuge noch ein vollständiger geometrischer Schnittbeweis vorliegt.

---

## Referenzverknüpfungen im DAG

| Blatt | Abhängigkeit |
|---|---|
| NEU-167b [O-167-2] | $A_p = \varnothing$ im auditierten Quellenkegel |
| NEU-157 rev.3 §157.H Gl. (157.B.1) | Definition $T_p^{pre}$; F.1-Nichtverschwindenssatz |
| NEU-166b | Arbeitsdefinition $G_p^{raw} := T_p^{pre}$ |
| NEU-166a | Architektur $\tilde{T}_p \to T_p^{adm} \to \bar{T}_p$ |
| NEU-169 (geplant) | Kollisionsanalyse $\ker(B_p)$ — [O-168-3] |
