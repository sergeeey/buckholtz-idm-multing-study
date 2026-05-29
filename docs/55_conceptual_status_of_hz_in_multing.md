# Conceptual Status of H(z) in MULTING — Internal Memo

**Date:** 2026-05-29  
**Status:** INTERNAL_CONCEPTUAL_MEMO  
**Classification:** HYPOTHESIS_NOT_SOURCE_CONFIRMED  
**Author-facing:** NO (internal analysis only)  
**MCMC status:** BLOCKED  
**Prediction status:** BLOCKED  
**Purpose:** Clarify possible operational differences between FLRW H(z) and MULTING H_MULT(z)

---

## ⚠️ Important Disclaimers

**This is a hypothesis, not a claim:**
- This memo explores possible interpretations of H_MULT(z)
- It does NOT claim Buckholtz is wrong
- It does NOT claim H_MULT is "fake" or "misleading"
- It documents conceptual ambiguity that affects MCMC design
- Author clarification is required to resolve ambiguity

**Status:**
- OPERATIONAL_MEANING_UNCLEAR
- AUTHOR_CLARIFICATION_REQUIRED
- INTERNAL_ANALYSIS_ONLY (not for public or author criticism)

**Use case:**
- Guide MCMC implementation decisions
- Prepare author clarification question
- Document why "just fit H_MULT" is non-trivial

---

## Executive Summary

**In FLRW / ΛCDM cosmology:** H(z) is a **metric expansion quantity** defined by H = ȧ/a, where a(t) is the scale factor of the FLRW metric. It describes how the fabric of spacetime expands and is directly tied to Einstein's field equations via the Friedmann equations.

**In MULTING:** H_MULT(z) appears in Table A1 as a quantity that fits H_obs(z) data better than H_FLRW(z). However, **H_MULT(z) may not be operationally identical to FLRW H(z)**. Possible interpretations:
1. **FLRW-like:** H_MULT is a modified Friedmann expansion rate from MULTING field equations
2. **Kinematic:** H_MULT is an effective separation rate of large astrophysical structures (lattice/N-body observable)
3. **Phenomenological:** H_MULT is an AI-assisted comparison quantity optimized to match H_obs

**Why this matters:** The operational meaning determines:
- Which computational bridge F_oP → H_MULT(z) is appropriate
- Whether MCMC should compare "modified Friedmann" or "effective kinematics"
- What cluster variables and averaging rules are needed
- Whether Table A1 is retrodiction or prediction

**Current status:** The operational meaning of H_MULT(z) is **not yet source-confirmed**. This ambiguity is a major component of **Blocker 1 (Source-Confirmed Bridge)** in the MCMC blocker chain.

**This memo hypothesis:** Given that MULTING starts from pairwise forces between large structures (not a metric/field theory), H_MULT(z) **may represent an effective kinematic observable** rather than a fundamental metric expansion. This would be consistent with lattice/N-body approaches where "expansion" emerges from collective motion rather than spacetime geometry.

**Action required:** Author clarification (see § Safe Author Question below).

---

## 1. FLRW Meaning of H(z)

### Definition

In standard FLRW cosmology:
```
H(z) ≡ ȧ/a

where:
  a(t) = scale factor of the FLRW metric
  ȧ = da/dt (time derivative)
  z = redshift (related to a by 1+z = 1/a)
```

### Operational Meaning

**Metric expansion:**
- H(z) describes how proper distances between comoving observers increase
- Embedded in the FLRW metric: ds² = -dt² + a²(t)[dr² + ...]
- Governed by Friedmann equations (from Einstein field equations)

**Observational connections:**
- **Luminosity distance:** d_L(z) = (1+z) ∫[1/(H(z'))] dz' (supernovae)
- **Angular diameter distance:** d_A(z) = d_L(z)/(1+z)² (BAO, CMB)
- **Cosmic chronometers:** dz/dt measured directly → H(z) via dz/dt = -H(z)(1+z)
- **CMB:** Early-universe H(z) from angular power spectrum

**Status:** Well-defined, source-confirmed via GR, extensively tested.

---

## 2. Possible MULTING Meaning of H_MULT(z)

### Starting Point: Pairwise Forces

MULTING begins from:
```
F_oP = F_m - F_d + F_q

where:
  F_m ∝ r⁻² (monopole, attractive)
  F_d ∝ r⁻³ (dipole, repulsive?)
  F_q ∝ r⁻⁴ (quadrupole, attractive)
```

**Key observation:** This is a **force law between large astrophysical structures** (clusters, voids), not a metric/field theory starting point.

### Three Possible Interpretations of H_MULT(z)

**Interpretation 1: FLRW-like Modified Friedmann**
- H_MULT(z) represents true metric expansion in a modified gravity theory
- MULTING forces → modified Einstein equations → modified Friedmann equation
- H_MULT would replace H_FLRW as the fundamental expansion rate
- **Status:** Possible but not source-confirmed
- **Evidence:** Hamiltonian bridge H²(a) = H₀²[Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵] has Friedmann-like form

**Interpretation 2: Kinematic Effective Observable**
- H_MULT(z) represents effective separation rate of large structures
- Emergent from N-body/lattice dynamics, not fundamental metric
- Analogous to "peculiar Hubble flow" in structure formation
- **Status:** Possible, consistent with lattice/N-body bridge candidates
- **Evidence:** 
  - Discrete lattice bridge: ä/a = N_eff F_oP/(μ D_AB)
  - Wigner-Seitz cell approach (pair → cell → background)
  - MULTING focuses on cluster-scale forces, not metric

**Interpretation 3: Phenomenological Comparison Quantity**
- H_MULT(z) is an AI-assisted fit to H_obs optimized for Table A1
- Not intended as fundamental expansion rate OR kinematic observable
- Purpose: demonstrate MULTING forces → parameter choices track data
- **Status:** Possible, consistent with "AI service" in Step 6
- **Evidence:** 
  - Phi-scaling heuristic: H_MULT = Φ(z) × H_FLRW
  - Beta parameters fitted/reported to match H_obs
  - No explicit H_MULT(z) formula in manuscript

### Current Status

| Aspect | Status |
|--------|--------|
| **Operational meaning** | ❌ UNCLEAR |
| **FLRW equivalence** | ❌ NOT ESTABLISHED |
| **Source confirmation** | ❌ MISSING |
| **Ambiguity impact** | ⚠️ BLOCKS MCMC DESIGN |

**Hypothesis (this memo):** Given MULTING's pairwise-force starting point and lack of explicit metric/field theory formulation in manuscript, **Interpretation 2 (kinematic effective observable)** may be closest to author's intent. But this remains **HYPOTHESIS_NOT_SOURCE_CONFIRMED**.

---

## 3. Why This Matters Computationally

**The operational meaning of H_MULT(z) determines MCMC implementation:**

### If H_MULT is FLRW-like (Interpretation 1)

**Implications:**
- Modified Friedmann equation: H²(z) = f(z; Ω_k, Ω_m, Ω_d, Ω_q)
- Direct comparison to ΛCDM: both are metric expansion rates
- Observables: luminosity distance, BAO, CMB all computable
- MCMC: compare H_MULT vs. H_FLRW on Pantheon+, BAO, Cosmic Chronometers

**Requirements:**
- Source-confirmed H²(z) formula (e.g., Hamiltonian bridge)
- Physical interpretation of Ω coefficients
- Connection to metric/field equations

**MCMC design:**
```python
def compute_luminosity_distance_MULTING(z, omega_k, omega_m, omega_d, omega_q, H0):
    """FLRW-like: integrate H_MULT to get d_L"""
    def H_MULT(z_prime):
        a = 1.0 / (1.0 + z_prime)
        return H0 * np.sqrt(omega_k * a**(-2) + omega_m * a**(-3) 
                            + omega_d * a**(-4) + omega_q * a**(-5))
    
    # Integrate 1/H(z) from 0 to z
    d_c = integrate.quad(lambda zp: 1.0/H_MULT(zp), 0, z)[0]
    return (1 + z) * d_c

# MCMC comparison: chi2_MULTING vs. chi2_LCDM on Pantheon+ supernovae
```

### If H_MULT is Kinematic (Interpretation 2)

**Implications:**
- Effective separation rate: H_MULT ∝ Ḋ/D for large structures
- Not directly comparable to ΛCDM (different observables)
- May need coarse-graining rule: cluster dynamics → background observable
- Observables: H_obs from Cosmic Chronometers (kinematic), but NOT d_L directly

**Requirements:**
- Cluster variable evolution: m_A(z), D_AB(z), N_eff
- Averaging prescription: N-body → H_eff
- Connection to structure formation

**MCMC design:**
```python
def compute_H_eff_MULTING(z, m_A, r_A, D_AB, N_eff, beta_d, beta_q):
    """Kinematic: compute effective separation rate from cluster dynamics"""
    # Compute pairwise force
    F_oP = compute_force_oP(r_A, beta_d, beta_q)
    
    # Effective acceleration (lattice bridge)
    mu = m_A / 2  # reduced mass
    a_eff = N_eff * F_oP / (mu * D_AB)
    
    # Convert to H-like quantity (ä/a)
    H_eff = np.sqrt(a_eff * (1 + z))  # dimensional scaling
    return H_eff

# MCMC comparison: chi2_MULTING vs. chi2_LCDM on Cosmic Chronometers ONLY
# (cannot use Pantheon+ d_L — different observable)
```

### If H_MULT is Phenomenological (Interpretation 3)

**Implications:**
- AI-assisted fit: H_MULT = Φ(z) × H_FLRW or other heuristic
- Table A1 is retrodiction output, not predictive model
- Cannot extrapolate beyond Table A1 range
- Not suitable for MCMC (no physical model)

**Requirements:**
- Explicit phenomenological formula (e.g., Φ(z) polynomial)
- Clear labeling as retrodiction

**MCMC design:**
```python
# NOT SUITABLE FOR MCMC
# Table A1 is the output, not a model to test
# Can only document: "MULTING procedure produces H_MULT closer to H_obs than H_FLRW"
# Cannot predict new z or compare Bayesian evidence
```

### Decision Impact Summary

| Aspect | FLRW-like | Kinematic | Phenomenological |
|--------|-----------|-----------|------------------|
| **MCMC comparison** | Direct (d_L, BAO, H_obs) | Limited (H_obs only) | Not applicable |
| **Prediction** | Yes (arbitrary z) | Requires cluster table | No (Table A1 only) |
| **Observables** | All (d_L, d_A, H) | H only | Table comparison |
| **Complexity** | Medium (5 params) | High (cluster evolution) | Low (retrodiction) |
| **Validation** | Standard | Structure-specific | Circular (fit to H_obs) |

**Current status:** Operational meaning unclear → **cannot design MCMC** until resolved.

---

## 4. Relation to Table A1

### What Table A1 Shows

**Data:** 12 rows (z=0 to z=8.5), columns: z, H_obs, H_FLRW, H_MULT

**Performance:**
- H_MULT mean residual (Rows 2-12): 1.27 km/s/Mpc
- H_FLRW mean residual (Rows 2-12): 8.13 km/s/Mpc
- H_MULT is about **6× closer to H_obs**

**Interpretation:** This is **strong retrodictive evidence** that a MULTING-inspired parameterization (β_d=4.5, β_q=18.0) can produce an H-like quantity tracking H_obs.

### What Table A1 Does NOT Show

**Missing information:**
1. **How H_MULT was computed:** Appendix A1 Step 6 says "AI service" generates candidates, but explicit formula not provided
2. **Operational meaning:** Whether H_MULT is metric expansion, kinematic rate, or phenomenological output
3. **Prediction:** Beta fitted/reported using data including Table A1 → cannot use same data for validation
4. **Generalization:** No independent test on Pantheon+, BAO, or other datasets

**Status labels:**

| Label | Status |
|-------|--------|
| **TABLE_REPORTED** | ✅ H_MULT values reported in Table A1 |
| **RETRODICTION_EVIDENCE** | ✅ Fit tracks H_obs well |
| **NOT_PREDICTION** | ❌ Beta fitted on this data |
| **NOT_VALIDATION** | ❌ No independent test |
| **OPERATIONAL_MEANING_UNCLEAR** | ⚠️ Don't know what H_MULT represents |

**Key statement:** Table A1 is useful evidence that MULTING forces → parameters can track H_obs, **but it does not by itself define the operational meaning of H_MULT(z)**. We cannot infer from Table A1 alone whether H_MULT is FLRW-like, kinematic, or phenomenological.

---

## 5. Relation to Bridge Candidates

### Our Three Bridge Candidates

**Recap from docs/53_three_path_hmult_roadmap_safe_memo.md:**

1. **Phi-scaling heuristic:** H_MULT = Φ(z) × H_FLRW
   - Status: Phenomenological, under-specified
   - Supports: Interpretation 3 (phenomenological output)

2. **Hamiltonian bridge:** H²(a) = H₀²[Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]
   - Status: Algebraically valid, NOT source-confirmed
   - Supports: Interpretation 1 (FLRW-like)

3. **Discrete lattice bridge:** ä/a = N_eff F_oP/(μ D_AB)
   - Status: Physically interesting, data-heavy
   - Supports: Interpretation 2 (kinematic)

### Relationship to Operational Meaning

**If Buckholtz confirms Phi-scaling (Path 1):**
- → H_MULT is Interpretation 3 (phenomenological)
- → Table A1 is retrodiction only
- → MCMC not applicable (no physical model)
- → Label: HEURISTIC_FIT_NOT_PHYSICAL_MODEL

**If Buckholtz confirms Hamiltonian (Path 2):**
- → H_MULT is Interpretation 1 (FLRW-like)
- → Implement modified Friedmann MCMC
- → Compare d_L, BAO, H_obs across datasets
- → Label: MODIFIED_FRIEDMANN_EXPANSION

**If Buckholtz confirms Lattice N-body (Path 3):**
- → H_MULT is Interpretation 2 (kinematic)
- → Implement N-body coarse-graining MCMC
- → Compare H_obs only (not d_L, BAO)
- → Label: KINEMATIC_EFFECTIVE_OBSERVABLE

**If Buckholtz does not clarify:**
- → Operational meaning remains UNCLEAR
- → Cannot design MCMC (don't know which observables apply)
- → Preserve as reproducibility artifact
- → Optionally develop Hamiltonian as independent model

---

## 6. Relation to the Hamiltonian Bridge

### Our Internal Reconstruction

**Formula:**
```
H²(a) = H₀² [Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]
```

**Derivation:** Force F_oP → potential V(a) → energy E = ½μḊ² + V → H²(a)

**Verification status:**
- ✅ Algebraically valid (force scaling, potential integration, monopole limit all pass)
- ✅ Acceleration interpretation: a⁻⁴ can accelerate if Ω_d < 0
- ⚠️ Literature support: PARTIAL (framework exists, MULTING-specific NOT proven)
- ❌ NOT source-confirmed

### Interpretation of Hamiltonian Bridge

**What it may represent:**

**Option A (FLRW-like):**
- Hamiltonian bridge is a **modified Friedmann equation** from MULTING field theory
- H_MULT(z) in Table A1 ≈ output of this Friedmann-like formula
- Ω coefficients are fundamental expansion parameters
- **If confirmed:** MCMC can compare MULTING vs. ΛCDM as alternative cosmologies

**Option B (Effective):**
- Hamiltonian bridge is an **effective description** of cluster dynamics
- H_MULT(z) in Table A1 ≈ emergent observable from coarse-graining
- Ω coefficients are phenomenological averages over cluster ensemble
- **If true:** Need mean-field averaging justification, cannot claim "metric expansion"

**Current status:**
- ❌ NOT source-confirmed → don't know if Option A or B
- ❌ Mean-field averaging gap → Option B lacks rigorous justification
- ⚠️ Cluster variables missing → cannot compute Ω from physics (either option)

**Labels:**

| Aspect | Status |
|--------|--------|
| **Bridge type** | OUR_COMPUTATIONAL_RECONSTRUCTION |
| **Algebraic validity** | ✅ VERIFIED |
| **Source confirmation** | ❌ MISSING |
| **Operational meaning** | ⚠️ AMBIGUOUS (FLRW-like? Effective?) |
| **MCMC readiness** | ❌ BLOCKED (ambiguity + no source confirmation) |

**Key caveat:** The Hamiltonian bridge **may or may not match Buckholtz's intended meaning of H_MULT(z)**. It is one possible interpretation among several, selected because it has the strongest algebraic foundation. But without source confirmation, we cannot claim it represents "MULTING cosmology."

---

## 7. Implications for MCMC Blocker Chain

### Blocker 1 Decomposition

**Previously (docs/54):** Blocker 1 = "Source-Confirmed Bridge Missing"

**Refined understanding:** Blocker 1 actually contains **two sub-questions**:

**Blocker 1a: Bridge Method**
- *Question:* Which computational rule maps F_oP → H_MULT(z)?
- *Candidates:* Phi-scaling / Hamiltonian / Lattice N-body / other
- *Status:* MISSING (Q15 prepared)

**Blocker 1b: Operational Meaning**
- *Question:* What does H_MULT(z) represent physically/observationally?
- *Candidates:* FLRW-like / Kinematic / Phenomenological
- *Status:* UNCLEAR (this memo addresses this)

**Why both are needed:**

Knowing the bridge method (1a) without knowing operational meaning (1b):
- → Can fit H_MULT to Table A1
- → Cannot design MCMC (don't know which observables)
- → Cannot predict (don't know if d_L, BAO apply)

Example:
- Buckholtz confirms Hamiltonian bridge (1a solved)
- But doesn't clarify if H_MULT is metric expansion or effective observable (1b unsolved)
- → Still cannot run MCMC (don't know if we can use Pantheon+ d_L)

**Both must be resolved to unblock MCMC.**

### Updated Blocker Status

| Blocker | Sub-component | Status | Resolution |
|---------|---------------|--------|------------|
| **1a. Bridge method** | Computational rule | ❌ MISSING | Author answers Q15 (which bridge?) |
| **1b. Operational meaning** | Physical interpretation | ❌ UNCLEAR | Author clarifies H_MULT meaning (new question) |
| **2. Cluster variables** | Evolution functions | ❌ MISSING | Author answers Q17 |
| **3. Independent data** | Out-of-sample test | ❌ MISSING | Integrate Pantheon+/BAO |
| **4. Complexity penalty** | AIC/BIC | ❌ MISSING | Implement in MCMC |

**Total resolved:** 0/5 sub-blockers → MCMC remains **BLOCKED**

---

## 8. Safe Author Question

**Context for new clarification question (addition to Q15/Q16):**

We need to understand what H_MULT(z) represents operationally, not just how to compute it.

**Proposed question wording:**

> **Q-operational:** "I may be misunderstanding the operational meaning of H_MULT(z). In FLRW cosmology, H(z) is tied to the scale-factor evolution of the metric (H = ȧ/a) and directly governs observables like luminosity distance and BAO. In MULTING, should H_MULT(z) be understood as:
>
> (a) A true Friedmann-like background expansion rate from modified field equations, operationally equivalent to FLRW H(z),
>
> (b) An effective kinematic measure of the separation rate of large astrophysical structures (analogous to an N-body or lattice-averaged observable),
>
> (c) A phenomenological comparison quantity optimized to match H_obs data, or
>
> (d) Something else?
>
> This affects which observational tests (luminosity distance, BAO, cosmic chronometers) are appropriate for comparing MULTING to ΛCDM."

**Why this wording is safe:**
- ✅ Frames as "I may be misunderstanding" (not "you're wrong")
- ✅ Lists multiple interpretations (not assuming one is correct)
- ✅ Explains why it matters (MCMC design, observables)
- ✅ Respectful, exploratory tone
- ✅ Does NOT call H_MULT "fake" or "misleading"
- ✅ Does NOT claim Buckholtz is wrong

**Where to add:** 
- Append to Q15 as sub-question OR
- Create as separate Q19 in docs/26_author_clarification_brief.md

---

## 9. Unsafe Wording to Avoid

**This memo is INTERNAL — these phrasings should NEVER appear in author-facing communication:**

| ❌ Unsafe Wording | ✅ Safer Wording |
|-------------------|------------------|
| "fake H(z)" | "operationally different H-like quantity" |
| "misleading term" | "potentially ambiguous term" |
| "AI just glued it together" | "AI-assisted phenomenological fitting procedure" |
| "destroys the meaning of H(z)" | "may differ from the FLRW operational meaning" |
| "not real cosmology" | "may be better modeled as effective large-scale structure dynamics" |
| "Buckholtz doesn't understand H(z)" | "the operational meaning of H_MULT is not yet clear to me" |
| "H_MULT is meaningless" | "H_MULT requires clarification of its observational interpretation" |
| "MULTING is wrong" | "MULTING may use a different observable framework than FLRW" |
| "Table A1 proves nothing" | "Table A1 provides retrodictive evidence but not out-of-sample prediction" |
| "you can't compare H_MULT to H_FLRW" | "comparing H_MULT to H_FLRW requires understanding their operational equivalence" |

**Tone guidelines:**
- ✅ Curious, not accusatory
- ✅ Exploratory, not definitive
- ✅ Respectful of author expertise
- ✅ Focused on clarification, not criticism
- ✅ "I may be misunderstanding..." framing

**Internal use only:**
- This memo may use phrases like "operationally different" internally
- But author-facing questions must be even gentler
- Never send this memo to Buckholtz
- Extract only the safe author question (§8) for Q19

---

## 10. Relation to Other Projects / Literature

**This conceptual ambiguity is not unique to MULTING:**

### Historical Precedents

**1. Hubble's Original H₀ (1929):**
- Originally: recession velocity / distance (kinematic)
- Later: scale factor expansion rate (metric)
- Transition required understanding metric expansion vs. peculiar velocities

**2. Structure Formation Literature:**
- "Local H" in clusters ≠ background H
- Peculiar velocities → Doppler shifts mimic expansion
- Requires careful averaging to extract H_background

**3. Lattice Universe Models (Zel'dovich, Irvine):**
- Discrete → continuum averaging
- Effective H_eff from pair dynamics
- Not identical to FLRW H unless averaging justified

**4. Buchert Backreaction:**
- H_D (domain-averaged) ≠ H_FLRW (background)
- Inhomogeneity → effective expansion different from metric
- Requires explicit averaging prescription

**Lesson:** Distinguishing "kinematic separation rate" from "metric expansion rate" is a real conceptual issue in cosmology, not just MULTING-specific.

### Why This Affects MULTING More

**MULTING starts from pairwise forces (not metric):**
- ΛCDM: GR metric → Friedmann → H(z) → structure formation
- MULTING: Structure (forces) → ??? → H_MULT(z)

**Arrow is reversed** → operational meaning less obvious.

**Standard cosmology path:**
```
Metric g_μν → Field equations → H(z) = ȧ/a → Observables (d_L, θ_BAO, etc.)
```

**MULTING path (unclear):**
```
F_oP(r) → ??? (bridge) → H_MULT(z) → ??? (observables)
```

**Central question:** Is the MULTING "bridge" trying to:
- Derive a modified metric → modified H → standard observables? (Interpretation 1)
- Compute effective kinematics → H-like observable → kinematic tests only? (Interpretation 2)
- Fit a comparison function → retrodiction → no prediction? (Interpretation 3)

**This is the core ambiguity.**

---

## 11. Final Status

### Summary Table

| Aspect | Status | Details |
|--------|--------|---------|
| **H_MULT operational meaning** | ❌ **UNCLEAR** | FLRW-like? Kinematic? Phenomenological? |
| **FLRW equivalence** | ❌ **NOT ESTABLISHED** | Cannot assume H_MULT = H in all contexts |
| **Source-confirmed bridge** | ❌ **MISSING** | No explicit F_oP → H_MULT(z) formula |
| **Internal bridge candidate** | ✅ **AVAILABLE** | Hamiltonian H²(a), algebraically valid |
| **Hamiltonian interpretation** | ⚠️ **AMBIGUOUS** | FLRW-like OR effective? |
| **Table A1 status** | ✅ **RETRODICTION_EVIDENCE** | Tracks H_obs well, NOT prediction |
| **MCMC design** | ❌ **BLOCKED** | Don't know which observables apply |
| **Prediction status** | ❌ **BLOCKED** | Don't know if d_L, BAO computable |
| **Author clarification** | ⏳ **REQUIRED** | Q-operational prepared (§8) |

### Impact on MCMC Blocker Chain

**Blocker 1 refined:**
- 1a. Bridge method (computational) → Q15, Q16 prepared
- 1b. Operational meaning (conceptual) → Q-operational prepared (this memo)

**Both required to unblock MCMC.**

### Next Steps

**Priority 1: Author Clarification**
1. Add Q-operational to docs/26_author_clarification_brief.md (as Q19)
2. Wait for author response to first letter
3. Send Q15, Q16, Q19 together (with user approval)

**Priority 2: Conditional MCMC Design**
- **If FLRW-like confirmed:** Implement Hamiltonian MCMC with d_L, BAO, H_obs
- **If kinematic confirmed:** Implement lattice N-body MCMC with H_obs only
- **If phenomenological confirmed:** Document Table A1 as retrodiction, no MCMC

**Priority 3: Internal Work (Allowed Now)**
- Run diagnostic fit on Rows 2-12 (code ready)
- Document overfitting classification
- Prepare MCMC implementation plan (conditional on clarification)

---

## 12. References

**Related project documents:**
- `docs/54_mcmc_blocker_chain.md` — 4 blockers (this memo refines Blocker 1b)
- `docs/53_three_path_hmult_roadmap_safe_memo.md` — 3 bridge candidates
- `docs/48_deep_bridge_independent_verification.md` — Hamiltonian bridge verification
- `docs/47_literature_bridge_map.md` — Lattice universe, Wigner-Seitz, Buchert
- `docs/26_author_clarification_brief.md` — Q14-Q18 prepared

**Literature (conceptual parallels):**
- Buchert, T. (2000) — Domain averaging, H_D vs. H_FLRW
- Zel'dovich, Y.B. (1970) — Lattice universe models
- Irvine, W.M. (1961) — Local irregularities vs. cosmological principle
- Layzer, D. (1963) — Energy equation for cosmological models

**Status:**
- INTERNAL_CONCEPTUAL_MEMO
- HYPOTHESIS_NOT_SOURCE_CONFIRMED
- NOT_FOR_AUTHOR_CRITICISM
- FOR_MCMC_DESIGN_GUIDANCE

---

**Last updated:** 2026-05-29  
**Classification:** INTERNAL_ANALYSIS_ONLY  
**Action required:** Add Q-operational to author clarification brief (Q19)  
**MCMC status:** BLOCKED (0/5 sub-blockers resolved)
