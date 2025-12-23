"""
------------------------------------------------------------------------------------
Module Name: tree_operations
------------------------------------------------------------------------------------
This module implements **tree-level operational logic** for a Normal Binary Tree.

It defines the core operations that mutate or query the tree structure while
delegating all low-level mechanics to the helpers module.

This module is responsible for:
- Tree insertion logic
- Tree deletion logic
- Tree search logic
- Tree traversal orchestration

No helper utilities or invariant validation logic is implemented here.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Insert nodes into the tree
- Delete nodes from the tree
- Search nodes in the tree
- Coordinate DFS and BFS traversals
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- initialize_tree
- insert_node
- delete_node
- search_node
- dfs_preorder
- dfs_inorder
- dfs_postorder
- bfs_level_order
- print_tree
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
None

(All helper utilities are defined in structural_helpers.py)
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions operate on TreeAPI / Tree instances
- Low-level traversal mechanics are delegated to helpers
- No invariant checks are performed here
- No I/O or formatting logic exists in this module
------------------------------------------------------------------------------------
"""
from typing import List, Any

import visual_helpers, structural_helpers
from tree.binary_tree.schemas import Tree, Node


# ================================================================================
# Core Operations
# ================================================================================
def insert_node(tree_api, value) -> None:
    """
    Purpose: Insert a value into the binary tree
    :param tree_api: TreeAPI instance
    :param value: Value to be inserted
    :return: None
    """
    pass


def delete_node(tree_api, value) -> None:
    """
    Purpose: Delete a value from the binary tree
    :param tree_api: TreeAPI instance
    :param value: Value to be deleted
    :return: None
    """
    pass


def search_node(tree: Tree, target_value) -> Node:
    """
    Purpose: Search for a value in the binary tree
    :param tree: TreeAPI instance
    :param target_value: Value to search for
    :return: Node if value exists, otherwise Error
    """
    if structural_helpers.is_tree_empty(tree):
        raise LookupError("Search Failed: the tree is empty.")

    target_node = structural_helpers.bfs_search([tree.root], target_value)

    if target_node is None:
        raise LookupError("Search Failed: the node is not found.")

    return target_node

# ================================================================================
# DFS Traversals
# ================================================================================
def dfs_preorder(node: Node) -> List[Any]:
    """
    Purpose: Perform preorder DFS traversal
    :param node: root node of tree
    :return: Traversal result
    root -> left -> right
    """
    if node is None:
        return []

    result = [node.data]
    if node.left:
        result.extend(dfs_preorder(node.left))
    if node.right:
        result.extend(dfs_preorder(node.right))

    return result

def dfs_inorder(node: Node) -> List[Any]:
    """
    Purpose: Perform inorder DFS traversal
    :param node: root node of tree
    :return: Traversal result
    left -> root -> right
    """
    if node is None:
        return []

    result = []
    if node.left:
        result.extend(dfs_inorder(node.left))

    result.append(node.data)

    if node.right:
        result.extend(dfs_inorder(node.right))

    return result

def dfs_postorder(node: Node) -> List[Any]:
    """
    Purpose: Perform postorder DFS traversal
    :param node: root node of tree
    :return: Traversal result
    left -> right -> root
    """
    if node is None:
        return []

    result = []
    if node.left:
        result.extend(dfs_postorder(node.left))
    if node.right:
        result.extend(dfs_postorder(node.right))

    result.append(node.data)
    return result


# ================================================================================
# BFS Traversal
# ================================================================================
def bfs_level_order(level_nodes: List[Node]) -> List[Any]:
    """
    Purpose: Perform level-order BFS traversal
    :param level_nodes: nodes at same level (root at beginning)
    :return: Traversal result
    """
    if not level_nodes:
        return []

    result = []
    next_level = []
    for node in level_nodes:
        result.append(node.data)
        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        next_level.extend(children)

    return result + bfs_level_order(next_level)


# ================================================================================
# Utilities
# ================================================================================
def print_tree(tree: Tree) -> None:
    """
    Purpose: Print tree structure
    :param tree: Tree instance
    :return: None
    """
    return visual_helpers.print_tree(tree)
