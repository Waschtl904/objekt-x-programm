# NEU-250l — Typsicherer Streublock-Mediatoraudit und Entscheidung J-A/J-B

**Katalog-ID:** NEU-250l  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Knoten:** $[O\text{-}250k/1a]$  
**Vorgänger:** NEU-250k (Drei-Port-Architektur, K3-Firewall), NEU-221c (Feshbach-Weyl-Kandidat), NEU-245d (Basistripel-Audit)  
**Status:** L1–L3 ✓[M]$_{\rm neg}$ oder ?[O]; L4–L5 Entscheidungsbefund (J-B vorläufig aktiv)

---

## 0. Präzise Aufgabenstellung

NEU-245d hatte $[O\text{-}245c/1]$ als "Direktaudit des Basistripels" behandelt und als $\checkmark[M]_{\rm part}$ gebucht. Dieser Status ist durch die 250-Serie **teilweise überholt**: NEU-250a hat gezeigt, dass die relative Wres-Paarung ohne die fehlende Repräsentationsabbildung $j_{p,N}$ nicht konstruiert ist; damit sind Grammatrix, Radikal und Hilbert-Quotient in NEU-245d noch nicht als **konkrete mathematische Objekte** verfügbar, sondern nur als abstrakte Konstruktionstypen.

Den alten Feshbach-Knoten als intaktes Basistripel zu behandeln, ist daher nicht zulässig.

Dieser Knoten stellt eine **engere Frage**, die unabhängig von $j_{p,N}$ entschieden werden kann:

$$
\boxed{\text{Auf welchem Raum ist }D_{\rm scatt,N}\text{ tatsächlich definiert, und liegt dieser Raum vor dem Wres-Quotienten?}} \qquad (0)
$$

Erst wenn diese Typfrage positiv entschieden ist, ist eine Mischsektorprojektion $P_{\mathcal{M}}D_{\rm scatt,N}$ überhaupt formulierbar, und erst dann darf $[O\text{-}250k/1]$ (J-A/J-B) getestet werden.

---

## L1 — Originaldefinition und Typ von $D_{\rm scatt,N}$

**Quellenbestand:** NEU-221c, NEU-221d, NEU-245d, NEU-46 (implizit)

**Was NEU-221c tatsächlich sagt:** Der Feshbach-Weyl-Kandidat setzt voraus:
$$
\mathcal{H}_N^{\rm rel}, \quad D_N^{\rm rel} = (D_N^{\rm rel})^*, \quad \Psi_N \in \mathcal{H}_N^{\rm rel}.
$$

Die Zerlegung $D_N^{\rm rel}$ in einen "Streublock" $D_{\rm scatt,N}$ und lokale Primblöcke erscheint in NEU-221c **nicht als explizite Definition**, sondern nur als Konstruktionsheuristik in §6:
> "Der relevante $D_N^{\rm rel}$ muss ein gekoppelter Schur-/Feshbach-Operator sein."

In NEU-221d wird ein Streublock nur als **offener Knoten** $[O\text{-}221\text{-}1c1d]$ geführt:
> "Nicht bewiesen ist, dass der Streublock tatsächlich eine nichttriviale globale Kopplung erzeugt."

**Befund L1:** Es existiert **keine explizite Definition**
$$
D_{\rm scatt,N}: \mathcal{X}_N \longrightarrow \mathcal{Y}_N
$$
mit benannten Räumen $\mathcal{X}_N$, $\mathcal{Y}_N$ in irgendeiner Quelldatei bis NEU-250k.

$$
\boxed{D_{\rm scatt,N}\text{ hat keine explizite Raum-/Typdefinition im Repo.}} \qquad \checkmark[M]_{\rm neg} \qquad (L1)
$$

---

## L2 — Abhängigkeit / Unabhängigkeit vom Wres-Quotienten

**Was bekannt ist:**  
Nach NEU-245d §1.1 wird $\mathcal{H}_N^{\rm rel}$ als
$$
\mathcal{H}_N^{\rm rel} = \mathcal{H}_{N,\rm raw} \big/ \mathcal{N}_{W_{\rm res},\rm rel}
$$
definiert. Der Quotient setzt die relative Wres-Paarung voraus. Nach NEU-250a ist diese Paarung ohne $j_{p,N}$ **noch nicht konstruiert**.

**Konsequenz:** Jeder Operator, der auf $\mathcal{H}_N^{\rm rel}$ lebt, setzt — zumindest implizit — den Wres-Quotienten voraus. Wenn $D_{\rm scatt,N}$ als Teil von $D_N^{\rm rel}$ (via Feshbach-Schur-Zerlegung in $\mathcal{H}_N^{\rm rel}$) definiert ist, dann:

$$
\boxed{D_{\rm scatt,N}\text{ hängt am Wres-Quotienten und ist damit aktuell nicht konstruiert.}} \qquad \checkmark[M]_{\rm neg} \qquad (L2)
$$

Ein **prä-quotientaler Streublock** — also einer, der auf $\mathcal{H}_{N,\rm raw}$ oder direkt auf der BC-Algebra definiert ist, bevor der Wres-Quotient gebildet wird — wäre die einzige Ausnahme. Nach aktuellem Quellenstand gibt es keinen solchen Kandidaten.

**Offene Hypothese** $[H\text{-}250l/1]$: Gibt es eine Realisierung von $D_{\rm scatt,N}$ auf $\mathcal{H}_{N,\rm raw}$ oder direkt auf dem BC-Algebra-Definitionsbereich, die **vor** dem Wres-Quotienten liegt? Ein solcher Kandidat müsste aus NEU-46 oder KONVENTIONEN.md §X.3 (Kreuzspektralmaße $\mu^{a,b}_{pq}$) extrahierbar sein.

$$
[H\text{-}250l/1]:\quad \exists\, D_{\rm scatt,N}^{\rm pre}: \mathcal{H}_{N,\rm raw} \to \mathcal{H}_{N,\rm raw}, \quad\text{unabhängig von }\mathcal{N}_{W_{\rm res},\rm rel}. \qquad ?[O] \qquad (L2a)
$$

---

## L3 — Kanonische Mischsektorprojektion $P_{\mathcal{M}}$

**Was benötigt wird:**  
Eine kanonische Projektion
$$
P_{\mathcal{M}}: \mathcal{H}_N \longrightarrow \mathcal{H}_{\mathcal{M},N}, \qquad \mathcal{M} = \{M: \omega(M) \geq 2\},
$$
die intrinsisch durch den Monoidindex $M$ definiert ist.

**Quellenbestand:**  
KONVENTIONEN.md §X.3 definiert die Graphbasis $\eta_{p;m;r,u} \leftrightarrow e_R V_M$ mit $M = pm$. Die Mischsektorvektoren sind diejenigen mit $\omega(M) \geq 2$ — das ist durch NEU-250j (✓[M]) zahlentheoretisch klar abgegrenzt.

**Typ der Projektion:**  
Die Projektion auf den Mischsektor ist als **Spektralmassrestriktion** auf den Indexbereich $\{M: \omega(M) \geq 2\}$ wohldefiniert, *sofern* eine orthogonale Zerlegung nach Monoidindex $M$ vorliegt.

**Problem:** Nach KONVENTIONEN.md §X.3 ist die Graphbasis global **nicht orthonormal** (verschiedene $(p,m)$ treffen dasselbe $V_{pm}$; Off-Diagonalterme $K_{pq} \neq 0$). Eine naive Projektion auf Mischindizes ist daher **nicht kanonisch** ohne eine vollständige Basis oder eine Spektralmaßzerlegung.

$$
\boxed{P_{\mathcal{M}}\text{ als kanonische Projektion erfordert eine Orthogonalisierung oder ein Spektralmaß, das noch nicht konstruiert ist.}} \qquad ?[O] \qquad (L3)
$$

**Ausnahme:** Falls man direkt auf dem Rohraumindex $M$ (also auf $\mathcal{H}_{N,\rm raw}$, bevor Nichtorthogonalitat relevant wird) projiziert, könnte eine förmliche Projektion
$$
P_{\mathcal{M}}^{\rm raw} j_{R,M} = \begin{cases} j_{R,M} & \omega(M) \geq 2 \\ 0 & \text{sonst} \end{cases}
$$
definiert werden. Aber dieser Rohraumprojektor ist kein Hilbertraum-Projektor, solange das Skalarprodukt auf $\mathcal{H}_{N,\rm raw}$ nicht fixiert ist.

---

## L4 — Ist $P_{\mathcal{M}} D_{\rm scatt,N} \neq 0$?

Da L1 und L2 beide negativ ausgegangen sind (kein explizit definierter Streublock, Abhängigkeit vom unkonstruierten Wres-Quotienten) und L3 die Projektion als unkonstruiert ausweist, ist die Frage
$$
P_{\mathcal{M}} D_{\rm scatt,N} \neq 0 \;?
$$
 **im aktuellen Quellenstand nicht formulierbar**.

Das ist kein positiver oder negativer Befund über den Mischsektorbeitrag — es ist ein **Typfehler**: die Frage stellt zwei noch nicht konstruierte Objekte nebeneinander.

$$
\boxed{P_{\mathcal{M}} D_{\rm scatt,N} \neq 0\; ?\quad\text{ist aktuell nicht formulierbar (Typfehler L1+L2+L3).}} \qquad \checkmark[M]_{\rm neg} \qquad (L4)
$$

---

## L5 — Entscheidung J-A oder J-B

### Befund

Aus L1–L4 ergibt sich:

$$
\boxed{\text{J-B aktiv: Der Streublock-Mediatorweg ist für den aktuellen Quellenstand nicht zugänglich.}} \qquad (L5)
$$

Dieser J-B-Befund ist jedoch **kein endgültiger Struktursatz**, sondern ein **Quellenbefund**: Das Repo enthält aktuell keine Definition, die $D_{\rm scatt,N}$ als quotienten-unabhängigen Mediatorport ermöglicht.

### Was J-A bräuchte (präzisierte Bedingungen)

J-A wäre bestätigt, wenn **alle drei** der folgenden Punkte positiv belegt werden könnten:

**J-A1:** Ein prä-quotientaler Streuoperator $D_{\rm scatt,N}^{\rm pre}$ auf $\mathcal{H}_{N,\rm raw}$ oder der BC-Algebra existiert und ist unabhängig von $\mathcal{N}_{W_{\rm res},\rm rel}$ definierbar. (Kandidat: Kreuzspektralmaße $\mu^{a,b}_{pq}$ aus KONVENTIONEN.md §X.3.)

**J-A2:** Die Projektion $P_{\mathcal{M}}$ ist durch ein kanonisches Spektralmaß oder eine Orthogonalisierung auf dem Rohraum realisierbar, die M1-konform ist.

**J-A3:** Das Bild $P_{\mathcal{M}} D_{\rm scatt,N}^{\rm pre} f$ verschwindet nicht für generisches $f \in \mathcal{S}_{\rm adel,N}$.

Diese drei Bedingungen definieren den neuen Unterknoten $[O\text{-}250l/1]$:

$$
\boxed{[O\text{-}250l/1]: \text{ J-A1+J-A2+J-A3 aus Kreuzspektralmaßen von KONVENTIONEN.md §X.3.}} \qquad ?[O]
$$

### Sofortkonsequenz für die Gesamtarchitektur

Da J-B vorläufig aktiv ist, wird $T_{\mathcal{M}} = 0$ als Arbeitshypothese gesetzt. Das bedeutet:

$$
\boxed{B_{\Lambda\infty} = T_\Lambda^* T_\infty \quad\text{ist vorläufig der einzige globale Kopplungsblock.}} \qquad (L5\text{-Kons.})
$$

Der archimedische Port $T_\infty: \mathcal{S}_{\rm adel} \to \mathcal{H}_\infty$ (NEU-221c/d/e, M4) ist damit der nächste Konstruktionsknoten, ohne vorherigen Mischsektorumweg.

---

## Strukturtabelle

| Schritt | Frage | Befund | Status |
|---|---|---|---|
| L1 | Raum/Typ von $D_{\rm scatt,N}$? | Keine explizite Definition im Repo | $\checkmark[M]_{\rm neg}$ |
| L2 | Unabhängig vom Wres-Quotienten? | Nein; Quotienten-abhängig via $\mathcal{H}_N^{\rm rel}$ | $\checkmark[M]_{\rm neg}$ |
| L2a | Prä-quotientaler Kandidat? | $[H\text{-}250l/1]$: möglich via $\mu^{a,b}_{pq}$, aber nicht konstruiert | $?[O]$ |
| L3 | Kanonische $P_{\mathcal{M}}$? | Erfordert Orthogonalisierung, noch nicht konstruiert | $?[O]$ |
| L4 | $P_{\mathcal{M}} D_{\rm scatt,N} \neq 0$? | Nicht formulierbar (Typfehler L1+L2+L3) | $\checkmark[M]_{\rm neg}$ |
| L5 | J-A oder J-B? | J-B vorläufig aktiv (Quellenbefund, nicht Struktursatz) | $\checkmark[M]_{\rm neg,\rm prov}$ |
| $[O\text{-}250l/1]$ | J-A1+J-A2+J-A3 aus $\mu^{a,b}_{pq}$? | Offen; Kreuzspektralmaße als einziger Kandidat | $?[O]$ |

---

## Folgeknoten

**Primärer Pfad (J-B aktiv):**  
$T_\infty$-Konstruktion: archimedischer Port aus NEU-221c/d/e, Knoten $[O\text{-}245c/1]$ (Nullmodusfreiheit, Basismoment $m_{0,N}$) und $[O\text{-}245c/2]$ ($M_{X,N} \to M_\Xi$).

**Sekundärer Pfad (J-A testen):**  
Knoten $[O\text{-}250l/1]$: Aus den Kreuzspektralmaßen $\mu^{a,b}_{pq}(B) = \langle V_p a, E_{D_{\rm rel}}(B) V_q b\rangle$ (KONVENTIONEN.md §X.3) einen prä-quotientalen Streuoperator extrahieren und gegen J-A1–J-A3 prüfen. Diese Arbeit blockiert den archimedischen Port nicht.

$$
\boxed{\text{J-B: }T_\infty\text{ ist der nächste Hauptknoten.} \quad [O\text{-}250l/1]\text{ läuft parallel, blockiert nichts.}}
$$

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-221c (b0f4e02) | Feshbach-Weyl-Kandidat; Streublock nur als Heuristik, nicht als Typdefinition |
| NEU-221d | $[O\text{-}221\text{-}1c1d]$: konkreter globaler Kopplungsgehalt offen |
| NEU-245d (bce8f9f) | Basistripel-Audit; $D_N^{\rm rel}$ auf Wres-Quotient abhängig; $\Psi_N$ nicht intrinsisch konstruiert |
| NEU-250a | Relative Wres-Paarung ohne $j_{p,N}$ unkonstruiert |
| NEU-250j (d855de8) | Trägertrennung $\mathcal{P}^* \cap \mathcal{M} = \varnothing$ |
| NEU-250k (a4ec0bb) | K3-Firewall: $\|T_{\mathcal{M}}a\|^2$ nicht als isolierter Weilterm zulässig |
| KONVENTIONEN.md §X.3 | Kreuzspektralmaße $\mu^{a,b}_{pq}$; einziger verbleibender J-A-Kandidat |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/objekt-x-programm.*
