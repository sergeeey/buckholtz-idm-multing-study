# Derived / Fitted / Assumed / Unknown Matrix

## Purpose

Separate what is derived, what is fitted to data, what is assumed, and what is unknown.

This prevents mixing different epistemic categories and clarifies which claims require which types of evidence.

---

## Matrix

| Item | Category | Source | Why this category | Risk | Next check |
|---|---|---|---|---|---|
| **6 isomers** | hypothesis | Buckholtz communications | Proposed structure, not yet tested observationally | High — foundational claim without observational confirmation | Request: (1) isomer definition, (2) observational signatures, (3) falsification criteria |
| **5 dark / 1 ordinary ratio** | assumption | Buckholtz communications | Ratio stated but derivation unclear | High — if assumed, not fundamental; if derived, need derivation | Clarify: derived from IDM internal structure or phenomenological choice? |
| **beta_d (4.25)** | unclear | Requires clarification | Multiple candidate values, context unclear | High — critical parameter with ambiguous definition | Clarify: fitted to H(z)? Derived from IDM? Normalization choice? |
| **beta_d (0.78)** | unclear | Requires clarification | Relationship to 4.25 unclear | High — same parameter or different context? | Same as above |
| **beta_q (8.10)** | unclear | Requires clarification | Multiple candidate values, context unclear | High — critical parameter with ambiguous definition | Clarify: fitted to H(z)? Derived from IDM? Normalization choice? |
| **beta_q (0.19)** | unclear | Requires clarification | Relationship to 8.10 unclear | High — same parameter or different context? | Same as above |
| **Eq.15 relation** | calculation | Buckholtz communications | Numerically reproduced (~1% error) | Medium — arithmetic confirmed, mechanism unknown | Mechanism for exponent 6 and prefactor 4/3 required |
| **Dipole repulsion** | hypothesis | Requires verification | MULTING term mentioned but functional form TBD | High — no functional form, no PPN check | Request explicit H(z, beta_d) formula + PPN mapping |
| **Quadrupole attraction** | hypothesis | Requires verification | MULTING term mentioned but functional form TBD | High — no functional form, no PPN check | Request explicit H(z, beta_q) formula + PPN mapping |
| **H(z) fit** | requires_clarification | Requires verification | Fit mentioned but methodology unclear | High — if betas are fitted to H(z), cannot claim to "predict" H(z) | Clarify: which dataset? Which free parameters? |
| **Future cosmic reversal** | hypothesis | Buckholtz communications | Proposed but not derived | Medium — prediction, requires mechanism | Clarify: at what redshift? Driven by what physics? |
| **Particle predictions (sub-eV, TeV)** | hypothesis | Buckholtz communications | Mentioned but derivation unclear | Medium — testable but need specifics | Request: masses, quantum numbers, detection signatures |

---

## Category Definitions

| Category | Meaning | Evidence required | Example |
|---|---|---|---|
| **fact** | Verified measurement/observation | Published data, PDG, CODATA | Electron mass = 0.511 MeV |
| **calculation** | Reproduced numerical result | Test passes, arithmetic verified | Eq.15 reproduction |
| **hypothesis** | Proposed but not yet tested | Falsification criterion, prediction | 6 isomers structure |
| **inference** | Logical conclusion from verified facts | Valid reasoning chain | Mass ratio from PDG values |
| **assumption** | Chosen premise without derivation | Explicit statement that it's assumed | 5 dark / 1 ordinary split (if not derived) |
| **fitted** | Phenomenological fit to data | Dataset specified, fit procedure documented | beta values from H(z) fit (if confirmed) |
| **derived** | Mathematically derived from other claims | Full derivation or reference | (none yet in IDM/MULTING) |
| **unknown** | Status not determined | N/A | Many MULTING details |
| **unclear** | Conflicting or ambiguous information | Clarification required | Beta candidate values |

---

## High-Risk Items Requiring Immediate Clarification

### 1. Beta definitions (beta_d, beta_q)
**Risk:** Core parameters with conflicting candidate values and unclear units.

**Impact:** Cannot implement H(z) solver, cannot make predictions, cannot test model.

**Questions:**
- Are these fitted or derived?
- What are the units?
- Which values are current?
- What is the relationship between candidate values?

### 2. MULTING functional forms
**Risk:** No explicit equations for monopole, dipole, quadrupole terms.

**Impact:** Cannot test against observations, cannot check PPN constraints.

**Questions:**
- What is H(z, beta_d, beta_q) explicitly?
- How do dipole/quadrupole terms enter the Friedmann equations?
- Are these modifications to the metric or to the energy-momentum tensor?

### 3. 5 dark / 1 ordinary ratio
**Risk:** If assumed, not fundamental; if derived, need derivation.

**Impact:** Foundational claim for IDM structure.

**Questions:**
- Is this ratio derived from symmetry arguments?
- Is it a phenomenological fit to observations?
- Is it an assumption?

---

## Derived vs Fitted vs Assumed: Decision Tree

```
For each claim:
  ├─ Is there a published derivation? → DERIVED
  │    └─ If yes: cite derivation
  │    └─ If no: continue
  │
  ├─ Is there a dataset and fit procedure? → FITTED
  │    └─ If yes: specify dataset, free parameters, goodness-of-fit
  │    └─ If no: continue
  │
  ├─ Is it explicitly stated as a premise? → ASSUMPTION
  │    └─ If yes: document as assumption, assess if testable
  │    └─ If no: continue
  │
  └─ Status unclear → UNKNOWN or UNCLEAR
       └─ Action: request clarification
```

---

## Observational Anchors vs Model Predictions

**Critical distinction:** What is input vs what is output?

| Item | Input or Output? | Dataset (if input) | Risk |
|---|---|---|---|
| Electron mass | Input | PDG 2022 | None (safe input) |
| Tau mass | Input | PDG 2022 | None (safe input) |
| H(z) cosmic chronometers | **Ambiguous** | Various surveys | High — if used to fit betas, cannot claim to "predict" H(z) |
| Planck CMB parameters | **Ambiguous** | Planck 2018 | High — if Omega_m used to derive betas, circular reasoning |
| beta_d, beta_q | **Ambiguous** | Unknown | High — unclear if input or output |
| Future cosmic reversal | Output (prediction) | N/A | None (testable prediction) |

**Action required:** Clarify which cosmological datasets (if any) were used to determine beta values.

---

## Status Summary

| Category | Count | Percentage |
|---|---:|---:|
| fact | 0 | 0% |
| calculation | 1 | 8% |
| hypothesis | 5 | 42% |
| inference | 0 | 0% |
| assumption | 1 | 8% |
| fitted | 0 | 0% |
| derived | 0 | 0% |
| unknown | 0 | 0% |
| unclear | 5 | 42% |
| **Total** | **12** | **100%** |

**Interpretation:**
- **50% unclear or hypothesis** — many foundational claims lack clear status
- **0% derived** — no explicit derivations available in repository
- **0% fitted with documented procedure** — if betas are fitted, procedure not documented

**Action:** Request clarification from Dr. Buckholtz to convert "unclear" items to definite categories.

---

## Next Steps

1. Request source verification for all "requires_source_verification" items
2. Request clarification for all "unclear" items (beta values, MULTING forms)
3. Request derivation or fit procedure documentation for all foundational claims
4. Update this matrix as information becomes available
5. Mark items as "fact" only after independent verification

---

**Epistemic discipline principle:**  
> Better to mark something as "unclear" or "unknown" than to silently assume it is "fact" or "derived".
