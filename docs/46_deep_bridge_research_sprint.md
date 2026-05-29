# Deep Bridge Research Sprint — Hamiltonian Reconstruction

**Date:** 2026-05-29 (pre-verification)  
**Status:** OUR_COMPUTATIONAL_RECONSTRUCTION (NOT source-confirmed)  
**Goal:** Derive H²(a) from MULTING pairwise force law via energy conservation

---

## Executive Summary

**Proposed formula:**
```
H²(a) = H₀² [Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]
```

**Derivation route:** Energy conservation E = ½μḊ² + V_MULT(D) → H²(a)

**Status:**
- ✅ Algebraically consistent (pending verification)
- ⚠️ Physical interpretation requires mean-field justification
- ❌ NOT source-confirmed (awaiting Buckholtz confirmation)
- ❌ MCMC BLOCKED (missing cluster variable evolution)

**Literature support:**
- Layzer-Irvine equation (energy conservation framework)
- Lattice universe models (discrete → continuum averaging)
- Wigner-Seitz cell approximation (pair → cell → background)
- Buchert/backreaction (inhomogeneity effects)

---

## Part 1: Starting Point — MULTING Pairwise Force Law

**Source-confirmed formulas** (from manuscript Appendix A.1):

```
F_oP = F_m - F_d + F_q

where:
  F_m = G m_A m_P / r²           (monopole, r⁻²)
  F_d = G c⁻² (k_A m_P |r_dA| + k_P m_A |r_dP|) / r³   (dipole, r⁻³)
  F_q = G k_A k_P c⁻⁴ |r_qAB|² / r⁴   (quadrupole, r⁻⁴)
```

**Beta length scales:**
- r_dA = β_d × r_A (β_d = 4.5 from Table A1)
- r_dP = β_d × r_P
- |r_qAB|² = β_q² × r_A × r_P (β_q = 18.0 from Table A1)

**Sign structure:**
- Monopole: attractive (−)
- Dipole: subtractive in F_oP → repulsive if F_d > 0
- Quadrupole: attractive (−)

---

## Part 2: Force → Potential Integration

**Method:** F(r) = −dV/dr

### Monopole Potential

**Force:** F_m = −G m_A m_P / r²

**Potential:**
```
V_m(r) = −∫ F_m dr = −G m_A m_P / r
```

**Scaling:** r = a(t) r₀ → V_m(a) ∝ a⁻¹

### Dipole Potential

**Force:** F_d = +C_d / r³ (repulsive)

**Potential:**
```
V_d(r) = −∫ F_d dr = +C_d / (2r²)

where C_d = G c⁻² (k_A m_P |r_dA| + k_P m_A |r_dP|)
```

**Scaling:** V_d(a) ∝ a⁻²

**Sign:** Positive (repulsive potential raises total energy)

### Quadrupole Potential

**Force:** F_q = −C_q / r⁴ (attractive)

**Potential:**
```
V_q(r) = −∫ F_q dr = −C_q / (3r³)

where C_q = G k_A k_P c⁻⁴ |r_qAB|²
```

**Scaling:** V_q(a) ∝ a⁻³

**Sign:** Negative (attractive potential lowers total energy)

### Total Potential

```
V_MULT(r) = V_m + V_d + V_q
          = −G m_A m_P / r  +  C_d / (2r²)  −  C_q / (3r³)
```

**Scaling with a(t):**
```
V_MULT(a) = A_m a⁻¹ + A_d a⁻² + A_q a⁻³

where:
  A_m = −G m_A m_P / D₀
  A_d = +C_d / (2D₀²)
  A_q = −C_q / (3D₀³)
```

---

## Part 3: Energy Conservation → H²(a) Derivation

**Starting equation:** Energy conservation for pairwise interaction

```
E = (1/2) μ Ḋ² + V_MULT(D)
```

Where:
- μ = reduced mass = (m_A m_P) / (m_A + m_P)
- D = inter-cluster distance = a(t) D₀ (comoving assumption)
- Ḋ = D₀ ȧ(t)

**Substitution:**
```
E = (1/2) μ (D₀ ȧ)² + V_MULT(a D₀)
```

**Rearrange for H²:**
```
(1/2) μ D₀² ȧ² = E − V_MULT(a D₀)

ȧ² = (2/μ D₀²) [E − V_MULT(a D₀)]

H² = (ȧ/a)² = (1/a²) × (2/μ D₀²) [E − V_MULT(a D₀)]
```

**Expand V_MULT:**
```
V_MULT(a) = A_m a⁻¹ + A_d a⁻² + A_q a⁻³
```

**Substitute:**
```
H² = (2/μ D₀²) × (1/a²) [E − A_m a⁻¹ − A_d a⁻² − A_q a⁻³]

H² = (2E/μ D₀²) a⁻²  −  (2A_m/μ D₀²) a⁻³  −  (2A_d/μ D₀²) a⁻⁴  −  (2A_q/μ D₀²) a⁻⁵
```

**Normalization:**
```
H²(a) = H₀² [Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]
```

**Coefficient identification:**

| Term | Source | Coefficient | Physical interpretation |
|------|--------|-------------|------------------------|
| a⁻² | E (integration constant) | Ω_k = 2E / (H₀² μ D₀²) | Curvature-like / kinetic |
| a⁻³ | V_m (monopole) | Ω_m = −2A_m / (H₀² μ D₀²) | Matter-like (attractive) |
| a⁻⁴ | V_d (dipole) | Ω_d = −2A_d / (H₀² μ D₀²) | Dipole (repulsive if A_d > 0) |
| a⁻⁵ | V_q (quadrupole) | Ω_q = −2A_q / (H₀² μ D₀²) | Quadrupole (attractive if A_q < 0) |

---

## Part 4: Physical Interpretation

### 4.1 Monopole-Only Limit

**Set β_d = 0, β_q = 0:**
```
H²(a) = Ω_k a⁻² + Ω_m a⁻³
```

**Interpretation:**
- a⁻³ term = matter-like (standard Friedmann)
- a⁻² term = curvature / integration constant E

**Comparison with ΛCDM:**
```
H²_ΛCDM(a) = H₀² [Ω_k a⁻² + Ω_m a⁻³ + Ω_Λ]
```

**Difference:** No Λ term in MULTING — acceleration explained via dipole, not cosmological constant.

### 4.2 Acceleration Analysis

**Acceleration equation:**
```
ä/a = −(1/2) d(H²)/d(ln a) − H²
```

**Contribution from each term:**

| Term | d(ln H²)/d(ln a) | ä/a contribution |
|------|-----------------|------------------|
| a⁻² | −2 | +1 × H² (acceleration-like) |
| a⁻³ | −3 | +0.5 × H² (deceleration) |
| a⁻⁴ | −4 | 0 (NEUTRAL) ⚠️ |
| a⁻⁵ | −5 | −0.5 × H² (deceleration) |

**Key finding:** a⁻⁴ term (dipole) is **NEUTRAL** for ä/a, NOT strongly accelerating.

**Implication:** Late-time acceleration requires:
- Positive Ω_k domination (curvature-driven, unusual)
- OR specific Ω coefficient balance (delicate tuning)

### 4.3 Era Structure

**Proposed three eras:**

1. **Early time (a << 1):** a⁻⁵ (quadrupole) dominates → deceleration
2. **Mid time (a ~ 1):** a⁻⁴ (dipole) emerges → neutral (borderline)
3. **Late time (a > 1):** a⁻² (curvature) vs a⁻³ (matter) balance → depends on Ω_k sign

**Note:** This era structure requires numerical fit to verify.

---

## Part 5: Assumptions and Limitations

### Critical Assumptions

1. **D = a(t) D₀** — comoving inter-cluster distance
   - Neglects peculiar velocities
   - Assumes Hubble flow dominates

2. **E = constant** — energy conservation
   - No energy injection/dissipation
   - Closed system approximation

3. **Single pair → background** — mean-field leap
   - Requires N-body → fluid averaging justification
   - Lattice universe models provide framework (see docs/47)

4. **μ, D₀ constants** — no z-evolution
   - Cluster masses fixed
   - Comoving distance normalization fixed

### Limitations

1. **Physical justification incomplete:**
   - Single pair interaction ≠ cosmological background
   - Requires Wigner-Seitz cell or virial theorem extension

2. **Cluster variable evolution missing:**
   - m_A(z), k_A(z), r_A(z) not provided
   - Cannot compute Ω coefficients without these

3. **Diagnostic fit stability unknown:**
   - 11 data points (Rows 2–12), 5 parameters
   - High risk of overfitting (degrees of freedom = 6)

4. **NOT source-confirmed:**
   - This is our computational reconstruction
   - May differ from Buckholtz's intended route

---

## Part 6: Comparison with Alternative Bridges

| Bridge | Formula | Status | Pros | Cons |
|--------|---------|--------|------|------|
| **B (Discrete Lattice ODE)** | ä/a = N_eff × F_oP/(μ×D_AB) | ALTERNATIVE | Direct force → accel | Requires N_eff averaging |
| **G (Hamiltonian, this doc)** | H² from energy conservation | THIS DOC | Standard physics framework | Single pair → background leap |
| **B+G Hybrid** | Combine lattice + Hamiltonian | POSSIBLE | Best of both | Complex, two-layer |
| **Phi(z) Heuristic** | H²∝ Φ(z) scaling | TABLE_ONLY | Reproduces Table A1 | No physical bridge |

**This document focuses on Candidate G (Hamiltonian/energy conservation route).**

---

## Part 7: Diagnostic Fit Plan (NOT YET EXECUTED)

**When source-confirmed OR approved for internal test:**

### Data
- Use Table A1 Rows 2–12 (exclude Row 1 = SOURCE_TABLE_OUTLIER)
- Target: H_MULT from table (not H_obs — avoid circularity)
- z range: 0.06 to 8.5

### Free Parameters
1. H₀ (normalization)
2. Ω_k (curvature/kinetic)
3. Ω_m (matter-like, monopole)
4. Ω_d (dipole)
5. Ω_q (quadrupole)

**Total: 5 parameters, 11 data points → 6 degrees of freedom**

### Fit Variants
A. **Unconstrained least squares**
B. **Sign-constrained:**
   - Ω_m ≥ 0 (matter attractive)
   - Ω_q ≥ 0 (quadrupole attractive)
   - Ω_d sign from derivation (if A_d > 0 → Ω_d < 0)
C. **Leave-one-out cross-validation**
D. **Comparison baselines:**
   - Polynomial: H² = c₀ + c₁(1+z) + c₂(1+z)² + c₃(1+z)³
   - ΛCDM: H² = H₀²[Ω_m(1+z)³ + Ω_Λ]
   - H_FLRW from Table A1 (no fit)

### Overfitting Checks
- AIC/BIC penalty
- Condition number (parameter degeneracy)
- Leave-one-out error
- Residual sum of squares

### Success Criteria (Internal Test Only)
- Residuals < 5% of H_MULT
- Leave-one-out error < 10%
- Condition number < 1000
- No negative H² in fit range

**Classification:**
- **ROBUST:** LOO < 5%, cond < 100
- **FLEXIBLE_CURVE_FIT:** LOO 5–15%, cond 100–1000
- **UNDERDETERMINED:** LOO > 15%, cond > 1000
- **FAILED:** Negative H², diverging parameters

---

## Part 8: What This Does NOT Mean

**If diagnostic fit passes (internal test only):**

❌ This does NOT prove MULTING is correct  
❌ This does NOT validate the theory  
❌ This does NOT refute ΛCDM  
❌ This does NOT confirm the formula is Buckholtz's  
❌ This does NOT enable prediction on new z  
❌ This does NOT justify MCMC on cosmological datasets  

**What it DOES mean:**
✅ The algebraic derivation is internally consistent  
✅ The formula can reproduce Table A1 (fitted data)  
✅ The H²(a) structure is plausible as a phenomenological model  
✅ Further investigation (author confirmation, cluster variables) is warranted  

---

## Part 9: Safety Notes

### Allowed Wording
- "Internal reconstruction"
- "Candidate bridge"
- "Algebraically consistent"
- "Diagnostic fit" (not "validation")
- "Source-unconfirmed"
- "Phenomenological model"

### Forbidden Wording
- "Validated"
- "Proved"
- "Solved"
- "Confirmed bridge"
- "Buckholtz formula" (until confirmed)
- "Discovery"
- "Prediction" (blocked)

### MCMC and Prediction Status
- ❌ **MCMC BLOCKED** — not source-confirmed, missing cluster variables
- ❌ **PREDICTION BLOCKED** — cannot generalize to new z without m_A(z), k_A(z), r_A(z)
- ✅ **DIAGNOSTIC FIT ALLOWED** — internal test on Rows 2–12 only (if approved)

---

## Part 10: Questions for Buckholtz

**Q16: Energy/Hamiltonian Bridge Confirmation**
> "I derived a candidate H²(a) formula from energy conservation E = ½μḊ² + V_MULT(D) using the MULTING pairwise potentials:
>
> H²(a) = H₀² [Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]
>
> where the a⁻² term comes from the integration constant E, a⁻³ from monopole potential V_m ∝ a⁻¹, a⁻⁴ from dipole potential V_d ∝ a⁻², and a⁻⁵ from quadrupole potential V_q ∝ a⁻³.
>
> Is this close to the intended H_MULT(z) derivation, or does the AI service use a different route (e.g., mean-field averaging, virial theorem, or direct Friedmann modification)?"

**Q17: Cluster Variable Evolution**
> "If the Hamiltonian bridge is correct, I would need m_A(z), k_A(z), r_A(z) evolution to compute the Ω coefficients. Are these provided in supplementary materials, or should they be inferred from observational data (e.g., cluster mass functions, velocity dispersions)?"

**Q18: Physical Interpretation**
> "I found that the a⁻⁴ term (dipole) contributes neutrally to ä/a (acceleration), not strongly accelerating as I initially expected. Does the three-era structure (deceleration → borderline → acceleration) rely on the interplay of all four terms (Ω_k, Ω_m, Ω_d, Ω_q), rather than dipole domination alone?"

---

## References

**Source materials:**
- Manuscript: preprints202511.0598.v6.pdf, Appendix A.1 (force law)
- Table A1: Appendix A.3 (β_d = 4.5, β_q = 18.0, H_MULT values)

**Internal documents:**
- docs/33_public_formula_stripping_report.md — source force law extraction
- docs/43_bridge_candidate_math_stress_test.md — bridge triage
- docs/47_literature_bridge_map.md — literature support map

**Related work:**
- Layzer-Irvine equation — energy conservation in expanding universe
- Lattice universe models — discrete → continuum averaging
- Wigner-Seitz cell approximation — pair interaction → background field
- Buchert averaging — inhomogeneity effects in cosmology

---

**Status:** DERIVATION COMPLETE — awaiting independent verification (docs/48)

**Next step:** Independent verification must check:
1. Force scalings (r⁻², r⁻³, r⁻⁴)
2. Potential integration (F → V → check −dV/dr = F)
3. H² derivation (energy conservation algebra)
4. Monopole-only limit (reduces to Friedmann?)
5. Sign consistency (attractive/repulsive interpretation)
6. Acceleration logic (ä/a from H²)
7. Diagnostic fit stability (if approved for internal test)
8. Literature claims (docs/47)

**Classification:** OUR_COMPUTATIONAL_RECONSTRUCTION — NOT source-confirmed, NOT validated, NOT predictive.
