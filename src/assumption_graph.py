"""
Assumption dependency graph.

Purpose: Track which claims depend on which assumptions.
         Identify hidden degrees of freedom and circular dependencies.
"""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class Dependency:
    """A dependency relationship between claims/parameters."""

    parent: str  # What depends on something
    child: str  # What it depends on
    relation: str  # How they relate
    risk: Literal["low", "medium", "high"]  # Risk if child is wrong


# Define dependency structure
DEPENDENCIES = [
    # H(z) fit dependencies
    Dependency(
        parent="H(z) fit", child="beta_d", relation="H(z) fit requires beta_d value", risk="high"
    ),
    Dependency(
        parent="H(z) fit", child="beta_q", relation="H(z) fit requires beta_q value", risk="high"
    ),
    Dependency(
        parent="H(z) fit",
        child="cluster radius definition",
        relation="Cluster radius needed for scale interpretation",
        risk="medium",
    ),
    Dependency(
        parent="H(z) fit",
        child="sub-object kinetic energy definition",
        relation="Kinetic energy definition affects multipole terms",
        risk="medium",
    ),
    Dependency(
        parent="H(z) fit",
        child="dataset choice",
        relation="Different datasets (Pantheon, cosmic chronometers) may give different results",
        risk="medium",
    ),
    # Beta_d dependencies
    Dependency(
        parent="beta_d",
        child="r_A definition",
        relation="If beta_d = r_dA / r_A, then beta_d depends on r_A definition",
        risk="high",
    ),
    Dependency(
        parent="beta_d",
        child="beta_d normalization choice",
        relation="Different normalizations may explain different candidate values",
        risk="high",
    ),
    # Beta_q dependencies
    Dependency(
        parent="beta_q",
        child="length scale L_ref",
        relation="If beta_q relates to L_q^2, needs reference length",
        risk="high",
    ),
    Dependency(
        parent="beta_q",
        child="beta_q normalization choice",
        relation="Different normalizations may explain different candidate values",
        risk="high",
    ),
    # Eq.15 dependencies
    Dependency(
        parent="Eq.15 relation",
        child="exponent 6 mechanism",
        relation="Physical reason for (m_tau/m_e)^12 term unclear",
        risk="high",
    ),
    Dependency(
        parent="Eq.15 relation",
        child="prefactor 4/3 mechanism",
        relation="Physical reason for 4/3 unclear",
        risk="medium",
    ),
    # IDM dependencies
    Dependency(
        parent="6 isomers claim",
        child="isomer definition",
        relation="Need to define what 'isomer' means in this context",
        risk="high",
    ),
    Dependency(
        parent="6 isomers claim",
        child="5 dark / 1 ordinary ratio",
        relation="Ratio derived or assumed?",
        risk="high",
    ),
    # MULTING GR compatibility
    Dependency(
        parent="MULTING dipole term",
        child="PPN constraints",
        relation="Dipole term must not violate Solar System tests",
        risk="high",
    ),
    Dependency(
        parent="MULTING quadrupole term",
        child="PPN constraints",
        relation="Quadrupole term must not violate Solar System tests",
        risk="high",
    ),
]


def get_all_dependencies() -> list[Dependency]:
    """Return all registered dependencies."""
    return DEPENDENCIES


def get_dependencies(node: str) -> list[Dependency]:
    """
    Get all dependencies where node is the parent.

    Args:
        node: Name of the parent node

    Returns:
        List of dependencies where this node depends on something
    """
    return [dep for dep in DEPENDENCIES if dep.parent == node]


def get_reverse_dependencies(node: str) -> list[Dependency]:
    """
    Get all dependencies where node is the child.

    Args:
        node: Name of the child node

    Returns:
        List of dependencies where something depends on this node
    """
    return [dep for dep in DEPENDENCIES if dep.child == node]


def get_high_risk_dependencies() -> list[Dependency]:
    """Get all high-risk dependencies."""
    return [dep for dep in DEPENDENCIES if dep.risk == "high"]


def check_circular_dependency(node1: str, node2: str) -> bool:
    """
    Check if there's a circular dependency between two nodes.

    Args:
        node1: First node
        node2: Second node

    Returns:
        True if circular dependency detected
    """
    # Check if node1 depends on node2 AND node2 depends on node1
    node1_deps = {dep.child for dep in get_dependencies(node1)}
    node2_deps = {dep.child for dep in get_dependencies(node2)}

    return node2 in node1_deps and node1 in node2_deps


def get_dependency_chain(start_node: str, max_depth: int = 5) -> list[list[str]]:
    """
    Get all dependency chains starting from a node.

    Args:
        start_node: Starting node
        max_depth: Maximum chain depth to explore

    Returns:
        List of dependency chains (each chain is a list of node names)
    """
    chains = []

    def explore(current: str, chain: list[str], depth: int):
        if depth >= max_depth:
            chains.append(chain)
            return

        deps = get_dependencies(current)
        if not deps:
            chains.append(chain)
            return

        for dep in deps:
            child = dep.child
            if child in chain:  # Circular dependency detected
                chains.append(chain + [child, "CIRCULAR"])
            else:
                explore(child, chain + [child], depth + 1)

    explore(start_node, [start_node], 0)
    return chains
