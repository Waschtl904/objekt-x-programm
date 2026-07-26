# NEU-189 — Typaudit der Operatorrealisierung von [Ω_p]

**Status:** Exakte Blockade (kein No-go-Satz)  
**Datum:** 2026-07-19 (Revision 2: 2026-07-19)  
**Vorgänger:** NEU-188 (Erweiterungsobstruktion Derivationen BC)  
**Nachfolger:** NEU-190 (Vollständige Katalogsichtung NEU-1 bis NEU-188)  
**Typ:** Atomarer Prüfknoten

---

## Atomare Ausgangsfrage

Aus welchen bereits konstruierten Daten des RH-Katalogs folgt ein typisierter Mechanismus

$$
Z^4(A,A) \;\text{ oder }\; HH^4(A,A) \longrightarrow \mathcal{O}(\mathcal{H}),
$$

wobei $\mathcal{O}(\mathcal{H})$ zu präzisieren ist als eines der folgenden:
- $B(\mathcal{H})$ (beschränkte Operatoren),
- $\mathrm{End}_{\mathrm{alg}}(\mathcal{D})$ (algebraische Endomorphismen auf einer gemeinsamen Domäne),
- $\mathcal{L}^p(\mathcal{H})$ (Schatten-$p$-Klasse),
- Raum unbeschränkter Operatoren auf gemeinsamer Domäne.

Die Frage ist bewusst auf der Ebene von $Z^4(A,A)$ gestellt, da Wohldefiniertheit auf $HH^4(A,A)$ erst nach Konstruktion eines solchen Mechanismus geprüft werden kann.

---

## Kohomologischer Ausgangsbefund (Präzisierung)

**NEU-176–185** sichern die **neutrale** Nichttrivialität:

$$
[\Omega_{\mathbf{p}}] \neq 0 \quad \text{in} \quad HH^4(A_{\mathbb{Q}}^{\mathrm{alg}}, A_{\mathbb{Q}}^{\mathrm{alg}}), \qquad \deg_\Gamma(\Omega_{\mathbf{p}}) = 1_\Gamma.
$$

**Offen** (noch nicht nachgewiesen) bleibt:

$$
HH^4(A,A)_{\mathrm{ch}} \neq 0.
$$

NEU-189 bezieht sich ausschließlich auf die **neutrale** Vierklasse. Die geladene $HH^4$-Klasse ist kein gesichertes Ergebnis des bisherigen Katalogs.

---

## Typbefund (Ausgangslage)

$\Omega_{\mathbf{p}} \in Z^4(A,A) = \mathrm{Hom}_{\mathbb{C}}(A^{\otimes 4}, A)$ ist eine **vierlineare $A$-wertige Abbildung**, kein Operator auf einem Hilbertraum.

Selbst bei treuer Darstellung $\pi: A \to B(\mathcal{H})$ erhält man zunächst nur:

$$
(a_1, a_2, a_3, a_4) \longmapsto \pi\!\left(\Omega_{\mathbf{p}}(a_1, a_2, a_3, a_4)\right) \in B(\mathcal{H}),
$$

also eine vierlineare operatorwertige Abbildung $A^{\otimes 4} \to B(\mathcal{H})$, aber **kein ausgezeichnetes Element** $\rho_{\mathrm{op}}([\Omega_{\mathbf{p}}]) \in \mathcal{O}(\mathcal{H})$.

---

## Prüfknoten O-189-1a: Partieller Katalogbefund

**Geltungsbereich:** Konkret geprüfte Quellen: NEU-122 (GNS/KMS), NEU-127–188 (BC-Komplex, Spurformeln, Rohkopplung, Lifts, Rp/Tp-Operatoren, Hochschild-Komplex). Der Befund gilt **nicht global** für NEU-1 bis NEU-188 — die vollständige Sichtung erfolgt in NEU-190.

**Frage:** Findet sich im bisher geprüften Datenbestand ein typisierter Mechanismus $Z^4(A,A)$ oder $HH^4(A,A) \to \mathcal{O}(\mathcal{H})$?

**Partieller Katalogbefund:**
- $\pi: A_{\mathbb{Q}}^{\mathrm{alg}} \to B(\mathcal{H})$ — GNS-Darstellung via KMS-Zustand (NEU-122), aber ohne Dirac-Operator $D$ und ohne Kontraktionsstruktur für die vier Eingabestellen von $\Omega_{\mathbf{p}}$.
- $L_3^\circ$, $C_p$, $\widetilde{\omega}_2$, $W_{\mathrm{res,BC}}^{\mathrm{top}}$ — downstream-Zielobjekte, keine Realisierungsabbildung.
- Kein Vierzyklus $z \in C_4(A, N)$ mit operatorwertiger Paarung konstruiert.
- Kein spektrales Tripel $(A_{\mathbb{Q}}^{\mathrm{alg}}, \mathcal{H}, D)$ explizit festgelegt.
- Kein universeller Differentialkalkül mit Darstellung $a_0\, da_1 \cdots da_4 \mapsto \pi(a_0)[D,\pi(a_1)]\cdots[D,\pi(a_4)]$ vorhanden.
- Kein Kasparov-/KK-Produkt $KK^4 \to \mathcal{O}(\mathcal{H})$ definiert.

**Ergebnis O-189-1a:** $\checkmark[M]_{\mathrm{neg,Quelle}}$ — **Im bisher geprüften Datenbestand keine Operatorbrücke gefunden.**  
**Globaler Abschluss steht aus** — wird durch NEU-190 (vollständige Sichtung NEU-1 bis NEU-188) geliefert.

---

## Prüfknoten O-189-2: Repräsentantenunabhängigkeit

**Frage:** Falls ein Mechanismus $\rho_{\mathrm{op}}: Z^4(A,A) \to \mathcal{O}(\mathcal{H})$ konstruiert würde — unter welcher Bedingung wäre er auf $HH^4(A,A)$ wohldefiniert?

**Befund:** Da aus O-189-1a kein Mechanismus auf $Z^4$ vorliegt, ist diese Frage **gesperrt**. Für spätere Konstruktion: Wohldefiniertheit auf $HH^4$ erfordert $\rho_{\mathrm{op}}(b\Psi) = 0$ für alle $\Psi \in C^3(A,A)$, d.h. $\ker(\rho_{\mathrm{op}}) \supseteq \mathrm{im}(b)$.

**Ergebnis O-189-2:** $?[O]$ — **Gesperrt.**

---

## Prüfknoten O-189-3: Nichtverschwindung

**Frage:** Impliziert $[\Omega_{\mathbf{p}}] \neq 0$ in $HH^4$ automatisch $\rho_{\mathrm{op}}([\Omega_{\mathbf{p}}]) \neq 0$ in $\mathcal{O}(\mathcal{H})$?

**Befund:** Injektivität von $\rho_{\mathrm{op}}$ ist eine eigenständige Bedingung, die nicht aus der Nichttrivialität der **neutralen** Vierklasse folgt. Problem ist gesperrt, solange O-189-1a nicht global bestätigt ist.

**Ergebnis O-189-3:** $?[O]$ — **Gesperrt.**

---

## Prüfknoten O-189-4: Downstream-Kompatibilität

**Frage:** Passt ein (hypothetischer) Operator $\rho_{\mathrm{op}}([\Omega_{\mathbf{p}}])$ in den downstream benötigten Typ?

**Befund:**

| Downstream-Objekt | Typ | Anforderung an $\rho_{\mathrm{op}}$ |
|---|---|---|
| $L_3^\circ$ | Schatten-$p$/Wodzicki-Rest-Typ | $\rho_{\mathrm{op}} \in \mathcal{L}^p(\mathcal{H})$ oder pseudodifferentiell |
| $C_p$ | Schatten-Norm-Schranke | Spurklasse-Eigenschaft |
| $\widetilde{\omega}_2$ | BC-Zweiform | Kompatibilität mit BC-Graduierung |
| $W_{\mathrm{res,BC}}^{\mathrm{top}}$ | Wodzicki-Rest im BC-Kontext | Pseudodifferentieller Typ |

Ohne global abgeschlossene Basisstruktur aus O-189-1a nicht prüfbar.

**Ergebnis O-189-4:** $?[O]$ — **Gesperrt.**

---

## Knotenstatusblock

$$
\begin{aligned}
[\text{O-189-1a}] &\quad \checkmark[M]_{\mathrm{neg,Quelle}} && \text{partieller negativer Befund (geprüfter Ausschnitt)},\\
[\text{O-189-2}] &\quad ?[O] && \text{gesperrt},\\
[\text{O-189-3}] &\quad ?[O] && \text{gesperrt},\\
[\text{O-189-4}] &\quad ?[O] && \text{gesperrt}.
\end{aligned}
$$

Globaler Abschluss von O-189-1 steht aus. Nach positivem Abschluss von NEU-190 tritt an dessen Stelle:

$$
\boxed{
\text{Im gesamten RH-Katalog ist kein Mechanismus } Z^4(A,A) \text{ oder } HH^4(A,A) \to \mathcal{O}(\mathcal{H}) \text{ konstruiert.}
}
$$

---

## Gesamtbefund: Exakte Blockade

$$
\boxed{
[A_{\mathbb{Q}}^{\mathrm{alg}}, \mathcal{H}, \pi, \Omega_{\mathbf{p}}] \text{ bestimmen allein keinen kanonischen Operator } \rho_{\mathrm{op}}([\Omega_{\mathbf{p}}]).
}
$$

**Einordnung:** Exakte Blockade — ausdrücklich **kein** mathematischer No-go-Satz. Die Abbildung $HH^4(A,A) \to \mathcal{O}(\mathcal{H})$ ist nicht prinzipiell ausgeschlossen, aber kein typisierter Mechanismus ist im bisher geprüften Katalog-Datenbestand vorhanden.

---

## Realisierungskandidaten (vier verschiedene Mechanismen)

Die folgenden vier Möglichkeiten sind **keine gleichwertigen Minimalstrukturen**, sondern verschiedene Realisierungsmechanismen mit unterschiedlichen Voraussetzungen, Typen und Zielobjekten. Erst nach globalem Abschluss von NEU-190 kann entschieden werden, ob einer davon bereits implizit vorhanden ist:

1. **Spektrales Tripel** $(A_{\mathbb{Q}}^{\mathrm{alg}}, \mathcal{H}, D)$ — Dirac-Typ; Zieltyp: pseudodifferentiell, Domänenstruktur von $D$ erforderlich.
2. **Operatorwertiger Vierzyklus** $z \in C_4(A, N)$ mit Spurklassenpaarung — Zieltyp: $\mathcal{L}^1(\mathcal{H})$ oder $\mathbb{C}$; Zyklus-Eigenschaft erforderlich.
3. **Universeller Differentialkalkül** mit Darstellung — wie Mechanismus 1, aber ohne festes spektrales Tripel; Zieltyp: $\Omega^4$-Darstellung.
4. **Kasparov-/KK-Produkt** $KK^4(A, N) \to \mathcal{O}(\mathcal{H})$ — Zieltyp: KK-Gruppe; erfordert Kasparov-Modul über $A$.

---

## DAG-Struktur: Nachfolgeknoten

| Knoten | Inhalt | Status |
|---|---|---|
| **NEU-190** | Vollständige Katalogsichtung NEU-1 bis NEU-188: Existiert irgendein typisierter Mechanismus $Z^4(A,A)$ oder $HH^4(A,A) \to \mathcal{O}(\mathcal{H})$? | $?[O]$ |
| **NEU-191** | Auswahl oder Neukonstruktion eines Realisierungsmechanismus | gesperrt bis NEU-190 |

NEU-191 wird erst nach globalem Abschluss von NEU-190 eröffnet.

---

## Abgrenzung

- Die Repositories `prolate-primes-paper` und `prolate-gram-coercivity` enthalten keine konstruierte Brücke und werden in NEU-189 **nicht referenziert**.
- NEU-189 öffnet **keine** neue Kohomologie- oder Mikrolokalroute.
- **Keine geladene $HH^4$-Klasse** wird in NEU-189 vorausgesetzt oder behauptet. Referenzen auf NEU-176–185 betreffen ausschließlich die neutrale Klasse $[\Omega_{\mathbf{p}}] \neq 0$.
