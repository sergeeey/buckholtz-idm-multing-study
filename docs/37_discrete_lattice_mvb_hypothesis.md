# Discrete Lattice + Virial Pressure MVB Hypothesis

**Date:** 2026-05-28  
**Status:** RESEARCH_HYPOTHESIS — computational reconstruction candidate, NOT source-supported  
**Purpose:** Document strongest candidate bridge route F_oP → H(z) pending author clarification

**CRITICAL:** This is **NOT** confirmed Buckholtz theory. This is a research hypothesis for computational reconstruction. MCMC remains blocked.

---

## Executive Summary

**What we have:**
1. ✅ Pairwise force law: F_oP = F_m - F_d + F_q (SOURCE_CANDIDATE)
2. ✅ AI heuristic closure: Phi(z) scaling (AI_TRANSCRIPT_REPORTED, table-reproduction only)
3. ❌ Source-supported F_oP → H(z) bridge: MISSING
4. ⚠️ **MVB candidate:** Discrete lattice + virial pressure route (RESEARCH_HYPOTHESIS)

**Bridge status:**
- **Source-supported routes:** 0 found
- **MVB candidate routes:** 1 (discrete lattice + virial pressure)
- **MCMC-ready routes:** 0
- **Prediction-allowed routes:** 0

**Critical distinction:**
- **Source-supported bridge:** Confirmed in Buckholtz materials → implement his model
- **MVB candidate:** Research hypothesis / computational reconstruction → may become **our** model, not his

**MCMC status:** BLOCKED until source-supported bridge identified or MVB confirmed by author

---

## 1. MVB Architecture — Discrete Lattice + Virial Pressure Route

### Step-by-Step Mapping

```
Pairwise MULTING force law (F_oP = F_m - F_d + F_q)
  ↓
Impose discrete topology (cluster lattice / Wigner-Seitz cells)
  ↓
Define clusters as cells/nodes at comoving positions
  ↓
Restrict interactions to nearest neighbors (reduce O(N²) → O(N))
  ↓
Compute pairwise MULTING forces between neighbors
  ↓
Calculate virial pressure: P_virial = -⟨r · F⟩ / (3V)
  ↓
Derive effective fluid: ρ_eff, P_eff from virial theorem
  ↓
Insert into Friedmann acceleration equation: ä/a = -(4πG/3)(ρ_eff + 3P_eff)
  ↓
Solve for H(z) = ȧ/a
```

### Physical Motivation

**Why discrete lattice?**
- MULTING operates at cluster scales (r ~ Mpc)
- Clusters naturally form discrete structures (cosmic web nodes)
- Lattice approximation: Wigner-Seitz cells around each cluster
- Reduces computational complexity from O(N²) pairwise to O(N) nearest-neighbor

**Why virial pressure?**
- Virial theorem connects pairwise forces to thermodynamic pressure
- Standard route: kinetic theory → collisionless Boltzmann → fluid approximation
- Virial pressure bypasses kinetic theory (clusters don't "collide" like gas particles)
- Direct map: ⟨r · F⟩ → pressure contribution

**Why Friedmann acceleration?**
- Standard cosmology uses Friedmann **equations** (2 equations: H² and ä/a)
- Friedmann **acceleration equation** is more fundamental (derived from stress-energy conservation)
- ä/a = -(4πG/3)(ρ + 3P) connects fluid to expansion directly
- H²(z) can be derived from ä/a by integration

---

## 2. Required Missing Inputs (10 Critical Items)

| Input | Description | Status | Blocker | Priority |
|-------|-------------|--------|---------|----------|
| **Lattice geometry** | FCC? BCC? hexagonal? irregular Voronoi? | MISSING | Cannot define neighbors without geometry | HIGH |
| **Neighbor count** | How many nearest neighbors per cluster? | MISSING | Virial sum depends on neighbor count | HIGH |
| **Cell volume** | Volume of Wigner-Seitz cell | MISSING | Pressure = Force/Volume requires V | HIGH |
| **Cluster mass function** | m_A(z) evolution | MISSING | F_m depends on m_A | CRITICAL |
| **Kinetic energy k_A(z)** | Sub-object kinetic energy scale | MISSING | F_d, F_q depend on k_A | CRITICAL |
| **Characteristic radius r_A(z)** | Cluster size evolution | MISSING | r_dA = beta_d × r_A | CRITICAL |
| **Comoving distance D_C:AB(z)** | Neighbor separation | COMPUTABLE | Standard cosmology, but which neighbors? | MEDIUM |
| **Virial pressure formula** | How ⟨r · F⟩ → P_virial? | MISSING | Multiple conventions exist | HIGH |
| **Energy-density mapping** | How virial → ρ_eff? | MISSING | ρ + 3P in Friedmann requires both | HIGH |
| **Validation dataset** | Independent H(z) measurements | AVAILABLE | Cosmic chronometers, but MCMC blocked | LOW |

**Critical blocker:** Without cluster mass function m_A(z), k_A(z), r_A(z), cannot evaluate F_oP → cannot compute virial pressure → cannot derive H(z).

---

## 3. Mathematical Sketch

### Step 1: Discrete Lattice Setup

Assume N clusters at comoving positions **r**_i(t) in expanding universe.

Lattice spacing: L ~ (V_universe / N)^(1/3) ~ few Mpc (typical cluster separation)

Each cluster A has:
- Mass: m_A
- Radius: r_A
- Kinetic energy scale: k_A
- Nearest neighbors: B₁, B₂, ..., B_n (n = neighbor count)

### Step 2: Pairwise MULTING Forces

For cluster A and neighbor B:

```
r_AB = |r_A - r_B|  (comoving separation)

F_m = G m_A m_B / r_AB²

F_d = G c⁻² (k_A m_B |r_dA| + k_B m_A |r_dB|) / r_AB³
      where r_dA = beta_d × r_A, r_dB = beta_d × r_B

F_q = G k_A k_B c⁻⁴ |r_qAB|² / r_AB⁴
      where |r_qAB|² = beta_q² × r_A × r_B

F_oP = F_m - F_d + F_q
```

Total force on A:
```
F_A = Σ_{B∈neighbors} F_oP(A,B) r̂_AB
```

### Step 3: Virial Pressure

Virial theorem (time-averaged):
```
⟨r · F⟩ = -3 ⟨P⟩ V
```

For discrete lattice:
```
P_virial(A) = -(1/3V_cell) Σ_{B∈neighbors} r_AB · F_oP(A,B)
```

where V_cell = Wigner-Seitz cell volume around A.

### Step 4: Effective Fluid

**Energy density:**
```
ρ_eff = ρ_clusters + ρ_virial_contribution
ρ_clusters = Σ m_A / V_total  (standard cluster mass density)
ρ_virial_contribution = ???  (MISSING — how virial forces contribute to ρ)
```

**Pressure:**
```
P_eff = P_virial = ⟨P_virial(A)⟩_ensemble
```

### Step 5: Friedmann Acceleration

```
ä/a = -(4πG/3)(ρ_eff + 3P_eff)
```

If ρ_eff and P_eff known as functions of a (or z), integrate:

```
H²(z) = (ȧ/a)² = ∫ 2(ä/a) d(ln a)
```

Compare with ΛCDM:
```
H²_ΛCDM(z) = H₀² [Ωₘ(1+z)³ + ΩΛ]
```

---

## 4. Status Labels (Enforce in Code)

### Primary Status
- **RESEARCH_HYPOTHESIS** — This is a research proposal, not confirmed Buckholtz theory
- **COMPUTATIONAL_RECONSTRUCTION_CANDIDATE** — Can be implemented, but interpretation is ours
- **NOT_SOURCE_SUPPORTED** — No manuscript material confirms this route

### Use Permissions
- **NOT_ALLOWED_FOR_PREDICTION** — Cannot predict H(z) on new data without author confirmation
- **NOT_ALLOWED_FOR_MCMC** — Cannot run parameter estimation without source support
- **ALLOWED_FOR_TOY_MODEL_EXPLORATION** — Can implement as research code to test feasibility

### Code Permission Guards
```python
def is_mcmc_allowed() -> bool:
    return False  # Always False until source-supported

def is_prediction_allowed() -> bool:
    return False  # Always False until source-supported

def is_source_supported() -> bool:
    return False  # MVB is research hypothesis, not confirmed theory
```

---

## 5. Risk Section (Why This May Fail / Mislead)

### Risk 1: May Become "Our Model", Not Buckholtz's
**Concern:** Implementing MVB without author confirmation = testing **our interpretation**, not **his model**.

**Consequence:** If we claim "MULTING validated" based on MVB results, we're validating **our reconstruction**, not Buckholtz's theory.

**Mitigation:** Explicitly label all MVB results as "computational reconstruction candidate" with source_supported=False.

---

### Risk 2: Backreaction May Be Small
**Concern:** Virial pressure from MULTING forces may be negligible compared to standard FLRW background.

**Why:** If dipole/quadrupole forces are ~1% corrections to monopole (Newtonian gravity), virial pressure contribution to ä/a may be <1% → indistinguishable from ΛCDM within observational uncertainties.

**Test:** Compute P_virial / P_matter ratio. If <<1 → backreaction negligible → MULTING reduces to ΛCDM → no predictive power.

**Consequence:** MVB may work mathematically but have zero distinguishable effect on H(z).

---

### Risk 3: Lattice Topology May Violate Homogeneity
**Concern:** Imposing discrete lattice (FCC, BCC, Voronoi) breaks statistical isotropy → violates cosmological principle.

**Why:** Real universe is statistically isotropic on large scales (CMB, large-scale structure). Lattice has preferred directions (lattice vectors).

**Consequence:** MVB may predict anisotropic H(z) → ruled out by CMB isotropy (ΔT/T ~ 10⁻⁵).

**Mitigation:** Average over all lattice orientations, or use irregular Voronoi tessellation (closer to real cosmic web).

---

### Risk 4: Parameter Degeneracy with Cluster Evolution
**Concern:** m_A(z), r_A(z), k_A(z) are free functions. Can tune them to fit any H(z) dataset.

**Why:** Three unknown functions + beta_d + beta_q = effectively infinite free parameters → can fit anything.

**Consequence:** MVB becomes overfitting machine, not physical model.

**Mitigation:** Require independent observational constraints on m_A(z), r_A(z), k_A(z) (e.g., cluster mass function from X-ray/SZ surveys, cluster size evolution from weak lensing).

---

### Risk 5: No Author Confirmation
**Concern:** Buckholtz may have a completely different F_oP → H(z) mapping in mind.

**Why:** MVB is our reconstruction. He may use: scalar field, modified metric, backreaction framework, or phenomenological parametrization.

**Consequence:** We build MVB, author says "that's not my model" → wasted effort, misleading claims.

**Mitigation:** Send MVB hypothesis to author as **question**, not **implementation**. Ask: "Is discrete lattice + virial pressure your intended route, or do you have a different mapping?"

---

## 6. Safe vs Unsafe Wording

### ✅ Safe Wording (Use This)

> "A candidate bridge route from F_oP to H(z) is the discrete lattice + virial pressure approach, where clusters form a lattice, pairwise MULTING forces generate virial pressure, and effective fluid drives Friedmann acceleration. This is a **research hypothesis** and **computational reconstruction candidate**, not source-supported Buckholtz theory. Implementing this route requires author clarification on lattice geometry, cluster mass function, and virial pressure formula. MCMC remains blocked until source support confirmed."

> "The MVB (Minimum Viable Bridge) is the strongest candidate route among evaluated options, but it is **not validated** and **not source-confirmed**. It may become **our model**, not Buckholtz's model, if implemented without confirmation."

> "This approach is **allowed for toy model exploration** to test feasibility, but **not allowed for MCMC parameter estimation** or **predictive modeling** without author confirmation."

---

### ❌ Unsafe Wording (DO NOT Use)

❌ "This solves the F_oP → H(z) bridge problem."  
→ **Why unsafe:** MVB is candidate, not solution. Solution requires source support.

❌ "We proved MULTING is viable."  
→ **Why unsafe:** Testing MVB ≠ proving MULTING. We're testing **our reconstruction**, not his theory.

❌ "This is the only physically valid path from F_oP to H(z)."  
→ **Why unsafe:** Other routes exist (stress-energy, scalar field, backreaction). MVB is one candidate among many.

❌ "Formal validation of discrete lattice approach."  
→ **Why unsafe:** No validation performed. MVB is hypothesis, not validated theory.

❌ "MCMC-ready implementation."  
→ **Why unsafe:** MCMC explicitly blocked (is_mcmc_allowed() = False) until source support.

❌ "Buckholtz's discrete lattice model."  
→ **Why unsafe:** This is **our** reconstruction hypothesis. No confirmation it's his model.

---

## 7. Author Clarification Question (Minimum Required)

**Q_MVB: Discrete Lattice + Virial Pressure Route**

> "One possible route from the pairwise MULTING force law F_oP = F_m - F_d + F_q to cosmological expansion H(z) is:
> 
> 1. Impose discrete topology: clusters arranged in lattice or Voronoi tessellation
> 2. Compute pairwise MULTING forces between nearest neighbors
> 3. Calculate virial pressure: P_virial = -⟨r · F⟩ / (3V)
> 4. Derive effective fluid (ρ_eff, P_eff) from virial theorem
> 5. Insert into Friedmann acceleration equation: ä/a = -(4πG/3)(ρ_eff + 3P_eff)
> 6. Solve for H(z)
> 
> Is this discrete lattice + virial pressure approach your intended mapping, or do you have a different route in mind?
> 
> If discrete lattice is correct, could you clarify:
> - Lattice geometry (FCC, BCC, Voronoi)?
> - Neighbor count?
> - Virial pressure formula convention?
> - Cluster mass function m_A(z)?
> - Kinetic energy scale k_A(z)?
> - Characteristic radius r_A(z)?"

**Why this question is critical:**
- Distinguishes MVB (our hypothesis) from Buckholtz's model (his theory)
- Prevents wasted implementation effort if route is wrong
- Unblocks MCMC if route is confirmed
- Documents blocker if route is rejected

---

## 8. Comparison with Other Bridge Routes

| Route | MVB Score | Why MVB Ranked Higher / Lower |
|-------|-----------|-------------------------------|
| **A. Newtonian dust + extra forces** | MVB ≈ A | Both use force → pressure mapping. MVB adds discrete lattice (more specific). |
| **B. Effective stress-energy tensor** | MVB > B | MVB has concrete prescription (virial theorem). B is abstract (no formula). |
| **C. Parametrized Friedmann** | MVB > C | MVB derives H(z) from physics. C is phenomenological (arbitrary f(z)). |
| **D. Scalar field / dark energy** | MVB > D | MVB uses pairwise forces. D abandons force law (unmotivated). |
| **E. N-body → fluid backreaction** | MVB < E | E is rigorous (simulation-based). MVB is analytical approximation. But E is computationally expensive. |
| **F. PPN extrapolation** | MVB >> F | F is dead end (wrong regime). MVB is viable candidate. |

**Why MVB is strongest candidate among A-E:**
- Concrete prescription (virial theorem)
- Uses pairwise force law (unlike C, D)
- Analytically tractable (unlike E)
- Physically motivated (discrete cosmic web topology)

**Why MVB is NOT guaranteed correct:**
- Not source-supported
- Lattice assumption may break homogeneity
- Virial backreaction may be negligible
- Parameter degeneracy with cluster evolution

---

## 9. What MVB Unblocks (If Source-Confirmed)

### If Buckholtz confirms discrete lattice + virial pressure route:

1. **Implement MVB forward model**
   - Build lattice generator (FCC, BCC, or Voronoi)
   - Compute nearest-neighbor forces
   - Calculate virial pressure
   - Solve Friedmann acceleration for H(z)

2. **Upgrade status**
   - MVB: RESEARCH_HYPOTHESIS → SOURCE_CONFIRMED
   - Code permission: toy_model_only → allowed_for_mcmc

3. **Unblock MCMC**
   - Define parameter vector: (beta_d, beta_q, Ωₘ, lattice_spacing, ...)
   - Specify priors
   - Implement likelihood: P(H_obs | H_MVB(z; params))
   - Run sampler (emcee, PyMC, Stan)

4. **Model comparison**
   - Fit MVB to cosmic chronometers / Pantheon+ / DESI
   - Compute AIC, BIC
   - Compare MVB vs ΛCDM (which fits better? which is simpler?)

5. **Validation**
   - Train/test split
   - Cross-validation
   - Out-of-sample predictions
   - Posterior predictive checks

---

## 10. What Remains Blocked (Even If MVB Confirmed)

### Even with source-confirmed MVB, the following remain MISSING:

1. **Cluster mass function m_A(z)**
   - Need independent observational constraint (X-ray, SZ, weak lensing)
   - If free parameter → overfitting risk

2. **Kinetic energy scale k_A(z)**
   - Definition unclear (sub-object kinetic energy? galaxy velocities?)
   - Need operational definition or observational proxy

3. **Characteristic radius r_A(z)**
   - Virial radius? Half-mass radius? Core radius?
   - Need prescription or observational constraint

4. **Lattice geometry**
   - FCC? BCC? Irregular Voronoi?
   - Different geometries → different neighbor counts → different H(z)

5. **Virial pressure convention**
   - Multiple definitions exist (time-averaged, volume-averaged, comoving vs physical)
   - Need exact formula

6. **Uncertainty estimates**
   - How uncertainties in m_A, k_A, r_A propagate to σ(H_MULT)?
   - Need error propagation formula

7. **Cosmological initial conditions**
   - Lattice at z=0? z=1100? Evolving?
   - Need prescription for lattice evolution

---

## 11. MVB Feasibility Check (Before Implementation)

**Before implementing MVB, answer these questions:**

### Q1: Is virial backreaction large enough to detect?
**Test:** Estimate P_virial / P_matter ~ (F_d + F_q) / F_m.  
**Threshold:** If <1% → indistinguishable from ΛCDM → not worth implementing.

### Q2: Does lattice break isotropy?
**Test:** Compute angular correlation function of H(z) on sky for FCC lattice.  
**Threshold:** If anisotropy >10⁻⁵ → violates CMB isotropy → dead end.

### Q3: How many free parameters?
**Count:** beta_d, beta_q, lattice_spacing, m_A(z), k_A(z), r_A(z), ...  
**Threshold:** If >5 free parameters → overfitting risk → need strong priors.

### Q4: Can we validate cluster inputs independently?
**Check:** Do X-ray/SZ surveys provide m_A(z)? Does weak lensing provide r_A(z)?  
**Threshold:** If no independent constraints → cannot distinguish MVB from arbitrary fit.

### Q5: What does ΛCDM predict for same observables?
**Baseline:** Fit ΛCDM (2 parameters: Ωₘ, H₀) to same dataset.  
**Threshold:** If MVB ≈ ΛCDM within uncertainties → no gain in explanatory power.

---

## 12. Document Status

**Hypothesis status:** RESEARCH_HYPOTHESIS — computational reconstruction candidate

**Source support:** NOT_SOURCE_SUPPORTED — zero manuscript material confirms this route

**MCMC readiness:** BLOCKED — not allowed until source-confirmed

**Prediction readiness:** BLOCKED — not allowed until source-confirmed

**Toy model status:** ALLOWED — can implement as research code to test feasibility

**Author clarification:** REQUIRED — Q_MVB must be answered before proceeding

**Safe to share with Dr. Buckholtz:** YES (framed as question, not claim)

**High-risk artifacts:** None (this is hypothesis documentation, not implementation)

**Next action:** Send Q_MVB to author, await response

---

**Last updated:** 2026-05-28  
**Requires:** Author clarification on discrete lattice + virial pressure route  
**Blocks:** MCMC, predictive modeling (until source-confirmed)  
**Unblocks:** (if confirmed) MVB implementation, forward model, MCMC setup
