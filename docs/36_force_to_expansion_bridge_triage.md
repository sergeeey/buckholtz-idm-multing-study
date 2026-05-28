# Force-to-Expansion Bridge Triage — F_oP → H(z) Mapping Candidates

**Date:** 2026-05-28  
**Status:** TRIAGE COMPLETE — zero source-supported bridges found  
**Purpose:** Systematic evaluation of all possible routes from pairwise MULTING force law to cosmological expansion

---

## Executive Summary

**What we have:**
1. ✅ Pairwise force-law layer exists: F_oP = F_m - F_d + F_q (SOURCE_CANDIDATE, docs/33)
2. ✅ Heuristic H(z) scaling candidate exists: Phi(z) formula (AI_TRANSCRIPT_REPORTED, docs/35)
3. ❌ Physical closure missing: No source-supported F_oP → H(z) mapping
4. ❌ MCMC blocked: Cannot build forward model H_MULT(z; params) without closure

**Bridge status:**
- **SOURCE_SUPPORTED bridges:** 0 found
- **Computational reconstructions:** 2 candidates (Newtonian dust, parametrized Friedmann)
- **Speculative toy models:** 3 candidates (stress-energy, scalar field, backreaction)
- **Dead ends:** 1 (PPN extrapolation)

**Critical blocker:** Without author clarification on F_oP → H(z) mapping, all bridge routes remain **audit reconstructions** or **speculative proposals**, not implementations of Buckholtz's model.

**Priority 0 question for author:** See Q0 below.

---

## 1. Bridge Candidate Matrix

| Route | Type | Status | Source Support | MCMC Ready | Author Clarification Needed |
|-------|------|--------|----------------|------------|----------------------------|
| **A. Newtonian dust + extra forces** | Computational reconstruction | CANDIDATE | ❌ NO | ❌ NO | YES (Q0) |
| **B. Effective stress-energy tensor** | Speculative toy model | CANDIDATE | ❌ NO | ❌ NO | YES (Q0) |
| **C. Parametrized Friedmann (MGCAMB-style)** | Computational reconstruction | CANDIDATE | ❌ NO | ❌ NO | YES (Q0) |
| **D. Scalar field / dark energy map** | Speculative toy model | CANDIDATE | ❌ NO | ❌ NO | YES (Q0) |
| **E. N-body → fluid backreaction** | Speculative toy model | CANDIDATE | ❌ NO | ❌ NO | YES (Q0) |
| **F. PPN extrapolation to cosmology** | Dead end | REJECTED | ❌ NO | ❌ NO | NO (wrong regime) |

**Key:** All routes except F are **possible in principle**, but **none are source-supported**. Implementing any route without author confirmation = testing **our interpretation**, not **Buckholtz's model**.

---

## 2. Route A — Newtonian Dust + Extra Forces

### Concept
Treat MULTING as Newtonian gravity + post-Newtonian corrections. Average pairwise forces over cosmological fluid.

### Assumptions
1. Dipole and quadrupole forces are perturbations to standard FLRW background
2. Homogeneous averaging preserves dipole/quadrupole contributions (non-standard)
3. Effective equation of state w_eff can capture multipole effects

### Mathematical sketch
```
ρ_total = ρ_m + ρ_dipole + ρ_quadrupole
P_total = P_m + P_dipole + P_quadrupole
H² = (8πG/3)(ρ_total) + ...
```

### Critical nuance
**Standard homogeneous Newtonian averaging nulls dipole/quadrupole background contributions** (spatial gradients average to zero in FRW symmetry).

This is **not a refutation** of MULTING. It means:
- Either MULTING uses a non-standard averaging prescription (e.g., backreaction framework, inhomogeneous cosmology)
- OR dipole/quadrupole enter as effective stress-energy components (not geometric averaging)
- OR MULTING is formulated differently (metric modification, not force averaging)

**Status:** Computational reconstruction (can be implemented), but **unknown if this matches Buckholtz's intent**.

### Code permission
- allowed_for_toy_model_only
- not_allowed_for_mcmc (without author confirmation)
- not_allowed_for_prediction (audit reconstruction, not source model)

### Author clarification needed
Q0: "Does MULTING use standard homogeneous averaging, or a non-standard prescription (e.g., backreaction, effective stress-energy tensor)?"

---

## 3. Route B — Effective Stress-Energy Tensor Averaging

### Concept
Map pairwise forces to effective stress-energy tensor T_μν^(eff), then use Einstein field equations.

### Assumptions
1. MULTING forces correspond to effective energy density and pressure
2. Dipole = anisotropic stress or bulk viscosity
3. Quadrupole = higher-order tensor structure

### Mathematical sketch
```
T_μν^(eff) = T_μν^(dust) + T_μν^(dipole) + T_μν^(quadrupole)
G_μν = 8πG T_μν^(eff)
→ Friedmann equations with w_eff(z)
```

### Status
Speculative toy model. **No source material** indicates MULTING uses stress-energy formalism.

### Critical question
What is the **physical mechanism** mapping F_d to T_μν^(dipole)? Is dipole a force between objects, or a spacetime curvature contribution?

If dipole = DM-DM scattering force → stress-energy map unclear.  
If dipole = metric modification → need weak-field expansion.

### Code permission
- allowed_for_speculative_toy_model
- not_allowed_for_mcmc (speculative, not source-supported)
- not_allowed_for_buckholtz_model_validation (our proposal, not his)

### Author clarification needed
Q0: "Is MULTING formulated as modified gravity (metric), or modified matter (stress-energy)?"

---

## 4. Route C — Parametrized Friedmann (MGCAMB-style)

### Concept
Bypass physical derivation. Parametrize H²(z) as phenomenological function of (beta_d, beta_q, cosmological params).

### Assumptions
1. H²(z) = H₀² [Ωₘ(1+z)³ + ΩΛ + f(z; beta_d, beta_q)]
2. f(z) chosen to fit observations
3. No physical mechanism — just effective description

### Examples
- Modified growth: f(z) ~ beta_d × (1+z)^α
- Extra dark energy: f(z) ~ beta_q × (1+z)^β
- Coupled components: f(z) ~ beta_d × beta_q × interaction_term

### Status
Computational reconstruction. **Can be implemented immediately**, but:
- Arbitrary functional form (infinite choices)
- No connection to pairwise force law (F_oP unused)
- Phenomenology, not physics

### Code permission
- allowed_for_fit_reproduction_only (if matches Table A1)
- not_allowed_for_prediction (overfitting risk)
- not_allowed_for_mcmc (arbitrary form without physical justification)

### Why this is NOT the heuristic closure candidate
Heuristic candidate (docs/35) has **specific structure**: Phi(z) = A_m - A_d + A_q, sign structure matches force law.

Route C is **generic parametrization** without force-law connection.

### Author clarification needed
Q0: "Is there a specific functional form H²(z; beta_d, beta_q), or is parametrized Friedmann the intended approach?"

---

## 5. Route D — Scalar Field / Dark Energy Map

### Concept
Interpret dipole/quadrupole as scalar field (quintessence, k-essence) or dark energy component.

### Assumptions
1. Dipole → kinetic term φ̇²
2. Quadrupole → potential V(φ)
3. Scalar field evolution drives H(z)

### Mathematical sketch
```
ρ_φ = (1/2)φ̇² + V(φ)
P_φ = (1/2)φ̇² - V(φ)
H² = (8πG/3)(ρ_m + ρ_φ)
```

### Status
Speculative toy model. **No source material** indicates MULTING uses scalar field formalism.

### Critical question
Why would pairwise gravitational forces (F_m, F_d, F_q) map to scalar field? Mechanism unclear.

### Code permission
- allowed_for_speculative_exploration
- not_allowed_for_mcmc (speculative, no source support)
- not_allowed_for_buckholtz_model_claims (our proposal, not his framework)

### Author clarification needed
Q0: "Does MULTING involve scalar fields, or is it purely gravitational (metric/force)?"

---

## 6. Route E — N-body → Fluid Backreaction

### Concept
Use N-body simulations with MULTING forces, extract emergent H(z) from spatial averaging (backreaction framework).

### Assumptions
1. Pairwise forces implemented in N-body code
2. Spatial averaging of inhomogeneous spacetime gives effective H(z)
3. Backreaction ≠ 0 (breaks FLRW assumption)

### Mathematical sketch
```
Simulate N particles with F_oP = F_m - F_d + F_q
Extract <ρ>, <P>, <H²> from simulation volume
Compare with FLRW H²_eff
```

### Status
Speculative toy model. **Computationally expensive**, and **no source indication** this is Buckholtz's approach.

### Critical question
Does MULTING **require** inhomogeneous cosmology, or does it admit FLRW background?

If FLRW symmetry preserved → backreaction framework unnecessary.  
If FLRW broken → need inhomogeneous field equations.

### Code permission
- allowed_for_computational_exploration (research code)
- not_allowed_for_mcmc (no analytical forward model)
- not_allowed_for_buckholtz_model_validation (speculative route)

### Author clarification needed
Q0: "Does MULTING preserve FLRW symmetry, or does it require inhomogeneous cosmology?"

---

## 7. Route F — PPN Extrapolation to Cosmology (DEAD END)

### Concept
Extract PPN parameters (γ, β) from local MULTING forces, extrapolate to cosmological scales.

### Why DEAD END
1. PPN is **weak-field, slow-velocity** expansion. Cosmology is **strong curvature, relativistic**.
2. PPN parameters (γ, β) describe **local** metric perturbations (Solar System, r ~ AU). Cosmological H(z) operates at r ~ Gpc.
3. If dipole ~ 4.5 Mpc scale → negligible at r ~ AU → γ = 1, β = 1 (GR recovered) → no cosmological effect.
4. If dipole operates at AU scales → **violates Solar System constraints** (Cassini: γ - 1 < 10⁻⁵).

**Verdict:** PPN extrapolation **cannot connect local tests to cosmological expansion**. Wrong regime, wrong scales.

### Status
REJECTED. Do not pursue.

### Code permission
- not_allowed (wrong physics regime)

---

## 8. Critical Nuance — Standard Averaging vs Non-Standard

**Standard FLRW assumption:** Universe is homogeneous and isotropic on large scales (cosmological principle).

**Implication for MULTING:**
- Dipole force F_d has directional dependence → breaks isotropy locally
- Quadrupole force F_q has angular dependence → breaks isotropy locally
- **Standard spatial averaging over homogeneous distribution → dipole and quadrupole contributions average to zero**

**This is NOT a refutation of MULTING.** It means one of the following:

### Option 1: Non-standard averaging prescription
MULTING may use backreaction framework, where:
- Spatial averaging ≠ volume averaging
- Inhomogeneities contribute to effective cosmology
- <H²> ≠ H²_FLRW

**Examples:** Buchert formalism, Q-cosmology, timescape cosmology.

**Status:** Possible, but **no source material** indicates MULTING uses backreaction.

### Option 2: Effective stress-energy formalism
Dipole/quadrupole enter as effective T_μν components, not geometric averaging.

**Example:** Dipole = bulk viscosity ζ, quadrupole = anisotropic stress π_μν.

**Status:** Possible, but **no source material** indicates stress-energy formalism.

### Option 3: Cluster-scale only (not cosmological background)
Dipole/quadrupole operate at cluster scales (r ~ Mpc), but **do not contribute to cosmic background H(z)**.

H(z) from monopole only (standard Newtonian gravity).  
Dipole/quadrupole modify cluster dynamics, not expansion rate.

**Status:** Possible, but **contradicts Table A1** (which shows H_MULT ≠ H_FLRW).

### Option 4: Metric modification (not force averaging)
MULTING is not Newtonian + forces, but **modified metric** (like f(R) gravity, TeVeS).

Dipole/quadrupole are metric coefficients, not force components.

**Status:** Possible, but **requires weak-field expansion** to connect to cosmology.

**Conclusion:** Without author clarification, we cannot determine which (if any) of these options applies.

---

## 9. Priority 0 Author Question (Q0)

**Q0: Force-to-Expansion Mapping**

> "How does the pairwise MULTING force law F_oP = F_m - F_d + F_q translate into a cosmological background expansion equation H(z)?
> 
> Specifically:
> 1. Is there a modified Friedmann equation derived from MULTING field equations?
> 2. Is there an effective stress-energy tensor T_μν^(eff) that maps forces to expansion?
> 3. Is there a spatial averaging prescription (e.g., backreaction framework) that connects cluster-scale forces to H(z)?
> 4. Or is H_MULT(z) a phenomenological parametrization independent of the pairwise force law?
> 
> Understanding this mapping is **critical** for implementing MCMC parameter estimation and distinguishing MULTING predictions from ΛCDM."

**Why this is Priority 0:**
- All other questions (beta provenance, PPN checks, microphysics) depend on knowing F_oP → H(z) route
- Without this, we cannot build forward model H_MULT(z; params)
- MCMC remains blocked until Q0 is answered

**Expected answer formats:**
- "See Equation X in manuscript Y" → implement that equation
- "Use averaging prescription Z" → implement that prescription
- "Parametrized Friedmann with f(z) = ..." → implement that function
- "Still being derived" → mark as blocker, wait
- "Proprietary / unpublished" → mark as blocker, document limitation

---

## 10. Safe vs Unsafe Wording

### ✅ Safe Wording (Use This)

> "The pairwise MULTING force law is documented (SOURCE_CANDIDATE), but the mapping from F_oP to cosmological expansion H(z) is not found in available materials. Without author clarification, we cannot determine whether MULTING uses standard Friedmann equations, modified gravity, effective stress-energy, or a backreaction framework. MCMC parameter estimation remains blocked pending Q0 clarification."

> "Standard homogeneous averaging would null dipole/quadrupole background contributions. This does not refute MULTING — it indicates a non-standard averaging prescription or effective formalism may be required. Author clarification needed."

> "Six possible bridge routes exist (Newtonian dust, stress-energy, parametrized Friedmann, scalar field, backreaction, PPN). None are source-supported. Implementing any route without confirmation = testing our interpretation, not Buckholtz's model."

> "Table reproduction candidate exists (Phi(z) heuristic, docs/35), but it requires cluster variable table. This is phenomenological scaling, not physical closure."

### ❌ Unsafe Wording (DO NOT Use)

❌ "MULTING is refuted because homogeneous averaging nulls dipole."  
→ **Why unsafe:** Assumes standard averaging without confirming Buckholtz's approach.

❌ "The model is inconsistent — no bridge from F_oP to H(z) exists."  
→ **Why unsafe:** Bridge may exist in unpublished work or different formalism.

❌ "We proved MULTING cannot work."  
→ **Why unsafe:** We documented **absence of source material**, not physical impossibility.

❌ "PPN rules out MULTING."  
→ **Why unsafe:** PPN checks blocked (no weak-field limit available). Cannot rule out what we haven't tested.

❌ "The force law is wrong."  
→ **Why unsafe:** Force law is SOURCE_CANDIDATE (awaiting manual verification). Status ≠ SOURCE_INCORRECT.

❌ "Buckholtz doesn't understand cosmology."  
→ **Why unsafe:** Ad hominem. We audit **work**, not **author**.

---

## 11. MCMC Blocker Summary

### What MCMC Requires
1. Forward model: H_MULT(z; beta_d, beta_q, ...) computable for any z
2. Physical mapping: F_oP → H(z) via identified bridge route
3. Parameter vector: (beta_d, beta_q, Ωₘ, ...) with priors
4. Likelihood: P(H_obs | H_MULT(z; params))
5. Independent data: NOT used to derive params (out-of-sample)

### What We Have
1. ❌ No forward model (bridge route unknown)
2. ❌ No physical mapping (6 candidates, 0 source-supported)
3. ⚠️ Two parameters identified (beta_d, beta_q), but provenance = fitted (not predictive)
4. ❌ No likelihood (depends on #1)
5. ⚠️ Data available (cosmic chronometers, Pantheon+), but not yet used

### Blocker Chain
```
No Q0 answer
  ↓
No F_oP → H(z) mapping
  ↓
No forward model H_MULT(z; params)
  ↓
No MCMC
```

**Critical path:** Q0 must be answered before MCMC can proceed.

---

## 12. Code Permission Summary

| Bridge Route | Code Permission | MCMC Allowed | Predictive Use Allowed |
|--------------|-----------------|--------------|------------------------|
| A. Newtonian dust + extra forces | allowed_for_toy_model_only | ❌ NO | ❌ NO |
| B. Effective stress-energy | allowed_for_speculative_exploration | ❌ NO | ❌ NO |
| C. Parametrized Friedmann | allowed_for_fit_reproduction_only | ❌ NO | ❌ NO |
| D. Scalar field / dark energy | allowed_for_speculative_exploration | ❌ NO | ❌ NO |
| E. N-body backreaction | allowed_for_computational_research | ❌ NO | ❌ NO |
| F. PPN extrapolation | not_allowed | ❌ NO | ❌ NO |

**Hard rule:** NO bridge route is allowed for MCMC or predictive modeling until Q0 is answered and source-supported route identified.

---

## 13. Relationship to Existing Findings

### Finding 3 — H_MULT Formula Missing
**Status:** STILL BLOCKED.

Bridge triage **confirms** this blocker. No source-supported F_oP → H(z) mapping found.

### Finding 12 — Force-Law Layer Found
**Status:** Consistent.

Force-law layer exists, but **closure missing**. Bridge triage documents why closure is missing (no source material on averaging/mapping).

### Finding 13 — Heuristic Closure Candidate
**Status:** Complementary.

Heuristic Phi(z) scaling (docs/35) is **one possible bridge** (phenomenological parametrization), but:
- Not source-confirmed (AI_TRANSCRIPT_REPORTED)
- Requires cluster variables (not provided)
- Phenomenological (fitted, not derived)

Bridge triage shows **5 other possible routes** (A, B, D, E, F), none source-supported.

---

## 14. Next Actions

### If Q0 Answered — Source-Supported Route
1. Implement bridge route as `src/force_to_expansion_bridge.py`
2. Build forward model `H_MULT(z; params)`
3. Upgrade status: bridge route → SOURCE_CONFIRMED
4. Unblock MCMC: implement likelihood, priors, sampler
5. Run fit on cosmic chronometers / Pantheon+
6. Compare MULTING vs ΛCDM (AIC, BIC)

### If Q0 Not Answered — Continue Audit
1. Mark bridge as BLOCKER in all docs
2. Document: "MCMC blocked pending Q0"
3. Archive bridge candidates as speculative
4. Focus on other findings (PPN, BBN, SIDM — if applicable)
5. Publish repository as incomplete but transparent

### If "Still Being Derived"
1. Respect author's timeline
2. Mark as blocker with expected timeline
3. Implement toy models (A, C) as placeholders
4. Note: toy models test **our reconstruction**, not **Buckholtz's model**

### If "Proprietary / Unpublished"
1. Document blocker explicitly
2. Note: reproducibility audit cannot proceed without public formula
3. Archive repository as incomplete
4. No MCMC, no model comparison

---

## 15. Relationship to Minimum Viable Bridge Candidate (MVB)

**Status:** This document (docs/36) evaluates all possible bridge routes. A separate document (docs/37_discrete_lattice_mvb_hypothesis.md) develops the strongest non-source-supported route in detail.

**What docs/36 does:**
- Systematic triage of 6 bridge routes (A-F)
- Classifies each as SOURCE_SUPPORTED / COMPUTATIONAL_RECONSTRUCTION / SPECULATIVE_TOY_MODEL / DEAD_END
- Documents Q0 priority question
- Enforces MCMC blocker

**What docs/37 does:**
- Develops one route (discrete lattice + virial pressure) from first principles
- Documents 10 required inputs, 5 risks, architecture, mathematical sketch
- Proposes Q_MVB author clarification question
- Status: RESEARCH_HYPOTHESIS (not source-supported)

**Critical distinction:**
- docs/36 = comprehensive survey of all routes → **ZERO source-supported**
- docs/37 = detailed development of strongest candidate → **STILL not source-supported**

**Does MVB change MCMC readiness?**
- **NO.** MVB is a research hypothesis / computational reconstruction candidate.
- MCMC remains BLOCKED until Q0 or Q_MVB answered and route source-confirmed.
- Implementing MVB without author confirmation = testing our interpretation, not Buckholtz's model.

**Relationship to heuristic Phi(z) closure (Finding 13):**

| Aspect | Heuristic Phi(z) (docs/35) | MVB discrete lattice (docs/37) |
|--------|----------------------------|--------------------------------|
| **Origin** | AI transcript materials | First-principles virial theorem |
| **Type** | Phenomenological parametrization | Mechanistic reconstruction |
| **Status** | AI_TRANSCRIPT_REPORTED | RESEARCH_HYPOTHESIS |
| **Inputs** | Cluster amplitudes A_m, A_d, A_q | Lattice geometry, neighbor count, virial sum |
| **Strength** | May reproduce Table A1 if cluster vars exist | Physically motivated, testable mechanism |

Both are **computational reconstruction candidates**. Neither is source-supported. Q0 and Q_MVB together ask author to choose/confirm bridge route.

**Summary:**
- docs/36: evaluated 6 routes → 0 source-supported → Q0 blocker identified
- docs/37: developed 1 candidate route → still not source-supported → Q_MVB proposed
- Source-supported bridges: **ZERO** (unchanged)
- MCMC readiness: **BLOCKED** (unchanged)

---

## 16. Document Status

**Triage status:** COMPLETE — all bridge routes evaluated (6 total: A-F)

**Source-supported bridges:** 0 found (unchanged after MVB development)

**Priority 0 question:** Q0 drafted (see section 9)

**MVB question:** Q_MVB drafted (see docs/37, docs/26 section 2c)

**MCMC readiness:** BLOCKED (no source-confirmed F_oP → H(z) mapping)

**Safe to share with Dr. Buckholtz:** YES (respectful framing, factual triage, no refutation claims)

**High-risk artifacts:** This doc is medium-risk (factual but "zero source-supported" sounds negative). Only share after trust established. MVB (docs/37) is high-risk (OUR reconstruction, not his model) — do NOT send early.

**Next action:** Send Q0 to author (see docs/26), wait for response. Q_MVB is optional long-horizon question (only ask if Q0-Q4 answered and trust established).

---

**Last updated:** 2026-05-28  
**Requires:** Q0 answer from Dr. Buckholtz (or Q_MVB if he prefers mechanistic route)  
**Blocks:** MCMC parameter estimation, predictive modeling, model comparison  
**Unblocks:** (pending Q0/Q_MVB answer) forward model implementation, likelihood construction
