# Abhängigkeitsgraph (DAG)

> **Historischer SYN-DAG, Stand 8. August 2026.** Der untenstehende P01→P04→NEU-260-Pfad
> ist nicht mehr die operative Forschungspriorität. Aktuelle operative Kette:
>
> \[
> \text{P12-RT / SW1-KNF--A10}
> \to \text{M1-RAW/M1-FULL}
> \to \text{C1B2A-TRANSFER}
> \to \boxed{\ker\Gamma_I=\{0\}\ ?[O]}.
> \]
>
> Maßgeblich sind [`../CURRENT-FRONT.md`](../CURRENT-FRONT.md) und
> [`ACTIVE_THEOREM_REGISTRY.md`](ACTIVE_THEOREM_REGISTRY.md). Der historische DAG
> bleibt für Provenienz der damaligen SYN-Architektur erhalten.
**Stand:** 2026-08-08 (Audit-Update)

```
BC/Frobenius/Nakayama
        |
        v
    [P01] BC Prime Power Weights            [Entwurf, P01-Audit ausstehend]
    Lambda(p^k)/sqrt(p^k) aus lokalem BC
        |
        v
    [P02] Adelic Weil Amplitude Port        [checkmark SYN-Audit 2026-08-08]
    F in S_adel^amp
      --(R_PW)--> a in A_PW = Cc^inf(R;C)
      --((a,b)->g_{a,b})--> G_ev^C
      --(Weil)--> B_W
    [Zwei getrennte Stufen; Typfehler Entwurf korrigiert]
        |
        v
    [P03] Haar-L2 Firewall                  [checkmark SYN-Audit 2026-08-08]
    B_W semibeschraenkt auf Cc^inf rel. L2(du) <=> RH
    B_W nicht abschliessbar (mu_W not<< du, Kriterium q_mu closable <=> mu<<dx)
    KLMN x[M]  (= Kato-Lions-Milgram-Nelson)
    H_W cong ell^2(Gamma, m_gamma) unter RH
        |
        v
    [P04] Finite Weil Geometry              [checkmark SYN-Audit 2026-08-08, in Arbeit]
    Q_W^a, A_a, H(T_a), D-bar_{a,theta}    [Suzuki 2026, RH-frei]
    lambda_w(a) = lambda_a - 1             [bequeme Konvention, c=1; checkmark]
    N_{pm} = span{v_pm}, T_a v_pm = e^{pm x}  [Typfehler Entwurf korrigiert]
    PA_a = A_aP                             [Suzuki, checkmark]
    Pv+ = v-                               [checkmark]
    U(1) --Paritaet--> {+P,-P} = Z2       [HAUPT-RESULTAT checkmark]
        |
        v
    [NEU-260b.1] Z2-Selektion              [?[O] hoechste Prioritaet]
    epsilon(a) in {+1,-1}: Stetigkeitsarg? BC/KMS-Zeitpfeil? Frobenius?
        |
        v
    [NEU-260c] phi(a,z)                    [?[O]]
        |
        v
    [NEU-260d] J_{a,b}                     [?[O]]
        |
        v (Objekt-X-Konjektur, unter RH)
    K_X = lim-> H(T_a) --> H_W cong ell^2(Gamma, m_gamma)
```

## SYN-Audit-Status

| Manuskript | Audit |
|---|---|
| P01 | Entwurf, ausstehend |
| P02 | checkmark 2026-08-08 |
| P03 | checkmark 2026-08-08 |
| P04 | checkmark 2026-08-08 |

## Veraltete Eintraege (gestrichen)

- ~~"Q_W^a-Spiegelungssymmetrie => theta_can=0" als hoechste Prioritaet~~
  (ersetzt durch Z2-Selektion)
- ~~"N_{pm} = span{e^{pm x}}"~~ (Typfehler, korrigiert)
- ~~"Antiunitaere Abbildung f->bar{f(-x)}"~~ (P linear, nicht antiunitaer)

---

*Zuletzt aktualisiert: 2026-08-08 (SYN-Audit P02-P04)*
