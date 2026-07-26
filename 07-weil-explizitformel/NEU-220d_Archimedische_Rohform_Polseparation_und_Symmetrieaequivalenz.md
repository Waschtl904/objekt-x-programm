# NEU-220d — PD-3d: Archimedische Rohform, Polseparation und Symmetrieäquivalenz

**Knoten:** `[O-220-1-PD3d-Weil-normalization]`  
**Stand:** 25. Juli 2026 (rev.2)  
**Vorgänger:** NEU-220c (PD-3d ✓[M]_part), NEU-47 (D_Arch-Designentscheidung)  
**Ziel:** PD-3d von ✓[M]_part auf ✓[K/M] schließen.

> **Rev.2-Korrektur (25. Juli 2026):** Algebraischer Fehler im Polterm von rev.1 behoben.
> Der Ausdruck $\frac{1}{\frac12+it}+\frac{1}{-\frac12+it}$ vereinfacht sich zu $-\frac{2it}{\frac14+t^2}$,
> nicht zu $\frac{1}{\frac14+t^2}$. Letzteres gehört zur reflektierten Kombination
> $\frac1s+\frac1{1-s}$. PD-3d4 und Abschnitt 0 wurden entsprechend korrigiert.
> Knoten `[O-220-1-PD3d4-pole-formula-v0]` wird ✓[M]_neg geschlossen.
> Knoten `[O-220-1-PD3d4-pole-functional]` bleibt ?[O].

Atomare Unterknoten:
- **PD-3d1** — Symmetrielexikon ✓[M]
- **PD-3d2** — Realität der Rohform ✓[M]
- **PD-3d3** — Äquivalenz der Darstellungen ✓[M]
- **PD-3d4** — Pol-/Gamma-Separation (rev.2) ✓[M] / `[O-220-1-PD3d4-pole-functional]` ?[O]
- **PD-3d5** — Autoritative Konvention ✓[K/M]

---

## 0. Ausgangspunkt und archimedische Zerlegung (rev.2)

NEU-220c hat zwei Ebenen als quellenfest geschlossen:

- ξ-Normalisierung: $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ — **✓ quellenfest**
- Konturmaß: $ds/(2\pi i)\mapsto dt/(2\pi)$ via NEU-29 — **✓ quellenfest**

NEU-47 fixiert den *gesamten* archimedischen Faktor:

$$
\frac{D_\infty'}{D_\infty}(s)
= \frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2).
$$

### Korrektes rohe Polterm-Resultat auf $s=\frac12+it$

Für $s=\frac12+it$ gilt exakt:

$$
\frac1s+\frac1{s-1}
= \frac1{\frac12+it}+\frac1{-\frac12+it}
= \frac{\frac12-it+\frac12+it}{(\frac12+it)(-\frac12+it)}
= \frac{1}{-\frac14-t^2}
\cdot(-1)
$$

oder direkt:

$$
\frac{1}{\frac12+it}+\frac{1}{-\frac12+it}
= \frac{-\frac12+it+\frac12+it}{(\frac12+it)(-\frac12+it)}
= \frac{2it}{-\frac14-t^2}
= -\frac{2it}{\frac14+t^2}.
$$

Also:

$$
\boxed{
p_\infty^\mathrm{raw}(t)
:= \frac1{\frac12+it}+\frac1{-\frac12+it}
= -\frac{2it}{\frac14+t^2}.
}
$$

**Warnung:** Davon zu unterscheiden ist die reflektierte Kombination:

$$
\frac1s+\frac1{1-s}
= \frac1{\frac12+it}+\frac1{\frac12-it}
= \frac{\frac12-it+\frac12+it}{\frac14+t^2}
= \frac{1}{\frac14+t^2}.
$$

Die positive Lorentz-Funktion $\left(\tfrac14+t^2\right)^{-1}$ gehört zur reflektierten Form, **nicht** zur logarithmischen Ableitung $\partial_s\log(s(s-1))$. Beide Ausdrücke sind nicht identisch.

### Vollständige archimedische Zerlegung auf der kritischen Linie

$$
\boxed{
\frac{D_\infty'}{D_\infty}\!\left(\tfrac12+it\right)
= p_\infty^\mathrm{raw}(t) + \gamma_\infty(t),
}
$$

mit

$$
p_\infty^\mathrm{raw}(t) = -\frac{2it}{\frac14+t^2}
$$

und

$$
\gamma_\infty(t) = -\tfrac12\log\pi + \tfrac12\psi\!\left(\tfrac14+\tfrac{it}{2}\right).
$$

**Symmetrieeigenschaften von $p_\infty^\mathrm{raw}$:**

Da $p_\infty^\mathrm{raw}(t)$ rein imaginär und ungerade ist:

$$
p_\infty^\mathrm{raw}(-t) = \overline{p_\infty^\mathrm{raw}(t)} = -p_\infty^\mathrm{raw}(t).
$$

Für hermitesche Testfunktionen $h(-t)=\overline{h(t)}$ ist $\Lambda_\mathrm{pole}^\mathrm{raw}(h)$ trotzdem reell.
Für reelles gerades $h$ hingegen gilt:

$$
\boxed{
\int_{\mathbb R}p_\infty^\mathrm{raw}(t)\,h(t)\,dt = 0.
}
$$

Der rohe Polterm verschwindet auf dem reell-geraden Testfunktionsraum. Dies zeigt, dass die positive Lorentz-Funktion nicht als naiver Ersatz für $p_\infty^\mathrm{raw}$ eingesetzt werden darf.

PD-3d betrifft ausschließlich $\gamma_\infty(t)$. Die genaue Übertragung des Polanteils in die Weil-Testfunktionsform ist Knoten `[O-220-1-PD3d4-pole-functional]`.

---

## 1. NEU-47-Import: Designentscheidungen D1–D3

Aus NEU-47 (Sätze 47.D1–D3) übernehmen wir autoritativ:

$$
\boxed{D_\mathrm{Arch}\text{ trägt }D_\infty(s) = \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2).} \tag{D1}
$$

$$
\boxed{D_\mathrm{scatt}\text{ trägt den Hadamard-Divisor (nichttriviale Nullstellen).}} \tag{D2}
$$

$$
\boxed{D_\mathrm{Jac}\text{ ist divisorneutral (exponentieller Renormierungsfaktor).}} \tag{D3}
$$

Keine Doppelzählung: Gamma liegt ausschließlich in $D_\mathrm{Arch}$, Nullstellen ausschließlich in $D_\mathrm{scatt}$.

$$
\boxed{\Lambda_\mathrm{Arch} = \Lambda_\mathrm{pole} + \Lambda_\Gamma.}
$$

PD-3d betrifft nur $\Lambda_\Gamma$; der Polterm-Funktional-Knoten ist offen.

---

## 2. PD-3d1 — Symmetrielexikon ✓[M]

Sei $\mathcal{M}_\infty$ die in NEU-220a fixierte Mellin-Transformation mit $h(t)=(\mathcal{M}_\infty f)(t)$,
$s=\tfrac12+it$. Sei ferner:
- $f^\sharp(x):=\overline{f(x^{-1})}$ — Selbstadjungiertheitsinvolution aus NEU-220a
- $(Jf)(x):=f(x^{-1})$ — reiner Inversionsoperator

**Satz PD-3d1 (Symmetrielexikon):**

$$
\boxed{f(x)\in\mathbb R\;\forall x \iff h(-t)=\overline{h(t)}.} \tag{L1}
$$

$$
\boxed{f^\sharp=f \iff h(t)\in\mathbb R\;\forall t.} \tag{L2}
$$

$$
\boxed{Jf=f \iff h(-t)=h(t).} \tag{L3}
$$

**Beweis.**
*(L1):* $h(t)=\int_0^\infty f(x)x^{it}\frac{dx}x$, also $\overline{h(t)}=\int_0^\infty\overline{f(x)}x^{-it}\frac{dx}x$.
Substitution $x\mapsto x^{-1}$: $\overline{h(t)}=\int_0^\infty\overline{f(x^{-1})}x^{it}\frac{dx}x=h(-t)$ gdw. $f$ reell.
*(L2):* $\mathcal{M}_\infty(f^\sharp)(t)=\int_0^\infty\overline{f(x^{-1})}x^{it}\frac{dx}x=\overline{h(t)}$.
Also $f^\sharp=f\iff h(t)\in\mathbb R$.
*(L3):* $\mathcal{M}_\infty(Jf)(t)=h(-t)$. Also $Jf=f\iff h(-t)=h(t)$. $\square$

**Korrekturnote:** Eine frühere Identifikation von $f^\sharp=f$ mit $h(-t)=\overline{h(t)}$ ist durch (L2) zu revidieren. Der reell-gerade Spektralraum entspricht $f^\sharp=f$ **und** $Jf=f$, also $h(t)\in\mathbb R$ **und** $h(-t)=h(t)$.

**Status PD-3d1: ✓[M]**

---

## 3. PD-3d2 — Realität der Rohform ✓[M]

**Satz PD-3d2:** $h(-t)=\overline{h(t)}\Rightarrow\Lambda_\Gamma^\mathrm{raw}(h):=\frac1{2\pi}\int_{\mathbb R}\gamma_\infty(t)h(t)\,dt\in\mathbb R.$

**Beweis.** Da $\gamma_\infty(-t)=\overline{\gamma_\infty(t)}$ (PD-3c ✓[M]):
$\overline{\Lambda_\Gamma^\mathrm{raw}(h)}=\frac1{2\pi}\int_{\mathbb R}\gamma_\infty(-t)h(-t)\,dt\stackrel{t\mapsto-t}{=}\Lambda_\Gamma^\mathrm{raw}(h).$

Äquivalente Halbgeradenform: $\Lambda_\Gamma^\mathrm{raw}(h)=\frac1\pi\operatorname{Re}\int_0^\infty\gamma_\infty(t)h(t)\,dt.$

**Status PD-3d2: ✓[M]**

---

## 4. PD-3d3 — Äquivalenz der Darstellungen ✓[M]

Sei $h\in\mathcal{S}(\mathbb R,\mathbb R)$ reell und gerade. Definiere:

$$
\gamma_\infty^\mathrm{sym}(t):=\gamma_\infty(t)+\gamma_\infty(-t)=2\operatorname{Re}\gamma_\infty(t)=-\log\pi+\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{it}2\right).
$$

**Satz PD-3d3 (Äquivalenz):** Für reelles gerades $h$:

$$
\boxed{
\frac1{2\pi}\int_{\mathbb R}\gamma_\infty h
= \frac1{4\pi}\int_{\mathbb R}\gamma_\infty^\mathrm{sym}h
= \frac1{2\pi}\int_0^\infty\gamma_\infty^\mathrm{sym}h.
}
$$

**Beweis.** Zerlegung und Substitution $t\mapsto -t$ liefern $\int_{\mathbb R}\gamma_\infty h=\int_0^\infty\gamma_\infty^\mathrm{sym}h$. Da $\gamma_\infty^\mathrm{sym}$ und $h$ gerade: $\int_0^\infty\gamma_\infty^\mathrm{sym}h=\frac12\int_{\mathbb R}\gamma_\infty^\mathrm{sym}h$. Division durch $2\pi$. $\square$

**Korollar (Doppelzählungswarnung):**
$\frac1{2\pi}\int_{\mathbb R}\gamma_\infty^\mathrm{sym}h = 2\cdot\Lambda_\Gamma^\mathrm{raw}(h)$ — um Faktor 2 zu groß.
Korrekte symmetrisierte Formen: $\frac1{4\pi}T_\Gamma^\mathrm{sym}$ auf ganz $\mathbb R$, oder $\frac1{2\pi}\int_0^\infty$.

**Status PD-3d3: ✓[M]**

---

## 5. PD-3d4 — Pol-/Gamma-Separation (rev.2)

**Strukturell (✓[M]):** Die archimedische Gesamtdistribution zerfällt:

$$
\boxed{\Lambda_\mathrm{Arch}(h) = \Lambda_\mathrm{pole}^\mathrm{raw}(h) + \Lambda_\Gamma(h),}
$$

mit

$$
\Lambda_\mathrm{pole}^\mathrm{raw}(h)
= \frac1{2\pi}\int_{\mathbb R}p_\infty^\mathrm{raw}(t)h(t)\,dt,
\qquad
p_\infty^\mathrm{raw}(t)=-\frac{2it}{\frac14+t^2}.
$$

**Negativer Kandidat (✓[M]_neg):**

$$
\boxed{[O\text{-}220\text{-}1\text{-PD3d4-pole-formula-v0}]\quad\checkmark[M]_\mathrm{neg}.}
$$

Die Formel $p_\infty(t)=(\tfrac14+t^2)^{-1}$ aus rev.1 ist algebraisch falsch als Polterm der logarithmischen Ableitung $\partial_s\log(s(s-1))$. Die positive Lorentz-Funktion gehört zur reflektierten Kombination $\frac1s+\frac1{1-s}$, nicht zu $\partial_s\log(s(s-1))=\frac1s+\frac1{s-1}$.

**Offener Knoten:**

$$
\boxed{[O\text{-}220\text{-}1\text{-PD3d4-pole-functional}]\quad?[O].}
$$

Die genaue Übertragung von $\Lambda_\mathrm{pole}^\mathrm{raw}$ in die endgültige Weil-Testfunktionsform ist offen. Insbesondere: für reelles gerades $h$ verschwindet $\Lambda_\mathrm{pole}^\mathrm{raw}(h)=0$; die Pol-Distribution wird nur auf dem hermiteschen Unterraum sichtbar. Frage: Wie erscheint dieser Term in der vollständigen Weil-Explizitformel?

**Status PD-3d4:** ✓[M] (Trennungsstruktur) / ✓[M]_neg (falscher Kandidat) / `[O-220-1-PD3d4-pole-functional]` ?[O]

---

## 6. PD-3d5 — Autoritative Konvention ✓[K/M]

**Definition (autoritative Gamma-Rohform):**

$$
\boxed{
\Lambda_\Gamma(h):=\frac1{2\pi}\int_{\mathbb R}\gamma_\infty(t)h(t)\,dt,
\qquad h\in\mathcal{S}_\mathrm{herm}(\mathbb R):=\{h\in\mathcal{S}(\mathbb R):h(-t)=\overline{h(t)}\}.
}
$$

**Begründung:** Folgt unmittelbar aus dem Konturintegral (NEU-29); $D_\infty(s)$ ist roh holomorph ohne a-priori-Symmetrisierung (NEU-47); Faktor $1/(2\pi)$ kanonisch sichtbar; symmetrisierte Form als bewiesene Einschränkung.

**Korollar:** Für $h\in\mathcal{S}(\mathbb R,\mathbb R)$ reell und gerade:
$\Lambda_\Gamma(h)=\frac1{4\pi}\int_{\mathbb R}\gamma_\infty^\mathrm{sym}h=\frac1{2\pi}\int_0^\infty\gamma_\infty^\mathrm{sym}h.$

**Status PD-3d5: ✓[K/M]**

---

## 7. Statusabschluss

$$
\boxed{[O\text{-}220\text{-}1\text{-PD3d-Weil-normalization}]\quad\checkmark[K/M]}
$$

*Einschränkung:* PD-3d bezeichnet ausschließlich die Gamma-Distribution $\Lambda_\Gamma$. Die vollständige archimedische Form einschließlich des Pol-Funktionals ist durch `[O-220-1-PD3d4-pole-functional]` ?[O] noch nicht geschlossen.

| Unterknoten | Aussage | Status |
|---|---|---|
| PD-3a | $\gamma_\infty(t)=O(\log(2+|t|))$ | ✓[M] |
| PD-3b | $T_\Gamma^\mathrm{raw},T_\Gamma^\mathrm{sym}\in\mathcal{S}'(\mathbb R)$ | ✓[K/M] |
| PD-3c | $\gamma_\infty(-t)=\overline{\gamma_\infty(t)}$ | ✓[M] |
| PD-3d1 | Symmetrielexikon L1–L3 | ✓[M] |
| PD-3d2 | Realität der Rohform | ✓[M] |
| PD-3d3 | Äquivalenz Rohform/sym. Form | ✓[M] |
| PD-3d4 | Trennungsstruktur; Polterm-Formel-v0 negativ | ✓[M] / ✓[M]_neg / ?[O] |
| PD-3d5 | Rohform auf $\mathcal{S}_\mathrm{herm}$ autoritativ | ✓[K/M] |

$$
\boxed{\text{PD-3 (Gamma-Distribution)}\quad\checkmark[K/M].}
$$

---

## 8. Übergabe an PD-4

PD-4 hat zwei Zielfragen:

1. **PD-4a (negativ):** Gewöhnliche Hilbertraumspur von $\gamma_\infty(H_\infty)h(H_\infty)$ existiert nicht.
2. **PD-4b (positiv):** Semifinite Spur $\tau_\infty$ auf $\mathcal{N}_\infty=L^\infty(\mathbb R)$ realisiert $\Lambda_\Gamma$.
3. **PD-4c (offen):** Intrinsischer geometrischer/relativer Ursprung der Digammafunktion.

Ferner: $H_\infty=M_t$ unter $\mathcal{M}_\infty$ erzeugt nicht von selbst $\gamma_\infty^\mathrm{sym}(t)$. PD-4 benötigt Funktionalkalkül oder relativen Operator.

---

*Rev.2 — 25. Juli 2026 | Kernkorrektur: $p_\infty^\mathrm{raw}(t)=-2it/(\tfrac14+t^2)$, nicht $+(\tfrac14+t^2)^{-1}$*  
*Quellen: NEU-47, NEU-29, NEU-220a–c*
