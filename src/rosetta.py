"""
Rosetta Stone: Buckholtz terminology to mainstream physics mapping.

Purpose: Facilitate communication by translating IDM/MULTING-specific
         terms into their possible mainstream analogues.
"""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class RosettaEntry:
    """Mapping between Buckholtz term and mainstream physics term."""

    buckholtz_term: str
    possible_mainstream_analogue: str
    confidence: Literal["low", "medium", "high"]
    caveat: str


# Rosetta mappings
ROSETTA_ENTRIES = [
    RosettaEntry(
        buckholtz_term="Isomeric Dark Matter (IDM)",
        possible_mainstream_analogue="Hidden sector / mirror-matter-like dark sector",
        confidence="medium",
        caveat=(
            "Mainstream 'hidden sector' typically refers to particles "
            "with no Standard Model charges. IDM's 'isomer' structure "
            "may imply more specific internal structure."
        ),
    ),
    RosettaEntry(
        buckholtz_term="Six isomers (5 dark + 1 ordinary)",
        possible_mainstream_analogue="Multiple dark sectors or flavors",
        confidence="low",
        caveat=(
            "'Isomer' in particle physics usually means nuclear isomers. "
            "Here it may mean: (1) multiple dark particle species, "
            "(2) different interaction channels, or (3) something novel."
        ),
    ),
    RosettaEntry(
        buckholtz_term="MULTING (multipole tiers)",
        possible_mainstream_analogue="Modified gravity with multipole terms",
        confidence="medium",
        caveat=(
            "Mainstream modified gravity (f(R), TeVeS, etc.) modifies "
            "field equations. MULTING seems to add multipole-like "
            "contributions to H(z). May be phenomenological."
        ),
    ),
    RosettaEntry(
        buckholtz_term="Dipole repulsion term",
        possible_mainstream_analogue="Effective repulsive modified-gravity term / dipole-like effect",
        confidence="low",
        caveat=(
            "GR is monopole-dominated. Dipole terms may violate PPN constraints "
            "(preferred-frame effects). Requires careful Solar System check."
        ),
    ),
    RosettaEntry(
        buckholtz_term="Quadrupole attraction term",
        possible_mainstream_analogue="Additional short-range attractive term",
        confidence="low",
        caveat=(
            "Could resemble: (1) higher-order GR corrections, "
            "(2) Yukawa-like modifications, or (3) tidal effects. "
            "Must not violate PPN tests."
        ),
    ),
    RosettaEntry(
        buckholtz_term="beta_d",
        possible_mainstream_analogue="Phenomenological scale parameter (length or dimensionless)",
        confidence="low",
        caveat=(
            "Without clear definition, unclear if beta_d is: "
            "(1) fundamental constant, (2) emergent scale, "
            "(3) fitted parameter, or (4) normalization choice."
        ),
    ),
    RosettaEntry(
        buckholtz_term="beta_q",
        possible_mainstream_analogue="Phenomenological scale parameter (length² or dimensionless)",
        confidence="low",
        caveat=("Similar to beta_d: definition and physical origin unclear."),
    ),
    RosettaEntry(
        buckholtz_term="Direct Outcomes methodology",
        possible_mainstream_analogue="Outcome-first / structured decision framework",
        confidence="medium",
        caveat=(
            "Appears to be a problem-solving methodology, not physics content. "
            "May be analogous to: (1) backwards induction, "
            "(2) goal-oriented reasoning, or (3) pragmatic philosophy."
        ),
    ),
    RosettaEntry(
        buckholtz_term="Eq.15 tau-electron relation",
        possible_mainstream_analogue="Numerical coincidence or deep physics relation (unclear)",
        confidence="low",
        caveat=(
            "Numerically reproducible relation between particle masses "
            "and fundamental constants. No known mainstream derivation. "
            "Could be: (1) coincidence, (2) numerology, or (3) hint at "
            "deeper structure. Requires physical mechanism."
        ),
    ),
    RosettaEntry(
        buckholtz_term="Future cosmic reversal / re-collapse",
        possible_mainstream_analogue="Cosmological turnaround (rare in ΛCDM)",
        confidence="low",
        caveat=(
            "ΛCDM with dark energy predicts eternal expansion. "
            "Re-collapse requires: (1) different dark energy equation of state, "
            "(2) modified gravity, or (3) novel mechanism."
        ),
    ),
    RosettaEntry(
        buckholtz_term="Particle mass predictions (sub-eV, TeV scale)",
        possible_mainstream_analogue="Beyond Standard Model (BSM) particle predictions",
        confidence="low",
        caveat=(
            "BSM predictions common in SUSY, extra dimensions, etc. "
            "Requires: (1) clear model structure, (2) detection strategy, "
            "(3) falsifiability criteria."
        ),
    ),
]


def get_all_rosetta_entries() -> list[RosettaEntry]:
    """Return all Rosetta Stone entries."""
    return ROSETTA_ENTRIES


def lookup_term(buckholtz_term: str) -> RosettaEntry | None:
    """
    Look up mainstream analogue for a Buckholtz term.

    Args:
        buckholtz_term: Term to look up

    Returns:
        RosettaEntry if found, None otherwise
    """
    for entry in ROSETTA_ENTRIES:
        if entry.buckholtz_term.lower() == buckholtz_term.lower():
            return entry
    return None


def get_low_confidence_mappings() -> list[RosettaEntry]:
    """Return mappings with low confidence (need clarification)."""
    return [e for e in ROSETTA_ENTRIES if e.confidence == "low"]


def get_high_confidence_mappings() -> list[RosettaEntry]:
    """Return mappings with high confidence."""
    return [e for e in ROSETTA_ENTRIES if e.confidence == "high"]
