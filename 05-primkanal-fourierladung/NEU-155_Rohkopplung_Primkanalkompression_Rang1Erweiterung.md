# NEU-155 — Rohkopplung, Primkanalkompression und Rang-1-Erweiterung

> Stand: 13. Juli 2026.  
> Vorgänger: NEU-41 (Fourier-Hebung, Kopplungsoperator), NEU-44 (Primkanten-Grundlagen), NEU-153 (Hebungsunabhängigkeit), NEU-154 (verbundene Paarung).  
> Typ: **Geometrietypblatt**. Struktursatz; kein Beweisblatt.

---

## DAG-Position

```
NEU-41  ──►  NEU-155  ──►  NEU-153 (Hebungsunabhängigkeit, Revisionshinweis)
NEU-44  ──►  NEU-155  ──►  NEU-154 (Pullback-Kandidat, Revisionshinweis)
```

---

## 155.0 — Drei-Operatoren-Typisierung

NEU-41 und NEU-44 definieren drei typologisch verschiedene Abbildungen, die in der bisherigen Notation unter dem Symbol $C_p^{\mathrm{rel}}$ zusammengefallen sind. NEU-155 trennt sie strikt.

**Rohkopplungsabbildung** (NEU-41 §4, (41.6)):

$$T_p: B_3^{\mathrm{adm}} \longrightarrow H_{J,N},
\qquad
T_p(x) := \Pi_{J,N}\widetilde\omega_2(x, L_3^\circ).$$

**Induzierter Primkanaloperator** (NEU-41 (41.7)), nach Wahl einer Hebung $\widehat\varepsilon_p$:

$$C_p^{[\widehat\varepsilon_p]}: \mathbb{C}\varepsilon_p \longrightarrow H_{J,N},
\qquad
C_p^{[\widehat\varepsilon_p]}(\lambda\varepsilon_p) = \lambda\,\Psi_p[\widehat\varepsilon_p].$$

**Hebungsabhängige Rang-1-Erweiterung** (NEU-44 §44.3, mit expliziter Hebungsabhängigkeit):

$$C_p^{\mathrm{rel}}[\widehat\varepsilon_p]
:= \iota_{J,N}\Psi_p[\widehat\varepsilon_p] \otimes f_3^{(p)*},
\tag{155.E.1}$$

wobei $\iota_{J,N}: H_{J,N} \hookrightarrow W_{\mathrm{res,rel}}$ die verwendete Einbettung bezeichnet
(deren Isometrie gesondert zu prüfen ist, s. §155.F).

**Trennungssatz:**

$$\boxed{T_p \neq C_p^{[\widehat\varepsilon_p]} \neq C_p^{\mathrm{rel}}[\widehat\varepsilon_p] \quad\text{als typisierte Abbildungen.}}$$

Sie sind durch den folgenden **Hauptsatz** verbunden.

**Status:** ✅[M]

---

## 155.A — Rohkopplung auf geladenen Moden

Für $u \neq 0$ gilt (NEU-41 (41.6)):

$$T_p(e_uV_p)
= -\Pi_{J,N}\sum_{s,m} \ell_{s,m}\,u\,s\log p\; e_{u+ps}V_{pm}.
\tag{155.A.1}$$

Die Indexabbildung $(s,m)\mapsto(u+ps,pm)$ ist für festes $u$ injektiv (NEU-153 §D.2): keine interne Auslöschung innerhalb der Summe vor der Projektion $\Pi_{J,N}$.

**Status:** ✅[M]

---

## 155.B — Verschwindung am Nullmodus

Wegen des Fourierfaktors $r=0$ (NEU-41 §2–§3, $\delta_{r,0}$-Regel):

$$\boxed{T_p(e_0V_p) = T_p(v_p) = 0.}
\tag{155.B.1}$$

Der Nullmodus $v_p = e_0V_p$ ist eine **algebraische Ableitungsobstruktion**, keine metrische Orthogonalität. Insbesondere folgt daraus nicht $\langle f_3^{(p)}, v_p\rangle = 0$; falls $f_3^{(p)} = v_p$ und beide normiert sind, gilt vielmehr $\langle f_3^{(p)}, v_p\rangle = 1$.

**Status:** ✅[M]

---

## 155.C — Konstruktion von $\Psi_p$ durch Linearität

Für $\widehat\varepsilon_p = v_p + k$ mit $k \in E_p^{\mathrm{ch}}$ gilt wegen (155.B.1) und Linearität von $T_p$:

$$\Psi_p[\widehat\varepsilon_p]
:= T_p(\widehat\varepsilon_p)
= T_p(k).
\tag{155.C.1}$$

Der ungeladene Anteil $v_p$ trägt nichts zur Kopplung bei; die gesamte Kopplung stammt aus der Hebungsänderung $k$.

**Konsequenz:** $\Psi_p[\widehat\varepsilon_p] = 0$ genau dann, wenn $k \in \ker T_p$.

**Status:** ✅[M] (NEU-41 §4; NEU-153 §D.0.1)

---

## 155.D — Induzierter Primkanaloperator

Nach Wahl von $\widehat\varepsilon_p$ definiert NEU-41 (41.7):

$$C_p^{[\widehat\varepsilon_p]}(\lambda\varepsilon_p) = \lambda\,\Psi_p[\widehat\varepsilon_p],
\qquad \lambda\in\mathbb{C}.
\tag{155.D.1}$$

Da der Definitionsbereich $\mathbb{C}\varepsilon_p$ eindimensional ist, hat $C_p^{[\widehat\varepsilon_p]}$ automatisch Rang höchstens 1. Dieser Rang-1-Befund ist **trivial** und kein Degenerationssatz über die Rohkopplung $T_p$.

Die Gram-Matrix $G_p^{\mathrm{raw}}(u,v) := \langle T_p(e_uV_p), T_p(e_vV_p)\rangle_{H_{J,N}}$ der Rohbilder kann beliebigen Rang haben.

**Status:** ✅[M]

---

## 155.E — Rang-1-Erweiterung und NEU-44-Identifikation

Die in NEU-44 §44.3 ohne explizite Hebungsabhängigkeit geschriebene Formel

$$C_p^{\mathrm{rel}} = c_p(e_1^{(p)}\otimes f_3^{(p)*})$$

ist korrekt zu lesen als $C_p^{\mathrm{rel}}[\widehat\varepsilon_p]$ für eine implizit gewählte normierte Hebung. Die einheitliche Definition lautet (155.E.1).

Für $\Psi_p[\widehat\varepsilon_p] \neq 0$ ist die polare Schreibweise

$$C_p^{\mathrm{rel}}[\widehat\varepsilon_p]
= c_p[\widehat\varepsilon_p]\bigl(e_1^{(p)}[\widehat\varepsilon_p]\otimes f_3^{(p)*}\bigr),
\quad
c_p[\widehat\varepsilon_p] = \|\Psi_p[\widehat\varepsilon_p]\|,
\quad
e_1^{(p)}[\widehat\varepsilon_p] = \frac{\Psi_p[\widehat\varepsilon_p]}{\|\Psi_p[\widehat\varepsilon_p]\|}$$

äquivalent zu (155.E.1). Bei $\Psi_p = 0$ ist die polare Schreibweise nicht definiert; (155.E.1) gilt weiterhin.

**Hauptsatz (drei Pfeile):**

$$\boxed{
\begin{aligned}
\Psi_p[\widehat\varepsilon_p] &= T_p(\widehat\varepsilon_p), \\
C_p^{[\widehat\varepsilon_p]}(\varepsilon_p) &= \Psi_p[\widehat\varepsilon_p], \\
C_p^{\mathrm{rel}}[\widehat\varepsilon_p]\,f_3^{(p)} &= \iota_{J,N}\,T_p(\widehat\varepsilon_p).
\end{aligned}
}
\tag{155.1}$$

**Zusatz zur Normfrage:** Aus der Vektoridentität in der dritten Zeile folgt die Normidentität $\|C_p^{\mathrm{rel}}[\widehat\varepsilon_p]f_3^{(p)}\| = \|T_p(\widehat\varepsilon_p)\|$ nur, wenn $\iota_{J,N}$ isometrisch ist. Diese Isometrie ist gesondert zu prüfen.

**Normierungsbedingung (NEU-41 §3, (41.4.3)):** Die korrekte Frage ist nicht $\|C_p^{\mathrm{rel}}v_p\| = 1$, sondern:

$$\left\|C_p^{\mathrm{rel}}[\widehat\varepsilon_p]\,f_3^{(p)}\right\| = \|T_p\widehat\varepsilon_p\| \stackrel{?}{=} 1.
\tag{155.E.2}$$

**Status:** ✅[Def] aus NEU-44 §44.3–§44.4; Isometrie von $\iota_{J,N}$: ❓[O]

---

## 155.F — Diagonaler und sesquilinearer Pullback

Die in NEU-41 §3 eingeführte verbundene Normalisierung $\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(x^\#x) = 1$ ist bislang nicht konstruktiv definiert. Zwei logisch verschiedene Pullbackaussagen sind zu unterscheiden.

**Diagonale Aussage** (für Liftgeometrie hinreichend):

$$\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(x^\#x)
\stackrel{?}{=}
\|T_px\|_{H_{J,N}}^2,
\qquad x\in\operatorname{dom}T_p.
\tag{155.F.1}$$

**Sesquilineare Aussage** (für Gram-Matrix und Orthogonalitätsstruktur erforderlich):

$$\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(x^\#y)
\stackrel{?}{=}
\langle T_px,T_py\rangle_{H_{J,N}},
\qquad x,y\in\operatorname{dom}T_p.
\tag{155.F.2}$$

(155.F.2) impliziert (155.F.1). Die Umkehrung durch Polarisation

$$\langle x,y\rangle = \tfrac{1}{4}\sum_{j=0}^{3} i^j\, q(x+i^jy)$$

gilt nur, wenn zuvor bewiesen ist, dass $(x,y)\mapsto\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(x^\#y)$ eine Hermitesche Sesquilinearform auf einem komplexen linearen Definitionsraum ist.

Die Vektoridentität (155.E.1) liefert unmittelbar:

$$C_p^{\mathrm{rel}}[\widehat\varepsilon_p]\,f_3^{(p)}
= \iota_{J,N}\,T_p(\widehat\varepsilon_p).
\tag{155.F.3}$$

**Status:**
$$\text{(155.F.1): ❓[O]}, \qquad
\text{(155.F.2): ❓[O]}, \qquad
\text{(155.F.3): ✅[M]}$$
bis auf die gesondert zu prüfende Normverträglichkeit von $\iota_{J,N}$.

**Die Liftgeometrie (§155.G–H) benötigt nur (155.F.1). Die volle sesquilineare Pullbackformel ist erst für die Gram- und Orthogonalitätsstruktur erforderlich.**

---

## 155.G — Quotientensphären-Geometrie unter (155.F.1)

**Voraussetzung:** (155.F.1) sei erfüllt.

Setze:

$$\mathcal{E}_p^{\mathrm{ch}}
:= E_p^{\mathrm{ch}}\cap\operatorname{dom}T_p,
\qquad
N_p^{\mathrm{raw}} := \ker\!\left(T_p|_{\mathcal{E}_p^{\mathrm{ch}}}\right),
\qquad
R_p^{\mathrm{raw}} := T_p(\mathcal{E}_p^{\mathrm{ch}}).$$

Unter (155.F.1) gilt für $\widehat\varepsilon_p = v_p + k$:

$$q_{\mathrm{conn}}(\widehat\varepsilon_p) = \|T_pk\|_{H_{J,N}}^2.
\tag{155.G.0}$$

Die normierte geladene Liftfaser ist:

$$\boxed{
\mathcal{L}_p^{\mathrm{ch}}
= v_p + \left\{ k\in\mathcal{E}_p^{\mathrm{ch}} : \|T_pk\|_{H_{J,N}} = 1 \right\}.
}
\tag{155.G.1}$$

Der Operator $T_p$ induziert eine isometrische lineare Bijektion

$$\overline{T}_p:
\mathcal{E}_p^{\mathrm{ch}}/N_p^{\mathrm{raw}} \longrightarrow R_p^{\mathrm{raw}}$$

für die Quotientennorm $\|[k]\|_{T_p} := \|T_pk\|_{H_{J,N}}$.

**Affine Nullraumfasern:** Ist $k_0\in\mathcal{E}_p^{\mathrm{ch}}$ mit $\|T_pk_0\| = 1$, so gilt:

$$v_p + k_0 + N_p^{\mathrm{raw}} \subseteq \mathcal{L}_p^{\mathrm{ch}}.
\tag{155.G.2}$$

**Phasenfasern:** Für eine einzelne Richtung $k$ gilt $q_{\mathrm{conn}}(v_p+\lambda k) = |\lambda|^2\|T_pk\|^2$; die Normierungsbedingung erzwingt $|\lambda| = \|T_pk\|^{-1}$, also einen **Kreis** von Phasen, keine affine Gerade.

**Vollständigkeit:** Der Quotient $\mathcal{E}_p^{\mathrm{ch}}/N_p^{\mathrm{raw}}$ ist nicht notwendig vollständig. Seine Hilbertvervollständigung ist kanonisch isometrisch zu $\overline{R_p^{\mathrm{raw}}}^{\,H_{J,N}}$. Die Faser (155.G.1) entspricht nach Vervollständigung der Einheitssphäre in $\overline{R_p^{\mathrm{raw}}}^{\,H_{J,N}}$.

$$\boxed{
\text{Geometrischer Typ: Einheitssphäre im normierten Rohkopplungsquotienten,}
\text{ mit affinen Fasern parallel zu }\ker T_p.
}$$

**Status:** ✅[M] bedingt auf (155.F.1).

**Verhältnis zu NEU-153 §D.0.5.B:** Der dortige positiv-definite Satz
($\mathcal{L}_p^{\mathrm{ch}} = \varnothing \Leftrightarrow v_p\perp E_p^{\mathrm{ch}}$)
bleibt als konditionaler Hilbertsatz korrekt. Unter (155.F.1) ist er jedoch **nicht anwendbar**, da $q_{\mathrm{conn}}(v_p) = 0 \neq 1$: die Voraussetzung $\|v_p\|_{\mathrm{conn}} = 1$ entfällt.

---

## 155.H — Existenzkriterium

**Voraussetzungen:** (155.F.1) und Skalarstabilität: $\mathcal{E}_p^{\mathrm{ch}}$ ist ein komplexer linearer Raum (insbesondere stabil unter nichtverschwindender Skalierung).

$$\boxed{
\mathcal{L}_p^{\mathrm{ch}}\neq\varnothing
\quad\Longleftrightarrow\quad
T_p(\mathcal{E}_p^{\mathrm{ch}})\neq\{0\}.
}
\tag{155.H.1}$$

*Beweis.* Existiert $w\in\mathcal{E}_p^{\mathrm{ch}}$ mit $T_pw\neq0$, so ist $k := w/\|T_pw\|$ (wegen Skalarstabilität in $\mathcal{E}_p^{\mathrm{ch}}$) eine zulässige geladene Hebungsänderung mit $\|T_pk\| = 1$; damit liegt $v_p+k\in\mathcal{L}_p^{\mathrm{ch}}$. Umgekehrt impliziert $v_p+k\in\mathcal{L}_p^{\mathrm{ch}}$ nach (155.G.1) sofort $T_pk\neq0$. $\square$

**Expliziter Nichtverschwinden-Test:** Aus (155.A.1) gilt

$$T_p(e_uV_p) = -\Pi_{J,N}\sum_{s,m}\ell_{s,m}\,u\,s\log p\; e_{u+ps}V_{pm}.$$

Damit ist $T_p(\mathcal{E}_p^{\mathrm{ch}})\neq\{0\}$, sobald ein Tripel $(u,s_0,m_0)$ mit $u\neq0$, $s_0\neq0$, $\ell_{s_0,m_0}\neq0$ existiert, für das $\Pi_{J,N}(e_{u+ps_0}V_{pm_0})\neq0$. Die Injektivität der Indexabbildung $(s,m)\mapsto(u+ps,pm)$ (NEU-153 §D.2) schließt interne Auslöschung vor $\Pi_{J,N}$ aus; Auslöschung durch $\Pi_{J,N}$ selbst muss gesondert ausgeschlossen werden.

**Status:** ✅[M] bedingt auf (155.F.1), Domänenwohlbestimmtheit und Skalarstabilität.

---

## 155.I — Konsequenzen für NEU-153 und NEU-154

**NEU-153:** §D.0.5.A fragte, ob $\operatorname{Tr}^{\mathrm{conn}}$ via (D.0.5.1) oder via (PB-raw) definiert ist, und formulierte dies als offene Quell/Ziel-Identifikation. NEU-155 löst die Ambiguität: der typologisch korrekte Pullbackkandidat auf dem Liftraum ist (155.F.1). Der Konventionstransfer $\|v_p\|_{\mathrm{conn}} = 1$ (§D.0.5.B Voraussetzung ⚠[O]) ist unter (155.F.1) **falsch**: $\|v_p\|_{\mathrm{conn}} = \|T_pv_p\| = 0$. §D.0.5.B ist als konditionaler Satz korrekt, aber auf die tatsächliche Geometrie nicht anwendbar.

**NEU-154:** Die dort gestellte Frage $\|C_p^{\mathrm{rel}}v_p\|^2 \stackrel{?}{=} 1$ ist typologisch falsch gestellt (fixierter Operator auf Liftvektor). Die korrekte Frage ist (155.E.2). NEU-154 §154.A sollte (D.0.5.1) durch (155.F.2) ersetzen und die Hebungsabhängigkeit explizit machen.

---

## 155.J — Endbefund

Die dreistufige Konstruktion lautet:

$$\boxed{
T_p(v_p) = 0,
\qquad
C_p^{[\widehat\varepsilon_p]}(v_p) = C_p^{\mathrm{rel}}[\widehat\varepsilon_p](v_p) = \Psi_p[\widehat\varepsilon_p] = T_p(\widehat\varepsilon_p).
}$$

Es gibt keinen Operatorwiderspruch zwischen NEU-41 und NEU-44; es gibt eine bislang unsichtbare hebungsabhängige Konstruktionsstufung.

$$\boxed{
\text{Die Liftgeometrie ist vollständig auf die diagonale Identität }
q_{\mathrm{conn}}(x) = \|T_px\|^2
\text{ reduziert.}
}$$

**Verbleibende Punkte (nachgeordnet, nicht geometrieblokkierend):**

| Punkt | Aussage | Status |
|---|---|---|
| (155.F.1) | Diagonaler Pullback $q_{\mathrm{conn}} = \|T_p\cdot\|^2$ | ❓[O] — Hauptidentifikationsfrage |
| (155.F.2) | Sesquilinearer Pullback (für Gram-Struktur) | ❓[O] — erfordert zusätzlich Sesquilinearitätsnachweis für $\operatorname{Tr}^{\mathrm{conn}}$ |
| Isometrie $\iota_{J,N}$ | Normverträglichkeit $H_{J,N}\hookrightarrow W_{\mathrm{res,rel}}$ | ❓[O] — nachgeordnete Verifikation |
| Skalarstabilität $\mathcal{E}_p^{\mathrm{ch}}$ | Stabilität zulässiger Hebungsänderungen unter Skalierung | ❓[O] — aus NEU-41 §3 zu entnehmen |
| $\Pi_{J,N}$-Nichtvernichtung | Mindestens ein Beitrag in (155.A.1) nicht durch $\Pi_{J,N}$ vernichtet | ❓[O] — nachgeordnet zu NEU-153 §D.2 |

---

## Verweise

- **NEU-41** §2–§4: $\delta_{r,0}$-Regel, Formeln (41.6)–(41.7), Wohlbestimmtheitsbedingung (41.4), verbundene Paarung §3
- **NEU-44** §44.1–§44.4: Rang-1-Modell, implizite Hebungsabhängigkeit von $C_p^{\mathrm{rel}}$
- **NEU-153** §D.0.1, §D.0.5.A–B, §D.2: Drei-Operatoren-Vorläufer, Quell/Ziel-Identifikation, Injektivitätssatz
- **NEU-154** §154.A: Pullback-Kandidat (zu revidieren gemäß §155.I)
- **NEU-152**: Nichtentartung $B_p\geq A/p$ (unberührt von NEU-155)
