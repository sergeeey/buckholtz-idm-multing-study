# Bridge Candidate Mathematical Stress Test

**Date:** 2026-05-29  
**Status:** INTERNAL_RECONSTRUCTION_AUDIT  
**Context:** No source-confirmed H_MULT(z) formula exists  
**Goal:** Determine which candidate F_oP → H_MULT bridge is mathematically defensible

---

## Executive Summary

**Key Findings:**

1. **Candidate B (Discrete Lattice ODE)** is the strongest internal computational reconstruction candidate
   - Dimensionally consistent: [F/(μ×D)] = [1/time²] = [ä/a]
   - Physically motivated: pairwise force → acceleration → Hubble parameter
   - Status: COMPUTATIONAL_RECONSTRUCTION_CANDIDATE (NOT source-confirmed)

2. **Phi(z) Heuristic** useful for Table A1 reproduction but NOT a physical bridge
   - Dimensionally under-specified: force ratios → H² without explicit length scale
   - Status: TABLE_REPRODUCTION_HEURISTIC_ONLY

3. **Candidate G (Potential/Hamiltonian)** requires careful sign/power derivation
   - a⁻⁵ term NOT verified until potential integration checked
   - Status: NEEDS_VERIFICATION

4. **Candidate B+G Hybrid** viable if D₀ dependence can be absorbed
   - Status: CONDITIONAL

5. **Candidate C (Virial Pressure)** more physical, less economical
   - Status: BACKUP

**MCMC Status:** ❌ **BLOCKED** — all candidates remain NOT_SOURCE_CONFIRMED

**Prediction Status:** ❌ **BLOCKED** — missing inputs (m_A(z), k_A(z), r_A(z), D_AB(z), N_eff)

**Row 1 Status:** ⚠️ **SOURCE_TABLE_OUTLIER** — exclude from diagnostics until author clarifies

---

## Part 1: Candidate B — Discrete Lattice ODE

### Formula

```
ä/a = N_eff × F_oP(D_AB, z) / (μ × D_AB)
```

Where:
- F_oP = F_m - F_d + F_q (MULTING pairwise force)
- μ = reduced mass (m_A × m_P) / (m_A + m_P)
- D_AB = inter-cluster distance
- N_eff = effective neighbor count / averaging factor

### Status

- ✅ **BEST_INTERNAL_BRIDGE_CANDIDATE**
- ⚠️ **NOT_SOURCE_CONFIRMED** — this may become our model, not Buckholtz's
- ❌ **MCMC_BLOCKED** — missing cluster variable tables
- ❌ **PREDICTION_BLOCKED** — no forward model without inputs

### 1.1 Unit Check

| Term | Units | Verification |
|------|-------|--------------|
| F_oP | [M L T⁻²] | Force ✅ |
| μ | [M] | Mass ✅ |
| D_AB | [L] | Length ✅ |
| F_oP / μ | [L T⁻²] | Acceleration ✅ |
| (F_oP / μ) / D_AB | [T⁻²] | 1/time² ✅ |
| ä/a | [T⁻²] | 1/time² ✅ |

**Result:** ✅ **DIMENSIONALLY CONSISTENT**

### 1.2 Sign Convention Check

| Component | Physical Interpretation | Expected Sign | Effect on ä/a |
|-----------|------------------------|---------------|---------------|
| F_m (monopole) | Attractive gravity | Negative | Deceleration (-) |
| -F_d (dipole) | Repulsive (if β_d > 0) | Positive | Acceleration (+) |
| F_q (quadrupole) | Attractive (if β_q > 0) | Negative | Deceleration (-) |

**Net effect:** F_oP = F_m - F_d + F_q

- If F_d dominates → ä > 0 (accelerated expansion)
- If F_m + F_q dominate → ä < 0 (decelerated expansion)

**Result:** ✅ **SIGN CONVENTION PLAUSIBLE** (consistent with late-time acceleration if F_d grows)

### 1.3 Missing Inputs

**Critical blockers:**

| Input | Units | Source | Status |
|-------|-------|--------|--------|
| m_A(z) | [M] | Table A1 or manuscript | ❌ MISSING |
| m_P(z) | [M] | Table A1 or manuscript | ❌ MISSING |
| k_A(z) | [M L T⁻²] | Table A1 or manuscript | ❌ MISSING |
| k_P(z) | [M L T⁻²] | Table A1 or manuscript | ❌ MISSING |
| r_A(z) | [L] | Table A1 or manuscript | ❌ MISSING |
| r_P(z) | [L] | Table A1 or manuscript | ❌ MISSING |
| D_AB(z) | [L] | Derived or specified | ❌ MISSING |
| β_d | dimensionless | Table A1 caption: 4.5 | ✅ AVAILABLE |
| β_q | dimensionless | Table A1 caption: 18.0 | ✅ AVAILABLE |
| N_eff | dimensionless | Averaging / geometry | ❌ MISSING |
| H₀ | [T⁻¹] | Initial condition | ✅ AVAILABLE (73 km/s/Mpc) |

**Cannot proceed to MCMC without at least:**
- m_A(z), r_A(z), k_A(z) for 12 redshift bins
- D_AB(z) definition (cosmological or peculiar?)
- N_eff value or derivation

### 1.4 Assumptions

| Assumption | Justification | Risk |
|------------|---------------|------|
| D_AB(t) = a(t) D₀ | Comoving inter-cluster distance | **HIGH** — peculiar velocities ignored |
| Nearest-neighbor lattice | Simplification | **MEDIUM** — real distribution not cubic |
| Isotropic averaging | FLRW symmetry | **HIGH** — forces may cancel under averaging |
| N_eff = constant | Geometry fixed | **MEDIUM** — may vary with z |
| μ ≈ m_A (if m_P << m_A) | Single-cluster approximation | **LOW** — depends on mass ratio |

### 1.5 Failure Modes

1. **Lattice anisotropy:** Real clusters not on cubic lattice → N_eff ambiguous
2. **Force cancellation:** Isotropic averaging may → F_net = 0
3. **Arbitrary N_eff:** Can fit any H(z) by tuning N_eff(z)
4. **Cluster ≠ background:** Cluster-scale force ≠ background expansion driver
5. **Peculiar velocities:** D_AB may not follow a(t) exactly
6. **Parameter degeneracy:** Many (m, k, r, D) combinations → same H(z)

### 1.6 Verdict

**Status:** **VIABLE** as internal reconstruction **IF**:
- Author confirms this is the intended averaging route
- Cluster variables provided
- N_eff justified or fitted

**Risk:** **MEDIUM-HIGH** — may become our model, not Buckholtz's

---

## Part 2: Candidate G — Potential/Hamiltonian Bridge

### Formula

Starting from pairwise force:

```
F_oP = F_m - F_d + F_q
```

Derive potential V(r) via:

```
F(r) = -dV/dr
```

### 2.1 Monopole Term

**Force:** F_m = -G m_A m_P / r²

**Potential:**
```
V_m(r) = -∫ F_m dr = -∫ (-G m_A m_P / r²) dr = -G m_A m_P / r
```

**Scaling with a(t):** If r = a(t) r₀, then V_m ∝ 1/a

**Energy density:** ρ_m ∝ V_m / a³ → ρ_m ∝ a⁻⁴ ❌ **WRONG** (should be a⁻³ for matter)

**Issue:** Pair potential scaling ≠ cosmological energy density scaling

### 2.2 Dipole Term

**Force:** F_d ∝ 1/r³ (from β_d r_dA² scaling)

**Potential:**
```
V_d(r) = -∫ F_d dr = -∫ (C_d / r³) dr = C_d / (2r²)
```

**Scaling:** V_d ∝ 1/a²

**Energy density:** ρ_d ∝ V_d / a³ → ρ_d ∝ a⁻⁵ ❓ **UNVERIFIED**

**Issue:** a⁻⁵ term not standard in cosmology

### 2.3 Quadrupole Term

**Force:** F_q ∝ 1/r⁴ (from β_q² r_A r_P scaling)

**Potential:**
```
V_q(r) = -∫ F_q dr = -∫ (C_q / r⁴) dr = C_q / (3r³)
```

**Scaling:** V_q ∝ 1/a³

**Energy density:** ρ_q ∝ V_q / a³ → ρ_q ∝ a⁻⁶ ❓ **UNVERIFIED**

### 2.4 Friedmann Equation Mapping

**Proposed:**
```
H²(a) = (8πG/3) [ρ_m a⁻³ + ρ_d a⁻⁵ + ρ_q a⁻⁶ + Λ]
```

**Issues:**

1. **Pair potential ≠ background field:** Pairwise V(r) between 2 clusters ≠ cosmic energy density ρ(a)
2. **Averaging ambiguity:** How to sum V_ij over all pairs?
3. **a⁻⁵, a⁻⁶ terms:** Not derived from energy conservation or field equations
4. **Sign convention:** Are dipole/quadrupole repulsive or attractive?

### 2.5 Verdict

**Status:** **PARTIAL** — requires:
- ✅ Unit check passes (force → potential integration correct)
- ⚠️ Mapping to Friedmann equation **NOT verified** — analogy, not derivation
- ❌ a⁻⁵, a⁻⁶ terms **NOT justified** without field-theoretic derivation
- ❌ Sign conventions **NOT confirmed**

**Recommendation:** **DO NOT ACCEPT** a⁻⁵ term until:
1. Field-theoretic derivation from MULTING Lagrangian provided
2. Or author confirms this is the intended scaling

---

## Part 3: Candidate B+G Hybrid — Lattice-Hamiltonian

### Formulation

Combine discrete lattice (B) with potential (G):

**Energy:**
```
E = (1/2) μ Ḋ_AB² + V_MULT(D_AB)
```

Where:
- D_AB(t) = a(t) D₀ (comoving distance)
- Ḋ_AB = D₀ ȧ(t)

**Substitute:**
```
E = (1/2) μ D₀² ȧ² + V_MULT(a D₀)
```

**Divide by μ D₀²:**
```
E / (μ D₀²) = (1/2) ȧ² + V_MULT(a D₀) / (μ D₀²)
```

**Define H = ȧ/a:**
```
(1/2) a² H² + V_MULT(a D₀) / (μ D₀²) = E / (μ D₀²)
```

### 3.1 D₀ Dependence Check

**Question:** Does equation depend on arbitrary D₀?

**Answer:** **YES** — V_MULT(a D₀) depends on D₀ unless V has specific scaling

**Example:** If V_MULT ∝ 1/D → V_MULT(a D₀) = C / (a D₀) → depends on D₀

**Can D₀ be absorbed?**
- Only if V_MULT has power-law scaling: V ∝ D⁻ⁿ
- Then V_MULT(a D₀) = C D₀⁻ⁿ a⁻ⁿ
- D₀⁻ⁿ can be absorbed into constant

**Verdict:** ✅ **CONDITIONAL** — works if V_MULT is power-law

### 3.2 Newtonian/FLRW Limit

**Question:** Does it reduce to standard cosmology?

**Test:** If F_oP → -G m_A m_P / D², then V_MULT → -G m_A m_P / D

**Energy equation:**
```
(1/2) a² H² - (G m_A m_P) / (μ a D₀²) = const
```

**Solve for H²:**
```
H² = (2/a²) [const + (G m_A m_P) / (μ a D₀²)]
```

**Issue:** This gives H² ∝ a⁻³ (matter-dominated), NOT H² ∝ a⁻² (expected from Friedmann)

**Verdict:** ⚠️ **SCALING MISMATCH** — does not cleanly reduce to FLRW

### 3.3 Free Parameter Count

| Parameter | Source |
|-----------|--------|
| m_A(z), m_P(z) | Cluster masses |
| k_A(z), k_P(z) | Force constants |
| r_A(z), r_P(z) | Cluster radii |
| β_d, β_q | Scaling factors (fitted: 4.5, 18.0) |
| D₀ | Lattice spacing (arbitrary) |
| N_eff | Neighbor count |

**Minimum:** 2 (β_d, β_q) if all cluster variables known  
**Maximum:** 8+ if m, k, r vary with z

**Verdict:** ⚠️ **PARAMETER DEGENERACY RISK** — too many free parameters can fit any H(z)

### 3.4 Verdict

**Status:** **CONDITIONAL** — viable IF:
- V_MULT has power-law scaling (allows D₀ absorption)
- FLRW limit mismatch explained
- Parameter count justified

**Risk:** **MEDIUM** — less economical than pure B or pure G

---

## Part 4: Candidate C — Virial Pressure (Backup)

### Formula

```
P_eff = -(1 / 3V_cell) Σ F_AB · D_AB
```

Then use virial relation to derive ä/a.

### 4.1 Unit Check

| Term | Units |
|------|-------|
| F_AB | [M L T⁻²] |
| D_AB | [L] |
| F_AB · D_AB | [M L² T⁻²] = Energy |
| V_cell | [L³] |
| P_eff | [M L⁻¹ T⁻²] = Pressure ✅ |

**Result:** ✅ **UNITS CORRECT**

### 4.2 Sign Convention

**Virial theorem:** For attractive forces, P_eff < 0

**Effect:** Negative pressure → ä > 0 (acceleration)

**Result:** ✅ **SIGN PLAUSIBLE**

### 4.3 Relation to Acceleration

**Friedmann acceleration equation:**
```
ä/a = -(4πG/3)(ρ + 3P/c²)
```

If P_eff interpreted as P_MULT:
```
ä/a ∝ -(ρ_MULT + 3P_MULT)
```

**Issue:** How to map P_eff → cosmological pressure?

**Verdict:** ⚠️ **MAPPING AMBIGUOUS** — virial pressure ≠ fluid pressure

### 4.4 Free Parameter Count

Same as Candidate B: m, k, r, D, N_eff

**Verdict:** ⚠️ **MORE PHYSICAL, LESS ECONOMICAL** than direct force approach

### 4.5 Verdict

**Status:** **BACKUP** — viable if Candidates B, G, B+G fail

**Advantage:** More grounded in statistical mechanics  
**Disadvantage:** More complex, not more predictive

---

## Part 5: Phi(z) Heuristic — Dimensional Review

### Formula (AI Transcript Candidate)

```
Φ(z) = A_m(z) - A_d(z) + A_q(z)

H_MULT²(z) = H_anchor² × [Φ(z) / Φ(anchor)]
```

Where A_m, A_d, A_q are "amplitude" functions (under-specified).

### 5.1 Dimensional Analysis

**Question:** Does Φ(z) → H²(z) mapping have correct dimensions?

**Check:**

| Term | Units | Notes |
|------|-------|-------|
| F_m / μ | [L T⁻²] | Acceleration |
| Φ (if = F/μ) | [L T⁻²] | Acceleration |
| H² | [T⁻²] | 1/time² |

**Problem:** [L T⁻²] ≠ [T⁻²] — **missing length scale L**

**If Φ is dimensionless ratio:**
```
Φ = (F_oP / μ) / (F_ref / μ) = F_oP / F_ref
```

Then:
```
H² = H_anchor² × Φ
```

**Units work:** [T⁻²] = [T⁻²] × [dimensionless] ✅

**BUT:** Physical scaling lost — H² now depends only on force **ratios**, not absolute forces

**Issue:** No explicit length scale (D_AB) → under-specified

### 5.2 Physical Interpretation

**What Phi(z) does:**
- Reproduces Table A1 H_MULT(z) values
- Uses AI service output (black box)
- Phenomenological fit

**What Phi(z) does NOT do:**
- Derive H_MULT from MULTING physics
- Provide forward model (cannot predict new z)
- Specify cluster variables or geometry

### 5.3 Status

- ✅ **TABLE_REPRODUCTION_HEURISTIC** — useful for fitting Table A1
- ❌ **NOT_PHYSICAL_BRIDGE** — dimensionally under-specified
- ❌ **NOT_ALLOWED_FOR_PREDICTION** — no forward model
- ⚠️ **AI_INTERPRETATION_CANDIDATE** — not source-confirmed

### 5.4 Verdict

**Use case:** Diagnostic only — compare other candidates against Table A1 via Phi(z) as reference

**Do NOT use for:**
- Prediction on new z
- Physical interpretation
- MCMC parameter estimation
- Claiming "MULTING model validated"

**Wording:** "Phi(z) heuristic is dimensionally under-specified" (NOT "catastrophic")

---

## Part 6: Table A1 Compatibility

**Question:** Could each candidate reproduce Table A1 H_MULT(z) in principle?

| Candidate | Could Reproduce? | Missing Data | Risk | Status |
|-----------|-----------------|--------------|------|--------|
| **B (Lattice ODE)** | ✅ YES | m_A(z), k_A(z), r_A(z), D_AB(z), N_eff | **MEDIUM** — many free parameters | BEST |
| **G (Potential)** | ⚠️ PARTIAL | a⁻⁵, a⁻⁶ terms not verified | **HIGH** — unverified scaling | NEEDS_VERIFICATION |
| **B+G (Hybrid)** | ✅ YES | Same as B + potential scaling | **MEDIUM** — D₀ dependence | CONDITIONAL |
| **C (Virial)** | ✅ YES | Same as B | **MEDIUM** — mapping ambiguity | BACKUP |
| **Phi(z) Heuristic** | ✅ YES (by design) | None (uses Table A1) | **LOW** — but not forward model | TABLE_ONLY |

**Note:** All candidates except Phi require cluster variable tables to proceed.

---

## Part 7: Row 1 (z=0) Integration

### 7.1 Row 1 Status

**Finding:** Row 1 (z=0) has sigma standardization inconsistency:
- sigma_MULT reported: 1.30 (positive)
- sigma_MULT calculated: (71.1 - 73.0) / 1.1 = -1.727 (negative)
- Diff: 3.027 >> tolerance 0.11 (27× exceeded)

**Rows 2-12:** All consistent (max diff 0.039, within tolerance)

**Classification:**
- ⚠️ **SOURCE_TABLE_OUTLIER** — not transcription error, table-level inconsistency
- ⚠️ **AMBIGUOUS** — PDF shows "±1.6" but calculation requires sigma_H=1.1

### 7.2 Recommendation for Diagnostics

**Exclude Row 1 from any internal fit** until author clarifies:
1. Is sigma_MULT at z=0 an absolute value or signed residual?
2. Is sigma_H for standardization different from H-data uncertainty?
3. Does z=0 anchor point use different convention?

**Use Rows 2-12 only** for diagnostic purposes:
- Internal consistency checks
- Candidate plausibility tests
- Parameter range estimation

**Do NOT:**
- Claim "11/12 validation" — this is diagnostic, not validation
- Use Row 1 to estimate H₀ — value may be non-standard
- Extrapolate to z=0 without author confirmation

### 7.3 Author Question (Q14)

See docs/26_author_clarification_brief.md Q14:

> "Row 1 (z=0) sigma values show larger-than-expected differences between reported and calculated. Could you clarify whether z=0 uses a different standardization convention?"

---

## Summary Table

| Candidate | Dimensional | Sign | Missing Inputs | MCMC | Prediction | Status |
|-----------|-------------|------|---------------|------|------------|--------|
| **B (Lattice)** | ✅ PASS | ✅ PASS | ❌ MANY | ❌ BLOCKED | ❌ BLOCKED | **BEST** |
| **G (Potential)** | ⚠️ PARTIAL | ❓ UNKNOWN | ❌ MANY | ❌ BLOCKED | ❌ BLOCKED | NEEDS_VERIFICATION |
| **B+G (Hybrid)** | ⚠️ CONDITIONAL | ✅ PASS | ❌ MANY | ❌ BLOCKED | ❌ BLOCKED | CONDITIONAL |
| **C (Virial)** | ✅ PASS | ✅ PASS | ❌ MANY | ❌ BLOCKED | ❌ BLOCKED | BACKUP |
| **Phi(z) Heuristic** | ❌ UNDER-SPECIFIED | N/A | ✅ NONE | ❌ BLOCKED | ❌ BLOCKED | TABLE_ONLY |

---

## Next Safe Step

**Option 1:** **RECOMMENDED** — Author Clarification (Q15)

> "I am exploring a possible computational interpretation where pairwise MULTING acceleration F_oP/(μ×D_AB) is averaged over nearest neighbors to produce ä/a, then integrated to H(z). Is this closer to the intended Table A1 calculation route, or does the AI service use a different averaging or phenomenological rule?"

**Option 2:** Diagnostic-only parameter estimation on Rows 2-12

- Fit Candidate B to Rows 2-12 using reasonable cluster variable estimates
- **Label:** DIAGNOSTIC_INTERNAL_TEST (NOT validation)
- **Purpose:** Check whether H_MULT(z) shape is plausible under MULTING physics

**Option 3:** Wait for cluster variable tables from author

**BLOCKED until:**
- Author confirms intended bridge method
- Cluster variables provided: m_A(z), k_A(z), r_A(z), D_AB(z), N_eff

---

## Verdict

**Best Internal Candidate:** **Candidate B (Discrete Lattice ODE)**
- Dimensionally consistent ✅
- Physically motivated ✅
- Requires cluster variables ❌
- Risk: may become our model, not Buckholtz's ⚠️

**MCMC Status:** ❌ **BLOCKED**  
**Prediction Status:** ❌ **BLOCKED**  
**Author Clarification:** ✅ **HIGH PRIORITY**

**Next:** Add Q15 to docs/26, wait for author response before proceeding to parameter estimation.

---

**End of Mathematical Stress Test**
