from typing import Dict
from tree.binary_search_tree.schemas.schemas import Tree, Node
from tree.binary_search_tree.helpers import state_helpers as stt_help

# ------------------------------------------------------------
# Tree Validator (Orchestrator)
# ------------------------------------------------------------
def validate_tree(tree: Tree) -> bool:
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
    inorder_nodes = metadata["inorder"]
    values = [node.data for node in inorder_nodes]

    assert all(values[i] >= values[i - 1] for i in range(1, len(values))), (
        "Invariant violation: BST ordering broken; inorder traversal is not non-decreasing"
    )
    return True
