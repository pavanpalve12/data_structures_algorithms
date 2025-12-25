"""
------------------------------------------------------------------------------------
Module Name: traversal_operations
------------------------------------------------------------------------------------
This module implements **tree traversal orchestration** for a Binary Search Tree
(BST).

It exposes a unified traversal interface that supports depth-first and
breadth-first traversals by leveraging precomputed tree metadata.

This module does not implement traversal mechanics directly for public use;
instead, it relies on metadata computed via state helpers to ensure consistency
and correctness across traversals.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Expose DFS traversals (preorder, inorder, postorder)
- Expose BFS (level-order) traversal
- Convert traversal results into user-friendly output
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- bst_traverse
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
- _preorder
- _inorder
- _postorder
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Traversal results are derived from computed metadata
- No tree mutation is performed
- Traversal helpers are recursive and node-based
- Output is formatted as node values for API consumers
------------------------------------------------------------------------------------
"""

from typing import List

from tree.binary_search_tree.helpers import (
    state_helpers as stt_help,
    structural_helpers as str_help
)
from tree.binary_search_tree.schemas.schemas import Tree, Node


# --------------------------------------------------------------------------
# Traversals
# --------------------------------------------------------------------------
def bst_traverse(tree: Tree, traverse_type: str = "preorder") -> List:
    """
    Perform a traversal of the Binary Search Tree.

    Supported traversal types include:
    - preorder
    - inorder
    - postorder
    - bfs

    :param tree: Tree instance to traverse.
    :param traverse_type: Type of traversal to perform.
    :return: List of node values in the specified traversal order.
    :raises ValueError: If the tree is empty.
    """
    if str_help._is_empty_tree(tree):
        raise ValueError(f"{traverse_type} Traverse Failed: bst is empty.")

    metadata = stt_help._compute_metadata(tree)
    result = metadata[traverse_type]
    result = [str(node.data) for node in result]
    return result


# --------------------------------------------------------------------------
# Internal helpers
# --------------------------------------------------------------------------

def _preorder(node: Node) -> List[Node]:
    """
    Perform a preorder depth-first traversal.

    Traversal order: root → left → right

    :param node: Root node of the current subtree.
    :return: List of nodes in preorder sequence.
    """
    if node is None:
        return []

    result = [node]
    if node.left:
        result.extend(_preorder(node.left))
    if node.right:
        result.extend(_preorder(node.right))

    return result


def _postorder(node: Node) -> List[Node]:
    """
    Perform a postorder depth-first traversal.

    Traversal order: left → right → root

    :param node: Root node of the current subtree.
    :return: List of nodes in postorder sequence.
    """
    if node is None:
        return []

    result = []
    if node.left:
        result.extend(_postorder(node.left))
    if node.right:
        result.extend(_postorder(node.right))
    result.append(node)
    return result


def _inorder(node: Node) -> List[Node]:
    """
    Perform an inorder depth-first traversal.

    Traversal order: left → root → right

    :param node: Root node of the current subtree.
    :return: List of nodes in inorder sequence.
    """
    if node is None:
        return []

    result = []
    if node.left:
        result.extend(_inorder(node.left))

    result.append(node)

    if node.right:
        result.extend(_inorder(node.right))

    return result
