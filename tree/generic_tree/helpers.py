"""
------------------------------------------------------------------------------------
Module: tree_helpers
------------------------------------------------------------------------------------

Helper utilities for tree validation, property computation,
and human-readable output.

This module contains no tree mutation logic.
------------------------------------------------------------------------------------
"""

from functools import wraps
from typing import List, Any
from schemas import Tree, Node
import operations


def pretty_print(func):
    """
    Decorator for formatted tree printing.

    Prints:
    - Tree header
    - BFS traversal output
    - Tree metadata (root, size, height)
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tree = args[0]
        if tree.root is None:
            print("Tree is empty.")
            return

        meta_lines = _get_metadata_strings(tree)
        max_left = max((len(left) for left, _ in meta_lines), default=0)

        title = " Tree "
        width = 50
        print(title.center(width, "="))

        func(*args, **kwargs)

        print("-" * width)
        print("\tNote:\n\t - Parent → Children\n\t - leaf node → **")
        print("-" * width)

        for left, right in meta_lines:
            print(f"\t{left.ljust(max_left)} → {right}")

        print("=" * width)
    return wrapper


def is_tree_empty(tree: Tree) -> bool:
    """
    Check whether the tree is empty.

    :param tree: Tree instance
    :return: True if tree has no root
    """
    return tree.root is None


def compute_height(tree: Tree, edges: bool = False) -> int:
    """
    Compute the height of the tree.

    :param tree: Tree instance
    :param edges: Measure height in edges if True, else in levels
    :return: Height value
    """
    if is_tree_empty(tree):
        return -1 if edges else 0

    level = _bfs_height([tree.root])
    return level - 1 if edges else level


def compute_depth(tree: Tree, target_node_data: Any, edges: bool = False) -> int:
    """
    Compute the depth of a node identified by value.

    :param tree: Tree instance
    :param target_node_data: Node value
    :param edges: Measure depth in edges if True, else in levels
    :return: Depth value
    """
    if is_tree_empty(tree):
        raise LookupError("Compute Depth Failed: the tree is empty.")

    level = _bfs_depth([tree.root], target_node_data)
    return level - 1 if edges else level


def compute_size(tree: Tree) -> int:
    """
    Compute the total number of nodes in the tree.

    :param tree: Tree instance
    :return: Node count
    """
    return 0 if is_tree_empty(tree) else _dfs_size(tree.root)


def check_invariants(tree: Tree) -> bool:
    """
    Validate structural invariants of the tree.

    Enforces:
    - exactly one root
    - connectivity
    - unique node values
    - exactly one parent per non-root node
    - total edges = nodes - 1
    """
    parent_map = _get_node_parent_relationships(tree.root, {})
    root_nodes = [k for k, v in parent_map.items() if not v]
    assert len(root_nodes) == 1

    all_nodes = set(parent_map.keys())
    reachable = operations.dfs_preorder(tree.root)

    assert len(reachable) == len(set(reachable))
    assert set(reachable) == all_nodes

    assert all(len(v) <= 1 for v in parent_map.values())

    total_edges = sum(len(v) for v in parent_map.values())
    assert total_edges == len(all_nodes) - 1

    return True


@pretty_print
def bfs_print(tree: Tree) -> None:
    """
    Print the tree using breadth-first traversal.
    """
    _bfs_print([tree.root], 0)


def _bfs_print(nodes: List[Node], level: int) -> None:
    if not nodes:
        return

    next_level = []
    for node in nodes:
        children = ", ".join(c.data for c in node.children) if node.children else "**"
        print(f"\tLevel {level}: {node.data} → {children}")
        next_level.extend(node.children)

    _bfs_print(next_level, level + 1)


def _get_node_parent_relationships(node: Node, parent_map: dict) -> dict:
    if node is None:
        return parent_map

    parent_map[node.data] = [] if node.parent is None else [node.parent.data]
    for child in node.children:
        _get_node_parent_relationships(child, parent_map)
    return parent_map


def _bfs_height(nodes: List[Node], level: int = 0) -> int:
    if not nodes:
        return level
    return _bfs_height([c for n in nodes for c in n.children], level + 1)


def _bfs_depth(nodes: List[Node], target: Any, level: int = 0) -> int:
    if not nodes:
        raise LookupError("Compute Depth Failed: target node not found.")

    for node in nodes:
        if node.data == target:
            return level

    return _bfs_depth([c for n in nodes for c in n.children], target, level + 1)


def _dfs_size(node: Node) -> int:
    return 1 + sum(_dfs_size(c) for c in node.children)


def _bfs_search(nodes: List[Node], target: Any) -> Optional[Node]:
    if not nodes:
        return None

    for node in nodes:
        if node.data == target:
            return node

    return _bfs_search([c for n in nodes for c in n.children], target)


def _get_metadata_strings(tree: Tree) -> list[tuple[str, str]]:
    return [
        ("Root Node", str(tree.root.data)),
        ("Size", str(compute_size(tree))),
        ("Height (Levels)", str(compute_height(tree))),
        ("Height (Edges)", str(compute_height(tree, edges=True))),
    ]
