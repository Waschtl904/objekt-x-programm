# NEU-219h — Dilatationspfad: Strukturaudit und DAG-Aufspaltung

**DAG-Position:** Nachfolger von NEU-219g (Commit f4c17e7).  
**Primdaerer offener Knoten:** [O-219-5e1a] — automorphe Dilatation der nichtunitalen $\rho_n$.  
**Gesperrt bis [O-219-5e1a]:** [O-219-5e1b] bis [O-219-5e2].

---

## 1. Konsolidierung der Ladungsobstruktion

Die Ladungsobstruktion tritt konsistent in drei äquivalenten Formen auf:

| Form | Ausdruck |
|------|----------|
| Parazyklische Eigenkomponente | $T_{\sigma_\beta}\Phi = g^{-\beta}\Phi \neq \Phi$ |
| Koinvariantenannihilation | $[\Phi] = 0$ nach gewöhnlicher Zyklisierung |
| SAYD-Stabilität | $c = 1 \neq g^{-\beta}$ (für $g \neq 1$, $\beta > 0$) |

Diese drei Formulierungen sind strukturell äquivalent; die Obstruktion ist keine Theorieartefakt.

**Vorbehalt:** Die SAYD-Argumentation (NEU-219g Abschnitte 6–8) sollte vor externer Verwendung gegen eine fixierte Links-/Rechts-SAYD-Konvention unabhängig geprüft werden. Der Widerspruch scheint konventionsstabil, aber einzelne Exponenten und Antipodenpositionen können sich umkehren.

---

## 2. Warum kein Symbol $u_g$ adjungiert werden darf

Der BC-Kern besitzt nur nichtunitale Endomorphismen:
$$
\rho_n(f) = \mu_n f \mu_n^*, \qquad \rho_n(1) = E_n \neq 1.
$$

Die $\rho_n$ bilden ein Semigruppensystem, keine Gruppe. Ein formal adjungiertes Symbol $u_g$ wäre ohne Konstruktion einer Algebra, in der es wirklich als Implementierer einer Automorphie wirkt, mathematisch leer — nicht stärker als die bereits ausgeschlossene externe Eigenlinie aus NEU-219e.

$$
\boxed{
\text{Ein bloues Symbol }u_g\text{ ohne Dilatationskonstruktion ist keine Reparatur.}
}
$$

---

## 3. [O-219-5e1a]: Automorphe Dilatation der $\rho_n$-Dynamik

**Status: ?[O] primär**

Gefordert ist ein Quadrupel $(\widetilde{B}, \gamma, \iota, e)$ mit:

1. **Automorphismengruppe:** $\gamma: \mathbb{Q}_+^\times \longrightarrow \operatorname{Aut}(\widetilde{B})$, d.h. $\gamma_{rs} = \gamma_r \circ \gamma_s$, jedes $\gamma_r$ ein echter unitärer Algebraauto­morphismus.

2. **Einbettung:** $\iota: B_{\mathrm{alg}} \hookrightarrow e\widetilde{B}e$ mit einem Eckprojektor $e = e^* = e^2 \in \widetilde{B}$.

3. **Kompressions­formel:**
$$
\boxed{\iota(\rho_n(f)) = e\,\gamma_n(\iota(f))\,e} \tag{3.1}
$$
mit präziser Behandlung des Rangeprojektors $E_n$: Da $\rho_n(1) = E_n \neq 1$, muss die Formel erklären, wie $e\gamma_n(e)e$ sich zu $\iota(E_n)$ verhält.

4. **Kein Raten:** Orientierung und Eckprojektionspositionen müssen aus der konkreten Dilatation folgen, nicht postuliert werden.

Hintergrund: Nichtunitale Endomorphismensysteme auf $C^*$-Algebren besitzen unter Bedingungen (z.B. endlicher Index, vollständige Positivität) kanonische minimale Dilationen zu Gruppenwirkungen; das entsprechende Standardresultat für Semigruppen von Endomorphismen ist in der $C^*$-Theorie bekannt (Frahm–Neeb-Typ, Stacey-Typ). Für den BC-Kern $B_{\mathrm{alg}} \subset A_{C^*}$ muss geprüft werden, ob die $\rho_n$ die erforderlichen Voraussetzungen erfüllen.

$$\boxed{ [O\text{-}219\text{-}5e1a]: \quad \text{Automorphe Dilatation }(\widetilde{B}, \gamma, \iota, e)\text{ der }\rho_n\text{-Dynamik} \quad ?[O]. }$$

---

## 4. [O-219-5e1b]: Crossed-Product $\widetilde{A} = \widetilde{B} \rtimes_\gamma \mathbb{Q}_+^\times$

**Status: gesperrt durch [O-219-5e1a]**

Nach erfolgreicher Dilatation wäre das Crossed-Product mit invertierbaren Implementierern $U_r$ definierbar:
$$
U_r U_s = U_{rs}, \qquad U_r b U_r^* = \gamma_r(b).
$$

Erst dann existiert ein mathematisch echter Kandidat für einen Ladungsträger $U_g \in \widetilde{A}$.

$$\boxed{ [O\text{-}219\text{-}5e1b]: \quad \widetilde{B} \rtimes_\gamma \mathbb{Q}_+^\times \text{ und Implementierer }U_r \quad \text{gesperrt.} }$$

---

## 5. [O-219-5e1c]: Grad und Modulargewicht von $U_r$

**Status: gesperrt durch [O-219-5e1b]**

In $\widetilde{A}$ sind zwei Eigenschaften von $U_r$ streng zu trennen:

- **Modulargewicht:** $\widetilde{\sigma}_\beta(U_r) = r^\beta U_r$ (aus der analytischen Fortsetzung der Zeitwirkung auf $\widetilde{A}$, sofern diese existiert).
- **Algebraischer Grad:** $\deg(U_r) = ?$ (aus der $\mathbb{Q}_+^\times$-Gradierung von $\widetilde{A}$, sofern vorhanden).

Für die Zyklizitätsreparatur wird der Eigenwert $g^\beta$ benötigt (um $T\Phi = g^{-\beta}\Phi$ zu kompensieren). Für eine algebraische Neutralisierung muss zugleich geprüft werden, ob Multiplikation mit $U_g$ oder $U_{g^{-1}}$ den Gesamtgrad tatsächlich neutral macht. **Diese beiden Anforderungen können entgegengesetzte Orientierungen verlangen.**

Daher: Erst wenn $\deg(U_r)$ und $\widetilde{\sigma}_\beta(U_r)$ exakt bestimmt sind, darf $\widetilde{\Phi} = U_r \cdot \Phi$ für den eindeutig ermittelten Wert $r$ definiert werden.

$$\boxed{ [O\text{-}219\text{-}5e1c]: \quad \text{Bestimme exakt }\deg(U_r)\text{ und }\widetilde{\sigma}_\beta(U_r) \quad \text{gesperrt.} }$$

---

## 6. [O-219-5e1d]: Lift des Koeffizientenmoduls $M$

**Status: gesperrt durch [O-219-5e1b]**

Die Erweiterung der Algebra allein genügt nicht. Benötigt wird ein $\widetilde{A}$-Bimodul $\widetilde{M}$ und eine typkorrekte Einbettung:
$$
j_M: \mathfrak{M}^{\log}_{\mathrm{glob}} \longrightarrow \widetilde{M}.
$$

Zu prüfen:
$$
j_M(amb) = j_A(a)\,j_M(m)\,j_A(b), \qquad
\widetilde{\sigma}_\beta(j_M(m)) = j_M(\sigma_\beta(m)).
$$

Außerdem: Existenz eines gelifteten Kozykels
$$
\widetilde{L} \in Z^4(\widetilde{A}, \widetilde{M}).
$$

Ein bloßes Einbetten von $A_{\mathrm{alg}}$ in eine größere Algebra garantiert nicht, dass die ursprüngliche Hochschildklasse nichttrivial bleibt. **Restriktion und Induktion der Klasse müssen separat auditiert werden.**

$$\boxed{ [O\text{-}219\text{-}5e1d]: \quad \text{Lift des Koeffizientenmoduls }\mathfrak{M}^{\log}_{\mathrm{glob}}\text{ auf }\widetilde{M} \quad \text{gesperrt.} }$$

---

## 7. [O-219-5e1e] und [O-219-5e2]: Kozykel und Zyklizität

**Status: gesperrt**

$$\boxed{ [O\text{-}219\text{-}5e1e]: \quad \text{Gelifteter und neutralisierter Grad-4-Kozykel} \quad \text{gesperrt.} }$$

$$\boxed{ [O\text{-}219\text{-}5e2]: \quad \text{Zyklischer Rand, Rotation und Nichtverschwindenspaarung} \quad \text{gesperrt.} }$$

---

## 8. Revidierter DAG

| Knoten | Inhalt | Status |
|--------|--------|--------|
| **[O-219-5e1a]** | Automorphe Dilatation $(\widetilde{B},\gamma,\iota,e)$ der $\rho_n$ | **?[O] primär** |
| [O-219-5e1b] | $\widetilde{B} \rtimes_\gamma \mathbb{Q}_+^\times$, Implementierer $U_r$ | gesperrt |
| [O-219-5e1c] | $\deg(U_r)$, $\widetilde{\sigma}_\beta(U_r)$ | gesperrt |
| [O-219-5e1d] | Lift $j_M: M \to \widetilde{M}$, Kozykel $\widetilde{L}$ | gesperrt |
| [O-219-5e1e] | Gelifteter neutralisierter Grad-4-Kozykel | gesperrt |
| [O-219-5e2] | Zyklischer Rand, Rotation, Paarung | gesperrt |

```
[O-219-5e1a]  automorphe Dilatation (B-tilde, gamma, iota, e)   ?[O] PRIMAER
      |
      +-- Kompressionsformel: iota(rho_n(f)) = e*gamma_n(iota(f))*e
      +-- Behandlung Rangeprojektor E_n != 1
      +-- Dilatationstyp: Stacey / Frahm-Neeb / BC-spezifisch
      |
[O-219-5e1b]  B-tilde x|_gamma Q+^x, U_r U_s = U_{rs}          gesperrt
      |
[O-219-5e1c]  deg(U_r) und sigma-tilde_beta(U_r)                gesperrt
      |
[O-219-5e1d]  j_M: M -> M-tilde, Lift L-tilde in Z^4           gesperrt
      |
[O-219-5e1e]  U_r * Phi: neutralisierter Grad-4-Kozykel         gesperrt
      |
[O-219-5e2]   zyklischer Rand, lambda, Nichtverschwindenspaarung gesperrt
```

---

## 9. Primaerer naechster Schritt

$$
\boxed{
\text{Konstruiere oder finde die minimale automorphe Dilatation
der nichtunitalen BC-Endomorphismen }\rho_n.
}
$$

Drei Kandidatenansätze für [O-219-5e1a], die zu prüfen sind:

1. **Stacey-Dilation:** Für Semigruppen isometrischer Endomorphismen auf Hilberträumen existiert eine minimale unitäre Dilatation; Übertragung auf den algebraischen BC-Kern unklar.
2. **BC-spezifische Konstruktion:** Die Cuntz-Algebra $\mathcal{O}_\infty$ oder eine verwandte universelle Algebra könnte $\widetilde{B}$ liefern, in der die $\mu_n$ als Isometrien sitzen und $\gamma_r$ als echte Automorphismen wirken.
3. **Gruppenalgebra-Vervollständigung:** Symmetrisierung des Semigruppensystems $\{\rho_n\}$ durch formale Inversengruppe; Typ und Universalität zu definieren.

Die Wahl des Dilatationstyps bestimmt die Gestalt der Kompressionsformel (3.1) und damit alle nachgelagerten Knoten.
