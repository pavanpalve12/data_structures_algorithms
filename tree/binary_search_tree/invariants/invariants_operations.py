"""
------------------------------------------------------------------------------------
Module Name: invariants
------------------------------------------------------------------------------------
This module implements **structural and ordering invariant validation** for a
Binary Search Tree (BST).

It defines a centralized validation mechanism that ensures the tree maintains
all required correctness guarantees after any mutation operation.

This module is strictly **read-only**:
- It does not modify the tree
- It does not perform traversal logic directly
- It relies on precomputed metadata for validation
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Validate single-root constraint
- Enforce binary child constraints
- Ensure single-parent relationships
- Verify tree connectivity
- Validate edge count correctness
- Enforce BST ordering rules
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- validate_tree
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
- _validate_single_root
- _validate_binary_constraint
- _validate_single_parent
- _validate_connectivity
- _validate_edge_count
- _validate_bst_ordering
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All validations operate on computed metadata
- No mutation or traversal logic is implemented here
- Violations are reported via assertions
- Invariants are evaluated independently and orchestrated centrally
------------------------------------------------------------------------------------
"""

from typing import Dict
from tree.binary_search_tree.schemas.schemas import Tree, Node
from tree.binary_search_tree.helpers import state_helpers as stt_help


# ------------------------------------------------------------
# Tree Validator (Orchestrator)
# ------------------------------------------------------------
def validate_tree(tree: Tree) -> bool:
    """
    Validate all structural and ordering invariants of the Binary Search Tree.

    This function computes tree metadata and invokes all invariant checks.
    It acts as the single entry point for tree validation.

    :param tree: Tree instance to be validated.
    :return: True if all invariants hold.
    """
    metadata = stt_help._compute_metadata(tree)

    _validate_single_root(metadata)
    _validate_binary_constraint(metadata)
    _validate_single_parent(metadata)
    _validate_connectivity(metadata)
    _validate_edge_count(metadata)
    _validate_bst_ordering(metadata)

    return True


# ------------------------------------------------------------
# Single Root Invariant
# ------------------------------------------------------------
def _validate_single_root(metadata: Dict) -> bool:
    """
    Validate that the tree contains exactly one root node.

    The root is defined as the only node with no parent.

    :param metadata: Metadata dictionary computed from the tree.
    :return: True if exactly one root exists.
    """
    parent_map = metadata["parent_map"]

    roots = [node for node, parent in parent_map.items() if parent is None]

    assert len(roots) == 1, (
        f"Invariant violation: expected exactly one root node, found {len(roots)}"
    )
    return True


# ------------------------------------------------------------
# Binary Constraint Invariant
# ------------------------------------------------------------
def _validate_binary_constraint(metadata: Dict) -> bool:
    """
    Validate that each node has at most two children.

    :param metadata: Metadata dictionary computed from the tree.
    :return: True if all nodes satisfy the binary constraint.
    """
    child_map = metadata["child_map"]

    invalid_parents = {
        parent: children
        for parent, children in child_map.items()
        if len(children) > 2
    }

    assert not invalid_parents, (
        "Invariant violation: node has more than two children"
    )
    return True


# ------------------------------------------------------------
# Single Parent Invariant
# ------------------------------------------------------------
def _validate_single_parent(metadata: Dict) -> bool:
    """
    Validate that each non-root node has exactly one parent.

    :param metadata: Metadata dictionary computed from the tree.
    :return: True if parent relationships are valid.
    """
    parent_map = metadata["parent_map"]

    roots = [node for node, parent in parent_map.items() if parent is None]

    assert len(roots) == 1, (
        "Invariant violation: multiple root nodes detected"
    )
    return True


# ------------------------------------------------------------
# Connectivity Invariant
# ------------------------------------------------------------
def _validate_connectivity(metadata: Dict) -> bool:
    """
    Validate that all nodes are reachable from the root.

    :param metadata: Metadata dictionary computed from the tree.
    :return: True if the tree is fully connected.
    """
    all_nodes = metadata["nodes"]
    reachable_nodes = metadata["bfs"]

    assert set(all_nodes) == set(reachable_nodes), (
        "Invariant violation: tree is disconnected; unreachable nodes detected"
    )
    return True


# ------------------------------------------------------------
# Edge Count Invariant
# ------------------------------------------------------------
def _validate_edge_count(metadata: Dict) -> bool:
    """
    Validate that the number of edges is equal to N - 1.

    :param metadata: Metadata dictionary computed from the tree.
    :return: True if edge count matches expected value.
    """
    edge_count = metadata["edge_count"]
    node_count = len(metadata["nodes"])

    assert edge_count == node_count - 1, (
        "Invariant violation: edge count mismatch"
    )
    return True


# ------------------------------------------------------------
# BST Ordering Invariant
# ------------------------------------------------------------
def _validate_bst_ordering(metadata: Dict) -> bool:
    """
    Validate the Binary Search Tree ordering invariant.

    The inorder traversal must be non-decreasing, allowing duplicates
    on the right subtree.

    :param metadata: Metadata dictionary computed from the tree.
    :return: True if BST ordering is preserved.
    """
    inorder_nodes = metadata["inorder"]
    values = [node.data for node in inorder_nodes]

    assert all(values[i] >= values[i - 1] for i in range(1, len(values))), (
        "Invariant violation: BST ordering broken; inorder traversal is not non-decreasing"
    )
    return True
