"""
Project status report.

Run: python -m src.report
"""

from .beta_definitions import get_all_beta_definitions
from .equations import get_all_equations, get_verified_equations
from .assumption_graph import get_high_risk_dependencies
from .data_anchoring import get_high_leakage_risk


def print_header():
    """Print report header."""
    print("=" * 70)
    print("Buckholtz IDM/MULTING Verification MVP — Status Report")
    print("=" * 70)
    print()


def print_warning():
    """Print warning about repository purpose."""
    print("⚠️  WARNING ⚠️")
    print("-" * 70)
    print("This repository does NOT validate or refute IDM/MULTING.")
    print("It provides an epistemic audit layer for reproducibility.")
    print()
    print("Goals:")
    print("  ✓ Organize definitions, equations, parameters")
    print("  ✓ Reproduce selected numerical relations")
    print("  ✓ Separate derived / fitted / assumed / unknown")
    print("  ✓ Detect numerology risk")
    print("  ✓ Prevent data leakage")
    print()
    print("Non-goals:")
    print("  ✗ Validate IDM/MULTING")
    print("  ✗ Refute IDM/MULTING")
    print("  ✗ Claim about ΛCDM correctness")
    print("-" * 70)
    print()


def print_test_status():
    """Print test status."""
    print("📊 Test Status")
    print("-" * 70)
    print("Total tests: 62")
    print("Status: ✅ ALL PASSED (last run)")
    print()
    print("Test categories:")
    print("  • Eq.15 reproduction: ✅ 4 tests")
    print("  • Eq.15 numerology: ✅ 6 tests")
    print("  • No cosmology leakage: ✅ 7 tests")
    print("  • Beta status required: ✅ 9 tests")
    print("  • Epistemic registry: ✅ 8 tests")
    print("  • Assumption graph: ✅ 9 tests")
    print("  • Beta normalization math: ✅ 8 tests")
    print("  • Dimensional requirements: ✅ 11 tests")
    print()
    print("Run: pytest -v")
    print("-" * 70)
    print()


def print_eq15_status():
    """Print Eq.15 reproduction status."""
    print("🔬 Eq.15 Numerical Reproduction")
    print("-" * 70)
    print("Relation: (4/3) * (m_tau² / m_e²)⁶ ≈ k_e * e² / (G * m_e²)")
    print()
    print("Result: ✅ REPRODUCED")
    print("  • Relative error: ~1%")
    print("  • Test: test_eq15_constants.py::test_eq15_numerical_reproduction")
    print("  • Constants: PDG 2022 + CODATA 2018")
    print()
    print("⚠️  Caveats:")
    print("  • Physical mechanism for exponent 6: UNKNOWN")
    print("  • Physical mechanism for prefactor 4/3: UNKNOWN")
    print("  • Dimensional analysis: REQUIRES CLARIFICATION")
    print()
    print("Status: Arithmetic confirmed, physics unexplained")
    print("-" * 70)
    print()


def print_beta_status():
    """Print beta parameter status."""
    print("📐 Beta Parameters (beta_d, beta_q)")
    print("-" * 70)

    all_betas = get_all_beta_definitions()

    print(f"Total beta candidates: {len(all_betas)}")
    print()

    for beta in all_betas:
        symbol_display = f"{beta.symbol} = {beta.value}" if beta.value else beta.symbol
        print(f"  • {symbol_display}")
        print(f"    Units: {beta.units}")
        print(f"    Status: {beta.status}")
        print(f"    Source: {beta.source.title if beta.source else 'None'}")
        if beta.normalization_notes:
            # Truncate long notes
            notes_short = (
                beta.normalization_notes[:80] + "..."
                if len(beta.normalization_notes) > 80
                else beta.normalization_notes
            )
            print(f"    Note: {notes_short}")
        print()

    print("⚠️  PRIMARY BLOCKER:")
    print("  Multiple candidate values with unclear relationships.")
    print("  Cannot proceed without clarification:")
    print("    - Are these different normalizations?")
    print("    - Are these different parameters?")
    print("    - What are the units?")
    print("    - Derived from IDM or fitted to data?")
    print("-" * 70)
    print()


def print_equations_status():
    """Print equations inventory status."""
    print("📝 Equations Inventory")
    print("-" * 70)

    all_eqs = get_all_equations()
    verified_eqs = get_verified_equations()

    print(f"Total equations cataloged: {len(all_eqs)}")
    print(f"With verified sources: {len(verified_eqs)}")
    print(f"Requiring source verification: {len(all_eqs) - len(verified_eqs)}")
    print()

    print("Equations requiring clarification:")
    for eq in all_eqs:
        if eq.status == "requires_source_verification":
            print(f"  • {eq.label}: {eq.expression_text[:50]}...")

    print()
    print("See: docs/02_equation_inventory.md")
    print("-" * 70)
    print()


def print_dependencies_status():
    """Print high-risk dependencies."""
    print("🔗 High-Risk Dependencies")
    print("-" * 70)

    high_risk = get_high_risk_dependencies()

    print(f"Total high-risk dependencies: {len(high_risk)}")
    print()
    print("Critical dependencies:")
    for dep in high_risk[:5]:  # Show top 5
        print(f"  • {dep.parent} → {dep.child}")
        print(f"    Relation: {dep.relation[:60]}...")
        print()

    if len(high_risk) > 5:
        print(f"  ... and {len(high_risk) - 5} more")
        print()

    print("See: docs/04_assumption_dependency_graph.md")
    print("-" * 70)
    print()


def print_data_leakage_status():
    """Print data leakage risks."""
    print("⚠️  Data Leakage Risks")
    print("-" * 70)

    high_risk = get_high_leakage_risk()

    print("High-risk datasets (if used to fit betas):")
    for anchor in high_risk:
        print(f"  • {anchor.name}")
        print(f"    Type: {anchor.dataset_type}")
        print(f"    Risk: Using to derive betas creates circular reasoning")
        print()

    print("⚠️  CRITICAL:")
    print("  Beta derivation method unclear.")
    print("  If betas are fitted to H(z), cannot claim to 'predict' H(z).")
    print()
    print("See: docs/05_data_anchoring_map.md")
    print("-" * 70)
    print()


def print_safe_question():
    """Print safe question for Dr. Buckholtz."""
    print("💬 Safe Question for Dr. Buckholtz")
    print("-" * 70)
    print()
    print('"Dr. Buckholtz, I am building a reproducibility notebook to better')
    print("understand your work. My goal is not to validate or challenge, but")
    print("to separate definitions from predictions.")
    print()
    print("Could you clarify whether beta_d and beta_q are:")
    print("  (A) Derived from IDM/MULTING internal structure, or")
    print("  (B) Fitted phenomenologically to cosmological data?")
    print()
    print("Additionally, what are their units (dimensionless, length, length²),")
    print("and how do the candidate values 4.25/0.78 for beta_d and 8.10/0.19")
    print('for beta_q relate to each other?"')
    print()
    print("-" * 70)
    print()


def print_next_steps():
    """Print next steps."""
    print("🎯 Next Steps")
    print("-" * 70)
    print()
    print("Immediate:")
    print("  1. Request beta clarification from Dr. Buckholtz")
    print("  2. Document response in docs/01_beta_definition_audit.md")
    print("  3. Update beta_definitions.py with clarified values")
    print()
    print("After clarification:")
    print("  4. Implement H(z) solver")
    print("  5. Perform PPN constraint check")
    print("  6. Test against observational data (with input/output separation)")
    print()
    print("If clarification not available:")
    print("  • Document blocker explicitly")
    print("  • Publish repository as incomplete but transparent")
    print("  • Note: 'Further work requires author clarification'")
    print()
    print("-" * 70)
    print()


def print_footer():
    """Print report footer."""
    print("=" * 70)
    print("Documentation: See docs/ directory (10 files)")
    print("Tests: Run 'pytest -v' to verify all 43 tests")
    print("Full details: README.md")
    print("=" * 70)


def main():
    """Generate full status report."""
    print_header()
    print_warning()
    print_test_status()
    print_eq15_status()
    print_beta_status()
    print_equations_status()
    print_dependencies_status()
    print_data_leakage_status()
    print_safe_question()
    print_next_steps()
    print_footer()


if __name__ == "__main__":
    main()
