# NEU-220 — Eröffnung des archimedischen Weil-/Gammafaktorpfads

**Stand:** 2026-08-05  
**Repository:** Waschtl904/objekt-x-programm  
**Typ:** Knoteneröffnung und strategische Firewall  
**Vorgänger:** NEU-219 (eingefroren, Commit fbbf62c)

---

## Ausgangsstand

Der algebraische geladene Hochschildkern ist abgeschlossen:
$$
[D_g^{\mathrm{corr}}]\smile[\Theta^\wedge]\neq0
\quad\text{in}\quad
HH^4\!\left(A_{\mathrm{alg}},\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g.
$$
Der kanonische Basislift $\widetilde{L}_0\in Z^4(A_{\mathrm{alg}},I_0)$ ist typkorrekt, besitzt aber keine globale konstante Rotationseigenrelation:
$$
t\Phi_0\neq C\Phi_0\qquad\forall C\in\mathbb{C}.
$$
Der zyklische Ersatzrepräsentantenpfad wurde nach $[O\text{-}220\text{-}2]$ exportiert und blockiert den Hauptpfad nicht.

$$\boxed{[O\text{-}220\text{-}1]\quad\text{Archimedischer Weil-/Gammafaktorkanal}}$$

---

## 1. Ziel von $[O\text{-}220\text{-}1]$

Gesucht sind:
- Ein präziser Quellraum $\mathcal{S}_\infty$.
- Ein archimedischer Ziel- oder Hilbertraum $H_\infty$.
- Eine stetige archimedische Funktional- bzw. Kanalabbildung
$$
\Lambda_\infty:\mathcal{S}_\infty\longrightarrow\mathbb{C}
\qquad\text{oder stärker}\qquad
T_\infty:\mathcal{S}_\infty\longrightarrow H_\infty,
$$
sodass der Gammafaktorbeitrag der expliziten Formel exakt reproduziert wird.

Die Zielidentität lautet zunächst abstrakt:
$$
\boxed{Q_\infty(f,h) = \langle T_\infty f,T_\infty h\rangle_{H_\infty} - R_\infty(f,h),}
$$
wobei ausdrücklich zu entscheiden ist:
- ob $R_\infty=0$ möglich ist;
- ob $R_\infty$ endlichdimensional ist;
- ob $R_\infty$ mit dem Polterm gekoppelt werden muss;
- oder ob der archimedische Beitrag isoliert keine positive Gram-Realisierung besitzt.

**Eine Positivitätsbehauptung wird zu Beginn nicht vorausgesetzt.**

---

## 2. Normalisierungs-Firewall

Vor jeder Operator- oder Hilbertraumkonstruktion müssen folgende Daten verbindlich fixiert werden.

### 2.1 Testfunktionskonvention

Es ist genau eine Fourier- bzw. Mellinkonvention festzulegen. Arbeitsschema (noch nicht verbindlich):
$$
\hat{f}(t) = \int_{\mathbb{R}} f(u)\,e^{-itu}\,du,
$$
mit expliziter Festlegung aller $2\pi$-Faktoren. Zusätzlich ist die Involution zu definieren:
$$
f^\sharp(u) = \overline{f(-u)}.
$$
Der positive Testausdruck ist anschließend $f^\sharp * f$. Solange diese Konventionen nicht fixiert sind, dürfen **keine Konstanten im Gamma-Term als verbindlich verbucht werden**.

### 2.2 Trennung der Beiträge

Die explizite Formel ist in drei unterschiedliche Bestandteile zu zerlegen:
$$
Q_W(f,h) = Q_{\mathrm{prime}}(f,h) + Q_\infty(f,h) + Q_{\mathrm{pole}}(f,h).
$$
Nicht stillschweigend zu vermischen:
- der Gammafaktor;
- der Faktor $\pi^{-s/2}$;
- die Pole bei $s=0,1$;
- Normierungskonstanten der Fouriertransformation.

Eine mögliche Positivität von $Q_\infty+Q_{\mathrm{pole}}$ darf nicht fälschlich als Positivität von $Q_\infty$ allein ausgegeben werden.

### 2.3 Archimedische Distribution

Zunächst ist eine Distribution $W_\infty\in\mathcal{S}_\infty'$ zu definieren, sodass:
$$
\boxed{Q_\infty(f,h) = \langle W_\infty, h^\sharp * f\rangle.}
$$
Die Definition muss exakt aus der logarithmischen Ableitung des archimedischen Faktors der vervollständigten Zetafunktion abgeleitet werden. Die zu auditierende Struktur ist schematisch:
$$
\frac{d}{ds}\log\!\left(\pi^{-s/2}\Gamma(s/2)\right),
$$
aber Argumente, Vorzeichen, reelle Teile und Normierungskonstanten sind erst nach vollständigem Formelaudit verbindlich.

---

## 3. Kandidat für den Quellraum

Als erster Arbeitskandidat:
$$
\boxed{\mathcal{S}_\infty^{(0)} = C_c^\infty(\mathbb{R})}
$$
mit der üblichen LF-Topologie und der Involution $f^\sharp(u)=\overline{f(-u)}$.

**Vorteile:**
- Faltungsstabilität: $f,h\in C_c^\infty(\mathbb{R})\Rightarrow f*h\in C_c^\infty(\mathbb{R})$, die Ausdrücke $f^\sharp*f$ sind wohldefiniert.
- Primzahlpotenzterme $f(m\log p)$ sind für jedes feste $f$ endlich unterstützt.

Eine Erweiterung auf $\mathcal{S}(\mathbb{R})$ oder einen gewichteten Sobolevraum ist erst nach dem Distributionsaudit zu entscheiden.

$$\boxed{[O\text{-}220\text{-}1a\text{-source}]\quad?[O]}$$

---

## 4. Erste zu beweisende Identität

Die archimedische sesquilineare Form soll aus der Distribution durch Polarisation entstehen:
$$
Q_\infty(f,h) = \Lambda_\infty(h^\sharp * f).
$$
Dann gilt automatisch $Q_\infty(f,h)=\overline{Q_\infty(h,f)}$ genau dann, wenn die Distribution die erforderliche Realitätssymmetrie besitzt.

Der erste echte mathematische Test ist daher nicht Positivität, sondern:
$$
\boxed{Q_\infty\text{ ist wohldefiniert, stetig und hermitesch auf }\mathcal{S}_\infty.}
$$

$$\boxed{[O\text{-}220\text{-}1b\text{-Herm}]\quad?[O]}$$

---

## 5. Positivitätsklassifikation

Erst nach Abschluss der Hermiteschheit ist zu entscheiden, welcher Fall gilt:

| Fall | Bedingung | Konsequenz |
|---|---|---|
| **A** | $Q_\infty(f,f)\ge0\;\forall f$ | GNS-Konstruktion: $H_\infty=\overline{\mathcal{S}_\infty/\mathcal{N}_\infty}^{Q_\infty}$ |
| **B** | $\exists$ endlichdim. $R_\infty$: $Q_\infty+R_\infty\ge0$ | $\langle T_\infty f,T_\infty h\rangle = Q_\infty(f,h)+R_\infty(f,h)$ |
| **C** | Nur $Q_\infty+Q_{\mathrm{pole}}\ge0$ (oder endl. Defekt) | Archimedischer Kanal nur mit Polterm realisierbar |
| **D** | Unendlicher negativer Index | Keine isolierte positive Hilbertraumrealisierung; Kre\u012bnstruktur nicht ausreichend |

$$\boxed{[O\text{-}220\text{-}1c\text{-positivity}]\quad?[O]}$$

---

## 6. Spektraler Kandidat

Falls sich der Gamma-Term nach Fouriertransformation in der Form
$$
Q_\infty(f,h) = \int_{\mathbb{R}} \hat{h}(t)\,\overline{\hat{f}(t)}\,w_\infty(t)\,dt + R_\infty(f,h)
$$
darstellen lässt, ist die Vorzeichenstruktur von $w_\infty(t)$ direkt zu auditieren.

- Falls $w_\infty(t)\ge0$ f.\u00fc.: $H_\infty = L^2(\mathbb{R},w_\infty(t)\,dt)$, $T_\infty f = \hat{f}$.
- Wechselt $w_\infty$ das Vorzeichen: negative Komponente explizit klassifizieren. Ein formaler Ausdruck mit $\sqrt{w_\infty(t)}$ ist dann **unzulässig**.

$$\boxed{[O\text{-}220\text{-}1d\text{-spectral}]\quad?[O]}$$

---

## 7. Brücke zum algebraischen $HH^4$-Kern

Die bereits bewiesene Klasse $[D_g^{\mathrm{corr}}]\smile[\Theta^\wedge]$ liefert noch keine kanonische archimedische Paarung. Benötigt wird eine konkrete Abbildung:
$$
\boxed{\mathcal{P}_\infty: HH^4\!\left(A_{\mathrm{alg}},\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g \times \mathcal{S}_\infty \longrightarrow \mathbb{C}}
$$
oder eine äquivalente Ketten-/Modulabbildung. Ohne eine solche Brücke dürfen $Q_\infty$ und die Hochschildklasse nicht aufgrund ihrer gemeinsamen philosophischen Rolle identifiziert werden.

$$\boxed{[O\text{-}220\text{-}1e\text{-HH-bridge}]\quad?[O]}$$

**Dieser Knoten ist nachgeordnet.** Er darf erst bearbeitet werden, nachdem $W_\infty$, $\mathcal{S}_\infty$ und $Q_\infty$ unabhängig exakt typisiert wurden.

---

## 8. Globaler Gluungsknoten

Nach Konstruktion des archimedischen Kanals ist zu zeigen, dass er mit den Primkanälen dieselbe Testfunktionskonvention verwendet. Benötigt wird eine gemeinsame Domäne:
$$
\mathcal{S}_W \subseteq \mathcal{S}_\infty \cap \bigcap_p \mathcal{S}_p
$$
und eine Identität:
$$
\boxed{Q_W(f,h) = Q_\infty(f,h) + \sum_p Q_p(f,h) + Q_{\mathrm{pole}}(f,h).}
$$

Zu prüfen:
- absolute oder lokal endliche Konvergenz der Primsumme;
- Primzahlpotenzen $p^m$, nicht nur Primzahlen;
- Übereinstimmung aller Fourier-/Mellinnormalisierungen;
- Hermiteschheit;
- Defektkontrolle;
- Dichtheit der gemeinsamen Domäne.

$$\boxed{[O\text{-}220\text{-}1f\text{-gluing}]\quad?[O]}$$

---

## 9. Knotenstruktur

```
[O-220-1] Archimedischer Weil-/Gammafaktorkanal
        |
        +-- [O-220-1a] exakte Normalisierung (W_infty, Lambda_infty)   ?[O]  <-- ERSTER DIREKTAUDIT
        |
        +-- [O-220-1b] Quellraum und Hermiteschheit                    ?[O]
        |
        +-- [O-220-1c] Positivitätsklassifikation                       ?[O]
        |
        +-- [O-220-1d] spektrale Darstellung (w_infty Vorzeichen)       ?[O]
        |
        +-- [O-220-1e] Brücke zum geladenen HH^4-Kern (nachgeordnet)   ?[O]
        |
        +-- [O-220-1f] globale Gluung                                   ?[O]
        |
        +-- [O-220-2] zyklischer Ersatzrepräsentant (Nebenpfad)        ?[O]
```

---

## 10. Erster konkreter Arbeitsauftrag: $[O\text{-}220\text{-}1a]$

Der erste Direktaudit bearbeitet ausschließlich den Normalisierungsknoten.

**Leitfragen:**
1. Welche exakte Version der expliziten Formel wird als Referenz verwendet?
2. Welche Fourier- bzw. Mellinkonvention liegt zugrunde?
3. Wie lautet der archimedische Term einschließlich aller Faktoren von $2$, $\pi$, $\log\pi$ und aller Argumentverschiebungen der Digammafunktion?
4. Welche Terme gehören zum Gammafaktor und welche zum separaten Polterm?
5. Auf welchem minimalen Testfunktionsraum ist die Distribution wohldefiniert?
6. Welche Realitätssymmetrie benötigt man, damit $Q_\infty(f,h)=\Lambda_\infty(h^\sharp*f)$ hermitesch wird?
7. Ist die archimedische Distribution eindeutig durch die fixierte explizite Formel bestimmt?

**Abschlusskriterium:** Der Knoten darf erst mit $\checkmark[M]$ geschlossen werden, wenn eine vollständig normalisierte Formel vorliegt, die sich an mindestens zwei nichttrivialen Testfunktionen oder Grenzfällen unabhängig überprüfen lässt.

$$\boxed{[O\text{-}220\text{-}1a]\quad?[O]}$$

---

## 11. Strategische Firewall (verbindlich für den gesamten NEU-220-Block)

$$\boxed{\text{Keine Positivität ohne Vorzeichenanalyse.}}$$

$$\boxed{\text{Kein Hilbertraum ohne positive oder defektkontrollierte Form.}}$$

$$\boxed{\text{Kein Operator ohne geschlossene Form und dichten Kern.}}$$

$$\boxed{\text{Keine Hochschild-/Weil-Identifikation ohne typisierte Paarung.}}$$

Der unmittelbar nächste Schritt ist nicht die Konstruktion von $H_\infty$, sondern die exakte Normalisierung von $W_\infty$ und $\Lambda_\infty$.

$$\boxed{[O\text{-}220\text{-}1a]\text{ — exakter Formelaudit des archimedischen Terms.}}$$
