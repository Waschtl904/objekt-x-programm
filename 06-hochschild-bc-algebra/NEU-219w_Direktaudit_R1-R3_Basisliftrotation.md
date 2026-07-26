# NEU-219w — Direktaudit (R1)–(R3): Basisliftrotation

**Datei:** `katalog/NEU-219w_Direktaudit_R1-R3_Basisliftrotation.md`  
**Knoten:** `[O-219-5e1i-R1R3-base-rotation]`  
**Status:** `✓[M]_{\mathrm{neg,Quelle}}`  
**DAG-Position:** Nachfolger von NEU-219v (Commit 959a165).  
**Datum:** 2026-07-24 (revidiert)

---

## 0. Eingangtatsachen (bereits bewiesen, unverändert gültig)

Für den kanonischen Basislift gilt wortgetreu (NEU-219r):
$$
\widetilde L_0 = \eta_0 \circ j_M \circ L^{\mathrm{cup}}, \qquad \widetilde L_0(A_{\mathrm{alg}}^{\otimes 4}) \subseteq I_0.
$$

Daraus folgt **definitionsgemäß**:
$$
\boxed{\kappa = 0, \qquad \varepsilon = 0, \qquad \widehat{\Omega}_\lambda \circ \widetilde{L}_0 \text{ ist } \lambda\text{-unabhängig.}}
$$

Diese drei Tatsachen bleiben von der folgenden Revision **unberührt**.

---

## 1. Prüfgrößen

$$
x_{0123} := j_M\!\left(L^{\mathrm{cup}}(a_0,a_1,a_2,a_3)\right), \qquad
x_{1234} := j_M\!\left(L^{\mathrm{cup}}(a_1,a_2,a_3,a_4)\right).
$$

Die Prüfaufgabe:
$$
\boxed{\text{Liefern (R1)–(R3) eine Relation zwischen }\; x_{0123}\,\tau^{-1}(j_A(a_4)) \;\text{ und }\; x_{1234}\,\tau^{-1}(j_A(a_0))?}
$$

---

## 2. Ergebnis des Direktaudits: (R1)–(R3) reichen nicht

Der in NEU-219s vorgelegte "Beweis" von $s=-1$ wurde geprüft und **zurückgerollt**. Die drei zitierten Regeln lauten:

- **(R1)** KMS-Zyklizität: $\widetilde\omega(AB) = \widetilde\omega(\widetilde\sigma_\beta(B)A)$
- **(R2)** Twistkommutation: $U_{g^{-1}}\tau(a) = \widetilde\sigma_\beta(a)U_{g^{-1}}$
- **(R3)** Grad-$g$-Eigenschaft von $L^{\mathrm{cup}}$

### 2.1 (R1) ändert nicht die Argumente von $L^{\mathrm{cup}}$

Die KMS-Relation permutiert lediglich Faktoren innerhalb des Arguments von $\widetilde\omega$. Sie liefert **keine** Beziehung zwischen $L^{\mathrm{cup}}(a_0,a_1,a_2,a_3)$ und $L^{\mathrm{cup}}(a_1,a_2,a_3,a_4)$ — genau dieser Austausch ist aber der Kern der gesuchten Rotation.

### 2.2 Schritt 2 in NEU-219s ist keine gültige Anwendung von (R1)

Aus $\widetilde\omega(U_{g^{-1}}\,j_A(a_4)\,x_{0123})$ folgt durch KMS mit $A = U_{g^{-1}}$, $B = j_A(a_4)x_{0123}$ korrekt:
$$
\widetilde\omega\!\left(\widetilde\sigma_\beta(j_A(a_4))\,\widetilde\sigma_\beta(x_{0123})\,U_{g^{-1}}\right),
$$
nicht die in NEU-219s behauptete Form, die $x_{0123}$ unverändert stehen lässt. NEU-219s verschiebt nur $j_A(a_4)$, obwohl KMS auf den **gesamten** rechten Block wirkt — eine substanzielle Lücke.

### 2.3 (R2) ist keine Rotationsrelation

Die Vertauschung $U_{g^{-1}}\tau(a) = \widetilde\sigma_\beta(a)U_{g^{-1}}$ liefert keine Relation $x_{0123}\tau^{-1}(j_A(a_4)) \leftrightarrow x_{1234}\tau^{-1}(j_A(a_0))$. Sie verändert weder die vier Eingaben des Kozykelwerts noch erzeugt sie den fehlenden Wert $x_{1234}$.

### 2.4 (R3) ist als "Grad-$g$-Eigenschaft" unbegründet

Die behauptete Äquivarianzformel $L^{\mathrm{cup}}(g\cdot a_1,\ldots) = g\cdot L^{\mathrm{cup}}(a_1,\ldots)$ folgt nicht allein aus dem $\Gamma$-Grad von $L^{\mathrm{cup}}$. Die Grad-Eigenschaft bedeutet lediglich $a_i \in (A_{\mathrm{alg}})_{h_i} \Rightarrow L^{\mathrm{cup}}(a_1,\ldots,a_4) \in M_{gh_1h_2h_3h_4}$ — eine Aussage über den Grad des Ausgangs, keine Operationsformel. (R3) ist damit mindestens unbegründet, möglicherweise untypisiert.

### 2.5 Der entscheidende Übergang fehlt vollständig

Selbst unter großzügiger Annahme von (R1)–(R3) enthält keine der Regeln einen Mechanismus, der $x_{0123}$ in $x_{1234}$ überführt. Die Formulierung in NEU-219s „Nach vollständiger Anwendung aller Rotationsschritte …“ ist **keine Ableitung**, sondern bezeichnet genau den fehlenden Beweisschritt.

---

## 3. Revidierte Entscheidung

$$
\boxed{[O\text{-}219\text{-}5e1i\text{-R1R3-base-rotation}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}.}
$$

Genauer:
$$
\boxed{\text{(R1)–(R3) liefern weder eine Identität in } N_0 \text{ noch eine bewiesene Paarungsidentität.}}
$$

**Wichtig:** Dies widerlegt nicht die globale Rotationsidentität selbst. Ausgeschlossen ist nur der in NEU-219s behauptete Beweisweg aus den drei Regeln. Auch $s = -1$ bleibt **unbewiesen** (nicht widerlegt, nur nicht hergeleitet).

Der übergeordnete Knoten bleibt daher offen:
$$
[O\text{-}219\text{-}5e1i\text{-typed-global-rotation-audit}] \quad ?[O].
$$

---

## 4. Entscheidungsgabel (Referenz)

| Fall | Befund | Zutreffend? |
|------|--------|-------------|
| (A) | Vollständige typkorrekte Identität bereits in $N_0$ | Nein |
| (B) | Identität nur modulo Hochschild-Rand | Nicht geprüft — nicht der Fund |
| (C) | Identität erst nach Anwendung von $\varpi_{\beta,\chi}$ | **Nein** — auch das ist nicht bewiesen |
| **(D)** | (R1)–(R3) enthalten die benötigte Relation nicht | **Zutreffend** — $\checkmark[M]_{\mathrm{neg,Quelle}}$ |

---

## 5. Nächster atomarer Knoten

$$
\boxed{[O\text{-}219\text{-}5e1j\text{-explicit-cup-rotation}]}
$$

Ausgehend von der expliziten Formel $L^{\mathrm{cup}} = D_g \smile \Theta^\wedge$ sind beide Werte vollständig zu expandieren:
$$
L^{\mathrm{cup}}(a_0,a_1,a_2,a_3), \qquad L^{\mathrm{cup}}(a_1,a_2,a_3,a_4).
$$

**Frage:**
$$
\boxed{\text{Erzeugt die explizite antisymmetrisierte Cup-Formel nach KMS-Paarung eine Rotationsrelation, oder entstehen unabhängige Restterme?}}
$$

Erst dieser Direktaudit kann Fall (C) tatsächlich beweisen oder endgültig ausschließen.

---

## 6. DAG-Status

| Knoten | Status |
|--------|--------|
| `5e1h1-scalar-rotation` | ✓[M] (NEU-219o–q) |
| $\kappa = 0$ für kanonischen Basislift | ✓[M] (NEU-219r) |
| $\varepsilon = 0$, $\lambda$-Unabhängigkeit | ✓[M] |
| `5e1i-candidate-v0` (typwidrige U-Eingaberotation) | ✓[M]$_{\mathrm{neg}}$ (NEU-219v) |
| `5e1i-R1R3-base-rotation` | **✓[M]$_{\mathrm{neg,Quelle}}$** (dieser Knoten) |
| NEU-219s, Schritte 2–4 (Rotationsbeweis) | **zurückgerollt** |
| $s = -1$ | unbewiesen (nicht widerlegt) |
| `5e1i-typed-global-rotation-audit` (Elternknoten) | ?[O] weiterhin offen |
| `5e1j-explicit-cup-rotation` | **?[O] nächster primärer Knoten** |
