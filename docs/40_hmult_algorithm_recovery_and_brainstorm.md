# H_MULT Algorithm Recovery and Brainstorming

**Purpose:** Systematic search, reverse engineering, and candidate algorithm brainstorming for H_MULT(z) computational bridge

**Date:** 2026-05-29  
**Status:** IN PROGRESS — Source Recovery underway, Candidate Algorithms drafted  
**Blocker context:** Appendix A1 Step 5 provides scaling relations but NOT explicit H_MULT formula

---

## Executive Summary

### The Question

> **What algorithm could have produced the Table A1 H_MULT(z) values from the MULTING force-law ingredients?**

### Known Source-Confirmed Items

✅ **Force-law layer:**
- F_m (monopole), F_d (dipole), F_q (quadrupole)
- F_oP = F_m - F_d + F_q

✅ **Scaling relations:**
- r_dA = β_d × r_A
- r_dP = β_d × r_P
- |r_qAB|² = β_q² × r_A × r_P

✅ **Fitted beta values (Table A1):**
- β_d = 4.5
- β_q = 18.0

✅ **Step 5 procedural instruction:**
- "minimize standard-deviations away from observed H(z)"
- "Feel free to use any or all the information" (monopole/dipole/quadrupole)

### Known Blocker

❌ **Explicit computational formula H_MULT(z; β_d, β_q, m_A, r_A, k_A, ...) NOT found in Appendix A1**

Bridge F_oP → H_MULT(z) is **UNDER_SPECIFIED** — procedural instruction only, NOT computational formula.

### Three-Track Approach

1. **Track 1 — Source Recovery:** Search all local files for hidden algorithm clues
2. **Track 2 — Reverse Engineering:** Infer algorithm class from Table A1 data (BLOCKED: table empty)
3. **Track 3 — Candidate Algorithm Brainstorming:** Generate plausible reconstruction candidates

**Critical safety rule:** Do NOT call any candidate "the Buckholtz formula" unless SOURCE_CONFIRMED.

---

## Track 1 — Source Recovery

**Goal:** Find explicit H_MULT algorithm or indirect clues in local project files

**Search targets:**
- AI transcripts
- Supplementary materials
- Appendix A sections
- Table A1 caption
- Force-law definitions
- Cluster variable tables
- sigma_MULT definition

**Status:** ⏳ IN PROGRESS (explorer agent launched)

### Source Recovery Matrix

*(To be filled by explorer agent)*

| Source File | Algorithm Clue Found? | Formula? | Variables? | Status | Notes |
|---|---|---|---|---|---|
| docs/35_ai_transcript_closure_candidate.md | YES | Phi(z) heuristic | A_m, A_d, A_q | AI_TRANSCRIPT_REPORTED | Phenomenological scaling, not source-confirmed |
| docs/37_discrete_lattice_mvb_hypothesis.md | YES | Virial pressure route | F_oP, P_virial | RESEARCH_HYPOTHESIS | Audit reconstruction, not manuscript |
| docs/39_appendix_a1_steps_3_7_forensic_reading.md | NO | Scaling relations only | r_dA, r_dP, r_qAB | SOURCE_CONFIRMED | Formula missing |
| ... | ... | ... | ... | ... | ... |

### Critical Questions (to be answered by Source Recovery)

1. **Explicit formula:** Is H_MULT = f(z, β_d, β_q, ...) written ANYWHERE?
   - **Answer:** *(pending explorer)*

2. **Cluster variables:** Is there a table m_A(z), r_A(z), k_A(z) for Table A1 redshifts?
   - **Answer:** *(pending explorer)*

3. **sigma_MULT definition:** Is the fit quality metric defined precisely?
   - **Answer:** *(pending explorer)*

4. **Anchor point:** Is H_anchor or z_anchor specified?
   - **Answer:** *(pending explorer)*

5. **AI service details:** What did the AI service actually compute?
   - **Answer:** *(pending explorer)*

---

## Track 2 — Reverse Engineering Table A1

**Goal:** Infer algorithm class from empirical H_MULT values in Table A1

**Status:** ⏸️ **BLOCKED** — `data/table_a1_raw.csv` is empty template (manual transcription required)

### Required Data Extraction

Before reverse engineering can proceed, need:

**From Table A1:**
- z (redshift)
- time (cosmic time)
- H_obs (observed H(z) with uncertainties)
- H_FLRW (ΛCDM expansion rate)
- H_MULT (MULTING expansion rate)
- sigma_MULT (fit quality metric)

**Current status:** Template exists (`data/table_a1_raw.csv`), awaiting manual transcription from manuscript PDF.

### Reverse Engineering Test Suite (Planned)

Once Table A1 data available, run:

#### Test A — Is H_MULT just H_obs shifted?

Check:
```python
# Simple shift
H_MULT ≈ H_obs
H_MULT = H_obs ± n*sigma_H

# Weighted average
H_MULT = α*H_obs + (1-α)*H_FLRW

# Smoothed version
H_MULT = moving_average(H_obs)
```

#### Test B — Is sigma_MULT internally consistent?

Check:
```python
sigma_MULT ?= |H_MULT - H_obs| / sigma_H
sigma_MULT ?= (H_MULT - H_obs)²
sigma_MULT ?= RMS(H_MULT - H_obs)
```

#### Test C — Is H_MULT tied to H_FLRW?

Check:
```python
ratio = H_MULT / H_FLRW
residual = H_MULT - H_FLRW

# Polynomial fit
H_MULT(z) = H_FLRW(z) * (a0 + a1*z + a2*z² + ...)
```

#### Test D — Is H_MULT a phenomenological rescaling?

Try heuristic Phi(z) scaling:
```python
# Phi(z) = A_m(z) - A_d(z) + A_q(z)
# H_MULT²(z) = H_anchor² * Phi(z) / Phi(z_anchor)

# Test if Phi can be inferred from H_MULT ratios
Phi_inferred(z) = (H_MULT(z) / H_anchor)² * Phi(z_anchor)
```

#### Test E — Can force-law ratios explain residuals?

Build dimensionless force ratios:
```python
D(z) = F_d / F_m
Q(z) = F_q / F_m
Net(z) = 1 - D(z) + Q(z)

# Check correlation with H_MULT / H_FLRW
```

**Problem:** Requires cluster variables m_A(z), r_A(z), k_A(z), D_CAB(z) — NOT available.

### Reverse Engineering Output (Template)

*(To be filled after Table A1 extraction)*

| Hypothesis | Fit Quality | Required Assumptions | Plausible? | Status |
|---|---:|---|---|---|
| Simple H_obs shift | ? | None | ? | AWAITING_DATA |
| Weighted H_obs/H_FLRW average | ? | Fixed α | ? | AWAITING_DATA |
| Polynomial H_FLRW correction | ? | ≤3 parameters | ? | AWAITING_DATA |
| Phi(z) phenomenological scaling | ? | A_m, A_d, A_q table | ? | AWAITING_DATA |
| Force ratio correlation | ? | Cluster variables | ? | AWAITING_DATA |

---

## Track 3 — Candidate Algorithm Brainstorming

**Goal:** Generate plausible H_MULT reconstruction candidates WITHOUT claiming they are Buckholtz's formula

### Safety Labels (Mandatory)

All candidates MUST carry one of these status labels:

- **SOURCE_CONFIRMED:** Explicit in manuscript, PDF page cited
- **AI_TRANSCRIPT_REPORTED:** From AI transcript materials
- **PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY:** Can fit Table A1, NOT predictive
- **COMPUTATIONAL_RECONSTRUCTION_CANDIDATE:** Audit team reconstruction from first principles
- **MVB_CANDIDATE:** Discrete lattice + virial pressure route
- **TOY_EFFECTIVE_MODEL:** Simplified physics toy model
- **POST_HOC_DIAGNOSTIC_ONLY:** Diagnostic tool, NOT forward model
- **NOT_ALLOWED_FOR_PREDICTION:** Blocked for new redshifts
- **AUTHOR_CONFIRMATION_REQUIRED:** Awaiting Buckholtz clarification

---

### Candidate 1 — Table-Reproduction Spline Fit

**Name:** Spline-Fit Table-Reproduction Candidate

**Formula:**
```python
H_MULT(z) = spline_interpolation(z_table, H_MULT_table)
```

**Source basis:** None — pure data interpolation

**Assumptions:**
- Table A1 H_MULT values are correct
- H_MULT(z) is smooth function of z
- No physics between tabulated points

**Required inputs:**
- Table A1: z, H_MULT

**Dimensional check:** ✅ [H] = km/s/Mpc (preserves units)

**Can reproduce Table A1?** ✅ YES (by construction)

**Can predict new z?** ❌ NO (requires extrapolation beyond table range)

**MCMC allowed?** ❌ NO (no free parameters, pure interpolation)

**Status:** **PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY**

**Notes:**
- Simplest possible candidate
- Zero physical content
- Useful for visualization only

---

### Candidate 2 — Heuristic Phi(z) Scaling

**Name:** AI Transcript Phi(z) Phenomenological Scaling

**Formula:**
```python
Phi(z) = A_m(z) - A_d(z) + A_q(z)
H_MULT²(z) = H_anchor² × [Phi(z) / Phi(z_anchor)]
```

**Source basis:** AI transcript materials (docs/35), NOT manuscript-confirmed

**Assumptions:**
- Multipole amplitudes A_m, A_d, A_q exist and are tabulated
- Sign structure matches force law (F_oP = F_m - F_d + F_q)
- H_anchor and z_anchor are specified
- Phi(z) scaling preserves dimensional correctness

**Required inputs:**
- A_m(z), A_d(z), A_q(z) tables for all z
- H_anchor (reference Hubble parameter)
- z_anchor (reference redshift)

**Dimensional check:**
```
[Phi] = dimensionless (if A_m, A_d, A_q dimensionless)
[H_MULT²] = [H_anchor²] × [dimensionless] = (km/s/Mpc)² ✅
```

**Can reproduce Table A1?** ✅ YES (if A_m, A_d, A_q tables provided)

**Can predict new z?** ⚠️ PARTIAL (requires A_m, A_d, A_q for new z — how to get?)

**MCMC allowed?** ❌ NO (not derived from first principles, heuristic only)

**Status:** **AI_TRANSCRIPT_REPORTED + PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY**

**Notes:**
- Most explicit candidate found in project files
- Heuristic analogy to force-law structure
- Still requires cluster variables (blocked)
- NOT source-confirmed physical derivation

**Unknowns:**
- What are A_m, A_d, A_q? Force amplitudes? Energy scales? Dimensionless?
- How to compute A_m(z), A_d(z), A_q(z) from cluster variables?
- What is H_anchor? H_0? Planck value? Fitted?
- What is z_anchor? z=0? z of CMB? Other?

---

### Candidate 3 — Net Force Ratio Scaling

**Name:** Dimensionless Force Ratio Scaling Candidate

**Formula:**
```python
Net(z) = F_oP(z) / F_m(z) = 1 - F_d(z)/F_m(z) + F_q(z)/F_m(z)
H_MULT²(z) = H_FLRW²(z) × Net(z)
```

Or:
```python
H_MULT(z) = H_FLRW(z) × sqrt(Net(z))
```

**Source basis:** Audit reconstruction — force-law structure suggests this scaling

**Assumptions:**
- Dimensionless force ratio Net(z) modulates ΛCDM expansion
- F_m, F_d, F_q can be evaluated at cosmological scales
- Cluster variables m_A(z), r_A(z), k_A(z), D_CAB(z) are known
- β_d = 4.5, β_q = 18.0 enter through force ratios

**Required inputs:**
```python
m_A(z), r_A(z), k_A(z)  # Cluster monopole properties
m_P(z), r_P(z), k_P(z)  # Cluster 2 properties (if A ≠ P)
D_CAB(z)                # Comoving distance between clusters
β_d = 4.5
β_q = 18.0
```

**Force ratio formulas:**
```python
# From force-law definitions:
r_dA = β_d × r_A
r_dP = β_d × r_P
|r_qAB|² = β_q² × r_A × r_P

# Assume A = P (single cluster scale):
F_d / F_m = 2 × (k_A / (m_A c²)) × (β_d r_A / D_CAB)
F_q / F_m = (k_A / (m_A c²))² × β_q² × (r_A / D_CAB)²

# Net ratio:
Net(z) = 1 - 2×(k_A/(m_A c²))×(β_d r_A / D_CAB) + (k_A/(m_A c²))²×β_q²×(r_A/D_CAB)²
```

**Dimensional check:**
```
[k_A / (m_A c²)] = dimensionless (energy ratio)
[r_A / D_CAB] = dimensionless (length ratio)
[Net] = dimensionless ✅
[H_MULT] = [H_FLRW] × [dimensionless] = km/s/Mpc ✅
```

**Can reproduce Table A1?** ⚠️ UNKNOWN (requires cluster variable table)

**Can predict new z?** ⚠️ UNKNOWN (requires cluster variables for all z)

**MCMC allowed?** ❌ NO (not author-confirmed, reconstruction only)

**Status:** **COMPUTATIONAL_RECONSTRUCTION_CANDIDATE**

**Notes:**
- Physically motivated: force ratios → expansion modulation
- Requires cluster variables (NOT provided in Appendix A1)
- β_d, β_q appear naturally in force ratios
- Still heuristic: why should force ratio scale H²?

**Blockers:**
- No cluster variable table m_A(z), r_A(z), k_A(z)
- Assumption A = P not verified
- Physical mechanism H² ~ Net(z) not derived

---

### Candidate 4 — Acceleration-Over-Length Scaling

**Name:** Pairwise Acceleration / Length Scale Bridge

**Formula:**
```python
a_MULT(z) = F_oP(z) / m_P
H_MULT²(z) ~ a_MULT(z) / L(z)
```

Where L(z) is characteristic length scale (options):
- D_CAB(z) — comoving distance between clusters
- r(z) — physical cluster separation
- c / H_FLRW(z) — Hubble horizon
- a(t) × χ(z) — scale-factor distance

**Source basis:** Dimensional analysis — [H²] = [a/L]

**Assumptions:**
- Pairwise acceleration a_MULT scales cosmological acceleration
- There exists characteristic length L(z) for cluster dynamics
- Proportionality constant absorbed into force normalization

**Required inputs:**
- F_oP(z) from cluster variables
- m_P (cluster mass)
- L(z) (length scale definition)

**Dimensional check:**
```
[F_oP] = kg·m/s²
[m_P] = kg
[a_MULT] = m/s²
[H²] = (1/s)² = [a/L] if [L] = m ✅
```

**Can reproduce Table A1?** ⚠️ UNKNOWN (requires cluster variables + L(z) choice)

**Can predict new z?** ❌ BLOCKED (no canonical L(z) choice)

**MCMC allowed?** ❌ NO (multiple arbitrary choices: L(z), proportionality constant)

**Status:** **TOY_EFFECTIVE_MODEL**

**Notes:**
- Dimensionally correct
- Multiple L(z) candidates → ambiguous
- No rigorous derivation why H² ~ a/L
- Useful for order-of-magnitude checks only

---

### Candidate 5 — Virial Pressure / Effective Fluid Bridge (MVB)

**Name:** Discrete Lattice + Virial Pressure Route (MVB Candidate)

**Formula:**
```python
# Step 1: Virial pressure from pairwise forces
P_virial(z) = -⟨r · F_oP⟩ / (3 V_cell(z))

# Step 2: Effective fluid
ρ_eff(z) = matter density
P_eff(z) = P_virial(z)

# Step 3: Friedmann acceleration equation
ä/a = -(4πG/3) × (ρ_eff + 3 P_eff / c²)

# Step 4: H²(z) from ä/a
H²(z) = (ȧ/a)² = ...
```

**Source basis:** Audit reconstruction (docs/37) — NOT manuscript-confirmed

**Assumptions:**
- Galaxy clusters form discrete lattice (Wigner-Seitz cells)
- Cosmic web topology = nearest-neighbor interactions
- Virial theorem applies: P = -⟨r·F⟩/(3V)
- Effective fluid approximation valid
- Friedmann equations hold with P_eff

**Required inputs:**
- F_oP(r, z) force law
- V_cell(z) — Wigner-Seitz cell volume
- ⟨r · F_oP⟩ — statistical average over cell
- ρ_eff(z) — matter density

**Dimensional check:**
```
[⟨r · F⟩] = m × (kg·m/s²) = kg·m²/s²
[V_cell] = m³
[P_virial] = (kg·m²/s²) / m³ = kg/(m·s²) = Pa ✅
[4πG/3 × ρ] = (1/s²) if [ρ] = kg/m³ ✅
[H²] = (1/s)² ✅
```

**Can reproduce Table A1?** ⚠️ UNKNOWN (requires solving ODE + lattice geometry)

**Can predict new z?** ⚠️ UNKNOWN (if ODE solvable + initial conditions specified)

**MCMC allowed?** ❌ NO (not author-confirmed, research hypothesis)

**Status:** **MVB_CANDIDATE + RESEARCH_HYPOTHESIS**

**Notes:**
- Most physically motivated candidate
- Uses standard statistical mechanics (virial theorem)
- Avoids homogeneous averaging (preserves dipole/quadrupole)
- Requires numerical ODE solver
- Lattice geometry NOT specified (FCC? BCC? Voronoi?)
- **Critical:** This is OUR reconstruction, NOT Buckholtz's stated approach

**Blockers:**
- Lattice topology not specified
- Cell volume V_cell(z) evolution not specified
- Averaging prescription ⟨r·F_oP⟩ not derived
- Boundary conditions / initial conditions not specified

---

### Candidate 6 — Discrete Lattice Neighbor Dynamics

**Name:** Nearest-Neighbor Cluster ODE Route

**Formula:**
```python
# Step 1: Cluster separation evolves
D_CAB(t) = a(t) × D0  # Comoving separation fixed, physical separation scales

# Step 2: Equation of motion for separation
D̈_CAB = F_oP / μ  # μ = reduced mass

# Step 3: Acceleration equation
ä/a = D̈_CAB / D_CAB

# Step 4: Hubble parameter
H(a) = ȧ/a = ...
```

**Source basis:** MVB variant (docs/37) — discrete dynamics

**Assumptions:**
- Clusters are point masses in lattice
- Nearest-neighbor dynamics dominates
- Comoving separation D0 constant (lattice fixed in comoving frame)
- Reduced mass μ = m_A m_P / (m_A + m_P)

**Required inputs:**
- F_oP(D_CAB, z)
- μ (reduced mass)
- D0 (comoving separation)
- Initial conditions: a(t0), ȧ(t0)

**Dimensional check:**
```
[F_oP] = kg·m/s²
[μ] = kg
[D̈_CAB] = m/s²
[ä/a] = (1/s²) if [D̈_CAB/D_CAB] = (1/s²) ✅
[H] = (1/s) ✅
```

**Can reproduce Table A1?** ⚠️ UNKNOWN (requires ODE integration)

**Can predict new z?** ⚠️ UNKNOWN (if ODE + ICs specified)

**MCMC allowed?** ❌ NO (not author-confirmed)

**Status:** **MVB_CANDIDATE + RESEARCH_HYPOTHESIS**

**Notes:**
- Simplest discrete dynamics candidate
- Analytically tractable (in principle)
- **Problem:** ä/a = D̈/D assumes all clusters have same dynamics
- **Problem:** Homogeneous expansion ⟹ D̈ = ä×D0, circular logic?
- Needs careful re-derivation

---

### Candidate 7 — Effective w(z) Reconstruction (Post-Hoc)

**Name:** Equation-of-State Reconstruction from H_MULT

**Formula:**
```python
# Given H_MULT(z), infer w_eff(z):
w_eff(z) = -1 - (2/3) × (1/(1+z)) × (d ln H_MULT / dz)
```

Or numerical differentiation from Table A1.

**Source basis:** Standard cosmology — w(z) diagnostic

**Assumptions:**
- H_MULT(z) is differentiable
- Friedmann equations hold
- Single effective fluid with w_eff

**Required inputs:**
- Table A1: z, H_MULT(z)

**Dimensional check:**
```
[w] = dimensionless ✅
[d ln H / dz] = dimensionless ✅
```

**Can reproduce Table A1?** N/A (uses Table A1 as input)

**Can predict new z?** ❌ NO (post-hoc diagnostic, not forward model)

**MCMC allowed?** ❌ NO (not a forward model)

**Status:** **POST_HOC_DIAGNOSTIC_ONLY**

**Notes:**
- Useful for checking if w_eff correlates with dominance of monopole/dipole/quadrupole
- Does NOT provide H_MULT(z) — requires H_MULT(z) as input
- Diagnostic tool, not forward model
- Can be computed once Table A1 is extracted

---

### Candidate 8 — ΛCDM + Phenomenological Correction

**Name:** ΛCDM + Polynomial Correction

**Formula:**
```python
H_MULT(z) = H_FLRW(z) × [1 + c1×z + c2×z² + c3×z³]
```

Where c1, c2, c3 are fitted parameters.

**Source basis:** None — pure phenomenology

**Assumptions:**
- MULTING is small correction to ΛCDM
- Correction is smooth polynomial in z
- 3 parameters sufficient to capture Table A1

**Required inputs:**
- H_FLRW(z) (standard ΛCDM)
- Table A1 for fitting c1, c2, c3

**Dimensional check:**
```
[H_MULT] = [H_FLRW] × [dimensionless] = km/s/Mpc ✅
```

**Can reproduce Table A1?** ✅ YES (fit by construction, 3 DoF)

**Can predict new z?** ⚠️ EXTRAPOLATION ONLY (polynomial may diverge outside fit range)

**MCMC allowed?** ❌ NO (phenomenological, not physical parameters)

**Status:** **PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY**

**Notes:**
- Simplest smooth interpolation with few parameters
- No physical content
- Useful for testing if MULTING ~ ΛCDM + small correction
- AIC/BIC penalty: 3 extra parameters vs ΛCDM (2 parameters: Ωm, H0)

**Overfitting risk:** HIGH if table has ≤ 12 rows

---

## Candidate Algorithm Summary Table

| Candidate | Status | Formula Exists? | Can Reproduce Table? | Can Predict New z? | MCMC Ready? | Blockers |
|---|---|---|---|---|---|---|
| **1. Spline Fit** | PHENOMENOLOGICAL | ✅ | ✅ YES | ❌ NO | ❌ NO | Extrapolation only |
| **2. Phi(z) Scaling** | AI_TRANSCRIPT | ✅ | ✅ YES* | ⚠️ PARTIAL* | ❌ NO | *Requires A_m, A_d, A_q table |
| **3. Force Ratio** | RECONSTRUCTION | ✅ | ⚠️ UNKNOWN | ⚠️ UNKNOWN | ❌ NO | Cluster variables missing |
| **4. Accel/Length** | TOY_MODEL | ✅ | ⚠️ UNKNOWN | ❌ NO | ❌ NO | L(z) ambiguous |
| **5. Virial Pressure (MVB)** | RESEARCH_HYPOTHESIS | ✅ | ⚠️ UNKNOWN | ⚠️ UNKNOWN | ❌ NO | Lattice geometry, ODE solver |
| **6. Discrete ODE** | RESEARCH_HYPOTHESIS | ✅ | ⚠️ UNKNOWN | ⚠️ UNKNOWN | ❌ NO | ICs, circular logic risk |
| **7. w_eff Diagnostic** | POST_HOC | ✅ | N/A | ❌ NO | ❌ NO | Not a forward model |
| **8. ΛCDM + Polynomial** | PHENOMENOLOGICAL | ✅ | ✅ YES | ⚠️ EXTRAPOLATION | ❌ NO | 3 DoF, overfitting risk |

---

## Best Candidate Ranking

### Criterion 1 — Most Source-Faithful

1. **Phi(z) Scaling** (AI_TRANSCRIPT_REPORTED) — only explicit formula found in project files
2. **Force Ratio** (COMPUTATIONAL_RECONSTRUCTION) — uses source-confirmed force law
3. **Virial Pressure (MVB)** (RESEARCH_HYPOTHESIS) — uses source-confirmed forces + standard physics
4. All others — pure phenomenology or post-hoc diagnostics

### Criterion 2 — Most Physically Defensible

1. **Virial Pressure (MVB)** — uses standard statistical mechanics (virial theorem) + Friedmann equations
2. **Discrete ODE** — nearest-neighbor dynamics, but risk of circular logic
3. **Force Ratio** — heuristic but dimensionally correct
4. **Accel/Length** — toy model, ambiguous length scale
5. All others — phenomenological, no physical mechanism

### Criterion 3 — Most Useful for Table A1 Reproduction

1. **Spline Fit** — trivial (interpolation)
2. **ΛCDM + Polynomial** — 3 parameters, smooth
3. **Phi(z) Scaling** — IF A_m, A_d, A_q table provided
4. All others — BLOCKED (missing inputs)

### Criterion 4 — Most Useful for Future Theory Development

1. **Virial Pressure (MVB)** — rigorous framework, testable, falsifiable
2. **Discrete ODE** — simpler variant of MVB, analytically tractable
3. **Force Ratio** — intermediate heuristic, testable
4. **Phi(z) Scaling** — heuristic, but most explicit AI transcript candidate
5. All others — dead ends (phenomenology or diagnostics)

---

## Dimensional Consistency Checks

All candidates pass basic dimensional analysis:

✅ **Candidate 1 (Spline):** [H] = km/s/Mpc (by construction)  
✅ **Candidate 2 (Phi):** [H²] = [H_anchor²] × [dimensionless] ✅  
✅ **Candidate 3 (Force Ratio):** [H] = [H_FLRW] × [dimensionless] ✅  
✅ **Candidate 4 (Accel/Length):** [H²] = [a/L] if [a]=m/s², [L]=m ✅  
✅ **Candidate 5 (MVB Virial):** [P] = kg/(m·s²), [H²] = (1/s²) ✅  
✅ **Candidate 6 (Discrete ODE):** [H] = [ȧ/a] = (1/s) ✅  
✅ **Candidate 7 (w_eff):** [w] = dimensionless ✅  
✅ **Candidate 8 (ΛCDM+Poly):** [H] = [H_FLRW] × [dimensionless] ✅

**No dimensional violations found.**

---

## Degrees of Freedom and Overfitting Warnings

### Table A1 Structure

**Expected rows:** ~12 (z = 0 to 8.5, based on Appendix A1 Step 3)

### Candidate DoF Count

| Candidate | Free Parameters | DoF / N_rows Ratio | Overfitting Risk |
|---|---|---|---|
| Spline Fit | N_rows (12) | 12/12 = 1.00 | ⚠️ **EXTREME** — perfect fit guaranteed |
| Phi(z) Scaling | A_m, A_d, A_q tables (3×12 = 36) | 36/12 = 3.00 | ⚠️ **EXTREME** — 3× overfit |
| Force Ratio | Cluster vars (≥3×12 = 36) | 36/12 = 3.00 | ⚠️ **EXTREME** |
| ΛCDM + Polynomial | 3 (c1, c2, c3) | 3/12 = 0.25 | ✅ ACCEPTABLE |
| MVB Virial Pressure | Lattice params + ICs (~5-10) | ~0.5 | ✅ ACCEPTABLE |
| Discrete ODE | ICs + D0 (~3) | ~0.25 | ✅ ACCEPTABLE |

### Overfitting Guard

**Rule:** DoF / N_rows > 0.5 → overfitting risk, penalize with AIC/BIC

**AIC penalty:**
```
AIC = -2 ln(L) + 2k
```
Where k = number of free parameters.

**For Table A1 (N=12):**
- k ≤ 6 → acceptable
- k > 6 → overfitting warning

**Candidates exceeding limit:**
- Spline Fit (k=12) — ⚠️ FLAGGED
- Phi(z) Scaling (k=36) — ⚠️ FLAGGED
- Force Ratio (k=36) — ⚠️ FLAGGED

**Mitigation:**
- Regularization (L1/L2 penalty)
- Prior constraints (Bayesian approach)
- Independent validation set (NOT from Table A1)

---

## Critical Unknowns Requiring Author Clarification

### Priority 1 (Blocks Table A1 Reproduction)

1. **Explicit H_MULT formula:** What is H_MULT(z; β_d, β_q, ...)?
2. **Cluster variable table:** Do you have m_A(z), r_A(z), k_A(z) for z = 0 to 8.5?
3. **AI interpretation route:** Did AI use Phi(z) scaling, force ratio, virial pressure, or other?

### Priority 2 (Blocks Predictive Modeling)

4. **Phi(z) definition:** If using Phi(z), what are A_m, A_d, A_q? Dimensionless? Amplitudes?
5. **Anchor point:** What is H_anchor and z_anchor?
6. **sigma_MULT definition:** How is fit quality metric computed?

### Priority 3 (Enables MCMC)

7. **Physical derivation:** Is there rigorous derivation F_oP → H(z) from field equations?
8. **Lattice geometry:** If using discrete approach, what is cell topology?
9. **Boundary conditions:** For ODE route, what are initial conditions?

---

## Recommended Next Steps

### Option A — Wait for Author Clarification

**Action:** Send updated question (Q12 from docs/26) to Dr. Buckholtz, wait for response

**Pros:**
- Source-faithful
- Avoids misrepresentation
- Unblocks once answered

**Cons:**
- May take weeks/months
- May not receive response
- Blocks progress

**Recommendation:** ✅ **PRIMARY PATH** — author confirmation required before implementation

---

### Option B — Build Phi(z) Scaling (AI Transcript Candidate)

**Action:** Implement Candidate 2 (Phi(z) heuristic) as TABLE_REPRODUCTION_ONLY

**Pros:**
- Most explicit formula found in project files
- Can reproduce Table A1 IF cluster variables provided
- Matches force-law sign structure

**Cons:**
- Requires cluster variable table (missing)
- Not source-confirmed
- Heuristic, not derived
- Cannot predict new z without cluster table

**Recommendation:** ⏸️ **SECONDARY PATH** — only if cluster variables provided or AI transcript clarified

---

### Option C — Develop MVB Virial Route (Research Hypothesis)

**Action:** Implement Candidate 5 (discrete lattice + virial pressure) as RESEARCH_HYPOTHESIS

**Pros:**
- Most physically rigorous candidate
- Uses standard statistical mechanics
- Falsifiable and testable
- Useful for theory development

**Cons:**
- NOT source-confirmed (audit reconstruction)
- Requires lattice geometry specification
- Requires ODE solver
- MCMC blocked until author confirms

**Recommendation:** ⏸️ **RESEARCH TRACK** — useful for internal development, NOT for validation claims

---

### Option D — Phenomenological Table Fit (Interim Diagnostic)

**Action:** Implement Candidate 8 (ΛCDM + polynomial) for exploratory analysis

**Pros:**
- Simple, minimal DoF
- Can reproduce Table A1
- Diagnostic: test if MULTING ~ ΛCDM + small correction

**Cons:**
- Zero physical content
- Cannot validate/refute MULTING
- Extrapolation risky

**Recommendation:** ✅ **DIAGNOSTIC TOOL** — safe for exploratory analysis, NOT for claims

---

## Final Recommendation

**Primary path:**

1. ✅ **Wait for author clarification** (Q12 from docs/26)
2. ✅ **Build diagnostic tools** (Candidate 7 w_eff, Candidate 8 phenomenological fit)
3. ⏸️ **Develop MVB internally** (Candidate 5) as research hypothesis, NOT validation claim
4. ❌ **Do NOT implement Phi(z) or Force Ratio** without cluster variables or author confirmation

**Repository status:**

- **Table A1 extraction:** AWAITING manual transcription
- **Source recovery:** IN PROGRESS (explorer agent)
- **Candidate algorithms:** 8 candidates documented
- **Implementation:** BLOCKED until author clarification OR diagnostic-only tools

**Communication to author:**

> "Appendix A1 Step 5 provides scaling relations and fitting instruction, but not explicit computational formula H_MULT(z; β_d, β_q, ...). I have identified 8 possible reconstruction candidates ranging from heuristic Phi(z) scaling (AI transcript) to discrete lattice + virial pressure (audit reconstruction). Could you clarify which route matches your intended approach, or provide explicit formula / cluster variable table for Table A1 reproduction?"

---

## Appendix: Notation and Definitions

### Force-Law Components

- **F_m:** Monopole force (attractive, gravity-like)
- **F_d:** Dipole force (repulsive at large scales)
- **F_q:** Quadrupole force (attractive or repulsive, scale-dependent)
- **F_oP:** Total pairwise force, F_oP = F_m - F_d + F_q

### Scaling Relations

- **r_dA = β_d × r_A:** Dipole length scale for cluster A
- **r_dP = β_d × r_P:** Dipole length scale for cluster P
- **|r_qAB|² = β_q² × r_A × r_P:** Quadrupole length scale squared

### Cluster Variables

- **m_A:** Monopole mass of cluster A
- **r_A:** Monopole length scale of cluster A
- **k_A:** Monopole coupling constant for cluster A
- **D_CAB:** Comoving distance between clusters A and B

### Beta Parameters

- **β_d = 4.5:** Dipole scaling factor (dimensionless, fitted)
- **β_q = 18.0:** Quadrupole scaling factor (dimensionless, fitted)

### Expansion Rates

- **H_obs:** Observed Hubble parameter from data
- **H_FLRW:** ΛCDM expansion rate (standard cosmology)
- **H_MULT:** MULTING expansion rate (IDM/MULTING framework)
- **sigma_MULT:** Fit quality metric (definition unclear)

### Other

- **Phi(z):** Multipole scaling factor (heuristic, AI transcript)
- **A_m, A_d, A_q:** Monopole/dipole/quadrupole amplitudes (undefined)
- **Net(z):** Dimensionless force ratio, Net = 1 - D + Q
- **P_virial:** Virial pressure from pairwise forces
- **w_eff(z):** Effective equation of state parameter

---

**Last updated:** 2026-05-29  
**Status:** Track 1 IN PROGRESS, Track 2 BLOCKED, Track 3 COMPLETE  
**Next action:** Await Source Recovery results from explorer agent, then update Source Recovery Matrix

---

**End of Document**
