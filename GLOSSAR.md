# Glossar

Notation und Begriffe des Objekt-X-Programms. Verbindliche Rechenregeln stehen in
[KONVENTIONEN.md](KONVENTIONEN.md); bei Widersprüchen hat jene Datei Vorrang.

---

## Zentrale Objekte

| Symbol | Bedeutung | Quelle |
|---|---|---|
| **Objekt X** | $\bigl(A_{2D}^r, [\tilde\omega_2], [L_3], \mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}}, m\xrightarrow{p} pm\bigr)$ — das zentrale zusammengesetzte Operatorobjekt mit fünf Schichten | Ebene XVI |
| $A_{C^*}$, $A_{\mathbb Q}^{\mathrm{alg}}$ | Bost–Connes-Algebra, C\*-Version bzw. algebraische Version | KONVENTIONEN §1 |
| $\mathcal H_{\mathrm{rel},N}$ | relativer Primkantenraum $\bigoplus_{p\le N}\bigoplus_m \mathcal H_{m\to pm}$ | NEU-44 |
| $\mathrm{Wres}_{\mathrm{rel}}$ | kantendiagonale Hebung der Wodzicki-Residuum-Spurform | NEU-44 |
| $\mathbb F_N^{\mathrm{rel}}$ | relativer Feshbach-Operator | NEU-44/45 |
| $D_N^{\mathrm{rel}}$, $D_{\mathrm{rel}}$ | relativer Dirac-artiger Operator, endlich bzw. im Limes | NEU-52/53 |
| $J^-$ | negativer Jacobi-Operator; $A_N^{\mathrm{Jac},-}$ die zugehörige Matrixfamilie | NEU-56/59 |
| $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ | renormalisierte relative Selbstenergie $\sum_p \frac{p^{-\beta}}{1-p^{-\beta}}P_p$ | NEU-136 |
| $R$ | unbeschränkte primdiagonale Observable, $R_p = \log p/\lvert c_p\rvert^2$ | NEU-144 |
| $m_{\mathrm{arith}}$ | Spektralschatten $\Pi_\gamma(X)$ — **nicht** $X$ selbst | NEU-114 |
| $W_\xi$, $Q_{\mathrm{Weil}}$ | Weil-Distributionsobjekt bzw. Weil-Quadratform | NEU-113/220l |
| $\Xi$, $M_\Xi(w)$ | Riemannsche Xi-Funktion, zugehörige Momenterzeugende | NEU-220u/w |

## Kohomologische Struktur

| Symbol | Bedeutung | Quelle |
|---|---|---|
| $[\tilde\omega_2]$ | Hochschild-2-Klasse in $HH^2$ | Ebene XVI |
| $[L_3]$, $L_3^\circ$ | Hochschild-Klasse in Grad 3/4 bzw. deren Fourierladungsanteil $\sum_{s,m}\ell_{s,m}e_sV_m$ | NEU-20/42/161 |
| $L^{\mathrm{cup}}_{g;\mathbf p}$ | geladener Cup-Aufstieg in $Z^4(A_{\mathrm{alg}},M)_g$ | NEU-218 |
| $\tilde L_0$ | kanonischer Basislift $\eta_0\circ j_M\circ L^{\mathrm{cup}}_{g;\mathbf p}$ | NEU-219r |
| $[\Omega_{\mathbf p}]$ | geladene $HH^4$-Klasse des Vier-Prim-Polynommodells | NEU-178/185 |
| $D_g$ | geladene Derivation vom Grad $g$ | NEU-211/216/217 |
| $\mathcal B^{\log}$ | logarithmischer Koeffiziententyp mit Norm $\lVert f\rVert_\infty + [f]_{\tan} + [f]_{\mathrm{rad}}$ | NEU-216 |
| $\mathcal A^{\log}$ | geladener Koeffiziententyp $\operatorname{span}\{\mu_m\mathcal B^{\log}\mu_n^*\}$ | NEU-216 |
| $\kappa$, $\varepsilon$, $s$ | Orbitindex, Gewichtsexponent, Rotationsexponent im O-219-Strang | NEU-219p–t |

## BC-Algebra-Notation

| Symbol | Definition |
|---|---|
| $\mu_k$ | Isometrien: $\mu_k^*\mu_k = 1$, $\mu_k\mu_k^* = E_k \neq 1$ für $k>1$ |
| $e(r)$ | Charaktere: $e(r)^* = e(-r)$, $e(r)e(s) = e(r+s)$, $e(0)=1$ |
| $\rho_k(f) = \mu_k f\mu_k^*$ | Range-Endomorphismus, **nicht unital** |
| $\sigma_k(f) = \mu_k^* f\mu_k$ | unitaler Endomorphismus, $(\sigma_k f)(x) = f(kx)$ |
| $T_a := \sigma_a$ | kanonische Translation |
| $E_k = 1_{k\hat{\mathbb Z}}$ | Rangeprojektionen |
| $\sigma_\beta$, $\omega_\beta$ | modulare Zeitentwicklung bzw. KMS-Zustand bei inverser Temperatur $\beta$ |
| $L_j = (j+1)!$, $S_j$, $\nu(x)$ | Faktorialschalen, Schalenindex | 

## Analytische Werkzeuge

| Begriff | Rolle im Programm |
|---|---|
| **Feshbach-Reduktion** | Elimination des Nicht-Primkanal-Sektors; erzeugt die Selbstenergie $\Sigma$ |
| **Fourier-Hebung** | überträgt den Mangoldt-Faktor $\log p$ in den relativen Kantenraum ($T_p^{\mathrm{rel}} = \log p$) |
| **PSWF** | prolate sphäroidale Wellenfunktionen; spektrale Brücke zur Edge-Koerzivität |
| **Primschalen-Abel-Lemma** | dyadische Zerlegung $p\sim 2^m$ zur Kontrolle von Kanalsummen |
| **Nelson-Kommutator-Methode** | Nachweis essentieller Selbstadjungiertheit über Schur-Test und Konfinement |
| **Birman–Schwinger-Indexsatz** | Spektralalternativen für die relative Determinante |
| **Herglotz-Funktion** | Funktion mit $\Im f > 0$ auf der oberen Halbebene; Herglotz-Eigenschaft von $m_{\mathrm{arith}}$ ist RH-äquivalent |
| **Stieltjes-Momentproblem** | liefert die Hankel-Charakterisierung: beide Hankelfamilien positiv semidefinit $\iff$ darstellendes Maß auf $[0,\infty)$ |
| **KMS-Zustand** | Gleichgewichtszustand der BC-Zeitentwicklung; Quelle des Faktors $g^{-\beta}$ im O-219-No-Go |
| **Morita-Induktion / Eckkern** | Transport von Koeffizientenmoduln entlang der adelischen Dilatation |
| **Laca-Dilatation** | automorphe Dilatation der Endomorphismen $\rho_n$ |

## Prozessbegriffe

| Begriff | Bedeutung |
|---|---|
| **Journaleintrag NEU-XXX** | fortlaufende Nummer, keine Qualitätsangabe |
| **Knoten `[O-...]`** | eindeutig bezeichnete offene Frage; Knoten bilden einen DAG |
| **Direktaudit** | Prüfung einer Behauptung gegen ihre Primärquelle im Repository |
| **Rücklese** | erneutes Lesen eines früheren Eintrags mit aktuellem Kenntnisstand |
| **Triage** | Fallunterscheidung zur Auswahl des weiterzuverfolgenden Pfades |
| **Zeugenroute** | Konstruktionsstrategie über ein explizites nichtverschwindendes Element |
| **No-Go** | gesichertes Negativresultat, das eine Route dauerhaft schließt |
| **Welt 1 / Welt 2** | Normierungsalternativen des Primkanals; Welt 2 ($\lVert\varepsilon_p\rVert^2=1$) wurde in NEU-135D gewählt |
| **Spur A / Spur B** | Spektralschatten-Spur bzw. X-Rückbindungs-Spur (ab NEU-114) |
| **Weg A / Weg B** | Zugang über $\tilde L$ bzw. über die reine Spektralmaß-Form; Weg B ist der robuste Standard (NEU-56) |
