"""
MULTING Force Law Records — Source-Candidate Documentation

Purpose: Document candidate pairwise force-law formulas from public materials.

Status: SOURCE_CANDIDATE (awaiting manual PDF verification)
Code Permission: allowed_for_dimensional_check ONLY
NOT allowed: H(z) modeling, MCMC fitting, cosmological predictions

See: docs/33_public_formula_stripping_report.md
"""

from dataclasses import dataclass
from enum import Enum


class ProvenanceStatus(Enum):
    """Source verification status."""

    SOURCE_CANDIDATE = "source_candidate"  # Formula-stripping extraction, not verified
    SOURCE_CONFIRMED = "source_confirmed"  # Manually verified against PDF
    SOURCE_INCORRECT = "source_incorrect"  # Verification failed, extraction error


class UnitsStatus(Enum):
    """Dimensional analysis status."""

    CORRECT = "correct"  # Units verified for force [kg·m/s²]
    INCORRECT = "incorrect"  # Dimensional mismatch
    UNKNOWN = "unknown"  # Not yet analyzed


class CodePermission(Enum):
    """What operations are allowed with this formula."""

    ALLOWED_FOR_RECORD_ONLY = "allowed_for_record_only"  # Document only, no computation
    ALLOWED_FOR_DIMENSIONAL_CHECK = (
        "allowed_for_dimensional_check"  # Can verify units, cannot compute H(z)
    )
    NOT_ALLOWED_FOR_HZ_MODELING = (
        "not_allowed_for_hz_modeling"  # Explicit block on cosmological modeling
    )


@dataclass
class ForceLawRecord:
    """Single force-law equation record (monopole, dipole, quadrupole, or total)."""

    name: str  # "monopole", "dipole", "quadrupole", "total"
    equation_latex: str  # LaTeX representation
    status: ProvenanceStatus  # SOURCE_CANDIDATE until manually verified
    source_note: str  # Where this was found (table, equation number, page)
    variables: dict[str, str]  # Variable name → description
    units_status: UnitsStatus  # Dimensional analysis result
    code_permission: CodePermission  # What operations are allowed
    interpretation: str  # Physical meaning


@dataclass
class LengthScaleRecord:
    """Beta length-scale definition (r_dA, r_dP, r_qAB)."""

    name: str  # "r_dA", "r_dP", "r_qAB"
    definition_latex: str  # LaTeX representation
    status: ProvenanceStatus  # SOURCE_CANDIDATE until manually verified
    source_note: str  # Where this was found
    beta_parameter: str  # Which beta (beta_d or beta_q)
    characteristic_radius: str  # Which r (r_A, r_P, or product)
    units: str  # Expected units ([length] or [length²])
    code_permission: CodePermission  # What operations are allowed
    interpretation_unknown: str  # What we don't know about this scale


@dataclass
class ClosureRequirement:
    """Missing component required to go from force law → H(z)."""

    requirement_type: str  # "mean_field", "closure_relation", "friedmann_equation", etc.
    description: str  # What is missing
    blocker_severity: str  # "CRITICAL", "HIGH", "MEDIUM"
    what_we_need: str  # Specific deliverable required
    example_from_lcdm: str  # How ΛCDM solves this (for comparison)


# ============================================================================
# Force Law Records
# ============================================================================


MONOPOLE_FORCE = ForceLawRecord(
    name="monopole",
    equation_latex=r"F_m = \frac{G m_A m_P}{r^2}",
    status=ProvenanceStatus.SOURCE_CANDIDATE,
    source_note="docs/33 extraction from public materials — awaiting manual PDF verification",
    variables={
        "G": "gravitational constant",
        "m_A": "mass of object A",
        "m_P": "mass of object P (probe/test mass)",
        "r": "separation distance",
    },
    units_status=UnitsStatus.CORRECT,
    code_permission=CodePermission.ALLOWED_FOR_DIMENSIONAL_CHECK,
    interpretation="Standard Newtonian gravitational force between two gravitating objects A and P.",
)


DIPOLE_FORCE = ForceLawRecord(
    name="dipole",
    equation_latex=r"F_d = \frac{G c^{-2} (k_A m_P |r_{dA}| + k_P m_A |r_{dP}|)}{r^3}",
    status=ProvenanceStatus.SOURCE_CANDIDATE,
    source_note="docs/33 extraction from public materials — awaiting manual PDF verification",
    variables={
        "G": "gravitational constant",
        "c": "speed of light",
        "k_A": "kinetic energy scale of object A (units: energy = kg·m²/s²)",
        "k_P": "kinetic energy scale of object P",
        "m_A": "mass of object A",
        "m_P": "mass of object P",
        "r_dA": "dipole length scale for A = beta_d × r_A",
        "r_dP": "dipole length scale for P = beta_d × r_P",
        "r": "separation distance",
    },
    units_status=UnitsStatus.CORRECT,
    code_permission=CodePermission.ALLOWED_FOR_DIMENSIONAL_CHECK,
    interpretation="Velocity/kinetic-energy-dependent correction, 1/r³ scaling (dipole). Physical mechanism for exponent unclear. Sign structure (subtractive in F_oP) unclear — repulsive under certain kinematic conditions?",
)


QUADRUPOLE_FORCE = ForceLawRecord(
    name="quadrupole",
    equation_latex=r"F_q = \frac{G k_A k_P c^{-4} |r_{qAB}|^2}{r^4}",
    status=ProvenanceStatus.SOURCE_CANDIDATE,
    source_note="docs/33 extraction from public materials — awaiting manual PDF verification",
    variables={
        "G": "gravitational constant",
        "c": "speed of light",
        "k_A": "kinetic energy scale of object A",
        "k_P": "kinetic energy scale of object P",
        "r_qAB": "quadrupole length scale = beta_q² × r_A × r_P",
        "r": "separation distance",
    },
    units_status=UnitsStatus.CORRECT,
    code_permission=CodePermission.ALLOWED_FOR_DIMENSIONAL_CHECK,
    interpretation="Higher-order correction, 1/r⁴ scaling (quadrupole). Physical mechanism unclear.",
)


TOTAL_FORCE = ForceLawRecord(
    name="total",
    equation_latex=r"F_{oP} = F_m - F_d + F_q",
    status=ProvenanceStatus.SOURCE_CANDIDATE,
    source_note="docs/33 extraction from public materials — awaiting manual PDF verification",
    variables={
        "F_m": "monopole force (attractive)",
        "F_d": "dipole force (subtractive — reduces attraction or repulsive?)",
        "F_q": "quadrupole force (additive — enhances attraction)",
    },
    units_status=UnitsStatus.CORRECT,
    code_permission=CodePermission.ALLOWED_FOR_DIMENSIONAL_CHECK,
    interpretation="Net force on probe P from object A. Sign structure: monopole (+), dipole (−), quadrupole (+). Why dipole is subtractive requires clarification from author.",
)


# ============================================================================
# Beta Length-Scale Records
# ============================================================================


R_DA_SCALE = LengthScaleRecord(
    name="r_dA",
    definition_latex=r"r_{dA} = \beta_d \times r_A",
    status=ProvenanceStatus.SOURCE_CANDIDATE,
    source_note="docs/33 extraction from public materials — awaiting manual PDF verification",
    beta_parameter="beta_d = 4.5 (candidate value from Table A1)",
    characteristic_radius="r_A (characteristic radius of object A)",
    units="[length] (meters)",
    code_permission=CodePermission.ALLOWED_FOR_RECORD_ONLY,
    interpretation_unknown="Physical interpretation unclear. Scale at which dipole becomes significant? Cutoff radius? Effective interaction range? What is r_A for Sun? Earth? Dark matter halo?",
)


R_DP_SCALE = LengthScaleRecord(
    name="r_dP",
    definition_latex=r"r_{dP} = \beta_d \times r_P",
    status=ProvenanceStatus.SOURCE_CANDIDATE,
    source_note="docs/33 extraction from public materials — awaiting manual PDF verification",
    beta_parameter="beta_d = 4.5 (candidate value from Table A1)",
    characteristic_radius="r_P (characteristic radius of object P)",
    units="[length] (meters)",
    code_permission=CodePermission.ALLOWED_FOR_RECORD_ONLY,
    interpretation_unknown="Physical interpretation unclear. Same beta_d as r_dA. Symmetric treatment of A and P.",
)


R_QAB_SCALE = LengthScaleRecord(
    name="r_qAB",
    definition_latex=r"|r_{qAB}|^2 = \beta_q^2 \times r_A \times r_P",
    status=ProvenanceStatus.SOURCE_CANDIDATE,
    source_note="docs/33 extraction from public materials — awaiting manual PDF verification",
    beta_parameter="beta_q = 18.0 (candidate value from Table A1)",
    characteristic_radius="r_A × r_P (product of characteristic radii)",
    units="[length²] (meters²)",
    code_permission=CodePermission.ALLOWED_FOR_RECORD_ONLY,
    interpretation_unknown="Physical interpretation unclear. Product of characteristic scales? Geometric mean with beta_q correction?",
)


# ============================================================================
# Missing Closure Components (CRITICAL BLOCKERS)
# ============================================================================


MEAN_FIELD_APPROXIMATION = ClosureRequirement(
    requirement_type="mean_field_approximation",
    description="How to go from pairwise forces between individual objects (A and P) to fluid-level stress-energy tensor T_μν for cosmological averaging.",
    blocker_severity="CRITICAL",
    what_we_need="Mean-field / virial approximation that maps pairwise MULTING force → effective gravitational potential → T_μν → Friedmann equations.",
    example_from_lcdm="ΛCDM: Newtonian gravity → Einstein equations (G_μν = 8πG T_μν) → Friedmann equations for fluid. MULTING: (MULTING force law → ??? → ??? → H²(z; params)). Missing steps.",
)


COSMOLOGICAL_AVERAGE = ClosureRequirement(
    requirement_type="cosmological_averaging",
    description="How to average MULTING forces over cosmic web structure (galaxy clusters, voids, large-scale structure).",
    blocker_severity="CRITICAL",
    what_we_need="Prescription for spatial averaging over G-ECOS 'solutions' (isomers, dark matter halos, galaxy clusters). What is the number density n(z) of solutions? How do we sum over all pairwise interactions?",
    example_from_lcdm="ΛCDM: smooth fluid approximation (ignores clustering below Hubble scale). MULTING: discrete solutions → need number density, clustering statistics, cutoff scale.",
)


CLOSURE_RELATIONS = ClosureRequirement(
    requirement_type="closure_relations",
    description="How do masses m_A(z), radii r_A(z), kinetic energies k_A(z), and separations D_C:AB(z) evolve with redshift z?",
    blocker_severity="CRITICAL",
    what_we_need="Evolutionary equations or phenomenological models for: m_A(z), r_A(z), k_A(z), comoving distance D_C:AB(z). Without these, cannot evaluate force law at arbitrary redshift.",
    example_from_lcdm="ΛCDM: ρ(z) = ρ₀(1+z)³ for matter. MULTING: need m_A(z), r_A(z), k_A(z) evolution — are these constant? Do they scale with (1+z)? Derived from structure formation?",
)


FRIEDMANN_LIKE_EQUATIONS = ClosureRequirement(
    requirement_type="friedmann_equation",
    description="What is the modified Friedmann equation H²(z; beta_d, beta_q, ...) that incorporates MULTING force corrections?",
    blocker_severity="CRITICAL",
    what_we_need="Closed-form or numerical H_MULT(z; params) that can be compared with H_FLRW(z; Ωm, ΩΛ, H0). This is the forward model required for MCMC fitting.",
    example_from_lcdm="ΛCDM: H²(z) = H₀²[Ωm(1+z)³ + ΩΛ]. MULTING: H_MULT²(z; beta_d, beta_q, ...) = ??? (not provided in public materials).",
)


LIKELIHOOD_FUNCTION = ClosureRequirement(
    requirement_type="likelihood_function",
    description="Statistical model P(H_obs | H_MULT(z; params)) for comparing MULTING predictions to observational data.",
    blocker_severity="HIGH",
    what_we_need="Likelihood function for MCMC: P(data | params). Requires H_MULT(z; params) as forward model. Also need priors on beta_d, beta_q, and any additional parameters.",
    example_from_lcdm="ΛCDM: χ² = Σ[(H_obs(z_i) - H_ΛCDM(z_i; Ωm, H0))² / σ_i²]. MULTING: χ² = Σ[(H_obs(z_i) - H_MULT(z_i; beta_d, beta_q, ...))² / σ_i²] — blocked by missing H_MULT formula.",
)


# ============================================================================
# Registry Access Functions
# ============================================================================


def get_all_force_laws() -> list[ForceLawRecord]:
    """Return all MULTING force-law records."""
    return [MONOPOLE_FORCE, DIPOLE_FORCE, QUADRUPOLE_FORCE, TOTAL_FORCE]


def get_all_length_scales() -> list[LengthScaleRecord]:
    """Return all beta length-scale records."""
    return [R_DA_SCALE, R_DP_SCALE, R_QAB_SCALE]


def get_all_closure_requirements() -> list[ClosureRequirement]:
    """Return all missing closure components that block H(z) modeling."""
    return [
        MEAN_FIELD_APPROXIMATION,
        COSMOLOGICAL_AVERAGE,
        CLOSURE_RELATIONS,
        FRIEDMANN_LIKE_EQUATIONS,
        LIKELIHOOD_FUNCTION,
    ]


def get_critical_blockers() -> list[ClosureRequirement]:
    """Return only CRITICAL-severity blockers."""
    return [req for req in get_all_closure_requirements() if req.blocker_severity == "CRITICAL"]


def is_hz_modeling_allowed() -> bool:
    """Check if H(z) modeling is allowed with current force-law records.

    Returns:
        False — always False until closure requirements are met.
    """
    return False


def get_force_law_status_summary() -> dict[str, str]:
    """Return summary of force-law layer status."""
    return {
        "force_law_layer": "SOURCE_CANDIDATE (awaiting manual PDF verification)",
        "cosmological_closure": "MISSING (no H_MULT(z) formula)",
        "mcmc_readiness": "BLOCKED (no forward model)",
        "code_permission": "allowed_for_dimensional_check ONLY",
        "safe_conclusion": (
            "MULTING provides candidate pairwise force law with monopole, dipole, and quadrupole terms. "
            "Public materials do not provide computational closure for mapping this force law to "
            "cosmological expansion H(z) or for MCMC parameter estimation."
        ),
    }
