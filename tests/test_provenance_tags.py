"""Tests for Provenance Tagging System

PURPOSE:
Verify that ProvenanceTag and ProvenanceRegistry correctly:
1. Store source information for each value
2. Track derivation status and use permissions
3. Index values by symbol
4. Generate unique tag IDs
5. Export to dict for serialization
6. Enforce "no silent mixing" via use permissions

CRITICAL:
These tests ensure values cannot be used computationally without
explicit provenance tracking and use permission checks.
"""

from datetime import date

import pytest

from src.source_provenance import (
    DerivationStatus,
    ProvenanceRegistry,
    ProvenanceTag,
    SourceType,
    UsePermission,
    get_registry,
    register_value,
)


class TestProvenanceTag:
    """Test ProvenanceTag dataclass."""

    def test_tag_creation_minimal(self):
        """Create tag with minimal required fields."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
        )

        assert tag.symbol == "beta_d"
        assert tag.value == 4.5
        assert tag.source_type == SourceType.MANUSCRIPT_TABLE
        assert tag.derivation_status == DerivationStatus.UNKNOWN  # Default
        assert tag.use_permission == UsePermission.REQUIRES_CLARIFICATION  # Default

    def test_tag_creation_full(self):
        """Create tag with all fields specified."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            manuscript_identifier="preprints202511.0598.v6.pdf",
            location="Appendix A.3, Table A1",
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
            verification_date=date(2026, 5, 27),
            verified_by="manual_verification",
            notes="AI-assisted thought experiment",
            uncertainty=None,
            units="dimensionless",
        )

        assert tag.manuscript_identifier == "preprints202511.0598.v6.pdf"
        assert tag.location == "Appendix A.3, Table A1"
        assert tag.derivation_status == DerivationStatus.FITTED
        assert tag.use_permission == UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY
        assert tag.verification_date == date(2026, 5, 27)
        assert tag.verified_by == "manual_verification"
        assert tag.notes == "AI-assisted thought experiment"
        assert tag.units == "dimensionless"

    def test_tag_id_generation(self):
        """Tag ID uniquely identifies value."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
        )

        # Format: {symbol}_{source_abbrev}_{value:.4f}
        assert tag.tag_id == "beta_d_MT_4.5000"

    def test_tag_id_different_sources(self):
        """Different sources generate different tag IDs."""
        tag1 = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
        )
        tag2 = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
        )

        assert tag1.tag_id == "beta_d_MT_4.5000"
        assert tag2.tag_id == "beta_d_AR_4.5000"
        assert tag1.tag_id != tag2.tag_id

    def test_tag_is_authoritative_manuscript(self):
        """Manuscript sources are authoritative."""
        tag_table = ProvenanceTag(
            symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TABLE
        )
        tag_text = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TEXT)
        tag_equation = ProvenanceTag(
            symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_EQUATION
        )

        assert tag_table.is_authoritative()
        assert tag_text.is_authoritative()
        assert tag_equation.is_authoritative()

    def test_tag_is_not_authoritative_audit(self):
        """Audit/AI sources are NOT authoritative."""
        tag_audit = ProvenanceTag(
            symbol="beta_d", value=4.5, source_type=SourceType.AUDIT_RECONSTRUCTION
        )
        tag_ai = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.AI_TRANSCRIPT)

        assert not tag_audit.is_authoritative()
        assert not tag_ai.is_authoritative()

    def test_tag_allows_computation_fit_reproduction(self):
        """Check use permission for fit reproduction."""
        tag_allowed = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )
        tag_blocked = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            use_permission=UsePermission.DO_NOT_USE,
        )

        assert tag_allowed.allows_computation("fit_reproduction")
        assert not tag_blocked.allows_computation("fit_reproduction")

    def test_tag_allows_computation_prediction(self):
        """Check use permission for prediction."""
        tag_fit_only = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )
        tag_prediction_allowed = ProvenanceTag(
            symbol="H0",
            value=67.4,
            source_type=SourceType.EXTERNAL_REFERENCE,
            use_permission=UsePermission.ALLOWED_FOR_PREDICTION,
        )

        # Fit-only tag cannot be used for prediction
        assert not tag_fit_only.allows_computation("prediction")

        # Prediction-allowed tag CAN be used for prediction
        assert tag_prediction_allowed.allows_computation("prediction")

    def test_tag_to_dict_export(self):
        """Export tag to dict for serialization."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
            manuscript_identifier="preprints202511.0598.v6.pdf",
            verification_date=date(2026, 5, 27),
        )

        d = tag.to_dict()

        assert d["symbol"] == "beta_d"
        assert d["value"] == 4.5
        assert d["source_type"] == "manuscript_table"
        assert d["derivation_status"] == "fitted"
        assert d["use_permission"] == "allowed_for_fit_reproduction_only"
        assert d["manuscript_identifier"] == "preprints202511.0598.v6.pdf"
        assert d["verification_date"] == "2026-05-27"


class TestProvenanceRegistry:
    """Test ProvenanceRegistry operations."""

    @pytest.fixture
    def registry(self):
        """Create fresh registry for each test."""
        return ProvenanceRegistry()

    def test_register_single_tag(self, registry):
        """Register single tag."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
        )

        registry.register(tag)

        assert "beta_d" in registry.list_symbols()
        tags = registry.get_all_values("beta_d")
        assert len(tags) == 1
        assert tags[0].value == 4.5

    def test_register_duplicate_tag_skipped(self, registry):
        """Registering same tag twice → skip second."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
        )

        registry.register(tag)
        registry.register(tag)  # Duplicate

        # Should have only 1 tag (duplicate skipped)
        tags = registry.get_all_values("beta_d")
        assert len(tags) == 1

    def test_register_multiple_values_same_symbol(self, registry):
        """Register multiple values for same symbol."""
        tag1 = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
        )
        tag2 = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
        )

        registry.register(tag1)
        registry.register(tag2)

        tags = registry.get_all_values("beta_d")
        assert len(tags) == 2
        values = {tag.value for tag in tags}
        assert values == {4.5, 4.25}

    def test_has_conflict_true(self, registry):
        """Detect conflict when values differ >1%."""
        tag1 = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TABLE)
        tag2 = ProvenanceTag(
            symbol="beta_d", value=4.25, source_type=SourceType.AUDIT_RECONSTRUCTION
        )

        registry.register(tag1)
        registry.register(tag2)

        # 5.9% difference → conflict
        assert registry.has_conflict("beta_d")

    def test_has_conflict_false_within_tolerance(self, registry):
        """No conflict when values within 1% tolerance."""
        tag1 = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TABLE)
        tag2 = ProvenanceTag(
            symbol="beta_d", value=4.501, source_type=SourceType.AUDIT_RECONSTRUCTION
        )

        registry.register(tag1)
        registry.register(tag2)

        # 0.02% difference → within tolerance
        assert not registry.has_conflict("beta_d")

    def test_get_canonical_single_value(self, registry):
        """Get canonical when only one value exists."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )

        registry.register(tag)

        canonical = registry.get_canonical("beta_d", use_case="fit_reproduction")
        assert canonical.value == 4.5

    def test_get_canonical_prefers_manuscript(self, registry):
        """Get canonical prefers manuscript over audit."""
        tag_manuscript = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )
        tag_audit = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )

        # Register in reverse order (audit first)
        registry.register(tag_audit)
        registry.register(tag_manuscript)

        # Should still prefer manuscript
        canonical = registry.get_canonical("beta_d", use_case="fit_reproduction")
        assert canonical.value == 4.5
        assert canonical.source_type == SourceType.MANUSCRIPT_TABLE

    def test_get_canonical_respects_use_permission(self, registry):
        """Get canonical returns None if use permission incompatible."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )

        registry.register(tag)

        # use_case = "prediction" but permission = "fit_reproduction_only"
        canonical = registry.get_canonical("beta_d", use_case="prediction")
        assert canonical is None

    def test_get_canonical_prefer_source_override(self, registry):
        """get_canonical can override precedence with prefer_source."""
        tag_manuscript = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )
        tag_audit = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            use_permission=UsePermission.ALLOWED_FOR_TOY_MODELING,
        )

        registry.register(tag_manuscript)
        registry.register(tag_audit)

        # Override: prefer audit (for toy modeling)
        canonical = registry.get_canonical(
            "beta_d", use_case="toy_modeling", prefer_source=SourceType.AUDIT_RECONSTRUCTION
        )

        assert canonical.value == 4.25
        assert canonical.source_type == SourceType.AUDIT_RECONSTRUCTION

    def test_export_conflict_summary(self, registry):
        """Export conflicts as dict for logging."""
        tag1 = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TABLE)
        tag2 = ProvenanceTag(
            symbol="beta_d", value=4.25, source_type=SourceType.AUDIT_RECONSTRUCTION
        )
        tag3 = ProvenanceTag(symbol="beta_q", value=18.0, source_type=SourceType.MANUSCRIPT_TABLE)

        registry.register(tag1)
        registry.register(tag2)
        registry.register(tag3)  # No conflict (single value)

        conflicts = registry.export_conflict_summary()

        # Should have 1 symbol with conflict
        assert len(conflicts) == 1
        assert "beta_d" in conflicts
        assert "beta_q" not in conflicts  # No conflict

        # Conflict should list both values
        assert len(conflicts["beta_d"]) == 2

    def test_count_conflicts(self, registry):
        """Count total symbols with conflicts."""
        tag1 = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TABLE)
        tag2 = ProvenanceTag(
            symbol="beta_d", value=4.25, source_type=SourceType.AUDIT_RECONSTRUCTION
        )
        tag3 = ProvenanceTag(symbol="beta_q", value=18.0, source_type=SourceType.MANUSCRIPT_TABLE)
        tag4 = ProvenanceTag(
            symbol="beta_q", value=8.10, source_type=SourceType.AUDIT_RECONSTRUCTION
        )

        registry.register(tag1)
        registry.register(tag2)
        registry.register(tag3)
        registry.register(tag4)

        # 2 symbols with conflicts
        assert registry.count_conflicts() == 2


class TestRegisterValueHelper:
    """Test convenience function register_value()."""

    def test_register_value_creates_and_registers_tag(self):
        """register_value() creates tag and adds to global registry."""
        # Note: get_registry() returns global singleton, cannot clear in tests

        tag = register_value(
            symbol="test_param",
            value=42.0,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_PREDICTION,
            notes="Test parameter",
        )

        # Tag created
        assert tag.symbol == "test_param"
        assert tag.value == 42.0
        assert tag.notes == "Test parameter"

        # Tag registered in global registry
        global_registry = get_registry()
        tags = global_registry.get_all_values("test_param")
        assert len(tags) >= 1  # May have tags from other tests
        assert any(t.value == 42.0 for t in tags)


class TestRealWorldUsage:
    """Test real-world usage patterns from Buckholtz audit."""

    def test_beta_d_manuscript_vs_audit(self):
        """Register beta_d from manuscript and audit sources."""
        registry = ProvenanceRegistry()

        # Manuscript value (authoritative)
        tag_manuscript = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
            manuscript_identifier="preprints202511.0598.v6.pdf",
            location="Appendix A.3, Table A1",
            verification_date=date(2026, 5, 27),
            notes="AI-assisted thought experiment, fitted to H(z)",
        )

        # Audit reconstruction (not authoritative)
        tag_audit = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            derivation_status=DerivationStatus.RECONSTRUCTED,
            use_permission=UsePermission.DO_NOT_USE,
            location="docs/13_internal_anchor_uniqueness.md",
            notes="beta_d_1 = 17/4, NOT confirmed by Buckholtz, 7 alternatives",
        )

        registry.register(tag_manuscript)
        registry.register(tag_audit)

        # Has conflict
        assert registry.has_conflict("beta_d")

        # Canonical prefers manuscript
        canonical = registry.get_canonical("beta_d", use_case="fit_reproduction")
        assert canonical.value == 4.5
        assert canonical.is_authoritative()

        # Audit value is blocked (DO_NOT_USE)
        # get_canonical filters by use_permission FIRST, then applies prefer_source
        # Since tag_audit has DO_NOT_USE, it should not appear in allowed_tags list
        # Therefore prefer_source=AUDIT_RECONSTRUCTION should return None (no allowed audit tag)
        # OR return manuscript tag (fallback to next available)
        audit_canonical = registry.get_canonical(
            "beta_d", use_case="fit_reproduction", prefer_source=SourceType.AUDIT_RECONSTRUCTION
        )

        # Current implementation: prefer_source is checked AFTER filtering by use_permission
        # audit tag has DO_NOT_USE → filtered out → prefer_source finds nothing → fallback to manuscript
        # So audit_canonical will be the manuscript tag (4.5), not the audit tag (4.25)
        if audit_canonical is not None:
            # Should be manuscript tag (fallback), not audit tag
            assert audit_canonical.value == 4.5
            assert audit_canonical.source_type == SourceType.MANUSCRIPT_TABLE

    def test_multiple_use_cases_same_parameter(self):
        """Same parameter may have different permissions for different use cases."""
        registry = ProvenanceRegistry()

        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )

        registry.register(tag)

        # Allowed for fit reproduction
        fit_canonical = registry.get_canonical("beta_d", use_case="fit_reproduction")
        assert fit_canonical is not None
        assert fit_canonical.value == 4.5

        # Blocked for prediction (fitted value, circular reasoning)
        pred_canonical = registry.get_canonical("beta_d", use_case="prediction")
        assert pred_canonical is None  # Blocked

    def test_source_missing_parameter(self):
        """Parameter mentioned but not defined → no tags registered."""
        registry = ProvenanceRegistry()

        # H_MULT formula not provided → no registration
        tags = registry.get_all_values("H_MULT_formula")
        assert len(tags) == 0

        # get_canonical returns None
        canonical = registry.get_canonical("H_MULT_formula")
        assert canonical is None
