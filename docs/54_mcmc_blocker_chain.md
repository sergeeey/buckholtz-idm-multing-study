# MCMC Blocker Chain — Buckholtz IDM/MULTING Project

**Date:** 2026-05-29  
**Status:** MCMC_BLOCKED  
**Purpose:** Document why MCMC comparison ΛCDM vs. MULTING is blocked and what must happen to unblock

---

## Executive Summary

**Current evidence:** Table A1 shows that H_MULT is about **6× closer to H_obs than H_FLRW** (mean residuals: 1.27 vs. 8.13 km/s/Mpc). This is a **strong retrodictive signal** indicating that a MULTING-inspired parameterization can track the reported H(z) data in Table A1.

**Critical limitation:** **Table A1 is useful evidence that the MULTING-inspired fit can track the reported H(z) data, but it is not yet an out-of-sample predictive test.** Beta parameters (β_d=4.5, β_q=18.0) were fitted to or reported alongside this data, making Table A1 part of the reconstruction process, not an independent validation set.

**Main blocker:** The confirmed computational bridge **F_oP → H_MULT(z)** is **missing**. Appendix A1 Step 6 refers to an "AI service" generating H_MULT candidates but does not provide the explicit formula or bridge method. Without source confirmation, we cannot distinguish between:
- The Hamiltonian bridge being Buckholtz's intended method
- The Hamiltonian bridge being our independent reconstruction that happens to fit Table A1

**MCMC status:** **BLOCKED** until:
1. Bridge method source-confirmed
2. Cluster variables provided or effective parameterization defined
3. Independent out-of-sample data integrated
4. Model complexity penalty applied (AIC/BIC)

**Current allowed work:** Internal diagnostic fit (Rows 2-12), leave-one-out stability, baseline comparisons — all labeled **INTERNAL_DIAGNOSTIC_FIT_ONLY, NOT_VALIDATION**.

**Project state:** **WAITING_FOR_AUTHOR_RESPONSE** — Q14-Q18 prepared (NOT sent), awaiting first letter response.

---

## Current Evidence

### Table A1 Retrodiction Performance

**Data:** 12 rows (z=0 to z=8.5), 7 columns

**H_MULT residuals (Rows 2-12 only):**
- Mean absolute deviation from H_obs: **1.27 km/s/Mpc**
- Root mean squared error: ~2 km/s/Mpc

**H_FLRW residuals (Rows 2-12):**
- Mean absolute deviation from H_obs: **8.13 km/s/Mpc**
- Root mean squared error: ~9.5 km/s/Mpc

**Performance ratio:** H_MULT is about **6× closer** to H_obs than H_FLRW

**Beta parameters (Table A1 caption):**
- β_d = 4.5 (dipole strength)
- β_q = 18.0 (quadrupole strength)
- **Status:** FITTED or TABLE_REPORTED (manuscript says "online service reported choosing")

**Row 1 (z=0) anomaly:**
- sigma_MULT deviation: 3.027 (27× tolerance exceeded)
- **Status:** SOURCE_TABLE_OUTLIER
- **Action:** Excluded from fits, Q14 prepared for clarification

**Rows 2-12:**
- Sigma consistency: max deviation 0.039 (passes adaptive tolerance)
- **Status:** Usable for INTERNAL_DIAGNOSTIC_FIT_ONLY

### Evidence Classification

| Evidence Type | Status |
|---------------|--------|
| **H_MULT vs. H_FLRW comparison** | ✅ RETRODICTION_EVIDENCE |
| **Prediction on new z** | ❌ NOT_PREDICTION |
| **Validation of MULTING theory** | ❌ NOT_VALIDATION |
| **Table A1 as training data** | ⚠️ Part of beta fit process |
| **Table A1 as test data** | ❌ Cannot use same data for both |

**Key limitation:** Beta parameters fitted/reported using data that includes Table A1 → circular if Table A1 is sole validation dataset.

---

## MCMC Blocker Chain

**Four sequential blockers prevent scientific MCMC comparison:**

```
MCMC Test (ΛCDM vs. MULTING)
    ↓ BLOCKED BY
Blocker 1: Source-Confirmed Bridge Missing
    ↓ AND
Blocker 2: Cluster Variable Evolution Missing
    ↓ AND
Blocker 3: Independent Out-of-Sample Data Missing
    ↓ AND
Blocker 4: Model Complexity Penalty Not Applied
    ↓
RESULT: MCMC_BLOCKED
```

---

### Blocker 1: Source-Confirmed Bridge Missing

**Problem:** Appendix A1 Step 6 states "AI service" generates H_MULT candidates but does not provide explicit H_MULT(z) formula or computational bridge method.

**What we need:** A confirmed rule for how pairwise force law F_oP maps to cosmological expansion H_MULT(z).

**Possible bridge families:**
1. **AI / Phi-scaling heuristic:** H_MULT = Φ(z) × H_FLRW
   - Status: Phenomenological, dimensionally under-specified
2. **Hamiltonian / Layzer-Irvine energy bridge:** H²(a) from E = ½μḊ² + V_MULT
   - Status: Algebraically valid, NOT source-confirmed
3. **Discrete lattice / neighbor acceleration:** ä/a = N_eff F_oP/(μ D_AB)
   - Status: Physically interesting, data-heavy
4. **Effective stress-energy / averaging prescription:** Coarse-graining rule
   - Status: Not discussed in manuscript
5. **Another author-intended rule:** Unknown method

**Current status:**

| Aspect | Status |
|--------|--------|
| **Bridge method identification** | ❌ UNKNOWN |
| **Hamiltonian bridge verification** | ✅ ALGEBRAICALLY_VALID |
| **Hamiltonian source confirmation** | ❌ NOT_CONFIRMED |
| **Author clarification** | ⏳ Q15, Q16 prepared (NOT sent) |
| **MCMC readiness** | ❌ BLOCKED |

**Why this blocks MCMC:**

Without knowing which bridge is intended, we cannot:
- Implement `compute_Hz_MULTING(z, params)` with confidence
- Define parameter space (which Ω coefficients? which cluster variables?)
- Specify priors (physical ranges depend on bridge type)
- Claim we're testing "Buckholtz's MULTING" vs. our reconstruction

**Clarification needed:** Q15 asks which bridge family is closest to author's method, Q16 asks if Hamiltonian approach is intended.

**Unblock condition:** Author confirms bridge method OR explicitly authorizes Hamiltonian as independent reconstruction labeled separately.

---

### Blocker 2: Cluster Variable Evolution Missing

**Problem:** If the bridge uses explicit cluster variables (as suggested by pairwise force approach), we need evolution functions or effective parameterization.

**Missing variables:**
- **m_A(z):** Cluster A mass evolution
- **m_P(z):** Cluster P mass evolution
- **r_A(z):** Cluster A radius evolution
- **r_P(z):** Cluster P radius evolution
- **k_A(z), k_P(z):** Cluster structure parameters
- **D_AB(z):** Inter-cluster separation evolution
- **N_eff:** Effective number of cluster pairs per comoving volume

**Why needed:**

For Hamiltonian bridge H²(a) = H₀²[Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵], Ω coefficients must be computed from:
```
Ω_m ~ G m_A m_P / (H₀² D₀)
Ω_d ~ C_d / (H₀² D₀²)
Ω_q ~ C_q / (H₀² D₀³)

where C_d, C_q depend on cluster multipole moments
```

Without cluster variables, Ω coefficients become **phenomenological fit parameters** rather than physics-derived quantities.

**Current status:**

| Variable | Manuscript Status | Impact |
|----------|------------------|--------|
| m_A, m_P | Not provided | Cannot compute Ω_m from physics |
| r_A, r_P | Not provided | Cannot compute multipole moments |
| k_A, k_P | Not provided | Cannot compute force law coefficients |
| D_AB(z) | Not provided | Cannot predict H(z) at arbitrary z |
| N_eff | Not provided | Cannot normalize pair density |

**Workaround options:**

1. **Request cluster variables from author** (Q17 prepared)
2. **Effective parameterization:** Treat Ω_k, Ω_m, Ω_d, Ω_q as free parameters
   - Pro: Allows fitting without cluster data
   - Con: Loses connection to pairwise force law, increases parameter count
3. **Infer from observations:** Use cluster mass functions, velocity dispersions
   - Pro: Data-driven
   - Con: Requires additional modeling, uncertain error propagation

**Unblock condition:** Author provides cluster evolution functions OR authorizes effective parameterization with clear labeling.

---

### Blocker 3: Independent Out-of-Sample Data Required

**Problem:** Using the same data that were used to fit β_d and β_q creates circular reasoning.

**Table A1 role in parameter fitting:**

From manuscript: "online service reported choosing β_d = 4.5 and β_q = 18.0"

**Interpretation:**
- Beta parameters were **selected/fitted** to achieve good H_MULT vs. H_obs agreement
- Table A1 H_MULT values reflect this choice
- Using Table A1 as validation dataset = testing model on training data

**Why circular:**
```
Beta fit process:
  1. Try different (β_d, β_q) combinations
  2. Compute H_MULT for each
  3. Select (β_d, β_q) that minimizes |H_MULT - H_obs|
  4. Report selected values in Table A1

Circular validation:
  "Table A1 shows H_MULT matches H_obs well"
  → But H_MULT was constructed to match H_obs!
```

**Correct statement:** "Table A1 can be used as a **reconstruction target** or **sanity check**, but not as the sole validation dataset."

**Independent datasets needed:**

| Dataset | Type | N points | z range | Status |
|---------|------|----------|---------|--------|
| **Pantheon+ supernovae** | Distance modulus | ~1700 | 0.01-2.3 | Not integrated |
| **DESI BAO** | Angular diameter distance | ~dozen | 0.3-2.3 | Not integrated |
| **Cosmic Chronometers** | H(z) direct | ~30 | 0.07-1.97 | Not integrated |
| **Union3 supernovae** | Distance modulus | ~2000 | 0.01-2.3 | Not integrated |
| **DES-SN5YR** | Distance modulus | ~1800 | 0.025-1.13 | Not integrated |

**Recommended test strategy:**

1. **Fit phase:** Use Table A1 H_MULT to determine Ω coefficients (if Hamiltonian confirmed)
2. **Validation phase:** Predict on Pantheon+, BAO, Cosmic Chronometers
3. **Comparison:** Compute ΛCDM vs. MULTING likelihood on independent data
4. **Report:** Out-of-sample performance, not in-sample reproduction

**Current status:**
- ❌ No independent data integrated
- ❌ No out-of-sample prediction performed
- ⚠️ Table A1 usable only as reconstruction check, NOT validation

**Unblock condition:** Integrate ≥1 independent dataset (Pantheon+, BAO, or Cosmic Chronometers) for out-of-sample testing.

---

### Blocker 4: Model Complexity Penalty Required

**Problem:** MULTING (or any reconstructed bridge) may introduce additional parameters beyond ΛCDM's Ω_m, Ω_Λ, H₀.

**Parameter count comparison:**

| Model | Parameters | Notes |
|-------|------------|-------|
| **ΛCDM (standard)** | 3 | Ω_m, Ω_Λ, H₀ (flat: Ω_k=0) |
| **ΛCDM (non-flat)** | 4 | + Ω_k |
| **Hamiltonian (phenomenological)** | 5 | Ω_k, Ω_m, Ω_d, Ω_q, H₀ |
| **Hamiltonian (physics-derived)** | 5+ | + cluster variables m_A, r_A, D_AB, etc. |
| **Phi-scaling heuristic** | 4-6 | H₀ + polynomial Φ(z) coefficients |
| **Lattice N-body** | 10+ | + N_eff, cluster evolution functions |

**Why complexity matters:**

**Naive comparison (WRONG):**
```
χ²_MULTING < χ²_ΛCDM → MULTING is better
```

**Correct comparison:**
```
1. Compute χ² for both models
2. Apply complexity penalty:
   AIC = χ² + 2k  (Akaike Information Criterion)
   BIC = χ² + k ln(N)  (Bayesian Information Criterion)
3. Compare penalized scores
4. Check if MULTING improvement justifies extra parameters
```

**Example:**

Suppose (hypothetical numbers):
- N = 30 data points (Cosmic Chronometers)
- ΛCDM: k=3, χ²=45 → AIC=51, BIC=55
- MULTING: k=5, χ²=40 → AIC=50, BIC=57

**Analysis:**
- MULTING has lower χ² (better fit)
- MULTING has lower AIC (improvement justifies 2 extra params)
- MULTING has higher BIC (penalty harsher for small N)
- **Verdict:** Weak evidence for MULTING (depends on criterion)

**Required for scientific comparison:**

1. **Likelihood function:**
   ```
   L = exp(-χ²/2) where χ² = Σ[(H_model - H_obs)² / σ²]
   ```

2. **Information criteria:**
   - AIC (Akaike)
   - BIC (Bayesian)
   - DIC (Deviance, if using MCMC)

3. **Posterior predictive checks:**
   - Simulate data from fitted model
   - Compare to observed data distribution
   - Check for systematic residuals

4. **Parameter count transparency:**
   - List all free parameters
   - Justify each parameter physically
   - Document which are fitted vs. fixed

**Important wording:** "A lower residual is not enough. MULTING must improve fit enough to justify additional degrees of freedom."

**Current status:**
- ❌ AIC/BIC comparison not implemented
- ❌ Posterior predictive checks not performed
- ⚠️ Parameter count clear (5 for Hamiltonian) but penalty not applied

**Unblock condition:** Implement AIC/BIC comparison in MCMC workflow, document complexity penalty results.

---

## What Would Unblock MCMC

**Requirements table:**

| Requirement | Current Status | Needed to Unblock |
|-------------|---------------|-------------------|
| **Source-confirmed bridge** | ❌ Missing | Author confirms formula/rule (Q15, Q16) |
| **Cluster variables** | ❌ Missing/under-specified | Functions, tables, or effective parameterization (Q17) |
| **Independent data** | ❌ Not integrated | Pantheon+, BAO, or Cosmic Chronometers |
| **Priors** | ❌ Missing | Physically justified parameter ranges |
| **Likelihood function** | ❌ Not defined | Dataset-specific likelihood (Gaussian, Poisson, etc.) |
| **Complexity penalty** | ⚠️ Planned | AIC/BIC/Bayes comparison implemented |
| **Row 1 z=0 issue** | ⚠️ Outlier | Exclude or clarify via Q14 |
| **MCMC sampler** | ✅ Available | emcee, PyMC, NumPyro (ready but blocked) |
| **Diagnostic fit code** | ✅ Ready | `src/deep_bridge_diagnostic_fit.py` (INTERNAL_ONLY) |

**Minimum viable unblock path:**

1. **Author confirms Hamiltonian bridge** (or alternative)
   → Bridge status: SOURCE_CONFIRMED
   
2. **Author provides effective parameterization OR authorizes Ω fit**
   → Treat Ω_k, Ω_m, Ω_d, Ω_q as free parameters
   
3. **Integrate Cosmic Chronometers (N~30, easy to parse)**
   → Independent H(z) measurements, no distance modulus conversion
   
4. **Define Gaussian likelihood**
   ```python
   def log_likelihood(params, z, H_obs, sigma_H):
       H_model = compute_Hz_MULTING(z, params)
       chi2 = np.sum(((H_model - H_obs) / sigma_H)**2)
       return -0.5 * chi2
   ```
   
5. **Compute AIC/BIC alongside χ²**
   ```python
   AIC = chi2 + 2 * n_params
   BIC = chi2 + n_params * np.log(n_data)
   ```
   
6. **Run MCMC with emcee**
   - Label output: MCMC_BUCKHOLTZ_AUTHORIZED or MCMC_HAMILTONIAN_RECONSTRUCTION
   - Compare ΛCDM vs. MULTING with complexity penalty
   - Report Bayes factor or BIC difference

**Timeline estimate (if all unblocked):**
- Implementation: 2-3 days
- MCMC run: 1 day (10,000 samples × 20 walkers)
- Analysis: 1-2 days
- **Total:** ~1 week from unblock to results

---

## Safe Work Allowed Now

**Work currently allowed (with safety labels):**

### 1. Internal Diagnostic Fit on Rows 2-12

**Allowed:**
```python
from src.deep_bridge_diagnostic_fit import run_full_diagnostic

report = run_full_diagnostic()
# Fits Hamiltonian H²(a) to Table A1 H_MULT (Rows 2-12)
```

**Required labels:**
- ✅ INTERNAL_DIAGNOSTIC_FIT_ONLY
- ✅ NOT_VALIDATION
- ✅ NOT_PREDICTION
- ✅ NOT_SOURCE_CONFIRMED

**Purpose:**
- Check if Hamiltonian algebraic form fits H_MULT shape
- Assess overfitting (expected: UNDERDETERMINED, 11 points / 4 params)
- Leave-one-out stability analysis
- Compare against polynomial baseline

### 2. Baseline Comparisons

**Allowed:**
- Polynomial H(z) = a₀ + a₁z + a₂z² + a₃z³
- H_FLRW(z) = H₀√[Ω_m(1+z)³ + Ω_Λ]
- Phi-scaling H_MULT = Φ(z) × H_FLRW

**Purpose:** Determine if Hamiltonian bridge fits better than simple heuristics.

### 3. Leave-One-Out Stability

**Allowed:**
- Exclude one data point at a time
- Refit Ω coefficients
- Compute coefficient of variation (CV)
- **Expected:** CV > 0.5 (UNSTABLE due to underdetermined system)

### 4. Overfitting Classification

**Allowed:**
- Classify fit as ROBUST / FLEXIBLE / UNDERDETERMINED / FAILED
- Document warnings (data/param ratio, stability, constraints)
- **Expected classification:** UNDERDETERMINED (11/4 = 2.75 < 3)

### 5. Author Question Preparation

**Allowed:**
- Draft Q15 (bridge method)
- Draft Q16 (Hamiltonian confirmation)
- Draft Q17 (cluster variables)
- **NOT allowed:** Sending without user approval

### 6. Documentation Updates

**Allowed:**
- Document blocker chain (this file)
- Update repo state checklist
- Update discovery ledger
- Prepare MCMC implementation plan (not execution)

---

## Work Not Allowed Yet

**Work currently BLOCKED:**

### 1. MCMC as Buckholtz Theory Test

**Blocked actions:**
- ❌ `compute_Hz_MULTING(z, params)` with SOURCE_CONFIRMED status
- ❌ MCMC sampling treating Hamiltonian as confirmed model
- ❌ Bayesian evidence comparison MULTING vs. ΛCDM
- ❌ Posterior parameter constraints on β_d, β_q
- ❌ Claiming "Buckholtz model prefers β_d=X"

**Why blocked:** Bridge not source-confirmed.

**Allowed alternative:** MCMC with label `HAMILTONIAN_RECONSTRUCTION_INDEPENDENT` if explicitly authorized.

### 2. Prediction on New Redshift

**Blocked actions:**
- ❌ Predict H(z=5.0) using fitted Ω coefficients
- ❌ Forecast H(z) for DESI DR2 redshift bins
- ❌ Extrapolate H_MULT beyond Table A1 range (z>8.5)
- ❌ Claim "MULTING predicts H(z=X) = Y km/s/Mpc"

**Why blocked:** Cluster variables missing + bridge not source-confirmed.

**Allowed alternative:** Interpolate within Table A1 range for visualization only, labeled INTERPOLATION_NOT_PREDICTION.

### 3. Public Validation/Refutation Claim

**Blocked actions:**
- ❌ Paper: "We validate MULTING using Table A1"
- ❌ Preprint: "Buckholtz model preferred over ΛCDM"
- ❌ Blog: "MULTING solves H₀ tension"
- ❌ Tweet: "Discovery: dark matter dipole explains acceleration"
- ❌ Email to author: "Your model is wrong" or "Your model is validated"

**Why blocked:** 
- No source confirmation
- No independent test set
- No author approval for public statements

**Allowed alternative:** Internal reproducibility report, shared privately with author for feedback.

### 4. Using "Buckholtz Formula" Wording

**Blocked wording:**
- ❌ "Buckholtz formula H²(a) = ..."
- ❌ "Confirmed bridge"
- ❌ "Validated"
- ❌ "Proved"
- ❌ "Discovery"

**Why blocked:** Hamiltonian bridge is OUR_COMPUTATIONAL_RECONSTRUCTION, not confirmed by Buckholtz.

**Safe wording:**
- ✅ "Candidate bridge"
- ✅ "Internal reconstruction"
- ✅ "Hamiltonian interpretation (source-unconfirmed)"
- ✅ "Algebraically consistent"
- ✅ "Awaiting author confirmation"

### 5. Using Table A1 as Both Training and Validation

**Blocked actions:**
- ❌ Fit Ω on Rows 2-12 → validate on Rows 2-12 → claim success
- ❌ Use same data for parameter estimation and goodness-of-fit test
- ❌ Report Table A1 χ² as validation metric without independent test

**Why blocked:** Circular reasoning (model fitted to data, then tested on same data).

**Allowed alternative:** 
- Fit on Table A1 (reconstruction phase)
- Test on Pantheon+/BAO/Cosmic Chronometers (validation phase)

### 6. Ignoring Parameter-Count Penalty

**Blocked actions:**
- ❌ Compare χ²_MULTING vs. χ²_ΛCDM without AIC/BIC
- ❌ Claim "lower residual = better model" without complexity penalty
- ❌ Add parameters (Ω_d, Ω_q) without checking if improvement justifies them

**Why blocked:** More parameters always improve fit; must check if improvement is statistically significant.

**Allowed alternative:** Always report AIC, BIC, or Bayes factor alongside χ².

---

## Decision Tree

**MCMC unblocking decision flow:**

```
START: Author response received
    ↓
┌───────────────────────────────────┐
│ Does Buckholtz confirm a bridge?  │
└───────────────────────────────────┘
    ↙ YES                    ↘ NO
    ↓                         ↓
┌─────────────────────┐   ┌──────────────────────────┐
│ Which bridge type?  │   │ Does Buckholtz decline   │
│                     │   │ to provide bridge?       │
└─────────────────────┘   └──────────────────────────┘
    ↓                         ↙ YES          ↘ NO
    ↓                         ↓               ↓
┌─────────────────────────────────┐   ┌─────────────────┐
│ If Hamiltonian:                 │   │ No answer       │
│ → Implement compute_Hz_MULTING  │   │ → Preserve repo │
│    with SOURCE_CONFIRMED status │   │ → Label as      │
│ → Request cluster variables Q17 │   │   reproducibility│
│ → Define priors (physical)      │   │   artifact      │
│ → Integrate Cosmic Chronometers │   │ → Optionally    │
│ → Run MCMC (labeled BUCKHOLTZ)  │   │   develop       │
│ → Compare ΛCDM vs. MULTING      │   │   Hamiltonian   │
│ → Report with AIC/BIC           │   │   as independent│
│                                 │   │   model         │
└─────────────────────────────────┘   └─────────────────┘
    ↓                                     ↓
┌─────────────────────────────────┐   ┌─────────────────┐
│ If Phi-scaling / AI heuristic:  │   │ Do NOT claim    │
│ → Treat as phenomenological     │   │ source          │
│ → Keep Table A1 as retrodiction │   │ confirmation    │
│ → Do NOT claim physics bridge   │   │                 │
│ → Label fits as HEURISTIC_ONLY  │   │                 │
└─────────────────────────────────┘   └─────────────────┘
    ↓
┌─────────────────────────────────┐
│ If Lattice N-body:              │
│ → Request cluster variables Q17 │
│ → Implement N_eff, D_AB(z)      │
│ → More data-heavy than          │
│   Hamiltonian                   │
│ → Consider simulation first     │
└─────────────────────────────────┘
```

**Key decision points:**

1. **Hamiltonian confirmed:**
   - Status: SOURCE_CONFIRMED_BRIDGE
   - Action: Implement full MCMC pipeline
   - Label: MCMC_BUCKHOLTZ_MODEL

2. **Phi-scaling / AI heuristic:**
   - Status: PHENOMENOLOGICAL_HEURISTIC
   - Action: Keep Table A1 as retrodiction only
   - Label: HEURISTIC_FIT_NOT_PHYSICAL_MODEL

3. **Lattice N-body:**
   - Status: PHYSICAL_BUT_DATA_HEAVY
   - Action: Request cluster variables, consider simulation
   - Label: RESEARCH_PATH_HIGH_COMPLEXITY

4. **Buckholtz declines detail:**
   - Status: AUTHOR_DECLINED_BRIDGE_DETAIL
   - Action: Preserve repo as reproducibility artifact
   - Label: PARTIAL_REPRODUCIBILITY_STUDY

5. **No answer:**
   - Status: AUTHOR_NO_RESPONSE
   - Action: Archive or develop Hamiltonian as independent
   - Label: HAMILTONIAN_RECONSTRUCTION_INDEPENDENT

---

## Conservative Final Statement

**Current project state:**

At present, the project is **ready for internal diagnostic testing and author clarification, but not ready for scientific MCMC validation**. 

**What we have accomplished:**
- ✅ Forensic extraction of Appendix A1 computational steps
- ✅ Table A1 transcription and reverse engineering
- ✅ Strong retrodictive evidence (H_MULT 6× closer to H_obs than H_FLRW)
- ✅ Hamiltonian bridge algebraic verification (force → potential → H²)
- ✅ Acceleration interpretation correction (a⁻⁴ can accelerate if Ω_d < 0)
- ✅ Q14-Q18 prepared for author clarification
- ✅ Internal diagnostic fit code ready

**What remains blocked:**
- ❌ Source-confirmed bridge F_oP → H_MULT(z)
- ❌ Cluster variable evolution functions
- ❌ Independent out-of-sample data integration
- ❌ Model complexity penalty implementation
- ❌ MCMC as Buckholtz theory validation
- ❌ Prediction on new redshift
- ❌ Public validation/refutation claim

**The strongest next step is to obtain source confirmation of the F_oP → H_MULT(z) bridge or explicitly proceed with a separately labeled Hamiltonian reconstruction.**

**Two possible paths forward:**

**Path A (Preferred):** Author confirms bridge method
1. Implement `compute_Hz_MULTING` with SOURCE_CONFIRMED status
2. Define priors from physical constraints
3. Integrate independent data (Cosmic Chronometers, Pantheon+, BAO)
4. Run MCMC with complexity penalty (AIC/BIC)
5. Report results as BUCKHOLTZ_MODEL comparison
6. **Timeline:** ~1 week from confirmation to results

**Path B (Fallback):** Author does not confirm or declines detail
1. Document Hamiltonian as INDEPENDENT_RECONSTRUCTION
2. Label all MCMC as HAMILTONIAN_MODEL (not Buckholtz)
3. Optionally develop as standalone alternative to ΛCDM
4. Publish as "reproducibility study + independent reconstruction"
5. Do NOT claim validation/refutation of Buckholtz's work
6. **Timeline:** Indefinite (research project, not audit)

**Either path requires explicit decision — we are currently in waiting state.**

---

## Summary: Four Blockers at a Glance

| Blocker | Missing Component | Impact | Unblock Action |
|---------|------------------|--------|----------------|
| **1. Bridge confirmation** | F_oP → H_MULT(z) rule | Cannot implement compute_Hz_MULTING | Author answers Q15, Q16 |
| **2. Cluster variables** | m_A(z), D_AB(z), N_eff | Cannot predict H(z) at arbitrary z | Author answers Q17 OR authorizes Ω fit |
| **3. Independent data** | Pantheon+, BAO, Cosmic Chronometers | Circular validation on Table A1 | Integrate ≥1 independent dataset |
| **4. Complexity penalty** | AIC/BIC comparison | Cannot justify extra parameters | Implement in MCMC workflow |

**All four must be resolved before scientific MCMC comparison.**

**Current status:** **0/4 blockers resolved** → MCMC remains **BLOCKED**.

---

**Last updated:** 2026-05-29  
**Status:** MCMC_BLOCKED, WAITING_FOR_AUTHOR_RESPONSE  
**Next step:** Wait for author response to first letter, then send Q15-Q17 if appropriate  
**Related docs:** docs/51, docs/53, docs/49, docs/26
