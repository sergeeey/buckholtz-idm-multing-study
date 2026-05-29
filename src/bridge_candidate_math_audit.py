"""Bridge Candidate Mathematical Audit Registry

Purpose: Track dimensional/sign/input analysis for F_oP → H_MULT bridge candidates

Safety: All candidates remain NOT_SOURCE_CONFIRMED, MCMC_BLOCKED, PREDICTION_BLOCKED
"""

from dataclasses import dataclass
from enum import Enum


class BridgeStatus(Enum):
    """Status for bridge candidates"""

    BEST_INTERNAL_CANDIDATE = "best_internal_candidate"
    CONDITIONAL = "conditional"
    BACKUP = "backup"
    TABLE_REPRODUCTION_HEURISTIC_ONLY = "table_reproduction_heuristic_only"
    NEEDS_VERIFICATION = "needs_verification"
    NOT_SOURCE_CONFIRMED = "not_source_confirmed"
    MCMC_BLOCKED = "mcmc_blocked"
    PREDICTION_BLOCKED = "prediction_blocked"


@dataclass
class DimensionalCheck:
    """Dimensional analysis result"""

    candidate_id: str
    formula: str
    lhs_units: str
    rhs_units: str
    passes: bool
    notes: str


@dataclass
class RequiredInput:
    """Missing input required for MCMC"""

    symbol: str
    units: str
    source: str
    status: str  # AVAILABLE, MISSING, UNKNOWN


@dataclass
class BridgeCandidate:
    """Bridge candidate audit record"""

    candidate_id: str
    name: str
    formula_latex: str
    dimensional_check: DimensionalCheck
    sign_convention_verified: bool
    required_inputs: list[RequiredInput]
    mcmc_allowed: bool
    prediction_allowed: bool
    status: list[BridgeStatus]
    risks: list[str]
    verdict: str


# ============================================================================
# Candidate B: Discrete Lattice ODE
# ============================================================================

CANDIDATE_B = BridgeCandidate(
    candidate_id="discrete_lattice_ode",
    name="Discrete Lattice ODE (Nearest-Neighbor Averaging)",
    formula_latex=r"\ddot{a}/a = N_{eff} \times F_{oP}(D_{AB},z) / (\mu \times D_{AB})",
    dimensional_check=DimensionalCheck(
        candidate_id="discrete_lattice_ode",
        formula=r"ä/a = N_eff × [F_oP / (μ × D_AB)]",
        lhs_units="[T⁻²]",
        rhs_units="[dimensionless] × [M L T⁻²] / ([M] × [L]) = [T⁻²]",
        passes=True,
        notes="Dimensionally consistent. F/μ = acceleration, acceleration/D = 1/time².",
    ),
    sign_convention_verified=True,
    required_inputs=[
        RequiredInput("m_A(z)", "[M]", "Table A1 or manuscript", "MISSING"),
        RequiredInput("m_P(z)", "[M]", "Table A1 or manuscript", "MISSING"),
        RequiredInput("k_A(z)", "[M L T⁻²]", "Table A1 or manuscript", "MISSING"),
        RequiredInput("k_P(z)", "[M L T⁻²]", "Table A1 or manuscript", "MISSING"),
        RequiredInput("r_A(z)", "[L]", "Table A1 or manuscript", "MISSING"),
        RequiredInput("r_P(z)", "[L]", "Table A1 or manuscript", "MISSING"),
        RequiredInput("D_AB(z)", "[L]", "Derived or specified", "MISSING"),
        RequiredInput("β_d", "dimensionless", "Table A1 caption", "AVAILABLE (4.5)"),
        RequiredInput("β_q", "dimensionless", "Table A1 caption", "AVAILABLE (18.0)"),
        RequiredInput("N_eff", "dimensionless", "Averaging/geometry", "MISSING"),
        RequiredInput("H₀", "[T⁻¹]", "Initial condition", "AVAILABLE (73 km/s/Mpc)"),
    ],
    mcmc_allowed=False,
    prediction_allowed=False,
    status=[
        BridgeStatus.BEST_INTERNAL_CANDIDATE,
        BridgeStatus.NOT_SOURCE_CONFIRMED,
        BridgeStatus.MCMC_BLOCKED,
        BridgeStatus.PREDICTION_BLOCKED,
    ],
    risks=[
        "May become our model, not Buckholtz's",
        "Lattice anisotropy — real clusters not on cubic lattice",
        "Force cancellation under isotropic averaging",
        "Arbitrary N_eff can fit any H(z)",
        "Cluster-scale force ≠ background expansion",
        "Parameter degeneracy (many combinations → same H)",
    ],
    verdict="BEST internal candidate IF author confirms and provides cluster variables",
)

# ============================================================================
# Phi(z) Heuristic
# ============================================================================

CANDIDATE_PHI = BridgeCandidate(
    candidate_id="phi_z_heuristic",
    name="Phi(z) Phenomenological Scaling (AI Transcript)",
    formula_latex=r"H_{MULT}^2(z) = H_{anchor}^2 \times [\Phi(z) / \Phi_{anchor}]",
    dimensional_check=DimensionalCheck(
        candidate_id="phi_z_heuristic",
        formula=r"H² = H_anchor² × Φ (dimensionless ratio)",
        lhs_units="[T⁻²]",
        rhs_units="[T⁻²] × [dimensionless] = [T⁻²]",
        passes=False,  # Units work but physical scaling under-specified
        notes=(
            "Dimensionally under-specified. Force ratios → H² without explicit "
            "length scale D_AB. Useful for Table A1 reproduction only."
        ),
    ),
    sign_convention_verified=False,  # N/A — heuristic
    required_inputs=[
        RequiredInput("A_m(z)", "under-specified", "AI service", "UNKNOWN"),
        RequiredInput("A_d(z)", "under-specified", "AI service", "UNKNOWN"),
        RequiredInput("A_q(z)", "under-specified", "AI service", "UNKNOWN"),
        RequiredInput("H_anchor", "[T⁻¹]", "Table A1 z=0 or other", "AVAILABLE"),
    ],
    mcmc_allowed=False,
    prediction_allowed=False,
    status=[
        BridgeStatus.TABLE_REPRODUCTION_HEURISTIC_ONLY,
        BridgeStatus.NOT_SOURCE_CONFIRMED,
        BridgeStatus.MCMC_BLOCKED,
        BridgeStatus.PREDICTION_BLOCKED,
    ],
    risks=[
        "Not a physical bridge — dimensionally under-specified",
        "Cannot predict new z — no forward model",
        "AI service black box — not reproducible",
    ],
    verdict="Useful for Table A1 diagnostics ONLY. Not allowed for prediction.",
)

# ============================================================================
# Registry
# ============================================================================

BRIDGE_CANDIDATES = {
    "discrete_lattice_ode": CANDIDATE_B,
    "phi_z_heuristic": CANDIDATE_PHI,
}


def get_best_internal_candidate() -> BridgeCandidate:
    """Return best internal reconstruction candidate

    Returns:
        Candidate B (Discrete Lattice ODE)

    WARNING: NOT source-confirmed, MCMC blocked
    """
    return CANDIDATE_B


def is_mcmc_allowed() -> bool:
    """Check if ANY candidate allows MCMC

    Returns:
        False — all candidates remain MCMC_BLOCKED
    """
    return False


def is_prediction_allowed() -> bool:
    """Check if ANY candidate allows prediction on new z

    Returns:
        False — all candidates remain PREDICTION_BLOCKED
    """
    return False


def get_author_question_bridge_method() -> str:
    """Author clarification question Q15: bridge method

    Returns:
        Question text for docs/26
    """
    return (
        "I am exploring a possible computational interpretation where pairwise "
        "MULTING acceleration F_oP/(μ×D_AB) is averaged over nearest neighbors "
        "to produce ä/a, then integrated to H(z). Is this closer to the intended "
        "Table A1 calculation route, or does the AI service use a different "
        "averaging or phenomenological rule?"
    )


def get_row_1_status() -> dict:
    """Row 1 (z=0) status for bridge diagnostics

    Returns:
        Status dictionary
    """
    return {
        "classification": "SOURCE_TABLE_OUTLIER",
        "sigma_mult_diff": 3.027,
        "tolerance": 0.11,
        "exceed_factor": 27.5,
        "recommendation": "Exclude Row 1 from internal fit until author clarifies",
        "usable_rows": "Rows 2-12 (z=0.06 to 8.5)",
        "max_diff_rows_2_12": 0.039,
    }


def validate_registry() -> list[str]:
    """Validate bridge candidate registry safety rules

    Returns:
        List of issues (empty if all pass)
    """
    issues = []

    # Rule 1: No candidate is source-confirmed
    for c in BRIDGE_CANDIDATES.values():
        if BridgeStatus.NOT_SOURCE_CONFIRMED not in c.status:
            issues.append(f"{c.candidate_id}: missing NOT_SOURCE_CONFIRMED status")

    # Rule 2: No candidate allows MCMC
    for c in BRIDGE_CANDIDATES.values():
        if c.mcmc_allowed:
            issues.append(f"{c.candidate_id}: mcmc_allowed=True (should be False)")

    # Rule 3: No candidate allows prediction
    for c in BRIDGE_CANDIDATES.values():
        if c.prediction_allowed:
            issues.append(f"{c.candidate_id}: prediction_allowed=True (should be False)")

    # Rule 4: Candidate B must pass dimensional check
    if not CANDIDATE_B.dimensional_check.passes:
        issues.append("Candidate B dimensional check failed")

    # Rule 5: Phi heuristic must NOT be marked as physical bridge
    if BridgeStatus.BEST_INTERNAL_CANDIDATE in CANDIDATE_PHI.status:
        issues.append("Phi heuristic incorrectly marked as best candidate")

    return issues


# No compute_H_MULT_source_confirmed function — all blocked
