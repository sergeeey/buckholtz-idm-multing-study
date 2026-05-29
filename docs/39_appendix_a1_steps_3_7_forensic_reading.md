# Appendix A1 Steps 3–7 — Forensic Close Reading

**Document type:** SOURCE_CONFIRMED — direct extraction from preprints202511.0598.v6.pdf  
**Pages:** 31–38 (Appendix A.1)  
**Date extracted:** 2026-05-29  
**Purpose:** Word-level forensic extraction WITHOUT interpretation or implementation  

---

## Summary of Key Findings

### 1. β_d and β_q Status
**STATUS:** FITTED_PHENOMENOLOGICAL  
**Evidence:** Step 5 explicitly instructs: *"Try to choose positive values for β_d and β_q that minimize the standard-deviations away from the nominal values of observed H(z)."*

Table A1 reports: β_d = 4.5, β_q = 18.0 (AI service output)

### 2. F_oP → H_MULT Bridge Status
**STATUS:** FORMULA_MISSING  
**Evidence:** Step 5 provides scaling relations (r_dA = β_d × r_A) but does NOT provide explicit formula for H_MULT(z, β_d, β_q, m_A, r_A, ...).

Instruction is: *"How well can you fit (by using my monopole, dipole, and quadrupole components of gravity) the data..."* — procedural/heuristic only, NOT computational formula.

### 3. AI Discretion
**STATUS:** AI_DISCRETION_ALLOWED  
**Evidence:**  
- Step 5: *"Feel free to use any or all the information in the Galaxy Cluster Parameters table."*  
- Step 5: *"Explain how you chose or estimated the observed values."*  
- Table A1 caption: *"Responses, to our prompt, by one online service that has bases in artificial intelligence."*

### 4. FLRW Usage
**STATUS:** FORBIDDEN for H-MULT computation, ALLOWED for comparison  
**Evidence:**  
- Step 5: *"Try to avoid using outputs from uses of the FLRW metric or other Lambda-CDM models."*  
- Step 7: Explicit request for w_eff(z) comparison using FLRW

---

## Step 3: Time Range — Forensic Extraction

### Author Instruction (verbatim)
> "Define a so-called 'Set of Times' as follows."

### Variables Introduced
1. **t_ROE,min** — earliest time (billions of years after Big Bang) with Good Data
2. **Set of Times** — specific integer sequence

### Definition of "Good Data"
> *"Anticipate that 'Good Data' should not include information that relies on theoretical models, such as theoretical models of dark-matter halo masses especially."*

### Set of Times Definition
> *"Let t_ROE,min denote the earliest time, in billions of years after the Big Bang, for which there is Good Data about the observed rate of expansion of the universe, the range of masses of protoclusters (as in clusters of proto galaxies, or early galaxies), the range of sizes of protoclusters, the total kinetic energies of sub-objects of protoclusters or galaxy clusters, and typical distances between neighboring non-colliding protoclusters."*

> *"Define a so-called 'Set of Times', which is set of times, in billions of years after the Big Bang, that has as members the number 13.5 and each integer that is less than or equal to 13 and greater than or equal to both t_ROE,min and 1."*

### User Prompt Instructions
- *"Tell me how you choose t_ROE,min."*
- *"Tell me the members of the Set of Times."*

### Status Tags
- **t_ROE,min:** AUTHOR_PROMPT_INSTRUCTION — AI service must choose
- **Set of Times:** DERIVED from t_ROE,min + rule
- **"Good Data" definition:** SOURCE_CONFIRMED — explicit constraint

---

## Step 4: Galaxy Cluster Parameters — Forensic Extraction

### Author Instruction (verbatim)
> *"Provide a table, named 'Galaxy Cluster Parameters', for which there is one row for each member of the Set of Times and you ordered the rows so that times are in descending order and the columns provide the following data about galaxy clusters or protoclusters."*

### Required Columns

| Column | Symbol | Meaning (verbatim from source) | Provenance |
|--------|--------|--------------------------------|------------|
| Time | - | The time | DATA |
| z | z | The redshift z that associates with the time | DERIVED from Time |
| m_A | m_A | A range of masses for, for example object-A | AI_ESTIMATED |
| r_A | r_A | A range of radii for, for example object-A | AI_ESTIMATED |
| D_C:AB | D_C:AB | A range of distances between the centers of neighboring similar objects | AI_ESTIMATED |
| k_A/c² | k_A/c² | A range of k_A/c² for protoclusters or galaxy clusters. Report in units of solar masses. | AI_ESTIMATED |
| H-data | H(z) | The observed rate of expansion of the universe. Show values that associate with data. Do not show values that associate with modeling that has bases in the FLRW metric. Include a nominal value and a standard deviation. | DATA |

### Critical Instruction
> *"Explain how you found, chose, or estimated the values in the table."*

### Status Tags
- **Time, z, H-data:** DATA — from observations
- **m_A, r_A, D_C:AB, k_A:** AI_ESTIMATED — *"chose or estimated"*
- **FLRW outputs:** FORBIDDEN for H-data column

---

## Step 5: Approximate Matches to Rate of Expansion Data — Forensic Extraction

**THIS IS THE CRITICAL STEP for β_d/β_q and H_MULT.**

### Author Instruction (verbatim)
> *"We are about to test the notion that gravitational interactions between neighboring non-colliding galaxy clusters provide a basis for explaining (at least approximately) changes in the rate of expansion of the universe."*

> *"Assume that each one of object-A and object-P is a galaxy cluster or a protocluster."*

> *"Assume that protoclusters and galaxy clusters can increase their masses by accreting nearby stuff or can change, over time, in other ways."*

### Key Question
> *"How well can you fit (by using my monopole, dipole, and quadrupole components of gravity) the data (in the Galaxy Cluster Parameters table) about the observed rate of expansion of the universe?"*

### Scaling Relations (ONLY formulas provided)
> *"In doing this work, use the formulas r_dA = β_d r_A, r_dP = β_d r_P, and |r_qAB|² = (β_q)² r_A r_P. Constrain each one of β_d and β_q to be non-negative. Do not constrain β_d or β_q based on any other physical distances or physical lengths. Try to choose positive values for β_d and β_q that minimize the standard-deviations away from the nominal values of observed H(z)."*

### β_d and β_q Instructions
**CRITICAL QUOTE:**
> *"Try to choose positive values for β_d and β_q that minimize the standard-deviations away from the nominal values of observed H(z)."*

> *"Report your value of values of β_d and β_q."*

### Objective Function
**Minimize:** standard-deviations away from observed H(z)  
**Method:** NOT specified — AI discretion  
**Constraints:**  
- β_d ≥ 0, β_q ≥ 0  
- Do NOT constrain based on physical distances/lengths  
- Quadrupole attraction dominates at high redshift  
- Dipole repulsion dominates at low redshift  

### H-MULT Table Requirements
> *"Provide a table, named 'Approximate Matches to Rate of Expansion Data', for which there is one row for each member of the Set of Times and you ordered the rows so the that times are in descending order and the columns provide the following information."*

**Columns:**
- Time
- z (redshift)
- H-data: H(z), observed rate, with uncertainty (repeat from Step 4)
- H-FLRW: rate calculated by FLRW metric (for comparison)
- σ_FLRW: standard deviations away from H-data
- H-MULT: *"The rate of expansion as calculated by use of my monopole, dipole, and quadrupole components of gravity and your values for β_d and β_q."*
- σ_MULT: standard deviations away from H-data

### Critical Constraints for H-MULT
- *"Ensure that quadrupole attraction dominates at high redshift."*
- *"Ensure that dipole repulsion dominates at low redshift."*
- *"Feel free to use any or all the information in the Galaxy Cluster Parameters table."*
- **"Try to avoid using outputs from uses of the FLRW metric or other Lambda-CDM models."**

### Explanation Requirements
> *"Explain how you chose or estimated the observed values. Explain how you found or computed the FLRW metric values."*

> *"Characterize the relative - between MULTING and FLRW - qualities of the two fits to observed rate of expansion data."*

### H_MULT Formula Status
**FORMULA PROVIDED:** NO  
**BRIDGE PROVIDED:** NO  
**PROCEDURAL INSTRUCTION:** YES — "fit by using monopole, dipole, quadrupole"  
**AI DISCRETION:** ALLOWED — "Feel free to use any or all..."

**Status:** UNDER_SPECIFIED — computational bridge F_oP → H_MULT is delegated to AI interpretation

---

## Step 6: Projections About the Future — Forensic Extraction

### FLRW Future Projection
> *"Does the rate of expansion calculated by use of the FLRW metric project a future time at which the rate of expansion would decrease? If so, estimate that time and an analog, for that time, to H(z). If not, estimate an asymptotic analog for H(z) for large times."*

### MULTING Future Projection
> *"Regarding making projections based on my work, try to avoid (to the extent reasonably possible) projections have bases in other models or theories. Does the rate of expansion calculated by the use of my monopole, dipole, and quadrupole components of gravity and your values for β_d and β_q project a future time at which the sum of monopole gravity plus quadrupole gravity would start to be larger than dipole gravity? If so, do the following."*

**If crossover occurs:**
- *"Estimate and report a time range for the future time at which the sum of monopole gravity attraction plus quadrupole gravity attraction would start to be larger than dipole gravity repulsion. Try to calculate (without using outputs from uses of the FLRW metric or other Lambda-CDM models) and report (for that time) an analog to H(z)."*

**If rate becomes negative:**
- *"Estimate and report a time, if any, at which the rate of expansion of the universe would start to be negative. Try to calculate (without using outputs from uses of the FLRW metric or other Lambda-CDM models) and report (for that time) an analog to H(z)."*

### Status Tags
- **FLRW projection:** ALLOWED for comparison
- **MULTING projection:** REQUIRED to avoid FLRW outputs
- **Crossover time (monopole+quadrupole > dipole):** PREDICTIVE claim (NOT table reproduction)

---

## Step 7: A Possible Equation of State for Use with the FLRW Metric — Forensic Extraction

### Author Request (verbatim)
> *"I request that you try to suggest an equation of state for which use of the FLRW metric would be more accurate (regarding H-data data) than present Lambda-CDM uses, regarding H(z), of the FLRW metric."*

### w_eff(z) Computation
> *"Compute a sample w_eff(z) curve from the H-data values (of H(z)) that you already used. Use FLRW techniques, but with an equation of state that features an adjustable (based on time) parameter w."*

### Table: Comparison of matches to data, including via w_eff(z)'

**Columns:**
- Time
- z
- H-data (с uncertainty) — repeat from earlier
- H-FLRW — Lambda-CDM (repeat from Step 5)
- σ_FLRW
- H-MULT — previously calculated (repeat from Step 5)
- σ_MULT
- w_eff — *"The value you suggest for w_eff(z)."*
- H-w_eff — *"The rate of expansion calculated by use of w_eff(z) and the FLRW metric."*
- σ_w_eff — standard deviations away from H-data

### Critical Note
> *"If appropriate, discuss notions of 'phase changes' that might associate with the equation of state (especially regarding the onset of multibillion-year eras in the rate of expansion)."*

> *"If appropriate, suggest additional perspective about the new equation of state."*

### Status Tags
- **w_eff:** AI_ESTIMATED — fitted to H-data using FLRW
- **H-w_eff:** DERIVED from w_eff via FLRW
- **Purpose:** comparison to show MULTING vs improved-FLRW

---

## Step 8: Recap — Forensic Extraction

> *"For my convenience, please restate the following."*

**Required outputs:**
- β_d value used
- β_q value used
- Time range (MULTING), if any, for future crossover (monopole+quadrupole > dipole)

---

## Table A1 — Forensic Extraction

### Table Caption (verbatim)
> *"Table A1. Responses, to our prompt, by one online service that has bases in artificial intelligence. Regarding time, the prompt asked for values for times corresponding to integers z, the prompt asked for a redshift that associates with the time. Regarding each one of the H-... columns, the prompt asked for values of the Hubble parameter, in units of km/s·Mpc (kilometers per second per megaparsec). Regarding H-data, the prompt asked for results from observations, corresponding to integers z and that I-H-FLM, H-FLM minus the nominal value of H-data. Regarding z_FLRW, the prompt asked that the value that ACDM cosmology suggests. Regarding σ_FLRW, the prompt asked for the number of observational standard deviations that associates with H-FLRW minus the nominal value of H-data. Regarding σ_MULT, the prompt asked for a value that MULTING suggests. Regarding σ_MULT, the prompt asked for the number of observational standard deviations that associates with σ_MULT minus the nominal value of H-data. Regarding w_eff, the prompt did not define w_eff but did state 'Compute a sample w_eff(z) curve from the H-data values of H(z)) that you already used. Use FLRW techniques, but with an equation of state that features an adjustable (based on time) parameter w.' Regarding H-w_eff, the prompt asked for 'The rate of expansion calculated by use of w_eff(z) and the FLRW metric.' Regarding σ_w_eff, the prompt asked for 'The positive, zero, or negative number of standard deviations that rate of expansion, calculated by use of w_eff(z) and the FLRW metric, is away from the nominal observed value.'. Regarding H-MULT, the online service reported choosing β_d = 4.5 and β_q = 18.0."*

### Table A1 Data

| Time | z | H-data | H-FLRW | σ_FLRW | H-MULT | σ_MULT | w_eff | H-w_eff | σ_w_eff |
|------|---|--------|--------|--------|--------|--------|-------|---------|---------|
| 13.5 | 0 | 73.0±7.0 | 67.4 | -5.6 | - | - | 1.30 | 73 | 0 |
| 13 | 0.06 | 69.0±3.0 | 68.1 | -0.3 | 70.2 | 0.4 | -1.25 | 69.3 | 0.1 |
| 12 | 0.14 | 74.0±4.0 | 69.3 | -1.2 | 73.5 | -0.1 | -1.20 | 74.1 | 0.03 |
| 11 | 0.25 | 79.0±4.5 | 71.5 | -1.7 | 78.8 | -0.04 | -1.15 | 79.2 | 0.04 |
| 10 | 0.4 | 82.0±5.0 | 75 | -1.4 | 83.1 | 0.2 | -1.10 | 82.3 | 0.1 |
| 9 | 0.65 | 92.0±7.0 | 83 | -1.3 | 91.4 | -0.1 | -1.05 | 92.4 | 0.1 |
| 8 | 1 | 105.0±8.0 | 95.7 | -1.2 | 104.2 | -0.1 | -1.01 | 105.3 | 0.04 |
| 7 | 1.5 | 125.0±15.0 | 114.8 | -0.7 | 126.5 | 0.1 | -0.98 | 125.6 | 0.04 |
| 6 | 2.1 | 150.0±20.0 | 140.3 | -0.5 | 151.8 | 0.1 | -0.96 | 150.5 | 0.03 |
| 5 | 3.2 | 195.0±30.0 | 187.6 | -0.2 | 197.3 | 0.1 | -0.95 | 195.2 | 0.01 |
| 4 | 5 | 270.0±50.0 | 265.2 | -0.1 | 271.5 | 0.03 | -0.97 | 270.2 | 0.004 |
| 3 | 8.5 | 420.0±90.0 | 398.5 | -0.2 | 418.1 | -0.02 | -1.00 | 420.1 | 0.001 |

### Key Values Reported
**β_d = 4.5**  
**β_q = 18.0**

### Provenance
**Source:** AI online service output (NOT author calculation, NOT verified)  
**Status:** AI_ESTIMATED — phenomenological fit to H-data

---

## Bridge Finding — Summary

### Question: Does Appendix A1 explicitly define F_oP → H_MULT(z)?

**Answer:** NO, formula missing

**Evidence:**

1. **Force formulas provided (Step 2):**
   - F_m = G m_A m_P / r² (monopole)
   - F_d = (G k_A c^{-2} m_P |r_dA| / (r³)) + (G k_P c^{-2} m_A |r_dP| / (r³)) (dipole)
   - F_q = G k_A k_P c^{-4} |r_qAB|² / (r⁴) (quadrupole)
   - F_oP = F_m - F_d + F_q (total)

2. **Scaling relations provided (Step 5):**
   - r_dA = β_d × r_A
   - r_dP = β_d × r_P
   - |r_qAB|² = β_q² × r_A × r_P

3. **What is NOT provided:**
   - How to compute H_MULT(z) from F_oP, β_d, β_q, m_A, r_A, k_A, ...
   - Functional form H_MULT = f(z, β_d, β_q, ...)
   - Computational procedure beyond "fit the data"

4. **What IS provided:**
   - Procedural instruction: *"How well can you fit (by using my monopole, dipole, and quadrupole components of gravity) the data..."*
   - Constraint: minimize standard deviations from observed H(z)
   - Constraint: quadrupole dominates high-z, dipole dominates low-z
   - AI discretion: *"Feel free to use any or all the information"*

**Status:** PARTIAL — procedural/heuristic bridge only, NOT computational formula

**Implication:** Table A1 reproduction requires either:
1. Reverse-engineering AI service interpretation (unknown), OR
2. Obtaining explicit formula from author, OR
3. Treating Table A1 as empirical data table (no predictive H(z) function)

---

## What Can Be Reproduced

### Allowed (Code-Ready)
1. **Table structure** — Step 3-7 table definitions
2. **Force formulas** — F_m, F_d, F_q, F_oP (Step 2)
3. **Scaling relations** — r_dA, r_dP, r_qAB (Step 5)
4. **β_d = 4.5, β_q = 18.0** — as TABLE_REPORTED values (NOT predictive)
5. **Table A1 data** — as empirical table for comparison

### Blocked (NOT Code-Ready)
1. **H_MULT(z) computation** — formula missing
2. **β_d, β_q fitting** — objective function and method under-specified
3. **Future projections** — requires H_MULT(z) formula
4. **MCMC parameter estimation** — requires H_MULT(z) likelihood function

---

## Conclusion

### Status of Steps 3–7
- **Step 3 (Time Range):** SOURCE_CONFIRMED, code-ready
- **Step 4 (Galaxy Cluster Parameters):** AUTHOR_PROMPT_INSTRUCTION, AI-estimated values
- **Step 5 (β_d, β_q, H_MULT):** UNDER_SPECIFIED, bridge formula missing
- **Step 6 (Future Projections):** BLOCKED by Step 5
- **Step 7 (w_eff comparison):** SOURCE_CONFIRMED, code-ready for comparison only

### Bridge F_oP → H_MULT(z) Status
**PARTIAL** — procedural instruction exists, computational formula does NOT

### What Remains Blocked
1. H(z) prediction on new redshifts
2. MCMC parameter estimation
3. Validation or falsification of MULTING cosmology
4. Comparison with observations beyond Table A1

### Next Smallest Safe Step
1. **Implement force formulas** (Step 2) — code-ready
2. **Implement scaling relations** (Step 5) — code-ready
3. **Store Table A1 as empirical data** — table reproduction only
4. **Mark β_d, β_q as FITTED_PHENOMENOLOGICAL** — NO predictive claim
5. **Document bridge as UNDER_SPECIFIED** — explicit blocker
6. **Update clarification brief** — add Step 5 finding to outreach docs

---

**End of Forensic Extraction**  
**Next action:** Create `src/appendix_a1_procedure_registry.py` to encode these findings programmatically.
