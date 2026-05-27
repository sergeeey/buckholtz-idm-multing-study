# Equation Inventory

## Purpose

Catalog all equations and relations mentioned in Buckholtz IDM/MULTING work, with source status, symbols, and dimensional analysis status.

---

## Equations

| ID | Equation / relation | Symbols | Units check | Source | Status | Notes |
|---|---|---|---|---|---|---|
| `eq_15` | `(4/3) * (m_tau^2 / m_e^2)^6 ≈ k_e * e^2 / (G * m_e^2)` | m_tau, m_e, k_e, e, G | requires_clarification | Communications (to be verified) | calculation | Numerically reproduced to ~1%. Physical mechanism for exponent 6 and prefactor 4/3 unclear. |
| `idm_six_isomers` | `N_isomers = 6 (5 dark + 1 ordinary matter)` | N_isomers | not_checked | Requires verification | hypothesis | How are isomers defined? What distinguishes them? Observational implications? |
| `multing_monopole` | `H(z) monopole component (exact form TBD)` | H, z | not_checked | Requires verification | requires_source_verification | MULTING includes monopole modification to H(z). Full functional form requires clarification. |
| `multing_dipole` | `H(z) dipole repulsion ~ beta_d (exact form TBD)` | H, z, beta_d | not_checked | Requires verification | requires_source_verification | Dipole repulsion term scaled by beta_d. Full functional form, dimensional analysis, and beta_d definition require clarification. **PPN/Solar System constraint implications require checking.** |
| `multing_quadrupole` | `H(z) quadrupole attraction ~ beta_q (exact form TBD)` | H, z, beta_q | not_checked | Requires verification | requires_source_verification | Quadrupole attraction term scaled by beta_q. Full functional form, dimensional analysis, and beta_q definition require clarification. **PPN/Solar System constraint implications require checking.** |
| `beta_d_scale` | `r_dA = beta_d * r_A (possible relation, TBD)` | r_dA, beta_d, r_A | not_checked | Requires verification | requires_source_verification | Possible definition: beta_d relates dipole scale r_dA to characteristic scale r_A. What is r_A? What is r_dA physically? Dimensional consistency? |
| `beta_q_scale` | `L_q^2 = beta_q * L_ref^2 (possible relation, TBD)` | L_q, beta_q, L_ref | not_checked | Requires verification | requires_source_verification | Possible definition: beta_q relates quadrupole scale L_q to reference length L_ref. What is L_ref? What is L_q physically? Dimensional consistency? |

---

## PPN / Solar System Quick-Check

**Critical for MULTING dipole and quadrupole terms.**

| MULTING term | Possible PPN relevance | GR limit | Current constraint | MULTING implication | Status |
|---|---|---|---|---|---|
| Dipole repulsion | Preferred-frame / dipole-like effects | 0 | Literature check required | Must map carefully to PPN framework | **must check** |
| Quadrupole extra attraction | Extra metric potential terms | 0 or constrained | Literature check required | Must preserve GR Solar System tests | **must check** |
| Light deflection (gamma) | Photon path bending | gamma = 1 in GR | gamma = 1.00001 ± 0.00001 (Cassini) | MULTING must not violate this | **must check** |
| Perihelion precession | Orbital dynamics | Standard GR prediction | Mercury: match to 0.1% | MULTING dipole/quad must preserve | **must check** |
| Shapiro delay | Time delay of light | Standard GR prediction | Cassini: match to 0.001% | MULTING must preserve | **must check** |

**Action required:** Map MULTING dipole and quadrupole terms to PPN formalism and verify consistency with Solar System constraints.

**Numerical constraints not invented** — literature check required before claiming specific bounds.

---

## Dimensional Analysis Status

| Equation | Dimensional status | Blocker |
|---|---|---|
| Eq.15 | requires_clarification | Mass ratio (dimensionless) vs force ratio requires careful unit tracking |
| IDM six isomers | not_checked | N_isomers is a count (dimensionless) |
| MULTING monopole | not_checked | Functional form unknown |
| MULTING dipole | not_checked | beta_d units unclear (dimensionless vs length?) |
| MULTING quadrupole | not_checked | beta_q units unclear (dimensionless vs length²?) |
| beta_d scale | not_checked | Requires r_A and r_dA definitions |
| beta_q scale | not_checked | Requires L_ref and L_q definitions |

---

## Equations with Verified Sources

**Count:** 1 out of 7

Only `eq_15` has a partial source reference (Buckholtz communications, pending formal publication verification).

All other equations are marked `requires_source_verification`.

---

## Equations Requiring Clarification

**Count:** 6 out of 7

**Blockers:**
1. **MULTING functional forms** — exact H(z, beta_d, beta_q) equations
2. **Beta definitions** — units, normalization, physical interpretation
3. **PPN mapping** — how dipole/quadrupole terms map to PPN formalism
4. **Dimensional consistency** — all length scales and dimensionless ratios must be clarified

---

## Next Steps

1. Request explicit functional forms for MULTING terms from Dr. Buckholtz
2. Request beta_d and beta_q definitions with units
3. Perform literature review of PPN constraints on dipole/quadrupole modified gravity
4. Perform dimensional analysis once functional forms are available
5. Update this inventory as sources become available

---

## Status Summary

| Category | Count |
|---|---:|
| Total equations cataloged | 7 |
| With verified sources | 1 |
| Requiring source verification | 6 |
| Numerically reproduced | 1 (Eq.15) |
| Dimensional analysis complete | 0 |
| Ready for implementation | 0 |

**Blocker:** Cannot implement H(z) solver or beta-based predictions until functional forms and definitions are clarified.
