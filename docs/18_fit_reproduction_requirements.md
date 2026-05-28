# Fit Reproduction Requirements — Table A1 H-MULT

**Purpose:** Define requirements for reproducing the Table A1 H-MULT fit reported in manuscript `preprints202511.0598.v6.pdf`, Appendix A.3.

**Status:** Planning phase — fit reproduction is ALLOWED, predictive modeling remains BLOCKED.

**Created:** 2026-05-27  
**Verification status:** Manual verification complete (beta values confirmed from manuscript)

---

## 1. Verified Fitted Beta Values

**Source:** `preprints202511.0598.v6.pdf`, Appendix A.3, Table A1

**Exact manuscript quote:**

> "Regarding H-MULT, the online service reported choosing beta_d = 4.5 and beta_q = 18.0."

**Context from manuscript:**
- AI-assisted thought experiment
- LLM was instructed to choose positive beta_d and beta_q values that minimize standard-deviations away from observed H(z)
- Beta values are **fitted phenomenological parameters**, NOT derived theoretical constants
- No uncertainty intervals provided for beta_d or beta_q
- Quality of fit reported through sigma_MULT (not χ²/dof)
- Observed H(z) data include uncertainties
- Beta values are dimensionless scaling factors (e.g., r_dA = beta_d × r_A)

**Provenance status (from beta_provenance.py):**
- `provenance_status`: `manuscript_reported_fitted`
- `derivation_status`: `fitted_not_derived`
- `use_permission_status`: `allowed_for_fit_reproduction_only`
- `manual_verification_status`: `manually_verified`
- `manuscript_identifier`: `preprints202511.0598.v6.pdf`

---

## 2. Scope — What is Allowed

✅ **Allowed actions:**

1. **Reproduce Table A1 fit numerically**
   - Use beta_d = 4.5 and beta_q = 18.0 as given constants
   - Compute H_MULT(z) on same dataset used by Buckholtz
   - Reproduce sigma_MULT if sufficient information available

2. **Compare fit quality with ΛCDM** on SAME dataset
   - Fair comparison: both models fitted to same data
   - Report χ²/dof or sigma for both models
   - Document: "Both models fitted to this dataset"

3. **Extract Table A1 data for analysis**
   - z values, H(z) observations, uncertainties
   - H_FLRW, H_MULT, sigma_MULT columns
   - Convert to machine-readable format (CSV)

4. **Verify internal consistency**
   - Check if Table A1 H_MULT values match H-MULT formula (when formula provided)
   - Verify sigma_MULT calculation (if definition provided)
   - Document any discrepancies

❌ **NOT allowed actions:**

1. **Predictive H(z) claims**
   - Cannot claim to "predict" H(z) on new redshift ranges
   - Cannot claim to "validate" MULTING with H(z) (circular: fitted to H(z))
   - Cannot use beta_d, beta_q for zero-parameter predictions

2. **Causal claims**
   - Cannot claim beta values "cause" expansion
   - Cannot claim fit quality proves MULTING mechanism correct
   - Fit quality ≠ physical truth (many models can fit same data)

3. **Independent dataset validation**
   - BLOCKED until beta values derived (not fitted) OR new beta values fitted to new dataset
   - CMB, BAO, lensing predictions require theoretical derivation, not phenomenological fit

---

## 3. Required Data and Information

| Requirement | Available? | Source | Status | Notes |
|---|---:|---|---|---|
| **H(z) observations** | ❓ | Table A1 | PARTIAL | Table exists, but extraction needed |
| **H(z) uncertainties** | ❓ | Table A1 | PARTIAL | Manuscript states "uncertainties included" |
| **z (redshift values)** | ❓ | Table A1 | PARTIAL | Listed in table |
| **Time after Big Bang** | ❓ | Table A1 | PARTIAL | Listed in table |
| **H_FLRW (ΛCDM)** | ❓ | Table A1 | PARTIAL | Listed in table |
| **H_MULT (IDM/MULTING)** | ❓ | Table A1 | PARTIAL | Listed in table |
| **sigma_MULT** | ❓ | Table A1 | PARTIAL | Listed in table |
| **Exact H-MULT formula** | ❌ | Unknown | **MISSING** | **BLOCKER** — functional form not in manuscript |
| **m_A (monopole mass)** | ❓ | Manuscript | UNCLEAR | Definition needed |
| **r_A (monopole length)** | ❓ | Manuscript | UNCLEAR | Definition needed |
| **k_A (monopole constant)** | ❓ | Manuscript | UNCLEAR | Definition needed |
| **D_C:AB (comoving distance)** | ❓ | Manuscript | UNCLEAR | Definition needed |
| **beta_d** | ✅ | Table A1 | **VERIFIED** | beta_d = 4.5 (dimensionless, fitted) |
| **beta_q** | ✅ | Table A1 | **VERIFIED** | beta_q = 18.0 (dimensionless, fitted) |
| **beta uncertainties** | ❌ | Table A1 | **MISSING** | No error bars provided |
| **Objective function** | ❓ | Manuscript | PARTIAL | "minimize standard-deviations away from observed H(z)" |
| **AI service identity** | ❓ | Manuscript | PARTIAL | "online service" — which one? |
| **AI service version** | ❌ | Unknown | **MISSING** | Reproducibility issue |
| **AI service prompt** | ❌ | Unknown | **MISSING** | Reproducibility issue |
| **Dataset source** | ❌ | Unknown | **MISSING** | Which H(z) observations? Cosmic chronometers? BAO? |
| **Fitting procedure** | ❌ | Unknown | **MISSING** | Grid search? Gradient descent? |
| **Convergence criteria** | ❌ | Unknown | **MISSING** | When did AI stop fitting? |

**Legend:**
- ✅ VERIFIED — manually confirmed from manuscript
- ❓ PARTIAL — mentioned but not fully specified
- ❌ MISSING — not available, blocks reproduction

---

## 4. Critical Blocking Gaps

### Gap 1: Exact H-MULT Functional Form (HIGHEST PRIORITY)

**Problem:** Manuscript does not provide explicit formula for H_MULT(z; beta_d, beta_q).

**Required information:**
- H_MULT = f(z, beta_d, beta_q, other_params?)
- Monopole contribution H_monopole(z)
- Dipole contribution H_dipole(z, beta_d)
- Quadrupole contribution H_quadrupole(z, beta_q)
- How terms combine (additive? multiplicative?)

**Without this:** Cannot reproduce Table A1 H_MULT column numerically.

**Resolution path:** Request explicit H-MULT formula from Dr. Buckholtz (see docs/12_beta_clarification_brief.md, Secondary Question).

### Gap 2: Dataset Source and Extraction

**Problem:** Table A1 does not cite which H(z) dataset was used.

**Possible sources:**
- Cosmic chronometers (differential age method)
- BAO measurements (angular diameter distance)
- Hybrid dataset
- Custom compilation

**Required:**
- z values (exact)
- H(z) values (exact)
- H(z) uncertainties (exact)
- Dataset citations

**Resolution path:** Extract from Table A1 OR request dataset file from Dr. Buckholtz.

### Gap 3: Beta Uncertainties

**Problem:** Beta values reported as point estimates (4.5, 18.0) without error bars.

**Impact:**
- Cannot assess fit stability
- Cannot propagate uncertainty to H_MULT predictions
- Cannot compare with alternative beta values

**Resolution path:** Request uncertainty estimates OR re-fit beta on extracted dataset with uncertainty quantification.

### Gap 4: AI Service Details (Reproducibility)

**Problem:** "Online service" identity unknown.

**Reproducibility issues:**
- Which AI model? (GPT-4, Claude, LLaMA?)
- Which version?
- What prompt exactly?
- What objective function implementation?
- Deterministic or stochastic optimization?

**Resolution path:** Request AI service details from Dr. Buckholtz OR ignore AI aspect and re-implement fit manually.

### Gap 5: sigma_MULT Definition

**Problem:** Manuscript reports sigma_MULT but does not define formula.

**Possible definitions:**
- RMS deviation: sqrt(mean((H_obs - H_MULT)²))
- Normalized chi-squared: sqrt(sum(((H_obs - H_MULT)/σ_obs)²) / N)
- Standard deviations away: max(|H_obs - H_MULT| / σ_obs)
- Other metric

**Resolution path:** Request sigma_MULT formula OR infer from Table A1 values.

---

## 5. Next Valid Computational Task

**Task:** Extract Table A1 into machine-readable format (CSV).

**Why this is valid:**
- Does NOT involve new physics calculations
- Does NOT make predictions
- Simply prepares manuscript data for analysis
- Prerequisite for fit reproduction

**Steps:**
1. Manually transcribe Table A1 from manuscript PDF
2. Create `data/table_a1_raw.csv` with columns:
   - z (redshift)
   - time_after_big_bang (units?)
   - H_FLRW (ΛCDM expansion rate)
   - H_MULT (IDM/MULTING expansion rate)
   - sigma_MULT (fit quality metric)
   - H_obs (if listed)
   - H_obs_uncertainty (if listed)
3. Validate: row count, column count, no missing values
4. Document: manuscript page, table caption, any notes

**Output:** `data/table_a1_raw.csv` + `data/table_a1_extraction_log.md`

**Do NOT yet:**
- Compute new H_MULT values (formula missing)
- Fit beta values (dataset source unclear)
- Validate MULTING (circular reasoning)

---

## 6. Fit Reproduction Checklist

| Step | Action | Status | Blocker |
|---:|---|---:|---|
| 0 | Manual verification of beta values | ✅ DONE | — |
| 1 | Extract Table A1 to CSV | ⏸️ READY | None |
| 2 | Request H-MULT functional form from Buckholtz | ⏸️ READY | None |
| 3 | Request dataset source / citations | ⏸️ READY | None |
| 4 | Implement H_MULT(z; beta_d, beta_q) | ❌ BLOCKED | Gap 1 (formula missing) |
| 5 | Load H(z) observations with uncertainties | ❌ BLOCKED | Gap 2 (dataset unclear) |
| 6 | Reproduce Table A1 H_MULT column | ❌ BLOCKED | Steps 4, 5 |
| 7 | Compute sigma_MULT | ❌ BLOCKED | Gap 5 (definition missing) |
| 8 | Compare with manuscript Table A1 values | ❌ BLOCKED | Step 6 |
| 9 | Implement ΛCDM H_FLRW(z) for comparison | ⏸️ READY | None (standard formula) |
| 10 | Compute χ²_MULT and χ²_ΛCDM on same data | ❌ BLOCKED | Steps 5, 6 |
| 11 | Document fit quality comparison | ❌ BLOCKED | Step 10 |
| 12 | Mark fit reproduction as COMPLETE | ❌ BLOCKED | Steps 1-11 |

**Legend:**
- ✅ DONE — completed
- ⏸️ READY — can proceed, no blockers
- ❌ BLOCKED — cannot proceed, dependency missing

---

## 7. Fit Quality Metrics (to be computed)

Once fit is reproduced, compute and report:

| Metric | MULTING | ΛCDM | Interpretation |
|--------|---------|------|----------------|
| χ² | ? | ? | Goodness of fit |
| χ²/dof | ? | ? | Normalized fit quality |
| AIC | ? | ? | Akaike Information Criterion (penalizes extra parameters) |
| BIC | ? | ? | Bayesian Information Criterion (stronger penalty) |
| RMSE | ? | ? | Root mean squared error |
| sigma_MULT | ? | N/A | Manuscript's metric (if definition available) |

**Critical:**
- **AIC/BIC comparison** — MULTING has 2 extra parameters (beta_d, beta_q) vs ΛCDM
- If χ²_MULT ≈ χ²_ΛCDM but AIC_MULT > AIC_ΛCDM → MULTING overfits
- Fit quality alone does NOT validate physical mechanism

---

## 8. Circular Reasoning Guard (Reminder)

**CRITICAL CONSTRAINT (from beta_provenance.py):**

Beta values were **fitted to H(z) observations**.

Therefore:
- ✅ Can reproduce the fit on the SAME dataset
- ✅ Can compare fit quality with ΛCDM on SAME dataset
- ❌ **CANNOT** use this fit to "validate" MULTING
- ❌ **CANNOT** claim to "predict" H(z) (already fitted to H(z))
- ❌ **CANNOT** generalize to new redshift ranges without independent verification

**Analogy:**
```
Fitting polynomial to data points → can reproduce curve.
BUT: This does NOT prove polynomial is "correct" physics.
      Many functions fit same data.
```

**To break circular reasoning (future work):**
1. Derive beta_d, beta_q from first principles (NOT fitting) → then predict H(z)
2. OR fit beta on training set → predict on held-out test set
3. OR make independent predictions (CMB, BAO, lensing) BEFORE testing

**Current status:** Only reproduction (retrodiction) is allowed, NOT prediction.

---

## 9. Integration with Existing Repository

**Files to reference:**
- `src/beta_provenance.py` — beta_d_A1, beta_q_A1 provenance records
- `tests/test_beta_provenance.py` — tests enforce `allowed_for_fit_reproduction_only`
- `docs/12_beta_clarification_brief.md` — questions for Buckholtz (Secondary Question: H-MULT formula)
- `docs/17_table_a1_manual_verification_protocol.md` — verification completed
- `docs/19_sabine_audit.md` — epistemological audit (circular reasoning identified)

**New files to create (when ready):**
- `data/table_a1_raw.csv` — extracted Table A1 data
- `data/table_a1_extraction_log.md` — extraction notes
- `src/h_mult_fit_reproduction.py` — fit reproduction code (when formula available)
- `tests/test_table_a1_reproduction.py` — verify reproduction matches manuscript

---

## 10. Questions for Dr. Buckholtz (Prioritized)

**Priority 1 (BLOCKER):**
> "Could you provide the explicit functional form for H-MULT(z; beta_d, beta_q)?  
> Specifically:
> - How do monopole, dipole, and quadrupole terms combine?
> - What are the definitions of m_A, r_A, k_A, D_C:AB?
> - Is there a published equation number or supplementary material?"

**Priority 2 (BLOCKER):**
> "Which H(z) dataset was used to fit beta_d and beta_q in Table A1?  
> - Cosmic chronometers?
> - BAO measurements?
> - Custom compilation?
> - Can you share the dataset file or citations?"

**Priority 3 (High):**
> "What is the definition of sigma_MULT reported in Table A1?  
> - RMS deviation?
> - Normalized chi-squared?
> - Maximum standard deviations away?
> - Other metric?"

**Priority 4 (Medium):**
> "What are the uncertainty estimates for beta_d = 4.5 and beta_q = 18.0?  
> - Fitting uncertainties?
> - Confidence intervals?
> - Or reported as point estimates only?"

**Priority 5 (Low, reproducibility):**
> "Which online AI service was used for fitting, and what was the exact prompt?  
> (For reproducibility purposes — we can also re-implement the fit manually.)"

---

## 11. Final Verdict

**Fit reproduction planning:** ✅ **ALLOWED**

**Status:**
- Beta values verified from manuscript
- Provenance correctly marked as `manuscript_reported_fitted`
- Use permission correctly set to `allowed_for_fit_reproduction_only`
- Circular reasoning guard in place
- Extraction task (Table A1 → CSV) ready to proceed

**Predictive modeling:** ❌ **REMAINS BLOCKED**

**Blockers:**
- H-MULT functional form missing (Priority 1 question)
- Dataset source unclear (Priority 2 question)
- Sigma_MULT definition missing (Priority 3 question)

**Next smallest step:**
1. Extract Table A1 from manuscript PDF to CSV (no blockers)
2. Send Priority 1-3 questions to Dr. Buckholtz
3. Wait for responses before implementing H_MULT(z) code

**Repository integrity:** All tests passing (99/99), provenance audit complete, circular reasoning documented.

---

**Document status:** COMPLETE — ready for Table A1 extraction and author clarification.

**Last updated:** 2026-05-27  
**Next review:** After receiving H-MULT formula from Dr. Buckholtz
