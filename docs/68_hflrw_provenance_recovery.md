# H_FLRW Provenance Recovery

**Date:** 2026-05-29  
**Purpose:** Identify which cosmological baseline reproduces Table A1 H_FLRW column  
**Status:** INTERNAL_DIAGNOSTIC_ONLY  
**Classification:** H_FLRW_PROVENANCE_MISMATCH | NOT_AUTHOR_ERROR | NOT_VALIDATION

---

## Problem Statement

Our independent Table A1 recomputation (docs/66) using assumed Planck-like flat ΛCDM parameters (H0=67.4, Ωm=0.315, ΩΛ=0.685) does not reproduce the reported H_FLRW column.

**Observed mismatch:**
- Max difference: 710.55 km/s/Mpc at z=8.5
- Only 1/12 rows match within 0.1 km/s/Mpc
- 0/12 sigma_FLRW values match

**This is NOT an author error.** It indicates:
1. We used wrong baseline parameters
2. Different FLRW convention was used
3. Different calculator/service was used
4. Paper-specific formula exists but was not recovered

**Goal:** Find which baseline reproduces Table A1 H_FLRW within measurement uncertainty.

---

## Search Results — Existing Documentation

### Files Searched

Searched all docs/, src/, data/, tests/ for:
- H_FLRW
- FLRW
- ΛCDM / Lambda
- H0 / H_0
- Omega_m / Omega_Lambda
- Planck / Riess / WMAP
- Cosmological parameters

**Total files containing these terms:** 82

### Key Findings

| File | Location | Finding | Status |
|------|----------|---------|--------|
| data/table_a1_reported.csv | Header comment line 19 | "H_FLRW: ΛCDM expansion rate (km/s/Mpc)" | FOUND_LABEL_ONLY (no parameters) |
| data/table_a1_reported.csv | Row 1, z=0 | H_FLRW=67.4 at z=0 | FOUND_H0_CANDIDATE |
| docs/28_value_reconciliation_protocol.md | Line 450 | "Using H0 = 67.4 km/s/Mpc (Planck 2018)" | FOUND_ASSUMED_ONLY |
| docs/28_value_reconciliation_protocol.md | Line 452 | "SH0ES gives H0 = 73.0 (Hubble tension)" | FOUND_ALTERNATIVE |
| preprints202511.0598.v6.pdf | Appendix A.3 | Table A1 with H_FLRW column | EXPLICIT_IN_PAPER (no parameters stated) |

### Paper Search (from PDF)

**Searched paper sections:**
- Appendix A.1-A.3 (Steps 1-7)
- Table A1 caption
- Main text cosmology references

**Result:** NO explicit statement of H_FLRW parameters found.

Table A1 caption states:
- β_d = 4.5 (EXPLICIT)
- β_q = 18.0 (EXPLICIT)
- H_FLRW source: NOT STATED
- Ωm source: NOT STATED
- ΩΛ source: NOT STATED

### Provenance Classification

| Parameter | Paper Status | Our Assumption | Evidence Level |
|-----------|-------------|----------------|----------------|
| H0 | NOT_STATED | 67.4 km/s/Mpc | INFERRED (from z=0 row) |
| Ωm | NOT_STATED | 0.315 | ASSUMED_STANDARD (Planck 2018) |
| ΩΛ | NOT_STATED | 0.685 | ASSUMED_STANDARD (Planck 2018) |
| Ωk | NOT_STATED | 0.0 (flat) | ASSUMED_STANDARD |
| Formula | "ΛCDM" stated | Standard Friedmann | ASSUMED_STANDARD |

**Conclusion:** H_FLRW provenance is UNDERSPECIFIED in available documents.

---

## Candidate Cosmology Sweep

### Tested Baselines

We tested 6 standard cosmological baselines against Table A1 H_FLRW column:

1. **Planck-like:** H0=67.4, Ωm=0.315, ΩΛ=0.685 (flat)
2. **SH0ES/Riess-like:** H0=73.0, Ωm=0.3, ΩΛ=0.7 (flat)
3. **WMAP-like:** H0=70.0, Ωm=0.27, ΩΛ=0.73 (flat)
4. **Einstein-de Sitter:** H(z) = H0(1+z)^1.5 (matter-only, Ωm=1)
5. **Linear Hubble:** H(z) = H0(1+z) (diagnostic only, not physical)
6. **Radiation-included:** Ωr=9e-5, Ωm=0.315, ΩΛ=0.685

### Results (Sorted by MAE, Best First)

| Candidate | Parameters | MAE (km/s/Mpc) | RMSE | Max Error | Matches <0.1 | Matches <1.0 |
|-----------|------------|----------------|------|-----------|--------------|--------------|
| Linear Hubble (diagnostic) | H0=67.4, power=1.0 | **59.09** | 90.13 | 241.80 @ z=8.5 | 1/12 | 1/12 |
| WMAP-like | H0=70.0, Ωm=0.27, ΩΛ=0.73 | 103.85 | 213.15 | 668.22 @ z=8.5 | 0/12 | 0/12 |
| Planck-like | H0=67.4, Ωm=0.315, ΩΛ=0.685 | 110.29 | 227.27 | 710.55 @ z=8.5 | 1/12 | 1/12 |
| Radiation-included | H0=67.4, Ωr=9e-5, Ωm=0.315, ΩΛ=0.685 | 110.48 | 227.72 | 712.05 @ z=8.5 | 1/12 | 1/12 |
| SH0ES/Riess | H0=73.0, Ωm=0.3, ΩΛ=0.7 | 125.36 | 248.93 | 773.85 @ z=8.5 | 0/12 | 0/12 |
| Einstein-de Sitter | H0=67.4, Ωm=1.0, ΩΛ=0.0 | 275.37 | 520.45 | 1575.04 @ z=8.5 | 1/12 | 1/12 |

**Full results:** docs/68_hflrw_candidate_sweep.csv

### Key Finding

**NONE of the standard ΛCDM baselines reproduce Table A1 H_FLRW well.**

- Best standard candidate: Linear Hubble (MAE=59 km/s/Mpc) — but this is NOT a physical cosmology
- Best physical ΛCDM: WMAP-like (MAE=104 km/s/Mpc) — still very poor
- Planck-like (our original assumption): MAE=110 km/s/Mpc

**Interpretation:** Table A1 H_FLRW column does NOT appear to be standard flat ΛCDM with any commonly-used parameter set.

---

## Reverse-Fit Diagnostic

### Model 1: Flat ΛCDM with Free Ωm (H0=67.4 fixed)

Formula:
```
H(z) = H0 * sqrt(Ωm * (1+z)^3 + (1 - Ωm))
```

Fit to Table A1 H_FLRW (rows 1-12):

**Best-fit parameters:**
- H0 = 67.4 km/s/Mpc (fixed, from z=0 row)
- Ωm = 0.048
- ΩΛ = 0.952 (implied)

**Fit quality:**
- MAE = 18.49 km/s/Mpc
- RMSE = 24.93 km/s/Mpc
- Max error = 44.51 km/s/Mpc

**Physical plausibility:**
- ❌ **NOT PLAUSIBLE**
- Ωm = 0.048 is far below observational constraints (Planck: Ωm ≈ 0.31)
- ΩΛ = 0.952 is unrealistically high
- This fit is mathematically valid but cosmologically implausible

**Interpretation:** Even with free Ωm, flat ΛCDM cannot physically reproduce Table A1 H_FLRW.

**Labels:** INTERNAL_DIAGNOSTIC_ONLY | NOT_SOURCE_CONFIRMED | NOT_PHYSICALLY_PLAUSIBLE

---

### Model 2: Power Law H(z) = A(1+z)^p ⭐

**Best-fit parameters:**
- A = 55.10 km/s/Mpc
- p = 0.8744

**Fit quality:**
- **MAE = 5.82 km/s/Mpc** ⭐ (BEST FIT)
- **RMSE = 6.71 km/s/Mpc**
- **Max error = 12.30 km/s/Mpc**

**Physical interpretation:**
- p = 0.87 is **between linear (p=1.0) and matter-dominated (p=1.5)**
- This is NOT a standard cosmology power index
- For comparison:
  - p ≈ 1.0 → linear Hubble (non-physical)
  - p ≈ 1.5 → matter-dominated (EdS)
  - p ≈ 2.0 → radiation-dominated
  - **p ≈ 0.87 → unknown / non-standard regime**

**Key Finding:**
This power law reproduces Table A1 H_FLRW **much better than any standard ΛCDM** (5.82 vs 59+ km/s/Mpc MAE).

**Possible explanations:**
1. H_FLRW column is NOT from standard ΛCDM
2. H_FLRW is from a modified gravity theory with different expansion rate
3. H_FLRW is from a non-standard calculator/approximation
4. H_FLRW is phenomenological, not theory-derived

**Labels:** DIAGNOSTIC_ONLY | NOT_STANDARD_COSMOLOGY | PHENOMENOLOGICAL_FIT | BEST_NUMERICAL_FIT

---

### Summary of Reverse-Fit Results

| Model | MAE (km/s/Mpc) | Physical? | Cosmological? |
|-------|----------------|-----------|---------------|
| **Power law (p=0.87)** | **5.82** ⭐ | ❌ Non-standard | ❌ Unknown regime |
| Free Ωm flat ΛCDM | 18.49 | ❌ Ωm=0.048 unphysical | ❌ Violates observations |
| Linear Hubble | 59.09 | ❌ Not physical | ❌ Diagnostic only |
| WMAP-like ΛCDM | 103.85 | ✅ Physical | ✅ Standard |
| Planck-like ΛCDM | 110.29 | ✅ Physical | ✅ Standard |

**Conclusion:** Table A1 H_FLRW is best fit by a non-standard power law with p≈0.87, NOT by any standard flat ΛCDM cosmology.

---

## Meeting-Safe Question

**Context:** For future author communication (NOT an email, meeting-only).

**Wording:**

> "I attempted to independently reproduce the H_FLRW column in Table A1 using a standard flat ΛCDM baseline, but my reconstruction does not match the reported values. I assume I may be using the wrong baseline parameters, convention, or formula.
>
> Could you clarify which H_FLRW convention or parameter set was used for Table A1? Specifically:
>
> 1. What H0 value was used?
> 2. What Ωm and ΩΛ values were used?
> 3. Was the cosmology flat (Ωk=0)?
> 4. Which calculator or service generated the H_FLRW column?
>
> This would allow independent verification of the table."

**Tone:** Respectful, assumes WE made the wrong assumption, not author error.

**Labels:** MEETING_ONLY | NOT_EMAIL | AUTHOR_CLARIFICATION_REQUEST | NOT_CRITICISM

---

## Summary

**Provenance status:** UNDERSPECIFIED

**Next steps:**
1. ✅ Run candidate cosmology sweep
2. ✅ Run reverse-fit diagnostics
3. ⏸️ Wait for author response (if meeting happens)
4. ⏸️ If author provides parameters → rerun recomputation
5. ⏸️ If no response → document as unresolved provenance

**Scientific impact:**
- Does NOT invalidate Table A1
- Does NOT invalidate MULTING
- Identifies reproducibility gap that author can close

**Status:** INTERNAL_DIAGNOSTIC_COMPLETE | AUTHOR_CLARIFICATION_PENDING

---

**Last updated:** 2026-05-29  
**Related docs:**
- docs/66_table_a1_recomputation_report.md
- docs/65_private_artifact_plan_table_a1_recomputation.md
- docs/26_author_clarification_brief.md (add as Q20)
