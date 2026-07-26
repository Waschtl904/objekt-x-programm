# NEU-169 — Kollisionssystem und Einzelmoden-Nichtverschwindung von $B_p$

**Status:** Kollisions- und Reduktionsblatt.  
**Vorgänger:** NEU-157 rev.3 → NEU-168 → NEU-169.  
**Gesperrt:** $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$ ohne Quellenimport; $\ker(B_p)=\{0\}$ ohne Endlichkeits- oder Annihilatornachweis; $\mathcal{M}_p^{wit,raw}\neq\varnothing$ ohne exakte Zulässigkeits- und Normierungsprüfung.

---

## 169.0 — DAG-Position und Auftrag

NEU-168 hat den präprojektiven Rohoperator auf dem algebraischen geladenen Modenraum in der Form

$$G_p^{raw} = B_p \circ P_p^{ch}$$

reduziert. Der offene Punkt [O-168-3] verlangt:
- die Bestimmung der Zielkoordinatenkollisionen,
- die Analyse von $\ker(B_p)$,
- nach Möglichkeit einen elementaren Rohzeugen ohne vollständige Kernberechnung.

NEU-169 trennt diese drei Aufgaben.

---

## 169.A — Quellenformel

Nach NEU-157 rev.3, §157.H, Gleichung (157.B.1), gilt für $u \neq 0$:

$$T_p^{pre}(e_u V_p) = -\sum_{s,m} \ell_{s,m}\, u\, s\log(p)\, e_{u+ps}V_{pm}. \tag{157.B.1}$$

Auf dem endlichen geladenen Modenraum wird gesetzt $G_p^{raw} := T_p^{pre}$, und für eine endlich getragene Koeffizientenfolge $a = (a_u)_{u\neq0}$:

$$B_p(a) = -\sum_{u\neq0}\sum_{s,m} a_u\, \ell_{s,m}\, u\, s\log(p)\, e_{u+ps}V_{pm}.$$

---

## 169.B — Exakte Kollisionsrelation

Zwei Tripel $(u,s,m)$ und $(u',s',m')$ erzeugen dieselbe algebraische Zielbasis genau dann, wenn

$$e_{u+ps}V_{pm} = e_{u'+ps'}V_{pm'}.$$

Da die Basis durch Fourierindex und Monoidindex bestimmt ist, ist dies äquivalent zu $pm = pm'$ und $u+ps = u'+ps'$. Für festes $p$ folgt $m = m'$ und $u - u' = p(s'-s)$. Damit lautet die Kollisionsrelation:

$$\boxed{(u,s,m)\sim_p(u',s',m') \iff m=m' \text{ und } u-u'=p(s'-s).} \tag{169.1}$$

Insbesondere ist

$$\boxed{u \equiv u' \pmod{p}}$$

eine notwendige Bedingung für jede Kollision. Die Kollisionsstruktur zerfällt daher in Restklassen des Eingangsindex $u$ modulo $p$.

---

## 169.C — Keine internen Kollisionen bei einem Einzelmodus

Fixiere $u \neq 0$. Angenommen,

$$e_{u+ps}V_{pm} = e_{u+ps'}V_{pm'}.$$

Dann liefert (169.1): $m = m'$ und $p(s'-s) = 0$, also $s = s'$. Folglich ist die Abbildung

$$(s,m) \longmapsto (u+ps,\, pm)$$

für festes $u$ injektiv. Damit gilt:

$$\boxed{\text{Innerhalb von }T_p^{pre}(e_uV_p)\text{ treten keine Zielkoordinatenkollisionen auf.}} \tag{169.2}$$

Insbesondere können verschiedene Summanden eines einzelnen Eingangsmodus sich nicht durch algebraische Zielkoordinatenkollision gegenseitig auslöschen.

---

## 169.D — Einzelmoden-Nichtverschwindung

Definiere den gewichteten Träger von $L_3^\circ$:

$$\operatorname{supp}^{\times}(L_3^\circ) := \left\{ (s,m) : s\ell_{s,m} \neq 0 \right\}.$$

Ist $\operatorname{supp}^{\times}(L_3^\circ) \neq \varnothing$, so wähle $(s_0, m_0)$ mit $s_0 \ell_{s_0,m_0} \neq 0$. Für jedes $u \neq 0$ besitzt dann $T_p^{pre}(e_u V_p)$ in der Zielkoordinate $e_{u+ps_0}V_{pm_0}$ den Koeffizienten

$$-u\, s_0\ell_{s_0,m_0}\log(p) \neq 0.$$

Wegen der Injektivität aus §169.C kann kein anderer Summand desselben Eingangsmodus diese Zielkoordinate aufheben. Daher:

$$\boxed{\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing \Longrightarrow T_p^{pre}(e_uV_p)\neq0 \quad \forall u\neq0.} \tag{169.3}$$

Äquivalent:

$$\boxed{B_p(\delta_u) \neq 0 \quad \forall u\neq0,} \tag{169.4}$$

wobei $\delta_u$ die einzelne Ladungskoordinate $u$ bezeichnet. Folglich enthält der Kern von $B_p$ keine Koordinatenachse:

$$\boxed{\mathbb{C}\delta_u \cap \ker(B_p) = \{0\} \quad \forall u\neq0.} \tag{169.5}$$

Dieser Satz ist bedingt durch die quellenfeste Prüfung $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$. Diese Prüfung bleibt als eigener Quellenimport zu behandeln.

---

## 169.E — Koeffizientengleichungen für allgemeine Mehrmodenvektoren

Sei $a = (a_u)_{u\neq0} \in c_{00}(\mathbb{Z}\setminus\{0\})$. Für eine Zielkoordinate $e_r V_{pm}$ ist der Koeffizient von $B_p(a)$:

$$-\log(p)\sum_{\substack{s\in\mathbb{Z}\\ r-ps\neq0}} a_{r-ps}\,(r-ps)\,s\,\ell_{s,m}.$$

Daher gilt $a \in \ker(B_p)$ genau dann, wenn für alle $r$ und $m$:

$$\sum_{\substack{s\in\mathbb{Z}\\ r-ps\neq0}} a_{r-ps}\,(r-ps)\,s\,\ell_{s,m} = 0. \tag{169.6}$$

Dies ist das vollständige lineare Kollisionssystem.

---

## 169.F — Restklassenzerlegung und Faltungsform

Fixiere eine Restklasse $c \in \mathbb{Z}/p\mathbb{Z}$. Schreibe $u = c+pk$, $r = c+pj$, $s = j-k$. Definiere:

$$x_k^{(c)} := (c+pk)\,a_{c+pk},$$

wobei im Fall $c=0$ der verbotene Index $u=0$ durch $x_0^{(0)} := 0$ ausgeschlossen wird. Für jedes $m$ definiere die gewichtete $L_3^\circ$-Folge

$$b_t^{(m)} := t\ell_{t,m}.$$

Dann wird Gleichung (169.6) zu:

$$\sum_k x_k^{(c)}\, b_{j-k}^{(m)} = 0 \quad \forall j,m. \tag{169.7}$$

In Faltungsschreibweise:

$$\boxed{x^{(c)} * b^{(m)} = 0 \quad \forall m.} \tag{169.8}$$

Der Operator $B_p$ zerfällt somit nach Restklassen modulo $p$, und sein Kern ist der gemeinsame Faltungsannihilator:

$$\boxed{\ker(B_p) = \bigoplus_{c\in\mathbb{Z}/p\mathbb{Z}} \left\{ a^{(c)} : x^{(c)} * b^{(m)} = 0 \text{ für alle } m \right\}.} \tag{169.9}$$

---

## 169.G — Bedingtes Injektivitätskriterium

Angenommen, es existiert ein $m_0$, für das $(t\ell_{t,m_0})_{t\in\mathbb{Z}}$ nicht null und endlich getragen ist. Identifiziert man endlich getragene Folgen mit Laurentpolynomen, so entspricht die Faltung dem Produkt:

$$X_c(z)\, B_{m_0}(z) = 0.$$

Da $\mathbb{C}[z,z^{-1}]$ nullteilerfrei ist und $B_{m_0}(z) \neq 0$, folgt $X_c(z) = 0$ für jede Restklasse $c$, also $a = 0$. Daher gilt unter dieser Endlichkeitshypothese:

$$\boxed{\ker(B_p) = \{0\} \quad \text{auf } c_{00}(\mathbb{Z}\setminus\{0\}).} \tag{169.10}$$

Ohne quellenfeste Endlichkeits- oder geeignete Nichtperiodizitätseigenschaft der Folgen $(t\ell_{t,m})_t$ darf diese Injektivität nicht behauptet werden.

---

## 169.H — Konsequenz für den kritischen Pfad

Für die Konstruktion eines algebraischen Rohzeugen ist die vollständige Berechnung von $\ker(B_p)$ **nicht erforderlich**.

Sobald $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$ quellenfest nachgewiesen ist, liefert jeder einzelne geladene Modus $e_u V_p$, $u\neq0$, einen präprojektiven Nichtverschwindensvektor:

$$G_p^{raw}(e_uV_p) \neq 0.$$

Falls zusätzlich der Import $e_u V_p \in K_p$ ($u\neq0$) verwendet werden darf, ist $k_u := e_u V_p$ eine nichtverschwindende geladene Liftänderungsrichtung. Damit verschiebt sich der kritische Pfad:

$$\boxed{\text{Nicht mehr die Kollisionsanalyse ist der Hauptengpass,}}$$

sondern:

$$\boxed{\text{die Vereinbarkeit einer Einzelmodenrichtung mit Normierungsquadrik,}}$$
$$\boxed{\text{exakten Faktorisierungsbedingungen und Quotientenabstieg.}}$$

---

## 169.I — Status von [O-168-3]

**[O-168-3a] Kollisionsrelation**

$$\boxed{(u,s,m)\sim_p(u',s',m') \iff m=m' \text{ und } u-u'=p(s'-s).}$$

Status: $\boxed{\checkmark[M].}$

**[O-168-3b] Einzelmoden-Kollision**

Für festes $u$ ist $(s,m)\mapsto(u+ps,pm)$ injektiv.

Status: $\boxed{\checkmark[M].}$

**[O-168-3c] Vollständiger Nullraum**

Der vollständige Nullraum wird durch das Faltungssystem (169.9) beschrieben. Seine explizite Bestimmung hängt von der Fourierstruktur von $L_3^\circ$ ab.

Status: $\boxed{?[O].}$

---

## 169.J — Offene Punkte

**[O-169-1]** Quellenfeste Entscheidung: $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$? Das heißt: $\exists(s_0,m_0)$ mit $s_0\ell_{s_0,m_0}\neq0$.

**[O-169-2]** Bestimmung, ob für mindestens ein $m_0$ die Folge $(t\ell_{t,m_0})_t$ endlich getragen ist.

**[O-169-3]** Falls keine Endlichkeit gilt: Bestimmung des gemeinsamen Faltungsannihilators der Folgen $b^{(m)} = (t\ell_{t,m})_t$.

**[O-169-4]** Prüfung, ob die Einzelmodenrichtung $k_u = e_u V_p$ alle exakten Bedingungen außer der Normierung erfüllt.

**[O-169-5]** Schnitt der affinen Einzelmodenfamilie $\widehat{\varepsilon}_p^{\,0} + a\, e_u V_p$ mit der Normierungsquadrik.

---

## 169.K — Gesamtbefund

Die Kollisionsstruktur ist vollständig bestimmt:

$$\boxed{\text{Kollisionen sind restklassenweise Faltungskollisionen modulo }p.}$$

Bei einem einzelnen Eingangsmodus treten keine internen Zielkollisionen auf:

$$\boxed{T_p^{pre}(e_uV_p) \neq 0}$$

sobald der gewichtete Fourierträger von $L_3^\circ$ nicht leer ist. Daher ist ein zusätzlicher Nachweis einer kollisionsfreien Zielkoordinate für einen Einzelmodenzeugen nicht erforderlich.

Die vollständige Kernberechnung von $B_p$ bleibt für Mehrmodenkombinationen offen, ist aber nicht mehr Voraussetzung für den elementaren präprojektiven Rohzeugen.

$$\boxed{[O\text{-}168\text{-}3a/3b]\text{ geschlossen;} \quad [O\text{-}168\text{-}3c]\text{ offen.}}$$

---

## Commit-Regel

NEU-169 ist als Kollisions- und Reduktionsblatt committed. Gesperrt bleiben:
- $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$ ohne Quellenimport,
- $\ker(B_p)=\{0\}$ ohne Endlichkeits- oder Annihilatornachweis,
- $\mathcal{M}_p^{wit,raw}\neq\varnothing$ ohne exakte Zulässigkeits- und Normierungsprüfung.

---

## Referenzverknüpfungen im DAG

| Blatt | Abhängigkeit |
|---|---|
| NEU-168 [O-168-3] | Primärer Auftrag dieses Blatts |
| NEU-157 rev.3 §157.H Gl. (157.B.1) | Quellenformel für $T_p^{pre}$ und Kollisionsrechnung |
| NEU-41 Gl. (41.6) | Quellenangabe Rohformel |
| NEU-170 (geplant) | Quellenimport $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$ — [O-169-1] |
| NEU-171 (geplant) | Normierungsgeometrie Einzelmodus — [O-169-5] |
