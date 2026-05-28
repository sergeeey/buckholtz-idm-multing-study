"""
Beta Provenance Registry — Source Tracking

CRITICAL: This module tracks the ACTUAL SOURCE of each beta value.

Do NOT confuse:
- "We derived 17/4 from anchors" → provenance_status = audit_reconstruction
- "Buckholtz stated beta_d = 4.25" → provenance_status = buckholtz_stated

Circular reasoning check: If we use audit_reconstruction values in H(z),
then validate H(z) against data, we are testing OUR reconstruction, not
Buckholtz's model.

Status taxonomy enforced:
- source_confirmed: Verified in peer-reviewed publication
- buckholtz_stated: Stated in communication/draft (not peer-reviewed)
- audit_reconstruction: We inferred from internal anchors
- source_missing: No known source for this value
- ai_generated_supplementary: From AI summary/exploration
- fitted_claim: Stated as fitted to data
- derived_claim: Stated as derived from theory
"""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class BetaProvenance:
    """
    Provenance record for a single beta candidate value.

    This is NOT physics metadata — it is SOURCE VERIFICATION.
    """

    beta_name: str  # e.g., "beta_d_1"
    value: float  # Numerical value
    source_type: Literal[
        "preprint",
        "peer_reviewed",
        "email",
        "draft_manuscript",
        "ai_summary",
        "audit_reconstruction",
        "manuscript_appendix",
        "manuscript_appendix_table_A1",
        "supplementary_table",
        "unknown",
    ]
    first_known_appearance: str  # "Preprint v2 Eq.42" or "Our reconstruction 17/4" or "Unknown"
    provenance_status: Literal[
        "source_confirmed",  # Explicit statement in verifiable source
        "buckholtz_stated",  # Stated by author (email/draft)
        "manuscript_reported_fitted",  # Reported in manuscript as fitted value
        "source_candidate_pending_manual_verification",  # NotebookLM/AI suggested, needs manual check
        "supplementary_exploratory",  # From supplementary/exploratory analysis
        "audit_reconstruction",  # We derived from anchors
        "source_missing",  # No known source
        "ai_generated_supplementary",  # From AI exploration
        "fitted_claim",  # Stated as fitted to data
        "derived_claim",  # Stated as derived from theory
    ]
    use_permission_status: Literal[
        "allowed_for_arithmetic_only",  # Can use in anchor search, NOT modeling
        "allowed_for_toy_model_only",  # Can use in exploratory code, NOT production
        "allowed_for_fit_reproduction_only",  # Can reproduce fit, NOT predict new data
        "do_not_use_for_modeling",  # BLOCKED for H(z) until source confirmed
        "source_confirmed",  # OK to use
    ]
    evidence_trail: str  # What evidence exists (or lacks) for this value
    recommended_action: str  # What to do before using this value
    manual_verification_status: str | None = None  # "manually_verified" or None
    derivation_status: str | None = None  # "fitted_not_derived" / "derived_from_theory" / None
    manuscript_identifier: str | None = None  # arXiv ID, DOI, or preprint ID


# Beta Provenance Registry (SINGLE SOURCE OF TRUTH)
BETA_PROVENANCE_REGISTRY: dict[str, BetaProvenance] = {
    "beta_d_1": BetaProvenance(
        beta_name="beta_d_1",
        value=4.25,
        source_type="audit_reconstruction",
        first_known_appearance="Audit reconstruction 17/4 from Eq.20 Higgs ratio",
        provenance_status="audit_reconstruction",
        use_permission_status="do_not_use_for_modeling",
        evidence_trail=(
            "❓ No direct quote from Buckholtz stating 'beta_d = 4.25'. "
            "❓ No preprint available for verification. "
            "✅ Audit reconstruction: We derived 4.25 from internal anchor 17/4 (exact match). "
            "⚠️ 7 alternative formulas exist within 1.2% error (uniqueness score 0.40)."
        ),
        recommended_action=(
            "Explicit confirmation from Buckholtz required: "
            "(1) Is beta_d intended to be derived from Eq.20? "
            "(2) Which specific formula (17/4 vs 17/N_max vs other)? "
            "(3) Units and normalization scheme?"
        ),
    ),
    "beta_d_2": BetaProvenance(
        beta_name="beta_d_2",
        value=0.78,
        source_type="audit_reconstruction",
        first_known_appearance="Audit reconstruction 7/9 ≈ 0.7778 from Eq.20 W/Z ratio",
        provenance_status="audit_reconstruction",
        use_permission_status="do_not_use_for_modeling",
        evidence_trail=(
            "❓ No direct quote from Buckholtz stating 'beta_d = 0.78'. "
            "❓ No preprint available. "
            "✅ Audit reconstruction: We derived 0.78 ≈ 7/9 from Eq.20 (error 0.28%). "
            "❌ **20 alternative formulas** within 5% error (uniqueness score 0.10) — HIGH structured numerology risk."
        ),
        recommended_action=(
            "Explicit confirmation from Buckholtz required: "
            "(1) Is beta_d = 0.78 or 7/9 = 0.7778? "
            "(2) Which normalization scheme? "
            "(3) Why 0.78 and not one of the 20 alternatives?"
        ),
    ),
    "beta_q_1": BetaProvenance(
        beta_name="beta_q_1",
        value=8.10,
        source_type="unknown",
        first_known_appearance="Unknown — cannot be reconstructed from known anchors",
        provenance_status="source_missing",
        use_permission_status="do_not_use_for_modeling",
        evidence_trail=(
            "❓ No direct quote from Buckholtz. "
            "❓ No preprint available. "
            "❌ No successful reconstruction from internal anchors (best match: 2×4 = 8.0, error 1.23%). "
            "Hypothesis: May require additional anchors (81?) or different formula structure or fitted to data."
        ),
        recommended_action=(
            "**HIGHEST PRIORITY for clarification.** "
            "Explicit source needed: "
            "(1) Where does 8.10 come from? "
            "(2) Is it derived from anchors (which ones?) or fitted to data? "
            "(3) Units?"
        ),
    ),
    "beta_q_2": BetaProvenance(
        beta_name="beta_q_2",
        value=0.19,
        source_type="audit_reconstruction",
        first_known_appearance="Audit reconstruction (1×4)/(3×7) ≈ 0.1905 from anchors",
        provenance_status="audit_reconstruction",
        use_permission_status="do_not_use_for_modeling",
        evidence_trail=(
            "❓ No direct quote from Buckholtz stating 'beta_q = 0.19'. "
            "❓ No preprint available. "
            "✅ Audit reconstruction: We derived 0.19 ≈ 4/21 from anchor formula (error 0.25%). "
            "⚠️ Requires complexity-2 formula (ratio of products) — less plausible than simple ratios."
        ),
        recommended_action=(
            "Explicit confirmation from Buckholtz required: "
            "(1) Is beta_q = 0.19 or (1×4)/(3×7) ≈ 0.1905? "
            "(2) Derivation formula or fitting procedure? "
            "(3) Relationship to beta_q_1 = 8.10?"
        ),
    ),
    # MANUALLY VERIFIED: preprints202511.0598.v6.pdf, Appendix A.3, Table A1
    "beta_d_A1": BetaProvenance(
        beta_name="beta_d_A1",
        value=4.5,
        source_type="manuscript_appendix_table_A1",
        first_known_appearance="preprints202511.0598.v6.pdf, Appendix A.3, Table A1",
        provenance_status="manuscript_reported_fitted",
        use_permission_status="allowed_for_fit_reproduction_only",
        evidence_trail=(
            "✅ MANUALLY VERIFIED (2026-05-27): preprints202511.0598.v6.pdf, Appendix A.3, Table A1. "
            "Exact quote: 'Regarding H-MULT, the online service reported choosing beta_d = 4.5 and beta_q = 18.0.' "
            "Context: AI-assisted thought experiment. LLM was instructed to choose positive beta_d and beta_q values "
            "that minimize standard-deviations away from observed H(z). "
            "⚠️ FITTED phenomenological parameters (NOT derived theoretical constants). "
            "No uncertainty intervals provided. Quality of fit reported through sigma_MULT. "
            "Beta values are dimensionless scaling factors (e.g., r_dA = beta_d * r_A). "
            "Dataset: observed H(z) data with uncertainties."
        ),
        recommended_action=(
            "**FIT REPRODUCTION ONLY:** "
            "(1) Can reproduce the fit on same dataset used by Buckholtz. "
            "(2) CANNOT use to 'predict' H(z) on new data (circular reasoning — fitted to H(z)). "
            "(3) Can compare fit quality with ΛCDM on DIFFERENT dataset (test set). "
            "(4) Document: 'Beta values fitted to H(z) observations, not theoretically derived.' "
            "(5) See docs/18_fit_reproduction_requirements.md for implementation spec."
        ),
        manual_verification_status="manually_verified",
        derivation_status="fitted_not_derived",
        manuscript_identifier="preprints202511.0598.v6.pdf",
    ),
    "beta_q_A1": BetaProvenance(
        beta_name="beta_q_A1",
        value=18.0,
        source_type="manuscript_appendix_table_A1",
        first_known_appearance="preprints202511.0598.v6.pdf, Appendix A.3, Table A1",
        provenance_status="manuscript_reported_fitted",
        use_permission_status="allowed_for_fit_reproduction_only",
        evidence_trail=(
            "✅ MANUALLY VERIFIED (2026-05-27): preprints202511.0598.v6.pdf, Appendix A.3, Table A1. "
            "Exact quote: 'Regarding H-MULT, the online service reported choosing beta_d = 4.5 and beta_q = 18.0.' "
            "Context: AI-assisted thought experiment. LLM was instructed to choose positive beta_d and beta_q values "
            "that minimize standard-deviations away from observed H(z). "
            "⚠️ FITTED phenomenological parameters (NOT derived theoretical constants). "
            "No uncertainty intervals provided. Quality of fit reported through sigma_MULT. "
            "Beta values are dimensionless scaling factors (e.g., r_dA = beta_d * r_A). "
            "Dataset: observed H(z) data with uncertainties."
        ),
        recommended_action=(
            "**FIT REPRODUCTION ONLY:** "
            "(1) Can reproduce the fit on same dataset used by Buckholtz. "
            "(2) CANNOT use to 'predict' H(z) on new data (circular reasoning — fitted to H(z)). "
            "(3) Can compare fit quality with ΛCDM on DIFFERENT dataset (test set). "
            "(4) Document: 'Beta values fitted to H(z) observations, not theoretically derived.' "
            "(5) See docs/18_fit_reproduction_requirements.md for implementation spec."
        ),
        manual_verification_status="manually_verified",
        derivation_status="fitted_not_derived",
        manuscript_identifier="preprints202511.0598.v6.pdf",
    ),
}


def get_beta_provenance(beta_name: str) -> BetaProvenance:
    """
    Get provenance record for a beta candidate.

    Raises KeyError if beta_name not in registry.
    """
    return BETA_PROVENANCE_REGISTRY[beta_name]


def is_allowed_for_modeling(beta_name: str) -> bool:
    """
    Check if beta value is allowed for H(z) modeling.

    Returns True only if use_permission_status == "source_confirmed".
    """
    provenance = get_beta_provenance(beta_name)
    return provenance.use_permission_status == "source_confirmed"


def get_all_beta_names() -> list[str]:
    """Return list of all beta candidate names in registry."""
    return list(BETA_PROVENANCE_REGISTRY.keys())


def get_source_confirmed_betas() -> list[str]:
    """Return list of beta names with confirmed sources (allowed for modeling)."""
    return [
        name
        for name, prov in BETA_PROVENANCE_REGISTRY.items()
        if prov.use_permission_status == "source_confirmed"
    ]


def get_audit_reconstruction_betas() -> list[str]:
    """Return list of beta names that are audit reconstructions (NOT Buckholtz stated)."""
    return [
        name
        for name, prov in BETA_PROVENANCE_REGISTRY.items()
        if prov.provenance_status == "audit_reconstruction"
    ]


def get_source_missing_betas() -> list[str]:
    """Return list of beta names with no known source."""
    return [
        name
        for name, prov in BETA_PROVENANCE_REGISTRY.items()
        if prov.provenance_status == "source_missing"
    ]


def get_pending_verification_betas() -> list[str]:
    """Return list of beta names pending manual verification (NotebookLM candidates)."""
    return [
        name
        for name, prov in BETA_PROVENANCE_REGISTRY.items()
        if prov.provenance_status == "source_candidate_pending_manual_verification"
    ]


def get_manuscript_reported_fitted_betas() -> list[str]:
    """Return list of beta names reported in manuscript as fitted values."""
    return [
        name
        for name, prov in BETA_PROVENANCE_REGISTRY.items()
        if prov.provenance_status == "manuscript_reported_fitted"
    ]


def count_by_provenance_status() -> dict[str, int]:
    """Count beta values by provenance status."""
    counts: dict[str, int] = {}
    for prov in BETA_PROVENANCE_REGISTRY.values():
        status = prov.provenance_status
        counts[status] = counts.get(status, 0) + 1
    return counts


def count_by_use_permission() -> dict[str, int]:
    """Count beta values by use permission status."""
    counts: dict[str, int] = {}
    for prov in BETA_PROVENANCE_REGISTRY.values():
        status = prov.use_permission_status
        counts[status] = counts.get(status, 0) + 1
    return counts


def h_z_modeling_blocked() -> bool:
    """
    Check if H(z) modeling is blocked due to beta provenance issues.

    Returns True if ANY beta value lacks source confirmation.
    """
    return len(get_source_confirmed_betas()) == 0


def get_blocking_summary() -> str:
    """
    Return human-readable summary of H(z) modeling blocker status.
    """
    source_confirmed = get_source_confirmed_betas()
    audit_recon = get_audit_reconstruction_betas()
    source_missing = get_source_missing_betas()
    pending_verification = get_pending_verification_betas()
    total_betas = len(BETA_PROVENANCE_REGISTRY)

    if len(source_confirmed) == total_betas:
        return "✅ All beta values have confirmed sources. H(z) modeling ALLOWED."

    blocker_lines = [
        "❌ H(z) modeling BLOCKED — beta provenance issues:",
        f"  • Source confirmed: {len(source_confirmed)}/{total_betas}",
        f"  • Audit reconstructions: {len(audit_recon)}/{total_betas} (circular reasoning risk)",
        f"  • Source missing: {len(source_missing)}/{total_betas} (cannot verify or derive)",
        f"  • Pending manual verification: {len(pending_verification)}/{total_betas} (NotebookLM candidates)",
    ]

    if audit_recon:
        blocker_lines.append(
            f"  • Audit reconstruction betas: {', '.join(audit_recon)} "
            "(using these = testing OUR inference, not Buckholtz's model)"
        )

    if source_missing:
        blocker_lines.append(
            f"  • Source missing betas: {', '.join(source_missing)} "
            "(no provenance — highest priority for clarification)"
        )

    if pending_verification:
        blocker_lines.append(
            f"  • Pending verification: {', '.join(pending_verification)} "
            "(NotebookLM reports beta_d=4.5, beta_q=18.0 in Appendix/Table A1 — REQUIRES MANUAL CHECK)"
        )

    blocker_lines.append(
        "\n**Action required:** Manual verification of Appendix/Table A1 OR explicit beta values from Buckholtz."
    )

    return "\n".join(blocker_lines)
