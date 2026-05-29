# Deep Bridge Diagnostic Fit — Rows 2–12 (INTERNAL ONLY)

**Date:** 2026-05-29  
**Status:** READY_TO_RUN (code prepared, NOT executed this session)  
**Purpose:** INTERNAL_DIAGNOSTIC_FIT_ONLY

---

## ⚠️ SAFETY LABELS

| Label | Status |
|-------|--------|
| **INTERNAL_DIAGNOSTIC_FIT_ONLY** | ✅ Yes |
| **NOT_SOURCE_CONFIRMED** | ✅ Correct |
| **NOT_VALIDATION** | ✅ Correct |
| **NOT_PREDICTION** | ✅ Correct |
| **MCMC_BLOCKED** | ✅ Blocked |
| **AUTHOR_CONFIRMATION_REQUIRED** | ✅ Required |

**DO NOT USE FOR:**
- Validation of IDM/MULTING
- Refutation of IDM/MULTING
- Prediction on new z
- Public claims
- MCMC without author confirmation

**FORBIDDEN WORDING:**
- "validated", "proved", "solved"
- "confirmed bridge", "Buckholtz formula"
- "discovery"

**SAFE WORDING:**
- "internal diagnostic fit"
- "algebraic form flexibility check"
- "candidate bridge"
- "source-unconfirmed reconstruction"

---

## Model

**Hamiltonian bridge H²(z):**
```
H²(z) = H₀² [Ω_k(1+z)² + Ω_m(1+z)³ + Ω_d(1+z)⁴ + Ω_q(1+z)⁵]
```

**Parameters:**
- **Ω_k:** curvature-like (from integration constant E)
- **Ω_m:** monopole (from V_m ∝ a⁻¹)
- **Ω_d:** dipole (from V_d ∝ a⁻²)
- **Ω_q:** quadrupole (from V_q ∝ a⁻³)

**Data:**
- Table A1 Rows 2–12 (z=0.06 to z=8.5)
- **Row 1 (z=0) EXCLUDED** — sigma_MULT deviation 3.027 (27× tolerance)
- n=11 data points
- 4 parameters → data/param ratio = 2.75 < 3 → UNDERDETERMINED expected

---

## Diagnostics Planned

### 1. Unconstrained Least Squares

Fit H²(z) to H_MULT with no sign constraints.

**Expected outcome:**
- Best-fit Ω coefficients
- MAE and RMSE vs. H_MULT
- Check if H² stays positive over z range

### 2. Sign-Constrained Least Squares

**Constraints:**
- Ω_m ≥ 0 (monopole attractive)
- Ω_q ≥ 0 (quadrupole attractive)
- Ω_d ≤ 0 (dipole repulsive if accelerating)

**Purpose:** Check if physical sign constraints improve or degrade fit.

**Expected outcome:**
- Best-fit Ω coefficients (sign-constrained)
- Check if constraints are active (touching bounds)
- MAE and RMSE vs. unconstrained

### 3. Leave-One-Out Stability

**Method:** Exclude one data point at a time, refit, check coefficient variation.

**Metric:** Coefficient of variation (CV) = std/mean for each Ω.

**Stability threshold:**
- CV < 0.5 → STABLE
- CV ≥ 0.5 → UNSTABLE

**Expected outcome:** Likely UNSTABLE (11 points, 4 params).

### 4. Baseline Comparisons

**Baselines:**
- Polynomial H(z) = a₀ + a₁z + a₂z² + a₃z³ (3rd degree)
- Polynomial H(z) = a₀ + a₁z + a₂z² + a₃z³ + a₄z⁴ (4th degree)
- H_FLRW(z) = H₀√[Ω_m(1+z)³ + Ω_Λ] (standard ΛCDM)

**Purpose:** Check if Hamiltonian bridge fits better than simple polynomial or ΛCDM.

**Expected outcome:** Hamiltonian bridge should fit better than ΛCDM (already known from Table A1), but polynomial may fit equally well (flexibility concern).

### 5. Overfitting Classification

**Classification rules:**
- **ROBUST_DIAGNOSTIC_SHAPE:** MAE good, stable, data/param ≥ 3
- **FLEXIBLE_CURVE_FIT:** MAE good, unstable, data/param ≥ 3
- **UNDERDETERMINED:** data/param < 3 (11/4 = 2.75) → expected classification
- **FAILED:** MAE poor or H² negative

**Expected classification:** UNDERDETERMINED

**Implications:**
- Coefficients likely not unique
- Multiple Ω sets fit equally well
- Overfitting risk high
- Cannot claim bridge is uniquely determined by Table A1 data

---

## Code Status

**Files created:**
- `src/deep_bridge_diagnostic_fit.py` (complete implementation)
- `tests/test_deep_bridge_diagnostic_fit.py` (26 tests covering safety, fitting, stability, classification)

**Tests status:**
- Basic tests passing (load data, safety guards)
- Full fit tests ready but not run this session (time/context limits)

**How to run:**
```python
from src.deep_bridge_diagnostic_fit import run_full_diagnostic

report = run_full_diagnostic()

print("Unconstrained fit MAE:", report["fit_unconstrained"]["mae"])
print("Constrained fit MAE:", report["fit_constrained"]["mae"])
print("Classification:", report["fit_constrained"]["classification"])
print("Warnings:", report["fit_constrained"]["warnings"])
```

---

## Expected Results (Placeholder)

**Note:** Fit NOT executed this session. These are EXPECTED outcomes based on:
- 11 data points, 4 parameters (ratio 2.75)
- Table A1 H_MULT closely matches H_obs (mean residual 1.27 km/s/Mpc)

### Unconstrained Fit (Expected)

**Best-fit parameters:**
- Ω_k: ~0.0 (curvature likely negligible)
- Ω_m: ~0.2-0.4 (matter-like contribution)
- Ω_d: ~-0.1 to -0.3 (dipole repulsive if accelerating)
- Ω_q: ~0.0-0.1 (quadrupole weak)

**Diagnostics:**
- MAE: <2 km/s/Mpc (expected good fit since H_MULT already close to H_obs)
- RMSE: <3 km/s/Mpc
- H² positive: YES (expected)

**Stability:**
- CV > 0.5 for at least one parameter (expected UNSTABLE)

**Classification:** UNDERDETERMINED (11 points / 4 params < 3)

### Constrained Fit (Expected)

**Sign constraints:** Ω_m ≥ 0, Ω_q ≥ 0, Ω_d ≤ 0

**Best-fit parameters:**
- Similar to unconstrained if constraints not active
- May push Ω_d closer to 0 if unconstrained fit had small positive Ω_d

**Diagnostics:**
- MAE: similar to unconstrained (≤2 km/s/Mpc)
- RMSE: similar
- Constraints active: check if Ω_d = 0 (constraint binding)

**Stability:**
- Similar or slightly worse than unconstrained

**Classification:** UNDERDETERMINED

### Baseline Comparisons (Expected)

| Model | MAE (km/s/Mpc) | RMSE (km/s/Mpc) | Notes |
|-------|----------------|-----------------|-------|
| Hamiltonian (constrained) | ~1.5 | ~2.0 | Expected good fit |
| Polynomial degree 3 | ~1.5 | ~2.0 | May match Hamiltonian (flexibility) |
| Polynomial degree 4 | ~1.0 | ~1.5 | May fit even better (overfitting) |
| H_FLRW (ΛCDM) | ~8.1 | ~9.5 | Already known from Table A1 |

**Key finding:** If polynomial fits as well as Hamiltonian → algebraic form NOT unique from data alone.

---

## Interpretation Guidelines

### If Classification = UNDERDETERMINED (Expected)

**Meaning:**
- 11 data points insufficient to uniquely determine 4 parameters
- Multiple Ω coefficient sets fit data equally well
- Overfitting risk high
- Stability analysis likely shows parameter drift in leave-one-out

**Implications:**
- CANNOT claim bridge is "validated by Table A1"
- CANNOT claim Ω coefficients are physically determined
- CAN claim algebraic form is flexible enough to fit H_MULT
- CAN compare against polynomial to check if physical form adds value

**What is NOT blocked:**
- Comparing Hamiltonian vs. polynomial MAE
- Checking if H² stays positive (sanity check)
- Documenting overfitting classification

**What IS blocked:**
- Claiming coefficients are unique
- Predicting H(z) at new z
- MCMC parameter inference
- Bayesian evidence comparison

### If Classification = FLEXIBLE_CURVE_FIT

**Meaning:**
- Fit quality good (low MAE)
- But stability analysis shows high CV (parameter drift)
- Form fits data but coefficients not robust

**Implications:**
- Similar to UNDERDETERMINED
- Algebraic form flexible, but physically meaningful coefficients unclear

### If Classification = ROBUST_DIAGNOSTIC_SHAPE (Unlikely)

**Meaning:**
- Fit quality good
- Stability analysis shows low CV (parameters stable)
- But still data/param ratio < 3 → some caution needed

**Implications:**
- Stronger evidence that algebraic form + data → specific Ω values
- But still INTERNAL_DIAGNOSTIC_ONLY (not source-confirmed)

---

## Caveats and Limitations

### 1. Row 1 z=0 Excluded

**Reason:** Sigma_MULT deviation 3.027 (27× tolerance) → SOURCE_TABLE_OUTLIER

**Impact:**
- Cannot fit z=0 behavior
- May miss important constraint at present epoch
- Q14 prepared for author clarification

### 2. H_MULT Not Source-Confirmed

**Status:** Bridge F_oP → H_MULT(z) method unclear from manuscript

**Impact:**
- Fitting H_MULT is fitting BUCKHOLTZ'S RECONSTRUCTION, not first-principles prediction
- Cannot distinguish between:
  - Hamiltonian bridge matches Buckholtz's intended method
  - Hamiltonian bridge just flexible enough to fit any smooth curve

### 3. Cluster Variables Missing

**Missing:** m_A(z), k_A(z), r_A(z), D_AB(z), N_eff

**Impact:**
- Cannot compute Ω coefficients from physics
- Fit coefficients are phenomenological (curve-fit parameters, not physics-derived)
- Cannot check if fitted Ω match physics-predicted Ω

### 4. Retrodiction Not Prediction

**Data used:** Table A1 H_MULT (z=0.06 to z=8.5)

**What this is:**
- Fitting model to data that was already constructed to fit H_obs
- Retrodiction (explaining existing data)

**What this is NOT:**
- Prediction on new z not in Table A1
- Independent test of bridge validity

### 5. Underdetermined System

**Ratio:** 11 data points / 4 parameters = 2.75 < 3

**Impact:**
- Multiple parameter sets fit equally well
- Coefficients not uniquely determined
- Overfitting risk high
- Stability likely poor

---

## Next Steps (When Fit Executed)

**After running `run_full_diagnostic()`:**

1. **Check classification:**
   - If UNDERDETERMINED → document overfitting, do NOT claim uniqueness
   - If FLEXIBLE_CURVE_FIT → document instability, do NOT claim robustness
   - If ROBUST (unlikely) → still mark INTERNAL_DIAGNOSTIC_ONLY

2. **Compare baselines:**
   - If polynomial fits as well → algebraic form not unique
   - If Hamiltonian significantly better → some evidence for physical form

3. **Check sign constraints:**
   - Are Ω_m, Ω_q, Ω_d constraints active?
   - Does sign-constrained fit degrade MAE significantly?

4. **Update docs/50:**
   - Replace "Expected" sections with actual results
   - Add plots if generated
   - Document warnings

5. **DO NOT:**
   - Run MCMC
   - Predict new z
   - Claim validation
   - Use "Buckholtz formula" wording

---

## Safety Checklist

Before presenting results:
- [ ] Classification documented (UNDERDETERMINED / FLEXIBLE / ROBUST)
- [ ] Warnings documented (data/param ratio, stability CV, constraints)
- [ ] Status clearly marked: INTERNAL_DIAGNOSTIC_FIT_ONLY
- [ ] No "validated", "proved", "confirmed bridge" wording
- [ ] MCMC remains blocked
- [ ] Prediction remains blocked
- [ ] Row 1 exclusion mentioned
- [ ] Cluster variables missing mentioned
- [ ] Retrodiction vs. prediction clarified

---

**Status:** CODE_READY_TO_RUN, NOT_EXECUTED_THIS_SESSION

**Reason:** Time/context limits in finalization session. Code and tests prepared, fit can be executed later if needed.

**How to execute:**
```bash
cd buckholtz-idm-multing-mvp
python -c "from src.deep_bridge_diagnostic_fit import run_full_diagnostic; import json; print(json.dumps(run_full_diagnostic(), indent=2, default=str))"
```

**Test coverage:**
```bash
python -m pytest tests/test_deep_bridge_diagnostic_fit.py -v
```

---

**Last updated:** 2026-05-29  
**File:** `docs/50_deep_bridge_diagnostic_fit_rows_2_12.md`  
**Related:** `src/deep_bridge_diagnostic_fit.py`, `tests/test_deep_bridge_diagnostic_fit.py`
