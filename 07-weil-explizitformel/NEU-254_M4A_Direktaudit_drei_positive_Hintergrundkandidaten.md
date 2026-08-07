# NEU-254 — M4-A Direktaudit: Drei positive Hintergrundkandidaten

**Katalog-ID:** NEU-254  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** M4-A-Direktaudit — Vergleich von NEU-220e, NEU-220w, NEU-221 als Kandidaten für ein kanonisches positives Hintergrundskalarprodukt $\langle\cdot,\cdot\rangle_0$ auf $\mathcal{A}_{\rm PW}$ mit $B_W(a,b)=\langle a,A_Xb\rangle_0$; Rollenklassifikation; Hauptpfad für M4-A.  
**Gesamtausgang:** Kein Kandidat liefert direkt die M4-A-Lösung; Rollenklassifikation $\checkmark[K/M]$; Hauptpfad $\checkmark[K/M]$ identifiziert; Normierungs-Firewall übernommen.  
**Vorgänger:** NEU-253 M4 (Patch), NEU-252 M3 (Patch), NEU-220e, NEU-220w, NEU-221

---

## 0. Ausgangslage

M4-A fragt (NEU-253 \S3):
$$
\boxed{\text{Existiert aus der adelischen/arithmetischen Struktur kanonisch ein positives }\langle\cdot,\cdot\rangle_0\text{ mit }B_W(a,b)=\langle a,A_Xb\rangle_0\,?} \qquad (0\text{-Goal})
$$

Drei Kandidaten aus dem Repo werden systematisch verglichen. Die zentrale Vorbedingung aus NEU-221:

$$
\boxed{\text{Normierungs-Firewall: }\mathcal{N}_X,\tau_X,T_X\text{ müssen quellseitig fixiert sein, bevor Momente getestet werden.}} \qquad (0\text{-Fire})
$$

Nachträgliches Fitten auf $\mu_0,\mu_1$ invalidiert jeden Kandidaten.

---

## 1. Kandidat I: NEU-220e — Semifinite Spur

### 1.1 Was NEU-220e liefert

NEU-220e konstruiert:
$$
\mathcal{N}_\infty=L^\infty(\mathbb{R},dt),\qquad \tau_\infty(M_a)=\int a(t)\,dt,
$$
und die semifinite Realisierung des Gamma-Funktionals:
$$
\Lambda_\Gamma(h)=\frac{1}{2\pi}\tau_\infty(M_{\gamma_\infty h}).
$$

$\gamma_\infty$ wird per Funktionalkalkül eingesetzt; intrinsischer Ursprung von $\gamma_\infty$ ist laut NEU-220e selbst noch offen.

### 1.2 Was NEU-220e nicht liefert

- $\tau_\infty$ ist kein inneres Produkt auf $\mathcal{A}_{\rm PW}$, sondern ein Spurzustand.
- Die Spur realisiert nur den **Gamma-Block** $B_\Gamma$; Polterm $B_{\rm pole}$ und Primzahlpotenzterm $B_{\rm fin}$ fehlen.
- Es gibt kein $\langle a,b\rangle_0$ aus $\tau_\infty$, das $B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}$ vollständig trägt.

### 1.3 Urteil

$$
\boxed{\text{NEU-220e: wertvoller archimedischer Baustein; kein vollständiges M4-A-}\langle\cdot,\cdot\rangle_0.}\quad\checkmark[K/M] \qquad (1\text{-Verdict})
$$

| Kriterium | NEU-220e |
|---|---|
| RH-frei positiv? | $\checkmark$ (lokal, Gamma-Block) |
| Volles $B_W$? | $\times$ (nur $B_\Gamma$) |
| Kanonisch aus Struktur? | $\checkmark$ teilweise ($\gamma_\infty$ noch offen) |
| Rolle | Archimedischer Baustein für $B_\Gamma$ |

---

## 2. Kandidat II: NEU-220w — Moment-GNS

### 2.1 Was NEU-220w liefert

NEU-220w konstruiert aus den $\Xi$-Momenten $\mu_k$ einen Hilbertraum:
$$
\mathcal{H}_\Xi^{\rm mom},\qquad J_\Xi,\qquad M_\Xi(w)=\langle\Omega_\Xi,(I-wJ_\Xi)^{-1}\Omega_\Xi\rangle.
$$

Das ist formal genau der Typ, den M4-A sucht: ein vollständiger Hilbertraum mit Resolventenoperator.

### 2.2 Das RH-Problem

Die benötigte Positivität
$$
\mathcal{L}_\Xi(p^*p)\ge0,\qquad\mathcal{L}_\Xi(xp^*p)\ge0
$$
ist laut NEU-220w selbst **RH-äquivalent**. Ein $\langle\cdot,\cdot\rangle_0$ aus NEU-220w wäre:
$$
\langle p,q\rangle_0:=\mathcal{L}_\Xi(q^*p)\quad\times[M]\text{ als RH-freie Konstruktion.} \qquad (2\text{-Err})
$$

Damit wäre die gesuchte positive Geometrie aus einer RH-äquivalenten Positivität gebaut — das ist die zentrale Firewall aus NEU-253 \S6.

### 2.3 Rolle als Kontrollmodell

NEU-220w beschreibt **sehr präzise**, welchen Typ von Hilbertraumstruktur $\mathcal{H}_\Xi^{\rm mom}$ Objekt X am Ende erzeugen müsste. Es ist damit ein wertvoller **Ziel- und Kontrollrahmen**: Wenn M4-A eine kanonische RH-freie Quelle findet, muss sie denselben Zieltyp reproduzieren.

### 2.4 Urteil

$$
\boxed{\text{NEU-220w: Kontroll- und Zielmodell; keine RH-freie Konstruktionsquelle.}\quad\checkmark[K/M]} \qquad (2\text{-Verdict})
$$

| Kriterium | NEU-220w |
|---|---|
| RH-frei positiv? | $\times$ (RH-äquivalent) |
| Volles $B_W$? | indirekt $\checkmark$ (nach Momentidentitäten) |
| Kanonisch aus Struktur? | $\checkmark$ nach Momentdaten |
| Rolle | Ziel-/Kontrollmodell, keine Konstruktion |

---

## 3. Kandidat III: NEU-221 — Adelische Momentquelle

### 3.1 Was NEU-221 richtig macht

NEU-221 dreht die Richtung korrekt um: nicht Positivität aus $\Xi$ voraussetzen, sondern ein positives BC-/KMS-Objekt finden, dessen Momente anschließend mit den $\Xi$-Momenten übereinstimmen. Normierungs-Firewall: $\mathcal{N}_X,\tau_X,T_X$ zuerst fixieren. Der stärkste Kandidat war:
$$
\boxed{D_{\rm Spec,N}^{\rm rel}=D_{\rm Jac}\cdot D_{\rm scatt},\qquad\text{relativer Feshbach-/Weyl-Sektor + Eulerkanal + archimedischer Kanal.}} \qquad (3\text{-NEU221})
$$

konzeptionell als **gemeinsame relative Determinanten-/Resolventenstruktur**, nicht als direkte Summe.

### 3.2 Was seit NEU-221 gelernt wurde

- $D_{\rm scatt,N}$ war in NEU-250l **nicht als echter Operator konstruiert** (untypisierter Strang).
- Der alte Feshbach-/Wres-Strang hatte Typisierungslücken.
- Andererseits liefern die neuen Strukturen:

$$
P_{\rm Haar},\quad J_{1/2},\quad R_{\rm PW},\quad\text{BC/Frobenius-Primkanal (NEU-250b--h)},\quad\tau_\infty\text{ (NEU-220e)}
$$

viel konkretere Bausteine. Insbesondere ist jetzt $\mathcal{S}_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal{A}_{\rm PW}$ surjektiv (NEU-250r), und die vollständige hermitesche Form $B_W$ ist typkorrekt definiert (NEU-252). Diese Basis hat NEU-221 nicht gehabt.

### 3.3 Technischer Status

NEU-221 ist **konzeptionell der stärkste Pfad**, aber technisch in Teilen überholt:

| Baustein aus NEU-221 | Heutiger Status |
|---|---|
| Normierungs-Firewall | $\checkmark$ unverändert gültig |
| Euler $\mathcal{P}_N(\beta)$ = Mangoldt-Quelle | $\checkmark$ Rolle bestätigt durch NEU-250ff |
| $D_{\rm scatt,N}$ als Operator | $\times[M]$ (NEU-250l untypisiert) |
| Feshbach/Weyl-Quellregion | $\checkmark$ Richtung korrekt, Re-Audit nötig |
| Archimedische Kopplung separat | $\times$ (muss integriert sein, nicht direkte Summe) |
| $T_X=B_X^{-1}\ge0$ als Arbeitsvariable | $\checkmark$ übernehmen |
| Momente $\mu_0,\mu_1,\mu_2$ als Frühtest | $\checkmark$ übernehmen |

### 3.4 Urteil

$$
\boxed{\text{NEU-221: konzeptionell stärkster Pfad; technisch Re-Audit gegen NEU-250ff nötig.}\quad\checkmark[K/M]} \qquad (3\text{-Verdict})
$$

| Kriterium | NEU-221 |
|---|---|
| RH-frei positiv? | Ziel $\checkmark$; noch nicht konstruiert |
| Volles $B_W$? | Ziel $\checkmark$ (Pol+$\Gamma$+Prim aus gemeinsamer Determinante) |
| Kanonisch aus Struktur? | Ziel $\checkmark$; Typisierung partiell offen |
| Rolle | Hauptpfad; technisches Re-Audit fällig |

---

## 4. Vergleichsmatrix

| Kandidat | RH-frei positiv? | Volles $B_W$? | Kanonisch? | Heutiger Status |
|---|---|---|---|---|
| NEU-220e semifinite Spur | $\checkmark$ (Gamma) | $\times$ ($B_\Gamma$ allein) | $\checkmark$ teilw. | Archimedischer Baustein |
| NEU-220w Moment-GNS | $\times$ (RH-äquiv.) | indirekt $\checkmark$ | $\checkmark$ nach Momente | Kontroll-/Zielmodell, Firewall |
| NEU-221 adelische Quelle | Ziel $\checkmark$ | Ziel $\checkmark$ | Ziel $\checkmark$ | Hauptpfad, Re-Audit nötig |

---

## 5. Neue Quelle: $R_{\rm PW}$-Struktur als M4-A-Kandidat

### 5.1 Die zentrale Frage

$$
\boxed{\text{Kann aus }P_{\rm Haar},\,J_{1/2},\,R_{\rm PW},\,\text{BC/Frobenius-Primkanal},\,\tau_\infty\text{ ein positives }\langle a,b\rangle_0\text{ gebaut werden, bevor }B_W\text{ hineinkommt?}} \qquad (5\text{-Core})
$$

Das wäre viel stärker als NEU-220w als GNS-Lösung zu nehmen.

### 5.2 Kandidatenbausteine

**Haarsches $L^2$-Produkt auf $\mathcal{S}_{\rm adel}^{\rm amp}$:**
$$
\langle F,G\rangle_{\rm Haar}:=\int_{\mathbb{A}_\mathbb{Q}}F(x)\overline{G(x)}\,d\mu_{\rm Haar}(x). \qquad (5\text{-Haar})
$$
Positiv, kanonisch, adelisch. Zu prüfen: Ist $B_W^{\rm adel}(F,G)=\langle F,A_X^{\rm adel}G\rangle_{\rm Haar}$ für einen beschränkten oder abschließbaren $A_X^{\rm adel}$?

**Port-Transport:**
Mittels $R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal{A}_{\rm PW}$ könnte das Haar-Produkt auf $\mathcal{A}_{\rm PW}$ transportiert werden:
$$
\langle a,b\rangle_0:=\langle R_{\rm PW}^{-1}a,R_{\rm PW}^{-1}b\rangle_{\rm Haar}. \qquad (5\text{-Transport})
$$
Vorbedingung: $R_{\rm PW}$ ist surjektiv, aber nicht injektiv auf der vollen Sadelamp; Rechts-Inverse muss kontrolliert gewählt werden.

**BC/Frobenius-Primkanal:**
Der Frobenius-Primkanal aus NEU-250b--h liefert die von-Mangoldt-Gewichte. Ob er ein positives Skalarprodukt trägt, hängt von seiner Darstellung als positiver Spurzustand ab — das ist der direkte Anschluss an die NEU-221-Idee mit neuem Typenrahmen.

### 5.3 Status

$$
\text{Haar-Transport-Kandidat: }?[O]\text{ (Beschränktheit/Abschließbarkeit von }A_X^{\rm adel}\text{ unklar)} \qquad (5\text{-status})
$$

---

## 6. M4-A Hauptpfad

$$
\boxed{\text{Hauptpfad M4-A: NEU-221-Idee vollständig gegen NEU-250ff re-auditiert.}} \qquad (6\text{-Main})
$$

Konkret:

1. **NEU-221-Strukturprinzip übernehmen:** $T_X=B_X^{-1}\ge0$; Normierungs-Firewall; Momente $\mu_0,\mu_1,\mu_2$ als Frühtests.
2. **Bausteine neu typisieren:** $P_{\rm Haar}$, $J_{1/2}$, $R_{\rm PW}$, BC/Frobenius-Primkanal (NEU-250b--h), $\tau_\infty$ (NEU-220e) als neue Quellarsenal.
3. **$D_{\rm scatt,N}$ nicht verwenden:** NEU-250l $\times[M]$; Feshbach-/Weyl-Quellregion nur nach Re-Typisierung.
4. **Gemeinsame Determinantenstruktur:** Pol + $\Gamma$ + Prim sollen aus einer einzigen kanonischen Resolventenstruktur kommen, nicht als direkte Summe.
5. **Haar-Transport prüfen:** $\langle\cdot,\cdot\rangle_{\rm Haar}$ auf $\mathcal{S}_{\rm adel}^{\rm amp}$ als Majorante; $A_X^{\rm adel}$ Beschränktheit/Abschließbarkeit via NEU-253 \S3-Kette.
6. **NEU-220w als Kontrollmodell:** Am Ende muss $\langle\cdot,\cdot\rangle_0$ denselben Typ wie $\mathcal{H}_\Xi^{\rm mom}$ reproduzieren.

---

## 7. Statusbuchungen

$$\text{NEU-220e: Gamma-Block-Baustein, kein vollständiges M4-A-}\langle\cdot,\cdot\rangle_0\quad\checkmark[K/M] \qquad (7\text{-a})$$
$$\text{NEU-220w: Kontroll-/Zielmodell; Konstruktionsquelle }\times[M]\text{ (RH-äquivalent)}\quad\checkmark[K/M] \qquad (7\text{-b})$$
$$\text{NEU-221: konzeptionell stärkster Pfad; }D_{\rm scatt,N}\;\times[M]\text{; Normierungs-Firewall }\checkmark\quad\checkmark[K/M] \qquad (7\text{-c})$$
$$\text{Haar-Transport-Kandidat: }?[O] \qquad (7\text{-d})$$
$$\text{M4-A-Hauptpfad identifiziert (neo-NEU-221 gegen NEU-250ff)}\quad\checkmark[K/M] \qquad (7\text{-e})$$
$$\text{M4-A gesamt}\quad?[O] \qquad (7\text{-M4A})$$

---

## 8. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-253 | a95d3b5 | M4 Rahmen; Rad, Signatur-Firewall, M4-A Zwei-Fälle |
| NEU-252 (Patch) | 4ee78ed | $B_W$ hermitesch; $B_W^{\rm adel}$ |
| NEU-220e | 9a1f3c2 | Semifinite Spur $\tau_\infty$; $\Lambda_\Gamma$ |
| NEU-220w | f1bce0f | Moment-GNS; $\mathcal{H}_\Xi^{\rm mom}$; Hankel-RH-Modell |
| NEU-221 | f678057 | Adelische Momentquelle; Normierungs-Firewall; $T_X=B_X^{-1}$ |
| NEU-250b--h | div. | BC/Frobenius-Primkanal |
| NEU-250r (Patch) | bd1c0ab | $R_{\rm PW}$ surjektiv; $\mathcal{S}_{\rm adel}^{\rm amp}$ |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
