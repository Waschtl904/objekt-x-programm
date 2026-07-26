# NEU-219e — Direktaudit der geladenen modularen Koeffizientenlinie

**DAG-Position:** Nachfolger von NEU-219d (Commit 88863eb).  
**Abgeschlossen:** [O-219-5c1a] ✓[K]; [O-219-5c1b] ✓[M]$_{\mathrm{neg}}$.  
**Offen:** [O-219-5c1c] Entscheidung zwischen drei Reparaturpfaden.

---

## 1. Ausgangspunkt

Vorliegt ein nichtverschwindender skalarer getwisteter Hochschildkozykel mit
$$
b^{\sigma_\beta}\Phi_{\beta,\chi}=0,
\qquad
T_{\sigma_\beta}\Phi_{\beta,\chi} = g^{-\beta}\Phi_{\beta,\chi} \neq \Phi_{\beta,\chi}.
$$

Der vorgeschlagene Reparaturansatz: eine Linie $E_{g,\beta} = \mathbb{C}\,\mathbf{e}_{g,\beta}$ mit $\sigma_\beta(\mathbf{e}_{g,\beta}) = g^\beta \mathbf{e}_{g,\beta}$ einführen. Zwei Interpretationen sind strikt zu trennen.

---

## 2. Interpretation A: Externe modulare $\mathbb{Z}$-Eigenlinie

**Status:** ✓[K]

Als Darstellung der von $\sigma_\beta$ erzeugten Gruppe:
$$
E_{g,\beta} := \mathbb{C}\,\mathbf{e}_{g,\beta},
\qquad
\sigma_\beta^k(\mathbf{e}_{g,\beta}) = g^{k\beta}\mathbf{e}_{g,\beta}.
$$

Für $\Psi_{\beta,\chi} := \mathbf{e}_{g,\beta} \otimes \Phi_{\beta,\chi}$ gilt formal:
$$
(S_{g,\beta} \otimes T_{\sigma_\beta})\Psi_{\beta,\chi}
= g^\beta \mathbf{e}_{g,\beta} \otimes g^{-\beta}\Phi_{\beta,\chi}
= \Psi_{\beta,\chi}.
$$

Die Gesamt-$T$-Obstruktion ist formal kompensiert.

$$\boxed{ [O\text{-}219\text{-}5c1a]: \quad E_{g,\beta} \text{ als externe modulare Eigenlinie} \quad \checkmark[K]. }$$

Dies ist jedoch noch **keine** zyklische Koeffiziententheorie.

---

## 3. Warum $T$-Invarianz nicht genügt

Aus $T_{\mathrm{tot}}\Psi = \Psi$ folgt **nicht** $\lambda_{\mathrm{tot}}\Psi = \Psi$. Die Relation $\lambda^{n+1} = T$ liefert nur die notwendige Bedingung $\lambda\Psi = \Psi \Rightarrow T\Psi = \Psi$; die Umkehrung gilt nicht. Selbst bei $T\Psi = \Psi$ kann $\Psi$ in einem beliebigen nichttrivialen $(n+1)$-ten Einheitswurzel-Eigenraum von $\lambda$ liegen.

Zusätzlich fehlen durch die bloge Angabe $S(\mathbf{e}) = g^\beta \mathbf{e}$:
- gradweise Operatoren $\delta_i^E$, $\sigma_i^E$, $\lambda_n^E$
- Koflächen und Kodegenerationen
- Kompatibilität mit $b^{\sigma_\beta}$
- die parazyklische Identität $\lambda_{E,n}^{n+1} = T_{E,n}$

$$
\boxed{
\text{„Eigenlinie} + T\text{-Kompensation} \Rightarrow \text{zyklischer Kozykel“}
\quad \checkmark[M]_{\mathrm{neg}}.
}
$$

---

## 4. Interpretation B: Unitales $\sigma_\beta$-äquivariantes $A$-Bimodul

**Status:** ✓[M]$_{\mathrm{neg}}$

Sei $E_{g,\beta}$ eine echte eindimensionale unital-nichtdegenerierte Koeffizientenlinie über $A := A_{\mathrm{alg}}$ mit Charakteren $\chi_L, \chi_R: A \to \mathbb{C}$ und $\sigma_\beta$-äquivarianter Abbildung $S(\mathbf{e}) = g^\beta \mathbf{e}$.

Die linke Modulkompatibilität $S(a \cdot \mathbf{e}) = \sigma_\beta(a) \cdot S(\mathbf{e})$ liefert:
$$
\chi_L(a)\,g^\beta\,\mathbf{e} = \chi_L(\sigma_\beta(a))\,g^\beta\,\mathbf{e},
$$
also:
$$
\boxed{\chi_L \circ \sigma_\beta = \chi_L.} \tag{4.2}
$$

Analog $\chi_R \circ \sigma_\beta = \chi_R$.

### Ausschluss über BC-Isometrien

Für jedes $k \ge 2$ gilt $\mu_k^* \mu_k = 1$, also $\chi_L(\mu_k) \neq 0$. Der modulare Twist erfüllt $\sigma_\beta(\mu_k) = k^\beta \mu_k$. Mit (4.2):
$$
\chi_L(\mu_k) = \chi_L(\sigma_\beta(\mu_k)) = \chi_L(k^\beta \mu_k) = k^\beta \chi_L(\mu_k).
$$

Wegen $\chi_L(\mu_k) \neq 0$ muss $k^\beta = 1$ gelten — für $k \ge 2$, $\beta > 0$ ist dies unmöglich.

$$
\boxed{
[O\text{-}219\text{-}5c1b]:\quad
\text{unitales }\sigma_\beta\text{-äquivariantes }A_{\mathrm{alg}}\text{-Bimodul der Dimension 1}
\quad \checkmark[M]_{\mathrm{neg}}.
}
$$

Der Ausschluss gilt unabhängig vom Eigenwert $g^\beta$ und sogar unabhängig von $g$: Für $\beta > 0$ existiert überhaupt keine eindimensionale unital-nichtdegenerierte $\sigma_\beta$-äquivariante $A_{\mathrm{alg}}$-Modullinie.

---

## 5. Vorhandene Eigenvektoren lösen das Problem nicht

Für $g = m/n$ ist $v_g := \mu_m \mu_n^*$ homogen vom Grad $g$ mit $\sigma_\beta(v_g) = g^\beta v_g$. Aber:
$$
A \cdot v_g \not\subseteq \mathbb{C}v_g,
\qquad
v_g \cdot A \not\subseteq \mathbb{C}v_g.
$$

Für nichtkonstantes $f \in B_{\mathrm{alg}}$ gilt $f \cdot v_g = \mu_m \sigma_m(f) \mu_n^*$, was im Allgemeinen kein skalares Vielfaches von $v_g$ ist. Somit ist $\mathbb{C}v_g$ kein $A$-Bimodul und keine zyklische Koeffizientenlinie.

---

## 6. Revidierter Status von [O-219-5c1]

$$\boxed{ [O\text{-}219\text{-}5c1a]: \quad \text{externe modulare }\mathbb{Z}\text{-Eigenlinie} \quad \checkmark[K]. }$$

$$\boxed{ [O\text{-}219\text{-}5c1b]: \quad \text{unitales }\sigma_\beta\text{-äquivariantes }A\text{-Bimodul der Dimension 1} \quad \checkmark[M]_{\mathrm{neg}}. }$$

$$\boxed{ [O\text{-}219\text{-}5c1c]: \quad \text{vollständiges para-/zyklisches Koeffizientenobjekt} \quad ?[O]. }$$

---

## 7. Konsequenzen für nachgelagerte Knoten

**[O-219-5c2]** — Parazyklischer Operator: Die einzelne Formel $S(\mathbf{e}) = g^\beta \mathbf{e}$ liefert keine gradweise Familie $\delta_i^E$, $\sigma_i^E$, $\lambda_n^E$ mit allen parazyklischen Identitäten.
$$\boxed{ [O\text{-}219\text{-}5c2] \quad ?[O]. }$$

**[O-219-5c3]** — Der bereits bewiesene Rand $b^{\sigma_\beta}\Phi = 0$ bleibt gültig. Für ein neues Koeffizientenobjekt muss jedoch separat gezeigt werden, dass der totale Rand auf $E_\bullet \otimes \Phi$ verschwindet.
$$\boxed{ [O\text{-}219\text{-}5c3] \quad \text{gesperrt durch [O-219-5c1c/2]. (Kein math. Negativbefund.)} }$$

**[O-219-5c4]** — Gesperrt, solange $\lambda_{\mathrm{tot}}$ nicht definiert ist.
$$\boxed{ [O\text{-}219\text{-}5c4] \quad \text{gesperrt durch [O-219-5c2].} }$$

---

## 8. Drei Reparaturpfade für [O-219-5c1c]

### Pfad I: Geladener parazyklischer Gewichtsektor

Man akzeptiert $T_{\sigma_\beta}\Phi = g^{-\beta}\Phi$ als intrinsische Ladungsinformation und definiert eine gewichtete parazyklische Kohomologie:
$$
HC^{4,\mathrm{para}}_{\sigma_\beta,g}(A),
$$
deren Kozykel im $g^{-\beta}$-Eigenraum von $T_{\sigma_\beta}$ liegen. **Typologisch kürzester Weg.** Keine zusätzliche Algebraerweiterung erforderlich; neue Modellstruktur zu definieren.

**Status:** ?[O]

### Pfad II: Crossed-Product-Erweiterung

Man vergrößert die Algebra um ein formales invertierbares Symbol $u_g$ mit $\sigma_\beta(u_g) = g^\beta u_g$. Dann könnte $u_g \Phi$ global $T$-invariant werden. Notwendig:
- Eine exakt definierte Automorphismus- oder partielle Automorphismuswirkung $\gamma_g$
- Vollständige Crossed-Product- oder Gruppenvervollständigungsarchitektur
- Typkorrekte Übertragung der BC-Semigruppenstruktur

Zyklische Homologie von Gruppen-Crossed-Products zerfällt natürlicherweise in durch Gruppen- bzw. Konjugationsdaten kontrollierte Komponenten; twisted complexes treten dort als strukturelle Bausteine auf. **Langfristig stärkste Verbindung zur Weil-Architektur.**

**Status:** ?[O]

### Pfad III: Hopf-zyklische Koeffizienten

Die Skalierungswirkung wird als Hopf- bzw. Gruppenalgebrawirkung behandelt. Eine eindimensionale Koeffizientenstruktur benötigt kompatible Modul-/Komoduldaten bzw. ein modulares Paar $(\delta, \sigma)$. Dies ist eine andere Theorie als die bisher verwendete automorphismengetwistete zyklische Kohomologie und darf nicht stillschweigend importiert werden.

**Status:** ?[O]

---

## 9. Gesamturteil

$$
\boxed{ \text{Externe Eigenlinie} \quad \checkmark[K], }
$$

$$
\boxed{ \text{eindimensionale unital-äquivariante }A_{\mathrm{alg}}\text{-Koeffizientenlinie} \quad \checkmark[M]_{\mathrm{neg}}. }
$$

Der unmittelbar nächste konstruktive Knoten:

$$
\boxed{
[O\text{-}219\text{-}5c1c]:\quad
\text{Entscheide zwischen geladenem parazyklischem Gewichtsektor (Pfad I),}
}
$$
$$
\text{Crossed-Product-Erweiterung (Pfad II) und Hopf-zyklischen Koeffizienten (Pfad III).}
$$

Die bloe Gleichung $S(\mathbf{e}) = g^\beta \mathbf{e}$ darf noch nicht als zyklische Koeffizientenstruktur gelten.

---

## 10. Revidierter DAG

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-5c1a] | Externe $\mathbb{Z}$-Eigenlinie | ✓[K] |
| [O-219-5c1b] | Unitales $\sigma_\beta$-äquivariantes $A$-Bimodul dim 1 | ✓[M]$_{\mathrm{neg}}$ |
| **[O-219-5c1c]** | Parazyklisches Koeffizientenobjekt, Pfadentscheidung | **?[O] primär** |
| [O-219-5c2] | Parazyklischer Operator | ?[O] |
| [O-219-5c3] | $b^{\sigma_\beta}\widetilde{\Phi} = 0$ | gesperrt |
| [O-219-5c4] | $\lambda_{\sigma_\beta}\widetilde{\Phi} = \widetilde{\Phi}$ | gesperrt |

```
[O-219-5c1a]  externe Z-Eigenlinie                         [K]
[O-219-5c1b]  unitales A-Bimodul dim 1                     [M]_neg
      |
[O-219-5c1c]  Pfadentscheidung:                            ?[O] PRIMAER
      +-- Pfad I:  geladener parazyklischer Gewichtsektor
      +-- Pfad II: Crossed-Product-Erweiterung
      +-- Pfad III: Hopf-zyklische Koeffizienten
      |
[O-219-5c2]   parazyklischer Operator                      ?[O]
      |
[O-219-5c3]   b^sigma Phi_tilde = 0                        gesperrt
      |
[O-219-5c4]   lambda Phi_tilde = Phi_tilde                 gesperrt
```

**Primärer nächster Audit:** [O-219-5c1c] — Typentscheidung zwischen den drei Reparaturpfaden.
