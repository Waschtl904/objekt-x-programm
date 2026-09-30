# Warum κ nahe eins liegt: ein zertifizierter Richtungszeuge

29. September 2026 · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Beweisbasis: `Waschtl904/objekt-x-programm`, Commit
`8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b`.

## Ergebnis und verbleibende Frage

**Ein konkreter Mechanismus lässt sich bereits aus den gespeicherten Daten
beweisen:** Eine exakt definierte Richtung der echten kanonischen Ergänzung
hat einen kleinen, aber von null getrennten Überlapp mit einer extrem
energiearmen physischen Quelle. Dieser Überlapp erzwingt ein riesiges inverses
Energiemoment und einen großen verallgemeinerten Schurquotienten.

Bei A₉→A₁₁ ist der Zeuge jeweils die **erste Spalte der bestehenden kanonischen
Rohbasis**, auf L²-Norm eins gebracht. Seine wirkliche Spektralverteilung trägt
sowohl sehr tiefe als auch wesentlich höhere Energien. Die Aussage verwendet
keinen neuen großen Resolventenlauf.

**Die tatsächliche maximierende Richtung im zweidimensionalen E ist hier noch
nicht isoliert.** Der Zeuge ist kein als Extremalrichtung ausgegebener
Mittelpunktseigenvektor. Für jeden tatsächlichen Maximierer werden zusätzlich
schwächere, aber rigorose Spektralbandfolgen bewiesen. Einzelne echte Eigenmoden
und ihre Herkunft aus dem alten Raum bleiben offen.

Der bisherige κ-/Resolventen-Block bleibt abgeschlossen. Seine vier publizierbar
vorbereiteten Intervalle werden unverändert übernommen. Dieses Paket untersucht
den Mechanismus; es ersetzt weder das frühere Paket noch dessen Prüfstatus.

## 1. Welcher Vektor maximiert tatsächlich?

Sei wie bisher

\[
V_0=P_BU_BN,\quad G=V_0^*V_0,\quad
L_0=V_0^*Q_BV_0,\quad Z_0=V_0^*Q_B^{-1}V_0.
\]

Setze \(B_0=L_0+17G\), \(R_0=L_0+34G+289Z_0\). Die maßgebliche
größte Eigenzahl ist exakt

\[
\beta=(1-\kappa)^{-1}
=\max_{x\ne0}
\frac{x^*R_0x}{x^*B_0L_0^{-1}B_0x}.
\tag{1}
\]

Die gesuchte Richtung erfüllt also das **verallgemeinerte Eigenwertproblem**

\[
R_0x=\beta B_0L_0^{-1}B_0x.
\tag{2}
\]

Begründung: In b-orthonormalen E-Koordinaten sind
\(D=B_0^{-1/2}L_0B_0^{-1/2}\) und
\(H=B_0^{-1/2}R_0B_0^{-1/2}\). Die Eigenzahlen von
\(D^{1/2}HD^{1/2}\) sind die verallgemeinerten Eigenzahlen von H gegen D⁻¹.
Die Substitution \(z=B_0^{1/2}x\) ergibt (1).

Zwei zugehörige Richtungen sollten unterschieden werden:

- \(V_0x\) ist der maximierende Vektor für die inverse Antwort in (1).
- \(V_0L_0^{-1}B_0x\) ist die zugehörige Richtung, welche den relativen
  Schurrest \(H^{-1}\) gegen D minimiert.

Die Transformation folgt aus \(Hz=\beta D^{-1}z\). Für
\(y=D^{-1}z\) gilt \(H^{-1}y=\beta^{-1}Dy\).

### Warum ein skalares Momentprodukt in Dimension zwei nicht genügt

Für eine beliebige normierte Richtung v ist
\(q[v]\langle v,Q^{-1}v\rangle\) im Allgemeinen **nicht** der Quotient (1).
Schon für einen invarianten zweidimensionalen Raum mit
\(Q|_E=\operatorname{diag}(\varepsilon,1)\) gilt κ=0. Die Richtung
\((1,1)/\sqrt2\) hat trotzdem das Momentprodukt
\((1+\varepsilon)(1+\varepsilon^{-1})/4\).
Bei ε=10⁻¹² ist dieses Produkt größer als 10¹¹.

Das Beispiel wird exakt rational geprüft. Der neue Kopplungszeuge wird deshalb
über (1) zertifiziert; die anschließenden skalaren Momente beschreiben seine
Spektralverteilung.

## 2. Ein energiearmer physischer Testvektor erklärt die inverse Antwort

Wir wählen in jedem Fall

\[
v=V_0e_1/\sqrt{G_{11}}\in E,\qquad \|v\|_2=1.
\]

Bei A₈→A₉ ist E eindimensional, sodass damit seine einzige Richtung feststeht.
Bei A₉→A₁₁ ist dies ein festgelegter Zeuge im zweidimensionalen Raum.
Als Testquelle dient \(u=U_Be_j\), mit j=1 außer im ungeraden A₈→A₉-Fall,
wo j=2 verwendet wird. Die U-Spalten sind die bestehenden exakt definierten
L²-orthonormalen physischen Hilfsquellen, einschließlich Mellinkorrektur.

Schreibe \(E_N=N^*S_BN\), \(q_j=(S_B)_{jj}\), und sei ν_B der vollständige
physische Komplement-Gap. Aus \(R_B=(I-P_B)U_B\) folgt

\[
\langle u,V_0e_1\rangle
=N_{j1}-(R_Be_j)^*R_BNe_1,
\]

\[
\left|\langle u,V_0e_1\rangle-N_{j1}\right|
\le\frac{\sqrt{q_j(E_N)_{11}}}{\nu_B}.
\tag{3}
\]

Die gespeicherten gerichteten N-, Gram- und Energieintervalle liefern somit
eine positive Untergrenze \(\alpha\le|\langle u,v\rangle|\).
Die Cauchy–Schwarz-Ungleichung in der Q-Energie ergibt

\[
|\langle u,v\rangle|^2
\le q_B[u]\langle v,Q_B^{-1}v\rangle,
\qquad
\boxed{\langle v,Q_B^{-1}v\rangle\ge\alpha^2/q_j.}
\tag{4}
\]

Die Existenz der positiven inversen Form bleibt eine Voraussetzung des
bereits positiven Terminals. Für (4) wird keine neue Resolventenlösung und
kein globaler inverser Terminalboden gebraucht.

### Gerichtete Ergebnisse

Alle Anzeigen sind nach außen gerundet. Der Prüfer wertet beide ursprünglichen
Präzisionsläufe aus und übernimmt jeweils die äußere Vereinigung.

| Übergang / Parität | Probe j | obere Schranke q_B[u] | untere Schranke α | durch (4) erzwungenes inverses Moment |
|---|---:|---:|---:|---:|
| A₈→A₉ gerade | 1 | 1.51244·10⁻³¹ | 6.05755·10⁻¹⁰ | ≥2.42614·10¹² |
| A₈→A₉ ungerade | 2 | 1.95715·10⁻²² | 2.67615·10⁻⁷ | ≥3.65932·10⁸ |
| A₉→A₁₁ gerade | 1 | 1.08056·10⁻⁴¹ | 1.13541·10⁻¹⁰ | ≥1.19305·10²¹ |
| A₉→A₁₁ ungerade | 1 | 1.55663·10⁻³⁸ | 2.19592·10⁻¹⁰ | ≥3.09776·10¹⁸ |

Im ungeraden A₈→A₉-Fall schließt die verfügbare Überlappeinschließung für j=1
null ein. Eine Beteiligung gerade dieser ersten Quelle wird dort nicht
behauptet. Die zweite Quelle liefert den rigorosen Zeugen.

### Der Zeuge erzeugt tatsächlich Schurkopplung

Für \(w=e_1\) ist der Nenner in (1)

\[
w^*B_0L_0^{-1}B_0w
=w^*L_0w+34w^*Gw+289w^*GL_0^{-1}Gw.
\]

Mit den vorhandenen positiven Schranken \(L_-\preceq L_0\preceq L_+\)
wird der letzte Term nach oben durch \(w^*GL_-^{-1}Gw\) begrenzt.
Der Zähler erhält seine Untergrenze aus L_-, G und (4), in den gemeinsamen
Rohkoordinaten. Alle Gram- und Kreuzterme werden mitgeführt.

| Übergang / Parität | zertifizierter unterer Wert des Quotienten (1) an e₁ |
|---|---:|
| A₈→A₉ gerade | 5.01063·10⁶ |
| A₈→A₉ ungerade | 4.03721·10⁴ |
| A₉→A₁₁ gerade | 7.29709·10¹¹ |
| A₉→A₁₁ ungerade | 1.24931·10¹¹ |

Diese Werte belegen einen konkreten Kopplungsmechanismus. Sie sind untere
Zeugenwerte für β, keine bestimmten Werte des tatsächlichen Maximums.
Die vorhandenen Energie-Untergrenzen L_- bleiben gebundene Eingaben; dieser
Nachweis ist kein vom früheren Resolventenpaket unabhängiger Gesamtbeweis.

## 3. Welche echten Spektralbereiche mischt dieser Zeuge?

Sei \(\mu_v\) das L²-Spektralmaß von Q_B an v. Es hat Gesamtmasse eins und
ist im positiven kritischen Spektrum enthalten. Setze

\[
a=4q_j/\alpha^2,\qquad b=\ell_v/2,
\qquad \ell_v\le q_B[v].
\]

Dann gelten drei getrennte Aussagen:

1. **Mindestens 3/4 der inversen Energie** von v liegt bei λ≤a.
   Denn der Anteil bei λ>a ist höchstens 1/a=α²/(4q_j), während das gesamte
   inverse Moment nach (4) mindestens α²/q_j beträgt.
2. **Mindestens 1/2 seiner Energie** liegt bei λ≥b. Unterhalb b ist
   \(\int\lambda\,d\mu_v\le b\le q_B[v]/2\).
3. Auch gewöhnliche Spektralmasse ist in beiden Bereichen positiv:

\[
\mu_v((0,a])\ge\alpha^2/4,\qquad
\mu_v([b,\Theta_B])\ge\frac{\ell_v}{2\Theta_B-\ell_v}.
\tag{5}
\]

Für die erste Massenschranke sei \(P_a=\mathbf1_{(0,a]}(Q_B)\).
Aus \(\|(I-P_a)u\|\le\sqrt{q_j/a}=\alpha/2\) folgt
\(\|P_av\|\ge|\langle v,u\rangle|-\|(I-P_a)u\|\ge\alpha/2\).
Die zweite folgt aus
\(q_B[v]\le b+(\Theta_B-b)\mu_v([b,\Theta_B])\).

**Energieanteile, inverse Energieanteile und gewöhnliche L²-Massen sind
unterschiedliche Größen.** Die 3/4-Aussage behauptet keine 75 % L²-Masse
im tiefen Bereich.

| Übergang / Parität | tiefer Bereich bis einschließlich | höherer Bereich ab einschließlich | untere L²-Masse im tiefen Bereich |
|---|---:|---:|---:|
| A₈→A₉ gerade | 1.64871·10⁻¹² | 1.03263·10⁻⁶ | 9.17349·10⁻²⁰ |
| A₈→A₉ ungerade | 1.09310·10⁻⁸ | 5.51641·10⁻⁵ | 1.79045·10⁻¹⁴ |
| A₉→A₁₁ gerade | 3.35274·10⁻²¹ | 3.05815·10⁻¹⁰ | 3.22291·10⁻²¹ |
| A₉→A₁₁ ungerade | 1.29126·10⁻¹⁸ | 2.01648·10⁻⁸ | 1.20551·10⁻²⁰ |

Die Bandgrenzen gelten für Q_B, nicht für Q_B(Q_B+17I)⁻¹. Sie sind
Trennschwellen mit garantierten Anteilen, keine isolierten Eigenwerte.
Insbesondere ist die Probe mit Energie ≤1.08056·10⁻⁴¹ nicht dadurch als
Eigenvektor mit Eigenwert 10⁻⁴¹ identifiziert.

## 4. Was ist daran vom alten Raum geerbt?

Die ausgewählte neue Trialquelle ähnelt der entsprechenden physisch
nullfortgesetzten alten Trialquelle stark. Für die normierten physischen
Überlappe liefert die gebundene Datei sichere Untergrenzen:

| Übergang / Parität | Überlapp ⟨JU_Ae_j,U_Be_j⟩ mindestens | absoluter Überlapp von v mit JU_Ae_j höchstens |
|---|---:|---:|
| A₈→A₉ gerade | 0.999958 | 1.96240·10⁻¹² |
| A₈→A₉ ungerade | 0.999453 | 9.47885·10⁻⁹ |
| A₉→A₁₁ gerade | 0.999915 | 6.34144·10⁻¹⁵ |
| A₉→A₁₁ ungerade | 0.999882 | 4.13075·10⁻¹⁴ |

Die letzte Spalte ist ein neuer Schluss aus der kanonischen Orthogonalität.
Für \(f=JP_AU_Ae_j\) gilt \(b_B(v,f)=0\); der Anteil außerhalb K_B ist
ebenfalls b-orthogonal zu v. Mit Formnaturality und Cauchy–Schwarz folgt

\[
|\langle v,JU_Ae_j\rangle|
\le \frac{\sqrt{q_B[v]q_A[U_Ae_j]}}{17}
+\sqrt{q_A[U_Ae_j]/\nu_A}.
\tag{6}
\]

Der deutlich größere, von null getrennte Überlapp mit der neuen Quelle
erfasst daher ihre Änderung gegenüber der alten nullfortgesetzten Quelle.
Bei A₉→A₁₁ beträgt der Überlapp mit dieser Differenz mindestens
1.13535·10⁻¹⁰ gerade bzw. 2.19550·10⁻¹⁰ ungerade.

Damit wird das Muster konkreter: **Die Änderung einer räumlich ähnlichen
schwachen Quelle dringt geringfügig in E ein; ihre extrem kleine neue Energie
verstärkt diesen Überlapp in der inversen Antwort.** Die neue Quellenergie
liegt gerade unter 1.08056·10⁻⁴¹, während die verwendete alte obere
Rayleigh-Schranke bei 1.51244·10⁻³¹ liegt; ungerade lauten die entsprechenden
oberen Schranken 1.55663·10⁻³⁸ und 1.12345·10⁻²⁸.
Zwei obere Schranken allein bestimmen kein Verhältnis tatsächlicher Energien.

Dies beschreibt exakt definierte physische Hilfsquellen und ihre Beziehung
zu E. Eine Identifikation mit einem bestimmten alten echten Eigenvektor,
einer neu hinzugekommenen Eigenmode oder ein allgemeines Skalengesetz wird
damit noch nicht bewiesen.

## 5. Was gilt bereits für jeden tatsächlichen Maximierer?

Auch ohne seine Koordinaten kann man den maximierenden Vektor der inversen
Antwort in (1) spektral eingrenzen. In einer L²-orthonormalen E-Basis sei
\(\ell_E I\preceq L\preceq\theta_E I\), und β≥β₀ aus dem bisherigen
κ-Paket. Für einen auf L²-Norm eins gebrachten Maximierer e gilt

\[
z=\langle e,Q_B^{-1}e\rangle
=\beta\langle e,L^{-1}e\rangle
+\frac{\beta-1}{289}\big(q_B[e]+34\big)
\ge\beta_0/\theta_E.
\tag{7}
\]

Dabei bezeichnet \(\langle e,L^{-1}e\rangle\) die inverse komprimierte
Energiematrix auf E. Folglich liegen mindestens die Hälfte seiner inversen
Energie bei λ≤2θ_E/β₀ und mindestens die Hälfte seiner Energie bei λ≥ℓ_E/2.
Die Rechnung benutzt sichere Schranken aus L_± und G.

| A₉→A₁₁ | tiefer Bereich bis einschließlich | höherer Bereich ab einschließlich |
|---|---:|---:|
| gerade | 2.03738·10⁻¹⁷ | 3.01562·10⁻¹⁰ |
| ungerade | 1.23320·10⁻¹⁴ | 1.94801·10⁻⁸ |

Diese Aussagen gelten für jeden Maximierer der inversen Antwort, auch bei
mehrfacher größter Eigenzahl. Die stärkeren Schwellen in §3 gehören dem
konkret festgelegten Zeugen v. Sie werden nicht auf den unbekannten
Maximierer übertragen.

## 6. Warum hier noch kein einzelner maximierender Vektor steht

Die Zertifikate für die beiden Rohkoordinatenrichtungen überlappen stark:

| A₉→A₁₁ | Quotient (1) an e₁ | Quotient (1) an e₂ |
|---|---:|---:|
| gerade | [7.16152·10¹¹, 1.29544·10¹³] | [2.18429·10³, 1.80864·10¹⁶] |
| ungerade | [1.14868·10¹¹, 1.85059·10¹³] | [1.08549·10², 7.11196·10¹⁶] |

Diese Tabelle verwendet die gespeicherten vollständigen Resolventenfaktoren.
Die unabhängigen oberen Richtungsgrenzen können gröber sein als die
vorhandene globale β-Obergrenze. Auch optimale Mischungen der Achsen wären
bei einer Extremalrichtung zu berücksichtigen.

Der Prüfer konstruiert zusätzlich je Parität zwei positive diagonale
Momentpaare innerhalb der gelieferten **physischen Eintragshüllen**, der
verfeinerten inversen Diagonalintervalle und der bisherigen κ-Grenzen.
Bei einem Paar maximiert Achse 1, beim anderen Achse 2. Beide erfüllen
auch Z≥L⁻¹. Das zeigt, weshalb bloßes Diagonalisieren eines ausgewählten
Momentmittelpunkts keine Richtungszertifizierung liefert.

Diese Beispiele gehören ausschließlich zur Eintragsrelaxation. Sie erfüllen
nicht nachgewiesenermaßen sämtliche gemeinsamen N-, Annihilator- und
Faktorbedingungen. Sie sind **kein Unmöglichkeitsbeweis**, aus weiter
ausgewerteten Originaldaten die Richtung zu bestimmen, und keine alternativen
Realisierungen des ursprünglichen Operators.

Ein sinnvoller nächster Abnahmepunkt ist deshalb:

1. Eine gemeinsame, hinreichend enge Einschließung des zweidimensionalen
   Problems (2), einschließlich aller Kreuzterme, liefern und daraus einen
   Eigenwertabstand sowie einen Winkelbereich für den Maximierer zertifizieren.
2. Für diese Richtung bandweise Momente
   \(V^*\mathbf1_I(Q_B)V\) und
   \(V^*Q_B^{-1}\mathbf1_I(Q_B)V\) bestimmen, um die beteiligten Energiebänder
   mit überprüfbaren Gewichten zuzuordnen.
3. Die Beziehung dieser Bänder zum transportierten alten kritischen Raum
   kontrollieren. Die in §4 bewiesene Trialquellenbeziehung ist dafür ein
   konkreter Anhaltspunkt, aber kein Ersatz für diese Identifikation.

## 7. Tatsächliche Prüfung und Status

- Vier gebundene Eingabedateien: beide bisherigen Resolventenläufe, deren
  rationaler Prüfbeleg und die bestehende physische Trialraum-Datei.
- Alle 25 ursprünglichen Repository-Eingaben wurden erneut byteweise mit
  den Git-Blobs des festen Commits verglichen, einschließlich der binären
  O8-Datei `reserve_refined_lower_matrices.json.gz`.
- Beide Präzisionsbelege wurden mit exakten rationalen Endpunkten ausgewertet.
  Wurzeln erhalten beweisbar gerichtete rationale Grenzen. Die Ergebnisanzeigen
  werden aus diesen Grenzen nach außen gerundet.
- Die Prüfung enthält das exakte Gegenbeispiel zur skalaren Abkürzung,
  drei nichtkommutierende rationale Identitätsprüfungen und die vier
  Eintragsrelaxationsbeispiele. Diese endlichen Prüfungen ergänzen die
  allgemeinen Beweise; sie ersetzen sie nicht.
- Der Wiederholungslauf erzeugt dieselbe Ergebnisdatei. Große Matrixsolver,
  ursprüngliche Terminalintegrale und eine neue Kammer wurden nicht gerechnet.

Die kanonischen Raum-, Energie- und Resolventenintervalle sowie die analytischen
Terminalnachweise bleiben Voraussetzungen. Externer mathematischer Review ist
offen. Die neue Positivität wird weiterhin vorausgesetzt; ein vorwärts
gerichteter Renewal-Satz, kofinale Positivität, ein globales Objekt X und eine
RH-Aussage folgen nicht.

Der bestehende κ-/Resolventen-Frontier ist abgeschlossen. Der neue
Mechanismusblock liefert gerichtete Zeugen und echte Spektralbandfolgen;
die vollständige Extremalrichtungs- und Eigenmodenidentifikation bleibt offen.
Alle drei jüngsten Pakete sind lokal. Repository, Registry und PR #187 wurden
in diesem Durchlauf nicht verändert.
