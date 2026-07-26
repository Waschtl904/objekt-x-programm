# NEU-142 — T2-Label-Audit

> Stand: 9. Juli 2026.  
> Anschluss: NEU-141 (unbeschränkte Mangoldt-Renormierung), NEU-132/133 (H1/H2/H3-rel, Primkantenraum).  
> **Kernfrage:** Sind die Summanden $H_{m\to pm}$ nach der Kante $(m,p)$ gelabelt — oder nur nach Zielindizes?

---

## Leitmotiv

$$\boxed{\text{Primkanten-Labeling gibt T2 formal.}}
\qquad
\boxed{\text{Zielindex-Labeling erzeugt mögliche Kreuzterme.}}$$

T2 ist ab NEU-141 keine kosmetische Vereinfachung mehr, sondern die Voraussetzung dafür, dass $R$ überhaupt primdiagonal definiert werden kann.

---

## 142.0 Aufstellung

Sei $\Psi_p \in W_{\mathrm{res,rel}}$ und sei
$$\bigoplus_{\alpha \in A} H_\alpha$$
eine orthogonale Hilbertsumme. Schreibe
$$\Psi_p = \bigoplus_{\alpha \in A_p} \psi_{p,\alpha}.$$

Dann gilt
$$\langle \Psi_p, \Psi_q \rangle = \sum_{\alpha \in A_p \cap A_q} \langle \psi_{p,\alpha}, \psi_{q,\alpha} \rangle.$$

Also:
$$A_p \cap A_q = \varnothing \quad\Longrightarrow\quad \langle \Psi_p, \Psi_q \rangle = 0.$$

Für T2 ist daher **entscheidend**, ob die Labels $\alpha$ Primkanten oder nur Zustände/Zielindizes bezeichnen.

---

## 142.1 Fall 1 — Primkanten-Labels

Falls
$$A_p = \{(p, m)\},$$
also die Hilbertsumme nach **Primkanten** $(m, p)$ gelabelt ist, dann gilt für $p \neq q$:
$$A_p \cap A_q = \varnothing.$$

Daher
$$\langle \Psi_p, \Psi_q \rangle = 0 \qquad (p \neq q).$$

T2 ist erfüllt. In diesem Fall ist
$$R\Psi_p = R_p \Psi_p$$
**kanonisch primdiagonal definierbar.**

---

## 142.2 Fall 2 — Ziel-/Zustands-Labels

Falls die Hilbertsumme nur nach **Zielindizes** gelabelt ist, etwa
$$A_p = \{pm \in M_p\},$$
dann können für $p \neq q$ Überschneidungen auftreten. Denn
$$pm = qn$$
hat Lösungen
$$m = qr, \qquad n = pr.$$

Also entstehen mögliche gemeinsame Zielindizes $pqr$, und $A_p \cap A_q$ ist im Allgemeinen **nicht leer**. T2 folgt dann nicht formal.

In diesem Fall ist
$$\langle \Psi_p, \Psi_q \rangle = \sum_{\alpha \in A_p \cap A_q} \langle \psi_{p,\alpha}, \psi_{q,\alpha} \rangle,$$
und die Orthogonalität muss durch eine zusätzliche Struktur bewiesen werden.

---

## 142.3 Warum $p \nmid m$ nicht ausreicht

Selbst die Bedingung "$m$ ist $p$-primitiv" verhindert die Kollision mit einem anderen Prim $q$ nicht automatisch. Denn
$$pm = qn \quad \text{mit} \quad m = qr,\; n = pr$$
ist mit $p \nmid m$ und $q \nmid n$ vereinbar, solange $r$ teilerfremd zu $pq$ ist.

$$\boxed{p \nmid m \text{ allein reicht nicht. Man braucht orthogonale Primkantenräume oder eine separate Kreuztermrechnung.}}$$

---

## 142.4 Konsequenz: Zwei Ausgangssituationen

| Labeling | T2-Status | $R$ definierbar als | Schwierigkeit |
|---|---|---|---|
| **Primkanten** $(m,p)$ | \checkmark formal | $R\Psi_p = R_p\Psi_p$ diagonal | gering |
| **Zielindex** $pm \in M_p$ | ❓[O] | Matrixproblem $RG = \Lambda$ | hoch |

Im Zielindex-Fall wird aus $R_p = \dfrac{\log p}{|c_p|^2}$ stattdessen ein Matrixproblem:
$$RG = \Lambda,$$
mit
$$G_{pq} = \langle \Psi_p, \Psi_q \rangle, \qquad \Lambda_{pq} = \delta_{pq} \log p.$$

Das wäre deutlich schwerer und instabiler.

---

## 142.5 Prüfauftrag

$$\boxed{\text{Lies NEU-132/133: Sind die Summanden }H_{m \to pm}\text{ nach der Kante }(m,p)\text{ gelabelt?}}$$

**Falls ja:** $\langle \Psi_p, \Psi_q \rangle = 0$ für $p \neq q$ ist erledigt. Weiter zu NEU-141.B.

**Falls nein:** $G_{pq} := \langle \Psi_p, \Psi_q \rangle$ muss explizit berechnet werden. $R$ ist nicht diagonal, sondern nur über eine Gram-/biorthogonale Renormierung definierbar.

---

## 142.6 Arbeitsplan

| Eintrag | Inhalt | Abhängigkeit |
|---|---|---|
| **NEU-142.A** | Prüfe Label-Struktur in NEU-132/133 | NEU-132, NEU-133 |
| **NEU-142.B** | Falls edge-label: T2 formal schließen | 142.A = Fall 1 |
| **NEU-142.C** | Falls vertex-label: $G_{pq}$ explizit berechnen | 142.A = Fall 2 |
| **NEU-141.B** | $R$ als unbeschränkte primdiagonale Observable | T2 aus 142.B |

---

## Verweise

- **NEU-141**: Unbeschränkte Mangoldt-Renormierung, drei Spurklassen-Ebenen
- **NEU-132**: H1/H2/H3-rel, Analogietabelle PSWF vs. Primkantenraum
- **NEU-133**: Primschalen-Abel-Mechanismus, drei Schlüsselgrößen
- **NEU-44.X**: $P_p = |\Psi_p\rangle\langle\Psi_p|$, $\operatorname{Tr}P_p = |c_p|^2$
