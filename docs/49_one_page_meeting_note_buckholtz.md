# One-Page Meeting Note — Buckholtz IDM/MULTING Computational Reproducibility

**Date:** 2026-05-29  
**Purpose:** Short reference for possible meeting or follow-up discussion  
**NOT an email to send now**

---

## Purpose

I am trying to understand selected computational parts of IDM/MULTING accurately enough to avoid misrepresenting them in code. This is a reproducibility study, not validation or refutation.

---

## What I Checked

**Manuscript focus:** Appendix A1 (Steps 3–7) and Table A1

**Computational layers examined:**
1. **Force law:** F_oP = F_m - F_d + F_q (SOURCE_CONFIRMED in manuscript)
2. **Beta scaling:** β_m, β_d, β_q parameters (Table A1: β_d=4.5, β_q=18.0)
3. **Sigma columns:** sigma_MULT consistency across 12 rows
4. **Bridge candidates:** Possible F_oP → H_MULT(z) mappings

**Files created:**
- Appendix A1 forensic extraction (docs/07)
- Table A1 CSV transcription (data/table_a1_extracted.csv)
- Reverse engineering diagnostics (docs/42)
- Bridge candidate stress test (docs/43)
- Hamiltonian bridge verification (docs/48)

---

## What I Found

### 1. Table A1 H_MULT Performance

**H_MULT vs. H_obs residuals (Rows 2–12):**
- H_MULT: 1.27 km/s/Mpc mean deviation
- H_FLRW: 8.13 km/s/Mpc mean deviation
- **H_MULT is about 6× closer to H_obs than H_FLRW**

**Interpretation:** Strong retrodiction/table-fit evidence (not prediction).

### 2. Sigma Consistency

**Rows 2–12:** max sigma deviation 0.039 (passes adaptive tolerance)  
**Row 1 (z=0):** sigma_MULT deviation 3.027 (27× tolerance exceeded)

**Classification:** Row 1 = SOURCE_TABLE_OUTLIER, excluded from internal fits.

**Question prepared:** Q14 asks whether Row 1 uses different convention or is special case.

### 3. Appendix A1 Bridge Method

**Steps 3–5:** Force computation clear (SOURCE_CONFIRMED).  
**Step 6:** "AI service" generates H_MULT candidates — method not fully specified.  
**Step 7:** Fit and sigma check — clear.

**Gap:** No explicit H_MULT(z) formula or bridge derivation in manuscript.

**Question prepared:** Q15 asks about intended bridge method.

---

## My Current Reconstruction

I derived a candidate Hamiltonian bridge from energy conservation:

```
H²(a) = H₀² [Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]

where:
  a = 1/(1+z)
  Ω_k from integration constant E
  Ω_m from monopole potential V_m ∝ a⁻¹
  Ω_d from dipole potential V_d ∝ a⁻²
  Ω_q from quadrupole potential V_q ∝ a⁻³
```

**Derivation path:**
1. Start from pairwise energy: E = ½μḊ² + V_MULT(D)
2. Integrate forces F(r) → potentials V(a)
3. Substitute D = a(t)D₀ → H² = (Ḋ/D)²
4. Identify Ω coefficients from E and V_MULT

**Verification status:**
- ✅ Algebraically valid (force scaling, potential integration, H² derivation all pass)
- ✅ Monopole-only limit (β_d=0, β_q=0) reduces to Friedmann-like form
- ✅ Acceleration interpretation: a⁻⁴ term can accelerate if Ω_d < 0
- ⚠️ Literature: framework support (Layzer-Irvine, lattice universe) but not MULTING-specific
- ❌ NOT source-confirmed

**Important:** This is **my reconstruction only**. It is not assumed to be Buckholtz's intended formula.

**Question prepared:** Q16 asks whether this Hamiltonian approach is close to intended derivation.

---

## Main Questions

### Q1: Intended Bridge Method (Q15 in prepared brief)

Is the Table A1 bridge closer to:
- Force-ratio scaling (F_oP/F_m → H adjustment)?
- Discrete lattice ODE (pair acceleration → background H)?
- AI phenomenological fitting (pattern matching H_MULT → H_obs)?
- Hamiltonian energy averaging (E → H² via statistical mechanics)?
- Something else?

**Why this matters:** Without knowing the intended method, I cannot confidently implement or test H_MULT computation for new z.

### Q2: Row 1 z=0 Treatment (Q14)

Is Row 1 z=0:
- Treated as an anchor row (not fit residual)?
- Using different sigma_MULT convention?
- Special case with different calculation rule?

**What I see:** sigma_MULT reported 1.30, calculated -1.727 from (H_MULT - H_obs)/sigma_obs. This is 27× tolerance and appears inconsistent with Rows 2–12.

**Why this matters:** Determines whether to include Row 1 in diagnostics or exclude as outlier.

### Q3: Cluster Variables (Q17)

Are m_A(z), k_A(z), r_A(z), D_AB(z), N_eff:
- Available in supplementary materials?
- Intended to be inferred from observational data (cluster mass functions, velocity dispersions)?
- Assumed constant for simplicity?

**Why this matters:** To compute Hamiltonian Ω coefficients from first principles (not fit), I need cluster variable evolution.

---

## Non-Goals

**This study is NOT:**
- Validation of IDM/MULTING
- Refutation of IDM/MULTING
- Public critique
- Immediate MCMC parameter inference

**This study IS:**
- Reproducibility audit of Appendix A1 computational steps
- Internal reconstruction of possible H_MULT(z) bridge
- Preparation for author discussion
- Documentation for future reference

---

## Status Summary

| Item | Status |
|------|--------|
| Appendix A1 Steps 3–7 extraction | ✅ SOURCE_CONFIRMED |
| Table A1 transcription | ✅ COMPLETE |
| H_MULT performance vs. H_FLRW | ✅ 6× better fit |
| Sigma audit Rows 2–12 | ✅ PASSES |
| Row 1 sigma anomaly | ⚠️ OUTLIER, Q14 prepared |
| Bridge method identification | ❌ NOT_SOURCE_CONFIRMED, Q15 prepared |
| Hamiltonian bridge algebraic check | ✅ VALID, Q16 prepared |
| Cluster variable evolution | ❌ MISSING, Q17 prepared |
| MCMC readiness | ❌ BLOCKED (bridge + variables) |
| Prediction readiness | ❌ BLOCKED (bridge + variables) |
| Communication status | ⏳ WAITING for first letter response |

---

**Next step:** Wait for author response to initial letter, then discuss Q14–Q18 if appropriate.

**Project state:** CLEAN, DOCUMENTED, READY_FOR_AUTHOR_CONVERSATION
