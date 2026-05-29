"""Diagnose H_FLRW Parameter Candidates

Purpose: Test multiple cosmological baselines against Table A1 H_FLRW to identify best match.

Safety Labels:
- INTERNAL_DIAGNOSTIC_ONLY
- NOT_SOURCE_CONFIRMED
- NOT_VALIDATION
- NOT_REFUTATION
- H_FLRW_PROVENANCE_RECOVERY

Usage:
    python scripts/diagnose_hflrw_parameter_candidates.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize

# ============================================================================
# Load Table A1 Data
# ============================================================================


def load_table_a1_hflrw() -> tuple[np.ndarray, np.ndarray]:
    """Load z and H_FLRW from Table A1

    Returns:
        (z_values, H_FLRW_reported)
    """
    csv_path = Path(__file__).parent.parent / "data" / "table_a1_reported.csv"
    df = pd.read_csv(csv_path, comment="#")
    df = df.replace("NA", np.nan)

    z_values = df["z"].values
    H_FLRW_reported = df["H_FLRW"].values

    return z_values, H_FLRW_reported


# ============================================================================
# Cosmology Models
# ============================================================================


def h_flrw_flat_lcdm(
    z: np.ndarray, H0: float, Omega_m: float, Omega_Lambda: float | None = None
) -> np.ndarray:
    """Standard flat ΛCDM

    Args:
        z: Redshift
        H0: Hubble constant [km/s/Mpc]
        Omega_m: Matter density
        Omega_Lambda: Dark energy density (if None, use 1 - Omega_m for flat)

    Returns:
        H(z) in km/s/Mpc
    """
    if Omega_Lambda is None:
        Omega_Lambda = 1.0 - Omega_m

    a = 1.0 / (1.0 + z)
    E_squared = Omega_m * a**-3 + Omega_Lambda
    return H0 * np.sqrt(E_squared)


def h_einstein_de_sitter(z: np.ndarray, H0: float) -> np.ndarray:
    """Einstein-de Sitter (matter-only, Ωm=1)

    Args:
        z: Redshift
        H0: Hubble constant

    Returns:
        H(z) = H0 * (1+z)^1.5
    """
    return H0 * (1.0 + z) ** 1.5


def h_linear(z: np.ndarray, H0: float) -> np.ndarray:
    """Linear Hubble (diagnostic only, not physical)

    Args:
        z: Redshift
        H0: Hubble constant

    Returns:
        H(z) = H0 * (1+z)
    """
    return H0 * (1.0 + z)


def h_power_law(z: np.ndarray, A: float, p: float) -> np.ndarray:
    """Power law H(z) = A(1+z)^p

    Args:
        z: Redshift
        A: Normalization [km/s/Mpc]
        p: Power index

    Returns:
        H(z) in km/s/Mpc
    """
    return A * (1.0 + z) ** p


def h_radiation_included(
    z: np.ndarray,
    H0: float,
    Omega_r: float = 9e-5,
    Omega_m: float = 0.315,
    Omega_Lambda: float = 0.685,
) -> np.ndarray:
    """Flat ΛCDM with radiation included

    Args:
        z: Redshift
        H0: Hubble constant
        Omega_r: Radiation density (default: 9e-5 for CMB)
        Omega_m: Matter density
        Omega_Lambda: Dark energy density

    Returns:
        H(z) in km/s/Mpc
    """
    a = 1.0 / (1.0 + z)
    E_squared = Omega_r * a**-4 + Omega_m * a**-3 + Omega_Lambda
    return H0 * np.sqrt(E_squared)


# ============================================================================
# Evaluation Metrics
# ============================================================================


def evaluate_model(z: np.ndarray, H_model: np.ndarray, H_obs: np.ndarray) -> dict:
    """Evaluate model fit quality

    Args:
        z: Redshift values
        H_model: Model predictions
        H_obs: Observed values

    Returns:
        Dict with MAE, RMSE, max_error, etc.
    """
    errors = H_model - H_obs
    abs_errors = np.abs(errors)

    mae = np.mean(abs_errors)
    rmse = np.sqrt(np.mean(errors**2))
    max_error = np.max(abs_errors)
    max_error_z = z[np.argmax(abs_errors)]

    # Count matches within thresholds
    matches_01 = np.sum(abs_errors < 0.1)
    matches_10 = np.sum(abs_errors < 1.0)

    # Best and worst rows
    best_idx = np.argmin(abs_errors)
    worst_idx = np.argmax(abs_errors)

    return {
        "mae": mae,
        "rmse": rmse,
        "max_error": max_error,
        "max_error_z": max_error_z,
        "matches_within_0.1": matches_01,
        "matches_within_1.0": matches_10,
        "best_row_z": z[best_idx],
        "best_row_error": abs_errors[best_idx],
        "worst_row_z": z[worst_idx],
        "worst_row_error": abs_errors[worst_idx],
    }


# ============================================================================
# Candidate Sweep
# ============================================================================


def sweep_candidates() -> pd.DataFrame:
    """Test all candidate baselines against Table A1 H_FLRW

    Returns:
        DataFrame with results for each candidate
    """
    z, H_FLRW = load_table_a1_hflrw()

    candidates = [
        {
            "name": "Planck-like (H0=67.4, Ωm=0.315)",
            "model": lambda z_: h_flrw_flat_lcdm(z_, 67.4, 0.315),
            "params": "H0=67.4, Ωm=0.315, ΩΛ=0.685",
        },
        {
            "name": "SH0ES/Riess (H0=73.0, Ωm=0.3)",
            "model": lambda z_: h_flrw_flat_lcdm(z_, 73.0, 0.3),
            "params": "H0=73.0, Ωm=0.3, ΩΛ=0.7",
        },
        {
            "name": "WMAP-like (H0=70.0, Ωm=0.27)",
            "model": lambda z_: h_flrw_flat_lcdm(z_, 70.0, 0.27),
            "params": "H0=70.0, Ωm=0.27, ΩΛ=0.73",
        },
        {
            "name": "Einstein-de Sitter (Ωm=1)",
            "model": lambda z_: h_einstein_de_sitter(z_, 67.4),
            "params": "H0=67.4, Ωm=1.0, ΩΛ=0.0",
        },
        {
            "name": "Linear Hubble (diagnostic)",
            "model": lambda z_: h_linear(z_, 67.4),
            "params": "H0=67.4, power=1.0",
        },
        {
            "name": "Radiation-included",
            "model": lambda z_: h_radiation_included(z_, 67.4),
            "params": "H0=67.4, Ωr=9e-5, Ωm=0.315, ΩΛ=0.685",
        },
    ]

    results = []

    for candidate in candidates:
        H_model = candidate["model"](z)
        metrics = evaluate_model(z, H_model, H_FLRW)

        results.append(
            {
                "candidate": candidate["name"],
                "parameters": candidate["params"],
                "MAE": metrics["mae"],
                "RMSE": metrics["rmse"],
                "max_error": metrics["max_error"],
                "max_error_at_z": metrics["max_error_z"],
                "matches_0.1": metrics["matches_within_0.1"],
                "matches_1.0": metrics["matches_within_1.0"],
                "best_z": metrics["best_row_z"],
                "best_error": metrics["best_row_error"],
                "worst_z": metrics["worst_row_z"],
                "worst_error": metrics["worst_row_error"],
            }
        )

    return pd.DataFrame(results)


# ============================================================================
# Reverse Fitting
# ============================================================================


def fit_flat_lcdm_free_omega_m() -> dict:
    """Fit flat ΛCDM with H0 fixed, Ωm free

    Returns:
        Dict with best-fit Ωm and fit quality
    """
    z, H_FLRW = load_table_a1_hflrw()
    H0_fixed = 67.4  # From z=0 row

    def objective(params):
        Omega_m = params[0]
        H_model = h_flrw_flat_lcdm(z, H0_fixed, Omega_m)
        return np.mean((H_model - H_FLRW) ** 2)  # MSE

    # Initial guess: Planck value
    result = minimize(objective, x0=[0.315], bounds=[(0.0, 1.0)], method="L-BFGS-B")

    best_omega_m = result.x[0]
    H_model = h_flrw_flat_lcdm(z, H0_fixed, best_omega_m)
    metrics = evaluate_model(z, H_model, H_FLRW)

    return {
        "H0": H0_fixed,
        "Omega_m": best_omega_m,
        "Omega_Lambda": 1.0 - best_omega_m,
        "MAE": metrics["mae"],
        "RMSE": metrics["rmse"],
        "max_error": metrics["max_error"],
        "physically_plausible": 0.1 < best_omega_m < 0.5,
    }


def fit_power_law() -> dict:
    """Fit power law H(z) = A(1+z)^p

    Returns:
        Dict with best-fit A, p and fit quality
    """
    z, H_FLRW = load_table_a1_hflrw()

    def objective(params):
        A, p = params
        H_model = h_power_law(z, A, p)
        return np.mean((H_model - H_FLRW) ** 2)

    # Initial guess: A~67, p~1.5 (matter-dominated)
    result = minimize(objective, x0=[67.0, 1.5], bounds=[(50, 100), (0.5, 3.0)], method="L-BFGS-B")

    A_best, p_best = result.x
    H_model = h_power_law(z, A_best, p_best)
    metrics = evaluate_model(z, H_model, H_FLRW)

    # Physical interpretation
    if 1.4 < p_best < 1.6:
        interpretation = "Matter-dominated (p ≈ 1.5)"
    elif 0.9 < p_best < 1.1:
        interpretation = "Linear (non-physical, p ≈ 1.0)"
    elif 1.9 < p_best < 2.1:
        interpretation = "Radiation-dominated (p ≈ 2.0)"
    else:
        interpretation = f"Unknown regime (p = {p_best:.2f})"

    return {
        "A": A_best,
        "p": p_best,
        "interpretation": interpretation,
        "MAE": metrics["mae"],
        "RMSE": metrics["rmse"],
        "max_error": metrics["max_error"],
    }


# ============================================================================
# Main Execution
# ============================================================================


def main() -> None:
    """Run full diagnostic suite"""
    print("=" * 70)
    print("H_FLRW Parameter Candidate Sweep")
    print("=" * 70)
    print()

    # Candidate sweep
    print("## Testing Candidate Baselines\n")
    df_candidates = sweep_candidates()

    # Sort by MAE (best first)
    df_candidates = df_candidates.sort_values("MAE")

    print(df_candidates.to_string(index=False))
    print()

    # Find best candidate
    best = df_candidates.iloc[0]
    print(f"\n🏆 Best Candidate: {best['candidate']}")
    print(f"   Parameters: {best['parameters']}")
    print(f"   MAE: {best['MAE']:.2f} km/s/Mpc")
    print(f"   RMSE: {best['RMSE']:.2f} km/s/Mpc")
    print(f"   Matches within 0.1 km/s/Mpc: {best['matches_0.1']:.0f}/12")
    print(f"   Matches within 1.0 km/s/Mpc: {best['matches_1.0']:.0f}/12")
    print()

    # Reverse fits
    print("## Reverse-Fit Diagnostics\n")

    print("### Model 1: Flat ΛCDM with Free Ωm (H0=67.4 fixed)")
    fit1 = fit_flat_lcdm_free_omega_m()
    print(f"   Best-fit Ωm: {fit1['Omega_m']:.4f}")
    print(f"   Implied ΩΛ: {fit1['Omega_Lambda']:.4f}")
    print(f"   MAE: {fit1['MAE']:.2f} km/s/Mpc")
    print(f"   RMSE: {fit1['RMSE']:.2f} km/s/Mpc")
    print(f"   Max error: {fit1['max_error']:.2f} km/s/Mpc")
    print(f"   Physically plausible: {'✅ YES' if fit1['physically_plausible'] else '❌ NO'}")
    print()

    print("### Model 2: Power Law H(z) = A(1+z)^p")
    fit2 = fit_power_law()
    print(f"   Best-fit A: {fit2['A']:.2f} km/s/Mpc")
    print(f"   Best-fit p: {fit2['p']:.4f}")
    print(f"   Interpretation: {fit2['interpretation']}")
    print(f"   MAE: {fit2['MAE']:.2f} km/s/Mpc")
    print(f"   RMSE: {fit2['RMSE']:.2f} km/s/Mpc")
    print(f"   Max error: {fit2['max_error']:.2f} km/s/Mpc")
    print()

    # Save results
    output_dir = Path(__file__).parent.parent / "docs"
    csv_path = output_dir / "68_hflrw_candidate_sweep.csv"
    df_candidates.to_csv(csv_path, index=False, float_format="%.3f")
    print(f"✅ Candidate sweep saved: {csv_path}")

    print()
    print("=" * 70)
    print("✅ Diagnostic complete!")
    print()
    print("Key findings:")
    print(f"- Best standard candidate: {best['candidate']}")
    print(f"- Best MAE achieved: {best['MAE']:.2f} km/s/Mpc")
    print(f"- Free Ωm fit gives: Ωm={fit1['Omega_m']:.3f}, MAE={fit1['MAE']:.2f} km/s/Mpc")
    print(f"- Power law fit gives: p={fit2['p']:.3f}, MAE={fit2['MAE']:.2f} km/s/Mpc")
    print()
    print("Next step: Update docs/68_hflrw_provenance_recovery.md with these results")


if __name__ == "__main__":
    main()
