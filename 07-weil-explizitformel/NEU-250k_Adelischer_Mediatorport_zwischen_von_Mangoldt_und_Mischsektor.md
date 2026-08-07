# NEU-250k — Adelischer Mediatorport zwischen von-Mangoldt- und Mischsektor

**Katalog-ID:** NEU-250k  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Vorgänger:** NEU-250j (Trägertrennung), NEU-245b/c (M1–M4, S_adel-Mindestarchitektur), NEU-250h (Quellenabbildung, primitiver Kanal)  
**Status:** K1 ?[O], K2 ?[O] mit Konstruktionsbedingungen, K3 ✓[M]_{neg}, K4 ?[O] Kandidat

---

## 0. Ausgangslage und Zielstellung

NEU-250j hat festgestellt:
$$
\operatorname{supp}\Lambda \cap \operatorname{supp}(K_{pq}\text{-Kollision}) = \varnothing. \qquad (0.1)
$$

Die lokale arithmetische Gewichtung (NEU-250g–i, $\mathcal{P}^*$-Sektor) und die globale Nichtorthogonalität (Mischsektor $\mathcal{M}$, $\omega(M)\geq2$) leben auf **disjunkten Trägern**. Kein vorhandener Dynamikoperator transportiert zwischen $\mathcal{H}_{\mathcal{P}^*}$ und $\mathcal{H}_{\mathcal{M}}$.

Der vorliegende Knoten klärt, ob ein **gemeinsames adelisches Quellenbild** $\mathcal{S}_{\rm adel}$ beide Sektoren gleichzeitig speisen kann, ohne die Mindestbedingungen M1–M4 aus NEU-245b/c zu verletzen.

Wichtig: Es soll kein ad-hoc-Operator $A:\mathcal{H}_{\mathcal{P}^*}\to\mathcal{H}_{\mathcal{M}}$ erfunden werden. Das wäre genau die Art nachträglicher Zielraumkopplung, die M1 (Blockseparation) und M3 (gemeinsames Quellenbild) verbieten.

---

## K1 — Existenz und Typ des gemeinsamen Quellenraums $\mathcal{S}_{\rm adel}$

**Befund aus NEU-245b (M3, verbindlich):**
> Die Kopplung zwischen archimedischem und p-adischem Sektor erfolgt ausschließlich über den gemeinsamen analytischen Testfunktionsraum (NEU-220j). Eine direkte Operatorkopplung ist nicht zulässig.

**Befund aus NEU-245c (§4, M3-Status):**
> $\mathcal{S}_{\rm adel}$ ist in NEU-220j typisiert, aber die vollständige Abbildung $\mathcal{S}_{\rm adel}\to(\mathcal{H}_N^{\rm rel}, D_N^{\rm rel}, \Psi_N)$ ist noch nicht konstruiert (Status: ?[O]).

Die **Architektur** des adelischen Quellenbildes ist damit verbindlich im Repo verankert [NEU-245b, §3-4]:

$$
\boxed{\begin{array}{ccc}
 &&\mathcal{S}_{\rm adel}\\
 &\swarrow T_\Lambda & \downarrow T_{\mathcal{M}} \searrow T_\infty\\
\mathcal{H}_\Lambda & \mathcal{H}_{\mathcal{M}} & \mathcal{H}_\infty
\end{array}} \qquad (1)
$$

wobei
$$
\mathcal{H}_\Lambda = \bigoplus_{p,k} \mathcal{H}_{p^k}^{\rm bal}, \qquad \mathcal{H}_{\mathcal{M}} = \overline{\operatorname{span}}\{j_{R,M}: M\in\mathcal{M},\ \omega(M)\geq2\}, \qquad \mathcal{H}_\infty = \mathcal{K}_X.
$$

**Typbedingung (M2, aus NEU-245b):** Der $p$-adische Block $W_p$ muss vollständig im Bewertungsderivations-Typ $\mathcal{B}_{\rm val}$ liegen. Ein Koszul-Additiv aus $\mathcal{B}_{\log}$ ist nicht zulässig (NEU-245b, M2; NEU-245c, §3).

**Aktueller Status:**
- Architektur und Typ: ?[O] — NEU-245b/c liefern nur die Mindestarchitektur-Vorgabe eines gemeinsamen Quellenraums; Existenz und vollständiger Typ von $\mathcal{S}_{\rm adel}$ sind noch nicht konstruktiv belegt (per NEU-250n, §Korrektur K1)
- Konkrete Abbildung $T_\Lambda$: ✓[M] auf $\mathcal{P}^*$ (NEU-250g–i liefern lokale Zutaten, NEU-250h den Port)
- Konkrete Abbildung $T_{\mathcal{M}}$: ?[O] (K2 unten)
- Konkrete Abbildung $T_\infty$: ?[O], verwiesen an NEU-221c/d/e (archimedischer Port, M4c)

---

## K2 — Existenz eines nichttrivialen Mediatorports $T_{\mathcal{M}}$

**Kernfrage:** Gibt es einen bereits motivierten, nichttrivialen Port $T_{\mathcal{M}}:\mathcal{S}_{\rm adel}\to\mathcal{H}_{\mathcal{M}}$, der nicht rückwärts aus gewünschten $K_{pq}$ konstruiert ist?

**Notwendige Bedingungen an $T_{\mathcal{M}}$ (aus dem Repobefund):**

1. $T_{\mathcal{M}}(f)$ muss für $f\in\mathcal{S}_{\rm adel}$ im Mischsektor $\mathcal{H}_{\mathcal{M}}$ liegen.
2. $T_{\mathcal{M}}$ darf keinen neuen diagonalen von-Mangoldt-Term erzeugen (K3, siehe unten).
3. $T_{\mathcal{M}}$ muss aus der intrinsischen BC-Algebrastruktur oder dem adelischen Momentenbild (NEU-221) stammen, nicht als ad-hoc-Abbildung postuliert werden.
4. $T_{\mathcal{M}}$ muss M1-konform sein: kein Off-Axis-Eintrag im Operator, sondern Kopplung ausschließlich über $\mathcal{S}_{\rm adel}$.

**Kandidat aus NEU-221 (Adelische Momentquelle):**

NEU-221 definiert die adelische Momentquelle als Abbildung
$$
f \mapsto \langle\Psi_N, J_{X,N}^k\,\Psi_N\rangle
$$
durch den Feshbach-Weyl-Kandidaten. Auf dem Mischsektor $\mathcal{H}_{\mathcal{M}}$ erzeugen Vektoren der Form $j_{R,M}$ ($M\in\mathcal{M}$) durch die $\Theta$-Wirkung und die Kreuzspektralmaße $\mu^{a,b}_{pq}$ (KONVENTIONEN.md §X.3) nicht-diagonale Beträge.

Ein nichttrivialer Port wäre dann:
$$
T_{\mathcal{M}}(f) := \text{Projektion auf } \mathcal{H}_{\mathcal{M}} \text{ der Feshbach-Streukomponente von } D_{\rm scatt,N}(f). \qquad (2)
$$

Hier ist $D_{\rm scatt,N}$ der Streublock aus dem Feshbach-Schema (NEU-221c, NEU-245c §2). **Ob dieser Block tatsächlich eine nichttriviale Projektion auf $\mathcal{H}_{\mathcal{M}}$ liefert, ist nach NEU-245c §2 noch offen** (M4c: konkrete globale Kopplung in $D_{\rm scatt,N}$ noch nicht verifiziert).

$$
\boxed{T_{\mathcal{M}}\text{ existiert als struktureller Kandidat (Feshbach-Streublock), aber ist noch nicht positiv konstruiert.}} \quad(?[O])
$$

---

## K3 — Firewall gegen falschen Selbstterm $\|T_{\mathcal{M}}a\|^2$

**Problem:** Wenn $T = T_\Lambda + T_{\mathcal{M}} + T_\infty$, dann gilt
$$
\|Ta\|^2 = \|T_\Lambda a\|^2 + 2\operatorname{Re}\langle T_\Lambda a, T_{\mathcal{M}}a\rangle + \|T_{\mathcal{M}}a\|^2 + \text{(weitere Kreuzterme)}. \qquad (3)
$$

Der Term $\|T_{\mathcal{M}}a\|^2$ würde einen **neuen positiven Beitrag** erzeugen, der auf dem Mischsektor liegt, wo $\Lambda(M)=0$. Das wäre ein falscher zusätzlicher diagonaler Weilterm.

**Firewall:** Das Vollblock-No-Go (NEU-220t, NEU-245b M1) verbietet es, $\mathcal{H}_{\mathcal{M}}$ als eigenständigen positiven Hilbertblock in die Weil-Form einzubauen. Der Selbstterm $\|T_{\mathcal{M}}a\|^2$ ist also **nicht zulässig als isolierter Summand** der Weil-Quadratik.

Dies ist auf **zwei Arten** konsistent lösbar:

**Option A: Geometrische Elimination.**  
Der Mischsektor $\mathcal{H}_{\mathcal{M}}$ wird nur als Zwischenraum verwendet und anschließend durch einen Schur/Feshbach-Ausdruck aus der effektiven Weilform herausintegriert:
$$
B_{\rm eff}(z) = T_\Lambda^* T_{\mathcal{M}}\,(A_{\mathcal{M}}-z)^{-1}\,T_{\mathcal{M}}^* T_\Lambda. \qquad (4)
$$
Dann erscheint $\|T_{\mathcal{M}}a\|^2$ nicht direkt in der Spektralformel; stattdessen entsteht ein effektiver $\mathcal{H}_\Lambda\to\mathcal{H}_\Lambda$-Kreuzblock. Dies erfordert einen wohldefinierten Operator $A_{\mathcal{M}}$ auf dem Mischsektor (noch nicht konstruiert).

**Option B: Nulling durch Typ-Bedingung.**  
Wenn $T_{\mathcal{M}}$ ausschließlich in den Off-Diagonalbeitrag $\operatorname{Re}\langle T_\Lambda a, T_{\mathcal{M}}a\rangle$ eingeht, und $\|T_{\mathcal{M}}a\|^2$ durch eine geeignete Nullteilungsbedingung verschwindet (z.B. $T_{\mathcal{M}}$ nilpotent oder als Randwert definiert), entfällt der Selbstterm strukturell. Diese Option ist konservativer, aber enger.

$$
\boxed{\|T_{\mathcal{M}}a\|^2\text{ als isolierter positiver Weilterm: nicht zulässig (M1, NEU-220t). Option A oder B erforderlich.}} \quad(\checkmark[M]_{\rm neg})
$$

---

## K4 — Intrinsischer Off-Diagonalblock aus $T_\Lambda^* T_{\mathcal{M}}$

**Kernfrage:** Entsteht der benötigte Off-Diagonalblock intrinsisch als $T_\Lambda^* T_{\mathcal{M}}$ oder $T_p^* T_q$, statt als separat definierter Kreuzterm?

**Antwort aus dem Repobefund:** Das ist das präzise Ziel, das M3 (gemeinsames Quellenbild) und das Additiv-Kreuzterm-No-Go (NEU-245b §2.2) gemeinsam erzwingen:

- Ein separat definierter Kreuzterm $B_{pq}$ wäre nach NEU-245 [c.2a] nicht zulässig (Typ-Inhomogenität).
- Ein Gramblock der Form $T_p^* T_q$ ist genau dann kanonisch, wenn $T_p$ und $T_q$ aus **derselben** Quellenabbildung $\mathcal{S}_{\rm adel}\to\mathcal{H}$ stammen.

Die globale Faktorisierung lautet dann
$$
\mathcal{T} = T_\Lambda + T_{\mathcal{M}} + T_\infty: \mathcal{S}_{\rm adel} \to \mathcal{H}_\Lambda \oplus \mathcal{H}_{\mathcal{M}} \oplus \mathcal{H}_\infty, \qquad (5)
$$
wobei der Zielraum **nicht orthogonal zerlegt** ist. Aus $\mathcal{T}^*\mathcal{T}$ entstehen automatisch die Kreuzblöcke:
$$
B_{\Lambda\mathcal{M}} = T_\Lambda^* T_{\mathcal{M}}, \qquad B_{\Lambda\infty} = T_\Lambda^* T_\infty, \qquad B_{\mathcal{M}\infty} = T_{\mathcal{M}}^* T_\infty. \qquad (6)
$$

Dies ist genau das S12-Konstruktionsprinzip (NEU-245c §2): Kopplung als Gramblock einer gemeinsamen Faktorisierung, nicht als nachträglich erfundener Term.

**Status:**
- Grammatikprinzip (6) als Zieltyp: ✓[M], aus NEU-245b/c (M1+M3+S12)
- Konkrete Realisierung von $T_{\mathcal{M}}$ und damit $B_{\Lambda\mathcal{M}}$: hängt an K2 (?[O])
- Konkrete Realisierung von $T_\infty$ und damit $B_{\Lambda\infty}$, $B_{\mathcal{M}\infty}$: hängt an NEU-221c/d/e und M4 (?[O])

$$
\boxed{\text{Off-Diagonalblock als }T_\Lambda^* T_{\mathcal{M}}\text{ ist der kanonische Zieltyp. Realisierung hängt an K2.}} \quad(?[O])
$$

---

## Gesamtbild: Drei-Port-Architektur im Repo-Kontext

Die strukturelle Position der NEU-250g–k-Serie ist jetzt:

| Knoten | Geleistetes | Status |
|---|---|---|
| NEU-250g | $h_n^{\rm bal}=n^{-1/2}I$, G1/G2 für $m=1$ | ✓[M] |
| NEU-250h | $T_\Lambda(a)$: Quellenabbildung primitiver Kanal, $\operatorname{Re}\langle a,U_{\log p}a\rangle$ | ✓[M] |
| NEU-250i | $\Lambda(p^k)/\sqrt{p^k}\,\delta_{RR'}$ vollständig auf $\mathcal{P}^*$ | ✓[M] |
| NEU-250j | Trägertrennung: $\operatorname{supp}\Lambda\cap\operatorname{supp}(K_{pq}\text{-Koll.})=\varnothing$ | ✓[M] |
| NEU-250k | Drei-Port-Architektur, K3-Firewall, K4-Grammatik | K1?[O], K2?[O], K3✓$_{\rm neg}$, K4?[O] |

Die **offene Hauptfrage** lautet jetzt präzise:

$$
\boxed{\text{Existiert ein aus NEU-221 / } \mathcal{S}_{\rm adel}\text{ kanonisch extrahierter Feshbach-Streublock als }T_{\mathcal{M}},}
$$
$$
\text{der Option A (Schur-Elimination) zugänglich ist und mit M4c-M4d kompatibel bleibt?} \qquad ([O\text{-}250k/1])
$$

Wenn $[O\text{-}250k/1]$ positiv entschieden wird (J-A aus NEU-250j), entsteht $B_{\Lambda\mathcal{M}} = T_\Lambda^* T_{\mathcal{M}}$ als erster nichtdiagonaler Kopplungsblock des Gesamt-Weil-Operators.

Wenn $[O\text{-}250k/1]$ negativ (J-B), ist $\mathcal{H}_{\mathcal{M}}$ geometrisch vorhanden, aber als Mediator ungeeignet; der einzig verbleibende Kopplungsweg führt über $T_\infty$ (archimedischer Port) und den Kreuzblock $B_{\Lambda\infty} = T_\Lambda^* T_\infty$.

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-245b (79ecf25) | M1–M3, $\mathcal{S}_{\rm adel}$-Mindestarchitektur, Vollblock-/Additiv-No-Go |
| NEU-245c (1ef32ab) | M4, S12-Grammatikprinzip, M3 allein genügt nicht, $[O\text{-}245c/1\text{-}2]$ |
| NEU-220t | Metrikblock-No-Go, OffAxis-Trägheit |
| NEU-220j | Analytischer Weil-Testfunktionsraum ($\mathcal{S}_{\rm adel}$-Typ) |
| NEU-221c/d/e | Feshbach-Weyl-Tripel, $T_\infty$-Kandidat, Normierungsfragen |
| NEU-250h (NEU-250h.md) | $T_\Lambda$ auf primitivem Kanal, lokale Zutaten |
| NEU-250i (73153ee) | Vollständiger primitiver Koeffizient $\Lambda(p^k)/\sqrt{p^k}$ |
| NEU-250j (d855de8) | Trägertrennung $\mathcal{P}^*$ vs. $\mathcal{M}$, J-A/J-B |
| NEU-250n (e0f2f70) | Direktaudit adelisch-archimedische Quellbrücke; fordert K1-Rückstufung |
| KONVENTIONEN.md §X.3 | $K_{pq}$-Überlappung, Kreuzspektralmaße, Spektralmaßwarnung |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/objekt-x-programm.*
