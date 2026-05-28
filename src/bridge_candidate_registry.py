"""
Bridge Candidate Registry — F_oP → H(z) Mapping Routes

Purpose: Document all possible routes from pairwise MULTING force law to cosmological expansion.

Status: TRIAGE COMPLETE — zero source-supported bridges found.

MCMC readiness: BLOCKED (no F_oP → H(z) mapping).

See: docs/36_force_to_expansion_bridge_triage.md
"""

from dataclasses import dataclass
from enum import Enum


class BridgeStatus(Enum):
    """Source and derivation status for bridge route."""

    SOURCE_SUPPORTED = "source_supported"  # Confirmed in manuscript/communications
    COMPUTATIONAL_RECONSTRUCTION = "computational_reconstruction"  # Audit-derived implementation
    SPECULATIVE_TOY_MODEL = "speculative_toy_model"  # Research proposal, not source-confirmed
    DEAD_END = "dead_end"  # Evaluated and rejected (wrong regime, wrong physics)


class CodePermission(Enum):
    """What operations are allowed with this bridge route."""

    ALLOWED_FOR_TOY_MODEL_ONLY = "allowed_for_toy_model_only"  # Research code, not Buckholtz model
    ALLOWED_FOR_SPECULATIVE_EXPLORATION = (
        "allowed_for_speculative_exploration"  # Exploratory research
    )
    ALLOWED_FOR_FIT_REPRODUCTION_ONLY = (
        "allowed_for_fit_reproduction_only"  # Phenomenological fit, not prediction
    )
    ALLOWED_FOR_COMPUTATIONAL_RESEARCH = "allowed_for_computational_research"  # N-body, simulations
    NOT_ALLOWED = "not_allowed"  # Rejected route


@dataclass
class RequiredAuthorInput:
    """Input information needed from Dr. Buckholtz to proceed with bridge route."""

    question_id: str  # Q0, Q1, etc.
    question_text: str  # Specific question for author
    why_needed: str  # What this unblocks
    priority: str  # CRITICAL, HIGH, MEDIUM, LOW


@dataclass
class BridgeCandidate:
    """Single F_oP → H(z) bridge route candidate."""

    name: str  # "Newtonian dust + extra forces", etc.
    route_type: str  # Physical description
    status: BridgeStatus  # SOURCE_SUPPORTED, COMPUTATIONAL_RECONSTRUCTION, etc.
    source_support: bool  # Found in manuscript/communications?
    assumptions: list[str]  # What this route assumes
    code_permission: CodePermission  # What operations allowed
    mcmc_ready: bool  # Can this route support MCMC?
    predictive_use_allowed: bool  # Can this route predict on new data?
    author_clarification_needed: list[RequiredAuthorInput]  # What questions must be answered
    critical_nuance: str  # Important caveats or subtleties
    why_not_source_supported: str  # Why this is not confirmed (if status ≠ SOURCE_SUPPORTED)


# ============================================================================
# Bridge Candidate Records
# ============================================================================

Q0_FORCE_TO_EXPANSION = RequiredAuthorInput(
    question_id="Q0",
    question_text=(
        "How does the pairwise MULTING force law F_oP = F_m - F_d + F_q translate into "
        "a cosmological background expansion equation H(z)? Is there a modified Friedmann "
        "equation, an effective stress-energy tensor, a spatial averaging prescription "
        "(e.g., backreaction framework), or is H_MULT(z) a phenomenological parametrization "
        "independent of the pairwise force law?"
    ),
    why_needed="Required to build forward model H_MULT(z; params) for MCMC",
    priority="CRITICAL",
)

ROUTE_A_NEWTONIAN_DUST = BridgeCandidate(
    name="Route A: Newtonian Dust + Extra Forces",
    route_type="Computational reconstruction (Newtonian averaging)",
    status=BridgeStatus.COMPUTATIONAL_RECONSTRUCTION,
    source_support=False,
    assumptions=[
        "MULTING forces are perturbations to standard FLRW background",
        "Homogeneous averaging preserves dipole/quadrupole contributions (non-standard)",
        "Effective equation of state w_eff can capture multipole effects",
    ],
    code_permission=CodePermission.ALLOWED_FOR_TOY_MODEL_ONLY,
    mcmc_ready=False,
    predictive_use_allowed=False,
    author_clarification_needed=[Q0_FORCE_TO_EXPANSION],
    critical_nuance=(
        "Standard homogeneous Newtonian averaging nulls dipole/quadrupole background "
        "contributions (spatial gradients average to zero in FRW symmetry). This is NOT "
        "a refutation — it means MULTING may use non-standard averaging prescription "
        "(backreaction framework) or effective stress-energy formalism."
    ),
    why_not_source_supported="No manuscript material indicates Newtonian dust + averaging approach",
)

ROUTE_B_STRESS_ENERGY = BridgeCandidate(
    name="Route B: Effective Stress-Energy Tensor",
    route_type="Speculative toy model (T_μν formalism)",
    status=BridgeStatus.SPECULATIVE_TOY_MODEL,
    source_support=False,
    assumptions=[
        "MULTING forces map to effective stress-energy tensor components",
        "Dipole = anisotropic stress or bulk viscosity",
        "Quadrupole = higher-order tensor structure",
    ],
    code_permission=CodePermission.ALLOWED_FOR_SPECULATIVE_EXPLORATION,
    mcmc_ready=False,
    predictive_use_allowed=False,
    author_clarification_needed=[Q0_FORCE_TO_EXPANSION],
    critical_nuance=(
        "Physical mechanism mapping F_d to T_μν^(dipole) is unclear. If dipole = DM-DM "
        "scattering force → stress-energy map not obvious. If dipole = metric modification "
        "→ need weak-field expansion."
    ),
    why_not_source_supported="No manuscript material indicates stress-energy tensor formalism",
)

ROUTE_C_PARAMETRIZED_FRIEDMANN = BridgeCandidate(
    name="Route C: Parametrized Friedmann (MGCAMB-style)",
    route_type="Computational reconstruction (phenomenological parametrization)",
    status=BridgeStatus.COMPUTATIONAL_RECONSTRUCTION,
    source_support=False,
    assumptions=[
        "H²(z) parametrized as phenomenological function of (beta_d, beta_q, cosmological params)",
        "Functional form f(z) chosen to fit observations",
        "No physical mechanism required — effective description",
    ],
    code_permission=CodePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
    mcmc_ready=False,
    predictive_use_allowed=False,
    author_clarification_needed=[Q0_FORCE_TO_EXPANSION],
    critical_nuance=(
        "Arbitrary functional form (infinite choices). No connection to pairwise force law "
        "(F_oP unused). Phenomenology, not physics. Distinct from heuristic Phi(z) closure "
        "(docs/35) which has specific sign structure matching force law."
    ),
    why_not_source_supported="No specific functional form H²(z; beta_d, beta_q) provided in manuscript",
)

ROUTE_D_SCALAR_FIELD = BridgeCandidate(
    name="Route D: Scalar Field / Dark Energy Map",
    route_type="Speculative toy model (quintessence/k-essence)",
    status=BridgeStatus.SPECULATIVE_TOY_MODEL,
    source_support=False,
    assumptions=[
        "Dipole maps to kinetic term φ̇²",
        "Quadrupole maps to potential V(φ)",
        "Scalar field evolution drives H(z)",
    ],
    code_permission=CodePermission.ALLOWED_FOR_SPECULATIVE_EXPLORATION,
    mcmc_ready=False,
    predictive_use_allowed=False,
    author_clarification_needed=[Q0_FORCE_TO_EXPANSION],
    critical_nuance=(
        "Why would pairwise gravitational forces map to scalar field? Mechanism unclear. "
        "No source material indicates MULTING uses scalar field formalism."
    ),
    why_not_source_supported="No manuscript material indicates scalar field / dark energy framework",
)

ROUTE_E_BACKREACTION = BridgeCandidate(
    name="Route E: N-body → Fluid Backreaction",
    route_type="Speculative toy model (Buchert formalism, inhomogeneous cosmology)",
    status=BridgeStatus.SPECULATIVE_TOY_MODEL,
    source_support=False,
    assumptions=[
        "Pairwise forces implemented in N-body simulation",
        "Spatial averaging of inhomogeneous spacetime gives effective H(z)",
        "Backreaction ≠ 0 (breaks FLRW assumption)",
    ],
    code_permission=CodePermission.ALLOWED_FOR_COMPUTATIONAL_RESEARCH,
    mcmc_ready=False,
    predictive_use_allowed=False,
    author_clarification_needed=[Q0_FORCE_TO_EXPANSION],
    critical_nuance=(
        "Computationally expensive. Does MULTING require inhomogeneous cosmology, or does "
        "it admit FLRW background? If FLRW preserved → backreaction unnecessary. If FLRW "
        "broken → need inhomogeneous field equations."
    ),
    why_not_source_supported="No manuscript material indicates backreaction / inhomogeneous cosmology framework",
)

ROUTE_F_PPN_EXTRAPOLATION = BridgeCandidate(
    name="Route F: PPN Extrapolation to Cosmology",
    route_type="Dead end (wrong regime, wrong scales)",
    status=BridgeStatus.DEAD_END,
    source_support=False,
    assumptions=[
        "PPN parameters (γ, β) extracted from local MULTING forces",
        "PPN extrapolated to cosmological scales",
    ],
    code_permission=CodePermission.NOT_ALLOWED,
    mcmc_ready=False,
    predictive_use_allowed=False,
    author_clarification_needed=[],
    critical_nuance=(
        "PPN is weak-field, slow-velocity expansion. Cosmology is strong curvature, relativistic. "
        "PPN parameters describe local metric perturbations (r ~ AU). Cosmological H(z) operates "
        "at r ~ Gpc. If dipole ~ 4.5 Mpc → negligible at AU → γ=1, β=1 (GR recovered) → no "
        "cosmological effect. If dipole at AU → violates Cassini constraints. PPN extrapolation "
        "cannot connect local tests to cosmological expansion."
    ),
    why_not_source_supported="PPN extrapolation physically invalid for this regime",
)


# ============================================================================
# Registry Access Functions
# ============================================================================


def get_all_bridge_candidates() -> list[BridgeCandidate]:
    """Return all F_oP → H(z) bridge route candidates."""
    return [
        ROUTE_A_NEWTONIAN_DUST,
        ROUTE_B_STRESS_ENERGY,
        ROUTE_C_PARAMETRIZED_FRIEDMANN,
        ROUTE_D_SCALAR_FIELD,
        ROUTE_E_BACKREACTION,
        ROUTE_F_PPN_EXTRAPOLATION,
    ]


def get_source_supported_bridges() -> list[BridgeCandidate]:
    """Return only source-supported bridge routes.

    Returns:
        list[BridgeCandidate]: Empty list (zero source-supported bridges found)
    """
    return [
        bridge
        for bridge in get_all_bridge_candidates()
        if bridge.status == BridgeStatus.SOURCE_SUPPORTED
    ]


def get_computational_reconstructions() -> list[BridgeCandidate]:
    """Return computational reconstruction candidates (audit-derived implementations)."""
    return [
        bridge
        for bridge in get_all_bridge_candidates()
        if bridge.status == BridgeStatus.COMPUTATIONAL_RECONSTRUCTION
    ]


def get_speculative_toy_models() -> list[BridgeCandidate]:
    """Return speculative toy model candidates (research proposals)."""
    return [
        bridge
        for bridge in get_all_bridge_candidates()
        if bridge.status == BridgeStatus.SPECULATIVE_TOY_MODEL
    ]


def get_dead_end_routes() -> list[BridgeCandidate]:
    """Return rejected routes (evaluated and found invalid)."""
    return [
        bridge for bridge in get_all_bridge_candidates() if bridge.status == BridgeStatus.DEAD_END
    ]


def get_mcmc_ready_bridges() -> list[BridgeCandidate]:
    """Return bridges ready for MCMC parameter estimation.

    Returns:
        list[BridgeCandidate]: Empty list (zero MCMC-ready bridges found)
    """
    return [bridge for bridge in get_all_bridge_candidates() if bridge.mcmc_ready]


def get_priority_zero_question() -> RequiredAuthorInput:
    """Return Priority 0 question (critical blocker for MCMC).

    Returns:
        RequiredAuthorInput: Q0 force-to-expansion mapping question
    """
    return Q0_FORCE_TO_EXPANSION


# ============================================================================
# Hard Guards (ENFORCE RESTRICTIONS)
# ============================================================================


def is_mcmc_allowed() -> bool:
    """Check if MCMC parameter estimation is allowed with current bridge routes.

    Returns:
        False — always False (zero MCMC-ready bridges).
               Cannot run MCMC without source-supported F_oP → H(z) mapping.
    """
    return len(get_mcmc_ready_bridges()) > 0


def is_predictive_modeling_allowed() -> bool:
    """Check if predictive modeling is allowed with current bridge routes.

    Returns:
        False — always False (zero source-supported bridges).
               Cannot predict on new data without source-confirmed route.
    """
    return any(bridge.predictive_use_allowed for bridge in get_all_bridge_candidates())


def get_bridge_status_summary() -> dict[str, str]:
    """Return summary of bridge candidate status."""
    all_bridges = get_all_bridge_candidates()
    source_supported = get_source_supported_bridges()
    reconstructions = get_computational_reconstructions()
    toy_models = get_speculative_toy_models()
    dead_ends = get_dead_end_routes()
    mcmc_ready = get_mcmc_ready_bridges()

    return {
        "total_routes": f"{len(all_bridges)} evaluated (A, B, C, D, E, F)",
        "source_supported": f"{len(source_supported)} found (CRITICAL BLOCKER)",
        "computational_reconstructions": f"{len(reconstructions)} candidates (A: Newtonian dust, C: parametrized Friedmann)",
        "speculative_toy_models": f"{len(toy_models)} candidates (B: stress-energy, D: scalar field, E: backreaction)",
        "dead_ends": f"{len(dead_ends)} rejected (F: PPN extrapolation)",
        "mcmc_ready": f"{len(mcmc_ready)} routes (MCMC BLOCKED)",
        "priority_zero_question": Q0_FORCE_TO_EXPANSION.question_id,
        "critical_blocker": (
            "No source-supported F_oP → H(z) mapping found. All routes are audit "
            "reconstructions or speculative proposals. MCMC remains blocked until Q0 answered."
        ),
        "safe_conclusion": (
            "Six possible bridge routes exist (Newtonian dust, stress-energy, parametrized "
            "Friedmann, scalar field, backreaction, PPN). None are source-supported. Implementing "
            "any route without author confirmation = testing our interpretation, not Buckholtz's model."
        ),
    }


# ============================================================================
# NO forward_model FUNCTION (INTENTIONAL)
# ============================================================================

# This module does NOT implement:
# - H_MULT(z, beta_d, beta_q)
# - forward_model(z, params)
# - build_friedmann_equation(params)
# - compute_expansion_rate(z, params)

# Reason: No source-supported F_oP → H(z) mapping available.
# Cannot build forward model without knowing which bridge route to use.

# If Q0 is answered and source-supported route identified, function would be named:
# - build_forward_model_route_X(z, params) where X = A, B, C, D, or E
# NOT:
# - compute_H_MULT(z, params) — ambiguous which route
