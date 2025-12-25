from typing import Optional

from tree.binary_search_tree.helpers import (
    structural_helpers as str_help,
    invariant_helpers as inv_help
)
from tree.binary_search_tree.schemas.schemas import Tree, Node


# --------------------------------------------------------------------------
# Core Operations
# --------------------------------------------------------------------------
def insert_node(tree: Tree, new_node: Node) -> bool:
    if str_help._is_empty_tree(tree):
        tree.root = new_node
        return True

    return _insert(tree.root, new_node)


def delete_node(tree: Tree, value) -> bool:
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
    if str_help.is_empty_tree(tree):
        return None
    return _search(tree.root, target_value)


# --------------------------------------------------------------------------
# Internal helpers
# --------------------------------------------------------------------------
def _search(node: Node, target_value) -> Optional[Node]:
    if node is None:
        return None

    if target_value == node.data:
        return node

    if target_value < node.data:
        return _search(node.left, target_value)
    else:
        return _search(node.right, target_value)


def _insert(node: Node, new_node: Node):
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


def _delete_leaf_node(node: Node, parent:Node) -> bool:
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

    target_node.data = successor.data

    if successor.right is None:
        return _delete_leaf_node(successor, successor_parent)
    else:
        return _delete_partial_parent(successor, successor_parent)


def _delete_partial_parent(node: Node, parent: Node) -> bool:
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
