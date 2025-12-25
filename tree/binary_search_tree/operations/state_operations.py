"""
------------------------------------------------------------------------------------
Module Name: state_operations
------------------------------------------------------------------------------------
This module implements **tree state computation operations** for a Binary
Search Tree (BST).

It provides read-only utilities to compute various properties of the tree
such as height, size, depth, edge count, and extremal values. All computations
are derived dynamically using tree metadata and do not mutate the tree.

This module relies on helper utilities to compute metadata and does not
implement traversal or structural logic directly.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Compute tree height (levels or edges)
- Compute total node count (size)
- Compute depth of nodes
- Compute total edge count
- Identify minimum and maximum values in the tree
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- compute_height
- compute_size
- compute_depth
- compute_edges
- compute_min_node
- compute_max_node
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
None

(All metadata computation is delegated to state_helpers)
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All operations are read-only
- Tree is treated as stateless (no cached properties)
- Metadata is recomputed on demand
- Errors are raised for empty tree scenarios
------------------------------------------------------------------------------------
"""

from typing import Dict, Any

from tree.binary_search_tree.helpers import (
    structural_helpers as str_help,
    state_helpers as stt_help
)
from tree.binary_search_tree.schemas.schemas import Tree


# --------------------------------------------------------------------------
# State Operations
# --------------------------------------------------------------------------
def compute_height(tree: Tree, edges: bool = False) -> int:
    """
    Compute the height of the Binary Search Tree.

    Height can be computed either in terms of levels or edges.

    :param tree: Tree instance whose height is to be computed.
    :param edges: If True, return height in terms of edges;
                  otherwise, return height in terms of levels.
    :return: Height of the tree.
    :raises ValueError: If the tree is empty.
    """
    if str_help._is_empty_tree(tree):
        raise ValueError("Height Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["height_levels"] if not edges else metadata["height_edges"]


def compute_size(tree: Tree) -> int:
    """
    Compute the total number of nodes in the Binary Search Tree.

    :param tree: Tree instance whose size is to be computed.
    :return: Number of nodes in the tree.
    :raises ValueError: If the tree is empty.
    """
    if str_help._is_empty_tree(tree):
        raise ValueError("Size Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["size"]


def compute_depth(tree: Tree, value) -> Dict:
    """
    Compute the depth of nodes matching a given value in the Binary Search Tree.

    Depth is measured in terms of edges from the root node.

    :param tree: Tree instance to analyze.
    :param value: Value of the node(s) whose depth is to be computed.
    :return: String representation of matching node depths.
    :raises ValueError: If the tree is empty.
    """
    if str_help._is_empty_tree(tree):
        raise ValueError("Depth Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    depth_map = metadata["depth_map"]

    result = ', '.join(
        [
            res for res in
            {
                f"{node.data} → {level}"
                for node, level in depth_map.items()
                if node.data == value
            }
        ]
    )
    return result


def compute_edges(tree: Tree) -> int:
    """
    Compute the total number of edges in the Binary Search Tree.

    :param tree: Tree instance whose edge count is to be computed.
    :return: Number of edges in the tree.
    :raises ValueError: If the tree is empty.
    """
    if str_help._is_empty_tree(tree):
        raise ValueError("Depth Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["edge_count"]


def compute_min_node(tree: Tree) -> Any:
    """
    Retrieve the minimum value stored in the Binary Search Tree.

    :param tree: Tree instance to analyze.
    :return: Minimum value in the tree.
    :raises ValueError: If the tree is empty.
    """
    if str_help._is_empty_tree(tree):
        raise ValueError("Depth Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["min_node"].data


def compute_max_node(tree: Tree) -> Any:
    """
    Retrieve the maximum value stored in the Binary Search Tree.

    :param tree: Tree instance to analyze.
    :return: Maximum value in the tree.
    :raises ValueError: If the tree is empty.
    """
    if str_help._is_empty_tree(tree):
        raise ValueError("Depth Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["max_node"].data
