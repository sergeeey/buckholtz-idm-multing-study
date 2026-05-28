# Public Formula Stripping Report — MULTING Force Law Candidates

**Date:** 2026-05-28  
**Status:** SOURCE_CANDIDATE (awaiting manual verification)  
**Purpose:** Document candidate MULTING force-law formulas found in public materials

---

## Executive Summary

**Found:**
- Candidate pairwise force-law equations (monopole, dipole, quadrupole)
- Beta length-scale definitions (r_dA, r_dP, r_qAB)
- Structure compatible with G-ECOS (gravitating objects, entities-created-by-collections-of-other-solutions)

**NOT found:**
- Closed H_MULT(z) formula for cosmological expansion
- Mean-field / fluid approximation mapping force → H(z)
- Closure relations for m_A(z), r_A(z), k_A(z), D_C:AB(z)
- Likelihood function for MCMC fitting

**Status:**
- Force-law layer: SOURCE_CANDIDATE (requires manual PDF verification)
- Cosmological closure: MISSING
- MCMC readiness: BLOCKED

**Safe conclusion:**
> MULTING provides a candidate pairwise gravitational force law extending Newtonian gravity with dipole and quadrupole terms. Public materials do not provide computational closure for mapping this force law to cosmological expansion H(z) or for MCMC parameter estimation.

---

## 1. Extracted Force Equations (Candidates)

### Monopole Force
```
F_m = G m_A m_P / r^2
```

**Interpretation:** Standard Newtonian gravitational force between two gravitating objects A and P.

**Variables:**
- G: gravitational constant
- m_A: mass of object A
- m_P: mass of object P (probe/test mass)
- r: separation distance

**Units:** [Force] = kg·m/s²
**Dimensionality:** ✅ Correct (standard Newtonian)

---

### Dipole Force
```
F_d = G c^-2 (k_A m_P |r_dA| + k_P m_A |r_dP|) / r^3
```

**Interpretation:** Velocity/kinetic-energy-dependent correction, 1/r³ scaling (dipole).

**Variables:**
- c: speed of light
- k_A: kinetic energy scale of object A (units: energy = kg·m²/s²)
- k_P: kinetic energy scale of object P
- r_dA = beta_d × r_A: dipole length scale for A
- r_dP = beta_d × r_P: dipole length scale for P
- r_A: characteristic radius of A (possibly cluster radius)
- r_P: characteristic radius of P

**Units check:**
- Numerator: [G] × [c⁻²] × [k] × [m] × [r_d]
  = (m³/kg·s²) × (s²/m²) × (kg·m²/s²) × kg × m
  = kg·m³/s²
- Denominator: r³ = m³
- Force: kg·m³/s² / m³ = kg·m/s² ✅

**Dimensionality:** ✅ Correct

---

### Quadrupole Force
```
F_q = G k_A k_P c^-4 |r_qAB|^2 / r^4
```

**Interpretation:** Higher-order correction, 1/r⁴ scaling (quadrupole).

**Variables:**
- |r_qAB|² = beta_q² × r_A × r_P: quadrupole length-scale product

**Units check:**
- Numerator: [G] × [k_A] × [k_P] × [c⁻⁴] × [r_qAB²]
  = (m³/kg·s²) × (kg·m²/s²) × (kg·m²/s²) × (s⁴/m⁴) × m²
  = kg·m⁴/s²
- Denominator: r⁴ = m⁴
- Force: kg·m⁴/s² / m⁴ = kg·m/s² ✅

**Dimensionality:** ✅ Correct

---

### Total MULTING Force
```
F_oP = F_m - F_d + F_q
```

**Interpretation:** Net force on probe P from object A, combining monopole, dipole (subtractive), and quadrupole (additive).

**Sign structure:**
- Monopole: + (attractive)
- Dipole: − (reduces attraction or repulsive depending on kinematics)
- Quadrupole: + (enhances attraction)

**Question for author:** Why is dipole subtractive? Does this encode repulsion under certain kinematic conditions?

---

## 2. Beta Length-Scale Definitions

### Dipole Length Scales
```
r_dA = beta_d × r_A
r_dP = beta_d × r_P
```

**Variables:**
- beta_d: dimensionless dipole strength parameter (candidate value: 4.5 from Table A1)
- r_A, r_P: characteristic radii of objects A and P

**Units:** [r_d] = [r] (length)

**Physical interpretation (UNKNOWN):**
- Scale at which dipole force becomes significant?
- Cutoff radius?
- Effective interaction range?

**Requires clarification:** What is r_A for Sun? For Earth? For dark matter halo?

---

### Quadrupole Length Scale
```
|r_qAB|^2 = beta_q^2 × r_A × r_P
```

**Variables:**
- beta_q: dimensionless quadrupole strength parameter (candidate value: 18.0 from Table A1)

**Units:** [r_qAB²] = [r²] (length²)

**Physical interpretation (UNKNOWN):**
- Product of characteristic scales?
- Geometric mean with beta_q correction?

---

## 3. Status Tags

### Force-Law Records Status

| Equation | Status | Code Permission | Verification Status |
|----------|--------|----------------|---------------------|
| F_m | SOURCE_CANDIDATE | allowed_for_dimensional_check | awaiting manual PDF verification |
| F_d | SOURCE_CANDIDATE | allowed_for_dimensional_check | awaiting manual PDF verification |
| F_q | SOURCE_CANDIDATE | allowed_for_dimensional_check | awaiting manual PDF verification |
| F_oP | SOURCE_CANDIDATE | allowed_for_dimensional_check | awaiting manual PDF verification |
| r_dA | SOURCE_CANDIDATE | allowed_for_record_only | awaiting manual PDF verification |
| r_dP | SOURCE_CANDIDATE | allowed_for_record_only | awaiting manual PDF verification |
| r_qAB | SOURCE_CANDIDATE | allowed_for_record_only | awaiting manual PDF verification |

**SOURCE_CANDIDATE:** Formula-stripping extraction, not yet manually verified against original PDF.

**Code permissions:**
- `allowed_for_dimensional_check`: Can verify units, cannot compute H(z)
- `allowed_for_record_only`: Can document, cannot compute forces

**NOT allowed:**
- H(z) modeling
- MCMC fitting
- Parameter estimation from cosmological data
- Predictions of cosmic expansion

---

## 4. Missing Bridge: Force Law → H(z)

### What We Have
- Pairwise force law between two objects (A and P)
- Depends on: masses (m_A, m_P), radii (r_A, r_P), kinetic energies (k_A, k_P), separation (r)

### What We Need (MISSING)
1. **Mean-field approximation:** How to go from pairwise forces to fluid-level stress-energy tensor T_μν?
2. **Cosmological average:** How to average over galaxy clusters, voids, cosmic web?
3. **Closure relations:** How do m_A(z), r_A(z), k_A(z), D_C:AB(z) evolve with redshift?
4. **Friedmann-like equations:** What is the modified Friedmann equation H²(z; params)?
5. **Likelihood function:** P(H_obs | H_MULT(z; beta_d, beta_q, ...))

### Example of Missing Steps

**Standard cosmology (ΛCDM):**
```
Newtonian gravity → Einstein equations → Friedmann equations → H(z; Ωm, ΩΛ, H0)
```

**MULTING (incomplete chain):**
```
MULTING force law → ??? → ??? → H_MULT(z; beta_d, beta_q, ...)
                    ^missing  ^missing
```

**Questions for author:**
1. Is there a mean-field / virial approximation?
2. Is there a MULTING-modified Friedmann equation?
3. How do beta_d, beta_q relate to cosmological observables (H(z), distance modulus)?
4. What are the closure assumptions for m_A(z), r_A(z)?

---

## 5. Dimensional Analysis (Preliminary)

### Force Scaling Summary

| Component | Scaling | Coefficient Dimensions |
|-----------|---------|------------------------|
| Monopole | r⁻² | [G m_A m_P] = kg·m³/s² |
| Dipole | r⁻³ | [G c⁻² k m r_d] = kg·m³/s² |
| Quadrupole | r⁻⁴ | [G c⁻⁴ k² r_q²] = kg·m⁴/s² |

**Observation:** Each term has correct units for force when divided by appropriate power of r.

**Implication:** At small r (Solar System), monopole dominates. At large r (cluster scales), dipole and quadrupole may become significant if k and r_d are large.

**Regime-of-applicability question:**
- If r_d ~ 4.5 Mpc (cluster scale), dipole may be negligible at r ~ AU (Solar System).
- This would resolve PPN Solar System constraints (dipole/quadrupole inactive locally).
- Requires explicit cutoff function or scale-dependent analysis.

---

## 6. G-ECOS Framework Context

**G-ECOS:** Gravitating objects, entities-created-by-collections-of-other-solutions.

**Interpretation (from public materials, not verified):**
- Objects A and P are "solutions" (possibly isomers, dark matter halos, galaxy clusters)
- Each solution has: mass (m), radius (r), kinetic energy (k)
- MULTING force law governs interactions between solutions
- Monopole: standard Newtonian attraction
- Dipole: velocity-dependent correction (relativistic? kinetic energy?)
- Quadrupole: higher-order structure correction

**Unclear:**
- What defines a "solution" operationally?
- Is the Sun a solution? Earth? Dark matter halo? Galaxy cluster?
- How many solutions populate the universe at z = 0? At z > 0?

---

## 7. Safe vs Unsafe Wording

### ✅ Safe
- "MULTING provides a candidate pairwise force law with monopole, dipole, and quadrupole terms."
- "Dimensional analysis confirms correct units for each force component."
- "Public materials do not provide the force-to-expansion mapping required for H(z) modeling."
- "Beta length-scale definitions (r_dA, r_dP, r_qAB) are documented but physical interpretation is unclear."
- "MCMC fitting is blocked pending closure relations and H_MULT(z) formula."

### ❌ Unsafe (do NOT say)
- "MULTING is just Newtonian gravity with ad-hoc corrections." (dismissive)
- "The force law is wrong." (unverified claim)
- "We can now compute H(z)." (false — missing bridge)
- "MCMC shows MULTING fails." (MCMC blocked, no fit performed)
- "This validates/refutes MULTING." (no validation or refutation performed)

---

## 8. Next Steps

### Priority 1 — Manual Verification
**Action:** Read original PDF (preprints202511.0598.v6.pdf) and verify extracted formulas character-by-character.

**Checklist:**
- [ ] F_m formula matches manuscript
- [ ] F_d formula matches manuscript
- [ ] F_q formula matches manuscript
- [ ] F_oP sign structure (+/−/+) matches manuscript
- [ ] r_dA, r_dP, r_qAB definitions match manuscript
- [ ] beta_d, beta_q values (4.5, 18.0) match Table A1

**If verified:**
- Upgrade status: SOURCE_CANDIDATE → SOURCE_CONFIRMED
- Update code_permission: allowed_for_dimensional_check → allowed_for_force_calculation

**If NOT verified:**
- Downgrade status: SOURCE_CANDIDATE → SOURCE_INCORRECT
- Mark as formula-stripping error
- Re-extract manually

---

### Priority 2 — Author Clarification (after Priority 1)
**Questions for Dr. Buckholtz:**

**Q1:** Are the extracted force equations (F_m, F_d, F_q, F_oP) correct?

**Q2:** Is there a mean-field or fluid approximation that maps pairwise forces to T_μν?

**Q3:** Is there a MULTING-modified Friedmann equation or closed H_MULT(z) formula?

**Q4:** What are the closure relations for m_A(z), r_A(z), k_A(z)?

**Q5:** What defines a "solution" in G-ECOS operationally? (Sun? Earth? Galaxy? Cluster?)

---

### Priority 3 — Dimensional Checks (if Priority 1 passes)
**Action:** Implement dimensional-analysis tests.

**Tests:**
- F_m has units of force
- F_d has units of force
- F_q has units of force
- r_dA has units of length
- beta_d is dimensionless
- beta_q is dimensionless

**Code permission:** allowed_for_dimensional_check (no H(z) modeling)

---

### Priority 4 — Regime-of-Applicability Analysis (if Priority 1 + 2 pass)
**Action:** Analyze force-law behavior at different scales.

**Scenarios:**
1. Solar System (r ~ AU, m_A = M_sun)
2. Galaxy (r ~ kpc, m_A = M_galaxy)
3. Galaxy cluster (r ~ Mpc, m_A = M_cluster)

**Questions:**
- At what r does F_d become comparable to F_m?
- At what r does F_q become significant?
- If r_d ~ Mpc, is dipole negligible at r ~ AU?

---

## 9. MCMC Blocker Summary

### What MCMC Requires
1. Forward model: H_MULT(z; params) computable for any z
2. Parameter vector: (beta_d, beta_q, ...) with priors
3. Likelihood: P(H_obs | H_MULT(z; params))
4. Data: (z_i, H_obs_i, σ_i) observational dataset
5. Sampler: MCMC algorithm (emcee, PyMC, Stan)

### What We Have
1. ❌ No H_MULT(z; params) formula
2. ✅ Two parameters identified (beta_d, beta_q from Table A1)
3. ❌ No likelihood function (depends on #1)
4. ⏳ Data available (cosmic chronometers, Pantheon+) but not used
5. ✅ Sampler ready (can use emcee if #1-3 provided)

### Blocker Status
**CRITICAL BLOCKER:** No H_MULT(z) formula.

**Cannot proceed with MCMC until:**
- H_MULT(z; beta_d, beta_q, ...) is provided by author, OR
- Force-to-expansion mapping is derived, OR
- Phenomenological H_MULT(z) form is proposed and justified

**Safe wording:**
> "MCMC parameter estimation is blocked pending the H_MULT(z) forward model. The force-law layer is documented but does not yet connect to cosmological observables."

---

## 10. Relationship to Existing Findings

### Finding 1 — Beta Values Fitted
**Status:** Consistent with force-law formulas.

Beta values (4.5, 18.0) from Table A1 appear in length-scale definitions (r_dA, r_qAB). Confirms they are scale parameters, not arbitrary coefficients.

### Finding 3 — H-MULT Formula Missing
**Status:** STILL BLOCKED.

Force-law extraction does NOT resolve this blocker. H(z) mapping remains missing.

### Finding 11 — PPN Check Blocked
**Status:** Partially addressable if force law is verified.

If r_d ~ Mpc and r << r_d → dipole negligible → PPN γ = 1, β = 1 (GR recovered locally).

Requires explicit scale-dependence analysis.

---

## 11. Document Status

**Verification status:** SOURCE_CANDIDATE (awaiting manual PDF check)

**Code permission:** allowed_for_dimensional_check (no H(z) modeling, no MCMC)

**Safe to share with Dr. Buckholtz:** YES (after manual verification)

**High-risk artifacts:** None (this is factual extraction, not critique)

**Next action:** Manual verification against preprints202511.0598.v6.pdf

---

**Last updated:** 2026-05-28  
**Requires:** Manual verification pass  
**Blocks:** H(z) modeling, MCMC fitting  
**Unblocks:** Dimensional analysis, force-law documentation
