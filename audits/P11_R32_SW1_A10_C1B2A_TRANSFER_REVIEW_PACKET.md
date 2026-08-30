# P11-R32 / SW1-A10-C1B2A-TRANSFER — Independent Review Packet

## Zweck

Dieser Review-Knoten ist **getrennt** vom bereits mechanisch zertifizierten Rank-4-Chirotop-Ledger.

Zu prüfen ist ausschließlich der mathematische Transferschritt

[
r_0=7/2
quadlongrightarrowquad
rin(3,4)
]

für die konkrete affine Hyperflächenfamilie aus 18 Kollisionsflächen plus 4 Simplexfacetten.

Keine Aussage über Cross-Gram-Injektivität.

---

## Zertifizierter finite/algebraischer Input

### 0. Affine Verstärkung mit ausgezeichnetem Unendlichkeitselement

Zusätzlich zum 22er-Chirotop liegt nun der stärkere affine Prüfer

`scripts/certify_sw1_a10_c1b2a_affine_chirotope.py`

vor.

Committed Blob:

`1c2f7a3e6123697846e4f6d5e931d3c962b1fb20`

Er fügt das feste ausgezeichnete Unendlichkeitselement

[
g_\infty=(0,0,0,1)
]

hinzu und prüft alle

[
\binom{23}{4}=8855
]

Rank-4-Minoren.

Die 1540 neuen INF-Minoren sind

[
622\text{ identisch Null}+918\text{ konstant nonzero}+0\text{ r-abhängig}.
]

Damit ist die affine, nicht nur projektive, Chirotop-Konstanz auf (3<r<4) mechanisch zertifiziert.

### 1. Ursprünglicher 22er-Minorenledger

Die Datei

`scripts/certify_sw1_a10_c1b2a_chirotope.py`

prüft exakt alle

[
inom{22}{4}=7315
]

orientierten Rank-4-Minoren der augmentierten Zeilen

[
(a_{i,1},a_{i,2},a_{i,3},-b_i(r)).
]

Committed Blob:

`c4acf11c1564a67bd10b92c76bcf74adc6d26ebb`

Ergebnis:

`SW1-A10-C1B2A CHIROTOPE CONSTANCY CERTIFICATE: PASS`

Klassifikation:

[
1652	ext{ identisch Null},qquad
2012	ext{ konstant nonzero},qquad
3651	ext{ affin-linear}.
]

Die einzige Nullstellenmenge der linearen Minoren ist

[
{-3,-2,-1,-1/2,0,1/3,1/2,2/3,1,4/3,3/2,2,5/2,3,4,5,6}.
]

Daher verschwindet kein nichtidentischer Rank-4-Minor für (3<r<4), und der vollständige Chirotop ist dort konstant.

Die vier Simplexfacetten sind Teil derselben 22er-Konfiguration.

---

## Zu prüfender mathematischer Schluss

Die benötigte Aussage ist bewusst enger als ein globaler topologischer Satz.

### TRANSFER-A

Für die stetige Einparameterfamilie der 22 orientierten affinen Hyperflächen folgt aus dem konstanten Chirotop auf (3<r<4), dass die Menge der Covektoren/Topes des realisierbaren orientierten Matroids konstant ist.

Insbesondere sind die 64 offenen Parameterkammer-Signvektoren bei (r_0=7/2) dieselben Signvektoren wie bei jedem tatsächlichen (rin(3,4)).

### TRANSFER-B

Weil die vier Simplexfacetten in der Konfiguration enthalten und orientiert mitgeführt werden, bleibt auch die innerhalb

[
0<sigma<R<arepsilon<(r+1)/2
]

relevante geklippte Kammerstruktur konstant.

### TRANSFER-C

Die (B_{96})-Kreiswanddifferenzen werden durch dieselben 18 Kollisionshyperflächen kontrolliert, und GATE1R hat bereits

[
S_{96}=S_{92},
qquad
C_{96}=C_{92}
]

als Mengengleichheiten zertifiziert.

Daher soll innerhalb korrespondierender Parameterkammern auch die zyklische Ordnung der 96 Kreiswände konstant bleiben.

### TRANSFER-D

Wenn A–C gelten, darf die exhaustive M1-FULL-Prüfung der 64 Kammern × 96 offenen Kreisatome am Referenzwert (r_0=7/2) auf jedes tatsächliche (rin(3,4)) übertragen werden, **sofern** M1-FULL selbst provenance-sauber PASS ist.

---

## Adversarielle Fragen

1. Reicht die Konstanz des **affinen 23er-Chirotops einschließlich des ausgezeichneten Unendlichkeitselements** tatsächlich aus, um den vollständigen realisierbaren affinen orientierten Matroid/Covektor-Datensatz konstant zu halten?

2. Können identisch verschwindende Minoren eine versteckte Änderung des Covektor-Datensatzes erlauben, obwohl sämtliche nichtidentischen Minoren auf ((3,4)) ihr Vorzeichen behalten?

3. Sind die vier Simplexfacetten korrekt Teil der orientierten Konfiguration, so dass auch Rand-/Clipping-Inzidenzen abgedeckt sind?

4. Reicht die konstante Tope-Struktur für die Aussage „dieselben 64 offenen Kammer-Signvektoren“, oder wird zusätzlich eine echte ambient isotopy benötigt?

5. Ist für M1-FULL überhaupt eine ambient isotopy nötig, oder genügt die Konstanz der Kammer-Signvektoren plus der (B_{96})-Kreisordnung?

6. Folgt die konstante zyklische (B_{96})-Ordnung in jeder Kammer tatsächlich aus den bereits zertifizierten Kollisionshyperflächen, oder fehlt eine zusätzliche Wrap-/Kreisorientierungsbedingung?

7. Gibt es bei (r=3) oder (r=4) relevante Degenerationen, die den offenen Intervalltransfer (3<r<4) trotzdem beeinflussen könnten?

8. Ist der Schluss TRANSFER-D korrekt auf **offene** Parameterkammern und **offene** Kreisatome beschränkt, wobei Randmengen später nur a.e. ignoriert werden?

9. Welche minimale mathematische Aussage sollte nach erfolgreichem Review gebucht werden:
   - konstante Covektor-/Tope-Struktur,
   - kombinatorische Arrangement-Isotopie,
   - oder volle ambient isotopy?

10. Folgt aus keinem dieser Punkte bereits irgendeine Aussage über
[
kerGamma_I?
]
Die erwartete Antwort ist ausdrücklich **nein**.

---

## Gewünschtes Verdict

Bitte getrennt urteilen:

- **C1B2A-CHIRO**: bereits mechanisch zertifizierter finite/algebraischer Input.
- **C1B2A-TRANSFER**: GREEN / PARTIAL / FAIL mit genauer Begründung.

Keine Promotion und keine Cross-Gram-Injektivitätsaussage.


---

## Präzisierter Transferbeweis ohne ambient isotopy

### Literaturlemma OM-CRYPT

Verwendet wird die Standard-Cryptomorphie orientierter Matroide.

**Referenz:**  
A. Björner, M. Las Vergnas, B. Sturmfels, N. White, G. M. Ziegler,  
*Oriented Matroids*, 2nd ed., Cambridge University Press, 1999, Chapter 3,
insbesondere Section 3.5 (Chirotopes).

Als frei zugängliche Kontrollreferenz formuliert G. M. Ziegler,
*Oriented Matroids Today*, Electronic Journal of Combinatorics 3 (1996),
Dynamic Survey 4, Section 2, ausdrücklich:

- Chirotop,
- Covektoren,
- Cocircuits,
- Vektoren,
- Circuits

sind äquivalente Datensätze eines orientierten Matroids und rekonstruieren
einander eindeutig, bis auf die globale Identifikation \(\chi\sim-\chi\).

Für unsere gelabelte Familie ist sogar der konkrete Signvektor aller
Rank-4-Minoren auf \(3<r<4\) konstant, also nicht nur seine globale
Vorzeichenklasse.

Daher gilt für alle \(r,r'\in(3,4)\):

\[
\boxed{
\chi_r=\chi_{r'}
\Longrightarrow
\mathcal M_r=\mathcal M_{r'}
\Longrightarrow
\mathcal V^*(\mathcal M_r)=\mathcal V^*(\mathcal M_{r'})
}
\]

und insbesondere ist die Topemenge identisch.

Der stärkere AFF-CHIRO-Prüfer führt das ausgezeichnete
Unendlichkeitselement \(g_\infty\) mit, so dass hier die **affine** und
nicht nur projektive orientierte Matroidstruktur gemeint ist.

---

### TRANSFER-A — 64 Kammer-Signvektoren

Für unser realisierbares affines Hyperflächenarrangement ist zu einem
festen vollständigen Vorzeichenvektor \(T\in\{+,-\}^{22}\) die
Realisierungsmenge

\[
C_T(r)
=
\left\{
x=(\sigma,R,\varepsilon):
T_i\bigl(a_i\cdot x-b_i(r)\bigr)>0
\text{ für alle }i
\right\}.
\]

Sie ist als Schnitt offener Halbräume konvex.

Daher besitzt jeder realisierte Tope-Signvektor höchstens eine offene
Kammerkomponente. Umgekehrt liefert jede offene Kammer genau ihren
Vorzeichenvektor.

Da OM-CRYPT die Topemenge für alle \(3<r<4\) identisch hält und die vier
Simplexfacetten explizit Teil der Konfiguration sind, bleiben insbesondere
diejenigen Topes identisch, welche die gewünschte Simplexseite

\[
0<\sigma<R<\varepsilon<(r+1)/2
\]

realisieren.

Somit bleibt die Menge der offenen Parameterkammer-Signvektoren gleich.
Am Referenzwert sind es zertifiziert 64; daher gilt für jedes
\(r\in(3,4)\):

\[
\boxed{
N_{\rm chamber}(r)=64
}
\]

mit kanonischer Identifikation über den Tope-Signvektor.

---

### TRANSFER-B — gemeinsame Verbindung im erweiterten \((r,x)\)-Raum

Für einen festen Tope \(T\) betrachte

\[
\widetilde C_T
=
\left\{
(r,x):
3<r<4,
\quad
T_i\bigl(a_i\cdot x-b_i(r)\bigr)>0
\text{ für alle }i
\right\}.
\]

Da jedes \(b_i(r)\) affin-linear in \(r\) ist, sind dies strikte lineare
Ungleichungen in den vier Variablen

\[
(r,\sigma,R,\varepsilon).
\]

Folglich ist \(\widetilde C_T\) selbst konvex.

Für jeden tatsächlichen Punkt \((r,x)\) im Tope und jeden
Referenzpunkt \((7/2,x_0)\) mit demselben Tope-Signvektor liegt deshalb
die gesamte Verbindungsstrecke in \(\widetilde C_T\).

Damit existiert ein konkreter kollisionsfreier stetiger Pfad vom
Referenzarrangement zum tatsächlichen Parameter, ohne dass eine globale
ambient isotopy behauptet werden muss.

---

### TRANSFER-C — zyklische \(B_{96}\)-Kreisordnung

Die 96 gelabelten Kreiswände sind stetige kreiswertige Funktionen der
Parameter.

Die zyklische Reihenfolge einer endlichen Menge gelabelter, paarweise
verschiedener Punkte auf einem orientierten Kreis ist lokal konstant und
kann sich entlang eines stetigen Pfades nur ändern, wenn zwei gelabelte
Punkte kollidieren.

GATE1R hat exhaustiv zertifiziert, dass die nichttrivialen
Paar-Kollisionsbedingungen des korrekten \(B_{96}\)-Alphabets exakt
dieselben 18 inneren Kollisionshyperflächen liefern:

\[
S_{96}=S_{92},
\qquad
C_{96}=C_{92}.
\]

Innerhalb eines festen offenen Topes/Kammerpfades wird keine dieser
Hyperflächen gekreuzt.

Daher bleibt entlang des Pfades aus TRANSFER-B die **zyklische**
Reihenfolge aller 96 Wände konstant.

Ein einzelner Wandpunkt darf dabei den gewählten Kreisursprung
\(0\equiv L\) überqueren; dies verändert nur eine lineare Listendarstellung,
nicht die zyklische Reihenfolge.

Somit:

\[
\boxed{
\text{gleicher Tope}
\Longrightarrow
\text{gleiche zyklische }B_{96}\text{-Ordnung}.
}
\]

---

### TRANSFER-D — genau der für M1 benötigte Schluss

M1-FULL benötigt keine globale topologische Isotopie der gesamten
Anordnung.

Benötigt werden nur:

1. dieselben offenen Parameterkammer-Signvektoren;
2. dieselbe zyklische Reihenfolge der 96 Kreiswände in jeder Kammer;
3. damit dieselbe Zuordnung der 96 offenen Kreisatome.

TRANSFER-A bis C liefern genau diese Daten.

Daher folgt, **sofern der obige Cryptomorphie-Schritt korrekt angewendet
ist**, dass die exhaustive Referenzprüfung

\[
64\times96=6144
\]

auf jedes \(r\in(3,4)\) übertragen werden darf.

---

## Aktualisierte Kernfragen für den unabhängigen Review

1. Ist die Verwendung der Chirotop-Cryptomorphie aus BLSWZ Chapter 3,
   insbesondere Section 3.5, in der Form
   \[
   \chi_r=\chi_{r'}\Rightarrow
   \text{identische Covektor-/Topemengen}
   \]
   korrekt?

2. Schließt die explizite Mitführung von \(g_\infty\) im AFF-CHIRO-Prüfer
   die relevante projektiv/affin-Ambiguität vollständig?

3. Ist für ein realisierbares affines Hyperflächenarrangement die Menge zu
   einem festen Tope-Signvektor tatsächlich ein konvexer Schnitt offener
   Halbräume und daher genau eine Kammer?

4. Ist \(\widetilde C_T\subset\mathbb R^4\) wegen der Affin-Linearität
   der rechten Seiten \(b_i(r)\) tatsächlich konvex, so dass ein
   kollisionsfreier Pfad zwischen Referenz- und tatsächlichem \(r\)
   innerhalb desselben Topes existiert?

5. Ist die elementare Aussage korrekt, dass sich die zyklische Reihenfolge
   endlich vieler gelabelter Kreispunkte entlang eines stetigen Pfades nur
   bei einer Paar-Kollision ändern kann?

6. Erfasst GATE1R wirklich sämtliche solchen Paar-Kollisionen der 96
   Matrixwände durch die 18 zertifizierten Hyperflächen?

7. Reichen A–C für M1-FULL aus, so dass **keine** volle ambient isotopy und
   insbesondere kein Einsatz des Folkman–Lawrence-Repräsentationssatzes
   benötigt wird?

8. Bleibt der Schluss strikt auf offene Parameterkammern und offene
   Kreisatome beschränkt, so dass Boundary-Sets erst im anschließenden
   a.e.-Schritt ignoriert werden?

9. Folgt aus TRANSFER weiterhin keinerlei Aussage über
   \[
   \ker\Gamma_I?
   \]
   Erwartete Antwort: ausdrücklich nein.

---

## Literatur

1. A. Björner, M. Las Vergnas, B. Sturmfels, N. White, G. M. Ziegler,
   *Oriented Matroids*, 2nd ed., Cambridge University Press, 1999,
   Chapter 3, insbesondere Section 3.5.

2. G. M. Ziegler,
   *Oriented Matroids Today*,
   Electronic Journal of Combinatorics 3 (1996), Dynamic Survey 4,
   Section 2. Dort wird ausdrücklich festgehalten, dass Chirotop,
   Covektoren, Cocircuits, Vektoren und Circuits äquivalente Datensätze
   sind und einander eindeutig rekonstruieren.

3. A. Björner et al., loc. cit., Chapter 5 nur als Hintergrund zum
   Topological Representation Theorem; dieser Satz wird für den hier
   formulierten TRANSFER-D **nicht** benötigt.


---

## Finales Hardening / Verdict (2026-08-30)

Die zuvor noch ausdrücklich verlangte mechanische Härtung ist nun im
committeten Branch-Stand ausgeführt und durch einen read-only GitHub-Actions-
Runner erfolgreich reproduziert worden.

### Mechanisch gehärtete Invarianten

1. **Rang 4.** In
   `scripts/certify_sw1_a10_c1b2a_affine_chirotope.py`
   (Blob `b92f7778bffe29fa11a76e2c260d1e12ae7b27c5`) wird der explizite Minor
   
   \[
   (B_e,B_R,D_{s0},INF)
   \]
   
   ausgewertet und durch
   
   \[
   \det=-1\neq 0
   \]
   
   als Rang-4-Zeuge asserted.

2. **Loopfreiheit.** Derselbe Prüfer asserted, dass alle 22 räumlichen
   Hyperflächennormalen ungleich Null sind und dass auch das ausgezeichnete
   Element
   
   \[
   g_\infty=(0,0,0,1)
   \]
   
   ungleich Null ist.

3. **Affine Chartwahl.** Derselbe Prüfer bildet symbolisch
   
   \[
   y=(\sigma,R,\varepsilon,1)
   \]
   
   und asserted exakt
   
   \[
   g_\infty\cdot y=1>0.
   \]
   
   Damit ist die verwendete affine Covektor-Chartbedingung
   \(X_\infty=+\) mechanisch verankert.

4. **Fester Kreis.** In
   `scripts/certify_sw1_a10_c2_gate1r_96_collision_hyperplanes.py`
   (Blob `18f992d117580260eb3865a493773d1b73833726`) wird die Normierung
   
   \[
   \widehat\theta=\theta/L(r)\pmod 1\in\mathbb R/\mathbb Z
   \]
   
   explizit implementiert. Der Prüfer asserted \(L(r)=4+10r>0\) auf dem
   Projektintervall und kontrolliert an einem zertifizierten generischen
   Referenzpunkt exakt, dass alle 96 Labels erhalten bleiben und die
   steigende bzw. zyklische Ordnung durch die positive Skalierung unverändert
   bleibt. Die bereits vorhandene GATE1R-Schleife läuft weiterhin über alle
   \(\binom{96}{2}=4560\) ungeordneten Paare modulo \(L\).

### Reproduzierbare CI-Provenienz

Workflow-Blob:

`7a6dc40a2c7881dbefd7f1641f91ddbf256f93c4`

Head-Commit:

`2fdb8f33e9e813dd0e5061dbfe00ec1d48c0158a`

GitHub-Actions-Run:

- Run: `33328052407`
- Job: `99301594041`
- Ergebnis: **SUCCESS**

Der Runner checkte den exakten Commit aus, protokollierte die Blob-Hashes,
installierte die gepinnte exakte Abhängigkeit `sympy==1.14.0` und führte in
diesem Commit nacheinander erfolgreich aus:

- C1B2A AFF-CHIRO hardening;
- C1B2A GATE1R circle hardening;
- die unveränderte vollständige M1-FULL-Regression über alle
  \(64\times96=6144\) offenen Referenzatome.

### Finales Review-Verdict

Die mathematische Transferkette benötigt keine ambient isotopy und keinen
Folkman--Lawrence-Schritt. Die Standard-Cryptomorphie liefert aus dem
konstanten gelabelten affinen Chirotop denselben orientierten Matroiden und
damit dieselben affinen Covektor-/Topemengen. Die festen Toperegionen sind
konvexe Schnitte offener Halbräume; im erweiterten \((r,\sigma,R,\varepsilon)\)-
Raum bleiben sie wegen der linearen Ungleichungen konvex. GATE1R erfasst
sämtliche B96-Paar-Kollisionen modulo \(L\); innerhalb eines festen offenen
Topes wird daher keine Kollisionswand gekreuzt, und die normierte zyklische
96er-Kreisordnung bleibt konstant.

Daher wird im exakt dokumentierten Scope gebucht:

\[
\boxed{\mathrm{C1B2A\text{-}CHIRO}\;\checkmark[M]}
\]

\[
\boxed{\mathrm{C1B2A\text{-}TRANSFER}\;\checkmark[M]}
\]

und damit

\[
\boxed{
\mathrm{M1\text{-}FULL}(7/2)\Longrightarrow
\mathrm{M1\text{-}FULL}(r),\qquad 3<r<4.
}
\]

**Scope-Firewall:** Diese Buchung betrifft ausschließlich offene
Parameterkammern und offene Kreisatome sowie deren Transfer. Sie liefert
keine Cross-Gram-Injektivität, keine Aussage über \(\ker\Gamma_I\), keinen
HT-RED-Schluss, kein Objekt-X-Zertifikat und keinen RH-Schluss.
