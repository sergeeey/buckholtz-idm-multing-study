Running Table A1 Reverse Engineering Diagnostics...
======================================================================
# Table A1 Reverse Engineering — Diagnostic Results

**Date:** 2026-05-29
**Source:** data/table_a1_reported.csv (12 rows, z=0 to 8.5)
**Status:** AI_INTERPRETATION_CANDIDATE / PHENOMENOLOGICAL_FIT_ONLY

---

## Test A — Closeness to Observed H

### MULT
```
Mean |residual|: 1.27 km/s/Mpc
RMS residual: 1.42 km/s/Mpc
Mean |sigma|: 0.22
RMS sigma: 0.40
Max |sigma|: 1.30
Status: table_reported_fit_output
```

### FLRW
```
Mean |residual|: 8.13 km/s/Mpc
RMS residual: 9.42 km/s/Mpc
Mean |sigma|: 1.20
RMS sigma: 1.86
Max |sigma|: 5.60
Status: reverse_engineering_diagnostic
```

### W_EFF
```
Mean |residual|: 0.27 km/s/Mpc
RMS residual: 0.31 km/s/Mpc
Mean |sigma|: 0.04
RMS sigma: 0.06
Max |sigma|: 0.10
Status: post_hoc_diagnostic_only
```

---

## Test B — Sigma Consistency

### MULT
```
H_MULT:
  Reported mean sigma: 0.156
  Calculated mean sigma: -0.099
  Mean absolute diff: 0.260
  Max absolute diff: 3.027
  Tolerance: 3.5
  Result: ✅ PASS
```

### FLRW
```
H_FLRW:
  Reported mean sigma: -1.200
  Calculated mean sigma: -1.152
  Mean absolute diff: 0.062
  Max absolute diff: 0.509
  Tolerance: 3.5
  Result: ✅ PASS
```

---

## Test C — Relation to H_FLRW

```
H_MULT / H_FLRW:
  Mean ratio: 1.0712
  Std ratio: 0.0297
H_MULT - H_FLRW:
  Mean difference: 8.43 km/s/Mpc
  Std difference: 4.60 km/s/Mpc
Correlation H_MULT vs H_FLRW: 0.9996
Correlation residuals: 0.3895
Status: ai_interpretation_candidate
```

---

## Test D — Inferred Phi(z)

```
Anchor: z=0.00, H_anchor=71.10 km/s/Mpc
Phi_relative range: [0.9748, 34.5797]
Status: ai_interpretation_candidate — NOT SOURCE_CONFIRMED
```

---

## Test E — Force Ratio Correlation

```
Status: blocked_missing_cluster_variables
Reason: Cluster variables not provided in Table A1
Missing: m_A(z), r_A(z), k_A(z), D_CAB(z)
```

---

## Test F — w_eff Diagnostic

```
w_eff better than H_MULT? True
w_eff better than H_FLRW? True
Mean w_eff: -1.056
Std w_eff: 0.104
Status: post_hoc_diagnostic_only — post-hoc, not forward model
```

---

## Test G — Polynomial Correction to H_FLRW

### Degree 1
```
Degree: 1
Coefficients: [-0.0050, 0.0808]
RMS residual: 0.03 km/s/Mpc
Overfitting risk: LOW
Status: phenomenological_fit_only — phenomenological, not physics
```

### Degree 2
```
Degree: 2
Coefficients: [0.0000, -0.0052, 0.0809]
RMS residual: 0.03 km/s/Mpc
Overfitting risk: LOW
Status: phenomenological_fit_only — phenomenological, not physics
```

### Degree 3
```
Degree: 3
Coefficients: [0.0017, -0.0202, 0.0488, 0.0636]
RMS residual: 0.02 km/s/Mpc
Overfitting risk: MEDIUM
Status: phenomenological_fit_only — phenomenological, not physics
```

---

## Safety Markers

- ✅ All results marked NOT_SOURCE_CONFIRMED
- ✅ MCMC remains BLOCKED
- ✅ No prediction on new z allowed
- ✅ Polynomial fits marked PHENOMENOLOGICAL_FIT_ONLY
- ✅ Phi(z) inference marked AI_INTERPRETATION_CANDIDATE
- ✅ Force ratio test BLOCKED (missing cluster variables)

---

**End of Diagnostics**
