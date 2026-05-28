"""
Minimum Viable Bridge (MVB) Registry — Discrete Lattice + Virial Pressure Route

Purpose: Document the strongest candidate bridge route from F_oP to H(z) as a research hypothesis.

Status: RESEARCH_HYPOTHESIS — computational reconstruction candidate, NOT source-supported.

MCMC readiness: BLOCKED (not source-confirmed).

See: docs/37_discrete_lattice_mvb_hypothesis.md
"""

from dataclasses import dataclass


@dataclass
class RequiredInput:
    """Input information needed to implement MVB route."""

    input_id: str  # I1, I2, etc.
    input_name: str  # "Lattice geometry specification", etc.
    why_needed: str  # What this unblocks
    priority: str  # CRITICAL, HIGH, MEDIUM, LOW


@dataclass
class RiskItem:
    """Risk of implementing MVB without source confirmation."""

    risk_id: str  # R1, R2, etc.
    risk_description: str  # What could go wrong
    severity: str  # HIGH, MEDIUM, LOW
    mitigation: str  # How to reduce risk


@dataclass
class AuthorClarification:
    """Question for Dr. Buckholtz about MVB route."""

    question_id: str  # Q_MVB
    question_text: str  # Specific question for author
    why_needed: str  # What this unblocks
    priority: str  # CRITICAL, HIGH, MEDIUM, LOW


@dataclass
class MVBCandidate:
    """Minimum Viable Bridge candidate route."""

    name: str  # Route name
    route_description: str  # Physical description
    status: str  # RESEARCH_HYPOTHESIS, etc.
    source_supported: bool  # Found in manuscript/communications?
    mcmc_ready: bool  # Can this route support MCMC?
    prediction_allowed: bool  # Can this route predict on new data?
    required_inputs: list[RequiredInput]  # What inputs are needed
    risks: list[RiskItem]  # What could go wrong
    author_clarification: AuthorClarification  # What question must be answered
    safe_wording: str  # How to communicate safely
    unsafe_wording: str  # What NOT to say


# ============================================================================
# Required Inputs
# ============================================================================

I1_LATTICE_GEOMETRY = RequiredInput(
    input_id="I1",
    input_name="Lattice geometry specification",
    why_needed="Define Wigner-Seitz cell topology (FCC, BCC, Voronoi tessellation)",
    priority="CRITICAL",
)

I2_NEIGHBOR_COUNT = RequiredInput(
    input_id="I2",
    input_name="Nearest-neighbor count N_n(z)",
    why_needed="Virial sum requires knowing how many neighbors interact per particle",
    priority="CRITICAL",
)

I3_CELL_VOLUME = RequiredInput(
    input_id="I3",
    input_name="Cell volume V_cell(z)",
    why_needed="Pressure P = -⟨r · F⟩ / (3V) requires volume normalization",
    priority="CRITICAL",
)

I4_MASS_PROFILE = RequiredInput(
    input_id="I4",
    input_name="Cluster mass m_A(z) per cell",
    why_needed="Monopole force F_m depends on particle masses",
    priority="HIGH",
)

I5_DIPOLE_SCALE = RequiredInput(
    input_id="I5",
    input_name="Dipole scale k_A(z)",
    why_needed="Dipole force F_d = k_A g_A / r_A² requires coefficient k_A(z)",
    priority="HIGH",
)

I6_QUADRUPOLE_SCALE = RequiredInput(
    input_id="I6",
    input_name="Quadrupole scale k_B(z)",
    why_needed="Quadrupole force F_q = k_B g_B / r_B³ requires coefficient k_B(z)",
    priority="HIGH",
)

I7_NEIGHBOR_DISTANCE = RequiredInput(
    input_id="I7",
    input_name="Neighbor distance r_A(z)",
    why_needed="All forces depend on separation r_A between cells",
    priority="CRITICAL",
)

I8_ANISOTROPY_TENSOR = RequiredInput(
    input_id="I8",
    input_name="Anisotropy tensor ⟨r ⊗ F⟩",
    why_needed="Full stress tensor T^ij requires directional averaging",
    priority="MEDIUM",
)

I9_TIME_AVERAGING = RequiredInput(
    input_id="I9",
    input_name="Time-averaging prescription",
    why_needed="Friedmann equation assumes time-averaged quantities",
    priority="MEDIUM",
)

I10_BOUNDARY_CONDITIONS = RequiredInput(
    input_id="I10",
    input_name="Boundary conditions at lattice edge",
    why_needed="Finite simulation box requires boundary handling",
    priority="LOW",
)


# ============================================================================
# Risks
# ============================================================================

R1_NOT_BUCKHOLTZ_MODEL = RiskItem(
    risk_id="R1",
    risk_description=(
        "MVB may become 'our model' not Buckholtz's. If author intended different "
        "bridge route → wasted effort, misrepresentation risk."
    ),
    severity="HIGH",
    mitigation=(
        "Always label as RESEARCH_HYPOTHESIS. Require author confirmation before "
        "claiming 'this is MULTING'. Include Q_MVB in all communications."
    ),
)

R2_BACKREACTION_TOO_SMALL = RiskItem(
    risk_id="R2",
    risk_description=(
        "Virial pressure from pairwise forces may be negligible at cosmological scales. "
        "If P_virial << P_ΛCDM → MVB cannot explain H(z) deviations."
    ),
    severity="MEDIUM",
    mitigation=(
        "Estimate P_virial order-of-magnitude before full implementation. "
        "If |P_virial / P_ΛCDM| < 0.01 → reject route early."
    ),
)

R3_LATTICE_BREAKS_HOMOGENEITY = RiskItem(
    risk_id="R3",
    risk_description=(
        "Discrete lattice is fundamentally inhomogeneous. Friedmann equation assumes "
        "homogeneity. Spatial averaging may not recover FLRW background."
    ),
    severity="MEDIUM",
    mitigation=(
        "Use Buchert backreaction formalism. Accept that H(z) may be effective, "
        "not fundamental. Document deviation from strict FLRW."
    ),
)

R4_PARAMETER_DEGENERACY = RiskItem(
    risk_id="R4",
    risk_description=(
        "10 required inputs (lattice geometry, neighbor count, cell volume, m_A, k_A, k_B, "
        "r_A, etc.) → high-dimensional parameter space. Many parameter sets may fit same H(z)."
    ),
    severity="MEDIUM",
    mitigation=(
        "Prioritize author clarification. Use priors from N-body simulations. "
        "Plan sensitivity analysis for degenerate parameters."
    ),
)

R5_NO_AUTHOR_CONFIRMATION = RiskItem(
    risk_id="R5",
    risk_description=(
        "No source material confirms discrete lattice + virial pressure route. "
        "Cannot validate until author responds to Q_MVB."
    ),
    severity="CRITICAL",
    mitigation=(
        "Do NOT implement MCMC or prediction until author confirms. "
        "Mark all results as COMPUTATIONAL_RECONSTRUCTION, not MULTING validation."
    ),
)


# ============================================================================
# Author Clarification
# ============================================================================

Q_MVB_DISCRETE_LATTICE = AuthorClarification(
    question_id="Q_MVB",
    question_text=(
        "Does MULTING use a discrete lattice approximation (e.g., Wigner-Seitz cells, "
        "cluster-based topology) to map pairwise forces F_oP to cosmological pressure? "
        "Specifically: (1) Is the cosmic web modeled as nearest-neighbor interactions "
        "between discrete cells? (2) Is virial pressure P = -⟨r · F⟩ / (3V) the bridge "
        "to Friedmann acceleration ä/a = -(4πG/3)(ρ + 3P)? (3) If not, what is the "
        "correct spatial averaging prescription for F_oP → H(z)?"
    ),
    why_needed=(
        "Required to confirm MVB route is Buckholtz-intended, not audit reconstruction. "
        "Unblocks MCMC if confirmed, prevents misrepresentation if rejected."
    ),
    priority="CRITICAL",
)


# ============================================================================
# MVB Candidate Record
# ============================================================================

MVB_DISCRETE_LATTICE_VIRIAL = MVBCandidate(
    name="Discrete lattice + virial effective-fluid bridge",
    route_description=(
        "Pairwise force law F_oP = F_m - F_d + F_q → discrete cluster lattice "
        "(Wigner-Seitz cells) → nearest-neighbor dynamics → virial pressure "
        "P_virial = -⟨r · F⟩ / (3V) → effective fluid (ρ_eff, P_eff) → "
        "Friedmann acceleration ä/a = -(4πG/3)(ρ + 3P) → H(z)"
    ),
    status="RESEARCH_HYPOTHESIS",
    source_supported=False,
    mcmc_ready=False,
    prediction_allowed=False,
    required_inputs=[
        I1_LATTICE_GEOMETRY,
        I2_NEIGHBOR_COUNT,
        I3_CELL_VOLUME,
        I4_MASS_PROFILE,
        I5_DIPOLE_SCALE,
        I6_QUADRUPOLE_SCALE,
        I7_NEIGHBOR_DISTANCE,
        I8_ANISOTROPY_TENSOR,
        I9_TIME_AVERAGING,
        I10_BOUNDARY_CONDITIONS,
    ],
    risks=[
        R1_NOT_BUCKHOLTZ_MODEL,
        R2_BACKREACTION_TOO_SMALL,
        R3_LATTICE_BREAKS_HOMOGENEITY,
        R4_PARAMETER_DEGENERACY,
        R5_NO_AUTHOR_CONFIRMATION,
    ],
    author_clarification=Q_MVB_DISCRETE_LATTICE,
    safe_wording=(
        "SAFE: 'strongest candidate bridge route', 'research hypothesis', "
        "'computational reconstruction candidate', 'requires author confirmation', "
        "'if confirmed by Buckholtz', 'not yet source-supported'"
    ),
    unsafe_wording=(
        "UNSAFE: 'solves the F_oP → H(z) bridge', 'proves MULTING cosmology', "
        "'validated route', 'only viable path', 'Buckholtz's approach' (unless confirmed)"
    ),
)


# ============================================================================
# Registry Access Functions
# ============================================================================


def get_mvb_candidate() -> MVBCandidate:
    """Return the minimum viable bridge candidate.

    Returns:
        MVBCandidate: Discrete lattice + virial pressure route (RESEARCH_HYPOTHESIS)
    """
    return MVB_DISCRETE_LATTICE_VIRIAL


def is_mvb_source_supported() -> bool:
    """Check if MVB route is source-supported.

    Returns:
        False — always False (not confirmed in manuscript/communications)
    """
    return MVB_DISCRETE_LATTICE_VIRIAL.source_supported


def is_mcmc_allowed() -> bool:
    """Check if MCMC parameter estimation is allowed with MVB route.

    Returns:
        False — always False (not source-confirmed, cannot run MCMC)
    """
    return MVB_DISCRETE_LATTICE_VIRIAL.mcmc_ready


def is_prediction_allowed() -> bool:
    """Check if predictive modeling is allowed with MVB route.

    Returns:
        False — always False (not source-confirmed, cannot predict on new data)
    """
    return MVB_DISCRETE_LATTICE_VIRIAL.prediction_allowed


def get_minimum_author_question() -> AuthorClarification:
    """Return the minimum author clarification question for MVB route.

    Returns:
        AuthorClarification: Q_MVB about discrete lattice + virial pressure
    """
    return Q_MVB_DISCRETE_LATTICE


def get_mvb_status_summary() -> dict[str, str]:
    """Return summary of MVB status."""
    mvb = get_mvb_candidate()

    return {
        "route_name": mvb.name,
        "status": mvb.status,
        "source_supported": f"{mvb.source_supported} (NOT confirmed in manuscript)",
        "mcmc_ready": f"{mvb.mcmc_ready} (BLOCKED until author confirms)",
        "prediction_allowed": f"{mvb.prediction_allowed} (BLOCKED until source-confirmed)",
        "required_inputs_count": f"{len(mvb.required_inputs)} critical inputs needed",
        "risks_count": f"{len(mvb.risks)} risks documented",
        "author_question": mvb.author_clarification.question_id,
        "critical_blocker": (
            "MVB is a research hypothesis / computational reconstruction candidate. "
            "It is NOT source-supported. Cannot run MCMC or prediction until author "
            "confirms this is the intended bridge route (Q_MVB)."
        ),
        "safe_conclusion": (
            "Discrete lattice + virial pressure is the strongest candidate bridge route "
            "from pairwise force law to H(z). It is physically motivated, mathematically "
            "tractable, and testable. BUT: it is our reconstruction, not Buckholtz's "
            "confirmed model. Implementing it without author confirmation = testing our "
            "interpretation, not MULTING theory."
        ),
    }


# ============================================================================
# NO forward_model FUNCTION (INTENTIONAL)
# ============================================================================

# This module does NOT implement:
# - H_MVB(z, lattice_params)
# - forward_model_mvb(z, params)
# - build_virial_pressure(params)
# - compute_effective_fluid(z, params)

# Reason: MVB route is not source-confirmed.
# Cannot build forward model until Q_MVB is answered.

# If Q_MVB is answered affirmatively and route confirmed, function would be named:
# - build_forward_model_mvb(z, lattice_geometry, neighbor_count, ...) → H(z)
# NOT:
# - compute_H_MULTING(z, params) — ambiguous which route, implies source-confirmation
