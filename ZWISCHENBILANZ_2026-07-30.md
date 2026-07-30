# Zwischenbilanz — Stand 2026-07-30

**Auditstand:** nach Blöcken 00–05 (vollständig) + 06-hochschild-bc-algebra Block 1 (NEU-174–178)
**Nächster Schritt:** NEU-179 (Transfertriage Geladene Nullkozykel A_Q)

---

## Gesamtübersicht Ordner

| Ordner | Dateien | Status |
|--------|---------|--------|
| 00-grundlegung | 20 | ✅ verifiziert |
| 01-primkanten-werkzeuge | 86 | ✅ verifiziert |
| 02-jacobi-limes | 34 | ✅ verifiziert |
| 03-weil-form-statistik | 31 | ✅ verifiziert |
| 04-grenzoperator-renormierung | 42 | ✅ verifiziert |
| 05-primkanal-fourierladung | 34 | ✅ verifiziert |
| 06-hochschild-bc-algebra | 79 (gesamt) | 🔄 laufend — Block 1 (NEU-174–178) abgeschlossen |
| 07-weil-explizitformel | — | ⚠️ ausstehend |

---

## Auditbericht: NEU-174 bis NEU-178
### Einstieg in Ordner 06-hochschild-bc-algebra

---

### 0. Auditumfang

Vollständig geprüft wurden:

- `NEU-174_Minimaler_Hochschild_Komplex_BC_Zeitwirkung.md`
- `NEU-175_Gewichtraumkomplex_Geladener_Kettenprojektor_BC.md`
- `NEU-176_Konstruktion_Nichttriviale_Geladene_4Kohomologieklasse.md`
- `NEU-177_Direkter_Kozykeltest_Gewichteter_Dualzyklus.md`
- `NEU-178_Vier_Prim_Polynommodell_Geladene_HH4_Klasse.md`

Der Ordner enthält laut aktuellem Repository **79 Dokumente** von NEU-174 bis NEU-222. Der vorliegende Block bildet dessen ersten zusammenhängenden Konstruktionsstrang.

Zur Typprüfung wurde außerdem NEU-72 zurückgelesen. Dort wird $A_{\mathbb Q}$ als komplexe BC-$C^*$-Algebra mit
$$\sigma_t(\mu_n) = n^{it}\mu_n$$
und Generatorgewicht $\log n$ dargestellt.

---

### 1. Gesamturteil

Der Block enthält zwei klar getrennte Ergebnisse.

#### 1.1 Positives Modellergebnis

Für $S_{\mathbf p} = \mathbb C[x_1,x_2,x_3,x_4]$ konstruiert NEU-178 einen expliziten Hochschild-Vierkozykel
$$L_\nu(a_1,a_2,a_3,a_4) = x^\nu \det\bigl(D_i(a_j)\bigr)_{i,j=1}^4, \qquad D_i = x_i\frac{\partial}{\partial x_i},$$
einen passenden dualen Vierzyklus und eine nichtverschwindende Paarung
$$\langle L_\nu, z_{-\lambda_\nu}\rangle = 24.$$

Damit ist
$$[L_\nu] \ne 0 \quad\text{in}\quad HH^4(S_{\mathbf p}, S_{\mathbf p})$$
innerhalb dieses Polynommodells tatsächlich bewiesen.

**Status:** $\boxed{\checkmark[M]}$ relativ zum ausdrücklich definierten Polynommodell, und $\boxed{\checkmark[K/M]}$ als konstruktiver Modellbaustein für das Forschungsprogramm.

#### 1.2 Keine Übertragung auf Objekt (X)

Nicht bewiesen sind:
- $HH^4(A_{\mathbb Q}, A_{\mathbb Q})_{\mathrm{ch}} \ne 0$
- eine Übertragung von $S_{\mathbf p}$ auf die BC-Algebra
- eine Identifikation mit der historischen Klasse $[L_3]$
- eine Operatorrealisierung $\rho_{\mathrm{op}}(L_\nu)$
- eine Verbindung zur ganzzahligen Fourierladung $s$ aus den früheren Primkanalformeln

NEU-178 erklärt die fehlende Transferbrücke selbst ausdrücklich.

**Gesamtstatus des Blocks:** $\boxed{\checkmark[M]_{\mathrm{part}}}$

---

### 2. Interpretationsfreier Primärextrakt

#### 2.1 NEU-174

NEU-174 beginnt ausdrücklich eine neue Konstruktion. Es setzt $B_3 := A_{\mathbb Q}$ und führt zwei Koeffizientenmodelle ein: $M_{\mathrm{untw}} = B_3$ sowie $M_\sigma = {}_{\mathrm{id}}B_{3,\sigma}$.

Danach wird der algebraische Hochschild-Kokettenraum $\operatorname{Hom}(B_3^{\otimes n}, M)$ mit dem üblichen Hochschild-Kodifferential $b$ definiert. Die Datei beansprucht $b^2 = 0$. Anschließend wird aus einer Algebraautomorphismengruppe $\alpha_t$ und einer kompatiblen Modulwirkung $\alpha_t^M$ die Kokettenwirkung gebildet und $b\alpha_t^C = \alpha_t^Cb$ behauptet. Schließlich wird unter einer zusätzlichen Kompaktheitsannahme eine diskrete Fourierzerlegung vorgeschlagen.

#### 2.2 NEU-175

NEU-175 korrigiert drei Punkte:
- $B_3^{\mathrm{mod}} := A_{\mathbb Q}$ ist eine Modellwahl, keine Identifikation mit dem historisch gemeinten $B_3$.
- $M_{\mathrm{untw}}$ ist das reguläre, nicht das symmetrische Bimodul.
- Im verdrehten Fall wird zusätzlich benötigt: $\alpha_t\sigma = \sigma\alpha_t$.

Außerdem erkennt die Datei, dass die BC-Zeit eine $\mathbb R$-Wirkung und keine periodische Kreiswirkung ist. Statt einer vollständigen Fourierreihe definiert sie den algebraischen Eigenkokettenkomplex $\bigoplus_\lambda^{\mathrm{alg}} C_\lambda^n$, wobei $C_\lambda^n = \{\varphi : \alpha_t^C\varphi = e^{it\lambda}\varphi\}$. Auf diesem Raum wird der geladene Projektor $P^{\mathrm{ch}} = \sum_{\lambda\ne 0} P_\lambda$ definiert und $P^{\mathrm{ch}}b = bP^{\mathrm{ch}}$ bewiesen.

#### 2.3 NEU-176

NEU-176 sucht einen geladenen Vierkokettenkandidaten. Die Datei erkennt ausdrücklich, dass weder $bL_{3,\lambda} = 0$ noch $L_{3,\lambda} \notin bC^3_{\mathrm{fin},\lambda}$ aus der Gewichtseigenschaft folgen. Beide Kernpunkte bleiben offen.

#### 2.4 NEU-177

NEU-177 typisiert einen möglichen Nichtrandzeugen durch $\operatorname{Hom}_{\mathbb C}(M, \mathbb C)$ und den Hochschild-Kettenkomplex $M^\vee \otimes (B_3^{\mathrm{mod}})^{\otimes 4}$. Ein Zeuge für einen Kokettenvektor vom Gewicht $\lambda$ muss bei invarianten Paarungen das Gegengewicht $-\lambda$ tragen. NEU-177 konstruiert aber selbst noch keinen konkreten Kozykel oder Zyklus.

#### 2.5 NEU-178

NEU-178 wechselt zu einem eigenständigen Polynommodell $S_{\mathbf p} = \mathbb C[x_1,x_2,x_3,x_4]$ mit Zeitwirkung $e^{it\log p_j}x_j$. Der Vierkozykel $L_\nu(a_1,\ldots,a_4) = x^\nu \det(D_i(a_j))$ trägt Gewicht $\lambda_\nu = \sum_j \nu_j \log p_j \ne 0$. Die Paarung mit dem antisymmetrisierten Dualzyklus ergibt 24, wodurch die Nichttrivialität der Klasse bewiesen wird. Die Datei begrenzt das Resultat ausdrücklich auf dieses Modell.

---

### 3. Dateitabelle

| Datei | Tragfähiger Kern | Hauptproblem | Status |
|-------|-----------------|--------------|--------|
| NEU-174 | Reguläres/verdrehtes Bimodul; $b$; $b^2=0$; induzierte Zeitwirkung | Grundkörper widersprüchlich ($\mathbb Q$ oder $\mathbb R$); Tensorprodukt/Stetigkeit offen; vollständige Fourierzerlegung falsch | $\checkmark[M]_{\mathrm{part}}$ |
| NEU-175 | Algebraischer Eigenkokettenkomplex; $P^{\mathrm{ch}}$; Kommutation mit $b$; Kohomologieabstieg | Nur Teilkomplex; kein historischer $B_3$-Nachweis; „Kettenprojektor" falsch benannt | $\checkmark[M]_{\mathrm{part}}$ |
| NEU-176 | Kozykel- und Nichtrandbedingung korrekt getrennt | Kandidatenformel nicht vollständig getypt; Gewichtsbuchhaltung passt nicht zur Formel | $\warning[M]$ |
| NEU-177 | Dualmodul, Kettenkomplex, Gegengewicht und Nichtrandkriterium korrekt | Kein konkreter Kozykel oder Zyklus auf $A_{\mathbb Q}$; Folgedatei falsch angekündigt | $\checkmark[M]_{\mathrm{part}}$ |
| NEU-178 | Expliziter geladener Vierkozykel, Dualzyklus und Nichttrivialitätsbeweis im Polynommodell | Kein Transfer auf $A_{\mathbb Q}$; keine Operatorrealisierung; falscher Ladungstyp für NEU-169 | $\checkmark[M]$ im Modell, $\checkmark[K/M]$ für Objekt (X) |

---

### 4. Kritische Ladungsunterscheidung

Der Begriff „geladen" bezeichnet in verschiedenen Ordnern verschiedene Strukturen.

**Frühere Fourierladung (Primkanalstrang):** ganzzahliger Index $s \in \mathbb Z$ in Basisvektoren $e_s V_m$; die Rohkopplung benötigt konkret $s\ell_{s,m} \ne 0$.

**BC-Zeitgewicht (NEU-174–178):** reelles Zeitgewicht $\lambda \in \mathbb R$ mit $\alpha_t^C L = e^{it\lambda} L$; im Polynommodell $\lambda_\nu = \sum_j \nu_j \log p_j$.

**Keine vorhandene Identifikation:** Es ist nicht konstruiert $\lambda \ne 0 \Rightarrow s \ne 0$, und es gibt keine Abbildung $C_\lambda^4 \to \operatorname{span}\{e_s V_m\}_{s\ne 0}$. Daher folgt aus NEU-178 nicht $\operatorname{supp}^\times(L_3^\circ) \ne \varnothing$ im Sinne von NEU-169.

**Status:** $\boxed{\checkmark[M]_{\mathrm{neg,Quelle}}}$ — dies ist der wichtigste noch offene Typknoten des Blocks.

---

### 5. Ersetzte und korrigierte Aussagen

**Grundkörper:** Zu streichen: Grundkörper $\mathbb Q$ oder $\mathbb R$. Festzulegen: $\boxed{\text{Grundkörper} = \mathbb C}$.

**Hochschildkomplex:** Zu präzisieren: $\boxed{\operatorname{Hom}_{\mathbb C}(B_3^{\otimes_{\mathrm{alg}} n}, M)}$. Ein kontinuierlicher Komplex wäre ein separates Projekt.

**Fourierzerlegung:** Zu streichen: $\bigoplus_{k\in\mathbb Z} C_k^n$ aus bloßer BC-Zeitwirkung. Korrekt: $\bigoplus_{\lambda\in\mathbb R}^{\mathrm{alg}} C_\lambda^n$ als Teilkomplex der endlichen Summen tatsächlich vorhandener Eigenkoketten.

**Kandidatenformel (NEU-176):** Zu ersetzen durch
$$\varphi(a_1,a_2,a_3,a_4) = \sum_k m_k f_{k,1}(a_1)f_{k,2}(a_2)f_{k,3}(a_3)f_{k,4}(a_4)$$
mit expliziten Typen und Gewichten von $m_k$ und $f_{k,j}$. Auch diese Reparatur garantiert noch nicht $b\varphi = 0$.

**Ergebnis NEU-178:** Korrekt: $HH^4(S_{\mathbf p}, S_{\mathbf p})_{\lambda_\nu} \ne 0$. Nicht korrekt (noch): $HH^4(A_{\mathbb Q}, A_{\mathbb Q})_{\mathrm{ch}} \ne 0$.

---

### 6. Korrigierter Hauptsatz des Blocks

**Satz 174–178 (korr.)** Sei $B$ eine komplexe assoziative Algebra, $M$ ein komplexes $B$-Bimodul, $C^n(B,M) = \operatorname{Hom}_{\mathbb C}(B^{\otimes_{\mathrm{alg}} n}, M)$, $\alpha_t$ eine Algebraautomorphismengruppe und $\alpha_t^M$ eine kompatible Modulwirkung. Dann:

1. $b^2 = 0$.
2. $b\alpha_t^C = \alpha_t^C b$.
3. $\bigoplus_{\lambda\in\mathbb R}^{\mathrm{alg}} C_\lambda^\bullet$ ist ein Unterkomplex.
4. $P^{\mathrm{ch}} = \sum_{\lambda\ne 0} P_\lambda$ kommutiert mit $b$ und steigt auf dessen Kohomologie ab.
5. Für das Polynommodell $S_{\mathbf p} = \mathbb C[x_1,x_2,x_3,x_4]$ existiert für jedes $\nu \ne 0$ eine explizite Klasse $[L_\nu] \ne 0$ in $HH^4(S_{\mathbf p}, S_{\mathbf p})$ mit BC-Zeitgewicht $\lambda_\nu = \sum_j \nu_j \log p_j \ne 0$.

Dieser Satz liefert weder einen Transfer nach $A_{\mathbb Q}$ noch eine Operatorrealisierung oder eine ganzzahlige Fourierladung. **Status:** $\boxed{\checkmark[M]}$

---

### 7. Aktualisierter DAG-Stand (Block NEU-174–178)

| Knoten | Inhalt | Status |
|--------|--------|--------|
| H-174-1 | $B_3^{\mathrm{mod}}$ als komplexe Algebra festgelegt | $\times[M]$ (widersprüchlicher Grundkörper) |
| H-174-2 | $M_{\mathrm{untw}}$ reguläres Bimodul | $\checkmark[M]$ |
| H-174-3 | $M_\sigma$ verdrehtes Bimodul | $\checkmark[M]$ |
| H-174-4 | $b^2 = 0$ | $\checkmark[M]$ |
| H-174-5 | $b\alpha_t^C = \alpha_t^Cb$ | $\checkmark[M]$ unter Modulkompatibilität |
| H-174-σ | $\alpha_t\sigma = \sigma\alpha_t$ | $?[O]$ |
| H-174-top | algebraischer oder kontinuierlicher Komplex | $?[O]$ |
| H-175-1 | $C_{\mathrm{fin}}^\bullet$ algebraischer Gewichtsunterkomplex | $\checkmark[M]$ |
| H-175-2 | $P^{\mathrm{ch}}b = bP^{\mathrm{ch}}$ | $\checkmark[M]$ |
| H-175-3 | $[P^{\mathrm{ch}}]$ auf $H^\bullet(C_{\mathrm{fin}})$ | $\checkmark[M]$ |
| H-175-full | $C_{\mathrm{fin}}^\bullet = C^\bullet$ | $?[O]$ |
| H-176-1 | Kandidatenformel vollständig typisiert | $\times[M]$ |
| H-176-2 | $bL_{3,\lambda} = 0$ auf $A_{\mathbb Q}$ | $?[O]$ |
| H-176-3 | $[L_{3,\lambda}] \ne 0$ auf $A_{\mathbb Q}$ | $?[O]$ |
| H-177-1 | dualer Kettenkomplex und Adjungiertheit | $\checkmark[M]$ |
| H-177-2 | Gegengewichtsbedingung | $\checkmark[M]$ |
| H-178-1 | $[L_\nu] \ne 0$ in $HH^4(S_{\mathbf p}, S_{\mathbf p})$ | $\checkmark[M]$ |
| H-178-2 | $\lambda_\nu \ne 0$ | $\checkmark[M]$ |
| H-178-transfer | $HH^4(S_{\mathbf p}) \to HH^4(A_{\mathbb Q})$ | $?[O]$ |
| H-178-orig | $[L_\nu] = [L_3^{\mathrm{orig}}]$ | $?[O]$ |
| H-178-op | $\rho_{\mathrm{op}}(L_\nu)$ | $\checkmark[M]_{\mathrm{neg,Quelle}}$ |
| H-178-charge | $\lambda_\nu \ne 0 \Rightarrow s \ne 0$ in $e_s V_m$ | $\checkmark[M]_{\mathrm{neg,Quelle}}$ |

---

### 8. Gesamtbeitrag zu Objekt (X)

**Erstmals ein echter Vierkozykelbeweis:** Im Unterschied zu den früheren symbolischen $L_3$-Verwendungen enthält NEU-178 eine vollständig explizite Vierkokette, einen Kozykelbeweis, einen expliziten Dualzyklus, eine nichtverschwindende Paarung und damit einen echten Nichtrandbeweis. Dies ist ein substantieller mathematischer Fortschritt.

**Der Fortschritt ist modellintern:** Das Ergebnis lebt in $\mathbb C[x_1,x_2,x_3,x_4]$, nicht in der BC-Algebra. Es zeigt, dass eine vierdimensionale kommutative Algebra mit logarithmischer Zeitgraduierung geladene $HH^4$-Klassen tragen *kann* — nicht, dass die konkrete BC-Algebra dieselbe Struktur besitzt.

**Noch keine Primkanalbrücke:** NEU-169 benötigt einen Operatorrepräsentanten $L_3^\circ = \sum_{s,m} \ell_{s,m} e_s V_m$ mit $s\ell_{s,m} \ne 0$. NEU-178 liefert dagegen eine multilineare Kokette mit Zeitgewicht $\lambda_\nu$. Zwischen beiden fehlt: Kokette → Operator → Kreis-Fouriergrad.

---

### 9. Nächster Auditblock

Vorrangig zu prüfen (NEU-179–185):

- ob das Vier-Prim-Polynommodell tatsächlich in $A_{\mathbb Q}$ eingebettet werden kann
- ob die Primvaluationsderivationen die BC-Relationen respektieren
- ob ein behaupteter Nullkozykel wegen fehlender Zentralität scheitert
- ob der Augmentationscharakter auf der tatsächlichen BC-Algebra existiert und der vorgeschlagene Dualzyklus wirklich geschlossen ist

**Nächster Einstieg:** NEU-179 (`Transfertriage_Geladene_Nullkozykel_AQ`)
