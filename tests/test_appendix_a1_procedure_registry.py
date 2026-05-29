"""
Tests for Appendix A1 Procedure Registry

Verifies that the forensic extraction correctly encodes what is SOURCE_CONFIRMED
vs UNDER_SPECIFIED vs BLOCKED.
"""

from src.appendix_a1_procedure_registry import (
    BLOCKED_OPERATIONS,
    STEPS,
    TABLE_A1,
    VARIABLES,
    CodePermission,
    VariableProvenance,
    get_beta_d_table_a1,
    get_beta_q_table_a1,
    get_bridge_finding,
    get_step,
    get_variable,
    is_operation_allowed,
    is_operation_blocked,
)

# ============================================================================
# Test Variable Provenance
# ============================================================================


def test_all_variables_have_provenance():
    """Every variable must have provenance tag."""
    for var in VARIABLES:
        assert var.provenance is not None
        assert var.code_permission is not None


def test_beta_d_beta_q_are_fitted_phenomenological():
    """β_d and β_q MUST be marked as FITTED_PHENOMENOLOGICAL."""
    beta_d = get_variable("β_d")
    beta_q = get_variable("β_q")

    assert beta_d is not None
    assert beta_q is not None

    assert beta_d.provenance == VariableProvenance.FITTED_PHENOMENOLOGICAL
    assert beta_q.provenance == VariableProvenance.FITTED_PHENOMENOLOGICAL

    # Can use for table reproduction ONLY
    assert beta_d.code_permission == CodePermission.ALLOWED_FOR_TABLE_REPRODUCTION_ONLY
    assert beta_q.code_permission == CodePermission.ALLOWED_FOR_TABLE_REPRODUCTION_ONLY


def test_h_mult_is_under_specified():
    """H-MULT MUST be marked as UNDER_SPECIFIED (formula missing)."""
    h_mult = get_variable("H-MULT")

    assert h_mult is not None
    assert h_mult.provenance == VariableProvenance.UNDER_SPECIFIED
    assert h_mult.code_permission == CodePermission.BLOCKED


def test_h_data_is_data():
    """H-data MUST be marked as DATA (observational)."""
    h_data = get_variable("H-data")

    assert h_data is not None
    assert h_data.provenance == VariableProvenance.DATA
    assert h_data.code_permission == CodePermission.CODE_READY


def test_cluster_parameters_are_ai_estimated():
    """m_A, r_A, D_C:AB, k_A/c² MUST be AI_ESTIMATED."""
    cluster_params = ["m_A", "r_A", "D_C:AB", "k_A/c²"]

    for symbol in cluster_params:
        var = get_variable(symbol)
        assert var is not None, f"{symbol} not found"
        assert var.provenance == VariableProvenance.AI_ESTIMATED
        assert var.code_permission == CodePermission.NOT_CODE_READY


# ============================================================================
# Test Steps 3–7
# ============================================================================


def test_all_steps_represented():
    """Steps 3, 4, 5, 6, 7 MUST be represented."""
    step_numbers = [step.step_number for step in STEPS]
    assert 3 in step_numbers
    assert 4 in step_numbers
    assert 5 in step_numbers
    assert 6 in step_numbers
    assert 7 in step_numbers


def test_step_5_is_under_specified():
    """Step 5 MUST be marked as UNDER_SPECIFIED."""
    step5 = get_step(5)

    assert step5 is not None
    assert "UNDER_SPECIFIED" in step5.status
    assert not step5.code_ready
    assert step5.ai_discretion_allowed


def test_step_6_is_blocked():
    """Step 6 MUST be marked as BLOCKED."""
    step6 = get_step(6)

    assert step6 is not None
    assert step6.status == "BLOCKED"
    assert not step6.code_ready


def test_step_7_is_source_confirmed():
    """Step 7 MUST be marked as SOURCE_CONFIRMED (comparison only)."""
    step7 = get_step(7)

    assert step7 is not None
    assert "SOURCE_CONFIRMED" in step7.status
    assert step7.code_ready


# ============================================================================
# Test Bridge Finding
# ============================================================================


def test_bridge_formula_missing():
    """Bridge F_oP → H_MULT MUST be marked as formula missing."""
    bridge = get_bridge_finding()

    assert bridge.answer == "NO, formula missing"
    assert "PARTIAL" in bridge.status
    assert "procedural/heuristic bridge only" in bridge.status.lower()


def test_bridge_has_evidence():
    """Bridge finding MUST cite evidence."""
    bridge = get_bridge_finding()

    assert len(bridge.evidence) >= 3
    assert any("Force formulas provided" in e for e in bridge.evidence)
    assert any("NO formula H_MULT" in e for e in bridge.evidence)


# ============================================================================
# Test Table A1
# ============================================================================


def test_table_a1_has_12_rows():
    """Table A1 MUST have 12 rows (z = 0 to 8.5)."""
    assert len(TABLE_A1) == 12


def test_table_a1_beta_values():
    """β_d = 4.5, β_q = 18.0 from Table A1."""
    assert get_beta_d_table_a1() == 4.5
    assert get_beta_q_table_a1() == 18.0


def test_table_a1_row_structure():
    """Every row MUST have all required fields."""
    for row in TABLE_A1:
        assert row.time is not None
        assert row.z is not None
        assert row.h_data is not None
        assert row.sigma_h_data is not None
        assert row.h_flrw is not None
        # h_mult may be None for z=0 (as in source)


# ============================================================================
# Test Allowed vs Blocked Operations
# ============================================================================


def test_h_mult_computation_is_blocked():
    """H_MULT(z) computation MUST be blocked."""
    assert is_operation_blocked("H_MULT(z) computation — formula missing")
    assert not is_operation_allowed("H_MULT(z) computation")


def test_mcmc_is_blocked():
    """MCMC parameter estimation MUST be blocked."""
    assert is_operation_blocked(
        "MCMC parameter estimation — requires H_MULT(z) likelihood function"
    )


def test_table_reproduction_is_allowed():
    """Table A1 reproduction MUST be allowed."""
    assert is_operation_allowed("Table A1 data as empirical table for comparison")


def test_force_formulas_are_allowed():
    """Force formulas MUST be allowed."""
    assert is_operation_allowed("Force formulas: F_m, F_d, F_q, F_oP")


def test_beta_fitting_is_blocked():
    """β_d, β_q fitting MUST be blocked (method under-specified)."""
    assert is_operation_blocked("β_d, β_q fitting — objective function and method under-specified")


# ============================================================================
# Test Invariants
# ============================================================================


def test_no_function_named_compute_hz():
    """MUST NOT have function named compute_Hz or H_MULT."""
    import src.appendix_a1_procedure_registry as registry

    # Check module does NOT define these functions
    assert not hasattr(registry, "compute_Hz")
    assert not hasattr(registry, "compute_H_MULT")
    assert not hasattr(registry, "fit_beta_d_beta_q")


def test_h_mult_not_marked_predictive():
    """H-MULT MUST NOT be marked as predictive."""
    h_mult = get_variable("H-MULT")

    assert h_mult.code_permission != CodePermission.CODE_READY
    assert "NOT predictive" in h_mult.notes or "BLOCKED" in str(h_mult.code_permission)


def test_step_5_notes_mention_missing_formula():
    """Step 5 notes MUST mention missing formula."""
    step5 = get_step(5)

    assert "formula" in step5.notes.lower() or "formula" in step5.status.lower()
    assert "under" in step5.status.lower() and "specified" in step5.status.lower()


# ============================================================================
# Test Consistency
# ============================================================================


def test_all_blocked_operations_have_reason():
    """Every blocked operation MUST state reason."""
    for op in BLOCKED_OPERATIONS:
        assert "—" in op, f"Blocked operation missing reason: {op}"


def test_beta_values_match_table_a1():
    """β_d, β_q from get_variable MUST match Table A1 reported values."""
    beta_d = get_variable("β_d")
    beta_q = get_variable("β_q")

    assert "4.5" in beta_d.notes
    assert "18.0" in beta_q.notes


def test_all_variables_have_step_introduced():
    """Every variable MUST have step_introduced."""
    for var in VARIABLES:
        assert var.step_introduced in [3, 4, 5, 6, 7]


# ============================================================================
# Integration Test
# ============================================================================


def test_full_procedure_status_report():
    """Generate full status report — no exceptions."""
    report = []

    for step in STEPS:
        report.append(f"Step {step.step_number}: {step.status}")

    bridge = get_bridge_finding()
    report.append(f"Bridge: {bridge.status}")

    # Should complete without error
    assert len(report) == len(STEPS) + 1

    # Step 5 MUST be under-specified
    assert any("UNDER_SPECIFIED" in line for line in report)

    # Step 6 MUST be blocked
    assert any("BLOCKED" in line for line in report)
