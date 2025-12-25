"""
------------------------------------------------------------------------------------
Module Name: structural_helpers
------------------------------------------------------------------------------------
This module implements **low-level structural helper utilities** for the
Binary Search Tree (BST).

It contains reusable, focused helper functions that operate directly on
Node and Tree structures and are shared across operations, state computation,
and invariant validation modules.

This module is intentionally free of:
- Business logic
- Traversal orchestration
- Invariant enforcement
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Identify empty tree state
- Resolve parent relationships between nodes
- Locate inorder successor for BST deletion
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- _is_empty_tree
- _get_parent
- _get_inorder_successor
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
None
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions are stateless and side-effect free
- All helpers assume valid BST structure
- Ordering-based navigation is used (not traversal-based)
- Used by core operations and state computation
------------------------------------------------------------------------------------
"""

from tree.binary_search_tree.schemas.schemas import Node, Tree


def _is_empty_tree(tree: Tree) -> bool:
    """
    Check whether the given tree is empty.

    :param tree: Tree instance to be checked.
    :return: True if the tree has no root node, False otherwise.
    """
    return tree.root is None


def _get_parent(node: Node, target_node: Node):
    """
    Find the parent of a given target node in the BST.

    This function navigates the tree using BST ordering rules to locate
    the parent of the specified target node.

    :param node: Current node in the recursive search.
    :param target_node: Node whose parent is to be found.
    :return: Parent node if found, otherwise None.
    """
    if node is None:
        return None

    if node.left == target_node or node.right == target_node:
        return node

    if target_node.data < node.data:
        return _get_parent(node.left, target_node)
    else:
        return _get_parent(node.right, target_node)


def _get_inorder_successor(node: Node):
    """
    Find the inorder successor of a given node in the BST.

    The inorder successor is defined as the leftmost node in the
    right subtree of the given node.

    :param node: Node whose inorder successor is to be found.
    :return: Inorder successor node if it exists, otherwise None.
    """
    if node is None or node.right is None:
        return None

    current = node.right

    while current.left is not None:
        current = current.left
    return current
