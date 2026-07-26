# NEU-159 — Dualer Projektionszeuge und lineare Liftzulässigkeit

> Stand: 14. Juli 2026. (Revision: Mitgliedschaft $e_{u_0}V_p \in \mathcal{E}_p^{\mathrm{lin,ch}}$ als explizite Prüfbedingung)  
> Vorgänger: NEU-157 §157.D, NEU-155 §155.A.1, NEU-41 §3.  
> Typ: **Konstruktiver Existenznachweis**.

---

## DAG-Position

```
NEU-157  ──►  NEU-159  ──►  NEU-160 (Quotient Q_p)
                    └──►  NEU-158 (Symmetrietest)
```

---

## 159.A — Lineare Präzulässigkeit: Kernraumrekonstruktion

$$\mathcal{E}_p^{\mathrm{lin}} = \ker(\pi_{\mathrm{prim}}) \cap \bigcap_j \ker(R_{p,j}).\tag{159.A.1}$$

Für jede Bedingung aus NEU-41 §3 ist Homogenität/Linearität des Operators $R_{p,j}$ zu prüfen:

| Bedingung | Operator | Homogen? | Status |
|---|---|---|---|
| $\pi_{\mathrm{prim}}(k)=0$ | $\pi_{\mathrm{prim}}$ | ✅ | ✅[M] |
| Weitere aus NEU-41 §3 | $R_{p,j}$ | zu prüfen | ❓[O] |

**Zielbefund:** $\mathcal{E}_p^{\mathrm{lin}}$ ist ein komplexer linearer Raum. **Statusmarker:** ❓[O].

---

## 159.B — Projektionsnichtvernichtung durch einen Dualzeugen

**Orthogonaler Projektionsfall:** Für $h \in H_{J,N}$ gilt $\langle \Pi_{J,N}x, h\rangle = \langle x,h\rangle$. Daher:
$$\langle T_p^{\mathrm{pre}}(e_uV_p), h\rangle \neq 0 \implies T_p(e_uV_p) \neq 0.\tag{159.B.1}$$

**Allgemeiner Idempotentenfall:** Für $\varphi$ mit $\varphi|_{\ker\Pi_{J,N}}=0$ und $\varphi(T_p^{\mathrm{pre}}(e_uV_p)) \neq 0$: da $x - \Pi_{J,N}x \in \ker\Pi_{J,N}$, gilt $\varphi(T_p(e_uV_p)) = \varphi(T_p^{\mathrm{pre}}(e_uV_p)) \neq 0$.

**Statusmarker:** ✅[M] (beide Prinzipien); Projektionstyp $\Pi_{J,N}$: ❓[O].

---

## 159.C — Minimaler Basiszeuge

### 159.C.1 — Zusätzliche Mitgliedschaftsbedingung

Der Dualzeuge beweist $T_p(e_{u_0}V_p) \neq 0$, aber er liefert $T_p(\mathcal{E}_p^{\mathrm{lin,ch}}) \neq \{0\}$ **nur dann**, wenn

$$e_{u_0}V_p \in \mathcal{E}_p^{\mathrm{lin,ch}}.\tag{159.C.0}$$

Dies ist eine eigenständige Prüfbedingung und muss aus NEU-41 §3 nachgewiesen werden.

### 159.C.2 — Definition des minimalen Basiszeugen

Ein **minimaler Basiszeuge** ist ein Quadrupel $(u_0, s_0, m_0, \rho_0)$ mit:

1. $e_{u_0}V_p \in \mathcal{E}_p^{\mathrm{lin,ch}}$ **(Mitgliedschaft)**
2. $u_0 \neq 0$, $s_0 \neq 0$, $\ell_{s_0,m_0} \neq 0$
3. $\langle e_{u_0+ps_0}V_{pm_0}, E_{\rho_0}\rangle \neq 0$
4. $\langle e_{u_0+ps}V_{pm}, E_{\rho_0}\rangle = 0$ für alle $(s,m) \neq (s_0,m_0)$

### 159.C.3 — Berechnung (mit Konvergenzvorbehalt)

Unter der Voraussetzung, dass die Rohkopplungssumme (157.B.1) endlich ist oder absolute Konvergenz vorliegt (termweise Paarung mit $E_{\rho_0}$ zulässig):

$$\langle T_p^{\mathrm{pre}}(e_{u_0}V_p), E_{\rho_0}\rangle
= -u_0 s_0 \log p\cdot \ell_{s_0,m_0}\cdot\langle e_{u_0+ps_0}V_{pm_0}, E_{\rho_0}\rangle \neq 0.\tag{159.C.1}$$

Im orthogonalen Projektionsfall folgt $T_p(e_{u_0}V_p) \neq 0$, und wegen (159.C.0):
$$T_p(\mathcal{E}_p^{\mathrm{lin,ch}}) \neq \{0\}.\tag{159.C.2}$$

**Statusmarker:** ✅[M] (Kriterium); Existenz von $(u_0,s_0,m_0,\rho_0)$ mit Mitgliedschaft (159.C.0): ❓[O].

---

## 159.D — Epistemische Bilanz

### 159.D.1 — Zwei konkrete Prüfungen

Die kurzfristige Spur ist auf genau zwei Aufgaben reduziert:

| Prüfung | Inhalt | Status |
|---|---|---|
| **(I) Mitgliedschaft** | $e_{u_0}V_p \in \mathcal{E}_p^{\mathrm{lin,ch}}$ (aus NEU-41 §3) | ❓[O] |
| **(II) Projektionszeuge** | $\langle T_p^{\mathrm{pre}}(e_{u_0}V_p), E_{\rho_0}\rangle \neq 0$ | ❓[O] |

### 159.D.2 — Vollständige Statusmarker

| Aussage | Status |
|---|---|
| Dualzeugenprinzip (159.B) | ✅[M] |
| Basiszeugenkriterium (159.C.1) | ✅[M] |
| Normierungslemma (NEU-157 §157.C) | ✅[M] |
| Mitgliedschaft $e_{u_0}V_p \in \mathcal{E}_p^{\mathrm{lin,ch}}$ | ❓[O] |
| Existenz $(u_0,s_0,m_0,\rho_0)$ mit Projektionszeuge | ❓[O] |
| $T_p(\mathcal{E}_p^{\mathrm{lin,ch}}) \neq \{0\}$ | ❓[O] bis zu (I)+(II) |
| $Q_p \neq \{0\}$ | ❓[O] bis zu (I)+(II); danach → NEU-160 |
| $\mathcal{S}_{p,\alpha} \neq \varnothing$ | ❓[O] bis zu (I)+(II), bedingt auf Formmodell |

### 159.D.3 — Implikationskette

$$\underbrace{(\mathrm{I}) + (\mathrm{II})}_{\text{konkrete Prüfungen}} + \text{Skalarstabilität}$$
$$\Downarrow$$
$$T_p(\mathcal{E}_p^{\mathrm{lin,ch}}) \neq \{0\}\quad[\text{modellunabhängig}]\qquad\checkmark[M]\text{ (nach Zeuge)}$$
$$\Downarrow\;(\text{NEU-160 §160.A–B})$$
$$Q_p \neq \{0\}\quad[\text{nichttrivialer Hilbertraum}]\qquad\checkmark[M]\text{ (nach Zeuge)}$$
$$\Downarrow\;(+ \text{Formmodell }\alpha_p)$$
$$\mathcal{S}_{p,\alpha} \neq \varnothing\quad\checkmark[M]\text{ bedingt auf Modellwahl}$$
$$\Downarrow$$
$$\text{NEU-158 mit } G_p \curvearrowright Q_p \text{ sachlich motiviert}$$

---

## Verweise

NEU-41 §3, NEU-143, NEU-155 §155.A.1, NEU-157 §157.A–D, NEU-158, NEU-160.
