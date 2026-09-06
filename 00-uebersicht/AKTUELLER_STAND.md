# Aktueller Stand — Objekt X / P11 Strong Terminal

> **Stand:** 6. September 2026  
> **Operative Kurzfassung.** Für Details gelten
> [CURRENT-FRONT](../CURRENT-FRONT.md),
> [ACTIVE_FRONT](ACTIVE_FRONT.yaml),
> [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md) und die
> [kanonische Forschungsroadmap](FORSCHUNGS_ROADMAP_AKTUELL.md).
>
> Historische Fassungen bleiben über Git und `archiv/` erhalten.

---

## 1. Aktive Forschungsfront

Die aktive Hauptfront ist **B / Strong Terminal / C6**, derzeit **R43**.

R38–R42 bleiben gemäß ihrer exakten Provenienz frozen/reviewed; R43 ist OPEN.

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

## 2. Aktiver ungemergter Stack

Die exakten Heads/States stehen in `ACTIVE_FRONT.yaml`.

```text
main@434cd6bd...
   |
   +-- PR55 structured Schur leakage              [Draft]
          |
          +-- PR56 relative resolvent             [Draft]
                 |
                 +-- PR57 geometric-mean transport [Draft]
                        |
                        +-- PR58 good tail + hard channels [Draft]
```

Keiner dieser Drafts ist durch die Stackbeziehung automatisch extern GREEN oder gemergt.

---

## 3. Aktueller COND-Kern

PR #57 liefert auf seinem exakten Draft-Head den kanonischen geometrischen-Mittelwert-Transport

\[
Q_{U,V}=B_U\#(\iota^*B_V\iota)
\]

und die exakte lokale Kongruenz

\[
\iota^*B_V\iota-B_U=-Q_{U,V}K_{U,V}^{\rm Schur}Q_{U,V}.
\]

PR #58 reduziert die resultierende strukturierte Leakage auf:

\[
\boxed{
\text{hard saturated}
+C_*\|\chi_{U,r}Q_{U,V}v_U\|
+C_*e^{-r/8}
}
\]

mit nur zwei durch die crude absolute Summierbarkeit nicht erledigten diagonal-sum Kanälen

\[
\boxed{k=\ell=1},\qquad\boxed{k=\ell=2}.
\]

Offen:

```text
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY              ?[O]
R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY           ?[O]
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
```

---

## 4. Zwei Wege Richtung B-FLAGTIGHT

### Strukturierter Direktweg

```text
collar + hard channels
        |
        v
structured leakage decay ?[O]
        |
        | offene quantitative Kompositionsbrücke
        v
projected B-FLAGDYN / FD23-compatible control ?[O]
        |
        v
B-FLAGTIGHT ?[O]
```

### Stärkerer Operatorweg

```text
B-METINC-COND / GEO / NEW ?[O]
        |
        v
B-METINC-WIDTH ?[O]
        |
        | hinreichend
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

Separat offen. Die Abhängigkeit von einer späteren X-Kandidatenarchitektur ist derzeit unresolved; R38–R43 promoten R37 nicht rückwirkend.

### Objekt X

Die aktuelle Definition steht in `OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`. Strong Terminal wäre höchstens ein X-Kandidatenbaustein; es existiert kein Satz `Strong Terminal => Objekt X`.

### RH

OPEN. Keine lokale PR55–58-Buchung erzeugt eine RH-Aussage.

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

- R43: OPEN, kein Freeze.
- PR55–58: Draft/unmerged gemäß `ACTIVE_FRONT.yaml`.
- Strong Terminal/C6: `?[O]`.
- R37/G4c: offen/separat.
- Kein Object-X- oder RH-Abschluss.
