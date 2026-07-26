# NEU-143 — T2-Abschluss im Edge-Label-Fall

> Stand: 9. Juli 2026.  
> Anschluss: NEU-142 (T2-Label-Audit), NEU-141 (Mangoldt-Renormierung), NEU-132/133 (Primkantenraum).  
> **Kernfrage:** Ist $W_{\mathrm{res,rel}}$ als orthogonale direkte Summe über Kanten $(m,p)$ definiert?

---

## Leitmotiv

$$\boxed{H_{m\to pm} \perp H_{n\to qn} \text{ falls } (m,p) \neq (n,q).}$$

Nicht bloß $pm \neq qn$. Entscheidend ist, ob der Hilbertraum die **Kante** speichert oder nur den Zielknoten.

---

## 143.0 Annahme (Edge-Label-Fall)

$$W_{\mathrm{res,rel}} = \bigoplus_{(m,p)}^{\perp} H_{m\to pm}$$

als orthogonale Hilbertsumme über Primkanten $(m,p)$.

Für jedes Prim $p$ sei
$$\Psi_p \in \bigoplus_m H_{m\to pm}.$$

---

## 143.1 T2-Abschluss

Für $p \neq q$ gilt:
$$\bigoplus_m H_{m\to pm} \perp \bigoplus_n H_{n\to qn}.$$

Folglich
$$\langle \Psi_p, \Psi_q \rangle = 0 \qquad (p \neq q).$$

**T2 ist erfüllt.**

Insbesondere sind die Rang-1-Projektoren
$$P_p := |\Psi_p\rangle\langle\Psi_p|$$
paarweise orthogonal:
$$P_p P_q = 0 \qquad (p \neq q).$$

---

## 143.2 Konsequenz für Spurpotenzen

Für
$$\sum_p \frac{p^{-\beta}}{1-p^{-\beta}} P_p$$
folgt wegen paarweiser Orthogonalität:
$$\operatorname{Tr}\!\left[\left(\sum_p \frac{p^{-\beta}}{1-p^{-\beta}} P_p\right)^k\right] = \sum_p \left(\frac{p^{-\beta}}{1-p^{-\beta}}\right)^k \operatorname{Tr}(P_p^k).$$

Da $P_p = |\Psi_p\rangle\langle\Psi_p|$ gilt $P_p^k = |\Psi_p|^{2(k-1)} P_p$, also
$$\operatorname{Tr}(P_p^k) = |\Psi_p|^{2k}.$$

Daher:
$$\operatorname{Tr}\!\left[\left(\sum_p \frac{p^{-\beta}}{1-p^{-\beta}} P_p\right)^k\right] = \sum_p \left(\frac{p^{-\beta}}{1-p^{-\beta}}\right)^k |\Psi_p|^{2k}.$$

---

## 143.3 Offene Prüffrage an NEU-132/133

$$\boxed{H_{m\to pm} \text{ ist eigener orthogonaler Kantensummand?}}$$

Konkret: Ist in NEU-132/133 wirklich
$$W_{\mathrm{res,rel}} = \bigoplus_{m,p}^{\perp} H_{m\to pm}$$
als orthogonale direkte Summe über Kanten definiert — oder wird $H_{m\to pm} = H_{pm}$ effektiv nur über den **Zielindex** identifiziert?

| Labeling | Status | Konsequenz |
|---|---|---|
| Edge-Label $(m,p)$, orth. direkte Summe | ✅ T2 fertig (143.1) | $R$ primdiagonal definierbar |
| Zielindex $pm$, keine Kantenstruktur | ❓[O] Gram-Problem | $RG = \Lambda$ (Matrixproblem) |

**Wichtig:** Zielkollisionen $pm = qn$ sind möglich (vgl. NEU-142.3), daher reicht die Notation $H_{m\to pm}$ allein nicht. Entscheidend ist, ob eine **orthogonale direkte Summe über Kanten** definiert wurde.

---

## 143.4 Statusdiagnose

$$\boxed{\text{Falls Edge-Label-Annahme bestätigt: T2 abgeschlossen. Weiter zu NEU-141.B.}}$$

$$\boxed{\text{Falls nicht: } G_{pq} = \langle\Psi_p, \Psi_q\rangle \text{ berechnen, dann } RG = \Lambda.}$$

---

## Verweise

- **NEU-142**: T2-Label-Audit, Bifurkation edge vs. vertex
- **NEU-141**: Unbeschränkte Mangoldt-Renormierung, drei Spurklassen-Ebenen
- **NEU-132**: H1/H2/H3-rel, Definition $W_{\mathrm{res,rel}}$
- **NEU-133**: Primschalen-Abel-Mechanismus
- **NEU-44.X**: $P_p = |\Psi_p\rangle\langle\Psi_p|$
