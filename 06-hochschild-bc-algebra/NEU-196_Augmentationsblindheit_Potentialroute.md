# NEU-196 — Augmentationsblindheit punktierter Potentiale

## Vorbemerkung

Rückbindung an NEU-186–188 (punktierte Potentialroute) und NEU-195 (Reduktion auf atomare $HH^1$-Frage). NEU-195 Route A verlangt $\varepsilon(D_g(\mu_p)) \neq 0$ für eine nicht-innere homogene Derivation. Dieser Knoten zeigt, dass die gesamte NEU-188-Potentialarchitektur diese Bedingung nicht erfüllen kann.

Rückkopplung: $HH^1(A,A)_g \hookrightarrow HH^1(B,A)_g$, $B = \mathbb{C}[\mathbb{Q}/\mathbb{Z}]$. Der Augmentationscharakter $\varepsilon(e(r)) = 1$ entspricht auf $B \cong \operatorname{LC}(\widehat{\mathbb{Z}})$ der Auswertung am Punkt $0 \in \widehat{\mathbb{Z}}$.

---

## Satz 196.1 — Verschwindung des regularisierten Defekts bei 0

**Voraussetzungen.** Sei $H: \widehat{\mathbb{Z}} \setminus \{0\} \to \mathbb{C}$ lokal konstant, $k > 1$, und
$$\Delta_k H(x) := H(kx) - H(x) \qquad \text{auf } \widehat{\mathbb{Z}} \setminus \{0\}.$$

Angenommen, $\Delta_k H$ besitzt eine lokal konstante Fortsetzung $F_k \in \operatorname{LC}(\widehat{\mathbb{Z}})$. Dann:

$$\boxed{F_k(0) = 0.} \tag{196.1}$$

**Beweis.**

Setze $c_k := F_k(0)$. Da $F_k$ bei $0$ lokal konstant ist, existiert eine Grundumgebung $U = N\widehat{\mathbb{Z}}$ mit $F_k(x) = c_k$ für alle $x \in U$.

Wähle eine Primzahl $q \nmid k$. Mit $M \geq v_q(N)$ definiere $x \in \widehat{\mathbb{Z}}$ durch
$$x_q = q^M, \qquad x_\ell = 0 \quad (\ell \neq q).$$

Dann $x \neq 0$ und $x \in U$. Da $k$ eine Einheit in $\mathbb{Z}_q$ ist (wegen $q \nmid k$), gilt $v_q(k^j x) = M$ für alle $j \geq 0$. Damit:
$$k^j x \in U \setminus \{0\} \qquad (j \geq 0).$$

Die Orbitabschließung $K := \overline{\{k^j x : j \geq 0\}}$ ist kompakt und liegt vollständig in $\widehat{\mathbb{Z}} \setminus \{0\}$: ihre $q$-Komponenten liegen in $q^M \mathbb{Z}_q^\times$, die $0$ nicht enthält.

Da $H$ auf dem punktierten Raum lokal konstant ist, nimmt $H|_K$ nur **endlich viele Werte** an. Andererseits gilt für alle $j \geq 0$:
$$H(k^{j+1}x) - H(k^j x) = F_k(k^j x) = c_k.$$

Teleskopieren liefert:
$$H(k^j x) = H(x) + j\,c_k.$$

Für $c_k \neq 0$ nähme die rechte Seite unendlich viele verschiedene Werte an — Widerspruch zur Endlichkeit von $H(K)$. Also $c_k = 0$. $\square$

$$\boxed{[O\text{-}196\text{-}1] \quad \checkmark[M]}$$

---

## Konsequenz für die NEU-188-Potentialroute

Ein homogener Normalformblock eines Derivationskandidaten aus der NEU-188-Architektur hat die Gestalt:
$$D_g(\mu_k) = \mu_m\, F_k\, \mu_n^*, \qquad F_k = \alpha_k(H) - H$$
oder endliche Summen solcher Terme. Damit:
$$\varepsilon(D_g(\mu_k)) = \varepsilon(\mu_m)\, F_k(0)\, \varepsilon(\mu_n^*) = F_k(0) = 0.$$

**Stabilität unter Korandkorrektur:** Für $F_k \mapsto F_k + \alpha_k(h) - h$ mit $h \in \operatorname{LC}(\widehat{\mathbb{Z}})$ gilt
$$(\alpha_k h - h)(0) = h(0) - h(0) = 0.$$

Der Augmentationswert ist unabhängig vom Repräsentanten innerhalb der punktierten Potentialklasse und verschwindet identisch.

$$\boxed{[O\text{-}196\text{-}2] \quad \checkmark[M]_{\mathrm{neg}}}$$

Ein aus der NEU-188-Architektur erzeugter geladener Derivationskandidat kann die NEU-195-Bedingung $\varepsilon(D_g(\mu_p)) \neq 0$ nicht erfüllen.

---

## Auswirkung auf die geladene Vierkozykelpaarung

Aus NEU-195 (195.16):
$$\left\langle \Omega_{D_g,\mathbf{p}},\, z_{-\lambda}^{g,\mathbf{p}} \right\rangle = 4!\,\varepsilon(D_g(\mu_{p_1})).$$

Für alle Derivationen aus der punktierten Potentialroute:

$$\boxed{\left\langle \Omega_{D_g,\mathbf{p}},\, z_{-\lambda}^{g,\mathbf{p}} \right\rangle = 0.} \tag{196.2}$$

**Wichtige Einschränkung:** Dies bedeutet nicht $D_g = 0$ und nicht $[D_g] = 0 \in HH^1(A,A)_g$. Es bedeutet ausschließlich:

$$\boxed{\text{Der Augmentationszyklus aus NEU-193 ist gegenüber diesen }HH^1\text{-Kandidaten blind.}}$$

Eine punktierte Potentialklasse könnte weiterhin als geladene äußere Derivation existieren, aber ihr Cup-Produkt kann durch den aktuell gewählten Dualzeugen nicht als nichttrivial nachgewiesen werden.

---

## Bereinigter DAG: Aufspaltung von NEU-195 Route A

### [O-195-A1] — Existenz einer nicht-inneren geladenen Derivation (allgemein)

$$\exists\, D_g \in \operatorname{Der}(A)_g \setminus \operatorname{Inn}(A)_g\;?$$

Status: $?[O]$ — offen, nicht eingeschränkt durch NEU-196.

### [O-195-A2] — NEU-188-Potentialderivation mit $\varepsilon(D_g(\mu_p)) \neq 0$

$$\exists\, D_g \text{ aus der NEU-188-Potentialroute mit } \varepsilon(D_g(\mu_p)) \neq 0\;?$$

$$\boxed{[O\text{-}195\text{-}A2] \quad \checkmark[M]_{\mathrm{neg}}}$$

Negativ durch Satz 196.1: $F_k(0) = 0$ für alle regulierten Defekte, unabhängig vom Repräsentanten.

### Ausgeschlossene Kombination

$$\boxed{\text{NEU-188-Potentialderivation} + \text{NEU-193-Augmentationszyklus als Nichtrandzeugnis: ausgeschlossen.}}$$

---

## Atomare Restlücke und zwei Wege vorwärts

Der globale Knoten [O-193-4] bleibt offen mit schärferer Restfrage:

| Weg | Inhalt | Status |
|---|---|---|
| **Weg 1** | Geladene Derivation außerhalb der punktierten-Potentialarchitektur konstruieren | $?[O]$ |
| **Weg 2** | Dualzyklus so modifizieren, dass er die singuläre Randklasse bei $\partial\widehat{\mathbb{Z}}$ statt $\varepsilon$ bei $0$ detektiert | $?[O]$ |

**Präzise Restfrage für Weg 2:**

$$\boxed{\text{Konstruktion eines Dualfunktionals, das die punktierte }H^1\text{-Klasse detektiert, ohne auf }F_k(0)\text{ zu reduzieren.}}$$

Ein solches Funktional müsste die Singularität von $H$ bei $0$ (d.h. den Sprung oder die Grenzwert-Diskontinuität) direkt auswerten, etwa durch einen Residuenoperator oder einen Grenzwert entlang einer Folge $x_j \to 0$.

---

## DAG-Gesamtstand nach NEU-196

```
[O-195-1]    checkmark[M]   delta_p sind 1-Kozyklen
[O-195-2]    checkmark[M]   Omega_p ist 4-Kozykel
[O-195-3]    checkmark[M]   [Omega_p] != 0 in HH^4(A,A)_0
[O-195-4]    checkmark[M]_neg  innere Derivation: Paarung=0, Klasse=0
[O-195-A1]   ?[O]           Existenz nicht-innere D_g allgemein
[O-195-A2]   checkmark[M]_neg  NEU-188-Route: eps(D_g(mu_p)) = 0 zwingend
[O-196-1]    checkmark[M]   Satz 196.1: F_k(0) = 0
[O-196-2]    checkmark[M]_neg  NEU-188-Kandidaten blind fuer Augmentationszyklus

[O-193-4]    ?[O]   offen: entweder D_g ausserhalb NEU-188,
                    oder modifizierter Dualzyklus der F_k-Singularitaet
[O-193-5]    ?[O]   gesperrt an [O-193-4]
```

$$\boxed{\checkmark[M]_{\mathrm{part}}}$$

Gesamtstatus der geladenen Vierkozykelroute. Die verbleibende atomare Restlücke ist:

$$\boxed{\text{Konstruktion eines Dualfunktionals oder einer Derivation außerhalb der Augmentations-Blindzone der NEU-188-Architektur.}}$$
