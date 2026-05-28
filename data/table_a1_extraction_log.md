# Table A1 Extraction Log

**Purpose:** Document extraction of Table A1 from manuscript `preprints202511.0598.v6.pdf`, Appendix A.3.

**Status:** TEMPLATE — awaiting manual transcription by user (PDF not available to Claude Code)

**Created:** 2026-05-27  
**Last updated:** 2026-05-27

---

## 1. Source Document

| Field | Value |
|-------|-------|
| **Manuscript ID** | preprints202511.0598.v6.pdf |
| **Appendix section** | Appendix A.3 |
| **Table number** | Table A1 |
| **Page number** | (to be filled) |
| **Table caption** | (to be filled) |

---

## 2. Extraction Method

**Method:** Manual transcription from PDF

**Why manual:**
- PDF not available to Claude Code in local repository
- Manual verification completed by user (2026-05-27) confirmed beta_d=4.5, beta_q=18.0
- Table transcription requires visual access to manuscript

**Tools used:**
- PDF viewer: (Adobe Acrobat / browser / other)
- Data entry: (Excel / manual CSV editing / other)

---

## 3. Table Structure (from manuscript)

**Column names (exact from manuscript):**

| Column # | Name (from manuscript) | Provisional name (if unclear) | Units | Data type |
|----------|------------------------|-------------------------------|-------|-----------|
| 1 | (to be filled) | z | dimensionless | float |
| 2 | (to be filled) | time_after_big_bang_gyr | Gyr | float |
| 3 | (to be filled) | H_obs | km/s/Mpc | float |
| 4 | (to be filled) | H_obs_uncertainty | km/s/Mpc | float |
| 5 | (to be filled) | H_FLRW | km/s/Mpc | float |
| 6 | (to be filled) | H_MULT | km/s/Mpc | float |
| 7 | (to be filled) | sigma_MULT | (units to be determined) | float |
| 8+ | (if exist) | other_columns | (to be determined) | (to be determined) |

**Row count:** (to be filled after extraction)

**Notes on column structure:**
- z = redshift (standard cosmology parameter)
- time_after_big_bang = cosmic time since Big Bang
- H_obs = observed Hubble parameter (if listed)
- H_FLRW = ΛCDM expansion rate (standard model)
- H_MULT = IDM/MULTING expansion rate (fitted with beta_d=4.5, beta_q=18.0)
- sigma_MULT = fit quality metric (definition unclear, see docs/18)

---

## 4. Verified Manuscript Information

**From manual verification (completed 2026-05-27):**

**Exact quote from manuscript:**
> "Regarding H-MULT, the online service reported choosing beta_d = 4.5 and beta_q = 18.0."

**Context:**
- AI-assisted thought experiment
- LLM instructed to choose positive beta_d and beta_q values
- Objective: minimize standard-deviations away from observed H(z)
- Beta values are **fitted phenomenological parameters** (NOT derived)
- No uncertainty intervals provided for beta_d or beta_q
- Quality of fit reported through sigma_MULT

**Beta values:**
- beta_d = 4.5 (dimensionless, fitted)
- beta_q = 18.0 (dimensionless, fitted)

---

## 5. Extraction Procedure (to be executed by user)

### Step 1: Open manuscript
- [ ] Open `preprints202511.0598.v6.pdf`
- [ ] Navigate to Appendix A.3
- [ ] Locate Table A1
- [ ] Record page number: __________

### Step 2: Record table metadata
- [ ] Copy table caption exactly: __________
- [ ] Count total rows (excluding header): __________
- [ ] Count total columns: __________
- [ ] Record exact column names from manuscript: __________

### Step 3: Transcribe data
- [ ] Create CSV file: `data/table_a1_raw.csv`
- [ ] First row = column headers (exact from manuscript)
- [ ] Subsequent rows = data values
- [ ] Use consistent decimal separator (period, not comma)
- [ ] Preserve exact numerical precision from manuscript
- [ ] If value is missing/unclear, use: `NA`

### Step 4: Validation checks
- [ ] All rows have same number of columns
- [ ] No stray commas or quotes
- [ ] Numeric columns parse without errors
- [ ] z values are monotonic (increasing or decreasing)
- [ ] No duplicate z values (unless intentional)

### Step 5: Document uncertainties
- [ ] Were H(z) uncertainties listed? YES / NO
- [ ] Were beta uncertainties listed? YES / NO
- [ ] Were other uncertainties listed? __________

### Step 6: Cross-check
- [ ] Spot-check 3 random rows against manuscript
- [ ] Verify beta_d=4.5 appears in table context
- [ ] Verify beta_q=18.0 appears in table context
- [ ] Verify H_MULT column exists

---

## 6. Known Issues / Challenges

**Potential issues to watch for:**

1. **Column name ambiguity**
   - If manuscript uses non-standard abbreviations
   - If units are unclear (e.g., H₀ normalization)
   - → Document in "notes" column

2. **Missing values**
   - If some rows lack H_obs (not all z have direct observations)
   - If sigma_MULT is not computed for all rows
   - → Use `NA` consistently

3. **Numerical precision**
   - Manuscript may round values for display
   - Balance: preserve manuscript precision vs avoid false precision
   - → Use same number of decimal places as manuscript

4. **Units consistency**
   - H(z) typically in km/s/Mpc
   - Time typically in Gyr
   - Check manuscript units explicitly

5. **Footnotes / special markers**
   - If table has footnotes or asterisks
   - → Record in separate "notes" field

---

## 7. Data Quality Checklist (post-extraction)

After transcription, verify:

- [ ] **Completeness:** All visible rows transcribed
- [ ] **Accuracy:** Spot-check ≥3 random rows against manuscript
- [ ] **Consistency:** All numeric columns parse as float
- [ ] **Monotonicity:** z values increase/decrease consistently
- [ ] **Range sanity:**
  - z values: 0 ≤ z ≤ ? (cosmological range)
  - time values: 0 < t < 13.8 Gyr (age of universe)
  - H values: > 0 (expansion rate positive)
  - sigma_MULT: ≥ 0 (deviation metric non-negative)

---

## 8. Expected Output Files

After extraction complete:

1. **`data/table_a1_raw.csv`**
   - Row 1: column headers (exact from manuscript)
   - Rows 2+: data values
   - Format: standard CSV (comma-separated, UTF-8)

2. **`data/table_a1_extraction_log.md`** (this file)
   - Updated with actual extraction details
   - Checkboxes marked as completed
   - Issues documented

3. **`tests/test_table_a1_extraction.py`** (optional, recommended)
   - Validate CSV structure
   - Check numeric parsing
   - Verify z monotonicity
   - Check for missing values

---

## 9. Post-Extraction Next Steps

Once `table_a1_raw.csv` is created:

### DO NOT do yet (blocked):
- ❌ Compute new H_MULT values (H-MULT formula missing)
- ❌ Fit beta values (already fitted, dataset source unclear)
- ❌ Validate MULTING (circular reasoning: beta fitted to H(z))
- ❌ Make predictions (use_permission = fit_reproduction_only)

### CAN do (allowed):
- ✅ Load CSV into Python for inspection
- ✅ Plot H_FLRW vs H_MULT vs z (visual comparison)
- ✅ Verify beta_d=4.5, beta_q=18.0 appear in table context
- ✅ Compute basic statistics (mean, std, range)
- ✅ Compare H_MULT with H_FLRW (residuals analysis)
- ✅ Document sigma_MULT values (infer definition)

### Questions to answer from extracted data:
1. What is the redshift range? (z_min, z_max)
2. How many H(z) data points? (row count)
3. Are H_obs and H_obs_uncertainty listed? (check columns)
4. What are typical sigma_MULT values? (distribution)
5. How does H_MULT compare with H_FLRW? (mean difference, RMS)

---

## 10. Integration with Repository

**Provenance reference:**
- `src/beta_provenance.py` — beta_d_A1, beta_q_A1 records
- `docs/18_fit_reproduction_requirements.md` — fit reproduction spec
- `docs/17_table_A1_manual_verification_protocol.md` — verification completed

**Next files to create (after CSV ready):**
- `src/table_a1_loader.py` — load CSV into pandas DataFrame
- `tests/test_table_a1_extraction.py` — validation tests
- `notebooks/01_table_a1_exploration.ipynb` — exploratory analysis

---

## 11. Extraction Status

**Status:** ⏸️ AWAITING USER ACTION

**Blocker:** PDF `preprints202511.0598.v6.pdf` not available to Claude Code

**Required:** User must manually transcribe Table A1 from manuscript PDF

**Template created:** `data/table_a1_raw.csv` (headers only, awaiting data)

**When ready:** User updates this log + fills CSV → tests can be run

---

**Last updated:** 2026-05-27  
**Extractor:** (user to fill)  
**Extraction time:** (user to fill)  
**Verification:** (user to mark checkboxes above)
