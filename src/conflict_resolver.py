"""Conflict Resolver — Decision Logic for Conflicting Values

PURPOSE:
When multiple values exist for same symbol (e.g., beta_d = 4.5 vs 4.25),
provide structured decision logic to:
1. Detect conflicts automatically
2. Classify conflict severity (minor vs major)
3. Recommend resolution strategy
4. Block silent mixing of incompatible values

DESIGN:
- ConflictReport: structured conflict diagnosis
- ConflictResolver: decision engine for resolving conflicts
- Resolution strategies: prefer_authoritative, prefer_fitted, require_clarification

INTEGRATION:
- Used by computational modules before using any parameter value
- Enforces "no silent mixing" rule
"""

import logging
from dataclasses import dataclass
from enum import Enum

from src.source_provenance import (
    DerivationStatus,
    ProvenanceRegistry,
    ProvenanceTag,
    SourceType,
)

logger = logging.getLogger(__name__)


class ConflictSeverity(Enum):
    """How severe is this conflict?"""

    NONE = "none"  # No conflict (single value or within tolerance)
    MINOR = "minor"  # Multiple values within 5% (rounding/precision)
    MODERATE = "moderate"  # Values differ 5-20% (different sources)
    MAJOR = "major"  # Values differ >20% (fundamental disagreement)
    CRITICAL = "critical"  # Incompatible sources (fitted vs derived)


class ResolutionStrategy(Enum):
    """How should this conflict be resolved?"""

    PREFER_AUTHORITATIVE = "prefer_authoritative"  # Manuscript > audit
    PREFER_FITTED = "prefer_fitted"  # Fitted > derived (for phenomenological params)
    PREFER_DERIVED = "prefer_derived"  # Derived > fitted (for theoretical constants)
    REQUIRE_CLARIFICATION = "require_clarification"  # Block until author clarifies
    BLOCK_ALL_USE = "block_all_use"  # Too ambiguous, cannot proceed
    USER_DECISION = "user_decision"  # Escalate to user


@dataclass
class ConflictReport:
    """Structured diagnosis of a value conflict.

    Contains:
    - All conflicting tags
    - Severity assessment
    - Recommended resolution strategy
    - Safe and unsafe wordings
    """

    symbol: str
    conflicting_tags: list[ProvenanceTag]
    severity: ConflictSeverity
    recommended_strategy: ResolutionStrategy
    safe_wording: str
    unsafe_wording: list[str]
    resolution_notes: str

    def to_dict(self) -> dict:
        """Export conflict report to dictionary."""
        return {
            "symbol": self.symbol,
            "severity": self.severity.value,
            "recommended_strategy": self.recommended_strategy.value,
            "conflicting_values": [tag.to_dict() for tag in self.conflicting_tags],
            "safe_wording": self.safe_wording,
            "unsafe_wording": self.unsafe_wording,
            "resolution_notes": self.resolution_notes,
        }


class ConflictResolver:
    """Decision engine for resolving value conflicts.

    Responsibilities:
    - Detect conflicts in ProvenanceRegistry
    - Classify conflict severity
    - Recommend resolution strategy
    - Generate safe/unsafe wording templates
    """

    def __init__(self, registry: ProvenanceRegistry):
        self.registry = registry

    def diagnose(self, symbol: str) -> ConflictReport | None:
        """Diagnose conflict for given symbol.

        Returns:
            ConflictReport if conflict exists, None otherwise
        """
        tags = self.registry.get_all_values(symbol)

        if len(tags) <= 1:
            return None  # No conflict

        if not self.registry.has_conflict(symbol):
            return None  # Values within tolerance

        # Assess severity
        severity = self._assess_severity(tags)

        # Recommend strategy
        strategy = self._recommend_strategy(tags, severity)

        # Generate wording templates
        safe_wording, unsafe_wording = self._generate_wording(symbol, tags, severity)

        # Generate resolution notes
        notes = self._generate_notes(symbol, tags, severity, strategy)

        return ConflictReport(
            symbol=symbol,
            conflicting_tags=tags,
            severity=severity,
            recommended_strategy=strategy,
            safe_wording=safe_wording,
            unsafe_wording=unsafe_wording,
            resolution_notes=notes,
        )

    def _assess_severity(self, tags: list[ProvenanceTag]) -> ConflictSeverity:
        """Assess conflict severity based on value spread and source types."""
        values = [tag.value for tag in tags]
        mean_value = sum(values) / len(values)
        value_range = max(values) - min(values)

        # Relative spread
        rel_spread = value_range / abs(mean_value) if mean_value != 0 else 0

        # Check for incompatible sources
        has_fitted = any(tag.derivation_status == DerivationStatus.FITTED for tag in tags)
        has_derived = any(tag.derivation_status == DerivationStatus.DERIVED for tag in tags)

        if has_fitted and has_derived:
            return ConflictSeverity.CRITICAL  # Fitted vs derived conflict

        # Numerical spread classification
        if rel_spread < 0.05:
            return ConflictSeverity.MINOR
        elif rel_spread < 0.20:
            return ConflictSeverity.MODERATE
        else:
            return ConflictSeverity.MAJOR

    def _recommend_strategy(
        self, tags: list[ProvenanceTag], severity: ConflictSeverity
    ) -> ResolutionStrategy:
        """Recommend resolution strategy based on tags and severity."""

        # CRITICAL conflicts: block until clarification
        if severity == ConflictSeverity.CRITICAL:
            return ResolutionStrategy.REQUIRE_CLARIFICATION

        # Check if we have authoritative (manuscript) values
        authoritative_tags = [tag for tag in tags if tag.is_authoritative()]

        if authoritative_tags:
            # Multiple manuscript values → author clarification needed
            if len(authoritative_tags) > 1:
                return ResolutionStrategy.REQUIRE_CLARIFICATION
            # One manuscript value → prefer it
            else:
                return ResolutionStrategy.PREFER_AUTHORITATIVE

        # No authoritative values → check derivation status
        fitted_tags = [tag for tag in tags if tag.derivation_status == DerivationStatus.FITTED]
        derived_tags = [tag for tag in tags if tag.derivation_status == DerivationStatus.DERIVED]

        # If we have fitted values (phenomenological params), prefer those
        if fitted_tags and not derived_tags:
            return ResolutionStrategy.PREFER_FITTED

        # If we have derived values (theoretical constants), prefer those
        if derived_tags and not fitted_tags:
            return ResolutionStrategy.PREFER_DERIVED

        # Mixed or unclear → require clarification
        if severity in (ConflictSeverity.MODERATE, ConflictSeverity.MAJOR):
            return ResolutionStrategy.REQUIRE_CLARIFICATION

        # MINOR conflicts → user decision
        return ResolutionStrategy.USER_DECISION

    def _generate_wording(
        self, symbol: str, tags: list[ProvenanceTag], severity: ConflictSeverity
    ) -> tuple[str, list[str]]:
        """Generate safe and unsafe wording templates for this conflict."""

        values_str = ", ".join(f"{tag.value:.4f} ({tag.source_type.value})" for tag in tags)

        # Safe wording
        safe = (
            f"Multiple values for {symbol} exist in source materials: {values_str}. "
            f"Conflict severity: {severity.value}. "
            "Values cannot be mixed silently. Clarification required before computational use."
        )

        # Unsafe wording examples (what NOT to say)
        unsafe = [
            f"Using {symbol} = {tags[0].value:.4f} (silent choice without justification)",
            f"{symbol} is well-defined (ignoring conflict)",
            f"Averaging conflicting values: {symbol} = {sum(t.value for t in tags) / len(tags):.4f}",
            "Conflict resolved (without specifying how)",
        ]

        return safe, unsafe

    def _generate_notes(
        self,
        symbol: str,
        tags: list[ProvenanceTag],
        severity: ConflictSeverity,
        strategy: ResolutionStrategy,
    ) -> str:
        """Generate resolution notes explaining conflict and recommended action."""

        notes = [f"Conflict detected for {symbol}:"]

        for tag in tags:
            notes.append(
                f"  • {tag.value:.4f} from {tag.source_type.value} "
                f"({tag.derivation_status.value}, {tag.use_permission.value})"
            )

        notes.append(f"\nSeverity: {severity.value}")
        notes.append(f"Recommended strategy: {strategy.value}")

        if strategy == ResolutionStrategy.REQUIRE_CLARIFICATION:
            notes.append(
                "\nAction: Send clarification request to author. "
                "Block computational use until resolved."
            )
        elif strategy == ResolutionStrategy.PREFER_AUTHORITATIVE:
            auth_tag = [tag for tag in tags if tag.is_authoritative()][0]
            notes.append(
                f"\nAction: Prefer authoritative value {auth_tag.value:.4f} "
                f"from {auth_tag.source_type.value}. "
                "Document choice explicitly in code and reports."
            )
        elif strategy == ResolutionStrategy.PREFER_FITTED:
            fitted_tag = [tag for tag in tags if tag.derivation_status == DerivationStatus.FITTED][
                0
            ]
            notes.append(
                f"\nAction: Prefer fitted value {fitted_tag.value:.4f}. "
                "Document choice and circular reasoning guard."
            )
        elif strategy == ResolutionStrategy.USER_DECISION:
            notes.append("\nAction: Minor conflict — present options to user and document choice.")

        return "\n".join(notes)

    def resolve(self, symbol: str, use_case: str = "fit_reproduction") -> ProvenanceTag | None:
        """Resolve conflict and return canonical tag for given use case.

        Returns:
            ProvenanceTag if resolvable, None if blocked

        Raises:
            ValueError: If conflict requires clarification or user decision
        """
        report = self.diagnose(symbol)

        if report is None:
            # No conflict — use registry's canonical
            return self.registry.get_canonical(symbol, use_case)

        # Check if conflict blocks use
        if report.recommended_strategy == ResolutionStrategy.REQUIRE_CLARIFICATION:
            raise ValueError(
                f"Conflict for {symbol} requires author clarification before use. "
                f"Severity: {report.severity.value}. "
                f"See docs/27_source_conflict_log.md for details."
            )

        if report.recommended_strategy == ResolutionStrategy.BLOCK_ALL_USE:
            raise ValueError(
                f"Conflict for {symbol} too severe — all use blocked. "
                f"Severity: {report.severity.value}."
            )

        if report.recommended_strategy == ResolutionStrategy.USER_DECISION:
            raise ValueError(
                f"Conflict for {symbol} requires user decision. "
                f"Multiple valid values available — explicit choice needed."
            )

        # Apply resolution strategy
        if report.recommended_strategy == ResolutionStrategy.PREFER_AUTHORITATIVE:
            canonical = self.registry.get_canonical(
                symbol, use_case, prefer_source=SourceType.MANUSCRIPT_TABLE
            )
            if canonical:
                logger.info(
                    f"Resolved {symbol} conflict: preferring authoritative value "
                    f"{canonical.value:.4f} from {canonical.source_type.value}"
                )
                return canonical

        if report.recommended_strategy == ResolutionStrategy.PREFER_FITTED:
            fitted_tags = [
                tag
                for tag in report.conflicting_tags
                if tag.derivation_status == DerivationStatus.FITTED
            ]
            if fitted_tags:
                logger.info(
                    f"Resolved {symbol} conflict: preferring fitted value "
                    f"{fitted_tags[0].value:.4f}"
                )
                return fitted_tags[0]

        if report.recommended_strategy == ResolutionStrategy.PREFER_DERIVED:
            derived_tags = [
                tag
                for tag in report.conflicting_tags
                if tag.derivation_status == DerivationStatus.DERIVED
            ]
            if derived_tags:
                logger.info(
                    f"Resolved {symbol} conflict: preferring derived value "
                    f"{derived_tags[0].value:.4f}"
                )
                return derived_tags[0]

        # Fallback: cannot resolve
        raise ValueError(
            f"Cannot resolve conflict for {symbol} with strategy "
            f"{report.recommended_strategy.value}"
        )

    def export_all_conflicts(self) -> list[ConflictReport]:
        """Export conflict reports for all symbols with conflicts."""
        reports = []

        for symbol in self.registry.list_symbols():
            report = self.diagnose(symbol)
            if report:
                reports.append(report)

        return reports
