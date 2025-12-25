"""
------------------------------------------------------------------------------------
Module Name: core_operations
------------------------------------------------------------------------------------
This module implements **core mutation and query operations** for a Binary
Search Tree (BST).

It defines the primary algorithms responsible for modifying and accessing the
tree structure, including insertion, deletion, and search. All operations
adhere strictly to BST ordering rules and delegate structural mechanics to
helper modules.

This module is responsible for:
- Inserting nodes into the BST
- Deleting nodes from the BST (all cases)
- Searching nodes using ordered traversal

Invariant validation is triggered after mutation operations but is not
implemented here.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Insert nodes following BST ordering rules
- Delete nodes (leaf, one-child, two-children, root)
- Search nodes using ordered recursion
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- insert_node
- delete_node
- search_node
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
- _search
- _insert
- _delete_leaf_node
- _delete_partial_parent
- _delete_full_parent
- _delete_root
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All mutations preserve BST ordering
- Duplicate values are inserted into the right subtree
- Helper functions encapsulate specific delete cases
- Invariants are validated after every mutation
------------------------------------------------------------------------------------
"""

from typing import Optional

from tree.binary_search_tree.helpers import (
    structural_helpers as str_help
)
from tree.binary_search_tree.invariants import invariants_operations as inv_help
from tree.binary_search_tree.schemas.schemas import Tree, Node


# --------------------------------------------------------------------------
# Core Operations
# --------------------------------------------------------------------------
def insert_node(tree: Tree, new_node: Node) -> bool:
    """
    Insert a new node into the Binary Search Tree.

    :param tree: Tree instance into which the node is to be inserted.
    :param new_node: Node to be inserted.
    :return: True if insertion succeeds.
    """
    if str_help._is_empty_tree(tree):
        tree.root = new_node
        return True

    return _insert(tree.root, new_node)


def delete_node(tree: Tree, value) -> bool:
    """
    Delete a node with the given value from the Binary Search Tree.

    This function handles all deletion cases, including:
    - deleting a leaf node
    - deleting a node with one child
    - deleting a node with two children
    - deleting the root node

    :param tree: Tree instance from which the node is to be deleted.
    :param value: Value of the node to be deleted.
    :return: True if deletion succeeds, False otherwise.
    """
    if str_help._is_empty_tree(tree):
        return False

    target_node = search_node(tree, value)

    if target_node is None:
        return False

    if target_node == tree.root:
        _delete_root(tree, tree.root)
        inv_help.validate_tree(tree)
        return True

    parent = str_help._get_parent(tree.root, target_node)

    if target_node.left is not None and target_node.right is not None:
        successor = str_help._get_inorder_successor(target_node)
        successor_parent = str_help._get_parent(tree.root, successor)

        _delete_full_parent(target_node, successor, successor_parent)

    elif target_node.left is None and target_node.right is None:
        _delete_leaf_node(target_node, parent)

    else:
        _delete_partial_parent(target_node, parent)

    inv_help.validate_tree(tree)
    return True


def search_node(tree: Tree, target_value) -> Optional[Node]:
    """
    Search for a node with the given value in the Binary Search Tree.

    :param tree: Tree instance to search.
    :param target_value: Value to search for.
    :return: Node containing the value if found, otherwise None.
    """
    if str_help._is_empty_tree(tree):
        return None
    return _search(tree.root, target_value)


# --------------------------------------------------------------------------
# Internal helpers
# --------------------------------------------------------------------------
def _search(node: Node, target_value) -> Optional[Node]:
    """
    Recursively search for a value in the BST using ordered traversal.

    :param node: Current node in the recursive search.
    :param target_value: Value being searched for.
    :return: Node containing the value if found, otherwise None.
    """
    if node is None:
        return None

    if target_value == node.data:
        return node

    if target_value < node.data:
        return _search(node.left, target_value)
    else:
        return _search(node.right, target_value)


def _insert(node: Node, new_node: Node):
    """
    Recursively insert a new node into the BST following ordering rules.

    Duplicate values are inserted into the right subtree.

    :param node: Current node in the recursive insertion.
    :param new_node: Node to be inserted.
    :return: True if insertion succeeds.
    """
    if new_node.data < node.data:
        if node.left is None:
            node.left = new_node
            return True
        else:
            return _insert(node.left, new_node)
    else:
        if node.right is None:
            node.right = new_node
            return True
        else:
            return _insert(node.right, new_node)


def _delete_leaf_node(node: Node, parent: Node) -> bool:
    """
    Delete a leaf node from the BST.

    :param node: Leaf node to be deleted.
    :param parent: Parent of the leaf node.
    :return: True if deletion succeeds.
    """
    if parent.left == node:
        parent.left = None
    else:
        parent.right = None
    return True


def _delete_full_parent(
        target_node: Node,
        successor: Node,
        successor_parent: Node
) -> bool:
    """
    Delete a node with two children by replacing its value with its
    inorder successor and deleting the successor node.

    :param target_node: Node being deleted.
    :param successor: Inorder successor of the target node.
    :param successor_parent: Parent of the inorder successor.
    :return: True if deletion succeeds.
    """
    target_node.data = successor.data

    if successor.right is None:
        return _delete_leaf_node(successor, successor_parent)
    else:
        return _delete_partial_parent(successor, successor_parent)


def _delete_partial_parent(node: Node, parent: Node) -> bool:
    """
    Delete a node with exactly one child by promoting its child.

    :param node: Node to be deleted.
    :param parent: Parent of the node.
    :return: True if deletion succeeds.
    """
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if parent.left == node:
        parent.left = child
    else:
        parent.right = child
    return True


def _delete_root(tree: Tree, node: Node) -> bool:
    """
    Delete the root node of the BST.

    This function handles all root deletion cases:
    - root is a leaf
    - root has one child
    - root has two children

    :param tree: Tree instance whose root is to be deleted.
    :param node: Root node.
    :return: True if deletion succeeds.
    """
    # root is leaf
    if node.left is None and node.right is None:
        tree.root = None
        return True

    # root has one child
    if node.left is None or node.right is None:
        tree.root = node.left if node.left else node.right
        inv_help.validate_tree(tree)
        return True

    # root has two children
    successor = str_help._get_inorder_successor(node)
    successor_parent = str_help._get_parent(tree.root, successor)

    node.data = successor.data

    if successor.right is None:
        _delete_leaf_node(successor, successor_parent)
    else:
        _delete_partial_parent(successor, successor_parent)

    return True
