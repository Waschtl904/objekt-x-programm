# CURRENT FRONT — Objekt X / P11 Strong Terminal

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 6. September 2026  
> **Volatile PR-/SHA-Single-Source:** [`00-uebersicht/ACTIVE_FRONT.yaml`](00-uebersicht/ACTIVE_FRONT.yaml)  
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

R38–R42 bleiben gemäß ihrer exakten Reviewer-/Governance-Provenienz frozen; R43 bleibt OPEN.

R37/G4c bleibt **separat offen** und wird durch R38–R43 nicht rückwirkend geschlossen.

---

## 2. Aktiver ungemergter R43-Stack

Die exakten Heads und GitHub-States stehen ausschließlich in `ACTIVE_FRONT.yaml`.

Schematisch:

```text
main (post-PR54)
   |
   +-- PR55 structured Schur defect -> saturated leakage       [Draft]
          |
          +-- PR56 half-shift shell + relative resolvent       [Draft]
                 |
                 +-- PR57 geometric-mean resolvent transport   [Draft]
                        |
                        +-- PR58 good-normal tail + hard chans  [Draft]
```

Alle vier PRs sind bewusst ungemergt. Downstream-Arbeit darf auf exakten Draft-Heads aufbauen, aber sie promotet die Parent-Heads nicht.

---

## 3. Was PR #57 strukturell geändert hat

Mit

\[
Q_{U,V}=B_U\#(\iota^*B_V\iota)
\]

gilt auf dem PR57-Head die exakte lokale Faktorisierung

\[
\boxed{
\iota^*B_V\iota-B_U
=-Q_{U,V}K_{U,V}^{\rm Schur}Q_{U,V}.
}
\]

Damit wird die frühere Firewall zwischen skalarem Schur-Defekt und tatsächlichem Inversmetrik-Inkrement über eine kanonisch **resolvententransportierte strukturierte Klasse** überbrückt.

Für den strukturierten Vektor `v_U=H_U^*E_{X,U}f` lautet der einseitige lokale Bound

\[
(\Delta s_{\rm cond}^{U,V}(f))_+
\le
\|(I+S^*S)^{-1/2}S^*M Q_{U,V}v_U\|^2.
\]

**Firewall:** globale cofinale Decay-Kontrolle von `||(L_{U,V})_-||` ist dadurch optional, nicht bewiesen. `Q\le I` erhält keinen Collar-Support und liefert kein Collar-Decay.

---

## 4. Was PR #58 strukturell geändert hat

Der Normaloperator wird prime-by-prime und translation-sign-by-translation-sign zerlegt.

Alle guten Zweige besitzen im PR58-Scope ein horizontuniformes exponentielles Verschiebungsmoment; bei `beta=1/8` entsteht ein guter Tail von der Form

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
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY              ?[O]
R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY           ?[O]
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
```

Die praktische Forschung darf die beiden harten Kanäle getrennt untersuchen:

```text
ROADMAP-HARD11  -> k=l=1
ROADMAP-HARD22  -> k=l=2
```

Diese ROADMAP-Namen sind noch keine kanonischen Theorem-IDs.

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
PR57 transported structured leakage
        |
        v
PR58 collar + good tail + hard-channel reduction
        |
        +--> transported collar decay ?[O]
        +--> hard (1,1)+(2,2) saturated decay ?[O]
        |
        v
structured leakage decay ?[O]
        |
        | OPEN direct composition bridge
        v
projected B-FLAGDYN / FD23-compatible control ?[O]
        |
        v
B-FLAGTIGHT ?[O]
```

Der offene Kompositionsknoten wird in der Roadmap als

```text
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN
```

geführt, bis Aussage und Quantoren theorematisiert sind.

### 6.2 Stärkerer Operator-/B-METINC-Weg

Separat offen:

```text
B-METINC-COND
B-METINC-GEO
B-METINC-NEW
B-METINC-WIDTH
```

Die Spectral-Width-/Sylvester-Kette ist nur eine **hinreichende Operatorroute** zu B-FLAGMOD.

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

RH bleibt OPEN.

---

## 10. Separater R37-Pfad

R37/G4c bleibt separat offen:

```text
real segment
   -> holomorphic annulus identity
   -> Laurent uniqueness
```

Die Abhängigkeit des R37-Pfads von einer späteren X-Kandidatenarchitektur ist derzeit **unresolved**; es wird keine prerequisite-Kante gesetzt.

---

## 11. Default-Arbeitsfolge

Solange der PR55–58-Stack nicht durch Review fällt, ist die Default-Reihenfolge:

1. **Hard Channel `k=l=1`** unter der echten Sättigung angreifen;
2. **Hard Channel `k=l=2`** unter der echten Sättigung angreifen;
3. transported collar mass `||chi_{U,r}Q_{U,V}v_U||` kontrollieren;
4. die **schwächste** direkte Summierbarkeits-/FD23-Kompositionsbedingung bestimmen;
5. erst bei Bedarf auf den stärkeren globalen B-METINC-WIDTH-Weg wechseln.

Parallel als Route-Optimierungsfrage:

```text
FD23-MINIMAL-CONDITION
```

Nicht automatisch priorisiert: finite-level Salvage, R37/G4c, finaler `K_X`, Object X, RH.

---

## 12. Lesereihenfolge

1. `CURRENT-FRONT.md` — heutige aktive Frage.
2. `00-uebersicht/ACTIVE_FRONT.yaml` — exakte volatile Stackdaten.
3. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md` — Abhängigkeiten/Firewalls.
4. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md` — Status/Review-Provenienz.
5. kanonische mathematische Quelle des verwendeten Inputs.
6. aktueller PR/Audit.
7. historische Dateien nur bei klarer Provenienzfrage.

---

## 13. Merge-/Rollback-Regel

Ein mathematisch relevanter Merge ist operativ erst abgeschlossen nach:

```text
Merge -> main verification -> Registry -> ACTIVE_FRONT -> CURRENT_FRONT -> next work
```

Für gestackte Drafts gilt: fällt ein Parent-Head, werden alle davon abhängigen Claims re-auditiert. Ein gescheiterter hinreichender Weg ist kein gescheitertes Fernziel, solange keine Notwendigkeitskante bewiesen wurde.

---

## Kurzstatus

```text
main                                434cd6bd...  (post-PR54)
PR55                                Draft / unmerged
PR56                                Draft / unmerged
PR57                                Draft / unmerged
PR58                                Draft / unmerged
R43 COND collar decay               ?[O]
R43 COND hard channels              ?[O]
structured COND leakage decay       ?[O]
B-METINC-COND                       ?[O]
B-FLAGDYN / B-FLAGTIGHT            ?[O]
B-SIGN / B-ORIENT                   ?[O]
Strong Terminal / C6                ?[O]
R37/G4c                             ?[O], separate
Object X                            ?[O]
RH                                  ?[O]
```

**Kein Freeze und keine globale Promotion aus dem PR55–58-Stack.**
