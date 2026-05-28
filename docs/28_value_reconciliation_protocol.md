# Value Reconciliation Protocol

**Purpose:** Define step-by-step procedures for handling conflicting values from different sources in the Buckholtz IDM/MULTING audit.

**Status:** Active protocol (v1.0, 2026-05-28)

**Core principle:** Values from different sources are NEVER mixed silently. Every computational use of a parameter must document which source was chosen and why.

---

## 1. Provenance Tagging (Mandatory First Step)

**Before using ANY value computationally:**

### Step 1.1: Create ProvenanceTag

```python
from datetime import date
from src.source_provenance import (
    register_value,
    SourceType,
    DerivationStatus,
    UsePermission,
)

# Example: Register beta_d = 4.5 from manuscript Table A1
tag = register_value(
    symbol="beta_d",
    value=4.5,
    source_type=SourceType.MANUSCRIPT_TABLE,
    derivation_status=DerivationStatus.FITTED,
    use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
    manuscript_identifier="preprints202511.0598.v6.pdf",
    location="Appendix A.3, Table A1",
    verification_date=date(2026, 5, 27),
    verified_by="manual_verification",
    notes="AI-assisted thought experiment, fitted to minimize H(z) deviations",
    units="dimensionless",
)
```

### Step 1.2: Tag Every Alternative Value

If multiple values exist for same symbol (e.g., beta_d = 4.25 from audit):

```python
# Register audit-reconstructed alternative
tag_audit = register_value(
    symbol="beta_d",
    value=4.25,
    source_type=SourceType.AUDIT_RECONSTRUCTION,
    derivation_status=DerivationStatus.RECONSTRUCTED,
    use_permission=UsePermission.DO_NOT_USE,
    location="docs/13_internal_anchor_uniqueness.md",
    notes="Audit inference: beta_d_1 = 17/4. NOT confirmed by Buckholtz. 7 alternative formulas within 1.2% error.",
    units="dimensionless",
)
```

**Rule:** Every value from every source gets exactly one ProvenanceTag.

---

## 2. Conflict Detection (Automatic)

### Step 2.1: Check for Conflicts

```python
from src.source_provenance import get_registry
from src.conflict_resolver import ConflictResolver

registry = get_registry()
resolver = ConflictResolver(registry)

# Check if symbol has conflicts
if registry.has_conflict("beta_d"):
    print("⚠️ CONFLICT DETECTED for beta_d")
    report = resolver.diagnose("beta_d")
    print(f"Severity: {report.severity.value}")
    print(f"Strategy: {report.recommended_strategy.value}")
```

### Step 2.2: Automatic Conflict Report

Conflict severity is automatically classified:

| Severity | Relative spread | Example |
|----------|-----------------|---------|
| NONE | <1% | Single value or rounding differences |
| MINOR | 1-5% | beta_d = 4.5 vs 4.7 (4.3% difference) |
| MODERATE | 5-20% | beta_d = 4.5 vs 4.25 (5.9% difference) |
| MAJOR | >20% | beta_d = 4.5 vs 0.78 (82.7% difference) |
| CRITICAL | Fitted vs derived | Epistemological incompatibility |

---

## 3. Resolution Decision Tree

### Decision Tree

```
Has conflict?
├─ NO → Use single value (check use_permission)
│
└─ YES → Assess severity
    ├─ CRITICAL (fitted vs derived)
    │   └─ → REQUIRE_CLARIFICATION (block all use)
    │
    ├─ MAJOR (>20% spread)
    │   ├─ Has authoritative (manuscript) value?
    │   │   ├─ YES → PREFER_AUTHORITATIVE
    │   │   └─ NO → REQUIRE_CLARIFICATION
    │   │
    │   └─ → BLOCK (send author question)
    │
    ├─ MODERATE (5-20% spread)
    │   ├─ Has authoritative value?
    │   │   ├─ YES (single) → PREFER_AUTHORITATIVE
    │   │   ├─ YES (multiple) → REQUIRE_CLARIFICATION
    │   │   └─ NO → REQUIRE_CLARIFICATION
    │   │
    │   └─ → Document choice OR block
    │
    └─ MINOR (<5% spread)
        └─ → USER_DECISION (document choice)
```

### Resolution Strategies

**PREFER_AUTHORITATIVE:**
- Use manuscript table/text/equation value
- Document: "Using X from manuscript Table Y, preferring authoritative source over audit reconstruction"
- Log alternative values for reference

**PREFER_FITTED:**
- Use fitted value for phenomenological parameters
- Document circular reasoning guard
- Block predictions, allow fit reproduction only

**PREFER_DERIVED:**
- Use derived value for theoretical constants
- Document derivation mechanism
- Allow predictions if mechanism sound

**REQUIRE_CLARIFICATION:**
- BLOCK all computational use
- Send question to author (docs/26 template)
- Document blocker explicitly in code

**USER_DECISION:**
- Minor conflicts only
- Present options to user
- Document choice in experiment log

---

## 4. Safe Usage Pattern (Code Template)

### Template 1: Get Canonical Value with Conflict Check

```python
from src.source_provenance import get_registry
from src.conflict_resolver import ConflictResolver, ConflictSeverity

def get_parameter_safe(
    symbol: str,
    use_case: str = "fit_reproduction",
    allow_conflicts: bool = False,
):
    """Get parameter value with automatic conflict checking.

    Args:
        symbol: Parameter name (e.g., "beta_d")
        use_case: "fit_reproduction", "toy_modeling", or "prediction"
        allow_conflicts: If False (default), raise on moderate/major conflicts

    Returns:
        (value, provenance_tag)

    Raises:
        ValueError: If conflict detected and not allowed
    """
    registry = get_registry()
    resolver = ConflictResolver(registry)

    # Check for conflicts
    report = resolver.diagnose(symbol)

    if report:
        # Conflict exists
        if not allow_conflicts:
            if report.severity in (
                ConflictSeverity.MODERATE,
                ConflictSeverity.MAJOR,
                ConflictSeverity.CRITICAL,
            ):
                raise ValueError(
                    f"Conflict for {symbol} (severity: {report.severity.value}). "
                    f"Resolution required. See docs/27_source_conflict_log.md"
                )

        print(f"⚠️ Using {symbol} despite conflict: {report.safe_wording}")

    # Get canonical value
    tag = resolver.resolve(symbol, use_case)

    if tag is None:
        raise ValueError(f"No value available for {symbol} with use_case={use_case}")

    return tag.value, tag


# Usage example
try:
    beta_d, beta_d_tag = get_parameter_safe("beta_d", use_case="fit_reproduction")
    print(f"Using beta_d = {beta_d:.4f}")
    print(f"Source: {beta_d_tag.source_type.value}")
    print(f"Derivation: {beta_d_tag.derivation_status.value}")
    print(f"Use permission: {beta_d_tag.use_permission.value}")
except ValueError as e:
    print(f"BLOCKED: {e}")
    # Send clarification request to author
```

### Template 2: Explicit Conflict Acknowledgment

```python
# When using value despite known conflict (ONLY for minor conflicts)
def use_with_conflict_acknowledgment(symbol: str, use_case: str):
    """Use parameter with explicit conflict acknowledgment.

    Use ONLY when:
    - Conflict severity is MINOR
    - User has made explicit choice
    - Choice is documented in experiment log
    """
    registry = get_registry()
    resolver = ConflictResolver(registry)

    report = resolver.diagnose(symbol)

    if report and report.severity != ConflictSeverity.MINOR:
        raise ValueError(
            f"Cannot use {symbol} with severity {report.severity.value}. "
            "Only MINOR conflicts can be overridden with explicit acknowledgment."
        )

    # Log conflict acknowledgment
    print(f"CONFLICT ACKNOWLEDGED for {symbol}:")
    print(f"  Severity: {report.severity.value}")
    print(f"  Strategy: {report.recommended_strategy.value}")
    print(f"  Safe wording: {report.safe_wording}")

    # Get canonical value
    tag = resolver.resolve(symbol, use_case)

    # Document choice in code comments
    # CONFLICT: beta_d has 3 values (4.5, 4.25, 0.78).
    # CHOICE: Using 4.5 from manuscript Table A1 (authoritative source).
    # ALTERNATIVES: 4.25 and 0.78 from audit reconstruction (not source-confirmed).
    # JUSTIFICATION: Prefer manuscript over audit inference.
    # DATE: 2026-05-28

    return tag.value, tag
```

---

## 5. Documentation Requirements

**Before using any parameter in computation:**

### Required Documentation (in code)

```python
# Example: beta_d usage documentation
beta_d = 4.5  # DO NOT USE — insufficient documentation

# CORRECT:
beta_d = 4.5  # preprints202511.0598.v6.pdf, Appendix A.3, Table A1
              # SOURCE: manuscript_table
              # DERIVATION: fitted (AI-assisted, minimize H(z) deviations)
              # USE PERMISSION: fit_reproduction_only (circular reasoning guard)
              # CONFLICT: alternatives 4.25, 0.78 from audit (NOT used)
              # VERIFIED: manual verification 2026-05-27
```

### Required Documentation (in experiment log)

```markdown
## Parameter Choices

### beta_d
- **Value used:** 4.5
- **Source:** preprints202511.0598.v6.pdf, Appendix A.3, Table A1
- **Derivation:** Fitted to H(z) observations
- **Use case:** Fit reproduction only
- **Conflict status:** MAJOR (alternatives: 4.25, 0.78)
- **Resolution:** PREFER_AUTHORITATIVE (manuscript table > audit)
- **Circular reasoning guard:** YES (fitted to H(z) → cannot predict H(z))
- **Date:** 2026-05-28

### beta_q
- **Value used:** 18.0
- **Source:** preprints202511.0598.v6.pdf, Appendix A.3, Table A1
- **Derivation:** Fitted to H(z) observations
- **Use case:** Fit reproduction only
- **Conflict status:** MAJOR (alternative: 8.10)
- **Resolution:** PREFER_AUTHORITATIVE
- **Date:** 2026-05-28
```

---

## 6. Forbidden Patterns (Anti-Patterns)

### ❌ FORBIDDEN: Silent Mixing

```python
# WRONG — using value without checking provenance
beta_d = 4.5
H_MULT = compute_h_mult(z, beta_d)  # Which beta_d? Where from? Why?
```

### ❌ FORBIDDEN: Averaging Conflicting Values

```python
# WRONG — averaging destroys source information
beta_d_values = [4.5, 4.25, 0.78]
beta_d = sum(beta_d_values) / len(beta_d_values)  # 3.18 (NONSENSE)
```

### ❌ FORBIDDEN: Ignoring Conflicts

```python
# WRONG — using value without resolving conflict
if registry.has_conflict("beta_d"):
    pass  # Ignore and proceed anyway
beta_d = registry.get_canonical("beta_d").value  # May fail or return wrong value
```

### ❌ FORBIDDEN: Undocumented Choice

```python
# WRONG — choosing value without documenting why
beta_d = 4.25  # Why 4.25? Why not 4.5 or 0.78?
```

---

## 7. Pre-Computation Checklist

Before running ANY computation using parameters:

- [ ] All parameters tagged with ProvenanceTag?
- [ ] Conflicts checked with ConflictResolver?
- [ ] Major/critical conflicts resolved or blocked?
- [ ] Resolution strategy documented in code?
- [ ] Use case (fit_reproduction / toy_modeling / prediction) specified?
- [ ] Circular reasoning guard in place (if fitted values)?
- [ ] Safe wording template used in reports?
- [ ] Experiment log updated with parameter choices?

**If ANY box unchecked → DO NOT proceed.**

---

## 8. Escalation Path

### When to Block (Cannot Proceed)

**Automatic blocks:**
- CRITICAL severity (fitted vs derived conflict)
- MAJOR severity without authoritative value
- Use case = "prediction" but use_permission = "fit_reproduction_only"
- Source type = SOURCE_MISSING

**Action:** Send clarification request (docs/26 template), mark as BLOCKED in discovery ledger.

### When to Escalate to User

**User decision required:**
- MINOR severity conflicts
- Multiple authoritative values (author contradiction)
- Ambiguous use case (unclear if fit/toy/prediction)

**Action:** Present options with pros/cons, document user choice.

### When to Proceed with Documentation

**Can proceed with documentation:**
- Single authoritative value (no conflict)
- MINOR conflict with explicit user choice
- MODERATE conflict resolved by PREFER_AUTHORITATIVE strategy

**Action:** Document choice, log in experiment notebook, continue.

---

## 9. Example Workflow: Adding New Parameter

**Scenario:** Need to use H0 (Hubble constant) from multiple sources.

### Step 1: Register all values

```python
# Planck 2018 value
register_value(
    symbol="H0",
    value=67.4,
    source_type=SourceType.EXTERNAL_REFERENCE,
    derivation_status=DerivationStatus.FITTED,
    use_permission=UsePermission.ALLOWED_FOR_PREDICTION,
    manuscript_identifier="Planck 2018, A&A 641, A6",
    notes="CMB-derived, ΛCDM model",
    units="km/s/Mpc",
)

# SH0ES 2022 value (Cepheid+SNIa)
register_value(
    symbol="H0",
    value=73.0,
    source_type=SourceType.EXTERNAL_REFERENCE,
    derivation_status=DerivationStatus.FITTED,
    use_permission=UsePermission.ALLOWED_FOR_PREDICTION,
    manuscript_identifier="Riess+ 2022, ApJ 934, L7",
    notes="Local distance ladder",
    units="km/s/Mpc",
)
```

### Step 2: Check for conflict

```python
resolver = ConflictResolver(get_registry())
report = resolver.diagnose("H0")

# Conflict: 67.4 vs 73.0 (8.1% difference → MODERATE)
# Strategy: REQUIRE_CLARIFICATION (Hubble tension, no consensus)
```

### Step 3: Document resolution

```python
# For ΛCDM comparison: use Planck value (consistent with ΛCDM fit to CMB)
# For local distance ladder: use SH0ES value
# For MULTING: ask Buckholtz which H0 was used in Table A1 fit

# Document in experiment log:
# H0 conflict: Using H0 = 67.4 km/s/Mpc (Planck 2018) for ΛCDM comparison.
# Rationale: Consistent with CMB-derived cosmology.
# Note: SH0ES gives H0 = 73.0 (Hubble tension unresolved).
```

---

## 10. Integration with Existing Systems

### beta_provenance.py

```python
# beta_provenance.py already uses this system:
from src.source_provenance import register_value, SourceType, DerivationStatus, UsePermission
from datetime import date

beta_d_A1 = register_value(
    symbol="beta_d",
    value=4.5,
    source_type=SourceType.MANUSCRIPT_TABLE,
    derivation_status=DerivationStatus.FITTED,
    use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
    # ... rest of fields
)
```

### Future: H_MULT solver

```python
# When H_MULT formula received and implemented:
def compute_h_mult(z, use_case="fit_reproduction"):
    """Compute H_MULT(z) with provenance checking.

    Args:
        z: Redshift
        use_case: "fit_reproduction", "toy_modeling", or "prediction"

    Returns:
        H_MULT value

    Raises:
        ValueError: If parameters have unresolved conflicts
    """
    # Get parameters with conflict checking
    beta_d, beta_d_tag = get_parameter_safe("beta_d", use_case)
    beta_q, beta_q_tag = get_parameter_safe("beta_q", use_case)

    # Document parameter sources in output
    metadata = {
        "beta_d": beta_d_tag.to_dict(),
        "beta_q": beta_q_tag.to_dict(),
        "use_case": use_case,
    }

    # Compute H_MULT (formula to be provided by Buckholtz)
    # H_MULT = ...

    return H_MULT, metadata
```

---

## 11. Audit Trail

**Every parameter use generates an audit trail entry:**

```json
{
  "timestamp": "2026-05-28T14:32:00Z",
  "symbol": "beta_d",
  "value": 4.5,
  "use_case": "fit_reproduction",
  "provenance_tag_id": "beta_d_MT_4.5000",
  "conflict_status": "MAJOR",
  "resolution_strategy": "PREFER_AUTHORITATIVE",
  "alternatives_rejected": [4.25, 0.78],
  "code_location": "src/h_mult_solver.py:42",
  "user": "audit_system",
  "notes": "Using manuscript Table A1 value, rejecting audit reconstruction"
}
```

Audit trail stored in: `data/parameter_audit_trail.jsonl`

---

## 12. Summary: Core Principles

1. **Tag everything** — every value from every source gets ProvenanceTag
2. **Check conflicts** — automatic detection via ConflictResolver
3. **Resolve explicitly** — document choice, never silent mixing
4. **Guard circular reasoning** — fitted values cannot predict same data
5. **Escalate ambiguity** — block use, send author clarification
6. **Document choices** — in code, logs, and audit trail
7. **Prefer authoritative** — manuscript > audit > AI
8. **Block major conflicts** — require clarification for >20% spread or fitted vs derived

---

**Protocol status:** ACTIVE v1.0  
**Last updated:** 2026-05-28  
**Next review:** After Buckholtz responds to clarification questions  
**Compliance:** Mandatory for all computational use of parameters
