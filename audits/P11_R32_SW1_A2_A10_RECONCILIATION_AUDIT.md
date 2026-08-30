# P11/R32 — SW1 A2–A10 Reconciliation Audit

> **Stand:** 30. August 2026  
> **Basis:** \`main@cf1cee4b9befc2b9c97b06cb58504485c8ad5e71\`  
> **Status:** Auditkandidat; keine Promotion.  
> **Ziel:** rückwärts prüfen, an welcher Stelle die vorhandene A2–A10-Kette erstmals keine echte Implikation mehr in Richtung \(\ker\Gamma_I=\{0\}\) liefert, und den heute kleinsten noch offenen Nichtentartungssatz isolieren.  
> **Scope-Firewall:** keine neue Injektivitäts-, HT-RED-, Objekt-X- oder RH-Aussage.

---

## 0. Ergebnis in einem Satz

Es gibt zwei verschiedene, beide relevante Bruchpunkte:

\[
\boxed{
\textbf{historischer/logischer Bruchpunkt: A3}\to\text{A4}
}
\]

und

\[
\boxed{
\textbf{heutiger operativer Restgate: Nichtentartung des A10-M1-Cocycles}.
}
\]

A2 und A3 liefern echte Kerneläquivalenzen bzw. exakte Koordinatisierungen.  
A4–A9 liefern danach Struktur-/Strategieaussagen über Punktgraphen, Rotation, Separatoren und Bypässe, aber **keinen** neuen Satz der Form „Kernel trivial“.  
A10 nimmt denselben offenen Kernel wieder auf, entfernt das Inverse, fiberisiert ihn und stellt den tatsächlichen Operator vollständig als finite-range M1-Cocycle dar. Die noch fehlende Aussage ist daher heute:

\[
\boxed{
\mathscr C_R(\xi,w)=0
\Longrightarrow
\xi=w=0.
}
\tag{REC.1}
\]

Äquivalent, nach C1C1/C2:

\[
\boxed{
\widehat{\mathscr C}_R F=0
\Longrightarrow
F=0.
}
\tag{REC.2}
\]

Und in der M1-Darstellung:

\[
\boxed{
\sum_{j=-3}^{3}M_j(\theta)\,F(\theta+j\Delta)=0
\quad\text{a.e.}
\Longrightarrow
F=0
}
\tag{REC.3}
\]

auf dem **tatsächlichen Hilbert-Bildraum** der C1C1-Fiberisierung, nicht auf einem frei erfundenen \(\mathbb C^{24}\)-Produkt ohne Bildbedingung.

---

# Teil I — Welche Schritte sind echte Äquivalenzen?

## 1. A-FOLD / A0 / A1

PR #38 schließt die Odd/even-Brücke:

\[
\boxed{
\ker\mathcal K_{I,A}
=
\{0\}
\iff
\ker\widehat{\mathcal K}_{I,A}
=
\{0\}.
}
\tag{REC.4}
\]

A0 und A1 liefern danach die exhaustive freie Zellzerlegung und das vollständige operatorwertige Rohsystem der ersten augmentierten Gleichung.

Diese Stufe ist **keine** offene Injektivitätsfrage mehr; sie ist die kanonische Darstellungsebene.

---

## 2. A2 — exakte Annulus-/Cross-Gram-Kernelreduktion

A2 definiert

\[
\mathscr T:=I+A,
\qquad
K:=\ker(E_I^*H|_{\mathscr H_+}),
\qquad
G:=P_K\mathscr T|_K
\]

und den inversenfreien Annulusoperator

\[
\boxed{
\mathcal L_{\rm ann}^{\rm SW1}
=
\left[
I-\mathscr T
\bigl(P_K\mathscr T|_K\bigr)^{-1}P_K
\right]
HE_{\mathcal A}.
}
\tag{REC.5}
\]

A2 beweist eine echte Kernelbijektion

\[
\boxed{
\ker\mathcal L_{\rm ann}^{\rm SW1}
\xrightarrow{\sim}
\ker\mathcal K_{I,A}.
}
\tag{REC.6}
\]

Ferner gilt exakt

\[
\boxed{
\ker\mathcal L_{\rm ann}^{\rm SW1}
=
\ker\Gamma_I.
}
\tag{REC.7}
\]

Mit P12-RT auf SW1 kann dieselbe Frage als Bildraumtransversalität formuliert werden:

\[
\boxed{
\ker\Gamma_I=\{0\}
\iff
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+A)K
=
\{0\}.
}
\tag{REC.8}
\]

**Auditurteil A2:** echte Reduktion/Äquivalenz; keine Injektivität.

---

## 3. A3 — exakte KNF-Gram-Koordinatisierung

A3 setzt

\[
J_R:=\Psi_R^{-1}:\mathcal F_R\to K
\]

und

\[
\boxed{
\mathfrak G_R
=
J_R^*(I+A)J_R.
}
\tag{REC.9}
\]

A3 beweist

\[
\mathfrak G_R
\ge
\|\Psi_R\|^{-2}I
\]

und damit

\[
\boxed{
\mathfrak G_R^{-1}\in\mathcal B(\mathcal F_R).
}
\tag{REC.10}
\]

Außerdem:

\[
\boxed{
G^{-1}P_K
=
J_R\mathfrak G_R^{-1}J_R^*.
}
\tag{REC.11}
\]

Somit wird der Annulusoperator exakt

\[
\boxed{
\mathcal L_{\rm ann}^{\rm SW1}
=
\left[
I-(I+A)
J_R\mathfrak G_R^{-1}J_R^*
\right]
HE_{\mathcal A}.
}
\tag{REC.12}
\]

A3 sagt selbst ausdrücklich, dass offen bleibt:

\[
\boxed{
\text{konkrete Wirkung von }
\mathfrak G_R^{-1}
\text{ auf }
J_R^*HE_{\mathcal A}w
}
\tag{REC.13}
\]

und anschließend die Injektivität von REC.12.

**Auditurteil A3:** letzte Stufe der ursprünglichen Kette, die noch eine exakte Operator-/Kernelreduktion liefert. Keine Injektivität.

---

# Teil II — Wo endet die Implikationskette?

## 4. A4 — erster logischer Bruch

A4 beweist:

- einen konkreten irrationalen Rotationsmechanismus im oberen SW1-Chamber;
- daraus ein No-Go gegen eine exhaustive Zerlegung in endliche physische Punktorbits.

A4 beweist ausdrücklich **nicht**:

\[
\ker\Gamma_I\ne0,
\qquad
\ker\Gamma_I=0,
\]

und auch keine Eigenschaft von \(\mathfrak G_R^{-1}\), die REC.12 entscheidet.

Damit ist der Übergang

\[
\boxed{
\text{A3}\to\text{A4}
}
\tag{REC.14}
\]

der **erste Punkt, an dem die historische Roadmap keine echte Implikationskette Richtung Injektivität mehr ist**.

A4 ist eine Strategierevision:

\[
\text{„finite Punktorbit-Determinanten reichen nicht“},
\]

kein neuer Kernelabschluss.

---

## 5. A5–A8 — Struktur, aber kein Kernelabschluss

### A5

Zwei-Blatt-Normalform der Echoabbildungen über irrationaler Basisrotation.

**Keine** Endlichkeits- oder Injektivitätsaussage.

### A6

Der kontrahierte A4-Rotationssubgraph besitzt im unteren Chamber ein offenes Hole und endliche kontrahierte Segmente.

**Keine** Aussage über die vollständige A1/A3-Komponente.

### A7

Der vollständige rohe A1-Punktgraph im unteren Chamber ist ein

\[
6\text{-State-, Range-3-Cocycle}
\]

über derselben irrationalen Rotation.

Das ist eine endliche Transferbeschreibung, aber noch keine Komponentendlichkeit und keine Injektivität.

### A8

Für den vollständigen **rohen A1-Punktgraphen** im unteren Chamber werden endliche Komponenten durch wiederkehrende Separatoren bewiesen.

Aber:

\[
\boxed{
\text{roher A1-Punktgraph}
\neq
\text{freier Gramgraph}
\neq
\ker\Gamma_I.
}
\tag{REC.15}
\]

A8 schließt daher keine Kerneltrivialität.

---

## 6. A9 — der freie Gramgraph ist selbst nicht global geschlossen

A9 untersucht die durch \(J_R^*(I+A)J_R\) erzeugten Zusatzkanten.

Der aktuelle Status ist:

\[
\boxed{\mathrm{A9\!-\!SEP}:?[O].}
\tag{REC.16}
\]

Zertifiziert sind unter anderem:

- J0/J1;
- vollständiger paritätserweiterter finite-state Cocycle;
- Gate-/Domainledger;
- \(\mathrm{SEP\!-\!SMALL}\) im kleinen unteren Subchamber.

Aber im komplementären unteren Bereich existiert ein partieller Bypass und die globale Separatorentscheidung bleibt offen.

Entscheidend für den Reconciliation-Audit:

Selbst ein globaler Abschluss von A9 zu „alle freien Gram-Punktkomponenten endlich“ würde **noch nicht automatisch**

\[
\ker\Gamma_I=\{0\}
\]

liefern. Er würde nur eine endliche Blockstrategie legitimieren.

A10-H1/H2/H3 zeigt zudem, dass gemeinsame Annulusvariablen getrennte freie Komponenten wieder verbinden können.

---

# Teil III — Warum A10 den alten A3-Bruch umgeht, aber nicht schließt

## 7. A10-C0 — inversefreie Rückkehr zur echten Kernelgleichung

A10-C0 setzt

\[
\boxed{
\mathscr C_R:
\mathcal F_R\oplus\mathscr W
\to
\mathscr H_+,
\qquad
\mathscr C_R(\xi,w)
=
(I+A)J_R\xi
+
HE_{\mathcal A}w.
}
\tag{REC.17}
\]

Definiere
\[
\Theta:=J_R\oplus I_{\mathscr W}:
\mathcal F_R\oplus\mathscr W
\longrightarrow
K\oplus\mathscr W.
\tag{REC.17a}
\]
Da \(J_R=\Psi_R^{-1}\) ein beschränkter Isomorphismus ist, ist die Umkehrabbildung **explizit**
\[
\boxed{
\Theta^{-1}(y,w)
=
(\Psi_Ry,w),
\qquad
(y,w)\in K\oplus\mathscr W.
}
\tag{REC.17b}
\]
Somit gelten beidseitig
\[
\boxed{
\Theta^{-1}\Theta=I_{\mathcal F_R\oplus\mathscr W},
\qquad
\Theta\Theta^{-1}=I_{K\oplus\mathscr W}.
}
\tag{REC.17c}
\]

Außerdem
\[
\mathcal K_{I,A}\Theta(\xi,w)
=
(\mathscr C_R(\xi,w),0).
\tag{REC.17d}
\]
Daher ist die Einschränkung
\[
\Theta:
\ker\mathscr C_R
\longrightarrow
\ker\mathcal K_{I,A}
\]
nicht nur injektiv, sondern bijektiv mit der expliziten Rückabbildung
\[
\boxed{
(y,w)\longmapsto(\Psi_Ry,w).
}
\tag{REC.17e}
\]

Wichtig: Hier wird \(\mathfrak G_R^{-1}\) **nicht** mehr benötigt.

Da

\[
J_R:\mathcal F_R\xrightarrow{\sim}K
\]

bijektiv ist, folgt exakt

\[
\boxed{
\ker\mathscr C_R
\xrightarrow{\sim}
\ker\mathcal K_{I,A}
\xrightarrow{\sim}
\ker\Gamma_I.
}
\tag{REC.18}
\]

Also:

\[
\boxed{
\ker\Gamma_I=\{0\}
\iff
\ker\mathscr C_R=\{0\}.
}
\tag{REC.19}
\]

Das ist der entscheidende Reconciliation-Punkt:

> Die heute beste Form des offenen Problems benötigt **keine explizite Berechnung von \(\mathfrak G_R^{-1}\)** mehr.

Damit ist A3.13 historisch der erste offene Punkt, aber nicht mehr der beste heutige Angriffspunkt.

---

## 8. A10-C1C1 — echte Hilbert-Fiberisierung

C1C1 konstruiert isometrische Mehrblattabbildungen auf ihre geschlossenen Bildräume. Setze
\[
\mathcal R_K:=U_HK,
\qquad
\mathcal R_W:=U_W\mathscr W
\]
und den Domain-Transport
\[
\boxed{
W:=(U_H|_K)\oplus U_W:
K\oplus\mathscr W
\longrightarrow
\mathcal R_K\oplus\mathcal R_W.
}
\tag{REC.20a}
\]
Per Definition der Bildräume ist \(W\) surjektiv auf
\(\mathcal R_K\oplus\mathcal R_W\), und wegen der Isometrie beider Summanden injektiv. Die Umkehrabbildung ist explizit
\[
\boxed{
W^{-1}(F,G)
=
\bigl((U_H|_K)^{-1}F,\ U_W^{-1}G\bigr).
}
\tag{REC.20b}
\]
Damit
\[
\boxed{
W^{-1}W=I_{K\oplus\mathscr W},
\qquad
WW^{-1}=I_{\mathcal R_K\oplus\mathcal R_W}.
}
\tag{REC.20c}
\]

Der transportierte Operator ist
\[
\widehat{\mathscr C}_R
=
U_H\,\widetilde{\mathscr C}_R\,W^{-1}
\quad
\text{auf }\mathcal R_K\oplus\mathcal R_W.
\tag{REC.20d}
\]
Daher gilt für \(X\in K\oplus\mathscr W\)
\[
\widehat{\mathscr C}_R(WX)
=
U_H\widetilde{\mathscr C}_R X.
\tag{REC.20e}
\]
Da \(U_H\) injektiv ist,
\[
\widetilde{\mathscr C}_R X=0
\iff
\widehat{\mathscr C}_R(WX)=0.
\]
Umgekehrt besitzt **jedes**
\[
(F,G)\in\mathcal R_K\oplus\mathcal R_W
\]
eindeutig den Rücktransport
\[
X=W^{-1}(F,G),
\]
so dass es auf dem Definitionsraum keine künstlichen Fibervektoren gibt. Folglich
\[
\boxed{
W:
\ker\widetilde{\mathscr C}_R
\xrightarrow{\sim}
\ker\widehat{\mathscr C}_R
}
\tag{REC.20f}
\]
mit explizitem inversen Kerneltransport \(W^{-1}\).

Zusammen mit C0:
\[
\boxed{
\ker\widehat{\mathscr C}_R
\cong
\ker\mathscr C_R
\cong
\ker\Gamma_I.
}
\tag{REC.20}
\]

**Wichtige Ambient-Firewall:** \(WW^{-1}=I\) gilt ausschließlich auf
\[
\mathcal R_K\oplus\mathcal R_W.
\]
Auf dem größeren formalen Slot-Ambientraum ist \(WW^{-1}\) nur die Rückprojektion auf den gültigen Bild-/Konsistenzraum und im Allgemeinen **nicht** die Identität. Ein M1-ND-Test darf daher nur auf
\[
\boxed{\mathcal R_K\oplus\mathcal R_W}
\tag{REC.20g}
\]
oder einer exakt äquivalent parametrisierten Darstellung dieses Raums geführt werden.

---

## 9. A10-C2 / M1-FULL — vollständige Operatorrepräsentation

C2 baut die sieben Operatorlagen

\[
j=-3,-2,-1,0,1,2,3.
\]

Am Referenzwert \(r_0=7/2\) ist exhaustiv auf

\[
64\times96=6144
\]

offenen Parameter-/Kreisatomen geprüft, dass die physische Operatorseite und das M1-Ledger als vollständige symbolische Beitragsmultimengen übereinstimmen.

Durch C1B2A-TRANSFER gilt dieselbe M1-FULL-Struktur für jedes tatsächliche

\[
3<r<4.
\]

Damit ist im dokumentierten a.e.-Scope die finite-range Darstellung kanonisch:

\[
\boxed{
(\widehat{\mathscr C}_R F)(\theta)
=
\sum_{j=-3}^{3}
M_j(\theta)
F(\theta+j\Delta).
}
\tag{REC.21}
\]

Hier endet die bisherige Konstruktion.

M1-FULL beweist:

\[
\boxed{
\text{„Das ist der richtige Operator.“}
}
\]

M1-FULL beweist **nicht**:

\[
\boxed{
\text{„Dieser Operator ist injektiv.“}
}
\]

---

# Teil IV — Der erste heute wirklich offene Satz

## 10. Minimaler aktueller Gate

Nach A-FOLD + A2 + C0 + C1C1 + M1-FULL ist die offene Frage exakt:

\[
\boxed{
\mathrm{M1\!-\!ND}:
\quad
\widehat{\mathscr C}_R F=0
\Longrightarrow
F=0
}
\tag{REC.22}
\]

auf dem tatsächlichen C1C1-Bildraum, für den SW1-Scope und den tatsächlichen Projektwert \(3<r<4\).

Äquivalent:

\[
\boxed{
\mathscr C_R(\xi,w)=0
\Longrightarrow
\xi=w=0.
}
\tag{REC.23}
\]

Äquivalent:

\[
\boxed{
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+A)K
=
\{0\}.
}
\tag{REC.24}
\]

Äquivalent:

\[
\boxed{
\ker\Gamma_I=\{0\}.
}
\tag{REC.25}
\]

Diese vier Aussagen sind nach den bereits auditierten Reconciliation-Schritten dieselbe mathematische Aufgabe.

---

## 11. Was jetzt NICHT mehr zuerst gelöst werden muss

Vor REC.22 muss nicht erneut bewiesen werden:

1. P12 im offenen Low-Radius-unrestricted-tail-Gebiet;
2. A0/A1-Coverage;
3. A2-Kernelreduktion;
4. die explizite Wirkung von \(\mathfrak G_R^{-1}\);
5. globale A9-Komponentendlichkeit;
6. Endlichkeit der augmentierten Hubkomponenten;
7. eine ambient isotopy der C1B2A-Arrangements;
8. die M1-Matrixkonstruktion.

Diese Punkte sind entweder bereits geschlossen, für SW1 nicht erforderlich oder durch den inversefreien C0/M1-Weg umgangen.

---

# Teil V — Welcher Nichtentartungstest ist als Nächstes zulässig?

## 12. Nicht einfach „punktweise Matrixrang“

REC.21 ist ein **finite-range Cocycle**

\[
\sum_{j=-3}^{3}M_j(\theta)U_\Delta^j,
\]

kein Multiplikationsoperator \(M_0(\theta)\).

Daher genügt im Allgemeinen weder

\[
\det M_0(\theta)\ne0
\]

noch der Rang einer einzelnen \(12\times24\)-Matrixlage.

Die Verschiebungen

\[
F(\theta+j\Delta)
\]

koppeln verschiedene Basispunkte entlang der irrationalen Rotation.

---

## 13. Der korrekte nächste Prüfgegenstand

Der nächste Audit sollte daher nicht „A4 nochmals“ heißen, sondern die **Nichtentartung des vollständigen siebenlagigen Cocycles** untersuchen.

Minimal zu klären sind:

### ND-1 — echter Zustandsraum

Die C1C1-Bild-/Konsistenzbedingungen des redundanten Covers müssen als geschlossener invariant(er) Zustandsraum explizit in die M1-Gleichung eingesetzt werden.

### ND-2 — Transfergleichung

Aus

\[
\sum_{j=-3}^{3}M_j(\theta)F(\theta+j\Delta)=0
\]

ist eine äquivalente finite-state Transfer-/Recurrenceform abzuleiten, ohne unzulässige Inversion eines möglicherweise singulären Außenblocks.

### ND-3 — Nichtentartungsalternative

Danach muss genau eine der beiden Richtungen geschlossen werden:

\[
\boxed{
F=0
}
\]

für jede zulässige \(L^2\)-Lösung,

oder ein exakter nichttrivialer zulässiger

\[
\boxed{
F\ne0,\qquad
\widehat{\mathscr C}_RF=0.
}
\]

---

## 14. Statusmatrix A2–A10

| Stufe | Was ist wirklich bewiesen? | Hilft direkt zu \(\ker\Gamma_I=0\)? | Rest |
|---|---|---:|---|
| A2 | exakte Annulus-/Cross-Gram-Kernelbijektion | **ja, als Äquivalenz** | Injektivität offen |
| A3 | positiver freier Gramoperator + exakte Koordinatisierung | **ja, als Darstellung** | Wirkung von \(\mathfrak G_R^{-1}\) / Injektivität offen |
| A4 | irrationaler Punktorbit-No-Go | nein | Strategiefrage |
| A5 | Zwei-Blatt-Normalform | nein | Dynamik offen |
| A6 | Hole + endliche kontrahierte Segmente | nein | volle Komponente offen |
| A7 | voller roher A1 finite-state Cocycle | nein | Bypass/Separator offen |
| A8 | endliche rohe A1-Komponenten im unteren Chamber | nein | KNF-/Cross-Gram-Kopplung fehlt |
| A9 | freier KNF-Cocycle; SEP-SMALL teilweise geschlossen | nein | A9 gesamt offen |
| A10-H | augmentierte Hub-Bridge/irrationale Komponente | nein | zeigt Grenze endlicher Blockstrategie |
| A10-C0 | inversefreie Kernelbijektion \(\ker\mathscr C_R\cong\ker\Gamma_I\) | **ja, als Äquivalenz** | \(\mathscr C_R\)-Injektivität offen |
| A10-C1C1 | Hilbert-Fiberisierung mit Kernelintertwining | **ja, als Äquivalenz** | fiberisierter Operator noch zu testen |
| A10-C2/M1 | vollständige tatsächliche-\(r\) finite-range Matrixdarstellung | **ja, als exakte Darstellung** | **Nichtentartung offen** |

---

## 15. Reconciliation-Verdict

### Historisch

Die ursprüngliche lineare Roadmap

\[
A2\to A3\to A4\to\cdots
\]

hört **nach A3** auf, eine echte logische Implikationskette zur Injektivität zu sein.

\[
\boxed{
\mathrm{FIRST\ HISTORICAL\ BREAK}
=
A3\to A4.
}
\tag{REC.26}
\]

### Operativ heute

A10 hat die offene A3-Frage nicht durch Berechnung von \(\mathfrak G_R^{-1}\) gelöst, sondern durch eine bessere inversefreie Repräsentation umgangen.

Nach M1-FULL ist der kleinste verbleibende mathematische Gate:

\[
\boxed{
\mathrm{M1\!-\!ND}:
\ker\widehat{\mathscr C}_R=\{0\}\ ?
}
\tag{REC.27}
\]

Dies ist äquivalent zu

\[
\boxed{
\ker\Gamma_I=\{0\}\ ?
}
\]

und ist der erste Punkt, an dem jetzt wirklich neue Nichtentartungsmathematik benötigt wird.

---


## 16. Reproduzierbares Bijektivitäts-Hardening

Zusätzlich zu den bereits existierenden Einzelzertifikaten wird für diesen Reconciliation-Audit ein separates algebraisch/mechanisches Zertifikat geführt:

\[
\boxed{
\texttt{scripts/certify\_sw1\_a2\_a10\_kernel\_bijections.py}.
}
\tag{REC.28}
\]

Es prüft in exakten rationalen nichttrivialen Modellen:

1. \(J_R\Psi_R=I_K\) und \(\Psi_RJ_R=I_{\mathcal F_R}\);
2. \(\Theta^{-1}\Theta=I\) und \(\Theta\Theta^{-1}=I\);
3. die Vorwärts- und Rückrichtung der C0-Kernelparametrisierung;
4. für tall isometrische Embeddings \(U_H,U_W\):
   \[
   W^{-1}W=I;
   \]
5. für jeden Vektor \(Y\in\operatorname{Ran}W\):
   \[
   WW^{-1}Y=Y;
   \]
6. ausdrücklich:
   \[
   WW^{-1}\ne I
   \]
   auf dem größeren Ambientraum im Testmodell;
7. die Kernelidentität
   \[
   \ker \widehat C
   =
   W(\ker C)
   \]
   in einem Modell mit **nichttrivialem Kernel**, damit nicht nur der triviale Nullfall getestet wird.

**Scope-Firewall:** Das Skript zertifiziert das endliche lineare-Algebra-/Intertwining-Skelett. Die unendlichdimensionale Tatsache, dass Isometrien geschlossene Bildräume besitzen und auf ihre Bilder unitär/bijektiv sind, bleibt der bereits separat geprüfte Hilbertraumsatz. Das Skript ersetzt diesen analytischen Beweis nicht.

---

## 17. Firewall

Dieser Audit:

- promotet A2–A10 nicht;
- schließt A9 nicht;
- behauptet keine Endlichkeit augmentierter Komponenten;
- behauptet keine Injektivität von M1;
- benutzt M1-FULL nur als Operatoridentifikation;
- benutzt C1B2A-TRANSFER nur im bereits gebuchten a.e.-Scope;
- erzeugt keinen HT-RED-, Objekt-X- oder RH-Schluss.

Der nächste Review-Knoten sollte ausschließlich REC.27 angreifen.
