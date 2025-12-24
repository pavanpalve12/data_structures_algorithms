"""
------------------------------------------------------------------------------------
Module Name: tree_invariants
------------------------------------------------------------------------------------
This module defines **tree invariant validation logic** for a Normal Binary Tree.

It provides validation functions that verify whether a tree satisfies the
structural and graph-theoretic properties required to be considered a valid
binary tree.

This module is responsible for:
- Validating tree correctness after operations
- Detecting structural violations
- Ensuring parent-child relationships are valid
- Verifying graph invariants such as connectivity and acyclicity

No tree mutation or traversal logic is implemented in this module.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Validate single-root invariant
- Validate parent-child consistency
- Validate child count constraints
- Validate tree connectivity
- Validate edge-count invariant (N - 1 edges)
- Detect structural cycles
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- validate_tree
- validate_single_root
- validate_parent_map
- validate_child_constraints
- validate_connectivity
- validate_edge_count
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
- _build_parent_map
- _count_nodes
- _count_edges
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions operate in read-only mode
- Tree structure must not be mutated
- Parent relationships are derived using traversal
- Validation failures are reported via return values
- No I/O or logging is performed
------------------------------------------------------------------------------------
"""
from typing import List, Dict

from tree.binary_tree.schemas import Node, Tree
import structural_helpers


# ================================================================================
# Public Invariant Validators
# ================================================================================
def validate_tree(tree: Tree) -> bool:
    """
    Purpose: Validate all invariants for a binary tree: Tree
    :param tree: Tree instance
    :return: True if all invariants hold, otherwise False
    """
    assert validate_single_root(tree), (
        "Invariant violated: Multiple roots found."
    )

    assert validate_child_constraints(tree), (
        "Invariant violated: Parents with more than 2 children found."
    )

    assert validate_parent_map(tree), (
        "Invariant violated: Children with multiple parents found."
    )

    assert validate_connectivity(tree), (
        "Invariant violated: Disconnected nodes found."
    )

    assert validate_edge_count(tree), (
        "Invariant violated: Extra nodes found."
    )
    return True


def validate_single_root(tree: Tree) -> bool:
    """
    Purpose: Validate that exactly one root node exists
    :param tree: Tree instance
    :return: True if single root invariant holds, otherwise False
    """
    parent_map = _build_parent_map([tree.root], {})

    invalid_root_nodes = {
        child: parents for child, parents in parent_map.items()
        if not parents
    }

    assert len(invalid_root_nodes) == 1, (
        "Invariant violated: multiple root nodes present in the tree."
    )
    return True


def validate_parent_map(tree: Tree) -> bool:
    """
    Purpose: Validate that each non-root node has exactly one parent
    :param tree: Tree instance
    :return: True if parent mapping is valid, otherwise False
    """
    parent_map = _build_parent_map([tree.root], {})

    invalid_children = {
        child: parents for child, parents in parent_map.items()
        if len(parents) > 1
    }

    assert len(invalid_children) == 0, (
        "Invariant violated: there are nodes with multiple parents. "
    )
    return True


def validate_child_constraints(tree: Tree) -> bool:
    """
    Purpose: Validate that each node has at most two children
    :param tree: Tree instance
    :return: True if child constraints hold, otherwise False
    """
    child_map = _build_child_map([tree.root], {})

    invalid_parents = {
        parent: children for parent, children in child_map.items()
        if len(children) > 2
    }

    assert len(invalid_parents) == 0, (
        "Invariant violated: there are parents with more than 2 children."
    )
    return True


def validate_connectivity(tree: Tree) -> bool:
    """
    Purpose: Validate that all nodes are reachable from the root
    :param tree: Tree instance
    :return: True if tree is fully connected, otherwise False
    """
    parent_map = _build_parent_map([tree.root], {})

    all_nodes = parent_map.keys()
    reachable_nodes = structural_helpers._bfs_traverse([tree.root])
    reachable_nodes_values = [node.data for node in reachable_nodes]

    assert set(reachable_nodes_values) == set(all_nodes), (
        "Invariant violated: there are disconnected nodes in tree."
    )

    return True


def validate_edge_count(tree: Tree) -> bool:
    """
    Purpose: Validate that the tree has exactly N - 1 edges
    :param tree: Tree instance
    :return: True if edge count invariant holds, otherwise False
    """
    parent_map = _build_parent_map([tree.root], {})
    edges_count = structural_helpers.compute_edges(tree)

    all_nodes = parent_map.keys()

    assert len(all_nodes) - 1 == edges_count, (
        "Invariant Violated: Extra edges found in the tree."
    )

    return True

# ================================================================================
# Internal Helpers (Invariant Support)
# ================================================================================
def _build_parent_map(level_nodes: List[Node], parent_map: Dict) -> Dict:
    """
    Purpose: Build a mapping of child node to parent node using BFS traversal
    :param level_nodes: List of nodes at the current BFS level
    :param parent_map: Dictionary mapping node -> parent (root maps to None)
    :return: Updated parent_map dictionary
    """
    if not level_nodes:
        return parent_map

    next_level = []
    for node in level_nodes:
        children = []

        if node.data not in parent_map:
            parent_map[node.data] = []

        if node.left:
            children.append(node.left)
            parent_map[node.left.data] = [node.data]

        if node.right:
            children.append(node.right)
            parent_map[node.right.data] = [node.data]

        next_level.extend(children)

    return _build_parent_map(next_level, parent_map)


def _build_child_map(level_nodes: List[Node], child_map: Dict) -> Dict:
    """
    Purpose: Build a mapping of parent node to its children using BFS traversal
    :param level_nodes: List of nodes at the current BFS level
    :param child_map: Dictionary mapping parent_value -> list of child_values
    :return: Updated child_map dictionary
    """
    if not level_nodes:
        return child_map

    next_level = []
    for node in level_nodes:
        children = []

        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        child_map[node.data] = [child.data for child in children]
        next_level.extend(children)

    return _build_child_map(next_level, child_map)
