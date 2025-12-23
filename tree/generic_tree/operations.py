"""
------------------------------------------------------------------------------------
Module: tree_operations
------------------------------------------------------------------------------------

State-mutating operations and traversal algorithms for a generic tree.

This module operates directly on Tree and Node objects and is invoked
exclusively through the TreeAPI layer.

Design goals:
- Stateless functional operations
- No user interaction
- Centralized mutation logic
------------------------------------------------------------------------------------
"""

from typing import Any, Optional, List
from schemas import Tree, Node
import helpers


def insert_node(tree: Tree, child_data: Any, parent_data: Any) -> None:
    """
    Insert a new node under a specified parent.

    :param tree: Tree instance to modify
    :param child_data: Value for the new child node
    :param parent_data: Value identifying the parent node
    """
    if child_data is None or parent_data is None:
        raise ValueError("Insert Failed: parent or child data is None.")
    if helpers.is_tree_empty(tree):
        raise LookupError("Insert Failed: the tree is empty.")

    parent_node = search_node(tree, parent_data)
    if parent_node is None:
        raise LookupError("Insert Failed: parent node not found.")

    child_node = Node(child_data)
    parent_node.children.append(child_node)
    child_node.parent = parent_node

    helpers.check_invariants(tree)


def delete_node(tree: Tree, target_data: Any) -> None:
    """
    Delete a node and its entire subtree.

    :param tree: Tree instance to modify
    :param target_data: Value identifying the node to delete
    """
    if target_data is None:
        raise ValueError("Delete Failed: target data is None.")
    if helpers.is_tree_empty(tree):
        raise LookupError("Delete Failed: tree is empty.")

    target_node = search_node(tree, target_data)
    if target_node is None:
        raise LookupError("Delete Failed: target node not found.")

    if tree.root == target_node:
        tree.root = None
        return

    parent = target_node.parent
    parent.children.remove(target_node)
    target_node.parent = None

    helpers.check_invariants(tree)


def search_node(tree: Tree, target_data: Any) -> Optional[Node]:
    """
    Search for a node by value using BFS.

    :param tree: Tree instance
    :param target_data: Value identifying the node
    :return: Matching Node if found, else None
    """
    if target_data is None:
        raise ValueError("Search Failed: target data is None.")
    if helpers.is_tree_empty(tree):
        raise LookupError("Search Failed: the tree is empty.")

    return helpers._bfs_search([tree.root], target_data)


def dfs_preorder(node: Optional[Node]) -> list[Any]:
    """
    Perform preorder depth-first traversal.

    :param node: Root node of the subtree
    :return: List of node values
    """
    if node is None:
        return []

    result = [node.data]
    for child in node.children:
        result.extend(dfs_preorder(child))
    return result


def dfs_postorder(node: Optional[Node]) -> list[Any]:
    """
    Perform postorder depth-first traversal.

    :param node: Root node of the subtree
    :return: List of node values
    """
    if node is None:
        return []

    result = []
    for child in node.children:
        result.extend(dfs_postorder(child))
    result.append(node.data)
    return result


def bfs_traversal(nodes: List[Node]) -> list[Any]:
    """
    Perform breadth-first (level-order) traversal.

    :param nodes: Nodes at the current BFS level
    :return: List of node values in BFS order
    """
    if not nodes:
        return []

    result = []
    next_level = []

    for node in nodes:
        result.append(node.data)
        next_level.extend(node.children)

    result.extend(bfs_traversal(next_level))
    return result
