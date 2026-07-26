# NEU-220f — PD-4c: Archimedischer Streufaktor und Zeitverzögerungsoperator

**Knoten:** `[O-220-1-PD4c-intrinsic-relative-origin]`  
**Stand:** 25. Juli 2026  
**Vorgänger:** NEU-220e (PD-4b ✓[K/M], PD-4c ?[O])  
**Ziel:** PD-4c teilweise schließen durch vier atomare Unterknoten.

Atomare Unterknoten:
- **PD-4c1** — Unitärer lokaler Streufaktor $S_\infty$ ✓[K/M]
- **PD-4c2** — Zeitverzögerungsidentität $Q_\infty = M_{\gamma_\infty^\mathrm{sym}}$ ✓[K/M]
- **PD-4c3** — Spur-Rückgewinnung $\Lambda_\Gamma = \frac1{4\pi}\tau_\infty(Q_\infty h(H_\infty))$ ✓[M]
- **PD-4c4** — Intrinsisches Streusystem $(H_0,H_1)$ ?[O]

---

## 0. Ausgangspunkt und Einschränkungsnotiz

NEU-220e hat festgestellt:
- **PD-4b ✓[K/M]:** $\Lambda_\Gamma(h)=\frac1{2\pi}\tau_\infty(M_{\gamma_\infty h})$ — typkorrekte semifinite Realisierung, aber $\gamma_\infty$ wird per Funktionalkalkül eingesetzt.
- **PD-4c ?[O]:** Intrinsischer Ursprung noch offen.

**DAG-Einschränkung (aus e4b7d9a):** Der rohe Polterm

$$
p_\infty^\mathrm{raw}(t) = -\frac{2it}{\frac14+t^2}
$$

verschwindet nur auf reellen geraden Testfunktionen. Auf dem vollständigen hermiteschen Raum $h(-t)=\overline{h(t)}$ ist das Polfunktional $\Lambda_\mathrm{pole}^\mathrm{raw}(h)$ im Allgemeinen nicht null. Die Formulierung „für die Weil-Form unsichtbar“ darf erst global behauptet werden, wenn der autoritative Weil-Testfunktionsraum auf den reell-geraden Sektor eingeschränkt ist. Dies betrifft `[O-220-1-PD3d4-pole-functional]` ?[O].

NEU-220f bearbeitet ausschließlich den Gammaterm $\gamma_\infty^\mathrm{sym}$; der Polterm bleibt separat offen.

---

## 1. PD-4c1 — Unitärer lokaler Streufaktor ✓[K/M]

**Definition.** Der archimedische lokale Streufaktor ist:

$$
\boxed{
S_\infty(t) := \frac{\Gamma_{\mathbb R}\!\left(\frac12-it\right)}{\Gamma_{\mathbb R}\!\left(\frac12+it\right)},
\qquad
\Gamma_{\mathbb R}(s) := \pi^{-s/2}\Gamma(s/2).
}
$$

**Satz PD-4c1 (Unitärität):** Für alle $t\in\mathbb R$ gilt $|S_\infty(t)|=1$.

**Beweis.** Die Schwarz-Reflexion liefert $\overline{\Gamma_{\mathbb R}(\frac12+it)} = \Gamma_{\mathbb R}(\frac12-it)$ für reelles $t$, denn $\Gamma_{\mathbb R}$ nimmt auf $\{\Re(s)>0\}\cap\mathbb R_{>0}$ reelle Werte an und setzt sich durch Schwarz-Reflexion fort. Also:

$$
|S_\infty(t)|^2
= S_\infty(t)\overline{S_\infty(t)}
= \frac{\Gamma_{\mathbb R}(\frac12-it)}{\Gamma_{\mathbb R}(\frac12+it)}
\cdot
\frac{\overline{\Gamma_{\mathbb R}(\frac12-it)}}{\overline{\Gamma_{\mathbb R}(\frac12+it)}}
= \frac{\Gamma_{\mathbb R}(\frac12-it)}{\Gamma_{\mathbb R}(\frac12+it)}
\cdot
\frac{\Gamma_{\mathbb R}(\frac12+it)}{\Gamma_{\mathbb R}(\frac12-it)}
= 1. \quad\square
$$

$S_\infty$ definiert damit einen unitären Multiplikationsoperator

$$
\mathscr{S}_\infty := M_{S_\infty}
$$

auf $L^2(\mathbb R,dt)$, mit $\mathscr{S}_\infty\in\mathcal{N}_\infty = L^\infty(\mathbb R)$.

**Herkunft.** $S_\infty(t)$ ist der standard archimedische lokale Faktor der funktionalen Gleichung von $\zeta$ in der Formulation von Tate/Iwasawa: Er erscheint als Quotient der $\Gamma_{\mathbb R}$-Faktoren bei $s$ und $1-s$ auf der kritischen Linie $s=\frac12+it$.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD4c1-unitary-scattering-factor}]\quad\checkmark[K/M].}
$$

---

## 2. PD-4c2 — Zeitverzögerungsidentität ✓[K/M]

**Vorbereitung.** Für $s=\frac12+it$ gilt:

$$
\partial_t\log\Gamma_{\mathbb R}\!\left(\tfrac12+it\right)
= \partial_t\left(-\tfrac12 it\log\pi + \log\Gamma\!\left(\tfrac14+\tfrac{it}2\right)\right)
= -\tfrac12 i\log\pi + \tfrac{i}{2}\psi\!\left(\tfrac14+\tfrac{it}2\right)
= i\gamma_\infty(t).
$$

Also:

$$
\boxed{
\frac{d}{dt}\log\Gamma_{\mathbb R}\!\left(\tfrac12+it\right) = i\gamma_\infty(t).
}
$$

**Satz PD-4c2 (Zeitverzögerungsidentität):**

$$
\boxed{
\frac{d}{dt}\log S_\infty(t)
= \frac{d}{dt}\log\Gamma_{\mathbb R}\!\left(\tfrac12-it\right)
- \frac{d}{dt}\log\Gamma_{\mathbb R}\!\left(\tfrac12+it\right)
= -i\gamma_\infty(-t) - i\gamma_\infty(t)
= -i\gamma_\infty^\mathrm{sym}(t).
}
$$

**Beweis.** Aus $\partial_t\log\Gamma_{\mathbb R}(\frac12-it) = -i\gamma_\infty(-t)$ (Kettenregel mit Vorzeichenwechsel) und der obigen Formel:

$$
\partial_t\log S_\infty(t)
= \partial_t\log\Gamma_{\mathbb R}\!\left(\tfrac12-it\right)
- \partial_t\log\Gamma_{\mathbb R}\!\left(\tfrac12+it\right)
= -i\gamma_\infty(-t) - i\gamma_\infty(t)
= -i\bigl(\gamma_\infty(t)+\gamma_\infty(-t)\bigr)
= -i\gamma_\infty^\mathrm{sym}(t). \quad\square
$$

**Operatorform.** Da $S_\infty$ unitär und glatt, gilt:

$$
iS_\infty(t)^* S_\infty'(t)
= i\cdot\overline{S_\infty(t)}\cdot\partial_t S_\infty(t)
= i\cdot\partial_t\log S_\infty(t)\cdot |S_\infty(t)|^2
= i\cdot(-i\gamma_\infty^\mathrm{sym}(t))\cdot 1
= \gamma_\infty^\mathrm{sym}(t).
$$

Also:

$$
\boxed{
Q_\infty
:= i\,\mathscr{S}_\infty^*\frac{d\mathscr{S}_\infty}{dt}
= M_{\gamma_\infty^\mathrm{sym}}.
}
$$

$Q_\infty$ ist der **archimedische Zeitverzögerungsoperator** im Sinne von Eisenbud-Wigner: Der Operator $-i\mathscr{S}^*\partial_t\mathscr{S}$ misst die durch das Streusystem induzierte Zeitverzögerung; hier liefert er genau das symmetrisierte Gamma-Symbol.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD4c2-time-delay-identity}]\quad\checkmark[K/M].}
$$

---

## 3. PD-4c3 — Spur-Rückgewinnung ✓[M]

**Satz PD-4c3 (Spurrückgewinnung):** Für $h\in\mathcal{S}(\mathbb R,\mathbb R)$ reell und gerade:

$$
\boxed{
\Lambda_\Gamma(h) = \frac1{4\pi}\,\tau_\infty\bigl(Q_\infty\,h(H_\infty)\bigr).
}
$$

**Beweis.** Aus PD-4c2: $Q_\infty = M_{\gamma_\infty^\mathrm{sym}}$. Also:

$$
\tau_\infty\bigl(Q_\infty h(H_\infty)\bigr)
= \tau_\infty\bigl(M_{\gamma_\infty^\mathrm{sym}}M_h\bigr)
= \tau_\infty\bigl(M_{\gamma_\infty^\mathrm{sym}h}\bigr)
= \int_{\mathbb R}\gamma_\infty^\mathrm{sym}(t)h(t)\,dt.
$$

Division durch $4\pi$ und Vergleich mit NEU-220d PD-3d3 für reelles gerades $h$:

$$
\frac1{4\pi}\int_{\mathbb R}\gamma_\infty^\mathrm{sym}(t)h(t)\,dt
= \frac1{2\pi}\int_{\mathbb R}\gamma_\infty(t)h(t)\,dt
= \Lambda_\Gamma(h). \quad\square
$$

**Vergleich mit PD-4b:** PD-4b lieferte $\Lambda_\Gamma(h)=\frac1{2\pi}\tau_\infty(M_{\gamma_\infty h})$ auf $\mathcal{S}_\mathrm{herm}$. PD-4c3 liefert $\Lambda_\Gamma(h)=\frac1{4\pi}\tau_\infty(Q_\infty h(H_\infty))$ auf dem reell-geraden Sektor. Das ist strukturell stärker: Das Gamma-Symbol erscheint nicht als direkt eingesetzter Funktionskalkul, sondern als logarithmische Ableitung eines unitären Streufaktors.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD4c3-trace-recovery}]\quad\checkmark[M].}
$$

---

## 4. PD-4c4 — Intrinsisches Streusystem ?[O]

**Offene Frage:** Gibt es ein Operatorpaar $(H_0,H_1)$ auf einem Hilbertraum $\mathcal{H}$, sodass die tatsächliche Wellenoperator-Streumatrix

$$
S = \Omega_+^*\Omega_-,
\qquad
\Omega_\pm = \lim_{t\to\pm\infty} e^{itH_1}e^{-itH_0}
$$

auf der kritischen Linie mit $\mathscr{S}_\infty$ übereinstimmt:

$$
S\big|_{\sigma=1/2} = \mathscr{S}_\infty?
$$

**Kandidaten und Status:**

| Ansatz | Idee | Status |
|---|---|---|
| Freier/gestörter Dilatationsoperator auf $\mathbb R^\times$ | $H_0=-ix\partial_x$, $H_1=H_0+V$ mit geeignetem $V$ | ?[O] |
| Funktionale-Gleichungs-Abbildung als unitärer Operator | $\mathscr{S}_\infty$ als Intertwiner $\pi_0\to\pi_1$ zweier $\mathbb R^\times$-Darstellungen | ?[O] |
| Archimedischer Grenzwert eines BC-Feshbach-Schur-Operators | $D_\mathrm{Arch}$ als Grenzwert von $D_{\mathrm{Arch},N}$ mit Streuanteil | ?[O] |
| Connes-Meyer-archimedisches Streusystem | $H_\infty^\mathrm{free}$ auf $L^2(\mathbb R_+,dx/x)$, $H_\infty^\mathrm{pert}$ mit Wechselwirkung | ?[O] |

**Einschränkung:** Ohne PD-4c4 ist $S_\infty$ ein kanonischer unitärer lokaler Faktor, der aus $\Gamma_{\mathbb R}$ *definiert* ist. Er organisiert den Ursprung von $\gamma_\infty^\mathrm{sym}$, erklärt ihn aber noch nicht als echte Streumatrix eines unabhängigen Operatorpaars.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD4c4-intrinsic-scattering-pair}]\quad?[O].}
$$

---

## 5. Aktualisierter PD-4-Status

| Knoten | Aussage | Status |
|---|---|---|
| PD-4a | Gewöhnliche Hilbertspur No-Go | ✓[M]_neg |
| PD-4b | Semifinite Spur $\tau_\infty$: $\Lambda_\Gamma=\frac1{2\pi}\tau_\infty(M_{\gamma_\infty h})$ | ✓[K/M] |
| PD-4c1 | Unitärer Streufaktor $S_\infty$, $|S_\infty|=1$ | ✓[K/M] |
| PD-4c2 | Zeitverzögerungsoperator $Q_\infty=M_{\gamma_\infty^\mathrm{sym}}$ | ✓[K/M] |
| PD-4c3 | Spurrückgewinnung $\Lambda_\Gamma=\frac1{4\pi}\tau_\infty(Q_\infty h(H_\infty))$ (reell-gerade $h$) | ✓[M] |
| PD-4c4 | Intrinsisches Streusystem $(H_0,H_1)$ mit $S=\mathscr{S}_\infty$ | ?[O] |
| Pol-Funktional | $\Lambda_\mathrm{pole}^\mathrm{raw}$ auf vollst. hermit. Testfunktionsraum | ?[O] |

$$
\boxed{\text{PD-4}\quad\checkmark[K/M]_{\mathrm{part}}.}
$$

PD-4c1–c3 zusammen heben PD-4c von ?[O] auf ✓[K/M]_part. PD-4c4 bleibt der konzeptionell tiefe offene Knoten.

---

## 6. Konsequenz für PD-5: Aufspaltung

PD-5 muss nicht vollständig bis PD-4c4 gesperrt bleiben. Sinnvolle Aufspaltung:

**PD-5a — Typisierter Anschluss der semifiniten Gammaform** (kann auf PD-4b aufbauen)

Kann bereits beginnen. Zielfrage: Wie setzt sich die semifinite archimedische Spur $\tau_\infty(\gamma_\infty(H_\infty)h(H_\infty))$ in den vollständigen adelischen Operator ein?

**PD-5b — Intrinsischer archimedisch-adelischer Operatoranschluss** (gesperrt bis PD-4c4 ≥ ✓[M])

Benötigt ein echtes Streusystem für den archimedischen Faktor, bevor der adelische Anschluss intrinsisch argumentiert werden kann.

Strategische Kette:

$$
\boxed{
S_\infty \longrightarrow Q_\infty \longrightarrow \Lambda_\Gamma
\longrightarrow \text{schwacher adelischer Anschluss (PD-5a)}
}
$$

parallel offen:

$$
\boxed{
\text{Welches echte Streusystem erzwingt }S_\infty? \quad (\text{PD-4c4, PD-5b})
}
$$

---

## 7. Vollständiger DAG-Stand NEU-220 (nach NEU-220f)

```
PD-1   checkmark[K/M]_part   Testfunktionsraum S_infty, Involution f^♯
PD-2   checkmark[K/M]         Mellin M_infty, Koordinatenübersetzung
PD-3   checkmark[K/M]         Gamma-Distribution vollständig
  ├── PD-3a–c  checkmark[M]/checkmark[K/M]
  └── PD-3d1–5  checkmark[M]...checkmark[K/M]
  └── [O-220-1-PD3d4-pole-functional]  ?[O]
         Polterm auf vollst. hermit. Raum offen
         Hinweis: verschwindet auf reell-geradem Sektor,
         aber nicht allgemein auf S_herm
PD-4   checkmark[K/M]_part
  ├── PD-4a   checkmark[M]_neg  (Hilbertspur No-Go)
  ├── PD-4b   checkmark[K/M]   (semifinite Spur tau_infty)
  ├── PD-4c1  checkmark[K/M]   (S_infty unitär)
  ├── PD-4c2  checkmark[K/M]   (Q_infty = M_gamma^sym)
  ├── PD-4c3  checkmark[M]     (Spurrückgewinnung reell-gerade)
  └── PD-4c4  ?[O]             (echtes Streusystem)
PD-5a  freigegeben (auf PD-4b/c3 aufbauend)
PD-5b  gesperrt bis PD-4c4 >= checkmark[M]
```

---

*Datei: `katalog/NEU-220f_Archimedischer_Streufaktor_und_Zeitverzoegerungsoperator.md` | 25. Juli 2026*  
*Kernresultat: PD-4c1–c3 ✓[K/M]/✓[M]; PD-4c4 ?[O]; PD-5a freigegeben*  
*Quellen: NEU-220d rev.2, NEU-220e, NEU-47*
