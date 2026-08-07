# NEU-250o — Konstruktionsaudit: Adelisch-archimedischer Port $r_{\infty,W}$

**Katalog-ID:** NEU-250o  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** Vier atomare Tests für $r_{\infty,W}:\mathcal{S}_{\rm adel}\to\mathcal{S}_{\infty,W}$. Kein Gram, keine Positivität, keine Polarisation — nur Existenz und Zieltyp des Ports.  
**Gesamtausgang:** Teilresultat — $\mathcal{S}_{\rm adel}\to\mathcal{S}_\infty$ via Paarung realisierbar; $\mathcal{S}_{\rm adel}\to\mathcal{S}_{\infty,W}$ zu restriktiv; Zielraumfrage offen.  
**Vorgänger:** NEU-250n (N-C; $\iota_\infty^{\rm loc}:\mathcal{S}_{\infty,W}\to\mathcal{W}$ $\checkmark[K/M]$; $r_{\infty,W}\;?[O]$)

---

## 0. Ausgangsbuchung aus NEU-250n

Die Gesamtbrücke zerlegt sich kanonisch:

$$
\boxed{\mathcal{S}_{\rm adel}
\xrightarrow{\;r_{\infty,W}\;?[O]\;}
\mathcal{S}_{\infty,W}
\xrightarrow{\;\iota_\infty^{\rm loc}\;\checkmark[K/M]\;}
\mathcal{W}.} \qquad (0\text{-DAG})
$$

Dieser Knoten auditiert ausschließlich den ersten Pfeil. Die Frage ist nicht
„Wie definieren wir irgendeine Projektion?“, sondern:

$$
\boxed{\text{Existiert eine kanonische, lineare, adelisch natürliche Extraktion }r_{\infty,W}\;?} \qquad (0\text{-Q})
$$

---

## 1. Test 1 — Quellentyp: Was ist $\mathcal{S}_{\rm adel}$ wirklich?

### 1.1 Drei mögliche Präzisierungen

| Kandidat | Topologie | Repository-Status |
|---|---|---|
| $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ (Schwartz-Bruhat, vollständig adelisch) | Induktiver Limes über endliche Primmengen $S$ | NEU-245b: Architekturvorgabe; NEU-245c: $?[O]$ |
| $\bigotimes_{\rm res}' \mathcal{S}(\mathbb{Q}_p)$ (eingeschränktes Tensorprodukt) | LF-Topologie über $\mathcal{S}(\mathbb{Z}_p)$-Sphären | Implizit in NEU-250k K1, nicht explizit |
| Spezieller Quellenunterraum (z.B. $\mathcal{S}_{\rm adel}^{\rm tens}$: reine Tensoren) | Unterraum-Spur | Nicht im Repository |

### 1.2 Befund

$$
\boxed{\mathcal{S}_{\rm adel}\text{ ist noch kein fertig konstruierter topologischer Raum im Repository.}} \qquad (1\text{-Status})
$$

Aus NEU-250n (11-d) ist $\mathcal{S}_{\rm adel}$ als Architekturplatzhalter mit $?[O]$ gebucht. Für die weiteren Tests verwenden wir als Arbeitsannahme $\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})$ im Sinne von Schwartz-Bruhat, halten aber fest:

$$
\boxed{\text{Jedes Resultat in diesem Knoten ist bedingt unter: }\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})\text{ (Arbeitsannahme, nicht bewiesen).}} \qquad (1\text{-Cond})
$$

---

## 2. Test 2 — Kandidatenklassifikation für $r_{\infty,W}$

### 2.1 Drei natürliche Kandidaten

**Kandidat A — Direkte archimedische Projektion (naiv):**
$$
r_A(f) := f_\infty, \qquad f = f_\infty \otimes f_{\rm fin} \text{ (reine Tensoren).}
$$
Für allgemeines $f\in\mathcal{S}(\mathbb{A}_\mathbb{Q})$ existiert keine kanonische Tensorzerlegung (NEU-250n §8). Kandidat A ist auf reinen Tensoren definiert, aber nicht kanonisch fortsetzbar.

**Kandidat B — Paarung mit endlichem Referenzvektor:**
$$
\boxed{r_B(f)(x_\infty) := \int_{\mathbb{A}_{\mathbb{Q},\rm fin}} f(x_\infty, x_{\rm fin})\,\phi_{\rm fin}^0(x_{\rm fin})\,d x_{\rm fin}.} \qquad (2\text{-B})
$$
Wohldefiniertheit: Für $f\in\mathcal{S}(\mathbb{A}_\mathbb{Q})$ und $\phi_{\rm fin}^0\in\mathcal{S}(\mathbb{A}_{\mathbb{Q},\rm fin})$ ist das Integral absolut konvergent (Haarmaß auf $\mathbb{A}_{\mathbb{Q},\rm fin}$ endlich auf Träger von $\phi_{\rm fin}^0$). Das Resultat ist eine Funktion auf $\mathbb{R}_+^\times$.

**Kandidat C — Fourier-/Mellin-Komposition:**
$$
r_C(f)(x_\infty) := \mathcal{F}_{\rm fin}^{-1}\!\left[\hat{f}(\cdot, 0)\right](x_\infty),
$$
also Auswertung der adelischen Fouriertransformierten auf dem archimedischen Faktor. Dieser Kandidat ist typkorrekt formulierbar, aber ohne weitere Konvergenz- und Inversionssätze für $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ noch nicht vollständig gesichert.

### 2.2 Vorläufige Rangliste

| Kandidat | Linear? | Kanonisch (ohne Wahl)? | Fortsetzbar auf ganz $\mathcal{S}(\mathbb{A}_\mathbb{Q})$? |
|---|---|---|---|
| A (Projektion) | Ja (auf reinen Tensoren) | Nein | Nein |
| **B (Paarung)** | **Ja** | **Nein — $\phi_{\rm fin}^0$ muss gewählt werden** | **Ja** |
| C (Fourier) | Ja | Potenziell ja | Offen |

$$
\boxed{\text{Kandidat B ist der nächstliegende, aber seine Kanonizität hängt vollständig an }\phi_{\rm fin}^0.} \qquad (2\text{-Finding})
$$

---

## 3. Test 3 — Bildbedingung: Landet $r_B(f)$ in $\mathcal{S}_{\infty,W}$?

$\mathcal{S}_{\infty,W}$ ist nach NEU-250n (6-Src) definiert als:
$$
\mathcal{S}_{\infty,W} = \Phi^{-1}\!\left(C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}\right)
= \{f\in\mathcal{S}_\infty : \Phi f \in C_c^\infty(\mathbb{R};\mathbb{R}),\;\Phi f\text{ gerade}\}. \qquad (3\text{-Def})
$$

Das sind **drei** gleichzeitig zu erfüllende Bedingungen:

| Bedingung | Erfüllt von $r_B(f)$? |
|---|---|
| (i) $r_B(f)\in\mathcal{S}_\infty$ (Schwartz-Klasse auf $\mathbb{R}_+^\times$) | Ja, für $f\in\mathcal{S}(\mathbb{A}_\mathbb{Q})$ und $\phi_{\rm fin}^0\in\mathcal{S}(\mathbb{A}_{\mathbb{Q},\rm fin})$, da die Paarung Schwartz-Regularität in $x_\infty$ erhält |
| (ii) $\Phi(r_B(f))$ kompakt getragen | **Im Allgemeinen nein.** $\Phi(r_B(f))(y)=r_B(f)(e^y)$ ist Schwartz, aber ohne kompakten Träger |
| (iii) $\Phi(r_B(f))$ reell und gerade | Nur für spezielle $f$ und $\phi_{\rm fin}^0$ |

### 3.1 Das Haupthindernis: kompakter Träger

Schwartz-Funktionen haben im Allgemeinen keinen kompakten Träger. Der Übergang $\mathcal{S}_\infty\to\mathcal{S}_{\infty,W}$ erfordert eine echte Einschränkung, nicht nur topologische Kontrolle.

$$
\boxed{r_B:\mathcal{S}(\mathbb{A}_\mathbb{Q})\longrightarrow\mathcal{S}_{\infty,W}\quad\text{ist zu restriktiv.}
\quad\text{Das Bild liegt generisch in }\mathcal{S}_\infty\setminus\mathcal{S}_{\infty,W}.} \qquad (3\text{-NoGo})
$$

### 3.2 Was tatsächlich erreichbar ist

$$
\boxed{r_B:\mathcal{S}(\mathbb{A}_\mathbb{Q})\longrightarrow\mathcal{S}_\infty \qquad \text{ist realisierbar (für geeignetes }\phi_{\rm fin}^0\text{).}} \qquad (3\text{-Pos})
$$

Das bedeutet: Der Pfeil landet natürlicherweise in $\mathcal{S}_\infty$, nicht in dem kleineren $\mathcal{S}_{\infty,W}$.

---

## 4. Test 4 — Kanonizität von $\phi_{\rm fin}^0$

Kanonizität bedeutet hier: $\phi_{\rm fin}^0$ muss **ohne freie Wahl** aus der adelischen/BC-Struktur ausgezeichnet sein.

### 4.1 Vier Kandidaten für $\phi_{\rm fin}^0$

| Kandidat | Herkunft | Kanonisch? | Adelisch natürlich? |
|---|---|---|---|
| $\mathbf{1}_{\hat{\mathbb{Z}}}$ (Einheitsfunktion auf $\hat{\mathbb{Z}}$) | Haarmaß auf $\mathbb{A}_{\mathbb{Q},\rm fin}$ | Ja, kanonisch | Ja |
| KMS-Grundzustand $\phi_{\rm KMS}^\beta$ bei $\beta=1$ | BC-Algebra (NEU-250b/k) | Ja, aus BC/KMS-Struktur | Ja, aber $\beta$-abhängig |
| Eulerprodukts-Vektor $\bigotimes_p \mathbf{1}_{\mathbb{Z}_p}$ | Direktes Tensorprodukt | Ja | Ja (identisch mit $\mathbf{1}_{\hat{\mathbb{Z}}}$) |
| Willkürliches $\phi_{\rm fin}^0\in\mathcal{S}(\mathbb{A}_{\mathbb{Q},\rm fin})$ | Freie Wahl | Nein | Nein |

### 4.2 Der Haarvektor $\mathbf{1}_{\hat{\mathbb{Z}}}$

Mit $\phi_{\rm fin}^0 = \mathbf{1}_{\hat{\mathbb{Z}}}$ wird:
$$
r_B^{\rm Haar}(f)(x_\infty) = \int_{\hat{\mathbb{Z}}} f(x_\infty, x_{\rm fin})\,d x_{\rm fin}.
$$
Das ist die Einschränkung auf den adelischen Grundzustand. Dieser Kandidat ist kanonisch und adelisch natürlich.

**Aber:** Das Bild $r_B^{\rm Haar}(f)$ liegt in $\mathcal{S}_\infty$, nicht in $\mathcal{S}_{\infty,W}$ (Test 3).

### 4.3 Befund

$$
\boxed{\phi_{\rm fin}^0 = \mathbf{1}_{\hat{\mathbb{Z}}}\text{ ist der kanonischste Kandidat.}
\quad\text{Er erzeugt }r_B^{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}_\infty,\text{ nicht }\to\mathcal{S}_{\infty,W}.} \qquad (4\text{-Finding})
$$

---

## 5. Hauptentscheidung: Zielraumfrage

Die vier Tests erzeugen gemeinsam die folgende harte Entscheidung:

$$
\boxed{
\mathcal{S}_{\rm adel}\longrightarrow\mathcal{S}_\infty\quad\text{ist relativ natürlich (via }r_B^{\rm Haar}\text{ mit }\phi_{\rm fin}^0=\mathbf{1}_{\hat{\mathbb{Z}}}\text{).}
} \qquad (5\text{-A})
$$

$$
\boxed{
\mathcal{S}_{\rm adel}\longrightarrow\mathcal{S}_{\infty,W}\quad\text{ist zu restriktiv: der kompakte-Träger-Schritt fehlt kanonisch.}
} \qquad (5\text{-B})
$$

Daraus folgt die **Zielraumrevision**:

$$
\boxed{
\mathcal{S}_{\infty,W}\text{ ist der Paley-Wiener-Testkern für den Konturtransport (NEU-220j).}
\quad\text{Objekt X benötigt als archimedischen Zielraum }\mathcal{S}_\infty\text{ oder eine Distributionserweiterung.}
} \qquad (5\text{-Rev})
$$

Der Fehler lag nicht im Fehlen einer adelischen Projektion, sondern in der übermäßig engen Zielraumforderung:

$$
\boxed{\text{Die globale Brücke sollte lauten: }
\mathcal{S}_{\rm adel}
\xrightarrow{\;r_\infty^{\rm Haar}\;}
\mathcal{S}_\infty
\xrightarrow{\;\text{Restriktion/Dichtheitsargument}\;}
\mathcal{S}_{\infty,W}\text{-Auswertung.}
} \qquad (5\text{-Chain})
$$

---

## 6. Revidierte DAG-Kette

$$
\boxed{
\mathcal{S}_{\rm adel}
\xrightarrow{\;r_\infty^{\rm Haar}\;\checkmark[M]_{\rm cond}\;}
\mathcal{S}_\infty
\xrightarrow{\;\iota_\infty^{\rm loc}|_{\mathcal{S}_{\infty,W}}\;\checkmark[K/M]\;}
\mathcal{W}.
} \qquad (6\text{-DAG})
$$

**Bedingungen für $\checkmark[M]_{\rm cond}$ des ersten Pfeils:**

1. $\mathcal{S}_{\rm adel} := \mathcal{S}(\mathbb{A}_\mathbb{Q})$ fertig konstruiert und topologisiert — noch $?[O]$ (NEU-245c).
2. Stetigkeit von $r_\infty^{\rm Haar}$ in LF-Topologien nachgewiesen.
3. Adelische Natürlichkeit von $\mathbf{1}_{\hat{\mathbb{Z}}}$ gegen BC-Struktur geprüft (Test 4, Teilbefund: gut, aber $\beta$-Abhängigkeit des KMS-Vektors noch offen).

---

## 7. Konsequenz für Objekt X

Die Zielraumrevision hat eine direkte Konsequenz für die Architektur von Objekt X:

$$
\boxed{
\begin{aligned}
&\text{Die Hermitesche Polarisation (M3) und die gemeinsame Gramgeometrie (M4)}\\
&\text{müssen über }\mathcal{S}_\infty\text{ oder eine Distributionserweiterung formuliert werden,}\\
&\text{nicht über den kleinen Paley-Wiener-Raum }\mathcal{S}_{\infty,W}.
\end{aligned}
} \qquad (7\text{-Arch})
$$

Das ist kein Rückschritt. Es präzisiert den Spielraum: $\mathcal{W}$ bleibt der richtige Testkern für die Weil-Explizitformel; aber der globale Port von der adelischen Quelle soll in $\mathcal{S}_\infty$ landen, von wo aus dann via Dichte/Fortsetzung auf $\mathcal{W}$ ausgewertet wird.

---

## 8. Auditmatrix

| Test | Frage | Befund |
|---|---|---|
| 1 — Quelle | $\mathcal{S}_{\rm adel}$ definiert? | Noch Architekturplatzhalter; Arbeitsannahme $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ |
| 2 — Kandidaten | Bester Kandidat für $r_{\infty,W}$? | Kandidat B (Paarung) mit $\phi_{\rm fin}^0=\mathbf{1}_{\hat{\mathbb{Z}}}$ |
| 3 — Bild | Landet $r_B(f)\in\mathcal{S}_{\infty,W}$? | **Nein** — Bild in $\mathcal{S}_\infty$, nicht kompakt getragen |
| 4 — Kanonizität | Ist $\phi_{\rm fin}^0$ kanonisch? | $\mathbf{1}_{\hat{\mathbb{Z}}}$ kanonisch; KMS-Vektor gut aber $\beta$-abhängig |
| 5 — Zielraum | $\mathcal{S}_{\infty,W}$ oder $\mathcal{S}_\infty$? | **$\mathcal{S}_\infty$ ist der richtige globale Zielraum** |

---

## 9. Statusbuchungen

$$
r_\infty^{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}_\infty\quad\checkmark[M]_{\rm cond}\qquad(\text{bedingt unter NEU-245c}) \qquad (9\text{-a})
$$

$$
r_{\infty,W}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}_{\infty,W}\quad\times[M]\qquad(\text{zu restriktiver Zielraum}) \qquad (9\text{-b})
$$

$$
\text{Zielraumrevision: archimedischer Port nach }\mathcal{S}_\infty\quad\checkmark[M] \qquad (9\text{-c})
$$

$$
\mathcal{S}_{\rm adel}\text{ Existenz/Topologie}\quad?[O]\quad\to\text{NEU-245c\,fort} \qquad (9\text{-d})
$$

---

## 10. Nächste atomare Schritte

1. **NEU-245c (fortgesetzt):** $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ topologisch konstruieren; $r_\infty^{\rm Haar}$ Stetigkeit nachweisen.
2. **Polarisationsknoten (M3):** $g_a(t)=\operatorname{Re}\langle a, U_t a\rangle$ hermitesch polarisieren zu $g_{a,b}(t)$, jetzt mit Zielraum $\mathcal{S}_\infty$ statt $\mathcal{S}_{\infty,W}$.
3. **Erstes gemeinsames endliches Modell:** Endlicher Primzahlsatz + archimedischer Cutoff; Blockform mit von-Mangoldt-Gewichten in $\mathcal{S}_\infty$.

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250n | e0f2f70 | Vorgänger; $\iota_\infty^{\rm loc}$ $\checkmark[K/M]$; $r_{\infty,W}$ $?[O]$ |
| NEU-220a | 653c8a9 | $\mathcal{S}_\infty$, $\mathcal{M}_\infty$, $2\pi$-Patch |
| NEU-220j | 41e28cf | $\mathcal{W}$, LF-Topologie, Konturtransport |
| NEU-245b | 79ecf25 | $\mathcal{S}_{\rm adel}$ Architekturvorgabe |
| NEU-245c | 1ef32ab | $\mathcal{S}_{\rm adel}$ Konstruktion $?[O]$ |
| NEU-250m | ce1a7af | M1--M4; M3/M4 $?[O]$ |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
