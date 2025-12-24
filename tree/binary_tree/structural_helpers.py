"""
------------------------------------------------------------------------------------
Module Name: tree_helpers
------------------------------------------------------------------------------------
This module defines **helper utilities** used by tree-level operations for a
Normal Binary Tree.

It provides reusable, low-level helper functions that support insertion,
deletion, traversal, and visualization logic.

This module is responsible for:
- Identifying empty insertion slots
- Finding the deepest rightmost node
- Checking basic tree state
- Supporting traversal mechanics
- Supporting tree visualization

No tree-level operational decisions are made in this module.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Locate next empty insertion slot (level-order)
- Identify deepest rightmost node in the tree
- Check if tree is empty
- Support DFS and BFS traversal mechanics
- Assist tree printing utilities
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- is_tree_empty
- next_empty_slot
- get_deepest_rightmost_node
- dfs_preorder_helper
- dfs_inorder_helper
- dfs_postorder_helper
- bfs_level_order_helper
- print_tree_helper
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
None
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions operate on Tree / Node instances
- No mutation decisions are made here
- No invariant validation is performed
- No I/O or formatting decisions are enforced
- This module contains reusable building blocks only
------------------------------------------------------------------------------------
"""

from typing import List, Any
from schemas import Node, Tree

# ================================================================================
# Tree State Helpers
# ================================================================================
def is_tree_empty(tree: Tree) -> bool:
    """
    Purpose: Check whether the tree is empty
    :param tree: Tree instance
    :return: True if tree is empty, otherwise False
    """
    return tree.root is None


def get_next_empty_slot(level_nodes):
    """
    Purpose: Identify the first node in BFS order that has a missing child
    :param level_nodes: List of nodes at the current BFS level
    :return: Node with an empty left or right child, or None if not found
    """
    if not level_nodes:
        return None

    next_level = []
    for node in level_nodes:
        if node.left is None or node.right is None:
            return node

        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)
        next_level.extend(children)

    return get_next_empty_slot(next_level)


def get_deepest_rightmost_node(tree) -> Node:
    """
    Purpose: Find the deepest rightmost node in the tree
    :param tree: Tree instance
    :return: Deepest rightmost node reference
    """
    if is_tree_empty(tree):
        raise LookupError("Get Rightmost Failed: the tree is empty")
    nodes = _bfs_traverse([tree.root])
    return nodes[-1]


def is_left_child(child: Node, parent: Node) -> bool:
    """
    Purpose: Check whether a node is the left child of a given parent
    :param child: Child node
    :param parent: Parent node
    :return: True if child is left child, otherwise False
    """
    return parent.left == child


def is_right_child(child: Node, parent: Node) -> bool:
    """
    Purpose: Check whether a node is the right child of a given parent
    :param child: Child node
    :param parent: Parent node
    :return: True if child is right child, otherwise False
    """
    return parent.right == child


def search_with_parent(tree: Tree, target_value) -> Node:
    """
    Purpose: Search for a node by value while tracking its parent using BFS
    :param tree: Tree instance
    :param target_value: Value to search for
    :return: parent if success else error
    """
    if is_tree_empty(tree):
        raise LookupError("Search Failed: the tree is empty")

    parent_list = _get_parent([tree.root], target_value)
    if not parent_list:
        raise LookupError("Search Failed: parent not found.")

    parent = parent_list.pop()
    return parent


def delete_leaf_node(tree, node, parent) -> bool:
    """
    Purpose: Delete a leaf node from the binary tree
    :param tree: Tree instance
    :param node: Leaf node to be deleted
    :param parent: Parent of the node
    :return: True if deletion succeeds, otherwise False
    """
    if parent is None:
        tree.root = None
        return True

    if is_left_child(node, parent):
        parent.left = None
        return True
    if is_right_child(node, parent):
        parent.right = None
        return True

    return False


def delete_partial_parent(tree, node, parent):
    """
    Purpose: Delete a node that has exactly one child and promote the child
    :param tree: Tree instance
    :param node: Node to be deleted
    :param parent: Parent of the node
    :return: True if deletion succeeds, otherwise False
    """
    child = node.left if node.left else node.right

    if parent is None:
        tree.root = child
        return True

    if is_left_child(node, parent):
        parent.left = child
        return True

    if is_right_child(node, parent):
        parent.right = child
        return True
    return False


def delete_full_parent(tree, node):
    """
    Purpose: Delete a node with two children using deepest-rightmost replacement
    :param tree: Tree instance
    :param node: Node to be deleted
    :return: True if deletion succeeds
    """
    replace_node = get_deepest_rightmost_node(tree)
    if not replace_node:
        raise LookupError("Delete Failed: deepest rightmost node is not found.")

    replace_parent = search_with_parent(tree, replace_node.data)

    node.data = replace_node.data
    return delete_leaf_node(tree, replace_node, replace_parent)

# ================================================================================
# Tree Property Computation Helpers
# ================================================================================
def compute_size(tree: Tree) -> int:
    """
    Purpose: Compute the total number of nodes in the tree
    :param tree: Tree instance
    :return: Total number of nodes, 0 for empty tree
    """
    if is_tree_empty(tree):
        return 0

    return _bfs_size([tree.root])


def compute_height(tree: Tree, edges: bool = False) -> int:
    """
    Purpose: Compute the height of the tree
    :param tree: Tree instance
    :param edges: If True, compute height in edges; otherwise in levels
    :return: Height of the tree
    """
    if is_tree_empty(tree):
        return -1 if edges else 0

    height = _bfs_height([tree.root])
    return height - 1 if edges else height


def compute_depth(tree, target_value) -> int:
    """
    Purpose: Compute the depth of a given node from the root
    :param tree: Tree instance
    :param target_value: Node value whose depth is to be computed
    :return: Depth of the node
    """
    if is_tree_empty(tree):
        return 0

    # subtract 1 since depth at root is 0
    return _bfs_depth([tree.root], target_value) - 1


def compute_edges(tree: Tree) -> int:
    """
    Purpose: Compute the total number of nodes in the tree
    :param tree: Tree instance
    :return: Total number of edges, 0 for empty tree
    """
    if is_tree_empty(tree):
        return 0

    return _bfs_edges([tree.root])


def compute_bfs_metadata(tree: Tree) -> dict:
    """
    Purpose: Collect BFS-based metadata for the binary tree
    :param tree: List of nodes at the current BFS level
    :return: None
    """
    metadata = {
        "nodes": [],
        "values": [],
        "depth": {},  # Node -> depth (edges)
        "size": 0,
        "edges": 0,
        "height_levels": 0
    }

    metadata = _bfs_metadata([tree.root], 0, metadata)

    # derived values
    metadata["height_edges"] = metadata["height_levels"] - 1 if metadata["size"] > 0 else 0
    metadata["deepest_rightmost"] = metadata["nodes"][-1] if metadata["nodes"] else None

    return metadata


# ================================================================================
# BFS Traversal Helpers
# ================================================================================
def _bfs_search(level_nodes: List[Node], target_value) -> Node:
    """
    Purpose: Assist level-order BFS traversal
    :param level_nodes: nodes at same level (root at the beginning)
    :param target_value: value of target node to be searched
    :return: Traversal result
    """
    if not level_nodes:
        return None

    next_level = []
    for node in level_nodes:
        if node.data == target_value:
            return node

        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        next_level.extend(children)

    return _bfs_search(next_level, target_value)


def _bfs_size(level_nodes: List[Node]) -> int:
    """
    Purpose: Assist level-order BFS traversal
    :param level_nodes: nodes at same level (root at the beginning)
    :return: Traversal result
    """
    if not level_nodes:
        return 0

    total_nodes = 0
    next_level = []
    for node in level_nodes:
        total_nodes += 1
        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        next_level.extend(children)

    return total_nodes + _bfs_size(next_level)


def _bfs_height(level_nodes: List[Node]) -> int:
    """
    Purpose: Assist level-order BFS traversal
    :param level_nodes: nodes at same level (root at the beginning)
    :return: Traversal result
    """
    if not level_nodes:
        return 0

    level = 1
    next_level = []
    for node in level_nodes:
        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        next_level.extend(children)

    return level + _bfs_height(next_level)


def _bfs_depth(level_nodes: List[Node], target_value) -> int:
    """
    Purpose: Assist level-order BFS traversal
    :param level_nodes: nodes at same level (root at the beginning)
    :param target_value: Node value whose depth is to be computed
    :return: Traversal result
    """
    if not level_nodes:
        return 0

    depth = 1
    next_level = []
    for node in level_nodes:
        if node.data == target_value:
            return depth
        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        next_level.extend(children)

    child_depth = _bfs_depth(next_level, target_value)
    if child_depth == 0:
        return 0
    return depth + child_depth


def _bfs_edges(level_nodes: List[Node]) -> int:
    """
    Purpose: Assist level-order BFS traversal
    :param level_nodes: nodes at same level (root at the beginning)
    :return: Traversal result
    """
    if not level_nodes:
        return 0

    edges = 0
    next_level = []
    for node in level_nodes:
        children = []
        if node.left:
            edges += 1
            children.append(node.left)
        if node.right:
            edges += 1
            children.append(node.right)

        next_level.extend(children)
    return edges + _bfs_edges(next_level)


def _bfs_traverse(level_nodes: List[Node]) -> List[Any]:
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
        result.append(node)
        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        next_level.extend(children)

    return result + _bfs_traverse(next_level)


def _bfs_metadata(level_nodes, level_index, metadata):
    """
    Purpose: Collect BFS-based metadata for the binary tree
    :param level_nodes: List of nodes at the current BFS level
    :param level_index: Current BFS level (0-based)
    :param metadata: Dictionary accumulating tree metadata
    :return: None
    """
    if not level_nodes:
        return

    next_level = []

    # height in levels (root level = 1)
    metadata["height_levels"] = max(
        metadata["height_levels"],
        level_index + 1
    )

    for node in level_nodes:
        # record node + value
        metadata["nodes"].append(node)
        metadata["values"].append(node.data)

        # record depth (edges-based)
        metadata["depth"][node] = level_index

        # count node
        metadata["size"] += 1

        # process children and edges
        if node.left:
            metadata["edges"] += 1
            next_level.append(node.left)

        if node.right:
            metadata["edges"] += 1
            next_level.append(node.right)

    # recurse to next BFS level
    return compute_bfs_metadata(next_level, level_index + 1, metadata)


def _get_parent(level_nodes: List[Node], target_value) -> List[Node]:
    """
    Purpose: Perform level-order BFS traversal
    :param level_nodes: nodes at same level (root at beginning)
    :param target_value: target value to be searched
    :return: Traversal result
    """
    if not level_nodes:
        return []

    parent = []
    next_level = []
    for node in level_nodes:
        children = []

        if node.data == target_value:
            return parent

        if node.left is not None or node.left is not None:
            parent.append(node)

        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        next_level.extend(children)

    return parent + _get_parent(next_level, target_value)