"""
Beta parameter definitions for IDM/MULTING.

CRITICAL: This module explicitly allows conflicting definitions.
          Do NOT assume one value is "correct".
          All candidate values are recorded with their sources and interpretations.
"""

from dataclasses import dataclass
from typing import Optional

from .epistemic_registry import SourceRef, Status


@dataclass(frozen=True)
class BetaDefinition:
    """
    Definition of a beta parameter (beta_d or beta_q).

    Multiple conflicting definitions may exist for the same parameter
    if they represent different normalizations, versions, or contexts.
    """

    name: str
    symbol: str
    value: Optional[float]
    units: str
    source: Optional[SourceRef]
    equation_ref: Optional[str]  # Reference to equation that defines or uses it
    interpretation: str
    status: Status
    normalization_notes: str = ""


# Placeholder source for values requiring clarification
SOURCE_REQUIRES_CLARIFICATION = SourceRef(
    id="buckholtz_unclear",
    title="Buckholtz communications (requires clarification)",
    location="Multiple sources with conflicting values",
    note="Beta values appear in different contexts with different normalizations",
)


# Beta_d candidate definitions
BETA_D_CANDIDATE_1 = BetaDefinition(
    name="Beta_d (candidate value 4.25)",
    symbol="beta_d",
    value=4.25,
    units="dimensionless or length scale (unclear)",
    source=SOURCE_REQUIRES_CLARIFICATION,
    equation_ref="H(z) fit relation",
    interpretation="Dipole scale parameter (candidate 1)",
    status="unclear",
    normalization_notes=(
        "This value appears in some H(z) fitting contexts. "
        "Unclear if dimensionless or has length dimension. "
        "May represent a different normalization than candidate 2."
    ),
)

BETA_D_CANDIDATE_2 = BetaDefinition(
    name="Beta_d (candidate value 0.78)",
    symbol="beta_d",
    value=0.78,
    units="dimensionless or length scale (unclear)",
    source=SOURCE_REQUIRES_CLARIFICATION,
    equation_ref=None,
    interpretation="Dipole scale parameter (candidate 2)",
    status="unclear",
    normalization_notes=(
        "This value appears in different context. "
        "Relationship to candidate 1 (4.25) is unclear. "
        "May represent: (1) different normalization, (2) different version, "
        "(3) supplementary calculation, or (4) different physical interpretation."
    ),
)

# Beta_q candidate definitions
BETA_Q_CANDIDATE_1 = BetaDefinition(
    name="Beta_q (candidate value 8.10)",
    symbol="beta_q",
    value=8.10,
    units="dimensionless or length² scale (unclear)",
    source=SOURCE_REQUIRES_CLARIFICATION,
    equation_ref="H(z) fit relation",
    interpretation="Quadrupole scale parameter (candidate 1)",
    status="unclear",
    normalization_notes=(
        "This value appears in some H(z) fitting contexts. "
        "Unclear if dimensionless or has length² dimension. "
        "May represent a different normalization than candidate 2."
    ),
)

BETA_Q_CANDIDATE_2 = BetaDefinition(
    name="Beta_q (candidate value 0.19)",
    symbol="beta_q",
    value=0.19,
    units="dimensionless or length² scale (unclear)",
    source=SOURCE_REQUIRES_CLARIFICATION,
    equation_ref=None,
    interpretation="Quadrupole scale parameter (candidate 2)",
    status="unclear",
    normalization_notes=(
        "This value appears in different context. "
        "Relationship to candidate 1 (8.10) is unclear. "
        "May represent: (1) different normalization, (2) different version, "
        "(3) supplementary calculation, or (4) different physical interpretation."
    ),
)


def get_all_beta_definitions() -> list[BetaDefinition]:
    """
    Return all beta parameter definitions.

    Returns:
        List of all beta definitions, including conflicting candidates.
    """
    return [
        BETA_D_CANDIDATE_1,
        BETA_D_CANDIDATE_2,
        BETA_Q_CANDIDATE_1,
        BETA_Q_CANDIDATE_2,
    ]


def get_beta_d_candidates() -> list[BetaDefinition]:
    """Return all beta_d candidate definitions."""
    return [BETA_D_CANDIDATE_1, BETA_D_CANDIDATE_2]


def get_beta_q_candidates() -> list[BetaDefinition]:
    """Return all beta_q candidate definitions."""
    return [BETA_Q_CANDIDATE_1, BETA_Q_CANDIDATE_2]
