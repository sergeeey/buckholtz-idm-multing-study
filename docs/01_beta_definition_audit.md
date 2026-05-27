# Beta Definition Audit

## Purpose

Clarify the definitions, values, units, and normalizations of `beta_d` and `beta_q`.

---

## Known Candidate Values

| Parameter | Candidate value | Source | Units | Interpretation | Status | Notes |
|---|---:|---|---|---|---|---|
| beta_d | 4.25 | Requires clarification | dimensionless or length | Dipole scale parameter (candidate 1) | unclear | From H(z) fitting contexts |
| beta_d | 0.78 | Requires clarification | dimensionless or length | Dipole scale parameter (candidate 2) | unclear | Different context, relationship to 4.25 unclear |
| beta_q | 8.10 | Requires clarification | dimensionless or length² | Quadrupole scale parameter (candidate 1) | unclear | From H(z) fitting contexts |
| beta_q | 0.19 | Requires clarification | dimensionless or length² | Quadrupole scale parameter (candidate 2) | unclear | Different context, relationship to 8.10 unclear |

---

## Key Uncertainty

**Are beta_d/beta_q values such as 4.25/8.10 and 0.78/0.19:**
1. Different parameters?
2. Different normalizations of the same parameter?
3. Different versions of the model?
4. Different supplementary calculations?

This requires clarification from Dr. Buckholtz.

---

## Questions for Dr. Buckholtz

1. Are `beta_d` and `beta_q` currently intended as **fitted phenomenological parameters**?
2. Are they expected to be **derivable** from IDM/MULTING internal structure?
3. Which values and normalizations should be considered **current**?
4. Do the different candidate values represent:
   - Different normalization choices (e.g., normalized by different length scales)?
   - Different physical contexts (cosmological vs cluster scales)?
   - Evolution of the model over time?
5. What are the **units** of beta_d and beta_q? Are they dimensionless, or do they have length/length² dimensions?

---

## Proposed Path Forward

1. **Clarify definitions** — obtain explicit formula for beta_d and beta_q in terms of other quantities
2. **Clarify units** — dimensional analysis to determine physical interpretation
3. **Clarify normalization** — if multiple values exist, document which normalization applies where
4. **Separate fitted vs derived** — classify whether betas are:
   - Phenomenological fits to H(z) data
   - Derived from IDM structure
   - Mixed (some aspects fitted, some derived)

---

## Status

**Current implementation:** All beta candidates marked as `status="unclear"` with placeholder sources.

**Blocker:** Cannot proceed with H(z) simulation or beta-based predictions until definitions are clarified.

**Next step:** Request clarification from Dr. Buckholtz using questions above.
