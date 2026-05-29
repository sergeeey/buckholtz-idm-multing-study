"""Table A1 Reverse Engineering Diagnostics

Purpose: Infer characteristics of H_MULT(z) from Table A1 data WITHOUT claiming
         to have found Buckholtz's formula.

Safety Rules:
- Do NOT call any result SOURCE_CONFIRMED
- Do NOT allow MCMC
- Do NOT allow prediction on new z
- Mark all findings as: AI_INTERPRETATION_CANDIDATE / PHENOMENOLOGICAL_FIT_ONLY

Status Labels Used:
- REVERSE_ENGINEERING_DIAGNOSTIC — diagnostic test result
- TABLE_REPORTED_FIT_OUTPUT — H_MULT appears to be direct fitted output
- PHENOMENOLOGICAL_FIT_ONLY — polynomial/spline fit (not physics)
- AI_INTERPRETATION_CANDIDATE — inferred pattern (not source-confirmed)
- POST_HOC_DIAGNOSTIC_ONLY — w_eff diagnostic (not forward model)
- BLOCKED_MISSING_CLUSTER_VARIABLES — cannot test without m_A(z), r_A(z), etc.
- NOT_SOURCE_CONFIRMED — explicitly not from manuscript
- MCMC_BLOCKED — parameter estimation blocked
"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import numpy as np
import pandas as pd


# ============================================================================
# Status Enums
# ============================================================================


class DiagnosticStatus(Enum):
    """Status for reverse engineering diagnostic results"""

    REVERSE_ENGINEERING_DIAGNOSTIC = "reverse_engineering_diagnostic"
    TABLE_REPORTED_FIT_OUTPUT = "table_reported_fit_output"
    PHENOMENOLOGICAL_FIT_ONLY = "phenomenological_fit_only"
    AI_INTERPRETATION_CANDIDATE = "ai_interpretation_candidate"
    POST_HOC_DIAGNOSTIC_ONLY = "post_hoc_diagnostic_only"
    BLOCKED_MISSING_CLUSTER_VARIABLES = "blocked_missing_cluster_variables"
    NOT_SOURCE_CONFIRMED = "not_source_confirmed"
    MCMC_BLOCKED = "mcmc_blocked"


# ============================================================================
# Data Loading
# ============================================================================


def load_table_a1() -> pd.DataFrame:
    """Load Table A1 data from CSV

    Returns:
        DataFrame with 12 rows, columns: time_gyr, z, H_obs, sigma_H,
        H_FLRW, sigma_FLRW, H_MULT, sigma_MULT, w_eff, H_w_eff, sigma_w_eff, notes
    """
    csv_path = Path(__file__).parent.parent / "data" / "table_a1_reported.csv"
    df = pd.read_csv(csv_path, comment="#")

    # Convert NA strings to np.nan
    df = df.replace("NA", np.nan)

    # Convert numeric columns
    numeric_cols = [
        "time_gyr",
        "z",
        "H_obs",
        "sigma_H",
        "H_FLRW",
        "sigma_FLRW",
        "H_MULT",
        "sigma_MULT",
        "w_eff",
        "H_w_eff",
        "sigma_w_eff",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


# ============================================================================
# Test A — Closeness to Observed H
# ============================================================================


@dataclass
class ResidualStats:
    """Statistics for H_MULT vs H_obs residuals"""

    mean_absolute_residual: float
    rms_residual: float
    mean_absolute_sigma: float
    rms_sigma: float
    max_absolute_sigma: float
    status: DiagnosticStatus

    def summary(self) -> str:
        """Human-readable summary"""
        return (
            f"Mean |residual|: {self.mean_absolute_residual:.2f} km/s/Mpc\n"
            f"RMS residual: {self.rms_residual:.2f} km/s/Mpc\n"
            f"Mean |sigma|: {self.mean_absolute_sigma:.2f}\n"
            f"RMS sigma: {self.rms_sigma:.2f}\n"
            f"Max |sigma|: {self.max_absolute_sigma:.2f}\n"
            f"Status: {self.status.value}"
        )


def diagnostic_a_closeness_to_observed(df: pd.DataFrame) -> dict:
    """Test A — How close is H_MULT to H_obs?

    Compute residuals: H_MULT - H_obs, H_FLRW - H_obs, H_w_eff - H_obs
    Compare fit quality.

    Args:
        df: Table A1 DataFrame

    Returns:
        Dictionary with keys: 'mult', 'flrw', 'w_eff' → ResidualStats
    """
    results = {}

    # H_MULT residuals
    residual_mult = df["H_MULT"] - df["H_obs"]
    sigma_mult = df["sigma_MULT"]
    results["mult"] = ResidualStats(
        mean_absolute_residual=np.abs(residual_mult).mean(),
        rms_residual=np.sqrt((residual_mult**2).mean()),
        mean_absolute_sigma=np.abs(sigma_mult).mean(),
        rms_sigma=np.sqrt((sigma_mult**2).mean()),
        max_absolute_sigma=np.abs(sigma_mult).max(),
        status=DiagnosticStatus.TABLE_REPORTED_FIT_OUTPUT,
    )

    # H_FLRW residuals
    residual_flrw = df["H_FLRW"] - df["H_obs"]
    sigma_flrw = df["sigma_FLRW"]
    results["flrw"] = ResidualStats(
        mean_absolute_residual=np.abs(residual_flrw).mean(),
        rms_residual=np.sqrt((residual_flrw**2).mean()),
        mean_absolute_sigma=np.abs(sigma_flrw).mean(),
        rms_sigma=np.sqrt((sigma_flrw**2).mean()),
        max_absolute_sigma=np.abs(sigma_flrw).max(),
        status=DiagnosticStatus.REVERSE_ENGINEERING_DIAGNOSTIC,
    )

    # H_w_eff residuals (skip rows with NA)
    df_w_eff = df.dropna(subset=["H_w_eff", "sigma_w_eff"])
    if len(df_w_eff) > 0:
        residual_w_eff = df_w_eff["H_w_eff"] - df_w_eff["H_obs"]
        sigma_w_eff = df_w_eff["sigma_w_eff"]
        results["w_eff"] = ResidualStats(
            mean_absolute_residual=np.abs(residual_w_eff).mean(),
            rms_residual=np.sqrt((residual_w_eff**2).mean()),
            mean_absolute_sigma=np.abs(sigma_w_eff).mean(),
            rms_sigma=np.sqrt((sigma_w_eff**2).mean()),
            max_absolute_sigma=np.abs(sigma_w_eff).max(),
            status=DiagnosticStatus.POST_HOC_DIAGNOSTIC_ONLY,
        )

    return results


# ============================================================================
# Test B — Sigma Consistency
# ============================================================================


@dataclass
class SigmaConsistency:
    """Sigma consistency check result"""

    model_name: str
    reported_mean: float
    calculated_mean: float
    absolute_diff_mean: float
    max_absolute_diff: float
    passes: bool
    tolerance: float

    def summary(self) -> str:
        """Human-readable summary"""
        status = "✅ PASS" if self.passes else "❌ FAIL"
        return (
            f"{self.model_name}:\n"
            f"  Reported mean sigma: {self.reported_mean:.3f}\n"
            f"  Calculated mean sigma: {self.calculated_mean:.3f}\n"
            f"  Mean absolute diff: {self.absolute_diff_mean:.3f}\n"
            f"  Max absolute diff: {self.max_absolute_diff:.3f}\n"
            f"  Tolerance: {self.tolerance}\n"
            f"  Result: {status}"
        )


def diagnostic_b_sigma_consistency(df: pd.DataFrame, tolerance: float = 3.5) -> dict:
    """Test B — Is sigma_MULT internally consistent?

    Verify: sigma_calc = (H - H_obs) / sigma_H matches reported sigma

    Args:
        df: Table A1 DataFrame
        tolerance: Maximum allowed absolute difference

    Returns:
        Dictionary with keys: 'mult', 'flrw' → SigmaConsistency
    """
    results = {}

    # sigma_MULT
    sigma_mult_calc = (df["H_MULT"] - df["H_obs"]) / df["sigma_H"]
    sigma_mult_reported = df["sigma_MULT"]
    diff_mult = np.abs(sigma_mult_calc - sigma_mult_reported)
    results["mult"] = SigmaConsistency(
        model_name="H_MULT",
        reported_mean=sigma_mult_reported.mean(),
        calculated_mean=sigma_mult_calc.mean(),
        absolute_diff_mean=diff_mult.mean(),
        max_absolute_diff=diff_mult.max(),
        passes=(diff_mult.max() <= tolerance),
        tolerance=tolerance,
    )

    # sigma_FLRW
    sigma_flrw_calc = (df["H_FLRW"] - df["H_obs"]) / df["sigma_H"]
    sigma_flrw_reported = df["sigma_FLRW"]
    diff_flrw = np.abs(sigma_flrw_calc - sigma_flrw_reported)
    results["flrw"] = SigmaConsistency(
        model_name="H_FLRW",
        reported_mean=sigma_flrw_reported.mean(),
        calculated_mean=sigma_flrw_calc.mean(),
        absolute_diff_mean=diff_flrw.mean(),
        max_absolute_diff=diff_flrw.max(),
        passes=(diff_flrw.max() <= tolerance),
        tolerance=tolerance,
    )

    return results


# ============================================================================
# Test C — Relation to H_FLRW
# ============================================================================


@dataclass
class FLRWRelation:
    """Relationship between H_MULT and H_FLRW"""

    mean_ratio: float
    std_ratio: float
    mean_difference: float
    std_difference: float
    correlation_h: float
    correlation_residual: float
    status: DiagnosticStatus

    def summary(self) -> str:
        """Human-readable summary"""
        return (
            f"H_MULT / H_FLRW:\n"
            f"  Mean ratio: {self.mean_ratio:.4f}\n"
            f"  Std ratio: {self.std_ratio:.4f}\n"
            f"H_MULT - H_FLRW:\n"
            f"  Mean difference: {self.mean_difference:.2f} km/s/Mpc\n"
            f"  Std difference: {self.std_difference:.2f} km/s/Mpc\n"
            f"Correlation H_MULT vs H_FLRW: {self.correlation_h:.4f}\n"
            f"Correlation residuals: {self.correlation_residual:.4f}\n"
            f"Status: {self.status.value}"
        )


def diagnostic_c_relation_to_flrw(df: pd.DataFrame) -> FLRWRelation:
    """Test C — Is H_MULT a simple correction to H_FLRW?

    Check:
    - H_MULT / H_FLRW (multiplicative)
    - H_MULT - H_FLRW (additive)
    - Correlation

    Args:
        df: Table A1 DataFrame

    Returns:
        FLRWRelation object
    """
    ratio = df["H_MULT"] / df["H_FLRW"]
    difference = df["H_MULT"] - df["H_FLRW"]
    residual_mult = df["H_MULT"] - df["H_obs"]
    residual_flrw = df["H_FLRW"] - df["H_obs"]

    return FLRWRelation(
        mean_ratio=ratio.mean(),
        std_ratio=ratio.std(),
        mean_difference=difference.mean(),
        std_difference=difference.std(),
        correlation_h=df[["H_MULT", "H_FLRW"]].corr().iloc[0, 1],
        correlation_residual=np.corrcoef(residual_mult, residual_flrw)[0, 1],
        status=DiagnosticStatus.AI_INTERPRETATION_CANDIDATE,
    )


# ============================================================================
# Test D — Inferred Phi(z)
# ============================================================================


@dataclass
class PhiInference:
    """Inferred Phi(z) from H_MULT ratios"""

    z_anchor: float
    H_anchor: float
    phi_relative: pd.Series  # Phi(z) / Phi(anchor)
    status: DiagnosticStatus

    def summary(self) -> str:
        """Human-readable summary"""
        return (
            f"Anchor: z={self.z_anchor:.2f}, H_anchor={self.H_anchor:.2f} km/s/Mpc\n"
            f"Phi_relative range: [{self.phi_relative.min():.4f}, "
            f"{self.phi_relative.max():.4f}]\n"
            f"Status: {self.status.value} — NOT SOURCE_CONFIRMED"
        )


def diagnostic_d_inferred_phi_z(df: pd.DataFrame, anchor_row: int = 0) -> PhiInference:
    """Test D — Infer Phi(z) from H_MULT ratios

    If H_MULT²(z) = H_anchor² × Phi(z) / Phi(anchor), then:
    Phi_relative(z) = (H_MULT(z) / H_MULT(anchor))²

    Args:
        df: Table A1 DataFrame
        anchor_row: Row index for anchor point (default: 0 = z=0)

    Returns:
        PhiInference object

    WARNING: This is AI_INTERPRETATION_CANDIDATE, NOT source-confirmed
    """
    z_anchor = df.iloc[anchor_row]["z"]
    H_anchor = df.iloc[anchor_row]["H_MULT"]

    # Phi_relative(z) = (H_MULT(z) / H_anchor)²
    phi_relative = (df["H_MULT"] / H_anchor) ** 2

    return PhiInference(
        z_anchor=z_anchor,
        H_anchor=H_anchor,
        phi_relative=phi_relative,
        status=DiagnosticStatus.AI_INTERPRETATION_CANDIDATE,
    )


# ============================================================================
# Test E — Force Ratio Correlation (BLOCKED)
# ============================================================================


@dataclass
class ForceRatioTest:
    """Force ratio test result (blocked)"""

    status: DiagnosticStatus
    missing_variables: list[str]
    reason: str

    def summary(self) -> str:
        """Human-readable summary"""
        return (
            f"Status: {self.status.value}\n"
            f"Reason: {self.reason}\n"
            f"Missing: {', '.join(self.missing_variables)}"
        )


def diagnostic_e_force_ratio_correlation() -> ForceRatioTest:
    """Test E — Force ratio correlation (BLOCKED)

    Cannot proceed without cluster variables:
    - m_A(z): cluster A mass
    - r_A(z): cluster A radius
    - k_A(z): cluster A force constant
    - D_CAB(z): inter-cluster distance

    Returns:
        ForceRatioTest with BLOCKED status
    """
    return ForceRatioTest(
        status=DiagnosticStatus.BLOCKED_MISSING_CLUSTER_VARIABLES,
        missing_variables=["m_A(z)", "r_A(z)", "k_A(z)", "D_CAB(z)"],
        reason="Cluster variables not provided in Table A1",
    )


# ============================================================================
# Test F — w_eff Diagnostic
# ============================================================================


@dataclass
class WEffDiagnostic:
    """w_eff diagnostic result"""

    w_eff_better_than_mult: bool
    w_eff_better_than_flrw: bool
    mean_w_eff: float
    std_w_eff: float
    status: DiagnosticStatus

    def summary(self) -> str:
        """Human-readable summary"""
        return (
            f"w_eff better than H_MULT? {self.w_eff_better_than_mult}\n"
            f"w_eff better than H_FLRW? {self.w_eff_better_than_flrw}\n"
            f"Mean w_eff: {self.mean_w_eff:.3f}\n"
            f"Std w_eff: {self.std_w_eff:.3f}\n"
            f"Status: {self.status.value} — post-hoc, not forward model"
        )


def diagnostic_f_w_eff_diagnostic(df: pd.DataFrame) -> WEffDiagnostic:
    """Test F — w_eff diagnostic

    Check:
    - Is H_w_eff closer to H_obs than H_MULT?
    - Is w_eff chosen post-hoc to match observations?

    Args:
        df: Table A1 DataFrame

    Returns:
        WEffDiagnostic object

    WARNING: w_eff is POST_HOC_DIAGNOSTIC_ONLY, not a forward model
    """
    df_w = df.dropna(subset=["H_w_eff", "w_eff"])

    if len(df_w) == 0:
        return WEffDiagnostic(
            w_eff_better_than_mult=False,
            w_eff_better_than_flrw=False,
            mean_w_eff=np.nan,
            std_w_eff=np.nan,
            status=DiagnosticStatus.POST_HOC_DIAGNOSTIC_ONLY,
        )

    residual_w_eff = np.abs(df_w["H_w_eff"] - df_w["H_obs"]).mean()
    residual_mult = np.abs(df_w["H_MULT"] - df_w["H_obs"]).mean()
    residual_flrw = np.abs(df_w["H_FLRW"] - df_w["H_obs"]).mean()

    return WEffDiagnostic(
        w_eff_better_than_mult=(residual_w_eff < residual_mult),
        w_eff_better_than_flrw=(residual_w_eff < residual_flrw),
        mean_w_eff=df_w["w_eff"].mean(),
        std_w_eff=df_w["w_eff"].std(),
        status=DiagnosticStatus.POST_HOC_DIAGNOSTIC_ONLY,
    )


# ============================================================================
# Test G — Polynomial Correction to FLRW
# ============================================================================


@dataclass
class PolynomialFit:
    """Polynomial correction fit result"""

    degree: int
    coefficients: np.ndarray
    rms_residual: float
    overfitting_risk: str
    status: DiagnosticStatus

    def summary(self) -> str:
        """Human-readable summary"""
        coef_str = ", ".join([f"{c:.4f}" for c in self.coefficients])
        return (
            f"Degree: {self.degree}\n"
            f"Coefficients: [{coef_str}]\n"
            f"RMS residual: {self.rms_residual:.2f} km/s/Mpc\n"
            f"Overfitting risk: {self.overfitting_risk}\n"
            f"Status: {self.status.value} — phenomenological, not physics"
        )


def diagnostic_g_polynomial_correction(df: pd.DataFrame, degree: int = 3) -> PolynomialFit:
    """Test G — Polynomial correction to H_FLRW

    Fit: H_MULT = H_FLRW × (1 + c1×z + c2×z² + ... + cN×z^N)

    Args:
        df: Table A1 DataFrame
        degree: Polynomial degree (default 3)

    Returns:
        PolynomialFit object

    WARNING: This is PHENOMENOLOGICAL_FIT_ONLY, not physical model
    """
    z = df["z"].values
    correction_factor = df["H_MULT"] / df["H_FLRW"] - 1  # H_MULT/H_FLRW = 1 + p(z)

    # Fit polynomial
    coefficients = np.polyfit(z, correction_factor, degree)
    poly_pred = np.polyval(coefficients, z)
    residual = correction_factor - poly_pred
    rms = np.sqrt((residual**2).mean())

    # Overfitting risk assessment
    n_rows = len(df)
    dof = degree
    if dof > n_rows / 2:
        overfitting = "EXTREME"
    elif dof > n_rows / 3:
        overfitting = "HIGH"
    elif dof > n_rows / 6:
        overfitting = "MEDIUM"
    else:
        overfitting = "LOW"

    return PolynomialFit(
        degree=degree,
        coefficients=coefficients,
        rms_residual=rms,
        overfitting_risk=overfitting,
        status=DiagnosticStatus.PHENOMENOLOGICAL_FIT_ONLY,
    )


# ============================================================================
# Master Diagnostic Runner
# ============================================================================


def run_all_diagnostics() -> dict:
    """Run all Table A1 reverse engineering diagnostics

    Returns:
        Dictionary with keys: 'test_a', 'test_b', ..., 'test_g'
    """
    df = load_table_a1()

    results = {
        "test_a": diagnostic_a_closeness_to_observed(df),
        "test_b": diagnostic_b_sigma_consistency(df),
        "test_c": diagnostic_c_relation_to_flrw(df),
        "test_d": diagnostic_d_inferred_phi_z(df),
        "test_e": diagnostic_e_force_ratio_correlation(),
        "test_f": diagnostic_f_w_eff_diagnostic(df),
        "test_g_deg1": diagnostic_g_polynomial_correction(df, degree=1),
        "test_g_deg2": diagnostic_g_polynomial_correction(df, degree=2),
        "test_g_deg3": diagnostic_g_polynomial_correction(df, degree=3),
    }

    return results


def generate_summary_markdown(results: dict) -> str:
    """Generate markdown summary of all diagnostics

    Args:
        results: Output from run_all_diagnostics()

    Returns:
        Markdown string
    """
    lines = [
        "# Table A1 Reverse Engineering — Diagnostic Results",
        "",
        "**Date:** 2026-05-29",
        "**Source:** data/table_a1_reported.csv (12 rows, z=0 to 8.5)",
        "**Status:** AI_INTERPRETATION_CANDIDATE / PHENOMENOLOGICAL_FIT_ONLY",
        "",
        "---",
        "",
        "## Test A — Closeness to Observed H",
        "",
    ]

    for model_name, stats in results["test_a"].items():
        lines.append(f"### {model_name.upper()}")
        lines.append("```")
        lines.append(stats.summary())
        lines.append("```")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Test B — Sigma Consistency",
            "",
        ]
    )

    for model_name, sigma in results["test_b"].items():
        lines.append(f"### {model_name.upper()}")
        lines.append("```")
        lines.append(sigma.summary())
        lines.append("```")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Test C — Relation to H_FLRW",
            "",
            "```",
            results["test_c"].summary(),
            "```",
            "",
            "---",
            "",
            "## Test D — Inferred Phi(z)",
            "",
            "```",
            results["test_d"].summary(),
            "```",
            "",
            "---",
            "",
            "## Test E — Force Ratio Correlation",
            "",
            "```",
            results["test_e"].summary(),
            "```",
            "",
            "---",
            "",
            "## Test F — w_eff Diagnostic",
            "",
            "```",
            results["test_f"].summary(),
            "```",
            "",
            "---",
            "",
            "## Test G — Polynomial Correction to H_FLRW",
            "",
        ]
    )

    for key in ["test_g_deg1", "test_g_deg2", "test_g_deg3"]:
        poly = results[key]
        lines.append(f"### Degree {poly.degree}")
        lines.append("```")
        lines.append(poly.summary())
        lines.append("```")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Safety Markers",
            "",
            "- ✅ All results marked NOT_SOURCE_CONFIRMED",
            "- ✅ MCMC remains BLOCKED",
            "- ✅ No prediction on new z allowed",
            "- ✅ Polynomial fits marked PHENOMENOLOGICAL_FIT_ONLY",
            "- ✅ Phi(z) inference marked AI_INTERPRETATION_CANDIDATE",
            "- ✅ Force ratio test BLOCKED (missing cluster variables)",
            "",
            "---",
            "",
            "**End of Diagnostics**",
        ]
    )

    return "\n".join(lines)


# ============================================================================
# CLI Entry Point
# ============================================================================

if __name__ == "__main__":
    print("Running Table A1 Reverse Engineering Diagnostics...")
    print("=" * 70)
    results = run_all_diagnostics()
    summary = generate_summary_markdown(results)
    print(summary)
