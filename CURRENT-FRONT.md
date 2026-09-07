# CURRENT FRONT — Objekt X / P11 Strong Terminal

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand (Governance):** 7. September 2026; mathematische Darstellung unverändert.<br>
> **Volatile PR-/SHA-Single-Source:** [`00-uebersicht/ACTIVE_FRONT.yaml`](00-uebersicht/ACTIVE_FRONT.yaml)  
> **Live-main-Policy:** Der aktuelle `main`-Head wird direkt aus GitHub gelesen und absichtlich nicht als SHA in einer versionierten Repo-Datei selbst gespeichert.  
> **Kanonische Roadmap:** [`00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)  
> **Theorem-/Reviewstatus:** [`00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md)  
> **Objekt-X-Definition:** [`00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)

Diese Datei ist eine **Navigationsschicht**, kein Beweis und keine Promotion. Bei Konflikten entscheiden die kanonischen mathematischen Quellen.

---

## 1. Aktuelles Ziel

Die aktive Hauptfront ist **B / Strong Terminal**, derzeit **R43**.

Für jedes feste

\[
0<R<S
\]

ist Strong Terminal / C6 auf die verbleibende Normalbahn reduziert. Das operative Observable ist

\[
L_{R,S}^{T,U}
:=
\operatorname{Re}
\langle\varepsilon_R,K_{R,S}^{T,U}\varepsilon_R\rangle,
\]

mit Ziel

\[
\boxed{L_{R,S}^{T,U}\to1\qquad(T,U\to\infty).}
\]

Exakter Registry-Governance-String für R38–R42:

```text
FROZEN — independently verified AI-GREEN
```

Die Registry stellt klar, dass dieser projektinterne String nicht automatisch als formaler `independent GREEN (cross-model/certificate/human)`-Subtyp gelesen werden darf. R43 bleibt OPEN.

R37/G4c bleibt **separat offen** und wird durch R38–R43 nicht rückwirkend geschlossen.

---

## 2. R43-Stack und Integrationsstand

Die exakten Heads, Parent-Heads, Branches und GitHub-States stehen ausschließlich in `ACTIVE_FRONT.yaml`.

**Historische Abhängigkeitskette:** `base`, Heads und Parent-Heads in `ACTIVE_FRONT.yaml` bewahren die ursprünglichen Review-Beziehungen aller 20 R43-PRs; `github_base` bezeichnet separat das gebuchte GitHub-Ziel. Der historische Stack-Root-Base-Pin bleibt unverändert. GitHub-Mergestatus und offene Anzahl werden ausschließlich dort nach belegten Merge-Ereignissen geführt; der aktuelle `main`-Head wird live aus GitHub gelesen.

`head_sha`/`parent_head_sha` sind **historical_dependency_pins**, nicht heutige Branch-Heads. Der tatsächlich freigegebene und gemergte Head steht separat als `merged_head_sha`; nach Review-Korrekturen (etwa PR #64/#78/#80) kann er vom historischen Pin abweichen, ohne die Parent-Kette umzuschreiben.

Die folgenden vier Container bilden den historischen Anfang der Kette, nicht den gesamten aktuellen Integrationsstand:

| Container | Rolle |
|---|---|
| PR #55 | strukturierter Schur-Defekt → gesättigte Leakage |
| PR #56 | Halbverschiebungs-Shell + relativer Resolventenvorläufer |
| PR #57 | geometrischer Mittelwert + exakter Resolvententransport |
| PR #58 | Good-Normal-Tail + Zwei-Hard-Channel-Reduktion |

Diese Tabelle ist **Provenienz**, kein mathematischer DAG. Downstream-Arbeit darf auf exakten Draft-Heads aufbauen, aber sie promotet die Parent-Heads nicht.

**Draft-source IDs** bleiben historische Quellbezeichnungen, keine Aussage zum heutigen GitHub-Draftstatus. Eine Stackintegration erzeugt keine Registry-Promotion; die Registry bleibt bei diesem Governance-Abgleich unverändert.

Jüngste XBAND-Audits der Kette: [Kommutatoren](audits/P11_R43_SCHUR_XBAND_COMM_2026-09-07.md), [Anker/Phase](audits/P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.md) und [symmetrische Quellen-Nachrechnung](audits/P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.md). Hier ausschließlich **lokale Diagnostik**, keine neue mathematische Front oder Promotion; ihr Integrationsstand folgt `ACTIVE_FRONT.yaml`, nicht historischen Draft-Kopfzeilen.

Der [Integrationsaudit vom 7. September 2026](audits/R43_STACK_INTEGRATION_2026-09-07.md) dokumentiert die abgeschlossenen Merges, begrenzten Korrekturen und exakten Review-Heads. Die Registry bleibt unverändert.

---

## 3. Exakter lokaler Resolvententransport

Draft-source ID:

```text
R43-COND-GEOMETRIC-MEAN-RESOLVENT-FACTORIZATION
```

Mit

\[
Q_{U,V}=B_U\#(\iota^*B_V\iota)
\]

gilt auf dem entsprechenden Draft-Head die exakte lokale Faktorisierung

\[
\boxed{
\iota^*B_V\iota-B_U
=-Q_{U,V}K_{U,V}^{\rm Schur}Q_{U,V}.
}
\]

Damit wird die frühere Firewall zwischen skalarem Schur-Defekt und tatsächlichem Inversmetrik-Inkrement über eine kanonisch **resolvententransportierte strukturierte Klasse** überbrückt.

Für den strukturierten Vektor `v_U=H_U^*E_{X,U}f` lautet der lokale Bound

\[
(\Delta s_{\rm cond}^{U,V}(f))_+
\le
\|(I+S^*S)^{-1/2}S^*M Q_{U,V}v_U\|^2.
\]

**Firewall:** globale cofinale Decay-Kontrolle von `||(L_{U,V})_-||` ist dadurch optional, nicht bewiesen. `Q\le I` erhält keinen Collar-Support und liefert kein Collar-Decay.

---

## 4. Good-Normal-/Hard-Channel-Reduktion

Draft-source IDs umfassen:

```text
R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL
R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS
R43-COND-NORMALIZED-GEOMETRIC-TRANSPORT-CONTRACTION
```

Der Normaloperator wird prime-by-prime und translation-sign-by-translation-sign zerlegt.

Alle guten Zweige besitzen im Draft-Scope ein horizontuniformes exponentielles Verschiebungsmoment; bei `beta=1/8` entsteht ein guter Tail von der Form

\[
O(e^{-r/8}).
\]

Die einzigen durch diese crude absolute Summierbarkeit nicht erledigten nichttrivialen diagonal-sum Kanäle sind

\[
\boxed{k=\ell=1},\qquad \boxed{k=\ell=2}.
\]

Für terminal-graph-normalisierte Quellen reduziert sich die resolvententransportierte Leakage schematisch auf

\[
\boxed{
\text{hard saturated}
+C_*\|\chi_{U,r}Q_{U,V}v_U\|
+C_*e^{-r/8}.
}
\]

---

## 5. Aktueller quantitative COND-Kern

Exakt offen bleiben:

```text
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY                ?[O]
R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY             ?[O]
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
```

Die praktische Forschung darf die beiden harten Kanäle getrennt untersuchen:

```text
ROADMAP-HARD11  — research-subquestion — k=l=1
ROADMAP-HARD22  — research-subquestion — k=l=2
```

Diese ROADMAP-Namen sind keine kanonischen Theorem-IDs und tragen keinen Registry-`math_status`.

### Quantoren-Firewall

Nicht still festlegen:

- Relation zwischen `U` und `V`;
- Uniformität in Zwischenhorizonten;
- cofinale Partition;
- pointwise-in-source versus uniforme Quellkontrolle;
- Wahl des Collar-Radius `r`;
- Reihenfolge der Grenzübergänge.

Unbekannte Quantoren bleiben `unresolved`.

---

## 6. Zwei verschiedene Wege Richtung Flag-Tightness

### 6.1 Strukturierter Direktweg

```text
R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND
        |
        | --used-by-->
        v
[R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL,
 R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS]
        |
        | --reduces current target to-->
        +---- R43-COND-TRANSPORTED-COLLAR-MASS-DECAY ?[O]
        |
        +---- R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY ?[O]
        |
        v
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
        |
        | --open-bridge-->
        v
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN
        |
        | --sufficient-route-->
        v
projected B-FLAGDYN / FD23-compatible control ?[O]
        |
        | --sufficient-route-->
        v
B-FLAGTIGHT ?[O]
```

### 6.2 Stärkerer Operator-/B-METINC-Weg

```text
B-METINC-WIDTH ?[O]
  uses:
    - B-METINC-COND ?[O]
    - B-METINC-GEO  ?[O]
    - B-METINC-NEW  ?[O]

B-METINC-WIDTH ?[O]
        |
        | --sufficient-route-->
        v
B-FLAGMOD ?[O]
```

**Wichtige Firewall:** Scheitert diese globale Operatorroute, ist B-FLAGMOD/Strong Terminal nicht widerlegt; dann ist zur direkt projizierten Normal-/Flaggröße zurückzukehren.

---

## 7. B-FLAGDYN / B-FLAGTIGHT

Auf dem festen Quellraum:

\[
Q_{m,U}=W_U^*P_mW_U,
\qquad
q_m(U)=\langle\varepsilon_R,Q_{m,U}\varepsilon_R\rangle
=\|P_mh_U\|^2.
\]

Der exakte Tightness-Gate lautet im gebuchten Scope

\[
\boxed{
\mathrm{B\!-\!FLAGTIGHT}
\Longleftrightarrow
\lim_{m\to\infty}\limsup_{U\to\infty}q_m(U)=0.
}
\]

B-FLAGDYN bezeichnet die quantitative Kontrolle der echten Terminalvariation von `q_m(U)`.

Ein stärkerer hinreichender Weg zerlegt die Änderung in B-FLAGMOD und B-FLAGPHASE.

---

## 8. Nach Tightness

Nach B-FLAGTIGHT bleibt B-SIGN/B-ORIENT.

Unter B-TIGHT gilt im exakt gebuchten Scope

\[
\boxed{
\text{Strong Terminal}
\Longleftrightarrow
\liminf_{T,U\to\infty}L_{R,S}^{T,U}>-1.
}
\]

Strong Terminal/C6 bleibt OPEN.

---

## 9. Object-X-Firewall

Strong Terminal ist **nicht** Objekt X.

Ein positiver B-Abschluss wäre zunächst ein X-Kandidatenbaustein. Es ist derzeit weder

\[
\text{Strong Terminal}\Rightarrow\text{Objekt X}
\]

noch die Notwendigkeit von Strong Terminal für jede mögliche Object-X-Realisierung gebucht.

Die aktuelle Object-X-Arbeitsdefinition steht ausschließlich in `OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`.

Eine echte Object-X-Realisierung verlangt insbesondere einen intrinsischen, nicht-zirkulären gemeinsamen Prime-/Archimedes-Mediator sowie die vollständige korrekt normalisierte Weil-Gram-Identität auf einer geeigneten Testklasse.

Offen sind daher getrennt:

```text
genuine X candidate      ?[O]
Object-X realization     ?[O]
RH                       ?[O]
```

Die **Definition** von Objekt X selbst ist nicht `?[O]`; sie ist kanonisch festgelegt.

---

## 10. Separater R37-Pfad

R37/G4c bleibt separat offen. Innerhalb von R37 ist der analytische Promotionsblocker die noch offene Passage vom reellen Segment zur holomorphen Annulusidentität und zur Laurent-Eindeutigkeit.

Die Abhängigkeit des R37-Pfads von einer späteren X-Kandidatenarchitektur ist derzeit **unresolved**. Deshalb gibt es **keine Kante** von R37/G4c zum X-Pfad.

---

## 11. Default-Arbeitsfolge

Für die hier unverändert dargestellten historischen Quellstände gilt vorbehaltlich ihres Reviews die Default-Reihenfolge:

1. **Hard Channel `k=l=1`** unter der echten Sättigung angreifen;
2. **Hard Channel `k=l=2`** unter der echten Sättigung angreifen;
3. transported collar mass `||chi_{U,r}Q_{U,V}v_U||` kontrollieren;
4. die **schwächste** direkte Summierbarkeits-/FD23-Kompositionsbedingung bestimmen;
5. erst bei Bedarf auf den stärkeren globalen B-METINC-WIDTH-Weg wechseln.

Parallel als Route-Optimierungsfrage:

```text
FD23-MINIMAL-CONDITION
```

Nicht automatisch priorisiert: finite-level Salvage, R37/G4c, finaler `K_X`, Object-X-Realisierung, RH.

---

## 12. Lesereihenfolge

1. `CURRENT-FRONT.md` — heutige aktive Frage.
2. `00-uebersicht/ACTIVE_FRONT.yaml` — exakte volatile Stackdaten.
3. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md` — Abhängigkeiten/Firewalls.
4. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md` — Status/Review-Provenienz.
5. kanonische mathematische Quelle des verwendeten Inputs.
6. aktueller PR/Audit.
7. historische Dateien nur bei klarer Provenienzfrage.

Der Verlust-/Migrationscheck gegenüber der vor-v2 Langfassung ist separat im Governance-Audit dieses Roadmap-PRs dokumentiert; historische Mathematik wird nicht durch Kürzung dieser Navigationsdatei gelöscht.

---

## 13. Merge-/Rollback-Regel

Ein mathematisch relevanter Merge ist operativ erst abgeschlossen nach:

```text
Merge --then--> main verification --then--> Registry --then--> ACTIVE_FRONT --then--> CURRENT_FRONT --then--> next work
```

Dabei wird der aktuelle `main`-Head **live** verifiziert. Ein versionierter Ledger speichert nicht die SHA seines eigenen aktuellen Commits. Für gestackte Drafts bleibt stattdessen der historische Stack-Root-Base-Pin exakt erhalten.

`Registry` bedeutet hier Statusprüfung, keine automatische Änderung oder Promotion durch einen GitHub-Merge.

Für gestackte Drafts gilt: fällt ein Parent-Head, werden alle davon abhängigen Claims re-auditiert. Ein gescheiterter hinreichender Weg ist kein gescheitertes Fernziel, solange keine Notwendigkeitskante bewiesen wurde.

---

## Kurzstatus

Die exakten Heads/States stehen ausschließlich in `ACTIVE_FRONT.yaml`.

```text
R43 integration / historical chain      see ACTIVE_FRONT.yaml
R43 COND collar decay                  ?[O]
R43 COND hard channels                 ?[O]
structured COND leakage decay          ?[O]
B-METINC-COND                          ?[O]
B-FLAGDYN / B-FLAGTIGHT               ?[O]
B-SIGN / B-ORIENT                      ?[O]
Strong Terminal / C6                   ?[O]
R37/G4c                                ?[O], separate
genuine X candidate                    ?[O]
Object-X realization                   ?[O]
RH                                     ?[O]
```

**Kein Freeze und keine globale Promotion durch Stackintegration.**
