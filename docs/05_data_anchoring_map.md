# Data-Anchoring Map

## Purpose

Track which observational datasets are used and how, to prevent:
1. Circular reasoning (using H0 to derive beta, then claiming to "predict" H0)
2. Data leakage (mixing input and output)
3. Overfitting (too many free parameters for available data)

---

## Data Anchors

| Claim / parameter | Observational anchor | Dataset | Used as input / target / constraint | Leakage risk | Notes |
|---|---|---|---|---|---|
| **Electron mass** | PDG particle masses | PDG 2022 | Input | None | Safe — fundamental constant |
| **Tau mass** | PDG particle masses | PDG 2022 | Input | None | Safe — fundamental constant |
| **k_e (Coulomb constant)** | CODATA constants | CODATA 2018 | Input | None | Safe — fundamental constant |
| **G (gravitational constant)** | CODATA constants | CODATA 2018 | Input | None | Safe — fundamental constant |
| **e (elementary charge)** | CODATA constants | CODATA 2018 | Input | None | Safe — fundamental constant |
| **Eq.15 relation** | None (pure numerical relation) | N/A | N/A | None | Uses only fundamental constants |
| **beta_d** | **Unknown** | **Unknown** | **Unknown** | **High** | If fitted to H(z) → cannot claim to "predict" H(z) |
| **beta_q** | **Unknown** | **Unknown** | **Unknown** | **High** | If fitted to H(z) → cannot claim to "predict" H(z) |
| **H(z) fit** | Cosmic chronometers / Pantheon+ / both? | Various | Target (if betas fitted) | **High** | Dataset unclear, fit procedure unclear |
| **Omega_dm / Omega_b** | Planck CMB / BAO / weak lensing | Planck 2018, SDSS, DES | Constraint or input? | **High** | If used to derive betas → circular |
| **Future cosmic reversal** | None (prediction) | N/A | Output | None | Testable prediction |
| **6 isomers** | None (hypothesis) | N/A | N/A | None | Requires observational signature definition |
| **Bullet Cluster** | Dark matter distribution | Chandra X-ray + optical | Constraint | Low | Tests collisionless nature, not beta values |
| **Weak lensing (S8)** | Matter clustering | DES, KiDS | Constraint | Medium | Constrains Omega_m * sigma_8 |
| **PPN constraints** | Solar System tests | Cassini, LLR, Mercury | Constraint | None | **Critical** for MULTING viability |

---

## High Leakage Risk Items

**These datasets, if used to determine betas, create circular reasoning:**

### 1. H(z) cosmic chronometers
- **Dataset:** Various surveys (e.g., Moresco et al. compilations)
- **What it measures:** Direct H(z) measurements from galaxy ages
- **Leakage risk:** **High**
- **Why risky:** If beta_d and beta_q are fitted to H(z) data, cannot then claim to "predict" H(z)
- **Mitigation:** Clarify if betas are (a) derived from IDM structure, or (b) fitted to H(z)

### 2. Planck CMB parameters
- **Dataset:** Planck 2018 (TT, TE, EE + lensing)
- **What it measures:** Omega_m, Omega_b, Omega_Lambda, H0, sigma_8
- **Leakage risk:** **High**
- **Why risky:** If Omega values used to derive beta formulas, circular reasoning
- **Mitigation:** Ensure betas are derived from fundamental physics, not from cosmological fits

### 3. Pantheon+ Type Ia Supernovae
- **Dataset:** Pantheon+ (1701 SNIa, z = 0.001 to 2.26)
- **What it measures:** Luminosity distance vs redshift
- **Leakage risk:** **High**
- **Why risky:** If used to fit betas, cannot claim independent H(z) prediction
- **Mitigation:** Same as (1)

### 4. BAO (SDSS/DESI)
- **Dataset:** SDSS, BOSS, eBOSS, DESI
- **What it measures:** Baryon acoustic oscillation scale (standard ruler)
- **Leakage risk:** **High**
- **Why risky:** BAO constrains expansion history; if used for beta fitting → circular
- **Mitigation:** Same as (1)

---

## Safe Input Datasets

**These can be used as inputs without circularity:**

### 1. PDG particle masses
- **Dataset:** Particle Data Group 2022
- **What it provides:** m_e, m_tau, m_mu, etc.
- **Leakage risk:** None
- **Why safe:** Fundamental measurements, not cosmological fits
- **Usage:** Eq.15 relation, particle predictions

### 2. CODATA fundamental constants
- **Dataset:** CODATA 2018
- **What it provides:** e, G, c, hbar, alpha, k_e
- **Leakage risk:** None
- **Why safe:** Fundamental constants, lab-measured
- **Usage:** Eq.15 relation

### 3. PPN Solar System tests
- **Dataset:** Cassini, lunar laser ranging, Mercury perihelion
- **What it provides:** gamma, beta PPN parameters, light deflection
- **Leakage risk:** None (it's a constraint, not a fit)
- **Why safe:** Tests GR deviations locally, does not determine betas
- **Usage:** **Critical constraint** on MULTING dipole/quadrupole terms

---

## Data Flow Diagram

```
INPUTS (no leakage risk):
  ├─ PDG particle masses (m_e, m_tau) ──→ Eq.15 relation
  ├─ CODATA constants (e, G, k_e) ──────→ Eq.15 relation
  └─ PPN constraints ────────────────────→ MULTING dipole/quad viability check

AMBIGUOUS (clarification required):
  ├─ H(z) data ──→ beta_d, beta_q? ──→ H(z) prediction?  [CIRCULAR if yes]
  ├─ Planck Omega ──→ beta formulas? ──→ cosmology prediction?  [CIRCULAR if yes]
  └─ SNIa / BAO ──→ beta fitting? ──→ distance prediction?  [CIRCULAR if yes]

OUTPUTS (predictions, no circularity):
  ├─ Future cosmic reversal (testable prediction)
  ├─ Particle mass predictions (testable if specific)
  └─ 6 isomers observational signatures (if specified)
```

---

## Circular Reasoning Check

**Question:** Are beta_d and beta_q:
- **(A)** Derived from IDM/MULTING internal structure (no data dependence)?
- **(B)** Fitted to H(z) or other cosmological observations?

**If (A):** No circular reasoning. Betas are input, H(z) is prediction. ✅

**If (B):** Circular reasoning risk. Betas are fitted to data, then "predict" the same data. ❌

**Current status:** **Unknown** — requires clarification from Dr. Buckholtz.

**Action:** Request explicit statement:
> "Are beta_d and beta_q derived from fundamental IDM/MULTING principles, or are they phenomenological parameters fitted to cosmological data?"

---

## Overfitting Risk

**Definition:** Too many free parameters relative to data points.

**Analysis (if betas are fitted):**

Assume H(z) fit with N_data = 100 data points (typical cosmic chronometer sample).

| Scenario | Free parameters | Degrees of freedom | Overfitting risk |
|---|---|---|---|
| ΛCDM | 2 (H0, Omega_m) | 98 | Low |
| MULTING (monopole only) | 2-3 (H0, Omega_m, + monopole term) | 97 | Low |
| MULTING (monopole + dipole + quadrupole) | 4-5 (H0, Omega_m, beta_d, beta_q, + monopole) | 95 | **Medium** — 5 parameters for 100 points |
| MULTING (if cluster radius, sub-object KE also free) | 6+ | <94 | **High** — too many free parameters |

**Interpretation:**
- If beta_d and beta_q are the only new free parameters → overfitting risk is manageable
- If additional parameters (cluster radius, sub-object definitions) are also free → high overfitting risk

**Mitigation:**
1. Minimize number of free parameters
2. Use independent datasets for validation (train on cosmic chronometers, test on SNIa)
3. Report reduced chi-squared (chi^2 / dof) — should be ~1 for good fit

---

## Dataset Usage Classification

| Dataset | Category | Leakage risk if used for beta fitting | Can be used for validation? |
|---|---|---|---|
| PDG masses | Input (safe) | None | N/A |
| CODATA constants | Input (safe) | None | N/A |
| Cosmic chronometers H(z) | Target (if fitted) or validation | High (if fitted) | Yes (if not used for fitting) |
| Pantheon+ SNIa | Target (if fitted) or validation | High (if fitted) | Yes (if not used for fitting) |
| Planck CMB | Constraint | High | Yes (check consistency after model fixed) |
| BAO | Constraint | High | Yes (check consistency after model fixed) |
| Bullet Cluster | Constraint | Low | Yes (tests dark matter properties) |
| Weak lensing | Constraint | Medium | Yes (tests matter clustering) |
| PPN Solar System | Constraint (**critical**) | None | No (it's a pass/fail test) |

---

## Recommended Data Usage Protocol

1. **Phase 1: Beta derivation (if possible)**
   - Derive beta_d and beta_q from IDM/MULTING internal structure
   - No cosmological data used
   - Result: beta values are predictions

2. **Phase 2: Validation (if Phase 1 succeeds)**
   - Use derived betas to compute H(z)
   - Compare to cosmic chronometers, SNIa, BAO
   - Report goodness-of-fit (no fitting allowed)
   - Result: model is validated or falsified

3. **Fallback: Phenomenological fitting (if Phase 1 fails)**
   - Fit beta_d and beta_q to Dataset A (e.g., cosmic chronometers)
   - Validate on Dataset B (e.g., SNIa)
   - Report: "betas are phenomenological fit parameters, not fundamental predictions"
   - Result: model works but is less predictive

---

## Status Summary

| Anchor type | Count | Leakage risk |
|---|---:|---|
| Safe inputs (PDG, CODATA) | 5 | None |
| High-risk datasets (if used for fitting) | 4 | High |
| Medium-risk datasets | 2 | Medium |
| Low-risk datasets | 1 | Low |
| Unclear usage (beta derivation) | 2 | **Requires clarification** |

**Blocker:** Cannot assess data leakage risk until beta derivation vs fitting is clarified.

---

## Next Steps

1. **Immediate:** Request clarification: are betas derived or fitted?
2. **If derived:** Document derivation, proceed to validation phase
3. **If fitted:** Specify dataset, fit procedure, degrees of freedom, validation dataset
4. **Critical:** Perform PPN constraint check (regardless of fitting)

---

**Data discipline principle:**  
> Input ≠ Output. If you fit to H(z), you cannot claim to "predict" H(z). Circular reasoning is not science.
