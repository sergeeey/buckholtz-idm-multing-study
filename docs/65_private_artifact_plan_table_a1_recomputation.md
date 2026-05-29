# Private Artifact Plan: Independent Table A1 Recomputation

**Artifact Name:** Independent Table A1 Recomputation with Anchor-Row Diagnostic  
**Status:** PLAN_ONLY — NOT_IMPLEMENTED  
**Created:** 2026-05-29  
**Implementation:** REQUIRES_USER_APPROVAL

**Safety Labels:**
```
INTERNAL_CONTRIBUTION_DRAFT
NOT_SENT
NOT_VALIDATION
NOT_REFUTATION
AUTHOR_CONFIRMATION_REQUIRED
PROVISIONAL_AUTHOR_DEPENDENT
```

---

## Purpose

Recompute Table A1 arithmetic independently and identify whether Row 1 (z=0) follows a different convention or anchor treatment.

**This is NOT:**
- A validation of MULTING theory
- A refutation of author's method
- A claim of author error
- A public artifact (unless author approves)

**This IS:**
- Pure arithmetic verification
- Baseline for future sensitivity work
- Diagnostic for anchor-row treatment
- Respectful contribution if author finds it useful

---

## Inputs Needed

### From Table A1 (Appendix A1)
- z values (12 rows: 0, 0.070, 0.100, ..., 2.340)
- H_obs ± σ_obs values (12 rows)
- H_FLRW values (12 rows)
- H_MULT values (12 rows)

### From Paper Parameters
- β_d = 4.5 (assumed from context)
- β_q = 18.0 (assumed from context)
- H0, Ω_m, Ω_Λ (for H_FLRW computation, if not directly given)
- Any explicit FLRW cosmology specification

### Assumptions to Document
- Which H_FLRW formula is used (standard flat ΛCDM assumed?)
- What sigma convention is used (absolute vs fractional)
- Whether Row 1 z=0 is treated as anchor vs data point
- What H_obs source catalog is used for each row

---

## What to Compute

### Step 1: Recompute Residuals

For each row i ∈ {1..12}:

1. **H_FLRW residual:**
   ```
   R_FLRW[i] = H_obs[i] - H_FLRW[i]
   ```

2. **H_MULT residual:**
   ```
   R_MULT[i] = H_obs[i] - H_MULT[i]
   ```

3. **Check against reported values** (if residuals are shown in table)

### Step 2: Recompute Normalized Sigma Values

Assuming standard convention:
```
σ_normalized[i] = R[i] / σ_obs[i]
```

For both FLRW and MULT models.

### Step 3: Compare Reported vs Recomputed

Create comparison table:
```
z | H_obs | H_FLRW_reported | H_FLRW_recomputed | H_MULT_reported | H_MULT_recomputed
```

Flag any discrepancies > 0.1 km/s/Mpc.

### Step 4: Row 1 (z=0) Special Treatment

Test three hypotheses for Row 1:

**Hypothesis A: Standard Convention**
- Treat Row 1 same as all other rows
- Compute residual normally
- Compare with reported value

**Hypothesis B: Anchor-Row (0 by definition)**
- Row 1 residual defined as 0
- H_MULT[1] = H_obs[1] by construction
- Check if this matches reported value

**Hypothesis C: Alternate Sigma Convention**
- Row 1 uses different normalization
- Test: σ[1] = absolute error vs fractional error
- Check which matches reported value

**Output:** Which hypothesis best matches reported Row 1 values

### Step 5: Document All Assumptions

Create explicit list:
```
ASSUMPTION_1: H_FLRW uses flat ΛCDM with [H0, Ω_m, Ω_Λ]
ASSUMPTION_2: Sigma convention is [absolute / fractional / other]
ASSUMPTION_3: Row 1 treatment is [standard / anchor / special]
ASSUMPTION_4: β values are [4.5, 18.0] from [source]
ASSUMPTION_5: [any other inference we make]
```

**Critical:** Label each assumption as:
- `[EXPLICIT_IN_PAPER]` — directly stated
- `[INFERRED_FROM_CONTEXT]` — reasonable inference
- `[ASSUMED_STANDARD]` — standard practice assumption
- `[UNKNOWN_GUESSED]` — pure guess, high risk

---

## Output Deliverables

### 1. CSV Comparison Table
```csv
z,H_obs,sigma_obs,H_FLRW_reported,H_FLRW_recomputed,H_MULT_reported,H_MULT_recomputed,residual_FLRW_reported,residual_FLRW_recomputed,residual_MULT_reported,residual_MULT_recomputed
0.000,73.8,2.4,73.8,73.8,73.8,73.8,0.0,0.0,0.0,0.0
0.070,69.0,19.6,...
```

### 2. Short Markdown Report

**Structure:**
```markdown
# Table A1 Independent Recomputation

## Summary
- X/12 rows match exactly
- Y/12 rows differ by <0.5 km/s/Mpc
- Z/12 rows differ by >0.5 km/s/Mpc

## Row 1 (z=0) Diagnostic
- Hypothesis A (standard): [result]
- Hypothesis B (anchor): [result]
- Hypothesis C (alternate sigma): [result]
- Best match: [which hypothesis]

## Discrepancies
[List any rows with >0.1 difference]

## Assumptions Used
[Full list with evidence labels]

## Interpretation
[NONE — pure arithmetic report, no physics claims]
```

### 3. Explicit Assumptions List

Separate file: `table_a1_recomputation_assumptions.md`

Format:
```
ASSUMPTION: [statement]
EVIDENCE: [EXPLICIT_IN_PAPER | INFERRED | ASSUMED | GUESSED]
SOURCE: [paper section / equation / figure]
CONFIDENCE: [HIGH | MEDIUM | LOW]
ALTERNATIVE: [what else it could be]
```

---

## Implementation Steps (When Approved)

### Phase 1: Data Extraction
1. Read Table A1 from PDF/appendix
2. Extract all values into structured CSV
3. Cross-check transcription (manual + OCR)
4. Document any ambiguities

### Phase 2: Assumption Inference
1. Search paper for H_FLRW specification
2. Search for sigma convention statement
3. Search for Row 1 treatment statement
4. Document what's explicit vs inferred

### Phase 3: Computation
1. Implement H_FLRW(z) function
2. Compute all residuals
3. Test Row 1 hypotheses A/B/C
4. Generate comparison tables

### Phase 4: Verification
1. Spot-check 3 random rows manually
2. Check edge cases (z=0, z=max)
3. Compare against reported values
4. Document any discrepancies

### Phase 5: Report Generation
1. Write markdown summary
2. Generate CSV output
3. Create assumptions list
4. Package as single artifact

---

## Safety Checks

Before considering this artifact complete:

### ✅ Arithmetic Verification
- [ ] All computations independently verified
- [ ] Spot-checks match hand calculations
- [ ] No phantom sources (all inputs cited)
- [ ] Edge cases tested (z=0, z→∞)

### ✅ Neutral Framing
- [ ] No claim of author error
- [ ] No claim of theory validation
- [ ] Row 1 described neutrally
- [ ] Discrepancies reported without judgment

### ✅ Assumption Transparency
- [ ] Every assumption labeled with evidence level
- [ ] Alternatives documented where uncertain
- [ ] Unknown unknowns acknowledged
- [ ] No hidden inferences

### ✅ Respectful Tone
- [ ] No condescending language
- [ ] Focus on "what we computed" not "what author did wrong"
- [ ] Acknowledge author's expertise
- [ ] Offer as optional resource, not correction

---

## Success Criteria

**Artifact succeeds if:**

1. **Reproducibility established**  
   - Someone else can replicate our computation
   - All inputs are traceable
   - All assumptions are explicit

2. **Row 1 diagnostic clarifies treatment**  
   - Clear answer about anchor vs standard convention
   - Non-obvious pattern identified (if any)
   - Useful regardless of which hypothesis is correct

3. **Baseline for future work**  
   - Enables β sensitivity analysis
   - Enables H_MULT algorithm recovery
   - Enables independent fit attempts

4. **No relationship damage**  
   - Author finds it useful (if shared)
   - Not perceived as attack
   - Respectful contribution framing

---

## Failure Modes

**What could go wrong:**

### 1. Wrong Sigma Convention
**Symptom:** All residuals off by factor of ~10  
**Mitigation:** Test both absolute and fractional conventions  
**Recovery:** Document which convention we used, offer both

### 2. Missing H_FLRW Inputs
**Symptom:** Cannot reproduce H_FLRW column at all  
**Mitigation:** Search paper exhaustively for cosmology spec  
**Recovery:** Report "H_FLRW not reproducible with available info"

### 3. Row 1 Misidentified
**Symptom:** Row 1 interpretation doesn't match any hypothesis  
**Mitigation:** Test A/B/C explicitly, report all results  
**Recovery:** Report "Row 1 treatment unclear, here are results under each hypothesis"

### 4. Overclaiming
**Symptom:** Report sounds like "author made arithmetic error"  
**Mitigation:** Peer review framing before finalizing  
**Recovery:** Rewrite to neutral: "our computation differs, possible reasons: [list]"

### 5. Unintentional Public Formula
**Symptom:** We reconstruct H_MULT(z) and call it "Buckholtz's method"  
**Mitigation:** Use neutral names, don't claim to know author's intent  
**Recovery:** Rename to "candidate expansion rate function"

---

## Next Steps

1. ✅ This plan created
2. ⏸️ Wait for user approval
3. ⏸️ If approved: implement Phase 1 (data extraction)
4. ⏸️ Checkpoint after each phase
5. ⏸️ Final artifact review before marking complete

**Do NOT implement without explicit user approval.**

---

**Last updated:** 2026-05-29  
**Status:** PLAN_READY, AWAITING_APPROVAL  
**Estimated effort:** 2-3 hours (if all inputs available)
