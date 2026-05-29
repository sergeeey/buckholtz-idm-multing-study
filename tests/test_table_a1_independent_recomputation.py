"""Tests for Table A1 Independent Recomputation

Safety: All tests verify arithmetic only, no validation/refutation claims.
"""

import numpy as np
import pandas as pd
import pytest

from src.table_a1_independent_recomputation import (
    AssumptionsRegistry,
    ConfidenceLevel,
    EvidenceLevel,
    RecomputationResult,
    compute_h_flrw,
    compute_residuals,
    diagnose_row_1,
    generate_markdown_report,
    recompute_table_a1,
)

# ============================================================================
# FLRW Computation Tests
# ============================================================================


def test_h_flrw_at_z_zero():
    """H_FLRW(z=0) should equal H0"""
    H0 = 67.4
    result = compute_h_flrw(z=0.0, H0=H0)
    assert np.isclose(result, H0, atol=0.01)


def test_h_flrw_increases_with_z():
    """H_FLRW should increase with redshift"""
    z_values = np.array([0.0, 0.5, 1.0, 2.0])
    H_values = compute_h_flrw(z_values, H0=67.4)

    # Check monotonically increasing
    assert all(H_values[i] < H_values[i + 1] for i in range(len(H_values) - 1))


def test_h_flrw_array_input():
    """H_FLRW should handle array input"""
    z_array = np.array([0.0, 0.1, 0.5, 1.0])
    result = compute_h_flrw(z_array)

    assert isinstance(result, np.ndarray)
    assert len(result) == len(z_array)
    assert all(np.isfinite(result))


def test_h_flrw_matches_table_a1_z0():
    """H_FLRW(z=0) with H0=67.4 should match Table A1 reported value"""
    # Table A1 Row 1: z=0, H_FLRW=67.4
    H0 = 67.4
    result = compute_h_flrw(z=0.0, H0=H0)
    assert np.isclose(result, 67.4, atol=0.1)


# ============================================================================
# Residual Computation Tests
# ============================================================================


def test_residuals_absolute_convention():
    """Test absolute residual: H_obs - H_model"""
    H_obs = np.array([73.0, 69.0, 74.0])
    H_model = np.array([67.4, 68.1, 69.3])
    sigma = np.array([1.1, 3.0, 4.0])

    result = compute_residuals(H_obs, H_model, sigma, convention="absolute")

    expected = H_obs - H_model
    np.testing.assert_allclose(result, expected, atol=0.01)


def test_residuals_normalized_convention():
    """Test normalized residual: (H_obs - H_model) / sigma"""
    H_obs = np.array([73.0, 69.0, 74.0])
    H_model = np.array([67.4, 68.1, 69.3])
    sigma = np.array([1.1, 3.0, 4.0])

    result = compute_residuals(H_obs, H_model, sigma, convention="normalized")

    expected = (H_obs - H_model) / sigma
    np.testing.assert_allclose(result, expected, atol=0.01)


def test_residuals_invalid_convention():
    """Invalid convention should raise ValueError"""
    H_obs = np.array([73.0])
    H_model = np.array([67.4])
    sigma = np.array([1.1])

    with pytest.raises(ValueError, match="Unknown convention"):
        compute_residuals(H_obs, H_model, sigma, convention="invalid")


# ============================================================================
# Assumptions Registry Tests
# ============================================================================


def test_assumptions_registry_add():
    """Test adding assumptions to registry"""
    registry = AssumptionsRegistry()

    registry.add(
        statement="H0 = 67.4 km/s/Mpc",
        evidence=EvidenceLevel.ASSUMED_STANDARD,
        source="Planck 2018",
        confidence=ConfidenceLevel.HIGH,
        alternative="Could use H0=70",
    )

    assert len(registry.assumptions) == 1
    assert registry.assumptions[0].statement == "H0 = 67.4 km/s/Mpc"
    assert registry.assumptions[0].evidence == EvidenceLevel.ASSUMED_STANDARD


def test_assumptions_to_markdown():
    """Test markdown generation from assumptions"""
    registry = AssumptionsRegistry()

    registry.add(
        statement="Test assumption",
        evidence=EvidenceLevel.EXPLICIT_IN_PAPER,
        source="Test source",
        confidence=ConfidenceLevel.MEDIUM,
        alternative="Alternative",
    )

    markdown = registry.to_markdown()

    assert "# Assumptions Used" in markdown
    assert "ASSUMPTION 1" in markdown
    assert "Test assumption" in markdown
    assert "explicit_in_paper" in markdown


# ============================================================================
# Row 1 Diagnostic Tests
# ============================================================================


def test_diagnose_row_1_standard_convention():
    """Test Row 1 diagnostic with standard convention"""
    # Create mock Row 1 from Table A1
    row_1 = pd.Series(
        {
            "z": 0.0,
            "H_obs": 73.0,
            "sigma_H": 1.1,
            "H_FLRW": 67.4,
            "sigma_FLRW": -5.6,  # Reported value
            "H_MULT": 71.1,
            "sigma_MULT": 1.30,
        }
    )

    # Recomputed values
    H_FLRW_recomputed = 67.4
    H_MULT_recomputed = 71.1

    result = diagnose_row_1(row_1, H_FLRW_recomputed, H_MULT_recomputed)

    assert isinstance(result.best_hypothesis, str)
    assert result.details["reported_sigma_FLRW"] == -5.6


def test_diagnose_row_1_returns_valid_hypothesis():
    """Diagnostic should return one of the 3 hypotheses"""
    row_1 = pd.Series(
        {
            "z": 0.0,
            "H_obs": 73.0,
            "sigma_H": 1.1,
            "H_FLRW": 67.4,
            "sigma_FLRW": -5.6,
            "H_MULT": 71.1,
            "sigma_MULT": 1.30,
        }
    )

    result = diagnose_row_1(row_1, 67.4, 71.1)

    valid_hypotheses = [
        "Hypothesis A (standard)",
        "Hypothesis B (anchor)",
        "Hypothesis C (alternate sigma)",
    ]
    assert result.best_hypothesis in valid_hypotheses


# ============================================================================
# Full Recomputation Tests
# ============================================================================


def test_recompute_table_a1_runs():
    """Test that full recomputation runs without errors"""
    result = recompute_table_a1()

    assert isinstance(result, RecomputationResult)
    assert isinstance(result.comparison_df, pd.DataFrame)
    assert len(result.comparison_df) == 12  # 12 rows in Table A1
    assert isinstance(result.assumptions, AssumptionsRegistry)


def test_recomputation_has_required_columns():
    """Comparison DataFrame should have all required columns"""
    result = recompute_table_a1()
    df = result.comparison_df

    required_cols = [
        "z",
        "H_obs",
        "sigma_H",
        "H_FLRW_reported",
        "H_FLRW_recomputed",
        "H_FLRW_diff",
        "sigma_FLRW_reported",
        "sigma_FLRW_recomputed",
    ]

    for col in required_cols:
        assert col in df.columns, f"Missing column: {col}"


def test_recomputation_row_count_matches():
    """Should have 12 rows (same as Table A1)"""
    result = recompute_table_a1()
    assert len(result.comparison_df) == 12


def test_recomputation_z_values_match():
    """Recomputed z values should match reported"""
    result = recompute_table_a1()
    df = result.comparison_df

    # Check first and last z values
    assert np.isclose(df["z"].iloc[0], 0.0, atol=0.01)
    assert np.isclose(df["z"].iloc[-1], 8.5, atol=0.01)


def test_recomputation_summary_keys():
    """Summary should contain expected statistics"""
    result = recompute_table_a1()
    summary = result.summary

    required_keys = [
        "total_rows",
        "h_flrw_exact_matches",
        "h_flrw_close_matches",
        "sigma_flrw_exact_matches",
        "max_h_flrw_discrepancy",
        "max_sigma_flrw_discrepancy",
    ]

    for key in required_keys:
        assert key in summary, f"Missing summary key: {key}"


def test_recomputation_has_assumptions():
    """Recomputation should register assumptions"""
    result = recompute_table_a1()

    assert len(result.assumptions.assumptions) > 0
    # Should have at least: FLRW cosmology, sigma convention, Row 1 treatment, β values
    assert len(result.assumptions.assumptions) >= 4


# ============================================================================
# Report Generation Tests
# ============================================================================


def test_generate_markdown_report_runs():
    """Test that markdown report generation runs"""
    result = recompute_table_a1()
    report = generate_markdown_report(result)

    assert isinstance(report, str)
    assert len(report) > 0


def test_markdown_report_has_safety_labels():
    """Report should contain safety labels"""
    result = recompute_table_a1()
    report = generate_markdown_report(result)

    assert "INTERNAL_CONTRIBUTION_DRAFT" in report
    assert "NOT_VALIDATION" in report
    assert "NOT_REFUTATION" in report
    assert "AUTHOR_CONFIRMATION_REQUIRED" in report


def test_markdown_report_has_row_1_diagnostic():
    """Report should include Row 1 diagnostic section"""
    result = recompute_table_a1()
    report = generate_markdown_report(result)

    assert "Row 1 (z=0) Diagnostic" in report
    assert "Best matching hypothesis" in report


def test_markdown_report_has_assumptions():
    """Report should include assumptions section"""
    result = recompute_table_a1()
    report = generate_markdown_report(result)

    assert "Assumptions Used" in report
    assert "ASSUMPTION" in report


def test_markdown_report_no_interpretation():
    """Report should explicitly state no interpretation"""
    result = recompute_table_a1()
    report = generate_markdown_report(result)

    assert "NONE" in report or "pure arithmetic" in report.lower()
    assert "No validation" in report or "NOT_VALIDATION" in report


# ============================================================================
# Safety Tests
# ============================================================================


def test_no_validation_claim_in_code():
    """Code should not contain validation claims"""
    # Read the source file
    source_file = "src/table_a1_independent_recomputation.py"  # Relative to repo root
    import pathlib

    source_path = pathlib.Path(__file__).parent.parent / source_file
    source_text = source_path.read_text()

    # Should NOT contain these phrases in POSITIVE context
    # (negative context like "NOT a claim of author error" is safe)
    forbidden_positive_phrases = [
        "validates MULTING",
        "proves MULTING",
        "confirms theory",
        "author made error",
        "Buckholtz made error",
        "this validates",
        "this refutes",
    ]

    for phrase in forbidden_positive_phrases:
        assert phrase.lower() not in source_text.lower(), f"Found forbidden phrase: {phrase}"


def test_safety_labels_in_docstring():
    """Module docstring should contain safety labels"""
    import src.table_a1_independent_recomputation as module

    docstring = module.__doc__

    assert "NOT_VALIDATION" in docstring
    assert "NOT_REFUTATION" in docstring
    assert "INTERNAL_CONTRIBUTION_DRAFT" in docstring


# ============================================================================
# Edge Cases
# ============================================================================


def test_h_flrw_at_high_redshift():
    """H_FLRW should remain finite at high redshift"""
    z_high = 100.0
    result = compute_h_flrw(z_high, H0=67.4)

    assert np.isfinite(result)
    assert result > 0


def test_residuals_with_zero_sigma():
    """Residuals should handle zero sigma gracefully"""
    H_obs = np.array([73.0])
    H_model = np.array([67.4])
    sigma = np.array([0.0])

    with pytest.warns(RuntimeWarning):  # Division by zero warning expected
        result = compute_residuals(H_obs, H_model, sigma, convention="normalized")
        assert np.isinf(result[0])  # Should be inf, not crash
