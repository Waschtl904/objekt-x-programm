# Unabhängiger Merge-Audit — PR66, 68, 74, 78, 80, 81

## Aktueller Stand nach enger Korrekturprüfung — 2026-09-07

**Alle sechs additiven Journaltexte sind an den unten bezeichneten Heads READY im dokumentierten Scope.** Die früheren Blocker von #78/#80 sind geschlossen; ihre Begründungen und ursprünglichen Identitäten bleiben im historischen Erstbericht weiter unten erhalten. Dies ist keine Theorem-Promotion, keine transitive Freigabe anderer Vorfahren und kein pauschales numerisches GREEN.

| PR | Aktuelles Urteil | Exakter geprüfter Head | Geprüfter Dokument-Blob |
|---|---|---|---|
| [#66](https://github.com/Waschtl904/objekt-x-programm/pull/66) | READY im dokumentierten Scope | `7d8a9e47c96962f49afedba83f1090a1598f5386` | `c6b2645b9153342c1c7b03146b2cda2e8af8ee50` |
| [#68](https://github.com/Waschtl904/objekt-x-programm/pull/68) | READY im dokumentierten Scope | `b9b3b70929df482588ad07c96dc3c1c06faa2fce` | `422f58613a79fd434c88c90866b82a1822f9bf9e` |
| [#74](https://github.com/Waschtl904/objekt-x-programm/pull/74) | READY im dokumentierten Scope | `117cb0afdde12b984808fbf97d24c28252a81acb` | `4d5574e85f9190bcddb6e957606461e033176263` |
| [#78](https://github.com/Waschtl904/objekt-x-programm/pull/78) | READY im dokumentierten Scope | `6807d1e04588de81d0e5b4c14a0a4e8e5756ba97` | `c1890870b889c8fb539b353a713c4bb41c58926f` |
| [#80](https://github.com/Waschtl904/objekt-x-programm/pull/80) | READY im dokumentierten Scope | `483421fe5eb94a4474103083ec998f4dfa3e4266` | `54515081a9213e0eb9215e7ff7e772d182ef5ab8` |
| [#81](https://github.com/Waschtl904/objekt-x-programm/pull/81) | READY im dokumentierten Scope | `4ca4abb37e7fcaa8d045e94ad5f816d481ec40d0` | `db11be66e49cf70f8581efb9ccbcf0d7f7c20aa8` |

Die Korrektur-Heads #78/#80 sind **lokal** geprüft und liegen jeweils unmittelbar auf dem zuvor geprüften PR-Head; ein GitHub-Publish dieser Heads wurde nicht geprüft oder durchgeführt. Beide Korrekturcommits ändern ausschließlich ihre jeweilige Audit-Datei. Die neuen Blobs sind von den historischen, im eingefrorenen Tip vorhandenen Blobs zu unterscheiden; der Erstprüfungs-Tip bleibt `a7f00fd6ef4824f2aecc934b52088127112a2b5f`. Identitäten und Korrekturdiffs sind ergänzend in `audit_reverse_recheck_identities.json` und `audit_reverse_pr78_correction.diff` / `audit_reverse_pr80_correction.diff` erfasst.

### Geschlossene Befunde — nur Korrekturdiffs nachgeprüft

| PR / bisheriger Befund | Korrektur am neuen Head | Nachprüfung |
|---|---|---|
| #78: fehlende Mindestbreite für OK20 | Z. 270–276 setzt festes, ausreichend großes `L0` anhand Bandbreite und Schwelle; Z. 287–308 schließt die untere Vergleichsaussage für beliebig kurze Intervalle ausdrücklich aus und erhält OK21 mit `1+L` für alle `L>0`. | **Geschlossen.** ([PR #78](https://github.com/Waschtl904/objekt-x-programm/pull/78)) |
| #80: verlorenes `1+L` | Z. 12–18, 119–127, 161–175 und 229–234 führen den Faktor konsistent in Profil, Integral, Restterm und Schlussabschätzung; Z. 180–198 behält ausschließlich die gültigen kurzen/dyadischen Konsequenzen. | **Geschlossen.** ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80)) |
| #80: fehlende Hub-Aktivierung | SC20 enthält in Z. 315 `p^k<=e^{2U}`; Z. 322–324 erklärt ausdrücklich, dass `P_U` den Cutoff nicht ersetzt. | **Geschlossen.** ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80)) |
| #80: nicht reproduzierbare Gaußtabellen | Z. 270–277 zieht die Zahlen samt Anspruch zurück; Z. 252–268 behält nur die schon geprüfte Konstantentabelle mit explizitem Raster, strengem Collar und `2r/61`, einschließlich korrigierter Rundung bei `r=16`. Kein neues Experiment. | **Geschlossen durch Rücknahme, nicht numerisch bestätigt.** ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80)) |
| #80: möglicher Übergang vom primitiven Kernelzeugen zum vollständigen Restgraphen | Z. 27, 204–207, 223–246, 289–292 und 351–355 beschränkt die Schärfeaussage konsistent auf SC4 plus L2-Normierung / primitives Modell; kein Vollgraph-Kernel- oder Vollgraph-Einheitsballsatz bleibt gebucht. | **Scope-Klarstellung abgeschlossen.** ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80)) |

**Closure:** #78 `6807d1e04588de81d0e5b4c14a0a4e8e5756ba97` und #80 `483421fe5eb94a4474103083ec998f4dfa3e4266` können aus diesem eng begrenzten Dokumentreview heraus als korrigierte bestehende PR-Heads veröffentlicht werden. READY66/68/74/81 bleibt unverändert auf deren oben bezeichnete additive Texte beschränkt; keine erneuten Experimente, keine Beweiserweiterung und keine Prüfung anderer Korrektur-PRs.

---

## Historischer Erstbericht — damalige Blocker, inzwischen wie oben geschlossen

Die folgenden Urteile und Zeilenangaben dokumentieren ausschließlich die **ursprünglichen** Heads; sie sind keine noch offenen Blocker der oben nachgeprüften Korrektur-Heads.


## Ergebnis und Prüfgrenze

**READY als additive Journaltexte: #66, #68, #74, #81. BLOCKED am exakten Head: #78, #80.** Maßstab ist die sachliche Richtigkeit innerhalb des dokumentierten lokalen/bedingten Scopes, ausdrücklich **keine Theorem-Promotion**; offene RH-/Strong-Terminal-/FD23-Ziele sind keine Blocker. Die Einzelurteile betreffen die jeweiligen additiven Änderungen, nicht eine transitive Freigabe ihrer gesamten Vorfahren.

Read-only geprüft gegen den eingefrorenen Repository-Tip `a7f00fd6ef4824f2aecc934b52088127112a2b5f`; jeder PR fügt genau die unten genannte Datei hinzu, und jeder geprüfte Blob ist im eingefrorenen Tip identisch vorhanden. Autoritative Heads: `open_prs.json`; vollständige lokale Identitätsaufnahme: `audit_reverse_identities.json`. Keine Repository-Edits, keine GitHub-Schreiboperationen. Die frühere Prüfung der separaten lokalen `fe907714`-XBAND-Datei wurde **nicht** als Zustimmung zu diesen Heads gewertet.

## Exakte Identitäten

Alle Dokumentpfade lauten `audits/P11_R43_<Dokument>_2026-09-06.md`; die Zeilenangaben unten beziehen sich auf den jeweiligen unveränderten Blob.

| PR | Urteil | Exakter Head | Dokument | Git-Blob |
|---|---|---|---|---|
| [#66](https://github.com/Waschtl904/objekt-x-programm/pull/66) | READY im dokumentierten Scope | `7d8a9e47c96962f49afedba83f1090a1598f5386` | `COND_DIRECT_FLAGDYN_REVERSE_NORMAL_BRIDGE` | `c6b2645b9153342c1c7b03146b2cda2e8af8ee50` |
| [#68](https://github.com/Waschtl904/objekt-x-programm/pull/68) | READY im dokumentierten Scope | `b9b3b70929df482588ad07c96dc3c1c06faa2fce` | `REVERSE_NORMAL_SCHUR_EXTENSION_REDUCTION` | `422f58613a79fd434c88c90866b82a1822f9bf9e` |
| [#74](https://github.com/Waschtl904/objekt-x-programm/pull/74) | READY im dokumentierten Scope | `117cb0afdde12b984808fbf97d24c28252a81acb` | `REVERSE_SHIFT_VARIANCE_MEAN_H1_FIREWALL` | `4d5574e85f9190bcddb6e957606461e033176263` |
| [#78](https://github.com/Waschtl904/objekt-x-programm/pull/78) | BLOCKED | `a9d1f1a944bbb154db7bdb5844135501630bda5c` | `REVERSE_OCCUPANCY_KERNEL_FIREWALL` | `df405768531da4b138a026c640f0a8353bd02674` |
| [#80](https://github.com/Waschtl904/objekt-x-programm/pull/80) | BLOCKED | `645d2bafe3c0f74fbfc769d4958ecf93316ae165` | `SHELLWISE_COLLAR_COMMON_MODE_FIREWALL` | `cb0b086ee122e59455c24ab6b258388aaa5d8ccf` |
| [#81](https://github.com/Waschtl904/objekt-x-programm/pull/81) | READY im dokumentierten Scope | `4ca4abb37e7fcaa8d045e94ad5f816d481ec40d0` | `REVERSE_REFLECTION_COMMON_MODE_FIREWALL` | `db11be66e49cf70f8581efb9ccbcf0d7f7c20aa8` |

## Blocker und kleinste Korrekturen

### #78 — fehlender Bereich für die zweiseitige Occupancy-Asymptotik

**Z. 261–278, insbesondere Z. 270 und OK20:** Die Anzahl voller logarithmischer Bänder ist nicht für beliebiges `L=V-U>0` mit `1+L` vergleichbar; ein kurzes Intervall `(U-u,V-u)` kann überhaupt kein `log p` enthalten, sodass `omega_+(u)=0`, während die rechte Seite von OK20 strikt positiv ist. Der Zusatz „away from only O(1) endpoint-band effects“ benennt das Problem, definiert aber keinen zulässigen Parameterbereich für die gebuchte zweiseitige Aussage. ([PR #78](https://github.com/Waschtl904/objekt-x-programm/pull/78))

**Minimalfix:** OK20 ausdrücklich auf `L>=L0` beschränken, wobei ein festes `L0` genügend volle Chebyshev-Bänder garantiert; für alle `L>0` nur die bereits richtige obere Schranke mit `1+L` aus OK21 beanspruchen. Das unter OK22 ausdrücklich betrachtete dyadische Regime `L asymp U` sowie der negative Befund zur bloßen Supremumsabschätzung bleiben davon unberührt. ([PR #78](https://github.com/Waschtl904/objekt-x-programm/pull/78), Z. 281–319)

Die übrige Ableitung ist konsistent: tatsächliches Gewicht `(log p)(p-1)p^(-3/2)`, lokale Nenner `1+W_+(u+log p)`, Variable am Mittelpunkt versus Endpunkt, gegenüberliegende Randlage und der Verlust `U * O(log U/U)=O(log U)` werden korrekt unterschieden. ([PR #78](https://github.com/Waschtl904/objekt-x-programm/pull/78), Z. 34–126, 138–230, 334–373)

### #80 — zwei falsche Formeln und eine offene Reproduzierbarkeitslücke

1. **SC0, Z. 9–17; Weiterverwendung SC12–SC13, Z. 156–179:** Der Faktor `1+L` aus PR78 OK21 wird ohne Untergrenze für `L` durch `L` ersetzt. Eine atomare Primverschiebung widerlegt die uniforme punktweise Aussage: fixiere ein großes `U` und ein `p` mit `U<log p<2U`; für `u_L=U+L/2-log p` enthält `omega_+(u_L)` bei `L -> 0+` den positiven, nicht gegen null gehenden Summanden `w_p/(1+W_+(U+L/2))`, während `L exp(-(U+u_L)/2) -> 0`. ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80), Z. 9–17; [PR #78](https://github.com/Waschtl904/objekt-x-programm/pull/78), Z. 160–169, 281–294)
   **Minimalfix:** Für uneingeschränkte Schrittweiten durchgehend `1+L` verwenden, also insbesondere `O((1+L)/U)+(1+L)exp(-cU)`; alternativ einen festen positiven Mindestschritt explizit voraussetzen. Die dyadische Schlussfolgerung „nur O(1), kein Zerfall aus dieser Majorante“ und die qualitativen `L=O(1)`-/`L=O(log U)`-Folgen bleiben korrekt. ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80), Z. 177–197)

2. **SC20, Z. 313–322:** In der als exakte Hub-Formel angegebenen Summe fehlt die Aktivierung `p^k<=exp(2U)`; dieselbe eingefrorene Definition wird in PR74 VM25 ausdrücklich mit dieser Grenze wiedergegeben. Projektion `P_U` ersetzt den Cutoff nicht: Halbverschiebungen `U<a=k log p/2<U+R` können bei festem Quellsupport noch im Terminalfenster liegen. ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80), Z. 313–322; [PR #74](https://github.com/Waschtl904/objekt-x-programm/pull/74), Z. 424–444)
   **Minimalfix:** SC20 auf `sum_{p,k: p^k<=exp(2U)}` beschränken; die behauptete Paritätsumkehr bleibt richtig. ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80), Z. 313–332)

3. **Diagnosetabellen Z. 239–281:** Die Gaußprofile und der konkrete Collar-Zählrand werden nicht definiert; mit den referenzierten PR72/76-Profilen und dem durch die Konstantentabelle festgelegten äußeren Collar `|z|>U-r` reproduzieren sich die Gaußwerte nicht. Beispiel `r=16`: center-gauss12 ergibt `3.4916926899e-5` statt `1.5e-3`, edge-gauss-wide `2.1372784977e-3` statt `9.82e-4`, edge-gauss-narrow `2.0174983290e-3` statt `1.016e-3`; die Konstantentabelle reproduziert sich hingegen bis auf Rundung (`32/61=0.524590...`). ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80), Z. 239–289; lokale Nachrechnung: `audit_reverse_local_checks.json`, Referenzdefinitionen `P11_R43_REVERSE_MEAN_LOCALIZATION_DIAGNOSTIC_2026-09-06.py`, Z. 79–87, 148–153)
   **Minimalfix:** Entweder tatsächlich verwendete Profile/Parameter, Collar-Konvention und reproduzierbare Berechnung ergänzen, oder Zahlen an die Referenzprofile anpassen beziehungsweise die nicht reproduzierten Tabellen entfernen. Ihre ausdrückliche Einstufung als reine Diagnose verhindert eine Theorem-Promotion, macht nicht nachvollziehbare Zahlen aber nicht überprüft. ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80), Z. 239, 283–289)

Die Radiusuniformität von SC1–SC4 und die Stieltjes-Rechnung sind sachlich richtig; mit dem korrekten Streifenfaktor liefern sie die oben angegebene Schranke. Der konstante Modus ist als **primitiver** Residual-Differenzmodus zu lesen, nicht als behaupteter Nachweis eines konstanten Anteils im kanonischen `x_rev` oder als Kernelidentität für den vollständigen Restoperator. ([PR #80](https://github.com/Waschtl904/objekt-x-programm/pull/80), Z. 34–85, 89–163, 201–233)

## READY-Urteile im jeweiligen dokumentierten Scope

- **#66 — READY:** Die Pullbacks und die Kompression `W_U^* A_S W_U=A_R` sind typgerecht; der Cap gilt einseitig, und das Jensen-/Quadratwurzelargument liefert BR17 und BR31 mit dem Faktor `3/2`. Die Reverse-Normalgröße ist korrekt `rho_rev=(||C_R^(-1) epsilon_R||²-1)_+`, nicht der positive Vorwärtszuwachs. ([PR #66](https://github.com/Waschtl904/objekt-x-programm/pull/66), Z. 74–193, 197–351, 363–489)
  Der zweidimensionale Gegenmechanismus widerlegt nur die abstrakte Ableitung aus einem einseitigen Cap; der Übergang zur FD23-Summe setzt sowohl BR39 als auch BR42 ausdrücklich voraus. Kein Schluss auf GEO/NEW/Phase oder Strong Terminal wird gebucht. Nicht blockierender Satzfehler: Z. 556 zeigt `e0.` statt `\ne0.`; Text und BR34 machen die beabsichtigte Nichtnullaussage eindeutig. ([PR #66](https://github.com/Waschtl904/objekt-x-programm/pull/66), Z. 493–578, 599–678, 731–759)

- **#68 — READY:** `f_rev=G_cond^(-1/2) epsilon_R` hat `q_cond(f_rev)=1`; daher `rho_rev=(-Delta s_cond(f_rev))_+=(<x_rev,K_Schur x_rev>)_+`, mit dem richtigen Vorzeichen und ohne zusätzlichen Normierungsfaktor. `Q=B_U#Btilde` ist der inverse geometrische Transport, und `Q A_U Q=Btilde` gibt die exakte alte Graphnormalisierung `||x_rev||²+||R_U x_rev||²<=1`, ohne Zirkelschluss über `rho_rev`. ([PR #68](https://github.com/Waschtl904/objekt-x-programm/pull/68), Z. 65–111, 116–247, 260–312)
  **Typprüfung:** `M:H_U -> Z_V`, `S:N -> Z_V`, somit `S^*M:H_U -> N` (alt → neu); `y_*=(I+S^*S)^(-1)S^*Mx` liegt korrekt im neuen Streifen. RE19–RE23 behalten den exakten gesättigten Nenner; ein billiger Versuchskorrektor und Zerfall bleiben offen. ([PR #68](https://github.com/Waschtl904/objekt-x-programm/pull/68), Z. 30–63, 357–469, 473–542)

- **#74 — READY:** Paargewichte `w_p w_q/(2W)`, unnormalisierter Koeffizient `S_2` statt `S_2/W`, Minimierer und Mean-Penalty `W/(1+W)|m|²` sind korrekt. Die Integration nimmt ausdrücklich einen festen aktiven Primzahlsatz an; variable lokale Nenner werden dadurch nicht durch einen globalen Nenner ersetzt. ([PR #74](https://github.com/Waschtl904/objekt-x-programm/pull/74), Z. 42–208, 212–343)
  Das Negativresultat betrifft allein „Varianz genügt“ im primitiven Least-Squares-Modell; `Q<=I` wird nicht zu `Q<=B_U`, Sobolev-Regularisierung oder einer echten `x_rev`-Abschätzung verstärkt. ([PR #74](https://github.com/Waschtl904/objekt-x-programm/pull/74), Z. 243–277, 356–461, 465–505)

- **#81 — READY:** Die feste Quelle einschließlich `epsilon_R` liegt im ungeraden Sektor; inverse Quellmetrik/Nullfortsetzung bleiben dort, `H_U^*` macht den Hub gerade, und Reflexionssymmetrie des vollständigen Rest-Normaloperators vererbt sich auf beide Resolventen und `Q`. Damit ist `x_rev` gerade; die Aussage ist keine Behauptung eines tatsächlich nichtverschwindenden konstanten Koeffizienten. ([PR #81](https://github.com/Waschtl904/objekt-x-programm/pull/81), Z. 106–162, 172–224, 234–430)
  Die terminale Mittelwertformel RF28 stimmt: bei `a<=U-R` null, bei `U-R<a<=U` gleich `-2 int_{U-a}^R g(t) dt` in der angegebenen Translationskonvention; das globale Hub-Adjunktvorzeichen ist davon getrennt. Der eindeutige Least-Squares-Korrektor ist bei geradem Eingang gerade, nicht paritätsbedingt gegenläufig auf den Streifenseiten. Das negative Scope bleibt auf universelle/paritätsbasierte Abkürzungen beschränkt. ([PR #81](https://github.com/Waschtl904/objekt-x-programm/pull/81), Z. 434–521, 525–617)

## Abschluss

Vollständige sechs Dokumente und die benötigten lokalen Elterndefinitionen geprüft; kein pauschales numerisches GREEN. Die Kontrollrechnungen betreffen nur einzelne algebraische Identitäten und die angegebenen endlichen Proxy-Collarwerte, niemals den kanonischen Reverse-Vektor oder terminale Grenzwerte. Mit den oben genannten Minimalfixes ist der abgegrenzte Review-Auftrag abgeschlossen; keine zusätzlichen Forschungsrichtungen und keine Promotionsanforderungen.
