# Three-Path H_MULT Roadmap — Safe Internal Decision Memo

**Date:** 2026-05-29  
**Status:** INTERNAL_DECISION_MEMO  
**Purpose:** Document three possible routes to H_MULT(z) without overclaiming

---

## Executive Summary

**Context:** Appendix A1 Step 6 states "AI service" generates H_MULT candidates but does not provide explicit H_MULT(z) formula or bridge method. We identified three possible computational interpretations.

**Key findings:**
- ✅ Force law F_oP = F_m - F_d + F_q is SOURCE_CONFIRMED
- ✅ Table A1 transcribed, H_MULT fits H_obs 6× better than H_FLRW (retrodiction)
- ⚠️ No H_MULT(z) formula is source-confirmed yet
- ⚠️ Hamiltonian bridge is strongest INTERNAL_RECONSTRUCTION but NOT confirmed by Buckholtz
- ❌ MCMC remains BLOCKED as Buckholtz-theory validation
- ✅ INTERNAL_DIAGNOSTIC_FIT_ONLY is allowed with safety labels

**Three possible routes:**
1. **Phi-scaling / AI heuristic** — table reproduction, physically under-specified
2. **Hamiltonian bridge** — algebraically valid, NOT source-confirmed
3. **Discrete lattice / N-body** — physically interesting, data-heavy, defer

**Recommendation:** Use Hamiltonian for internal diagnostic fit only. Wait for author confirmation before MCMC or prediction.

---

## Path 1: Phi-scaling / AI Heuristic

### Formula

```
H_MULT(z) = Φ(z) × H_FLRW(z)

where Φ(z) is a smooth scaling function fitted to H_obs
```

### Status Labels

| Label | Status |
|-------|--------|
| **TABLE_REPRODUCTION_HEURISTIC_ONLY** | ✅ Yes |
| **AI_INTERPRETATION_CANDIDATE** | ✅ Yes |
| **NOT_PHYSICAL_BRIDGE** | ✅ Correct |
| **NOT_ALLOWED_FOR_PREDICTION** | ✅ Blocked |
| **SOURCE_CONFIRMED** | ❌ No |

### Description

**What it is:**
- Phenomenological scaling function Φ(z) that adjusts H_FLRW to match H_obs
- Could be polynomial, spline, or neural network
- "AI service" in Step 6 might refer to this approach

**Why it reproduces Table A1:**
- By construction: fit Φ(z) to minimize |H_MULT - H_obs|
- High flexibility: any smooth function can be expressed as Φ
- Low parameter count if Φ is simple (e.g., polynomial degree 3)

**Why it is under-specified as a physical bridge:**
- Dimensional analysis: Φ(z) is dimensionless ratio, not derived from force law
- Missing ingredients:
  - Length scale (how do pairwise forces → background H?)
  - Averaging rule (single pair → ensemble?)
  - Connection to F_oP, β_d, β_q unclear
- Status: heuristic curve-fit, not first-principles derivation

**Careful wording:** NOT "dimensionally incorrect" but "dimensionally / physically under-specified because the length-scale and averaging rule are not explicit."

### Use cases

**Allowed:**
- ✅ Interpreting Table A1 structure (how Φ(z) deviates from 1.0)
- ✅ Comparing H_MULT shape vs. ΛCDM
- ✅ Quick visualization

**Not allowed:**
- ❌ Prediction on new z (Φ fitted to Table A1 only)
- ❌ MCMC as Buckholtz validation (not a physical model)
- ❌ Claiming this is "the bridge" without author confirmation

### Verdict

**Classification:** TABLE_REPRODUCTION_HEURISTIC_ONLY

**Recommendation:** Use only for Table A1 interpretation. Do NOT use for MCMC or prediction until author confirms this is the intended method.

---

## Path 2: Hamiltonian Bridge

### Formula

```
H²(a) = H₀² [Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]

where:
  a = 1/(1+z)  (scale factor)
  Ω_k = coefficient from integration constant E
  Ω_m = coefficient from monopole potential V_m ∝ a⁻¹
  Ω_d = coefficient from dipole potential V_d ∝ a⁻²
  Ω_q = coefficient from quadrupole potential V_q ∝ a⁻³
```

### Status Labels

| Label | Status |
|-------|--------|
| **BEST_INTERNAL_RECONSTRUCTION_CANDIDATE** | ✅ Yes |
| **ALGEBRAICALLY_VALID** | ✅ Verified |
| **NOT_SOURCE_CONFIRMED** | ⚠️ True |
| **AUTHOR_CONFIRMATION_REQUIRED** | ⚠️ Required |
| **MCMC_BLOCKED** | ❌ Blocked |
| **PREDICTION_BLOCKED** | ❌ Blocked |

### Derivation Path

**Step 1:** Start from pairwise energy
```
E = ½μḊ² + V_MULT(D)

where V_MULT = V_m + V_d + V_q
```

**Step 2:** Integrate forces F(r) → potentials V(a)
- F_m ∝ r⁻² (monopole) → V_m ∝ a⁻¹
- F_d ∝ r⁻³ (dipole) → V_d ∝ a⁻²
- F_q ∝ r⁻⁴ (quadrupole) → V_q ∝ a⁻³

**Step 3:** Substitute D = a(t)D₀ into energy equation
```
½(Ḋ/D)² = E/D² - V_MULT/D²

→ ½H² = E/(a²D₀²) - [V_m/(aD₀) + V_d/(a²D₀²) + V_q/(a³D₀³)]
```

**Step 4:** Identify Ω coefficients
- Ω_k from integration constant E
- Ω_m from monopole potential V_m
- Ω_d from dipole potential V_d
- Ω_q from quadrupole potential V_q

### Verification Results

**Algebraic checks (all passed):**
- ✅ Force scaling F_m ∝ r⁻², F_d ∝ r⁻³, F_q ∝ r⁻⁴ (SOURCE_CONFIRMED)
- ✅ Force → potential integration dV/dr = -F(r) verified
- ✅ Potential → H² derivation V(a) → H²(a) checked
- ✅ Monopole-only limit: β_d=0, β_q=0 → Ω_k a⁻² + Ω_m a⁻³ (Friedmann-like)
- ✅ Sign analysis: dipole repulsive → Ω_d < 0 possible
- ✅ Acceleration interpretation: a⁻⁴ can accelerate if Ω_d < 0

**Files:**
- `docs/48_deep_bridge_independent_verification.md` (19 KB, 9-part verification)
- `src/deep_bridge_verification.py` (complete implementation)
- `tests/test_deep_bridge_verification.py` (41 tests, all passing)

### Acceleration Physics

**Corrected formula:** ä/a = H²(1 - n/2) for H² = C a⁻ⁿ

| Term | n | Factor | ä/a contribution | Interpretation |
|------|---|--------|------------------|----------------|
| a⁻² | 2 | 0 | 0 × Ω_k H₀² a⁻² | NEUTRAL (curvature) |
| a⁻³ | 3 | -0.5 | -0.5 × Ω_m H₀² a⁻³ | Deceleration if Ω_m > 0 |
| a⁻⁴ | 4 | -1.0 | -1.0 × Ω_d H₀² a⁻⁴ | **ACCELERATION if Ω_d < 0** ✅ |
| a⁻⁵ | 5 | -1.5 | -1.5 × Ω_q H₀² a⁻⁵ | Strong deceleration if Ω_q > 0 |

**Key insight:** Three-era structure (deceleration → borderline → acceleration) is physically plausible if dipole dominates late times with Ω_d < 0.

### Literature Support

**Status:** PARTIAL_SUPPORT

| Framework | Support | Strength | Caveat |
|-----------|---------|----------|--------|
| Layzer-Irvine energy conservation | ✅ | STRONG | Applies to N-body, not single pair |
| Lattice universe discrete→continuum | ✅ | PARTIAL | Requires homogeneity assumption |
| Wigner-Seitz cell pair→background | ✅ | PARTIAL | Valid only for periodic lattices |
| Buchert backreaction | ✅ | BACKGROUND | Does not endorse specific potentials |

**What literature provides:**
- ✅ Energy conservation framework (Layzer-Irvine)
- ✅ Discrete → continuum averaging concept (lattice universe)
- ✅ Pair → cell → background idea (Wigner-Seitz)

**What literature does NOT provide:**
- ❌ MULTING-specific dipole/quadrupole validation
- ❌ Single pair → background generalization proof
- ❌ Mean-field averaging justification

**File:** `docs/47_literature_bridge_map.md` (14.8 KB)

### Gaps and Limitations

**Gap 1: Mean-field averaging**
- **Issue:** Single pair E = ½μḊ² + V → background H²(a) leap not rigorously justified
- **What's missing:** Statistical mechanics averaging over cluster ensemble
- **Impact:** Cannot claim bridge is "derived from first principles" without this

**Gap 2: Cluster variables missing**
- **Missing:** m_A(z), k_A(z), r_A(z), D_AB(z), N_eff evolution
- **Impact:** Cannot compute Ω coefficients from physics
- **Status:** Fit coefficients are phenomenological parameters, not physics-derived

**Gap 3: Source confirmation**
- **Issue:** Appendix A1 does not specify Hamiltonian approach
- **Impact:** This is OUR_COMPUTATIONAL_RECONSTRUCTION, not Buckholtz's confirmed method
- **Required:** Author confirmation via Q16

### Use Cases

**Allowed:**
- ✅ Internal diagnostic fit on Table A1 Rows 2–12 (INTERNAL_DIAGNOSTIC_FIT_ONLY)
- ✅ Leave-one-out stability analysis
- ✅ Comparison against polynomial baseline
- ✅ Overfitting classification (expected: UNDERDETERMINED)
- ✅ Documenting algebraic consistency

**Not allowed:**
- ❌ MCMC as Buckholtz validation (bridge not source-confirmed)
- ❌ Prediction on new z (cluster variables missing, not source-confirmed)
- ❌ Public claim of "validated bridge"
- ❌ Calling this "Buckholtz formula" (it's OUR reconstruction)
- ❌ Bayesian evidence comparison against ΛCDM (requires source confirmation first)

### Verdict

**Classification:** BEST_INTERNAL_RECONSTRUCTION_CANDIDATE

**Strengths:**
- Algebraically valid (force → potential → H² derivation passes)
- Physically motivated (energy conservation)
- Acceleration mechanism plausible (dipole with Ω_d < 0)
- Monopole-only limit reduces to Friedmann

**Weaknesses:**
- Not source-confirmed
- Mean-field averaging gap
- Cluster variables missing
- Literature support partial

**Recommendation:** Use for INTERNAL_DIAGNOSTIC_FIT_ONLY. Prepare Q16 for author confirmation. If confirmed → implement cluster variable evolution → run full MCMC. If not confirmed → document as interesting reconstruction but not Buckholtz's method.

---

## Path 3: Discrete Lattice / N-body Bridge

### Formula

```
ä/a = N_eff × F_oP / (μ × D_AB)

where:
  ä/a = acceleration parameter (second derivative of scale factor)
  N_eff = effective number of cluster pairs per background volume
  F_oP = F_m - F_d + F_q (pairwise force, SOURCE_CONFIRMED)
  μ = reduced mass
  D_AB = cluster separation
```

### Status Labels

| Label | Status |
|-------|--------|
| **RESEARCH_PATH** | ✅ Yes |
| **PHYSICALLY_INTERESTING** | ✅ Yes |
| **DATA_HEAVY** | ⚠️ True |
| **NOT_NEXT_STEP** | ✅ Defer |
| **SOURCE_CONFIRMED** | ❌ No |

### Description

**What it is:**
- Direct acceleration bridge: pairwise force → background acceleration
- Dimensional bridge: ä/a has dimensions [T⁻²], F_oP/μ has [LT⁻²], so need D_AB⁻¹ to match
- N_eff accounts for cluster number density and averaging

**Why it's physically interesting:**
- ✅ Most direct force → expansion mapping
- ✅ Could be tested via N-body simulation
- ✅ Explicitly shows how discrete forces → continuous H(z)

**Why it's data-heavy:**
- Requires cluster variable evolution:
  - m_A(z), k_A(z), r_A(z) (cluster A properties)
  - m_P(z), k_P(z), r_P(z) (cluster P properties)
  - D_AB(z) (separation evolution)
  - N_eff(z) (effective pair density)
- Requires statistical averaging over cluster distribution
- Requires verification via N-body simulation

### Comparison to Hamiltonian Bridge

| Aspect | Hamiltonian | Discrete Lattice |
|--------|-------------|------------------|
| **Derivation start** | Energy E = ½μḊ² + V | Force F_oP directly |
| **Bridge equation** | H² from energy | ä/a from acceleration |
| **Integration step** | F → V → H² | F → ä/a → H² |
| **Cluster variables** | Needed for Ω coefficients | Needed for N_eff, D_AB |
| **Data requirements** | Medium (Ω fit possible) | High (need full cluster evolution) |
| **Simulation testable** | Harder (energy conservation check) | Easier (direct N-body test) |

### Use Cases

**Future research:**
- ✅ N-body simulation of MULTING forces
- ✅ Testing force → expansion causality directly
- ✅ Independent verification of Hamiltonian bridge

**Not economical now:**
- ❌ Requires extensive cluster data (not in manuscript)
- ❌ Requires N-body simulation setup (weeks of work)
- ❌ Hamiltonian bridge already provides H²(a) form
- ❌ Author confirmation still needed regardless of which bridge

### Verdict

**Classification:** RESEARCH_PATH, defer until cluster variables available

**Strengths:**
- Most direct force → expansion mapping
- Simulation-testable
- Physically transparent

**Weaknesses:**
- Data-heavy (cluster variables needed)
- Simulation setup required
- Not more source-confirmed than Hamiltonian

**Recommendation:** Document as interesting alternative. Defer implementation until:
1. Author confirms any bridge method
2. Cluster variables provided or inferred
3. Hamiltonian bridge tested first (lower data requirements)

---

## Decision Matrix

| Path | Use now? | Purpose | Risk | Status |
|------|----------|---------|------|--------|
| **Phi-scaling** | ⚠️ LIMITED | Table A1 interpretation only | Overclaiming as physics | TABLE_HEURISTIC |
| **Hamiltonian** | ✅ YES | Internal diagnostic fit Rows 2–12 | Not source-confirmed | BEST_INTERNAL_CANDIDATE |
| **Lattice N-body** | ❌ DEFER | Future simulation research | Data-heavy, not urgent | RESEARCH_PATH |

### Recommended Actions by Path

**Phi-scaling (Path 1):**
- ✅ Use for quick Table A1 visualization
- ✅ Document as heuristic interpretation
- ❌ Do NOT use for MCMC or prediction
- ❌ Do NOT claim as physical bridge without author confirmation

**Hamiltonian (Path 2):**
- ✅ Run internal diagnostic fit on Rows 2–12
- ✅ Document overfitting classification (expected: UNDERDETERMINED)
- ✅ Compare against polynomial baseline
- ✅ Prepare Q16 for author confirmation
- ❌ Do NOT run MCMC as Buckholtz validation yet
- ❌ Do NOT predict new z without source confirmation

**Lattice N-body (Path 3):**
- ✅ Document as future research direction
- ✅ Include in author question (Q15) as alternative interpretation
- ❌ Do NOT implement until cluster variables available
- ❌ Do NOT prioritize over Hamiltonian (less economical)

---

## Safe Next Actions (Prioritized)

### Priority 1: Immediate (No Author Input Needed)

1. **Run internal diagnostic fit (Hamiltonian, Rows 2–12)**
   ```python
   from src.deep_bridge_diagnostic_fit import run_full_diagnostic
   report = run_full_diagnostic()
   ```
   - Label: INTERNAL_DIAGNOSTIC_FIT_ONLY
   - Document: overfitting classification, stability, baseline comparison
   - Expected: UNDERDETERMINED (11 points / 4 params)

2. **Fix remaining 3 diagnostic fit tests**
   - Current status: 152/155 passing
   - Impact: Test suite 100% clean
   - Effort: <30 min

3. **Extract reusable assets**
   - Epistemic Registry Framework (score 19/20)
   - Scientific Table Auditor (score 18/20)
   - Respectful Clarification Template (score 18/20)

### Priority 2: Waiting for Author Response

4. **Send Q14-Q18 (user approval required)**
   - Q14: Row 1 sigma convention
   - Q15: Bridge method identification ← **includes three-path question**
   - Q16: Hamiltonian confirmation
   - Q17: Cluster variables
   - Q18: Acceleration mechanism

5. **If author confirms Hamiltonian:**
   - Request cluster variable evolution functions
   - Implement Ω coefficient calculation from physics
   - Re-run diagnostic fit with physics-derived priors
   - Prepare prediction test on new z (if independent data available)

6. **If author specifies different bridge:**
   - Update derivation to match
   - Re-verify algebraically
   - Update Q16-Q18 based on new understanding

### Priority 3: Blocked Until Source Confirmation

7. **MCMC parameter inference** (BLOCKED)
   - Blocker 1: Bridge not source-confirmed
   - Blocker 2: Cluster variables missing
   - Blocker 3: 11 data points / 4 params = underdetermined

8. **Prediction on new z** (BLOCKED)
   - Blocker 1: Bridge not source-confirmed
   - Blocker 2: Cluster variables missing
   - Blocker 3: Cannot compute Ω from physics

9. **Public validation claim** (FORBIDDEN)
   - Blocker 1: Not source-confirmed
   - Blocker 2: No independent test set
   - Blocker 3: Author approval required

---

## Forbidden Actions (Reminder)

**Do NOT do the following without author confirmation:**
- ❌ Run MCMC as Buckholtz-theory validation
- ❌ Predict H(z) at new redshifts
- ❌ Claim bridge is "validated" or "proved"
- ❌ Call Hamiltonian bridge "Buckholtz formula" (it's OUR reconstruction)
- ❌ Post Table A1 analysis publicly
- ❌ Compare Bayesian evidence MULTING vs. ΛCDM
- ❌ Send Q14-Q18 without user approval
- ❌ Use word "discovery"

**Safe wording:**
- ✅ "Internal reconstruction"
- ✅ "Candidate bridge"
- ✅ "Algebraically consistent"
- ✅ "Diagnostic fit" (not "validation")
- ✅ "Source-unconfirmed"
- ✅ "Awaiting author confirmation"

---

## Author-Facing Distilled Question (for Q15)

**Context for Q15:** We explored three computational interpretations of the F_oP → H_MULT(z) bridge after finding that Appendix A1 Step 6 does not provide an explicit formula.

**Proposed Q15 text:**

> "I explored three possible computational interpretations of how F_oP might connect to H_MULT(z):
>
> **(a) Phi-scaling heuristic:** H_MULT = Φ(z) × H_FLRW, where Φ is a smooth scaling function fitted to H_obs. This reproduces Table A1 well but is dimensionally under-specified as a first-principles bridge because the length-scale and averaging rule are not explicit.
>
> **(b) Hamiltonian energy bridge:** Starting from pairwise energy E = ½μḊ² + V_MULT(D), integrating forces to potentials (F_m ∝ r⁻² → V_m ∝ a⁻¹, etc.), and deriving H²(a) = H₀²[Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]. This passes algebraic verification (force scaling, monopole-only limit, sign analysis) but I do not assume it is your intended method.
>
> **(c) Discrete lattice acceleration bridge:** ä/a = N_eff × F_oP/(μ × D_AB), mapping pairwise acceleration directly to background. This would require cluster variable evolution (m_A(z), D_AB(z), N_eff) not provided in the manuscript.
>
> Is Table A1 H_MULT closer to one of these interpretations, or based on a different computational rule? If the Hamiltonian approach is close, are cluster variable evolution functions available for computing the Ω coefficients from first principles?"

**Why this wording is safe:**
- ✅ Frames as "my exploration", not "your error"
- ✅ Lists multiple interpretations (not assuming one is right)
- ✅ Explains each without overclaiming
- ✅ Uses "dimensionally under-specified" not "incorrect"
- ✅ States Hamiltonian is NOT assumed to be Buckholtz's method
- ✅ Asks respectfully for clarification
- ✅ Does NOT claim validation or discovery

---

## Comparison to Original Overclaiming Draft

**If there was an earlier draft with overclaiming, this memo corrects it by:**

### Removed Overclaims

❌ **"Path 1 is dimensionally incorrect"**  
→ ✅ **"Path 1 is dimensionally under-specified as a first-principles bridge"**

❌ **"Hamiltonian bridge is the correct method"**  
→ ✅ **"Hamiltonian is best INTERNAL_RECONSTRUCTION_CANDIDATE, NOT source-confirmed"**

❌ **"We can now run MCMC"**  
→ ✅ **"MCMC remains BLOCKED until source confirmation"**

❌ **"Buckholtz formula"**  
→ ✅ **"OUR_COMPUTATIONAL_RECONSTRUCTION, awaiting confirmation"**

❌ **"Lattice bridge is wrong"**  
→ ✅ **"Lattice bridge is RESEARCH_PATH, defer until data available"**

### Added Safety Labels

- ✅ INTERNAL_DIAGNOSTIC_FIT_ONLY for all fits
- ✅ NOT_SOURCE_CONFIRMED for all bridges
- ✅ MCMC_BLOCKED explicitly stated
- ✅ PREDICTION_BLOCKED explicitly stated
- ✅ AUTHOR_CONFIRMATION_REQUIRED before proceeding

### Added Caveats

- ✅ Mean-field averaging gap documented
- ✅ Cluster variables missing documented
- ✅ Literature support: PARTIAL, not full
- ✅ 11 data points / 4 params = UNDERDETERMINED expected
- ✅ Retrodiction vs. prediction clarified

---

## References

**Related documents:**
- `docs/43_bridge_candidate_math_stress_test.md` — 6 bridge families evaluated
- `docs/46_deep_bridge_research_sprint.md` — Hamiltonian derivation
- `docs/47_literature_bridge_map.md` — Layzer-Irvine, lattice universe support
- `docs/48_deep_bridge_independent_verification.md` — 9-part algebraic verification
- `docs/50_deep_bridge_diagnostic_fit_rows_2_12.md` — Fit documentation
- `docs/26_author_clarification_brief.md` — Q14-Q18 prepared

**Status files:**
- `docs/51_repo_waiting_state_checklist.md` — Current project state
- `docs/52_reusable_assets_harvest.md` — Asset extraction roadmap

---

## Conclusion

**Three paths identified:**
1. Phi-scaling (heuristic, table-only)
2. Hamiltonian (algebraically valid, NOT source-confirmed)
3. Lattice N-body (research path, defer)

**Recommended path:** Hamiltonian for INTERNAL_DIAGNOSTIC_FIT_ONLY.

**Blocked until author confirmation:**
- MCMC as Buckholtz validation
- Prediction on new z
- Public validation claim

**Safe next action:** Run internal diagnostic fit, prepare Q15 with three-path question, wait for Buckholtz response.

---

**Last updated:** 2026-05-29  
**Status:** SAFE_INTERNAL_MEMO_COMPLETE  
**Next step:** Wait for author response to first letter, then send Q15 with three-path question if appropriate
