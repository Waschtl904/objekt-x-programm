# NEU-219v — Negativer Audit: typwidrige U-Eingaberotation ausschließen

**Datei:** `katalog/NEU-219v_neg_U-Eingaberotation_typwidrig.md`  
**Status:** `[O-219-5e1i-candidate-v0] ✓[M]neg`  
**Hauptknoten:** `[O-219-5e1i-typed-global-rotation-audit] ?[O]` — bleibt offen  
**Datum:** 2026-07-24

---

## Kontext

Dieser Audit dokumentiert den Ausschluss eines Beweiskandidaten für die Rotationsidentität

$$
t\,\Phi_0(a_0,\ldots,a_4) = g^{-\beta}\,\Phi_0(a_0,\ldots,a_4).
$$

Der Kandidat versuchte, den Faktor $g^{-\beta}$ durch Einsetzen von $U_{g^{-1}}a_i$ in die Argumente von $\Phi_0$ herzuleiten. Er wird hiermit als typwidrig ausgeschlossen.

Die im O-219-Strang gesicherten Resultate (NEU-219r bis NEU-219u) bleiben unberührt.

---

## Verbindliche Definitionen

### Φ₀

$$
\Phi_0(a_0,\ldots,a_4)
= \widetilde{\omega}_{\beta,\chi}\!\left(
U_{g^{-1}}\,j_A(a_0)\,j_M\!\left(L^{\mathrm{cup}}(a_1,\ldots,a_4)\right)
\right).
$$

Hier sind:
- $\widetilde{\omega}_{\beta,\chi}$ der KMS$_\beta$-Zustand mit Charakter $\chi$,
- $j_A: A_{\mathrm{alg}} \hookrightarrow R$ die Einbettung der algebraischen BC-Algebra in die adelische Kreuzproduktalgebra $R$,
- $j_M: M \hookrightarrow R$ die Einbettung des Koeffizientenmoduls,
- $U_{g^{-1}} \in R$ die Translationsisometrie zum Element $g^{-1} \in \mathbb{Q}^+_\times$,
- $L^{\mathrm{cup}}: A_{\mathrm{alg}}^{\otimes 4} \to M$ der geladene Cup-Kozykel (Typ: $M$-wertig, nicht $A_{\mathrm{alg}}$-wertig).

### Zyklischer Operator t

Für eine skalare 4-Kochaine gilt wegen $(-1)^4 = 1$:

$$
(t\,\Phi_0)(a_0,\ldots,a_4) = \Phi_0(a_4,a_0,a_1,a_2,a_3)
= \widetilde{\omega}_{\beta,\chi}\!\left(
U_{g^{-1}}\,j_A(a_4)\,j_M\!\left(L^{\mathrm{cup}}(a_0,\ldots,a_3)\right)
\right).
$$

---

## Die acht Ausschlussgründe

### F1 — Φ₀-Definition unvollständig

Der Kandidat ersetzte die verbindliche Definition durch

$$
\widetilde{\omega}\!\left(a_0\,\widetilde{L}^{\mathrm{cup}}(a_1,\ldots,a_4)\right),
$$

wobei $U_{g^{-1}}$, $j_A$, $j_M$ sowie die Unterscheidung zwischen $M_0$, $I_0$ und der adelischen Algebra fehlen. Da $\widetilde{L}_0$ zudem $I_0$-wertig ist, darf sein Wert ohne deklarierte Paarungsabbildung nicht als Faktor im Argument von $\widetilde{\omega}$ stehen.

**Urteil:** Das gerechnete Objekt ist nicht $\Phi_0$. ✗

### F2 — Operator t durch falschen Operator ersetzt

Der Kandidat definierte

$$
(t\,\Phi_0)(a_0,\ldots,a_4) := \Phi_0(U_{g^{-1}}a_0,\ldots,U_{g^{-1}}a_4).
$$

Das ist nicht der zyklische Operator $t$. Die Rotationsidentität $(\mathcal{R})$ wurde somit gar nicht untersucht.

**Urteil:** Gegenstand der Rechnung verfehlt. ✗

### F3 — Definitionsbereichsbruch für L̃₀

Es gilt $\widetilde{L}_0: A_{\mathrm{alg}}^{\otimes 4} \to I_0$. Das Element

$$
U_{g^{-1}}\,j_A(a_i) \in R
$$

liegt im Allgemeinen in der adelischen Kreuzproduktalgebra $R$, nicht in $A_{\mathrm{alg}}$. Daher ist der Ausdruck

$$
\widetilde{L}_0(U_{g^{-1}}a_1,\ldots,U_{g^{-1}}a_4)
$$

außerhalb des deklarierten Definitionsbereichs. Der Beweis bricht vor jeder Faktorenrechnung ab.

**Urteil:** Typfehler vor dem ersten Rechenschritt. ✗

### F4 — τ falsch identifiziert

Verbindlich ist

$$
\tau = \operatorname{Ad}(U_g) \circ \widetilde{\sigma}_\beta.
$$

Aus der korrekten Relation $U_{g^{-1}}\tau(a) = \widetilde{\sigma}_\beta(a)\,U_{g^{-1}}$ folgt **nicht**

$$
U_{g^{-1}}\,a = \widetilde{\sigma}_\beta(a)\,U_{g^{-1}},
$$

da $a \neq \tau(a)$ im Allgemeinen. Diese unzulässige Ersetzung wurde für alle $a_i$ verwendet.

**Urteil:** Alle darauf aufbauenden Faktorenrechnungen sind ungültig. ✗

### F5 — Koeffiziententypfehler bei L^cup

Der geladene Cup-Kozykel hat Typ

$$
L^{\mathrm{cup}}: A_{\mathrm{alg}}^{\otimes 4} \longrightarrow M.
$$

Der Kandidat behauptete

$$
L^{\mathrm{cup}}(a_1,\ldots,a_4) \in (A_{\mathrm{alg}})_{h_1 h_2 h_3 h_4 g},
$$

d.h. einen Wert in $A_{\mathrm{alg}}$ statt in $M$. Eine homogene Gradformel müsste als Aussage über die graduierte Komponente des Koeffizientenmoduls $M$ formuliert werden.

**Urteil:** Koeffiziententypfehler. ✗

### F6 — Multilinearität zieht keine Unitaries heraus

Aus Multilinearität folgt ausschließlich das Herausziehen skalarer Faktoren $\in \mathbb{C}$. Die behauptete Formel

$$
L^{\mathrm{cup}}(a_1 U,\ldots,a_4 U) = L^{\mathrm{cup}}(a_1,\ldots,a_4)\cdot U^4 \cdot [\text{Faktoren}]
$$

setzt eine explizit bewiesene Rechtskovarianz in jedem Argument voraus. Ein Hochschild-Kozykel ist weder multiplikativ noch automatisch balanciert bezüglich nachgestellter Kreuzprodukt-Unitaries.

Der Platzhalter $[\text{KMS-Faktoren}]$ im Kandidaten ist keine Rechnung, sondern genau die offene Hauptbehauptung.

**Urteil:** Zirkelschluss. ✗

### F7 — U-Buchführung widersprüchlich

Der Kandidat akkumulierte $U_{g^{-1}}^5 = U_{g^{-5}}$. Skalare Faktoren $h_i^{\pm\beta}$ können Unitaries nicht wegkürzen. Würde man KMS auf $U_{g^{-1}}^5$ anwenden, entstünde

$$
\widetilde{\sigma}_\beta(U_{g^{-1}}^5) = g^{-5\beta}\,U_{g^{-1}}^5,
$$

nicht $g^{-\beta}$. Der Übergang von fünf auf ein $U_{g^{-1}}$ besitzt keine algebraische Begründung.

**Urteil:** Arithmetischer Buchführungsfehler. ✗

### F8 — Letzter KMS-Schritt falsch

Die inverse KMS-Relation liefert

$$
\widetilde{\omega}(X\,U_{g^{-1}})
= \widetilde{\omega}\!\left(\widetilde{\sigma}_\beta(U_{g^{-1}})\,X\right)
= g^{-\beta}\,\widetilde{\omega}(U_{g^{-1}}\,X),
$$

nicht $\widetilde{\omega}(X\,U_{g^{-1}}) = \widetilde{\omega}(U_{g^{-1}}\,X)$. Der nach der Anwendung verbleibende $U_{g^{-1}}$-Faktor gehört zur verbindlichen Definition von $\Phi_0$ und darf nicht entfernt werden.

**Urteil:** KMS-Schlussfehler und Definition verletzt. ✗

---

## Abschlussstatus

$$
\boxed{[O\text{-}219\text{-}5e1i\text{-candidate-v0}] \quad \checkmark[M]_{\mathrm{neg}}}
$$

$$
\boxed{[O\text{-}219\text{-}5e1i\text{-typed-global-rotation-audit}] \quad ?[O]}
$$

Die bereits gesicherten Resultate bleiben unberührt:

| Knoten | Status |
|--------|--------|
| $L^{\mathrm{cup}}_{g;\mathbf{p}} \in Z^4(A_{\mathrm{alg}}, M)_g$ | ✓[M] |
| $\widetilde{L}_0 \in Z^4(A_{\mathrm{alg}}, I_0)$ | ✓[K/M] |
| $\kappa=0$, $\varepsilon=0$, $\lambda$-Unabhängigkeit | ✓[M] |
| Recovery-Identität typkorrigiert | ✓[M] |
| $g \neq 1$, $\beta > 1 \Rightarrow g^{-\beta} \neq 1$ | ✓[M] |
| $[O\text{-}219\text{-}r3]$ abhängig von $(\mathcal{R})$ | bedingt |

---

## Was der nächste Kandidat leisten muss

Die Rechnung darf ausschließlich von den beiden verbindlichen Ausdrücken ausgehen:

$$
\Phi_0(a_0,\ldots,a_4) = \widetilde{\omega}_{\beta,\chi}\!\left(U_{g^{-1}}\,j_A(a_0)\,j_M(L^{\mathrm{cup}}(a_1,\ldots,a_4))\right),
$$

$$
(t\,\Phi_0)(a_0,\ldots,a_4) = \widetilde{\omega}_{\beta,\chi}\!\left(U_{g^{-1}}\,j_A(a_4)\,j_M(L^{\mathrm{cup}}(a_0,\ldots,a_3))\right).
$$

Ein gültiger Beweis benötigt eine **typkorrekte, explizit hergeleitete Identität**, welche

$$
j_A(a_4)\,j_M(L^{\mathrm{cup}}(a_0,\ldots,a_3))
$$

mit

$$
j_A(a_0)\,j_M(L^{\mathrm{cup}}(a_1,\ldots,a_4))
$$

innerhalb von $\widetilde{\omega}_{\beta,\chi}(U_{g^{-1}}\,\cdots)$ verbindet.

Homogenität und KMS allein leisten diese zyklische Umordnung nicht. Vermutlich muss die vollständige Kozykelstruktur von $D_g \smile \Theta^\wedge$ einschließlich der Regeln (R1)–(R3) aus NEU-219s ausgeschrieben werden.

**Nächste Datei:** `katalog/NEU-219w_Direktaudit_R1-R3_Zyklische_Rotation.md`  
**Atomarer Auftrag:** Leiten (R1)–(R3) tatsächlich eine Relation zwischen $j_A(a_4)j_M(L(a_0,\ldots,a_3))$ und $j_A(a_0)j_M(L(a_1,\ldots,a_4))$ her?
