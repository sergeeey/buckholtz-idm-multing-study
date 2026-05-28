# Source Conflict Log — Buckholtz IDM/MULTING Audit

**Purpose:** Track all source conflicts detected during audit where multiple values exist for the same symbol from different sources (manuscript, AI transcript, audit reconstruction, supplementary notes).

**Status:** Active tracking (updated 2026-05-28)

**Audit principle:** Values from different sources are NEVER mixed silently. Each conflict is documented, classified by severity, and resolved according to explicit precedence rules.

---

## Classification System

### Conflict Severity

| Severity | Definition | Numerical spread | Action |
|----------|------------|------------------|--------|
| **NONE** | Single value or within tolerance | <1% difference | No conflict |
| **MINOR** | Multiple values within precision/rounding | 1-5% difference | Document choice |
| **MODERATE** | Values differ (different sources) | 5-20% difference | Prefer authoritative |
| **MAJOR** | Fundamental disagreement | >20% difference | Require clarification |
| **CRITICAL** | Incompatible epistemologies | Fitted vs derived | Block all use |

### Resolution Strategies

| Strategy | When applied | Action |
|----------|-------------|--------|
| **PREFER_AUTHORITATIVE** | Manuscript table exists | Use manuscript value, document choice |
| **PREFER_FITTED** | Phenomenological parameters | Use fitted value with circular reasoning guard |
| **PREFER_DERIVED** | Theoretical constants | Use derived value if mechanism clear |
| **REQUIRE_CLARIFICATION** | Major/critical conflicts | Block use, send author question |
| **BLOCK_ALL_USE** | Unresolvable ambiguity | Block computational use entirely |
| **USER_DECISION** | Minor conflicts with valid alternatives | Present options, document choice |

---

## Conflict 1: beta_d (Multiple Values)

### Detected Values

| Value | Source | Derivation | Use Permission | Location |
|-------|--------|------------|----------------|----------|
| **4.5** | Manuscript Table | **FITTED** | Fit reproduction only | preprints202511.0598.v6.pdf, Appendix A.3, Table A1 |
| 4.25 | Audit reconstruction | RECONSTRUCTED | Do not use | docs/13_internal_anchor_uniqueness.md (beta_d_1 = 17/4) |
| 0.78 | Audit reconstruction | RECONSTRUCTED | Do not use | docs/13_internal_anchor_uniqueness.md (beta_d_2 = 7/9) |

### Conflict Analysis

**Severity:** MAJOR  
**Reason:** 4.5 vs 4.25 (5.9% difference), 4.5 vs 0.78 (82.7% difference)

**Epistemological status:**
- 4.5: **Manuscript-reported fitted value** (author statement, AI-assisted thought experiment)
- 4.25: **Audit reconstruction from internal anchors** (OUR inference: beta_d_1 = 17/4, NOT confirmed by Buckholtz)
- 0.78: **Audit reconstruction from internal anchors** (OUR inference: beta_d_2 = 7/9, NOT confirmed by Buckholtz)

**Critical distinction:**
- 4.5 is **explicitly stated** by Buckholtz in Table A1
- 4.25 and 0.78 are **audit inferences** — testing OUR pattern-matching hypothesis, NOT Buckholtz's model

### Resolution

**Strategy:** PREFER_AUTHORITATIVE

**Canonical value:** beta_d = **4.5** (manuscript table)

**Rationale:**
1. Manuscript table value is explicitly stated by author
2. Audit-reconstructed values (4.25, 0.78) are OUR hypotheses about Buckholtz's method
3. Testing audit inference = testing OUR model, not Buckholtz's model (circular reasoning)
4. Cannot use audit values computationally without author confirmation

**Use permission:**
- beta_d = 4.5: ✅ **Allowed for fit reproduction only** (fitted to H(z))
- beta_d = 4.25: ❌ **Do not use** (audit reconstruction, 7 alternative formulas within 1.2% error)
- beta_d = 0.78: ❌ **Do not use** (audit reconstruction, 20 alternative formulas within 5% error)

**Action taken:**
- beta_provenance.py uses beta_d_A1 = 4.5 exclusively
- Audit-reconstructed values documented in docs/13 but NOT used computationally
- Numerology risk documented (uniqueness score 0.10-0.40)

### Safe vs Unsafe Wording

✅ **Safe:**
- "Manuscript reports beta_d = 4.5 (fitted to H(z) observations). Audit reconstruction suggests alternative candidates (4.25, 0.78) but these are not source-confirmed."
- "Using beta_d = 4.5 from Table A1. Note: This is a fitted value, not derived, so predictions are blocked (circular reasoning)."
- "Audit identified 7-20 alternative formulas matching candidate values within small error margins. Author clarification needed to resolve ambiguity."

❌ **Unsafe:**
- "beta_d = 4.25 from Eq.20" (WE inferred this, not stated by Buckholtz)
- "Using beta_d = 0.78" (no source confirmation, high numerology risk)
- "Beta values uniquely determined" (conflict exists, multiple alternatives)
- "Audit confirms beta_d = 17/4" (audit PROPOSES, does NOT confirm)

---

## Conflict 2: beta_q (Multiple Values)

### Detected Values

| Value | Source | Derivation | Use Permission | Location |
|-------|--------|------------|----------------|----------|
| **18.0** | Manuscript Table | **FITTED** | Fit reproduction only | preprints202511.0598.v6.pdf, Appendix A.3, Table A1 |
| 8.10 | Audit reconstruction | RECONSTRUCTED | Do not use | docs/13_internal_anchor_uniqueness.md (beta_q_2 = 81/10) |
| 0.19 | AI-generated supplementary | INFERRED | Do not use | (hypothetical, if AI transcript existed) |

### Conflict Analysis

**Severity:** MAJOR  
**Reason:** 18.0 vs 8.10 (55.0% difference)

**Epistemological status:**
- 18.0: **Manuscript-reported fitted value** (author statement)
- 8.10: **Audit reconstruction from internal anchors** (OUR inference: beta_q_2 = 81/10)
- 0.19: **AI-generated supplementary** (if exists — hypothetical example)

**Critical distinction:**
- 18.0 is **author-stated** in primary manuscript
- 8.10 is **audit pattern-matching** (NOT author confirmation)
- 0.19 would be **AI hallucination** (not author-generated)

### Resolution

**Strategy:** PREFER_AUTHORITATIVE

**Canonical value:** beta_q = **18.0** (manuscript table)

**Rationale:**
1. Manuscript table value is explicit
2. Audit-reconstructed 8.10 is OUR hypothesis (81/10 from internal anchor 81)
3. AI-generated values are NOT author-generated (even if AI prompted by author)

**Use permission:**
- beta_q = 18.0: ✅ **Allowed for fit reproduction only** (fitted to H(z))
- beta_q = 8.10: ❌ **Do not use** (audit reconstruction, NOT source-confirmed)
- beta_q = 0.19: ❌ **Do not use** (AI-generated, NOT author-stated)

**Action taken:**
- beta_provenance.py uses beta_q_A1 = 18.0 exclusively
- Audit-reconstructed 8.10 documented but NOT used

### Safe vs Unsafe Wording

✅ **Safe:**
- "Manuscript reports beta_q = 18.0 (fitted). Audit reconstruction suggests 8.10 (81/10) but this is not source-confirmed."
- "Using beta_q = 18.0 from Table A1 with circular reasoning guard (fitted to H(z))."

❌ **Unsafe:**
- "beta_q = 8.10 from internal anchors" (OUR inference, not Buckholtz statement)
- "AI-generated beta_q = 0.19 is valid" (AI ≠ author, even if author-prompted)
- "Beta values are well-defined" (conflict exists, 55% difference)

---

## Conflict 3: H-MULT Functional Form (Source Missing)

### Detected Values

| Value | Source | Derivation | Use Permission | Location |
|-------|--------|------------|----------------|----------|
| *Unknown* | SOURCE_MISSING | UNKNOWN | Requires clarification | Manuscript mentions "monopole, dipole, quadrupole" but NO explicit formula |

### Conflict Analysis

**Severity:** CRITICAL (BLOCKER)  
**Reason:** Formula not provided in manuscript

**Epistemological status:**
- Manuscript mentions monopole/dipole/quadrupole terms
- NO explicit combination formula H_MULT(z; beta_d, beta_q)
- Cannot guess formula without author confirmation

**Multiple possible interpretations:**
```
Variant A: H_MULT = H_monopole + beta_d * H_dipole(z) + beta_q * H_quadrupole(z)
Variant B: H_MULT = H_monopole * (1 + beta_d * f_d(z) + beta_q * f_q(z))
Variant C: Other combination
```

All variants are plausible — cannot choose without clarification.

### Resolution

**Strategy:** REQUIRE_CLARIFICATION

**Canonical value:** BLOCKED (formula missing)

**Rationale:**
1. Guessing formula = implementing OUR model, not Buckholtz's
2. Different functional forms give different H(z) predictions
3. Fit reproduction requires EXACT formula from manuscript

**Action taken:**
- Priority 1 question sent to Dr. Buckholtz (docs/26, Q1)
- H_MULT(z) implementation blocked until formula received
- Table A1 fit reproduction blocked

### Safe vs Unsafe Wording

✅ **Safe:**
- "H-MULT functional form is not explicitly stated in available manuscript materials. Request for explicit formula sent to author (Priority 1). Fit reproduction blocked pending response."
- "Manuscript mentions monopole/dipole/quadrupole terms but does not provide combination formula."

❌ **Unsafe:**
- "H-MULT formula is H_FLRW + beta_d * dipole + beta_q * quadrupole" (guessing, not confirmed)
- "Formula is obvious from context" (it's not)
- "We can infer the formula" (no — explicit confirmation required)
- "Implementing best guess" (testing OUR guess, not Buckholtz's model)

---

## Conflict 4: m_A, r_A, k_A, D_C:AB (AI-Estimated vs Fixed)

### Detected Values

**Status:** SOURCE_MISSING (clarification needed)

### Conflict Analysis

**Severity:** MODERATE  
**Reason:** Unclear which quantities are free parameters vs fixed inputs

**Manuscript statement (Appendix A.3):**
> "The online service estimated values for m_A, r_A, k_A, D_C:AB and selected beta_d and beta_q."

**Ambiguity:**
- Were m_A, r_A, k_A, D_C:AB **estimated by AI** (free parameters)?
- Or were they **fixed inputs** to AI (constraints)?
- Which quantities are independent vs derived?

**Impact:**
- Counting free parameters: 2 (beta_d, beta_q) vs 6 (all of above)?
- Overfitting risk: more parameters → easier to fit any dataset
- AIC/BIC comparison requires exact parameter count

### Resolution

**Strategy:** REQUIRE_CLARIFICATION

**Canonical value:** BLOCKED (parameter count unknown)

**Rationale:**
1. Cannot compute AIC/BIC without knowing number of free parameters
2. Cannot assess overfitting risk
3. Cannot fair comparison with ΛCDM (2 parameters: H0, Omega_m)

**Action taken:**
- Priority 4 question sent to Dr. Buckholtz (docs/26, Q4)
- AIC/BIC computation blocked until clarified

### Safe vs Unsafe Wording

✅ **Safe:**
- "Manuscript mentions AI estimated m_A, r_A, k_A, D_C:AB but does not clarify which were free parameters vs fixed inputs. Parameter count unknown."
- "Cannot compute AIC/BIC until number of free parameters is clarified."

❌ **Unsafe:**
- "MULTING has 2 free parameters" (may be 6)
- "MULTING has same parameter count as ΛCDM" (unknown)
- "Overfitting is not a concern" (cannot assess without parameter count)

---

## Summary Statistics

| Conflict | Severity | Strategy | Status |
|----------|----------|----------|--------|
| beta_d (4.5 vs 4.25 vs 0.78) | MAJOR | PREFER_AUTHORITATIVE | ✅ Resolved (use 4.5) |
| beta_q (18.0 vs 8.10) | MAJOR | PREFER_AUTHORITATIVE | ✅ Resolved (use 18.0) |
| H-MULT formula (missing) | CRITICAL | REQUIRE_CLARIFICATION | ❌ BLOCKED (Q1 sent) |
| m_A, r_A, k_A, D_C:AB (AI-estimated vs fixed) | MODERATE | REQUIRE_CLARIFICATION | ❌ BLOCKED (Q4 sent) |

**Total conflicts:** 4  
**Resolved:** 2 (beta_d, beta_q)  
**Blocked:** 2 (H-MULT formula, parameter count)

---

## Precedence Rules (Global)

When multiple values exist for same symbol:

1. **Manuscript table** > manuscript text > manuscript equation
2. **Authoritative** (author-stated) > audit reconstruction > AI-generated
3. **Fitted values** (for phenomenological params) > reconstructed (if authoritative source unavailable)
4. **Derived values** (for theoretical constants) > fitted (if mechanism clear)
5. **Major/critical conflicts** → BLOCK use, require clarification
6. **Minor conflicts** → document choice, note uncertainty

**Hard rule:** NEVER mix values from different sources without explicit documentation and justification.

---

## Conflict Detection Protocol

Before using ANY parameter value computationally:

1. Check ProvenanceRegistry for all registered values of that symbol
2. If multiple values exist → run ConflictResolver.diagnose()
3. If conflict severity ≥ MODERATE → BLOCK use, escalate
4. If conflict severity = MINOR → document choice explicitly
5. Log choice in experiment notebook / code comments

**Example (beta_d):**
```python
from src.conflict_resolver import ConflictResolver
from src.source_provenance import get_registry

resolver = ConflictResolver(get_registry())

# Check for conflicts before use
report = resolver.diagnose("beta_d")

if report and report.severity in (ConflictSeverity.MAJOR, ConflictSeverity.CRITICAL):
    raise ValueError(f"Cannot use beta_d: {report.resolution_notes}")

# Get canonical value with explicit use case
beta_d_tag = resolver.resolve("beta_d", use_case="fit_reproduction")
beta_d = beta_d_tag.value  # 4.5

# Document choice in code
# Using beta_d = 4.5 from Table A1 (manuscript-reported fitted value).
# Audit-reconstructed 4.25 and 0.78 NOT used (not source-confirmed).
```

---

## Next Actions

**Immediate:**
1. ✅ DONE: Resolve beta_d conflict (prefer 4.5 from Table A1)
2. ✅ DONE: Resolve beta_q conflict (prefer 18.0 from Table A1)
3. ⏸️ WAITING: H-MULT formula clarification (Q1 sent to Buckholtz)
4. ⏸️ WAITING: Parameter count clarification (Q4 sent to Buckholtz)

**After Buckholtz response:**
1. Register H-MULT formula in ProvenanceRegistry with MANUSCRIPT_EQUATION source
2. Register parameter count (m_A, r_A, k_A, D_C:AB status)
3. Update conflict log if new conflicts detected
4. Proceed with fit reproduction

**Long-term:**
1. Extend ProvenanceRegistry to ALL physical constants (H0, Omega_m, c, G, etc.)
2. Automate conflict detection in CI/CD (pytest pre-commit hook)
3. Create visualization of provenance graph (symbol → sources → conflicts)

---

**Document status:** ACTIVE — updated as new conflicts detected  
**Last updated:** 2026-05-28  
**Next review:** After Buckholtz responds to docs/26 clarification questions
