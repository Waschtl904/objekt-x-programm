# Aktueller Stand — Objekt X / P11 Strong Terminal

> **Stand (Governance):** 7. September 2026; mathematische Darstellung unverändert.<br>
> **Operative Kurzfassung.** Für Details gelten
> [CURRENT-FRONT](../CURRENT-FRONT.md),
> [ACTIVE_FRONT](ACTIVE_FRONT.yaml),
> [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md) und die
> [kanonische Forschungsroadmap](FORSCHUNGS_ROADMAP_AKTUELL.md).
>
> Volatile Stack-Heads/States werden hier **nicht** dupliziert. Der aktuelle `main`-Head wird live aus GitHub gelesen und nicht selbstreferenziell als SHA in einer versionierten Repo-Datei gespeichert. Historische Fassungen bleiben über Git und `archiv/` erhalten.

---

## 1. Aktive Forschungsfront

Die aktive Hauptfront ist **B / Strong Terminal / C6**, derzeit **R43**.

Exakter Registry-Governance-String für R38–R42:

```text
FROZEN — independently verified AI-GREEN
```

Die Registry-Firewall bleibt maßgeblich: dieser projektinterne String ist nicht automatisch ein formaler `independent GREEN (cross-model/certificate/human)`-Subtyp. R43 ist OPEN.

Für jedes feste

\[
0<R<S
\]

ist der verbleibende Strong-Terminal-Gate auf die eine Normalbahn reduziert, äquivalent auf

\[
\boxed{
\operatorname{Re}
\langle
\varepsilon_R,K_{R,S}^{T,U}\varepsilon_R
\rangle
\to1
\quad?
}
\]

---

## 2. R43-Stack und Integrationsstand

Exakte Branches, Heads, Parent-Heads und GitHub-States stehen ausschließlich in `ACTIVE_FRONT.yaml`.

Die ursprünglichen Review-Bases, Heads und Parent-Heads aller 20 R43-PRs bleiben als historische Abhängigkeitskette erhalten; der Stack-Root bleibt auf seinem historischen Base-Commit gepinnt. GitHub-Ziel (`github_base`), tatsächlich gemergter Head (`merged_head_sha`), belegter Mergestatus und offene Anzahl werden davon getrennt in `ACTIVE_FRONT.yaml` geführt.

Die vier folgenden Container sind der historische Anfang der Kette, nicht deren vollständiger Integrationsstand:

| Container | Rolle |
|---|---|
| PR #55 | strukturierte Schur-Leakage |
| PR #56 | Halbverschiebung + relativer Resolventenvorläufer |
| PR #57 | geometrischer Mittelwert + Resolvententransport |
| PR #58 | Good-Normal-Tail + Hard-Channel-Reduktion |

**Draft-source IDs** bleiben historische Quellbezeichnungen, keine aktuellen GitHub-Statusangaben. Weder Stackbeziehung noch Merge erzeugen externes GREEN oder Registry-Promotion; die Registry bleibt bei diesem Governance-Abgleich unverändert.

Die jüngsten XBAND-Audits sind in [CURRENT-FRONT, Abschnitt 2](../CURRENT-FRONT.md#2-r43-stack-und-integrationsstand) ausschließlich als lokale Diagnostik verlinkt; keine neue mathematische Front.

---

## 3. Aktueller COND-Kern

Der geometrische-Mittelwert-Draft liefert lokal

\[
Q_{U,V}=B_U\#(\iota^*B_V\iota)
\]

und

\[
\iota^*B_V\iota-B_U=-Q_{U,V}K_{U,V}^{\rm Schur}Q_{U,V}.
\]

Die Good-Normal-Reduktion führt die strukturierte Leakage schematisch auf

\[
\boxed{
\text{hard saturated}
+C_*\|\chi_{U,r}Q_{U,V}v_U\|
+C_*e^{-r/8}
}
\]

zurück, mit nur zwei durch die crude absolute Summierbarkeit nicht erledigten diagonal-sum Kanälen

\[
\boxed{k=\ell=1},\qquad\boxed{k=\ell=2}.
\]

Offen:

```text
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY                ?[O]
R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY             ?[O]
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
```

---

## 4. Zwei Wege Richtung B-FLAGTIGHT

### Strukturierter Direktweg

```text
R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND
        |
        | --used-by-->
        v
[R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL,
 R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS]
        |
        | --reduces current target to-->
        +---- collar decay ?[O]
        +---- hard-channel decay ?[O]
        |
        v
structured leakage decay ?[O]
        |
        | --open-bridge-->
        v
projected B-FLAGDYN / FD23-compatible control ?[O]
        |
        | --sufficient-route-->
        v
B-FLAGTIGHT ?[O]
```

### Stärkerer Operatorweg

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

**Firewall:** Scheitert die globale Spectral-Width-/Operatorroute, ist die direkt projizierte Normal-/Flagroute nicht widerlegt.

---

## 5. Tightness / Sign / Strong Terminal

Mit

\[
Q_{m,U}=W_U^*P_mW_U,
\qquad
q_m(U)=\langle\varepsilon_R,Q_{m,U}\varepsilon_R\rangle
\]

gilt im gebuchten Scope

\[
\mathrm{B\!-\!FLAGTIGHT}
\Longleftrightarrow
\lim_m\limsup_U q_m(U)=0.
\]

Danach bleibt B-SIGN/B-ORIENT. Unter B-TIGHT gilt der scharfe Resttest

\[
\text{Strong Terminal}
\Longleftrightarrow
\liminf_{T,U\to\infty}L_{R,S}^{T,U}>-1.
\]

Strong Terminal/C6 bleibt OPEN.

---

## 6. Andere Fronten

### A / finite-level

Die universelle positive SW1-Cross-Gram-Route ist in ihrem gebuchten Scope negativ entschieden; Salvage bleibt Nebenfront.

### R37/G4c

Separat offen. Die Beziehung zu einer späteren X-Kandidatenarchitektur ist derzeit `unresolved`; es gibt keine Kante von R37/G4c zum X-Pfad. R38–R43 promoten R37 nicht rückwirkend.

### Objekt X

Die aktuelle Definition steht in `OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md` und ist **nicht** offen.

Offen sind getrennt:

```text
genuine X candidate      ?[O]
Object-X realization     ?[O]
RH                       ?[O]
```

Strong Terminal wäre höchstens ein X-Kandidatenbaustein; es existiert kein Satz `Strong Terminal => Objekt X`.

---

## 7. Nächste Default-Arbeitsfolge

1. Hard Channel `k=l=1` unter echter Sättigung angreifen.
2. Hard Channel `k=l=2` unter echter Sättigung angreifen.
3. Transported Collar `||chi_{U,r}Q_{U,V}v_U||` kontrollieren.
4. Die schwächste hinreichende direkte FD23-/B-FLAGDYN-Kompositionsbedingung identifizieren.
5. Nur bei Bedarf den stärkeren globalen B-METINC-WIDTH-Weg verfolgen.

Parallel: `FD23-MINIMAL-CONDITION` als Route-Optimierungsfrage.

---

## 8. Governance

- aktueller `main`-Head: live aus GitHub; nicht selbstreferenziell im Repo gespeichert;
- volatile Stackdaten und historischer Stack-Root-Base-Pin: `ACTIVE_FRONT.yaml`;
- R43: OPEN, kein Freeze;
- R43-Integrationsstand und historische Abhängigkeitskette: gemäß `ACTIVE_FRONT.yaml`;
- Strong Terminal/C6: `?[O]`;
- R37/G4c: offen/separat;
- genuine X candidate: `?[O]`;
- Object-X realization: `?[O]`;
- RH: `?[O]`;
- kein Object-X- oder RH-Abschluss.
