# NEU-160 — Rohkopplungsquotient und induzierte Symmetrie

> Stand: 14. Juli 2026. (Revision: §160.B beide Isometrie-Richtungen; §160.C Bildrauminvarianz automatisch; vollständige Statusarchitektur)  
> Vorgänger: NEU-159, NEU-157 §157.A.  
> Typ: **Konstruktiver Aufbau des Zielraums für NEU-158**.  
> Voraussetzung: $T_p(\mathcal{E}_p^{\mathrm{lin,ch}}) \neq \{0\}$ (NEU-159 §159.D, nach Zeugen-Konstruktion).

---

## DAG-Position

```
NEU-159  ──►  NEU-160  ──►  NEU-158 (Kommutantentest)
```

---

## 160.A — Quotientenraum und Positivdefinitheit

$$N_p := \mathcal{E}_p^{\mathrm{lin,ch}} \cap \ker T_p,\qquad Q_p^{\mathrm{raw}} := \mathcal{E}_p^{\mathrm{lin,ch}} / N_p.\tag{160.A.1}$$

**Lemma:** Das Sesquilinearform
$$\langle [k],[\ell]\rangle_{Q_p} := \alpha_p\langle T_pk, T_p\ell\rangle_{H_{J,N}}\tag{160.A.2}$$
ist auf $Q_p^{\mathrm{raw}}$ wohldefiniert und positiv definit.

*Beweis.*
- **Wohldefiniert:** $k' = k+n$, $n \in N_p$ $\Rightarrow$ $T_pk' = T_pk$. ✓
- **Positiv semidefinit:** $\alpha_p\|T_pk\|^2 \geq 0$. ✓
- **Positiv definit:** $\langle[k],[k]\rangle_{Q_p} = 0 \iff T_pk = 0 \iff k \in N_p \iff [k] = [0]$. ✓ $\square$

$$Q_p := \overline{Q_p^{\mathrm{raw}}}\quad(\text{Hilbert-Vervollständigung}).\tag{160.A.3}$$

$Q_p \neq \{0\}$ $\iff$ $T_p(\mathcal{E}_p^{\mathrm{lin,ch}}) \neq \{0\}$ (NEU-159 §159.D).

**Statusmarker:** ✅[M] (Lemma); $Q_p \neq \{0\}$: ❓[O] bis NEU-159 Zeuge, dann ✅[M].

---

## 160.B — Skaliert-isometrische Identifikation mit dem Kopplungsbild

**Satz:** Definiere
$$J_p: Q_p^{\mathrm{raw}} \longrightarrow T_p(\mathcal{E}_p^{\mathrm{lin,ch}}),\qquad J_p[k] := \sqrt{\alpha_p}\, T_pk.\tag{160.B.1}$$

Dann ist $J_p$ wohldefiniert, linear, injektiv und **isometrisch**:
$$\|J_p[k]\|_{H_{J,N}}^2 = \alpha_p\|T_pk\|^2 = \|[k]\|_{Q_p}^2.\tag{160.B.2}$$

Die Umkehrabbildung:
$$J_p^{-1}(T_pk) = \alpha_p^{-1/2}\,[k],\qquad \|J_p^{-1}(T_pk)\|_{Q_p} = \alpha_p^{-1/2}\|T_pk\|_{H_{J,N}}.\tag{160.B.3}$$

**Beide Richtungen zusammengefasst:**
$$J_p[k] = \sqrt{\alpha_p}\,T_pk, \qquad J_p^{-1}(T_pk) = \alpha_p^{-1/2}[k].\tag{160.B.4}$$

**Bemerkung zur unsignierten Abbildung:** Die unskalierte Abbildung $\widetilde{T}_p: [k] \mapsto T_pk$ erfüllt $\|\widetilde{T}_p[k]\|_{H_{J,N}} = \alpha_p^{-1/2}\|[k]\|_{Q_p}$; sie ist daher nur für $\alpha_p = 1$ isometrisch.

Durch Fortsetzung auf die Vervollständigungen:
$$Q_p \cong \overline{T_p(\mathcal{E}_p^{\mathrm{lin,ch}})} \subseteq H_{J,N}.\tag{160.B.5}$$

**Statusmarker:** ✅[M].

---

## 160.C — Abstieg der Symmetrie

### 160.C.1 — Starke Hypothesen (bevorzugte Route)

Sei $\rho_p: G_p \to \mathrm{GL}(\mathcal{E}_p^{\mathrm{lin,ch}})$ eine Gruppenwirkung. Die drei Bedingungen:

$$\boxed{
\begin{aligned}
&(\alpha)\quad \rho_p(g)\mathcal{E}_p^{\mathrm{lin,ch}} = \mathcal{E}_p^{\mathrm{lin,ch}} &&(\text{Präzulässigkeitsinvarianz})\\
&(\beta)\quad T_p\rho_p(g) = U_p(g)T_p &&(\text{Intertwining})\\
&(\gamma)\quad U_p(g) \in \mathcal{U}(H_{J,N}) &&(\text{Unitärität auf Zielraum})
\end{aligned}
}\tag{160.C.1}$$

**Statusmarker:** Alle drei ❓[O] — $G_p$, $\rho_p$, $U_p$ noch aus NEU-41 §3 zu identifizieren.

### 160.C.2 — Implikationen aus ($\alpha$)+($\beta$)+($\gamma$)

Unter diesen drei Bedingungen folgen die nachstehenden Aussagen **automatisch** (keine zusätzlichen offenen Prüfungen):

**(i) Nullraumabstieg:**
$$T_pk = 0 \Rightarrow T_p(\rho_p(g)k) = U_p(g)T_pk = 0 \Rightarrow \rho_p(g)N_p \subseteq N_p.$$
Mit ($\alpha$) gilt $\rho_p(g^{-1})N_p \subseteq N_p$ analog, also $\rho_p(g)N_p = N_p$.

**(ii) Wohldefiniertheit der Quotientenwirkung:**
$$\pi_p(g)[k] := [\rho_p(g)k]\quad\text{wohldefiniert auf }Q_p^{\mathrm{raw}}.$$

**(iii) Unitärität auf dem Quotienten:**
$$\|\pi_p(g)[k]\|_{Q_p}^2 = \alpha_p\|T_p\rho_p(g)k\|^2 = \alpha_p\|U_p(g)T_pk\|^2 = \alpha_p\|T_pk\|^2 = \|[k]\|_{Q_p}^2.$$

**(iv) Bildrauminvarianz (automatisch, kein eigenständiger offener Punkt):**
$$U_p(g)T_p(\mathcal{E}_p^{\mathrm{lin,ch}}) = T_p(\rho_p(g)\mathcal{E}_p^{\mathrm{lin,ch}}) \overset{(\alpha)}{=} T_p(\mathcal{E}_p^{\mathrm{lin,ch}}).$$
Durch Abschluss: $U_p(g)\overline{T_p(\mathcal{E}_p^{\mathrm{lin,ch}})} = \overline{T_p(\mathcal{E}_p^{\mathrm{lin,ch}})}$.

**(v) Unitäre Darstellung:**
$$\pi_p: G_p \longrightarrow \mathcal{U}(Q_p).\tag{160.C.2}$$

**Statusmarker:** Implikationen (i)–(v): ✅[M] als allgemeine Sätze; Nachweis von ($\alpha$)+($\beta$)+($\gamma$): ❓[O].

### 160.C.3 — Schwache Route (nur Nullraumabstieg)

Falls Intertwining nicht zugänglich: mindestens $\rho_p(g)N_p \subseteq N_p$ genügt für Wohldefiniertheit von $\pi_p(g)[k]$, liefert aber keine Isometrie automatisch.

### 160.C.4 — Eigentliche offene Prüfung

Die **einzige eigenständige offene Prüfung** im Symmetrieabstieg ist:

$$\text{($\alpha$)+(\beta)+(\gamma$): Identifikation von }G_p,\,\rho_p,\,U_p\text{ aus NEU-41 §3.}\qquad ?[O]$$

Nach deren Nachweis sind (i)–(v) automatisch geschlossen.

---

## 160.D — Vollständige Statusarchitektur

| Aussage | Status |
|---|---|
| $Q_p^{\mathrm{raw}}$ wohldefiniert und positiv definit (160.A.2) | ✅[M] |
| Skaliert-isometrische Identifikation $J_p$ (160.B.1–3) | ✅[M] |
| $Q_p \cong \overline{T_p(\mathcal{E}_p^{\mathrm{lin,ch}})}$ (160.B.5) | ✅[M] |
| Allgemeines Nullraumabstiegslemma | ✅[M] |
| Allgemeines Intertwining $\Rightarrow$ Unitäritätslemma (160.C.2) | ✅[M] |
| Bildrauminvarianz automatisch aus ($\alpha$)+($\beta$) | ✅[M] |
| $Q_p \neq \{0\}$ | ❓[O] bis NEU-159 Zeuge; ✅[M] danach |
| Konkrete Wirkung $\rho_p$ erfüllt ($\alpha$)+($\beta$)+($\gamma$) | ❓[O] |
| Konkrete unitäre Darstellung $\pi_p: G_p \to \mathcal{U}(Q_p)$ | ❓[O] als Anwendung |
| Äquivalenz $\pi_p(G_p)' = \mathbb{C}I \iff \pi_p$ irreduzibel (Schurs Lemma) | ✅[M] (allg. Satz) |
| Konkrete Irreduzibilität von $\pi_p$ | ❓[O] → NEU-158 |

### 160.D.1 — Unmittelbare Forschungsspur

Die Kette lässt sich auf zwei Schritte komprimieren:

$$\underbrace{\text{NEU-159: Mitgliedschaft + Dualzeuge}}_{\Rightarrow\, Q_p \neq \{0\}}$$
$$\Downarrow$$
$$\underbrace{\text{NEU-160: Präzulässigkeitsinvarianz (}\alpha\text{) + Intertwining (}\beta\text{,}\gamma\text{)}}_{\Rightarrow\, \pi_p: G_p \to \mathcal{U}(Q_p)\text{ (automatisch)}}$$
$$\Downarrow$$
$$\underbrace{\text{NEU-158: Irreduzibilität von }\pi_p}_{\Rightarrow\text{ Ausgang A oder B}}$$

---

## Verweise

NEU-41 §3, NEU-157 §157.A, NEU-159 §159.D, NEU-158.
