# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 14. September 2026.**

Forschungsprogramm **Objekt X** im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor. ChatGPT übernimmt Repo-Arbeiten; externe Modelle sind Reviewer. Keine Promotion allein durch Merge, CI oder Numerik.

## Zuerst lesen

1. `CURRENT-FRONT.md`
2. `audits/P11_A1_FINITE_GATE_ARCHITECTURE_2026-09-14.md`
3. `audits/P11_A1_OSIPOV1102_REDUCTION_2026-09-14.md`
4. `audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md`
5. `audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md`
6. Registry/Arbeitsdefinition nur als unveränderte Governancequellen.

## Gesicherter Stand

```text
COMMON-JUMP / Q0                         ✓[M]
rank-2 completion / Morse / parity      ✓[M]
canonical lambda=1                      ✓[M]
exact a=1 Fourier multiplier            ✓[M]
Omega1551 high-frequency floor          ✓[K/M]
Osipov N=1102 Schur reduction           ✓[K/M]
canonical mathematical reduction <=1104 ✓[K/M]
```

Die kleinste kanonische Restobligation bleibt

```math
(L_1)_{RR}\succeq3\times10^{-39}I
```

auf höchstens `552 even + 552 odd` PSWF/moment-augmentierten Dimensionen.

## Durchlauf B — Architekturentscheidung `✓[M]`

Für den **ersten ausführbaren Vollzertifikatsversuch** wird nicht die kleinere PSWF-Basis konstruiert, sondern der bereits vorbereitete orthonormale Legendre-Backend verwendet.

Fixiert:

```text
M=2150
1075 even + 1075 odd
Gram I exactly
finite target=1e-35
panel width<=0.4
Gauss-Legendre q=40
analytic strip |Im xi|<=0.4
quadrature operator error <4e-38
```

Die Legendre-Ausführung ersetzt die kleinere PSWF-Reduktion nicht; sie ist die derzeit robustere Zertifikatsbasis, weil Basis, Gram, Parität, Tail/Cross und Quadraturbudget bereits rigoros geschlossen sind.

## Default-Auftrag — C-even ONLY

Im nächsten Durchlauf **nur den geraden Paritätsblock** bauen und zertifizieren:

```math
\boxed{A_e\succeq10^{-35}I_{1075}}.
```

### Fixiertes Verfahren

1. common-node Arb matrix assembly;
2. spherical-Bessel vector evaluation with deterministic fail-closed recurrence;
3. moment block `2aa^T` in Arb;
4. certified #118 quadrature radius directly in every matrix entry;
5. interval symmetry checks;
6. untrusted midpoint eigenbasis/preconditioner as proposal only;
7. freeze proposal to dyadic Arb points;
8. form in Arb
   ```math
   V^T(A_e-10^{-35}I)V;
   ```
9. verified interval Cholesky/LDL;
10. accept only if every decisive pivot lower endpoint is strictly positive.

### Fixed precision ladder

```text
512
768
1024
1536
2048
3072 bits
```

Only precision may increase. Do **not** retune `M`, target, quadrature order, panel width or basis after seeing results.

If C-even is green, stop and checkpoint. Run C-odd only in a separate later pass.

### Firewalls

- A pivot containing `0` is undecided.
- Float eigenvectors/factors are untrusted proposals only.
- B defined architecture; it did not prove finite positivity.
- No `a=1` promotion after even alone.
- Fixed-window `a=1`, all-a NP-GAP, Object X and RH remain open.
- Registry/Arbeitsdefinition unchanged.
